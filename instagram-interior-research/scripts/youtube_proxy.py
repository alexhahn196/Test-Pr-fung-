"""Cross-platform proxy analysis on YouTube Shorts (length, title hooks, visual change).

Why: Instagram does not expose reel duration/motion publicly and the only reel-watching tool
available (NexLev) is capped at 15 calls/day. YouTube Shorts from faceless interior/home channels
(many cross-post the same clips) provide duration + views at scale. Treat results as a PROXY.

Input : data/raw/youtube/shorts_*.json (NexLev youtube_channel_shorts + youtube_video_details)
Output: data/processed/youtube_shorts.csv, data/processed/stats/yt_*.csv
Views are normalized per channel (views / channel median) so big and small channels are comparable.
Visual change score: mean absolute difference between YouTube's auto-thumbnails at ~25/50/75 %
(i.ytimg.com/vi/<id>/hq1.jpg, hq2.jpg, hq3.jpg) -> low = static/slow single scene, high = cuts/fast motion.
"""
import glob
import io
import json
import os
import re
import sys
import urllib.request

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_topics import parse_views  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw", "youtube")
P = os.path.join(ROOT, "data", "processed")
ST = os.path.join(P, "stats")
CACHE = os.path.join(RAW, "frame_scores.json")

HOOKS = {
    "question": r"\?|^(would|which|what|how|can|do|does|is|are|who|why)\b",
    "choice": r"choose|pick|which one|\b1 or 2\b|\bor\b.*\?|\bvs\.?\b|1,? 2 or 3",
    "pov": r"^\s*pov\b|\bpov:",
    "curiosity": r"secret|hidden|won'?t believe|wait for|insane|genius|shocking|unreal|nobody|didn'?t expect|🤯|😱|crazy|mind|impossible",
    "transformation": r"turn(ed|s)? .* into|transform|built|build|from .* to|before|after|makeover|renovat|glow ?up|restor",
    "money_status": r"\$|million|billion|rich|expensive|cost|price|luxury|billionaire|millionaire",
    "location": r"dubai|bali|maldives|new york|tokyo|london|paris|swiss|italy|japan|monaco|miami|la\b|california",
    "instructional": r"how to|ideas?\b|tips?\b|hack|smart|clever|design ideas|storage",
    "fantasy_ai": r"\bai\b|imagine|dream|if you|what if|fantasy|magic",
    "cozy_ambience": r"rain|cozy|cosy|relax|sleep|asmr|calm|storm|snow",
}


def classify(title):
    t = (title or "").lower()
    return [k for k, rx in HOOKS.items() if re.search(rx, t)] or ["descriptive"]


def dur_bucket(s):
    if pd.isna(s):
        return None
    for lo, hi, lab in [(0, 5, "0-5s"), (6, 8, "6-8s"), (9, 12, "9-12s"), (13, 20, "13-20s"), (21, 30, "21-30s")]:
        if lo <= s <= hi:
            return lab
    return "30s+"


def frame_score(vid, cache):
    if vid in cache:
        return cache[vid]
    try:
        from PIL import Image
        arrs = []
        for k in ("hq1", "hq2", "hq3"):
            with urllib.request.urlopen(f"https://i.ytimg.com/vi/{vid}/{k}.jpg", timeout=20) as r:
                im = Image.open(io.BytesIO(r.read())).convert("L").resize((64, 48))
                arrs.append(np.asarray(im, dtype=float))
        d = [np.abs(arrs[i] - arrs[i + 1]).mean() for i in range(2)]
        cache[vid] = round(float(np.mean(d)), 2)
    except Exception as e:  # network or missing frame
        cache[vid] = None
    return cache[vid]


def main():
    os.makedirs(ST, exist_ok=True)
    rows, lists = [], []
    for path in sorted(glob.glob(os.path.join(RAW, "shorts_*.json"))):
        try:
            d = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError as e:
            print("!! bad json", path, e); continue
        if not d.get("relevant", True):
            continue
        ch = d.get("channel_name")
        for s in d.get("shorts", []):
            lists.append({"channel": ch, "video_id": s.get("video_id"), "title": s.get("title"), "views": parse_views(s.get("views_text")), "list": s.get("list")})
        for s in d.get("details", []):
            rows.append({"channel": ch, **{k: s.get(k) for k in ["video_id", "title", "duration_sec", "published", "views", "likes", "comments"]}})
    L = pd.DataFrame(lists).drop_duplicates("video_id")
    D = pd.DataFrame(rows).drop_duplicates("video_id")
    if L.empty:
        print("no youtube data yet"); return
    L["ch_index"] = L["views"] / L.groupby("channel")["views"].transform("median")
    L["hooks"] = L["title"].apply(classify)
    x = L.explode("hooks")
    hk = x.groupby("hooks").agg(n=("video_id", "count"), n_channels=("channel", "nunique"), median_ch_index=("ch_index", "median"), median_views=("views", "median"))
    hk.sort_values("median_ch_index", ascending=False).to_csv(os.path.join(ST, "yt_title_hooks.csv"))
    if not D.empty:
        D["duration_sec"] = pd.to_numeric(D["duration_sec"], errors="coerce")
        D["views"] = pd.to_numeric(D["views"], errors="coerce")
        D["ch_index"] = D["views"] / D.groupby("channel")["views"].transform("median")
        D["bucket"] = D["duration_sec"].apply(dur_bucket)
        cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
        D["visual_change"] = D["video_id"].apply(lambda v: frame_score(v, cache))
        json.dump(cache, open(CACHE, "w"))
        D["change_bucket"] = pd.qcut(D["visual_change"], 3, labels=["low (static/slow)", "mid", "high (cuts/fast)"]) if D["visual_change"].notna().sum() >= 9 else None
        order = ["0-5s", "6-8s", "9-12s", "13-20s", "21-30s", "30s+"]
        db = D.groupby("bucket").agg(n=("video_id", "count"), n_channels=("channel", "nunique"), median_views=("views", "median"),
                                     mean_views=("views", "mean"), median_ch_index=("ch_index", "median"),
                                     share_2x_channel_median=("ch_index", lambda s: (s >= 2).mean())).reindex(order)
        db.to_csv(os.path.join(ST, "yt_duration_buckets.csv"))
        if D["change_bucket"] is not None:
            cb = D.groupby("change_bucket", observed=True).agg(n=("video_id", "count"), median_ch_index=("ch_index", "median"), median_views=("views", "median"), median_duration=("duration_sec", "median"))
            cb.to_csv(os.path.join(ST, "yt_visual_change.csv"))
        D.to_csv(os.path.join(P, "youtube_shorts_details.csv"), index=False)
    L.to_csv(os.path.join(P, "youtube_shorts.csv"), index=False)
    print(f"shorts listed: {len(L)} from {L['channel'].nunique()} channels | with details: {len(D)}")


if __name__ == "__main__":
    main()
