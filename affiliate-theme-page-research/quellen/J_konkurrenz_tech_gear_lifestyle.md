# J – Konkurrenz- und Case-Study-Datenbank: Tech-, Gear- und Lifestyle-Nischen

**Studie:** Welche Nische und welcher Markt eignen sich für eine KI-generierte, faceless Instagram-Reels-Theme-Page mit Affiliate-Monetarisierung (Content → Reichweite → Link in Bio → Affiliate-Kauf)?
**Teilbereich J:** Tech, Gear und Lifestyle (EN und DE)
**Prüfdatum:** 2026-09-26
**Rohdaten:** `raw_competitors_tech.csv` (97 Zeilen, 27 Spalten, UTF-8)

---

## 0. Kurzfazit

- **Datenbasis:** 97 Account-Profile (42 Instagram, 31 YouTube, 23 TikTok, 1 reiner Amazon-Storefront) aus rund 85 Marken bzw. Betreibern und 44 Nischen-Labels. **40 Zeilen bzw. 31 eindeutige Marken sind Case Studies** mit belegtem Affiliate-Modell (Amazon-Storefront, Amazon-Tag, ShareASale, Refersion, Impact/Walmart, ShopMy, Brand-Referral oder schriftliche Affiliate-Disclosure). Davon sind rund 22 Marken faceless bzw. Theme-Pages. Die übrigen Case Studies sind Media- oder Personen-Marken und dienen als Kontext.
- **Am besten belegt ist das Modell „Theme-Page + Affiliate“ in diesen Nischen:**
  1. **Desk-/Gaming-Setups:** 11 Setup-Pages mit Affiliate, davon 7 mit Amazon-Storefront.
  2. **Tech-/Home-Gadgets („Amazon Finds“):** Justice Buys mit 2,13 Mio. YouTube-Abos und 1,5 Mio. TikTok-Followern (VERIFIED) ist der größte Einzel-Case.
  3. **Tesla-Zubehör:** TaylorOnWheels.
  4. **3D-Druck:** The 3D Wizard.
  5. **DIY/Werkzeug in DE:** Malerart mit 464K YouTube-Abos, 508K TikTok-Followern und amazon.de-Tags.
  6. **EDC:** Everyday Carry.
  7. **LEGO in DE:** über Blog-Modelle (Promobricks, Zusammengebaut).
- **Schwach oder nicht belegt:** Uhren (Media- oder Händler-Modelle), Golf (Merch statt Affiliate), Camping/Vanlife (Kurse, Bücher, Merch), Audio/Hi-Fi und Schmuck (keine Treffer).
- **DE vs. EN:** Im DE-Markt fanden wir **keine einzige nennenswerte deutschsprachige faceless Setup- oder Gadget-Theme-Page auf Instagram**. Die DE-Konkurrenz besteht aus Plattformen und Blogs (mydealz, MyTopDeals, Promobricks, Zusammengebaut, Grailify), die auf Social Video teils kaum aktiv sind (MyTopDeals: 1,2K TikTok-Follower). Hinzu kommt ein einzelner starker Faceless-Creator (Malerart, Werkzeug/DIY). Ein Sonderfall: @cleandesksetup (48K) ist eine englisch benannte Page, die bereits mit amazon.de-Tags monetarisiert.
- **KI plus Affiliate:** Nur ein Beleg in Tech/Gear. @topdailysetups (67K) zeigt 3D-/CGI-Setups und hat einen Amazon-Storefront. Die übrigen KI-Kanäle (Bau Rausch mit 621K, Dreamy Interior mit 315K) monetarisieren ohne Affiliate-Links. Ein Negativbeispiel ist Top Finds Daily: 166K Abos, aber nur 1,6K Median-Views.

---

## 1. Methodik & Grenzen

### 1.1 Vorgehen

1. **Account-Discovery**
   - WebSearch-Snippets („site:instagram.com …“), dort mit Follower- und Post-Zahl.
   - Die Liste „30 Instagram Sources for Desk Setup Inspiration“ (geekyminded.com, Stand 06/2023, mit Follower-Zahlen).
   - NexLev-Vektorsuche über YouTube-Shorts-Kanäle (faceless/AI-Flags, Median-Views, Uploads).
   - Gezieltes Handle-Probing bei bekannten Marken bzw. Seed-Handles.
2. **Affiliate-Nachweis:** Abruf öffentlicher Seiten.
   - Linktree: JSON aus `__NEXT_DATA__` mit Bio, Social-Links und allen Links. Kurzlinks (amzn.to, a.co) wurden aufgelöst, um Domain und `tag=` zu sehen.
   - Amazon-Storefront: `amazon.com/shop/<handle>` bzw. `amazon.de/shop/<handle>`. Ergebnis 200 mit „<Name>'s Amazon Page“ = existiert, 404 = nicht unter diesem Handle.
   - Websites: Disclosure-Texte wie „earn a commission“ oder „Provision“.
   - YouTube-About-Links.
3. **Reichweitendaten**
   - TikTok-Profil-JSON: Follower, Likes, Videos und Bio-Link. Direkt abgerufen, daher **VERIFIED**.
   - YouTube-About-Seite: Abonnenten, daher **VERIFIED**.
   - NexLev: Median-Views, Durchschnitt, Top-Short und Upload-Zahl. Drittanbieter, daher **ESTIMATED**.
   - Instagram-Follower: ausschließlich aus Suchsnippets bzw. der geekyminded-Liste, daher **ESTIMATED**.

### 1.2 Datenqualität

| Kennzeichnung | Bedeutung |
|---|---|
| VERIFIED | direkt auf Plattform/Primärquelle abgerufen (TikTok-JSON, YouTube-About, Linktree, Amazon-Storefront, Website-Disclosure) |
| ESTIMATED | Suchsnippet, geekyminded (2023) oder NexLev (Drittanbieter) |
| ESTIMATED (CLAIMED) | Eigenangabe des Betreibers (z. B. „1M on Instagram“) |
| UNKNOWN | nicht bestimmbar |

### 1.3 Grenzen (wichtig für die Interpretation)

- **Instagram-Login-Wall:** Instagram lieferte für jeden direkten Abruf 429, Login-Redirect oder 401. Das betraf Profile, Embed-Endpunkte und die Web-Profile-API. **Kein Instagram-Wert ist VERIFIED.** Views und Median-Views von Instagram-Reels sind durchgängig UNKNOWN.
- **Drittanbieter blockiert:** Social Blade, HypeAuditor, StarNgage, Heepsy, Feedspot, Picuki und Imginn antworteten mit 403, 502 oder Cloudflare-Sperre. Engagement-Raten liegen deshalb nicht vor.
- **Suchbudget:** Das gemeinsame WebSearch-Budget der Session war nach wenigen Abfragen dieses Teilbereichs erschöpft. Die Discovery stützt sich danach auf Direktabrufe und NexLev. Eine alternative Web-Suchmaschine wurde bewusst nicht eingesetzt.
- **Folge:** Deutsche Instagram-Pages sind wahrscheinlich **unterrepräsentiert**. Die Aussage „kaum DE-Theme-Pages“ ist ein starkes Indiz, aber kein Vollzensus.
- **Zuordnungsrisiko Handle ↔ Storefront/Linktree:** Wo ein Linktree oder Storefront nur über ein identisches Handle gefunden wurde, ist das in den Notizen vermerkt. Das betrifft z. B. topdailysetups, chillsetup und killergamingsetups. Wo Linktree-Social-Links oder YouTube-About-Links die Zuordnung bestätigen, gilt sie als gesichert.
- **Größenklassen:** Bei Instagram teils auf Basis von 2023-Daten (geekyminded). Ist nur der Stand von 2023 bekannt, steht das in der Spalte `follower`.
- **Kit.co wurde am 2026-05-11 eingestellt** (kit.co: „Kit.co has closed … Service discontinued“; Profile liefern HTTP 410). Alle kit.co-Collections von Setup-Pages sind seitdem tote Links. Das betrifft u. a. thedreamsetup, isetups und setupcreate.

---

## 2. Datenbasis-Überblick

| Kennzahl | Wert |
|---|---|
| Zeilen (Account-Profile) | 97 |
| Instagram / YouTube / TikTok / Storefront | 42 / 31 / 23 / 1 |
| Größenklassen | 1M+: 4 · 500k–1M: 8 · 100k–500k: 26 · 10k–100k: 35 · <10k: 5 · UNKNOWN: 19 |
| Affiliate = ja (Zeilen) | 41 |
| Case Studies (Zeilen / eindeutige Marken) | 40 / 31 |
| DE-sprachige bzw. DE-Markt-Zeilen | 17 (14 Marken) |
| Accounts mit KI-/3D-Content (AI/mixed) | 7 Zeilen (topdailysetups, Ryzen4070, ryzentek, BauRausch, DreamyInterior, HomeGraphix, topfndsdaily) |

---

## 3. Befunde je Nische (EN vs. DE)

| Nische | EN-Befund | DE-Befund | Modell bewiesen? |
|---|---|---|---|
| **Desk Setups / Home Office** | Reifes Theme-Page-Ökosystem: 23 IG-Pages (15K–651K). 11 mit Affiliate: Amazon-Storefronts (thedreamsetup, setuputic, killergamingsetups, chillsetup, topdailysetups, setupcreate, thesetupaddict), Brand-Referrals (Keychron, MOFT, Grovemade, Ergonofis via ShareASale/Refersion). Mehrere große Pages ohne Monetarisierung (minimalsetups 291K, minimal.desksetups 206K). Teils sinkende Follower seit 2023 (minimalsetups −13 %, killergamingsetups −16 %). | Keine DE-sprachige Setup-Page gefunden. **@cleandesksetup** (48K) nutzt einen DE-Linktree mit amazon.de-Tag (`pintrendde-21`, Links ca. 03/2026) | **Ja (stark)** |
| **Gaming Setups / PC Accessories** | IG: killergamingsetups (213K, Storefront), cleanpcsetup (71,5K, amzn + keyboardnerd), setupwarriors (81K, 125 Posts). YT-Shorts: Ryzen4070 (82,6K, Median 3,95 Mio., Windows-Key-Referral), LGA-1155 (Median 464K), R4 DECK (eigener Shop) | Ryzen4070 laut NexLev mit Betreiber in DE, aber EN-Content; keine DE-Gaming-Setup-Page gefunden | **Ja** (IG + Shorts) |
| **Tech Gadgets / Amazon Finds** | Stärkste Reichweiten: Justice Buys (YT 2,13 Mio., TT 1,5 Mio., IG laut Eigenangabe 1 Mio.; Website mit 111 Produktlinks, ShopMy, Walmart/Impact). Weitere: dealify (54,8K, 45 Amazon-Links, ~15 Shorts/Woche), Sathi Mart (26,3K, 33 Amazon-Links). Worldwide Gadgets (484K) = Dropshipping statt Affiliate | Deal-Plattformen: mydealz.de (TT 571,8K), MyTopDeals (TT 1,2K, „Affiliate Links“ im Linktree). Einzelne Kleinst-Pages (AmazonGlowUpDE 0 Follower, techdeals.de inaktiv). Smartcase-De = Eigenprodukt | **Ja (sehr stark, EN)**; DE nur Plattformen |
| **Smartphone-Zubehör** | über Gadget-Accounts abgedeckt | Smartcase-De (61,4K, Eigenprodukt, 1 Viralhit mit 73 Mio.) | teilweise |
| **EDC** | Everyday Carry (TT 109,4K, YT 39,3K, Amazon-Storefront, beacons-Shop), UrbanEDC (Linktree → Affiliate-Publisher-Website) | nicht gefunden | **Ja** |
| **Fotografie / Kameras** | Shorts-Reichweite vorhanden (lensevision 238K, Median 1,6 Mio.; cgm.photos 67,8K), aber keine Affiliate-Links | nicht gefunden | **Nein (Lücke)** |
| **Audio / Hi-Fi** | keine faceless Audio-Theme-Page gefunden | – | **Datenlücke** |
| **Car Accessories / Detailing / Tesla** | TaylorOnWheels (TT 28,4K, YT 31,2K): Storefront + 4 Tesla-Aftermarket-Codes + Tesla-Referral. Obsessed Garage (Person, Storefront). Bacotes (591K, Median 3,1 Mio.) ohne Links | liquidelements (Marke, 1,8K TT); keine DE-Detailing-Theme-Page gefunden | **Ja** (Tesla-Nische) |
| **Tools / DIY / Werkstatt** | – | **Malerart** (YT 464K, Median 10,5 Mio.; TT 508K; IG malerart_): amazon.de-Tags `malerart2107-21`, `malerart0c-21`, „(Anzeige)“. Bau Rausch (KI, 621K) ohne Links | **Ja (DE!)** |
| **Travel Gear** | Pack Hacker (YT 140K, Storefront, „may earn an affiliate commission“) – Media | nicht gefunden | Ja (Media, nicht faceless) |
| **Camping / Van Life / Overland** | Vanlife Diaries, Project Vanlife, Overland Bound: Monetarisierung über Buch, Kurs, Events, Merch. Alexan Strib (736K, Top 310 Mio.) ohne Links | nicht gefunden | **Nein** (eigene Produkte dominieren) |
| **Fitness / Home Gym** | Garage Gym Reviews (TT 58,3K; Disclosure: Affiliate für „nearly every product“) – Media/Person | nicht gefunden | Ja (Media) |
| **Running** | Doctors of Running (Linktree mit 408 Review-Links; Disclosure nicht geprüft) | nicht gefunden | unklar |
| **Cycling / E-Bikes** | ProViewGear (289K, Top 108 Mio., Kamera-Helm-Demo) ohne Links; BikeRadar (Media) | mtbnews (TT 4,1K) – DE-Portal schwach auf TikTok | **Nein (Lücke)** |
| **Golf** | Golf Gods: Theme-Page → eigene Merch-Marke + Dabble-Referral. Faceless Highlight-Shorts (Everythingolf: Median 3,65 Mio. bei 27K Abos) ohne Links | nicht gefunden | teilweise (Merch/Referral) |
| **Uhren** | Media/Händler (Worn & Wound, Teddy Baldassarre) mit Eigenhandel | Chrono24 (TT 273,9K, DE-Unternehmen = potenzieller Partner) | **Nein** (als Theme-Page nicht belegt) |
| **Sneakers** | Sneaker News (TT 648,7K), Media | Grailify (TT 32,1K), snkraddicted (TT 43K, faceless), Sneakerjagers (TT 20,5K, „Provision“-Disclosure) | Ja (Release-Plattformen) |
| **Jewelry** | nichts gefunden | nichts gefunden | **Datenlücke** |
| **Beauty / Skincare (faceless)** | Modern Girl Aesthetic (33,3K → Storefront shair10); Nerviea23 (643K, Top 585 Mio., Shop epixen.com); Skinfluence (287K) ohne Affiliate | AmazonGlowUpDE (0 Follower) | Ja (klein) |
| **Luxury Lifestyle / Gear-Kuratierung** | Uncrate (Storefront), Gear Patrol (Linktree mit 728 Links, fave.co/amzn), Cool Material („Daily Steals“), Man of Many (TT 119K) | – | Ja (Media-Kuratierung) |
| **LEGO / Collectibles / 3D-Druck** | The 3D Wizard (TT 179,5K, YT 77,6K, „Printers I Use (Affiliate)“ via ShareASale); PrintLair, MC Print Lab ohne Affiliate | Promobricks (TT 19,6K), Zusammengebaut (TT 140,3K, ukonio media GmbH): Affiliate-Disclosure (LEGO, Amazon, eBay, Alternate, Proshop) | **Ja** |

---

## 4. Case Studies (ausführlich)

> Alle Zahlen stammen aus der CSV. Die Qualitätskennzeichnung steht dort je Zelle.

### 4.1 @thedreamsetup (Instagram, EN) – Desk Setups
- **Reichweite:** 374K Follower (Snippet 09/2026). 2023 waren es 408K bei 3.844 Posts.
- **Link in Bio:** Linktree mit dem Titel „All Product Links“. Bio: *„Links to regularly featured products and discount codes for our favourite brands“*.
- **Affiliate:**
  - Amazon-Storefront `amazon.com/shop/thedreamsetup`.
  - ShareASale-Link zu Ergonofis (Premium-Schreibtische).
  - Grovemade über Refersion (`?rfsn=`), mit Code THEDREAMSETUP.
  - kit.co-Setup-Liste (`kit.co/joekerny`, seit der Kit-Schließung tot).
- **Lehre:** Die Page setzt auf Premium-Marken mit hohem Warenkorbwert statt Amazon-Kleinkram. Durch die Kit-Schließung bestehen Linkfäule und Conversion-Verlust.

### 4.2 @isetups (Instagram, EN) – Minimal Setups
- **Reichweite:** 651K Follower, 4.940 Posts (Snippet).
- **Link in Bio:** Linktree mit Disclosure *„We may earn small commissions for purchases made through links“*.
- **Affiliate:**
  - Refersion für Grovemade und LaMetric.
  - Anker-Trackinglink.
  - 4 kit.co-Listen, heute tot: „6 Best Keyboards for Mac Users“, „7 Essential MacBook Accessories“ u. a.
- **Betreiber:** laut TikTok-Bio @sebastiaanchia.
- **Lehre:** Das Top-N-Listenformat wurde als Collection monetarisiert. Das Cross-Posting ist ungenutzt: TikTok hat nur 379 Follower.

### 4.3 @setuputic (Instagram, EN)
- **Reichweite:** 241K Follower. Seit 2023 plus 30 %.
- **Link in Bio:** Linktree mit *„Curated desk setups. Clean aesthetics. Click and copy the look.“* Er führt zum Amazon-Storefront `amazon.com/shop/setuputic`. Die Seite trägt den Hinweis „Earns revenue … may earn commission from purchases“.
- **Eigenprodukt:** Wallpaper-Pack auf Gumroad.
- **Lehre:** „Copy the look“ ist die direkteste Übersetzung von Setup-Content in einen Kauf.

### 4.4 @killergamingsetups (Instagram, EN) – Gaming
- **Reichweite:** 213K Follower (2023: 255K).
- **Affiliate:** Amazon-Storefront plus Linktree mit Amazon-Tag `2014gamersunite-20`. Verlinkt sind der Samsung 49" Curved Monitor, Nanoleaf Aurora und Corsair- bzw. Phanteks-Gehäuse.
- **Lehre:** Hochpreisige Gaming-Hardware wird verlinkt, die Links sind jedoch veraltet. Die Page ist ungepflegt und verliert Follower.

### 4.5 @topdailysetups (Instagram, EN) – 3D-/CGI-Setups
- **Reichweite:** 67K Follower, 1.319 Posts. Profiltitel „3D Room Setups | Gaming Room Ideas“.
- **Affiliate:** Amazon-Storefront `amazon.com/shop/topdailysetups` (Share-Tag `kevindejong-20`).
- **Lehre:** Einziger Beleg in Tech/Gear, dass **synthetische Setup-Visuals mit einem Amazon-Storefront kombiniert** werden. Das ist das Nächste am Zielmodell „KI-Theme-Page + Affiliate“. Die Reichweite ist aber mittel, der TikTok-Ableger hat nur 7 Follower.

### 4.6 @cleandesksetup (Instagram, EN-Name, DE-Monetarisierung)
- **Reichweite:** 48K Follower.
- **Link in Bio:** Linktree auf Deutsch: *„Die besten Gadgets für ein cleanes & produktives Desk Setup“*.
- **Affiliate:** 5 amzn.to-Links auf amazon.de mit Tag `pintrendde-21`: Wireless Charger, Desk Organizer, Monitorlicht, LED und Laptop-Stand. Die Links wurden ca. im März 2026 erzeugt.
- **Lehre:** Ein bestehender englischer Setup-Account wird **auf den DE-Markt umgelenkt**. Das ist ein Hinweis, dass Betreiber DE-Affiliate für lohnend halten. Die Produkte sind durchweg günstig (Impulskauf).

### 4.7 @thesetuptoday / @cleanpcsetup / @setupcreate / @chillsetup / @thesetupaddict (Instagram, EN)
- **@thesetuptoday** (41,9K, 2023): Direkte Brand-Programme statt Amazon, nämlich Keychron (`refr.cc`), MOFT (`?ref=`) und Magflott (Kickbooster).
- **@cleanpcsetup** (71,5K, 2023): amzn.to plus keyboardnerd über UpPromote (`sca_ref`).
- **@setupcreate** (48,2K): Storefront (Tag `setupcreate-20`) plus 5 kit.co-Top-5-Listen, alle tot.
- **@chillsetup** (106K, 2023): Storefront plus App-Affiliate (theplug.co).
- **@thesetupaddict** (heute thesetupaddiction): Storefront plus Collectibles-Fokus.

### 4.8 Justice Buys (YouTube / TikTok / Instagram, EN) – Gadgets
- **Reichweite:**
  - YouTube: 2,13 Mio. Abos (VERIFIED), Median 26,5 Mio. Views, Top-Short 81 Mio.
  - TikTok: 1,5 Mio. Follower, 49,8 Mio. Likes (VERIFIED).
  - Instagram @justice_buys: laut Eigenangabe 1 Mio.
- **Format:** faceless Compilations wie „Top 15 Amazon Products of 2023“ oder „10 Things I Bought…“.
- **Affiliate:**
  - Website justicebuys.com mit ~111 Produktlinks über joylink.io, dazu ShopMy, Amazon und Anker/Soundcore. Disclosure: *„As an affiliate, I earn from qualifying purchases“*.
  - Der IG-Linktree (@justice_buys) enthält 19 Walmart-Affiliate-Links (Impact), dazu Impact-Brands (sjv.io/pxf.io) und einen eigenen Shop.
  - Management über die Agentur undercurrent.net.
- **Lehre:** Der größte Beleg im Gadget-Segment. Das Modell skaliert über **mehrere Händler-Programme**, nicht nur Amazon, und über eine **eigene Linkseite**.

### 4.9 dealify & Sathi Mart (YouTube Shorts, EN) – Amazon-Finds-Fabriken
- **dealify:** 54,8K Abos, 531 Shorts seit 01/2026 (~15 pro Woche). Median 140,5K, Top 141 Mio. Linktree mit 45 amzn.to-Links.
- **Sathi Mart:** Betreiber laut NexLev in Indien. 26,3K Abos, ~10 Shorts pro Woche, 33 Amazon-Links.
- **Lehre:** Hochfrequenz und das Muster „Get this … – Link in bio“ sind billig zu replizieren. Die Nische ist entsprechend wettbewerbsintensiv, die Median-Views sind moderat.

### 4.10 TaylorOnWheels (TikTok / YouTube / IG, EN) – Tesla-Zubehör
- **Reichweite:** TikTok 28,4K, YouTube 31,2K (Median 81,5K, ~8 Shorts pro Woche). Instagram @tayloronwheels12.
- **Affiliate:**
  - Amazon-Storefront (Tag `tayloronwheel-20`).
  - HaloBLK, Hansshow (`bg_ref`), 3W Liners (`ref`) und EVBASE, alle mit Rabattcode.
  - Tesla-Referral („Get $1,000 off a Tesla“) und Robinhood-Referral.
- **Lehre:** **Eine enge Nische mit Aftermarket-Marken** bringt höhere Provisionen und Rabattcodes als Amazon. Die Views sind sehr stabil (Median ≈ Durchschnitt).

### 4.11 Everyday Carry (TikTok / YouTube, EN) – EDC
- **Reichweite:** TikTok 109,4K, YouTube 39,3K.
- **Affiliate:** Amazon-Storefront `amazon.com/shop/everydaycarry` plus beacons-Shop „Shop Featured Gear“.
- **Einordnung:** Gründer von everydaycarry.com (Person plus Theme-Marke).

### 4.12 The 3D Wizard (TikTok / YouTube, EN) – 3D-Druck
- **Reichweite:** TikTok 179,5K (5,2 Mio. Likes), YouTube 77,6K (Median 596,5K).
- **Affiliate:** Linktree mit „Printers I Use (Affiliate)“ über ShareASale, dazu ein Tripo-3D-AI-Referral.
- **Lehre:** Wenige, **hochpreisige** Affiliate-Produkte (3D-Drucker) plus Tool-Referral.

### 4.13 Malerart (YouTube / TikTok / IG, DE) – Werkzeug/DIY
- **Reichweite:** YouTube 464K Abos, Median 10,5 Mio., Top 194 Mio. TikTok 508,4K. IG @malerart_.
- **Affiliate:** Linktree mit amazon.de-Links. Die Tags lauten `malerart2107-21` und `malerart0c-21`. Verlinkt sind tesa Easy Cover, ROLLINGDOG-Pinselkamm, GoPro und ein Cutter mit „(Anzeige)“.
- **Schwachstelle:** Der TikTok-Bio-Link zeigt auf Twitch, nicht auf den Affiliate-Linktree.
- **Lehre:** **Stärkster DE-Beleg.** Deutschsprachiger faceless Hands-Content erreicht internationale Massenreichweite und wird mit amazon.de monetarisiert.

### 4.14 Promobricks & Zusammengebaut (TikTok + Blog, DE) – LEGO
- **Promobricks** (TikTok 19,6K) schreibt: *„Diese Webseite finanziert sich durch Affiliate-Links zu ausgewählten Partnerprogrammen wie beispielsweise von LEGO, Amazon oder eBay“*.
- **Zusammengebaut** (TikTok 140,3K, 1.247 Videos, ukonio media GmbH Hamburg) schreibt: *„Hinweis: Es handelt sich hierbei um Affiliate-Links … erhalten wir eine Provision“*.
- **Lehre:** Die DE-Konkurrenz in Collectibles ist **professionell und Blog-zentriert**. Social Video dient als Zubringer.

### 4.15 Weitere Case Studies (Kurzform)
- **Pack Hacker** (Travel, YT 140K): Storefront plus Website-Disclosure. Media/Team.
- **Garage Gym Reviews** (Home Gym, TT 58,3K): Affiliate-Disclosure, *„affiliate program … for nearly every product“*. Media/Person.
- **Golf Gods** (Golf, IG): eigene Merch-Marke plus Dabble-Referral.
- **Gear Patrol** (Lifestyle-Gear, IG): Linktree mit 728 Links (fave.co, amzn.to). Media.
- **Uncrate** (Lifestyle-Gear): Amazon-Storefront (Tag `uncrate-20`).
- **Modern Girl Aesthetic** (Beauty faceless, YT 33,3K): a.co-Link führt zum Storefront `shair10`.
- **Sneakerjagers** (NL/DE, TT 20,5K): Disclosure *„… dass wir von Sneakerjagers eine Provision verdienen“*.
- **MyTopDeals** (DE-Deals, TT 1,2K): „*MyTopDeals Affiliate Links“ im Linktree.
- **Ryzen4070 / ryzentek** (PC-Gaming, YT 82,6K, TT 11,3K): Windows-Key-Referral keysfan.com mit Code RYZEN50.
- **UrbanEDC** (EDC, IG): Linktree „Where to buy gear shown in pics“ führt zu einem Affiliate-Publisher.
- **Obsessed Garage** (Detailing, Person): Amazon-Storefront.

---

## 5. Antworten auf die qualitativen Fragen

### 5.1 Welche Tech-/Gear-Nischen beweisen, dass „Theme-Page + Affiliate“ funktioniert?

| Beweisstärke | Nischen | Belege |
|---|---|---|
| **Stark** | Desk-/Gaming-Setups | 11 Setup-Pages mit Affiliate, 7 Storefronts, Premium-Brand-Referrals; Pages bis 651K Follower |
| **Stark** | Tech-/Home-Gadgets (Amazon Finds) | Justice Buys (Millionenreichweite, Multi-Händler-Affiliate); dealify, Sathi Mart |
| **Mittel** | Tesla-Zubehör | TaylorOnWheels |
| **Mittel** | EDC | Everyday Carry, UrbanEDC |
| **Mittel** | 3D-Druck | The 3D Wizard |
| **Mittel** | DIY/Werkzeug (DE) | Malerart |
| **Mittel** | LEGO (DE) | Promobricks, Zusammengebaut |
| **Mittel** | Beauty faceless | Modern Girl Aesthetic |
| **Nur Media/Person** | Travel | Pack Hacker |
| **Nur Media/Person** | Home Gym | Garage Gym Reviews |
| **Nur Media/Person** | Lifestyle-Gear | Gear Patrol, Uncrate |
| **Nicht belegt** | Uhren | Media/Händler |
| **Nicht belegt** | Camping/Vanlife | Kurse, Merch |
| **Nicht belegt** | Golf | Merch/Wetten statt Affiliate |
| **Nicht belegt** | Fotografie, Cycling | große Reichweiten ohne Links |
| **Nicht belegt** | Audio, Schmuck | keine Treffer |

### 5.2 Deutschsprachige vs. englischsprachige Konkurrenz

- **EN:** Dichtes Feld aus Setup-Theme-Pages (23 IG-Pages in unserer Stichprobe, 11 monetarisiert) sowie professionellen Gadget-Operationen mit Agentur-Management (Justice Buys) und Offshore-„Amazon-Finds“-Fabriken (dealify, Sathi Mart).
- **DE (14 Marken identifiziert):**
  - **Professionelle Plattformen/Blogs:** mydealz (TikTok 571,8K, größte DE-Deal-Community), MyTopDeals (Social schwach), Promobricks, Zusammengebaut (140K TikTok), Grailify (32K), Sneakerjagers.
  - **Faceless Creator:** Malerart (Werkzeug/DIY, sehr groß), snkraddicted (Sneaker, 43K), Bau Rausch (KI-DIY, 621K, ohne Affiliate).
  - **Mydealz-ähnliche Instagram-Theme-Pages** (Solo-Deal-Pages auf Instagram): **nicht gefunden**. Handles wie `techdeals.de` sind belegt, aber inaktiv. `amazonfundstuecke` auf TikTok hat 6 Follower, AmazonGlowUpDE 0.
  - **DE-Desk-Setup- oder Gadget-Theme-Page auf Deutsch:** nicht gefunden. Nur @cleandesksetup monetarisiert englischen Content mit amazon.de.
- **Einschränkung:** Die IG-Discovery war durch das Suchbudget und die Login-Wall begrenzt. Die Zahl kleiner DE-Pages (<10K) kann höher liegen.
- **Befund:** Die DE-Konkurrenz ist **auf Plattform-/Blog-Ebene professionell**, auf **Ebene der faceless Reels-Theme-Page aber dünn**.

### 5.3 Gibt es erfolgreiche KI-generierte Setup-, Gadget-, Car- oder Travel-Pages mit Affiliate?

- **Nur ein direkter Beleg:** @topdailysetups mit 3D-/CGI-Setups, 67K Followern und Amazon-Storefront.
- **KI-/3D-Kanäle mit großer Reichweite, aber ohne Affiliate:**
  - Bau Rausch: 621K, KI-DIY auf Deutsch.
  - Dreamy Interior: 315K, KI-Interior.
  - Home Graphix: 1,08 Mio., 3D-Raumdesign, monetarisiert über Eigenprodukt.
  - Ryzen4070: 3D-animierte PC-Memes, monetarisiert über Key-Referral.
- **Negativbeispiel:** Top Finds Daily mit KI-„Top-5 Amazon“-Listen hat 166K Abos, aber nur 1,6K Median-Views.
- **Fazit:** **Reichweite mit KI-Visuals ist belegt** (Interior/DIY bis 1 Mio.+). **KI plus Affiliate in Tech/Gear ist kaum belegt.** Das ist eine Chance (First Mover), aber auch ein Risiko: Vertrauen und Kaufintention bei synthetischen Produktbildern sind unbewiesen.

### 5.4 Dominante Content-Formate der Affiliate-Accounts

1. **Kuratierte Setup-Fotos/Reels plus „Link in bio for all products“.** Linktree führt zu Amazon-Storefront oder kit.co-Liste („Click and copy the look“). Beispiele: setuputic, thedreamsetup.
2. **Top-N-Listen/Collections:** „5 Best Ergonomic Keyboards“ (setupcreate), „6 Best Keyboards for Mac Users“ (isetups), „Top 15 Amazon Products“ (Justice Buys).
3. **Produkt-Demo-Clip mit „Get this … – Link in bio“:** dealify, Sathi Mart, Worldwide Gadgets, Nerviea23. Titel-CTA plus Link-Hub.
4. **Compilation „10 Things I Bought …“** (Justice Buys).
5. **Tipps/Hidden Features plus Zubehör-Codes** (TaylorOnWheels).
6. **Deals/Spartipps** (mydealz, MyTopDeals, Cool Material „Daily Steals“).
7. **Comment-to-DM:** z. B. IG-Post *„Desk Setup Prime Deals – Comment 'prime' and I'll DM you …“* (instagram.com/p/DL6ZxmVs3GG).
8. **Rabattcodes statt reiner Links:** Grovemade THEDREAMSETUP, Hansshow tayloronwheels, keysfan RYZEN50.

### 5.5 Hinweise auf Einnahmen

- **CLAIMED:** Keine konkreten Affiliate-Umsatzangaben gefunden. Justice Buys nennt Reichweiten („1M on TikTok, 1M on Instagram, 800k on Facebook“) und eine Management-Agentur, das spricht für ein Business-Level-Setup.
- **ESTIMATED (NexLev, nur YouTube-AdSense, kein Affiliate):**
  - Justice Buys: ≈ 191K USD kumuliert.
  - Malerart: ≈ 124K USD.
  - Worldwide Gadgets: ≈ 51K USD.
  - Bau Rausch: ≈ 39K USD.
- Amazon-Storefronts tragen den Plattformhinweis „Earns revenue … may earn commission“. Das belegt die Teilnahme, aber keine Höhe.
- **Datenlücke:** Verifizierte Affiliate-Einnahmen von Theme-Pages liegen nicht vor.

### 5.6 Kauft die Gaming-Audience teure oder eher günstige Produkte?

- **Setup-/Battlestation-Pages auf Instagram (ästhetik-orientiert):** verlinken **teure** Produkte. Beispiele: 49"-Curved-Monitor, Nanoleaf (killergamingsetups), Ergonofis-Tische, Grovemade (thedreamsetup), Keychron, MOFT (thesetuptoday).
- **Gaming-Shorts-Audience (jünger):** wird mit **Billigprodukten** monetarisiert.
  - Windows-Keys über Rabattcode (Ryzen4070/ryzentek).
  - „A Steam deck for 20 bucks???“ mit 16 Mio. Views und „$5 for a PlayStation Portal“ (R4 DECK, Eigenshop für Billig-Handhelds).
  - LED-Hexagons und Keycaps (cleanpcsetup).
  - DE-Beispiel @cleandesksetup: nur Produkte unter ca. 50 €.
- **Einordnung:** Hohe Klick-, aber niedrige Warenkorbwerte bei Gaming-Shorts. Premium-Warenkörbe entstehen eher bei „Desk-Setup/Productivity“-Ästhetik (erwachsene Home-Office-Zielgruppe). Das ist eine Tendenz aus Link-Inhalten, keine Conversion-Messung.

---

## 6. Auffällige Ineffizienzen und Opportunities

1. **Kit.co-Schließung (11.05.2026):** Große Setup-Pages verlinken weiter auf tote kit.co-Collections. Betroffen sind isetups (651K), thedreamsetup (374K) und setupcreate. Eine neue Page mit sauberem Storefront-/Collection-Setup trifft auf geschwächte Etablierte.
2. **Große Pages ohne Monetarisierung:** minimalsetups (291K), minimal.desksetups (206K, +67 % seit 2023), bestdreamsetup (180K) und setupwarriors (81K bei 125 Posts) zeigen keinen sichtbaren Affiliate-Link.
3. **Reichweite ohne Link in Shorts:**
   - Bacotes Detailing: 591K, Median 3,1 Mio.
   - ProViewGear: Top 108 Mio., Produkt-Demo ohne Link.
   - Everythingolf: Median 3,65 Mio. bei 27K Abos.
   - MC Print Lab: Median 8,2 Mio.
   - Alexan Strib: Camping, Top 310 Mio.
   - Lensevision: Foto, Median 1,6 Mio.
   - In Detailing, Golf, Camping, Foto und Cycling ist also Nachfrage nach Visuals da, aber kaum jemand verlinkt Produkte.
4. **Cross-Platform-Lücken:** isetups hat auf TikTok 379 Follower, thedreamsetup 0, topdailysetups 7, MyTopDeals 1,2K, Uncrate 150. Bei Malerart zeigt der TikTok-Bio-Link auf Twitch statt auf den Affiliate-Linktree.
5. **DE-Weißraum:** Keine deutschsprachige faceless Setup-, Gadget- oder Car-Care-Reels-Theme-Page mit relevanter Größe gefunden. Handles wie techdeals.de und amazonfundstuecke sind belegt, aber inaktiv. Die DE-Nachfrage ist durch mydealz (571,8K TikTok) und Malerart (amazon.de-Monetarisierung) belegt.
6. **Diversifizierte Programme schlagen Amazon:** Die erfolgreichsten Cases kombinieren Amazon mit Brand-Programmen (Refersion, ShareASale, UpPromote, Impact/Walmart, ShopMy) und Rabattcodes. Die Nischen Tesla und 3D-Druck haben hochpreisige Einzelprodukte.
7. **Sättigungssignal EN-Setups:** Mehrere große EN-Setup-Pages verlieren seit 2023 Follower (minimalsetups −13 %, killergamingsetups −16 %, thedreamsetup −8 %), andere wachsen (setuputic +30 %, minimal.desksetups +67 %). Der Markt ist reif; Differenzierung (z. B. Video/Reels statt Foto) wird nötig.

---

## 7. Datenlücken

- Instagram-Follower (nur ESTIMATED), Reel-Views und Median-Views (UNKNOWN) sowie Postingfrequenz auf Instagram (UNKNOWN). Grund: Login-Wall und blockierte Drittanbieter.
- Keine Engagement-Raten (HypeAuditor und Social Blade blockiert).
- Audio/Hi-Fi und Schmuck: keine Accounts gefunden. Running, Fotografie und Cycling: nur Media oder Accounts ohne Affiliate.
- DE-Instagram-Discovery unvollständig (Suchbudget). Kleine DE-Pages sind wahrscheinlich untererfasst.
- Affiliate-Status unklar bei mydealz (FAQ-Antwort per JS), Grailify, Sneaker News, Gear Junkie und Cool Material (Cloudflare/403).
- Amazon-Storefront-Prüfung nur für identische Handles. „nein“ bedeutet: nicht unter diesem Handle gefunden.
- Keine verifizierten Affiliate-Umsätze. NexLev-Werte sind nur AdSense-Schätzungen.

---

## 8. Quellenliste (Auswahl; vollständige Quelle je Zeile in der CSV, Spalte `quelle_url`)

**Listen & Discovery**
- geekyminded.com – „30 Instagram Sources For New Desk Setup Inspiration“ (06/2023): https://geekyminded.com/best-instagram-accounts-to-find-desk-setup-inspiration-and-new-ideas/
- Instagram-Profil-URLs (Snippet-Daten 09/2026), z. B. https://www.instagram.com/thedreamsetup/ , https://www.instagram.com/isetups/ , https://www.instagram.com/setuputic/ , https://www.instagram.com/killergamingsetups/ , https://www.instagram.com/topdailysetups/ , https://www.instagram.com/cleandesksetup/
- IG-Post (Comment-to-DM-Format): https://www.instagram.com/p/DL6ZxmVs3GG/
- NexLev MCP `search_shorts_niche_finder_channels` (Abfragen: Amazon-Gadgets, Desk/Gaming-Setup, Car Detailing, Tesla, EDC, Travel, Camping, Amazon Fundstücke DE, Watches, 3D-Druck, Beauty, Audio, Kamera, Golf)

**Affiliate-Nachweise (Linktree)**
- https://linktr.ee/thedreamsetup · https://linktr.ee/isetups · https://linktr.ee/setuputic · https://linktr.ee/killergamingsetups · https://linktr.ee/cleandesksetup · https://linktr.ee/cleanpcsetup · https://linktr.ee/setupcreate · https://linktr.ee/thesetuptoday · https://linktr.ee/chillsetup · https://linktr.ee/thesetupaddict
- https://linktr.ee/justice_buys · https://linktr.ee/dealify_01 · https://linktr.ee/sathimart · https://linktr.ee/worldwidegadgets01 · https://linktr.ee/tayloronwheels · https://linktr.ee/ryzen4070 · https://linktr.ee/the3dwizard · https://linktr.ee/printlair · https://linktr.ee/malerart · https://linktr.ee/mytopdeals · https://linktr.ee/mydealz · https://linktr.ee/techdeals.de · https://linktr.ee/AmazonGlowUpDE · https://linktr.ee/promobricks · https://linktr.ee/zusammengebaut · https://linktr.ee/golfgods · https://linktr.ee/gearpatrol · https://linktr.ee/coolmaterial · https://linktr.ee/urbanedc · https://linktr.ee/garagegymreviews · https://linktr.ee/vanlifediaries · https://linktr.ee/projectvanlife · https://linktr.ee/overlandbound · https://linktr.ee/doctorsofrunning · https://linktr.ee/bikeradar · https://linktr.ee/wornandwound · https://linktr.ee/teddybaldassarre · https://linktr.ee/carswithoutlimits · https://linktr.ee/gearjunkie

**Amazon-Storefronts (abgerufen, existent)**
- https://www.amazon.com/shop/thedreamsetup · /shop/setuputic · /shop/killergamingsetups · /shop/topdailysetups · /shop/chillsetup · /shop/setupcreate · /shop/thesetupaddict · /shop/tayloronwheels12 · /shop/everydaycarry · /shop/packhacker · /shop/uncrate · /shop/obsessedgarage · /shop/shair10

**Websites / Disclosures**
- https://www.justicebuys.com · https://www.promobricks.de/ · https://zusammengebaut.com/ · https://www.sneakerjagers.com/de · https://www.garagegymreviews.com/disclosure · https://www.packhacker.com/ · https://urbanedc.xyz/category/edcgoals/ · https://www.mydealz.de/faq · https://www.mytopdeals.net/ · https://kit.co/ (Schließungshinweis)

**TikTok-Profile (VERIFIED)**
- https://www.tiktok.com/@justicebuys · @worldwidegadgets01 · @mydealz.de · @mytopdeals · @amazonfindsde · @tayloronwheels · @everydaycarry · @garagegymreviews · @homegym · @mtbnews · @chrono24 · @sneakernews · @grailify · @sneakerjagers · @snkraddicted · @uncrate · @manofmany · @promobricks · @zusammengebaut · @the3dwizard · @printlair · @malerart · @ryzentek · @isetups · @topdailysetups · @thedreamsetup

**YouTube-About-Seiten (VERIFIED Abonnenten)**
- https://www.youtube.com/@justicebuys1 · @WorldwideGadgets01 · @dealify_01 · @Sathi_Mart · @topfndsdaily · @Xtrikeffliate · @HomeSprucely · @Smartcase-De · @Ryzen4070 · @R4DECKOFFICIAL · @tayloronwheels · @Bacotesmobiledetailing · @SpankinCleanDetailing · @everydaycarry · @packhacker · @ProViewGear · @Everythingolf1 · @GolfManiacs · @The_3DWizard · @PrintLair · @MCPrintLab · @moderngirlaesthetic · @Nervie23 · @skinfluence_11 · @Malerart · @BauRausch · @HomeGraphix · @DreamyInterior · @lensevision · @cgm.photos
