# Red-Team: Winner-Videos pro Produkt – Views, Bestellungen, GPM und Format (TikTok Shop)

Stand: 2026-09-25 · Zugriff auf alle Quellen: 2026-09-25 · Winkel: `_prompt_product_top_videos.txt`
Arbeitsdateien: `research/redteam/ptv/` (videos.json, ni_rows.json, imgs/, et/, Kalodata-/FastMoss-Screenshots)

## 0. Kurzfassung (was gegen den Vorbericht spricht und was ihn stützt)

1. **Öffentliche Per-Video-Daten sind rar.** Die FastMoss-Blogartikel zu den 12–15 Top-Produkten (medicube, Toplux, Goli, NeoCell, Dr.Melaxin, PetPivot, Rhino, EcoFlow, Nex Playground, GreatVita DE, Portland Leather, UnciaActive) enthalten fast nur **Produkt-** oder **Creator-Summen**. Echte Video-Zeilen (Views + Units + GMV) gibt es nur für DR.DENT (3 Videos, FastMoss-Screenshot), Built Bar (2 Videos), MREGB Socket Fan Light und Dog Car Seat Cover (Kalodata-Screenshots) sowie EchoTik-Fallstudien (2023/24 + Yoga 2026). Zusammen mit Selbstauskünften ergibt das **28 dokumentierte Winner-Videos** (Tabelle 2), davon **15 aus Analyseplattformen**, 13 Claimed aus Kursen/Reddit.
2. **Stärkster Gegenbefund (human-face, nicht KI):** @quinclips3 („Ayden“, 98.500 Follower) – ein einziges DR.DENT-Selfie-Demo-Video brachte laut FastMoss in 28 Tagen **81,5 Mio. Views, 27.300 Units, 430.000 USD GMV** (Video auf TikTok verifiziert: heute 165,9 Mio. Plays, 45 s, 01.02.2026). Bei 15 % Provision ≈ **64.500 USD Provision aus einem Video** (Estimated). Net Influencer führt Ayden im Februar 2026 mit **871.990 USD GMV** (≈ 130.800 USD Provision, Estimated). Das widerspricht der impliziten Annahme des Vorberichts (C5–C7), Einkommen skaliere nur über Videomenge – **ein Winner-Creative plus markenfinanzierte Ad-Verstärkung** kann ein Vielfaches liefern. Es ist aber **kein KI-Fall**.
3. **KI-Gegenbefund (mittel/schwach):** Kalodata-Dashboard-Screenshot (Anbieterblog, verkauft KI-Videotool) zeigt für MREGB Socket Fan Light ein **als „AI“ und „AD“ markiertes Video mit 739.780 Views, 3.160 Items, 82.130 USD Umsatz** (GPM 111 USD) im Zeitraum 18.06.–19.07.2026. Handle nicht genannt, Affiliate-Status und Provision unbekannt, teils bezahlte Reichweite. Das zeigt: **KI-markierte Produkt-Creatives können Winner werden** – ein Punkt gegen C1/C3 in ihrer absoluten Form, aber nicht gegen C1 im engeren Sinn (kein virtueller Influencer).
4. **Konversion pro View fällt mit der Viralität – über Produkte/Creator hinweg, nicht innerhalb eines Creatives.** Median der dokumentierten 1M+-Videos: **GPM 14,5 USD, 0,37 Bestellungen/1.000 Views**; Videos < 1 Mio.: **GPM 81 USD, 1,02 Bestellungen/1.000 Views** (Selektionsbias beachten). Innerhalb von Aydens drei Videos bleibt die Rate aber konstant (0,33–0,38/1k bei 14,6–81,5 Mio. Views).
5. **Top-10-US-Creator (Net Influencer, 70 Creator-Monate):** Median **24,9 USD GMV pro 1.000 Content-Views** (IQR 17,8–35,5), Median 0,42 Items/1k. Das liegt **unter** dem „realistischen“ GPM des Vorberichts (30,4 USD) – in diesem Punkt war der Vorbericht eher zu **optimistisch**, nicht zu pessimistisch.
6. **Paid Amplification ist der fehlende Hebel im Vorbericht:** Fast alle 1M+-Winner mit Analysedaten tragen Ad-Signale (Ayden: FastMoss-„Ads“-Label; Dog Seat Cover: 57 % Ad-Views, 80 % Ad-Umsatz; MREGB-Video 1: „AD“; Built Bar Hero-SKU: 50,5 % Ad-Anteil; Healthy Smart Deals: „alle als Ads“). Marken kaufen Reichweite auf funktionierende Affiliate-Videos (Spark/GMV Max). Das organische Modell (C5: ~4.000 Views/Video) bildet diesen Tail nicht ab.
7. **Hypothese „200 Videos → 1 Video mit 2 Mio. Views → 1.200 Verkäufe → 8.400 EUR Provision“:** Die implizierte Rate (0,6 Best./1k, 7 EUR Provision/Verkauf ≈ GPM 18–30 USD) liegt **über dem Median** dokumentierter 1M+-Videos (0,37/1k; GPM 14,5), aber innerhalb der Spannweite. Mit Median-Konversion bringt ein 2-Mio.-Video **≈ 1.450–5.100 EUR** (je nach AOV × Provisionssatz), nicht 8.400. Die eigentliche Unsicherheit ist die **Frequenz** „1 von 200“: Belegt nur für einen Top-1-%-Human-Creator (Ayden ≥ 5 Videos ≥ 2 Mio. bei 801 Videos ≈ 1 von 160), nicht für neue oder KI-Accounts. Bedingt auf einen echten Winner kann der Ertrag durch Marken-Ads dagegen **weit über** 8.400 EUR liegen (Ayden-Video: ≈ 59.000 EUR Provision, Estimated).

## 1. Methode und Evidenzklassen

- Quellen: 23 FastMoss-Blogposts (10 bereits vorhanden, 15 neu geladen nach `ptv/fm2_*.txt`), Bild-Tabellen visuell gelesen (DR.DENT-Videotabelle), FastMoss-Influencerseite (liefert nur Handle, Daten hinter Login), 46 EchoTik-Blogposts (`ptv/et/`), Kalodata-Blog via r.jina.ai (+ 2 Screenshots visuell gelesen), 10 Net-Influencer-Monatsrankings (von anderem Agenten geladen, `research/redteam/ni/`, neu geparst), Selbstauskünfte aus den Quellen des Vorberichts (`quellen/claims_*.md`, `sweep_*.md`).
- TikTok-Prüfung: `tt_profile.sh`, `tt_recent.sh`, `tt_video.sh` für @quinclips3, @demi_does.it, @drew.review, @lorienwright, @grantsdealz, @simplysammyk, @callmebelly, @callmecollins.hdc, @furniturebyfara; `tt_media.py` + Kontaktbogen für @quinclips3 (DR.DENT-Winner), @grantsdealz und @drew.review.
- WebSearch: 11 Aufrufe (Limit 15).
- Tags: **Verified** = in TikTok-Rohdaten gesehen; **Claimed** = von Plattform/Person behauptet (Analyseplattform-Zahlen sind Schätzungen der Plattform, auch wenn ich den Screenshot gesehen habe); **Estimated** = eigene Rechnung (Formel angegeben). GMV ≠ Provision ≠ Gewinn. Wechselkurs wie Vorbericht: 0,92 EUR/USD.
- Kennzahlen: **GPM** = GMV / Views × 1.000; **Best./1k** = Bestellungen (bzw. Units/Items) / Views × 1.000.

## 2. Tabelle der dokumentierten Winner-Videos (n = 28)

Quellenkürzel siehe Abschnitt 9. „n/a“ = nicht veröffentlicht.

| ID | Handle / Quelle-Label | Produkt | Views | Bestellungen | GMV (USD) | GPM (USD/1k) | Best./1k Views | Format | Tag | Quelle | Anmerkung |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V01 | quinclips3 | DR.DENT Purple Whitening Strips (US) | 81.500.000 | 27.300 | 430.000 | 5,3 | 0,33 | human-face | Claimed (FastMoss) | FM-DRDENT | Ads-Label; 28d; Video verifiziert 165,9 Mio. Plays |
| V02 | quinclips3 | DR.DENT (US) | 28.800.000 | 10.700 | 170.100 | 5,9 | 0,37 | human-face | Claimed (FastMoss) | FM-DRDENT | Ads-Label; 28d |
| V03 | quinclips3 | DR.DENT (US) | 14.600.000 | 5.500 | 85.600 | 5,9 | 0,38 | human-face | Claimed (FastMoss) | FM-DRDENT | Ads-Label; 28d |
| V04 | demi_does.it | Built Bar Mixed Variety Box (US) | 3.000.000 | 745 | 19.900 | 6,6 | 0,25 | human-face | Claimed (FastMoss) | FM-BUILT | 28d bis 26.06.2026; 162 s |
| V05 | lorienwright | Built Bar (US) | 598.000 | 549 | 15.317 | 25,6 | 0,92 | unknown (Creator mit Gesicht im Profil) | Claimed/Estimated GMV | FM-BUILT | GMV = 549 x 27,9 USD (SKU-Mittel 28d) |
| V06 | n/a (MREGB-Video 1, Kalodata-Tag AI+AD) | MREGB Socket Fan Light (US) | 739.780 | 3.160 | 82.130 | 111,0 | 4,27 | AI (Kalodata-Label) + Ad | Claimed (Kalodata-Screenshot) | KALO-AI | 18.06.-19.07.2026; 40 s |
| V07 | n/a (MREGB-Video 2) | MREGB Socket Fan Light (US) | 478.030 | 2.290 | 65.120 | 136,2 | 4,79 | unknown | Claimed (Kalodata-Screenshot) | KALO-AI | 24 s |
| V08 | n/a (MREGB-Video 3, Kalodata-Tag AI) | MREGB Socket Fan Light (US) | 1.920.000 | 883 | 22.950 | 12,0 | 0,46 | AI (Kalodata-Label) | Claimed (Kalodata-Screenshot) | KALO-AI | 30 s |
| V09 | n/a (Dog Car Seat Cover) | Dog Car Seat Cover (US) | 827.480 | 734 | 96.770 | 116,9 | 0,89 | UGC-Stil, KI unklar | Claimed (Kalodata-Screenshot) | KALO-AI | 57 % Ad-Views, 80 % Ad-Umsatz, Ad-Spend 33,56k, ROAS 2,31 |
| V10 | simplysammyk | Fußmassagegerät (US) | 14.500.000 | 6.000 | 496.800 | 34,3 | 0,41 | human-face | Claimed (EchoTik-Schaetzung) | ET-FOOT | 2023; GMV = 6.000 x 82,8 USD (Produkt-GMV/Units) |
| V11 | grantsdealz | Fanttik Powerstation (US) | 3.700.000 | 411 | 62.000 | 16,8 | 0,11 | F (hands-only, Kanal-Format heute) | Claimed (EchoTik) | ET-FANTTIK | 2023 |
| V12 | callmebelly | Buerostuhl (US) | 105.500 | 108 | 4.380 | 41,5 | 1,02 | unknown (Food/Travel-Creator) | Claimed (EchoTik) | ET-FURN | 2023 |
| V13 | callmecollins.hdc | Homelikas Akku-Sauger (US) | 520.000 | 186 | 15.808 | 30,4 | 0,36 | human-face | Claimed/Estimated GMV | ET-HOMELIKAS | 2023/24; Preis 84,99 |
| V14 | furniturebyfara | Homelikas (US) | 30.000 | 99 | 8.414 | 280,5 | 3,30 | human-face (Unboxing) | Claimed/Estimated GMV | ET-HOMELIKAS | 2023/24 |
| V15 | Kiani (Handle n/a) | UnciaActive Yoga-Set (US) | 1.800.000 | 2.000 | n/a | n/a | 1,11 | human-face (Try-on) | Claimed (EchoTik) | ET-YOGA | 2026; Preis nicht genannt |
| V16 | Derek Kumo-Beispiel (Handle n/a) | Kfz-Ladegeraet (US) | 9.000.000 | n/a | 245.000 | 27,2 | n/a | F (faceless, human) | Claimed (YouTube) | YT-KUMO | 2024 |
| V17 | Derek Kumo-Beispiel | Luftreiniger (US) | 8.480.000 | n/a | 317.000 | 37,4 | n/a | F (faceless, human) | Claimed (YouTube) | YT-KUMO | 2024 |
| V18 | Derek Kumo-Beispiel | Fanttik Akkuschrauber (US) | 3.380.000 | n/a | 181.000 | 53,6 | n/a | F (faceless, human) | Claimed (YouTube) | YT-KUMO | 2024 |
| V19 | Healthy Smart Deals (Seller) | Supplement (US) | 1.600.000 | n/a | 23.180 | 14,5 | n/a | KI-Content (laut Kurs-Video) | Claimed (YouTube/Kalodata-Screen) | YT-HSD | GMV-Max-Ads |
| V20 | Harry Chang (Kunde/Kurs) | Rosabella-Supplement (US) | 1.300.000 | n/a | 67.420 | 51,9 | n/a | A/B KI (Veo3/HeyGen) | Claimed (404 Media/YouTube) | 404 | Video geloescht |
| V21 | tkay-Kunde | n/a (US) | 643.000 | n/a | 70.000 | 108,9 | n/a | KI (Veo3-Avatar) | Claimed (YouTube) | YT-TKAY |  |
| V22 | tkay-Kunde | n/a (US) | 130.000 | 582 | 10.500 | 80,8 | 4,48 | KI | Claimed (YouTube) | YT-TKAY |  |
| V23 | Reddit-Seller (Burner-Accounts) | n/a (US) | 1.300.000 | n/a | 11.400 | 8,8 | n/a | human (Handy) | Claimed (Reddit) | RD-HYB |  |
| V24 | Reddit r/passive_income | Bettgestell u.a. (US) | 100.000 | n/a | 10.000 | 100,0 | n/a | KI-Videos aus Programm | Claimed (Reddit) | RD-PI |  |
| V25 | Patryk Marketer | n/a (Sora 2) | 310.000 | 39 | 1.300 | 4,2 | 0,13 | A/B KI (Sora 2) | Dashboard gesehen (YouTube) | YT-PATRYK |  |
| V26 | Reddit r/TikTokshop | n/a | 41.000 | 87 | n/a | n/a | 2,12 | human (Handy) | Claimed (Reddit) | RD-41K |  |
| V27 | Reddit r/TikTokshop | n/a | 900.000 | 0 | 0 | 0,0 | 0,00 | Trend-Video | Claimed (Reddit) | RD-900K |  |
| V28 | healthiswealthfyp (tommycetty) | Goli Beetroot (US) | 226.000 | n/a | 7.232 | 32,0 | n/a | A (KI-Oma) | Claimed (YouTube) | YT-TOMMY | GMV = 32 USD/1k Claim |
Zusätzliche Aggregat-Punkte (keine Einzelvideos, aber Per-View-Ökonomie):

| Fall | Views | Ergebnis | GPM (USD/1k) | Tag | Quelle |
|---|---|---|---|---|---|
| Built Bar Hero-SKU, bezahlte Placements 28 d (857 Creatives) | 4,0 Mio. | 107.100 USD Ad-GMV bei 22.400 USD geschätztem Ad-Spend (ROAS 4,78) | 26,8 (Estimated) | Claimed (FastMoss) | FM-BUILT |
| Built Bar Top-Ad-Video „super brand day deals“ (27 s) | n/a | 327 Units, 8.700 USD, ROAS 4,73 | n/a | Claimed (FastMoss) | FM-BUILT |
| Portland Leather Affiliate-Blitz (≈ 500 Creator) | 13 Mio. auf 3.800 Videos (Ø 3.421 Views/Video, Estimated) | „> 1 Mio. USD Umsatz in 20 Tagen“ (Gesamtshop, nicht nur diese Videos) | ≤ 77 (Obergrenze, Estimated) | Claimed (Modern Retail) | MR-PLG |
| NeoCell Top-Creator (kumuliert) | n/a | Drew Review 30,7k Units / 941,6k USD, Video-GPM 33,4; Veronica 27,4k / 847,5k, GPM 46,3; FrancoPluma 19,8k / 614,2k, GPM 47,6 | 33–48 | Claimed (FastMoss) | FM-NEOCELL |
| Pickle-Jar-Sweatshirt (2023; 103 Videos, 30 Tage) | 1,5 Mio. | 2,105 Items/1k, GPM 98,61 | 98,6 | Claimed (EchoTik) | ET-PICKLE |
| COSRX (2023; 278 Videos, 30 Tage, Ø 131.600 Plays) | ≈ 36,6 Mio. (Estimated) | GPM 51,41 | 51,4 | Claimed (EchoTik) | ET-COSRX |
| Dragon-Egg-Toys (2023/24; 51 Videos + 11 LIVEs) | 33 Mio. „exposures“ | GPM 13,33 | 13,3 | Claimed (EchoTik) | ET-DRAGON |

## 3. Wie häufig sind 1M+-Videos mit 1.000+ Bestellungen, und welche GPM haben sie?

- In der Stichprobe haben **14 Videos ≥ 1 Mio. Views**. Davon mit belegter Bestellzahl ≥ 1.000: **V01–V03 (Ayden, 27.300 / 10.700 / 5.500), V10 (simplysammyk, ≈ 6.000), V15 (Kiani, ≈ 2.000)** = 5. Unter 1.000 trotz 1M+: V04 (745), V08 (883), V11 (411). Bei V16–V20/V23 ist nur GMV bekannt; bei plausiblen AOV von 25–40 USD lägen V16/V17/V18/V20 über 1.000 Bestellungen (Estimated, z. B. V17: 317.000 / 40 ≈ 7.900).
- **GPM der 1M+-Videos:** Median **14,5 USD** (n = 13 mit GMV), Spanne 5,3 (Ayden, 15,75-USD-Strips) bis 53,6 (Kumo-Akkuschrauber). **Bestellungen/1k:** Median **0,37** (n = 8), Spanne 0,11–1,11.
- **Basisrate:** Aus öffentlichen Quellen **nicht bestimmbar** – die Artikel zeigen nur Gewinner. Hinweise auf Seltenheit (Estimated/Claimed): Built Bar hat 63.900 shoppable Videos; das beste Video der 28 Tage (3,0 Mio. Views) schaffte 745 Units – also **kein** 1.000+-Video im Fenster. MREGB: 190 Video/Ad-Einträge in 30 Tagen; die zwei 1.000+-Unit-Videos hatten **weniger** als 1 Mio. Views (740k / 478k), das 1,92-Mio.-Video nur 883. DR.DENT: 3.800 Affiliates, aber die drei Top-Videos eines einzigen Creators machten 685.000 USD (≈ 9 % des Januar-GMV von 7,5 Mio.).
- Fazit: 1M+ **und** 1.000+ Bestellungen kommt pro Top-Produkt und Monat **eine Handvoll Mal** vor, konzentriert auf wenige Creator, meist mit Marken-Ad-Budget. 1.000+ Bestellungen gibt es auch ohne 1 Mio. Views, wenn das Produkt stark konvertiert (MREGB 4,3–4,8 Best./1k).

## 4. Fällt oder steigt die Konversion pro View mit der Viralität?

| Stichprobe | n | Spearman(Views, GPM) | Spearman(Views, Best./1k) | Lesart |
|---|---|---|---|---|
| Plattform-Videos (FastMoss/Kalodata/EchoTik) | 14 / 15 | **−0,82** | **−0,68** | stark fallend |
| alle 28 Videos (inkl. Claimed) | 26 | −0,52 | – | fallend |
| Net-Influencer-Top-10, Creator-Monate | 70 / 49 | −0,85 | −0,24 | GPM fallend, Items/1k kaum |
| Innerhalb Ayden (3 Videos, gleiches Produkt) | 3 | – | 0,33 → 0,37 → 0,38 bei 81,5 → 28,8 → 14,6 Mio. | **nahezu konstant** |
| Innerhalb MREGB (3 Videos, gleicher Zeitraum) | 3 | – | 4,79 (478k) / 4,27 (740k) / 0,46 (1,92 Mio.) | fallend |

Einschränkungen: (a) Alle Stichproben sind nach GMV/Units **selektiert** (Top-Listen); bei fast gleicher GMV (Net-Influencer-Top-10: 0,87–4,87 Mio. USD) ist GPM ≈ 1/Views **mechanisch**; (b) die viralsten Videos gehören zu billigen Impuls-Produkten (Strips 15,75 USD, Snacks 27,9 USD) oder Entertainment-Formaten. Belastbar ist: **Mega-Viralität bringt keine proportional höheren Käufe; die GPM der 10M+-Videos liegt bei 5–6 USD (DR.DENT) bis 34 USD (Fußmassagegerät)**, während 100k–800k-Videos mit Problem-Lösungs-Produkten 30–136 USD erreichen. Innerhalb eines erfolgreichen Creatives skaliert die Konversion aber etwa linear mit den (auch bezahlten) Views – deshalb lohnt sich für Marken das Boosten.

## 5. Format der Winner-Videos

| Format | Videos (IDs) | Anteil (n = 28) | Bemerkung |
|---|---|---|---|
| human-face (echte Person vor der Kamera) | V01–V04, V10, V13, V14, V15 (+ vermutlich V05, V12) | 8–10 | alle Plattform-Winner mit ≥ 5.000 Bestellungen sind human-face (Ayden Selfie-Demo, simplysammyk Krankenschwester-Demo) |
| F – faceless/hands-only, menschlich | V11, V16–V18, V23, V26 | 6 | @grantsdealz heute: Hände + Produkt, Skripttitel-Schema „POV: You finally found …“, 7.403 Videos |
| KI-markiert/KI (A/B/G/unklar) | V06, V08 (Kalodata-„AI“), V19, V20, V21, V22, V24, V25, V28 | 9 | nur V06/V08 mit Plattformdaten; Rest Claimed von Kursanbietern/Reddit; Handles überwiegend nicht prüfbar |
| unklar | V07, V09, V27 | 3 | V09 „UGC-Stil“ im Artikel eines KI-Tool-Verkäufers |

Befund: Die **großen, plattformbelegten** Winner (≥ 5.000 Bestellungen) sind ausnahmslos **human-face**. KI-markierte Winner existieren (V06: 3.160 Items), sind aber kleiner, nicht einem prüfbaren Account zuordenbar und stark ad-gestützt. Das stützt C1 (virtuelle KI-Influencer) weiterhin, relativiert aber C3: „KI-Creative als Produktdemo“ (Kategorie G/C/D) kann einzelne vierstellige Bestellzahlen erreichen.

Format-Prüfung per `tt_media.py` (Kontaktbögen gelesen):
- @quinclips3, Video 7602038446722436382: junger Mann, Selfie vor Betonwand, schneidet/klebt Strip, zeigt lila Zähne, wischt ab, Vorher-Nachher unten/oben; ASR-Transkript = eigene Stimme („So these are the only ones that I could afford that actually work for me“). **human-face**, kein KI-Label (IsAigc false).
- @grantsdealz, Video 7689334150179933454 (neu, 3 Plays): Hand hält Parfum-Karton/Flakon im Wohnzimmer, Textbanner oben, Ton −11,8 dB „original sound“ ohne ASR. **F (hands-only)**; Stimme unbekannt.
- @drew.review, Video 7592733868550114574 (Astaxanthin, 7,3 Mio. Plays): Frau vor Kamera + Folien/Review-Screenshots. **human-face** (Wissens-Explainer).

## 6. Implikation für die Hypothese „200 Videos → 1 Video mit 2 Mio. Views → 1.200 Verkäufe → 8.400 EUR Provision“

Implizit: 0,6 Best./1k; 8.400 EUR / 1.200 = 7 EUR = 7,61 USD Provision pro Verkauf ⇒ AOV × Satz = 7,61 USD (z. B. 30 USD × 25 % oder 51 USD × 15 %) ⇒ GPM 18–30 USD.

| Szenario für ein 2-Mio.-Video (Estimated) | Bestellungen | Provision USD | Provision EUR (× 0,92) | nach 10 % Retouren |
|---|---|---|---|---|
| Ayden-Ökonomie (0,335/1k; 15,75 USD × 15 % = 2,36 USD) | 670 | 1.584 | 1.457 | 1.311 |
| Median 1M+ (0,37/1k) × DR.DENT-Satz 2,36 USD | 740 | 1.748 | 1.608 | 1.447 |
| Median 1M+ × Built-Bar-Satz (27,9 × 15 % = 4,19 USD) | 740 | 3.097 | 2.849 | 2.564 |
| Median 1M+ × Supplement (30 × 25 % = 7,50 USD) | 740 | 5.550 | 5.106 | 4.595 |
| GPM-Median 1M+ (14,5 USD) × 15 % / × 25 % | – | 4.350 / 7.250 | 4.002 / 6.670 | 3.602 / 6.003 |
| Hypothese (0,6/1k × 7,61 USD) | 1.200 | 9.130 | 8.400 | 7.560 |
| Bestfall Kiani-Rate (1,11/1k) × 7,50 USD | 2.220 | 16.650 | 15.318 | 13.786 |

Bewertung:
- **Pro Winner-Video** ist 8.400 EUR bei 2 Mio. Views **optimistisch, aber nicht unmöglich** (benötigt obere Hälfte der Konversion und ein 25-%-Supplement oder ≥ 50-USD-Produkt). Mit Median-Werten eher **1.500–5.100 EUR**.
- **Die Frequenz „1 von 200“** ist nur für einen etablierten Top-Creator belegt: Ayden hat ≥ 5 Videos mit ≥ 2 Mio. Plays (165,9 Mio.; 51,6 Mio.; ≈ 28,8 Mio.; ≈ 14,6 Mio.; 2,7 Mio.) bei 801 Videos ≈ **1 von 160** (Verified Zählung Untergrenze, Survivorship-Fall). Für neue Accounts und KI-Accounts zeigt der Vorbericht Median-Views < 1.000; dafür gibt es keinen Gegenbeleg.
- **Tail-Effekt:** Wenn ein Video tatsächlich gewinnt, bleibt es selten bei 2 Mio. – Marken boosten Gewinner (Ayden-Video 81,5 Mio. Views in 28 Tagen). Bedingter Erwartungswert eines echten Winners ist daher **höher** als 8.400 EUR; der unbedingte Erwartungswert pro 200 Videos hängt fast vollständig an der (unbekannten) Trefferquote.
- Gewinner verblassen: Aydens aktuelle Videos 1.764–3.034 Plays (Verified, 12.–13.09.2026); @grantsdealz aktuell 17–629 Plays pro Video (Verified, 24.–25.09.2026) trotz früherem 3,7-Mio.-Winner und Bio-Claim „15M GMV on TikTok shop“.

## 7. Einordnung gegen C1–C7

| Claim | Befund aus diesem Winkel | Richtung |
|---|---|---|
| C1 (virtuelle KI-Influencer funktionieren praktisch nicht) | Kein virtueller Influencer unter den plattformbelegten Winnern. | stützt |
| C2 (virale KI-Shop-Accounts = kurzlebige Supplement-Netzwerke) | V19/V20/V28 sind Supplements mit Ads bzw. gelöscht; MREGB (Haushalt) ist Gegenbeispiel, aber Account unbekannt. | überwiegend stützt, leicht relativiert |
| C3 (dauerhafte vierstellige Provisionen mit KI selten) | MREGB-KI-Video: 82.130 USD GMV in < 3 Wochen (bei 10–15 % wären 8.200–12.300 USD Provision, Estimated; Satz unbekannt). Dauer nicht belegt. | relativiert (medium/weak) |
| C4 (10.000+-USD-Claims v. a. von Kursverkäufern) | Ayden (human-face) Feb 2026: 871.990 USD GMV ⇒ ≈ 130.800 USD Provision (Estimated). Echte Creator-Einkommen > 10k existieren – aber nicht KI. | widerlegt für „Creator allgemein“, nicht für KI |
| C5 (realistisches Konto ≈ 1.650 EUR/Monat) | Modell nutzt GPM 30,4; Top-10-Creator-Median 24,9, Mega-Virals 5–15 ⇒ GPM-Annahme eher optimistisch. Aber: Modell ignoriert Marken-Ad-Verstärkung (Fat Tail). | GPM stützt; Tail widerspricht |
| C6/C7 (830 / 1.650 Videos für 10k/20k EUR) | Ayden: ≈ 35–49 Videos/Monat (801 Videos seit Kontoanlage 25.10.2024 bzw. Shop-Debüt Mai 2025 laut Net Influencer) und sechsstelliger Monats-GMV – Menge ist nicht der einzige Weg. Aber Einzelfall, human-face. | relativiert |

## 8. Verifikation (Selbstprüfung der 3 stärksten Gegenbefunde)

### Verifikation F1 – @quinclips3 (Ayden), DR.DENT-Winner (human-face)
- Quelle erneut geöffnet: FastMoss-Blog DR.DENT (Tabelle als Bild `66848e17-…png`, visuell gelesen): Zeile 1 „Veneers who #whiteningstri…“, 00:00:45, **27,3k Units, 430,0k USD GMV, 81,5 Mio. Views**, 991,5k Likes, veröffentlicht 2026-02-02, „Ads“-Badge; Zeile 2 „This is crazy…“ 1:16, 10,7k / 170,1k / 28,8 Mio. (2026-02-03); Zeile 3 „Veneers who ???“ 1:21, 5,5k / 85,6k / 14,6 Mio. (2026-02-15). Zeitraum „last 28 days“, Provision 15 % laut Text.
- Handle: FastMoss-Influencerseite 7429520051840271403 trägt den Titel „Ayden (@quinclips3)“.
- TikTok (Verified, 2026-09-25): Profil 98.500 Follower, 6,6 Mio. Likes, 801 Videos, angelegt 25.10.2024, kein Seller-Konto, Bio „Paid collabs>…“. Video 7602038446722436382: 165,9 Mio. Plays, 2,0 Mio. Likes, 14.200 Kommentare, 45 s, erstellt 01.02.2026 (UTC; FastMoss 02.02.), Beschreibung „Veneers who #whiteningstripes #drdent …“, Produkt-Anchor Typ 35, IsAigc false. Weitere DR.DENT-Videos: 7611765800403324190 (51,6 Mio. Plays, 28.02.2026), 7616472711530925342 (2,7 Mio., 12.03.2026). Aktuelle Videos (4 geprüft, 12.–13.09.2026): 1.764–3.034 Plays.
- Format (`tt_media.py`, Kontaktbogen gelesen): Selfie, echtes Gesicht, echte Anwendung, eigene Stimme → **human-face**, kein KI-Anteil erkennbar.
- Zweitquelle: Net Influencer Feb 2026: Platz 9, **871.990 USD** Umsatz, **185,89 Mio. Content-Views**, Ø Stückpreis 15,45 USD, 64,4k Follower.
- Arithmetik: 430.000 / 81.500.000 × 1.000 = **5,28 USD GPM**; 27.300 / 81.500 = **0,335 Units/1k**; Provision 15 % × 430.000 = **64.500 USD** (Estimated), nach 10 % Retouren ≈ 58.000 USD ≈ 53.400 EUR. Februar: 871.990 × 15 % = **130.800 USD** (Estimated); GPM 871.990 / 185.890 = 4,69 – konsistent mit dem Video.
- Metrik-Typ: GMV (Plattformschätzung), nicht Provision; Provision ist Estimated. Offene Punkte: „Ads“-Badge ⇒ ein Teil der Views wurde von der Marke bezahlt; ob die Provision auf Ad-GMV mit 15 % oder einem gesonderten Ads-Satz lief, ist **nicht öffentlich verifizierbar**. TikToks `isAd`-Feld ist bei allen geprüften Ayden- und Demi-Videos true (auch bei 2k-View-Videos), ist also kein Beleg für Paid Reach.
- Bias: FastMoss verkauft Abos (Rabattcode im Artikel), hat aber kein Interesse an erfundenen Handles; Net Influencer ist Branchenmedium.
- **Verdict: CONFIRMED** (Views/GMV als Analyseplattform-Schätzung aus zwei Quellen, Video und Format auf TikTok verifiziert). Kategorie **human-face** – widerspricht C4/C6/C7 als Aussage über Creator-Ökonomie, **nicht** C1–C3 (kein KI-Fall).

### Verifikation F2 – KI-markierte MREGB-Socket-Fan-Light-Videos (Kalodata)
- Quelle erneut geöffnet (r.jina.ai-Abruf, veröffentlicht 23.07.2026) und Screenshot „Video & Ad (190 items)“ 18.06.–19.07.2026 visuell gelesen: Video 1 „Flimsy desk fans only blow tiny areas…“, Badges **AI** + **AD**, 40 s, **82,13k USD, 739,78k Views, 3,16k Items**, 29.06.2026; Video 2 (ohne Badge) 24 s, 65,12k / 478,03k / 2,29k, 22.06.; Video 3 „Our summer sale is going strong!…“, Badge **AI**, 30 s, 22,95k / **1,92 Mio.** / 883, 01.07.
- Arithmetik: V1 GPM 82.130 / 739,78 = **111,0**; 3.160 / 739,78 = **4,27/1k**; AOV 26,0 USD. V3 GPM **12,0**, 0,46/1k. Provision unbekannt; bei 10–15 % wären V1 ≈ 8.200–12.300 USD (Estimated).
- TikTok-Prüfung: Handle im Screenshot nicht sichtbar; WebSearch nach dem Hook-Text lieferte keinen Treffer → Account/Video **nicht auffindbar**, keine eigene Format-Klassifikation möglich. Bedeutung des Kalodata-„AI“-Badges im Artikel nicht definiert (Artikeltext: „mostly AI-generated content“). Ob Affiliate- oder Seller-Account: unbekannt. V1 trägt „AD“ ⇒ bezahlte Reichweite.
- Bias: Artikel bewirbt Kaloclip (KI-Videogenerator, „one-click posting to up to 100 linked accounts“) – starkes Verkaufsinteresse an KI-Erfolgsgeschichten; zudem zeigt derselbe Screenshot, dass das **viralste KI-Video am schlechtesten konvertierte**.
- **Verdict: PARTIALLY.** Zahlen im Dashboard-Screenshot gesehen, Rechnung korrekt; KI-Kategorie **unknown (KI-markiert, vermutlich G/B – KI-Szene mit echtem Produkt)**, Account und Provision **UNVERIFIABLE**, Dauerhaftigkeit nicht belegt. Relativiert C3 nur schwach.

### Verifikation F3 – Marken-Ad-Verstärkung als Fat Tail, den das organische Modell (C5–C7) nicht abbildet
- Belege erneut geprüft: Ayden-Videos mit FastMoss-„Ads“-Badge (Screenshot); Dog Car Seat Cover (Kalodata-Screenshot): 827,48k Views, 734 Items, 96,77k USD, **Ad View Ratio 57,37 %, Ad Revenue Ratio 80,00 %, Ad Spend 33,56k USD, ROAS 2,31**; Built Bar Hero-SKU (FastMoss-Tabelle FM-31): 50,51 % Ad-Anteil, 4,0 Mio. Views, 857 Creatives, ROAS 4,78 (Ad-Spend von FastMoss geschätzt); Healthy Smart Deals (YouTube-Transkript): „All of them are coming up as ads … GMV Max“.
- Arithmetik Dog Seat: organischer Umsatzanteil 20 % × 96.770 = 19.354 USD; Ad-Spend/Ad-Umsatz = 33.560 / 77.416 = 43 % (Seller-Kosten, nicht Creator-Kosten).
- Einschränkungen: Wer die Ads bezahlt (Marke), ist klar; wie viel Provision der Creator auf Ad-GMV erhält (Standard- vs. Ads-Provisionssatz), ist **nicht öffentlich verifizierbar**. TikTok-`isAd` ist als Indikator unbrauchbar (siehe F1). Die Ad-Verstärkung setzt ein bereits organisch funktionierendes Video voraus – sie erhöht den Tail, nicht die Trefferquote.
- **Verdict: PARTIALLY.** Der Mechanismus ist in drei Plattformquellen belegt und erklärt die 10–80-Mio.-View-Winner; wie viel davon beim Affiliate als Provision ankommt, bleibt offen. Für KI-Accounts gibt es nur Claimed-Belege (Healthy Smart Deals, Seller-Account).

## 9. Quellen (Zugriff 2026-09-25)

- FM-DRDENT: https://www.fastmoss.com/blog/how-dr-dent-dominated-the-tiktok-shop-market-in-january-2026/ (Videotabelle: https://www.fastmoss.com/blog/wp-content/uploads/2026/02/66848e17-1245-418d-af19-0025d7321eb5.png); Handle: https://www.fastmoss.com/influencer/detail/7429520051840271403
- TikTok @quinclips3: https://www.tiktok.com/@quinclips3/video/7602038446722436382 · https://www.tiktok.com/@quinclips3/video/7611765800403324190 · https://www.tiktok.com/@quinclips3/video/7616472711530925342
- FM-BUILT: https://www.fastmoss.com/blog/the-tiktok-shop-protein-bar-playbook-why-built-bar-is-winning/ ; TikTok @demi_does.it (622.900 Follower, 2.418 Videos; das 3,0-Mio.-Video wurde nicht gefunden, geprüft: /video/7640595083598875917 = 220.400 Plays, /video/7662552340465044749 = 40.400 Plays); @lorienwright (6.101 Follower, Bio „TikTok Shop Affiliate“)
- FM-NEOCELL: https://www.fastmoss.com/blog/14m-from-a-single-can-how-neocell-collagen-won-on-tiktok-shop-under-the-2026-protein-surge/ ; TikTok @drew.review (192.200 Follower), /video/7592733868550114574 (7,3 Mio. Plays, human-face)
- FM-Produktlisten: https://www.fastmoss.com/blog/top-selling-products-tiktok-shop-us-q1-2026/ · https://www.fastmoss.com/blog/best-selling-tiktok-shop-products-us-q2-2026/ · https://www.fastmoss.com/blog/what-to-sell-tiktok-shop-q4-2026/ (PetPivot, Rhino, Nex Playground, EcoFlow, Goli, Toplux, medicube – nur Produktsummen) · https://www.fastmoss.com/blog/tiktok-shop-europe-top-products-april-2026/ (GreatVita DE: 22.910 Orders / 261.861 USD im April 2026, keine Videodaten)
- KALO-AI: https://www.kalodata.com/blog/ecommerce/how-tiktok-shop-sellers-are-using-ai-tools-to-redefine-growth/ (Screenshots …/2026/07/%E4%B8%8B%E8%BD%BD-3-1024x425.png und …%E4%B8%8B%E8%BD%BD-12-1024x326.png)
- ET-FOOT: https://www.echotik.live/blog/home-wellness-has-become-a-fashion-trend-foot-massagers-on-tiktok-us-generated-dollar13-million-gmv-in-30-days-or-echotik-product-insight-clqd76tra84131wo7uhsfucqk/
- ET-FANTTIK: https://www.echotik.live/blog/gmv-4-million-usd-outdoor-tools-and-power-station-brand-fanttik-ranks-top-4-in-tiktokshop-us-ranking-list-road-trips-become-popular-topic-in-north-america-or-echotik-product-insights-clqx6t6hu51701wpeguegs11x/
- ET-FURN: https://www.echotik.live/blog/single-week-gmv-around-dollar15-million-the-first-hot-selling-furniture-store-emerging-on-tiktok-shop-us-a-promising-start-for-cross-border-furniture-brands-going-international-or-echotik-product-selection-insights-closddzvk1117551vmebc3wzsgc/
- ET-HOMELIKAS: https://www.echotik.live/blog/homelikas-tiktok-success-dollar10m-gmv-in-2-months-clr5rnsxo35011vm9ccz3v19a/
- ET-YOGA: https://www.echotik.live/blog/case-study-how-viral-tiktok-yogawear-hit-66m-sales-in-7-days-2026-trends/
- ET-PICKLE / ET-COSRX / ET-DRAGON: siehe `ptv/et/index.txt` (EchoTik-Produkt-Insights 2023/24)
- Net Influencer Top-10 (Nov 2025–Aug 2026): URLs in `research/redteam/ni/urls.txt`, z. B. https://www.netinfluencer.com/top-10-independent-tiktok-creators-who-generated-the-most-sales-in-february-2026/
- MR-PLG: https://www.modernretail.co/marketing/how-portland-leather-goods-did-1m-in-sales-in-20-days-on-tiktok-shop-thanks-to-an-affiliate-blitz/ (via Suchergebnis-Snippet)
- YT-KUMO https://www.youtube.com/watch?v=90MZx-l7mSI · YT-HSD https://www.youtube.com/watch?v=b7POUuz16xc · 404: https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/ · YT-TKAY https://www.youtube.com/watch?v=M7t2WRgOJWg · RD-PI https://www.reddit.com/r/passive_income/comments/1u9s0zn/ · RD-HYB https://www.reddit.com/r/FacebookAds/comments/1q1l1ua/ · RD-41K https://www.reddit.com/r/TikTokshop/comments/1qhvmg4/ · RD-900K https://www.reddit.com/r/TikTokshop/comments/1w4rfxc/ · YT-PATRYK/YT-TOMMY: siehe `quellen/claims_youtube.md` des Vorberichts
- TikTok-Profile (Verified 2026-09-25): @grantsdealz 204.400 Follower, 7.403 Videos, Bio „15M GMV on TikTok shop“ (Claimed); @simplysammyk 60.800 (RN-BSN); @callmebelly 1,6 Mio.; @callmecollins.hdc 691.200; @furniturebyfara 454.600.

## Anhang A – Net Influencer Top-10 unabhängige US-Creator, Creator-Monate mit Views (n = 70, sortiert nach Views)

GMV und Content-Views laut Net Influencer (Claimed); GPM und Items/1k Estimated (Items teils aus GMV / Ø-Stückpreis). „Content-Views“ enthalten auch Nicht-Shop-Videos → echte Shop-GPM eher höher.

| Monat | Creator | GMV (USD) | Content-Views | GPM (USD/1k) | Items/1k Views |
|---|---|---|---|---|---|
| 2025-12 | @mikaylanogueira | 1.730.000 | 326.990.000 | 5,3 | n/a |
| 2026-06 | @myfamilypov | 2.560.000 | 195.730.000 | 13,1 | n/a |
| 2026-02 | @quinclips3 | 871.990 | 185.890.000 | 4,7 | 0,30 |
| 2025-12 | @myfamilypov | 2.000.000 | 155.040.000 | 12,9 | n/a |
| 2026-01 | @prettypickedd | 1.050.000 | 134.180.000 | 7,8 | 0,24 |
| 2026-06 | @natiscart | 1.440.000 | 127.190.000 | 11,3 | 0,61 |
| 2026-01 | @kid.shops | 907.200 | 124.280.000 | 7,3 | 0,18 |
| 2025-12 | @trending_ttok | 1.920.000 | 120.270.000 | 16,0 | n/a |
| 2026-08 | @myfamilypov | 1.780.000 | 100.010.000 | 17,8 | 0,48 |
| 2025-12 | @hannahbentley | 2.370.000 | 97.720.000 | 24,3 | n/a |
| 2026-02 | @myfamilypov | 918.590 | 96.370.000 | 9,5 | n/a |
| 2026-05 | @myfamilypov | 1.320.000 | 93.960.000 | 14,0 | 0,42 |
| 2026-05 | @jordantheodore | 1.820.000 | 93.960.000 | 19,4 | 0,10 |
| 2026-08 | @trending_ttok | 3.370.000 | 90.700.000 | 37,2 | n/a |
| 2025-12 | @dealswithty | 2.720.000 | 86.650.000 | 31,4 | n/a |
| 2026-08 | @huntergrazianoo | 1.040.000 | 79.140.000 | 13,1 | 0,60 |
| 2026-01 | @trending_ttok | 1.000.000 | 74.940.000 | 13,3 | 0,33 |
| 2026-01 | @anniedanner | 1.230.000 | 74.930.000 | 16,4 | 0,78 |
| 2025-11 | @trending_ttok | 1.560.000 | 72.950.000 | 21,4 | n/a |
| 2026-02 | @hannahbentley | 1.370.000 | 71.090.000 | 19,3 | 0,32 |
| 2026-02 | @prettypickedd | 919.690 | 69.460.000 | 13,2 | n/a |
| 2026-08 | @torijflow | 1.330.000 | 69.060.000 | 19,3 | 0,53 |
| 2026-06 | @trending_ttok | 1.970.000 | 63.410.000 | 31,1 | 0,38 |
| 2025-12 | @anniedanner | 1.370.000 | 62.910.000 | 21,8 | n/a |
| 2026-05 | @dealswithty | 1.280.000 | 62.680.000 | 20,4 | 0,15 |
| 2026-06 | @kid.shops | 1.280.000 | 60.660.000 | 21,1 | 0,27 |
| 2026-04 | @trending_ttok | 2.150.000 | 60.570.000 | 35,5 | 0,38 |
| 2026-04 | @dj.foof | 927.700 | 59.850.000 | 15,5 | 0,50 |
| 2026-05 | @trending_ttok | 1.780.000 | 57.670.000 | 30,9 | 0,43 |
| 2026-06 | @dj.foof | 1.200.000 | 55.320.000 | 21,7 | 0,63 |
| 2026-06 | @torijflow | 1.200.000 | 55.210.000 | 21,7 | 0,68 |
| 2026-02 | @sharpafedc | 929.320 | 54.560.000 | 17,0 | 0,28 |
| 2026-06 | @cakedfinds | 1.590.000 | 54.540.000 | 29,2 | 0,57 |
| 2026-02 | @trending_ttok | 1.140.000 | 52.300.000 | 21,8 | 0,36 |
| 2026-04 | @hannahbentley | 1.320.000 | 51.770.000 | 25,5 | 0,36 |
| 2026-08 | @kid.shops | 1.110.000 | 50.200.000 | 22,1 | 0,25 |
| 2026-04 | @torijflow | 863.260 | 48.760.000 | 17,7 | 0,51 |
| 2026-06 | @hannahbentley | 1.320.000 | 47.520.000 | 27,8 | 0,57 |
| 2026-01 | @jordyn_gunderson | 1.110.000 | 47.310.000 | 23,5 | n/a |
| 2026-05 | @kajsa.ziebell | 1.100.000 | 46.670.000 | 23,6 | 0,48 |
| 2026-01 | @hannahbentley | 989.560 | 46.020.000 | 21,5 | 0,34 |
| 2026-08 | @dj.foof | 989.400 | 45.510.000 | 21,7 | 0,63 |
| 2026-01 | @cakedfinds | 1.180.000 | 45.430.000 | 26,0 | 0,49 |
| 2025-12 | @be.lush | 1.750.000 | 45.220.000 | 38,7 | n/a |
| 2026-05 | @hannahbentley | 1.310.000 | 42.060.000 | 31,1 | 0,51 |
| 2026-01 | @dealswithty | 1.200.000 | 41.960.000 | 28,6 | 0,22 |
| 2026-04 | @bestiebriitt | 1.600.000 | 40.710.000 | 39,3 | 0,34 |
| 2025-12 | @sadiejonesuploading | 1.160.000 | 38.810.000 | 29,9 | n/a |
| 2026-02 | @anniedanner | 868.540 | 37.010.000 | 23,5 | n/a |
| 2026-01 | @midlife.nursing | 947.230 | 36.730.000 | 25,8 | 0,42 |
| 2025-12 | @sarahgibbons_ | 1.290.000 | 35.260.000 | 36,6 | n/a |
| 2026-05 | @sophmademebu | 1.060.000 | 34.390.000 | 30,8 | 0,64 |
| 2026-05 | @be.lush | 1.540.000 | 32.450.000 | 47,5 | 0,29 |
| 2026-05 | @cakedfinds | 1.040.000 | 32.260.000 | 32,2 | 0,65 |
| 2026-02 | @cakedfinds | 975.760 | 31.480.000 | 31,0 | n/a |
| 2026-04 | @cakedfinds | 960.660 | 30.950.000 | 31,0 | 0,68 |
| 2026-06 | @be.lush | 1.150.000 | 30.640.000 | 37,5 | 0,38 |
| 2026-06 | @ericsfindss | 1.620.000 | 30.130.000 | 53,8 | 0,21 |
| 2026-02 | @skincarepronikki | 956.630 | 29.550.000 | 32,4 | n/a |
| 2026-08 | @cakedfinds | 1.030.000 | 29.290.000 | 35,2 | 0,63 |
| 2026-05 | @ericsfindss | 1.640.000 | 29.040.000 | 56,5 | 0,21 |
| 2026-04 | @be.lush | 1.690.000 | 28.600.000 | 59,1 | n/a |
| 2026-08 | @bennettfinds | 1.130.000 | 24.050.000 | 47,0 | 0,37 |
| 2026-02 | @therealmustbecindy | 888.540 | 24.010.000 | 37,0 | n/a |
| 2026-04 | @dealswithty | 917.010 | 21.640.000 | 42,4 | 0,30 |
| 2026-04 | @ediedricks_ | 945.600 | 17.460.000 | 54,2 | 0,39 |
| 2025-12 | @highland.fashion7 | 1.830.000 | 16.830.000 | 108,7 | n/a |
| 2026-01 | @highland.fashion7 | 1.010.000 | 12.500.000 | 80,8 | 4,01 |
| 2026-08 | @airgeeksrc | 1.090.000 | 8.070.000 | 135,1 | 0,73 |
| 2026-08 | @kevin.finds | 1.170.000 | 6.880.000 | 170,1 | 1,09 |