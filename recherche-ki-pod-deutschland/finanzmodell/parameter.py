"""
Eingaben des Finanzmodells je Finalist.

Kennzeichnung in PARAMETER_QUELLEN: BELEGT / ANBIETERANGABE / SCHÄTZUNG / ANNAHME.
Alles, was dort nicht steht, ist ANNAHME. Recherchestand 30.09.2026.
Wechselkurs: 1 USD = 0,86 EUR (ANNAHME, wie in den Produktionsanalysen verwendet).
"""
from dataclasses import replace

from finanzmodell import Produkt, Szenario

USD = 0.86  # ANNAHME Wechselkurs

PRODUKTE = {}
SZENARIEN = {}
PARAMETER_QUELLEN = {}

# ---------------------------------------------------------------------------
# Finalist 1: Haustier-Gedenkporträt „Wiedervereint“ (Mensch + verstorbenes Tier aus getrennten Fotos)
# ---------------------------------------------------------------------------
# Produktmix (ANNAHME) mit Printful-Einkaufspreisen (USD, Katalog-API und Versandseite, 30.09.2026):
#   Kern „Wiedervereint“ Leinwand 20×28″ (≈51×71 cm)  129 € brutto  34,95 USD + Versand Leinwand M 11,39 USD (ES)
#   Einzeltier-Gedenkporträt Leinwand 16×20″          89 € brutto  28,56 USD + 11,39 USD (ES)
#   Gedenk-Set: Leinwand 20×28″ + Tasse 11 oz + Decke 50×60″ 169 € brutto
#               34,95 + 6,07 + 29,36 USD; Versand 11,39 (ES) + 7,29 Decke + 2,05 Tasse als Zusatzstück (LV)
MIX = {  # Anteil, Preis brutto €, Herstellung USD, Versand USD
    "kern": (0.55, 129.0, 34.95, 11.39),
    "einzeltier": (0.25, 89.0, 28.56, 11.39),
    "set": (0.20, 169.0, 34.95 + 6.07 + 29.36, 11.39 + 7.29 + 2.05),
}
# Mix-Anteile je Szenario (ANNAHME): vorsichtig mehr Einzeltier und 10 % Rabatt, optimistisch mehr Sets
MIX_ANTEILE = {
    "Basis": {"kern": 0.55, "einzeltier": 0.25, "set": 0.20},
    "Vorsichtig": {"kern": 0.45, "einzeltier": 0.45, "set": 0.10},
    "Optimistisch": {"kern": 0.50, "einzeltier": 0.15, "set": 0.35},
}
RABATT = {"Basis": 0.0, "Vorsichtig": 0.10, "Optimistisch": 0.0}


def _mix(szenario):
    ant = MIX_ANTEILE[szenario]
    preis = sum(ant[k] * MIX[k][1] for k in MIX) * (1 - RABATT[szenario])
    herst = sum(ant[k] * MIX[k][2] for k in MIX) * USD
    vers = sum(ant[k] * MIX[k][3] for k in MIX) * USD
    return preis, herst, vers


_preis, _herst, _vers = _mix("Basis")
_pv, _hv, _vv = _mix("Vorsichtig")
_po, _ho, _vo = _mix("Optimistisch")

PRODUKTE["gedenk"] = Produkt(
    key="gedenk",
    name="Finalist 1 – Haustier-Gedenkporträt „Wiedervereint“ (Leinwand/Set, EU-POD)",
    preis_brutto=round(_preis, 2),
    herstellung=round(_herst, 2),
    versand=round(_vers, 2),
    verpackung_beilage=1.0,
    ki_kosten_je_generierung=round(0.101 * USD + 0.005 * USD, 3),
    gen_je_kaeufer=8,
    gen_je_nichtkaeufer=3,
    ki_produktionsdatei=round(0.05 * USD, 3),
    pruef_minuten=10,
    support_minuten=5,
    nachdruck_quote=0.05,
    erstattung_quote=0.02,
    erstattung_anteil=0.5,
    partner_traegt_anteil_nachdruck=0.3,
    fixkosten_monat=280.0,
    einmalig_aufbau=1500.0 + 1900.0,
    testbudget=1500.0,
)
PARAMETER_QUELLEN["gedenk"] = {
    "preis_brutto": "ANNAHME: gewichteter Mix (MIX_ANTEILE) – Basis 55 % Kern-Leinwand 129 €, 25 % Einzeltier-Leinwand 89 €, 20 % Set 169 €; vorsichtig 45/45/10 % und 10 % Rabatt; optimistisch 50/15/35 %. Preisempfehlung der Marktanalyse 119–149 € für das Kernprodukt. DE-Anker bei ähnlichem Format deutlich niedriger (Pet Printed Gedenkleinwand 60×40 cm 44,95 €, BELEGT products.json).",
    "herstellung": "BELEGT (Preise) / ANNAHME (Mix, Kurs): Printful Katalog-API 30.09.2026 – Leinwand 20×28″ 34,95 USD (im Faktencheck verifiziert), 16×20″ 28,56 USD, Tasse 11 oz 6,07 USD, Decke 50×60″ 29,36 USD; × 0,86. Print API (NL) Leinwand 40×60 cm 16,21 € + 1,50 € Handling (ANBIETERANGABE) wäre günstiger.",
    "versand": "BELEGT (printful.com/shipping, USD): Leinwand M Europa 11,39 USD; Set mit zweitem Paket aus LV (Decke 7,29 USD + Tasse als Zusatzstück 2,05 USD); × 0,86. Risiko: EUR-Abrechnung mit gleichen Zahlenwerten (+15 %, siehe Sensitivität).",
    "verpackung_beilage": "ANBIETERANGABE 0,45 € Pick-Gebühr Einleger (Printful) + ANNAHME 0,55 € Druck Gedenkkarte.",
    "ki_kosten_je_generierung": "BELEGT: Gemini 3.1 Flash Image 2K 0,101 USD/Bild + ca. 0,005 USD Vision-Prüfung (ai.google.dev/gemini-api/docs/pricing, Stand 24.09.2026) × 0,86.",
    "gen_je_kaeufer": "ANNAHME (Produktionsanalyse): 8 Generierungen inkl. Re-Rolls; im Test messen.",
    "gen_je_nichtkaeufer": "ANNAHME: 3 Gratis-Vorschauen je Nichtkäufer, technisch begrenzt (Rate-Limit).",
    "ki_produktionsdatei": "BELEGT: Topaz Image Upscale bis 24 MP 0,05 USD (replicate.com).",
    "pruef_minuten": "ANNAHME: 15 Min. in der Testphase, 5 Min. skaliert → Jahresmittel 10 Min.",
    "support_minuten": "ANNAHME.",
    "nachdruck_quote": "ANNAHME: 5–8 % Testphase, Ziel < 4 % (Produktionsanalyse); Printful meldet 0,24 % Qualitäts-Nachversand über alle Produkte (ANBIETERANGABE).",
    "partner_traegt_anteil_nachdruck": "ANNAHME: Produktions-/Transportschäden trägt der Partner (Printful-Policy BELEGT), Ähnlichkeitskulanz der Shop.",
    "fixkosten_monat": "ANNAHME aus Kostenbenchmarks: Shopify Basic ~36 €, Hosting/Speicher ~20 €, Rechtstexte 9,90 € (BELEGT), Buchhaltung 21,90 € (BELEGT), Versicherung ~30 €, Steuerberatung ~80 €, Tools/Apps ~40 €, Printful-Einlegerlager 22 € (ANBIETERANGABE), Lizenzero ~3 € (ANBIETERANGABE), Domain/Mail ~10 € = ca. 280 €.",
    "einmalig_aufbau": "ANNAHME: Testbudget 1.500 € (siehe testbudget) + Aufbau nach dem Test 1.900 € ohne Doppelung mit dem Test: Rechtsprüfung 700 €, Marke DPMA 290 € (optional), Branding/Mockups/Produktfotos 300 €, Start-Content 250 €, Partnermaterial 200 €, weitere Formatmuster 100 €, Tools/Setup 60 €.",
    "testbudget": "ANNAHME (14-Tage-Plan): Muster 300 €, KI-Tests 80 €, Landingpage 60 €, Rechtstexte 30 €, Rechts-/Datenschutz-Kurzcheck vor Live-Test 250 €, Werbung 600 €, Creator 150 €, Reserve 30 €.",
    "sz_kosten_faktor": "ANNAHME: Herstell-/Versandkosten des jeweiligen Szenario-Mix relativ zum Basis-Mix.",
    "sz_preis_faktor": "ANNAHME: Ø Warenkorb des jeweiligen Szenario-Mix relativ zum Basis-Mix.",
    "sz_cpc": "SCHÄTZUNG: Meta DE CPC ca. 0,91 € (Superads, Median-Werte Jul 2025–Jul 2026, branchenübergreifend; Spanne 0,76–1,33 €).",
    "sz_start_quote": "ANNAHME (kein Beleg für Vorschau-Starts).",
    "sz_bestell_quote": "ANNAHME: Gesamt-Conversion Besuch→Bestellung Basis 1,6 % (0,20 × 0,08); Benchmarks 1,4 % Shopify-Median, 2,86 % EMEA (SCHÄTZUNG).",
    "sz_partner_bestellungen_max": "ANNAHME: Empfehlungen über Tierbestatter/Tierärzte (Rosengarten >60 Standorte, ANUBIS 22 Partner – ANBIETERANGABE); Einlösequote unbekannt, wird im 14-Tage-Test NICHT gemessen (zweite Prüfphase).",
    "sz_partner_provision": "ANNAHME: 15 % vom Nettoumsatz.",
    "sz_organisch_max": "ANNAHME: SEO/Pinterest/organisches Social nach 12 Monaten; setzt laufende Content-Kosten voraus; wird im 14-Tage-Test NICHT gemessen.",
    "sz_zahl_prozent": "ANNAHME Mix aus BELEGT: Stripe EWR-Karte 1,5 % + 0,25 €, PayPal 2,99 % + 0,39 €, Klarna ab 2,99 % + 0,35 €.",
    "sz_unternehmerlohn_monat": "ANNAHME: kalkulatorisch 2.500 €/Monat (ca. 0,6 FTE).",
    "sz_stundensatz_fremd": "ANNAHME: Minijob/Freelancer inkl. Nebenkosten.",
}
_basis_budget = [600, 700, 800, 900, 1000, 1000, 1200, 1200, 1400, 1400, 1500, 1500]
SZENARIEN["gedenk"] = {
    "Vorsichtig": Szenario(
        name="Vorsichtig", preis_faktor=_pv / _preis, kosten_faktor=(_hv + _vv) / (_herst + _vers), cpc=1.10, start_quote=0.15, bestell_quote=0.06,
        lernkurve_start=0.6, werbebudget_plan=[500] * 12, werbe_gate=True, werbe_minimum=200,
        organisch_max=600, organisch_rampe_monate=12, content_kosten_monat=250,
        partner_start_monat=5, partner_rampe_monate=6, partner_bestellungen_max=8, partner_provision=0.15,
        partner_kosten_monat=40, wiederkauf_quote_monat=0.003, gen_faktor=1.3, nachdruck_faktor=1.4,
        zahl_prozent=0.02, zahl_fix=0.28),
    "Basis": Szenario(
        name="Basis", cpc=0.90, start_quote=0.20, bestell_quote=0.08, lernkurve_start=0.6,
        werbebudget_plan=_basis_budget, werbe_gate=True, werbe_minimum=300,
        organisch_max=1500, organisch_rampe_monate=12, content_kosten_monat=400,
        partner_start_monat=4, partner_rampe_monate=6, partner_bestellungen_max=20, partner_provision=0.15,
        partner_kosten_monat=60, wiederkauf_quote_monat=0.005, zahl_prozent=0.02, zahl_fix=0.28),
    "Optimistisch": Szenario(
        name="Optimistisch", preis_faktor=_po / _preis, kosten_faktor=(_ho + _vo) / (_herst + _vers), cpc=0.80, start_quote=0.22, bestell_quote=0.09,
        lernkurve_start=0.7, werbebudget_plan=[800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2500, 2500],
        werbe_gate=True, werbe_minimum=400, organisch_max=3000, organisch_rampe_monate=12, content_kosten_monat=600,
        partner_start_monat=3, partner_rampe_monate=6, partner_bestellungen_max=35, partner_provision=0.15,
        partner_kosten_monat=80, wiederkauf_quote_monat=0.008, nachdruck_faktor=0.8, zahl_prozent=0.02, zahl_fix=0.28),
}


# ---------------------------------------------------------------------------
# Vergleichsrechnungen (KEINE Finalisten): GELB bewertete Nischen, nur Basis-Szenario.
# Gleiche Kanal-Annahmen wie Finalist 1 (Basis), aber ohne Partnerkanal – so werden
# Unterschiede in der Stückwirtschaft sichtbar. Quellen: rohdaten/vertiefung-ergebnisse*.json
# ---------------------------------------------------------------------------
def _vergleich_szenario(bestell_quote=0.08, wiederkauf=0.005):
    return {"Basis": Szenario(
        name="Basis", cpc=0.90, start_quote=0.20, bestell_quote=bestell_quote, lernkurve_start=0.6,
        werbebudget_plan=_basis_budget, werbe_gate=True, werbe_minimum=300,
        organisch_max=1500, organisch_rampe_monate=12, content_kosten_monat=400,
        wiederkauf_quote_monat=wiederkauf, zahl_prozent=0.02, zahl_fix=0.28)}


PRODUKTE["karten"] = Produkt(
    key="karten", name="Vergleich (kein Finalist) – Personalisiertes KI-Kartendeck (Mix Tarot/Orakel/Skat/Quartett, meinspiel Hamburg)",
    preis_brutto=69.0, herstellung=22.0, versand=4.6, verpackung_beilage=0.0,
    ki_kosten_je_generierung=round(0.101 * USD, 3), gen_je_kaeufer=70, gen_je_nichtkaeufer=4, ki_produktionsdatei=0.0,
    pruef_minuten=20, support_minuten=5, nachdruck_quote=0.04, erstattung_quote=0.02, erstattung_anteil=0.5,
    partner_traegt_anteil_nachdruck=0.3, fixkosten_monat=280.0, einmalig_aufbau=3400.0, testbudget=1500.0)
PARAMETER_QUELLEN["karten"] = {
    "preis_brutto": "ANNAHME Mix aus Preisempfehlung der Marktanalyse (Tarot 89 €, Orakel 69 €, Skat/Quartett 49,90 €).",
    "herstellung": "BELEGT/ANNAHME: meinspiel 80 Karten 34,95 € brutto = 29,37 € netto, 40 Karten 22,95 € brutto, 33 Karten 16,95 € + Box 4,95 € (meinspiel.de, 30.09.2026, B2C-Preise); Mix ≈ 22 €.",
    "versand": "BELEGT: DHL Warenpost 4,95 € / Paket 5,95 € brutto (meinspiel.de); Mix.",
    "gen_je_kaeufer": "ANNAHME (Produktionsanalyse): Tarot 105–115, Quartett 45–50, Skat 20–30 Generierungen.",
    "pruef_minuten": "ANNAHME: Testphase 15–40 Min., skaliert 5–10 Min.",
}
SZENARIEN["karten"] = _vergleich_szenario()

PRODUKTE["hochzeit"] = Produkt(
    key="hochzeit", name="Vergleich (kein Finalist) – KI-illustrierte Hochzeitspapeterie (Save-the-Date/Einladung, WIRmachenDRUCK)",
    preis_brutto=175.0, herstellung=50.0, versand=3.0, verpackung_beilage=0.0,
    ki_kosten_je_generierung=round(0.134 * USD, 3), gen_je_kaeufer=15, gen_je_nichtkaeufer=4, ki_produktionsdatei=0.1,
    pruef_minuten=35, support_minuten=10, nachdruck_quote=0.04, erstattung_quote=0.02, erstattung_anteil=0.5,
    partner_traegt_anteil_nachdruck=0.3, fixkosten_monat=280.0, einmalig_aufbau=3400.0, testbudget=1500.0)
PARAMETER_QUELLEN["hochzeit"] = {
    "preis_brutto": "ANNAHME Mix: Einstiegsset Save-the-Date 159 €, Einladungsphase ca. 265 € (Marktanalyse), gewichtet zum Erstkauf hin → 175 €; DE-Papeterie-Budget Ø 338 € (Bridebook, ANBIETERANGABE).",
    "herstellung": "BELEGT/ANNAHME: WIRmachenDRUCK 100 A5-Klappkarten 38,35 € + 250 C5-Umschläge 15,85 € netto inkl. Versand DE (30.09.2026); Mix mit Save-the-Date-Postkarten ≈ 50 €.",
    "gen_je_kaeufer": "ANNAHME (Produktionsanalyse): 12–25 Generierungen; Nano Banana Pro 0,134 USD (BELEGT).",
    "sz_wiederkauf_quote_monat": "ANNAHME: 3 %/Monat ≈ 36 % Folgekäufe in 12 Monaten (Save-the-Date → Einladung → Tag-der-Hochzeit); der Prüfer hält ≥ 40 % für nötig und durch mitgelieferte Dateien gefährdet.",
    "pruef_minuten": "ANNAHME: Testphase 25–40 Min. (Text-/Datumsprüfung!), skaliert 8–15 Min.; hier 35 Min. inkl. Designerzeit.",
}
SZENARIEN["hochzeit"] = _vergleich_szenario(wiederkauf=0.03)

PRODUKTE["gemalt"] = Produkt(
    key="gemalt", name="Vergleich (kein Finalist) – Handgemaltes Ölporträt nach KI-Entwurf (Studio Xiamen, Made-to-Order)",
    preis_brutto=229.0, herstellung=60.2, versand=21.5, verpackung_beilage=14.5,
    ki_kosten_je_generierung=round(0.067 * USD, 3), gen_je_kaeufer=15, gen_je_nichtkaeufer=6, ki_produktionsdatei=0.0,
    pruef_minuten=30, support_minuten=10, nachdruck_quote=0.08, erstattung_quote=0.03, erstattung_anteil=0.5,
    partner_traegt_anteil_nachdruck=0.3, fixkosten_monat=280.0, einmalig_aufbau=3400.0, testbudget=1500.0)
PARAMETER_QUELLEN["gemalt"] = {
    "preis_brutto": "ANNAHME (Marktanalyse 229 € für 40×50 cm Öl). Umsatzsteuer hier 19 % angesetzt: Der ermäßigte Satz für Kunstgegenstände gilt nach eigener Einschätzung nicht ohne Weiteres für den Weiterverkauf durch Händler (steuerlich zu prüfen).",
    "herstellung": "ANNAHME: 70 USD × 0,86 (Studio-Listings 30–190 USD, ANBIETERANGABE made-in-china.com).",
    "versand": "SCHÄTZUNG: Express-Rolle Xiamen→DE 25 USD.",
    "verpackung_beilage": "SCHÄTZUNG: Verzollungs-/Auslagepauschale ca. 12 €, mögliche EU-Bearbeitungsgebühr ca. 2 €, Beilage 0,50 €.",
    "pruef_minuten": "ANNAHME: Testphase 35–60 Min., skaliert 12–20 Min.",
    "sz_bestell_quote": "ANNAHME: wegen höheren Preises niedrigere Bestellquote (5 %) als bei Finalist 1.",
}
SZENARIEN["gemalt"] = _vergleich_szenario(bestell_quote=0.05)


# Finalist 1 ohne Partnerkanal – für einen gleichwertigen Vergleich mit den Vergleichsnischen
PRODUKTE["gedenk_ohne_partner"] = replace(PRODUKTE["gedenk"], key="gedenk_ohne_partner",
                                          name="Vergleich – Finalist 1 ohne Partnerkanal (gleiche Kanalannahmen wie die Vergleichsnischen)")
PARAMETER_QUELLEN["gedenk_ohne_partner"] = PARAMETER_QUELLEN["gedenk"]
SZENARIEN["gedenk_ohne_partner"] = _vergleich_szenario()
