#!/usr/bin/env python3
"""Weekly competitor & trend monitor (Part 33, see 17_competitor_monitor.md).

Reads ONE week of raw public data in exactly the format of this research and writes a German markdown report
plus machine-readable tables. It never fetches anything itself.

    python3 scripts/monitor/monitor_weekly.py data/monitor/2026-W40 --prev data/monitor/2026-W39
    python3 scripts/monitor/monitor_weekly.py data/monitor/2026-W40 --prev data/raw        # 1st run: research baseline
    python3 scripts/monitor/monitor_weekly.py data/raw --out-dir data/monitor/2026-W39_baseline   # test on research data
    python3 scripts/monitor/monitor_weekly.py data/monitor/2026-W40 --todo   # only list embed lookups still needed
    python3 scripts/monitor/monitor_weekly.py data/monitor/2026-W40 --dump-captions -1   # caption chunks for coding agents

Week folder layout (files may also sit directly in the folder):
    topics/batch_*.json        topic-page sweep   {"batch","fetched_at","topics":[{"slug","slug_used","status",
                               "reels":[{"handle","shortcode","views_text","caption"[,"likes_text"]}]}]}
    accounts/followers_*.json  embed lookups      {"fetched_at","accounts":[{"handle","handle_shown","shortcode","status",
                               "followers_text","posts_text","likes_text","comments_text",...}]}
    reels/*.json   (optional)  codebook-coded reels, same format as data/raw/reels/cover_*.json
    competitors/media_*.json (optional, official API mode) {"handle","followers_count","media_count",
                               "media":[{"permalink"|"shortcode","timestamp","like_count","comments_count","view_count","caption"}]}
    run_meta.json  (optional)  {"week","run_started_utc","collection_mode","failed_urls":[...]}

Outputs (into --out-dir, default = the week folder):
    report.md, alerts.json, monitor_reels.csv, monitor_topics.csv, monitor_segments.csv, monitor_competitors.csv,
    inspiration_candidates.csv, watchlist_competitors_next.csv        (--todo: embed_todo.json only)

Metrics as in the research (scripts/analyze.py): views = rounded play count on the public topic page;
topic_index = views / median views of the same topic page this week; vpf = views / followers (embed, rounded);
tiers by vpf: NORMAL <0.5 | GOOD 0.5-2 | VERY_GOOD 2-5 | VIRAL 5-20 | EXTREME_OUTLIER >=20.
All comparisons are descriptive. Week-over-week comparisons only use topics swept successfully in BOTH weeks.
Standard library only (no pandas/scipy needed).
"""
import argparse
import csv
import datetime as dt
import glob
import json
import math
import os
import re
import statistics
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)
ROOT = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)
from parse_topics import parse_views  # noqa: E402  (same number parser as the research)
from shortcode_time import shortcode_to_datetime  # noqa: E402
from topic_groups import topic_group  # noqa: E402

DEFAULT_WL_TOPICS = os.path.join(HERE, "watchlist_topics.csv")
DEFAULT_WL_COMP = os.path.join(HERE, "watchlist_competitors.csv")
UTC = dt.timezone.utc
WEEK_DIR_RX = re.compile(r"^\d{4}-W?\d{2}")

# ----------------------------------------------------------------------------------------------------------------
# number helpers
# ----------------------------------------------------------------------------------------------------------------


def parse_count(text):
    """'547K followers' -> 547000, '2,727 posts' -> 2727, '9,276 likes' -> 9276 (as scripts/parse_accounts.py)."""
    if text is None:
        return None
    if isinstance(text, (int, float)):
        return int(text)
    t = re.sub(r"(?i)(followers?|posts?|likes?|comments?|views?|plays?|view all)", "", str(text)).strip()
    return parse_views(t)


def rounding_step(text):
    """Resolution of a displayed count: '547K' -> 1000, '1.2M' -> 100000, '2M' -> 1000000, '2,727' -> 1."""
    if text is None:
        return None
    if isinstance(text, (int, float)):
        return 1
    t = re.sub(r"(?i)(followers?|posts?|likes?|comments?)", "", str(text)).strip().replace(" ", "")
    m = re.fullmatch(r"(?i)([\d.,]+)([KMB])?", t)
    if not m:
        return None
    num, suf = m.group(1), (m.group(2) or "").upper()
    if not suf:
        return 1
    if num.count(",") == 1 and "." not in num:
        num = num.replace(",", ".")
    dec = len(num.split(".")[1]) if "." in num else 0
    return int({"K": 1e3, "M": 1e6, "B": 1e9}[suf] / (10 ** dec))


def tier(vpf):
    if vpf is None:
        return None
    if vpf < 0.5:
        return "1_NORMAL"
    if vpf < 2:
        return "2_GOOD"
    if vpf < 5:
        return "3_VERY_GOOD"
    if vpf < 20:
        return "4_VIRAL"
    return "5_EXTREME_OUTLIER"


def de(x, d=1):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    s = f"{x:,.{d}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def de_count(v):
    if v is None:
        return "–"
    if v >= 1e6:
        return f"{de(v / 1e6, 1)} Mio."
    if v >= 1e4:
        return f"{de(v / 1e3, 0)} Tsd."
    return de(v, 0)


def pct(x, d=1):
    return "–" if x is None else f"{de(100 * x, d)} %"


def median(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


# ----------------------------------------------------------------------------------------------------------------
# statistics (descriptive guards only, no causal claims)
# ----------------------------------------------------------------------------------------------------------------


def _logc(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def fisher_two_sided(a, b, c, d):
    """Fisher exact test for [[a, b], [c, d]] (a = segment in week 1, b = rest week 1, c/d = week 2)."""
    r1, c1, n = a + b, a + c, a + b + c + d
    if n == 0 or r1 == 0 or r1 == n or c1 == 0 or c1 == n:
        return 1.0
    lo, hi = max(0, c1 - (n - r1)), min(r1, c1)
    denom = _logc(n, c1)
    probs = {k: math.exp(_logc(r1, k) + _logc(n - r1, c1 - k) - denom) for k in range(lo, hi + 1)}
    p_obs = probs[a]
    return min(1.0, sum(p for p in probs.values() if p <= p_obs * (1 + 1e-7)))


def bh_qvalues(pvals):
    """Benjamini-Hochberg q-values (same order as input); guards against many simultaneous comparisons."""
    n = len(pvals)
    order = sorted(range(n), key=lambda i: pvals[i])
    q, prev = [0.0] * n, 1.0
    for rank in range(n, 0, -1):
        i = order[rank - 1]
        prev = min(prev, pvals[i] * n / rank)
        q[i] = prev
    return q


def mann_whitney(x, y):
    """Two-sided Mann-Whitney U, normal approximation with tie correction. Returns (U_x, p)."""
    n1, n2 = len(x), len(y)
    if n1 == 0 or n2 == 0:
        return None, None
    allv = sorted([(v, 0) for v in x] + [(v, 1) for v in y])
    ranks, i, ties = [0.0] * len(allv), 0, 0.0
    while i < len(allv):
        j = i
        while j + 1 < len(allv) and allv[j + 1][0] == allv[i][0]:
            j += 1
        r = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[k] = r
        t = j - i + 1
        ties += t ** 3 - t
        i = j + 1
    r1 = sum(r for r, (_, g) in zip(ranks, allv) if g == 0)
    u1 = r1 - n1 * (n1 + 1) / 2
    n = n1 + n2
    sd = math.sqrt(n1 * n2 / 12 * ((n + 1) - ties / (n * (n - 1)))) if n > 1 else 0
    if sd == 0:
        return u1, 1.0
    z = (u1 - n1 * n2 / 2) / sd
    return u1, math.erfc(abs(z) / math.sqrt(2))


# ----------------------------------------------------------------------------------------------------------------
# segment rules (keyword/heuristic -> identical method every week; codebook codes only for validation/display)
# ----------------------------------------------------------------------------------------------------------------

ROOM_KW = [
    ("bedroom", r"bed ?rooms?|master suite|\bbeds?\b"), ("bathroom", r"bath ?rooms?|\bbath\b|bathtub|shower|\bspa\b"),
    ("kitchen", r"kitchens?"), ("closet", r"closet|wardrobe|dressing room"), ("living_room", r"living ?rooms?|lounge"),
    ("dining", r"dining"), ("pool", r"\bpools?\b"), ("home_theater", r"home ?theat|cinema"),
    ("office_library", r"office|library|study room"),
    ("whole_home", r"\bhouses?\b|\bhomes?\b|villa|mansion|penthouse|cabin|chalet|treehouse|bunker|facade|architecture|apartment"),
]
STYLE_KW = [
    ("tropical", r"tropical|jungle|bali\b|tulum|\bpalms?\b"), ("japandi", r"japandi|wabi|\bzen\b|japanese"),
    ("scandinavian", r"scandi|nordic|hygge"), ("mediterranean", r"mediterran|santorini|greek|amalfi|mykonos|ibiza"),
    ("futuristic", r"futur|2050|sci-?fi|cyberpunk|parametric|spaceship"), ("brutalist", r"brutalis|concrete"),
    ("biophilic", r"biophil|organic modern|greenery"), ("cozy_rustic", r"cozy|cosy|rustic|cabin|fireplace|chalet"),
    ("dark_luxury", r"dark (?:luxury|academia|interior|moody)|moody|black marble"), ("minimalist", r"minimal"),
    ("art_deco", r"art ?deco"), ("classical", r"neoclassic|classic|baroque|palace|victorian"),
    ("industrial", r"industrial|\bloft"), ("modern_luxury", r"luxur|modern|elegan"),
]
SETTING_KW = [
    ("underwater", r"underwater"), ("ocean_beach", r"ocean|beach|sea ?view|seaside|coast|overwater|maldiv"),
    ("mountain_snow", r"mountain|alps|alpine|snow|winter|\bski"), ("rain", r"\brain|rainy|storm|thunder"),
    ("forest", r"forest|woods|treehouse"), ("desert", r"desert|dune"), ("jungle", r"jungle|rainforest"),
    ("cliff", r"cliff"), ("lake_river", r"\blake|river|waterfall"),
    ("city_skyline", r"skyline|city view|new york|manhattan|dubai"),
]
HOOK_RULES = [
    ("pov", r"^\W*pov\b"),
    ("choice", r"which (?:one|room|house|home|villa|bedroom|kitchen|bathroom|design|style|view|would you)|pick (?:one|your)"
               r"|choose (?:one|your)|\b1 or 2\b|one or two|this or that|\b[1-9] ?(?:,|or) ?[1-9]\b.*\?"),
    ("money", r"\$|€|£|\busd\b|\bmillion|\bbillion|\bprice|\bcost|\bworth\b|\bbudget"),
    ("instructional", r"^\W*(?:how to|how i|tips?\b|\d+ (?:tips|ideas|ways|mistakes|rules)|guide\b|step)"),
    ("promotional", r"link in (?:my )?bio|in (?:my )?bio\b|shop now|order (?:now|your)|book now|available (?:now|at|on)|dm (?:us|me)"
                    r"|use code|discount|% off|\bsale\b|contact us|whatsapp|for (?:sale|rent)|our (?:recent|latest|new) (?:project|design)"
                    r"|for our client|\bcourse\b|designed (?:&|and) built by|☎|📞"),
    ("curiosity", r"wait (?:for|till|until)|till the end|until the end|won'?t believe|nobody|no one|secret|the reason"
                  r"|here'?s why|this is why|didn'?t expect|plot twist|\bguess\b|you need to see|never seen|what happens"),
    ("contrarian", r"unpopular opinion|stop (?:doing|buying|using)|overrated|don'?t (?:buy|do)|\bmyth"),
    ("question", r"\?\s*$|^\W*(?:would|could|can|do|does|did|is|are|what|where|who|how|why|should)\b"),
    ("status", r"billionaire|millionaire|\brich\b|\b1 ?%|\belite\b|wealthy"),
    ("fantasy", r"imagine|fantasy|fairy|magical|another world|impossible|surreal|if you could"),
    ("location", r"📍|\b(?:dubai|bali|maldives|monaco|swiss|switzerland|santorini|mykonos|ibiza|tulum|lake como|amalfi|positano"
                 r"|malibu|aspen|tokyo|kyoto|london|paris|new york|miami|marrakech|norway|iceland|lapland|bora bora|skardu"
                 r"|los angeles|beverly hills|mallorca|marbella|tuscany|italy|greece|mexico|thailand|phuket)\b"),
    ("aspirational", r"dream|goals|living|\blife\b|would live|sanctuary|escape|paradise|vibes|\bmood|peace|serenity|perfect"),
]
CODE_ROOM = {"bedroom": "bedroom", "hotel_room": "bedroom", "bathroom": "bathroom", "spa": "bathroom", "kitchen": "kitchen",
             "closet": "closet", "living_room": "living_room", "dining": "dining", "pool": "pool",
             "home_theater": "home_theater", "office": "office_library", "exterior_facade": "whole_home"}
CODE_STYLE = {"tropical": "tropical", "japandi": "japandi", "scandinavian": "scandinavian", "mediterranean": "mediterranean",
              "futuristic": "futuristic", "cyberpunk": "futuristic", "brutalist": "brutalist", "biophilic": "biophilic",
              "organic_modern": "biophilic", "rustic_cozy": "cozy_rustic", "dark_luxury": "dark_luxury",
              "minimalist": "minimalist", "art_deco": "art_deco", "classical_luxury": "classical", "neoclassical": "classical",
              "industrial": "industrial", "modern_luxury": "modern_luxury", "warm_luxury": "modern_luxury"}
SEG_DIMS = [("topic_group", "Topic-Gruppe"), ("kw_room", "Raum (Keyword)"), ("kw_style", "Stil (Keyword)"),
            ("kw_setting", "Setting (Keyword)"), ("kw_combo", "Stil × Raum (Keyword)"), ("hook", "Hook-Typ")]
# heuristic hook classes with high precision against the codebook labels of the research sample (see report section 8);
# with heuristic hooks, pairwise hook alerts are only raised between these classes
HOOK_RELIABLE = {"pov", "choice", "question", "money"}
AI_RX = re.compile(r"(?i)#ai\b|#aiart|\bai[- ]generated|\bmade with ai|midjourney|\bai art\b|\bai design|#aiinterior|\bsora\b|\bkling\b|\brunway\b")


def first_line(caption):
    c = (caption or "").strip()
    if not c:
        return ""
    return re.split(r"(?<=[.!?])\s|\n", c, maxsplit=1)[0][:120].strip()


def classify(text, rules, default="none"):
    t = (text or "").lower()
    for label, rx in rules:
        if re.search(rx, t):
            return label
    return default


def hook_heuristic(caption):
    fl = first_line(caption)
    if not fl:
        return "none"
    return classify(fl, HOOK_RULES, default="descriptive")


# ----------------------------------------------------------------------------------------------------------------
# loading one week
# ----------------------------------------------------------------------------------------------------------------


def _files(folder, subs, pattern):
    out = set()
    for d in [folder] + [os.path.join(folder, s) for s in subs]:
        out.update(glob.glob(os.path.join(d, pattern)))
    return sorted(out)


def _load_json(path, issues):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        issues.append(f"Ungültige Datei übersprungen: `{os.path.relpath(path, ROOT)}` ({e.__class__.__name__})")
        return None


def _date(s):
    if not s:
        return None
    s = re.sub(r"([+-]\d{2})(\d{2})$", r"\1:\2", str(s).strip())  # Graph API style '+0000' -> '+00:00'
    try:
        d = dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=UTC)


def iso_week_label(d):
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


class Week:
    def __init__(self, folder, label=None):
        self.folder = os.path.abspath(folder)
        self.issues = []
        self.topic_status = []        # one dict per topic entry
        self.apps = []                # one dict per reel appearance on a topic page
        self.accounts = {}            # handle -> account record (followers etc.)
        self.embeds = {}              # shortcode -> per-reel embed record (likes/comments/followers)
        self.codes = {}               # shortcode -> codebook dict
        self.comp_media = []          # official-API media rows
        self.fetched = set()
        self.meta = {}
        self._load()
        self.run_time = _date(self.meta.get("run_started_utc")) or (
            min(_date(d) for d in self.fetched if _date(d)) if any(_date(d) for d in self.fetched) else None)
        base = os.path.basename(self.folder.rstrip("/"))
        if label:
            self.label = label
        elif self.meta.get("week"):
            self.label = self.meta["week"]
        elif WEEK_DIR_RX.match(base):
            self.label = base
        else:
            self.label = f"{iso_week_label(self.run_time)} ({os.path.relpath(self.folder, ROOT)})" if self.run_time else base

    # -- raw files ---------------------------------------------------------------------------------------------
    def _load(self):
        mp = os.path.join(self.folder, "run_meta.json")
        if os.path.exists(mp):
            self.meta = _load_json(mp, self.issues) or {}
        for path in _files(self.folder, ["topics"], "batch_*.json"):
            data = _load_json(path, self.issues)
            if not data:
                continue
            if data.get("fetched_at"):
                self.fetched.add(data["fetched_at"])
            for t in data.get("topics", []):
                slug = (t.get("slug_used") or t.get("slug") or "").strip().strip("/")
                reels = t.get("reels") or []
                self.topic_status.append({"slug": slug, "requested": t.get("slug"), "status": t.get("status"),
                                          "n_reels": len(reels), "batch": data.get("batch") or os.path.basename(path),
                                          "total_reels_label": t.get("total_reels_label")})
                if t.get("status") not in (None, "ok") or not slug:
                    continue
                for pos, r in enumerate(reels, 1):
                    sc = (r.get("shortcode") or "").strip().strip("/")
                    if not sc or sc.upper() == "NA":
                        continue
                    self.apps.append({
                        "topic": slug, "position": pos, "shortcode": sc,
                        "handle": (r.get("handle") or "").lower().lstrip("@").strip(),
                        "views": parse_views(r.get("views_text")), "likes": parse_count(r.get("likes_text")),
                        "caption": (r.get("caption") or "").replace("\n", " ").strip(),
                    })
        for path in _files(self.folder, ["accounts"], "followers_*.json"):
            data = _load_json(path, self.issues)
            if not data:
                continue
            if data.get("fetched_at"):
                self.fetched.add(data["fetched_at"])
            for a in data.get("accounts", []):
                self._add_embed(a, data.get("fetched_at"), "followers_json")
        for path in _files(self.folder, ["reels", "codes"], "*.json"):
            data = _load_json(path, self.issues)
            if not isinstance(data, dict) or not isinstance(data.get("reels"), list):
                continue
            for r in data["reels"]:
                if not isinstance(r, dict):
                    continue
                self._add_embed(r, data.get("coded_at"), "coded_json")
                code = r.get("code")
                sc = (r.get("shortcode") or "").strip()
                if isinstance(code, dict) and sc:
                    ok = r.get("visual_status", r.get("code_status")) == "ok"
                    if sc not in self.codes or (ok and not self.codes[sc].get("_ok")):
                        self.codes[sc] = {**code, "_ok": ok}
        for path in _files(self.folder, ["competitors"], "media_*.json"):
            data = _load_json(path, self.issues)
            if not data:
                continue
            for acc in data if isinstance(data, list) else [data]:
                self._add_api_account(acc)
        # a topic swept twice (retry batch) must not count its reels twice
        seen, apps = set(), []
        for a in self.apps:
            if (a["topic"], a["shortcode"]) not in seen:
                seen.add((a["topic"], a["shortcode"]))
                apps.append(a)
        if len(apps) < len(self.apps):
            self.issues.append(f"{len(self.apps) - len(apps)} doppelte Topic-Reel-Einträge (Mehrfachabruf) ignoriert.")
        self.apps = apps

    def slug_status(self):
        """Unique requested slug -> 'ok' if any attempt succeeded with reels, else the last status seen."""
        st = {}
        for t in self.topic_status:
            key = t["slug"] or t["requested"]
            ok = t["status"] == "ok" and t["n_reels"] > 0
            if ok or st.get(key) != "ok":
                st[key] = "ok" if ok else (t["status"] or "unknown")
            if t["requested"] and t["requested"] != key and ok:
                st.pop(t["requested"], None)  # slug redirected to slug_used and succeeded
        return st

    def _add_embed(self, a, fetched_at, src):
        if a.get("status", a.get("meta_status", "ok")) != "ok":
            return
        h = (a.get("handle_shown") or a.get("handle") or "").lower().lstrip("@").strip()
        sc = (a.get("shortcode") or "").strip().strip("/")
        fol = parse_count(a.get("followers_text"))
        posts = parse_count(a.get("posts_text"))
        if h and fol:
            prev = self.accounts.get(h)
            if prev is None or (src == "followers_json" and prev["source"] != "followers_json"):
                self.accounts[h] = {"handle": h, "followers": fol, "followers_text": a.get("followers_text"),
                                    "followers_step": rounding_step(a.get("followers_text")), "posts": posts,
                                    "posts_text": a.get("posts_text"), "shortcode": sc, "source": src,
                                    "fetched_at": fetched_at, "handle_expected": (a.get("handle") or "").lower()}
        if sc:
            rec = self.embeds.get(sc, {})
            for k, v in (("handle", h), ("followers", fol), ("posts", posts), ("likes", parse_count(a.get("likes_text"))),
                         ("comments", parse_count(a.get("comments_text"))), ("caption", a.get("caption") or a.get("caption_200"))):
                if v is not None and rec.get(k) is None:
                    rec[k] = v
            self.embeds[sc] = rec

    def _add_api_account(self, acc):
        h = (acc.get("handle") or acc.get("username") or "").lower().lstrip("@")
        if not h:
            return
        if acc.get("followers_count") is not None:
            self.accounts[h] = {"handle": h, "followers": int(acc["followers_count"]), "followers_text": str(acc["followers_count"]),
                                "followers_step": 1, "posts": acc.get("media_count"), "posts_text": str(acc.get("media_count")),
                                "shortcode": "", "source": "official_api", "fetched_at": acc.get("fetched_at")}
        for m in acc.get("media", []):
            sc = m.get("shortcode") or (re.search(r"/(?:reel|p)/([A-Za-z0-9_-]{6,})", m.get("permalink") or "") or [None, None])[1]
            if not sc:
                continue
            self.comp_media.append({"handle": h, "shortcode": sc, "timestamp": m.get("timestamp"),
                                    "views": m.get("view_count"), "likes": m.get("like_count"),
                                    "comments": m.get("comments_count"), "caption": m.get("caption") or ""})
            self.embeds.setdefault(sc, {}).update({k: v for k, v in (("handle", h), ("likes", m.get("like_count")),
                                                                        ("comments", m.get("comments_count"))) if v is not None})

    # -- derived -----------------------------------------------------------------------------------------------
    def ok_topics(self):
        return sorted(k for k, v in self.slug_status().items() if v == "ok")

    def topic_metrics(self):
        """Per topic page: metric (views, or likes if a page has no views, e.g. API hashtag mode), median, index."""
        by = defaultdict(list)
        for a in self.apps:
            by[a["topic"]].append(a)
        info = {}
        for slug, rows in by.items():
            has_v = sum(1 for r in rows if r["views"] is not None)
            has_l = sum(1 for r in rows if r["likes"] is not None)
            metric = "views" if has_v >= max(1, len(rows) / 2) or has_v >= has_l else "likes"
            vals = sorted(r[metric] for r in rows if r[metric] is not None)
            med = statistics.median(vals) if vals else None
            for r in rows:
                v = r[metric]
                r["metric"] = metric
                r["topic_median"] = med
                r["topic_index"] = (v / med) if (v is not None and med) else None
                r["topic_pct"] = ((sum(1 for x in vals if x < v) + (sum(1 for x in vals if x == v) + 1) / 2) / len(vals)
                                  if v is not None and vals else None)
            info[slug] = {"topic": slug, "metric": metric, "n": len(rows), "n_metric": len(vals), "median": med,
                          "max": max(vals) if vals else None, "group": topic_group(slug)[0]}
        return info


def build_reels(week, topics=None, cutoff=None, fallback_accounts=None):
    """Unique reels (optionally restricted to a topic set) with metrics and segments."""
    uniq = {}
    for a in week.apps:
        if topics is not None and a["topic"] not in topics:
            continue
        u = uniq.get(a["shortcode"])
        if u is None:
            u = uniq[a["shortcode"]] = {"shortcode": a["shortcode"], "handle": a["handle"], "views": a["views"],
                                        "likes_page": a["likes"], "caption": a["caption"], "topics": set(),
                                        "topic_index": a["topic_index"], "topic_pct": a["topic_pct"], "metric": a["metric"]}
        u["topics"].add(a["topic"])
        if not u["handle"] and a["handle"]:
            u["handle"] = a["handle"]
        for k in ("views", "topic_index", "topic_pct"):
            if a[k] is not None and (u[k] is None or a[k] > u[k]):
                u[k] = a[k]
        if len(a["caption"]) > len(u["caption"]):
            u["caption"] = a["caption"]
    out = []
    for u in uniq.values():
        sc = u["shortcode"]
        emb = week.embeds.get(sc, {})
        acc = week.accounts.get(u["handle"]) or {}
        acc_prev = (fallback_accounts or {}).get(u["handle"]) or {}
        posted = shortcode_to_datetime(sc)
        fol = emb.get("followers") or acc.get("followers") or acc_prev.get("followers")
        vpf = (u["views"] / fol) if (u["views"] is not None and fol) else None
        groups = sorted({topic_group(t) for t in u["topics"]}, key=lambda g: (g[1], g[0]))
        text = f"{u['caption']} {' '.join(t.replace('-', ' ') for t in sorted(u['topics']))}"
        room, style, setting = classify(text, ROOM_KW, "other"), classify(text, STYLE_KW, "other"), classify(text, SETTING_KW, "none")
        code = week.codes.get(sc) or {}
        row = {
            "shortcode": sc, "url": f"https://www.instagram.com/reel/{sc}/", "handle": u["handle"],
            "posted_at_utc": posted.isoformat() if posted else None, "_posted": posted,
            "is_new": bool(posted and cutoff and posted > cutoff),
            "age_days": round((week.run_time - posted).total_seconds() / 86400, 1) if (posted and week.run_time) else None,
            "views": u["views"], "metric": u["metric"], "topic_index": u["topic_index"], "topic_pct": u["topic_pct"],
            "in_top_quartile": bool(u["topic_pct"] is not None and u["topic_pct"] >= 0.75),
            "n_topics": len(u["topics"]), "topics": ";".join(sorted(u["topics"])),
            "topic_group": groups[0][0] if groups else "other",
            "followers": fol, "followers_source": ("embed_reel" if emb.get("followers") else "account_lookup" if acc.get("followers")
                                                   else "account_prev_week" if fol else None),
            "vpf": vpf, "tier": tier(vpf),
            "likes": emb.get("likes") if emb.get("likes") is not None else u["likes_page"], "comments": emb.get("comments"),
            "kw_room": room, "kw_style": style, "kw_setting": setting, "kw_combo": f"{style} × {room}",
            "hook_h": hook_heuristic(u["caption"]), "hook": None, "hook_source": None, "ai_disclosed_kw": bool(AI_RX.search(u["caption"] or "")),
            "caption_first_line": first_line(u["caption"]),
            "code_room": CODE_ROOM.get(code.get("room_primary"), "other") if code else None,
            "code_style": CODE_STYLE.get(code.get("style_primary"), "other") if code else None,
            "code_hook": code.get("caption_hook_category") if code else None,
            "code_production": code.get("production") if code else None,
            "code_realism": code.get("realism") if code else None,
            "code_visual_ok": bool(code.get("_ok")) if code else False,
        }
        row["likes_per_view"] = (row["likes"] / row["views"]) if (row["likes"] and row["views"] and row["metric"] == "views") else None
        out.append(row)
    return out


# ----------------------------------------------------------------------------------------------------------------
# analyses
# ----------------------------------------------------------------------------------------------------------------


def code_coverage(rows):
    return (sum(1 for r in rows if r["code_hook"]) / len(rows)) if rows else 0.0


def apply_hook_source(rows, use_code):
    """hook = codebook caption_hook_category where coded (else heuristic) if use_code, otherwise heuristic for all."""
    for r in rows:
        if use_code and r["code_hook"]:
            r["hook"], r["hook_source"] = r["code_hook"], "code"
        else:
            r["hook"], r["hook_source"] = r["hook_h"], "heuristic"


def segment_shares(cur, prev, args):
    """Share of top-quartile reels per segment value, this week vs previous week (same topics)."""
    rows = []
    tq_c = [r for r in cur if r["in_top_quartile"]]
    tq_p = [r for r in prev if r["in_top_quartile"]] if prev is not None else []
    overlap = (len({r["shortcode"] for r in tq_c} & {r["shortcode"] for r in tq_p}) / len(tq_c)) if (tq_c and tq_p) else None
    for dim, dim_label in SEG_DIMS:
        vals = Counter(r[dim] for r in cur) + Counter(r[dim] for r in prev or [])
        for v in vals:
            if v in ("none", "other", "other × other"):
                continue
            n_tq_c = sum(1 for r in tq_c if r[dim] == v)
            n_all_c = sum(1 for r in cur if r[dim] == v)
            share_c = n_tq_c / len(tq_c) if tq_c else None
            base_c = n_all_c / len(cur) if cur else None
            rec = {"dimension": dim, "dimension_label": dim_label, "value": v, "n_tq_cur": n_tq_c, "tq_cur": len(tq_c),
                   "share_tq_cur": share_c, "share_all_cur": base_c,
                   "lift_cur": (share_c / base_c) if (share_c is not None and base_c) else None,
                   "n_tq_prev": None, "tq_prev": None, "share_tq_prev": None, "delta_pp": None, "p_fisher": None, "q_bh": None,
                   "status": ""}
            if prev is not None and tq_p:
                n_tq_p = sum(1 for r in tq_p if r[dim] == v)
                share_p = n_tq_p / len(tq_p)
                rec.update({"n_tq_prev": n_tq_p, "tq_prev": len(tq_p), "share_tq_prev": share_p,
                            "delta_pp": 100 * (share_c - share_p) if share_c is not None else None})
                enough = len(tq_c) >= args.min_tq and len(tq_p) >= args.min_tq and max(n_tq_c, n_tq_p) >= args.min_seg
                if enough:
                    rec["p_fisher"] = fisher_two_sided(n_tq_p, len(tq_p) - n_tq_p, n_tq_c, len(tq_c) - n_tq_c)
                else:
                    rec["status"] = "n zu klein"
            rows.append(rec)
    tested = [r for r in rows if r["p_fisher"] is not None]
    for r, q in zip(tested, bh_qvalues([r["p_fisher"] for r in tested])):
        r["q_bh"] = q
        if abs(r["delta_pp"]) >= args.min_pp and q < args.max_q:
            r["status"] = "ALARM"
        elif abs(r["delta_pp"]) >= args.min_pp and r["p_fisher"] < 0.20:
            r["status"] = "beobachten"
    return rows, overlap


def hook_table(cur, prev, args, allowed=None):
    out, pairs = [], []
    by_c = defaultdict(list)
    for r in cur:
        if r["topic_index"] is not None:
            by_c[r["hook"]].append(r["topic_index"])
    by_p = defaultdict(list)
    for r in prev or []:
        if r["topic_index"] is not None:
            by_p[r["hook"]].append(r["topic_index"])
    for h in sorted(set(by_c) | set(by_p)):
        xs = by_c.get(h, [])
        out.append({"hook": h, "n": len(xs), "median_ti": median(xs),
                    "share_tq": (sum(1 for r in cur if r["hook"] == h and r["in_top_quartile"]) / len(xs)) if xs else None,
                    "n_prev": len(by_p.get(h, [])) if prev is not None else None,
                    "median_ti_prev": median(by_p.get(h, [])) if prev is not None else None,
                    "enough": len(xs) >= args.min_n})
    elig = [h for h in by_c if len(by_c[h]) >= args.min_n and h != "none" and (allowed is None or h in allowed)]
    for i, a in enumerate(elig):
        for b in elig[i + 1:]:
            _, p = mann_whitney(by_c[a], by_c[b])
            ma, mb = median(by_c[a]), median(by_c[b])
            if p is None or not ma or not mb:
                continue
            hi, lo = (a, b) if ma >= mb else (b, a)
            ratio = max(ma, mb) / min(ma, mb)
            pairs.append({"better": hi, "worse": lo, "median_better": max(ma, mb), "median_worse": min(ma, mb),
                          "n_better": len(by_c[hi]), "n_worse": len(by_c[lo]), "p": p, "ratio": ratio})
    for pr, q in zip(pairs, bh_qvalues([pr["p"] for pr in pairs])):
        pr["q_bh"] = q
    pairs.sort(key=lambda x: x["p"])
    return sorted(out, key=lambda x: -(x["median_ti"] or 0)), pairs


def topic_table(week_c, info_c, week_p, info_p, cur_reels, cutoff, prev_shortcodes):
    rows = []
    apps_by = defaultdict(list)
    for a in week_c.apps:
        apps_by[a["topic"]].append(a)
    status = week_c.slug_status()
    for slug in sorted(set(status) | set(info_c)):
        ic = info_c.get(slug)
        ip = (info_p or {}).get(slug)
        apps = apps_by.get(slug, [])
        n_fresh = sum(1 for a in apps if (shortcode_to_datetime(a["shortcode"]) or dt.datetime.min.replace(tzinfo=UTC)) > (cutoff or dt.datetime.max.replace(tzinfo=UTC)))
        n_newentry = sum(1 for a in apps if a["shortcode"] not in prev_shortcodes) if prev_shortcodes is not None else None
        rows.append({
            "topic": slug, "group": topic_group(slug)[0], "status": status.get(slug, "ok"), "metric": ic["metric"] if ic else None,
            "n": ic["n"] if ic else 0, "median": ic["median"] if ic else None, "max": ic["max"] if ic else None,
            "median_prev": ip["median"] if ip else None,
            "median_ratio": (ic["median"] / ip["median"]) if (ic and ip and ic["median"] and ip["median"] and ic["metric"] == ip["metric"]) else None,
            "n_fresh": n_fresh, "share_fresh": (n_fresh / len(apps)) if apps else None,
            "n_new_entries": n_newentry, "share_new_entries": (n_newentry / len(apps)) if (apps and n_newentry is not None) else None,
        })
    return rows


def competitor_media_table(week, cutoff):
    """Official-API mode: each competitor reel vs. the median views (else likes) of that account's returned media."""
    by = defaultdict(list)
    for m in week.comp_media:
        by[m["handle"]].append(m)
    rows = []
    for h, ms in by.items():
        metric = "views" if sum(1 for m in ms if m["views"] is not None) >= len(ms) / 2 else "likes"
        med = median([m[metric] for m in ms if m[metric] is not None])
        for m in ms:
            posted = _date(m["timestamp"]) or shortcode_to_datetime(m["shortcode"])
            v = m[metric]
            rows.append({"handle": h, "shortcode": m["shortcode"], "posted_at_utc": posted.isoformat() if posted else None,
                         "is_new": bool(posted and cutoff and posted > cutoff), "metric": metric, "value": v,
                         "account_median": med, "account_index": (v / med) if (v is not None and med) else None,
                         "likes": m["likes"], "comments": m["comments"], "n_media_returned": len(ms),
                         "caption_first_line": first_line(m["caption"]), "hook_h": hook_heuristic(m["caption"])})
    rows.sort(key=lambda r: (not r["is_new"], -(r["account_index"] or 0)))
    return rows


def load_watchlist(path):
    if not path or not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if str(r.get("active", "1")).strip() not in ("0", "false", "False")]


def history_series(root, exclude_folder=None):
    """handle -> [(label, run_time, followers, followers_text, step, posts)] from sibling week folders."""
    series = defaultdict(list)
    if not root or not os.path.isdir(root):
        return series
    for d in sorted(os.listdir(root)):
        full = os.path.join(root, d)
        if not os.path.isdir(full) or not WEEK_DIR_RX.match(d):
            continue
        if not _files(full, ["accounts"], "followers_*.json") and not _files(full, ["competitors"], "media_*.json"):
            continue
        w = Week(full)
        for h, a in w.accounts.items():
            series[h].append((w.label, w.run_time, a["followers"], a["followers_text"], a["followers_step"], a["posts"]))
    return series


def competitor_table(wl, week_c, week_p, cur_reels, series):
    rows = []
    by_handle = defaultdict(list)
    for r in cur_reels:
        by_handle[r["handle"]].append(r)
    days = ((week_c.run_time - week_p.run_time).total_seconds() / 86400) if (week_p and week_c.run_time and week_p.run_time) else None
    for c in wl:
        h = c["handle"].lower().lstrip("@")
        a = week_c.accounts.get(h) or {}
        ap = (week_p.accounts.get(h) if week_p else None) or {}
        reels = by_handle.get(h, [])
        fol, fol_p = a.get("followers"), ap.get("followers")
        step = max(a.get("followers_step") or 1, ap.get("followers_step") or 1)
        dfol = (fol - fol_p) if (fol and fol_p) else None
        detectable = dfol is not None and abs(dfol) > step
        posts, posts_p = a.get("posts"), ap.get("posts")
        dposts = (posts - posts_p) if (posts is not None and posts_p is not None) else None
        newest = max((r for r in reels if r["_posted"]), key=lambda r: r["_posted"], default=None)
        wl_last = _date(c.get("last_posted_utc"))
        ser = series.get(h, [])
        rows.append({
            "handle": h, "role": c.get("role"), "followers": fol, "followers_text": a.get("followers_text"),
            "followers_prev_text": ap.get("followers_text"), "delta_followers": dfol, "rounding_step": step,
            "delta_detectable": detectable,
            "growth_pct": (100 * dfol / fol_p) if (detectable and fol_p) else None,
            "posts": posts, "posts_prev": posts_p, "delta_posts": dposts,
            "posts_per_week": (dposts / days * 7) if (dposts is not None and days) else None,
            "reels_on_topic_pages": len(reels), "new_reels_on_topic_pages": sum(1 for r in reels if r["is_new"]),
            "best_topic_index": max((r["topic_index"] for r in reels if r["topic_index"] is not None), default=None),
            "best_tier": max((r["tier"] for r in reels if r["tier"]), default=None),
            "newest_shortcode": newest["shortcode"] if newest else None,
            "newest_posted": newest["posted_at_utc"] if newest else None,
            "watchlist_shortcode_outdated": bool(newest and wl_last and newest["_posted"] > wl_last),
            "embed_found": bool(a), "history": " → ".join(short(s[3]) for s in ser[-6:]) if ser else "",
            "baseline_followers": c.get("baseline_followers"), "baseline_posts": c.get("baseline_posts"),
        })
    return rows


# ----------------------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------------------


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join("" if x is None else str(x).replace("|", "/") for x in r) + " |")
    return "\n".join(out)


def short(text):
    if text is None or text == "":
        return "–"
    t = re.sub(r"(?i)\s*followers?", "", str(text)).strip()
    return de_count(int(t)) if t.isdigit() else t


def link(sc):
    return f"[{sc}](https://www.instagram.com/reel/{sc}/)"


def build_alerts(new_out, seg_rows, pairs, topics, comps, dq, overlap, args, hook_source):
    alerts = []
    for r in new_out:
        if r["tier"] in ("5_EXTREME_OUTLIER", "4_VIRAL"):
            extreme, strong_page = r["tier"].startswith("5"), (r["topic_index"] or 0) >= 1
            small = (r["followers"] or 0) < args.min_followers
            prio = 1 if (extreme and strong_page and not small) else 2 if (strong_page or extreme) and not small else 3
            eng = f", {de_count(r['likes'])} Likes / {de_count(r['comments'])} Kommentare" if r["likes"] is not None else ""
            alerts.append({"priority": prio, "type": "new_outlier", "shortcode": r["shortcode"], "handle": r["handle"],
                           "text": f"Neuer {'EXTREME-' if extreme else 'VIRAL-'}Ausreißer {link(r['shortcode'])} von @{r['handle']} "
                                   f"({r['topics'].split(';')[0]}): {de_count(r['views'])} Views bei {de_count(r['followers'])} Followern "
                                   f"(vpf {de(r['vpf'], 1)}×, topic_index {de(r['topic_index'], 1)}{eng}), Hook „{r['caption_first_line'][:60]}“"
                                   + (f". Achtung: Account < {de_count(args.min_followers)} Follower, vpf wenig aussagekräftig." if small else ".")})
        elif r["followers"] is None and (r["topic_index"] or 0) >= 5:
            alerts.append({"priority": 3, "type": "new_outlier_no_followers", "shortcode": r["shortcode"],
                           "text": f"Neues Reel {link(r['shortcode'])} (@{r['handle']}) mit topic_index {de(r['topic_index'], 1)}, "
                                   f"Follower unbekannt → Embed nachschlagen (`--todo`)."})
    for s in seg_rows:
        if s["status"] == "ALARM":
            direction = "gestiegen" if s["delta_pp"] > 0 else "gefallen"
            alerts.append({"priority": 2, "type": "segment_shift", "dimension": s["dimension"], "value": s["value"],
                           "text": f"{s['dimension_label']} **{s['value']}**: Anteil an Top-Quartil-Reels von {pct(s['share_tq_prev'])} auf "
                                   f"{pct(s['share_tq_cur'])} {direction} (n = {s['n_tq_prev']}/{s['tq_prev']} → {s['n_tq_cur']}/{s['tq_cur']}; "
                                   f"Fisher p = {de(s['p_fisher'], 3)}, BH-q = {de(s['q_bh'], 3)}; TQ-Überlappung {pct(overlap, 0)}). Beschreibend, keine Ursache belegt."})
    for p in [p for p in pairs if p["q_bh"] < args.max_q and p["ratio"] >= 1.5][:3]:
        alerts.append({"priority": 3, "type": "hook_compare", "better": p["better"], "worse": p["worse"],
                       "text": f"Hook-Typ **{p['better']}** liegt diese Woche vor **{p['worse']}**: Median topic_index "
                               f"{de(p['median_better'], 2)} vs. {de(p['median_worse'], 2)} (n = {p['n_better']} / {p['n_worse']}; "
                               f"Mann-Whitney p = {de(p['p'], 3)}, BH-q = {de(p['q_bh'], 3)} über {len(pairs)} Paare; Hook-Quelle: {hook_source}). Korrelation, kein Test."})
    for t in topics:
        if t["median_ratio"] is not None and t["n"] >= args.min_n and (t["median_ratio"] >= 2 or t["median_ratio"] <= 0.5):
            alerts.append({"priority": 4, "type": "topic_shift", "topic": t["topic"],
                           "text": f"Topic `{t['topic']}`: Median-{t['metric']} {de_count(t['median_prev'])} → {de_count(t['median'])} "
                                   f"(×{de(t['median_ratio'], 2)}; n = {t['n']}). Einzelne Seite mit ~12 Reels, nur Hinweis."})
    for c in comps:
        if c["growth_pct"] is not None and c["growth_pct"] >= args.min_growth:
            alerts.append({"priority": 3, "type": "competitor_growth", "handle": c["handle"],
                           "text": f"@{c['handle']} ({c['role']}): Follower {short(c['followers_prev_text'])} → {short(c['followers_text'])} "
                                   f"(+{de(c['growth_pct'], 1)} %, über Rundungsgrenze {de_count(c['rounding_step'])})."})
        if c["posts_per_week"] is not None and c["posts_per_week"] >= args.min_posts_week:
            alerts.append({"priority": 4, "type": "competitor_cadence", "handle": c["handle"],
                           "text": f"@{c['handle']}: {de(c['posts_per_week'], 1)} Beiträge/Woche (Posts {c['posts_prev']} → {c['posts']})."})
    for msg in dq:
        alerts.append({"priority": 5, "type": "data_quality", "text": msg})
    alerts.sort(key=lambda a: a["priority"])
    return alerts


def hook_precision(rows, min_n=10):
    """Per heuristic hook class: precision/recall against codebook caption_hook_category (where both exist)."""
    pairs = [(r["hook_h"], r["code_hook"]) for r in rows if r.get("code_hook")]
    nh, nc, tp = Counter(h for h, _ in pairs), Counter(c for _, c in pairs), Counter(h for h, c in pairs if h == c)
    return [{"hook": h, "n_heuristic": nh[h], "n_code": nc[h], "precision": tp[h] / nh[h], "recall": (tp[h] / nc[h]) if nc[h] else None}
            for h in sorted(nh, key=lambda k: -nh[k]) if nh[h] >= min_n]


def validation(rows):
    out = []
    for kw, code, label in (("kw_room", "code_room", "Raum"), ("kw_style", "code_style", "Stil"), ("hook_h", "code_hook", "Hook-Typ")):
        pairs = [(r[kw], r[code]) for r in rows if r.get(code) and (r["code_visual_ok"] or code == "code_hook")]
        if code != "code_hook":
            pairs = [(a, b) for a, b in pairs if a not in ("other",) and b not in ("other",)]
        if not pairs:
            continue
        agree = sum(1 for a, b in pairs if a == b)
        conf = Counter((b, a) for a, b in pairs if a != b).most_common(3)
        out.append({"field": label, "n": len(pairs), "agreement": agree / len(pairs),
                    "top_confusions": "; ".join(f"Code {b} → Heuristik {a} ({n})" for (b, a), n in conf)})
    return out


def write_csv(path, rows, fields=None):
    if not rows:
        with open(path, "w", encoding="utf-8") as f:
            f.write("")
        return
    fields = fields or [k for k in rows[0].keys() if not k.startswith("_")]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items() if k in fields})


def main():
    ap = argparse.ArgumentParser(description="Wöchentlicher Wettbewerber-/Trend-Monitor (nur öffentliche Daten, liest nur lokale Rohdateien).")
    ap.add_argument("current", help="Wochenordner mit Rohdaten (z. B. data/monitor/2026-W40 oder data/raw)")
    ap.add_argument("prev", nargs="?", help="Vorwochenordner (alternativ --prev)")
    ap.add_argument("--prev", dest="prev_opt", help="Vorwochenordner; ohne Angabe: nächstälterer Geschwisterordner mit Rohdaten")
    ap.add_argument("--no-auto-prev", action="store_true", help="keinen Vorwochenordner automatisch suchen")
    ap.add_argument("--out-dir", help="Ausgabeordner (Standard: Wochenordner)")
    ap.add_argument("--label", help="Wochenlabel überschreiben")
    ap.add_argument("--since", help="ISO-Zeitpunkt: Reels danach gelten als neu (Standard: Lauf der Vorwoche bzw. 7 Tage vor Abruf)")
    ap.add_argument("--watchlist-topics", default=DEFAULT_WL_TOPICS)
    ap.add_argument("--watchlist-competitors", default=DEFAULT_WL_COMP)
    ap.add_argument("--only-watchlist", action="store_true", help="nur Watchlist-Topics auswerten")
    ap.add_argument("--history-root", help="Ordner mit Wochenordnern für Follower-Verläufe (Standard: Elternordner)")
    ap.add_argument("--min-n", type=int, default=8, help="Mindest-n je Hook-Typ/Topic für Vergleiche (Standard 8)")
    ap.add_argument("--min-tq", type=int, default=30, help="Mindestzahl Top-Quartil-Reels je Woche für Anteilsvergleiche (30)")
    ap.add_argument("--min-seg", type=int, default=5, help="Mindestzahl Top-Quartil-Reels des Segments in einer der Wochen (5)")
    ap.add_argument("--min-pp", type=float, default=5.0, help="Mindeständerung in Prozentpunkten für Alarm (5)")
    ap.add_argument("--max-q", type=float, default=0.10, help="max. Benjamini-Hochberg-q für Segment- und Hook-Alarme (0,10)")
    ap.add_argument("--min-followers", type=int, default=1000, help="unter dieser Followerzahl gelten vpf-Alarme als schwach (1000)")
    ap.add_argument("--min-growth", type=float, default=5.0, help="Follower-Wachstum in %% pro Lauf für Alarm (5)")
    ap.add_argument("--min-posts-week", type=float, default=14.0, help="Beiträge/Woche für Kadenz-Hinweis (14)")
    ap.add_argument("--min-code-cov", type=float, default=0.8, help="Mindestanteil codierter Reels, damit Hook-Codes statt Heuristik genutzt werden (0,8)")
    ap.add_argument("--todo", action="store_true", help="nur embed_todo.json schreiben (welche Embeds fehlen noch)")
    ap.add_argument("--todo-max", type=int, default=40)
    ap.add_argument("--dump-captions", type=int, metavar="I", help="Captions-Chunk I (sortiert nach Shortcode) als JSON ausgeben; -1 = nur Anzahl")
    ap.add_argument("--chunk", type=int, default=150, help="Chunkgröße für --dump-captions (150)")
    args = ap.parse_args()

    cur_dir = os.path.abspath(args.current)
    if not os.path.isdir(cur_dir):
        sys.exit(f"Ordner nicht gefunden: {cur_dir}")
    out_dir = os.path.abspath(args.out_dir or cur_dir)
    os.makedirs(out_dir, exist_ok=True)
    week_c = Week(cur_dir, args.label)
    if not week_c.apps:
        sys.exit(f"Keine Topic-Reels in {cur_dir} (erwartet topics/batch_*.json oder batch_*.json).")
    if args.dump_captions is not None:  # helper for the caption-coding agents of the weekly workflow
        caps = {}
        for a in week_c.apps:
            if a["shortcode"] not in caps or len(a["caption"]) > len(caps[a["shortcode"]]["caption"]):
                caps[a["shortcode"]] = {"shortcode": a["shortcode"], "handle": a["handle"], "caption": a["caption"][:300]}
        rows = [caps[k] for k in sorted(caps)]
        if args.dump_captions < 0:
            print(json.dumps({"n": len(rows), "chunk_size": args.chunk, "chunks": math.ceil(len(rows) / args.chunk)}))
        else:
            print(json.dumps(rows[args.dump_captions * args.chunk:(args.dump_captions + 1) * args.chunk], ensure_ascii=False))
        return

    prev_dir = args.prev_opt or args.prev
    if not prev_dir and not args.no_auto_prev:
        parent = os.path.dirname(cur_dir)
        sibs = sorted(d for d in os.listdir(parent) if WEEK_DIR_RX.match(d) and os.path.join(parent, d) != cur_dir
                      and d < os.path.basename(cur_dir) and _files(os.path.join(parent, d), ["topics"], "batch_*.json"))
        if sibs:
            prev_dir = os.path.join(parent, sibs[-1])
    week_p = Week(os.path.abspath(prev_dir)) if prev_dir else None
    if week_p is not None and not week_p.apps:
        week_c.issues.append(f"Vorwochenordner `{prev_dir}` enthält keine Topic-Reels – kein Wochenvergleich.")
        week_p = None

    if args.since:
        cutoff = _date(args.since)
    elif week_p is not None and week_p.run_time:
        cutoff = week_p.run_time
    elif week_c.run_time:
        cutoff = week_c.run_time - dt.timedelta(days=7)
    else:
        cutoff = None
    cutoff_note = ("--since" if args.since else "Lauf der Vorwoche" if (week_p is not None and week_p.run_time) else "7 Tage vor Abruf")

    info_c = week_c.topic_metrics()
    info_p = week_p.topic_metrics() if week_p else None
    wl_topics = {r["slug"] for r in load_watchlist(args.watchlist_topics)}
    topics_c = set(week_c.ok_topics())
    if args.only_watchlist and wl_topics:
        topics_c &= wl_topics
    common = (topics_c & set(week_p.ok_topics())) if week_p else None
    prev_sc = {a["shortcode"] for a in week_p.apps} if week_p else None

    fb = week_p.accounts if week_p is not None else None
    all_c = build_reels(week_c, topics_c, cutoff, fb)
    for r in all_c:
        r["seen_last_week"] = (r["shortcode"] in prev_sc) if prev_sc is not None else None
        if prev_sc is not None and r["shortcode"] in prev_sc:
            r["is_new"] = False
    wl_comp = load_watchlist(args.watchlist_competitors)

    # ---------- todo mode: which embed pages are still missing? -------------------------------------------------
    if args.todo:
        comp = []
        for c in wl_comp:
            h = c["handle"].lower()
            newest = max((r for r in all_c if r["handle"] == h and r["_posted"]), key=lambda r: r["_posted"], default=None)
            sc = newest["shortcode"] if newest and (not _date(c.get("last_posted_utc")) or newest["_posted"] > _date(c["last_posted_utc"])) else c.get("last_shortcode")
            if h not in week_c.accounts and sc:
                comp.append({"handle": h, "shortcode": sc, "embed_url": f"https://www.instagram.com/reel/{sc}/embed/captioned/"})
        # new reels: always (exact likes/comments + current followers); older reels only if followers are still unknown
        need = [r for r in all_c if r["shortcode"] not in week_c.embeds
                and (r["is_new"] or (r["followers"] is None and (r["topic_index"] or 0) >= 2))]
        need.sort(key=lambda r: (not r["is_new"], -(r["topic_index"] or 0)))
        todo = {"week": week_c.label, "competitors": comp,
                "reels": [{"handle": r["handle"], "shortcode": r["shortcode"], "reason": "new" if r["is_new"] else "followers_unknown",
                           "topic_index": round(r["topic_index"], 2) if r["topic_index"] else None,
                           "embed_url": f"https://www.instagram.com/reel/{r['shortcode']}/embed/captioned/"} for r in need[:args.todo_max]],
                "dropped_by_todo_max": max(0, len(need) - args.todo_max)}
        path = os.path.join(out_dir, "embed_todo.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(todo, f, ensure_ascii=False, indent=1)
        print(f"embed_todo.json: {len(comp)} Wettbewerber + {len(todo['reels'])} Reels ({todo['dropped_by_todo_max']} wegen --todo-max ausgelassen) -> {path}")
        return

    # ---------- comparisons on common topics ------------------------------------------------------------------
    cur_cmp = build_reels(week_c, common, cutoff, fb) if common is not None else all_c
    prev_cmp = build_reels(week_p, common, None) if common is not None else None
    # hook type: codebook codes only if (almost) every reel is coded in BOTH weeks, else the same heuristic for all
    cov_c, cov_p = code_coverage(cur_cmp), (code_coverage(prev_cmp) if prev_cmp is not None else None)
    use_code = cov_c >= args.min_code_cov and (cov_p is None or cov_p >= args.min_code_cov)
    for rows in (all_c, cur_cmp, prev_cmp or []):
        apply_hook_source(rows, use_code)
    hook_source = (f"Codebuch-Codierung (Abdeckung {pct(cov_c, 0)}{'' if cov_p is None else ' / Vorwoche ' + pct(cov_p, 0)}, Rest Heuristik)"
                   if use_code else f"Heuristik (Codebuch-Abdeckung {pct(cov_c, 0)} < {pct(args.min_code_cov, 0)}; Paarvergleiche nur {', '.join(sorted(HOOK_RELIABLE))})")
    seg_rows, overlap = segment_shares(cur_cmp, prev_cmp, args)
    hooks, pairs = hook_table(cur_cmp, prev_cmp, args, allowed=None if use_code else HOOK_RELIABLE)
    topics = topic_table(week_c, info_c, week_p, info_p, all_c, cutoff, prev_sc)
    if args.only_watchlist and wl_topics:
        topics = [t for t in topics if t["topic"] in wl_topics]
    hist_root = args.history_root or os.path.dirname(cur_dir)
    series = history_series(hist_root)
    if week_p is not None and os.path.dirname(week_p.folder) != os.path.abspath(hist_root):
        for h, a in week_p.accounts.items():  # previous week lives elsewhere (e.g. data/raw baseline): prepend it
            if not any(x[0] == week_p.label for x in series.get(h, [])):
                series[h].insert(0, (week_p.label, week_p.run_time, a["followers"], a["followers_text"], a["followers_step"], a["posts"]))
    comps = competitor_table(wl_comp, week_c, week_p, all_c, series)
    cmedia = competitor_media_table(week_c, cutoff)
    new_api = Counter(r["handle"] for r in cmedia if r["is_new"])
    for c in comps:
        c["new_posts_api"] = new_api.get(c["handle"]) if cmedia else None

    # ---------- data quality ------------------------------------------------------------------------------------
    dq = list(week_c.issues)
    slug_st = week_c.slug_status()
    n_status = len(slug_st)
    n_fail = sum(1 for v in slug_st.values() if v != "ok")
    if n_status and n_fail / n_status > 0.2:
        dq.append(f"{n_fail} von {n_status} Topic-Seiten nicht erfolgreich (> 20 %) – Wochenvergleich eingeschränkt.")
    if wl_topics:
        missing = sorted(wl_topics - {t["slug"] for t in week_c.topic_status} - {t["requested"] for t in week_c.topic_status})
        if missing and len(missing) < len(wl_topics):
            dq.append(f"{len(missing)} Watchlist-Topics fehlen in dieser Woche: {', '.join(missing[:12])}{' …' if len(missing) > 12 else ''}")
    new_out = sorted([r for r in all_c if r["is_new"]], key=lambda r: -(r["topic_index"] or 0))
    fol_cov = sum(1 for r in all_c if r["followers"]) / len(all_c)
    if fol_cov < 0.5:
        dq.append(f"Nur {pct(fol_cov, 0)} der Reels mit Followerzahl – vpf/Tiers unvollständig (Embeds via `--todo` nachziehen).")
    comp_missing = [c["handle"] for c in comps if not c["embed_found"]]
    if wl_comp and len(comp_missing) > len(wl_comp) / 2:
        dq.append(f"Für {len(comp_missing)} von {len(wl_comp)} Watchlist-Accounts keine Embed-Daten in dieser Woche.")
    if week_p is not None and common is not None and len(common) < 10:
        dq.append(f"Nur {len(common)} gemeinsame Topics mit der Vorwoche – Anteilsvergleiche kaum belastbar.")
    alerts = build_alerts(new_out, seg_rows, pairs, topics, comps, dq, overlap, args, hook_source)
    for r in cmedia:
        if r["is_new"] and (r["account_index"] or 0) >= 3:
            alerts.append({"priority": 2, "type": "competitor_outlier", "handle": r["handle"], "shortcode": r["shortcode"],
                           "text": f"@{r['handle']}: neues Reel {link(r['shortcode'])} mit {de_count(r['value'])} {r['metric']} = "
                                   f"{de(r['account_index'], 1)}× Account-Median (n = {r['n_media_returned']} Medien, offizielle API)."})
    alerts.sort(key=lambda a: a["priority"])
    val = validation(all_c)

    # ---------- files -------------------------------------------------------------------------------------------
    reel_fields = ["shortcode", "url", "handle", "posted_at_utc", "is_new", "seen_last_week", "age_days", "views", "metric",
                   "topic_index", "topic_pct", "in_top_quartile", "followers", "followers_source", "vpf", "tier", "likes",
                   "comments", "likes_per_view", "n_topics", "topics", "topic_group", "kw_room", "kw_style", "kw_setting",
                   "kw_combo", "hook", "hook_source", "hook_h", "ai_disclosed_kw", "caption_first_line", "code_room", "code_style", "code_hook",
                   "code_production", "code_realism"]
    write_csv(os.path.join(out_dir, "monitor_reels.csv"), sorted(all_c, key=lambda r: -(r["topic_index"] or 0)), reel_fields)
    write_csv(os.path.join(out_dir, "monitor_topics.csv"), topics)
    write_csv(os.path.join(out_dir, "monitor_segments.csv"), seg_rows)
    write_csv(os.path.join(out_dir, "monitor_competitors.csv"), comps)
    if cmedia:
        write_csv(os.path.join(out_dir, "monitor_competitor_media.csv"), cmedia)
    insp = [r for r in all_c if (r["is_new"] or prev_sc is None or not r.get("seen_last_week"))
            and (r["tier"] in ("4_VIRAL", "5_EXTREME_OUTLIER") or (r["topic_index"] or 0) >= 5)]
    insp.sort(key=lambda r: (not r["is_new"], -(r["topic_index"] or 0)))
    insp_rows = [{**{k: r[k] for k in ("shortcode", "url", "handle", "posted_at_utc", "is_new", "topics", "views", "topic_index",
                                       "followers", "vpf", "tier", "hook", "hook_source", "kw_room", "kw_style", "kw_setting", "caption_first_line")},
                  "principle_own_words": "", "pillar_fit": "", "test_idea": "", "similarity_risk": "", "decision": ""}
                 for r in insp[:60]]
    write_csv(os.path.join(out_dir, "inspiration_candidates.csv"), insp_rows)
    nxt = []
    for c, row in zip(wl_comp, comps):
        c2 = dict(c)
        if row["watchlist_shortcode_outdated"]:
            c2["last_shortcode"], c2["last_posted_utc"] = row["newest_shortcode"], row["newest_posted"]
            c2["embed_url"] = f"https://www.instagram.com/reel/{row['newest_shortcode']}/embed/captioned/"
        nxt.append(c2)
    if nxt:
        write_csv(os.path.join(out_dir, "watchlist_competitors_next.csv"), nxt, list(wl_comp[0].keys()))
    with open(os.path.join(out_dir, "alerts.json"), "w", encoding="utf-8") as f:
        json.dump({"week": week_c.label, "prev_week": week_p.label if week_p else None, "alerts": alerts,
                   "hook_pairs": pairs[:10], "validation": val}, f, ensure_ascii=False, indent=1, default=str)

    # ---------- report.md ---------------------------------------------------------------------------------------
    L = []
    L.append(f"# Wettbewerber- und Trend-Monitor {week_c.label}\n")
    L.append(f"Automatisch erzeugt von `scripts/monitor/monitor_weekly.py` am {dt.datetime.now(UTC).strftime('%Y-%m-%d %H:%M')} UTC. "
             "Nur öffentliche Daten, keine Kausalaussagen. Methodik und Grenzen: `17_competitor_monitor.md`.\n")
    L.append("## 0. Datenbasis\n")
    tq_all = sum(1 for r in all_c if r["in_top_quartile"])
    L.append(md_table(["Kennzahl", "Diese Woche", "Vorwoche / Vergleich"], [
        ["Rohdatenordner", f"`{os.path.relpath(cur_dir, ROOT)}`", f"`{os.path.relpath(week_p.folder, ROOT)}`" if week_p else "keiner"],
        ["Abrufdatum / Laufzeit", ", ".join(sorted(week_c.fetched)) or "–", ", ".join(sorted(week_p.fetched)) if week_p else "–"],
        ["Topic-Seiten ok / angefragt (eindeutige Slugs)", f"{len(week_c.ok_topics())} / {n_status}", f"{len(week_p.ok_topics())} / {len(week_p.slug_status())}" if week_p else "–"],
        ["Ausgewertete Topics", len(topics_c), f"{len(common)} gemeinsame Topics (nur diese im Wochenvergleich)" if common is not None else "–"],
        ["Eindeutige Reels / davon Top-Quartil", f"{len(all_c)} / {tq_all}", f"{len(prev_cmp)} / {sum(1 for r in prev_cmp if r['in_top_quartile'])} (gemeinsame Topics)" if prev_cmp is not None else "–"],
        ["Neue Reels (veröffentlicht nach Stichtag)", f"{len(new_out)} (Stichtag {cutoff.strftime('%Y-%m-%d %H:%M') if cutoff else '–'} UTC, {cutoff_note})", ""],
        ["Reels mit Followerzahl (vpf/Tier möglich)", f"{sum(1 for r in all_c if r['followers'])} ({pct(fol_cov, 0)})", ""],
        ["Reels mit Codebuch-Codierung", f"{sum(1 for r in all_c if r['code_hook'] or r['code_room'])} (Hook-Quelle: {hook_source})", ""],
        ["Watchlist-Accounts mit Embed-Daten", f"{sum(1 for c in comps if c['embed_found'])} / {len(comps)}", ""],
        ["Metrik je Topic-Seite", ", ".join(f"{k}: {v}" for k, v in Counter(i["metric"] for i in info_c.values()).items()), ""],
    ]))
    L.append("\n**Lesehilfe:** topic_index 1,0 = typisch für die Topic-Seite; Top-Quartil = Reel liegt auf mindestens einer seiner "
             "Topic-Seiten im oberen Viertel (topic_pct ≥ 0,75; wer auf mehreren Seiten steht, hat mehr Chancen, daher > 25 %). "
             "Raum, Stil und Setting stammen aus Keyword-Regeln auf Caption + Topic-Slug, damit jede Woche identisch gemessen wird; "
             f"Hook-Quelle: {hook_source}. Genauigkeit der Regeln: Abschnitt 8. "
             "Topic-Seiten zeigen nur ~12 Top-Reels: Wir sehen Gewinner, keine Flops (Survivorship).\n")

    L.append("## 1. Alerts\n")
    if alerts:
        caps = {"new_outlier": 10, "new_outlier_no_followers": 5, "topic_shift": 5, "competitor_cadence": 5, "competitor_growth": 8}
        shown_by, hidden = Counter(), Counter()
        for a in alerts:
            if shown_by[a["type"]] >= caps.get(a["type"], 99):
                hidden[a["type"]] += 1
                continue
            shown_by[a["type"]] += 1
            L.append(f"- **P{a['priority']} · {a['type']}** – {a['text']}")
        if hidden:
            L.append("- … nicht gezeigt (vollständig in `alerts.json`): " + ", ".join(f"{n} × {t}" for t, n in hidden.items()))
    else:
        L.append("Keine Alerts über den Mindest-n-Schwellen.")
    L.append("")

    L.append("## 2. Neue Reels auf den Topic-Seiten (nach topic_index)\n")
    if new_out:
        L.append(md_table(["Reel", "Handle", "Topic(s)", "Views", "topic_index", "Follower", "vpf", "Tier", "Alter (T)", "Hook", "Stil × Raum", "Erste Zeile"],
                          [[link(r["shortcode"]), "@" + r["handle"], r["topics"].replace(";", ", ")[:50], de_count(r["views"]), de(r["topic_index"], 2),
                            de_count(r["followers"]), de(r["vpf"], 1), (r["tier"] or "–")[2:], de(r["age_days"], 1), r["hook"], r["kw_combo"],
                            r["caption_first_line"][:70]] for r in new_out[:25]]))
        if len(new_out) > 25:
            L.append(f"\n… {len(new_out) - 25} weitere in `monitor_reels.csv` (Spalte `is_new`).")
    else:
        L.append("Keine neuen Reels seit dem Stichtag auf den Topic-Seiten.")
    L.append("")

    L.append("## 3. Ausreißer der Woche (alle Reels, vpf-Tier VIRAL/EXTREME)\n")
    outl = sorted([r for r in all_c if r["tier"] in ("4_VIRAL", "5_EXTREME_OUTLIER")], key=lambda r: -(r["vpf"] or 0))
    tier_counts = Counter(r["tier"] for r in all_c if r["tier"])
    L.append("Tier-Verteilung (Reels mit Followerzahl): " + ", ".join(f"{k[2:]} {v}" for k, v in sorted(tier_counts.items())) + "\n")
    if outl:
        L.append(md_table(["Reel", "Handle", "Views", "Follower", "vpf", "topic_index", "neu?", "Veröffentlicht", "Likes/View", "Hook", "Stil × Raum"],
                          [[link(r["shortcode"]), "@" + r["handle"], de_count(r["views"]), de_count(r["followers"]), de(r["vpf"], 1),
                            de(r["topic_index"], 2), "ja" if r["is_new"] else "", (r["posted_at_utc"] or "")[:10],
                            de(r["likes_per_view"], 3), r["hook"], r["kw_combo"]] for r in outl[:20]]))
    L.append("")

    L.append("## 4. Segment-Anteile im Top-Quartil\n")
    if prev_cmp is None:
        L.append("Kein Vorwochenordner → nur Anteile dieser Woche (Lift = Anteil im Top-Quartil ÷ Anteil an allen Reels).\n")
    else:
        L.append(f"Vergleich auf {len(common)} gemeinsamen Topics. {pct(overlap, 0)} der Top-Quartil-Reels dieser Woche waren schon letzte Woche "
                 "im Top-Quartil → Stichproben überlappen, p-Werte sind nur orientierend. Alarm = |Δ| ≥ "
                 f"{de(args.min_pp, 0)} pp und Benjamini-Hochberg-q < {de(args.max_q, 2)} (über alle getesteten Segmente) und ≥ {args.min_tq} "
                 f"TQ-Reels je Woche und ≥ {args.min_seg} Segment-Reels; beobachten = |Δ| ≥ {de(args.min_pp, 0)} pp und p < 0,20.\n")
    # show: all alarms/watch items, then per dimension the most frequent values with enough top-quartile reels
    flagged = [x for x in seg_rows if x["status"] in ("ALARM", "beobachten")]
    flagged.sort(key=lambda x: (x["status"] != "ALARM", -abs(x["delta_pp"] or 0)))
    per_dim = []
    for dim, _ in SEG_DIMS:
        cand = [x for x in seg_rows if x["dimension"] == dim and x not in flagged and "other" not in x["value"]
                and max(x["n_tq_cur"], x["n_tq_prev"] or 0) >= args.min_seg]
        per_dim += sorted(cand, key=lambda x: -x["n_tq_cur"])[:6]
    L.append(md_table(["Dimension", "Wert", "TQ jetzt", "Anteil TQ jetzt", "Anteil alle", "Lift", "Anteil TQ Vorwoche", "Δ pp", "p", "q (BH)", "Status"],
                      [[x["dimension_label"], x["value"], f"{x['n_tq_cur']}/{x['tq_cur']}", pct(x["share_tq_cur"]), pct(x["share_all_cur"]),
                        de(x["lift_cur"], 2), pct(x["share_tq_prev"]), de(x["delta_pp"], 1), de(x["p_fisher"], 3), de(x["q_bh"], 3), x["status"]]
                       for x in flagged + per_dim]))
    L.append(f"\nVollständige Tabelle (alle Werte): `monitor_segments.csv`. Gezeigt: Alarme/Beobachten und je Dimension die 6 häufigsten Werte mit ≥ {args.min_seg} TQ-Reels.")
    L.append("")

    L.append("## 5. Hook-Typen\n")
    L.append(f"Quelle: {hook_source}.\n")
    L.append(md_table(["Hook", "n", "Median topic_index", "Anteil im TQ", "n Vorwoche", "Median Vorwoche", "Vergleichbar (n ≥ %d)" % args.min_n],
                      [[h["hook"], h["n"], de(h["median_ti"], 2), pct(h["share_tq"]), h["n_prev"] if h["n_prev"] is not None else "–",
                        de(h["median_ti_prev"], 2), "ja" if h["enough"] else "nein"] for h in hooks]))
    sig = [p for p in pairs if p["q_bh"] < args.max_q and p["ratio"] >= 1.5]
    L.append(f"\nPaarvergleiche (Mann-Whitney, {len(pairs)} Paare, Benjamini-Hochberg-q < {de(args.max_q, 2)}, Median-Verhältnis ≥ 1,5): " +
             ("; ".join(f"{p['better']} > {p['worse']} ({de(p['median_better'], 2)} vs. {de(p['median_worse'], 2)}, n = {p['n_better']}/{p['n_worse']}, "
                        f"p = {de(p['p'], 3)}, q = {de(p['q_bh'], 3)})" for p in sig[:5]) if sig else "keine.") + "\n")

    L.append("## 6. Topics\n")
    tt = sorted([t for t in topics if t["status"] == "ok"], key=lambda t: -(t["share_fresh"] or 0))
    L.append("Frische = Anteil der Reels auf der Seite, die nach dem Stichtag veröffentlicht wurden (dort brechen neue Reels ein). "
             "Neueinträge = nicht auf der Seite der Vorwoche.\n")
    L.append(md_table(["Topic", "Gruppe", "n", "Median", "Median Vorwoche", "×", "Frische", "Neueinträge"],
                      [[t["topic"], t["group"], t["n"], de_count(t["median"]), de_count(t["median_prev"]), de(t["median_ratio"], 2),
                        pct(t["share_fresh"], 0), pct(t["share_new_entries"], 0)] for t in tt[:30]]))
    failed = [t for t in topics if t["status"] != "ok"]
    if failed:
        L.append(f"\nNicht erfolgreich abgerufen ({len(failed)}): " + ", ".join(t["topic"] for t in failed[:40]))
    L.append("")

    L.append("## 7. Wettbewerber-Watchlist\n")
    if comps:
        L.append("Follower sind auf Embed-Seiten gerundet: Eine Änderung zählt nur, wenn sie größer als die Rundungsstufe ist. "
                 "Beitragszahlen sind exakt → Beiträge/Woche ist belastbar.\n")
        cs = sorted(comps, key=lambda c: (-(c["best_topic_index"] or 0), c["handle"]))
        L.append(md_table(["Handle", "Rolle", "Follower", "Vorwoche", "Δ erkennbar?", "Posts", "Δ Posts", "Posts/Woche", "Reels auf Topics (neu)", "bester topic_index", "Verlauf"],
                          [["@" + c["handle"], c["role"], short(c["followers_text"]), short(c["followers_prev_text"]),
                            ("ja, " + de(c["growth_pct"], 1) + " %") if c["delta_detectable"] else ("innerhalb Rundung" if c["delta_followers"] is not None else "–"),
                            c["posts"] if c["posts"] is not None else "–", c["delta_posts"] if c["delta_posts"] is not None else "–",
                            de(c["posts_per_week"], 1), f"{c['reels_on_topic_pages']} ({c['new_reels_on_topic_pages']})", de(c["best_topic_index"], 2),
                            c["history"]] for c in cs]))
        outdated = [c for c in comps if c["watchlist_shortcode_outdated"]]
        if outdated:
            L.append(f"\n{len(outdated)} Watchlist-Shortcodes sind veraltet → `watchlist_competitors_next.csv` prüfen und übernehmen.")
    else:
        L.append("Keine Wettbewerber-Watchlist gefunden.")
    L.append("")

    if cmedia:
        L.append("### 7b. Wettbewerber-Reels aus der offiziellen API (Account-Index = Reel ÷ Median des Accounts)\n")
        L.append(md_table(["Handle", "Reel", "Veröffentlicht", "neu?", "Wert", "Account-Median", "Account-Index", "Hook (H)", "Erste Zeile"],
                          [["@" + r["handle"], link(r["shortcode"]), (r["posted_at_utc"] or "")[:10], "ja" if r["is_new"] else "",
                            f"{de_count(r['value'])} {r['metric']}", de_count(r["account_median"]), de(r["account_index"], 2), r["hook_h"],
                            r["caption_first_line"][:60]] for r in cmedia[:20]]))
        L.append("")

    L.append("## 8. Messgenauigkeit der Segment-Regeln (gegen Codebuch-Codes, falls vorhanden)\n")
    if val:
        L.append(md_table(["Feld", "n", "Übereinstimmung", "Häufigste Abweichungen"],
                          [[v["field"], v["n"], pct(v["agreement"], 0), v["top_confusions"]] for v in val]))
        hp = hook_precision(all_c)
        if hp:
            L.append("\nHook-Heuristik je Klasse (Präzision = Anteil der Heuristik-Treffer, die das Codebuch genauso codiert):\n")
            L.append(md_table(["Hook (Heuristik)", "n Heuristik", "n Codebuch", "Präzision", "Recall"],
                              [[h["hook"], h["n_heuristic"], h["n_code"], pct(h["precision"], 0), pct(h["recall"], 0)] for h in hp]))
        L.append("\nNiedrige Übereinstimmung heißt: Segmentanteile nur als Trendrichtung lesen; für Entscheidungen die Reels im Board ansehen.")
    else:
        L.append("Keine codierten Reels in diesem Ordner – Genauigkeit nicht messbar (Referenz: Research-Baseline).")
    L.append("")

    L.append("## 9. Menschliche Review (G5, ca. 20 Min.)\n")
    L.append("- [ ] Alerts P1–P2 öffnen (Links), Reel ansehen, in `inspiration_candidates.csv` **Prinzip in eigenen Worten** notieren – keine Downloads, keine Motiv-Kopie.")
    L.append("- [ ] Pro übernommenem Prinzip: Pillar-Fit (ja/nein) und eine Testidee für die Testmatrix der nächsten Woche (genau **ein** Faktor).")
    L.append("- [ ] Segment-Alarme gegen Abschnitt 8 (Messgenauigkeit) und Überlappung prüfen; nur als Hypothese übernehmen.")
    L.append("- [ ] `watchlist_competitors_next.csv` übernehmen, falls Shortcodes veraltet; Accounts ohne Embed-Daten prüfen (umbenannt/gelöscht?).")
    L.append("- [ ] Eigener **Account Status** in der App geprüft (nur manuell möglich).")
    L.append("")
    with open(os.path.join(out_dir, "report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    print(f"Woche {week_c.label}: {len(all_c)} Reels ({len(new_out)} neu), {len(topics_c)} Topics"
          f"{f', Vergleich {week_p.label} auf {len(common)} gemeinsamen Topics' if week_p else ', kein Vorwochenvergleich'}; "
          f"{len(alerts)} Alerts -> {os.path.relpath(os.path.join(out_dir, 'report.md'), os.getcwd())}")


if __name__ == "__main__":
    main()
