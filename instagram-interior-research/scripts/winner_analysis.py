#!/usr/bin/env python3
"""Weekly winner analysis for the OWN Instagram account (Part 31 of the playbook).

Reads a CSV in the format of data/winner_database_template.csv (one row per reel; engagement
metrics = 7-day snapshot; views_1h/6h/24h/7d = snapshots at those ages) and prints a weekly
report in German:

  1. Week KPIs vs. launch bands (hypotheses from 15_kpi_framework.md, section 3)
  2. Reel table of the week with class (Hit/Solide/Schwach/Flop) and action
  3. KEEP / ITERATE / SCALE / KILL per series, pillar, format, hook type, visual hook, style
     (rules = constants below = 15_kpi_framework.md, section 4)
  4. Per-factor lift on log(views_24h) - by default trend-adjusted, i.e. log(views_24h) minus
     log(rolling median of the previous 15 reels) = log(account_index); --raw-lift = unadjusted -
     and on follows per 1,000 views, with stratified bootstrap CIs, bootstrap p-values and
     Benjamini-Hochberg q-values; flags only with minimum n
  5. Ridge regression (numpy; LOO-CV for lambda; bootstrap CIs). statsmodels OLS (HC3) as an
     optional cross-check if statsmodels is installed and n is large enough
  6. Running A/B tests (test_id x variant)
  7. Thompson sampling over hook_type x style -> slot proposal for next week + next tests
  8. Own percentiles for recalibrating the bands after 14 days, data-quality checks

Only numpy is required. Examples:
  python3 scripts/winner_analysis.py data/winner_database_template.csv
  python3 scripts/winner_analysis.py my_reels.csv --week 2026-W42 --out report_w42.md
  python3 scripts/winner_analysis.py my_reels.csv --to-sqlite data/winner.db
  python3 scripts/winner_analysis.py --demo 90 --demo-csv /tmp/sim.csv   # simulated dry run

Rows whose reel_id starts with EXAMPLE (or whose notes contain EXAMPLE) are fake template rows.
They are dropped automatically as soon as real rows exist (use --include-examples to keep them).
A note containing "POLICY" (e.g. "POLICY: Account Status restriction") forces KILL for every
series/format/hook/style group that reel belongs to.
"""
import argparse
import csv
import datetime as dt
import math
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict

try:
    import numpy as np
except ImportError:  # pragma: no cover
    sys.exit("numpy is required: pip install numpy")

try:  # optional cross-check only
    import statsmodels.api as sm  # type: ignore
    HAVE_SM = True
except Exception:  # noqa: BLE001
    HAVE_SM = False

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCHEMA_PATH = os.path.join(ROOT, "data", "winner_database_schema.sql")
sys.path.insert(0, HERE)
try:
    from shortcode_time import shortcode_to_datetime  # decodes publish time from an IG shortcode
except Exception:  # noqa: BLE001
    shortcode_to_datetime = None

NAN = float("nan")

# ----------------------------------------------------------------------------------------------
# Decision thresholds - keep in sync with 15_kpi_framework.md, section 4
# ----------------------------------------------------------------------------------------------
MIN_N = 6              # reels per group before KEEP / SCALE / KILL
MIN_N_ITERATE = 3      # reels per group before an ITERATE diagnosis
ROLL_WINDOW = 15       # account_index = views_24h / median(views_24h of previous 15 reels)
ROLL_MIN = 3           # fewer previous reels -> median of all reels in file
SCALE_MEDIAN_AI = 1.5  # SCALE: median account_index >= 1.5 ...
KILL_MEDIAN_AI = 0.6   # KILL: median account_index < 0.6 ...
                       # ... and P(lift<0) >= P_DECIDE
KILL_NS_INDEX = 0.6    # ... and north-star index (median AI x F/1k ratio) < 0.6 (low reach but strong follows != KILL)
P_DECIDE = 0.95        # bootstrap P(direction) needed for SCALE / KILL (one-sided 95 %)
P_DIRECTION = 0.90     # bootstrap P(direction) for a "Tendenz" flag -> replication test, no decision
CI_LEVEL = 0.95        # "belegt" = 95% CI excludes 0 AND BH q < FDR_Q
FDR_Q = 0.10
F1K_SCALE_MIN = 1.0    # SCALE needs group F/1k >= 1.0 x account F/1k
F1K_ITER_MAX = 0.7     # ITERATE "reach without follows": median AI >= 1.2 and F/1k < 0.7 x account
REACH_NO_FOLLOW_AI = 1.2
PACKAGING_AI_MAX = 0.8     # ITERATE "packaging": median AI < 0.8 ...
PACKAGING_RATIO = 1.2      # ... but sends/reach or watch% >= 1.2 x account median
SLOTS_PER_WEEK = 21        # 3 reels/day
SLOTS_CHAMPION, SLOTS_TS, SLOTS_EXPLORE = 7, 10, 4
RECALIBRATE_MIN_N = 42     # 14 days x 3 reels
REEL_CLASSES = [(2.0, "Hit"), (0.8, "Solide"), (0.5, "Schwach"), (0.0, "Flop")]
VPF_TIERS = [(20, "EXTREME_OUTLIER"), (5, "VIRAL"), (2, "VERY_GOOD"), (0.5, "GOOD"), (0, "NORMAL")]

# Launch-month bands (HYPOTHESES, recalibrate after 14 days): (weak<a, ok<b, good<c, strong>=c)
# higher_is_better=False inverts the scale (skip rate).
LAUNCH_BANDS = {
    "views_24h_median": ((200, 1000, 5000), True),
    "non_follower_share": ((0.60, 0.80, 0.90), True),
    "watch_pct": ((0.35, 0.60, 0.90), True),
    "skip_rate": ((0.50, 0.35, 0.25), False),
    "completion_rate": ((0.15, 0.30, 0.45), True),
    "likes_per_view": ((0.010, 0.025, 0.037), True),
    "comments_per_view": ((0.0002, 0.0004, 0.001), True),
    "sends_per_reach": ((0.003, 0.010, 0.020), True),
    "saves_per_reach": ((0.003, 0.010, 0.020), True),
    "follows_per_1k": ((0.5, 2.0, 5.0), True),
    "profile_visits_per_view": ((0.003, 0.010, 0.020), True),
    "follow_conversion": ((0.10, 0.25, 0.40), True),
}
BAND_LABELS = ["schwach", "ok", "gut", "stark"]

# ----------------------------------------------------------------------------------------------
# Codebook v1 - aligned with scripts/cover_codebook.md and scripts/reel_codebook_prompt.txt
# (union of both where they differ). data/winner_database_schema.sql uses the same lists.
# ----------------------------------------------------------------------------------------------
ALLOWED = {
    "pillar": ["luxury_room", "luxury_home", "future_arch", "unusual_home", "fantasy_dream", "cozy_ambience",
               "location", "hotel_resort", "pool", "architecture", "style", "decor_commerce", "other"],
    "format": ["single_scene_ambience", "multi_scene_montage", "house_tour", "transformation_morph", "before_after",
               "choice_compare", "pov_story", "process_tutorial", "slideshow_stills", "real_estate_tour",
               "talking_head", "other"],
    "hook_type": ["curiosity", "pov", "aspirational", "choice", "question", "status", "money", "location", "fantasy",
                  "contrarian", "instructional", "none"],
    "visual_hook": ["text_hook", "exterior_reveal", "view_reveal", "pool", "bedroom", "person_present", "door_opening",
                    "unusual_architecture", "empty_to_full", "before_after", "motion_immediate", "sound_hook", "none"],
    "room": ["bedroom", "living_room", "kitchen", "bathroom", "dining", "closet", "home_theater", "office", "pool",
             "terrace_outdoor", "garden_landscape", "exterior_facade", "multi_room_tour", "hotel_room", "lobby_common",
             "spa", "stairs_hall", "other"],
    "building_type": ["villa", "penthouse", "apartment", "mansion", "cabin_chalet", "treehouse", "hotel_resort", "house",
                      "castle_palace", "unusual_structure", "none_visible"],
    "style": ["modern_luxury", "minimalist", "japandi", "tropical", "mediterranean", "brutalist", "futuristic",
              "organic_modern", "biophilic", "scandinavian", "dark_luxury", "warm_luxury", "industrial", "cyberpunk",
              "classical_luxury", "neoclassical", "art_deco", "rustic_cozy", "mid_century", "maximalist",
              "glam_feminine", "traditional_regional", "other"],
    "landscape": ["ocean_beach", "mountain", "forest", "desert", "jungle_tropical", "lake_river", "snow", "city_skyline",
                  "cliff", "underwater", "space_sky", "rain_window", "none"],
    "lighting": ["daylight", "golden_hour", "blue_hour", "night_artificial", "overcast_rain", "candle_fire", "mixed"],
    "realism": ["fantasy_impossible", "stylized_dreamy", "aspirational_realistic", "real_existing"],
    "visual_quality": ["high", "medium", "low"],
    "camera": ["static", "slow_push_in", "pull_back", "pan", "tilt", "orbit", "drone_aerial", "fly_through", "pov_walk",
               "morph_transform", "zoom", "handheld", "mixed"],
    "audio_type": ["music_only", "music_plus_ambient", "ambient_nature_only", "voiceover", "asmr_sfx", "silence"],
    "text_overlay": ["none", "hook_only", "hook_plus_labels", "continuous_text"],
    "caption_type": ["curiosity", "pov", "aspirational", "choice", "question", "status", "money", "location", "fantasy",
                     "contrarian", "instructional", "descriptive", "promotional", "none"],
    "cta_type": ["comment_keyword", "question_engagement", "follow", "save_share", "link_in_bio", "dm", "shop_product",
                 "tag_friend", "none"],
    "ad_disclosure": ["none", "affiliate", "paid_partnership", "own_product"],
}

FIELDS = [
    "reel_id", "date", "time_posted", "followers_at_post", "pillar", "series_id", "test_id", "variant", "is_trial_reel",
    "format", "hook_type", "hook_text", "visual_hook", "room", "building_type", "style", "landscape", "lighting",
    "location", "realism", "visual_quality", "camera", "length_sec", "n_scenes", "audio_type", "audio_name", "text_overlay",
    "caption_type", "caption_first_line", "cta_type", "hashtags_n", "ai_tool", "prompt_id", "ai_label", "ad_disclosure",
    "views_1h", "views_6h", "views_24h", "views_7d", "reach", "non_follower_reach_pct", "likes", "comments", "shares",
    "saves", "reposts", "followers_gained", "profile_visits", "avg_watch_time", "completion_rate", "skip_rate",
    "link_clicks", "revenue", "notes",
]
NUMERIC = ["followers_at_post", "is_trial_reel", "length_sec", "n_scenes", "hashtags_n", "ai_label", "views_1h",
           "views_6h", "views_24h", "views_7d", "reach", "non_follower_reach_pct", "likes", "comments", "shares",
           "saves", "reposts", "followers_gained", "profile_visits", "avg_watch_time", "completion_rate", "skip_rate",
           "link_clicks", "revenue"]
REQUIRED = ["reel_id", "date", "pillar", "format", "hook_type", "style", "views_24h"]

LIFT_FACTORS = ["pillar", "format", "hook_type", "visual_hook", "room", "building_type", "style", "landscape",
                "lighting", "realism", "visual_quality", "camera", "audio_type", "text_overlay", "caption_type", "cta_type",
                "length_bucket", "hashtag_bucket", "hour_bucket_utc", "ai_tool", "is_trial_reel"]
DECISION_FIELDS = ["series_id", "pillar", "format", "hook_type", "visual_hook", "style"]
REG_FACTORS = ["pillar", "format", "hook_type", "visual_hook", "style", "realism", "camera", "audio_type", "cta_type",
               "text_overlay"]

# Weak research priors, used ONLY to order untested levels for exploration (not significant in the
# public data: Kruskal-Wallis on topic_index p=0.53 for style; see data/processed/analysis_digest.md).
# style: median topic_index of cover-coded reels (segments n>=15); hook: YouTube Shorts proxy title hooks.
PRIOR_STYLE = {"futuristic": 2.06, "rustic_cozy": 1.5, "tropical": 1.44, "scandinavian": 1.14,
               "organic_modern": 1.08, "modern_luxury": 1.05, "mediterranean": 1.05, "traditional_regional": 0.92,
               "minimalist": 0.79, "classical_luxury": 0.70, "dark_luxury": 0.44}
PRIOR_HOOK = {"location": 2.0, "curiosity": 1.15, "fantasy": 1.05, "choice": 0.995, "question": 0.949,
              "money": 0.938, "status": 0.938, "instructional": 0.874}


# ----------------------------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------------------------
def ok(x):
    return x is not None and isinstance(x, (int, float, np.floating)) and not math.isnan(x)


def nanmed(a):
    a = np.asarray([x for x in a if ok(x)], dtype=float)
    return float(np.median(a)) if a.size else NAN


def safe_div(a, b):
    return a / b if ok(a) and ok(b) and b != 0 else NAN


def pooled(rows, num, den, scale=1.0):
    s_n = s_d = 0.0
    k = 0
    for r in rows:
        if ok(r[num]) and ok(r[den]) and r[den] > 0:
            s_n += r[num]
            s_d += r[den]
            k += 1
    return (scale * s_n / s_d) if k and s_d > 0 else NAN


def fnum(x, d=0):
    if not ok(x):
        return "–"
    return f"{x:,.{d}f}".replace(",", " ") if abs(x) >= 1000 or d == 0 else f"{x:.{d}f}"


def fpct(x, d=1):
    return "–" if not ok(x) else f"{100 * x:.{d}f} %"


def fmul(x):
    return "–" if not ok(x) else f"×{x:.2f}"


def band(value, key):
    if key not in LAUNCH_BANDS or not ok(value):
        return "–"
    (a, b, c), hib = LAUNCH_BANDS[key]
    if hib:
        idx = 0 if value < a else 1 if value < b else 2 if value < c else 3
    else:
        idx = 0 if value > a else 1 if value > b else 2 if value > c else 3
    return BAND_LABELS[idx]


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return out


def iso_week(ts):
    y, w, _ = ts.isocalendar()
    return f"{y}-W{w:02d}"


def bh_qvalues(pvals):
    p = np.asarray(pvals, dtype=float)
    n = p.size
    if n == 0:
        return p
    order = np.argsort(p)
    ranked = p[order] * n / (np.arange(n) + 1)
    q = np.minimum.accumulate(ranked[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.minimum(q, 1.0)
    return out


# ----------------------------------------------------------------------------------------------
# loading / validation / derived metrics
# ----------------------------------------------------------------------------------------------
def to_float(x, decimal_comma=False):
    s = (x or "").strip().replace(" ", "").replace(" ", "")
    if s == "" or s.lower() in ("na", "n/a", "nan", "none", "null", "-", "–"):
        return NAN
    s = s.replace("%", "")
    if decimal_comma and re.fullmatch(r"-?\d{1,3}(\.\d{3})+(,\d+)?", s):   # German thousands: 1.400,5
        s = s.replace(".", "").replace(",", ".")
    elif not decimal_comma and re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", s):  # English thousands: 1,400.5
        s = s.replace(",", "")
    elif "," in s and "." not in s:                                          # decimal comma: 6,1
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None  # signals a parse problem


def parse_ts(date_s, time_s):
    date_s = (date_s or "").strip()
    time_s = (time_s or "").strip() or "12:00"
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%d.%m.%Y %H:%M", "%d.%m.%Y %H:%M:%S"):
        try:
            return dt.datetime.strptime(f"{date_s} {time_s}", fmt).replace(tzinfo=dt.timezone.utc)
        except ValueError:
            continue
    return None


def load_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        head = fh.readline()
        fh.seek(0)
        delim = max([",", ";", "\t"], key=head.count)
        rows = list(csv.DictReader(fh, delimiter=delim))
    return rows, delim


def prepare(raw_rows, delim):
    issues = []
    rows = []
    dec_comma = delim == ";"
    header = list(raw_rows[0].keys()) if raw_rows else []
    missing_cols = [f for f in FIELDS if f not in header]
    if missing_cols:
        issues.append(f"Fehlende Spalten (werden leer angenommen): {', '.join(missing_cols)}")
    for i, rr in enumerate(raw_rows, start=2):
        r = {k: (rr.get(k) or "").strip() for k in FIELDS}
        if not any(r.values()):
            continue
        for k in NUMERIC:
            v = to_float(r[k], dec_comma)
            if v is None:
                issues.append(f"Zeile {i} ({r['reel_id']}): '{k}' ist keine Zahl ('{r[k]}') -> leer")
                v = NAN
            elif ok(v) and v < 0:
                issues.append(f"Zeile {i} ({r['reel_id']}): '{k}' ist negativ ({v:g}) -> leer")
                v = NAN
            r[k] = v
        for k in ALLOWED:
            r[k] = r[k].lower()
            if r[k] and r[k] not in ALLOWED[k]:
                issues.append(f"Zeile {i} ({r['reel_id']}): {k}='{r[k]}' nicht im Codebook")
        for k in REQUIRED:
            if (isinstance(r[k], str) and not r[k]) or (not isinstance(r[k], str) and not ok(r[k])):
                issues.append(f"Zeile {i} ({r['reel_id']}): Pflichtfeld '{k}' fehlt")
        r["ts"] = parse_ts(r["date"], r["time_posted"])
        if r["ts"] is None:
            issues.append(f"Zeile {i} ({r['reel_id']}): Datum/Zeit nicht lesbar -> Zeile ignoriert")
            continue
        if shortcode_to_datetime and len(r["reel_id"]) == 11 and not r["reel_id"].upper().startswith(("EXAMPLE", "SIM")):
            sc_ts = shortcode_to_datetime(r["reel_id"])
            if sc_ts and abs((sc_ts - r["ts"]).total_seconds()) > 36 * 3600:
                issues.append(f"Zeile {i} ({r['reel_id']}): Datum weicht vom Shortcode-Zeitstempel ab ({sc_ts:%Y-%m-%d %H:%M} UTC)")
        seq = [r["views_1h"], r["views_6h"], r["views_24h"], r["views_7d"]]
        seq_ok = [x for x in seq if ok(x)]
        if any(b < a for a, b in zip(seq_ok, seq_ok[1:])):
            issues.append(f"Zeile {i} ({r['reel_id']}): views_1h<=6h<=24h<=7d verletzt")
        if ok(r["reach"]) and ok(r["views_7d"]) and r["reach"] > r["views_7d"] * 1.02:
            issues.append(f"Zeile {i} ({r['reel_id']}): reach > views_7d (Reach = eindeutige Konten, sollte <= Views sein)")
        if ok(r["hashtags_n"]) and r["hashtags_n"] > 5:
            issues.append(f"Zeile {i} ({r['reel_id']}): hashtags_n={r['hashtags_n']:.0f} > 5 (Plattformlimit seit 12/2025, q01)")
        for k in ("completion_rate", "skip_rate"):
            if ok(r[k]) and r[k] > 1:
                r[k] = r[k] / 100.0  # entered as percent
        if ok(r["non_follower_reach_pct"]) and r["non_follower_reach_pct"] <= 1:
            r["non_follower_reach_pct"] *= 100.0  # entered as share
        r["is_example"] = r["reel_id"].upper().startswith("EXAMPLE") or "EXAMPLE" in r["notes"].upper()
        r["is_sim"] = r["reel_id"].upper().startswith("SIM_")
        rows.append(r)
    rows.sort(key=lambda x: x["ts"])
    return rows, issues


def length_bucket(x):
    if not ok(x):
        return ""
    for hi, lab in ((5, "00-05s"), (8, "06-08s"), (12, "09-12s"), (20, "13-20s"), (30, "21-30s")):
        if x <= hi:
            return lab
    return "31s+"


def derive(rows):
    valid_v24 = []
    glob = nanmed([r["views_24h"] for r in rows])
    t0 = rows[0]["ts"] if rows else None
    for r in rows:
        v24, v7 = r["views_24h"], r["views_7d"]
        vref = v7 if ok(v7) else v24
        r["views_ref"] = vref
        r["log_v24"] = math.log1p(v24) if ok(v24) else NAN
        prev = valid_v24[-ROLL_WINDOW:]
        base = float(np.median(prev)) if len(prev) >= ROLL_MIN else glob
        r["ai_base_rolling"] = len(prev) >= ROLL_MIN
        r["account_index"] = safe_div(v24, base) if ok(base) and base > 0 else NAN
        if ok(v24):
            valid_v24.append(v24)
        r["f1k"] = safe_div(1000 * r["followers_gained"], vref) if ok(r["followers_gained"]) else NAN
        r["likes_pv"] = safe_div(r["likes"], vref)
        r["comments_pv"] = safe_div(r["comments"], vref)
        r["likes_pr"] = safe_div(r["likes"], r["reach"])
        r["sends_pr"] = safe_div(r["shares"], r["reach"])
        r["saves_pr"] = safe_div(r["saves"], r["reach"])
        r["pv_rate"] = safe_div(r["profile_visits"], vref)
        r["follow_conv"] = safe_div(r["followers_gained"], r["profile_visits"])
        r["watch_pct"] = safe_div(r["avg_watch_time"], r["length_sec"])
        r["nf_share"] = r["non_follower_reach_pct"] / 100.0 if ok(r["non_follower_reach_pct"]) else NAN
        r["nf_reach"] = r["reach"] * r["nf_share"] if ok(r["reach"]) and ok(r["nf_share"]) else NAN
        r["vpf_7d"] = safe_div(v7, r["followers_at_post"]) if ok(r["followers_at_post"]) and r["followers_at_post"] >= 1000 else NAN
        r["longtail"] = 1 - safe_div(v24, v7) if ok(v24) and ok(v7) and v7 > 0 else NAN
        r["clicks_1k_reach"] = safe_div(1000 * r["link_clicks"], r["reach"]) if ok(r["link_clicks"]) else NAN
        r["rpm"] = safe_div(1000 * r["revenue"], vref) if ok(r["revenue"]) else NAN
        r["length_bucket"] = length_bucket(r["length_sec"])
        h = r["hashtags_n"]
        r["hashtag_bucket"] = "" if not ok(h) else "0" if h == 0 else "1-3" if h <= 3 else "4-5" if h <= 5 else ">5"
        hr = r["ts"].hour
        r["hour_bucket_utc"] = f"{(hr // 6) * 6:02d}-{(hr // 6) * 6 + 5:02d}h"
        r["is_trial_reel"] = "" if not ok(r["is_trial_reel"]) else "trial" if r["is_trial_reel"] >= 1 else "regular"
        r["day_index"] = (r["ts"] - t0).total_seconds() / 86400.0
        r["week"] = iso_week(r["ts"])
        ai = r["account_index"]
        r["reel_class"] = "–" if not ok(ai) else next(lab for thr, lab in REEL_CLASSES if ai >= thr)
        r["vpf_tier"] = "–" if not ok(r["vpf_7d"]) else next(lab for thr, lab in VPF_TIERS if r["vpf_7d"] >= thr)
        r["policy"] = "POLICY" in r["notes"].upper()
    return rows


# ----------------------------------------------------------------------------------------------
# statistics
# ----------------------------------------------------------------------------------------------
def boot_diff_means(y, mask, B, rng):
    y = np.asarray(y, dtype=float)
    valid = ~np.isnan(y)
    a, b = y[mask & valid], y[~mask & valid]
    if a.size < 1 or b.size < 1:
        return None
    ia = rng.integers(0, a.size, size=(B, a.size))
    ib = rng.integers(0, b.size, size=(B, b.size))
    d = a[ia].mean(axis=1) - b[ib].mean(axis=1)
    lo, hi = np.quantile(d, [(1 - CI_LEVEL) / 2, 1 - (1 - CI_LEVEL) / 2])
    p = max(2 * min((d <= 0).mean(), (d >= 0).mean()), 1.0 / B)
    return {"n": int(a.size), "n_rest": int(b.size), "point": float(a.mean() - b.mean()), "lo": float(lo),
            "hi": float(hi), "p_pos": float((d > 0).mean()), "p_neg": float((d < 0).mean()), "p": float(min(p, 1.0))}


def boot_ratio(num, den, mask, B, rng, scale=1000.0, pseudo=0.5):
    num = np.asarray(num, dtype=float)
    den = np.asarray(den, dtype=float)
    valid = ~np.isnan(num) & ~np.isnan(den) & (den > 0)
    fa, va = num[mask & valid], den[mask & valid]
    fb, vb = num[~mask & valid], den[~mask & valid]
    if fa.size < 1 or fb.size < 1:
        return None
    point = math.log((fa.sum() + pseudo) / va.sum()) - math.log((fb.sum() + pseudo) / vb.sum())
    ia = rng.integers(0, fa.size, size=(B, fa.size))
    ib = rng.integers(0, fb.size, size=(B, fb.size))
    d = np.log((fa[ia].sum(1) + pseudo) / va[ia].sum(1)) - np.log((fb[ib].sum(1) + pseudo) / vb[ib].sum(1))
    lo, hi = np.quantile(d, [(1 - CI_LEVEL) / 2, 1 - (1 - CI_LEVEL) / 2])
    p = max(2 * min((d <= 0).mean(), (d >= 0).mean()), 1.0 / B)
    return {"n": int(fa.size), "rate": scale * fa.sum() / va.sum(), "rate_rest": scale * fb.sum() / vb.sum(),
            "point": point, "lo": float(lo), "hi": float(hi), "p_pos": float((d > 0).mean()),
            "p_neg": float((d < 0).mean()), "p": float(min(p, 1.0))}


def flag(res, qv, min_n):
    if res is None:
        return "–"
    if res["n"] < min_n:
        return f"n<{min_n}"
    if (res["lo"] > 0 or res["hi"] < 0) and ok(qv) and qv < FDR_Q:
        return "WINNER (belegt)" if res["lo"] > 0 else "LOSER (belegt)"
    if res["p_pos"] >= P_DIRECTION:
        return "Tendenz +"
    if res["p_neg"] >= P_DIRECTION:
        return "Tendenz −"
    return "offen"


def factor_lifts(rows, factors, B, rng, min_n, raw=False):
    # default: trend-adjusted log(views_24h) = log(views_24h) - log(rolling baseline) = log(account_index),
    # so that account growth over the 30 days does not masquerade as a factor effect
    y = np.array([r["log_v24"] if raw else (math.log(r["account_index"]) if ok(r["account_index"]) and r["account_index"] > 0 else NAN)
                  for r in rows])
    fol = np.array([r["followers_gained"] for r in rows], dtype=float)
    vref = np.array([r["views_ref"] for r in rows], dtype=float)
    results = []
    for f in factors:
        vals = np.array([str(r.get(f) or "") for r in rows])
        for lvl in sorted(set(vals) - {""}):
            mask = vals == lvl
            rv = boot_diff_means(y, mask, B, rng)
            rf = boot_ratio(fol, vref, mask, B, rng)
            if rv is None:
                continue
            sub = [r for r, m in zip(rows, mask) if m]
            results.append({"factor": f, "level": lvl, "views": rv, "f1k": rf,
                            "median_v24": nanmed([r["views_24h"] for r in sub]),
                            "median_ai": nanmed([r["account_index"] for r in sub])})
    for key in ("views", "f1k"):
        idx = [i for i, r in enumerate(results) if r[key] is not None and r[key]["n"] >= min_n]
        q = bh_qvalues([results[i][key]["p"] for i in idx])
        for i in results:
            i[key + "_q"] = NAN
        for j, i in enumerate(idx):
            results[i][key + "_q"] = float(q[j])
    for r in results:
        r["views_flag"] = flag(r["views"], r["views_q"], min_n)
        r["f1k_flag"] = flag(r["f1k"], r["f1k_q"], min_n)
    return results


def build_design(rows, factors, numeric):
    n = len(rows)
    cols, names, meta = [], [], []
    for f in factors:
        vals = [str(r.get(f) or "") for r in rows]
        cnt = Counter(v for v in vals if v)
        rare = {k for k, c in cnt.items() if c < 2}
        vals = ["_rare" if v in rare else v for v in vals]
        cnt = Counter(v for v in vals if v)
        if len(cnt) < 2:
            continue
        ref = cnt.most_common(1)[0][0]
        for lvl in sorted(cnt):
            if lvl == ref:
                continue
            cols.append(np.array([1.0 if v == lvl else 0.0 for v in vals]))
            names.append(f"{f}={lvl}")
            meta.append({"n": cnt[lvl], "ref": ref})
    for name, arr in numeric:
        a = np.array(arr, dtype=float)
        if np.all(np.isnan(a)):
            continue
        a[np.isnan(a)] = np.nanmedian(a)
        sd = a.std()
        if sd == 0:
            continue
        cols.append((a - a.mean()) / sd)
        names.append(f"{name} (+1 SD)")
        meta.append({"n": n, "ref": None})
    X = np.column_stack(cols) if cols else np.zeros((n, 0))
    return X, names, meta


def ridge_beta(X, y, lam):
    Xc = X - X.mean(axis=0)
    yc = y - y.mean()
    A = Xc.T @ Xc + lam * np.eye(X.shape[1])
    return np.linalg.solve(A, Xc.T @ yc)


def ridge_loo_mse(X, y, lam):
    n = X.shape[0]
    Xc = X - X.mean(axis=0)
    yc = y - y.mean()
    A_inv = np.linalg.inv(Xc.T @ Xc + lam * np.eye(X.shape[1]))
    H = Xc @ A_inv @ Xc.T
    e = yc - H @ yc
    h = np.clip(np.diag(H) + 1.0 / n, None, 1 - 1e-6)
    return float(np.mean((e / (1 - h)) ** 2))


def ridge_analysis(rows, B, rng):
    use = [r for r in rows if ok(r["log_v24"])]
    n = len(use)
    if n < 3:
        return {"skipped": f"n={n} < 3"}
    y = np.array([r["log_v24"] for r in use])
    if y.std() == 0:
        return {"skipped": "keine Varianz in views_24h"}
    numeric = [("log_length_sec", [math.log(r["length_sec"]) if ok(r["length_sec"]) and r["length_sec"] > 0 else NAN for r in use]),
               ("hashtags_n", [r["hashtags_n"] for r in use]),
               ("day_index", [r["day_index"] for r in use]),
               ("log_followers_at_post", [math.log1p(r["followers_at_post"]) if ok(r["followers_at_post"]) else NAN for r in use])]
    X, names, meta = build_design(use, REG_FACTORS, numeric)
    if X.shape[1] == 0:
        return {"skipped": "keine variierenden Faktoren"}
    grid = np.logspace(-2, 3, 26)
    mses = [ridge_loo_mse(X, y, lam) for lam in grid]
    best = min(range(len(grid)), key=lambda i: (round(mses[i], 10), -grid[i]))
    lam = float(grid[best])
    beta = ridge_beta(X, y, lam)
    fitted = (X - X.mean(0)) @ beta + y.mean()
    r2 = 1 - np.sum((y - fitted) ** 2) / np.sum((y - y.mean()) ** 2)
    r2_loo = 1 - mses[best] / np.var(y)
    Bb = min(B, 500)
    boots = np.empty((Bb, X.shape[1]))
    for b in range(Bb):
        idx = rng.integers(0, n, n)
        Xb, yb = X[idx], y[idx]
        boots[b] = ridge_beta(Xb, yb, lam) if yb.std() > 0 else 0.0
    lo, hi = np.quantile(boots, [0.05, 0.95], axis=0)
    terms = [{"term": nm, "beta": float(bt), "lo": float(l), "hi": float(h), "n": m["n"], "ref": m["ref"]}
             for nm, bt, l, h, m in zip(names, beta, lo, hi, meta)]
    terms.sort(key=lambda t: -t["beta"])
    out = {"n": n, "p": X.shape[1], "lambda": lam, "r2": float(r2), "r2_loo": float(r2_loo), "terms": terms}
    if HAVE_SM and n >= X.shape[1] + 10:
        try:
            res = sm.OLS(y, sm.add_constant(X)).fit(cov_type="HC3")
            out["ols"] = [(names[i], float(res.params[i + 1]), float(res.pvalues[i + 1]))
                          for i in range(X.shape[1]) if res.pvalues[i + 1] < 0.05]
        except Exception as e:  # noqa: BLE001
            out["ols_error"] = str(e)
    elif HAVE_SM:
        out["ols_note"] = f"OLS-Gegencheck übersprungen (n={n} < p+10={X.shape[1] + 10})"
    else:
        out["ols_note"] = "statsmodels nicht installiert – nur Ridge (numpy)"
    return out


# ----------------------------------------------------------------------------------------------
# decisions KEEP / ITERATE / SCALE / KILL
# ----------------------------------------------------------------------------------------------
def decide_groups(rows, lifts, B, rng, min_n):
    acct_f1k = pooled(rows, "followers_gained", "views_ref", 1000)
    acct_sends = nanmed([r["sends_pr"] for r in rows])
    acct_watch = nanmed([r["watch_pct"] for r in rows])
    acct_ai = nanmed([r["account_index"] for r in rows])  # >1 in a growing account (rolling median lags)
    lift_map = {(l["factor"], l["level"]): l for l in lifts}
    y = np.array([r["log_v24"] for r in rows])
    out = []
    for f in DECISION_FIELDS:
        vals = np.array([str(r.get(f) or "") for r in rows])
        for lvl in sorted(set(vals) - {""}):
            mask = vals == lvl
            grp = [r for r, m in zip(rows, mask) if m]
            n = len(grp)
            lf = lift_map.get((f, lvl))
            rv = lf["views"] if lf else boot_diff_means(y, mask, B, rng)
            p_pos = rv["p_pos"] if rv else NAN
            p_neg = rv["p_neg"] if rv else NAN
            med_ai = safe_div(nanmed([r["account_index"] for r in grp]), acct_ai)  # group index relative to account
            f1k = pooled(grp, "followers_gained", "views_ref", 1000)
            f1k_ratio = safe_div(f1k, acct_f1k)
            sends_ratio = safe_div(nanmed([r["sends_pr"] for r in grp]), acct_sends)
            watch_ratio = safe_div(nanmed([r["watch_pct"] for r in grp]), acct_watch)
            ns_index = med_ai * f1k_ratio if ok(med_ai) and ok(f1k_ratio) else med_ai
            packaging = ok(med_ai) and med_ai < PACKAGING_AI_MAX and (
                (ok(sends_ratio) and sends_ratio >= PACKAGING_RATIO) or (ok(watch_ratio) and watch_ratio >= PACKAGING_RATIO))
            if any(r["policy"] for r in grp):
                dec, why = "KILL", "POLICY-Vermerk (Account Status/Originalität/Kennzeichnung) – sofort stoppen"
            elif (n >= min_n and ok(med_ai) and med_ai < KILL_MEDIAN_AI and ok(p_neg) and p_neg >= P_DECIDE
                  and ok(ns_index) and ns_index < KILL_NS_INDEX and not packaging):
                dec, why = "KILL", (f"Gruppen-Index {med_ai:.2f} < {KILL_MEDIAN_AI}, P(schlechter) {fpct(p_neg, 0)}, "
                                    f"North-Star-Index {ns_index:.2f} < {KILL_NS_INDEX}")
            elif n >= MIN_N_ITERATE and ok(med_ai) and med_ai < KILL_MEDIAN_AI and ok(f1k_ratio) and f1k_ratio >= 1.5:
                dec, why = "ITERATE", f"wenig Reichweite, aber starke Follow-Conversion (F/1k {fmul(f1k_ratio)} Konto) → Hook/Cover testen, nicht töten"
            elif n >= min_n and ok(med_ai) and med_ai >= SCALE_MEDIAN_AI and ok(p_pos) and p_pos >= P_DECIDE and (not ok(f1k_ratio) or f1k_ratio >= F1K_SCALE_MIN):
                why = f"Gruppen-Index {med_ai:.2f}, P(besser) {fpct(p_pos, 0)}, F/1k {fmul(f1k_ratio)} Konto"
                if not ok(f1k_ratio):
                    why += " (Follow-Daten fehlen – prüfen)"
                dec = "SCALE"
            elif n >= MIN_N_ITERATE and ok(med_ai) and med_ai >= REACH_NO_FOLLOW_AI and ok(f1k_ratio) and f1k_ratio < F1K_ITER_MAX:
                dec, why = "ITERATE", f"Reichweite ohne Follows (F/1k {fmul(f1k_ratio)} Konto) → CTA, Serienbindung, Profil"
            elif n >= MIN_N_ITERATE and packaging:
                dec, why = "ITERATE", f"Inhalt resoniert (Sends {fmul(sends_ratio)}, Watch {fmul(watch_ratio)}), Views schwach → Hook/Cover/1. Sekunde"
            elif n >= min_n and ok(med_ai) and med_ai >= SCALE_MEDIAN_AI:
                dec, why = "ITERATE", f"stark (Gruppen-Index {med_ai:.2f}), aber noch nicht belastbar (P {fpct(p_pos, 0)}) → replizieren"
            elif n >= min_n:
                dec = "KEEP"
                if ok(p_neg) and p_neg >= P_DECIDE:
                    why = f"unter Schnitt (Gruppen-Index {fnum(med_ai, 2)}, P(schlechter) {fpct(p_neg, 0)}) → Slots reduzieren, Hook testen"
                elif ok(p_pos) and p_pos >= P_DECIDE:
                    why = f"über Schnitt (Gruppen-Index {fnum(med_ai, 2)}, P(besser) {fpct(p_pos, 0)}) → SCALE-Kandidat"
                else:
                    why = f"im Rahmen (Gruppen-Index {fnum(med_ai, 2)})"
            else:
                dec, why = "OFFEN", f"n={n} < {min_n} → weiter testen"
            out.append({"field": f, "level": lvl, "n": n, "median_ai": med_ai, "f1k": f1k, "p_pos": p_pos,
                        "ns_index": ns_index, "decision": dec, "why": why})
    return out, acct_f1k


# ----------------------------------------------------------------------------------------------
# Thompson sampling over hook_type x style
# ----------------------------------------------------------------------------------------------
def thompson(rows, rng, draws=20000, k_prior=2.0, n_explore_levels=2):
    f1k_med = nanmed([r["f1k"] for r in rows])
    data = defaultdict(lambda: [0, 0])
    hooks, styles = Counter(), Counter()
    for r in rows:
        if not r["hook_type"] or not r["style"] or not ok(r["account_index"]):
            continue
        win = r["account_index"] >= 1.0 and (not ok(r["f1k"]) or not ok(f1k_med) or r["f1k"] >= f1k_med)
        data[(r["hook_type"], r["style"])][0 if win else 1] += 1
        hooks[r["hook_type"]] += 1
        styles[r["style"]] += 1
    if not data:
        return None

    def marg(counter_key, idx):
        w = sum(v[0] for k, v in data.items() if k[idx] == counter_key)
        n = sum(v[0] + v[1] for k, v in data.items() if k[idx] == counter_key)
        return (w + 1) / (n + 2)

    glob_w = sum(v[0] for v in data.values())
    glob_n = sum(v[0] + v[1] for v in data.values())
    glob_p = (glob_w + 1) / (glob_n + 2)
    new_hooks = [h for h in sorted(PRIOR_HOOK, key=lambda k: -PRIOR_HOOK[k]) if h not in hooks][:n_explore_levels]
    new_styles = [s for s in sorted(PRIOR_STYLE, key=lambda k: -PRIOR_STYLE[k]) if s not in styles][:n_explore_levels]
    cand_h = list(hooks) + new_hooks
    cand_s = list(styles) + new_styles
    cells = [(h, s) for h in cand_h for s in cand_s]
    alphas, betas, info = [], [], []
    for h, s in cells:
        ph = marg(h, 0) if h in hooks else glob_p
        ps = marg(s, 1) if s in styles else glob_p
        m = (ph + ps) / 2
        w, l = data.get((h, s), [0, 0])
        alphas.append(1 + k_prior * m + w)
        betas.append(1 + k_prior * (1 - m) + l)
        info.append({"hook_type": h, "style": s, "n": w + l, "wins": w, "new": h in new_hooks or s in new_styles})
    a, b = np.array(alphas), np.array(betas)
    samples = rng.beta(a[None, :], b[None, :], size=(draws, len(cells)))
    p_best = np.bincount(samples.argmax(axis=1), minlength=len(cells)) / draws
    ts_pick = Counter(int(rng.beta(a, b).argmax()) for _ in range(SLOTS_TS))
    for i, c in enumerate(info):
        c["post_mean"] = float(a[i] / (a[i] + b[i]))
        c["p_best"] = float(p_best[i])
        c["ts_slots"] = ts_pick.get(i, 0)
    info.sort(key=lambda c: (-c["p_best"], -c["post_mean"]))
    return {"cells": info, "f1k_med": f1k_med, "new_hooks": new_hooks, "new_styles": new_styles}


# ----------------------------------------------------------------------------------------------
# tests (test_id x variant)
# ----------------------------------------------------------------------------------------------
def ab_tests(rows, B, rng):
    out = []
    by_test = defaultdict(list)
    for r in rows:
        if r["test_id"]:
            by_test[r["test_id"]].append(r)
    for tid, grp in sorted(by_test.items()):
        variants = sorted({r["variant"] or "?" for r in grp})
        low = {v.lower(): v for v in variants}
        control = low.get("control") or low.get("a") or variants[0]
        y = np.array([math.log(r["account_index"]) if ok(r["account_index"]) and r["account_index"] > 0 else NAN for r in grp])
        vals = np.array([r["variant"] or "?" for r in grp])
        for v in variants:
            sub = [r for r in grp if (r["variant"] or "?") == v]
            p_better = NAN
            if v != control:
                m = (vals == v) | (vals == control)
                res = boot_diff_means(y[m], vals[m] == v, B, rng)
                p_better = res["p_pos"] if res else NAN
            out.append({"test_id": tid, "variant": v, "control": v == control, "n": len(sub),
                        "median_v24": nanmed([r["views_24h"] for r in sub]),
                        "median_ai": nanmed([r["account_index"] for r in sub]),
                        "f1k": pooled(sub, "followers_gained", "views_ref", 1000), "p_better": p_better})
    return out


# ----------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------
def week_kpis(rows, target_share):
    k = {"n": len(rows), "days": len({r["ts"].date() for r in rows})}
    k["views_24h_median"] = nanmed([r["views_24h"] for r in rows])
    k["views_7d_sum"] = sum(r["views_7d"] for r in rows if ok(r["views_7d"]))
    k["reach_sum"] = sum(r["reach"] for r in rows if ok(r["reach"]))
    k["nf_reach_sum"] = sum(r["nf_reach"] for r in rows if ok(r["nf_reach"]))
    k["qualified_reach"] = k["nf_reach_sum"] * target_share if target_share is not None else NAN
    k["median_ai"] = nanmed([r["account_index"] for r in rows])
    k["hits"] = sum(1 for r in rows if r["reel_class"] == "Hit")
    k["follows_sum"] = sum(r["followers_gained"] for r in rows if ok(r["followers_gained"]))
    k["follows_per_1k"] = pooled(rows, "followers_gained", "views_ref", 1000)
    k["non_follower_share"] = nanmed([r["nf_share"] for r in rows])
    k["watch_pct"] = nanmed([r["watch_pct"] for r in rows])
    k["skip_rate"] = nanmed([r["skip_rate"] for r in rows])
    k["completion_rate"] = nanmed([r["completion_rate"] for r in rows])
    k["likes_per_view"] = pooled(rows, "likes", "views_ref")
    k["comments_per_view"] = pooled(rows, "comments", "views_ref")
    k["likes_per_reach"] = pooled(rows, "likes", "reach")
    k["sends_per_reach"] = pooled(rows, "shares", "reach")
    k["saves_per_reach"] = pooled(rows, "saves", "reach")
    k["profile_visits_per_view"] = pooled(rows, "profile_visits", "views_ref")
    k["follow_conversion"] = pooled(rows, "followers_gained", "profile_visits")
    k["longtail"] = nanmed([r["longtail"] for r in rows])
    k["link_clicks"] = sum(r["link_clicks"] for r in rows if ok(r["link_clicks"]))
    k["revenue"] = sum(r["revenue"] for r in rows if ok(r["revenue"]))
    k["clicks_1k_reach"] = pooled(rows, "link_clicks", "reach", 1000)
    k["rpm"] = pooled(rows, "revenue", "views_ref", 1000)
    k["epc"] = pooled(rows, "revenue", "link_clicks")
    return k


def delta(cur, prev):
    if not ok(cur) or not ok(prev) or prev == 0:
        return "–"
    return f"{100 * (cur / prev - 1):+.0f} %"


def reel_action(r, acct):
    c = r["reel_class"]
    if r["policy"]:
        return "POLICY: stoppen, Account Status prüfen"
    low_f = ok(r["f1k"]) and ok(acct["f1k"]) and r["f1k"] < F1K_ITER_MAX * acct["f1k"]
    pack = (ok(r["sends_pr"]) and ok(acct["sends"]) and r["sends_pr"] >= PACKAGING_RATIO * acct["sends"]) or \
           (ok(r["watch_pct"]) and ok(acct["watch"]) and r["watch_pct"] >= PACKAGING_RATIO * acct["watch"])
    if c == "Hit":
        return "Hit ohne Follows → Serien-CTA/Profil prüfen" if low_f else "Folge-Variante in ≤72 h (gleiche Serie, neuer Raum/Stil)"
    if c in ("Schwach", "Flop") and pack:
        return "Inhalt gut, Verpackung schwach → neuer Hook/Cover"
    if c == "Flop":
        return "nicht wiederholen; Faktoren in Lift-Tabelle beobachten"
    return "normal weiter"


def percentiles_block(rows):
    keys = [("views_24h", "views_24h"), ("likes_pv", "likes_per_view"), ("comments_pv", "comments_per_view"),
            ("sends_pr", "sends_per_reach"), ("saves_pr", "saves_per_reach"), ("f1k", "follows_per_1k"),
            ("pv_rate", "profile_visits_per_view"), ("follow_conv", "follow_conversion"), ("watch_pct", "watch_pct"),
            ("skip_rate", "skip_rate (niedriger = besser)"), ("completion_rate", "completion_rate"),
            ("nf_share", "non_follower_share")]
    out = []
    for k, lab in keys:
        a = np.array([r[k] for r in rows if ok(r[k])])
        if a.size == 0:
            out.append([lab, 0, "–", "–", "–", "–"])
            continue
        qs = np.quantile(a, [0.25, 0.5, 0.75, 0.9])
        pct = k not in ("views_24h", "f1k")
        f = (lambda x: fpct(x, 2)) if pct else (lambda x: fnum(x, 1) if k == "f1k" else fnum(x))
        out.append([lab, a.size] + [f(x) for x in qs])
    return out


def next_tests(decisions, lifts, ts, min_n):
    sug = []
    for d in decisions:
        if d["decision"] == "SCALE":
            sug.append(f"SCALE `{d['field']}={d['level']}`: 3–5 neue Varianten, ≥1 Slot/Tag (Champion-Slot).")
    for d in decisions:
        if d["decision"] == "ITERATE" and "Hook" in d["why"]:
            sug.append(f"Hook-/Cover-Test auf `{d['field']}={d['level']}`: gleiche Szene neu generieren, 2 neue Hook-Typen "
                       f"(keine identischen Re-Uploads – Originalitätsregel, q01).")
        elif d["decision"] == "ITERATE" and "Follows" in d["why"]:
            sug.append(f"Follow-Test auf `{d['field']}={d['level']}`: Serien-Kennung im Hook + CTA `follow` vs. `save_share`.")
    lean = [l for l in lifts if l["views_flag"] == "Tendenz +" and l["views"]["n"] >= min_n]
    for l in sorted(lean, key=lambda l: -l["views"]["point"])[:3]:
        sug.append(f"Replikation `{l['factor']}={l['level']}` ({fmul(math.exp(l['views']['point']))} Views, noch nicht belegt): "
                   f"{min_n} weitere Reels, übrige Faktoren variieren.")
    small = [l for l in lifts if l["views"]["n"] < min_n and l["views"]["point"] > 0.4 and l["factor"] in ("hook_type", "style", "format")]
    for l in sorted(small, key=lambda l: -l["views"]["point"])[:2]:
        sug.append(f"Mehr Daten für `{l['factor']}={l['level']}` (n={l['views']['n']}, Punktschätzung "
                   f"{fmul(math.exp(l['views']['point']))}) – bis n={min_n} auffüllen.")
    if ts:
        top = [c for c in ts["cells"] if c["ts_slots"] > 0][:4]
        if top:
            sug.append("Thompson-Slots nächste Woche: " + ", ".join(f"{c['hook_type']}×{c['style']} ({c['ts_slots']})" for c in top) + ".")
        if ts["new_hooks"] or ts["new_styles"]:
            sug.append("Exploration (noch nie getestet, schwacher Research-Prior): Hooks " + (", ".join(ts["new_hooks"]) or "–")
                       + "; Stile " + (", ".join(ts["new_styles"]) or "–") + ".")
    return sug[:10]


def build_report(rows, all_rows, issues, args, rng, source_label):
    L = []
    B = args.bootstrap
    min_n = args.min_n
    L.append(f"# Winner-Report ({source_label})")
    L.append("")
    L.append(f"Erstellt: {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC · Reels: {len(rows)} · "
             f"Zeitraum: {rows[0]['ts']:%Y-%m-%d} – {rows[-1]['ts']:%Y-%m-%d} · Bootstrap B={B} · min. n={min_n} · "
             f"statsmodels: {'ja' if HAVE_SM else 'nein'}")
    if all(r["is_example"] for r in rows):
        L.append("")
        L.append("> **ACHTUNG: Nur EXAMPLE-Zeilen (fiktive Werte).** Ausgabe ist ein Funktionstest, keine Aussage.")
    elif any(r["is_sim"] for r in rows):
        L.append("")
        L.append("> **SIMULIERTE DATEN (--demo).** Effekte sind künstlich eingebaut – nur zum Kennenlernen des Reports.")
    L.append("")

    weeks = sorted({r["week"] for r in rows})
    week = args.week or weeks[-1]
    if week not in weeks:
        L.append(f"_Woche {week} hat keine Daten; verfügbar: {', '.join(weeks)}_")
        week = weeks[-1]
    wi = weeks.index(week)
    prev_week = weeks[wi - 1] if wi > 0 else None
    wk = [r for r in rows if r["week"] == week]
    pw = [r for r in rows if r["week"] == prev_week] if prev_week else []
    share = args.target_market_share
    kc, kp = week_kpis(wk, share), (week_kpis(pw, share) if pw else None)

    L.append(f"## 1. Wochen-KPIs {week}" + (f" (vs. {prev_week})" if prev_week else ""))
    L.append("")
    L.append(f"Reels: {kc['n']} an {kc['days']} Tagen (Soll: {SLOTS_PER_WEEK}/Woche) · Hits (Index ≥2): {kc['hits']} · "
             f"Median account_index: {fnum(kc['median_ai'], 2)}")
    L.append("")
    spec = [
        ("North Star: Follows gesamt (7-Tage-Stand)", "follows_sum", fnum, None),
        ("Follows pro 1.000 Views (gepoolt)", "follows_per_1k", lambda x: fnum(x, 2), "follows_per_1k"),
        ("Nicht-Follower-Reichweite (Σ)", "nf_reach_sum", fnum, None),
        ("Qualifizierte Reichweite (× Zielmarkt-Anteil)", "qualified_reach", fnum, None),
        ("views_24h (Median)", "views_24h_median", fnum, "views_24h_median"),
        ("Views 7d (Σ)", "views_7d_sum", fnum, None),
        ("Nicht-Follower-Anteil Reach (Median)", "non_follower_share", fpct, "non_follower_share"),
        ("Ø % angesehen (avg_watch_time/Länge, Median)", "watch_pct", fpct, "watch_pct"),
        ("Skip Rate 3 s (Median)", "skip_rate", fpct, "skip_rate"),
        ("Completion Rate (Median)", "completion_rate", fpct, "completion_rate"),
        ("Likes/View", "likes_per_view", lambda x: fpct(x, 2), "likes_per_view"),
        ("Likes/Reach", "likes_per_reach", lambda x: fpct(x, 2), None),
        ("Kommentare/View", "comments_per_view", lambda x: fpct(x, 3), "comments_per_view"),
        ("Sends (Shares)/Reach", "sends_per_reach", lambda x: fpct(x, 2), "sends_per_reach"),
        ("Saves/Reach", "saves_per_reach", lambda x: fpct(x, 2), "saves_per_reach"),
        ("Profilbesuche/View", "profile_visits_per_view", lambda x: fpct(x, 2), "profile_visits_per_view"),
        ("Follow-Conversion (Follows/Profilbesuche)", "follow_conversion", fpct, "follow_conversion"),
        ("Long-Tail-Anteil (1 − views_24h/views_7d, Median)", "longtail", fpct, None),
        ("Link-Klicks (Σ)", "link_clicks", fnum, None),
        ("Klicks pro 1.000 Reach", "clicks_1k_reach", lambda x: fnum(x, 2), None),
        ("Umsatz (Σ, EUR)", "revenue", lambda x: fnum(x, 2), None),
        ("RPM (Umsatz/1.000 Views, EUR)", "rpm", lambda x: fnum(x, 3), None),
        ("EPC (Umsatz/Klick, EUR)", "epc", lambda x: fnum(x, 2), None),
    ]
    tab = []
    for lab, key, f, bkey in spec:
        cur = kc[key]
        prev = kp[key] if kp else NAN
        tab.append([lab, f(cur), f(prev) if kp else "–", delta(cur, prev) if kp else "–", band(cur, bkey) if bkey else ""])
    L += md_table(["KPI", week, prev_week or "Vorwoche", "Δ", "Band (Launch-Hypothese)"], tab)
    if share is None:
        L.append("")
        L.append("_Qualifizierte Reichweite: `--target-market-share` (Anteil Zielmärkte aus Konto-Insights) angeben._")
    L.append("")

    acct = {"f1k": pooled(rows, "followers_gained", "views_ref", 1000),
            "sends": nanmed([r["sends_pr"] for r in rows]), "watch": nanmed([r["watch_pct"] for r in rows])}
    L.append(f"## 2. Reels der Woche {week} (sortiert nach account_index)")
    L.append("")
    L.append(f"account_index = views_24h ÷ Median views_24h der letzten {ROLL_WINDOW} Reels "
             f"(bei < {ROLL_MIN} Vorgängern: Median aller Reels, markiert mit *).")
    L.append("")
    t = []
    for r in sorted(wk, key=lambda r: -(r["account_index"] if ok(r["account_index"]) else -1)):
        t.append([r["reel_id"], f"{r['ts']:%m-%d %H:%M}", r["series_id"] or "–", f"{r['hook_type']}/{r['style']}",
                  fnum(r["views_24h"]), fnum(r["account_index"], 2) + ("" if r["ai_base_rolling"] else "*"),
                  r["reel_class"], fnum(r["f1k"], 2), fpct(r["sends_pr"], 2), fpct(r["watch_pct"], 0), r["vpf_tier"],
                  reel_action(r, acct)])
    L += md_table(["Reel", "UTC", "Serie", "Hook/Stil", "views_24h", "Index", "Klasse", "F/1k", "Sends/Reach",
                   "Watch %", "VPF-Tier", "Aktion"], t)
    L.append("")

    lifts = factor_lifts(rows, LIFT_FACTORS, B, rng, min_n, raw=args.raw_lift)
    decisions, acct_f1k = decide_groups(rows, lifts, B, rng, min_n)
    L.append("## 3. Entscheidungen KEEP / ITERATE / SCALE / KILL (kumuliert, alle Wochen)")
    L.append("")
    L.append(f"Regeln (Abschnitt 4 in 15_kpi_framework.md): SCALE n≥{min_n}, Gruppen-Index ≥{SCALE_MEDIAN_AI}, "
             f"P(besser) ≥{P_DECIDE:.0%}, F/1k ≥{F1K_SCALE_MIN}× Konto · KILL n≥{min_n}, Gruppen-Index <{KILL_MEDIAN_AI}, "
             f"P(schlechter) ≥{P_DECIDE:.0%} und North-Star-Index <{KILL_NS_INDEX} · "
             f"ITERATE ab n≥{MIN_N_ITERATE} bei Diagnose · "
             f"Konto-F/1k: {fnum(acct_f1k, 2)}")
    L.append("")
    order = {"KILL": 0, "SCALE": 1, "ITERATE": 2, "KEEP": 3, "OFFEN": 4}
    t = [[d["decision"], d["field"], d["level"], d["n"], fnum(d["median_ai"], 2), fnum(d["f1k"], 2), fnum(d["ns_index"], 2),
          fpct(d["p_pos"], 0), d["why"]]
         for d in sorted(decisions, key=lambda d: (order[d["decision"]], d["field"], -d["n"]))]
    L += md_table(["Entscheidung", "Feld", "Wert", "n", "Gruppen-Index", "F/1k", "NS-Index", "P(besser)", "Begründung"], t)
    L.append("")
    L.append("_Gruppen-Index = Median account_index der Gruppe ÷ Median account_index aller Reels (neutralisiert den "
             "Wachstums-Bias des Rolling-Medians). NS-Index (North-Star-Index) = Gruppen-Index × (F/1k Gruppe ÷ F/1k Konto) "
             "≈ Follow-Beitrag je Reel relativ zum Kontoschnitt._")
    L.append("")

    L.append("## 4. Faktor-Lifts (kumuliert)")
    L.append("")
    L.append(("Lift = exp(Mittel log(1+views_24h) im Level − Mittel übrige Reels)" if args.raw_lift else
              "Lift = exp(Mittel trendbereinigtes log(views_24h) im Level − Mittel übrige Reels); trendbereinigt = "
              "log(views_24h) − log(Rolling-Median) = log(account_index), damit Kontowachstum nicht als Faktoreffekt erscheint "
              "(`--raw-lift` = unbereinigt)") + "; F/1k-Lift = gepoolte Follows/1.000 Views "
             "im Level ÷ übrige (+0,5 Pseudo-Follow). KI = 95 % Bootstrap (stratifiziert). q = Benjamini-Hochberg über alle "
             f"Levels mit n≥{min_n}. 'belegt' = KI ohne 0 und q<{FDR_Q}; 'Tendenz' = P(Richtung) ≥{P_DIRECTION:.0%}.")
    L.append("")
    show = [l for l in lifts if l["views"]["n"] >= args.show_min_n]
    t = []
    for l in sorted(show, key=lambda l: (l["factor"], -l["views"]["point"])):
        v, f = l["views"], l["f1k"]
        t.append([l["factor"], l["level"], v["n"], fnum(l["median_v24"]),
                  f"{fmul(math.exp(v['point']))} [{math.exp(v['lo']):.2f}–{math.exp(v['hi']):.2f}]",
                  fpct(v["p_pos"], 0), fnum(l["views_q"], 2), l["views_flag"],
                  fnum(f["rate"], 2) if f else "–",
                  f"{fmul(math.exp(f['point']))} [{math.exp(f['lo']):.2f}–{math.exp(f['hi']):.2f}]" if f else "–",
                  l["f1k_flag"]])
    if t:
        L += md_table(["Faktor", "Level", "n", "Median views_24h", "Lift Views [95%-KI]", "P(>0)", "q", "Flag Views",
                       "F/1k", "Lift F/1k [95%-KI]", "Flag F/1k"], t)
    else:
        L.append(f"_Keine Levels mit n≥{args.show_min_n}._")
    hidden = len(lifts) - len(show)
    if hidden:
        L.append("")
        L.append(f"_{hidden} weitere Levels mit n<{args.show_min_n} ausgeblendet (`--show-min-n 1` zeigt alle)._")
    L.append("")

    L.append("## 5. Regularisierte Regression (Ridge auf log(1+views_24h))")
    L.append("")
    reg = ridge_analysis(rows, B, rng)
    if "skipped" in reg:
        L.append(f"_Übersprungen: {reg['skipped']}_")
    else:
        L.append(f"n={reg['n']}, Terme={reg['p']}, λ={reg['lambda']:.3g} (LOO-CV), R² in-sample={reg['r2']:.2f}, "
                 f"R² LOO={reg['r2_loo']:.2f}. Effekte relativ zum häufigsten Level je Faktor (Referenz), "
                 "kontrolliert für Länge, Hashtags, Zeittrend, Followerstand. 90 %-Bootstrap-KI. Seltene Levels (n<2) = `_rare`.")
        if reg["n"] < 30:
            L.append("")
            L.append(f"> n={reg['n']} ist klein: Koeffizienten sind stark geschrumpft und nur Richtungshinweise.")
        L.append("")
        t = []
        for tm in reg["terms"]:
            sig = (tm["lo"] > 0 or tm["hi"] < 0) and tm["n"] >= min_n
            t.append([tm["term"], tm["ref"] or "–", tm["n"], fmul(math.exp(tm["beta"])),
                      f"{math.exp(tm['lo']):.2f}–{math.exp(tm['hi']):.2f}", "✔" if sig else ""])
        top = t[:8] + (t[-6:] if len(t) > 14 else t[8:])
        L += md_table(["Term", "Referenz", "n", "Effekt auf Views", "90%-KI", f"KI ohne 1 & n≥{min_n}"], top)
        if len(t) > 14:
            L.append(f"_(Top 8 und Bottom 6 von {len(t)} Termen)_")
        L.append("")
        if reg.get("ols"):
            L.append("statsmodels-OLS (HC3), Terme mit p<0,05: " + "; ".join(f"{n} ×{math.exp(b):.2f} (p={p:.3f})" for n, b, p in reg["ols"]))
        elif reg.get("ols_note"):
            L.append(f"_{reg['ols_note']}_")
        elif reg.get("ols_error"):
            L.append(f"_OLS-Gegencheck fehlgeschlagen: {reg['ols_error']}_")
    L.append("")

    tests = ab_tests(rows, B, rng)
    L.append("## 6. Laufende Tests (test_id × variant)")
    L.append("")
    if tests:
        t = [[x["test_id"], x["variant"] + (" (Kontrolle)" if x["control"] else ""), x["n"], fnum(x["median_v24"]),
              fnum(x["median_ai"], 2), fnum(x["f1k"], 2), fpct(x["p_better"], 0) if not x["control"] else "–"] for x in tests]
        L += md_table(["Test", "Variante", "n", "Median views_24h", "Median-Index", "F/1k", "P(besser als Kontrolle)"], t)
        L.append("")
        L.append(f"_Entscheiden erst ab n≥{min_n} je Variante; Kontrolle = Variante 'control' bzw. 'A', sonst alphabetisch erste. "
                 "P(besser) auf trendbereinigtem log(views_24h)._")
    else:
        L.append("_Keine test_id eingetragen._")
    L.append("")

    ts = thompson(rows, rng)
    L.append("## 7. Nächste Woche: Thompson Sampling (hook_type × style) und Testvorschläge")
    L.append("")
    if ts:
        L.append(f"Erfolg = account_index ≥ 1,0 und F/1k ≥ Median ({fnum(ts['f1k_med'], 2)}). Beta-Prior je Zelle aus "
                 f"den Randverteilungen (Stärke 2). Slots/Woche: {SLOTS_CHAMPION} Champion · {SLOTS_TS} Thompson · "
                 f"{SLOTS_EXPLORE} Exploration.")
        L.append("")
        t = [[c["hook_type"], c["style"], c["n"], c["wins"], fpct(c["post_mean"], 0), fpct(c["p_best"], 1),
              c["ts_slots"], "neu" if c["new"] else ""] for c in ts["cells"][:12]]
        L += md_table(["hook_type", "style", "n", "Erfolge", "Posterior-Mittel", "P(beste Zelle)", "TS-Slots", ""], t)
    else:
        L.append("_Keine Reels mit hook_type, style und views_24h._")
    L.append("")
    champs = [d for d in decisions if d["field"] == "series_id" and d["decision"] in ("SCALE", "KEEP")]
    champ = max(champs, key=lambda d: d["median_ai"] if ok(d["median_ai"]) else -1) if champs else None
    L.append(f"Champion-Slots ({SLOTS_CHAMPION}/Woche): " + (f"Serie `{champ['level']}` ({champ['decision']}, Gruppen-Index "
             f"{fnum(champ['median_ai'], 2)})" if champ else "noch keine Serie mit KEEP/SCALE → bis dahin Top-Zelle aus Thompson-Tabelle."))
    L.append("")
    for s in next_tests(decisions, lifts, ts, min_n):
        L.append(f"- {s}")
    L.append("")

    L.append("## 8. Eigene Perzentile (für Rekalibrierung der Launch-Bänder)")
    L.append("")
    if len(rows) >= RECALIBRATE_MIN_N:
        L.append(f"n={len(rows)} ≥ {RECALIBRATE_MIN_N}: Bänder neu setzen – schwach < P25 ≤ ok < P50 ≤ gut < P75 ≤ stark.")
    else:
        L.append(f"n={len(rows)} < {RECALIBRATE_MIN_N} (14 Tage × 3 Reels): noch nicht rekalibrieren, nur beobachten.")
    L.append("")
    L += md_table(["KPI", "n", "P25", "P50", "P75", "P90"], percentiles_block(rows))
    L.append("")

    L.append("## 9. Datenqualität")
    L.append("")
    n_ex = sum(1 for r in all_rows if r["is_example"])
    if n_ex and len(rows) != len(all_rows):
        L.append(f"- {n_ex} EXAMPLE-Zeilen ignoriert.")
    miss = []
    for k in ("views_24h", "views_7d", "reach", "followers_gained", "shares", "saves", "avg_watch_time",
              "non_follower_reach_pct", "followers_at_post", "length_sec"):
        m = sum(1 for r in rows if not ok(r[k]))
        if m:
            miss.append(f"{k}: {m}")
    L.append("- Fehlende Werte: " + (", ".join(miss) if miss else "keine"))
    for i in issues[:40]:
        L.append(f"- {i}")
    if len(issues) > 40:
        L.append(f"- … {len(issues) - 40} weitere Hinweise")
    return L


# ----------------------------------------------------------------------------------------------
# SQLite export
# ----------------------------------------------------------------------------------------------
def export_sqlite(rows, db_path):
    if not os.path.exists(SCHEMA_PATH):
        raise SystemExit(f"Schema fehlt: {SCHEMA_PATH}")
    con = sqlite3.connect(db_path)
    con.execute("PRAGMA foreign_keys = ON")
    if not con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='reels'").fetchone():
        con.executescript(open(SCHEMA_PATH, encoding="utf-8").read())

    def nz(x):
        if isinstance(x, str):
            return x or None
        return x if ok(x) else None

    def cat(k, v):  # values outside the codebook would violate the CHECK constraints -> NULL
        return v if (k not in ALLOWED or not v or v in ALLOWED[k]) else None

    skipped, nulled = [], 0

    static = ["pillar", "format", "hook_type", "hook_text", "visual_hook", "room", "building_type", "style", "landscape",
              "lighting", "location", "realism", "visual_quality", "camera", "length_sec", "n_scenes", "audio_type", "audio_name",
              "text_overlay", "caption_type", "caption_first_line", "cta_type", "hashtags_n", "ai_tool", "ai_label",
              "ad_disclosure", "notes"]
    cols = ["reel_id", "posted_at_utc", "followers_at_post", "series_id", "test_id", "variant_id", "is_trial_reel",
            "prompt_id"] + static
    for r in rows:
        variant_id = f"{r['test_id']}:{r['variant']}" if r["test_id"] and r["variant"] else None
        trial = 1 if r["is_trial_reel"] == "trial" else 0 if r["is_trial_reel"] == "regular" else None
        nulled += sum(1 for k in static if k in ALLOWED and r[k] and cat(k, r[k]) is None)
        vals = [r["reel_id"], r["ts"].strftime("%Y-%m-%dT%H:%M:%SZ"), nz(r["followers_at_post"]), nz(r["series_id"]),
                nz(r["test_id"]), variant_id, trial, nz(r["prompt_id"])] + [nz(cat(k, r[k])) for k in static]
        con.execute("SAVEPOINT reel")
        try:
            if r["series_id"]:
                con.execute("INSERT OR IGNORE INTO series(series_id, pillar, format) VALUES (?,?,?)",
                            (r["series_id"], nz(cat("pillar", r["pillar"])), nz(cat("format", r["format"]))))
            if r["test_id"]:
                con.execute("INSERT OR IGNORE INTO tests(test_id, status) VALUES (?, 'running')", (r["test_id"],))
            if variant_id:
                con.execute("INSERT OR IGNORE INTO variants(variant_id, test_id, label) VALUES (?,?,?)",
                            (variant_id, r["test_id"], r["variant"]))
            if r["prompt_id"]:
                con.execute("INSERT OR IGNORE INTO prompts(prompt_id, ai_tool) VALUES (?,?)", (r["prompt_id"], nz(r["ai_tool"])))
            con.execute(f"INSERT OR REPLACE INTO reels({','.join(cols)}) VALUES ({','.join('?' * len(cols))})", vals)
            insert_snapshots(con, r, nz)
            con.execute("RELEASE reel")
        except sqlite3.IntegrityError as e:
            con.execute("ROLLBACK TO reel")
            con.execute("RELEASE reel")
            skipped.append(f"{r['reel_id']}: {str(e).splitlines()[0]}")
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM v_reel_kpis").fetchone()[0]
    con.close()
    return n, skipped, nulled


def insert_snapshots(con, r, nz):
    """Flat CSV row -> snapshots at T+1h, 6h, 24h (views only) and T+7d (all cumulative metrics)."""
    stamp = lambda h: (r["ts"] + dt.timedelta(hours=h)).strftime("%Y-%m-%dT%H:%M:%SZ")  # noqa: E731
    for h, key in ((1, "views_1h"), (6, "views_6h"), (24, "views_24h")):
        if ok(r[key]):
            con.execute("INSERT OR REPLACE INTO daily_snapshots(reel_id, snapshot_at_utc, hours_since_post, source, views) "
                        "VALUES (?,?,?,?,?)", (r["reel_id"], stamp(h), h, "csv_import", r[key]))
    m7 = ["views_7d", "reach", "non_follower_reach_pct", "likes", "comments", "shares", "saves", "reposts",
          "followers_gained", "profile_visits", "avg_watch_time", "completion_rate", "skip_rate", "link_clicks", "revenue"]
    if any(ok(r[k]) for k in m7):
        sc = ["views" if k == "views_7d" else k for k in m7]
        con.execute(f"INSERT OR REPLACE INTO daily_snapshots(reel_id, snapshot_at_utc, hours_since_post, source, {','.join(sc)}) "
                    f"VALUES (?,?,?,?,{','.join('?' * len(sc))})",
                    [r["reel_id"], stamp(168), 168, "csv_import"] + [nz(r[k]) for k in m7])


# ----------------------------------------------------------------------------------------------
# simulated data (dry run)
# ----------------------------------------------------------------------------------------------
def simulate(n, seed):
    rng = np.random.default_rng(seed)
    hooks = {"curiosity": 0.5, "question": 0.0, "fantasy": 0.3, "pov": -0.3, "location": 0.2}
    styles = {"modern_luxury": 0.0, "futuristic": 0.6, "japandi": -0.2, "rustic_cozy": 0.3}
    formats = {"single_scene_ambience": 0.0, "transformation_morph": 0.4, "choice_compare": -0.1}
    series = {"S01_dream_bedrooms": ("luxury_room", "bedroom"), "S02_future_homes": ("future_arch", "exterior_facade"),
              "S03_cozy_rain": ("cozy_ambience", "living_room")}
    start = dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc)
    followers = 0.0
    out = []
    for i in range(n):
        day, slot = divmod(i, 3)
        ts = start + dt.timedelta(days=day, hours=(13, 17, 21)[slot], minutes=int(rng.integers(0, 10)))
        h = rng.choice(list(hooks))
        s = rng.choice(list(styles))
        f = rng.choice(list(formats))
        sid = rng.choice(list(series))
        pillar, room = series[sid]
        length = int(rng.choice([7, 9, 12, 15, 22]))
        mu = math.log(600) + 0.08 * day + hooks[h] + styles[s] + formats[f] + (0.3 if sid == "S02_future_homes" else 0)
        v24 = float(np.exp(mu + rng.normal(0, 1.2)))
        v7 = v24 * float(rng.uniform(1.1, 2.2))
        f_rate = 0.002 * math.exp(0.4 * (h == "curiosity") + 0.3 * (sid == "S02_future_homes") + rng.normal(0, 0.3))
        gained = float(rng.poisson(v7 * f_rate))
        reach = v7 * float(rng.uniform(0.75, 0.92))
        watch = length * float(np.clip(rng.normal(0.55 + 0.1 * (f == "single_scene_ambience"), 0.12), 0.1, 1.3))
        out.append({
            "reel_id": f"SIM_{i + 1:04d}", "date": ts.strftime("%Y-%m-%d"), "time_posted": ts.strftime("%H:%M"),
            "followers_at_post": round(followers), "pillar": pillar, "series_id": sid,
            "test_id": "T01_hook_type" if day < 14 else "T02_style", "variant": h if day < 14 else s,
            "is_trial_reel": 0, "format": f, "hook_type": h, "hook_text": "SIMULATED", "visual_hook": rng.choice(["view_reveal", "text_hook", "exterior_reveal"]),
            "room": room, "building_type": "villa", "style": s, "landscape": "none", "lighting": "golden_hour", "location": "none",
            "realism": rng.choice(["stylized_dreamy", "fantasy_impossible", "aspirational_realistic"]), "visual_quality": "high",
            "camera": rng.choice(["slow_push_in", "orbit", "fly_through"]), "length_sec": length, "n_scenes": int(rng.integers(1, 5)),
            "audio_type": rng.choice(["music_only", "music_plus_ambient"]), "audio_name": "SIMULATED",
            "text_overlay": "hook_only", "caption_type": "aspirational", "caption_first_line": "SIMULATED",
            "cta_type": rng.choice(["follow", "save_share", "none"]), "hashtags_n": int(rng.integers(0, 6)),
            "ai_tool": "sim_tool", "prompt_id": f"P{i + 1:04d}", "ai_label": 1, "ad_disclosure": "none",
            "views_1h": round(v24 * 0.12), "views_6h": round(v24 * 0.45), "views_24h": round(v24), "views_7d": round(v7),
            "reach": round(reach), "non_follower_reach_pct": round(float(np.clip(97 - followers / 200, 55, 99)), 1),
            "likes": round(v7 * float(rng.uniform(0.015, 0.05))), "comments": round(v7 * float(rng.uniform(0.0002, 0.001))),
            "shares": round(reach * float(rng.uniform(0.003, 0.02))), "saves": round(reach * float(rng.uniform(0.003, 0.02))),
            "reposts": 0, "followers_gained": gained, "profile_visits": round(gained * float(rng.uniform(3, 8))),
            "avg_watch_time": round(watch, 1), "completion_rate": round(float(np.clip(watch / length - 0.25, 0.05, 0.9)), 2),
            "skip_rate": round(float(rng.uniform(0.25, 0.55)), 2), "link_clicks": 0, "revenue": 0, "notes": "SIMULIERT",
        })
        followers += gained
    return out


# ----------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Wochenanalyse der Winner-Datenbank (Instagram-Reels).")
    ap.add_argument("csv", nargs="?", help="CSV im Format data/winner_database_template.csv")
    ap.add_argument("--week", help="ISO-Woche YYYY-Www (Standard: letzte Woche mit Daten)")
    ap.add_argument("--min-n", type=int, default=MIN_N, help=f"Mindest-n je Gruppe für Flags/Entscheidungen (Standard {MIN_N})")
    ap.add_argument("--show-min-n", type=int, default=MIN_N_ITERATE, help="Levels in der Lift-Tabelle ab diesem n zeigen")
    ap.add_argument("--bootstrap", type=int, default=2000, help="Bootstrap-Stichproben (Standard 2000)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--raw-lift", action="store_true", help="Lift auf unbereinigtem log(1+views_24h) statt log(account_index)")
    ap.add_argument("--include-examples", action="store_true", help="EXAMPLE-Zeilen auch bei echten Daten behalten")
    ap.add_argument("--target-market-share", type=float, default=None,
                    help="Anteil Zielmärkte (0–1) an der Nicht-Follower-Reichweite, aus Konto-Insights")
    ap.add_argument("--out", help="Report zusätzlich als Markdown-Datei speichern")
    ap.add_argument("--to-sqlite", help="Reels zusätzlich in eine SQLite-DB (Schema data/winner_database_schema.sql) schreiben")
    ap.add_argument("--demo", type=int, metavar="N", help="N simulierte Reels erzeugen und analysieren (Probelauf)")
    ap.add_argument("--demo-csv", help="mit --demo: simulierte Daten als CSV speichern")
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)

    if args.demo:
        sim = simulate(args.demo, args.seed)
        raw = [{k: ("" if v is None else str(v)) for k, v in row.items()} for row in sim]
        if args.demo_csv:
            with open(args.demo_csv, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=FIELDS)
                w.writeheader()
                w.writerows(raw)
        delim, label = ",", f"SIMULATION n={args.demo}"
    elif args.csv:
        raw, delim = load_csv(args.csv)
        label = os.path.basename(args.csv)
    else:
        ap.error("CSV-Pfad oder --demo N angeben")

    all_rows, issues = prepare(raw, delim)
    if not all_rows:
        print("Keine auswertbaren Zeilen.")
        for i in issues:
            print("-", i)
        return 1
    real = [r for r in all_rows if not r["is_example"]]
    rows = all_rows if (args.include_examples or not real) else real
    rows = derive(rows)
    report = "\n".join(build_report(rows, all_rows, issues, args, rng, label))
    print(report)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report + "\n")
    if args.to_sqlite:
        n, skipped, nulled = export_sqlite(rows, args.to_sqlite)
        print(f"\nSQLite: {n} Reels in v_reel_kpis ({args.to_sqlite})"
              + (f"; {nulled} Codebook-fremde Werte als NULL gespeichert" if nulled else ""))
        for msg in skipped:
            print(f"SQLite: übersprungen – {msg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
