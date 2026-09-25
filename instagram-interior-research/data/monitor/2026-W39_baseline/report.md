# Wettbewerber- und Trend-Monitor 2026-W39 (data/raw)

Automatisch erzeugt von `scripts/monitor/monitor_weekly.py` am 2026-09-25 17:18 UTC. Nur öffentliche Daten, keine Kausalaussagen. Methodik und Grenzen: `17_competitor_monitor.md`.

## 0. Datenbasis

| Kennzahl | Diese Woche | Vorwoche / Vergleich |
|---|---|---|
| Rohdatenordner | `data/raw` | keiner |
| Abrufdatum / Laufzeit | 2026-09-25 | – |
| Topic-Seiten ok / angefragt (eindeutige Slugs) | 239 / 250 | – |
| Ausgewertete Topics | 57 | – |
| Eindeutige Reels / davon Top-Quartil | 616 / 204 | – |
| Neue Reels (veröffentlicht nach Stichtag) | 1 (Stichtag 2026-09-18 00:00 UTC, 7 Tage vor Abruf) |  |
| Reels mit Followerzahl (vpf/Tier möglich) | 588 (95 %) |  |
| Reels mit Codebuch-Codierung | 592 (Hook-Quelle: Codebuch-Codierung (Abdeckung 96 %, Rest Heuristik)) |  |
| Watchlist-Accounts mit Embed-Daten | 40 / 40 |  |
| Metrik je Topic-Seite | views: 239 |  |

**Lesehilfe:** topic_index 1,0 = typisch für die Topic-Seite; Top-Quartil = Reel liegt auf mindestens einer seiner Topic-Seiten im oberen Viertel (topic_pct ≥ 0,75; wer auf mehreren Seiten steht, hat mehr Chancen, daher > 25 %). Raum, Stil und Setting stammen aus Keyword-Regeln auf Caption + Topic-Slug, damit jede Woche identisch gemessen wird; Hook-Quelle: Codebuch-Codierung (Abdeckung 96 %, Rest Heuristik). Genauigkeit der Regeln: Abschnitt 8. Topic-Seiten zeigen nur ~12 Top-Reels: Wir sehen Gewinner, keine Flops (Survivorship).

## 1. Alerts

- **P3 · hook_compare** – Hook-Typ **promotional** liegt diese Woche vor **pov**: Median topic_index 1,78 vs. 0,31 (n = 28 / 12; Mann-Whitney p = 0,001, BH-q = 0,071 über 55 Paare; Hook-Quelle: Codebuch-Codierung (Abdeckung 96 %, Rest Heuristik)). Korrelation, kein Test.

## 2. Neue Reels auf den Topic-Seiten (nach topic_index)

| Reel | Handle | Topic(s) | Views | topic_index | Follower | vpf | Tier | Alter (T) | Hook | Stil × Raum | Erste Zeile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Ddde8wrqc6o](https://www.instagram.com/reel/Ddde8wrqc6o/) | @dreamlandsymphony | waterfall-house | 380 | 0,00 | 4.000 | 0,1 | NORMAL | 5,7 | aspirational | other × whole_home | Imagine waking up to this every single morning… 🌿💧🏡 A hidden home surr |

## 3. Ausreißer der Woche (alle Reels, vpf-Tier VIRAL/EXTREME)

Tier-Verteilung (Reels mit Followerzahl): NORMAL 140, GOOD 110, VERY_GOOD 98, VIRAL 110, EXTREME_OUTLIER 126

| Reel | Handle | Views | Follower | vpf | topic_index | neu? | Veröffentlicht | Likes/View | Hook | Stil × Raum |
|---|---|---|---|---|---|---|---|---|---|---|
| [DYNqA2ARGzy](https://www.instagram.com/reel/DYNqA2ARGzy/) | @aktraveltwo | 246 Tsd. | 366 | 672,1 | 1,03 |  | 2026-05-11 | 0,043 | descriptive | tropical × whole_home |
| [DZqhf_pAUW6](https://www.instagram.com/reel/DZqhf_pAUW6/) | @relaxationreflections_ | 6,0 Mio. | 12 Tsd. | 500,0 | 10,69 |  | 2026-06-16 | 0,037 | question | cozy_rustic × other |
| [DV1TGjKguzz](https://www.instagram.com/reel/DV1TGjKguzz/) | @processlabstudio | 4,6 Mio. | 10 Tsd. | 460,0 | 4,15 |  | 2026-03-13 | 0,049 | curiosity | modern_luxury × bathroom |
| [DXUIBEajIwd](https://www.instagram.com/reel/DXUIBEajIwd/) | @architectkhyatisaini | 5,0 Mio. | 11 Tsd. | 454,5 | 2,17 |  | 2026-04-19 | 0,078 | aspirational | modern_luxury × whole_home |
| [DcWTQ_jiSCi](https://www.instagram.com/reel/DcWTQ_jiSCi/) | @husnain_g13_properties | 1,7 Mio. | 4.000 | 425,0 | 2,38 |  | 2026-08-22 | 0,059 | descriptive | modern_luxury × kitchen |
| [DXFgq7hpmOu](https://www.instagram.com/reel/DXFgq7hpmOu/) | @05kai_562 | 3,3 Mio. | 8.000 | 412,5 | 1,12 |  | 2026-04-13 | 0,010 | curiosity | modern_luxury × whole_home |
| [CwTBiWeK6uY](https://www.instagram.com/reel/CwTBiWeK6uY/) | @ki.render | 7,3 Mio. | 19 Tsd. | 384,2 | 4,25 |  | 2023-08-23 | 0,099 | descriptive | other × kitchen |
| [DXRMLZVjWUC](https://www.instagram.com/reel/DXRMLZVjWUC/) | @hm_architecture078 | 3,9 Mio. | 11 Tsd. | 354,5 | 1,70 |  | 2026-04-18 | 0,015 | descriptive | modern_luxury × whole_home |
| [DSGQeRiEvi1](https://www.instagram.com/reel/DSGQeRiEvi1/) | @philkeandesigngroup | 3,7 Mio. | 11 Tsd. | 336,4 | 5,23 |  | 2025-12-10 | 0,038 | aspirational | modern_luxury × closet |
| [DPik9aHAdpr](https://www.instagram.com/reel/DPik9aHAdpr/) | @arunashokanphotography | 6,1 Mio. | 19 Tsd. | 321,1 | 49,39 |  | 2025-10-08 | 0,099 | descriptive | biophilic × bedroom |
| [C-APLc-yI85](https://www.instagram.com/reel/C-APLc-yI85/) | @ayeshadeary5 | 4,4 Mio. | 16 Tsd. | 275,0 | 6,68 |  | 2024-07-29 | 0,064 | choice | other × bedroom |
| [DW3n03NCOri](https://www.instagram.com/reel/DW3n03NCOri/) | @proud_and_property | 13,5 Mio. | 50 Tsd. | 270,0 | 5,87 |  | 2026-04-08 | 0,059 | promotional | classical × whole_home |
| [C87NQHRtm6B](https://www.instagram.com/reel/C87NQHRtm6B/) | @drcozyvibes | 155,0 Mio. | 584 Tsd. | 265,4 | 40,26 |  | 2024-07-02 | 0,039 | descriptive | cozy_rustic × bedroom |
| [DVf3hz8k2lW](https://www.instagram.com/reel/DVf3hz8k2lW/) | @midnight_files_ll | 2,0 Mio. | 8.000 | 250,0 | 1,80 |  | 2026-03-05 | 0,045 | curiosity | other × whole_home |
| [DMYHlSWuqZK](https://www.instagram.com/reel/DMYHlSWuqZK/) | @clarazrd | 72,1 Mio. | 297 Tsd. | 242,8 | 48,07 |  | 2025-07-21 | 0,126 | promotional | modern_luxury × whole_home |
| [DUVBmy5DcTo](https://www.instagram.com/reel/DUVBmy5DcTo/) | @architecturaai_ | 5,4 Mio. | 23 Tsd. | 237,9 | 5,48 |  | 2026-02-04 | 0,008 | promotional | other × whole_home |
| [Da_rdPUj1jN](https://www.instagram.com/reel/Da_rdPUj1jN/) | @sandiwara_multiverse.99 | 85,2 Mio. | 402 Tsd. | 211,9 | 32,15 |  | 2026-07-20 | 0,023 | descriptive | tropical × whole_home |
| [C6rOLbLriyx](https://www.instagram.com/reel/C6rOLbLriyx/) | @iz__designs | 21,9 Mio. | 109 Tsd. | 200,9 | 12,74 |  | 2024-05-07 | 0,034 | descriptive | other × living_room |
| [DSkb82VjPBD](https://www.instagram.com/reel/DSkb82VjPBD/) | @_crystalvisual | 1,8 Mio. | 10 Tsd. | 180,0 | 1,61 |  | 2025-12-22 | – | choice | cozy_rustic × bedroom |
| [CyGpI71u_QA](https://www.instagram.com/reel/CyGpI71u_QA/) | @jiqbalrealtor | 19,5 Mio. | 110 Tsd. | 177,3 | 13,00 |  | 2023-10-07 | 0,047 | aspirational | modern_luxury × whole_home |

## 4. Segment-Anteile im Top-Quartil

Kein Vorwochenordner → nur Anteile dieser Woche (Lift = Anteil im Top-Quartil ÷ Anteil an allen Reels).

| Dimension | Wert | TQ jetzt | Anteil TQ jetzt | Anteil alle | Lift | Anteil TQ Vorwoche | Δ pp | p | q (BH) | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Topic-Gruppe | luxury_room | 28/204 | 13,7 % | 14,0 % | 0,98 | – | – | – | – |  |
| Topic-Gruppe | unusual_home | 26/204 | 12,7 % | 12,3 % | 1,03 | – | – | – | – |  |
| Topic-Gruppe | ai | 23/204 | 11,3 % | 10,9 % | 1,04 | – | – | – | – |  |
| Topic-Gruppe | style | 20/204 | 9,8 % | 9,6 % | 1,02 | – | – | – | – |  |
| Topic-Gruppe | luxury_home | 20/204 | 9,8 % | 9,4 % | 1,04 | – | – | – | – |  |
| Topic-Gruppe | future_arch | 20/204 | 9,8 % | 9,6 % | 1,02 | – | – | – | – |  |
| Raum (Keyword) | whole_home | 112/204 | 54,9 % | 53,9 % | 1,02 | – | – | – | – |  |
| Raum (Keyword) | bedroom | 27/204 | 13,2 % | 13,1 % | 1,01 | – | – | – | – |  |
| Raum (Keyword) | pool | 13/204 | 6,4 % | 5,7 % | 1,12 | – | – | – | – |  |
| Raum (Keyword) | living_room | 10/204 | 4,9 % | 5,0 % | 0,97 | – | – | – | – |  |
| Raum (Keyword) | bathroom | 8/204 | 3,9 % | 4,7 % | 0,83 | – | – | – | – |  |
| Raum (Keyword) | kitchen | 5/204 | 2,5 % | 2,1 % | 1,16 | – | – | – | – |  |
| Stil (Keyword) | modern_luxury | 54/204 | 26,5 % | 26,6 % | 0,99 | – | – | – | – |  |
| Stil (Keyword) | cozy_rustic | 32/204 | 15,7 % | 15,6 % | 1,01 | – | – | – | – |  |
| Stil (Keyword) | futuristic | 25/204 | 12,3 % | 10,7 % | 1,14 | – | – | – | – |  |
| Stil (Keyword) | tropical | 12/204 | 5,9 % | 5,4 % | 1,10 | – | – | – | – |  |
| Stil (Keyword) | biophilic | 7/204 | 3,4 % | 3,6 % | 0,96 | – | – | – | – |  |
| Setting (Keyword) | mountain_snow | 14/204 | 6,9 % | 6,8 % | 1,01 | – | – | – | – |  |
| Setting (Keyword) | rain | 12/204 | 5,9 % | 5,2 % | 1,13 | – | – | – | – |  |
| Setting (Keyword) | forest | 10/204 | 4,9 % | 5,2 % | 0,94 | – | – | – | – |  |
| Setting (Keyword) | desert | 7/204 | 3,4 % | 2,4 % | 1,41 | – | – | – | – |  |
| Setting (Keyword) | lake_river | 5/204 | 2,5 % | 2,6 % | 0,94 | – | – | – | – |  |
| Stil × Raum (Keyword) | modern_luxury × whole_home | 27/204 | 13,2 % | 11,7 % | 1,13 | – | – | – | – |  |
| Stil × Raum (Keyword) | futuristic × whole_home | 19/204 | 9,3 % | 8,4 % | 1,10 | – | – | – | – |  |
| Stil × Raum (Keyword) | cozy_rustic × whole_home | 15/204 | 7,4 % | 7,3 % | 1,01 | – | – | – | – |  |
| Stil × Raum (Keyword) | cozy_rustic × bedroom | 9/204 | 4,4 % | 3,9 % | 1,13 | – | – | – | – |  |
| Stil × Raum (Keyword) | tropical × whole_home | 8/204 | 3,9 % | 3,9 % | 1,01 | – | – | – | – |  |
| Stil × Raum (Keyword) | modern_luxury × bedroom | 6/204 | 2,9 % | 3,4 % | 0,86 | – | – | – | – |  |
| Hook-Typ | descriptive | 68/204 | 33,3 % | 34,9 % | 0,96 | – | – | – | – |  |
| Hook-Typ | aspirational | 48/204 | 23,5 % | 25,5 % | 0,92 | – | – | – | – |  |
| Hook-Typ | curiosity | 18/204 | 8,8 % | 8,0 % | 1,11 | – | – | – | – |  |
| Hook-Typ | promotional | 14/204 | 6,9 % | 4,5 % | 1,51 | – | – | – | – |  |
| Hook-Typ | question | 12/204 | 5,9 % | 7,1 % | 0,82 | – | – | – | – |  |
| Hook-Typ | fantasy | 8/204 | 3,9 % | 2,8 % | 1,42 | – | – | – | – |  |

Vollständige Tabelle (alle Werte): `monitor_segments.csv`. Gezeigt: Alarme/Beobachten und je Dimension die 6 häufigsten Werte mit ≥ 5 TQ-Reels.

## 5. Hook-Typen

Quelle: Codebuch-Codierung (Abdeckung 96 %, Rest Heuristik).

| Hook | n | Median topic_index | Anteil im TQ | n Vorwoche | Median Vorwoche | Vergleichbar (n ≥ 8) |
|---|---|---|---|---|---|---|
| promotional | 28 | 1,78 | 50,0 % | – | – | ja |
| money | 7 | 1,71 | 57,1 % | – | – | nein |
| none | 18 | 1,40 | 50,0 % | – | – | ja |
| status | 5 | 1,26 | 20,0 % | – | – | nein |
| instructional | 18 | 1,16 | 38,9 % | – | – | ja |
| fantasy | 17 | 1,16 | 47,1 % | – | – | ja |
| choice | 20 | 1,15 | 40,0 % | – | – | ja |
| contrarian | 12 | 1,08 | 16,7 % | – | – | ja |
| curiosity | 49 | 1,05 | 36,7 % | – | – | ja |
| aspirational | 157 | 0,98 | 30,6 % | – | – | ja |
| location | 11 | 0,95 | 36,4 % | – | – | ja |
| descriptive | 214 | 0,92 | 31,8 % | – | – | ja |
| question | 44 | 0,79 | 27,3 % | – | – | ja |
| pov | 12 | 0,31 | 8,3 % | – | – | ja |

Paarvergleiche (Mann-Whitney, 55 Paare, Benjamini-Hochberg-q < 0,10, Median-Verhältnis ≥ 1,5): promotional > pov (1,78 vs. 0,31, n = 28/12, p = 0,001, q = 0,071)

## 6. Topics

Frische = Anteil der Reels auf der Seite, die nach dem Stichtag veröffentlicht wurden (dort brechen neue Reels ein). Neueinträge = nicht auf der Seite der Vorwoche.

| Topic | Gruppe | n | Median | Median Vorwoche | × | Frische | Neueinträge |
|---|---|---|---|---|---|---|---|
| waterfall-house | fantasy_dream | 12 | 187 Tsd. | – | – | 8 % | – |
| ai-architecture | ai | 12 | 376 Tsd. | – | – | 0 % | – |
| ai-cozy-cabin | ai | 12 | 336 Tsd. | – | – | 0 % | – |
| ai-generated-house | ai | 12 | 548 Tsd. | – | – | 0 % | – |
| ai-home-design | ai | 12 | 985 Tsd. | – | – | 0 % | – |
| ai-interior-design | ai | 12 | 1,7 Mio. | – | – | 0 % | – |
| architecture-design | architecture | 12 | 285 Tsd. | – | – | 0 % | – |
| art-deco-interior-design | style | 12 | 306 Tsd. | – | – | 0 % | – |
| bathroom-design | room_generic | 12 | 620 Tsd. | – | – | 0 % | – |
| bedroom-design | room_generic | 12 | 937 Tsd. | – | – | 0 % | – |
| biophilic-bedroom-design | style | 12 | 124 Tsd. | – | – | 0 % | – |
| cliff-house | unusual_home | 12 | 18 Tsd. | – | – | 0 % | – |
| cozy-bedroom-ideas | cozy_ambience | 12 | 429 Tsd. | – | – | 0 % | – |
| cozy-cabin-in-the-snow | cozy_ambience | 12 | 202 Tsd. | – | – | 0 % | – |
| cozy-rain | cozy_ambience | 12 | 3,9 Mio. | – | – | 0 % | – |
| cozy-winter-cabin | cozy_ambience | 12 | 170 Tsd. | – | – | 0 % | – |
| desert-house | unusual_home | 12 | 40 Tsd. | – | – | 0 % | – |
| dream-bedroom | luxury_room | 12 | 659 Tsd. | – | – | 0 % | – |
| dream-bedrooms | luxury_room | 12 | 1,1 Mio. | – | – | 0 % | – |
| dream-closet | luxury_room | 12 | 708 Tsd. | – | – | 0 % | – |
| dream-home | luxury_home | 12 | 2,3 Mio. | – | – | 0 % | – |
| dream-room | fantasy_dream | 12 | 3,5 Mio. | – | – | 0 % | – |
| future-houses-2050 | future_arch | 12 | 54 Tsd. | – | – | 0 % | – |
| futuristic-home | future_arch | 12 | 280 Tsd. | – | – | 0 % | – |
| futuristic-house | future_arch | 12 | 402 Tsd. | – | – | 0 % | – |
| futuristic-houses | future_arch | 12 | 575 Tsd. | – | – | 0 % | – |
| futuristic-interior | future_arch | 12 | 290 Tsd. | – | – | 0 % | – |
| glass-house | unusual_home | 12 | 94 Tsd. | – | – | 0 % | – |
| house-in-the-forest | unusual_home | 8 | 673 Tsd. | – | – | 0 % | – |
| indoor-pool | pool | 12 | 270 Tsd. | – | – | 0 % | – |

## 7. Wettbewerber-Watchlist

Follower sind auf Embed-Seiten gerundet: Eine Änderung zählt nur, wenn sie größer als die Rundungsstufe ist. Beitragszahlen sind exakt → Beiträge/Woche ist belastbar.

| Handle | Rolle | Follower | Vorwoche | Δ erkennbar? | Posts | Δ Posts | Posts/Woche | Reels auf Topics (neu) | bester topic_index | Verlauf |
|---|---|---|---|---|---|---|---|---|---|---|
| @sunt_mrr | direct | 2M | – | – | 728 | – | – | 7 (0) | 370,57 |  |
| @soothenests | benchmark | 2M | – | – | 2119 | – | – | 4 (0) | 129,60 |  |
| @fast_buildsx | direct | 1M | – | – | 113 | – | – | 1 (0) | 87,19 |  |
| @foorcrafts | direct | 110K | – | – | 57 | – | – | 1 (0) | 70,84 |  |
| @sandiwara_multiverse.99 | direct | 402K | – | – | 79 | – | – | 1 (0) | 32,15 |  |
| @lena_nichi_art | direct | 203K | – | – | 206 | – | – | 1 (0) | 17,83 |  |
| @elitebuildhq | direct | 2M | – | – | 317 | – | – | 3 (0) | 15,59 |  |
| @cozyzen.ai | benchmark | 498K | – | – | 2305 | – | – | 2 (0) | 12,18 |  |
| @luxurydreamhub | benchmark | 1M | – | – | 1144 | – | – | 9 (0) | 11,49 |  |
| @relaxationreflections_ | emerging | 12K | – | – | 818 | – | – | 2 (0) | 10,69 |  |
| @shri_bk_babu | direct | 355K | – | – | 127 | – | – | 1 (0) | 9,08 |  |
| @modern_house__3d | direct | 33K | – | – | 104 | – | – | 1 (0) | 6,72 |  |
| @urban_lifestyle_lab | direct | 250K | – | – | 4660 | – | – | 3 (0) | 4,48 |  |
| @watchthebuild | direct | 106K | – | – | 128 | – | – | 1 (0) | 4,28 |  |
| @rain.nest | direct | 36K | – | – | 531 | – | – | 1 (0) | 2,97 |  |
| @buildenza_ | direct | 145K | – | – | 29 | – | – | 1 (0) | 2,94 |  |
| @wayup_media | benchmark | 941K | – | – | 3170 | – | – | 2 (0) | 2,09 |  |
| @aiforarchitects | direct | 1M | – | – | 513 | – | – | 1 (0) | 1,26 |  |
| @travelask.world | direct | 681K | – | – | 764 | – | – | 2 (0) | 1,02 |  |
| @parametric.architecture | direct | 1.7M | – | – | – | – | – | 1 (0) | 0,29 |  |
| @rainy__village | emerging | 8K | – | – | 45 | – | – | 1 (0) | 0,16 |  |
| @ai.cozy.fun.scenes | emerging | 4K | – | – | 80 | – | – | 1 (0) | 0,15 |  |
| @ai_furniture_design | emerging | 3K | – | – | 40 | – | – | 0 (0) | – |  |
| @archimyst1 | direct | 556K | – | – | 292 | – | – | 0 (0) | – |  |
| @buildcraft.hq | direct | 890K | – | – | 225 | – | – | 0 (0) | – |  |
| @cairo_ia | direct | 944K | – | – | 219 | – | – | 0 (0) | – |  |
| @calmstorms_13 | direct | 47K | – | – | 240 | – | – | 0 (0) | – |  |
| @day_design_101 | direct | 145K | – | – | 227 | – | – | 0 (0) | – |  |
| @designevolutionn | emerging | 26K | – | – | 69 | – | – | 0 (0) | – |  |
| @diniz_nasaroba | direct | 293K | – | – | 52 | – | – | 0 (0) | – |  |
| @ideadesigncasa | direct | 1M | – | – | 224 | – | – | 0 (0) | – |  |
| @kratosdigitalarts | direct | 90K | – | – | 242 | – | – | 0 (0) | – |  |
| @milanchettri123 | emerging | 15K | – | – | 249 | – | – | 0 (0) | – |  |
| @nashla_t_02 | emerging | 16K | – | – | 75 | – | – | 0 (0) | – |  |
| @poppet_tales | emerging | 11K | – | – | 28 | – | – | 0 (0) | – |  |
| @primurse_log | direct | 43K | – | – | 346 | – | – | 0 (0) | – |  |
| @renovaistudio | emerging | 11K | – | – | 248 | – | – | 0 (0) | – |  |
| @thehomopien | direct | 546K | – | – | 378 | – | – | 0 (0) | – |  |
| @uniqchalets | benchmark | 684K | – | – | 655 | – | – | 0 (0) | – |  |
| @vesgantti_home | emerging | 22K | – | – | 958 | – | – | 0 (0) | – |  |

## 8. Messgenauigkeit der Segment-Regeln (gegen Codebuch-Codes, falls vorhanden)

| Feld | n | Übereinstimmung | Häufigste Abweichungen |
|---|---|---|---|
| Raum | 445 | 75 % | Code living_room → Heuristik whole_home (44); Code bedroom → Heuristik whole_home (27); Code pool → Heuristik whole_home (8) |
| Stil | 351 | 56 % | Code modern_luxury → Heuristik futuristic (18); Code minimalist → Heuristik modern_luxury (11); Code classical → Heuristik modern_luxury (10) |
| Hook-Typ | 590 | 51 % | Code aspirational → Heuristik descriptive (62); Code descriptive → Heuristik aspirational (37); Code curiosity → Heuristik descriptive (29) |

Hook-Heuristik je Klasse (Präzision = Anteil der Heuristik-Treffer, die das Codebuch genauso codiert):

| Hook (Heuristik) | n Heuristik | n Codebuch | Präzision | Recall |
|---|---|---|---|---|
| descriptive | 317 | 205 | 48 % | 74 % |
| aspirational | 121 | 150 | 52 % | 42 % |
| question | 54 | 41 | 67 % | 88 % |
| choice | 19 | 20 | 95 % | 90 % |
| location | 18 | 11 | 17 % | 27 % |
| fantasy | 17 | 16 | 6 % | 6 % |
| curiosity | 14 | 49 | 64 % | 18 % |
| promotional | 10 | 26 | 80 % | 31 % |

Niedrige Übereinstimmung heißt: Segmentanteile nur als Trendrichtung lesen; für Entscheidungen die Reels im Board ansehen.

## 9. Menschliche Review (G5, ca. 20 Min.)

- [ ] Alerts P1–P2 öffnen (Links), Reel ansehen, in `inspiration_candidates.csv` **Prinzip in eigenen Worten** notieren – keine Downloads, keine Motiv-Kopie.
- [ ] Pro übernommenem Prinzip: Pillar-Fit (ja/nein) und eine Testidee für die Testmatrix der nächsten Woche (genau **ein** Faktor).
- [ ] Segment-Alarme gegen Abschnitt 8 (Messgenauigkeit) und Überlappung prüfen; nur als Hypothese übernehmen.
- [ ] `watchlist_competitors_next.csv` übernehmen, falls Shortcodes veraltet; Accounts ohne Embed-Daten prüfen (umbenannt/gelöscht?).
- [ ] Eigener **Account Status** in der App geprüft (nur manuell möglich).

