-- Winner-Datenbank (Teil 31) - SQLite-Schema, Codebook v1.1
-- Erzeugt aus ALLOWED in scripts/winner_analysis.py (CHECK-Listen = gleiche Werte wie das Skript
-- und wie scripts/cover_codebook.md / scripts/reel_codebook_prompt.txt, Vereinigungsmenge).
-- Beschreibung aller Felder: 15_kpi_framework.md, Abschnitt 5.
--
-- Anlegen:   sqlite3 data/winner.db < data/winner_database_schema.sql
-- Befuellen: python3 scripts/winner_analysis.py <reels.csv> --to-sqlite data/winner.db
--
-- Konventionen: Zeiten in UTC als ISO-8601-Text ('2026-10-01T13:05:00Z'); Anteile 0-1 (ausser
-- non_follower_reach_pct 0-100); Geld in EUR; NULL = unbekannt, 0 = echte Null.
-- Neue Codebook-Werte: ALLOWED im Skript erweitern, dieses Schema neu erzeugen, Tabelle migrieren.
-- v1.1 (Abgleich mit 08_content_pillars.md / 11_brand_style_guide.md): neue Spalten playbook_pillar
-- (P1-P6, CHECK) und series_family (Konzeptfamilie, Freitext) in reels; playbook_pillar in series;
-- Flagship-Serien aus 08 Abschnitt 7 als Stammdaten. 'pillar' bleibt die Research-Themengruppe.
-- Bestehende v1-Datenbanken ergaenzt das Skript beim Export automatisch (ALTER TABLE ... ADD COLUMN).

PRAGMA foreign_keys = ON;

-- ------------------------------------------------------------------------------------------
-- Stammdaten
-- ------------------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS codebook (
    field       TEXT NOT NULL,
    value       TEXT NOT NULL,
    description TEXT,
    PRIMARY KEY (field, value)
);

CREATE TABLE IF NOT EXISTS prompts (
    prompt_id        TEXT PRIMARY KEY,               -- z. B. P0001
    ai_tool          TEXT,                            -- Bild-/Video-Tool, lowercase
    model_version    TEXT,
    prompt_text      TEXT,
    negative_prompt  TEXT,
    seed             TEXT,
    reference_image  TEXT,                            -- Pfad/URL eines Referenzbildes (eigene Rechte!)
    parent_prompt_id TEXT REFERENCES prompts(prompt_id),
    created_at       TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    notes            TEXT
);

CREATE TABLE IF NOT EXISTS series (
    series_id   TEXT PRIMARY KEY,                     -- z. B. S01_unbuilt (Konvention: 08, Abschnitt 7)
    name        TEXT,                                 -- Serien-Badge, z. B. 'UNBUILT No. ###'
    pillar      TEXT CHECK (pillar IN (
        'luxury_room', 'luxury_home', 'future_arch', 'unusual_home', 'fantasy_dream',
        'cozy_ambience', 'location', 'hotel_resort', 'pool', 'architecture', 'style',
        'decor_commerce', 'other')),                  -- Research-Themengruppe (optional)
    playbook_pillar TEXT CHECK (playbook_pillar IN (
        'p1_impossible_homes', 'p2_pick_one', 'p3_dream_builds', 'p4_night_stories', 'p5_wildcards',
        'p6_statement_rooms')),                  -- Playbook-Pillar P1-P6 (08)
    format      TEXT CHECK (format IN (
        'single_scene_ambience', 'multi_scene_montage', 'house_tour', 'transformation_morph',
        'before_after', 'choice_compare', 'pov_story', 'process_tutorial', 'slideshow_stills',
        'real_estate_tour', 'talking_head', 'other')),
    start_date  TEXT,
    status      TEXT DEFAULT 'active' CHECK (status IN ('active', 'paused', 'killed', 'scaled')),
    decision    TEXT CHECK (decision IN ('KEEP', 'ITERATE', 'SCALE', 'KILL', 'OFFEN')),
    notes       TEXT
);

-- ------------------------------------------------------------------------------------------
-- Tests und Varianten
-- ------------------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tests (
    test_id            TEXT PRIMARY KEY,              -- IDs aus 13_testing_matrix.csv (T01_format ... T27_style_explore); neue ab T28
    name               TEXT,
    hypothesis         TEXT,                          -- "curiosity-Hooks bringen >=1.5x views_24h ggue. question"
    factor             TEXT,                          -- getesteter Faktor (Spaltenname in reels), genau EINER
    primary_kpi        TEXT DEFAULT 'log_views_24h',
    secondary_kpi      TEXT DEFAULT 'follows_per_1k_views',
    min_n_per_variant  INTEGER DEFAULT 6 CHECK (min_n_per_variant >= 1),
    start_date         TEXT,
    end_date           TEXT,
    status             TEXT DEFAULT 'planned' CHECK (status IN ('planned', 'running', 'done', 'stopped')),
    decision           TEXT CHECK (decision IN ('KEEP', 'ITERATE', 'SCALE', 'KILL', 'OFFEN')),
    decision_date      TEXT,
    result_summary     TEXT
);

CREATE TABLE IF NOT EXISTS variants (
    variant_id   TEXT PRIMARY KEY,                    -- test_id || ':' || label
    test_id      TEXT NOT NULL REFERENCES tests(test_id),
    label        TEXT NOT NULL,                       -- A, B, C oder Level-Name
    level        TEXT,                                -- Wert des getesteten Faktors
    is_control   INTEGER DEFAULT 0 CHECK (is_control IN (0, 1)),
    description  TEXT,
    UNIQUE (test_id, label)
);

-- ------------------------------------------------------------------------------------------
-- Reels: ein Datensatz pro veroeffentlichtem Reel (statische Merkmale)
-- ------------------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS reels (
    reel_id            TEXT PRIMARY KEY,              -- Instagram-Shortcode (aus der URL /reel/<code>/)
    permalink          TEXT,
    posted_at_utc      TEXT NOT NULL,                 -- Kontrolle: scripts/shortcode_time.py <code>
    followers_at_post  INTEGER CHECK (followers_at_post >= 0),
    series_id          TEXT REFERENCES series(series_id),
    test_id            TEXT REFERENCES tests(test_id),
    variant_id         TEXT REFERENCES variants(variant_id),
    is_trial_reel      INTEGER CHECK (is_trial_reel IN (0, 1)),
    prompt_id          TEXT REFERENCES prompts(prompt_id),
    pillar             TEXT CHECK (pillar IN (
        'luxury_room', 'luxury_home', 'future_arch', 'unusual_home', 'fantasy_dream',
        'cozy_ambience', 'location', 'hotel_resort', 'pool', 'architecture', 'style',
        'decor_commerce', 'other')),                  -- Research-Themengruppe (Vergleich mit dem Research)
    playbook_pillar    TEXT CHECK (playbook_pillar IN (
        'p1_impossible_homes', 'p2_pick_one', 'p3_dream_builds', 'p4_night_stories', 'p5_wildcards',
        'p6_statement_rooms')),                  -- Playbook-Pillar P1-P6 (08)
    series_family      TEXT,                          -- Konzeptfamilie, z. B. under_things, bare_ledge (15, Feld 6a)
    format             TEXT CHECK (format IN (
        'single_scene_ambience', 'multi_scene_montage', 'house_tour', 'transformation_morph',
        'before_after', 'choice_compare', 'pov_story', 'process_tutorial', 'slideshow_stills',
        'real_estate_tour', 'talking_head', 'other')),
    hook_type          TEXT CHECK (hook_type IN (
        'curiosity', 'pov', 'aspirational', 'choice', 'question', 'status', 'money', 'location',
        'fantasy', 'contrarian', 'instructional', 'none')),
    hook_text          TEXT,
    visual_hook        TEXT CHECK (visual_hook IN (
        'text_hook', 'exterior_reveal', 'view_reveal', 'pool', 'bedroom', 'person_present',
        'door_opening', 'unusual_architecture', 'empty_to_full', 'before_after',
        'motion_immediate', 'sound_hook', 'none')),
    room               TEXT CHECK (room IN (
        'bedroom', 'living_room', 'kitchen', 'bathroom', 'dining', 'closet', 'home_theater',
        'office', 'pool', 'terrace_outdoor', 'garden_landscape', 'exterior_facade',
        'multi_room_tour', 'hotel_room', 'lobby_common', 'spa', 'stairs_hall', 'other')),
    building_type      TEXT CHECK (building_type IN (
        'villa', 'penthouse', 'apartment', 'mansion', 'cabin_chalet', 'treehouse', 'hotel_resort',
        'house', 'castle_palace', 'unusual_structure', 'none_visible')),
    style              TEXT CHECK (style IN (
        'modern_luxury', 'minimalist', 'japandi', 'tropical', 'mediterranean', 'brutalist',
        'futuristic', 'organic_modern', 'biophilic', 'scandinavian', 'dark_luxury', 'warm_luxury',
        'industrial', 'cyberpunk', 'classical_luxury', 'neoclassical', 'art_deco', 'rustic_cozy',
        'mid_century', 'maximalist', 'glam_feminine', 'traditional_regional', 'other')),
    landscape          TEXT CHECK (landscape IN (
        'ocean_beach', 'mountain', 'forest', 'desert', 'jungle_tropical', 'lake_river', 'snow',
        'city_skyline', 'cliff', 'underwater', 'space_sky', 'rain_window', 'none')),
    lighting           TEXT CHECK (lighting IN (
        'daylight', 'golden_hour', 'blue_hour', 'night_artificial', 'overcast_rain', 'candle_fire',
        'mixed')),
    location           TEXT,                          -- benannter Ort, 'none' oder 'fictional'
    realism            TEXT CHECK (realism IN (
        'fantasy_impossible', 'stylized_dreamy', 'aspirational_realistic', 'real_existing')),
    visual_quality     TEXT CHECK (visual_quality IN (
        'high', 'medium', 'low')),              -- Selbst-Check vor Upload (QA-Gate)
    camera             TEXT CHECK (camera IN (
        'static', 'slow_push_in', 'pull_back', 'pan', 'tilt', 'orbit', 'drone_aerial',
        'fly_through', 'pov_walk', 'morph_transform', 'zoom', 'handheld', 'mixed')),
    length_sec         REAL CHECK (length_sec > 0 AND length_sec <= 180),
    n_scenes           INTEGER CHECK (n_scenes >= 1),
    audio_type         TEXT CHECK (audio_type IN (
        'music_only', 'music_plus_ambient', 'ambient_nature_only', 'voiceover', 'asmr_sfx',
        'silence')),
    audio_name         TEXT,
    text_overlay       TEXT CHECK (text_overlay IN (
        'none', 'hook_only', 'hook_plus_labels', 'continuous_text')),
    caption_type       TEXT CHECK (caption_type IN (
        'curiosity', 'pov', 'aspirational', 'choice', 'question', 'status', 'money', 'location',
        'fantasy', 'contrarian', 'instructional', 'descriptive', 'promotional', 'none')),
    caption_first_line TEXT,
    cta_type           TEXT CHECK (cta_type IN (
        'comment_keyword', 'question_engagement', 'follow', 'save_share', 'link_in_bio', 'dm',
        'shop_product', 'tag_friend', 'none')),
    hashtags_n         INTEGER CHECK (hashtags_n BETWEEN 0 AND 30),  -- Plattformlimit 5 (q01), Skript warnt
    ai_tool            TEXT,
    ai_label           INTEGER CHECK (ai_label IN (0, 1)),           -- KI-Label beim Upload gesetzt
    ad_disclosure      TEXT CHECK (ad_disclosure IN (
        'none', 'affiliate', 'paid_partnership', 'own_product')),
    notes              TEXT,                                          -- 'POLICY: ...' erzwingt KILL im Skript
    created_at         TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);
CREATE INDEX IF NOT EXISTS ix_reels_posted ON reels(posted_at_utc);
CREATE INDEX IF NOT EXISTS ix_reels_series ON reels(series_id);
CREATE INDEX IF NOT EXISTS ix_reels_test ON reels(test_id, variant_id);

-- ------------------------------------------------------------------------------------------
-- Kennzahlen-Snapshots je Reel (T+1h, T+6h, T+24h, T+7d, optional taeglich). Kumulierte Werte.
-- ------------------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS daily_snapshots (
    reel_id                TEXT NOT NULL REFERENCES reels(reel_id) ON DELETE CASCADE,
    snapshot_at_utc        TEXT NOT NULL,
    hours_since_post       REAL NOT NULL CHECK (hours_since_post >= 0),
    source                 TEXT NOT NULL CHECK (source IN ('app', 'api', 'manual', 'csv_import')),
    views                  INTEGER CHECK (views >= 0),
    reach                  INTEGER CHECK (reach >= 0),
    non_follower_reach_pct REAL CHECK (non_follower_reach_pct BETWEEN 0 AND 100),
    likes                  INTEGER CHECK (likes >= 0),
    comments               INTEGER CHECK (comments >= 0),
    shares                 INTEGER CHECK (shares >= 0),
    saves                  INTEGER CHECK (saves >= 0),
    reposts                INTEGER CHECK (reposts >= 0),
    followers_gained       INTEGER CHECK (followers_gained >= 0),
    profile_visits         INTEGER CHECK (profile_visits >= 0),
    avg_watch_time         REAL CHECK (avg_watch_time >= 0),
    completion_rate        REAL CHECK (completion_rate BETWEEN 0 AND 1),
    skip_rate              REAL CHECK (skip_rate BETWEEN 0 AND 1),
    link_clicks            INTEGER CHECK (link_clicks >= 0),
    revenue                REAL CHECK (revenue >= 0),
    PRIMARY KEY (reel_id, snapshot_at_utc)
);
CREATE INDEX IF NOT EXISTS ix_snap_hours ON daily_snapshots(reel_id, hours_since_post);

-- ------------------------------------------------------------------------------------------
-- Konto-Ebene (North Star, Follows ohne Reel-Zuordnung, Account Status) und Affiliate-Umsatz
-- ------------------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS account_daily (
    date                   TEXT PRIMARY KEY,          -- YYYY-MM-DD (UTC)
    followers              INTEGER,
    follows                INTEGER,                   -- API follows_and_unfollows (ab 100 Followern)
    unfollows              INTEGER,
    reach                  INTEGER,
    reach_non_follower     INTEGER,                   -- API reach, breakdown follow_type
    views                  INTEGER,
    views_non_follower     INTEGER,
    target_market_share    REAL CHECK (target_market_share BETWEEN 0 AND 1),  -- aus Zielgruppen-Insights
    bio_link_clicks        INTEGER,                   -- eigener Redirect/Link-Tool, NICHT profile_links_taps
    story_link_clicks      INTEGER,
    account_status         TEXT CHECK (account_status IN ('ok', 'restricted', 'unknown')),
    notes                  TEXT
);

CREATE TABLE IF NOT EXISTS affiliate_daily (
    date      TEXT NOT NULL,
    network   TEXT NOT NULL,                          -- amazon, ltk, awin, rakuten, ...
    sub_id    TEXT NOT NULL,                          -- Konvention: reel_id oder series_id
    reel_id   TEXT REFERENCES reels(reel_id),
    clicks    INTEGER CHECK (clicks >= 0),
    orders    INTEGER CHECK (orders >= 0),
    revenue   REAL CHECK (revenue >= 0),              -- Provision in EUR
    currency_original TEXT,
    PRIMARY KEY (date, network, sub_id)
);

-- ------------------------------------------------------------------------------------------
-- Views
-- ------------------------------------------------------------------------------------------
-- Snapshot je Zielzeitpunkt = naechster Snapshot im Fenster: 1h [0.5,2], 6h [4,9], 24h [18,36], 7d [144,216]
CREATE VIEW IF NOT EXISTS v_reel_kpis AS
SELECT r.*,
       s1.views  AS views_1h,
       s6.views  AS views_6h,
       s24.views AS views_24h,
       s7.views  AS views_7d,
       s7.reach, s7.non_follower_reach_pct, s7.likes, s7.comments, s7.shares, s7.saves, s7.reposts,
       s7.followers_gained, s7.profile_visits, s7.avg_watch_time, s7.completion_rate, s7.skip_rate,
       s7.link_clicks, s7.revenue,
       1.0    * s7.likes            / NULLIF(s7.views, 0)          AS likes_per_view,
       1.0    * s7.comments         / NULLIF(s7.views, 0)          AS comments_per_view,
       1.0    * s7.likes            / NULLIF(s7.reach, 0)          AS likes_per_reach,
       1.0    * s7.shares           / NULLIF(s7.reach, 0)          AS sends_per_reach,
       1.0    * s7.saves            / NULLIF(s7.reach, 0)          AS saves_per_reach,
       1000.0 * s7.followers_gained / NULLIF(s7.views, 0)          AS follows_per_1k_views,
       1.0    * s7.profile_visits   / NULLIF(s7.views, 0)          AS profile_visits_per_view,
       1.0    * s7.followers_gained / NULLIF(s7.profile_visits, 0) AS follow_conversion,
       1.0    * s7.avg_watch_time   / NULLIF(r.length_sec, 0)      AS avg_pct_watched,
       CASE WHEN r.followers_at_post >= 1000                    -- VPF erst ab 1.000 Followern sinnvoll
            THEN 1.0 * s7.views / r.followers_at_post END         AS vpf_7d,
       1.0    * s1.views            / NULLIF(s24.views, 0)         AS share_1h_of_24h,
       1.0 - 1.0 * s24.views        / NULLIF(s7.views, 0)          AS longtail_share,
       1000.0 * s7.link_clicks      / NULLIF(s7.reach, 0)          AS clicks_per_1k_reach,
       1000.0 * s7.revenue          / NULLIF(s7.views, 0)          AS rpm_eur,
       1.0    * s7.revenue          / NULLIF(s7.link_clicks, 0)    AS epc_eur
FROM reels r
LEFT JOIN daily_snapshots s1 ON s1.rowid = (
    SELECT x.rowid FROM daily_snapshots x WHERE x.reel_id = r.reel_id AND x.hours_since_post BETWEEN 0.5 AND 2
    ORDER BY abs(x.hours_since_post - 1) LIMIT 1)
LEFT JOIN daily_snapshots s6 ON s6.rowid = (
    SELECT x.rowid FROM daily_snapshots x WHERE x.reel_id = r.reel_id AND x.hours_since_post BETWEEN 4 AND 9
    ORDER BY abs(x.hours_since_post - 6) LIMIT 1)
LEFT JOIN daily_snapshots s24 ON s24.rowid = (
    SELECT x.rowid FROM daily_snapshots x WHERE x.reel_id = r.reel_id AND x.hours_since_post BETWEEN 18 AND 36
    ORDER BY abs(x.hours_since_post - 24) LIMIT 1)
LEFT JOIN daily_snapshots s7 ON s7.rowid = (
    SELECT x.rowid FROM daily_snapshots x WHERE x.reel_id = r.reel_id AND x.hours_since_post BETWEEN 144 AND 216
    ORDER BY abs(x.hours_since_post - 168) LIMIT 1);

-- Wochenuebersicht; week_start = Montag der ISO-Woche (UTC)
CREATE VIEW IF NOT EXISTS v_week_summary AS
SELECT date(posted_at_utc, 'weekday 0', '-6 days')                     AS week_start,
       COUNT(*)                                                        AS reels,
       SUM(views_7d)                                                   AS views_7d,
       SUM(reach)                                                      AS reach,
       SUM(followers_gained)                                           AS follows,
       1000.0 * SUM(followers_gained) / NULLIF(SUM(views_7d), 0)       AS follows_per_1k_views,
       1.0 * SUM(shares) / NULLIF(SUM(reach), 0)                       AS sends_per_reach,
       1.0 * SUM(saves)  / NULLIF(SUM(reach), 0)                       AS saves_per_reach,
       1.0 * SUM(likes)  / NULLIF(SUM(views_7d), 0)                    AS likes_per_view,
       SUM(link_clicks)                                                AS link_clicks,
       SUM(revenue)                                                    AS revenue_eur
FROM v_reel_kpis
GROUP BY week_start;

CREATE VIEW IF NOT EXISTS v_affiliate_by_reel AS
SELECT reel_id, network,
       SUM(clicks) AS clicks, SUM(orders) AS orders, SUM(revenue) AS revenue_eur,
       1.0 * SUM(orders)  / NULLIF(SUM(clicks), 0) AS conversion_rate,
       1.0 * SUM(revenue) / NULLIF(SUM(clicks), 0) AS epc_eur
FROM affiliate_daily
GROUP BY reel_id, network;

-- ------------------------------------------------------------------------------------------
-- Codebook-Werte (Referenz fuer Eingabemasken)
-- ------------------------------------------------------------------------------------------
INSERT OR IGNORE INTO codebook(field, value) VALUES
    ('pillar', 'luxury_room'),
    ('pillar', 'luxury_home'),
    ('pillar', 'future_arch'),
    ('pillar', 'unusual_home'),
    ('pillar', 'fantasy_dream'),
    ('pillar', 'cozy_ambience'),
    ('pillar', 'location'),
    ('pillar', 'hotel_resort'),
    ('pillar', 'pool'),
    ('pillar', 'architecture'),
    ('pillar', 'style'),
    ('pillar', 'decor_commerce'),
    ('pillar', 'other'),
    ('playbook_pillar', 'p1_impossible_homes'),
    ('playbook_pillar', 'p2_pick_one'),
    ('playbook_pillar', 'p3_dream_builds'),
    ('playbook_pillar', 'p4_night_stories'),
    ('playbook_pillar', 'p5_wildcards'),
    ('playbook_pillar', 'p6_statement_rooms'),
    ('format', 'single_scene_ambience'),
    ('format', 'multi_scene_montage'),
    ('format', 'house_tour'),
    ('format', 'transformation_morph'),
    ('format', 'before_after'),
    ('format', 'choice_compare'),
    ('format', 'pov_story'),
    ('format', 'process_tutorial'),
    ('format', 'slideshow_stills'),
    ('format', 'real_estate_tour'),
    ('format', 'talking_head'),
    ('format', 'other'),
    ('hook_type', 'curiosity'),
    ('hook_type', 'pov'),
    ('hook_type', 'aspirational'),
    ('hook_type', 'choice'),
    ('hook_type', 'question'),
    ('hook_type', 'status'),
    ('hook_type', 'money'),
    ('hook_type', 'location'),
    ('hook_type', 'fantasy'),
    ('hook_type', 'contrarian'),
    ('hook_type', 'instructional'),
    ('hook_type', 'none'),
    ('visual_hook', 'text_hook'),
    ('visual_hook', 'exterior_reveal'),
    ('visual_hook', 'view_reveal'),
    ('visual_hook', 'pool'),
    ('visual_hook', 'bedroom'),
    ('visual_hook', 'person_present'),
    ('visual_hook', 'door_opening'),
    ('visual_hook', 'unusual_architecture'),
    ('visual_hook', 'empty_to_full'),
    ('visual_hook', 'before_after'),
    ('visual_hook', 'motion_immediate'),
    ('visual_hook', 'sound_hook'),
    ('visual_hook', 'none'),
    ('room', 'bedroom'),
    ('room', 'living_room'),
    ('room', 'kitchen'),
    ('room', 'bathroom'),
    ('room', 'dining'),
    ('room', 'closet'),
    ('room', 'home_theater'),
    ('room', 'office'),
    ('room', 'pool'),
    ('room', 'terrace_outdoor'),
    ('room', 'garden_landscape'),
    ('room', 'exterior_facade'),
    ('room', 'multi_room_tour'),
    ('room', 'hotel_room'),
    ('room', 'lobby_common'),
    ('room', 'spa'),
    ('room', 'stairs_hall'),
    ('room', 'other'),
    ('building_type', 'villa'),
    ('building_type', 'penthouse'),
    ('building_type', 'apartment'),
    ('building_type', 'mansion'),
    ('building_type', 'cabin_chalet'),
    ('building_type', 'treehouse'),
    ('building_type', 'hotel_resort'),
    ('building_type', 'house'),
    ('building_type', 'castle_palace'),
    ('building_type', 'unusual_structure'),
    ('building_type', 'none_visible'),
    ('style', 'modern_luxury'),
    ('style', 'minimalist'),
    ('style', 'japandi'),
    ('style', 'tropical'),
    ('style', 'mediterranean'),
    ('style', 'brutalist'),
    ('style', 'futuristic'),
    ('style', 'organic_modern'),
    ('style', 'biophilic'),
    ('style', 'scandinavian'),
    ('style', 'dark_luxury'),
    ('style', 'warm_luxury'),
    ('style', 'industrial'),
    ('style', 'cyberpunk'),
    ('style', 'classical_luxury'),
    ('style', 'neoclassical'),
    ('style', 'art_deco'),
    ('style', 'rustic_cozy'),
    ('style', 'mid_century'),
    ('style', 'maximalist'),
    ('style', 'glam_feminine'),
    ('style', 'traditional_regional'),
    ('style', 'other'),
    ('landscape', 'ocean_beach'),
    ('landscape', 'mountain'),
    ('landscape', 'forest'),
    ('landscape', 'desert'),
    ('landscape', 'jungle_tropical'),
    ('landscape', 'lake_river'),
    ('landscape', 'snow'),
    ('landscape', 'city_skyline'),
    ('landscape', 'cliff'),
    ('landscape', 'underwater'),
    ('landscape', 'space_sky'),
    ('landscape', 'rain_window'),
    ('landscape', 'none'),
    ('lighting', 'daylight'),
    ('lighting', 'golden_hour'),
    ('lighting', 'blue_hour'),
    ('lighting', 'night_artificial'),
    ('lighting', 'overcast_rain'),
    ('lighting', 'candle_fire'),
    ('lighting', 'mixed'),
    ('realism', 'fantasy_impossible'),
    ('realism', 'stylized_dreamy'),
    ('realism', 'aspirational_realistic'),
    ('realism', 'real_existing'),
    ('visual_quality', 'high'),
    ('visual_quality', 'medium'),
    ('visual_quality', 'low'),
    ('camera', 'static'),
    ('camera', 'slow_push_in'),
    ('camera', 'pull_back'),
    ('camera', 'pan'),
    ('camera', 'tilt'),
    ('camera', 'orbit'),
    ('camera', 'drone_aerial'),
    ('camera', 'fly_through'),
    ('camera', 'pov_walk'),
    ('camera', 'morph_transform'),
    ('camera', 'zoom'),
    ('camera', 'handheld'),
    ('camera', 'mixed'),
    ('audio_type', 'music_only'),
    ('audio_type', 'music_plus_ambient'),
    ('audio_type', 'ambient_nature_only'),
    ('audio_type', 'voiceover'),
    ('audio_type', 'asmr_sfx'),
    ('audio_type', 'silence'),
    ('text_overlay', 'none'),
    ('text_overlay', 'hook_only'),
    ('text_overlay', 'hook_plus_labels'),
    ('text_overlay', 'continuous_text'),
    ('caption_type', 'curiosity'),
    ('caption_type', 'pov'),
    ('caption_type', 'aspirational'),
    ('caption_type', 'choice'),
    ('caption_type', 'question'),
    ('caption_type', 'status'),
    ('caption_type', 'money'),
    ('caption_type', 'location'),
    ('caption_type', 'fantasy'),
    ('caption_type', 'contrarian'),
    ('caption_type', 'instructional'),
    ('caption_type', 'descriptive'),
    ('caption_type', 'promotional'),
    ('caption_type', 'none'),
    ('cta_type', 'comment_keyword'),
    ('cta_type', 'question_engagement'),
    ('cta_type', 'follow'),
    ('cta_type', 'save_share'),
    ('cta_type', 'link_in_bio'),
    ('cta_type', 'dm'),
    ('cta_type', 'shop_product'),
    ('cta_type', 'tag_friend'),
    ('cta_type', 'none'),
    ('ad_disclosure', 'none'),
    ('ad_disclosure', 'affiliate'),
    ('ad_disclosure', 'paid_partnership'),
    ('ad_disclosure', 'own_product');

UPDATE codebook SET description = 'P1 Impossible Homes, Serie UNBUILT No. ###' WHERE field = 'playbook_pillar' AND value = 'p1_impossible_homes';
UPDATE codebook SET description = 'P2 Pick One, Serie PICK ONE No. ###' WHERE field = 'playbook_pillar' AND value = 'p2_pick_one';
UPDATE codebook SET description = 'P3 Dream Builds, Serie FROM NOTHING No. ###' WHERE field = 'playbook_pillar' AND value = 'p3_dream_builds';
UPDATE codebook SET description = 'P4 Night Stories, Serie AFTER DARK No. ###' WHERE field = 'playbook_pillar' AND value = 'p4_night_stories';
UPDATE codebook SET description = 'P5 Wildcards, Serien S05_wild_<thema>' WHERE field = 'playbook_pillar' AND value = 'p5_wildcards';
UPDATE codebook SET description = 'P6 Statement Rooms (Reserve), Serie THE ROOM No. ###' WHERE field = 'playbook_pillar' AND value = 'p6_statement_rooms';

-- ------------------------------------------------------------------------------------------
-- Stammdaten: Flagship-Serien (08_content_pillars.md, Abschnitt 7; Badges laut 11, Abschnitt 16).
-- Format = Standardformat der Pillar (08, Abschnitt 7). P5 bekommt je Thema eine eigene Serie
-- S05_wild_<thema> (z. B. S05_wild_named_setting), sie wird beim ersten Reel angelegt.
-- ------------------------------------------------------------------------------------------
INSERT OR IGNORE INTO series(series_id, name, playbook_pillar, format, status) VALUES
    ('S01_unbuilt',      'UNBUILT No. ###',      'p1_impossible_homes', 'single_scene_ambience', 'active'),
    ('S02_pick_one',     'PICK ONE No. ###',     'p2_pick_one',         'choice_compare',        'active'),
    ('S03_from_nothing', 'FROM NOTHING No. ###', 'p3_dream_builds',     'transformation_morph',  'active'),
    ('S04_after_dark',   'AFTER DARK No. ###',   'p4_night_stories',    'single_scene_ambience', 'active'),
    ('S06_the_room',     'THE ROOM No. ###',     'p6_statement_rooms',  'single_scene_ambience', 'paused');
