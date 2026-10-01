# KI-personalisierte Premium-POD-Produkte für Deutschland – Recherchebericht

**Recherchedatum: 01.10.2026.** Web-Quellen wurden am 01.10.2026 abgerufen (Vorarbeit aus der ersten Recherche: 30.09.2026), sofern nicht anders angegeben. Laufende Zähler (Bewertungen, Follower) gelten mit Stand des Abrufs.

**Kennzeichnung:** **BELEGT** = auf einer Primärquelle direkt geprüft (Statistik, Gesetz, öffentlicher Zähler, Preis auf der Anbieterseite). **ANBIETERANGABE** = Selbstauskunft (Größe, Kunden, Qualität). **SCHÄTZUNG** = Drittanbieter-Benchmark oder abgeleitete Zählung. **ANNAHME** = eigene Setzung. **Modellwerte** (Warenkorb, DB I, Bestellungen, Ergebnisse) sind Rechenwerte aus überwiegend ANNAHME-Eingaben (`finanzmodell/parameter.py`) und gelten insgesamt als ANNAHME. Bewertungen sind keine Bestellungen, Follower keine Käufer, Finanzierung kein Umsatz, Umsatz kein Gewinn.

**Wettbewerbsampel (Definition aus dem Auftrag):** **GRÜN** = Konkurrenz vorhanden, aber fragmentiert oder nachvollziehbare Differenzierung. **GELB** = starke Konkurrenz, Einstieg über eine Zielgruppe oder Unterkategorie denkbar. **ROT** = ein oder mehrere dominante Anbieter haben Produkt, Marke, Distribution und Personalisierungsprozess so besetzt, dass ein Neueinsteiger kaum wirtschaftlich konkurrieren kann. In der Longlist-Vorbewertung wurde ROT teils als Gesamturteil vergeben (fehlende Fertigung, Recht, zu kleiner Warenkorb); die Wettbewerbsampel im engeren Sinn gilt für die Shortlist.

**Begriffe:** POD = Print-on-Demand (Fertigung ab Stück 1 auf Bestellung); CAC = Kosten für die Gewinnung eines Neukunden; blended CAC = Durchschnitt über alle Kanäle (bezahlte Werbung, organische Reichweite, Partner); Media-CAC = nur Werbekosten; AOV = durchschnittlicher Warenkorb; DB I = Deckungsbeitrag vor Kundengewinnung; Break-even-CAC = höchster CAC, bei dem das Ergebnis noch ≥ 0 ist; Day-of = Papeterie für den Hochzeitstag (Willkommensschild, Sitzplan, Tischnummern, Menü); Upsell = Zusatzkauf; Creative = Werbevideo/-bild; Mockup = Darstellung des Entwurfs auf dem Produkt; Neutralversand/White Label = Versand ohne Logo und Preise des Druckpartners; WMD = WIRmachenDRUCK.

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
- Nach Neuzuschnitt und Gegenprüfung hat der Kandidat den **höchsten Deckungsbeitrag vor Werbung (DB I) und den höchsten tragbaren CAC**. Der Break-even-CAC bei 1 Mio. € Umsatz liegt aber nur auf Höhe des realistischen CAC (Modell ≈ 149 € gegen ≈ 150 €; Markt-Prüfer ≈ 136 € gegen 125 €) – im konservativen Szenario deutlich darunter. Rechnerisch ist er ein **Grenzfall**, die anderen Kandidaten liegen im Basisszenario klar darunter.
- Der Test klärt die Annahme, an der alle Neuzuschnitte hängen: Wird eine KI-Gestaltungsgebühr bezahlt? Scheitert sie beim stärksten Anlass, ist auch die Reserve sehr wahrscheinlich nicht tragfähig.

**Plausibler Ø-Warenkorb:** etwa **400–440 € brutto je Erstbestellung** (Basis 417 €, Modell). Je Neukunde kommen inklusive Folgephasen etwa 540 € brutto zusammen (Modell, ANNAHME).

**Deckungsbeitrag vor Werbung:** etwa **185 € je Erstbestellung (53 % vom Nettoumsatz)**, konservativ 161 €, optimistisch 199 €. Daraus folgt:

- Der maximal tragbare CAC liegt bei 185 € für die Erstbestellung und bei 227 € inklusive Folgephasen.
- Damit das Ergebnis bei 1 Mio. € Umsatz inklusive Fixkosten mindestens bei null liegt, darf ein Neukunde im Schnitt höchstens etwa 149 € kosten (bei 500.000 € Umsatz etwa 140 €; mit Gründerlohn etwa 95 €).

**Bestellungen für 1 Mio. € Jahresnettoumsatz:** etwa **3.200 pro Jahr ≈ 270 pro Monat ≈ 9 pro Tag** (im Spitzenmonat etwa 13 pro Tag), von etwa 2.200 Neukunden (Modell). Das liegt deutlich unter 10.000.

**Größte Unsicherheit:** Bezahlen Paare einer neuen, als KI gekennzeichneten Marke eine Designgebühr von etwa 150–180 €, mit welcher Vorschau→Kauf-Quote und zu welchem CAC? Belegt sind nur Käufe bei menschlichen Ateliers. Vorschau→Kauf-Quote, Set- und Folgekaufquote und CAC sind nirgends gemessen. In der Basis kostet ein Neukunde realistisch etwa 150 €. Bei 1 Mio. € Umsatz liegt das operative Ergebnis dann **bei etwa null (−1.800 € vor Gründerlohn)**, nach einem kalkulatorischen Gründerlohn von 120.000 € bei etwa −122.000 €; im Anlaufjahr eher bei −50.000 € vor Gründerlohn. Erst bei einem CAC um 100 € entsteht ein Geschäft: etwa +108.000 € vor bzw. −12.000 € nach Gründerlohn; den Gründerlohn trägt es ab etwa 95 €.

**Ehrliches Gesamturteil:** Die Recherche hat **keinen Kandidaten gefunden, der im Basisszenario ohne Bedingungen wirtschaftlich überzeugt**. Es gibt **einen bedingten Finalisten (Hochzeit)** und **eine Reserve (Kinderzimmer-Stilwelt)**. Nach der Vorgabe „nicht künstlich auf fünf auffüllen“ bleibt es bei diesen beiden. Das Muster ist über alle 10 Kandidaten gleich:

- Der Druck über POD ist gegenüber den Marktführern nicht margenfähig.
- Marge entsteht nur über eine Gestaltungsleistung.
- Deren Zahlungsbereitschaft ist für KI-Marken unbelegt.

Bevor mehr Kapital fließt, sollte der 14-Tage-Test (ca. 6.000 €, davon 4.000 € Werbung) genau diese Frage beantworten. Weil das Modell bei realistischem CAC nur auf null kommt, muss der Test **besser** sein als die vorsichtige Basisannahme, damit sich das Weitermachen lohnt.

---

## 2. Top-Finalisten

| Produkt | Zielgruppe | AOV (brutto, Basis) | Deckungsbeitrag vor CAC | Max. tragbarer CAC | Bestellungen für 1 Mio. € netto | Stärkster Wettbewerber | EU-Produktionspartner | KI-Mehrwert | Bewertung (100) | Datensicherheit |
|---|---|---:|---:|---:|---|---|---|---|---:|---|
| **Finalist 1 (bedingt): KI-Designwelt Hochzeit** | Verlobte 30–38 mit besonderer Location, 80–120 Gäste; Trauzeugen; Eltern | 417 € | 185 € (52,7 %) | 185 € Erstkauf; 227 € inkl. Folgephasen; ≈ 149 € für Ergebnis ≥ 0 bei 1 Mio. € | 3.189/Jahr · 266/Monat · 8,7/Tag | die kartenmacherei (Vorlagen-Marktführer); im Premiumsegment Ateliers (Tatengold) | WIRmachenDRUCK (DE), Onlineprinters (DE, Neutralversand belegt), Print API (NL, API) | Paar + Hund + Location → Illustration → Designsystem über 10–15 Formate; Sofortvorschau statt wochenlanger Proof-Schleifen | 60–61 | NIEDRIG–MITTEL |
| **Reserve: Kinderzimmer-Stilwelt** | Erst-Eltern (Nestbau), Eltern von 3- bis 7-Jährigen, Großeltern | 402 € | 174 € (51,4 %) | 174 € Erstkauf; ≈ 118 € für Ergebnis ≥ 0 bei 1 Mio. € | 3.193/Jahr · 266/Monat · 8,7/Tag | Photowall; Gimmersta (Rebel Walls, Hovia); myposter; Tenstickers | WIRmachenDRUCK (Vliestapete), Caspar Manufaktur (DE, Shopify-App), Printseekers (LV), Printful (Poster) | Welt aus Raumfoto + Wandmaß, Kuscheltier/Haustier als Figur, Bahnplan, Set-Übertragung | 59–61 | MITTEL |

Alle Zahlen der Tabelle sind Modellwerte (ANNAHME-Eingaben; Bewertung = Punkte der beiden Gegenprüfungen). Realistischer CAC (blended, ANNAHME auf SCHÄTZUNG-Benchmarks): Hochzeit 150 € (konservativ 215 €, optimistisch 85 €), Kinderzimmer 155 € (215 € / 110 €; Markt-Prüfer 135 €). Ergebnis bei 1 Mio. € und diesem CAC: Hochzeit −263 / **−2** / +168 Tsd. €; Kinderzimmer −437 / **−106** / +71 Tsd. € (konservativ / Basis / optimistisch, vor Gründerlohn).

**Datensicherheit:** In der Longlist bekam die Hochzeitssuite HOCH, weil Anlass, Marktgröße und Preise belegt waren. Nach der Vertiefung zählt vor allem, dass Zahlungsbereitschaft für eine KI-Designgebühr, Conversion und CAC nicht gemessen sind – deshalb NIEDRIG bis MITTEL (Ökonomie-Prüfer MITTEL, Markt-Prüfer NIEDRIG).

---

## 3. Detailanalyse (Kurzfassung; vollständig in `finalisten.md`)

### Finalist 1 (bedingt): KI-Designwelt Hochzeit

| Thema | Kern |
|---|---|
| Produktidee | Designsystem des Paares aus Fotos; Phasenverkauf: Start (Design + 75 Save-the-Dates mit Goldfolie) 299 €, Einladung 249 €, Day-of aus Hartschaum/Papier 379 €, Danke 159 €; Hochzeitszeitung 349 € (Trauzeugen); Wandbild 129 € |
| Kaufanlass | feste Fristen: Save-the-Date 8–12, Einladung 4–6, Menü/Tisch 1–2 Monate vorher; Danksagung 2–4 Wochen danach (ANBIETERANGABE) |
| Zielgruppe / Größe | 348.813 Eheschließungen 2025, niedrigster Wert seit 1950 (BELEGT); Ø Papeterie 338 € (ANBIETERANGABE); Segment ≥ 250 € ≈ 140.000 Paare (SCHÄTZUNG) |
| Bestehender Markt | Vorlagenmarkt (Suite 80 Gäste ≈ 464–563 €, SCHÄTZUNG aus BELEGT-Preisen) und Ateliermarkt (ab 690 € nur Design, BELEGT); Größenordnung ≈ 118 Mio. € (SCHÄTZUNG: Ø-Ausgabe × Eheschließungen) |
| US-Vorbilder | Minted (> 300 Mio. USD erwartet 2026, ANBIETERANGABE; KI-Funktion angekündigt, nicht gestartet), Joy/Paperlust (Suite 518 USD je Paar, ANBIETERANGABE), Papier UK als Warnung (56 % Rohmarge, 3,8 Mio. GBP operativer Verlust, BELEGT) |
| Deutsche Konkurrenz | kartenmacherei, Kartenliebe, Rosemood, CEWE, Canva Print, Ateliers, Cartalia; myprintcard insolvent; Ampel GELB |
| KI-Mehrwert | Mehrfoto-Szene + Designsystem + Sofortvorschau; Text nie aus dem Bildmodell; Schwierigkeit 4/5; KI-Kosten ≈ 10 € je Bestellung inkl. Nichtkäufer |
| Produktionspartner | WIRmachenDRUCK (Preise BELEGT; Neutralversand und API noch anzufragen), Onlineprinters (Neutralversand BELEGT), Print API (API) |
| Kosten / Preis | Einkauf je Erstbestellung Ø 108 € netto inkl. Versand; Preis Ø 417 € brutto |
| Bundle / Upsells | Phasen als Folgekäufe (0,45 je Paar, ANNAHME); Acryl +69 €, Gästebuch 69 €, Express 39 €, Korrekturrunde 49 € |
| Marketing / Creatives | Meta, Pinterest, Location-Partner, Trauzeugen-Link; Creatives: Handyfoto → Suite, Goldfolie-ASMR, Hochzeitszeitung-Reaktion; Creative-Potenzial 8/10 |
| Finanzmodell | DB I 185 €; Ergebnis bei 1 Mio. € und CAC 150 €: ≈ −2 Tsd. € vor Gründerlohn (Grenzfall), bei CAC 100 €: +108 Tsd. € |
| Risiken | unbelegte Zahlungsbereitschaft, CAC, schrumpfende Basis, Nachahmung (Minted, Marktführer), Abgriff über Vorschau, Terminware, WMD ohne API |
| Skalierbarkeit | 1 Mio. € ≈ 3.190 Bestellungen, ≈ 1,4 Vollzeitstellen Prüfung/Support; 5 Mio. € ≈ 15.900 Bestellungen, ≈ 6,8 Stellen; kritischste Stufe 500.000 € (Break-even-CAC ≈ 140 €) |

### Reserve: Kinderzimmer-Stilwelt

Wandwelt auf Maß (Gestaltung 119 € + 39 €/m²) mit Kuscheltier oder Haustier als Figur, Bahnplan und Set-Aufpreis. Der DB I ist hoch (174 €), aber die etablierten Anbieter sind schnell, günstig und kulant: Photowall und Rebel Walls nehmen 39 €/m² für ein eigenes Bild, Hovia 50 €/m² (Designteam auf Anfrage), Tenstickers bietet Namens-Kindertapeten auf Maß für ≈ 103–112 € an. Für ein Ergebnis von mindestens null bei 1 Mio. € wäre ein CAC ≤ 118 € nötig. Realistisch sind 155 € (Modell; Markt-Prüfer 135 €). Details in `finalisten.md`.

---

## 4. Was wurde verworfen?

**Nach Vertiefung bzw. Neuzuschnitt (DB I und realistischer CAC aus dem Modell, Basis):**

| Kandidat | Ergebnis | Hauptgrund |
|---|---|---|
| Mehrfoto-Familienbild (Generationen, Mensch + Tier) | verworfen nach Neuzuschnitt (58–60 Punkte) | Preisanker durch Handarbeit (Sketchus: handgezeichnetes A4 mit 5 Personen als Artprint 239,99 €, Werbung „Keine KI-Zeichnung“) und Automatik (MyPortrait: Leinwand 60×90 mit Live-Vorschau 109,95 €) (BELEGT); niedrigster Warenkorb der vier, ≈ 5.000 Bestellungen für 1 Mio. € |
| Lebensweg-Festpaket (runde Geburtstage, Jubiläen) | nur Modul (54–60 Punkte) | Marge hängt an der Auflage; korrigiert DB I ≈ 121 € gegen CAC ≈ 96 € → bei 1 Mio. € −68 Tsd. €; Vorlaufkonflikt (Bestellung ≥ 4 Wochen vor der Feier) |
| Familienfeste-Suite (Geburt, Taufe, Kommunion, Konfirmation) | verworfen (51 Punkte) | DB I ≈ 37 € gegen CAC ≈ 80 €; CEWE und kartenmacherei bieten Vorlagen-Sets; Kerze als Anker schwach (Kerzenonkel druckt hochgeladene Kundenmotive bereits 1:1 ab 47,99 € und hat ein Händlerprogramm, BELEGT) |
| Reise-Erinnerungswand | verworfen (57) | DB I ≈ 57 € gegen CAC ≈ 95 €; KI-Reiseplakat aus Urlaubsfoto ist Gratisfunktion (Dreamina); keine Kauffrist |
| Hausporträt + Einzugs-Set | verworfen (57) | DB I ≈ 46 € gegen CAC ≈ 65 €; Set-Kaufbereitschaft unbelegt; Architekturtreue der KI |
| Team-Saisonabschluss-Set | verworfen (56) | DB I ≈ 29 € (Abstimmung mit 12–16 Familien); belegter Teamanker 70–130 €; Einwilligungen aller Eltern |
| Fahrzeug-Porträt und Garagenwelt | verworfen (57) | DB I ≈ 40 € gegen CAC ≈ 65 €; sechs etablierte DE-Anbieter für 30–130 €; Marken- und Designrechte der Hersteller |
| Feste türkisch-, arabisch- und russlanddeutscher Familien | verworfen (47) | Stückpreisanker 0,10–0,63 € je Karte; Paar-Illustration menschlich ab 0,17 € je Karte; DB I ≈ 8 € |

**Vor der Vertiefung verworfen oder nur beobachtet (Longlist-Vorbewertung):**

| Kategorie | Status | Grund |
|---|---|---|
| Küchen-/Duschrückwand mit Motiv | ROT | Spezialfertigung, Maß-/Bruchrisiko, geringer KI-Mehrwert |
| Raumabgestimmte Galeriewand | beobachten | Gegenbefunde: Desenio-Umsatz in Deutschland 2025 185,3 nach 217,6 Mio. SEK (−14,8 %, BELEGT, Geschäftsbericht); Framebridge mit „significant operating losses“, 2025 höher als 2024 (BELEGT, Graham-Holdings-10-K); als Upsell-Modul |
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

- **Angebot:** „Start“ = Designsystem + 75 Save-the-Dates mit Goldfolie; zwei Preisarme 299 € gegen 269 € (implizite Designgebühr ≈ 179 € gegen ≈ 149 €); dazu Spätstart (mit Einladungen) 419/389 €, Suite 519/489 € und Hochzeitszeitung 349 €. Volle Zahlung mit Geld-zurück bis zur Proof-Freigabe; kein reiner Fake-Door.
- **Landingpage:** Video „Handyfoto → Aquarell → Suite mit euren Namen“, Upload im Kopfbereich, Preisblock mit belegtem Atelier-Vergleich, KI-Kennzeichnung und Rechte-FAQ.
- **Kostenlose Vorschau:** 3 Stile + 1 Korrektur, E-Mail-Gate vor dem Reveal, Wasserzeichen, 0,25–0,50 € je Sitzung.
- **Drei Werbeangles:** „Eure Location, gezeichnet“ · „Illustration wie vom Atelier – Vorschau sofort“ · „Ein Design – von Save-the-Date bis Sitzplan“.
- **Budget:** ≈ 6.000 € (4.000 € Meta-Werbung in 10 Tagen, 600 € Werbevideos, 200 € KI/Shop, 150 € Muster nach Freigabe, 400 € Rechtstexte und Kurzcheck, 650 € Reserve).
- **Besucher / Bestellungen:** Modell-Funnel 0,55 % Besuch→Kauf bei 1,00 € Klickpreis → ≈ 4.000 Besucher und ≈ 22 Bestellungen; **„Weiter“ erst ab ≥ 25 bezahlten Bestellungen** (besser als das Modell).
- **Max. CAC (reine Werbekosten je Bestellung):** ≤ 160 € weiter; 161–227 € nachjustieren; > 227 € Stopp.
- **Abbruch:** ≤ 17 Bestellungen, Vorschau→Kauf < 4 %, Preisarm 299 € erreicht < 50 % der Conversion von 269 €, Vorschau-Qualität < 60 % fehlerfrei.
- **Weiterentwicklung:** nur wenn Bestellungen, Media-CAC und Vorschau→Kauf gleichzeitig im Bereich „Weiter“ liegen. Danach Phase 2 (≈ 90 Tage): Automatisierung, Location-Partner, Folgekäufe und Reklamationen über die Einladungssaison messen.

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

Punkte: Wirtschaftlichkeit 30, Markt und Nachfrage 20, KI-Mehrwert 15, Wettbewerb 15, Produktion 10, Social/Marketing 10 (Einzelpunkte in `shortlist.md`). Bei „Ökonomie / Markt“ stehen die Punkte und die Datensicherheit der beiden Gegenprüfungen nebeneinander. Die Longlist-Vorbewertung lag für dieselben Kandidaten bei 60–79 Punkten. Die Abwertung kam fast immer aus der Wirtschaftlichkeit, sobald Partnerpreise, Mehrfachversand und Prüfminuten vollständig gerechnet waren.

**Vergleichsrechnung (gleiche Annahmen, Basis; vollständig in `finanzmodell/ergebnisse.md`):**

| Kandidat | Warenkorb brutto | DB I | Realistischer CAC | DB I − CAC | Bestellungen für 1 Mio. € | Ergebnis bei 1 Mio. € |
|---|---:|---:|---:|---:|---:|---:|
| A Hochzeit – Neuzuschnitt | 417 € | 185 € | 150 € | +35 € | 3.189 | −2 Tsd. € |
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

1. **POD-Druck ist gegenüber den Marktführern nicht margenfähig.** Print API verlangt 1,00 € netto Einkauf je gefalteter Tischkarte zuzüglich Handling und Versand, beim Marktführer kostet die Tischkarte 0,88 € brutto im Verkauf. Bei Tapete auf Maß verlangen Photowall und Rebel Walls 39 €/m² für ein eigenes Bild. Marge entsteht nur über eine ausgewiesene oder implizite Gestaltungsleistung (Hochzeit 179 €, Kinderzimmer 119 €).
2. **Belegt ist Zahlungsbereitschaft für Handarbeit, nicht für KI-Gestaltung einer Marke ohne Bewertungen.** Ateliers werben mit „von Hand“, und einzelne Anbieter positionieren sich ausdrücklich gegen KI (Sketchus).
3. **Conversion, Preis und CAC entscheiden, die KI-Kosten selbst kaum.** Eine um 40 % niedrigere Vorschau→Kauf-Quote erhöht den Werbe-CAC und kostet beim Finalisten bei 1 Mio. € ≈ 183 Tsd. €; ein um 15 % niedrigerer Warenkorb ≈ 127 Tsd. €. Doppelte KI-Kosten verschieben das Ergebnis nur um 27–38 Tsd. €.
4. **CAC wird regelmäßig unterschätzt.** Kosten für Werbevideos (≈ 8–12 € je über Werbung gewonnenem Kunden), marktübliche Partnerprovisionen (10–15 % und mehr) und Rabattcodes fehlten in den Neuzuschnitten; beim Finalisten fehlen die Videokosten auch nach der Korrektur. Die Prüfer erhöhten den CAC um 12–45 % (Ökonomie-Prüfer 28–45 %). Zum Vergleich: Desenio (≈ 33 % vom Umsatz, eigene Ableitung) und Etsy (31,7 %, BELEGT) geben rund ein Drittel des Umsatzes für Marketing aus.
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
| KI-Kennzeichnung | Art. 50 KI-VO seit 02.08.2026 (Kennzeichnung KI-erzeugter Inhalte); durch die Omnibus-Änderung der KI-VO gelten ab 02.12.2026 zusätzliche Verbote, die Upload-Filter (z. B. für intime Bilder realer Personen) nötig machen; nicht mit „handgezeichnet“ werben (§ 5a UWG) | EUR-Lex (Vorarbeit) |
| Produktsicherheit | Eigenmarke = Hersteller (GPSR Art. 13, § 4 ProdHaftG; ab 09.12.2026 RL 2024/2853); Tapete = Bauprodukt (EN 15102, CE, Emissionen); Herstellerangaben online (Art. 19 GPSR) | Vorarbeit, Partnerangaben |
| Preisangaben | Grundpreis je m² bei Tapete (§ 4 Abs. 1, § 5 PAngV; Ausnahme § 4 Abs. 3 Nr. 4 für Waren im Rahmen einer Dienstleistung prüfen lassen); niedrigster Preis der letzten 30 Tage bei Rabatten (§ 11 PAngV) | gesetze-im-internet.de (BELEGT) |
| Verpackung | PPWR/VerpackDG seit 12.08.2026, LUCID-Registrierung; Rolle bei Direktversand durch Partner klären | Vorarbeit |
| Abhängigkeiten | KI-Modelle (Preis-/Versionswechsel → Master-Dateien einfrieren), Druckpartner ohne API (WMD), Werbeplattformen (Klickpreis +30 % im bezahlten Anteil kostet bei 1 Mio. € ≈ 76 Tsd. €, blended CAC +30 % ≈ 99 Tsd. €) | Modell |

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
