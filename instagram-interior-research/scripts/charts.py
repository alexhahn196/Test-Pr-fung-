"""Static charts (PNG) for the markdown reports.

Design rules (dataviz skill): one measure per chart, no dual axes, single-hue bars for a single
series (no legend box), thin bars with values at the tip, hairline recessive grid, n shown in labels,
segments with n < MIN_N greyed out (low confidence).
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ST = os.path.join(ROOT, "data", "processed", "stats")
OUT = os.path.join(ROOT, "charts")
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
SERIES, MUTED = "#2a78d6", "#c9c8c2"
MIN_N = 15

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK, "font.size": 10, "axes.titlesize": 12, "axes.titleweight": "bold",
    "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
})


def fmt(v):
    if pd.isna(v):
        return "–"
    if abs(v) >= 1e6:
        return f"{v/1e6:.1f}M"
    if abs(v) >= 1e3:
        return f"{v/1e3:.0f}K"
    if abs(v) >= 10:
        return f"{v:.0f}"
    return f"{v:.2f}"


def hbar(df, value, label_col, title, subtitle, fname, xlabel, top=None, log=False, min_n=MIN_N, n_col="n"):
    d = df.copy()
    d = d[d[value].notna()]
    if top:
        d = d.sort_values(value, ascending=False).head(top)
    d = d.sort_values(value, ascending=True)
    if d.empty:
        return
    h = max(2.6, 0.32 * len(d) + 1.4)
    fig, ax = plt.subplots(figsize=(8.6, h))
    colors = [SERIES if (n_col not in d or d[n_col].iloc[i] >= min_n) else MUTED for i in range(len(d))]
    y = np.arange(len(d))
    ax.barh(y, d[value], height=0.55, color=colors, edgecolor=SURFACE, linewidth=2)
    labels = [f"{l}  (n={int(n)})" if n_col in d else str(l) for l, n in zip(d[label_col], d[n_col] if n_col in d else [0] * len(d))]
    ax.set_yticks(y, labels)
    for yi, v in zip(y, d[value]):
        ax.text(v * (1.04 if log else 1) + (0 if log else d[value].max() * 0.01), yi, fmt(v), va="center", ha="left", color=INK2, fontsize=9)
    if log:
        ax.set_xscale("log")
    ax.xaxis.grid(True, color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel(xlabel)
    ax.set_xlim(right=(d[value].max() * (3 if log else 1.18)))
    fig.suptitle(title, x=0.01, ha="left", fontsize=12, fontweight="bold", color=INK)
    import textwrap
    ax.set_title("\n".join(textwrap.wrap(subtitle, 88)), loc="left", fontsize=9, color=INK2, fontweight="normal")
    if value in ("median_adj_factor", "median_topic_index", "median_ch_index") and not log:
        ax.axvline(1.0, color=INK2, linewidth=1.4, zorder=3)  # 1.0 = as expected / typical
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, fname), dpi=150)
    plt.close(fig)


def seg(name):
    p = os.path.join(ST, f"seg_{name}.csv")
    if not os.path.exists(p):
        return None
    d = pd.read_csv(p)
    d = d.rename(columns={d.columns[0]: "cat"})
    d["cat"] = d["cat"].astype(str).str.replace("_", " ")
    return d


def main():
    os.makedirs(OUT, exist_ok=True)
    note = "Instagram public topic pages, 2026-09-25. Grey bars = n<15 (low confidence)."
    specs = [
        ("style_primary", "Median views by interior/architecture style", "views_by_style.png"),
        ("room_primary", "Median views by room / space type", "views_by_room.png"),
        ("caption_hook_category", "Median views by caption hook type", "views_by_caption_hook.png"),
        ("cover_hooks", "Median views by visual element in the cover frame", "views_by_visual_hook.png"),
        ("location_any", "Median views by location", "views_by_location.png"),
        ("realism", "Median views: fantasy vs. realistic", "views_by_realism.png"),
        ("production", "Median views by production mode (AI vs. real)", "views_by_production.png"),
        ("palette_temp", "Median views by color temperature", "views_by_palette.png"),
        ("materials", "Median views by dominant material", "views_by_material.png"),
        ("lighting", "Median views by lighting", "views_by_lighting.png"),
        ("account_kind_hint", "Median views by account type", "views_by_account_type.png"),
        ("building_type", "Median views by building type", "views_by_building.png"),
        ("landscape", "Median views by landscape/setting", "views_by_landscape.png"),
    ]
    for name, title, fn in specs:
        d = seg(name)
        if d is None or d.empty:
            continue
        hbar(d, "median_views", "cat", title, note, fn, "median views (log scale)", top=25, log=True)
        # main controlled metric: views vs. expectation for account size on the same topic page
        if "median_adj_factor" in d:
            hbar(d.rename(columns={"n": "n_all"}).rename(columns={"n_adj": "n"}), "median_adj_factor", "cat",
                 title.replace("Median views", "Performance vs. expectation (size- & topic-adjusted)"),
                 "Median of views ÷ expected views for the account's follower count on the same topic page (1.0 = as expected). " + note,
                 fn.replace("views_by", "adj_by"), "median adj_factor (× expected views)", top=25)
        # controlled metric: topic index (views relative to other reels on the same topic page)
        hbar(d, "median_topic_index", "cat", title.replace("Median views", "Topic-normalized performance"),
             "Median of views ÷ median views of the same topic page (1.0 = typical). " + note,
             fn.replace("views_by", "index_by"), "median topic index", top=25)
        if "share_viral_5x" in d and d["share_viral_5x"].notna().any():
            dd = d[d["n_vpf"] >= 5].copy() if "n_vpf" in d else d
            hbar(dd.assign(share=dd["share_viral_5x"] * 100), "share", "cat", title.replace("Median views", "Share of reels with views ≥5× followers"),
                 note, fn.replace("views_by", "viral_share_by"), "% of reels ≥5× followers", top=25, n_col="n_vpf" if "n_vpf" in dd else "n")
    # themes
    p = os.path.join(ST, "themes.csv")
    if os.path.exists(p):
        t = pd.read_csv(p)
        hbar(t, "median_views", "theme", "Median views by theme", note, "views_by_theme.png", "median views (log scale)", log=True)
        if "median_adj_factor" in t:
            hbar(t.rename(columns={"n": "n_all"}).rename(columns={"n_adj": "n"}), "median_adj_factor", "theme", "Performance vs. expectation by theme (size- & topic-adjusted)",
                 "1.0 = as expected for account size on the same topic page. " + note, "adj_by_theme.png", "median adj_factor (× expected views)")
        hbar(t, "median_topic_index", "theme", "Topic-normalized performance by theme", "1.0 = typical reel on the same topic page. " + note, "index_by_theme.png", "median topic index")
    # YouTube proxy: duration + visual change
    p = os.path.join(ST, "yt_duration_buckets.csv")
    if os.path.exists(p):
        d = pd.read_csv(p).dropna(subset=["n"])
        d["bucket"] = d["bucket"].astype(str)
        hbar(d.assign(order=range(len(d))), "median_ch_index", "bucket", "Video length vs. performance (YouTube Shorts PROXY)",
             "Views ÷ channel median, faceless interior/home Shorts channels via NexLev. Not Instagram data.", "views_by_length_yt_proxy.png", "median views relative to channel median", min_n=10)
    p = os.path.join(ST, "yt_visual_change.csv")
    if os.path.exists(p):
        d = pd.read_csv(p)
        hbar(d, "median_ch_index", "change_bucket", "Visual change (camera motion/cuts proxy) vs. performance",
             "YouTube Shorts PROXY: pixel change between auto-frames at 25/50/75 %. Not Instagram data.", "views_by_camera_yt_proxy.png", "median views relative to channel median", min_n=10)
    p = os.path.join(ST, "yt_title_hooks.csv")
    if os.path.exists(p):
        d = pd.read_csv(p)
        hbar(d, "median_ch_index", "hooks", "Title hook type vs. performance (YouTube Shorts PROXY)", "Views ÷ channel median. Not Instagram data.", "views_by_hook_yt_proxy.png", "median views relative to channel median", min_n=10)
    # accounts: views / followers
    p = os.path.join(ROOT, "data", "processed", "accounts_metrics.csv")
    if os.path.exists(p):
        a = pd.read_csv(p)
        a = a[(a["n_reels_sample"] >= 2) & a["median_vpf"].notna() & (a["followers"] >= 1000)]
        a["label"] = "@" + a["handle"] + " (" + a["followers"].apply(fmt) + ")"
        hbar(a.rename(columns={"n_reels_sample": "n"}), "median_vpf", "label", "Views ÷ followers by account (outperformance)",
             "Median over the account's reels found on topic pages (≥2 reels, ≥1K followers). n = reels in sample.", "vpf_by_account.png",
             "median views ÷ followers (log scale)", top=35, log=True, min_n=3)
    # topic demand vs supply scatter
    p = os.path.join(ST, "topics.csv")
    if os.path.exists(p):
        t = pd.read_csv(p).dropna(subset=["reels_on_topic", "median_views"])
        t = t[t["reels_on_topic"] > 0]
        fig, ax = plt.subplots(figsize=(9, 6.5))
        ax.scatter(t["reels_on_topic"], t["median_views"], s=36, color=SERIES, edgecolor=SURFACE, linewidth=2, alpha=0.9)
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.grid(True, color=GRID, linewidth=1); ax.set_axisbelow(True)
        lab = pd.concat([t.nlargest(10, "median_views"), t.nlargest(8, "median_views_per_1k_reels"), t.nlargest(6, "reels_on_topic")]).drop_duplicates("topic")
        for _, r in lab.iterrows():
            ax.annotate(r["topic"], (r["reels_on_topic"], r["median_views"]), textcoords="offset points", xytext=(5, 3), fontsize=8, color=INK2)
        ax.set_xlabel("reels Instagram lists for the topic (supply proxy, log)")
        ax.set_ylabel("median views of top reels on topic page (log)")
        fig.suptitle("Demand vs. supply per topic page", x=0.01, ha="left", fontsize=12, fontweight="bold")
        ax.set_title("Upper-left = high views with few competing reels (candidate gaps). Source: Instagram topic pages, 2026-09-25.",
                     loc="left", fontsize=9, color=INK2, fontweight="normal")
        fig.tight_layout(); fig.savefig(os.path.join(OUT, "topics_demand_vs_supply.png"), dpi=150); plt.close(fig)
    print("charts:", sorted(os.listdir(OUT)))


if __name__ == "__main__":
    main()
