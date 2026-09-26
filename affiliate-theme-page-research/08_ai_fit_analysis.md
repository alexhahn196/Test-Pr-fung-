# 08 – KI-Eignung und KI-Vorteil (Teil 3 „AI-Eignung“, Teil 20)

**Stand:** 26.09.2026 · Detailquelle: [`quellen/H_ai_tools_kosten_automation.md`](quellen/H_ai_tools_kosten_automation.md)

## 1. Stand der Werkzeuge (September 2026)

| Aufgabe | Beste Option laut Recherche | Preis | Qualität |
|---|---|---|---|
| Video (günstig) | Veo 3.1 Lite 720p · Wan 2.5 (fal) | $0,05 pro Sekunde | VERIFIED |
| Video (mittel) | Veo 3.1 Fast 1080p (inkl. Audio) · Kling 3.0 Std (fal) | $0,12 · $0,084 pro Sekunde | VERIFIED |
| Video (premium) | Veo 3.1 Standard · Kling 3.0 Pro mit Audio | $0,40 · $0,112–0,168 pro Sekunde | VERIFIED |
| Sora 2 | **eingestellt:** App 26.04.2026, API 24.09.2026 | – | VERIFIED (OpenAI Help Center) |
| Bild / Reference-Editing | Nano Banana Pro ($0,134), Nano Banana 2 ($0,067), FLUX Kontext ($0,04), Seedream | pro Bild | VERIFIED |
| Aggregator | Higgsfield Ultra 129 € / 3.000 Credits (Kling, Seedance, Marketing Studio) | – | VERIFIED (MCP-Preiskonfiguration) |
| Voice | ElevenLabs Creator $22/Monat | – | VERIFIED |
| Render | Remotion (kostenlos bis 3 Personen) + FFmpeg | $0 | VERIFIED |
| **Kosten pro Reel** (4 Clips × 6 s × 2,5 Versuche + 12 Bilder) | günstig $3,5–5,6 · mittel $8 · premium $12–26 | | MODEL ASSUMPTION (H 9.2) |

## 2. Die entscheidende Frage: Kann man ein **echtes** Produkt zeigen, ohne zu täuschen?

| Ansatz | Form/Farbe | Logo/Schrift | Bewertung |
|---|---|---|---|
| **A) Echtes Produktfoto freistellen + Szene generieren** (Outpaint/Relight) | sehr hoch | sehr hoch (Originalpixel) | **Standard für die Empfehlung** |
| B) Bild-Reference-Editing (Nano Banana Pro ≤ 6 Objekt-Refs, FLUX Kontext) | hoch bei starren Produkten | mittel (kleine Schrift driftet) | für Nebenobjekte |
| C) Image-to-Video aus A/B-Startframe, wenig Bewegung | mittel–hoch in ruhigen Shots | mittel–niedrig bei Rotation/Nahaufnahme | für Atmosphäre |
| D) Reference-to-Video (Veo „Ingredients“, Kling Elements, Seedance Multi-SKU) | mittel | Herstellerangabe „precise lettering“, **kein unabhängiger Test** | CLAIMED |
| E) Objekt-Ersetzung in bestehendem Video | unbelegt | unbelegt | CLAIMED |

**Befund (H 10.2):** Auf Bildebene ist echte Produkttreue 2026 zuverlässig machbar. Im Video driften Logos, Etikettentexte und feine Details häufig. Die Arbeitshypothese lautet, dass 30–60 % der Produktclips Abweichungen zeigen (MODEL ASSUMPTION). **Regel:** KI für Raum, Licht und Bewegung. Das Produkt in Nahaufnahme und auf der End-Card ist immer ein echtes Foto. Keine KI-gerenderten Produkttexte. Produktaussagen nur aus dem Datenfeed.

**Bildrechte:** Amazon-Produktbilder dürfen nicht verändert und nicht gespeichert werden (VERIFIED, A). Für Freisteller sind deshalb **Hersteller-Pressebilder mit Nutzungsrecht** oder **eigene Fotos** nötig. Das ist ein manueller Klärungsschritt pro Marke.

## 3. KI-Fit je Nische (Rubrik 1–5, wie in der Scorecard)

| KI-Fit | Nischen | Warum |
|---|---|---|
| **5** | Backyard Wellness (Fass-Sauna, Plunge), AI-Interiors/-Architektur, Gaming-Setups | Szene ist der Star; Produkte geometrisch einfach bzw. keine Produkte |
| **4** | Kitchen & Coffee Setups (Geräte), Küchengeräte/Kochgeschirr, Desk Setups, Travel Gear (Flat-Lays), Camping, Garten-Design, Outdoor Living, Pools, Power Stations, Balkon, EDC, Luxury Homes, Home Bar | **statische Produkte** in inszenierten Räumen; Freisteller-Compositing zuverlässig |
| **3** | Home Decor Finds (viele kleine Objekte), Espresso-Setups allein (Community kritisch ggü. KI), Küchengadgets, BBQ (Food/Feuer wirkt künstlich), Smart Home, Möbel, Schlaf, Travel Destinations, Home Gym, Golf, Cycling, Home Organization, Aquaristik, Hiking, PC-/Smartphone-Zubehör | gemischt: Teile per KI, Funktion oder Detail heikel |
| **2** | Tech Gadgets (Funktionsdemos), Cleaning, Hunde/Katzen (Tiere „nutzen“ Produkte), Beauty/Haircare (Ergebnisse), Fashion/Sneakers (Passform), Schmuck/Uhren/Taschen (Details, Marken), Autozubehör, 3D-Druck, Tools/DIY, Audio/Music (Klang), Consumer Electronics, LEGO, Baby, Running | **der Nutzen muss echt gezeigt werden**; KI-Demo wäre Täuschung |
| **1** | Car Detailing (Vorher/Nachher), Fotografie (Bildqualität) | nur echte Aufnahmen sinnvoll |

Vollständige Werte je Nische: [`01_longlist_niches.csv`](01_longlist_niches.csv), Spalte `ai_fit_1_5`.

**Die Kernspannung:** Die Nischen mit dem höchsten KI-Fit (AI-Interiors, Gaming) haben die schwächste Economics. Die Nischen mit der höchsten Kaufintention (Gadgets, Beauty) haben den niedrigsten KI-Fit, weil dort Funktion oder Ergebnis gezeigt werden muss. **Der Schnittpunkt sind statische, hochpreisige Produkte in inszenierten Räumen:** Kitchen & Coffee, Desk, BBQ, Travel Gear, Backyard Wellness.

## 4. Wo KI einen **strukturellen** Vorteil bringt (Teil 20)

| Vorteil | Stärke | Beleg / Begründung |
|---|---|---|
| **Stil- und Preisstufen-Varianten** (derselbe Setup in Japandi/Landhaus/Industrial; $500/$1.500/$3.000) | **hoch** | Echte Produktionen bräuchten mehrere Räume und Geräte. KI braucht nur Freisteller + Szene. Nirgends so wirksam wie bei Setups |
| **Schnelle Creative-Tests** (Hooks, erste 3 s, Trial Reels) | **hoch** | Instagram Trial Reels per API (H). Varianten kosten $1–4 statt einen Drehtag |
| **Mehrere Zielmärkte** (EN + DE aus denselben Visuals) | **hoch** | Zweite Sprache ≈ Grenzkosten null: TTS, Captions, Links (F 9) |
| **Keine Repost-/Urheberrechtsabhängigkeit** | **hoch** | Viele große Theme-Pages nutzen fremden Content („DM for removal“ – I); die Originalitätsregel straft das ab |
| **Niedrige Produktionskosten** | mittel | $3,5–8 pro Reel (H), aber die QA-Zeit bleibt |
| **Ungewöhnliche Settings** (Traumküchen, Backyard-Spas) | mittel | Reichweite belegt (Dreamy Interior 315k, Bau Rausch 620k), **Kaufabsicht aber nicht** |
| **Automatische Analyse / Winner Detection** | mittel | IG/YT/Awin/Impact-APIs vorhanden; **Amazon ohne Reporting-API** |
| **Content-Volumen** | niedrig | Offshore-„Finds“-Fabriken posten schon ~15 Shorts/Woche (J). Volumen allein skaliert nicht (cool_amazon_homefinds: 2.555 Posts, 89k Follower – I) |

## 5. Wo KI kaum hilft oder schadet

- **Produktfunktion, Ergebnis und Erfahrung** (Gadgets, Beauty, Pflege, Tiere): Eine KI-Darstellung wäre irreführend, siehe [17](17_compliance.md).
- **Vertrauen:** Personen-Creator mit Gesicht verkaufen besser, das zeigen die LTK-/Storefront-Erfolge (I). Ein KI-Avatar mit Erfahrungsbericht ist ausgeschlossen (FTC 465, UWG Anh. 23c).
- **Plattform-Gegenwind gegen „AI slop“:**
  - YouTube „inauthentic content“ (Monetarisierung)
  - TikTok-Nutzerregler für weniger KI (UNKNOWN\*)
  - Pinterest Gen-AI-Labels und „weniger KI“ in Home Decor (UNKNOWN\*)
  - Instagram-KI-Labels
  - Ob Labels die Reichweite auf Instagram senken, ist **nicht belegt** (UNKNOWN).
- **Kaufentscheidungen mit Recherchephase** (Espresso, Sauna): KI erzeugt Aufmerksamkeit, die Entscheidung fällt auf YouTube-Reviews oder Vergleichsseiten, oft außerhalb des Cookie-Fensters.
