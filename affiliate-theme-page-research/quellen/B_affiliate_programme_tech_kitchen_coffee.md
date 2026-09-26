# Teil B – Affiliate-Programme: Gaming/Desk Setup, Tech Gadgets, Foto/Audio/Musik, Küche, Kaffee

Prüfdatum: 2026-09-26 · Rohdaten: `raw_programs_B.csv` (96 Programmzeilen, 18 Spalten)
Amazon ist nicht Teil dieser Datei, das deckt ein anderer Researcher ab.

---

## 1. Methodik

**Quellen nach Priorität**

1. **Primärquellen (VERIFIED/CLAIMED):** öffentliche Awin-Merchant-Profile (`ui.awin.com/merchant-profile/<ID>`) und offizielle Affiliate-Seiten der Marken. Geprüft wurden Logitech, Breville, Sage UK, Herman Miller FAQ und Signup, Thomann/Clickfire, Teufel, Adorama FAQ, Apple Performance Partners, Best Buy und noblechairs.
2. **Verzeichnis (THIRD-PARTY ESTIMATE):** `affiliate-marketing.de/partnerprogramme/<domain>`. Das Verzeichnis spiegelt die Listings der Netzwerke mit Zeitstempel. Die meisten Einträge wurden am 26.09.2026 aktualisiert, ältere sind in der CSV markiert. Es nennt das Netzwerk und die Rate je Länderprogramm, zeigt aber **bei Impact meist keine Rate** („Login erforderlich“).
3. **Blogs und Listen** (getlasso, referralrocket, linkclicky, commissiondex, geniuslink): nur verwendet, wenn nichts anderes zu finden war. Immer als THIRD-PARTY ESTIMATE markiert, Widersprüche sind in `besonderheiten` vermerkt.

**Labels:**
- VERIFIED: Primärquelle mit konkretem Wert.
- CLAIMED: Primärquelle mit „bis zu“-Wert, etwa De'Longhi US „up to 15 %“ oder Breville/Sage „up to 8 %“.
- THIRD-PARTY ESTIMATE: Wert aus Verzeichnis oder Sekundärquelle.
- UNKNOWN: kein Wert gefunden.

**Wichtige methodische Einschränkungen**
- **Subnetzwerk-Raten:** Viele Verzeichniswerte stammen von Subnetzwerken wie FlexOffers, SaleGains, MCANISM, cityads, MyLead, AdPump oder Admitad. Das sind Weiterverkaufsraten, die normalerweise *unter* der Direktrate liegen. Beispiel: Peak Design über FlexOffers 8 %, die Impact-Direktrate ist vermutlich höher. Wo es eine Direktnetz-Rate gab (Awin, CJ, ADCELL, Tradedoubler, Rakuten, Webgains, Adtraction), wurde diese bevorzugt.
- **Such-Budget:** Das WebSearch-Kontingent der Session war nach etwa 40 eigenen Suchen erschöpft. Danach wurde nur noch mit gezielten Abrufen bekannter URLs gearbeitet.
- **Gesperrte Seiten:** Mehrere Markenseiten lieferten 403 oder 404, darunter getlasso.co, bhphotovideo.com, wexphotovideo.com, clivecoffee.com, insta360.com und whoop.com.
- **Deeplinks:** Programmspezifisch fast nie angegeben. Dort steht „UNKNOWN (Netzwerk-Standard …)“, weil Awin, Impact und CJ Deeplink-Tools netzwerkseitig anbieten.

**Verteilung der Datenqualität (Spalte Provision):** 14 VERIFIED · 4 CLAIMED · 67 THIRD-PARTY ESTIMATE · 11 UNKNOWN. Beim Cookie sind 18 Werte VERIFIED.

---

## 2. Wichtigste Befunde je Nische

Faustformel: Provision pro Sale ≈ Provision × Warenkorbwert (AOV). Die Berechnungen unten nutzen nur öffentlich genannte Werte.

### 2.1 Kaffee / Espresso – das stärkste Verhältnis aus hohem AOV und hoher Provision

| Programm | Markt | Provision | Cookie | AOV | ≈ € / $ / £ pro Sale |
|---|---|---|---|---|---|
| De'Longhi US (Awin 33739) | US | bis 15 % (CLAIMED) | 30 T | 398 USD | bis ≈ 60 USD |
| Breville US (Impact) | US | bis 8 % (CLAIMED) | 30 T | Barista Express 699,95 USD (Stichprobe) | bis ≈ 56 USD |
| Sage UK (Impact) | UK | bis 8 % (CLAIMED) | 30 T | ≈ 290 GBP | bis ≈ 23 GBP |
| De'Longhi UK (Awin 25781) | UK | bis 10 % (CLAIMED) | 15 T | 150 GBP | bis ≈ 15 GBP |
| De'Longhi DE (Awin 22915) | DE | bis 7 % (VERIFIED) | 15 T | > 200 EUR | > 14 EUR |
| Coffee Friend (Adtraction/CJ) | DE/EU, UK | 10 % bzw. 4–10 % (3rd party) | ? | 260 EUR (3rd party) | ≈ 26 EUR |
| Coffee Circle (Awin 14018) | DE | 5–13 % (3rd party) | **60 T** (VERIFIED) | ? | – |
| Kaffee24 (Awin 21380) | DE | 5–6 % (VERIFIED) | 30 T | 115 EUR | ≈ 6–7 EUR |

- **DE:** Hier gibt es die besten *verifizierten* Kaffee-Programme: De'Longhi DE, Kaffee24 und Coffee Circle mit 60-Tage-Cookie. De'Longhi DE heißt Social Media ausdrücklich willkommen. Einschränkungen sind der kurze 15-Tage-Cookie, 45 Tage Validierung, das Brand-Bidding-Verbot und fehlende Provision bei manchen Produkt-Launches.
- **US:** Die Hersteller-Programme von De'Longhi und Breville bieten die höchsten Raten. Die Siebträger-Fachhändler Whole Latte Love, Seattle Coffee Gear und Clive haben keine öffentlich einsehbaren Konditionen. Seattle Coffee Gear und Fellow laufen über Impact, die Rate ist nicht öffentlich.
- **UK:** Sage (8 %, 30 T) und De'Longhi UK (bis 10 %). Für De'Longhi UK nennt das Verzeichnis nur 1 %, das Awin-Profil dagegen „bis 10 %“. Der Wert sollte vor einer Entscheidung im Programm selbst geprüft werden.
- **Nicht gefunden oder nicht öffentlich:** Jura, Siemens EQ, Philips/Saeco, Nespresso DE/US/UK (nur ein Programm für Portugal gelistet) sowie Lelit, ECM, Rocket, Profitec, La Marzocco, Rancilio, Eureka, Niche, Comandante, roastmarket, Kaffeezentrale und Espresso Perfetto.

### 2.2 Gaming / Desk Setup – hohe AOVs bei Möbeln, niedrige Raten bei Hardware-Händlern

- **Ergonomie-Möbel (bester Hebel):**
  - Herman Miller: CJ, ca. 4 % (3rd party); Aeron ab 2.305 USD, also ≈ 92 USD pro Stuhl. Laut FAQ werden **nur US-Partner** angenommen. Es gibt ein eigenes Gaming-Programm über CJ in Kooperation mit Logitech G.
  - FlexiSpot UK: Awin, 4–8 %, 30 T, AOV 291,69 GBP (VERIFIED).
  - FlexiSpot DE: ADCELL 1–7 % bzw. Awin 4 %, AOV 246,58 EUR (3rd party).
  - noblechairs: Awin, 5 %, 30 T, in 11 Ländern, digitale Content-Creator ausdrücklich willkommen (VERIFIED).
  - Secretlab: Konditionen nicht abrufbar. Eine Sekundärquelle nennt 12 % bei 7-Tage-Cookie, unbestätigt.
  - Uplift V3 kostet ab 599 USD; ein Programm wurde nicht gefunden.
- **Peripherie-Marken:** Logitech ist verifiziert mit 4–10 %, 30 T und AOV 125 USD, also nur ≈ 5–12,50 USD pro Sale. Razer, Corsair, SteelSeries, HyperX und Elgato laufen meist über Impact mit nicht öffentlicher Rate; Verzeichnis- und Subnetzwerte liegen bei 1–4 %.
- **Händler:**
  - **UK:** Currys (Awin, VERIFIED) hat seit 01.08.2025 eine eigene Stufe „Content Creators & Influencers“ mit **3 %**, aber Apple, Mobiles und Konsolen nur 1 %. Scan 1 %, Overclockers bis 2 %; beide Programme richten sich ausdrücklich an Gamer, Creator und Streamer.
  - **DE:** notebooksbilliger 2 % (Awin), MediaMarkt/Saturn per communicationAds mit Fixbeträgen, Caseking 1 % Basis bis 5 % Eigenmarken. Für **Alternate, Mindfactory, Cyberport und Galaxus ist kein Programm im Verzeichnis erfasst.**
  - **US:** Best Buy (Impact) hat einen eigenen Pfad „Best Buy Creator“ für Social-Media-Creator; die Raten stehen nicht auf der Seite. Dell über CJ 1–7 %. Newegg und Micro Center: nichts gefunden.
- **Apple:** Das Programm deckt nur digitale Services ab (Partnerize), **keine Hardware**, und nimmt nur eine „limitierte Zahl“ von Partnern mit Volumen auf. Für Desk-Setup-Content ist es damit praktisch irrelevant.
- **Setup-Zubehör:** Hohe Prozente, aber niedriger AOV: Govee Awin DE 5–12 %, Ugreen Awin 8 %, Nomad CJ 10 %, Orbitkey und Nanoleaf per Subnetz 7–8 %.

### 2.3 Tech Gadgets / Smartphone-Zubehör

- **Großmarken zahlen wenig:** Samsung DE über Awin 2–5 %; ein UK- oder US-Direktprogramm ist im Verzeichnis nicht sichtbar. Garmin CJ 2 % (US, EU, UK). OnePlus nur über Subnetze mit 1,5–3,75 %.
- **Zubehör-Marken zahlen mehr:** CASETiFY Awin US 10 %, Nomad CJ 10 %, Ugreen 8 %, Anker Webgains UK 5 %. Die Direktraten von Peak Design und Belkin liegen hinter dem Impact-Login.
- **DJI, Insta360, GoPro, Oura und WHOOP:** Netzwerke sind identifiziert (DJI, Oura und WHOOP bei Impact, GoPro bei Partnerize), die Raten aber nicht öffentlich. Subnetzwerte liegen bei 0,75–6 %. Damit ist das die größte Datenlücke mit hohem AOV (Drohnen, Kameras).

### 2.4 Foto / Audio / Musik

- **DE:**
  - Thomann (Clickfire, VERIFIED): Influencer 4,5 %, Website 3,5 %, 14-Tage-Cookie. Für Social Media gilt eine **Mindestreichweite von 5.000 Followern**, für Websites 500 Unique Visits pro Tag. Eine neue Theme-Page kann also erst nach dem Aufbau der Reichweite teilnehmen.
  - Teufel (Rakuten, VERIFIED): bis 8 %, aber mit **Multi-Touch-Attribution**, d. h. die Provision wird zwischen beteiligten Partnern geteilt. Bestätigung erst nach 8 Wochen.
  - Calumet über Awin 3–5 %, Sony über Awin 3 % bei AOV 500 EUR (≈ 15 EUR pro Sale), Canon über CJ 2 % bei AOV > 200 EUR, B&O über CJ 5 %.
- **US:** B&H 2 % Basis und 8 % auf Featured Brands, Cookie laut Sekundärquellen nur 60 Stunden. Adorama über Impact 2 %, 30 T, Auszahlung 45 Tage nach Versand (VERIFIED). Sweetwater und Guitar Center liegen laut Sekundärquellen bei 4–6 %, beide inzwischen über Impact.
- **UK:** Gear4music über Awin (VERIFIED): 30 T, 60 Tage pending, **keine Cashback-, Gutschein-, Incentive- oder CSS-Partner**, kein Brand-PPC, keine Publisher mit aktiven Google/Microsoft-Ads; die Rate ist nicht genannt. Wex ist offenbar zu Impact gewechselt, ca. 1,5 %.
- **Audio-Marken:** Sennheiser mit 60-Tage-Cookie und 3,5–7 % je Kategorie (laut Verzeichnis-Beschreibung). Sonos und Bose haben widersprüchliche Sekundärangaben von 2–5 %.

### 2.5 Küche / Kochgeschirr

- **DE:** Zwilling über Awin 6,4–8 %, KitchenAid über Awin 7 %, WMF 5 %, Tchibo 5–8 %. SharkNinja/Ninja über Awin 5 % bei 30 T, AOV 146 EUR und 40 Tagen Validierung, mit Feed und Deeplinks. Le Creuset läuft über Rakuten, die Rate ist nicht öffentlich. Für Springlane, Kochform und Otto wurde kein Programm gefunden.
- **UK:** Zwilling über Awin 8 %. Lakeland über Awin mit **2,5 %, 15 T**; Provision gibt es nur auf UK-Sales (VERIFIED). ProCook und John Lewis laufen über Impact, Raten nicht öffentlich. SharkNinja UK ist nur über ein Subnetz mit 0,75–2,25 % gelistet.
- **US:** Zwilling über CJ 6 %, KitchenAid über CJ 5 %, Vitamix über CJ 3 %, Fissler über Awin 5 %.
  - Die DTC-Premium-Marken Made In, Our Place und Caraway laufen alle über **Impact ohne öffentliche Raten**. Caraway zahlt über FlexOffers einen **Fixbetrag von 32–52 USD pro Sale**.
  - HexClad-Sets kosten 219–2.999 USD (12-teilig 699 USD); ein Programm wurde nicht gefunden.
  - Williams Sonoma: nichts gefunden. Sur La Table 3,2–4 %.

---

## 3. Vergleich der Märkte (DE vs. US vs. UK)

| Aspekt | DE / DACH | US | UK |
|---|---|---|---|
| Dominantes Netzwerk | Awin (dazu ADCELL, Rakuten, Tradedoubler, TradeTracker, communicationAds) | Impact (dazu CJ, Rakuten) | Awin (dazu Impact, CJ, Webgains) |
| Transparenz der Raten | **hoch**: viele Awin-Profile öffentlich | **niedrig**: Impact-Raten meist hinter Login | mittel bis hoch |
| Beste verifizierte Kombination aus AOV und Rate | De'Longhi DE (7 %, > 200 EUR), noblechairs (5 %), Zwilling (bis 8 %, 3rd party) | De'Longhi US (bis 15 %, 398 USD), Breville (bis 8 %), Herman Miller (4 % auf 2.305 USD) | Sage (8 %, 290 GBP), FlexiSpot (4–8 %, 292 GBP), De'Longhi UK (bis 10 %, 150 GBP) |
| Hardware-Händler | schwach bis nicht vorhanden (nbb 2 %; Alternate, Mindfactory, Cyberport, Galaxus nicht gelistet) | Best Buy mit Creator-Pfad; B&H und Adorama 2 % | Currys 3 % für Creator; Scan und OC bis 2 % |
| Cookies | häufig 15–30 T, Ausreißer Coffee Circle 60 T | 30 T üblich, B&H nur 60 h | 15–30 T |

Auffällig: Eine Marke zahlt je nach Land deutlich unterschiedlich. De'Longhi: US bis 15 %, UK bis 10 %, DE bis 7 %. Samsung: nordische Länder 8 %, DE 2–5 %. Die Raten müssen daher pro Markt geprüft werden.

---

## 4. Social Media / Instagram: was ausdrücklich geregelt ist

- **Keine** der geprüften Primärquellen verbietet Instagram ausdrücklich. Instagram wird aber auch fast nirgends ausdrücklich erlaubt. In den meisten Zeilen steht deshalb `UNKNOWN`.
- **Ausdrücklich Social- oder Creator-freundlich:**
  - De'Longhi DE: Social Media als Werbeform willkommen.
  - Currys: eigene Creator- und Influencer-Stufe mit 3 %.
  - noblechairs: „digitale Content-Ersteller“.
  - Overclockers UK: „gamers, creators, streamers“.
  - Best Buy: Creator-Programm.
  - Breville US: richtet sich an Content-Creator.
  - Sage UK: eigener Influencer-Kontakt.
- **Einschränkungen, die für eine neue KI-Theme-Page relevant sind:**
  - Thomann: mindestens **5.000 Follower** für Social-Media-Partner.
  - Apple: nur Partner mit Volumen.
  - Gear4music: keine Incentive-, Cashback- oder Gutschein-Partner.
  - Wex: exklusive Codes dürfen nicht auf Social Media geteilt werden.
  - Kaffee24 und De'Longhi: nur autorisierte Codes, sonst Provision 0.
  - Currys: keine BNPL-Publisher.
  - De'Longhi DE und Gear4music: kein Brand-Bidding.
- **Programme, die Social-Traffic ausdrücklich ausschließen, wurden nicht gefunden.** Die Ausschlüsse betreffen Incentive-, Cashback- und Gutschein-Traffic sowie Paid Search.

---

## 5. Typische AOV-Spannen der Hauptprodukte

| Kategorie | Wert | Quelle / Art | Datum |
|---|---|---|---|
| Siebträger (Breville Barista Express, US) | 699,95 USD | Preisstichprobe breville.com (ausverkauft) | 2026-09-26 |
| Espresso/Kaffee Sage UK | ≈ 290 GBP AOV | Programmseite Sage | 2026-09-26 |
| De'Longhi US / UK / DE | 398 USD / 150 GBP / > 200 EUR AOV | Awin-Profile | 2026-09-26 |
| Kaffee-Onlineshop DE (Kaffee24) | 115 EUR AOV | Awin-Profil | 2026-09-26 |
| Coffee Friend | 260 EUR AOV | Verzeichnis (3rd party) | 2026-09-26 |
| Ergonomie-Stuhl Herman Miller Aeron | ab 2.305 USD | Preisstichprobe store.hermanmiller.com | 2026-09-26 |
| Steh-Schreibtisch Uplift V3 | ab 599 USD | Preisstichprobe upliftdesk.com | 2026-09-26 |
| Steh-Schreibtisch FlexiSpot UK / DE | 291,69 GBP / 246,58 EUR AOV | Awin-Profil / Verzeichnis | 2026-09-26 |
| Peripherie Logitech | 125 USD AOV | Programmseite Logitech | 2026-09-26 |
| Küchengeräte SharkNinja DE | 146 EUR AOV | Verzeichnis (Awin-Beschreibung) | 2026-09-26 |
| Premium-Kochgeschirr HexClad | Sets 219–2.999 USD (12-tlg. 699 USD, regulär 999 USD) | Preisstichprobe hexclad.com | 2026-09-26 |
| Sony Store / Canon EMEA | 500 EUR / > 200 EUR AOV | Verzeichnis (3rd party) | 2026-09-26 |
| PC-Hardware Mindfactory | 550 EUR AOV | Verzeichnis, **archiviert, Stand 2018** | alt |

Grob zusammengefasst: Espresso und Siebträger liegen bei 150–700 USD/EUR (High-End-Dualboiler kosten mehr, wurden aber nicht verifiziert). Ergonomie-Stühle und Schreibtische liegen bei 250–2.300 USD. Premium-Kochgeschirr liegt bei 200–1.000 USD. Peripherie liegt bei ≈ 125 USD.

---

## 6. Datenlücken

- **Impact-Raten fehlen fast überall.** Betroffen sind unter anderem Razer, Corsair, SteelSeries, Elgato, DJI, Oura, WHOOP, Peak Design, Belkin, Best Buy, Made In, Our Place, Caraway, Fellow, Seattle Coffee Gear, ProCook, John Lewis, Guitar Center, Sweetwater und Musician's Friend. Das lässt sich nur mit einem Publisher-Account klären.
- **Nicht dokumentiert** (kein Programm gefunden, Seite gesperrt oder wegen des Such-Budgets nicht mehr recherchiert):
  - **Gaming/Desk:** Keychron, NuPhy, Glorious, Wooting, Grovemade, Oakywood, Twelve South, Satechi (nicht im Verzeichnis), Native Union, Ergotron, BenQ, Steelcase, Fully/Vari, Branch, Autonomous, Uplift (nur Preis), Microsoft Store, Newegg (nicht im Verzeichnis), Micro Center, LG/Samsung-Monitore UK/US.
  - **Tech Gadgets:** Nothing, Google Store, dbrand, Mous, Kindle/Boox, Ecovacs.
  - **Foto/Audio/Musik:** Fujifilm, Foto Koester, Audio-Technica, Marshall, Splice, Plugin Boutique.
  - **Küche:** Thermomix/Vorwerk (vermutlich kein klassisches Affiliate-Programm, da Direktvertrieb; nicht verifiziert), Staub separat (Zwilling-Gruppe), Global/Shun, Blendtec, GreenPan, Misen, HexClad (Programm), Williams Sonoma (nicht im Verzeichnis), Crate&Barrel, Kochform, Springlane (Verzeichnis-Stand 2016), Otto Küche, Cosori.
  - **Kaffee:** Jura, Siemens EQ, Philips/Saeco, Nespresso (nur ein Programm für Portugal), die Siebträger-Marken (siehe 2.1), Baratza, Hario, Chemex, Oxo, roastmarket, Kaffeezentrale, Espresso Perfetto, Whole Latte Love (nicht im Verzeichnis), Clive Coffee (403), Bean Box und Espresso Outlet.
- **Fehlender Verzeichniseintrag heißt nicht, dass kein Programm existiert.** Das betrifft Alternate, Cyberport, Galaxus, Mindfactory, Newegg, Satechi, Springlane, roastmarket, Kaffeezentrale, Williams-Sonoma und Whole Latte Love.
- **Widersprüche**, die im Programm geprüft werden müssen:
  - De'Longhi UK: 1 % im Verzeichnis gegenüber „bis 10 %“ im Awin-Profil.
  - B&H: Cookie 60 h oder 30 T.
  - Sweetwater: AvantLink oder Impact.
  - Secretlab: 12 % bei 7 T, unbestätigt.
  - Herman Miller: US-only laut FAQ, aber CJ-Programme für UK, DE und FR im Verzeichnis.
  - KitchenAid US: CJ 5 % gegenüber FlexOffers 9 %.
- **AOV** ist nur bei etwa 15 Programmen öffentlich. **EPC und Konversionsraten** waren auf den abgerufenen Awin-Profilen nicht sichtbar; einzige Ausnahme ist Thomann mit „~5 % Konversionsrate“ als Eigenangabe.

---

## 7. Quellen (abgerufen am 2026-09-26)

**Primärquellen: Awin-Merchant-Profile**
- https://ui.awin.com/merchant-profile/22506 (FlexiSpot UK)
- https://ui.awin.com/merchant-profile/22915 (De'Longhi DE)
- https://ui.awin.com/merchant-profile/33739 (De'Longhi US)
- https://ui.awin.com/merchant-profile/25781 (De'Longhi UK)
- https://ui.awin.com/merchant-profile/39624 (noblechairs EUR)
- https://ui.awin.com/merchant-profile/28817 (Caseking DE)
- https://ui.awin.com/merchant-profile/1599 (Currys)
- https://ui.awin.com/merchant-profile/1117 (Gear4music)
- https://ui.awin.com/merchant-profile/1751 (Lakeland)
- https://ui.awin.com/merchant-profile/14018 (Coffee Circle DE)
- https://ui.awin.com/merchant-profile/21380 (Kaffee24 DE)
- https://ui.awin.com/merchant-profile/28821 (Overclockers UK)
- https://ui.awin.com/merchant-profile/15473 (Scan Computers)

**Primärquellen: Marken- und Händlerseiten**
- https://www.logitech.com/en-us/programs/affiliate-program
- https://www.breville.com/us/en/learn-more/breville-affiliates-program.html
- https://www.sageappliances.com/uk/en/learn-more/sage-affiliates-program.html
- https://store.hermanmiller.com/faq-affiliate-program.html?lang=en_US
- https://store.hermanmiller.com/affiliate-signup.html?lang=en_US
- https://store.hermanmiller.com/gaming-affiliate-signup?lang=en_US
- https://thomann.clickfire.de/
- https://www.thomann.de/de/faq_question_wie_werde_ich_thomann_affiliate_partner.html
- https://teufel.de/partnerprogramme
- https://www.adorama.com/api/getContent?contentName=affiliate_faq&output=desktop
- https://performance-partners.apple.com/
- https://www.bestbuy.com/site/misc/affiliate-program/pcmcat198500050002.c?id=pcmcat198500050002
- https://www.noblechairs.eu/de-at/partnerprogramm/cp_000023.html
- https://secretlab.co/pages/affiliates (Inhalt beim Abruf abgeschnitten)

**Preisstichproben**
- https://www.breville.com/us/en/products/espresso/bes870.html
- https://store.hermanmiller.com/office-chairs/aeron-chair/2195348.html
- https://www.upliftdesk.com/uplift-v2-standing-desk-v2-or-v2-commercial/ (zeigt V3)
- https://hexclad.com/collections/cookware-sets

**Verzeichnis (THIRD-PARTY): `https://www.affiliate-marketing.de/partnerprogramme/<domain>`**, abgerufen für diese Domains:
- **Gaming/Desk:** logitech.com, razer.com, corsair.com, steelseries.com, hyperx.com, asus.com, flexispot.de, elgato.com, govee.com, nanoleaf.me, orbitkey.com, nomadgoods.com, satechi.net, hermanmiller.com
- **Händler und PC-Hersteller:** alternate.de, notebooksbilliger.de, cyberport.de, mediamarkt.de, galaxus.de, mindfactory.de, bestbuy.com, newegg.com, dell.com, lenovo.com, hp.com, argos.co.uk, johnlewis.com
- **Tech Gadgets:** samsung.com, oneplus.com, casetify.com, peakdesign.com, belkin.com, anker.com, ugreen.com, dji.com, insta360.com, gopro.com, garmin.com, ouraring.com, whoop.com
- **Foto/Audio/Musik:** sony.de, canon.de, calumetphoto.de, sonos.com, sennheiser.com, bang-olufsen.com, native-instruments.com, musiciansfriend.com, sweetwater.com, guitarcenter.com
- **Küche:** kitchenaid.de, ninjakitchen.de, sharkninja.co.uk, wmf.com, zwilling.com, fissler.com, lecreuset.de, lecreuset.com, tchibo.de, otto.de, smeg.com, vitamix.com, williams-sonoma.com, surlatable.com, madeincookware.com, fromourplace.com, carawayhome.com, procook.co.uk, philips.de, springlane.de
- **Kaffee:** delonghi.com, coffeecircle.com, coffeefriend.de, kaffeezentrale.de, roastmarket.de, nespresso.com, drinktrade.com, atlascoffeeclub.com, fellowproducts.com, bluebottlecoffee.com, seattlecoffeegear.com, wholelattelove.com

**Sekundärquellen (nur als Ergänzung)**
- https://www.100partnerprogramme.de/p/thomann-de/ (Stand 04/2023)
- https://getlasso.co/affiliate/logitech/
- https://getlasso.co/affiliate/corsair/
- https://getlasso.co/affiliate/argos/
- https://getlasso.co/affiliate/bose/
- https://getlasso.co/affiliate/sonos-europe/
- https://getlasso.co/affiliate/bh-photo-video/
- https://geniuslink.com/blog/bh-photo-affiliate-program/
- https://referralrocket.io/affiliate-program/razer_10I
- https://taprefer.com/secretlab-affiliate-program/secretlab/
- https://commissiondex.com/programs/sweetwater/
- https://linkclicky.com/affiliate-program/guitar-center/
- https://linkclicky.com/affiliate-program/john-lewis-partners/
- https://www.flexoffers.com/affiliate-programs/wex-photographic-affiliate-program/
