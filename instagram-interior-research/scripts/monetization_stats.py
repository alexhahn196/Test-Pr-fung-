"""Monetization evidence from deep profiles + commerce-CTA contrasts (for 09_monetization.md, Teil 19/20).

Inputs
- data/raw/accounts/profile_*.json  (72 deep profiles: link_in_bio.offers, monetization_evidence, brand_deals_seen)
- data/processed/accounts_metrics.csv (followers, n_reels_sample, median_adj_factor per account)
- data/processed/reels_master.pkl     (reel-level adj_factor, comments_per_view, cta_type, production, shoppability)

Outputs (data/processed/stats/)
- monetization_accounts.csv   one row per deep-profiled account, STRICT flags (typed evidence only)
- monetization_summary.csv    counts of accounts per flag, overall and by content mode / account type
- monetization_contrasts.csv  exploratory contrasts (median ratio, Mann-Whitney / Kruskal p)

Why STRICT flags: 02_competitor_database.csv sets has_brand_deals=True when any evidence *type* contains
"brand" (incl. brand_contact) and has_affiliate=True on free-text matches ("amazon", "wayfair" ...).
Those columns therefore over-count real deals/affiliate links. Here a flag is only set from the typed
offer/evidence entries (or a non-empty brand_deals_seen list for deals_seen).
"""
import glob
import json
import os
import re

import numpy as np
import pandas as pd
from scipy.stats import kruskal, mannwhitneyu

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "processed")
OUT = os.path.join(P, "stats")

# keyword CTA that promises a DM/link/info/lead (engagement-only "Comment ME if you'd escape here" is excluded)
COMMENT_KW = re.compile(r"(comment|comente)\s*[\"'“][A-Za-z]{2,20}[\"'”]?.{0,25}?(i'll send|i will send|send you|dm you|for the link|for links|to get|if you want)"
                        r"|comente\s+[A-Z]{3,}\s*👇", re.I)


def load_flags():
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "raw", "accounts", "profile_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        offers = (d.get("link_in_bio") or {}).get("offers") or []
        ev = d.get("monetization_evidence") or []
        types = [str(o.get("type", "")) for o in offers] + [str(e.get("type", "")) for e in ev]
        text = json.dumps(offers + ev, ensure_ascii=False).replace('\\"', '"').lower()
        cta = (d.get("cta_pattern") or "")
        r = {
            "handle": d["handle"],
            "account_type": d.get("account_type"),
            "content_mode": d.get("content_mode"),
            "affiliate_any": any(t.startswith("affiliate") for t in types),
            "affiliate_amazon": "affiliate_amazon" in types,
            "amazon_storefront": ("amazon.com/shop" in text) or ("amazon.de/shop" in text) or ("storefront" in text and "amazon" in text),
            "affiliate_ltk": "affiliate_ltk" in types,
            "affiliate_shopmy": "shopmy" in text,
            "own_shop": "shop" in types,
            "services_b2b": any(t in ("service", "service_lead_gen", "dm_lead_gen") for t in types),
            "digital_or_course": any(t in ("digital_product", "course", "education") for t in types),
            "newsletter": "newsletter" in types,
            "membership": any(t in ("membership", "membership_tips") for t in types),
            "app_saas": any(t in ("app", "own_product_saas") for t in types),
            "real_estate_or_booking": any(t in ("real_estate", "own_booking_platform") for t in types),
            "sponsored_seen": any(t in ("sponsored_content", "sponsored_collab", "brand_deal", "hotel_campaign",
                                        "tool_promotion", "advertising_sales", "agency", "agency_parent") for t in types),
            "deals_seen": len(d.get("brand_deals_seen") or []) > 0,
            "brand_contact": "brand_contact" in types,
            "comment_kw_dm_funnel": bool(COMMENT_KW.search(cta + " " + text)),
        }
        rev = ["affiliate_any", "own_shop", "services_b2b", "digital_or_course", "newsletter", "membership",
               "app_saas", "real_estate_or_booking", "sponsored_seen"]
        r["any_revenue_path"] = any(r[k] for k in rev)
        r["nothing_observed"] = not r["any_revenue_path"] and not r["brand_contact"]
        rows.append(r)
    return pd.DataFrame(rows)


def main():
    fl = load_flags()
    acc = pd.read_csv(os.path.join(P, "accounts_metrics.csv"))[["handle", "followers", "n_reels_sample", "median_views", "median_adj_factor"]]
    fl = fl.merge(acc, on="handle", how="left")
    fl["mode_group"] = fl["content_mode"].map(lambda m: "AI" if m == "AI" else ("real" if m == "real" else "3d/mixed/unknown"))
    fl.to_csv(os.path.join(OUT, "monetization_accounts.csv"), index=False)

    flag_cols = ["affiliate_any", "affiliate_amazon", "amazon_storefront", "affiliate_ltk", "affiliate_shopmy", "own_shop",
                 "services_b2b", "digital_or_course", "newsletter", "membership", "app_saas", "real_estate_or_booking",
                 "sponsored_seen", "deals_seen", "brand_contact", "comment_kw_dm_funnel", "any_revenue_path", "nothing_observed"]
    parts = []
    tot = fl[flag_cols].sum().to_frame("all").T
    tot.insert(0, "n_accounts", len(fl))
    parts.append(tot.assign(group="all"))
    for key in ["mode_group", "account_type"]:
        g = fl.groupby(key)[flag_cols].sum()
        g.insert(0, "n_accounts", fl.groupby(key).size())
        g["group"] = key + "=" + g.index.astype(str)
        parts.append(g)
    summ = pd.concat(parts)
    summ = summ[["group", "n_accounts"] + flag_cols]
    summ.to_csv(os.path.join(OUT, "monetization_summary.csv"), index=False)

    # ---- exploratory contrasts on reels ----
    r = pd.read_pickle(os.path.join(P, "reels_master.pkl"))
    res = []

    def contrast(name, metric, a, b, la, lb):
        a = a.dropna(); b = b.dropna()
        if len(a) < 3 or len(b) < 3:
            return
        p = mannwhitneyu(a, b).pvalue
        res.append(dict(contrast=name, metric=metric, group_a=la, n_a=len(a), median_a=a.median(), group_b=lb,
                        n_b=len(b), median_b=b.median(), ratio_a_over_b=a.median() / b.median() if b.median() else np.nan,
                        test="mann-whitney", p=p))

    ck, none = r[r.cta_type == "comment_keyword"], r[r.cta_type == "none"]
    contrast("Comment-keyword CTA vs no CTA (all reels)", "adj_factor", ck.adj_factor, none.adj_factor, "comment_keyword", "none")
    contrast("Comment-keyword CTA vs no CTA (all reels)", "comments_per_view", ck.comments_per_view, none.comments_per_view, "comment_keyword", "none")
    aick, ainone = ck[ck.production == "ai_generated"], none[none.production == "ai_generated"]
    contrast("AI: comment-keyword CTA vs no CTA", "adj_factor", aick.adj_factor, ainone.adj_factor, "ai comment_keyword", "ai none")
    contrast("AI: comment-keyword CTA vs no CTA", "comments_per_view", aick.comments_per_view, ainone.comments_per_view, "ai comment_keyword", "ai none")
    lib = r[r.cta_type.isin(["link_in_bio", "shop_product"])]
    contrast("Link-in-bio/shop CTA vs no CTA (all reels)", "adj_factor", lib.adj_factor, none.adj_factor, "link_in_bio+shop_product", "none")
    ai = r[r.production == "ai_generated"]
    contrast("AI: high vs low shoppability", "adj_factor", ai[ai.shoppability == "high"].adj_factor, ai[ai.shoppability == "low"].adj_factor, "ai high", "ai low")
    groups = [x.adj_factor.dropna().values for _, x in ai.groupby("shoppability")]
    k = kruskal(*groups)
    res.append(dict(contrast="AI: shoppability high/medium/low", metric="adj_factor", group_a="kruskal k=%d" % len(groups),
                    n_a=int(sum(len(g) for g in groups)), test="kruskal", p=k.pvalue))

    # account monetization class vs reel performance (accounts' topic-page reels; selection-biased)
    cls = np.select([fl.affiliate_any, fl.digital_or_course, fl.services_b2b,
                     fl.any_revenue_path | fl.brand_contact | fl.deals_seen],
                    ["affiliate", "digital/course", "service/B2B", "other/contact only"], "none observed")
    fl2 = fl.assign(mon_class=cls)[["handle", "mon_class"]]
    m = r.merge(fl2, on="handle", how="inner")
    m = m[m.adj_factor.notna()]
    accm = m.groupby(["handle", "mon_class"]).adj_factor.median().reset_index()
    for c, x in accm.groupby("mon_class"):
        res.append(dict(contrast="Deep-profiled accounts by monetization class (account-level median of reel adj_factor)",
                        metric="adj_factor", group_a=c, n_a=len(x), median_a=x.adj_factor.median(),
                        n_b=int((m.mon_class == c).sum()), group_b="n_b = reels", test="descriptive"))
    k2 = kruskal(*[x.adj_factor.values for _, x in accm.groupby("mon_class")])
    res.append(dict(contrast="Deep-profiled accounts by monetization class", metric="adj_factor",
                    group_a="kruskal k=%d (account level)" % accm.mon_class.nunique(), n_a=len(accm), test="kruskal", p=k2.pvalue))
    pd.DataFrame(res).to_csv(os.path.join(OUT, "monetization_contrasts.csv"), index=False)
    print(summ.to_string())
    print(pd.DataFrame(res).to_string())


if __name__ == "__main__":
    main()
