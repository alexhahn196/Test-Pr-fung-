"""Inter-coder reliability of the AI-assisted cover coding.

A random sample of already-coded reels (seed 42) was coded a second time by independent agents
(data/raw/reliability/). For each categorical field we report % agreement and Cohen's kappa;
for list fields the mean Jaccard overlap. Output: data/processed/stats/reliability.csv
"""
import glob
import json
import os

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SINGLE = ["room_primary", "building_type", "landscape", "style_primary", "palette_temp", "brightness", "lighting",
          "realism", "production", "shoppability", "caption_hook_category", "cta_type", "account_kind_hint",
          "people_present", "view_through_window", "ai_disclosed"]
LISTS = ["materials", "dominant_colors", "cover_hooks", "ambience_fx", "rooms_visible"]


def load(pattern):
    out = {}
    for p in glob.glob(pattern):
        for r in json.load(open(p))["reels"]:
            if r.get("visual_status") == "ok" and isinstance(r.get("code"), dict):
                out[r["shortcode"]] = r["code"]
    return out


def kappa(a, b):
    cats = sorted(set(a) | set(b))
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    orig = load(os.path.join(ROOT, "data", "raw", "reels", "cover_*.json"))
    rel = load(os.path.join(ROOT, "data", "raw", "reliability", "cover_*.json"))
    common = sorted(set(orig) & set(rel))
    rows = []
    for f in SINGLE:
        a = [str(orig[s].get(f)).lower() for s in common]
        b = [str(rel[s].get(f)).lower() for s in common]
        rows.append({"field": f, "n": len(common), "agreement": round(sum(x == y for x, y in zip(a, b)) / max(1, len(a)), 3),
                     "cohen_kappa": round(kappa(a, b), 3) if common else None, "type": "categorical"})
    for f in LISTS:
        js = []
        for s in common:
            x, y = set(orig[s].get(f) or []), set(rel[s].get(f) or [])
            js.append(len(x & y) / len(x | y) if (x | y) else 1.0)
        rows.append({"field": f, "n": len(common), "agreement": round(sum(js) / max(1, len(js)), 3), "cohen_kappa": None, "type": "list (mean Jaccard)"})
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(ROOT, "data", "processed", "stats", "reliability.csv"), index=False)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
