"""QA: broken relative links in the markdown deliverables + originality of generated hooks/ideas.

Originality: every English hook/title/overlay line we generated (07_hooks.md quoted lines, 12_100_content_ideas.csv
hook/titel/text_overlay/visual_hook columns) is compared with all observed caption first lines and cover texts in
04_reel_database.csv. difflib ratio >= 0.85 -> flagged as too close to an existing creative.
"""
import difflib
import glob
import os
import re

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_links():
    bad = []
    for md in glob.glob(os.path.join(ROOT, "*.md")) + glob.glob(os.path.join(ROOT, "quellen", "*.md")):
        txt = re.sub(r"`[^`]*`", "", open(md, encoding="utf-8").read())  # ignore inline code
        for m in re.finditer(r"\]\(([^)\s]+)\)", txt):
            target = m.group(1).split("#")[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            path = os.path.normpath(os.path.join(os.path.dirname(md), target))
            if not os.path.exists(path):
                bad.append((os.path.relpath(md, ROOT), target))
    return bad


def observed_lines():
    df = pd.read_csv(os.path.join(ROOT, "04_reel_database.csv"), usecols=["caption_first_line", "cover_text", "handle"], low_memory=False)
    obs = []
    for col in ["caption_first_line", "cover_text"]:
        for v, h in zip(df[col], df["handle"]):
            if isinstance(v, str) and len(v.strip()) >= 12:
                obs.append((v.strip().lower(), h))
    return obs


def generated_lines():
    gen = []
    p = os.path.join(ROOT, "12_100_content_ideas.csv")
    if os.path.exists(p):
        ideas = pd.read_csv(p)
        for col in [c for c in ideas.columns if c in ("hook", "titel", "text_overlay", "visual_hook_first_2s")]:
            gen += [("12_ideas:" + col, str(v)) for v in ideas[col].dropna()]
    p = os.path.join(ROOT, "07_hooks.md")
    if os.path.exists(p):
        for m in re.finditer(r"[\"“„]([A-Z][^\"”“]{11,140})[\"”“]", open(p, encoding="utf-8").read()):
            gen.append(("07_hooks", m.group(1)))
    return gen


def main():
    bad = check_links()
    print(f"broken links: {len(bad)}")
    for b in bad:
        print("  ", b)
    obs = observed_lines()
    flagged = []
    for src, g in generated_lines():
        gl = g.lower().strip()
        for o, h in obs:
            if abs(len(o) - len(gl)) > 40:
                continue
            r = difflib.SequenceMatcher(None, gl, o).ratio()
            if r >= 0.85:
                flagged.append((src, g, o, h, round(r, 2)))
                break
    print(f"generated lines checked: {len(generated_lines())} | too close to observed creatives: {len(flagged)}")
    for f in flagged:
        print("  ", f)


if __name__ == "__main__":
    main()
