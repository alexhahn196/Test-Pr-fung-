# Q06 – Fallstudien: Gesichtslose KI-Themenseiten zu Interior, Architektur, Luxusvillen und Cozy Rooms. Was hat funktioniert, wie wurde verdient, was ist gescheitert?

**Stand der Recherche:** 2026-09-25 · **Sprache:** Deutsch, Originalzitate auf Englisch · **Ergänzt:** `q01_instagram_platform_rules.md` (Plattformregeln), `q03_sponsors_brand_deals.md` (Sponsoren), `q05_competitor_lists.md` (Wettbewerber)

**Methode und Einschränkungen (bitte vor dem Lesen beachten):**
- Das **WebSearch-Budget der Session war bei Beginn dieser Teilrecherche schon aufgebraucht** (200/200). Websuchen waren deshalb nicht möglich, und ich habe sie auch nicht über Suchmaschinen per WebFetch nachgebaut. Gearbeitet habe ich mit direkt abgerufenen, bekannten URLs (WebFetch), der YouTube-Suche und YouTube-Metadaten bzw. -Transkripten über NexLev sowie mit öffentlichen Instagram-Embed-Seiten.
- **Nicht abrufbar:** reddit.com/old.reddit.com (Tool-seitig blockiert), nymag.com (blockiert), PromptBase, Etsy, Fiverr, Social Blade (HTTP 403), Snopes (HTTP 402), das Instagram-Profil (HTTP 429, danach keine weiteren Profilabrufe). Gumroad lieferte eine leere Trefferseite, und der NexLev-Instagram-Video-Analyzer war im Tageslimit (15/15). **Reddit-, Indie-Hackers-, X- und Medium-Belege fehlen deshalb fast vollständig.** Das ist eine echte Lücke, keine Aussage darüber, dass es solche Beiträge nicht gibt.
- **Projektdaten:** Das Repo enthält einen am 2026-09-25 erhobenen Datensatz öffentlicher Instagram-Themenseiten (`data/processed/*.csv`, `data/raw/accounts/profile_*.json`). View-Zahlen daraus sind als „Projektdaten“ gekennzeichnet. Ich habe sie nicht selbst neu abgerufen, außer wo „selbst geprüft“ dabeisteht. Profil-JSONs aus `data/raw/accounts/` stammen von einem anderen Pipeline-Schritt und sind als solche zitiert.
- **Keine Logins, keine Umgehung von Paywalls oder Rate-Limits.**
- Insgesamt über 60 Abrufe, Suchen und Transkript- bzw. Metadaten-Abfragen.

**Status-Tags:**
- `[VERIFIED]`: selbst in der genannten Quelle gesehen. Das heißt nur, dass die Quelle es so sagt, nicht, dass es stimmt.
- `[ESTIMATED]`: eigene Ableitung oder Rechnung, oder Projektdaten, die ich nicht neu abgerufen habe
- `[THIRD-PARTY ESTIMATE]`: jede Einkommens- oder Umsatzangabe Dritter, **auch Selbstauskünfte** von Gründern oder Creatorn
- `[UNKNOWN]`: nicht belegbar

---

## 1. Fragestellung

Welche belastbaren Fallbeispiele gibt es für gesichtslose, KI-generierte Instagram-Themenseiten zu Interior, Architektur, Luxury Homes, Dream Homes und Cozy Rooms?

1. **Wachstum:** Wie schnell, mit welchen View-Zahlen, und wann lag das Zeitfenster?
2. **Formate:** Welche haben funktioniert (Cozy-Rain-Bedroom, Transformation, Luxusvilla mit Ortsangabe, Fantasy-Häuser, Bau-Timelapse …)?
3. **Monetarisierung:** Prompt-Packs, Gumroad/Etsy, Kurse, KI-Render-Services, Virtual Staging, B2B, Brand Deals, Affiliate, Cross-Platform-Funnel.
4. **Gegenbelege:** Stagnation, Sättigung, Einstufung als „unoriginal“, Publikums-Backlash („AI slop“), Plattform- und Rechtsrisiken.

---

## 2. Kernbefunde

### 2.1 Überblick in 12 Punkten

1. **Die großen KI-Cozy- und Dream-Home-Hits häufen sich im Zeitfenster Juli bis Oktober 2024.** Beispiele aus den Projektdaten: @siyad_abdali 282 Mio. Views (29.08.2024), @drcozyvibes 155 Mio. (02.07.2024), @ifonly.ai 136 Mio. (22.08.2024), @soothenests 45,1 Mio. (20.10.2024). Das Datum ist jeweils aus dem Shortcode dekodiert. `[ESTIMATED – Projektdaten; Datum per Shortcode-Dekodierung]`
2. **Die Accounts sind reichweitenstark, aber hit-getrieben.** Einzelne Reels liegen um 2–3 Zehnerpotenzen über den übrigen Reels desselben Accounts. Beispiele: @drcozyvibes 155 Mio. vs. 421 Tsd./251 Tsd., @cozyzen.ai 4,1 Mio. (2024) vs. 27 Tsd./18,3 Tsd. (2026). `[ESTIMATED – Projektdaten]`
3. **Seit 2025 schneiden KI-Reels im Projekt-Sample schlechter ab als Nicht-KI-Reels.** 2024: Median 1,6 Mio. (KI, n=14) vs. 548 Tsd. (Nicht-KI). 2025: 221 Tsd. vs. 383 Tsd. 2026: 102 Tsd. vs. 245 Tsd. Gleichzeitig stieg der KI-Anteil unter den gecodeten Reels von 3,3 % (2023) auf 31,9 % (2026). Das deutet auf Sättigung hin, ist aber durch Aktualitäts- und Auswahl-Bias verzerrt. `[ESTIMATED – eigene Auswertung der Projektdaten]`
4. **Einzelne kleine Accounts brechen 2026 trotzdem noch durch**, vor allem mit **Fantasy-, Humor- oder „unmöglichen“ Motiven** statt realistischer Cozy-Zimmer. Beispiele: @polliviva (48K Follower) 97,2 Mio. Views am 05.07.2026 (Cartoon-Badezimmer, KI offengelegt), @processlabstudio (10K) 4,6 Mio., @craftlab2050 (50K) 7,1 Mio. `[ESTIMATED – Projektdaten]`
5. **@soothenests (2M Follower, 2.119 Posts) ist der Referenzfall für KI-Cozy-Bedrooms.** Das Top-Reel hat 2.083.003 Likes und 6.514 Kommentare (selbst geprüft) und hat keine KI-Kennzeichnung in der Caption. **Bis September 2026 hat der Account auf Threads von Interiors auf allgemeine KI-Tool-Showcases umgeschwenkt** (Partner-Post `#dreaminapartner` mit nur 460 Views und 2 Likes). Monetarisierung ist nur als Collab-Kontakt und Tool-Partnerschaft belegt. `[VERIFIED]`
6. **Der klarste belegte Geldweg ist B2B:** KI-Visuals als Lead-Funnel für hochpreisige Aufträge. @aiforarchitects (1M Follower) verlinkt eine Website mit „Architectural Design“, „Interior Design“, „Concept Design“ usw. und schreibt unter Reels *"For private commissions and inquiries"*. Preise werden nicht genannt. `[VERIFIED]`
7. **Kurse und Tutorials sind nachweislich ein Geschäftsmodell rund um die Nische.** Tim Fu verkaufte einen Midjourney-Architekturkurs (150 EUR, 100 Plätze). Tutorial-YouTuber verkaufen Communities und Kurse zu genau diesen Formaten. `[VERIFIED]` Ihre Umsatzbehauptungen sind unbelegt und teils rechnerisch falsch: *"$150 a day, which is about $45,000 a month"*. `[THIRD-PARTY ESTIMATE]`
8. **SaaS statt Theme-Page:** Pieter Levels (Interior AI) nennt selbst *"40K, 50K a month"* (Aug. 2024). RoomGPT wirbt mit *"Used by over 4 million people"*. Virtual Staging AI wirbt mit *"10,000+ users"* und ab $16 pro Monat. `[THIRD-PARTY ESTIMATE / Selbstauskunft]`
9. **Prompt-Packs, Gumroad und Etsy:** **Für KI-Interior-Theme-Pages konnte ich keinen einzigen verifizierten Verkaufsbeleg finden** (Marktplätze 403 bzw. leer, Suchbudget erschöpft). Beobachtet wurden nur kostenlose Prompt-Lead-Magnete per Kommentar→DM (@soothenests auf Threads). `[UNKNOWN]`
10. **Cross-Platform-Funnels konvertieren schwach.** Beispiele: @drcozyvibes (584K IG, Top-Reel 155 Mio. Views) hat auf YouTube 1.130 Abonnenten und 234.008 Gesamtaufrufe. @nostalgicraindrops (selbstgenannt 673K IG) hat auf YouTube 6.270 Abonnenten und 155.098 Aufrufe. `[VERIFIED]`
11. **Publikums-Backlash ist dokumentiert, gerade im Wohnbereich:**
    - Pinterest reagierte auf *"a backlash among Pinterest's loyal customer base"* mit KI-Labels (30.04.2025) und einer Einstellung, KI-Inhalte in *"beauty, art, fashion, and home décor"* zu reduzieren (16.10.2025).
    - Auf Facebook posteten 43 von 125 untersuchten KI-Spam-Seiten KI-Häuser oder -Hütten.
    - KI-geschönte Immobilienfotos lösten 2026 in Detroit eine Vertrauensdebatte aus.

    `[VERIFIED]`
12. **Die Plattformregeln treffen typische Theme-Page-Taktiken:**
    - Nicht monetarisierbar sind *"static images played in succession"*, *"Content that loops"* und *"unoriginal"* Inhalte.
    - Accounts mit überwiegend unoriginalem Content verlieren seit 30.04.2026 auch bei Fotos und Karussells die Empfehlungen.

    Tutorials raten dagegen zum Entfernen von Wasserzeichen und zum Loopen von Clips. `[VERIFIED]`

---

### 2.2 Fallstudien einzelner Accounts

**@soothenests (Cozy AI Bedrooms und Cabins, ca. 2M Follower)**
- Embed-Seite des Reels DBWhf0koR7_ (selbst geprüft am 2026-09-25): „2M followers“, „2,119 posts“, **2.083.003 Likes, 6.514 Kommentare**. Caption: *"Raindrops on My Window, Euphoria in My Soul: Luxury Bedroom Bliss"* mit #cozybedroom #cozyapartment #euphoria. Die Caption enthält keinen KI-Hinweis, keinen Link und kein Produkt. [Quelle](https://www.instagram.com/reel/DBWhf0koR7_/embed/captioned/) `[VERIFIED]`
- Views laut Projektdaten: DBWhf0koR7_ 45,1 Mio. (20.10.2024), DOvkVSNCDEW 8,1 Mio. (18.09.2025), DDR89qOo08t 5,8 Mio. (07.12.2024), C_P-6KmOGt9 2,5 Mio. (29.08.2024). Das älteste gesehene Reel ist vom 29.08.2024. Der Account erreichte also in **grob 1–2 Jahren** 2M Follower. Das Startdatum des Accounts ist unbekannt. `[ESTIMATED – Projektdaten, Datum per Shortcode]`
- Format: Standbild-nahe Luxus-Schlafzimmer oder Hütte mit Fenster zu Regen, Schnee oder Meer, stimmungsvoller Titel im Stil „Euphoria …“, 2–3 Hashtags, kein CTA. `[VERIFIED – Captions]`
- Threads-Post vom 14.09.2026 (selbst geprüft): *"Comment 'Dreamina' and I'll send you the exact prompt + link. Seedance 2.5 is getting all the hype, but this video was made entirely with Seedance 2.0."* mit #dreamina **#dreaminapartner**. Engagement: **2 Likes, 1 Repost, 2 Shares, 460 Views**. [Quelle](https://www.threads.com/@soothenests/post/DdS6abyEgZ6) `[VERIFIED]` → Das ist eine Tool-Partnerschaft. Der Schwenk weg von Interiors erreicht auf Threads aber kaum Publikum.
- Laut Projekt-Profil (`data/raw/accounts/profile_soothenests.json`, Quelle: Threads-Bio) lautet die Bio *"AI-Powered Content Creation … For Collabs / Partnerships"* mit Gmail-Kontakt. **Dieselbe Kontakt-Adresse** steht auch in der Threads-Bio von **@cozyzen.ai** (*"For promos Dm"*). Das deutet auf einen Betreiber mit **mehreren Cozy-KI-Seiten** hin, also ein Portfolio-Modell. Die Adresse wird hier bewusst nicht wiedergegeben. `[ESTIMATED – Projektdaten, nicht selbst neu abgerufen]`
- Zwei winzige YouTube-Kanäle heißen ebenfalls „Soothe Nests“ und beschreiben sich als „AI-Inspired Cozy Vibes“. Der eine hat 9 Abonnenten und 61 Views, der andere 4 Abonnenten und 49 Views, dazu *"For Promos & Ads DM"*, Land Indien. [NexLev/YouTube](https://www.youtube.com/channel/UCmLIJIzOIZHLLJhJTQGg2Jw), [2](https://www.youtube.com/channel/UCrR6fn1Gm_zVGstBR9sEqig). **Ob sie zum IG-Betreiber gehören oder Trittbrettfahrer sind, ist UNKNOWN.** `[VERIFIED Kanaldaten / UNKNOWN Zuordnung]`
- **Eine Einkommensangabe oder ein Interview wurde nicht gefunden.** `[UNKNOWN]`

**@drcozyvibes (Cozy Cabins und Bedrooms im Regen)**
- Embed des Reels C87NQHRtm6B (selbst geprüft): „584K“ Follower, „978 posts“, **6.127.798 Likes, 18.043 Kommentare**. Caption: *"Rainy Day Reflections: Comfort Bed, Melodic Drops, and a Scenic Window #cozycabin #RainyDayVibes"*. [Quelle](https://www.instagram.com/reel/C87NQHRtm6B/embed/captioned/) `[VERIFIED]`
- Views laut Projektdaten: 155 Mio. (02.07.2024). Die anderen gesichteten Reels liegen bei 421 Tsd. und 251 Tsd. → **Ein einziger Mega-Hit hat nur 584K Follower gebracht.** Die View-to-Follower-Konversion ist schwach. `[ESTIMATED]`
- YouTube-Funnel „Dr Cozy Vibes (Healing Your Soul)“: **1.13K Abonnenten, 109 Videos, 234.008 Aufrufe**, gegründet 22.12.2020, UK. [NexLev/YouTube](https://www.youtube.com/@drcozyvibes) `[VERIFIED]`

**@siyad_abdali (Biophile, verträumte Schlafzimmer; 4M Follower)**
- Embed des Reels C_Pf1dboaeJ (selbst geprüft): „4M“, „2,110 posts“, **11.986.598 Likes**. [Quelle](https://www.instagram.com/reel/C_Pf1dboaeJ/embed/captioned/) `[VERIFIED]`
- Views laut Projektdaten: 282 Mio. (29.08.2024) und 109 Mio. (11.07.2024). Spätere Reels liegen bei 5,1 Mio., 4,0 Mio., 2,3 Mio. und 316 Tsd. (20.01.2026). `[ESTIMATED]`
- Monetarisierung, Presseberichte oder ein Interview: **nicht gefunden** (YouTube-Suche ohne Treffer, Websuche nicht möglich). `[UNKNOWN]`

**@aiforarchitects (KI-Luxusvillen als Auftrags-Funnel; 1M Follower)**
- Embed des Reels DHBihXfMPDA (selbst geprüft): „1M followers“, „513 posts“, **2.890.579 Likes, 9.506 Kommentare**. Caption: *"Mansion in Dubai: Experience ultra-modern elegance and unparalleled luxury with our black concept design. By @aiforarchitects"*. Views laut Projektdaten 34,7 Mio. (10.03.2025). [Quelle](https://www.instagram.com/reel/DHBihXfMPDA/embed/captioned/) `[VERIFIED / Views ESTIMATED]`
- Website-Leistungen (selbst geprüft): *"ARCHITECTURAL DESIGN"*, *"INTERIOR DESIGN"*, *"CONCEPT DESIGN"* (*"From initial floor plans to stunning 3D renderings, we translate your ideas into reality"*), *"LANDSCAPE DESIGN"*, *"PROJECT CONSULTING"*. **Keine Preise, kein Hinweis auf KI** auf der Leistungsseite. [aiforarchitects.co/services](https://aiforarchitects.co/services/) `[VERIFIED]`
- Laut Projekt-Profil enden andere Reel-Captions mit *"For private commissions and inquiries: www.aiforarchitects.co | WhatsApp …"*. LinkedIn nennt „founded 2023“ und „2-10 employees“ (loginbeschränkt). `[ESTIMATED – Projektdaten]`
- Die Domain aiforarchitects**.com** ist geparkt und steht zum Verkauf. Der Betrieb läuft über **.co**. `[VERIFIED]`
- **Bewertung:** Das ist das deutlichste Beispiel für „KI-Visual → B2B-Auftrag“. Ob Aufträge tatsächlich zustande kommen und zu welchem Volumen, ist **UNKNOWN**.

**@ifonly.ai (surreale oder essbare Häuser; 1M Follower)**
- Embed des Reels C--Al6UA6GE (selbst geprüft): „1M followers“, „419 posts“, **3.268.122 Likes, 18.007 Kommentare**. Caption: *"If only 'home sweet home' meant living in a tiramisu house. Art/Prompts by @ifonly.ai & @sunt_mrr — AI-generated video (Midjourney • Magnific AI • Immersity)"*. Views laut Projektdaten 136 Mio. (22.08.2024). [Quelle](https://www.instagram.com/reel/C--Al6UA6GE/embed/captioned/) `[VERIFIED / Views ESTIMATED]`
- **Gegenbeleg zur These „KI-Offenlegung killt Reichweite“:** Dieses offengelegte KI-Video gehört zu den größten Hits im Datensatz. `[ESTIMATED – Einzelfall]`

**Weitere Accounts aus den Projektdaten (nicht selbst neu abgerufen)** `[ESTIMATED]`
- **@cozyzen.ai:** 498K Follower laut Reel-Embed. Reels: 4,1 Mio. (05.08.2024), 27 Tsd. (28.08.2026), 18,3 Tsd. (24.06.2026). Threads-Posts enden mit *"Created completely with AI."* Das ist offengelegte KI mit **deutlichem Reichweitenabfall**.
- **@calm_neststudio:** 156K Follower. Reels: 13,1 Mio. (02.01.2026) mit Caption *"Relaxing Gentle Rain, for longer rain videos on my Youtube"*, 172 Tsd., 28,3 Tsd. Ein YouTube-Funnel ist angekündigt, der Kanal aber nicht bestätigt.
- **@luxurydreamhub:** 1M Follower. Jüngere Embeds haben 2.315 bzw. 12.014 Likes gegenüber 302.997 bei einem älteren Hit. Laut Profil-Notiz *"reach is hit-driven"*. Keine Monetarisierung sichtbar.
- **@naturesms:** 10M Follower (rustikale Cozy-Cabins, Fragen-Captions *"who would you most like to live with …"*), gesichtete Reels zwischen 133 Tsd. und 1,3 Mio. Das Tutorial von AI-pocalypse (2023, siehe 2.4) beschreibt eine ungenannte Cozy-KI-Seite mit *"almost 10 million followers"*. **Ob es derselbe Account ist, ist UNKNOWN.**

**@nostalgicraindrops (Regen- und Cozy-Ambient mit KI)**
- YouTube-About (selbst geprüft): *"VFX & AI By @angelmaderazo on IG"*, *"Check out my IG page, @nostalgicraindrops - with 673K Followers on Instagram!"*, dazu **6.27K Abonnenten, 109 Videos, 155.098 Aufrufe**, gegründet 25.07.2023, Philippinen. [NexLev/YouTube](https://www.youtube.com/@NostalgicRaindrops) `[VERIFIED; IG-Followerzahl = Selbstauskunft]`

---

### 2.3 Wachstumsgeschichten und Zeitbedarf (Creator-Aussagen)

- **Tim Fu (KI-Architektur, damals bei Zaha Hadid Architects)**, Podcast ArchiTech Network #44 (04.06.2023, Transkript selbst geprüft):
  - Zum Wachstum: *"July of 2022, I had about a few hundred followers. And ever since then … it's not even been a year, but I had steady progress. It wasn't a overnight sensation type of thing."* Der Host sagt: *"you passed 100,000 a few weeks ago"*. → **Von einigen Hundert auf über 100K in weniger als 11 Monaten.**
  - Zur Strategie, Abgrenzung durch Stil: *"what is lacking is a someone who is trying to produce realistic architecture that was extremely rational but beautiful … amongst this chaos, this ocean of crazy AI things"*.
  - Zur Datenpflege: *"I have actually an Excel spreadsheet … every image that I did post, I put the views on the side"*.
  - Zu Plateaus: *"when it slows down I plateau, I understand this … trajectory no longer works, I have to switch it up"*.
  - Zur Monetarisierung über Lehre, Talks und Konferenzen: *"that's also including teaching at PA, um doing conferences and talks"*.
  - [YouTube](https://www.youtube.com/watch?v=cSMqgh1hNww) `[VERIFIED – Selbstauskunft]`
- **Tim Fus Kurs** „Midjourney Architecture 3.0“ bei Parametric Architecture, 14.–15.01.2023, 8 Stunden: Early-bird *"90 EUR (Available for first 10 seats)"*, *"105 EUR"*, General *"150 EUR"*, *"Total Seats: 100 Seats"*. Theoretischer Maximalumsatz bei Vollbelegung zum Normalpreis: < 15.000 EUR brutto, vor dem Anteil der Plattform. [Quelle](https://parametric-architecture.com/midjourney-architecture-3-0-studio-tim-fu/) `[VERIFIED Preise/Plätze; Umsatz ESTIMATED, tatsächliche Belegung UNKNOWN]`
- **Pieter Levels (Interior AI, SaaS statt Theme-Page)**, Lex Fridman #440 (20.08.2024):
  - Zu Umsatz und Alter: *"makes like 40K, 50K a month, and it's been like two years"*.
  - Zum Start: *"within a week, made 10K, 20K a month"*.
  - Zur Entstehung: Stable Diffusion sei *"really good at interior"*.
  - Vermarktung laut Transkript-Zusammenfassung vor allem über X/Twitter und Hacker News.
  - [Transkript](https://lexfridman.com/pieter-levels-transcript/) `[THIRD-PARTY ESTIMATE – Selbstauskunft]`
  - Levels’ Vorgängerprojekt **thishousedoesnotexist.org** (KI-Häuser im ArchDaily-Stil) bekam 2022 einen ArchDaily-Artikel, siehe [ArchDaily, 07.09.2022](https://www.archdaily.com/988606). `[VERIFIED]`
- **Theme-Page-Ökonomie allgemein** (nicht KI-, nicht Interior-spezifisch), Josh Ryan, 29.08.2024:
  - Verkaufte eigene Theme-Page, Monetarisierungsleiter „sponsored posts → affiliate → eigenes Business“.
  - Preisspanne für Sponsored Posts: von *"$10"* bis *"accounts charging over $11,000 per post"*.
  - Beispiel für Affiliate-Provision: *"product that pays $90 commission"*.
  - [YouTube](https://www.youtube.com/watch?v=B7tZw_EK35c) `[THIRD-PARTY ESTIMATE – Selbstauskunft]`

---

### 2.4 Formate, die funktioniert haben (belegt durch Hits und Tutorials)

1. **Cozy-Wetter-Fenster:** Schlafzimmer, Hütte oder Wohnzimmer mit Regen, Schnee oder Kamin, langsamer Schwenk, Ambient-Sound. Das ist das dominante Format der Mega-Hits von 2024 (soothenests, drcozyvibes, siyad_abdali, cozyzen.ai).
   - Das Tutorial von AI-pocalypse (25.11.2023, **560.286 Views**) beschreibt die Machart: KI-Standbild, Fenster ausschneiden, Green-Screen-Schnee und -Feuer, Keyframe-Schwenk im Format 9:16.
   - Zitat: *"I found out that they have almost 10 million followers and all these videos are getting tens of millions and sometimes even over 100 million views so it's safe to say that this page is making tens of thousands of dollars every month"*. [YouTube](https://www.youtube.com/watch?v=Ny9Q3zgcOv8)
   - `[VERIFIED Zitat; Einkommensaussage = THIRD-PARTY ESTIMATE, reine Spekulation des Tutorial-Autors]`
2. **Transformation vom leeren zum eingerichteten Raum** (Start-/End-Frame-Video). Tutorial von AiPerson (02.11.2025, **190.366 Views, 6.037 Likes**):
   - Zur Idee: *"The idea of the niche is to show an empty room, house, terrace, office or studio and then create a beautiful interior"*.
   - Zu Länge und Frequenz: *"Video duration 8 seconds is ideal"*, *"publish videos regularly and ideally two or three per day"*.
   - Zum Stil: *"Preferably something expensive or luxury style"*.
   - [YouTube](https://www.youtube.com/watch?v=RD0Z9G9HCk0) `[VERIFIED]`
   - Auch luxurydreamhub schwenkt 2026 auf solche „Transformation“-Reels um (Projektdaten). `[ESTIMATED]`
3. **KI-Bau-Timelapse** („From Empty Land to Mansion“). Tutorial von Grow with Ank (01.12.2025, **160.808 Views**): *"These 'satisfying' construction videos are blowing up on YouTube right now, getting millions of views"*. Auch hier wird ein Folgeformat angekündigt: *"AI Luxury House Tours"*. [YouTube](https://www.youtube.com/watch?v=jWthLwZJ0DY) `[VERIFIED Zitat; „millions of views“ = Behauptung]`
4. **Luxusvilla mit prestigeträchtigem Ortsbezug** (Dubai, Los Angeles, Miami) und langer Architektur-Caption, siehe aiforarchitects: 34,7 Mio. Views (Projektdaten). `[ESTIMATED]`
5. **Fantasy, unmögliche Häuser oder Humor:** Tiramisu-Haus (ifonly.ai, 136 Mio.), Cartoon-Bad (polliviva, 97,2 Mio., 2026), dazu „Pick-your-home“-Formate (yourfantasyhomes: *"which one is your new home ?"*). Im Projekt-Sample hat „fantasy_impossible“ den höchsten Median von 890 Tsd. Views, bei allerdings **n=14, niedriger Konfidenz**. `[ESTIMATED – Projektdaten]`
6. **Fragen-Captions** (*"Would You Hide Away Here During a Snowstorm?"*, *"What will you do in this cozy room?"*) und Mood-Titel sind durchgängig. Ein direkter Wirkungsnachweis fehlt. `[ESTIMATED]`

---

### 2.5 Monetarisierung – was ist belegt, was nicht?

| Modell | Evidenz | Status |
|---|---|---|
| **B2B-Aufträge** (Architektur/Interior-Design) über KI-Visuals | @aiforarchitects: Leistungsseite und Auftrags-CTA in Captions; keine Preise, kein Auftragsvolumen | Leistungen `[VERIFIED]`, Umsatz `[UNKNOWN]` |
| **Tool-Partnerschaft / Sponsored Content** | @soothenests `#dreaminapartner` (Threads, 14.09.2026) | `[VERIFIED]` |
| **Promo-/Collab-Anfragen per Bio** | soothenests *"For Collabs / Partnerships"*, cozyzen.ai *"For promos Dm"*, drcozyvibes *"looking for collaborations"* (Projektdaten/Threads) | `[ESTIMATED – Projektdaten]` |
| **Kurse / Communities / Coaching** | Tim Fu PA-Kurs 150 EUR, 100 Plätze. Tutorial-YouTuber verlinken Skool-, Whop- und Stan-Store-Kurse (AI Venture, AiPerson, Josh Ryan, AI-pocalypse: *"I grew my faceless YouTube channel from 0 to 70,000 subscribers in 4 months and I made a course"*) | Angebote `[VERIFIED]`, Umsätze `[UNKNOWN]` |
| **SaaS / KI-Render- und Staging-Tools** | Interior AI $49/$99/$199 pro Monat; *"40K, 50K a month"* (Levels). RoomGPT *"Used by over 4 million people"*. Virtual Staging AI *"10,000+ users"*, *"Starting at only $16 a month"*, Konkurrenz ab *"$20 for one photo"* | Preise `[VERIFIED]`, Umsätze `[THIRD-PARTY ESTIMATE]` |
| **Cross-Platform-Funnel** (IG → YouTube-Ambient-Kanal, AdSense) | drcozyvibes und nostalgicraindrops: YouTube 1,13K bzw. 6,27K Abonnenten trotz IG-Hits im zweistelligen bzw. dreistelligen Millionenbereich | `[VERIFIED]`, Konversion schwach |
| **Prompt-Packs, Gumroad, Etsy** | Nur kostenlose Prompt-DMs gesehen. YouTube-Titel *"Make Money online with ChatGPT 4 and Midjourney v5 with Interior Design on Etsy"* (2.770 Views, ca. 2023) verspricht *"$100000 on Etsy"*, ohne Beleg | `[UNKNOWN]` / `[THIRD-PARTY ESTIMATE]` |
| **Plattform-Bonus (Facebook)** | 404 Media zitiert ein Tutorial: *"Facebook now pays you $100 for 1,000 likes"*. Nicht von 404 verifiziert, gilt für Facebook | `[THIRD-PARTY ESTIMATE]` |
| **Theme-Page-Verkauf, Shoutouts** | Josh Ryan: Sponsored Posts von $10 bis über $11.000 pro Post; eigene Seite verkauft, Betrag im Transkript unklar | `[THIRD-PARTY ESTIMATE]` |

---

### 2.6 Gegenbelege: Scheitern, Sättigung, Backlash, Policy-Risiko

- **Facebook-KI-Spam mit Häusern und Hütten** (HKS Misinformation Review, 15.08.2024; arXiv 19.03.2024):
  - Datengrundlage: *"125 Facebook Pages that posted at least 50 AI-generated images each"*, *"mean follower count of 146,681 and a median of 81,000"*, zusammen *"hundreds of millions of exposures"*.
  - Themen: *"AI-generated houses or cabins (43 Pages)"*.
  - Eine Seite wechselte von einer Koch-Seite zu KI-Küchenbildern. Ein Post erreichte *"40 million views and 1.9 million interactions"*.
  - Häuser-Cluster verwiesen auf Seiten, die angeblich *"instructions on how to build them"* anboten (Content-Farm-Traffic).
  - Die meisten Kommentierenden bemerkten die KI nicht, aber *"a subset of comments include text or infographics alerting others and warning of scams"*.
  - [HKS](https://misinforeview.hks.harvard.edu/article/how-spammers-and-scammers-leverage-ai-generated-images-on-facebook-for-audience-growth/), [arXiv](https://arxiv.org/abs/2403.12838) `[VERIFIED]`
  - → **Reputationsrisiko:** KI-Häuser und -Hütten sind in Forschung und Presse als Spam-Genre etabliert.
- **404 Media (06.08.2024):** Die Facebook-Seite „Dream Home“ mit **113.000 Followern** bestand aus *"AI generated homes that look like roosters, giraffes, horses, and hummingbirds"*. Die Macher sitzen laut Artikel in Indien, Vietnam und auf den Philippinen, Anleitungen kursieren per YouTube und Telegram. [404 Media](https://www.404media.co/where-facebooks-ai-slop-comes-from/) `[VERIFIED]`
- **Pinterest-Backlash, direkt im Bereich Wohnen:**
  - 30.04.2025, TechCrunch: *"AI-generated Pins and other low-quality AI content — often referred to as 'AI slop' — have created a backlash among Pinterest's loyal customer base."* Pinterest führt Labels und KI-Klassifikatoren ein. [TechCrunch](https://techcrunch.com/2025/04/30/pinterest-launches-new-tools-to-fight-ai-slop/)
  - 16.10.2025: Nutzer können GenAI-Inhalte in *"beauty, art, fashion, and home décor"* reduzieren. [TechCrunch](https://techcrunch.com/2025/10/16/pinterest-adds-controls-to-let-you-limit-the-amount-of-ai-slop-in-your-feed/)
  - `[VERIFIED]`
  - → **Home décor gehört zu den ersten Kategorien, in denen eine große Plattform eine Abwahl von KI-Inhalten anbietet.** Ob Instagram einen vergleichbaren Regler hat, habe ich nicht geprüft. `[UNKNOWN]` Q01 zitiert Mosseri (Juli 2026) mit *"People who love AI content should be able to have a feed that's just AI town"*. Das Zitat habe ich nicht selbst gesehen, es stammt aus Q01.
- **Immobilien und Virtual Staging:** WDIV Detroit (02.03.2026). Ein KI-geschöntes Inseratsfoto eines Bungalows wurde in einem Social-Post mit der Realität verglichen und zog laut Bericht *"millions of views"* an. Eine Anwohnerin: *"It's beautiful, but it's AI … It looks fake. It looks like a painting."* Das Thema: *"trust, disclosure and the role of artificial intelligence in real estate marketing."* [YouTube/WDIV](https://www.youtube.com/watch?v=08zJd3gUbOs) `[VERIFIED]` → Das ist ein Risiko für B2B-Staging-Angebote. Der Anbieter Virtual Staging AI wirbt selbst mit *"Fully MLS compliant: No misrepresentation"*. `[VERIFIED – Werbeaussage]`
- **Instagram-Regeln gegen typische Taktiken:**
  - Nicht monetarisierbar sind *"Content that primarily displays static images played in succession"*, *"Content that loops and displays the same segment multiple times"*, *"Content that primarily displays still or moving images with overlaid text"* und *"Content that is unoriginal or reproduced without making meaningful enhancements"*. [Instagram Help](https://www.facebook.com/help/instagram/2635536099905516)
  - Seit 30.04.2026: *"Accounts that primarily post unoriginal content in photos or carousel posts, in addition to reels, will no longer be shown in places where we recommend content."* Außerdem *"75% of recommendations in the US now coming from original posts"*. Der Beitrag erwähnt **KI nicht**. [creators.instagram.com](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram)
  - `[VERIFIED]`
  - **Widerspruch zu Tutorials:** AI Venture (21.11.2024, 184.316 Views) empfiehlt, Wasserzeichen mit einem *"Watermark Remover"* zu entfernen und Clips zu loopen, weil *"Instagram's algorithm tends to favor videos that keep viewers around and looping your content is a clever way to hack this"*. [YouTube](https://www.youtube.com/watch?v=fBU50XlVE4o) `[VERIFIED]` → Wer nach verbreiteten Tutorials arbeitet, verletzt potenziell Monetarisierungsregeln.
- **Sättigung und Copycats:**
  - YouTube-Suchen zu „AI house“ liefern zahlreiche Kanäle („AI House World“, „AI Dream Homes“, „DreamBuild AI“, „Dream Ai Renovation 17“ …). Viele Shorts haben zweistellige bis niedrige vierstellige Views (z. B. „From Empty Land to an Ultra-Luxury Mansion“ 167 Views, „Abandoned hut to dream home“ 19 Views). `[VERIFIED – Stichprobe aus Suchergebnissen, nicht repräsentativ]`
  - Projektdaten: siehe Punkt 3 im Überblick. Dort hat KI den niedrigsten Median aller Produktionsarten: ai_generated **164.500** Views (n=156) gegenüber real_footage 276.000 und 3D-Render 402.500. Viral-Quote (≥5× Follower) 30 % vs. 38 %. `[ESTIMATED – Projektdaten]`
- **Schwenk statt Skalierung:** Das Aushängeschild @soothenests postet 2026 auf Threads KI-Tool-Showcases (Anime-Welten, iPhone-Werbespot, Tool-Partnerschaft) statt Interiors, mit sehr geringer Resonanz (460 Views). Das spricht dafür, dass der Betreiber die **Interior-Nische als Geldquelle nicht für ausreichend hält**. Diese Deutung ist meine eigene Interpretation. `[ESTIMATED]`
- **Unzuverlässige Einkommensbehauptungen:** AiPerson sagt *"The creator earns around $150 a day, which is about $45,000 a month in a houses niche"*. Rechnerisch ergeben $150/Tag nur ca. $4.500/Monat, die Angabe ist also um den Faktor 10 inkonsistent. Außerdem geht es um YouTube-Shorts-Monetarisierung, nicht um Instagram. [YouTube](https://www.youtube.com/watch?v=RD0Z9G9HCk0) `[THIRD-PARTY ESTIMATE – nachweislich inkonsistent]`
- **Urheberrechts- und Originalitätsrisiko bei Prompts:** Kapwing hat **4.929.594** Midjourney-Prompts ausgewertet. Zaha Hadid wird **63.103**-mal referenziert, Frank Lloyd Wright 13.361-mal. Illustrator Greg Rutkowski *"is also involved in a legal case against AI companies"*. [designboom, 27.10.2025](https://www.designboom.com/technology/from-zaha-hadid-wes-anderson-midjourney-most-copied-architects-artists-ai-10-27-2025/) `[VERIFIED – Sekundärquelle]`
- **Mockery- und Reaktionsgenre:** „I Recreated Ai Slop CRAFTS“ (HopeScope, **5.934.142 Views**, ca. April 2026) zeigt, dass die Abgrenzung von KI-„Slop“ selbst ein Massenformat ist. Bezieht sich auf Bastelarbeiten, nicht auf Interiors. [YouTube](https://www.youtube.com/watch?v=_n2IEbFJDao) `[VERIFIED Views; Übertragbarkeit ESTIMATED]`
- **Instagram-Einkommen mit KI-Bildern (Sekundär):** Wikipedia zitiert Max Read (NYMag, 25.09.2024): *"A medical student in India said he made thousands of dollars each month from low effort, AI-generated images on Instagram and Fanvue."* Das betrifft keine Interiors, und NYMag selbst war nicht abrufbar. [Wikipedia: AI slop](https://en.wikipedia.org/wiki/AI_slop) `[THIRD-PARTY ESTIMATE / Primärquelle UNKNOWN]`

---

## 3. Zahlen-Tabelle

| # | Kennzahl | Wert | Quelle (Datum) | Status |
|---|---|---|---|---|
| 1 | @soothenests Follower / Posts | 2M / 2,119 | IG-Embed DBWhf0koR7_ (abgerufen 2026-09-25) | VERIFIED |
| 2 | @soothenests Top-Reel Likes / Kommentare | 2,083,003 / 6,514 | IG-Embed DBWhf0koR7_ | VERIFIED |
| 3 | @soothenests Top-Reel Views | 45,1 Mio. (Post 20.10.2024) | Projektdaten `reels_unique.csv` | ESTIMATED |
| 4 | @soothenests Dreamina-Partnerpost (Threads) | 460 Views, 2 Likes | threads.com (14.09.2026) | VERIFIED |
| 5 | @drcozyvibes Follower / Posts | 584K / 978 | IG-Embed C87NQHRtm6B | VERIFIED |
| 6 | @drcozyvibes Top-Reel Likes / Kommentare | 6,127,798 / 18,043 | IG-Embed C87NQHRtm6B | VERIFIED |
| 7 | @drcozyvibes Top-Reel Views | 155 Mio. (02.07.2024) | Projektdaten | ESTIMATED |
| 8 | Dr Cozy Vibes YouTube | 1.13K Abos, 234,008 Aufrufe, 109 Videos | NexLev/YouTube (2026-09-25) | VERIFIED |
| 9 | @siyad_abdali Follower / Posts / Likes Top-Reel | 4M / 2,110 / 11,986,598 | IG-Embed C_Pf1dboaeJ | VERIFIED |
| 10 | @siyad_abdali Top-Reel Views | 282 Mio. (29.08.2024) | Projektdaten | ESTIMATED |
| 11 | @aiforarchitects Follower / Posts / Likes / Kommentare | 1M / 513 / 2,890,579 / 9,506 | IG-Embed DHBihXfMPDA | VERIFIED |
| 12 | @aiforarchitects Top-Reel Views | 34,7 Mio. (10.03.2025) | Projektdaten | ESTIMATED |
| 13 | @ifonly.ai Follower / Posts / Likes / Kommentare | 1M / 419 / 3,268,122 / 18,007 | IG-Embed C--Al6UA6GE | VERIFIED |
| 14 | @ifonly.ai Tiramisu-Haus Views | 136 Mio. (22.08.2024) | Projektdaten | ESTIMATED |
| 15 | Nostalgic Raindrops YouTube | 6.27K Abos, 155,098 Aufrufe; „673K Followers on Instagram“ (selbstgenannt) | NexLev/YouTube | VERIFIED / IG-Zahl Selbstauskunft |
| 16 | KI-Anteil an gecodeten Reels | 3,3 % (2023, n=30) → 22,6 % (2024, n=62) → 30,6 % (2025, n=170) → 31,9 % (2026, n=279) | Projektdaten `reels_cover_coded.csv`, eigene Auswertung | ESTIMATED |
| 17 | Median-Views KI vs. Nicht-KI | 2024: 1,6 Mio. vs. 548 Tsd.; 2025: 221 Tsd. vs. 383 Tsd.; 2026: 102 Tsd. vs. 245 Tsd. | Projektdaten, eigene Auswertung | ESTIMATED |
| 18 | Median-Views nach Produktion (gesamt) | ai_generated 164.500 (n=156); real_footage 276.000 (n=327); 3d_render 402.500 (n=42) | `stats/seg_production.csv` | ESTIMATED |
| 19 | KI-Offenlegung unter KI-Reels | 35 von 156 offengelegt (eigene Auswertung `reels_cover_coded.csv`). Die Segment-Statistik `seg_ai_disclosed.csv` nutzt eine andere Teilmenge mit n=8 offengelegten Reels. | Projektdaten | ESTIMATED |
| 20 | Tim Fu Followerwachstum | „a few hundred“ (Juli 2022) → „passed 100,000“ (ca. Mai 2023) | Podcast ATN #44 (04.06.2023) | VERIFIED (Selbstauskunft) |
| 21 | Tim Fu Kurs | 90/105/150 EUR; 100 Plätze; 8 h | parametric-architecture.com (Kurs 14.–15.01.2023) | VERIFIED |
| 22 | Interior AI Umsatz | „40K, 50K a month“; Start „10K, 20K a month“ | Lex Fridman #440 (20.08.2024) | THIRD-PARTY ESTIMATE |
| 23 | Interior AI Preise | $49 / $99 / $199 pro Monat (1.000 / 5.000 / 25.000 Designs) | interiorai.com (abgerufen 2026-09-25) | VERIFIED |
| 24 | RoomGPT Nutzer | „Used by over 4 million people“ | roomgpt.io (abgerufen 2026-09-25) | THIRD-PARTY ESTIMATE (Firmenangabe) |
| 25 | Virtual Staging AI | „10,000+ users“; „Starting at only $16 a month“ (6 Bilder) | virtualstagingai.app | THIRD-PARTY ESTIMATE / Preis VERIFIED |
| 26 | Facebook-KI-Spamseiten | 125 Seiten; 43 mit Häusern/Hütten; Ø 146.681 / Median 81.000 Follower | HKS Misinformation Review (15.08.2024) | VERIFIED |
| 27 | Viraler KI-Küchenpost (Facebook) | 40 Mio. Views, 1,9 Mio. Interaktionen | HKS (15.08.2024) | VERIFIED |
| 28 | Unconnected Posts im Facebook-Feed | 8 % (Q2 2021) → 24 % (Q3 2023) | HKS (15.08.2024) | VERIFIED |
| 29 | FB-Seite „Dream Home“ | 113.000 Follower | 404 Media (06.08.2024) | VERIFIED |
| 30 | „Facebook now pays you $100 for 1,000 likes“ | – | Tutorial-Zitat in 404 Media (06.08.2024) | THIRD-PARTY ESTIMATE |
| 31 | Instagram: Anteil Originalposts an US-Empfehlungen | 75 % | creators.instagram.com (30.04.2026) | VERIFIED |
| 32 | AI-pocalypse-Tutorial | 560.286 Views; Behauptung „almost 10 million followers“, „tens of thousands of dollars every month“ | YouTube (25.11.2023) | Views VERIFIED / Einkommen THIRD-PARTY ESTIMATE |
| 33 | AiPerson-Tutorial | 190.366 Views; „$150 a day … about $45,000 a month“ | YouTube (02.11.2025) | THIRD-PARTY ESTIMATE (inkonsistent) |
| 34 | Grow-with-Ank-Tutorial (KI-Bau-Timelapse) | 160.808 Views | YouTube (01.12.2025) | VERIFIED |
| 35 | Josh Ryan Sponsored-Post-Preise | $10 bis „over $11,000 per post“ | YouTube (29.08.2024) | THIRD-PARTY ESTIMATE |
| 36 | Kapwing Midjourney-Prompts | 4.929.594 Prompts; „Zaha Hadid“ 63.103 Nennungen | designboom (27.10.2025) | VERIFIED (sekundär) |
| 37 | WDIV-Bericht KI-Inseratsfoto | viraler Post mit „millions of views“; Video 41.246 Views | YouTube/WDIV (02.03.2026) | VERIFIED |

---

## 4. Widersprüche und Unsicherheiten

1. **Views stammen aus Projekt-Topic-Pages** (Instagram `/popular/`-Seiten). Sie sind gerundet, zeigen bevorzugt Top-Posts (Auswahl-Bias) und sind nicht über die volle Account-Historie erhoben. **Ältere Reels hatten mehr Zeit, Views zu sammeln** (Aktualitäts-Bias). Der Median-Rückgang der KI-Reels 2024→2026 ist deshalb nur ein Indiz, kein Beweis für Sättigung. Der Vergleich KI vs. Nicht-KI **innerhalb** eines Jahres (2025 und 2026 liegt KI jeweils darunter) ist robuster, 2024 hat aber nur n=14 KI-Reels.
2. **Survivorship Bias:** Alle Fallbeispiele sind Gewinner. Gescheiterte KI-Interior-Seiten tauchen weder auf Topic-Pages noch in Tutorials auf. Belegte „Failures“ gibt es nur indirekt: Accounts mit Reichweitenabfall (cozyzen.ai, luxurydreamhub), den soothenests-Schwenk und Copycat-Kanäle mit wenigen Views. **Einen dokumentierten Einzelfall „Account wegen Unoriginalität gesperrt oder demonetarisiert“ habe ich nicht gefunden.** `[UNKNOWN]`
3. **Ob Instagram KI-Inhalte als „original“ einstuft, ist offen.** Die Originalitätsregel von 2026 erwähnt KI nicht. Eigene Generierung ist kein Repost, aber Reposts fremder KI-Clips (bei Theme-Pages üblich, siehe Credits wie *"By: @cozyzen.ai @interior_home_design1"* in den Projektdaten) fallen klar darunter.
4. **Offenlegung vs. Reichweite ist widersprüchlich.** @ifonly.ai hat offengelegt *"AI-generated video"* und trotzdem 136 Mio. Views, @cozyzen.ai hat offengelegt und fällt ab. Im Projekt-Sample haben offengelegte Reels niedrigere Mediane (71.850 vs. 226.000), bei **n=8** aber zu wenig für eine Aussage.
5. **Einkommen:** Es gibt **keine einzige verifizierte Einnahmenzahl einer KI-Interior-Theme-Page.** Alle Zahlen sind Selbstauskünfte von SaaS-Gründern (Levels) oder Spekulation in Tutorials. Mindestens eine ist rechnerisch falsch (AiPerson), und Tutorial-Autoren verkaufen selbst Kurse (Interessenkonflikt).
6. **Zuordnung:** Ob die YouTube-Kanäle „Soothe Nests“ zum IG-Account gehören und ob @naturesms die 10M-Seite aus dem AI-pocalypse-Tutorial ist, ist **UNKNOWN**. Die geteilte Kontakt-E-Mail von soothenests und cozyzen.ai stammt aus Threads-Bios (Projektdaten), nicht aus Instagram.
7. **Plattformtransfer:** Die HKS- und 404-Befunde betreffen **Facebook**, Pinterest-Controls betreffen **Pinterest**, die AiPerson- und Ank-Tutorials zielen auf **YouTube Shorts**. Die Übertragung auf Instagram ist plausibel, aber nicht belegt.
8. **Lücken durch Tool-Limits:** Reddit, X, Indie Hackers, Medium, PromptBase, Etsy, Gumroad und Social Blade waren nicht auswertbar (siehe Methode). Gerade Belege zu Prompt-Pack-Verkäufen und Erfahrungsberichten von Betreibern könnten dort liegen.
9. **Tim Fu ist kein gesichtsloser Theme-Page-Betreiber**, sondern ein namentlich auftretender Architekt. Seine Wachstumskurve und Kurs-Monetarisierung beruhen auch auf Fachreputation (Zaha Hadid Architects) und sind nicht 1:1 auf anonyme Seiten übertragbar.

---

## 5. Quellenliste

| # | URL | Titel | Datum | Quellentyp |
|---|---|---|---|---|
| 1 | https://www.instagram.com/reel/DBWhf0koR7_/embed/captioned/ | @soothenests Reel-Embed | abgerufen 2026-09-25 (Post 2024-10-20) | instagram_public |
| 2 | https://www.threads.com/@soothenests/post/DdS6abyEgZ6 | soothenests Threads-Post (Dreamina) | 2026-09-14 | instagram_public (Threads) |
| 3 | https://www.instagram.com/reel/C87NQHRtm6B/embed/captioned/ | @drcozyvibes Reel-Embed | abgerufen 2026-09-25 (Post 2024-07-02) | instagram_public |
| 4 | https://www.instagram.com/reel/C_Pf1dboaeJ/embed/captioned/ | @siyad_abdali Reel-Embed | abgerufen 2026-09-25 (Post 2024-08-29) | instagram_public |
| 5 | https://www.instagram.com/reel/DHBihXfMPDA/embed/captioned/ | @aiforarchitects Reel-Embed | abgerufen 2026-09-25 (Post 2025-03-10) | instagram_public |
| 6 | https://www.instagram.com/reel/C--Al6UA6GE/embed/captioned/ | @ifonly.ai Reel-Embed (Tiramisu-Haus) | abgerufen 2026-09-25 (Post 2024-08-22) | instagram_public |
| 7 | https://aiforarchitects.co/services/ | AI for Architects – Services | abgerufen 2026-09-25 | company_primary |
| 8 | https://www.youtube.com/@drcozyvibes | Dr Cozy Vibes (Healing Your Soul) – Kanal-About (via NexLev) | abgerufen 2026-09-25 | other (YouTube-Metadaten) |
| 9 | https://www.youtube.com/@NostalgicRaindrops | Nostalgic Raindrops – Kanal-About (via NexLev) | abgerufen 2026-09-25 | other (YouTube-Metadaten) |
| 10 | https://www.youtube.com/channel/UCmLIJIzOIZHLLJhJTQGg2Jw ; https://www.youtube.com/channel/UCrR6fn1Gm_zVGstBR9sEqig | „Soothe Nests“-YouTube-Kanäle (via NexLev) | abgerufen 2026-09-25 | other |
| 11 | https://misinforeview.hks.harvard.edu/article/how-spammers-and-scammers-leverage-ai-generated-images-on-facebook-for-audience-growth/ | How spammers and scammers leverage AI-generated images on Facebook for audience growth (DiResta/Goldstein) | 2024-08-15 | industry_report (peer-reviewed) |
| 12 | https://arxiv.org/abs/2403.12838 | How Spammers and Scammers Leverage AI-Generated Images on Facebook for Audience Growth (Preprint) | 2024-03-19 | industry_report |
| 13 | https://www.404media.co/where-facebooks-ai-slop-comes-from/ | Where Facebook's AI Slop Comes From (Jason Koebler) | 2024-08-06 | news_media |
| 14 | https://www.404media.co/facebook-is-being-overrun-with-stolen-ai-generated-images-that-people-think-are-real/ | Facebook Is Being Overrun With Stolen, AI-Generated Images That People Think Are Real | 2023-12-18 | news_media |
| 15 | https://techcrunch.com/2025/04/30/pinterest-launches-new-tools-to-fight-ai-slop/ | Pinterest launches new tools to fight AI slop | 2025-04-30 | news_media |
| 16 | https://techcrunch.com/2025/10/16/pinterest-adds-controls-to-let-you-limit-the-amount-of-ai-slop-in-your-feed/ | Pinterest adds controls to let you limit the amount of 'AI slop' in your feed | 2025-10-16 | news_media |
| 17 | https://creators.instagram.com/blog/rewarding-original-creators-on-instagram | Original Creators Get Priority | 2026-04-30 | meta_primary |
| 18 | https://www.facebook.com/help/instagram/2635536099905516 | Instagram Content Monetization Policies | undatiert, abgerufen 2026-09-25 | meta_primary |
| 19 | https://lexfridman.com/pieter-levels-transcript/ ; https://lexfridman.com/pieter-levels/ | Lex Fridman Podcast #440 – Pieter Levels (Transkript) | 2024-08-20 | other (Podcast, Selbstauskunft) |
| 20 | https://interiorai.com/ | Interior AI – Startseite/Preise | abgerufen 2026-09-25 | company_primary |
| 21 | https://thishousedoesnotexist.org/ | This House Does Not Exist | abgerufen 2026-09-25 | company_primary |
| 22 | https://www.archdaily.com/988606 | "This House Does Not Exist" Uses AI to Generate Images Inspired by ArchDaily's Modern Architecture Projects | 2022-09-07 | news_media |
| 23 | https://www.roomgpt.io/ ; https://github.com/Nutlope/roomGPT | RoomGPT (SaaS) / Open-Source-Repo | abgerufen 2026-09-25 | company_primary |
| 24 | https://www.virtualstagingai.app/ | Virtual Staging AI | abgerufen 2026-09-25 | company_primary |
| 25 | https://www.youtube.com/watch?v=cSMqgh1hNww | #44 AI in Architecture: Disrupting the AEC Industry with Tim Fu (ArchiTech Network) | 2023-06-04 | other (Creator-Interview) |
| 26 | https://parametric-architecture.com/midjourney-architecture-3-0-studio-tim-fu/ | Midjourney Architecture 3.0 – Studio Tim Fu | Kurs 2023-01-14/15 | company_primary |
| 27 | https://www.youtube.com/watch?v=Ny9Q3zgcOv8 | How to Create Relaxing Snow / Rain Videos \| 100+ MILLION VIEWS?! (AI-pocalypse) | 2023-11-25 | blog_case_study (Tutorial) |
| 28 | https://www.youtube.com/watch?v=RD0Z9G9HCk0 | How to Make Viral Aesthetic Home Videos with AI (AiPerson) | 2025-11-02 | blog_case_study (Tutorial) |
| 29 | https://www.youtube.com/watch?v=jWthLwZJ0DY | Create Viral Construction Timelapse with AI (100% FREE) (Grow with Ank) | 2025-12-01 | blog_case_study (Tutorial) |
| 30 | https://www.youtube.com/watch?v=fBU50XlVE4o | How to ACTUALLY Make $5000 With AI Generated Art Reels (AI Venture) | 2024-11-21 | blog_case_study (Tutorial) |
| 31 | https://www.youtube.com/watch?v=B7tZw_EK35c | How To Build A $100,000 Theme Page Business On Instagram (Josh Ryan) | 2024-08-29 | blog_case_study |
| 32 | https://www.youtube.com/watch?v=08zJd3gUbOs | Detroit listing prompts debate over AI-enhanced home photos (WDIV Local 4) | 2026-03-02 | news_media |
| 33 | https://www.designboom.com/technology/from-zaha-hadid-wes-anderson-midjourney-most-copied-architects-artists-ai-10-27-2025/ | from zaha hadid to wes anderson, these are midjourney's most copied architects and artists | 2025-10-27 | news_media |
| 34 | https://en.wikipedia.org/wiki/AI_slop | AI slop (Wikipedia; zitiert Max Read, NYMag 2024-09-25) | abgerufen 2026-09-25 | other |
| 35 | https://www.youtube.com/watch?v=_n2IEbFJDao | I Recreated Ai Slop CRAFTS (HopeScope) | ca. 2026-04 („5mo ago“) | other |
| 36 | Repo: `data/processed/reels_unique.csv`, `reels_cover_coded.csv`, `accounts_metrics.csv`, `stats/seg_production.csv`, `data/raw/accounts/profile_*.json` | Projektdatensatz (öffentliche IG-Topic-Pages, Embeds, Threads-Bios) | erhoben 2026-09-25 | other (interner Datensatz) |

**Nicht abrufbar (für Folgerecherche):** reddit.com (Tool-Block), nymag.com (Block), promptbase.com (403), etsy.com (403), fiverr.com (403), socialblade.com (403), snopes.com (402), gumroad.com/discover (leere Trefferliste), instagram.com/soothenests/ (429).
