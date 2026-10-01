#!/usr/bin/env python3
"""Extrahiert alle zitierten URLs aus den Rohdaten (rohdaten/*.json) in quellen-vollstaendig.md.

Jede URL erscheint einmal je Rohdatei mit der ersten gefundenen Aussage, Label und Datum,
sofern im JSON-Objekt vorhanden. Abrufdatum: 01.10.2026; Dateien mit Präfix vorarbeit- stammen aus der Recherche vom 30.09.2026.
"""
import json
import os
import re
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROH = os.path.join(HERE, "..", "rohdaten")
OUT = os.path.join(HERE, "..", "quellen-vollstaendig.md")
URL_RE = re.compile(r"https?://[^\s<>\"'\)\]\},;]+")

TEXT_KEYS = ("aussage", "befund", "thema", "was", "behauptung", "name", "nische", "produkt")
LABEL_KEYS = ("label",)
DATE_KEYS = ("veroeffentlicht", "datum")


def walk(obj, ctx, sink):
    if isinstance(obj, dict):
        text = next((str(obj[k]) for k in TEXT_KEYS if k in obj and isinstance(obj[k], str)), ctx.get("text", ""))
        label = next((str(obj[k]) for k in LABEL_KEYS if k in obj), ctx.get("label", ""))
        datum = next((str(obj[k]) for k in DATE_KEYS if k in obj), ctx.get("datum", ""))
        sub = {"text": text, "label": label, "datum": datum}
        for k, v in obj.items():
            if isinstance(v, str):
                for u in URL_RE.findall(v):
                    u = u.rstrip(".").replace("&amp;", "&")
                    if u not in sink:
                        sink[u] = sub
            else:
                walk(v, sub, sink)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, ctx, sink)
    elif isinstance(obj, str):
        for u in URL_RE.findall(obj):
            u = u.rstrip(".").replace("&amp;", "&")
            if u not in sink:
                sink[u] = ctx


def main():
    lines = ["# Vollständiges Quellenverzeichnis (automatisch extrahiert)", "",
             "Erzeugt von `werkzeuge/quellen_extrahieren.py` aus den Rohdaten der Recherche-Agenten. "
             "Abrufdatum der Web-Quellen: 01.10.2026 (Dateien mit Präfix `vorarbeit-`: 30.09.2026). Label = Kennzeichnung im Rohdatensatz "
             "(BELEGT / ANBIETERANGABE / SCHÄTZUNG / ANNAHME), soweit dort vergeben. Die im Bericht "
             "verwendeten Kernquellen stehen zusätzlich kuratiert in `quellen.md`.", ""]
    total = 0
    for root, _, files in os.walk(ROH):
        for fn in sorted(files):
            if not fn.endswith(".json"):
                continue
            path = os.path.join(root, fn)
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            sink = OrderedDict()
            walk(data, {"text": "", "label": "", "datum": ""}, sink)
            rel = os.path.relpath(path, os.path.join(HERE, ".."))
            lines += [f"## {rel} ({len(sink)} URLs)", "", "| # | URL | Kontext (gekürzt) | Label | Datum |", "|---:|---|---|---|---|"]
            for i, (u, c) in enumerate(sink.items(), 1):
                t = re.sub(r"\s+", " ", c.get("text", ""))[:140].replace("|", "/")
                lines.append(f"| {i} | <{u}> | {t} | {c.get('label', '')} | {str(c.get('datum', ''))[:40].replace('|', '/')} |")
            lines.append("")
            total += len(sink)
    lines.insert(4, f"Insgesamt {total} URL-Einträge (Duplikate zwischen Dateien möglich).")
    lines.insert(5, "")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"{total} URLs -> {OUT}")


if __name__ == "__main__":
    main()
