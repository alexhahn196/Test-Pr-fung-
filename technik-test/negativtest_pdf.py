"""Negativtest der PDF-Rückprüfung: absichtlich fehlerhaftes PDF muss erkannt werden."""
import copy
import random

import sudoku_pipeline as sp

rng = random.Random(1)
items = []
for _ in range(4):
    p, s = sp.make_puzzle(rng, 34)
    items.append({"puzzle": p, "solution": s, "grade": sp.logic_grade(p)})
bad = copy.deepcopy(items)
sol = bad[2]["solution"]
sol[4][4], sol[4][5] = sol[4][5], sol[4][4]      # Satzfehler im Lösungsteil
bad[1]["puzzle"][0] = [0] * 9                     # gedruckte Vorgaben unvollständig
sp.build_pdf("negativtest.pdf", bad)
pages, problems = sp.pdf_backcheck("negativtest.pdf", items)
print(problems)
assert any("Seite 2" in p for p in problems), "Vorgabenfehler nicht erkannt"
assert any("Lösung 3" in p for p in problems), "Lösungsfehler nicht erkannt"
print("Negativtest PDF: beide eingebauten Fehler erkannt")
