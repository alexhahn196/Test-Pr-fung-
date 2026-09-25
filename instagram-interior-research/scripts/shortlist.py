"""Part 3: score accounts and pick the 20 most interesting (not by follower count).

Candidates: accounts with followers known and >= 2 reels in the topic-page sample.
Each criterion is converted to a 0-1 percentile rank among candidates, then weighted:
  virality (median views/followers)            0.20
  consistency (share of reels above topic median) 0.10
  reach (median views)                          0.10
  growth proxy (followers / days since earliest known post) 0.10  [ESTIMATED]
  repeatability (reels in sample, capped at 8)  0.10
  AI suitability (share of reels AI-generated or 3D-rendered) 0.15
  monetizability (observed offers + shoppable share) 0.10
  quality (share of high visual quality)        0.10
  originality (not a repost aggregator: own AI/3D/design output) 0.05
Output: data/processed/shortlist_scores.csv
"""
import os

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "processed")
W = {"virality": .20, "consistency": .10, "reach": .10, "growth": .10, "repeatability": .10,
     "ai_suitability": .15, "monetizability": .10, "quality": .10, "originality": .05}


def main():
    df = pd.read_pickle(os.path.join(P, "reels_master.pkl"))
    comp = pd.read_csv(os.path.join(ROOT, "02_competitor_database.csv"))
    d = df[df["views"].notna()].copy()
    g = d.groupby("handle")
    a = pd.DataFrame({
        "followers": g["followers"].max(), "n": g["shortcode"].count(),
        "median_views": g["views"].median(), "median_vpf": g["vpf"].median(),
        "share_above_topic_median": g["topic_index"].apply(lambda s: (s > 1).mean()),
        "share_ai_or_3d": g["production"].apply(lambda s: s.isin(["ai_generated", "3d_render"]).sum() / max(1, s.notna().sum())) if "production" in d else 0,
        "share_high_quality": g["visual_quality"].apply(lambda s: (s == "high").sum() / max(1, s.notna().sum())) if "visual_quality" in d else 0,
        "share_shoppable": g["shoppability"].apply(lambda s: s.isin(["high", "medium"]).sum() / max(1, s.notna().sum())) if "shoppability" in d else 0,
        "account_kind": g["account_kind_hint"].agg(lambda s: s.dropna().mode().iloc[0] if s.dropna().size else None) if "account_kind_hint" in d else None,
        "top_topic_groups": g["primary_group"].agg(lambda s: ";".join(s.dropna().value_counts().index[:3])),
    })
    a = a[(a["followers"] >= 1000) & (a["n"] >= 2)].copy()
    c = comp.set_index("handle")
    a["earliest_known_post"] = c["earliest_known_post"].reindex(a.index)
    age = (pd.Timestamp("2026-09-25") - pd.to_datetime(a["earliest_known_post"], errors="coerce")).dt.days
    a["followers_per_day_since_first_known_post"] = a["followers"] / age.clip(lower=30)
    mon_cols = ["has_affiliate", "has_brand_deals", "has_shop", "has_services", "has_digital_products", "has_newsletter"]
    mon = c[mon_cols].reindex(a.index).fillna(False).astype(bool).sum(axis=1) if set(mon_cols) <= set(c.columns) else 0
    a["observed_monetization_types"] = mon
    a["deep_profiled"] = c["deep_profiled"].reindex(a.index).fillna(False)
    orig = a["account_kind"].isin(["ai_creator", "designer_studio", "architect", "brand_manufacturer", "contractor_trade", "lifestyle_influencer", "real_estate"]).astype(float)
    orig[a["account_kind"].eq("theme_page")] = 0.5
    crit = pd.DataFrame({
        "virality": a["median_vpf"], "consistency": a["share_above_topic_median"], "reach": a["median_views"],
        "growth": a["followers_per_day_since_first_known_post"], "repeatability": a["n"].clip(upper=8),
        "ai_suitability": a["share_ai_or_3d"], "monetizability": a["observed_monetization_types"] + a["share_shoppable"],
        "quality": a["share_high_quality"], "originality": orig,
    })
    ranks = crit.rank(pct=True).fillna(0)
    for k in W:
        a[f"score_{k}"] = ranks[k].round(3)
    a["score_total"] = sum(ranks[k] * w for k, w in W.items()).round(4)
    a = a.sort_values("score_total", ascending=False)
    a["rank"] = range(1, len(a) + 1)
    a["outperformer"] = (a["median_vpf"] >= 5) & (a["n"] >= 2)
    a.to_csv(os.path.join(P, "shortlist_scores.csv"))
    cols = ["rank", "followers", "n", "median_views", "median_vpf", "share_ai_or_3d", "account_kind", "observed_monetization_types", "score_total"]
    print(a[cols].head(30).to_string())
    print("candidates:", len(a), "| outperformers (median vpf>=5, >=2 reels):", int(a["outperformer"].sum()))


if __name__ == "__main__":
    main()
