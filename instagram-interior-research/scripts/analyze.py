"""Main analysis: builds the reel + competitor databases and all segment statistics.

Run after parse_topics.py, parse_accounts.py, parse_reels.py.
Outputs (research root):
  04_reel_database.csv, 02_competitor_database.csv (base columns; profile columns merged if present)
  data/processed/stats/*.csv  (one table per analysis dimension)
  data/processed/stats/summary.json
Metric definitions (see README):
  views        = play count shown on Instagram's public /popular/<topic>/ page (rounded as displayed)
  vpf          = views / followers (followers as shown on the public embed page at fetch time 2026-09-25)
  topic_index  = views / median views of all reels on the same topic page (controls for topic size)
  tier         = NORMAL <0.5x | GOOD 0.5-2x | VERY_GOOD 2-5x | VIRAL 5-20x | EXTREME_OUTLIER >=20x (vpf)
"""
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd
from scipy import stats as sst

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shortcode_time import shortcode_to_datetime  # noqa: E402
from topic_groups import topic_group  # noqa: E402
from parse_topics import parse_views  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "processed")
ST = os.path.join(P, "stats")
FETCH_DATE = datetime(2026, 9, 25, tzinfo=timezone.utc)
MIN_N = 15  # segments below this are reported but flagged low-confidence

LOCATION_MAP = [
    ("Dubai/UAE", r"dubai|abu dhabi|uae|emirates"), ("Bali/Indonesia", r"bali|ubud|uluwatu|indonesia|jakarta|lombok"),
    ("Maldives", r"maldiv"), ("Switzerland", r"swiss|switzerland|zermatt|st\.? moritz|gstaad|interlaken|alps"),
    ("Monaco", r"monaco|monte carlo"), ("New York", r"new york|nyc|manhattan|brooklyn"),
    ("Tokyo/Japan", r"tokyo|kyoto|japan|osaka"), ("Santorini/Mykonos/Greece", r"santorini|mykonos|greece|greek|athens"),
    ("Lake Como/Italy", r"como|amalfi|positano|italy|italia|tuscany|milan|rome|capri|sicily|dolomit"),
    ("Ibiza/Spain", r"ibiza|mallorca|marbella|spain|madrid|barcelona"), ("Miami/Florida", r"miami|florida|palm beach"),
    ("Los Angeles/California", r"los angeles|beverly|malibu|california|hollywood|bel air|la jolla|palm springs"),
    ("London/UK", r"london|england|uk\b|united kingdom|cotswold|scotland"), ("Saudi/Qatar/Gulf", r"saudi|riyadh|qatar|doha|kuwait|bahrain|oman|neom"),
    ("Morocco", r"morocc|marrakech|riad"), ("Mexico/Tulum", r"tulum|mexico|cabo|cancun"),
    ("France", r"france|paris|provence|nice|cannes|french riviera"), ("India", r"india|mumbai|delhi|bangalore|kerala|goa|hyderabad|pune|jaipur"),
    ("Thailand/SE Asia", r"thailand|phuket|bangkok|vietnam|philippines|malaysia|singapore"),
    ("USA other", r"texas|colorado|aspen|utah|arizona|hawaii|usa|united states|montana|new jersey|georgia|carolina"),
    ("Nordics/Iceland/Faroe", r"norway|iceland|faroe|sweden|finland|denmark|lapland|rovaniemi"),
    ("Other", r"."),
]


def load():
    topic = pd.read_csv(os.path.join(P, "topic_reels.csv"))
    uniq = pd.read_csv(os.path.join(P, "reels_unique.csv"))
    cov = pd.read_csv(os.path.join(P, "reels_cover_coded.csv")) if os.path.exists(os.path.join(P, "reels_cover_coded.csv")) else pd.DataFrame()
    acc = pd.read_csv(os.path.join(P, "accounts_followers.csv")) if os.path.exists(os.path.join(P, "accounts_followers.csv")) else pd.DataFrame()
    vid = pd.read_csv(os.path.join(P, "reels_video_coded.csv")) if os.path.exists(os.path.join(P, "reels_video_coded.csv")) else pd.DataFrame()
    return topic, uniq, cov, acc, vid


def canon_location(text):
    import re
    if not isinstance(text, str) or not text.strip() or text.strip().lower() in {"null", "none", "nan"}:
        return None
    t = text.lower()
    for name, rx in LOCATION_MAP:
        if re.search(rx, t):
            return name
    return None


def tier(v):
    if pd.isna(v):
        return None
    if v < 0.5:
        return "1_NORMAL"
    if v < 2:
        return "2_GOOD"
    if v < 5:
        return "3_VERY_GOOD"
    if v < 20:
        return "4_VIRAL"
    return "5_EXTREME_OUTLIER"


def build_reels(topic, uniq, cov, acc):
    # topic-normalized index: views / median views on the same topic page
    topic = topic.copy()
    topic["topic_median"] = topic.groupby("topic")["views"].transform("median")
    topic["topic_index"] = topic["views"] / topic["topic_median"]
    topic["topic_pct"] = topic.groupby("topic")["views"].rank(pct=True)
    tagg = topic.groupby("shortcode").agg(topic_index=("topic_index", "max"), topic_pct=("topic_pct", "max"),
                                          n_topics=("topic", "nunique"))
    df = uniq.merge(tagg, on="shortcode", how="left")
    df["topic_groups"] = df["topics"].fillna("").apply(lambda s: ";".join(sorted({topic_group(t)[0] for t in s.split(";") if t})))
    df["primary_group"] = df["topics"].fillna("").apply(lambda s: sorted([topic_group(t) for t in s.split(";") if t], key=lambda x: x[1])[0][0] if s else None)
    dt = df["shortcode"].apply(shortcode_to_datetime)
    df["posted_at_utc"] = dt.apply(lambda d: d.isoformat() if d else None)
    df["post_year"] = dt.apply(lambda d: d.year if d else None)
    df["age_days"] = dt.apply(lambda d: (FETCH_DATE - d).days if d else None)
    df["post_hour_utc"] = dt.apply(lambda d: d.hour if d else None)
    df["post_weekday"] = dt.apply(lambda d: d.strftime("%a") if d else None)
    if not cov.empty:
        df = df.merge(cov.drop(columns=["handle"]).rename(columns={"caption": "caption_full"}), on="shortcode", how="left")
    # followers: embed at coding time, fallback to follower lookup table
    if not acc.empty:
        fmap = acc.set_index("handle")["followers"].to_dict()
        pmap = acc.set_index("handle")["posts"].to_dict()
    else:
        fmap, pmap = {}, {}
    if "followers_at_fetch" not in df:
        df["followers_at_fetch"] = np.nan
    df["followers"] = df["followers_at_fetch"]
    df["followers_source"] = np.where(df["followers"].notna(), "embed_reel", None)
    miss = df["followers"].isna()
    df.loc[miss, "followers"] = df.loc[miss, "handle"].map(fmap)
    df.loc[miss & df["followers"].notna(), "followers_source"] = "embed_account_lookup"
    df["vpf"] = df["views"] / df["followers"]
    df["tier"] = df["vpf"].apply(tier)
    for c in ["likes", "comments"]:
        if c not in df:
            df[c] = np.nan
    df["likes_per_view"] = df["likes"] / df["views"]
    df["comments_per_view"] = df["comments"] / df["views"]
    df["comments_per_like"] = df["comments"] / df["likes"]
    df["views_per_day"] = df["views"] / df["age_days"].clip(lower=1)
    # size- and topic-adjusted performance: within-topic regression of log10(views) on log10(followers);
    # residual = how many log10 units a reel beats the expectation for its account size on its topic page.
    first_topic = df["topics"].fillna("").str.split(";").str[0]
    ok = df["views"].gt(0) & df["followers"].gt(0)
    y = np.log10(df.loc[ok, "views"]); x = np.log10(df.loc[ok, "followers"]); t = first_topic[ok]
    yd = y - y.groupby(t).transform("mean"); xd = x - x.groupby(t).transform("mean")
    b = float((xd * yd).sum() / (xd * xd).sum()) if (xd * xd).sum() > 0 else 0.0
    df["adj_resid"] = np.nan
    df.loc[ok, "adj_resid"] = yd - b * xd
    df["adj_factor"] = 10 ** df["adj_resid"]  # 1.0 = as expected for account size on that topic page; 2.0 = twice
    df.attrs["size_slope"] = b
    df["location"] = df.get("location_claimed", pd.Series(index=df.index, dtype=object)).apply(canon_location)
    df["location_from_topic"] = df["topics"].fillna("").apply(lambda s: canon_location(" ".join(t.replace("-", " ") for t in s.split(";") if topic_group(t)[0] == "location")))
    df["location_any"] = df["location"].fillna(df["location_from_topic"])
    df["status_views"] = np.where(df["views"].notna(), "VERIFIED (public topic page, rounded)", "UNKNOWN")
    df["status_followers"] = np.where(df["followers"].notna(), "VERIFIED (public embed, rounded, at fetch)", "UNKNOWN")
    df["status_codes"] = np.where(df.get("visual_status", pd.Series(index=df.index)).eq("ok"), "ESTIMATED (AI-assisted coding of cover frame + caption)", np.where(df.get("visual_status", pd.Series(index=df.index)).notna(), "ESTIMATED (caption only)", "UNKNOWN (not coded)"))
    return df


def theme_flags(df):
    """Theme membership for Part 16 (a reel can belong to several themes)."""
    rp = df.get("room_primary", pd.Series(index=df.index, dtype=object)).fillna("")
    rv = df.get("rooms_visible", pd.Series(index=df.index, dtype=object)).fillna("")
    bt = df.get("building_type", pd.Series(index=df.index, dtype=object)).fillna("")
    ls = df.get("landscape", pd.Series(index=df.index, dtype=object)).fillna("")
    hk = df.get("cover_hooks", pd.Series(index=df.index, dtype=object)).fillna("")
    tp = df["topics"].fillna("")
    th = {
        "Bedroom": rp.eq("bedroom"), "Living Room": rp.eq("living_room"), "Kitchen": rp.eq("kitchen"),
        "Bathroom": rp.eq("bathroom") | rp.eq("spa"), "Closet": rp.eq("closet"), "Dining": rp.eq("dining"),
        "Home Theater/Office/Library": rp.isin(["home_theater", "office"]),
        "Pool": rp.eq("pool") | hk.str.contains("pool") | rv.str.contains("pool"),
        "Outdoor/Terrace/Garden": rp.isin(["terrace_outdoor", "garden_landscape"]),
        "Exterior/Facade": rp.eq("exterior_facade"),
        "Villa": bt.eq("villa"), "Penthouse": bt.eq("penthouse"), "Mansion": bt.eq("mansion"),
        "Hotel/Resort": bt.eq("hotel_resort") | rp.isin(["hotel_room", "lobby_common"]),
        "Cabin/Chalet": bt.eq("cabin_chalet"), "Treehouse": bt.eq("treehouse"),
        "Apartment": bt.eq("apartment"), "Castle/Palace": bt.eq("castle_palace"), "Unusual Structure": bt.eq("unusual_structure"),
        "Mountain Home": ls.eq("mountain") | ls.eq("snow"), "Ocean/Beach Home": ls.eq("ocean_beach"),
        "Forest Home": ls.eq("forest"), "Desert Home": ls.eq("desert"), "Jungle/Tropical": ls.eq("jungle_tropical"),
        "Cliff": ls.eq("cliff"), "City Skyline": ls.eq("city_skyline"), "Lake/River": ls.eq("lake_river"),
        "Underwater": ls.eq("underwater"), "Rain Window": ls.eq("rain_window") | df.get("ambience_fx", pd.Series(index=df.index, dtype=object)).fillna("").str.contains("rain"),
        "Topic: AI pages": tp.str.contains(r"(?:^|;)ai-|midjourney|virtual-staging", regex=True),
    }
    return th


def seg_table(df, col, multi=False, metric_cols=("views", "vpf", "topic_index", "likes_per_view", "comments_per_view")):
    d = df[df["views"].notna()].copy()
    if multi:
        d = d.assign(_v=d[col].fillna("").astype(str).str.split(";")).explode("_v")
        d["_v"] = d["_v"].str.strip()
        d = d[d["_v"].ne("") & d["_v"].ne("none") & d["_v"].ne("nan")]
    else:
        d["_v"] = d[col].astype(str)
        d = d[~d["_v"].isin(["nan", "None", ""])]
    if d.empty:
        return pd.DataFrame()
    g = d.groupby("_v")
    out = pd.DataFrame({
        "n": g.size(),
        "median_views": g["views"].median(), "mean_views": g["views"].mean(),
        "p90_views": g["views"].quantile(0.9),
        "median_vpf": g["vpf"].median(), "n_vpf": g["vpf"].count(),
        "share_viral_5x": g["vpf"].apply(lambda s: (s >= 5).sum() / s.count() if s.count() else np.nan),
        "median_topic_index": g["topic_index"].median(),
        "median_adj_factor": g["adj_factor"].median(), "mean_adj_log10": g["adj_resid"].mean(), "n_adj": g["adj_resid"].count(),
        "share_beats_expectation_2x": g["adj_factor"].apply(lambda s: (s >= 2).sum() / s.count() if s.count() else np.nan),
        "share_top_quartile_on_topic_page": g["topic_pct"].apply(lambda s: (s >= 0.75).mean()),
        "median_likes_per_view": g["likes_per_view"].median(),
        "median_comments_per_view": g["comments_per_view"].median(),
        "median_comments_per_like": g["comments_per_like"].median() if "comments_per_like" in d else np.nan,
    })
    out["low_confidence"] = out["n"] < MIN_N
    # Kruskal-Wallis across categories with n>=MIN_N on topic_index
    return out.sort_values("median_adj_factor", ascending=False)


def kruskal(df, col, metric="topic_index", multi=False):
    d = df[df[metric].notna()]
    if multi:
        return None
    groups = [g[metric].values for k, g in d.groupby(col) if len(g) >= MIN_N]
    if len(groups) < 2:
        return None
    h, p = sst.kruskal(*groups)
    return {"H": round(float(h), 2), "p": float(p), "k": len(groups)}


def within_account(df, min_reels=5):
    """Top-10% vs bottom-50% within the same account (views on topic pages)."""
    d = df[df["views"].notna() & df.get("visual_status", pd.Series(index=df.index)).eq("ok")].copy()
    cnt = d.groupby("handle")["shortcode"].transform("count")
    d = d[cnt >= min_reels]
    if d.empty:
        return pd.DataFrame(), d
    d["acct_pct"] = d.groupby("handle")["views"].rank(pct=True, method="average")
    d["acct_rel"] = d["views"] / d.groupby("handle")["views"].transform("median")
    d["class"] = np.where(d["acct_pct"] >= 0.9, "top10", np.where(d["acct_pct"] <= 0.5, "bottom50", "middle"))
    return d, d


def main():
    os.makedirs(ST, exist_ok=True)
    topic, uniq, cov, acc, vid = load()
    df = build_reels(topic, uniq, cov, acc)
    summary = {"generated": FETCH_DATE.date().isoformat()}
    summary["n_topics"] = int(topic["topic"].nunique())
    summary["n_reels_unique"] = int(len(df))
    summary["n_reels_with_views"] = int(df["views"].notna().sum())
    summary["n_reels_coded_visual"] = int(df.get("visual_status", pd.Series()).eq("ok").sum())
    summary["n_reels_with_followers"] = int(df["followers"].notna().sum())
    summary["n_handles"] = int(df["handle"].nunique())
    v = df["views"].dropna()
    summary["views_quantiles"] = {q: float(v.quantile(q)) for q in [0.1, 0.25, 0.5, 0.75, 0.9, 0.99]}
    summary["vpf_quantiles"] = {q: float(df["vpf"].dropna().quantile(q)) for q in [0.1, 0.25, 0.5, 0.75, 0.9]} if df["vpf"].notna().any() else {}
    summary["tier_counts"] = df["tier"].value_counts().sort_index().to_dict()
    # age vs views correlation (to show lifetime accumulation bias)
    ok = df[["views", "age_days"]].dropna()
    if len(ok) > 10:
        r = sst.spearmanr(ok["views"], ok["age_days"])
        summary["spearman_views_age"] = {"rho": round(float(r.correlation), 3), "p": float(r.pvalue), "n": int(len(ok))}
    ok = df[["views", "followers"]].dropna()
    if len(ok) > 10:
        r = sst.spearmanr(ok["views"], ok["followers"])
        summary["spearman_views_followers"] = {"rho": round(float(r.correlation), 3), "p": float(r.pvalue), "n": int(len(ok))}

    dims_single = ["primary_group", "room_primary", "building_type", "landscape", "style_primary", "palette_temp", "brightness",
                   "lighting", "realism", "production", "shoppability", "visual_quality", "caption_hook_category", "cta_type",
                   "account_kind_hint", "language", "people_present", "view_through_window", "media_type", "ai_disclosed",
                   "location_any", "post_year", "post_hour_utc", "post_weekday", "caption_has_question", "caption_link_hint",
                   "caption_comment_cta"]
    dims_multi = ["materials", "dominant_colors", "ambience_fx", "cover_hooks", "rooms_visible", "topic_groups"]
    tests = {}
    for c in dims_single:
        if c in df:
            t = seg_table(df, c)
            if not t.empty:
                t.to_csv(os.path.join(ST, f"seg_{c}.csv"))
                k = kruskal(df, c)
                k2 = kruskal(df, c, metric="adj_resid")
                if k or k2:
                    tests[c] = {"topic_index": k, "adj_resid": k2}
    for c in dims_multi:
        if c in df:
            t = seg_table(df, c, multi=True)
            if not t.empty:
                t.to_csv(os.path.join(ST, f"seg_{c}.csv"))
    summary["kruskal_tests"] = tests
    summary["size_slope_log10views_on_log10followers_within_topic"] = round(df.attrs.get("size_slope", float("nan")), 3)

    # caption length / hashtags buckets
    if "caption_len" in df:
        df["caption_len_bucket"] = pd.cut(df["caption_len"], [-1, 0, 50, 150, 400, 1000, 100000], labels=["0", "1-50", "51-150", "151-400", "401-1000", "1000+"])
        df["hashtag_bucket"] = pd.cut(df["caption_hashtags"], [-1, 0, 3, 10, 20, 100], labels=["0", "1-3", "4-10", "11-20", "21+"])
        for c in ["caption_len_bucket", "hashtag_bucket"]:
            seg_table(df, c).to_csv(os.path.join(ST, f"seg_{c}.csv"))
    # followers bucket (account size)
    df["follower_bucket"] = pd.cut(df["followers"], [0, 1e4, 1e5, 5e5, 1e6, 1e10], labels=["<10k", "10k-100k", "100k-500k", "500k-1M", "1M+"])
    seg_table(df, "follower_bucket").to_csv(os.path.join(ST, "seg_follower_bucket.csv"))

    # themes (Part 16)
    th = theme_flags(df)
    rows = []
    for name, mask in th.items():
        d = df[mask & df["views"].notna()]
        if len(d) == 0:
            continue
        rows.append({"theme": name, "n": len(d), "median_views": d["views"].median(), "p90_views": d["views"].quantile(0.9),
                     "median_vpf": d["vpf"].median(), "share_viral_5x": (d["vpf"] >= 5).mean() if d["vpf"].notna().any() else np.nan,
                     "median_topic_index": d["topic_index"].median(), "median_adj_factor": d["adj_factor"].median(), "n_adj": int(d["adj_factor"].count()), "median_comments_per_view": d["comments_per_view"].median(),
                     "low_confidence": len(d) < MIN_N})
    pd.DataFrame(rows).sort_values("median_adj_factor", ascending=False).to_csv(os.path.join(ST, "themes.csv"), index=False)

    # topics table (demand/supply per topic page)
    ts = pd.read_csv(os.path.join(P, "topics_status.csv"))
    tt = topic.groupby("topic").agg(n=("shortcode", "count"), median_views=("views", "median"), max_views=("views", "max"),
                                    p90_views=("views", lambda s: s.quantile(0.9)), n_handles=("handle", "nunique"))
    lab = ts.drop_duplicates("slug_used").set_index("slug_used")["total_reels_label"]
    tt["total_reels_label"] = lab.reindex(tt.index)
    tt["group"] = [topic_group(t)[0] for t in tt.index]
    # supply proxy: total number of reels Instagram shows for the topic ("23K reels on Instagram")
    tt["reels_on_topic"] = tt["total_reels_label"].astype(str).str.extract(r"([\d.,]+\s*[KMB]?)\+?\s*reels", expand=False).apply(
        lambda s: parse_views(s.replace(" ", "")) if isinstance(s, str) else np.nan)
    # demand/supply: median views of the top reels shown per 1,000 reels competing for the topic
    tt["median_views_per_1k_reels"] = tt["median_views"] / (tt["reels_on_topic"] / 1000)
    # AI share on page
    if "production" in df:
        pr = topic.merge(df[["shortcode", "production", "realism", "account_kind_hint", "vpf"]], on="shortcode", how="left")
        tt["share_ai_generated"] = pr.groupby("topic")["production"].apply(lambda s: (s == "ai_generated").sum() / s.notna().sum() if s.notna().sum() else np.nan)
        tt["share_theme_pages"] = pr.groupby("topic")["account_kind_hint"].apply(lambda s: (s == "theme_page").sum() / s.notna().sum() if s.notna().sum() else np.nan)
        tt["median_vpf"] = pr.groupby("topic")["vpf"].median()
    tt.sort_values("median_views", ascending=False).to_csv(os.path.join(ST, "topics.csv"))
    # freshness per topic group: share of top-page reels posted in the last 180 days (+ how those recent reels perform)
    fr = topic.merge(df[["shortcode", "age_days", "production", "adj_factor"]], on="shortcode", how="left")
    fr["group"] = fr["topic"].apply(lambda t: topic_group(t)[0])
    rec = fr[fr["age_days"] <= 180]
    fg = fr.groupby("group").agg(n=("shortcode", "count"), share_recent_180d=("age_days", lambda s: (s <= 180).mean())).join(
        rec.groupby("group").agg(n_recent=("shortcode", "count"), recent_med_adj=("adj_factor", "median"),
                                 recent_ai_share=("production", lambda s: (s == "ai_generated").sum() / max(1, s.notna().sum()))))
    fg.sort_values("share_recent_180d", ascending=False).round(3).to_csv(os.path.join(ST, "freshness_by_group.csv"))
    if "production" in df:
        c = df[df["production"].notna()]
        summary["ai_share_by_post_year"] = c.groupby("post_year")["production"].apply(lambda s: round(float((s == "ai_generated").mean()), 3)).to_dict()

    # group-level
    seg_table(df.assign(_g=df["topic_groups"]), "_g", multi=True).to_csv(os.path.join(ST, "seg_topic_groups_all.csv"))

    # within-account comparison (Part 15)
    wa, _ = within_account(df)
    if not wa.empty:
        wa.to_csv(os.path.join(ST, "within_account_reels.csv"), index=False)
        comp = {}
        for c in ["style_primary", "room_primary", "realism", "palette_temp", "brightness", "lighting", "caption_hook_category",
                  "cta_type", "production", "shoppability", "building_type", "landscape", "people_present", "view_through_window"]:
            if c in wa:
                ct = pd.crosstab(wa[c].astype(str), wa["class"], normalize="columns")
                comp[c] = ct.round(3).to_dict()
        for c in ["cover_hooks", "materials", "ambience_fx"]:
            if c in wa:
                x = wa.assign(_v=wa[c].fillna("").astype(str).str.split(";")).explode("_v")
                x = x[x["_v"].ne("")]
                share = x.groupby(["class", "_v"])["shortcode"].nunique() / wa.groupby("class")["shortcode"].nunique()
                comp[c] = share.unstack(0).round(3).fillna(0).to_dict()
        num = {}
        for c in ["caption_len", "caption_hashtags", "caption_emojis", "age_days", "likes_per_view", "comments_per_view", "post_hour_utc"]:
            if c in wa:
                num[c] = wa.groupby("class")[c].median().round(4).to_dict()
        summary["within_account"] = {"n_accounts": int(wa["handle"].nunique()), "n_reels": int(len(wa)),
                                     "class_counts": wa["class"].value_counts().to_dict(), "numeric_medians": num}
        json.dump(comp, open(os.path.join(ST, "within_account_feature_shares.json"), "w"), indent=1, default=str)

    # extreme outliers vs normal (Part 14)
    if df["tier"].notna().any():
        comp = {}
        for c in ["style_primary", "room_primary", "realism", "production", "caption_hook_category", "account_kind_hint", "building_type", "landscape", "palette_temp", "brightness", "lighting", "follower_bucket"]:
            if c in df:
                comp[c] = pd.crosstab(df[c].astype(str), df["tier"], normalize="columns").round(3).to_dict()
        json.dump(comp, open(os.path.join(ST, "tier_feature_shares.json"), "w"), indent=1, default=str)

    # accounts
    ag = df.groupby("handle").agg(
        n_reels_sample=("shortcode", "count"), followers=("followers", "max"), posts=("posts_at_fetch", "max") if "posts_at_fetch" in df else ("shortcode", "count"),
        median_views=("views", "median"), max_views=("views", "max"), sum_views=("views", "sum"),
        median_vpf=("vpf", "median"), max_vpf=("vpf", "max"), median_topic_index=("topic_index", "median"), median_adj_factor=("adj_factor", "median"),
        first_post_seen=("posted_at_utc", "min"), last_post_seen=("posted_at_utc", "max"),
        topics=("topics", lambda s: ";".join(sorted({t for x in s.dropna() for t in x.split(";")}))[:400]),
    )
    for c, name in [("account_kind_hint", "account_kind"), ("production", "production_mode"), ("style_primary", "style_mode"), ("room_primary", "room_mode"), ("realism", "realism_mode"), ("language", "language_mode")]:
        if c in df:
            ag[name] = df.groupby("handle")[c].agg(lambda s: s.dropna().mode().iloc[0] if s.dropna().size else None)
    if "production" in df:
        ag["share_ai_generated"] = df.groupby("handle")["production"].apply(lambda s: (s == "ai_generated").sum() / s.notna().sum() if s.notna().sum() else np.nan)
    top = df.sort_values("views", ascending=False).groupby("handle").head(1).set_index("handle")
    ag["top_reel_url"] = top["url"]
    ag["instagram_url"] = ["https://www.instagram.com/" + h + "/" for h in ag.index]
    ag["follower_status"] = np.where(ag["followers"].notna(), "VERIFIED (public embed page, rounded, 2026-09-25)", "UNKNOWN")
    ag["views_status"] = "VERIFIED (public topic pages; sample, not full account history)"
    ag = ag.sort_values("max_views", ascending=False)
    ag.to_csv(os.path.join(P, "accounts_metrics.csv"))

    # write master reel database
    cols_first = ["shortcode", "url", "handle", "posted_at_utc", "age_days", "views", "views_text", "status_views", "followers",
                  "followers_source", "status_followers", "vpf", "tier", "likes", "comments", "likes_per_view", "comments_per_view",
                  "topic_index", "topic_pct", "topics", "topic_groups", "primary_group", "location_any", "status_codes"]
    rest = [c for c in df.columns if c not in cols_first and c not in {"caption", "source", "source_file"}]
    df[cols_first + rest].to_csv(os.path.join(ROOT, "04_reel_database.csv"), index=False)
    df.to_pickle(os.path.join(P, "reels_master.pkl"))
    json.dump(summary, open(os.path.join(ST, "summary.json"), "w"), indent=1, default=str)
    print(json.dumps(summary, indent=1, default=str)[:3000])


if __name__ == "__main__":
    main()
