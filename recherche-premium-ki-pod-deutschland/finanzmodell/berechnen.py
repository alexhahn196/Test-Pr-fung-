#!/usr/bin/env python3
"""Rechnet alle Finalisten aus parameter.py durch und schreibt die Ergebnisdateien.

Aufruf (aus diesem Ordner):  python3 berechnen.py
Ausgabe: ergebnisse.md, ergebnisse.json, cac_matrix.csv, skalierung.csv
"""
import csv
import json
import os

from modell import (CAC_STUFEN, ZIELE, einheit, cac_matrix, skalierung, sensitivitaet, testbudget, fmt)
from parameter import PRODUKTE, SZENARIEN, REF_CAC, PARAMETER_QUELLEN, TESTPLAN

HIER = os.path.dirname(os.path.abspath(__file__))
SZ_REIHE = ["Konservativ", "Basis", "Optimistisch"]

EINHEIT_ZEILEN = [
    ("Warenkorb brutto (inkl. 19 % USt.)", "warenkorb_brutto", 2),
    ("davon Upsells brutto", "davon_upsells_brutto", 2),
    ("Umsatzsteuer", "ust", 2),
    ("**Nettoumsatz je Bestellung**", "umsatz_netto", 2),
    ("Produkte je Bestellung", "produkte_je_bestellung", 2),
    ("Sendungen je Bestellung", "sendungen_je_bestellung", 2),
    ("Produktion (Partner, netto)", "herstellung", 2),
    ("Versand an Kunden (Partner)", "versand", 2),
    ("Verpackung/Beilage", "verpackung", 2),
    ("Zahlungsgebühren", "zahlung", 2),
    ("KI: Vorschauen der Nichtkäufer (umgelegt)", "ki_vorschau_nichtkaeufer", 2),
    ("KI: Vorschau, Änderungen, Finalisierung der Käufer", "ki_kaeufer", 2),
    ("Infrastruktur variabel (Speicher, Hosting, Mail)", "infrastruktur", 2),
    ("Menschliche Qualitätsprüfung", "pruefung", 2),
    ("Kundenservice", "support", 2),
    ("Ersatzproduktionen (Erwartungswert)", "nachdruck", 2),
    ("Erstattungen (Erwartungswert)", "erstattung", 2),
    ("Summe variable Kosten", "variable_kosten", 2),
    ("**DB I je Bestellung (vor CAC)**", "db1", 2),
    ("DB-I-Quote vom Nettoumsatz", "db1_quote", None),
    ("**Max. tragbarer CAC = Break-even-CAC (Erstkauf)**", "max_cac_erstkauf", 2),
    ("Max. tragbarer CAC inkl. Folgekäufe 12 Monate", "max_cac_inkl_wiederkauf_12m", 2),
    ("Vorschau-Sitzungen je Bestellung", "vorschau_sitzungen_je_bestellung", 1),
]


def zelle(e, key, nk):
    v = e[key]
    if nk is None:
        return f"{fmt(v * 100, 1)} %"
    return fmt(v, nk)


def main():
    md = ["# Finanzmodell – Ergebnisse", "",
          "Automatisch erzeugt von `berechnen.py` aus `parameter.py` (Rechenkern `modell.py`). "
          "Alle Beträge in €, netto ohne Umsatzsteuer, sofern nicht als brutto bezeichnet. "
          "Kennzeichnung der Eingaben in der Parametertabelle je Finalist; alles ohne Quelle ist ANNAHME. "
          "Die Ergebnisse sind Rechenwerte aus diesen Eingaben, keine Prognosen.", "",
          "**Lesehilfe:** DB I = Deckungsbeitrag vor Kundengewinnung. Max. tragbarer CAC = Break-even-CAC = DB I der Erstbestellung. "
          "Operatives Ergebnis = DB I − Kundengewinnung (Neukunden × CAC) − Fixkosten inkl. angestellter Mitarbeitender, "
          "vor Ertragsteuern und vor Gründerlohn. Skalierung = eingeschwungenes Jahr ohne Anlaufverluste.", ""]
    alle = {}
    cac_rows, sk_rows = [], []
    for key, p in PRODUKTE.items():
        szs = SZENARIEN[key]
        es = {n: einheit(p, szs[n]) for n in SZ_REIHE}
        alle[key] = {"name": p.name, "szenarien": {}}
        md += [f"## {p.name}", "", "### Stückrechnung je Bestellung", "",
               "| Position | " + " | ".join(SZ_REIHE) + " |", "|---|" + "---:|" * len(SZ_REIHE)]
        for label, k, nk in EINHEIT_ZEILEN:
            md.append(f"| {label} | " + " | ".join(zelle(es[n], k, nk) for n in SZ_REIHE) + " |")
        md.append("")
        md += ["**Angebote (Bruttopreis, Einkauf netto, Versand netto) und Mix je Szenario:**", "",
               "| Angebot | Preis brutto | Einkauf netto | Versand netto | Produkte | " + " | ".join(f"Mix {n}" for n in SZ_REIHE) + " |",
               "|---|---:|---:|---:|---:|" + "---:|" * len(SZ_REIHE)]
        for a in p.angebote:
            md.append(f"| {a.name} | {fmt(a.preis_brutto, 2)} | {fmt(a.einkauf, 2)} | {fmt(a.versand, 2)} | {fmt(a.artikel, 1)} | "
                      + " | ".join(f"{fmt(szs[n].mix.get(a.name, 0) * 100, 0)} %" for n in SZ_REIHE) + " |")
        if p.upsells:
            md += ["", "| Upsell | Preis brutto | Einkauf netto | Quote Basis |", "|---|---:|---:|---:|"]
            for u in p.upsells:
                md.append(f"| {u.name} | {fmt(u.preis_brutto, 2)} | {fmt(u.einkauf_netto + u.versand_netto, 2)} | {fmt(u.quote * szs['Basis'].upsell_faktor * 100, 0)} % |")
        md.append("")

        md += ["### CAC-Szenarien je Neukunde", "",
               "| CAC | " + " | ".join(f"Gewinn je Erstbestellung {n}" for n in SZ_REIHE) + " | Gewinn je Kunde inkl. Folgekäufe (Basis) | Marketingquote vom Netto (Basis) |",
               "|---:|" + "---:|" * (len(SZ_REIHE) + 2)]
        mats = {n: cac_matrix(es[n], szs[n]) for n in SZ_REIHE}
        for i, cac in enumerate(CAC_STUFEN):
            md.append(f"| {cac} € | " + " | ".join(fmt(mats[n][i]["gewinn_je_erstbestellung"], 2) for n in SZ_REIHE)
                      + f" | {fmt(mats['Basis'][i]['gewinn_je_kunde_12m'], 2)} | {fmt(mats['Basis'][i]['marketingquote_vom_netto'] * 100, 1)} % |")
            for n in SZ_REIHE:
                cac_rows.append({"produkt": key, "szenario": n, **mats[n][i]})
        md += ["", f"Break-even-CAC (Erstkauf): Konservativ {fmt(es['Konservativ']['max_cac_erstkauf'], 2)} €, "
               f"Basis {fmt(es['Basis']['max_cac_erstkauf'], 2)} €, Optimistisch {fmt(es['Optimistisch']['max_cac_erstkauf'], 2)} €. "
               f"Realistischer Referenz-CAC für dieses Produkt (Basis, siehe Parameter): {fmt(REF_CAC[key], 0)} €.", ""]

        md += ["### Skalierung: benötigte Bestellungen und Ergebnis (eingeschwungenes Jahr)", ""]
        for n in SZ_REIHE:
            sk = skalierung(p, es[n], szs[n])
            alle[key]["szenarien"][n] = {"einheit": es[n], "cac_matrix": mats[n], "skalierung": sk}
            cacs = [c["cac"] for c in sk[0]["je_cac"]]
            kopf = [f"Ergebnis bei CAC {fmt(c)} €" + (" (realistisch)" if c == szs[n].cac_realistisch else "") for c in cacs]
            md += [f"**{n}** (realistischer CAC in diesem Szenario: {fmt(szs[n].cac_realistisch)} €)", "",
                   "| Jahresnettoumsatz | Bestellungen/Jahr | /Monat | /Tag | /Tag im Spitzenmonat | Neukunden/Jahr | DB I gesamt | Fixkosten | QA+Support-Stellen | "
                   + " | ".join(kopf) + " |",
                   "|---:|---:|---:|---:|---:|---:|---:|---:|---:|" + "---:|" * len(cacs)]
            for z in sk:
                md.append(f"| {fmt(z['ziel_umsatz_netto'])} | {fmt(z['bestellungen_jahr'])} | {fmt(z['bestellungen_monat'])} | {fmt(z['bestellungen_tag'], 1)} | "
                          f"{fmt(z['bestellungen_tag_spitzenmonat'], 1)} | {fmt(z['neukunden_jahr'])} | {fmt(z['db1_gesamt'])} | {fmt(z['fixkosten'])} | {fmt(z['qa_support_vollzeitstellen'], 1)} | "
                          + " | ".join(fmt(c['operatives_ergebnis']) for c in z['je_cac']) + " |")
                for c in z["je_cac"]:
                    sk_rows.append({"produkt": key, "szenario": n, "ziel": z["ziel_umsatz_netto"], "bestellungen_jahr": round(z["bestellungen_jahr"]),
                                    "bestellungen_monat": round(z["bestellungen_monat"], 1), "bestellungen_tag": round(z["bestellungen_tag"], 2),
                                    "db1_gesamt": round(z["db1_gesamt"]), "fixkosten": z["fixkosten"], "cac": c["cac"],
                                    "kundengewinnung": round(c["kundengewinnung"]), "operatives_ergebnis": round(c["operatives_ergebnis"]),
                                    "umsatzrendite": round(c["umsatzrendite"], 4), "nach_gruenderlohn": round(c["nach_gruenderlohn"])})
            md.append("")
        md += [f"Gründerlohn kalkulatorisch: {fmt(szs['Basis'].gruenderlohn_jahr)} € p. a. (in den Tabellen nicht abgezogen; Werte nach Gründerlohn in `skalierung.csv`).", ""]

        sens = sensitivitaet(p, szs["Basis"], REF_CAC[key])
        alle[key]["sensitivitaet_basis"] = sens
        md += [f"### Sensitivität (Basis, 1 Mio. € Nettoumsatz, Referenz-CAC {fmt(REF_CAC[key])} €)", "",
               "| Fall | DB I je Bestellung | Max. CAC | Operatives Ergebnis p. a. | Veränderung |", "|---|---:|---:|---:|---:|"]
        for r in sens:
            md.append(f"| {r['fall']} | {fmt(r['db1'], 2)} | {fmt(r['max_cac'], 2)} | {fmt(r['ergebnis_1mio'])} | {fmt(r['delta'])} |")
        md.append("")

        md += ["### Eingaben und Kennzeichnung", "", "| Parameter | Wert | Label | Quelle/Begründung |", "|---|---|---|---|"]
        for (pk, name, wert, label, quelle) in PARAMETER_QUELLEN:
            if pk == key:
                md.append(f"| {name} | {wert} | {label} | {quelle} |")
        md += ["", "---", ""]

    if TESTPLAN:
        md += ["## Testrechnung für den 14-Tage-Test (Platz 1)", "",
               "| Fall | Conversion Besuch→Kauf | CPC | Ziel-Bestellungen | Benötigte Besucher | Werbebudget | Impliziter CAC |",
               "|---|---:|---:|---:|---:|---:|---:|"]
        tp_out = []
        for fall in TESTPLAN["faelle"]:
            t = testbudget(fall["conversion"], fall["cpc"], fall["bestellungen"])
            tp_out.append({**fall, **t})
            md.append(f"| {fall['name']} | {fmt(fall['conversion'] * 100, 2)} % | {fmt(fall['cpc'], 2)} € | {fmt(fall['bestellungen'])} | "
                      f"{fmt(t['besucher'])} | {fmt(t['budget'])} € | {fmt(t['cac_impliziert'], 2)} € |")
        md += ["", TESTPLAN.get("hinweis", ""), ""]
        alle["_testplan"] = tp_out

    open(os.path.join(HIER, "ergebnisse.md"), "w", encoding="utf-8").write("\n".join(md))
    json.dump(alle, open(os.path.join(HIER, "ergebnisse.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=float)
    for fn, rows in (("cac_matrix.csv", cac_rows), ("skalierung.csv", sk_rows)):
        with open(os.path.join(HIER, fn), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    print("ergebnisse.md, ergebnisse.json, cac_matrix.csv, skalierung.csv geschrieben")


if __name__ == "__main__":
    main()
