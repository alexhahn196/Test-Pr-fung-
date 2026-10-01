# Finalisten – Detailanalyse

Recherchedatum 01.10.2026. Kennzeichnung: **BELEGT** (Primärquelle direkt geprüft), **ANBIETERANGABE** (Selbstauskunft), **SCHÄTZUNG** (Drittanbieter-Benchmark oder abgeleitete Zählung), **ANNAHME** (eigene Setzung). Bewertungen sind keine Bestellungen, Follower sind keine Käufer, Finanzierung ist kein Umsatz. Alle Rechenwerte stammen aus `finanzmodell/` (Aufruf `python3 berechnen.py`); die Eingaben dort sind die korrigierten Werte der Ökonomie-Prüfer aus dem Neuzuschnitt (`rohdaten/neuzuschnitt.json`).

## Ergebnis vorab

Von 50 Longlist-Kategorien kamen 10 auf die Shortlist. **Keiner der 10 Kandidaten hat die Vertiefung als „wirtschaftlich überzeugend“ bestanden**: Überall lag der Deckungsbeitrag vor Werbung (DB I) unter dem realistischen Preis für einen Neukunden. Die vier stärksten wurden deshalb neu zugeschnitten und doppelt gegengeprüft. Danach gilt:

| Status | Kandidat | Kurzbegründung |
|---|---|---|
| **Finalist 1 (bedingt)** | **KI-Designwelt Hochzeit** | Höchster DB I (≈ 185 €, 53 %) und höchster tragbarer CAC aller Kandidaten; als einziger Kandidat liegt der Break-even-CAC bei 1 Mio. € in allen Prüfrechnungen über dem realistischen CAC – aber nur knapp. |
| **Reserve (Platz 2)** | **Kinderzimmer-Stilwelt** | Höchster Warenkorb, starke Vorher/Nachher-Werbung, echter KI-Mehrwert; der Break-even-CAC (≈ 118 €) liegt aber unter dem realistischen CAC (≈ 135–155 €). |
| Modul von Finalist 1 | Lebensweg-Festpaket (Fest-/Hochzeitszeitung) | Trägt eigenständig nicht; als Trauzeugen-Produkt in der Hochzeits-Engine sinnvoll. |
| Modul | Mehrfoto-Familienbild | Preisanker durch Handarbeit widerlegt (Sketchus 239,99 € „ohne KI“, MyPortrait 109,95 €); die Komposition aus getrennten Fotos bleibt als Funktion (z. B. Wandbild nach der Hochzeit). |

Die Vorgabe „nicht künstlich auf fünf auffüllen“ ist damit umgesetzt: ein bedingter Finalist, eine Reserve mit vollständiger Rechnung.

---

## Finalist 1 (bedingt): KI-Designwelt Hochzeit – „Eure Location. Euer Stil.“

### Auf einen Blick

| Merkmal | Wert |
|---|---|
| Zielgruppe | Verlobte Paare (30–38) mit besonderer oder freier Location (Gutshof, Scheune, Schloss, Weingut, Destination), 80–120 Gäste, Papeterie-Budget über dem Durchschnitt; dazu Trauzeugen (Hochzeitszeitung) und Eltern (Wandbild) |
| Ø-Warenkorb Erstbestellung (brutto) | **417 €** Basis (396 € konservativ, 438 € optimistisch); je Paar inkl. Folgephasen ≈ 510 € brutto (Basis, Rechnung aus Modell) |
| DB I vor CAC | **185 €** je Erstbestellung (52,7 % vom Netto), konservativ 161 €, optimistisch 199 € |
| Max. tragbarer CAC | **185 €** Erstkauf; **227 €** inkl. Folgephasen in 12 Monaten; Break-even-CAC bei 1 Mio. € inkl. Fixkosten ≈ **153 €** |
| Realistischer CAC (blended) | 150 € Basis (215 € konservativ, 85 € optimistisch) – ANNAHME auf SCHÄTZUNG-Benchmarks |
| Bestellungen für 1 Mio. € netto | **3.376 pro Jahr** = 281 pro Monat = 9,2 pro Tag (13,9 im Spitzenmonat), aus ≈ 2.330 Neukunden-Paaren |
| Stärkster Wettbewerber | die kartenmacherei (Vorlagen-Marktführer, 36.172 Trustpilot-Bewertungen, davon 17.474 in 12 Monaten, BELEGT 01.10.2026); im Premiumsegment Ateliers wie Tatengold |
| EU-Produktionspartner | WIRmachenDRUCK (DE, Hauptpartner, Preise BELEGT), Onlineprinters (DE, Ausweichpartner mit belegtem Neutralversand), Print API (NL, REST-API) |
| KI-Mehrwert | Mehrere Fotos (Paar, Hund, Location) → eine Illustration im gewählten Stil → automatisch übertragen auf 10–15 Formate (Designsystem); Sofortvorschau der ganzen Suite statt Proof-Schleifen über Wochen |
| Bewertung (100 Punkte) | **60–61** (Ökonomie-Prüfer 61: W 18 / M 12 / K 10 / Wb 7 / P 7 / S 7; Markt-Prüfer 60: 19 / 11 / 9 / 7 / 7 / 7) |
| Ampel Wettbewerb | **GELB** (starker Marktführer, Einstieg über Unterkategorie „illustrierte Location-Suite“ plausibel) |
| Datensicherheit | **NIEDRIG bis MITTEL**: Markt, Preise der Partner und Wettbewerber MITTEL bis HOCH; Zahlungsbereitschaft für eine KI-Designgebühr, Conversion und CAC NIEDRIG (nicht gemessen) |

### 1. Produktidee

Das Paar lädt 3–10 Fotos hoch (Paar, optional Hund, 1–3 Fotos der Location) und gibt Namen, Datum, Orte und Stilwunsch ein. Eine KI erstellt daraus eine Illustration von Paar und Location (Aquarell, Fineline, Gouache). Ein Mensch prüft Gesichter und Architektur. Aus der Illustration entsteht ein **Designsystem**: Farbpalette, Monogramm, Ornamente. Alle Texte setzt eine deterministische Layout-Engine, nie das Bildmodell. Verkauft wird **in Phasen**, jeweils mit demselben Design:

1. **Start:** Designsystem + 75 Save-the-Dates mit Goldfolie (299 €)
2. **Einladung:** 75 Klappkarten DIN lang mit Goldfolie + Kuverts (249 € als Folgephase; als Einstieg „Designsystem + Einladung“ 419 €)
3. **Day-of:** Willkommensschild 50×70 und Sitzplan A1 aus Hartschaum, 10 Tischnummern, 100 Menükarten mit Gold (379 € als Folgephase; als Einstieg 529 €)
4. **Danke:** 75 Dankeskarten mit Gold (159 €)
5. **Dritte Käufer:** Hochzeitszeitung für die Trauzeugen (349 €, 60 Exemplare A4/20 Seiten), Wandbild nach der Hochzeit (129 €)

Die Marge kommt aus der **Designleistung** (implizit ≈ 179 € brutto im Einstiegspreis), nicht aus dem Druck. Die Druckphasen kosten auf Marktführer-Niveau (Einladung ≈ 3,32 €/Karte inkl. Folie gegenüber kartenmacherei 3,30–3,62 €; Rechnung aus BELEGT-Stückpreisen). Gestrichen wurden margenschwache Teile der ersten Fassung: Acryl-Day-of (23 % Rohertrag), Acryl-Platzkarten, Antwortkarte (ersetzt durch RSVP-QR), Sticker.

### 2. Kaufanlass

Die Hochzeit setzt feste Fristen, die zum Kauf zwingen (Bridebook, ANBIETERANGABE, Stand 15.07.2026): Save-the-Date 8–12 Monate vorher, Einladung 4–6 Monate, Menü- und Tischkarten 1–2 Monate, Danksagung 2–4 Wochen danach. Day-of-Schilder 4–8 Wochen vorher (ANNAHME). Pro Paar entstehen so 3–5 Kaufpunkte in etwa 12 Monaten.

Saisonalität (Google Trends DE, relativer Index, SCHÄTZUNG, eigener Abruf 01.10.2026): „Hochzeitseinladung“ Spitze im Januar, Tief im Juli; „Save the Date Karten“ Juli–Oktober; Willkommensschild und Sitzplan Mai–Juli; Hochzeitszeitung April–Juli. Im Modell Spitzenmonat = 1,5 × Durchschnitt (ANNAHME).

### 3. Zielgruppe und Größe

- **348.813 Eheschließungen 2025** (BELEGT, Destatis, Themenseite Eheschließungen, abgerufen 01.10.2026), Tiefstand außer 2021; 2024: 349.216.
- Ø-Ausgabe für Papeterie **338 €** (2025), Spannen Basic 100–200 €, Mittelklasse 250–500 €, Luxus ab 500 €, 22 % papierlos (ANBIETERANGABE, Bridebook, Stand 15.07.2026; Stichprobe nicht genannt). Zweite Quelle: Ø 303 €, 60 % der Paare unter 250 € (ANBIETERANGABE, Sekundärzitat „Bridal Times“, Primärstudie nicht gefunden).
- Abgeleitetes Segment mit ≥ 250 € Papeterie-Budget: ≈ 40 % ≈ 140.000 Paare pro Jahr (SCHÄTZUNG). Für 1 Mio. € netto braucht es ≈ 2.330 Paare = ≈ 1,7 % dieses Segments (Rechnung aus Modell).
- AT/CH: kartenmacherei betreibt .at und .ch (BELEGT); Eheschließungszahlen AT/CH nicht abgerufen.

### 4. Bestehender Markt

- Theoretisches Papeterie-Volumen DE ≈ 348.813 × 338 € ≈ 118 Mio. € (SCHÄTZUNG, Obergrenze).
- Komplette 80-Gäste-Suite beim Marktführer ≈ 464 € ohne bzw. ≈ 563 € mit Veredelung (SCHÄTZUNG aus BELEGT-Staffelpreisen).
- **Zahlungsbereitschaft für individuelle Gestaltung ist belegt – aber nur für Handarbeit:** Tatengold Design-Sets 690 / 1.390 / 2.590 € ohne Druck, Location-Strichzeichnung ab 249 €, Kapazität „bis zu vier Paare pro Monat“ (BELEGT, tatengold.de, 01.10.2026). Cartalia Location-Zeichnung +185 € (Skizze) bzw. +355 € (Aquarell) (BELEGT, Vorarbeit 30.09.2026).
- Wie viele Paare ihre ganze Suite bei einem Anbieter kaufen, ist **weder für DE noch für die USA belegt**. Indiz dagegen: Der Ø-Betrag (303–338 €) liegt unter einer kompletten Marktführer-Suite.
- Gegenbewegung: „Hochzeitseinladung“ im Trends-Index −16 % zum Vorjahr; Markensuche „kartenmacherei“ seit 2021 mehr als halbiert (SCHÄTZUNG, Index); myprintcard (Augsburg) seit 01.07.2026 im Insolvenzverfahren (Registerbekanntmachung über Northdata; Bekanntmachungsportal nicht direkt geprüft).

### 5. US- und internationale Vorbilder

| Vorbild | Was | Größenbeleg | KI |
|---|---|---|---|
| **Minted** (US) | Künstler-Papeterie für die ganze Hochzeit, Day-of, Wanddeko | erwartet > 300 Mio. USD Umsatz 2026, Gesamtunternehmen (ANBIETERANGABE, Business Wire 28.04.2026); Trustpilot 2.332 Bewertungen, 2,6 (BELEGT) | KI-Anpassung (eigene Location/Hund im Künstlerstil) am 30.04.2026 angekündigt; laut Fast Company (29.05.2026) nicht live; bis 01.10.2026 keine Startmeldung gefunden (Negativbefund) |
| **Papier** (UK) | Premium-Papeterie, Hochzeit eine Kategorie | 31,9 Mio. GBP Umsatz (+18 %), Rohertragsmarge 56 %, **operativer Verlust 3,8 Mio. GBP** im Geschäftsjahr bis 03.05.2025 (BELEGT, Companies House) | keine bekannt |
| **Joy / Paperlust** (US/AU) | Hochzeitswebsite als Zubringer für Papeterie; Individualillustration ab 100 AUD | US-Paare: Suite 518 USD, davon Day-of 140 USD (ANBIETERANGABE, Joy-Blog, aktualisiert 22.06.2026) | KI nur für Moodboards |
| **Lily & Roe Co.** (US) | Day-of-Beschilderung als Set | Sets 375–1.290 USD; Produktanlagen 2023: 313, 2026 bis Sept.: 37 (BELEGT, Zählung Shopify-Katalog; Anlagen ≠ Umsatz) | nicht erkennbar |

Lehre: Das Konzept „Künstlerstil + eigene Location als Premium“ ist in den USA beim Marktführer angekündigt, aber nicht gestartet. Papier zeigt, dass selbst 56 % Rohmarge bei hohem Marketinganteil nicht automatisch Gewinn bedeuten.

### 6. Deutsche und europäische Konkurrenz

| Anbieter | Typ | Preis (Beispiele) | Personalisierung / Vorschau | Größe (Signal) | KI |
|---|---|---|---|---|---|
| **die kartenmacherei** (Gilching, .de/.at/.ch) | Spezialist, Marktführer Vorlagen | Save-the-Date 1,15–1,45 €, Einladung 1,58–1,80 €, Klappkarte 2,80–3,12 € (+0,50 € Folie), Sitzplan-Plakat 19 € (BELEGT, Vorarbeit) | Vorlage, Text, Farbe, Foto; Live-Konfigurator | 36.172 Trustpilot-Bewertungen, 17.474 in 12 Monaten (BELEGT) | keine |
| **Kartenliebe** (München) | Spezialist | Einladung 2,95–4,50 €/Stk. (ANBIETERANGABE), Acryl ab 15,95 € | Vorlage, Foto; Wandbilder am nächsten Werktag | 9.711 Bewertungen, 1.721 in 12 Monaten (BELEGT) | keine |
| **Atelier Rosemood** (FR, DE-Shop) | Premium-Spezialist | Einladung ab 1,16–2,41 €/Stk. (BELEGT) | Vorlage, Probedruck | 753 Bewertungen, 639 in 12 Monaten (BELEGT) | keine; laut Prüfer selbe Gruppe wie kartenmacherei |
| **Tatengold** u. a. Ateliers | Handarbeit | Design-Sets 690–2.590 € ohne Druck (BELEGT) | voll individuell, Wochen Vorlauf | 4 Paare/Monat (ANBIETERANGABE) | keine |
| **Cartalia Studio** (UK, DE-Shop) | international | Location +185/355 €, Einladung 8,95–35,95 €/Stk. (BELEGT, Vorarbeit) | menschliche Zeichnung, 3–5 Wochen | keine Bewertungsbasis | keine |
| **Canva Print** + Vorlagenhändler | DIY | Einladungen ab 19 € für 25 Stk. (ANBIETERANGABE, Vorarbeit) | volle Freiheit, KI-Bildgenerator | Canva 7.498 Bewertungen (alle Produkte) | ja, Einzelbild |
| **CEWE** | Generalist | Day-of-Produkte ab 32,98 € (laut Prüfer) | Foto auf Vorlage | sehr groß | keine Komposition |
| **myprintcard** (Augsburg) | Spezialist | Einladungen ab 72,60 € (30 Stk.) | Vorlage | 24.065 Bewertungen, nur 478 in 12 Monaten; Insolvenzverfahren seit 01.07.2026 | keine |

**Ampel GELB:** Der Gesamtmarkt ist stark besetzt, ein Frontalangriff auf Kartenpreise ist für einen POD-Händler aussichtslos. Die Unterkategorie „individuelles Designsystem aus eigenen Fotos mit Sofortvorschau, übertragen auf Suite, Day-of, Zeitung und Wandbild“ bietet in DE nach unserer Prüfung niemand an (Etsy, Amazon und Instagram waren nicht auslesbar – nicht belegt, dass es niemand tut). Einstieg über Zielgruppe (besondere Location) und Preisband zwischen Vorlage (≈ 2 €/Karte) und Atelier (≥ 690 € nur Design).

### 7. Konkreter KI-Mehrwert und Umsetzung

**Was die KI tut (Pipeline):**

1. Upload: 2–6 Paarfotos (optional Hund), 1–3 Location-Fotos, Formular (Namen, Datum, Orte, Stil). Pflicht-Checkboxen zu Bildrechten (Fotograf, § 72 UrhG) und Einwilligung abgebildeter Personen.
2. Analyse: Vision-LLM extrahiert Merkmale (Haare, Brille, Hund, Baustil, Farben), Qualitäts- und Moderationsprüfung (Minderjährige, Prominente, Logos).
3. Varianten: 3 Stilvarianten der Szene (Gemini 3.1 Flash Image in 0,5K–1K); Palette, Monogramm und Ornamente deterministisch.
4. Auswahl: Layout-Engine rendert sofort Mockups der ganzen Suite mit echten Namen und das Schild am Location-Foto.
5. Änderung: 2–4 Korrekturrunden per Text, Edit mit Gemini 3 Pro Image 2K; Architektur gegen das Location-Foto geprüft; ab Runde 4 Designer-Nacharbeit.
6. Final: Master-Illustration eingefroren (Hash, Modellversion), nie neu generiert; nicht-generatives Upscaling für A1; Linien und Monogramm vektorisiert als Folienmaske.
7. Produktionsdatei: PDF/X-4 je Partner (Beschnitt, Folienkanal), Preflight.
8. QA: Softproof = Druck-PDF; Paar gibt jede Seite per Checkbox frei; automatische Text-, Namens- und CSV-Prüfung; menschliche Sichtprüfung (Gesicht, Architektur, Folie).
9. Übergabe: WIRmachenDRUCK und Onlineprinters in der Testphase manuell (keine API), Print API per REST.
10. Hochzeitszeitung: Gäste laden über einen Sammellink Texte, Sprachnachrichten und Fotos hoch; das LLM schreibt nur aus diesen Eingaben, 8–12 Comic-Panels, Freigabe durch die Trauzeugen.

| Kriterium | Einschätzung |
|---|---|
| Technischer Schwierigkeitsgrad | 4 von 5 (Identität von zwei Personen + Architektur, Folienmaske, Mehrformat-Layout) |
| Generierungen | Vorschau ≈ 4 Bildaufrufe + 1 Analyse; Käufer Phase 1+2 ≈ 10 Bilder Pro-2K + 4 Bilder Flash-2K + Vektorisierung + Upscale (ANNAHME) |
| API-Kosten | Gemini 3 Pro Image 0,134 USD je 1K/2K-Bild, Gemini 3.1 Flash Image 0,045 (0,5K) / 0,067 (1K) / 0,101 (2K) USD (BELEGT, ai.google.dev, 01.10.2026). Modell: 0,45 € je Vorschau-Sitzung, 2,50 € Finalisierung je Käufer; mit Nichtkäufern ≈ 10 € je Bestellung (Basis) |
| Manuelle Nacharbeit | bei ≈ 20–35 % der Aufträge 5–20 Min., ≈ 5 % > 30 Min. (ANNAHME, vor Start mit 20–30 Paaren messen) |
| Prüf- und Supportzeit | Modell 30 + 12 Min. je Erstbestellung (ANNAHME) |
| Konsistenzrisiken | Identitätsdrift bei Neu-Generierung (Abhilfe: eingefrorener Master), Modellwechsel im 12-Monats-Zyklus, Farbunterschiede zwischen Druckpartnern, Folienstärken |
| Automatisierung | hoch für Bild, Layout, Preflight, Softproof, Textprüfung, Phasen-Mails, Print API; gering für WMD/Onlineprinters-Bestellungen; menschlich bleiben Identitäts- und Architekturprüfung (kein automatischer Gesichtsabgleich, Art. 9 DSGVO) |

**Ehrliche Grenze:** KI-Illustrationen sind 2026 Allgemeingut (Gemini, ChatGPT, Canva). Der Vorsprung liegt im Prozess (Designsystem über alle Formate, Druckqualität, Prüfung, Terminsicherheit) und in einer Location-Bibliothek mit Partnerschaften, nicht im Bildmodell.

### 8. Kostenlose Vorschau

| Punkt | Empfehlung |
|---|---|
| Wow-Effekt | sehr hoch: eigenes Paar, eigener Hund, eigene Location nach 60–90 Sekunden in der kompletten Suite mit echten Namen |
| Kosten je Vorschau | ≈ 0,25–0,48 € (ANNAHME auf BELEGT-Modellpreisen); Modell 0,45 € |
| Missbrauch | mittel bis hoch: Screenshot und Druck bei „Eigenes Design“-Angeboten (ab 1,80 €/Karte), Bot-Nutzung, fremde Fotos |
| Wasserzeichen | ja, halbtransparent über der Illustration, Vorschau nur in 0,5K–1K, kein Download ohne Text |
| Gratis-Varianten | 3 Stile + 1 Korrektur; weitere Runden gegen 29 € Anzahlung (wird verrechnet) |
| E-Mail vor Vorschau | ja, nach dem Upload und vor dem Reveal (unscharfer Teaser vorher) – Bot-Schutz und Lead für die Folgephasen; Werbe-Mails nur mit separatem Double-Opt-in |

### 9. Produktionspartner

| Prüfpunkt | WIRmachenDRUCK (DE, Hauptpartner) | Onlineprinters (DE, Ausweichpartner Karten) | Print API (NL, API-Weg) |
|---|---|---|---|
| Produktion ab 1 | Hartschaum, Acryl, Broschüre, Hardcover ab 1; Karten ab 25, Kuverts ab 250 (Auf der Website bestätigt) | Folienkarten ab 10 (Auf der Website bestätigt) | ab 1 (Auf der Website bestätigt) |
| Direktversand | Lieferadresse frei (Auf der Website bestätigt) | ja (Auf der Website bestätigt) | ja (Vom Anbieter beworben) |
| Neutral / White Label | **nicht dokumentiert – Noch anzufragen** (Blocker); Reseller-Programm beworben | neutrales Paket, Lieferschein, Label (Auf der Website bestätigt) | blanko Karton, eigenes Logo auf Lieferschein (Vom Anbieter beworben) |
| Shopify / WooCommerce | nein – Noch anzufragen | nein – Noch anzufragen | keine App; Web-Plugin – Noch anzufragen |
| API | keine öffentliche – Noch anzufragen | keine | REST-API mit Testumgebung (Vom Anbieter beworben) |
| Datei je Bestellung | ja (Auf der Website bestätigt) | ja | ja, je Position |
| Produktion / Versand | ≈ 3 Arbeitstage, Versand DE frei (Auf der Website bestätigt) | ≈ 5 Arbeitstage | 1 Werktag + 1–3 Tage (Kalkulator) |
| Einkauf (netto) | 75 Postkarten DIN lang + Gold 52,60 €; 75 Klappkarten DIN lang + Gold 97,22 €; 250 DL-Kuverts 13,16 €; Hartschaum 50×70 21,79 €, A1 24,75 €; 10 Tischnummern A4 30,13 €; 100 Menükarten Gold 55,00 €; Broschüre A4/20 S./60 Stk. 134,06 € (alle BELEGT, Preisrechner 01.10.2026) | A6 flach mit Goldfolie 60 Stk. 26,73 € (BELEGT) | Plexiglas 40×60 24,06 €, Tischkarten 1,00 €/Stk. (BELEGT) |
| Reklamation | „reiner Druckdienstleister“, prüft keine Inhalte; 2 Wochen Rügefrist (AGB) | Datencheck ohne Rechtschreibung | 2 Wochen Rügefrist, nur Neudruck (AGB) |

Nicht POD-fähig: Letterpress, Blindprägung, echtes Wachssiegel, Büttenpapier, gefütterte Kuverts, Staffeleien (Leihe über die Location). WIRmachenDRUCK führt nur Büro-Kuverts (Qualitätsrisiko). **Vor dem Start nötig:** schriftliche Bestätigung von Neutralversand/Reseller-Versand ohne Preisangaben bei WMD, Musterbestellung Folie und Hartschaum (nach eurer Freigabe).

### 10. Kosten, Verkaufspreise, Bundle, Upsells

| Angebot (Erstbestellung) | Preis brutto | Einkauf netto (inkl. Versand) | Mix Basis |
|---|---:|---:|---:|
| Start: Designsystem + 75 Save-the-Dates | 299 € | 52,60 € | 45 % |
| Spätstart: Designsystem + 75 Einladungen + Kuverts | 419 € | 110,38 € | 20 % |
| Suite: Designsystem + Save-the-Date + Einladung | 519 € | 162,98 € | 15 % |
| Day-of-Start: Designsystem + Day-of-Set | 529 € | 131,67 € | 8 % |
| Komplett vorab: Designsystem + STD + Einladung + Day-of | 879 € | 294,65 € | 5 % |
| Hochzeitszeitung (Trauzeugen, 60 Expl.) | 349 € | 134,06 € | 7 % |

Upsells (Quote Basis): Acryl statt Hartschaum +69 € (4 %), Gästebuch 69 € (4 %), 48-h-Express 39 € (6 %), zusätzliche Korrekturrunde 49 € (5 %). Folgephasen desselben Paares (Einladung 249 €, Day-of 379 €, Danke 159 €, Wandbild 129 €): 0,45 Folgebestellungen je Neukunde in 12 Monaten, DB je Folgebestellung ≈ 50 % der Erstbestellung (ANNAHME). Alle Preise ANNAHME, Einkaufspreise BELEGT.

### 11. Marketing und Creatives

**Kanäle (Basis-Mix des Ökonomie-Prüfers, ANNAHME):** Meta-Ads 55 % der Neukunden zu ≈ 183 € (CPC 1,00 € ÷ 13 % Klick→Upload × 70 % Upload→Vorschau × 6 % Vorschau→Kauf), Google 8 % zu 160 €, Pinterest/organisch 12 % zu 85 €, Location- und Planer-Partner 12 % zu 115 € (10 % Paarrabatt + 25 € Gutschrift + Gewinnungskosten), Empfehlungen 8 % zu 40 €, Etsy 3 % zu 75 €, Messen 2 % zu 230 € → blended ≈ 150 € inkl. Musterversand.

Belegte Kanalsignale: Pinterest ist Hauptinspirationsquelle (≈ 74 % der Paare, WeddyPlace-Studie 2022, ANBIETERANGABE, älter); Minted 211.745 Pinterest-Follower, kartenmacherei ≈ 19.900 (BELEGT, Zähler). Meta DE Median-Kosten pro Kauf ≈ 63 (SCHÄTZUNG, alle Branchen, kleine Warenkörbe dominieren).

**Drei Creatives (5–15 Sekunden):**

1. **Vom Handyfoto zur Suite (Vorher/Nachher):** wackeliges Selfie mit Hund + Handyfoto des Gutshofs → Pinselstrich-Wipe → Aquarell von Paar und Hund vor genau diesem Gutshof → Kamerafahrt über die Suite mit echten Namen → „Vorschau in 60 Sekunden – kostenlos“.
2. **Goldfolie im Licht (Reveal/ASMR):** Makro, Karte aus dem Kuvert, Lichtschwenk über das Folien-Monogramm, Schnitt auf das Willkommensschild im selben Stil – „Ein Design. Von Save-the-Date bis Sitzplan.“
3. **„Wer hat das verraten?!“ (Reaktion):** Trauzeugin überreicht die Hochzeitszeitung mit Comic der Kennenlerngeschichte, Paar lacht – „Aus 30 Sprachnachrichten wurde ein Magazin.“

Creative-Potenzial 8/10 (Produktionsanalyse). Abzug: gesättigtes Content-Feld; echte Paare brauchen schriftliche Einwilligung (§ 22 KUG); KI-Herkunft offenlegen (§ 5a UWG, Art. 50 KI-VO).

### 12. Finanzmodell (Kurzfassung; vollständig in `finanzmodell/ergebnisse.md`)

**Stückrechnung je Erstbestellung:**

| Position | Konservativ | Basis | Optimistisch |
|---|---:|---:|---:|
| Warenkorb brutto | 395,92 € | 417,21 € | 437,99 € |
| Umsatzsteuer 19 % | 63,21 € | 66,61 € | 69,93 € |
| Nettoumsatz | 332,70 € | 350,60 € | 368,06 € |
| Produkte je Bestellung | 2,9 | 3,2 | 3,4 |
| Produktion inkl. Versand (Partner) | 104,04 € | 108,27 € | 117,28 € |
| Verpackung/Beilage | 0,68 € | 0,72 € | 0,77 € |
| Zahlungsgebühren | 9,44 € | 9,93 € | 10,40 € |
| KI: Vorschauen der Nichtkäufer | 10,80 € | 7,05 € | 4,05 € |
| KI: Käufer (Vorschau + Finalisierung) | 2,95 € | 2,95 € | 2,95 € |
| Infrastruktur | 0,30 € | 0,30 € | 0,30 € |
| Qualitätsprüfung (30 Min.) | 15,00 € | 15,00 € | 15,00 € |
| Kundenservice (12 Min.) | 6,00 € | 6,00 € | 6,00 € |
| Ersatzproduktion (Erwartungswert) | 7,18 € | 4,96 € | 3,99 € |
| Erstattungen (Erwartungswert) | 14,97 € | 10,52 € | 8,28 € |
| **DB I (vor CAC)** | **161,34 €** | **184,90 €** | **199,03 €** |
| DB-I-Quote | 48,5 % | 52,7 % | 54,1 % |
| Max. CAC inkl. Folgephasen 12 Monate | 179,49 € | 226,50 € | 257,25 € |

**Gewinn je Erstbestellung nach CAC (Basis):** CAC 20 € → 164,90 €; 40 € → 144,90 €; 60 € → 124,90 €; 80 € → 104,90 €; 100 € → 84,90 €; 120 € → 64,90 €; 150 € → 34,90 €. Break-even-CAC Erstkauf = 184,90 €.

**Skalierung (Basis; operatives Ergebnis vor Ertragsteuern und vor Gründerlohn; Fixkosten inkl. Angestellter):**

| Jahresnettoumsatz | Bestellungen/Jahr | /Monat | /Tag | Neukunden | DB I gesamt | Fixkosten | Ergebnis CAC 60 € | CAC 100 € | CAC 150 € (realistisch) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 250.000 € | 844 | 70 | 2,3 | 582 | 131.846 € | 26.000 € | 70.921 € | 47.637 € | 18.532 € |
| 500.000 € | 1.688 | 141 | 4,6 | 1.164 | 263.693 € | 95.000 € | 98.841 € | 52.273 € | −5.937 € |
| 1.000.000 € | 3.376 | 281 | 9,2 | 2.328 | 527.386 € | 170.000 € | 217.682 € | 124.547 € | 8.127 € |
| 5.000.000 € | 16.881 | 1.407 | 46,2 | 11.642 | 2.636.929 € | 720.000 € | 1.218.411 € | 752.733 € | 170.634 € |

Konservativ (realistischer CAC 215 €) ist das Ergebnis bei 1 Mio. € −265.939 €, optimistisch (CAC 85 €) +192.088 €. Nach einem kalkulatorischen Gründerlohn von 120.000 € p. a. bleibt bei 1 Mio. € und CAC 150 € ein Verlust von ≈ −112.000 €; bei CAC 100 € ≈ +4.500 €.

**Sensitivität (Basis, 1 Mio. €, CAC 150 €, Ausgangswert +8.127 €):** CAC +30 % → −96.651 €; Warenkorb −15 % → −126.785 €; Prüf- und Supportzeit ×2 → −53.482 €; Produktion +15 % → −40.048 €; Reklamationen ×2 → −36.020 €; KI-Kosten ×2 → −20.396 €; Vorschau→Kauf −40 % → −6.135 €. **Preis und CAC entscheiden, KI-Kosten kaum.**

### 13. Wiederkäufe und Produktwelt

- Kein klassischer Wiederkauf, aber eine **Kaufkette** in ≈ 12 Monaten (Save-the-Date → Einladung → Day-of → Danke) mit dem einmal gewonnenen Paar, ohne zweiten CAC.
- **Mehrere Käufer je Hochzeit:** Trauzeugen (Zeitung, JGA), Eltern (Wandbild), Gäste als künftige Paare (Empfehlung, ANNAHME).
- Nach der Hochzeit: Jahrestage, Umzug, Geburt, Taufe, Weihnachtskarten im selben Stil (Brücke wie bei kartenmacherei). Die Familienfeste-Suite (Kandidat E) ist eigenständig unwirtschaftlich, als Folgekauf bestehender Kunden aber ohne CAC denkbar (ANNAHME).

### 14. Risiken und stärkste Gegenargumente

1. **Zahlungsbereitschaft unbelegt:** Belegt ist sie nur für menschliche Ateliers. Für eine neue, als KI gekennzeichnete Marke gibt es keinen Kaufbeleg; der Marktführer verkauft Gestaltungsservice für 15–50 €, RSVP und digitale Save-the-Dates gibt es gratis (Markt-Prüfer).
2. **CAC:** Der Basis-CAC von 150 € setzt ≈ 45 % nicht bezahlte Neukunden voraus. Für eine neue Marke ist das erst nach 12–18 Monaten belegbar.
3. **Durchschnittspaar zahlt weniger:** Ø 303–338 € Papeterie-Budget; unser Einstieg (299–529 €) zielt auf das obere Segment.
4. **Schrumpfende Basis:** Eheschließungen auf Tiefstand, generische Suchnachfrage rückläufig, 22 % papierlos.
5. **Nachahmung:** Minted hat die Funktion angekündigt; die Marktführer können KI nachrüsten; KI-Output ist kaum schutzfähig.
6. **Abgriff über die Vorschau:** Screenshot + „Eigenes Design“-Druck beim Marktführer.
7. **Betrieb:** Terminware mit null Fehlertoleranz bei Namen und Daten; WMD ohne API und ohne dokumentierten Neutralversand.
8. **Mahnendes Vorbild:** Papier (UK) schreibt trotz 56 % Rohmarge operative Verluste.

### 15. Skalierbarkeit

- 1 Mio. € netto ≈ 3.400 Bestellungen von ≈ 2.330 Paaren – deutlich unter 10.000 Bestellungen.
- Prüfung und Support binden bei 1 Mio. € ≈ 1,4 Vollzeitstellen, bei 5 Mio. € ≈ 7 (Modell, 42 Min. je Bestellung). Nur mit Automatisierung (Stichproben statt Vollprüfung) sinkt das.
- Engpässe: Partner ohne API (WMD), Saisonspitzen (Spitzenmonat ≈ 14 Bestellungen pro Tag bei 1 Mio. €), Location-Bibliothek als Aufbauarbeit.
- Erweiterbar auf AT/CH (Zoll für CH prüfen) und auf weitere Feste im selben Designsystem.

### 16. Rechtliches (produktspezifisch, fachlich prüfen lassen)

- **Widerruf:** personalisierte Karten, Schilder, Zeitung und Wandbild fallen wahrscheinlich unter § 312g Abs. 2 Nr. 1 BGB, auch vor Produktionsbeginn (EuGH C-529/19); Pflichtinformation nach Art. 246a § 1 Abs. 3 EGBGB; Widerrufsbutton nach § 356a BGB (seit 19.06.2026) für unpersonalisierte Teile. Vorauszahlung späterer Phasen nur mit klarer Absage-Regelung.
- **Proof und Haftung:** Kaufrecht (§ 650 BGB); dokumentierte Freigabe je Seite; gesetzliche Rechte nach § 476 BGB nicht abdingbar.
- **Fotos:** Hochzeits- und Verlobungsfotos gehören meist dem Fotografen (§ 72 UrhG); Location-Fotos vom Privatgrund nicht frei (BGH V ZR 45/10); keine Location-Marken ohne Zustimmung.
- **Personen und Daten:** § 22 KUG für Gäste und Eltern; Gästeliste = Daten Dritter (Zweckbindung, AV-Verträge, Löschung); kein automatischer Gesichtsabgleich (Art. 9 DSGVO).
- **KI-Kennzeichnung:** Art. 50 KI-VO seit 02.08.2026; nicht mit „handgezeichnet“ werben (§ 5a UWG).
- **Produktsicherheit/Verpackung:** Eigenmarke = Hersteller (GPSR Art. 13, § 4 ProdHaftG); Verpackungspflichten seit 12.08.2026 (PPWR/VerpackDG) – Rolle beim Direktversand durch Partner klären.

### 17. Was der Test beweisen muss

Siehe `testplan.md`. Kernfrage: Kaufen mindestens 5 % der Paare, die eine Vorschau sehen, zum Einstiegspreis von 299 € (Designgebühr ≈ 179 €), und kostet ein zahlendes Paar über Meta höchstens 150 €?

---

## Reserve (Platz 2): Kinderzimmer-Stilwelt – Wandwelt auf Maß aus dem Raumfoto

### Auf einen Blick

| Merkmal | Wert |
|---|---|
| Zielgruppe | Werdende Eltern beim ersten Kind (Nestbau, 2.–3. Trimester); Eltern von 3- bis 7-Jährigen beim Umbau zum Schulkindzimmer; Großeltern als Schenkende |
| Ø-Warenkorb (brutto) | **402 €** Basis (359 € konservativ, 431 € optimistisch) |
| DB I vor CAC | **174 €** (51,4 %), konservativ 132 €, optimistisch 195 € |
| Max. tragbarer CAC | 174 € Erstkauf, 177 € inkl. Folgekäufe; Break-even-CAC bei 1 Mio. € inkl. Fixkosten ≈ 118 € |
| Realistischer CAC (blended) | 155 € Basis (215 € konservativ, 110 € optimistisch) – ANNAHME |
| Bestellungen für 1 Mio. € netto | **3.193 pro Jahr** = 266 pro Monat = 8,7 pro Tag |
| Ergebnis bei 1 Mio. € und realistischem CAC | −436.872 € / **−106.111 €** / +70.911 € (konservativ / Basis / optimistisch) |
| Stärkste Wettbewerber | Photowall (SE, eigene Fabrik, 39 €/m² eigenes Bild, 9.901 Trustpilot-Bewertungen) und Gimmersta mit Rebel Walls und Hovia (Designteam, 50 €/m²); myposter (KI-Stilfilter gratis); Tenstickers (Namens-Kindertapete auf Maß) |
| EU-Produktionspartner | WIRmachenDRUCK (Vliestapete 11,43 €/m² + 8,90 € netto, DE-Versand frei, BELEGT); Caspar Manufaktur (DE, Shopify-App mit Neutralversand, CE nach EN 15102, Preise noch anzufragen); Printseekers (LV, Fallback); Printful (Poster) |
| KI-Mehrwert | Welt aus Raumfoto und Wandmaß, Kuscheltier oder Haustier als Figur, Bahnplan mit Sperrzonen, Übertragung auf Poster und Messlatte |
| Bewertung | **59–61** (Ökonomie 61: 16/11/12/8/6/8; Markt 59: 16/11/11/7/6/8) |
| Ampel / Datensicherheit | **GELB** / **MITTEL** (Kosten belegt; Zahlungsbereitschaft für die Gestaltungsgebühr und CAC nicht) |

### Produkt, Anlass und Markt

- **Produkt:** „Wandwelt nach Maß“ = Gestaltung 119 € + Wanddruck 39 €/m² Wandfläche (Teilwand 1,80×2,50 m = 294,50 €, Standard 2,80×2,50 m = 392 €, groß 3,80×2,55 m = 496,91 €); Set-Aufpreis 99 € (Poster-Trio ungerahmt, Messlatte, A3-Farbproof). Gestrichen: gerahmte Poster, Metallschild, Textilien, Wimpelkette (kein Partner).
- **Anlass:** Nestbau mit harter Frist vor dem Geburtstermin; Schulkindzimmer (811.500 Einschulungen 2025/26, BELEGT laut Vorarbeit); Geschwister (35,1 % der Geborenen im 1. Halbjahr 2026 waren zweite Kinder, BELEGT, Destatis).
- **Größe:** 654.241 Geburten 2025 (BELEGT, Destatis), davon ≈ 302.000 Erstgeburten (SCHÄTZUNG); Geburten 2025 −3,4 %, 1. Halbjahr 2026 −0,9 %.
- **Markt-Preisleiter für eine Wand mit 7,5 m² (BELEGT-€/m², Ableitung):** Pixers 130–218 €, wall-art.de ≈ 200–235 €, Photowall 292–412 €, Rebel Walls 293–375 € + Designstudio 122 €/h; Tenstickers Namens-Kindertapete auf Maß ab 99,25 € (BELEGT laut Prüfer). Ein Kinderzimmer-Set über 300 € ist in DE nicht als Angebot belegt (größtes belegtes Bundle 110,70 €, Kidsmood).
- **US-Vorbild:** Pottery Barn Kids & Teen 1,138 Mrd. USD Umsatz GJ 2025, Wachstum „driven by … baby offerings“ (BELEGT, 10-K/10-Q); Personalisierungsanteil unbekannt.

### Warum nur Reserve

Der DB I ist hoch (174 €), aber der realistische CAC für einen 400-€-Erwägungskauf mit Raumfoto-Upload liegt bei ≈ 135–155 € (Kaltverkehr Meta mit 0,6–0,8 % Klick→Kauf, Creator-Honorare, Rabattstandard der Branche). Für ein operatives Ergebnis von null bei 1 Mio. € wären ≤ 118 € nötig, mit Gründerlohn ≤ 77 €. Dazu kommen:

- Die Standardwand für 392 € ist das teuerste Angebot der belegten Preisleiter; Photowall, Hovia und Tenstickers liefern schneller und günstiger, teils mit Designteam und 30 Tagen Kulanz.
- Nach § 4 PAngV ist für Tapete der Grundpreis je m² anzugeben; enthält er die Gestaltung, steht statt „39 €/m² wie Photowall“ ≈ 51–65 €/m² in der Werbung (rechtliche Einordnung ANNAHME, prüfen).
- Raumvorschau und KI-Stil sind Commodity (Genroom, myposter); der Burggraben liegt nur in Figur, Bahnplan und Prozess.
- Maß- und Nahtreklamationen beim Unikat trägt der Shop; WMD-AGB (2 Wochen Rügefrist, 1 Jahr Verjährung) gegen 2 Jahre B2C-Gewährleistung.

### Rechnung (Basis, vollständig in `finanzmodell/ergebnisse.md`)

| Position | Wert |
|---|---:|
| Warenkorb brutto / netto | 401,93 € / 337,75 € |
| Produktion + Versand | 105,35 € |
| KI (Nichtkäufer + Käufer) | 12,80 € (Vorschau→Kauf 2,5 % nach Gating) |
| Prüfung + Support (25 + 14 Min.) | 19,50 € |
| Nachdruck + Erstattung | 16,05 € |
| **DB I** | **173,54 € (51,4 %)** |
| Gewinn je Erstbestellung bei CAC 60 / 100 / 155 € | 113,54 / 73,54 / 18,54 € |
| 1 Mio. € netto: Bestellungen | 3.193 pro Jahr, 266 pro Monat, 8,7 pro Tag |
| Ergebnis bei 1 Mio. € und CAC 80 / 100 / 155 € | +111.590 / +53.536 / −106.111 € |

### Bedingungen für eine Wiederaufnahme (aus beiden Gegenprüfungen)

Vorbestelltest mit bezahlter Anzahlung zum vollen Preis; ≥ 30–50 bezahlte Bestellungen bei Ø ≥ 380 € brutto; Klick→Kauf ≥ 0,7 % bei CPC ≤ 0,95 € (Media-CAC ≤ 125 €); blended CAC ≤ 118 €; die sichtbare Gestaltungsgebühr kostet gegenüber einem All-in-Preis höchstens 15–20 % Conversion; ≥ 50 % der Käufer nennen Figur oder Raumkomposition als Kaufgrund; WMD-Neutralversand bestätigt; Nachdruckquote ≤ 4,5–5 % in den ersten 100 Wänden.

---

## Querschnitt: Was für alle Kandidaten gilt

1. **POD-Druck ist gegenüber den Marktführern nicht margenfähig** (z. B. Print API 1,08 € je Platzkarte gegenüber 0,88 € Verkaufspreis beim Marktführer). Marge entsteht nur über eine ausgewiesene oder implizite Gestaltungsleistung – genau die Größe, deren Zahlungsbereitschaft für KI-Marken unbelegt ist.
2. **Ein um 15 % niedrigerer Warenkorb bringt jedes Modell bei 1 Mio. € ins Minus**; KI-Kosten sind dagegen fast irrelevant.
3. **CAC:** Alle Neuzuschnitte haben nicht bezahlte Kanäle optimistisch angesetzt; die Prüfer haben den CAC um 14–45 % erhöht. Regelmäßig fehlten Creative-Kosten, marktübliche Partnerprovisionen (10–15 % bzw. höher) und Rabatte.
4. **Belegt ist Zahlungsbereitschaft für Handarbeit**, nicht für KI-gekennzeichnete Gestaltung einer Marke ohne Bewertungen. Diese eine Annahme muss der Test zuerst klären – beim Kandidaten mit dem stärksten Anlass und dem höchsten tragbaren CAC.
