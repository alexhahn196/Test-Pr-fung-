"""Benchmarks for content pillars (Teil 24) and AI-only style contrasts (Teil 23).

Source: 04_reel_database.csv (same reels/codes as the digest; adj_factor = views vs. expectation for
account size on the same topic page). All groupings are post-hoc proxies for the pillars, NOT the
pillars themselves -> treat as explorative. Topic pages show TOP reels (selection bias): absolute
views are benchmarks of reels that reached a topic page, not expectations for a new account.

Outputs:
  data/processed/stats/pillar_benchmarks.csv   (views quantiles, adj_factor, viral share, rates per proxy segment)
  data/processed/stats/ai_style_contrasts.csv  (AI-only contrasts: median ratio, 95 % bootstrap CI, Mann-Whitney p)
  data/processed/stats/ai_segments.csv         (AI-only segment medians per dimension: room, style, landscape, light ...)
Bootstrap: 2,000 resamples, seed 7 (same convention as key_contrasts.py).
"""
import os

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "processed", "stats")
RNG = np.random.default_rng(7)

TRANSFORM_RX = (r"before|after|transform|from (?:an )?(?:empty|abandoned|old|raw|nothing)|makeover|renovat|"
                r"build(?:ing)? (?:a|my|the)|turned .* into|construction|timelapse")


def load():
    d = pd.read_csv(os.path.join(ROOT, "04_reel_database.csv"))
    d["is_ai"] = d["production"] == "ai_generated"
    d["cap"] = d["caption_full"].fillna("").str.lower()
    d["transform_kw"] = d["cap"].str.contains(TRANSFORM_RX, regex=True)
    for c in ["topic_groups", "ambience_fx", "cover_hooks", "materials"]:
        d[c] = d[c].fillna("")
    return d


def segments(d):
    ai = d["is_ai"]
    tg = d["topic_groups"]
    return {
        "P1 | all fantasy_impossible": d["realism"] == "fantasy_impossible",
        "P1 | AI fantasy_impossible": ai & (d["realism"] == "fantasy_impossible"),
        "P1 | AI unusual_structure": ai & (d["building_type"] == "unusual_structure"),
        "P1 | topic group architecture": tg.str.contains("architecture"),
        "P1 | AI mountain or ocean_beach setting": ai & d["landscape"].isin(["mountain", "ocean_beach"]),
        "P1 | AI cliff setting": ai & (d["landscape"] == "cliff"),
        "P2 | all choice hook": d["caption_hook_category"] == "choice",
        "P2 | AI choice hook": ai & (d["caption_hook_category"] == "choice"),
        "P3 | AI garden/terrace/pool/bath/stairs": ai & d["room_primary"].isin(["garden_landscape", "terrace_outdoor", "pool", "bathroom", "stairs_hall"]),
        "P3 | AI transformation caption keywords (explorative)": ai & d["transform_kw"],
        "P3 | all empty_room cover": d["cover_hooks"].str.contains("empty_room"),
        "P3 | all before_after_split cover": d["cover_hooks"].str.contains("before_after_split"),
        "P4 | all night_artificial": d["lighting"] == "night_artificial",
        "P4 | AI night_artificial": ai & (d["lighting"] == "night_artificial"),
        "P4 | AI night_artificial + people": ai & (d["lighting"] == "night_artificial") & (d["people_present"] == True),  # noqa: E712
        "P4 | AI city_lights fx": ai & d["ambience_fx"].str.contains("city_lights"),
        "P4 | AI city_skyline setting": ai & (d["landscape"] == "city_skyline"),
        "P4 | all penthouse": d["building_type"] == "penthouse",
        "P5 | all cozy_ambience topic group": tg.str.contains("cozy_ambience"),
        "P5 | AI cozy_ambience topic group": ai & tg.str.contains("cozy_ambience"),
        "P5 | all money hook": d["caption_hook_category"] == "money",
        "P5 | location Dubai/UAE": d["location_any"] == "Dubai/UAE",
        "P5 | location Switzerland": d["location_any"] == "Switzerland",
        "P6 | AI stairs_hall or bathroom": ai & d["room_primary"].isin(["stairs_hall", "bathroom"]),
        "P6 | all stairs_hall or bathroom": d["room_primary"].isin(["stairs_hall", "bathroom"]),
        "REF | all coded reels": d["realism"].notna(),
        "REF | AI all": ai,
        "REF | AI bedroom/living/kitchen": ai & d["room_primary"].isin(["bedroom", "living_room", "kitchen"]),
    }


def q(s, p):
    s = s.dropna()
    return float(s.quantile(p)) if len(s) else np.nan


def bench(d):
    rows = []
    for name, m in segments(d).items():
        s = d[m]
        sm = s[s["followers"] < 100_000]
        nv = s["vpf"].notna().sum()
        rows.append({
            "segment": name, "n_reels": int(len(s)), "n_views": int(s["views"].notna().sum()),
            "views_p25": q(s["views"], .25), "views_median": q(s["views"], .5), "views_p75": q(s["views"], .75), "views_p90": q(s["views"], .9),
            "n_adj": int(s["adj_factor"].notna().sum()), "median_adj_factor": q(s["adj_factor"], .5),
            "share_viral_5x": float((s["vpf"] >= 5).sum() / nv) if nv else np.nan,
            "median_likes_per_view": q(s["likes_per_view"], .5), "median_comments_per_view": q(s["comments_per_view"], .5),
            "share_shoppability_high": float((s["shoppability"] == "high").mean()), "share_shoppability_low": float((s["shoppability"] == "low").mean()),
            "share_people_present": float((s["people_present"] == True).mean()),  # noqa: E712
            "share_posted_last_180d": float((s["age_days"] <= 180).mean()),
            "n_small_accounts_lt100k": int(sm["views"].notna().sum()),
            "small_views_p25": q(sm["views"], .25), "small_views_median": q(sm["views"], .5), "small_views_p75": q(sm["views"], .75),
            "low_confidence": len(s) < 15,
        })
    return pd.DataFrame(rows)


def contrast(name, a, b, metric="adj_factor"):
    a = a[metric].dropna().values
    b = b[metric].dropna().values
    if len(a) < 5 or len(b) < 5:
        return None
    r = [np.median(RNG.choice(a, len(a))) / np.median(RNG.choice(b, len(b))) for _ in range(2000)]
    lo, hi = np.percentile(r, [2.5, 97.5])
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    return {"contrast": name, "metric": metric, "n_a": len(a), "median_a": round(float(np.median(a)), 4),
            "n_b": len(b), "median_b": round(float(np.median(b)), 4), "ratio_a_over_b": round(float(np.median(a) / np.median(b)), 3),
            "ci95_low": round(float(lo), 3), "ci95_high": round(float(hi), 3), "mannwhitney_p": float(p),
            "significant_0.05": p < 0.05, "ci_excludes_1": (lo > 1) or (hi < 1), "posthoc": True}


def ai_contrasts(d):
    ai = d[d["is_ai"] & d["adj_factor"].notna()]
    ch = ai["cover_hooks"]
    fx = ai["ambience_fx"]
    rows = [
        contrast("AI: warm palette vs cool+neutral", ai[ai["palette_temp"] == "warm"], ai[ai["palette_temp"] != "warm"]),
        contrast("AI: night_artificial vs all other lighting", ai[ai["lighting"] == "night_artificial"], ai[ai["lighting"] != "night_artificial"]),
        contrast("AI: night_artificial vs daylight", ai[ai["lighting"] == "night_artificial"], ai[ai["lighting"] == "daylight"]),
        contrast("AI: candle_fire vs all other lighting", ai[ai["lighting"] == "candle_fire"], ai[ai["lighting"] != "candle_fire"]),
        contrast("AI: person on cover vs not", ai[ch.str.contains("person")], ai[~ch.str.contains("person")]),
        contrast("AI: view_reveal cover vs not", ai[ch.str.contains("view_reveal")], ai[~ch.str.contains("view_reveal")]),
        contrast("AI: cover text present vs none", ai[ai["cover_text"].notna()], ai[ai["cover_text"].isna()]),
        contrast("AI: marble visible vs not", ai[ai["materials"].str.contains("marble")], ai[~ai["materials"].str.contains("marble")]),
        contrast("AI: curiosity caption hook vs all other hooks", ai[ai["caption_hook_category"] == "curiosity"], ai[ai["caption_hook_category"] != "curiosity"]),
        contrast("AI: curiosity vs descriptive caption hook", ai[ai["caption_hook_category"] == "curiosity"], ai[ai["caption_hook_category"] == "descriptive"]),
        contrast("AI: medium brightness vs bright+dark", ai[ai["brightness"] == "medium"], ai[ai["brightness"] != "medium"]),
        contrast("AI: mountain/ocean_beach setting vs rest", ai[ai["landscape"].isin(["mountain", "ocean_beach"])], ai[~ai["landscape"].isin(["mountain", "ocean_beach"])]),
        contrast("AI: cliff setting vs rest", ai[ai["landscape"] == "cliff"], ai[ai["landscape"] != "cliff"]),
        contrast("AI: stairs_hall/bathroom vs bedroom/living/kitchen", ai[ai["room_primary"].isin(["stairs_hall", "bathroom"])], ai[ai["room_primary"].isin(["bedroom", "living_room", "kitchen"])]),
        contrast("AI: high vs low shoppability", ai[ai["shoppability"] == "high"], ai[ai["shoppability"] == "low"]),
        contrast("AI: rain/snow/fireplace fx vs no fx", ai[fx.str.contains("rain|snow|fireplace")], ai[fx.str.contains("none") | (fx == "")]),
        contrast("AI: transformation caption keywords vs rest (explorative)", ai[ai["transform_kw"]], ai[~ai["transform_kw"]]),
        contrast("AI: choice hook vs others (comments/view)", ai[ai["caption_hook_category"] == "choice"], ai[ai["caption_hook_category"] != "choice"], metric="comments_per_view"),
    ]
    return pd.DataFrame([r for r in rows if r])


def ai_segments(d):
    """AI-generated reels only: median adj_factor etc. per single-label dimension (for the style guide)."""
    ai = d[d["is_ai"]]
    out = []
    for dim in ["room_primary", "style_primary", "landscape", "lighting", "building_type", "palette_temp",
                "brightness", "caption_hook_category", "realism", "account_kind_hint", "shoppability"]:
        for val, s in ai.groupby(dim):
            nv = s["vpf"].notna().sum()
            out.append({"dimension": dim, "value": val, "n": int(len(s)), "n_adj": int(s["adj_factor"].notna().sum()),
                        "median_adj_factor": q(s["adj_factor"], .5), "median_views": q(s["views"], .5),
                        "share_viral_5x": float((s["vpf"] >= 5).sum() / nv) if nv else np.nan,
                        "median_comments_per_view": q(s["comments_per_view"], .5),
                        "low_confidence": len(s) < 15})
    return pd.DataFrame(out).sort_values(["dimension", "median_adj_factor"], ascending=[True, False])


def main():
    d = load()
    b = bench(d)
    b.to_csv(os.path.join(OUT, "pillar_benchmarks.csv"), index=False)
    c = ai_contrasts(d)
    c.to_csv(os.path.join(OUT, "ai_style_contrasts.csv"), index=False)
    a = ai_segments(d)
    a.to_csv(os.path.join(OUT, "ai_segments.csv"), index=False)
    pd.set_option("display.width", 250)
    print(b.round(4).to_string())
    print(c.to_string())
    print(a.round(3).to_string())


if __name__ == "__main__":
    main()
