"""Parse follower lookups (reel embed pages) into one account table.

Input : data/raw/accounts/followers_*.json
Output: data/processed/accounts_followers.csv
"""
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_topics import parse_views  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw", "accounts")
OUT = os.path.join(ROOT, "data", "processed")


def parse_count(text):
    if text is None:
        return None
    t = re.sub(r"(?i)(followers?|posts?|likes?|comments?|view all)", "", str(text)).strip()
    return parse_views(t)


def main():
    rows = {}
    for path in sorted(glob.glob(os.path.join(RAW, "followers_*.json"))):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"!! invalid JSON {path}: {e}")
            continue
        for a in data.get("accounts", []):
            h = (a.get("handle_shown") or a.get("handle") or "").lower().lstrip("@").strip()
            if a.get("status") != "ok" or not h:
                continue
            fol = parse_count(a.get("followers_text"))
            rec = {
                "handle": h, "expected_handle": (a.get("handle") or "").lower(), "handle_mismatch": a.get("handle_mismatch"),
                "display_name": a.get("display_name"), "followers_text": a.get("followers_text"), "followers": fol,
                "posts_text": a.get("posts_text"), "posts": parse_count(a.get("posts_text")),
                "verified": a.get("verified"), "sample_shortcode": a.get("shortcode"),
                "sample_likes": parse_count(a.get("likes_text")), "sample_comments": parse_count(a.get("comments_text")),
                "source_url": a.get("url"), "fetched_at": data.get("fetched_at"), "status": "VERIFIED" if fol else "UNKNOWN",
            }
            if h not in rows or (rows[h]["followers"] is None and fol):
                rows[h] = rec
    out = sorted(rows.values(), key=lambda r: -(r["followers"] or 0))
    with open(os.path.join(OUT, "accounts_followers.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()) if out else ["handle"])
        w.writeheader(); w.writerows(out)
    print(f"accounts with data: {len(out)} | with followers: {sum(1 for r in out if r['followers'])}")


if __name__ == "__main__":
    main()
