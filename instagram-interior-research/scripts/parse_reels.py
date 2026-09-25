"""Flatten coded reels into tables.

Inputs
  data/raw/reels/cover_*.json  - cover-frame + caption codebook (scripts/cover_codebook.md), embed-page metadata
  data/raw/reels/coded_*.json  - NexLev video-watch codebook (scripts/reel_codebook_prompt.txt), small subset
Outputs
  data/processed/reels_cover_coded.csv
  data/processed/reels_video_coded.csv
"""
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_accounts import parse_count  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw", "reels")
OUT = os.path.join(ROOT, "data", "processed")

COVER_SCALARS = [
    "room_primary", "building_type", "landscape", "style_primary", "style_secondary", "palette_temp", "brightness",
    "lighting", "view_through_window", "people_present", "cover_text", "realism", "production", "production_evidence",
    "shoppability", "visual_quality", "notable", "caption_hook_category", "caption_first_line", "cta_type",
    "location_claimed", "price_claimed", "ai_disclosed", "account_kind_hint", "language",
]
COVER_LISTS = ["rooms_visible", "dominant_colors", "materials", "ambience_fx", "cover_hooks"]
VIDEO_SCALARS = [
    "length_sec", "n_scenes", "room_primary", "building_type", "landscape", "location_claimed", "style_primary",
    "style_secondary", "palette_temp", "brightness", "lighting", "camera_motion", "camera_speed", "format",
    "first_frame", "onscreen_text", "text_hook_category", "audio_type", "music_genre", "audio_mood", "voiceover",
    "people_present", "realism", "production", "ai_evidence", "shoppability", "notable",
]
VIDEO_LISTS = ["rooms_all", "dominant_colors", "materials", "ambience_fx", "first_2s_hooks"]
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")


def as_code(c):
    if isinstance(c, str):
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            return {}
    return c or {}


def caption_feats(cap):
    cap = cap or ""
    return {
        "caption_len": len(cap), "caption_hashtags": len(re.findall(r"#\w+", cap)),
        "caption_has_question": "?" in cap, "caption_emojis": len(EMOJI.findall(cap)),
        "caption_mentions": len(re.findall(r"@\w+", cap)),
        "caption_link_hint": bool(re.search(r"(?i)link in (bio|profile)|shop (the|my)|amzn|ltk|liketoknow|shopmy", cap)),
        "caption_comment_cta": bool(re.search(r"(?i)comment ['\"“]?\w+['\"”]? (below|and|for|to)|comment below|drop a|tell me|which one|would you", cap)),
    }


def parse_cover():
    rows = {}
    for path in sorted(glob.glob(os.path.join(RAW, "cover_*.json"))):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"!! invalid JSON {path}: {e}")
            continue
        for r in data.get("reels", []):
            sc = (r.get("shortcode") or "").strip()
            if not sc:
                continue
            code = as_code(r.get("code"))
            cap = r.get("caption") or ""
            rec = {
                "shortcode": sc,
                "handle": (r.get("handle") or r.get("expected_handle") or "").lower().lstrip("@").strip(),
                "meta_status": r.get("meta_status"), "visual_status": r.get("visual_status"),
                "media_type": r.get("media_type"),
                "followers_text": r.get("followers_text"), "followers_at_fetch": parse_count(r.get("followers_text")),
                "posts_at_fetch": parse_count(r.get("posts_text")),
                "likes": parse_count(r.get("likes_text")), "comments": parse_count(r.get("comments_text")),
                **caption_feats(cap), "caption": cap.replace("\n", " ")[:1500], "coder": data.get("coder"),
                "source_file": os.path.basename(path),
            }
            for k in COVER_SCALARS:
                rec[k] = code.get(k)
            for k in COVER_LISTS:
                v = code.get(k)
                rec[k] = ";".join(str(x) for x in v) if isinstance(v, list) else (v or "")
            prev = rows.get(sc)
            if prev is None or (prev.get("visual_status") != "ok" and rec.get("visual_status") == "ok"):
                rows[sc] = rec
    return list(rows.values())


def parse_video():
    rows = {}
    for path in sorted(glob.glob(os.path.join(RAW, "coded_*.json"))):
        data = json.load(open(path, encoding="utf-8"))
        for r in data.get("reels", []):
            code = as_code(r.get("code"))
            if not code:
                continue
            rec = {"shortcode": r["shortcode"], "handle": (r.get("handle") or r.get("expected_handle") or "").lower()}
            for k in VIDEO_SCALARS:
                rec[k] = code.get(k)
            for k in VIDEO_LISTS:
                v = code.get(k)
                rec[k] = ";".join(str(x) for x in v) if isinstance(v, list) else (v or "")
            rows[rec["shortcode"]] = rec
    return list(rows.values())


def write(rows, name):
    if not rows:
        return
    keys = list(rows[0].keys())
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader(); w.writerows(rows)


def main():
    cov = parse_cover()
    write(cov, "reels_cover_coded.csv")
    vid = parse_video()
    write(vid, "reels_video_coded.csv")
    print(f"cover-coded: {len(cov)} (visual ok {sum(1 for r in cov if r['visual_status']=='ok')}, "
          f"followers {sum(1 for r in cov if r['followers_at_fetch'])}) | video-coded (NexLev): {len(vid)}")


if __name__ == "__main__":
    main()
