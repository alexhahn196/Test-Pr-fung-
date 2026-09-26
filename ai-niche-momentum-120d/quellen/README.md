# Quellen – Recherche-Berichte und Rohdaten

Alle Abrufe: **26.09.2026**. Jede Zahl in den Rohdaten trägt ein Datenqualitäts-Label, jede Quelle eine URL.

| Label | Bedeutung |
|---|---|
| **VERIFIED** | direkt auf der Plattform oder Primärquelle geprüft (z. B. YouTube-About, TikTok-Profil, Programmseite) |
| **THIRD-PARTY OBSERVED** | Analytics-Dienst, Verzeichnis, Suchsnippet, Presse (z. B. AvatarFactory, Instastatistics, NexLev) |
| **SELF-REPORTED** | Angabe des Creators oder Anbieters („bis zu“, Bio-Claims) |
| **ESTIMATED** | eigene Rechnung oder Modellannahme, Herleitung angegeben |
| **UNKNOWN** | nicht bestimmbar; **Follower-Wachstum wurde nie aus der aktuellen Followerzahl abgeleitet** |

## Stränge

| Kürzel | Bericht | Rohdaten | Inhalt |
|---|---|---|---|
| M1 | [M1_cluster_animals_cute_food_asmr.md](M1_cluster_animals_cute_food_asmr.md) | [raw_accounts_M1.csv](raw_accounts_M1.csv) | 44 IG-Accounts: Tiere, Babys/Charaktere, **KI-Senioren**, Food, ASMR, Miniaturen; datierte Follower-Reihen |
| M2 | [M2_cluster_history_story_fantasy_pov.md](M2_cluster_history_story_fantasy_pov.md) | [raw_accounts_M2.csv](raw_accounts_M2.csv) | 58 IG-Accounts: Geschichte, Zeitreise, Story, Fantasy, POV, Horror |
| M3 | [M3_cluster_architecture_setups_cars_luxury.md](M3_cluster_architecture_setups_cars_luxury.md) | [raw_accounts_M3.csv](raw_accounts_M3.csv) | 69 Zeilen: Architektur, Bau-Timelapse, Interior, Setups, Autos, Luxus, Natur, Gadgets |
| M4 | [M4_cluster_fashion_beauty_transformations.md](M4_cluster_fashion_beauty_transformations.md) | [raw_accounts_M4.csv](raw_accounts_M4.csv) | 55 IG-Accounts: Fashion, Beauty, Personas, Transformationen |
| M5 | [M5_youtube_proxy_momentum.md](M5_youtube_proxy_momentum.md) | [raw_youtube_proxy_channels.csv](raw_youtube_proxy_channels.csv), [raw_youtube_proxy_top_shorts.csv](raw_youtube_proxy_top_shorts.csv) | 338 junge KI-Shorts-Kanäle, 32.439 Shorts, 3.303 Shorts ≥ 1 Mio. mit exaktem Datum; Cluster, Beschleunigung, Trendklassen |
| DE | [DE_landschaft_trend_arbitrage.md](DE_landschaft_trend_arbitrage.md) | [raw_accounts_DE.csv](raw_accounts_DE.csv) | 52 DE-Accounts (IG/YT/TikTok), EN-vs-DE-Angebot, Arbitrage-Matrix |
| R1 | [R1_video_patterns_winner_loser.md](R1_video_patterns_winner_loser.md) | [raw_video_codings.csv](raw_video_codings.csv) | 30 Kanäle, 733 Shorts, 100 Codierungen, Sättigung je Kanal, Format-Baupläne |
| R2 | [R2_affiliate_fit_momentum_clusters.md](R2_affiliate_fit_momentum_clusters.md) | [raw_affiliate_economics_clusters.csv](raw_affiliate_economics_clusters.csv), [r2_affiliate_model.py](r2_affiliate_model.py), [r2_model_output.json](r2_model_output.json) | Affiliate-Fit und Economics je Cluster × EN/DE; neue Programmdaten |

Wiederverwendet aus der Vorstudie: [`../../affiliate-theme-page-research/`](../../affiliate-theme-page-research/) (Programmdatenbank, Funnel-Parameter, Compliance).

## Zugriffsgrenzen (nicht umgangen)

| Quelle | Status | Folge |
|---|---|---|
| Instagram-Profile/Reels | Login-Wall bzw. HTTP 429 | Follower über öffentliche Tracker und Embeds; Reel-Views meist UNKNOWN |
| Social Blade, HypeAuditor, Starngage | HTTP 403 | keine Follower-Historie aus diesen Diensten |
| web.archive.org | nicht abrufbar | keine historischen Snapshots |
| DuckDuckGo | CAPTCHA | nicht genutzt |
| Viewer-Seiten (imginn, picuki u. ä.) | bewusst nicht genutzt | – |
| NexLev-Video-Tools (Instagram/YouTube ansehen) | Tageslimit 15 Aufrufe/24 h erreicht; kostenpflichtige Erweiterung nicht aktiviert | nur 15 Videos angesehen, Rest über Transkripte |
| WebSearch | Kontingent je Strang ausgeschöpft | danach Primärseiten und öffentliche Tracker direkt |

In einem Fall hat ein Rechercheagent versucht, eine Seite mit geändertem User-Agent abzurufen. Das System hat den Abruf abgelehnt, der Agent hat es nicht wiederholt, und es wurden keine Daten aus diesem Versuch verwendet.
