"""Micro-niche screen for Teil 21 (10_market_gaps.md).

Each micro-niche is measured on two levels:

1. Topic level (demand / supply / freshness): the public topic pages that carry the niche's name.
   - median of topic-page medians (views of the ~12 top reels shown), sum/median of "X reels on Instagram"
     (supply proxy; small counts = narrow search phrase), median views per 1k reels,
   - freshness = share of top-page slots posted <= 180 days before fetch (same rule as analyze.py),
     median adj_factor of those recent slots, AI share / theme-page share of coded slots.
2. Content level (performance): reels anywhere in the dataset that show the niche's feature
   (AI-assisted cover/caption codes -> ESTIMATED), mostly restricted to AI-generated reels.
   - median adj_factor (views vs. expectation for account size on the same topic page),
     share_viral_5x, comments/view, number of handles and "specialists" (handles with >= 2 reels
     in the segment), contrast vs. all other AI reels (median ratio, 95 % bootstrap CI, Mann-Whitney p).

Caveats: topic pages only show TOP reels (selection bias); adj_factor is centred per topic page, so
comparisons of whole topic groups via adj are flat by construction (see 01_market_analysis.md 1.2);
segment definitions are post-hoc -> explorative. n < 15 = low confidence.

Outputs: data/processed/stats/micro_niches.csv, topic_freshness.csv, micro_niches_summary.json  (run: python3 scripts/micro_niches.py)
Bootstrap: 2,000 resamples, seed 7 (same convention as key_contrasts.py / pillar_style_stats.py).
"""
import os

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ST = os.path.join(ROOT, "data", "processed", "stats")
RNG = np.random.default_rng(7)

COZY = ["cozy-rain", "rainy-day", "rain-cozy", "cozy-room", "cozy-bedroom-ideas", "cozy-cabin",
        "cozy-cabin-in-the-snow", "cozy-winter-cabin", "rain-sounds", "ai-cozy-cabin"]
HOTEL = ["treehouse-hotel", "luxury-resort", "overwater-villa", "unique-airbnb", "hotel-bathroom-designs",
         "glamping-ideas", "luxury-hotel", "underwater-hotel", "maldives-resort", "best-rooftop-pools",
         "arctic-treehouse-hotel-rovaniemi", "luxury-suite", "luxury-hotel-suite", "hotel-design", "boutique-hotel",
         "bora-bora-luxury-hotels", "cook-islands-luxury-resorts", "hotel-suite-design-ideas",
         "hunza-valley-luxury-resorts", "hotel-room-interior-design-ideas", "luxury-hotel-room"]


def niches(d):
    ai = d["production"] == "ai_generated"
    txt = (d["caption_full"].fillna("") + " " + d["notable"].fillna("")).str.lower()
    fx = d["ambience_fx"].fillna("")
    rp, ls, bt, sp = d["room_primary"], d["landscape"], d["building_type"], d["style_primary"]
    return [
        # key, label, topic pages, content segment, segment description
        ("impossible_locations", "Luxury Homes in Impossible Locations",
         ["waterfall-house", "impossible-architecture", "surreal-architecture", "capsule-castle-luxury-space-capsule-houses"],
         ai & (d["realism"] == "fantasy_impossible"), "AI & realism=fantasy_impossible"),
        ("ai_mountain_coast", "Alpine & coastal edge homes (setting)",
         ["swiss-chalet", "chalet", "aspen", "mountain-house"],
         ai & ls.isin(["mountain", "ocean_beach"]), "AI & landscape in (mountain, ocean_beach)"),
        ("alpine", "Alpine / Swiss concept homes",
         ["swiss-chalet", "chalet", "aspen", "mountain-house"],
         ai & (ls == "mountain"), "AI & landscape=mountain"),
        ("garden", "AI landscaping / garden transformations",
         ["landscape-design-ai", "landscape-design", "luxury-garden", "garden-design", "backyard-design", "outdoor-living"],
         ai & rp.isin(["garden_landscape", "terrace_outdoor"]), "AI & room in (garden_landscape, terrace_outdoor)"),
        ("bathrooms", "Impossible / statement bathrooms",
         ["luxury-bathroom-design", "luxury-bathroom", "quiet-luxury-bathroom",
          "luxury-bathroom-interior-design-inspiration", "bathroom-design", "hotel-bathroom-designs"],
         ai & (rp == "bathroom"), "AI & room=bathroom"),
        ("stairs", "Statement staircases & halls",
         [], ai & (rp == "stairs_hall"), "AI & room=stairs_hall"),
        ("underground", "Underground oases / bunkers",
         ["underground-house", "inside-underground-bunker-house"],
         ai & txt.str.contains(r"underground|bunker|cave|subterran", regex=True),
         "AI & caption/notable matches underground|bunker|cave|subterran"),
        ("waterfall", "Waterfall & water houses",
         ["waterfall-house"], ai & txt.str.contains("waterfall"), "AI & caption/notable matches waterfall"),
        ("treehouse", "Treehouse homes",
         ["treehouse", "treehouse-hotel", "arctic-treehouse-hotel-rovaniemi"],
         bt == "treehouse", "ALL & building=treehouse (AI n too small)"),
        ("treehouse_ai", "Treehouse homes (AI only)",
         ["treehouse", "treehouse-hotel", "arctic-treehouse-hotel-rovaniemi"],
         ai & (bt == "treehouse"), "AI & building=treehouse"),
        ("cliff", "Cliff homes",
         ["cliff-house", "house-on-cliff"], ai & (ls == "cliff"), "AI & landscape=cliff"),
        ("pick_one", "'Pick one' rooms / homes",
         [], ai & (d["caption_hook_category"] == "choice"), "AI & caption hook=choice"),
        ("tropical", "AI tropical luxury homes",
         ["tropical-villa", "tropical-house", "tropical-house-architecture-styles",
          "bali-luxury-villas-with-private-pools", "bali-villa", "bali-infinity-pool-villas"],
         ai & ((sp == "tropical") | (ls == "jungle_tropical")), "AI & (style=tropical or landscape=jungle_tropical)"),
        ("tropical_style", "AI tropical (style only)",
         ["tropical-villa", "tropical-house", "tropical-house-architecture-styles"],
         ai & (sp == "tropical"), "AI & style=tropical"),
        ("tropical_jungle", "AI jungle setting (landscape only)",
         ["bali-luxury-villas-with-private-pools", "bali-villa", "bali-infinity-pool-villas"],
         ai & (ls == "jungle_tropical"), "AI & landscape=jungle_tropical"),
        ("night_penthouse", "Night penthouses / skyline",
         ["luxury-penthouse", "penthouse-tour", "dubai-penthouse", "dubai-luxury-penthouse"],
         ai & ((bt == "penthouse") | (ls == "city_skyline")), "AI & (building=penthouse or landscape=city_skyline)"),
        ("future_bedrooms", "Future bedrooms",
         ["futuristic-interior", "dream-bedrooms", "dream-bedroom"],
         ai & (rp == "bedroom") & ((sp == "futuristic") | (ls == "space_sky") | fx.str.contains("stars")),
         "AI & room=bedroom & (style=futuristic or space_sky or stars fx)"),
        ("ai_bedrooms", "AI bedrooms (reference)",
         ["dream-bedrooms", "dream-bedroom", "luxury-bedroom", "luxury-bedroom-design", "luxury-master-bedroom"],
         ai & (rp == "bedroom"), "AI & room=bedroom"),
        ("cozy_night", "Cozy night retreats",
         COZY, ai & fx.str.contains(r"rain|snow|fireplace", regex=True), "AI & ambience fx in (rain, snow, fireplace)"),
        ("ai_hotels", "AI hotels / future resorts",
         HOTEL, ai & ((bt == "hotel_resort") | rp.isin(["hotel_room", "lobby_common"])),
         "AI & (building=hotel_resort or room in hotel_room/lobby)"),
        ("pools", "Infinity pools (standalone)",
         ["infinity-pools", "luxury-pool", "indoor-pool", "rooftop-pool", "villa-with-pool", "luxury-villa-with-pool"],
         ai & (rp == "pool"), "AI & room=pool"),
        ("art_deco", "Neo-Deco statement rooms",
         ["art-deco-interior-design", "minimalist-art-deco-interior-design"],
         sp == "art_deco", "ALL & style=art_deco"),
        ("library", "Dark-academia home libraries",
         ["dark-academia-home-library", "home-library"],
         txt.str.contains(r"library|biblioth", regex=True), "ALL & caption/notable matches library"),
        ("cyberpunk", "Cyberpunk night cities",
         ["cyberpunk-city"], sp == "cyberpunk", "ALL & style=cyberpunk"),
        ("unique_stays", "Unique stays (glamping / Airbnb)",
         ["unique-airbnb", "glamping-ideas"], ai & (bt == "hotel_resort"), "AI & building=hotel_resort (proxy)"),
        ("desert", "Desert concept homes",
         ["desert-house", "desert-modern-house-tours", "desert-house-interior-design-ideas"],
         ai & (ls == "desert"), "AI & landscape=desert"),
        ("underwater", "Underwater homes",
         ["underwater-hotel"], ls == "underwater", "ALL & landscape=underwater"),
    ]


def contrast(a, b, metric="adj_factor"):
    a = a[metric].dropna().values
    b = b[metric].dropna().values
    if len(a) < 5 or len(b) < 5:
        return {}
    r = [np.median(RNG.choice(a, len(a))) / np.median(RNG.choice(b, len(b))) for _ in range(2000)]
    lo, hi = np.percentile(r, [2.5, 97.5])
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    return {"ratio_vs_rest_ai": round(float(np.median(a) / np.median(b)), 3), "ci95_low": round(float(lo), 3),
            "ci95_high": round(float(hi), 3), "mannwhitney_p": float(p)}


def main():
    d = pd.read_csv(os.path.join(ROOT, "04_reel_database.csv"), low_memory=False)
    tp = pd.read_csv(os.path.join(ST, "topics.csv"))
    tr = pd.read_csv(os.path.join(ROOT, "data", "processed", "topic_reels.csv"))
    slots = tr[["topic", "shortcode"]].merge(
        d[["shortcode", "handle", "age_days", "production", "account_kind_hint", "adj_factor"]], on="shortcode", how="left")
    ai = d["production"] == "ai_generated"
    rows = []
    for key, label, topics, seg, desc in niches(d):
        row = {"niche": key, "label": label, "segment_definition": desc, "topics": ";".join(topics), "n_topics": len(topics)}
        if topics:
            t = tp[tp["topic"].isin(topics)]
            s = slots[slots["topic"].isin(topics)]
            rec = s[s["age_days"] <= 180]
            coded = s["production"].notna()
            row.update({
                "topic_median_of_medians": t["median_views"].median(),
                "topic_max_median": t["median_views"].max(),
                "topics_with_supply_label": int(t["reels_on_topic"].notna().sum()),
                "supply_sum_reels_on_topic": t["reels_on_topic"].sum(min_count=1),
                "supply_median_reels_on_topic": t["reels_on_topic"].median(),
                "median_views_per_1k_reels": t["median_views_per_1k_reels"].median(),
                "n_slots": len(s),
                "fresh_share_180d": round(float((s["age_days"] <= 180).mean()), 3) if len(s) else np.nan,
                "n_recent": len(rec),
                "recent_median_adj": round(float(rec["adj_factor"].median()), 3) if rec["adj_factor"].notna().any() else np.nan,
                "slot_ai_share": round(float((s.loc[coded, "production"] == "ai_generated").mean()), 3) if coded.any() else np.nan,
                "slot_theme_page_share": round(float((s.loc[coded, "account_kind_hint"] == "theme_page").mean()), 3) if coded.any() else np.nan,
                "slot_unique_handles": int(s["handle"].nunique()),
            })
        g = d[seg]
        vc = g["handle"].value_counts()
        small = g[g["followers"] < 100_000]
        row.update({
            "seg_n_small_lt100k": len(small),
            "seg_small_median_views": small["views"].median() if len(small) else np.nan,
            "seg_n": len(g), "seg_n_adj": int(g["adj_factor"].count()),
            "seg_median_adj": round(float(g["adj_factor"].median()), 3) if g["adj_factor"].notna().any() else np.nan,
            "seg_median_views": g["views"].median(), "seg_p90_views": g["views"].quantile(0.9) if len(g) else np.nan,
            "seg_share_viral_5x": round(float((g["vpf"] >= 5).sum() / g["vpf"].count()), 3) if g["vpf"].count() else np.nan,
            "seg_median_comments_per_view": g["comments_per_view"].median(),
            "seg_fresh_share_180d": round(float((g["age_days"] <= 180).mean()), 3) if len(g) else np.nan,
            "seg_share_of_all_ai": round(len(g) / int(ai.sum()), 4),
            "seg_unique_handles": int(g["handle"].nunique()),
            "seg_specialists_ge2": int((vc >= 2).sum()),
            "seg_top_handles": ";".join(f"{h}:{c}" for h, c in vc.head(4).items()),
            "seg_share_high_shoppability": round(float((g["shoppability"] == "high").mean()), 3) if len(g) else np.nan,
            "seg_share_people": round(float((g["people_present"] == True).mean()), 3) if len(g) else np.nan,  # noqa: E712
            "low_confidence": len(g) < 15,
        })
        if seg.sum() and (seg & ai).sum() == seg.sum():  # AI-only segment -> contrast vs. rest of AI
            row.update(contrast(d[seg], d[ai & ~seg]))
        rows.append(row)
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(ST, "micro_niches.csv"), index=False)
    print(out.to_string())
    # per topic page: freshness and AI share (same slot logic as freshness_by_group.csv, n = 12 per page -> low confidence)
    g = slots.groupby("topic")
    tf = pd.DataFrame({
        "n_slots": g.size(),
        "fresh_share_180d": g["age_days"].apply(lambda s: round(float((s <= 180).mean()), 3)),
        "n_recent": g["age_days"].apply(lambda s: int((s <= 180).sum())),
        "recent_median_adj": slots[slots["age_days"] <= 180].groupby("topic")["adj_factor"].median().round(3),
        "median_adj_all_slots": g["adj_factor"].median().round(3),
        "slot_ai_share": g["production"].apply(lambda s: round(float((s == "ai_generated").sum() / s.notna().sum()), 3) if s.notna().any() else np.nan),
        "slot_ai_creator_share": g["account_kind_hint"].apply(lambda s: round(float((s == "ai_creator").sum() / s.notna().sum()), 3) if s.notna().any() else np.nan),
    })
    tf = tp.set_index("topic")[["group", "median_views", "reels_on_topic", "median_views_per_1k_reels"]].join(tf)
    tf["low_confidence"] = True
    tf.sort_values("median_views", ascending=False).to_csv(os.path.join(ST, "topic_freshness.csv"))
    # is "views per 1k reels" a gap signal? check against freshness (can new reels still reach the page?)
    lab = tf.dropna(subset=["median_views_per_1k_reels"])
    top10 = lab.sort_values("median_views_per_1k_reels", ascending=False).head(10)
    rho = stats.spearmanr(lab["median_views_per_1k_reels"], lab["fresh_share_180d"])
    summ = {"n_topics_with_supply_label": int(len(lab)),
            "spearman_views_per_1k_vs_freshness": {"rho": round(float(rho.statistic), 3), "p": float(rho.pvalue)},
            "top10_ratio_topics": top10.index.tolist(),
            "top10_ratio_median_freshness": float(top10["fresh_share_180d"].median()),
            "top10_ratio_n_freshness_le_25pct": int((top10["fresh_share_180d"] <= 0.25).sum()),
            "all_topics_median_freshness": float(tf["fresh_share_180d"].median())}
    pd.Series(summ).to_json(os.path.join(ST, "micro_niches_summary.json"), indent=1)


if __name__ == "__main__":
    main()
