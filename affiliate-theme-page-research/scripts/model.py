"""
Affiliate-Funnel-Modell für KI-/faceless Instagram-Theme-Pages.

Rechnet für 30 Nische×Markt-Kombinationen in 4 Szenarien:
  Affiliate-Provision pro 1 Mio. organischer Views
  = monetarisierbare Link-Klicks × Σ_Kanal (Anteil × CVR × AOV × Provision × Netto-Faktor) × (1 − Retouren/Storno)

Alle Parameter sind entweder aus den Rohdaten in ../quellen/ abgeleitet (Quelle im Kommentar)
oder als MODEL ASSUMPTION gekennzeichnet. Ausführen:  python3 scripts/model.py
Erzeugt: 04_niche_economics.csv, 11_revenue_per_million_views.csv, scorecard.csv,
         diagramme/*.png, scripts/model_output.json
"""
import csv
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCEN = ["Conservative", "Base", "Strong", "Exceptional"]

# ---------------------------------------------------------------------------
# 1) Globale Funnel-Vektoren (Quelle: quellen/E_funnel_benchmarks.md, Abschnitt M1–M5)
# ---------------------------------------------------------------------------
# Link-Klicks pro 1.000 Reel-Views, Comment-to-DM + Bio-Link kombiniert (E, M2) – MODEL ASSUMPTION
CLICKS_PER_1K = [0.25, 1.2, 3.0, 7.5]

# Kaufintention (Rubrik 1–5) -> Multiplikator auf die Klickrate. Anker: Die E-Benchmarks stammen
# überwiegend aus Shopping-/Amazon-Finds-Kontexten (CreatorFlow, Linktree) = Intent 4 = 1,0. MODEL ASSUMPTION
INTENT_FACTOR = {1: 0.3, 2: 0.5, 3: 0.75, 4: 1.0, 5: 1.2}

# Anteil monetarisierbarer Klicks nach Publikums-Geografie (F, Abschnitt 8: EN-Finds-Kanal US 41,7 %,
# IN 24,1 %, UK/CA/AU 34 %; DE-Kanäle ≈80 % DACH). Mit Geo-Routing (Geniuslink/OneLink). MODEL ASSUMPTION
GEO = {
    "EN": [0.45, 0.55, 0.62, 0.68],   # international englisch, Links US + Geo-Routing UK/CA/AU
    "US": [0.45, 0.55, 0.62, 0.68],   # US-Programme, EN-Content -> gleiches Publikum, Nicht-US-Klicks teils wertlos
    "DE": [0.72, 0.80, 0.85, 0.88],   # DACH (DE+AT über amazon.de; CH nur teilweise)
}

# Shop-Conversion Klick -> Bestellung (E, M3) – MODEL ASSUMPTION auf Basis Dynamic Yield/IRP/Geniuslink
CVR = {
    "AMZ_US": [0.02, 0.04, 0.07, 0.10],       # Geniuslink Q1/2022 Amazon.com 11,1 % (inkl. Halo), Social-Abschlag
    "AMZ_DE": [0.015, 0.03, 0.05, 0.07],      # Geniuslink Amazon.de 5,94 %
    "HOME": [0.003, 0.007, 0.015, 0.025],     # DY Home & Furniture 1,22 %
    "ELEC": [0.004, 0.009, 0.018, 0.025],     # DY Consumer Goods 1,6–2,5 %
    "SPORT": [0.004, 0.009, 0.018, 0.025],    # IRP Sports 2,11 %
    "BEAUTY": [0.01, 0.02, 0.035, 0.05],      # DY Beauty 5,39 %
    "FASHION": [0.005, 0.01, 0.02, 0.03],     # DY Fashion 2,77 %, IRP 1,86 %
    "PETS": [0.008, 0.018, 0.03, 0.045],      # DY Pet 4,71 %
    "LUX": [0.001, 0.003, 0.006, 0.01],       # DY Luxury & Jewelry 0,63–0,72 %
    # Produkte >2.000 €/$: kein Benchmark gefunden -> Ableitung: Luxury-CVR (AOV 426 $) halbiert/gedrittelt
    "HIGHTICKET": [0.0002, 0.0005, 0.0012, 0.002],
    "TRAVEL": [0.002, 0.005, 0.010, 0.015],   # Buchungen, keine Primärquelle -> MODEL ASSUMPTION
}

# Retouren + Storno als Provisionsverlust (E, M5). Amazon zahlt bei Retoure/Storno keine Provision (VERIFIED)
RET = {
    ("fashion", "US"): [0.35, 0.25, 0.20, 0.15], ("fashion", "DE"): [0.55, 0.45, 0.35, 0.25],
    ("elec", "US"): [0.15, 0.10, 0.08, 0.05], ("elec", "DE"): [0.18, 0.14, 0.10, 0.07],
    ("home", "US"): [0.15, 0.10, 0.07, 0.05], ("home", "DE"): [0.18, 0.12, 0.09, 0.06],
    ("beauty", "US"): [0.10, 0.06, 0.04, 0.02], ("beauty", "DE"): [0.12, 0.08, 0.05, 0.03],
    ("pets", "US"): [0.08, 0.05, 0.03, 0.02], ("pets", "DE"): [0.10, 0.06, 0.04, 0.02],
    ("sport", "US"): [0.20, 0.12, 0.09, 0.06], ("sport", "DE"): [0.30, 0.20, 0.14, 0.10],
    ("lux", "US"): [0.30, 0.20, 0.15, 0.10], ("lux", "DE"): [0.35, 0.25, 0.18, 0.12],
    ("travel", "US"): [0.35, 0.25, 0.20, 0.15],  # Reise-Stornos, Provision erst nach Reise (D, 2.2) – ASSUMPTION
}

# Wechselkurse – MODEL ASSUMPTION (Größenordnung 2025/26; Sensitivität gering ggü. Funnel-Unsicherheit)
FX = {"EUR": 1.0, "USD": 0.86, "GBP": 1.16}
# Provision wird i. d. R. auf den Nettowarenwert berechnet (ohne USt/Versand). US-Preise sind netto.
NET = {"DE": 1 / 1.19, "US": 1.0, "EN": 0.97}

# Laufende Kosten (H, Abschnitt 9.4: 60 Reels ≈ 320–810 $, 120 Reels ≈ 530–1.290 $) – MODEL ASSUMPTION
MONTHLY_COST_EUR = 600  # ~90 Reels/Monat, günstiger/mittlerer Video-Stack + Fixkosten
REELS_PER_MONTH = 90

# Realistisch erreichbare Views/Monat nach ~12 Monaten guter Umsetzung (Base / Strong) – MODEL ASSUMPTION.
# Herleitung: Views/Reel ≈ 0,5 × Follower (SupGrowth-Median 47–112 %), ~75–90 Reels/Monat;
# EN-Base ≈ Page mit 80–130k Followern, EN-Strong ≈ 300–500k; DE-Deckel: ≈37 Mio. dt. IG-Nutzer (F, 1.3).
REACH = {
    ("EN", "broad"): (5e6, 20e6), ("EN", "medium"): (3e6, 10e6), ("EN", "small"): (1.5e6, 5e6),
    ("DE", "broad"): (2e6, 7e6), ("DE", "medium"): (1e6, 4e6), ("DE", "small"): (0.5e6, 2e6),
}

# Ausnahme-Reichweite (Top-Page, 0,5–1 Mio. Follower EN bzw. ~500k DE, vgl. dealbunny.de 988k, echtemamas 526k) – MODEL ASSUMPTION
REACH_EXC = {
    ("EN", "broad"): 50e6, ("EN", "medium"): 25e6, ("EN", "small"): 12e6,
    ("DE", "broad"): 20e6, ("DE", "medium"): 10e6, ("DE", "small"): 5e6,
}

WEIGHTS = {  # Vorgabe des Auftraggebers (Teil 23)
    "econ": 0.20, "intent": 0.15, "viral": 0.15, "comp": 0.10, "ai": 0.10,
    "passiv": 0.10, "intl": 0.05, "variety": 0.05, "compliance": 0.05, "cross": 0.05,
}

# ---------------------------------------------------------------------------
# 2) Nische×Markt-Kombinationen
#    ch = (Kanal, Klick-Anteil, CVR-Schlüssel, CVR-Multiplikator, AOV in Landeswährung, Provision)
#    Scores (1–5): intent, viral, comp, ai, passiv, intl, variety, compliance, cross
# ---------------------------------------------------------------------------
C = []


def combo(**kw):
    C.append(kw)


combo(id="K01", label="Desk Setups – EN/INT", niche="Desk Setup / Home Office", market="EN", cur="USD", ret="elec", reach="medium",
      ch=[("Amazon.com", 0.70, "AMZ_US", 0.8, 60, 0.035), ("Brands (FlexiSpot, Logitech, Grovemade, Nanoleaf …)", 0.30, "ELEC", 1.0, 250, 0.06)],
      intent=4, viral=4, comp=2, ai=4, passiv=3, intl=4, variety=5, compliance=4, cross=4,
      note="Amazon US: Electronics 4 %, PC 2,5 %, Home/Furniture 3 % (A). FlexiSpot UK 4–8 % AOV 292 £, Logitech 4–10 % AOV 125 $ (B).")
combo(id="K02", label="Desk Setups – DE/DACH", niche="Desk Setup / Home Office", market="DE", cur="EUR", ret="elec", reach="medium",
      ch=[("Amazon.de", 0.75, "AMZ_DE", 0.8, 55, 0.035), ("Brands (noblechairs, FlexiSpot, Govee, Ugreen, nbb)", 0.25, "ELEC", 1.0, 220, 0.05)],
      intent=4, viral=3, comp=4, ai=4, passiv=3, intl=3, variety=5, compliance=4, cross=3,
      note="Amazon.de: Elektronik 3 %, Wohnen/Möbel 5 %, Mobile Elektronik 2,5 % (A). noblechairs 5 %, FlexiSpot DE 4 % AOV 247 €, Govee 5–12 % (B).")
combo(id="K03", label="Gaming Setups – EN/INT", niche="Gaming Setup", market="EN", cur="USD", ret="elec", reach="broad",
      ch=[("Amazon.com", 0.80, "AMZ_US", 0.8, 50, 0.03), ("Brands (Logitech G, Corsair, Secretlab)", 0.20, "ELEC", 1.0, 150, 0.05)],
      intent=3, viral=5, comp=2, ai=5, passiv=2, intl=4, variety=5, compliance=4, cross=4, geo_override=[0.35, 0.45, 0.55, 0.62],
      note="PC 2,5 %, Videospiele 1 %, Electronics 4 % (A). Gaming-Publikum jünger/globaler -> Geo-Abschlag (J: Monetarisierung oft mit Billigprodukten).")
combo(id="K04", label="Home Decor Finds – DE/DACH", niche="Interior / Home Decor Finds", market="DE", cur="EUR", ret="home", reach="broad",
      ch=[("Amazon.de", 0.70, "AMZ_DE", 1.0, 40, 0.05), ("Shops (Connox 8 %/60 T, Nordic Nest 8 %, Desenio, Lampenwelt)", 0.30, "HOME", 1.0, 120, 0.08)],
      intent=4, viral=4, comp=4, ai=3, passiv=3, intl=3, variety=5, compliance=3, cross=4,
      note="Amazon.de Wohnen/Möbel 5 % (VERIFIED, A). EN-Content-Dichte Wohnen 19,5× höher als DE (F 7.2). Keine DE faceless Home-Finds-Page >100k gefunden (I).")
combo(id="K05", label="Home Decor Finds – US", niche="Interior / Home Decor Finds", market="US", cur="USD", ret="home", reach="broad",
      ch=[("Amazon.com", 0.65, "AMZ_US", 1.0, 45, 0.03), ("Shops (AllModern 8 %/45 T, Wayfair, Ruggable, LTK/ShopMy)", 0.35, "HOME", 1.0, 180, 0.07)],
      intent=4, viral=5, comp=1, ai=3, passiv=3, intl=3, variety=5, compliance=3, cross=4,
      note="Amazon US Home/Furniture 3 % (A). Williams-Sonoma-Gruppe 1 %/1 Tag, schließt anonyme Accounts aus (A). ≥12 EN Home-Theme-Pages >100k (I).")
combo(id="K06", label="Küche & Küchengadgets – DE", niche="Küche / Küchengadgets", market="DE", cur="EUR", ret="home", reach="broad",
      ch=[("Amazon.de", 0.75, "AMZ_DE", 1.0, 35, 0.05), ("Brands (Zwilling 6,4–8 %, KitchenAid 7 %, SharkNinja 5 %, WMF)", 0.25, "ELEC", 1.0, 140, 0.06)],
      intent=5, viral=4, comp=4, ai=3, passiv=4, intl=3, variety=4, compliance=3, cross=4,
      note="Amazon.de Küche 5 % (A). SharkNinja DE 5 %, AOV 146 € (B). DE-Küchen-Hashtags nicht messbar, aber 'Amazon-Fundstücke/Haushalt' 25,6× Lücke (F); keine DE-Küchen-Theme-Page gefunden (I).")
combo(id="K07", label="Küche & Küchengadgets – US", niche="Küche / Küchengadgets", market="US", cur="USD", ret="home", reach="broad",
      ch=[("Amazon.com", 0.75, "AMZ_US", 1.0, 35, 0.045), ("Brands (KitchenAid 5 %, Zwilling 6 %, Caraway 32–52 $ fix)", 0.25, "ELEC", 1.0, 180, 0.06)],
      intent=5, viral=5, comp=1, ai=3, passiv=4, intl=3, variety=4, compliance=3, cross=4,
      note="Amazon US Kitchen 4,5 % (A). Justice Buys 2,1 Mio. YT / 616k IG -> Nische stark besetzt (I, J).")
combo(id="K08", label="Espresso-Setups – DE/DACH", niche="Kaffee / Espresso-Setups", market="DE", cur="EUR", ret="elec", reach="medium",
      ch=[("Amazon.de (Zubehör, Mühlen)", 0.50, "AMZ_DE", 0.8, 70, 0.05), ("Brands/Shops (De'Longhi 7 %, Coffee Circle 60 T, Coffee Friend 10 %, Kaffee24)", 0.50, "ELEC", 0.75, 300, 0.07)],
      intent=4, viral=3, comp=3, ai=3, passiv=4, intl=3, variety=4, compliance=4, cross=4,
      note="De'Longhi DE bis 7 % (VERIFIED), AOV >200 € (B). DE-Kaffee-Community pro Nutzer ähnlich aktiv wie EN (F 7.2) -> kein DE-Konkurrenzvorteil.")
combo(id="K09", label="Espresso-Setups – EN/US", niche="Kaffee / Espresso-Setups", market="EN", cur="USD", ret="elec", reach="medium",
      ch=[("Amazon.com (Zubehör, Mühlen)", 0.50, "AMZ_US", 0.8, 70, 0.045), ("Brands (Breville bis 8 %, De'Longhi US bis 15 %)", 0.50, "ELEC", 0.75, 450, 0.07)],
      intent=4, viral=4, comp=2, ai=3, passiv=4, intl=4, variety=4, compliance=4, cross=4,
      note="Breville bis 8 % (CLAIMED), De'Longhi US bis 15 % (CLAIMED), AOV 398 $ (B). Modell nutzt 7 % (kein 'bis zu').")
combo(id="K10", label="Backyard Wellness (Sauna/Plunge) – US", niche="Backyard Wellness: Sauna, Cold Plunge, Hot Tub", market="US", cur="USD", ret="home", reach="small",
      ch=[("Amazon.com (Fass-Saunen, Plunges, Zubehör)", 0.40, "AMZ_US", 0.5, 120, 0.03), ("Brands (Sun Home 5 %, RecoSauna 7 %, Sweat Kingdom 5–10 %, Renu 7 %)", 0.60, "HIGHTICKET", 1.0, 5000, 0.055)],
      intent=3, viral=4, comp=3, ai=5, passiv=4, intl=2, variety=3, compliance=4, cross=4,
      note="Sun Home 5 %, Social ausdrücklich erlaubt; Saunen 12–45k $; Sweat Kingdom AOV 4–25k $ (C). High-Ticket-CVR ohne Benchmark (ASSUMPTION).")
combo(id="K11", label="Garten-Wellness (Sauna/Whirlpool/Pool) – DE", niche="Backyard Wellness: Sauna, Whirlpool, Pool", market="DE", cur="EUR", ret="home", reach="small",
      ch=[("Amazon.de", 0.40, "AMZ_DE", 0.6, 80, 0.035), ("Shops (Mein-Saunashop Ø851 €, Sauna24 8 %/90 T, AIDA 10 %, primepool Ø628 €)", 0.60, "LUX", 1.0, 650, 0.065)],
      intent=3, viral=3, comp=3, ai=5, passiv=4, intl=3, variety=3, compliance=4, cross=4,
      note="Adcell-gemessene Ø-Warenkörbe 387–851 € bei 4–10 % (C, VERIFIED). Saison gegenläufig (Sauna Winter / Pool Sommer).")
combo(id="K12", label="Grill & Pizzaofen – DE", niche="BBQ / Pizzaöfen / Outdoor Kitchen", market="DE", cur="EUR", ret="home", reach="medium",
      ch=[("Amazon.de", 0.50, "AMZ_DE", 0.9, 60, 0.04), ("Shops (SANTOS 10 %/7 %, Kuppelofen Ø766 €/90 T, Ooni 10 %, Gozney 5 %)", 0.50, "HOME", 1.0, 400, 0.075)],
      intent=4, viral=4, comp=3, ai=3, passiv=3, intl=3, variety=4, compliance=4, cross=4,
      note="SANTOS 10 % Eigenmarke / 7 % Fremdmarken, AOV >392 € netto; Ooni ab 10 % content-only (C). Starke Saisonalität März–August.")
combo(id="K13", label="BBQ & Outdoor Kitchen – US", niche="BBQ / Pizzaöfen / Outdoor Kitchen", market="US", cur="USD", ret="home", reach="medium",
      ch=[("Amazon.com", 0.50, "AMZ_US", 0.9, 60, 0.035), ("Brands (BBQGuys 6 %, Ooni 10 %, Solo Stove 5–10 %, Blackstone 5 %)", 0.50, "HOME", 1.0, 550, 0.065)],
      intent=4, viral=5, comp=2, ai=3, passiv=3, intl=3, variety=4, compliance=4, cross=4,
      note="BBQGuys 6 % (Impact) inkl. Outdoor-Küchen; Outer 5–8 %/90 T (C). Weber US nur 2 %.")
combo(id="K14", label="Tech Gadgets / Amazon Finds – EN/US", niche="Tech Gadgets / Amazon Finds", market="EN", cur="USD", ret="elec", reach="broad",
      ch=[("Amazon.com", 0.90, "AMZ_US", 1.0, 35, 0.04), ("Brands (Ugreen 8 %, Casetify 10 %, Nomad 10 %)", 0.10, "ELEC", 1.0, 80, 0.08)],
      intent=5, viral=5, comp=1, ai=2, passiv=2, intl=3, variety=4, compliance=2, cross=4,
      note="Amazon 'All other' 4 % (A). EN-Finds-Kanal: 41,7 % US, 24,1 % Indien (F 8). Hochgesättigt (Justice Buys, JayFindsThings 7,8 Mio.).")
combo(id="K15", label="Amazon-Fundstücke Gadgets – DE", niche="Tech Gadgets / Amazon Finds", market="DE", cur="EUR", ret="elec", reach="broad",
      ch=[("Amazon.de", 0.90, "AMZ_DE", 1.0, 35, 0.03), ("Brands (Ugreen 8 %, Govee 5–12 %)", 0.10, "ELEC", 1.0, 70, 0.07)],
      intent=5, viral=4, comp=4, ai=2, passiv=2, intl=2, variety=4, compliance=2, cross=3,
      note="Amazon.de 'Alle anderen' 3 %, Mobile Elektronik 2,5 % (A). Amazon-Finds-Content-Dichte EN 25,6× DE (F). Kein dedizierter DE-Finds-Kanal in Top-20 (F 7.3).")
combo(id="K16", label="Smart Home – DE", niche="Smart Home", market="DE", cur="EUR", ret="elec", reach="medium",
      ch=[("Amazon.de", 0.70, "AMZ_DE", 0.9, 60, 0.03), ("Brands (Nanoleaf 10 %, Govee, Ecovacs 5 %, Dyson 7 % Content)", 0.30, "ELEC", 1.0, 150, 0.07)],
      intent=3, viral=3, comp=4, ai=3, passiv=3, intl=3, variety=4, compliance=4, cross=3,
      note="Nanoleaf 10 % weltweit, Ring 10 % (A); eufy DE nur mit Genehmigung (A). Keine DE Smart-Home-Theme-Page belegt (I).")
combo(id="K17", label="Travel Gear – EN/US", niche="Travel Gear / Packing", market="EN", cur="USD", ret="sport", reach="medium",
      ch=[("Amazon.com (Gepäck 4 %)", 0.50, "AMZ_US", 0.9, 45, 0.04), ("Brands (NOMATIC 15 %, Tortuga 10 %, Travelpro 8–10 %, Bellroy 7 %, eSIM)", 0.50, "FASHION", 1.0, 180, 0.09)],
      intent=3, viral=4, comp=3, ai=4, passiv=4, intl=4, variety=4, compliance=4, cross=5,
      note="Tortuga 10 %, AOV >250 $ (VERIFIED); Travelpro 8–10 %, 45 T, AOV 165 $ (VERIFIED); Saily 15 % ohne Website (D).")
combo(id="K18", label="Beauty & Skincare – DE", niche="Beauty / Skincare", market="DE", cur="EUR", ret="beauty", reach="broad",
      ch=[("Amazon.de (Beauty 4 %)", 0.40, "AMZ_DE", 1.0, 30, 0.04), ("Shops (The Ordinary 13–20 %, Sephora DE 12 %, Lookfantastic 12 %)", 0.60, "BEAUTY", 1.0, 50, 0.12)],
      intent=4, viral=4, comp=2, ai=2, passiv=3, intl=3, variety=4, compliance=1, cross=4,
      note="Hohe Raten (D). Aber: KI darf keine Hautergebnisse zeigen; faceless Beauty ohne Vertrauen; HIGH Compliance (G).")
combo(id="K19", label="Beauty Devices – US", niche="Beauty Devices (LED, Tools)", market="US", cur="USD", ret="elec", reach="medium",
      ch=[("Amazon.com (Beauty 3 % / Luxury Beauty 10 %)", 0.40, "AMZ_US", 0.8, 50, 0.05), ("Brands (medicube 20 %, Foreo 6 %/60 T)", 0.60, "BEAUTY", 0.6, 250, 0.12)],
      intent=4, viral=4, comp=2, ai=2, passiv=3, intl=3, variety=2, compliance=1, cross=3,
      note="medicube 20 % (D). Wirkungsversprechen = Health-/Kosmetik-Claims -> HIGH (G).")
combo(id="K20", label="Fashion 'Shop the Look' – DE", niche="Fashion (faceless Outfits)", market="DE", cur="EUR", ret="fashion", reach="broad",
      ch=[("Amazon.de (Fashion 6 %)", 0.30, "AMZ_DE", 1.0, 45, 0.06), ("Shops (Breuninger 12 %, Lounge 12 %, Mango 6 %, OTTO via Stylink)", 0.70, "FASHION", 1.0, 120, 0.10)],
      intent=4, viral=4, comp=2, ai=2, passiv=1, intl=3, variety=5, compliance=2, cross=5,
      note="Breuninger 12 % (D). DE-Fashion-Retouren 45–55 % (E). Zalando/ABOUT YOU ohne öffentliches Programm (D).")
combo(id="K21", label="Golf-Simulatoren & Golf-Tech – US", niche="Golf / Golf-Simulatoren", market="US", cur="USD", ret="sport", reach="small",
      ch=[("Amazon.com (Sports 3 %)", 0.50, "AMZ_US", 0.7, 80, 0.03), ("Brands (SkyTrak 10–15 %, 2nd Swing 5–15 %)", 0.50, "HIGHTICKET", 2.0, 1500, 0.10)],
      intent=3, viral=3, comp=4, ai=3, passiv=4, intl=2, variety=3, compliance=4, cross=3,
      note="SkyTrak 15 % (Awin) / 10 % (CJ), Produkte >1.300 $ (D). Keine Golf-Affiliate-Theme-Page belegt (J).")
combo(id="K22", label="Camping & Power Stations – DE", niche="Camping / Vanlife / Power Stations", market="DE", cur="EUR", ret="sport", reach="medium",
      ch=[("Amazon.de (Sport 4 %, Elektronik 3 %)", 0.50, "AMZ_DE", 0.9, 60, 0.035), ("Shops (EcoFlow 5 %/7 T, Jackery 5–8 %, Bergfreunde 7 %)", 0.50, "SPORT", 0.6, 500, 0.06)],
      intent=3, viral=3, comp=3, ai=4, passiv=3, intl=3, variety=4, compliance=4, cross=4,
      note="EcoFlow DE 5 %, AOV 1.000 €, nur 7 T Cookie; Bergfreunde Bestätigungsrate nur 65 % (D).")
combo(id="K23", label="Hundeprodukte – DE", niche="Haustiere (Hund)", market="DE", cur="EUR", ret="pets", reach="broad",
      ch=[("Amazon.de (Haustier 3 %)", 0.60, "AMZ_DE", 1.0, 35, 0.03), ("Shops (Fressnapf 8 % Neukunden/60 T, ZooRoyal 11 %, wildfang 10–13 %)", 0.40, "PETS", 1.0, 55, 0.09)],
      intent=4, viral=5, comp=2, ai=2, passiv=4, intl=3, variety=4, compliance=3, cross=4,
      note="Fressnapf 8 % Neukunden (C). DE-Hunde-Community pro Nutzer ähnlich aktiv wie EN (F). KI-Hunde, die Produkte 'benutzen' = irreführend (G).")
combo(id="K24", label="Autozubehör & Pflege – DE", niche="Automotive Accessories / Car Care", market="DE", cur="EUR", ret="elec", reach="medium",
      ch=[("Amazon.de (Auto 5 %)", 0.80, "AMZ_DE", 1.0, 35, 0.05), ("Shops (Autodoc 8 %, kfzteile24 6–8 %, Nextbase 6 %)", 0.20, "ELEC", 1.0, 100, 0.07)],
      intent=4, viral=3, comp=3, ai=2, passiv=3, intl=3, variety=4, compliance=3, cross=3,
      note="Amazon.de Auto & Motorrad 5 % (A). Pflege-Ergebnisse müssen echt sein -> KI-Fit gering.")
combo(id="K25", label="Schlaf & Matratzen – US", niche="Schlaf / Matratzen", market="US", cur="USD", ret="lux", reach="small",
      ch=[("Amazon.com (Home 3 %)", 0.40, "AMZ_US", 0.8, 60, 0.03), ("Brands (DreamCloud 150 $/12 %, Nectar 8–12 %)", 0.60, "LUX", 1.0, 900, 0.12)],
      intent=2, viral=1, comp=3, ai=3, passiv=4, intl=2, variety=3, compliance=3, cross=2,
      note="DreamCloud 150 $ bzw. 12 %, Helix nur US-Traffic, Simba zahlt erst nach Probezeit (A).")
combo(id="K26", label="Garten & Gartendesign – DE", niche="Garten / Gardening", market="DE", cur="EUR", ret="home", reach="medium",
      ch=[("Amazon.de (Garten 3 %, Baumarkt 5 %)", 0.50, "AMZ_DE", 0.9, 45, 0.04), ("Shops (STIHL 8 %, Baldur 8 %/90 T, hagebau 10 % Content, Mähroboter)", 0.50, "HOME", 1.0, 120, 0.08)],
      intent=3, viral=3, comp=2, ai=4, passiv=2, intl=3, variety=4, compliance=3, cross=5,
      note="STIHL 8 % CPO; Plantura Stornoquote 41 % (C). DE-Garten-Community ähnlich aktiv (F) -> kein Vorteil.")
combo(id="K27", label="Home Gym – US", niche="Home Gym / Fitness Equipment", market="US", cur="USD", ret="sport", reach="medium",
      ch=[("Amazon.com (Sports 3 %)", 0.60, "AMZ_US", 0.8, 60, 0.03), ("Brands (REP 5 % US-only, Bowflex 3 %, Hyperice 5 %)", 0.40, "SPORT", 0.6, 500, 0.05)],
      intent=3, viral=4, comp=2, ai=3, passiv=4, intl=2, variety=4, compliance=3, cross=3,
      note="Rogue ohne Programm; REP nur US, keine bezahlte Social-Werbung (D).")
combo(id="K28", label="3D-Druck & Maker – US", niche="3D-Druck / Maker", market="US", cur="USD", ret="elec", reach="small",
      ch=[("Amazon.com (All other 4 %)", 0.50, "AMZ_US", 0.9, 45, 0.04), ("Brands (Bambu Lab 10 %, Creality 4–8 %, Anycubic 5 %/60 T)", 0.50, "ELEC", 0.75, 500, 0.08)],
      intent=4, viral=4, comp=3, ai=2, passiv=3, intl=4, variety=3, compliance=3, cross=3,
      note="Bambu Lab US 10 % (D). Community reagiert negativ auf KI-'Prints', die nie gedruckt wurden.")
combo(id="K29", label="AI Dream Interiors / Luxury Homes – EN", niche="AI-Interior / Luxury Homes (aspirational)", market="EN", cur="USD", ret="home", reach="broad",
      ch=[("Amazon.com ('ähnliche' Deko)", 0.60, "AMZ_US", 0.7, 60, 0.03), ("Möbel-Shops (AllModern 8 %)", 0.40, "HOME", 0.7, 400, 0.06)],
      intent=2, viral=5, comp=2, ai=5, passiv=5, intl=5, variety=3, compliance=3, cross=5,
      note="Dreamy Interior 315k / Bau Rausch 620k ohne Kauflinks (I, J). Views hoch, Kaufabsicht niedrig (K: Unterhaltungs-Views ~0–3 $/1 Mio.).")
combo(id="K30", label="Travel Destinations / Dream Trips – EN", niche="Travel Destinations (Booking)", market="EN", cur="USD", ret="travel", reach="broad",
      ch=[("Buchung (GetYourGuide 8 %, Viator 8 %, Booking-Anteil)", 1.00, "TRAVEL", 1.0, 300, 0.05)],
      intent=2, viral=5, comp=1, ai=3, passiv=3, intl=5, variety=3, compliance=2, cross=5,
      note="Expedia 7 T Cookie, nur 'consumed' Reisen; Airbnb ohne Programm seit 2021 (D).")

combo(id="K31", label="Küchen- & Kaffee-Setups – DE/DACH", niche="Kitchen & Coffee Setups (Geräte in KI-Szenen)", market="DE", cur="EUR", ret="elec", reach="broad",
      ch=[("Amazon.de (Küche 5 %)", 0.55, "AMZ_DE", 0.9, 45, 0.05), ("Brands (De'Longhi 7 %, Zwilling 6,4–8 %, KitchenAid 7 %, SharkNinja 5 %, Coffee Friend 10 %)", 0.45, "ELEC", 0.8, 260, 0.07)],
      intent=4, viral=4, comp=3, ai=4, passiv=4, intl=3, variety=5, compliance=4, cross=4, synth=True,
      note="Synthese aus K06 (#1) und K08: statische Geräte (Siebträger, Küchenmaschine, Messer, Kochgeschirr) per Freisteller in KI-Küchen. Programme: A, B.")
combo(id="K32", label="Kitchen & Coffee Setups – EN/US", niche="Kitchen & Coffee Setups (Geräte in KI-Szenen)", market="EN", cur="USD", ret="elec", reach="broad",
      ch=[("Amazon.com (Kitchen 4,5 %)", 0.55, "AMZ_US", 0.9, 45, 0.045), ("Brands (Breville bis 8 %, De'Longhi, KitchenAid 5 %, Zwilling 6 %)", 0.45, "ELEC", 0.8, 350, 0.065)],
      intent=4, viral=5, comp=2, ai=4, passiv=4, intl=4, variety=5, compliance=4, cross=4, synth=True,
      note="Synthese aus K07 und K09; EN-Spiegel des Gewinner-Konzepts. Programme: A, B.")


# ---------------------------------------------------------------------------
# 3) Rechnung
# ---------------------------------------------------------------------------
def rkey(c):
    mk = "DE" if c["market"] == "DE" else "US"
    return RET[(c["ret"], mk)]


def compute(c):
    fx = FX[c["cur"]]
    net = NET[c["market"]]
    geo = c.get("geo_override", GEO[c["market"]])
    ret = rkey(c)
    out = {}
    for i, s in enumerate(SCEN):
        clicks_total = 1e6 / 1000 * CLICKS_PER_1K[i] * INTENT_FACTOR[c["intent"]]
        clicks = clicks_total * geo[i]  # monetarisierbare Klicks
        orders = 0.0
        comm_gross = 0.0  # Provision vor Retouren, EUR
        gmv = 0.0
        for (_, share, ck, mult, aov, com) in c["ch"]:
            cvr = CVR[ck][i] * mult
            o = clicks * share * cvr
            orders += o
            gmv += o * aov * fx
            comm_gross += o * aov * fx * net * com
        comm_net = comm_gross * (1 - ret[i])
        blended_cvr = orders / clicks if clicks else 0
        out[s] = {
            "clicks_all_per_1m": clicks_total,
            "clicks_monetizable_per_1m": clicks,
            "orders_per_1m": orders,
            "blended_cvr": blended_cvr,
            "gmv_per_1m_eur": gmv,
            "commission_gross_per_1m_eur": comm_gross,
            "revenue_per_1m_eur": comm_net,
            "epc_eur": comm_net / clicks if clicks else 0,
            "comm_per_order_eff_eur": comm_net / orders if orders else 0,
            "return_rate": ret[i],
        }
    # Strukturkennzahlen (Base-Mix, nach Bestellanteilen gewichtet)
    b = 1
    wsum = sum(sh * CVR[ck][b] * m for (_, sh, ck, m, a, co) in c["ch"])
    aov_w = sum(sh * CVR[ck][b] * m * a * FX[c["cur"]] for (_, sh, ck, m, a, co) in c["ch"]) / wsum
    comm_nom = sum(sh * CVR[ck][b] * m * a * FX[c["cur"]] * co for (_, sh, ck, m, a, co) in c["ch"]) / wsum
    out["_struct"] = {
        "aov_eur": aov_w,
        "comm_rate_weighted": comm_nom / aov_w,
        "comm_per_order_nominal_eur": comm_nom,  # vor USt-Abzug und Retouren
        "comm_per_order_eff_eur": out["Base"]["comm_per_order_eff_eur"],
    }
    return out


def views_needed(rev_per_1m, profit):
    return (profit + MONTHLY_COST_EUR) / rev_per_1m * 1e6 if rev_per_1m > 0 else float("inf")


def econ_score(rev_base):
    lo, hi = 20.0, 800.0  # Log-Skala: 20 €/1 Mio. -> 1, 800 €/1 Mio. -> 5
    v = 1 + 4 * (math.log(max(rev_base, 1e-6)) - math.log(lo)) / (math.log(hi) - math.log(lo))
    return max(1.0, min(5.0, v))


def total_score(c, econ):
    vals = {"econ": econ, "intent": c["intent"], "viral": c["viral"], "comp": c["comp"], "ai": c["ai"],
            "passiv": c["passiv"], "intl": c["intl"], "variety": c["variety"], "compliance": c["compliance"], "cross": c["cross"]}
    return sum(WEIGHTS[k] * (vals[k] - 1) / 4 * 100 for k in WEIGHTS), vals


results = []
for c in C:
    r = compute(c)
    econ = econ_score(r["Base"]["revenue_per_1m_eur"])
    score, vals = total_score(c, econ)
    reach_base, reach_strong = REACH[("DE" if c["market"] == "DE" else "EN", c["reach"])]
    reach_exc = REACH_EXC[("DE" if c["market"] == "DE" else "EN", c["reach"])]
    results.append({"c": c, "r": r, "econ": econ, "score": score, "vals": vals,
                    "reach_base": reach_base, "reach_strong": reach_strong, "reach_exc": reach_exc})

results.sort(key=lambda x: -x["score"])

# ---------------------------------------------------------------------------
# 4) CSV-Ausgaben
# ---------------------------------------------------------------------------
def f0(x):
    return round(x) if x != float("inf") else "inf"


with open(os.path.join(ROOT, "04_niche_economics.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "kombination", "nische", "markt", "kanaele_und_programme", "aov_gewichtet_eur", "provision_gewichtet_pct",
                "provision_pro_bestellung_nominal_eur", "provision_pro_bestellung_effektiv_eur_nach_ust_und_retouren",
                "retourenquote_base_pct", "bestellungen_fuer_3k", "bestellungen_fuer_5k", "bestellungen_fuer_10k", "bestellungen_fuer_20k",
                "cvr_blended_base_pct", "klicks_fuer_10k_base", "views_fuer_10k_provision_base",
                "datenqualitaet", "quellen_notiz"])
    for x in results:
        c, r, s = x["c"], x["r"], x["r"]["_struct"]
        eff = s["comm_per_order_eff_eur"]
        cvr = r["Base"]["blended_cvr"]
        ctr = r["Base"]["clicks_monetizable_per_1m"] / 1e6
        chan = " | ".join(f"{n} ({int(sh*100)} % Klicks, AOV {a} {c['cur']}, {co*100:.1f} %)" for (n, sh, ck, m, a, co) in c["ch"])
        w.writerow([c["id"], c["label"], c["niche"], c["market"], chan, round(s["aov_eur"], 1), round(s["comm_rate_weighted"] * 100, 2),
                    round(s["comm_per_order_nominal_eur"], 2), round(eff, 2), round(r["Base"]["return_rate"] * 100),
                    f0(3000 / eff), f0(5000 / eff), f0(10000 / eff), f0(20000 / eff),
                    round(cvr * 100, 2), f0(10000 / eff / cvr), f0(10000 / eff / cvr / ctr),
                    "Provisionen/AOV: VERIFIED bzw. THIRD-PARTY laut quellen/raw_programs_*.csv; Klickanteile, CVR, Retouren, Geo: MODEL ASSUMPTION",
                    c["note"]])

with open(os.path.join(ROOT, "11_revenue_per_million_views.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    head = ["rang_score", "id", "kombination", "markt", "kaufintention_1_5"]
    for s in SCEN:
        head += [f"klicks_pro_1m_{s.lower()}", f"bestellungen_pro_1m_{s.lower()}", f"provision_pro_1m_eur_{s.lower()}"]
    head += ["epc_base_eur", "views_fuer_5k_gewinn_base", "views_fuer_10k_gewinn_base", "views_fuer_20k_gewinn_base",
             "views_fuer_5k_gewinn_strong", "views_fuer_10k_gewinn_strong", "views_fuer_20k_gewinn_strong",
             "realistische_views_monat12_base", "realistische_views_monat12_strong",
             "realistische_views_monat12_exceptional",
             "gewinn_monat_bei_realistischen_views_base_szenario", "gewinn_monat_bei_strong_views_strong_szenario",
             "gewinn_monat_bei_exceptional_views_exceptional_szenario",
             "contentkosten_pro_1m_views_bei_base_reichweite_eur", "annahmen"]
    w.writerow(head)
    for rank, x in enumerate(results, 1):
        c, r = x["c"], x["r"]
        row = [rank, c["id"], c["label"], c["market"], c["intent"]]
        for s in SCEN:
            row += [round(r[s]["clicks_monetizable_per_1m"]), round(r[s]["orders_per_1m"], 1), round(r[s]["revenue_per_1m_eur"])]
        rb, rs = r["Base"]["revenue_per_1m_eur"], r["Strong"]["revenue_per_1m_eur"]
        row += [round(r["Base"]["epc_eur"], 3), f0(views_needed(rb, 5000)), f0(views_needed(rb, 10000)), f0(views_needed(rb, 20000)),
                f0(views_needed(rs, 5000)), f0(views_needed(rs, 10000)), f0(views_needed(rs, 20000)),
                f0(x["reach_base"]), f0(x["reach_strong"]), f0(x["reach_exc"]),
                round(x["reach_base"] / 1e6 * rb - MONTHLY_COST_EUR), round(x["reach_strong"] / 1e6 * rs - MONTHLY_COST_EUR),
                round(x["reach_exc"] / 1e6 * r["Exceptional"]["revenue_per_1m_eur"] - MONTHLY_COST_EUR),
                round(MONTHLY_COST_EUR / (x["reach_base"] / 1e6)),
                "Views = organische Reel-Views; Klicks = monetarisierbare Affiliate-Klicks (nach Geo); Gewinn = Provision − 600 € Kosten/Monat; alles MODEL ASSUMPTION"]
        w.writerow(row)

with open(os.path.join(ROOT, "scorecard.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["rang", "id", "kombination", "markt", "score_0_100", "affiliate_economics_1_5 (20%)", "kaufintention (15%)", "organic_viral (15%)",
                "competition_opportunity (10%)", "ai_content_fit (10%)", "passivity (10%)", "market_flexibility (5%)", "product_variety (5%)",
                "compliance_trust (5%)", "cross_platform (5%)", "provision_pro_1m_base_eur"])
    for rank, x in enumerate(results, 1):
        v = x["vals"]
        w.writerow([rank, x["c"]["id"], x["c"]["label"], x["c"]["market"], round(x["score"], 1), round(v["econ"], 2), v["intent"], v["viral"],
                    v["comp"], v["ai"], v["passiv"], v["intl"], v["variety"], v["compliance"], v["cross"],
                    round(x["r"]["Base"]["revenue_per_1m_eur"])])

# JSON für die Markdown-Dokumente
dump = []
for rank, x in enumerate(results, 1):
    d = {"rank": rank, "id": x["c"]["id"], "label": x["c"]["label"], "market": x["c"]["market"], "score": round(x["score"], 1),
         "econ": round(x["econ"], 2), "reach_base": x["reach_base"], "reach_strong": x["reach_strong"],
         "reach_exc": x["reach_exc"], "synth": x["c"].get("synth", False),
         "vals": {k: (round(v, 2) if isinstance(v, float) else v) for k, v in x["vals"].items()},
         "profit_base_reach_base": round(x["reach_base"] / 1e6 * x["r"]["Base"]["revenue_per_1m_eur"] - MONTHLY_COST_EUR),
         "profit_strong_reach_strong": round(x["reach_strong"] / 1e6 * x["r"]["Strong"]["revenue_per_1m_eur"] - MONTHLY_COST_EUR),
         "profit_exc_reach_exc": round(x["reach_exc"] / 1e6 * x["r"]["Exceptional"]["revenue_per_1m_eur"] - MONTHLY_COST_EUR),
         "profit_strong_reach_exc": round(x["reach_exc"] / 1e6 * x["r"]["Strong"]["revenue_per_1m_eur"] - MONTHLY_COST_EUR),
         "struct": {k: round(v, 3) for k, v in x["r"]["_struct"].items()}}
    for s in SCEN:
        d[s] = {k: round(v, 4) for k, v in x["r"][s].items()}
        d[s]["views_5k"] = f0(views_needed(x["r"][s]["revenue_per_1m_eur"], 5000))
        d[s]["views_10k"] = f0(views_needed(x["r"][s]["revenue_per_1m_eur"], 10000))
        d[s]["views_20k"] = f0(views_needed(x["r"][s]["revenue_per_1m_eur"], 20000))
    dump.append(d)
with open(os.path.join(ROOT, "scripts", "model_output.json"), "w", encoding="utf-8") as fh:
    json.dump(dump, fh, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    print(f"{'Rg':>2} {'ID':4} {'Kombination':44} {'Score':>5} {'Cons':>6} {'Base':>6} {'Strong':>7} {'Exc':>7} {'V10k Base':>10} {'V10k Str':>9} {'€/Best':>7} {'P_b':>6} {'P_s':>6} {'P_e':>7}")
    for d in dump:
        print(f"{d['rank']:>2} {d['id']:4} {d['label'][:44]:44} {d['score']:>5} {d['Conservative']['revenue_per_1m_eur']:>6.0f} "
              f"{d['Base']['revenue_per_1m_eur']:>6.0f} {d['Strong']['revenue_per_1m_eur']:>7.0f} {d['Exceptional']['revenue_per_1m_eur']:>7.0f} "
              f"{d['Base']['views_10k']/1e6:>9.0f}M {d['Strong']['views_10k']/1e6:>8.1f}M {d['struct']['comm_per_order_eff_eur']:>7.2f} "
              f"{d['profit_base_reach_base']:>6} {d['profit_strong_reach_strong']:>6} {d['profit_exc_reach_exc']:>7}")
