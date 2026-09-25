# Red-Team: Direkte TikTok-Suche nach Hybrid-Formaten (Kategorien C–H)

Zugriff auf alle Quellen: **2026-09-25** (TikTok-Rohdaten 13:40–14:20 UTC). Arbeitsdateien: `research/redteam/hybrid/` (prof_*.json, vids_*.jsonl, table_out.md, stack_*.jpg = Kontaktbögen). Medien-Frames: `media/<video-id>/sheet.jpg` + `meta.json`.
Tags: **Verified** = selbst in TikTok-SSR-JSON (tt_profile.sh / tt_video.sh / tt_media.py) oder in einer selbst neu abgerufenen Primärseite gesehen; **Claimed** = Behauptung Dritter; **Estimated** = eigene Rechnung (Formel angegeben). GMV ≠ Provision ≠ Gewinn.

## 0. Methode und was nicht funktionierte

| Route | Ergebnis |
|---|---|
| TikTok-Discover-Seiten (`/discover/faceless-tiktok-shop-affiliate-example`, `/tiktok-shop-text-to-speech`, `/tts-tiktok-shop-finds`, `/faceless-tiktok-shop-videos`, `/tiktok-shop-voiceover`) per curl und WebFetch | ~370 KB Shell, SSR-JSON enthält nur `app-context`/`i18n`, **keine Items, keine Handles** (canonical = tiktok.com/). WebFetch: „TikTok – Make Your Day", leer. |
| WebSearch (5 von 15 Aufrufen genutzt) | liefert nur Discover-Seiten bzw. Tool-/Kurs-Blogs, keine Video-URLs. |
| Brave via WebFetch | HTTP 429. |
| Reddit-Dumps im Scratchpad (as_*.json, research/reddit/*.json) nach tiktok.com/@-Links durchsucht | 33 Handles, davon shop-relevant: pinecommerce, stellarhealth, landonfinds, dr.uncfinds. |
| YouTube (yt_search.py + NexLev-Transkripte) | Handle-Entdeckung: @cakedfinds (David Margaryan, eJDVLWAn3vs), „lucky finds for you" (Patryk Marketer, Di2nVNQUCsQ – Handle nicht auffindbar). |
| Net-Influencer-Monatsranking (Kalodata-Daten) Nov 2025–Aug 2026, im Scratchpad `research/redteam/ni/` von einem Parallel-Agenten gespeichert; **August-Artikel von mir neu abgerufen** | Liste der Top-10-GMV-Creator → Kandidaten mit „finds"-Namen auf Format geprüft. |
| FastMoss-Blog „Top TikTok Shop creators UK H1 2026" (**von mir neu abgerufen**) | UK-Home-Supplies-Finds-Accounts mit Kategorie-GMV. |
| Bereits gesammelte Videodaten (874 Videos) nach `aigcLabelType ≠ null` UND `isECVideo = 1` gefiltert | neue Hybrid-Kandidaten: beautypickshub, darrenrealdeal, magnificentwalnut, kevin.finds, airgeeksrc. |

Pro Account: tt_profile.sh, tt_recent.sh (neueste ~10 Videos + angepinnte), tt_video.sh für alle 10; tt_media.py auf 1–3 Videos (insgesamt **35 Videos** mit Frames/ASR), Kontaktbögen mit dem Read-Tool angesehen. 22 Accounts mit Shop-Aktivität tabelliert, 1 gelöscht (landonfinds, statusCode 10221).

**Wichtige Grenze:** Eine Stimme kann ich nicht hören. ASR-Text ohne sichtbaren Sprecher = Voiceover (menschlich oder TTS unbekannt). „F" heißt daher: faceless, reale Aufnahmen, Stimme menschlich/unbekannt – **kein Nachweis von KI**.

## 1. Kernergebnisse (Kurzfassung)

1. **Faceless-Formate (F) sind unter den umsatzstärksten TikTok-Shop-Affiliates vertreten und langlebig.** @cakedfinds (reine Hände-/Produkt-Videos mit Voiceover bzw. Text-Hook, 12.700 Videos) stand laut Kalodata/Net Influencer **acht Monate in Folge (Jan–Aug 2026) in den US-Top-10** mit **0,96–1,59 Mio. USD GMV pro Monat** (Ø 1,16 Mio.). @bennettfinds (Körper/Hände ohne Gesicht) Aug 2026: 1,13 Mio. USD GMV. Das widerspricht C2 („High-View-KI-Shop-Accounts = kurzlebige Supplement-Netzwerke") für faceless Formate und C3 – **aber nicht für echte KI-Formate**: Bei keinem dieser Accounts ist KI-Einsatz nachweisbar (kein AI-Label, reale Aufnahmen).
2. **KI-gelabelte Clips (H/G) tauchen inzwischen in Millionen-GMV-Accounts auf – als Beimischung, nicht als Umsatztreiber.** @kevin.finds (Aug 1,17 Mio. USD GMV) und @airgeeksrc (Aug 1,09 Mio.) posten neben Gesichts-Videos Produktclips mit **plattformseitigem AI-Label (`aigcLabelType = 2`)** (1/10 bzw. 3/10 der neuesten Videos, Verified); @magnificentwalnut (E-Scooter, 72.400 Follower) 1/10. Diese KI-Clips haben 66–2.230 Views; die Top-Videos der Accounts (12,4 Mio., 1,6 Mio.) sind reale Aufnahmen.
3. **Reine TTS-/KI-Stimme + Produkt (C/D) zeigt keinen dauerhaften Output.** Einziges belegtes C/G-Beispiel @pinecommerce: TTS-artiges Voiceover + Stock/KI-B-Roll, letztes Video 2026-06-12, Median 38 Views (Verified) → eingeschlafen. @stellarhealth (Supplement, 140.700 Follower) postet seit 2025-01-23 nicht mehr. @landonfinds gelöscht. Das stützt C1/C2 für die engen KI-Formate.
4. **Die Top-10-„Finds"-Accounts sind überwiegend Menschen vor der Kamera** (kid.shops, ericsfindss, dealswithty, huntergrazianoo, magnificentwalnut, myfamilypov-Intro, trending_ttok teilweise). Der Verdacht „Top-Verdiener sind heimlich KI" wird für die Top-Liste **nicht** bestätigt.
5. **Methodische Schwäche des Vorberichts (C5):** Der Parameter „~30 USD GMV pro 1.000 Views" wird durch Kalodata bestätigt (Median der Aug-Top-10: **28,6 USD**, Spanne 13–47 bei Massenware, 135–170 bei Refurb-Apple/E-Bikes). Aber die **View-Annahme** (Stichprobe der neuesten Videos, Ø ~4.000) unterschätzt erfolgreiche GMV-Max-Accounts um 1–3 Größenordnungen: @myfamilypov neueste 10 Videos Median 754 Views bei 18 Videos/Tag → öffentlich hochgerechnet 0,06 Mio. Views/Monat; Kalodata meldet für August **100,0 Mio. Content-Views**. Grund: 70–100 % der Videos dieser Accounts tragen `isAd = true` (GMV-Max/Brand-Ad-Spend), Views laufen über Tage/Wochen nach.
6. **C6/C7 (Videomenge als Engpass) greifen zu kurz:** @cakedfinds erzeugt laut Kalodata-Screen (Claimed, YouTube) ~270 Videos/30 Tage (Lebenszeit-Schnitt 12.700 Videos / 22,4 Monate ≈ 570/Monat, Estimated) und ~1 Mio. USD GMV → **~3.800 USD GMV pro Video** gegenüber 120 USD im C5-Modell (4.000 Views × 30 USD/1.000). Entscheidend sind Produktauswahl mit Brand-Ad-Budget (GMV Max), nicht die Videoanzahl. Allerdings: Alle Top-Accounts posten ebenfalls sehr viel (5–19 Videos/Tag) und mehrere haben Firmen-/Agentur-Kontakte (proecomltd.com, creatornegotiator.com) → „Team" ist plausibel.
7. **Mittelfeld der faceless Finds-Accounts (UK) liegt im Bereich des C5-Modells:** @truehealthsource (F, 24,8-Mio.-View-Video) und @thedealshunter (F) erzielten laut FastMoss in der Kategorie Home Supplies H1 2026 £71.212 bzw. £60.470 → Estimated **~1.200–2.150 USD Provision/Monat** (nur diese Kategorie). Das bestätigt eher die Größenordnung von C5 (1.650 EUR) als dass es sie widerlegt.

## 2. Account-Tabelle (Verified TikTok-Daten, 2026-09-25)

Spalten „Est. Monatsviews" und „Est. Provision" nach der vorgegebenen Formel: Monatsviews = Median(neueste 10) × Videos/Tag (Minimum aus Lebenszeit- und 14-Tage-Rate) × 30; Provision low = Views/1.000 × 0,3 Bestellungen × AOV × 10 %; high = × 1,5 × AOV × 15 %. AOV aus Kalodata (Net Influencer) wo vorhanden, sonst Annahme. **Diese Formel unterschätzt GMV-Max-Accounts massiv (siehe §4) – für die Kalodata-Accounts gilt §3.**

| Handle | Kat. | Follower | Videos | erstellt | Alter (Mon.) | Videos/Tag Lebenszeit | Videos/Tag letzte 14 T. | neuestes Video | Ø Views | Median | Max | Anteil Top-Video | isAd | AI-Label | Est. Monatsviews (Median×V/Tag×30) | AOV (USD) | Est. Provision/Monat low | high |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| @cakedfinds | F/G | 78700 | 12700 | 2024-11-13 | 22.4 | 18.6 | None | 2026-09-02 | 12001 | 11050 | 21600 | 18 | 10 | 0 | 6180294 | 55.84 | 10353 | 77649 |
| @bennettfinds | F | 55900 | 2058 | 2024-09-25 | 24.0 | 2.8 | 5.7 | 2026-09-25 | 2331697 | 3543 | 10300000 | 44 | 10 | 0 | 299555 | 126.14 | 1134 | 8502 |
| @trending_ttok | human-face+F | 233500 | 7563 | 2022-09-25 | 48.0 | 5.2 | 18.0 | 2026-09-25 | 1718 | 1222 | 7175 | 42 | 7 | 0 | 189823 | 115.97 | 660 | 4953 |
| @airgeeksrc | human-face+F+H(AI-Label) | 215500 | 3238 | 2025-04-22 | 17.2 | 6.2 | 4.9 | 2026-09-25 | 1521587 | 1227 | 12400000 | 81 | 5 | 3 | 181494 | 186.96 | 1018 | 7635 |
| @kevin.finds | human-face+H(AI-Label) | 241700 | 6676 | 2023-11-21 | 34.2 | 6.4 | 8.4 | 2026-09-24 | 1500 | 1094 | 5421 | 36 | 3 | 1 | 210822 | 155.8 | 985 | 7390 |
| @kid.shops | human-face | 190300 | 4149 | 2024-08-30 | 24.9 | 5.5 | 6.0 | 2026-09-25 | 2622 | 1101 | 10900 | 42 | 7 | 0 | 181269 | 89.98 | 489 | 3670 |
| @huntergrazianoo | human-face | 16900 | 1626 | 2019-09-13 | 84.5 | 0.6 | 6.6 | 2026-09-25 | 25374 | 4382 | 190200 | 75 | 10 | 0 | 83222 | 21.83 | 55 | 409 |
| @myfamilypov | human-face+F | 329500 | 6364 | 2020-08-10 | 73.6 | 2.8 | 18.0 | 2026-09-25 | 921 | 754 | 1975 | 21 | 8 | 0 | 64295 | 37.22 | 72 | 538 |
| @ericsfindss | human-face | 17500 | 1589 | 2023-10-12 | 35.5 | 1.5 | 4.9 | 2026-09-25 | 839 | 541 | 3030 | 36 | 5 | 0 | 23909 | 265.18 | 190 | 1427 |
| @dealswithty | human-face | 159400 | 3439 | 2023-09-04 | 36.7 | 3.1 | 8.1 | 2026-09-25 | 2862 | 1945 | 7386 | 26 | 8 | 0 | 179699 | 137.99 | 744 | 5579 |
| @truehealthsource | F | 22600 | 816 | 2024-01-03 | 32.8 | 0.8 | 0.4 | 2026-09-25 | 3645648 | 9430 | 24800000 | 68 | 9 | 0 | 123812 | 30 | 111 | 836 |
| @thedealshunter | F | 30800 | 6654 | 2023-09-02 | 36.8 | 5.9 | 11.7 | 2026-09-25 | 89396 | 440 | 653500 | 73 | 3 | 0 | 78586 | 20 | 47 | 354 |
| @beautypickshub | F/G | 7363 | 427 | 2025-02-11 | 19.4 | 0.7 | None | 2026-09-24 | 35479 | 2170 | 184600 | 52 | 9 | 3 | 47057 | 40 | 56 | 424 |
| @darrenrealdeal | human-face+F | 29000 | 3061 | 2024-03-11 | 30.5 | 3.3 | 12.0 | 2026-09-25 | 155841 | 2563 | 1100000 | 71 | 7 | 0 | 253653 | 60 | 457 | 3424 |
| @three_reasons_why | human-face | 26700 | 1717 | 2024-06-29 | 26.9 | 2.1 | 0.5 | 2026-09-25 | 142332 | 7514 | 702100 | 49 | 7 | 0 | 113345 | 40 | 136 | 1020 |
| @chrisandjet.tts | human-face | 29600 | 2514 | 2024-07-26 | 26.0 | 3.2 | 9.3 | 2026-09-25 | 176244 | 568 | 1200000 | 68 | 5 | 0 | 54133 | 200 | 325 | 2436 |
| @magnificentwalnut | human-face(+H) | 72400 | 799 | 2020-04-06 | 77.7 | 0.3 | 0.9 | 2026-09-23 | 10226 | 10400 | 23000 | 22 | 10 | 1 | 105474 | 400 | 1266 | 9493 |
| @pinecommerce | C/G | 628 | 509 | 2020-12-25 | 69.1 | 0.2 | None | 2026-06-12 | 139 | 38 | 961 | 69 | 0 | 0 | 273 | 8 | 0 | 0 |
| @stellarhealth | unknown (Supplement) | 140700 | 67 | 2023-07-29 | 38.0 | 0.1 | None | 2025-01-23 | 1906 | 1280 | 4464 | 26 | 0 | 0 | 2230 | 30 | 2 | 15 |
| @xiaoyi9955 | F | 18200 | 490 | 2025-07-04 | 14.7 | 1.1 | None | 2026-08-16 | 1600 | 929 | 4094 | 26 | 0 | 0 | 30461 | 15 | 14 | 103 |
| @teachingtts | human-face | 53800 | 1334 | 2024-08-23 | 25.1 | 1.7 | 8.2 | 2026-09-24 | 1100 | 569 | 4983 | 45 | 9 | 0 | 29858 | 50 | 45 | 336 |
| @dr.uncfinds | human-face/Repost | 35100 | 235 | 2024-07-22 | 26.2 | 0.3 | None | 2026-09-18 | 1268 | 1038 | 4077 | 40 | 3 | 0 | 9208 | 40 | 11 | 83 |

„None" bei Videos/Tag (14 T.) = weniger als 3 Videos in den letzten 14 Tagen im Sample. Das Embed zeigt angepinnte Alt-Videos mit, daher „Anteil Top-Video" teils aus alten Hits (z. B. truehealthsource 24,8 Mio., airgeeksrc 12,4 Mio., bennettfinds 10,3 Mio.).

### 2.1 Formatklassifikation (Kontaktbögen angesehen)

| Handle | Video (Views, Datum) | Was die Frames zeigen | ASR/Ton | Kategorie |
|---|---|---|---|---|
| @cakedfinds | 7680788024334077215 (21.600, 2026-09-02); 7677076242574757151 (10.300); 7677061725258026271 (7.974, 7 s) | nur Hände + Karton mit Skincare-Bundle, Text-Hook „HOW IS THIS EVEN LEGAL?"/„Anyone else!?"; 7-s-Video: Stock-/KI-artige Portraitbilder („my biggest insecurity") + Hände mit Produkt | Voiceover ohne Sprecher („Yes! You get this entire box of 200 worth of products…"); 7-s-Video ohne Sprache | **F** (Stimme unbekannt), teils **G** (Stock/KI-Hook-Bild + echtes Produkt) |
| @bennettfinds | 7640260801978289438 (10,3 Mio., 2026-05-15); 7671407687652920606 (6,5 Mio.) | Person im Bett / auf der Terrasse, Gesicht nicht im Fokus, Hände am Produkt (Mellow-Kissen, Shark-Bläser) | Voiceover | **F** |
| @truehealthsource (UK) | 7629444796087651606 (24,8 Mio., 2026-04-16); 7684311765756185878 (31.900) | nur Hände, Waschbecken/Abfluss, Eierkocher; Wort-für-Wort-Captions (CapCut) | Voiceover ohne Sprecher | **F** |
| @thedealshunter (UK) | 7660868016422407446 (653.500); 7689418722209008918 (593) | nur Hände + Produkt (Flagge, Crimpzange), Titel-Overlay | Voiceover mit Füllwörtern („uh, the uh") → wahrscheinlich menschlich | **F** |
| @beautypickshub | 7665691177278082335 (184.600, 2026-07-23); 7671368646588943647 (4.001) | nur Hände im Auto, Tarte-Bundle, Swatches – gleiche Vorlage wie cakedfinds („Such a great deal today omg") | lautes Voiceover (−9,9 dB) ohne Sprecher | **F**; neuere Posts = Foto-Slideshows mit `aigcLabelType 2` → **G/H** |
| @trending_ttok | 7689258510520995085 (7.188); 7689178234591792397 (1.205) | Video 1: Mann vor Kamera (Küche); Video 2: nur Hände + Luftreiniger | Voiceover/Direktton | **human-face + F** |
| @kevin.finds | 7688905577250032926 (2.081, AI-Label 2); 7689216484475751710 (693); 7688873430179171615 (5.421) | AI-gelabelter Clip: MacBook auf Teppich, Hände, Text-Overlays („LOW STOCK LEFT RIGHT NOW"); sonst Mann vor Kamera/Vlog | KI-Clip: „The MacBook Air fully updated to the 2027 Golden Gate…" (inhaltlich unsinnig → Skript/TTS wahrscheinlich KI) | **human-face + H/G** |
| @airgeeksrc | 7611067129126849806 (12,4 Mio.); 7689163845247552781 (1.105, AI-Label 2); 7666464793829690637 (1,2 Mio.); 7689107479736667406 | RC-Auto-Produktfahrt (Musik); AI-gelabelter iPad-Clip: Hände + Produkt, fotoreal, kein Ton (−39,8 dB); MacBook/iPad-Videos: Mann vor Kamera, LIVE-Verweis | Musik bzw. Direktton | **human-face + F + H** |
| @darrenrealdeal (UK) | 7657936707253325078 (1,1 Mio.) | Mann-Gesicht als Hook, dann Hände + Powerstation | Direktton/Voiceover | **human-face + F**; ein Foto-Post mit AI-Label 2 (Verified aus Vorlauf-Daten) |
| @myfamilypov | 7689223073333054750 (1.989) | Gesicht-Intro, dann Füße/Hände/Produkt-B-Roll | Voiceover | **human-face + F** |
| @kid.shops, @ericsfindss, @dealswithty, @huntergrazianoo, @magnificentwalnut, @three_reasons_why, @chrisandjet.tts, @teachingtts | je 1–2 Videos | Person vor Kamera | Direktton | **human-face** |
| @pinecommerce | 7632016814028967182 (961) | Steckdosen-Ultraschallgerät (Produkt-Close-up) + Szenen Kleinkind/Golden Retriever (Stock oder KI) | glattes Werbe-Voiceover („total game changer… plug and play") | **C/G** (TTS lt. Vorbericht per Gemini 95 %) |
| @dr.uncfinds | 7680668451806989581 (4.077) | News-Mitschnitte + Mann mit Peptid-Dosen | Fremdton | human-face/Repost (Peptide) |

## 3. Umsatzdaten der faceless/hybriden Top-Accounts (Analytics-Plattform, Claimed-Charakter)

Quelle: Net Influencer, Monatsrankings „Top 10 independent creators" mit „Data from Kalodata". August-Artikel **neu abgerufen** (https://www.netinfluencer.com/top-10-sales-by-independent-creators-on-tiktok-in-august-2026/, published 2026-09-24, Zugriff 2026-09-25); Jan–Jul aus `research/redteam/ni/` (canonical-URLs dort). Kalodata = Schätzung eines Drittanbieters, **kein Dashboard**.

| Account | Kat. | GMV-Verlauf (USD) | Content-Views Aug | GMV/1.000 Views | Est. Provision/Monat (GMV × 5–15 % × 0,9 Retouren) |
|---|---|---|---|---|---|
| @cakedfinds | F/G | Jan 1,18 Mio · Feb 975.760 · Mär 1,15 Mio · Apr 960.660 · Mai 1,04 Mio · Jun 1,59 Mio · Jul 1,35 Mio · Aug 1,03 Mio (8/8 Monate Top 10) | 29,29 Mio | 35,2 | 46.350 – 139.050 |
| @bennettfinds | F | Aug 1,13 Mio (erstmals Top 10) | 24,05 Mio | 47,0 | 50.850 – 152.550 |
| @trending_ttok | human-face + F | Nov 2025 1,56 Mio … Aug 2026 3,37 Mio (10/10 Monate Top 10) | 90,7 Mio | 37,2 | 151.650 – 454.950 |
| @kevin.finds | human-face + H | Jul 975.780 · Aug 1,17 Mio | 6,88 Mio | 170,1 | 52.650 – 157.950 |
| @airgeeksrc | human-face + F + H | Aug 1,09 Mio (erstmals) | 8,07 Mio | 135,1 | 49.050 – 147.150 (Account betreibt LIVE-Verkauf; ob Affiliate-Provision oder Händlermarge: nicht öffentlich verifizierbar) |

Warum 5 % als Untergrenze: Laut Creator „ducrez" (YouTube Ldkgz8ptFUQ, Kursanbieter, Claimed) sinkt die Provision, wenn Videos per GMV Max beworben werden, und seine Agentur-Accounts laufen unter „1 % invite". Die tatsächliche Provisionsrate der genannten Accounts ist **nicht öffentlich verifizierbar**.

Ergänzend (Claimed, Kursverkäufer): David Margaryan (YouTube eJDVLWAn3vs, ~Aug 2026, 3.802 Views) zeigt @cakedfinds im Kalodata-Creator-Tab: „made over $1.1 million in sales in the last 30 days … in the last 90 days … almost $4 million … post simple videos … without ever having to show their face", „270 videos in the last 30 days", Platz 10 der Kalodata-Creator-Liste. Er verkauft ein Nachbau-System (Produkte + Videos mit KI nachbauen) → Bias.

UK-Mittelfeld (FastMoss, „Top TikTok Shop creators UK H1 2026", https://www.fastmoss.com/blog/top-tiktok-shop-creators-uk-h1-2026/, datePublished 2026-07-24, **neu abgerufen** 2026-09-25; Kategorie-Umsatz Home Supplies, nicht Gesamtumsatz):

| Account | Kat. | Est. H1-Kategorieumsatz | Monate im Ranking | Est. Provision/Monat (H1/6 × 10–15 % × 0,9; £1 = 1,34 USD) |
|---|---|---|---|---|
| @three_reasons_why | human-face | £117.486 | 5/6 | £1.762–2.643 (≈ 2.360–3.540 USD) |
| @darrenrealdeal | human-face + F | £105.353 | 3/6 | £1.580–2.370 (≈ 2.120–3.180 USD) |
| @truehealthsource | **F** | £71.212 | 2/6 | £1.068–1.602 (≈ 1.430–2.150 USD) |
| @thedealshunter | **F** | £60.470 | 3/6 | £907–1.361 (≈ 1.215–1.820 USD) |

## 4. Methodenkritik am Vorbericht (C5–C7)

- **GMV pro 1.000 Views:** Kalodata-Aug-Top-10: huntergrazianoo 13,1 · myfamilypov 17,8 · torijflow 19,3 · dj.foof 21,7 · kid.shops 22,1 · cakedfinds 35,2 · trending_ttok 37,2 · bennettfinds 47,0 · airgeeksrc 135,1 · kevin.finds 170,1 (Median 28,6) → **C5-Parameter 30 USD bestätigt** (Estimated aus Claimed-GMV/Views).
- **Views:** Die öffentliche Stichprobe der neuesten Videos (Vorbericht: „neueste 10–20 Videos") misst bei Vielpostern Views wenige Stunden nach Upload. Vergleich öffentliche Hochrechnung (Median × Videos/Tag × 30) vs. Kalodata-Content-Views Aug: cakedfinds 6,2 Mio vs 29,3 Mio (×4,7); trending_ttok 0,19 Mio vs 90,7 Mio (×480); myfamilypov 0,064 Mio vs 100,0 Mio (×1.560); huntergrazianoo 0,083 Mio vs 79,1 Mio (×950); bennettfinds 0,30 Mio vs 24,1 Mio (×80). **Die Methode kann erfolgreiche Accounts strukturell nicht erkennen** (Verified Stichprobe, Claimed Kalodata, Estimated Verhältnis).
- **Mechanismus:** 70–100 % der neuesten Videos der Top-Accounts sind `isAd = true` (Verified: cakedfinds 10/10, bennettfinds 10/10, huntergrazianoo 10/10, magnificentwalnut 10/10, truehealthsource 9/10, myfamilypov 8/10, dealswithty 8/10, trending_ttok 7/10). Reichweite kommt aus Brand-Ad-Spend (GMV Max), nicht aus Followern. Das Modell C5 („~4.000 mittlere Views, organisch") bildet diesen Kanal nicht ab.
- **Aber:** Für das Mittelfeld (UK-Finds-Accounts mit 21–29k Followern) liegen die Schätzungen bei 1.200–3.500 USD Provision/Monat – nahe C5. Die Verteilung ist extrem schief: wenige Accounts mit 1–3 Mio. USD GMV, ein breites Mittelfeld um vierstellige Provisionen.

## 5. Welche Hybrid-Formate zeigen dauerhaften Output?

| Kategorie | Beispiele | Aktiv > 3 Monate? | Viele Shop-Videos? | Konstante Views? | Est. Einkommensband (Provision/Monat) |
|---|---|---|---|---|---|
| **F** faceless reale Aufnahmen (Hände/Körper + Voiceover/Text) | cakedfinds, bennettfinds, truehealthsource, thedealshunter, beautypickshub | ja (22–37 Monate; cakedfinds 8 Monate Top 10) | ja (427–12.700 Videos, 10/10 isEC) | Basis-Views niedrig (Median 440–11.050), Spitzen 0,65–24,8 Mio. über GMV Max | Top: ~46.000–153.000 USD (Est. aus Kalodata-GMV); Mittelfeld: ~1.200–2.200 USD (Est. aus FastMoss); klein/Burst: beautypickshub ~1.000–1.800 USD aus einem Burst-Tag (Est.: 342.300 Views × 31–35 USD/1.000 × 10–15 %) |
| **H/G** KI-gelabelte Produktclips als Beimischung | kevin.finds, airgeeksrc, magnificentwalnut, darrenrealdeal, beautypickshub | ja (Accounts), KI-Clips erst seit Aug/Sep 2026 sichtbar | ja | KI-Clips 66–2.230 Views | Einzelbeitrag der KI-Clips: nicht öffentlich verifizierbar; Account-Einkommen stammt überwiegend aus Nicht-KI-Videos |
| **G** Stock/KI-Hook-Bild + echtes Produkt | cakedfinds (7-s-Video), pinecommerce | cakedfinds ja; pinecommerce nein | – | – | s. F; pinecommerce ≈ 0 |
| **C/D** TTS/KI-Stimme + Produkt | pinecommerce | **nein** (letztes Video 2026-06-12) | 509 Videos | Median 38 | ≈ 0 aktuell; früher Claimed „$200–300/Tag" (Reddit, Vorbericht) |
| **E** KI-Skript/-Varianten bei echtem UGC | nicht erkennbar (Skript-KI ist aus Frames/ASR nicht nachweisbar); Indiz: kevin.finds-Clip mit unsinnigem Text („2027 Golden Gate") | – | – | – | nicht öffentlich verifizierbar |
| **A/B** | keiner in dieser Stichprobe | – | – | – | – |
| unknown/Supplement | stellarhealth (140.700 Follower, 67 Videos) | **nein** (inaktiv seit 2025-01-23) | – | Median 1.280 | ≈ 0 aktuell |

## 6. Negativbefunde (für Fairness gegenüber dem Vorbericht)

- @landonfinds (in Reddit als Finds-Account genannt): statusCode 10221 – existiert nicht mehr.
- @pinecommerce: 628 Follower, letztes Video 2026-06-12, Median 38 Views (Verified) – das einzige klare TTS+Produkt-Beispiel ist eingeschlafen.
- @stellarhealth: Reddit 2024 „Has anyone noticed the sales of these TIKTOK AI videos?"; 140.700 Follower, aber nur 67 Videos, alle Prostata-Supplement-Clips 54–130 s, letztes Video 2025-01-23 (Verified) → klassisches kurzlebiges Supplement-Muster (stützt C2).
- @xiaoyi9955 (F, reale Aufnahmen): isECVideo 0 in allen 10 neuesten Videos, letztes Video 2026-08-16 → Shop-Aktivität rückläufig.
- @cakedfinds: neuestes Video im Embed vom **2026-09-02** – seit 23 Tagen keine neuen Posts sichtbar (Verified), und Kalodata-GMV fällt seit Juni (1,59 → 1,35 → 1,03 Mio.). Langlebigkeit über 8 Monate belegt, Fortbestand offen.
- „lucky finds for you" (Patryk Marketer, Kurs/Tool-Anbieter Krafie, YouTube Di2nVNQUCsQ): „he is making 174,000 in sales in GMV" mit „all AI"-Videos; ein weiterer Account „370 in GMV" – Handles nicht verifizierbar (luckyfindsforyou = 100 Follower, 11 Videos). **Claimed, nicht verifizierbar.**
- „ducrez" (YouTube Ldkgz8ptFUQ, 2026-09-22): „over 452K in GMV as a community … every single account that we run is under our agency under a 1% invite" und fremde 10-s-KI-Videos mit „$24,000 in GMV" / „$27,000 in GMV" – keine Handles, Kursanbieter-Bias. Bemerkenswert: bei 1 % Provision entspräche 452K GMV nur ~4.500 USD Provision (Estimated).

## 7. Auswirkungen auf C1–C7

- **C1** (vollvirtuelle KI-Influencer funktionieren nicht): nicht angegriffen – kein A/B-Account mit Shop gefunden.
- **C2** (High-View-KI-Shop-Accounts = kurzlebige Supplement-Netzwerke): **teilweise widerlegt**, wenn man faceless (F) mitzählt: cakedfinds, bennettfinds, truehealthsource sind keine Supplement-Accounts und über viele Monate aktiv. Für echte KI-Formate (C/D) bestätigt (pinecommerce, stellarhealth).
- **C3** (dauerhaft vierstellige Provisionen mit KI-Content selten): für F-Formate **widerlegt** (Top: fünf- bis sechsstellig Est.; Mittelfeld: vierstellig Est.), für KI-Formate im engen Sinn **nicht widerlegt**.
- **C4** (10k+-Claims vor allem von Kursverkäufern): **teilweise widerlegt** – die Kalodata-Rankings (Net Influencer, FastMoss) sind keine Kursverkäufer-Claims; die YouTube-Claims zu KI-Accounts (ducrez, Margaryan, Patryk) stammen aber weiterhin von Kurs-/Tool-Anbietern.
- **C5** (≈1.650 EUR/Monat bei 5 Videos/Tag): GMV/View-Parameter **bestätigt**; die View-Annahme **methodisch verzerrt** (Neueste-Video-Stichprobe, kein GMV-Max-Kanal). Für das Mittelfeld der F-Accounts plausibel.
- **C6/C7** (10k EUR ≈ 830, 20k ≈ 1.650 Videos/Monat): **als Mengengesetz widerlegt** – cakedfinds: ~270–570 Videos/Monat ↔ ~1 Mio. USD GMV (≈3.800 USD GMV/Video, Estimated). Die Hebel sind Produktauswahl mit Brand-Ad-Budget und CTR, nicht Videozahl. „Wahrscheinlich ein Team" bleibt plausibel (Business-Adressen: [E-Mail-Adresse aus Bio entfernt], [E-Mail-Adresse aus Bio entfernt]; myfamilypov-Bio „How We Run $100K+/mo TikTok Shop").

## 8. Selbstverifikation der drei stärksten Gegenbefunde

### Verifikation H1 – @cakedfinds (F/G, Kalodata-Top-10 Jan–Aug 2026)
- Quelle neu geöffnet: Net-Influencer-Augustartikel (published 2026-09-24): „@cakedfinds posted $1.03 million in revenue in August, selling 18.43k items at an average unit price of $55.84. The account had 76.9k followers and drew 29.29 million content views. @cakedfinds ranked No. 4 in June at $1.59 million and No. 3 in July at $1.35 million". Datenbasis Kalodata (Schätzung). Jan–Jul aus gespeicherten Artikeln (canonical-URLs in `research/redteam/ni/*.html`).
- TikTok neu geprüft: Profil 78.700 Follower, 1,7 Mio. Likes, 12.700 Videos, createTime 2024-11-13, ttSeller false, Bio „amazing deals just for you 🎁❤️ / 📧 [E-Mail-Adresse aus Bio entfernt]" (Verified). 10 neueste Videos (2026-08-18 bis 09-02): 7.032–21.600 Views, Median 11.050, alle isAd = true, isECVideo = 1, kein AI-Label (Verified). 3 Videos per tt_media.py klassifiziert: Hände + Produktkarton + Voiceover bzw. Stock/KI-artiges Hook-Bild + Hände.
- Rechnung: 1,03 Mio. / 29,29 Mio. × 1.000 = 35,2 USD GMV/1.000 Views; Provision 1,03 Mio. × 5–15 % × 0,9 = 46.350–139.050 USD (Estimated). Metrik = GMV (nicht Provision, nicht Gewinn); Zeitraum monatlich.
- Bias: Net Influencer = Branchenmedium, Kalodata = kommerzieller Anbieter; YouTube-Bestätigung durch Kursverkäufer.
- Kategorie: **F** (reale Hände, Stimme unbekannt), punktuell G. KI-Einsatz **nicht nachgewiesen**.
- Seit 2026-09-02 keine neuen Videos sichtbar; GMV-Trend seit Juni fallend.
- **Verdict: PARTIALLY** – GMV-Dauerhaftigkeit (8 Monate ≥ 0,96 Mio.) durch Analytics-Plattform bestätigt; als „KI-Content"-Beleg überzeichnet (Format F, kein KI-Nachweis); Provision nur geschätzt; aktueller Posting-Stopp.

### Verifikation H2 – @truehealthsource (F, UK)
- Quelle neu geöffnet: FastMoss „Top TikTok Shop creators UK H1 2026" (datePublished 2026-07-24): „3 TrueHealth Source @truehealthsource 21.4K £71,212 2 / 6 Video-led" (Home Supplies, geschätzter Kategorieumsatz).
- TikTok neu geprüft: 22.600 Follower, 816 Videos, createTime 2024-01-03, Bio „2026"; Video 7629444796087651606: **24.800.000 Views**, 33 s, isAd = true, isECVideo = 1, Sticker „ENMALL Drain cleaner", kein AI-Label (Verified). 10 neueste: Median 9.430, 9/10 isAd. tt_media: 2 Videos nur Hände + Produkt + Wort-Captions, Voiceover ohne Sprecher.
- Rechnung: £71.212/6 × 10–15 % × 0,9 = £1.068–1.602/Monat ≈ 1.430–2.150 USD (Estimated; nur eine Kategorie; Umsatz auf 2 Monate konzentriert).
- Kategorie **F**; Stimme unbekannt (keine KI-Label, keine TTS-Kennzeichnung).
- **Verdict: PARTIALLY** – belegt einen langlebigen (32 Monate) faceless Account mit Mega-Ausreißer und vierstelliger Est.-Provision; bestätigt damit eher die C5-Größenordnung als sie zu sprengen; KI nicht nachgewiesen.

### Verifikation H3 – „KI-gelabelte Clips in Millionen-GMV-Accounts" (@kevin.finds, @airgeeksrc)
- Quelle neu geöffnet: Net-Influencer-August: kevin.finds 1,17 Mio. USD, 6,88 Mio. Views; airgeeksrc 1,09 Mio. USD, 8,07 Mio. Views.
- TikTok neu geprüft: kevin.finds 241.700 Follower, 6.676 Videos, ttSeller true; Video 7688905577250032926 `aigcLabelType = 2`, isAd true, 2.081 Views (Verified); Frames: MacBook mit Text-Overlays, Hände; ASR mit sinnlosem Modellnamen. airgeeksrc 215.500 Follower, 3.238 Videos; 3/10 neueste Videos `aigcLabelType = 2` (66–1.105 Views); Top-Videos 12,4 Mio./1,6 Mio./1,2 Mio. ohne Label, teils Mann vor Kamera mit LIVE-Hinweis.
- Kategorie: Account = human-face + F; die KI-Clips = **H/G**. Die KI-Clips erzeugen nachweislich nur wenige Views; der Millionen-GMV hängt an Nicht-KI-Content und LIVE.
- **Verdict: OVERSTATED** als Gegenbeweis zu C3 (KI-Clips sind nicht der Umsatztreiber); **CONFIRMED** als Beleg, dass Top-Accounts KI-Produktclips bereits beimischen und dass diese ein plattformseitiges Label tragen.

## 9. Outlier-Videos (Verified Views; GMV pro Video nicht öffentlich)

| Video | Handle | Views | Kat. | Hinweis |
|---|---|---|---|---|
| https://www.tiktok.com/@truehealthsource/video/7629444796087651606 | truehealthsource | 24.800.000 | F | isAd, Abflussreiniger |
| https://www.tiktok.com/@airgeeksrc/video/7611067129126849806 | airgeeksrc | 12.400.000 | F (Produkt-only, Musik) | isAd |
| https://www.tiktok.com/@bennettfinds/video/7640260801978289438 | bennettfinds | 10.300.000 | F | isAd, Mellow-Kissen |
| https://www.tiktok.com/@truehealthsource/video/7610537211720781078 | truehealthsource | 9.200.000 | F (nicht per Frames geprüft, gleiche Serie) | isAd |
| https://www.tiktok.com/@bennettfinds/video/7671407687652920606 | bennettfinds | 6.500.000 | F | isAd, Shark |
| https://www.tiktok.com/@darrenrealdeal/video/7657936707253325078 | darrenrealdeal | 1.100.000 | human-face + F | isAd |
| https://www.tiktok.com/@thedealshunter/video/7660868016422407446 | thedealshunter | 653.500 | F | isAd |
| https://www.tiktok.com/@beautypickshub/video/7665691177278082335 | beautypickshub | 184.600 | F | isAd, 7.363-Follower-Account |
| https://www.tiktok.com/@huntergrazianoo/video/7688812477068496142 | huntergrazianoo | 190.300 | human-face | isAd |

Account-Level-GPM (Kalodata Aug): bennettfinds 47,0 USD/1.000 Views, airgeeksrc 135,1 – auf Einzelvideos **nicht** übertragbar; Bestellungen pro Video: nicht öffentlich verifizierbar.
