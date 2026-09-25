"""Build 02_competitor_database.csv (Part 2) from reel metrics + deep profiles.

Rows: every deep-profiled account (data/raw/accounts/profile_*.json) plus the strongest other
accounts from the topic sweep (by max views / reels in sample) so the table has >= 100 rows.
Every value carries a status column: VERIFIED (seen on a public page), ESTIMATED (derived /
AI-coded / search-index snapshot / bounds), UNKNOWN (not observable without login).
"""
import glob
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shortcode_time import shortcode_to_datetime  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "processed")
FETCH = datetime(2026, 9, 25, tzinfo=timezone.utc)
GROUPS = {
    "theme_page": "A/F theme page", "ai_creator": "D/E AI creator", "designer_studio": "A designer/3D studio",
    "architect": "C architecture", "real_estate": "B luxury real estate", "media_publication": "C/G media",
    "lifestyle_influencer": "G lifestyle", "brand_manufacturer": "brand", "contractor_trade": "trade",
    "education_course": "E education", "other": "other",
}


def load_profiles():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "data", "raw", "accounts", "profile_*.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        out[d.get("handle", "").lower()] = d
    return out


def offers_flags(d):
    offers = (d.get("link_in_bio") or {}).get("offers") or []
    ev = d.get("monetization_evidence") or []
    types = [str(o.get("type", "")) for o in offers] + [str(e.get("type", "")) for e in ev]
    text = " ".join(json.dumps(x) for x in offers + ev).lower()
    f = {
        "affiliate": any(t.startswith("affiliate") for t in types) or any(k in text for k in ["amazon", "ltk", "shopmy", "affiliate", "wayfair"]),
        "brand_deals": bool(d.get("brand_deals_seen")) or any("brand" in t or "sponsor" in t for t in types),
        "shop": "shop" in types,
        "services": "service" in types,
        "digital_products": any(t in ("digital_product", "course") for t in types),
        "newsletter": "newsletter" in types,
        "other_monetization": any(t in ("app", "membership", "real_estate") for t in types),
        "brand_contact": "brand_contact" in types,
    }
    return f, "; ".join(sorted({o.get("label", "")[:60] for o in offers if o.get("label")}))[:400]


def main():
    acc = pd.read_csv(os.path.join(P, "accounts_metrics.csv"))
    df = pd.read_pickle(os.path.join(P, "reels_master.pkl"))
    prof = load_profiles()
    # candidate rows: profiled + top by breadth/views
    cand = set(prof)
    top = acc[acc["followers"].notna()].sort_values(["n_reels_sample", "max_views"], ascending=False).head(60)["handle"]
    cand |= set(top)
    cand |= set(acc.sort_values("max_views", ascending=False).head(25)["handle"])
    rows = []
    for h in sorted(cand):
        a = acc[acc["handle"] == h]
        a = a.iloc[0] if len(a) else pd.Series(dtype=object)
        d = prof.get(h, {})
        reels = df[df["handle"] == h]
        codes = [str(x.get("shortcode")) for x in (d.get("reel_sample") or [])] + list(reels["shortcode"])
        dts = [t for t in (shortcode_to_datetime(c) for c in codes) if t]
        earliest = min(dts) if dts else None
        age_days = (FETCH - earliest).days if earliest else None
        posts = a.get("posts") if "posts" in a else np.nan
        freq = (posts / age_days * 7) if (age_days and posts and not pd.isna(posts) and age_days > 0) else np.nan
        flags, offer_labels = offers_flags(d) if d else ({k: None for k in ["affiliate", "brand_deals", "shop", "services", "digital_products", "newsletter", "other_monetization", "brand_contact"]}, "")
        kind = d.get("account_type") or a.get("account_kind")
        mode = d.get("content_mode") or (("AI" if a.get("share_ai_generated", 0) >= 0.6 else "mixed" if a.get("share_ai_generated", 0) > 0.2 else "real") if not pd.isna(a.get("share_ai_generated", np.nan)) else "unknown")
        rows.append({
            "handle": h, "instagram_url": f"https://www.instagram.com/{h}/",
            "followers": a.get("followers"), "followers_status": "VERIFIED (embed page, rounded, 2026-09-25)" if not pd.isna(a.get("followers", np.nan)) else "UNKNOWN",
            "posts": posts, "posts_status": "VERIFIED (embed page)" if not pd.isna(posts) else "UNKNOWN",
            "display_name": d.get("display_name"), "niche_focus": d.get("niche_focus") or (a.get("topics") or "")[:120],
            "account_type": kind, "group": GROUPS.get(str(kind), "other"), "content_mode_AI_real_mixed": mode,
            "content_mode_status": "ESTIMATED (profile evidence / AI-assisted cover coding)" if mode != "unknown" else "UNKNOWN",
            "reels_in_sample": int(a.get("n_reels_sample")) if not pd.isna(a.get("n_reels_sample", np.nan)) else 0,
            "median_reel_views_sample": a.get("median_views"), "mean_reel_views_sample": reels["views"].mean() if len(reels) else np.nan,
            "top_reel_views_seen": a.get("max_views"), "views_status": "VERIFIED per reel (public topic pages); account-level = sample of top-page reels, biased upward",
            "median_views_per_follower": a.get("median_vpf"), "max_views_per_follower": a.get("max_vpf"),
            "median_likes_per_view": reels["likes_per_view"].median() if len(reels) else np.nan,
            "median_comments_per_view": reels["comments_per_view"].median() if len(reels) else np.nan,
            "engagement_status": "VERIFIED inputs (embed likes/comments + topic views); ratio computed",
            "posting_freq_per_week_upper_bound": round(freq, 1) if not pd.isna(freq) else np.nan,
            "posting_freq_status": "ESTIMATED upper bound = posts / days since earliest known post" if not pd.isna(freq) else "UNKNOWN",
            "earliest_known_post": earliest.date().isoformat() if earliest else None,
            "account_age_status": "ESTIMATED lower bound (earliest post seen, decoded from shortcode)" if earliest else "UNKNOWN",
            "bio": d.get("bio"), "bio_source": d.get("bio_source"), "cta_pattern": d.get("cta_pattern"),
            "external_links": "; ".join(d.get("external_links") or []) if d else None,
            "link_in_bio_offers": offer_labels,
            **{f"has_{k}": v for k, v in flags.items()},
            "brand_deals_seen": "; ".join(d.get("brand_deals_seen") or [])[:300] if d else None,
            "monetization_status": "VERIFIED where URL given in profile JSON; absence = not observed (not proof of absence)" if d else "UNKNOWN (not deep-profiled)",
            "deep_profiled": bool(d), "top_reel_url": a.get("top_reel_url"), "topics": (a.get("topics") or "")[:200],
            "profile_json": f"data/raw/accounts/profile_{h}.json" if d else None,
            "source": "topic-page sample + embed pages" + (" + deep profile" if d else ""),
        })
    # extra rows: accounts found in third-party rankings / articles (research q05) not already present
    extra_path = os.path.join(ROOT, "data", "raw", "accounts", "q05_accounts_found.json")
    grp_map = {"A": "A classic interior theme/creator", "B": "B luxury homes / real estate", "C": "C architecture",
               "D": "D AI architecture", "E": "E AI interior", "F": "F dream/future homes", "G": "G luxury lifestyle",
               "H": "H small account, extreme reel views"}
    have = {r["handle"] for r in rows}
    if os.path.exists(extra_path):
        from parse_topics import parse_views
        for x in json.load(open(extra_path)):
            h = str(x.get("handle", "")).lstrip("@").lower().strip()
            if not h or h in have:
                continue
            have.add(h)
            ft = str(x.get("followers_text") or "")
            num = parse_views(ft.split()[0].replace("followers", "")) if ft.strip() else None
            rows.append({"handle": h, "instagram_url": f"https://www.instagram.com/{h}/", "followers": num,
                         "followers_status": f"THIRD-PARTY ({ft}; {x.get('source_url') or 'list/ranking'})" if num else "UNKNOWN",
                         "group": grp_map.get(str(x.get("category")), str(x.get("category"))), "niche_focus": x.get("note"),
                         "deep_profiled": False, "reels_in_sample": 0,
                         "monetization_status": "UNKNOWN (not deep-profiled)", "content_mode_status": "UNKNOWN"})
    out = pd.DataFrame(rows).sort_values(["deep_profiled", "reels_in_sample", "followers"], ascending=[False, False, False])
    out.to_csv(os.path.join(ROOT, "02_competitor_database.csv"), index=False)
    print("competitor rows:", len(out), "deep-profiled:", int(out["deep_profiled"].sum()))


if __name__ == "__main__":
    main()
