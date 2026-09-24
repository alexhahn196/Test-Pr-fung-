# Wie professionelle KDP-Unternehmen arbeiten – und welcher Weg von 0 für dich prüfbar ist

**Recherchedatum:** 23.–24.09.2026 · **Sechsmonatsziel:** 5.000 € operativer Monatsgewinn bis 24.03.2027

**Dateien:**
- [`quellen.md`](quellen.md) – Quellen mit Belegqualität
- [`annahmen.md`](annahmen.md) – alle Modellannahmen
- [`kdp_modell.py`](kdp_modell.py) – ausführbares Rechenmodell mit Prüfungen
- [`modell_ausgabe.md`](modell_ausgabe.md) – vollständige Modellausgabe
- [`../technik-test/`](../technik-test/) – lokal ausgeführter Produktionstest

**Kennzeichnung:** BF = belegter Fakt, MA = Modellannahme, SCH = Schätzung, UK = ungeklärt.

**Methode:**
- Die Recherche lief in drei parallelen KI-Agenten-Strängen und wurde von mir ergänzt. Es sind **keine unabhängigen Marktbelege**.
- amazon.de- und amazon.com-Suchseiten waren gesperrt. Bestsellerränge und Rezensionszahlen konkreter Titel sind deshalb **UK**.
- **Nichts wurde gekauft, veröffentlicht, beworben oder kontaktiert.**

---

## 0. Kurzfassung

**Was erfolgreiche Profis wirklich tun:**
- Sie betreiben **große Kataloge**: mehrere Hundert Titel, aufgebaut über Jahre.
- Oft ist es eine **Nische mit Fachbezug** (Prüfungsvorbereitung) oder **Belletristik-Serien**.
- Sie haben **Freelancer oder Ghostwriter**, teils E-Mail-Listen und Autorenwebsites.
- Ihr Umsatz hängt stark an **wenigen Titeln**.
- Die bekannten Szene-Namen verdienen nennenswert an Kursen, Software oder Coaching. Gegen einen Anbieter hat die FTC 2026 wegen irreführender Einkommensversprechen einen Vergleich erzielt (BF).

**Belegte Gewinnhöhen:**

| Segment | Geprüfter Monatsgewinn (Marktplatz-geprüft) |
|---|---|
| Rätsel, Activity, Low-Content | höchstens **≈ 12.000 $** (Low-Content-Vorlagen, ca. 67 Pseudonyme, seit 2020) |
| Prüfungsvorbereitung, 700 Titel, 11 Jahre | ≈ 25.000 $ |
| KI-gestützte Belletristik, über 500 Titel | ≈ 37.000 $ im Jahresschnitt (Spitze laut Übersicht 55.500 $) |

- **50.000 € und mehr pro Monat im Rätselsegment: nicht belegt.**
- 100.000 € im Monat: nirgends belegt.
- Daraus folgt nicht, dass es das nicht gibt. Es ist aber nicht belegbar.

**Was übertragbar ist:**
- Die **Produktionsseite**: Ein lokal ausgeführter Test zeigt, dass eine KI-gebaute Pipeline eindeutige Sudokus erzeugt, mit einem **unabhängigen SAT-Solver** prüft, Dubletten und Schwierigkeit kontrolliert und ein KDP-taugliches PDF mit Rückprüfung liefert.
- **Nicht übertragbar** sind die jahrelang aufgebauten Kataloge.
- Dazu kommt eine **Plattformgrenze**: höchstens **2 neu angelegte Titel je Format und Woche** (BF, [KDP](https://kdp.amazon.com/en_US/help/topic/G202172740)). Das sind höchstens ca. 8 Taschenbücher pro Monat. Diese Grenze bindet stärker als deine Zeit.

**Das Sechsmonatsziel ist derzeit nicht ausreichend belegt.**

| Modellwert Monat 6 (Monte-Carlo-Median, 5 h/Woche) | Gewinn |
|---|---|
| Plausibel | ca. 270 € |
| Stark | ca. 940 € |

- Selbst wenn 8 % der Titel Hits mit 2.000 Verkäufen pro Monat wären, läge der Median in Monat 6 bei ca. 2.600 €.

**Erster Schritt an deiner Stelle:**
- Ein **technischer Abnahmetest**, danach ein **Nachfragetest mit 4 Titeln**:
  - dasselbe sprachneutrale Sudoku-Produkt, jeweils als englische und deutsche Ausgabe
  - einmal klassisch, einmal als differenzierte Variante (Killer-/Jigsaw-Sudoku)
- Kosten ca. 600 €, davon höchstens 500 € Werbung. Ca. 8 Stunden pro Monat.
- Ausbau nur nach Belegen.

---

## 1. Prüfung der Behauptung „Profis verdienen 50.000 € und mehr pro Monat“

### Belegtabelle

| Anbieter | Produkt | Markt / Sprache | Titel / Alter | Zeitraum | Umsatz | Werbung / Kosten | Belegbarer Gewinn | Team / Zeit | Reichweite / sonstige Einnahmen | Qualität |
|---|---|---|---|---|---|---|---|---|---|---|
| [EF #94912](https://empireflippers.com/listing/94912/) | KI-gestützte Belletristik (LitRPG, Romance …) | KDP, 40 % US, übersetzt | über 500 Titel, 5 Pseudonyme, ca. 10 neue pro Woche, 16 Monate alt | 12 Monate | 451.782 $ | Werbung unter 1 % | **≈ 37.000 $/Monat** (Übersicht: 55.508 $) | allein, 10 h/Woche | 5 Websites, E-Mail-Liste | B |
| [EF #94013](https://empireflippers.com/listing/94013/) | Religion | KDP, Meta-Anzeigen | 1 Buch ≈ 96 % des Umsatzes | ca. 12 Monate | 503.166 $ | ≈ 120.800 $ | ≈ 31.900 $/Monat | 15 h/Woche | 40.000 E-Mail-Abonnenten | B |
| [Flippa #11998429](https://flippa.com/11998429-profitable-kdp-publishing-business-specializing-in-trade-vocational-exam-prep-700-titles) | Prüfungsvorbereitung | KDP | über 700 Titel, 11 Jahre | – | – (78 % Marge) | Werbung, Betrag UK | ≈ 25.100 $/Monat | „systematisiert“, UK | – | B |
| [Flippa-Fallstudie](https://flippa.com/blog/sell-amazon-kdp-business-case-study/) | Kochbücher | KDP | 6 Titel | – | 32.480 $/Monat | 58 % Kosten | ≈ 13.800 $/Monat | UK | – | B/C |
| [EF #92315](https://empireflippers.com/listing/92315/) | **Low-Content nach Vorlagen** | KDP, EN + lokalisiert | ca. 67 Pseudonyme, seit 2020 | 12 Monate | 162.384 $ | „niedrig“ | **≈ 12.000 $/Monat** | 4–8 h/Woche (Q4: 15–25), eigene Leute + Freelancer | – | B |
| [EF #90998](https://empireflippers.com/listing/90998/) | Kinder-Sachbücher | KDP, EN | 12 Titel | 12 Monate | 112.459 $ | 65 % Kosten | ≈ 3.300 $/Monat | 3 h/Woche + Ghostwriter | 500 E-Mail-Abonnenten | B |
| [Danny on Demand](https://dannyondemand.substack.com/p/how-i-made-2625792-in-december-with) | **Activity-Bücher** | Amazon, mehrere Länder | UK | **nur Dezember 2024** | 26.258 $ | 6.281 $ Werbung | 19.877 $ (Einzelmonat, Q4) | allein | Newsletter | D |
| [lowcontentprofits](https://lowcontentprofits.com/amazon-kdp-earnings-report/) | Mathe-Arbeitshefte | US/CA | 9 Titel | 2024 | 5.317 $ Tantiemen | 2.810 $ | ≈ 210 $/Monat | allein | Blog | D |
| Dave Chesson | Sachbücher + Software | KDP | 10 Bücher | – | Bücher 7–14.000 $/Monat | UK | UK | 6 Mitarbeitende (Software) | Software 120.000 $/Monat **Umsatz** | D |
| Kappa (klassischer Rätselverlag, USA) | Rätselhefte | Kiosk, Abo | – | – | ≈ 11,5 Mio. $/Jahr | – | nicht veröffentlicht | Verlag | – | E |

### Einordnung

- **Umsatz statt Gewinn:** Überschriften nennen oft den Umsatz. Beispiele:
  - Der „26.257 $“-Monat ist Umsatz vor Werbung und ein einzelner Dezember.
  - Die „120.000 $/Monat“ sind Software-Umsatz.
- **Bücher allein:** Die Szene-Namen verdienen zusätzlich an Kursen, Software oder Coaching. Die FTC stellte bei Publishing.com fest, dass die meisten Kunden das versprochene Einkommen nie erreichten ([FTC](https://www.ftc.gov/news-events/news/press-releases/2026/04/publishingcom-pay-15-million-misleading-consumers-about-how-much-income-they-could-earn-using), BF).
- **„Passiv“ heißt meist: mit Team.**
  - #92315 hat eigene Leute plus Freelancer und im 4. Quartal bis 25 Stunden pro Woche.
  - #90998 arbeitet mit Ghostwritern.
  - Die geprüften „Nettogewinne“ sind **vor dem Lohn des Inhabers** gerechnet.
- **Dauerhaftigkeit:**
  - Käufer zahlen nur das **2,3- bis 3-Fache des Jahresgewinns**. Der Markt erwartet also eine kurze Lebensdauer.
  - Mehrere Inserate zeigen Rückgänge von −4 % bis −24 % beim Gewinn ([Empire Flippers](https://empireflippers.com/marketplace/amazon-kdp-businesses-for-sale/)).
- **Pseudonyme:** #92315 nutzt ca. 67 Pseudonyme. **Mehrere KDP-Konten sind aber unzulässig** (AGB 4.2, BF). Pseudonyme innerhalb eines Kontos sind erlaubt, solange sie nicht irreführen. Eine Skalierungsstrategie sind sie nicht.
- **Ergebnis:**
  - Ein Gewinn **über 50.000 €/Monat mit Rätsel- oder Activity-Büchern ist nicht belegt**.
  - Der beste geprüfte Rätsel-/Low-Content-Wert liegt bei ≈ 12.000 $/Monat nach etwa 5 Jahren mit Team.
  - Über 50.000 $ lag nur ein Belletristik-Katalog, und das nur in einer Übersichtszahl.
- **Basisraten für die Breite:** Selbstverleger verdienten 2022 im Median ≈ 12.749 $ **im Jahr** ([ALLi via PW](https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/92003-survey-finds-self-published-authors-making-gains.html), C). 44 % der befragten Indie-Autoren verdienen höchstens 100 $ im Monat ([WWM 2025](https://www.writtenwordmedia.com/2025-indie-author-survey-results-insights-into-self-publishing-for-authors/), C). Das ist ein Durchschnittsbild, keine Obergrenze.

---

## 2. Rekonstruktion: Wie die drei relevantesten Fälle aufgebaut wurden

| | EF #92315 (Low-Content) | Flippa #11998429 (Prüfungsvorbereitung) | EF #94912 (KI-Belletristik) |
|---|---|---|---|
| **Dokumentiert** | seit Nov. 2020; ca. 67 Pseudonyme; EN + lokalisierte Ausgaben; 4–8 h/Woche, im Q4 15–25; Team + Freelancer; ≈ 12.000 $/Monat | 11 Jahre; über 700 Titel; gezielte Werbung; 78 % Marge; ≈ 25.100 $/Monat | 16 Monate; über 500 Titel; ca. 10 neue Titel pro Woche; 5 Pseudonyme; Übersetzungen; Werbung unter 1 %; Websites + E-Mail-Liste |
| **Ableitbar** | ≈ 5 Jahre bis zum heutigen Niveau; Q4 stark überdurchschnittlich; Wachstum vor den Grenzen von 2023 begonnen | ≈ 36 $ Gewinn je Titel und Monat im Schnitt, also ein breiter Long-Tail-Katalog; die Nische „Berufsprüfung“ hat echte, zahlungsbereite Nachfrage | ≈ 74 $ je Titel und Monat; Wachstum über **Leser-Serien** (Folgebände), nicht über Werbung. 10 Titel pro Woche übersteigen das Wochenlimit für ein Format; vermutlich E-Book + Taschenbuch (UK) |
| **Unbekannt** | Startkapital, Zahl gescheiterter Titel, Anteil Top-Titel | Startphase, Team, Werbekosten | Qualitätskontrolle, Anteil Top-Titel, Beständigkeit |
| **Bedingungen seitdem verändert** | Tantieme unter 9,99 von 60 % auf 50 % gesenkt (2025); Tageslimit und KI-Offenlegung (2023); „disappointing content“ (BF) | – | KI-Offenlegung; Risiko von Richtlinienänderungen bei KI-Belletristik |
| **Für dich wiederholbar?** | Nur teilweise: Die Produktion ja, die 5 Jahre Katalogaufbau nein | Nein: braucht Fachwissen zur Prüfungsrichtigkeit | Nein: Belletristik-Qualität und Serien-Leserbindung sind ohne Fachwissen nicht prüfbar |

**Misserfolge und Stagnation (Auswahl):**
- Ein Low-Content-Bericht zeigt −70 % im Januar gegenüber Dezember ([getmoneyontheside](https://getmoneyontheside.com/amazon-kdp-income-report-for-january-2024-70-drop/), D).
- Ein Arbeitsheft-Portfolio mit 13 Titeln kam auf ≈ 300 $ Gewinn pro Monat ([lowcontentprofits](https://lowcontentprofits.com/amazon-kdp-income-report-breakdown/), D).
- Es gibt Kontosperren mit einbehaltenen Tantiemen (Forum, Einzelfälle).

---

## 3. Der professionelle Arbeitsablauf und was davon zu dir passt

| Schritt | Beobachtete Vorgehensweise | Quelle | KI-Unterstützung | Deine Restarbeit | Kosten | Passt zu A/B? |
|---|---|---|---|---|---|---|
| Nischenauswahl | Mehrere Top-Titel mit gutem Bestsellerrang (BSR) belegen Nachfrage. Eine Keyword-Kombination ohne verkaufende Titel belegt keine. Bei Low-Content z. B. Top-Titel unter BSR 350.000 | [Book Bolt](https://bookbolt.io/how-to-identify-profitable-niche-markets-using-bookbolts-research-tools/), [lowcontentprofits](https://lowcontentprofits.com/amazon-kdp-niche-research-for-beginners/) (D) | Claude wertet Ränge aus, die du per Screenshot oder Tool-Export lieferst. Direkter Abruf von amazon ist gesperrt, Scraping unzulässig | 15 min: 10 Top-Titel je Idee im eigenen Browser öffnen, Rang und Preis notieren (Vorlage) | Tool optional 10–20 $/Monat (SCH) | ja |
| Nachfrageprüfung | Rang in Verkäufe umrechnen, nur mit Schätzrechnern (amazon.de-Methodik UK) | [Kindlepreneur](https://kindlepreneur.com/amazon-kdp-sales-rank-calculator/) (D) | Umrechnung, Bandbreiten | Entscheidung | 0 | ja |
| Konkurrenzanalyse | Rezensionen, Preisband, Seitenzahl, Innenleben („Blick ins Buch“) | D | Beschwerden aus Rezensionen zusammenfassen | 10 min: Stichprobe prüfen | 0 | ja |
| Positionierung | Unterschied über Format, Schwierigkeit, Schriftgröße, Mischung, Thema. Zu wenig Unterschied riskiert „disappointing content“ | KDP (A) | Konzeptvarianten | wählen | 0 | ja |
| Preis | Verlage setzen in DE einen Preisanker bei **4,99 € für 192 Seiten** ([Naumann & Göbel](https://www.naumann-goebel.de/produkt-details/grossdruck-kreuzwortraetsel-band-1-9783625194590/show/), A). KDP braucht 9,99 netto (≈ 10,69 € brutto bei 7 % bzw. 11,89 € bei 19 %) für 60 % Tantieme | A | Rechnung | freigeben | 0 | ja |
| Inhaltserstellung | Generatoren (Book Bolt u. a.) oder eigene Programme | D | **Claude Code schreibt den Generator** | – | Claude Pro 20 €/Monat | ja |
| Qualitätskontrolle | Profis: Stichproben, Freelancer. Für uns: automatische Prüfung plus Stichprobe | – | Unabhängige SAT-Prüfung, Schwierigkeit, Dubletten, PDF-Rückprüfung (lokal getestet, s. Abschnitt 5) | 25 min: Checkliste und Stichprobe | 0 | ja |
| Cover und Layout | Designer oder Vorlage; Genre-typisches Cover | D | KI-Entwurf, Vorlagen-Rechner von KDP | Auswahl aus 3 Entwürfen, 10 min | optional einmalig 50–150 € Designer (SCH) | ja |
| Druckprüfung | Testexemplar bestellen | D | – | Exemplar ansehen, 10 min | ca. 10 € je Muster | ja |
| Veröffentlichung | Upload von Hand, KI-Angabe, Kategorien | A | Metadaten-Entwurf, Regelprüfung | 25 min Upload | 0 | ja (**Limit 2 pro Woche und Format**) |
| Werbetest | Sponsored Products; 10–15 Klicks je Keyword vor dem Pausieren; 14 Tage auf die Zuordnung warten | [KDP](https://kdp.amazon.com/en_US/help/topic/G201499010) (A), [kboards](https://www.kboards.com/threads/amazon-advertising-when-do-you-pause-a-campaign.333606/) (D) | Kampagnenaufbau, Keyword-Listen, Auswertung der Berichte | Budget freigeben, wöchentlich 30 min entscheiden | Testbudget | ja |
| Auswertung | Diagnose: kaum Impressionen → Gebot/Keywords/Nachfrage; Impressionen ohne Klicks → Cover/Preis; Klicks ohne Kauf → Produktseite/Produkt | [Kindlepreneur](https://kindlepreneur.com/book-sales-problem/) (D) | Automatisch aus Bericht-CSV | Bericht herunterladen | 0 | ja |
| Überarbeitung | Neues Cover oder neue Beschreibung und erneut testen | D | Neue Varianten | freigeben, hochladen (10 min) | 0 | ja |
| Ausbau | Mehr Titel in bewährten Linien (Band 2, 3 …), andere Schwierigkeitsgrade, Formate (Hardcover), Sprachen | D; EF #92315 lokalisiert | Serienproduktion | Prüfung je Titel | – | begrenzt durch Upload-Limit und Zeit |
| Einstellen | Werbung für Titel ohne Verkäufe stoppen. Titel bleiben meist gelistet, weil das kaum kostet | D | Liste der Kandidaten | freigeben | 0 | ja |
| Laufende Kontrolle | Richtlinienmails, Buchhaltung, Werbebudget | A | Entwürfe, Monatsbericht | 1–2 h/Monat | Buchhaltungs-Tool | ja |

**Konkrete Verfahren**, die ich übernehmen würde. Alle Schwellen sind MA, abgeleitet aus Praktikerregeln:
- **Echte Nische:** mindestens 3 Konkurrenztitel mit gutem Rang (Schwelle nach Test festlegen) **und** Preisband ≥ 9,99. Nur Suchbegriffe ohne verkaufende Titel reichen nicht.
- **Vor großer Produktion:** 1 Titel je Linie (bzw. je Sprache) und 6–8 Wochen Werbetest.
- **Mehr Werbung für ein Buch**, wenn:
  - die Werbekosten je Werbeverkauf unter 60 % der Tantieme liegen, **und**
  - mindestens 5 Werbeverkäufe vorliegen.
- **Werbung pausieren** für ein Keyword nach **15 Klicks ohne Verkauf**, für einen Titel nach **60 Klicks ohne Verkauf**.
- **Diagnose-Regeln:**
  - Weniger als 1.000 Impressionen in 14 Tagen → Gebot oder Keywords.
  - Klickrate unter 0,2 % → Cover oder Preis.
  - Über 60 Klicks und 0 Käufe → Produktseite oder Produkt.
  - Nirgends Impressionen trotz höherem Gebot → vermutlich zu wenig Nachfrage (**nicht bewiesen** bei so kleinen Zahlen).
- **Konzentration:** Praktiker sprechen von einer 80/20-Verteilung (D). Das Modell rechnet deshalb mit wenigen Hits und vielen schwachen Titeln.
- **Qualität im großen Portfolio:** Jeder Titel läuft durch dieselbe automatische Pipeline. Rätsel-Fingerabdrücke werden über **alle** Bücher hinweg gespeichert, damit es keine Wiederholung zwischen Büchern gibt („excessively reused … across books“, BF).

---

## 4. Welche Produkte passen?

**Bewertung:** ++ sehr gut, + gut, o neutral, − schwach, −− sehr schwach.

| Kandidat | Nachfragebelege | Differenzierbar | Marge | KI-produzierbar | Ohne Fachwissen prüfbar | Nacharbeit | Werbung | Portfolio | Plattformrisiko |
|---|---|---|---|---|---|---|---|---|---|
| Klassisches Sudoku, Großdruck | o (viele Angebote, Verkäufe UK) | −− | o | ++ | ++ (SAT) | ++ | + | + | Ähnlichkeit zu anderen Büchern |
| Sudoku-Varianten (Killer, Jigsaw, Diagonal), Großdruck | o/UK | + | o | ++ | ++ (SAT mit Zusatzregeln) | ++ | + | + | gering |
| Logikrätsel-Mix (Sudoku, Nonogramm, Kakuro, Futoshiki) | UK | ++ | o | + | + (je Rätseltyp ein Solver) | ++ | + | ++ | gering |
| Wortsuche / Buchstabensalat (Themen) | + (US-Angebote 6–13 $ mit bis zu 148 Bewertungen, [Walmart](https://www.walmart.com/ip/Word-Search-Large-Print-Book-Word-Search-for-Seniors-Large-Print-word-search-book-for-adult-with-a-huge-supply-of-puzzles-including-solutions-9798598109878/364771890), A) | o | o | ++ | + (anstößige Wörter per Sperrliste, Rechtschreibung je Sprache) | ++ | + | + | gering |
| Kreuzworträtsel | + (klassischer Markt) | o | o | − (Füllung und Hinweise schwierig, s. [JAIR](https://arxiv.org/abs/1401.4597)) | **−** (Hinweise erfordern Sprachkompetenz) | + | + | + | Qualitätsbeschwerden |
| Activity-Bücher für Kinder | + (Q4-Beleg D) | + | − (Farbdruck teuer) | + | o (Altersgerechtigkeit) | + | + | + | Kinder-Inhalte |
| Malbücher mit KI-Bildern | UK | − | − | + | o | + | + | + | KI-Offenlegung, Sättigung (UK) |

**Märkte im Vergleich:**
- **Deutscher Markt:**
  - Die Verlage setzen den Preisanker (4,99 € für 192 Seiten A4).
  - Bei KDP sind für 60 % Tantieme mindestens ≈ 10,69 € (bei 7 % USt) bzw. 11,89 € (bei 19 % USt) Endkundenpreis nötig. Für Sudoku-Bücher gilt laut EuGH-Bezug vermutlich 19 % (E).
  - Konsequenz: **Über den Preis ist KDP in DE nicht konkurrenzfähig**, nur über Differenzierung (Varianten, Großdruck-Qualität, Themen).
  - Tantieme pro Stück ≈ 3,76 €.
- **US- und UK-Markt:**
  - Größer, Preise um 6–13 $ (A, Einzelbeispiele).
  - Wegen höherer Druckkosten nur ≈ 2,91 € Tantieme bei 10,99 $.
  - Deutlich mehr Konkurrenz (UK).
- **Später international:**
  - Sudoku und Logikrätsel sind **sprachneutral**. Eine Lokalisierung kostet nur Anleitung, Titel und Metadaten (≈ 30 min Prüfung je Sprache, MA). Werbung läuft je Marktplatz, der Europa-Zugang deckt UK, DE, FR, IT, ES und NL ab (D).
  - Wortsuche braucht je Sprache neue Wortlisten und eine Sperrliste.
  - **Achtung:** Jede Sprachausgabe verbraucht einen der 8 monatlichen Upload-Plätze.

**Empfehlung für den Test:** **Sudoku-Varianten in Großdruck, EN und DE.**
- Maschinell vollständig prüfbar.
- Sprachneutral und damit günstig in mehreren Märkten zu testen.
- Stärker differenzierbar als klassisches Sudoku.
- Das klassische Sudoku läuft als **Vergleichstitel** mit.

---

## 5. Verlässliche KI-Produktion: Architektur und lokaler Test

**Rollen:**
1. **Sprachmodell (Claude Code) als Entwickler** des Produktionssystems. Es schreibt Generator, Prüfer, Satz und Tests. Dokumentiert: [Claude Code](https://code.claude.com/docs/en/overview).
2. **Generator:** eigener Backtracking-Algorithmus, der Lösungen zählt.
3. **Unabhängige Prüfung** mit einem **anderen Verfahren und einer anderen Bibliothek**: SAT-Solver (Glucose über PySAT). Er prüft:
   - Die gespeicherte Lösung erfüllt alle Regeln und passt zu den Vorgaben.
   - Eine Sperrklausel gegen diese Lösung liefert „unerfüllbar“, das Rätsel ist also **eindeutig**.
4. **Schwierigkeit:** Ein Logiklöser nutzt nur menschliche Techniken (Single, Pair, Pointing).
5. **Dubletten:** kanonischer Fingerabdruck über 8 Symmetrien und Umbenennung der Ziffern. Er muss über **alle** Bücher gespeichert werden.
6. **Satz:** PDF mit eingebetteter TrueType-Schrift, 8,5 × 11 Zoll, Ziffern 30 pt, Lösungen 16 pt, Seitenzahlen.
7. **Rückprüfung aus dem fertigen PDF:**
   - Die gedruckten Vorgaben werden ausgelesen und mit den Daten verglichen.
   - Die gedruckten Lösungen werden erneut mit dem SAT-Solver gegen die gedruckten Rätsel geprüft.
   - Seitenformat und Schrifteinbettung werden kontrolliert.
8. **Menschliche Endkontrolle:** Checkliste und Stichprobe, dazu ein Testexemplar.

**Warum die Prüfung unabhängig ist:**
- Generator und Prüfer teilen weder Algorithmus noch Code. Der SAT-Solver ist eine fremde, verbreitete Bibliothek.
- Die PDF-Rückprüfung prüft das **Endprodukt**, nicht die internen Daten. So fallen auch Satzfehler auf.
- **Negativtests** belegen, dass die Prüfer Fehler tatsächlich finden.

**Ergebnis des lokalen Tests (24.09.2026, in dieser Umgebung ausgeführt):**

| Prüfung | 20 Rätsel (Seed 2026) | 40 Rätsel (Seed 7) |
|---|---|---|
| SAT bestätigt „eindeutig lösbar“ | 20/20 | 40/40 |
| Schwierigkeit laut Plan (leicht/mittel) | 10/10 | 20/20 |
| Dubletten | 0 | 0 |
| Wegen falscher Schwierigkeit verworfen | 87 | 201 |
| PDF-Seiten | 25 | 50 |
| Befunde der PDF-Rückprüfung (nach Korrektur) | 0 | 0 |
| Laufzeit | ca. 14 s | – |

**Negativtests (alle bestanden):**
- ein mehrdeutiges Rätsel erkannt
- eine falsche Lösung erkannt
- eine gedrehte Dublette erkannt
- im PDF eine fehlende Vorgabenzeile **und** eine vertauschte Lösungsziffer erkannt

**Ein echter Fund:**
- Die erste PDF-Version enthielt **nicht eingebettetes Helvetica**, die Standardschrift der Bibliothek. KDP verlangt eingebettete Schriften (BF).
- Die Prüfung hat das gemeldet, die Korrektur ist erfolgt.
- Das zeigt: **KI-generierter Code braucht automatische Abnahmetests.**

**Was der Test nicht beweist:**
- **Druckqualität am echten Exemplar.** Die Seiten wurden nicht gerastert oder angesehen, nötig ist ein Testexemplar.
- **Cover.**
- **KDP-Vorschau.**
- **Varianten-Sudokus.** Die SAT-Kodierung ist leicht erweiterbar, aber noch nicht gebaut.
- **Wahrgenommene Schwierigkeit.** Die Bewertung mit Basistechniken ist eine Näherung, nicht das SE-Rating.
- **Nachfrage.** Ein simulierter Verkauf ist kein Beleg.

**Technischer Abnahmetest vor dem ersten Upload** (Kriterien MA):
1. 100 Rätsel je Titel: 100 % SAT-eindeutig, 0 Dubletten auch gegen alle bisherigen Bücher, Schwierigkeitsverteilung wie auf dem Cover angegeben.
2. PDF-Rückprüfung ohne Befund.
3. Innenrand gemäß KDP-Tabelle (bei 130 Seiten ≥ 0,375 Zoll, BF), Linien ≥ 0,75 pt, Schrift ≥ 16 pt bei den Ziffern.
4. KDP-Vorschau ohne Warnung.
5. Testexemplar: 5 zufällige Rätsel von Hand lösen oder lösen lassen, Stichprobe mit den Lösungen abgleichen.
6. Negativtests laufen vor jeder Produktion automatisch mit.

**Fachhilfe:** Einmalig optional ca. 100–200 € für eine Prüfung von Satz und Druckvorlage durch einen Setzer (SCH). **Laufend nicht nötig**, weil die Rätsel maschinell verifizierbar sind. Kreuzworträtsel wären dagegen **je Buch** prüfpflichtig. Deshalb sind sie nicht empfohlen.

---

## 6. Plattformregeln und Verantwortung

**Amazon übernimmt** (BF, KDP-AGB):
- Druck, Versand, Zahlung, Erstattungen und Kundenservice

**Bei dir bleibt:**
- Rechte an Inhalt und Cover
- korrekte Metadaten
- KI-Angabe
- Qualitätsmängel beheben
- Steuern (Formular W-8BEN)
- **Impressum im Buch**: Laut Landespressegesetzen z. B. Name und Anschrift des Verlegers bzw. Verfassers (A, Beispiel Niedersachsen). Die Ausnahme für „harmlose Druckwerke“ ist UK und rechtlich zu klären.
- mögliche Sperre nach Amazon-Ermessen

**Regeln, die das Modell begrenzen:**
- 2 neue Titel je Format und Woche; 3 pro Tag (BF)
- ein Konto (BF)
- „disappointing content“ und Wiederverwendung über Bücher hinweg (BF)
- keine Marken oder fremden Namen in Metadaten (BF)
- keine Rezensionen gegen Gegenleistung (E)
- Rätselbücher sind **kein Low-Content**, bekommen also eine kostenlose ISBN (BF)

**Offene Punkte:**
- **KI-Angabe:** Ob algorithmisch, also ohne Sprachmodell, erzeugte Rätsel als „AI-generated“ gelten, ist UK. **Vorsichtsprinzip:** angeben, sobald Texte, Cover oder Bilder KI-generiert sind.
- **Automatisierung:** Ein Upload-API gibt es nicht (E). Browser-Bots für Uploads sind nicht ausdrücklich geregelt (UK). Wegen des Sperrrisikos lädst du **von Hand** hoch.

---

## 7. Gewinnstufen: Was wäre nötig? (Modell, amazon.com-Ökonomie, stationär)

Die Tabelle trennt **„so viele Verkäufe wären nötig“** von der Frage nach Belegen. Die Belegfrage beantwortet sie **nicht**.

| Ziel €/Monat | Szenario | nötige Verkäufe/Monat | Tantiemen | Werbung | bedingt nötige Titel | Monate allein wegen Upload-Limit (8/Monat) |
|---|---|---|---|---|---|---|
| 5.000 | schwach | 10.792 | 30.778 | 25.733 | 2.447 | 306 |
| 5.000 | plausibel | 4.113 | 11.730 | 6.685 | 332 | 41 |
| 5.000 | stark | 2.968 | 8.466 | 3.421 | 92 | 11 |
| 10.000 | schwach | 68.012 | 193.973 | 184.437 | 15.422 | 1928 |
| 10.000 | plausibel | 8.904 | 25.394 | 15.349 | 718 | 90 |
| 10.000 | stark | 6.152 | 17.546 | 7.501 | 190 | 24 |
| 25.000 | schwach | inf | inf | inf | inf | inf |
| 25.000 | plausibel | 25.219 | 71.925 | 46.880 | 2.034 | 254 |
| 25.000 | stark | 16.245 | 46.330 | 21.285 | 502 | 63 |
| 50.000 | schwach | inf | inf | inf | inf | inf |
| 50.000 | plausibel | 56.358 | 160.734 | 110.689 | 4.545 | 568 |
| 50.000 | stark | 34.005 | 96.983 | 46.938 | 1.051 | 131 |
| 100.000 | schwach | inf | inf | inf | inf | inf |
| 100.000 | plausibel | 128.225 | 365.704 | 265.659 | 10.341 | 1293 |
| 100.000 | stark | 71.405 | 203.650 | 103.605 | 2.207 | 276 |

**Lesart:**
- **Plausibles Szenario:**
  - 5.000 € brauchen ≈ 4.100 Verkäufe pro Monat bzw. ≈ 330 Titel.
  - Allein das Upload-Limit von 8 Taschenbüchern pro Monat erlaubt das frühestens nach **≈ 41 Monaten**.
  - Mit Hardcover als zweitem Format wären es ca. 21 Monate, bei doppeltem Prüfaufwand.
- **Starkes Szenario:** 92 Titel bzw. ca. 11 Monate.
- **50.000 €:**
  - braucht ≈ 34.000–56.000 Verkäufe pro Monat und 1.000–4.500 Titel
  - ≈ 47.000–111.000 € Werbung pro Monat
  - mit steigenden Kosten je Werbeverkauf
  - Das ist **kein Vielfaches** des 5.000-€-Modells, weil die Werbekosten mit dem Volumen steigen.
- **Belege für diese Mengen im Rätselsegment: keine.** Das beste geprüfte Portfolio liegt bei ≈ 12.000 $.

**Monte-Carlo über 300 zufällige Portfolios** (Monatsgewinn in €, Veröffentlichungen bis zur Grenze von Zeit und Upload-Limit):

| Szenario | Budget | M6 P10 | M6 Median | M6 P90 | M12 P10 | M12 Median | M12 P90 |
|---|---|---|---|---|---|---|---|
| schwach | A | -27 | -16 | 10 | 4 | 32 | 64 |
| schwach | B | 11 | 36 | 67 | 110 | 154 | 210 |
| plausibel | A | 15 | 82 | 180 | 128 | 244 | 390 |
| plausibel | B | 162 | 271 | 406 | 560 | 739 | 969 |
| stark | A | 117 | 333 | 630 | 530 | 861 | 1.305 |
| stark | B | 592 | 941 | 1.381 | 1.790 | 2.459 | 3.154 |

---

## 8. Werbung und Liquidität

**Definitionen** (Bezugsgrößen ausdrücklich):
- **Werbekosten je Werbeverkauf (CPA)** = Werbeausgaben ÷ werbezugerechnete Bestellungen
- **ACOS** = Werbeausgaben ÷ werbezugerechneter Umsatz (Amazon-Definition, BF). Ob die Konsole in DE brutto oder netto zählt, ist UK.
- **TACOS** = Werbeausgaben ÷ **gesamte Tantiemen**. Das ist die Kindlepreneur-Definition (D), nicht die Amazon-Definition, weil Amazon TACOS nicht definiert.

**Obergrenzen:**
- **Break-even je Werbeverkauf** = Tantieme: 3,76 € (DE) bzw. 2,91 € (US).
- Break-even-ACOS ≈ 34 % (DE, auf Netto-Listenpreis) bzw. ≈ 31 % (US).

**Zusatzverkäufe:** Werbezugerechnete Verkäufe sind **nicht** automatisch Zusatzverkäufe. Messung über einen Vergleich mit Werbepausen (A/B über Zeiträume) oder über den Verlauf der Gesamtverkäufe. **Wiederkäufe durch Serien werden nicht unterstellt.**

**Liquidität:**
- Tantiemen kommen ca. 60 Tage nach Monatsende. Werbung wird laufend belastet.
- Im Plausibel-Szenario liegt der **niedrigste Kassenstand bei ca. 1.460 € von 2.500 €**.

| Startkapital | Einschätzung |
|---|---|
| 1.000 € | reicht für Test und langsamen Ausbau, wenn das Werbetestbudget auf 300 € sinkt |
| 2.500 € | komfortabel |
| 5.000 € | beschleunigt nicht, weil Upload-Limit und Nachfrage begrenzen |

- **Mehr Kapital nötig** wäre erst bei Werbung über ≈ 1.500 €/Monat, also etwa bei 5.000 € Gewinn. Gründe: Auszahlungsverzögerung plus Kreditkartenzyklus.
- **Reinvestition:** nur aus ausgezahlten Tantiemen, nach einer Reserve von 3 Monaten Fixkosten plus Werbung und einer Steuerrücklage von 30–40 % (MA).
- **Währung:** US-Werbung wird in $ bezahlt, Tantiemen werden von Amazon umgerechnet (BF). Das Kursrisiko ist im Modell nicht abgebildet (MA 0,86).

**Sechs bzw. zwölf Monate im Planungsszenario:** Budget B, Plan 2, 2, 4, dann 8 Titel pro Monat.

| Monat | neue Titel | Titel ges. | Verkäufe | Endkundenumsatz | Tantiemen | Werbung | **op. Gewinn** | ausgezahlt | Kasse | kum. Gewinn | deine Std. | Gewinn − Zeit à 25 €/h |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | 2 | 2 | 4 | 42 | 13 | 255 | **-288** | 0 | 2.200 | -288 | 6.5 | -450 |
| M2 | 2 | 4 | 16 | 149 | 45 | 269 | **-269** | 0 | 1.885 | -557 | 6.6 | -433 |
| M3 | 4 | 8 | 29 | 272 | 82 | 35 | **2** | 13 | 1.818 | -555 | 9.6 | -239 |
| M4 | 8 | 16 | 40 | 374 | 113 | 49 | **19** | 45 | 1.769 | -536 | 15.7 | -375 |
| M5 | 8 | 24 | 108 | 1.017 | 307 | 137 | **125** | 82 | 1.669 | -411 | 16.0 | -274 |
| M6 | 8 | 32 | 210 | 1.982 | 598 | 275 | **278** | 113 | 1.462 | -133 | 16.2 | -126 |
| M7 | 8 | 40 | 319 | 3.012 | 909 | 428 | **436** | 307 | 1.296 | 303 | 16.4 | 26 |
| M8 | 8 | 48 | 404 | 3.817 | 1.152 | 551 | **556** | 598 | 1.298 | 859 | 16.6 | 141 |
| M9 | 8 | 56 | 431 | 4.074 | 1.229 | 590 | **594** | 909 | 1.572 | 1.453 | 16.8 | 175 |
| M10 | 8 | 64 | 471 | 4.451 | 1.343 | 649 | **649** | 1.152 | 2.030 | 2.102 | 16.9 | 227 |
| M11 | 8 | 72 | 552 | 5.216 | 1.574 | 769 | **760** | 1.229 | 2.445 | 2.862 | 17.1 | 331 |
| M12 | 8 | 80 | 674 | 6.370 | 1.922 | 953 | **924** | 1.343 | 2.791 | 3.787 | 17.4 | 490 |

---

## 9. Zeitgrenzen je Stufe

| Stufe | KI-Arbeit | Deine Stunden (Modell A/B) | Andere Menschen |
|---|---|---|---|
| Test (4 Titel) | Generator, Prüfung, Satz, Texte, Auswertung | ca. 8 h pro Monat, passt in **A** | – |
| Ausbau bis 8 Titel pro Monat | wie oben | ca. 16–17 h pro Monat, **nur B** | – |
| 5.000 € (≈ 100–330 Titel) | wie oben | Pflege ≈ 7–14 h pro Monat plus Neuerscheinungen 12 h. Mit B **knapp oder überschritten**, wenn Ausbau und Hardcover parallel laufen | optional VA ca. 260 €/Monat |
| 10.000–25.000 € | wie oben | nicht mehr in 5 h/Woche: Werbesteuerung bei hunderten Titeln, Qualitätsfälle, 2 Formate | VA, Satzprüfung, Werbe-Manager: ca. 1.300 €/Monat plus deine Führung ca. 15–18 h/Monat |
| 50.000–100.000 € | – | **nicht mit deinen Grenzen vereinbar** | Team, laut Belegen mit eigenem Personal (#92315) oder Serienaufbau (#94912) |

**Variante B mit Team** ist nur als Abweichung gedacht. Sie senkt deine Arbeit **nicht auf null**: Bleiben würden Führung, Freigaben, Buchhaltung und Qualitätsverantwortung, also ca. 3–4 h pro Woche.

---

## 10. Der Weg von null: Hauptansatz

**Produkt:**
- „Large Print Sudoku Variety – Killer, Jigsaw & Classic, 100 Puzzles, Easy to Medium, with Solutions“
- dazu die deutsche Ausgabe „Sudoku Großdruck – Killer, Jigsaw & Klassisch“
- Vergleichstitel: klassisches Sudoku in Großdruck, EN/DE

**Zielgruppe:** ältere Rätselfreunde und Menschen, die ein Geschenk suchen.
**Positionierung:** große Ziffern (≥ 30 pt), klar ausgewiesene Schwierigkeit, geprüfte eindeutige Lösbarkeit.
**Preis:** 10,99 netto.
**Marktplätze:** amazon.com, amazon.co.uk, amazon.de.
**Erster Vertriebskanal:** Amazon-Suche plus Sponsored Products.

| Monat | Messbares Ziel | Max. Ausgabe | Deine Zeit | Entscheidung |
|---|---|---|---|---|
| M1 | Pipeline um Killer- und Jigsaw-Sudoku erweitert; Abnahmetest (Abschnitt 5) bestanden; 2 Titel (Varianten EN + DE) live | 150 € (Claude, 2 Muster, Konto) | ≤ 8 h | Abnahmetest nicht bestanden → nicht hochladen |
| M2 | 2 Vergleichstitel (klassisch EN + DE) live; Werbung für alle 4 Titel | 250 € Werbung + 45 € | ≤ 8 h | nach 14 Tagen erste Auswertung, noch keine Stopp-Entscheidung |
| M3 | ≥ 60 Klicks je Titel gesammelt; Werbekosten je Werbeverkauf gemessen | 250 € Werbung (Rest der 500) | ≤ 8 h | **Entscheidungspunkt 1** (s. u.) |
| M4 | Nur bei „weiter“: Band 2 der besten Linie in den besten 1–2 Märkten; Dubletten-Datenbank über alle Bücher | 300 € | ≤ 12 h (Budget B) | Werbung nur für profitable Titel |
| M5 | 4–6 weitere Titel in der bewährten Linie; Hardcover-Ausgabe des besten Titels testen | 400 € | ≤ 18 h | zweite Linie nur, wenn Linie 1 in zwei aufeinanderfolgenden Monaten profitabel ist |
| M6 | Bilanz: Gewinn je Titel, TACOS, Anteil organischer Verkäufe; Q4-Effekt gesondert herausrechnen | 400 € | ≤ 18 h | Ausbau auf 8 pro Monat nur bei Gewinn je Titel ≥ 15 €/Monat außerhalb der Q4-Spitze |

**Entscheidungsregeln (MA):**
- **Buch überarbeiten:** über 1.000 Impressionen, aber Klickrate unter 0,2 % → neues Cover. Über 60 Klicks ohne Kauf → Beschreibung, Preis oder Innenansicht.
- **Werbung pausieren:** je Keyword nach 15 Klicks ohne Verkauf; je Titel, wenn die Werbekosten je Werbeverkauf 2 Wochen lang über der Tantieme liegen.
- **Zweiter Titel einer Linie:** Der erste Titel hat mindestens 10 Verkäufe in 6 Wochen **und** Werbekosten je Werbeverkauf unter 60 % der Tantieme.
- **Weitere Nische:** Die bestehende Linie ist 2 Monate profitabel, **und** Zeitbudget und Upload-Platz sind frei.
- **Gesamtbudget steigt:** nur aus ausgezahlten Tantiemen nach Reserven.
- **Produkt einstellen:** 4 Monate ohne nennenswerte Verkäufe → Werbung aus. Der Titel bleibt gelistet, keine Folgebände.
- **Datenmenge:**
  - Unter 60 Klicks je Titel gibt es **keine** Marktaussage.
  - Nach 4 Titeln × 60 Klicks lässt sich nur eine grobe Aussage über **dieses** Angebot treffen, nicht über den Rätselmarkt.

**Entscheidungspunkt 1 (Ende M3):**
- **Weiter:** mindestens ein Titel mit ≥ 10 Verkäufen und Werbekosten je Werbeverkauf ≤ 60 % der Tantieme.
- **Überarbeiten:** Verkäufe vorhanden, aber zu teuer. Eine Variable ändern (Cover, Preis, Keywords) und weitere 6 Wochen testen.
- **Stopp:** alle 4 Titel unter 3 Verkäufen trotz ≥ 60 Klicks je Titel, **oder** Richtlinienprobleme.

---

## 11. Von 5.000 € zu 50.000 € und 100.000 €: Voraussetzungen statt Wachstumskurve

| Stufe | Notwendige Veränderung | Bei Profis belegt? | Verlangt ausgeschlossene Arbeit? | Hauptrisiken |
|---|---|---|---|---|
| 5.000 € | Portfolio ≈ 100–330 Titel **oder** wenige Hits; 2 Formate; 2–3 Sprachen | Kataloge ja (B), Hits als Einzelfälle | teils: Pflege und Ausbau übersteigen 5 h/Woche, sobald über 100 aktive Titel beworben werden | Upload-Limit, Werbekosten, Q4-Verzerrung |
| 10.000 € | zusätzlich VA für Upload und Metadaten, externe Satzprüfung | #92315 (Team, ≈ 12.000 $) | Führung und Kontrolle ca. 15 h pro Monat | Kontosperre trifft alles, weil es nur ein Konto gibt |
| 25.000 € | 500–2.000 Titel, mehrere Linien und Sprachen, Werbe-Manager | Prüfungsvorbereitung ≈ 25.000 $ nach 11 Jahren mit 700 Titeln (anderes Segment, Fachwissen) | ja | Werbekosten steigen schneller als Tantiemen |
| 50.000 € | Hit-Serien **oder** anderes Genre mit Leserbindung **oder** weitere Kanäle (Buchhandel, Direktvertrieb) | nur ein Grenzfall bei Belletristik (Übersicht 55.500 $, Jahresschnitt ≈ 37.000 $) | ja, Team | Abhängigkeit von Hits und Plattform; Bewertung mit dem 2,3-Fachen zeigt Risiko |
| 100.000 € | eigene Verlagsstruktur | kein Beleg | ja | – |

**Schaden bei Kontosperre:**
- Bei nur einem Konto (BF) fällt der **gesamte** Umsatz weg.
- Bereits verdiente Tantiemen können einbehalten werden (Forum, Einzelfälle).
- Streuung auf andere Kanäle (IngramSpark, Direktvertrieb) wäre ein Schutz, verlangt aber zusätzliche Arbeit.

**Saison:** Q4 kann das 2- bis 3-Fache bringen (D). Nur Monate außerhalb von November und Dezember zählen als Beleg für die Stufe.

---

## 12. Abschließende Entscheidung

**WAS BEI PROFIS NACHWEISLICH FUNKTIONIERT:**
- Große, über Jahre aufgebaute Kataloge in Nischen mit echter Nachfrage.
- Wenige Titel tragen einen großen Teil.
- Die Arbeit wird mit Freelancern oder Team organisiert.
- Hohe Beträge entstehen mit Leserbindung (Serien, E-Mail-Listen) oder über Fachnischen.
- Geprüft sind im Low-Content-Segment ≈ 12.000 $ Monatsgewinn nach ca. 5 Jahren.

**WELCHE 50K-/100K-GEWINNBEHAUPTUNGEN BELASTBAR SIND:**
- Für Rätsel, Activity und Low-Content: **keine**.
- Ein von Empire Flippers geprüfter Belletristik-Katalog liegt im Jahresschnitt bei ≈ 37.000 $ (Übersicht 55.508 $).
- 100.000 €: nicht belegt.
- Viele „50k“-Angaben sind Umsatz, Einzelmonate oder stammen aus Kurs-, Software- oder Coaching-Einnahmen.

**WAS DAVON FÜR MICH ÜBERTRAGBAR IST:**
- Die maschinell prüfbare Produktion (lokal getestet).
- Die Werbe- und Diagnoseverfahren.
- Der Katalogaufbau in bewährten Linien.
- **Nicht übertragbar:** Jahre des Aufbaus, Team, Serien-Leserbindung, Fachnischen.

**EMPFOHLENES ERSTES PRODUKT:**
„Sudoku Variety Großdruck (Killer, Jigsaw, Klassisch), 100 Rätsel, leicht bis mittel, mit Lösungen“, 8,5 × 11 Zoll, 10,99 netto. Dazu klassisches Sudoku in Großdruck als Vergleichstitel.

**EMPFOHLENER MARKTPLATZ UND SPRACHE:**
Amazon KDP. Dasselbe Produkt auf Englisch (amazon.com und amazon.co.uk) und Deutsch (amazon.de) testen und danach die bessere Kombination ausbauen.

**WAS DIE KI VOLLSTÄNDIG ÜBERNEHMEN KANN:**
- Generator und unabhängige SAT-Prüfung
- Schwierigkeit und Dubletten über alle Bücher
- PDF-Satz und Rückprüfung aus dem PDF
- Cover-Entwürfe, Metadaten-Entwürfe
- Kampagnenaufbau und Auswertung der Werbeberichte
- Buchhaltungsvorbereitung

**WAS ICH PERSÖNLICH TUN MUSS:**
- Freigaben
- Checkliste und Stichprobe (25 min je Titel)
- Testexemplar ansehen
- Upload von Hand mit KI-Angabe
- Werbebudget und wöchentliche Werbeentscheidung (30 min)
- Werbeberichte herunterladen
- Richtlinienmails, Steuerformular, Buchhaltung

**KOSTEN UND ZEIT DES ERSTEN TESTS:**
- ca. 600–650 €: höchstens 500 € Werbung, ca. 60 € KI, ca. 40 € Testexemplare, Rest Puffer
- ca. 8 h pro Monat über 3 Monate, passt in Budget A

**NOTWENDIGE VERKÄUFE FÜR 5.000 € GEWINN:**
ca. 3.000 (stark) bis 4.100 (plausibel) Verkäufe pro Monat bei US-Ökonomie. Bei mehr amazon.de-Anteil etwas weniger, weil die Tantieme höher ist. Im schwachen Szenario ≈ 10.800.

**BEDINGT NOTWENDIGE PORTFOLIO-GRÖSSE:**
- ca. 90 (stark) bis 330 (plausibel) Titel, unter der Annahme realistisch ungleich verteilter Titel
- nicht erreichbar in 6 Monaten: Upload-Limit ≈ 8 pro Monat und Format

**EINSCHÄTZUNG DES SECHSMONATSZIELS: Derzeit nicht ausreichend belegt.**
- Median in Monat 6: plausibel ca. 270 €, stark ca. 940 €.
- 5.000 € erfordern Hits weit über den belegten Werten.
- Monat 12 liegt im Median bei ca. 740 € (plausibel) bzw. 2.460 € (stark). Das sind keine Prognosen.

**VORAUSSETZUNGEN FÜR 50.000 €:**
- Mehrere Hit-Serien oder ein Wechsel in ein Segment mit Leserbindung
- 1.000+ Titel in mehreren Sprachen und Formaten
- ein Team (VA, Qualitätsprüfung, Werbe-Manager)
- Werbekapital von fünfstelliger Höhe pro Monat
- zusätzliche Vertriebskanäle
- Für Rätselbücher gibt es dafür keinen Beleg.

**VORAUSSETZUNGEN FÜR 100.000 €:**
- Eine Verlagsorganisation mit Personal und mehreren Kanälen.
- Nicht belegt, keine Übertragbarkeit auf dein Modell erkennbar.

**AB WANN MEINE ZEITGRENZEN NICHT MEHR EINHALTBAR SIND:**
- **2 h/Woche:** reicht nur für Test und langsamen Ausbau (≈ 3 Titel pro Monat).
- **5 h/Woche:** reicht bis ca. 8 neue Titel pro Monat und ca. 100 aktive Titel.
- Ab etwa **5.000–10.000 € Monatsgewinn** bzw. mehreren hundert beworbenen Titeln brauchst du bezahlte Hilfe und eigene Führungszeit. Das wäre eine Abweichung von deinen Grenzen.

**GRÖSSTE UNBEWIESENE ANNAHME:**
Dass differenzierte Sudoku-Großdruckbücher auf amazon.com, .co.uk oder .de überhaupt profitabel beworben werden können. Konkret: Werbekosten je Werbeverkauf unter ca. 60 % der Tantieme, also unter ≈ 1,70–2,25 €, und eine Verteilung mit Hits.

**DER KONKRETE NÄCHSTE SCHRITT:**
- Mit deiner Freigabe erweitert Claude Code die vorhandene Pipeline [`technik-test/sudoku_pipeline.py`](../technik-test/sudoku_pipeline.py) um Killer- und Jigsaw-Sudoku, Cover-Vorlage und den vollständigen Abnahmetest.
- Du prüfst das Ergebnis anhand der Checkliste und entscheidest dann über ein KDP-Konto und die ersten 2 Uploads.
- Noch kein Konto, kein Upload und keine Werbung ohne deine Freigabe.
