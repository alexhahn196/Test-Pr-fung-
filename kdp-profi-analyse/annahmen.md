# Modellannahmen

Alle Werte stehen in `kdp_modell.py` und lassen sich dort ändern. Außer den Plattformwerten aus [quellen.md](quellen.md) (BF) ist **jede Zahl eine Annahme**.

## Plattformwerte (belegt)

| Parameter | Wert | Beleg |
|---|---|---|
| Druckkosten Large Trim s/w, amazon.de | 0,75 € + 0,016 € je Seite | BF, KDP |
| Druckkosten Large Trim s/w, amazon.com | 1,00 $ + 0,017 $ je Seite | BF, KDP |
| Tantiemensatz | 60 % ab 9,99 netto, sonst 50 % | BF |
| Auszahlung | etwa 2 Monate verzögert | BF |
| Neue Titel | höchstens 2 je Format und Woche, im Modell 8 pro Monat | BF |
| Konten | nur ein KDP-Konto | BF |

## Produkt

| Parameter | Wert | Art |
|---|---|---|
| Format | 8,5 × 11 Zoll (Large Trim), 130 Seiten, 100 Rätsel plus Lösungsteil | MA |
| Listenpreis | 10,99 netto (€ bzw. $) | MA, knapp über der 60-%-Schwelle |
| Wechselkurs | 1 $ = 0,86 € | MA |
| Rückgaben und Verrechnungen | 2 % | MA |

## Portfolio-Verteilung

Stabile Monatsverkäufe je Titel nach der Anlaufphase. Angegeben ist jeweils der Anteil der Titel mit den Verkäufen pro Monat.

| Szenario | Hit | Mittel | Klein | Null |
|---|---|---|---|---|
| schwach | 2 % mit 60 | 15 % mit 12 | 43 % mit 3 | 40 % mit 0,3 |
| plausibel | 5 % mit 120 | 20 % mit 20 | 45 % mit 5 | 30 % mit 0,5 |
| stark | 8 % mit 250 | 25 % mit 35 | 42 % mit 8 | 25 % mit 1 |

Die Klasse wird pro Titel zufällig gezogen (Monte-Carlo über 300 Läufe).

**Worauf die Werte beruhen:**
- Praktikerangaben zur 80/20-Verteilung (SCH).
- Katalogwerte geprüfter Inserate von etwa 30–75 $ Gewinn je Titel und Monat (Prüfungsvorbereitung mit 700 Titeln, KI-Belletristik mit 500 Titeln).
- Einzelberichte mit etwa 12 Verkäufen je Titel und Monat.

**Nicht belegt** sind die Anteile und die Hit-Höhen für deutschsprachige Rätselbücher.

## Verlauf je Titel

| Parameter | Wert |
|---|---|
| Anlauf | 20 %, 50 %, 80 %, dann 100 % |
| Nachlassen | ab Monat 9 um 2 % pro Monat |
| Kannibalisierung | Faktor 1 / (1 + 0,10 × (Titel in derselben Linie − 1)), 10 Titel je Linie |
| Einstellen | Titel der Klasse „null“ ab Monat 4 (keine Werbung mehr) |

**Saison** (Kalendermonat, Start im Oktober):

| Monat | Jan | Feb | Mär | Apr | Mai | Jun | Jul | Aug | Sep | Okt | Nov | Dez |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Faktor | 0,8 | 0,85 | 0,9 | 0,9 | 0,9 | 0,85 | 0,85 | 0,9 | 1,0 | 1,2 | 1,8 | 2,2 |

Das ist eine Schätzung auf Basis der Praktikerangabe „Q4 = 2- bis 3-mal so viel“.

## Werbung

| Parameter | Wert |
|---|---|
| Anteil werbezugerechneter Verkäufe | 55 % |
| Kosten je Werbeverkauf bei kleinem Volumen (schwach / plausibel / stark) | 3,00 € / 2,20 € / 1,60 € |
| Anstieg der Kosten | +25 % je Verzehnfachung des Werbevolumens |
| Werbetest | 250 € pro Monat in Monat 1 und 2 |

**Einordnung der Werbewerte:**
- **Obergrenze je Werbeverkauf** ist die Tantieme: 3,76 € auf amazon.de, 2,91 € auf amazon.com.
- **Praktikerwert:** 0,38 $ pro Klick bei 18 % Kaufquote ergäben etwa 2,10 $ je Werbeverkauf (SCH, nicht nach Ländern getrennt).
- **Zusätzliche Verkäufe durch Werbung** sind im Modell **nicht** gesondert erfasst. Die Werbezuordnung wird also nicht als Beweis für Zusatzverkäufe behandelt.

## Zeit (deine Stunden)

| Parameter | Wert |
|---|---|
| Je neuem Titel | 1,5 h (Prüfung 25 min, Metadaten 10 min, Upload 25 min, Rest) |
| Fixaufwand pro Monat | 3,5 h (Werbeentscheidungen 4 × 30 min, Verwaltung, Mails) |
| Portfolio-Kontrolle | 0,3 h je 10 aktive Titel |
| Budget A | 8,66 h pro Monat |
| Budget B | 21,65 h pro Monat |
| Wert einer Stunde | 25 € |

## Kosten

| Parameter | Wert |
|---|---|
| Fixkosten | 45 € pro Monat (Claude Pro, Buchhaltungswerkzeug, Konto) |
| Startkasse | 2.500 €; Varianten 1.000 € und 5.000 € im Text |

**Variante B mit Team** (alles SCH):

| Posten | Wert |
|---|---|
| Virtueller Assistent | ca. 15 $/h, 1 h je Titel |
| Satz- und Qualitätsprüfung | 40 €/h, 0,5 h je Titel |
| Werbe-Manager ab 150 aktiven Titeln | 800 € pro Monat |
| Deine Führungsarbeit | ca. 12 h pro Monat |

## Plausibilitätsprüfungen

Aufruf mit `python3 kdp_modell.py --test`. Geprüft wird:
- Tantieme stimmt mit der Handrechnung überein
- 50-%-Regel unter 9,99
- Kosten je Werbeverkauf steigen mit dem Volumen
- Zeitbudgets A und B werden in keinem Monat überschritten
- Upload-Limit wird eingehalten
- Auszahlung ist verzögert
