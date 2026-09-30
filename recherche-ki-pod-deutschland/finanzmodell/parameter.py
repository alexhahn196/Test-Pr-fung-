"""
Eingaben des Finanzmodells je Finalist.

Kennzeichnung in PARAMETER_QUELLEN: BELEGT / ANBIETERANGABE / SCHÄTZUNG / ANNAHME.
Alles, was dort nicht steht, ist ANNAHME. Recherchestand 30.09.2026.
Wechselkurs: 1 USD = 0,86 EUR (ANNAHME, wie in den Produktionsanalysen verwendet).
"""
from finanzmodell import Produkt, Szenario

USD = 0.86  # ANNAHME Wechselkurs

PRODUKTE = {}
SZENARIEN = {}
PARAMETER_QUELLEN = {}

# ---------------------------------------------------------------------------
# Finalist 1: Haustier-Gedenkporträt „Wiedervereint“ (Mensch + verstorbenes Tier aus getrennten Fotos)
# ---------------------------------------------------------------------------
PRODUKTE["gedenk"] = Produkt(
    key="gedenk",
    name="Finalist 1 – Haustier-Gedenkporträt „Wiedervereint“ (Leinwand/Poster/Set, EU-POD)",
    preis_brutto=119.0,
    herstellung=29.0,
    versand=9.8,
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
    einmalig_aufbau=2400.0,
    testbudget=1300.0,
)
PARAMETER_QUELLEN["gedenk"] = {
    "preis_brutto": "ANNAHME: Ø-Warenkorb aus Mix „Wiedervereint“-Leinwand 129 €, Einzeltier 69–99 €, Set 169 €; Preiskorridor der Marktanalyse 119–149 €. DE-Anker 29,95–89,95 € (Pet Printed, BELEGT products.json) sprechen für Risiko nach unten → Szenario vorsichtig 105 €.",
    "herstellung": "BELEGT/ANNAHME: Printful Leinwand 20×28″ 35,70 USD (api.printful.com/products/3, 30.09.2026) × 0,86 = 30,70 €; Mix mit kleineren Formaten/Postern → 29 €. Print API (NL) 40×60 cm 16,21 € + 1,50 € Handling (ANBIETERANGABE) wäre günstiger.",
    "versand": "BELEGT: Printful Versand Leinwand Medium Europa 11,39 USD (printful.com/shipping, 30.09.2026) × 0,86. Risiko: EUR-Abrechnung mit gleichen Zahlenwerten (+15 %).",
    "verpackung_beilage": "ANBIETERANGABE 0,45 € Pick-Gebühr Einleger (Printful) + ANNAHME 0,55 € Druck Gedenkkarte.",
    "ki_kosten_je_generierung": "BELEGT: Gemini 3.1 Flash Image 2K 0,101 USD/Bild + ca. 0,005 USD Vision-Prüfung (ai.google.dev/pricing, Stand 24.09.2026) × 0,86.",
    "gen_je_kaeufer": "ANNAHME (Produktionsanalyse): 8 Generierungen inkl. Re-Rolls; im Test messen.",
    "gen_je_nichtkaeufer": "ANNAHME: 3 Gratis-Vorschauen je Nichtkäufer, technisch begrenzt (Rate-Limit).",
    "ki_produktionsdatei": "BELEGT: Topaz Image Upscale bis 24 MP 0,05 USD (replicate.com).",
    "pruef_minuten": "ANNAHME: 15 Min. in der Testphase, 5 Min. skaliert → Jahresmittel 10 Min.",
    "support_minuten": "ANNAHME.",
    "nachdruck_quote": "ANNAHME: 5–8 % Testphase, Ziel < 4 % (Produktionsanalyse); Printful meldet 0,24 % Qualitäts-Nachversand über alle Produkte (ANBIETERANGABE).",
    "partner_traegt_anteil_nachdruck": "ANNAHME: Produktions-/Transportschäden trägt der Partner (Printful-Policy BELEGT), Ähnlichkeitskulanz der Shop.",
    "fixkosten_monat": "ANNAHME aus Kostenbenchmarks: Shopify Basic ~36 €, Hosting/Speicher ~20 €, Rechtstexte 9,90 € (BELEGT), Buchhaltung 21,90 € (BELEGT), Versicherung ~30 €, Steuerberatung ~80 €, Tools/Apps ~40 €, Printful-Einlegerlager 22 € (ANBIETERANGABE), Lizenzero ~3 € (ANBIETERANGABE), Domain/Mail ~10 €.",
    "einmalig_aufbau": "ANNAHME: Muster 300 €, Rechtsprüfung (AGB/Widerruf/KI-VO/DSGVO) 700 €, Marke DPMA 290 € (optional), Branding/Mockups 400 €, KI-Testcredits/Tools 200 €, Start-Content 300 €, Partnermaterial 200 €.",
    "testbudget": "ANNAHME: siehe 14-Tage-Plan (Muster ~250 €, Werbung ~800 €, KI-Tests ~80 €, Creator ~150 €).",
    "sz_cpc": "SCHÄTZUNG: Meta DE Median-CPC 0,91 € (Superads Jul 2025–Jul 2026, Spanne 0,76–1,33 €).",
    "sz_start_quote": "ANNAHME (kein Beleg für Proof-Starts).",
    "sz_bestell_quote": "ANNAHME: Gesamt-Conversion Besuch→Bestellung Basis 1,6 % (0,20 × 0,08); Benchmarks 1,4 % Shopify-Median, 2,86 % EMEA (SCHÄTZUNG).",
    "sz_partner_bestellungen_max": "ANNAHME: Empfehlungen über Tierbestatter/Tierärzte (Rosengarten >60 Standorte, ANUBIS 22 Partner – ANBIETERANGABE); Einlösequote unbekannt.",
    "sz_partner_provision": "ANNAHME: 15 % vom Nettoumsatz.",
    "sz_organisch_max": "ANNAHME: SEO/Pinterest/organisches Social nach 12 Monaten; setzt laufende Content-Kosten voraus.",
    "sz_zahl_prozent": "ANNAHME Mix aus BELEGT: Stripe EWR-Karte 1,5 % + 0,25 €, PayPal 2,99 % + 0,39 €, Klarna ab 2,99 % + 0,35 €.",
    "sz_unternehmerlohn_monat": "ANNAHME: kalkulatorisch 2.500 €/Monat (ca. 0,6 FTE).",
    "sz_stundensatz_fremd": "ANNAHME: Minijob/Freelancer inkl. Nebenkosten.",
}
_basis_budget = [600, 700, 800, 900, 1000, 1000, 1200, 1200, 1400, 1400, 1500, 1500]
SZENARIEN["gedenk"] = {
    "Vorsichtig": Szenario(
        name="Vorsichtig", preis_faktor=105 / 119, cpc=1.10, start_quote=0.15, bestell_quote=0.06,
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
        name="Optimistisch", preis_faktor=129 / 119, cpc=0.75, start_quote=0.25, bestell_quote=0.10,
        lernkurve_start=0.7, werbebudget_plan=[800, 1000, 1300, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4000, 4000],
        werbe_gate=True, werbe_minimum=400, organisch_max=4000, organisch_rampe_monate=12, content_kosten_monat=600,
        partner_start_monat=3, partner_rampe_monate=6, partner_bestellungen_max=45, partner_provision=0.15,
        partner_kosten_monat=80, wiederkauf_quote_monat=0.008, nachdruck_faktor=0.8, zahl_prozent=0.02, zahl_fix=0.28),
}
