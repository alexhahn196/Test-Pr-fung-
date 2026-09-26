# AI-Niche-Momentum 120 Tage

**Frage:** Welche KI-produzierbaren Instagram-Nischen zeigen **jetzt** (letzte 30–120 Tage) außergewöhnliches organisches Momentum, und welche davon haben gleichzeitig genug Kaufintention und Affiliate-Economics für ein Theme-Page-Business?

**Stand der Daten:** 26.09.2026 · **Vorstudie:** [`../affiliate-theme-page-research/`](../affiliate-theme-page-research/)

> **Kurzantwort:**
> - Viral sind vor allem Story-Serien, Fußball-Sketche, Marvel-What-ifs und Kids-Figuren. Sie haben keine Kaufintention.
> - Momentum *und* Affiliate-Logik zeigt nur die **KI-Seniorin, die echte Rezepte kocht** (Instagram-Sprünge +18 % bis +168 % in 9–16 Tagen, September 2026).
> - Empfehlung: EN/US-Test plus DE-Spiegel, Entscheidung nach 30 Tagen.
> - → [00_executive_summary.md](00_executive_summary.md)

## Lesereihenfolge

| Datei | Inhalt | Teil des Auftrags |
|---|---|---|
| [00_executive_summary.md](00_executive_summary.md) | Ergebnis, Rankings, Top 5, Reality Check | – |
| [01_200_accounts.csv](01_200_accounts.csv) | 616 Accounts/Kanäle mit allen Momentum-Feldern | 1–7 |
| [02_verified_ai_accounts.csv](02_verified_ai_accounts.csv) | 235 Accounts mit KI-Status VERIFIED | 3 |
| [03_30_day_growth.csv](03_30_day_growth.csv) · [04_90_day_growth.csv](04_90_day_growth.csv) | nur datierte Follower-Werte (sonst UNKNOWN) | 5 |
| [05_niche_clusters.md](05_niche_clusters.md) | 22 Cluster, Trendklassen, Treiber, Emerging Outliers | 6, 8, 9, 12 |
| [06_momentum_scores.csv](06_momentum_scores.csv) | Momentum-Score je Cluster mit Teil-Scores | 19 |
| [07_top_reels.csv](07_top_reels.csv) | 3.368 Reels/Shorts mit Datum und Views | 5, 10 |
| [08_video_patterns.md](08_video_patterns.md) · [09_winner_vs_loser.md](09_winner_vs_loser.md) | Video-Reverse-Engineering, Top 20 % vs. Bottom 50 % | 10, 11 |
| [10_affiliate_fit.md](10_affiliate_fit.md) · [11_affiliate_economics.csv](11_affiliate_economics.csv) | Produktlogik, Purchase Intent, Economics, Matrix | 13–16 |
| [12_de_vs_international.md](12_de_vs_international.md) · [13_trend_arbitrage.md](13_trend_arbitrage.md) | Märkte, Arbitrage, eigene Formate | 17, 18, 25 |
| [14_combined_scores.csv](14_combined_scores.csv) | Business- und Combined-Score | 20, 21 |
| [15_top10_momentum.md](15_top10_momentum.md) · [16_top10_business.md](16_top10_business.md) | Rankings | 22, 23 |
| [17_top5_opportunities.md](17_top5_opportunities.md) | 5 konkrete Opportunities | 24, 25 |
| [18_accounts_to_watch.md](18_accounts_to_watch.md) | ≥ 5 Accounts je Top-Nische | 26 |
| [19_recommendation.md](19_recommendation.md) | Empfehlung, Testkriterien, Reality Check | 27, Endziel |
| [diagramme/](diagramme/) | Virality × Affiliate-Matrix, 30-Tage-Momentum | 15 |
| [quellen/](quellen/) | 8 Rohberichte, Rohdaten, Zugriffsgrenzen | 29, 30 |
| [scripts/](scripts/) | Score-Modell, Diagramme, Watchlist | Reproduzierbarkeit |

## Reproduzieren

```bash
pip install matplotlib
python3 scripts/score.py                  # 01–04, 06, 07, 11, 14 und scripts/score_output.json
python3 scripts/charts.py                 # diagramme/*.png
python3 scripts/watchlist.py              # 18_accounts_to_watch.md
python3 quellen/r2_affiliate_model.py     # Affiliate-Economics je Cluster (R2)
```
