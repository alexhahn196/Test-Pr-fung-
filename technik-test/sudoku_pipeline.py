"""Technischer Machbarkeitstest: Sudoku-Großdruckbuch (Prototyp, lokal ausgeführt).

Stufen:
  1. Generator (zufälliges Vollgitter + Ausdünnen mit eigenem Backtracking-Zähler)
  2. Unabhängige Prüfung per SAT-Solver (anderer Algorithmus, andere Bibliothek)
  3. Schwierigkeitsbewertung per Logik-Löser (nur menschliche Techniken)
  4. Dublettenprüfung (auch über Symmetrien/Umbenennung der Ziffern)
  5. PDF-Satz (eingebettete TrueType-Schrift, Lösungsteil)
  6. Rückprüfung: Ziffern aus dem fertigen PDF extrahieren und erneut per SAT prüfen

Aufruf: python3 sudoku_pipeline.py [ANZAHL] [SEED]
Keine Netzwerkzugriffe, keine Veröffentlichung.
"""
import hashlib
import json
import random
import sys
from itertools import product

from pysat.solvers import Glucose3
from pypdf import PdfReader
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ---------------------------------------------------------------- 1. Generator
def candidates(g, r, c):
    used = set(g[r]) | {g[i][c] for i in range(9)}
    br, bc = 3 * (r // 3), 3 * (c // 3)
    used |= {g[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)}
    return [d for d in range(1, 10) if d not in used]


def count_solutions(g, limit=2):
    """Backtracking mit 'fewest candidates first'; bricht bei limit ab."""
    best, best_c = None, None
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                cs = candidates(g, r, c)
                if not cs:
                    return 0
                if best is None or len(cs) < len(best_c):
                    best, best_c = (r, c), cs
    if best is None:
        return 1
    r, c = best
    n = 0
    for d in best_c:
        g[r][c] = d
        n += count_solutions(g, limit - n)
        g[r][c] = 0
        if n >= limit:
            break
    return n


def full_grid(rng):
    g = [[0] * 9 for _ in range(9)]

    def fill(k=0):
        if k == 81:
            return True
        r, c = divmod(k, 9)
        cs = candidates(g, r, c)
        rng.shuffle(cs)
        for d in cs:
            g[r][c] = d
            if fill(k + 1):
                return True
        g[r][c] = 0
        return False

    fill()
    return g


def make_puzzle(rng, target_givens):
    sol = full_grid(rng)
    puz = [row[:] for row in sol]
    cells = list(product(range(9), range(9)))
    rng.shuffle(cells)
    givens = 81
    for r, c in cells:
        if givens <= target_givens:
            break
        keep = puz[r][c]
        puz[r][c] = 0
        if count_solutions([row[:] for row in puz]) != 1:
            puz[r][c] = keep
        else:
            givens -= 1
    return puz, sol

# ---------------------------------------------------------- 2. SAT-Prüfung
def var(r, c, d):
    return 81 * r + 9 * c + d  # d in 1..9 -> 1..729


def sat_clauses(puz):
    cl = []
    for r, c in product(range(9), range(9)):
        cl.append([var(r, c, d) for d in range(1, 10)])
        for d1 in range(1, 10):
            for d2 in range(d1 + 1, 10):
                cl.append([-var(r, c, d1), -var(r, c, d2)])
    units = [[(r, c) for c in range(9)] for r in range(9)]
    units += [[(r, c) for r in range(9)] for c in range(9)]
    units += [[(br + i, bc + j) for i in range(3) for j in range(3)]
              for br in (0, 3, 6) for bc in (0, 3, 6)]
    for u in units:
        for d in range(1, 10):
            cl.append([var(r, c, d) for r, c in u])
            for a in range(9):
                for b in range(a + 1, 9):
                    cl.append([-var(*u[a], d), -var(*u[b], d)])
    for r, c in product(range(9), range(9)):
        if puz[r][c]:
            cl.append([var(r, c, puz[r][c])])
    return cl


def sat_check(puz, sol):
    """Unabhängig vom Generator: (a) Lösung erfüllt alle Regeln und passt zu den Vorgaben,
    (b) es gibt KEINE zweite Lösung (Blockier-Klausel -> UNSAT)."""
    with Glucose3(bootstrap_with=sat_clauses(puz)) as s:
        if not s.solve():
            return False, "keine Lösung"
        model = {v for v in s.get_model() if v > 0}
        found = [[next(d for d in range(1, 10) if var(r, c, d) in model) for c in range(9)]
                 for r in range(9)]
        if found != sol:
            return False, "SAT-Lösung weicht von gespeicherter Lösung ab"
        s.add_clause([-var(r, c, sol[r][c]) for r, c in product(range(9), range(9))])
        if s.solve():
            return False, "mehrdeutig"
    return True, "eindeutig"

# ------------------------------------------------- 3. Schwierigkeit (Logik)
UNITS = ([[(r, c) for c in range(9)] for r in range(9)]
         + [[(r, c) for r in range(9)] for c in range(9)]
         + [[(br + i, bc + j) for i in range(3) for j in range(3)]
            for br in (0, 3, 6) for bc in (0, 3, 6)])
PEERS = {(r, c): {p for u in UNITS if (r, c) in u for p in u} - {(r, c)}
         for r, c in product(range(9), range(9))}


def logic_grade(puz):
    """Löst nur mit menschlichen Techniken. Rückgabe: höchste benötigte Stufe oder 'unlösbar'."""
    cand = {(r, c): ({puz[r][c]} if puz[r][c] else set(range(1, 10)))
            for r, c in product(range(9), range(9))}
    for cell, s in cand.items():
        if len(s) == 1 and puz[cell[0]][cell[1]]:
            for p in PEERS[cell]:
                cand[p].discard(next(iter(s)))
    level = 0

    def assign(cell, d):
        cand[cell] = {d}
        for p in PEERS[cell]:
            cand[p].discard(d)

    placed = {c for c, s in cand.items() if len(s) == 1}
    while len(placed) < 81:
        progress = False
        for cell, s in cand.items():               # Stufe 1: Naked Single
            if cell not in placed and len(s) == 1:
                assign(cell, next(iter(s)))
                placed.add(cell)
                progress = True
        if progress:
            continue
        for u in UNITS:                            # Stufe 1: Hidden Single
            for d in range(1, 10):
                spots = [c for c in u if d in cand[c]]
                if len(spots) == 1 and spots[0] not in placed:
                    assign(spots[0], d)
                    placed.add(spots[0])
                    progress = True
        if progress:
            continue
        for u in UNITS:                            # Stufe 2: Naked Pair
            open_cells = [c for c in u if len(cand[c]) == 2]
            for i in range(len(open_cells)):
                for j in range(i + 1, len(open_cells)):
                    a, b = open_cells[i], open_cells[j]
                    if cand[a] == cand[b]:
                        for c in u:
                            if c not in (a, b) and cand[c] & cand[a]:
                                cand[c] -= cand[a]
                                progress = True
        if not progress:                           # Stufe 2: Pointing (Block -> Zeile/Spalte)
            for bi in range(18, 27):
                box = UNITS[bi]
                for d in range(1, 10):
                    spots = [c for c in box if d in cand[c] and c not in placed]
                    if len(spots) < 2:
                        continue
                    rows = {r for r, _ in spots}
                    cols = {c for _, c in spots}
                    line = None
                    if len(rows) == 1:
                        line = UNITS[next(iter(rows))]
                    elif len(cols) == 1:
                        line = UNITS[9 + next(iter(cols))]
                    if line:
                        for c in line:
                            if c not in box and d in cand[c]:
                                cand[c].discard(d)
                                progress = True
        if progress:
            level = max(level, 2)
            continue
        return "schwer/unlösbar mit Basistechniken"
    return {0: "leicht", 2: "mittel"}.get(level, "leicht")

# ------------------------------------------------------ 4. Dublettenprüfung
def canonical(puz):
    """Kanonische Form über 8 Drehungen/Spiegelungen + Ziffern-Umbenennung
    (vereinfachte Variante; erkennt nicht alle Band/Stack-Permutationen)."""
    grids = []
    g = [row[:] for row in puz]
    for _ in range(4):
        g = [list(r) for r in zip(*g[::-1])]
        grids.append(g)
        grids.append([row[::-1] for row in g])
    keys = []
    for gg in grids:
        mapping, nxt, flat = {}, 1, []
        for v in (x for row in gg for x in row):
            if v and v not in mapping:
                mapping[v] = nxt
                nxt += 1
            flat.append(mapping.get(v, 0))
        keys.append("".join(map(str, flat)))
    return hashlib.sha256(min(keys).encode()).hexdigest()

# ------------------------------------------------------------ 5. PDF-Satz
PAGE_W, PAGE_H = 8.5 * inch, 11 * inch       # KDP-Standardformat 8,5 x 11 in, ohne Anschnitt
INSIDE, OUTSIDE, TOP = 0.875 * inch, 0.625 * inch, 0.9 * inch


def draw_grid(cv, grid, x0, y0, size, font_size, bold=True):
    cell = size / 9
    for i in range(10):
        cv.setLineWidth(3 if i % 3 == 0 else 1)
        cv.line(x0, y0 + i * cell, x0 + size, y0 + i * cell)
        cv.line(x0 + i * cell, y0, x0 + i * cell, y0 + size)
    cv.setFont("DVB" if bold else "DV", font_size)
    for r, c in product(range(9), range(9)):
        v = grid[r][c]
        if v:
            cx = x0 + c * cell + cell / 2
            cy = y0 + size - r * cell - cell / 2 - font_size * 0.35
            cv.drawCentredString(cx, cy, str(v))


def build_pdf(path, items):
    pdfmetrics.registerFont(TTFont("DV", FONT))
    pdfmetrics.registerFont(TTFont("DVB", FONT_BOLD))
    cv = canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H), initialFontName="DV")
    page = 1

    def margins():
        left = INSIDE if page % 2 == 1 else OUTSIDE
        return left, PAGE_W - left - (OUTSIDE if page % 2 == 1 else INSIDE)

    def footer():
        cv.setFont("DV", 14)
        cv.drawCentredString(PAGE_W / 2, 0.55 * inch, str(page))

    # Rätselseiten: 1 Rätsel pro Seite, Ziffern 30 pt (Großdruck)
    for n, it in enumerate(items, 1):
        left, width = margins()
        cv.setFont("DVB", 22)
        cv.drawString(left, PAGE_H - TOP, f"Rätsel {n}  ·  {it['grade']}")
        size = min(width, 6.6 * inch)
        draw_grid(cv, it["puzzle"], left + (width - size) / 2, 1.3 * inch, size, 30)
        footer()
        cv.showPage()
        page += 1
    # Lösungsteil: 4 Lösungen pro Seite, 16 pt
    for start in range(0, len(items), 4):
        left, width = margins()
        cv.setFont("DVB", 20)
        cv.drawString(left, PAGE_H - TOP, "Lösungen")
        size = 3.4 * inch
        for k, it in enumerate(items[start:start + 4]):
            col, row = k % 2, k // 2
            x = left + col * (width / 2) + (width / 2 - size) / 2
            y = PAGE_H - TOP - 0.45 * inch - (row + 1) * (size + 0.55 * inch)
            cv.setFont("DV", 13)
            cv.drawString(x, y + size + 0.12 * inch, f"Lösung {start + k + 1}")
            draw_grid(cv, it["solution"], x, y, size, 16, bold=False)
        footer()
        cv.showPage()
        page += 1
    cv.save()

# ------------------------------------------- 6. Rückprüfung aus dem PDF
def extract_digits(page_text):
    return [int(ch) for ch in page_text if ch.isdigit()]


def pdf_backcheck(path, items):
    """Liest die Rätselseiten aus dem fertigen PDF zurück und prüft die gedruckten
    Vorgaben gegen die Daten. Prüft außerdem Seitenformat und Schrifteinbettung."""
    reader = PdfReader(path)
    problems = []
    for n, it in enumerate(items):
        text = reader.pages[n].extract_text()
        body = text.split("\n", 1)[1] if "\n" in text else text
        digits = extract_digits(body)
        expected = [v for row in it["puzzle"] for v in row if v]
        # Die letzte Zahl ist die Seitenzahl.
        if digits[:len(expected)] != expected:
            problems.append(f"Seite {n + 1}: gedruckte Vorgaben weichen ab")
    # Lösungsteil zurücklesen: nach jedem "Lösung k" folgen 81 Ziffern
    sol_text = "\n".join(p.extract_text() for p in reader.pages[len(items):])
    import re
    blocks = re.split(r"Lösung (\d+)\n", sol_text)
    printed = {int(blocks[i]): extract_digits(blocks[i + 1])[:81] for i in range(1, len(blocks) - 1, 2)}
    for n, it in enumerate(items, 1):
        grid = printed.get(n)
        if grid is None or len(grid) != 81:
            problems.append(f"Lösung {n}: fehlt oder unvollständig im PDF")
            continue
        g = [grid[r * 9:(r + 1) * 9] for r in range(9)]
        if not sat_check(it["puzzle"], g)[0]:
            problems.append(f"Lösung {n}: gedruckte Lösung passt nicht zum gedruckten Rätsel")
    for i, p in enumerate(reader.pages):
        w, h = float(p.mediabox.width), float(p.mediabox.height)
        if abs(w - 612) > 0.5 or abs(h - 792) > 0.5:
            problems.append(f"Seite {i + 1}: Format {w}x{h} pt")
        fonts = p.get("/Resources", {}).get("/Font", {})
        for f in fonts.values():
            fo = f.get_object()
            desc = fo.get("/FontDescriptor")
            if fo.get("/Subtype") != "/Type3" and (desc is None or not any(
                    k in desc.get_object() for k in ("/FontFile", "/FontFile2", "/FontFile3"))):
                # Type0-Schriften tragen den Deskriptor im DescendantFont
                dfs = fo.get("/DescendantFonts")
                ok = False
                if dfs:
                    d = dfs[0].get_object().get("/FontDescriptor").get_object()
                    ok = any(k in d for k in ("/FontFile", "/FontFile2", "/FontFile3"))
                if not ok:
                    problems.append(f"Seite {i + 1}: Schrift nicht eingebettet: {fo.get('/BaseFont')}")
    return len(reader.pages), problems

# --------------------------------------------------------------- Ablauf
def main(n=20, seed=2026):
    rng = random.Random(seed)
    plan = ["leicht"] * (n // 2) + ["mittel"] * (n - n // 2)
    items, seen, log = [], set(), {"verworfen_schwierigkeit": 0, "verworfen_dublette": 0}
    for want in plan:
        while True:
            puz, sol = make_puzzle(rng, 36 if want == "leicht" else 28)
            ok, why = sat_check(puz, sol)
            if not ok:
                raise SystemExit(f"FEHLER Generator/SAT uneinig: {why}")
            grade = logic_grade(puz)
            if grade != want:
                log["verworfen_schwierigkeit"] += 1
                continue
            key = canonical(puz)
            if key in seen:
                log["verworfen_dublette"] += 1
                continue
            seen.add(key)
            givens = sum(1 for row in puz for v in row if v)
            items.append({"puzzle": puz, "solution": sol, "grade": grade, "givens": givens,
                          "key": key})
            break
    pdf = "testbuch_sudoku_grossdruck.pdf"
    build_pdf(pdf, items)
    pages, problems = pdf_backcheck(pdf, items)
    report = {
        "raetsel": len(items),
        "sat_eindeutig": sum(sat_check(i["puzzle"], i["solution"])[0] for i in items),
        "schwierigkeit": {g: sum(1 for i in items if i["grade"] == g) for g in ("leicht", "mittel")},
        "vorgaben_min_max": [min(i["givens"] for i in items), max(i["givens"] for i in items)],
        "dubletten": len(items) - len({i["key"] for i in items}),
        **log,
        "pdf_seiten": pages,
        "pdf_probleme": problems,
    }
    with open("testbericht.json", "w") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))

    # Negativtests: absichtlich fehlerhafte Fälle müssen erkannt werden
    bad = [row[:] for row in items[0]["puzzle"]]
    # Vorgaben entfernen, bis das Rätsel mehrdeutig wird
    for r, c in product(range(9), range(9)):
        if bad[r][c]:
            bad[r][c] = 0
            if count_solutions([row[:] for row in bad]) > 1:
                break
    wrong_sol = [row[:] for row in items[0]["solution"]]
    wrong_sol[0][0], wrong_sol[0][1] = wrong_sol[0][1], wrong_sol[0][0]
    neg = {
        "mehrdeutiges_raetsel_erkannt": not sat_check(bad, items[0]["solution"])[0],
        "falsche_loesung_erkannt": not sat_check(items[0]["puzzle"], wrong_sol)[0],
        "dublette_per_drehung_erkannt":
            canonical([list(r) for r in zip(*items[0]["puzzle"][::-1])]) == items[0]["key"],
    }
    print("Negativtests:", json.dumps(neg, ensure_ascii=False))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20,
         int(sys.argv[2]) if len(sys.argv) > 2 else 2026)
