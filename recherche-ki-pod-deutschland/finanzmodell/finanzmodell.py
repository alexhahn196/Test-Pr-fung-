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
    werbebudget_plan: List[float]     # geplantes Werbebudget Monat 1..12 (netto); ab Monat 13 = Monat 12
    werbe_gate: bool                  # True: ist Paid im Vormonat unprofitabel, sinkt Budget auf werbe_minimum
    organisch_max: float              # organische Besuche/Monat nach Rampe (Obergrenze)
    organisch_rampe_monate: int       # Monate bis Obergrenze erreicht
    content_kosten_monat: float       # laufende Content-/Creator-/Musterkosten (netto) – Voraussetzung für organisch
    wiederkauf_quote_monat: float     # Anteil bisheriger Kunden, die pro Monat erneut bestellen
    werbe_minimum: float = 0.0        # Restbudget (Retargeting/Tests), wenn das Gate greift
    partner_start_monat: int = 99     # Monat, ab dem der Partnerkanal Bestellungen liefert
    partner_rampe_monate: int = 6     # Monate bis partner_bestellungen_max erreicht ist
    partner_bestellungen_max: float = 0.0  # Bestellungen/Monat über Empfehlungspartner nach Rampe
    partner_provision: float = 0.0    # Provision in % des Nettoumsatzes je Partnerbestellung
    partner_kosten_monat: float = 0.0 # Material/Displays/Pflege Partnerkanal (netto, fix ab Start)
    saison: List[float] = field(default_factory=lambda: [1.0] * 12)  # Nachfragefaktor je Kalendermonat ab Start
    preis_faktor: float = 1.0         # Anpassung Ø Warenkorb
    gen_faktor: float = 1.0           # Anpassung Generierungen je Sitzung
    nachdruck_faktor: float = 1.0     # Anpassung Nachdruck-/Erstattungsquote
    unternehmerlohn_monat: float = 2500.0  # kalkulatorisch (ANNAHME)
    stundensatz_fremd: float = 22.0   # € je Stunde Prüf-/Supportzeit (Minijob/Freelancer inkl. Nebenkosten)
    zahl_prozent: float = 0.019       # Zahlungsgebühr prozentual (Mischsatz)
    zahl_fix: float = 0.25            # Zahlungsgebühr fix je Transaktion
    liquiditaetsreserve_monate: float = 1.0  # Reserve in Monaten (Fixkosten + Marketing)


# ---------------------------------------------------------------------------
# Kernrechnung
# ---------------------------------------------------------------------------
def einheitswerte(p: Produkt, s: Szenario) -> Dict[str, float]:
    """Deckungsbeitrag je Bestellung vor Kundengewinnung (DB I), inkl. anteiliger Nichtkäufer-KI-Kosten
    bei eingeschwungener Conversion (ohne Lernkurve) und ohne Partnerprovision."""
    brutto = p.preis_brutto * s.preis_faktor
    netto = brutto / (1 + UST)
    zahl = brutto * s.zahl_prozent + s.zahl_fix
    ki_kaeufer = p.gen_je_kaeufer * s.gen_faktor * p.ki_kosten_je_generierung
    nichtkaeufer_je_bestellung = (1.0 / s.bestell_quote) - 1.0
    ki_nichtkaeufer = nichtkaeufer_je_bestellung * p.gen_je_nichtkaeufer * s.gen_faktor * p.ki_kosten_je_generierung
    arbeit = (p.pruef_minuten + p.support_minuten) / 60.0 * s.stundensatz_fremd
    nachdruck_q = min(p.nachdruck_quote * s.nachdruck_faktor, 0.9)
    nachdruck_kosten_voll = p.herstellung + p.versand + p.verpackung_beilage + p.pruef_minuten / 60.0 * s.stundensatz_fremd
    nachdruck = nachdruck_q * (1 - p.partner_traegt_anteil_nachdruck) * nachdruck_kosten_voll
    erstattung = min(p.erstattung_quote * s.nachdruck_faktor, 0.9) * p.erstattung_anteil * netto
    variabel_ohne_nk = (p.herstellung + p.versand + p.verpackung_beilage + zahl + ki_kaeufer
                        + p.ki_produktionsdatei + arbeit + nachdruck + erstattung)
    variabel = variabel_ohne_nk + ki_nichtkaeufer
    db1 = netto - variabel
    return {
        "preis_brutto": brutto, "umsatz_netto": netto, "herstellung": p.herstellung, "versand": p.versand,
        "verpackung": p.verpackung_beilage, "zahlungsgebuehr": zahl, "ki_kaeufer": ki_kaeufer,
        "ki_nichtkaeufer": ki_nichtkaeufer, "ki_produktionsdatei": p.ki_produktionsdatei,
        "pruef_support_arbeit": arbeit, "nachdruck": nachdruck, "erstattung": erstattung,
        "variable_kosten": variabel, "variable_ohne_nichtkaeufer": variabel_ohne_nk,
        "db1": db1, "db1_quote": db1 / netto if netto else 0.0,
    }


def simuliere(p: Produkt, s: Szenario, monate: int = 24) -> Dict:
    """Monatliche Simulation. Berichtet werden Monat 1–12 (Jahr 1); Monat 13–24 dient nur dazu,
    Break-even-Monat und Kapitalbedarf bis zum Break-even zu bestimmen (Parameter wie Monat 12)."""
    ew = einheitswerte(p, s)
    zeilen = []
    kunden_kumuliert = 0.0
    kasse = -p.einmalig_aufbau  # Monat 0: Aufbau
    kasse_min = kasse
    paid_db_vormonat = None
    for m in range(1, monate + 1):
        plan = s.werbebudget_plan[min(m, 12) - 1]
        if s.werbe_gate and paid_db_vormonat is not None and paid_db_vormonat < 0:
            werbung = min(plan, s.werbe_minimum)  # Paid unprofitabel -> auf Restbudget zurückfahren
        else:
            werbung = plan
        lern = min(1.0, s.lernkurve_start + (1.0 - s.lernkurve_start) * (m - 1) / 3.0)
        saison = s.saison[(m - 1) % 12]
        start_q = s.start_quote
        bestell_q = s.bestell_quote * lern * saison
        paid_besuche = werbung / s.cpc if s.cpc > 0 else 0.0
        org_besuche = s.organisch_max * min(1.0, m / max(1, s.organisch_rampe_monate))
        besuche = paid_besuche + org_besuche
        starts = besuche * start_q
        neu_web = starts * bestell_q
        if m >= s.partner_start_monat:
            neu_partner = s.partner_bestellungen_max * min(1.0, (m - s.partner_start_monat + 1) / max(1, s.partner_rampe_monate)) * saison
            partner_fix = s.partner_kosten_monat
        else:
            neu_partner, partner_fix = 0.0, 0.0
        neu = neu_web + neu_partner
        wieder = kunden_kumuliert * s.wiederkauf_quote_monat
        bestellungen = neu + wieder
        # Partnerkunden starten ebenfalls einen Entwurf (Käufer-KI im Einheitswert); Nichtkäufer nur aus Web
        nichtkaeufer_sitzungen = max(0.0, starts - neu_web)
        ki_nichtkaeufer = nichtkaeufer_sitzungen * p.gen_je_nichtkaeufer * s.gen_faktor * p.ki_kosten_je_generierung
        umsatz_brutto = bestellungen * ew["preis_brutto"]
        umsatz_netto = bestellungen * ew["umsatz_netto"]
        provision = neu_partner * ew["umsatz_netto"] * s.partner_provision
        variabel = bestellungen * ew["variable_ohne_nichtkaeufer"] + ki_nichtkaeufer + provision
        db1 = umsatz_netto - variabel
        marketing = werbung + s.content_kosten_monat + partner_fix
        db2 = db1 - marketing
        ergebnis = db2 - p.fixkosten_monat
        ergebnis_nach_lohn = ergebnis - s.unternehmerlohn_monat
        paid_neu = paid_besuche * start_q * bestell_q
        paid_nk = max(0.0, paid_besuche * start_q - paid_neu) * p.gen_je_nichtkaeufer * s.gen_faktor * p.ki_kosten_je_generierung
        paid_db = paid_neu * (ew["umsatz_netto"] - ew["variable_ohne_nichtkaeufer"]) - paid_nk - werbung
        kasse += ergebnis
        kasse_min = min(kasse_min, kasse)
        stunden = bestellungen * (p.pruef_minuten + p.support_minuten) / 60.0
        zeilen.append({
            "monat": m, "werbung": werbung, "content": s.content_kosten_monat, "partner_fix": partner_fix,
            "besuche": besuche, "paid_besuche": paid_besuche, "org_besuche": org_besuche,
            "gestaltungsstarts": starts, "neukunden": neu, "neukunden_partner": neu_partner,
            "wiederkaeufe": wieder, "bestellungen": bestellungen,
            "umsatz_brutto": umsatz_brutto, "umsatz_netto": umsatz_netto, "variable_kosten": variabel,
            "ki_nichtkaeufer": ki_nichtkaeufer, "provision": provision, "db1": db1, "marketing": marketing,
            "db2": db2, "fixkosten": p.fixkosten_monat, "ergebnis_vor_lohn": ergebnis,
            "ergebnis_nach_lohn": ergebnis_nach_lohn,
            "cac": marketing / neu if neu > 0 else float("inf"),
            "cac_paid": werbung / paid_neu if paid_neu > 0 else float("inf"),
            "paid_db": paid_db, "kasse_kumuliert": kasse, "pruef_support_stunden": stunden,
        })
        kunden_kumuliert += neu
        paid_db_vormonat = paid_db
    j1 = zeilen[:12]
    jahr = {k: sum(z[k] for z in j1) for k in (
        "werbung", "content", "partner_fix", "bestellungen", "neukunden", "umsatz_brutto", "umsatz_netto",
        "variable_kosten", "provision", "db1", "marketing", "db2", "fixkosten", "ergebnis_vor_lohn",
        "ergebnis_nach_lohn")}
    jahr["ergebnis_vor_lohn_inkl_aufbau"] = jahr["ergebnis_vor_lohn"] - p.einmalig_aufbau
    jahr["ergebnis_nach_lohn_inkl_aufbau"] = jahr["ergebnis_nach_lohn"] - p.einmalig_aufbau
    jahr["cac_mittel"] = jahr["marketing"] / jahr["neukunden"] if jahr["neukunden"] else float("inf")
    m12 = zeilen[11]
    # Break-even-Bestellmengen (Monat, vor Unternehmerlohn):
    # (a) Deckung von Fixkosten + Marketing des Monats 12 durch DB I
    be_deckung = (p.fixkosten_monat + m12["marketing"]) / ew["db1"] if ew["db1"] > 0 else float("inf")
    # (b) Wachstum über bezahlte Werbung: Fixkosten / (DB I – Paid-CAC); ∞, wenn Paid-CAC >= DB I
    cac_paid12 = m12["cac_paid"]
    be_paid = p.fixkosten_monat / (ew["db1"] - cac_paid12) if ew["db1"] > cac_paid12 else float("inf")
    be_deckung_lohn = (p.fixkosten_monat + m12["marketing"] + s.unternehmerlohn_monat) / ew["db1"] if ew["db1"] > 0 else float("inf")
    # Maximal tragbare CAC: Erstkauf und inkl. erwarteter Wiederkäufe in 12 Monaten
    wiederkaeufe_12m = s.wiederkauf_quote_monat * 12
    max_cac_ltv = ew["db1"] * (1 + wiederkaeufe_12m)
    erster_plus = next((z["monat"] for z in zeilen if z["ergebnis_vor_lohn"] >= 0), None)
    erster_plus_lohn = next((z["monat"] for z in zeilen if z["ergebnis_nach_lohn"] >= 0), None)
    kasse_min_bis_be = min([-p.einmalig_aufbau] + [z["kasse_kumuliert"] for z in zeilen])
    reserve = s.liquiditaetsreserve_monate * (p.fixkosten_monat + m12["marketing"])
    return {
        "produkt": p.key, "szenario": s.name, "einheit": ew, "monate": zeilen[:12], "monate_bis_24": zeilen,
        "jahr1": jahr,
        "max_cac_erstkauf": ew["db1"], "max_cac_inkl_wiederkauf_12m": max_cac_ltv,
        "break_even_bestellungen_deckung_m12": be_deckung,
        "break_even_bestellungen_deckung_m12_nach_lohn": be_deckung_lohn,
        "break_even_bestellungen_bei_paid_cac": be_paid,
        "cac_paid_m12": cac_paid12,
        "erster_monat_ergebnis_positiv": erster_plus,
        "erster_monat_ergebnis_nach_lohn_positiv": erster_plus_lohn,
        "kasse_minimum_24m": kasse_min_bis_be,
        "kapitalbedarf_bis_break_even": (-kasse_min_bis_be + reserve) if erster_plus else None,
        "kapitalbedarf_24m_ohne_break_even": (-kasse_min_bis_be + reserve),
        "liquiditaetsreserve": reserve,
    }


# ---------------------------------------------------------------------------
# Sensitivitäten (Parameter der Produkte/Szenarien stehen in parameter.py)
# ---------------------------------------------------------------------------
SENSITIVITAETEN = [
    ("Werbung 50 % teurer (CPC ×1,5)", dict(cpc=1.5)),
    ("Conversion 30 % niedriger (Gestaltung → Bestellung)", dict(bestell_quote=0.7)),
    ("Doppelt so viele KI-Generierungen je Sitzung", dict(gen_faktor=2.0)),
    ("Dreifache KI-Generierungen je Sitzung", dict(gen_faktor=3.0)),
    ("Doppelte Reklamations-/Erstattungsquote", dict(nachdruck_faktor=2.0)),
    ("Partnerkanal liefert nur die Hälfte", dict(partner_bestellungen_max=0.5)),
    ("Organische Reichweite nur die Hälfte", dict(organisch_max=0.5)),
    ("Kombiniert: CPC ×1,5, Conversion −30 %, Reklamation ×2", dict(cpc=1.5, bestell_quote=0.7, nachdruck_faktor=2.0)),
]


def variiere(s: Szenario, aenderung: Dict[str, float]) -> Szenario:
    """Multipliziert die genannten Szenario-Felder mit dem jeweiligen Faktor."""
    return replace(s, **{k: getattr(s, k) * v for k, v in aenderung.items()})


def fmt(x, nk: int = 0) -> str:
    if x is None:
        return "–"
    if isinstance(x, float) and x == float("inf"):
        return "∞"
    s = f"{x:,.{nk}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def berichte(ergebnisse: Dict, sens: Dict, PRODUKTE: Dict, SZENARIEN: Dict, PARAMETER_QUELLEN: Dict) -> str:
    out = ["# Finanzmodell – Ergebnisse", "",
           "Automatisch erzeugt von `finanzmodell.py` mit den Eingaben aus `parameter.py`. Alle Werte in €, netto "
           "(ohne Umsatzsteuer), sofern nicht als brutto bezeichnet. Monat 1 = erster Verkaufsmonat nach dem Aufbau "
           "(Monat 0). Ergebnis = operatives Ergebnis vor Ertragsteuern; „nach Lohn“ zusätzlich nach kalkulatorischem "
           "Unternehmerlohn. Werbung wird nur einmal als Kosten gebucht; CAC ist nur eine abgeleitete Kennzahl. "
           "Alle Eingaben ohne Quellenangabe sind ANNAHMEN (siehe Parametertabellen).", ""]
    for pkey, szs in ergebnisse.items():
        p = PRODUKTE[pkey]
        out += [f"## {p.name}", ""]
        out += ["### Stückrechnung je Bestellung (DB I = Deckungsbeitrag vor Kundengewinnung)", "",
                "| Position | " + " | ".join(szs.keys()) + " |", "|---|" + "---:|" * len(szs)]
        rows = [("preis_brutto", "Verkaufspreis inkl. USt (Ø Warenkorb)"), ("umsatz_netto", "Umsatz netto"),
                ("herstellung", "Herstellung (Partner)"), ("versand", "Versand an Kunden"),
                ("verpackung", "Beilage/Verpackung"), ("zahlungsgebuehr", "Zahlungsgebühr"),
                ("ki_kaeufer", "KI-Vorschau der Käufer"), ("ki_nichtkaeufer", "KI-Vorschau der Nichtkäufer (umgelegt)"),
                ("ki_produktionsdatei", "KI/Software für Produktionsdatei"),
                ("pruef_support_arbeit", "Prüfung & Support (Fremdleistung)"), ("nachdruck", "Nachdrucke (Erwartungswert)"),
                ("erstattung", "Erstattungen (Erwartungswert)"), ("variable_kosten", "Summe variable Kosten"),
                ("db1", "**DB I je Bestellung**")]
        for k, lab in rows:
            out.append(f"| {lab} | " + " | ".join(fmt(r['einheit'][k], 2) for r in szs.values()) + " |")
        out.append("| DB-I-Quote (vom Nettoumsatz) | " + " | ".join(fmt(r['einheit']['db1_quote'] * 100, 1) + " %" for r in szs.values()) + " |")
        out.append("| **Max. tragbare CAC Erstkauf (= DB I)** | " + " | ".join(fmt(r['max_cac_erstkauf'], 2) for r in szs.values()) + " |")
        out.append("| Max. tragbare CAC inkl. Wiederkäufe 12 Monate | " + " | ".join(fmt(r['max_cac_inkl_wiederkauf_12m'], 2) for r in szs.values()) + " |")
        out.append("")
        out += ["### Szenarien: Monat 3, 6, 12 und Jahr 1 (Hochlauf)", ""]
        for n, r in szs.items():
            out += [f"**{n}**", "", "| Kennzahl | Monat 3 | Monat 6 | Monat 12 | Jahr 1 |", "|---|---:|---:|---:|---:|"]
            def zeile(label, key, nk=0, summe=True):
                vals = [fmt(r["monate"][m - 1][key], nk) for m in (3, 6, 12)]
                vals.append(fmt(r["jahr1"][key], nk) if (summe and key in r["jahr1"]) else "–")
                out.append(f"| {label} | " + " | ".join(vals) + " |")
            zeile("Werbebudget (bezahlt)", "werbung")
            zeile("Content/Creator + Partnerpflege", "content")
            zeile("Besuche (bezahlt + organisch)", "besuche", summe=False)
            zeile("Gestaltungsstarts (KI-Vorschau)", "gestaltungsstarts", summe=False)
            zeile("Neukunden gesamt", "neukunden", 1)
            zeile("davon über Partner", "neukunden_partner", 1, summe=False)
            zeile("Bestellungen inkl. Wiederkäufe", "bestellungen", 1)
            zeile("Umsatz brutto (inkl. USt)", "umsatz_brutto")
            zeile("**Umsatz netto**", "umsatz_netto")
            zeile("DB I (nach variablen Kosten inkl. Provision)", "db1")
            zeile("Marketing gesamt (Werbung + Content + Partner)", "marketing")
            zeile("DB II (nach Kundengewinnung)", "db2")
            zeile("Fixkosten", "fixkosten")
            zeile("**Operatives Ergebnis vor Lohn**", "ergebnis_vor_lohn")
            zeile("Ergebnis nach kalk. Unternehmerlohn", "ergebnis_nach_lohn")
            zeile("CAC gesamt (Marketing / Neukunden)", "cac", 2, summe=False)
            zeile("CAC bezahlt (Werbung / Paid-Neukunden)", "cac_paid", 2, summe=False)
            zeile("Prüf-/Supportstunden", "pruef_support_stunden", 1)
            zeile("Kassenstand kumuliert (inkl. Aufbau)", "kasse_kumuliert", summe=False)
            out.append("")
        out += ["### Break-even, Kapitalbedarf, Jahr 1", "",
                "| Kennzahl | " + " | ".join(szs.keys()) + " |", "|---|" + "---:|" * len(szs)]
        kz = [
            ("Einmalige Aufbaukosten (ohne eigene Arbeitszeit)", lambda r: fmt(p.einmalig_aufbau)),
            ("Testbudget 14-Tage-Validierung", lambda r: fmt(p.testbudget)),
            ("Jahr 1: Nettoumsatz", lambda r: fmt(r["jahr1"]["umsatz_netto"])),
            ("Jahr 1: Ergebnis vor Lohn (inkl. Aufbau)", lambda r: fmt(r["jahr1"]["ergebnis_vor_lohn_inkl_aufbau"])),
            ("Jahr 1: Ergebnis nach Lohn (inkl. Aufbau)", lambda r: fmt(r["jahr1"]["ergebnis_nach_lohn_inkl_aufbau"])),
            ("Break-even-Bestellungen/Monat: Fixkosten + Marketing M12 gedeckt (vor Lohn)", lambda r: fmt(r["break_even_bestellungen_deckung_m12"])),
            ("… dasselbe nach Unternehmerlohn", lambda r: fmt(r["break_even_bestellungen_deckung_m12_nach_lohn"])),
            ("Break-even-Bestellungen/Monat bei Wachstum nur über Paid (∞ = Paid-CAC ≥ DB I)", lambda r: fmt(r["break_even_bestellungen_bei_paid_cac"])),
            ("Paid-CAC in Monat 12", lambda r: fmt(r["cac_paid_m12"], 2)),
            ("Erster Monat mit Ergebnis vor Lohn ≥ 0 (Horizont 24 M.)", lambda r: str(r["erster_monat_ergebnis_positiv"] or "nicht in 24 Monaten")),
            ("Erster Monat mit Ergebnis nach Lohn ≥ 0 (Horizont 24 M.)", lambda r: str(r["erster_monat_ergebnis_nach_lohn_positiv"] or "nicht in 24 Monaten")),
            ("Tiefster Kassenstand in 24 Monaten (inkl. Aufbau)", lambda r: fmt(r["kasse_minimum_24m"])),
            ("Kapitalbedarf bis Break-even inkl. 1 Monat Reserve", lambda r: fmt(r["kapitalbedarf_bis_break_even"]) if r["kapitalbedarf_bis_break_even"] is not None else "kein Break-even ≤ 24 M. (" + fmt(r["kapitalbedarf_24m_ohne_break_even"]) + " bis M24)"),
        ]
        for lab, fn in kz:
            out.append(f"| {lab} | " + " | ".join(fn(r) for r in szs.values()) + " |")
        out.append("")
        out += ["### Sensitivität (Basis-Szenario, jeweils nur ein Parameter verändert)", "",
                "| Variante | DB I/Bestellung | Paid-CAC M12 | Bestellungen M12 | Nettoumsatz M12 | Ergebnis vor Lohn M12 | Jahr 1 vor Lohn inkl. Aufbau | Break-even-Monat |",
                "|---|---:|---:|---:|---:|---:|---:|---:|"]
        for lab, r in sens[pkey].items():
            m12 = r["monate"][11]
            out.append(f"| {lab} | {fmt(r['einheit']['db1'], 2)} | {fmt(r['cac_paid_m12'], 2)} | {fmt(m12['bestellungen'])} | "
                       f"{fmt(m12['umsatz_netto'])} | {fmt(m12['ergebnis_vor_lohn'])} | "
                       f"{fmt(r['jahr1']['ergebnis_vor_lohn_inkl_aufbau'])} | {r['erster_monat_ergebnis_positiv'] or '> 24'} |")
        out.append("")
        out += ["### Produktparameter", "", "| Parameter | Wert | Quelle/Status |", "|---|---:|---|"]
        q = PARAMETER_QUELLEN.get(pkey, {})
        for k, v in asdict(p).items():
            if k in ("key", "name"):
                continue
            out.append(f"| {k} | {v} | {q.get(k, 'ANNAHME')} |")
        out.append("")
        out += ["### Szenarioparameter", "", "| Parameter | " + " | ".join(szs.keys()) + " | Quelle/Status |",
                "|---|" + "---|" * len(szs) + "---|"]
        sz_objs = SZENARIEN[pkey]
        for k in ("preis_faktor", "cpc", "start_quote", "bestell_quote", "lernkurve_start", "werbebudget_plan",
                  "werbe_gate", "werbe_minimum", "organisch_max", "organisch_rampe_monate", "content_kosten_monat",
                  "partner_start_monat", "partner_rampe_monate", "partner_bestellungen_max", "partner_provision",
                  "partner_kosten_monat", "wiederkauf_quote_monat", "saison", "gen_faktor", "nachdruck_faktor",
                  "unternehmerlohn_monat", "stundensatz_fremd", "zahl_prozent", "zahl_fix"):
            out.append(f"| {k} | " + " | ".join(str(getattr(sz_objs[n], k)) for n in szs) + f" | {q.get('sz_' + k, 'ANNAHME')} |")
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
