#!/usr/bin/env python3
"""Finanzmodell für KI-personalisierte Premium-POD-Produkte (Deutschland).

Rechenkern ohne Eingabewerte. Die Eingaben stehen in parameter.py, jede mit
Kennzeichnung BELEGT / ANBIETERANGABE / SCHÄTZUNG / ANNAHME und Quelle.
Aufruf:  python3 berechnen.py   (schreibt ergebnisse.md, ergebnisse.json, cac_matrix.csv, skalierung.csv)

Begriffe
- Brutto = inkl. 19 % USt.; netto = ohne USt.
- DB I  = Nettoumsatz minus alle variablen Kosten einer Bestellung (vor Kundengewinnung).
- CAC   = Kosten je NEUKUNDE (bezahlte Werbung, Creator, Rabatte für Erstkauf). Wird nur einmal gebucht.
- Max. tragbarer CAC = Break-even-CAC = DB I der Erstbestellung (+ DB I erwarteter Folgebestellungen
  in 12 Monaten in der Variante "inkl. Wiederkauf").
- Operatives Ergebnis = DB I gesamt − Kundengewinnung − Fixkosten (inkl. angestellter Mitarbeitender),
  vor Ertragsteuern und vor Unternehmerlohn der Gründer; zusätzlich "nach Gründerlohn".
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field, replace
from typing import Dict, List, Optional

UST = 0.19
TAGE_JAHR = 365


@dataclass
class Position:
    """Physischer Artikel in einem Angebot (Produktionsdatei je Artikel)."""
    name: str
    einkauf_netto: float          # Herstellpreis beim Partner, netto, je Stück
    menge: float = 1.0            # Stück je Angebot (z. B. 80 Einladungen = 1 Position mit menge 80 und Stückpreis)
    versand_netto: float = 0.0    # zusätzlicher Partner-Versand, der diesem Artikel zugeordnet ist (0 = in Sendung enthalten)
    produkte: float = 1.0         # zählt als so viele "Produkte je Bestellung" (eine Auflage von 80 Karten = 1 Produkt)


@dataclass
class Angebot:
    """Ein Paket/Set mit festem Bruttopreis."""
    name: str
    preis_brutto: float
    positionen: List[Position]
    sendungen: int = 1            # Anzahl getrennter Pakete (verschiedene Werke/Partner)
    versand_je_sendung_netto: float = 0.0
    produktionsdateien: int = 1   # Anzahl individueller Dateien (für KI-/Prüfaufwand)

    @property
    def einkauf(self) -> float:
        return sum(p.einkauf_netto * p.menge for p in self.positionen)

    @property
    def versand(self) -> float:
        return self.sendungen * self.versand_je_sendung_netto + sum(p.versand_netto for p in self.positionen)

    @property
    def artikel(self) -> float:
        return sum(p.produkte for p in self.positionen)


@dataclass
class Upsell:
    name: str
    quote: float                  # erwartete Anzahl je Bestellung (meist Anteil der Bestellungen mit diesem Zusatz)
    preis_brutto: float
    einkauf_netto: float
    versand_netto: float = 0.0    # Zusatzversand (z. B. eigenes Paket)
    produktionsdateien: int = 1


@dataclass
class Produkt:
    key: str
    name: str
    angebote: List[Angebot]
    upsells: List[Upsell] = field(default_factory=list)
    saison_spitzenfaktor: float = 1.0   # Spitzenmonat / Durchschnittsmonat


@dataclass
class Szenario:
    name: str
    mix: Dict[str, float]                 # Angebotsname -> Anteil (Summe 1)
    upsell_faktor: float = 1.0            # multipliziert alle Upsell-Quoten
    preis_faktor: float = 1.0             # multipliziert alle Bruttopreise (Rabatte/Preisniveau)
    kosten_faktor: float = 1.0            # multipliziert Einkauf + Versand (z. B. EUR- statt USD-Preise)
    verpackung_beilage: float = 1.0       # € netto je Sendung (Beilage, Branding-Einleger)
    zahlung_prozent: float = 0.019        # gemischte Zahlungsgebühr
    zahlung_fix: float = 0.30
    vorschau_kauf_quote: float = 0.08     # Anteil der Vorschau-Sitzungen, die zu einer Bestellung führen
    kosten_vorschau_sitzung: float = 0.30 # KI-Kosten € je Vorschau-Sitzung (alle Varianten, ohne Käufer-Finalisierung)
    kosten_finalisierung: float = 1.00    # KI-Kosten € je Käufer GESAMT: Änderungsrunden, Endbilder, Upscaling, Set-Übertragung (nicht je Datei)
    infrastruktur_je_bestellung: float = 0.30  # Speicher, Hosting, E-Mail, Software-Anteil variabel
    pruef_minuten: float = 10.0           # menschliche QA je Bestellung
    support_minuten: float = 6.0
    stundensatz: float = 30.0             # € je Stunde (Fremdleistung oder Mitarbeitende, voll belastet)
    nachdruck_quote: float = 0.04         # Anteil Bestellungen mit Ersatzproduktion (ganz)
    erstattung_quote: float = 0.02        # Anteil Nettoumsatz, der erstattet wird (Kulanz, Teilerstattungen)
    wiederkauf_12m: float = 0.10          # Folgebestellungen je Neukunde in 12 Monaten
    wiederkauf_aov_faktor: float = 0.6    # Warenkorb der Folgebestellung relativ zur Erstbestellung
    fixkosten_stufen: Optional[Dict[int, float]] = None  # Jahresnettoumsatz -> Fixkosten p. a.
    gruenderlohn_jahr: float = 0.0        # kalkulatorischer Lohn der Gründer p. a.
    cac_realistisch: float = 0.0          # für Zielgruppe und Szenario plausibler CAC (Referenzspalte)


def _upsells(p: Produkt, s: Szenario):
    zeilen = []
    for u in p.upsells:
        q = u.quote * s.upsell_faktor  # erwartete Stückzahl je Bestellung; darf > 1 sein (z. B. Familienkopien je Team)
        zeilen.append((u, q))
    return zeilen


def einheit(p: Produkt, s: Szenario) -> Dict[str, float]:
    """Stückrechnung je Bestellung (Mittel über Angebots-Mix und Upsell-Quoten)."""
    assert abs(sum(s.mix.values()) - 1.0) < 1e-6, f"Mix {s.name} summiert nicht auf 1"
    angebote = {a.name: a for a in p.angebote}
    brutto = einkauf = versand = sendungen = dateien = artikel = 0.0
    for name, anteil in s.mix.items():
        a = angebote[name]
        brutto += anteil * a.preis_brutto * s.preis_faktor
        einkauf += anteil * a.einkauf * s.kosten_faktor
        versand += anteil * a.versand * s.kosten_faktor
        sendungen += anteil * a.sendungen
        dateien += anteil * a.produktionsdateien
        artikel += anteil * a.artikel
    up_brutto = up_einkauf = up_versand = 0.0
    for u, q in _upsells(p, s):
        up_brutto += q * u.preis_brutto * s.preis_faktor
        up_einkauf += q * u.einkauf_netto * s.kosten_faktor
        up_versand += q * u.versand_netto * s.kosten_faktor
        dateien += q * u.produktionsdateien
        artikel += q
    brutto_ges = brutto + up_brutto
    netto = brutto_ges / (1 + UST)
    ust = brutto_ges - netto
    herstellung = einkauf + up_einkauf
    versand_ges = versand + up_versand
    verpackung = sendungen * s.verpackung_beilage
    zahlung = brutto_ges * s.zahlung_prozent + s.zahlung_fix
    ki_nichtkaeufer = s.kosten_vorschau_sitzung * (1 - s.vorschau_kauf_quote) / s.vorschau_kauf_quote
    ki_kaeufer = s.kosten_vorschau_sitzung + s.kosten_finalisierung
    infrastruktur = s.infrastruktur_je_bestellung
    pruefung = s.pruef_minuten / 60 * s.stundensatz
    support = s.support_minuten / 60 * s.stundensatz
    nachdruck = s.nachdruck_quote * (herstellung + versand_ges + verpackung + pruefung)
    erstattung = s.erstattung_quote * netto
    variabel = (herstellung + versand_ges + verpackung + zahlung + ki_nichtkaeufer + ki_kaeufer
                + infrastruktur + pruefung + support + nachdruck + erstattung)
    db1 = netto - variabel
    db1_folge = db1 * s.wiederkauf_aov_faktor  # Näherung: Folgebestellung skaliert proportional
    return {
        "warenkorb_brutto": brutto_ges, "davon_upsells_brutto": up_brutto, "ust": ust, "umsatz_netto": netto,
        "produkte_je_bestellung": artikel, "sendungen_je_bestellung": sendungen, "produktionsdateien": dateien,
        "herstellung": herstellung, "versand": versand_ges, "verpackung": verpackung, "zahlung": zahlung,
        "ki_vorschau_nichtkaeufer": ki_nichtkaeufer, "ki_kaeufer": ki_kaeufer, "infrastruktur": infrastruktur,
        "pruefung": pruefung, "support": support, "nachdruck": nachdruck, "erstattung": erstattung,
        "variable_kosten": variabel, "db1": db1, "db1_quote": db1 / netto if netto else 0.0,
        "max_cac_erstkauf": db1,
        "max_cac_inkl_wiederkauf_12m": db1 + s.wiederkauf_12m * db1_folge,
        "vorschau_sitzungen_je_bestellung": 1 / s.vorschau_kauf_quote,
    }


CAC_STUFEN = [20, 40, 60, 80, 100, 120, 150]


def cac_matrix(e: Dict[str, float], s: Szenario, stufen=CAC_STUFEN) -> List[Dict[str, float]]:
    """Gewinn je Neukunde nach CAC (Erstbestellung) und inkl. Folgebestellungen in 12 Monaten."""
    out = []
    for cac in stufen:
        out.append({
            "cac": cac,
            "gewinn_je_erstbestellung": e["db1"] - cac,
            "gewinn_je_kunde_12m": e["max_cac_inkl_wiederkauf_12m"] - cac,
            "marketingquote_vom_netto": cac / e["umsatz_netto"],
        })
    return out


def fixkosten(s: Szenario, umsatz_netto: float) -> float:
    if not s.fixkosten_stufen:
        return 0.0
    stufen = sorted(s.fixkosten_stufen.items())
    wert = stufen[0][1]
    for grenze, f in stufen:
        if umsatz_netto >= grenze:
            wert = f
    return wert


ZIELE = [250_000, 500_000, 1_000_000, 5_000_000]


def skalierung(p: Produkt, e: Dict[str, float], s: Szenario, ziele=ZIELE, stufen=None) -> List[Dict]:
    """Bestellungen und Ergebnis für Jahresnettoumsatz-Ziele je CAC-Stufe (eingeschwungener Zustand)."""
    # Ø Nettoumsatz je Bestellung über Erst- und Folgebestellungen
    folge_je_kunde = s.wiederkauf_12m
    netto_kunde = e["umsatz_netto"] * (1 + folge_je_kunde * s.wiederkauf_aov_faktor)
    db_kunde = e["max_cac_inkl_wiederkauf_12m"]
    bestell_je_kunde = 1 + folge_je_kunde
    if stufen is None:
        stufen = list(CAC_STUFEN) + ([s.cac_realistisch] if s.cac_realistisch and s.cac_realistisch not in CAC_STUFEN else [])
    rows = []
    for z in ziele:
        kunden = z / netto_kunde
        bestellungen = kunden * bestell_je_kunde
        db1_ges = kunden * db_kunde
        fix = fixkosten(s, z)
        zeile = {
            "ziel_umsatz_netto": z, "neukunden_jahr": kunden, "bestellungen_jahr": bestellungen,
            "bestellungen_monat": bestellungen / 12, "bestellungen_tag": bestellungen / TAGE_JAHR,
            "bestellungen_tag_spitzenmonat": bestellungen / 12 * p.saison_spitzenfaktor / 30.4,
            "warenkorb_brutto_mittel": z * (1 + UST) / bestellungen,
            "db1_gesamt": db1_ges, "db1_quote": db1_ges / z, "fixkosten": fix,
            "qa_support_stunden_jahr": bestellungen * (s.pruef_minuten + s.support_minuten) / 60,
            "qa_support_vollzeitstellen": bestellungen * (s.pruef_minuten + s.support_minuten) / 60 / 1650,
            "je_cac": [],
        }
        for cac in stufen:
            mk = kunden * cac
            erg = db1_ges - mk - fix
            zeile["je_cac"].append({
                "cac": cac, "kundengewinnung": mk, "db2": db1_ges - mk,
                "operatives_ergebnis": erg, "umsatzrendite": erg / z,
                "nach_gruenderlohn": erg - s.gruenderlohn_jahr,
            })
        rows.append(zeile)
    return rows


SENSITIVITAETEN = [
    ("Werbung teurer: CAC +30 % (Spalte bei CAC 60 → 78)", {"_cac": 1.3}),
    ("Niedrigere Conversion: Vorschau→Kauf −40 %", {"vorschau_kauf_quote": 0.6}),
    ("Mehr KI-Generierungen: Vorschau- und Finalisierungskosten ×2", {"kosten_vorschau_sitzung": 2.0, "kosten_finalisierung": 2.0}),
    ("Mehr Reklamationen: Nachdruck ×2, Erstattung ×2", {"nachdruck_quote": 2.0, "erstattung_quote": 2.0}),
    ("Produktion/Versand +15 % (z. B. EUR-Preise, Zuschläge)", {"kosten_faktor": 1.15}),
    ("Warenkorb −15 % (Preisdruck, weniger Upsells)", {"preis_faktor": 0.85}),
    ("Mehr Handarbeit: Prüfung und Support ×2", {"pruef_minuten": 2.0, "support_minuten": 2.0}),
]


def variiere(s: Szenario, faktoren: Dict[str, float]) -> Szenario:
    aend = {k: getattr(s, k) * v for k, v in faktoren.items() if not k.startswith("_")}
    return replace(s, **aend)


def sensitivitaet(p: Produkt, s: Szenario, ref_cac: float, ziel: float = 1_000_000) -> List[Dict]:
    basis_e = einheit(p, s)
    basis_sk = skalierung(p, basis_e, s, ziele=[ziel], stufen=[ref_cac])[0]["je_cac"][0]["operatives_ergebnis"]
    out = [{"fall": "Ausgangswert", "db1": basis_e["db1"], "max_cac": basis_e["max_cac_erstkauf"],
            "ergebnis_1mio": basis_sk, "delta": 0.0}]
    for label, f in SENSITIVITAETEN:
        s2 = variiere(s, f)
        cac = ref_cac * f.get("_cac", 1.0)
        e2 = einheit(p, s2)
        erg = skalierung(p, e2, s2, ziele=[ziel], stufen=[cac])[0]["je_cac"][0]["operatives_ergebnis"]
        out.append({"fall": label, "db1": e2["db1"], "max_cac": e2["max_cac_erstkauf"],
                    "ergebnis_1mio": erg, "delta": erg - basis_sk})
    return out


def testbudget(conversion_besuch_kauf: float, cpc: float, ziel_bestellungen: float) -> Dict[str, float]:
    besucher = ziel_bestellungen / conversion_besuch_kauf
    return {"besucher": besucher, "budget": besucher * cpc, "cac_impliziert": cpc / conversion_besuch_kauf}


def fmt(x: float, nk: int = 0) -> str:
    if x is None or (isinstance(x, float) and (math.isinf(x) or math.isnan(x))):
        return "–"
    s = f"{x:,.{nk}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")
