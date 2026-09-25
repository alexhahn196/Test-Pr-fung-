# 03 – Wettbewerbsanalyse (Teil 2, Teil 3, Teil 4 und Teil 20 teilweise)

**Stand der Daten:** 25.09.2026 · **Für:** neuen internationalen (englischsprachigen) Instagram-Account mit überwiegend KI-generierten Reels (Luxury Interiors, Future Homes, Architektur)

**Grundlage dieses Kapitels**

| Datei | Inhalt |
|---|---|
| [02_competitor_database.csv](02_competitor_database.csv) | 111 Accounts mit Status je Feld; 103 mit Followerzahl `VERIFIED`, 72 tief profiliert (Bio, Links, Angebote, Deals) |
| [data/processed/shortlist_scores.csv](data/processed/shortlist_scores.csv) | Scoring von 261 Kandidaten (≥ 2 Reels im Sample, ≥ 1.000 Follower), erzeugt mit [scripts/shortlist.py](scripts/shortlist.py) |
| [04_reel_database.csv](04_reel_database.csv) | 2.498 Reels von 239 öffentlichen Topic-Seiten, 2.393 davon per Cover-Frame und Caption codiert |
| `data/raw/accounts/profile_*.json` | Tiefenprofile, z. B. [profile_aiforarchitects.json](data/raw/accounts/profile_aiforarchitects.json) |
| [data/processed/analysis_digest.md](data/processed/analysis_digest.md), `data/processed/stats/*.csv` | Segment-Tabellen, Kruskal-Wallis-Tests, Key Contrasts |
| [q05](quellen/q05_competitor_lists.md), [q06](quellen/q06_ai_theme_page_case_studies.md) | Wettbewerber-Landkarte (354 Handles, 8 Gruppen) und Fallstudien zu KI-Theme-Pages |

**Lesehilfe (Kennzahlen)**
- **vpf** (views per follower) = Views ÷ Follower beim Abruf. „20×“ heißt: 20-mal so viele Views wie Follower.
- **adj_factor** = Views im Verhältnis zur Erwartung für die Accountgröße auf *derselben* Topic-Seite (1,0 = erwartbar, 2,0 = doppelt so viel). Das ist die **Hauptmetrik**, weil vpf kleine Accounts systematisch bevorzugt (Abschnitt 3.3).
- **topic_index** = Views ÷ Median-Views derselben Topic-Seite.
- **Status-Tags:** Views und Follower von öffentlichen Seiten = `[VERIFIED]` (gerundet, wie angezeigt). KI-gestützte Codes (Produktion, Stil, Raum, Hook) = `[ESTIMATED]` (Reliabilität κ 0,63–1,0). Selbstauskünfte zu Umsätzen und Drittzahlen = `[THIRD-PARTY ESTIMATE]`. Nicht belegbar = `[UNKNOWN]`.
- **Selektionsbias:** Topic-Seiten zeigen die *Top*-Reels eines Themas. Alle Account-Werte beschreiben daher „die Reels dieses Accounts, die es auf eine Topic-Seite geschafft haben“, nicht den Account-Durchschnitt. Absolute Views sind nach oben verzerrt; *relative* Vergleiche sind die Stärke der Daten.
- **Beobachtete Beispiele** (Hooks, Captions) stehen als kurzer Auszug mit Handle und sind mit „beobachtet“ markiert. Daraus leiten wir das **Prinzip** ab. Alle neuen Formulierungen in diesem Dokument sind eigene Wortlaute.

---

## 0. Kurzfassung

1. **Das Wettbewerbsfeld ist groß und gemischt.** Die Landkarte in [q05](quellen/q05_competitor_lists.md) umfasst 354 Handles in 8 Gruppen (A 121 · B 35 · C 39 · D 25 · E 25 · F 28 · G 30 · H 51). Die Competitor-DB enthält 111 Accounts (108 laut DB-Feld mit Reels im Sample; in `04_reel_database.csv` haben alle 111 mindestens ein Reel); 47 davon posten laut Codierung überwiegend KI-Inhalte `[ESTIMATED]`.
2. **Kleine Accounts mit Millionen-Views sind häufig, aber meist real gefilmt.** 207 Accounts mit < 100K Followern haben ein Reel mit ≥ 1 Mio. Views im Sample. Deren Top-Reel ist in 143 Fällen reales Material, in 45 Fällen KI, in 11 Fällen 3D `[VERIFIED Zählung; Produktion ESTIMATED]`.
3. **Views ÷ Follower allein führt in die Irre.** Unter den 261 Kandidaten liegen 67 % der 10–100K-Accounts bei einem Median-vpf ≥ 5, aber nur 14 % der ≥ 1M-Accounts. Die größenbereinigte Metrik (adj_factor) zeigt dagegen kaum einen Größeneffekt (10–100K 1,07 vs. 1M+ 0,91, Reel-Ebene).
4. **Die Top-20-Shortlist ist nicht followergetrieben.** Die Rangkorrelation zwischen Score und Followern liegt bei ρ = 0,03 (p = 0,62). Die Top 20 reichen von 40K bis 4M Followern.
5. **Das stärkste Muster der Top 20 ist Identität plus B2B.** Nur 2 der 20 sind laut Reel-Codierung reine Theme-Pages (laut Profil-Einstufung 4); die übrigen treten als Studio, Creator, Firma oder Person auf. 10 der 20 verkaufen nachweislich Dienstleistungen (Design, Rendering, Landscaping, Workshops) `[VERIFIED]`. Das deckt sich mit dem robusten Befund auf Reel-Ebene: Theme-Pages adj ≈ 0,74 (n = 503) vs. AI-Creator ≈ 1,09 (n = 276), Kruskal-Wallis p < 0,001.
6. **Reichweite ist extrem hit-getrieben.** Innerhalb desselben Accounts liegen zwischen bestem und schwächstem Reel im Sample bei 6 der Top 20 Faktoren von 150–900 (z. B. @siyad_abdali 282 Mio. vs. 316 Tsd.). Mehrere KI-Cozy-Accounts zeigen ein Decay-Muster; ein Alterseffekt ist nicht ausgeschlossen (Abschnitt 7, Muster 3).
7. **Was die Top-Accounts visuell verbindet** (beschreibend, nicht getestet): Nacht-, Blue-Hour- oder Golden-Hour-Licht in 57 % ihrer Reels (Gesamt-Sample 33 %), kaum Text auf dem Cover (11 % vs. 47 %), eine klare Architektur- oder Außenraum-Idee pro Reel, fast nie Menschen im Bild (5 von 72 Reels). Menschen und Choice-Mechaniken nutzen die Top-Accounts kaum; ob sie wirken, ist offen (Menschen bei KI ≈ 1,68×, nur nominal signifikant; Choice nur für Kommentare belegt) und gehört in die eigenen Tests.
8. **Monetarisierung der Top 20:** B2B-Aufträge dominieren (10 Accounts). Kurse und Prompts finden sich bei 2, KI-Tool-Partnerschaften bzw. -Referrals bei 2, Produkt-Affiliate bei 2 (Amazon, Wayfair per DM). Bei 3 Accounts ist keine Monetarisierung sichtbar, einer ist nicht tief profiliert. **Umsätze sind bei keinem Account belegt** `[UNKNOWN]`.

---

## 1. Datenbasis und Methode in Kürze

| Baustein | Umfang | Status |
|---|---|---|
| Topic-Seiten `instagram.com/popular/<slug>/` | 239 Topics, 2.498 Reels, 1.985 Handles | Views `[VERIFIED]` (gerundet) |
| Follower je Account (öffentliche Embed-Seiten) | 1.913 Accounts im Reel-Datensatz mit Followerzahl | `[VERIFIED]` (gerundet, Stand Abruf) |
| Competitor-DB | 111 Accounts, 72 tief profiliert | je Feld eigener Status |
| Cover- und Caption-Codierung | 2.393 Reels | `[ESTIMATED]` |
| Wettbewerber-Landkarte ([q05](quellen/q05_competitor_lists.md)) | 354 Handles aus hafi.pro, HypeAuditor, Embeds und Projekt-DB | Drittanbieter-Follower `[VERIFIED als Anzeige]` |

**Wichtig:** Die „letzten 20 Reels“ eines Accounts sind ohne Login nicht abrufbar. Pro Account liegen deshalb nur die Reels vor, die auf Topic-Seiten auftauchen: bei 165 der 261 Scoring-Kandidaten genau 2 Reels. Siehe Abschnitt 9 (Limitationen).

---

## 2. Teil 2 – Überblick über die Accounts nach Gruppen A–H

### 2.1 Gruppen und Zuordnungsregel

Die Gruppen folgen der Aufgabenstellung und [q05](quellen/q05_competitor_lists.md). Für dieses Kapitel wurde jeder der 111 DB-Accounts **redaktionell genau einer Gruppe** zugeordnet. Maßgeblich waren Account-Identität und inhaltlicher Fokus; die Produktionsart (KI/real) steht separat. Bei einzelnen Handles weicht die Zuordnung daher von q05 ab (z. B. @wayup_media dort F, hier B).

| Gruppe | Definition in diesem Kapitel |
|---|---|
| **A** | Interior-Theme-Pages, Interior-Creator, Design- und 3D-Studios, Interior-/Home-Trade (auch Studios mit KI-Look) |
| **B** | Luxury Real Estate, Makler, Home-Tour-Medien |
| **C** | Architektur- und Designmedien, Architekturbüros, Stadt-/Architekturfotografie |
| **D** | KI-first-Accounts mit Architektur-, Villen- oder Außenfokus (inkl. KI-Architektur-Lehre und Tool-Anbieter) |
| **E** | KI-first-Accounts mit Interior-, Cozy- oder Home-Transformation-Fokus (inkl. Garten-Makeover) |
| **F** | Gesichtslose Dream-/Future-Home-Theme-Pages (Häuser, Villen; real oder KI) |
| **G** | Luxury-Lifestyle-, Travel- und Hotel-Accounts mit Interior- oder Hotel-Anteil |
| **H** | **Querschnitt:** Accounts mit < 100K Followern und mindestens einem Reel ≥ 1 Mio. Views (zählt zusätzlich zur Hauptgruppe) |
| (Sonstige) | Nicht-Interior-Accounts, die über Interior-Topics in die DB kamen (generische KI-Videos, Naturklang, Produkt-Finds) |

### 2.2 Übersichtstabelle A–H mit Follower-Tiers

Spalten „< 100K“ bis „≥ 1M“ = Anzahl der DB-Accounts je Follower-Tier. „davon H“ = < 100K **und** ein Reel ≥ 1 Mio. Views. „Neu & schnell“ = ältestes gesehenes Reel ≤ 12 Monate alt, ≥ 100K Follower und plausible Posting-Rate (Definition in 2.4). Median-vpf = Median der Account-Mediane (nach oben verzerrt, nur zur Orientierung).

| Gruppe | q05-Landkarte (Handles) | DB-Accounts | davon KI-Modus `[EST.]` | < 100K | davon H | 100–500K | 500K–1M | ≥ 1M | Follower UNKNOWN | Neu & schnell `[EST.]` | Reels im Sample | Median-vpf | Beispiele (Follower · bestes Reel im Sample) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **A** Interior-Pages, Studios, Creator | 121 | 31 | 7 | 6 | 4 | 13 | 6 | 5 | 1 | 2 | 89 | 3,8 | @paulmarkkitchens (304K · 135 Mio.), @elarch.studio (540K · 15,5 Mio.), @design_x_interior (88K · 17,4 Mio.), @georgios_tataridis (321K · 4,5 Mio.), @ell.glamhome (1M · 8,2 Mio.) |
| **B** Luxury Real Estate | 35 | 8 | 0 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 40 | 2,8 | @alshifarealtor.dxb (47K · 54,3 Mio.), @wayup_media (942K · 22,7 Mio.), @glashaus.realestate (296K · 1,5 Mio.), @theluxuryhomeshow (2M · 5,8 Mio.) |
| **C** Architektur-/Designmedien | 39 | 3 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 9 | 3,6 | @architectanddesign (8,4M · 55,2 Mio.), @hafezi.architects (606K · 4,3 Mio.) |
| **D** KI-Architektur | 25 | 20 | 15 | 6 | 2 | 7 | 2 | 4 | 1 | 3 | 81 | 2,8 | @aiforarchitects (1M · 34,7 Mio.), @sunt_mrr (2M · 24,5 Mio.), @elitebuildhq (2M · 24 Mio.), @archibible (220K · 14,3 Mio.), @visionbuildofficial (50K · 6,6 Mio.) |
| **E** KI-Interior / Cozy / Transformation | 25 | 21 | 18 | 7 | 5 | 5 | 5 | 3 | 1 | 3 | 81 | 3,0 | @siyad_abdali (4M · 282 Mio.), @drcozyvibes (584K · 155 Mio.), @soothenests (2M · 45,1 Mio.), @neuraltransform (83K · 2,7 Mio.), @roomify.design (62K · 1,7 Mio.) |
| **F** Dream-/Future-Home-Pages | 28 | 6 | 4 | 1 | 0 | 3 | 0 | 2 | 0 | 2 | 40 | 1,0 | @manhwa_diablo (331K · 78,4 Mio.), @luxurydreamhub (1M · 8,2 Mio.), @luxuryhouseview (389K · 4,7 Mio.), @exploringdreamhomes (177K · 996 Tsd.) |
| **G** Luxury Lifestyle / Travel / Hotels | 30 | 16 | 1 | 1 | 1 | 2 | 3 | 9 | 1 | 1 | 53 | 1,9 | @syifa_in_switzerland (3M · 71,8 Mio.), @clarazrd (297K · 72,1 Mio.), @timelessdiaries (65K · 60,7 Mio.), @beautifulhotels (6M · 5,4 Mio.) |
| **H** Klein + Millionen-Views (Querschnitt) | 51 | *15* | *8* | *15* | *15* | – | – | – | – | – | – | – | siehe 2.4 |
| Sonstige (nicht Interior) | – | 6 | 2 | 2 | 2 | 0 | 1 | 0 | 3 | 0 | 8 | – | @ai.poly_ (14K · 147 Mio.), @polliviva (48K · 97,2 Mio.), @earthfm_net (757K · 58,5 Mio.) |
| **Summe DB** | **354** | **111** | **47** | **25** | **15** | **34** | **19** | **26** | **7** | **11** | | | |

Die H-Zeile ist kursiv, weil sie Accounts aus A–G doppelt zählt. Tier-, UNKNOWN- und Reel-Spalten folgen den Feldern der Competitor-DB. Drei Accounts führt die DB mit 0 Reels, obwohl `04_reel_database.csv` Reels enthält: @luxuriatetouche (2), @ti.fu (1), @kohlectcabins (2). Für @ti.fu (272K) und @kohlectcabins (434K) zeigen die Reel-Embeds Follower, die DB führt sie als UNKNOWN. Vollständige Liste aller 111 Accounts nach Gruppe: Anhang A.

**Wie man die Tabelle liest:**
- **D und E sind die direkten Wettbewerber** (41 DB-Accounts, davon 33 im KI-Modus). A enthält die zweite Welle: Studios, die mit KI-Look oder 3D-Renderings Aufträge akquirieren.
- **Große Theme-Pages (F, Teile von E) haben niedrige vpf:** Median 1,0 in F; @naturesms hat 10M Follower, das beste Reel im Sample aber nur 1,3 Mio. Views (vpf 0,13).
- Die Gruppen-Mediane sind **keine** fairen Vergleichswerte. Dafür gilt die Reel-Ebene mit adj_factor:

![Performance vs. Erwartung nach Account-Typ](charts/adj_by_account_type.png)

| Account-Typ (Reel-Ebene) | n Reels | Median adj_factor | Anteil ≥ 5× Follower |
|---|---:|---:|---:|
| lifestyle_influencer | 508 | 1,24 | 44 % |
| ai_creator | 276 | 1,09 | 43 % |
| contractor_trade | 100 | 0,96 | 45 % |
| designer_studio | 382 | 0,88 | 36 % |
| real_estate | 223 | 0,83 | 34 % |
| brand_manufacturer | 123 | 0,80 | 35 % |
| media_publication | 66 | 0,79 | 12 % |
| theme_page | 503 | 0,74 | 33 % |

Quelle: `stats/seg_account_kind_hint.csv` bzw. Digest „Account type“. Der Unterschied ist nach Bonferroni-Korrektur **signifikant** (Kruskal-Wallis p < 0,001 für topic_index und adj). Nur KI-Reels: Theme-Page 0,70 (n = 228) vs. AI-Creator 1,02 (n = 271), Verhältnis ≈ 0,68×, 95-%-KI 0,39–0,84, p < 0,001. KI-Reels von Accounts, die als Designstudio codiert sind, liegen bei 0,80 (n = 110; eigene Auswertung aus `04_reel_database.csv`). **Ein Studio-Label allein hebt die Werte also nicht**; ob eine erkennbare eigene Handschrift den Unterschied macht, ist eine Hypothese für eigene Tests.

### 2.3 Follower-Tiers über den gesamten Reel-Datensatz

| Tier (Reel-Ebene) | n Reels | Median Views | Median vpf | Median adj_factor | Anteil Reels ≥ 5× Follower | Accounts im Datensatz |
|---|---:|---:|---:|---:|---:|---:|
| < 10K | 402 | 20 Tsd. | 9,3 | 0,89 | 57 % | 1.120 (< 100K gesamt) |
| 10K–100K | 850 | 187 Tsd. | 5,1 | 1,07 | 50 % | ↑ |
| 100K–500K | 674 | 320 Tsd. | 1,5 | 0,86 | 27 % | 531 |
| 500K–1M | 325 | 638 Tsd. | 0,84 | 0,87 | 17 % | 157 |
| 1M+ | 127 | 1,2 Mio. | 0,27 | 0,91 | 9 % | 105 |

Quelle: `stats/seg_follower_bucket.csv`; Account-Zählung aus `04_reel_database.csv` (1.913 Accounts mit Followerzahl). Follower sind der stärkste Einzeltreiber absoluter Views (Spearman ρ = 0,43, n = 2.378). Nach Größenbereinigung liegt das **10–100K-Tier vorn** (1,07 vs. 0,86–0,91 in den übrigen Tiers). Der Abstand ist klein und nicht getestet; ob Spezialisierung dahintersteht, ist offen. Es ist keine Aussage über Ursachen.

### 2.4 Tier-Listen mit Beispielen

**a) < 100K Follower mit Millionen-Views (Gruppe H)**

- **Häufigkeit:** 207 Accounts mit < 100K Followern haben ein Reel ≥ 1 Mio. Views, 21 davon eines ≥ 10 Mio. Produktion der jeweiligen Top-Reels: 143 real, 45 KI, 11 3D, 8 unklar; bei ≥ 10 Mio.: 14 real, 6 KI, 1 3D `[Zählung VERIFIED; Produktion ESTIMATED]`. q05 hatte in einem früheren DB-Snapshot 70 solcher Accounts gezählt; die DB ist seither gewachsen.
- **Survivorship-Bias:** Wie viele kleine Accounts *ohne* Hit posten, ist unbekannt `[UNKNOWN]`.

| Account | Follower | bestes Reel im Sample | Produktion `[EST.]` | Motiv (Codierung) | n Reels |
|---|---:|---:|---|---|---:|
| @alshifarealtor.dxb | 47K | 54,3 Mio. | real | Dubai-Villa, Money-Hook („HOW MUCH RENT DO YOU PAY?“, beobachtet) | 1 |
| @timelessdiaries | 65K | 60,7 Mio. | real | Färöer-Haus, „Maybe I don’t want a bigger house…“ (beobachtet) | 1 |
| @sanyamboraarchitects | 32K | 19,3 Mio. | KI | Bad mit „WRONG / CORRECT“-Maßen auf dem Cover | 1 |
| @design_x_interior | 88K | 17,4 Mio. | KI | dunkles Luxus-Schlafzimmer, Budget-Hook | 2 |
| @kratosdigitalarts | 90K | 17,1 Mio. | KI | Cartoon-Figuren (Fremd-IP) auf einer Dachterrasse im Sturm, KI offengelegt | 1 |
| @abdullahaslanoglu_ | 68K | 10,2 Mio. | 3D | Villa-Fassade mit Lichtkanten | 2 |
| @designevolutionn | 26K | 8,9 Mio. | KI | Luxus-Garten | 1 |
| @craftlab2050 | 50K | 7,1 Mio. | KI | Baumhaus-Bau im Dschungel | 1 |
| @visionbuildofficial | 50K | 6,6 Mio. | KI | Schlangen-Turm („Ever Built in the USA“, beobachtet) | 3 |
| @relaxationreflections_ | 12K | 6,0 Mio. | KI | Regen-Schlafzimmer, Frage-Hook | 2 |
| @processlabstudio | 10K | 4,6 Mio. | KI | Luxus-Bunker unter einer Villa | 1 |
| @stylishnorrastudios | 40K | 3,7 Mio. | KI (wahrscheinlich) | Walnuss-Pavillon mit Regenwaldblick | 2 |
| @neuraltransform | 83K | 2,7 Mio. | KI | Wüsten-Infinity-Pool | 3 |

**Muster:** Die KI-Ausreißer unter den kleinen Accounts zeigen überwiegend **ungewöhnliche Architektur, Außenräume oder ein klares „Aha“** (Bunker, Baumhaus, Schlangenturm, Garten, falsche vs. richtige Maße). Klassische Luxus-Schlafzimmer sind die Ausnahme (@design_x_interior, @relaxationreflections_).

**b) 100–500K Follower**

@archibible (220K · 14,3 Mio.), @georgios_tataridis (321K · 4,5 Mio.), @diniz_nasaroba (293K · 25 Mio.), @urban_lifestyle_lab (250K · 3 Mio.), @manhwa_diablo (331K · 78,4 Mio.), @sandiwara_multiverse.99 (402K · 85,2 Mio., n = 1), @homeofmerve (459K · 13,1 Mio.), @luxuryhouseview (389K · 4,7 Mio.). In diesem Tier liegen die meisten Shortlist-Accounts: 6 der Top 20 (weitere 5 unter 100K, 4 bei 500K–1M, 5 ab 1M).

**c) 500K–1M Follower**

@elarch.studio (540K · 15,5 Mio.), @siriorsinterior (547K · 3,7 Mio.), @montani3d (603K · 946 Tsd.), @drcozyvibes (584K · 155 Mio.), @nostalgicraindrops (713K · 14,1 Mio.), @cairo_ia (944K · 81,1 Mio., n = 1), @wayup_media (942K · 22,7 Mio.), @arteo_luxury (871K · 3,5 Mio.), @miladeshtiyaghi (642K · 2,1 Mio.).

**d) ≥ 1M Follower**

@siyad_abdali (4M · 282 Mio.), @sunt_mrr (2M · 24,5 Mio.), @soothenests (2M · 45,1 Mio.), @elitebuildhq (2M · 24 Mio.), @aiforarchitects (1M · 34,7 Mio.), @ifonly.ai (1M · 136 Mio., n = 1), @luxurydreamhub (1M · 8,2 Mio.), @naturesms (10M · 1,3 Mio.), @thetrillionairelife (13M · 1,4 Mio.). Bei den ganz großen Theme-Pages (≥ 5M) liegt das beste Reel im Sample oft **unter** der Followerzahl. Das passt zur HypeAuditor-Beobachtung sehr niedrigen „Authentic Engagement“ großer Theme-Pages in [q05](quellen/q05_competitor_lists.md) `[THIRD-PARTY ESTIMATE]`.

**e) Neue, schnell wachsende Accounts (Kandidaten)**

**Definition:** Ältestes im Sample gesehenes Reel ≥ 25.09.2025, ≥ 100K Follower und eine rechnerische Posting-Rate ≤ 21 Posts/Woche. Letzteres ist ein Plausibilitätsfilter: Bei mehr als 3 Posts pro Tag ist der Account sehr wahrscheinlich älter als sein ältestes gesehenes Reel. Das Datum stammt aus dem Shortcode des ältesten *gesehenen* Reels, nicht aus dem Gründungsdatum. Deshalb sind alle Einträge nur **Kandidaten** `[ESTIMATED]`.

| Account | Gruppe | Follower | Posts | ältestes gesehenes Reel | n Reels | Modus `[EST.]` | bestes Reel |
|---|---|---:|---:|---|---:|---|---:|
| @elitebuildhq | D | 2M | 317 | 2026-04-09 | 6 | KI | 24 Mio. |
| @cairo_ia | E | 944K | 219 | 2026-03-08 | 1 | KI | 81,1 Mio. |
| @sandiwara_multiverse.99 | D | 402K | 79 | 2026-07-20 | 1 | KI | 85,2 Mio. |
| @manhwa_diablo | F | 331K | 115 | 2026-01-29 | 2 | gemischt | 78,4 Mio. |
| @georgios_tataridis | A | 321K | 321 | 2026-01-22 | 2 | 3D | 4,5 Mio. |
| @olena_prykhodko_design | A | 308K | 434 | 2026-01-24 | 3 | unklar | 1,7 Mio. |
| @luxquisit | D | 190K | 463 | 2025-10-12 | 4 | KI | 912 Tsd. |
| @exploringdreamhomes | F | 177K | 167 | 2026-02-05 | 5 | KI | 996 Tsd. |
| @ai.design.ideas | E | 136K | 249 | 2025-12-31 | 3 | KI | 11,3 Mio. |
| @nouxri | G | 120K | 227 | 2025-11-10 | 3 | real | 7,5 Mio. |
| @watchthebuild | E | 107K | 128 | 2026-07-04 | 4 | KI | 1,3 Mio. |

- **Beobachtung:** 7 der 11 Kandidaten posten KI, meist Konzeptbauten oder Transformationen (Bunker, Baumhaus, Garten-Makeover, leerer Raum → eingerichtet). Einträge mit n = 1 sind am schwächsten belegt.
- **Außerhalb der DB** erfüllt auch @diniz_nasaroba die Kriterien (293K, 52 Posts, ältestes gesehenes Reel 2026-03-27, n = 2, KI; Abschnitt 5.17).
- **Belegter Vergleichsfall:** Tim Fu (KI-Architektur, namentlich auftretend) wuchs nach eigener Aussage von „a few hundred“ Followern (Juli 2022) auf über 100K in weniger als 11 Monaten ([q06](quellen/q06_ai_theme_page_case_studies.md)) `[VERIFIED – Selbstauskunft]`.

---

## 3. Outperformance-Accounts: Views im Verhältnis zu Followern

### 3.1 Top 25 nach Median-vpf (≥ 2 Reels im Sample, ≥ 1.000 Follower)

Basis: 261 Kandidaten aus [shortlist_scores.csv](data/processed/shortlist_scores.csv). 98 davon (38 %) erfüllen die Outperformer-Definition des Skripts: Median-vpf ≥ 5 bei ≥ 2 Reels. **Alle Zeilen mit n = 2 oder 3 sind Einzelbeobachtungen und kein stabiler Account-Wert.**

| # | Account | Follower | n Reels | Median Views | Max Views | Median vpf | Max vpf | Median adj | Lesart | Typ (codiert) | Produktion | Shortlist-Rang |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---:|
| 1 | @soldbytyler | 12K | 2 | 5,2 Mio. | 8,8 Mio. | 438× | 733× | 77,8 | 12K Follower + 8,8 Mio. Views = 733× | real_estate | real | 85 |
| 2 | @archstudent.marteen | 51K | 2 | 18,9 Mio. | 32 Mio. | 370× | 627× | 2,0 | 51K + 32 Mio. = 627× | lifestyle | real | 138 |
| 3 | @relaxationreflections_ | 12K | 2 | 3 Mio. | 6 Mio. | 252× | 500× | 36,1 | 12K + 6 Mio. = 500× | ai_creator | KI | 45 |
| 4 | @paulmarkkitchens | 304K | 2 | 68,3 Mio. | 135 Mio. | 225× | 444× | 44,0 | 304K + 135 Mio. = 444× | brand | real | 30 |
| 5 | @tiatinn_ | 8K | 3 | 1,4 Mio. | 1,4 Mio. | 175× | 175× | 20,4 | 8K + 1,4 Mio. = 175× | real_estate | real | 95 |
| 6 | @proud_and_property | 50K | 2 | 7,2 Mio. | 13,5 Mio. | 144× | 270× | 10,4 | 50K + 13,5 Mio. = 270× | real_estate | real | 146 |
| 7 | @clarazrd | 297K | 2 | 36,8 Mio. | 72,1 Mio. | 124× | 243× | 18,0 | 297K + 72,1 Mio. = 243× | lifestyle | real | 75 |
| 8 | @manhwa_diablo | 331K | 2 | 39,6 Mio. | 78,4 Mio. | 119× | 237× | 26,3 | 331K + 78,4 Mio. = 237× | theme_page | gemischt | 28 |
| 9 | @design_x_interior | 88K | 2 | 8,9 Mio. | 17,4 Mio. | 102× | 200× | 19,2 | 88K + 17,4 Mio. = 200× | designer_studio | KI | 3 |
| 10 | @_crystalvisual | 10K | 2 | 946 Tsd. | 1,8 Mio. | 95× | 180× | 3,5 | 10K + 1,8 Mio. = 180× | ai_creator | KI | 82 |
| 11 | @rvnxii_ | 21K | 2 | 1,8 Mio. | 3,5 Mio. | 84× | 167× | 2,6 | 21K + 3,5 Mio. = 167× | theme_page | real | 212 |
| 12 | @purehotelbyhollywood | 10K | 2 | 803 Tsd. | 1,6 Mio. | 80× | 160× | 12,2 | 10K + 1,6 Mio. = 160× | other | real | 163 |
| 13 | @abdullahaslanoglu_ | 68K | 2 | 5,2 Mio. | 10,2 Mio. | 76× | 150× | 15,8 | 68K + 10,2 Mio. = 150× | designer_studio | 3D | 25 |
| 14 | @lisi.quietdiaries | 153K | 2 | 11,4 Mio. | 22,7 Mio. | 75× | 148× | 14,8 | 153K + 22,7 Mio. = 148× | lifestyle | real | 51 |
| 15 | @bic_trading | 14K | 2 | 974 Tsd. | 1,9 Mio. | 70× | 136× | 5,0 | 14K + 1,9 Mio. = 136× | theme_page | real | 135 |
| 16 | @quaintandsimple | 26K | 2 | 1,8 Mio. | 2,8 Mio. | 69× | 108× | 23,7 | 26K + 2,8 Mio. = 108× | lifestyle | real | 67 |
| 17 | @imtiazsahib33 | 120K | 2 | 8,3 Mio. | 16,6 Mio. | 69× | 138× | 15,2 | 120K + 16,6 Mio. = 138× | other | KI (50 %) | 96 |
| 18 | @myplants.uae | 123K | 2 | 8,3 Mio. | 15,6 Mio. | 67× | 127× | 19,8 | 123K + 15,6 Mio. = 127× | contractor_trade | KI | 1 |
| 19 | @vesgantti_home | 22K | 2 | 1,4 Mio. | 2 Mio. | 62× | 91× | 5,5 | 22K + 2 Mio. = 91× | theme_page | KI (50 %) | 59 |
| 20 | @stylishnorrastudios | 40K | 2 | 2,2 Mio. | 3,7 Mio. | 56× | 92× | 11,3 | 40K + 3,7 Mio. = 92× | designer_studio | KI (50 %) | 10 |
| 21 | @shanwicki | 60K | 3 | 2,9 Mio. | 7 Mio. | 48× | 117× | 11,4 | 60K + 7 Mio. = 117× | lifestyle | real | 68 |
| 22 | @astralgate.ai | 44K | 2 | 2,1 Mio. | 4,1 Mio. | 47× | 93× | 1,7 | 44K + 4,1 Mio. = 93× | ai_creator | KI | 48 |
| 23 | @earthfm_net | 757K | 2 | 35,3 Mio. | 58,5 Mio. | 47× | 77× | 2,7 | 757K + 58,5 Mio. = 77× | theme_page | unklar | 73 |
| 24 | @renovaistudio | 11K | 2 | 506 Tsd. | 713 Tsd. | 46× | 65× | 3,5 | 11K + 713 Tsd. = 65× | ai_creator | KI | 49 |
| 25 | @visionbuildofficial | 50K | 3 | 2,3 Mio. | 6,6 Mio. | 46× | 132× | 5,3 | 50K + 6,6 Mio. = 132× | ai_creator | KI | 29 |

Views und Follower `[VERIFIED]` (gerundet); Typ und Produktion `[ESTIMATED]`; „KI (50 %)“ = eines von zwei Reels KI-codiert.

![Views ÷ Follower nach Account](charts/vpf_by_account.png)

### 3.2 Einzel-Hits (nur 1 Reel im Sample, daher nicht im Scoring)

| Account | Follower | Reel | vpf | Produktion `[EST.]` | Relevanz für uns |
|---|---:|---:|---:|---|---|
| @ai.poly_ | 14K | 147 Mio. | 10.500× | KI | gering: allgemeines KI-Video (russische Caption), kein Interior ([q05](quellen/q05_competitor_lists.md)) |
| @polliviva | 48K | 97,2 Mio. | 2.025× | KI | gering: Cartoon-Bad, Humor; zeigt aber, dass Fantasy und Humor 2026 noch durchbrechen ([q06](quellen/q06_ai_theme_page_case_studies.md)) |
| @alshifarealtor.dxb | 47K | 54,3 Mio. | 1.155× | real | Money-Hook plus Kommentar-Keyword im Immobilienkontext |
| @timelessdiaries | 65K | 60,7 Mio. | 934× | real | Sehnsuchts-Setting (Färöer), Cover-Text als innerer Monolog |
| @kellmarcel | 126K | 74,9 Mio. | 594× | real | „richte mit mir ein“ (Creator-Format) |
| @sandiwara_multiverse.99 | 402K | 85,2 Mio. | 212× | KI | Riesen-Baumhaus im Regenwald: ungewöhnliche Wohnform |
| @ifonly.ai | 1M | 136 Mio. | 136× | KI, offengelegt | Tiramisu-Haus: surreales Konzept, KI in der Caption genannt ([q06](quellen/q06_ai_theme_page_case_studies.md)) |
| @cairo_ia | 944K | 81,1 Mio. | 86× | KI | Paletten → Backyard-Oase: Transformation |

### 3.3 Warum vpf allein täuscht, und was stattdessen zählt

- **Größeneffekt:** Unter den 261 Kandidaten erreichen 67 % der 10–100K-Accounts (n = 86) einen Median-vpf ≥ 5, aber nur 30 % bei 100–500K (n = 93), 10 % bei 500K–1M (n = 41) und 14 % bei ≥ 1M (n = 36). Der Median-vpf fällt von 11,7 (10–100K) auf 0,54 (≥ 1M). Ein hoher vpf ist also vor allem ein Merkmal **kleiner** Accounts.
- **KI vs. nicht KI:** Accounts mit ≥ 50 % KI-Reels sind nicht häufiger Outperformer als andere (36 %, n = 110 vs. 38 %, n = 151).
- **Follower-Zeitpunkt:** Gemessen wird mit den Followern *beim Abruf*, also nach dem Hit. Bei Accounts, die durch einen Hit gewachsen sind, **unterschätzt** vpf die damalige Überperformance.
- **Konsequenz:** Für die Shortlist ist vpf nur ein Kriterium (20 %). Für Aussagen über Formate nutzen wir adj_factor. Beispiel: @montani3d hat vpf 1,1 und adj 0,98 (liegt genau im Erwartungswert), @design_x_interior vpf 102 und adj 19,2 (einer von zwei Reels war ein Mega-Hit).

---

## 4. Teil 3 – Shortlist der 20 interessantesten Accounts (nicht nach Followern)

### 4.1 Scoring-Methode ([scripts/shortlist.py](scripts/shortlist.py))

**Kandidaten:** alle Accounts mit bekannter Followerzahl ≥ 1.000 und ≥ 2 Reels im Topic-Sample (n = 261). Jedes Kriterium wird in einen **Perzentilrang 0–1** unter den Kandidaten umgerechnet (Gleichstände teilen sich den Rang, fehlende Werte = 0) und gewichtet:

| Kriterium | Messgröße | Gewicht | Warum |
|---|---|---:|---|
| Viralität | Median Views ÷ Follower | 0,20 | Überperformance relativ zur Größe |
| Konsistenz | Anteil Reels über dem Median ihrer Topic-Seite | 0,10 | nicht nur ein Glückstreffer |
| Reichweite | Median Views | 0,10 | absolute Nachfrage |
| Wachstum (Proxy) | Follower ÷ Tage seit ältestem gesehenem Post (mind. 30) | 0,10 | `[ESTIMATED]`, Alter = Untergrenze |
| Wiederholbarkeit | Reels im Sample (gedeckelt bei 8) | 0,10 | Breite auf Topic-Seiten |
| KI-Eignung | Anteil KI- oder 3D-Reels | 0,15 | Übertragbarkeit auf unser Produktionsmodell |
| Monetarisierbarkeit | beobachtete Monetarisierungstypen + Anteil kaufbarer Szenen | 0,10 | Geschäftsmodell sichtbar |
| Qualität | Anteil „high visual quality“ | 0,10 | Produktionsniveau |
| Originalität | 1 = Creator/Studio/Marke/Makler/Handwerk/Lifestyle, 0,5 = Theme-Page, 0 = sonst | 0,05 | Repost-Aggregatoren abwerten |

**Prüfung „nicht nach Followern“:** Die Spearman-Korrelation von Score und Followern liegt bei ρ = 0,03 (p = 0,62, n = 261). Die Top 20 reichen von 40K bis 4M Followern (Median 307K).

**Bekannte Verzerrungen des Scores:**
- **Monetarisierbarkeit hängt am Tiefenprofil.** Nur 66 der 261 Kandidaten sind tief profiliert, aber 19 der Top 20. Nicht profilierte Accounts bekommen 0 beobachtete Monetarisierungstypen (Beispiel @diniz_nasaroba: Teilscore 0,45).
- **KI-Eignung bevorzugt KI/3D bewusst** (Projektziel). Reale Accounts schaffen es nur mit sehr starken übrigen Werten in die Top 20 (@syifa_in_switzerland).
- Bei n = 2 kann „Konsistenz“ nur 0, 50 oder 100 % sein; der Wert ist grob.
- **Der Score ist eine Priorisierungshilfe für die Analyse, kein Qualitätsurteil.**

### 4.2 Top 20 mit Score-Aufschlüsselung

Teilscores = Perzentilränge (0–1); Gewicht in Klammern. Outperformer = Median-vpf ≥ 5 bei ≥ 2 Reels.

| Rang | Account | Viralität (0,20) | Konsistenz (0,10) | Reichweite (0,10) | Wachstum (0,10) | Wiederholbarkeit (0,10) | KI-Eignung (0,15) | Monetarisierbarkeit (0,10) | Qualität (0,10) | Originalität (0,05) | **Score** | Outperformer |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | @myplants.uae | 0,94 | 0,88 | 0,94 | 0,56 | 0,32 | 0,79 | 0,98 | 0,75 | 0,66 | **0,782** | ja |
| 2 | @archibible | 0,89 | 0,88 | 0,94 | 0,34 | 0,32 | 0,79 | 0,98 | 0,75 | 0,66 | **0,750** | ja |
| 3 | @design_x_interior | 0,97 | 0,88 | 0,95 | 0,24 | 0,32 | 0,79 | 0,86 | 0,75 | 0,66 | **0,746** | ja |
| 4 | @elarch.studio | 0,75 | 0,64 | 0,91 | 0,47 | 0,72 | 0,79 | 0,90 | 0,75 | 0,66 | **0,741** | ja |
| 5 | @georgios_tataridis | 0,70 | 0,88 | 0,83 | 0,71 | 0,32 | 0,79 | 0,94 | 0,75 | 0,66 | **0,735** | ja |
| 6 | @sunt_mrr | 0,34 | 0,76 | 0,84 | 0,84 | 0,99 | 0,79 | 0,88 | 0,75 | 0,66 | **0,726** | nein |
| 7 | @aiforarchitects | 0,41 | 0,75 | 0,77 | 0,67 | 0,97 | 0,79 | 0,89 | 0,75 | 0,66 | **0,715** | nein |
| 8 | @soothenests | 0,54 | 0,88 | 0,93 | 0,83 | 0,85 | 0,79 | 0,91 | 0,27 | 0,19 | **0,705** | nein |
| 9 | @neuraltransform | 0,82 | 0,64 | 0,74 | 0,27 | 0,72 | 0,79 | 0,70 | 0,75 | 0,66 | **0,699** | ja |
| 10 | @stylishnorrastudios | 0,93 | 0,88 | 0,80 | 0,30 | 0,32 | 0,51 | 0,94 | 0,75 | 0,66 | **0,694** | ja |
| 11 | @watchthebuild | 0,61 | 0,71 | 0,47 | 0,70 | 0,85 | 0,79 | 0,70 | 0,75 | 0,66 | **0,693** | nein |
| 12 | @syifa_in_switzerland | 0,77 | 0,64 | 0,92 | 0,93 | 0,72 | 0,24 | 0,70 | 0,75 | 0,66 | **0,689** | ja |
| 13 | @siriorsinterior | 0,57 | 0,88 | 0,79 | 0,53 | 0,32 | 0,79 | 0,88 | 0,75 | 0,66 | **0,680** | nein |
| 14 | @nostalgicraindrops | 0,65 | 0,88 | 0,87 | 0,51 | 0,72 | 0,55 | 0,85 | 0,75 | 0,19 | **0,679** | ja |
| 15 | @zaxzaaafrica | 0,74 | 0,88 | 0,55 | 0,36 | 0,32 | 0,79 | 0,94 | 0,75 | 0,66 | **0,679** | ja |
| 16 | @siyad_abdali | 0,30 | 0,64 | 0,89 | 0,90 | 0,96 | 0,79 | 0,53 | 0,75 | 0,66 | **0,678** | nein |
| 17 | @diniz_nasaroba | 0,90 | 0,88 | 0,97 | 0,00 | 0,32 | 0,79 | 0,45 | 0,75 | 0,66 | **0,670** | ja |
| 18 | @roomify.design | 0,64 | 0,58 | 0,35 | 0,20 | 0,97 | 0,79 | 0,94 | 0,75 | 0,66 | **0,660** | ja |
| 19 | @urban_lifestyle_lab | 0,60 | 0,71 | 0,67 | 0,44 | 0,85 | 0,79 | 0,36 | 0,75 | 0,66 | **0,651** | nein |
| 20 | @montani3d | 0,29 | 0,71 | 0,57 | 0,81 | 0,85 | 0,79 | 0,96 | 0,45 | 0,66 | **0,647** | nein |

Knapp dahinter (Rang 21–25): @ell.glamhome (0,644), @recastliving (0,641), @vrishtidesigns (0,634), @juliagal_ (0,630), @abdullahaslanoglu_ (0,629).

### 4.3 Kennzahlen der Top 20

| Rang | Account | Gruppe | Follower | Posts | n Reels | Median / Max Views | Median vpf | Median adj | Reels > Topic-Median | Produktion `[EST.]` | ältestes gesehenes Reel | Posts/Woche (Obergrenze) |
|---:|---|---|---:|---:|---:|---|---:|---:|---:|---|---|---:|
| 1 | @myplants.uae | A (Trade) | 123K | 547 | 2 | 8,3 Mio. / 15,6 Mio. | 67,3 | 19,8 | 100 % | KI | 2026-05-12 | 28,4 † |
| 2 | @archibible | D | 220K | 1.206 | 2 | 7,4 Mio. / 14,3 Mio. | 33,5 | 9,7 | 100 % | KI (+ 3D) | 2025-05-15 | 17,0 |
| 3 | @design_x_interior | A | 88K | 379 | 2 | 8,9 Mio. / 17,4 Mio. | 102,2 | 19,2 | 100 % | KI | 2026-01-31 | 11,2 |
| 4 | @elarch.studio | A | 540K | 3.243 | 3 | 5,5 Mio. / 15,5 Mio. | 10,2 | 13,2 | 67 % | 3D | 2024-09-14 | 30,7 † |
| 5 | @georgios_tataridis | A | 321K | 321 | 2 | 2,6 Mio. / 4,5 Mio. | 8,2 | 3,3 | 100 % | 3D | 2026-01-22 | 9,2 |
| 6 | @sunt_mrr | D | 2M | 728 | 9 | 2,9 Mio. / 24,5 Mio. | 1,4 | 3,1 | 89 % | KI | 2024-09-04 | 6,8 |
| 7 | @aiforarchitects | D | 1M | 513 | 7 | 2 Mio. / 34,7 Mio. | 2,0 | 1,3 | 86 % | KI | 2024-06-10 | 4,3 |
| 8 | @soothenests | E | 2M | 2.119 | 4 | 7 Mio. / 45,1 Mio. | 3,5 | 3,3 | 100 % | KI | 2024-08-29 | 19,6 |
| 9 | @neuraltransform | E | 83K | 97 | 3 | 1,6 Mio. / 2,7 Mio. | 19,3 | 1,8 | 67 % | KI | 2026-02-27 | 3,2 |
| 10 | @stylishnorrastudios | A | 40K | 502 | 2 | 2,2 Mio. / 3,7 Mio. | 55,7 | 11,3 | 100 % | KI (wahrsch.) | 2026-06-20 | 36,6 † |
| 11 | @watchthebuild | E | 107K | 128 | 4 | 497 Tsd. / 1,3 Mio. | 4,7 | 2,3 | 75 % | KI | 2026-07-04 | 10,9 |
| 12 | @syifa_in_switzerland | G | 3M | 2.642 | 3 | 6,6 Mio. / 71,8 Mio. | 12,0 | 33,5 | 67 % | real | 2025-08-20 | 46,2 † |
| 13 | @siriorsinterior | A | 547K | 2.727 | 2 | 2,1 Mio. / 3,7 Mio. | 3,8 | 9,1 | 100 % | 3D | 2025-01-17 | 31,0 † |
| 14 | @nostalgicraindrops | E | 713K | 151 | 3 | 3,9 Mio. / 14,1 Mio. | 5,5 | 1,9 | 100 % | KI (+ VFX) | 2024-05-30 | 1,2 |
| 15 | @zaxzaaafrica | A | 65K | 763 | 2 | 650 Tsd. / 977 Tsd. | 10,0 | 2,1 | 100 % | KI | 2026-05-21 | 42,4 † |
| 16 | @siyad_abdali | E | 4M | 2.110 | 6 | 4,5 Mio. / 282 Mio. | 1,1 | 5,7 | 67 % | KI | 2024-07-11 | 18,3 |
| 17 | @diniz_nasaroba | E (nicht in DB) | 293K | 52 | 2 | 13,1 Mio. / 25 Mio. | 44,7 | 8,4 | 100 % | KI | 2026-03-27 | 2,0 |
| 18 | @roomify.design | E | 62K | 152 | 7 | 337 Tsd. / 1,7 Mio. | 5,4 | 1,8 | 57 % | KI | 2026-02-20 | 4,9 |
| 19 | @urban_lifestyle_lab | D | 250K | 4.660 | 4 | 1,1 Mio. / 3 Mio. | 4,2 | 4,7 | 75 % | KI | 2025-10-04 | 91,9 † |
| 20 | @montani3d | D | 603K | 1.578 | 4 | 684 Tsd. / 946 Tsd. | 1,1 | 1,0 | 75 % | KI | 2026-01-19 | 44,5 † |

† = mehr als 21 Posts/Woche. Hier ist der Account sehr wahrscheinlich älter als das älteste gesehene Reel, die echte Frequenz liegt deutlich niedriger. Die Posting-Frequenz ist grundsätzlich eine **Obergrenze** (Posts ÷ Tage seit ältestem gesehenem Post). Median der plausiblen Werte (n = 12): **8,0 Posts/Woche** (≈ 1,1 pro Tag), Spanne 1,2–19,6. Posts von @diniz_nasaroba stammen aus dem Reel-Embed in `04_reel_database.csv` (nicht in der Competitor-DB).

---

## 5. Teil 4 – Analyse der Top-20-Accounts und ihrer Reels (mit Teil 20: Monetarisierung)

**Aufbau je Account:** Datenzeile → Reels im Sample (Views `[VERIFIED]`, adj, Motiv aus der Codierung `[ESTIMATED]`) → Analyse → Monetarisierung → Lernen (Prinzip) / Nicht kopieren. Profilangaben stammen aus `data/raw/accounts/profile_<handle>.json`. Instagram-Bios waren meist nicht abrufbar; wo eine Bio genannt wird, stammt sie von Threads oder Linktree (Abschnitt 9).

### 5.1 Rang 1 – @myplants.uae (A, Trade: Pflanzenhandel und Landscaping in Dubai)

**Daten:** 123K Follower · 547 Posts · 2 Reels · Median-vpf 67 · Median adj 19,8 · beide Reels KI, beide offen als KI gekennzeichnet.

**Reels im Sample:**
- [DYPJn3DMuaV](https://www.instagram.com/reel/DYPJn3DMuaV/): 15,6 Mio. Views, adj 37,4. Teich mit schwebenden Trittsteinen, Feuerstelle, Bougainvillea, Blue Hour. 246.948 Likes (Embed).
- DYQ3I3fMJkN: 957 Tsd., adj 2,3. Kleiner Pool mit Pergola im Innenhof, Blue Hour.

**Analyse:** Ein realer Gartenbau- und Pflanzenhändler postet KI-Konzepte für Gärten und Pools und bindet sie offen an die eigene Leistung (beobachtet: „AI-generated, but we'd absolutely build this…“). Das Format ist ein einzelner Außenraum in der Blue Hour mit Wasser, Feuer und üppiger Bepflanzung, ohne Cover-Text. Die Caption beginnt mit einem Teilen-Auslöser (beobachtet: „Send this to someone who…“) und endet mit einer Kommentarfrage. Beide Reels sind als KI gekennzeichnet, und der Account führt trotzdem die Shortlist an. Das ist bei n = 2 anekdotisch, passt aber zum nicht signifikanten Offenlegungseffekt innerhalb der KI-Reels (0,82×, p = 0,15).

**Monetarisierung:** Shopify-Shop für Pflanzen, Töpfe und Bäume `[VERIFIED]`. Dienstleistungen: Landscaping Design & Build, „2D & 3D Landscaping Design“, Pools und Wasserspiele, Wartung `[VERIFIED]`. Die Reels dienen als Lead-Generierung. Brand Deals wurden nicht gesehen, Umsatz `[UNKNOWN]`.

**Lernen:** *Machbar wirkendes Konzept plus ehrliches KI-Label* verbindet Fantasie mit Kaufabsicht. Außenraum, Wasser und Blue Hour passen zu den stärksten KI-Räumen (Garten 1,61, n = 43). Der Teilen-Impuls gehört in die erste Zeile. **Nicht kopieren:** die „Send this to someone who…“-Schablone wörtlich und das Motiv mit den schwebenden Trittsteinen. Eigene Variante: kaufbare Outdoor-Elemente als Teil einer Serie.

### 5.2 Rang 2 – @archibible (D, Futurist World-Builder)

**Daten:** 220K Follower · 1.206 Posts · 2 Reels · Median-vpf 33,5 · Median adj 9,7 · beide KI (Pipeline laut Linktree C4D, UE5 und KI) · Anzeigename laut Threads: Corey Danaher.

**Reels im Sample:**
- [DLI3AbXsnNC](https://www.instagram.com/reel/DLI3AbXsnNC/) „Alpine Future“: 14,3 Mio. Views, adj 18,9. Megastruktur mit Bögen über einer verschneiten Stadt, Blue Hour, winzige Menschen.
- DJsJL2ysHBZ „Archwave“: 446 Tsd., adj 0,59.

**Analyse:** Spekulative Architektur im epischen Maßstab, `fantasy_impossible`, mit kleinen menschlichen Figuren als Maßstab und Stadtlichtern. Die Caption besteht aus einem Werktitel mit 1–2 Wörtern, dann Follow-CTA, Shop- und Commission-Hinweis. Das eine Reel ist ein Mega-Hit, das andere liegt unter der Erwartung (Spanne 32×). Das Muster „Fantasy + Menschen“ entspricht den stärksten KI-Kontrasten im Datensatz (fantasy vs. dreamy 3,25×, p < 0,001; KI mit Personen 1,68×, p ≈ 0,02).

**Monetarisierung:** Luma-AI-Referral-Link als erster Linktree-Button `[VERIFIED]`. Auftragsarbeiten („DM for commissions“) `[VERIFIED]`. Ein Etsy-Shop ist gelistet, Inhalte und Preise sind `[UNKNOWN]` (HTTP 403). Kontakt per E-Mail in der Bio. Umsatz `[UNKNOWN]`.

**Lernen:** *Welt statt Raum:* Ein Werktitel wirkt wie ein Serienname, Menschen geben Maßstab und Geschichte. Ein hybrider Workflow (3D + KI) hebt die Qualität. **Nicht kopieren:** Sci-Fi-Megastädte und seine Titel. Unser Fokus sind *bewohnbare* Häuser im menschlichen Maßstab.

### 5.3 Rang 3 – @design_x_interior (A, Interior-„Studio“ aus Indien)

**Daten:** 88K Follower · 379 Posts · 2 Reels · Median-vpf 102 · Median adj 19,2 · beide KI-codiert `[ESTIMATED]`, nicht offengelegt.

**Reels im Sample:**
- [DULItzMjQq7](https://www.instagram.com/reel/DULItzMjQq7/): 17,4 Mio. Views, adj 37,4, vpf 200. Schwarzes Schlafzimmer mit orange leuchtender Deckenvoute und Kamin. 843.973 Likes, 2.147 Kommentare.
- DWgf2nQiV_a: 390 Tsd., adj 0,96, fast gleiche Formel.

**Analyse:** Dunkles Luxus-Schlafzimmer mit warmem Lichtkontrast bei Nachtlicht. Der Hook ist eine Budget-Spannung (beobachtet: „Client: I want Super luxury bedroom in my budget 💸“). Die Captions stellen die Bilder als reale Kundenprojekte mit Baustellen-Adresse dar und nennen eine Agentur für „Video Shoot + Edit“. Die Cover-Codierung sieht dagegen KI-Artefakte. Das zweite Reel mit derselben Formel blieb bei der Erwartung: ein One-Hit bei n = 2.

**Monetarisierung:** Framing als Designleistung (Kundenprojekte) `[VERIFIED als Caption]`. Link, Bio und Preise `[UNKNOWN]`. Kein Deal gesehen.

**Lernen (Hypothese):** *Preis-/Wert-Spannung* („Luxus trotz Budget“) kann Neugier erzeugen. Money-Hooks liegen segmentweit bei 1,19 (n = 82, nicht signifikant). Ein dunkler Raum mit einer warmen Lichtquelle ergibt eine klare Cover-Silhouette (Gestaltungsurteil, nicht getestet). **Nicht kopieren:** KI-Bilder als echte Kundenprojekte mit echter Adresse ausgeben. Das ist ein Irreführungsrisiko ([q07](quellen/q07_legal_ai_risk.md)) und bei fotorealistischem Content kennzeichnungspflichtig ([q01](quellen/q01_instagram_platform_rules.md)). Auch die „Client: I want…“-Schablone nicht übernehmen.

### 5.4 Rang 4 – @elarch.studio (A, Archviz-Studio aus Brasilien)

**Daten:** 540K Follower · 3.243 Posts · 3 Reels · Median-vpf 10,2 · Median adj 13,2 · klassisches 3D-Rendering, keine KI.

**Reels im Sample:**
- [C_5u72pxVBx](https://www.instagram.com/reel/C_5u72pxVBx/): 15,5 Mio. Views, adj 14,6. Nächtliche Vorbeifahrt an einem auskragenden Haus, Supersportwagen im Carport, Sternenhimmel.
- DHvsnj8oqaE: 5,5 Mio., adj 13,2. Fassade in der Blue Hour mit schwebenden Stufen.
- DQmCrTgiPzn: 36,5 Tsd., adj 0,09. Heimkino mit Sternendecke und Cover-Text „Me, you & a home cinema“.

**Analyse:** Filmische Außenansichten bei Nacht oder Blue Hour mit Kamerabewegung tragen den Account. Das einzige Interior-Reel mit Text-Cover fiel durch (Spanne 425×). Die Captions sind zweisprachig (PT/EN) und enthalten eine Kundennennung (beobachtet: „Rendered by @elarch.studio for @…“) sowie eine Kommentarfrage.

**Monetarisierung:** B2B-Renderings: Behance „House exterior renderings starting from US$200“, Website mit Archviz, Immobilienfilmen und 360°-Touren, Anfragen per WhatsApp `[VERIFIED]`. Kundenprojekte in Captions genannt `[VERIFIED]`. Ein YouTube-Kanal existiert (346 Abonnenten), spielt aber kaum eine Rolle. Umsatz `[UNKNOWN]`.

**Lernen:** *Kamerafahrt + Nachtlicht + ein Statusobjekt* geben einer ruhigen Architektur einen filmischen Moment. Die Instagram-Reichweite dient als Portfolio für B2B-Aufträge. **Nicht kopieren:** das Supersportwagen-Klischee, seine konkreten Kompositionen und Text-Cover (Text-Overlay 0,92×, n. s.; innerhalb von Accounts 14 % Text-Cover in den Top 10 % vs. 27 % in der unteren Hälfte, Digest Abschnitt 7).

### 5.5 Rang 5 – @georgios_tataridis (A, Interior-Architekt aus Athen)

**Daten:** 321K Follower · 321 Posts · 2 Reels · Median-vpf 8,2 · Median adj 3,3 · 3D-Renderings, keine generative KI · Kandidat „neu & schnell“ (ältestes gesehenes Reel 2026-01-22) `[ESTIMATED]`.

**Reels im Sample:**
- [DWWYZ87iiV4](https://www.instagram.com/reel/DWWYZ87iiV4/): 4,5 Mio. Views, adj 5,2. Schwarzer Bett-Baldachin mit linearen LED-Linien. 517 Kommentare.
- DT0BHW6Ct9o: 761 Tsd., adj 1,3. Penthouse in Dubai, doppelte Raumhöhe, Sternendecke. 427 Kommentare.

**Analyse:** Ein Einzeldesigner mit klarer Handschrift: zeitgenössischer Dark Luxury mit Lichtlinien. Die Captions sind in der Designer-Stimme geschrieben: Projektname, Stilsatz, Meinungsfrage und teils ein DM-Angebot. Likes sind ausgeblendet, die Kommentarzahlen hoch. Beide Reels liegen über der Erwartung (Spanne nur 6×; bei n = 2 kein stabiler Account-Wert).

**Monetarisierung:** Website mit Interior Design und 3D-Visualisierung weltweit, B2B-Kooperationen und Kontaktformular `[VERIFIED]`. DM-CTA in der Caption `[VERIFIED]`. Preise `[UNKNOWN]`.

**Lernen:** *Autorenschaft statt Theme-Page:* Eine erkennbare Person oder ein Studio mit Meinung erzeugt Kommentare und Aufträge. **Nicht kopieren:** seine Signatur aus schwarzem Riffelpaneel und LED-Linien.

### 5.6 Rang 6 – @sunt_mrr (D, KI-Villen und Fantasy-Architektur; Maria Dudkina laut Threads)

**Daten:** 2M Follower · 728 Posts · 9 Reels (bestes Sample der Shortlist) · Median-vpf 1,4 · Median adj 3,1 · alle KI, 7 von 9 offengelegt (#midjourney).

**Reels im Sample:**
- [DNS1_gYMh2a](https://www.instagram.com/reel/DNS1_gYMh2a/): 24,5 Mio. Views, adj 6,4. Runder Infinity-Pool über Reisterrassen in Bali, Nebel, Golden Hour.
- DG-dfDMMxzF: 6,8 Mio., adj 33,5. Pool an einer Felsklippe.
- C_fqAjaMNIJ: 5,4 Mio., adj 6,7. Haus in Gitarrenform (Kollaboration mit @ti.fu).
- DPT0PbTEwtD: 4,7 Mio., adj 3,1. Unterwasser-Villa.
- DTkhih2DAEC: 2,9 Mio., adj 3,1. Schwarze Villa im Nebel.
- Weitere: 1,7 Mio. (adj 4,4, Cover „Plan A“), 1,6 Mio. (adj 1,4), 655 Tsd. (adj 1,8), 70 Tsd. (adj 0,35).

**Analyse:** Die konsistenteste KI-Architektur-Quelle im Datensatz: 8 von 9 Reels über dem Topic-Median, trotz 2M Followern ein Median-adj von 3,1. Pro Reel gibt es genau eine architektonische Idee (Pool über dem Abgrund, Villa unter Wasser, Haus als Objekt). Außenaufnahmen mit Wasser und Tropen, Golden Hour oder Tageslicht. Die Caption ist ein Titel mit 2–4 Wörtern plus Hashtags, ohne CTA. Die Reichweite wird durch Kollaborationen verstärkt: @ifonly.ai (Tiramisu-Haus, 136 Mio., [q06](quellen/q06_ai_theme_page_case_studies.md)) sowie Reposts mit Credit durch @thetrillionairelife und @shltr (`profile_sunt_mrr.json`; ob bezahlt, `[UNKNOWN]`).

**Monetarisierung:** Linktree mit „Shop All AI Courses“, „Get Premium Prompts“, Video-Tutorials und einem russischsprachigen Kurs `[VERIFIED]`. Die Shop-Domains waren beim Abruf nicht erreichbar, Produkte und Preise `[UNKNOWN]`. Collab-E-Mail in der Bio `[VERIFIED]`. Creator-Kollaborationen `[VERIFIED]`, ob bezahlt `[UNKNOWN]`. Ein Threads-Post zu einem Resort ohne Paid-Label: Sponsoring `[UNKNOWN]`.

**Lernen:** *Eine Idee pro Reel, eine feste Titel-Formel, Kollaborationen als Verbreitungskanal.* Offenlegung schließt Reichweite nicht aus. **Nicht kopieren:** den runden Pool über Reisterrassen, die Titel-Formel „Dream … villa“, ihre Bali-Ästhetik. Location-Captions sind segmentweit schwach (≈ 0,63, n = 161); Orte nur als Setting nutzen.

### 5.7 Rang 7 – @aiforarchitects (D, KI-Luxusvillen als Auftrags-Funnel)

**Daten:** 1M Follower · 513 Posts · 7 Reels · Median-vpf 2,0 · Median adj 1,3 · alle KI-codiert, 5 von 7 als KI gekennzeichnet.

**Reels im Sample:**
- [DHBihXfMPDA](https://www.instagram.com/reel/DHBihXfMPDA/) „Mansion in Dubai…“: 34,7 Mio. Views, adj 47,6. Schwarze auskragende Villa im Sonnenuntergang, Porsche. Rund 2,89 Mio. Likes ([q06](quellen/q06_ai_theme_page_case_studies.md)).
- DcRC92XMXh5: 2,4 Mio., adj 9,0. Berg-Anwesen aus der Luft, Tennessee.
- DRH0bWEDGpI: 2,0 Mio., adj 8,7. Dunkle Steinvilla in Los Angeles.
- Weitere: 2,9 Mio. (adj 1,0), 910 Tsd. (adj 0,6), 267 Tsd. (adj 1,0), 226 Tsd. (adj 1,3; Helikopter über Pool in Miami).

**Analyse:** KI-Villen in Prestige-Lagen (Dubai, LA, Miami) mit langen Captions in Architekten-Stimme. Wiederkehrende Statussymbole (Porsche, Helikopter). Der 34,7-Mio.-Hit ist ein Ausreißer (Spanne 154×); der Median-adj liegt nur bei 1,3. Die Reichweite ist also nicht verlässlich; der Auftrags-Funnel ist dagegen durchgängig sichtbar (ob er Aufträge bringt, ist `[UNKNOWN]`).

**Monetarisierung:** Website mit Architectural, Interior, Concept und Landscape Design sowie Consulting, Anfrageformular, Caption-CTA „For private commissions and inquiries“ `[VERIFIED]`. LinkedIn: gegründet 2023, 2–10 Mitarbeitende `[ESTIMATED]`. Preise und Auftragsvolumen `[UNKNOWN]`. Laut [q06](quellen/q06_ai_theme_page_case_studies.md) das deutlichste Beispiel für „KI-Visual → B2B-Auftrag“.

**Lernen:** *Studio-Stimme plus ein klarer Auftrags-CTA* sollen aus Reichweite Leads machen, auch ohne konstant hohe Views (Lead-Volumen `[UNKNOWN]`). **Nicht kopieren:** fiktive Villen mit echten Ortsnamen ohne Konzept-Hinweis („Mansion in Dubai“ ist Irreführungsrisiko, [q07](quellen/q07_legal_ai_risk.md)) und das Porsche-vor-Villa-Klischee.

### 5.8 Rang 8 – @soothenests (E, KI-Cozy-Rooms; Referenzfall mit Schwenk)

**Daten:** 2M Follower · 2.119 Posts · 4 Reels · Median-vpf 3,5 · Median adj 3,3 · alle KI, keine Offenlegung in den Interior-Captions · Qualitäts-Teilscore 0,27, Originalität 0,19 (Theme-Page).

**Reels im Sample:**
- [DBWhf0koR7_](https://www.instagram.com/reel/DBWhf0koR7_/): 45,1 Mio. Views (20.10.2024), adj 13,9. Glaswand-Lounge im dichten Wald mit Kamin. Rund 2,08 Mio. Likes ([q06](quellen/q06_ai_theme_page_case_studies.md)).
- DOvkVSNCDEW: 8,1 Mio. (09/2025), adj 3,8. Höhlen-Nische aus Putz bei Schneesturm.
- DDR89qOo08t: 5,8 Mio., adj 2,8. Rosa Glam-Lounge.
- C_P-6KmOGt9: 2,5 Mio., adj 0,77. Loft-Bett mit nächtlicher Skyline.

**Analyse:** Das Format der KI-Cozy-Welle 2024: ein Raum gegen das Wetter (Regen, Schnee, Feuer), Stimmungstitel (beobachtet: „Raindrops on My Window, Euphoria…“), 2–3 Hashtags, kein CTA. Alle Reels sind `stylized_dreamy`, also der schwächste Realismus-Typ bei KI (0,70, n = 305). Bis 09/2026 ist der Account auf Threads zu allgemeinen KI-Tool-Showcases umgeschwenkt; ein Dreamina-Partnerpost erreichte dort 460 Views ([q06](quellen/q06_ai_theme_page_case_studies.md)).

**Monetarisierung:** Tool-Partnerschaft Dreamina (#dreaminapartner) `[VERIFIED]`. Collab-Kontakt `[VERIFIED]`. Kommentar → DM-Funnel für kostenlose Prompts `[VERIFIED]`. Ein Produktlink per DM, Affiliate-Status `[UNKNOWN]`. Dieselbe Kontaktadresse wie bei @cozyzen.ai, also vermutlich ein Portfolio-Betreiber `[ESTIMATED, q06]`. Umsatz `[UNKNOWN]`.

**Lernen:** *Emotion vor Einrichtung:* Geborgenheit gegen Sturm war der emotionale Kern. Der Schwenk zeigt zugleich, dass der Betreiber die Interior-Nische allein offenbar nicht für tragfähig hält (Deutung von q06). **Nicht kopieren:** die Regen-Fenster-Schlafzimmer-Schablone. Sie ist gesättigt; KI-Schlafzimmer liegen bei 0,77 (n = 110), KI-Wohnzimmer bei 0,69 (n = 123).

### 5.9 Rang 9 – @neuraltransform (E, Garten- und Pool-Makeover)

**Daten:** 83K Follower · 97 Posts · 3 Reels · Median-vpf 19,3 · Median adj 1,8 · KI-codiert `[ESTIMATED]`, nicht offengelegt · ältestes gesehenes Reel 2026-02-27.

**Reels im Sample:**
- [DVRdL5wkkIK](https://www.instagram.com/reel/DVRdL5wkkIK/): 2,7 Mio. Views, adj 9,3. Extrem langer Infinity-Pool mit Feuerschalen über einem Wüstencanyon; Curiosity-Hook „They turned a desert hill into THIS?!“ (beobachtet).
- DV1gTOdk5nC: 1,6 Mio., adj 1,85. Gepflegte Staudenrabatte vor modernem Haus.
- DVgQrzKgpki: 163 Tsd., adj 0,47.

**Analyse:** Gesichtslose Außenraum-Transformationen mit Curiosity-Hook und CamelCase-Hashtags. Das spektakuläre Pool-Reel sticht heraus (adj 9,3); die realistischen Gartenbilder liegen deutlich darunter (adj 1,85 bzw. 0,47).

**Monetarisierung:** Linktree mit 12 Amazon-Affiliate-Links für Gartenprodukte (Solarleuchten, Pflanzkübel, Werkzeug, Rasenkanten) `[VERIFIED]`. Umsatz `[UNKNOWN]`. Die Ökonomie ist dünn: Amazon Home/Garden 3 %, 24-h-Cookie ([q02](quellen/q02_furniture_affiliate_commerce.md)).

**Lernen:** *Sichtbares Ergebnis plus günstige, kaufbare Kleinteile* ist eine natürliche Affiliate-Brücke für Outdoor-Content. **Nicht kopieren:** den „They turned X into THIS?!“-Wortlaut und KI-Makeovers ohne Kennzeichnung, die man für echte Renovierungen halten kann.

### 5.10 Rang 10 – @stylishnorrastudios (A, „Studio“-Persona mit KI-Look)

**Daten:** 40K Follower · 502 Posts · 2 Reels · Median-vpf 55,7 · Median adj 11,3 · 1 Reel KI, 1 unklar `[ESTIMATED]`, nicht offengelegt.

**Reels im Sample:**
- [DZ0TBEsOgkU](https://www.instagram.com/reel/DZ0TBEsOgkU/): 3,7 Mio. Views, vpf 92, adj 3,3. Doppelhoher Walnuss-Essraum mit Farn-Galerie und Blick auf Regenwald und Wasserfall.
- Da0tFqToXsM: 755 Tsd., adj 19,3. Schwarzes Industrial-Loft mit Galerie.

**Analyse:** Lange, polierte Architektur-Texte ohne Hashtags, die den Account als Studio rahmen, mit DM-CTA für „private project timelines“ (beobachtet). Beide Reels liegen über 5× Follower; der Verzicht auf Hashtags hat bei n = 2 nicht erkennbar geschadet (Reels ohne Hashtags liegen segmentweit bei 0,93, n = 423 mit Followerwert, also nahe der Erwartung).

**Monetarisierung:** Nur ein DM-Service-CTA `[VERIFIED]`. Link, Shop und Bio `[UNKNOWN]`.

**Lernen:** *Studio-Identität über Sprache*: Copywriting in Architektenton ist ein billiges Markensignal. **Nicht kopieren:** den Eindruck realer, buchbarer Bauprojekte, wenn die Bilder KI sind, und seinen Textstil.

### 5.11 Rang 11 – @watchthebuild (E, „leerer Raum → eingerichtet“)

**Daten:** 107K Follower · 128 Posts · 4 Reels · Median-vpf 4,7 · Median adj 2,3 · KI-codiert, 1 Reel offengelegt · Kandidat „neu & schnell“ (ältestes gesehenes Reel 2026-07-04) `[ESTIMATED]`.

**Reels im Sample:**
- [DbmsOfOywba](https://www.instagram.com/reel/DbmsOfOywba/) „THIS ROOM WAS COMPLETELY EMPTY… 🤯“ (beobachtet): 1,3 Mio. Views, adj 7,6. Organic-modern Wohnzimmer als Endzustand.
- Da2LadfSUXi: 529 Tsd., adj 2,5. Leeres Schlafzimmer → grünes Japandi.
- DacJhpkS_0q: 465 Tsd., adj 0,9.
- DaXROTBSfSt: 349 Tsd., adj 2,05. Skandinavisches Wohnzimmer mit Klavier.

**Analyse:** Kurze Transformationen mit realistischem, sehr kaufbarem Endzustand (alle Reels „shoppability high“), meist Tageslicht oder Golden Hour, rund 25 Hashtags. Auf Threads werden Räume als Follower-Wünsche gerahmt und Meinungsfragen gestellt. Bemerkenswert: Das Scandinavian-Reel (adj 2,05) und das stärkere Organic-Modern-Reel (adj 7,6; das zweite liegt bei 0,9) liegen *auf diesem Account* über der Erwartung, obwohl diese Stile bei KI segmentweit schwach sind (Scandinavian 0,28, n = 16; Organic Modern 0,57, n = 56). Das Format scheint hier stärker zu wirken als der Stil (Hypothese).

**Monetarisierung:** Nichts beobachtet (kein Link, Shop oder Affiliate) `[UNKNOWN]`.

**Lernen:** *Payoff durch Vorher/Nachher als Videoablauf*, nicht als Split-Cover (Split-Cover 0,56×, n = 22, n. s.). Ein kaufbarer Endzustand bereitet spätere Affiliate-Links vor. **Nicht kopieren:** die 10-Sekunden-Schablone 1:1 und die Behauptung „echte Follower-Anfrage“, wenn sie nicht stimmt.

### 5.12 Rang 12 – @syifa_in_switzerland (G, reale Reisebilder aus der Schweiz)

**Daten:** 3M Follower · 2.642 Posts · 3 Reels · Median-vpf 12,0 · Median adj 33,5 (2 Reels mit Followerwert) · reales Material.

**Reels im Sample:**
- [DSzbGfUjOwu](https://www.instagram.com/reel/DSzbGfUjOwu/): 71,8 Mio. Views, adj 66,9. Übersättigtes Postkartenbild eines Seedorfs unter Schneegipfeln.
- DNkc9c-sjx4: 6,6 Mio. (nicht codiert).
- DV8UUPMDOvJ: 217 Tsd., adj 0,20. Zug vor Dorf und Bergen.

**Analyse:** Kein Interior und keine KI. Der Account kam über Viralität, Wachstum und Reichweite in die Top 20. Die Caption ist nur Flagge plus Ortslabel. Relevant ist er als **Setting-Signal:** Schweiz liegt auf Reel-Ebene bei 1,84 (n = 16, nicht signifikant).

**Monetarisierung:** Linktree nur mit YouTube, Facebook, TikTok und einem Reiseblog; keine Affiliate-Links, keine Deals gesehen `[VERIFIED als Befund; Einnahmen UNKNOWN]`.

**Lernen:** *Sehnsuchtsort als Kulisse* (Alpensee, Dorf, Berge) für eigene Häuser, nicht als Hook-Text. **Nicht kopieren:** reale Reiseaufnahmen und die extreme Übersättigung.

### 5.13 Rang 13 – @siriorsinterior (A, Interior-Studio aus Indonesien)

**Daten:** 547K Follower · 2.727 Posts · 2 Reels · Median-vpf 3,8 · Median adj 9,1 · 3D-Renderings · Captions auf Indonesisch.

**Reels im Sample:**
- [DE7Rnh-vZQf](https://www.instagram.com/reel/DE7Rnh-vZQf/): 3,7 Mio. Views, adj 16,1. Helles Marmor-Schlafzimmer mit goldgefasster LED-Decke.
- DKMeZCuvoTU: 508 Tsd., adj 2,2. Modern-klassisches Schlafzimmer.

**Analyse:** Ein Studio im lokalen Markt mit polierten, aber generischen Luxus-Schlafzimmern. Die Reel-Captions enthalten Kommentar-Aufforderungen, einen Marken-Hashtag (#sibambointerior) und rund 29 lokale Hashtags; der Service-CTA stammt aus einem Threads-Post. Schlafzimmer funktionieren hier für ein reales Studio in seiner Sprache.

**Monetarisierung:** Design-Service-CTA („Hubungi Siriors…“) `[VERIFIED]`. Kein Link-in-Bio gefunden.

**Lernen (Hypothese):** *Sprach- und Marktnische* (lokale Sprache, lokales Studio) kann eigene Nachfrage erschließen; segmentweit sind indonesische Captions dafür kein Beleg (0,59, n = 11, geringe Konfidenz). **Nicht kopieren:** austauschbare Gold-Marmor-Schlafzimmer ohne eigene Idee.

### 5.14 Rang 14 – @nostalgicraindrops (E, Regen-Ambient als YouTube-Funnel)

**Daten:** 713K Follower · 151 Posts · 3 Reels · Median-vpf 5,5 · Median adj 1,9 · KI/VFX laut YouTube von einem Dritt-Artist · 2 Reels offengelegt.

**Reels im Sample:**
- [C7mtT4-yj7n](https://www.instagram.com/reel/C7mtT4-yj7n/): 14,1 Mio. Views, adj 21,1. Regenfenster zum Wald aus einem ungemachten Bett.
- DJmXw9og9Na: 3,9 Mio., adj 1,02.
- C__GsibSv6K: 1,1 Mio., adj 1,94.

**Analyse:** Ambient-Content mit Nutzenversprechen (Schlafen, Lernen) und Link-in-Bio-CTA in der ersten Zeile (beobachtet: „Sleep fast with my rain sleep video playlist in bio!“). Die Konversion zu YouTube ist schwach: 6,27K Abonnenten und 155.098 Aufrufe trotz eines 14-Mio.-Reels ([q06](quellen/q06_ai_theme_page_case_studies.md)).

**Monetarisierung:** Cross-Platform-Funnel zu YouTube und Business-E-Mail `[VERIFIED]`. YouTube laut NexLev nicht monetarisiert `[THIRD-PARTY ESTIMATE, geringe Konfidenz]`.

**Lernen:** *Ein klarer Nutzen* gibt einen Grund zum Folgen und Speichern. Funnels zu Long-Form konvertieren aber schwach; wenn überhaupt, erst später testen. **Nicht kopieren:** das Regen-Schlafzimmer und Anime-Referenzen (IP-Risiko).

### 5.15 Rang 15 – @zaxzaaafrica (A, Interior-Studio mit KI-Bädern)

**Daten:** 65K Follower · 763 Posts · 2 Reels · Median-vpf 10,0 · Median adj 2,1 · KI-codiert, nicht offengelegt · „ZA“-Wasserzeichen und Text auf den Covern.

**Reels im Sample:**
- [DZhV2noRxp1](https://www.instagram.com/reel/DZhV2noRxp1/): 977 Tsd. Views, adj 3,2. Freistehende Wanne unter einem riesigen leuchtenden Vollmond an einer Marmorwand; Fantasy-Hook „Escape to the stars…“ (beobachtet).
- DYndyxPB5gr: 323 Tsd., adj 1,06. Weißes Marmor-Spa-Bad, „Click the Link on my Bio“.

**Analyse:** Glänzende KI-Luxusbäder als Portfolio eines afrikanischen Design-, Build- und Möbel-Sourcing-Studios. Das surreale Element (Mond) hebt das eine Reel; das Standard-Spa-Bad bleibt bei der Erwartung. KI-Bäder liegen segmentweit bei 1,45 (n = 28).

**Monetarisierung:** Service-CTA für Anfragen und Buchungen `[VERIFIED]`. Möbel-Vorbestellung auf Threads (#preorder) `[VERIFIED]`. Linktree leer. Preise `[UNKNOWN]`.

**Lernen (Hypothese, n = 2):** *Ein surreales Element in einem sonst realistischen Raum* kann den Scroll-Stopp erzeugen. Das Bad eignet sich als Statement-Raum. **Nicht kopieren:** das Mond-Wannen-Motiv, große Wasserzeichen und Text auf dem Cover (q01: sichtbare Wasserzeichen kosten Reichweite, gemeint sind dort Dritt-Wasserzeichen).

### 5.16 Rang 16 – @siyad_abdali (E, die größten KI-Einzel-Hits im Datensatz)

**Daten:** 4M Follower · 2.110 Posts · 6 Reels · Median-vpf 1,1 · Median adj 5,7 · alle KI-codiert, keine Offenlegung.

**Reels im Sample:**
- [C_Pf1dboaeJ](https://www.instagram.com/reel/C_Pf1dboaeJ/): 282 Mio. Views (29.08.2024), adj 99,5. Loft-Schlafzimmer mit Lichterketten-Nestbett vor verregneter nächtlicher Skyline, ohne Caption.
- C9SiQc8S9xq: 109 Mio. (11.07.2024), adj 116,7. Weißes Glam-Penthouse, Schnee, Stadtlichter.
- DQostfIDLYr: 5,1 Mio. (11/2025), adj 8,3. Winterhütte.
- DQ_1nRPiIxg: 4,0 Mio., adj 3,1. Turm aus runden rosa Betten (fantasy).
- DHMBPpcpswh: 2,3 Mio., adj 0,41.
- DTvByw5kyek: 316 Tsd. (20.01.2026), adj 0,11.

**Analyse:** Maximal verträumte Räume bei Nachtlicht mit Wetter und Stadtlichtern; die beiden Mega-Hits haben keine Caption. Hit-getrieben wie kein anderer Top-20-Account (Spanne 892×) und mit einem Decay-Muster: vom 282-Mio.-Hit 2024 zum jüngsten Reel mit adj 0,11 (n = 6, also nur ein Hinweis). Ältere Reels hatten mehr Zeit; Views und Alter korrelieren im Datensatz aber nur schwach (ρ = 0,05).

**Monetarisierung:** Nichts beobachtet. Threads-Persona „Traveler, Horticulturist“ `[VERIFIED als Bio]`, Einnahmen `[UNKNOWN]`.

**Lernen (Hypothese):** *Neuheit nutzt sich ab.* Der „unmögliche Cozy-Moment“ war 2024 ein Peak; die jüngeren Reels des Accounts liegen unter der Erwartung. Das stützt als Hypothese unsere Novelty-Engine mit wechselnden Serien. **Nicht kopieren:** Lichterketten-Loftbetten, Etagenbett-Motive und Posts ohne Caption (keine Markenbildung).

### 5.17 Rang 17 – @diniz_nasaroba (E, KI-Garten-„Hacks“; nicht tief profiliert)

**Daten:** 293K Follower · 52 Posts (Reel-Embed) · 2 Reels (beide Ende März 2026) · Median-vpf 44,7 · Median adj 8,4 · beide KI-codiert · Bio und Monetarisierung `[UNKNOWN]` (nicht in der Competitor-DB).

**Reels im Sample:**
- [DWZGY4YjvrK](https://www.instagram.com/reel/DWZGY4YjvrK/): 25 Mio. Views, adj 16,0. Blumenbeet aus „ausgekipptem“ Terrakotta-Topf mit Kieselrand; Hook „Turn Your Yard Into a Paradise with This DIY Garden Hack!“ (beobachtet).
- DWgzHgYDpdN: 1,2 Mio., adj 0,84. Nächtliche Garten-Transformation mit Palme.

**Analyse:** KI-Bilder werden als nachbaubarer DIY-Hack gerahmt. Instruktionale Hooks sind segmentweit schwach (0,72, n = 74, n. s.), dieses Reel ist ein Ausreißer. KI-Gärten liegen segmentweit tendenziell über der Erwartung (1,61, n = 43; der Gruppenkontrast Outdoor/Bad vs. Standardräume ist post-hoc gebildet).

**Monetarisierung:** `[UNKNOWN]` (nicht profiliert).

**Lernen:** *Ein alltagsnahes Versprechen* („das kannst du auch“) macht Outdoor-Content teilbar. **Nicht kopieren:** KI-Ergebnisse als real nachbaubare Anleitung verkaufen (Irreführung, Enttäuschungsrisiko) und das Topf-Motiv.

### 5.18 Rang 18 – @roomify.design (E, „leerer Raum → Luxus“ mit Shop-DM)

**Daten:** 62K Follower · 152 Posts · 7 Reels · Median-vpf 5,4 · Median adj 1,8 · KI-codiert, nicht offengelegt.

**Reels im Sample:**
- [DVrk07ojSsm](https://www.instagram.com/reel/DVrk07ojSsm/): 1,7 Mio. Views, adj 12,0. Warm-neutrales Schlafzimmer mit Walnuss-Riffelwand, „Turning an empty room into…“ (beobachtet).
- DWSPe8LjTqx: 842 Tsd., adj 1,85. Küche, „…made the whole house feel expensive…“.
- DU_6TszDUU9: 337 Tsd., adj 14,7. Virtual Staging Wohnzimmer.
- DV3t286gJp6: 301 Tsd., adj 3,55.
- DXNO5bbDWVp: 353 Tsd., adj 0,57. Serien-Hook „Day 5 of styling the same house…“, Kommentar-Keyword; 1.991 Kommentare bei 3.738 Likes.
- DXCuw34jVm4: 62 Tsd., adj 0,33 (Preisangabe $5M).
- DXFzOSZiBeX: 55 Tsd., adj 0,56 (Kommentar-Keyword).

**Analyse:** Warm-neutrale, sehr kaufbare Räume in Golden Hour mit Serienrahmen („Day N“) und Kommentar → DM-Funnel. Die Keyword-Reels erzeugen viele Kommentare, aber wenig Views. Das passt zum Segment: Kommentar-Keyword-CTA ≈ 6,6× Kommentare pro View (0,00203 vs. 0,00031 ohne CTA), aber adj 0,86 (n = 145) gegenüber 0,98 (n = 1.273).

**Monetarisierung:** Kommentar-Keyword → DM mit „curated Wayfair collection + room links“ `[VERIFIED]`. Ob es Affiliate-Links sind: `[UNKNOWN]`. Wayfair zahlt laut Drittquelle bis 7 % bei 7 Tagen Cookie ([q02](quellen/q02_furniture_affiliate_commerce.md)) `[THIRD-PARTY ESTIMATE]`.

**Lernen:** *Commerce über Kommentar-Trigger als Zusatzformat*, nicht als Reichweitenformat. Serienrahmen schaffen Wiederkehr. **Nicht kopieren:** „Day N of styling…“ und den Keyword-Text wörtlich.

### 5.19 Rang 19 – @urban_lifestyle_lab (D, Future-Flex-Architektur)

**Daten:** 250K Follower · 4.660 Posts · 4 Reels · Median-vpf 4,2 · Median adj 4,7 · KI-codiert `[ESTIMATED]`, Captions beanspruchen „Concept & Copyright ©“.

**Reels im Sample:**
- [DTwE4CFjKFK](https://www.instagram.com/reel/DTwE4CFjKFK/): 3 Mio. Views, adj 5,8. Mega-Villa am Wasser; Status-Hook in Wechsel-Großschreibung (beobachtet).
- DVesrMZDNwx: 1,8 Mio., adj 10,9. Schwarze Marmor-Klippenvilla mit Helikopter und Jet (fantasy).
- DPZ9k9SjLjL: 320 Tsd., adj 3,6. Futuristische Klippenvilla, Supersportwagen-Garage unter dem Pool.
- DR-2WFuidU2: 13,6 Tsd., adj 0,06. Penthouse-Interior.

**Analyse:** Extreme Status-Fantasien in der Blue Hour mit provokanten Kurz-Hooks (Status, Contrarian). Die Außen-Fantasy-Reels tragen, das einzige Interior fällt durch. Die rechnerische Posting-Rate (91,9/Woche) ist unplausibel; der Account ist älter als das älteste gesehene Reel.

**Monetarisierung:** Nichts beobachtet; Bio `[UNKNOWN]`.

**Lernen:** *Konzept-Autorschaft sichtbar machen* („Concept by …“) passt zu Originalitätsregeln und zur Studio-Identität. **Nicht kopieren:** Meme-Schreibweise und Jet/Helikopter-Klischees.

### 5.20 Rang 20 – @montani3d (D, KI-Render-Lehre aus Brasilien)

**Daten:** 603K Follower · 1.578 Posts · 4 Reels · Median-vpf 1,1 · Median adj 1,0 · alle KI, offengelegt · Captions auf Portugiesisch.

**Reels im Sample:**
- [DUannSokdQD](https://www.instagram.com/reel/DUannSokdQD/): 946 Tsd. Views, adj 0,97. „Röntgen“-Explosionsansicht eines Hauses (Leitungen, Rohbau); „Comente WORKSHOP 👇“ (beobachtet); 10.387 Kommentare.
- DXwWo-7RwTl: 870 Tsd., adj 0,99. Paar mit Plan, holografische Pflanzen „wachsen“ im Garten.
- DULe4AKkfl7: 499 Tsd., adj 1,82. Grundstück mit 3D-Maßzahlen, Helikopter mit Banner „RENDER COM IA“; 9.025 Kommentare.
- DTsR_g4kfQj: 139 Tsd., adj 0,23. Ein Foto → viele Stilvarianten.

**Analyse:** Ein reiner Lern-Funnel. Die Kommentarquote ist extrem (Median 0,012 Kommentare pro View), die Views liegen genau bei der Erwartung. Menschen sind in 2 von 4 Reels zu sehen. Die Positionierung zielt klar auf Architekten und 3D-Artists (B2B).

**Monetarisierung:** Live-Workshop per Hotmart, „R$29,90“ (statt R$97), Replay „R$197“, Upsell „Formação Render.IA“ (Preis `[UNKNOWN]`) `[VERIFIED]`. Studio-Services, u. a. monatliche 3D-Retainer `[VERIFIED]`. Die Aussage „Renderaufträge bis R$ 80 mil“ ist eine Selbstauskunft `[THIRD-PARTY ESTIMATE]`.

**Lernen:** *Making-of als zweite Content-Ebene* („Wie ist das entstanden?“) lässt sich mit Kursen und Services verbinden, auch ohne Mega-Reichweite (Angebote belegt, Umsätze nicht). **Nicht kopieren:** Countdown- und Knappheits-Verkaufsmechanik sowie seine Röntgen-Haus-Visualisierung.

### 5.21 Relevante Accounts außerhalb der Top 20 (Watchlist)

| Account | Rang | Warum relevant | Kerndaten (Sample) |
|---|---:|---|---|
| @recastliving | 22 | KI-Transformation Garten → Lounge, **mit Menschen im Bild**, Blue Hour; SEO-Captions für Hausbesitzer, Architekten und Builder | 47K · 1,4 Mio. (adj 5,3) / 409 Tsd. (adj 1,2) |
| @abdullahaslanoglu_ | 25 | 3D-Villa „Modernism touched by light“, Lichtkanten-Fassade; kennzeichnet Eigenwerbung mit #reklam | 68K · 10,2 Mio. (adj 29,8) / 187 Tsd. |
| @elitebuildhq | 35 | Kandidat „neu & schnell“; Konzeptbauten (Living-Garden-Garage, Untergrund-Oase, Bunker) mit YouTube-artigen Titeln | 2M · 24 Mio. und 17,3 Mio. (04/2026); spätere Reels 138 Tsd. bis 4,9 Mio. |
| @ifonly.ai | – (n = 1) | Surreale „If only…“-Konzepte, KI offengelegt, Kooperation mit @artlist.io `[VERIFIED]` | 1M · 136 Mio. |
| @luxurydreamhub | 70 | **Decay-Fall:** 16 Reels; nach 8,2 Mio. (09/2025, adj 4,9) und 4 Mio. (02/2026) liegen die jüngsten Reels (03–05/2026) bei 51–133 Tsd. (adj 0,09–0,14); keine Monetarisierung sichtbar | 1M · Median adj 0,70 |
| @cozyzen.ai | 204 | **Decay-Fall:** 4,1 Mio. (2024, adj 3,7) → 27 Tsd. und 18 Tsd. (2026, adj 0,02–0,12), offengelegte KI | 498K |
| @ti.fu | – (n = 1) | Namentlicher KI-Architekt; belegtes Wachstum und Kurs-Monetarisierung (150 EUR, 100 Plätze) ([q06](quellen/q06_ai_theme_page_case_studies.md)) | 272K · 1,8 Mio. (2024, adj 5,6) |

---

## 6. Teil 20 (teilweise) – Monetarisierung pro Top-Account

Legende: ✔ = `[VERIFIED]` gesehen (Quelle: Profil-JSON) · – = nicht beobachtet (heißt nicht, dass es nicht existiert) · ? = Angebot gelistet, Details `[UNKNOWN]`. **Umsätze: bei allen 20 `[UNKNOWN]`.**

| Rang | Account | B2B-Service / Aufträge | Kurs, Prompts, Digital | KI-Tool-Partner / Referral | Produkt-Affiliate | Eigener Shop / Produkte | Cross-Platform-Funnel | Kontakt für Collabs / Anfragen |
|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | @myplants.uae | ✔ Landscaping, 2D/3D-Design | – | – | – | ✔ Pflanzen-Shop | – | ✔ WhatsApp / Formular |
| 2 | @archibible | ✔ Commissions | – | ✔ Luma AI | – | ? Etsy | – | ✔ E-Mail |
| 3 | @design_x_interior | ✔ (Caption-Framing) | – | – | – | – | – | – |
| 4 | @elarch.studio | ✔ Renderings ab US$200 | – | – | – | – | ✔ YouTube (klein) | ✔ WhatsApp |
| 5 | @georgios_tataridis | ✔ Interior + 3D weltweit | – | – | – | – | – | ✔ Formular, DM |
| 6 | @sunt_mrr | – | ✔ Kurse, Prompts, Tutorials (Shop beim Abruf nicht erreichbar) | – | – | – | – | ✔ E-Mail |
| 7 | @aiforarchitects | ✔ Architektur, Interior, Konzept | – | – | – | – | – | ✔ Website / WhatsApp |
| 8 | @soothenests | – | – (Prompts gratis per DM) | ✔ Dreamina | ? Produktlink per DM | – | – | ✔ E-Mail |
| 9 | @neuraltransform | – | – | – | ✔ Amazon (12 Links) | – | – | – |
| 10 | @stylishnorrastudios | ✔ DM für Projekte | – | – | – | – | – | ✔ DM |
| 11 | @watchthebuild | – | – | – | – | – | – | – |
| 12 | @syifa_in_switzerland | – | – | – | – | – | ✔ YouTube, Blog | – |
| 13 | @siriorsinterior | ✔ Design-Service | – | – | – | – | – | – |
| 14 | @nostalgicraindrops | – | – | – | – | – | ✔ YouTube-Playlist | ✔ E-Mail |
| 15 | @zaxzaaafrica | ✔ Design & Build | – | – | – | ✔ Möbel-Vorbestellung | – | ✔ Link (leer) |
| 16 | @siyad_abdali | – | – | – | – | – | – | – |
| 17 | @diniz_nasaroba | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 18 | @roomify.design | – | – | – | ✔ Wayfair-Links per DM (Provision ?) | – | – | – |
| 19 | @urban_lifestyle_lab | – | – | – | – | – | – | – |
| 20 | @montani3d | ✔ Studio-Retainer | ✔ Workshop R$29,90, Replay R$197 | – | – | – | – | ✔ WhatsApp |
| | **Summe** | **10** | **2** | **2** | **2** (+1 ?) | **2** (+1 ?) | **3** | **11** |

**Was daraus folgt** (Details und eigene Roadmap: `09_monetization.md`):
1. **B2B ist der häufigste sichtbare Geldweg** der interessantesten Accounts: Design-, Render- und Landscaping-Aufträge. KI-Visuals dienen als Portfolio und Lead-Magnet. Das stützt die Positionierung als *AI-Architektur-/Design-Studio* (Strategy Brief).
2. **Die einzigen sichtbaren Sponsoren sind KI-Tool-Firmen** (Dreamina, Luma-Referral; außerhalb der Top 20 Artlist bei @ifonly.ai). Das deckt sich mit [q03](quellen/q03_sponsors_brand_deals.md): Tool-Firmen sind die zahlungsbereitesten Sponsoren (z. B. Higgsfield Earn bis „$2,500 per video“, Affiliate bis 25 %) `[VERIFIED laut q03]`.
3. **Möbel- und Produkt-Affiliate ist selten und dünn:** Nur 2 der Top 20 nutzen es, beide über Link-Listen oder DM. Die Ökonomie laut [q02](quellen/q02_furniture_affiliate_commerce.md): Amazon Home 3 % mit 24-h-Cookie, Wayfair bis 7 % mit 7 Tagen `[THIRD-PARTY ESTIMATE]`.
4. **Drei KI-Accounts ohne Studio- oder Personenmarke** (@siyad_abdali, @urban_lifestyle_lab, @watchthebuild) zeigen **keine** sichtbare Monetarisierung, darunter der Account mit dem größten Einzel-Hit (282 Mio.). Reichweite allein ist kein Geschäftsmodell.
5. **Kurse und Lehre** finden sich nur bei Accounts mit Fachpublikum (@montani3d, @sunt_mrr, Tim Fu); bei Endkunden-Pages wurden keine bezahlten Kurse gesehen. Umsätze sind in keinem Fall belegt (bei @sunt_mrr war der Shop beim Abruf nicht erreichbar).

---

## 7. Account-übergreifende Muster

Alle Muster sind **Korrelationen im Topic-Sample** und werden als **Hypothesen** für die Testing-Matrix formuliert, nicht als Ursachen.

![Performance nach Realismus-Grad](charts/adj_by_realism.png)

| # | Muster | Evidenz (n, Signifikanz) | Hypothese für uns |
|---|---|---|---|
| 1 | **Identität schlägt Theme-Page** | Reel-Ebene: theme_page 0,74 (n = 503) vs. ai_creator 1,09 (n = 276), Kruskal-Wallis p < 0,001 (robust). Nur KI: 0,70 vs. 1,02, ≈ 0,68×, p < 0,001. Top 20: nur 2 (Reel-Codierung) bzw. 4 (Profil) reine Theme-Pages; 10 verkaufen Services. | Als benanntes Studio mit Konzept-Autorschaft auftreten („Concept by …“), nicht als Repost-Page |
| 2 | **Reichweite ist hit-getrieben** | Spanne bestes/schwächstes Reel im Sample: @siyad_abdali 892×, @elarch.studio 425×, @sunt_mrr 350×, @syifa_in_switzerland 331×, @urban_lifestyle_lab 221×, @aiforarchitects 154×. Nur 3 der 20 liegen unter 5×. | Nicht auf Einzel-Reels planen, sondern auf Serien, Volumen und die Winner-DB (15_kpi_framework.md) |
| 3 | **Decay bei KI-Cozy- und Dreamy-Interiors** | @siyad_abdali 282 Mio. (2024) → 316 Tsd. (2026, adj 0,11); @luxurydreamhub 8,2 Mio. (09/2025) → 51–133 Tsd. (03–05/2026); @cozyzen.ai 4,1 Mio. → 18–27 Tsd.; @soothenests schwenkt um. Alterseffekt möglich, aber Views vs. Alter nur ρ = 0,05. | Novelty-Engine: Serien mit Halbwertszeit, wöchentliche Rotation (17_competitor_monitor.md) |
| 4 | **Konzept und Außenraum vor Standardraum (bei KI)** | KI fantasy_impossible 2,27 (n = 53) vs. stylized_dreamy 0,70 (n = 305): 3,25×, p < 0,001. KI-Räume: Treppe/Halle 2,24 (n = 16), Garten 1,61 (n = 43), Bad 1,45 (n = 28), Pool 1,16 (n = 23) vs. Schlafzimmer 0,77 (n = 110), Wohnzimmer 0,69 (n = 123), Küche 0,67 (n = 31); Einzelräume mit kleinem n, Raum-Dimension insgesamt n. s.; Gruppenkontrast 2,07×, p < 0,001, **post-hoc gebildet**. Bei 9 der 20 Top-Accounts ist das beste Reel ein Außenraum (Fassade, Garten, Pool, Terrasse). | Kern: unmögliche Häuser und Außenräume; Schlafzimmer nur als Choice-Format |
| 5 | **Aber: Schlafzimmer-Hits existieren** | 6 der 20 besten Reels sind Schlafzimmer, getragen von Studios mit 3D-Qualität (@georgios_tataridis, @siriorsinterior), einem Budget-Hook (@design_x_interior), dem Cozy-Peak 2024 (@siyad_abdali), einem Nutzenversprechen (@nostalgicraindrops, Schlaf-Ambient) oder einer Transformation (@roomify.design). | Schlafzimmer nicht ausschließen, aber nur mit starkem Konzept oder Hook, nie als generischer KI-Look |
| 6 | **Nacht- und Kantenlicht** | Top-20-Reels: 57 % Nacht, Blue Hour oder Golden Hour (41 von 72) vs. 33 % im Gesamt-Sample; Tageslicht 15 % vs. 35 %. Segment: Nacht vs. Tag 1,21×, **n. s.** (p = 0,12). | Nachtlicht und Blue Hour als Signatur (Marken- und Testentscheidung, kein belegter Hebel) |
| 7 | **Cover ohne Text** | Top-20-Reels: 11 % mit Cover-Text (8 von 72) vs. 47 % im Gesamt-Sample (1.120 von 2.393). Segment: 0,92×, n. s.; innerhalb von Accounts 14 % Text-Cover in den Top 10 % vs. 27 % in der unteren Hälfte (−13 Pp., 25 Accounts, 172 Reels). Das Text-Cover-Reel von @elarch.studio lag bei adj 0,09. | Starkes Einzelmotiv als Cover, Text höchstens minimal |
| 8 | **Menschen fehlen fast überall** | Nur 5 von 72 Top-20-Reels zeigen Menschen. Bei KI: mit Personen 1,34 vs. ohne 0,80, ≈ 1,68×, p ≈ 0,02 (n = 106 vs. 580), nur nominal signifikant (95-%-KI 0,99–2,52). | Kleine Figuren und Silhouetten für Maßstab: eine Lücke, die die Top-Accounts offenlassen |
| 9 | **Captions: Titel statt CTA** | 41 von 72 Top-20-Captions sind beschreibende oder aspirative Titel, 36 ohne CTA. Kommentar-Keyword-CTA: ≈ 6,6× Kommentare/View, aber adj 0,86 (n = 145). Choice-Hook: 5,67× Kommentare/View, p < 0,001 (n = 39); Views-Effekt 1,65×, **nicht belastbar** (p = 0,05). Kein Top-20-Reel ist als Choice-Hook codiert; nur eines deutet ihn an (@sunt_mrr, Cover „Plan A“). | Serien-Titel als Standard; Choice (P2 „Pick One“) für Kommentare; Keyword-CTA nur in Commerce-Reels |
| 10 | **KI-Offenlegung und Reichweite schließen sich nicht aus** | 23 von 72 Top-20-Reels sind offengelegt. @sunt_mrr: 7 von 9 offengelegt, Median adj 3,1; @myplants.uae: 2 von 2, adj 19,8. Segment (nur KI-Reels): offengelegt 0,73 vs. 0,89, ≈ 0,82×, **n. s.** (p = 0,15). Über alle Reels 0,69 vs. 0,98, nur nominal signifikant (Kruskal-Wallis p ≈ 0,006, nicht Bonferroni-robust). | Offen kennzeichnen (Pflicht, [q07](quellen/q07_legal_ai_risk.md)), markenkonform formulieren |
| 11 | **Motive werden schnell kopiert** | Dasselbe Schlangen-Hochhaus bei @visionbuildofficial und @facade_designn ([q05](quellen/q05_competitor_lists.md)); runde Infinity-Pools und Regenfenster-Schlafzimmer bei mehreren Accounts. | Eigene Motiv-Bibliothek und Ähnlichkeitsprüfung vor dem Posten (16_automation_strategy.md, Abschnitt 4.4) |
| 12 | **Frequenz** | Plausible Obergrenzen der Top 20: Median 8,0 Posts/Woche (1,2–19,6; n = 12). | 3 Reels/Tag (21/Woche) liegen am oberen Rand der Top-Accounts; als 30-Tage-Test vertretbar, danach die Rate an der Qualität ausrichten |
| 13 | **B2B-Funnel häufiger sichtbar als Long-Form-Funnel** | 10 der 20 verkaufen Services. Funnels zu YouTube konvertieren schwach: @drcozyvibes 1,13K Abonnenten trotz 155-Mio.-Reel, @nostalgicraindrops 6,27K ([q06](quellen/q06_ai_theme_page_case_studies.md)). | Früh ein Anfrage-Angebot (Konzeptvisualisierung) statt Long-Form-Funnel |

**Beobachtete Hook-Prinzipien → eigene Formulierungen** (neu formuliert, keine Übernahme):

| Prinzip | Beobachtet bei | Eigene Formulierung (EN) |
|---|---|---|
| Machbarkeit plus KI-Ehrlichkeit | @myplants.uae | "AI concept. Real materials. Could it be built?" |
| Werktitel als Serie | @archibible, @sunt_mrr | "Unbuilt No. 017 – The House Under the Falls" |
| Preis-/Wert-Spannung | @design_x_interior | "Guess the build cost before the last frame." |
| Transformation als Payoff | @watchthebuild, @neuraltransform | "Bare slope at dusk. Watch what grows here." |
| Designer-Meinung | @georgios_tataridis | "I'd remove one thing from this room. Which one?" |
| Autorschaft | @urban_lifestyle_lab | "Concept by [Studio]. Not for sale – yet." |
| Choice | Segment-Befund (5,67× Kommentare) | "Three stairs, one house. Pick 1, 2 or 3." |

Weitere Hooks: `07_hooks.md`.

---

## 8. Entscheidungsregeln aus der Wettbewerbsanalyse

| Frage | Regel | Begründung (oben) |
|---|---|---|
| Wie treten wir auf? | Als benanntes KI-Architektur- und Design-Studio mit Konzept-Credit, nie als Repost-Page | Muster 1, Abschnitt 6 |
| Was posten wir im Kern? | Unmögliche Häuser, Außenräume (Garten, Pool, Terrasse), Treppen und Hallen, Bäder als Statement | Muster 4, @sunt_mrr, @archibible, @myplants.uae |
| Was meiden wir? | Generische dreamy KI-Schlafzimmer, Wohnzimmer und Küchen; Regenfenster-Schablonen; Supersportwagen- und Jet-Klischees | Muster 3–5, @soothenests, @siyad_abdali |
| Wie bauen wir Hooks? | Ein Konzept pro Reel, Serien-Titel, Choice für Kommentare, Preis-Spannung nur mit „concept“-Hinweis | Muster 9, @design_x_interior |
| Wie sieht das Cover aus? | Ein starkes Einzelmotiv, Nacht oder Blue Hour, kein Text-Overlay, kein Split-Screen, kleine Figur für Maßstab | Muster 6–8 |
| Wie verdienen wir zuerst? | B2B-Konzeptvisualisierung und KI-Tool-Partnerschaften; Möbel-Affiliate erst mit P2/P3-Reels per DM | Abschnitt 6 |
| Was ist tabu? | KI als reales Projekt, reale Adresse oder nachbaubarer Hack ausgeben; fiktive Preis- und Ortsangaben ohne Konzept-Hinweis; fremde Motive oder Hook-Schablonen wörtlich übernehmen | @design_x_interior, @diniz_nasaroba, @aiforarchitects; [q07](quellen/q07_legal_ai_risk.md), [q01](quellen/q01_instagram_platform_rules.md) |
| Wen beobachten wir? | Top 20 plus Watchlist 5.21; Decay-Fälle als Frühwarnung | 17_competitor_monitor.md |

---

## 9. Limitationen

1. **WebSearch-Budget erschöpft (200/200).** Instagram-Suchsnippets, Paid-Partnership-Suchen und Storefront-Suchen konnten für die Tiefenprofile nicht laufen. Instagram-Bios sind daher meist `[UNKNOWN]`; genannte Bios stammen von Threads, Linktree, YouTube oder Websites. Instagram selbst wurde für die Profile nicht abgerufen (HTTP 429 bei früheren Versuchen, [q05](quellen/q05_competitor_lists.md), [q06](quellen/q06_ai_theme_page_case_studies.md)).
2. **Keine „letzten 20 Reels“ pro Account.** Ohne Login ist die Reel-Liste eines Profils nicht zugänglich. Wir nutzen die Reels, die auf Topic-Seiten erscheinen: 165 der 261 Kandidaten haben genau 2 Reels, nur 10 haben ≥ 7. Account-Kennzahlen sind deshalb Stichproben der *besten* Reels und nach oben verzerrt.
3. **Posting-Frequenz = Obergrenze.** Berechnet als Posts ÷ Tage seit dem ältesten *gesehenen* Reel. Ist der Account älter, liegt die echte Frequenz niedriger. Werte über 21/Woche sind markiert (†).
4. **Account-Alter = Untergrenze.** „Neu & schnell“ ist daher nur eine Kandidatenliste. Umbenannte oder übernommene Accounts sind nicht erkennbar.
5. **Follower beim Abruf, nicht beim Posten.** vpf unterschätzt die damalige Überperformance von Accounts, die durch den Hit gewachsen sind. Follower-Werte ≥ 1M sind von Instagram auf ganze Millionen gerundet (z. B. „2M“).
6. **KI-Codierung ist geschätzt.** Produktion, Stil und Raum stammen aus KI-gestützter Cover- und Caption-Codierung (κ 0,63–1,0). Bei Accounts ohne Offenlegung bleibt „KI“ eine Einschätzung (z. B. @stylishnorrastudios, @design_x_interior).
7. **Monetarisierung:** Nicht beobachtet heißt nicht, dass es sie nicht gibt. Umsätze sind für keinen Account belegt. Paid-Partnership-Labels konnten ohne Suche nicht systematisch geprüft werden.
8. **Gruppenzuordnung A–H ist redaktionell** (Abschnitt 2.1) und weicht bei einzelnen Handles von q05 ab. Die q05-Gruppengrößen stammen aus Drittanbieter-Listen mit unklarer Kategorisierung.
9. **Score-Verzerrungen:** Tiefprofilierte Accounts sind bei der Monetarisierbarkeit im Vorteil (19 der Top 20 sind profiliert, aber nur 66 der 261 Kandidaten). KI-Eignung bevorzugt KI und 3D bewusst.
10. **Keine Kausalität.** Alle Muster sind Korrelationen unter Reels, die es auf Topic-Seiten geschafft haben. Über Formate entscheiden erst eigene Tests (13_testing_matrix.csv, 15_kpi_framework.md).

---

## Anhang A – Alle 111 DB-Accounts nach Gruppe

Format: @handle (Follower · bestes Reel im Sample). „?“ = Follower oder Views `[UNKNOWN]`. Rohdaten mit Status je Feld: [02_competitor_database.csv](02_competitor_database.csv).

| Gruppe | Accounts |
|---|---|
| **A** (31) | @paulmarkkitchens (304K · 135 Mio.), @kellmarcel (126K · 74,9 Mio.), @interiorbyuma22 (295K · 55,5 Mio.), @longingtocomehome (130K · 36 Mio.), @design_x_interior (88K · 17,4 Mio.), @myplants.uae (123K · 15,6 Mio.), @elarch.studio (540K · 15,5 Mio.), @homeofmerve (459K · 13,1 Mio.), @abdullahaslanoglu_ (68K · 10,2 Mio.), @luxuriatetouche (4M · 9,7 Mio.), @ell.glamhome (1M · 8,2 Mio.), @eloisepreen (? · 7,6 Mio.), @divaa.finds (764K · 5,8 Mio.), @georgios_tataridis (321K · 4,5 Mio.), @siriorsinterior (547K · 3,7 Mio.), @stylishnorrastudios (40K · 3,7 Mio.), @em_henderson (1M · 3,6 Mio.), @styltechinterior_official (201K · 3,6 Mio.), @arteo_luxury (871K · 3,5 Mio.), @roxy_carretero (54K · 2,8 Mio.), @vrishtidesigns (2M · 2,2 Mio.), @olena_prykhodko_design (308K · 1,7 Mio.), @ibuilddevelopers (601K · 1,3 Mio.), @idw.design (318K · 1 Mio.), @zaxzaaafrica (65K · 977 Tsd.), @ihsansamhoun.interiors (169K · 885 Tsd.), @vishnu_xo (406K · 752 Tsd.), @2pdesigners (134K · 711 Tsd.), @_vlasov_roman_ (553K · 638 Tsd.), @luxhilspace (71K · 394 Tsd.), @deirdres_design (1M · 72 Tsd.) |
| **B** (8) | @alshifarealtor.dxb (47K · 54,3 Mio.), @gautamsinghania99 (12M · 48,7 Mio.), @wayup_media (942K · 22,7 Mio.), @theluxuryhomeshow (2M · 5,8 Mio.), @thehouserealty (265K · 2,9 Mio.), @glashaus.realestate (296K · 1,5 Mio.), @nestseekersdubai (189K · 604 Tsd.), @realtordenisbibik (91K · 548 Tsd.) |
| **C** (3) | @architectanddesign (8,4M · 55,2 Mio.), @hafezi.architects (606K · 4,3 Mio.), @abeastinside (182K · 1,6 Mio.) |
| **D** (20) | @ifonly.ai (1M · 136 Mio.), @sandiwara_multiverse.99 (402K · 85,2 Mio.), @aiforarchitects (1M · 34,7 Mio.), @sunt_mrr (2M · 24,5 Mio.), @elitebuildhq (2M · 24 Mio.), @archibible (220K · 14,3 Mio.), @visionbuildofficial (50K · 6,6 Mio.), @urban_lifestyle_lab (250K · 3 Mio.), @miladeshtiyaghi (642K · 2,1 Mio.), @facade_designn (47K · 2,1 Mio.), @ti.fu (272K · 1,8 Mio.), @architectcha (148K · 978 Tsd.), @montani3d (603K · 946 Tsd.), @luxquisit (190K · 912 Tsd.), @harmosai (57K · 752 Tsd.), @digitaldesign.lab (164K · 731 Tsd.), @insmultiverse (79K · 604 Tsd.), @rendair.ai (189K · 556 Tsd.), @vkuoo (92K · 552 Tsd.), @ai.perfect.world (14K · 13,6 Tsd.) |
| **E** (21) | @siyad_abdali (4M · 282 Mio.), @drcozyvibes (584K · 155 Mio.), @cairo_ia (944K · 81,1 Mio.), @soothenests (2M · 45,1 Mio.), @kohlectcabins (434K laut Reel-Embed · 23,8 Mio.; Decay-Fall: 23,8 Mio. 2024 vs. 70,6 Tsd. 2026), @nostalgicraindrops (713K · 14,1 Mio.), @calm_neststudio (156K · 13,1 Mio.), @ai.design.ideas (136K · 11,3 Mio.), @ayeshadeary5 (16K · 4,4 Mio.), @cozyzen.ai (498K · 4,1 Mio.), @neuraltransform (83K · 2,7 Mio.), @roomify.design (62K · 1,7 Mio.), @recastliving (47K · 1,4 Mio.), @naturesms (10M · 1,3 Mio.), @watchthebuild (107K · 1,3 Mio.), @fromrawto_real (40K · 1 Mio.), @imaginativemike (506K · 931 Tsd.), @jareef__saifi (339K · 547 Tsd.), @cabinstillwoods (18K · 403 Tsd.), @nesthome.03 (39K · 352 Tsd.), @interior_home_design1 (688K · 72 Tsd.) |
| **F** (6) | @manhwa_diablo (331K · 78,4 Mio.), @diycraftstvofficial (6M · 17,6 Mio.), @luxurydreamhub (1M · 8,2 Mio.), @luxuryhouseview (389K · 4,7 Mio.), @exploringdreamhomes (177K · 996 Tsd.), @yourfantasyhomes (23K · 313 Tsd.) |
| **G** (16) | @clarazrd (297K · 72,1 Mio.), @syifa_in_switzerland (3M · 71,8 Mio.), @travelwithjaro (1M · 66,5 Mio.), @timelessdiaries (65K · 60,7 Mio.), @swissaround (3M · 49,2 Mio.), @juliagal_ (4M · 13,6 Mio.), @nouxri (120K · 7,5 Mio.), @starlight_retreats (? · 5,4 Mio.), @beautifulhotels (6M · 5,4 Mio.), @beautifuldestinations (24M · 5,3 Mio.), @uniqchalets (684K · 5 Mio.), @aureliestory (3M · 4,9 Mio.), @lawrencewalton_ (547K · 4,5 Mio.), @travelask.world (681K · 2,7 Mio.), @thetrillionairelife (13M · 1,4 Mio.), @vacations (7M · 706 Tsd.) |
| **Sonstige** (6) | @ai.poly_ (14K · 147 Mio.), @polliviva (48K · 97,2 Mio.), @shellychicboutique (? · 77,2 Mio.), @natural_._scenery (? · 74,1 Mio.), @earthfm_net (757K · 58,5 Mio.), @karissa.brighton (? · 37,7 Mio.) |

---

## Quellen und Dateien

- Daten: [02_competitor_database.csv](02_competitor_database.csv), [04_reel_database.csv](04_reel_database.csv), [data/processed/shortlist_scores.csv](data/processed/shortlist_scores.csv), [data/processed/accounts_metrics.csv](data/processed/accounts_metrics.csv), `data/raw/accounts/profile_*.json`
- Statistik: [data/processed/analysis_digest.md](data/processed/analysis_digest.md) (Abschnitte 1, 3 „Account type“ / „Account size“, 8 „Accounts“, 10), `data/processed/stats/seg_account_kind_hint.csv`, `seg_follower_bucket.csv`, `seg_cta_type.csv`, `seg_caption_hook_category.csv`, `seg_location_any.csv`, `key_contrasts.csv`
- Skript: [scripts/shortlist.py](scripts/shortlist.py)
- Recherche-Notizen: [q01](quellen/q01_instagram_platform_rules.md) (Originalität, Wasserzeichen, KI-Label), [q02](quellen/q02_furniture_affiliate_commerce.md) (Affiliate-Konditionen), [q03](quellen/q03_sponsors_brand_deals.md) (KI-Tool-Sponsoren), [q05](quellen/q05_competitor_lists.md) (Landkarte A–H), [q06](quellen/q06_ai_theme_page_case_studies.md) (Fallstudien, Decay, Monetarisierung), [q07](quellen/q07_legal_ai_risk.md) (Irreführung, Kennzeichnung)
- Grafiken: [charts/adj_by_account_type.png](charts/adj_by_account_type.png), [charts/vpf_by_account.png](charts/vpf_by_account.png), [charts/adj_by_realism.png](charts/adj_by_realism.png)
