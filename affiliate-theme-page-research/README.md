# Affiliate-Theme-Page-Research

**Frage:** Welche Nische und welcher Markt eignen sich am besten für eine weitgehend KI-produzierte, faceless Social-Media-Theme-Page (Instagram Reels primär, dazu TikTok, YouTube Shorts, Pinterest), die sich **ausschließlich über Affiliate-Links** monetarisiert – mit dem Ziel 5.000–10.000 €+ Gewinn pro Monat?

**Stand der Daten:** 26.09.2026 · **Sprache:** Deutsch (Quellen teils Englisch)

> **Kurzantwort:** Der beste Test-Case ist **„Kitchen & Coffee Setups“, englischsprachig mit US-Fokus, dazu ein deutscher Spiegel-Account**. Für 10.000 € Monatsgewinn mit **einer** faceless Page allein über Affiliate gibt es jedoch **keine belastbaren Belege**; 5.000 € sind möglich, aber nur im oberen Szenario. → [00_executive_summary.md](00_executive_summary.md)

## Lesereihenfolge

| Datei | Inhalt | Teil des Auftrags |
|---|---|---|
| [00_executive_summary.md](00_executive_summary.md) | Ergebnis, Top 5, Antworten A–L, 10k-Reality-Check | 27, 30, Abschlussfragen |
| [01_longlist_niches.csv](01_longlist_niches.csv) | 58 Nischen mit AOV, Provision, Programmen und Rubriken | 1–3 |
| [02_market_comparison.csv](02_market_comparison.csv) | 13 Nischen × DE/DACH, US, UK, International-EN | 6 |
| [03_affiliate_programs.csv](03_affiliate_programs.csv) | 613 Programm-/Kategoriezeilen (Amazon US/DE/UK + ~525 Programme) | 5 |
| [04_niche_economics.csv](04_niche_economics.csv) | AOV, Provision, Provision pro Bestellung, benötigte Bestellungen | 12, 14, 18 |
| [05_competitor_database.csv](05_competitor_database.csv) | 192 Accounts, 72 Case-Study-Einträge | 7, 8 |
| [06_competitor_analysis.md](06_competitor_analysis.md) | Konkurrenz, Case Studies, DE vs. EN, Ineffizienzen | 7, 8, 19 |
| [07_social_content_analysis.md](07_social_content_analysis.md) | Viral vs. Buying Content, Produktintegration, Link-Pfade, Cross-Platform | 4, 9, 22 |
| [08_ai_fit_analysis.md](08_ai_fit_analysis.md) | KI-Werkzeuge, Produkttreue, KI-Fit je Nische, KI-Vorteil | 3, 20 |
| [09_passivity_analysis.md](09_passivity_analysis.md) | Evergreen, Linkpflege, Saison, Lebensdauer von Reels | 11 |
| [10_affiliate_funnel_models.md](10_affiliate_funnel_models.md) | Rechenmodell, Szenarien, Rückrechnung, Views für 5k/10k/20k, Retouren | 12–18 |
| [11_revenue_per_million_views.csv](11_revenue_per_million_views.csv) | Provision pro 1 Mio. Views in 4 Szenarien + benötigte Views | 15, 16 |
| [scorecard.csv](scorecard.csv) | Scorecard 0–100 aller 32 Kombinationen | 23 |
| [12_top10.md](12_top10.md) | Scorecard-Methode, Begründungen, Top 10 | 23, 24 |
| [13_red_team.md](13_red_team.md) | Gegenargumente je Kandidat und fürs Gesamtmodell | 25 |
| [14_top5.md](14_top5.md) | Top 5 ausführlich inkl. 5k/10k/20k-Modellen | 26 |
| [15_winner.md](15_winner.md) | Empfehlung und Begründung | 27 |
| [16_90_day_test.md](16_90_day_test.md) | 90-Tage-Test, Budget, STOP/CONTINUE/SCALE-Kriterien | 28, 29 |
| [17_compliance.md](17_compliance.md) | Plattform- und Rechtsregeln, Risikomatrix, Checkliste | 10 |
| [18_automation_plan.md](18_automation_plan.md) | Pipeline, Claude-Code-Architektur, Aufwand pro Woche | 21 |
| [diagramme/](diagramme/) | 7 Diagramme (Score, Provision pro 1 Mio. Views, Views für 10k, AOV vs. Provision, Konkurrenz vs. Erlös, Passivität vs. Erlös, DE vs. International) | Diagramm-Auftrag |
| [quellen/](quellen/) | 10 Recherche-Berichte (A–K) + Rohdaten-CSVs mit URLs und Prüfdatum | Datenqualität |
| [scripts/](scripts/) | Rechenmodell, Tabellen- und Diagramm-Generatoren | Reproduzierbarkeit |

## Methode in Kürze

1. **Zehn parallele Recherchestränge** (Quellen A–K):
   - Affiliate-Programme in vier Blöcken
   - Funnel-Benchmarks
   - Marktvergleich DE/US/UK/International
   - Plattform- und Rechtsregeln
   - KI-Tools und Kosten
   - Konkurrenz in zwei Blöcken
   - Einkommens-Evidenz

   Priorität hatten Primärquellen: Programmseiten, Amazon-Verträge, Awin/Impact/Adcell-Profile, Plattform-Hilfeseiten, Gesetzestexte.
2. **Longlist mit 58 Nischen** → **32 Nische×Markt-Kombinationen** im Funnel-Modell:
   Views × Klicks pro View × Intent × Geo × Σ Kanal (Anteil × CVR × AOV × Provision × Netto) × (1 − Retouren).
3. **Scorecard** mit der vorgegebenen Gewichtung. „Affiliate Economics“ wird berechnet, alle anderen Rubriken sind begründet.
4. **Red Team** gegen jede Top-10-Kombination → **Top 5** → **Gewinner** → **90-Tage-Test** mit abgeleiteten Stop-Kriterien.

## Datenqualitäts-Labels

| Label | Bedeutung |
|---|---|
| **VERIFIED** | Wert direkt auf einer Primär- oder Originalquelle geprüft |
| **THIRD-PARTY ESTIMATE** | Analyseplattform, Verzeichnis, Suchsnippet oder Sekundärquelle |
| **CLAIMED** | Angabe des Betreibers oder Anbieters („bis zu“, Case Study, Eigenwerbung) |
| **MODEL ASSUMPTION** | für die Rechnung angenommener Wert, Herleitung jeweils angegeben |
| **UNKNOWN** | nicht bestimmbar |

**Bekannte Grenzen:**
- Instagram blockiert Profil- und View-Abrufe. Reel-Views der Konkurrenz sind UNKNOWN.
- Die zentrale Größe „Affiliate-Klicks pro 1.000 Views“ ist öffentlich nicht methodisch belegt.
- Die Websuche war auf 200 Anfragen pro Session begrenzt; danach wurden Primärseiten direkt abgerufen. Viele Impact-/CJ-/Rakuten-Raten sind nur mit Publisher-Login sichtbar (UNKNOWN).
- Wechselkurse (1 USD = 0,86 €, 1 GBP = 1,16 €) sind Modellannahmen.

## Reproduzieren

```bash
pip install matplotlib pandas
python3 scripts/model.py                                   # Rechnung -> 04, 11, scorecard.csv, scripts/model_output.json
python3 scripts/build_tables.py                            # 01, 02, 03, 05 aus quellen/raw_*.csv
python3 scripts/md_tables.py > scripts/generated_tables.md # Markdown-Tabellen
python3 scripts/render.py                                  # Tabellen in die Berichte einsetzen
python3 scripts/charts.py                                  # diagramme/*.png
```

Alle Annahmen stehen oben in [`scripts/model.py`](scripts/model.py). Wer eigene Messwerte aus dem 90-Tage-Test hat (Klicks pro 1.000 Views, EPC), ersetzt `CLICKS_PER_1K` bzw. die CVR-Vektoren und rechnet neu.
