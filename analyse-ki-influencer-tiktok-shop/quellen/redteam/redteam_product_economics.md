# Red-Team: Produkt-Ökonomie (Provision × Preis × Nachfrage × Wettbewerb)

Stand: 2026-09-25 (alle Zugriffe an diesem Tag). Rolle: Gegenprüfung des Berichts `analyse-ki-influencer-tiktok-shop/README.md` (C1–C7), Blickwinkel „Gibt es Produkte, deren Ökonomie die pessimistischen Aussagen C3, C5, C6 und C7 kippt?“.
Tags: **Verified** = selbst in TikTok-Rohdaten gesehen (tt_profile/tt_video/tt_media) oder im Primärtext gelesen; **Claimed** = Behauptung Dritter (FastMoss, Kalodata via Net Influencer, Betreiber-Bericht); **Estimated** = eigene Rechnung, Formel steht dabei.
Wechselkurs wie im Ursprungsbericht: **1 USD = 0,92 EUR** (Annahme). „Provision“ = Brutto-Provision vor Retouren, sofern nicht anders vermerkt; GMV ≠ Provision ≠ Gewinn.

---

## 0. Kurzfazit (Red-Team-Sicht)

1. **Beispiel A existiert fast exakt und hat mehr als genug Nachfrage.** Goli Zero Sugar Trio: 25,17 USD × 34 % = 8,56 USD (≈ 7,87 EUR) pro Einheit, **75.240 Einheiten im Mai 2026** (≈ 2.500/Tag), 3.380 Creator (Claimed, Kalodata via Net Influencer). Für 10.000 EUR Provision reichen 42 Verkäufe/Tag = **1,7 % des Produkt-Monatsvolumens** (Estimated). Ähnlich: Dr.Melaxin Collagen Set (8,88 USD/Einheit, 44.630 Einheiten, 2.010 Creator), NeoCell (7,19 USD/Bestellung, ~88.600 Bestellungen/Monat in Q1).
2. **Beispiel B (69 EUR × 25 %) wurde in keiner öffentlichen Rangliste gefunden.** Die nächsten realen Produkte liegen bei 11,5–12,3 EUR pro Verkauf (medicube Gatekeeping Set 72,38 USD × 18 %, Glass Glow Set 89,11 USD × 15 %, Mellow-Sleep-Decke 83,63 USD × 15 %) mit 18.800–27.400 Einheiten/Monat und 3.380–4.550 Creatorn. 10.000 EUR erfordern hier **3–4 % des gesamten Produktvolumens**.
3. **Beispiel C (≈ 30 EUR pro Verkauf) existiert nur als High-Ticket-Produkt mit niedriger Rate oder saisonal.** Nex Playground (≈ 250 USD × 20 % = 46 EUR/Einheit, 27.384 Einheiten im Nov. 2025, 5.875 Creator) – dort genügen **7 Verkäufe/Tag = 0,8 % des Volumens** für 10.000 EUR, aber nur im Q4. Ein „99 EUR × 30 %“-Produkt mit sichtbarem Volumen fand sich nicht (Nicht öffentlich verifizierbar).
4. **Die Nachfrage begrenzt nicht, sondern der Anteil, den ein Creator davon bekommt.** Der Durchschnitts-Creator bekommt 1,4–32 Einheiten je Produkt und Monat. Für 10.000 EUR muss man **47- bis 200-mal so gut sein wie der Durchschnitt**, also zu den Top 0,5–2 % der Creator dieses Produkts gehören. Belegte Verteilung: 38 von 21.365 Affiliates = 80 % des Affiliate-GMV, 99 % ohne Verkauf (Swoveralls/DudeRobe, Claimed); NeoCell-Top-1 = 6,7 % aller Einheiten; DR.DENT-Top-Creator: 3 Videos = 685.000 USD GMV in 28 Tagen (Claimed, FastMoss).
5. **Stärkstes Gegenargument zu C3 (nur für Menschen belegt):** Top-Affiliates von A-Produkten erzielten sechsstellige Provisionen (Estimated aus Claimed-GMV): NeoCell @drew.review1 ≈ 217.000 USD, @vero.sin.filtro ≈ 195.000 USD, @francopluma1 ≈ 141.000 USD (Lebenszeit bis 06.03.2026); DR.DENT @quinclips3 ≈ 103.000 USD in 28 Tagen. **Alle drei geprüften Konten sind human-face** (tt_media geprüft); keines ist KI. Eines davon (FrancoPluma) war nach ca. 4 Monaten faktisch tot (Views 6,8 Mio. → ~1.100–1.900 pro Video, seit April 2026 keine Posts).
6. **C5/C6/C7 sind produktabhängig. Bei den volumenstärksten Produkten sind sie eher großzügig, bei High-AOV-Produkten eher pessimistisch.** Das Modell rechnet mit 4,10 USD Provision pro 1.000 Views. Bei gleicher Conversion ergibt Goli 34 % 6,16 USD (1,5×), Gatekeeping 18 % 9,38 USD (2,3×) und Nex Playground 20 % bei 0,3 Bestellungen/1.000 Views 13,5 USD (3,3×). Dann sinken die für 10.000 EUR Gewinn nötigen Videos von 833 auf etwa 220–520 pro Monat (Estimated). Für PDRN-Balm (15 % × 16 USD) oder Toplux (Aug.: 25 % × 15 USD) ist das Modell dagegen zu optimistisch (0,4–0,8×).
7. **UK/DE:** Beispiele A/B/C existieren dort nicht mit Volumen. Die DE-Top-5 im April 2026 kamen zusammen auf 60.794 Bestellungen und 764.819 USD, bei Ø 13,83 EUR und 5–15 % Provision. Das DE-#1-Produkt zahlt ≈ 1,40 EUR pro Verkauf. 10.000 EUR wären dort 31 % des gesamten Produktvolumens.

**Gesamturteil:** Der Bericht ist bei C5–C7 **nicht grundsätzlich zu pessimistisch**. Er unterschätzt aber die **Produktwahl als Hebel**: Hohe Rate × hoher AOV ergibt 2–3× Provision pro View, und ein Top-Platz bei einem Produkt bringt fünfstellige Monatsprovisionen. Dass KI-Content diesen Top-Platz erreicht, ist in den Produktdaten **nirgends belegt**. Alle geprüften Top-Affiliates der A-Produkte sind echte Menschen vor der Kamera, deren Formate (Testimonial, „Arzt“-Clip, Hautergebnis) nach der AIGC-Policy mit KI nicht erlaubt nachzubauen wären.

---

## 1. Quellenlage und Definitionen

- **Kalodata-Monatsrankings via Net Influencer** (Jan–Aug 2026): Einheiten, Ø-Stückpreis (= Umsatz/Einheiten), Provision, Creator-Zahl („creators promoting“ im Monat) und „creator conversion rate“. Die Definition der Conversion Rate wird im Artikel nicht erklärt. Meine Lesart „Anteil der Creator mit ≥ 1 Verkauf“ ist eine **Annahme**. Kalodata selbst blockt (HTTP 403).
- **FastMoss-Blog** (Q1/Q2 2026 Top 10, Q4-2025-Framework, Black Friday, NeoCell-, DR.DENT- und Built-Bar-Case): Umsatz, Bestellungen, Provision, „linked creators“ (kumuliert am Listing), Top-Affiliates mit GMV. Die Handles wurden über FastMoss-Influencer-IDs aufgelöst (Seitentitel via WebFetch).
- **Provisionssätze schwanken je Quelle und Monat.** Toplux: 30 % (Q1), 25 % (Q2, Aug), 32 % (Mai). Goli: 25 % (FastMoss) bzw. 34 % (Kalodata Mai). Vermutlich Open-Collab- vs. Maximal- oder Targeted-Rate. Tag: **Claimed**.
- Kein sold-Zähler direkt auf TikTok-Produktseiten verifizierbar (Security Check, wie im Ursprungsbericht).

---

## 2. Produkttabelle: Provision pro Verkauf, Nachfrage, Wettbewerb, nötige Verkäufe

Formel (Estimated): Verkäufe/Monat = Ziel-EUR / (Preis × Rate × 0,92). Anteil = Verkäufe für 10k / Einheiten des Produkts im Monat. Vielfaches = Verkäufe für 10k / (Einheiten / Creator). Keine Retouren abgezogen; mit 10 % Retouren sind ~11 % mehr Verkäufe nötig.

| Produkt | Quelle/Periode | Preis/Einheit USD | Prov. | Prov./Verkauf USD (EUR) | Einheiten/Monat (Produkt gesamt) | Creator (Periode) | Ø Einheiten je Creator | Verkäufe/Tag für 3k/5k/10k/20k EUR | Anteil am Monatsvolumen für 10k EUR | Vielfaches Ø-Creator für 10k |
|---|---|---|---|---|---|---|---|---|---|---|
| Goli Zero Sugar Trio | Kalodata/NI, Mai 2026 | 25,17 | 34 % | 8,56 (7,87) | 75.240 | 3.380 | 22,3 | 13/21/42/85 | 1,7 % | 57× |
| Toplux Magnesium 8-in-1 | Kalodata/NI, Mai 2026 | 14,77 | 32 % | 4,73 (4,35) | 187.690 | 5.910 | 31,8 | 23/38/77/153 | 1,2 % | 72× |
| Toplux Magnesium 8-in-1 | Kalodata/NI, Aug 2026 | 15,23 | 25 % | 3,81 (3,50) | 155.090 | n. a. | n. a. | 29/48/95/190 | 1,8 % | n. a. |
| NeoCell Collagen 20 oz | FastMoss Q1 2026 (Bestellungen/3) | 31,24 (je Bestellung) | 23 % | 7,19 (6,61) | ~88.600 | n. a. (40.300 Videos kum.) | n. a. | 15/25/50/101 | 1,7 % | n. a. |
| Dr.Melaxin Collagen Boost Set | Kalodata/NI, Mai 2026 | 59,19 | 15 % | 8,88 (8,17) | 44.630 | 2.010 | 22,2 | 12/20/41/82 | 2,7 % | 55× |
| medicube PDRN Pink Collagen Balm | Kalodata/NI, Jul 2026 | 16,34 | 15 % | 2,45 (2,25) | 188.040 | 8.140 | 23,1 | 44/74/148/296 | 2,4 % | 192× |
| medicube Gatekeeping My Real Age Set | Kalodata/NI, Jul 2026 | 72,38 | 18 % | 13,03 (11,99) | 27.400 | 3.690 | 7,4 | 8/14/28/56 | 3,0 % | 112× |
| medicube Glass Glow Set | Kalodata/NI, Mai 2026 | 89,11 | 15 % | 13,37 (12,30) | 18.840 | 4.550 | 4,1 | 8/14/27/54 | 4,3 % | 196× |
| Mellow Sleep MarshMellow Comforter | Kalodata/NI, Mai 2026 | 83,63 | 15 % | 12,54 (11,54) | 20.450 | 3.380 | 6,1 | 9/14/29/58 | 4,2 % | 143× |
| NuDerma High Frequency Wand | FastMoss Q4 2025 (/3) | 85,49 | 15 % | 12,82 (11,80) | 5.978 | 4.166 (kum.) | 1,4 | 8/14/28/57 | 14,2 % | 591× |
| Rhino USA Ratchet Straps | FastMoss Q4 2025 (/3), GMV/Einheit | 77,17 | 15 % | 11,58 (10,65) | 38.827 | 8.264 (kum.) | 4,7 | 9/16/31/63 | 2,4 % | 200× |
| Nex Playground | FastMoss Nov 2025, GMV/Einheit | 250,57 | 20 % | 50,11 (46,10) | 27.384 | 5.875 (kum.) | 4,7 | 2/4/7/14 | 0,8 % | 47× |
| EcoFlow DELTA 3 | FastMoss Q4 2025 (/3), GMV/Einheit | 335,78 | 6 % | 20,15 (18,54) | 6.766 | 2.586 (kum.) | 2,6 | 5/9/18/36 | 8,0 % | 206× |
| Built Bar Mixed Variety Box | FastMoss 28 T. (30.05.–26.06.2026) | 30,00 | 15 % | 4,50 (4,14) | 7.600 | Shop: 18.800 | n. a. | 24/40/81/161 | 31,8 % | n. a. |
| GreatVita gefriergetr. Erdbeeren (DE #1) | FastMoss Apr 2026 | ~15,2 (≈ 14 EUR) | 10 % | 1,52 (1,40) | 22.910 | n. a. | n. a. | 71/119/238/476 | 31,2 % | n. a. |

Weitere Einzeldaten (alle Claimed):
- Shark IQ Robot (Mai 2026): 291,62 USD, nur **255 Creator**, 2,07 Mio. USD, davon 2,05 Mio. aus Video.
- Shark Matrix Plus (Aug 2026): 663,98 USD, 2.610 Einheiten; Provision nicht genannt, Shark sonst 5 %.
- Comfrt Dreamer Blanket (Aug 2026): 87,94 USD, 25.850 Einheiten; Provision nicht genannt.
- ADDWIN Fascia Ring (Jul 2026): 22,39 USD, 10 %, 1.090 Creator, 79.310 Einheiten.
- MB Voyage Nova Parfum (Jul 2026): 23,03 USD, 17 %, 2.380 Creator.
- Bella Vita Honey Oud (Jul 2026): 19,74 USD, 15 %, 3.560 Creator.
- tarte CC Serum (Jun 2026): 100 USD, 3,11 Mio. USD im Launch-Monat; Provision nicht genannt.

---

## 3. Test der drei Beispielrechnungen

| Beispiel | Verkäufe/Monat (Tag) für 3k / 5k / 10k / 20k EUR | Reales Produkt am nächsten | Existiert mit ≥ 20–40 Verkäufen/Tag *über Affiliates*? | Wie viele teilen? |
|---|---|---|---|---|
| **A** 39 EUR × 20 % = 7,80 | 385 / 641 / **1.282** / 2.564 (12,8 / 21 / **43** / 85) | Goli Trio 7,87 EUR (Mai 2026, 34 %); Dr.Melaxin Set 8,17 EUR (15 %); NeoCell 6,61 EUR (23 %) | **Ja, deutlich.** Goli ~2.500/Tag, Dr.Melaxin ~1.490/Tag, NeoCell ~2.950/Tag (Claimed). Video-Anteil am Umsatz bei NeoCell 86 %, bei DR.DENT 91 %. | Goli 3.380 Creator im Monat (13.681 verknüpft, 110.416 Videos in Q4 2025). Dr.Melaxin-Set 2.010 im Monat (Shop 37.200). NeoCell 40.300 Shoppable Videos. |
| **B** 69 EUR × 25 % = 17,25 | 174 / 290 / **580** / 1.159 (5,8 / 9,7 / **19** / 39) | Kein 25-%-Produkt bei ~69 EUR mit Volumen gefunden. Nächste: Gatekeeping 11,99 EUR (18 %), Glass Glow 12,30 EUR, Mellow 11,54 EUR | Nur bei 11–12 EUR/Verkauf: dort 834–867 Verkäufe/Monat (28–29/Tag) nötig, **3–4,3 % des Produktvolumens**. | 3.380–4.550 Creator. Laut „creator conversion“ verkaufen davon nur 13,9–58 % überhaupt (Annahme zur Definition). |
| **C** 99 EUR × 30 % = 29,70 | 101 / 168 / **337** / 673 (3,4 / 5,6 / **11** / 22) | Nex Playground 46 EUR (20 %, Q4). EcoFlow 18,5 EUR (6 %). Shark-Robot ≈ 30 EUR (bei angenommenen 5 %) | **Nur saisonal oder High-Ticket.** Nex: 27.384 Einheiten im Nov. 2025, ~7 Verkäufe/Tag für 10k (0,8 %). Shark Matrix: 2.610 Einheiten/Monat, 328 Verkäufe wären 12,6 % des gesamten Produkts. „99 EUR × 30 %“ mit Volumen: nicht gefunden. | Nex 5.875, EcoFlow 2.586, Shark IQ nur 255 Creator. Weniger Konkurrenz, aber auch weniger Gesamtvolumen. |

**Lesart:** Die Nachfrage-Hürde (≥ 20–40 Verkäufe/Tag) ist bei A-Produkten trivial und bei B/C-nahen Produkten erreichbar. Die eigentliche Hürde ist **Anteil und Konzentration**. Für 10.000 EUR braucht man 1–4 % des Gesamtvolumens eines Produkts, das sich 2.000–8.000 aktive Creator teilen. Das schaffen nur die obersten ~0,5–2 % der Creator dieses Produkts (siehe 4).

**Gegen-Argument zu A:** FastMoss hat 298 Produkte untersucht. Die **Median-Bestellungen liegen bei ~350, egal ob 10 % oder 20 % Provision** (Claimed, FastMoss Seller-Costs, Juni 2026). Hohe Provision schafft also keine Nachfrage, sondern zieht mehr Creator auf dieselbe Nachfrage. Dazu kommen die Lebenszyklen:
- Toplux-Umsatz fällt seit Juni: 2,91 → 2,67 → 2,36 Mio. USD.
- PDRN-Balm war vier Monate #1 und ist im August ganz aus den Top 10 gefallen.
- Das Dr.Melaxin-Set fällt seit März jeden Monat.
- Laut FastMoss halten nur 6 von 37 Top-20-Produkten alle drei Monate eines Quartals.
Eine 10k-Position auf *einem* Produkt hält typischerweise 2–5 Monate (Estimated aus diesen Verläufen).

---

## 4. Wie viele Affiliates teilen die Nachfrage – und wie ungleich?

| Evidenz | Zahlen | Tag | Bedeutung |
|---|---|---|---|
| Swoveralls/DudeRobe, Betreiber-Feldbericht (Apr–Jul 2026, 12–20 % Provision, Apparel) | 21.365 Affiliates; nur ~1 von 8 postete je ein Shoppable Video; **~99 % ohne Verkauf**; **38 Creator = 80 % des Affiliate-GMV**; **1 Creator ≈ 30 %** | Claimed (Net Influencer, Betreiberbericht) | Extreme Power-Law. Der Median-Affiliate verdient 0. |
| Built Bar Store, 28 Tage (30.05.–26.06.2026) | ~18.800 Affiliates → 30.400 Einheiten / 873.600 USD. **Ø 46 USD GMV ≈ 7 USD Provision je Affiliate** (Estimated, 15 %). Top: Kim & Blaine 69.100 USD GMV (≈ 10.400 USD Provision), Tyler.sandell 62.900 USD (≈ 9.400), Demi Does It 33.600 USD (≈ 5.000) | Claimed / Estimated | Top-3-Affiliates ≈ 19 % des Affiliate-Umsatzes. Mit einem 30-USD-Snack und 15 % sind 9.000–10.000 USD Provision in 28 Tagen möglich, aber nur für die Top-3 von 18.800. |
| NeoCell (Lebenszeit bis 06.03.2026) | 458.900 Einheiten; Top-3: Drew Review 30.700 Einh./941.600 USD, Veronica 27.400/847.500, FrancoPluma 19.800/614.200 = **17 % aller Einheiten**; Video-GPM der Top-3 33–48 USD | Claimed (FastMoss) | Top-1 = 6,7 %. Ein Top-Platz bei einem A-Produkt ist sechsstellig wert (s. 5). |
| DR.DENT (Jan 2026) | 3.800+ Affiliates; Top-Creator „Ayden“ (@quinclips3): **3 Videos = 685.000 USD GMV in 28 Tagen** ≈ 22 % des Januar-GMV (3,1 Mio.) | Claimed (FastMoss) | Wenige virale Videos statt Masse. Widerspricht der Mengenlogik von C6/C7, aber mit einem echten Menschen. |
| Kalodata „creator conversion rate“ (Mai 2026) | PDRN 57,4 % von 5.230, Gatekeeping 58,1 % von 1.030, Glass Glow 13,9 % von 4.550, Mellow 17,25 % von 3.380 | Claimed; Interpretation = Annahme | Unter dieser Annahme verdient ein *verkaufender* Creator im Mittel (Estimated): PDRN ~70 Einh. ≈ 200 USD, Gatekeeping ~42 Einh. ≈ 560 USD, Glass Glow ~30 Einh. ≈ 400 USD, Mellow ~35 Einh. ≈ 440 USD Provision/Monat. |
| Kleine Nischen (World-Cup-Merch, Jun 2026) | FIFA-Mug-Set 60,09 USD, 12 %: 1.985 Einheiten auf **305 Creator** (6,5/Creator, Lebenszeit). Schal-Set: 196 Einheiten auf **320 Creator** (0,6/Creator) | Claimed (FastMoss) | Bei Nischenprodukten reicht die Nachfrage für Creator-Einkommen nicht. |
| Bloom Creatine Gummies (6 Monate) | 1,3 Mio. USD GMV, 4.700 Creator, 82 % via Affiliate-Video → Ø 277 USD GMV je Creator in 6 Monaten | Claimed (FastMoss) | Ø-Creator bei einem bekannten Supplement ≈ 10 USD Provision/Monat (Estimated, Rate ~20–25 % angenommen). |
| Marketplace Pulse (Seller-Seite) | Top 1 % der Seller = 60 % des US-GMV; untere Hälfte = 0,1 % | Claimed (Net Influencer 12.06.2026) | Die Konzentration gilt auch auf Produktebene. |

**Mittelwerte pro Video als Gegencheck zu C5 (Estimated):**
- **Goli, Q4 2025:** 7,38 Mio. USD Umsatz / 110.416 verknüpfte Videos ≈ 67 USD GMV ≈ **16,7 USD Provision je Video** (25 %). Das liegt praktisch auf dem Modellwert von 14,97 EUR ≈ 16,3 USD je Video (C5 „realistisch“). Die Perioden passen nicht exakt: Umsatz nur Q4, Videos kumuliert.
- **NeoCell, Lebenszeit:** 14,0 Mio. × 86 % Video-Anteil / 40.300 Videos ≈ 299 USD GMV ≈ **69 USD Provision je Video**, ohne die Top-3 ≈ 55 USD. Das ist das **3,4- bis 4,2-fache** des Modellwerts.
- **Lesart:** Bei einem Supplement mit 23 % Provision auf dem Höhepunkt lag der *Durchschnitt* aller Videos deutlich über C5. Der Durchschnitt wird allerdings von wenigen Viral-Videos getragen, der Median ist unbekannt (Nicht öffentlich verifizierbar).

---

## 5. Format-Check der Top-Affiliates von A-Produkten (Verified auf TikTok, 2026-09-25)

| Handle | Produkt / Claimed-Leistung | Profil (Verified) | Aktuelle Videos (Verified) | Format (tt_media, Contact Sheet angesehen) | Kategorie | Langlebigkeit |
|---|---|---|---|---|---|---|
| @francopluma1 (FrancoPluma) | NeoCell: 19.800 Einh., 614.200 USD GMV ≈ **141.300 USD Provision** (23 %, Estimated); GPM 47,63 USD | 50.400 Follower, 315 Videos, Konto seit 06/2024, spanischsprachig | 12.12.2025: **6,8 Mio. Plays** (Video 7582860059206634783); 14.01.2026: 4,4 Mio.; 13.01.2026: 1,7 Mio.; April 2026 (NMN): 1.149–1.886 Plays; **kein neueres Video** | Mann spricht in die Kamera, hält die NeoCell-Dose, blendet einen „Arzt“-Clip ein (Stitch/Green Screen). Testimonial mit Heilversprechen („Falten, Flecken, Haarausfall weg“). IsAigc = false | **human-face** | ~4 Monate Boom, danach Reichweiten-Kollaps / inaktiv |
| @vero.sin.filtro („Veronica“) | NeoCell: 27.400 Einh., 847.500 USD GMV ≈ **194.900 USD Provision** (Estimated) | 39.000 Follower, 1.621 Videos, Konto seit 05/2025, „53 y brillando“, spanisch | Sept. 2026: 22–1.041 Plays/Post, mehrere Posts/Tag, auch Foto-Slideshows (duration 0) | Frau vor der Kamera, Make-up-Anwendung (tarte-CC-Serum), spricht selbst. IsAigc = false | **human-face** | Konto aktiv, Reichweite aktuell niedrig |
| @quinclips3 („Ayden“) | DR.DENT: 3 Videos = 685.000 USD GMV in 28 T. ≈ **102.750 USD Provision** (15 %, Estimated) | 98.500 Follower, 801 Videos, Konto seit 10/2024 | 12.–13.09.2026: 10 Videos in 2 Tagen, 1.565–9.508 Plays, alle isECVideo = 1 | Zwei junge Männer im Restaurant, Dialog-Sketch („Du isst ja kaum was?“ → Produkt). IsAigc = false | **human-face** (Skit) | Konto aktiv. Heute Masse mit wenigen Tausend Views pro Video, also genau das C5-Profil. |
| @drew.review1 („Drew Review“) | NeoCell: 30.700 Einh., 941.600 USD GMV ≈ 216.600 USD Provision (Estimated) | **Nicht abrufbar** (statusCode 209002, Embed ohne Videos) | – | – | unknown | Konto nicht mehr öffentlich (gesperrt/umbenannt?). Nicht öffentlich verifizierbar. |
| @dailydealz2025 („MarieC“) | Goli-Video 11/2025 mit 725.700 Plays (Verified); Umsatz nicht öffentlich | 13.800 Follower, **10.600 Videos** seit 12/2024 (≈ 16/Tag) | 24.09.2026: 10 Videos an einem Tag mit **14–408 Plays** | 2025: Frau vor der Kamera („Don’t get this … get the 6 pack“). 2026: nur Hände + Produkt, Musik statt Stimme | 2025 human-face → 2026 **F** | Das Massen-F-Format erreicht heute ~100–400 Views/Video, also **weniger** als die 3.965 in C5. |

**Schluss:** In den Produktdaten ist kein KI-Account unter den Top-Affiliates der A-Produkte zu finden. Die erfolgreichen Formate verlangen echte Menschen: Testimonial, eingeblendeter Arzt, Make-up auf echter Haut, Sketch mit zwei Personen. Nach TikTok-AIGC-Policy wären KI-„Ärzte“, fabrizierte Testimonials und AI-Hautergebnisse verboten. Für C1 bleibt das Bild daher **unwidersprochen**. Für C3 gilt: Vierstellige bis sechsstellige Monatsprovisionen sind bei Top-Affiliates von A-Produkten **real**, aber **mit Menschen** und oft **kurzlebig**.

---

## 6. Auswirkung auf C5/C6/C7 (Estimated)

Modell „realistisch“: 3.965 Views/Video, 0,8 Bestellungen/1.000 Views, AOV 38 USD, 15 %, 10 % Retouren → **4,10 USD Provision/1.000 Views** → 833 Videos/Monat für 10.000 EUR Gewinn.

Gleiche Conversion (0,8/1.000), aber realer Produktpreis und reale Rate (Formel: 0,8 × AOV × Rate × 0,9; Videos = (10.000/0,92 + 190) / (3,965 × CPM − 3)):

| Produkt-Typ | Provision/1.000 Views | Faktor vs. Modell | Videos/Monat für 10k EUR Gewinn |
|---|---|---|---|
| PDRN-Balm (16,34 USD, 15 %) | 1,76 USD | 0,43× | ~2.770 |
| Toplux (14,77 USD, 32 %) | 3,40 USD | 0,83× | ~1.050 |
| Modell C5 (38 USD, 15 %) | 4,10 USD | 1,0× | 833 |
| Goli (25,17 USD, 34 %) | 6,16 USD | 1,5× | ~516 |
| Gatekeeping-Set (72,38 USD, 18 %) | 9,38 USD | 2,3× | ~323 |
| Nex Playground (250 USD, 20 %) bei nur 0,3 Best./1.000 Views | 13,53 USD | 3,3× | ~218 |

Plausibilitäts-Anker für High-Ticket-Conversion (Claimed, Kalodata via Net Influencer, Aug 2026; Einheiten/Views, GPM = Umsatz/Views): @kevin.finds 7.490 Einh./6,88 Mio. Views = 1,09 pro 1.000 (GPM ≈ 170 USD), @airgeeksrc 0,73 (GPM ≈ 135 USD), @bennettfinds 0,37 (GPM ≈ 47 USD), @trending_ttok 0,32 (GPM ≈ 37 USD), @kid.shops 0,25 (GPM ≈ 22 USD). Die Provisionssätze dieser Produkte sind nicht genannt.

**Bewertung:**
- C6 und C7 gelten nur für das Modellprodukt. Mit einem 18–20-%-Produkt über 70 USD halbiert bis drittelt sich die nötige Videozahl rechnerisch.
- Die Voraussetzungen dafür sind aber (a) Top-Creator-Conversion auf einem teuren Produkt und (b) 3.965 mittlere Views bei einem KI-Format. Beides ist für KI-Content in keinem Datensatz belegt.
- Die volumenstärksten Produkte (PDRN, Toplux) machen das Modell sogar schlechter. Der Bericht erwähnt die Produktwahl bereits als stärksten Hebel (Kap. 5.5). Die Kritik lautet daher „unterquantifiziert“, nicht „falsch“.

---

## 7. UK und Deutschland

- **UK** (FastMoss Jan–Mai 2026): Die 10 konstanten Gewinner liegen bei £3,65–£24,54 und 5–12,5 % Provision, also ≈ £0,37–£3,07 pro Verkauf (Claimed-Inputs, Estimated; im April-EU-Datensatz sogar £1,28 × 10 % = £0,13). Einziges Set über £40: Dr.Melaxin 3-Step £44 × 12 % = £5,28. Beispiel A erfordert in UK etwa 2–4× mehr Verkäufe als in den USA.
- **DE** (FastMoss Apr 2026): Die Top-5 kamen zusammen auf 60.794 Bestellungen und 764.819 USD (Claimed), bei Ø 13,83 EUR und 5–15 % Provision. Höchste Rate: Oildem Schwarzkümmelöl, 19,55 EUR × 15 % = 2,93 EUR. Für 10.000 EUR bräuchte man beim DE-#1 (GreatVita) 7.100 Verkäufe/Monat = 31 % des gesamten Produktvolumens. **In DE existiert keines der Beispiele A/B/C mit Volumen.** Das stützt C5 („konservativ, DE nicht erreichbar“).

---

## 8. AIGC-Eignung der ökonomisch besten Produkte

| Produkt | Ökonomie | AI-Eignung unter AIGC-Policy (US 02.09.2026 / UK) |
|---|---|---|
| Goli Trio, NeoCell, Toplux (Supplements) | A-Typ, höchste Raten | **Bedingt.** Erlaubt: AI-Voiceover, Etikett- und Inhaltsstoff-Explainer, reales Produkt (Kategorie C/D/G). **Nicht erlaubt**: das nachweislich erfolgreiche Format (Testimonial „hat mir geholfen“, Arzt-Einblendung, Hautergebnis). Health gilt als High-Risk-Kategorie. |
| medicube Gatekeeping / Glass Glow / Dr.Melaxin Set | B-nah (11–12 EUR) | **Riskant.** Das Verkaufsargument ist sichtbare Hautwirkung, und Vorher/Nachher per KI ist verboten. Die Bundle-Inhalte müssen exakt stimmen. |
| Mellow Sleep Comforter, Rhino Straps | B-nah (10,7–11,5 EUR) | **Gut.** Material- und Mechanik-Explainer, reales Produkt, keine Wirkversprechen. |
| Nex Playground, EcoFlow | C-Typ (18–46 EUR) | **Gut** (Screen-Content, Spezifikationen). Nur Q4-saisonal (Nex) bzw. 6 % (EcoFlow). High-Ticket-„Trust-Gap“ bei KI (ShortFormNation, Claimed). |
| NuDerma HF Wand | B-nah | Medizinnah, Hautresultate tabu. Nachfrage (~6.000/Monat) reicht für 10k nicht (14 % Anteil). |

---

## 9. Findings (für die Synthese)

- **PE1 – A-Produkte mit ausreichender Nachfrage existieren** (Goli 34 %, Dr.Melaxin, NeoCell). Für 10k EUR ist nur 1,7–2,7 % des Produktvolumens nötig. Demand ist nicht der Engpass. [Claimed Daten / Estimated Rechnung]
- **PE2 – Top-Affiliates von A-Produkten verdienen fünf- bis sechsstellig**, aber alle geprüften sind human-face und teils kurzlebig. [Claimed GMV / Estimated Provision / Verified Format]
- **PE3 – Die Provision pro View ist produktabhängig (0,4–3,3× Modellwert).** C6/C7 halbieren sich bis dritteln sich bei 18–20 % auf 70–250 USD, verschlechtern sich aber bei den volumenstärksten Billigprodukten. [Estimated]
- **PE4 – Beispiel B existiert so nicht.** Die nächsten realen Produkte liegen bei 11,5–12,3 EUR pro Verkauf; 10k erfordern dort 3–4 % Anteil bei 3.400–4.600 Konkurrenten. [Claimed/Estimated]
- **PE5 – Beispiel C nur saisonal bzw. High-Ticket mit niedriger Rate.** Nex (Q4) ist das einzige volumenstarke Produkt mit ≥ 30 EUR pro Verkauf. [Claimed/Estimated]
- **PE6 – Extreme Konzentration der Affiliate-Umsätze** (Swoveralls: 38 von 21.365 = 80 %; Built Bar: Ø-Affiliate ≈ 7 USD/28 Tage). Stützt C3. [Claimed]
- **PE7 – UK/DE: keine A/B/C-Produkte mit Volumen.** Stützt C5 „konservativ“. [Claimed]
- **PE8 – Massen-F-Account (@dailydealz2025, 10.600 Videos) erreicht aktuell 14–408 Views pro Video.** Die 3.965 mittleren Views in C5 sind für reine Massen-F-Formate eher optimistisch (Einzelfall). [Verified]

---

### Verifikation PE1 (A-Produkte haben genug Nachfrage; 10k = 1,7 % des Goli-Volumens)
- **Quelle erneut geöffnet:** Net Influencer „Top 10 Products Sold On TikTok Shop In May 2026“ (Kalodata), Text gelesen: „selling 75.24k units at $25.17 across 3.38k creators. Its 34% commission rate is the highest on the chart.“ Weitere Werte gegengeprüft: Dr.Melaxin 44,63k @ 59,19 USD, 15 %, 2,01k Creator; FastMoss Q1: NeoCell 265.765 Bestellungen, 8.303.193 USD, 23 %.
- **Rechnung:** 25,17 × 0,34 × 0,92 = 7,87 EUR; 10.000 / 7,87 = 1.271 Verkäufe; 1.271 / 75.240 = 1,69 %; 1.271 / 30 = 42/Tag. Stimmt.
- **Metrik:** Umsatz = GMV (Kalodata-Schätzung). Die Provisionsrate schwankt (FastMoss 25 %); bei 25 % sind 1.729 Verkäufe nötig = 2,3 %.
- **Periode:** Mai 2026. Goli ist im Juli und August nicht mehr in den Top 10, die Nachfrage hat also sinkende Tendenz. Tatsächliches Aug-Volumen: Nicht öffentlich verifizierbar.
- **Bias:** Kalodata-/FastMoss-Daten stammen von Tool-Verkäufern (Scraping-Schätzungen). Net Influencer ist Branchenmedium.
- **Kategorie:** Produkt (keine Account-Kategorie).
- **Verdict: CONFIRMED** für „Nachfrage reicht“. Für „ein KI-Account kann 1,7 % davon bekommen“ gibt es keinen Beleg (siehe PE2).

### Verifikation PE2 (Top-Affiliates von A-Produkten: sechsstellige Provisionen)
- **Quelle erneut geöffnet:** FastMoss NeoCell-Case (Datenstand 06.03.2026): Drew Review 30,7k / 941,6k USD, Veronica 27,4k / 847,5k, FrancoPluma 19,8k / 614,2k, GPM 33,39–47,63. DR.DENT-Case: „These three videos alone generated over $685,000 in GMV“.
- **Handles:** über FastMoss-Influencer-IDs aufgelöst: 7371363406307640366 → @francopluma1, 7501469854579983390 → @vero.sin.filtro, 7404357247877366826 → @drew.review1, 7429520051840271403 → @quinclips3.
- **TikTok-Check:** tt_profile.sh für alle vier (drew.review1 = 209002, nicht abrufbar); tt_recent.sh + tt_video.sh für je 6–10 Videos; tt_media.py für je ein Video (FrancoPluma 7582860059206634783, Veronica 7688710525278047502, Ayden 7684767321394629919). Contact Sheets angesehen: alle drei human-face, IsAigc = false.
- **Rechnung:** 941,6k × 0,23 = 216,6k; 847,5k × 0,23 = 194,9k; 614,2k × 0,23 = 141,3k; 685k × 0,15 = 102,75k USD. Das ist Brutto-Provision vor Retouren, unter der Annahme konstanter Rate. Möglicherweise stammt ein Teil aus Ads/Spark-Boosts (isAd = true bei vielen Videos), dann wäre der Gewinn niedriger.
- **Periode:** NeoCell kumuliert ohne Startdatum. FrancoPluma-Views konzentrieren sich auf 12/2025–01/2026, danach Kollaps. Grob geschätzt (Estimated) ≈ 35.000–47.000 USD Provision/Monat über ~3–4 Monate.
- **Bias:** FastMoss-Marketing-Case (Rabattcode im Artikel).
- **Verdict: PARTIALLY.** Die Größenordnung der Top-Affiliate-Einkommen ist plausibel und widerlegt „vierstellig ist selten“ für Top-Creator allgemein. Kategorie ist **human-face**, nicht KI. Mindestens ein Fall ist kurzlebig und einer nicht mehr öffentlich. Für C1/C3 im KI-Sinn also **kein Gegenbeweis**.

### Verifikation PE3 (Provision pro 1.000 Views: 0,4–3,3× des Modells)
- **Rechnung erneut ausgeführt** (Skript `pe_calc.py`): Modell 0,8 × 38 × 0,15 × 0,9 = 4,104 USD → 833 Videos (identisch mit Bericht). Goli 6,16 USD → 516; Gatekeeping 9,38 → 323; Nex (0,3/1.000) 13,53 → 218; Toplux 3,40 → 1.054; PDRN 1,76 → 2.767 Videos.
- **Eingangsannahme geprüft:** 0,8 Bestellungen/1.000 Views bei 72-USD-Sets und 0,3 bei 250-USD-Produkten. Belegte Top-Creator-Werte (Claimed): 0,25–1,09 bei High-Ticket. NeoCell-Top-Creator hatten GPM 33–48 USD, also bei 31 USD AOV ~1,1–1,5 Bestellungen/1.000 Views. Das sind **Top-Creator-Werte**, keine Durchschnittswerte.
- **Metrik:** Provision (USD) pro 1.000 Views, vor Toolkosten; Gewinnformel wie Bericht (Fixkosten 190 USD, 3 USD/Video, 0,92 EUR/USD).
- **Bias:** eigene Rechnung.
- **Verdict: PARTIALLY.** Arithmetik bestätigt. Die Aussage „C6/C7 hängen stark am Produkt“ ist richtig. Dass ein KI-Account auf High-AOV-Produkten die angenommene Conversion und 3.965 mittlere Views erreicht, ist **UNVERIFIABLE**. Der Bericht nennt den Hebel bereits qualitativ (Kap. 5.5).

---

## 10. Quellen (Zugriff 2026-09-25)

- Net Influencer / Kalodata, Top 10 Products Mai 2026: https://www.netinfluencer.com/top-10-products-sold-on-tiktok-shop-in-may-2026/
- Net Influencer / Kalodata, Top 10 Products Juli 2026: https://www.netinfluencer.com/top-10-products-sold-on-tiktok-shop-in-july-2026/
- Net Influencer / Kalodata, Top 10 Products August 2026: https://www.netinfluencer.com/top-10-products-sold-on-tiktok-in-august-2026/
- Net Influencer / Kalodata, Top 10 Products Februar 2026: https://www.netinfluencer.com/10-best-selling-products-on-tiktok-shop-in-february-2026/
- Net Influencer / Kalodata, Top 10 Independent Creators August 2026: https://www.netinfluencer.com/top-10-sales-by-independent-creators-on-tiktok-in-august-2026/
- Net Influencer, Swoveralls/DudeRobe-Feldbericht: https://www.netinfluencer.com/swoveralls-duderobe-spent-more-than-2-usd-for-every-1-usd-in-tiktok-shop-gmv-during-four-month-affiliate-push/
- Net Influencer, Marketplace Pulse (Top 1 % = 60 %): https://www.netinfluencer.com/tiktok-shop-is-more-top-heavy-than-amazon-with-1-of-sellers-driving-60-of-sales-per-report/
- Net Influencer, 5W-Report (1.000-Creator-Programme): https://www.netinfluencer.com/beauty-brands-need-1000-creator-programs-to-compete-on-tiktok-shop-in-2026-report-says/
- FastMoss, US Q2 2026 Top 10: https://www.fastmoss.com/blog/best-selling-tiktok-shop-products-us-q2-2026/ (lokal: research/redteam/fm_best-selling-tiktok-shop-products-us-q2-2026.txt)
- FastMoss, US Q1 2026 Top 10: https://www.fastmoss.com/blog/top-selling-products-tiktok-shop-us-q1-2026/
- FastMoss, Q4-2026-Framework (Q4-2025-Daten, linked creators): https://www.fastmoss.com/blog/what-to-sell-tiktok-shop-q4-2026/
- FastMoss, Black Friday 2026: https://www.fastmoss.com/blog/tiktok-shop-black-friday-2026-what-to-sell/
- FastMoss, Seller Costs (298 Produkte, Median 350 Bestellungen): https://www.fastmoss.com/blog/tiktok-shop-seller-costs-in-the-us-2026-fees-creator-commissions-fulfillment-returns-real-profit/
- FastMoss, NeoCell-Case: https://www.fastmoss.com/blog/14m-from-a-single-can-how-neocell-collagen-won-on-tiktok-shop-under-the-2026-protein-surge/
- FastMoss, DR.DENT-Case: https://www.fastmoss.com/blog/how-dr-dent-dominated-the-tiktok-shop-market-in-january-2026/
- FastMoss, Built-Bar-Playbook: https://www.fastmoss.com/blog/the-tiktok-shop-protein-bar-playbook-why-built-bar-is-winning/
- FastMoss, Bloom Creatine: https://www.fastmoss.com/blog/how-bloom-quietly-dominated-tiktok-shop-in-the-past-6-months/
- FastMoss, World-Cup-Merch: https://www.fastmoss.com/blog/what-world-cup-fans-buy-tiktok-shop-2026/
- FastMoss, UK Jan–Mai 2026: https://www.fastmoss.com/blog/best-selling-tiktok-shop-products-uk-2026/ ; Europa April 2026: https://www.fastmoss.com/blog/tiktok-shop-europe-top-products-april-2026/
- FastMoss-Influencer-Seiten (Handle-Auflösung): https://www.fastmoss.com/influencer/detail/7371363406307640366 ; …/7501469854579983390 ; …/7404357247877366826 ; …/7429520051840271403 ; …/6925495512365106182
- TikTok (Verified, tt_*-Skripte): https://www.tiktok.com/@francopluma1/video/7582860059206634783 ; https://www.tiktok.com/@francopluma1/video/7595358608779529503 ; https://www.tiktok.com/@francopluma1/video/7594727246674332958 ; https://www.tiktok.com/@vero.sin.filtro/video/7688710525278047502 ; https://www.tiktok.com/@quinclips3/video/7684767321394629919 ; https://www.tiktok.com/@dailydealz2025/video/7572268384000281887 ; https://www.tiktok.com/@dailydealz2025/video/7689077779735907597 ; Profile @drew.review1 (209002)
- TheIndustry.beauty, Beauty-Tech +400 % (LED-Masken, ohne Stückzahlen): https://theindustry.beauty/beauty-tech-soars-400-on-tiktok-shop-amid-red-light-therapy-boom/
- Nicht erreichbar: Kalodata-Blog (HTTP 403), FastMoss-Sitemap (Security-Seite via curl).
- Rechenskript: research/redteam/pe_calc.py; Rohtexte: research/redteam/pe/*.txt; Medien: media/<video-id>/sheet.jpg
