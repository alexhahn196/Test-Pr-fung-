"""Diagramme aus scripts/model_output.json -> diagramme/*.png  (python3 scripts/charts.py)"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, NullFormatter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "diagramme")
os.makedirs(OUT, exist_ok=True)
D = json.load(open(os.path.join(ROOT, "scripts", "model_output.json"), encoding="utf-8"))

# Palette (validiert mit dataviz/validate_palette.js, light surface): Markt = Identität, feste Zuordnung
EN_C, DE_C, THIRD = "#2a78d6", "#eb6834", "#1baf7a"
SURF, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "font.family": "DejaVu Sans", "font.size": 10, "text.color": INK, "axes.labelcolor": INK2,
    "xtick.color": MUTED, "ytick.color": INK2, "axes.edgecolor": AXIS, "axes.linewidth": 0.8,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "grid.linestyle": "-",
    "axes.spines.top": False, "axes.spines.right": False,
})


def de_num(x):
    return f"{x:,.0f}".replace(",", ".")


def logfmt_x(ax, unit="€"):
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{de_num(x)} {unit}"))
    ax.xaxis.set_minor_formatter(NullFormatter())


def logfmt_y(ax, unit="€"):
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{de_num(x)} {unit}"))
    ax.yaxis.set_minor_formatter(NullFormatter())


def col(d):
    return DE_C if d["market"] == "DE" else EN_C


def mk_legend(ax, loc="lower right"):
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=DE_C, label="DE/DACH (deutschsprachig)"), Patch(color=EN_C, label="EN / US / International")],
              loc=loc, frameon=False, fontsize=9)


def title(ax, t, sub):
    ax.set_title(t, loc="left", fontsize=13, fontweight="bold", color=INK, pad=24)
    ax.text(0, 1.02, sub, transform=ax.transAxes, fontsize=9, color=INK2, va="bottom")


def millions(x, _):
    return f"{x/1e6:,.0f} Mio." if x >= 1e6 else f"{x/1e3:,.0f}k"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight")
    plt.close(fig)


top = [d for d in D][:15]

# 1) Score Top 15 ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7))
rows = list(reversed(top))
y = range(len(rows))
ax.barh(y, [d["score"] for d in rows], color=[col(d) for d in rows], height=0.62)
for i, d in enumerate(rows):
    ax.text(d["score"] + 0.6, i, f"{d['score']:.1f}", va="center", fontsize=9, color=INK2)
ax.set_yticks(list(y), [d["label"] + (" *" if d["synth"] else "") for d in rows])
ax.set_xlim(0, 72)
ax.set_xlabel("Gewichteter Score (0–100), Gewichtung laut Auftrag")
ax.grid(axis="y", visible=False)
title(ax, "Top-15 Nische × Markt nach Scorecard", "Abstände < 3 Punkte liegen innerhalb der Modellunsicherheit · * = Synthese aus zwei Top-Nischen")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=DE_C, label="DE/DACH (deutschsprachig)"), Patch(color=EN_C, label="EN / US / International")],
          loc="upper center", bbox_to_anchor=(0.45, -0.09), ncol=2, frameon=False, fontsize=9)
save(fig, "01_top_nischen_score.png")

# 2) Provision pro 1 Mio. Views: Base vs Strong (log) --------------------------------
allr = sorted(D, key=lambda d: d["Base"]["revenue_per_1m_eur"])
fig, ax = plt.subplots(figsize=(10, 10))
for i, d in enumerate(allr):
    b, s, c = d["Base"]["revenue_per_1m_eur"], d["Strong"]["revenue_per_1m_eur"], d["Conservative"]["revenue_per_1m_eur"]
    ax.plot([max(c, 1), s], [i, i], color=AXIS, lw=2, solid_capstyle="round", zorder=1)
    ax.scatter([max(c, 1)], [i], s=26, color=MUTED, zorder=2)
    ax.scatter([b], [i], s=60, color=col(d), zorder=3, edgecolor=SURF, linewidth=1.5)
    ax.scatter([s], [i], s=60, color=col(d), marker="D", zorder=3, edgecolor=SURF, linewidth=1.5)
    ax.text(s * 1.12, i, f"{de_num(b)} / {de_num(s)} €", va="center", fontsize=8, color=INK2)
ax.set_yticks(range(len(allr)), [d["label"] for d in allr], fontsize=8.5)
ax.set_xscale("log")
ax.set_xlim(1, 4000)
logfmt_x(ax)
ax.set_xlabel("Affiliate-Provision pro 1 Mio. organischer Views (nach USt, Retouren, Geo) – log. Skala")
ax.grid(axis="y", visible=False)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", color=MUTED, label="Conservative"),
                   Line2D([], [], marker="o", ls="", color=INK2, label="Base (Kreis)"),
                   Line2D([], [], marker="D", ls="", color=INK2, label="Strong (Raute)"),
                   Line2D([], [], marker="s", ls="", color=DE_C, label="DE/DACH"),
                   Line2D([], [], marker="s", ls="", color=EN_C, label="EN/US/INT")],
          loc="lower right", frameon=False, fontsize=8.5)
title(ax, "Provision pro 1 Mio. Views je Kombination", r"Beschriftung: Base / Strong in € · Empirie (quellen/K): Repost-Views ≈ 3 \$, Shopping-Content ≈ 500–900 \$ pro 1 Mio.")
save(fig, "02_provision_pro_1mio_views.png")

# 3) Benötigte Views für 10k Gewinn vs. realistische Reichweite ---------------------
fig, ax = plt.subplots(figsize=(10, 7.5))
rows = list(reversed(top))
for i, d in enumerate(rows):
    need = d["Strong"]["views_10k"]
    ax.barh(i, need, color=col(d), height=0.55, alpha=0.9)
    ax.scatter([d["reach_strong"]], [i], marker="|", s=260, color=INK, zorder=3, linewidths=2)
    ax.scatter([d["reach_exc"]], [i], marker="|", s=260, color=MUTED, zorder=3, linewidths=2)
    ax.text(need * 1.03, i, f"{need/1e6:,.0f} Mio.", va="center", fontsize=8.5, color=INK2)
ax.set_yticks(range(len(rows)), [d["label"] for d in rows], fontsize=9)
ax.xaxis.set_major_formatter(FuncFormatter(millions))
ax.set_xlabel("Views pro Monat")
ax.grid(axis="y", visible=False)
ax.legend(handles=[Line2D([], [], color=EN_C, lw=6, label="benötigte Views für 10k € Gewinn (Strong-Funnel), EN"),
                   Line2D([], [], color=DE_C, lw=6, label="… DE/DACH"),
                   Line2D([], [], color=INK, marker="|", ls="", markersize=14, mew=2, label="realistische Views (Strong-Reichweite, Monat 12)"),
                   Line2D([], [], color=MUTED, marker="|", ls="", markersize=14, mew=2, label="Ausnahme-Reichweite (Top-Page)")],
          loc="upper center", bbox_to_anchor=(0.4, -0.09), ncol=2, frameon=False, fontsize=8.5)
title(ax, "Views für 10.000 € Monatsgewinn – und was realistisch erreichbar ist", "Top-15 nach Score · Base-Funnel bräuchte 3–7× mehr Views (siehe 11_revenue_per_million_views.csv)")
save(fig, "03_views_fuer_10k.png")

# 4) AOV vs. Provision ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7))
for d in D:
    a, r, p = d["struct"]["aov_eur"], d["struct"]["comm_rate_weighted"] * 100, d["struct"]["comm_per_order_eff_eur"]
    ax.scatter(a, r, s=40 + p * 18, color=col(d), alpha=0.85, edgecolor=SURF, linewidth=1.5, zorder=3)
lab = {"K10", "K11", "K25", "K19", "K13", "K12", "K09", "K06", "K14", "K18", "K20", "K31", "K32", "K15"}
off = {"K15": (6, -10), "K31": (-10, 8), "K12": (6, 6), "K09": (8, -3), "K32": (5, -14)}
for d in D:
    if d["id"] in lab:
        ax.annotate(("Kitchen & Coffee (EN)" if d["id"] == "K32" else d["label"].split(" – ")[0] + (" (DE)" if d["market"] == "DE" else "")), (d["struct"]["aov_eur"], d["struct"]["comm_rate_weighted"] * 100),
                    xytext=off.get(d["id"], (6, 4)), textcoords="offset points", fontsize=8, color=INK2,
                    ha="right" if d["id"] == "K31" else "left")
ax.set_xscale("log")
ax.set_xticks([30, 50, 100, 200, 300])
logfmt_x(ax)
ax.set_xlabel("Gewichteter Warenkorb (AOV) der attribuierten Bestellungen, € – log. Skala")
ax.set_ylabel("Gewichtete Provision, % vom Warenkorb (nominal)")
title(ax, "AOV vs. Provisionssatz je Kombination", "Punktgröße = effektive Provision pro Bestellung · Amazon-lastige Nischen links unten (AOV 30–60 €, 3–5 %)")
mk_legend(ax, "upper right")
save(fig, "04_aov_vs_provision.png")

# 5) Competition vs Revenue -----------------------------------------------------------
import random
random.seed(3)
fig, ax = plt.subplots(figsize=(10, 7))
for d in D:
    x = d["vals"]["comp"] + random.uniform(-0.18, 0.18)
    yv = d["Strong"]["revenue_per_1m_eur"]
    ax.scatter(x, yv, s=70, color=col(d), edgecolor=SURF, linewidth=1.5, zorder=3)
    if d["rank"] <= 12 or d["vals"]["comp"] >= 4 or d["id"] in {"K19", "K14", "K05", "K29"}:
        ax.annotate(d["label"].split(" – ")[0][:26] + (" (DE)" if d["market"] == "DE" else ""), (x, yv), xytext=(6, 3), textcoords="offset points", fontsize=7.5, color=INK2)
ax.set_yscale("log")
ax.set_yticks([100, 200, 300, 500])
logfmt_y(ax)
ax.set_xticks([1, 2, 3, 4, 5], ["1\nstark gesättigt", "2", "3\nneutral", "4", "5\nkaum Konkurrenz"])
ax.set_xlabel("Competition Opportunity (Rubrik 1–5, belegt in 12_top10.md / quellen F, I, J)")
ax.set_ylabel("Provision pro 1 Mio. Views, Strong-Szenario (log)")
title(ax, "Konkurrenz-Lücke vs. Erlöspotenzial", "Rechts oben = hohe Monetarisierung bei wenig Konkurrenz · x leicht gestreut, damit Punkte lesbar bleiben")
mk_legend(ax, "upper left")
save(fig, "05_competition_vs_revenue.png")

# 6) Passivity vs Revenue ----------------------------------------------------------------
random.seed(5)
fig, ax = plt.subplots(figsize=(10, 7))
for d in D:
    x = d["vals"]["passiv"] + random.uniform(-0.18, 0.18)
    yv = d["Strong"]["revenue_per_1m_eur"]
    ax.scatter(x, yv, s=70, color=col(d), edgecolor=SURF, linewidth=1.5, zorder=3)
    if d["id"] in {"K32", "K31", "K09", "K08", "K13", "K12", "K19", "K20", "K29", "K15", "K10", "K04", "K01", "K03"}:
        ax.annotate(d["label"].split(" – ")[0][:26] + (" (DE)" if d["market"] == "DE" else ""), (x, yv), xytext=(6, 3), textcoords="offset points", fontsize=7.5, color=INK2)
ax.set_yscale("log")
ax.set_yticks([100, 200, 300, 500])
logfmt_y(ax)
ax.set_xticks([1, 2, 3, 4, 5], ["1\nhoher Pflegeaufwand", "2", "3", "4", "5\nsehr evergreen"])
ax.set_xlabel("Passivity / Evergreen (Rubrik 1–5, siehe 09_passivity_analysis.md)")
ax.set_ylabel("Provision pro 1 Mio. Views, Strong-Szenario (log)")
title(ax, "Passivität vs. Erlöspotenzial", "Rechts oben = hoher Ertrag pro View bei wenig laufender Pflege · Punkte ohne Label: siehe scorecard.csv")
mk_legend(ax, "upper left")
save(fig, "06_passivity_vs_revenue.png")

# 7) DE vs International (zwei Kleinmultiples, je eigene Achse) --------------------------
pairs = [("K02", "K01", "Desk Setups"), ("K04", "K05", "Home Decor Finds"), ("K06", "K07", "Küche/Gadgets"),
         ("K08", "K09", "Espresso-Setups"), ("K31", "K32", "Kitchen & Coffee *"), ("K15", "K14", "Amazon Finds/Gadgets"),
         ("K12", "K13", "Grill/BBQ"), ("K11", "K10", "Backyard Wellness")]
by = {d["id"]: d for d in D}
fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
import numpy as np
yy = np.arange(len(pairs))
h = 0.36
for ax, key, xl, sub in [
    (axes[0], lambda d: d["Base"]["revenue_per_1m_eur"], "Provision pro 1 Mio. Views, Base (€)", "Monetarisierung pro View"),
    (axes[1], lambda d: d["profit_strong_reach_strong"], "Gewinn/Monat bei Strong-Funnel × Strong-Reichweite (€)", "Absoluter Gewinn inkl. Reichweiten-Deckel")]:
    de = [key(by[a]) for a, b, n in pairs]
    en = [key(by[b]) for a, b, n in pairs]
    ax.barh(yy + h / 2, de, height=h, color=DE_C, label="DE/DACH")
    ax.barh(yy - h / 2, en, height=h, color=EN_C, label="EN/US/INT")
    for i in range(len(pairs)):
        ax.text(max(de[i], 0) + (max(de + en) * 0.01), yy[i] + h / 2, de_num(de[i]), va="center", fontsize=8, color=INK2)
        ax.text(max(en[i], 0) + (max(de + en) * 0.01), yy[i] - h / 2, de_num(en[i]), va="center", fontsize=8, color=INK2)
    ax.set_xlabel(xl, fontsize=9)
    ax.set_title(sub, loc="left", fontsize=10.5, color=INK, fontweight="bold")
    ax.grid(axis="y", visible=False)
    ax.axvline(0, color=AXIS, lw=0.8)
axes[0].set_yticks(yy, [n for a, b, n in pairs])
axes[0].invert_yaxis()
axes[1].legend(loc="lower right", frameon=False, fontsize=9)
fig.suptitle("DE/DACH vs. International: gleiche Nische, anderer Markt", x=0.01, ha="left", fontsize=13, fontweight="bold")
fig.text(0.01, 0.905, "Links: DE verdient pro View gleich viel oder mehr (5 % Amazon.de, 80 % monetarisierbares Publikum). Rechts: EN gewinnt absolut durch ~3× höheren Reichweiten-Deckel.",
         fontsize=9, color=INK2)
fig.tight_layout(rect=(0, 0, 1, 0.9))
save(fig, "07_de_vs_international.png")
print("ok", sorted(os.listdir(OUT)))
