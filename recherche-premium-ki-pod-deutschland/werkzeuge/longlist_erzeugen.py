#!/usr/bin/env python3
"""Erzeugt longlist.md aus rohdaten/longlist-workflow.json (+ shortlist-auswahl.json, endstatus.json).

Bestellungen für 1 Mio. € Jahresnettoumsatz = 1.000.000 / (Ø-Warenkorb brutto / 1,19).
Der Ø-Warenkorb ist eine SCHÄTZUNG der Kuratierung (Preisbelege in der Spalte "Warenkorb-Beleg").
"""
import json
import os

HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HIER, "..")
ROH = os.path.join(ROOT, "rohdaten")


def cell(s, n=300):
    s = " ".join(str(s).split()).replace("|", "/")
    return s if len(s) <= n else s[: n - 1] + "…"


def de(x, nk=0):
    return f"{x:,.{nk}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    wf = json.load(open(os.path.join(ROH, "longlist-workflow.json"), encoding="utf-8"))
    cur = wf["kuratierung"]
    sl = json.load(open(os.path.join(ROH, "shortlist-auswahl.json"), encoding="utf-8"))
    sl_map = {}
    for k in sl["kandidaten"]:
        for nr in k["longlist_nrs"]:
            sl_map[nr] = f"Shortlist {k['id']}"
    endstatus = {}
    fp = os.path.join(ROH, "endstatus.json")
    if os.path.exists(fp):
        endstatus = json.load(open(fp, encoding="utf-8"))
    ll = sorted(cur["longlist"], key=lambda e: -e["punkte_gesamt_100"])

    L = ["# Longlist – personalisierte Premium-Produktkategorien mit KI-Potenzial (Deutschland)", "",
         "Recherchedatum 01.10.2026. Erzeugt von `werkzeuge/longlist_erzeugen.py` aus `rohdaten/longlist-workflow.json` "
         "(9 Segment-Scouts, Lückenkritik, 2 Lückensuchen, Kuratierung). "
         f"{sum(len(s['kategorien']) for s in wf['segmente'])} Rohkategorien wurden zu {len(ll)} Kategorien zusammengeführt.", "",
         "**Lesehilfe:**", "",
         "- **Ø-Warenkorb brutto** ist eine SCHÄTZUNG für das beste Set-Angebot; die Preisbelege stehen in den Details.",
         "- **Bestellungen für 1 Mio. €** = 1.000.000 € ÷ (Ø-Warenkorb ÷ 1,19); Tag = Jahr ÷ 365.",
         "- **Punkte** = Vorbewertung der Kuratierung nach dem 100-Punkte-Raster: Wirtschaftlichkeit 30, Markt 20, KI-Mehrwert 15, Wettbewerb 15, Produktion 10, Social 10. "
         "Für die 10 Shortlist-Kandidaten gilt die Bewertung nach der Vertiefung (`shortlist.md`).",
         "- **Datensicherheit** separat: HOCH / MITTEL / NIEDRIG. **Ampel** vorläufig, Wettbewerb nach Auftragsdefinition.",
         "- Labels in den Belegen: BELEGT / ANBIETERANGABE / SCHÄTZUNG / ANNAHME.", "",
         "## Übersicht (sortiert nach Vorbewertung)", "",
         "| Nr | Kategorie | Segment | Ø-Warenkorb brutto | 1 Mio. €: Bestellungen/Jahr | /Monat | /Tag | Punkte W/M/K/Wb/P/S | Gesamt | Datensicherheit | Ampel | Status |",
         "|---:|---|---|---:|---:|---:|---:|---|---:|---|---|---|"]
    for e in ll:
        netto = e["aov_brutto_eur"] / 1.19
        jahr = 1_000_000 / netto
        pkt = f"{e['punkte_wirtschaft_30']}/{e['punkte_markt_20']}/{e['punkte_ki_15']}/{e['punkte_wettbewerb_15']}/{e['punkte_produktion_10']}/{e['punkte_social_10']}"
        status = endstatus.get(str(e["nr"])) or sl_map.get(e["nr"]) or e["empfehlung"]
        L.append(f"| {e['nr']} | {cell(e['kategorie'], 120)} | {e['segment']} | {de(e['aov_brutto_eur'])} € | {de(jahr)} | {de(jahr / 12)} | {de(jahr / 365, 1)} | {pkt} | {e['punkte_gesamt_100']} | {e['datensicherheit']} | {e['ampel_vorlaeufig']} | {cell(status, 120)} |")
    L += ["", "Hinweis zu Nr. 34 (Abibuch): Der Warenkorb ist ein Gruppenauftrag eines ganzen Jahrgangs; die Bestellzahl ist deshalb klein, der Vertriebsaufwand je Auftrag aber hoch.", "",
          "## Details je Kategorie", ""]
    for e in sorted(ll, key=lambda e: e["nr"]):
        status = endstatus.get(str(e["nr"])) or sl_map.get(e["nr"]) or e["empfehlung"]
        L += [f"### {e['nr']}. {e['kategorie']}", "",
              f"- **Segment / Herkunft:** {e['segment']} – {cell(e['herkunft'], 300)}",
              f"- **Produkt und Bundle:** {cell(e['produkt_und_bundle'], 900)}",
              f"- **Typischer Warenkorb:** ca. {de(e['aov_brutto_eur'])} € brutto (SCHÄTZUNG). Belege: {cell(e['aov_beleg'], 900)}",
              f"- **Zielgruppe:** {cell(e['zielgruppe'], 400)}",
              f"- **Kaufanlass:** {cell(e['kaufanlass'], 400)}",
              f"- **Personalisierung heute:** {cell(e['personalisierung_heute'], 600)}",
              f"- **Mögliche KI-Verbesserung:** {cell(e['ki_verbesserung'], 600)}",
              f"- **Produktionsmöglichkeit (EU):** {cell(e['produktion_eu'], 600)}",
              f"- **Vorhandene Konkurrenz:** {cell(e['konkurrenz'], 700)}",
              f"- **US-Vorbilder:** {cell(e['us_vorbilder'], 700)}",
              f"- **Nachfrage und Größe:** {cell(e['nachfrage_und_groesse'], 700)}",
              f"- **Wiederkauf / Produktwelt:** {cell(e['wiederkauf_produktwelt'], 400)}",
              f"- **Social-Creative:** {cell(e['social_creative'], 400)}",
              f"- **Vorbewertung:** {e['punkte_gesamt_100']}/100 (W {e['punkte_wirtschaft_30']}, M {e['punkte_markt_20']}, K {e['punkte_ki_15']}, Wb {e['punkte_wettbewerb_15']}, P {e['punkte_produktion_10']}, S {e['punkte_social_10']}); Datensicherheit {e['datensicherheit']}; Ampel {e['ampel_vorlaeufig']}",
              f"- **Status:** {status}. Begründung der Kuratierung: {cell(e['begruendung'], 600)}", ""]
    L += ["## Methodik", "", cell(cur["methodik_notiz"], 3000), "",
          "**Rohkategorien je Segment:** " + "; ".join(f"{s['segment']}: {len(s['kategorien'])}" for s in wf["segmente"]), ""]
    open(os.path.join(ROOT, "longlist.md"), "w", encoding="utf-8").write("\n".join(L))
    print("longlist.md geschrieben:", len(ll), "Kategorien")


if __name__ == "__main__":
    main()
