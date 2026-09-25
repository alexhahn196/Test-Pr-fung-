# Q08 – Cross-Platform-Nachfragesignale: KI-Luxushäuser, KI-Interior, Dream House, Zukunftsarchitektur und Cozy Bedroom auf YouTube Shorts und TikTok als Proxy für Instagram Reels

**Stand:** 2026-09-25 · **Quellennotiz (Recherche-Rohmaterial, Deutsch; englische Zitate im Original)**
**Werkzeuge:** NexLev-MCP (YouTube-Datenbank und Echtzeit-YouTube-Abfragen), WebFetch auf direkt bekannte URLs. **WebSearch war nicht verfügbar:** Das Session-Budget war schon aufgebraucht (200/200), alle 4 Suchversuche wurden abgewiesen. Suchmaschinen habe ich nicht über WebFetch nachgebaut, um das Limit nicht zu umgehen.

**Status-Tags:** `[VERIFIED]` = in der Quelle selbst gesehen · `[ESTIMATED]` = eigene Ableitung oder Rechnung aus gesehenen Daten · `[THIRD-PARTY ESTIMATE]` = Schätzung oder Klassifikation eines Dritten (v. a. NexLev-Umsatz, Outlier-Score, KI-/Faceless-Flags) · `[UNKNOWN]` = nicht belegbar

---

## 1. Fragestellung

Welche **plattformübergreifenden Nachfragesignale** gibt es für Kurzvideos zu **KI-Luxushäusern, KI-Interior, „Dream House“, Zukunftsarchitektur und „Cozy Bedroom / Rain Ambience“** auf **YouTube Shorts** und **TikTok**? Lassen sie sich als **Proxy** dafür nutzen, was auf **Instagram Reels** funktioniert?

Im Einzelnen:
1. Welche YouTube-Kanäle und Shorts gibt es in diesen Nischen? Erfasst werden Abonnenten, Views, Upload-Frequenz, Faceless- und KI-Flags, Outlier-Scores, NexLev-Umsatzschätzung und Top-Themen.
2. In welchen Sub-Themen erzielen **viele kleine Kanäle überproportionale Views** (Outlier)?
3. Welche **TikTok-Evidenz** gibt es (virale KI-Haus-Videos, Medienberichte mit View-Zahlen)?
4. **Gegenevidenz:** Sättigung, abnehmende Reichweite, KI-Backlash, Monetarisierungs- und Policy-Risiken. Und wie gut lassen sich Shorts-Zahlen überhaupt auf Reels übertragen?

---

## 2. Methodik (kurz)

- **NexLev Shorts-Niche-Finder** (semantische Vektorsuche, `search_shorts_niche_finder_channels`). Meine 10 Abfragen: „AI generated luxury houses“, „dream house AI“, „luxury interior design shorts“, „future architecture AI futuristic buildings“, „cozy bedroom rain ambience“, „luxury villa tour“, „AI tiny house“, „mansion tour“, dazu zwei gefilterte Abfragen („AI generated house, interior design and architecture visuals“ mit `isAiChannel=true`, `maxSubscribers=150000`, sowie „cozy aesthetic room, rainy window, relaxing ambience visuals“). Ausgewertet habe ich außerdem die Rohdateien von **7 weiteren NexLev-Shorts-Abfragen**, die früher am selben Tag in dieser Recherche-Session liefen (z. B. „luxury villa and mansion house tour shorts“, „cozy rainy bedroom ambience AI video“, „luxury hotels resorts and unique stays“). Nach Deduplizierung ergibt das **224 Kanäle**. **60 davon habe ich als thematisch relevant in 6 Sub-Themen geclustert**, viele übrige Treffer sind semantisches Rauschen (v. a. Luxusautos).
- **NexLev Long-Form-Niche-Finder** (3 Abfragen mit RPM- und Monetarisierungsfeldern), **Faceless-Outlier-Feed** (5 semantische Abfragen, nur Shorts), **Viral-Small-Channels-Feed** (5 Titel-Keywords, letzte 90 Tage).
- **Echtzeit-YouTube über NexLev:** die jeweils 48 neuesten Shorts (bei Feels Like HOME 38) von 6 Kanälen (`youtube_channel_shorts`, sort=newest), 1 Kanal-About, 4 YouTube-Suchen (Shorts der letzten Woche bzw. des letzten Monats), 6 Monetarisierungs-Checks (einer scheiterte mit HTTP 429).
- **Wichtige Definitionen:**
  - **NexLev-„totalRevenueGenerated“ ist mechanisch totalViews × 0,0001 USD**, also eine pauschale RPM von 0,10 $. Nachgerechnet habe ich das an allen **224 von 224** Kanälen. `[VERIFIED Rechnung; Umsatz selbst = THIRD-PARTY ESTIMATE]` Der Wert ist also **keine** gemessene Auszahlung und sagt nichts darüber, ob ein Kanal überhaupt monetarisiert ist.
  - **Kanal-Outlier-Score** laut NexLev-Doku: *"How much a channel outperforms peers in its niche. 0 = average, >= 1 = above average, >= 2 = strong performer, >= 3 = exceptional."* **Video-Outlier-Score:** *"video views / channel average views"*. `[THIRD-PARTY ESTIMATE]`
  - **Upload-Frequenz:** NexLev liefert für Shorts-Kanäle keine Uploads pro Woche. Ich habe sie als *numOfUploads ÷ Wochen seit erstem Upload bis 25.09.2026* berechnet. `[ESTIMATED]` Das ist grob, denn die NexLev-Snapshots können älter sein.

---

## 3. Kernbefunde

### 3.1 Es gibt Nachfrage, aber sie ist stark hit-getrieben

- **Die Nachfrage nach „Haus/Interior als visuelles Spektakel“ auf YouTube Shorts ist groß.** Beispiele: Bau Rausch (@BauRausch) mit **621K Abos** und **386.860.826 Aufrufen** ([Kanal-About](https://www.youtube.com/@BauRausch)), Top-Short *"DIY Floating Cabin on Plastic Bottles | Time-Lapse [Concept AI]"* mit **127M Views** ([Short](https://www.youtube.com/shorts/BMlCqeKWe5Y)). Dreamy Interior mit **314K Abos**, Top-Short *"This Tiny Bedroom Transformation Is Genius"* mit **32M** ([Short](https://www.youtube.com/shorts/ABCQ2EDzW7U)). Home Graphix mit **1,08 Mio. Abos**, *"Designing 3m² Apartment in New York!"* mit **167M** ([Kanal](https://www.youtube.com/@HomeGraphix)). `[VERIFIED – YouTube/NexLev, 25.09.2026]`
- **Mittelwert und Median klaffen extrem auseinander:** Die Reichweite hängt an wenigen Einzel-Hits.
  - Goodluck Psd: Ø **1.213.375** Views pro Video, aber Median **910**. Getragen wird das von einem **64M**-Short (*"This Sitar-Shaped House Is Pure Art"*) ([Kanal](https://www.youtube.com/@GoodluckPsd_1)).
  - CreativeAIConcept: Ø 915.905, Median **14.000**.
  - Aura Frame: Ø 5.197.760, Median **65.000**.
  - Aesthetic Redesign: Ø 3.596.710, Median **51.500**.

  `[VERIFIED NexLev-Felder; Interpretation ESTIMATED]` **Für die Instagram-Planung heißt das:** Einzelne Reels können explodieren, der typische Post bleibt aber weit darunter.

### 3.2 Sub-Themen: Wo erzielen kleine Kanäle überproportionale Views?

Die 60 thematisch passenden Kanäle aus den Tabellen 1–2 habe ich in 6 Sub-Themen geclustert. Die Zuordnung ist meine eigene `[ESTIMATED]`.

- **A. KI-Konzept-Bau / Transformations-Timelapse** (Bunker, Tiny House, Baumhaus, „[Concept AI]“/„[KI-Konzept]“): **10 von 13** Kanälen hatten ihren ersten Upload **2026**, 8 von 13 tragen das KI-Flag. **7 von 13** Kanälen unter 100K Abos kommen auf Ø-Views ≥ 5× ihrer Abozahl (CreativeAIConcept, BuildFlow, Goodluck Psd, Dreamers Horizon, Jeremiah Carter, Sakura, LuxBuild Timelapse). Das ist das **stärkste Outlier-Cluster für junge, kleine Kanäle**, aber auch das **am schnellsten besetzte**. `[VERIFIED Rohdaten; Clusterung ESTIMATED]`
  - Ein deutscher Sonderfall ist **Bau Rausch**: Titel auf Deutsch mit „[KI-Konzept]“ und deutschen Orten (*"Ich habe einen geheimen Turm in Quedlinburg gekauft & DAS daraus gemacht 🤯"*, **56M**). Der Kanal wurde am **13.07.2025** angelegt, als Land ist **US** angegeben, und er verlinkt einen **„AI Timelapse Guide“** (vukovic.ink) mit dem Satz *"Want to create the same content I do? My Starter Guide is linked below"* ([About](https://www.youtube.com/@BauRausch)). Das Geschäftsmodell ist also **Kursverkauf**, nicht Werbeerlös. `[VERIFIED]`
- **B. Interior- und Raum-Makeover / Design-Explainer** (Small-Space, Kinderzimmer, Smart Furniture): größtes und am besten etabliertes Cluster. Die Mediane sind hoch (Median der Kanal-Mediane **564.500**). **6 von 18** Kanälen haben einen Outlier-Score ≥ 2, darunter Smart Design (**18,06**), Vinarch Group (**4,79**), Adam Smart Home (**3,37**, erster Upload **07.07.2026**, 16,7K Abos) und Rosedisfan1997 (**3,00**). Nur **5 von 18** tragen das KI-Flag. Die Top-Kanäle sind 3D-/Animations-Explainer ohne KI-Label. `[VERIFIED; THIRD-PARTY ESTIMATE für Outlier und Flags]`
- **C. Luxus-Epoxy / Material-Spektakel** (Epoxy-Böden, „Money vs Love Floor“, Resin-Treppen): sehr hohe Hit-Spitzen, zum Beispiel Structural.Aesthetics mit *"Stunning Epoxy River Stone Floor with Suspended Bed"* (**249M**), Aura Frame mit **101M**, Momentum Builds mit **74M** und The Bitter Trade mit **53M**. **5 von 7** tragen das KI-Flag. Die Mediane sind aber niedrig (Median der Kanal-Mediane **79.000**), die Hits sind also Einzelereignisse. `[VERIFIED]`
- **D. Dream-Bedroom / Cozy / Ambience:** Das Format **„Choose your dream bedroom“** (UnrealLife) hatte einmal **22M** ([Short](https://www.youtube.com/shorts/i5ot2RecvDw)), ist heute aber ausgereizt (siehe 3.4). **Sehr stark** läuft dagegen **Cozy + Regen + Familien-Story im Ghibli-Stil**: Feels Like HOME (462K Abos, erster Upload **19.06.2026**, Kanal-Median **2,15 Mio.**), *"🌧️ Stormy Village Life | Homemade Rasgulla & Family Love ❤️ #ghibli"* **59M** ([Short](https://www.youtube.com/shorts/NMy9_aIuKaQ)). Die reichweitenstärksten „Cozy Room“-Shorts sind aber **Produkt-Ads**: Galix-Sternenprojektor **183M** mit *"If you're afraid of the dark, you need this"* und CozeeBed **296M** mit *"get all products at cozeebed🔥 LINK IN BIO"*. `[VERIFIED]`
  - **Reine „Cozy Bedroom Rain Ambience“-Shorts haben auf YouTube kaum Angebot und kaum Views.** Eine Suche nach Shorts der letzten Woche ergab **15 Treffer mit 5 bis 791 Views** (geschätzt **2.272** Ergebnisse insgesamt). Keine NexLev-Abfrage fand einen dedizierten KI-Cozy-Rain-Shorts-Kanal mit relevanter Größe. `[VERIFIED Stichprobe]` Zum Vergleich hält q06 fest, dass Instagram-Cozy-Rain-Pages mit Millionen-Reels auf YouTube nur 1,13K bzw. 6,27K Abonnenten haben. **Cozy-Rain ist eher ein Instagram-natives als ein Shorts-Format.** `[ESTIMATED]`
- **E. Luxus-Lifestyle / Mansion (ohne KI):** „Mansion Tour“-Abfragen liefern überwiegend **Luxusauto- und „Aura/Millionaire“-Kanäle** (Ayehxncho Vault mit Outlier-Score **6,23**, *"My house is worth more than you"* **25M**). Echte Haus-Tour-Shorts-Kanäle sind in der NexLev-Shorts-DB kaum vertreten. Die **Nachfrage nach Luxus hängt an Geld- und Status-Narrativen**, weniger an Architektur. `[VERIFIED Treffer; Interpretation ESTIMATED]`
- **F. Surreale Orte / KI-Landschaften** („Places on earth that don't feel real“): **5 von 6** Kanälen sind 2026 gestartet, 4 von 6 liegen unter 100K Abos mit Ø-Views ≥ 5× Abos (z. B. Avena Earth: 85,1K Abos, Median **502.000**, Outlier **2,40**, erster Upload **03.07.2026**). Das ist ein benachbartes Format, das „Dream Destination“-Ästhetik bedient. `[VERIFIED; THIRD-PARTY ESTIMATE Outlier]`
- **Zukunftsarchitektur („future architecture AI“):** Die semantische Suche lieferte **keinen einzigen** dedizierten, großen Futur-Architektur-Shorts-Kanal. Treffer waren Bunker-, Bus- und Tiny-House-Konzepte (Cluster A). Die YouTube-Suche nach „futuristic house architecture AI“ (letzter Monat) brachte 24 Shorts mit **2 bis 1.600 Views**. **Das Sub-Thema „Zukunftsarchitektur“ zeigt auf YouTube Shorts derzeit kein eigenständiges Nachfragesignal.** `[VERIFIED Stichprobe; Schluss ESTIMATED]`

### 3.3 Faceless-Outlier- und Viral-Feeds: kaum aktuelle Interior-Outlier

- Der **kuratierte Faceless-Outlier-Feed** von NexLev (Einträge überwiegend Juli–Sept. 2026) lieferte bei 5 semantischen Abfragen (KI-Mansion/Interior-Tour, Cozy-Rain-Bedroom, Zukunftsarchitektur, Tiny-House-Timelapse, Luxus-Interior-Makeover) unter je 30 Treffern **keine On-Topic-Interior-Shorts**. Die Ähnlichkeit lag im Schnitt bei nur 0,60–0,64, die Treffer drehten sich um Autos, Gaming und Tech. Tangential passend waren nur *"Why THIS House Survived the Deadly Nepal Flood"* (Visual Cogs, **1.880** Abos, **718.425** Views, Outlier **23,43**, KI) und *"Humans built diff gng😭✌️"* (Hydro calm, 4.300 Abos, **10.186.588** Views, Outlier **71,30**). `[VERIFIED]` **Deutung:** Im aktuellen Outlier-Strom kommen Interior- und KI-Haus-Shorts nicht prominent vor. Ob das an der Feed-Abdeckung liegt, ist `[UNKNOWN]`.
- Der **Viral-Small-Channels-Feed** (letzte 90 Tage, überwiegend Long-Form) zeigt:
  - Titel-Keyword „interior“: **0** Treffer. „bedroom“: **4** Treffer, darunter ein 3-Std.-Regen-Piano-Video *"Peaceful Piano with Soft Rain – 3 Hours Calm Piano in the Warm Bedroom"* (1.790 Abos, **182.962** Views, KI).
  - „mansion“: 15 Treffer. Darunter **KI-Renovierung zu Luxus-Mansion** (SynthArq, 3.820 Abos: *"150 Year Old Abandoned Cargo Ship Turned Into a Luxury Mansion"* **298.973**; TitanCraft Builds, 9.520 Abos: **281.598**; Cirrus Land, 4.380 Abos: **202.545**) und **Luxus-Katastrophen-Narrative** (Luxury Alert, 9.960 Abos: *"Malibu's $40 Million Mansions Are Sliding Into the Ocean"* **436.292**).
  - „house“: u. a. *"AI Designed This House... And It's Weird"* (Design Intent, 5.650 Abos, **389.167**). **KI-skeptischer Content funktioniert ebenfalls.**

  `[VERIFIED]`

### 3.4 Gegenevidenz: Format-Verschleiß und Sättigung

Neueste Shorts im Vergleich zu früheren Hits. Echtzeit-Abruf am 25.09.2026, jeweils 48 bzw. 38 neueste Shorts:

- **Kou Yang** (KI-Renovierung, u. a. #adobefirefly; Top-Short **30M**): Die **48 neuesten Shorts liegen alle bei 1.000–16.000 Views**, Median **2.700**. NexLev weist dagegen einen Kanal-Median von **622.500** aus. **Das Format ist auf diesem Kanal kollabiert.** `[VERIFIED]`
- **UnrealLife** („Choose your dream bedroom“, Top **22M**): 48 neueste Shorts mit **6.600–76.000** Views, Median **26.000**. Kein einziger kam über 1M. Das **identische Titel-Template wurde 48× wiederholt**. `[VERIFIED]`
- **Dreamy Interior** (Top **32M**): Die 10 neuesten Shorts haben einen Median von **81.500** (4.600–157.000), über alle 48 neuesten liegt der Median bei **336.000**. Das Niveau ist deutlich gesunken, auch wenn einzelne Shorts noch Millionen holen. `[VERIFIED]`
- **Isla | Interior Designer** (App-Promo für „RenoMuse“): 10 neueste Shorts mit Median **38.500**. Der NexLev-Median liegt bei **585.000**, der Top-Short bei **5,5M**. `[VERIFIED]`
- **Stabil laufen:** **Bau Rausch** (10 neueste mit Median **1,2 Mio.**; 25 der 48 neuesten ≥ 1M) und **Feels Like HOME** (10 neueste mit Median **892.500**; 26 von 38 ≥ 1M). `[VERIFIED]` **Muster:** Stabil sind die Kanäle, die **Story und Überraschung** liefern (Bunker, Familie, Regen). Verschlissen sind **reine Vorher-Nachher- oder Template-Formate** ohne Narrativ. `[ESTIMATED]`
- **Die Angebotsflut ist messbar:** YouTube-Suchen nach Shorts der **letzten Woche**:
  - „AI dream house transformation“: **15 Treffer mit 8–2.200 Views** (geschätzt **52.894** Ergebnisse)
  - „AI luxury mansion tour“: **20 Treffer mit 0–1.400 Views** (geschätzt **122.885**)
  - „AI house transformation“ (letzter Monat): **14 Treffer mit 3–2.200 Views** (geschätzt **139.775**)

  `[VERIFIED Stichprobe; YouTube-Suchreihenfolge ist keine Zufallsstichprobe, und sehr neue Uploads sammeln noch Views]`
- **Long-Form spiegelt das:** Die NexLev-Suche „AI generated abandoned house renovation ASMR“ liefert viele **2026 gegründete KI-Kanäle mit Mini-Reichweite**: Shelter Revival (318 Abos), Ultimate Rebuild Studio (176 Abos, Median **177**), Prime Revival (956 Abos, **116 Videos**, Median **774,5**, ~6,75 Uploads/Woche). `[VERIFIED NexLev]`

### 3.5 Monetarisierung und Policy (Gegenevidenz)

- **Der YouTube-Policy-Text ist direkt einschlägig:** Seit **15.07.2025** heißt die Kategorie „repetitious content“ **„inauthentic content“**. Ausgeschlossen sind u. a. *"Image slideshows, templated storylines, or scrolling text with minimal or no narrative"* und *"AI-generated content made with generic or unoriginal templates giving the impression of mass production"*. Inhalte sollen *"not be mass-produced, generic, repetitive, or manipulative"* sein ([YouTube-Hilfe, Monetarisierungsrichtlinien](https://support.google.com/youtube/answer/1311392?hl=en)). `[VERIFIED]` Genau das Template-Muster aus 3.4 (z. B. 48× „Choose your dream bedroom“) fällt darunter.
- **Große KI-Interior-Kanäle sind laut NexLev nicht monetarisiert:** Bau Rausch **„Not monetized“** (386,9 Mio. Aufrufe), Feels Like HOME **„Not monetized“** (frischer Cache), Kou Yang und Aura Frame **„Not monetized“** (veralteter Cache, API-429). **Monetarisiert** ist dagegen Dreamy Interior (frischer Cache). `[VERIFIED NexLev-Status; Ursache UNKNOWN; Cache teils veraltet]` Die NexLev-„Umsätze“ dieser Kanäle (z. B. **38.641 $** bei Bau Rausch) sind deshalb **reine Rechengrößen** (Views × 0,10 $/1.000) und kein realer Werbeerlös. `[THIRD-PARTY ESTIMATE, faktisch widerlegt für nicht monetarisierte Kanäle]`
- **Auch die Long-Form-KI-Renovierung ist oft nicht monetarisiert** und hat eine niedrige RPM:
  - Wildcrafted Homes: 18,3K Abos, **14.507.121** Aufrufe, Outlier **19,4**, `isMonetizationEnabled=false`, RPM gesamt **1,66 $**
  - Wildwood Restore: `false`
  - Estate Revive: monetarisiert, **349,54 $/Monat**, RPM **1,91 $**
  - Zum Vergleich klassische **Luxus-Home-Tours**: Luxe List mit 144K Abos und **5.356,39 $/Monat** bei RPM **4,77 $**, Real Property Tours mit **2.066,67 $/Monat**
  - **Cozy-Rain-Sleep (Long-Form)** hat eine höhere RPM: Rainy Flower Dreams **8,22 $**, Wahyu Wild Rain **6,62 $**

  `[THIRD-PARTY ESTIMATE – NexLev]`
- **Pflicht zur KI-Kennzeichnung:**
  - YouTube (18.03.2024): Offenzulegen ist *"realistic content – content a viewer could easily mistake for a real person, place, scene, or event"*. Nicht nötig ist das für *"Animation or fantastical imagery"* ([YouTube Blog](https://blog.youtube/news-and-events/disclosing-ai-generated-content/)). `[VERIFIED]` Fotorealistische KI-Häuser und -Interiors dürften damit **kennzeichnungspflichtig** sein, stilisierte Ghibli-Szenen eher nicht. `[ESTIMATED]`
  - TikTok (19.09.2023): *"requires people to label AI-generated content that contains realistic images, audio or video"* und testet ein Auto-Label ([TikTok Newsroom](https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content)). `[VERIFIED]`
  - Bau Rausch kennzeichnet seine Titel freiwillig mit „[KI-Konzept]“ / „[Concept AI]“. `[VERIFIED]`
- **Die Kapwing-Studie zeigt die „AI slop“-Flut, aber ohne Interior-Bezug:** Unter den ersten 500 Shorts eines neuen Kontos waren **33 %** Brainrot und **21 %** KI-generiert (Daten Okt. 2025). **Interior-, Haus- oder Cozy-Inhalte werden nicht genannt** ([Kapwing](https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/)). `[VERIFIED]`
- **Frühe Präzedenz auf Facebook:** Die Seite „Dream Home“ (**113.000** Follower) zeigte *"AI generated homes that look like roosters, giraffes, horses, and hummingbirds"*. Die Macher saßen in Indien, Vietnam und auf den Philippinen, der Traffic kam *"mainly the US"* ([404 Media, 06.08.2024](https://www.404media.co/where-facebooks-ai-slop-comes-from/)). `[VERIFIED]` Das zeigt: **„KI-Traumhaus“ ist ein bekanntes Slop-Genre**, entsprechend hoch ist das Reputationsrisiko.

### 3.6 Taugt YouTube Shorts als Proxy für Reels? Nur mit starkem Abschlag

- **Socialinsider** (Varga und Cucu, **05.08.2026**; **69M** Shorts, Reels und TikToks, Jan. 2025–Juli 2026) misst durchschnittliche Views nach Follower-Klasse ([Socialinsider](https://www.socialinsider.io/blog/tiktok-vs-instagram-reels-vs-youtube-shorts/)). `[VERIFIED]`
  - **< 5K Follower:** TikTok **350**, Reels **625**, Shorts **15.160**
  - **10–50K:** TikTok **3.240**, Reels **2.745**, Shorts **23.200**
  - **100K–1M:** TikTok **34.900**, Reels **18.300**, Shorts **58.400**
  - Zitat: *"TikTok and Shorts both push content to non-followers by default"*, während *"Reels stays more dependent on your existing audience"*.
- **Abgeleiteter Abschlag Shorts→Reels:** Faktor **~24×** (< 5K), **~8,5×** (10–50K), **~3,2×** (100K–1M). `[ESTIMATED – eigene Division der Socialinsider-Mittelwerte]` **Shorts-Viewzahlen aus NexLev sind also nicht 1:1 als Reels-Erwartung zu lesen**, besonders nicht für einen neuen Account.
- **Engagement-Rate** (Socialinsider 2026): TikTok **2,60 %**, Reels **0,45 %**, Shorts **0,30 %**. `[VERIFIED]`

### 3.7 TikTok-Evidenz: weitgehend UNKNOWN

- **Konkrete View-Zahlen viraler KI-Haus-, Interior- oder Cozy-Videos auf TikTok konnte ich nicht belegen.** `[UNKNOWN]` Gründe: WebSearch-Budget erschöpft. TikTok-Discover- und Hashtag-Seiten (`/discover/ai-dream-house`, `/tag/aihouse`) liefern per WebFetch nur die Hülle *"TikTok - Make Your Day"*. Die TikTok-Support-Seite zu AIGC lieferte keinen Inhalt. Die geratenen Newsroom-URLs zu KI-Content-Controls (2025) führten auf fremde Seiten. Der Guardian ließ sich nicht abrufen.
- **Indirekte Hinweise auf TikTok-Herkunft oder -Kreuzung:**
  - Die Cozy-Room-Produktkanäle Galix (#projectorgalaxy, #cozyroom) und CozeeBed (*"LINK IN BIO"*) folgen dem Muster von TikTok-Shop-artigen Produkt-Ads. `[ESTIMATED]`
  - Der Wikipedia-Artikel „AI slop“ nennt TikTok-Viralität nur für andere Genres (z. B. *"Fruit Love Island … became one of the fastest-growing accounts in the United States"*, März 2026), **nicht für Häuser oder Interiors** ([Wikipedia](https://en.wikipedia.org/wiki/AI_slop)). `[VERIFIED]`
  - q06 dokumentiert das WDIV-Beispiel (KI-geschöntes Inseratsfoto mit *"millions of views"*). Die genaue Plattform ist dort nicht eindeutig.

### 3.8 Sichtbare Geschäftsmodelle hinter den Reichweiten (relevant für Instagram)

- **Kurs- und Guide-Verkauf:** Bau Rausch verlinkt einen „AI Timelapse Guide“. `[VERIFIED]`
- **App-Marketing als Content:** „Isla | Interior Designer“ (50,9K Abos, **64.293.231** Views) macht faktisch Werbung für die App **RenoMuse**. Die Kanalbeschreibung sagt *"Since y'all keep asking what app I use 😅 👉🏻 search RenoMuse in the App Store"*, fast alle Titel nennen die App. Das Format *"my landlord said NO to changes... so I showed him AI 😈"* kam auf **2,9M**. `[VERIFIED]` **KI-Interior-Tools bezahlen oder betreiben offenbar solche Kanäle.** Ob Isla gesponsert wird oder der App-Anbieter den Kanal selbst betreibt, ist `[UNKNOWN]`.
- **E-Commerce:** CozeeBed (**296M**-Short, *"get all products at cozeebed"*), Galix (**183M**), MistleCast (Raumprojektor, *"A must-have for book readers"*, **5,6M**). **Das stärkste kommerzielle „Cozy Bedroom“-Signal ist produktgetrieben, nicht KI-getrieben.** `[VERIFIED]`

---

## 4. Zahlen-Tabellen

### Tabelle 1 – Sub-Themen-Cluster (NexLev-Shorts-DB, Snapshot 25.09.2026)

| Cluster | n | Median Abos | Median Ø-Views/Video | Median der Kanal-Mediane | Outlier ≥ 2 | KI-Flag | Erster Upload 2026 | Kleine Kanäle (< 100K) mit Ø-Views ≥ 5× Abos | Status |
|---|---|---|---|---|---|---|---|---|---|
| A KI-Konzept-Bau/Transformation | 13 | 99.900 | 1.263.046 | 245.500 | 3/13 | 8/13 | 10/13 | 7 | VERIFIED Rohdaten; Cluster ESTIMATED |
| B Interior-Makeover/Design-Explainer | 18 | 105.550 | 949.849 | 564.500 | 6/18 | 5/18 | 6/18 | 7 | dito |
| C Luxus-Epoxy/Material-Spektakel | 7 | 111.000 | 3.596.710 | 79.000 | 1/7 | 5/7 | 4/7 | 3 | dito |
| D Dream-Bedroom/Cozy/Ambience | 11 | 51.000 | 524.935 | 103.500 | 4/11 | 5/11 | 4/11 | 4 | dito |
| E Luxus-Lifestyle/Mansion (nicht-KI) | 5 | 80.300 | 592.250 | 944.000 | 1/5 | 0/5 | 3/5 | 2 | dito |
| F Surreale Orte/KI-Landschaften | 6 | 80.900 | 890.990 | 347.750 | 2/6 | 3/6 | 5/6 | 4 | dito |

### Tabelle 2 – Kanäle (Auswahl der relevanten; NexLev-Snapshot, Upload-Frequenz ESTIMATED, Umsatz THIRD-PARTY ESTIMATE = Views × 0,10 $/1.000)

| Kanal (Handle) | Cluster | Abos | Ø Views/Video | Median Views | Uploads (≈/Woche) | Outlier | KI / Faceless | NexLev-„Umsatz“ | Top-Short (Views) | Erster Upload |
|---|---|---|---|---|---|---|---|---|---|---|
| Bau Rausch (@BauRausch) | A | 620.000 | 7.290.796 | 1.200.000 | 53 (~2,2) | 0,77 | KI / ja | 38.641 $ | DIY Floating Cabin on Plastic Bottles [Concept AI] (127M) | 2026-04-13 |
| CreativeAIConcept (@CreativeAIConcept) | A | 40.900 | 915.905 | 14.000 | 30 (~0,9) | 0,17 | KI / ja | 2.748 $ | Turning a Rusted School Bus into a DREAM Home! (12M) | 2026-01-28 |
| BuildFlow (@BuildFlow-11) | A | 83.000 | 1.263.046 | 31.000 | 46 (~1,6) | 0,15 | KI / ja | 5.810 $ | Turning a giant strawberry into a tiny house (24M) | 2026-03-05 |
| Goodluck Psd (@GoodluckPsd_1) | A | 25.500 | 1.213.375 | 910 | 54 (~1,5) | 0,01 | KI / ja | 6.552 $ | This Sitar-Shaped House Is Pure Art (64M) | 2026-01-18 |
| Dreamers Horizon (@DreamersHorizon-d7d) | A | 17.000 | 176.320 | 355.500 | 254 (~3,8) | 4,44 | KI / ja | 4.479 $ | The Ultimate Double-Decker Dream Bus (13M) | 2025-06-17 |
| Jeremiah Carter (@JeremiahCarter-u3q5n) | A | 99.900 | 695.577 | 425.000 | 109 (~2,1) | 2,04 | KI / ja | 7.582 $ | #BackyardMakeover … (19M) | 2025-09-19 |
| Calm Creations (@CalmCreations15) | A | 319.000 | 6.194.198 | 541.000 | 51 (~1,5) | 0,66 | nein / ja | 31.590 $ | I Built a Secret Room Under My Swimming Pool (181M) | 2026-01-31 |
| Kai C. Films (@Kaicfilms) | A | 550.000 | 6.031.904 | 288.000 | 19 (~0,6) | 0,19 | nein* / ja | 11.461 $ | Overgrown Yard Transformation (62M); „(AI story)“ im Titel (18M) | 2026-02-27 |
| Buildenza (@buildenza) | A | 133.000 | 2.673.132 | 245.500 | 38 (~1,5) | 0,56 | nein / ja | 10.158 $ | Buried a Root Cellar Underground… (19M) | 2026-03-27 |
| Mr ZoFy (@MrZoFy) | A (Miniatur) | 2.250.000 | 24.193.216 | 4.000.000 | 64 (~0,8) | 2,58 | nein / ja | 154.837 $ | Built a Stunning House on 7 Pillars (437M) | 2025-03-24 |
| Sakura (@SakuraBuilds) | A | 55.100 | 562.158 | 31.000 | 59 (~2,9) | 0,15 | nein / ja | 3.317 $ | Family Living Under a Tarp Gets a Beautiful Tiny Home (15M) | 2026-05-06 |
| Isla \| Interior Designer (@IslaInteriorDesigner) | B | 50.900 | 275.937 | 585.000 | 233 (~9,4) | 2,80 | KI / ja | 6.429 $ | Used RenoMuse app and turned my room into Blanket Fort (5,5M) | 2026-04-05 |
| Kou Yang (@KouYangAI) | B | 72.100 | 553.448 | 622.500 | 278 (~3,5) | 2,98 | KI / ja | 15.386 $ | Backyard Glow Up From Abandoned (30M) | 2025-03-25 |
| Dreamy Interior (@DreamyInterior) | B | 313.000 | 1.753.959 | 579.500 | 88 (~3,2) | 0,70 | KI / ja | 15.435 $ | This Tiny Bedroom Transformation Is Genius (32M) | 2026-03-18 |
| Home Graphix (@HomeGraphix) | B | 1.080.000 | 6.606.903 | 1.077.500 | 48 (~0,6) | 0,70 | nein / ja | 31.713 $ | Designing 3m² Apartment in New York! (167M) | 2025-02-21 |
| Smart Design (@SmartDesign365) | B | 2.130.000 | 15.777.204 | 28.000.000 | 277 (~3,1) | 18,06 | nein / ja | 437.029 $ | Multifunctional folding table design (911M) | 2025-01-09 |
| Vinarch Group Official (@VinarchGroupOfficial) | B | 172.000 | 12.582.872 | 2.100.000 | 17 (~0,1) | 4,79 | nein / ja | 21.391 $ | How to make your home secure (76M) | 2023-12-22 |
| Rosedisfan1997 (@Rosedisfan1997) | B | 86.800 | 869.506 | 626.000 | 159 (~3,7) | 3,00 | nein / ja | 13.825 $ | 30. Smart furniture ideas (28M) | 2025-11-25 |
| Adam Smart Home (@AdamSmartHome22) | B | 16.700 | 395.694 | 269.500 | 61 (~5,3) | 3,37 | KI / ja | 2.414 $ | Smart home ideas (3,5M) | 2026-07-07 |
| ArchitectAdamFan (@ArchitectAdamFan) | B | 133.000 | 1.135.669 | 166.500 | 101 (~2,4) | 0,38 | nein / ja | 11.470 $ | EP27. Affordable Interior Design Ideas For You (67M) | 2025-12-01 |
| Deck Haven (@Deck_Haven) | B | 39.900 | 137.681 | 41.500 | 163 (~4,4) | 0,52 | nein / ja | 2.244 $ | Three Kids. One Tiny Room. Endless Storage (6,6M) | 2026-01-08 |
| Katz Handy (@KatzHandy) | B | 95.100 | 1.030.192 | 50.500 | 125 (~2,5) | 0,24 | nein / ja | 12.877 $ | You will fall in love with these incredible designs (104M) | 2025-10-10 |
| Aura Frame (@AuraaFrame) | C | 196.000 | 5.197.760 | 65.000 | 31 (~1,1) | 0,15 | KI / ja | 16.113 $ | THIS SPLIT FLOOR IS AMAZING! Luxury Epoxy (101M) | 2026-03-12 |
| Structural.Aesthetics (@Structural.Aesthetics) | C | 387.000 | 7.089.115 | 4.049.999 | 89 (~1,2) | 4,90 | nein / ja | 63.093 $ | Stunning Epoxy River Stone Floor with Suspended Bed (249M) | 2025-04-15 |
| Momentum Builds (@Momentum.Builds) | C | 154.000 | 1.539.765 | 136.000 | 88 (~2,1) | 0,31 | KI / ja | 13.550 $ | Stunning Epoxy Aquarium Bedroom Floor (74M) | 2025-12-08 |
| The Bitter Trade (@TheBitterTrade) | C | 87.500 | 937.843 | 79.000 | 81 (~2,5) | 0,38 | KI / ja | 7.597 $ | THIS FLOOR IS MESMERIZING Luxury Epoxy Floor (53M) | 2026-02-07 |
| Aesthetic Redesign (@Aesthetic_Redesign) | C | 45.200 | 3.596.710 | 51.500 | 18 (~0,5) | 0,64 | KI / ja | 6.474 $ | Epoxy Resin stairs design (50M) | 2025-12-25 |
| Epic Epoxy Builds (@Epic_Epoxy_Builds) | C | 111.000 | 5.830.217 | 704.000 | 15 (~0,5) | 1,61 | nein / ja | 8.745 $ | Money vs Love Floor (49M) | 2026-03-17 |
| UnrealLife (@UnrealLife1) | D | 95.300 | 224.764 | 103.500 | 153 (~1,4) | 0,50 | KI / ja | 3.439 $ | Choose your dream bedroom (22M) | 2024-08-17 |
| LIAM-EDITZ (@LIAM-EDITZ-99) | D | 34.700 | 560.436 | 84.000 | 112 (~3,7) | 1,05 | KI / ja | 6.277 $ | #aesthetic (A-frame house) (18M) | 2026-02-24 |
| Feels Like HOME (@FeelsLike_Home) | D | 462.000 | 6.399.173 | 2.150.000 | 39 (~2,8) | 2,24 | KI / ja | 24.957 $ | Stormy Village Life … #ghibli (58–59M) | 2026-06-19 |
| Ghibli_trip (@Ghibli_trip) | D | 34.100 | 437.029 | 41.000 | 49 (~1,4) | 0,51 | KI / ja | 2.141 $ | Mango Shrikhand & Puri, Ghibli Cozy Cooking (7M) | 2026-01-24 |
| Liminal Backrooms (@TheLiminalBackroom) | D | 33.800 | 524.935 | 353.500 | 159 (~3,6) | 4,42 | nein / ja | 8.346 $ | It kept getting brighter #nostalgia (15M) | 2025-11-22 |
| Galix (@Thegalix) | D (Produkt) | 226.000 | 2.511.453 | 1.600.000 | 209 (~12,6) | 2,30 | nein / ja | 52.489 $ | If you're afraid of the dark, you need this (183M) | 2026-06-01 |
| CozeeBed (@CozeeBed) | D (Produkt) | 309.000 | 9.890.928 | 669.000 | 57 (~0,7) | 0,81 | nein / ja | 56.378 $ | get all products at cozeebed LINK IN BIO (296M) | 2025-02-09 |
| Ayehxncho Vault (@ayehxncho_vault) | E | 80.300 | 839.354 | 1.300.000 | 303 (~4,9) | 6,23 | nein / ja | 25.432 $ | My house is worth more than you (25M) | 2025-07-17 |
| Dynasty Focus (@dynastyFocus) | E | 23.500 | 117.100 | 148.000 | 376 (~21,6) | 1,85 | nein / ja | 4.403 $ | POV: … your mansion has its own beach (3M) | 2026-05-26 |
| Avena Earth (@AvenaEarth) | F | 85.100 | 766.733 | 502.000 | 114 (~9,5) | 2,40 | KI / ja | 8.741 $ | Which place did you like the most 1 or 2 or 3? (19M) | 2026-07-03 |
| Elvora Vibe (@ElvoraVibe) | F | 63.900 | 2.382.133 | 245.000 | 31 (~2,7) | 1,17 | nein / ja | 7.385 $ | Places on earth that don't feel real (18M) | 2026-07-08 |
| Mythic Elite (@MythicEliteMoney) | F | 174.000 | 2.084.632 | 898.500 | 108 (~4,0) | 2,05 | nein / ja | 22.514 $ | #travel #beautiful … (128M) | 2026-03-18 |

\*Kai C. Films: Laut NexLev kein KI-Flag, ein Top-Titel lautet aber *"From a tent in the forest to a real home. 🛠️(AI story)"*. Die Klassifikation ist inkonsistent `[UNKNOWN]`.

### Tabelle 3 – Format-Verschleiß: neueste Shorts im Vergleich zu früheren Hits (Echtzeit-YouTube via NexLev, 25.09.2026)

| Kanal | Top-Short (NexLev) | NexLev-Median | Median der 10 neuesten | Spanne 10 neueste | Median aller gelisteten (n) | Neueste ≥ 1M | Status |
|---|---|---|---|---|---|---|---|
| Kou Yang | 30M | 622.500 | 3.150 | 1.200–16.000 | 2.700 (48) | 0/48 | VERIFIED |
| UnrealLife | 22M | 103.500 | 21.000 | 9.500–74.000 | 26.000 (48) | 0/48 | VERIFIED |
| Isla \| Interior Designer | 5,5M | 585.000 | 38.500 | 17.000–201.000 | 108.500 (48) | 0/48 | VERIFIED |
| Dreamy Interior | 32M | 579.500 | 81.500 | 4.600–157.000 | 336.000 (48) | 9/48 | VERIFIED |
| Bau Rausch | 127M | 1.200.000 | 1.200.000 | 99.000–14.000.000 | 1.000.000 (48) | 25/48 | VERIFIED |
| Feels Like HOME | 59M | 2.150.000 | 892.500 | 298.000–26.000.000 | 2.150.000 (38) | 26/38 | VERIFIED |

(Mediane selbst aus den View-Texten „1.2M“, „30K“ usw. berechnet. Die Rundung von YouTube bleibt dabei erhalten. `[ESTIMATED Rechnung]`)

### Tabelle 4 – Angebot vs. Nachfrage: YouTube-Suchstichproben (Shorts)

| Suchbegriff | Zeitraum | Geschätzte Ergebnisse | Treffer | View-Spanne der Treffer | Status |
|---|---|---|---|---|---|
| AI dream house transformation | letzte Woche | 52.894 | 15 | 8–2.200 | VERIFIED |
| AI luxury mansion tour | letzte Woche | 122.885 | 20 | 0 („No views“)–1.400 | VERIFIED |
| cozy bedroom rain ambience | letzte Woche | 2.272 | 15 | 5–791 | VERIFIED |
| futuristic house architecture AI | letzter Monat | 150.129 | 24 | 2–1.600 | VERIFIED |
| AI house transformation | letzter Monat | 139.775 | 14 | 3–2.200 | VERIFIED |

### Tabelle 5 – Plattform-Benchmark als Proxy-Korrektur (Socialinsider, 05.08.2026; 69M Videos)

| Follower-Klasse | TikTok Ø Views | Reels Ø Views | Shorts Ø Views | Faktor Shorts/Reels (ESTIMATED) |
|---|---|---|---|---|
| < 5K | 350 | 625 | 15.160 | ~24,3× |
| 5–10K | 945 | 1.182 | 22.000 | ~18,6× |
| 10–50K | 3.240 | 2.745 | 23.200 | ~8,5× |
| 50–100K | 9.900 | 6.000 | 28.400 | ~4,7× |
| 100K–1M | 34.900 | 18.300 | 58.400 | ~3,2× |
| Engagement-Rate 2026 | 2,60 % | 0,45 % | 0,30 % | – |

### Tabelle 6 – Monetarisierung und RPM (NexLev)

| Kanal | Format | Monetarisiert? | NexLev-Monatsumsatz | RPM gesamt | Quelle/Status |
|---|---|---|---|---|---|
| Bau Rausch | KI-Bau-Shorts | Not monetized (veralteter Cache, HTTP 429) | – | – | NexLev, VERIFIED Status / Ursache UNKNOWN |
| Feels Like HOME | KI-Cozy-Ghibli-Shorts | Not monetized (frischer Cache) | – | – | dito |
| Kou Yang | KI-Renovierungs-Shorts | Not monetized (veralteter Cache) | – | – | dito |
| Aura Frame | KI-Epoxy-Shorts | Not monetized (veralteter Cache) | – | – | dito |
| Dreamy Interior | Interior-Explainer-Shorts | Monetized (frischer Cache) | – | – | dito |
| Wildcrafted Homes | KI-Renovierung Long-Form | false | 0 $ | 1,66 $ | THIRD-PARTY ESTIMATE |
| Estate Revive | KI-Renovierung Long-Form | true | 349,54 $ | 1,91 $ | THIRD-PARTY ESTIMATE |
| Luxe List | Luxus-Home-Tours Long-Form | true | 5.356,39 $ | 4,77 $ | THIRD-PARTY ESTIMATE |
| Real Property Tours | Luxus-Home-Tours Long-Form | true | 2.066,67 $ | 4,62 $ | THIRD-PARTY ESTIMATE |
| Rainy Flower Dreams | KI-Regen-Ambience Long-Form | true | 148,34 $ | 8,22 $ | THIRD-PARTY ESTIMATE |
| Wahyu Wild Rain | Regen-Ambience Long-Form | true | 364,79 $ | 6,62 $ | THIRD-PARTY ESTIMATE |

---

## 5. Widersprüche und Unsicherheiten

1. **Proxy-Validität:** YouTube Shorts verteilt Inhalte standardmäßig an Nicht-Follower, Reels stärker an die bestehende Audience (Socialinsider). Die Shorts-Views liegen je nach Follower-Klasse **3–24× über** den Reels-Views. Die hier gezeigten Hit-Zahlen (10M–400M) sind deshalb **kein** Maßstab für Reels. Übertragbar ist eher die **relative Themen-Rangfolge**, und selbst die nur mit Vorsicht. `[ESTIMATED]`
2. **Keine TikTok-Primärdaten:** Alle TikTok-Aussagen zur Nachfrage sind `[UNKNOWN]` (Suchbudget erschöpft, TikTok-Seiten JS-gerendert). Verifiziert ist nur TikToks Kennzeichnungsregel von 2023. Den TikTok-Anteil an der Cross-Platform-Frage kann diese Notiz nicht beantworten.
3. **NexLev-Datenqualität:**
   - „Umsatz“ ist pauschal Views × 0,10 $/1.000 (224/224 Kanäle). Mehrere dieser Kanäle sind laut NexLev selbst **nicht monetarisiert**.
   - KI- und Faceless-Flags sind uneinheitlich (Kai C. Films, Calm Creations und Buildenza ohne KI-Flag trotz KI-typischer Formate; „Evergreen Rain Relax“ mit Ø 58 Views, aber Median 56.000).
   - Outlier-Scores widersprechen teils der Intuition: Goodluck Psd mit 64M-Hit hat Score 0,01, weil der Kanal-Median bei 910 liegt.
   - Die Snapshot-Zeitpunkte der Kanal-Stats sind unbekannt (`createdAt` der DB-Einträge reicht von 2026-02 bis 2026-07).
4. **Semantische Suche ist verrauscht:** „mansion tour“ und „luxury villa tour“ lieferten überwiegend Luxusauto- und „Aura“-Kanäle. Ob echte Villa-Tour-Shorts-Kanäle fehlen oder nur nicht erfasst sind, ist `[UNKNOWN]`.
5. **Kausalität des Verschleißes:** Dass bei Kou Yang und UnrealLife die neuen Shorts einbrechen, kann an Format-Ermüdung, an einer Algorithmus-Einstufung als „inauthentic“, an Kanal-Strafen oder an sinkender Posting-Qualität liegen. Die Ursache ist `[UNKNOWN]`. Zu beachten ist auch, dass die „newest“-Sortierung neueste Uploads zeigt, die noch Views sammeln. Bei Kou Yang reicht das aber als Erklärung nicht, denn alle 48 liegen unter 16K.
6. **Positiv und negativ zugleich:** Cluster A (KI-Konzept-Bau) zeigt die meisten kleinen Outlier-Kanäle, **und** die meisten Neugründungen 2026 sowie massenhaft Shorts mit zweistelligen Views (Tabelle 4). Das spricht für ein **Lotterie-Profil**: hohe Varianz, niedriger Erwartungswert pro Post. `[ESTIMATED]`
7. **Cozy-Rain:** Auf YouTube Shorts ist das Signal schwach (Tabelle 4). Auf Instagram ist es laut q06 stark (Einzel-Reels mit dreistelligen Millionen-Views). **Die beiden Plattformen widersprechen sich hier.** Shorts eignen sich für dieses Sub-Thema **nicht** als Proxy.
8. **Monetarisierungs-Checks** beruhen teils auf veraltetem Cache (HTTP 429). Einen erneuten Abruf habe ich wegen des Rate-Limits bewusst nicht versucht.

---

## 6. Quellenliste

| # | URL | Titel | Datum | Quellentyp |
|---|---|---|---|---|
| 1 | NexLev MCP `search_shorts_niche_finder_channels` (10 eigene Abfragen + 7 Rohdateien früherer Abfragen derselben Session) | NexLev Shorts Niche Finder – Kanal-Snapshots (224 Kanäle) | Abruf 2026-09-25 | analytics_platform |
| 2 | NexLev MCP `search_niche_finder_channels` (3 Abfragen) | NexLev Long-Form Niche Finder (RPM, Monetarisierung) | Abruf 2026-09-25 | analytics_platform |
| 3 | NexLev MCP `faceless_outliers_videos` (5 Abfragen, Shorts) | NexLev Faceless-Outlier-Feed | Abruf 2026-09-25 | analytics_platform |
| 4 | NexLev MCP `search_viral_videos_small_channels` („house“, „bedroom“, „mansion“, „villa“, „interior“) | NexLev Viral-Small-Channels-Feed (90 Tage) | Abruf 2026-09-25 | analytics_platform |
| 5 | NexLev MCP `check_channel_monetization` (6 Checks) | Monetarisierungsstatus | Abruf 2026-09-25 | analytics_platform |
| 6 | https://www.youtube.com/@BauRausch | Bau Rausch – Kanal-About und neueste Shorts (via NexLev) | Abruf 2026-09-25 | other (YouTube-Metadaten) |
| 7 | https://www.youtube.com/@DreamyInterior | Dreamy Interior – neueste Shorts | Abruf 2026-09-25 | other (YouTube-Metadaten) |
| 8 | https://www.youtube.com/@UnrealLife1 | UnrealLife – neueste Shorts | Abruf 2026-09-25 | other |
| 9 | https://www.youtube.com/@KouYangAI | Kou Yang – neueste Shorts | Abruf 2026-09-25 | other |
| 10 | https://www.youtube.com/@FeelsLike_Home | Feels Like HOME – neueste Shorts | Abruf 2026-09-25 | other |
| 11 | https://www.youtube.com/@IslaInteriorDesigner | Isla \| Interior Designer – neueste Shorts und Kanalbeschreibung (RenoMuse) | Abruf 2026-09-25 | other |
| 12 | NexLev MCP `youtube_search` (4 Shorts-Suchen) | YouTube-Suchstichproben „AI dream house transformation“, „AI luxury mansion tour“, „cozy bedroom rain ambience“, „futuristic house architecture AI“, „AI house transformation“ | Abruf 2026-09-25 | other (YouTube-Suche) |
| 13 | https://support.google.com/youtube/answer/1311392?hl=en | YouTube channel monetization policies (inauthentic content, reused content) | Update 2025-07-15 | company_primary |
| 14 | https://blog.youtube/news-and-events/disclosing-ai-generated-content/ | How we're helping creators disclose altered or synthetic content | 2024-03-18 | company_primary |
| 15 | https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content | New labels for disclosing AI-generated content (TikTok) | 2023-09-19 | company_primary |
| 16 | https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/ | AI Slop Report: The Global Rise of Low-Quality AI Videos | Daten Okt. 2025 | industry_report |
| 17 | https://www.404media.co/where-facebooks-ai-slop-comes-from/ | Where Facebook's AI Slop Comes From | 2024-08-06 | news_media |
| 18 | https://www.socialinsider.io/blog/tiktok-vs-instagram-reels-vs-youtube-shorts/ | TikTok vs. Reels vs. Shorts: 2026 Engagement Data (Varga, Cucu) | 2026-08-05 | industry_report |
| 19 | https://en.wikipedia.org/wiki/AI_slop | AI slop (Wikipedia) – TikTok-Erwähnungen | Abruf 2026-09-25 | other |
| 20 | https://www.youtube.com/shorts/BMlCqeKWe5Y | DIY Floating Cabin on Plastic Bottles \| Time-Lapse [Concept AI] (127M) | Abruf 2026-09-25 | other |
| 21 | https://www.youtube.com/shorts/ABCQ2EDzW7U | This Tiny Bedroom Transformation Is Genius (32M) | Abruf 2026-09-25 | other |
| 22 | https://www.youtube.com/shorts/i5ot2RecvDw | Choose your dream bedroom (22M) | Abruf 2026-09-25 | other |
| 23 | https://www.youtube.com/shorts/NMy9_aIuKaQ | Stormy Village Life \| Homemade Rasgulla & Family Love #ghibli (59M) | Abruf 2026-09-25 | other |
| 24 | https://www.youtube.com/@HomeGraphix | Home Graphix (Designing 3m² Apartment in New York! 167M) | Abruf 2026-09-25 | other |
| 25 | https://www.youtube.com/@GoodluckPsd_1 | Goodluck Psd (Sitar-Shaped House 64M, Median 910) | Abruf 2026-09-25 | other |
| 26 | https://www.youtube.com/@Structural.Aesthetics | Structural.Aesthetics (Epoxy River Stone Floor 249M) | Abruf 2026-09-25 | other |
| 27 | https://www.youtube.com/@Thegalix ; https://www.youtube.com/@CozeeBed | Galix / CozeeBed (Cozy-Room-Produktkanäle) | Abruf 2026-09-25 | other |
| 28 | Nicht erfolgreich: https://www.tiktok.com/discover/ai-dream-house ; https://www.tiktok.com/tag/aihouse ; https://www.tiktok.com/support/faq_detail?id=7636670084747893268 ; https://newsroom.tiktok.com/en-us/more-ways-to-spot-shape-and-understand-ai-generated-content ; theguardian.com (Kapwing-Bericht) | Kein verwertbarer Inhalt (JS-Hülle, falsche Seite oder Abruf blockiert) | 2026-09-25 | – |
| 29 | Interne Querverweise: `q01_instagram_platform_rules.md` (Instagram-Originalitäts-Ranking, Mosseri-Aussagen), `q06_ai_theme_page_case_studies.md` (IG-Cozy-Pages vs. YouTube-Funnel, WDIV-Fall) | Projekt-Quellennotizen | 2026-09-25 | other |
