# KI-personalisierte Print-on-Demand-Produkte für Deutschland – Recherchebericht

**Recherchedatum: 30.09.2026** (Systemdatum der Rechercheumgebung, als Erstes ermittelt). „Letzte sechs Monate“ bedeutet in diesem Bericht **April bis September 2026**. Web-Quellen wurden am 30.09.2026 abgerufen, sofern nicht anders angegeben. Laufende Zähler wie Bewertungszahlen gelten mit Stand 30.09.2026.

**Kennzeichnung:**

- **BELEGT:** auf einer Primärquelle direkt geprüfte Tatsache. Dazu zählen Gesetzestexte, Statistiken, APIs, öffentlich sichtbare Zähler sowie Preise und Produktangaben auf der Anbieterseite, diese als Beleg für das Angebot.
- **ANBIETERANGABE:** Selbstauskunft zu Leistung, Größe, Kundenzahlen, Qualität oder Produktionsort ohne unabhängige Bestätigung.
- **SCHÄTZUNG:** Drittanbieter-Benchmark oder abgeleitete Zählung.
- **ANNAHME:** eigene Setzung.

Bewertungen sind keine Bestellungen, Finanzierung ist kein Umsatz, kumulierte Zahlen sind kein Jahresumsatz.

**Ordnerinhalt:**

| Datei | Inhalt |
|---|---|
| `bericht.md` | dieser Bericht |
| `kandidaten-longlist.md` | Longlist mit 25 Nischen plus 2 aus der Nachsuche: Scores vor und nach der Vertiefung, Endstatus, vorab ausgeschlossene Rohfunde, alle 14 Nachsuche-Funde |
| `quellen.md` | kuratierte Kernquellen zu den tragenden Aussagen |
| `quellen-vollstaendig.md` | alle rund 1.360 URL-Einträge aus den Rohdaten, automatisch extrahiert |
| `finanzmodell/finanzmodell.py`, `finanzmodell/parameter.py` | Rechenmodell und Eingaben mit Quellenstatus je Parameter; Aufruf `python3 finanzmodell.py` |
| `finanzmodell/ergebnisse.md`, `.json`, `monate.csv` | erzeugte Ergebnisse: Szenarien, Break-even, Sensitivität, Monatswerte |
| `rohdaten/` | strukturierte Rohergebnisse aller Recherche-Agenten, einschließlich Faktencheck |
| `werkzeuge/` | Skripte, die Longlist und Quellenverzeichnis aus den Rohdaten erzeugen |

---

## A. Klare Empfehlung

### Zuerst testen: Haustier-Gedenkporträt „Wiedervereint“ (Finalist 1, Ampel GELB)

**Produkt:** Aus **getrennten** Fotos von Mensch und verstorbenem Haustier entsteht per KI ein Gedenkporträt im Malstil, das beide zeigt.

- **Ablauf:** Der Kunde sieht vorab eine kostenlose Vorschau. Er markiert Besonderheiten des Tiers, ein Mensch prüft sie vor dem Druck.
- **Lieferformen:** Leinwand (Kernprodukt 129 €), Einzeltier-Gedenkporträt (89 €) oder Gedenk-Set mit Leinwand, Tasse und Decke (169 €).
- **Auftritt:** deutschsprachige Gedenkmarke. Das Porträt wird als „im Malstil gestaltet, KI-gestützt“ kommuniziert, nicht als „gemalt“ (siehe F).
- **Fertigung:** EU-Print-on-Demand. Hauptpartner ist Printful (Leinwand aus Spanien, Decke und Tasse aus Lettland), Alternative Print API (Niederlande).
- **Kanalmix im Basismodell, Monat 12:** rund 24 Bestellungen aus organischer Reichweite (SEO, Pinterest, Creator-Inhalte, gegen 400 € Content pro Monat), rund 20 über Empfehlungspartner (Tierbestatter und Tierarztpraxen, 15 % Provision), rund 5 über ein kleines Werbebudget, rund 2 Wiederkäufe.

**Warum dieses Produkt, entlang der vorgegebenen Prioritäten:**

| Priorität | Finalist 1: Gedenkporträt | Stärkster Rivale: KI-Hochzeitspapeterie (Reserve) |
|---|---|---|
| 1. Einstiegschance trotz Konkurrenz | Prüfer-Score 2/5, GELB. Die Lücke „Mensch + **verstorbenes** Tier aus getrennten Fotos, Sofortvorschau, Merkmalsprüfung, Gedenk-Framing“ ist schmal, aber in keinem geprüften deutschen Shop automatisiert besetzt. Zusätzlich gibt es einen eigenen Kanal: Tierbestatter führen keine Porträts | Prüfer-Score 2/5, GELB am unteren Rand. Bastellösung ChatGPT + kartenmacherei „Eigenes Design“ ab 1,80 €/Karte; handgezeichnete Illustration ab 50 GBP |
| 2. Wirtschaftlichkeit inkl. Kundengewinnung | Prüfer 2/5. Modell Basis: DB I 44 €, Paid-CAC 56 € → Werbung unprofitabel; Monat 12 +967 € vor Unternehmerlohn nur mit Partner- und organischem Kanal; **ohne Partnerkanal** +369 € | Prüfer 2/5. Modell Basis (gleiche Kanalannahmen, ohne Partner): DB I 63 €, Monat 12 +1.656 €. Dieser Vorteil hängt aber an unbelegten Annahmen: 36 % Folgekäufe, gleiche Conversion wie beim Gedenkporträt, Paar mit zwei Entscheidern |
| 3. Nachfrage und Übertragbarkeit | Prüfer 3/5. US-Indie-Anbieter Companion Archive mit 443 Trustpilot-Bewertungen, 435 davon in 12 Monaten (BELEGT); US-Anbieter mit genau diesem Anwendungsfall (Pet Plus Us, klein und neu); 25,7 Mio. Hunde und Katzen in DE | Prüfer 2/5. **Kein** US-Anbieter mit laufender KI-Variante: Minted hat am 30.04.2026 angekündigt, bis 30.09.2026 folgte keine Startmeldung. Zahlende Kunden gibt es nur für Illustrationen von Hand |
| 4. Einzelstück und Direktversand | 4/5: EU-POD über API belegt, kein Zoll | 4/5: DE-Druckereien, Neutralversand bei Onlineprinters belegt |
| 5. KI-Beherrschbarkeit | 2/5: Identitätstreue von Mensch **und** Tier nicht garantiert | 3/5: zwei Gesichter plus Architektur, Tippfehler-Risiko |

Bei Priorität 1 herrscht Gleichstand. Bei Priorität 2 liegt die Hochzeitspapeterie **im Modell** vorn, aber nur unter Annahmen, die der Prüfer ausdrücklich angezweifelt hat. Den Ausschlag gibt Priorität 3: Für die Hochzeitspapeterie fehlt jeder Beleg zahlender Kunden für die KI-Variante. Die Vorgabe „ein älteres, nachweislich funktionierendes Modell ist besser als ein Hype ohne zahlende Kunden“ spricht deshalb für das Gedenkporträt. Hinzu kommt: Der Test ist schneller auswertbar, weil Hochzeitspaare Monate im Voraus kaufen.

**Offen gesagt: Das Wachstumskriterium ist nicht erfüllt.**

- Für April bis September 2026 gibt es keinen Beleg für einen Durchbruch. Das Bewertungstempo von Companion Archive ist eher rückläufig (SCHÄTZUNG, C.2).
- Die Empfehlung stützt sich deshalb auf ein seit Jahren funktionierendes Modell (Haustier-Gedenkporträts bei Crown & Paw und West & Willow mit jeweils über 19.000 Trustpilot-Bewertungen) und auf dessen jüngere KI-Variante mit messbarer Nachfrage seit Ende 2025.
- Den konkreten Anwendungsfall „Wiedervereint“ belegt nur ein sehr kleiner, neuer Anbieter.

**Einordnung der Zahlen** (C.7, `finanzmodell/ergebnisse.md`):

| Szenario | Monat 12 Nettoumsatz | Monat 12 operatives Ergebnis vor Ertragsteuern und Unternehmerlohn | Jahr 1 inkl. Einmalkosten | Break-even vor / nach Lohn | Kapitalbedarf bis Break-even |
|---|---:|---:|---:|---|---:|
| Vorsichtig | 1.330 € | −418 € | −10.451 € | kein Break-even in 24 Monaten | – (Abbruch) |
| **Basis** | **5.423 €** | **+967 €** | −2.004 € | Monat 6 / nicht in 24 Monaten | **7.101 €** |
| Optimistisch | 18.870 € | +3.765 € | +16.029 € | Monat 4 / Monat 8 | 6.304 € |

Im ersten Jahr ist das realistisch ein **Nebenerwerb**. Nach einem kalkulatorischen Unternehmerlohn von 2.500 € pro Monat trägt es sich nur im optimistischen Szenario, und zwar ab Monat 8.

**Kapitaltreppe (Basis):**

| Schritt | Betrag |
|---|---:|
| Test | 1.500 € |
| Aufbau nach bestandenem Test | 1.900 € |
| Anlaufverluste bis zum Kassentiefpunkt in Monat 5 | 2.661 € |
| Reserve | 1.040 € |
| **Kapitalbedarf bis Break-even** | **7.101 €** |

Nur der Test (1.500 €) liegt vorab fest; alles Weitere wird erst nach bestandenem Test freigegeben.

**Weiter, nachjustieren oder abbrechen:** Die vorab festgelegten Kriterien stehen in **einer** Tabelle in Abschnitt E.2. Sie sind aus den Basiswerten des Modells abgeleitet.

### Nur ein Finalist, weil die Belege nicht für mehr reichen

Vertieft wurden 11 Nischen: 7 in Runde 1, 4 in Runde 2. Jede hatte eine eigene Markt-, Produktions- und adversariale Gegenprüfung. Sieben kamen auf ROT, drei auf GELB ohne Finalistentauglichkeit:

- **KI-Hochzeitspapeterie:** siehe oben. Sie ist der **Reservekandidat** für einen zweiten Test, falls der Favorit scheitert, oder für einen günstigen Fake-Door-Test mit 300–800 €.
- **Personalisiertes Kartendeck:** Der DB I im Modell-Mix liegt bei ca. 9 €.
- **Handgemaltes Porträt nach KI-Entwurf:** Das ist kein POD, die KI ist austauschbar, und das Konzept wird bereits kopiert (EverPortrait).

Eine Nachsuche mit frischem Suchkontingent brachte 14 weitere US-Funde, aber keinen zusätzlichen Finalisten (H). Sie bestätigt die Richtung: Generisches „KI aufs Shirt“ wird gerade zur Gratisfunktion großer Plattformen (Printify-App in ChatGPT, Amazon), während ein enger Anlass mit schwer nachzubauendem Bildinhalt übrig bleibt.

---

## B. Vergleichstabelle

Die Monat-12-Werte stammen aus dem Rechenmodell (Basisszenario). **Nur die erste Zeile ist ein Finalist.** Die übrigen sind Vergleichsrechnungen, einheitlich mit denselben Kanalannahmen und **ohne** Partnerkanal. Die Zeile „Finalist ohne Partner“ macht den Vergleich gleichwertig. Die Prüfer-Scores sind in der Reihenfolge Einstieg/Wirtschaftlichkeit/Nachfrage/Produktion/KI angegeben, jeweils 1–5; DQ steht für Datenqualität.

| Produkt | US-Vorbild | Nachfragebelege | Stärkste Konkurrenz (DE) | Konkrete Einstiegschance | POD-Partner | Testbudget | M12-Nettoumsatz (Basis) | Operatives Ergebnis vor Lohn (Basis, M12 / Jahr 1 inkl. Einmalkosten) | Wichtigste Unsicherheit |
|---|---|---|---|---|---|---|---|---|---|
| **Finalist 1: Haustier-Gedenkporträt „Wiedervereint“** (Prüfer 2/2/3/4/2, DQ 2) | Companion Archive; Pet Plus Us (Mensch + Tier aus getrennten Fotos, seit ca. 09/2026, ANNAHME); Referenz Crown & Paw, West & Willow | Companion Archive 443 Trustpilot-Bewertungen, 435 in 12 Monaten (BELEGT), in einer Stichprobe ca. 30 % mit Gedenkbezug (SCHÄTZUNG); Pet Plus Us 11 Bewertungen, darunter Gedenkfälle (BELEGT); kein Umsatz bekannt; Tempo April–Sept. 2026 rückläufig (SCHÄTZUNG) | Pet Printed GmbH, Fürth: KI-Vorschau, Gedenkleinwand 29,95–89,95 € seit 11.09.2026, 1.385 Trustpilot-Bewertungen in 12 Monaten (BELEGT); MyPortrait; MEINFOTO; Bildmania (handgemalt Mensch + Tier ab 169 €); Selbermachen mit Gemini + CEWE | **GELB.** Schmale Lücke: automatisierte Zusammenführung Mensch + verstorbenes Tier, Merkmalsprüfung, Gedenk-Framing; eigener Tierbestatter-Kanal | Printful (Leinwand ES, Decke und Tasse LV; API; neutral); Alternative Print API (NL) | 1.500 € | 5.423 € (vorsichtig 1.330 €; optimistisch 18.870 €) | +967 € / −2.004 € | Zahlen Käufer das 2,5- bis 3-Fache des Pet-Printed-Preises? Trifft die KI Mensch **und** Tier in ≥ 80 %? Liefern Partner- und organischer Kanal? |
| Vergleich: Finalist 1 ohne Partnerkanal | wie oben | wie oben | wie oben | wie oben | wie oben | – | 3.230 € | +369 € / −5.663 € | wie oben, ohne Partnerhebel |
| Vergleich (Reserve): KI-Hochzeitspapeterie (Prüfer 2/2/2/4/3, DQ 3) | Minted (KI-Tool angekündigt 30.04.2026, nicht gestartet); Letterfest und Paperlust (Illustration von Hand) | Nur qualitativ; kein KI-Anbieter live; 348.813 Eheschließungen 2025 (Destatis, BELEGT); Ø Papeterie-Budget 338 € (Bridebook, ANBIETERANGABE) | kartenmacherei (36.166 Trustpilot-Bewertungen) mit „Eigenes Design“ ab 1,80 €/Karte; myprintcard; Canva Print mit KI | GELB am unteren Rand: Sofortvorschau einer stilgleichen Suite | WIRmachenDRUCK, Onlineprinters (DE) | 300–800 € (Fake-Door) | 8.793 € | +1.656 € / +1.877 € | Zahlungsbereitschaft für KI- statt Handillustration; Folgekaufquote ≥ 40 %; tatsächlicher CAC bei Paaren |
| Vergleich: KI-Kartendeck (Tarot, Orakel, Skat, Quartett) (Prüfer 2/2/2/3/3, DQ 2) | Tails (Paris, US-Fokus, deutsche Seite) | Nur stündlicher Anbieter-Zähler (39.388 Kunden, Stand 30.09.2026, ANBIETERANGABE); Trustpilot 2 Bewertungen | Tails (99–469 €); meinspiel (Foto-Spiele ab 16,95 €); CustomFaceCards (SE, 35–45 USD) | GELB am unteren Rand: deutsche Formate, schnelle DE-Lieferung | meinspiel Hamburg (ab 1 Stück) | – | 1.755 € | −706 € / −13.510 € | DB I im Mix ca. 9 € (70 Generierungen und 20 Min. Prüfung je Deck) |
| Vergleich: handgemaltes Porträt nach KI-Entwurf (Prüfer 2/2/2/2/3, DQ 3) | Instapainting; EverPortrait (seit Sommer 2026) | PaintYourLife ca. 1.079 Trustpilot-Bewertungen pro Jahr (SCHÄTZUNG) | Sketchus, Galleryy, Bildmania | GELB: kein POD, KI austauschbar | Malstudios in Xiamen (nicht geprüft) | – | 3.640 € | +165 € / −7.158 € | Qualitätsstreuung, 3–6 Wochen Lieferzeit, Einfuhr durch den Shop |

---

## C. Detailanalyse Finalist 1: Haustier-Gedenkporträt „Wiedervereint“

### C.1 Angebot

| Element | Vorschlag | Einkauf Printful (BELEGT, USD, 30.09.2026) | Status |
|---|---|---|---|
| Kernprodukt „Wiedervereint“ | Mensch(en) und Tier aus getrennten Fotos, Gedenkstil im Malstil (z. B. Öl, Aquarell, „Regenbogenbrücke“, Sternenhimmel); **Leinwand 20×28″ (≈ 51×71 cm)**, 129 € | Leinwand 34,95 + Versand 11,39 | Preis ANNAHME (Marktanalyse: 119–149 €) |
| Einzeltier-Gedenkporträt | Leinwand 16×20″, 89 € | 28,56 + 11,39 | ANNAHME. Preis ist kein Hebel, weil MEINFOTO ab 19,90 € und Pet Printed ab 29,95 € verkaufen |
| Gedenk-Set | Leinwand 20×28″ + Tasse 11 oz + Decke 50×60″, 169 € | 34,95 + 6,07 + 29,36; Versand in **zwei Paketen** (ES und LV): 11,39 + 7,29 + 2,05 | ANNAHME. Erhöht den Warenkorb |
| Gerahmtes Poster | **nicht** im Startsortiment: 50×70 cm kostet bei Printful 60,75 USD + ca. 21 USD Versand und hat zu wenig Marge | – | Später über Print API oder Prodigi prüfen |
| Gutschein für Trauernde | Dritte verschenken, die beschenkte Person lädt die Fotos später selbst hoch | – | ANNAHME. Pet Plus Us bietet eine Geschenkfunktion (BELEGT) |
| Qualitätsversprechen | Bis zu 3 Besonderheiten markieren (Fleck, Knickohr, Augenfarbe, Mehrzehigkeit); menschliche Prüfung; Druck erst nach Freigabe; kostenloser Neuversuch statt Rückgabe | – | Antwort auf die belegte Ähnlichkeitskritik bei den Vorbildern |
| Keine freien Prompts | Nur kuratierte Gedenkstile | – | Senkt Varianz, Kosten und Missbrauchsrisiko |

Im Modell ergibt sich der Ø Warenkorb aus dem Mix. Basis: 55 % Kern, 25 % Einzeltier, 20 % Set, ergibt 127 €. Vorsichtig: 45/45/10 % mit 10 % Rabatt, ergibt 103,50 €. Optimistisch: 50/15/35 %, ergibt 137 €. Herstell- und Versandkosten folgen dem jeweiligen Mix.

### C.2 US-Vorbild und Nachfrage

**Was Kunden kaufen:**

- **Companion Archive:** gerahmte Leinwände oder Poster des eigenen, häufig verstorbenen Tiers im Öl-, Schwarzweiß- oder Gedenkstil. Über 60 Stile, darunter „Rainbow Rest“ und „Remembrance“.
- **Pet Plus Us:** setzt Person und Tier aus getrennten Fotos zusammen, auch mit verstorbenem Tier. Im FAQ: „Do we need a photo together? – Nope. A separate photo of each person or pet works perfectly.“ (BELEGT, [Startseite](https://www.pet-plus-us.com/)).

| Beleg | Label | Quelle |
|---|---|---|
| Companion Archive: 443 Trustpilot-Bewertungen, Score 4,7, davon 435 in 12 Monaten, fast alle also seit Oktober 2025; 89 % 5 Sterne, 6 % 1 Stern | BELEGT | [Trustpilot](https://www.trustpilot.com/review/companionarchive.com) |
| Bewertungstempo nach Datumsfilter: Dez.–März ca. 50/Monat, April–Juni ca. 40–53/Monat, Juli–Sept. ca. 27–33/Monat. **Kein Durchbruch im Zeitraum** | SCHÄTZUNG (Paginierung) | [Trustpilot, Filter 6 Monate](https://www.trustpilot.com/review/companionarchive.com?date=last6months&page=2) |
| Stichprobe von 60 Bewertungen (Mai–Sept. 2026): ca. 18 erwähnen ein verstorbenes oder todkrankes Tier | SCHÄTZUNG | [Trustpilot Seite 4](https://www.trustpilot.com/review/companionarchive.com?page=4) |
| 1-Stern-Bewertung „AI makes all cats look alike“ vom 28.09.2026 (polydaktyle Katze, Korrektur abgelehnt); am selben Tag eine weitere 1-Stern-Bewertung zu Qualität und Service | BELEGT | [Trustpilot](https://www.trustpilot.com/review/companionarchive.com) |
| Preise Companion Archive: Leinwand 12×18″ 99 USD, gerahmt 145 USD, bis 595 USD; Versand nach DE, AT und CH kostenlos | BELEGT (Angebot) | [Pricing-JS](https://companionarchive.com/assets/Pricing-CpKCIQ7a.js), [Policies-JS](https://companionarchive.com/assets/Policies-CKKl9S--.js) (Stand August 2026) |
| Pet Plus Us: 11 Bewertungen vom 17. bis 26.09.2026, Score 4,4, mehrere Gedenkfälle, z. B. „took two separate pictures and combined them to make a cherished photo of me and my deceased fur baby“ (26.09.2026) | BELEGT | [Trustpilot](https://www.trustpilot.com/review/pet-plus-us.com) |
| Pet Plus Us: Rahmendruck 89 USD, Decke 99 USD, Tasse 29 USD, Sets 109/119/179 USD; „We deliver to US addresses only“ | BELEGT (Angebot) | [Keepsakes](https://www.pet-plus-us.com/keepsakes) |
| Crown & Paw: 34 Gedenkprodukte (15,99–349 USD), im Sept. 2026 neu ein Memorial-Sweatshirt; nur 58 Trustpilot-Bewertungen in 12 Monaten bei 20.194 insgesamt | BELEGT | [products.json](https://crownandpaw.com/products.json), [Trustpilot](https://www.trustpilot.com/review/crownandpaw.com) |
| West & Willow: 19.617 Trustpilot-Bewertungen, 910 in 12 Monaten; Kritik an Ähnlichkeit und Verzögerung | BELEGT | [Trustpilot](https://www.trustpilot.com/review/westandwillow.com) |
| Vergleich Zahlungsbereitschaft beim Gedenkplüsch: Cuddle Clones 247,99 USD, 354 Trustpilot-Bewertungen in 12 Monaten | BELEGT | [Trustpilot](https://www.trustpilot.com/review/cuddleclones.com) |

**Umsatz:** Für keinen dieser Anbieter gibt es belastbare Umsatz- oder Bestellzahlen. Bewertungen sind keine Bestellungen.

### C.3 Übertragbarkeit nach Deutschland

- **Basis:** 2025 lebten in Deutschland 15,7 Mio. Katzen und 10 Mio. Hunde; in 43 % der Haushalte lebt ein Heimtier (ZZF/IVH, BELEGT: [IVH](https://www.ivh-online.de/der-verband/daten-fakten/der-deutsche-heimtiermarkt.html)). Daraus ergeben sich rund 1,7–2,1 Mio. verstorbene Hunde und Katzen pro Jahr (SCHÄTZUNG, abgeleitet aus Bestand und Lebenserwartung).
- **Gedenkkultur und Infrastruktur:** ROSENGARTEN-Tierbestattung gibt über 60 Standorte und eine Fressnapf-Partnerschaft an, ANUBIS 22 Partner und 4 Krematorien (beides ANBIETERANGABE). Der Begriff „Regenbogenbrücke“ ist als Produktbegriff verbreitet.
- **Preisniveau:** Deutlich niedriger als in den USA. Pet Printed verkauft seine Gedenkleinwand für 29,95 € (30×20 cm), 44,95 € (60×40 cm) und 89,95 € (120×80 cm); MyPortrait Leinwände für 59,95–129,95 €; MEINFOTO KI-Porträts ab 4,90 € (alles BELEGT). Unser Kernprodukt zu 129 € kostet damit bei ähnlichem Format etwa das 2,5- bis 3-Fache der Pet-Printed-Gedenkleinwand. Belegte Preispunkte in dieser Höhe gibt es in DE bei Von Pfote (Leinwand 69/129/149 €, KI, ohne Mensch + Tier) und bei Handmalerei (Bildmania „Mensch und Tier“ ab 169 €).
- **KI-Skepsis:** 42 % der Bevölkerung würden lieber in einer Welt ohne KI leben (Bitkom, 26.05.2026, BELEGT). Deutsche Wettbewerber werben ausdrücklich mit „handgezeichnet statt KI“, z. B. Lineries (BELEGT). Deshalb braucht es eine offene, aber zurückhaltende KI-Kennzeichnung und ein Qualitätsversprechen statt eines KI-Versprechens.
- **Warnsignale:** Der reine deutsche Gedenkspezialist Regenbogenspuren führt im Impressum Kleinunternehmerstatus. Die Designer-Porträtmarke Nobelpfoten „schließt seine Türen“ (beides BELEGT). Das spricht für ein begrenztes oder schwer erschließbares Volumen (ANNAHME).

### C.4 Wettbewerb in Deutschland

| Anbieter | Region / Typ | Produkt und Preis | Lieferzeit | Personalisierung und Vorschau | Größe/Nachfrage | Marke und Kanäle | Stärken | Schwächen und Lücken | Bedrohung |
|---|---|---|---|---|---|---|---|---|---|
| **Pet Printed GmbH** (Fürth) | DE / Spezialist (Haustier-Personalisierer) | ca. 25 Gedenkprodukte; seit 11.09.2026 „Personalisierte Leinwand – Memorial Photo Portrait“ 29,95/44,95/89,95 €; Poster „Du & Ich & unsere Tiere“ | nicht erhoben; Versand 4,95 € | KI-Live-Vorschau; laut eigener Angabe „ohne nachträgliche Prüfung exakt gemäß der Live-Vorschau produziert“ | 9.655 Trustpilot-Bewertungen, 1.385 in 12 Monaten, Score 4,7 (BELEGT); „über 500.000 Kunden“ (ANBIETERANGABE); 121 neue Produkte April–Sept. 2026 (BELEGT) | „Made in Germany“; Kanäle nicht erhoben | Reichweite, Preis, Sortimentstempo | Keine automatisierte Zusammenführung von Mensch und **verstorbenem** Tier aus getrennten Fotos belegt; keine menschliche Merkmalsprüfung | **hoch** (kann vermutlich schnell nachrüsten, ANNAHME) |
| **MyPortrait GmbH** (Würzburg) | DE / Spezialist | Poster 29,95–59,95 €, Leinwand 59,95–129,95 €; auch „Tierportrait auf Wolken“ | 5–8 Werktage (ANBIETERANGABE) | Live-Vorschau in 30 s | Trusted Shops 4,9 bei 8.271 Bewertungen (ANBIETERANGABE); „über 50.000 Portraits“ | Shopify-Shop mit 14 Länder-Domains, Trusted Shops | Tempo, Preis, Auslandsshops | Gedenk-Motiv nur ansatzweise; keine Zusammenführung von Mensch und Tier belegt | hoch |
| **MEINFOTO** (Picanova, Köln) | DE / Großer Generalist | KI-Porträts ab 4,90 €; Leinwand ab 19,90 €, Poster ab 17,90 € (Rabattpreise) | nicht angegeben; Kritik an Verzögerungen | KI-Vorschau unbegrenzt; Fotoregel: **„Dein Haustier sollte nicht mit Menschen interagieren“** (BELEGT) | ca. 24.600 Trustpilot-Bewertungen, 3.858 in 12 Monaten (BELEGT) | große Fotodruckmarke | Preis, Reichweite | Schließt Mensch-Tier-Interaktion aus; keine Gedenkstile | mittel |
| **Von Pfote** (Wien) | DACH (AT) / Spezialist, KI | KI-Ölporträt; Leinwand 69/129/149 €, Poster 49/79 €; Versand nach AT und DE inklusive | nicht erhoben | Gratis-Vorschau ohne Anmeldung | 2 Trustpilot-Bewertungen (BELEGT) | Magazinartikel zu Regenbogenbrücke und Gedenken | Deutschsprachiger Klon von Companion Archive | Keine Zusammenführung von Mensch und Tier | mittel (zeigt Nachahmungstempo) |
| **Bildmania** | DE / funktional gleichwertig ohne KI | „Mensch und Tier malen lassen“: Ölbild aus **getrennten Fotos** ab 169 € | 20–30 Werktage | Vorschau vor dem Trocknen | nicht erhoben | eigener Shop | Echtes Gemälde | Langsam, teuer; keine Sofortvorschau | mittel (bedient die Szene bereits manuell) |
| **Companion Archive** (USA) | international / Spezialist, KI | 99–595 USD; Versand nach DE kostenlos | 5 Werktage Produktion + 2–3 Versand (ANBIETERANGABE) | kostenloses Proof vor Zahlung | siehe C.2 | Meta-Pixel und Klaviyo im Code (BELEGT), viele Landingpages | Stilvielfalt, Vorbild | Englisch, USD; Fertigungsort unklar (bei US-Fertigung seit 01.07.2026 Zoll) | mittel |
| **Turn Me Royal** (Betreiber in Litauen, US-Fokus) | EU / KI-Themenporträts | Druckpreise erst nach der Vorschau | 3–5 Werktage (ANBIETERANGABE) | KI-Vorschau in 10–20 s | 6.786 Trustpilot-Bewertungen, 271 in 12 Monaten (BELEGT) | US-Performance-Marke | Tempo | Versand nach DE nicht verifiziert; kein Gedenkangebot | gering |
| **Petsuns** (Berlin) | DE / ohne KI (Designerin) | Engel-Stil Leinwand 99,95–239,95 €, Decke 84,95–161,45 € | nicht angegeben | Entwurf per Mail oder WhatsApp | 10–218 Produktbewertungen je Stil (ANBIETERANGABE) | Shopify-Shop | Preisanker nach oben | Keine Sofortvorschau, keine Kombination Mensch + Tier | mittel |
| **Portrait-Zauber**, **Regenbogenspuren**, **MyHappyMoments** | DE / kleine Spezialisten, ohne KI oder mit Vorlagen | 18,95–105,90 € | 3–14 Tage (ANBIETERANGABE) | manuelle Entwürfe bzw. Vorlagen | klein (z. B. 20 Trustpilot-Bewertungen bei Portrait-Zauber) | Shops, teils eBay; Regenbogenspuren rankt bei Gedenkbegriffen | – | Langsam, keine Kombination Mensch + Tier | gering |
| **Etsy.de** | Marktplatz | nicht auslesbar (403) | digital teils 1–2 Werktage | manuelle Zusammenführung „Verstorbene in Bilder einfügen“ auf Deutsch (ANBIETERANGABE) | unbekannt | Etsy-Suche und Etsy Ads | Suchintention vorhanden | meist digital oder international, keine Sofortvorschau | mittel |
| **ROSENGARTEN, ANUBIS** | DE / Tierbestatter | Schiefer- und Glas-Erinnerungsbilder 55–65 € | nicht angegeben | Fotodruck, kein Porträt | >60 Standorte bzw. 22 Partner (ANBIETERANGABE) | Standortnetz, Tierärzte, Fressnapf | Kontakt im Moment des Verlusts | Keine künstlerischen Porträts → **Vertriebspartner statt Konkurrent** | gering |
| **Selbermachen:** Gemini-App + CEWE-Leinwand | funktional gleichwertig | Leinwand ab 17,99 € | CEWE-Standard | Google bewirbt genau diesen Fall: „take your photo and another of your dog to create a perfect portrait of you both“ (26.08.2025, BELEGT) | – | – | kostenlos | Druckauflösung, Merkmalstreue und Gedenkstil muss der Laie selbst leisten | mittel |
| **Produktionspartner** (Printful, Prodigi, merchOne u. a.) | Produktionspartner, beliefern Händler | – | – | – | Beispiel: MyHappyMoments bezieht über die POD-Vendoren merchOne und snapwear (BELEGT, products.json) | – | – | **Niemand hat einen Produktionsvorteil**, alle nutzen dieselben Netze | – |

Quellen: [Pet Printed Trustpilot](https://de.trustpilot.com/review/petprinted.de), [Pet Printed products.json](https://petprinted.de/products.json), [MyPortrait](https://myportrait.de/), [MEINFOTO Haustierporträt](https://www.meinfoto.de/design-geschenke/foto-in-zeichnung-umwandeln-mit-ki/haustierportraet-als-wanddeko.jsf), [MEINFOTO Trustpilot](https://de.trustpilot.com/review/meinfoto.de), [Von Pfote](https://vonpfote.at/), [Bildmania „Mensch und Tier“](https://www.bildmania.de/mensch-und-tier-malen-lassen-), [Google Gemini Blog](https://blog.google/products/gemini/updated-image-editing-model/), [CEWE Wandbilder](https://www.cewe.de/wandbilder.html), [Rosengarten-Versand Erinnerungsbilder](https://www.rosengarten-versand.de/tierandenken/erinnerungsbilder/). Alle Wettbewerber mit Belegen: `rohdaten/vertiefung-ergebnisse.json` (Nische 2).

### C.5 Einstiegschance: GELB

Der Prüfer hat die Lücke als **„teilweise bestätigt“** eingestuft.

**Warum nicht ROT:**

- Im genauen Zielsegment gibt es keine erdrückende Dominanz: automatisierte Zusammenführung von Mensch und **verstorbenem** Tier aus getrennten Fotos, Sofortvorschau, menschliche Merkmalsprüfung, Gedenk-Framing auf Deutsch.
- Pet Printed und MyPortrait bedienen den Fall bisher nicht. MEINFOTO schließt ihn aus.
- Die manuelle Handmalerei (Bildmania) ist langsam und teuer.
- Tierbestatter führen keine Porträts und lassen sich als Kanal nutzen.

**Warum nicht GRÜN:**

1. Die KI-Zusammenführung ist technisch Standard: Gemini selbst gemacht, Etsy-Handarbeit, Bildmania von Hand. Der Burggraben entsteht nur aus Service, Merkmalstreue, Gedenk-Framing und Kanal.
2. Pet Printed ist ein starker, schneller deutscher Spezialist mit Gedenkreihe und KI-Vorschau zu 30–90 € und kann nachziehen (ANNAHME). Der nötige Aufpreis (etwa das 2,5- bis 3-Fache bei ähnlichem Format) ist nicht belegt.
3. Der Kaufanlass (Tod des Tiers) lässt sich nicht gezielt bewerben. Die Meta-Werberichtlinien verbieten Anzeigen, die persönliche Eigenschaften unterstellen, etwa zur Gesundheit (vom Prüfer als BELEGT gemeldet). Anzeigen wie „Hast du deinen Hund verloren?“ sind deshalb prüfanfällig (ANNAHME). § 4a Abs. 2 Nr. 3 UWG nennt das bewusste Ausnutzen konkreter Unglückssituationen als Merkmal aggressiver Werbung ([UWG § 4a](https://www.gesetze-im-internet.de/uwg_2004/__4a.html), BELEGT).

**Was als Abgrenzung trägt:** Bloße Übersetzung und „bessere Werbung“ reichen nicht.

| Abgrenzung | Warum plausibel | Offen |
|---|---|---|
| „Wiedervereint“ aus getrennten Fotos als Kernprodukt | In DE nicht automatisiert angeboten; US-Anwendungsfall belegt (Pet Plus Us) | Akzeptanzquote der KI; Nachahmung |
| Menschliche Merkmalsprüfung und Freigabe vor dem Druck | Ähnlichkeitskritik ist das wiederkehrende Problem der Vorbilder; Pet Printed druckt nach eigener Angabe ohne Prüfung | ca. 5,50 €/Bestellung; skaliert nur mit Automatik |
| Empfehlungspartner (Tierbestatter, Krematorien, Tierärzte) | Erreicht Kunden im Moment des Verlusts ohne sensible Anzeigen; Partner haben keine Porträts | Bereitschaft, Provision, Einlösequote; UWG-konforme Form; Berufsrecht der Tierärzte (F) |
| Gutschein für Trauernde von Dritten | Erweitert die bewerbbare Zielgruppe auf Freunde und Familie, dann ohne Trauer-Targeting | Anteil der Geschenkkäufe unbekannt |

### C.6 Produktion und KI-Pipeline

**Prüfmatrix Produktionspartner:**

| Prüfpunkt | Printful (Hauptpartner) | Status | Print API, Groningen (Alternative) | Status |
|---|---|---|---|---|
| Produktionsstandort | Laut Katalog-API Leinwand in EU_ES (Sant Climent de Llobregat bei Barcelona); Decke und Tasse in EU_LV (Riga). Einige Varianten nur außerhalb der EU; diese nicht anbieten | API: **auf der Website bestätigt**; tatsächliches Routing einer DE-Bestellung: **per Muster prüfen** | „onze drukkerij“ Groningen | **beworben, nicht geprüft** |
| Einzelstück ohne Lager | ja | auf der Website bestätigt | ja, keine Grundgebühr | beworben, nicht geprüft |
| Individuelle Datei je Bestellung | ja (JPG/PNG, sRGB, bis 100 MB) | auf der Website bestätigt | ja (Datei-URL oder POST; nur Maßprüfung, falsches Seitenverhältnis wird beschnitten) | beworben, nicht geprüft |
| Direktversand an Endkunden | ja; Produkte aus verschiedenen Werken kommen in getrennten Paketen | auf der Website bestätigt | ja | beworben, nicht geprüft |
| Neutral / Branding | neutral; Packing Slip mit eigener Nachricht und Logo; Einleger 0,45 € + mind. 22 €/Monat Lager | beworben, nicht geprüft; Postanschrift auf dem Packing Slip (GPSR): **noch anzufragen** | neutraler Karton, Logo auf dem Lieferschein | beworben, nicht geprüft |
| Rücksendeadresse / Retouren | Standard: Printful-Werk; unzustellbare Retouren werden nach 30 Tagen gespendet; bei eigener Rücksendeadresse haftet der Händler für Retouren | auf der Website bestätigt | nicht angegeben | **noch anzufragen** |
| Anbindung | Shopify, WooCommerce, REST-API; Mockup-API vorhanden | auf der Website bestätigt | REST-API mit Testumgebung; keine Shopify-App gefunden | beworben, nicht geprüft / Shopify: noch anzufragen |
| Manuelle Übergabe (Testphase) | Bestellung im Dashboard, ca. 3–5 Min. (ANNAHME) | beworben, nicht geprüft | ob das Portal Einzelbestellungen erlaubt, ist offen | noch anzufragen |
| Materialien, Größen, Grenzen | Leinwand Poly-Baumwolle 344 g/m², 3,18-cm-Keilrahmen, 6×6″ bis 40×60″; Decke 100 % Polyester, „flame retardant“; Tasse Keramik 11/15/20 oz; Auflösung: 300 DPI empfohlen, bei großen Formaten 120–150 DPI | auf der Website bestätigt (API-Beschreibungen) | Leinwand 100 % Baumwolle auf 2-cm-Rahmen, 11 Größen 20×20 bis 90×60 cm (kein 50×70); Tasse 330 ml, Druckfläche 198×98 mm; keine Decken; 150–300 DPI | beworben, nicht geprüft |
| Zeiten | Fulfillment im Schnitt 2–5 Werktage; Versand ES/LV→DE nicht veröffentlicht | auf der Website bestätigt / Laufzeit: per Muster messen | 1 Werktag Produktion + 1–3 Tage Zustellung nach DE (Kalkulator) | auf der Website bestätigt (Kalkulator) |
| Einkaufspreise (netto) | Leinwand 20×28″ 34,95 USD, 16×20″ 28,56 USD; Tasse 11 oz 6,07 USD; Decke 50×60″ 29,36 USD. **EUR-Preise nur im Dashboard** (Risiko: gleiche Zahlenwerte in EUR, +15 %) | USD: auf der Website bestätigt (API; 20×28″ im Faktencheck verifiziert); EUR: **noch anzufragen** | Leinwand 40×60 cm 16,21 €, 60×90 cm 27,02 € + Handling 1,50 €; Tasse 4,95 € | auf der Website bestätigt (Preisliste) |
| Versand je Artikel nach DE | Leinwand M 11,39 USD (+10,99 je weiteres Stück); Tasse 5,39 USD (+2,05); Decke 7,29 USD (+2,40); Poster M 6,89 USD | auf der Website bestätigt (USD) | 6,25 € je Sendung (ob netto, unklar) | auf der Website bestätigt |
| Reklamation / Nachdruck | Fehldruck, Schaden oder Defekt binnen 30 Tagen nach Erhalt: Nachdruck oder Erstattung ohne Rücksendung; keine Erstattung bei Nichtgefallen | auf der Website bestätigt | 2 Wochen Rügefrist; nur Neudruck; Dateiqualität trägt der Kunde | beworben, nicht geprüft (AGB) |

Quellen: [Printful-Katalog-API Leinwand](https://api.printful.com/products/3), [Printful Versand](https://www.printful.com/shipping), [Printful Returns](https://www.printful.com/policies/returns), [Printful Branding-Tools](https://www.printful.com/blog/printful-branding-tools), [Print API Leinwand](https://www.printapi.nl/drukwerk/canvas), [Print-API-Kalkulator](https://www.printapi.nl/shipping-quote?productId=canvas_40x60&pageCount=1&quantity=1&country=DE), [Print API AGB](https://www.printapi.nl/voorwaarden). Gewebte oder bestickte Decken haben keinen EU-Weg, nur die bedruckte Decke aus Lettland. Prodigi (Venlo), Gelato (Fertigung in DE beworben) und Posterflow (Mannheim) sind weitere Alternativen; ihre Preise gibt es nur nach Login oder per E-Mail (**noch anzufragen**).

**Vom KI-Entwurf zur Produktionsdatei** (Produktionsanalyse; Modellpreise BELEGT, Mengen ANNAHME):

1. **Upload:** 1–3 Personen- und 1–4 Tierfotos. Dazu Rechte- und Einwilligungs-Checkbox, EXIF-Daten entfernen, Speicherung in der EU mit Löschfrist.
2. **Automatische Fotoprüfung:** Schärfe, erkannte Personen und Tiere, Hinweis bei Minderjährigen.
3. **Merkmalsliste:** Der Kunde markiert Besonderheiten, ein Vision-Modell ergänzt die Beschreibung.
4. **Komposition** mit Gemini 3.1 Flash Image: bis 14 Referenzbilder, 2K zu 0,101 USD/Bild (BELEGT). Qualitätsoption ist Gemini 3 Pro Image, Alternativen sind FLUX.2 (BFL, Freiburg) und gpt-image-2.
5. **Automatische Ähnlichkeitsprüfung** beim Tier per Vision-Modell und Bild-Embedding. Beim Menschen bewusst **keine** Gesichtserkennungs-Embeddings (Art. 9 DSGVO).
6. **Produktionsdatei:** Das freigegebene Bild wird **nicht neu generiert**. Es wird nur nicht-generativ hochskaliert (Topaz, 0,05 USD). Name und Lebensdaten kommen als Schrift-Overlay dazu, der Zuschnitt folgt der Variante: Leinwand-Wrap, Henkel bei der Tasse.
7. **Vorschau aus der Produktionsdatei:** Mockups und 100-%-Detailansicht entstehen aus genau der Datei, die gedruckt wird. Die Freigabe wird mit einem Hash gespeichert.
8. **Manueller Proof:** in der Testphase bei jeder Bestellung, später nur markierte Fälle und Stichproben.
9. **Übergabe an die Produktion:** in der Testphase manuell, später per API.

**KI-Kosten je Bestellung:**

- Die Produktionsanalyse kommt auf ca. 2,38 € (Spanne 1,40–3,30 €). Sie rechnet mit 15 % Vorschau→Kauf.
- Das Modell setzt 3,91 € an (Basis), weil es mit 8 % Vorschau→Kauf rechnet. Damit entfallen mehr Nichtkäufer-Vorschauen auf jede Bestellung.

**Manueller Prüfaufwand:**

- in der Testphase 10–20 Minuten je Bestellung
- ab ca. 50 Bestellungen pro Monat 3–6 Minuten (ANNAHME)
- im Modell als Jahresmittel 10 Minuten Prüfung plus 5 Minuten Support

**Die eigentliche Herstellbarkeitslücke ist die Identitätstreue, nicht der Druck.** Eine schöne Vorschau kann das falsche Tier zeigen. Typische Fehler:

- asymmetrische Flecken, Augenfarbe, Mehrzehigkeit
- falsche Größenverhältnisse zwischen Mensch und Tier
- schlechte Einzelfotos verstorbener Tiere
- matschiger Druck dunkler Gedenkstile (beim US-Vorbild als 1-Stern-Bewertung belegt)
- Sicherheitsfilter der Modelle bei Kinderfotos

### C.7 Zahlen (Rechenmodell)

**Modelllogik** (Skript `finanzmodell/finanzmodell.py`, Eingaben mit Quellenstatus in `finanzmodell/parameter.py`):

- **Bestellungen** ergeben sich aus Besuchen, Gestaltungsstarts (KI-Vorschau) und Bestellungen, getrennt nach drei Kanälen:
  - bezahlte Besuche: Budget geteilt durch CPC
  - organische Besuche: lineare Rampe bis zur Obergrenze in Monat 12, **nur gegen laufende Content-Kosten**
  - Partnerbestellungen: Rampe ab dem Startmonat, **15 % Provision** als variable Kosten
- **Werbeausgaben** werden genau einmal gebucht; CAC ist eine abgeleitete Kennzahl. War Paid im Vormonat unprofitabel, fährt das Modell das Budget auf ein Restbudget zurück, wie es ein Betreiber tun würde.
- **Prüf- und Supportzeit** wird als Fremdleistung zu 22 €/h bewertet. Der kalkulatorische Unternehmerlohn von 2.500 €/Monat deckt Leitung, Marketing und Entwicklung, damit nichts doppelt gezählt wird.
- **Ergebnisbegriffe:** „Operatives Ergebnis“ bedeutet vor Ertragsteuern und vor Unternehmerlohn.
- **Einmalkosten in Monat 0** = Test (1.500 €) + Aufbau nach dem Test (1.900 €).

**Stückrechnung je Bestellung (netto, €):**

| Position | Vorsichtig | Basis | Optimistisch |
|---|---:|---:|---:|
| Verkaufspreis brutto (Ø Warenkorb aus Mix) | 103,50 | 127,00 | 137,00 |
| Umsatz netto (19 % USt) | 86,97 | 106,72 | 115,13 |
| Herstellung (Printful, Mix) | 31,05 | 34,78 | 39,54 |
| Versand an Kunden (Mix, Set in zwei Paketen) | 10,18 | 11,40 | 12,96 |
| Beilage (Einleger-Gebühr + Gedenkkarte) | 1,00 | 1,00 | 1,00 |
| Zahlungsgebühr (Mix Stripe/PayPal/Klarna) | 2,35 | 2,82 | 3,02 |
| KI-Vorschau der Käufer | 0,95 | 0,73 | 0,73 |
| KI-Vorschau der Nichtkäufer (umgelegt) | 5,56 | 3,14 | 2,76 |
| KI-Upscaling für die Produktionsdatei | 0,04 | 0,04 | 0,04 |
| Prüfung und Support (15 Min. × 22 €/h) | 5,50 | 5,50 | 5,50 |
| Nachdrucke und Erstattungen (Erwartungswert) | 3,47 | 2,85 | 2,52 |
| **DB I je Webbestellung = maximal tragbare Kosten pro Erstkauf** | **26,88** | **44,47** | **47,05** |
| DB I je Partnerbestellung (nach 15 % Provision) | 19,39 | 31,60 | 32,54 |
| Maximal tragbare CAC inkl. erwarteter Wiederkäufe in 12 Monaten | 27,85 | 47,13 | 51,56 |

**Szenarien (Monat 3 / Monat 6 / Monat 12 / Jahr 1):**

| Kennzahl | Vorsichtig | Basis | Optimistisch |
|---|---|---|---|
| Kanalannahmen | CPC 1,10 €; Start 15 %, Kauf 6 % (0,9 % der Besuche); organisch bis 600/Monat; Partner ab Monat 5 bis 8/Monat | CPC 0,90 €; Start 20 %, Kauf 8 % (1,6 %); organisch bis 1.500/Monat; Partner ab Monat 4 bis 20/Monat | CPC 0,80 €; Start 22 %, Kauf 9 % (2,0 %); organisch bis 3.000/Monat; Partner ab Monat 3 bis 35/Monat |
| Bestellungen | 3 / 7 / 15 / 99 | 10 / 28 / 51 / 353 | 28 / 94 / 164 / 1.143 |
| Umsatz brutto | 269 / 730 / 1.582 / 10.281 | 1.257 / 3.511 / 6.454 / 44.786 | 3.887 / 12.909 / 22.455 / 156.517 |
| **Umsatz netto** | 226 / 613 / 1.330 / 8.639 | 1.056 / 2.951 / **5.423** / 37.635 | 3.267 / 10.848 / 18.870 / 131.527 |
| DB I gesamt (nach variablen Kosten inkl. Provision) | 68 / 170 / 352 / 2.329 | 435 / 1.102 / 2.007 / 13.996 | 1.244 / 4.099 / 7.225 / 49.989 |
| Marketing (Werbung + Content + Partnerpflege) | 450 / 490 / 490 / 6.020 | 700 / 760 / 760 / 9.240 | 1.080 / 2.280 / 3.180 / 27.200 |
| DB II nach Kundengewinnung | −382 / −320 / −138 / −3.691 | −265 / 342 / 1.247 / 4.756 | 164 / 1.819 / 4.045 / 22.789 |
| Fixkosten | 280 je Monat / 3.360 | 280 je Monat / 3.360 | 280 je Monat / 3.360 |
| **Operatives Ergebnis vor Ertragsteuern und Unternehmerlohn** | −662 / −600 / −418 / −7.051 | −545 / 62 / **967** / 1.396 | −116 / 1.539 / 3.765 / 19.429 |
| … Jahr 1 inkl. Einmalkosten (3.400 €) | −10.451 | −2.004 | 16.029 |
| Ergebnis nach kalkulatorischem Unternehmerlohn | −3.162 / −3.100 / −2.918 / −37.051 | −3.045 / −2.438 / −1.533 / −28.604 | −2.616 / −961 / 1.265 / −10.571 |
| Paid-CAC (Werbung / bezahlte Neukunden) | 141 / 122 / 122 | 65 / 56 / 56 | 45 / 40 / 40 |
| Prüf- und Supportstunden pro Monat | 0,7 / 1,8 / 3,8 | 2,5 / 6,9 / 12,7 | 7 / 24 / 41 |

**Fixkosten** 280 €/Monat (ANNAHME auf Basis der Kostenbenchmarks):

- Shopify ca. 36 €
- Hosting und Speicher ca. 20 €
- Rechtstexte 9,90 € (BELEGT)
- Buchhaltung 21,90 € (BELEGT)
- Versicherung ca. 30 €
- Steuerberatung ca. 80 €
- Tools ca. 40 €
- Einlegerlager bei Printful 22 €
- Verpackungslizenz ca. 3 €
- Domain und Mail ca. 10 €

**Break-even und Kapital:**

| Kennzahl | Vorsichtig | Basis | Optimistisch |
|---|---:|---:|---:|
| Break-even-Bestellungen pro Monat (Fixkosten + Marketing von M12 durch DB I gedeckt, vor Lohn) | 29 | 23 | 74 |
| … nach Unternehmerlohn | 122 | 80 | 127 |
| … wenn nur über Paid gewachsen wird: Fixkosten / (DB I − Paid-CAC) | ∞ (Paid-CAC > DB I) | ∞ | 42 |
| Erster Monat mit operativem Ergebnis ≥ 0 (vor / nach Lohn) | – / – | 6 / nicht in 24 Monaten | 4 / 8 |
| Kassentiefpunkt (inkl. Einmalkosten) | −15.348 (Monat 24) | −6.061 (Monat 5) | −4.944 |
| **Kapitalbedarf bis Break-even** = Tiefpunkt + Reserve (Fixkosten + Marketing im Monat des Tiefpunkts) | kein Break-even (16.118 bis Monat 24) → **Abbruch** | **7.101** | 6.304 |

Die Break-even-Menge steigt mit dem Marketingbudget. Deshalb liegt sie im optimistischen Szenario höher als in der Basis.

**Testbudget, Aufbau und Liquidität, getrennt ausgewiesen (Basis):**

| Stufe | Betrag | Inhalt |
|---|---:|---|
| 1. Testbudget (14 Tage) | 1.500 € | siehe E.1 |
| 2. Aufbau nach bestandenem Test | 1.900 € | Rechtsprüfung 700 €, Marke DPMA 290 € (optional), Branding und Produktfotos 300 €, Start-Content 250 €, Partnermaterial 200 €, weitere Formatmuster 100 €, Tools 60 €; ohne Doppelung mit dem Test |
| 3. Anlaufverluste bis zum Kassentiefpunkt (Monat 5) | 2.661 € | Modell Basis |
| 4. Liquiditätsreserve | 1.040 € | Fixkosten + Marketing eines Monats |
| **Summe Kapitalbedarf bis Break-even** | **7.101 €** | Das liegt über den 5.000 € Testbudget; die Stufen 2–4 werden erst nach bestandenem Test freigegeben |

Kunden zahlen bei der Bestellung, Printful belastet bei der Auftragsübergabe. Pro Bestellung fällt deshalb kaum Vorfinanzierung an. Zahlungsanbieter können bei neuen Händlern Auszahlungen zurückhalten; dafür ist die Reserve gedacht (ANNAHME).

**Sensitivität:** Jeweils ein Parameter wird verändert. Die vollständigen Tabellen für Basis **und** optimistisches Szenario stehen in `ergebnisse.md`.

| Variante | Basis: Ergebnis vor Lohn M12 / Jahr 1 inkl. Einmalkosten / Break-even-Monat | Optimistisch: Ergebnis vor Lohn M12 / Jahr 1 / Break-even-Monat nach Lohn |
|---|---|---|
| Referenz | 967 / −2.004 / 6 | 3.765 / 16.029 / 8 |
| Werbung 50 % teurer | 883 / −2.956 / 7 | 3.132 / 11.320 / 10 |
| Conversion 30 % niedriger | 532 / −5.173 / 8 | 2.209 / 5.509 / 21 |
| Doppelte KI-Generierungen | 838 / −2.970 / 7 | 3.303 / 12.692 / 10 |
| Dreifache KI-Generierungen | 709 / −3.937 / 7 | 2.760 / 9.283 / 11 |
| Doppelte Reklamations- und Erstattungsquote | 822 / −3.007 / 7 | 3.344 / 13.007 / 10 |
| Warenkorb −17 % | 115 / −7.942 / 11 | 1.291 / −1.131 / > 24 |
| Herstell- und Versandkosten +15 % (Printful-EUR-Risiko) | 603 / −4.532 / 7 | 2.415 / 6.907 / 15 |
| Partnerkanal nur halb so stark | 638 / −4.103 / 7 | 3.150 / 11.579 / 10 |
| Organische Reichweite nur halb so stark | 418 / −5.473 / 8 | 2.303 / 6.799 / 16 |
| Kombiniert: CPC ×1,5, Conversion −30 %, Reklamation ×2 | 360 / −6.589 / 8 | 1.878 / 2.658 / > 24 |

**Lesart:**

- **Warenkorb und Herstellkosten** sind die stärksten Hebel. 17 % weniger Warenkorb halbieren den DB I fast und schieben den Break-even in Monat 11. Deshalb prüft der Test ausdrücklich den Preis.
- **Im Basisszenario** wirken teurere Klicks nur schwach, weil Paid dort schon unprofitabel ist und das Modell die Werbung auf ein Restbudget zurückfährt. Das ist eine Folge dieser Modellregel, kein Hinweis auf geringes Werberisiko.
- **Im optimistischen Szenario**, das von bezahlter Werbung lebt, wirken CPC und Conversion deutlich: Der Break-even nach Lohn verschiebt sich um 2–13 Monate.
- **Mehr KI-Generierungen und mehr Reklamationen** kosten weniger, als man denkt. Sprünge in der optimistischen Tabelle entstehen, wenn Paid unter die Profitabilitätsschwelle fällt und das Budget gedrosselt wird.

### C.8 Produktspezifische Rechtspunkte

Den vollständigen Querschnitt enthält F.

- **Widerrufsrecht:** Für Porträts, die aus Kundenfoto und -wunsch individuell erzeugt werden, ist es wahrscheinlich ausgeschlossen (§ 312g Abs. 2 Nr. 1 BGB). Gutscheine und etwaiges Standardzubehör bleiben widerrufbar. Nötig sind daher eine gemischte Belehrung und die Widerrufsfunktion nach § 356a BGB, die seit 19.06.2026 gilt. **Vor dem Live-Test fachlich prüfen.**
- **KI-VO Art. 50** (anwendbar seit 02.08.2026): Ein realistisches Bild einer realen Person mit verstorbenem Tier könnte als Deepfake nach Abs. 4 gelten; bei erkennbar künstlerischem Stil genügt wohl eine zurückhaltende Offenlegung. **Fachlich prüfen.** Filter für Kinderfotos sind **dringend empfohlen**, weil ab 02.12.2026 die neuen Verbote nach der Omnibus-VO 2026/1744 gelten; den Umfang fachlich prüfen.
- **Irreführung (§ 5 UWG):** Ein KI-Druck darf nicht als „gemalt“ oder „vom Künstler“ beworben werden. Das wiegt umso schwerer, weil Wettbewerber mit echter Handmalerei werben.
- **DSGVO und KUG:** Personenfotos, auch von Dritten und Kindern, erfordern Einwilligung bzw. Rechtsgrundlage, Datenschutzhinweise zur KI-Verarbeitung, AV-Verträge mit Google (Gemini API, im EWR nur Paid Services zulässig) und Printful, ein Löschkonzept und den Verzicht auf Gesichts-Embeddings. Ob die Einzelanfertigung für den Besteller ein „Verbreiten“ nach § 22 KUG ist, ist fraglich (ANNAHME); die DSGVO gilt in jedem Fall.
- **UWG § 4a und Tierärzte:** Keine Ansprache, die eine konkrete Trauersituation ausnutzt. Ob Tierärzte Provisionen für Empfehlungen annehmen dürfen, regeln die Berufsordnungen der Landestierärztekammern. **Prüfen.**
- **GPSR und ProdSG:** Mit Eigenmarke gilt der Shop als Hersteller: Risikoanalyse, Herstellerangaben mit Postanschrift (Packing Slip oder Beilage), Sicherheitshinweise auf Deutsch.
- **Tasse und Decke:**
  - Tasse: Lebensmittelkontaktrecht (VO 1935/2004, Keramik-RL), Konformitätserklärung beim Partner anfordern.
  - Decke: Faserangabe (VO 1007/2011); REACH-Auskunft wegen „flame retardant“ einholen.
- **Verpackung:** PPWR und VerpackDG gelten seit 12.08.2026. Die Rolle beim Versand durch Partner aus ES, LV oder NL ist **zu klären**.

### C.9 Risiken und stärkste Gegenargumente

Aus der adversarialen Prüfung, mit Modellzahlen:

1. **Die KI-Kernfunktion ist Standard und für Kunden kostenlos** (Gemini-App plus CEWE-Leinwand ab 17,99 €). Es bleibt nur ein Service-Burggraben. In den USA wandert inzwischen auch die Bestellung in den KI-Assistenten (Printify-App in ChatGPT seit April/Mai 2026, nur US; H). Kommt so etwas nach DE, wird das Selbermachen noch einfacher.
2. **Pet Printed** kann die Funktion schnell nachrüsten und verkauft Gedenkleinwände bereits für 30–90 €. Unser Kernpreis liegt bei ähnlichem Format beim 2,5- bis 3-Fachen. Dass Kunden das zahlen, ist unbelegt.
3. **Paid-Marketing trägt sich im Basisszenario nicht:** DB I 44,47 € gegenüber 56 € Paid-CAC. Der Meta-Median für Deutschland liegt bei 63,1 Kosten pro Kauf (Superads, branchenübergreifend, SCHÄTZUNG, Währung nicht angegeben). Ohne Partner- und organische Kanäle erreicht das Basisszenario in Monat 12 nur +369 € (Vergleichszeile in B).
4. **Der Nachfragebeleg für „Wiedervereint“ ist dünn:** Gedenkfälle bei einem US-Startup mit 11 Bewertungen aus 10 Tagen, vermutlich eingeladene Startbewertungen (ANNAHME). Für Deutschland gibt es weder Suchvolumen noch Etsy- oder Amazon-Daten.
5. **Qualitätsrisiko:** Gesichter **und** Tiermerkmale müssen stimmen. Kulanz im Trauerfall ist teuer, und die Prüfzeit begrenzt die Kapazität.
6. **Kanal über Tierbestatter:** zersplittert; die großen Tierbestatter betreiben eigene Gedenkshops mit eigenem Margeninteresse; lange Vertriebszyklen; Grenzen durch UWG und Berufsrecht.
7. **Printful-EUR-Preise:** Rechnet Printful in EUR mit denselben Zahlenwerten wie in USD, fällt der DB I in der Basis auf 37,30 €.

**Was stimmen müsste:**

- ≥ 80 % Akzeptanz von Mensch **und** Tier bei ≤ 10 Generierungen
- Ø Warenkorb ≥ 120 €
- ≥ 30–40 % der Bestellungen aus Partner- und organischen Kanälen, also ohne Werbeausgaben, aber mit Content- und Provisionskosten
- Reklamationen ≤ 7 %
- Pet Printed, MyPortrait und MEINFOTO ziehen innerhalb von 6–12 Monaten nicht nach, oder der eigene Qualitätsvorsprung trägt einen deutlichen Aufpreis

---

## D. Ausschlussliste

**Vertieft und verworfen** (je Nische Markt-, Produktions- und Gegenprüfung; Details in `rohdaten/vertiefung-ergebnisse*.json`):

| Nische | Ampel | Hauptgrund | Schlüsselbeleg |
|---|---|---|---|
| **KI-Hochzeitspapeterie** (Illustration von Location und Paar als stilgleiche Suite) | GELB, kein Finalist → **Reservekandidat** | Kein US-Anbieter mit laufender KI-Variante. Minted kündigte am 30.04.2026 an (BELEGT, Pressemitteilung); laut Fast Company vom 29.05.2026 war das Tool nicht gestartet (bei der Nachprüfung 403, nicht erneut verifizierbar). Im Minted-Pressroom gibt es nach dem 30.04.2026 keine Startmeldung (BELEGT). Weitere Gründe: Bastellösung ChatGPT + kartenmacherei „Eigenes Design“ ab 1,80 €/Karte; handgezeichnete Festpreis-Illustration ab 50 GBP (Letterfest); 348.813 Eheschließungen 2025. Die Modellwirtschaft ist die beste der Vergleichsrechnungen, hängt aber an unbelegten Folgekäufen | [Minted-Pressroom](https://www.minted.com/lp/press-room); [kartenmacherei „Eigenes Design“](https://www.kartenmacherei.de/p/hochzeitseinladung-eigenes-design.html); [Destatis](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Eheschliessungen-Ehescheidungen-Lebenspartnerschaften/_inhalt.html) |
| **Personalisiertes KI-Kartendeck** (Tarot, Orakel, Skat, Quartett) | GELB, kein Finalist | Der Prüfer rechnet für Tarot mit ca. 21–31 € DB vor Arbeitszeit, für Skat und Quartett mit ca. 8–14 €. Im Modell-Mix (Ø 69 €, 70 Generierungen, 20 Min. Prüfung) bleiben 8,93 €. Tails bedient das Premiumsegment in DE; CustomFaceCards (SE) verkauft KI-Spielkarten ab 35 USD. Stärke: meinspiel Hamburg druckt ab 1 Stück | [Tails DE](https://tailscards.com/de/tarot); [meinspiel](https://www.meinspiel.de/tarotkarten-komplett-individuell-gestalten-drucken/); [CustomFaceCards](https://customfacecards.com/) |
| **Handgemaltes Porträt nach KI-Entwurf** | GELB, kein Finalist | Kein POD: Studios in Xiamen ungeprüft, Einfuhr durch den Shop, 3–6 Wochen. KI als austauschbare Verkaufshilfe; EverPortrait setzt das Konzept seit Sommer 2026 um; Bildmania bietet „Mensch und Tier“ bereits handgemalt | [EverPortrait](https://everportrait.com) |
| **Foto zu 3D-Vollfarbfigur** (Mini-Me, Haustier, Tortenfigur) | ROT | Stärkster Burggraben (echte 3D-Datei), aber EU-Vollfarbdruck kostet ca. 95–107 € netto je 10-cm-Figur (Craftcloud-API, BELEGT). Meshy verkauft dieselbe Leistung nach DE ab 34 USD; laut Shop-Seite fallen Versandkosten an, Abonnenten erhalten Versandgutscheine. Für Tortenfiguren gilt Lebensmittelkontaktrecht | [Meshy Shop](https://www.meshy.ai/shop) |
| **3D-Kristall-Innengravur mit KI-Szene** | ROT | Reifer DE-Markt mit Eigenfertigern (LOOXIS seit 1999 ab 69 €, glasfoto.com, Personello ab 29,95 €); KI-Komposition austauschbar; exakte Vorschau vor der Bestellung nicht lieferbar | [LOOXIS FAQ](https://faq.loox.is/books/3d-laser-fotos/page/kann-ich-eine-vorschau-des-3d-glasfotos-sehen) |
| **KI-Line-Art als Stickerei** | ROT | DE mehrfach besetzt, mit eigener Fertigung, günstiger und schneller (Lineries 49,99–59,99 €, Loovina 59,95 €, 3–6 Tage), teils mit Werbung „statt billiger KI“; DB I über Printful-Stick ca. 12–22 € | [Lineries](https://lineries.de/) |
| **Eingestrickter Haustierpullover** | ROT | Lieferanten verkaufen selbst an Endkunden: Knitwise 38 USD (Versand nur in ausgewählte Länder, in die EU nur Express), Printful mit deutscher B2C-Seite; Crown & Paw bietet 114,95 € in EUR; fast nur Q4 | [Knitwise](https://www.knitwise.com/collections/custom-pet-sweater); [Printful DE](https://www.printful.com/de/ugly-christmas-sweater-erstellen) |
| **KI-Test-Tattoo** (Jagua) | ROT | Einziger verifizierter EU-Lieferant ist ein Endkunden-Wettbewerber ohne Händlerpreis (Temporalis: 3× Mittel 54,00 €, 4–5 Wochen) → negativer DB; Kosmetikrecht; Tatship bietet KI + Klebetattoo auf Deutsch ab 19,90 USD | [Temporalis](https://www.temporalis.tattoo/de/products/custom-jagua-tattoo.json); [Tatship](https://tatship.com/de/tattoo/customized-temporary-tattoo) |
| **Familienkochbuch aus Handschrift** (inkl. Sütterlin) | ROT | Keine belegte Nachfrage: US-Nischenführer mit 33 Trustpilot-Bewertungen, zuletzt 01.01.2026, davor 10.06.2023; rezepte.digital 2.400+ Nutzer in 12 Jahren. Handschrifterkennung ist Massenware; DB I ca. 42 € vor Korrekturlesezeit. Produktion wäre gut (Print API A4-Hardcover 80 S. 26,35 € inkl. Versand) | [Trustpilot FCP](https://www.trustpilot.com/review/familycookbookproject.com) |
| **KI-Relief-Schmuck** (Kinderzeichnung, Pfote) | ROT | Lücke im Tiersegment besetzt (GREAT manufaktur: 3D-Pfotenreliefs 239–450 €); Gravur von Kinderzeichnungen ab 35 € überfüllt; kein EU-Direktversand-Partner; Paid-CAC bei Schmuck-Conversion 0,7 % ca. 130 € (SCHÄTZUNG) | [GREAT manufaktur](https://greatmanufaktur.de/) |

**Vor der Vertiefung verworfen oder nur beobachtet** (Details und Endstatus in `kandidaten-longlist.md`):

- **KI-Stilporträt ohne Anlass:** MEINFOTO (Picanova, gleicher Konzern wie das US-Vorbild CANVASDISCOUNT) ab 4,90 €; höchstens Zusatzprodukt.
- **Foto-zu-Muster-Textilien:** von MEINFOTO in DE besetzt.
- **Freier Prompt auf Merch:** Amazon (Juni 2026) und die Printify-App in ChatGPT (April/Mai 2026) bieten das in den USA kostenlos an; Gegenbeleg Wearlie mit rund 5 Kunden nach 9 Monaten (H).
- **KI-Puzzle** (Nachsuche): kein Nachfragebeleg, DE-Fotopuzzle-Anbieter etabliert (H).
- **Prompt-zu-Wandbild ohne Anlass:** kaum Nachfrage (Artsire).
- **Malen nach Zahlen aus Foto:** von Figured'Art und Schipper besetzt.
- **KI-Fotobuch:** CEWE-Domäne.
- **Nur beobachtet:**
  - Tabletop-Miniaturen: kleiner Warenkorb.
  - Wackelköpfe: Handarbeit in Asien.
  - Plüsch nach Foto: kein EU-Hersteller mit Direktversand, Spielzeugrecht.
  - Sammelkarte im Slab: Slab-Kultur in DE klein.
  - Malbuch aus Fotos: nah an der Kinderbuch-Kategorie.
  - KI-Grußkarten: zu kleiner Warenkorb.
  - KI-Song auf Vinyl: Suno Vinyl nicht live, GEMA-Urteile.
  - KI-Fotoeffekt-Massenartikel: kein Burggraben.
  - KI-Teambanner für Jugendsport (Nachsuche, Gamestand): kleine Nische, Ritual in DE fraglich, nah an B2B.
  - KI-Press-on-Nägel (Nachsuche, Nailzotica): keine Nachfrage belegt, kein EU-Fertiger ab Stück 1 bekannt.
- **Bekannte Kategorien** (Kinderbücher, Comics, Familienbiografien, KI-Teppiche) wurden nicht erneut untersucht. Das angrenzende Familienkochbuch wurde als eigene Nische geprüft, siehe oben.

---

## E. 14-Tage-Validierungsplan für den Favoriten

**Grundsatz:** Erst Kaufbereitschaft und Produktqualität prüfen, dann automatisieren.

- **Kein App-Bau:** Im Test gibt es eine Landingpage mit Upload-Formular. Die Vorschauen entstehen halbautomatisch per Skript mit der Gemini-API und werden innerhalb weniger Stunden manuell freigegeben.
- **Einschränkung:** Das weicht vom späteren Produkt mit Sofortvorschau ab. Die gemessene Vorschau→Kauf-Quote ist deshalb eher eine Untergrenze.
- **Bestellung:** manuell im Printful-Dashboard.
- **Freigabe:** Käufe, Registrierungen (z. B. Gewerbeanmeldung) und Kontaktaufnahmen erst nach eurer Freigabe.

### E.1 Budget ca. 1.500 € und Voraussetzungen

| Posten | € (netto) | Hinweis |
|---|---:|---|
| Musterbestellungen: 2× Leinwand Printful (ES) in heller und dunkler Gedenkvariante, 1× Leinwand Print API (NL), 1× Set-Komponenten Decke + Tasse (LV) | ca. 300 | Laufzeit, Verpackung, Farbe dunkler Stile, tatsächliches Routing ES/LV, Packing-Slip-Angaben (GPSR) |
| KI-Testreihe: 25 Mensch-Tier-Fotopaare × bis zu 10 Generierungen, 3 Modelle | ca. 80 | Gemini 3.1 Flash Image, Gemini 3 Pro Image, FLUX.2 |
| Landingpage (Baukasten), Domain, Formular, Zahlungslink bzw. Vorbestellung | ca. 60 | z. B. Shopify-Testmonat oder Carrd + Stripe Payment Links |
| Rechtstexte-Starterpaket | ca. 30 | IT-Recht Kanzlei Starter 9,90 €/Monat (BELEGT) + Puffer |
| **Rechts- und Datenschutz-Kurzcheck vor dem Live-Test** | ca. 250 | ANNAHME zum Preis; siehe Voraussetzungen unten |
| Bezahlter Nachfragetest: **eine** Plattform (Meta), zwei Botschaften („Wiedervereint“ vs. Einzeltier-Gedenken), ohne Trauer-Targeting | ca. 600 | – |
| Creator- bzw. UGC-Video (Tierhalter-Creator) | ca. 150 | Organisches Signal, zugleich Werbemittel |
| Reserve | ca. 30 | – |
| **Summe** | **ca. 1.500** | Test- und Musterbestellungen mit Kundenzahlung laufen durch; Einkauf ca. 40–70 € je Bestellung wird sofort durch die Zahlung gedeckt |

**Voraussetzungen vor dem ersten echten Verkauf:**

- Gewerbeanmeldung
- Impressum
- AGB mit Widerrufsausschluss und Hinweis nach Art. 246a § 1 Abs. 3 EGBGB
- Datenschutzerklärung mit KI-Verarbeitung
- AV-Verträge bzw. Datenschutzbedingungen von Google (Gemini API, Paid-Tarif) und Printful
- KI-Kennzeichnung
- **nur eigene Fotos der Besteller**, keine Fotos Dritter, keine Kinderfotos (im Formular ausschließen)

Bis diese Punkte stehen, läuft der Test als Vorbestellung ohne Zahlung. Das schwächt aber das Kaufsignal.

### E.2 Einheitliche Weiter- und Abbruchkriterien

Diese Tabelle gilt für A, C.9 und E. Die Schwellen sind aus den Basiswerten des Modells abgeleitet.

| Kennzahl | Basiswert im Modell | **Weiter** (≥ Basis) | **Nachjustieren** | **Abbruch** |
|---|---|---|---|---|
| KI-Akzeptanz: Halter beurteilen Mensch **und** Tier als erkennbar | Ziel der Produktionsanalyse: 80 % | ≥ 80 % mit ≤ 10 Generierungen | 60–79 % | < 60 % |
| Manuelle Nacharbeit je Auftrag | 15 Min. (Testphase) | ≤ 15 Min. | 16–30 Min. | regelmäßig > 30 Min. |
| Vorschau-Start → bezahlte Bestellung (alle Quellen) | 8 % | ≥ 8 % | 5–7,9 % | < 5 % |
| Ø Warenkorb | 127 € | ≥ 120 € | 105–119 € | < 105 € (DB I fast halbiert, siehe Sensitivität) |
| Paid-CAC (nur Richtwert, siehe Statistik) | 56 € | ≤ 60 €; ≤ 40 € → Paid ausbauen (optimistischer Pfad) | 61–120 € → Paid auf Restbudget, weiter über Partner und organisch | > 120 € **und** kein Partner bereit |
| Partnerbereitschaft (Gespräche mit 5 Tierbestattern und 3 Tierarztpraxen) | Partnerstart Monat 4 | ≥ 2 zum Test bereit | 1 | 0 und Paid-CAC > 60 € |
| Musterqualität | Reklamation 5 % + Erstattung 2 % | keine Mängel, Laufzeit ≤ 10 Werktage | einzelne behebbare Mängel | wiederholte Mängel bei allen Partnern |
| Nachkontrolle an Tag 30: Reklamations- und Kulanzquote der Testbestellungen | 7 % | ≤ 7 % | 8–15 % | > 15 % |
| Wettbewerb | – | kein DE-Anbieter mit automatisierter „Wiedervereint“-Funktion unter 90 € | – | Pet Printed oder MyPortrait bieten es unter 90 € an |

**Entscheidungsregel:**

- **Weiter:** Keine Kennzahl steht auf Abbruch, und KI-Akzeptanz, Vorschau→Kauf und Warenkorb erreichen mindestens „Nachjustieren“. Mindestens zwei davon erreichen „Weiter“.
- **Abbruch:** Mindestens eine Kennzahl steht auf „Abbruch“.
- **Nachjustieren:** alles andere. Dann läuft der Test 4 Wochen ohne neue Werbeausgaben weiter. Dabei wird der Mix angepasst (mehr Sets, Preis) oder das Kernprodukt reduziert: Bei schwacher KI-Qualität bleibt nur das Einzeltier-Gedenkporträt mit Merkmalsprüfung; dann entscheidet der Preisvergleich mit Pet Printed.

**Statistik:** 600 € Werbung bei 0,90 € CPC ergeben ca. 670 Besuche. Bei 20 % Startquote sind das ca. 130 Vorschau-Starts, bei 8 % also ca. 10 Bestellungen. Ein 95-%-Poisson-Intervall reicht von etwa 5 bis 18 Bestellungen, der Paid-CAC also von etwa 33 bis 120 €. **Der Test unterscheidet deshalb nur grob zwischen vorsichtigem und Basis-Szenario.** Vorschau→Kauf wird über alle Vorschau-Starts gemessen (Werbung, Creator, organisch).

### E.3 Ablauf

| Tage | Aufgabe | Ergebnis |
|---|---|---|
| 1–2 | Muster bestellen. Printful-EUR-Preise und Routing im Dashboard prüfen. Google Keyword Planner abfragen für „Regenbogenbrücke Bild“, „Bild mit verstorbenem Hund“, „Gedenkbild Katze“, „Haustier Portrait Gedenken“. Rechtscheck beauftragen. KI-Testreihe mit 25 Fotopaaren aus dem eigenen Umfeld starten (mit Einwilligung; verschiedene Rassen und Fellzeichnungen, 5 alte oder unscharfe Fotos). | Kostenbasis in EUR, Suchvolumen, erste KI-Qualität |
| 3–4 | **Zweistufige Bewertung:** (a) Die Halter beurteilen die Merkmalstreue ihrer eigenen Tiere und Personen. (b) Etwa 10 Fremde beurteilen Ästhetik und Zahlungsbereitschaft („Würden Sie 129 € zahlen?“). Generierungen bis zur Akzeptanz und Minuten Nacharbeit zählen. | Akzeptanzquote, Generierungen, Prüfminuten, Preisindikation |
| 3–5 | Landingpage mit echtem Angebot: kostenlose Vorschau per Upload; Preise 129 € Kern, 89 € Einzeltier, 169 € Set; Zahlung mit voller Erstattung vor dem Druck, falls die finale Vorschau nicht gefällt. Parallel, nach eurer Freigabe: 5 Tierbestatter und 3 Tierarztpraxen um ein Gespräch bitten. | Test live, Gespräche terminiert |
| 5–12 | Werbetest mit ca. 600 € über 7 Tage, zwei Botschaften. Täglich messen: Besuche, Vorschau-Starts, Vorschau→Zahlung, CPC, Paid-CAC, Warenkorb. Vorschauen innerhalb weniger Stunden liefern; Testbestellungen regulär über Printful ausliefern. | Conversion-Kette, CAC, Warenkorb |
| 6–10 | Partnergespräche: Interesse an Gutschein- bzw. QR-Karte, Provision (Vorschlag 15 %), UWG-konforme Form (Auslage statt Einleger); Berufsrecht bei Tierärzten klären. | Zahl bereiter Partner |
| 8–12 | Muster bewerten: Farbe dunkler Stile, Leinwand, Decke, Tasse, Verpackung, Laufzeit, Packing Slip. | Qualitätsfreigabe je Partner |
| 13–14 | Auswertung nach E.2 und Entscheidung. | Weiter, Nachjustieren oder Abbruch |
| Tag 30 | Nachkontrolle: Reklamationen und Kulanz der Testbestellungen. | Reklamationsquote |

### E.4 Was der Test misst und was offen bleibt

| Misst der 14-Tage-Test | Misst er **nicht** → zweite Prüfphase (Woche 3–12, nur bei „Weiter“) |
|---|---|
| KI-Qualität und Nacharbeit, Vorschau→Kauf, Warenkorb, grober Paid-CAC, Musterqualität, **Bereitschaft** von Partnern | **Organische Reichweite:** Modell Basis 375 Besuche in Monat 3, 1.500 in Monat 12. Frühindikatoren: Keyword-Planner-Volumen (Tag 1); ≥ 300 organische Besuche im dritten Monat; Pinterest- und SEO-Impressionen |
| | **Partnervolumen:** Modell Basis ab Monat 4, bis 20 Bestellungen pro Monat in Monat 10. Kriterien: ≥ 3 Partner mit Material bis Woche 8; erste eingelöste Codes bis Woche 12; sonst Partnerannahme im Modell halbieren (Sensitivität: Jahr 1 −4.103 €) |

**Nach bestandener zweiter Phase:** Automatisierung (API-Bestellfluss, Score-Schwellen, Mockups aus der Produktionsdatei), vollständige Rechtsprüfung, LUCID-Registrierung und Produkthaftpflicht.

---

## F. Rechtliche und operative Stolpersteine (Querschnitt)

Stand 30.09.2026, überwiegend aus Primärquellen; Details in `rohdaten/kontext-recht-partner-kosten.json`. **Das ist keine Rechtsberatung.** Alles, was mit „prüfen“ markiert ist, vor dem Start fachlich klären.

| Thema | Befund | Vor Start fachlich prüfen |
|---|---|---|
| **Widerrufsrecht** | Ausgeschlossen nur bei Waren, die nicht vorgefertigt sind und deren Herstellung auf einer maßgeblichen individuellen Bestimmung durch den Verbraucher beruht (§ 312g Abs. 2 Nr. 1 BGB); das gilt auch vor Produktionsbeginn (EuGH C-529/19). Katalogmotive, Standardgrößen, Zubehör und Gutscheine bleiben widerrufbar. Über den Ausschluss ist zu informieren (Art. 246a § 1 Abs. 3 EGBGB). Die **Widerrufsfunktion** (§ 356a BGB, Beschriftung „Vertrag widerrufen“ plus Bestätigung) gilt seit 19.06.2026; erste Abmahnungen gibt es seit August 2026 (Händlerbund). **Das Widerrufsrecht entfällt nicht automatisch bei jedem KI- oder POD-Produkt.** | ja: Einordnung je Artikel, gemischte Belehrung |
| **Gewährleistung und Haftung** | Kaufrecht (§ 650 BGB), 2 Jahre Gewährleistung, Beweislastumkehr im ersten Jahr (§ 477). Abweichungen von der üblichen Beschaffenheit, etwa KI-Abweichungen oder Farbe, nur mit gesonderter, ausdrücklicher Vereinbarung (§ 476 Abs. 1). Der Rückgriff auf den Partner (§§ 445a, 478) läuft bei ausländischen Partnern mit kurzen AGB-Fristen oft ins Leere: Printful 30 Tage, Print API 2 Wochen. | ja: Partner-AGB |
| **Produkthaftung** | Wer mit Eigenmarke auftritt, gilt als Quasi-Hersteller (§ 4 ProdHaftG). Nach der Richtlinie 2024/2853 gilt für Produkte ab 09.12.2026 auch als Hersteller, wer „herstellen lässt“; Software und KI sind Produkte. Die deutsche Umsetzung stand auf der BMJV-Seite am 05.03.2026 als „Entwurf“; den **aktuellen Stand prüfen**. | ja: Produkthaftpflicht (Eigenmarke) |
| **Produktsicherheit (GPSR)** | Art. 9, 13 und 19: Risikoanalyse, technische Unterlagen (10 Jahre), Chargen- bzw. Bestellnummer, Herstelleranschrift, Online-Angaben, Sicherheitsinformationen auf Deutsch (§ 6 ProdSG). | ja: Umsetzung beim Partner |
| **Spielzeug, Lebensmittelkontakt, Textil, Schmuck** | Spielzeugrecht mit CE (Plüsch, bespielbare Figuren); Lebensmittelkontakt (VO 1935/2004, 10/2011) für Tassen und Tortenfiguren; Faserangabe (VO 1007/2011); Nickel, Blei und Cadmium (REACH) bei Schmuck. | je Produkt |
| **Verpackung** | Seit 12.08.2026 PPWR und VerpackDG: LUCID-Registrierung und Systembeteiligung ohne Bagatellgrenze; neue Rollen „Erzeuger“ und „Hersteller“. Beim POD-Versand aus dem EU-Ausland ist die Rolle ungeklärt. | ja: ZSVR und Partner |
| **Urheberrecht an Fotos** | Auch einfache Lichtbilder sind geschützt (§ 72 UrhG). Der Shop stellt die Kopie selbst her und haftet deshalb nicht nur als Plattform. Nötig sind Rechtezusicherung und Freistellung in den AGB. | ja |
| **Rechte an KI-Motiven** | Reine KI-Motive sind in der Regel nicht geschützt (AG München, 13.02.2026, 142 C 9786/25; laut Sekundärquelle). Nachahmung lässt sich kaum verhindern; Kunden kein „Urheberrecht“ versprechen. | ja: AGB |
| **Recht am eigenen Bild und Persönlichkeitsrecht** | § 22 KUG: Einwilligung der Abgebildeten, bei Verstorbenen 10 Jahre lang die der Angehörigen. Ob die Einzelanfertigung für den Besteller ein „Verbreiten“ ist, ist fraglich. Die DSGVO gilt unabhängig davon. | ja |
| **Marken- und Figurenschutz** | Stil-Prompts wie „Disney“ oder „Ghibli“ sind riskant bei konkreten Figuren, Logos und Namen in Titeln oder Anzeigen (§ 14 MarkenG, §§ 23, 97 UrhG). Nötig sind eine Prompt-Sperrliste und eine Prüfung der Ausgabe. | ja |
| **Irreführung (§ 5 UWG)** | KI-Drucke nicht als „gemalt“ oder „handgemalt“ bewerben; Herstellungsart klar benennen. | ja: Werbetexte |
| **KI-VO** | Art. 50 seit 02.08.2026: maschinenlesbare Kennzeichnung (Anbieter der API) und Offenlegung von Deepfakes (Betreiber). Ab 02.12.2026 neue Verbote für nicht einvernehmliche intime Deepfakes und Missbrauchsdarstellungen (Omnibus-VO 2026/1744, in Kraft seit 27.07.2026). Schutzfilter, besonders für Kinderfotos, sind dringend empfohlen. | ja |
| **Datenschutz** | Normale Fotos sind keine biometrischen Daten; Face-Embeddings können es werden (Art. 9). Nötig sind AV-Verträge mit KI-API, Hosting und Produktionspartner, kein Training mit Kundendaten, ein Löschkonzept und die DPF-Zertifizierung des US-Anbieters (EuG hat das DPF am 03.09.2025 bestätigt, Rechtsmittel anhängig). Bei Kinderfotos gilt besondere Vorsicht. | ja |
| **Zoll bei Drittlandfertigung** | Die 150-€-Zollbefreiung ist seit 01.07.2026 gestrichen. Bis 01.07.2028 gilt pauschal 3 € je Ware bei Sendungen bis 150 € Sachwert, aber nur bei IOSS oder Postsendung; sonst der reguläre Tarif (VO (EU) 2026/382). Ab 01.11.2026 kommt möglicherweise eine Bearbeitungsgebühr hinzu (SCHÄTZUNG). → Der Finalist wird bewusst nur in der EU gefertigt. | bei Nicht-EU-Partnern |
| **Umsatzsteuer** | Regelbesteuerung oder Kleinunternehmerregelung (§ 19 UStG) im Nebenerwerb; Reverse-Charge bei Rechnungen von Printful und Google aus dem EU-Ausland; Einordnung der Lieferung ES/LV → DE-Endkunde (Reihengeschäft, Fernverkauf, OSS). Das Modell unterstellt Regelbesteuerung mit 19 %. | ja: Steuerberatung |
| **Provisionen an Tierärzte** | Berufsordnungen der Landestierärztekammern können Provisionen für Empfehlungen einschränken. | ja |
| **Barrierefreiheit (BFSG)** | Kleinstunternehmen (unter 10 Beschäftigte, höchstens 2 Mio. € Umsatz), die Dienstleistungen anbieten, sind ausgenommen (§ 3 Abs. 3 BFSG). | nein (bei Wachstum erneut) |
| **Basispflichten Shop** | Impressum (§ 5 DDG); Bestellbutton „zahlungspflichtig bestellen“ (§ 312j BGB); Preisangaben, bei Rabatten der niedrigste Preis der letzten 30 Tage (§ 11 PAngV); OS-Link entfernen (VO 2024/3228); Melde- und Abhilfeverfahren für gespeicherte Uploads (DSA Art. 16). | Standard-Rechtstexte |
| **Abhängigkeit von KI-Anbietern** | Modelle, Preise, Ratenlimits (z. B. gpt-image-2 Tier 1: 5 Bilder/Minute) und Filter ändern sich; die Lizenz von Hunyuan3D schließt die EU aus. Mindestens zwei Modelle anbinden, Stile nicht an ein Modell koppeln. | technisch |
| **Abhängigkeit vom Produktionspartner** | Insolvenzrisiko (Shopify-Rezension meldet ein Verfahren bei Shirtee.Cloud, nicht amtlich geprüft), kurze Rügefristen, Routing ins Drittland bei fehlender EU-Variante. Mindestens zwei Partner qualifizieren. | Musterbestellungen |

---

## G. Methodik, Datenlage und Einschränkungen

**Vorgehen** (agentengestützte Webrecherche am 30.09.2026):

1. **Breitensuche:** 8 Suchwinkel nach Produktkategorie und Belegtyp, Lückenkritik, 2 Nachsuchen. Ergebnis: 56 Rohfunde, daraus eine Longlist von 25 Nischen (nach der Nachsuche in H: 27).
2. **Querschnitt:** Recht (Primärquellen), 44 EU-Produktionspartner, Markt- und Werbebenchmarks, Kostenbenchmarks.
3. **Vertiefung:** 11 Nischen in 2 Runden. Je Nische gab es eine Markt- und Wettbewerbsanalyse, eine Produktions- und KI-Analyse und einen adversarialen Prüfer, der tragende Aussagen selbst nachgeprüft und übersehene Wettbewerber gesucht hat.
4. **Nachsuche** nach übersehenen US-Vorbildern mit frischem Suchkontingent: 4 Suchwinkel, 14 Rohfunde, Abgleich mit Stichprobenprüfung (H).
5. **Faktencheck:** 36 tragende Aussagen gegen ihre Quellen geprüft, dazu eine Vollständigkeits- und Konsistenzprüfung gegen den Auftrag (`rohdaten/faktencheck.json`). Ergebnis: 25 bestätigt, 10 abweichend, 1 nicht prüfbar. Die Abweichungen sind korrigiert: Printful-Preis, zwei Zählerstände, Versandangaben von Meshy und Knitwise, Destatis-Quelle, Tails-Zähler, ein Zitat, § 356a BGB genauer.
6. **Rechenmodell** als Skript.

**Datenqualität, getrennt von der Attraktivität der Idee:**

| Aspekt | Datenqualität | Begründung |
|---|---|---|
| Produktion und Partnerpreise | gut bis mittel | Viele Preise direkt aus APIs und Preisseiten (BELEGT). EUR-Preise bei Printful und Laufzeiten nach DE fehlen; keine Musterbestellung. |
| Wettbewerb DE | mittel | Shops, products.json und Trustpilot direkt geprüft. Etsy (403, CAPTCHA) und Amazon (503) kaum auslesbar, daher Marktplatzvolumen unbekannt. Lieferzeiten und Kanäle nicht bei allen erhoben. |
| US-Nachfrage | mittel bis schwach | Überwiegend Bewertungszähler (keine Bestellungen) und Anbieterangaben. **Für keinen KI-Anbieter mit physischem Produkt gibt es belastbare Umsatzzahlen.** |
| DE-Nachfrage | schwach | **Kein Suchvolumen** (kein Zugang zu Keyword-Tools), keine Conversion-Daten. Die Werbebenchmarks sind branchenübergreifende SCHÄTZUNGEN. Superads nennt für Meta DE einen CPC von ca. 0,91 € und Kosten pro Kauf von ca. 63,1 ohne Währungsangabe; der Seitenkopf zeigt teils den Zeitraum Sep. 2025–Aug. 2026. |
| Recht | gut | Primärquellen (gesetze-im-internet.de, EUR-Lex, Amtsblatt, ZSVR); Rechtsprechung zu KI-Output nur aus Sekundärquellen. |

**Einschränkungen:**

1. In der Breitensuche war das gemeinsame Websuche-Kontingent der Suchagenten früh erschöpft (200 von 200). Die Agenten wichen auf Direktabrufe bekannter Domains, Google-News-RSS und die Hacker-News-API aus. Kleine KI-first-Shops waren deshalb unterrepräsentiert. Die Nachsuche mit frischem Kontingent (H) hat 14 weitere Funde gebracht, aber keinen neuen Finalisten; vollständig ist die Marktabdeckung damit trotzdem nicht.
2. Ohne eure Freigabe gab es keine Musterbestellungen und keine Kontaktaufnahmen. Konditionen, die es nur auf Anfrage gibt, stehen als „noch anzufragen“ im Bericht.
3. Wechselkurs 1 USD = 0,86 € (ANNAHME).
4. Das Modell hängt an unbelegten Annahmen zu Conversion, organischer Reichweite, Partnerbestellungen und Warenkorb. Sie sind in `finanzmodell/parameter.py` gekennzeichnet; E.4 zeigt, welche davon der Test misst.

---

## H. Nachsuche nach übersehenen US-Vorbildern

Die Nachsuche lief mit 4 Suchwinkeln: Presse und Finanzierungen, Social-Commerce und virale Trends, bisher unterabgedeckte Kategorien, Enabler-Daten. Danach wurden die Funde gegen Longlist und Finalisten abgeglichen; der Abgleich hat die tragenden Zahlen mit 8 eigenen Abrufen stichprobenhaft nachgeprüft. Rohfunde und Bewertung stehen in `rohdaten/nachsuche.json`.

**Ergebnis: 14 neue Rohfunde, kein zusätzlicher Finalist.** Keiner der Funde schlägt „Wiedervereint“, keiner wurde zur Vertiefung empfohlen. Nur drei sind echte neue Kategorien, die übrigen sind Varianten bestehender Longlist-Nischen.

| Fund (US, sofern nicht anders angegeben) | Einordnung | Nachfragebeleg April–Sept. 2026 | Urteil |
|---|---|---|---|
| [Gamestand](https://gamestand.com/) – KI-Teambanner für Jugendsport-Mannschaften | **neu** (Nr. 26 der Longlist) | Öffentlicher Shop-Katalog: 1.762 Einträge „Custom Team Banner“ von 05/2024 bis 09/2026, meist 80 USD (BELEGT als Zählung; dass jeder Eintrag eine Bestellung ist, bleibt ANNAHME). Frühjahr 2026 ca. +143 % zum Vorjahr, Herbst 2026 ca. −45 % (SCHÄTZUNG, September unvollständig). Vertrieb über eine Jugendfußball-Liga in 30 Regionen, weniger als 10 Mitarbeiter (BELEGT, [OCBJ, 10.02.2025](https://www.ocbj.com/oc-homepage/gamestand-taps-ai-to-boost-youth-sports-merchandising/)) | **Beobachten.** Kleine Nische, Wachstum im Zeitfenster nicht belegt, DB I deutlich unter 60 € (SCHÄTZUNG). Ob deutsche Jugendteams das Ritual „Fantasiename + Banner“ kennen, ist ungeprüft (ANNAHME: eher Vereinsname und Wappen), und die Kaufentscheidung liegt nah am Verein (B2B) |
| [Nailzotica](https://nailzotica.com) – per KI entworfene Press-on-Nägel | **neu** (Nr. 27) | App-Start 13.06.2026 (BELEGT); ca. 550 Installationen laut Drittanbieter (SCHÄTZUNG, keine Bestellungen); 12 App-Store-Bewertungen, Ø 3,8 (BELEGT) | **Beobachten, niedrige Priorität.** Kein Nachfragebeleg, kein bekannter EU-Fertiger für einzeln bedruckte Nagel-Tips ab Stück 1; mitgelieferter Kleber evtl. Kosmetikrecht (ANNAHME) |
| [Puzzably](https://www.puzzably.com/) – KI-Motiv als Einzelpuzzle | neu als Format | keiner; Produktion laut eigener Seite noch „under sample and specification review“ (ANBIETERANGABE) | **Verwerfen.** Fotopuzzles ab 1 Stück sind in DE etabliert (PuzzleYOU, myRavensburger, Schmidt); Puzzle-Community lehnt KI-Motive teils ab. Höchstens Zusatzformat für ein validiertes Motiv |
| [Printify App in ChatGPT](https://printify.com/printify_chatgpt/) – Prompt → Shirt, Hoodie, Tasche | Nr. 15 | Start April/Mai 2026 (BELEGT, [AI Journal, 10.05.2026](https://aijourn.com/printify-launches-chatgpt-app-to-power-personalized-gifting-through-ai/)); keine Nutzungszahlen; laut Hilfe-Center nur für US-Nutzer (ANBIETERANGABE) | **Verwerfen, Warnsignal:** nach Amazon (Juni 2026) der zweite große Anbieter, der generisches Prompt-Merch kostenlos in einen KI-Assistenten verlegt |
| [Wearlie](https://wearlie.com) – KI-Prompt → Shirt | Nr. 15 | **Gegenbeleg:** ein Verkaufsinserat nennt 5 Kunden und 200 USD wiederkehrenden Jahresumsatz nach rund 9 Monaten (ANBIETERANGABE; Zuordnung zu Wearlie über identische Preise = ANNAHME) | **Verwerfen.** Stützt die Entscheidung für einen engen Anlass statt „KI aufs Shirt“ |
| [Joy Studio](https://withjoy.com/studio/hello) (withjoy) – Foto → KI-Illustration als Karte | Nr. 21 | Start zum Muttertag 2026 (BELEGT, Forbes-Contributor 30.04.2026, nur Snippet); 2,99 USD digital, 11 USD gedruckt inkl. Versand (ANBIETERANGABE); keine Nutzer- oder Bestellzahlen | Zusatzvorbild unter Nr. 21; Warenkorb viel zu klein für ein Kernprodukt. Allenfalls Gedenkkarte als Zusatz zum Finalisten |
| [P.S. (Personalize Send)](https://www.ps.app/) – KI-Grußkarte mit Direktversand | Nr. 21 | nichts im Zeitfenster; „hundreds of paid members“ (ANBIETERANGABE, 10/2025) | Verwerfen; Preisanker 10 USD inkl. Porto |
| [Stat Legend](https://www.statlegend.com/) – Sportsammelkarten | Nr. 18 | nichts im Zeitfenster; „4,500 cards in a day“ aus einem Vereinsauftrag 11/2025 (BELEGT als Zitat) | Verwerfen; KI nur für Text und Freistellung; Vereinskanal in DE durch Stickerstars besetzt |
| [Fancy Pet](https://fancy.pet) – KI-Stilporträt vom Haustier (Sitz vermutlich UK) | Nr. 1 | 3 Trustpilot-Bewertungen 06–08/2026 (BELEGT) | Verwerfen; aber als **technischer Bauplan** nützlich (siehe unten) |
| [YETI Custom Shop](https://www.yeti.com/ai-customization-faq.html) – KI-Motiv als Lasergravur | Nr. 14/15 | keine KI-spezifischen Zahlen; Konzern Q2 2026 +9 % (BELEGT, Gesamtgeschäft) | Verwerfen; Serienprodukt, KI als Standardoption einer Massenmarke |
| [PopSockets AI Customizer](https://www.popsockets.com/en-us/pages/cyo-landing-page.html) | Nr. 15 | Start 10/2023, nichts im Zeitfenster | Verwerfen |
| [Shutterfly](https://www.shutterfly.com/ideas/how-to-make-a-christmas-card-with-ai-that-still-feels-personal/) – KI-Werkzeuge im Editor | Nr. 21/22 | **negativ:** Umsatzrückgang, Kreditgeber werten generative KI als Risiko (BELEGT, [Private Equity Wire, 10.06.2026](https://www.privateequitywire.co.uk/apollo-backed-shutterfly-sweetens-debt-terms-as-ai-concerns-weigh-on-credit-markets/)) | Verwerfen; nur Bildbearbeitung, keine Motiverzeugung |
| [Womp](https://womp.com) – Prompt → 3D-Druck | Nr. 6/9 | Start 11/2025, nichts im Zeitfenster | Verwerfen; ROT für 3D bleibt |
| [Stickerbox](https://stickerbox.com) – Kind spricht Idee, Gerät druckt Sticker | außerhalb des Suchraums (Serien-Hardware) | stärkster Durchbruchsbeleg der Nachsuche: Übernahme durch Spin Master am 17.08.2026 (BELEGT, [PR Newswire](https://www.prnewswire.com/news-releases/spin-master-to-acquire-creative-play-technology-company-hapiko-inc-302852440.html)); 7 Mio. USD Finanzierung 2025 sind kein Umsatz | Verwerfen; kein POD, gedruckt wird beim Kunden |

**Was daraus für die Empfehlung folgt:**

1. **Generisches Prompt-Merch wird zur Gratisfunktion.** Printify (ChatGPT-App, April/Mai 2026) und Amazon (Juni 2026) bieten es in den USA kostenlos an, YETI und PopSockets als Standardoption; Wearlie ist ein Gegenbeleg aus dem Kleinsegment. Das stützt den Ausschluss von Nr. 15 und die Logik des Finalisten: enger Anlass plus ein Bildinhalt, den ein Assistent nicht ohne Weiteres liefert (Mensch und verstorbenes Tier aus getrennten Fotos, Merkmalsprüfung, Gedenk-Framing). Startet eine solche Assistenten-App in DE, wird das Gedenkporträt aber ebenfalls leichter selbst zu basteln; das Risiko steht in C.9.
2. **Kanalmuster aus einer anderen Nische:** Gamestand verkauft über Organisationen mit fester Provision je Kauf. Genau diesen Kanal braucht der Finalist, weil bezahlte Werbung im Basismodell nicht trägt (Tierbestatter und Tierarztpraxen, E.2).
3. **Schlanker Technikbauplan:** Fancy Pet nennt als Unterauftragnehmer fal.ai (Bilderzeugung), Printify und Printful (Fertigung), Stripe, Supabase und Vercel; Ablauf „kostenlose Vorschau ohne Registrierung, dann Produktwahl am Mockup“ (ANBIETERANGABE, [fancy.pet/sub-processors](https://fancy.pet/sub-processors), Stand 24.09.2026). Das ähnelt dem in C.6 geplanten Aufbau (Bilderzeugung per API, Fertigung über Printful) und zeigt, dass er mit wenigen Standarddiensten auskommt.
4. **Wert entsteht bei neu erzeugten Motiven, nicht beim Druck eigener Fotos.** Shutterfly steht laut Kreditmarkt unter KI-Druck; der Finalist erzeugt ein Motiv, das es als Foto nicht gibt.

**Einschränkung:** Auch die Websuche der Nachsuche war US-lastig. Die DE-Konkurrenzangaben zu den neuen Kategorien (Teambanner, Press-on-Nägel, Puzzle) sind deshalb VORLÄUFIG.

---

## I. Wichtigste Quellen

Die kuratierten Kernquellen mit Datum stehen in `quellen.md`, das vollständige, automatisch extrahierte Verzeichnis in `quellen-vollstaendig.md`. Abrufdatum aller Web-Quellen: 30.09.2026.
