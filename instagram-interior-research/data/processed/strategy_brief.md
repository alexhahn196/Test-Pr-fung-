# Strategy Brief (interne Synthese für alle Dokumente)

Dieses Brief fasst die datenbasierten Entscheidungen zusammen, auf die sich ALLE Dokumente (00–17) stützen müssen.
Zahlen immer aus `data/processed/analysis_digest.md` bzw. `data/processed/stats/*.csv` zitieren (dort nachprüfbar),
nie aus dem Gedächtnis. Wo das Brief eine Zahl nennt, ist sie ein Verweis auf den Digest-Stand – beim Schreiben
gegen den Digest prüfen.

## 1. Methodische Leitplanken (in jedem Dokument respektieren)

- **Datenbasis:** 2.498 Reels von 239 öffentlichen Instagram-Topic-Seiten (`/popular/<slug>/`, Stand 25.09.2026),
  davon 2.393 per Cover-Frame + Caption codiert (KI-gestützt, Reliabilität κ 0,63–1,0), Follower via öffentliche
  Embed-Seiten, exakte Posting-Zeit aus dem Shortcode. 72 Accounts tief profiliert. YouTube-Shorts als Proxy.
- **Selektionsbias:** Topic-Seiten zeigen die *Top*-Reels eines Themas. Alle Vergleiche sind „unter Reels, die es auf
  eine Topic-Seite geschafft haben“. Absolute Views sind daher nach oben verzerrt; *relative* Vergleiche sind die Stärke.
- **Hauptmetrik = `adj_factor`:** Views relativ zur Erwartung für die Accountgröße auf derselben Topic-Seite
  (Regression log Views ~ log Follower innerhalb Topic; 1,0 = erwartbar; 2,0 = doppelt). Grund: Followerzahl ist der
  stärkste Einzel-Treiber (Spearman ρ≈0,44; 1M+-Accounts Topic-Index 3,4 vs. <10K 0,4). Ohne Größenkontrolle würden
  Theme-Pages/AI-Accounts falsch bewertet.
- **Signifikanz:** Kruskal-Wallis je Dimension; bei ~27 Tests Bonferroni-Schwelle p≈0,0019. Robust (nach Korrektur):
  Account-Typ, Realismus-Grad, Postjahr, (Visual Quality knapp). Nur nominal (p<0,05): Produktion (AI vs. real),
  Personen im Bild, Fensterblick, AI-Kennzeichnung (Licht nur im Kruskal-Test knapp, p≈0,05; Nacht vs. Tag n.s.). **Nicht signifikant:** Stil, Raum, Location, Farbe,
  Helligkeit, Caption-Hook, CTA, Posting-Uhrzeit/Wochentag. → Ehrlich kommunizieren: „Was“ (Stil/Raum) erklärt wenig;
  „Wie“ (Konzept, Realismus, Account-Identität) erklärt mehr.
- **Keine Kausalität behaupten.** Korrelationen als Hypothesen für die Testing-Matrix formulieren.
- **Belastbarste Kontraste** stehen mit 95-%-Bootstrap-KI und Mann-Whitney-p in `stats/key_contrasts.csv` (Digest-Abschnitt
  „Key contrasts“). Dort signifikant: KI fantasy vs. KI dreamy (≈3,25×), KI fantasy vs. KI realistisch (≈2,5×), fantasy vs. Rest
  (≈2,3×), Theme-Page vs. AI-Creator (≈0,68×), KI Outdoor/Bad/Treppe/Pool vs. KI Schlaf/Wohn/Küche (≈2,1×; post-hoc gebildet!),
  KI warm/tropical/glam/futuristic vs. organic/scandi/japandi/med/modern-lux (≈2,5×; post-hoc!), Choice-Hook → Kommentare/View
  (≈5,7×), Fensterblick (≈0,70×), KI mit Personen (≈1,68×, p≈0,02). **Nicht signifikant:** KI vs. reale Aufnahmen (≈0,92×,
  KI 0,75–1,09), Nachtlicht vs. Tag (≈1,21×), Farbtemperatur kühl vs. warm (≈1,04×), Text-Overlay (≈0,92×), Money-Hook (≈1,28×),
  Location-Hook (≈0,66×), Split-Cover (≈0,56×, n=22), Shoppability (≈1,02×), Choice-Hook auf Views (≈1,65×, p≈0,05). Post-hoc-Gruppierungen immer als
  „explorativ – im eigenen Test bestätigen“ kennzeichnen.
- **Nicht messbar mit öffentlichen Daten:** Reel-Länge, Kamerafahrt, Audio, erste 1–2 Sekunden auf Instagram
  (NexLev-Video-Tool nur 15/Tag → 7 Reels). Proxy: YouTube Shorts (12 Kanäle, 713 Shorts, 219 mit Dauer) + Cover-Frame.
  Klar als PROXY/UNKNOWN kennzeichnen.

## 2. Kernbefunde (die „Story“)

1. **Die Nische ist riesig, aber das Ursprungskonzept (KI-Luxus-Interiors: Schlaf-/Wohnzimmer/Küchen im „dreamy“
   Look) ist der schwächste KI-Teilbereich in den Daten.**
   - KI-generierte Reels liegen *tendenziell* unter realen Aufnahmen (Median-Verhältnis ≈0,92, 95-%-KI 0,75–1,09 → nicht
     signifikant). Der starke, signifikante Unterschied liegt **innerhalb** der KI-Reels – beim Konzept/Realismusgrad.
   - Innerhalb KI: *fantasy_impossible* ≈2,27× (n=53) vs. *aspirational_realistic* ≈0,90 (n=328) vs. *stylized_dreamy* ≈0,70 (n=305).
   - KI-Räume: Wohnzimmer ≈0,69 (n=123), Küche ≈0,67 (n=31), Schlafzimmer ≈0,77 (n=110) – dagegen Treppen/Hallen ≈2,24 (n=16),
     Garten ≈1,61 (n=43), Bad ≈1,45 (n=28), Pool ≈1,16 (n=23), Terrasse ≈1,06 (n=26) (kleine n, Richtung; Gruppenvergleich ≈2,1×, p<0,001, post-hoc).
   - KI-Stile: glam ≈1,95 (n=15), warm luxury ≈1,85 (n=15), tropical ≈1,70 (n=20), futuristic ≈1,06 (n=58); schwach: Scandinavian ≈0,28 (n=16),
     classical ≈0,56, organic modern ≈0,57 (n=56), japandi ≈0,61, dark luxury ≈0,64, biophilic ≈0,64, mediterranean ≈0,69, rustic cozy ≈0,78,
     modern luxury ≈0,79 (n=128, der häufigste KI-Stil!).
2. **Faceless Theme-Pages performen strukturell schwächer** (adj ≈0,74; n=503) als Creator-/Studio-Identitäten
   (ai_creator ≈1,09, n=276; lifestyle ≈1,24, n=508). Innerhalb KI: Theme-Page ≈0,70 (n=228) vs. AI-Creator ≈1,02 (n=271); Kontrast ≈0,68×, p<0,001. → Wir positionieren
   uns als **„AI-Architektur-/Design-Studio mit Originalwerken“**, nicht als Repost-/Theme-Page (auch wegen
   Instagram-Originalitätsregeln, q01).
3. **Menschliche Präsenz hilft tendenziell** (alle Reels ≈1,11×, n.s.; bei KI ≈1,68×, p≈0,02; innerhalb Accounts
   +8 Pp. in Top-10 %). → Kleine menschliche Figuren/Silhouetten für Maßstab & Story – kein Creator-Gesicht nötig.
4. **Frische/Wachstum (Anteil Top-Reels der letzten 180 Tage je Topic-Gruppe; `stats/freshness_by_group.csv`):**
   Architektur 57 % (neue Reels adj ≈1,53, 44 % KI), Cozy-Ambience 44 % (≈1,11; aber 67 % der neuen Reels KI → Sättigung),
   Unusual Homes 38 % (≈1,09), generische Räume 32 % (≈1,38). Verkrustet/schwach: KI-Topic-Seiten 27 % (neue Reels ≈0,72;
   89 % KI!), Luxury Rooms 24 % (≈0,80), Hotels 30 % (≈0,71), Future-Arch-Topicseiten 22 % (neue ≈0,59), Locations 38 % (≈0,82).
   KI-Anteil an codierten Topic-Reels nach Postjahr: 5 % (2023) → 22 % (2024) → 29 % (2025) → 33 % (2026).
5. **Decay-Evidenz:** Mehrere KI-Cozy/Interior-Accounts brachen nach 2024-Hits ein (cozyzen.ai 4,1M → 18–27K;
   kohlectcabins 23,8M → 70,6K; luxurydreamhub jüngere Reels nur Bruchteil der Likes; YouTube: Kou Yang, UnrealLife,
   Dreamy Interior, Simple Vision: neueste Uploads 10–1.000× unter den Hits; teils altersbedingt). → Format-Müdigkeit
   ist real: Wir brauchen eine **Novelty-Engine** (Serien mit wechselnden Konzepten) statt eines Einheits-Looks.
6. **Hooks:** Choice („Welches würdest du wählen?“) bringt signifikant ≈5,7× mehr Kommentare pro View (KI: 68 % der
   Choice-Reels ≥5× Follower); der Views-Effekt (≈1,65×, p≈0,05) ist dagegen **nicht belastbar**. Money/Price ≈1,3× (n.s.);
   Status ≈1,37 (n=37). Schwach: reine Location-Caption ≈0,63 (n=161), Contrarian ≈0,70, Instructional ≈0,72; bei KI
   POV und Question unter 1 (kleine n). Text-Overlay auf dem Cover ≈0,92 und innerhalb Accounts −13 Pp. in Top-10 %.
   Split-Screen-Vorher/Nachher-Cover ≈0,56 (n=22, n.s.) – *Transformations-Storys* als Video funktionieren dagegen
   (Beispiele recastliving, renovaistudio, elitebuildhq; YT-Transformation-Titel ≈1,15).
7. **Licht/Farbe:** Nacht/künstliches Licht (adj ≈1,14, n=387) ≈1,2× vs. Tageslicht (nicht signifikant; innerhalb Accounts +12 Pp. in Top-10 %),
   City-Lights/Skyline innerhalb Accounts +13/+16 Pp. (kleine n); Kerzen/Dunkel-cozy ≈0,55 (n=20); „mixed“ ≈0,78.
   **Farbtemperatur hat keinen messbaren Effekt** (kühl vs. warm ≈1,04×). Warm-neutrale Paletten wählen wir daher aus
   **Marken- und Commerce-Gründen** (Holz/Stein/Messing = kaufbar, konsistent), nicht als Performance-Hebel.
   Fensterblick-Klischee ≈0,70× (signifikant, übernutzt). Schnee ≈0,68, Wüste ≈0,63 (Richtung).
8. **Fantasy vs. realistisch (Teil 18):** Fantasy/impossible bringt mehr Reichweite (≈2,1× gesamt; ≈2,3× bei KI), ist
   aber zu 95 % „low shoppability“ (n=62). **Shoppability zeigt keinen messbaren Reichweiten-Unterschied** (high ≈0,98 vs. low ≈0,97; Kontrast ≈1,02×, p=0,91).
   Schwach ist nicht „kaufbar“, sondern der **generische KI-Realismus-Look**. → Hybrid-Hypothese: *„Impossible places,
   possible furniture“* (unmögliche Architektur-Hülle, kaufbare Möbel innen) – als Test, nicht als Fakt.
9. **Locations:** Indien ≈1,95 (n=48, v. a. reale Designer-Accounts), Schweiz ≈1,84 (n=16), Tulum/Mexiko ≈1,24, Tokyo ≈1,19,
   Bali ≈1,11, Dubai ≈1,10 (n=97), Lake Como ≈1,07; schwach London ≈0,58, Nordics ≈0,52, Maldives ≈0,81, Ibiza ≈0,85. Nicht signifikant → Location als *Setting*, nicht als Hook.
10. **Posting-Zeit** (Stunde/Wochentag UTC) ohne messbaren Effekt. Posting-Frequenz der Top-KI-Accounts (Obergrenze):
    ~1–3/Tag (siehe Competitor-DB) → 3/Tag ist im Rahmen.
11. **Länge/Kamera (nur Proxy):** YouTube: ≤12 s Loops über Kanal-Median (konfundiert), wenig Bildwechsel (statisch/
    langsam) ≈1,7 vs. viele Schnitte ≈0,4 (konfundiert mit Dauer). NexLev-Stichprobe (7 IG-Reels): 7–23 s, meist
    statische/langsame Einstellungen. → Länge und Kamera sind **Testvariablen**, keine Befunde.
12. **Monetarisierung (q02, q03, q06, Profile):** Möbel-Affiliate ist dünn (Amazon Home/Furniture 3 %, 24-h-Cookie,
    geboostete Reels verlieren Provision; Wayfair bis 7 %/7 Tage laut Drittquelle); KI-Möbel existieren nicht →
    „similar items“ nötig. Am besten belegt für KI-Visual-Accounts: **KI-Tool-Sponsoring/Affiliate** (z. B.
    Dreamina-Partner bei soothenests, RenoMuse-App-Promo-Kanal, Higgsfield Earn bis $2.500/Video, Runway/Planner 5D
    Affiliate), **B2B-Visualisierung** (aiforarchitects → Designservices), **digitale Produkte** (Prompts/Kurse:
    montani3d, archibible), Kommentar-Keyword→DM-Funnels (roomify.design: „kuratierte Wayfair-Kollektion per DM“).
    Marken zeigen ungern KI-Creator nach außen (Begeisterung 60 %→26 %).

## 3. Entscheidung: Positionierung

**Nicht:** „noch eine KI-Luxus-Interior-Theme-Page“ (Bedrooms/Living/Kitchen, dreamy, organic-modern/Scandi).
**Sondern:** Ein **AI-Architektur-Studio für „Homes that shouldn’t exist (yet)“** – unmögliche/zukunftsweisende
Häuser und Räume als *Originalentwürfe*, mit wiederkehrenden Serien, warmem Nachtlicht, menschlichem Maßstab,
Choice-Mechaniken und kaufbaren Interieur-Momenten. Arbeitstitel (für Konzepte variieren): *Impossible Estates*,
*The Unbuilt*, *Nowhere Homes*.

Die Konzeptentscheidung lässt sich auf die anderen geprüften Segmente übertragen:
- Future Architecture: **Kern** (wenn konzeptuell/fantastisch; frisch; KI-geeignet).
- AI Landscaping / Outdoor / Transformation: **starker zweiter Pfeiler** (KI-Garten/Pool/Terrasse >1; Transformations-
  Storys; kaufbare Outdoor-Möbel).
- Dream Bedrooms: nur als Choice-Format, nicht als Kern (KI-Bedrooms ≈0,70; gesättigt).
- Luxury Hotels / Future Resorts: schwach (≈0,7–0,8; Realitäts-/Irreführungsrisiko) → nur gelegentlich.
- Luxury Kitchens: schwach bei KI (≈0,59) → nein.
- Cozy Ambience: hohe Views/Follower, aber Sättigung/Decay → nur als Nebenserie (Nacht-Retreats), später YouTube-Long-form.

## 4. Content Pillars (Daten-gestützt) & Start-Mix (30 Tage, 90 Reels)

| Pillar | Anteil | Daten-Begründung | Ziel |
|---|---|---|---|
| P1 Impossible Homes (Konzept-Architektur außen+innen, Klippe/Fels/Turm/Alpin/unterirdische Oase; nicht Unterwasser ≈0,39) | 35 % | KI fantasy ≈2,3×; Architektur frisch (57 %, ≈1,5) | Reichweite, Shares, Follows |
| P2 Pick One (2–4 Varianten desselben Raums/Hauses) | 20 % | Choice ≈1,4×, 5–13× Kommentare | Kommentare, Community, Affiliate-Brücke |
| P3 Dream Builds / Transformations (leer→fertig, Garten/Pool/Bad/Terrasse) | 20 % | KI-Garten ≈1,61, Bad ≈1,45, Pool ≈1,16; Transformations-Winner | Watch-Time, Saves, kaufbare Outdoor/Bad-Items |
| P4 Night Stories (Penthouse/City-Lights, warmes Nachtlicht, Figuren) | 15 % | Nachtlicht ≈1,14; City-Lights innerhalb Accounts +13 Pp. | Ästhetische Signatur, Sends |
| P5 Wildcards (Location-Serie Schweiz/Dubai/Tokyo, Cozy Night, Price-Hook) | 10 % | Explorativ | Neue Gewinner finden |

Nach 30 Tagen: 60–70 % Reichweite (P1/P4) und 30–40 % Commerce-nahe Formate (P2/P3) – abhängig vom Winner-DB-Ergebnis.

## 5. Style-Guide-Leitlinien (aus Mustern abgeleitet, nicht kopiert)

- Licht: warmes künstliches Nachtlicht + Blue Hour; keine Kerzen-Düsternis, kein diffuses Mischlicht.
- Palette: warm-neutral (Travertin, Sand, Walnuss, Bronze/Messing) + tiefes Nachtblau als Signatur-Kontrast (Marken-
  entscheidung; Farbtemperatur selbst zeigt keinen Performance-Effekt). Kühle Grau/Weiß-Skandi-Looks meiden, weil die
  *Stile* Scandinavian/organic modern bei KI sehr schwach sind (post-hoc, explorativ).
- Architektur: ungewöhnliche Strukturen (in Fels gehauen, auskragend, Turm, unterirdische Oase), Treppen/Hallen als
  Hero-Element, Pools & Gärten, Bäder als Statement.
- Mensch: kleine Figur/Silhouette für Maßstab & Story (kein Gesicht-Branding).
- Cover: ohne dichten Text-Overlay; kein Split-Screen; starkes Einzelmotiv (Architektur-Merkmal oder Reveal).
- Hooks: Curiosity + Price + Choice; Location nur als Setting; keine reinen „instructional“-Hooks.
- Captions: kurzer Titel-Satz + Frage/Choice-CTA; ≤5 Hashtags (Instagram-Limit seit 12/2025); keine „link in bio“/
  „save & share“-Befehle als Standard (link_in_bio ≈0,82, save_share ≈0,75; n.s.).
- Wiedererkennung: feste Serien-Titel/Nummerierung („Unbuilt No. 017“), Signatur-Farbkontrast, konstantes Ending
  (z. B. Rückfahrt in die Nacht), dezentes Wasserzeichen/Logo *nicht* großflächig (Originalitäts-/Wasserzeichen-Regel beachten).
- KI-Kennzeichnung: offen, markenkonform („AI concept by …“), Meta-/EU-Pflichten einhalten (q01/q07) – Offenlegung
  korreliert mit geringeren Views (≈0,64), ist aber keine Option, sondern Pflicht bei fotorealistischem Content.

## 6. Die 3 ersten Test-Formate

1. **„Unbuilt No. X“** – Impossible Home Reveal (8–12 s, langsamer Push-in/Fly-through, Nacht, Figur, Curiosity/Price-Hook).
2. **„Pick One“** – 3 Varianten (Stil/Setting) desselben Raums, Choice-Hook, Kommentar-CTA; Variante mit kaufbaren Stücken.
3. **„From Nothing“** – Transformation leerer Ort → Traum-Outdoor/Bad/Pool (12–20 s, sequenzieller Reveal, kein Split).

## 7. Risiken (ehrlich benennen)

- Größter Hebel ist Account-Größe/-Identität → Start ist schwer; erste Wochen liefern wenig Reichweite ohne Durchbruch.
- KI-Sättigung + Decay: jede Serie hat eine Halbwertszeit → wöchentliches Monitoring (17) & Rotation.
- Plattform/Legal: KI-Labels, Originalität, irreführende Preis-/Orts-Claims („$50M home in Dubai“ ist fiktiv → als Konzept
  kennzeichnen), Marken/Designrechte, Musikrechte, Werbekennzeichnung (q01, q07).
- Monetarisierung über Möbel-Affiliate allein trägt nicht; Mix aus KI-Tool-Sponsoring, B2B, digitalen Produkten nötig.
