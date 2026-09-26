# Teil D – Affiliate-Programme: Travel, Outdoor, Sport, Golf, Beauty, Fashion, Uhren, Hobby

**Prüfdatum:** 2026-09-26
**Zugehörige Rohdaten:** `raw_programs_D.csv` (161 Zeilen, 18 Spalten, UTF-8)
**Nicht im Scope:** Amazon (anderer Researcher)

---

## 1. Methodik

1. **Websuche (ca. 50 Abfragen):** Einstieg über Brand- und Netzwerkseiten, zuerst Travel Gear, Travel Booking und Outdoor. Danach war das Websuche-Budget der Session aufgebraucht (200/200, von allen Researchern gemeinsam genutzt). Es wurden keine weiteren Suchen über Umwege ausgeführt.
2. **Direkter Abruf von Primärquellen** (WebFetch bzw. `curl`) über bekannte oder aus URL-Mustern abgeleitete Adressen:
   - offizielle Affiliate-Seiten der Marken (z. B. Nike, OTTO, Cult Beauty, Travelpro, Tortuga, Canyon, Aventon, REP Fitness, Stanley, Cricut, Anycubic, Creality, Blue Nile, Miniature Market, 2nd Swing, Ellis Brigham, Bluetti, Jackery, EcoFlow US, Foreo, Etsy, LEGO US),
   - öffentliche **Awin-Merchant-Profile** (Monos, BÉIS, Db DE, EcoFlow DE/UK, Decathlon UK, Bergfreunde DE),
   - öffentliche **Webgains-Programmseiten** (Horizn DE, Cotswold Outdoor, Jackery UK/EU),
   - die **eBay-Partner-Network-Rate-Card** (als Bild ausgelesen).
3. **Netzwerk-Verzeichnis affiliate-marketing.de:** Rund 220 Shop-Domains wurden systematisch abgefragt. Das Verzeichnis ist tagesaktuell (Stand 26.09.2026) und bündelt Programmdaten aus Awin, CJ, Impact, Rakuten, Partnerize, Webgains, ADCELL, Tradedoubler, belboon, Daisycon, TradeTracker und weiteren Netzwerken. Die Werte gelten hier als **THIRD-PARTY ESTIMATE**. Häufig ist nur ein Höchstsatz genannt, und für Impact-, Rakuten- und Partnerize-Programme fehlen die Prozentsätze.
4. **Sub-Netzwerke** wie FlexOffers, SaleGains, MyLead, CityAds, AdPump oder MCANISM geben die Raten der Marke abzüglich ihrer eigenen Marge weiter. Diese Werte stehen nur als Hinweis in der Tabelle, wenn kein Primärnetzwerk bekannt ist. Offensichtliche Artefakte wie „75 % / Sale“ bei SaleGains wurden verworfen.

**Datenqualitäts-Labels (je Provision und Cookie):**

| Label | Bedeutung |
|---|---|
| VERIFIED | In dieser Session direkt auf der Primärquelle gelesen (Brand-Seite, Awin-/Webgains-Profil, eBay-Rate-Card) |
| CLAIMED | Marketingangabe der Marke („bis zu X %“) oder Inhalt einer offiziellen Seite, der nur als Such-Snippet sichtbar war (Seite blockiert) |
| THIRD-PARTY ESTIMATE | Aggregatoren, Verzeichnisse, Blogs (getlasso, FlexOffers, affiliate-marketing.de usw.) |
| UNKNOWN | Nicht auffindbar oder nicht öffentlich |

**Verteilung (Spalte Provision):** 23 VERIFIED · 9 CLAIMED · 96 THIRD-PARTY ESTIMATE · 33 UNKNOWN.
**Zeilen:** 161, davon 156 Programme bzw. Länderprogramme mit Daten und 5 Zeilen „kein Programm / eingestellt“ (Airbnb, Rogue Fitness, Zalando, ABOUT YOU, Golf-Simulatoren Uneekor/Foresight/Rain or Shine).

---

## 2. Befunde je Nische und Markt

### 2.1 Travel Gear (Koffer, Taschen, eSIM)

| Markt | Stärkste belegte Programme |
|---|---|
| **US** | **NOMATIC 15 %** (Awin, Verzeichnis) · **Tortuga 10 %**, 30 Tage, AOV > 250 USD (AvantLink, VERIFIED) · **Travelpro 8–10 %**, 45-Tage-Cookie, AOV 165 USD (VERIFIED) · CALPAK 8 % (Impact, LTK) · Bellroy 7 %, AOV 180 USD (VERIFIED) · Monos 5 % · Away nur ca. 3 % |
| **DE** | Koffer.de 5 % (Awin) · Koffer-Direkt bis 5 %/60 Tage (retailAds, Datenstand 2025) · Eastpak 6 % (Daisycon) · Db Journey 3 % (Awin; AOV 180 €) · **Horizn Studios 8 % (Webgains), das DE-Programm wird aber geschlossen** (keine Neuanmeldung, letzte Zahlung 16.09.2026) |
| **UK** | Db UK 3 % (Awin/Webgains) · Eastpak (Daisycon/Rakuten). Für Luxus-Koffer (Rimowa, Tumi) gibt es nur widersprüchliche Drittangaben von etwa 5–6 %. |
| **Global** | eSIMs: **Saily 15 %** (laut Brand-FAQ ausdrücklich ohne eigene Website möglich) · Holafly 10–20 % · Airalo 10 % (Impact). Hohe Raten, aber niedriger Warenkorb. |

**Fazit:** Premium-Luggage-Direktmarken in den USA zahlen 8–15 % bei 165–250 USD AOV. In DACH liegen Händlerprogramme meist nur bei ca. 5 %. Luxusmarken wie Rimowa und Tumi haben keine transparenten Programme.

### 2.2 Travel Booking (nur zum Vergleich)
GetYourGuide 8 % bei 31 Tagen, Viator 8 % bei 30 Tagen mit „Viator Shop“ als Link-in-Bio-Storefront für Creator. Expedia Group zahlt bis ca. 5,8 % bei nur **7 Tagen** Cookie und nur für bereits angetretene Reisen („consumed“). Booking.com zahlt einen Anteil an der eigenen Provision. **Airbnb hat sein Programm 2021 eingestellt.** Der strukturelle Nachteil: Die Provision fließt erst nach der Reise, und Stornos verfallen. Für Reels ist Travel Booking daher eher Zusatzmonetarisierung.

### 2.3 Outdoor / Camping / Power Stations

| Markt | Programme |
|---|---|
| **DE** | **Bergfreunde** (Awin): Content bis 15 %, Standard 7 %, **AOV 165 €, Bestätigungsrate nur 65 %**, Storno bei Retoure innerhalb von 100 Tagen · SportScheck 6–8 % · Globetrotter 5 % (inhouse; Tracking **nur bei Cookie-Consent**) · **EcoFlow DE 5 %, AOV 1.000 €, aber nur 7 Tage Cookie** (Awin, VERIFIED) · Bluetti DE 3,5 % (TradeTracker) |
| **US** | Stanley 1913 10 % (AvantLink, VERIFIED) · Backcountry 4–12 % · Arc'teryx 7 % · REI 5 %/15 Tage · Jackery „5 %+“, AOV ca. 1.300 USD (Drittangabe) · EcoFlow US ≥ 5 %/7 Tage, AOV > 1.000 USD · YETI 4–7 % |
| **UK** | Cotswold Outdoor 4–8 %, AOV ca. 90 £, **Instagram/TikTok ausdrücklich erlaubt** (Webgains) · Jackery UK 6 %/30 Tage · EcoFlow UK 5 %/7 Tage, AOV 1.000 £ · Decathlon UK 3 % (keine Provision auf Marketplace) · Snow+Rock 2–8 % · Ellis Brigham (**nur mit eigener Domain**) |

**Power Stations** kombinieren am deutlichsten hohen AOV (1.000 €/£/USD) mit mittlerer Rate: 5 % × 1.000 € ≈ 50 € pro Sale laut Awin-Angaben EcoFlow. Das 7-Tage-Cookie bei EcoFlow ist für verzögerte Käufe aus Reels jedoch ein klarer Nachteil. Jackery (30 Tage) und Bluetti (bis 10 %, Social ausdrücklich erlaubt) sind dafür attraktiver.

### 2.4 Fitness & Running

| Markt | Programme |
|---|---|
| **US** | **Nike bis 15 %** (CJ, **7 Tage**, Creator ausdrücklich zugelassen) · **On 18 %** (Awin; auffällig hoch, evtl. Höchstsatz) · REP Fitness bis 5 % (nur US, **keine bezahlte Social-Werbung**, Retouren werden rückwirkend abgezogen) · BowFlex ab 3 %/30 Tage (Impact) · Tonal, Hydrow, WHOOP, Therabody über Impact (Prozente nicht öffentlich) · **Rogue: kein Affiliate-Marketing-Programm** |
| **DE** | Sport-Thieme 10 % (Awin/Tradedoubler) · On DE 18 % · Hyperice 5 % · Tradeinn/Runnerinn 5 % (belboon) · adidas DE nur 2 % |
| **UK** | On UK 18 % · **adidas UK 6 % (dreimal so viel wie DE)** · Peloton UK 2,5 % + 2,50–3,00 £ pro Lead · Hyperice UK 5 % |

### 2.5 Cycling / E-Bikes
- **DE:** ROSE 5 %, Lucky Bike 5 % (Webgains), bike-components 3 %, VanMoof 3,5 % (nur Sub-Netzwerk), **Canyon 2 % Basis auf Bikes** bei 30 Tagen (VERIFIED).
- **US:** Aventon 4 % bei 30 Tagen und 2,5 % Conversion Rate (AvantLink, VERIFIED). Rad Power Bikes, Lectric, Competitive Cyclist und Zwift laufen über Impact, die Prozente sind nicht öffentlich.
- **UK:** kaum belastbare Daten. Wiggle und Chain Reaction sind nur über Sub-Netzwerke bzw. AU gelistet, ihr Status 2026 ist unklar.
- **Fazit:** E-Bikes haben einen hohen Produktpreis, aber meist nur 2–5 %. Kein E-Bike-Programm mit ≥ 5–10 % war belegbar.

### 2.6 Golf
- **US:** **SkyTrak 15 % (Awin) bzw. 10 % (CJ)**. Das ist ein Launch-Monitor/Simulator; die laufende Aktion „Save 1.300 USD off ST MAX“ zeigt Produktpreise deutlich über 1.300 USD (Produktpreis, nicht AOV). **2nd Swing Golf 15 %** auf ausgewählte Neuheiten (14 Tage) bzw. 5 % (30 Tage), VERIFIED. Carl's Golfland 4 %. TaylorMade, PGA TOUR Superstore, Golf Galaxy und Rapsodo laufen über Impact, Callaway über Partnerize (Prozente nicht öffentlich).
- **DE:** Golf House 6 % (Awin), Golfshop.de 2,5–6 % (ADCELL).
- **UK:** American Golf über Partnerize (Prozente nicht öffentlich).
- **Kein öffentliches Programm gefunden:** Uneekor, Foresight Sports, Rain or Shine Golf.
- **Fazit:** Golf-Simulatoren bzw. Launch Monitors (SkyTrak) sind einer der wenigen Fälle mit hohem Produktpreis **und** ≥ 10 %, derzeit aber US-only.

### 2.7 Beauty / Skincare / Haircare

| Markt | Programme |
|---|---|
| **DE** | **The Ordinary DE 13–20 %** · **Sephora DE 12 %** · **LOOKFANTASTIC DACH 12 %** · Douglas 5–10 % · Flaconi 3–5 % · Dyson DE 5 % · ghd DE 5 % · CurrentBody DE (LED-Masken) nur 2–4 % |
| **UK** | **LOOKFANTASTIC UK 15 %** · Cult Beauty bis 15 % (**Influencer nicht über Awin**, nur 1 % bei Promo-Codes) · The Ordinary 13 % · Space NK 7 % · Foreo UK 6 % · ghd UK 1–5 % |
| **US** | **medicube 20 %** (Awin; Beauty-Devices) · LOOKFANTASTIC US 10 % · Foreo 6 % (Brand: 2–15 %, **60 Tage Cookie**) · ghd US 5 %. Sephora US, Estée Lauder und Olaplex (Rakuten) sowie Ulta und Glossier (Impact): Prozente nicht öffentlich. |

**LED-Masken/Devices:** Nur medicube (20 %) erfüllt „hochpreisiges Gerät + hohe Rate“. CurrentBody DE (2–4 %) ist schwach, für Solawave und NuFace wurde kein Primärprogramm gefunden.

### 2.8 Fashion / Luxus / Resale
- **DE:** **Breuninger 12 %** (Awin) · **OTTO bis 15 %** (Warenkorb-Ebene, dynamische Attribution; **reine Social-Creator nur über Stylink oder Metapic**) · Lounge by Zalando 12 % + 0,50 € Lead · Mytheresa DACH 4,8–9,6 % (CJ) · Mango 6 % · adidas 2 %. **Zalando und ABOUT YOU: kein öffentliches Affiliate-Programm gefunden.**
- **US:** Nike bis 15 % · Revolve 5 % · Rebag 7 % · StockX, GOAT, The RealReal und FASHIONPHILE über Impact (Prozente nicht öffentlich) · Shopbop nur über Sub-Netzwerk.
- **UK:** Mytheresa UK 4 % · NET-A-PORTER/MR PORTER (Rakuten) und FARFETCH (Partnerize, Programme aktiv gelistet): Konditionen nicht öffentlich · adidas UK 6 %.
- **Retouren/Stornos:** Direkte Retourenquoten für Fashion-Programme waren öffentlich nicht auffindbar. Belege aus angrenzenden Programmen:
  - Bergfreunde (Outdoor-Bekleidung/Schuhe): durchschnittliche **Bestätigungsrate 65 %**, also rund ein Drittel stornierter Sales, und ein Stornofenster von 100 Tagen.
  - Db: 90 Tage Validierung. BÉIS: 60 Tage Validierung. REP: rückwirkender Abzug von Retouren.
  - Etsy und LEGO provisionieren ausdrücklich ohne Retouren; Bellroy nennt ca. 6 % Retourenquote.
  - Für Fashion sind daher eher 20–40 % Stornoabzug plausibel. **Das ist eine Annahme, keine belegte Zahl.** Die Nominalprovision muss entsprechend abgewertet werden.

### 2.9 Uhren & Schmuck
- **Chrono24:** Awin **US 2,5 % + 1 USD pro Lead**, Awin **UK 2,5 %**. Das US-Programm wurde am 21.09.2026 im Verzeichnis aufgenommen, ein DE-Programm war nicht auffindbar, die offizielle Seite ist blockiert. Die Rate ist niedrig, der Warenkorb (Luxusuhren) sehr hoch; AOV nicht öffentlich.
- **DE:** Uhrcenter 9 % · CHRIST 8 % · THOMAS SABO 8 % (auch CH/UK) · Daniel Wellington 8 %.
- **US:** Jomashop 1–6 % bzw. 5–40 USD pro Sale (CJ) · Blue Nile 3,5 % (**eigene Domain erforderlich**) · Mejuri, Ana Luisa und Brilliant Earth über Impact (Prozente nicht öffentlich).
- **eBay Partner Network:** „Jewelry & Watches“ 4,0 % (Deckel 550 USD pro Transaktion), **24 Stunden** Attributionsfenster.
- Watchfinder: kein Programm gelistet.

### 2.10 Hobby / Collectibles / 3D-Druck
- **eBay Partner Network (VERIFIED):** Collectibles (Toys, Hobbies, Sports Memorabilia usw.) 3,0 % mit Deckel 550 USD, All Other 4,0 %. Nur **24 Stunden** Fenster, Links in Social Media ausdrücklich erlaubt, Kurz-URLs zulässig.
- **LEGO:** US über Rakuten (Prozente nicht öffentlich; ohne Versand, Steuern und Retouren), EU/UK über Daisycon mit 3,57 %.
- **Etsy:** eigenes „Creator Collective“ für Social-Media-Creator (Prozente nicht öffentlich).
- **Weitere Programme:** TCGplayer und Fanatics über Impact · Funko 4 % (CJ) · Revell DE 8 % · Miniature Market 5 %/7 Tage (LinkConnector) · Conrad DE 5 %.
- **3D-Druck:** **Bambu Lab US 10 %** (Awin) · Creality 4–8 % (Impact/Awin; IG-, TikTok- und YouTube-Creator ausdrücklich) · **Anycubic ab 5 %, 60 Tage Cookie** · Elegoo 5 % · Cricut bis 12 %, aber nur **5 Tage** Cookie · DJI über Impact (Prozente nicht öffentlich).
- **Kein Programm gefunden:** Prusa, Märklin, Games Workshop, Pokémon Center, HobbyKing, Philibert.

---

## 3. Typische AOV-Spannen (nur mit Quelle)

| Produktgruppe | AOV / Warenkorb | Quelle | Qualität |
|---|---|---|---|
| Power Stations (EcoFlow DE / UK / US) | 1.000 € / 1.000 £ / > 1.000 USD | Awin-Profile 51793, 51797; us.ecoflow.com | VERIFIED |
| Power Stations (Jackery) | ca. 1.300 USD | getlasso/Drittangabe | THIRD-PARTY |
| Reiserucksack (Tortuga) | > 250 USD | tortugabackpacks.com/pages/affiliates | CLAIMED/VERIFIED |
| Reisetaschen (Db Journey DE) | 180 € | Awin-Profil 109840 | VERIFIED |
| Wallets/Taschen (Bellroy) | 180 USD | bellroy.com/affiliate-program | VERIFIED |
| Koffer (Travelpro) | 165 USD (Bestellungen 19–479 USD) | travelpro.com/pages/affiliate-program | VERIFIED |
| Koffer (BÉIS) | ca. 233 USD | hienergy (Drittangabe) | THIRD-PARTY |
| Outdoor-Ausrüstung (Bergfreunde DE) | 165 € | Awin-Profil 14102 | VERIFIED |
| Outdoor-Ausrüstung (Cotswold UK) | ca. 90 £ | Webgains-Programm 7795 | VERIFIED |
| Outdoor (REI) | 120–175 USD | Drittangabe | THIRD-PARTY |
| Kamerataschen (Peak Design), Rucksäcke (Osprey) | ca. 150 USD | Drittangaben | THIRD-PARTY |
| Luxus-Koffer (Rimowa) | „oft > 500 USD“ | Drittangabe | THIRD-PARTY |
| Golf-Launch-Monitor (SkyTrak) | Produktpreis deutlich > 1.300 USD (Rabatt 1.300 USD auf ST MAX) | skytrakgolf.com (Banner) | Produktpreis, kein AOV |
| LED-Maske (Solawave) | 399–499 USD Produktpreis | solawave.co (Shop) | Produktpreis, kein AOV |

Für Uhren (Chrono24), E-Bikes, Fashion-Plattformen und 3D-Drucker waren **keine öffentlichen AOV-Angaben** auffindbar.

---

## 4. Auffälligkeiten für eine faceless Instagram-Reels-Theme-Page

**Programme, die Social-only-Seiten ausschließen oder erschweren:**
- **Ellis Brigham (UK):** „Your website must be live and have a top level domain“, ohne eigene Domain also keine Aufnahme.
- **Blue Nile (US):** „You have a live domain“ ist Voraussetzung.
- **Cult Beauty (UK):** „does not work with influencers via the Awin affiliate channel“, Influencer nur in-house.
- **OTTO (DE):** reine Instagram-, TikTok- oder YouTube-Creator nur über Stylink oder Metapic.
- **CALPAK:** nur Partner mit überwiegend US-Publikum.
- **REP Fitness:** nur US-Affiliates, keine bezahlte Social-Werbung; Seiten werden auf Engagement und Qualität des Publikums geprüft.
- **Jackery UK/EU (Webgains):** Keine Pages oder Accounts mit dem Markennamen „Jackery“. Das ist relevant für die Namenswahl einer Theme-Page.
- **Monos:** sucht Presse- und Review-Seiten, keine Coupon-Seiten. **Tortuga:** keine Coupon-Seiten.

**Programme mit ausdrücklicher Social-/Creator-Öffnung:**
Saily („no website necessary“), Viator (Viator Shop / Link-in-Bio), Etsy Creator Collective, eBay Partner Network, Airalo, Holafly, Bluetti, Creality, Anycubic, Miniature Market, Db, BÉIS, Stanley, Aventon, Nike, Canyon, Cotswold Outdoor (Instagram ausdrücklich), Horizn (Programm schließt jedoch). CALPAK bindet Creator über LTK/MagicLinks ein.

**Cookie-Laufzeiten:**
- **Kurz** (für Reels mit verzögertem Kauf ungünstig): eBay 24 h · Cricut 5 Tage · EcoFlow, Nike, Expedia und Miniature Market je 7 Tage · Db 14 Tage (Standard) · REI 15 Tage.
- **Lang:** SafetyWing 364 Tage · Horizn bis 90 Tage · Foreo, Anycubic, Ellis Brigham und Koffer-Direkt je 60 Tage · Travelpro 45 Tage.

**Consent und Attribution:**
- Globetrotter wertet das Affiliate-Cookie als Marketing-Cookie; Tracking läuft nur bei Opt-in des Kunden.
- OTTO verteilt die Provision per dynamischer Attribution auf mehrere Touchpoints.

**Markt-Gefälle:**
- adidas: DE 2 % vs. UK 6 %.
- LOOKFANTASTIC: UK 15 % vs. DACH 12 % vs. US 10 %.
- Chrono24: Programme nur für US und UK sichtbar.
- Hochpreisige Gerätekategorien mit zweistelligen Raten (SkyTrak, medicube, Bambu Lab, NOMATIC) sind überwiegend **US-Programme**.

**Programmänderungen und Schließungen:**
- Horizn Studios DE (Webgains) schließt.
- Airbnb ist seit 2021 eingestellt.
- Thule: Affiliate-Seite liefert 404.
- MATCHES ist 2024 geschlossen (Wissensstand, 2026 nicht erneut geprüft).
- Wiggle und VanMoof liefen nach Insolvenzen 2023 unter neuen Eigentümern weiter (Wissensstand, nicht verifiziert).
- Creality empfiehlt neuen Partnern inzwischen Impact statt Awin.

---

## 5. Datenlücken
- **Impact, Rakuten und Partnerize** veröffentlichen keine Prozentsätze. Das betrifft u. a. WHOOP, Therabody, Tonal, Hydrow, Rad Power, Lectric, TaylorMade, PGA TOUR Superstore, Rapsodo, Callaway, Ulta, Glossier, Sephora US, Estée Lauder, Olaplex, StockX, GOAT, The RealReal, FASHIONPHILE, Mejuri, Ana Luisa, Brilliant Earth, TCGplayer, Fanatics, DJI, NET-A-PORTER und FARFETCH. Die tatsächlichen Konditionen sind nur nach Account-Anmeldung einsehbar.
- **Blockierte Primärseiten (HTTP 403 / Bot-Schutz):** Chrono24, Bambu Lab, REI, Peak Design, Osprey, GetYourGuide, Expedia, StockX, GOAT, The RealReal, WHOOP, Dyson, Boots, Saily (per WebFetch; per curl lesbar).
- **Nicht gefunden:** Chrono24 DE, Zalando- und ABOUT-YOU-Affiliate, Gymshark, Hoka/Brooks/Running Warehouse, Uneekor/Foresight/Rain or Shine, NuFace, Solawave (primär), CurrentBody UK/US, Prusa, Märklin, Games Workshop, Watchfinder, Vestiaire Collective, Roofnest, Gentle Tent, Dometic.
- **Retourenquoten** für Fashion-Programme sind nicht öffentlich. Es gibt nur Proxy-Belege (Bergfreunde 65 % Bestätigung, Bellroy ca. 6 % Retouren).
- **AOV** ist nur für 12 Programme belegt; EPC und Conversion Rate nur für Jackery UK/EU (Webgains) und Aventon.
- Wegen des erschöpften Suchbudgets konnten Sekundärquellen nicht breiter gegengeprüft werden. Einige Drittangaben (Rimowa, Tumi, Peak Design, Osprey, REI, Booking.com) sollten vor einer Entscheidung im jeweiligen Netzwerk-Account verifiziert werden.

---

## 6. Quellenliste

**Awin-Merchant-Profile**
- https://ui.awin.com/merchant-profile/92089 (Monos)
- https://ui.awin.com/merchant-profile/115877 (BÉIS)
- https://ui.awin.com/merchant-profile/109840 (Db Journey DE)
- https://ui.awin.com/merchant-profile/51793 (EcoFlow DE)
- https://ui.awin.com/merchant-profile/51797 (EcoFlow UK)
- https://ui.awin.com/merchant-profile/26895 (Decathlon UK)
- https://ui.awin.com/merchant-profile/14102 (Bergfreunde DE)

**Webgains**
- https://www.webgains.de/front/publisher/program/view/programID/11093 (Horizn Studios DE)
- https://www.webgains.com/front/publisher/program/view/programID/7795 (Cotswold Outdoor UK)
- https://www.webgains.com/front/publisher/program/view/programID/310480 (Jackery UK)
- https://www.webgains.com/front/publisher/program/view/programID/310854 (Jackery EU)

**Offizielle Brand- und Netzwerkseiten**
- https://horizn-studios.com/pages/affiliate
- https://www.calpaktravel.com/pages/affiliate-program
- https://bellroy.com/affiliate-program
- https://travelpro.com/pages/affiliate-program
- https://www.tortugabackpacks.com/pages/affiliates
- https://eaglecreek.com/pages/affiliate-program
- https://www.cabinzero.com/pages/affiliates
- https://www.airalo.com/blog/airalo-affiliate-program-faqs
- https://esim.holafly.com/affiliate-program/
- https://saily.com/affiliate/
- https://partnerresources.viator.com/creator/
- https://www.bergfreunde.de/partnerprogramm-faq/
- https://www.globetrotter-partnerprogramm.de/faq
- https://www.ellis-brigham.com/information/affiliate-programme
- https://us.ecoflow.com/pages/affiliate-program
- https://www.jackery.com/pages/affiliate-program
- https://www.bluettipower.com/pages/affiliate-program
- https://www.bluettipower.eu/pages/affiliate-program
- https://www.stanley1913.com/pages/affiliate-program
- https://www.repfitness.com/pages/affiliate-program
- https://www.bowflex.com/pages/affiliate-program
- https://www.nike.com/help/a/nike-affiliate-program
- https://www.on.com/en-us/explore/affiliates
- https://www.canyon.com/en-us/affiliate-program/
- https://www.aventon.com/pages/affiliate-program
- https://www.2ndswing.com/affiliate-program
- https://www.skytrakgolf.com/pages/affiliates
- https://www.cultbeauty.co.uk/c/info/affiliates/
- https://www.foreo.com/affiliate-program
- https://www.otto.de/partnerprogramm/
- https://partner.zalando.com/partnership/partnership-models
- https://www.bluenile.com/affiliates
- https://partnernetwork.ebay.com/our-program/rate-card (Rate-Card-Bild: https://secureir.ebaystatic.com/cr/v/c1/EPN/Rate%20Card.png)
- https://partnernetwork.ebay.com/page/network-agreement
- https://www.lego.com/en-us/page/affiliate-program
- https://www.etsy.com/affiliates
- https://www.miniaturemarket.com/utility/affiliate-program
- https://www.creality.com/pages/affiliate-program
- https://store.anycubic.com/pages/affiliate-program
- https://cricut.com/en-us/partners
- https://www.solawave.co/pages/affiliate

**Netzwerk-Verzeichnis (THIRD-PARTY, Stand 26.09.2026)**
- `https://www.affiliate-marketing.de/partnerprogramme/<domain>`: abgefragt u. a. für chrono24.com, chrono24.co.uk, jomashop.com, uhrcenter.de, christ.de, thomassabo.com, danielwellington.com, breuninger.com, mytheresa.com, zalando-lounge.de, zalando.de, aboutyou.de, mango.com, revolve.com, rebag.com, farfetch.com, net-a-porter.com, stockx.com, goat.com, sephora.de, douglas.de, flaconi.de, lookfantastic.de, spacenk.com, theordinary.com, dyson.de, ghdhair.com, foreo.com, medicube.us, currentbody.de, olaplex.com, on.com, adidas.de, sport-thieme.de, hyperice.com, onepeloton.de, sportscheck.com, rosebikes.de, bike-components.de, lucky-bike.de, vanmoof.com, skytrakgolf.com, golfhouse.de, golfshop.de, carlsgolfland.com, nomatic.com, monos.com, koffer.de, eastpak.com, travelpro.com, dbjourney.com, airalo.com, hydroflask.com, garmin.com, snowandrock.com, ellis-brigham.com, globetrotter.de, bergfreunde.de, bambulab.com, creality.com, elegoo.com, cricut.com, lego.com, funko.com, revell.de, conrad.de.

**Drittquellen (nur THIRD-PARTY, über Websuche)**
- https://getlasso.co/niche/luggage/ · https://getlasso.co/affiliate/rimowa/ · https://getlasso.co/affiliate/osprey-packs/ · https://getlasso.co/affiliate/arcteryx/ · https://getlasso.co/affiliate/patagonia/ · https://getlasso.co/affiliate/safetywing/ · https://getlasso.co/affiliate/skyscanner/ · https://getlasso.co/affiliate/trip-com/ · https://getlasso.co/affiliate/hostelworld/ · https://getlasso.co/affiliate/the-north-face-au/
- https://www.flexoffers.com/affiliate-programs/away-affiliate-program/ · https://www.flexoffers.com/affiliate-programs/peak-design-affiliate-program/ · https://www.flexoffers.com/affiliate-programs/ikamper-affiliate-program/
- https://www.100partnerprogramme.de/p/koffer-direkt-de-2866/
- https://track360.io/blog/booking-com-affiliate-partner-program-operator-teardown-2026 · https://track360.io/blog/best-travel-affiliate-programs-2026-operator-rate-card-benchmark
- https://help.creator.expediagroup.com/hc/en-us/articles/13164005434519-Understanding-cookies-validity-windows-and-commissions (Snippet)
- https://partner.getyourguide.support/hc/en-us/articles/13981068165917-Our-partner-program (Snippet)
- https://involve.asia/blog/klook-affiliate-program/
- https://www.nichepursuits.com/airbnb-affiliate-program/ · https://hello.pricelabs.co/blog/airbnb-affiliate-program/
- https://genki.world/partners · https://affiliate.watch/affiliate/genki
- https://afprogs.com/rei-affiliate-program/ · https://geniuslink.com/blog/backcountry-affiliate-program/
- https://statsdrone.com/affiliate-programs/yeti-affiliates/
- https://cellesim.com/en/blog/esim-affiliate-programs-travel-creators
- https://www.cuelinks.com/campaigns/tumi-affiliate-program · https://merchant.skimlinks.com/network/5092/Tumi-affiliate-program/offers
- https://linkclicky.com/affiliate-program/cabin-zero/
- https://affiliateprogramfinder.com/affiliate-programs/peak-design-affiliate-program/
- https://www.postaffiliatepro.com/affiliate-program-directory/the-north-face-affiliate-program/
