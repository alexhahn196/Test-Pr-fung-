"""Setzt die Tabellen aus scripts/generated_tables.md in die Berichte ein.
Marker im Markdown:  <!-- TABLE:T1 START --> ... <!-- TABLE:T1 END -->   (python3 scripts/render.py)"""
import glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "scripts", "generated_tables.md"), encoding="utf-8").read()
parts = {}
for block in re.split(r"(?m)^## ", src)[1:]:
    key = block.split(" ", 1)[0]
    parts[key] = block.split("\n", 1)[1].strip()
for f in glob.glob(os.path.join(ROOT, "*.md")):
    txt = open(f, encoding="utf-8").read()
    new = re.sub(r"<!-- TABLE:(T\d+) START -->.*?<!-- TABLE:\1 END -->",
                 lambda m: f"<!-- TABLE:{m.group(1)} START -->\n{parts[m.group(1)]}\n<!-- TABLE:{m.group(1)} END -->", txt, flags=re.S)
    if new != txt:
        open(f, "w", encoding="utf-8").write(new)
        print("aktualisiert:", os.path.basename(f))
