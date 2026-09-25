#!/usr/bin/env python3
"""Build the two input watchlists of the weekly competitor monitor (Part 33) from the research data.

Output (next to this script):
  watchlist_topics.csv       ~57 /popular/<slug>/ topics across the content pillars (hand-picked list below,
                             every slug was swept successfully on 2026-09-25, baseline stats attached)
  watchlist_competitors.csv  ~40 handles in three roles (direct / emerging / benchmark), selected by the
                             rules below from data/processed/accounts_metrics.csv, each with the newest reel
                             shortcode seen in the research sweep (needed for the embed lookup)

Re-run after a new research sweep; edit the constants, not the CSVs, so the selection stays reproducible.
Manual additions: put them into EXTRA_COMPETITORS / TOPICS below (or edit the CSV and note it in the doc).
"""
import csv
import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)
ROOT = os.path.dirname(SCRIPTS)
P = os.path.join(ROOT, "data", "processed")
sys.path.insert(0, SCRIPTS)
from shortcode_time import shortcode_to_datetime  # noqa: E402
from topic_groups import topic_group  # noqa: E402

# (slug, cluster) - cluster = monitoring cluster for reading the report; group (from topic_groups.py) = the pillar
# value used in the winner database (data/winner_database_schema.sql, series.pillar / reels.pillar)
TOPICS = [
    # AI-heavy topic pages = direct competitive field
    ("ai-interior-design", "ai_field"), ("ai-home-design", "ai_field"), ("ai-generated-house", "ai_field"),
    ("midjourney-architecture", "ai_field"), ("ai-architecture", "ai_field"), ("ai-cozy-cabin", "ai_field"),
    # Future homes / architecture
    ("futuristic-houses", "future_homes"), ("futuristic-house", "future_homes"), ("futuristic-interior", "future_homes"),
    ("futuristic-home", "future_homes"), ("parametric-architecture", "future_homes"), ("future-houses-2050", "future_homes"),
    ("modern-architecture", "architecture"), ("architecture-design", "architecture"),
    ("tropical-house-architecture-styles", "architecture"),
    # Luxury rooms
    ("dream-bedrooms", "luxury_interiors"), ("dream-bedroom", "luxury_interiors"), ("luxury-bedroom", "luxury_interiors"),
    ("luxury-bathroom-design", "luxury_interiors"), ("luxury-kitchen", "luxury_interiors"), ("dream-closet", "luxury_interiors"),
    ("luxury-living-room-design", "luxury_interiors"), ("quiet-luxury", "luxury_interiors"),
    ("bedroom-design", "luxury_interiors"), ("living-room-design", "luxury_interiors"), ("bathroom-design", "luxury_interiors"),
    # Luxury homes
    ("dream-home", "luxury_homes"), ("luxury-house", "luxury_homes"), ("luxury-penthouse", "luxury_homes"),
    ("modern-villa", "luxury_homes"), ("ultra-modern-luxury-house-design", "luxury_homes"),
    ("modern-luxury-house-interiors", "luxury_homes"),
    # Unusual / fantasy homes
    ("treehouse", "unusual_homes"), ("underground-house", "unusual_homes"), ("house-in-the-forest", "unusual_homes"),
    ("glass-house", "unusual_homes"), ("cliff-house", "unusual_homes"), ("luxury-cabin", "unusual_homes"),
    ("desert-house", "unusual_homes"), ("dream-room", "unusual_homes"), ("waterfall-house", "unusual_homes"),
    # Cozy ambience
    ("cozy-rain", "cozy_ambience"), ("rain-cozy", "cozy_ambience"), ("cozy-cabin-in-the-snow", "cozy_ambience"),
    ("cozy-winter-cabin", "cozy_ambience"), ("cozy-bedroom-ideas", "cozy_ambience"),
    # Pools / resorts
    ("infinity-pools", "pools_resorts"), ("indoor-pool", "pools_resorts"), ("luxury-pool", "pools_resorts"),
    ("overwater-villa", "pools_resorts"), ("treehouse-hotel", "pools_resorts"), ("underwater-hotel", "pools_resorts"),
    # Styles
    ("japandi", "styles"), ("tropical-house", "styles"), ("biophilic-bedroom-design", "styles"),
    ("art-deco-interior-design", "styles"), ("organic-modern", "styles"),
]

# Competitor selection rules (applied to accounts_metrics.csv; research snapshot 2026-09-25)
DIRECT_KINDS = {"ai_creator", "theme_page", "media_publication"}
PRODUCTION_OK = {"ai_generated", "3d_render"}
DIRECT_MIN_FOLLOWERS, DIRECT_ACTIVE_SINCE, DIRECT_N = 30_000, "2026-03-01", 25
EMERGING_MIN, EMERGING_MAX, EMERGING_ACTIVE_SINCE, EMERGING_MIN_MAXVPF, EMERGING_N = 3_000, 30_000, "2026-05-01", 5.0, 10
# large reference pages from the profiled shortlist (data/raw/accounts/profile_*.json), any production mode
BENCHMARKS = ["luxurydreamhub", "elitebuildhq", "aiforarchitects", "soothenests", "wayup_media", "uniqchalets",
              "sunt_mrr", "cozyzen.ai"]
EXTRA_COMPETITORS = []  # (handle, role, note) added by hand
# off-niche despite matching the rules (checked by hand against topics/bio on 2026-09-25)
EXCLUDE = {"diycraftstvofficial",  # DIY/crafts page, interior only incidental
           "naturesms",            # nature/landscape page (10M), not interior/architecture
           "thedollstudio2026"}    # AI art/doll content, surfaced only via the ai-art topic


def newest_shortcodes():
    u = pd.read_csv(os.path.join(P, "reels_unique.csv"))
    u["posted"] = u["shortcode"].apply(shortcode_to_datetime)
    u = u[u["posted"].notna()].sort_values("posted")
    last = u.groupby("handle").tail(1).set_index("handle")
    return last


def main():
    tstats = pd.read_csv(os.path.join(P, "stats", "topics.csv")).set_index("topic")
    status = pd.read_csv(os.path.join(P, "topics_status.csv"))
    ok = set(status.loc[status["status"] == "ok", "slug_used"])
    trows = []
    for slug, cluster in TOPICS:
        if slug not in ok:
            print(f"!! topic {slug} was not swept ok on 2026-09-25 - skipped")
            continue
        s = tstats.loc[slug] if slug in tstats.index else None
        trows.append({
            "slug": slug, "cluster": cluster, "group": topic_group(slug)[0],
            "url": f"https://www.instagram.com/popular/{slug}/",
            "baseline_date": "2026-09-25",
            "baseline_n_reels": int(s["n"]) if s is not None else "",
            "baseline_median_views": int(s["median_views"]) if s is not None and pd.notna(s["median_views"]) else "",
            "baseline_share_ai_coded": round(float(s["share_ai_generated"]), 2) if s is not None and pd.notna(s["share_ai_generated"]) else "",
            "total_reels_label": s["total_reels_label"] if s is not None and pd.notna(s["total_reels_label"]) else "",
        })
    with open(os.path.join(HERE, "watchlist_topics.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(trows[0].keys()))
        w.writeheader(); w.writerows(trows)
    print(f"topics: {len(trows)} -> watchlist_topics.csv")

    a = pd.read_csv(os.path.join(P, "accounts_metrics.csv"))
    a["last"] = a["last_post_seen"].astype(str).str[:10]
    a = a[a["followers"].notna() & ~a["handle"].isin(EXCLUDE)]
    base = a[(a["language_mode"] == "en") & a["production_mode"].isin(PRODUCTION_OK) & a["account_kind"].isin(DIRECT_KINDS)]
    direct = base[(base["followers"] >= DIRECT_MIN_FOLLOWERS) & (base["last"] >= DIRECT_ACTIVE_SINCE)]
    direct = direct.sort_values("median_topic_index", ascending=False).head(DIRECT_N)
    emerg = base[(base["followers"] >= EMERGING_MIN) & (base["followers"] < EMERGING_MAX)
                 & (base["last"] >= EMERGING_ACTIVE_SINCE) & (base["max_vpf"] >= EMERGING_MIN_MAXVPF)]
    emerg = emerg.sort_values("max_vpf", ascending=False).head(EMERGING_N)
    bench = a[a["handle"].isin(BENCHMARKS)]

    last = newest_shortcodes()
    rows, seen = [], set()
    for role, df, why in [("direct", direct, f"AI/3D, en, >= {DIRECT_MIN_FOLLOWERS:,} followers, active since {DIRECT_ACTIVE_SINCE}, top median topic_index"),
                          ("emerging", emerg, f"AI/3D, en, {EMERGING_MIN:,}-{EMERGING_MAX:,} followers, active since {EMERGING_ACTIVE_SINCE}, max vpf >= {EMERGING_MIN_MAXVPF}"),
                          ("benchmark", bench, "large reference page from profiled shortlist")]:
        for r in df.itertuples():
            if r.handle in seen:
                continue
            seen.add(r.handle)
            sc = last.loc[r.handle, "shortcode"] if r.handle in last.index else ""
            posted = last.loc[r.handle, "posted"] if r.handle in last.index else None
            rows.append({
                "handle": r.handle, "role": role, "account_kind": r.account_kind, "production_mode": r.production_mode,
                "baseline_followers": int(r.followers), "baseline_posts": int(r.posts) if pd.notna(r.posts) else "",
                "baseline_median_topic_index": round(float(r.median_topic_index), 2) if pd.notna(r.median_topic_index) else "",
                "baseline_max_vpf": round(float(r.max_vpf), 2) if pd.notna(r.max_vpf) else "",
                "last_shortcode": sc, "last_posted_utc": posted.isoformat() if posted is not None else "",
                "embed_url": f"https://www.instagram.com/reel/{sc}/embed/captioned/" if sc else "",
                "selection_rule": why, "active": 1,
            })
    for h, role, note in EXTRA_COMPETITORS:
        if h not in seen:
            rows.append({"handle": h, "role": role, "selection_rule": note, "active": 1})
    with open(os.path.join(HERE, "watchlist_competitors.csv"), "w", newline="", encoding="utf-8") as f:
        fields = ["handle", "role", "account_kind", "production_mode", "baseline_followers", "baseline_posts",
                  "baseline_median_topic_index", "baseline_max_vpf", "last_shortcode", "last_posted_utc", "embed_url",
                  "selection_rule", "active"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    by = pd.Series([r["role"] for r in rows]).value_counts().to_dict()
    print(f"competitors: {len(rows)} {by} -> watchlist_competitors.csv")


if __name__ == "__main__":
    main()
