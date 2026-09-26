# M4 – AI Fashion, Beauty, Personas, Transformations, Product-Ads (Instagram)

Prüfdatum: 2026-09-26 · Betrachtungsfenster: ca. 28.05.–26.09.2026 · Rohdaten: `raw_accounts_M4.csv` (55 Accounts)

## 1. Kurzfazit

- **55 Instagram-Accounts** erfasst: 53 AI VERIFIED, 2 AI LIKELY. Belegt sind sie über Selbstbezeichnung in der Bio, Presse bzw. Rankings oder eine Reel-Analyse.
- **Junge, schnell wachsende Accounts (Klassen A–D) ließen sich auf Instagram kaum belegen.** Der Grund sind fehlende Daten, nicht fehlende Accounts: Instagram-Profile ließen sich weder per WebFetch (HTTP 429) noch über Social Blade oder HypeAuditor (HTTP 403) abrufen. Follower- und Postzahlen kleiner Accounts stammen deshalb fast nur aus Such-Snippets ohne Datum.
- Das **stärkste belegte Momentum im Cluster** zeigen AI-Personas mit ungewöhnlichem Konzept, nicht das Standardprofil „junge schöne KI-Frau“:
  - **@grannyspills** (KI-Oma, Luxus-Lifestyle): Start 07/2025, laut Presse „1 Mio. Follower in wenigen Wochen“, 1,9 Mio. (20.08.2026) → 2,2 Mio. (09/2026).
  - **@millasofiafin**: 479K (02/2026) → 675K (31.07.2026), danach flach.
- Legacy-Personas (Lil Miquela, Imma, Noonoouri, Shudu, Rozy, Kyra) wachsen 2026 **seitwärts bis rückläufig**. Das spricht für Sättigung im klassischen Virtual-Influencer-Segment.
- **Transformations und Restoration** („restoring abandoned …“, Car-, House- und Airplane-Restoration) sind plattformübergreifend der klarste Momentum-Treiber. Belegt ist das mit Zahlen **nur auf YouTube Shorts** (NexLev), wo es mehrere sehr junge Kanäle mit Shorts von 10 bis 127 Mio. Views gibt. Dazugehörige Instagram-Zwillinge ließen sich nicht verifizieren.
- **Affiliate-Links (LTK, ShopMy, Amazon, „outfit details“) sind in keinem einzigen Fall belegt.** Sichtbar sind nur andere Monetarisierungsformen: Fanvue-Abos, Brand Deals, B2B-Dienstleistungen (KI-Shootings, Hochzeitskonzepte), SaaS-Tools und Info-Produkte.

## 2. Methodik & Grenzen

**Vorgehen**

1. Websuche (25 von 25 Aufrufen verbraucht). Die Queries mit `site:instagram.com` lieferten Profil-Snippets mit Follower-Zahl und Bio-Text.
2. WebFetch auf öffentliche Rankings und Listen: aipulled, Favikon, yoloco, hypefy, bracai, kolsquare, creatorflow, invideo, nataliajohansson, getpassionfruit, topaichatgirls. Aus den Artikeldaten habe ich **datierte Snapshots** gebaut.
3. NexLev `watch_instagram_video_and_ask`: Reel-Analyse für DQWIAB3DEMb (varyalai) und DWasA13ADMN. Das Tageskontingent von 15 Aufrufen war danach für die ganze Session erschöpft, auch durch andere Agenten.
4. NexLev Shorts Niche Finder (`isAiChannel=true`, `firstUploadAfter`) und `youtube_channel_about`, um Momentum-Kanäle auf YouTube zu finden, die als Instagram-Zwilling in Frage kommen.

**Grenzen**

- **Kein direkter Profilabruf:** Instagram-Profile und Reel-Seiten waren nicht abrufbar. Ich habe keine Login-Sperre umgangen und keine Viewer- oder Downloader-Seiten genutzt. Einen Abruf mit geänderter User-Agent-Kennung hat das System abgelehnt, und ich habe ihn nicht weiter versucht.
- **Folgen für die Datenlage:**
  - Reel-Views, Median-Views und Top-5-Reels sind für alle 55 Accounts UNKNOWN.
  - Postzahl und Erstpost sind mit einer Ausnahme UNKNOWN.
  - Follower aus Such-Snippets haben ein **unbekanntes Indexdatum** (Datenqualität THIRD-PARTY OBSERVED).
- **Follower-Historie:** Die Zeitreihen stammen nur aus Artikelständen verschiedener Anbieter. Die Zahlen sind gerundet und teils widersprüchlich. Die Follower-Zahl von Lil Miquela reicht je nach Quelle von 2,25 bis 3,3 Mio. Werte wie „vor 30 Tagen“ sind deshalb nur als Snapshot mit ±7 Tagen Toleranz eingetragen, niemals interpoliert.
- **Label „AI-generated profile“:** Das Label gibt es seit 31.08.2026 (TechCrunch, 9to5Google, Engadget). Ob ein Account es trägt, ließ sich bei keinem prüfen, weil die Profile nicht geladen werden konnten. In der CSV steht dazu nichts. Laut Meta gilt: Profile ohne Label, die eine KI-Person zeigen, verlieren Reichweite bei Nicht-Followern (Explore, Reels-Tab). Davon wären Fashion-Persona-Accounts stark betroffen, Transformation- oder Objekt-Accounts ohne KI-Person dagegen nicht.

## 3. Befunde je Unter-Nische

### 3.1 AI-Personas / Virtual Influencer (28 Accounts)

| Account | Datierte Snapshots | Tendenz im 120-Tage-Fenster |
|---|---|---|
| @grannyspills | Start 07/2025; 1,9 Mio. (2026-08-20, kolsquare) → 2,2 Mio. (2026-09, creatorflow) | **stark steigend** (ca. +300K in ca. 1 Monat, Rundung beachten) |
| @millasofiafin | 232K (2025-05) → 479K (2026-02) → 675K (2026-07-31) → ~675K (2026-09) | starker Anstieg im 1. Halbjahr 2026, im Fenster flach |
| @naina_avtr | ~375K (2026-02) → 405K (2026-08-20) | moderat steigend |
| @fit_aitana | 391K (2026-05-11) → 402K (07-31) → 393K (08-20) → 404K (09/2026) | ca. +3 %, Quellenrauschen |
| @imma.gram / @noonoouri / @kyraonig / @rozy.gram / @shudu.gram | siehe CSV | seitwärts bis rückläufig |
| @daisy.nicholsxoxo | „100K Instagram Q1 2026“ (aipulled) | möglicher Kandidat für Klasse A, Startdatum unbekannt |
| @plustika, @thalasya_, @kenza.layli | aipulled: „New Wave (50K+ Q1-2026-Wachstum)“ | Wachstum nur als Kategorie belegt |
| @natt.alia2007 | Start 11/2025; 10.841 Follower (2026-09-20, eigene Angabe) | jung, aber langsam |

**Interpretation:** Das Persona-Segment ist gesättigt. Durchbrüche 2025/26 hatten ein **klares, ungewöhnliches Konzept**, etwa eine Oma, Satire über Luxus oder einen Kultur-Nischen-Bezug (Indien, MENA). Fanvue-Funnel-Accounts (Emily Pellegrini, Daisy Nichols) wachsen zwar, sind aber durch das neue Label und das Reichweitenlimit am stärksten gefährdet.

### 3.2 AI Fashion (Models, Runway, Outfit-Konzepte)

- **@varyalai (VARYA JAMYL), 266K:** KI-Shootings mit echter Kleidung und KI-Models. Das analysierte Reel zeigt einen KI-Runway-Walk mit Latexkleid in einer klassizistischen Halle. Der Hook ist rein visuell, es gibt weder AI-Label noch Shop-Link. Das Geschäftsmodell ist B2B (Shootings für Marken). Das ist der stärkste reine AI-Fashion-Content-Account im Fund.
- **@zwei_handvoll_fashion, 161K (deutschsprachig):** Virtuelle Fashion-Show für Curvy- und Plus-Size-Mode mit KI-Models. Das ist eine **interessante Unter-Nische** (Body-Diversity × AI), zum Wachstum gibt es keine Daten.
- Nachahmer mit geringer Reichweite: @ai_girls_lingerie (2.143), @who.is.she.official (3.594 Follower bei 842 Posts), @dressxagent (700).

### 3.3 AI Beauty (Makeup, Nails)

- **@itsolivia.ai:** Format „natural → glam makeup transition reveal“, von alici.ai als KI-Video katalogisiert. Zahlen waren nicht zugänglich.
- **AI Nail Art ist auf Instagram nicht skaliert.** @naildesign.ai hat 507 Follower. Die großen Nail-Pages (z. B. ideas_for_nailart mit 1 Mio.) sind nicht als KI belegt und deshalb nicht erfasst.

### 3.4 AI Transformations & Before/After (inkl. Restoration)

Auf Instagram belegt ist nur **@remodel.ai** (20K, eine Tool-Marke für Room-Makeover).

Das eigentliche Momentum zeigt sich **auf YouTube Shorts** (NexLev-Daten, abgerufen 2026-09-26). Diese Kanäle sind nicht in der CSV, weil ihre Instagram-Zwillinge nicht verifiziert sind:

| YT-Kanal | Start | Abos | Top-Shorts | Format |
|---|---|---|---|---|
| Bau Rausch (@BauRausch) | beigetreten 2025-07-13; laut NexLev erste Uploads ab 2026-04-13 | 621K, 53 Videos | 127 Mio. („DIY Floating Cabin“), 85 Mio., 56 Mio. | KI-Bau- und Renovierungs-Timelapse; Link „AI Timelapse Guide“ (Info-Produkt) |
| storycar.barnfind | beigetreten 2026-03-04, Uploads ab 2026-04-01 | 149K, 368 Videos, Median ca. 1 Mio. | 12 Mio. (Airplane Home), 8 Mio., 7,7 Mio. | Restoration/Barnfind, spanisch; Handle im Instagram-Stil |
| Soft sound Space | beigetreten 2026-07-22 | 32,3K | **28 Mio.** (Sports Car Restoring), 3,3 Mio. | KI-Car-Restoration → **Emerging Outlier** |
| x54m | Kanal von 2019, KI-Restoration seit 12/2025 | 37K | 11 Mio. (Honda RC51), 4,7 Mio. (Bugatti) | KI-Car-Restoration im ASMR-Stil |
| AI Forever (@ai_forever66) | Uploads ab 2025-12-21 | 82,4K, 21 Videos, Outlier-Score 5,7 | 22 Mio., 17 Mio., 13 Mio. | KI-„Celebrity Aging / Then & Now“-Transformation |

Solche Kanäle posten in der Praxis oft parallel auf Instagram, das ist hier aber **nicht verifiziert**. Die Unter-Nische eignet sich als Priorität für eine manuelle Nachprüfung in der Instagram-App.

### 3.5 AI Fitness / Body

Mehrere kleine Nachahmer: @siennavixen (8.039, „AI Fitness Model & Nutritionist“), @aiqueenoffitness (906), @ai_fitgirls (523), @fitnessgirls.ai (32), @ai_fitness_models (7). Ein Durchbruch ist nicht belegt. Das Segment ist gesättigt und überschneidet sich mit Fanvue-Funnels.

### 3.6 AI Weddings / Dresses

- @aisle_wedding.ai (31K, B2B-Konzepte für Planer), @aiweddingdesign (1.504), @bridelyapp (1.061, Try-on-App).
- „Pick a dress“-Formate existieren als Trend, etwa „Dress to Impress“-Outfit-Reveal oder Outfit-Wechsel im Beat (revid.ai, flowshorts). Einem konkreten jungen Instagram-Account ließen sie sich nicht zuordnen.

### 3.7 AI Product-Ads / UGC

Die Instagram-Präsenz besteht fast nur aus **Tool-Marken**: @createugc.ai (6.843), @magic.ugc (3.108), @adcrafty.ai (77), @storista.io (35, TikTok-Shop-Fokus). Dazu kommt eine Dienstleisterin, @aiugc.creator (279, Beauty/Skincare). AI-UGC ist ein B2B-Produktionsmarkt und keine Reichweiten-Nische.

### 3.8 Luxury-Concepts / „Choose your house“ / Kids & Toys

- Luxury-Concepts: @imagineyachts (876), @theaimansion (37).
- Kids & Toys nur als Kontext: @guggimon (1,3 Mio., CGI-Toy-Marke).
- **Formate vom Typ „Choose your house“ oder „Pick one“ ließen sich auf Instagram nicht mit Zahlen belegen.** Das ist eine Datenlücke, keine Aussage über den Markt.

## 4. Emerging Outliers

- **Instagram:** Kein Outlier belegbar, weil keine Reel-View-Zahlen zugänglich waren.
- **Plattformübergreifend (YouTube Shorts, Hinweis auf Instagram-Potenzial):**
  - **Soft sound Space:** 32K Abos, ein Short mit 28 Mio. Views, Kanal seit 22.07.2026.
  - **AI Forever:** 82K Abos, 21 Videos, Shorts mit 22, 17 und 13 Mio. Views.
  - **x54m:** 37K Abos, 11 Mio. Views.
  - **Bau Rausch:** 53 Videos, 387 Mio. Gesamtviews.
- **Instagram-Kandidaten zur Nachprüfung:**
  - @daisy.nicholsxoxo: 100K in Q1 2026
  - @plustika: 50K+ in Q1 2026
  - @varyalai: 266K bei B2B-Fokus

## 5. Formate & Hooks

1. **Restoration-Timelapse:** Ein verfallenes Objekt (Auto, Truck, Flugzeug, Haus, Container) wird zum Luxusobjekt. Der Hook ist der „Wreck“-Zustand in den ersten Sekunden, die Titel folgen dem Muster „Restoring …“, „Full part“. Diese Clips haben die höchsten View-Multiplikatoren im Cluster.
2. **Runway-Walk bzw. Hero-Shot eines KI-Models:** Rein visueller Hook mit glänzenden Materialien und klassizistischen Settings, ohne Text (varyalai).
3. **Makeup- oder Glow-up-Transition** („natural → glam“) mit KI-Persona (itsolivia.ai).
4. **Celebrity Aging / Then & Now** (AI Forever): Nostalgie als Hook, Titel im Muster „Same Actors, Different Ages“.
5. **Persona mit Haltung** (Granny Spills): Bissige Kommentare zu Luxus statt reiner Ästhetik.
6. **Outfit-Wechsel im Beat bzw. „Dress to Impress“-Reveal** als Trend-Template, von Tool-Anbietern beworben.

## 6. Copycats & Sättigung

- **Stark gesättigt:**
  - Weibliche KI-Fashion- und Fitness-Personas: viele Accounts mit unter 10K Followern und hoher Postfrequenz, etwa who.is.she.official mit 842 Posts bei 3,6K Followern.
  - Legacy-Personas: stagnierend.
- **Portfolio-Strategie:** Ein Operator betreibt mehrere Personas (Mia Zelu und Ana Zelu, beide aus dem Umfeld von The Clueless / ZELU House).
- **Tool-Marken kopieren das Format:** Anbieter wie revid.ai, hooked.so und pixpretty bieten Vorlagen für „Abandoned“- oder „Glow-up“-Generatoren an. Die Einstiegshürde sinkt, Copycats werden in der Restoration-Nische schnell folgen.
- **Regulatorischer Druck:** Das Label seit 31.08.2026 und Art. 50 EU AI Act (seit 02.08.2026) treffen vor allem Persona-Accounts ohne Offenlegung.

## 7. Sichtbare Monetarisierung (Fokus Affiliate)

| Typ | Belege |
|---|---|
| **Affiliate (LTK, ShopMy, Amazon, „outfit details“)** | **kein Beleg gefunden**. Nur creatorflow nennt „Affiliate“ allgemein für @fit_aitana, ohne Link-Details. Zuschauerfragen nach Produkten ließen sich nicht prüfen (Kommentare nicht zugänglich). |
| Abo/Adult-nah | Fanvue: @fit_aitana (Ambassador), @emilypellegrini, @daisy.nicholsxoxo („five figures monthly“, SELF-REPORTED) |
| Brand Deals | Legacy-Personas (Prada, Dior, IKEA, CaratLane-Schmuck bei @kyraonig); @grannyspills geschätzt 26.000–77.000 EUR pro Post (ESTIMATED) |
| B2B-Service | @varyalai (KI-Shootings), @aisle_wedding.ai, @aiugc.creator |
| SaaS/App | remodel.ai, bridelyapp, createugc.ai, magic.ugc, dressxagent |
| Info-Produkt | Bau Rausch (YouTube): „AI Timelapse Guide“; @natt.alia2007: Novelle für 4,99 USD |
| Eigenhandel | @magazineluiza, @casasbahia (Retail-Personas) |

**Einordnung:** Die „AI-Outfit → Affiliate-Link“-Strecke ist im Fund nicht nachweisbar. Ein plausibler Grund: KI-generierte Outfits existieren meist nicht als kaufbares Produkt. Ausnahme wären KI-Shootings mit echter Kleidung, wie varyalai sie macht. Das ist die Lücke, die sich für einen Affiliate-Ansatz als Hypothese testen ließe.

## 8. Datenlücken

- Reel-Views, Median, Top-5-Reels und Anzahl der 1M+-Reels fehlen für **alle** 55 Instagram-Accounts.
- Account-Alter und erster Post fehlen für die meisten Content-Pages, also auch die Einordnung in die Klassen A–D.
- Follower-Werte „vor 30/60/90/120 Tagen“ gibt es nur als Artikel-Snapshots und nur für 9 Personas.
- Das Label „AI-generated profile“ ist für keinen Account geprüft.
- Die Instagram-Zwillinge der YouTube-Restoration- und Transformation-Kanäle sind nicht verifiziert.
- Handle-Konflikte zwischen Quellen: milla_sofia/millasofiafin, mia_zelu/miazelu, ana_zelu/anazelu, emily_pellegrini/emilypellegrini, _imma.gram_/imma.gram, oh_rozy/rozy.gram.

**Empfehlung:** Manuelle Nachprüfung in der Instagram-App (eingeloggt, ohne Scraping) für varyalai, zwei_handvoll_fashion, daisy.nicholsxoxo, plustika und grannyspills. Dazu eine Suche nach Instagram-Pendants zu Bau Rausch, storycar.barnfind und Soft sound Space.

## 9. Quellen

- Label-Kontext:
  - https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/
  - https://9to5google.com/2026/08/31/instagram-ai-generated-influencers-label-update/
  - https://www.engadget.com/2246914/instagram-will-demote-ai-generated-influencers-if-they-dont-clearly-label-their-account/
  - https://creatorflow.so/blog/instagram-ai-generated-profile-label/
  - https://help.instagram.com/1555776438852001/
- Rankings und Snapshots:
  - https://aipulled.com/news/ai-instagram-influencers-q1-2026.html (Apr 2026)
  - https://www.favikon.com/blog/top-ai-influencers-instagram (Mai 2026)
  - https://yoloco.io/blog/top-ai-influencers-instagram (2025-05-30)
  - https://topaichatgirls.org/ai-fashion-models-worth-following/ (2026-06-13)
  - https://hypefy.ai/blog/top-ai-influencers-on-instagram (2026-07-31)
  - https://www.kolsquare.com/en/top-influencers/10-ai-influencers-transforming-social-media (2026-08-20)
  - https://creatorflow.so/blog/ai-influencers-instagram/ (09/2026)
  - https://nataliajohansson.com/2026/03/16/ai-fashion-influencers-instagram-2026/ (Refresh 09/2026)
  - https://www.bracai.eu/post/ai-influencer-instagram (Update 2026-02-06)
  - https://invideo.io/blog/ai-influencers-on-instagram/ (undatiert)
  - https://www.getpassionfruit.com/blog/top-ai-generated-influencers-virtual-models-marketing-virality-mia-zelu-lil-miquela (2026-09-25)
- Instagram-Profil-Snippets (Websuche 2026-09-26): die Profil-URLs der Content-Pages in der CSV, dazu https://www.instagram.com/varyalai/reel/DQWIAB3DEMb/
- Format-Kontext:
  - https://alici.ai/formulas/media/itsolivia-ai/a5181cb4-b5fd-525a-a3f5-4b2234d1c825-ai-influencer-makeup-transition-reveal-ai-video
  - https://www.vidmakerpro.com/blog/restoration-timelapse-viral-videos-ai
  - https://www.revid.ai/category/abandoned
  - https://www.revid.ai/tools/create-viral-dresstoimpress-outfit-reveal-video
  - https://lightreel.ai/blogs/whats-trending-on-instagram (09/2026; keine AI-Formate dokumentiert)
- YouTube Shorts (NexLev Shorts Niche Finder und youtube_channel_about, 2026-09-26):
  - youtube.com/@BauRausch
  - youtube.com/@storycar.barnfind
  - youtube.com/@SoftSoundSpace-l1c
  - youtube.com/@X54MQ
  - youtube.com/@ai_forever66
