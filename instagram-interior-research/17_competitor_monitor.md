# 17 – Wettbewerber-Monitor (Teil 33): wöchentliches System nur mit öffentlichen Daten

Stand: 2026-09-25 · Gilt für den neuen, englischsprachigen Instagram-Themen-Account mit überwiegend KI-generierten Luxury-Interiors, Future Homes und Architektur-Reels. Betrieben wird er aus Deutschland.

**Abgleich mit der finalen Strategie (25.09.2026):** Standard-Erhebung sind die offizielle Graph API (Business Discovery) und der manuelle Modus; ein automatischer Web-Sweep braucht eine schriftliche Erlaubnis (Abschnitt 2, [README – Compliance-Hinweis](README.md)). Monitor-Hypothesen gehen in Monat 1 nur in die Pilot-Slots des Tagesplans ([14](14_30_day_launch_plan.md)), ab Monat 2 in die Explorations-Slots ([15 §4.5](15_kpi_framework.md)); neue Test-IDs beginnen bei `T28` (Abschnitt 7). `pillar_fit` meint die Pillars P1–P6 aus [08](08_content_pillars.md). [q07](quellen/q07_legal_ai_risk.md) liegt vor, behandelt aber die Datenerhebung nicht (2.1).

**Kennzeichnung:**
- **[VERIFIED]**: in einer Primär- oder zitierten Quelle gesehen
- **[DATEN]**: eigene Auswertung bzw. eigener Testlauf
- **[ANNAHME]**: Planungswert, nicht gemessen
- **zu verifizieren**: vor Nutzung prüfen

**Dateien dieses Teils:**

| Datei | Inhalt |
|---|---|
| [`scripts/monitor/monitor_weekly.py`](scripts/monitor/monitor_weekly.py) | Auswertung: nur Standardbibliothek, liest nur lokale Rohdateien |
| [`scripts/monitor/monitor_workflow_prompt.md`](scripts/monitor/monitor_workflow_prompt.md) | Agent-Prompts, Workflow-Skript, Zeitplan, API-Spezifikation |
| [`scripts/monitor/weekly_monitor.workflow.js`](scripts/monitor/weekly_monitor.workflow.js) | aus der `.md` extrahiertes Workflow-Skript |
| [`scripts/monitor/routine_prompt.txt`](scripts/monitor/routine_prompt.txt) | Prompt der Routine |
| [`scripts/monitor/build_watchlists.py`](scripts/monitor/build_watchlists.py) | erzeugt `watchlist_topics.csv` und `watchlist_competitors.csv` |
| [`data/monitor/2026-W39_baseline/`](data/monitor/2026-W39_baseline/report.md) | Beispiel-Report auf den Research-Daten |
| [`data/monitor/inspiration_board.csv`](data/monitor/inspiration_board.csv) | Vorlage für das Inspirations-Board |

---

## 0. Kurzfassung

1. **Was der Monitor tut.** Einmal pro Woche wertet er Topic- und Wettbewerberdaten in genau dem Rohformat dieser Research aus: im Modus `manual` 20–25 vom Owner gespeicherte Topic-Seiten (Wettbewerber monatlich), im Modus `api` Business Discovery für ca. 40 Wettbewerber und Hashtag Search; die volle Watchlist hat 57 Topic-Seiten. Daraus berechnet `monitor_weekly.py`:
   - neue Reels (Veröffentlichung nach dem letzten Lauf, dekodiert aus dem Shortcode)
   - `topic_index`, `vpf` und Tiers
   - EXTREME- und VIRAL-Alarme
   - Anteilsverschiebungen im Top-Quartil nach Raum, Stil, Setting, Stil × Raum und Hook-Typ
   - Hook-Vergleiche
   - Follower- und Posting-Kadenz der Wettbewerber

   Ergebnis ist ein deutscher `report.md` mit Alerts. Danach folgen 20–30 Minuten menschliche Review.
2. **Wichtigster Befund zum Datenzugang [VERIFIED, 2026-09-25].** Die `robots.txt` von instagram.com sperrt `User-agent: *` (und `ClaudeBot`) mit `Disallow: /`. Sie hält fest: *"Collection of data on Instagram through automated means is prohibited unless you have express written permission from Instagram."* Ein automatisch geplanter WebFetch-Sweep ist daher **nicht** durch „öffentlich, ohne Login“ gedeckt. Der Workflow kennt drei Modi (Abschnitt 2):
   - `api`: offizielle Graph API, **Zielbild**
   - `manual`: der Owner speichert die Seiten selbst, **sofort nutzbar**
   - `webfetch_permitted`: nur mit schriftlicher Erlaubnis, sonst bricht das Skript ab

   Ohne Angabe startet das Workflow-Skript im Modus `manual`.
3. **Leitplanken der Auswertung:**
   - Mindest-n: 30 Top-Quartil-Reels pro Woche, 5 pro Segment, 8 pro Hook-Typ
   - Benjamini-Hochberg-Korrektur über alle Segment- und Hook-Tests
   - Wochenvergleiche nur auf den Topics, die in beiden Wochen erfolgreich erhoben wurden
   - Follower-Deltas nur oberhalb der Rundungsstufe der Embed-Anzeige
   - Jeder Alert trägt den Satz „keine Ursache belegt“
4. **Getestet [DATEN]:**
   - Auf `data/raw` laufen alle 22 `batch_*.json` fehlerfrei: 2.498 Reels, 239 Topics, 12 neue Reels im 7-Tage-Fenster, < 1 s Laufzeit.
   - Mit synthetischer Folgewoche erkennt der Wochenvergleich eine eingebaute Verschiebung zuverlässig.
   - Mit einem Fixture im API-Format funktionieren die Likes-Metrik und der Account-Index.
5. **Die Messgenauigkeit ist offen ausgewiesen [DATEN].** Die Keyword-Regeln stimmen mit dem Codebuch überein:
   - Raum zu 72 %, Stil zu 59 %
   - Hook-Heuristik nur zu 45 %; einzelne Klassen sind präzise (`pov` 100 %, `choice` 93 %)
   - Deshalb codieren Agenten die Captions jede Woche mit dem Codebuch (nur Text, ohne Netz). Hook-Vergleiche über alle Klassen gibt es nur, wenn ≥ 80 % der Reels in beiden Wochen codiert sind.
6. **Wohin die Ergebnisse gehen:**
   - Inspirations-Board: nur Prinzipien in eigenen Worten, nie Motive oder Captions
   - höchstens 2 neue Hypothesen pro Woche in die `tests`-Tabelle der Winner-DB
   - im Launch-Monat nur die Pilot-Slots `T18`, `T26`, `T27` ([14 §8](14_30_day_launch_plan.md)); laufende Tests der [Testing-Matrix](13_testing_matrix.csv) ändert der Monitor nicht
   - ab Monat 2 die 4 Explorations-Slots pro Woche ([15 §4.5](15_kpi_framework.md))

   Konkurrenzsignale sind Hypothesen. Entscheidungen fallen nur auf eigenen Daten.

---

## 1. Architektur

```
                      ┌──────────────────────── Inputs (Repo) ────────────────────────┐
                      │ watchlist_topics.csv (57 Slugs)   watchlist_competitors.csv (40)│
                      └───────────────┬───────────────────────────────┬────────────────┘
                                      │                               │
 Mo 06:51 Routine ─► Workflow  Preflight ─► Topics ─► Embeds ─┬─► Codes (Captions, ohne Netz)
 (Modus api / manual /        (Gate)    (sequenziell)  (sequenziell)│
  webfetch_permitted)                                               ▼
                               data/monitor/2026-Www/  topics/ accounts/ reels/ competitors/ run_meta.json
                                                                    │
                                              monitor_weekly.py ◄───┘  (+ Vorwoche automatisch)
                                                                    │
                   report.md · alerts.json · monitor_*.csv · inspiration_candidates.csv · watchlist_competitors_next.csv
                                                                    │
                          Mensch (G5, 20–30 Min.) ─► inspiration_board.csv ─► tests (Winner-DB) ─► Testmatrix Folgewoche
```

---

## 2. Datenzugang: was „nur öffentliche Daten“ konkret heißt

### 2.1 Befund `robots.txt` (per WebFetch abgerufen am 2026-09-25)

| Punkt | Wortlaut / Ergebnis | Status |
|---|---|---|
| Hinweis im Kopf | *"Notice: Collection of data on Instagram through automated means is prohibited unless you have express written permission from Instagram and may only be conducted for the limited purpose contained in said permission."* | [VERIFIED] |
| Verweis | *"All authorized user-agents listed on this page must comply with Meta's Automated Data Collection Terms"*, verlinkt auf `facebook.com/legal/automated_data_collection_terms` | [VERIFIED]; Inhalt der Terms nicht gelesen, zu verifizieren |
| `User-agent: *` | `Disallow: /` | [VERIFIED] |
| `User-agent: ClaudeBot` | `Disallow: /` | [VERIFIED] |
| Freigaben für `/popular/`, `/reel/`, `/embed/` | für keinen User-Agent vorhanden. Googlebot und facebookexternalhit haben nur Einzelsperren, z. B. `/ajax/`, `/publicapi/`, `/query/`, `/direct/` | [VERIFIED] |
| User-Agent des WebFetch-Tools | nicht dokumentiert. Das ist egal, weil jeder nicht gelistete Agent unter `*` fällt. | zu verifizieren |
| Instagram-Nutzungsbedingungen zur automatisierten Erhebung | Hilfeseite per WebFetch nicht lesbar (nur JavaScript-Hülle) | zu verifizieren |

**Folge:** Die Research-Erhebung vom 2026-09-25 lief als einmalige Stichprobe über WebFetch. Details: 264 Topic-Abrufe, inklusive Wiederholungen 250 eindeutige Slugs, davon 239 mit Reels, dazu Embed-Seiten. Für einen **wiederkehrenden, geplanten** Lauf gilt der Hinweis in der `robots.txt` ausdrücklich. Deshalb erzwingt das Workflow-Skript einen Modus. Eine rechtliche Bewertung (Nutzungsbedingungen, DSGVO für Handles natürlicher Personen, Datenbankrecht) steht aus und ist **zu verifizieren**. [q07](quellen/q07_legal_ai_risk.md) liegt inzwischen vor, behandelt aber KI-Kennzeichnung, Werbung, Marken, Irreführung und Musik, **nicht** die automatisierte Erhebung, die DSGVO oder das Datenbankrecht. Diese Seite ist keine Rechtsberatung.

### 2.2 Drei Erhebungsmodi

| | `api` (Zielbild) | `manual` (Start) | `webfetch_permitted` |
|---|---|---|---|
| **Wettbewerber** | Business Discovery: `followers_count` und `media_count` exakt; pro Medium `like_count`, `comments_count`, `view_count` [VERIFIED, [Meta-Doku](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/business-discovery)]. Liefert **alle** neuen Reels eines Wettbewerbers, nicht nur die auf Topic-Seiten. | Owner speichert monatlich die Embed-Seiten der 10 wichtigsten Wettbewerber | wie Research: Embed-Seite des zuletzt bekannten Reels |
| **Trends** | Hashtag Search `top_media`: *"a maximum of 30 unique hashtags … within a rolling, 7 day period"*; App Review für „Instagram Public Content Access“ nötig [VERIFIED, [Meta-Doku](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/hashtag-search)]. Rückgabefelder zu verifizieren, Views eventuell nicht verfügbar. Der Monitor rechnet dann auf Likes. | Owner öffnet 20–25 Kern-Topics im eigenen Browser, speichert sie nach `inbox/topics/<slug>.html`, ein Agent parst **lokal**. Ob gespeicherte Seiten Reel-Links und Views enthalten: beim ersten Mal zu verifizieren. | 57 Topic-Seiten per WebFetch |
| **Voraussetzung** | Business- oder Creator-Konto, Meta-App, Token; Collector `collect_graph_api.py` noch zu bauen (Spezifikation in der Workflow-Datei, Abschn. 7) | keine | schriftliche Erlaubnis von Instagram/Meta (`args.permission_ref`) |
| **Aufwand pro Woche** | ~0 Min. Mensch | 15–25 Min. Speichern [ANNAHME] | ~0 Min. Mensch |
| **Grenzen** | nur professionelle Accounts; keine Daten altersbeschränkter Accounts [VERIFIED]; Rate-Limits zu verifizieren | weniger Topics, Handarbeit | ohne Erlaubnis unzulässig |

**Empfehlung:**
- Start mit `manual` (Topics wöchentlich, 20–25 Slugs der Cluster `ai_field`, `future_homes`, `luxury_interiors`, `unusual_homes`).
- Ab dem Einrichten des Business-Kontos auf `api` wechseln.
- `webfetch_permitted` nur mit dokumentierter Erlaubnis.

**Abstimmung mit Teil 32:** [16, Abschn. 1–2](16_automation_strategy.md) übernimmt diese Modi: kein automatischer Web-Sweep, Wettbewerber im Modus `api` wöchentlich, im Modus `manual` monatlich. Das Referenz-Set für den Ähnlichkeitscheck ([16 §4.4](16_automation_strategy.md)) wird nur aus zulässigen Quellen aufgefrischt; der Monitor selbst lädt keine Bilder (2.3).

### 2.3 Regeln in allen Modi

Die Prompts enthalten diese Regeln wörtlich als `RULES`-Block, siehe [Workflow-Datei](scripts/monitor/monitor_workflow_prompt.md).

1. **Kein Login, keine Cookies, keine Tokens** außer dem eigenen Graph-API-Token im Modus `api`. Keine inoffiziellen Endpunkte (`/api/`, `/graphql/`, `?__a=1`). Keine Mirror-, Viewer- oder Proxy-Dienste.
2. **Keine Umgehung.** Die erste Login-Wall, der erste 429 oder das erste Captcha stoppt alle weiteren Abrufe der Woche. Es gibt kein Retry, keinen Hostwechsel und keine Verzögerungstricks.
3. **Tempo:** Abrufe laufen nacheinander (eine Seite zur Zeit, Batches à 6 bzw. 8 nacheinander). Die Obergrenze liegt bei ca. 180 Abrufen pro Woche. Jede URL wird höchstens einmal pro Lauf abgerufen. Liegen schon Batches im Wochenordner, wird nicht neu erhoben.
4. **Datensparsamkeit:**
   - Gespeichert werden Handle, öffentliche Zähler (wie angezeigt), Shortcode und Caption (höchstens 300 Zeichen).
   - Keine Bilder oder Videos, keine Profile, Kommentare, Liker-Listen oder Stories.
   - Cover-Frames werden im Monitor **nicht** heruntergeladen. Eine visuelle Codierung bleibt der Research vorbehalten.
5. **Aufbewahrung [ANNAHME]:** Rohdaten 12 Monate im privaten Repo, danach nur noch die Wochen-Aggregate (`monitor_segments.csv`, `monitor_topics.csv`). Löschung einzelner Handles auf Anfrage. DSGVO-Einordnung zu verifizieren.

### 2.4 Was öffentliche Daten nicht zeigen

| Grenze | Folge im Monitor |
|---|---|
| Die Top-3-Rankingsignale laut Mosseri sind *"watch time, likes and sends"* ([q01, Abschn. 2 (1)](quellen/q01_instagram_platform_rules.md), [VERIFIED, Sekundärquelle]). Öffentlich sichtbar sind davon nur Likes. | `likes_per_view` ist der einzige Resonanz-Proxy. Watch Time und Sends gibt es nur für eigene Reels (Insights, [15](15_kpi_framework.md)). |
| Topic-Seiten zeigen ca. 12 Top-Reels mit gerundeten Views | Survivorship: Wir sehen Gewinner, keine Basisrate. Jeder Befund ist eine Hypothese. |
| Follower sind auf Embed-Seiten gerundet: „547K“ = 1.000er-Stufe, „2M“ = 1-Mio.-Stufe | Das Wachstum gilt erst als erkannt, wenn die Differenz größer ist als die gröbere Rundungsstufe beider Wochen (`rounding_step`). Beitragszahlen sind exakt, daher sind Beiträge pro Woche belastbar. |
| Im Modus `webfetch`/`manual` bekommen wir neue Reels eines Wettbewerbers nur zu sehen, wenn sie auf einer Topic-Seite auftauchen | Die Posting-Kadenz kommt aus dem Delta der Beitragszahl. Vollständige Reel-Listen gibt es erst im Modus `api`. |

---

## 3. Inputs

### 3.1 Topic-Watchlist: 57 Slugs in 9 Clustern

Die Datei `scripts/monitor/watchlist_topics.csv` wurde von Hand aus den 239 erfolgreich erhobenen Topics ausgewählt und enthält Baseline-Werte. Die Spalte `group` entspricht dem Feld `pillar` der Winner-DB, also der Research-Themengruppe ([Schema](data/winner_database_schema.sql)); die Playbook-Pillar P1–P6 steht dort in `playbook_pillar` ([15 §5.2](15_kpi_framework.md)). Die Spalte `cluster` dient nur der Lesbarkeit.

| Cluster | n | Slugs (Median-Views am 2026-09-25) |
|---|---|---|
| ai_field | 6 | `ai-interior-design` (1,7 Mio.), `ai-home-design` (985 Tsd.), `ai-generated-house` (548 Tsd.), `midjourney-architecture` (414 Tsd.), `ai-architecture` (376 Tsd.), `ai-cozy-cabin` (336 Tsd.) |
| future_homes | 6 | `futuristic-houses` (575 Tsd.), `futuristic-house` (402 Tsd.), `parametric-architecture` (292 Tsd.), `futuristic-interior` (290 Tsd.), `futuristic-home` (280 Tsd.), `future-houses-2050` (54 Tsd.) |
| architecture | 3 | `modern-architecture` (3,0 Mio.), `architecture-design` (285 Tsd.), `tropical-house-architecture-styles` (238 Tsd.) |
| luxury_interiors | 11 | `dream-bedrooms` (1,1 Mio.), `luxury-bathroom-design` (1,1 Mio.), `bedroom-design` (937 Tsd.), `living-room-design` (914 Tsd.), `luxury-kitchen` (713 Tsd.), `dream-closet` (708 Tsd.), `dream-bedroom` (659 Tsd.), `bathroom-design` (620 Tsd.), `quiet-luxury` (564 Tsd.), `luxury-living-room-design` (394 Tsd.), `luxury-bedroom` (348 Tsd.) |
| luxury_homes | 6 | `dream-home` (2,3 Mio.), `luxury-house` (1,8 Mio.), `luxury-penthouse` (1,5 Mio.), `modern-luxury-house-interiors` (527 Tsd.), `modern-villa` (457 Tsd.), `ultra-modern-luxury-house-design` (387 Tsd.) |
| unusual_homes | 9 | `dream-room` (3,5 Mio.), `treehouse` (2,6 Mio.), `underground-house` (1,1 Mio.), `house-in-the-forest` (673 Tsd.), `luxury-cabin` (463 Tsd.), `waterfall-house` (187 Tsd.), `glass-house` (94 Tsd.), `desert-house` (40 Tsd.), `cliff-house` (18 Tsd.) |
| cozy_ambience | 5 | `cozy-rain` (3,9 Mio.), `rain-cozy` (562 Tsd.), `cozy-bedroom-ideas` (429 Tsd.), `cozy-cabin-in-the-snow` (202 Tsd.), `cozy-winter-cabin` (170 Tsd.) |
| pools_resorts | 6 | `infinity-pools` (1,9 Mio.), `treehouse-hotel` (1,6 Mio.), `overwater-villa` (888 Tsd.), `luxury-pool` (674 Tsd.), `indoor-pool` (270 Tsd.), `underwater-hotel` (255 Tsd.) |
| styles | 5 | `japandi` (314 Tsd.), `art-deco-interior-design` (306 Tsd.), `tropical-house` (228 Tsd.), `organic-modern` (139 Tsd.), `biophilic-bedroom-design` (124 Tsd.) |

**Pflege:**
- Höchstens 5 Slugs pro Monat tauschen. Wochenvergleiche laufen ohnehin nur auf gemeinsamen Topics; zu viele Wechsel machen Trends über 4–8 Wochen unlesbar.
- Neue Kandidaten kommen aus den `related_topics` der Topic-Seiten.
- Im Modus `manual` die 20–25 Slugs der Cluster ai_field, future_homes, luxury_interiors und unusual_homes nehmen.

### 3.2 Wettbewerber-Watchlist: 40 Handles in drei Rollen

Die Datei `scripts/monitor/watchlist_competitors.csv` wird von `build_watchlists.py` aus `data/processed/accounts_metrics.csv` erzeugt.

| Rolle | n | Regel (Research-Snapshot 2026-09-25) |
|---|---|---|
| direct | 25 | Produktion `ai_generated` oder `3d_render` (codiert), Sprache en, Kontotyp ai_creator, theme_page oder media_publication, ≥ 30.000 Follower, letzter gesehener Post ≥ 2026-03-01, sortiert nach Median-topic_index |
| emerging | 10 | wie direct, aber 3.000–30.000 Follower, aktiv seit 2026-05-01, max. vpf ≥ 5, sortiert nach max. vpf. Das sind die „kleiner Account, großer Hit“-Fälle. |
| benchmark | 5 | große Referenz-Seiten aus der profilierten Shortlist, unabhängig von der Produktionsart |

**Stand der Generierung** (die Liste ändert sich, solange die Research-Codierung läuft; nach deren Abschluss `build_watchlists.py` erneut ausführen):
- **direct:** @cairo_ia, @parametric.architecture, @fast_buildsx, @foorcrafts, @buildcraft.hq, @thehomopien, @sandiwara_multiverse.99, @sunt_mrr, @lena_nichi_art, @diniz_nasaroba, @day_design_101, @modern_house__3d, @primurse_log, @travelask.world, @shri_bk_babu, @elitebuildhq, @calmstorms_13, @kratosdigitalarts, @archimyst1, @urban_lifestyle_lab, @aiforarchitects, @watchthebuild, @rain.nest, @buildenza_, @ideadesigncasa
- **emerging:** @relaxationreflections_, @poppet_tales, @designevolutionn, @ai_furniture_design, @ai.cozy.fun.scenes, @vesgantti_home, @renovaistudio, @milanchettri123, @rainy__village, @nashla_t_02
- **benchmark:** @soothenests, @wayup_media, @luxurydreamhub, @uniqchalets, @cozyzen.ai

**Von Hand ausgeschlossen** (`EXCLUDE` im Skript): @diycraftstvofficial (DIY), @naturesms (Natur) und @thedollstudio2026 (KI-Kunst). Sie erfüllen die Regeln, liegen aber thematisch außerhalb der Nische.

**Pro Handle führt die Liste:**
- `last_shortcode`: das neueste Reel aus der Research, daraus die `embed_url`
- `last_posted_utc`

Findet der Monitor ein neueres Reel des Handles auf einer Topic-Seite, schlägt er in `watchlist_competitors_next.csv` den neuen Shortcode vor. Der Mensch übernimmt ihn in der Review.

---

## 4. Wöchentlicher Ablauf

| Wann | Schritt | Wer | Output |
|---|---|---|---|
| Mo 06:51 (Europe/Berlin), bei `manual` 10:51 | Routine startet eine frische Session und berechnet `WEEK` und `RUN` per `date -u` | Routine | – |
| | **Preflight:** Modus-Gate (ohne `permission_ref` kein WebFetch), Ordner, `run_meta.json`, Watchlists lesen; im WebFetch-Modus `robots.txt` als Schnappschuss mit Änderungsvergleich | Agent | `data/monitor/2026-Www/run_meta.json` |
| | **Topics:** Batches à 6 Slugs **nacheinander**, Circuit Breaker; `manual`: lokales Parsen von `inbox/`; `api`: Collector | Agenten | `topics/batch_<wk>_NN.json` |
| | **Embeds** (nur WebFetch-Modus): `monitor_weekly.py --todo` listet fehlende Embeds (Wettbewerber, neue Reels, Reels ohne Follower mit topic_index ≥ 2; max. 80); Batches à 8 nacheinander | Agenten | `accounts/followers_<wk>_NN.json` |
| | **Codes** (parallel zu Embeds, ohne Netz): Caption-Felder des Codebuchs für alle Reels der Woche, Chunks à 150 | Agenten | `reels/caption_codes_<wk>_NN.json` |
| | **Report:** `monitor_weekly.py` mit automatisch gefundener Vorwoche; im ersten Lauf `--prev data/raw` | Agent | `report.md` und Tabellen |
| | Commit in Branch `monitor/2026-Www`, Antwort mit den Top-5-Alerts | Routine | Git |
| Mo, 20–30 Min. | **Review G5** (Abschnitt 6), danach Board, Tests und Watchlist pflegen | Mensch | `inspiration_board.csv`, `tests` |
| Di | Konzeptkarten der Woche nach Tagesplan und Matrix finalisieren ([14 §4–5](14_30_day_launch_plan.md), [13](13_testing_matrix.csv)); Monitor-Hypothesen nur in Pilot- bzw. Explorations-Slots (7.2) | Mensch | Content-Plan |

**Zeitplan einrichten:** Details in [Workflow-Datei, Abschn. 3](scripts/monitor/monitor_workflow_prompt.md).
- Routine als geplanter Trigger mit frischer Session pro Lauf, Cron `CRON_TZ=Europe/Berlin 51 6 * * 1`.
- Die Minute 51 ist bewusst nicht :00, damit der Lauf nicht mit anderen Routinen zur vollen Stunde startet.
- Alternative: `cron` auf eigenem Server; die Flags des `claude`-CLI sind zu verifizieren.
- Ob das Workflow-Tool in Routine-Sessions verfügbar ist, beim ersten Lauf **verifizieren**. Fehlt es, arbeitet die Session die Prompts der Reihe nach ab.

---

## 5. Auswertung: `monitor_weekly.py`

### 5.1 Aufruf

```bash
python3 scripts/monitor/monitor_weekly.py data/monitor/2026-W40                  # Vorwoche automatisch (nächstälterer Ordner mit topics/)
python3 scripts/monitor/monitor_weekly.py data/monitor/2026-W40 --prev data/raw  # 1. Lauf gegen die Research-Baseline
python3 scripts/monitor/monitor_weekly.py data/raw --out-dir data/monitor/2026-W39_baseline --only-watchlist
python3 scripts/monitor/monitor_weekly.py <woche> --todo            # nur embed_todo.json
python3 scripts/monitor/monitor_weekly.py <woche> --dump-captions -1  # Caption-Chunks für die Coding-Agenten
```

**Parameter** (Standardwerte in Klammern): `--min-n` (8), `--min-tq` (30), `--min-seg` (5), `--min-pp` (5), `--max-q` (0,10), `--min-followers` (1.000), `--min-growth` (5 %), `--min-posts-week` (14), `--min-code-cov` (0,8), `--since`, `--only-watchlist`.

**Wiederverwendung:**
- `parse_views` aus [`parse_topics.py`](scripts/parse_topics.py)
- `shortcode_to_datetime` aus [`shortcode_time.py`](scripts/shortcode_time.py)
- `topic_group` aus [`topic_groups.py`](scripts/topic_groups.py)

Alle drei kommen per `sys.path`. Das Rohformat ist identisch mit `data/raw/topics/batch_*.json`, `data/raw/accounts/followers_*.json` und `data/raw/reels/*.json`.

### 5.2 Kennzahlen

| Kennzahl | Definition | Hinweis |
|---|---|---|
| neues Reel | Veröffentlichung (aus dem Shortcode) liegt nach dem Lauf der Vorwoche **und** der Shortcode fehlte in der Vorwoche. Ohne Vorwoche gilt: 7 Tage vor dem Abruf. | exakt, [`shortcode_time.py`](scripts/shortcode_time.py) |
| topic_index | Views ÷ Median-Views derselben Topic-Seite **dieser Woche**; pro Reel das Maximum über seine Topics | wie in der Research ([analyze.py](scripts/analyze.py)). Liefert eine Seite keine Views (Hashtag-API), wird auf Likes gerechnet und das in `metric` vermerkt. |
| Top-Quartil (TQ) | Reel mit topic_pct ≥ 0,75 auf mindestens einer seiner Seiten | Reels auf mehreren Seiten haben mehr Chancen, daher gilt ca. ein Drittel der Reels als TQ |
| vpf, Tier | Views ÷ Follower; NORMAL < 0,5 · GOOD 0,5–2 · VERY_GOOD 2–5 · VIRAL 5–20 · EXTREME ≥ 20 | Follower: Embed dieser Woche, sonst Account-Lookup, sonst Vorwoche (`followers_source`) |
| Account-Index (API) | view_count ÷ Median des Accounts über die gelieferten Medien | nur im Modus `api`; Alarm ab 3× bei neuem Reel |
| Beiträge/Woche | Δ Beitragszahl ÷ Tage zwischen den Läufen × 7 | exakt |
| Follower-Wachstum | Δ Follower, nur wenn größer als die Rundungsstufe | „innerhalb Rundung“ wird ausgewiesen |
| Frische | Anteil der Reels einer Topic-Seite, die nach dem Stichtag erschienen sind | zeigt, wo neue Reels überhaupt einbrechen |

### 5.3 Segmente

| Dimension | Quelle | Genauigkeit gegen Codebuch [DATEN, Testlauf 2026-09-25] |
|---|---|---|
| Topic-Gruppe | [`topic_groups.py`](scripts/topic_groups.py) | exakt |
| Raum | Keyword-Regeln auf Caption + Topic-Slug (bedroom, bathroom, kitchen, closet, living_room, dining, pool, home_theater, office_library, whole_home) | 72 % Übereinstimmung mit `room_primary` (n = 1.482). Häufigster Fehler: Living-Room-Cover landen als whole_home. |
| Stil | Keyword-Regeln (tropical, japandi, futuristic, cozy_rustic, …, modern_luxury als Auffangklasse) | 59 % (n = 1.289); Fehler meist „→ modern_luxury“ |
| Setting | Keyword-Regeln (ocean_beach, mountain_snow, forest, jungle, rain, …) | nicht gegen das Codebuch gemessen, weil keine 1:1-Zuordnung existiert |
| Stil × Raum | Kombination, z. B. `tropical × bedroom` | wie oben, multipliziert sich |
| Hook-Typ | `caption_hook_category` des Codebuchs, wenn ≥ 80 % der Reels in **beiden** Wochen codiert sind (wöchentliche Caption-Codierung durch Agenten). Sonst gilt für alle Reels die Heuristik, und Paarvergleiche laufen nur zwischen `pov`, `choice`, `question` und `money`. | Heuristik gesamt 45 % (n = 2.400). Präzision je Klasse: `pov` 100 % (n = 21), `choice` 93 % (27), `question` 57 % (207), `money` 54 % (111); `fantasy` nur 16 %. |

Die Regeln sind auf demselben Datensatz entstanden, gegen den sie gemessen wurden. Die Werte sind daher eher optimistisch. Der Report zeigt die Übereinstimmung jede Woche neu (Abschnitt 8 im Report), sobald codierte Reels vorliegen.

### 5.4 Alarmregeln

| Alert | Auslöser | Guard | Priorität |
|---|---|---|---|
| `new_outlier` | neues Reel mit Tier VIRAL oder EXTREME | P1 nur bei EXTREME **und** topic_index ≥ 1 **und** ≥ 1.000 Follower; Mini-Accounts werden markiert | P1–P3 |
| `new_outlier_no_followers` | neues Reel mit topic_index ≥ 5, Follower unbekannt | geht in `--todo` | P3 |
| `segment_shift` | Anteil eines Segments im TQ ändert sich um ≥ 5 pp | ≥ 30 TQ-Reels je Woche, ≥ 5 Segment-Reels, Fisher-Test, **BH-q < 0,10** über alle getesteten Segmente; nur gemeinsame Topics; die TQ-Überlappung mit der Vorwoche wird angegeben | P2 („beobachten“ bei p < 0,20 nur in der Tabelle) |
| `hook_compare` | Hook A liegt vor Hook B | n ≥ 8 je Hook, Mann-Whitney, **BH-q < 0,10** über alle Paare, Median-Verhältnis ≥ 1,5 | P3 |
| `competitor_outlier` | API: neues Reel ≥ 3× Account-Median | nur Modus `api` | P2 |
| `competitor_growth` | Follower +≥ 5 % zur Vorwoche | über der Rundungsstufe | P3 |
| `competitor_cadence` | ≥ 14 Beiträge pro Woche | exakt | P4 |
| `topic_shift` | Median einer Topic-Seite ×≥ 2 oder ×≤ 0,5 | n ≥ 8 | P4 |
| `data_quality` | > 20 % der Topics fehlgeschlagen, < 50 % Follower-Abdeckung, < 10 gemeinsame Topics, > 50 % der Watchlist ohne Embed | – | P5 |

**Formulierung:** Alerts beschreiben nur. Sie enthalten n, p/q und die Überlappung, dazu „Beschreibend, keine Ursache belegt“ bzw. „Korrelation, kein Test“. Anteile sind kompositionell: Steigt ein Segment, fallen andere mechanisch. Im Testlauf erscheint z. B. `whole_home` als Gegenbewegung zu `bedroom`.

### 5.5 Testläufe [DATEN]

| Lauf | Ergebnis |
|---|---|
| **Research-Daten komplett** (`data/raw`, 22 Batches, alle Topics) | 239 von 250 eindeutigen Slugs ok, 2.498 Reels, 822 im TQ, 12 neue Reels (18.–25.09.), 96 % mit Followerzahl. 5 Alerts, darunter ein EXTREME-Reel eines 1.000-Follower-Accounts auf `dream-house` (2,3 Mio. Views, vpf 2.300). Mit 78 Paaren gab es keinen Hook-Paarvergleich unter q < 0,10. Laufzeit < 1 s. Duplikate aus Mehrfachabrufen werden erkannt, Weiterleitungen (`slug` → `slug_used`) zusammengeführt. |
| **Baseline nur Watchlist** (`--only-watchlist`, abgelegt in [`data/monitor/2026-W39_baseline/`](data/monitor/2026-W39_baseline/report.md)) | 57 Topics, 616 Reels, 204 im TQ, 1 neues Reel. Einziger Alert: `promotional`-Hooks liegen vor `pov`-Hooks (Median-topic_index 1,78 vs. 0,31; n = 28/12; p = 0,001; q = 0,071 über 55 Paare). Im Gesamtdatensatz liegt `pov` dagegen bei 0,95 (n = 47; Stand von [analysis_digest.md](data/processed/analysis_digest.md) beim Schreiben). Der Befund gilt also nur auf den Watchlist-Topics und bei kleinem n. Genau deshalb ist er eine Hypothese und keine Regel. |
| **Synthetische Folgewoche** (Fixture aus den Research-Daten; 3 neue Reels pro Topic mit „tropical bedroom“- und „POV“-Captions eingebaut; nicht im Repo, **keine echten Daten**) | Der Wochenvergleich auf 54 gemeinsamen Topics (3 Seiten „fehlgeschlagen“) findet die eingebaute Verschiebung. Beispiel-Alert: *„Stil × Raum tropical × bedroom: Anteil an Top-Quartil-Reels von 1,0 % auf 26,2 % gestiegen (n = 2/194 → 53/202; Fisher p = 0,000, BH-q = 0,000; TQ-Überlappung 54 %)“*. Dazu: *„Hook-Typ pov liegt diese Woche vor question: Median topic_index 2,98 vs. 0,52 (n = 84/35)“*. Follower-Deltas innerhalb der Rundung („2M“ → „2.2M“) wurden korrekt **nicht** als Wachstum gemeldet. |
| **API-Fixture** (Hashtag-Seite nur mit Likes, Business-Discovery-Datei) | Die Likes-Metrik greift, der Account-Index wird berechnet (Abschnitt 7b im Report). Die Graph-API-Zeitstempel im Format `+0000` werden gelesen. |

Statistik-Funktionen gegen scipy geprüft: Fisher exakt und Mann-Whitney (asymptotisch, ohne Stetigkeitskorrektur) liefern identische p-Werte.

### 5.6 Outputs pro Woche

| Datei | Inhalt | Wofür |
|---|---|---|
| `report.md` | Datenbasis, Alerts, neue Reels, Ausreißer, Segment- und Hook-Tabellen, Topics, Wettbewerber, Messgenauigkeit, Review-Checkliste | Mensch |
| `alerts.json` | alle Alerts, Hook-Paare, Validierung | Agenten, Ideenkarten |
| `monitor_reels.csv` | alle Reels mit Metriken und Segmenten | Analyse, Winner-DB-Priors |
| `monitor_segments.csv` · `monitor_topics.csv` · `monitor_competitors.csv` (+ `monitor_competitor_media.csv` im Modus `api`) | Aggregate | Zeitreihen über Wochen |
| `inspiration_candidates.csv` | bis zu 60 neue bzw. neu aufgetauchte Ausreißer; Spalten `principle_own_words`, `pillar_fit`, `test_idea`, `similarity_risk`, `decision` bleiben leer | Review |
| `watchlist_competitors_next.csv` | Watchlist mit aktualisierten Shortcodes | Review |
| `embed_todo.json` | fehlende Embed-Seiten | Workflow |

**Größe:** Der Baseline-Ordner hat 356 KB. Pro Woche fallen so weniger als 1 MB CSV/JSON ohne Medien an [DATEN].

---

## 6. Menschliche Review und Inspirations-Board

### 6.1 Ablauf G5, ca. 20–30 Minuten, montags

1. **Datenbasis prüfen:** Stoppgrund in `run_meta.json`? Fehlgeschlagene Topics? Unter 10 gemeinsame Topics → Segment-Alerts ignorieren.
2. **P1–P2-Alerts öffnen** (Reel-Link im Browser ansehen, nichts herunterladen). Für jedes übernommene Reel eine Zeile in `inspiration_candidates.csv`:
   - `principle_own_words`: die Mechanik, nicht das Motiv
   - `pillar_fit` (P1–P6 laut [08](08_content_pillars.md))
   - `test_idea`
   - `similarity_risk`
   - `decision` (board/skip)
3. **Segment- und Hook-Alerts gegenlesen:**
   - Messgenauigkeit der Dimension (Report, Abschnitt 8)
   - Überlappung
   - Kompositions-Effekt

   Übernommen wird nur als Hypothese.
4. **Watchlist:**
   - `watchlist_competitors_next.csv` übernehmen
   - Accounts ohne Embed-Daten prüfen (umbenannt oder gelöscht? `handle_mismatch`)
   - Neue Kandidaten aus `emerging`-Treffern höchstens monatlich aufnehmen
5. **Eigener Account Status** in der App (nur manuell möglich, [q01, Abschn. 2 (4)](quellen/q01_instagram_platform_rules.md)).
6. **Entscheiden:** höchstens 2 Hypothesen in die `tests`-Tabelle (Abschnitt 7).

### 6.2 Board-Regeln: Prinzipien ja, Kopien nie

**Warum:** Instagram empfiehlt bei identischen Inhalten *"only … the original one"*. Accounts, die überwiegend nicht-originale Inhalte posten, werden aus Empfehlungen ausgeschlossen. Als nicht original gilt auch bloßes Reposten *"without adding meaningful creative input"* ([q01, Abschn. 2 (2)](quellen/q01_instagram_platform_rules.md), [VERIFIED]). Ein nachgebautes Wettbewerber-Motiv ist zudem ein Rechts- und Reputationsrisiko ([q07](quellen/q07_legal_ai_risk.md), keine Rechtsberatung):
- Reine Prompt-Outputs sind wahrscheinlich nicht urheberrechtlich geschützt, wohl aber menschliche Auswahl, Anordnung und Bearbeitung, also etwa der Schnitt eines fremden Reels (q07 §2.3, [ESTIMATED]).
- Wer erkennbar fremde Designs, Marken oder reale Innenräume übernimmt, riskiert Urheber-, Design- und Markenverletzungen; Meta entfernt Accounts bei wiederholten IP-Verstößen (q07 §2.4, [VERIFIED]).
- Outputs sind nicht exklusiv: *"SIMILAR OUTPUTS MAY BE GENERATED FOR OTHER USERS"* (Runway-AGB, q07 §2.3). Deshalb bleibt die Ähnlichkeitsprüfung auch für eigene Motive Pflicht.

| Erlaubt im Board | Nicht erlaubt |
|---|---|
| Link zum Reel, Kennzahlen, Codebuch-Tags | Bild- oder Video-Dateien, Screenshots, Cover-Downloads |
| Mechanik in eigenen Worten: z. B. „Ausblick zuerst, Raum per Rückfahrt“, „Frage-Hook mit zwei Optionen“, „Regen am Fenster als Ambient-Loop über 1 Szene“ | Szene, Komposition oder Farbpalette nachbauen; Prompt „im Stil von @handle“; Caption-Text übernehmen oder paraphrasieren |
| Übersetzung in **eigenes** Motiv. Abstandsregel: mindestens 2 von 4 Dimensionen verschieden (Raum, Stil, Setting, Palette), eigene Komposition | Referenzbilder von Wettbewerbern im Generator |
| Ähnlichkeitsprüfung des Ergebnisses per pHash/CLIP und Reverse Search nach [16, Abschn. 4.4](16_automation_strategy.md) | Veröffentlichen ohne Ähnlichkeitsbefund |

**Vorlage:** [`data/monitor/inspiration_board.csv`](data/monitor/inspiration_board.csv), eine EXAMPLE-Zeile.

**Felder:**
- `added_week`, `source_url`, `source_handle`
- `source_topic_index`, `source_vpf`
- `pillar` (Playbook-Pillar, Werte wie `playbook_pillar` in [15 §5.2](15_kpi_framework.md)), `mechanism_type` (hook_opening, format, camera, setting, composition, caption, cta, audio)
- `principle_own_words`, `why_hypothesis`, `our_translation`, `distance_check`
- `monitor_alert_ref`, `test_id`
- `status` (idee, im_test, behalten, verworfen), `notes`

**Beispiel für `our_translation`:** Eigenes `UNBUILT`-Konzept: Steinbad in einem gespaltenen Findling bei Nacht, Rückfahrt durch den Felsspalt zur freistehenden Wanne, Hook-Text *"This bathroom has one rule"*.

---

## 7. Anbindung an Winner-DB und Testmatrix

### 7.1 Vom Alert zum Test

| Schritt | Was | Wo |
|---|---|---|
| 1 | Alert oder Board-Prinzip wird zur **Hypothese mit genau einem Faktor**, z. B. „`hook_type` = choice schlägt question bei luxury_room“ | Review |
| 2 | Zeile in `tests`: `test_id` mit fortlaufender Nummer ab `T28`, weil `T01`–`T27` in der [Testing-Matrix](13_testing_matrix.csv) vergeben sind (z. B. `T28_choice_vs_question`), `hypothesis` mit Monitor-Beleg („Monitor 2026-W40: Median topic_index 1,8 vs. 0,9, n = 12/15, q = 0,06“), `factor`, `primary_kpi = log_views_24h`, `min_n_per_variant = 6`, `status = planned` | [Winner-DB-Schema](data/winner_database_schema.sql), [15, Abschn. 5](15_kpi_framework.md) |
| 3 | Varianten in `variants` anlegen (Kontrolle `control`, Varianten `B`/`C`); Reels neu generieren, **nie** als identischen Re-Upload; ein Tagesblock prüft genau eine Variable | [15, Abschn. 4.5](15_kpi_framework.md), [14 §5](14_30_day_launch_plan.md) |
| 4 | Entscheidung KEEP / ITERATE / SCALE / KILL **nur auf eigenen Daten** mit `scripts/winner_analysis.py` | [15, Abschn. 4](15_kpi_framework.md) |
| 5 | Nach 8 Wochen Treffer-Quote messen: Anteil der Tests aus dem Monitor mit KEEP oder SCALE, verglichen mit Tests aus anderen Quellen | Abschnitt 8.3 |

**Feld-Zuordnung Monitor → Winner-DB:**

| Monitor | Winner-DB | Hinweis |
|---|---|---|
| `topic_group` | `pillar` | Research-Themengruppe; identische Wertelisten ([topic_groups.py](scripts/topic_groups.py)) |
| `pillar_fit` (Review) bzw. `pillar` (Board) | `playbook_pillar` | `p1_impossible_homes` … `p6_statement_rooms` ([15 §5.2](15_kpi_framework.md)) |
| `hook` (Codebuch) | `hook_type` | `descriptive` und `promotional` gibt es im Schema nicht, daher als `none` bzw. nicht als Testfaktor verwenden |
| `kw_room` | `room` | `office_library` → `office`, `whole_home` → `exterior_facade` oder `multi_room_tour` |
| `kw_style` | `style` | `cozy_rustic` → `rustic_cozy`, `classical` → `classical_luxury`/`neoclassical`, `biophilic` → `biophilic`/`organic_modern` |
| `kw_setting` | `landscape` | `mountain_snow` → `mountain`/`snow`, `jungle` → `jungle_tropical`, `rain` → `rain_window` |

### 7.2 Einbau in die Testmatrix der Folgewoche

**Launch-Monat (Tag 1–30):** Die Slots sind durch den Tagesplan in [14](14_30_day_launch_plan.md) und die 27 Tests der [Testing-Matrix](13_testing_matrix.csv) fest vergeben. Monitor-Hypothesen gehen nur in die Pilot-Slots der Wochen 3–4 (`T18_location`, `T26_p4_view`, `T27_style_explore`) und ändern keine laufenden Tests ([14 §8](14_30_day_launch_plan.md)).

**Ab Monat 2:** [15, Abschn. 4.5](15_kpi_framework.md) sieht pro Woche vor:
- 7 Champion-Slots
- 10 Thompson-Slots
- **4 Explorations-Slots**

Dazu kommen Replikationen aus Monat 1 und höchstens ein neuer Ein-Faktor-Test. [16, Abschn. 2](16_automation_strategy.md) nennt für Ideen den Mix 70 % Gewinner-Varianten, 20 % Nachbarthemen, 10 % Experimente [ANNAHME].

**Der Monitor speist nur Pilot- bzw. Explorations-Slots und höchstens einen Ein-Faktor-Test:**

| Monitor-Signal | Slot | Beispiel |
|---|---|---|
| Segment-ALARM (z. B. tropical × bedroom steigt) | 2 der 4 Explorations-Slots mit **eigenen** Motiven dieses Segments, in der Markenwelt aus [11](11_brand_style_guide.md) (Nacht, Palette, „The Visitor“) | tropisches Konzept mit Dschungelblick bei Nacht in einer passenden Pillar; KI-Schlafzimmer nur als Variante in P2 ([08 §4](08_content_pillars.md)) |
| Hook-Paarvergleich unter q < 0,10 | nächster Ein-Faktor-Test (`T28` ff.), je Variante ≥ 6 Reels; die übrigen Faktoren bleiben auf dem Champion-Rezept | `choice` vs. `question` bei gleichem Motivtyp |
| neuer EXTREME-Ausreißer eines Wettbewerbers | Board-Prinzip → 1 Explorations-Slot | „View-first opening“ in eigenem Motiv |
| `topic_shift` / Frische hoch | kein Slot; Watchlist bzw. Hashtag-Auswahl prüfen | – |

**Grenzen:**
- Pro Woche höchstens **2 neue** Monitor-Hypothesen.
- Kein Monitor-Signal ersetzt Champion-Slots.
- Laut [15, Abschn. 4.6](15_kpi_framework.md) sind mit 6 Reels pro Stufe erst Effekte ab etwa ×5 sicher erkennbar. Monitor-Tests laufen daher über 2–3 Wochen, oder mit Trial Reels, sobald berechtigt (≈ 1.000 Follower, [ESTIMATED], [q01, Abschn. 2 (5)](quellen/q01_instagram_platform_rules.md)).
- Ein Test-Arm muss die Rechtsregeln aus [15 §3.6](15_kpi_framework.md) und [16 §4.5](16_automation_strategy.md) einhalten (KI-Kennzeichnung, keine Marken- oder Hotelnamen, Orte nur als Setting). Ein Monitor-Signal, das nur mit einem realen Ort, Hotel oder Preis funktioniert, wird nicht getestet.

---

## 8. Betrieb

### 8.1 Zeitplan

| Takt | Was |
|---|---|
| wöchentlich, Mo 06:51 | Routine: Erhebung und Report (Modus `api` oder `webfetch_permitted`) |
| wöchentlich, Mo 09:30 bis 10:51 | Modus `manual`: Owner speichert die Seiten, danach läuft die Routine |
| wöchentlich, Mo | Review G5 (20–30 Min.) |
| monatlich | Watchlist-Pflege (≤ 5 Topic-Tausche; Wettbewerber aufnehmen oder streichen); im Modus `manual` Embed-Seiten der 10 wichtigsten Wettbewerber |
| quartalsweise | `build_watchlists.py` neu ausführen, Keyword-Regeln gegen neue Codes prüfen (Abschnitt 8 im Report), Schwellen justieren |

### 8.2 Speicherung

```
data/monitor/
  2026-W39_baseline/          # Beispiel und Referenz (aus data/raw; Rohdaten bleiben in data/raw)
  2026-W40/ …                 # ein Ordner pro ISO-Woche: Rohdaten + Outputs
  inspiration_board.csv       # dauerhaft, nur Links + Text
scripts/monitor/watchlist_*.csv   # Inputs, versioniert per Git
```

- **Versionierung:** wöchentlicher Commit in einen eigenen Branch `monitor/2026-Www`, Merge nach der Review.
- **Vorwoche:** wird automatisch gefunden (nächstälterer Wochenordner mit `topics/`).
- **Follower-Verläufe:** kommen aus allen Wochenordnern (Spalte „Verlauf“ im Report).

### 8.3 Monitor überwachen

| Kennzahl | Soll [ANNAHME] | Wenn verfehlt |
|---|---|---|
| Topic-Seiten ok | ≥ 90 % | Stoppgrund prüfen. Bei 2 Stopps in Folge nicht weiter erheben, sondern auf `api`/`manual` wechseln. |
| Reels mit Followerzahl | ≥ 80 % | `--todo-max` erhöhen, sofern das Volumen-Limit es erlaubt |
| Caption-Codes | ≥ 80 % in beiden Wochen | Sonst fällt der Hook-Vergleich auf die Heuristik zurück; das steht im Report |
| Gemeinsame Topics | ≥ 45 von 57 | Watchlist stabil halten |
| Monitor-Tests mit KEEP/SCALE nach 8 Wochen | höher als bei Tests anderer Herkunft | Sonst Monitor auf monatlich reduzieren |

---

## 9. Offen und zu verifizieren

| # | Frage | Status |
|---|---|---|
| 1 | Schriftliche Erlaubnis für automatisierte Erhebung (Voraussetzung für `webfetch_permitted`); Inhalt der Meta Automated Data Collection Terms | zu verifizieren |
| 2 | Business Discovery: nötige Berechtigungen, Rate-Limits, Anzahl zurückgegebener Medien; Verfügbarkeit von `view_count` für Reels anderer Accounts im Praxistest | laut Doku `view_count` vorhanden [VERIFIED]; Praxis zu verifizieren |
| 3 | Hashtag Search: Rückgabefelder von `top_media` (Likes, Views?), App-Review-Aufwand | zu verifizieren |
| 4 | Enthalten im Browser gespeicherte `/popular/`-Seiten Reel-Links und Views (Modus `manual`)? | beim ersten Lauf prüfen |
| 5 | DSGVO: Speicherung von Handles und Kennzahlen natürlicher Personen; berechtigtes Interesse, Aufbewahrung, Auskunft | zu verifizieren ([q07](quellen/q07_legal_ai_risk.md) behandelt die DSGVO nicht) |
| 6 | Workflow-Tool in Routine-Sessions; Headless-Flags des `claude`-CLI für Server-cron | zu verifizieren |
| 7 | Keyword-Regeln sind auf den Research-Daten entwickelt; Übereinstimmung auf neuen Wochen | läuft automatisch mit (Report, Abschnitt 8) |

---

## Quellen und Daten

- [quellen/q01_instagram_platform_rules.md](quellen/q01_instagram_platform_rules.md): Rankingsignale (Watch Time, Likes, Sends), Originalität und Empfehlungsausschluss, Trial Reels, Account Status
- [quellen/q07_legal_ai_risk.md](quellen/q07_legal_ai_risk.md): Urheberrecht an KI-Outputs, Marken und Designs, Meta-IP-Policy; behandelt nicht die automatisierte Datenerhebung, DSGVO oder Datenbankrecht
- [README – Compliance-Hinweis](README.md): Nutzung der Research-Rohdaten, Erhebungsmodi
- `https://www.instagram.com/robots.txt`: per WebFetch abgerufen am 2026-09-25 (Wortlaut in 2.1)
- Meta-Entwicklerdoku [Business Discovery](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/business-discovery) und [Hashtag Search](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/hashtag-search), abgerufen am 2026-09-25 (ohne Datumsangabe auf den Seiten)
- [15_kpi_framework.md](15_kpi_framework.md): Winner-DB, Testplan, statistische Grenzen · [16_automation_strategy.md](16_automation_strategy.md): Gates, Ähnlichkeitsprüfung, 70/20/10 · [13_testing_matrix.csv](13_testing_matrix.csv), [14_30_day_launch_plan.md](14_30_day_launch_plan.md): Tests und Review-Ritual im Launch-Monat · [08_content_pillars.md](08_content_pillars.md): Pillars P1–P6
- Research-Rohdaten `data/raw/` (Topic-Sweep und Embeds vom 2026-09-25), [`scripts/cover_codebook.md`](scripts/cover_codebook.md), [`data/processed/analysis_digest.md`](data/processed/analysis_digest.md)
