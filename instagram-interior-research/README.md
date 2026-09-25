# Instagram Interior / Luxury Homes / AI Architecture: Research-Playbook

**Stand der Daten: 25.09.2026.** Datenbasiertes Markt-, Konkurrenz- und Content-Playbook für einen neuen, internationalen,
englischsprachigen Instagram-Account mit überwiegend KI-generierten Bildern und Reels (Luxury Interiors, Future Homes,
Architektur). Ziel war ausdrücklich **nicht**, die Ursprungsidee zu bestätigen, sondern die beste datenbasierte
Positionierung zu finden.

> **Kurzfazit:** Die Nische ist groß. Das Ursprungskonzept „KI-Luxus-Interiors“ (Schlaf- und Wohnzimmer, Küchen im
> weichen „dreamy“-KI-Look) ist in den Daten aber der **schwächste** KI-Teilbereich. Stärker schneiden
> **unmögliche, konzeptionelle Architektur** ab (≈2,3× über Erwartung) sowie Außenräume, Bäder und Treppen, Choice-Formate
> (≈5,7× mehr Kommentare) und eine **Studio-/Creator-Identität statt Theme-Page**. Details: [00_executive_summary.md](00_executive_summary.md).

---

## 1. Wo finde ich was? (Teil 1–35 → Datei)

| Teil | Thema | Datei |
|---|---|---|
| 35 | Abschließende Entscheidung (A–N) | [00_executive_summary.md](00_executive_summary.md) |
| 1 | Ist die Nische attraktiv? | [01_market_analysis.md](01_market_analysis.md) |
| 2 | 50+ Accounts (Rohdaten mit Status je Feld) | [02_competitor_database.csv](02_competitor_database.csv) |
| 2, 3, 4, 20 | Account-Überblick, Top-20-Shortlist, Outperformance-Accounts, Monetarisierung der Top-Accounts | [03_competitor_analysis.md](03_competitor_analysis.md) |
| 4–18 | Reel-Datenbank (2.498 Reels) | [04_reel_database.csv](04_reel_database.csv) |
| 7, 8, 12, 13, 14, 15 | Video-Aufbau, erste Sekunden, Länge, Frequenz, Viralitätsstufen, Gewinner vs. Verlierer | [05_viral_patterns.md](05_viral_patterns.md) |
| 5, 6, 16, 17, 18 | Szenen, Stile, Farben/Materialien, Themen-Rankings, Fantasy vs. realistisch | [06_visual_styles.md](06_visual_styles.md) |
| 8, 9, 25, 26 | Hook-Analyse, 50 Text-Hooks, 30+ visuelle Hooks | [07_hooks.md](07_hooks.md) |
| 24 | Content Pillars | [08_content_pillars.md](08_content_pillars.md) |
| 19, 20 | Möbel-Affiliate-Konkurrenz, Monetarisierung der Konkurrenz, eigene Monetarisierungs-Roadmap | [09_monetization.md](09_monetization.md) |
| 21, 22 | 10+ Micro-Niches, 5 Account-Konzepte | [10_market_gaps.md](10_market_gaps.md) |
| 23 | Eigener Style Guide | [11_brand_style_guide.md](11_brand_style_guide.md) |
| 27 | 100 Content-Ideen | [12_100_content_ideas.csv](12_100_content_ideas.csv) |
| 28 | Testing-Matrix | [13_testing_matrix.csv](13_testing_matrix.csv) |
| 29 | 30-Tage-Launchplan (KEEP / ITERATE / SCALE / KILL) | [14_30_day_launch_plan.md](14_30_day_launch_plan.md) |
| 30, 31 | KPI-System, Winner-Database | [15_kpi_framework.md](15_kpi_framework.md), [data/winner_database_template.csv](data/winner_database_template.csv), [data/winner_database_schema.sql](data/winner_database_schema.sql), [scripts/winner_analysis.py](scripts/winner_analysis.py) |
| 32 | Automatisierbarkeit | [16_automation_strategy.md](16_automation_strategy.md) |
| 33 | Konkurrenzmonitor | [17_competitor_monitor.md](17_competitor_monitor.md), [scripts/monitor/](scripts/monitor/) |
| 34 | Quellen und Quellenqualität | [quellen/README.md](quellen/README.md), `quellen/q01–q09` |
| — | Grafiken | [charts/](charts/) (60 PNGs) |
| — | Alle Kennzahlen an einem Ort | [data/processed/analysis_digest.md](data/processed/analysis_digest.md) |

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
   Accounts mit ≥5 Reels in der Topic-Stichprobe (20 Accounts, 138 Reels).
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
python3 scripts/digest.py              # data/processed/analysis_digest.md
python3 scripts/charts.py              # charts/*.png
```

Rohdaten liegen in `data/raw/` (Topic-Batches, Embed-Lookups, codierte Reels, Profile, YouTube). Cover-Bilder werden bewusst
**nicht** gespeichert, weil sie urheberrechtlich geschützte Werke Dritter sind. Die Datenerhebung lief über Claude-Code-Agenten
mit WebFetch. Wie man das wöchentlich wiederholt, steht in [17_competitor_monitor.md](17_competitor_monitor.md).

## 5. Grundsatz

Wir kopieren keine Creatives. Beobachtete Hooks und Captions erscheinen nur als gekennzeichnete Beispiele. Alle Hook-Libraries,
Ideen und der Style Guide sind eigenständig aus **Prinzipien** abgeleitet.
