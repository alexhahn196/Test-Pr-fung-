"""Eingaben des Finanzmodells mit Kennzeichnung (BELEGT / ANBIETERANGABE / SCHÄTZUNG / ANNAHME).

Zwei Ebenen:
1. VERGLEICH: alle 10 Shortlist-Kandidaten, automatisch aus den vorsichtigen Modelleingaben der
   adversarialen Prüfer (rohdaten/vertiefung-batch*.json, Feld pruefer.modell_eingaben) mit
   einheitlichen gemeinsamen Annahmen. Dient dem fairen Vergleich.
2. PRODUKTE: die Finalisten mit geprüften Einzelwerten (Abschnitt FINALISTEN unten). Wo die
   Finalisten-Werte von den Prüferwerten abweichen, steht der Grund in PARAMETER_QUELLEN.
"""
import glob
import json
import os
from dataclasses import replace

from modell import Angebot, Position, Produkt, Szenario, Upsell

HIER = os.path.dirname(os.path.abspath(__file__))
ROH = os.path.join(HIER, "..", "rohdaten")

# ---------------------------------------------------------------------------
# Gemeinsame Annahmen (für alle Kandidaten gleich)
# ---------------------------------------------------------------------------
# Fixkosten p. a. je Umsatzstufe (Jahresnettoumsatz ab ... €), ohne Gründerlohn, ohne QA/Support
# (die stecken als variable Kosten über den Stundensatz in jeder Bestellung). ANNAHME:
#  < 500 k: Software/Hosting/KI-Grundgebühren 8 k, Steuerberatung/Recht 8 k, Versicherungen 2 k,
#           Muster/Proben 4 k, Sonstiges 4 k                                   = 26 k
#  ≥ 500 k: + 1 Vollzeitstelle Betrieb/Marketing (55 k Arbeitgeberkosten), Tools/Beratung +14 k = 95 k
#  ≥ 1 Mio: 2 Stellen (110 k), Tools/Software 25 k, Beratung/Recht 20 k, Sonstiges 15 k        = 170 k
#  ≥ 5 Mio: 8 Stellen (480 k), Tools/Büro 120 k, Beratung/Recht 60 k, Sonstiges 60 k          = 720 k
FIXKOSTEN = {0: 26_000, 500_000: 95_000, 1_000_000: 170_000, 5_000_000: 720_000}
GRUENDERLOHN = 120_000  # 2 Gründer × 60 k kalkulatorisch (ANNAHME)

GEMEINSAM = dict(
    verpackung_beilage=0.50,      # ANNAHME: Marken-Einleger beim Partner; Printful-Einleger 0,45 € (Vorarbeit, ANBIETERANGABE)
    zahlung_prozent=0.023,        # ANNAHME Mix aus Stripe EWR-Karte 1,5 % + 0,25 €, PayPal 2,99 % + 0,39 €, Klarna (BELEGT Tarife, Vorarbeit)
    zahlung_fix=0.33,
    infrastruktur_je_bestellung=0.30,  # ANNAHME: Speicher (R2 0,015 USD/GB-Monat), Hosting, Mailversand
    stundensatz=30.0,             # ANNAHME: voll belastete Stunde Prüfung/Support (z. B. Angestellte 35 k € + 21 % AG / 1.650 h ≈ 26 €)
    fixkosten_stufen=FIXKOSTEN,
    gruenderlohn_jahr=GRUENDERLOHN,
)

# Szenario-Hebel, die der Prüfer nicht je Szenario liefert (ANNAHME)
SZ_HEBEL = {
    "Konservativ": dict(upsell_faktor=0.7, kosten_faktor=1.05, nachdruck=1.5, erstattung=1.5, wiederkauf=0.5),
    "Basis": dict(upsell_faktor=1.0, kosten_faktor=1.0, nachdruck=1.0, erstattung=1.0, wiederkauf=1.0),
    "Optimistisch": dict(upsell_faktor=1.25, kosten_faktor=1.0, nachdruck=0.75, erstattung=0.75, wiederkauf=1.3),
}
SZ_KEY = {"Konservativ": "konservativ", "Basis": "basis", "Optimistisch": "optimistisch"}


def _lade_kandidaten():
    k = []
    for fn in sorted(glob.glob(os.path.join(ROH, "vertiefung-batch*.json"))):
        k += json.load(open(fn, encoding="utf-8"))
    return {x["id"]: x for x in k}


def aus_eingaben(key, name, mi, saison=None):
    """Baut Produkt und drei Szenarien aus einem Satz Modelleingaben (Format pruefer.modell_eingaben)."""
    angebote = []
    for a in mi["angebote"]:
        s = max(1, int(round(a["sendungen"])))
        angebote.append(Angebot(a["name"], a["preis_brutto"],
                                [Position(a["name"], a["einkauf_netto"], 1, produkte=a["produkte"])],
                                sendungen=s, versand_je_sendung_netto=a["versand_netto"] / s,
                                produktionsdateien=max(1, int(round(a["produktionsdateien"])))))
    ups = [Upsell(u["name"], u["quote_basis"], u["preis_brutto"], u["einkauf_netto"], u["versand_netto"]) for u in mi["upsells"]]
    p = Produkt(key, name, angebote, ups, saison_spitzenfaktor=saison or mi["saison_spitzenfaktor"])
    szs = {}
    for n, h in SZ_HEBEL.items():
        k = SZ_KEY[n]
        mix = {a["name"]: a[f"mix_{k}"] for a in mi["angebote"]}
        tot = sum(mix.values())
        mix = {m: v / tot for m, v in mix.items()}  # auf 1 normieren
        szs[n] = Szenario(n, mix, upsell_faktor=h["upsell_faktor"], kosten_faktor=h["kosten_faktor"],
                          vorschau_kauf_quote=mi[f"vorschau_kauf_quote_{k}"],
                          kosten_vorschau_sitzung=mi["kosten_vorschau_sitzung_eur"],
                          kosten_finalisierung=mi["kosten_finalisierung_eur"],
                          pruef_minuten=mi["pruef_minuten"], support_minuten=mi["support_minuten"],
                          nachdruck_quote=mi["nachdruck_quote"] * h["nachdruck"],
                          erstattung_quote=mi["erstattung_quote"] * h["erstattung"],
                          wiederkauf_12m=mi["wiederkauf_12m"] * h["wiederkauf"],
                          wiederkauf_aov_faktor=mi["wiederkauf_aov_faktor"],
                          cac_realistisch=mi[f"cac_realistisch_{k}"], **GEMEINSAM)
    return p, szs


def aus_pruefer(k, saison=None):
    """Vertiefung: Eingaben des adversarialen Prüfers."""
    return aus_eingaben(k["id"], f"{k['id']}: {k['titel']}", k["pruefer"]["modell_eingaben"], saison)


KANDIDATEN = _lade_kandidaten()
NEUZUSCHNITT = {k["id"]: k for k in json.load(open(os.path.join(ROH, "neuzuschnitt.json"), encoding="utf-8"))["kandidaten"]}


def oekonomie_eingaben(kid):
    """Neuzuschnitt: korrigierte Eingaben des Ökonomie-Prüfers (vorsichtigste Kostenseite und CAC)."""
    gp = [g for g in NEUZUSCHNITT[kid]["gegenpruefung"] if g["linse"].lower().startswith("oekonomie") or g["linse"].lower().startswith("ökonomie")]
    return gp[0]["modell_eingaben_korrigiert"]


VERGLEICHE = [
    ("Vergleich der 10 Shortlist-Kandidaten nach der Vertiefung (Eingaben der adversarialen Prüfer)",
     {kid: aus_pruefer(k) for kid, k in sorted(KANDIDATEN.items())}),
    ("Neuzuschnitt der 4 stärksten Kandidaten (korrigierte Eingaben der Ökonomie-Prüfer)",
     {kid: aus_eingaben(kid, f"{kid}: {NEUZUSCHNITT[kid]['titel']} – Neuzuschnitt", oekonomie_eingaben(kid)) for kid in sorted(NEUZUSCHNITT)}),
]

# ---------------------------------------------------------------------------
# FINALISTEN: korrigierte Eingaben der Ökonomie-Prüfer aus dem Neuzuschnitt
#   A = bedingter Finalist (Platz 1), D = Reserve. Begründung je Eingabe in PARAMETER_QUELLEN.
# ---------------------------------------------------------------------------
FINAL_NAMEN = {
    "A": "Finalist 1 (bedingt): KI-Designwelt Hochzeit – Designsystem + Phasen-Papeterie",
    "D": "Reserve: Kinderzimmer-Stilwelt – Wandwelt auf Maß aus Raumfoto",
}
PRODUKTE, SZENARIEN, REF_CAC = {}, {}, {}
PARAMETER_QUELLEN = []
for _kid, _name in FINAL_NAMEN.items():
    _mi = oekonomie_eingaben(_kid)
    PRODUKTE[_kid], SZENARIEN[_kid] = aus_eingaben(_kid, _name, _mi)
    REF_CAC[_kid] = _mi["cac_realistisch_basis"]
    for a in _mi["angebote"]:
        PARAMETER_QUELLEN.append((_kid, f"Angebot „{a['name']}“: {a['preis_brutto']} € brutto, Einkauf {a['einkauf_netto']} €, Versand {a['versand_netto']} €, "
                                  f"Mix K/B/O {a['mix_konservativ']:.0%}/{a['mix_basis']:.0%}/{a['mix_optimistisch']:.0%}", "siehe Text", "gemischt", a["label_und_quelle"]))
    for u in _mi["upsells"]:
        PARAMETER_QUELLEN.append((_kid, f"Upsell „{u['name']}“: {u['preis_brutto']} € brutto, Einkauf {u['einkauf_netto'] + u['versand_netto']:.2f} €, Quote {u['quote_basis']:.0%}",
                                  "siehe Text", "gemischt", u["label_und_quelle"]))
    for feld, label in [("vorschau_kauf_quote_konservativ", "ANNAHME"), ("vorschau_kauf_quote_basis", "ANNAHME"), ("vorschau_kauf_quote_optimistisch", "ANNAHME"),
                        ("kosten_vorschau_sitzung_eur", "ANNAHME auf BELEGTEN Modellpreisen"), ("kosten_finalisierung_eur", "ANNAHME auf BELEGTEN Modellpreisen"),
                        ("pruef_minuten", "ANNAHME"), ("support_minuten", "ANNAHME"), ("nachdruck_quote", "ANNAHME"), ("erstattung_quote", "ANNAHME"),
                        ("wiederkauf_12m", "ANNAHME"), ("wiederkauf_aov_faktor", "ANNAHME"),
                        ("cac_realistisch_konservativ", "ANNAHME auf SCHÄTZUNG-Benchmarks"), ("cac_realistisch_basis", "ANNAHME auf SCHÄTZUNG-Benchmarks"),
                        ("cac_realistisch_optimistisch", "ANNAHME auf SCHÄTZUNG-Benchmarks"), ("saison_spitzenfaktor", "ANNAHME (Saisonindex aus Google Trends, SCHÄTZUNG)")]:
        PARAMETER_QUELLEN.append((_kid, feld, str(_mi[feld]), label, "Herleitung siehe Begründung des Ökonomie-Prüfers (unten)"))
    PARAMETER_QUELLEN.append((_kid, "Begründung des Ökonomie-Prüfers", "–", "–", _mi["begruendung"]))
    PARAMETER_QUELLEN.append((_kid, "Szenario-Hebel (alle Kandidaten gleich)", str(SZ_HEBEL), "ANNAHME", "konservativ: Upsells ×0,7, Kosten ×1,05, Nachdruck/Erstattung ×1,5, Wiederkauf ×0,5; optimistisch: Upsells ×1,25, Nachdruck/Erstattung ×0,75, Wiederkauf ×1,3"))
    PARAMETER_QUELLEN.append((_kid, "Gemeinsame Annahmen", "Zahlung 2,3 % + 0,33 €; Beilage 0,50 €/Sendung; Infrastruktur 0,30 €; 30 €/h; Fixkosten 26/95/170/720 Tsd. € ab 0/0,5/1/5 Mio. €; Gründerlohn 120 Tsd. €",
                              "ANNAHME (Zahlungstarife BELEGT)", "Stripe/PayPal-Tarife laut Vorarbeit; Fixkostenstufen siehe Kommentar in parameter.py"))

# Testrechnung für den 14-Tage-Test von Finalist 1 (Meta-Kaltverkehr; Funnel Klick→Upload→Vorschau→Kauf, ANNAHME;
# CPC Meta DE 0,91 € Median, Q4 bis 1,33 € – Superads, SCHÄTZUNG)
TESTPLAN = {
    "faelle": [
        {"name": "Konservativ: 13 % × 65 % × 4 % = 0,34 %, CPC 1,05 €", "conversion": 0.13 * 0.65 * 0.04, "cpc": 1.05, "bestellungen": 20},
        {"name": "Basis: 15 % × 70 % × 6 % = 0,63 %, CPC 0,95 €", "conversion": 0.15 * 0.70 * 0.06, "cpc": 0.95, "bestellungen": 20},
        {"name": "Optimistisch: 18 % × 75 % × 10 % = 1,35 %, CPC 0,91 €", "conversion": 0.18 * 0.75 * 0.10, "cpc": 0.91, "bestellungen": 20},
        {"name": "Fest gedeckeltes Testbudget 3.000 € bei Basis-Funnel", "conversion": 0.15 * 0.70 * 0.06, "cpc": 0.95, "bestellungen": 3000 / 0.95 * 0.15 * 0.70 * 0.06},
    ],
    "hinweis": "Funnel-Quoten sind ANNAHMEN (Neuzuschnitt und Ökonomie-Prüfer A); der Test misst sie. 20 Bestellungen sind statistisch nur ein grobes Signal (95-%-Intervall bei 20 Käufen etwa ±45 %).",
}
