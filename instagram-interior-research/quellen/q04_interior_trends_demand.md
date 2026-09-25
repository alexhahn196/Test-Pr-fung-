# Q04 – Nachfrage- und Trendindikatoren: Interior / Luxury Homes / Architektur (2025–2026)

**Stand:** 25.09.2026 · **Bearbeitung:** Research-Subagent (Desk Research) · **Projekt:** instagram-interior-research

**Status-Tags:**
- `[VERIFIED]`: Zahl oder Zitat selbst in der Quelle gesehen.
- `[ESTIMATED]`: nur als Such-Snippet oder indirekt gesehen, oder abgeleitet.
- `[THIRD-PARTY ESTIMATE]`: Schätzung eines Dritten (Marktforscher, SEO-Tool, Blog).
- `[UNKNOWN]`: nicht belegbar.

**Methodik und Grenzen dieser Notiz**
- Das WebSearch-Budget der Sitzung war nach wenigen Suchen erschöpft (Meldung „200 of 200 WebSearch calls“). Deshalb wurde der Großteil über **direkte Abrufe (WebFetch/curl)** bekannter Primär-URLs, Sitemaps und Archivseiten recherchiert. Das Budgetlimit wurde nicht umgangen, auch nicht über andere Suchmaschinen.
- **Google Trends** (API-Endpunkt `trends.google.com/trends/api/explore`) antwortete mit **HTTP 429** (Rate Limit). Das Limit wurde bewusst nicht umgangen. Echte Google-Trends-Kurven liegen daher **nicht** vor `[UNKNOWN]`. Ersatzweise dienen Drittanbieter-Tools (Exploding Topics, Accio) als Proxy `[THIRD-PARTY ESTIMATE]`.
- Nicht zugänglich waren (403, Paywall oder Login): Axios, Apartment Therapy, Grand View Research, Allied Market Research, Getty-Images-Newsroom, WWD (Umleitung auf „tollbit“), Reddit (403), Homes & Gardens (Inhalt abgeschnitten) und der Substack von Kendall Flavin (Paywall).

---

## 1. Fragestellung

Wie groß und wie dynamisch ist die **Nachfrage nach Interior-, Luxury-Home- und Architektur-Inhalten** 2025–2026, und welche **Stilrichtungen** steigen oder fallen? Die Notiz ist Grundlage für die Bewertung eines (ggf. KI-gestützten, gesichtslosen) Instagram-Theme-Accounts.

Abgedeckt sind:
1. Pinterest Predicts 2025/2026 und die saisonalen Pinterest-Reports
2. Houzz-, Etsy- und 1stDibs-Trendreports 2026
3. Suchinteresse an Stilbegriffen (Japandi, Organic Modern, Quiet Luxury, Dark Academia, Warm Minimalism, Cozy Rain, Future Home, AI Interior Design)
4. Volumenangaben auf Instagram
5. Marktgrößen für Möbel-E-Commerce und Home Décor
6. Nachfrage nach KI-Interior-Apps
7. **Gegenevidenz**: Sättigung, „AI slop“, Backlash, Trend-Fatigue

---

## 2. Kernbefunde

### 2.1 Pinterest Predicts 2026 (erschienen 09.12.2025)

- **Nur 3 von 21 Trends** sind explizit Wohn- bzw. Interior-Trends, und ihre Anstiege sind **moderat (+35 % bis +220 %)**. Alle drei gehen weg von Minimalismus, hin zu Farbe, Glamour und Kultur-Mix. Quellen: [Pinterest Newsroom, 09.12.2025](https://newsroom.pinterest.com/news/pinterest-predicts-nonconformity-self-preservation-and-escapism-drive-21-trends-for-2026/); Stat-Items im Seiten-JSON von [business.pinterest.com – Neo Deco](https://business.pinterest.com/pinterest-predicts/2026/neo-deco/) `[VERIFIED]`
  - **FunHaus** (Zirkus-Deko): *"circus-inspired home decor will be on the rise thanks to Boomers and Millennials"*. Suchanstiege: striped ceiling +40 %, circus nursery +50 %, circus interior +130 %, circus art +35 %, vintage circus aesthetic +70 %.
  - **Neo Deco**: *"After years of heavy minimalism, Gen X and Millennials are bringing this retro aesthetic back with crisp chevrons, fan arches and other geometric hits, all edged in chrome or brass."* Suchanstiege: pendant lamp +40 %, red marble bathroom +80 %, antique bar cart +100 %, brass aesthetic +35 %, leather banquette +35 %.
  - **Afrohemian Decor**: afrobohemian home decor +220 %, adire fabric +130 %, motif berbere +210 % (nur im Newsroom), bamboo beaded curtains +60 %, ethiopian art +50 %, rattan accent chair +50 %.
- **Methodik (Fußnote im Original):** *"Pinterest internal data, English language search data, Global, analysis period September 2023 to August 2025. Unless otherwise noted, changes are calculated using normalized searches during September 2024 - August 2025"*. Laut NBC ist die Vergleichsbasis Sept. 2023 bis Aug. 2024 ([NBC Select, 11.12.2025](https://www.nbcnews.com/select/shopping/pinterest-predicts-2026-trend-report-rcna248706)). `[VERIFIED]`
- **Eigenangaben von Pinterest:** *"has proven over the past six years to be 88% accurate"*, *"67% of the 2026 trends are driven by Gen Z"*, Basis *"600 million monthly"* Nutzer. `[VERIFIED als Eigenangabe; die Trefferquote ist nicht unabhängig geprüft]`
- **Gegenevidenz direkt im Report:** *"Trends are growing 4.4x faster than they were seven years ago. And in 2026, people will look to combat trend fatigue"*. Außerdem: *"Curating, not copying."* Das spricht für kurze Trend-Halbwertszeiten und für Ermüdung bei Einheitsästhetik. `[VERIFIED]`

### 2.2 Pinterest Predicts 2025 (erschienen 05.12.2024)

- **Wohn-Trends mit Suchanstiegen** laut Stat-Items im Seiten-JSON von [business.pinterest.com (Castlecore u. a.)](https://business.pinterest.com/pinterest-predicts/2025/castlecore/) `[VERIFIED]`:
  - **Mix & Maximalist:** eclectic apartment +630 %, vintage maximalism +260 %, eclectic maximalism +215 %, fabric wall decor +135 %, eclectic boho bedroom +65 %.
  - **Primary Play:** hand painted furniture +135 %, contrast trim +85 %, door murals +70 %, hand painted wall pattern +60 %, cupboard painting +45 %.
  - **Castlecore:** medieval core +110 %, castle house plans +45 %.
  - **Cherry Coded:** dark cherry red +235 %, cherry bedroom +100 %.
  - **Terra Futura:** chaos gardening +300 %, solarpunk house +80 %, self sufficient garden +55 %.
  - **Surreal Soirees:** modern surrealism +70 %, dinner party tablescapes +55 %.
  - **Dolled Up:** cutecore room ideas +40 %.
- **Methodik:** *"Pinterest internal data, global English language searches. Analysis period Sep 2022–Aug 2024."* Angegebene Trefferquote damals: *"over the past five years to be 80% accurate"*, Basis *"Over half a billion people"* ([Newsroom, 05.12.2024](https://newsroom.pinterest.com/news/pinterest-predicts-20-bold-trends-for-2025/)). `[VERIFIED]`
- **Richtungsaussage 2025:** *"people will be ditching minimalist design in favor of something more dramatic—like eclectic prints, textured wallpaper and eye-catching patterns."* (Seiten-Metadaten auf business.pinterest.com) `[VERIFIED]`
- **Nachträgliche Bewertung:** Ein Blog bestätigt allgemein, dass *"Mix and Maximalist, Goddess Complex, and Rococo Revival"* eingetroffen seien. Es nennt aber keine Wohn-spezifische Auswertung und keine Kritik an der Methode ([The Creative Radar, 02.02.2026](https://thecreativeradar.wordpress.com/2026/02/02/pinterest-predicts-2026/)). `[VERIFIED – schwache Quelle]`

### 2.3 Saisonale Pinterest-Reports 2025/2026 (Newsroom)

- **Fall 2025** (20.08.2025) ([Newsroom](https://newsroom.pinterest.com/news/the-2025-pinterest-fall-trend-report/)) `[VERIFIED]`. Einen Datenzeitraum nennt der Report **nicht** `[UNKNOWN]`.
  - „Cubicle Chic“: "Luxe office" +2,766 %, "Cubicle makeover ideas" +2,767 %, "Work office makeover" +2,652 %.
  - „Statement Tiles“: "Vintage tiles" +1,107 %, "Terracotta tiles texture" +833 %.
  - „Art Deco Decor“: "Art deco vintage" +805 %, "Art deco interior 1920s vintage" +745 %, "New art deco" +497 %.
- **Spring 2026** (17.03.2026) ([Newsroom](https://newsroom.pinterest.com/news/spring-trend-report-2026/)) `[VERIFIED]`. Leitmotiv: *"home isn't about perfection. It's about showing off who you really are, right now"*.
  - Küchen und Räume: "Dark cottagecore kitchen" +915 %, "Village kitchen ideas" +825 %, "White oak and black kitchen" +625 %, "Grandma core kitchen" +545 %, "Aubergine kitchen" +495 %, "Comfy reading chair small spaces" +455 %, "My room my rules" +415 %, "Sage green and cream kitchen" +410 %, "Vibey apartment living room aesthetic" +380 %, "Moody blue kitchen" +325 %, "Reading nook ideas" +245 %.
  - Fußnoten im Report: *"Pinterest Internal Data; Global; January 2025 vs January 2026"* und *"Pinterest Internal Data, Global, Q4 2025"*. Welche Fußnote zu welcher Zahl gehört, bleibt unklar.
- **Summer 2026** (26.05.2026): **keine** Wohn- oder Interior-Trends. Der Report behandelt nur Mode, Beauty, Food und Sport ([Newsroom](https://newsroom.pinterest.com/news/summer-trend-report-2026/)). `[VERIFIED]`

### 2.4 Houzz 2026 (USA)

- **Emerging Summer Trends 2026** (20.05.2026). Datenbasis: *"year-over-year growth in U.S.-based searches on Houzz from January-March 2026 versus January-March 2025"* ([Houzz Blog](https://blog.houzz.com/2026-u-s-houzz-emerging-summer-trends-report/); [Houzz Magazine, 23.05.2026](https://www.houzz.com/magazine/8-design-trends-emerging-in-2026-stsetivw-vs~185246097)) `[VERIFIED]`
  - Kurven: "scalloped tile" +300 % (*"more than tripled"*), "arched range hood" +177 %, "rounded kitchen island" +123 %.
  - Texturen: "sandstone" +257 %, "linen wallpaper" +104 %, "Venetian plaster" +94 %, "limewash interior paint" +53 %.
  - Warme Erdfarben: "rust colors" +178 %, "chocolate brown" +153 %, "mushroom color" +69 %.
  - Nostalgische Räume: "mahjong room" +1,900 %, "bibliothèque" +191 %, "speakeasies" +75 %.
  - Wellness: "wellness room" +164 %, "biophilic design" +112 %.
  - Europäische Gärten: "French courtyards" +500 %, "Italian courtyards" +350 %, "cottage patios" +204 %.
  - Der Report nennt **nur steigende Begriffe**, keine fallenden. Social Media oder Instagram kommen nicht vor.
- **Fall 2026** (Bericht in KBB, 14.09.2026) ([KBB](https://kbbonline.com/trends-inspirations/houzz-reports-fall-2026-design-trends/170955)) `[VERIFIED]`
  - Fünf Trends: „Warmth Is the New Baseline“, „Collected, Layered Interiors“, „Character and Personality Matter More Than Perfection“, „Natural Materials Get More Expressive“, „Designing Homes to Evolve“.
  - Zusatzdaten aus der Houzz & Home Study 2026: 61 % planen, nach der Renovierung 11+ Jahre im Haus zu bleiben; 44 % sprechen von einem „forever home“.
  - Die Angabe *"nearly 50 home design professionals"* befragt stammt nur aus einem Such-Snippet (CultureMap). `[ESTIMATED]`

### 2.5 1stDibs Interior Designer Trends Survey 2026 (Pressemitteilung 17.11.2025)

- Quelle: [1stDibs Investor Relations](https://investors.1stdibs.com/news/news-details/2025/2026-Interior-Design-Trends-1stDibs-Survey-Identifies-Maximalism-Chocolate-Brown-and-Vintage-Antiques-as-Top-Designer-Choices/default.aspx). Befragt wurden **468 Designer** (Juli–Aug. 2025, Trade-1st-Mitglieder). `[VERIFIED]`
- Stile: **Maximalism 39 %**, **Eclecticism 38 %** am häufigsten nachgefragt. Chocolate Brown 33 % (2022: 17 %). `[VERIFIED]`
- **KI bei Designern:** Nutzung 29 % (2025) gegenüber 9 % (2023); weitere 20 % planen die Nutzung; **24 % sind „strongly against“**. `[VERIFIED]`
- Zölle: 92 % berichten von Auswirkungen durch die Zölle 2025. `[VERIFIED]`
- Aus Such-Snippets der Pressemitteilung (selbst nicht nachgeprüft) `[ESTIMATED]`:
  - Butter Yellow: 14 % → 30 %.
  - Kurvige Möbel: 43 %.
  - Rattan: 27 %.

### 2.6 Etsy Trend-Insights Frühjahr/Sommer 2026

- Gepostet von Etsy-Staff („Resident Trend Expert“). Datenbasis: *"as of February 10, 2026, and based on searches and sales in the last three months compared to the same time last year."* ([Etsy Community](https://community.etsy.com/forum/etsy-success-300/topic/etsy-insights-explore-the-trends-shaping-spring-and-summer-2026-165859/)) `[VERIFIED]`
- **"wall art decor" +110 %**, **"gallery prints" +80 %**. Zitat: *"Shoppers—especially Gen Z—are gravitating toward visible craftsmanship and pieces that feel unmistakably handmade."* `[VERIFIED]`
- Die Angaben „wall decor mirrors +50 %“, „abstract art +38 %“ und „Patina Blue“ als Farbe des Jahres fanden sich nur in Snippets von Seller-Blogs. `[ESTIMATED]`

### 2.7 Suchinteresse an Stilbegriffen (Proxy für Google Trends)

- **Google Trends direkt:** nicht abrufbar (HTTP 429). `[UNKNOWN]`
- **Exploding Topics** (abgerufen am 25.09.2026, Standard-Zeitraum „2 years“) `[THIRD-PARTY ESTIMATE]`. Die Seite sagt nicht, ob „Volume“ monatlich, für die USA oder global gilt.
  - **Japandi:** *"current search volume of 135K with a growth of +100%"*, Status **Exploding**. ([Link](https://explodingtopics.com/topic/japandi))
  - **Quiet luxury:** 60.5K, +118 %, Status **Peaked**.
  - **Maximalism:** 49.5K, +67 %, Status **Exploding**.
  - **Biophilic design:** 27.1K, +3 %, Status **Peaked**.
  - **AI interior design:** 22.2K, +42 %, Status **Peaked**.
  - **Interior AI:** 18.1K, +156 %, Status **Peaked**.
  - **RoomGPT:** 49.5K, +36 %, Status **Exploding**.
  - **Virtual staging:** 8.1K, **−24 %**, Status **Peaked**.
  - Für „organic modern“, „warm minimalism“, „dark academia“ und „wabi sabi“ gibt es dort keine Seiten (404).
- **Accio** (B2B-Seite, 16.09.2026) nennt normierte Google-Trends-Werte für Japandi-Begriffe ([Accio](https://www.accio.com/business/japandi_trend)) `[THIRD-PARTY ESTIMATE]`:
  - "Japandi furniture": Höchstwert 93 Ende Aug. 2025, 74 im Nov. 2025.
  - "Japandi lighting": 40 bzw. 37.
  - "japandi home decor": 8 (Ende Dez. 2025).
- **Quiet Luxury:** Mehrere Deko-Blogs erklären „Quiet Luxury“ 2026 weiterhin zum Leittrend. Homes & Gardens dagegen positioniert „Found Luxury“ als Nachfolger (laut Such-Snippet; der Artikel war abgeschnitten). Das deckt sich mit dem Status „Peaked“ bei Exploding Topics und mit der Maximalismus-Welle bei Pinterest und 1stDibs. `[ESTIMATED]`

### 2.8 Volumenangaben auf Instagram

- **Hashtag-Zahlen aus seriösen Quellen** (#interiordesign, #luxuryhomes, #architecture, #homedecor): **nicht gefunden bzw. nicht verifizierbar.** Instagrams Hashtag-Seiten verlangen einen Login; es wurde nicht eingeloggt. `[UNKNOWN]`
- **Ersatz: öffentliche Instagram-Themenseiten** (`instagram.com/popular/<slug>/`). Sie zeigen ein Label *"X reels on Instagram"*. Sieben davon habe ich selbst abgerufen (25.09.2026) `[VERIFIED]`:
  - [Home Decor](https://www.instagram.com/popular/home-decor/): *"901M reels on Instagram"*
  - [Architecture](https://www.instagram.com/popular/architecture/): *"1B reels on Instagram"*
  - [Luxury Homes](https://www.instagram.com/popular/luxury-homes/): *"128M reels on Instagram"*
  - [Warm Minimalism](https://www.instagram.com/popular/warm-minimalism/): *"1.1M reels on Instagram"*
  - [Japandi](https://www.instagram.com/popular/japandi/): *"841K reels on Instagram"*
  - [Ai Interior Design](https://www.instagram.com/popular/ai-interior-design/): *"152K reels on Instagram"*
  - [Dark Academia Interior](https://www.instagram.com/popular/dark-academia-interior/): *"1.4K reels on Instagram"*
  - Die Seite [Interior Design](https://www.instagram.com/popular/interior-design/) zeigt keine Zahl.
- **Weitere Labels aus dem Projekt-Sweep** (`data/processed/topics_status.csv`, abgerufen 25.09.2026) `[VERIFIED – Projektdaten, stichprobenartig gegengeprüft]`:
  - Wohnen und Stile: interior-styling 116M · kitchen-design 102M · dream-home 151M · mid-century-modern 40M · quiet-luxury 7M · luxury-interior 6.4M · cozy-room 2.6M · organic-modern 1M · minimalist-interior 815K · biophilic-design 396K · wabi-sabi-interior 104K · scandinavian-interior 61K
  - Immobilien: real-estate 686M · luxury-real-estate 85M · mansion-tour 133K
  - Architektur und Zukunft: architecture-photography 135M · modern-architecture 24M · future-house 6.9M · future-home 2.2M · futuristic-architecture 269K · futuristic-interior 5.2K
  - Regen und Stimmung: rainy-day 118M · rain-sounds 427K · cozy-rain 23K
  - KI-Themen: ai-art 114M · midjourney-architecture 1.7M · ai-architecture 1.4M · virtual-staging 884K · ai-render 87K · ai-interior 66K · ai-home-design 37K
- **Lesart:** Allgemeine Oberbegriffe (Home Decor, Architecture, Real Estate) liegen bei Hunderten Millionen bis 1 Mrd. Reels. Konkrete Stilbegriffe liegen meist im Bereich **Tausende bis wenige Millionen**. Nischen-Ästhetiken wie „dark academia interior“ (1.4K) und „cozy rain“ (23K) sind auf Instagram als Themen kaum ausgeprägt. KI-spezifische Interior-Themen (152K) sind **klein im Vergleich zu Home Decor (901M)**. Das kann wenig Wettbewerb bedeuten, aber ebenso wenig Nachfrage. `[ESTIMATED – Interpretation]`
- **Einschränkung:** Instagram definiert nicht, was die Labels zählen (Hashtags, Keywords, Zeitraum). Es sind **keine Nachfragemaße** (Views, Suchen), sondern Angebotsmaße (Anzahl Reels).

### 2.9 Marktgrößen (Möbel-E-Commerce, Home Décor)

- **Statista Market Insights, eCommerce Furniture weltweit** (inkl. Home Décor laut Definition: *"selling furniture and home decor products through digital channels"*) ([Statista](https://www.statista.com/outlook/emo/furniture/worldwide)) `[THIRD-PARTY ESTIMATE]`:
  - *"projected to reach US$280.84bn in 2026"*, CAGR 2026–2030 von 4.73 %, *"US$337.91bn by 2030"*.
  - USA: US$130.84bn (2026).
  - Käufer: *"1.3bn users by 2030"*; Penetration 17.2 % (2026) → 18.1 % (2030); ARPB US$260.04.
- **Statista Furniture gesamt** (B2C, online und offline): *"US$737.91bn in 2026"*, CAGR 3.10 % (2026–2031). Living Room US$215.85bn; USA US$249.51bn ([Statista](https://www.statista.com/outlook/cmo/furniture/worldwide)). `[THIRD-PARTY ESTIMATE]`
- **Statista Home Décor** (B2C): *"US$126.84bn in 2026"*, CAGR 3.34 % (2026–2031); USA US$32.91bn ([Statista](https://www.statista.com/outlook/cmo/furniture/home-decor/worldwide)). Die E-Commerce-Werte für Home Décor liegen hinter der Paywall. `[THIRD-PARTY ESTIMATE]`
- **Mordor Intelligence, Home Decor** (Scope inkl. Möbel, Textilien, Bodenbeläge, Leuchten, Pflanzen) ([Mordor, 06.08.2026](https://www.mordorintelligence.com/industry-reports/home-decor-market)) `[THIRD-PARTY ESTIMATE]`:
  - *"expected to grow from USD 681.05 billion in 2025 to USD 716.53 billion in 2026 and is forecast to reach USD 924.34 billion by 2031 at 5.21% CAGR"*.
  - Treiber *"Growing influence of social media and digital platforms"* mit **+0.6 %** CAGR-Effekt.
  - APAC-CAGR 8.11 %.
- **Technavio, Online Home Decor:** *"valued to increase by USD 73.93 billion, at a CAGR of 9.26% from 2023 to 2028"* (Feb. 2024; [Technavio](https://www.technavio.com/report/online-home-decor-market-industry-analysis)). `[THIRD-PARTY ESTIMATE]`

### 2.10 Nachfrage nach KI-Interior-Apps

- **Google Play**: Suche „ai interior design“ (US, 25.09.2026), dazu 30 Detailseiten abgerufen ([Suche](https://play.google.com/store/search?q=ai%20interior%20design&c=apps&hl=en&gl=US)) `[VERIFIED]`
  - [Planner 5D: AI Home Design](https://play.google.com/store/apps/details?id=com.planner5d.planner5d): **50M+** Downloads, 573.939 Bewertungen, 4,4★. Ältere 3D-App, inzwischen „AI“-gebrandet.
  - [Home AI – AI Interior Design (HubX)](https://play.google.com/store/apps/details?id=interior.home.design.ai): **10M+**, 991.745 Bewertungen, 4,3★.
  - [AI Home Design: Interior DecAI](https://play.google.com/store/apps/details?id=ai.interior.design.home.renovation.app): **10M+**, 291.983 Bewertungen.
  - [Home Planner AI (Room Planner Ltd)](https://play.google.com/store/apps/details?id=com.icandesignapp.all): **10M+**, 240.185 Bewertungen.
  - [Homestyler – Home Design Game](https://play.google.com/store/apps/details?id=com.autodesk.homestyler): **10M+**, 3,3★.
  - [AI Remodel – Interior Design](https://play.google.com/store/apps/details?id=pro.airemodel.android): **5M+**, 183.726 Bewertungen.
  - 1M+: Remodel AI (ReImage), SnapHome, Interio.
  - Die Nischen-Apps „Interior AI – AI Home Design“ (BIVEX; **nicht** interiorai.com) und „RoomGPT AI“ (AZUR APPS; **nicht** roomgpt.io) liegen bei 500K+.
  - **Long Tail:** Von 30 Treffern haben **10 unter 1M** und **10 höchstens 10K+** Downloads (50+, 500+, 5K+, 10K+). Das spricht für einen **stark besetzten, fragmentierten Markt**.
  - Einschränkung: Downloadzahlen sind kumulierte Lebenszeit-Bänder, keine aktiven Nutzer.
- **RoomGPT.io:** Die Website sagt *"See what our over 4 million users are saying about the product."* Der zugehörige Link führt auf einen Tweet von ca. Aug. 2023, die Angabe ist also wahrscheinlich veraltet ([roomgpt.io](https://www.roomgpt.io/)). `[VERIFIED als Eigenangabe]` Das Open-Source-Repo hat 10.7k Stars und 1.5k Forks ([GitHub](https://github.com/Nutlope/roomGPT)). `[VERIFIED]`
- **Interior AI (Pieter Levels):**
  - Umsatz laut Gründer: *"InteriorAI.com $43K/m"* (Blogpost vom 22.09.2024, [levels.io](https://levels.io/new-420k-mo-revenue-record-lex-fridman)). `[VERIFIED als Eigenangabe, nicht auditiert]`
  - Preise heute: Pro $49/Monat, Premium $99, Ultra $199 ([interiorai.com](https://interiorai.com/)). `[VERIFIED]`
  - Wayfair nutzte das Tool vor dem eigenen Launch: *"They had 8 different accounts on Interior AI that ran for months"* ([levels.io, 27.03.2024](https://levels.io/wayfair-used-interior-ai-to-build-their-own)). `[VERIFIED als Eigenangabe]`
  - Aktuelle Umsatzzahlen für 2025/2026: nicht gefunden. `[UNKNOWN]`
- **Homestyler:** *"Trusted by 20 M+ designers worldwide"* ([homestyler.com](https://www.homestyler.com/)). `[VERIFIED als Eigenangabe]`
- **Profis:** 29 % der Designer nutzen KI (1stDibs, siehe 2.5). `[VERIFIED]`

### 2.11 Gegenevidenz: Sättigung, „AI slop“, Backlash, Fatigue

- **Pinterest stuft Home Decor und Architektur ausdrücklich als KI-anfällig ein:**
  - 30.04.2025: Label „AI modified“ und eine „see fewer“-Option für Kategorien *"like beauty, art, and home decor"* ([Newsroom](https://newsroom.pinterest.com/news/introducing-gen-ai-labels/)). `[VERIFIED]`
  - 16.10.2025: Regler, um weniger KI-Inhalte zu sehen, u. a. in **"architecture"** und **"home decor"**. Zitat: *"categories that are highly prone to AI modification or generation like beauty, art, fashion and home decor"* ([Newsroom, 16.10.2025, aktualisiert 12.12.2025](https://newsroom.pinterest.com/news/pinterest-rolls-out-new-tools-to-give-users-more-control-over-gen-ai-content/)). `[VERIFIED]`
  - Pinterest zitiert dort, dass generative KI *"now making up an incredible 57%"* aller Online-Inhalte ausmache. Die Zahl stammt aus einer von Pinterest zitierten Studie; ich habe sie nicht selbst geprüft. `[VERIFIED als Zitat; Zahl selbst THIRD-PARTY ESTIMATE]`
- **Backlash bei Nutzern:**
  - TechCrunch (30.04.2025): *"AI-generated Pins and other low-quality AI content — often referred to as 'AI slop' — have created a backlash among Pinterest's loyal customer base."* ([TechCrunch](https://techcrunch.com/2025/04/30/pinterest-launches-new-tools-to-fight-ai-slop/)) `[VERIFIED]`
  - TechCrunch (16.10.2025): *"has come under fire from users who have complained about the massive uptick in GenAI content"*, und *"The problem, if left unresolved, could destroy Pinterest's reputation and, ultimately, its bottom line."* ([TechCrunch](https://techcrunch.com/2025/10/16/pinterest-adds-controls-to-let-you-limit-the-amount-of-ai-slop-in-your-feed/)) `[VERIFIED]`
- **Verbraucherhaltung zu KI** (Pew, Befragung 9.–15.06.2025, n = 5.023 US-Erwachsene) ([Pew Research](https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/)) `[VERIFIED]`:
  - *"50% say they're more concerned than excited"* (2021: 37 %).
  - 76 % halten es für *"extremely or very important to be able to tell"*, ob Inhalte von KI stammen.
  - 53 % trauen sich das nicht zu.
- **Allgemeine Flut von „AI slop“:** Kapwing fand in den ersten 500 Shorts eines neuen YouTube-Kontos 21 % KI-generierte Videos und 33 % „brainrot“ (Daten Okt. 2025). Der Report nennt keine Interior-Beispiele ([Kapwing](https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/)). `[VERIFIED; Methode: Stichprobe eines einzelnen Kontos]`
- **Die Stilrichtung arbeitet gegen „perfekte“ KI-Render:**
  - Houzz Fall 2026: *"Character and Personality Matter More Than Perfection"*.
  - Pinterest Spring 2026: *"home isn't about perfection"*.
  - Etsy: *"unmistakably handmade"*.
  - Pinterest 2026: *"Curating, not copying"*, *"combat trend fatigue"*.
  - 1stDibs: 24 % der Designer sind strikt gegen KI.
  - `[VERIFIED für die Zitate; der Schluss auf KI-Content ist Interpretation]`
- **Such-Proxies:** „AI interior design“ und „Interior AI“ stehen bei Exploding Topics auf **Peaked**, „virtual staging“ bei **−24 %** (siehe 2.7). `[THIRD-PARTY ESTIMATE]`
- **Instagram-spezifisch:** Für **sinkendes Engagement von Interior-Theme-Pages** oder Instagram-Artikel über „AI slop“ speziell bei Interior-Videos habe ich **keine belastbare Quelle gefunden**. Das liegt auch am erschöpften Suchbudget. `[UNKNOWN]` Aussagen von Meta und Mosseri zu KI-Content und Originalität stehen in `q01_instagram_platform_rules.md`.

---

## 3. Zahlen-Tabelle

| Kennzahl | Wert | Zeitraum/Basis | Quelle | Status |
|---|---|---|---|---|
| Pinterest Predicts 2026: Wohn-Trends | 3 von 21 (FunHaus, Neo Deco, Afrohemian) | Suchdaten Sep 2024–Aug 2025 vs. Vorjahr | Pinterest Newsroom 09.12.2025 | VERIFIED |
| afrobohemian home decor | +220 % | s. o. | Pinterest 2026 | VERIFIED |
| circus interior | +130 % | s. o. | Pinterest 2026 | VERIFIED |
| antique bar cart / red marble bathroom | +100 % / +80 % | s. o. | Pinterest 2026 | VERIFIED |
| Pinterest-Trefferquote (Eigenangabe) | 88 % (6 J.) / 80 % (5 J., Vorjahr) | – | Pinterest Newsroom 2025/2024 | VERIFIED (Eigenangabe) |
| „Trends are growing … faster“ | 4.4x vs. vor 7 Jahren | – | Pinterest 2026 | VERIFIED (Eigenangabe) |
| eclectic apartment / vintage maximalism | +630 % / +260 % | Sep 2022–Aug 2024 | Pinterest Predicts 2025 | VERIFIED |
| hand painted furniture | +135 % | s. o. | Pinterest 2025 | VERIFIED |
| medieval core / castle house plans | +110 % / +45 % | s. o. | Pinterest 2025 | VERIFIED |
| Dark cottagecore kitchen | +915 % | Jan 2025 vs. Jan 2026 bzw. Q4 2025 (Fußnote unklar) | Pinterest Spring 2026 | VERIFIED |
| Art deco vintage | +805 % | nicht angegeben | Pinterest Fall 2025 | VERIFIED |
| Houzz: mahjong room / French courtyards | +1,900 % / +500 % | Jan–Mär 2026 vs. 2025, US | Houzz 20.05.2026 | VERIFIED |
| Houzz: chocolate brown / biophilic design | +153 % / +112 % | s. o. | Houzz | VERIFIED |
| 1stDibs: Maximalism / Eclecticism | 39 % / 38 % | n = 468, Jul–Aug 2025 | 1stDibs 17.11.2025 | VERIFIED |
| 1stDibs: KI-Nutzung Designer | 29 % (2025) vs. 9 % (2023); 24 % „strongly against“ | s. o. | 1stDibs | VERIFIED |
| Etsy: wall art decor / gallery prints | +110 % / +80 % | 3 Monate bis 10.02.2026 vs. Vorjahr | Etsy Community | VERIFIED |
| Exploding Topics: Japandi | 135K Volumen, +100 %, „Exploding“ | 2 Jahre | explodingtopics.com | THIRD-PARTY ESTIMATE |
| Exploding Topics: Quiet luxury | 60.5K, +118 %, „Peaked“ | 2 Jahre | explodingtopics.com | THIRD-PARTY ESTIMATE |
| Exploding Topics: AI interior design | 22.2K, +42 %, „Peaked“ | 2 Jahre | explodingtopics.com | THIRD-PARTY ESTIMATE |
| Exploding Topics: Virtual staging | 8.1K, −24 %, „Peaked“ | 2 Jahre | explodingtopics.com | THIRD-PARTY ESTIMATE |
| Google Trends direkt | nicht abrufbar (HTTP 429) | – | trends.google.com | UNKNOWN |
| Instagram „Home Decor“ | 901M Reels | Stand 25.09.2026 | instagram.com/popular | VERIFIED |
| Instagram „Architecture“ | 1B Reels | s. o. | instagram.com/popular | VERIFIED |
| Instagram „Luxury Homes“ | 128M Reels | s. o. | instagram.com/popular | VERIFIED |
| Instagram „Warm Minimalism“ / „Japandi“ | 1.1M / 841K Reels | s. o. | instagram.com/popular | VERIFIED |
| Instagram „Quiet Luxury“ / „Organic Modern“ | 7M / 1M Reels | s. o. | Projekt-Sweep | VERIFIED (Projektdaten) |
| Instagram „Ai Interior Design“ | 152K Reels | s. o. | instagram.com/popular | VERIFIED |
| Instagram „Dark Academia Interior“ / „Cozy Rain“ | 1.4K / 23K Reels | s. o. | instagram.com/popular; Sweep | VERIFIED |
| Instagram „Future House“ / „Future Home“ | 6.9M / 2.2M Reels | s. o. | Projekt-Sweep | VERIFIED (Projektdaten) |
| Hashtag-Zahlen #interiordesign etc. (seriöse Quelle) | – | – | – | UNKNOWN |
| Möbel-E-Commerce weltweit | US$280.84bn (2026) → US$337.91bn (2030), CAGR 4.73 % | Prognose | Statista | THIRD-PARTY ESTIMATE |
| Möbelmarkt gesamt (B2C) | US$737.91bn (2026), CAGR 3.10 % | 2026–2031 | Statista | THIRD-PARTY ESTIMATE |
| Home Décor (Statista, B2C) | US$126.84bn (2026), CAGR 3.34 % | 2026–2031 | Statista | THIRD-PARTY ESTIMATE |
| Home Decor (Mordor, inkl. Möbel) | USD 716.53bn (2026) → 924.34bn (2031), CAGR 5.21 % | 2026–2031 | Mordor 06.08.2026 | THIRD-PARTY ESTIMATE |
| Online Home Decor (Technavio) | +USD 73.93bn, CAGR 9.26 % | 2023–2028 | Technavio 02/2024 | THIRD-PARTY ESTIMATE |
| Planner 5D (Google Play) | 50M+ Downloads | kumuliert | Google Play 25.09.2026 | VERIFIED |
| Home AI (HubX) | 10M+ Downloads, 991.745 Bewertungen | kumuliert | Google Play | VERIFIED |
| KI-Interior-Apps im Long Tail | 10 von 30 Treffern ≤ 10K+ Downloads | Suche „ai interior design“ US | Google Play | VERIFIED |
| RoomGPT.io Nutzer (Eigenangabe) | „over 4 million users“ | wohl Stand ~2023 | roomgpt.io | VERIFIED (Eigenangabe) |
| Interior AI Umsatz (Eigenangabe) | $43K/Monat | Sep 2024 | levels.io | VERIFIED (Eigenangabe) |
| Homestyler (Eigenangabe) | „20 M+ designers“ | undatiert | homestyler.com | VERIFIED (Eigenangabe) |
| Pinterest GenAI-Filter | u. a. home decor, architecture | seit 16.10.2025 | Pinterest Newsroom | VERIFIED |
| Pew: mehr besorgt als begeistert | 50 % (2021: 37 %) | Jun 2025, n = 5.023 | Pew Research | VERIFIED |
| Pew: wichtig, KI erkennen zu können | 76 % | s. o. | Pew Research | VERIFIED |
| Kapwing: KI-Anteil im Shorts-Feed eines neuen Kontos | 21 % KI, 33 % brainrot | Okt 2025, 500 Shorts | Kapwing | VERIFIED |

---

## 4. Widersprüche und Unsicherheiten

1. **Minimalismus gegen Maximalismus.**
   - Pinterest (2025: *"ditching minimalist design"*; 2026: *"After years of heavy minimalism"*) und 1stDibs (Maximalism 39 %, Eclecticism 38 %) sehen einen klaren Trend weg von Beige und Minimalismus.
   - Japandi hält sich trotzdem: Exploding Topics „Exploding“ mit +100 %; Instagram 841K Reels; Warm Minimalism 1.1M Reels.
   - Quiet Luxury gilt bei Exploding Topics als „Peaked“, auf Instagram gibt es aber 7M Reels. Das Angebot an Content ist hier deutlich größer als das aktuelle Wachstum.
   - Für einen Content-Account heißt das: Minimal-Luxus-Ästhetik ist **verbreitet** (viel Angebot), aber nicht mehr der **Wachstumstreiber**.
2. **Große Prozentwerte, kleine Basis.**
   - Die saisonalen Pinterest-Reports nennen Anstiege von +245 % bis +2,767 % für sehr spezifische Long-Tail-Suchen. Houzz nennt +1,900 % für „mahjong room“.
   - Keine Quelle nennt absolute Suchvolumina. Die Prozentwerte sagen daher **nichts über die Größe der Nachfrage** aus.
   - Pinterest und Houzz veröffentlichen **nur steigende** Begriffe (Selektionsbias).
3. **Die Trefferquote von Pinterest ist nur Eigenangabe.** Die 88 % bzw. 80 % sind nicht unabhängig geprüft. Eine kritische Analyse (Kendall Flavin) liegt hinter einer Paywall.
4. **Marktgrößen je nach Definition um den Faktor 5 bis 6 auseinander.**
   - Home Décor liegt bei Statista bei US$126.84bn, bei Mordor bei USD 716.53bn (2026). Mordor rechnet Möbel, Textilien und Bodenbeläge mit ein.
   - Statistas E-Commerce-Segment „Furniture“ schließt Home Décor ein. Die USA liegen dort bei US$130.84bn online gegenüber US$249.51bn im Gesamtmarkt. Das deutet auf einen sehr hohen Online-Anteil oder auf abweichende Abgrenzungen hin; das ist nicht auflösbar, weil der Anteil hinter der Paywall liegt.
   - Alle Marktzahlen sind `THIRD-PARTY ESTIMATE` und nicht direkt auf Content-Nachfrage übertragbar.
5. **Instagram-Labels sind keine Nachfragemetrik.** „X reels on Instagram“ zählt das Angebot an Reels, keine Views und keine Suchen. Die Zählmethode ist undokumentiert. Die Seite „Interior Design“ zeigt gar keine Zahl.
6. **Nachfrage nach KI-Apps: groß, aber gesättigt.**
   - Mehrere Apps haben über 10M Downloads, gleichzeitig gibt es viele Klone mit sehr wenigen Downloads.
   - Die Such-Proxies „AI interior design“ und „Interior AI“ stehen auf „Peaked“, RoomGPT auf „Exploding“ (+36 %). Das Signal ist gemischt.
   - Die Nutzerzahlen von RoomGPT (4M) und Homestyler (20M+) sind Eigenangaben ohne Datum.
7. **Backlash gegen KI im Interior-Bereich ist belegt, aber vor allem für Pinterest.** Pinterest behandelt Home Decor und Architektur ausdrücklich als KI-anfällige Kategorien mit Filter. Für Instagram fehlt vergleichbare Evidenz `[UNKNOWN]`. Ob dort sinkendes Engagement für KI-Interior-Theme-Pages messbar ist, konnte ich nicht klären.
8. **Hashtag-Volumina** (#interiordesign, #homedecor, #luxuryhomes, #architecture) aus seriösen Quellen fehlen. Zahlen aus Hashtag-Generator-Seiten wurden bewusst **nicht** übernommen.
9. **Google Trends fehlt.** Aussagen zu Japandi, Organic Modern, Dark Academia, Warm Minimalism, Cozy Rain und Future Home beruhen nicht auf Google-Trends-Kurven, sondern auf Drittanbietern und Instagram-Labels.

---

## 5. Kurz-Einordnung für das Projekt (aus der Evidenz abgeleitet, keine neue Faktenbehauptung)

- **Große Oberthemen** (Home Decor 901M, Architecture 1B, Luxury Homes 128M Reels) zeigen ein enormes Angebot. Sichtbarkeit entsteht eher über **aufsteigende Nischen-Ästhetiken**:
  - Neo Deco / Art Deco
  - dunkle, „cottagecore“- oder „village“-Küchen
  - Reading Nooks / Bibliothèque
  - Kurven und Texturen
  - europäische Innenhöfe
  - Wellness-Räume
- „Quiet Luxury“ bzw. beiger Minimalismus ist **reif oder im Abklingen**.
- **Die Ästhetik der Zeit** („character over perfection“, „handmade“, „lived-in“) und der **dokumentierte Backlash gegen KI** in genau den Kategorien Home Decor und Architecture (Pinterest-Filter) sind die größten Risiken für glatte, perfekte KI-Render. Hinzu kommt die KI-Skepsis von 50 % der US-Erwachsenen.
- **Nutzerinteresse an KI-Interior-Tools** ist real (mehrere Apps mit 10M+ Downloads), der Markt ist aber **dicht besetzt** und die Such-Proxies zeigen teils „Peaked“.

---

## 6. Quellenliste

| # | URL | Titel | Datum | Quellentyp |
|---|---|---|---|---|
| 1 | https://newsroom.pinterest.com/news/pinterest-predicts-nonconformity-self-preservation-and-escapism-drive-21-trends-for-2026/ | Pinterest Predicts™: Nonconformity, self-preservation, and escapism drive 21 trends for 2026 | 2025-12-09 | company_primary |
| 2 | https://business.pinterest.com/pinterest-predicts/2026/neo-deco/ | Neo Deco – Pinterest Predicts 2026 (Stat-Items im Seiten-JSON) | 2025-12-09 | company_primary |
| 3 | https://newsroom.pinterest.com/news/pinterest-predicts-20-bold-trends-for-2025/ | Pinterest Predicts: 20 bold trends for 2025 | 2024-12-05 | company_primary |
| 4 | https://business.pinterest.com/pinterest-predicts/2025/castlecore/ | Castlecore – Pinterest Predicts 2025 (Stat-Items im Seiten-JSON) | 2024-11/12 | company_primary |
| 5 | https://newsroom.pinterest.com/news/the-2025-pinterest-fall-trend-report/ | The 2025 Pinterest Fall Trend Report | 2025-08-20 | company_primary |
| 6 | https://newsroom.pinterest.com/news/spring-trend-report-2026/ | Pinterest Spring Trend Report 2026 | 2026-03-17 | company_primary |
| 7 | https://newsroom.pinterest.com/news/summer-trend-report-2026/ | Pinterest Summer Trend Report 2026 | 2026-05-26 | company_primary |
| 8 | https://newsroom.pinterest.com/news/introducing-gen-ai-labels/ | Introducing Gen AI labels | 2025-04-30 | company_primary |
| 9 | https://newsroom.pinterest.com/news/pinterest-rolls-out-new-tools-to-give-users-more-control-over-gen-ai-content/ | Pinterest rolls out new tools to give users more control over GenAI content | 2025-10-16 (upd. 2025-12-12) | company_primary |
| 10 | https://www.nbcnews.com/select/shopping/pinterest-predicts-2026-trend-report-rcna248706 | Pinterest's 2026 trend predictions are here | 2025-12-11 | news_media |
| 11 | https://www.socialmediatoday.com/news/pinterest-publishes-2026-trend-predictions-report/807452/ | Pinterest Publishes 2026 Trend Predictions Report | 2025-12-09 | news_media |
| 12 | https://thecreativeradar.wordpress.com/2026/02/02/pinterest-predicts-2026/ | Pinterest Predicts 2026: Which 2025 Trends Actually Came True? | 2026-02-02 | blog_case_study |
| 13 | https://blog.houzz.com/2026-u-s-houzz-emerging-summer-trends-report/ | 2026 U.S. Houzz Emerging Summer Trends Report | 2026-05-20 | company_primary |
| 14 | https://www.houzz.com/magazine/8-design-trends-emerging-in-2026-stsetivw-vs~185246097 | 8 Design Trends Emerging in 2026 | 2026-05-23 | company_primary |
| 15 | https://www.houzz.com/magazine/2026-u-s-houzz-emerging-summer-trends-report-stsetivw-vs~185266615 | 2026 U.S. Houzz Emerging Summer Trends Report (Magazine) | 2026-05-20 | company_primary |
| 16 | https://kbbonline.com/trends-inspirations/houzz-reports-fall-2026-design-trends/170955 | Houzz Reports Fall 2026 Design Trends | 2026-09-14 | news_media |
| 17 | https://investors.1stdibs.com/news/news-details/2025/2026-Interior-Design-Trends-1stDibs-Survey-Identifies-Maximalism-Chocolate-Brown-and-Vintage-Antiques-as-Top-Designer-Choices/default.aspx | 2026 Interior Design Trends: 1stDibs Survey … | 2025-11-17 | company_primary |
| 18 | https://community.etsy.com/forum/etsy-success-300/topic/etsy-insights-explore-the-trends-shaping-spring-and-summer-2026-165859/ | Etsy Insights: Explore the trends shaping Spring and Summer 2026 | ca. 2026-02 (Daten bis 10.02.2026) | company_primary |
| 19 | https://explodingtopics.com/topic/japandi (analog: /quiet-luxury, /maximalism, /biophilic-design, /ai-interior-design, /interior-ai, /roomgpt, /virtual-staging) | Exploding Topics – Topic-Seiten | abgerufen 2026-09-25 | analytics_platform |
| 20 | https://www.accio.com/business/japandi_trend | Japandi Trend (Accio) | 2026-09-16 | blog_case_study |
| 21 | https://trends.google.com/trends/api/explore | Google Trends (HTTP 429, nicht genutzt) | 2026-09-25 | analytics_platform |
| 22 | https://www.instagram.com/popular/home-decor/ | Home Decor • 901M reels on Instagram | abgerufen 2026-09-25 | instagram_public |
| 23 | https://www.instagram.com/popular/architecture/ | Architecture • 1B reels on Instagram | abgerufen 2026-09-25 | instagram_public |
| 24 | https://www.instagram.com/popular/luxury-homes/ | Luxury Homes • 128M reels on Instagram | abgerufen 2026-09-25 | instagram_public |
| 25 | https://www.instagram.com/popular/japandi/ | Japandi • 841K reels on Instagram | abgerufen 2026-09-25 | instagram_public |
| 26 | https://www.instagram.com/popular/warm-minimalism/ | Warm Minimalism • 1.1M reels on Instagram | abgerufen 2026-09-25 | instagram_public |
| 27 | https://www.instagram.com/popular/ai-interior-design/ | Ai Interior Design • 152K reels on Instagram | abgerufen 2026-09-25 | instagram_public |
| 28 | https://www.instagram.com/popular/dark-academia-interior/ | Dark Academia Interior • 1.4K reels on Instagram | abgerufen 2026-09-25 | instagram_public |
| 29 | https://www.instagram.com/popular/interior-design/ | Interior Design on Instagram (ohne Zahl) | abgerufen 2026-09-25 | instagram_public |
| 30 | data/processed/topics_status.csv (Projekt-Sweep der instagram.com/popular-Seiten) | Topic-Labels „X reels on Instagram“ | 2026-09-25 | instagram_public |
| 31 | https://www.statista.com/outlook/emo/furniture/worldwide | Ecommerce Furniture – Worldwide | 2026 (Market Insights) | industry_report |
| 32 | https://www.statista.com/outlook/cmo/furniture/worldwide | Furniture – Worldwide | 2026 | industry_report |
| 33 | https://www.statista.com/outlook/cmo/furniture/home-decor/worldwide | Home Décor – Worldwide | 2026 | industry_report |
| 34 | https://www.statista.com/outlook/emo/furniture/home-decor/worldwide | Ecommerce Home Décor (Werte hinter Paywall) | 2026 | industry_report |
| 35 | https://www.mordorintelligence.com/industry-reports/home-decor-market | Home Decor Market Size & Share Analysis (2026–2031) | 2026-08-06 | industry_report |
| 36 | https://www.technavio.com/report/online-home-decor-market-industry-analysis | Online Home Decor Market 2024–2028 | 2024-02 | industry_report |
| 37 | https://play.google.com/store/search?q=ai%20interior%20design&c=apps&hl=en&gl=US (+ 30 Detailseiten, z. B. …details?id=com.planner5d.planner5d, interior.home.design.ai, ai.interior.design.home.renovation.app, com.icandesignapp.all, com.autodesk.homestyler, pro.airemodel.android) | Google Play – AI interior design apps | abgerufen 2026-09-25 | other |
| 38 | https://www.roomgpt.io/ | RoomGPT | abgerufen 2026-09-25 (Claim ~2023) | company_primary |
| 39 | https://github.com/Nutlope/roomGPT | Nutlope/roomGPT (GitHub) | abgerufen 2026-09-25 | other |
| 40 | https://interiorai.com/ | Interior AI | abgerufen 2026-09-25 | company_primary |
| 41 | https://levels.io/new-420k-mo-revenue-record-lex-fridman | I hit a new $420,000/mo revenue record … | 2024-09-22 | company_primary |
| 42 | https://levels.io/wayfair-used-interior-ai-to-build-their-own | Wayfair used my AI interior design tool to build their own | 2024-03-27 | company_primary |
| 43 | https://www.homestyler.com/ | Homestyler | abgerufen 2026-09-25 | company_primary |
| 44 | https://techcrunch.com/2025/04/30/pinterest-launches-new-tools-to-fight-ai-slop/ | Pinterest launches new tools to fight AI slop | 2025-04-30 | news_media |
| 45 | https://techcrunch.com/2025/10/16/pinterest-adds-controls-to-let-you-limit-the-amount-of-ai-slop-in-your-feed/ | Pinterest adds controls to let you limit the amount of AI slop in your feed | 2025-10-16 | news_media |
| 46 | https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/ | AI Slop Report: The Global Rise of Low-Quality AI Videos | Daten Okt. 2025 | industry_report |
| 47 | https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/ | How Americans View AI and Its Impact on People and Society | 2025-09-17 | other |

**Versucht, aber nicht zugänglich oder ohne verwertbaren Inhalt:**
- axios.com/2025/12/09/2026-pinterest-trend-report (403)
- apartmenttherapy.com (403)
- grandviewresearch.com/industry-analysis/home-decor-market (403)
- alliedmarketresearch.com/home-decor-market (403)
- newsroom.gettyimages.com (403)
- wwd.com (Umleitung auf tollbit, nicht gefolgt)
- homesandgardens.com (Inhalt abgeschnitten)
- kendallflavin.substack.com (Paywall)
- reddit.com (403)
- fortunebusinessinsights.com (falsche Seite)
- imarcgroup.com (404)
- precedenceresearch.com (keine Daten)
- trends.google.com (429)

## Faktencheck (automatisiert)

Geprüft am 2026-09-25 gegen die jeweils zitierte URL (Rohtext/HTML, bei 403 über WebFetch bzw. das vom Quellserver selbst verlinkte Dokument). Andere Quellen wurden nicht zur „Rettung“ einer Angabe herangezogen, abweichende Fundstellen werden nur vermerkt.

| # | Claim (Kurzform) | Urteil | Begründung (eine Zeile) |
|---|---|---|---|
| 1 | Pinterest Predicts 2026: FunHaus / Neo Deco / Afrohemian Decor, +35 % bis +220 %; 3 von 21 Trends Home-Decor | CONFIRMED | Alle 16 Suchbegriff-Werte und „21 trends“ stehen wörtlich im Newsroom-Text; „3 von 21“ ist eigene Zählung (Extra Celestial nennt „holographic home accents“, Opera Aesthetic Party-Deko nur am Rand). |
| 2 | Methodik-Zitat 2026 (Sep 2023–Aug 2025, normalisierte Suchen Sep 2024–Aug 2025); 88 % Trefferquote; 67 % Gen Z; 600 Mio. Nutzer | NOT_CONFIRMED | Methodik-Fußnote steht wörtlich auf der Neo-Deco-Seite, aber 88 %, 67 % und 600 Mio. kommen dort nicht vor; sie stehen in der Newsroom-Meldung (URL von Claim 1/3), also Quellenangabe falsch. |
| 3 | Pinterest 2026: „4.4x faster … seven years ago“, „Curating, not copying“, „After years of heavy minimalism“, 55 % Komfort | CONFIRMED | Alle vier Stellen stehen wörtlich in der Newsroom-Meldung (55 % „of global respondents prioritizing it as a need“). |
| 4 | Pinterest Predicts 2025: 14 Home-Werte (+40 % bis +630 %) und Methodik Sep 2022–Aug 2024 | CONFIRMED | Alle 14 Werte und die Methodik-Fußnote stehen in den Seitendaten; nur medieval core (+110 %) und castle house plans (+45 %) sind Castlecore-Werte, die übrigen gehören zu anderen 2025-Trends (Mix & Maximalist, Primary Play, Cherry Coded, Terra Futura, Surreal Soirees, Dolled Up), die in die Seite eingebettet sind. |
| 5 | Pinterest 2025: „80% accurate“ über fünf Jahre; „Over half a billion“ pro Monat; Metadaten-Zitat „ditching minimalist design…“ | CONFIRMED | 80 % („past five years“) und „Over half a billion“ stehen wörtlich im Newsroom-Text; das Zitat „ditching minimalist design“ steht dagegen NICHT auf dieser Seite, sondern ist die og:description von Mix & Maximalist (in die Seite aus Claim 4 eingebettet). |
| 6 | Pinterest Fall 2025 (Home): Luxe office +2.766 %, Cubicle makeover +2.767 % … New art deco +497 %; kein Datenfenster | CONFIRMED | Alle 7 Werte stehen wörtlich im Text; Bandbreite +388 % (Accent tile behind stove) bis +2.767 % stimmt; im Seitentext gibt es keine Methodik-Fußnote. |
| 7 | Pinterest Spring 2026 (Home): 11 Werte +245 % bis +915 %; „home isn't about perfection“; Fußnoten unklar | CONFIRMED | Alle 11 Werte und das Zitat stehen wörtlich im Text; laut Reihenfolge der Fußnoten gehört Fußnote 1 („Q4 2025“) zu „600 million monthly active users“ und Fußnote 2 („January 2025 vs January 2026“) zu den Suchwerten. |
| 8 | Houzz Emerging Summer Trends 2026, 16 Werte +20 % bis +1.900 % | CORRECTED(scalloped tile „more than 3x“; mahjong room „nearly 20x“; French courtyards „nearly 6x“; Italian courtyards „up 4.5x“) | Methodik und 12 Prozentwerte stimmen wörtlich; für vier Begriffe nennt Houzz nur Faktoren. +300 %/+1.900 %/+500 %/+350 % sind Umrechnungen des Analysten, „more than 3x“ entspräche folgerichtig > +200 %, nicht +300 %. |
| 9 | Houzz Fall 2026: fünf Trend-Überschriften; 61 % bleiben 11+ Jahre, 44 % „forever home“ | CONFIRMED | 61 % und 44 % (2026 Houzz & Home Study) stehen wörtlich im KBB-Artikel; zwei Überschriften sind leicht gekürzt („…Take Hold“, „Pros Are Designing Homes to Evolve“). |
| 10 | 1stDibs Survey: n=468, Juli–Aug 2025; 39 %/38 %; Chocolate Brown 33 % (17 % 2022); KI 29 % vs. 9 %; +20 %; 24 % dagegen; 92 % Zölle | CONFIRMED | Alles wörtlich in der Pressemitteilung (IR-Seite bzw. ihr verlinktes PDF); 92 % bezieht sich auf „some degree of negative impact“. |
| 11 | 1stDibs via BusinessWire: Butter Yellow 14 %→30 %, Curvy Furniture 43 %, Wicker/Rattan 27 % | NOT_CONFIRMED | Die zitierte BusinessWire-URL ist blockiert (403 bzw. Cloudflare), ließ sich also nicht prüfen; dieselben Werte stehen wörtlich im gleichlautenden Release auf der 1stDibs-IR-Seite (Claim 10), dorthin umzitieren. |
| 12 | Etsy Insights S/S 2026: Wall Art Decor +110 %, Gallery Prints +80 %; Zitat Gen Z / Handwerk | CONFIRMED | Werte, Datenfenster („as of February 10, 2026 … last three months compared to the same time last year“) und Zitat stehen wörtlich im Beitrag (Autorin: Etsys „Resident Trend Expert“); Einschränkung: nur Aktivität angemeldeter US-Nutzer. |
