# 00 – Executive Summary & Entscheidung (Teil 35)

**Stand:** 25.09.2026 · **Datenbasis:** 2.498 Reels von 239 öffentlichen Instagram-Topic-Seiten (davon 2.393 visuell codiert,
2.397 mit Followerzahl), 1.985 Accounts, 72 tief profilierte Accounts, 9 Recherche-Notizen mit Faktencheck, YouTube-Shorts-Proxy
(12 Kanäle, 713 Shorts). Methodik und Grenzen stehen in der [README](README.md), alle Zahlen in
[analysis_digest.md](data/processed/analysis_digest.md) und [key_contrasts.csv](data/processed/stats/key_contrasts.csv).

**Lesehilfe:** `adj_factor` = Views im Verhältnis zur Erwartung für die Accountgröße auf derselben Topic-Seite
(1,0 = wie erwartet, 2,0 = doppelt so viele). Alle Aussagen beziehen sich auf Reels, die es auf Topic-Seiten geschafft haben
(Selektionsbias). Es sind Korrelationen und damit Hypothesen, keine Kausalbeweise.

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
   (p=0,008). Architektur ist zudem das frischeste Feld: 57 % der Top-Reels sind jünger als 180 Tage, neue Reels liegen bei ≈1,5×.
5. **Die Identität schlägt das Motiv.** Faceless-Theme-Pages liegen bei ≈0,74 (n=503), KI-Creator/Studios bei ≈1,09 (n=276).
   Der Kontrast beträgt ≈0,68× (p<0,001). Stil, Raum, Location, Farbtemperatur und Posting-Zeit zeigen dagegen **keinen**
   signifikanten Effekt.
6. **Choice-Mechaniken ziehen Kommentare.** „Pick one“-Hooks bringen ≈5,7× mehr Kommentare pro View (p<0,0001). Der Effekt
   auf die Views (≈1,65×) ist knapp nicht signifikant.
7. **Kaufbarkeit kostet keine Reichweite.** Reels mit hoher und niedriger Shoppability performen gleich (≈1,02×, p=0,91).
   Schwach ist nicht das Kaufbare, sondern der generische KI-Realismus-Look.
8. **KI-Theme-Pages zeigen Decay.** Mehrere KI-Cozy- und Interior-Accounts brachen nach ihren 2024-Hits stark ein.
   Beispiele: cozyzen.ai von 4,1 Mio. auf 18–27K Views, kohlectcabins von 23,8 Mio. auf 70,6K. Ähnliches zeigen
   YouTube-Kanäle. Ein Einheits-Look verbrennt schnell, gebraucht wird eine **Novelty-Engine**.

---

## A. Ist Interior/Luxury Homes aktuell eine interessante Nische für einen KI-Theme-Account?

**Ja, aber nicht in der geplanten Form.** Reichweite, Frische und KI-Eignung sprechen dafür. Dagegen sprechen:
- ein gesättigter KI-Interior-Mainstream,
- Theme-Pages mit strukturell schwächerer Performance,
- sichtbarer Decay bei KI-Accounts,
- Plattformregeln (Originalität, KI-Labels, siehe [q01](quellen/q01_instagram_platform_rules.md)),
- ein dünnes Möbel-Affiliate-Modell (Amazon Furniture/Home 3 %, 24-h-Cookie, siehe [q02](quellen/q02_furniture_affiliate_commerce.md)).

Attraktiv ist die Nische deshalb nur als **originäres KI-Architektur-/Design-Studio** mit unmöglichen, konzeptionellen Häusern
und nicht als Repost- oder „Pretty-Rooms“-Seite. Details: [01_market_analysis.md](01_market_analysis.md).

## B. Welche Unter-Nische ist anhand der Daten am attraktivsten?

**„Impossible Homes“ (konzeptionelle, unmögliche Architektur).** Dazu gehören Häuser in Fels oder an Klippen, Türme,
alpine Konzepte und unterirdische Oasen, außen und innen, jeweils mit menschlichem Maßstab. Unterwasser-Konzepte gehören nicht dazu, sie sind schwach (adj ≈0,39, n=14). Das Segment ist das stärkste KI-Segment
(≈2,3×), das frischeste Feld (Architektur) und am wenigsten mit dem gesättigten Interior-Mainstream verwechselbar.

Zweiter Pfeiler: **Outdoor, Bad und Treppen sowie Transformationen** („from nothing to dream space“). KI-Outdoor, -Bad, -Treppen
und -Pool liegen bei ≈2,1× gegenüber KI-Schlaf-, Wohnzimmer und Küche (p<0,001, post-hoc gebildet; im eigenen Test bestätigen).

## C. Wo ist der Wettbewerb relativ zur Nachfrage am geringsten?

Die Topic-Seiten mit hohen Views und wenigen konkurrierenden Reels sind unten gelistet. Kleine Reel-Zahlen entsprechen oft
engen Suchphrasen, deshalb sind das Indikatoren, keine Marktgrößen.

| Topic | Median-Views | Reels zum Thema |
|---|---|---|
| ai-interior-designer | 935K | 700 |
| futuristic-houses | 575K | 650 |
| cozy-rain | 3,85 Mio. | 23K |
| dream-bedrooms | 1,12 Mio. | 9,5K |
| lake-como-villa | 2,42 Mio. | 25K |

Strukturell offen ist die Kombination aus **KI + fantastischer Architektur + Studio-Identität + Serienformat**. Die meisten
KI-Accounts sind Theme-Pages im gesättigten Dreamy-Interior-Look. Liste mit Begründungen: [10_market_gaps.md](10_market_gaps.md).

## D. Welche Arten von Reels wachsen am stärksten?

Gemessen am Anteil der Top-Reels aus den letzten 180 Tagen und an deren adj:

| Feld | Anteil letzte 180 Tage | adj neuer Reels | Einordnung |
|---|---|---|---|
| Architektur | 57 % | ≈1,53 | wächst |
| Cozy-Ambience | 44 % | ≈1,11 | wächst, aber 67 % der neuen Reels sind KI (Sättigung) |
| Unusual Homes | 38 % | ≈1,09 | wächst |
| Generische Räume | 32 % | ≈1,38 | wächst |
| KI-Topic-Seiten | 27 % | ≈0,72 | verkrustet |
| Luxury Rooms | 24 % | ≈0,80 | verkrustet |
| Hotels | 30 % | ≈0,71 | verkrustet |
| Future-Arch-Topicseiten | 22 % | ≈0,59 | verkrustet |

Siehe [05_viral_patterns.md](05_viral_patterns.md) und [01_market_analysis.md](01_market_analysis.md).

## E. Welche Styles funktionieren am besten?

Stil ist insgesamt **nicht signifikant**. Die Tendenzen:

| Gruppe | Stile (adj) |
|---|---|
| Über alle Reels vorn | warm luxury ≈1,8 (n=34), neoclassical ≈1,6, mid-century ≈1,5, traditional-regional ≈1,3, minimalist ≈1,2 |
| Innerhalb KI vorn | glam ≈1,95, warm luxury ≈1,85, tropical ≈1,70, futuristic ≈1,06 |
| Schwach | modern luxury ≈0,83 (n=566, der häufigste Stil), organic modern ≈0,79, mediterranean ≈0,80, japandi ≈0,77, dark luxury ≈0,67 |
| Innerhalb KI schwach | Scandinavian ≈0,28, organic modern ≈0,57 |

Konsequenz: den generischen „Modern-Luxury-Beige“-KI-Look vermeiden. Siehe [06_visual_styles.md](06_visual_styles.md).

## F. Welche Video-Längen funktionieren?

**Auf Instagram öffentlich nicht messbar (UNKNOWN).** Nur als Proxy aus YouTube-Shorts vergleichbarer Kanäle, konfundiert mit
Kanal und Format:
- Kurze Loops liegen über dem Kanal-Median: 0–12 s ≈2–19×, bei kleinen n.
- 13–20 s liegen darunter (≈0,22).
- Clips mit wenig Bildwechsel (statisch oder langsam) ≈1,67, viele Schnitte ≈0,40.
- Die NexLev-Stichprobe (7 Instagram-Reels) lag bei 7–23 s mit überwiegend ruhigen Einstellungen.

→ **Testvariable** in der [Testing-Matrix](13_testing_matrix.csv): 7–9 s Loop vs. 12–15 s vs. 20–30 s.

## G. Welche Hooks funktionieren?

**Stärker:**
- **Choice** („Which one would you move into?“): Kommentare ≈5,7× (signifikant)
- Status ≈1,37
- Money/Price ≈1,2–1,3 (n.s.)
- Visuell: unmögliche Architektur, Reveal, menschliche Figur. Bei KI erreichen Reels mit Personen ≈1,68× (p≈0,02).

**Schwächer:**
- Reine Location-Caption ≈0,63
- Instructional ≈0,72
- Contrarian ≈0,70
- Text-lastige Cover ≈0,92 (n.s.; innerhalb von Accounts −13 Pp. in den Top-10 %)
- Split-Screen-Vorher/Nachher-Cover ≈0,56 (n=22)
- Fensterblick-Klischee ≈0,70 (signifikant)

Bibliothek mit 50 Text-Hooks und 30+ visuellen Hooks: [07_hooks.md](07_hooks.md).

## H. Welche Räume funktionieren?

Über alle Reels vorn: Bad ≈1,43 (n=60), Treppen/Hallen ≈1,17. Hinten: Esszimmer ≈0,69, Home-Theater ≈0,49,
Wohnzimmer ≈0,80. Innerhalb KI sind Treppen/Hallen, Garten, Bad, Pool und Terrasse stärker als Schlafzimmer (≈0,77),
Wohnzimmer (≈0,69) und Küche (≈0,67). Der Raum ist insgesamt nicht signifikant. Er ist ein Gestaltungshebel, kein Garant.

## I. Welche Locations funktionieren?

Nicht signifikant. Tendenzen:
- **Vorn:** Schweiz ≈1,84 (n=16), Tulum/Mexiko ≈1,24, Tokyo ≈1,19, Bali ≈1,11, Dubai ≈1,10 (n=97), Lake Como ≈1,07.
- **Schwach:** London ≈0,58, Nordics ≈0,52, Maldives ≈0,81.
- Indien (≈1,95, n=48) beruht überwiegend auf realen Designer-Accounts.

Location als **Setting** nutzen, nicht als Hook (Location-Captions ≈0,63).

## J. Fantasy oder Realistic Luxury?

**Fantasy für die Reichweite, Realismus für den Commerce, und nie der generische KI-Realismus-Look.**

| Realismus | adj |
|---|---|
| Fantasy/impossible | ≈2,1 (n=62) |
| Aspirational-realistic | ≈1,00 |
| Real existing | ≈0,95 |
| Stylized dreamy | ≈0,70 |

Die Hypothese „Fantasy bringt mehr Views“ wird **gestützt**. Die Hypothese „Realismus verkauft mehr Möbel“ lässt sich mit
öffentlichen Daten **nicht messen** (keine Klick- oder Kaufdaten). Fantasy-Reels sind aber zu 95 % „low shoppability“ (n=62),
während Shoppability selbst keine Reichweite kostet. Details: [06_visual_styles.md](06_visual_styles.md), Teil 18.

## K. Welcher Mix ist optimal zwischen Viralität und späterer Möbel-Monetarisierung?

**Start (30 Tage):** ≈65 % Reichweite und ≈35 % commerce-nahe Formate.
- **Reichweite:** P1 Impossible Homes 35 %, P4 Night Stories 15 %, P5 Wildcards 10 %.
- **Commerce-nah:** P2 Pick One 20 %, P3 Dream Builds/Transformations 20 %.
- **Hybrid-Test:** „Impossible places, possible furniture“, also eine unmögliche Hülle mit kaufbaren Hero-Stücken.

**Ab Monat 2:** 60–70 % Reichweite und 30–40 % commerce-nah, je nach Winner-Database.

Der Umsatz kommt realistischerweise zuerst aus KI-Tool-Sponsorings und -Affiliates, B2B-Visualisierung und digitalen
Produkten. Möbel-Affiliate folgt ergänzend über Comment-Keyword-DM-Funnels. Siehe [09_monetization.md](09_monetization.md) und
[08_content_pillars.md](08_content_pillars.md).

## L. Wie sollte unser visueller Stil aussehen?

Ein wiedererkennbares **„Nocturnal Impossible Architecture“**-System:
- **Licht:** warmes künstliches Nachtlicht und Blue Hour (Nacht/künstlich ≈1,14; n.s., innerhalb von Accounts +12 Pp.).
- **Palette:** warm-neutrale Materialien (Travertin, Walnuss, Messing) gegen tiefes Nachtblau. Das ist eine Markenentscheidung,
  denn die Farbtemperatur selbst zeigt keinen Effekt.
- **Formen:** unmögliche Strukturen, Treppen als Hero-Element.
- **Mensch:** eine kleine menschliche Figur für Maßstab und Story.
- **Cover:** ohne Text-Wände.
- **Serie:** Nummerierung („Unbuilt No. 017“) und ein konstanter Abschluss-Shot.

Vollständig: [11_brand_style_guide.md](11_brand_style_guide.md).

## M. Welche 3 Formate sollten wir zuerst testen?

1. **„Unbuilt No. X“**: Impossible-Home-Reveal, 8–12 s, langsamer Push-in/Fly-through, Nacht, Figur, Curiosity- oder Price-Hook
   (als Konzept gekennzeichnet).
2. **„Pick One“**: drei Varianten desselben Raums oder Hauses, Choice-Hook, Kommentar-CTA. Eine Variante enthält kaufbare Stücke.
3. **„From Nothing“**: Transformation eines leeren Orts zum Traum-Außenraum, Bad oder Pool, 12–20 s, sequenzieller Reveal
   statt Split-Screen.

## N. Wie sollte unser 30-Tage-Test aussehen?

3 Reels/Tag, also 90 Reels. Die Wochen sind so aufgebaut:
- **Woche 1:** breite Tests über alle 5 Pillars mit Ein-Variablen-A/B (Hook, Stil, Raum, Länge, Licht, Mensch, Cover-Text).
- **Woche 2:** Schwache Formate werden gestrichen (KILL), wenn Follows/1.000 Views und Views/Follower unter 50 % des eigenen
  rollierenden Medians liegen.
- **Woche 3:** Gewinner verdoppeln (Serien ausbauen).
- **Woche 4:** Gewinner skalieren und neue Varianten der Top-Formate einführen (Novelty-Engine).

Messung über die [Winner-Database](data/winner_database_template.csv) mit
[winner_analysis.py](scripts/winner_analysis.py). Wöchentlich läuft der [Konkurrenzmonitor](17_competitor_monitor.md) mit.
Details und Tagesplan: [14_30_day_launch_plan.md](14_30_day_launch_plan.md) und [13_testing_matrix.csv](13_testing_matrix.csv).

---

## Die unbequeme Wahrheit (bewusst gegen die Ursprungsidee geprüft)

- Der größte Einzeltreiber von Views ist die **Accountgröße** (ρ≈0,43; 1M+-Accounts haben den ≈9-fachen Topic-Index von
  <10K-Accounts). Ein neuer Account startet also mit dem schwächsten Hebel. Die ersten Wochen hängen an einzelnen Durchbrüchen.
- **Faceless** ist ein messbarer Nachteil. Theme-Pages liegen bei ≈0,74, Lifestyle-Creator bei ≈1,24. Wir kompensieren das mit
  einer Studio-Identität, Serien und menschlichem Maßstab im Bild, nicht mit einem Gesicht.
- **KI-Content ist kein Vorteil an sich.** KI gegenüber realen Aufnahmen: ≈0,92×, n.s. Der Vorteil entsteht nur, wenn KI
  zeigt, was real nicht möglich ist.
- **Möbel-Affiliate allein trägt nicht.** Der Umsatzpfad ist ein Mix (siehe K).
- Die geprüften Alternativsegmente:

| Segment | Urteil | Begründung |
|---|---|---|
| Future Architecture | Kern | wenn konzeptionell |
| AI Landscaping/Outdoor | starker zweiter Pfeiler | |
| Dream Bedrooms | nur als Choice-Format | |
| Luxury Hotels | schwach | ≈0,71–1,05, Realitäts- und Irreführungsrisiko |
| Luxury Kitchens | schwach bei KI | ≈0,67 |
| Future Resorts | nur als Teil von P1 | |

---

## Nächste Schritte

1. Positionierung und Namen aus den 5 Konzepten in [10_market_gaps.md](10_market_gaps.md) wählen.
2. Style Guide umsetzen: Prompt-Blöcke in [11_brand_style_guide.md](11_brand_style_guide.md), QA-Checkliste in
   [16_automation_strategy.md](16_automation_strategy.md).
3. Produktion der ersten 21 Reels (Woche 1) aus [12_100_content_ideas.csv](12_100_content_ideas.csv) nach dem
   [Launchplan](14_30_day_launch_plan.md).
4. Winner-Database ab Reel 1 führen. Wöchentlicher Review plus [Konkurrenzmonitor](17_competitor_monitor.md), und zwar über
   die offizielle Graph API (Business Discovery) oder manuell, **nicht** als automatischer Web-Sweep. Instagrams `robots.txt`
   verbietet automatisierte Erhebung ohne schriftliche Erlaubnis (siehe [README – Compliance](README.md)).
