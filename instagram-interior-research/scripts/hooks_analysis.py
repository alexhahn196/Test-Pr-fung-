"""Hook analysis for 07_hooks.md (Teil 8/9): caption first-line hooks and cover-text hooks.

Inputs : data/processed/reels_master.pkl (built by scripts/analyze.py)
Outputs: data/processed/stats/hooks_caption_by_production.csv  caption hook category x (all / AI / real footage)
         data/processed/stats/hooks_cover_text_categories.csv  rule-based category of on-cover text (all / AI)
         data/processed/stats/hooks_cover_text_words.csv       cover-text length (words) buckets (all / AI)
         data/processed/stats/hooks_contrasts.csv              Mann-Whitney + bootstrap CI for hook contrasts
         data/processed/stats/hooks_kruskal.csv                Kruskal-Wallis across hook categories (n>=15)
         data/processed/stats/hooks_cover_elements_ai.csv      cover elements (multi-label) with/without, all and AI
         data/processed/stats/hooks_ai_curiosity_subtypes.csv  AI curiosity captions by sub-type (post-hoc)
         data/processed/stats/hooks_yt_by_channel.csv          YouTube title hooks per channel (PROXY)
         data/processed/stats/hooks_cover_rule_agreement.csv   rule-based cover category vs AI-coded caption hook

Metric: adj_factor (views vs. expectation for account size on the same topic page), comments per view.
Cover-text categories are assigned by transparent keyword rules (first match wins, see RULES); they are
ESTIMATED. Agreement with the AI-coded caption hook is reported where cover text == caption first line.
"""
import os
import re

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "processed")
ST = os.path.join(P, "stats")
RNG = np.random.default_rng(7)

LOC = (r"dubai|bali|maldives|switzerland|swiss|ibiza|amalfi|italy|tokyo|japan|london|paris|new york|nyc|morocco|"
       r"marrakech|mexico|tulum|santorini|greece|como|monaco|miami|malibu|california|india|kerala|hunza|skardu|"
       r"faroe|iceland|norway|sri lanka|thailand|tashkent|uzbek|riyadh|saudi|barcelona|spain|portugal|lisbon|"
       r"bora bora|mykonos|france|germany|münchen|munich|africa|seattle|florida|texas|australia|canada|london")
RULES = [  # (category, regex) - first match wins; order matters
    ("promotional", r"\+\d{6,}|www\.|\.com\b|contact|for sale|book now|limited time|\bsale\b|\bshop\b|collection|"
                    r"hotels? & resorts|realty|studio\b|designs?\b\s*$|^@\S+$"),
    ("choice", r"\bwhich\b|\bpick\b|\bchoose\b|would you rather|\bvs\.?\b|❌.*✅|\bor\s*(\.\.\.|…|\?)|\bor\b.+\?"),
    ("pov", r"\bpov\b"),
    ("money", r"[$€£₹]|\bmillion|\bbillion|\bcrore|\blakh|\bdirham|\bprice|\bcost|\bbudget|\brent\b|\bcheap|"
              r"\bafford|\bworth\b|\bspent\b|\bpaid\b"),
    ("status", r"billionaire|millionaire|richest|most expensive|celebrit|\bowner of\b|\belite\b"),
    ("instructional", r"how to|\btips?\b|\bideas?\b|\bways?\b|\bguide\b|\bsteps?\b|must.?haves?|\bhacks?\b|\bdiy\b|"
                      r"\bitinerary\b|\bmistakes?\b"),
    ("contrarian", r"^(don'?t|stop|never|nobody|forget)\b|\bwasting\b|\boverrated\b|\bwrong\b|\binstead of\b"),
    ("curiosity", r"wait for it|wait till|watch till|\bsecret\b|\bhidden\b|won'?t believe|\bcraziest\b|\bfirst\b|"
                  r"\bworld'?s\b|\bwhat happens\b|\binside\b|\bguess\b|\bnobody\b|\bunbelievable\b|\bimpossible\b|🤯|😱|"
                  r"\.\.\.|…"),
    ("question", r"\?"),
    ("fantasy", r"\bimagine\b|\bdream|\bif only\b|\bfairy|\bmagic|\bheaven|\bparadise\b"),
    ("aspirational", r"\bmy type\b|\bone day\b|\bgoals?\b|\bi want\b|\bsomeday\b|\bquiet life\b|\bmanifest|"
                     r"\bperfect\b|\bmy (dream|home|room|house)\b|\bfeel(s|ing)?\b"),
    ("location", r"📍|\b(" + LOC + r")\b"),
]


def classify(text):
    t = str(text).strip()
    if not t:
        return None
    low = t.lower()
    for cat, rx in RULES:
        if re.search(rx, low, re.IGNORECASE):
            return cat
    return "descriptive"


def seg(d, col):
    g = d.groupby(col)
    out = pd.DataFrame({
        "n": g.size(),
        "n_adj": g["adj_factor"].count(),
        "median_views": g["views"].median(),
        "median_adj_factor": g["adj_factor"].median(),
        "share_beats_expectation_2x": g["adj_factor"].apply(lambda s: (s >= 2).sum() / s.count() if s.count() else np.nan),
        "share_viral_5x": g["vpf"].apply(lambda s: (s >= 5).sum() / s.count() if s.count() else np.nan),
        "median_comments_per_view": g["comments_per_view"].median(),
    })
    out["low_confidence"] = out["n_adj"] < 15
    return out.reset_index().sort_values("median_adj_factor", ascending=False)


def boot_ratio(a, b, n=2000):
    a, b = np.asarray(a), np.asarray(b)
    r = [np.median(RNG.choice(a, len(a))) / np.median(RNG.choice(b, len(b))) for _ in range(n)]
    return np.percentile(r, [2.5, 97.5])


def contrast(name, a, b, metric="adj_factor"):
    a = a[metric].dropna(); b = b[metric].dropna()
    if len(a) < 5 or len(b) < 5:
        return None
    lo, hi = boot_ratio(a, b)
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    return {"contrast": name, "metric": metric, "n_a": len(a), "median_a": round(float(a.median()), 5), "n_b": len(b),
            "median_b": round(float(b.median()), 5), "ratio_a_over_b": round(float(a.median() / b.median()), 3),
            "ci95_low": round(float(lo), 3), "ci95_high": round(float(hi), 3), "mannwhitney_p": round(float(p), 5),
            "significant_0.05": p < 0.05}


def kruskal(d, col, metric):
    groups = [g[metric].dropna().values for _, g in d.groupby(col) if g[metric].count() >= 15]
    if len(groups) < 2:
        return None
    h, p = stats.kruskal(*groups)
    return {"dimension": col, "metric": metric, "k": len(groups), "H": round(float(h), 2), "p": round(float(p), 5)}


def main():
    df = pd.read_pickle(os.path.join(P, "reels_master.pkl"))
    d = df[df["caption_hook_category"].notna()].copy()
    d["prod_grp"] = np.where(d["production"] == "ai_generated", "ai", np.where(d["production"] == "real_footage", "real", "other"))

    # 1) caption hook category by production
    rows = []
    for label, sub in [("all", d), ("ai", d[d["prod_grp"] == "ai"]), ("real", d[d["prod_grp"] == "real"])]:
        s = seg(sub, "caption_hook_category"); s.insert(0, "subset", label); rows.append(s)
    pd.concat(rows).to_csv(os.path.join(ST, "hooks_caption_by_production.csv"), index=False)

    # 2) cover text categories (rule-based)
    d["cover_text_clean"] = d["cover_text"].fillna("").astype(str).str.strip()
    d["cover_text_cat"] = d["cover_text_clean"].apply(classify)
    d.loc[d["cover_text_clean"] == "", "cover_text_cat"] = "no_cover_text"
    rows = []
    for label, sub in [("all", d), ("ai", d[d["prod_grp"] == "ai"])]:
        s = seg(sub, "cover_text_cat"); s.insert(0, "subset", label); rows.append(s)
    pd.concat(rows).to_csv(os.path.join(ST, "hooks_cover_text_categories.csv"), index=False)

    # agreement check: cover text equals caption first line (normalised) -> compare rule category vs AI-coded caption hook
    norm = lambda s: re.sub(r"[^a-z0-9 ]", "", str(s).lower()).strip()
    same = d[(d["cover_text_clean"] != "") & (d["cover_text_clean"].apply(norm) == d["caption_first_line"].apply(norm))]
    agree = (same["cover_text_cat"] == same["caption_hook_category"]).mean() if len(same) else np.nan

    # 3) cover text length in words
    wc = d["cover_text_clean"].str.split().str.len().fillna(0)
    d["cover_words"] = pd.cut(wc, [-1, 0, 3, 7, 12, 1000], labels=["0 (none)", "1-3", "4-7", "8-12", "13+"])
    rows = []
    for label, sub in [("all", d), ("ai", d[d["prod_grp"] == "ai"])]:
        s = seg(sub, "cover_words"); s.insert(0, "subset", label); rows.append(s)
    pd.concat(rows).to_csv(os.path.join(ST, "hooks_cover_text_words.csv"), index=False)

    # 4) contrasts
    a = d[d["adj_factor"].notna()]
    ai = a[a["prod_grp"] == "ai"]
    cat = "caption_hook_category"
    C = [
        contrast("AI: curiosity caption vs other AI captions", ai[ai[cat] == "curiosity"], ai[ai[cat] != "curiosity"]),
        contrast("All: curiosity caption vs others", a[a[cat] == "curiosity"], a[a[cat] != "curiosity"]),
        contrast("Real footage: curiosity caption vs others", a[(a.prod_grp == "real") & (a[cat] == "curiosity")], a[(a.prod_grp == "real") & (a[cat] != "curiosity")]),
        contrast("AI: choice caption vs other AI captions", ai[ai[cat] == "choice"], ai[ai[cat] != "choice"]),
        contrast("AI: choice caption vs others (comments/view)", ai[ai[cat] == "choice"], ai[ai[cat] != "choice"], "comments_per_view"),
        contrast("AI: descriptive caption vs other AI captions", ai[ai[cat] == "descriptive"], ai[ai[cat] != "descriptive"]),
        contrast("AI: aspirational caption vs other AI captions", ai[ai[cat] == "aspirational"], ai[ai[cat] != "aspirational"]),
        contrast("All: question caption vs others", a[a[cat] == "question"], a[a[cat] != "question"]),
        contrast("All: instructional caption vs others", a[a[cat] == "instructional"], a[a[cat] != "instructional"]),
        contrast("All: contrarian caption vs others", a[a[cat] == "contrarian"], a[a[cat] != "contrarian"]),
        contrast("All: status caption vs others", a[a[cat] == "status"], a[a[cat] != "status"]),
        contrast("All: POV caption vs others", a[a[cat] == "pov"], a[a[cat] != "pov"]),
        contrast("All: price claimed (caption/cover) vs none", a[a["price_claimed"].notna()], a[a["price_claimed"].isna()]),
        contrast("All: cover text 1-7 words vs 8+ words", a[a["cover_words"].isin(["1-3", "4-7"])], a[a["cover_words"].isin(["8-12", "13+"])]),
        contrast("All: cover text 1-7 words vs no cover text", a[a["cover_words"].isin(["1-3", "4-7"])], a[a["cover_words"] == "0 (none)"]),
        contrast("All: cover text 8+ words vs no cover text", a[a["cover_words"].isin(["8-12", "13+"])], a[a["cover_words"] == "0 (none)"]),
        contrast("AI: cover text 8+ words vs 1-7 words", ai[ai["cover_words"].isin(["8-12", "13+"])], ai[ai["cover_words"].isin(["1-3", "4-7"])]),
        contrast("AI: cover text 1-7 words vs no cover text", ai[ai["cover_words"].isin(["1-3", "4-7"])], ai[ai["cover_words"] == "0 (none)"]),
        contrast("Real footage: cover text 8+ words vs 1-7 words", a[(a.prod_grp == "real") & a["cover_words"].isin(["8-12", "13+"])], a[(a.prod_grp == "real") & a["cover_words"].isin(["1-3", "4-7"])]),
        contrast("Non-lifestyle accounts: cover text 8+ words vs 1-7 words", a[(a["account_kind_hint"] != "lifestyle_influencer") & a["cover_words"].isin(["8-12", "13+"])], a[(a["account_kind_hint"] != "lifestyle_influencer") & a["cover_words"].isin(["1-3", "4-7"])]),
        contrast("All: cover text choice vs other cover texts", a[a["cover_text_cat"] == "choice"], a[~a["cover_text_cat"].isin(["choice", "no_cover_text"])]),
        contrast("All: cover text money vs other cover texts", a[a["cover_text_cat"] == "money"], a[~a["cover_text_cat"].isin(["money", "no_cover_text"])]),
        contrast("All: cover text curiosity vs other cover texts", a[a["cover_text_cat"] == "curiosity"], a[~a["cover_text_cat"].isin(["curiosity", "no_cover_text"])]),
        contrast("All: cover text promotional/branding vs other cover texts", a[a["cover_text_cat"] == "promotional"], a[~a["cover_text_cat"].isin(["promotional", "no_cover_text"])]),
    ]
    pd.DataFrame([c for c in C if c]).to_csv(os.path.join(ST, "hooks_contrasts.csv"), index=False)

    # 5) Kruskal
    K = [kruskal(a, cat, "adj_resid"), kruskal(ai, cat, "adj_resid"), kruskal(a, cat, "comments_per_view"),
         kruskal(ai, cat, "comments_per_view"), kruskal(a[a["cover_text_cat"] != "no_cover_text"], "cover_text_cat", "adj_resid"),
         kruskal(a, "cover_words", "adj_resid")]
    k = pd.DataFrame([x for x in K if x])
    k["subset"] = ["all", "ai", "all", "ai", "all_with_cover_text", "all"][: len(k)]
    k.to_csv(os.path.join(ST, "hooks_kruskal.csv"), index=False)

    # 5b) cover elements within AI (median adj with / without, Mann-Whitney) - multi-label cover_hooks
    rows = []
    for label, sub in [("all", a), ("ai", ai)]:
        tags = sorted({t for v in sub["cover_hooks"].dropna() for t in str(v).split(";") if t})
        for t in tags:
            has = sub["cover_hooks"].fillna("").str.split(";").apply(lambda l: t in l)
            x, y2 = sub.loc[has, "adj_factor"], sub.loc[~has, "adj_factor"]
            if len(x) >= 5:
                rows.append({"subset": label, "cover_hook": t, "n_with": len(x), "median_adj_with": round(x.median(), 3),
                             "median_adj_without": round(y2.median(), 3), "share_viral_5x_with": round((sub.loc[has, "vpf"] >= 5).mean(), 3),
                             "mannwhitney_p": round(stats.mannwhitneyu(x, y2).pvalue, 4), "low_confidence": len(x) < 15})
    pd.DataFrame(rows).to_csv(os.path.join(ST, "hooks_cover_elements_ai.csv"), index=False)

    # 5c) AI curiosity captions: process/build narrative vs secret/hidden vs other (post-hoc sub-typing, keyword rules)
    cur = ai[ai[cat] == "curiosity"].copy()
    low = cur["caption_first_line"].fillna("").str.lower()
    cur["cur_type"] = np.where(low.str.contains(r"buil|construct|turn(?:ed|s)? .* into|from .* to|transform|process|empty|makeover|becomes"),
                               "process_build", np.where(low.str.contains(r"secret|hidden|beneath|underground|bunker"), "secret_hidden", "other"))
    ct = cur.groupby("cur_type").agg(n=("adj_factor", "count"), median_adj_factor=("adj_factor", "median"),
                                     median_views=("views", "median")).reset_index()
    ct["low_confidence"] = ct["n"] < 15
    ct.to_csv(os.path.join(ST, "hooks_ai_curiosity_subtypes.csv"), index=False)

    # 6) YouTube title hooks by channel (PROXY) - shows channel concentration of each hook
    import ast
    y = pd.read_csv(os.path.join(P, "youtube_shorts.csv"))
    y["hook"] = y["hooks"].apply(ast.literal_eval)
    e = y.explode("hook")
    yc = e.groupby(["hook", "channel"]).agg(n=("video_id", "count"), median_ch_index=("ch_index", "median")).reset_index()
    yc.to_csv(os.path.join(ST, "hooks_yt_by_channel.csv"), index=False)

    # 7) tag rows for agreement check
    pd.DataFrame([{"n_cover_equals_first_line": len(same), "agreement_rule_vs_coded": round(float(agree), 3)}]).to_csv(
        os.path.join(ST, "hooks_cover_rule_agreement.csv"), index=False)

    print("cover text == caption first line:", len(same), "agreement rule vs coded:", round(float(agree), 3))
    print(pd.read_csv(os.path.join(ST, "hooks_kruskal.csv")).to_string())


if __name__ == "__main__":
    main()
