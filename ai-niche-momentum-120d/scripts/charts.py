"""Diagramme aus scripts/score_output.json -> diagramme/*.png  (python3 scripts/charts.py)"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "diagramme")
os.makedirs(OUT, exist_ok=True)
S = json.load(open(os.path.join(ROOT, "scripts", "score_output.json"), encoding="utf-8"))

# Palette wie in affiliate-theme-page-research/scripts/charts.py (validiert, light surface)
HI, MID, THIRD = "#eb6834", "#2a78d6", "#1baf7a"
SURF, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "font.family": "DejaVu Sans", "font.size": 10, "text.color": INK, "axes.labelcolor": INK2,
    "xtick.color": MUTED, "ytick.color": INK2, "axes.edgecolor": AXIS, "axes.linewidth": 0.8,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "grid.linestyle": "-",
    "axes.spines.top": False, "axes.spines.right": False,
})

SHORT = {
    "AI Senioren-Charaktere (Oma-Rezepte/Hausmittel/Ratgeber)": "Senioren-Charaktere (IG)",
    "AI Story-Serien (Roblox/3D, Rettung/Moral)": "Story-Serien",
    "AI Fußball-/Promi-Sketche": "Fußball-Sketche",
    "AI Kids-/Game-Figuren": "Kids/Game",
    "AI Film-/Marvel-What-if (3D)": "Film-What-if",
    "AI Babys/Familien-Comedy": "Babys",
    "AI Village-/Cozy-Cooking": "Village-/Cozy-Cooking",
    "AI Horror/Mystery": "Horror",
    "AI Tiere & Haustiere": "Tiere",
    "AI Nostalgie/Then & Now": "Nostalgie",
    "AI Surreal/VFX-Comedy": "Surreal",
    "AI Hausbau/Cabin/DIY-Timelapse": "Hausbau/Cabin/DIY",
    "AI Traumorte/„Places that don't feel real“": "Traumorte",
    "AI 3D-Explainer/Kuriositäten": "Explainer",
    "AI Autos/Luxus": "Autos",
    "AI Produkt-/Gadget-Konzepte": "Gadgets",
    "AI Tierrettung/Wholesome": "Tierrettung",
    "AI Geschichte/Zeitreise-POV": "Geschichte/Zeitreise",
    "AI Restoration/Satisfying": "Restoration",
    "AI Interior/Architektur": "Interior",
    "AI Garten/Obst": "Garten",
    "AI Personas/Virtual Influencer (Fashion/Lifestyle)": "Personas",
}

# Label-Versatz (dx, dy in Punkten) gegen Überlappungen
OFFS = {
    "Senioren-Charaktere (IG)": (-8, 8, "right"), "Village-/Cozy-Cooking": (8, 4, "left"),
    "Hausbau/Cabin/DIY": (8, 4, "left"), "Restoration": (8, -2, "left"), "Personas": (8, -2, "left"),
    "Interior": (-8, 2, "right"), "Geschichte/Zeitreise": (-8, 4, "right"), "Garten": (8, -4, "left"),
    "Nostalgie": (8, 6, "left"), "Horror": (8, 4, "left"), "Traumorte": (8, -2, "left"),
    "Autos": (-8, 4, "right"), "Tiere": (8, 4, "left"), "Gadgets": (0, -12, "center"),
    "Tierrettung": (-8, -2, "right"), "Explainer": (8, -5, "left"), "Babys": (8, -6, "left"),
    "Fußball-Sketche": (8, 2, "left"), "Story-Serien": (8, -2, "left"), "Film-What-if": (8, -2, "left"),
    "Kids/Game": (8, -6, "left"), "Surreal": (8, -6, "left"),
}


def title(ax, t, sub):
    ax.set_title(t, loc="left", fontsize=13, fontweight="bold", color=INK, pad=24)
    ax.text(0, 1.02, sub, transform=ax.transAxes, fontsize=9, color=INK2, va="bottom")


def chart_matrix():
    fig, ax = plt.subplots(figsize=(10.5, 7.2))
    for d in S.values():
        n = SHORT.get(d["name"], d["name"])
        c = HI if d["fit"] == "MEDIUM" else MUTED
        ax.scatter(d["momentum"], d["business"], s=70, color=c, edgecolor=SURF, linewidth=1, zorder=3)
        dx, dy, ha = OFFS.get(n, (8, 2, "left"))
        ax.annotate(n, (d["momentum"], d["business"]), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK if d["fit"] == "MEDIUM" else INK2, ha=ha, va="center")
    ax.axvline(50, color=AXIS, lw=1, zorder=1)
    ax.axhline(50, color=AXIS, lw=1, zorder=1)
    ax.set_xlim(25, 85)
    ax.set_ylim(25, 75)
    ax.set_xlabel("Momentum-Score (0–100)")
    ax.set_ylabel("Business-Score (0–100)")
    for x, y, t in ((83, 74, "Momentum + Business"), (83, 26.5, "Viral, aber kaum Kaufanlass"),
                    (26, 74, "Kaufnah, aber abkühlend"), (26, 26.5, "weder noch")):
        ax.text(x, y, t, fontsize=9, color=MUTED, ha="right" if x > 50 else "left",
                va="top" if y > 50 else "bottom", style="italic")
    ax.legend(handles=[Line2D([], [], marker="o", ls="", color=HI, label="Affiliate-Fit MEDIUM"),
                       Line2D([], [], marker="o", ls="", color=MUTED, label="Affiliate-Fit LOW")],
              loc="upper right", bbox_to_anchor=(1, 0.93), frameon=False, fontsize=9)
    ax.text(0, -0.11, "Kein Cluster erreicht Affiliate-Fit HIGH. Senioren-Charaktere = Instagram-Daten (Teil-Scores ESTIMATED), "
            "alle anderen = YouTube-Shorts-Proxy.", transform=ax.transAxes, fontsize=8, color=MUTED)
    title(ax, "Virality × Affiliate: nur ein Cluster liegt oben rechts",
          "22 KI-Cluster, Momentum (letzte 30–120 Tage) gegen Business-Score · Stand 26.09.2026 · Quelle: 06/14_*.csv")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "01_virality_affiliate_matrix.png"), dpi=160)
    plt.close(fig)


def chart_accel():
    # Millionen-Shorts letzte 30 T vs. Monatsdurchschnitt T31–120 (YouTube-Proxy, M5), nur originär KI-generierte Cluster
    keys = [k for k, d in S.items() if isinstance(d.get("hits120"), (int, float)) and d["hits120"] >= 9]
    rows = []
    for k in keys:
        d = S[k]
        prev = (d["hits120"] - d["hits30"]) / 3
        rows.append((SHORT.get(d["name"], d["name"]), d["hits30"], prev, d["fit"]))
    rows.sort(key=lambda r: r[1] - r[2])
    fig, ax = plt.subplots(figsize=(10.5, 7.2))
    y = range(len(rows))
    ax.barh([i + 0.2 for i in y], [r[2] for r in rows], height=0.38, color=AXIS, label="Ø je 30 Tage (Tage 31–120)")
    ax.barh([i - 0.2 for i in y], [r[1] for r in rows], height=0.38,
            color=[HI if r[3] == "MEDIUM" else MID for r in rows], label="letzte 30 Tage")
    ax.set_yticks(list(y))
    ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlabel("KI-Shorts mit ≥ 1 Mio. Views")
    ax.grid(axis="y", visible=False)
    for i, r in enumerate(rows):
        ax.text(max(r[1], r[2]) + 1.5, i, f"{r[1]} vs. {r[2]:.0f}", va="center", fontsize=8, color=INK2)
    ax.legend(handles=[Line2D([], [], lw=6, color=MID, label="letzte 30 T (Affiliate-Fit LOW)"),
                       Line2D([], [], lw=6, color=HI, label="letzte 30 T (Affiliate-Fit MEDIUM)"),
                       Line2D([], [], lw=6, color=AXIS, label="Ø je 30 T in Tagen 31–120")],
              loc="center right", frameon=False, fontsize=9)
    ax.text(0, -0.1, "YouTube-Shorts-Proxy (VERIFIED Views/Daten, AI-Flag LIKELY). Junge Shorts hatten weniger Zeit zu wachsen: "
            "Marktdurchschnitt 30 T ÷ Vorperiode = 0,69.", transform=ax.transAxes, fontsize=8, color=MUTED)
    title(ax, "Die kaufnahen Cluster hatten ihren Peak im Juni/Juli",
          "Millionen-Shorts junger KI-Kanäle: letzte 30 Tage gegen Ø der Tage 31–120 · Stand 26.09.2026 · Quelle: M5")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "02_momentum_30T_vs_vorher.png"), dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    chart_matrix()
    chart_accel()
    print("ok")
