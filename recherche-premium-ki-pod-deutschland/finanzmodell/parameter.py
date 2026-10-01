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


def aus_pruefer(k, saison=None):
    """Baut Produkt und drei Szenarien aus den Modelleingaben des Prüfers."""
    mi = k["pruefer"]["modell_eingaben"]
    angebote = []
    for a in mi["angebote"]:
        s = max(1, int(round(a["sendungen"])))
        angebote.append(Angebot(a["name"], a["preis_brutto"],
                                [Position(a["name"], a["einkauf_netto"], 1, produkte=a["produkte"])],
                                sendungen=s, versand_je_sendung_netto=a["versand_netto"] / s,
                                produktionsdateien=max(1, int(round(a["produktionsdateien"])))))
    ups = [Upsell(u["name"], u["quote_basis"], u["preis_brutto"], u["einkauf_netto"], u["versand_netto"]) for u in mi["upsells"]]
    p = Produkt(k["id"], f"{k['id']}: {k['titel']}", angebote, ups, saison_spitzenfaktor=saison or mi["saison_spitzenfaktor"])
    szs = {}
    for n, h in SZ_HEBEL.items():
        key = SZ_KEY[n]
        mix = {a["name"]: a[f"mix_{key}"] for a in mi["angebote"]}
        tot = sum(mix.values())
        mix = {m: v / tot for m, v in mix.items()}  # auf 1 normieren
        szs[n] = Szenario(n, mix, upsell_faktor=h["upsell_faktor"], kosten_faktor=h["kosten_faktor"],
                          vorschau_kauf_quote=mi[f"vorschau_kauf_quote_{key}"],
                          kosten_vorschau_sitzung=mi["kosten_vorschau_sitzung_eur"],
                          kosten_finalisierung=mi["kosten_finalisierung_eur"],
                          pruef_minuten=mi["pruef_minuten"], support_minuten=mi["support_minuten"],
                          nachdruck_quote=mi["nachdruck_quote"] * h["nachdruck"],
                          erstattung_quote=mi["erstattung_quote"] * h["erstattung"],
                          wiederkauf_12m=mi["wiederkauf_12m"] * h["wiederkauf"],
                          wiederkauf_aov_faktor=mi["wiederkauf_aov_faktor"],
                          cac_realistisch=mi[f"cac_realistisch_{key}"], **GEMEINSAM)
    return p, szs


KANDIDATEN = _lade_kandidaten()
VERGLEICH = {kid: aus_pruefer(k) for kid, k in sorted(KANDIDATEN.items())}
VERGLEICH_TITEL = "Vergleich der 10 Shortlist-Kandidaten (Vertiefung, einheitliche Annahmen)"

# ---------------------------------------------------------------------------
# FINALISTEN (geprüfte Einzelwerte) – werden nach Abschluss der Vertiefung gesetzt
# ---------------------------------------------------------------------------
PRODUKTE = {}
SZENARIEN = {}
REF_CAC = {}
PARAMETER_QUELLEN = []
TESTPLAN = {}
