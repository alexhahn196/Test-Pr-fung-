#!/usr/bin/env python3
"""
Finanzmodell für KI-personalisierte POD-/Made-to-Order-Finalisten (Deutschland).

Aufruf:  python3 finanzmodell.py            -> schreibt ergebnisse.md, ergebnisse.json, monate.csv
         python3 finanzmodell.py --print    -> zusätzlich Ausgabe auf stdout

Grundprinzipien (siehe auch README im Bericht):
- Bestellungen werden aus Kundengewinnung abgeleitet (Besuche -> Gestaltungsstarts -> Bestellungen),
  nicht aus einem Anteil am Gesamtmarkt.
- Werbeausgaben werden GENAU EINMAL als Kosten gebucht. CAC ist eine abgeleitete Kennzahl
  (Marketingausgaben / Neukunden) und wird nicht zusätzlich abgezogen.
- Organische Reichweite ist nicht kostenlos: sie entsteht nur mit laufenden Content-Kosten
  und wächst begrenzt (Rampe mit Obergrenze).
- Manuelle Prüf-/Supportzeit wird als variable Kosten zu einem Fremdleistungs-Stundensatz
  bewertet (Minijob/Freelancer). Der kalkulatorische Unternehmerlohn deckt Leitung, Marketing,
  Entwicklung – nicht diese Stunden -> keine Doppelzählung.
- Alle Eingaben ohne Quellenangabe in PARAMETER_QUELLEN sind ANNAHMEN.
"""
from __future__ import annotations

import csv
import json
import os
import sys
from dataclasses import dataclass, field, replace, asdict
from typing import Dict, List

HERE = os.path.dirname(os.path.abspath(__file__))
UST = 0.19


# ---------------------------------------------------------------------------
# Datenstrukturen
# ---------------------------------------------------------------------------
@dataclass
class Produkt:
    key: str
    name: str
    # Verkauf
    preis_brutto: float               # Ø Warenkorb inkl. USt (inkl. evtl. Versandanteil)
    # Variable Kosten je Bestellung (netto, €)
    herstellung: float                # Einkaufspreis Partner
    versand: float                    # Versand an Endkunde
    verpackung_beilage: float         # eigene Beilage, Zusatzverpackung, Branding-Aufpreis
    ki_kosten_je_generierung: float   # € je Bild-/Varianten-Generierung (Vorschau)
    gen_je_kaeufer: float             # Generierungen einer Sitzung, die bestellt
    gen_je_nichtkaeufer: float        # Generierungen einer Sitzung ohne Bestellung
    ki_produktionsdatei: float        # € je Bestellung (Upscaling/3D-Modell/Vektor/Farbauszug)
    pruef_minuten: float              # manuelle Prüfung/Nacharbeit Produktionsdatei je Bestellung
    support_minuten: float            # Kundenservice je Bestellung
    nachdruck_quote: float            # Anteil Bestellungen mit kostenloser Ersatzlieferung
    erstattung_quote: float           # Anteil Bestellungen mit (Teil-)Erstattung ohne Nachdruck
    erstattung_anteil: float          # Anteil des Nettoumsatzes, der bei Erstattung verloren geht
    partner_traegt_anteil_nachdruck: float  # Anteil der Nachdrucke, die Partner (Produktionsfehler) trägt
    # Fixkosten (monatlich, netto) und Einmalkosten
    fixkosten_monat: float
    einmalig_aufbau: float            # vollständige Aufbaukosten (ohne eigene Arbeitszeit)
    testbudget: float                 # Budget für den 14-Tage-Test + erste Musterbestellungen


@dataclass
class Szenario:
    name: str
    cpc: float                        # € je bezahltem Klick (Mischwert Meta/Pinterest/Google)
    start_quote: float                # Anteil Besucher, die einen KI-Entwurf starten
    bestell_quote: float              # Anteil Gestaltungsstarts, die bestellen
    lernkurve_start: float            # Faktor auf Conversion in Monat 1 (steigt linear bis Monat 4 auf 1,0)
    werbebudget_plan: List[float]     # geplantes Werbebudget Monat 1..12 (netto)
    werbe_gate: bool                  # True: Budget wächst nur, wenn Vormonat Paid-Deckungsbeitrag >= 0
    organisch_max: float              # organische Besuche/Monat nach Rampe (Obergrenze)
    organisch_rampe_monate: int       # Monate bis Obergrenze erreicht
    content_kosten_monat: float       # laufende Content-/Creator-/Musterkosten (netto)
    wiederkauf_quote_monat: float     # Anteil bisheriger Kunden, die pro Monat erneut bestellen
    preis_faktor: float = 1.0         # Anpassung Ø Warenkorb
    gen_faktor: float = 1.0           # Anpassung Generierungen je Sitzung
    nachdruck_faktor: float = 1.0     # Anpassung Nachdruckquote
    unternehmerlohn_monat: float = 2500.0  # kalkulatorisch (ANNAHME: ~0,6 FTE)
    stundensatz_fremd: float = 22.0   # € je Stunde Prüf-/Supportzeit (Minijob/Freelancer inkl. Nebenkosten)
    zahl_prozent: float = 0.019       # Zahlungsgebühr prozentual (Mischsatz, ANNAHME bis Quelle)
    zahl_fix: float = 0.25            # Zahlungsgebühr fix je Transaktion
    liquiditaetsreserve_monate: float = 1.0  # Reserve in Monaten Fixkosten+Werbung


# ---------------------------------------------------------------------------
# Kernrechnung
# ---------------------------------------------------------------------------
def einheitswerte(p: Produkt, s: Szenario) -> Dict[str, float]:
    """Deckungsbeitrag je Bestellung (vor Kundengewinnung), inkl. anteiliger Nichtkäufer-KI-Kosten."""
    brutto = p.preis_brutto * s.preis_faktor
    netto = brutto / (1 + UST)
    zahl = brutto * s.zahl_prozent + s.zahl_fix
    ki_kaeufer = p.gen_je_kaeufer * s.gen_faktor * p.ki_kosten_je_generierung
    # Nichtkäufer je Bestellung: (1/bestell_quote - 1) Sitzungen ohne Kauf
    nichtkaeufer_je_bestellung = (1.0 / s.bestell_quote) - 1.0
    ki_nichtkaeufer = nichtkaeufer_je_bestellung * p.gen_je_nichtkaeufer * s.gen_faktor * p.ki_kosten_je_generierung
    arbeit = (p.pruef_minuten + p.support_minuten) / 60.0 * s.stundensatz_fremd
    nachdruck_q = min(p.nachdruck_quote * s.nachdruck_faktor, 0.9)
    nachdruck_kosten_voll = p.herstellung + p.versand + p.verpackung_beilage + p.pruef_minuten / 60.0 * s.stundensatz_fremd
    nachdruck = nachdruck_q * (1 - p.partner_traegt_anteil_nachdruck) * nachdruck_kosten_voll
    erstattung = p.erstattung_quote * s.nachdruck_faktor * p.erstattung_anteil * netto
    variabel = (p.herstellung + p.versand + p.verpackung_beilage + zahl + ki_kaeufer + ki_nichtkaeufer
                + p.ki_produktionsdatei + arbeit + nachdruck + erstattung)
    db1 = netto - variabel
    return {
        "preis_brutto": brutto, "umsatz_netto": netto, "herstellung": p.herstellung, "versand": p.versand,
        "verpackung": p.verpackung_beilage, "zahlungsgebuehr": zahl, "ki_kaeufer": ki_kaeufer,
        "ki_nichtkaeufer": ki_nichtkaeufer, "ki_produktionsdatei": p.ki_produktionsdatei,
        "pruef_support_arbeit": arbeit, "nachdruck": nachdruck, "erstattung": erstattung,
        "variable_kosten": variabel, "db1": db1, "db1_quote": db1 / netto if netto else 0.0,
        "max_cac_erstkauf": db1,
    }


def simuliere(p: Produkt, s: Szenario, monate: int = 12) -> Dict:
    ew = einheitswerte(p, s)
    zeilen = []
    kunden_kumuliert = 0.0
    kasse = -p.einmalig_aufbau  # Monat 0: Aufbau
    kasse_min = kasse
    budget_vormonat = None
    paid_db_vormonat = None
    for m in range(1, monate + 1):
        plan = s.werbebudget_plan[m - 1]
        if s.werbe_gate and m > 1 and paid_db_vormonat is not None and paid_db_vormonat < 0:
            werbung = min(plan, budget_vormonat)  # kein Wachstum, solange Paid unprofitabel
        else:
            werbung = plan
        lern = min(1.0, s.lernkurve_start + (1.0 - s.lernkurve_start) * (m - 1) / 3.0)
        start_q = s.start_quote
        bestell_q = s.bestell_quote * lern
        paid_besuche = werbung / s.cpc if s.cpc > 0 else 0.0
        org_besuche = s.organisch_max * min(1.0, m / max(1, s.organisch_rampe_monate))
        besuche = paid_besuche + org_besuche
        starts = besuche * start_q
        neu = starts * bestell_q
        wieder = kunden_kumuliert * s.wiederkauf_quote_monat
        bestellungen = neu + wieder
        # Nichtkäufer-KI-Kosten real (nicht über Einheitswert, da Lernkurve die Quote verändert)
        nichtkaeufer_sitzungen = max(0.0, starts - neu)
        ki_nichtkaeufer = nichtkaeufer_sitzungen * p.gen_je_nichtkaeufer * s.gen_faktor * p.ki_kosten_je_generierung
        umsatz_brutto = bestellungen * ew["preis_brutto"]
        umsatz_netto = bestellungen * ew["umsatz_netto"]
        var_ohne_nk = bestellungen * (ew["variable_kosten"] - ew["ki_nichtkaeufer"])
        variabel = var_ohne_nk + ki_nichtkaeufer
        db1 = umsatz_netto - variabel
        marketing = werbung + s.content_kosten_monat
        db2 = db1 - marketing
        ergebnis = db2 - p.fixkosten_monat
        ergebnis_nach_lohn = ergebnis - s.unternehmerlohn_monat
        # Paid-Deckungsbeitrag für Budget-Gate: DB1 der bezahlten Neukunden minus Werbung
        paid_neu = paid_besuche * start_q * bestell_q
        paid_nk = max(0.0, paid_besuche * start_q - paid_neu) * p.gen_je_nichtkaeufer * s.gen_faktor * p.ki_kosten_je_generierung
        paid_db = paid_neu * (ew["umsatz_netto"] - (ew["variable_kosten"] - ew["ki_nichtkaeufer"])) - paid_nk - werbung
        kasse += ergebnis
        kasse_min = min(kasse_min, kasse)
        stunden = bestellungen * (p.pruef_minuten + p.support_minuten) / 60.0
        zeilen.append({
            "monat": m, "werbung": werbung, "content": s.content_kosten_monat, "besuche": besuche,
            "paid_besuche": paid_besuche, "org_besuche": org_besuche, "gestaltungsstarts": starts,
            "neukunden": neu, "wiederkaeufe": wieder, "bestellungen": bestellungen,
            "umsatz_brutto": umsatz_brutto, "umsatz_netto": umsatz_netto, "variable_kosten": variabel,
            "ki_nichtkaeufer": ki_nichtkaeufer, "db1": db1, "marketing": marketing, "db2": db2,
            "fixkosten": p.fixkosten_monat, "ergebnis_vor_lohn": ergebnis,
            "ergebnis_nach_lohn": ergebnis_nach_lohn,
            "cac": marketing / neu if neu > 0 else float("inf"),
            "cac_paid": werbung / paid_neu if paid_neu > 0 else float("inf"),
            "paid_db": paid_db, "kasse_kumuliert": kasse, "pruef_support_stunden": stunden,
        })
        kunden_kumuliert += neu
        budget_vormonat = werbung
        paid_db_vormonat = paid_db
    jahr = {k: sum(z[k] for z in zeilen) for k in (
        "werbung", "content", "bestellungen", "neukunden", "umsatz_brutto", "umsatz_netto",
        "variable_kosten", "db1", "marketing", "db2", "fixkosten", "ergebnis_vor_lohn", "ergebnis_nach_lohn")}
    jahr["ergebnis_vor_lohn_inkl_aufbau"] = jahr["ergebnis_vor_lohn"] - p.einmalig_aufbau
    jahr["ergebnis_nach_lohn_inkl_aufbau"] = jahr["ergebnis_nach_lohn"] - p.einmalig_aufbau
    jahr["cac_mittel"] = jahr["marketing"] / jahr["neukunden"] if jahr["neukunden"] else float("inf")
    # Break-even-Bestellmenge je Monat (vor Unternehmerlohn) bei beobachtetem CAC Monat 12
    cac12 = zeilen[-1]["cac"]
    db_nach_cac = ew["db1"] - cac12
    be_bestellungen = p.fixkosten_monat / db_nach_cac if db_nach_cac > 0 else float("inf")
    be_bestellungen_lohn = (p.fixkosten_monat + s.unternehmerlohn_monat) / db_nach_cac if db_nach_cac > 0 else float("inf")
    # Fixkosten-Break-even ohne Marketing (reiner DB1-Deckungspunkt)
    be_db1 = p.fixkosten_monat / ew["db1"] if ew["db1"] > 0 else float("inf")
    reserve = s.liquiditaetsreserve_monate * (p.fixkosten_monat + max(s.werbebudget_plan[:3]) + s.content_kosten_monat)
    erster_plus_monat = next((z["monat"] for z in zeilen if z["ergebnis_vor_lohn"] >= 0), None)
    return {
        "produkt": p.key, "szenario": s.name, "einheit": ew, "monate": zeilen, "jahr1": jahr,
        "break_even_bestellungen_monat_vor_lohn": be_bestellungen,
        "break_even_bestellungen_monat_nach_lohn": be_bestellungen_lohn,
        "break_even_nur_fixkosten_db1": be_db1,
        "erster_monat_ergebnis_positiv": erster_plus_monat,
        "kapitalbedarf_bis_break_even": -kasse_min + reserve,
        "kasse_minimum": kasse_min, "liquiditaetsreserve": reserve,
    }


# ---------------------------------------------------------------------------
# Sensitivitäten (Parameter der Produkte/Szenarien stehen in parameter.py)
# ---------------------------------------------------------------------------
SENSITIVITAETEN = [
    ("Werbung 50 % teurer (CPC ×1,5)", dict(cpc=1.5)),
    ("Conversion 30 % niedriger", dict(bestell_quote=0.7)),
    ("Doppelt so viele KI-Generierungen", dict(gen_faktor=2.0)),
    ("Dreifache KI-Generierungen", dict(gen_faktor=3.0)),
    ("Doppelte Reklamations-/Erstattungsquote", dict(nachdruck_faktor=2.0)),
    ("Kombiniert: CPC ×1,5 + Conversion −30 % + Reklamation ×2", dict(cpc=1.5, bestell_quote=0.7, nachdruck_faktor=2.0)),
]


def variiere(s: Szenario, aenderung: Dict[str, float]) -> Szenario:
    """Multipliziert die genannten Szenario-Felder mit dem jeweiligen Faktor."""
    return replace(s, **{k: getattr(s, k) * v for k, v in aenderung.items()})


def fmt(x: float, nk: int = 0) -> str:
    if x == float("inf"):
        return "∞"
    if x is None:
        return "–"
    s = f"{x:,.{nk}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def berichte(ergebnisse: Dict, sens: Dict, PRODUKTE: Dict, SZENARIEN: Dict, PARAMETER_QUELLEN: Dict) -> str:
    out = ["# Finanzmodell – Ergebnisse", "",
           "Automatisch erzeugt von `finanzmodell.py`. Alle Werte netto in €, sofern nicht anders angegeben. "
           "Eingaben siehe Abschnitt *Parameter* und `PARAMETER_QUELLEN` im Skript; alles ohne Quelle ist ANNAHME.", ""]
    for pkey, szs in ergebnisse.items():
        p = PRODUKTE[pkey]
        out += [f"## {p.name}", ""]
        # Einheitswerte
        b = szs["Basis"]["einheit"]
        out += ["### Stückrechnung je Bestellung (Basis)", "",
                "| Position | € |", "|---|---:|"]
        for k, lab in [("preis_brutto", "Verkaufspreis inkl. USt"), ("umsatz_netto", "Umsatz netto"),
                       ("herstellung", "Herstellung (Partner)"), ("versand", "Versand"), ("verpackung", "Beilage/Verpackung"),
                       ("zahlungsgebuehr", "Zahlungsgebühr"), ("ki_kaeufer", "KI-Vorschau (Käufer)"),
                       ("ki_nichtkaeufer", "KI-Vorschau Nichtkäufer (anteilig)"), ("ki_produktionsdatei", "KI-Produktionsdatei"),
                       ("pruef_support_arbeit", "Prüfung & Support (Fremdleistung)"), ("nachdruck", "Nachdrucke (erwartet)"),
                       ("erstattung", "Erstattungen (erwartet)"), ("variable_kosten", "Summe variable Kosten"),
                       ("db1", "**Deckungsbeitrag vor Kundengewinnung (DB I)**")]:
            out.append(f"| {lab} | {fmt(b[k], 2)} |")
        out.append(f"| DB-I-Quote | {fmt(b['db1_quote'] * 100, 1)} % |")
        out.append(f"| **Maximal tragbare Kundengewinnungskosten (Erstkauf, Break-even je Bestellung)** | {fmt(b['max_cac_erstkauf'], 2)} |")
        out.append("")
        # Szenarien
        out += ["### Szenarien: Monat 3, 6, 12 und Jahr 1", "",
                "| Kennzahl | " + " | ".join(f"{n} M3 | {n} M6 | {n} M12 | {n} Jahr 1" for n in szs) + " |",
                "|---|" + "---:|" * (4 * len(szs))]
        def zeile(label, key, nk=0):
            vals = []
            for n, r in szs.items():
                for m in (3, 6, 12):
                    vals.append(fmt(r["monate"][m - 1][key], nk))
                vals.append(fmt(r["jahr1"].get(key, float("nan")), nk) if key in r["jahr1"] else "–")
            out.append(f"| {label} | " + " | ".join(vals) + " |")
        zeile("Werbebudget", "werbung")
        zeile("Besuche", "besuche")
        zeile("Gestaltungsstarts", "gestaltungsstarts")
        zeile("Bestellungen", "bestellungen", 0)
        zeile("Umsatz brutto (inkl. USt)", "umsatz_brutto")
        zeile("Umsatz netto", "umsatz_netto")
        zeile("DB I (vor Kundengewinnung)", "db1")
        zeile("Marketing (Werbung + Content)", "marketing")
        zeile("DB II (nach Kundengewinnung)", "db2")
        zeile("Fixkosten", "fixkosten")
        zeile("Operatives Ergebnis vor Unternehmerlohn", "ergebnis_vor_lohn")
        zeile("Ergebnis nach kalk. Unternehmerlohn", "ergebnis_nach_lohn")
        zeile("CAC (Marketing / Neukunden)", "cac", 2)
        zeile("Prüf-/Supportstunden", "pruef_support_stunden", 1)
        out.append("")
        out += ["| Kennzahl | " + " | ".join(szs.keys()) + " |", "|---|" + "---:|" * len(szs)]
        for lab, fn in [
            ("Einmalige Aufbaukosten", lambda r: fmt(p.einmalig_aufbau)),
            ("Jahr 1 Ergebnis vor Lohn inkl. Aufbau", lambda r: fmt(r["jahr1"]["ergebnis_vor_lohn_inkl_aufbau"])),
            ("Jahr 1 Ergebnis nach Lohn inkl. Aufbau", lambda r: fmt(r["jahr1"]["ergebnis_nach_lohn_inkl_aufbau"])),
            ("Break-even Bestellungen/Monat (vor Lohn, bei CAC M12)", lambda r: fmt(r["break_even_bestellungen_monat_vor_lohn"])),
            ("Break-even Bestellungen/Monat (nach Lohn, bei CAC M12)", lambda r: fmt(r["break_even_bestellungen_monat_nach_lohn"])),
            ("Erster Monat mit positivem Ergebnis vor Lohn", lambda r: str(r["erster_monat_ergebnis_positiv"] or "nicht in 12 Monaten")),
            ("Tiefster Kassenstand (inkl. Aufbau)", lambda r: fmt(r["kasse_minimum"])),
            ("Kapitalbedarf bis Break-even inkl. Reserve", lambda r: fmt(r["kapitalbedarf_bis_break_even"])),
        ]:
            out.append(f"| {lab} | " + " | ".join(fn(r) for r in szs.values()) + " |")
        out.append("")
        # Sensitivität
        out += ["### Sensitivität (auf Basis-Szenario)", "",
                "| Variante | DB I/Bestellung | Bestellungen M12 | Nettoumsatz M12 | Ergebnis vor Lohn M12 | Jahr 1 vor Lohn inkl. Aufbau | Kapitalbedarf |",
                "|---|---:|---:|---:|---:|---:|---:|"]
        for lab, r in sens[pkey].items():
            m12 = r["monate"][11]
            out.append(f"| {lab} | {fmt(r['einheit']['db1'], 2)} | {fmt(m12['bestellungen'])} | {fmt(m12['umsatz_netto'])} | "
                       f"{fmt(m12['ergebnis_vor_lohn'])} | {fmt(r['jahr1']['ergebnis_vor_lohn_inkl_aufbau'])} | {fmt(r['kapitalbedarf_bis_break_even'])} |")
        out.append("")
        # Parameter
        out += ["### Parameter", "", "| Parameter | Wert | Quelle/Status |", "|---|---:|---|"]
        q = PARAMETER_QUELLEN.get(pkey, {})
        for k, v in asdict(p).items():
            if k in ("key", "name"):
                continue
            out.append(f"| {k} | {v} | {q.get(k, 'ANNAHME')} |")
        out.append("")
        out += ["| Szenario-Parameter | " + " | ".join(szs.keys()) + " |", "|---|" + "---|" * len(szs)]
        sz_objs = SZENARIEN[pkey]
        for k in ("cpc", "start_quote", "bestell_quote", "lernkurve_start", "werbebudget_plan", "werbe_gate",
                  "organisch_max", "organisch_rampe_monate", "content_kosten_monat", "wiederkauf_quote_monat",
                  "unternehmerlohn_monat", "stundensatz_fremd", "zahl_prozent", "zahl_fix"):
            out.append(f"| {k} | " + " | ".join(str(getattr(sz_objs[n], k)) for n in szs) + " |")
        out.append("")
    return "\n".join(out)


def main():
    sys.path.insert(0, HERE)
    from parameter import PRODUKTE, SZENARIEN, PARAMETER_QUELLEN
    ergebnisse, sens = {}, {}
    for pkey, p in PRODUKTE.items():
        ergebnisse[pkey] = {n: simuliere(p, s) for n, s in SZENARIEN[pkey].items()}
        basis = SZENARIEN[pkey]["Basis"]
        sens[pkey] = {"Basis (Referenz)": ergebnisse[pkey]["Basis"]}
        for lab, ae in SENSITIVITAETEN:
            sens[pkey][lab] = simuliere(p, variiere(basis, ae))
    md = berichte(ergebnisse, sens, PRODUKTE, SZENARIEN, PARAMETER_QUELLEN)
    with open(os.path.join(HERE, "ergebnisse.md"), "w", encoding="utf-8") as f:
        f.write(md)
    with open(os.path.join(HERE, "ergebnisse.json"), "w", encoding="utf-8") as f:
        json.dump({"ergebnisse": ergebnisse, "sensitivitaet": sens}, f, ensure_ascii=False, indent=1, default=str)
    with open(os.path.join(HERE, "monate.csv"), "w", encoding="utf-8", newline="") as f:
        w = None
        for pkey, szs in ergebnisse.items():
            for n, r in szs.items():
                for z in r["monate"]:
                    row = {"produkt": pkey, "szenario": n,
                           **{k: (round(v, 2) if isinstance(v, float) and v != float("inf") else v) for k, v in z.items()}}
                    if w is None:
                        w = csv.DictWriter(f, fieldnames=list(row.keys()), delimiter=";")
                        w.writeheader()
                    w.writerow(row)
    if "--print" in sys.argv:
        print(md)


if __name__ == "__main__":
    main()
