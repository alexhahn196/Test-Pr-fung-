"""Parse raw Instagram /popular/ topic sweep batches into a flat reel table.

Input : data/raw/topics/batch_*.json   (written by the topic-sweep agents)
Output: data/processed/topic_reels.csv  (one row per reel x topic appearance)
        data/processed/reels_unique.csv (one row per unique shortcode)
        data/processed/handles_from_topics.csv (aggregated per handle)
        data/processed/topics_status.csv
"""
import csv
import glob
import json
import os
import re
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw", "topics")
OUT = os.path.join(ROOT, "data", "processed")


def parse_views(text):
    """'3.7M' -> 3700000, '508K' -> 508000, '9,527' -> 9527. Returns None if unparseable."""
    if text is None:
        return None
    t = str(text).strip().replace(" ", "").replace(" ", "")
    if not t or t.upper() in {"NA", "N/A", "NONE", "NULL", "-"}:
        return None
    t = re.sub(r"(?i)views?|plays?", "", t)
    m = re.fullmatch(r"(?i)([\d.,]+)([KMB])?", t)
    if not m:
        return None
    num, suf = m.group(1), (m.group(2) or "").upper()
    if suf:
        num = num.replace(",", ".") if num.count(",") == 1 and "." not in num else num.replace(",", "")
        try:
            val = float(num)
        except ValueError:
            return None
        return int(round(val * {"K": 1e3, "M": 1e6, "B": 1e9}[suf]))
    digits = num.replace(",", "").replace(".", "")
    return int(digits) if digits.isdigit() else None


def main():
    os.makedirs(OUT, exist_ok=True)
    rows, status_rows = [], []
    for path in sorted(glob.glob(os.path.join(RAW, "batch_*.json"))):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"!! invalid JSON {path}: {e}")
            continue
        batch = data.get("batch") or os.path.basename(path)
        for t in data.get("topics", []):
            slug = t.get("slug_used") or t.get("slug")
            reels = t.get("reels") or []
            status_rows.append({
                "batch": batch, "slug": t.get("slug"), "slug_used": slug, "status": t.get("status"),
                "n_reels": len(reels), "total_reels_label": t.get("total_reels_label"), "page_title": t.get("page_title"),
            })
            for pos, r in enumerate(reels, 1):
                sc = (r.get("shortcode") or "").strip().strip("/")
                if not sc or sc.upper() == "NA":
                    continue
                rows.append({
                    "topic": slug, "position": pos, "handle": (r.get("handle") or "").lower().lstrip("@").strip(),
                    "shortcode": sc, "views_text": r.get("views_text"), "views": parse_views(r.get("views_text")),
                    "caption": (r.get("caption") or "").replace("\n", " ").strip(),
                    "url": f"https://www.instagram.com/reel/{sc}/", "source": f"https://www.instagram.com/popular/{slug}/",
                    "batch": batch,
                })

    with open(os.path.join(OUT, "topics_status.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(status_rows[0].keys()) if status_rows else ["slug"])
        w.writeheader(); w.writerows(status_rows)
    with open(os.path.join(OUT, "topic_reels.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["shortcode"])
        w.writeheader(); w.writerows(rows)

    # unique reels: keep max views seen, list of topics
    uniq = {}
    for r in rows:
        u = uniq.setdefault(r["shortcode"], {**r, "topics": set()})
        u["topics"].add(r["topic"])
        if r["views"] is not None and (u["views"] is None or r["views"] > u["views"]):
            u["views"], u["views_text"] = r["views"], r["views_text"]
        if not u["handle"] and r["handle"]:
            u["handle"] = r["handle"]
    uniq_rows = []
    for u in uniq.values():
        u = dict(u); u["topics"] = ";".join(sorted(u["topics"])); u.pop("position", None); u.pop("topic", None); u.pop("batch", None)
        uniq_rows.append(u)
    uniq_rows.sort(key=lambda x: -(x["views"] or 0))
    with open(os.path.join(OUT, "reels_unique.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["shortcode", "handle", "views", "views_text", "topics", "caption", "url", "source"])
        w.writeheader(); w.writerows(uniq_rows)

    # handles
    hs = {}
    for u in uniq_rows:
        h = hs.setdefault(u["handle"], {"handle": u["handle"], "n_reels": 0, "views": [], "topics": set()})
        h["n_reels"] += 1
        if u["views"] is not None:
            h["views"].append(u["views"])
        h["topics"].update(u["topics"].split(";"))
    hrows = []
    for h in hs.values():
        v = h["views"]
        hrows.append({
            "handle": h["handle"], "n_reels_in_topics": h["n_reels"],
            "max_views": max(v) if v else None, "median_views": int(statistics.median(v)) if v else None,
            "sum_views": sum(v) if v else None, "n_topics": len(h["topics"]), "topics": ";".join(sorted(h["topics"]))[:500],
        })
    hrows.sort(key=lambda x: -(x["max_views"] or 0))
    with open(os.path.join(OUT, "handles_from_topics.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(hrows[0].keys()) if hrows else ["handle"])
        w.writeheader(); w.writerows(hrows)

    ok = sum(1 for s in status_rows if s["status"] == "ok")
    print(f"topics: {len(status_rows)} ({ok} ok) | reel rows: {len(rows)} | unique reels: {len(uniq_rows)} | handles: {len(hrows)}")


if __name__ == "__main__":
    main()
