# 05 – Nischen-Cluster, Trendklassen und Treiber (Teile 8, 9, 12)

**Stand:** 26.09.2026 · **Daten:** [`01_200_accounts.csv`](01_200_accounts.csv), [`06_momentum_scores.csv`](06_momentum_scores.csv), Rohberichte M1–M5 und DE in [`quellen/`](quellen/)

## 1. Zwei Datenbasen und warum es zwei sind

| Basis | Was sie liefert | Was sie nicht liefert | Datenqualität |
|---|---|---|---|
| **Instagram direkt** (M1–M4, DE): 229 IG-Accounts, davon 188 VERIFIED und 27 LIKELY KI | aktuelle Follower, Posts, Bio/Links, KI-Belege; für **13 Accounts datierte Follower-Reihen** (AvatarFactory, Instastatistics) und für 11 Accounts Reel-Views | Follower-Historie für alle übrigen Accounts, Reel-Views der meisten Accounts | Follower THIRD-PARTY OBSERVED, Historie wo vorhanden THIRD-PARTY OBSERVED, sonst **UNKNOWN** |
| **YouTube-Shorts-Proxy** (M5): 338 junge KI-Kanäle, 32.439 Shorts, davon 3.303 mit ≥ 1 Mio. Views | exakte Upload-Daten und Views → echte 30/60/90/120-Tage-Werte je Cluster | Instagram-Verhalten; Abo-Verläufe (Social Blade gesperrt) | Views/Daten VERIFIED, KI-Flag LIKELY (NexLev) |

Instagram gibt keine Historie öffentlich heraus; Social Blade, HypeAuditor und web.archive.org waren gesperrt (403) und wurden nicht umgangen. Deshalb misst diese Studie Momentum **auf YouTube Shorts als Proxy** (viele KI-Marken posten dieselben Clips auf IG, YT und TikTok) und ergänzt es um die wenigen **datierten Instagram-Reihen**. Die Übertragbarkeit von YT auf Reels ist plausibel, aber nicht belegt.

**Trendklassen (Teil 9):** Gezählt werden unabhängige, junge KI-Kanäle (Start ab 01.03.2026) mit mindestens einem Millionen-Short in 120 Tagen.
- **ONE-OFF OUTLIER:** 1–2 Kanäle
- **EMERGING PATTERN:** 3–4 Kanäle
- **STRONG TREND:** ≥ 5 Kanäle

## 2. Cluster-Tabelle

Sortiert nach Momentum-Score. Spalten:
- **Mio.-Shorts 30 T / 120 T:** Anzahl KI-Shorts ≥ 1 Mio. Views (VERIFIED, YouTube).
- **Kanäle mit Hit:** unabhängige junge Kanäle mit ≥ 1 Mio.-Short in 120 T.
- **Median-Wachstum:** Median Abos pro Tag seit Start der jungen Kanäle (VERIFIED Abos ÷ Tage; Abo-Verläufe fehlen).
- **Views/Abo:** Median der Kanal-Median-Views ÷ Abos (Proxy für „Content stärker als Audience“).
- **Wiederholbarkeit:** Hit-Rate 120 T (Anteil Uploads ≥ 1 Mio.) und Konzentration (Anteil des stärksten Kanals an den Hits).
- **Beschleunigung:** Hits der letzten 30 T ÷ Monatsschnitt der Tage 31–120, relativ zum Markt (0,69). > 1,2 = beschleunigt, < 0,8 = verlangsamt.

| # | Cluster | Trendklasse | Mio.-Shorts 30 T / 120 T | Kanäle mit Hit | Median-Wachstum (Abos/Tag) | Views/Abo | Hit-Rate / Konzentration | Beschleunigung |
|---|---|---|---|---|---|---|---|---|
| 1 | **KI-Senioren-Charaktere (Oma-Rezepte/Hausmittel)** – Instagram | **EMERGING PATTERN** (5–6 Accounts mit datiertem Sprung) | ≥ 6 Reels ≥ 1 Mio. bekannt, alle Juli–Sep. (THIRD-PARTY OBSERVED) | 5–6 | **+18 % bis +168 % Follower in 9–16 Tagen** (THIRD-PARTY OBSERVED) | Top-Reel bis 92× Follower | UNKNOWN / mittel (Einzel-Reel-Breakouts) | **stark** (Sprünge 10.–26.09.) |
| 2 | Story-Serien (Roblox/3D, Rettung/Moral) | **STRONG TREND** | 112 / 352 | 34 | 702 | 1,71 | 14,1 % / 15 % | **2,03 beschleunigt** |
| 3 | Fußball-/Promi-Sketche | **STRONG TREND** | 70 / 342 | 30 | 1.086 | 0,64 | 14,4 % / 22 % | 1,12 marktkonform |
| 4 | Kids-/Game-Figuren | **STRONG TREND** | 21 / 285 | 16 | 2.136 | 0,76 | 12,0 % / 18 % | 0,35 verlangsamt |
| 5 | Film-/Marvel-What-if (3D) | **STRONG TREND** | 35 / 129 | 13 | 556 | 1,18 | 11,0 % / 28 % | **1,62 beschleunigt** |
| 6 | Babys/Familien-Comedy | EMERGING PATTERN | 1 / 47 | 4 | 1.029 | 0,90 | 22,7 % / 62 % | 0,10 verlangsamt |
| 7 | Village-/Cozy-Cooking | **ONE-OFF** (2 Kanäle) | 3 / 42 | 2 | 3.412 | 2,66 | 37,2 % / 62 % | 0,33 verlangsamt |
| 8 | Horror/Mystery | EMERGING PATTERN | 13 / 38 | 4 | 870 | 1,50 | 8,5 % / 71 % | 2,26 beschleunigt (Einzelkanal) |
| 9 | Tiere & Haustiere | **STRONG TREND** | 11 / 80 | 17 | 529 | 0,59 | 7,3 % / 14 % | 0,70 verlangsamt |
| 10 | Nostalgie/Then & Now | STRONG TREND | 3 / 25 | 5 | 352 | 1,48 | 4,7 % / 32 % | 0,59 verlangsamt |
| 11 | Surreal/VFX-Comedy | EMERGING PATTERN | 31 / 77 | 3 | 847 | 1,29 | 26,1 % / 60 % | 2,93 beschleunigt (Einzelkanal) |
| 12 | Hausbau/Cabin/DIY-Timelapse | EMERGING PATTERN | 6 / 71 | 4 | 2.148 | 0,46 | 34,3 % / 44 % | 0,41 verlangsamt |
| 13 | Traumorte („Places that don't feel real“) | EMERGING PATTERN | 0 / 22 | 4 | 897 | 1,27 | 7,3 % / 50 % | 0,00 verlangsamt |
| 14 | 3D-Explainer/Kuriositäten | STRONG TREND | 16 / 109 | 11 | 407 | 0,93 | 6,9 % / 27 % | 0,75 verlangsamt |
| 15 | Autos/Luxus | STRONG TREND | 9 / 53 | 6 | 546 | 0,62 | 7,5 % / 51 % | 0,88 marktkonform |
| 16 | Produkt-/Gadget-Konzepte | EMERGING PATTERN | 8 / 22 | 3 | 1.615 | 0,27 | 4,9 % / 64 % | 2,48 beschleunigt (Einzelkanal) |
| 17 | Tierrettung/Wholesome | STRONG TREND | 3 / 29 | 5 | 673 | 0,56 | 6,7 % / 34 % | 0,51 verlangsamt |
| 18 | Geschichte/Zeitreise-POV | STRONG TREND | 3 / 17 | 5 | 459 | 1,48 | 3,3 % / 35 % | 0,93 marktkonform |
| 19 | Restoration/Satisfying | EMERGING PATTERN | 4 / 30 | 4 | 723 | 0,58 | 8,3 % / 73 % | 0,67 verlangsamt |
| 20 | Interior/Architektur | ONE-OFF | 2 / 9 | 2 | 232 | (8,3; n = 2) | 4,3 % / 67 % | 1,25 (zu dünn) |
| 21 | Garten/Obst | ONE-OFF | 0 / 14 | 2 | 398 | 0,67 | 10,2 % / 93 % | 0,00 verlangsamt |
| 22 | Personas/Virtual Influencer (Fashion/Lifestyle) – Instagram | ONE-OFF / Legacy | grannyspills: 12M- und 3,8M-Reel im August | 2–3 | +5,7 %/90 T (grannyspills), −1,2 %/90 T (auntieauroraa) (THIRD-PARTY OBSERVED) | UNKNOWN | UNKNOWN | seitwärts/rückläufig |

Nicht als eigene Cluster gewertet (M5), weil kaum originär KI-generiert: Meme-/Ranking-Kompilationen (80/393), Religions-Edits (36/232), Motivation, Sport-Trickshots, Kindness-Clips.

## 3. Was die Tabelle zeigt

1. **Die breitesten, schnellsten Trends sind Unterhaltung für ein junges, globales Publikum:**
   - Story-Serien: 34 unabhängige Kanäle, 112 Millionen-Shorts in 30 Tagen, als einziger großer Cluster mit steigender Hit-Rate
   - Fußball-Sketche
   - Kids-/Game-Figuren
   - Marvel-What-if
2. **Die „KI-Ästhetik“-Nischen mit Produktnähe hatten ihren Peak im Juni/Juli und sind jetzt verlangsamt** (Diagramm [`02_momentum_30T_vs_vorher.png`](diagramme/02_momentum_30T_vs_vorher.png)):
   - DIY/Cabin: 6 vs. 22 Millionen-Shorts je 30 Tage
   - Village-Cooking: 3 vs. 13
   - Restoration: 4 vs. 9
   - Babys: 1 vs. 15
   - Traumorte: 0 vs. 7
   - Garten: 0 vs. 5
3. **Auf Instagram gibt es eine frische, datierte Bewegung** bei KI-Senioren-Charakteren. 5–6 junge Accounts sind zwischen dem 10. und 26.09.2026 gesprungen:
   - grandmaroseremedies 82.000 → 154.788 (+89 % in 15 T)
   - grannyruthsredflags 50.000 → 134.184 (+168 % in 16 T)
   - cookwithgrace2026 +42 % in 16 T
   - chefdos_ia +18 % in 9 T
   - hua_jin123 +10 % in 45 T

   Das ist ein **EMERGING PATTERN**, noch kein STRONG TREND: 5–6 Accounts, KI-Status überwiegend LIKELY, Beobachtungsfenster nur 9–45 Tage.
4. **Tiere, Tierrettung, ASMR, Miniaturen:** auf YouTube breit, aber verlangsamt; auf Instagram kein junger Breakout, dafür viele tote Copycats (M1).

## 4. Warum funktioniert die Nische? (Teil 12)

Die Treiber sind aus den Winner-vs-Loser-Codierungen abgeleitet ([`09_winner_vs_loser.md`](09_winner_vs_loser.md)). Hauptreiber stehen fett. „Kaufwunsch“ ist nur markiert, wo er im Content sichtbar ist.

| Cluster | Emotion | Niedlich | Überraschung | Nostalgie | Story | Schönheit | Status | Fantasie | Wissen | Transformation | Kontroverse | Identifikation | Kaufwunsch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Senioren-Charaktere | ● | | **●** (Alters-Schock) | ● | | | | | **●** (Rezept/Tipp) | | ● („Pharmacies don't want…“) | **●** (Oma-Figur) | ◐ (Kochgeschirr, E-Books) |
| Story-Serien | **●** (Moral) | | **●** (Schock, Twist) | | **●** | | | ● | | | | ● (Kind/Familie) | – |
| Fußball-Sketche | | | ● | ● (Prime-Legenden) | | | **●** | | | | | **●** (Fans) | – |
| Kids/Game | | ● | | | ● | | ● (Power-Scaling) | **●** | | | | ● | – |
| Film-What-if | | | ● | | | | | **●** | **●** | | | ● (Fandom) | – |
| Babys | | ● | **●** (Schock-Kontrast) | | | | | | | | | **●** (Eltern) | – |
| Village-/Cozy-Cooking | **●** (Wärme) | | | **●** | ● | **●** | | | | | | ● | ◐ (Gusseisen sichtbar) |
| Horror | ● (Opfer) | | **●** | | ● | | | **●** (Regelwelt) | | | | | – |
| Tiere | ● (Mitleid) | **●** | ● | ● (Meme-Katzen) | | | | | | | | | – |
| Nostalgie | | | | **●** | | | | | ● | | | **●** | ◐ |
| Surreal | | | **●** | | | | | **●** | | | | | – |
| Hausbau/Cabin/DIY | | | ● | | | ● | **●** (Luxus-Endzustand) | ● | | **●** | | | ◐ (Werkzeug sichtbar) |
| Traumorte | | | | | | **●** | ● | | ● | | | | ◐ (Reise) |
| Autos | | | | | | | **●** | | | | | | ◐ |
| Gadgets | | | ● | | | | | | ● | | | | **●** (Mr.Dumblings) |
| Tierrettung | **●** | **●** | **●** (Rollentausch) | | ● | | | | | | | | – |
| Geschichte/Zeitreise | | | **●** | | ● | | | | **●** | ● | **●** (Dark History) | | – |
| Restoration | | | | ● (Oldtimer) | | **●** | | | | **●** | | | ◐ (Pflegemittel) |
| Interior | | | | | | **●** | ● | | | | | | ◐ |
| Personas | | | | | | ● | ● | | | | | ● | ◐ (Outfits, oft nicht real) |

● = Treiber · **●** = Haupttreiber · ◐ = Produkt sichtbar, aber nicht Mittelpunkt

**Lesart für die Monetarisierung:** Keiner der schnell wachsenden Cluster lebt von Kaufwunsch. Wo Produkte sichtbar sind (Kochgeschirr, Werkzeug, Pflegemittel), sind sie Requisite. Die Kaufnähe muss das eigene Format herstellen, ohne den Unterhaltungskern zu zerstören (siehe [`10_affiliate_fit.md`](10_affiliate_fit.md)).

## 5. Emerging Outliers (Content stärker als Audience, Teil 6)

| Account | Plattform | Follower/Abos | Signal | Qualität |
|---|---|---|---|---|
| grannyruthsredflags | IG | ~54K beim Posten | 6,04M-Reel (19.09.) → Follower mehr als verdoppelt | THIRD-PARTY OBSERVED |
| grandmaroseremedies | IG | ~82K am 11.09. | 14,26M-Reel (07.09.), danach 5,17M, 1,35M, 1,15M | THIRD-PARTY OBSERVED |
| zawpolyshorts | IG | 16.072 bei 9 Posts | Reel mit 189.747 Likes (Like/Follower bis 11,8×) | THIRD-PARTY OBSERVED |
| Pixel Siuu | YT | 44K (Start 06.08.) | 31 Millionen-Shorts in 30 T | VERIFIED |
| The Minute Before | YT | 4.690 | 15,7M-Short (POV-Zeitreise, 15.07.) | VERIFIED |
| Tyler | YT | 56K (Start 18.08.) | 23 Millionen-Shorts in 30 T | VERIFIED |
| Golazo Fx | YT | 67K (Start 28.08.) | 19 Millionen-Shorts in 29 T | VERIFIED |
| Soft sound Space | YT | 32K (Start 28.07.) | 29,3M-Short (Restoration-ASMR) | VERIFIED |
| aifruitdrama | IG | 170 | Reel mit 60.463 Views ≈ 350× Follower; danach aufgegeben | THIRD-PARTY OBSERVED |

Die Outlier-Liste bestätigt das Muster: Einzelne Reels laufen weit über der Follower-Basis, gehalten wird das Wachstum aber nur mit Serienlogik (feste Figur, feste Mechanik).
