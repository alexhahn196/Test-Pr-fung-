"""Erzeugt 18_accounts_to_watch.md aus 01_200_accounts.csv  (python3 scripts/watchlist.py)"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROWS = list(csv.DictReader(open(os.path.join(ROOT, "01_200_accounts.csv"), encoding="utf-8")))


def find(handle, strang):
    for r in ROWS:
        if r["handle"] == handle and r["quelle_strang"] == strang:
            return r
    raise KeyError(handle)


def num(v):
    v = v.replace(",", "").strip()
    try:
        return f"{int(float(v)):,}".replace(",", ".")
    except ValueError:
        return v


def views(v):
    try:
        x = float(v.replace(",", ""))
    except ValueError:
        return v
    return f"{x / 1e6:.2f}M".replace(".", ",") if x >= 1e6 else f"{x / 1e3:.0f}K"


# (Handle, Strang, Wachstum mit Label) – Wachstum nur aus datierten Snapshots, sonst UNKNOWN
NICHES = [
    ("1. KI-Oma kocht Familienrezepte – EN/US (und Hausmittel-Vergleich)", [
        ("grannyruthsredflags", "M1", "50.000 (10.09.) → 134.184 (26.09.): +168 % in 16 T (THIRD-PARTY OBSERVED)"),
        ("cookwithgrace2026", "M1", "90.147 (10.09.) → 127.822: +42 % in 16 T (THIRD-PARTY OBSERVED)"),
        ("chefdos_ia", "M1", "173.000 (17.09.) → 204.914: +18 % in 9 T (THIRD-PARTY OBSERVED)"),
        ("grandmaroseremedies", "M1", "82.000 (11.09.) → 154.788: +89 % in 15 T (THIRD-PARTY OBSERVED); Hausmittel-Variante"),
        ("yukis.ancient.kitchen", "M1", "118.000 (08.09.) → 125.000 (20.09.) (THIRD-PARTY OBSERVED); Hausmittel-Variante"),
        ("hua_jin123", "M1", "932.021 (12.08.) → 1.027.991: +10 % in 45 T (THIRD-PARTY OBSERVED)"),
        ("grannyspills", "M1", "2.046.576 (28.06.) → 2.162.172: +5,6 % in 90 T (THIRD-PARTY OBSERVED); Legacy-Benchmark"),
        ("grannybeatrice_", "M1", "95.771 (19.05.) → 101.259 (THIRD-PARTY OBSERVED)"),
    ]),
    ("2. KI-Oma-Küche / Cozy-Cooking – DE/DACH (keine DE-Accounts gefunden; Vorbilder)", [
        ("Feels Like HOME", "M5", "Start 18.06.2026; Abo-Verlauf UNKNOWN; 26 Millionen-Shorts in 120 T, 0 in 30 T (VERIFIED)"),
        ("Ai ka churcha", "M5", "Start 20.06.2026; Abo-Verlauf UNKNOWN; 16 / 3 Millionen-Shorts 120 T / 30 T (VERIFIED)"),
        ("chefdos_ia", "M1", "+18 % in 9 T (THIRD-PARTY OBSERVED); Beleg für nicht-englische Lokalisierung (PT/BR)"),
        ("cookwithgrace2026", "M1", "+42 % in 16 T (THIRD-PARTY OBSERVED)"),
        ("grannyruthsredflags", "M1", "+168 % in 16 T (THIRD-PARTY OBSERVED)"),
    ]),
    ("3. KI-Umbau Laube/Gartenhaus/Fachwerk – DE/DACH", [
        ("Bau Rausch", "M5", "Start 14.04.2026; Abo-Verlauf UNKNOWN; 19 Millionen-Shorts in 120 T, 0 in 30 T (VERIFIED)"),
        ("@not_your_basic_build", "M3", "UNKNOWN (IG-Zwilling von Bau Rausch/Vukovic)"),
        ("@vukovic_vlad", "M3", "UNKNOWN (Bio: „1B+ views in the 30 days“, SELF-REPORTED)"),
        ("Prime Production", "M5", "Start 04.04.2026; 31 / 6 Millionen-Shorts 120 T / 30 T (VERIFIED)"),
        ("grannybuilder", "M1", "UNKNOWN (IG); YT-Zwilling Start 27.03.2026"),
        ("TEXX EDITT", "M5", "Start 22.04.2026; 13 / 0 Millionen-Shorts 120 T / 30 T (VERIFIED); IG @texx_ed1tt"),
        ("CraftWorks", "M5", "Start 23.04.2026; 14 / 0 Millionen-Shorts (VERIFIED)"),
        ("WhiteDot", "M5", "Start 26.07.2026; 11 / 9 Millionen-Shorts 120 T / 30 T (VERIFIED) – wachsend"),
    ]),
    ("4. KI-Restaurierung mit realen Pflegeprodukten – DE/DACH", [
        ("storycar.barnfind", "M5", "Start 04.03.2026; 22 / 4 Millionen-Shorts 120 T / 30 T (VERIFIED)"),
        ("Virexa Build", "M5", "Start 28.06.2026; 9 / 3 Millionen-Shorts (VERIFIED); Reichweite je Hit 9,5M → 1,4M"),
        ("CUT CRAZE", "M5", "Start 16.04.2026; 16 / 1 Millionen-Shorts (VERIFIED) – gesättigt"),
        ("Steel Hangar", "M5", "Start 29.03.2026; 2 / 0 Millionen-Shorts (VERIFIED)"),
        ("Soft sound Space", "M5", "Start 28.07.2026; 2 / 0 Millionen-Shorts (VERIFIED)"),
        ("@cartuner.ai", "M3", "UNKNOWN"),
    ]),
    ("5. KI-Zeitreise durch deutsche Städte – DE/DACH", [
        ("chloe.vs.history", "M2", "547K (01.04.) → ~715K (18.09.): +31 % in 170 T; zuletzt +~9K in 13 T (THIRD-PARTY OBSERVED)"),
        ("histairy_films", "M2", "UNKNOWN (941K undatiert → 910K, evtl. rückläufig)"),
        ("ai.timetravelers", "M2", "49K (01.04.) → 49K: seitwärts (THIRD-PARTY OBSERVED)"),
        ("@hakimdecoded", "DE", "UNKNOWN"),
        ("@TomsZeitreisen", "DE", "Start 26.01.2026 → 46,3K; Verlauf UNKNOWN"),
        ("In The Easy Way", "M5", "Start 07.07.2026; 6 / 2 Millionen-Shorts 120 T / 30 T (VERIFIED); IG @intheeasyway"),
        ("The Minute Before", "M5", "Start 12.07.2026; 1 Millionen-Short (15,7M) bei 4.690 Abos (VERIFIED)"),
    ]),
]

out = [
    "# 18 – Accounts to Watch (Teil 26)",
    "",
    "**Stand:** 26.09.2026 · erzeugt mit [`scripts/watchlist.py`](scripts/watchlist.py) aus [`01_200_accounts.csv`](01_200_accounts.csv)",
    "",
    "Pro Top-5-Nische mindestens fünf Accounts zum selbst Ansehen.",
    "- **Follower:** Instagram THIRD-PARTY OBSERVED (AvatarFactory, Instastatistics, Snippets), YouTube/TikTok VERIFIED (öffentliche Profilanzeige).",
    "- **Wachstum:** nur aus datierten Snapshots, sonst **UNKNOWN**.",
    "- **KI-Status:** VERIFIED = Selbstauskunft, Offenlegungs-Hashtag oder Presse; LIKELY = nur Verzeichnis-Listung oder NexLev-Flag; UNKNOWN = nur visuell vermutet.",
    "",
    "> Hinweis: Für die Oma-Nische (#1/#2) ist der KI-Status der schnellsten Accounts nur **LIKELY**. Vor einer Entscheidung die Reels selbst ansehen (Artefakte, Konsistenz der Figur, Offenlegung).",
    "",
]
for title, items in NICHES:
    out += [f"## {title}", "", "| Handle | Plattform | Follower/Abos | Posts | Wachstum | Top-Reel/Short | KI-Status und Beleg |", "|---|---|---|---|---|---|---|"]
    for h, s, growth in items:
        r = find(h, s)
        top = r["top_reel_views"]
        top_s = "UNKNOWN" if top.startswith("UNKNOWN") or not top else views(top)
        if r["top_reel_url"] and not top_s.startswith("UNKNOWN"):
            top_s = f"[{top_s}]({r['top_reel_url']}) ({r['top_reel_datum']})"
        elif top.startswith("UNKNOWN") and "Likes" in top:
            top_s = top
        n1m = r["anzahl_reels_ueber_1m_bekannt"]
        if n1m and not n1m.startswith("UNKNOWN") and not n1m.startswith("0"):
            top_s += f"; ≥ 1 Mio.: {n1m}"
        beleg = r["ai_beleg"].replace("|", "/")
        if len(beleg) > 180:
            beleg = beleg[:177].rsplit(" ", 1)[0] + " …"
        plat = r["plattform"].split(" (")[0]
        out.append(f"| [{h}]({r['url']}) | {plat} | {num(r['follower_heute'])} | {r['posts'] or 'UNKNOWN'} | {growth} | {top_s} | **{r['ai_status']}**: {beleg} |")
    out.append("")

out += [
    "## Emerging Outliers außerhalb der Top 5 (zum Beobachten)",
    "",
    "| Handle | Plattform | Signal | Qualität |",
    "|---|---|---|---|",
    "| [zawpolyshorts](https://www.instagram.com/zawpolyshorts/) | IG (16.072 Follower, 9 Posts) | Reel mit 189.747 Likes; YT-Zwilling 112K Abos seit 05/2026 | THIRD-PARTY OBSERVED / VERIFIED |",
    "| [Tyler](https://www.youtube.com/channel/UCUJ0vqQ-m0aSrnixXLfx13g) | YT (56K seit 18.08.) | 23 Millionen-Shorts in 30 T (Story-Serien) | VERIFIED |",
    "| [Pixel Siuu](https://www.youtube.com/channel/UCwM2NFog1tdH0KaGcBXshPw) | YT (44K seit 06.08.) | 31 Millionen-Shorts in 30 T (Surreal) | VERIFIED |",
    "| [Super Labs](https://www.youtube.com/channel/UCl1tb2MB0JUNceBl67aDmGg) | YT (100K), IG @superlabs1 | 21 Millionen-Shorts in 30 T (Marvel-What-if) | VERIFIED |",
    "| [Valor Rise](https://www.youtube.com/channel/UCXiqWghIVpGAG4DrFPKoLow) | YT (254K seit 26.07.) | 8 Millionen-Shorts in 30 T (Reise-Fakten) | VERIFIED; KI UNKNOWN |",
    "",
]
open(os.path.join(ROOT, "18_accounts_to_watch.md"), "w", encoding="utf-8").write("\n".join(out))
print("ok")
