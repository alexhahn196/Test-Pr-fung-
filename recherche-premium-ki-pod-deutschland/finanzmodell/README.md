# Finanzmodell

Reproduzierbares Modell für die Stückrechnung, CAC-Szenarien und die Skalierung auf 250.000 € bis 5 Mio. € Jahresnettoumsatz.

```bash
cd finanzmodell
python3 berechnen.py     # schreibt ergebnisse.md, ergebnisse.json, cac_matrix.csv, skalierung.csv
```

Nur Python-Standardbibliothek, keine Abhängigkeiten.

| Datei | Inhalt |
|---|---|
| `modell.py` | Rechenkern: `einheit()` (Stückrechnung je Bestellung), `cac_matrix()` (Gewinn je Neukunde bei CAC 20–150 €), `skalierung()` (Bestellungen pro Jahr/Monat/Tag, DB I, Kundengewinnung, Fixkosten, operatives Ergebnis je CAC), `sensitivitaet()`, `testbudget()` |
| `parameter.py` | Eingaben: gemeinsame Annahmen (Zahlung, Beilage, Infrastruktur, Stundensatz, Fixkostenstufen, Gründerlohn), Szenario-Hebel, Vergleich aller 10 Shortlist-Kandidaten (Prüfereingaben aus `rohdaten/vertiefung-batch*.json`), Neuzuschnitt der 4 stärksten (`rohdaten/neuzuschnitt.json`), Finalist und Reserve, Testrechnung |
| `berechnen.py` | erzeugt die Ergebnisdateien |
| `ergebnisse.md` | lesbare Ergebnisse inkl. Parametertabelle mit Kennzeichnung |
| `cac_matrix.csv`, `skalierung.csv` | Maschinenlesbare Tabellen (inkl. Ergebnis nach Gründerlohn) |

**Rechenlogik in Kürze:**

- Nettoumsatz = Warenkorb brutto ÷ 1,19. Warenkorb = Angebots-Mix × Preis + Upsell-Quote × Upsell-Preis.
- DB I = Nettoumsatz − Produktion − Versand − Verpackung/Beilage − Zahlungsgebühren − KI der Nichtkäufer (Kosten je Vorschau × (1 − Quote) ÷ Quote) − KI der Käufer − Infrastruktur − Prüfung und Support (Minuten × Stundensatz) − Nachdruck (Quote × Herstell- und Prüfkosten) − Erstattung (Quote × Netto).
- Max. tragbarer CAC = Break-even-CAC = DB I der Erstbestellung; mit Folgekäufen: DB I × (1 + Folgebestellungen × DB-Faktor).
- Skalierung: Neukunden = Zielumsatz ÷ Nettoumsatz je Kunde (inkl. Folgekäufe); Ergebnis = DB I gesamt − Neukunden × CAC − Fixkosten der Umsatzstufe. Werbung wird nur einmal gebucht (als CAC).
- Ergebnis = operativ vor Ertragsteuern und vor Gründerlohn; nach Gründerlohn in `skalierung.csv`.

Alle ergebnisbestimmenden Eingaben (Preise, Mix, Vorschau→Kauf, CAC, Folgekäufe, Prüfminuten, Fixkosten) sind ANNAHMEN; belegt sind vor allem Einkaufs- und Versandpreise der Partner. Neue Messwerte aus dem Test einfach in `parameter.py` eintragen und neu rechnen.
