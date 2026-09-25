"""Key contrasts behind the headline findings, with bootstrap CIs and Mann-Whitney tests.

Metric: adj_factor (views vs. expectation for account size on the same topic page) and, where
relevant, comments per view. Median ratio A/B with 95 % bootstrap CI (2,000 resamples, seed 7).
Output: data/processed/stats/key_contrasts.csv
"""
import os

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "processed")
RNG = np.random.default_rng(7)


def boot_ratio(a, b, n=2000):
    a, b = np.asarray(a), np.asarray(b)
    r = [np.median(RNG.choice(a, len(a))) / np.median(RNG.choice(b, len(b))) for _ in range(n)]
    return np.percentile(r, [2.5, 97.5])


def contrast(name, a, b, metric="adj_factor", la="A", lb="B"):
    a = a[metric].dropna(); b = b[metric].dropna()
    if len(a) < 5 or len(b) < 5:
        return None
    lo, hi = boot_ratio(a, b)
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    return {"contrast": name, "metric": metric, "group_a": la, "n_a": len(a), "median_a": round(float(a.median()), 5),
            "group_b": lb, "n_b": len(b), "median_b": round(float(b.median()), 5),
            "ratio_a_over_b": round(float(a.median() / b.median()), 3), "ci95_low": round(float(lo), 3), "ci95_high": round(float(hi), 3),
            "mannwhitney_p": float(p), "significant_0.05": p < 0.05}


def main():
    df = pd.read_pickle(os.path.join(P, "reels_master.pkl"))
    d = df[df["adj_factor"].notna()]
    ai = d[d["production"] == "ai_generated"]
    rows = [
        contrast("AI-generated vs real footage", ai, d[d["production"] == "real_footage"], la="ai_generated", lb="real_footage"),
        contrast("AI-generated vs 3D render", ai, d[d["production"] == "3d_render"], la="ai_generated", lb="3d_render"),
        contrast("AI: fantasy/impossible vs stylized dreamy", ai[ai["realism"] == "fantasy_impossible"], ai[ai["realism"] == "stylized_dreamy"], la="ai fantasy_impossible", lb="ai stylized_dreamy"),
        contrast("AI: fantasy/impossible vs aspirational realistic", ai[ai["realism"] == "fantasy_impossible"], ai[ai["realism"] == "aspirational_realistic"], la="ai fantasy_impossible", lb="ai aspirational_realistic"),
        contrast("All: fantasy/impossible vs rest", d[d["realism"] == "fantasy_impossible"], d[d["realism"] != "fantasy_impossible"], la="fantasy_impossible", lb="other realism"),
        contrast("Theme page vs AI creator (all reels)", d[d["account_kind_hint"] == "theme_page"], d[d["account_kind_hint"] == "ai_creator"], la="theme_page", lb="ai_creator"),
        contrast("AI: theme page vs AI creator", ai[ai["account_kind_hint"] == "theme_page"], ai[ai["account_kind_hint"] == "ai_creator"], la="ai theme_page", lb="ai ai_creator"),
        contrast("People visible vs not (all)", d[d["people_present"] == True], d[d["people_present"] == False], la="people", lb="no people"),  # noqa: E712
        contrast("AI: people visible vs not", ai[ai["people_present"] == True], ai[ai["people_present"] == False], la="ai people", lb="ai no people"),  # noqa: E712
        contrast("Night/artificial light vs daylight", d[d["lighting"] == "night_artificial"], d[d["lighting"] == "daylight"], la="night_artificial", lb="daylight"),
        contrast("Cover text overlay vs none", d[d["cover_hooks"].fillna("").str.contains("text_overlay")], d[~d["cover_hooks"].fillna("").str.contains("text_overlay")], la="text overlay", lb="no text overlay"),
        contrast("Choice caption hook vs all other hooks (adj)", d[d["caption_hook_category"] == "choice"], d[d["caption_hook_category"] != "choice"], la="choice", lb="other hooks"),
        contrast("Choice caption hook vs others (comments/view)", d[d["caption_hook_category"] == "choice"], d[d["caption_hook_category"] != "choice"], metric="comments_per_view", la="choice", lb="other hooks"),
        contrast("Money/price hook vs others", d[d["caption_hook_category"] == "money"], d[d["caption_hook_category"] != "money"], la="money", lb="other hooks"),
        contrast("Location-only caption hook vs others", d[d["caption_hook_category"] == "location"], d[d["caption_hook_category"] != "location"], la="location", lb="other hooks"),
        contrast("High shoppability vs low", d[d["shoppability"] == "high"], d[d["shoppability"] == "low"], la="high", lb="low"),
        contrast("AI: outdoor/bath/stairs/pool vs bedroom/living/kitchen", ai[ai["room_primary"].isin(["garden_landscape", "terrace_outdoor", "bathroom", "stairs_hall", "pool"])], ai[ai["room_primary"].isin(["bedroom", "living_room", "kitchen"])], la="ai outdoor/bath/stairs/pool", lb="ai bedroom/living/kitchen"),
        contrast("AI: warm luxury/tropical/glam/futuristic vs organic modern/scandi/japandi/mediterranean/modern luxury", ai[ai["style_primary"].isin(["warm_luxury", "tropical", "glam_feminine", "futuristic"])], ai[ai["style_primary"].isin(["organic_modern", "scandinavian", "japandi", "mediterranean", "modern_luxury"])], la="ai warm/tropical/glam/futuristic", lb="ai organic/scandi/japandi/med/modern-lux"),
        contrast("Cool palette vs warm palette", d[d["palette_temp"] == "cool"], d[d["palette_temp"] == "warm"], la="cool", lb="warm"),
        contrast("Window view vs none", d[d["view_through_window"] == True], d[d["view_through_window"] == False], la="window view", lb="no window view"),  # noqa: E712
        contrast("AI disclosed vs not (AI reels only)", ai[ai["ai_disclosed"] == True], ai[ai["ai_disclosed"] == False], la="ai disclosed", lb="ai not disclosed"),  # noqa: E712
        contrast("Before/after split cover vs rest", d[d["cover_hooks"].fillna("").str.contains("before_after_split")], d[~d["cover_hooks"].fillna("").str.contains("before_after_split")], la="split cover", lb="other covers"),
    ]
    out = pd.DataFrame([r for r in rows if r])
    out.to_csv(os.path.join(P, "stats", "key_contrasts.csv"), index=False)
    print(out[["contrast", "n_a", "n_b", "ratio_a_over_b", "ci95_low", "ci95_high", "mannwhitney_p"]].to_string(index=False))


if __name__ == "__main__":
    main()
