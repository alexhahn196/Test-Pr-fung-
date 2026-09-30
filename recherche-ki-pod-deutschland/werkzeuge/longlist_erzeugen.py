#!/usr/bin/env python3
"""Erzeugt kandidaten-longlist.md aus den Rohdaten (Longlist-Kuratierung + Vertiefungsrunden).

Eingaben: rohdaten/discovery-longlist.json, rohdaten/vertiefung-ergebnisse*.json,
          rohdaten/finalstatus.json (manuelle Endbewertung aus dem Bericht),
          rohdaten/nachsuche.json (Nachsuche nach übersehenen US-Vorbildern, Bericht Abschnitt H).
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ROH = os.path.join(ROOT, "rohdaten")


def cell(s, n=400):
    s = " ".join(str(s).split()).replace("|", "/")
    return s if len(s) <= n else s[: n - 1] + "…"


# Echt neue Kategorien aus der Nachsuche, die als Longlist-Nischen weitergeführt werden.
NACHSUCHE_NR = {"Gamestand": 26, "Nailzotica (House of Fleek LLC)": 27}
NACHSUCHE_NISCHE = {
    26: "KI-Teambanner für Jugendsport-Mannschaften zum Saisonstart (Einzeldruck, Vertrieb über Ligen)",
    27: "Per KI entworfene Press-on-Nägel als Einzelset",
}
NACHSUCHE_FERTIGUNG = {26: "Klassisches POD (Bannerdruck; Fertiger beim Vorbild nicht offengelegt)", 27: "Unklar"}


def lade_nachsuche():
    fp = os.path.join(ROH, "nachsuche.json")
    if not os.path.exists(fp):
        return None, {}
    ns = json.load(open(fp, encoding="utf-8"))
    roh = {a["name"]: a for f in ns["rohfunde"] for a in f["angebote"]}
    return ns, roh


def main():
    disc = json.load(open(os.path.join(ROH, "discovery-longlist.json"), encoding="utf-8"))
    cur = disc["curated"]
    vert = {}
    for fn in sorted(glob.glob(os.path.join(ROH, "vertiefung-ergebnisse*.json"))):
        for r in json.load(open(fn, encoding="utf-8")):
            vert[r["nr"]] = r
    final = {}
    fp = os.path.join(ROH, "finalstatus.json")
    if os.path.exists(fp):
        final = {int(k): v for k, v in json.load(open(fp, encoding="utf-8")).items()}

    L = ["# Kandidatenliste (Longlist) – KI-personalisierte POD-/Made-to-Order-Produkte", "",
         "Recherchedatum 30.09.2026. Erzeugt von `werkzeuge/longlist_erzeugen.py` aus den Rohdaten. "
         "Scores 1–5 (5 = sehr gut) in der Reihenfolge der Auftragsprioritäten: E = Einstiegschance trotz Konkurrenz, "
         "W = Wirtschaftlichkeit inkl. Kundengewinnung, N = Nachfrage & Übertragbarkeit, P = Einzelstückproduktion & Direktversand, "
         "K = Beherrschbarkeit KI/Automatisierung; DQ = Datenqualität (getrennt bewertet). "
         "„Vorauswahl“ = Bewertung der Kuratierung nach der Breitensuche; „Nach Vertiefung“ = Bewertung des adversarialen Prüfers "
         "(nur für vertiefte Nischen). Labels in den Belegen: BELEGT / ANBIETERANGABE / SCHÄTZUNG / ANNAHME.", "",
         "## Übersicht", "",
         "| Nr | Nische | US-Vorbild(er) | Fertigung | Vorauswahl E/W/N/P/K (DQ) | Empfehlung Vorauswahl | Nach Vertiefung: Ampel, E/W/N/P/K (DQ) | Endstatus |",
         "|---:|---|---|---|---|---|---|---|"]
    for e in cur["longlist"]:
        nr = e["nr"]
        vb = "; ".join(f"[{cell(v['name'], 60)}]({v['url']})" for v in e["us_vorbilder"][:3])
        pre = f"{e['score_einstieg']}/{e['score_wirtschaftlichkeit']}/{e['score_nachfrage_uebertragbarkeit']}/{e['score_produktion']}/{e['score_ki_beherrschbarkeit']} ({e['datenqualitaet']})"
        post = "–"
        if nr in vert and vert[nr].get("skeptic"):
            s = vert[nr]["skeptic"]
            m = vert[nr].get("market") or {}
            post = (f"Markt: {m.get('ampel', '–')} → Prüfer: **{s['ampel_korrigiert']}**, "
                    f"{s['score_einstieg']}/{s['score_wirtschaftlichkeit']}/{s['score_nachfrage']}/{s['score_produktion']}/{s['score_ki']} ({s['datenqualitaet']})")
        L.append(f"| {nr} | {cell(e['nische'], 140)} | {vb} | {e['fertigungsart']} | {pre} | {e['empfehlung']} | {post} | {cell(final.get(nr, '–'), 160)} |")
    ns, roh = lade_nachsuche()
    neue = []
    if ns:
        for b in ns["abgleich"]["bewertungen"]:
            if b["name"] in NACHSUCHE_NR:
                neue.append((NACHSUCHE_NR[b["name"]], b, roh.get(b["name"], {})))
        for nr, b, r in sorted(neue, key=lambda x: x[0]):
            L.append(f"| {nr} | {NACHSUCHE_NISCHE[nr]} (aus Nachsuche) | [{cell(b['name'], 60)}]({b['url']}) | {NACHSUCHE_FERTIGUNG[nr]} | – (nicht vorab bewertet) | {b['empfehlung']} | – | {cell(final.get(nr, b['empfehlung']), 160)} |")
    L.append("")
    L += ["## Details je Nische", ""]
    for e in cur["longlist"]:
        nr = e["nr"]
        L += [f"### {nr}. {e['nische']}", "",
              f"- **US-Vorbilder:** " + "; ".join(f"[{v['name']}]({v['url']})" for v in e["us_vorbilder"]),
              f"- **Produkt:** {cell(e['produkt'], 700)}",
              f"- **KI-Ablauf für Kunden:** {cell(e['ki_ablauf'], 700)}",
              f"- **Kaufanlass:** {cell(e['kaufanlass'], 400)}",
              f"- **Preise (US):** {cell(e['preisspanne_us'], 400)}",
              f"- **Nachfragebelege:** {cell(e['nachfrage_zusammenfassung'], 1600)}",
              f"- **Wachstum April–September 2026:** {cell(e['wachstum_6m'], 700)}",
              f"- **KI-Burggraben:** {cell(e['ki_burggraben'], 500)}",
              f"- **Fertigungsart:** {e['fertigungsart']}",
              f"- **Vorläufige DE-Konkurrenz (Vorauswahl):** {cell(e['vorlaeufige_de_konkurrenz'], 700)}",
              f"- **Begründung der Vorauswahl:** {cell(e['begruendung'], 700)}"]
        if nr in vert and vert[nr].get("skeptic"):
            s = vert[nr]["skeptic"]
            L.append(f"- **Ergebnis der Vertiefung (adversarialer Prüfer):** Ampel {s['ampel_korrigiert']}, finalisttauglich: {'ja' if s['finalist_tauglich'] else 'nein'}. "
                     f"Wichtigste Unsicherheit: {cell(s['wichtigste_unsicherheit'], 600)}")
        if nr in final:
            L.append(f"- **Endstatus im Bericht:** {final[nr]}")
        L.append("")
    for nr, b, r in sorted(neue, key=lambda x: x[0]):
        L += [f"### {nr}. {NACHSUCHE_NISCHE[nr]} (aus der Nachsuche)", "",
              f"- **US-Vorbild:** [{b['name']}]({b['url']}) – Sitz: {cell(r.get('sitz', '–'), 300)}",
              f"- **Produkt:** {cell(r.get('produkt', '–'), 700)}",
              f"- **KI-Ablauf für Kunden:** {cell(r.get('ki_ablauf_kunde', '–'), 700)}",
              f"- **Kaufanlass:** {cell(r.get('kaufanlass', '–'), 400)}",
              f"- **Preise (US):** {cell(r.get('preis', '–'), 400)}",
              f"- **Nachfragebelege (Abgleich):** {cell(b['nachfrage_staerke'], 1600)}",
              f"- **Wachstum April–September 2026 (Rohfund):** {cell(r.get('wachstum_2026', '–'), 700)}",
              f"- **KI-Burggraben:** {cell(r.get('ki_burggraben', '–'), 500)}",
              f"- **Fertigung beim Vorbild:** {cell(r.get('fertigung', '–'), 400)}",
              f"- **Einschätzung DE:** {cell(b['de_einschaetzung'], 1200)}",
              f"- **Empfehlung:** {b['empfehlung']}. {cell(b['begruendung'], 1200)}"]
        if nr in final:
            L.append(f"- **Endstatus im Bericht:** {final[nr]}")
        L.append("")
    if ns:
        L += ["## Alle Funde der Nachsuche (Bericht Abschnitt H)", "",
              "Abgleich gegen Longlist und Finalisten; „neu“ = keine Variante einer bestehenden Nische.", "",
              "| Fund | Einordnung | neu | Nachfragebeleg (Abgleich) | Empfehlung |", "|---|---|---|---|---|"]
        for b in ns["abgleich"]["bewertungen"]:
            L.append(f"| [{cell(b['name'], 70)}]({b['url']}) | {cell(b['nische'], 220)} | {'ja' if b['neu'] else 'nein'} | {cell(b['nachfrage_staerke'], 420)} | {b['empfehlung']} |")
        L += ["", "**Gesamtfazit des Abgleichs:** " + cell(ns["abgleich"]["gesamtfazit"], 4000), ""]
    L += ["## Vor der Longlist ausgeschlossene Rohfunde", "", "| Rohfund | Grund |", "|---|---|"]
    for x in cur["ausgeschlossen_vor_longlist"]:
        L.append(f"| {cell(x['name'], 120)} | {cell(x['grund'], 400)} |")
    L += ["", "## Methodik der Longlist", "", cell(cur["methodik_notiz"], 4000), ""]
    open(os.path.join(ROOT, "kandidaten-longlist.md"), "w", encoding="utf-8").write("\n".join(L))
    print("kandidaten-longlist.md geschrieben")


if __name__ == "__main__":
    main()
