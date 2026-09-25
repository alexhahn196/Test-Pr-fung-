# 00 – Executive Summary & Entscheidung (Teil 35)

**Stand:** 25.09.2026 · **Datenbasis:** 2.498 Reels von 239 öffentlichen Instagram-Topic-Seiten (davon 2.393 visuell codiert,
2.397 mit Followerzahl), 1.985 Accounts, 72 tief profilierte Accounts, 9 Recherche-Notizen mit Faktencheck, YouTube-Shorts-Proxy
(12 Kanäle, 713 Shorts). Methodik und Grenzen stehen in der [README](README.md), alle Zahlen in
[analysis_digest.md](data/processed/analysis_digest.md) und [key_contrasts.csv](data/processed/stats/key_contrasts.csv).

**Lesehilfe:** `adj_factor` = Views im Verhältnis zur Erwartung für die Accountgröße auf derselben Topic-Seite
(1,0 = wie erwartet, 2,0 = doppelt so viele). Alle Aussagen beziehen sich auf Reels, die es auf Topic-Seiten geschafft haben
(Selektionsbias). Es sind Korrelationen und damit Hypothesen, keine Kausalbeweise.

**Entscheidung in einem Satz:** Wir starten nicht als KI-Luxus-Interior-Theme-Page, sondern als Konzept **K1 *The Unbuilt***
(Arbeitstitel), ein AI-Architektur-Studio für *„Homes that shouldn't exist (yet)“*, mit den Serien `UNBUILT`, `PICK ONE`,
`FROM NOTHING` und `AFTER DARK` ([10 §11](10_market_gaps.md), [11](11_brand_style_guide.md), [08](08_content_pillars.md)).

---

## Das Wichtigste in 8 Sätzen

1. **Die Nachfrage ist riesig.** Topic-Seiten zeigen enorme Volumina (z. B. „home-decor“ 901 Mio. Reels, „dream-home“ 151 Mio.,
   „luxury-homes“ 128 Mio., „kitchen-design“ 102 Mio.). Der Median der Top-Reels liegt bei 233K Views, 10 % erreichen ≥3,9 Mio.
2. **Die Konkurrenz ist genauso riesig, und KI-Content nimmt schnell zu.** Der KI-Anteil unter den codierten Top-Reels stieg
   von 5 % (2023) über 22 % (2024) und 29 % (2025) auf 33 % (2026). Auf KI-Topic-Seiten sind 89 % der neuen Top-Reels KI.
3. **Das Ursprungskonzept ist der schwächste KI-Teilbereich.** Gemeint sind KI-Luxus-Interiors mit Schlaf-, Wohnzimmern und
   Küchen im weichen „dreamy“-Look. Dreamy-KI liegt bei adj ≈0,70 (n=305), realistische KI-Interiors bei ≈0,90 (n=328).
   KI-Wohnzimmer ≈0,69, KI-Küchen ≈0,67, KI-Schlafzimmer ≈0,77.
4. **Was funktioniert, ist das Unmögliche.** Fantastische, physikalisch „unmögliche“ Konzepte erreichen bei KI ≈2,3× der
   Erwartung (n=53). Das sind ≈3,25× mehr als Dreamy-KI (95-%-KI 1,8–5,6; p=0,001) und ≈2,5× mehr als realistische KI
   (p=0,008). Architektur gehört zudem zu den frischesten Feldern: 57 % der Top-Reels sind jünger als 180 Tage (nur
   Commerce-Decor liegt mit 60 % höher), neue Architektur-Reels liegen bei ≈1,5×.
5. **Die Identität schlägt das Motiv.** Faceless-Theme-Pages liegen bei ≈0,74 (n=503), KI-Creator bei ≈1,09 (n=276),
   Lifestyle-Creator bei ≈1,24 (n=508). Der Kontrast Theme-Page zu KI-Creator beträgt ≈0,68× (p<0,001). Stil, Raum, Location,
   Farbtemperatur und Posting-Zeit zeigen dagegen **keinen** signifikanten Effekt.
6. **Choice-Mechaniken ziehen Kommentare.** „Pick one“-Hooks bringen ≈5,7× mehr Kommentare pro View (p<0,0001). Der Effekt
   auf die Views (≈1,65×) ist knapp nicht signifikant.
7. **Kaufbarkeit kostet keine Reichweite.** Reels mit hoher und niedriger Shoppability performen gleich (≈1,02×, p=0,91).
   Schwach ist nicht das Kaufbare, sondern der generische KI-Realismus-Look.
8. **KI-Theme-Pages zeigen Decay.** Mehrere KI-Cozy- und Interior-Accounts brachen nach ihren 2024-Hits stark ein.
   Beispiele: cozyzen.ai von 4,1 Mio. auf 18–27K Views, kohlectcabins von 23,8 Mio. auf 70,6K. Ähnliches zeigen
   YouTube-Kanäle (teils altersbedingt verzerrt). Ein Einheits-Look scheint schnell zu verschleißen, deshalb planen wir eine
   **Novelty-Engine** (konstante Signatur, wechselnde Konzepte).

---

## A. Ist Interior/Luxury Homes aktuell eine interessante Nische für einen KI-Theme-Account?

**Ja, aber nicht in der geplanten Form.** Reichweite, Frische und KI-Eignung sprechen dafür. Dagegen sprechen:
- ein gesättigter KI-Interior-Mainstream,
- Theme-Pages mit strukturell schwächerer Performance,
- sichtbarer Decay bei KI-Accounts,
- Plattformregeln (Originalität, KI-Labels, siehe [q01](quellen/q01_instagram_platform_rules.md)),
- ein dünnes Möbel-Affiliate-Modell (Amazon Furniture/Home 3 %, 24-h-Cookie, siehe [q02](quellen/q02_furniture_affiliate_commerce.md)).

Attraktiv ist die Nische deshalb nur als **originäres KI-Architektur-/Design-Studio** mit unmöglichen, konzeptionellen Häusern
und nicht als Repost- oder „Pretty-Rooms“-Seite. In der Scoring-Matrix liegt der Querschnitt Fantasy/Impossible mit 31/45 vorn,
Architecture folgt mit 28/45; KI-Schlaf-, Wohnzimmer, Küchen und Mansions scheitern am K.-o.-Kriterium KI-Eignung.
Details: [01_market_analysis.md](01_market_analysis.md), Abschnitt 4–5.

## B. Welche Unter-Nische ist anhand der Daten am attraktivsten?

**„Luxury Homes in Impossible Locations“ bzw. „Impossible Homes“ (konzeptionelle, unmögliche Architektur), Urteil GO.**
Dazu gehören Häuser, die in einen Fels oder Findling gebaut sind, Auskragungen, Türme, alpine Konzepte, unterirdische Oasen und
Wasserfall-Häuser, außen und innen, jeweils mit menschlichem Maßstab. Die Unmöglichkeit muss aus der Architektur kommen, nicht
aus dem Standort: **Klippen-Villen** (KI adj ≈0,48, n=35; Cliff Homes REJECT) und **Unterwasser-Konzepte** (≈0,39, n=14, geringe
Konfidenz; REJECT) sind kein Standard-Setting. KI-Fantasy ist das stärkste KI-Segment (≈2,3×; 2,81× gegenüber übrigen KI-Reels,
p=0,002, als einziger der 22 Nischen-Kontraste Bonferroni-fest) und wird über frische Architektur-Seiten verteilt.
„Impossible“ ist dabei ein Format, kein Suchbegriff (die Seite `impossible-architecture` hat einen Median von nur 486 Views).

Zweiter Pfeiler: **Outdoor, Bad und Treppen sowie Transformationen** („from nothing to dream space“; AI Landscaping/Garden
Transformations = GO). KI-Outdoor, -Bad, -Treppen und -Pool liegen bei ≈2,1× gegenüber KI-Schlaf-, Wohnzimmer und Küche
(p<0,001, post-hoc gebildet; im eigenen Test bestätigen). Als TEST laufen Alpine/Swiss Concept Homes (höchste Nischen-Wertung
22/25, aber nur nominal signifikant), Underground Oases, Statement Staircases, Impossible Bathrooms, Tropical (nur als Stil),
Treehouse und Waterfall Houses. Screening aller 22 Micro-Niches: [10_market_gaps.md](10_market_gaps.md), Abschnitt 3–6.

## C. Wo ist der Wettbewerb relativ zur Nachfrage am geringsten?

**Nicht dort, wo das Verhältnis „Views je konkurrierendem Reel“ am besten aussieht.** Diese Ratio hängt *negativ* mit der
Frische zusammen (Spearman ρ = −0,34, p < 0,001, 166 Seiten). Die zehn „besten“ Ratio-Seiten haben im Median nur 8 % junge
Top-Reels und sind meist enge Suchphrasen oder verkrustete Evergreen-Seiten:

| Topic | Median-Views | Reels zum Thema | junge Top-Reels | KI-Anteil | Lesart ([10 §2](10_market_gaps.md)) |
|---|---|---|---|---|---|
| ai-interior-designer | 935K | 700 | 25 % | 50 % | enge Phrase, Suchbegriff gilt als „Peaked“ |
| futuristic-houses | 575K | 650 | 0 % | 75 % | verkrustet und KI-lastig |
| cozy-rain | 3,85 Mio. | 23K | 25 % | 42 % | echte Nachfrage, gehalten von Evergreen-Hits |
| dream-bedrooms | 1,12 Mio. | 9,5K | 0 % | 92 % | verkrustet und KI-gesättigt |
| lake-como-villa | 2,42 Mio. | 25K | 25 % | 0 % | reale Orte, KI wäre irreführend |

Eine echte Lücke braucht **vier Signale zugleich**: Nachfrage, Frische, KI-Performance über Erwartung und einen fiktiven
Gegenstand ohne Irreführungsrisiko. Diese Kombination erfüllen vor allem **KI + fantastische Architektur + Studio-Identität +
Serienformat**: Nur 2,6 % der codierten Top-Reels sind fantasy/impossible, und im Segment fanden sich nur 8 Spezialisten unter
45 Handles. Die meisten KI-Accounts sind Theme-Pages im gesättigten Dreamy-Interior-Look. Auch in der Top-20-Shortlist
(angeführt von @myplants.uae, @archibible und @design_x_interior) sind nur 2 reine Theme-Pages; 10 der 20 verkaufen
Dienstleistungen ([03_competitor_analysis.md](03_competitor_analysis.md), Abschnitt 4 und 7). Micro-Niches, Scores und
Urteile: [10_market_gaps.md](10_market_gaps.md).

## D. Welche Arten von Reels wachsen am stärksten?

Gemessen am Anteil der Top-Reels aus den letzten 180 Tagen und an deren adj:

| Feld | Anteil letzte 180 Tage | adj neuer Reels | Einordnung |
|---|---|---|---|
| Commerce-Decor | 60 % | ≈0,86 | frisch, aber real und produktgetrieben (7 % KI) |
| Architektur | 57 % | ≈1,53 | wächst, offen für KI (44 % der neuen Reels KI) |
| Garten/Outdoor | 45 % | ≈0,84 | frisch, aber neue Reels unter Erwartung → Wettbewerb steigt |
| Cozy-Ambience | 44 % | ≈1,11 | wächst, aber 67 % der neuen Reels sind KI (Sättigung) |
| Unusual Homes | 38 % | ≈1,09 | stabil (Treehouse, Underground) |
| Generische Räume | 32 % | ≈1,38 | stabil bis wachsend |
| Hotels | 30 % | ≈0,71 | schwach |
| KI-Topic-Seiten | 27 % | ≈0,72 | verkrustet und gesättigt (89 % der neuen Reels KI) |
| Luxury Rooms | 24 % | ≈0,80 | verkrustet |
| Future-Arch-Topicseiten | 22 % | ≈0,59 | verkrustet, KI-lastig |

Quelle: [freshness_by_group.csv](data/processed/stats/freshness_by_group.csv) (Momentaufnahme, keine Zeitreihe). Der Querschnitt
Fantasy/Impossible ist zu 42 % jung, neue Reels liegen bei ≈1,87 (n=26). Auf YouTube wächst das Cluster „KI-Konzept-Bau/
Transformation“ am stärksten, ist aber auch am schnellsten besetzt (`PROXY`). Siehe [01_market_analysis.md](01_market_analysis.md)
(Teil 1.6), [06_visual_styles.md](06_visual_styles.md) (Abschnitt 4.4) und [05_viral_patterns.md](05_viral_patterns.md).

## E. Welche Styles funktionieren am besten?

Stil ist insgesamt **nicht signifikant**. Die Tendenzen:

| Gruppe | Stile (adj) |
|---|---|
| Über alle Reels vorn | warm luxury ≈1,8 (n=34), neoclassical ≈1,6, mid-century ≈1,5, traditional-regional ≈1,3, minimalist ≈1,2 |
| Innerhalb KI vorn | glam ≈1,95, warm luxury ≈1,85, tropical ≈1,70, futuristic ≈1,06 |
| Schwach | modern luxury ≈0,83 (n=566, der häufigste Stil), organic modern ≈0,79, mediterranean ≈0,80, japandi ≈0,77, dark luxury ≈0,67 |
| Innerhalb KI schwach | Scandinavian ≈0,28, organic modern ≈0,57 |

Der Kontrast „KI warm luxury/tropical/glam/futuristic vs. organic/scandi/japandi/mediterranean/modern luxury“ (≈2,5×, p=0,001)
ist post-hoc gebildet. Dieselben Stile funktionieren als **echte** Aufnahmen oft gut (Scandinavian real ≈1,71, n=44); schwach ist
der KI-Standard-Look, nicht der Stil. Konsequenz: den generischen „Modern-Luxury-Beige“-KI-Look vermeiden; unser Hausstil heißt
„Warm Monolith“ ([11](11_brand_style_guide.md)). Siehe [06_visual_styles.md](06_visual_styles.md), Teil 5 und 17.

## F. Welche Video-Längen funktionieren?

**Auf Instagram öffentlich nicht messbar (UNKNOWN).** Nur als Proxy aus YouTube-Shorts vergleichbarer Kanäle (219 Shorts mit
Dauer, 12 Kanäle), konfundiert mit Kanal, Format und Alter:
- Kurze Shorts liegen scheinbar über dem Kanal-Median (0–12 s ≈2–19×, bei sehr kleinen n), 13–20 s darunter (≈0,22).
  **Aber:** 13 der 19 Shorts ≤ 12 s stammen aus einem einzigen Kanal und dessen 2025er-Hits; ohne ihn liegt ≤ 12 s bei ≈0,06
  (n=6). Über alle Längen-Buckets ist der Unterschied nicht signifikant (Kruskal p=0,22).
- Clips mit wenig Bildwechsel (statisch oder langsam) ≈1,67, viele Schnitte ≈0,40, ebenfalls nicht signifikant und mit der
  Dauer verknüpft.
- Die NexLev-Stichprobe (7 Instagram-Reels, alle EXTREME-Outlier) lag bei 7–23 s mit überwiegend ruhigen Einstellungen.
- Marken-Benchmarks (Socialinsider, Instagram) nennen dagegen 45–60 s als „sweet spot“, ebenfalls unbereinigt.

→ **Testvariable, kein Befund.** Test T12 in der [Testing-Matrix](13_testing_matrix.csv): 10 s (Kontrolle) vs. 6-s-Loop vs.
20 s, im [Launchplan](14_30_day_launch_plan.md) an Tag 22 und 27. Details: [05_viral_patterns.md](05_viral_patterns.md), Teil 12.

## G. Welche Hooks funktionieren?

Die Hook-Kategorie erklärt die Reichweite kaum (Kruskal p=0,35), die Kommentare aber stark.

**Stärker:**
- **Choice** („Which one would you move into?“): Kommentare ≈5,7× (signifikant; bei KI ≈13,6×). Der Views-Effekt (≈1,65×) ist
  nicht belastbar.
- **Curiosity bei KI** ≈1,50 (n=67; nur nominal, p=0,037), getragen vom Prozess-/Bau-Typ („from X to Y“). Bei realen Aufnahmen
  liegt Curiosity nur bei ≈0,71, deshalb nur mit sichtbarem Payoff.
- Status ≈1,37 und Money/Price ≈1,2–1,3 (beide n.s., bei KI kaum getestet). Preis-Hooks nie als Tatsachenbehauptung über
  fiktive Objekte ([q07](quellen/q07_legal_ai_risk.md) §2.6).
- Visuell: unmögliche Architektur, Reveal, menschliche Figur. Bei KI erreichen Reels mit Personen ≈1,68× (p≈0,02, nur nominal;
  KI berührt 1).

**Schwächer:**
- Reine Location-Caption ≈0,63
- Instructional ≈0,72
- Contrarian ≈0,70
- Text-lastige Cover ≈0,92 (n.s.; innerhalb von Accounts −13 Pp. in den Top-10 %)
- Split-Screen-Vorher/Nachher-Cover ≈0,56 (n=22, n.s.)
- Fensterblick-Klischee ≈0,70 (nominal signifikant, p=0,02; nicht Bonferroni-fest)

Bibliothek mit 50 eigenen Text-Hooks und 34 eigenen visuellen Hooks: [07_hooks.md](07_hooks.md).

## H. Welche Räume funktionieren?

Über alle Reels vorn: Bad ≈1,43 (n=60), Treppen/Hallen ≈1,17. Hinten: Esszimmer ≈0,69, Home-Theater ≈0,49,
Wohnzimmer ≈0,80. Innerhalb KI sind Treppen/Hallen, Garten, Bad, Pool und Terrasse stärker als Schlafzimmer (≈0,77),
Wohnzimmer (≈0,69) und Küche (≈0,67). Der Raum ist insgesamt nicht signifikant (Kruskal p=0,93), der KI-Gruppenkontrast
(≈2,1×) ist post-hoc gebildet. Der Raum ist ein Gestaltungshebel, kein Garant. Siehe [06_visual_styles.md](06_visual_styles.md),
Teil 5.

## I. Welche Locations funktionieren?

Nicht signifikant. Tendenzen:
- **Vorn:** Schweiz ≈1,84 (n=16), Tulum/Mexiko ≈1,24, Tokyo ≈1,19, Bali ≈1,11, Dubai ≈1,10 (n=97), Lake Como ≈1,07.
- **Schwach:** London ≈0,58, Nordics ≈0,52, Maldives ≈0,81.
- Indien (≈1,95, n=48) beruht überwiegend auf realen Designer-Accounts.

Location als **Setting** nutzen, nicht als Hook (Location-Captions ≈0,63), und bei fiktiven Objekten nur als
„Concept set in …“, nie als Ortsbehauptung ([q07](quellen/q07_legal_ai_risk.md) §2.6). Siehe [06_visual_styles.md](06_visual_styles.md),
Abschnitt 4.2.

## J. Fantasy oder Realistic Luxury?

**Fantasy für die Reichweite, Realismus für den Commerce, und nie der generische KI-Realismus-Look.**

| Realismus | adj |
|---|---|
| Fantasy/impossible | ≈2,1 (n=62) |
| Aspirational-realistic | ≈1,00 |
| Real existing | ≈0,95 |
| Stylized dreamy | ≈0,70 |

Die Hypothese „Fantasy bringt mehr Views“ wird **gestützt**. Die Hypothese „Realismus verkauft mehr Möbel“ lässt sich mit
öffentlichen Daten **nicht messen** (keine Klick- oder Kaufdaten). Fantasy-Reels sind aber zu 95 % „low shoppability“ und zu
0 % „high“ (n=62), während Shoppability selbst keine messbare Reichweite kostet (high vs. low ≈1,02×, p=0,91). Die
Hybrid-Hypothese *„Impossible places, possible furniture“* ist in den Daten praktisch ungetestet und deshalb ein eigener Test
(T14 im Launchplan). Details: [06_visual_styles.md](06_visual_styles.md), Teil 18, und [09_monetization.md](09_monetization.md),
Abschnitt 2.3 und 5.3.

## K. Welcher Mix ist optimal zwischen Viralität und späterer Möbel-Monetarisierung?

**Soll-Mix für den Start (Strategy Brief und [08](08_content_pillars.md)):** 50 % Reichweite, 40 % commerce-nah, 10 % Exploration.
- **Reichweite:** P1 Impossible Homes (`UNBUILT`) 35 %, P4 Night Stories (`AFTER DARK`, Lichtmoment mit Figur) 15 %.
- **Commerce-nah:** P2 Pick One (`PICK ONE`) 20 %, P3 Dream Builds (`FROM NOTHING`) 20 %.
- **Exploration:** P5 Wildcards 10 % (z. B. Named Setting, Sky Homes, Real Price).
- **Reserve:** P6 Statement Rooms (`THE ROOM`), zunächst nur als Pilot mit 4 Reels innerhalb von P3.
- **Hybrid-Test:** „Impossible places, possible furniture“, also eine unmögliche Hülle mit kaufbaren Hero-Stücken (T14).

**Im 30-Tage-Launchplan** folgen Woche 1–2 diesem Mix annähernd (P1 38 %, P2/P3/P4 je 19 %, P5 5 % der 42 Reels). Woche 3–4
verdoppeln bewusst den Gewinner. Mit dem Default-Champion P1 ergibt sich über 30 Tage P1 51 %, P2 16 %, P3 16 %, P4 12 %, P5 6 %,
also 63 % Reichweite und 31 % commerce-nah (36 % inklusive der 4 Hybrid- bzw. Kaufbar-Reels aus T14)
([14 §4.3](14_30_day_launch_plan.md)).

**Ab Monat 2:** 60–70 % Reichweite (P1, P4) und 30–40 % commerce-nah (P2, P3, ggf. P6), je nach Winner-Database. P1 und P4
bleiben commerce-frei, bis der Hybrid-Test SCALE ergibt.

**Monetarisierung, sortiert nach Evidenz** ([09 §5.1](09_monetization.md)):
1. KI-Tool-Affiliate und -Sponsoring ab Tag 1 (nur für tatsächlich genutzte Tools),
2. B2B-Konzeptvisualisierung, sobald ein Portfolio steht (häufigster beobachteter Geldweg: 30 der 72 profilierten Accounts),
3. digitale Produkte nur nach einem Nachfragetest (Warteliste),
4. Möbel-Affiliate nur über Choice- und Transformationsformate und nach dem Hybrid-Test, z. B. über Comment-Keyword-DM-Funnels
   (≈6,6× Kommentare pro View, aber kein Reichweitenvorteil),
5. Real Estate nur als B2B mit Compliance-Prüfung,
6. Newsletter als eigener Kanal ab Start (bezahlte Platzierungen erst ab 50K).

Für keinen KI-Interior-Account ist ein Einkommen verifiziert; alle Einkommenszahlen sind Drittangaben oder Annahmen.

## L. Wie sollte unser visueller Stil aussehen?

Ein wiedererkennbares Signatur-System für *The Unbuilt* (Arbeitstitel). Die Formel aus dem Style Guide lautet:
**Glow gegen Blau** + **eine unmögliche Geste** + **eine kleine Figur („The Visitor“)** + **Seriennummer** + **„Last Light“-Ende**.
- **Licht:** späte Blue Hour bis Nacht; das warme Kunstlicht des Gebäudes dominiert (KI-Nachtlicht ≈1,27 vs. übrige KI ≈0,82,
  p=0,046, post-hoc; über alle Reels Nacht/künstlich ≈1,14, vs. Tageslicht n.s.; innerhalb von Accounts +12 Pp.). „Nacht“ heißt
  nicht dunkel: keine Kerzen-Düsternis, kein Mischlicht.
- **Palette „Unbuilt Night“ und Hausstil „Warm Monolith“:** Travertin, Sandstein, Basalt, Nussbaum und Messing gegen tiefes
  Nachtblau. Das ist eine Markenentscheidung, denn die Farbtemperatur selbst zeigt keinen Effekt (≈1,04×, n.s.).
- **Formen:** pro Reel genau eine unmögliche Geste, lesbar in 1 Sekunde; Masse statt Glasbox; Treppen als Hero-Element.
- **Mensch:** eine kleine Figur in Rückenansicht, ohne Gesicht, für Maßstab und Story.
- **Cover:** starkes Einzelmotiv ohne Text-Wände, kein Split-Screen, kein Fensterblick-Klischee.
- **Serie:** Badge `UNBUILT · No. 017 · AI CONCEPT` (analog `PICK ONE`, `FROM NOTHING`, `AFTER DARK`, `THE ROOM`) ab Frame 0,
  zugleich KI-Kennzeichnung; konstanter „Last Light“-Abschluss; kein Logo-Wasserzeichen zum Start.

Vollständig, inklusive fünf Prompt-Blöcken: [11_brand_style_guide.md](11_brand_style_guide.md).

## M. Welche 3 Formate sollten wir zuerst testen?

1. **`UNBUILT No. ###`** (P1): Impossible-Home-Reveal außen → innen, 8–12 s (Kontroll-Rezept K0-P1: 10 s), eine langsame,
   durchgehende Kamerafahrt (Push-in), Nacht, kleine Figur, Curiosity-Hook (z. B. „No road leads to this house.“); Caption mit
   „AI concept, not a real property.“
2. **`PICK ONE No. ###`** (P2): drei Varianten desselben Raums oder Hauses (Start: Bad, 3 × 4 s), Choice-Hook („Pick one. You can
   only keep one.“), Kommentar-CTA. Eine Variante enthält kaufbare Hero-Stücke.
3. **`FROM NOTHING No. ###`** (P3): Transformation eines leeren Orts zum Traum-Außenraum, Bad oder Pool, 12–20 s (Kontrolle:
   15 s, 4–5 Bauphasen als Morph), sequenzieller Reveal statt Split-Screen, endet bei Nacht mit Figur.

Test T01 im Launchplan vergleicht genau diese drei Formate (Tag 5 und 12). `AFTER DARK` (P4) läuft in Woche 1–2 als Test-Arm
mit (T04, T05). Rezepte und Test-Arme: [14 §2](14_30_day_launch_plan.md), Steckbriefe: [08 §3](08_content_pillars.md),
Aufbau-Blaupausen: [05 §2.5](05_viral_patterns.md).

## N. Wie sollte unser 30-Tage-Test aussehen?

3 Reels/Tag, also 90 Reels, in festen Slots um 11:00, 17:00 und 23:00 UTC (die Posting-Zeit zeigt im Datensatz keinen Effekt;
die Test-Arme rotieren über die Slots). Der Plan ist ein Experiment mit 27 Tests aus der Testing-Matrix. Ein Tag ist ein Block:
dieselbe Architektur-Idee in 3 Reels, die sich in genau **einer** Variable unterscheiden (Kontrolle K0 plus 2 Varianten).
- **Woche 1 (Tag 1–7):** breite Tests der „Was“-Fragen: Pillar, Realismus, Hook, Stil, Format, Setting, Raum (T01–T07, je ein
  Tagesblock). Keine Leistungsentscheidung mit n=1, nur Policy- und QA-Stopps.
- **Woche 2 (Tag 8–14):** Replikat derselben 7 Tests, danach rollierend je Test VORLÄUFIGER GEWINNER, PAUSIEREN oder OFFEN
  (gepaarte Regel u. a.: Median-Verhältnis Variante/Kontrolle ≥ 1,5 bzw. ≤ 0,67). An Tag 13 wird das Champion-Rezept K\* festgelegt. „Pausieren“ ist
  kein Beweis: Mit 2 Paaren entstehen ohne echten Effekt ≈22–24 % Scheingewinner.
- **Woche 3 (Tag 15–21):** Gewinner verdoppeln. 71 % der Reels bauen auf K\* auf; getestet werden nur noch „Wie“-Faktoren
  (Licht, Mensch, Kamera, Text, Audio), dazu Hybrid-Block (T14), P3-Star und Location-Pilot. An Tag 22 folgt K\*\*.
- **Woche 4 (Tag 22–30):** Gewinner skalieren: neue Konzepte der Gewinner-Serie mit Varianten der Verpackung (Länge, Audio,
  Hook, Kamera) plus Commerce-Tests (Keyword-CTA, Preis-Labels, Hybrid-Replikat).

**Entscheidungsregeln** ([15 §4.3](15_kpi_framework.md), [14 §6](14_30_day_launch_plan.md)): Alle Werte sind relativ zum Median
der letzten 15 eigenen Reels (`account_index`). **SCALE** ab n ≥ 6, Gruppen-Index ≥ 1,5, P(besser) ≥ 95 % und Follows pro
1.000 Views ≥ Kontoschnitt. **KILL** ab n ≥ 6, Gruppen-Index < 0,6, P(schlechter) ≥ 95 % und NS-Index < 0,6; ein Policy-Hinweis
im Account Status bedeutet sofort KILL. Dazwischen liegen ITERATE-Diagnosen (z. B. „Reichweite ohne Follows“, „Inhalt gut,
Verpackung schwach“) und KEEP. Mit 90 Reels sind nur große Effekte (ab etwa ×2,3–5) sicher erkennbar, deshalb wird jeder
vorläufige Gewinner repliziert.

Messung über die [Winner-Database](data/winner_database_template.csv) mit
[winner_analysis.py](scripts/winner_analysis.py). Wöchentlich läuft der [Konkurrenzmonitor](17_competitor_monitor.md) mit
(über Graph API oder manuell, siehe Compliance-Hinweis unten). Trial Reels sind vermutlich erst ab ~1.000 Followern verfügbar
(`ESTIMATED`). Details und Tagesplan: [14_30_day_launch_plan.md](14_30_day_launch_plan.md),
[13_testing_matrix.csv](13_testing_matrix.csv) und [15_kpi_framework.md](15_kpi_framework.md).

---

## Die unbequeme Wahrheit (bewusst gegen die Ursprungsidee geprüft)

- Der größte gemessene Einzelfaktor für Views ist die **Accountgröße** (ρ≈0,43; 1M+-Accounts haben einen Topic-Index von
  ≈3,3, <10K-Accounts von ≈0,4, also ≈8-mal so viel). Ein neuer Account startet also mit dem schwächsten Hebel. Die ersten
  Wochen hängen an einzelnen Durchbrüchen; Marken-Accounts mit 1–5K Followern erreichen im Schnitt 580–658 Views pro Reel
  ([q09](quellen/q09_reels_format_benchmarks.md)).
- **Faceless-Theme-Pages schneiden messbar schwächer ab** (Korrelation). Theme-Pages liegen bei ≈0,74, Lifestyle-Creator bei
  ≈1,24. Wir setzen deshalb auf eine Studio-Identität, Serien und menschlichen Maßstab im Bild, nicht auf ein Gesicht. Ob das
  den Abstand ausgleicht, zeigt erst der eigene Test.
- **KI-Content ist kein Vorteil an sich.** KI gegenüber realen Aufnahmen: ≈0,92×, n.s. Ein Vorteil zeigt sich in den Daten nur
  dort, wo KI zeigt, was real nicht möglich ist.
- **Möbel-Affiliate allein trägt nicht.** Der Umsatzpfad ist ein Mix (siehe K).
- Die geprüften Alternativsegmente:

| Segment | Urteil | Begründung |
|---|---|---|
| Future Architecture | Kern (P1) | nur als Konzept, nicht als Label: Future-Arch-Topicseiten sind verkrustet (neue Reels ≈0,59) |
| AI Landscaping/Outdoor | starker zweiter Pfeiler (P3, GO) | KI-Garten ≈1,61, Bad ≈1,45; Garten-Seiten füllen sich aber schnell (49 % KI) |
| Dream Bedrooms | nur als Variante in P2 (Pick One) | KI-Schlafzimmer ≈0,77; dream-bedrooms zu 92 % KI, 0 % junge Top-Reels |
| Luxury Hotels / Future Resorts | nein (REJECT) | KI-Hotels ≈0,58 (n=9, geringe Konfidenz), neue Hotel-Reels ≈0,71; Realitäts- und Irreführungsrisiko |
| Luxury Kitchens | nein (für KI) | KI-Küche ≈0,67 |
| Cozy Ambience | nur Wildcard (P5) | hohe Nachfrage, aber KI-Cozy ≈0,68 vs. real ≈1,82, Sättigung und Decay |

---

## Nächste Schritte

1. Positionierung bestätigen: empfohlen ist **K1 *The Unbuilt*** (Arbeitstitel; 26/35 in der Vergleichsmatrix vor K2 *From
   Nothing* 22, K3 *One of Three* 21, K5 *Concept Villas* 17 und K4 *After Rain* 13). K3 und K2 laufen als Pillars P2 und P3,
   K5 nur als B2B-Portfolio-Schicht ([10 §9–11](10_market_gaps.md)). Handle-Verfügbarkeit prüfen (`UNKNOWN`).
2. Style Guide umsetzen: Prompt-Blöcke in [11_brand_style_guide.md](11_brand_style_guide.md), QA-Checkliste in
   [16_automation_strategy.md](16_automation_strategy.md).
3. Produktion der ersten 21 Reels (Woche 1) nach dem [Launchplan](14_30_day_launch_plan.md); Konzepte, Hooks und Titel aus
   [12_100_content_ideas.csv](12_100_content_ideas.csv) (100 Ideen, verteilt 35/20/20/15/10 auf P1–P5).
4. Winner-Database ab Reel 1 führen. Wöchentlicher Review plus [Konkurrenzmonitor](17_competitor_monitor.md), und zwar über
   die offizielle Graph API (Business Discovery) oder manuell, **nicht** als automatischer Web-Sweep. Instagrams `robots.txt`
   verbietet automatisierte Erhebung ohne schriftliche Erlaubnis (siehe [README – Compliance](README.md)).
