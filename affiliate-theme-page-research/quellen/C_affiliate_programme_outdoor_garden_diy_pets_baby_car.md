# Teil C – Affiliate-Programme: Outdoor/BBQ, Pools/Spa/Sauna, Garten, Tools/DIY, Cleaning, Automotive, Haustiere, Baby

**Prüfdatum:** 2026-09-26 · **Datensatz:** `raw_programs_C.csv` (157 Programme, 18 Spalten) · **Amazon:** bewusst ausgeklammert (anderer Researcher)

Kontext der Studie: Welche Nische und welcher Markt (DE/DACH, USA, UK, International-Englisch) eignet sich am besten für eine KI-generierte, faceless Instagram-Reels-Theme-Page mit Affiliate-Monetarisierung? Dieser Teil liefert die Programm-Datenbasis für acht „Home & Lifestyle“-Nischen.

---

## 1. Methodik

**Primärquellen (alle am 26.09.2026 abgerufen):**

| Quelle | Was dort öffentlich sichtbar ist | Grenzen |
|---|---|---|
| Awin-Merchant-Profile `ui.awin.com/merchant-profile/<ID>` | Attributionszeitraum (Cookie), Programmbeschreibung des Advertisers. Wenn der Advertiser es veröffentlicht, auch Provisionsgruppen, AOV und Regeln. | EPC, Konversionsrate, Approval-Rate und Netzwerk-AOV sind **nur eingeloggt** sichtbar, nicht im öffentlichen Profil. AOV ist daher nur belegt, wenn der Advertiser ihn selbst nennt. |
| Awin-Advertiser-Verzeichnis `awin.com/<land>/search/advertiser-directory` (Länder: gb/de/us) | Zuordnung Brand zu Awin-ID | Enthält nur aktive Programme. Inaktive Profile, z. B. Weber UK 18897 und weststyle/Weber DE 14763, sind als „not active“ markiert. |
| Impact-Brand-Seiten `app.impact.com/advertiser-advertiser-info/<Brand>.brand` und `advertiser-campaign-info` | Payout je Event, **Referral Period (= Cookie)**, Auszahlungsrhythmus, Kampagnen-Erstellungsdatum, Creator-Kampagnen | Für die Suche musste der exakte Brand-Slug geraten werden. Nicht gefundene Slugs heißen nicht, dass kein Programm existiert. |
| Adcell-Programmseiten `adcell.de/partnerprogramme/<slug>` (Verzeichnis mit 2.353 Programmen gecrawlt) | Provision, Cookie, **„Ø Warenkorb bei ADCELL“**, Stornoquote, Ø- und Max-Freigabezeit, SEM/PLA/Cashback/Gutschein-Regeln | Adcell ist ein DE-Netzwerk mit eher kleinen und mittleren Shops. |
| Affiliate-Seiten der Brands, über deren Sitemaps gefunden | Konditionen, Social-/Creator-Regeln, Netzwerk-Links (CJ-CID, ShareASale-ID) | Einige Seiten sind bot-geschützt (403/429): Solo Stove, BBQGuys, Frontgate, Wayfair, Halfords, tails.com, Crocus, T&M, ATU, Autodoc. |
| Preis-Stichproben: Shopify-Endpunkt `/products.json` der Brand-Shops | Listenpreise der Produkte | Das sind **keine Transaktions-AOVs**. Bundles und Zubehör verzerren den Median. |

**Datenqualitäts-Labels in der CSV:**
- VERIFIED: Wert auf einer Primärquelle gesehen (Brand-Affiliate-Seite oder Netzwerk-Programmseite). Widersprüche auf derselben Primärquelle stehen in `besonderheiten`.
- THIRD-PARTY ESTIMATE: nur in einer Drittquelle belegt. Einziger Fall: Traeger 6 % laut getlasso.co.
- UNKNOWN: nicht öffentlich oder nicht gefunden.
- Bei `aov_bekannt` gibt es zwei Arten von Werten. „Ø Warenkorb bei Adcell“ wird vom Netzwerk gemessen. Angaben mit „vom Brand/Händler genannt“ sind Selbstauskünfte aus dem Programmtext. Preis-Stichproben tragen immer den Zusatz „Stichprobe 26.09.2026“.

**Einschränkungen:**
- Das WebSearch-Kontingent dieser Session war nach etwa 10 eigenen Suchen erschöpft (Session-Limit von 200 Anfragen erreicht). Danach lief die Recherche ausschließlich über direkte Abrufe von Primärquellen und Netzwerkverzeichnissen.
- CJ, Rakuten, Partnerize, Tradedoubler und Webgains haben **keine öffentlich durchsuchbaren Konditionsseiten**. Programme dort sind nur über Angaben der Brand belegt: Chemical Guys und Nanit bei CJ, Click & Grow bei Rakuten/CJ, Roborock zusätzlich bei CJ.
- ShareASale ist seit 2025 in Awin integriert. Mehrere Brand-Seiten verlinken aber noch auf ShareASale: Polywood (143124), Segway Navimow (154959) und Tuft + Paw.
- Social-Media- und Instagram-Regeln stehen meist in den eingeloggten Programm-AGB. „UNKNOWN“ heißt also **nicht verboten**, sondern „nicht öffentlich geregelt“.

---

## 2. Die wichtigsten Befunde auf einen Blick

1. **Die attraktivste Kombination im Scope ist Sauna/Cold Plunge in den USA.** Hier treffen fünfstellige Warenkörbe, 5–10 % Provision und ausdrücklich erlaubte Social-Promotion zusammen:
   - Sun Home Saunas: Impact, 5 %, 30 Tage. Instagram, TikTok und YouTube sind auf der Affiliate-Seite ausdrücklich erlaubt. Stichprobe: Saunen 11.999–45.399 USD.
   - RecoSauna: Awin, 7 %. Produkte kosten 2.000–16.000+ USD; laut Brand sind „commissions > $1,000 per order“ möglich.
   - Sweat Kingdom: Awin, 5–10 %, AOV 4.000–25.000 USD.
   - Sunlighten: 6 %, aber erst beim Vertriebsabschluss.

   Eine einzelne Conversion bringt hier rechnerisch 200–2.000+ USD.
2. **In DE sind es die Spezialhändler.** Das Netzwerk Adcell misst hohe Warenkörbe:
   - Mein-Saunashop: Ø 851 €
   - Kuppelofen (Pizzaöfen): Ø 766 €, 90 Tage Cookie
   - mein-poolroboter.de: Ø 755 €
   - primepool: Ø 628 €
   - Sauna24: Ø 517 €, 8 %, 90 Tage
   - heckenpflanzen.de: Ø 500 €
   - Werkzeug bei myToolStore: Ø 1.143 €

   Die Provisionen liegen meist bei 5–10 %. Dazu kommen SANTOS (Awin, 10 %/7 %, AOV >392 € netto) sowie hagebau (Content 10 %, AOV >260 € netto, 60 Tage).
3. **Große US-Retailer taugen kaum für Instagram-Traffic:**
   - Home Depot: Standard 1 % bei **1 Tag** Referral Period
   - Lowe’s: 1 % bei 1 Tag
   - Ace: 2 % bei 10 Tagen
   - Chewy: 1 % bei 15 Tagen
   - Petco: 2 % bei 7 Tagen
   - Target: 3 % bei 7 Tagen
   - Weber US: 2 %

   Bei Link-in-Bio-Traffic mit verzögertem Kauf gehen hier viele Conversions verloren.
4. **Pizzaöfen sind global gut abgedeckt.**
   - Ooni: ab 10 %, 30 Tage, Awin US/UK/EU, ausdrücklich für Content Creator. Das Programm ist aber *content-only*: keine Gutscheinseiten, kein PPC.
   - Gozney: bis 5 %, AOV >600 USD bzw. >450 GBP, Awin US/UK/DE, „engaged social following“ willkommen.
5. **Tiernahrungs-Abos zahlen fixe Neukunden-CPAs statt Recurring-Provision:**
   - The Farmer’s Dog: 50 USD pro Neukunden-Sale (Impact, 30 Tage)
   - Butternut Box UK: 40 GBP pro Referral über Code, eigenes Programm ausdrücklich für Instagram-/TikTok-„Dogfluencer“
   - Butternut Box DE: 10–15 € (Adcell)
   - tails.com UK: nur 3 GBP
   - Petcube: 20 USD pro zahlendem Abonnenten, für Influencer

   Eine **echte Recurring-Provision wurde im Scope nirgends gefunden**. Blueland weist „Recurring Subscription: 0 %“ sogar explizit aus.
6. **Creator-Kampagnen auf Impact mit höheren Raten als der Standard:**
   - Petlibro: 15 % statt 8 %
   - Eden Brothers: 10 % statt 2 %
   - PetSmart: 5 % statt 2 %
   - Elvie: 8 % statt 4 %
   - Außerdem Creator-Kampagnen ohne ausgewiesene Mehrrate: BBQGuys, Big Green Egg, Renu Therapy, Blueland

   Für eine Theme-Page ist die Creator-Schiene oft der bessere Einstieg.
7. **Chewy hat (wieder) ein öffentliches Programm.** Es läuft seit 03/2025 auf Impact: 1 % bei 15 Tagen, eine weitere 4 %-Kampagne mit unklarem Zweck und 20 USD je Neukunde nur für Tierheime.

---

## 3. Befunde je Nische und Markt

### 3.1 Outdoor Living / BBQ / Pizzaöfen / Feuerstellen (24 Programme)

| Markt | Stärkste Programme (Provision · Cookie · AOV) | Bemerkungen |
|---|---|---|
| **DE** | SANTOS (Awin 10 % Eigenmarke/7 % Fremdmarken · 30 T · AOV >392 € netto); Kuppelofen (Adcell 5 % · 90 T · Ø 766 €); 360° BBQ (Adcell 3–8 % · 30 T · Ø 334 €); grill-profi-shop (Adcell 2,25–7 % · 14 T · Ø 235 €); Czaja Feuerschalen (7,5 % · 90 T · Ø 126 €); Petromax (4–12 % · 60 T · Ø 96 €); Ooni EU (ab 10 %); Gozney DE (bis 5 %); Gartenhausfabrik (7 %); OTTO (Content: Living 12 %) | Die Weber-DE-Programme (weststyle) sind auf Awin inaktiv. Für Grillfürst und höfats wurde kein öffentliches Programm gefunden. Das Awin-Programm „KETTLER DE“ betrifft Spielgeräte, nicht Gartenmöbel. |
| **US** | Outer (Impact 5–8 % · **90 T** · Sets 7.320–17.400 USD); BBQGuys (Impact **6 %** · 30 T, Creator-Kampagne, Call-Tracking 1 %); Ooni US (ab 10 % · 30 T); Gozney US (≤5 % · AOV >600 USD); Solo Stove (5 %, neue 10 %-Kampagne seit 07/2026); Blackstone, Big Green Egg, recteq (je 5 % · 30 T); Traeger (30 T, Provision öffentlich nicht beziffert); Weber (2 %); Polywood (7 T); Wayfair (10 % · 7 T) | BBQGuys ist mit 6 % auf Impact höher als die „typischen 4 %“ auf der eigenen Seite (Suchindex-Auszug). Keine öffentlichen Programme gefunden für Napoleon, Masterbuilt, Kamado Joe (nur Ambassador), Frontgate, Yardbird, Breeo (nur Ambassadors) und Sunnylife. |
| **UK** | Ooni UK (ab 10 %); Gozney UK (≤5 % · AOV >450 GBP) | Das Awin-Profil von Weber UK ist inaktiv. Das UK-Angebot an High-Ticket-Outdoor-Programmen ist öffentlich dünn. |

### 3.2 Pools / Spas / Sauna / Hot Tubs / Cold Plunge (23 Programme)

| Markt | Stärkste Programme | Bemerkungen |
|---|---|---|
| **DE** | Mein-Saunashop (Adcell 4–6 % · 60 T · **Ø 851 €**); Sauna24 (8 % · 90 T · Ø 517 €); AIDA Whirlpools (10 % · 30 T · Ø 387 €, Freigabe Ø 59 T); primepool (7 % · 45 T · Ø 628 €); mein-poolroboter.de (3–5 % · 60 T · Ø 755 €); poolmondo (5 % · 60 T · Ø 395 €); GartenHaus GmbH (Awin 5–7 %, Saunen/Hot & Cold Tubs, **„starke saisonale Nachfrage“**); Hansagarten24 (Awin 3 % Basis, Content/Influencer bis 7–8 % · **90 T**); Bast Sauna DE (6 %); Saunaloft (Awin, Rate nicht öffentlich); Poolwonder (Awin, Zielgruppe „Blogs & Influencer“, kein SEA) | Für Poolsana, Pool-Discount, Intex und Bestway/Lay-Z-Spa wurde kein öffentliches Programm gefunden. POOL Total hat nur 5 Tage Cookie. |
| **US** | Sun Home (Impact 5 % · 30 T · Social ausdrücklich erlaubt); RecoSauna (Awin 7 %); Sweat Kingdom (Awin 5–10 % · AOV 4–25k USD); Peak Saunas (3–5 %, nur Lower 48); Renu Therapy (Impact 7 %, Creator-Kampagne); Sunlighten (6 % auf „Opportunity Closed“); Plunge (nur 3 %); Wave Spas US (Awin, Rate nicht öffentlich) | Ice Barrel bietet nur Ambassador- und Challenge-Formate, Almost Heaven nur ein Referral-Programm. Für Clearlight wurde kein Programm gefunden. |
| **UK** | Bast Sauna UK (Awin 6 % · 30 T); Wave Spas UK (Awin, aufblasbare Hot Tubs, Rate nicht öffentlich); Sunlighten (Lead-/Deal-Kampagne in GBP) | Für Hot Tub Store, Aqua Hot Tubs, Wellis und Lay-Z-Spa wurden keine öffentlichen Programme gefunden. |

### 3.3 Garten (20 Programme)

| Markt | Stärkste Programme | Bemerkungen |
|---|---|---|
| **DE** | STIHL (Awin **8 % CPO**, 5 % bei Gutschein · 30 T · Feed; nur Startseiten- und Kategorie-Deeplinks); BALDUR-Garten (8 % · **90 T** · SEM verboten); Pflanzen-Kölle (8 %); Plantura (Adcell 10 % · Ø 69 € · **Stornoquote 41 %**); Garten von Ehren (10 % · Ø 84 €); heckenpflanzen.de (5 % · 14 T · **Ø 500 €**, kein SEM/Cashback/Gutschein); Mähroboter: ANTHBOT DE (Awin ≥10 %), Mammotion (Impact 3 % inkl. DE-Kampagne), Ecovacs DE/GOAT (Awin 5 %) | **STIHL hat ein Programm** (Awin 20646). Für Gardena, Husqvarna, Worx, Einhell, Bakker und Lubera wurde kein öffentliches Programm gefunden. Die Baumärkte stehen unter Tools/DIY. |
| **US** | Gardyn (Impact **12–100 USD fix** pro Sale); Click & Grow (eigenes Programm 10 %+ · 30 T; Deal-Seiten über Rakuten/CJ); Lettuce Grow (Impact 4 % · Farmstand 599–1.449 USD); The Sill (bis 10 %); Eden Brothers (2 %, Creator 10 %); Gardener’s Supply (4 %); Lively Root (Awin 5 %+, Code-Programm bis 20 %); Navimow (ShareASale, **90 T**, Rate nicht öffentlich · Mähroboter 799–3.199 USD); Greenworks (3–6 %) | Für Burpee, Bloomscape, AeroGarden und Horti wurde nichts gefunden. Das Awin-Profil „Léon & George“ existiert (90391), enthält aber keine Konditionen. |
| **UK** | Thompson & Morgan (Awin 8 % netto · „key sales period is the spring“); Crocus (10 % Pflanzen/7 % Produkte); Mammotion UK (3 %) | Für Patch Plants wurde kein Programm gefunden. |

### 3.4 Tools / DIY / Home Improvement (15 Programme)

| Markt | Stärkste Programme | Bemerkungen |
|---|---|---|
| **DE** | hagebau (Awin, Content **10 %** · **60 T** · AOV >260 € netto); toom (Content 8 %, Feed); BAUHAUS (Inhouse/Sunlab: Content/Influencer/Cashback 7 %, Standard 5 % · 30 T · 1st-Party + Server-Tracking); OBI (Content 7 %, Standard 2 %; Click & Collect sowie HeyOBI-App nicht vergütet); myToolStore (Adcell 4–10 % · **Ø 1.143 €**); Contorion (bis 6 %, **Influencer über Awin ausgeschlossen**, nur Direktkooperation); Toolineo (2–5 % · 60 T); Globus (Rate nicht öffentlich, Konversionsrate >5,4 %) | Für Hornbach wurde weder auf Awin noch auf Adcell ein Programm gefunden. Von Bosch gibt es nur das Hausgeräte-Programm (4 %), kein Power-Tools-Programm. Für Einhell, Wera, Knipex und Festool wurde nichts Öffentliches gefunden. |
| **US** | The Home Depot (1–8 %, Standard **1 % bei 1 Tag**; 8 %-Kampagne mit 14 T); Lowe’s (1 % · 1 T); Ace (2 % · 10 T); Acme Tools (2 % · 15 T); VEVOR (5 % · 30 T) | Marken wie Ryobi, Milwaukee, Makita und DeWalt monetarisiert man in den USA praktisch nur über Händler. Das ist für Reels schwach, weil die Cookies extrem kurz sind. Für Harbor Freight wurde kein Programm gefunden. |
| **UK** | B&Q (Kingfisher/Impact 2 %, TradePoint 4 % · 30 T); Robert Dyas (Awin 1 %) | Für Screwfix und Toolstation wurde kein öffentliches Programm gefunden. |

### 3.5 Cleaning / Home Organization (17 Programme)

| Markt | Stärkste Programme | Bemerkungen |
|---|---|---|
| **DE** | Dyson DE (Awin: Editorial Content **7 %**, Cashback 5 %, Coupon 2 %; Zubehör ausgeschlossen); SharkNinja DE (bis 5 %, **Influencer-Gruppe 5 %**, AOV 146 €, 30 T Validierung); Ecovacs DE (5 %); Vorwerk (Kobold 5 %, Thermomix nur 10 € fix, **60 T**); Bosch Hausgeräte (4 %); Cleangang (Adcell 5–9 %, Storno 58 %) | Für Kärcher und Brabantia wurde kein öffentliches Programm gefunden. Dreame DE läuft auf Impact mit 0 % (Platzhalter). |
| **US** | Roborock (4–7 % · AOV >400 USD · Feed auf Impact; Cookie auf derselben Seite widersprüchlich: 35/45 T); Dreame (6–15 %, neue 10 %-Kampagne); Yamazaki Home (**7 %**, direkt über Impact); simplehuman (5 % · 15 T); Blueland (5–20 %, Abo 0 %); Branch Basics (10 % · AOV ~60 USD); SharkNinja US (4 % · 7 T, neue 10 %-Kampagne · 30 T); Tineco (5 %); Container Store (2 %) | Grove und Branch Basics bieten zusätzlich Referral-Programme an. Für Open Spaces und Bissell wurde nichts gefunden. |
| **UK** | Joseph Joseph (3 %, Influencer 5 % · Feed); Ecovacs UK (5 %); Tineco UK (5 %); Dyson UK (Impact nur **1 %**) | Dyson UK zahlt deutlich weniger als die Content-Stufe in DE. |

### 3.6 Automotive / Car Detailing (17 Programme)

| Markt | Stärkste Programme | Bemerkungen |
|---|---|---|
| **DE** | Autodoc (Awin 8 %, 4 % Bestandskunden; Cookie laut Text 45 T, im Header 30 T); kfzteile24 (Neukunden 6–8 %, Bestandskunden 4–6 %; Zielgruppe zu 90 % männlich); Nextbase DE (6 %); Motointegrator (2–7 % · AOV 160 €); Tirendo (3 %, saisonal); Speed-Reifen (Adcell 10 % · Ø 116 €); Autoteile-Preiswert (5–9 % · 60 T) | Für ATU wurde kein öffentliches Programm gefunden. Reifen zeigen eine klare Saisonalität (Frühjahr/Herbst, die Programme sprechen von „saisonalen Aktionen“). |
| **US** | Chemical Guys (CJ, **bis 10 %**, Ø Sale >100 USD); Advance Auto Parts (4 % · 30 T + Influencer-Kampagne); Nextbase US (5 % · 14 T); CARiD (1 %); JEGS (1–3 % · 5 T · AOV 260 USD) | Für AutoZone, CarParts.com, RockAuto, WeatherTech, Thule, Rhino-Rack, Tire Rack, Viofo, Adam’s Polishes und Griot’s wurde kein öffentliches Programm gefunden. |
| **UK** | Nextbase UK (**8 %**); Autodoc UK (8 %/4 %); Black Circles (Reifen, AOV 200–250 GBP, **„Social media influencers“ ausdrücklich gesucht**, Rate nicht öffentlich); Euro Car Parts (3 %); Tirendo UK (Content 4 %) | Für Halfords wurde kein öffentliches Programm gefunden (Shop blockiert Bots). |

### 3.7 Haustiere (20 Programme)

| Markt | Stärkste Programme | Bemerkungen |
|---|---|---|
| **DE** | Fressnapf (Neukunden 8 %, Bestandskunden 4 % · **60 T**); ZooRoyal (DE-Seite 3–12 %; AT-Profil Content 11 % Neukunden/5 % Bestandskunden · 60 T); zooplus DE (**3 % nur für die ersten 3 Bestellungen**, danach 1 %; AOV 65 €; Konversionsrate >15 %); Medpets (bis 8 % · AOV 45 €); wildfang.pet (Adcell 10–13 % · 60 T); LuckyPets (Neukunden **20 %**); Butternut Box DE (10–15 € pro Box · 7 T) | Die Warenkörbe sind niedrig (40–70 €). Hohe Konversionsraten gleichen das teilweise aus. |
| **US** | Whisker/Litter-Robot (Impact **8 % · 90 T**); The Farmer’s Dog (**50 USD CPA** · 30 T); Petlibro (8 %, Creator 15 %); Tuft + Paw (12 % · 60 T); Petcube (10 % · 60 T, 20 USD/Abo für Creator); Wild One (Ambassador 10 %, Social Snowball); Chewy (1 % · 15 T); PetSmart (2 %, Creator 5 %); Petco (2 % · 7 T); Ollie (Impact, Rate nicht öffentlich) | Für BarkBox, Fable, Fi, Furbo, PetSafe, KONG und Catit wurden keine öffentlichen Programme gefunden. |
| **UK** | zooplus UK (**7 %** auf die ersten 3 Bestellungen · AOV 46 GBP · Konversionsrate >22 % · Influencer ausdrücklich zugelassen); Butternut Box UK (**40 GBP** pro Referral, Instagram/TikTok ausdrücklich); tails.com (3 GBP) | Für Pets at Home wurde kein öffentliches Programm gefunden. |

### 3.8 Baby / Parenting (21 Programme)

| Markt | Stärkste Programme | Bemerkungen |
|---|---|---|
| **DE** | CYBEX DE (Awin bis **6 %** · AOV 350 € · keine Gutschein-/Cashback-Seiten); Babybrands (Adcell 2–7 % · Ø 224 € · **Freigabe 98 T**); babyandfamily (3–7 % · Ø 180 €); Pinolino (5 % · AOV ~180 €); baby-walz (6 % · **10 T**); babymarkt (5 %); Joolz (Rate nicht öffentlich) | Für babyone, windeln.de, Stokke, Bugaboo, Maxi-Cosi und Flexa wurde kein öffentliches Programm gefunden. |
| **US** | Momcozy (Impact **10 %** · 30 T); CYBEX US (6 %); Elvie (4 %, Creator 8 %); Hatch (4 %); Happiest Baby/SNOO (4 % · 7 T; 25 USD je Miet-Versand); Babylist (Standard 1 %, 1–20 %, 5 USD je Registry-Sign-up); Target (3 % · 7 T); Nanit (CJ, Rate nicht öffentlich); Owlet (Awin, 45 T) | Für KiwiCo, UPPAbaby und Pottery Barn Kids wurde nichts gefunden. Lovevery US läuft über ein GRIN-Creator-Programm. |
| **UK** | Lovevery UK (Impact **10 %**); CYBEX UK (bis 5 % · AOV 350 GBP); Mamas & Papas (bis 5 %, Social-Kanäle ausdrücklich genannt, Feed); Silver Cross (3 % · AOV 360+ GBP · **Validierung bis 120 T**) | Für JoJo Maman Bébé wurde kein Programm gefunden. |

---

## 4. Typische AOV-Spannen der Hauptprodukte

### 4.1 Vom Netzwerk gemessen (Adcell „Ø Warenkorb bei ADCELL“, Stand 26.09.2026)

| Nische | Programm | Ø Warenkorb |
|---|---|---|
| Tools | myToolStore | 1.143,36 € |
| Sauna | Mein-Saunashop | 851,21 € |
| Pizzaöfen | Kuppelofen | 766,22 € |
| Pool | mein-poolroboter.de | 754,62 € |
| Pool | primepool.de | 628,30 € |
| Sauna | Sauna24 | 517,18 € |
| Garten | heckenpflanzen.de | 500,00 € |
| Pool | poolmondo.de | 394,95 € |
| Whirlpool | AIDA Whirlpools | 386,52 € |
| BBQ | 360° BBQ | 334,28 € |
| BBQ | grill-profi-shop | 234,90 € |
| Baby | Babybrands | 223,57 € |
| Baby | babyandfamily | 180,47 € |
| Pool-Zubehör | POOL Total | 165,35 € |
| Feuerschalen | Czaja | 125,84 € |
| Auto | Speed-Reifen | 116,06 € |
| Sauna-Zubehör | SAUNA Total | 99,00 € |
| Outdoor | Petromax | 96,22 € |
| Garten | Garten von Ehren | 84,42 € |
| Tools | Toolineo | 83,32 € |
| Garten | Plantura | 69,15 € |
| Haustiere | Butternut Box DE | 50,00 € |
| Haustiere | wildfang.pet | 44,71 € |
| Cleaning | Cleangang | 36,04 € |

### 4.2 Vom Advertiser selbst genannt (Awin/Impact-Programmtext)

| Programm | AOV-Angabe |
|---|---|
| Sweat Kingdom Saunas (US) | 4.000–25.000 USD |
| RecoSauna (US/CA) | Produkte 2.000–16.000+ USD |
| Gozney | >600 USD / >450 GBP / >900 AUD |
| Roborock US | >400 USD |
| SANTOS DE | >392 € netto |
| Silver Cross UK | 360+ GBP |
| CYBEX DE / UK | 350 € / 350 GBP |
| hagebau.de | >260 € netto |
| JEGS | 260 USD |
| Black Circles UK | 200–250 GBP |
| Pinolino DE | ~180 € |
| Motointegrator | 160 € |
| SharkNinja DE | 146 € |
| Chemical Guys | >100 USD |
| zooplus DE / UK | 65 € / 46 GBP |
| Branch Basics | ~60 USD |
| ZooRoyal AT | >50 € |
| Medpets | 45 € |

### 4.3 Preis-Stichproben (Listenpreise, Shopify-Produktfeeds, abgerufen 26.09.2026)

| Brand/Shop | Stichprobe |
|---|---|
| Sun Home Saunas (US) | 38 Produkte, Median 3.899 USD; Nova Indoor-Sauna 11.999–15.799 USD; Luminar Outdoor Infrarot 13.899 USD; Solaris Outdoor 36.399–45.399 USD; Cold Plunge Pro Titan 15.199 USD |
| Plunge (US) | Infrared Sauna 7.690 USD; Sauna Pro 7.990–8.490 USD; Plunge All-In + Sauna-Bundle 15.680 USD |
| Outer (US) | 250 Produkte, Median 1.705 USD; Lounge-/Dining-Sets 7.320–17.400 USD |
| POLYWOOD (US) | Median 2.995 USD; 9-teilige Sets 5.849–10.149 USD |
| Gozney (US) | Arc Lite 399,99 USD; Arc XL 999,99 USD; Dome Gen 2 Essentials-Bundle 2.889,97 USD; Dome XL Ultimate-Bundle 4.114,92 USD |
| Ooni (US/UK/EU) | US: Median 90 USD (123 Produkte), Koda 2 Max Outdoor Kitchen Bundle 1.837 USD; UK: Koda 2 Essentials-Bundle 460 GBP, Koda 2 Max-Bundle 1.058 GBP; EU: Koda 2 Essentials-Bundle 539 €, Koda 2 Max 999 € |
| Blackstone (US) | Griddle-Bundles 299–1.399 USD; Median 79,99 USD |
| Kamado Joe (US) | Maximalpreis im Feed 3.517,99 USD |
| Segway Navimow (US) | Mähroboter 799 USD (i105e) bis 3.199 USD (X4) |
| Lettuce Grow (US) | Farmstand 599–1.449 USD |
| Click & Grow | Smart Garden 9 PRO 299,95 USD; Smart Garden 27 899,95 USD |
| Petlibro (US) | Futterautomaten und Brunnen ca. 40–400 USD |
| Tuft + Paw (US) | Kratzbäume 299 USD; Median 50,50 USD |
| Momcozy (US) | Milchpumpen 225–370 USD |
| Nanit (US) | Babyphone 249–869 USD |
| tonies (US) | Toniebox 2 Starter Set 149,99 USD |

**Ableitung (Einschätzung des Researchers):** Grob ergeben sich drei Tiers.

| Tier | Warenkorb | Nischen und Programme | Provision pro Sale |
|---|---|---|---|
| Hoch | 1.000–45.000 USD | Saunen, Cold Plunges, Outdoor-Möbel-Sets, Outdoor-Küchen/BBQGuys, Premium-Pizzaöfen (Dome) | 5–10 % ergeben 50–2.000+ USD |
| Mittel | 150–1.000 € | Pool-Technik, Mähroboter, Saugroboter, Kinderwagen, Pizzaöfen Einstieg, Werkzeug | ca. 10–80 € |
| Niedrig | 35–120 € | Tierbedarf, Pflanzen, Reinigungsmittel, Autoteile | 2–10 € pro Sale |

Im Niedrig-Tier sind hohe Konversionsraten und Wiederkäufe nötig.

---

## 5. Saisonalität

**Von den Brands selbst genannt (Primärquelle):**
- Thompson & Morgan (UK): „Our key sales period is the spring“; zusätzlich saisonale Cookie-Aktionen.
- GartenHaus GmbH (DE, Saunen/Hot Tubs/Gartenhäuser): „Starke saisonale Nachfrage“, „starke saisonale Themenwelten“.
- ANTHBOT (Mähroboter DE): „Seasonal promotions“.
- Tirendo DE/UK: „Spezielle saisonale Aktionen und Kampagnen“, typischerweise Reifenwechsel.
- kfzteile24: „vielfältige, saisonabhängige Aktionen“.

**Aus Kampagnen-Zeitstempeln ablesbar:**
- Big Green Egg hat 09/2026 neue Impact-Kampagnen aufgesetzt, also Vorbereitung auf die Saison 2027 bzw. das Holiday-Geschäft.
- Solo Stove führte im 07/2026 eine 10 %-Kampagne ein.
- primepool meldete im 04/2026 „zahlreiche Bewerbungen“, poolmondo startete im 08/2025.

**Einschätzung des Researchers, nicht als Brand-Aussage belegt:**
- Pool, Garten, Grill und Mähroboter haben in DACH/UK/US ihre Nachfragespitze etwa zwischen März und August.
- Sauna, Hot Tub und Cold Plunge verhalten sich eher gegenläufig: Herbst und Winter sind stark, Cold Plunge teils ganzjährig.
- Eine „Backyard & Wellness“-Page, die Sommer-Outdoor und Winter-Sauna kombiniert, würde die Saisonalität glätten.
- Tierbedarf, Cleaning und Baby sind weitgehend ganzjährig, mit Q4-Peaks (Black Friday, Weihnachten).

Adcell bietet Publishern zusätzlich einen eigenen „Saisonkalender“ (Tool im Netzwerk).

---

## 6. Auffälligkeiten mit Relevanz für eine Instagram-Theme-Page

**Social/Instagram ausdrücklich erwünscht (Primärquelle):**
- Eigene Social-Regeln oder -Zielgruppen: Sun Home Saunas (Instagram, TikTok, YouTube wörtlich genannt), Butternut Box UK („Instagram, TikTok, YouTube“), Ooni (Content Creators; Social-Posts im Wettbewerb), Gozney („engaged social following“), POLYWOOD (Social Media Accounts), Black Circles („Social media influencers“), zooplus UK (Influencer/Content Creator zugelassen), Poolwonder (Zielgruppe Blogs & Influencer).
- Eigene Influencer-Provisionsstufen: BAUHAUS (7 %), SharkNinja DE (5 %), Joseph Joseph (5 %), Hansagarten (bis 7–8 %).
- Creator-/Ambassador-Programme: Wild One, Petcube, Mamas & Papas, Lovevery (GRIN), Click & Grow, Lettuce Grow (Superfiliate).
- Creator-Kampagnen auf Impact: BBQGuys, Big Green Egg, Renu Therapy, Eden Brothers, PetSmart, Petlibro, Elvie, Blueland, Acme Tools (Platzhalter).

**Social ausgeschlossen oder eingeschränkt:**
- **Contorion (DE)** schließt „individuelle Influencer“ im Awin-Programm aus; nur Direktkooperation über social@contorion.de.
- **CYBEX DE** lehnt Bestellungen von Rabattcode- und Cashback-Seiten ab. Das trifft Instagram-Accounts, die mit Codes arbeiten.
- **Ooni** ist content-only: Gutscheine/Incentives und PPC sind verboten, eine gewöhnliche Social-Promotion bleibt aber erlaubt.
- **Silver Cross** lehnt Sales ab, wenn der Last Click nicht Awin war.
- **Code-basiertes Tracking** (Butternut UK, Wild One, Lively Root) eignet sich für Reels besser als Link-in-Bio, weil der Code auch ohne Klick zugeordnet wird.

**Cookie-Länge:**

| Kategorie | Programme |
|---|---|
| Kritisch kurz (≤7 Tage) | Home Depot (1 T), Lowe’s (1 T), JEGS (5 T), POOL Total (5 T), Petco, Wayfair, SharkNinja US (Standard), Happiest Baby, Target, Butternut Box DE, POLYWOOD (je 7 T) |
| Knapp | Babywalz (10 T), Ace (10 T) |
| Lang (≥60 Tage) | 90 T: Outer, Navimow, Litter-Robot, BALDUR, Hansagarten, Kuppelofen, Sauna24, Czaja. 60 T: Petcube, Tuft + Paw, Fressnapf, ZooRoyal, hagebau, Vorwerk, Mein-Saunashop, poolmondo, mein-poolroboter, wildfang, Petromax, Toolineo, Autoteile-Preiswert |

**Neukunden-Logik:**
- Nach Neu-/Bestandskunde gestaffelt: zooplus (3 % bzw. 7 % nur auf die ersten 3 Bestellungen), Fressnapf, ZooRoyal, kfzteile24, Autodoc, LuckyPets.
- Nur Neukunden: tails.com, The Farmer’s Dog, Butternut.

**Validierung und Storno:**

| Merkmal | Programme |
|---|---|
| Lange Validierung | Silver Cross (bis 120 T), Babybrands (98 T), AIDA (Ø 59/max. 70 T), 360° BBQ (Ø 44/max. 63 T). Sunlighten zahlt erst bei „Opportunity Closed“. |
| Hohe Stornoquote | Cleangang 58 %, Plantura 41 % |
| Niedrige Stornoquote | SANTOS, zooplus (~2 %), ZooRoyal (<2 %) |

**Weitere Auffälligkeiten:**
- **Keine Recurring-Provisionen im Scope.** Abo-Brands (Farmer’s Dog, Butternut, tails.com, Blueland, Petcube, Gardyn) zahlen einmalige CPAs oder ausdrücklich 0 % auf Folgeumsätze.
- **Programme mit widersprüchlichen Cookie-/Provisionsangaben auf derselben Primärquelle:**
  - Roborock: 35 vs. 45 Tage
  - Autodoc: 30 vs. 45 Tage
  - Lively Root: 7 vs. 30 Tage
  - mein-poolroboter: 3 % vs. 5 %
  - zooplus: „bis 3 %“ auf der Shopseite, 3 %/1 % im Awin-Profil
- **DE vs. US vs. UK im Vergleich:**
  - **DE** bietet die meisten öffentlich einsehbaren Konditionen (Awin + Adcell) und häufig 5–10 % Provision. Bei Spezialhändlern sind die Warenkörbe dreistellig. Eine DE-Page braucht deutschsprachigen Content, der Markt ist kleiner.
  - **US** hat die höchsten absoluten Tickets (Sauna, Outdoor-Möbel, Pizzaöfen) mit 5–10 % bei D2C-Brands. Die großen Retailer zahlen dagegen 1–2 % bei 1–15 Tagen Cookie.
  - **UK** ist öffentlich am dünnsten besetzt, besonders bei Hot Tubs und Outdoor-Möbeln. Stark sind Garten (T&M, Crocus), Auto (Nextbase 8 %, Autodoc 8 %) und Pet-Abos (Butternut 40 GBP).
  - **International-Englisch** funktioniert am besten mit Marken, die US-, UK- und EU-Kampagnen parallel betreiben: Ooni, Gozney, Mammotion, Happiest Baby, Tineco, Solo Stove (US+EU), VEVOR.

---

## 7. Datenlücken

- **Kein öffentliches Programm gefunden.** Das heißt nicht, dass keines existiert: Die Suche lief ohne Websuche, nur über Awin-Verzeichnis, Impact-Slugs, Adcell-Verzeichnis und Brand-Sitemaps. Betroffen sind:
  - Outdoor/BBQ: Napoleon, Masterbuilt, Kamado Joe (nur Ambassador), Frontgate, Yardbird, Sunnylife, Breeo (nur Ambassadors), höfats, Grillfürst, Kettler-Gartenmöbel
  - Pools/Spa/Sauna: Intex, Bestway/Lay-Z-Spa, Hot Tub Store, Aqua Hot Tubs, Wellis, Ice Barrel (nur Ambassador/Challenge), Clearlight, Almost Heaven (nur Referral), Poolsana, Pool-Discount
  - Garten: Gardena, Husqvarna, Worx, EcoFlow, Bakker, Lubera, Burpee, Bloomscape, Horti, Patch, AeroGarden
  - Tools/DIY: Hornbach, Screwfix, Toolstation, Harbor Freight, Bosch Power Tools, Makita, Milwaukee, DeWalt, Einhell, Festool, Wera, Knipex
  - Cleaning: Kärcher, Bissell, Brabantia, Grove (nur Referral), Open Spaces
  - Automotive: AutoZone, CarParts.com, RockAuto, ATU, Halfords, WeatherTech, Thule, Rhino-Rack, Viofo, Tire Rack, Tesla-Zubehörhändler, Adam’s Polishes, Griot’s Garage
  - Haustiere: Pets at Home, BarkBox, Fable, Fi, Furbo, PetSafe, KONG, Catit, Tractive, Lyka
  - Baby: Pottery Barn Kids, UPPAbaby, Bugaboo, Stokke, Maxi-Cosi, KiwiCo, JoJo Maman Bébé, babyone, windeln.de, Flexa
- **Provision nicht öffentlich** trotz belegtem Programm: Traeger (nur Drittquelle 6 %), Navimow, POLYWOOD, Ollie, Nanit, Owlet, Saunaloft, Wave Spas UK/US, Poolwonder, Globus, Joolz, Black Circles, tonies US, Wild One (Awin-Teil).
- **Nicht öffentlich einsehbar:** EPC, Konversionsrate und Approval-Rate auf Awin (Login nötig). Ausnahmen sind Selbstauskünfte der Advertiser: Ooni 2,5 %, zooplus >15 % bzw. >22 %, Globus >5,4 %/92 %, Autodoc >5,5 %.
- **Social-Media-Regeln** sind in der Mehrheit der Programme nicht öffentlich (AGB hinter Login). Vor einer Bewerbung also im Einzelfall prüfen.
- **Transaktions-AOVs aus den USA** sind nicht öffentlich. Die Preis-Stichproben sind Listenpreise, keine Warenkörbe.

---

## 8. Quellenliste

**Methodische Quellen und Verzeichnisse:**
- Awin-Advertiser-Verzeichnis: https://www.awin.com/gb/search/advertiser-directory · https://www.awin.com/de/search/advertiser-directory · https://www.awin.com/us/search/advertiser-directory
- Adcell-Programmverzeichnis: https://www.adcell.de/partnerprogramme
- Impact-Brand-Seiten (Muster): https://app.impact.com/advertiser-advertiser-info/<Brand>.brand
- 100partnerprogramme.de (Sekundärquelle, nur für BAUHAUS-Netzwerkinfo): https://www.100partnerprogramme.de/p/bauhaus-4247/
- getlasso.co (Drittquelle, nur Traeger): https://getlasso.co/affiliate/traeger-grills/
- Preis-Stichproben (Shopify-Produktfeeds, 26.09.2026): https://sunhomesaunas.com/products.json · https://plunge.com/products.json · https://liveouter.com/products.json · https://www.polywood.com/products.json · https://us.gozney.com/products.json · https://ooni.com/products.json · https://uk.ooni.com/products.json · https://eu.ooni.com/products.json · https://blackstoneproducts.com/products.json · https://www.kamadojoe.com/products.json · https://navimow.segway.com/products.json · https://www.lettucegrow.com/products.json · https://www.clickandgrow.com/products.json · https://petlibro.com/products.json · https://www.tuftandpaw.com/products.json · https://momcozy.com/products.json · https://www.nanit.com/products.json · https://us.tonies.com/products.json

**Programm-Quellen (alle in der CSV referenzierten URLs):**

- https://ui.awin.com/merchant-profile/77074
- https://ui.awin.com/merchant-profile/77076
- https://ui.awin.com/merchant-profile/77082
- https://eu.ooni.com/pages/become-an-affiliate
- https://ui.awin.com/merchant-profile/16803
- https://ui.awin.com/merchant-profile/16804
- https://ui.awin.com/merchant-profile/32287
- https://app.impact.com/campaign-promo-signup/Traeger-Grills.brand
- https://getlasso.co/affiliate/traeger-grills/
- https://app.impact.com/advertiser-campaign-info/Weber-Inc.brand
- https://app.impact.com/advertiser-campaign-info/BBQGuys.brand
- https://www.bbqguys.com/corporate/about/affiliates
- https://app.impact.com/advertiser-advertiser-info/Solo-Stove.brand
- https://app.impact.com/advertiser-campaign-info/Blackstone-Products.brand
- https://app.impact.com/advertiser-advertiser-info/Big-Green-Egg.brand
- https://app.impact.com/advertiser-campaign-info/recteq.brand
- https://app.impact.com/advertiser-campaign-info/Outer.brand
- https://www.polywood.com/pages/affiliate-program
- https://ui.awin.com/merchant-profile/125006
- https://www.adcell.de/partnerprogramme/360-bbq
- https://www.adcell.de/partnerprogramme/grill-profi-shop
- https://www.adcell.de/partnerprogramme/kuppelofen
- https://www.adcell.de/partnerprogramme/petromax
- https://www.adcell.de/partnerprogramme/czaja-feuerschalen
- https://ui.awin.com/merchant-profile/76696
- https://ui.awin.com/merchant-profile/14336
- https://app.impact.com/advertiser-campaign-info/Wayfair.brand
- https://app.impact.com/advertiser-campaign-info/Sun-Home.brand
- https://sunhomesaunas.com/pages/become-an-affiliate
- https://app.impact.com/advertiser-campaign-info/Plunge.brand
- https://app.impact.com/advertiser-advertiser-info/Sunlighten.brand
- https://app.impact.com/advertiser-advertiser-info/Renu-Therapy.brand
- https://ui.awin.com/merchant-profile/128491
- https://ui.awin.com/merchant-profile/125462
- https://ui.awin.com/merchant-profile/118291
- https://ui.awin.com/merchant-profile/119247
- https://ui.awin.com/merchant-profile/119243
- https://ui.awin.com/merchant-profile/25645
- https://ui.awin.com/merchant-profile/22747
- https://www.gartenhaus.com/page/partnerprogramm
- https://ui.awin.com/merchant-profile/119819
- https://ui.awin.com/merchant-profile/125982
- https://ui.awin.com/merchant-profile/125991
- https://ui.awin.com/merchant-profile/44061
- https://www.adcell.de/partnerprogramme/aida-whirlpools
- https://www.adcell.de/partnerprogramme/sauna24
- https://www.adcell.de/partnerprogramme/mein-saunashop
- https://www.adcell.de/partnerprogramme/saunatotal
- https://www.adcell.de/partnerprogramme/primepool.de
- https://www.adcell.de/partnerprogramme/poolmondo.de
- https://www.adcell.de/partnerprogramme/mein-poolroboter.de
- https://www.adcell.de/partnerprogramme/pool-total
- https://ui.awin.com/merchant-profile/20646
- https://www.stihl.de/de/service-events/kooperationsprogramm
- https://ui.awin.com/merchant-profile/28417
- https://ui.awin.com/merchant-profile/13634
- https://www.baldur-garten.de/onion/content/affiliate-partnerprogramm
- https://www.adcell.de/partnerprogramme/plantura-shop
- https://www.adcell.de/partnerprogramme/garten-von-ehren
- https://www.adcell.de/partnerprogramme/heckenpflanzen.de
- https://ui.awin.com/merchant-profile/2283
- https://ui.awin.com/merchant-profile/7833
- https://ui.awin.com/merchant-profile/29729
- https://www.livelyroot.com/pages/affiliates
- https://app.impact.com/advertiser-campaign-info/The-Sill.brand
- https://app.impact.com/advertiser-advertiser-info/Eden-Brothers.brand
- https://app.impact.com/advertiser-campaign-info/Gardeners-Supply-Company.brand
- https://app.impact.com/advertiser-advertiser-info/Gardyn.brand
- https://www.clickandgrow.com/pages/affiliate-program
- https://app.impact.com/advertiser-campaign-info/Lettuce-Grow.brand
- https://www.lettucegrow.com/pages/affiliate
- https://navimow.segway.com/pages/affiliate-program
- https://app.impact.com/advertiser-advertiser-info/Mammotion-Tech.brand
- https://ui.awin.com/merchant-profile/125144
- https://ui.awin.com/merchant-profile/30763
- https://app.impact.com/advertiser-advertiser-info/Greenworks-Tools.brand
- https://app.impact.com/advertiser-advertiser-info/The-Home-Depot.brand
- https://app.impact.com/advertiser-campaign-info/Lowes.brand
- https://app.impact.com/advertiser-campaign-info/Ace-Hardware.brand
- https://app.impact.com/advertiser-advertiser-info/Acme-Tools.brand
- https://app.impact.com/advertiser-advertiser-info/VEVOR.brand
- https://app.impact.com/advertiser-advertiser-info/Kingfisher.brand
- https://ui.awin.com/merchant-profile/1528
- https://ui.awin.com/merchant-profile/9326
- https://ui.awin.com/merchant-profile/11513
- https://ui.awin.com/merchant-profile/16017
- https://toom.de/wissen-service/toom-affiliate-programm/
- https://affiliates.bauhaus.info/
- https://www.100partnerprogramme.de/p/bauhaus-4247/
- https://ui.awin.com/merchant-profile/14578
- https://ui.awin.com/merchant-profile/11830
- https://www.adcell.de/partnerprogramme/mytoolstore
- https://www.adcell.de/partnerprogramme/toolineo
- https://ui.awin.com/merchant-profile/12802
- https://app.impact.com/advertiser-campaign-info/Dyson.brand
- https://app.impact.com/advertiser-advertiser-info/SharkNinja.brand
- https://ui.awin.com/merchant-profile/19810
- https://app.impact.com/advertiser-advertiser-info/Tineco.brand
- https://app.impact.com/advertiser-advertiser-info/Dreametech.brand
- https://us.roborock.com/pages/roborock-affiliate-program
- https://ui.awin.com/merchant-profile/30761
- https://ui.awin.com/merchant-profile/14937
- https://ui.awin.com/merchant-profile/102205
- https://ui.awin.com/merchant-profile/30663
- https://app.impact.com/advertiser-campaign-info/The-Container-Store.brand
- https://app.impact.com/advertiser-advertiser-info/Yamazaki-Home.brand
- https://app.impact.com/advertiser-campaign-info/simplehuman.brand
- https://app.impact.com/advertiser-advertiser-info/Blueland.brand
- https://ui.awin.com/merchant-profile/90429
- https://www.adcell.de/partnerprogramme/cleangang
- https://www.chemicalguys.com/pages/affiliate-program
- https://app.impact.com/advertiser-advertiser-info/Advance-Auto-Parts.brand
- https://app.impact.com/advertiser-campaign-info/CARiD.brand
- https://app.impact.com/advertiser-campaign-info/Jegs.brand
- https://app.impact.com/advertiser-campaign-info/Nextbase.brand
- https://ui.awin.com/merchant-profile/22563
- https://ui.awin.com/merchant-profile/105597
- https://ui.awin.com/merchant-profile/10444
- https://ui.awin.com/merchant-profile/12639
- https://ui.awin.com/merchant-profile/13928
- https://www.kfzteile24.de/partnerprogramm
- https://ui.awin.com/merchant-profile/13940
- https://ui.awin.com/merchant-profile/3997
- https://www.eurocarparts.com/affiliate-program
- https://ui.awin.com/merchant-profile/13763
- https://ui.awin.com/merchant-profile/15112
- https://ui.awin.com/merchant-profile/99505
- https://www.adcell.de/partnerprogramme/speed-reifen
- https://www.adcell.de/partnerprogramme/autoteile-preiswert
- https://app.impact.com/advertiser-advertiser-info/Chewy.brand
- https://app.impact.com/advertiser-advertiser-info/Petco.brand
- https://app.impact.com/advertiser-advertiser-info/PetSmart.brand
- https://app.impact.com/advertiser-advertiser-info/The-Farmers-Dog.brand
- https://www.ollie.com/affiliate/
- https://app.impact.com/campaign-promo-signup/Ollie-Pets.brand
- https://app.impact.com/advertiser-advertiser-info/Litter-Robot.brand
- https://app.impact.com/advertiser-advertiser-info/Petlibro.brand
- https://ui.awin.com/merchant-profile/33889
- https://ui.awin.com/merchant-profile/83977
- https://wildone.com/pages/become-an-influencer-ambassador
- https://www.tuftandpaw.com/pages/affiliates
- https://ui.awin.com/merchant-profile/11330
- https://www.zooplus.de/info/about/partnerprogramm
- https://ui.awin.com/merchant-profile/2940
- https://ui.awin.com/merchant-profile/14757
- https://www.zooroyal.de/partner-programm/
- https://ui.awin.com/merchant-profile/14268
- https://ui.awin.com/merchant-profile/14419
- https://ui.awin.com/merchant-profile/6074
- https://join.butternutbox.com/affiliateinfluencers/
- https://www.adcell.de/partnerprogramme/butternut-box
- https://www.adcell.de/partnerprogramme/wildfang.pet
- https://www.adcell.de/partnerprogramme/luckypets
- https://app.impact.com/advertiser-campaign-info/Babylist.brand
- https://app.impact.com/advertiser-advertiser-info/Target.brand
- https://app.impact.com/advertiser-campaign-info/Cybex.brand
- https://ui.awin.com/merchant-profile/103281
- https://ui.awin.com/merchant-profile/103291
- https://app.impact.com/advertiser-campaign-info/Lovevery.brand
- https://lovevery.com/pages/affiliate-partnerships
- https://app.impact.com/advertiser-advertiser-info/Happiest-Baby.brand
- https://app.impact.com/advertiser-campaign-info/Hatch.brand
- https://app.impact.com/advertiser-advertiser-info/Elvie.brand
- https://app.impact.com/advertiser-advertiser-info/Momcozy.brand
- https://www.nanit.com/pages/press-and-partnerships
- https://ui.awin.com/merchant-profile/94823
- https://ui.awin.com/merchant-profile/6526
- https://www.mamasandpapas.com/pages/affiliate-programme
- https://ui.awin.com/merchant-profile/117735
- https://ui.awin.com/merchant-profile/14824
- https://ui.awin.com/merchant-profile/12387
- https://www.adcell.de/partnerprogramme/babyandfamily
- https://www.adcell.de/partnerprogramme/babybrands
- https://ui.awin.com/merchant-profile/129719
- https://ui.awin.com/merchant-profile/43419
- https://us.tonies.com/pages/affiliate-program
