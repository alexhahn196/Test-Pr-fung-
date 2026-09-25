# Instagram Interior / Luxury Homes / AI Architecture: Research-Playbook

**Stand der Daten: 25.09.2026.** Datenbasiertes Markt-, Konkurrenz- und Content-Playbook für einen neuen, internationalen,
englischsprachigen Instagram-Account mit überwiegend KI-generierten Bildern und Reels (Luxury Interiors, Future Homes,
Architektur). Ziel war ausdrücklich **nicht**, die Ursprungsidee zu bestätigen, sondern die beste datenbasierte
Positionierung zu finden.

> **Kurzfazit:** Die Nische ist groß. Das Ursprungskonzept „KI-Luxus-Interiors“ (Schlaf- und Wohnzimmer, Küchen im
> weichen „dreamy“-KI-Look) ist in den Daten aber der **schwächste** KI-Teilbereich. Stärker schneiden
> **unmögliche, konzeptionelle Architektur** ab (≈2,3× über Erwartung) sowie Außenräume, Bäder und Treppen, Choice-Formate
> (≈5,7× mehr Kommentare) und eine **Studio-/Creator-Identität statt Theme-Page**. Empfohlen wird deshalb das Konzept
> **K1 *The Unbuilt*** (Arbeitstitel): ein AI-Architektur-Studio für *„Homes that shouldn't exist (yet)“* mit den Serien
> `UNBUILT`, `PICK ONE`, `FROM NOTHING` und `AFTER DARK`. Alle Muster sind Korrelationen unter Top-Reels und werden im eigenen
> 30-Tage-Test geprüft. Details: [00_executive_summary.md](00_executive_summary.md).

---

## 1. Wo finde ich was? (Teil 1–35 → Datei)

| Teil | Thema | Datei |
|---|---|---|
| 35 | Abschließende Entscheidung (A–N) | [00_executive_summary.md](00_executive_summary.md) |
| 1 | Ist die Nische attraktiv? | [01_market_analysis.md](01_market_analysis.md) |
| 2 | 111 Accounts, davon 72 tief profiliert (Rohdaten mit Status je Feld) | [02_competitor_database.csv](02_competitor_database.csv) |
| 2, 3, 4, 20 | Account-Überblick, Top-20-Shortlist, Outperformance-Accounts, Monetarisierung der Top-Accounts | [03_competitor_analysis.md](03_competitor_analysis.md) |
| 4–18 | Reel-Datenbank (2.498 Reels) | [04_reel_database.csv](04_reel_database.csv) |
| 7, 8, 11, 12, 13, 14, 15 | Video-Aufbau, Audio (§2.6), erste Sekunden, Länge, Frequenz, Viralitätsstufen, Gewinner vs. Verlierer | [05_viral_patterns.md](05_viral_patterns.md) |
| 5, 6, 16, 17, 18 | Szenen, Stile, Farben/Materialien, Themen-Rankings, Fantasy vs. realistisch | [06_visual_styles.md](06_visual_styles.md) |
| 8, 9, 10, 25, 26 | Hook-Analyse, Caption-Analyse (§2.10), 50 eigene Text-Hooks, 34 eigene visuelle Hooks | [07_hooks.md](07_hooks.md) |
| 24 | Content Pillars P1–P5 und Reserve P6 (Serien `UNBUILT`, `PICK ONE`, `FROM NOTHING`, `AFTER DARK`, `THE ROOM`) | [08_content_pillars.md](08_content_pillars.md) |
| 19, 20 | Möbel-Affiliate-Konkurrenz, Monetarisierung der Konkurrenz, eigene Monetarisierungs-Roadmap | [09_monetization.md](09_monetization.md) |
| 21, 22 | 22 geprüfte Micro-Niches (GO/TEST/WATCH/REJECT), 5 Account-Konzepte, Empfehlung K1 *The Unbuilt* | [10_market_gaps.md](10_market_gaps.md) |
| 23 | Eigener Style Guide (Marke *The Unbuilt*, Arbeitstitel) | [11_brand_style_guide.md](11_brand_style_guide.md) |
| 27 | 100 Content-Ideen (35/20/20/15/10 auf P1–P5) | [12_100_content_ideas.csv](12_100_content_ideas.csv) |
| 28 | Testing-Matrix (27 Tests) | [13_testing_matrix.csv](13_testing_matrix.csv) |
| 29 | 30-Tage-Launchplan (KEEP / ITERATE / SCALE / KILL) | [14_30_day_launch_plan.md](14_30_day_launch_plan.md) |
| 30, 31 | KPI-System, Winner-Database | [15_kpi_framework.md](15_kpi_framework.md), [data/winner_database_template.csv](data/winner_database_template.csv), [data/winner_database_schema.sql](data/winner_database_schema.sql), [scripts/winner_analysis.py](scripts/winner_analysis.py) |
| 32 | Automatisierbarkeit | [16_automation_strategy.md](16_automation_strategy.md) |
| 33 | Konkurrenzmonitor | [17_competitor_monitor.md](17_competitor_monitor.md), [scripts/monitor/](scripts/monitor/), Beispiel-Report [data/monitor/2026-W39_baseline/](data/monitor/2026-W39_baseline/report.md) |
| 34 | Quellen und Quellenqualität | [quellen/README.md](quellen/README.md), `quellen/q01–q09` |
| — | Grafiken | [charts/](charts/) (60 PNGs) |
| — | Alle Kennzahlen an einem Ort | [data/processed/analysis_digest.md](data/processed/analysis_digest.md) |
| — | Erhebungs-Workflows (Topic-Sweep, Embeds, Codierung, Profile, YouTube, Research, Schreiben) | [scripts/workflows/](scripts/workflows/) |
| — | Kernkontraste mit 95-%-Bootstrap-KI und Mann-Whitney-p | [data/processed/stats/key_contrasts.csv](data/processed/stats/key_contrasts.csv) |
| — | Interne Strategie-Synthese (Leitplanken für alle Dokumente) | [data/processed/strategy_brief.md](data/processed/strategy_brief.md) |

### Weitere Dateien (Daten, Statistik-Tabellen, Skripte)

| Pfad | Inhalt | erzeugt von |
|---|---|---|
| `data/raw/` | Rohdaten: Topic-Batches, Embed-Lookups, codierte Reels, Reliabilitäts-Stichprobe, Profile, YouTube | Erhebungs-Agenten (einmalig, siehe Compliance-Hinweis) |
| `data/processed/*.csv` | u. a. `topic_reels.csv`, `reels_unique.csv`, `accounts_followers.csv`, `reels_cover_coded.csv`, `accounts_metrics.csv`, `youtube_shorts.csv`, [shortlist_scores.csv](data/processed/shortlist_scores.csv) | `parse_*.py`, `analyze.py`, `youtube_proxy.py`, `shortlist.py` |
| `data/processed/stats/seg_*.csv`, `summary.json`, `themes.csv`, `topics.csv`, `within_account_*`, `tier_feature_shares.json` | Segment-Statistiken je Dimension, Kruskal-Wallis-Tests, Vergleich innerhalb von Accounts | [scripts/analyze.py](scripts/analyze.py) |
| [stats/freshness_by_group.csv](data/processed/stats/freshness_by_group.csv) | Anteil junger Top-Reels (≤ 180 Tage) und deren adj je Topic-Gruppe | [scripts/analyze.py](scripts/analyze.py) |
| [stats/key_contrasts.csv](data/processed/stats/key_contrasts.csv) (dazu `key_contrasts.txt` als Textfassung) | Kernkontraste (Median-Verhältnis, Bootstrap-KI, Mann-Whitney) | [scripts/key_contrasts.py](scripts/key_contrasts.py) |
| `stats/hooks_*.csv` | Caption- und Cover-Hooks, YouTube-Titel-Hooks (07) | [scripts/hooks_analysis.py](scripts/hooks_analysis.py) |
| `stats/pillar_benchmarks.csv`, `ai_segments.csv`, `ai_style_contrasts.csv` | Pillar-Proxys und KI-only-Segmente (08, 11) | [scripts/pillar_style_stats.py](scripts/pillar_style_stats.py) |
| `stats/micro_niches.csv`, `topic_freshness.csv`, `micro_niches_summary.json` | Micro-Niche-Screening (10) | [scripts/micro_niches.py](scripts/micro_niches.py) |
| `stats/monetization_*.csv` | strikte Monetarisierungs-Flags der 72 Profile, Commerce-Kontraste (09) | [scripts/monetization_stats.py](scripts/monetization_stats.py) |
| `stats/yt_*.csv` | YouTube-Proxy: Länge, Bildwechsel, Titel-Hooks | [scripts/youtube_proxy.py](scripts/youtube_proxy.py) |
| [stats/reliability.csv](data/processed/stats/reliability.csv) | Codier-Reliabilität (Cohen's κ) | [scripts/reliability.py](scripts/reliability.py) |
| `scripts/cover_codebook.md`, `scripts/reel_codebook_prompt.txt` | Codebücher für Cover- und Video-Codierung | – |
| [scripts/qa_checks.py](scripts/qa_checks.py) | QA: defekte relative Links in allen `.md`-Dateien und Originalitätsprüfung der eigenen Hooks/Ideen gegen alle beobachteten Captions und Cover-Texte | – |
| [scripts/winner_analysis.py](scripts/winner_analysis.py), [data/winner_database_template.csv](data/winner_database_template.csv), [data/winner_database_schema.sql](data/winner_database_schema.sql) | Winner-Datenbank des eigenen Accounts und Wochenanalyse (15) | – |
| [scripts/monitor/](scripts/monitor/): `monitor_weekly.py`, `build_watchlists.py`, `watchlist_topics.csv`, `watchlist_competitors.csv`, `monitor_workflow_prompt.md`, `weekly_monitor.workflow.js`, `routine_prompt.txt` | Wöchentlicher Konkurrenzmonitor (17): Auswertung, Watchlists (57 Topics, 40 Handles), Agent-Workflow; Erhebung nur per Graph API, manuell oder mit schriftlicher Erlaubnis | – |
| `data/monitor/` | Baseline-Lauf `2026-W39_baseline/` (Report, Alerts, Tabellen) und Vorlage `inspiration_board.csv` | `monitor_weekly.py` |

---

## 2. Methodik in Kürze

**Warum so?** Instagram-Profilseiten sind ohne Login gesperrt bzw. rate-limitiert (HTTP 429). Login-Sperren und technische
Schutzmaßnahmen umgehen wir nicht. Wir haben daher ausschließlich **öffentlich zugängliche** Seiten genutzt:

| Schritt | Quelle / Methode | Ergebnis | Status |
|---|---|---|---|
| 1. Topic-Sweep | Öffentliche Instagram-Themenseiten `instagram.com/popular/<thema>/` (264 Slugs, 239 erfolgreich) zeigen je ~12 Top-Reels mit **Views** und die Gesamtzahl der Reels zum Thema | 2.863 Reel-Einträge, **2.498 eindeutige Reels**, 1.985 Accounts | Views **VERIFIED** (öffentlich angezeigt, gerundet) |
| 2. Embed-Seiten | `instagram.com/reel/<code>/embed/captioned/` (öffentlich für Einbettungen) | Follower, Posts, exakte Likes, Kommentare, Caption, Cover-URL | **VERIFIED** (Follower gerundet, Stand Abruf) |
| 3. Posting-Zeit | Aus dem Shortcode dekodiert (Media-ID enthält 41-bit-Millisekunden-Zeitstempel; [scripts/shortcode_time.py](scripts/shortcode_time.py), gegen bekannte Daten geprüft) | Exaktes UTC-Datum/-Uhrzeit jedes Reels, Alter, Konto-Mindestalter | **VERIFIED** (abgeleitet) |
| 4. Visuelle Codierung | Cover-Frame vom Instagram-CDN + Caption, codiert von multimodalen Agenten nach festem Codebuch ([scripts/cover_codebook.md](scripts/cover_codebook.md)) | 2.393 Reels mit Raum, Stil, Farben, Materialien, Licht, Realismus, KI/real, Hooks, CTA … | **ESTIMATED**; Reliabilität: 36 Reels unabhängig doppelt codiert, Cohen's κ 0,63–1,0 ([stats/reliability.csv](data/processed/stats/reliability.csv)) |
| 5. Video-Analyse | NexLev „watch_instagram_video“ (Gemini) | Nur **7 Reels**, da auf 15 Aufrufe/Tag begrenzt | ESTIMATED |
| 6. Cross-Platform-Proxy | NexLev YouTube-Daten: 12 relevante Faceless-Interior/Home-Kanäle, 713 Shorts, 219 mit Dauer | Länge, Bildwechsel (Pixel-Differenz der Auto-Thumbnails), Titel-Hooks | **PROXY**, keine Instagram-Daten |
| 7. Account-Profile | 72 Accounts: Threads-Bios, Link-in-Bio-Seiten, Embeds, öffentliche Posts | Bio, Links, Angebote, Brand Deals, Content-Modus | VERIFIED wo URL angegeben, sonst UNKNOWN |
| 8. Desk Research | 9 Recherche-Notizen mit automatisiertem Faktencheck | Plattformregeln, Affiliate, Sponsoren, Trends, Wettbewerberlisten, Case Studies, Recht, Cross-Platform, Benchmarks | Status-Tags je Aussage |

### Kennzahlen

- `views`: öffentlich angezeigte Views auf der Topic-Seite (gerundet, z. B. „3.7M“).
- `vpf` = Views ÷ Follower (Follower beim Abruf; bei älteren Reels waren es meist weniger → vpf eher konservativ).
- `topic_index` = Views ÷ Median-Views derselben Topic-Seite (1,0 = typisch).
- **`adj_factor` (Hauptmetrik):** Views relativ zur Erwartung für die Followerzahl des Accounts auf derselben Topic-Seite.
  Grundlage ist eine Regression log10(Views) ~ log10(Follower) innerhalb jeder Topic-Seite mit Steigung ≈0,47.
  1,0 = wie erwartet, 2,0 = doppelt so viele. Warum? Die Followerzahl ist der stärkste Einzeltreiber (Spearman ρ≈0,43).
  Ohne diese Kontrolle würden große Accounts jede Kategorie dominieren.
- Viralitätsstufen: NORMAL <0,5× Follower · GOOD 0,5–2× · VERY GOOD 2–5× · VIRAL 5–20× · EXTREME OUTLIER ≥20×.
- Signifikanz: Kruskal-Wallis je Dimension und Mann-Whitney für Kernkontraste mit 95-%-Bootstrap-KI
  ([stats/key_contrasts.csv](data/processed/stats/key_contrasts.csv)).

### Wichtigste Einschränkungen (bitte beim Lesen beachten)

1. **Selektionsbias:** Topic-Seiten zeigen Top-Reels. Die Daten sagen, was *unter erfolgreichen Reels* besser oder schlechter
   läuft, nicht was ein durchschnittlicher neuer Post erreicht. Absolute View-Zahlen sind keine Prognose.
2. **Korrelation ≠ Kausalität:** Alle Muster sind Hypothesen, die die [Testing-Matrix](13_testing_matrix.csv) prüft.
3. **Nicht öffentlich messbar:** Reel-Länge, Kamerafahrten, Audio und die ersten 1–2 Sekunden auf Instagram
   (nur Cover-Frame-, NexLev- und YouTube-Proxy). Dazu Saves, Shares, Watch Time und Follows pro Reel.
4. **„Letzte 20 Reels je Account“** waren ohne Login nicht abrufbar. Der Vergleich innerhalb eines Accounts (Teil 15) nutzt deshalb
   Accounts mit ≥5 Reels in der Topic-Stichprobe (25 Accounts, 172 Reels).
5. **WebSearch-Budget** (200 Suchen/Sitzung) war während der Recherche erschöpft. Einige Bios und Monetarisierungsdetails
   sind deshalb UNKNOWN (nicht beobachtet ≠ nicht vorhanden).
6. Codierung per KI-Agenten = ESTIMATED; Reliabilität gemessen (s. o.), `shoppability` ist mit κ 0,63 am schwächsten.

### Compliance-Hinweis zur Datenerhebung (bitte lesen)

Die `robots.txt` von instagram.com sperrt alle User-Agents (`Disallow: /`). Wortlaut: *„Collection of data on Instagram
through automated means is prohibited unless you have express written permission from Instagram.“* Stand 25.09.2026,
Details in [17_competitor_monitor.md](17_competitor_monitor.md), Abschnitt 2.1.

Die Erhebung dieser Studie war eine **einmalige, agentengestützte Stichprobe**. Sie umfasste einige tausend Abrufe
öffentlicher Seiten, jeweils ohne Login, Tokens, inoffizielle Endpunkte oder Umgehung von Rate-Limits. Das ändert nichts
daran, dass automatisierte Erhebung laut Instagram eine Erlaubnis voraussetzt. Daraus folgt:

1. Die Rohdaten nur **intern** für Strategiezwecke nutzen, nicht veröffentlichen oder weitergeben. Handles natürlicher
   Personen sind personenbezogene Daten (DSGVO: Datenminimierung, Löschkonzept).
2. Wiederkehrendes Monitoring **nicht** als automatischen Web-Sweep betreiben, sondern über die offizielle
   **Instagram Graph API (Business Discovery)** mit dem eigenen Business-Account, manuell oder nur mit schriftlicher
   Erlaubnis. Der Monitor erzwingt diese Modi.
3. Eine rechtliche Prüfung (Nutzungsbedingungen, Datenbankrecht, DSGVO) steht aus. Diese Studie ist keine Rechtsberatung,
   siehe auch [q07](quellen/q07_legal_ai_risk.md).

---

## 3. Datenwörterbuch (Kurzfassung)

**[04_reel_database.csv](04_reel_database.csv)**: eine Zeile pro Reel (2.498).
- Identität: `shortcode`, `url`, `handle`, `posted_at_utc`, `age_days`, `post_year`, `post_hour_utc`, `post_weekday`
- Performance: `views`, `views_text`, `followers`, `vpf`, `tier`, `likes`, `comments`, `likes_per_view`, `comments_per_view`,
  `comments_per_like`, `views_per_day`, `topic_index`, `topic_pct`, `adj_resid` (log10), `adj_factor`
- Kontext: `topics`, `topic_groups`, `primary_group`, `n_topics`, `location_any` (Caption oder Topic), `location`,
  `location_from_topic`, `follower_bucket`
- Codes (Cover + Caption, ESTIMATED): `room_primary`, `rooms_visible`, `building_type`, `landscape`, `style_primary`,
  `style_secondary`, `palette_temp`, `brightness`, `dominant_colors`, `materials`, `lighting`, `ambience_fx`,
  `view_through_window`, `people_present`, `cover_text`, `cover_hooks`, `realism`, `production`, `production_evidence`,
  `shoppability`, `visual_quality`, `notable`, `caption_hook_category`, `caption_first_line`, `cta_type`, `location_claimed`,
  `price_claimed`, `ai_disclosed`, `account_kind_hint`, `language`
- Caption-Features: `caption_full`, `caption_len`, `caption_hashtags`, `caption_emojis`, `caption_mentions`,
  `caption_has_question`, `caption_link_hint`, `caption_comment_cta`
- Status: `status_views`, `status_followers`, `status_codes`, `meta_status`, `visual_status`, `followers_source`

**[02_competitor_database.csv](02_competitor_database.csv)**: eine Zeile pro Account (72 tief profiliert, dazu Topic-Stichprobe
und Accounts aus Drittanbieter-Rankings). Jedes Kernfeld hat eine eigene `*_status`-Spalte (VERIFIED / ESTIMATED /
THIRD-PARTY / UNKNOWN). Weitere Felder: Posting-Frequenz (Obergrenze), frühester bekannter Post (Mindestalter), Bio, CTA,
Links, Link-in-Bio-Angebote und `has_affiliate`, `has_brand_deals`, `has_shop`, `has_services`, `has_digital_products`,
`has_newsletter`.

---

## 4. Reproduzieren / aktualisieren

```bash
pip install pandas numpy scipy matplotlib
cd instagram-interior-research
python3 scripts/parse_topics.py        # Topic-Seiten → data/processed/topic_reels.csv, reels_unique.csv
python3 scripts/parse_accounts.py      # Follower-Lookups
python3 scripts/parse_reels.py         # codierte Reels
python3 scripts/analyze.py             # 04_reel_database.csv, Segment-Statistiken, adj_factor, Frische
python3 scripts/key_contrasts.py       # Kernkontraste mit Bootstrap-KI
python3 scripts/youtube_proxy.py       # YouTube-Proxy (Länge, Bildwechsel, Titel-Hooks)
python3 scripts/reliability.py         # Codier-Reliabilität
python3 scripts/build_competitor_db.py # 02_competitor_database.csv
python3 scripts/shortlist.py           # Top-20-Scoring
python3 scripts/hooks_analysis.py      # stats/hooks_*.csv (07)
python3 scripts/pillar_style_stats.py  # stats/pillar_benchmarks.csv, ai_segments.csv, ai_style_contrasts.csv (08, 11)
python3 scripts/micro_niches.py        # stats/micro_niches.csv, topic_freshness.csv (10)
python3 scripts/monetization_stats.py  # stats/monetization_*.csv (09)
python3 scripts/digest.py              # data/processed/analysis_digest.md
python3 scripts/charts.py              # charts/*.png
python3 scripts/qa_checks.py           # QA: Links und Originalität der eigenen Hooks/Ideen
python3 scripts/monitor/build_watchlists.py   # Watchlists des Konkurrenzmonitors (17)
```

Die Wochenanalyse des eigenen Accounts läuft mit `python3 scripts/winner_analysis.py <winner_db.csv>` (Format:
[data/winner_database_template.csv](data/winner_database_template.csv)), der Konkurrenzmonitor mit
`python3 scripts/monitor/monitor_weekly.py <Wochenordner> --prev <Vorwoche>` (Details in
[17_competitor_monitor.md](17_competitor_monitor.md), Abschnitt 5).

Rohdaten liegen in `data/raw/` (Topic-Batches, Embed-Lookups, codierte Reels, Profile, YouTube). Cover-Bilder werden bewusst
**nicht** gespeichert, weil sie urheberrechtlich geschützte Werke Dritter sind. Die einmalige Datenerhebung lief über
Claude-Code-Agenten mit WebFetch. Wiederkehrendes Monitoring läuft **nicht** so, sondern über die offizielle Graph API (Business
Discovery), manuell oder nur mit schriftlicher Erlaubnis; die drei Modi und ihre Regeln stehen in
[17_competitor_monitor.md](17_competitor_monitor.md), Abschnitt 2 (siehe Compliance-Hinweis oben).

## 5. Grundsatz

Wir kopieren keine Creatives. Beobachtete Hooks und Captions erscheinen nur als gekennzeichnete Beispiele. Alle Hook-Libraries,
Ideen und der Style Guide sind eigenständig aus **Prinzipien** abgeleitet.

## 6. Anforderungs-Abdeckung (Teil 1–35)

Abgleich des Auftrags (35 Teile) mit den Deliverables, Stand 25.09.2026. **vollständig** = alle Unterpunkte mit Instagram-Daten
oder Primärquellen beantwortet · **mit Proxy** = beantwortet, aber teilweise über Ersatzmessung (Cover-Frame, YouTube-Shorts,
Codierung statt Messung) · **Einschränkung** = ein Unterpunkt ist mit öffentlichen Daten nicht messbar; Ersatz und eigener Test
sind angegeben.

| Teil | erfüllt in (Datei §) | Status | Hinweis |
|---|---|---|---|
| 1 Nischen-Attraktivität | [01](01_market_analysis.md) §0–§5 (12 Sub-Nischen, 10 Leitfragen, Tabellen A–D, Scoring) | vollständig | Indikatoren große Accounts, Views, Frequenz (Tab. D, nur DB-Auswahl), Engagement, Frische/Wachstum, neue schnelle Accounts, Commerce, Marken. Hashtag-Volumina und Größe von `/popular/interior-design/` `UNKNOWN`; Angebotslabels zählen Reels, nicht Nachfrage |
| 2 ≥ 50 Accounts, Gruppen A–H, Tiers | [02](02_competitor_database.csv), [03](03_competitor_analysis.md) §2, Anhang A | vollständig | 111 Accounts (72 tief profiliert); Status-Spalten je Kernfeld. Alter = Untergrenze, Frequenz = Obergrenze (`ESTIMATED`); viele Bios `UNKNOWN` (Profilseiten HTTP 429, WebSearch-Budget) |
| 3 Shortlist 20 + Outperformer | [03](03_competitor_analysis.md) §3–§4, [shortlist_scores.csv](data/processed/shortlist_scores.csv) | vollständig | 9 Kriterien, Score nicht followergetrieben (ρ = 0,03); vpf-Beispiele in §3.1–3.2 |
| 4 Reel-Analyse der Top-Accounts | [03](03_competitor_analysis.md) §5, [04](04_reel_database.csv) | Einschränkung | „Letzte 20 Reels“ ohne Login nicht abrufbar → Topic-Stichprobe je Account (bei 165 von 261 Kandidaten genau 2 Reels). 2.498 Reels analysiert (Ziel 300–500 übertroffen) mit URL, Datum, Views, Likes, Kommentaren; **Länge nur für 7 Reels**, Shares/Saves nicht öffentlich |
| 5 Szenen/Räume | [06](06_visual_styles.md) §2 | vollständig | Cover-Frame-Codierung `ESTIMATED` (κ 0,63–1,0) |
| 6 Farben, Materialien, Holz/Stein vs. Weiß | [06](06_visual_styles.md) §3, §3.5 | vollständig | Farbtemperatur n.s. |
| 7 Video-Aufbau | [05](05_viral_patterns.md) §2 | mit Proxy | Länge, Szenen, Tempo, Kamera auf Instagram nur n = 7 (NexLev); Zusammenhang mit Performance nur im YouTube-Proxy (n.s.) |
| 8 Erste 1–2 Sekunden | [05](05_viral_patterns.md) §3, [07](07_hooks.md) §3 | mit Proxy | Cover-Frame als Proxy; stimmt nur bei 3 von 7 geprüften Reels mit dem ersten Frame überein |
| 9 Text-Hooks + Psychologie | [07](07_hooks.md) §2.1–2.9 | vollständig | Kategorien-Kruskal n.s.; robust nur Choice → Kommentare; Prinzipien sind Erklärungshypothesen |
| 10 Captions | [07](07_hooks.md) §2.10 | vollständig | Länge, Frage, CTA, Hashtags, Emojis, Link-Hinweis gemessen; Storytelling und Such-Keywords nicht codiert (`UNKNOWN`) |
| 11 Audio | [05](05_viral_patterns.md) §2.6, [11](11_brand_style_guide.md) §10 | Einschränkung | Audio öffentlich nicht messbar: nur 7 Reels plus Meta-Aussagen; Trending vs. Original `UNKNOWN` → Test `T13_audio` |
| 12 Länge 0–5 … 30+ s | [05](05_viral_patterns.md) §4 | mit Proxy | Alle Buckets mit Median, Mittelwert, Views ÷ Kanal-Median, Views ÷ Abonnenten und Viralitätsquote, aber **YouTube-Shorts**, keine Instagram-Daten; kurze Buckets n < 15 aus 1 Kanal; Kruskal n.s. → Test `T12_length` |
| 13 Postingfrequenz 1/2/3/4+ | [05](05_viral_patterns.md) §5 | vollständig | Frequenz = Obergrenze (`ESTIMATED`); Uhrzeit/Wochentag n.s. |
| 14 Viralitätsstufen, Extrem-Ausreißer | [05](05_viral_patterns.md) §6 | vollständig | vpf-Stufen messen v. a. Accountgröße; deshalb zusätzlich adj-Stufen |
| 15 Top 10 % vs. Bottom 50 % | [05](05_viral_patterns.md) §7 | vollständig | 25 Accounts / 172 Reels (≥ 5 Reels im Sample); inkl. Posting-Zeit und CTA; kein Unterschied belastbar außer Skyline (nominal) |
| 16 Themen-Rankings | [06](06_visual_styles.md) §4 | vollständig | alle geforderten Räume, Gebäude, Landschaften und Orte mit Median, p90, vpf; kleine n markiert (z. B. Monaco n = 10) |
| 17 Stile | [06](06_visual_styles.md) §5 | mit Proxy | Saves nicht öffentlich → Saves-Proxy; Möbelpotenzial `ESTIMATED` |
| 18 Fantasy vs. realistisch | [06](06_visual_styles.md) §6 | vollständig | robustester Inhaltsbefund (3,25×, p = 0,001) |
| 19 Möbel-Affiliate-Konkurrenz | [09](09_monetization.md) §2 | vollständig | Affiliate-Status teils `UNKNOWN` (DM-Funnels) |
| 20 Monetarisierung der Konkurrenz | [09](09_monetization.md) §3, [03](03_competitor_analysis.md) §6 | vollständig | keine eigenen Einkommensschätzungen; nur `THIRD-PARTY ESTIMATE` |
| 21 Micro-Niches | [10](10_market_gaps.md) §1–§7 | vollständig | 22 Nischen mit Wettbewerb, Reichweite, KI-Eignung, Affiliate, Sponsoring, Differenzierung |
| 22 5 Account-Konzepte | [10](10_market_gaps.md) §8–§11 | vollständig | Zielgruppen sind Hypothesen; Handle-Verfügbarkeit `UNKNOWN` |
| 23 Style Guide | [11](11_brand_style_guide.md) §2–§16 | vollständig | Audio-Teil ohne eigene Performance-Daten (s. Teil 11) |
| 24 Content Pillars | [08](08_content_pillars.md) §2–§4 | vollständig | 5 Pillars + Reserve P6; „typische Views“ = Top-Page-Proxy, Potenzial-Ratings `ESTIMATED` |
| 25 50 Text-Hooks | [07](07_hooks.md) §4 | vollständig | 9 Kategorien; Originalität per [qa_checks.py](scripts/qa_checks.py) geprüft |
| 26 ≥ 30 visuelle Hooks | [07](07_hooks.md) §5 | vollständig | 34 Hooks in 6 Familien |
| 27 100 Ideen | [12](12_100_content_ideas.csv) | vollständig | 17 Felder je Idee, keine Lücken |
| 28 Testing-Matrix | [13](13_testing_matrix.csv) | vollständig | 27 Tests, u. a. HOOK, STIL, RAUM, LOCATION, LÄNGE, KAMERA, TEXT, AUDIO |
| 29 30-Tage-Plan | [14](14_30_day_launch_plan.md) §1–§8 | vollständig | Wochen 1–4, Regeln KEEP/ITERATE/SCALE/KILL |
| 30 KPIs | [15](15_kpi_framework.md) §2–§4 | vollständig | Saves, Shares, Watch Time, Completion und Klicks nur im eigenen Account messbar; Conversion-Referenz `THIRD-PARTY` |
| 31 Winner-Datenbank | [15](15_kpi_framework.md) §5, [Template](data/winner_database_template.csv), [Schema](data/winner_database_schema.sql) | vollständig | views_1h/6h/24h/7d, Reach, Shares, Saves, Follows, Watch Time, Link-Klicks, Umsatz |
| 32 Automatisierung + Gates | [16](16_automation_strategy.md) §2–§4 | vollständig | Gates für Qualität, Marke, KI-Artefakte, Ähnlichkeit, Recht; Kosten/Zeit = `ANNAHME` |
| 33 Konkurrenzmonitor | [17](17_competitor_monitor.md), [scripts/monitor/](scripts/monitor/) | vollständig | nur öffentliche Daten; Erhebung nur per Graph API (Business Discovery), manuell oder mit schriftlicher Erlaubnis (`robots.txt`, §2.1) |
| 34 Quellen + Status | [quellen/README.md](quellen/README.md) §34.0–§34.7, q01–q09 | vollständig | Kernbefunde mit Quelle und Status in §34.7 |
| 35 Antworten A–N | [00](00_executive_summary.md) A–N | vollständig | Entscheidung K1 *The Unbuilt* |
| Output-Ordner, Grafiken | dieses README, [charts/](charts/), [quellen/](quellen/) | mit Proxy | Views nach Stil ([06](06_visual_styles.md) §2.3), Raum (§2.1), Location (§4.2), Hook ([07](07_hooks.md) §2.2 Instagram, §2.6 YouTube-Proxy), Views/Follower je Account ([03](03_competitor_analysis.md) §3.1); Länge und Kamera nur als YouTube-Proxy ([05](05_viral_patterns.md) §2.3, §4.1) |
