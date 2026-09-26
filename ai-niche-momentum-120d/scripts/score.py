"""
Momentum-, Business- und Combined-Score je KI-Nischen-Cluster + Zusammenführung der Rohdaten.
Ausführen: python3 scripts/score.py
Erzeugt: 01_200_accounts.csv, 02_verified_ai_accounts.csv, 03_30_day_growth.csv, 04_90_day_growth.csv,
         06_momentum_scores.csv, 07_top_reels.csv, 11_affiliate_economics.csv, 14_combined_scores.csv, scripts/score_output.json
Quellen: quellen/raw_*.csv, quellen/M5_youtube_proxy_momentum.md (Tabellen 3+4), quellen/R2_affiliate_fit_momentum_clusters.md
"""
import csv
import datetime as dt
import json
import math
import os
import statistics as st
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(ROOT, "quellen")
TODAY = dt.date(2026, 9, 26)


def rd(name):
    with open(os.path.join(Q, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def wr(name, rows, cols):
    with open(os.path.join(ROOT, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def num(x):
    try:
        return float(str(x).replace(".", "").replace(",", ".")) if isinstance(x, str) and x.count(".") > 1 else float(x)
    except Exception:
        return None


# ------------------------------------------------------------------ 1) Accounts zusammenführen
IG_FILES = [("M1", "raw_accounts_M1.csv"), ("M2", "raw_accounts_M2.csv"), ("M3", "raw_accounts_M3.csv"),
            ("M4", "raw_accounts_M4.csv"), ("DE", "raw_accounts_DE.csv")]
acc = []
for src, f in IG_FILES:
    for r in rd(f):
        r = dict(r)
        r["quelle_strang"] = src
        acc.append(r)
IG_COLS = list(rd("raw_accounts_M1.csv")[0].keys())

yt = rd("raw_youtube_proxy_channels.csv")
for r in yt:
    start = r["start_erstes_video"][:10]
    acc.append({
        "handle": r["kanal"], "url": r["youtube_url"], "plattform": "YouTube Shorts (Proxy)",
        "nische_cluster": r["nische_cluster"], "unter_nische": r["unter_nische"], "land_sprache": r["sprache_land"],
        "account_alter_oder_start": start, "erstes_sichtbares_posting": start, "start_datenqualitaet": "VERIFIED (ältester Short, youtube.com)",
        "follower_heute": r["abonnenten"], "follower_heute_datum": "2026-09-26", "follower_heute_dq": "VERIFIED",
        "follower_vor_30d": "UNKNOWN", "follower_vor_60d": "UNKNOWN", "follower_vor_90d": "UNKNOWN", "follower_vor_120d": "UNKNOWN",
        "follower_historie_quelle": "keine Abo-Historie (Social Blade gesperrt)", "follower_historie_dq": "UNKNOWN",
        "posts": r["uploads"], "posts_dq": "VERIFIED", "median_reel_views": r["median_views"], "median_dq": "VERIFIED",
        "top_reel_url": r["top_short_url"], "top_reel_views": r["top_short_views"], "top_reel_datum": r["top_short_datum"], "top_reels_dq": "VERIFIED",
        "anzahl_reels_ueber_1m_bekannt": r["shorts_ueber_1m_letzte_120d"],
        "ai_status": ("VERIFIED" if r["ai_status"].startswith("VERIFIED") else ("LIKELY" if r["ai_status"].startswith("LIKELY") else ("BESTRITTEN" if "BESTRITTEN" in r["ai_status"] else "UNKNOWN"))),
        "ai_beleg": r["ai_beleg"], "link_in_bio": r["instagram_handle_falls_verlinkt"], "quelle_urls": r["youtube_url"],
        "pruefdatum": "2026-09-26", "notizen": f"Shorts ≥1M: 120T={r['shorts_ueber_1m_letzte_120d']} / 30T={r['shorts_ueber_1m_letzte_30d']}; " + r["notizen"][:300],
        "quelle_strang": "M5",
    })
cols = ["quelle_strang"] + IG_COLS
wr("01_200_accounts.csv", acc, cols)
ver = [a for a in acc if str(a.get("ai_status", "")).startswith("VERIFIED")]
wr("02_verified_ai_accounts.csv", ver, cols)


# ------------------------------------------------------------------ 2) Wachstum 30/90 Tage (nur datierte Werte)
def f2(x):
    if x is None:
        return None
    s = str(x).split("(")[0].strip().replace(".", "").replace(",", "").replace(" ", "")
    try:
        return float(s)
    except Exception:
        return None


g30, g90 = [], []
for a in acc:
    now = f2(a.get("follower_heute"))
    for key, target in (("follower_vor_30d", g30), ("follower_vor_90d", g90)):
        past = f2(a.get(key))
        if now and past and past > 0 and "UNKNOWN" not in str(a.get(key, "")).split("(")[0]:
            target.append({"handle": a["handle"], "plattform": a["plattform"], "nische_cluster": a["nische_cluster"],
                           "follower_heute": int(now), "follower_vorher": int(past), "vorher_angabe": a.get(key),
                           "wachstum_pct": round((now / past - 1) * 100, 1), "quelle": a.get("follower_historie_quelle", ""),
                           "datenqualitaet": a.get("follower_historie_dq", ""), "ai_status": a.get("ai_status", "")})
# Kurzfrist-Sprünge mit datiertem Frühsnapshot (<30 Tage) – separat ausgewiesen, NICHT als 30-Tage-Wert
short = [
    ("grandmaroseremedies", "Instagram", "KI-Senioren-Charaktere (Rezepte/Hausmittel)", 154788, 82000, "2026-09-11 → 2026-09-26 (15 T)", "AvatarFactory-Tagesreihe + Instastatistics", "THIRD-PARTY OBSERVED", "LIKELY"),
    ("grannyruthsredflags", "Instagram", "KI-Senioren-Charaktere (Rezepte/Hausmittel)", 134184, 50000, "2026-09-10 → 2026-09-26 (16 T)", "AvatarFactory + Instastatistics", "THIRD-PARTY OBSERVED", "LIKELY"),
    ("cookwithgrace2026", "Instagram", "KI-Senioren-Charaktere (Rezepte/Hausmittel)", 127822, 90147, "2026-09-10 → 2026-09-26 (16 T)", "AvatarFactory + Instastatistics", "THIRD-PARTY OBSERVED", "LIKELY"),
    ("chefdos_ia", "Instagram", "KI-Senioren-Charaktere (Rezepte/Hausmittel)", 204914, 173000, "2026-09-17 → 2026-09-26 (9 T)", "AvatarFactory + Instastatistics", "THIRD-PARTY OBSERVED", "LIKELY"),
    ("hua_jin123", "Instagram", "KI-Senioren-Charaktere (Rezepte/Hausmittel)", 1027991, 932021, "2026-08-12 → 2026-09-26 (45 T)", "AvatarFactory", "THIRD-PARTY OBSERVED", "VERIFIED"),
    ("chloe.vs.history", "Instagram", "KI-Geschichte/POV/Zeitreise", 715000, 547000, "2026-04-01 → 2026-09-18 (170 T)", "avatarfactory.io-Scans / Snippets", "THIRD-PARTY OBSERVED", "VERIFIED"),
]
for h, p, c, now, past, per, src, dq, ai in short:
    g30.append({"handle": h, "plattform": p, "nische_cluster": c, "follower_heute": now, "follower_vorher": past, "vorher_angabe": per,
                "wachstum_pct": round((now / past - 1) * 100, 1), "quelle": src, "datenqualitaet": dq + " (Zeitraum abweichend, siehe vorher_angabe)", "ai_status": ai})
gcols = ["handle", "plattform", "nische_cluster", "follower_heute", "follower_vorher", "vorher_angabe", "wachstum_pct", "quelle", "datenqualitaet", "ai_status"]
g30.sort(key=lambda x: -x["wachstum_pct"])
g90.sort(key=lambda x: -x["wachstum_pct"])
wr("03_30_day_growth.csv", g30, gcols)
wr("04_90_day_growth.csv", g90, gcols)

# ------------------------------------------------------------------ 3) Top-Reels / Top-Shorts
ts = rd("raw_youtube_proxy_top_shorts.csv")
tops = []
for r in ts:
    tops.append({"plattform": "YouTube Shorts (Proxy)", "url": r["video_url"], "titel": r["titel"], "account": r["kanal"],
                 "nische_cluster": r["nische_cluster"], "datum": r["upload_datum"], "views": r["views"],
                 "account_follower": r["kanal_abos"], "ai_status": r["ai_status"], "datenqualitaet": r["datenqualitaet"]})
for a in acc:
    if a["plattform"].lower().startswith("instagram") and a.get("top5_reels"):
        for part in str(a["top5_reels"]).split(";"):
            bits = [b.strip() for b in part.split("|")]
            if len(bits) >= 2 and bits[0].startswith("http") and bits[1] not in ("", "UNKNOWN"):
                tops.append({"plattform": "Instagram", "url": bits[0], "titel": "", "account": a["handle"], "nische_cluster": a["nische_cluster"],
                             "datum": bits[2] if len(bits) > 2 else "UNKNOWN", "views": bits[1], "account_follower": a.get("follower_heute", ""),
                             "ai_status": a.get("ai_status", ""), "datenqualitaet": a.get("top_reels_dq", "")})


def vnum(v):
    s = str(v).lower().replace(",", ".").replace(" ", "")
    mult = 1
    for suf, m in (("mio", 1e6), ("m", 1e6), ("k", 1e3)):
        if s.endswith(suf):
            s, mult = s[: -len(suf)], m
            break
    try:
        return float(s) * mult
    except Exception:
        return 0


tops.sort(key=lambda x: -vnum(x["views"]))
wr("07_top_reels.csv", tops, ["plattform", "url", "titel", "account", "nische_cluster", "datum", "views", "account_follower", "ai_status", "datenqualitaet"])

# ------------------------------------------------------------------ 4) Cluster-Metriken (YouTube-Proxy, M5 Tab. 3/4 + eigene Berechnung)
# hits30, hits120, kanaele_mit_hit_120T, uploads_120T, konzentration_top_kanal, rel_beschleunigung, gewinner(≤6M), gewinner(≤120T), ergänzung_hits120/30 (ohne AI-Flag)
M5 = {
    "KI-Story-Serien (animiert/Roblox/Moral)": (112, 352, 34, 2489, .15, 2.03, 32, 19, 0, 0),
    "KI-Fußball-/Promi-Sketche": (70, 342, 30, 2376, .22, 1.12, 27, 18, 0, 0),
    "Film/Anime/Promi-Edits & Commentary": (35, 129, 13, 1171, .28, 1.62, 11, 6, 20, 3),
    "KI-Surreal/VFX/What-if": (31, 77, 3, 295, .60, 2.93, 3, 1, 27, 2),
    "Kids/Cartoon-/Game-Figuren": (21, 285, 16, 2376, .18, 0.35, 17, 5, 219, 57),
    "KI-3D-Explainer/Kuriositäten": (16, 109, 11, 1572, .27, 0.75, 11, 4, 0, 0),
    "KI-Horror/Mystery/True Crime": (13, 38, 4, 447, .71, 2.26, 4, 2, 0, 0),
    "KI-Tiere & Haustiere (Humor/Fakten)": (11, 80, 17, 1098, .14, 0.70, 15, 7, 59, 29),
    "KI-Tierrettung & Wholesome-Tierstorys": (3, 29, 5, 430, .34, 0.51, 4, 2, 63, 5),
    "KI-DIY/Bau/Cabin/Handwerk": (6, 71, 4, 207, .44, 0.41, 4, 0, 47, 11),
    "KI-Restoration/Satisfying/ASMR": (4, 30, 4, 361, .73, 0.67, 2, 1, 35, 4),
    "KI-Kochen/Village-Food": (3, 42, 2, 113, .62, 0.33, 2, 2, 0, 0),
    "KI-Geschichte/POV/Zeitreise": (3, 17, 5, 521, .35, 0.93, 4, 1, 22, 3),
    "KI-Babys/Kinder/Familien-Comedy": (1, 47, 4, 207, .62, 0.10, 4, 3, 15, 0),
    "KI-Reise-Traumorte": (0, 22, 4, 303, .50, 0.0, 3, 1, 27, 9),
    "KI-Autos/Luxus": (9, 53, 6, 707, .51, 0.88, 6, 3, 0, 0),
    "KI-Interior/Architektur/Smart Home": (2, 9, 2, 210, .67, 1.25, 2, 1, 0, 0),
    "KI-Produkte/Gadgets": (8, 22, 3, 452, .64, 2.48, 2, 2, 0, 0),
    "Nostalgie/Then&Now/Promi-Revival": (3, 25, 5, 536, .32, 0.59, 4, 2, 0, 0),
    "KI-Garten/Pflanzen/Obst": (0, 14, 2, 137, .93, 0.0, 1, 0, 0, 0),
}
# Median Abos/Tag seit Start und Median-Views/Abo je Cluster (junge Kanäle, Start ≥ 2026-03-01, ohne "BESTRITTEN")
vel, vpf = defaultdict(list), defaultdict(list)
for r in yt:
    if "BESTRITTEN" in r["ai_status"]:
        continue
    try:
        s = dt.date.fromisoformat(r["start_erstes_video"][:10])
        subs, med = float(r["abonnenten"]), float(r["median_views"] or 0)
    except Exception:
        continue
    if s < dt.date(2026, 3, 1) or subs <= 0:
        continue
    d = (TODAY - s).days
    vel[r["nische_cluster"]].append(subs / d)
    vpf[r["nische_cluster"]].append(med / subs)

CL = {}  # cluster-key -> Anzeige, Metriken
DISPLAY = {
    "KI-Story-Serien (animiert/Roblox/Moral)": "AI Story-Serien (Roblox/3D, Rettung/Moral)",
    "KI-Fußball-/Promi-Sketche": "AI Fußball-/Promi-Sketche",
    "Film/Anime/Promi-Edits & Commentary": "AI Film-/Marvel-What-if (3D)",
    "KI-Surreal/VFX/What-if": "AI Surreal/VFX-Comedy",
    "Kids/Cartoon-/Game-Figuren": "AI Kids-/Game-Figuren",
    "KI-3D-Explainer/Kuriositäten": "AI 3D-Explainer/Kuriositäten",
    "KI-Horror/Mystery/True Crime": "AI Horror/Mystery",
    "KI-Tiere & Haustiere (Humor/Fakten)": "AI Tiere & Haustiere",
    "KI-Tierrettung & Wholesome-Tierstorys": "AI Tierrettung/Wholesome",
    "KI-DIY/Bau/Cabin/Handwerk": "AI Hausbau/Cabin/DIY-Timelapse",
    "KI-Restoration/Satisfying/ASMR": "AI Restoration/Satisfying",
    "KI-Kochen/Village-Food": "AI Village-/Cozy-Cooking",
    "KI-Geschichte/POV/Zeitreise": "AI Geschichte/Zeitreise-POV",
    "KI-Babys/Kinder/Familien-Comedy": "AI Babys/Familien-Comedy",
    "KI-Reise-Traumorte": "AI Traumorte/„Places that don't feel real“",
    "KI-Autos/Luxus": "AI Autos/Luxus",
    "KI-Interior/Architektur/Smart Home": "AI Interior/Architektur",
    "KI-Produkte/Gadgets": "AI Produkt-/Gadget-Konzepte",
    "Nostalgie/Then&Now/Promi-Revival": "AI Nostalgie/Then & Now",
    "KI-Garten/Pflanzen/Obst": "AI Garten/Obst",
}
for k, v in M5.items():
    h30, h120, chan, up, conc, acc_i, w6, w120, sup120, sup30 = v
    CL[k] = dict(name=DISPLAY[k], src="YouTube-Proxy (VERIFIED Views/Daten; AI-Flag LIKELY)", hits30=h30, hits120=h120, chan=chan,
                 hitrate=h120 / up, conc=conc, accel=acc_i, maturity=(w120 / w6) if w6 else 0,
                 vel=st.median(vel[k]) if vel[k] else 0, vpf=st.median(vpf[k]) if vpf[k] else 0, sup120=sup120, sup30=sup30)


def pct_rank(vals, x):
    s = sorted(vals)
    below = sum(1 for v in s if v < x)
    eq = sum(1 for v in s if v == x)
    return 100 * (below + 0.5 * eq) / len(s)


keys = list(CL)
metrics = {"vel": 0.25, "vpf": 0.20, "hitrate": 0.15, "chan": 0.15, "maturity": 0.10, "consist": 0.10, "accel": 0.05}
for k in keys:
    CL[k]["consist"] = 1 - CL[k]["conc"]
for m in metrics:
    vals = [CL[k][m] for k in keys]
    for k in keys:
        CL[k][m + "_s"] = pct_rank(vals, CL[k][m])
# Kleine Stichproben schrumpfen: Medianwerte/Raten aus 1–3 Kanälen sind Zufallstreffer-anfällig.
# Gewicht n/(n+5), n = junge KI-Kanäle im Cluster (Geschwindigkeit, Views/Abo) bzw. Kanäle mit Millionen-Short (Hit-Rate). MODEL ASSUMPTION
for k in keys:
    n_ch = len(vel[k])
    for m, n in (("vel", n_ch), ("vpf", n_ch), ("hitrate", CL[k]["chan"]), ("accel", CL[k]["chan"])):
        w = n / (n + 5)
        CL[k][m + "_s"] = 50 + (CL[k][m + "_s"] - 50) * w

# Instagram-basierte Cluster ohne YouTube-Äquivalent: Teil-Scores ESTIMATED aus datierten IG-Reihen (M1, M4)
IG_CL = {
    "IG:SENIOR": dict(name="AI Senioren-Charaktere (Oma-Rezepte/Hausmittel/Ratgeber)", src="Instagram (AvatarFactory-/Instastatistics-Reihen, THIRD-PARTY OBSERVED; Teil-Scores ESTIMATED)",
                      vel_s=95, vpf_s=90, hitrate_s=70, chan_s=60, maturity_s=85, consist_s=45, accel_s=100,
                      hits30="≥6 Reels ≥1 Mio (14,3M, 6,0M, 5,2M, 1,35M, 1,15M …)", hits120="13 bekannte", chan="5–6", hitrate="UNKNOWN",
                      conc="mittel (Einzel-Reel-Breakouts)", accel="stark (Sprünge 10.–26.09.)", maturity="jung (Breakouts Sep. 2026)", vel="+18 % bis +168 % in 9–16 Tagen", vpf="bis ~90× Follower (14,3M-Reel bei ~155k)", sup120="", sup30=""),
    "IG:PERSONA": dict(name="AI Personas/Virtual Influencer (Fashion/Lifestyle)", src="Instagram (Presse/Rankings, THIRD-PARTY OBSERVED; Teil-Scores ESTIMATED)",
                       vel_s=25, vpf_s=35, hitrate_s=30, chan_s=45, maturity_s=15, consist_s=40, accel_s=10,
                       hits30="grannyspills 12M/3,8M (Aug.)", hits120="wenige belegt", chan="2–3", hitrate="UNKNOWN", conc="hoch",
                       accel="seitwärts/rückläufig (Legacy-Personas)", maturity="überwiegend >12 Monate", vel="+5,7 %/90 T (grannyspills), −1,2 % (auntieauroraa)", vpf="UNKNOWN", sup120="", sup30=""),
}
for k, v in IG_CL.items():
    CL[k] = v
for k in CL:
    CL[k]["momentum"] = sum(w * CL[k][m + "_s"] for m, w in metrics.items())

# ------------------------------------------------------------------ 5) Business-Score
# econ: beste Markt-Variante aus R2 (Strong €/1 Mio. Views); log-Skala 20 € -> 0, 300 € -> 100
r2 = rd("raw_affiliate_economics_clusters.csv")
R2MAP = {  # Momentum-Cluster -> R2-Cluster-Präfix
    "KI-Story-Serien (animiert/Roblox/Moral)": "01", "KI-Fußball-/Promi-Sketche": "02", "Film/Anime/Promi-Edits & Commentary": "03",
    "KI-Surreal/VFX/What-if": "04", "KI-Tiere & Haustiere (Humor/Fakten)": "05", "KI-Tierrettung & Wholesome-Tierstorys": "05",
    "KI-DIY/Bau/Cabin/Handwerk": "06", "KI-Restoration/Satisfying/ASMR": "07", "KI-Geschichte/POV/Zeitreise": "08",
    "KI-Babys/Kinder/Familien-Comedy": "09", "KI-Kochen/Village-Food": "10", "KI-Reise-Traumorte": "11", "KI-Horror/Mystery/True Crime": "12",
    "KI-Autos/Luxus": "13", "KI-Interior/Architektur/Smart Home": "14", "IG:PERSONA": "15", "Nostalgie/Then&Now/Promi-Revival": "16",
    "KI-Garten/Pflanzen/Obst": "17", "KI-Produkte/Gadgets": "18", "Kids/Cartoon-/Game-Figuren": "19", "IG:SENIOR": "10",
    "KI-3D-Explainer/Kuriositäten": None,
}
econ_rows = {}
for r in r2:
    pre = r["nische_cluster"][:2]
    econ_rows.setdefault(pre, []).append(r)


def fnum(s):
    try:
        return float(str(s).replace(",", "."))
    except Exception:
        return None


# Rubriken (1–5) mit Begründung: intent (aus R2 bzw. begründet), ai, passiv, comp, compliance, variety
RUB = {
    "KI-Story-Serien (animiert/Roblox/Moral)": (1, 5, 3, 2, 2, 1, "Kein Produkt; oft minderjähriges Publikum; Roblox-Affiliate eingestellt (R2)"),
    "KI-Fußball-/Promi-Sketche": (2, 4, 2, 1, 1, 3, "Reale Spieler (Persönlichkeitsrecht/Deepfake), Vereins-IP; Trikots 5–10 % (R2)"),
    "Film/Anime/Promi-Edits & Commentary": (2, 4, 3, 2, 1, 2, "Disney/Marvel-IP; Collectibles bis 10 % (SELF-REPORTED)"),
    "KI-Surreal/VFX/What-if": (1, 5, 3, 3, 3, 1, "Kein Produktbezug (R2: Blocker)"),
    "Kids/Cartoon-/Game-Figuren": (2, 4, 2, 1, 1, 2, "Kinderpublikum + Franchise-IP; Gift-Cards 0 %"),
    "KI-3D-Explainer/Kuriositäten": (2, 4, 4, 2, 4, 2, "Wissen/Kuriosität, Produkte nur beiläufig; R2 ohne Rechnung → Economics ESTIMATED 40 €"),
    "KI-Horror/Mystery/True Crime": (2, 5, 4, 3, 3, 2, "Bücher/Games (Thalia 11 %, Humble 4–10 %), schwacher Kaufanlass"),
    "KI-Tiere & Haustiere (Humor/Fakten)": (2, 3, 4, 1, 3, 3, "Pet-Produkte möglich, aber Content = Unterhaltung; KI-Tiere als Produktdemo irreführend"),
    "KI-Tierrettung & Wholesome-Tierstorys": (2, 3, 4, 2, 2, 2, "Fake-Rettungen = Täuschungsrisiko; Spenden ohne Provision"),
    "KI-DIY/Bau/Cabin/Handwerk": (3, 4, 4, 3, 3, 4, "Werkzeug, Gartenhaus-/Cabin-Kits (GartenHaus 7 %, hagebau 10 %, Jamaica Cottage 5 %); IG in DE leer (DE-Recherche)"),
    "KI-Restoration/Satisfying/ASMR": (3, 3, 4, 3, 3, 4, "Reinigungs-/Pflegeprodukte (Kärcher AT 5 %, Chemical Guys); KI-Vorher/Nachher heikel"),
    "KI-Kochen/Village-Food": (3, 4, 4, 3, 4, 4, "Kochgeschirr, Gusseisen, Messer (Zwilling 6–8 %, Petromax, Amazon Küche 4,5/5 %)"),
    "KI-Geschichte/POV/Zeitreise": (2, 5, 5, 3, 3, 2, "Bücher (Thalia 11 %), Stadtführungen (GetYourGuide 8 %); DE-Städte-Arbitrage (DE-Recherche)"),
    "KI-Babys/Kinder/Familien-Comedy": (2, 4, 3, 2, 1, 3, "Baby-Produkte = Compliance HIGH (Vorstudie)"),
    "KI-Reise-Traumorte": (2, 5, 4, 2, 2, 2, "KI-Orte ≠ reale Orte → Irreführung bei Buchungen; Provision erst nach Reise"),
    "KI-Autos/Luxus": (2, 4, 3, 2, 2, 3, "Marken-/Logo-Risiko; Car-Care/Modellautos (CK-Modelcars 7 %)"),
    "KI-Interior/Architektur/Smart Home": (2, 5, 4, 2, 3, 5, "KI-Möbel nicht kaufbar (Vorstudie: AI-Interior-Paradox)"),
    "KI-Produkte/Gadgets": (3, 2, 2, 2, 2, 3, "Konzept-Produkte existieren nicht; echte Gadgets per KI-Demo irreführend"),
    "Nostalgie/Then&Now/Promi-Revival": (2, 4, 5, 3, 3, 3, "Retro-Konsolen 1 % (Amazon), Vinyl (HHV bis 8 %), Bücher"),
    "KI-Garten/Pflanzen/Obst": (2, 4, 2, 3, 3, 4, "Garten-Programme gut, aber Saison + KI-Pflanzen ≠ reale Sorten"),
    "IG:SENIOR": (3, 4, 4, 3, 2, 4, "Rezepte → Kochgeschirr/Zutaten; 'Comment RECIPE' belegt hohe Kommentarquote; Hausmittel = Health-Claims (HIGH) → nur Rezept-Variante; KI-Person braucht 'AI-generated profile'-Label, keine Erfahrungs-Testimonials"),
    "IG:PERSONA": (3, 3, 1, 2, 2, 5, "Kleidung mit hohen Retouren; KI-Model zeigt nie exakt das Teil; Label-Pflicht KI-Person"),
}
BW = {"econ": 0.25, "intent": 0.20, "ai": 0.15, "passiv": 0.10, "comp": 0.10, "compliance": 0.10, "variety": 0.10}
for k in CL:
    pre = R2MAP.get(k)
    rows = econ_rows.get(pre, []) if pre else []
    best = None
    for r in rows:
        s = fnum(r["umsatz_pro_1m_views_strong_eur"])
        b = fnum(r["umsatz_pro_1m_views_base_eur"])
        if s is not None and (best is None or s > best[0]):
            best = (s, b, r["markt"], r["affiliate_fit"], r["views_fuer_10k_strong"], r["aov_eur"], r["provision_pct"])
    if best is None:
        best = (40.0, 7.0, "EN/US (ESTIMATED)", "LOW", "UNKNOWN", "UNKNOWN", "UNKNOWN")
    intent, ai, passiv, comp, compl, var, why = RUB[k]
    econ = max(0, min(100, 100 * (math.log(best[0]) - math.log(20)) / (math.log(300) - math.log(20))))
    sub = {"econ": econ, "intent": (intent - 1) / 4 * 100, "ai": (ai - 1) / 4 * 100, "passiv": (passiv - 1) / 4 * 100,
           "comp": (comp - 1) / 4 * 100, "compliance": (compl - 1) / 4 * 100, "variety": (var - 1) / 4 * 100}
    CL[k].update(dict(business=sum(BW[m] * sub[m] for m in BW), econ_strong=best[0], econ_base=best[1], econ_market=best[2], fit=best[3],
                      views10k=best[4], aov=best[5], prov=best[6], intent=intent, ai=ai, passiv=passiv, comp=comp, compliance=compl,
                      variety=var, why=why, econ_s=econ))
    CL[k]["combined"] = 0.5 * CL[k]["momentum"] + 0.5 * CL[k]["business"]

ranked_m = sorted(CL, key=lambda k: -CL[k]["momentum"])
ranked_c = sorted(CL, key=lambda k: -CL[k]["combined"])


def r1(x):
    return round(x, 1) if isinstance(x, (int, float)) else x


mcols = ["rang_momentum", "cluster", "datenbasis", "momentum_score", "growth_velocity_25", "views_pro_follower_20", "million_hit_rate_15",
         "unabhaengige_gewinner_15", "geringe_reife_10", "konsistenz_10", "beschleunigung_5", "abos_pro_tag_median", "median_views_pro_abo",
         "millionen_shorts_30T", "millionen_shorts_120T", "kanaele_mit_millionen_short_120T", "hit_rate_120T", "konzentration_top_kanal",
         "rel_beschleunigung", "ergaenzung_ohne_ai_flag_hits_120T_30T", "trendklasse"]


def trend(k):
    c = CL[k]["chan"]
    if isinstance(c, str):
        return "EMERGING PATTERN (IG, 5–6 Accounts)" if k == "IG:SENIOR" else "ONE-OFF/Legacy"
    return "STRONG TREND" if c >= 5 else ("EMERGING PATTERN" if c >= 3 else "ONE-OFF OUTLIER")


rows = []
for i, k in enumerate(ranked_m, 1):
    c = CL[k]
    rows.append({"rang_momentum": i, "cluster": c["name"], "datenbasis": c["src"], "momentum_score": r1(c["momentum"]),
                 "growth_velocity_25": r1(c["vel_s"]), "views_pro_follower_20": r1(c["vpf_s"]), "million_hit_rate_15": r1(c["hitrate_s"]),
                 "unabhaengige_gewinner_15": r1(c["chan_s"]), "geringe_reife_10": r1(c["maturity_s"]), "konsistenz_10": r1(c["consist_s"]),
                 "beschleunigung_5": r1(c["accel_s"]), "abos_pro_tag_median": r1(c["vel"]) if isinstance(c["vel"], float) else c["vel"],
                 "median_views_pro_abo": round(c["vpf"], 2) if isinstance(c["vpf"], float) else c["vpf"], "millionen_shorts_30T": c["hits30"],
                 "millionen_shorts_120T": c["hits120"], "kanaele_mit_millionen_short_120T": c["chan"],
                 "hit_rate_120T": f"{c['hitrate']*100:.1f} %" if isinstance(c["hitrate"], float) else c["hitrate"],
                 "konzentration_top_kanal": f"{c['conc']*100:.0f} %" if isinstance(c["conc"], float) else c["conc"],
                 "rel_beschleunigung": c["accel"], "ergaenzung_ohne_ai_flag_hits_120T_30T": f"{c['sup120']}/{c['sup30']}" if c["sup120"] != "" else "",
                 "trendklasse": trend(k)})
wr("06_momentum_scores.csv", rows, mcols)

ccols = ["rang_combined", "cluster", "combined_score", "momentum_score", "rang_momentum", "business_score", "rang_business",
         "affiliate_economics_25", "purchase_intent_1_5", "ai_fit_1_5", "passivity_1_5", "competition_opportunity_1_5", "compliance_1_5",
         "product_variety_1_5", "bester_markt", "provision_pro_1m_views_base_eur", "provision_pro_1m_views_strong_eur", "affiliate_fit",
         "views_fuer_10k_gewinn_strong", "begruendung"]
rank_b = {k: i for i, k in enumerate(sorted(CL, key=lambda k: -CL[k]["business"]), 1)}
rank_mm = {k: i for i, k in enumerate(ranked_m, 1)}
rows = []
for i, k in enumerate(ranked_c, 1):
    c = CL[k]
    rows.append({"rang_combined": i, "cluster": c["name"], "combined_score": r1(c["combined"]), "momentum_score": r1(c["momentum"]),
                 "rang_momentum": rank_mm[k], "business_score": r1(c["business"]), "rang_business": rank_b[k], "affiliate_economics_25": r1(c["econ_s"]),
                 "purchase_intent_1_5": c["intent"], "ai_fit_1_5": c["ai"], "passivity_1_5": c["passiv"], "competition_opportunity_1_5": c["comp"],
                 "compliance_1_5": c["compliance"], "product_variety_1_5": c["variety"], "bester_markt": c["econ_market"],
                 "provision_pro_1m_views_base_eur": c["econ_base"], "provision_pro_1m_views_strong_eur": c["econ_strong"], "affiliate_fit": c["fit"],
                 "views_fuer_10k_gewinn_strong": c["views10k"], "begruendung": c["why"]})
wr("14_combined_scores.csv", rows, ccols)

# 11 Affiliate-Economics (aus R2 übernommen, um Momentum-Kontext ergänzt)
arows = []
for r in r2:
    arows.append(dict(r))
wr("11_affiliate_economics.csv", arows, list(r2[0].keys()))

json.dump({k: {kk: (vv if not isinstance(vv, float) else round(vv, 3)) for kk, vv in v.items()} for k, v in CL.items()},
          open(os.path.join(ROOT, "scripts", "score_output.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    print(f"Accounts gesamt: {len(acc)} (IG/TikTok/YT aus M1–M4/DE: {len(acc)-len(yt)}, YT-Proxy: {len(yt)}); VERIFIED: {len(ver)}")
    print(f"30-T-Wachstum datiert: {len(g30)} · 90-T: {len(g90)} · Top-Reels: {len(tops)}")
    print(f"{'Rg':>2} {'Cluster':52} {'Mom':>5} {'Bus':>5} {'Comb':>5} {'€/1M S':>7} {'Fit':6}")
    for i, k in enumerate(ranked_c, 1):
        c = CL[k]
        print(f"{i:>2} {c['name'][:52]:52} {c['momentum']:5.1f} {c['business']:5.1f} {c['combined']:5.1f} {c['econ_strong']:7.0f} {c['fit']:6} (M#{rank_mm[k]}, B#{rank_b[k]})")
