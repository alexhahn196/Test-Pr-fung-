# Q05 – Wettbewerber- und Account-Landkarte (Interior / Luxury / Architektur / AI)

Stand der Abrufe: 2026-09-25 · Bearbeitung: Research-Subagent (Workflow) · Status-Tags: VERIFIED / ESTIMATED / THIRD-PARTY ESTIMATE / UNKNOWN

## Fragestellung

Welche Instagram-Accounts bilden das Wettbewerbsumfeld für eine (AI-)Interior-Page, und wie groß sind sie? Gesucht war eine möglichst breite Liste über acht Gruppen:

- **A** klassische Interior-Theme-Pages (plus große Interior-Creator)
- **B** Luxury Homes / Luxury Real Estate
- **C** Architektur- und Designmedien (archdaily, dezeen, designboom, amazing.architecture, architecture_hunter, archdigest, homeadore, designmilk …)
- **D** AI-Architektur-Creator (u. a. Hassan Ragab, Manas Bhatia, Tim Fu)
- **E** AI-Interior-Creator und -Pages
- **F** Dream-Home- und Future-Home-Pages
- **G** Luxury-Lifestyle-Pages mit hohem Interior- oder Hotel-Anteil
- **H** kleine Accounts mit extremen Reel-Views

Ziel waren 120+ Handles, jeweils mit dem Follower-Text genau so, wie die Quelle ihn anzeigt, und mit Quell-URL. Ausdrücklich gesucht war auch Gegenevidenz: Sättigung, Probleme mit AI-Inhalten, Plattform- und Policy-Risiken.

**Ergebnis:** 354 Handles, alle mit Quelle (A 121 · B 35 · C 39 · D 25 · E 25 · F 28 · G 30 · H 51). Die vollständige Tabelle steht im Anhang.

### Methodik und Einschränkungen (bitte vor der Nutzung lesen)

- **Keine WebSearch möglich.** Das WebSearch-Budget der Session war schon beim Start dieses Teilauftrags erschöpft („200 of 200 WebSearch calls“). Deshalb liefen keine `site:instagram.com`-Suchen und keine Suche nach Listicles wie „best AI architecture instagram accounts“. Um das Budget nicht zu umgehen, habe ich auch keine anderen Suchmaschinen per Fetch abgefragt.
- **Genutzt wurden direkte Abrufe (WebFetch) von:**
  - hafi.pro-Kategorieseiten (Stand laut Seite „As of September 25, 2026“)
  - HypeAuditor-Toplisten (Kategorien „Architecture & Urban Design“, „DIY & Design“ und „Luxury“, global und nach Ländern)
  - öffentlichen Instagram-Reel-Embeds (`/reel/<code>/embed/captioned/`), 33 Abrufe
  - Wikipedia und einzelnen Firmenseiten
- **Nicht erreichbar:**
  - Feedspot: `instagram.feedspot.com` löst nicht auf (DNS), `influencers.feedspot.com` antwortet mit 403.
  - hafi.pro-Kategorien `architecture`, `home-decor` und `real-estate`: HTTP 500. Diese Kategorien gibt es laut Kategorienliste nicht.
  - socialblade, starngage, trackalytics, HypeAuditor-Profilseiten und dezeen.com/about: 403.
  - scrumball: 404.
  - `instagram.com/archdaily/`: **429 Too Many Requests**. Nach Vorgabe habe ich keinen weiteren Versuch unternommen und nichts umgangen.
- **Zusätzlich genutzt: die Projekt-Datenbank** `04_reel_database.csv` (2,498 Reels, 1,985 Handles) und `data/raw/accounts/*.json`. Beide wurden von anderen Agenten dieses Workflows aus öffentlichen Instagram-Topic-Seiten und Embeds erhoben. Ich habe die Werte gelesen, aber nicht selbst neu abgerufen. Abgleich: 11 der 33 Handles, die ich selbst per Embed abgerufen habe, haben auch einen Wert in der DB, und alle 11 Werte sind identisch (z. B. ti.fu 272K, drcozyvibes 584K, polliviva 48K, facade_designn 47K, stylarc 2M).
- **Bekannte Lücken bei Gruppe C:** archdaily, dezeen, amazing.architecture, architecture_hunter, homeadore und designmilk konnte ich ohne Suche und bei gesperrtem Profilabruf **nicht** verifizieren. Sie stehen deshalb nicht in der Tabelle (Follower = UNKNOWN). Belegt sind archdigest (11.3M), designboom (4M) und architectanddesign (8.4M).
- **Bekannte Lücken bei Gruppe D:** Die Handles von Hassan Ragab und Manas Bhatia sind UNKNOWN. manasbhatia.com bestätigt „AI Architecture“ als Arbeitsfeld, verlinkt aber kein Instagram-Profil. Für Tim Fu gibt es einen Kandidaten: **@ti.fu** (272K, verifiziert, Caption zu „Parametric Design and Artificial Intelligence“). Die Zuordnung zu Tim Fu ist ESTIMATED.

## Kernbefunde

1. **Die Toplisten der Drittanbieter messen Unterschiedliches und sind unvollständig.**
   - hafi.pro sortiert innerhalb einer eigenen Kategorisierung nach Followern. HypeAuditor rankt nach „genuine audiences and their authentic engagement“.
   - Deshalb fehlt z. B. @archdigest (11.3M laut [HA DIY & Design](https://hypeauditor.com/top-instagram-diy-design/)) in der hafi-Interior-Top-50, deren Nr. 1 @want.zamora mit 2.3M ist ([hafi](https://hafi.pro/top/most-followed-instagram/interior-design)).
   - Die Architektur-Liste von HypeAuditor enthält fachfremde Accounts wie @claudeai (2.1M), @muzammilhb („Quran Reciter“, 4.8M) und @unesco (3.5M, US-Liste) ([HA Arch](https://hypeauditor.com/top-instagram-architecture-urban-design/), [HA Arch US](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/)).
   - Laut hafi wird das Ranking „updated daily“. Die Kategorisierungsmethode wird nicht offengelegt.
   - [VERIFIED als Befund über die Quellen]
2. **Die größten Accounts mit Interior- oder Architekturbezug laut Quellen:**
   - @art_dailydose 22.8M (Aggregator für Kunst und Architektur)
   - @joannagaines 13.7M
   - @archdigest 11.3M
   - @artistsuniversum 11.3M
   - @westwingcom 8.7M
   - @howthingsarebuilld 8.5M
   - @architectanddesign 8.4M
   - @zarahome 8.1M
   - @farahjmerhi 7.5M
   - Quellen: [HA Arch](https://hypeauditor.com/top-instagram-architecture-urban-design/), [HA DIY](https://hypeauditor.com/top-instagram-diy-design/), [HA DIY DE](https://hypeauditor.com/top-instagram-diy-design-germany/). [VERIFIED als Drittanbieter-Anzeige]
3. **Viele Follower bedeuten nicht viel Engagement (Hinweis auf Sättigung).** HypeAuditor zeigt für große Theme-Pages sehr niedriges „Authentic Engagement“ pro Post:

   | Account | Follower | Auth. Eng. pro Post |
   |---|---|---|
   | @howthingsarebuilld | 8.5M | 1.6K |
   | @aipagedaily | 3.1M | 1.7K |
   | @beaverart.engineer1 | 6.2M | 910 |
   | @westwingcom | 8.7M | 781 |
   | @ihsansamhoun.interiors (Gegenbeispiel) | 152.6K | 83.7K |
   | @ahmed.hamdy96 (Gegenbeispiel) | 124.3K | 179.8K |

   Die Engagement-Werte sind Modellwerte von HypeAuditor [THIRD-PARTY ESTIMATE]. Dass große Theme-Pages ihre Reichweite verlieren, ist meine Deutung [ESTIMATED].
4. **Megapages erreichen in der Projekt-Stichprobe wenig Reel-Views.**

   | Account | Follower | Top-Reel im Sample | Views pro Follower |
   |---|---|---|---|
   | @naturesms | 10M | 1.3M | ≈0.13 |
   | @thetrillionairelife | 13M | 1.4M (AI-codiert: „Car shaped villas“) | ≈0.11 |

   Quelle: Projekt-DB ([Reel naturesms](https://www.instagram.com/reel/DOcrXxqknf7/), [Reel trillionairelife](https://www.instagram.com/reel/C-GK8yJyZjT/)). [VERIFIED für Datenpunkte; Schluss auf Sättigung ESTIMATED, da Stichprobe = Topic-Seiten]
5. **AI-Architektur-Creator mit öffentlich belegten Zahlen:**

   | Account | Follower | Quelle / Hinweis |
   |---|---|---|
   | @aiforarchitects | 1.2M | [HA US](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/); Embed-DB 1M; Top-Reel 34.7M Views |
   | @matitectura | 507K followers | [Embed](https://www.instagram.com/reel/DGvmymOMdST/embed/captioned/), Caption: „Bringing old ruins back to life with the help of AI“ |
   | @anderalencar | 478K followers | Caption „Visualization“; AI-Nutzung nicht belegt |
   | @ti.fu | 272K followers | Zuordnung zu Tim Fu ESTIMATED |
   | @archibible | 220K followers | Reel 14.3M auf der Topic-Seite `midjourney-architecture` |
   | @theimagehs | 137K followers | Tools laut Caption: Midjourney, Magnific, Hailuo |
   | @refikanadol | 1.1M | HA |
   | @aipagedaily | 3.1M | HA |

   [VERIFIED]
6. **AI-Interior- und Dream-Room-Pages erreichen die höchsten Einzelreichweiten im Sample:**
   - @siyad_abdali: 4M, Reel mit 282M Views (AI-codiert)
   - @drcozyvibes: 584K followers, Reel mit 155M Views (AI-codiert, nicht als AI offengelegt)
   - @ifonly.ai: 1M followers, Reel mit 136M Views, Caption „AI-generated video (Midjourney • Magnific“
   - @soothenests: 2M, 45.1M Views
   - @sunt_mrr: 2M followers, 24.5M Views, #midjourney
   - @elitebuildhq: 2M followers, 24M Views
   - @luxuriatetouche: 4M, 9.7M Views
   - @cozyzen.ai: 498K followers
   - [VERIFIED, Embeds 2026-09-25]
7. **Gegenevidenz 1: Virale Ausreißer kleiner Accounts sind überwiegend echte Aufnahmen, nicht AI.**
   - In der Projekt-DB haben 657 Accounts einen Follower-Wert. 70 davon haben unter 100K Follower und ein Reel mit mindestens 1M Views.
   - Produktionsart ihrer Top-Reels: **35 real footage, 8 ai_generated, 2 3d_render**, 2 unclear, 23 uncodiert.
   - Die extremsten Fälle sind reale Aufnahmen: @jen.casanovas.ibiza (5K, 11.7M), @alshifarealtor.dxb (47K, 54.3M), @ekam_sandhu_fitness (1K, 2.3M).
   - Die extremen AI-Fälle @ai.poly_ (14K followers, 147M) und @polliviva (48K followers, 97.2M) zeigen **keine** Interior-Inhalte, sondern allgemeine AI-Videos (russische Captions).
   - [VERIFIED für die Zählung. Die Codierung ist AI-gestützt und damit ESTIMATED; die DB wird parallel ergänzt.]
8. **Gegenevidenz 2: Auf den „AI-Interior“-Topic-Seiten steht viel klassisches CGI.**
   - @sireen.design (94K, 7.4M Views): „Software: 3D max , vray ,Photoshop“
   - @ki.render (19K, 7.3M): „3dsMax, Corona Render“
   - @leylaa__asgarii (60K, 5.8M), @iz__designs (109K, 21.9M): „Design & Render“
   - @homebyhyla (168K, 28.6M): „#render3d“
   - Von 132 Reels auf AI-Topic-Seiten in der DB sind nur 11 als ai_generated codiert, 4 als 3d_render und 114 noch nicht codiert.
   - Folge: Das Wettbewerbsfeld „AI-Interior“ überschneidet sich stark mit Archviz-Studios. Dort sind die Produktionskosten höher, aber die Inhalte gelten auch als glaubwürdiger. [VERIFIED für die Captions]
9. **Gegenevidenz 3: Kopierte Motive und irreführende Behauptungen.**
   - Dasselbe Motiv, ein schlangenförmiger Wolkenkratzer, läuft auf zwei Accounts:
     - @visionbuildofficial (50K followers, 6.6M Views): „The Craziest Snake Tower Ever Built in the USA 🐍🏙️“
     - @facade_designn (47K followers, 2.1M Views): „A futuristic skyscraper inspired by the power of a serpent…“ (AI-codiert)
   - Quellen: [Embed](https://www.instagram.com/reel/DW8_CcQESn8/embed/captioned/), [Embed](https://www.instagram.com/reel/DS5GYPmAESA/embed/captioned/).
   - Das deutet auf schnelle Sättigung populärer AI-Motive hin. Zudem wird ein wahrscheinlich AI-generiertes Gebäude als real gebaut dargestellt, was ein Policy- und Glaubwürdigkeitsrisiko ist.
   - [VERIFIED für Captions; AI-Status von visionbuild ESTIMATED]
10. **Luxury-Lifestyle-Pages: niedrige Einstiegshürde, harte Konkurrenz.**
    - @millionaire1ife: 172K followers mit **4 posts**, Reel „Your life in 3 years 😎“ mit 4.1M Views
    - @wifizei: 329K followers, „Future Life 🫀💸“, 8.6M Views
    - @nouxri: 120K, Dubai-Pool, 7.5M Views
    - Etablierte Pages laut HA Luxury: @goodlife 3.3M, @luxurysouqls 2.5M, @heritageclass 1.2M, @luxrysociety 520.9K; außerdem @beautifulhotels mit 6M followers (Embed).
    - [VERIFIED]
11. **Luxury Real Estate:**
    - @ryanserhant 3M followers (Embed)
    - @jasonoppenheim 1.6M
    - @stylarc 1.6M bei HA, 2M im Embed
    - @binghatti 1.8M
    - @theluxuryhomeshow 2M
    - @greathousesandestates 633.9K
    - Der größte Einzelhit im Sample: @clarazrd (297K), NYC-Penthouse-Reel mit 72.1M Views, real footage.
    - Makler-Reels mit echten Aufnahmen konkurrieren direkt um dieselbe „Dream Home“-Aufmerksamkeit.
    - [VERIFIED]
12. **Deutschsprachiger Markt:**
    - HA DIY & Design Deutschland: @westwingcom 8.7M, @mi.interieur 1.3M, @haus_plan_b 1.2M (Auth.Eng. 120.9K), @live.like.archi 1.1M, @homeofmerve 459.4K ([HA DIY DE](https://hypeauditor.com/top-instagram-diy-design-germany/)).
    - HA Architecture Deutschland: @baunetz 126.9K, @gestalten 251.7K, @ifdesign 246.7K.
    - In keiner der beiden deutschen Top-50-Listen steht eine erkennbare AI-Interior-Page. Das spricht für eine Nischenlücke im Deutschen, kann aber auch bedeuten, dass es dort wenig Nachfrage gibt [ESTIMATED].
13. **Generische AI-Pages sind groß, zeigen aber keine Interiors.** Laut [hafi AI & Tech](https://hafi.pro/top/most-followed-instagram/ai-tech):
    - @evolving.ai 4.8M
    - @artificialntellligence 1.5M
    - @theartificialintelligence 1.3M
    - @predmet_ai 446.5K (in der DB mit einem ai-render-Reel über 9.9M Views)
    - @the_a_i_prompter 155K (hafi Digital Art)
    - [VERIFIED]
14. **Architekturmedien (Gruppe C) mit Belegen:**
    - @designboom: 4M followers, 17,300 posts (Embed, verifiziert)
    - @archdigest: 11.3M
    - @architectanddesign: 8.4M
    - @vogueliving: 3M
    - @houseandgardenuk: 2.4M
    - @zha.world: 1.6M
    - @tmagazine: 1.4M
    - @archiproducts: 1M
    - Für dezeen gibt es nur eine Gesamtzahl für alle Plattformen: „more than 6.5 million social media followers“ zum Zeitpunkt der Übernahme im März 2021 ([Wikipedia Dezeen](https://en.wikipedia.org/wiki/Dezeen)). Die Instagram-Zahl ist UNKNOWN.
15. **Monetarisierung ist sichtbar.**
    - @architecturaai_ (23K followers, 5.4M Views): „FREE EBOOK IN BIO⬆️ Learn to create AI interiors, home designs & prompts Join 13M+ viewers“
    - @archibible: „Shop link in bio 🖼️ DM for commissions 📩“
    - @ti.fu: bewirbt einen Workshop bei @thepaacademy
    - [VERIFIED; Umsätze UNKNOWN]
16. **Plattform- und Gesellschaftskontext (Gegenevidenz, nicht Instagram-spezifisch):**
    - Der Wikipedia-Artikel „AI slop“ nennt als Beispiel: „A medical student in India said he made thousands of dollars each month from low effort, AI-generated images on Instagram and Fanvue.“ (Einkommen: THIRD-PARTY ESTIMATE)
    - Zu YouTube: „YouTube CEO Neal Mohan stated that reducing slop and detecting deepfakes were priorities for YouTube in 2026.“ ([Wikipedia AI slop](https://en.wikipedia.org/wiki/AI_slop))
    - Das ist ein Richtungssignal für Plattform-Policies. Eine Instagram-spezifische Maßnahme gegen AI-Interior-Inhalte wurde hier nicht belegt [UNKNOWN].

## Zahlen-Tabelle

| Kennzahl / Account | Wert (exakt wie angezeigt) | Quelle | Datum | Status |
|---|---|---|---|---|
| hafi Interior-Design Top 50, Nr. 1 | @want.zamora 2.3M | [hafi](https://hafi.pro/top/most-followed-instagram/interior-design) | Stand 2026-09-25 | VERIFIED (Drittanbieter-Anzeige) |
| @interiordesignideas | 1.8M | hafi Interior | 2026-09-25 | VERIFIED (Drittanbieter) |
| @archdigest | 11.3M / Auth.Eng. 22.8K | [HA DIY](https://hypeauditor.com/top-instagram-diy-design/) | 2026 (ohne Monat) | Follower VERIFIED (Drittanbieter); Eng. THIRD-PARTY ESTIMATE |
| @architectanddesign | 8.4M / 25.4K | [HA Arch](https://hypeauditor.com/top-instagram-architecture-urban-design/) | 2026 | wie oben |
| @art_dailydose | 22.8M / 58K | HA Arch | 2026 | wie oben |
| @howthingsarebuilld | 8.5M / 1.6K | HA Arch | 2026 | wie oben |
| @aipagedaily | 3.1M / 1.7K | HA Arch | 2026 | wie oben |
| @ihsansamhoun.interiors | 152.6K / 83.7K | HA Arch; hafi 152.6K; Embed-DB 168K | 2026 | wie oben |
| @westwingcom | 8.7M / 781 | [HA DIY DE](https://hypeauditor.com/top-instagram-diy-design-germany/) | 2026 | wie oben |
| @aiforarchitects | 1.2M / 2.4K | [HA Arch US](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | 2026 | wie oben |
| @stylarc | 1.6M (HA) vs. „2M followers“ (Embed) | HA Arch; [Embed](https://www.instagram.com/reel/DEZr68gOpD0/embed/captioned/) | 2026-09-25 | Rundungsdifferenz |
| @designboom | „4M followers“, „17,300 posts“ | [Embed](https://www.instagram.com/reel/DMdzxzsup8T/embed/captioned/) | 2026-09-25 | VERIFIED |
| @ifonly.ai | „1M followers“, „419 posts“; Reel 136M Views | [Embed](https://www.instagram.com/reel/C--Al6UA6GE/embed/captioned/) + DB | 2026-09-25 | VERIFIED |
| @drcozyvibes | „584K followers“; Reel 155M | [Embed](https://www.instagram.com/reel/C87NQHRtm6B/embed/captioned/) | 2026-09-25 | VERIFIED |
| @siyad_abdali | 4M; Reel 282M | Projekt-DB ([Reel](https://www.instagram.com/reel/C_Pf1dboaeJ/)) | Abruf durch Workflow 2026-09-25 | VERIFIED (DB) |
| @ai.poly_ | „14K followers“, „30 posts“; Reel 147M | [Embed](https://www.instagram.com/reel/DYoyUS9NlAr/embed/captioned/) | 2026-09-25 | VERIFIED |
| @polliviva | „48K followers“; Reel 97.2M | [Embed](https://www.instagram.com/reel/Daa8AwIMNMt/embed/captioned/) | 2026-09-25 | VERIFIED |
| @alshifarealtor.dxb | 47K followers; Reel 54.3M | DB ([Reel](https://www.instagram.com/reel/DdMPxaloS3f/)) | 2026-09 | VERIFIED (DB) |
| @millionaire1ife | „172K followers“, „4 posts“; Reel 4.1M | [Embed](https://www.instagram.com/reel/DLAjTvmIRre/embed/captioned/) | 2026-09-25 | VERIFIED |
| @naturesms | 10M; Top-Reel im Sample 1.3M | DB | 2026-09 | VERIFIED (DB) |
| Projekt-DB: Accounts mit Follower-Wert | 657 (davon 70 mit <100K Followern und einem Reel ≥1M Views) | `04_reel_database.csv` | Snapshot 2026-09-25 | VERIFIED (Zählung) |
| Produktionsart der Top-Reels dieser 70 | 35 real_footage / 8 ai_generated / 2 3d_render / 2 unclear / 23 uncodiert | DB | 2026-09-25 | ESTIMATED (AI-gestützte Codierung) |
| Reels auf AI-Topic-Seiten (DB) | 132, davon 11 ai_generated, 4 3d_render, 2 real, 1 unclear, 114 uncodiert | DB | 2026-09-25 | ESTIMATED |
| Dezeen Social-Media-Follower (alle Plattformen) | „more than 6.5 million“ (2021) | [Wikipedia](https://en.wikipedia.org/wiki/Dezeen) | Aussage für März 2021 | VERIFIED (Sekundärquelle); IG-Wert UNKNOWN |
| hafi AI & Tech, Nr. 1 | @evolving.ai 4.8M | [hafi AI](https://hafi.pro/top/most-followed-instagram/ai-tech) | 2026-09-25 | VERIFIED (Drittanbieter) |

## Widersprüche/Unsicherheiten

- **Rundung der Instagram-Embeds.** Ab 1M zeigt das Embed ganze Millionen an: @stylarc „2M“ gegenüber 1.6M bei HA, @ell.glamhome „1M“ gegenüber 1.2M bei HA, @aiforarchitects 1M (DB) gegenüber 1.2M bei HA. Für präzise Vergleiche sind die Drittanbieterwerte feiner, aber nicht gegen Instagram verifiziert.
- **Drittanbieter-Werte sind im Wesentlichen konsistent.** @smyrna__home: hafi 615.7K, HA DE 615.6K, Embed-DB 616K. @ihsansamhoun.interiors: hafi und HA 152.6K, das Embed zeigt 168K (anderer Zeitpunkt oder Cache).
- **Kategorien-Rauschen.** hafi führt in „Interior Design“ z. B. @aramideskitchen und einen Maler (@wendel.lazottioficial). HA führt in „Architecture“ @claudeai, @muzammilhb und @unesco. HA-Ranglisten sind nach Engagement sortiert, sodass Pages mit vielen Followern und wenig Engagement fehlen. Bei beiden Anbietern ist unklar, wie Accounts in Kategorien kommen.
- **HypeAuditor nennt nur das Jahr** („2026“), keinen genauen Monat. Die Paginierung (`?p=2`) liefert wieder Rang 1–50. Nur die Top 50 sind einsehbar.
- **Einordnung als AI ist unsicher.** Hashtags und Topic-Seiten („ai-interior-design“) enthalten klassische 3D-Renderings. Umgekehrt legen AI-Accounts ihre Inhalte oft nicht offen (@drcozyvibes ist AI-codiert, die Caption nennt keine AI). Die AI-Codierung in der DB ist AI-gestützt (ESTIMATED).
- **Identitäten:** @ti.fu = Tim Fu ist ESTIMATED. Hassan Ragab und Manas Bhatia sind UNKNOWN. @gautamsinghania99 (12M) ist ein Unternehmer und keine Immobilien-Page; er steht wegen eines Immobilien-Reels (48.7M Views) in Gruppe B.
- **Die Projekt-DB ändert sich laufend.** Zwischen zwei Abfragen stieg die Zahl der Accounts mit Follower-Wert von 274 auf 657. Alle DB-Zahlen hier sind ein Snapshot vom 2026-09-25.
- **Nicht verifiziert (UNKNOWN):** archdaily, dezeen, amazing.architecture, architecture_hunter, homeadore, designmilk, luxurylistings, luxury (Instagram-Handles aus der Aufgabenstellung). Die Aufnahme in eine Wettbewerberliste ist plausibel, Follower-Zahlen liegen aber nicht vor.
- **Gruppe H ist nach Views ausgewählt,** also mit Survivorship-Bias. Die Topic-Seiten zeigen nur Top-Reels. Die Basisrate kleiner Accounts ohne viralen Hit ist unbekannt.
- **Einkommen und Umsätze:** In diesem Teilauftrag wurde keine Umsatzzahl eines Accounts belegt (UNKNOWN). Die einzige Einkommensangabe, aus dem Wikipedia-Artikel „AI slop“, gilt als THIRD-PARTY ESTIMATE und betrifft keine Interior-Inhalte.

## Quellenliste

| # | URL | Titel | Datum | Quellentyp |
|---|---|---|---|---|
| 1 | https://hafi.pro/top/most-followed-instagram/interior-design | Top 50 Interior Design Instagram Accounts | „As of September 25, 2026“ | analytics_platform |
| 2 | https://hafi.pro/top/most-followed-instagram/designers | Top 50 Designers Instagram Accounts | 2026-09-25 | analytics_platform |
| 3 | https://hafi.pro/top/most-followed-instagram/ai-tech | Top 50 AI & Tech Instagram Accounts | 2026-09-25 | analytics_platform |
| 4 | https://hafi.pro/top/most-followed-instagram/digital-art | Top 50 Digital Art Instagram Accounts | 2026-09-25 | analytics_platform |
| 5 | https://hafi.pro/top/most-followed-instagram/art-design | Top 50 Art & Design Instagram Accounts | 2026-09-25 | analytics_platform |
| 6 | https://hafi.pro/top/most-followed-instagram/hotels | Top 50 Hotels Instagram Accounts | 2026-09-25 | analytics_platform |
| 7 | https://hafi.pro/top/most-followed-instagram/travel | Top 50 Travel Instagram Accounts | 2026-09-25 | analytics_platform |
| 8 | https://hafi.pro/top/most-followed-instagram/graphic-design | Top 50 Graphic Design Instagram Accounts | 2026 | analytics_platform |
| 9 | https://hafi.pro/top/most-followed-instagram/motivational | Top 50 Motivational Instagram Accounts | 2026 | analytics_platform |
| 10 | https://hafi.pro/top/most-followed-instagram (sowie /diy, /photography) | Übersicht und Kategorienliste; DIY- und Photography-Listen geprüft, kaum relevant | 2026-09-25 | analytics_platform |
| 11 | https://hypeauditor.com/top-instagram-architecture-urban-design/ | Top Architecture & Urban Design Instagram Influencers | 2026 | analytics_platform |
| 12 | https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/ | dito, United States | 2026 | analytics_platform |
| 13 | https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/ | dito, United Kingdom | 2026 | analytics_platform |
| 14 | https://hypeauditor.com/top-instagram-architecture-urban-design-germany/ | dito, Germany | 2026 | analytics_platform |
| 15 | https://hypeauditor.com/top-instagram-architecture-urban-design-italy/ | dito, Italy | 2026 | analytics_platform |
| 16 | https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/ | dito, UAE | 2026 | analytics_platform |
| 17 | https://hypeauditor.com/top-instagram-architecture-urban-design-chile/ | dito, Chile | 2026 | analytics_platform |
| 18 | https://hypeauditor.com/top-instagram-diy-design/ | Top 50 DIY & Design Instagram Influencers | 2026 | analytics_platform |
| 19 | https://hypeauditor.com/top-instagram-diy-design-united-states/ | dito, United States | 2026 | analytics_platform |
| 20 | https://hypeauditor.com/top-instagram-diy-design-germany/ | dito, Germany | 2026 | analytics_platform |
| 21 | https://hypeauditor.com/top-instagram-diy-design-united-arab-emirates/ | dito, UAE | 2026 | analytics_platform |
| 22 | https://hypeauditor.com/top-instagram-luxury/ | Top 50 Luxury Influencers on Instagram | 2026 | analytics_platform |
| 23 | https://hypeauditor.com/top-instagram-luxury-united-states/ | dito, United States | 2026 | analytics_platform |
| 24 | https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/ | dito, UAE | 2026 | analytics_platform |
| 25 | https://www.instagram.com/reel/{code}/embed/captioned/ (33 Codes, siehe Anhang: „IG-Embed …“) | Öffentliche Instagram-Reel-Embeds (Follower- und Post-Text, Caption) | Abruf 2026-09-25 | instagram_public |
| 26 | https://en.wikipedia.org/wiki/Dezeen | Dezeen (Wikipedia) | Abruf 2026-09-25, Aussage 2021 | other |
| 27 | https://en.wikipedia.org/wiki/ArchDaily | ArchDaily (Wikipedia): keine IG-Zahl; „17.9 million monthly readers … as of 2022“ | Abruf 2026-09-25 | other |
| 28 | https://en.wikipedia.org/wiki/AI_slop | AI slop (Wikipedia) | Abruf 2026-09-25 | other |
| 29 | https://www.manasbhatia.com/landing.html | Manas Bhatia: „Computational Designer & Spatial Artist“, „AI Architecture“ | Abruf 2026-09-25 | company_primary |
| 30 | https://design-milk.com/advertise/ | Design Milk Advertise: keine Follower-Zahl | Abruf 2026-09-25 | company_primary |
| 31 | /home/user/Test-Pr-fung-/instagram-interior-research/04_reel_database.csv und data/raw/accounts/followers_w1_*.json | Projekt-DB (öffentliche Topic-Seiten und Embeds, erhoben von Workflow-Agenten) | Snapshot 2026-09-25 | instagram_public (sekundär, projektintern) |
| – | Nicht erreichbar: instagram.feedspot.com (DNS), influencers.feedspot.com (403), hafi …/architecture, /home-decor, /real-estate (500), socialblade (403), starngage (403), trackalytics (403), hypeauditor.com/instagram/archdaily (403), dezeen.com/about (403), designboom.com/about (404), archdaily.com/content/about/company (404), instagram.com/archdaily/ (429), scrumball.com/rankings/instagram (404), modash (Redirect auf 404) | – | 2026-09-25 | – |

## Anhang: Vollständige Account-Liste (354 Handles)

Spalte "Follower (Text)" = exakt wie in der Quelle angezeigt (hafi.pro/HypeAuditor: Zahl ohne Zusatz; Instagram-Embed: "... followers"; Projekt-DB = gerundeter Wert aus öffentlichem Embed-Abruf eines anderen Workflow-Agents, Datei `04_reel_database.csv` bzw. `data/raw/accounts/`). "UNKNOWN" = Follower nicht erhoben; der Handle stammt dann von einer öffentlichen Instagram-Topic-Seite (Reel-URL als Beleg, Views gerundet). Abkürzungen: HA = HypeAuditor, IG = Instagram. Status der Follower-Werte: hafi/HA = Drittanbieter-Anzeige (VERIFIED als "so angezeigt", nicht gegen Instagram geprüft); IG-Embed = VERIFIED (öffentlich, gerundet, Stand 2026-09-25).


### A - Klassische Interior-Theme-Pages & Interior-Creator (121)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @want.zamora | 2.3M | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Marco Zamora |
| 2 | @interiordesignideas | 1.8M | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Theme-Page 'Interior Design Ideas' |
| 3 | @interiordesign.addicts | 1.2M | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Theme-Page 'Interior Design Addicts' |
| 4 | @theworldofinteriors | 1.2M | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Magazin The World of Interiors |
| 5 | @carawoodhouseinteriors | 986.9K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Designerin |
| 6 | @arrofiramadhan | 827.6K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Arrofi Ramadhan |
| 7 | @essajeesatelier | 752.1K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Atelier |
| 8 | @interior_xpressions | 748.2K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Interior Xpression |
| 9 | @smyrna__home | 615.7K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Nevin Yekdar; Embed-DB 616K |
| 10 | @mrphoenixgrey | 476K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Phoenix Grey / Interior Design |
| 11 | @aramideskitchen | 439.4K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Kategorie-Zuordnung durch hafi fraglich |
| 12 | @beautyofinteriors | 405.5K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; 'INTERIORS / LISTINGS' - Interior+Immobilien-Theme-Page |
| 13 | @lluxuryanddesign | 319.8K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Leah Lilly/Interior Designer |
| 14 | @lisaspollock | 315.5K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Lisa Pollock |
| 15 | @the_interior_lens | 305.6K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Becks - Interior Designer |
| 16 | @laurenmakk | 304.7K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Lauren Makk |
| 17 | @interioresmag | 298.7K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Revista INTERIORES |
| 18 | @wendel.lazottioficial | 253.5K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Maler - Zuordnung fraglich |
| 19 | @osborninteriors | 244.7K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Bee Osborn |
| 20 | @madspatial | 239.1K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; adri - interior lifestyle |
| 21 | @previewsinteriors | 232.1K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Sally Draughon |
| 22 | @salvatoreizzointeriors | 227.2K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Salvatore Izzo |
| 23 | @oummi_interior | 226.8K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 24 | @felipedealmeida_designer | 223.7K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 25 | @interiorbygini | 202K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Angelina Doerfler (DE) |
| 26 | @the.elm.house | 184.1K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; DIY & Vintage |
| 27 | @img_nyc | 177.5K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Interior Marketing Group |
| 28 | @sol_van_dorssen | 175K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 29 | @rocking_the_cotswolds | 170.3K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Interiors-Journalistin |
| 30 | @cindykronfle | 169K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 31 | @saobentocurainterior | 168.8K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 32 | @liebs_hier | 167.5K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Jana Ahlers (DE) |
| 33 | @mcinteriores_sevilla | 166.3K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 34 | @studio.lux.interiors | 162.1K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Interior Design/Styling Page |
| 35 | @hendidesign | 157.4K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Marbella |
| 36 | @ihsansamhoun.interiors | 152.6K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; auch HypeAuditor Arch #21 (152.6K); Embed-DB 168K |
| 37 | @willcarinteriores | 149K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 38 | @studiopietboon | 146.6K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Studio Piet Boon |
| 39 | @interiorsbysteveng | 142.8K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 40 | @anthonyimmediato | 141.3K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 41 | @meladecodesign | 140.7K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Online-Interior-Studio |
| 42 | @interiors.stuff | 140.4K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50; Theme-Page 'Interiors & Stuff' |
| 43 | @kemble_interiors | 139.1K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 44 | @nointerioreassim | 128.5K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 45 | @biscottohouse | 127.2K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 46 | @bloom_jennybrooks | 125.7K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 47 | @camillealexandrainteriors | 122.2K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 48 | @pauladuarteinteriores | 113.8K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 49 | @andrewjhow | 104.2K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 50 | @rosario.interiores | 100.2K | [hafi interior-design](https://hafi.pro/top/most-followed-instagram/interior-design) | hafi.pro Interior-Design Top 50;  |
| 51 | @lux.interiors | 1.6M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor Architecture Top 50; Theme-Page 'Interior Design & Architecture'; HA Auth.Eng. 4.9K |
| 52 | @one.interior.mag | 1.1M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor Architecture Top 50; Theme-Page 'One Interior Magazine'; HA Auth.Eng. 8K |
| 53 | @farahjmerhi | 7.5M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Farah Merhi |
| 54 | @joannagaines | 13.7M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Joanna Gaines |
| 55 | @shellychicboutique | 2.7M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Michelle McRae |
| 56 | @ell.glamhome | 1.2M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Embed-DB zeigt '1M' |
| 57 | @haus_plan_b | 1.2M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Cindy-Adriana Speich (DE); Auth.Eng. 120.9K |
| 58 | @prettymyadeco | 2.9M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Judith J Kombe |
| 59 | @vk_passiondeco_officiel | 5.1M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Victoria Floc'h |
| 60 | @maniadedecoracao | 3.5M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Raisa Guerra |
| 61 | @kjg_home | 2.1M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Kirsty Gore |
| 62 | @belgravevilla | 2.2M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Renovation |
| 63 | @dekorhomedekor | 1.8M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Esra |
| 64 | @biancamoratto | 1.4M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Bianca Morato |
| 65 | @anajohnson | 1.5M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; Ana Johnson |
| 66 | @celiasawyer | 1.3M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor DIY & Design Top 50; auch hafi Designers 1.3M |
| 67 | @decor.snippets | 3.3M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US; 'Rue / Home Decor / Lifestyle' |
| 68 | @studiomcgee | 4.1M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US; Studio McGee |
| 69 | @nateberkus | 2M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US; Nate Berkus |
| 70 | @lonefoxhome | 1.6M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US; Drew Michael Scott |
| 71 | @glamorouslyliving | 2.4M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US;  |
| 72 | @blissfulhomedecor | 1.8M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US; Stephanie Padilla |
| 73 | @nestingwithgrace | 1.7M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US;  |
| 74 | @homewithhelenandco | 1.3M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US;  |
| 75 | @magnolia | 5.8M | [HA diy-design-united-states](https://hypeauditor.com/top-instagram-diy-design-united-states/) | HypeAuditor DIY & Design US; Marke Magnolia |
| 76 | @mi.interieur | 1.3M | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland; Michele / Interieur |
| 77 | @interiorby_selinda | 113.1K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland; Auth.Eng. 67.7K |
| 78 | @westwingcom | 8.7M | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland; Marke WESTWING; Auth.Eng. nur 781 |
| 79 | @live.like.archi | 1.1M | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland; Rosemarie Thiedmann |
| 80 | @interiorsari | 437.1K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland;  |
| 81 | @interior_by_canik | 664K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland;  |
| 82 | @homeofmerve | 459.4K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland; Embed-DB 459K; Reel 13.1M Views |
| 83 | @monaport.interiors | 384.9K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland;  |
| 84 | @home.ba.interieur | 602.9K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland;  |
| 85 | @homestory_pictures | 764.8K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland;  |
| 86 | @cima.villa | 400.1K | [HA diy-design-germany](https://hypeauditor.com/top-instagram-diy-design-germany/) | HypeAuditor DIY & Design Deutschland;  |
| 87 | @nour.aljabrii | 1.1M | [HA diy-design-united-arab-emirates](https://hypeauditor.com/top-instagram-diy-design-united-arab-emirates/) | HypeAuditor DIY & Design UAE;  |
| 88 | @babsharqii | 483.2K | [HA diy-design-united-arab-emirates](https://hypeauditor.com/top-instagram-diy-design-united-arab-emirates/) | HypeAuditor DIY & Design UAE;  |
| 89 | @evainteriors | 417.6K | [HA diy-design-united-arab-emirates](https://hypeauditor.com/top-instagram-diy-design-united-arab-emirates/) | HypeAuditor DIY & Design UAE;  |
| 90 | @gaurikhan | 5.8M | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50; Gauri Khan; auch HA Architecture #10 |
| 91 | @jeremiahbrent | 1.4M | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50;  |
| 92 | @adesignersmind | 1.4M | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50; 'A Designers Mind' |
| 93 | @leannefordinteriors | 583.5K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50;  |
| 94 | @lohause | 518.4K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50;  |
| 95 | @karim_rashid_official | 507.1K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50;  |
| 96 | @jimmiemartin | 241.8K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50;  |
| 97 | @designeers.club | 161.1K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50; Theme-Page 'DESIGNEERS / Interior Design' |
| 98 | @nicoleweberdesign | 154.4K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50;  |
| 99 | @miriam_alia | 104.5K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi.pro Designers Top 50;  |
| 100 | @thatcoolmoodboard | 394.3K | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor; Moodboard-Theme-Page |
| 101 | @mid_century_friends | 1.3M | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor; MCF - SELECT |
| 102 | @ashleytstark | 1.6M | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor;  |
| 103 | @renovationpalazzopuro | 574.3K | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor; Renovation-Serie |
| 104 | @spazibelli | 408.4K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor; 'SPAZI BELLI / INTERIOR DESIGN' |
| 105 | @beautifuldecor__ | 131.8K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 106 | @olenkainteriors | 72.1K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 107 | @blogdecorador | 605.7K | [HA architecture-urban-design-chile](https://hypeauditor.com/top-instagram-architecture-urban-design-chile/) | HypeAuditor; El Blog del Decorador |
| 108 | @sophiepatersoninteriors | 729K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 109 | @beataheuman | 362.4K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 110 | @roseuniacke | 279.8K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 111 | @pollyanna_wilkinson | 614.4K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 112 | @benpentreath | 220.2K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 113 | @studioashby | 224.2K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 114 | @katrinakuzina | 458.4K | [HA architecture-urban-design-united-arab-emirates](https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/) | HypeAuditor;  |
| 115 | @wafa.ghaoui.designs | 130.3K | [HA architecture-urban-design-united-arab-emirates](https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/) | HypeAuditor; Interior Designer Dubai |
| 116 | @class_designstudio | 496K | [HA architecture-urban-design-united-arab-emirates](https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/) | HypeAuditor; Auth.Eng. nur 93 |
| 117 | @berlin.interior | 316.8K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor; Melanie Kharad |
| 118 | @onxinteriors | 81.4K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 119 | @lar.cabral | 2.5M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor;  |
| 120 | @revestindoacasa | 120.4K | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Auth.Eng. 64.3K |
| 121 | @reevcon | 1M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Reeves Connelly |

### B - Luxury Homes / Luxury Real Estate (35)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @greathousesandestates | 633.9K | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Great Houses & Estates; Auth.Eng. 13.8K |
| 2 | @jasonoppenheim | 1.6M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Jason Oppenheim (Selling Sunset) |
| 3 | @stylarc | 1.6M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; 'STYLARC / Luxury Architecture'; Embed zeigt '2M followers' (Rundung) |
| 4 | @binghatti | 1.8M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Developer Dubai |
| 5 | @cheapoldhouses | 3M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Cheap Old Houses |
| 6 | @lake_country_log_homes | 1.2M | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor;  |
| 7 | @damacofficial | 514.5K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor; DAMAC Properties |
| 8 | @sobharealty | 228.6K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor;  |
| 9 | @danubeproperties | 387.2K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor;  |
| 10 | @new.heights.real.estate | 41.5K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor;  |
| 11 | @realtoronaharley | 337.2K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor;  |
| 12 | @ellingtondubai | 122.9K | [HA architecture-urban-design-united-arab-emirates](https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/) | HypeAuditor; Ellington Properties |
| 13 | @tigerpropertiesae | 260.3K | [HA architecture-urban-design-united-arab-emirates](https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/) | HypeAuditor;  |
| 14 | @ukestates | 319.1K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor; UK Estates & Properties |
| 15 | @property_london | 438K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 16 | @themodernhouse | 893.7K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor; The Modern House (Makler) |
| 17 | @katy_campbell_house_hunter | 230.1K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 18 | @country_house_obsession | 272.8K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 19 | @reschio | 1.7M | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor; Estate, Hotel & Houses |
| 20 | @ssa.realestate | 157.8K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 21 | @larskruessel | 102.6K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor; Immobilien & Hausbau |
| 22 | @lydia_geldmacher | 83.7K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor; Immobilien Hamburg |
| 23 | @ryanserhant | 3M followers | [IG-Embed DZU_GwjO1sk](https://www.instagram.com/reel/DZU_GwjO1sk/embed/captioned/) | Embed; Reel 8.4M Views (Topic-Seite) |
| 24 | @gautamsinghania99 | 12M followers | [IG-Embed DVfSb-Jkk-a](https://www.instagram.com/reel/DVfSb-Jkk-a/embed/captioned/) | Embed; Unternehmer, Reel ueber Immobilienprojekt 48.7M Views; kein reiner Immo-Account |
| 25 | @clarazrd | 297K | [IG-Reel DMYHlSWuqZK](https://www.instagram.com/reel/DMYHlSWuqZK/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); NYC-Maklerin; Reel 72.1M Views |
| 26 | @theluxuryhomeshow | 2M | [IG-Reel DBvoA6IIZqo](https://www.instagram.com/reel/DBvoA6IIZqo/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 5.8M |
| 27 | @tuesday_leroux | 1M | [IG-Reel DLNhRhFykn0](https://www.instagram.com/reel/DLNhRhFykn0/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 7.8M |
| 28 | @navarealtygroup | 2M | [IG-Reel DLJJ4R-Ajvd](https://www.instagram.com/reel/DLJJ4R-Ajvd/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1M |
| 29 | @jameseditioncom | 167K | [IG-Reel CmKT2FMvofs](https://www.instagram.com/reel/CmKT2FMvofs/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); JamesEdition; Reel 679K |
| 30 | @verandaestatehomes | 371K | [IG-Reel DSxrSKakvV9](https://www.instagram.com/reel/DSxrSKakvV9/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.8M |
| 31 | @thehouserealty | 265K | [IG-Reel DWbYY55k3v4](https://www.instagram.com/reel/DWbYY55k3v4/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 2.9M |
| 32 | @barnesrealty | 391K | [IG-Reel DSQJLXYikmU](https://www.instagram.com/reel/DSQJLXYikmU/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet);  |
| 33 | @royashabboui | 191K | [IG-Reel C_qsri6hBKL](https://www.instagram.com/reel/C_qsri6hBKL/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet);  |
| 34 | @realtordenisbibik | 91K | [IG-Reel DKHkvBlOzX7](https://www.instagram.com/reel/DKHkvBlOzX7/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Miami |
| 35 | @corcoransunshine | 34K | [IG-Reel CyMU7yQRVIA](https://www.instagram.com/reel/CyMU7yQRVIA/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1M |

### C - Architektur- & Designmedien (39)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @architectanddesign | 8.4M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Architecture & Design; Auth.Eng. 25.4K |
| 2 | @art_dailydose | 22.8M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Kunst+Architektur-Aggregator; Auth.Eng. 58K |
| 3 | @accidentallywesanderson | 1.9M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; AWA |
| 4 | @howthingsarebuilld | 8.5M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Auth.Eng. nur 1.6K; erscheint auch auf AI-Architecture-Topic-Seiten |
| 5 | @studio.drift | 653.9K | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor; Installationskunst |
| 6 | @eccellenzaitaliana | 603.2K | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor;  |
| 7 | @archdigest | 11.3M | [HA diy-design](https://hypeauditor.com/top-instagram-diy-design/) | HypeAuditor; Architectural Digest; Auth.Eng. 22.8K |
| 8 | @vogueliving | 3M | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor;  |
| 9 | @tmagazine | 1.4M | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor;  |
| 10 | @zha.world | 1.6M | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor; Zaha Hadid Architects |
| 11 | @archimarathon | 577.1K | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor;  |
| 12 | @ninosbuildings | 503.4K | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor;  |
| 13 | @itisartime | 710.4K | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor;  |
| 14 | @houseandgardenuk | 2.4M | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 15 | @homesandgardensofficial | 790.2K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 16 | @granddesignstv | 287.8K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 17 | @greatbritisharchitecture | 483.5K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 18 | @architecture_candy | 215.9K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor;  |
| 19 | @designmuseum | 619.4K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor; auch hafi Designers |
| 20 | @archiproducts | 1M | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 21 | @apartamentomagazine | 467K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 22 | @cabanamagazine | 529.3K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 23 | @castles_and_palaces | 212.3K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 24 | @meetmyproject | 268.7K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 25 | @valerioolgiati | 219.9K | [HA architecture-urban-design-italy](https://hypeauditor.com/top-instagram-architecture-urban-design-italy/) | HypeAuditor;  |
| 26 | @baunetz | 126.9K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 27 | @gestalten | 251.7K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 28 | @ifdesign | 246.7K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 29 | @architectsnotarchitecture | 216.2K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 30 | @lookingup_architecture | 212K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 31 | @catchcato | 78.3K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 32 | @vitradesignmuseum | 247.1K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 33 | @archi.duha | 326.2K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor;  |
| 34 | @admiddleeast | 350.5K | [HA architecture-urban-design-united-arab-emirates](https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/) | HypeAuditor; AD Middle East; auch hafi Designers |
| 35 | @d3dubai | 246.7K | [HA architecture-urban-design-united-arab-emirates](https://hypeauditor.com/top-instagram-architecture-urban-design-united-arab-emirates/) | HypeAuditor;  |
| 36 | @revistaed | 134.6K | [HA architecture-urban-design-chile](https://hypeauditor.com/top-instagram-architecture-urban-design-chile/) | HypeAuditor;  |
| 37 | @designboom | 4M followers | [IG-Embed DMdzxzsup8T](https://www.instagram.com/reel/DMdzxzsup8T/embed/captioned/) | Embed (verifiziert-Badge), 17,300 posts |
| 38 | @milkdecoration_magazine | 467.6K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi Designers |
| 39 | @the.archart | 244.6K | [hafi graphic-design](https://hafi.pro/top/most-followed-instagram/graphic-design) | hafi Graphic Design; Architecture & Design Educator |

### D - AI-Architektur-Creator (25)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @aiforarchitects | 1.2M | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor; Ahmet Eren Keskin; Embed-DB 1M; Top-Reel 34.7M Views |
| 2 | @ti.fu | 272K followers | [IG-Embed C1ofaiFM95o](https://www.instagram.com/reel/C1ofaiFM95o/embed/captioned/) | Embed, verifiziert; 510 posts; Caption 'Parametric Design and Artificial Intelligence'; Identitaet Tim Fu ESTIMATED |
| 3 | @archibible | 220K followers | [IG-Embed DLI3AbXsnNC](https://www.instagram.com/reel/DLI3AbXsnNC/embed/captioned/) | Embed; 1,206 posts; Reel 14.3M (midjourney-architecture) |
| 4 | @matitectura | 507K followers | [IG-Embed DGvmymOMdST](https://www.instagram.com/reel/DGvmymOMdST/embed/captioned/) | Embed; 'Bringing old ruins back to life with the help of AI' |
| 5 | @theimagehs | 137K followers | [IG-Embed DNisARex_K2](https://www.instagram.com/reel/DNisARex_K2/embed/captioned/) | Embed; Tools Midjourney/Magnific/Hailuo; Reel 5.6M |
| 6 | @anderalencar | 478K followers | [IG-Embed C2N6luRLzhO](https://www.instagram.com/reel/C2N6luRLzhO/embed/captioned/) | Embed, verifiziert; Caption 'Visualization' - klassische ArchViz, AI-Nutzung nicht belegt |
| 7 | @buildcraft.hq | 890K followers | [IG-Embed DW6LdVcDGeh](https://www.instagram.com/reel/DW6LdVcDGeh/embed/captioned/) | Embed; 'Future of Architectural Excellence'; Reel 9.2M; AI-Status ESTIMATED |
| 8 | @elitebuildhq | 2M followers | [IG-Embed DW4-fMTiB96](https://www.instagram.com/reel/DW4-fMTiB96/embed/captioned/) | Embed; 'Living Garden Garage'; Reel 24M; Topic ai-generated-house |
| 9 | @refikanadol | 1.1M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor Arch; AI/Data-Art |
| 10 | @aipagedaily | 3.1M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor Arch; Auth.Eng. nur 1.7K |
| 11 | @juve3dstudio | 3.5M | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor Arch #2; 3D-Studio, AI-Status UNKNOWN |
| 12 | @predmet_ai | 446.5K | [hafi ai-tech](https://hafi.pro/top/most-followed-instagram/ai-tech) | hafi AI & Tech; im Projekt-DB Topic ai-render Reel 9.9M |
| 13 | @urban_lifestyle_lab | UNKNOWN | [IG-Reel DTwE4CFjKFK](https://www.instagram.com/reel/DTwE4CFjKFK/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 3M Views; Follower nicht erhoben |
| 14 | @montani3d | UNKNOWN | [IG-Reel DUannSokdQD](https://www.instagram.com/reel/DUannSokdQD/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 946K Views; Follower nicht erhoben |
| 15 | @ohneis652 | UNKNOWN | [IG-Reel DJCTsDzPJQ_](https://www.instagram.com/reel/DJCTsDzPJQ_/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 693K Views; Follower nicht erhoben |
| 16 | @about.archi.ai | UNKNOWN | [IG-Reel DW4ikbfiYl6](https://www.instagram.com/reel/DW4ikbfiYl6/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 374K Views; Follower nicht erhoben |
| 17 | @rendair.ai | UNKNOWN | [IG-Reel DM7kNwKB-QA](https://www.instagram.com/reel/DM7kNwKB-QA/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 556K Views; Follower nicht erhoben |
| 18 | @creatoarquitectos | UNKNOWN | [IG-Reel DZaAHDMRcrd](https://www.instagram.com/reel/DZaAHDMRcrd/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 377K Views; Follower nicht erhoben |
| 19 | @ioscapes | UNKNOWN | [IG-Reel DIJuOLftp2z](https://www.instagram.com/reel/DIJuOLftp2z/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 381K Views; Follower nicht erhoben |
| 20 | @architectcha | UNKNOWN | [IG-Reel DQCC9iNiuAS](https://www.instagram.com/reel/DQCC9iNiuAS/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 978K Views; Follower nicht erhoben |
| 21 | @design.input | UNKNOWN | [IG-Reel Cwxf5cmsoSX](https://www.instagram.com/reel/Cwxf5cmsoSX/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 900K Views; Follower nicht erhoben |
| 22 | @kheer_rvt | UNKNOWN | [IG-Reel DPuHH28jJm7](https://www.instagram.com/reel/DPuHH28jJm7/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 1.2M Views; Follower nicht erhoben |
| 23 | @vkuoo | UNKNOWN | [IG-Reel DYCXsDBs_Ya](https://www.instagram.com/reel/DYCXsDBs_Ya/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 552K Views; Follower nicht erhoben |
| 24 | @ant.archviz | UNKNOWN | [IG-Reel DKUtUceS7XW](https://www.instagram.com/reel/DKUtUceS7XW/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 329K Views; Follower nicht erhoben |
| 25 | @amirsaeedvadie | UNKNOWN | [IG-Reel DQqkiEPjJzF](https://www.instagram.com/reel/DQqkiEPjJzF/) | Projekt-DB 04_reel_database.csv; AI-/Future-Architektur-Topic-Seite, Top-Reel 433K Views; Follower nicht erhoben |

### E - AI-Interior-Creator/-Pages (25)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @siyad_abdali | 4M | [IG-Embed C9SiQc8S9xq](https://www.instagram.com/reel/C9SiQc8S9xq/embed/captioned/) | Projekt-DB 04_reel_database.csv (raw accounts); Top-Reel 282M (AI-codiert); Topics ai-house-design/dream-room |
| 2 | @ifonly.ai | 1M followers | [IG-Embed C--Al6UA6GE](https://www.instagram.com/reel/C--Al6UA6GE/embed/captioned/) | Embed; 419 posts; 'AI-generated video (Midjourney - Magnific'; Reel 136M |
| 3 | @soothenests | 2M | [IG-Embed DBWhf0koR7_](https://www.instagram.com/reel/DBWhf0koR7_/embed/captioned/) | Projekt-DB 04_reel_database.csv (raw accounts); Reel 45.1M; Topic ai-cozy-cabin |
| 4 | @sunt_mrr | 2M followers | [IG-Embed DNS1_gYMh2a](https://www.instagram.com/reel/DNS1_gYMh2a/embed/captioned/) | Embed; 728 posts; #midjourney; Reel 24.5M |
| 5 | @cozyzen.ai | 498K followers | [IG-Embed C-RyNNZMIaO](https://www.instagram.com/reel/C-RyNNZMIaO/embed/captioned/) | Embed; 2,305 posts; Reel 4.1M |
| 6 | @drcozyvibes | 584K followers | [IG-Embed C87NQHRtm6B](https://www.instagram.com/reel/C87NQHRtm6B/embed/captioned/) | Embed; 978 posts; Reel 155M (AI-codiert, nicht offengelegt) |
| 7 | @luxuriatetouche | 4M | [IG-Reel DI9Q70Uo8fB](https://www.instagram.com/reel/DI9Q70Uo8fB/) | Projekt-DB 04_reel_database.csv; AI-codiert; Reel 9.7M |
| 8 | @homebyhyla | 168K followers | [IG-Embed C25OoI1IRag](https://www.instagram.com/reel/C25OoI1IRag/embed/captioned/) | Embed; Caption #render3d - evtl. klassisches Rendering; Reel 28.6M |
| 9 | @iz__designs | 109K followers | [IG-Embed C6rOLbLriyx](https://www.instagram.com/reel/C6rOLbLriyx/embed/captioned/) | Embed; 'Design & Render' - AI nicht belegt; Reel 21.9M |
| 10 | @theraj_interior | 148K | [IG-Reel DTrgOnZk3v-](https://www.instagram.com/reel/DTrgOnZk3v-/) | Projekt-DB 04_reel_database.csv |
| 11 | @nemoza_interiors | 96K | [IG-Reel DV9K7tciJ0p](https://www.instagram.com/reel/DV9K7tciJ0p/) | Projekt-DB 04_reel_database.csv |
| 12 | @luxhilspace | 71K | [IG-Reel DYW4iAlN-YX](https://www.instagram.com/reel/DYW4iAlN-YX/) | Projekt-DB 04_reel_database.csv |
| 13 | @nesthome.03 | 39K | [IG-Reel DYfXRE8hEx6](https://www.instagram.com/reel/DYfXRE8hEx6/) | Projekt-DB 04_reel_database.csv; AI-codiert |
| 14 | @insmultiverse | 79K followers | [IG-Reel DMPZzYxNF_b](https://www.instagram.com/reel/DMPZzYxNF_b/) | Projekt-DB 04_reel_database.csv; Topics ai-house/future-houses-2050 |
| 15 | @nomadatoast | UNKNOWN | [IG-Reel DGQc37kNcJ7](https://www.instagram.com/reel/DGQc37kNcJ7/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 2.4M (ai-virtual-staging) Views; Follower nicht erhoben |
| 16 | @prinzessavideo_ai | UNKNOWN | [IG-Reel DSIaDRLjGMU](https://www.instagram.com/reel/DSIaDRLjGMU/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 3.3M Views; Follower nicht erhoben |
| 17 | @homemorph | UNKNOWN | [IG-Reel DRwOVkBDl8n](https://www.instagram.com/reel/DRwOVkBDl8n/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 997K Views; Follower nicht erhoben |
| 18 | @alinarsenova | UNKNOWN | [IG-Reel DUxO1KOjaWF](https://www.instagram.com/reel/DUxO1KOjaWF/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 870K Views; Follower nicht erhoben |
| 19 | @cozy_cabin_diaries | UNKNOWN | [IG-Reel DZ_JYrbhmDc](https://www.instagram.com/reel/DZ_JYrbhmDc/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 733K Views; Follower nicht erhoben |
| 20 | @rain.nest | UNKNOWN | [IG-Reel DYPD2_JEzhy](https://www.instagram.com/reel/DYPD2_JEzhy/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 1M Views; Follower nicht erhoben |
| 21 | @journey.to_serenity | UNKNOWN | [IG-Reel DCZpxj-t48e](https://www.instagram.com/reel/DCZpxj-t48e/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 467K Views; Follower nicht erhoben |
| 22 | @dshousetransformation | UNKNOWN | [IG-Reel DSXf1Yzj91c](https://www.instagram.com/reel/DSXf1Yzj91c/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 4.1M Views; Follower nicht erhoben |
| 23 | @lena_nichi_art | UNKNOWN | [IG-Reel DXMw4QLjB35](https://www.instagram.com/reel/DXMw4QLjB35/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 6M (ai-cozy-cabin) Views; Follower nicht erhoben |
| 24 | @naturesms_for_u | UNKNOWN | [IG-Reel DJM1L1SyU0x](https://www.instagram.com/reel/DJM1L1SyU0x/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 2.5M Views; Follower nicht erhoben |
| 25 | @imaginativemike | UNKNOWN | [IG-Reel DHGy6WZOH7p](https://www.instagram.com/reel/DHGy6WZOH7p/) | Projekt-DB 04_reel_database.csv; AI-Interior-Topic-Seite, Top-Reel 931K Views; Follower nicht erhoben |

### F - Dream Homes / Future Homes (28)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @luxurydreamhub | 1M | [IG-Reel DOHJ3rMgVna](https://www.instagram.com/reel/DOHJ3rMgVna/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 8.2M; 16 Reels im Sample |
| 2 | @wayup_media | 941K | [IG-Reel DQ4OUB3Di0Y](https://www.instagram.com/reel/DQ4OUB3Di0Y/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 22.7M |
| 3 | @exploringdreamhomes | 177K | [IG-Reel DUWxMeTCn65](https://www.instagram.com/reel/DUWxMeTCn65/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Topics ai-generated-house/dream-house |
| 4 | @thetrillionairelife | 13M | [IG-Reel C-GK8yJyZjT](https://www.instagram.com/reel/C-GK8yJyZjT/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert 'Car shaped villas'; Reel nur 1.4M |
| 5 | @naturesms | 10M | [IG-Reel DOcrXxqknf7](https://www.instagram.com/reel/DOcrXxqknf7/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Top-Reel im Sample nur 1.3M |
| 6 | @luxuryhouseview | 389K | [IG-Reel DOExDYCiEYm](https://www.instagram.com/reel/DOExDYCiEYm/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); futuristic-house Topics |
| 7 | @luxuriatehomes | 803K | [IG-Reel DLaOzlesmzc](https://www.instagram.com/reel/DLaOzlesmzc/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert |
| 8 | @miladeshtiyaghi | 642K | [IG-Reel Da714ebtLOp](https://www.instagram.com/reel/Da714ebtLOp/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet);  |
| 9 | @uniqchalets | 684K | [IG-Reel DdJPLxqMGaP](https://www.instagram.com/reel/DdJPLxqMGaP/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 5M |
| 10 | @idw.design | 318K | [IG-Reel DPoAX_tkiWR](https://www.instagram.com/reel/DPoAX_tkiWR/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); future-home |
| 11 | @capsulecastle004 | 246K | [IG-Reel DZMA3SHRsy-](https://www.instagram.com/reel/DZMA3SHRsy-/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Kapselhaus-Hersteller; Reel 5.7M |
| 12 | @astralserenity | 222K | [IG-Reel C24_SYQxzLT](https://www.instagram.com/reel/C24_SYQxzLT/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 7.2M |
| 13 | @inside_142 | 211K | [IG-Reel C9HhYw3MmE_](https://www.instagram.com/reel/C9HhYw3MmE_/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 6.2M |
| 14 | @elarch.studio | 540K | [IG-Reel C_5u72pxVBx](https://www.instagram.com/reel/C_5u72pxVBx/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); 3D-Render; Reel 15.5M |
| 15 | @containerhouseplans | 15K | [IG-Reel DTF5mohEWJQ](https://www.instagram.com/reel/DTF5mohEWJQ/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert; Reel 738K |
| 16 | @archived.dreams | 808.1K | [hafi designers](https://hafi.pro/top/most-followed-instagram/designers) | hafi Designers 'Archived Dreams' |
| 17 | @somewhereiwouldliketolive | 810.4K | [HA architecture-urban-design-united-states](https://hypeauditor.com/top-instagram-architecture-urban-design-united-states/) | HypeAuditor |
| 18 | @french_exterior | 955.2K | [HA architecture-urban-design](https://hypeauditor.com/top-instagram-architecture-urban-design/) | HypeAuditor 'French Art de Vivre' |
| 19 | @koto_cabins | 199.9K | [HA architecture-urban-design-united-kingdom](https://hypeauditor.com/top-instagram-architecture-urban-design-united-kingdom/) | HypeAuditor |
| 20 | @alpine.spaces | 104.9K | [HA architecture-urban-design-germany](https://hypeauditor.com/top-instagram-architecture-urban-design-germany/) | HypeAuditor |
| 21 | @containershome.cl | 447.7K | [HA architecture-urban-design-chile](https://hypeauditor.com/top-instagram-architecture-urban-design-chile/) | HypeAuditor; Auth.Eng. 59 |
| 22 | @majestic_manors_assam | UNKNOWN | [IG-Reel DKlpwIsBsfB](https://www.instagram.com/reel/DKlpwIsBsfB/) | Projekt-DB 04_reel_database.csv; dream-/future-home-Topic, Top-Reel 6.2M Views; Follower nicht erhoben |
| 23 | @fortune.sketches | UNKNOWN | [IG-Reel C_gOckLuO36](https://www.instagram.com/reel/C_gOckLuO36/) | Projekt-DB 04_reel_database.csv; dream-/future-home-Topic, Top-Reel 3.8M Views; Follower nicht erhoben |
| 24 | @lvrannx | UNKNOWN | [IG-Reel DM3fWa6M8e9](https://www.instagram.com/reel/DM3fWa6M8e9/) | Projekt-DB 04_reel_database.csv; dream-/future-home-Topic, Top-Reel 3.3M Views; Follower nicht erhoben |
| 25 | @designxdani | UNKNOWN | [IG-Reel DV-CtiaDrrN](https://www.instagram.com/reel/DV-CtiaDrrN/) | Projekt-DB 04_reel_database.csv; dream-/future-home-Topic, Top-Reel 1.7M Views; Follower nicht erhoben |
| 26 | @hm_architecture078 | UNKNOWN | [IG-Reel DXRMLZVjWUC](https://www.instagram.com/reel/DXRMLZVjWUC/) | Projekt-DB 04_reel_database.csv; dream-/future-home-Topic, Top-Reel 3.9M Views; Follower nicht erhoben |
| 27 | @architectkhyatisaini | UNKNOWN | [IG-Reel DXUIBEajIwd](https://www.instagram.com/reel/DXUIBEajIwd/) | Projekt-DB 04_reel_database.csv; dream-/future-home-Topic, Top-Reel 5M Views; Follower nicht erhoben |
| 28 | @veerhomesjaipur | UNKNOWN | [IG-Reel DPswds-k8kt](https://www.instagram.com/reel/DPswds-k8kt/) | Projekt-DB 04_reel_database.csv; dream-/future-home-Topic, Top-Reel 3.5M Views; Follower nicht erhoben |

### G - Luxury Lifestyle mit Interior-/Hotel-Anteil (30)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @goodlife | 3.3M | [HA luxury](https://hypeauditor.com/top-instagram-luxury/) | HypeAuditor Luxury; GOODLIFE |
| 2 | @heritageclass | 1.2M | [HA luxury](https://hypeauditor.com/top-instagram-luxury/) | HypeAuditor Luxury; Auth.Eng. 27.6K |
| 3 | @luxrysociety | 520.9K | [HA luxury](https://hypeauditor.com/top-instagram-luxury/) | HypeAuditor Luxury; Luxury Society; Auth.Eng. 38.7K |
| 4 | @luxurysouqls | 2.5M | [HA luxury](https://hypeauditor.com/top-instagram-luxury/) | HypeAuditor Luxury;  |
| 5 | @tomclaeren | 1.1M | [HA luxury](https://hypeauditor.com/top-instagram-luxury/) | HypeAuditor Luxury; Monaco |
| 6 | @luxuryindubai | 314.6K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor Luxury;  |
| 7 | @richboysworld.in | 551.1K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor Luxury;  |
| 8 | @karim.luxury | 876.4K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor Luxury;  |
| 9 | @palazzoversacedubai | 663.9K | [HA luxury-united-arab-emirates](https://hypeauditor.com/top-instagram-luxury-united-arab-emirates/) | HypeAuditor Luxury; Hotel |
| 10 | @ralphlaurenhome | 1M | [HA luxury-united-states](https://hypeauditor.com/top-instagram-luxury-united-states/) | HypeAuditor Luxury; Marke, Interior |
| 11 | @beautifulhotels | 6M followers | [IG-Embed C7PFB2NIp-e](https://www.instagram.com/reel/C7PFB2NIp-e/embed/captioned/) | Embed, verifiziert; 9,121 posts; Reel 5.4M |
| 12 | @travellingthroughtheworld | 3.4M | [hafi hotels](https://hafi.pro/top/most-followed-instagram/hotels) | hafi Hotels #1 / Travel #1 |
| 13 | @hotelsfr | 443.1K | [hafi hotels](https://hafi.pro/top/most-followed-instagram/hotels) | hafi Hotels |
| 14 | @myfavhotels | 135.6K | [hafi hotels](https://hafi.pro/top/most-followed-instagram/hotels) | hafi Hotels 'Hotels & More' |
| 15 | @worldpitou | 594.3K | [hafi travel](https://hafi.pro/top/most-followed-instagram/travel) | hafi Travel 'Luxury Travel' |
| 16 | @milliondollamotive | 290.3K | [hafi motivational](https://hafi.pro/top/most-followed-instagram/motivational) | hafi Motivational - Luxus-Motivation, Interior-Anteil UNKNOWN |
| 17 | @wifizei | 329K followers | [IG-Embed DDnJ5x6tfYm](https://www.instagram.com/reel/DDnJ5x6tfYm/embed/captioned/) | Embed; 402 posts; 'Future Life #luxury #success #wealth'; Reel 8.6M |
| 18 | @millionaire1ife | 172K followers | [IG-Embed DLAjTvmIRre](https://www.instagram.com/reel/DLAjTvmIRre/embed/captioned/) | Embed; nur 4 posts; 'Your life in 3 years'; Reel 4.1M |
| 19 | @nouxri | 120K followers | [IG-Embed DQ20_hkCG1S](https://www.instagram.com/reel/DQ20_hkCG1S/embed/captioned/) | Embed; 227 posts; Dubai-Pool; Reel 7.5M |
| 20 | @aureliestory | 3M | [IG-Reel DcmBZJINnDz](https://www.instagram.com/reel/DcmBZJINnDz/) | Projekt-DB 04_reel_database.csv; Reel 4.9M |
| 21 | @lisi.quietdiaries | 153K | [IG-Reel DQzx59pEsqO](https://www.instagram.com/reel/DQzx59pEsqO/) | Projekt-DB 04_reel_database.csv; quiet-luxury; Reel 22.7M |
| 22 | @thevisualpoetflavia | 145K | [IG-Reel DDj-lyuOm2b](https://www.instagram.com/reel/DDj-lyuOm2b/) | Projekt-DB 04_reel_database.csv; quiet-luxury |
| 23 | @karinaross | 184K | [IG-Reel DYY0vCUIjmH](https://www.instagram.com/reel/DYY0vCUIjmH/) | Projekt-DB 04_reel_database.csv; quiet-luxury |
| 24 | @millionaire.vibes__ | UNKNOWN | [IG-Reel DEXdiSOCLz0](https://www.instagram.com/reel/DEXdiSOCLz0/) | Projekt-DB 04_reel_database.csv; luxury-lifestyle/dubai/monaco-Topic, Top-Reel 2.1M Views; Follower nicht erhoben |
| 25 | @richbynature09 | UNKNOWN | [IG-Reel DR94Qu_ktrH](https://www.instagram.com/reel/DR94Qu_ktrH/) | Projekt-DB 04_reel_database.csv; luxury-lifestyle/dubai/monaco-Topic, Top-Reel 1.9M Views; Follower nicht erhoben |
| 26 | @lavishsocietie | UNKNOWN | [IG-Reel DS2t7OKk2Jk](https://www.instagram.com/reel/DS2t7OKk2Jk/) | Projekt-DB 04_reel_database.csv; luxury-lifestyle/dubai/monaco-Topic, Top-Reel 1M Views; Follower nicht erhoben |
| 27 | @7figurelives | UNKNOWN | [IG-Reel DS06JVuCDhd](https://www.instagram.com/reel/DS06JVuCDhd/) | Projekt-DB 04_reel_database.csv; luxury-lifestyle/dubai/monaco-Topic, Top-Reel 366K Views; Follower nicht erhoben |
| 28 | @luxvelosity | UNKNOWN | [IG-Reel DZXl1qqsDHl](https://www.instagram.com/reel/DZXl1qqsDHl/) | Projekt-DB 04_reel_database.csv; luxury-lifestyle/dubai/monaco-Topic, Top-Reel 430K Views; Follower nicht erhoben |
| 29 | @dubai._dreamer | UNKNOWN | [IG-Reel DH8ZgwQC7Yy](https://www.instagram.com/reel/DH8ZgwQC7Yy/) | Projekt-DB 04_reel_database.csv; luxury-lifestyle/dubai/monaco-Topic, Top-Reel 4.4M Views; Follower nicht erhoben |
| 30 | @mona.co98000 | UNKNOWN | [IG-Reel Dain7u4qfku](https://www.instagram.com/reel/Dain7u4qfku/) | Projekt-DB 04_reel_database.csv; luxury-lifestyle/dubai/monaco-Topic, Top-Reel 7.3M Views; Follower nicht erhoben |

### H - Kleine Accounts mit extremen Reel-Views (51)

| # | Handle | Follower (Text) | Quelle | Notiz |
|---|---|---|---|---|
| 1 | @ai.poly_ | 14K followers | [IG-Embed DYoyUS9NlAr](https://www.instagram.com/reel/DYoyUS9NlAr/embed/captioned/) | Embed; 30 posts; AI-Video (RU); Reel 147M Views - Inhalt nicht Interior |
| 2 | @polliviva | 48K followers | [IG-Embed Daa8AwIMNMt](https://www.instagram.com/reel/Daa8AwIMNMt/embed/captioned/) | Embed; 264 posts; AI-Video (syntx); Reel 97.2M - Inhalt nicht Interior |
| 3 | @_jeni__va | 9K followers | [IG-Embed DVOqMmzCRgK](https://www.instagram.com/reel/DVOqMmzCRgK/embed/captioned/) | Embed; 'My simple room'; Reel 10.3M (dream-room) |
| 4 | @proud_and_property | 50K followers | [IG-Embed DW3n03NCOri](https://www.instagram.com/reel/DW3n03NCOri/embed/captioned/) | Embed; 2,592 posts; Immobilien PK; Reel 13.5M |
| 5 | @ki.render | 19K followers | [IG-Embed CwTBiWeK6uY](https://www.instagram.com/reel/CwTBiWeK6uY/embed/captioned/) | Embed; '3dsMax, Corona Render' (kein AI); Reel 7.3M auf ai-interior-Topic |
| 6 | @sireen.design | 94K followers | [IG-Embed C3abe85I_vw](https://www.instagram.com/reel/C3abe85I_vw/embed/captioned/) | Embed; '3D max, vray' (kein AI); Reel 7.4M |
| 7 | @architecturaai_ | 23K followers | [IG-Embed DUVBmy5DcTo](https://www.instagram.com/reel/DUVBmy5DcTo/embed/captioned/) | Embed; 833 posts; 'FREE EBOOK IN BIO ... AI interiors'; Reel 5.4M |
| 8 | @visionbuildofficial | 50K followers | [IG-Embed DW8_CcQESn8](https://www.instagram.com/reel/DW8_CcQESn8/embed/captioned/) | Embed; 'Craziest Snake Tower Ever Built in the USA'; Reel 6.6M |
| 9 | @lovedwellstudio | 74K followers | [IG-Embed C20JhAHLOGJ](https://www.instagram.com/reel/C20JhAHLOGJ/embed/captioned/) | Embed; 'AI Design by @lovedwellstudio'; Reel 6.7M |
| 10 | @leylaa__asgarii | 60K followers | [IG-Embed C8ry_2ENAqh](https://www.instagram.com/reel/C8ry_2ENAqh/embed/captioned/) | Embed; Architektin, 3D-Render; Reel 5.8M |
| 11 | @kratosdigitalarts | 90K followers | [IG-Embed DaM-d0KTKUQ](https://www.instagram.com/reel/DaM-d0KTKUQ/embed/captioned/) | Embed; PicsArt-AI; Reel 17.1M |
| 12 | @facade_designn | 47K followers | [IG-Embed DS5GYPmAESA](https://www.instagram.com/reel/DS5GYPmAESA/embed/captioned/) | Embed; Schlangen-Wolkenkratzer; Reel 2.1M |
| 13 | @luxuviouz | 16K followers | [IG-Reel DBQ3T40sm6V](https://www.instagram.com/reel/DBQ3T40sm6V/) | Projekt-DB 04_reel_database.csv; Dubai; Reel 3.9M |
| 14 | @jen.casanovas.ibiza | 5K | [IG-Reel DVGaPhTDQO8](https://www.instagram.com/reel/DVGaPhTDQO8/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 11.7M, real footage |
| 15 | @ekam_sandhu_fitness | 1K | [IG-Reel DdbN1FLJIXF](https://www.instagram.com/reel/DdbN1FLJIXF/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 2.3M dream-house, real footage |
| 16 | @creativ_storiess | 1K | [IG-Reel DXW8mQ4jP7S](https://www.instagram.com/reel/DXW8mQ4jP7S/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.2M |
| 17 | @alshifarealtor.dxb | 47K | [IG-Reel DdMPxaloS3f](https://www.instagram.com/reel/DdMPxaloS3f/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Makler Dubai; Reel 54.3M |
| 18 | @cocinasintegralesjv | 32K | [IG-Reel DJo4QLktHJz](https://www.instagram.com/reel/DJo4QLktHJz/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Kuechenbauer; Reel 24M |
| 19 | @soldbytyler | 12K | [IG-Reel DWzPi-IgcuY](https://www.instagram.com/reel/DWzPi-IgcuY/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Makler; Reel 8.8M |
| 20 | @processlabstudio | 10K | [IG-Reel DV1TGjKguzz](https://www.instagram.com/reel/DV1TGjKguzz/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert; Reel 4.6M |
| 21 | @husnain_g13_properties | 4K | [IG-Reel DcWTQ_jiSCi](https://www.instagram.com/reel/DcWTQ_jiSCi/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.7M |
| 22 | @eigsticonstruction | 8K | [IG-Reel DU9gCl-Du3V](https://www.instagram.com/reel/DU9gCl-Du3V/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 3M |
| 23 | @northern___bear | 29K | [IG-Reel DZ-j3rtI5AA](https://www.instagram.com/reel/DZ-j3rtI5AA/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 10.4M |
| 24 | @philkeandesigngroup | 11K | [IG-Reel DSGQeRiEvi1](https://www.instagram.com/reel/DSGQeRiEvi1/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 3.7M |
| 25 | @pune_designer | 15K | [IG-Reel DW2355fiMXs](https://www.instagram.com/reel/DW2355fiMXs/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 4.5M |
| 26 | @ayeshadeary5 | 16K | [IG-Reel C-APLc-yI85](https://www.instagram.com/reel/C-APLc-yI85/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 4.4M |
| 27 | @pmkpod | 23K | [IG-Reel DUNWW5NiL9l](https://www.instagram.com/reel/DUNWW5NiL9l/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 4.6M |
| 28 | @gumaanresorts | 22K | [IG-Reel DK7LpKhtdth](https://www.instagram.com/reel/DK7LpKhtdth/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 4.4M |
| 29 | @jonaways | 84K | [IG-Reel DXPCR1cE_iL](https://www.instagram.com/reel/DXPCR1cE_iL/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 16.6M |
| 30 | @girardteam | 34K | [IG-Reel C9FRKpjOSoi](https://www.instagram.com/reel/C9FRKpjOSoi/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 6.3M |
| 31 | @tiatinn_ | 8K | [IG-Reel CuHTr3rJ5pJ](https://www.instagram.com/reel/CuHTr3rJ5pJ/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.4M |
| 32 | @sara.interiorstudio | 10K | [IG-Reel DdHegfQM6DU](https://www.instagram.com/reel/DdHegfQM6DU/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert; Reel 1.6M |
| 33 | @ghazale_siami | 34K | [IG-Reel DExUPqcsNfS](https://www.instagram.com/reel/DExUPqcsNfS/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Topic ai-interior; Reel 5.3M |
| 34 | @abdullahaslanoglu_ | 68K | [IG-Reel C-ks822KeDg](https://www.instagram.com/reel/C-ks822KeDg/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 10.2M |
| 35 | @craftlab2050 | 50K | [IG-Reel Dcnh66ERGzY](https://www.instagram.com/reel/Dcnh66ERGzY/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert; Reel 7.1M |
| 36 | @theelitespaces | 22K | [IG-Reel C-M7VT2POMk](https://www.instagram.com/reel/C-M7VT2POMk/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Theme-Page; Reel 3.1M |
| 37 | @pentarkdesign | 15K | [IG-Reel DVK9k-mEa_S](https://www.instagram.com/reel/DVK9k-mEa_S/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 2.1M |
| 38 | @bic_trading | 14K | [IG-Reel DSnW9BIksbc](https://www.instagram.com/reel/DSnW9BIksbc/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.9M |
| 39 | @petersoncabinetworks | 29K | [IG-Reel DAGRW5NPUo1](https://www.instagram.com/reel/DAGRW5NPUo1/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 2.7M |
| 40 | @erfan_padiav | 71K | [IG-Reel DLffL8pNp5j](https://www.instagram.com/reel/DLffL8pNp5j/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); 3D-Render auf ai-interior-designer-Topic; Reel 2.3M |
| 41 | @recastliving | 47K | [IG-Reel DZnSu7zoJeQ](https://www.instagram.com/reel/DZnSu7zoJeQ/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert; Reel 1.4M |
| 42 | @buildsinblack | 55K | [IG-Reel DZx1gIBofW9](https://www.instagram.com/reel/DZx1gIBofW9/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert; Reel 1.3M |
| 43 | @rodnova_installation_ | 41K | [IG-Reel DaxVmNVR4R1](https://www.instagram.com/reel/DaxVmNVR4R1/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); AI-codiert; Reel 1.1M |
| 44 | @sourcedinteriorsdesign | 21K | [IG-Reel DctONdERiHk](https://www.instagram.com/reel/DctONdERiHk/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 2.1M |
| 45 | @timberwit | 17K | [IG-Reel DcypdnmoFJq](https://www.instagram.com/reel/DcypdnmoFJq/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.4M |
| 46 | @lvclosetdesign | 62K | [IG-Reel DQ77Qe_gSdS](https://www.instagram.com/reel/DQ77Qe_gSdS/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 2.2M |
| 47 | @roomify.design | 62K | [IG-Reel DVrk07ojSsm](https://www.instagram.com/reel/DVrk07ojSsm/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.7M |
| 48 | @riya_realtor | 62K | [IG-Reel DK2Kx6tyuNR](https://www.instagram.com/reel/DK2Kx6tyuNR/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 3M |
| 49 | @balidroomvillas | 14K | [IG-Reel DJnfJsWPbAI](https://www.instagram.com/reel/DJnfJsWPbAI/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 1.5M |
| 50 | @longingtocomehome | 130K | [IG-Reel DGQYtSbOz6S](https://www.instagram.com/reel/DGQYtSbOz6S/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Reel 36M (knapp ueber 100K) |
| 51 | @paulmarkkitchens | 304K | [IG-Reel DBKFpVDoZzM](https://www.instagram.com/reel/DBKFpVDoZzM/) | Projekt-DB 04_reel_database.csv (oeffentl. Embed, gerundet); Outdoor-Kuechen-Marke; Reel 135M; mittelgross, aber vpf ~444 |

## Faktencheck (automatisiert)

Prüfung am 2026-09-25 (WebFetch plus Roh-HTML derselben URL per curl; bei Aussagen, die ausdrücklich der Projekt-DB zugeschrieben sind, zusätzlich `04_reel_database.csv`). Andere Quellen wurden nicht zur Rettung von Aussagen herangezogen.

| # | Aussage (Kurzform) | Ergebnis | Begründung |
|---|---|---|---|
| 1 | hafi Interior Top 50: want.zamora 2.3M, interiordesignideas 1.8M, interiordesign.addicts 1.2M, theworldofinteriors 1.2M, Nr. 50 rosario.interiores 100.2K; „updated daily“; keine Kategorisierungsmethode | CONFIRMED | Roh-HTML der hafi-Seite zeigt #1–#4 und #50 mit exakt diesen Werten, den Satz „Our ranking is updated daily…“ und keinen Methodik-Text (WebFetch rendert die Tabelle leer, „Top 0“). |
| 2 | HA Architecture global: Ranking nach „genuine audiences and their authentic engagement“; art_dailydose 22.8M/58K, architectanddesign 8.4M/25.4K, howthingsarebuilld 8.5M/1.6K, aipagedaily 3.1M/1.7K, ihsansamhoun.interiors 152.6K/83.7K | CONFIRMED | Methodik-Satz und alle fünf Follower-/Auth.-Eng.-Paare stehen wörtlich auf der Seite. |
| 3 | Kategorie-Rauschen: claudeai 2.1M, muzammilhb 4.8M (global), unesco 3.5M (US-Liste) | CONFIRMED | Zitierte US-Seite: claudeai 2.1M (Rang 22) und unesco 3.5M (Rang 48). muzammilhb 4.8M („Quran Reciter“) steht nur in der globalen Liste (URL aus Aussage 2), nicht auf der zitierten US-URL. |
| 4 | HA DIY & Design global: archdigest 11.3M/22.8K, joannagaines 13.7M, farahjmerhi 7.5M, 5.min.crafts 49.7M/3.4K | CONFIRMED | Alle Werte exakt auf der Seite (Ränge 4, 7, 3, 6). |
| 5 | HA DIY & Design DE: westwingcom 8.7M/781, haus_plan_b 1.2M/120.9K, mi.interieur 1.3M, live.like.archi 1.1M, homeofmerve 459.4K; keine AI-Interior-Page | CONFIRMED | Alle Werte exakt auf der Seite. Die 50 Handles enthalten keinen erkennbaren AI-Interior-Account (Einordnung per Handle/Name). |
| 6 | aiforarchitects („Architect & Interior Designer“) in HA US: 1.2M / 2.4K; DB-Top-Reel 34.7M | CONFIRMED | HA US Rang 42: „Ahmet Eren Keskin \| Architect & Interior Designer“, 1.2M / 2.4K. DB: Reel DHBihXfMPDA mit 34.7M (steht nicht auf der HA-Seite, nur in der DB). |
| 7 | ti.fu-Embed: „272K followers“, „510 posts“, verifiziert, Caption „Parametric Design and Artificial Intelligence“, Workshop mit @thepaacademy; Zuordnung zu Tim Fu offen | CONFIRMED | Embed zeigt genau diese Werte, das Badge und die Caption. Die Caption enthält „#timfu“, das ist ein Hinweis, aber kein Beleg der Identität. |
| 8 | matitectura: „507K followers“, „626 posts“, Caption „Ruins Reimagined … with the help of AI“ | CONFIRMED | Embed zeigt genau diese Werte und diese Caption (außerdem „Generated by @matitectura using MidJourney“). |
| 9 | archibible: „220K followers“, „1,206 posts“, „Shop link in bio … DM for commissions“; DB-Reel 14.3M auf midjourney-architecture | CONFIRMED | Embed bestätigt Follower, Posts und Caption. DB: Reel DLI3AbXsnNC, 14.3M, Topic midjourney-architecture. |
| 10 | ifonly.ai: „1M followers“, „419 posts“, Caption „Art/Prompts by @ifonly.ai & @sunt_mrr AI-generated video (Midjourney • Magnific…“; DB 136M auf ai-house-design | CONFIRMED | Embed bestätigt Follower, Posts und Caption („…Magnific AI • Immersity)“). DB: 136M, Topic ai-house-design. Das Embed zeigt nur Likes (3,268,113), keine Views. |
| 11 | drcozyvibes: „584K followers“, „978 posts“, Reel „Rainy Day Reflections…“ 155M Views, in der DB AI-codiert, Caption ohne AI | CONFIRMED | Embed bestätigt 584K, 978 und die Caption ohne AI-Bezug. 155M und „ai_generated“ stehen nur in der DB. Das Embed zeigt 6,127,779 Likes und keine Views. Die Zahlen-Tabelle zitiert für 155M nur das Embed; richtig wäre die DB. |
| 12 | sunt_mrr 2M/728/#midjourney/24.5M; elitebuildhq 2M/317/24M; cozyzen.ai 498K/2,305; buildcraft.hq 890K/225/9.2M | NOT_CONFIRMED | Die zitierte URL (DNS1_gYMh2a) belegt nur sunt_mrr: „2M followers“, „728 posts“, #midjourney. Keine Views (1,562,484 Likes). elitebuildhq, cozyzen.ai und buildcraft.hq kommen auf dieser URL nicht vor. Die DB-Werte stimmen überein (DW4-fMTiB96, C-RyNNZMIaO, DW6LdVcDGeh), sind aber nicht die zitierte Quelle. |
