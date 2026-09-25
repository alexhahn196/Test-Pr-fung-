# Dossier: @laife_official (LAIFE) – TikTok-Account-Prüfung

Zugriffsdatum aller Quellen: 2026-09-24/25. Legende: **Verified** = direkt in TikTok-Daten/Primärquelle gesehen; **Claimed** = Behauptung Dritter (hier: Tool-Anbieter Creatify); **Estimated** = eigene Rechnung (Formel + Inputs angegeben).

## 1. Stammdaten (Verified, TikTok-SSR-Daten via tt_profile.sh, 2026-09-24)

| Feld | Wert |
|---|---|
| Username | laife_official |
| URL | https://www.tiktok.com/@laife_official |
| Anzeigename | LAIFE |
| Existiert | ja (statusCode 0) |
| Bio | "Graceful aging for everyone. www.laife.us" |
| Verifiziert (blauer Haken) | nein |
| Account erstellt | 2024-09-04 (createTime 1725479975) |
| Follower | 1.237 |
| Likes gesamt | 943 |
| Videos gesamt | 36 |
| Following | 0 |
| ttSeller | **true** |
| commerceUserInfo.commerceUser | false |
| bioLink | keiner (Website nur als Text in der Bio) |
| Land | USA (Shop laife.us in USD; Creatify-Fallstudie beschreibt US-TikTok-Shop) – Region-Feld in TikTok-Daten: null |
| Modelltyp | B/E: Brand-eigener Verkäufer-Account (Marke bewirbt eigene Supplements), kein Affiliate-Creator |
| Nische | Longevity-/Anti-Aging- und Frauengesundheits-Supplements (Ovarevive, Life Shield u. a.) |
| Content-Typ | Talking-Head-UGC-Style-Clips (35–60 s), laut Hersteller-Fallstudie mit Creatify-AI-Avataren produziert; Musik-Feld immer "original sound - LAIFE" |
| Upload-Frequenz | Burst-Phase: 10 Videos in 18 Tagen (21.03.–07.04.2025, ca. 4/Woche). Gesamt: 36 Videos in ca. 7 Monaten aktiver Zeit (Sep 2024–Apr 2025) ≈ 1,2/Woche. **Seit 2025-04-07 kein neues Video (17+ Monate inaktiv).** |

Alternative Handles geprüft: @liioo_kko (in Creatify-Fallstudie genannt) → statusCode 10221 (existiert nicht/privat). @laifeofficial (auf laife.us verlinkt) → statusCode 10221 (existiert nicht). Der einzige auffindbare aktive Account ist @laife_official.

## 2. Video-Stichprobe (n = 10, neueste Videos via Embed-Seite; Verified, tt_video.sh 2026-09-24)

| Video-ID | Datum | Views | Likes | Kommentare | Shares | Dauer | Anchors | AI-Label (aigcLabelType) | isAd | isECVideo | Hashtags |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 7481114569784446254 | 2025-04-07 | 202 | 1 | 0 | 0 | 38 s | CapCut (kein Produkt) | keins | nein | – | pms, periodcramps, womenshealth |
| 7481112073737440558 | 2025-04-04 | 390 | 2 | 0 | 0 | 39 s | CapCut | keins | nein | 1 | beautyfromwithin, wellness, healthytips |
| 7481159792871001390 | 2025-04-02 | 432 | 3 | 0 | 0 | 45 s | CapCut | keins | nein | 1 | menopause, womenshealth |
| 7481158127551876398 | 2025-03-30 | 379 | 2 | 0 | 0 | 50 s | CapCut | keins | nein | 1 | postpartumweightloss, postpartumrecovery, newmom |
| 7481160065819413802 | 2025-03-27 | 60 | 0 | 0 | 0 | 35 s | CapCut | keins | nein | 1 | (ovarian, womenhealth, womenbeauty im Text) |
| 7481159956100599086 | 2025-03-25 | 203 | 1 | 0 | 0 | 37 s | CapCut | keins | nein | – | periodcramps, period, ovarian |
| 7481160099466251566 | 2025-03-23 | 875 | 8 | 1 | 0 | 44 s | CapCut | keins | nein | 1 | womenhealth, antiaging, supplementsforwomen, … |
| 7484123259626343726 | 2025-03-21 | **9.868** | 13 | 1 | 0 | 20 s | keine | keins | **ja** | – | keine |
| 7484123210301066542 | 2025-03-21 | 517 | 2 | 0 | 0 | 60 s | keine | keins | **ja** | – | keine |
| 7481159790153043246 | 2025-03-21 | 122 | 0 | 0 | 0 | 41 s | CapCut | keins | nein | – | beautytips, supplements, supplementsforwomen, ovarian |

Video-URLs: https://www.tiktok.com/@laife_official/video/<ID> (alle 10 IDs oben). Rohdaten: laife_official_raw.jsonl im selben Ordner.

**Kennzahlen der Stichprobe (Verified, berechnet aus n = 10):**
- Durchschnitt: 1.304,8 Views (Summe 13.048 / 10) – stark verzerrt durch das eine als Ad geflaggte Video mit 9.868 Views
- Median: 384,5 Views
- Maximum: 9.868 Views (Video 7484123259626343726, isAd = true → vermutlich bezahlte Reichweite/Spark Ad, nicht organisch)
- Ohne die beiden Ad-Videos: Ø 333 Views, Median 291
- Engagement: 32 Likes auf 13.048 Views = 0,25 %; 2 Kommentare gesamt
- Kein einziges Video trägt ein TikTok-AI-Label (aigcLabelType null, AIGCDescription leer)
- Kein einziges Video hat einen Produkt-Anchor (TikTok-Shop-Link); der einzige Anchor ist der automatische CapCut-Template-Link
- 5 von 10 Videos sind mit isECVideo = 1 geflaggt (TikTok-interne E-Commerce-Kennzeichnung)

## 3. Video-Inhalt / AI-Prüfung

Ein visuelles Watching mit mcp__NexLev__watch_tiktok_video_and_ask war **nicht möglich** (Tageslimit 15/15 erreicht, Fehler "RATE LIMIT EXCEEDED" am 2026-09-25). Die AI-Einschätzung stützt sich daher auf:

1. **Creatify-Fallstudie (Claimed, Anbieter des AI-Avatar-Tools)** – https://creatify.ai/case-study/laife (abgerufen 2026-09-24):
   - Zitat: "Almost all the videos on our TikTok account are made using Creatify."
   - Zitat: "We like Creatify because the characters look more realistic and we have a wider variety to choose from."
   - Zitat: "It helped us successfully get through the cold-start stage of TikTok Shop."
   - Claimed-Kennzahlen: "$3.89 cost per order", "50 videos/week" (vorher 10 pro Kampagne), "200+ videos per month" Creative-Tests, Nutzung von TikTok Shop und GMV Max.
   - Die Fallstudie nennt den Handle @liioo_kko, der nicht existiert; die Zuordnung zu @laife_official erfolgt über Markenname, Bio ("Graceful aging for everyone" = Mission in der Fallstudie) und Produkte.
2. **TikTok-Metadaten (Verified):** Alle 10 Videos nutzen "original sound - LAIFE" (kein Trend-Sound), Beschreibungen im Ich-Erzähl-UGC-Stil ("Three babies later, and I'm on a mission to get my body back!", "My wellness journey changed everything!") – typisch für Avatar-Skripte einer Marke. Kein AI-Label gesetzt.

**Einstufung AI-Level: vermutlich AI** (Anbieter-Claim "fast alle Videos mit Creatify-Avataren", kein visueller Nachweis durch uns, keine TikTok-AI-Kennzeichnung). Hook/CTA/Szenenaufbau: nicht verifizierbar ohne Watching; aus den Captions: Hook-Muster = Problem-Frage ("Think PMS is just part of life?", "Period cramps got me fighting for my life!"), Länge 35–60 s, Produkt-Nennung (Ovarevive) im Text.

## 4. Shop-Aktivität

| Indikator | Befund |
|---|---|
| ttSeller-Flag | **true** (Verified) – Account ist als TikTok-Shop-Verkäufer registriert |
| commerceUser | false |
| Produkt-Anchors in Videos | **keine** in allen 10 Videos (nur CapCut-Anchor) |
| isECVideo | 5/10 Videos = 1 |
| Hashtags #tiktokshop / #tiktokshopfinds | keine |
| Bio | Verweis auf eigenen Shop www.laife.us, kein Showcase-Hinweis |
| Fallstudie | Creatify: TikTok Shop + GMV Max genutzt, "cold-start stage of TikTok Shop" überstanden (Claimed) |
| Website laife.us (Verified, 2026-09-24) | Preise: Ovarevive III $69,99 (UVP $209), Ovarevive II $58,99, Liver Rejuver $69,99, Performax $99,99, Life Shield $29,99, kleinere SKUs $15,99–$29,99. Verlinkt TikTok @laifeofficial (existiert nicht). |

**shop_active = wahrscheinlich**: Verkäuferstatus ist verifiziert und die Marke beschreibt TikTok-Shop-Verkäufe selbst; aktuell aber keine Produktkarten in den Videos sichtbar und der Account ist seit April 2025 inaktiv. Ob der Shop heute noch Umsatz macht, ist nicht öffentlich verifizierbar.

## 5. Einkommens-/GMV-Schätzung

Keine öffentliche Kalodata-/FastMoss-Zahl gefunden (WebSearch-Budget der Session ausgeschöpft; Fallstudie nennt keine GMV). Creatify-Claim "$3.89 cost per order" ist eine Werbekosten-Kennzahl, keine Umsatzangabe.

**Estimated (nur Organik-Reichweite des Accounts, aktive Phase März/April 2025):**
- Monatliche Views = Median 385 Views × 4 Videos/Woche × 4,33 = **≈ 6.700 Views/Monat** (mit Ø 1.305 inkl. Ad-Ausreißer: ≈ 22.600)
- Bestellungen = Views × CTR 2 % × CVR 5 % = 6.700 × 0,001 = **≈ 7 Bestellungen/Monat** (bis ≈ 23 mit Ø-Wert)
- GMV = Bestellungen × typischer Preis $59–70 = **≈ $400–1.600/Monat**
- "Creator-Provision" 10–20 % = **≈ $40–320/Monat** – als Brand-Account fällt keine Affiliate-Provision an; die Marke behält die Produktmarge (unbekannt), zieht aber Werbe- und Tool-Kosten ab.
- **Aktuell (Sep 2026): 0 organische Views/Monat, da seit 17 Monaten keine Uploads → Estimated Einkommen aus diesem Account ≈ $0.**
- Bezahlte GMV-Max-Umsätze der Marke sind nicht öffentlich verifizierbar.

## 6. Warum es (nicht) funktioniert

- **Organisch gescheitert:** 36 Videos, 1.237 Follower, Median 385 Views, 0,25 % Like-Rate, 2 Kommentare in 10 Videos. Die Avatar-Clips erzeugen keine Community-Interaktion.
- **Einziger Ausreißer ist bezahlt:** Das Video mit 9.868 Views ist als Ad geflaggt – Reichweite kam über Werbebudget, nicht über den Algorithmus.
- **Kein Shop-Link in den Videos:** Trotz ttSeller-Status haben die Videos keine Produktkarten; die Conversion muss über Website/Ads laufen, was das organische TikTok-Shop-Modell aushebelt.
- **Fallstudie ≠ Account-Realität:** Die Creatify-Zahlen (50 Videos/Woche, 200+/Monat) passen nicht zu 36 Videos in 7 Monaten auf diesem Account; der in der Fallstudie genannte Handle existiert nicht. Die Fallstudie beschreibt vermutlich Ad-Creatives (GMV Max / Spark Ads), nicht den organischen Feed.
- **Aufgegeben:** Letztes Video 07.04.2025 – die Marke hat den organischen Avatar-Ansatz offenbar eingestellt.
- **Lehre:** AI-Avatar-Massenproduktion für eine Supplement-Marke lieferte hier nur als bezahltes Creative (cost per order) Werte; als organischer Shop-Account ist es ein Negativbeispiel ("low performer" bestätigt).

## 7. Quellen

- https://www.tiktok.com/@laife_official (TikTok SSR-Daten, 2026-09-24)
- https://www.tiktok.com/embed/@laife_official (Video-Liste + Views, 2026-09-24)
- https://www.tiktok.com/@laife_official/video/7484123259626343726 (+ 9 weitere IDs aus Tabelle, 2026-09-24)
- https://creatify.ai/case-study/laife (Claimed, 2026-09-24)
- https://www.laife.us (Produkte/Preise, 2026-09-24)
- Nicht existent geprüft: https://www.tiktok.com/@liioo_kko, https://www.tiktok.com/@laifeofficial (2026-09-24, statusCode 10221)

Datenqualität: **Verified profile+videos** (Profil + 10 Videos mit Metadaten verifiziert; visuelles Watching wegen Tool-Quota nicht möglich).
