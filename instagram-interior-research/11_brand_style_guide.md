# 11 – Brand Style Guide (Teil 23)

> **Stand:** 25.09.2026 · **Arbeitstitel der Marke:** *The Unbuilt*, ein AI-Architektur-Studio für *„Homes that shouldn't exist (yet)“* (Strategy Brief §3; der Name ist austauschbar, das System nicht)
> **Ziel dieses Teils:** ein **eigenes, wiedererkennbares** Stilsystem. Nach wenigen Wochen sollen Zuschauer sagen: *„Das ist wahrscheinlich von diesem Account.“* Abgeleitet wird es aus **Prinzipien**, die in den Daten funktionieren, nicht aus den Creatives anderer Accounts.
> **Zahlenquellen:** [analysis_digest.md](data/processed/analysis_digest.md), [key_contrasts.csv](data/processed/stats/key_contrasts.csv), KI-spezifische Werte aus [ai_segments.csv](data/processed/stats/ai_segments.csv) und [ai_style_contrasts.csv](data/processed/stats/ai_style_contrasts.csv) (erzeugt mit [scripts/pillar_style_stats.py](scripts/pillar_style_stats.py) aus [04_reel_database.csv](04_reel_database.csv)), dazu die Research-Notizen [q01](quellen/q01_instagram_platform_rules.md)–[q09](quellen/q09_reels_format_benchmarks.md).
> **Status-Tags:** `[VERIFIED]` · `[ESTIMATED]` (KI-gestützte Codes, eigene Ableitungen, Hausregeln) · `[THIRD-PARTY ESTIMATE]` · `[PROXY]` (YouTube) · `[UNKNOWN]`
> **Verwandte Teile:** Content Pillars (Teil 24) in [08_content_pillars.md](08_content_pillars.md) · KPI-System in [15_kpi_framework.md](15_kpi_framework.md) · Pipeline, QA und Prompt-Bibliothek in [16_automation_strategy.md](16_automation_strategy.md)

---

## 0. Kurzfassung: die Signatur-Formel

> **Glow gegen Blau** + **eine unmögliche Geste** + **eine kleine Figur** + **Seriennummer** + **„Last Light“-Ende**

| # | Signatur-Element | Regel in einem Satz | Datenanker |
|---|---|---|---|
| 1 | **Glow gegen Blau** | Warmes Architekturlicht (Bernstein) liegt direkt vor tiefem Nachtblau, in jedem ersten und letzten Frame. | KI-Nachtlicht 1,27 (n = 93) vs. übrige KI 0,82 (p = 0,046, post-hoc). Farbtemperatur selbst ist neutral (1,04×, n.s.) → **Markenentscheidung**. |
| 2 | **Eine unmögliche Geste** | Pro Reel bricht genau ein architektonisches Element eine Regel, lesbar in 1 Sekunde. | KI fantasy/impossible 3,25× gegenüber dreamy (signifikant) |
| 3 | **„The Visitor“** | Eine kleine Figur in Rückenansicht, ohne Gesicht, gibt Maßstab und Story. | KI mit Personen 1,68× (p = 0,02 nominal; 95-%-KI 0,99–2,53 berührt 1); Person auf dem Cover 2,05× (p = 0,02, post-hoc) |
| 4 | **Serien-Badge** | `UNBUILT · No. 017 · AI CONCEPT`, immer an derselben Stelle, in derselben Schrift, ab Frame 0 | Theme-Page vs. AI-Creator 0,68× (signifikant); KI-Label bei erster Exposition ([q07](quellen/q07_legal_ai_risk.md)) |
| 5 | **„Last Light“-Ende** | In den letzten 1,5–2 s fährt die Kamera zurück, bis das Haus ein einzelner warmer Punkt in der Nacht ist. | Wiedererkennung `[ESTIMATED]`; kein Loop (Monetarisierungsregel, [q01](quellen/q01_instagram_platform_rules.md)) |

**Wichtig zur Einordnung:**
- Die meisten Stilfaktoren sind in den Daten **nicht signifikant**, wenn man die Accountgröße herausrechnet: Stil p = 0,17, Farbtemperatur p = 0,91, Helligkeit p = 0,60, Licht p = 0,09, Caption-Hook p = 0,35 ([Digest §1](data/processed/analysis_digest.md)).
- Dieser Style Guide ist deshalb vor allem ein **Wiedererkennungs- und Qualitätssystem**. Wo Daten eine Richtung zeigen, folgt er ihr. Wo nicht, entscheidet die Marke.
- Alles, was als Hebel wirken soll, wird **getestet** (§21), nicht geglaubt.

---

## 1. Herleitung: Prinzip statt Kopie

Jede Regel unten folgt aus einem **beobachteten Muster** in den Daten, nicht aus dem Look eines bestimmten Accounts.

| Beobachtetes Muster (Daten) | n | Prinzip | Unsere Umsetzung |
|---|---|---|---|
| KI fantasy/impossible 2,27 vs. stylized dreamy 0,70 vs. aspirational realistic 0,90 | 53 / 305 / 328 | Die Unmöglichkeit muss **sofort** sichtbar sein. Weiche Traumoptik ist das Schwächste. | Eine klare, scharf gezeichnete unmögliche Geste im ersten Frame; kein Haze, kein Bloom |
| Fensterblick 0,70× (nominal signifikant, p = 0,02; nicht Bonferroni-robust); KI-Cover mit „View Reveal“ 0,56 | 306 / 118 | Der Blick aus dem Fenster ist verbraucht. | Das Haus **selbst** ist das Motiv, nicht die Aussicht |
| KI Treppe/Halle 2,24, Garten 1,61, Bad 1,45 vs. Wohnzimmer 0,69, Küche 0,67, Schlafzimmer 0,77 | 16 / 43 / 28 vs. 123 / 31 / 110 | Statement-Räume statt Alltagsräume (post-hoc) | Treppen, Bäder, Pools und Gärten als Hero-Räume |
| KI-Stile warm luxury 1,85, tropical 1,70, futuristic 1,06 vs. modern luxury 0,79, organic modern 0,57, scandinavian 0,28 | 15 / 20 / 58 vs. 128 / 56 / 16 | Der häufigste KI-Stil ist ein „Meer der Gleichheit“ (Gruppenkontrast 2,47×, post-hoc). | Eigener Hausstil „Warm Monolith“ statt Beige-Minimalismus |
| Theme-Page 0,74 vs. AI-Creator 1,09 | 503 / 276 | Identität geht in den Daten mit höheren Werten einher als Anonymität (Korrelation, keine Kausalität). | Studio-Auftritt mit Serien, Nummern, Signatur |
| Text-Overlay auf dem Cover 0,92× (n.s.); innerhalb derselben Accounts −13 Pp bei den Top-10 % | 986 / 28 Top-Reels | Text hilft nicht messbar. | Minimaler Text, das Bild trägt |
| Before/After-Split-Cover 0,53 (Kontrast 0,56×, p = 0,07, nicht signifikant) | 22 | Split-Screen teilt das Einzelmotiv; die Daten zeigen nur eine Richtung. | Transformationen laufen nacheinander, nie geteilt |
| Formatverschleiß nach 2024-Hits (z. B. @cozyzen.ai 4,1 Mio. → 18–27 Tsd.) | Fallstudien | Ein Einheitslook altert. | **Konstante Signatur, wechselnde Konzepte** (Novelty-Engine) |

**Regel gegen das Kopieren:**
- Keine Referenzbilder anderer Accounts in Prompts oder Image-to-Image.
- Keine Namen von Architekten (lebend oder verstorben), Studios oder Marken im Prompt. Laut designboom wird Zaha Hadid in 4,9 Mio. ausgewerteten Midjourney-Prompts 63.103-mal referenziert ([q06](quellen/q06_ai_theme_page_case_studies.md) §2.6, `[VERIFIED – Sekundärquelle]`). Zum Markenrisiko siehe [q07](quellen/q07_legal_ai_risk.md) §2.4.
- Der Ähnlichkeits-Check gegen Wettbewerber läuft nach [16 §4.4](16_automation_strategy.md).

---

## 2. Farben

![Farbtemperatur vs. Erwartung](charts/adj_by_palette.png)

**Was die Daten sagen:**

| Befund | Wert | Einordnung |
|---|---|---|
| Farbtemperatur, alle Reels: kühl vs. warm | 0,96 vs. 0,92 → 1,04× (0,84–1,23), p = 0,74 (n = 560 / 1.056) | **kein Effekt** |
| Nur KI-Reels: warme Palette vs. kühl + neutral | 0,75 vs. 0,97 → 0,77× (0,55–0,98), Mann-Whitney p = 0,11 (n = 378 / 308) | nicht signifikant; das KI streift knapp 1 |
| **Konfundierung** | 51 % der warmen KI-Reels sind Schlaf-/Wohnzimmer/Küche, bei den übrigen nur 23 % | Warm steht hier für das schwache Ursprungskonzept, nicht für die Farbe an sich |
| Trend-Kontext USA: Houzz-Suchen Q1 2026 vs. Q1 2025 | sandstone +257 %, rust colors +178 %, chocolate brown +153 %, Venetian plaster +94 %; Houzz-Trend Herbst 2026: „Warmth Is the New Baseline“ | `[VERIFIED]` ([q04](quellen/q04_interior_trends_demand.md) §2.4) |
| Trend-Kontext Pinterest | Neo Deco („edged in chrome or brass“): brass aesthetic +35 %, red marble bathroom +80 %; beiger „Quiet Luxury“-Minimalismus gilt als reif | `[VERIFIED]` Suchanstiege; Einordnung `[ESTIMATED]` ([q04](quellen/q04_interior_trends_demand.md) §2.1, §5) |

**Entscheidung:**
- **Die Wärme kommt aus dem Licht, nicht aus dem Grading.** Die Oberflächen bleiben steinig-neutral, der Himmel ist nachtblau.
- Warm sind nur die Lichtquellen und wenige Messing- und Oxid-Akzente.
- Das ist eine **Markenentscheidung**, kein Performance-Hebel (Strategy Brief §2.7).

**Palette „Unbuilt Night“** (Hex-Werte sind Hausstandard; Anteile sind Richtwerte `[ESTIMATED]`)

| Rolle | Name | Hex | Anteil im Frame | Einsatz |
|---|---|---|---|---|
| Grund / Himmel | **Unbuilt Night** | `#0D1B2A` | 30–45 % | Nachthimmel, tiefe Außenschatten |
| Himmel oben / Reflexe | Deep Slate | `#1F3448` | 10–15 % | oberer Himmelsverlauf, Spiegelungen in Glas und Wasser |
| **Signaturlicht** | **Lamp Glow** | `#F2B45C` | 5–12 % | Fenster, Lichtfugen, Pendelleuchten, Poollicht (2700–3000 K) |
| Hauptmaterial hell | Travertine | `#D6C6AA` | 15–25 % | Fassaden, Böden, Wannen |
| Hauptmaterial mittel | Sandstone | `#B89468` | 5–15 % | Fels, Terrassen, Mauern |
| Material dunkel | Basalt | `#2B2926` | 5–10 % | Sockel, Treppen, Felsen |
| Holz | Walnut | `#5A3D2B` | ≤ 8 % | Möbel, Deckenflächen |
| Metall-Akzent | Brass | `#B08A4E` | ≤ 3 % | Leuchten, Beschläge, Geländer |
| Farbakzent (1 Objekt) | Oxide Red | `#8B3A2A` | ≤ 3 % | ein Hero-Objekt, z. B. ein Marmorblock oder eine Keramik |
| Vegetation (nur P3) | Olive Leaf | `#5E6A45` | ≤ 10 % | Oliven, Gräser |
| Text | Paper | `#F2EDE3` | – | alle On-Screen-Texte |
| Text-Akzent | Lamp Glow | `#F2B45C` | – | nur die Seriennummer |

**Farbregeln:**
1. **Glow-Regel:** Erster und letzter Frame enthalten mindestens eine Fläche in *Lamp Glow*, die direkt an *Unbuilt Night* grenzt.
2. **Kein Gesamt-Grading ins Orange oder Beige.** Die Neutralen (Travertin, Basalt) bleiben neutral. Prüfpunkt: Das Farbhistogramm des Keyframes liegt im Brand-Board ([16 §4.2](16_automation_strategy.md), Markencheck 1).
3. **Kein Rosa- oder Lila-Dämmerungshimmel.** Das ist eine Markenentscheidung; zur Richtung: Lila 0,82 (n = 74, alle Reels), dominante Farben sind nicht auf Signifikanz getestet.
4. **Maximal ein Farbakzent** (Oxide Red) pro Reel, sonst verliert der Glow-Kontrast.
5. Grün nur in P3-Gärten, nie als Wandfarbe.

---

## 3. Licht

![Licht vs. Erwartung](charts/adj_by_lighting.png)

| Befund | Wert (adj) | n | Einordnung |
|---|---|---|---|
| Nacht/Kunstlicht, alle Reels | 1,14; vs. Tageslicht 1,21× (0,94–1,59), p = 0,12 | 387 | nicht signifikant |
| **Nacht/Kunstlicht, nur KI** | **1,27** vs. übrige 0,82 → 1,55× (0,97–2,50), p = 0,046 | 93 | post-hoc, Richtung |
| KI Blue Hour / Golden Hour / Tageslicht | 0,89 / 0,82 / 0,90 | 101 / 84 / 143 | Dämmerung ist nicht dasselbe wie Nacht mit Kunstlicht |
| KI Mischlicht / Bedeckt-Regen / Kerze | 0,77 / 0,70 / 0,32 | 186 / 65 / 14 | unklares oder düsteres Licht meiden (Kerze: geringe Konfidenz) |
| **KI Helligkeit:** mittel / hell / dunkel | 0,98 / 0,82 / 0,73 | 359 / 224 / 103 | „Nacht“ heißt **nicht dunkel**: Architektur muss lesbar bleiben (n.s., Richtung) |
| Innerhalb derselben Accounts: Nachtlicht in den Top-10 % | +12 Pp | 28 Top-Reels | Richtung |
| KI-Ambience-FX: Nebel / Schnee / Kamin / Regen | 0,73 / 0,70 / 0,67 / 0,63 | 68 / 51 / 70 / 49 | Wetter-FX nicht als Standard |

**Lichtregeln:**
1. **Standard:** späte Blue Hour bis Nacht (Strategy Brief §5). Der Himmel ist tiefblau und klar, ohne Dämmerungsverlauf ins Rosa oder Orange. Das Kunstlicht des Gebäudes dominiert und ist die einzige warme Lichtquelle (2700–3000 K). Solche Szenen würden im Codebook als `night_artificial` codiert, nicht als `blue_hour` (KI 1,27 vs. 0,89).
2. **Sichtbare Lichtquellen** (Pendel, Lichtfugen, Wandfluter, Poollicht). Sie begründen das Licht, und Leuchten sind **kaufbar** (Abschnitt 6).
3. **Mittlere Belichtung:** Fassadenkanten, Materialien und Figur bleiben lesbar. Keine abgesoffenen Schatten, kein Halo und kein Bloom um Lichtquellen.
4. **Eine Lichtlogik pro Szene.** Keine Sonnenflecken bei Nachthimmel (QA-Punkt 7 in [16 §4.3](16_automation_strategy.md)).
5. **Ausnahme Tageslicht:** nur in P3-Transformationen für die Rohzustände. Die Sequenz endet immer in der Nacht (**Tag-Nacht-Bogen**).
6. Keine Kerzen- oder Kamin-Szenen als Hauptlicht, kein Nebel, Regen oder Schnee als Standard-Effekt. Erlaubt nur als Wildcard in P5.

---

## 4. Materialien

![Materialien vs. Erwartung (alle Reels)](charts/adj_by_material.png)

| Befund | Wert | n | Einordnung |
|---|---|---|---|
| KI + Marmor sichtbar vs. nicht | 1,18 vs. 0,83 → 1,42× (0,89–2,13), p = 0,50 | 101 / 585 | nicht signifikant |
| KI Naturstein / Holz / Glas / Putz / Leder | 0,89 / 0,80 / 0,74 / 0,71 / 0,69 | 267 / 439 / 504 / 114 / 42 | Multi-Label, nicht getestet: nur Richtung |
| Glas ist das häufigste KI-Material und liegt unter dem Median | 0,74 | 504 | „Glasbox“ ist Standardware |
| Innerhalb derselben Accounts, Top-10 % vs. untere 50 % | Marmor +7 Pp · Pflanzen −14 Pp · Wasser −16 Pp · Feuer −12 Pp | 28 Top-Reels | Richtung |
| Trend (Houzz, USA) | sandstone +257 %, Venetian plaster +94 %, limewash +53 %; Kurven: scalloped tile mehr als verdreifacht (Houzz nennt nur den Faktor), arched range hood +177 % | – | `[VERIFIED]` ([q04](quellen/q04_interior_trends_demand.md) §2.4) |

**Material-Kanon (Hausstil „Warm Monolith“):** geschliffener Travertin, Sandstein, dunkler Basalt, Nussbaum, gebürstetes Messing, Kalkputz. Dazu **ein** Statement-Stein pro Reel, z. B. geäderter Marmor oder ein rotoxidierter Block.

**Regeln:**
1. **„3 + 1“:** höchstens drei Grundmaterialien und ein Statement-Material pro Szene.
2. **Masse statt Glas:** Glas nur als Öffnung oder Spalt in massiver Wand, nie als ganze Hülle.
3. **Wasser als Spiegel**, nicht als Pool-Klischee: dunkle, ruhige Fläche, die das Licht spiegelt. Pool-Cover liegen bei KI bei 0,73 (n = 81).
4. **Kurven sparsam:** eine gerundete Form pro Raum (Bogen, Wendeltreppe, gerundete Wanne) als Trend-Anschluss.
5. Materialien müssen **physikalisch lesbar** bleiben: Fugen, Maserung, Kontaktschatten. Rund die Hälfte der Codierer-Begründungen für „KI“ lautete „übermäßig glatt, wachsartig, too perfect“ ([16 §4.3](16_automation_strategy.md)). Laut Houzz gilt zudem „character and personality matter more than perfection“ ([q04](quellen/q04_interior_trends_demand.md) §2.4). Leichte Patina und Gebrauchsspuren sind deshalb erwünscht.

---

## 5. Architektur-Vokabular

**Prinzip:** eine **Geste** pro Entwurf. Sie muss sich in einem Satz beschreiben und in einer Sekunde sehen lassen.

| Geste (DE) | Prompt-Vokabel (EN) | Pillar | Hinweis |
|---|---|---|---|
| In den Fels geschnitten | *"carved into a single granite outcrop, one clean cut revealing the interior"* | P1 | Findling oder Bergrücken statt Klippenrand |
| Auskragung über Leere | *"a long cantilever over empty air, the steel structure honestly visible"* | P1 | Tragwerk sichtbar (QA-Punkt 3), außer bewusst unmöglich |
| Hängendes Haus | *"suspended from a stone arch spanning two ridges"* | P1 | |
| Gestapelte Steinkörper | *"stone volumes stacked off-axis down a mountain slope"* | P1/P3 | |
| Ring ums Loch | *"a circular house wrapped around a sunken garden"* | P1/P3 | |
| Wasserfall-Haus | *"a house that holds a waterfall inside its central void"* | P1 | |
| Schwelle als Tunnel | *"entry through a rock tunnel lit by a single warm line"* | P1/P4 | Eingang als Rätsel (`The Way In`) |
| Wendeltreppe in die Tiefe | *"a spiral stone stair descending around a top-lit void"* | P1/P6 | KI Treppe/Halle 2,24 (n = 16) |
| Terrassen-Kaskade | *"sandstone terraces cascading to a long dark pool"* | P3 | KI Garten 1,61 (n = 43) |
| Steinbad | *"a double-height bath carved into rock, freestanding tub under one pendant"* | P2/P6 | KI Bad 1,45 (n = 28) |

**Settings (KI-Werte, post-hoc, Richtung)**

| Bevorzugen | Nicht als Standard |
|---|---|
| Berg 1,72 (n = 33), Küste 1,81 (n = 26); zusammen 2,21× vs. Rest (p = 0,018) | Klippe 0,48 (n = 35) |
| Über den Wolken / Sternenhimmel 3,42 (**n = 7**, nur als Test in P5) | Wald 0,58 (n = 63) |
| | Wüste 0,68 (n = 22) |
| | Schnee 0,70 (n = 45) |
| | Dschungel 0,73 (n = 33) |
| | Skyline 0,77 (n = 49) |
| | Unterwasser 0,39 (n = 7, geringe Konfidenz) |

**Stil-Codes** (für die Winner-DB, Codebook aus [15 §5.2](15_kpi_framework.md)):

| Status | Codes (KI-Werte) |
|---|---|
| Erlaubt | `warm_luxury` (1,85, n = 15) · `futuristic` (1,06, n = 58) · `tropical` (1,70, n = 20) |
| Ausgeschlossen | `modern_luxury` (0,79, n = 128) · `organic_modern` (0,57, n = 56) · `scandinavian` (0,28, n = 16) · `japandi` (0,61, n = 15) · `mediterranean` (0,69, n = 28) · `dark_luxury` (0,64, n = 31) · `classical_luxury` (0,56, n = 28) |

Stil über alle Reels ist nicht signifikant (p = 0,17). Der Gruppenkontrast bei KI ist post-hoc gebildet. **Ausnahme:** In P2 `PICK ONE` darf eine ausgeschlossene Stilwelt als bewusste Kontrastvariante vorkommen. Nachtlicht, Palette und Figur bleiben dabei gleich (deckt sich mit [06_visual_styles.md](06_visual_styles.md) §2.5).

![Stil vs. Erwartung (alle Reels)](charts/adj_by_style.png)

**Nie:**
- die generische „Glasvilla mit Infinity-Pool und Meerblick“
- reale Wahrzeichen, reale Hotels oder erkennbare reale Gebäude ([q07](quellen/q07_legal_ai_risk.md) §2.4: Innenräume realer Häuser fallen nicht unter die Panoramafreiheit)
- „in the style of“ + Name

---

## 6. Möbel und die Regel „Buyable Hero Pieces“

**Daten:** Kaufbarkeit kostet **keine messbare Reichweite**.
- Alle Reels: high vs. low 1,01× (0,80–1,25), p = 0,91.
- Nur KI: 1,22× (0,69–1,95), p = 0,78.
- Schwach ist der **generische KI-Realismus-Look**, nicht das Kaufbare (Strategy Brief §2.8).

**Hypothese:** *„Impossible places, possible furniture.“*

**Allgemeine Möbelregeln (alle Pillars):**
- Proportionen wie in der realen Welt, Kontaktschatten, keine schwebenden Objekte (QA-Punkte 2 und 3 in [16 §4.3](16_automation_strategy.md)).
- **Wenige Stücke:** eine Sitzgruppe oder ein Solitär statt voller Kataloge.
- In P1 sind Möbel skulptural und zweitrangig. Es gibt keine Kaufbehauptung.

**Regel „Buyable Hero Pieces“ für die Commerce-Pillars P2, P3 und P6:**

| # | Regel | Begründung / Quelle |
|---|---|---|
| 1 | Jedes Commerce-Reel zeigt **1–3 Hero-Stücke** aus Kategorien mit Affiliate-Chance: Leuchte, Lounge-Sessel, Outdoor-Sofa oder Daybed, freistehende Wanne oder Armatur, Teppich, Beistelltisch, Pflanzgefäß. | Der Anteil „high shoppability“ ist bei KI-Treppe/Bad am höchsten (30 %, n = 44) gegenüber 12 % aller KI-Reels ([08](08_content_pillars.md) §4) |
| 2 | Das Hero-Stück ist **≥ 2 s sichtbar**, steht im Vordergrund oder in der Mitte, liegt im Glow und wird weder vom Bildrand noch von der UI-Safe-Zone abgeschnitten. | Nur was erkennbar ist, lässt sich verlinken `[ESTIMATED]` |
| 3 | **Hero-Piece-First:** Zuerst ein reales Produkt mit exaktem Link wählen, dann die Szene darum bauen (Referenzbild oder präzise Formbeschreibung, Prompt-Block 5). | Nachträgliches Matching ist unzuverlässig, selbst Wayfair ist zurückgerudert. Bei Amazon verdient man onsite nur an der **exakten** ASIN ([q02](quellen/q02_furniture_affiliate_commerce.md) §2.7) `[VERIFIED]` |
| 4 | Passt das Stück nicht exakt, wird es als **„similar, not exact“** verlinkt und gekennzeichnet. | LTK „Exact vs Similar“; Backlash gegen Instagrams „Shop the Look“-Test ([q02](quellen/q02_furniture_affiliate_commerce.md)) |
| 5 | **Keine erkennbaren Nachbildungen geschützter Designklassiker**, keine „Dupe“-Links, keine Logos. | Urheberrecht an angewandter Kunst (EuGH *Mio/konektra*), das Risiko steigt mit Dupe-Links ([q07](quellen/q07_legal_ai_risk.md) §2.4) |
| 6 | Die Rechte am Produkt-Referenzbild vor der Nutzung als Generator-Input prüfen (Programm-AGB). | `[UNKNOWN]`, in den Quellen nicht geklärt |
| 7 | Preise nur für reale Stücke, mit Datum. Kennzeichnung „Werbung“ bzw. „Anzeige“ plus Affiliate-Hinweis. | [q07](quellen/q07_legal_ai_risk.md) §2.7; [16 §4.5](16_automation_strategy.md) |

---

## 7. Perspektiven

![Bildelemente im Cover vs. Erwartung (alle Reels)](charts/adj_by_visual_hook.png)

| Befund (KI-Cover) | Wert | n | Einordnung |
|---|---|---|---|
| Person im Cover vs. nicht | 1,63 vs. 0,79 → 2,05× (1,09–3,41), p = 0,021 | 74 / 612 | post-hoc; passt zu „KI mit Personen 1,68×“ (Key Contrasts) |
| Ungewöhnliche Architektur / Wasser im Bild | 1,00 / 1,05 | 170 / 69 | neutral bis leicht positiv |
| Außen-Reveal / Pool / Bett im Fokus / View Reveal | 0,81 / 0,73 / 0,70 / 0,56 | 234 / 81 / 108 / 118 | klassische Motive liegen unter 1 |

**Haus-Perspektiven:**

| Code | Perspektive | Einsatz | Regel |
|---|---|---|---|
| **PV1 Scale Shot** | weit, Augenhöhe 1,4–1,6 m oder leicht von unten, 24–28 mm, Figur klein im unteren Drittel | Erster Frame in P1 und P4 | Die unmögliche Geste und die Figur sind gleichzeitig im Bild. |
| **PV2 Threshold Shot** | aus dem dunklen Innenraum hinaus ins Licht bzw. durch eine Öffnung | Übergänge außen → innen | Die Schwelle rahmt, sie verdeckt nicht. |
| **PV3 Aerial 30°** | Drohnenblick etwa 30° nach unten, 35 mm | P3-Sequenzen, P1-Außenansicht | kein flacher Top-down-Blick; Horizont gerade |
| **PV4 One-Point** | zentralperspektivisch, locked-off | P2-Varianten, P6-Räume | Kamera über alle Varianten identisch |

**Immer:** stürzende Linien korrigiert, Vertikalen gerade ([16 §4.2](16_automation_strategy.md), Markencheck 3).

**Nie:** Blick durchs Fenster als Hauptmotiv (Fensterblick 0,70×, nominal signifikant), zentriertes Bett, Poolkante mit Meerhorizont.

---

## 8. Kamerafahrten

![Visuelle Veränderung vs. Performance (YouTube-Proxy)](charts/views_by_camera_yt_proxy.png)

**Datenlage:** Kamerabewegung ist auf Instagram im Research **nicht messbar** `[UNKNOWN]`. Es gibt zwei Proxys:
- **YouTube Shorts** `[PROXY]`: geringe Bildveränderung (statisch oder langsam) Median-Kanalindex 1,67 vs. viele Schnitte bzw. schnelle Bewegung 0,40 (je n = 73). Das ist **konfundiert**: Die statischen Shorts sind im Median 15 s lang, die schnellen 60 s.
- **7 per NexLev angesehene Reels**: 7–23 s, dreimal statisch, einmal Schwenk, zweimal gemischt, einmal POV-Gang ([Digest](data/processed/analysis_digest.md)). Das ist anekdotisch.

**Das Haus-Repertoire:** nur **fünf** Bewegungen. Die Begrenzung ist Teil der Wiedererkennung.

| Code | Bewegung | Einsatz | Regel `[ESTIMATED]` |
|---|---|---|---|
| **M1 Slow Push-in** | langsame Fahrt auf die Geste zu | Standard-Opener P1 | konstante Höhe, konstante Geschwindigkeit |
| **M2 Lateral Drift** | seitliches Gleiten mit Parallaxe | Innenräume, Fassaden | Vordergrund-Element für Tiefe |
| **M3 Rise Reveal** | Kran-Aufstieg von der Figur zum Gebäude | Maßstab zeigen | Start bei der Figur |
| **M4 Last Light** | Rückfahrt und Aufstieg, bis das Haus ein Lichtpunkt ist | **Signatur-Ende aller Pillars** | 1,5–2 s, am Ende 0,5 s halten |
| **M5 Locked-off** | Stativ, nichts bewegt sich außer Licht und Wasser | P2-Varianten, P4 „Lights On“ | Das Ereignis ist das Licht. |

**Verboten:**
- Reißschwenks
- Flug durch Wände (typische Morphing-Quelle, QA-Punkt 11)
- Drohnen-Achterbahn
- Orbits über 30°

**Testvariable:** statisch (M5) vs. Push-in (M1) als eigener Test ab Woche 3 ([15 §4.5](15_kpi_framework.md)).

---

## 9. Geschwindigkeit

Hausregeln `[ESTIMATED]`, abgeleitet aus dem Proxy „langsam > schnell“ (s. o., konfundiert). Sie werden im eigenen Account getestet.

| Element | Regel |
|---|---|
| Kamera | eine Bewegung pro Einstellung, keine Speed-Ramps; Ausnahme ist der Reveal-Moment. |
| Einstellungslänge P1/P4/P6 | ≥ 2,5 s pro Einstellung, höchstens 4 Einstellungen in 12 s |
| P2-Varianten | 2,5–3,5 s pro Variante, harter Schnitt |
| P3-Stufen | 2–3 s pro Stufe, 4 Stufen, danach das Ende |
| Licht-Ereignis | innerhalb der **ersten Sekunde** (Hook), zweites Ereignis in der Mitte |
| Schnitt auf Musik | höchstens jeder zweite Takt; der Schnitt folgt dem Licht, nicht dem Beat |

---

## 10. Musik und Audio

**Datenlage:**
- **Unsere Daten:** `[UNKNOWN]`. Audio ist aus Cover-Frames nicht codierbar. Die 7 NexLev-Reels hatten fünfmal nur Musik, einmal Musik plus Ambient, einmal nur Naturklang. Das ist anekdotisch.
- **Plattform:** Stumme Reels werden herabgestuft, und *"go to the audio page"* ist eine der Reels-Vorhersagen ([q01](quellen/q01_instagram_platform_rules.md), [q09](quellen/q09_reels_format_benchmarks.md) §3.6, `[VERIFIED]`). Trending Audio *"can also impact distribution"* (Meta-FAQ, `[VERIFIED]`). Eine **quantitative Studie zu Trending vs. Original Audio gibt es nicht** ([q09](quellen/q09_reels_format_benchmarks.md) §3.8, `[UNKNOWN]`).

**Lizenzlage ([q07](quellen/q07_legal_ai_risk.md) §2.9, `[VERIFIED]` Wortlaut / `[ESTIMATED]` Anwendung):**
- Die Instagram-Musikbibliothek ist *"intended for personal, non-commercial use"*. *"certain business accounts … do not have access to the library."*
- Die **Meta Sound Collection** umfasst *"over 14,000 songs and sounds which are entirely royalty free"* und darf *"for commercial purposes like ads"* genutzt werden.
- Musik für kommerzielle Zwecke ohne Lizenz ist verboten. Sie kann *"blocked, muted or removed"* werden (Meta Music Guidelines).
- Folge: **Gesponserte oder Affiliate-Reels** mit Chart-Musik aus der Bibliothek kollidieren mit „non-commercial“.
- Lizenzbedingungen von KI-Musiktools sind nicht geprüft `[UNKNOWN]`.

**Audio-Regeln:**
1. **Nie stumm posten.**
2. **Standard für alle Reels:** eigenes Sound-Design plus lizenzierte Musik aus der Sound Collection oder mit dokumentierter kommerzieller Lizenz. Die Lizenz-ID steht in der Sidecar-JSON ([16 §4.5](16_automation_strategy.md)).
3. **Klang-Signatur „Glow Tone“:** ein selbst produzierter, ca. 1 s langer, tiefer warmer Ton im Moment, in dem das Licht angeht bzw. am „Last Light“-Ende. Er ist selbst erstellt, also originell und lizenzfrei. Nach einigen Wochen soll er so wiedererkennbar sein wie das Bild `[ESTIMATED]`.
4. **Raumklang statt Wetter-Loop:** Wind am Fels, Wasser, Schritte der Figur, Lichtschalter-Klick. Kein Regen- oder Kaminloop als Standard (siehe Licht).
5. **Trending Audio** nur als dokumentierter Test auf **nicht kommerziellen** Reels (P1/P4) und nur, wenn der Kontotyp Zugriff hat. Die Wahl zwischen Creator- und Business-Konto ist mit [16](16_automation_strategy.md) und rechtlich abzustimmen.
6. **Testplan Audio** (ab Woche 3, `test_id` z. B. `T04_audio`): A = Sound Collection + Glow Tone · B = reines Sound-Design · C = Trend-Audio (nur nicht kommerziell). Ab ~1.000 Followern bevorzugt als Trial Reels ([q01](quellen/q01_instagram_platform_rules.md), `[ESTIMATED]`).

Beobachtetes Beispiel: @epocraftdiy wirbt in der Caption mit *„No Music. Just Pure Construction.“* (adj 330, Einzelfall). **Prinzip:** Konstruktionsgeräusch kann selbst der Reiz sein. Für P3 als Variante B testen.

---

## 11. Text auf dem Bildschirm

| Befund | Wert | Einordnung |
|---|---|---|
| Cover-Text-Overlay vs. keins (alle) | 0,92× (0,77–1,09), p = 0,39 (n = 986 / 1.392) | nicht signifikant |
| Nur KI: Cover-Text vs. keins | 0,87× (0,66–1,17), p = 0,48 (n = 261 / 425) | nicht signifikant |
| Innerhalb derselben Accounts | Text-Overlay −13 Pp bei den Top-10 % | Richtung |
| Plattform | Herabgestuft werden u. a. *"reels that are majority text"*. Nicht monetarisierbar: *"still or moving images with overlaid text"* | `[VERIFIED]` ([q09](quellen/q09_reels_format_benchmarks.md) §3.6, [q01](quellen/q01_instagram_platform_rules.md) §9) |

**Textregeln:**
1. **Nie mehr als ein Textelement gleichzeitig**, das Serien-Badge ausgenommen.
2. **Hook-Text optional**, höchstens 7 Wörter, auf Englisch, in den ersten 2 s, danach weg (Markencheck 4 in [16](16_automation_strategy.md)). Ob Text hilft, wird getestet: Variante „Badge only“ vs. „Badge + Hook-Zeile“.
3. **Das Cover trägt nur das Badge**, keine Headline. Das Bild ist der Hook.
4. P2-Labels nur als `A`, `B`, `C`, keine Beschreibungen.
5. Keine Absätze, keine Listen, keine Preise auf dem Bild. Ausnahme: reale Produktpreise in `Real Price` (P5) mit Datum in der Caption.
6. Keine Pseudo-Schrift im Bild: Generierter Text auf Büchern oder Schildern ist ein Blocker (QA-Punkt 5).
7. **Caption-Aufbau:**
   - Zeile 1: Serie, Nummer und Titel
   - Zeile 2: ein Satz
   - Zeile 3: Frage oder Wahl
   - Zeile 4: KI-Hinweis
   - höchstens 5 Hashtags (Limit seit 12/2025, [q01](quellen/q01_instagram_platform_rules.md))
   - Richtwert: 51–150 Zeichen vor dem KI-Hinweis. In dieser Längenklasse liegt adj 1,10 (n = 523) gegenüber 0,88 bei 401–1.000 Zeichen (n = 750); nicht getestet.
8. **Keine „Save this!“- oder „Share this!“-Befehle als Standard.** `save_share`-CTA 0,75 (n = 102), CTA insgesamt nicht signifikant (p = 0,62).

---

## 12. Schrift, Größen und Safe Zones (9:16)

**Schriftfamilien** (Vorschlag; alle bei Google Fonts unter SIL Open Font License verfügbar – Lizenz vor Nutzung prüfen `[ESTIMATED]`):

| Rolle | Schrift | Schnitt | Warum |
|---|---|---|---|
| Hook-Zeile, Titel | **Instrument Serif** | Regular / Italic | ruhige Editorial-Serife mit Architektur-Magazin-Anmutung; Ziel ist die Abgrenzung von den verbreiteten Luxus-Serifen der Nische `[ESTIMATED]` |
| Labels, Hinweise | **Inter** | SemiBold, Versalien, Laufweite +6–8 % | hohe Lesbarkeit auf kleinem Display |
| Serien-Badge, Nummern | **IBM Plex Mono** | Medium | technisch, „Plannummer“-Anmutung, tabellarische Ziffern |

**Größen auf der 1080 × 1920-Leinwand** (Hausstandard `[ESTIMATED]`):

| Element | Schrift | Größe | Farbe | Position |
|---|---|---|---|---|
| Serien-Badge `UNBUILT · No. 017 · AI CONCEPT` | Plex Mono Medium | 34 px | Paper `#F2EDE3` 90 %; Nummer in Lamp Glow `#F2B45C` | oben links, Oberkante bei y ≈ 290 px |
| Hook-Zeile (≤ 7 Wörter, max. 2 Zeilen) | Instrument Serif | 72 px (64–84) | Paper | oberes Drittel, y ≈ 360–560 px |
| P2-Label `A` / `B` / `C` | Instrument Serif | 120 px | Paper | links, y ≈ 1.250–1.400 px |
| Hinweis (z. B. *"similar, not exact"*) | Inter SemiBold | 30 px | Paper 80 % | über der unteren Safe Zone |
| Endkarte (0,5 s, optional) | Plex Mono + Instrument Serif | 40 / 64 px | Paper auf Unbuilt Night | Mitte |

**Lesbarkeit:** kein Kasten und keine Balken. Stattdessen ein weicher Schatten (Unbuilt Night, 40 % Deckkraft, 12 px Blur). Text nie auf Lamp-Glow-Flächen setzen.

**Safe Zones** `[ESTIMATED – Praxiswerte; in unseren Quellen gibt es keine offizielle Instagram-Spezifikation; vor dem Launch mit zwei Test-Uploads (Entwurf/privat) prüfen]`:

| Bereich | frei halten | Grund |
|---|---|---|
| oben | 0–250 px | Statusleiste, „Reels“-Kopf |
| unten | 1.500–1.920 px | Caption, Handle, Audio-Zeile |
| rechts | 930–1.080 px | Like-, Kommentar- und Teilen-Buttons |
| links | 0–60 px | Rand |
| **Profil-Raster** | Motiv und Badge in der mittleren 1080 × 1440-Fläche (y ≈ 240–1.680) | Das Raster zeigt Reels hochformatig beschnitten (3:4) – zu verifizieren `[ESTIMATED]` |

---

## 13. Video-Länge

![Länge vs. Performance (YouTube-Proxy)](charts/views_by_length_yt_proxy.png)

| Quelle | Befund | Einordnung |
|---|---|---|
| Unsere Instagram-Daten | Reel-Länge ist nicht messbar | `[UNKNOWN]` |
| YouTube Shorts ([Digest](data/processed/analysis_digest.md)) | ≤ 12 s über dem Kanal-Median (n = 3 / 5 / 11, nur 1–4 Kanäle), 13–20 s 0,22 (n = 58), 30 s+ 1,00 (n = 120) | `[PROXY]`, geringe Konfidenz, konfundiert |
| NexLev, 7 Instagram-Reels | 7–23 s; die beiden KI-Reels je 7 s, eine Szene, statisch | anekdotisch |
| Socialinsider (Marken-Accounts, 6 Mio. Reels, H1 2026) | Median-Views 1–30 s: 4.700; 45–60 s: 10.374 (bester Wert); über 180 s: 4.428 | `[VERIFIED]`, aber nicht nach Content-Typ bereinigt; keine KI-Theme-Pages ([q09](quellen/q09_reels_format_benchmarks.md) §3.4) |
| Meta | Empfehlung an Nicht-Follower nur für Videos ≤ 3 min | `[VERIFIED]` ([q01](quellen/q01_instagram_platform_rules.md) §6) |

**Längenregeln:**

| Phase / Pillar | Länge | Grund |
|---|---|---|
| **Tage 1–14, alle Pillars** | **8–12 s, konstant**; P3 `FROM NOTHING` bei **12 s** | Das faktorielle Startdesign hält die Länge fix ([15 §4.5](15_kpi_framework.md)); Startkorridor laut [16](16_automation_strategy.md). Der Strategy Brief (§6) sieht für „From Nothing“ 12–20 s vor. 12 s ist der gemeinsame Punkt beider Vorgaben. |
| P1 / P4 / P6 ab Tag 15 | 8–12 s Standard | |
| P2 ab Tag 15 | 9–12 s (3 × 3 s + Ende) | |
| P3 ab Tag 15 | 8–12 s Standard; **13–20 s als Längentest** `T03` | Transformationen brauchen eventuell mehr Zeit |
| Längentest Woche 4 | 6–8 s vs. 13–20 s ([15 §4.5](15_kpi_framework.md)) | Die Marken-Benchmarks (45–60 s) werden ab Monat 2 mit einer `house_tour`-Variante geprüft. |

**Abgleich mit dem Launch-Plan:** Für Monat 1 verbindlich sind die Kontroll-Rezepte in [14 §2](14_30_day_launch_plan.md) (P1 10 s, P2 12 s, P3 15 s, P4 10 s) und der Längentest T12 der [Testing-Matrix](13_testing_matrix.csv) (10 s vs. 6 s vs. 20 s, Tag 22 und 27). Die Regeln oben bleiben der Korridor für Monat 2.

**Loop-Hinweis:** Das Ende ist eine eigene Einstellung („Last Light“), kein wiederholtes Segment. *"Content that loops and displays the same segment multiple times"* ist nicht monetarisierbar ([q01](quellen/q01_instagram_platform_rules.md) §9, `[VERIFIED]`).

---

## 14. Hook-Stil

![Caption-Hook vs. Erwartung (alle Reels)](charts/adj_by_caption_hook.png)

| Befund | Wert | n | Einordnung |
|---|---|---|---|
| Caption-Hook (Kruskal, adj) | p = 0,35 | 14 Kategorien | **nicht signifikant** |
| Choice: Kommentare pro View | 5,67× (2,05–14,3), p = 6 × 10⁻⁸ | 39 | **robust** |
| KI: Curiosity vs. übrige Hooks | 1,50 vs. 0,84 → 1,79× (0,81–3,35), p = 0,037 | 67 | post-hoc; das KI schließt 1 ein, also nicht belastbar |
| KI: deskriptiv (der häufigste KI-Hook) | 0,76 | 209 | Beschreibungen sind der Standard und liegen unter 1. |
| Alle: Location-only / Instructional / Contrarian | 0,63 / 0,72 / 0,70 | 161 / 74 / 56 | meiden |
| Alle: Money / Status | 1,19 / 1,37 | 82 / 37 | nicht signifikant |
| YouTube-Titel: Transformation / Curiosity / Cozy-Ambience | 1,15 / 1,15 / 0,49 | 268 / 164 / 61 | `[PROXY]` |

**Hook-Architektur (drei Ebenen, in dieser Reihenfolge):**
1. **Visueller Hook (Pflicht):** Der erste Frame zeigt die unmögliche Geste und die Figur (PV1). In der ersten Sekunde passiert ein Licht- oder Bewegungsereignis. Es gibt keinen schwarzen Vorspann und kein Logo-Intro. Die ersten 3 Sekunden zählen laut Meta-FAQ (`[VERIFIED]`, [q09](quellen/q09_reels_format_benchmarks.md) §3.7). Bei kleinen Accounts (1–5K) überspringen im Schnitt 65,5 % der Zuschauer das Reel in den ersten 3 s (Skip Rate, `[VERIFIED]`, ebd.).
2. **Text-Hook (optional, ≤ 7 Wörter, EN):** eine **Behauptung** über das Unmögliche oder eine **Wahl**. Keine Frage wie „Would you live here?“ (KI-Question 0,89, n = 45), kein POV (KI 0,47, n = 14, geringe Konfidenz).
3. **Caption, erste Zeile:** Serie, Nummer und Titel, danach eine Curiosity-Aussage oder eine Choice-Frage.

**Formeln (eigene, EN):**

| Typ | Formel | Beispiele (original) |
|---|---|---|
| Impossible Fact | *[Haus] + [gebrochene Regel]* | *"This house has no ground floor."* · *"The only way in is through the rock."* |
| Hidden Layer | *[Bekanntes] + [darunter/dahinter]* | *"There's a second house under this lake."* |
| Wait-For | *[Warte-Versprechen auf das Licht]* | *"Wait for the second light."* |
| Choice | *[gleicher Ort] + [drei Varianten] + [du bekommst eine]* | *"Three baths. You only get one."* |
| Send-Trigger | *[Person, der man es schickt]* | *"Send this to the person who keeps saying 'one day'."* |
| Arc | *[Anfang] → [Ende] in einem Satz* | *"A bare ledge. Four steps. One pool."* |

Die beobachteten Vorbilder und die daraus abgeleiteten Prinzipien stehen in [08](08_content_pillars.md) je Pillar. Alle Formulierungen hier sind eigene.

---

## 15. Übergänge

| Code | Übergang | Einsatz | Regel |
|---|---|---|---|
| **T1 Light Cut** | Schnitt genau in dem Frame, in dem ein Licht angeht | P1, P4 | Das Licht ist der Grund für den Schnitt. |
| **T2 Threshold Wipe** | Die Kamera passiert eine dunkle Wand- oder Türkante, dahinter liegt die nächste Einstellung. | außen → innen | nur über echte Architekturkanten |
| **T3 Shape Match** | Form auf Form, z. B. Bogen auf Bogen oder Kreis auf Kreis | P1-Montagen | höchstens einmal pro Reel |
| **T4 Day-to-Night Dissolve** | Überblendung über den Himmel von Tag zu Nacht | nur P3 | endet immer in der Nacht |
| **T5 Hard Cut, same frame** | harter Schnitt bei identischer Kamera | P2-Varianten | Geometrie bleibt pixelgleich, nur Material und Licht wechseln |

**Nie:** Split-Screen (0,53, n = 22), Glitch- oder Whoosh-Effekte, Zoom-Übergänge, Morph zwischen **verschiedenen** Häusern.

---

## 16. Wiedererkennbare Elemente (Signatur-System)

| Element | Spezifikation | Wirkung / Datenanker |
|---|---|---|
| **Serien-Badge und Nummerierung** | `UNBUILT · No. 017 · AI CONCEPT`, bzw. `PICK ONE · No. 009 …`, `FROM NOTHING · No. 004 …`, `AFTER DARK · No. 006 …`, `THE ROOM · No. 002 …`. Immer oben links, Plex Mono, von Frame 0 bis zum Ende. Die Nummern laufen je Serie fortlaufend, eine Nummer wird nie doppelt vergeben. | Sammel- und Serienlogik (Theme-Page vs. AI-Creator 0,68×); erfüllt zugleich die KI-Kennzeichnung bei erster Exposition ([q07](quellen/q07_legal_ai_risk.md) §2.1) |
| **Glow gegen Blau** | Palette Abschnitt 2, Regel 1 | Farbkontrast als Erkennungszeichen im Feed und im Raster |
| **„The Visitor“ (Maßstabsfigur)** | eine Figur, **immer dieselbe Silhouette**: langer anthrazitfarbener Mantel, Rückenansicht oder Profil im Gegenlicht, **nie ein Gesicht**, unter 1/10 der Bildhöhe, steht oder geht, keine Pose | Menschlicher Maßstab (KI mit Personen 1,68×). Keine fotorealistische Person im Vordergrund: Die Recommendation Guidelines zielen auf Accounts, die fotorealistische KI-Personen *"prominently"* zeigen ([q01](quellen/q01_instagram_platform_rules.md) §2). Persönlichkeitsrecht: Personen als *„Beiwerk“* ([q07](quellen/q07_legal_ai_risk.md) §2.5) |
| **„Last Light“-Ende** | Kamerabewegung M4: Das Haus schrumpft zum warmen Punkt in der Nacht, am Ende 0,5 s halten, dazu der Glow Tone | Konstanter Abschluss; eigenes Segment, kein Loop |
| **Glow Tone** | Klang-Signatur (Abschnitt 10) | akustische Wiedererkennung `[ESTIMATED]` |
| **Raster-Rhythmus** | Jedes Cover zeigt Glow gegen Blau und das Badge in der mittleren Rasterfläche. Keine Textcover. | Das Profil wirkt als ein Werk. Das ist wichtig für die Follow-Conversion ([15 §3.5](15_kpi_framework.md)). |
| **Caption-Signatur** | Zeile 1 `UNBUILT No. 017 — The House That Holds a Waterfall`; letzte Zeile *"AI-generated concept – not a real property."* | wiederkehrende Form; der KI-Hinweis ist wörtlich wie in [16 §4.5](16_automation_strategy.md). |

**Kein Logo-Wasserzeichen zum Start** (Markencheck 5 in [16 §4.2](16_automation_strategy.md)). Das Badge ist ein typografisches Serienelement, kein Logo. Fremde Wasserzeichen schaden laut Instagram der Reichweite (*"Ditch the watermark!"*, [q01](quellen/q01_instagram_platform_rules.md), `[VERIFIED]`).

---

## 17. KI-Kennzeichnung im Markenauftritt

**Datenlage:**
- Offengelegte Reels 0,69 vs. 0,98 (alle; n = 237 / 2.141). Der Effekt kommt vor allem daher, dass offengelegte Reels KI-Reels sind.
- **Nur unter KI-Reels:** 0,73 vs. 0,89 → 0,82× (0,58–1,18), p = 0,15, also **nicht signifikant**.
- 215 von 686 KI-Reels (31 %) im Datensatz legen KI offen ([key_contrasts](data/processed/stats/key_contrasts.csv)).
- Ob das Instagram-Label „AI info“ die Reichweite senkt, ist `[UNKNOWN]` ([q01](quellen/q01_instagram_platform_rules.md) §3).

**Pflichtlage** (keine Rechtsberatung):
- **Meta:** Selbstauskunft für *"photorealistic video"*, *"we may apply penalties if they fail to do so"* ([q01](quellen/q01_instagram_platform_rules.md) §3, `[VERIFIED]`).
- **EU AI Act Art. 50 seit 02.08.2026:**
  - Ein Account mit Affiliate- oder Sponsoring-Einnahmen ist „Deployer“.
  - Auch plausible fiktive **Gebäude und Orte** können Deepfakes sein.
  - Das Label muss **bei der ersten Exposition** sichtbar sein. *"Disclosure as part of end credits does not comply"*. Metadaten reichen nicht.
  - Laut FAQ und Draft Guidelines, `[VERIFIED]` Wortlaut / `[ESTIMATED]` Anwendung ([q07](quellen/q07_legal_ai_risk.md) §2.1).
- **Physikalisch unmögliche Szenen** können aus dem Anwendungsbereich fallen. Bei Commerce-Bezug gilt die abgeschwächte Pflicht für „fiktionale“ Werke aber oft nicht (q07 §2.1). **Deshalb wird immer gekennzeichnet.**

**Umsetzung als Markenelement:** Die Pflicht wird Teil der Positionierung. *„Unbuilt“* heißt per Definition: nicht real.

| Ebene | Umsetzung |
|---|---|
| Profil | Bio-Zeile *"AI architecture concepts. None of these homes exist — yet."* Das optionale Profil-Label „AI-generated profile“ ist für Accounts ohne KI-Person **nicht** nötig: *"Creators who simply use AI tools as part of their creative process don't need to add the label."* ([q01](quellen/q01_instagram_platform_rules.md) §3, `[VERIFIED]`) |
| Video | Das Badge trägt `AI CONCEPT` ab Frame 0 bis zum Ende und ist im Bild eingebettet, bleibt also auch beim Teilen oder Herunterladen sichtbar. Das EU-Icon ist optional ([q07](quellen/q07_legal_ai_risk.md) §2.1). |
| Plattform | Instagram-KI-Label bei **jedem** Reel setzen; es ist kein Testfaktor ([15 §3.6](15_kpi_framework.md)). |
| Caption | *"AI-generated concept – not a real property."* ([16 §4.5](16_automation_strategy.md)) |
| Orte | nur *"imagined in the Swiss Alps"* bzw. *"concept inspired by …"*, nie „located in“; keine Hotelnamen |
| Preise | keine für fiktive Häuser; reale Produktpreise mit Datum |
| Werbung | „Werbung“ bzw. „Anzeige“ plus „Paid partnership“ als Doppelkennzeichnung. „#ad“ allein reicht der deutschen Medienaufsicht nicht ([q07](quellen/q07_legal_ai_risk.md) §2.7). Bei werblicher Hauptrolle Dauereinblendung „Werbung“ im Video. |
| Provenienz | C2PA- und IPTC-Metadaten nicht entfernen. Sichtbare Generator-Wasserzeichen **nicht wegretuschieren** (AGB, z. B. Higgsfield, [q07](quellen/q07_legal_ai_risk.md) §2.2), sondern einen Tarif ohne sichtbares Wasserzeichen nutzen. Die Eligibility setzt *"no visible watermarks"* voraus ([q01](quellen/q01_instagram_platform_rules.md) §1). |

---

## 18. Do / Don't

| ✅ Do | Datenanker | ❌ Don't | Datenanker |
|---|---|---|---|
| Eine unmögliche Geste pro Reel, im ersten Frame lesbar | KI fantasy 3,25× vs. dreamy (signifikant) | Weichzeichner, Haze, „dreamy“ Glow | stylized dreamy 0,70 (n = 335) |
| Maßstabsfigur „The Visitor“ | KI mit Personen 1,68× (p = 0,02); Person im Cover 2,05× (post-hoc) | fotorealistische Gesichter oder Personen im Vordergrund | [q01](quellen/q01_instagram_platform_rules.md) Recommendation Guidelines |
| Nachtlicht mit lesbarer Architektur (mittlere Belichtung) | KI Nacht 1,27 (n = 93); KI mittel 0,98 vs. dunkel 0,73 | Kerzen-Düsternis, Kamin als Hauptlicht, Regen-, Schnee- oder Nebel-FX | Kerze 0,55 (n = 20); KI Kamin 0,67, Regen 0,63, Nebel 0,73 |
| Statement-Räume: Treppe, Bad, Garten, Pool-Terrasse | KI 2,07× bzw. 2,39× vs. Schlaf-/Wohnzimmer/Küche (post-hoc) | generisches Wohnzimmer, Küche oder Schlafzimmer als Hauptmotiv | KI 0,69 / 0,67 / 0,77 |
| Berg und Küste als Setting | KI 1,80 (n = 59), post-hoc | Klippen-Villa, Wald, Wüste, Schnee als Default | KI 0,48 / 0,58 / 0,68 / 0,70 |
| Hausstil „Warm Monolith“ (warm luxury / futuristic / tropical) | KI 1,85 / 1,06 / 1,70 | Beige-Minimalismus: modern luxury, organic, skandi, japandi | KI 0,79 / 0,57 / 0,28 / 0,61; 2,47× (post-hoc) |
| Das Haus als Motiv | – | Fensterblick oder View Reveal als Hauptmotiv | 0,70× (nominal signifikant); KI 0,56 (n = 118) |
| Serien-Badge, Nummer, Signatur-Ende | Theme-Page vs. Creator 0,68× (signifikant) | anonyme Bildstrecken ohne Serienlogik | Theme-Page 0,74 (n = 503) |
| Transformationen nacheinander (Tag → Nacht) | YouTube-Transformation 1,15 `[PROXY]` | Split-Screen vorher/nachher | 0,53 (n = 22) |
| Minimaler Text (Badge, optional ≤ 7 Wörter) | Text 0,92× (n.s.); innerhalb Accounts −13 Pp | Textlastige Cover, Absätze im Bild | *"majority text"* herabgestuft ([q09](quellen/q09_reels_format_benchmarks.md)) |
| Choice-Mechanik für Kommentare | 5,7× Kommentare/View (signifikant) | „Save this!“ oder „Share this!“ als Standard-CTA | `save_share` 0,75 (n = 102) |
| Hero-Piece-First mit exaktem Link | Kaufbarkeit ohne Reichweitenverlust (1,01×) | Lookalikes als „exact“ ausgeben, Dupes geschützter Klassiker | [q02](quellen/q02_furniture_affiliate_commerce.md), [q07](quellen/q07_legal_ai_risk.md) §2.4 |
| Eigene Prompt-Vokabeln (Abschnitt 5) | – | Namen von Architekten, Marken oder Hotels im Prompt | [q06](quellen/q06_ai_theme_page_case_studies.md) §2.6, [q07](quellen/q07_legal_ai_risk.md) §2.4 |
| KI-Label ab Frame 0 im Bild | [q07](quellen/q07_legal_ai_risk.md) §2.1 | Label nur im Abspann oder unter „mehr“ | *"end credits does not comply"* |
| Eigener Klang (Glow Tone) plus lizenzierte Musik | [q07](quellen/q07_legal_ai_risk.md) §2.9 | Stumm posten; Chart-Musik in Werbe-Reels | muted wird herabgestuft ([q01](quellen/q01_instagram_platform_rules.md)) |
| Eigenes Ende als Einstellung | – | dasselbe Segment loopen | nicht monetarisierbar ([q01](quellen/q01_instagram_platform_rules.md) §9) |
| Preise nur für reale Produkte, mit Datum | [16 §4.5](16_automation_strategy.md) | „$40M villa in Dubai“ für fiktive Häuser | [q07](quellen/q07_legal_ai_risk.md) §2.6 |
| Tarif ohne sichtbares Generator-Wasserzeichen | *"no visible watermarks"* ([q01](quellen/q01_instagram_platform_rules.md)) | Wasserzeichen oder Metadaten entfernen | AGB und Provenienz ([q07](quellen/q07_legal_ai_risk.md) §2.2) |

---

## 19. Fünf Prompt-Blöcke (Bild und Video, EN)

**Aufbau:** Jeder Block besteht aus Keyframe-Prompt (Bild), Motion-Prompt (Video), Spezifikation und QA. Er nutzt den **House-Style-Block** und den **Negativ-Block** unten.

**Anpassung und Ablage:**
- Die Blöcke sind tool-agnostisch. Parameter und Syntax werden je Generator angepasst.
- Tools ohne Negativ-Prompt bekommen den Negativ-Block als Satz *"Avoid: …"* angehängt ([16 §7](16_automation_strategy.md)).
- `prompt_id`, Seed, Modell und Tarif wandern in die Sidecar-JSON ([15](15_kpi_framework.md), Feld 33).
- Die Prompts sind **Starthypothesen**, keine belegten Gewinner.

### Block 0 – House Style (`STY-unbuilt-core`) und Negativ (`NEG-unbuilt`)

```text
STY-unbuilt-core:
Architectural night photograph, vertical 9:16 frame. Clear deep night-blue sky (#0D1B2A),
no pink or purple tones. The building is the only warm light source: 2700K amber light
(#F2B45C) from windows, recessed light lines and pendant lamps, with realistic falloff and
reflections. Materials limited to honed travertine (#D6C6AA), sandstone (#B89468), dark basalt
(#2B2926), walnut (#5A3D2B) and small brushed-brass details (#B08A4E). Medium exposure:
architecture, edges and textures clearly readable, crisp detail, slight natural patina,
straight verticals, one clear focal point. One small human figure seen from behind for scale,
long charcoal coat, less than one tenth of the frame height, face never visible.
Physically plausible structure with visible supports unless the concept is explicitly
impossible. Real-world furniture proportions. Calm, quiet, editorial.

NEG-unbuilt:
text, letters, numbers, signage, logos, brand names, watermark, pink sky, purple sky,
sunset gradient, haze, bloom, dreamy soft-focus glow, lens flare, candles, fireplace as main
light, fog, rain, snow, view-through-window composition, glass box villa with infinity pool,
beige minimalist living room, duplicated objects, warped or bent lines, floating furniture,
melted textures, extra doors, stairs leading nowhere, visible faces, crowds, famous landmarks,
real hotels, split screen
```

### Block 1 – P1 `UNBUILT` · „The Split Boulder“

```text
KEYFRAME (image):
A single granite boulder the size of a four-storey building rests on a high alpine ridge
above a sea of clouds. One clean vertical cut runs through the boulder; inside the cut,
three floors of a home glow warm amber: a spiral stone stair, a walnut library wall,
one brass pendant. A narrow stone path leads up to the cut; the small figure in the charcoal
coat stands on the path, looking up. Night, first stars. Eye level 1.5 m, 24 mm lens,
boulder in the upper two thirds, figure in the lower third.
+ STY-unbuilt-core   | negative: NEG-unbuilt

MOTION (video, 10 s):
Shot A, 0–8 s: very slow push-in along the path toward the lit cut, camera height constant,
constant speed; the boulder and the interior stay rigid; only faint cloud movement below.
Shot B, 8–10 s (signature "Last Light"): smooth pull-back and rise until the boulder is a
single warm point on the dark ridge; hold the final frame for 0.5 s.
```

**Spezifikation:** 1080 × 1920; Schnitt ohne Übergang A → B, alternativ T1 Light Cut. Badge `UNBUILT · No. ### · AI CONCEPT`, optionaler Hook *"The only way in is through the rock."*

**QA:** Die Geste ist im Frame 1 lesbar. Die Figur ist kleiner als 1/10 der Bildhöhe und ohne Gesicht. Der Schnitt ist die einzige warme Lichtquelle. Keine schwebenden Steine und kein Morphing der Treppe (QA-Punkte 3, 11 und 14 in [16 §4.3](16_automation_strategy.md), mit der Figurenregel aus Abschnitt 20).

### Block 2 – P2 `PICK ONE` · „Three Baths“

```text
KEYFRAME TEMPLATE (image, generate 3 variants with IDENTICAL camera and geometry):
A double-height stone bathroom carved into a hillside at night, one-point perspective from
the doorway at 1.5 m, 28 mm lens. A freestanding bathtub centered under a single pendant lamp,
a tall slot window showing only night sky, a stone bench on the left.
Walls: {MATERIAL}. Tub: {TUB}. Pendant: {LIGHT}. One accent: {ACCENT}.
+ STY-unbuilt-core (figure only in variant A: standing in the doorway at the left frame edge,
back view)   | negative: NEG-unbuilt

VARIANTS:
A "Travertine & Brass":  MATERIAL honed travertine | TUB white stone | LIGHT brushed brass dome |
                         ACCENT olive tree in a stone pot
B "Basalt & Walnut":     MATERIAL dark basalt | TUB walnut-clad | LIGHT blackened bronze cylinder |
                         ACCENT linen towel on a walnut stool
C "Sandstone & Oxide":   MATERIAL sandstone | TUB oxide-red marble | LIGHT amber glass globe |
                         ACCENT hand-thrown ceramic vessel

MOTION (video, 3 s per variant, total 9–10 s):
Locked-off camera. In each variant the pendant switches on within the first 0.3 s, the water
surface moves slightly, nothing else changes. Hard cut between variants on the same frame.
Final 1 s: variant B pulls back through the doorway into the dark corridor ("Last Light").
```

**Spezifikation:**
- Labels `A` / `B` / `C` in Instrument Serif, 120 px, links oberhalb der unteren Safe Zone.
- Hook optional: *"Three baths. You only get one."*
- Caption-Frage: *"A, B or C?"*
- Eine Variante nutzt ein **reales Hero-Stück** (Wanne oder Leuchte) nach dem Workflow in Block 5.

**QA:** Kanten und Geometrie sind in A, B und C deckungsgleich (Differenzbild). Spiegelungen stimmen (QA-Punkt 6). Kein Pseudo-Text. Split-Screen ist verboten.

### Block 3 – P3 `FROM NOTHING` · „Bare Ledge“

```text
KEYFRAMES (image, same camera for all four: aerial 30° down, 35 mm, ledge in the middle third):
K1 (day, raw):   A bare granite ledge on a steep mountainside above a dark lake, loose rubble,
                 one wooden survey stake; the small figure in the charcoal coat stands at the
                 edge. Soft overcast daylight.
K2 (afternoon):  Same camera. Sandstone terraces cut into the ledge, the outline of a long
                 pool, stone steps, no planting yet.
K3 (blue hour):  Same camera. Pool filled with dark still water, olive trees and grasses
                 planted, a walnut daybed and a brass floor lamp on the upper terrace.
K4 (night):      Same camera. Night, clear deep-blue sky; pool lit warm amber from below,
                 terrace lamps on; the figure sits at the pool edge.
K4 + STY-unbuilt-core; K1–K3 use STY-unbuilt-core with daylight exception | negative: NEG-unbuilt

MOTION (video, 12 s, start/end-frame pairs):
K1→K2, K2→K3, K3→K4, about 3 s each; the camera stays fixed except one continuous slow
5 % push-in over the whole sequence. Elements appear in building order: stone, then water,
then plants, then light; no object flickers in and out. Last 1.5 s: slow rise and pull-back
("Last Light").
```

**Spezifikation:** T4 Day-to-Night nur über den Himmel. Hero-Stücke (Daybed, Leuchte) sind von K3 bis K4 identisch. Hook optional: *"A bare ledge. Four steps. One pool."*

**QA:** gleiche Kamera in allen Keyframes, plausible Terrassen und Stützmauern, kein Morphing der Möbel. Rohzustand als erster Frame **mit** Figur, kein leerer Raum ohne Spannung (Cover „empty room“ 0,76).

### Block 4 – P4 `AFTER DARK` · „Lights On“

```text
KEYFRAME (image):
A long, low house of dark basalt and travertine built into a rocky coastline just above the
waterline (not on a cliff top), one wing cantilevered over black, calm water. Night, clear
deep-blue sky. All windows dark except one warm entrance light; the small figure walks on the
stone path toward the entrance. Eye level 1.4 m, 28 mm, house across the middle third,
horizon in the upper third.
+ STY-unbuilt-core   | negative: NEG-unbuilt

MOTION (video, 10 s):
Locked-off camera. At 0.5 s the first room lights up warm amber; then room by room from left
to right about every second, each with a matching reflection appearing on the water. The figure
reaches the door at 7 s. Final 2 s ("Last Light"): slow pull-back until the house is a thin
line of warm light between dark sea and dark sky; hold 0.5 s.
```

**Spezifikation:** T1 Light Cut entfällt, eine Einstellung. Der Glow Tone liegt beim ersten Licht und am Ende. Hook optional: *"Wait for the second light."*

**QA:** Jede Spiegelung gehört zu einem erleuchteten Fenster (QA-Punkt 6). Die Geometrie ändert sich beim Einschalten nicht. Kein rosa Himmel. Die Figur bleibt klein.

### Block 5 – P3-Pilot / P6 `THE ROOM` · Hero-Piece-First

```text
INPUTS:
{HERO_REF} = product image of a real, purchasable lounge chair (or floor lamp / bathtub);
product URL and affiliate link documented; reference-image rights checked.

KEYFRAME (image-to-image with {HERO_REF} as reference):
A top-lit stair hall carved into pale travertine: a spiral stair of solid stone descends
around a circular void. On the bottom landing stands ONE lounge chair that matches the
reference image exactly in shape, proportions, material and color, placed in the warm pool
of light from a hidden cove, a brass floor lamp beside it. A round skylight shows the night
sky. The chair is fully visible in the lower-middle third, not cropped, contact shadows
correct. Optional: the small figure at the top of the stair, back view.
+ STY-unbuilt-core   | negative: NEG-unbuilt + "no chair variations, no second chair"

MOTION (video, 10 s):
Slow descending camera along the curve of the stair over 8 s, ending face-on to the chair;
the chair stays rigid and unchanged in every frame. Final 2 s ("Last Light"): pull-back
upward through the skylight into the night.
```

**Spezifikation:** Hinweis *"similar, not exact"* nur, wenn der Abgleich scheitert. Caption mit Affiliate-Kennzeichnung („Werbung“ bzw. „Anzeige“ plus Amazon-Pflichtsatz, falls Amazon).

**QA:**
- Silhouette, Material und Farbe entsprechen der Referenz (Seite-an-Seite-Vergleich); sonst neu generieren.
- Keine Logos, keine Nachbildung eines geschützten Klassikers.
- Hero-Stück ≥ 2 s sichtbar und nicht in der UI-Safe-Zone.

---

## 20. Abgleich mit [16_automation_strategy.md](16_automation_strategy.md) (zur Abstimmung)

| Punkt in 16 | Stand in 16 | Dieser Style Guide | Vorschlag |
|---|---|---|---|
| Markencheck 6 und QA-Punkt 14: „Keine fotorealistischen Menschen“, Standard „keine Menschen“ | Blocker | **„The Visitor“** als einzige zulässige Figur (klein, Rückenansicht, kein Gesicht). Datenbeleg: KI mit Personen 1,68× (p = 0,02); der Strategy Brief sieht die Figur ausdrücklich vor (§2.3, §5). | QA-Punkt 14 ergänzen um „Blocker, außer Scale Figure nach 11 §16“ |
| Templates T01–T03 (Wohnzimmer Blue Hour, Klippe Golden Hour, Cozy-Schlafzimmer) | aus einem **früheren Teil-Sample** abgeleitet | Aktuelle KI-Daten: Wohnzimmer 0,69 (n = 123), Blue Hour 0,89 (n = 101), Klippe 0,48 (n = 35), Golden Hour 0,82 (n = 84), rustic cozy 0,78 (n = 107), Kamin-FX 0,67 (n = 70) | T01–T03 durch die Blöcke 1–5 ersetzen und als `@2.0.0` versionieren |
| Markencheck 4: Text ≤ 7 Wörter, Hausschrift, Safe Zone | ✓ | Schrift und Safe Zones in Abschnitt 12 definiert | übernehmen |
| Markencheck 5: kein Logo-Wasserzeichen | ✓ | Badge ist Typografie, kein Logo | übernehmen |
| KI-Caption-Zeile, Preis- und Ortsregeln (§4.5) | ✓ | wörtlich übernommen | – |
| Hinweis „q07 lag nicht vor“ (§4.5) | offen | q07 liegt vor: Label bei erster Exposition, Musiklizenz, Werbekennzeichnung (Abschnitte 10, 17) | Tabelle in 16 §4.5 mit q07 abgleichen |

---

## 21. Validierung: Wie wir prüfen, ob der Stil wirkt und erkannt wird

**1. Stil als Testfaktor.** Vorschlag für die 3 Stil-Stufen im faktoriellen Startdesign ([15 §4.5](15_kpi_framework.md)); die finale Auswahl trifft der Content-Plan. Alle drei bleiben innerhalb der Marke: gleiche Nacht, gleiche Palette, gleiche Figur. Variiert werden nur Materialwelt und Vegetation.
   - S1 `warm_luxury` („Warm Monolith“: Travertin, Messing)
   - S2 `futuristic` („Night Machine“: Basalt, lineares Licht, präzise Kanten)
   - S3 `tropical` („Night Garden“: Sandstein, Pflanzen, Wasser)
   - KI-Werte: 1,85 (n = 15) / 1,06 (n = 58) / 1,70 (n = 20); Stil insgesamt nicht signifikant.

**2. Signatur-Elemente einzeln testen**, jeweils mit genau einem Faktor ([15 §4.5](15_kpi_framework.md)), ab Woche 3:
   - Figur ja/nein
   - Hook-Text ja/nein
   - M5 statisch vs. M1 Push-in
   - Audio A/B/C

**3. Wiedererkennungs-Check** ab Woche 4, monatlich `[ESTIMATED – Hausmethode]`:
   - 10 Personen aus der Zielgruppe sehen ein 3 × 3-Raster aus 3 eigenen Covern ohne Badge und 6 Wettbewerber-Covern.
   - **Ziel: ≥ 7 von 10** erkennen alle 3 eigenen.
   - Zusätzlich qualitativ: Kommentare, die Serie oder Nummer nennen („Unbuilt“, „No. 12“), werden in der Winner-DB als `notes` gezählt.

**4. Markenkonsistenz im Prozess:**
   - Farbhistogramm-Check gegen das Brand-Board.
   - Qualitäts-Rubrik aus [16 §4.2](16_automation_strategy.md): alle Kriterien ≥ 3, Schnitt ≥ 4.
   - QA-Checkliste aus [16 §4.3](16_automation_strategy.md).
   - Nur visuelle Qualität „high“ posten. Die visuelle Qualität ist im Research nur beim topic_index robust signifikant (p = 3 × 10⁻⁷); größenbereinigt nur nominal (p = 0,013).

**5. Stil-Revision:** Belegt die Winner-DB nach 30 Tagen einen Nachteil des Nachtlooks (Regel „belegt“ in [15 §4.3](15_kpi_framework.md)), wird zuerst die **Lichtregel** geändert, nicht die Signatur-Formel insgesamt. Figur, Badge und Ende bleiben stabil, damit die Wiedererkennung nicht verloren geht.

---

## Quellen

- [data/processed/analysis_digest.md](data/processed/analysis_digest.md): Segmente Licht, Farbe, Material, Cover-Elemente, Hooks, CTA, Caption-Länge, KI-Offenlegung, Within-Account, YouTube-Proxy, NexLev-Stichprobe
- [data/processed/strategy_brief.md](data/processed/strategy_brief.md): Positionierung, Style-Leitlinien (§5)
- [key_contrasts.csv](data/processed/stats/key_contrasts.csv) · [ai_segments.csv](data/processed/stats/ai_segments.csv) · [ai_style_contrasts.csv](data/processed/stats/ai_style_contrasts.csv), erzeugt mit [scripts/pillar_style_stats.py](scripts/pillar_style_stats.py)
- [q01](quellen/q01_instagram_platform_rules.md) Plattformregeln, Originalität, KI-Labels, Monetarisierung · [q02](quellen/q02_furniture_affiliate_commerce.md) Affiliate und „similar vs. exact“ · [q04](quellen/q04_interior_trends_demand.md) Trends · [q06](quellen/q06_ai_theme_page_case_studies.md) Fallstudien · [q07](quellen/q07_legal_ai_risk.md) AI Act, Marken, Musik, Werbekennzeichnung · [q09](quellen/q09_reels_format_benchmarks.md) Länge, Hook, Audio
- Charts: [adj_by_palette](charts/adj_by_palette.png), [adj_by_lighting](charts/adj_by_lighting.png), [adj_by_material](charts/adj_by_material.png), [adj_by_style](charts/adj_by_style.png), [adj_by_visual_hook](charts/adj_by_visual_hook.png), [adj_by_caption_hook](charts/adj_by_caption_hook.png), [views_by_camera_yt_proxy](charts/views_by_camera_yt_proxy.png), [views_by_length_yt_proxy](charts/views_by_length_yt_proxy.png)
