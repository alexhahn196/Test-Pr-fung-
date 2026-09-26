# DE-Landschaft KI-/Faceless-Short-Form & Trend-Arbitrage

**Prüfdatum:** 2026-09-26 · **Rohdaten:** `raw_accounts_DE.csv` (52 Zeilen, 40 Spalten) · **Fokus:** mit KI produzierbare Nischen, deutschsprachig (DACH), Instagram mit YouTube Shorts und TikTok als Proxy

---

## 1. Kurzfazit

1. **Das deutschsprachige KI-Short-Form-Angebot ist extrem dünn.** In der NexLev-Datenbank gibt es **7.318 englischsprachige Shorts-Kanäle mit erstem Upload 2026, davon 618 als KI-Content markiert**. Für **Deutsch sind es 29 neue Shorts-Kanäle 2026, davon genau 1 KI-Kanal (Bau Rausch)**. Insgesamt sind nur **4 deutschsprachige KI-Shorts-Kanäle** erfasst: Bau Rausch, Zivox, Champion Spieler und Yunior. Zum Vergleich hat Spanisch 24 KI-Kanäle seit 2026, Französisch 3. Alle Werte sind THIRD-PARTY OBSERVED (NexLev, Abruf 2026-09-26). NexLev deckt nicht alle Kanäle ab, die Unterschiede sind aber um Größenordnungen zu groß, um nur daran zu liegen.
2. **Die stärksten DE-KI-Accounts sitzen auf YouTube, nicht auf Instagram.** An der Spitze steht **@BauRausch** mit 621K Abos (VERIFIED), 387 Mio. Views und 53 Shorts seit 2026-04-13. Die Titel tragen das Label „[KI-Konzept]“. Danach folgen Zivox (347K), Champion Spieler (232K) und Yunior (83,8K, KI-Horror in mehreren Sprachen). Auf Instagram gibt es **keinen einzigen eindeutig deutschsprachigen KI-Account mit verifizierbarer sechsstelliger Followerzahl**. Einzelne Reels erreichen trotzdem Millionen: @spassvibes 5,9 Mio., @dailyflexx_ 3,3 Mio. (beide KI-Tier-Comedy mit deutschem Ton).
3. **Viele Betreiber deutschsprachiger KI-Kanäle sitzen im Ausland.** Bau Rausch hat das Kanal-Land USA, ZeitLab und Die Eisenchroniken Brasilien, Alte Industrie und Amis Staunen ebenfalls USA. Umgekehrt produziert der **deutsche** Betreiber Theoretico auf Englisch (179K YT / 117,5K TikTok). Deutsche Operatoren bespielen den DE-Markt also selbst kaum.
4. **Wo es DE-KI gibt, ist die Ausführung meist schwach.** Häufig sind es Long-Tail-Accounts unter 5K Views pro Reel, mit Veo-Wasserzeichen, kopierten globalen Trends (Trampolin-Hasen, Animalympics) oder rechtlich riskanten IP-Parodien (Bibi Blocksberg, Pokémon, Harry Potter).
5. **Nachfrage nach DE-spezifischen KI-Themen ist belegt, aber nur auf YouTube Long-Form bedient.** Dazu zählen KI-Rekonstruktionen deutscher Städte, BRD-/DDR-Nostalgie und deutsche Industriegeschichte. Kleine Kanäle erreichen hier 250–390K Views pro Video bei weniger als 50K Abos. Auf Instagram fehlt ein entsprechender Short-Form-Account.

---

## 2. Methodik

| Schritt | Werkzeug | Umfang |
|---|---|---|
| Kanal-Discovery YouTube Shorts (DE) | NexLev `search_shorts_niche_finder_channels` (language=German; isAiChannel; firstUploadAfter; semantische Cluster-Queries) | ca. 12 Abfragen |
| KI-Outlier-Videos DE | NexLev `faceless_outliers_videos` (languages=["german"], isAiContent=true) | 67 Treffer, fast nur Long-Form. Shorts ab 2026-05-29: 0 Treffer |
| Internationale Benchmarks | NexLev (language=English, isAiChannel, semantische Queries je Cluster) | 8 Abfragen |
| Instagram (DE) | Öffentliche Instagram-Themenseiten `instagram.com/popular/<begriff>/` (ki-tiere, ki-katze, ki-baby, ki-garten, ki-geschichte, ki-haus), Suchmaschinen-Snippets | Profilseiten liefern HTTP 302 auf den Login bzw. 429. **Nicht umgangen.** |
| Reel-Inhaltsprüfung | NexLev `watch_instagram_video_and_ask` | 6 Reels. Danach war das Tageslimit (sitzungsweit geteilt) erreicht |
| YouTube-Profile | Öffentliche About-Seiten (Abos, Videos, Gesamtviews, Beitrittsdatum, Links), YouTube-oEmbed zur Kanalzuordnung | ca. 30 Kanäle |
| TikTok-Profile | Öffentliche Profilseiten (Follower, Likes, Videoanzahl, Bio) | 20 Handles |
| Presse/Kontext | WebSearch (24 von max. 25 Aufrufen), WebFetch: DWDL, watson, basicthinking, teltarif, netzpolitik, virtual-faces | – |

**Nicht genutzt** (Quellenregeln): imginn, picuki, insta-stories-viewer und ähnliche Viewer-Seiten. Social Blade antwortete mit 403 und wurde nicht umgangen.

**Datenqualitäts-Stufen in der CSV:**
- VERIFIED: öffentliche Plattformanzeige am 2026-09-26, zum Beispiel YouTube-About, TikTok-Profil oder Instagram-Themenseite
- THIRD-PARTY OBSERVED: NexLev, Suchmaschinen-Snippet, Presse
- SELF-REPORTED
- ESTIMATED: eigene Rechnung, etwa Posts pro Woche aus Uploads geteilt durch Wochen seit Start
- UNKNOWN

**Wachstum 30/60/90/120 Tage:** Für **keinen** DE-Account wurden datierte Follower-Snapshots gefunden. Alle Historienfelder stehen deshalb auf UNKNOWN. Als Wachstumsersatz dient nur „Startdatum + heutiger Stand“, also Kanalalter gegen Reichweite.

**Emerging-Outlier-Kriterium in der CSV:** Start vor höchstens ca. 8 Monaten **und** entweder mindestens 20K Follower oder ein Outlier-Video mit Outlier-Score von mindestens 5 bzw. mindestens 1 Mio. Views.

---

## 3. DE-Landschaft je Cluster

| Cluster | Gefundene DE-Accounts (Beispiele) | Stärkster DE-Wert | Professionalität DE | Einordnung |
|---|---|---|---|---|
| **KI-Tiere** | IG: @spassvibes, @dailyflexx_, @aikittendreams, @ki.quatsch, @ki.videos.deutsch, @alluniversum, @princess.and.chipp u. a.; YT: @zivoxreal | Reel 5,9 Mio. (@spassvibes); @aikittendreams ca. 308K Follower (Snippet, Datum unklar); Zivox 347K YT | niedrig bis mittel: meist anonyme Einzelclips ohne Serienformat oder Marke; Veo-Wasserzeichen sichtbar (@ki.videos.deutsch) | **vorhanden, fragmentiert** |
| **KI-Babys/Charaktere** | YT: @AICreatura-life (18,6K; Top-Short 18 Mio.); IG: @systemfreiexit (#kibaby #veo3, 2,5K Views); Marke @idealo (31,9K Views) | 18 Mio. (Einzel-Short) | niedrig: Hit-getrieben (Median 32K) | **dünn** |
| **KI-Geschichte/Zeitreise/POV** | TikTok: @hakimdecoded (14K; „Köln Vlog im Jahr 1248“), @derzeitspringer; YT Long-Form: @TomsZeitreisen (46,3K), @ZeitspringerDE (29,6K), @geschichte.lebt1 (15,9K), @zeitlabofc (10,5K) | Toms Zeitreisen „Bauer im Jahr 1250“ 387K Views | mittel auf YT Long-Form; **auf IG kein Account gefunden** | **Arbitrage hoch** |
| **KI-Architektur/Häuser/Bau** | YT Shorts: **@BauRausch** (621K) | 127 Mio. (Top-Short), Median 1,2 Mio. | hoch, aber ausländischer Operator; **kein IG- oder TikTok-Pendant gefunden** | **Arbitrage hoch (IG leer)** |
| **KI-Interior** | keine DE-KI-Accounts gefunden (Themenseite „ki-haus“ zeigt nur echte Interior-Creator, z. B. @bamwohnen 142K Views) | – | – | **leer** |
| **KI-Garten** | IG: nur reale Creator mit KI als Werkzeug (@gartenlovers 266K, @einfach.phil 68,6K); YT Long-Form: @GrunerDaumenn, @WundersameErinnerungen | Outlier 275K (Grüner Daumen) | Tool-Tutorials statt KI-Visuals; Long-Form mit Clickbait | **KI-Visual-Garten leer** |
| **KI-Food/Kochen, KI-Kaffee** | keine DE-KI-Accounts gefunden | – | – | **leer** |
| **KI-Autos** | YT Long-Form: @FantastiCars.youtube (1,9K; Outlier 353K) | 353K | niedrig | **dünn** |
| **KI-Mode** | nur @noonoouri (virtuelle Influencerin, ca. 472K, Stand Jan. 2026 laut Snippet; EN-Content) | – | hoch, aber CGI-Persona statt KI-Short-Form | **dünn** |
| **KI-Satisfying/ASMR, KI-Miniaturen** | keine DE-KI-Accounts gefunden (der DE-Satisfying-Leader @Malerart ist real) | – | – | **leer** |
| **KI-Storytelling/Horror/Märchen** | YT: @yuniormkt (KI-Horror, DE-Versionen 28 Mio./11 Mio./5,3 Mio. Views); @KENXEXPLORE.01 (73K, Animation, KI unbelegt). **KI-Märchen (Grimm): nichts gefunden** | 28 Mio. (DE-Horror-Short) | mittel (Übersetzung eines EN-Hits) | **Märchen leer, Horror dünn** |
| **KI-Nostalgie DDR/80er/90er** | YT: @DeutschlandNacherzählt (7K; Outlier 318K „Was man 1975 für 10 Mark kaufen konnte“), @DieGutenAlteZeiten (8,3K; Outlier-Score 4,1), @WundersameErinnerungen; IG (Archiv, nicht KI): @ddr.kult ca. 76K, @heimaterinnerungen_an_die_ddr ca. 36K | 318K Views | niedrig; die IG-DDR-Seiten nutzen Originalmaterial | **Arbitrage hoch** |
| **KI-Städte früher/heute** | YT: @Zeitbilder1 („Hamburg 1890 KI-Rekonstruktion“, 6 Videos, 372K Views gesamt), @PretimeHistory, @chronoshistory (117K; echtes Archiv mit KI-Restaurierung), @ZeitspringerDE („Berlin 1709“) | ca. 62K Views/Video bei Zeitbilder | mittel (Long-Form); **Short-Form auf IG fehlt** | **Arbitrage hoch** |
| **KI-Memes/Comedy/Parodie** | TikTok: @tralala0070 (15,2K), @pokestorys67 (14K), @bibi.unzensiert (2,6K); YT: @ChampionSpieler (232K, KI-Fußball) | 232K YT | niedrig und IP-riskant | vorhanden, riskant |
| **KI-Musik** (Zusatzfund) | TikTok: @nimixnimi (111,4K, „Realest AI Artist“); KI-Schlager-Trend („Zwei Pfund Hack“) | 1,7 Mio. Likes | mittel | wachsend (DWDL 09/2026) |
| **KI-Setups** | nichts gefunden | – | – | leer |

---

## 4. Trend-Arbitrage-Matrix (international stark, DE schwach)

INT-Werte: YouTube-Abos laut NexLev (THIRD-PARTY OBSERVED) bzw. Plattformanzeige (VERIFIED), Abruf 2026-09-26.

| Cluster / Format | Internationale Stärke (Belege) | DE-Accounts (Anzahl, Qualität) | Arbitrage | Begründung |
|---|---|---|---|---|
| **KI-Zeitreise-Vlog/POV (Chloe-Format)** | @chloe.vs.history: laut watson (27.02.2026) knapp 180K IG-Follower, laut Presse-/Snippet-Angabe 624K am 03.07.2026 (THIRD-PARTY OBSERVED; also ca. +440K in etwa 4 Monaten). TikTok heute 148,1K (VERIFIED). Tool laut Berichten: PAI (Utopai Studios). YT: MR_DATA 119K („What if you spent one week in Ancient Greece“ 16 Mio.), Theoretico 179K | 1 TikTok-Account mit 14K (@hakimdecoded), 0 auf IG; 4–5 YT-Long-Form-Kanäle unter 50K | **SEHR HOCH** | Format nachweislich viral, DE-Städte (Köln, Lübeck, Nürnberg) bieten unerschöpflichen Stoff. Auf DE-IG ist die Nische leer |
| **KI-Bau-/Transformation-Timelapse** | Momentum Builds 154K (Top 74 Mio.), Kou Yang 72,1K (Top 30 Mio.), BuildFlow 83K („giant strawberry tiny house“ 24 Mio.), Prime Production 683K (Garten-DIY, Start 04/2026) | 1 Kanal (Bau Rausch, YT, ausländischer Operator); IG und TikTok: 0 | **HOCH** | Bau Rausch belegt DE-Nachfrage (621K in etwa 5,5 Monaten, Quedlinburg-Video 56 Mio.), auf Instagram gibt es aber keinen DE-Anbieter |
| **KI-Nostalgie (80er/90er POV)** | Yhujjbg 60,1K („POV you're a 90s kid“ 4,6–10 Mio.), qqq 42,9K, Iconic Archives 38,8K | 0 KI-Accounts auf IG; DDR-IG-Seiten (36–76K) nur mit Archivmaterial; YT-Outlier 318K | **HOCH** | Nachfrage in DE belegt (DDR-Seiten, 1975/10-Mark-Video), KI-POV-Umsetzung fehlt |
| **KI-Tier-Seifenoper / Katzen-Drama** | CATS on GPT 288K (Median 3,5 Mio.), Cat-Holic 328K, Mystery of giants 100K | 0 Serienformate; nur Einzelclips (@spassvibes, @dailyflexx_) | **MITTEL-HOCH** | Einzelclips mit DE-Voiceover erreichen 3–6 Mio. Es fehlt eine wiederkehrende Figur bzw. Serie |
| **KI-Obst-/Objekt-Soap (Fruit Love Island)** | @ai.cinema021: TikTok 2,1 Mio. Follower, 30,6 Mio. Likes, 38 Videos (VERIFIED); laut the-decoder über 10 Mio. Views pro Folge; laut basicthinking Staffel 13.–28.03.2026 | DE: „zahlreiche Nachahmer“ (basicthinking), aber kein namentlich belegter DE-Account | **MITTEL** | Hype-Kurve evtl. schon abgeflacht. Chance nur mit DE-Reality-Parodie (z. B. „Bauer sucht Frau“-Gemüse), dabei Markenrecht beachten |
| **KI-Satisfying/ASMR (Kristalle, Glas, Lava)** | Leon Agate Studio 53,2K (Top 44 Mio., Start 02/2026) | 0 | **MITTEL** | sprachneutral, also kaum DE-Vorteil. Arbitrage nur über DE-Hooks/Text |
| **KI-Cozy-Cooking (Ghibli-Stil)** | Feels Like HOME 462K (Start 19.06.2026, Top 58 Mio.), Ghibli_trip 34,1K | 0 | **HOCH** | DE-Küche (Omas Sonntagsbraten, Kartoffelsalat, Weihnachtsplätzchen) im Cozy-Stil gibt es nicht; Food hat außerdem Affiliate-Nähe |
| **KI-Babys** | global stark (Babys im Podcast, als Sportler), NexLev-EN-Belege nicht gezielt erhoben | 1 YT-Kanal (18,6K) + Long-Tail auf IG | **MITTEL** | Format bekannt (auch idealo-Werbung), Qualität in DE niedrig |
| **KI-Horror/Mystery** | Yunior (EN-Version 164 Mio.), Vidzaw 499K, Nancy Ellise 487K | 1 (Yunior, übersetzt) | MITTEL | DE-Sagen (Rübezahl, Loreley, Krampus, Wilde Jagd) sind unbesetzt |
| **KI-Märchen** | international viel Kids-Animation (Kids-Richtlinien beachten) | 0 KI-Märchen-Accounts gefunden | MITTEL | Grimm-Märchen sind gemeinfrei, aber Kinderzielgruppe (COPPA/„Made for Kids“) begrenzt die Monetarisierung |
| **KI-Interior/Dream Homes** | Dreamy Interior ca. 315K (EN, aus Vorstudie `affiliate-theme-page-research`) | 0 | MITTEL | laut Vorstudie Reichweite ohne Kaufabsicht |
| KI-Tiere-Allgemein | sehr stark | viele Long-Tail-Accounts | NIEDRIG-MITTEL | schon am dichtesten besetzt |
| KI-Memes/IP-Parodien | stark | mehrere kleine TikTok-Accounts | NIEDRIG | Rechtsrisiko |

**EN-Formate ohne gefundenes DE-Pendant:**
- Chloe-vs-History-Zeitreise-Reporterin mit fester Figur
- „What if you spent one week in …“ (MR_DATA)
- Cozy-Ghibli-Cooking (Feels Like HOME)
- „Giant fruit tiny house“ (BuildFlow)
- Epoxy-/Backyard-KI-Transformation (Momentum Builds, Kou Yang)
- „Grandpa-Garden-DIY“ (Prime Production)
- 90s-Kid-POV-Nostalgie (Yhujjbg)
- Crystal-Break-ASMR (Leon Agate)
- KI-Katzen-Serien mit wiederkehrender Familie (CATS on GPT)
- Fruit-Love-Island-Serienformat (DE nur unbenannte Kopien)

---

## 5. DE-spezifische Themen, die KI gut bedienen kann (international nicht vorhanden)

1. **„Zeitreise in deine Stadt“:** Köln 1248 (Dombau), Lübeck 1350 (Pest/Hanse), Nürnberg 1500, Berlin 1920, Dresden vor 1945. Belege für die Nachfrage: @hakimdecoded, @ZeitspringerDE, Zeitbilder („Hamburg 1890“), Geschichte. Lebt. („Berlin in 12 Minuten“ 250K).
2. **BRD-/DDR-Alltagsnostalgie:** „Was kostete 1975 …“, Konsum, Trabi-Warteliste, Westpaket, 90er-Kinderzimmer, D-Mark. Belege: DeutschlandNacherzählt (318K bei 7K Abos), DDR-IG-Seiten mit 36–76K.
3. **Deutsches Bauen und Wohnen:** Fachwerk-Sanierung, Altbau-Transformation, Bunker, Wasserturm, Tiny House auf dem Dorf. Beleg: Bau Rausch „Turm in Quedlinburg“ 56 Mio.
4. **Schrebergarten/Kleingarten-Makeover:** Laube von verwildert zu Traum-Parzelle. Das internationale Garten-DIY-Format (Prime Production 683K) gibt es, eine DE-Variante fehlt.
5. **Deutsche Sagen und Märchen:** Grimm, Rübezahl, Loreley, Krampus/Perchten, Rattenfänger von Hameln. Für die Horror-/Mystery-Schiene sollte man eher auf Erwachsene zielen.
6. **„Amis staunen über Deutschland“:** TÜV, Meisterbrief, Mülltrennung, Kipp-Fenster. Beleg: Amis Staunen mit Outlier 232K im September 2026. Das Format ist KI-Storytelling mit DE-Stolz-Trigger.
7. **Deutsche Industrie- und Markengeschichte:** Pfaff, Neoplan, Quelle, Neckermann. Beleg: Alte Industrie mit 15,5K Abos und Outliern bis 170K.
8. **Oma-Wissen/Alte Gartenpflanzen:** Beleg: Wundersame Erinnerungen, Grüner Daumen mit Outlier 275K. Hier ist das Risiko von Pseudo-Fakten hoch.

---

## 6. Beispiele schlechter lokaler Ausführung

- **@ki.videos.deutsch:** „Oma im Gorilla-Gehege“ mit sichtbarem **Veo-Wasserzeichen**, Morphing der Körper und statischer Menge (Reel-Analyse). 4.017 Views. Das TikTok-Pendant hat 1 Follower und 0 Videos.
- **@ki.quatsch:** „Animalympics“ ist eine Kopie eines globalen Formats. 11,6K Views, kein Serien-Branding.
- **@princess.and.chipp, @wildrose1975, @zauberherzmomente:** Trampolin-Hasen und CapCut-Hunde-Clips mit 1–4K Views. Das ist Trend-Kopie ohne Hook.
- **@systemfreiexit:** Die Idee (KI-Baby + „Typisch Deutschland“) ist DE-spezifisch gut, erreicht aber nur 2,5K Views. Die Umsetzung scheitert, nicht die Idee.
- **@bibi.unzensiert, @pokestorys67, @tralala0070:** Reichweite entsteht über fremde IP (Bibi Blocksberg, Pokémon, Harry Potter) plus Vulgarität. Das birgt Löschungs- und Abmahnrisiko (DWDL 18.09.2026).
- **@zeitlabofc / @PretimeHistory:** KI-Rekonstruktionen von Auschwitz 1942 bzw. dem Berghof sind reichweitenstark, aber mit hohem Reputations- und Plattformrisiko verbunden.
- **@AICreatura-life:** Ein 18-Mio.-Hit steht einem Median von 32K gegenüber. Es gibt keine Serienlogik und keine Figur.
- Generell hat **keiner** der gefundenen DE-KI-Instagram-Accounts einen sichtbaren Link-in-Bio mit Monetarisierung. Das war wegen der Login-Wall allerdings nur eingeschränkt prüfbar.

---

## 7. Monetarisierung (sichtbar)

- **Bau Rausch:** eigenes Info-Produkt („AI Timelapse Guide“, vukovic.ink), keine Affiliate-Links.
- **Toms Zeitreisen:** PayPal-Spenden, Ko-fi, eigene Website, Instagram verlinkt.
- **Theoretico:** Patreon, eigene Website.
- **CHRONOS-MEDIA:** Archiv-Lizenzgeschäft.
- **Amazon.de-Storefront oder Affiliate:** bei **keinem** DE-KI-Account gefunden. Das deckt sich mit der Vorstudie (`affiliate-theme-page-research`): KI-Unterhaltungsreichweite bringt ohne Produktbezug kaum Kaufabsicht.

---

## 8. Top-3-Arbitrage-Chancen

1. **KI-Zeitreise-Vlog mit DE-Städten auf Instagram („Chloe auf Deutsch“)**
   - International: +ca. 440K Follower in etwa 4 Monaten beim Vorbild.
   - DE: kein IG-Account; auf TikTok nur 14K (@hakimdecoded).
   - YT-Long-Form belegt die DE-Nachfrage (Toms Zeitreisen 46K in 8 Monaten, Videos mit 250–390K Views).
   - Die Figur ist markenfähig, der Content lässt sich fortlaufend produzieren (Stadt × Epoche).
2. **KI-Bau-/Transformation-Timelapses mit deutschem Bezug für Instagram**
   - Bau Rausch (621K YT, 387 Mio. Views, gestartet 04/2026) zeigt die DE-Nachfrage.
   - Auf IG und TikTok gibt es kein Pendant, und der Betreiber ist nicht deutsch.
   - Fachwerk, Altbau, Bunker und Schrebergarten sind DE-exklusive Hooks.
3. **KI-POV-Nostalgie BRD/DDR (70er–90er)**
   - International funktioniert „POV you're a 90s kid“ (Top-Videos 4–10 Mio.).
   - In DE nutzen die IG-Seiten (36–76K) nur Archivmaterial.
   - YT-Outlier „1975 für 10 Mark“ mit 318K Views bei 7K Abos.
   - Die Zielgruppe (35–60 Jahre) hat hohe Kaufkraft und reagiert auf Retro-Produkte, was Affiliate-Potenzial eröffnet.

*Nächste Kandidaten:* KI-Cozy-Cooking mit deutscher Küche (EN-Vorbild 462K in 3 Monaten, DE leer) und eine KI-Katzen-Serie mit fester Figur und deutschem Voiceover (Einzelclips erreichen in DE bereits 3–6 Mio.).

---

## 9. Datenlücken

- **Instagram-Followerzahlen:** Für 17 von 21 IG-Zeilen UNKNOWN (Login-Wall, keine zulässige öffentliche Analytics erreichbar; Social Blade 403). Vorhanden sind nur Snippet-Werte ohne sicheres Datum (@aikittendreams ca. 308K, @ddr.kult ca. 76K, @heimaterinnerungen_an_die_ddr ca. 36K, @noonoouri ca. 472K Jan. 2026).
- **Wachstum 30/60/90/120 Tage:** Für keinen DE-Account liegen datierte Snapshots vor, daher überall UNKNOWN. Einzige datierte Reihe ist das EN-Vorbild Chloe vs. History (watson 27.02.2026: ca. 180K; Presse 03.07.2026: 624K).
- **@nimixnimi:** DWDL nennt „über 21.000 Follower“, das Profil zeigt heute 111.400. Das Datum der DWDL-Zahl ist unklar, deshalb wird kein Wachstum ausgewiesen.
- **Reel-Daten:** Instagram-Themenseiten zeigen gerundete Views ohne Datum. Posts, Median und Startdatum der IG-Accounts sind UNKNOWN.
- **Reel-Analyse:** Nur 6 Reels konnten inhaltlich geprüft werden. Das NexLev-Tageslimit von 15 Aufrufen war sitzungsweit erschöpft.
- **NexLev-Abdeckung:** NexLev erfasst nicht alle Kanäle, und das KI-Flag ist uneinheitlich (z. B. @AICreatura-life: isAIContent=false trotz AI-Handle). Die EN/DE-Verhältniszahlen sind deshalb als Größenordnung zu lesen.
- **TikTok createTime:** Der Wert im Profil-JSON wurde als ESTIMATED-Kontostart übernommen. Die Semantik ist nicht offiziell dokumentiert.
- **Nicht bestätigte Zuordnungen:** Instagram-Pendants von Bau Rausch, ZeitLab und Geschichte. Lebt. wurden nicht gefunden. @derzeitspringer (TikTok) und @ZeitspringerDE (YT) sind möglicherweise identisch, das ist nicht verifiziert.
- **Kaum Presse:** Zu DE-spezifischen KI-Accounts gibt es wenig Berichterstattung. Die Presse fokussiert auf KI-Desinformation (CeMAS: 72 TikTok-Accounts, 162 Mio. Views) und Fruit Love Island.

---

## 10. Quellen

**Plattformen (Abruf 2026-09-26):**
- YouTube-About-Seiten: youtube.com/@BauRausch, @zivoxreal, @ChampionSpieler, @yuniormkt, @AICreatura-life, @KENXEXPLORE.01, @DieGutenAlteZeiten, @Shady.History, @TomsZeitreisen, @zeitlabofc, @geschichte.lebt1, @ZeitspringerDE, @Zeitbilder1, @PretimeHistory, @DeutschlandNacherzählt, @WundersameErinnerungen, @FantastiCars.youtube, @AlteIndustrie, @Verstecktes-Deutschland, @DieEisenchroniken, @GrunerDaumenn, @amisstaunen, @chronoshistory, @TheoreticoYT, youtube.com/channel/UC-7DO8-dvzI6B2qbEISkIHQ
- TikTok-Profile: tiktok.com/@hakimdecoded, @nimixnimi, @bibi.unzensiert, @pokestorys67, @tralala0070, @theoretico5, @chloe.vs.history, @ai.cinema021
- Instagram-Themenseiten: https://www.instagram.com/popular/ki-tiere/ ; /ki-katze/ ; /ki-baby/ ; /ki-garten/ ; /ki-geschichte/ ; /ki-haus/

**NexLev (THIRD-PARTY OBSERVED):**
- `search_shorts_niche_finder_channels` (German/English/Spanish/French, isAiChannel, firstUploadAfter)
- `faceless_outliers_videos` (german, isAiContent)
- `youtube_channel_about`
- `watch_instagram_video_and_ask` (Shortcodes DQXGeDNCMsg, DMNi4p2N6sS, DMdAwdVsAdZ, DXEk-4rM3UO, DRevxjnDayZ, DCg19kOi0fi)

**Presse/Web:**
- DWDL, „Was aktuell auf Instagram und TikTok viral geht“ (Stand 18.09.2026): https://www.dwdl.de/magazin/105105/was_aktuell_auf_instagram_und_tiktok_viral_geht/
- watson, „Chloe vs. History“ (27.02.2026): https://politik.watson.de/politik/international/987673655-chloe-vs-history-auf-instagram-wie-ki-geschichte-fuer-die-gen-z-macht
- Chloe vs. History, Follower 03.07.2026, Tool PAI: https://thinklikeacreator.substack.com/p/the-most-viral-history-influencer ; https://www.thecooldown.com/green-business/chloe-history-influencer-ai-reveal/ (via WebSearch-Snippets)
- basicthinking, Fruit Love Island (14.04.2026): https://www.basicthinking.de/blog/2026/04/14/ki-serie-fruit-love-island/
- the-decoder, Fruit Love Island: https://the-decoder.de/fruit-love-island-eine-ki-dating-show-mit-obst-begeistert-millionen/
- teltarif, KI-Obst-Trend (02.05.2026): https://www.teltarif.de/en/ki-trend-tiktok-videos/news/103298.html
- 20 Minuten, KI-Tierchen-Trend: https://www.20min.ch/story/ki-tierchen-fake-tierchen-fuer-klicks-warum-der-neue-insta-hype-polarisiert-103456875
- CeMAS, KI-Slop auf TikTok: https://cemas.io/blog/ki-slop-auf-tiktok/
- netzpolitik.org, AI-Forensics-Studie: https://netzpolitik.org/2025/studie-zu-ai-slop-wie-kuenstliche-videos-social-media-fluten/
- virtual-faces.com, KI-Influencer 2026 (17.08.2026): https://virtual-faces.com/ki-influencer-beispiele/
- OMR, Noonoouri: https://omr.com/de/daily/virtuelle-influencer-noonoouri-zoe
- TikTok-Videos: https://www.tiktok.com/@hakimdecoded/video/7557695839993482518 ; https://www.tiktok.com/@derzeitspringer/video/7560654345474379031
- YouTube-Videos (oEmbed-Zuordnung): ztzzbUNXyXU (ZeitLab), R8uj4lZj0FI (ZEITBILDER), Vl61E7yO228 (Zeitspringer), RKZoVOpH2lI (CHRONOS-MEDIA)

**Vorstudie im Repo:** `affiliate-theme-page-research/05_competitor_database.csv`, `06_competitor_analysis.md` (Bau Rausch, Dreamy Interior)
