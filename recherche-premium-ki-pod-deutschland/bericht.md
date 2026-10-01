# KI-personalisierte Premium-POD-Produkte für Deutschland – Recherchebericht

**Recherchedatum: 01.10.2026.** Web-Quellen wurden am 01.10.2026 abgerufen (Vorarbeit aus der ersten Recherche: 30.09.2026), sofern nicht anders angegeben. Laufende Zähler (Bewertungen, Follower) gelten mit Stand des Abrufs.

**Kennzeichnung:** **BELEGT** = auf einer Primärquelle direkt geprüft (Statistik, Gesetz, öffentlicher Zähler, Preis auf der Anbieterseite). **ANBIETERANGABE** = Selbstauskunft (Größe, Kunden, Qualität). **SCHÄTZUNG** = Drittanbieter-Benchmark oder abgeleitete Zählung. **ANNAHME** = eigene Setzung. Bewertungen sind keine Bestellungen, Follower keine Käufer, Finanzierung kein Umsatz, Umsatz kein Gewinn.

**Ordnerinhalt:**

| Datei | Inhalt |
|---|---|
| `bericht.md` | dieser Bericht |
| `finalisten.md` | Detailanalyse des bedingten Finalisten und der Reserve |
| `testplan.md` | 14-Tage-Test für Platz 1 |
| `longlist.md` | 50 Kategorien mit Warenkorb, Bestellungen für 1 Mio. € (Jahr/Monat/Tag), Punkten, Datensicherheit, Status |
| `shortlist.md` | 10 vertiefte Kandidaten mit Prüferurteil, nachgeprüften Aussagen und dem Neuzuschnitt der vier stärksten |
| `wettbewerber.md` | Wettbewerber je Shortlist-Kandidat (DE/AT/CH/EU/international, Etsy/Amazon, Nicht-KI-Alternativen, US-Vorbilder) |
| `produktionspartner.md` | Partner je Kandidat mit Prüfstatus, Stücklisten, KI-Pipeline, Vorschau-Konzept |
| `quellen.md` / `quellen-vollstaendig.md` | kuratierte Kernquellen / alle rund 1.300 URL-Einträge aus den Rohdaten |
| `finanzmodell/` | reproduzierbares Modell: `modell.py` (Rechenkern), `parameter.py` (Eingaben mit Kennzeichnung), `berechnen.py` (Aufruf), Ergebnisse als `ergebnisse.md`, `.json`, `cac_matrix.csv`, `skalierung.csv` |
| `rohdaten/`, `werkzeuge/` | strukturierte Ergebnisse aller Recherche-Agenten; Skripte, die die Markdown-Dateien daraus erzeugen |

---

## 1. Executive Summary

**Welches Produkt zuerst testen?** Die **KI-Designwelt Hochzeit**: Aus Fotos von Paar, Hund und Location entsteht eine Illustration im gewählten Stil und daraus ein Designsystem für die gesamte Hochzeitspapeterie. Verkauft wird es in Phasen: Save-the-Date, Einladung, Day-of-Beschilderung und Danksagung. Dazu kommen die Hochzeitszeitung für die Trauzeugen und ein Wandbild nach der Hochzeit. Die Marge kommt aus einer im Preis enthaltenen Designleistung, gedruckt wird zu Marktpreisen.

**Warum?**

- Der Kaufanlass ist der stärkste der Recherche. Feste Fristen erzwingen den Kauf, pro Paar gibt es 3–5 Kaufpunkte in etwa 12 Monaten.
- Zahlungsbereitschaft für individuelle Location-Illustration ist belegt, allerdings nur für Handarbeit. Beispiele: das Atelier Tatengold mit Design-Sets ab 690 € ohne Druck (Kapazität „bis zu vier Paare pro Monat“) und Cartalia mit +185 € bzw. +355 € für die Zeichnung der Location (BELEGT).
- Zwischen Vorlagen-Marktführer (ca. 2 € je Karte) und Atelier (ab 690 € nur Design) fanden wir in Deutschland keinen Anbieter mit Sofortvorschau einer individuellen Illustration. Minted (USA) hat genau diese Funktion am 30.04.2026 angekündigt, bis 01.10.2026 aber keinen Start gemeldet.
- Der Kandidat hat den **höchsten Deckungsbeitrag vor Werbung (DB I) aller 10 Shortlist-Kandidaten**. Er ist der einzige, bei dem der Break-even-CAC bei 1 Mio. € Umsatz in allen Prüfrechnungen über dem realistischen CAC liegt.
- Der Test klärt die Annahme, an der alle Neuzuschnitte hängen: Wird eine KI-Gestaltungsgebühr bezahlt? Scheitert sie beim stärksten Anlass, ist auch die Reserve sehr wahrscheinlich nicht tragfähig.

**Plausibler Ø-Warenkorb:** etwa **400–440 € brutto je Erstbestellung** (Basis 417 €). Je Paar kommen inklusive Folgephasen etwa 510 € brutto zusammen (Modell, ANNAHME).

**Deckungsbeitrag vor Werbung:** etwa **185 € je Erstbestellung (53 % vom Nettoumsatz)**, konservativ 161 €, optimistisch 199 €. Daraus folgt:

- Der maximal tragbare CAC liegt bei 185 € für die Erstbestellung und bei 227 € inklusive Folgephasen.
- Damit das Ergebnis bei 1 Mio. € Umsatz inklusive Fixkosten mindestens bei null liegt, darf ein Neukunde höchstens etwa 153 € kosten.

**Bestellungen für 1 Mio. € Jahresnettoumsatz:** etwa **3.400 pro Jahr ≈ 280 pro Monat ≈ 9 pro Tag** (im Spitzenmonat etwa 14 pro Tag), von etwa 2.330 Paaren. Das liegt deutlich unter 10.000.

**Größte Unsicherheit:** Bezahlen Paare einer neuen, als KI gekennzeichneten Marke eine Designgebühr von etwa 150–180 €, und zu welchem CAC? Belegt sind nur Käufe bei menschlichen Ateliers. Vorschau→Kauf-Quote, Set- und Folgekaufquote und CAC sind nirgends gemessen. In der Basis kostet ein Neukunde realistisch etwa 150 €. Bei 1 Mio. € Umsatz bleibt dann operativ nur **etwa +8.000 € vor Gründerlohn** (etwa −112.000 € nach einem kalkulatorischen Gründerlohn von 120.000 €). Erst bei einem CAC um 100 € entsteht ein echtes Geschäft: etwa +125.000 € vor bzw. +5.000 € nach Gründerlohn.

**Ehrliches Gesamturteil:** Die Recherche hat **keinen Kandidaten gefunden, der im Basisszenario ohne Bedingungen wirtschaftlich überzeugt**. Es gibt **einen bedingten Finalisten (Hochzeit)** und **eine Reserve (Kinderzimmer-Stilwelt)**. Nach der Vorgabe „nicht künstlich auf fünf auffüllen“ bleibt es bei diesen beiden. Das Muster ist über alle 10 Kandidaten gleich:

- Der Druck über POD ist gegenüber den Marktführern nicht margenfähig.
- Marge entsteht nur über eine Gestaltungsleistung.
- Deren Zahlungsbereitschaft ist für KI-Marken unbelegt.

Bevor mehr Kapital fließt, sollte der 14-Tage-Test (ca. 5.000 €, davon 3.000 € Werbung) genau diese Frage beantworten.

---

## 2. Top-Finalisten

| Produkt | Zielgruppe | AOV (brutto, Basis) | Deckungsbeitrag vor CAC | Max. tragbarer CAC | Bestellungen für 1 Mio. € netto | Stärkster Wettbewerber | EU-Produktionspartner | KI-Mehrwert | Bewertung (100) | Datensicherheit |
|---|---|---:|---:|---:|---|---|---|---|---:|---|
| **Finalist 1 (bedingt): KI-Designwelt Hochzeit** | Verlobte 30–38 mit besonderer Location, 80–120 Gäste; Trauzeugen; Eltern | 417 € | 185 € (52,7 %) | 185 € Erstkauf; 227 € inkl. Folgephasen; ≈ 153 € für Ergebnis ≥ 0 bei 1 Mio. € | 3.376/Jahr · 281/Monat · 9,2/Tag | die kartenmacherei (Vorlagen-Marktführer); im Premiumsegment Ateliers (Tatengold) | WIRmachenDRUCK (DE), Onlineprinters (DE, Neutralversand belegt), Print API (NL, API) | Paar + Hund + Location → Illustration → Designsystem über 10–15 Formate; Sofortvorschau statt wochenlanger Proof-Schleifen | 60–61 | NIEDRIG–MITTEL |
| **Reserve: Kinderzimmer-Stilwelt** | Erst-Eltern (Nestbau), Eltern von 3- bis 7-Jährigen, Großeltern | 402 € | 174 € (51,4 %) | 174 € Erstkauf; ≈ 118 € für Ergebnis ≥ 0 bei 1 Mio. € | 3.193/Jahr · 266/Monat · 8,7/Tag | Photowall; Gimmersta (Rebel Walls, Hovia); myposter; Tenstickers | WIRmachenDRUCK (Vliestapete), Caspar Manufaktur (DE, Shopify-App), Printseekers (LV), Printful (Poster) | Welt aus Raumfoto + Wandmaß, Kuscheltier/Haustier als Figur, Bahnplan, Set-Übertragung | 59–61 | MITTEL |

Realistischer CAC (blended, ANNAHME auf SCHÄTZUNG-Benchmarks): Hochzeit 150 € (konservativ 215 €, optimistisch 85 €), Kinderzimmer 155 € (215 € / 110 €). Ergebnis bei 1 Mio. € und diesem CAC: Hochzeit −266 / **+8** / +192 Tsd. €; Kinderzimmer −437 / **−106** / +71 Tsd. € (konservativ / Basis / optimistisch, vor Gründerlohn).

---

## 3. Detailanalyse (Kurzfassung; vollständig in `finalisten.md`)

### Finalist 1 (bedingt): KI-Designwelt Hochzeit

| Thema | Kern |
|---|---|
| Produktidee | Designsystem des Paares aus Fotos; Phasenverkauf: Start (Design + 75 Save-the-Dates mit Goldfolie) 299 €, Einladung 249 €, Day-of aus Hartschaum/Papier 379 €, Danke 159 €; Hochzeitszeitung 349 € (Trauzeugen); Wandbild 129 € |
| Kaufanlass | feste Fristen: Save-the-Date 8–12, Einladung 4–6, Menü/Tisch 1–2 Monate vorher; Danksagung 2–4 Wochen danach (ANBIETERANGABE) |
| Zielgruppe / Größe | 348.813 Eheschließungen 2025 (BELEGT); Ø Papeterie 338 € (ANBIETERANGABE); Segment ≥ 250 € ≈ 140.000 Paare (SCHÄTZUNG) |
| Bestehender Markt | Vorlagenmarkt (Suite 80 Gäste ≈ 464–563 €, SCHÄTZUNG aus BELEGT-Preisen) und Ateliermarkt (ab 690 € nur Design, BELEGT); Volumen ≈ 118 Mio. € (SCHÄTZUNG, Obergrenze) |
| US-Vorbilder | Minted (> 300 Mio. USD erwartet 2026, ANBIETERANGABE; KI-Funktion angekündigt, nicht gestartet), Joy/Paperlust (Suite 518 USD je Paar, ANBIETERANGABE), Papier UK als Warnung (56 % Rohmarge, 3,8 Mio. GBP operativer Verlust, BELEGT) |
| Deutsche Konkurrenz | kartenmacherei, Kartenliebe, Rosemood, CEWE, Canva Print, Ateliers, Cartalia; myprintcard insolvent; Ampel GELB |
| KI-Mehrwert | Mehrfoto-Szene + Designsystem + Sofortvorschau; Text nie aus dem Bildmodell; Schwierigkeit 4/5; KI-Kosten ≈ 10 € je Bestellung inkl. Nichtkäufer |
| Produktionspartner | WIRmachenDRUCK (Preise BELEGT; Neutralversand und API noch anzufragen), Onlineprinters (Neutralversand BELEGT), Print API (API) |
| Kosten / Preis | Einkauf je Erstbestellung Ø 108 € netto inkl. Versand; Preis Ø 417 € brutto |
| Bundle / Upsells | Phasen als Folgekäufe (0,45 je Paar, ANNAHME); Acryl +69 €, Gästebuch 69 €, Express 39 €, Korrekturrunde 49 € |
| Marketing / Creatives | Meta, Pinterest, Location-Partner, Trauzeugen-Link; Creatives: Handyfoto → Suite, Goldfolie-ASMR, Hochzeitszeitung-Reaktion; Creative-Potenzial 8/10 |
| Finanzmodell | DB I 185 €; Ergebnis bei 1 Mio. € und CAC 150 €: +8 Tsd. € vor Gründerlohn |
| Risiken | unbelegte Zahlungsbereitschaft, CAC, schrumpfende Basis, Nachahmung (Minted, Marktführer), Abgriff über Vorschau, Terminware, WMD ohne API |
| Skalierbarkeit | 1 Mio. € ≈ 3.400 Bestellungen, ≈ 1,4 Vollzeitstellen Prüfung/Support; 5 Mio. € ≈ 16.900 Bestellungen, ≈ 7 Stellen |

### Reserve: Kinderzimmer-Stilwelt

Wandwelt auf Maß (Gestaltung 119 € + 39 €/m²) mit Kuscheltier oder Haustier als Figur, Bahnplan und Set-Aufpreis. Der DB I ist hoch (174 €), aber die etablierten Anbieter sind schnell, günstig und kulant: Photowall und Rebel Walls nehmen 39 €/m² für ein eigenes Bild, Hovia 50 €/m² mit Designteam, Tenstickers bietet Namens-Kindertapeten auf Maß an. Für ein Ergebnis von mindestens null bei 1 Mio. € wäre ein CAC ≤ 118 € nötig. Realistisch sind 135–155 €. Details in `finalisten.md`.

---

## 4. Was wurde verworfen?

**Nach Vertiefung bzw. Neuzuschnitt (DB I und realistischer CAC aus dem Modell, Basis):**

| Kandidat | Ergebnis | Hauptgrund |
|---|---|---|
| Mehrfoto-Familienbild (Generationen, Mensch + Tier) | verworfen nach Neuzuschnitt (58–60 Punkte) | Preisanker durch Handarbeit (Sketchus: handgezeichnetes A4 mit 5 Personen 239,99 €, wirbt „ohne KI“) und Automatik (MyPortrait: Leinwand 60×90 mit Live-Vorschau 109,95 €); niedrigster Warenkorb der vier, ≈ 5.000 Bestellungen für 1 Mio. € |
| Lebensweg-Festpaket (runde Geburtstage, Jubiläen) | nur Modul (54–60 Punkte) | Marge hängt an der Auflage; korrigiert DB I ≈ 121 € gegen CAC ≈ 96 € → bei 1 Mio. € −68 Tsd. €; Vorlaufkonflikt (Bestellung ≥ 4 Wochen vor der Feier) |
| Familienfeste-Suite (Geburt, Taufe, Kommunion, Konfirmation) | verworfen (51 Punkte) | DB I ≈ 37 € gegen CAC ≈ 80 €; CEWE und kartenmacherei bieten Vorlagen-Sets; Kerze als Anker schwach (Kerzenhändler drucken bereits Kundendesigns) |
| Reise-Erinnerungswand | verworfen (57) | DB I ≈ 57 € gegen CAC ≈ 95 €; KI-Reiseplakat aus Urlaubsfoto ist Gratisfunktion (Dreamina); keine Kauffrist |
| Hausporträt + Einzugs-Set | verworfen (57) | DB I ≈ 46 € gegen CAC ≈ 65 €; Set-Kaufbereitschaft unbelegt; Architekturtreue der KI |
| Team-Saisonabschluss-Set | verworfen (56) | DB I ≈ 29 € (Abstimmung mit 12–16 Familien); belegter Teamanker 70–130 €; Einwilligungen aller Eltern |
| Fahrzeug-Porträt und Garagenwelt | verworfen (57) | DB I ≈ 40 € gegen CAC ≈ 65 €; sechs etablierte DE-Anbieter für 30–130 €; Marken- und Designrechte der Hersteller |
| Feste türkisch-, arabisch- und russlanddeutscher Familien | verworfen (47) | Stückpreisanker 0,10–0,63 € je Karte; Paar-Illustration menschlich ab 0,17 € je Karte; DB I ≈ 8 € |

**Vor der Vertiefung verworfen oder nur beobachtet (Longlist-Vorbewertung):**

| Kategorie | Status | Grund |
|---|---|---|
| Küchen-/Duschrückwand mit Motiv | ROT | Spezialfertigung, Maß-/Bruchrisiko, geringer KI-Mehrwert |
| Raumabgestimmte Galeriewand | beobachten | Gegenbefunde: Desenio Deutschland 2025 −15 %, Framebridge mit erheblichen operativen Verlusten (BELEGT laut Scouts); als Upsell-Modul |
| Plüsch-Replik nach Foto/Zeichnung | ROT | keine EU-Fertigung ab 1 mit Direktversand, Spielzeugrecht |
| Weihnachts-Partnerlook (Pyjamas, Pullover) | ROT | keine EU-Fertigung, geringer KI-Mehrwert |
| Porzellan mit eingebranntem Dekor | ROT | kein POD-fähiger Einbrand-Partner, Lebensmittelkontakt |
| Namensschmuck | ROT | kein KI-Mehrwert, niedriger Warenkorb, rückläufig |
| Stadt-, Koordinaten-, Sternenkarte | ROT | Referenzmarkt ohne KI-Hebel, Warenkorb ≈ 65 € |
| Foto-Bastelsets (Bausteine-Mosaik, Diamond Painting, Malen nach Zahlen) | ROT | Lager nötig, kein KI-Mehrwert, besetzt |
| Vereins-Massenware (Stickeralbum, Pokale) | ROT | dominanter Spezialist (Stickerstars) bzw. Billigware |
| Kind als Held: Hörspiel + Figur | ROT | geschlossenes Ökosystem (Tonies/Yoto), kleiner physischer Anteil |
| Trauer-Drucksachen | ROT | Gatekeeper Bestatter, kaum bewerbbar |
| Haustier-Zubehör, Kinderkostüme, Namenspuzzle | ROT | Warenkorb 35–45 €, kein KI-Mehrwert, keine Fertigung |
| Einschulungs-Set mit KI-Held | beobachten | ein Saisonfenster, Schultüte nicht POD, Preisanker 34,99–39,90 € |
| Familien-/Hochzeitswappen als Designsystem | beobachten | reinster Designsystem-Fall, aber kleine, unquantifizierte Zielgruppe; als Upsell der Hochzeit testen |
| Abibuch mit illustrierten Porträts | beobachten | kein B2C (Komitee-Entscheidung), Minderjährige |
| JGA- und Gruppen-Merch mit Karikaturen | beobachten | virales Format, aber Commodity-Preise und KUG-Risiko |
| Golf-, Pferde-, Angel-/Jagd-Kunst | beobachten | kaufkräftige Nischen, aber DE-Nachfrage unbelegt bzw. Rechte- und Werberisiken |
| LED-Neon nach Zeichnung | beobachten | Elektro-Compliance (CE, ElektroG), Asien-Preisdruck |

Die vollständige Liste mit Belegen und Punkten steht in `longlist.md`.

---

## 5. 14-Tage-Test für Platz 1 (Kurzfassung; vollständig in `testplan.md`)

- **Angebot:** „Start“ = Designsystem + 75 Save-the-Dates mit Goldfolie; zwei Preisarme 299 € gegen 269 € (implizite Designgebühr ≈ 179 € gegen ≈ 149 €); dazu Suite 519/489 € und Hochzeitszeitung 349 €. Volle Zahlung oder verrechnete Anzahlung 49 €; kein reiner Fake-Door.
- **Landingpage:** Video „Handyfoto → Aquarell → Suite mit euren Namen“, Upload im Hero, Preisblock mit Atelier-Vergleich, KI-Kennzeichnung und Rechte-FAQ.
- **Kostenlose Vorschau:** 3 Stile + 1 Korrektur, E-Mail-Gate vor dem Reveal, Wasserzeichen, 0,25–0,50 € je Sitzung.
- **Drei Werbeangles:** „Eure Location, gezeichnet“ · „Atelier-Ergebnis ohne Atelier-Wartezeit“ · „Ein Design – von Save-the-Date bis Sitzplan“.
- **Budget:** ≈ 5.000 € (3.000 € Meta in 10 Tagen, 600 € Creatives, 200 € KI/Shop, 150 € Muster nach Freigabe, 400 € Rechtstexte und Kurzcheck, 650 € Reserve).
- **Besucher / Bestellungen:** Basis-Funnel 0,63 % Besuch→Kauf → ≈ 3.200 Besucher für **≥ 20 bezahlte Bestellungen**.
- **Max. CAC:** ≤ 150 € weiter; 151–250 € nachjustieren; > 250 € Stopp.
- **Abbruch:** ≤ 11 Bestellungen, Vorschau→Kauf < 3 %, Preisarm 299 € erreicht < 60 % der Conversion von 269 €, Vorschau-Qualität < 60 % fehlerfrei.
- **Weiterentwicklung:** nur wenn Bestellungen, CAC und Vorschau→Kauf gleichzeitig im grünen Bereich liegen. Danach Phase 2 (≈ 90 Tage): Automatisierung, Location-Partner, Folgekäufe und Reklamationen über die Einladungssaison messen.

---

## 6. Bewertung aller Shortlist-Kandidaten

| Kandidat | Punkte nach Vertiefung | Punkte nach Neuzuschnitt (Ökonomie / Markt) | Datensicherheit | Ampel | Status |
|---|---:|---|---|---|---|
| A KI-Designwelt Hochzeit | 58 | 61 / 60 | MITTEL / NIEDRIG | GELB | **Finalist 1 (bedingt)** |
| D Kinderzimmer-Stilwelt | 58 | 61 / 59 | MITTEL | GELB | **Reserve** |
| C Lebensweg-Festpaket | 53 | 54 / 60 | NIEDRIG | GELB / GRÜN | Modul von A |
| B Mehrfoto-Familienbild | 59 | 58 / 60 | NIEDRIG | GELB | verworfen |
| F Reise-Erinnerungswand | 57 | – | NIEDRIG | GELB | verworfen |
| G Hausporträt + Einzugs-Set | 57 | – | NIEDRIG | GELB | verworfen |
| I Fahrzeug-Porträt | 57 | – | MITTEL | GELB | verworfen |
| H Team-Saisonabschluss | 56 | – | NIEDRIG | GRÜN | verworfen |
| E Familienfeste-Suite | 51 | – | MITTEL | GELB | verworfen |
| J Community-Feste | 47 | – | NIEDRIG | GELB | verworfen |

Punkte: Wirtschaftlichkeit 30, Markt und Nachfrage 20, KI-Mehrwert 15, Wettbewerb 15, Produktion 10, Social/Marketing 10 (Einzelpunkte in `shortlist.md`). Die Longlist-Vorbewertung lag für dieselben Kandidaten bei 61–79 Punkten. Die Abwertung kam fast immer aus der Wirtschaftlichkeit, sobald Partnerpreise, Mehrfachversand und Prüfminuten vollständig gerechnet waren.

**Vergleichsrechnung (gleiche Annahmen, Basis; vollständig in `finanzmodell/ergebnisse.md`):**

| Kandidat | Warenkorb brutto | DB I | Realistischer CAC | DB I − CAC | Bestellungen für 1 Mio. € | Ergebnis bei 1 Mio. € |
|---|---:|---:|---:|---:|---:|---:|
| A Hochzeit – Neuzuschnitt | 417 € | 185 € | 150 € | +35 € | 3.376 | +8 Tsd. € |
| D Kinderzimmer – Neuzuschnitt | 402 € | 174 € | 155 € | +19 € | 3.193 | −106 Tsd. € |
| C Festpaket – Neuzuschnitt | 330 € | 121 € | 96 € | +25 € | 3.711 | −68 Tsd. € |
| B Mehrfoto – Neuzuschnitt | 255 € | 117 € | 102 € | +15 € | 4.983 | −88 Tsd. € |
| E Familienfeste (Vertiefung) | 328 € | 37 € | 80 € | −43 € | 3.715 | −320 Tsd. € |
| F Reise-Wand (Vertiefung) | 249 € | 57 € | 95 € | −38 € | 5.027 | −332 Tsd. € |
| G Hausporträt (Vertiefung) | 184 € | 46 € | 65 € | −19 € | 6.711 | −272 Tsd. € |
| H Team-Set (Vertiefung) | 278 € | 29 € | 110 € | −81 € | 4.424 | −482 Tsd. € |
| I Fahrzeug (Vertiefung) | 160 € | 40 € | 65 € | −25 € | 7.838 | −332 Tsd. € |
| J Community-Feste (Vertiefung) | 400 € | 8 € | 100 € | −92 € | 3.037 | −389 Tsd. € |

E bis J wurden nicht neu zugeschnitten. Ihr Abstand zwischen DB I und CAC war deutlich größer, und die Prüfer nannten zusätzliche strukturelle Hürden: Gratis-Konkurrenz (Reiseplakat), Abstimmungsaufwand mit vielen Familien (Team-Set), Stückpreisanker unter 1 € (Community-Feste) sowie Marken- und Designrechte (Fahrzeuge). Dass ein Neuzuschnitt diese Lücke nicht geschlossen hätte, ist unsere Einschätzung (ANNAHME), nicht geprüft (siehe `shortlist.md`).

---

## 7. Was über alle Kandidaten gilt

1. **POD-Druck ist gegenüber den Marktführern nicht margenfähig.** Print API verlangt 1,08 € Einkauf je Platzkarte, beim Marktführer kostet sie 0,88 € im Verkauf. Bei Tapete auf Maß verlangen Photowall und Rebel Walls 39 €/m² für ein eigenes Bild. Marge entsteht nur über eine ausgewiesene oder implizite Gestaltungsleistung (Hochzeit 179 €, Kinderzimmer 119 €).
2. **Belegt ist Zahlungsbereitschaft für Handarbeit, nicht für KI-Gestaltung einer Marke ohne Bewertungen.** Ateliers werben mit „von Hand“, und einzelne Anbieter positionieren sich ausdrücklich gegen KI (Sketchus).
3. **Preis und CAC entscheiden, KI-Kosten kaum.** Ein um 15 % niedrigerer Warenkorb bringt jedes Modell bei 1 Mio. € ins Minus. Doppelte KI-Kosten verschieben das Ergebnis nur um 20–40 Tsd. €.
4. **CAC wird regelmäßig unterschätzt.** Creative-Kosten (≈ 8–12 € je Paid-Kunde), marktübliche Partnerprovisionen (10–15 % und mehr) und Rabattcodes fehlten in den Neuzuschnitten. Die Prüfer erhöhten den CAC um 14–45 %. Zum Vergleich: Desenio (≈ 33 % vom Umsatz, eigene Ableitung) und Etsy (31,7 %, BELEGT) geben rund ein Drittel des Umsatzes für Marketing aus.
5. **Generische KI-Funktionen werden zur Gratisware.** Raumvorschau (Genroom), KI-Stilfilter (myposter) und KI-Reiseplakate (Dreamina) gibt es kostenlos. Ein Vorsprung entsteht nur über Prozess, Druckqualität, Prüfung, Designsystem und Kanäle.
6. **Premium kann trotzdem unprofitabel sein.** Papier (UK) erzielt 56 % Rohmarge bei 31,9 Mio. GBP Umsatz und schreibt dennoch 3,8 Mio. GBP operativen Verlust.

---

## 8. Recht, Produktsicherheit, Abhängigkeiten (Querschnitt; fachlich prüfen lassen)

| Thema | Kern | Quelle |
|---|---|---|
| Widerruf | Ausschluss bei personalisierten Waren wahrscheinlich (§ 312g Abs. 2 Nr. 1 BGB), auch vor Produktionsbeginn (EuGH C-529/19); Information vor Vertragsschluss (Art. 246a § 1 Abs. 3 EGBGB); Widerrufsbutton nach § 356a BGB seit 19.06.2026 für widerrufbare Teile | gesetze-im-internet.de, EUR-Lex (Vorarbeit) |
| Gewährleistung | Kaufrecht (§ 650 BGB); dokumentierte Proof-Freigabe; negative Beschaffenheitsvereinbarung nur gesondert (§ 476 BGB); Rückgriff auf Partner begrenzt (WMD: 2 Wochen Rügefrist, 1 Jahr Verjährung) | Vorarbeit, Partner-AGB |
| Fotos und Personen | Fotografenrechte (§ 72 UrhG), Recht am eigenen Bild (§ 22 KUG), Location-Fotos vom Privatgrund (BGH V ZR 45/10); Kinderfotos vermeiden (Kinderzimmer: nur Kuscheltier/Haustier) | Vorarbeit |
| Datenschutz | Gästelisten = Daten Dritter; kein automatischer Gesichtsabgleich (Art. 9 DSGVO); AV-Verträge mit KI- und Druckpartnern; Gemini bezahlte Stufe ohne Training (BELEGT 01.10.2026) | Vorarbeit, ai.google.dev |
| KI-Kennzeichnung | Art. 50 KI-VO seit 02.08.2026; Verbote nach Digital-Omnibus ab 02.12.2026 (Filter); nicht mit „handgezeichnet“ werben (§ 5a UWG) | EUR-Lex (Vorarbeit) |
| Produktsicherheit | Eigenmarke = Hersteller (GPSR Art. 13, § 4 ProdHaftG; ab 09.12.2026 RL 2024/2853); Tapete = Bauprodukt (EN 15102, CE, Emissionen); Herstellerangaben online (Art. 19 GPSR) | Vorarbeit, Partnerangaben |
| Preisangaben | Grundpreis je m² bei Tapete (§ 4 PAngV); niedrigster Preis der letzten 30 Tage bei Rabatten (§ 11 PAngV) | gesetze-im-internet.de |
| Verpackung | PPWR/VerpackDG seit 12.08.2026, LUCID-Registrierung; Rolle bei Direktversand durch Partner klären | Vorarbeit |
| Abhängigkeiten | KI-Modelle (Preis-/Versionswechsel → Master-Assets einfrieren), Druckpartner ohne API (WMD), Werbeplattformen (CPC +30 % kostet bei 1 Mio. € ≈ 105 Tsd. €) | Modell |

---

## 9. Methodik, Datenlage, Einschränkungen

**Vorgehen** (agentengestützte Webrecherche, 01.10.2026):

1. **Longlist:** 9 Segment-Scouts (Hochzeit, Baby/Taufe, Kinder, Familie/Feste, Haustiere, Wohnen, Sport/Vereine, Hobbys/Reisen, bewährte US-Kategorien ohne KI-Pflicht), eine Lückenkritik, 2 Lückensuchen (u. a. Feste der türkisch-, arabisch- und russlanddeutschen Communities, Gastgeschenke, Wappen) und eine Kuratierung. Ergebnis: 75 Rohkategorien, zusammengeführt zu 50.
2. **Shortlist:** 10 Kandidaten, je 3 unabhängige Agenten: Markt und Wettbewerb in DACH; Produktion, KI, Vorschau und Social; ein adversarialer Prüfer mit eigenen Nachprüfungen, 100-Punkte-Bewertung und vorsichtigen Modelleingaben.
3. **Neuzuschnitt:** Die vier stärksten Kandidaten wurden neu zugeschnitten, je mit 2 Gegenprüfungen (Ökonomie/CAC, Markt/Zahlungsbereitschaft) und einem übergreifenden Finalisten-Urteil.
4. **Finanzmodell:** ein gemeinsamer Rechenkern für alle Kandidaten. Die Prüfer haben ihre Zahlen damit selbst nachgerechnet.
5. **Faktencheck und Vollständigkeitsprüfung** der tragenden Aussagen dieses Berichts (Ergebnis in `rohdaten/faktencheck.json`, siehe Abschnitt 10).

**Datenlage:**

| Bereich | Datensicherheit | Begründung |
|---|---|---|
| Produktions- und Partnerpreise | MITTEL bis HOCH | viele Preise direkt aus Preisrechnern und APIs (BELEGT); Neutralversand, API und Reklamationsprozess teils nur anzufragen; keine Musterbestellung |
| Wettbewerb DE | MITTEL | Shops, Shopify-Kataloge und Trustpilot direkt geprüft; Etsy (403), Amazon (503) und Instagram (429) kaum auslesbar; Marktplatzvolumen unbekannt |
| Marktgrößen (Anlässe) | HOCH für Fallzahlen (Destatis), NIEDRIG für Ausgaben (Portal-Umfragen ohne Stichprobenangabe) | |
| Zahlungsbereitschaft für KI-Gestaltung | NIEDRIG | kein einziger belegter Kauf bei einer KI-Marke in den Finalisten-Kategorien |
| Conversion und CAC | NIEDRIG | keine DE-Primärdaten; branchenübergreifende Benchmarks (Superads, Littledata) als SCHÄTZUNG; kein Keyword-Tool, deshalb keine Suchvolumina, nur Google-Trends-Indizes |
| US-Vorbilder | MITTEL | Umsätze überwiegend ANBIETERANGABE (Minted) bzw. Gesamtunternehmen (Pottery Barn Kids); Papier UK aus Pflichtabschluss (BELEGT) |

**Einschränkungen:**

1. Keine Käufe, Registrierungen oder Kontaktaufnahmen (Vorgabe). Konditionen hinter Login oder auf Anfrage sind als „noch anzufragen“ markiert.
2. Das Suchkontingent war je Agent begrenzt (6–12 Websuchen). Viele Belege stammen aus Direktabrufen. Kleine Etsy- und Instagram-Anbieter sind deshalb unterrepräsentiert; „in DE nicht gefunden“ heißt nicht „gibt es nicht“.
3. Wechselkurse: USD-Preise teils 1:1 als EUR (vorsichtig), teils mit EZB-Kurs umgerechnet (in den Parametern vermerkt).
4. Alle ergebnisbestimmenden Modellgrößen sind ANNAHME: Preise, Mix, Vorschau→Kauf, CAC, Folgekäufe und Prüfminuten. Der Test soll sie messen. Belegt sind Partnerpreise, Wettbewerberpreise und Anlasszahlen.
5. Die Fixkosten je Umsatzstufe (26 / 95 / 170 / 720 Tsd. €) und der Gründerlohn (120 Tsd. €) sind ANNAHME.

---

## 10. Quellen

Kuratierte Kernquellen mit Datum: `quellen.md`. Alle rund 1.300 URL-Einträge aus den Rohdaten, automatisch extrahiert: `quellen-vollstaendig.md`.
