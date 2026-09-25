# 15 – KPI-System und Winner-Datenbank (Teil 30 + 31)

**Stand:** 25.09.2026 · **Für:** neuen internationalen (englischsprachigen) Instagram-Theme-Account mit überwiegend KI-generierten Reels zu Luxury Interiors, Future Homes und Architektur · **Test-Setup:** 3 Reels pro Tag über 30 Tage (≈ 90 Reels)

**Dateien zu diesem Kapitel**

| Datei | Inhalt |
|---|---|
| [data/winner_database_template.csv](data/winner_database_template.csv) | Eingabevorlage: 1 Zeile = 1 Reel, 56 Felder plus 3 Zusatzspalten aus dem Launch-Plan (`plan_id`, `cover_type`, `caption_len`), 3 fiktive `EXAMPLE`-Zeilen (Tagesblock `T01_format` aus [14](14_30_day_launch_plan.md)) |
| [data/winner_database_schema.sql](data/winner_database_schema.sql) | SQLite-Schema (Codebook v1.1): `reels`, `variants`, `tests`, `daily_snapshots` sowie `prompts`, `series` (mit den Flagship-Serien als Stammdaten), `account_daily`, `affiliate_daily`, `codebook` und drei Views |
| [scripts/winner_analysis.py](scripts/winner_analysis.py) | Wochenanalyse: Lifts mit Bootstrap-KIs, Ridge-Regression, KEEP/ITERATE/SCALE/KILL, Thompson Sampling, Rekalibrierung |
| [13_testing_matrix.csv](13_testing_matrix.csv), [14_30_day_launch_plan.md](14_30_day_launch_plan.md) | verbindliches Testdesign für Monat 1 (27 Tests, Tag-für-Tag-Plan); ersetzt das frühere Beispiel-Design dieses Kapitels (Abschnitt 4.5) |

**Kennzeichnung:** Die Status-Tags `[VERIFIED]`, `[ESTIMATED]`, `[THIRD-PARTY ESTIMATE]` und `[UNKNOWN]` sind wie in den Quellennotizen verwendet. Für die Herkunft der Zielbänder gilt: **B** = aus unserem Research-Datensatz abgeleitet, **P** = Plattformquelle, **S** = Setzung bzw. Arbeitshypothese ohne externe Evidenz.

**Abgleich mit der finalen Strategie (25.09.2026):** Pillars P1–P6 und Serien aus [08](08_content_pillars.md) und [11](11_brand_style_guide.md) sind in der Winner-DB als `playbook_pillar`, `series_id` und `series_family` abgebildet (Abschnitt 5.2). Das Testdesign in Abschnitt 4.5 folgt [13](13_testing_matrix.csv) und [14](14_30_day_launch_plan.md). Die Rechtspunkte (KI-Kennzeichnung, Werbung, Marken, Orte und Preise, Musik) stützen sich jetzt auf [q07](quellen/q07_legal_ai_risk.md) (Abschnitte 3.6 und 4.7). Die Kruskal-Werte in Abschnitt 0 entsprechen dem aktuellen [Digest](data/processed/analysis_digest.md).

---

## 0. Kurzfassung

1. **North Star:** qualifizierte Follows pro Woche. Sie ergeben sich aus der Nicht-Follower-Reichweite × dem Anteil der Zielmärkte × den Follows pro 1.000 Views. Je Reel steuern wir mit zwei Größen: **F/1k** (Follows pro 1.000 Views) und **account_index** (views_24h ÷ Median der letzten 15 eigenen Reels).
2. **Frühindikatoren nach Instagram-Aussage:** Watch Time, Likes und Sends sind laut Mosseri die drei wichtigsten Ranking-Signale. Sends zählen bei „unconnected content“ etwas mehr ([q01](quellen/q01_instagram_platform_rules.md), Kernbefund 1). Für einen neuen Account mit fast nur Nicht-Follower-Reichweite heißt das: **Sends/Reach** und **% angesehen** sind die wichtigsten Frühindikatoren, danach **Likes/Reach**.
3. **Messlücke:** Follows und Profilbesuche pro Reel liefert die Graph API für Reels nicht. Diese Metriken gibt es dort nur für Feed und Story `[VERIFIED, Meta-Entwicklerdoku, abgerufen 25.09.2026]`. Wir tragen sie deshalb von Hand aus der App ein; ob die App sie je Reel anzeigt, ist **zu verifizieren**. Auch views_1h, views_6h und views_24h kommen nur aus der App, weil API-Daten bis zu 48 h verzögert sein können.
4. **Öffentliche Daten zeigen keine Gewinner-Stile:** Im Research-Datensatz unterscheiden sich Stil, Raum und Caption-Hook nicht signifikant (Kruskal-Wallis topic_index p = 0,74 / 0,75 / 0,53; größenbereinigt p = 0,17 / 0,93 / 0,35). Größenbereinigt robust sind nur der Realismusgrad (p = 0,0011; im topic_index p = 0,052) und der Account-Typ (p < 0,001). Die visuelle Qualität ist im topic_index robust (p < 0,001), größenbereinigt nur nominal (p = 0,013) ([analysis_digest.md](data/processed/analysis_digest.md)). Das sind Korrelationen auf Top-Reels. **Gewinner-Faktoren müssen wir also im eigenen Account testen.** Dafür ist die Winner-Datenbank da.
5. **Statistische Realität:** Innerhalb eines Accounts streuen die Views stark: Die Median-Standardabweichung von log(Views) liegt bei 1,38 (104 Research-Accounts mit ≥ 3 Reels). Mit 90 Reels lassen sich deshalb nur große Effekte sicher erkennen, etwa ab dem Faktor 2,3 bis 5. Konsequenz: wenige Faktoren gleichzeitig testen, auf Faktor-Ebene entscheiden (nicht je Kombination) und Gewinner replizieren.
6. **Entscheidungsregeln:** **SCALE** gilt ab n ≥ 6, Gruppen-Index ≥ 1,5, P(besser) ≥ 95 % und F/1k ≥ Kontoschnitt. **KILL** gilt ab n ≥ 6, Gruppen-Index < 0,6, P(schlechter) ≥ 95 % und NS-Index < 0,6. **ITERATE** greift bei einer Diagnose: „Reichweite ohne Follows“ oder „Inhalt gut, Verpackung schwach“. Ein Policy-Problem bedeutet sofort **KILL**. Die Regeln wurden per Simulation kalibriert (Abschnitt 4.6). Sie sind identisch mit [14](14_30_day_launch_plan.md), Abschnitt 6.3. In Monat 1 kommt davor die **Test-Ebene** aus [13](13_testing_matrix.csv): gepaarte Tagesblöcke mit VORLÄUFIGER GEWINNER / PAUSIEREN / OFFEN (Abschnitt 4.5).
7. **Commerce-KPIs steuern wir erst ab Monat 2.** Im Launch-Monat wird nur das Tracking vorbereitet (Sub-ID je Reel bzw. Serie). Grober Überschlag: Affiliate bringt ≈ 0,3–3 USD pro 1.000 Views, Sponsoring-Benchmarks liegen bei 9–20 USD pro 1.000 Views (Drittangaben, Abschnitt 3.8). Reichweite ist also vor allem für Sponsoring und B2B wertvoll.

---

## 1. Datenquellen und Messgrenzen

### 1.1 Was wir woher bekommen

| # | Quelle | Liefert | Grenzen | Status |
|---|---|---|---|---|
| 1 | **Instagram-App, Insights** (eigener Professional-Account) | Pro Reel: Views, Reach, Likes, Kommentare, Shares, Saves, Watch Time. Laut Drittquellen zusätzlich Skip Rate, Anteil Follower/Nicht-Follower, Follows und Profilaktivität je Reel. | Die genaue Feldliste ist **zu verifizieren**: beim ersten Reel einen Screenshot der Insights-Seite ablegen. Nur manuell abrufbar, Werte laufen weiter, daher Zeitpunkt protokollieren. | ESTIMATED (Skip Rate laut Drittquellen seit Aug. 2025, [q01](quellen/q01_instagram_platform_rules.md)) |
| 2 | **Graph API, Media Insights** (Reels, Business/Creator-Account mit verbundener App) | `views`, `reach` (geschätzt), `likes`, `comments`, `shares`, `saved`, `reposts`, `total_interactions`, `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time` (inkl. Replays), `reels_skip_rate` (Anteil der Views mit Abbruch in den ersten 3 s; „in development“, geschätzt), `crossposted_views`, `facebook_views` | `follows`, `profile_visits` und `profile_activity` gibt es **nur für FEED und STORY, nicht für REELS**. Daten können bis zu 48 h verzögert sein und werden bis zu 2 Jahre gespeichert. | VERIFIED ([Meta-Doku Media Insights](https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights), abgerufen 25.09.2026) |
| 3 | **Graph API, Konto-Insights** | `follows_and_unfollows` (erst ab 100 Followern), `reach` aufgeschlüsselt nach `follow_type`, `views` nach `follower_type`, `engaged_audience_demographics` (Land/Stadt/Alter/Geschlecht, ab 100 Interaktionen), `profile_links_taps` | `profile_links_taps` zählt nur Taps auf die Buttons für Adresse, Anruf, E-Mail und Text, **nicht auf Bio-Links**. `impressions` ist seit v22.0 (21.04.2025) abgeschaltet. | VERIFIED ([Meta-Doku User Insights](https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights), abgerufen 25.09.2026) |
| 4 | **Eigenes Link-Tracking** (Bio-Link-Tool mit Klickzählung, UTM oder Redirect je Reel/Serie) | `link_clicks` je Reel bzw. Serie | Eine Zuordnung ist nur über einen eigenen Link bzw. eine Sub-ID je Reel oder Serie möglich. | – |
| 5 | **Affiliate-Netzwerke** (Amazon, LTK, Awin, Rakuten …) | Klicks, Bestellungen, Provision je Sub-ID | Kurze Fenster, z. B. Amazon 24 h plus Warenkorb-Regel. LTK schrieb 2022: *"Instagram does not have a cookie window"*, deshalb ist eine niedrige Conversion zu erwarten ([q02](quellen/q02_furniture_affiliate_commerce.md)). | VERIFIED (LTK: Stand 2022) |
| 6 | **Research-Datensatz** ([04_reel_database.csv](04_reel_database.csv), [analysis_digest.md](data/processed/analysis_digest.md)) | Benchmarks fremder Top-Reels für Views, VPF, Likes/View und Kommentare/View | Abgefragt wurden 264 öffentliche Topic-Seiten `instagram.com/popular/<slug>/` (ohne Login, per WebFetch, 25.09.2026), als **einmalige** Stichprobe. Instagrams `robots.txt` untersagt automatisierte Erhebung ohne schriftliche Erlaubnis; Wettbewerbsdaten kommen künftig nur über die Graph API (Business Discovery), manuell oder mit Erlaubnis ([README – Compliance-Hinweis](README.md), [17 §2](17_competitor_monitor.md)). Mit Daten ausgewertet sind 239 Topics und 2.479 Reels, je Seite ~12 Top-Reels. Daraus folgt ein **Survivorship-Bias nach oben**. Views sind gerundet wie angezeigt. Likes und Kommentare sind exakt, Follower gerundet (öffentliche Embed-Seiten). Shares, Saves und Watch Time sind öffentlich nicht verfügbar. Cover-Codes wurden von Agenten vergeben und sind daher geschätzt. Die Inter-Coder-Reliabilität ist mit [scripts/reliability.py](scripts/reliability.py) gemessen: 36 Reels doppelt codiert, Cohens κ 0,63–1,0 ([reliability.csv](data/processed/stats/reliability.csv)); `visual_quality` ist darin nicht enthalten. | B |

### 1.2 Konsequenzen für die Erfassung

- **views_1h, views_6h, views_24h** werden manuell in der App zum jeweiligen Zeitpunkt abgelesen (Toleranz ±20 min bei 1 h/6 h, ±2 h bei 24 h). Die API liefert nur kumulierte Lifetime-Werte, teils bis zu 48 h verzögert. Einen 24-h-Stand kann man nachträglich **nicht** rekonstruieren.
- **followers_gained, profile_visits, non_follower_reach_pct und completion_rate** werden am 7-Tage-Stichtag aus der App übernommen; ob die App alle diese Werte zeigt, ist zu verifizieren.
  - Fallback für Follows (erst ab 100 Followern): die Tages-Follows des Kontos anteilig auf die Reels verteilen, gewichtet nach ihrem Anteil an den Nicht-Follower-Views des Tages. In `notes` dann `follows_attributed` vermerken.
- **Alle übrigen 7-Tage-Werte** lassen sich per API automatisieren, sobald eine App verbunden ist. Bis dahin erfassen wir sie manuell.
- **Zeitstempel** immer in UTC. Mit [scripts/shortcode_time.py](scripts/shortcode_time.py) lässt sich die Uhrzeit aus dem Shortcode prüfen; das Analyse-Skript warnt bei mehr als 36 h Abweichung.

---

## 2. KPI-Baum

```
NORTH STAR   Qualifizierte Follows pro Woche
             ≈ Σ Nicht-Follower-Reichweite × Zielmarkt-Anteil × (Follows / 1.000 Views)   (Kontrolle: − Unfollows)
│
├─ A  DISTRIBUTION   bekommt das Reel Reichweite?
│      views_1h / 6h / 24h / 7d · account_index · Nicht-Follower-Anteil · Long-Tail-Anteil · VPF (ab 1.000 Followern)
│
├─ B  RETENTION      wird es angesehen?                          ← Ranking-Signal "watch time" (q01)
│      Ø Watch Time · Ø % angesehen · Skip Rate (erste 3 s) · Completion Rate
│
├─ C  RESONANZ       reagieren Menschen?                         ← "likes per reach, sends per reach" (q01)
│      Sends/Reach · Likes/Reach (Likes/View für Benchmarks) · Saves/Reach · Kommentare/View
│
├─ D  CONVERSION     wird aus einem Zuschauer ein Follower?
│      Profilbesuche/View · Follow-Conversion (Follows ÷ Profilbesuche) · F/1k
│
├─ E  KONTO-GESUNDHEIT   Gates, keine Optimierungsziele
│      Account Status · 100 % eigene Generierung, 0 Wasserzeichen · KI-Label-Quote · ≤ 5 Hashtags · QA-Gate · Unfollows
│
└─ F  COMMERCE (ab Monat 2)
       Link-Klicks · Klicks/1.000 Reach · CTR Profil→Link · Affiliate-Conversion · EPC · RPM · Umsatz/Reel · Media-Kit-KPIs
```

**Wirkungslogik:** Instagram zeigt jeden „eligible“ Inhalt zuerst einem kleinen Publikum und weitet die Verteilung nach der Performance aus, unabhängig von der Followerzahl ([q01](quellen/q01_instagram_platform_rules.md), Kernbefund 1). A, B und C bestimmen die Verteilung, D wandelt sie in den North Star um, E entscheidet, ob überhaupt verteilt wird.

**Diagnose immer von unten nach oben lesen:**

| Symptom | Engpass | Maßnahme |
|---|---|---|
| Views hoch, F/1k niedrig | Conversion (D) | Profil, Serienbindung, CTA überarbeiten |
| Views niedrig, Sends/Retention gut | Packaging | Hook, Cover, erste Sekunde ändern |
| Views niedrig, Retention schlecht | Inhalt | Inhalt überarbeiten |
| Nicht-Follower-Anteil niedrig | Eligibility (E) | Konto-Gesundheit prüfen |

---

## 3. KPI-Katalog

Alle Zielbänder sind **Anfangshypothesen für die ersten 14 Tage** und in der Reihenfolge schwach / ok / gut / stark angegeben. An Tag 14 (n ≈ 42 Reels) ersetzen wir sie durch eigene Perzentile: schwach < P25 ≤ ok < P50 ≤ gut < P75 ≤ stark. Die Perzentile gibt der Skript-Report in Abschnitt 8 aus. Die Gates in 3.6 bleiben absolut. Die Bänder sind im Skript als `LAUNCH_BANDS` hinterlegt.

### 3.1 North Star und Konto

| KPI | Formel | Quelle | Kadenz | Zielband Launch-Monat | Basis | Entscheidung |
|---|---|---|---|---|---|---|
| **Qualifizierte Follows/Woche** (North Star) | Σ `followers_gained` der Reels der Woche (7-Tage-Stand); Kontrolle über Konto-Follows − Unfollows | App je Reel; API `follows_and_unfollows` ab 100 Followern | wöchentlich (Mo) | Tag 30: ≥ 500 Follower (Basis), ≥ 1.000 (Stretch) | S; die Schwellen sind P: Gifts ab 500 Followern `[VERIFIED]`, Trial Reels ab ~1.000 `[ESTIMATED]` ([q01](quellen/q01_instagram_platform_rules.md)) | Gesamturteil über den Test. Unter 250 Followern an Tag 30: Pillar- bzw. Formatwechsel prüfen (S) |
| **Qualifizierte Reichweite** | Σ `reach` × `non_follower_reach_pct` × Zielmarkt-Anteil | Reach und Anteil je Reel (App/API); Zielmarkt-Anteil aus `engaged_audience_demographics` (Land) | wöchentlich | steigend Woche über Woche | S | Sinkt der Zielmarkt-Anteil, Themen/Hooks stärker auf die Zielmärkte ausrichten. Zielmärkte im Content-Plan festlegen (z. B. US/UK/CA/AU). Für Affiliate zählt vor allem der US-Anteil, weil viele der Programme in [q02](quellen/q02_furniture_affiliate_commerce.md) US-Programme sind. |
| **F/1k** (Follows pro 1.000 Views) | 1.000 × `followers_gained` ÷ `views_7d` | App je Reel | je Reel (T+7 d); pro Woche gepoolt | < 0,5 / 0,5–2 / 2–5 / ≥ 5 | S | Neben den Views das Hauptkriterium für SCALE. Hohe Views bei niedriger F/1k führt zu ITERATE (CTA, Serie, Profil). |
| **Netto-Follower-Wachstum** | followers(t) − followers(t − 7 d) | App/API | wöchentlich | – | – | Kontrollgröße für den North Star |

### 3.2 Distribution (Frühindikatoren je Reel)

| KPI | Formel | Quelle | Kadenz | Zielband Launch-Monat | Basis | Entscheidung |
|---|---|---|---|---|---|---|
| **views_1h, views_6h** | kumulierte Views bei T+1 h bzw. T+6 h | App (manuell) | je Reel | keine absoluten Bänder, nur relativ zum Median der letzten 15 Reels | S | Nur Frühwarnung, z. B. Kommentare zügig beantworten oder Story-Teaser setzen. **Keine** KEEP/KILL-Entscheidung auf 1-h- oder 6-h-Werten. |
| **views_24h** | kumulierte Views bei T+24 h | App (manuell) | täglich | Wochen-Median < 200 / 200–1.000 / 1.000–5.000 / ≥ 5.000 | S | Ergibt die vorläufige Reel-Klasse. Liegt der Median über 7 Tage unter 100, Account Status und Eligibility prüfen ([q01](quellen/q01_instagram_platform_rules.md)). |
| **views_7d** | kumulierte Views bei T+7 d | App/API | wöchentlich | – | – | Nenner der Raten; ergibt die finale Klasse |
| **account_index** | views_24h ÷ Median views_24h der vorherigen 15 Reels (bei < 3 Vorgängern: Median aller Reels) | Skript | je Reel | Flop < 0,5 · Schwach 0,5–0,8 · Solide 0,8–2 · Hit ≥ 2 | S (analog zum topic_index im Research) | Reel-Klasse und Grundlage aller Gruppenentscheidungen |
| **Nicht-Follower-Anteil** | `non_follower_reach_pct` | App je Reel (zu verifizieren); API: Konto-`reach` nach `follow_type` | je Reel / wöchentlich | < 60 / 60–80 / 80–90 / ≥ 90 % | S | Unter 60 % bei weniger als 5.000 Followern greifen die Empfehlungen nicht. Dann Account Status, Originalität und Wasserzeichen prüfen ([q01](quellen/q01_instagram_platform_rules.md)). |
| **Long-Tail-Anteil** | 1 − views_24h ÷ views_7d | Skript | je Reel | beobachten | – | Über 50 % heißt: Das Reel wird weiter empfohlen und ist ein Kandidat für eine Serie. |
| **VPF** | views_7d ÷ followers_at_post | Skript | je Reel, erst ab 1.000 Followern | Tiers wie im Research: NORMAL < 0,5 · GOOD 0,5–2 · VERY GOOD 2–5 · VIRAL 5–20 · EXTREME ≥ 20 | B: Definition wie im Research. Bei den Research-Top-Reels liegt der Median-VPF bei 2,4; 37 % erreichen ≥ 5× (n = 815, Top-Reel-Auswahl) | Vergleich mit dem Wettbewerb. Vor 1.000 Followern nicht aussagekräftig, weil fast jedes Reel „EXTREME“ wäre. |

### 3.3 Retention

| KPI | Formel | Quelle | Kadenz | Zielband Launch-Monat | Basis | Entscheidung |
|---|---|---|---|---|---|---|
| **Ø Watch Time** | `avg_watch_time` (s) | API `ig_reels_avg_watch_time` / App | je Reel | über „% angesehen“ | P (Metrik) | – |
| **Ø % angesehen** | avg_watch_time ÷ length_sec | Skript | je Reel | < 35 / 35–60 / 60–90 / ≥ 90 % | S | Werte über 100 % sind bei Loops möglich, falls Replays eingerechnet werden (zu verifizieren). Bei niedrigem Wert trotz gutem Hook den Mittelteil kürzen. |
| **Skip Rate (erste 3 s)** | Anteil der Views mit Abbruch in den ersten 3 s | API `reels_skip_rate` („in development“) / App | je Reel | > 50 / 35–50 / 25–35 / ≤ 25 % (niedriger ist besser) | S | Bei hohem Wert erste Sekunde, Hook und Cover tauschen (ITERATE Packaging). |
| **Completion Rate** | Anteil der Views bis zum Ende | App-Retention-Kurve (zu verifizieren); sonst leer lassen, **kein** Proxy | je Reel | < 15 / 15–30 / 30–45 / ≥ 45 % | S | Grundlage für Längen-Tests (`length_bucket`) |

### 3.4 Resonanz

| KPI | Formel | Quelle | Kadenz | Zielband Launch-Monat | Basis | Entscheidung |
|---|---|---|---|---|---|---|
| **Sends/Reach** | shares ÷ reach | API `shares`, `reach` / App | je Reel; pro Woche gepoolt | < 0,3 / 0,3–1 / 1–2 / ≥ 2 % | S (keine öffentlichen Share-Daten) | Wichtigster Resonanz-KPI bei Nicht-Follower-Reichweite ([q01](quellen/q01_instagram_platform_rules.md)). Hohe Sends bei niedrigen Views führen zu ITERATE Packaging. |
| **Likes/Reach** | likes ÷ reach | API | je Reel | Bänder siehe Likes/View | P (Mosseri empfiehlt, „likes per reach“ zu beobachten) | Steuergröße für den eigenen Account |
| **Likes/View** | likes ÷ views_7d | API/App | je Reel | < 1,0 / 1,0–2,5 / 2,5–3,7 / ≥ 3,7 % | B: Research-Accounts < 10k Follower P25 1,05 %, P50 2,45 %, P75 3,69 % (n = 87); über alle Größen P50 3,5 % (n = 518) | Vergleich mit dem Wettbewerb; Engagement-Qualität fürs Media-Kit |
| **Saves/Reach** | saves ÷ reach | API `saved` | je Reel | < 0,3 / 0,3–1 / 1–2 / ≥ 2 % | S; Saves nennt die Primärquelle nur für Explore ([q01](quellen/q01_instagram_platform_rules.md)) | Zeigt den Wert als Inspiration bzw. Referenz, also die Commerce-Eignung (shoppable Räume) |
| **Kommentare/View** | comments ÷ views_7d | API | je Reel | < 0,02 / 0,02–0,04 / 0,04–0,10 / ≥ 0,10 % | B: < 10k Follower P25 0,021 %, P50 0,041 %, P75 0,106 % (n = 50) | Bewertung von Choice- und Frage-Formaten. `comment_keyword`-CTAs nur vorsichtig einsetzen: *"engagement bait"* wird nicht empfohlen ([q01](quellen/q01_instagram_platform_rules.md)). Ob Keyword-CTAs darunter fallen, ist zu verifizieren. |

### 3.5 Conversion (Zuschauer → Follower)

| KPI | Formel | Quelle | Kadenz | Zielband Launch-Monat | Basis | Entscheidung |
|---|---|---|---|---|---|---|
| **Profilbesuche/View** | profile_visits ÷ views_7d | App (API liefert das für Reels nicht) | je Reel | < 0,3 / 0,3–1 / 1–2 / ≥ 2 % | S | Hoch bei niedriger Follow-Conversion heißt: Profil, Grid oder Bio sind der Engpass. |
| **Follow-Conversion** | followers_gained ÷ profile_visits | App | je Reel; pro Woche gepoolt | < 10 / 10–25 / 25–40 / ≥ 40 % | S | Unter 10 % Bio-Versprechen, Highlights, Grid-Konsistenz und angepinnte Reels überarbeiten. |
| **F/1k** | siehe 3.1 | | | | | |

### 3.6 Konto-Gesundheit (Gates, absolut)

| KPI | Messung | Quelle | Kadenz | Soll | Basis | Entscheidung |
|---|---|---|---|---|---|---|
| **Account Status** | Einschränkungen, Empfehlbarkeit | App: Einstellungen → Account Status | wöchentlich und nach jedem Einbruch | 0 Einschränkungen | P ([q01](quellen/q01_instagram_platform_rules.md)) | Bei jeder Einschränkung das betroffene Format sofort auf KILL setzen (`notes`: `POLICY: …`) und einen Einspruch prüfen. |
| **Originalitätsquote** | Anteil der Reels aus eigener Generierung und eigenem Schnitt | `prompt_id` je Reel | wöchentlich | 100 %; nie fremde Clips reposten | P: Aggregator-Schwelle *"10 or more times in the last 30 days"* (2024); ab 2026 soll die Mehrheit der Posts in 30 Tagen original sein ([q01](quellen/q01_instagram_platform_rules.md)) | Ein Verstoß bedeutet KILL. |
| **Sichtbare Generator-Wasserzeichen** | Anzahl | QA vor dem Upload | je Reel | 0 | P: Eligibility erfordert *"no visible watermarks"* ([q01](quellen/q01_instagram_platform_rules.md)) | Upload blockieren |
| **KI-Kennzeichnung** | Anteil **aller** KI-Reels mit `ai_label` = 1, d. h. In-App-Label gesetzt **und** sichtbare Kennzeichnung im Video ab Frame 0 (Badge `AI CONCEPT`, [11 §16–17](11_brand_style_guide.md)) | eigene Doku | je Reel | 100 % | P: Meta verlangt die Offenlegung fotorealistischer KI-Videos; Sanktionen sind möglich ([q01](quellen/q01_instagram_platform_rules.md)). EU AI Act Art. 50 gilt seit 02.08.2026; die Offenlegung muss spätestens bei der ersten Exposition sichtbar sein, Metadaten allein reichen nicht ([q07 §2.1](quellen/q07_legal_ai_risk.md)) | Ob das Label die Reichweite beeinflusst, ist `[UNKNOWN]`. Das Label deshalb **nicht** als Testfaktor nutzen, sondern immer setzen. Fotorealistische KI-Personen nur mit Kennzeichnung zeigen (Recommendation Guidelines, [q01](quellen/q01_instagram_platform_rules.md)). |
| **Werbe- und Affiliate-Kennzeichnung** | Anteil der Reels mit Affiliate-Link, Sponsoring oder eigenem Produkt, bei denen `ad_disclosure` gesetzt und vollständig umgesetzt ist | eigene Doku | je Reel | 100 % | P: § 5a Abs. 4 UWG, Leitfaden der Medienanstalten, Instagram-Regeln zu Branded Content, FTC ([q07 §2.7](quellen/q07_legal_ai_risk.md)) | Fehlt die Kennzeichnung, wird das Reel nicht veröffentlicht bzw. sofort korrigiert. Umsetzung siehe unten. |
| **Musiklizenz** | Anteil der Reels mit `ad_disclosure` ≠ `none`, deren Audio aus der Sound Collection stammt oder kommerziell lizenziert ist | `audio_name` + Lizenz-ID in der Sidecar-JSON ([16 §6](16_automation_strategy.md)) | je Reel | 100 % | P: Die Instagram-Musikbibliothek ist *"intended for personal, non-commercial use"* ([q07 §2.9](quellen/q07_legal_ai_risk.md)) | Trend-Musik nur auf nicht kommerziellen Reels (Test `T13_audio`, [14 §6.5](14_30_day_launch_plan.md)) |
| **Hashtags je Reel** | `hashtags_n` | eigene Doku | je Reel | ≤ 5 | P: Limit 5 seit 12/2025 ([q01](quellen/q01_instagram_platform_rules.md)) | Das Skript warnt bei mehr als 5. |
| **QA-Gate visuelle Qualität** | Selbst-Check high/medium/low vor dem Upload | eigene Doku | je Reel | nur `high` posten | B: im Research im topic_index robust signifikant (Kruskal-Wallis p < 0,001), größenbereinigt nur nominal (p = 0,013) ([Digest](data/processed/analysis_digest.md)) | `low` nicht posten, `medium` nur in Tests |
| **Unfollow-Quote** | unfollows ÷ follows | API `follows_and_unfollows` (ab 100 Followern) | wöchentlich | < 20 % | S | Ein steigender Wert heißt: Der Content passt nicht mehr zum Follow-Versprechen (Pillar-Drift). |

**Rechtliche Vorgaben aus [q07](quellen/q07_legal_ai_risk.md)** (Quellen-Notiz, keine Rechtsberatung; vor der ersten Monetarisierung anwaltlich prüfen lassen, q07 Hinweis im Kopf):

- **KI-Kennzeichnung (EU AI Act Art. 50):**
  - Art. 50 gilt seit dem **02.08.2026** ([EU-FAQ](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act), `[VERIFIED]`). Die Übergangsfrist bis 02.12.2026 betrifft nur Anbieter und nur die maschinenlesbare Markierung nach Art. 50(2), nicht die Offenlegung durch den Account-Betreiber (q07 §2.1, `[ESTIMATED]` Anwendung). Inhalte von vor dem 02.08.2026 müssen nicht rückwirkend gekennzeichnet werden `[VERIFIED]`.
  - Wer mit dem Account regelmäßig Geld verdient (Affiliate, Sponsoring), gilt als „Deployer“ und ist pflichtig (q07 §2.1, `[ESTIMATED]`).
  - Auch fiktive, aber plausible **Gebäude und Orte** können Deepfakes sein ([Draft Guidelines](https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act), Rn. 107, `[VERIFIED – Entwurf]`). Physikalisch unmögliche Szenen können herausfallen; bei kommerziellem Zweck greift die abgeschwächte Pflicht für „fiktionale“ Werke aber oft nicht. **Folge: jedes KI-Reel kennzeichnen**, auch P1.
  - Zeitpunkt: *"at the latest at the time of the first interaction or exposure"*; *"Disclosure as part of end credits does not comply"*. Das Meta-Label „AI info“ im Post-Menü genügt wahrscheinlich nicht (q07 §2.2 und §4 Nr. 4, `[ESTIMATED]`/`[UNKNOWN]`). Daher Badge im Bild ab Frame 0 plus In-App-Label plus Caption-Zeile. Das EU-Icon ist optional ([EU icons](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content)).
  - C2PA-/Provenienz-Markierungen der Tools nicht entfernen (z. B. [Higgsfield-AGB](https://higgsfield.ai/terms-of-use-agreement), q07 §2.2). Bußgeldrahmen bis 15 Mio. € oder 3 % des weltweiten Umsatzes (EU-FAQ, `[VERIFIED]`).
- **Werbe- und Affiliate-Kennzeichnung** (`ad_disclosure`, q07 §2.7 und §5 Nr. 5):
  - Tool „Paid partnership“ **plus** eigene Kennzeichnung „Werbung | Ad“ bzw. „Anzeige“ als erstes Wort, ohne Ausklappen sichtbar. „#ad“ allein reicht der deutschen Medienaufsicht nicht ([Leitfaden der Medienanstalten, Mai 2025](https://www.die-medienanstalten.de//fileadmin/user_upload/die_medienanstalten/Service/Merkblaetter_Leitfaeden/Leitfaden_Werbekennzeichnung_Online-Medien_interaktiv.pdf)).
  - Affiliate-Links: Laut Instagram *"should have the Paid partnership with label"* ([Instagram Help](https://www.facebook.com/help/instagram/128845584325492)); dazu Sternchen (*) mit Erläuterung direkt am Link, kein pauschaler Bio-Hinweis. Bei Amazon zusätzlich der Pflichtsatz ([q02](quellen/q02_furniture_affiliate_commerce.md)).
  - Video mit werblicher Hauptrolle: Dauereinblendung „Werbung“. Für US-Zuschauer verlangt die FTC die Offenlegung *"in the video and not just in the description"* ([FTC Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers)).
  - Welches Recht für einen englischsprachigen Account aus Deutschland greift, ist `[UNKNOWN]` (q07 §4 Nr. 5). Deshalb die strengere Doppelkennzeichnung.
- **Marken, reale Orte und Preise** (q07 §2.4 und §2.6):
  - Keine bekannten Marken- oder Hotelnamen zur Beschreibung fiktiver Szenen („Aman-inspired“ ist heikel, [§ 14 MarkenG](https://dejure.org/gesetze/MarkenG/14.html)); Stilbegriffe statt Namen. Keine erkennbaren Nachbildungen geschützter Designklassiker, vor allem nicht in Affiliate-„Dupe“-Kontexten. Halluzinierte Logos sind ein QA-Blocker.
  - Innenräume realer Hotels und Villen sind nicht von der Panoramafreiheit gedeckt ([§ 59 UrhG](https://dejure.org/gesetze/UrhG/59.html)).
  - Monetarisierte Posts sind geschäftliche Handlungen ([BGH PM 170/2021](https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2021/2021170.html)). „This $50M home in Dubai“ für ein fiktives Objekt ist der Kernfall der Irreführung ([§ 5 UWG](https://dejure.org/gesetze/UWG/5.html)). Orte daher nur als Setting (`Concept set in …`), Preise nur für real kaufbare Produkte mit Datum; einzige Ausnahme ist der vorregistrierte Test `T25_p2_price_labels` mit `est. build cost (concept): $X` ([13](13_testing_matrix.csv), [14 §6.5](14_30_day_launch_plan.md)).
- **Musik** (q07 §2.9): Sponsoring- und Affiliate-Reels nur mit Sound Collection (*"over 14,000 songs and sounds"*, kommerziell nutzbar) oder eigens lizenzierter Musik ([Instagram Help](https://www.facebook.com/help/instagram/402084904469945), [Music Guidelines](https://www.facebook.com/legal/music_guidelines)). Welche Post-Typen keinen Bibliothekszugriff haben, ist `[UNKNOWN]`.

### 3.7 Commerce-KPIs (ab Monat 2; im Launch nur Tracking vorbereiten)

| KPI | Formel | Quelle | Kadenz | Zielband / Referenz | Basis | Entscheidung |
|---|---|---|---|---|---|---|
| **Link-Klicks** | Klicks je Reel bzw. Serie | eigener Redirect, Bio-Link-Tool, UTM, Story-Link-Sticker | wöchentlich | Launch: Tracking-Quote 100 % (jede Serie hat eine eigene Sub-ID) | – | Voraussetzung für alle weiteren Commerce-KPIs |
| **Klicks pro 1.000 Reach** | 1.000 × link_clicks ÷ reach | Skript / View `v_reel_kpis` | wöchentlich | ab Monat 2 aus eigenen Daten | – | Welche Pillars und CTAs erzeugen Kaufinteresse (shoppable vs. Fantasy)? |
| **CTR Profil → Link** | link_clicks ÷ profile_visits | Skript | wöchentlich | ab Monat 2 | – | Angebot hinter dem Bio-Link testen |
| **Affiliate-Conversion** | orders ÷ clicks | Netzwerk-Dashboard je Sub-ID (`affiliate_daily`) | monatlich | Referenz „~1,4 %“ für Home & Furniture, nur aus Such-Snippets `[THIRD-PARTY ESTIMATE / UNKNOWN]` ([q02](quellen/q02_furniture_affiliate_commerce.md)) | – | Händler und Programme vergleichen |
| **EPC** | revenue ÷ clicks | Netzwerk | monatlich | Referenz: Wayfair 7-Day-EPC 1,52 USD, CB2 0,16 USD `[THIRD-PARTY ESTIMATE]` ([q02](quellen/q02_furniture_affiliate_commerce.md)) | – | Programmwahl |
| **RPM** | 1.000 × revenue ÷ views | Skript / View | monatlich | ab Monat 2 | – | Commerce-Pillar gegen Reichweiten-Pillar abwägen |
| **Umsatz pro Reel** | Σ revenue je `reel_id` (Sub-ID) | Netzwerk + DB (`v_affiliate_by_reel`) | monatlich | – | – | Entscheiden, welche Reels Produktlisten bekommen |
| **Media-Kit-KPIs** | Median-Reach je Reel, Nicht-Follower-Anteil, Sends- und Saves-Rate, Zielmarkt-Anteil | DB | monatlich | Benchmarks: Home-Decor „$9–$20“ pro 1.000 Views; DACH-Reels-CPM „€10–€50“ `[THIRD-PARTY ESTIMATE]` ([q03](quellen/q03_sponsors_brand_deals.md)) | – | Grundlage für Sponsoring-Pitches |

**Shoppable/Affiliate-Reels:** Laut Instagram (24.03.2026) zunächst nur in US, BR, IN, ID und TH verfügbar; Deutschland ist nicht in der Startliste. Für welchen Markt der eigene Account zählt, ist **zu verifizieren** ([q01](quellen/q01_instagram_platform_rules.md)).

**Voraussetzung für alle Commerce-KPIs:** Jedes Reel mit Affiliate-Link, Sponsoring oder eigenem Produkt trägt die Werbe- und Affiliate-Kennzeichnung aus 3.6 und nutzt nur kommerziell lizenzierte Musik ([q07 §2.7, §2.9](quellen/q07_legal_ai_risk.md)). Kaufbare Stücke werden als *"similar, not exact"* ausgewiesen, wenn sie nicht identisch sind ([q02](quellen/q02_furniture_affiliate_commerce.md)).

### 3.8 Rechenbeispiel: Affiliate-RPM (illustrativ, keine Prognose)

**Formel:** RPM = Klicks pro 1.000 Views × Conversion × AOV × Provision

| Annahme | Wert | Status |
|---|---|---|
| Klicks pro 1.000 Views | 2 | S |
| Conversion | 1,4 % | THIRD-PARTY / UNKNOWN |
| AOV Wayfair Q2 2026 | 332 USD | VERIFIED, [q02](quellen/q02_furniture_affiliate_commerce.md) |
| Provision | „up to 7%“ | THIRD-PARTY |

- **Über die Formel:** 2 × 0,014 × 332 × 0,07 ≈ **0,65 USD pro 1.000 Views**.
- **Über EPC-Referenzen:** 2 × 0,16 bis 1,52 USD ≈ **0,32–3,04 USD pro 1.000 Views**.
- **Hochgerechnet:** 1 Mio. Views/Monat ergeben bei 2 Klicks pro 1.000 Views ≈ 300–3.000 USD Provision. Die Sponsoring-Benchmarks liegen bei 9–20 USD pro 1.000 Views (Drittangaben, [q03](quellen/q03_sponsors_brand_deals.md)).

**Folgerung:** Im Launch-Monat auf Reichweite und Follows optimieren. Die Klickrate trotzdem ab Tag 1 messen, weil sie die größte Unbekannte dieser Rechnung ist.

---

## 4. Entscheidungsregeln KEEP / ITERATE / SCALE / KILL

### 4.1 Messzeitpunkte und Normalisierung

- **T+1 h / T+6 h:** nur Frühwarnung, keine Entscheidung.
- **T+24 h:** vorläufige Reel-Klasse.
- **T+7 d:** finale Werte. Gruppenentscheidungen fallen montags über **alle** bisherigen Reels (kumuliert).
- **account_index statt roher Views:** Ein wachsender Account hebt alle Views an. Ohne Normalisierung würden spätere Reels systematisch „gewinnen“.
- **Lift-Berechnung:** auf log(views_24h) − log(Rolling-Median) = log(account_index). Das ist die Voreinstellung des Skripts; `--raw-lift` rechnet unbereinigt.
- **Gruppen-Index:** Median account_index der Gruppe ÷ Median account_index aller Reels. Das neutralisiert den Wachstums-Bias des nachlaufenden Rolling-Medians.
- **NS-Index (North-Star-Index):** Gruppen-Index × (F/1k der Gruppe ÷ F/1k des Kontos). Er entspricht ungefähr dem Follow-Beitrag je Reel relativ zum Kontoschnitt.
- **Gruppen** sind die einzelnen Werte von `series_id`, `series_family`, `playbook_pillar` (P1–P6), `pillar` (Themengruppe), `format`, `hook_type`, `visual_hook` und `style` (marginal betrachtet). `playbook_pillar` und `series_family` sind seit dem Abgleich mit [08](08_content_pillars.md) dazugekommen: Der Pillar-Test `T05_pillar` und die Familien-Rotation in P1 brauchen diese Ebenen. Test-Arme werden über Tests hinweg gepoolt, z. B. alle Reels mit `hook_type = money` ([14 §6.3](14_30_day_launch_plan.md)). **Kombinationen** wie hook_type × style steuern nur die Slot-Verteilung (Thompson Sampling), nicht KILL oder SCALE. Dafür reicht n in 30 Tagen nicht: 20 Zellen ergeben ≈ 4–5 Reels je Zelle.
- **P(besser) bzw. P(schlechter):** Anteil von 2.000 stratifizierten Bootstrap-Stichproben, in denen der mittlere trendbereinigte log(views_24h) der Gruppe über bzw. unter dem der übrigen Reels liegt.

### 4.2 Reel-Klassen (je Reel, ab T+24 h)

| Klasse | account_index | Aktion (vom Skript vorgeschlagen) |
|---|---|---|
| Hit | ≥ 2,0 | Folge-Variante innerhalb von 72 h: gleiche Serie, neuer Raum oder Stil. Bei F/1k < 0,7 × Konto stattdessen Serien-CTA und Profil prüfen. |
| Solide | 0,8–2,0 | normal weiter |
| Schwach | 0,5–0,8 | Sind Sends oder Watch-% ≥ 1,2 × Konto-Median, ist der Inhalt gut und die Verpackung schwach: neuer Hook bzw. neues Cover. |
| Flop | < 0,5 | nicht wiederholen, Faktoren in der Lift-Tabelle beobachten |

In Woche 1–2 ändern Reel-Klassen den Plan nicht, weil alle Slots Test-Arme sind. Ein Hit wird notiert und ab Woche 3 als Konzept für einen K\*-Slot genutzt ([14 §6.2](14_30_day_launch_plan.md)). Ergänzend nennt 14 ein manuelles **Community-Signal** (Kommentare pro 1.000 Views ≥ 2,0 × Median der 15 Vorgänger → Kommentar-Themen als Optionen für den nächsten Pick One).

### 4.3 Gruppenregeln

Die Regeln werden in dieser Reihenfolge geprüft, die erste zutreffende gilt. Die Schwellen sind im Skript als Konstanten identisch hinterlegt.

| # | Entscheidung | Bedingung | Folge |
|---|---|---|---|
| 1 | **KILL (Policy)** | Mindestens ein Reel der Gruppe hat in `notes` den Vermerk `POLICY: …`, z. B. wegen einer Einschränkung im Account Status, eines Originalitäts-Hinweises oder eines Label-Problems. | Sofort, unabhängig von n: Format stoppen, Account Status und Einspruch prüfen. |
| 2 | **KILL** | n ≥ 6, Gruppen-Index < 0,6, P(schlechter) ≥ 95 %, NS-Index < 0,6 und keine Packaging-Diagnose | 0 Slots. Faktoren dokumentieren; frühestens nach 30 Tagen mit neuer Hypothese wieder testen. |
| 3 | **ITERATE (Nische)** | n ≥ 3, Gruppen-Index < 0,6, F/1k ≥ 1,5 × Konto | Wenig Reichweite, aber ein Follower-Magnet: Hook und Cover testen, **nicht** streichen. |
| 4 | **SCALE** | n ≥ 6, Gruppen-Index ≥ 1,5, P(besser) ≥ 95 %, F/1k ≥ 1,0 × Konto | Champion-Slots (7 pro Woche), 3–5 neue Varianten, eine Serie daraus bauen. Ab ~1.000 Followern Varianten als Trial Reels posten ([q01](quellen/q01_instagram_platform_rules.md), ESTIMATED). |
| 5 | **ITERATE (Reichweite ohne Follows)** | n ≥ 3, Gruppen-Index ≥ 1,2, F/1k < 0,7 × Konto | Serien-Kennung in den Hook, CTA `follow` gegen `save_share` testen, Bio und Grid prüfen. |
| 6 | **ITERATE (Packaging)** | n ≥ 3, Gruppen-Index < 0,8, Sends/Reach oder % angesehen ≥ 1,2 × Konto-Median | Neuer Hook, neues Cover bzw. neue erste Sekunde; den Inhalt **neu generieren**, nicht neu hochladen. |
| 7 | **ITERATE (Replizieren)** | n ≥ 6, Gruppen-Index ≥ 1,5, P(besser) < 95 % | 6 weitere Reels posten, die übrigen Faktoren dabei variieren. |
| 8 | **KEEP** | n ≥ 6, sonst | Bleibt im Rotationspool. Das Skript vermerkt „über Schnitt → SCALE-Kandidat“ bzw. „unter Schnitt → Slots reduzieren“, wenn P ≥ 95 %. |
| 9 | **OFFEN** | n < 6 | weiter testen |

**Ergänzungen außerhalb des Skripts** (manuell im Montags-Review; sie lockern oder verschärfen die Regeln nur für den Zweck der jeweiligen Pillar):

- **P2 Pick One:** Kommentare pro 1.000 Views ≥ 2,0 × Median bei Gruppen-Index ≥ 0,6 → KEEP statt KILL, weil P2 für Kommentare gebaut ist ([14 §6.3](14_30_day_launch_plan.md)). Mechanik-Check und Decay nach [08 §3, P2](08_content_pillars.md).
- **P1 Impossible Homes:** Eine Konzeptfamilie (`series_family`) mit n ≥ 6 und Gruppen-Index < 0,8 bekommt 0 Slots, die nächste Familie übernimmt. Pillar-KILL erst, wenn drei Familien (n ≥ 18) Regel 2 erfüllen ([08 §3, P1](08_content_pillars.md)).
- **P3, P4, P5, P6:** Spannungs-Check, Signatur-Check, Promote/Kill für Wildcards (n = 3 je Thema) und Aktivierungsregel für P6 laut [08 §3–§4 und §6](08_content_pillars.md).
- **Ab 1.000 Followern:** VPF-Index als Gegenprobe zum account_index ([14 §6.3](14_30_day_launch_plan.md)).

**Warum einseitig 95 % und nicht das klassische zweiseitige 95 %-KI?** Die Entscheidungen werden jede Woche überprüft und lassen sich billig umkehren. Für dokumentierte „Learnings“ verlangt die Lift-Tabelle deshalb mehr: **„belegt“** heißt 95 %-KI ohne 0 **und** Benjamini-Hochberg q < 0,10. **„Tendenz“** heißt P(Richtung) ≥ 90 %; daraus folgt nur ein Replikationstest.

### 4.4 Diagnose-Matrix

| | F/1k ≥ Kontoschnitt | F/1k < 0,7 × Kontoschnitt |
|---|---|---|
| **Gruppen-Index ≥ 1,5** | SCALE-Kandidat (Regel 4) | Reichweite ohne Follows: ITERATE, CTA/Serie/Profil (Regel 5) |
| **Gruppen-Index < 0,6** | Nische bzw. Packaging: ITERATE (Regeln 3/6) | KILL-Kandidat (Regel 2), außer Sends oder Watch sind gut: dann Packaging (Regel 6) |

### 4.5 30-Tage-Testplan mit 3 Reels pro Tag (verbindlich: 13 und 14)

Frühere Fassungen dieses Kapitels skizzierten als Beispiel ein faktorielles Startdesign (`T01_factorial`: 3 Serien × 3 Hook-Typen × 3 Stile, dabei Format und Länge über alle Reels konstant). Dieses Design ist **ersetzt**. In [08](08_content_pillars.md) und [14](14_30_day_launch_plan.md) hat jede Pillar ihr eigenes Format, ein über alle Reels konstantes Format ist deshalb nicht möglich. Verbindlich sind die 27 Tests aus [13_testing_matrix.csv](13_testing_matrix.csv) und der Tagesplan aus [14_30_day_launch_plan.md](14_30_day_launch_plan.md). Dieser Abschnitt fasst beide zusammen; bei Abweichungen gilt 14.

**Grundregeln**

- **Drei feste Slots:** 11:00, 17:00 und 23:00 UTC, auch über die Zeitumstellungen ([14 §3](14_30_day_launch_plan.md)). Im Research zeigt die Posting-Stunde keinen signifikanten Effekt (Kruskal-Wallis p = 0,85, größenbereinigt p = 0,94, [analysis_digest.md](data/processed/analysis_digest.md)). Die Kontrolle rotiert täglich über die Slots; `T24_post_slot` wertet das passiv aus.
- **Ein Tag = ein Block = ein Konzept:** Die 3 Reels eines Tages zeigen dieselbe Architektur-Idee und unterscheiden sich in genau **einer** Variable (Kontrolle K plus 2 Varianten). Verglichen wird innerhalb des Tagesblocks bzw. eines 2-Tage-Clusters derselben Woche ([14 §0](14_30_day_launch_plan.md)).
- **Varianten nie als identischen Re-Upload.** Bei identischem Content empfiehlt Instagram nur das Original ([q01](quellen/q01_instagram_platform_rules.md), Kernbefund 2). Varianten deshalb neu generieren oder neu schneiden; `prompt_id` z. B. `P0031`, `P0031-v2`.
- **Erfassung:** `test_id` = ID aus der Matrix (`T01_format` … `T27_style_explore`), `variant` = `control` für die Kontrolle und `B`/`C` für die Varianten. Kontrollen mehrerer Tests bekommen den ersten Test, die übrigen stehen in `notes` (`also_control: T09,T10`). Dazu die Zusatzspalten `plan_id` (R01–R90), `cover_type` und `caption_len` ([14 §5](14_30_day_launch_plan.md)).

**Format und Länge je Pillar**

Innerhalb eines Tagesblocks ist alles außer der Testvariable konstant. Über die Blöcke hinweg sind Format und Länge an die Pillar gebunden:

| Pillar | Serie (Badge, [11 §16](11_brand_style_guide.md)) | Format im Plan (Code, Feld 10) | Länge im Monat-1-Plan | Quelle |
|---|---|---|---|---|
| P1 Impossible Homes | `UNBUILT No. ###` | Reveal = `single_scene_ambience`; laut 08 zusätzlich `multi_scene_montage` möglich | 10 s (K0-P1); `T12_length` testet 6 / 10 / 20 s | [08 §3](08_content_pillars.md), [14 §2.1](14_30_day_launch_plan.md) |
| P2 Pick One | `PICK ONE No. ###` | `choice_compare` | 12 s | [14 §2.2](14_30_day_launch_plan.md), `T01_format` |
| P3 Dream Builds | `FROM NOTHING No. ###` | Build = `transformation_morph` | 15 s | [14 §2.2](14_30_day_launch_plan.md), `T01_format` |
| P4 Night Stories | `AFTER DARK No. ###` | Reveal = `single_scene_ambience` | 10 s | [14 §2.2](14_30_day_launch_plan.md) |
| P5 Wildcards | wechselnd | Format der nächstliegenden Kern-Pillar, im Plan Reveal | 10 s | [08 §3](08_content_pillars.md), `T05_pillar`, `T18_location` |
| P6 Statement Rooms (Reserve) | `THE ROOM No. ###` | `single_scene_ambience`; `house_tour` nur als Längentest | nicht im Monat-1-Plan | [08 §4, §7](08_content_pillars.md) |

**Folge für die Auswertung:** Pillar- und Formateffekt sind in Monat 1 nicht trennbar. `T01_format` (Reveal vs. Pick One vs. Build) und `T05_pillar` (P1 vs. P4 vs. P5) testen Bündel aus Pillar, formattypischem Hook und Länge ([13](13_testing_matrix.csv): *"Format ist ein Bündel inkl. formattypischem Hook"*). In den Gruppenregeln (4.3) liegen `playbook_pillar` und `format` deshalb weitgehend übereinander; ein Unterschied gehört dem Bündel, nicht dem Format allein. [11 §13](11_brand_style_guide.md) verweist für Monat 1 ebenfalls auf diese Längen; seine Längenregeln sind der Korridor ab Monat 2.

**Phasen** ([14 §1](14_30_day_launch_plan.md))

| Phase | Reels | Was läuft | Entscheidungen |
|---|---|---|---|
| **Woche 1** (Tag 1–7) | 21 | 7 Tests mit je einem Tagesblock (Replikat 1): `T05` Pillar, `T03` Realismus, `T02` Hook, `T04` Stil, `T01` Format, `T07` Setting, `T06` Raum | Nur POLICY- und QA-Stopps. Checks: Datenerfassung vollständig, Nicht-Follower-Anteil, Account Status. |
| **Woche 2** (Tag 8–14) | 21 | Replikat 2 derselben 7 Tests | Rollierend an Tag 10–16 je Test: VORLÄUFIGER GEWINNER / PAUSIEREN / OFFEN (Test-Ebene, unten). **Tag 13:** Champion-Rezept K\*. **Tag 14:** Launch-Bänder durch eigene Perzentile ersetzen (n = 42). |
| **Woche 3** (Tag 15–21) | 21 | Cluster aus K\* plus Geschwistern (Licht, Mensch, Kamera, Text, Audio), Hybrid-Block `T14`, P3-Block, Location-Pilot `T18`; 15 von 21 Reels bauen auf K\* auf | Ab Tag 15 Gruppenregeln aus 4.3 (n ≥ 6). **Tag 22:** K\*\* aus `T08` Licht und `T09` Mensch. |
| **Woche 4** (Tag 22–30) | 27 | Reichweite mit K\*/K\*\* (Länge `T12`, Audio, Hook, Kamera); Commerce: Hybrid Replikat 2, P2-Block (`T22` Keyword-CTA, `T25` Preis-Labels), P3-Block Replikat 2; P4-Pilot `T26` | Je Test an Tag 25–31. Abschlussreport an Tag 31, mit allen T+7d-Werten an Tag 37. |

**Test-Ebene in Monat 1** ([13](13_testing_matrix.csv), Spalte `entscheidungsregel`; [14 §6.4](14_30_day_launch_plan.md)):

- **GEPAART** (`T01`–`T14`, `T16`, `T17`, `T22`, `T25`): q = KPI(Variante) ÷ KPI(Kontrolle) im selben Block. **VORLÄUFIGER GEWINNER** bei Median q ≥ 1,5, allen q > 1 und Sekundär-KPI ≥ 0,8 × Kontrolle. **PAUSIEREN** (= KILL für Monat 1) bei Median q ≤ 0,67, allen q < 1 und Sekundär-KPI nicht ≥ 1,2×. Sonst **OFFEN**. Testspezifische Abweichungen stehen in der Matrix (z. B. `T14`, `T22`).
- **PILOT** (`T15`, `T18`, `T26`, `T27`): keine Slot-Entscheidung; Signal bei q ≥ 3 oder q ≤ 0,33 führt zur Replikation in Monat 2.
- **OVERLAY** (`T19`–`T21`, `T23`): Auswertung in zwei Sichten (alle Reels, nur Kontroll-Reels). GEWINNER nur bei Ratio ≥ 1,5 und P(besser) ≥ 95 % in beiden Sichten sowie account_index-Ratio ≥ 0,8.
- **PASSIV** (`T24`): Slot nur verschieben bei ≤ 0,67× mit P(schlechter) ≥ 95 % in beiden Sichten.
- **Verhältnis zu 4.3:** Test-Entscheidungen sind Slot-Entscheidungen für Monat 1. „Pausieren“ heißt nicht „widerlegt“: Mit 2 Paaren pausiert die Regel auch ohne echten Effekt ≈ 22–24 % der Stufen (Simulation in 14 §6.4, `[ESTIMATED]`). SCALE und KILL im Sinne von 4.3 gibt es erst ab n ≥ 6 je Gruppe. Das Skript zeigt die Tests in Report-Abschnitt 6 (`test_id` × `variant`); die gepaarten q-Werte liefert das Matrix-Snippet in [14 §8](14_30_day_launch_plan.md).

**Pillar-Mix in Monat 1** ([14 §4.3](14_30_day_launch_plan.md)): Woche 1–2 P1 38 %, P2 19 %, P3 19 %, P4 19 %, P5 5 % der 42 Reels. Über 30 Tage mit dem Default-Champion P1: P1 46 (51 %), P2 14 (16 %), P3 14 (16 %), P4 11 (12 %), P5 5 (6 %). Die Anteile aus [08 §5](08_content_pillars.md) (35/20/20/15/10) bleiben die Soll-Korridore des Strategy Brief; die Phasen-Spalten der Tabelle in 08 §5 beziehen sich auf das ersetzte faktorielle Design, der Hinweis darunter verweist auf 14. Woche 3–4 weichen bewusst ab, weil sie den Gewinner verdoppeln. **P6** ist im Tagesplan nicht enthalten. Die nächstliegende Evidenz liefert `T14_hybrid` (kaufbare Möbel), ein Pilot `THE ROOM` kommt frühestens in Monat 2 ([08 §4](08_content_pillars.md)).

**Slot-Verteilung ab Monat 2** (Vorschlag des Skripts, Report-Abschnitt 7): 7 Champion-Slots, 10 Thompson-Slots (hook_type × style), 4 Explorations-Slots für bisher ungetestete Hooks oder Stile. In Woche 3–4 sind die Slots durch 14 fest vergeben; Thompson Sampling nutzen wir erst ab Monat 2 ([14 §1](14_30_day_launch_plan.md)).

**Alte Beispiel-IDs:** Frühere Fassungen dieses Kapitels und einzelne Verweise in 08 und 11 nennen `T01_factorial`, `T02` (Format), `T03` (Länge bzw. CTA) oder `T04_audio`. In der Matrix entsprechen ihnen `T01_format`, `T12_length`, `T19_cta_question`/`T20_cta_follow`/`T22_cta_keyword` und `T13_audio`. Neue Tests ab Monat 2 bekommen fortlaufende IDs ab `T28`.

### 4.6 Statistische Grenzen und Kalibrierung der Regeln

**Kleinster sicher erkennbarer Effekt auf die Views**

Berechnung bei 80 % Power und α = 5 % zweiseitig. Als Streuung dient σ = 1,38: die Median-SD von log(Views) innerhalb von 104 Research-Accounts mit ≥ 3 Reels. Weil das eine Top-Reel-Stichprobe ist, liegt die echte Streuung eher höher.

| Reels in der Stufe | übrige Reels | erkennbarer Effekt | 95 %-KI-Halbbreite |
|---|---|---|---|
| 6 | 84 | × 5,1 | × 3,1 |
| 9 | 81 | × 3,9 | × 2,6 |
| 12 | 78 | × 3,3 | × 2,3 |
| 18 | 72 | × 2,8 | × 2,0 |
| 30 | 60 | × 2,4 | × 1,8 |
| 45 | 45 | × 2,3 | × 1,8 |

**Simulation** (`--demo`, σ = 1,2, 20 simulierte 30-Tage-Tests à 90 Reels, [scripts/winner_analysis.py](scripts/winner_analysis.py)):

| Szenario | Ergebnis |
|---|---|
| **Ohne echte Effekte** (Faktoren zufällig vertauscht), 360 Gruppenbewertungen mit n ≥ 6 | 6 falsche KILL (1,7 %) und 8 falsche SCALE (2,2 %). Das sind ≈ 0,3 bzw. 0,4 Fehlentscheidungen pro 30-Tage-Test. |
| **Stil-Effekt ×1,8** (futuristic vs. modern_luxury) | SCALE in 8 von 20 Läufen; mindestens „Tendenz +“ in 17 von 20 |
| **Hook-Effekt ×1,65** (curiosity vs. question) | SCALE in 5 von 20 Läufen; „Tendenz +“ oder „belegt“ in 9 von 20 |
| **Stil-Effekt ×0,82** (japandi) | KILL in 7 von 20 Läufen; „Tendenz −“ in 15 von 20 |

**Folgerung:** Die Regeln sind konservativ. Fehlentscheidungen sind selten, aber mittlere Effekte zeigen sich nach 30 Tagen oft nur als „Tendenz“. Das ist kein Scheitern, sondern der Replikationsauftrag für Monat 2. Einzelne Hits sind kein Beweis.

**Grenzen dieser Kalibrierung:** Die Simulation lief mit zufällig gemischten Faktoren, nicht mit dem gepaarten Blockdesign aus 14; dessen Fehlerraten stehen in [14 §6.4](14_30_day_launch_plan.md). Außerdem lief sie mit den Gruppenfeldern vor dem Abgleich. Mit `playbook_pillar` und `series_family` gibt es pro Test mehr Gruppenbewertungen und damit mehr Gelegenheiten für Fehlentscheidungen; die Rate je Bewertung sollte ähnlich bleiben, ist aber nicht neu simuliert. Die Simulationsdaten von `--demo` selbst sind unverändert, nur die Serien heißen jetzt wie in 08.

### 4.7 Leitplanken

- **Trial Reels** sind das native Testwerkzeug: Sie werden nur Nicht-Followern gezeigt, nach ~24 h ausgewertet und bei guter Performance innerhalb von 72 h automatisch geteilt. Für neue Accounts sind sie vermutlich erst ab ~1.000 Followern verfügbar ([q01](quellen/q01_instagram_platform_rules.md), ESTIMATED). In der DB `is_trial_reel` = 1 setzen; das Skript wertet es als eigenen Faktor aus.
- **Kein Engagement-Bait, keine Gewinnspiele** zur Reichweitensteigerung, keine gekauften Likes oder Follower. Sonst drohen der Ausschluss aus Empfehlungen ([q01](quellen/q01_instagram_platform_rules.md)) und verfälschte KPIs.
- **Kein Faktor mitten im Test umdefinieren.** Wird das Codebook geändert, die Version in `notes` vermerken (`codebook_v2`).
- **Slideshow- und Loop-Formate** (`slideshow_stills`, reine Text-Overlays) sind nach den Content Monetization Policies nicht monetarisierbar ([q01](quellen/q01_instagram_platform_rules.md)). Ein SCALE in diesem Format gefährdet die spätere Monetarisierung.
- **Rechtliche Leitplanken gelten für jeden Test-Arm** ([q07](quellen/q07_legal_ai_risk.md), Details in 3.6): KI-Kennzeichnung ab Frame 0 bei jedem Reel (Art. 50 AI Act seit 02.08.2026), Orte nur als Setting, keine Preise für fiktive Objekte außer als `est. … (concept)` im Test `T25`, keine Marken- oder Hotelnamen, Trend-Musik nur auf nicht kommerziellen Reels (`T13_audio`), Werbekennzeichnung doppelt. Ein Test-Arm, der eine dieser Regeln bräuchte, wird nicht gebaut. Ein Hinweis im Account Status führt zu `POLICY: …` in `notes` und damit zu KILL.

---

## 5. Winner-Datenbank (Teil 31)

### 5.1 Aufbau

```
series  1─n reels n─1 prompts                  codebook   (erlaubte Werte je Feld)
tests   1─n variants                           account_daily  (Konto je Tag: Follower, Follows/Unfollows, Reach nach
tests   1─n reels n─1 variants                                  Follower-Typ, Zielmarkt-Anteil, Bio-Link-Klicks, Account Status)
reels   1─n daily_snapshots  (T+1h, 6h, 24h, 7d, optional täglich/T+30d)
reels   1─n affiliate_daily  (Netzwerk × Sub-ID × Tag)
Views:  v_reel_kpis (views_1h/6h/24h/7d + alle Raten) · v_week_summary · v_affiliate_by_reel
```

- **Tägliche Arbeit:** CSV bzw. Google-Sheet nach [data/winner_database_template.csv](data/winner_database_template.csv), eine Zeile je Reel. Die Kennzahlen entsprechen dem 7-Tage-Stand; views_1h bis views_24h sind Zeitpunkt-Werte.
- **Auswertung:** `python3 scripts/winner_analysis.py <datei.csv>` (Abschnitt 6).
- **Langfristig:** `--to-sqlite data/winner.db` überträgt die CSV in das Schema [data/winner_database_schema.sql](data/winner_database_schema.sql). Die Snapshots erlauben beliebig viele Messzeitpunkte, z. B. T+30 d für den Long-Tail. Die CHECK-Constraints lehnen Werte außerhalb des Codebooks ab; das wurde mit jedem erlaubten Wert und einem unerlaubten getestet (zuletzt am 25.09.2026 für Codebook v1.1, 203 Einfügeversuche ohne Abweichung).
- **Stammdaten:** Das Schema legt die Flagship-Serien aus [08 §7](08_content_pillars.md) in `series` an: `S01_unbuilt`, `S02_pick_one`, `S03_from_nothing`, `S04_after_dark` und `S06_the_room` (Reserve, Status `paused`). P5-Serien heißen `S05_wild_<thema>` und entstehen beim ersten Reel. Datenbanken im alten Schema ergänzt das Skript beim Export um die neuen Spalten.

### 5.2 Feldliste

**Pflichtstufen:**

- **P** = Pflicht; das Skript meldet ein Fehlen.
- **K** = Kern; für Entscheidungen nötig.
- **O** = optional.

Alle Kennzahlen ab `views_7d` beziehen sich auf den Snapshot bei T+7 d.

**Identifikation und Timing**

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 1 | `reel_id` | text | P | Instagram-Shortcode (11 Zeichen aus `/reel/<code>/`); in der Vorlage `EXAMPLE_…` | App-URL | Primärschlüssel. Das Skript prüft das Datum gegen den Shortcode-Zeitstempel. |
| 2 | `date` | date | P | `YYYY-MM-DD` (UTC); auch `TT.MM.JJJJ` | App | Veröffentlichungsdatum |
| 3 | `time_posted` | time | K | `HH:MM` (UTC) | App / `shortcode_time.py` | Uhrzeit; zur Prüfung der Slot-Rotation |
| 4 | `followers_at_post` | int | K | ≥ 0 | App | Followerstand beim Posten; für VPF und als Kontrollgröße in der Regression |

**Test-Design**

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 5 | `pillar` | cat | P | `luxury_room`, `luxury_home`, `future_arch`, `unusual_home`, `fantasy_dream`, `cozy_ambience`, `location`, `hotel_resort`, `pool`, `architecture`, `style`, `decor_commerce`, `other` | Content-Plan | **Research-Themengruppe**, nicht die Playbook-Pillar. Teilmenge der Themengruppen aus [scripts/topic_groups.py](scripts/topic_groups.py) und damit vergleichbar mit dem Research. Zuordnung laut [14 §4.1](14_30_day_launch_plan.md): P1 = `unusual_home` (bzw. `future_arch` bei futuristischen Konzepten), P2 = `luxury_room`, P3 = `pool` bei Pool-Endzustand, sonst `architecture`, P4 = `luxury_home`, P5 = `cozy_ambience` bzw. `location`. |
| 5a | `playbook_pillar` | cat | P | `p1_impossible_homes`, `p2_pick_one`, `p3_dream_builds`, `p4_night_stories`, `p5_wildcards`, `p6_statement_rooms` | Content-Plan ([08](08_content_pillars.md)) | Pillar P1–P6 des Playbooks (P6 = Reserve). Gruppe für `T05_pillar` und die Pillar-Regeln aus 08. |
| 6 | `series_id` | text | K | `S##_kurzname`: `S01_unbuilt`, `S02_pick_one`, `S03_from_nothing`, `S04_after_dark`, `S05_wild_<thema>`, `S06_the_room` ([08 §7](08_content_pillars.md)) | Content-Plan | Flagship-Serie mit Badge und fortlaufender Nummer ([11 §16](11_brand_style_guide.md)); dieselbe Konvention nutzt [14 §4.1](14_30_day_launch_plan.md), z. B. `S05_wild_cozy_night`, `S05_wild_named_setting`. |
| 6a | `series_family` | text | O | snake_case, Konzeptfamilien aus [08 §3](08_content_pillars.md): P1 `one_rule_broken`, `the_way_in`, `under_things`, `above_the_clouds` · P2 `same_room_three_lives`, `which_door`, `your_partner_picks`, `real_pieces` · P3 `bare_ledge`, `backyard_brief`, `raw_bath`, `night_shift` · P4 `lights_on`, `arrival`, `the_late_room`; leer, wenn keine Familie | Content-Plan | Konzeptfamilie innerhalb der Serie; Grundlage für Familien-Rotation und Decay-Regeln (4.3, Ergänzungen). Freitext, damit die Novelty-Engine neue Familien ohne Codebook-Änderung anlegen kann. |
| 7 | `test_id` | text | O | IDs aus [13](13_testing_matrix.csv): `T01_format` … `T27_style_explore`; neue Tests ab `T28_…` | Testplan | Laufender Test (genau eine Variable je Tagesblock, 4.5) |
| 8 | `variant` | text | O | `control` für die Kontrolle, `B`/`C` für die Varianten (14); sonst `A`/`B`/`C` oder Stufenname | Testplan | Variante; als Kontrolle gilt `control` bzw. `A`. Weitere Tests einer geteilten Kontrolle in `notes` (`also_control: …`). |
| 9 | `is_trial_reel` | 0/1 | K | 0, 1 | App | Trial Reel (nur Nicht-Follower) |

**Content-Codierung** (Codebook v1.1, Abgleich siehe 5.3)

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 10 | `format` | cat | P | `single_scene_ambience`, `multi_scene_montage`, `house_tour`, `transformation_morph`, `before_after`, `choice_compare`, `pov_story`, `process_tutorial`, `slideshow_stills`, `real_estate_tour`, `talking_head`, `other` | Reel-Codebook | Formattyp. Playbook-Formate: Reveal = `single_scene_ambience` (P1, P4, P5; P1 auch `multi_scene_montage`), Pick One = `choice_compare` (P2), Build = `transformation_morph` (P3), `house_tour` nur als Längentest ([08 §7](08_content_pillars.md), [14 §4.1](14_30_day_launch_plan.md)). Achtung bei `slideshow_stills`: *"static images played in succession"* sind nicht monetarisierbar ([q01](quellen/q01_instagram_platform_rules.md)). |
| 11 | `hook_type` | cat | P | `curiosity`, `pov`, `aspirational`, `choice`, `question`, `status`, `money`, `location`, `fantasy`, `contrarian`, `instructional`, `none` | Reel-Codebook `text_hook_category` | Kategorie des On-Screen-Hooks. Die Hook-Formeln aus [11 §14](11_brand_style_guide.md) sind keine eigenen Codes: Impossible Fact, Hidden Layer, Wait-For und Arc werden als `curiosity`, Choice als `choice` erfasst; Fantasy-Statement (`T15`) als `fantasy`. |
| 12 | `hook_text` | text | K | wörtlich, Englisch, z. B. *"Would you sleep here?"* | – | Text des Hooks |
| 13 | `visual_hook` | cat | K | `text_hook`, `exterior_reveal`, `view_reveal`, `pool`, `bedroom`, `person_present`, `door_opening`, `unusual_architecture`, `empty_to_full`, `before_after`, `motion_immediate`, `sound_hook`, `none` | Reel-Codebook `first_2s_hooks` (hier ein Hauptwert) | Dominanter Reiz in den ersten 2 s |
| 14 | `room` | cat | K | `bedroom`, `living_room`, `kitchen`, `bathroom`, `dining`, `closet`, `home_theater`, `office`, `pool`, `terrace_outdoor`, `garden_landscape`, `exterior_facade`, `multi_room_tour`, `hotel_room`, `lobby_common`, `spa`, `stairs_hall`, `other` | beide Codebooks | Hauptraum |
| 15 | `building_type` | cat | O | `villa`, `penthouse`, `apartment`, `mansion`, `cabin_chalet`, `treehouse`, `hotel_resort`, `house`, `castle_palace`, `unusual_structure`, `none_visible` | beide Codebooks | Gebäudetyp |
| 16 | `style` | cat | P | `modern_luxury`, `minimalist`, `japandi`, `tropical`, `mediterranean`, `brutalist`, `futuristic`, `organic_modern`, `biophilic`, `scandinavian`, `dark_luxury`, `warm_luxury`, `industrial`, `cyberpunk`, `classical_luxury`, `neoclassical`, `art_deco`, `rustic_cozy`, `mid_century`, `maximalist`, `glam_feminine`, `traditional_regional`, `other` | Cover-Codebook `style_primary` | Hauptstil |
| 17 | `landscape` | cat | O | `ocean_beach`, `mountain`, `forest`, `desert`, `jungle_tropical`, `lake_river`, `snow`, `city_skyline`, `cliff`, `underwater`, `space_sky`, `rain_window`, `none` | beide Codebooks | Umgebung bzw. Ausblick |
| 18 | `lighting` | cat | O | `daylight`, `golden_hour`, `blue_hour`, `night_artificial`, `overcast_rain`, `candle_fire`, `mixed` | beide Codebooks | Lichtstimmung |
| 19 | `location` | text | O | benannter Ort (Englisch), `none` oder `fictional` | Caption/Text | Ortsbezug. Ein Ort erscheint nur als Setting (`Concept set in …`), nie als Tatsachen- oder Preisbehauptung ([q07 §2.6](quellen/q07_legal_ai_risk.md), `T18_location`). |
| 20 | `realism` | cat | K | `fantasy_impossible`, `stylized_dreamy`, `aspirational_realistic`, `real_existing` | beide Codebooks | Fantasy / Dreamy / Realistic |
| 21 | `visual_quality` | cat | K | `high`, `medium`, `low` | Cover-Codebook; Selbst-Check vor dem Upload | QA-Gate (3.6) |
| 22 | `camera` | cat | K | `static`, `slow_push_in`, `pull_back`, `pan`, `tilt`, `orbit`, `drone_aerial`, `fly_through`, `pov_walk`, `morph_transform`, `zoom`, `handheld`, `mixed` | Reel-Codebook `camera_motion` | Kamerabewegung |
| 23 | `length_sec` | num | K | > 0 und ≤ 180 | Datei | Länge. Empfohlen an Nicht-Follower werden Reels ≤ 3 min ([q01](quellen/q01_instagram_platform_rules.md)). |
| 24 | `n_scenes` | int | K | ≥ 1 (ein durchgehender Morph zählt als 1) | Schnitt | Anzahl Szenen bzw. Schnitte |
| 25 | `audio_type` | cat | K | `music_only`, `music_plus_ambient`, `ambient_nature_only`, `voiceover`, `asmr_sfx`, `silence` | Reel-Codebook | Tonspur |
| 26 | `audio_name` | text | O | Titel bzw. Quelle | – | Track; Lizenzquelle (Sound Collection oder Lizenz-ID) dokumentieren. Bibliotheksmusik nur auf nicht kommerziellen Reels ([q07 §2.9](quellen/q07_legal_ai_risk.md)). |
| 27 | `text_overlay` | cat | K | `none`, `hook_only`, `hook_plus_labels`, `continuous_text` | eigenes Feld | Menge an Bildschirmtext. Achtung: *"still or moving images with overlaid text"* sind nicht monetarisierbar ([q01](quellen/q01_instagram_platform_rules.md)). |
| 28 | `caption_type` | cat | K | `curiosity`, `pov`, `aspirational`, `choice`, `question`, `status`, `money`, `location`, `fantasy`, `contrarian`, `instructional`, `descriptive`, `promotional`, `none` | Cover-Codebook `caption_hook_category` | Typ der ersten Caption-Zeile |
| 29 | `caption_first_line` | text | O | wörtlich, Englisch | – | Erste Caption-Zeile |
| 30 | `cta_type` | cat | K | `comment_keyword`, `question_engagement`, `follow`, `save_share`, `link_in_bio`, `dm`, `shop_product`, `tag_friend`, `none` | Cover-Codebook | Handlungsaufforderung |
| 31 | `hashtags_n` | int | K | 0–5 | – | Anzahl Hashtags (Limit 5, [q01](quellen/q01_instagram_platform_rules.md)) |

**Produktion und Compliance**

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 32 | `ai_tool` | text | K | Toolnamen in Kleinbuchstaben, mehrere mit `+` verbunden; `none` bei echtem Footage | eigene Doku | Bild- bzw. Video-Tool(s) |
| 33 | `prompt_id` | text | K | `P####`, Varianten `P####-v2` | Tabelle `prompts` | Verweis auf Prompt, Seed und Referenz; Beleg für die Originalität |
| 34 | `ai_label` | 0/1 | K | 0, 1 | Upload | 1 = In-App-KI-Label gesetzt **und** Kennzeichnung im Video ab Frame 0 sichtbar (Badge `AI CONCEPT`). Nur das Label im Post-Menü oder in der Caption zählt nicht ([q07 §2.1](quellen/q07_legal_ai_risk.md)). |
| 35 | `ad_disclosure` | cat | K | `none`, `affiliate`, `paid_partnership`, `own_product` | Upload | Werbekennzeichnung nach 3.6: Tool „Paid partnership“ plus „Werbung \| Ad“ bzw. „Anzeige“ als erstes Wort; bei Affiliate zusätzlich * mit Erläuterung am Link ([q07 §2.7](quellen/q07_legal_ai_risk.md)). Anwaltliche Prüfung steht aus. |

**Distribution**

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 36 | `views_1h` | int | O | ≥ 0 | App, T+1 h ± 20 min | Frühwert |
| 37 | `views_6h` | int | O | ≥ 0 | App, T+6 h | Frühwert |
| 38 | `views_24h` | int | P | ≥ 0 | App, T+24 h ± 2 h | Basis für account_index |
| 39 | `views_7d` | int | K | ≥ views_24h | App/API, T+7 d | Nenner der Raten |
| 40 | `reach` | int | K | ≥ 0 (sollte ≤ views_7d sein) | API `reach` (geschätzt) | Erreichte eindeutige Konten |
| 41 | `non_follower_reach_pct` | num | K | 0–100 (das Skript akzeptiert auch 0–1) | App | Anteil Nicht-Follower an der Reichweite |

**Resonanz**

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 42 | `likes` | int | K | ≥ 0 | API | Likes |
| 43 | `comments` | int | K | ≥ 0 | API | Kommentare |
| 44 | `shares` | int | K | ≥ 0 | API `shares` | Sends/Shares |
| 45 | `saves` | int | K | ≥ 0 | API `saved` | Saves |
| 46 | `reposts` | int | O | ≥ 0 | API `reposts` | Reposts |

**Conversion und Retention**

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 47 | `followers_gained` | int | K | ≥ 0 | App je Reel (zu verifizieren), sonst attribuiert (`notes`) | Follows durch das Reel |
| 48 | `profile_visits` | int | K | ≥ 0 | App (nicht per API für Reels) | Profilbesuche aus dem Reel |
| 49 | `avg_watch_time` | num (s) | K | ≥ 0 | API `ig_reels_avg_watch_time` | Ø Wiedergabezeit |
| 50 | `completion_rate` | num | O | 0–1 (Eingabe in % wird umgerechnet) | App-Retention (zu verifizieren) | Anteil der Views bis zum Ende; leer, falls nicht angezeigt |
| 51 | `skip_rate` | num | O | 0–1 | API `reels_skip_rate` / App | Abbruch in den ersten 3 s |

**Commerce und Notizen**

| # | Feld | Typ | Stufe | Erlaubte Werte / Format | Quelle | Bedeutung |
|---|---|---|---|---|---|---|
| 52 | `link_clicks` | int | O | ≥ 0 | eigener Redirect / Sub-ID | Klicks, die dem Reel zugeordnet sind |
| 53 | `revenue` | num (EUR) | O | ≥ 0 | Netzwerke (Sub-ID) | Zugeordnete Provision bzw. zugeordneter Umsatz |
| 54 | `notes` | text | O | Freitext | – | Konventionen: `POLICY: …` erzwingt KILL · `follows_attributed` · `codebook_v2` · `also_control: T09,T10` (geteilte Kontrollen, 14) · `EXAMPLE` markiert Vorlagenzeilen |

**Zusatzspalten aus dem Launch-Plan** ([14 §5](14_30_day_launch_plan.md); stehen in der Vorlage, das Skript ignoriert sie, das Matrix-Snippet in 14 §8 liest `plan_id`):

| Feld | Typ | Werte | Bedeutung |
|---|---|---|---|
| `plan_id` | text | `R01`–`R90` | Plan-ID aus dem Tagesplan (Tag × Slot) |
| `cover_type` | cat | `clean`, `series_title` | Cover ohne Text bzw. mit Serien-Titel (`T21_cover_text`) |
| `caption_len` | int | Zeichen | Caption-Länge (`T23_caption_length`: kurz 51–150, lang 400–1.000) |

### 5.3 Abgleich mit den Research-Codebooks

Die kategorialen Werte stammen aus [scripts/cover_codebook.md](scripts/cover_codebook.md) (Cover und Caption) und [scripts/reel_codebook_prompt.txt](scripts/reel_codebook_prompt.txt) (Video). Eigene Reels lassen sich so direkt mit den 2.393 visuell codierten Research-Reels vergleichen ([Digest §1](data/processed/analysis_digest.md)).

- **Vereinigungsmenge bei Abweichungen:**
  - `room` enthält `stairs_hall` (nur Cover-Codebook) und `multi_room_tour` (nur Reel-Codebook); `none_person_only` entfällt, weil es für eigene Reels nicht vorkommt.
  - `style` enthält `glam_feminine` und `traditional_regional` (nur Cover-Codebook).
- **Umbenannt bzw. vereinfacht:**
  - `hook_type` = `text_hook_category`
  - `caption_type` = `caption_hook_category` (zusätzlich `descriptive` und `promotional`)
  - `camera` = `camera_motion`
  - `visual_hook` = `first_2s_hooks`, aber nur ein Hauptwert statt einer Liste
- **Neu, nicht im Codebook:**
  - `pillar` (Teilmenge der Themengruppen aus `topic_groups.py`)
  - `playbook_pillar` (P1–P6 aus [08](08_content_pillars.md), seit Codebook v1.1)
  - `series_family` (Freitext, Konzeptfamilien aus 08, seit v1.1)
  - `text_overlay`
  - `ad_disclosure`
- **Pflege:** `ALLOWED` in [scripts/winner_analysis.py](scripts/winner_analysis.py) ist die Referenz; die CHECK-Listen im SQL-Schema sind daraus erzeugt. Neue Werte immer zuerst dort ergänzen.

### 5.4 Data Dictionary: abgeleitete Kennzahlen und Konventionen

| Kennzahl | Definition | Hinweis |
|---|---|---|
| `views` | Instagram „Views“, laut API *"Total number of times IG Media has been played on Instagram"* | Ob Wiederholungen mitzählen, ist zu verifizieren. |
| `reach` | eindeutige Konten, die das Reel mindestens einmal gesehen haben | laut Meta geschätzt |
| `views_ref` | views_7d, falls leer views_24h | Nenner für alle „/View“-Raten |
| `account_index` | views_24h ÷ Median views_24h der vorherigen 15 Reels | Bei weniger als 3 Vorgängern dient der Median aller Reels als Basis (im Report mit * markiert). |
| Gruppen-Index | Median account_index der Gruppe ÷ Median account_index aller Reels | Grundlage der Gruppenregeln |
| NS-Index | Gruppen-Index × (F/1k der Gruppe ÷ F/1k des Kontos) | Follow-Beitrag relativ zum Kontoschnitt |
| F/1k | 1.000 × Σ followers_gained ÷ Σ views_ref | pro Woche bzw. Gruppe **gepoolt** (Summe durch Summe, nicht Mittel der Raten) |
| Likes/View, Kommentare/View, Profilbesuche/View | Summe ÷ Σ views_ref | gepoolt |
| Likes/Reach, Sends/Reach, Saves/Reach | Summe ÷ Σ reach | gepoolt |
| Follow-Conversion | Σ followers_gained ÷ Σ profile_visits | gepoolt |
| % angesehen | avg_watch_time ÷ length_sec | kann über 100 % liegen |
| Long-Tail-Anteil | 1 − views_24h ÷ views_7d | – |
| `vpf_7d` | views_7d ÷ followers_at_post | erst ab 1.000 Followern berechnet |
| Klicks/1.000 Reach, RPM, EPC | 1.000 × clicks ÷ reach; 1.000 × revenue ÷ views; revenue ÷ clicks | EUR |
| Lift (Views) | exp(Mittelwert trendbereinigtes log(views_24h) der Stufe − Mittelwert der übrigen) | 95 %-Bootstrap-KI, stratifiziert |
| Lift (F/1k) | (F/1k der Stufe) ÷ (F/1k der übrigen), mit +0,5 Pseudo-Follow | vermeidet log(0) bei Stufen ohne Follows |

**Konventionen**

- **Leere und Nullwerte:** leer = unbekannt, 0 = echte Null.
- **Einheiten:** `completion_rate` und `skip_rate` als Anteil 0–1, `non_follower_reach_pct` in Prozent 0–100. Geld in EUR; Umrechnung zum Monatskurs, die Originalwährung steht in `affiliate_daily.currency_original`.
- **Zeiten:** immer UTC.
- **Dateiformat:** Das Skript erkennt Komma-CSV mit Dezimalpunkt ebenso wie deutsches Excel-Format (Semikolon und Dezimalkomma, `1.400,5`).
- **Snapshot-Fenster in `v_reel_kpis`:** 1 h = [0,5; 2] h, 6 h = [4; 9] h, 24 h = [18; 36] h, 7 d = [144; 216] h. Verwendet wird jeweils der Snapshot, der dem Sollzeitpunkt am nächsten liegt.

### 5.5 Tabellen im SQLite-Schema

| Tabelle / View | Zweck | Schlüssel |
|---|---|---|
| `reels` | statische Merkmale je Reel; CHECK auf alle Codebook-Felder | `reel_id` |
| `daily_snapshots` | kumulierte Kennzahlen zu beliebigen Zeitpunkten; `source` = app, api, manual oder csv_import | (`reel_id`, `snapshot_at_utc`) |
| `tests` | Hypothese, Faktor, primärer/sekundärer KPI, min. n, Status, Entscheidung | `test_id` |
| `variants` | Varianten je Test, Kontroll-Flag | `variant_id` = `test_id:label` |
| `series` | Serien mit Themengruppe (`pillar`), Playbook-Pillar (`playbook_pillar`), Format, Status und Entscheidung; Flagship-Serien aus 08 als Stammdaten | `series_id` |
| `prompts` | Tool, Modellversion, Prompt, Seed, Referenzbild, Eltern-Prompt | `prompt_id` |
| `account_daily` | Follower, Follows/Unfollows, Reach und Views nach Follower-Typ, Zielmarkt-Anteil, Link-Klicks, Account Status | `date` |
| `affiliate_daily` | Klicks, Bestellungen und Provision je Netzwerk × Sub-ID × Tag | (`date`, `network`, `sub_id`) |
| `codebook` | erlaubte Werte, z. B. für Eingabemasken | (`field`, `value`) |
| `v_reel_kpis` | pivotiert views_1h/6h/24h/7d und berechnet alle Raten | – |
| `v_week_summary` | Wochensummen und gepoolte Raten (Wochenbeginn Montag) | – |
| `v_affiliate_by_reel` | Conversion und EPC je Reel und Netzwerk | – |

### 5.6 Erfassungsroutine

| Zeitpunkt | Aufwand | Was |
|---|---|---|
| vor dem Upload | ≈ 2 min | Felder 5–35 (inkl. 5a, 6a) und `plan_id` codieren; QA-Gate: `visual_quality`, keine Wasserzeichen, `ai_label` (Badge ab Frame 0 + In-App-Label), `ad_disclosure`, Musiklizenz |
| T+1 h, T+6 h (optional) | je ≈ 30 s | Views aus der App |
| T+24 h | ≈ 1 min | `views_24h` |
| T+7 d | ≈ 3 min | alle Kennzahlen, zuerst aus der App, später per API |
| täglich (Konto) | ≈ 1 min | `account_daily`: Follower, Link-Klicks; Account Status wöchentlich |
| Montag | ≈ 30 min | Skript ausführen, Entscheidungen in `series`/`tests` eintragen, die 21 Slots der Woche planen. Im Launch-Monat sind die Slots durch [14](14_30_day_launch_plan.md) vergeben; das Review-Ritual steht in 14 §8. |

---

## 6. Analyse-Skript `scripts/winner_analysis.py`

```bash
python3 scripts/winner_analysis.py data/winner_database_template.csv          # Funktionstest (nur EXAMPLE-Zeilen)
python3 scripts/winner_analysis.py reels.csv --out report_w42.md              # Wochenreport, zusätzlich als Markdown
python3 scripts/winner_analysis.py reels.csv --week 2026-W42 --target-market-share 0.7
python3 scripts/winner_analysis.py reels.csv --to-sqlite data/winner.db       # zusätzlich in SQLite schreiben
python3 scripts/winner_analysis.py --demo 90 --demo-csv /tmp/sim.csv          # Probelauf mit simulierten Daten
```

- **Abhängigkeiten:** Pflicht ist nur numpy. `statsmodels` wird als OLS-Gegencheck (HC3) genutzt, wenn es installiert ist und n ≥ Terme + 10; der Import ist abgesichert.
- **Getestet am 25.09.2026:** Vorlage mit 3 EXAMPLE-Zeilen, Simulation mit 90 Reels, deutsches Excel-CSV mit Fehlerzeilen, SQLite-Export; alle ohne Fehler, auch mit `-W error::RuntimeWarning`. Nach dem Abgleich (Codebook v1.1) erneut ausgeführt: Vorlage mit SQLite-Export, Export in eine Datenbank im alten Schema (Spalten werden ergänzt), `--demo 90` (Simulationsdaten identisch zur Vorversion), CSV ohne die neuen Spalten (läuft, meldet fehlende Pflichtfelder).
- **EXAMPLE-Zeilen** werden automatisch ignoriert, sobald echte Zeilen vorhanden sind (`--include-examples` behält sie).
- **SQLite-Export:** Werte außerhalb des Codebooks werden als NULL gespeichert und gezählt. Zeilen mit anderen Constraint-Verletzungen werden übersprungen und gemeldet. Ein erneuter Export aktualisiert bestehende Reels per `INSERT OR REPLACE`.

**Report-Abschnitte**

1. **Wochen-KPIs** gegen Vorwoche und Launch-Bänder, inklusive North Star, qualifizierter Reichweite und Commerce-KPIs.
2. **Reels der Woche** mit account_index, Klasse, F/1k, Sends/Reach, Watch-%, VPF-Tier und vorgeschlagener Aktion.
3. **KEEP / ITERATE / SCALE / KILL** je Serie, Konzeptfamilie, Playbook-Pillar, Themengruppe, Format, Hook-Typ, visuellem Hook und Stil, mit Begründung (Regeln aus 4.3).
4. **Faktor-Lifts** für 22 Faktoren (inkl. `playbook_pillar`), u. a. Längen-, Hashtag- und Uhrzeit-Buckets, `ai_tool` und `is_trial_reel`:
   - Lift auf trendbereinigtes log(views_24h) und auf F/1k
   - 95 %-KI aus stratifiziertem Bootstrap (B = 2.000)
   - Bootstrap-p und Benjamini-Hochberg-q
   - Flags erst ab n ≥ 6
5. **Ridge-Regression** auf log(1 + views_24h):
   - One-Hot-Faktoren, Referenz ist die häufigste Stufe; seltene Stufen (n < 2) werden zu `_rare` zusammengefasst
   - Kontrollgrößen: log Länge, Hashtags, Zeittrend, log Followerstand
   - λ per Leave-one-out-CV (geschlossene Form); 90 %-Bootstrap-KI der Effekte
   - R² in-sample und LOO
6. **A/B-Tests** (`test_id` × `variant`): P(besser als Kontrolle).
7. **Thompson Sampling über hook_type × style:**
   - Erfolg = account_index ≥ 1 **und** F/1k ≥ Median
   - Beta-Prior je Zelle aus den Randverteilungen (Stärke 2)
   - Ungetestete Stufen gehen als Exploration ein: bis zu 2 Hooks und 2 Stile, geordnet nach schwachen Research-Priors (Stil: Median-topic_index; Hook: YouTube-Shorts-Proxy). Diese Priors sind nicht signifikant und dienen nur der Reihenfolge.
   - Ausgabe: P(beste Zelle), Slot-Vorschlag und Liste der nächsten Tests (SCALE-Ausbau, Hook-/Follow-Tests, Replikationen, Exploration)
8. **Eigene Perzentile** P25/P50/P75/P90 zur Rekalibrierung der Bänder ab n ≥ 42.
9. **Datenqualität:**
   - Werte außerhalb des Codebooks, Pflichtfelder, nicht lesbare Zahlen
   - Views-Reihenfolge 1 h ≤ 6 h ≤ 24 h ≤ 7 d
   - Reach größer als Views
   - mehr als 5 Hashtags
   - Abweichung des Datums vom Shortcode

---

## 7. Offene Punkte (zu verifizieren)

1. **In-App-Insights je Reel:** Welche Felder zeigt die App genau (Follows, Profilbesuche, Nicht-Follower-Anteil, Retention/Completion, Skip Rate)? Beim ersten Reel prüfen und Abschnitt 1 anpassen.
2. **Zählweise:** Zählt `views` Wiederholungen mit? Enthält `ig_reels_avg_watch_time` Replays?
3. **Skip Rate:** Ist `reels_skip_rate` („in development“) für den eigenen Account per API verfügbar?
4. **Trial Reels:** Schwelle für neue Accounts, ~1.000 Follower `[ESTIMATED]` ([q01](quellen/q01_instagram_platform_rules.md)).
5. **Shoppable/Affiliate-Reels:** Verfügbarkeit für den Standort des Accounts (Deutschland nicht in der Startliste, [q01](quellen/q01_instagram_platform_rules.md)).
6. **Engagement-Bait:** Gelten `comment_keyword`-CTAs als „engagement bait“?
7. **Recht:** [q07](quellen/q07_legal_ai_risk.md) liegt vor und ist in 3.6 und 4.7 umgesetzt. Offen bleiben laut q07 §4: ob das Meta-Label „AI info“ die Pflicht aus Art. 50 erfüllt, welches Recht für einen englischsprachigen Account aus Deutschland gilt (DE vs. UK/US), welche Aufsicht in DE zuständig ist, und die finale Fassung der Art.-50-Leitlinien. Impressumspflicht ist in q07 nicht behandelt. Vor der ersten Monetarisierung anwaltlich prüfen lassen.
9. **Abweichungen zwischen 08, 11 und 14,** die dieses Kapitel nicht auflösen kann: Wildcard-Themen in Monat 1 (08: Named Setting, Sky Homes und Real Price mit je 3 Reels; 14: Cozy Night in `T05` und der Location-Pilot `T18`) sowie Preis-Labels für fiktive Konzepte (08/11: nie; 13/14: nur als `est. … (concept)` in `T25`). Für den Test gilt 14; vor einem Ausbau der Preis-Labels nach dem Test rechtlich prüfen.
8. **Zielbänder:** Alle Bänder der Basis **S** an Tag 14 durch eigene Perzentile ersetzen. Die Bänder der Basis **B** beruhen auf Top-Reels und sind deshalb eher zu hoch angesetzt.

---

## Quellen

- [quellen/q01_instagram_platform_rules.md](quellen/q01_instagram_platform_rules.md): Ranking-Signale (Mosseri 22.01.2025), Originalität (30.04.2024 / 30.04.2026), KI-Labels, Recommendation Guidelines, Trial Reels, Hashtag-Limit, Account Status, Monetarisierungs-Policies, Shoppable Reels
- [quellen/q02_furniture_affiliate_commerce.md](quellen/q02_furniture_affiliate_commerce.md): Cookie-Fenster, EPC, AOV, Conversion-Referenzen
- [quellen/q03_sponsors_brand_deals.md](quellen/q03_sponsors_brand_deals.md): CPM- und Preis-Benchmarks (Drittangaben)
- [quellen/q07_legal_ai_risk.md](quellen/q07_legal_ai_risk.md): EU AI Act Art. 50 (seit 02.08.2026), Meta-KI-Labels, Werbe- und Affiliate-Kennzeichnung (UWG, Medienanstalten, FTC, ASA), Marken, reale Orte und Irreführung, Musiklizenzen
- [08_content_pillars.md](08_content_pillars.md), [11_brand_style_guide.md](11_brand_style_guide.md): Pillars P1–P6, Serien, Konzeptfamilien, Formate, Badges
- [13_testing_matrix.csv](13_testing_matrix.csv), [14_30_day_launch_plan.md](14_30_day_launch_plan.md): verbindliches Testdesign und Tagesplan für Monat 1
- [data/processed/analysis_digest.md](data/processed/analysis_digest.md) und [04_reel_database.csv](04_reel_database.csv): Research-Datensatz (Kruskal-Wallis-Tests, VPF- und Engagement-Quantile, YouTube-Shorts-Proxy). Die Quantile für Likes/View und Kommentare/View nach Accountgröße und die Streuung innerhalb der Accounts wurden am 25.09.2026 für dieses Kapitel aus `04_reel_database.csv` berechnet.
- Meta for Developers: [Instagram Media Insights](https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights) und [Instagram User Insights](https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights), beide am 25.09.2026 per WebFetch abgerufen (die Seiten liegen als Zusammenfassung des Abruf-Tools vor, nicht als Volltext)
- Codebooks: [scripts/cover_codebook.md](scripts/cover_codebook.md), [scripts/reel_codebook_prompt.txt](scripts/reel_codebook_prompt.txt), [scripts/topic_groups.py](scripts/topic_groups.py)
