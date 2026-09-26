"""Erzeugt 01_longlist_niches.csv, 02_market_comparison.csv, 03_affiliate_programs.csv, 05_competitor_database.csv.
Ausführen: python3 scripts/build_tables.py   (Quellen: quellen/raw_*.csv + Befunde aus quellen/*.md)"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(ROOT, "quellen")


def read(name):
    with open(os.path.join(Q, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# ---------------------------------------------------------------- 03 Affiliate-Programme
rows = []
for part, fname in [("A", "raw_programs_A.csv"), ("B", "raw_programs_B.csv"), ("C", "raw_programs_C.csv"), ("D", "raw_programs_D.csv")]:
    for i, r in enumerate(read(fname), 1):
        r = {"programm_id": f"P-{part}{i:03d}", **r, "quelle_datei": f"quellen/{fname}"}
        rows.append(r)
cols = list(rows[0].keys())
with open(os.path.join(ROOT, "03_affiliate_programs.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)
print("03:", len(rows), "Programme/Zeilen")

# ---------------------------------------------------------------- 05 Konkurrenz
rows = []
for part, fname in [("H", "raw_competitors_home.csv"), ("T", "raw_competitors_tech.csv")]:
    for i, r in enumerate(read(fname), 1):
        rows.append({"account_id": f"C-{part}{i:03d}", **r, "quelle_datei": f"quellen/{fname}"})
cols = list(rows[0].keys())
with open(os.path.join(ROOT, "05_competitor_database.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)
print("05:", len(rows), "Accounts")

# ---------------------------------------------------------------- 01 Longlist (55 Nischen)
# Spalten: Bereich | Nische | Beispielprodukte | AOV-Spanne € | Provision % | Provision/Bestellung € | Hauptprogramme (Beleg) |
# Kaufintention | Visual/Viral | AI-Fit | Passivität | Compliance | Cross-Platform | Produkte pro Content | Theme-Page+Affiliate belegt? |
# Saisonalität | Markt-Hypothese | Status | Begründung
L = [
 ("Wohnen", "Interior / Home Decor Finds", "Lampen, Vasen, Teppiche, Kissen, Wandbilder", "25–150", "DE/UK 5 % Amazon, 8 % Connox/Nordic Nest; US 3 % Amazon", "1–8", "Amazon (A), Connox 8 %/60 T, Nordic Nest ≥8 %, AllModern 8 %/45 T (A)", 4, 4, 3, 3, "MEDIUM", 4, "5–10", "ja (EN: trendyhomefinds1, divaa.finds, stylerior – I)", "gering", "DE (Content-Lücke 19,5×, 5 %)", "Shortlist K04/K05", "Beleg für Modell (EN), DE-Lücke"),
 ("Wohnen", "Möbel (Big Ticket: Sofa, Esstisch, Bett)", "Sofas, Tische, Betten", "300–3.000", "3–8 % (Amazon 3–5 %, AllModern 8 %, Williams-Sonoma 1 %)", "15–150", "AllModern 8 %, Wayfair, Castlery/Article (A); home24/IKEA ohne Programm (A)", 3, 4, 3, 3, "MEDIUM", 4, "3–6", "teilweise (nur als Teil von Interior-Pages)", "gering", "US", "in K04/K05/K29 enthalten", "niedrige CVR (DY Home 1,2 %), regionale Lieferung, WSI-Gruppe schließt anonyme Accounts aus"),
 ("Wohnen", "Luxury Homes / Immobilien-Showcase", "keine kaufbaren Produkte (Immobilien)", "n/a", "n/a", "0", "keine sinnvollen Programme", 1, 5, 4, 5, "LOW", 5, "0", "nein (Reichweite ohne Kauflink – I)", "gering", "EN", "verworfen", "keine Produkte → keine Affiliate-Ökonomie"),
 ("Wohnen", "AI-Architektur / AI-Dream-Interiors", "'ähnliche' Möbel/Deko", "40–400", "3–8 %", "1–20", "Amazon, AllModern (A)", 2, 5, 5, 5, "MEDIUM", 5, "2–5", "nein (Dreamy Interior 315k, Bau Rausch 620k ohne Kauflinks – I, J)", "keine", "EN", "Shortlist K29 (Referenz)", "maximaler AI-Fit, aber Unterhaltungs-Views (K: ~0–3 $/1 Mio.)"),
 ("Wohnen", "Smart Home", "Licht, Thermostate, Kameras, Saugroboter", "40–600", "3 % Amazon DE; Nanoleaf 10 %, Ring 10 %, Ecovacs 5 %", "2–30", "Nanoleaf, Ring (A), Govee (B), Ecovacs (C)", 3, 3, 3, 3, "LOW-MEDIUM", 3, "2–5", "nein (keine DE-Page belegt – I)", "gering", "DE", "Shortlist K16", "erklärungsbedürftig, weniger visuell"),
 ("Wohnen", "Home Organization", "Boxen, Regale, Organizer", "15–80", "3–5 % Amazon; Container Store 2 %; Yamazaki 7 %", "0,5–4", "Yamazaki 7 % (C), Amazon", 4, 4, 3, 4, "LOW-MEDIUM", 4, "4–8", "ja (thatorganizedhome – I)", "Jan. (Neujahr)", "EN/DE", "Longlist", "niedriger AOV; in K04/K06 abbildbar"),
 ("Wohnen", "Cleaning / Putzgadgets", "Reiniger, Saugroboter, Putztools", "15–600", "Dyson DE 7 % Content, SharkNinja 5 %, Amazon 3–5 %", "1–30", "Dyson DE, SharkNinja (C)", 4, 4, 2, 3, "MEDIUM", 4, "1–3", "teilweise (Reichweite ohne Links: CrazyClean01 – I)", "Frühjahr", "DE", "Longlist", "Reinigungsergebnis muss echt sein → AI-Fit gering; DE-Community ähnlich aktiv (F: 1,3×)"),
 ("Wohnen", "Schlaf / Matratzen / Bettwäsche", "Matratzen, Bettwäsche, Kissen", "60–1.500", "8–12 % bzw. 150 $ (DreamCloud, Nectar)", "30–150", "DreamCloud, Nectar, Simba (A)", 2, 1, 3, 4, "MEDIUM", 2, "1–3", "nein", "gering", "US/UK", "Shortlist K25", "nicht visuell, Probezeit-Retouren, Review-Seiten dominieren"),
 ("Wohnen", "Kinderzimmer / Kids Room Design", "Kinderbetten, Deko, Spielzeug", "30–500", "3–7 % (Pinolino 5 %, Amazon 3 %)", "1–20", "Pinolino, babymarkt (C)", 3, 4, 3, 3, "MEDIUM-HIGH", 4, "4–8", "unbekannt", "gering", "DE", "Longlist", "Kinder-/Eltern-Zielgruppe = höheres Trust-/Compliance-Risiko"),
 ("Wohnen", "Balkon / Small Space Living (inkl. Balkonkraftwerk)", "Balkonmöbel, Pflanzen, Balkonkraftwerke", "30–800", "Amazon 3–5 %, EcoFlow 5 % (7 T)", "1–40", "EcoFlow DE (D), Amazon", 3, 3, 4, 3, "LOW-MEDIUM", 4, "3–6", "unbekannt", "stark (Apr.–Aug.)", "DE", "Longlist", "DE-spezifisch interessant, aber Programme dünn und Cookie kurz (EcoFlow 7 T)"),
 ("Küche", "Küchengadgets", "Schneider, Spender, Helfer", "15–60", "DE/UK 5 %, US 4,5 % Amazon", "0,6–2,5", "Amazon Küche (A)", 5, 4, 3, 4, "MEDIUM", 4, "1–5", "ja (Justice Buys 2,1 Mio. YT/616k IG – I)", "Q4 Geschenke", "DE", "Shortlist K06/K07", "höchste Kaufintention; niedriger Warenkorb"),
 ("Küche", "Küchengeräte & Kochgeschirr (Premium)", "Küchenmaschine, Airfryer, Messer, Pfannen", "80–700", "5–8 % (Zwilling 6,4–8 %, KitchenAid 7 %, SharkNinja 5 %)", "5–40", "Zwilling, KitchenAid, SharkNinja, WMF (B)", 4, 4, 4, 4, "LOW-MEDIUM", 4, "3–6", "teilweise", "Q4 Geschenke", "DE/EN", "in K31/K32", "statische Geräte → Freisteller in AI-Szenen zuverlässig (H 10.2)"),
 ("Küche", "Kaffee / Espresso-Setups", "Siebträger, Mühlen, Waagen, Tamper", "50–900", "7 % De'Longhi DE, bis 8 % Breville, bis 15 % De'Longhi US (CLAIMED)", "5–60", "De'Longhi, Breville/Sage, Coffee Circle 60 T, Coffee Friend 10 % (B)", 4, 4, 3, 4, "LOW-MEDIUM", 4, "3–6", "nein (baristadaily: Reichweite ohne Links – I)", "Q4", "EN/DE", "Shortlist K08/K09 → K31/K32", "bestes AOV×Provision-Verhältnis in Teil B"),
 ("Küche", "Home Bar / Cocktails", "Shaker, Gläser, Barwagen", "20–300", "Amazon 3–5 %; Alkohol 0 %", "1–10", "Amazon (Alkohol ausgeschlossen – A)", 3, 4, 4, 4, "MEDIUM", 4, "3–6", "unbekannt", "Q4", "EN", "verworfen", "Alkohol-Werbung reguliert, Alkohol 0 % bei Amazon"),
 ("Küche", "Food / Rezepte (ohne Produktfokus)", "Zutaten, Lebensmittel", "20–60", "Amazon Lebensmittel 1 %", "0,2–0,6", "Amazon Fresh 1 % (A)", 2, 5, 3, 4, "LOW", 5, "0–2", "nein", "gering", "EN", "verworfen", "Viral, aber kaum Provision"),
 ("Outdoor", "BBQ / Grill / Pizzaöfen / Outdoor Kitchen", "Pizzaöfen, Kamados, Pelletgrills, Plancha", "60–5.000", "5–10 % (Ooni 10 %, SANTOS 10/7 %, BBQGuys 6 %, Solo Stove 5–10 %)", "5–150", "Ooni, Gozney, SANTOS, BBQGuys, Blackstone (C)", 4, 5, 3, 3, "LOW-MEDIUM", 4, "3–6", "unbekannt", "stark (März–Aug.)", "US/DE", "Shortlist K12/K13", "hohe Provision pro Bestellung, aber Saisonalität"),
 ("Outdoor", "Backyard Wellness: Sauna / Cold Plunge / Hot Tub", "Fass-Saunen, Infrarot, Plunges, Whirlpools", "300–25.000", "5–10 % (Sun Home 5 %, RecoSauna 7 %, Sweat Kingdom 5–10 %; DE Sauna24 8 %, AIDA 10 %)", "20–2.000", "Sun Home, RecoSauna, Sweat Kingdom (US); Mein-Saunashop Ø851 €, Sauna24 (DE) (C)", 3, 4, 5, 4, "LOW-MEDIUM", 4, "2–4", "unbekannt", "gegenläufig (Sauna Winter/Pool Sommer)", "US", "Shortlist K10/K11", "nicht offensichtliche High-Ticket-Nische; CVR sehr niedrig"),
 ("Outdoor", "Pools", "Aufstellpools, Poolroboter, Wärmepumpen", "100–3.000", "3–7 % (primepool 7 % Ø628 €, poolroboter 3–5 % Ø755 €)", "10–50", "primepool, mein-poolroboter, poolmondo (C)", 3, 4, 4, 2, "LOW-MEDIUM", 4, "2–4", "unbekannt", "sehr stark (Mai–Aug.)", "DE", "in K11", "Saison zu kurz für Stand-alone"),
 ("Outdoor", "Outdoor Living / Terrasse / Gartenmöbel", "Loungemöbel, Sonnenschirme, Beleuchtung", "100–8.000", "5–8 % (Outer 5–8 %/90 T; OTTO Living 12 % Content)", "10–400", "Outer (C), OTTO (D), Wayfair", 3, 4, 4, 2, "MEDIUM", 5, "4–8", "unbekannt", "stark", "US/DE", "Longlist", "in K12/K13 als Cross-Sell; Saisonalität"),
 ("Outdoor", "Garten / Gardening", "Pflanzen, Hochbeete, Werkzeug, Mähroboter", "20–1.500", "5–10 % (STIHL 8 %, Baldur 8 %, hagebau 10 % Content)", "2–60", "STIHL, Baldur, hagebau, Plantura (C)", 3, 3, 4, 2, "MEDIUM", 5, "3–6", "nein (EN-Theme-Pages nicht belegt – I)", "sehr stark", "DE", "Shortlist K26", "Plantura-Stornoquote 41 %; DE-Community ähnlich aktiv (F)"),
 ("Outdoor", "Camping / Vanlife / Overlanding", "Zelte, Dachzelte, Kocher, Kühlboxen", "50–3.000", "4–8 % (Bergfreunde 7 %, Backcountry 4–12 %)", "3–60", "Bergfreunde, Campz, Backcountry (D)", 3, 4, 4, 3, "LOW-MEDIUM", 4, "4–8", "nein (Reichweite ohne Links – J)", "stark (Frühjahr/Sommer)", "DE/US", "Shortlist K22", "Bergfreunde Bestätigungsrate nur 65 %"),
 ("Outdoor", "Power Stations / Off-Grid", "EcoFlow, Jackery, Bluetti, Solarpanels", "300–2.000", "5–10 % (Jackery 5–8 %/30 T, EcoFlow 5 %/7 T, Bluetti bis 10 %)", "15–100", "EcoFlow, Jackery, Bluetti (D)", 3, 3, 4, 3, "LOW-MEDIUM", 3, "1–3", "unbekannt", "mittel", "DE/US", "in K22", "hoher AOV, aber kurze Cookies und wenig virales Potenzial"),
 ("Outdoor", "Hiking / Outdoor-Bekleidung", "Jacken, Schuhe, Rucksäcke", "80–400", "5–8 % (Bergfreunde 7 %, Arc'teryx 7 %)", "4–25", "Bergfreunde, Arc'teryx, REI 5 %/15 T (D)", 3, 4, 3, 2, "MEDIUM", 4, "3–5", "nein", "saisonal", "DE", "Longlist", "Bekleidungsretouren (Bergfreunde 65 % Bestätigung)"),
 ("Tech", "Gaming Setups", "Monitore, Tastaturen, LED, Stühle, Tische", "30–1.500", "1–5 % (Amazon PC 2,5 %, Spiele 1 %; Logitech 4–10 %)", "1–15", "Logitech, Secretlab, Corsair, Amazon (B)", 3, 5, 5, 2, "LOW-MEDIUM", 4, "6–10", "ja (@killergamingsetups 213k u. a. – J)", "Q4", "EN", "Shortlist K03", "junges, globales Publikum; Billigprodukte (J)"),
 ("Tech", "Desk Setups / Home Office / Productivity", "Monitore, Lampen, Schreibtische, Stühle, Zubehör", "40–2.300", "3–8 % (FlexiSpot 4–8 %, noblechairs 5 %, Herman Miller 4 % US-only)", "2–90", "FlexiSpot, noblechairs, Logitech, Grovemade, Amazon (B)", 4, 4, 4, 3, "LOW-MEDIUM", 4, "6–10", "ja (11 von 23 Setup-Pages monetarisieren, 7 mit Storefront – J)", "Q1 (Neujahr), Q4", "EN/DE", "Shortlist K01/K02", "Modell bewiesen; EN reif (Follower −8 bis −16 % seit 2023 – J)"),
 ("Tech", "PC-Zubehör / Peripherie", "Mäuse, Keyboards, Headsets", "30–200", "1–5 % (Händler 1–3 %, Logitech 4–10 %)", "1–8", "Logitech, Currys 3 % Creator (B)", 4, 4, 3, 2, "LOW-MEDIUM", 3, "1–3", "teilweise", "Q4", "EN", "in K01/K03", "niedrige Provision"),
 ("Tech", "Tech Gadgets / Amazon Finds (allgemein)", "Gadgets unter 50 €", "15–80", "3–4 % Amazon; Ugreen 8 %, Casetify 10 %", "0,5–3", "Amazon, Ugreen, Casetify, Nomad (B)", 5, 5, 2, 2, "MEDIUM-HIGH", 4, "1–5", "ja (Justice Buys, JayFindsThings 7,8 Mio. – F, I, J)", "Q4", "DE (Lücke 25,6×)", "Shortlist K14/K15", "hyper-gesättigt (EN); Funktionsdemos per AI = Irreführungsrisiko"),
 ("Tech", "Smartphone-Zubehör", "Hüllen, Ladegeräte, MagSafe", "20–80", "8–10 % (Casetify, Nomad), Amazon 2,5–4 %", "1–5", "Casetify, Nomad, Ugreen, Anker (B)", 4, 3, 3, 2, "LOW-MEDIUM", 3, "2–4", "teilweise", "Sept. (iPhone-Launch)", "EN", "Longlist", "kurze Produktzyklen"),
 ("Tech", "Consumer Electronics (TV, Konsolen, Laptops)", "TVs, Laptops, Konsolen", "300–2.000", "1–3 % (Amazon TV 2 %, Konsolen 1 %)", "5–30", "Best Buy, Currys 3 %, nbb 2 % (B)", 3, 3, 2, 2, "MEDIUM", 3, "1–3", "teilweise (Deal-Pages)", "Q4", "EN", "verworfen", "Provision zu niedrig, Tests/Reviews nötig"),
 ("Tech", "Fotografie / Kameras", "Kameras, Objektive, Gimbals", "300–3.000", "2–5 % (B&H 2 %, Calumet 3–5 %, Sony 3 %)", "10–60", "B&H, Adorama, Calumet (B)", 3, 3, 1, 3, "MEDIUM-HIGH", 3, "1–4", "nein (J: nicht belegt)", "Q4", "EN", "verworfen", "Beweisfotos müssen echt sein – AI-Fit sehr gering"),
 ("Tech", "Audio / Hi-Fi / Kopfhörer", "Lautsprecher, Kopfhörer, Plattenspieler", "80–2.000", "2–8 % (Teufel bis 8 % Multi-Touch, Sennheiser 3,5–7 %)", "3–60", "Teufel, Sennheiser, B&O (B)", 3, 3, 2, 3, "MEDIUM", 3, "2–4", "nein (J: keine Accounts gefunden)", "Q4", "DE", "Longlist", "Klang nicht per AI darstellbar"),
 ("Tech", "Music Equipment / Home Studio", "Synths, Mikrofone, Interfaces", "100–2.000", "3–6 % (Thomann 4,5 % ab 5.000 Followern)", "5–60", "Thomann, Sweetwater (B)", 3, 3, 2, 3, "MEDIUM", 3, "3–6", "unbekannt", "Q4", "DE", "Longlist", "Thomann erst ab 5.000 Followern; Sound nicht per AI"),
 ("Tech", "3D-Druck / Maker", "Drucker, Filament, Zubehör", "30–1.500", "4–10 % (Bambu Lab 10 %, Creality 4–8 %, Anycubic 5 %/60 T)", "3–80", "Bambu Lab, Creality, Anycubic (D)", 4, 4, 2, 3, "MEDIUM", 3, "1–4", "ja (The 3D Wizard – J)", "Q4", "EN", "Shortlist K28", "Community lehnt AI-'Prints' ab"),
 ("Tech", "EDC (Everyday Carry)", "Messer, Taschenlampen, Wallets", "20–300", "4–10 % (Bellroy 7 %, Orbitkey 7–8 %)", "1–15", "Bellroy, Orbitkey (B, D)", 4, 3, 4, 4, "MEDIUM (Messer)", 3, "4–8", "ja (J: mittel belegt)", "gering", "EN", "Longlist", "kleine Nische, Messer rechtlich heikel (DE)"),
 ("Reisen", "Travel Gear / Packing", "Koffer, Rucksäcke, Packwürfel, eSIM", "30–600", "4–15 % (NOMATIC 15 %, Tortuga 10 %, Travelpro 8–10 %, Saily 15 %)", "2–40", "Tortuga, Travelpro, Bellroy, NOMATIC, Saily (D)", 3, 4, 4, 4, "LOW-MEDIUM", 5, "4–8", "unbekannt", "Frühjahr/Sommer", "EN/US", "Shortlist K17", "Pinterest-stark; US-Programme dominieren"),
 ("Reisen", "Travel Destinations / Dream Trips", "Touren, Hotels, Aktivitäten", "100–1.000", "Booking-Anteil, GetYourGuide 8 %, Viator 8 %", "5–40", "GetYourGuide, Viator, Booking (D)", 2, 5, 3, 3, "MEDIUM-HIGH", 5, "1–3", "teilweise", "saisonal", "EN", "Shortlist K30 (Referenz)", "Provision erst nach Reise, Stornos, AI-Orte irreführend"),
 ("Sport", "Home Gym / Fitness Equipment", "Racks, Hanteln, Laufbänder", "50–3.000", "3–5 % (REP 5 % US-only, Bowflex 3 %; Rogue ohne Programm)", "2–60", "REP, Bowflex, Hyperice (D)", 3, 4, 3, 4, "MEDIUM", 3, "3–6", "unbekannt", "Jan.", "US", "Shortlist K27", "Fitness-Claims; US-only Programme"),
 ("Sport", "Running", "Laufschuhe, Uhren, Bekleidung", "80–500", "5–18 % (On 18 %?, Nike bis 15 %/7 T, adidas DE 2 %)", "4–30", "On, Nike, Runnerinn (D)", 3, 3, 2, 2, "MEDIUM", 3, "2–4", "nein", "Frühjahr", "UK/US", "Longlist", "Schuhretouren, Personen-Nische"),
 ("Sport", "Cycling / E-Bikes", "E-Bikes, Zubehör, Trainer", "50–5.000", "2–5 % (Canyon 2 %, ROSE 5 %, Aventon 4 %)", "5–150", "ROSE, Canyon, Aventon (D)", 3, 3, 3, 3, "MEDIUM", 3, "1–3", "nein (J)", "Frühjahr", "DE", "Longlist", "kein E-Bike-Programm ≥5–10 % belegt (D)"),
 ("Sport", "Golf (inkl. Simulatoren)", "Launch Monitors, Simulatoren, Schläger", "50–15.000", "3–15 % (SkyTrak 10–15 %, 2nd Swing 5–15 %)", "3–300", "SkyTrak, 2nd Swing, Golf House 6 % (D)", 3, 3, 3, 4, "LOW-MEDIUM", 3, "2–4", "nein (J: nicht belegt)", "Winter (Indoor)", "US", "Shortlist K21", "kleiner Markt, US-only High-Ticket"),
 ("Haustiere", "Hunde-Produkte", "Betten, Leinen, Spielzeug, Futter-Abos", "20–150", "3–20 % (Fressnapf 8 % Neukunden, LuckyPets 20 % Neukunden, Farmer's Dog 50 $ CPA)", "1–50", "Fressnapf, ZooRoyal, Farmer's Dog, Butternut Box (C)", 4, 5, 2, 4, "MEDIUM", 4, "2–5", "ja (round.boys, dogsofinstagram – I)", "gering", "DE/EN", "Shortlist K23", "AI-Hunde, die Produkte nutzen = Irreführung; DE-Community aktiv (F)"),
 ("Haustiere", "Katzen-Produkte", "Kratzbäume, Katzenklos, Brunnen", "20–700", "3–12 % (Litter-Robot 8 %/90 T, Tuft+Paw 12 %)", "1–60", "Whisker, Tuft + Paw, Petlibro 15 % Creator (C)", 4, 5, 2, 4, "MEDIUM", 4, "2–5", "teilweise", "gering", "US", "Longlist", "wie Hund; Litter-Robot als High-Ticket-Anker"),
 ("Haustiere", "Aquaristik / Aquascaping", "Becken, Licht, CO2, Pflanzen", "50–1.500", "3–5 % (Amazon 3 %, zooplus 3 % erste 3 Bestellungen)", "2–40", "Amazon, zooplus (C)", 3, 4, 3, 4, "MEDIUM", 4, "3–6", "unbekannt", "gering", "DE/EN", "Longlist", "Lebewesen per AI = Irreführungsrisiko; Programme schwach"),
 ("Beauty", "Skincare", "Seren, Cremes, Sonnenschutz", "20–80", "4–20 % (The Ordinary 13–20 %, Sephora DE 12 %, Lookfantastic 12–15 %)", "2–8", "The Ordinary, Sephora, Lookfantastic (D)", 4, 4, 2, 3, "HIGH", 4, "3–6", "nein (faceless Beauty ohne Belege)", "gering", "DE/UK", "Shortlist K18", "Wirkversprechen/HCVO-nahe Claims; faceless ohne Vertrauen"),
 ("Beauty", "Beauty Devices (LED-Masken, Airwrap)", "LED-Masken, Styler", "150–600", "2–20 % (medicube 20 %, Foreo 6 %/60 T, CurrentBody DE 2–4 %)", "10–60", "medicube, Foreo (D)", 4, 4, 2, 3, "HIGH", 3, "1–2", "nein", "Q4", "US", "Shortlist K19", "Wirkung nicht per AI zeigbar; HIGH Compliance"),
 ("Beauty", "Haircare", "Stylingtools, Pflege", "20–500", "1–5 % (ghd 1–5 %, Dyson DE 5 %)", "1–25", "ghd, Dyson (D)", 3, 4, 2, 3, "MEDIUM-HIGH", 4, "1–3", "nein", "gering", "DE", "Longlist", "Ergebnisse müssen echt sein"),
 ("Mode", "Fashion (faceless 'Shop the Look')", "Outfits, Basics", "40–300", "6–15 % (Breuninger 12 %, Lounge 12 %, Amazon Fashion 6 %)", "3–15", "Breuninger, Mango, OTTO via Stylink (D)", 4, 4, 2, 1, "MEDIUM-HIGH", 5, "4–6", "ja (Herrenmode-Theme-Page D01 – K)", "saisonal", "DE/UK", "Shortlist K20", "DE-Retouren 45–55 %; Links sterben mit der Kollektion"),
 ("Mode", "Sneakers", "Sneaker-Releases", "100–400", "3–15 % (Nike bis 15 %/7 T, StockX/GOAT Impact)", "5–30", "Nike, StockX (D)", 3, 4, 2, 1, "MEDIUM", 4, "1–3", "teilweise (Grailify, Sneakerjagers – J)", "Drops", "EN/DE", "Longlist", "Drop-getrieben, hoher Pflegeaufwand"),
 ("Mode", "Schmuck", "Ketten, Ringe", "30–500", "3–9 % (Thomas Sabo 8 %, CHRIST 8 %, Blue Nile 3,5 % nur mit Domain)", "2–30", "Thomas Sabo, CHRIST (D)", 3, 4, 2, 3, "MEDIUM-HIGH", 5, "2–4", "nein (J: keine Accounts)", "Q4", "DE", "Longlist", "Produktdetails per AI nicht exakt; Luxus-CVR 0,6–0,7 %"),
 ("Mode", "Uhren", "Luxus- und Designuhren", "100–20.000", "2,5–9 % (Chrono24 2,5 %, Uhrcenter 9 %, eBay 4 %/24 h)", "5–500", "Chrono24, Uhrcenter, Jomashop (D)", 3, 4, 2, 4, "MEDIUM-HIGH", 3, "1–2", "nein (J: nicht belegt)", "Q4", "EN", "Longlist", "Uhren-Details/Logos per AI heikel (Marken, Fälschungsnähe)"),
 ("Mode", "Taschen / Luxury Resale", "Designertaschen", "300–5.000", "4–7 % (Rebag 7 %, Mytheresa 4,8–9,6 %)", "15–200", "Rebag, Mytheresa (D)", 3, 4, 2, 3, "HIGH", 4, "1–2", "nein", "Q4", "EN", "verworfen", "Fälschungs-/Markenrisiko bei AI-Darstellung"),
 ("Lifestyle", "Luxury Lifestyle (Autos, Yachten)", "nicht kaufbar", "n/a", "n/a", "0", "keine", 1, 5, 4, 5, "LOW", 5, "0", "nein", "keine", "EN", "verworfen", "keine Affiliate-Produkte"),
 ("Auto", "Autozubehör / Tesla-Zubehör", "Matten, Halterungen, Dashcams", "20–300", "DE 5 % Amazon; Nextbase 6–8 %, Autodoc 8 %", "1–15", "Amazon Auto, Nextbase, Autodoc (C)", 4, 3, 2, 3, "MEDIUM", 3, "2–5", "ja (TaylorOnWheels – J)", "gering", "DE", "Shortlist K24", "Einbau-/Funktionsdemos müssen echt sein"),
 ("Auto", "Car Detailing", "Pflegemittel, Poliermaschinen", "20–300", "5–10 % (Chemical Guys bis 10 %)", "1–15", "Chemical Guys, Amazon (C)", 4, 4, 1, 3, "MEDIUM-HIGH", 3, "2–4", "nein (Reichweite ohne Links – J)", "Frühjahr", "US", "in K24", "Vorher/Nachher per AI = Täuschung"),
 ("DIY", "Tools / DIY / Werkstatt", "Akkuwerkzeug, Werkbänke", "30–1.200", "DE 5 % Amazon, hagebau 10 %, toom 8 %; US Home Depot 1 %/1 Tag", "2–60", "hagebau, toom, OBI, myToolStore Ø1.143 € (C)", 4, 3, 2, 3, "MEDIUM", 3, "2–5", "ja (Malerart DE 464k YT – J)", "Frühjahr", "DE", "Longlist", "Nutzung muss echt sein; DE-Programme gut (5 %/10 %)"),
 ("Baby", "Baby / Parenting Products", "Kinderwagen, Babyphones, Autositze", "30–1.200", "3–10 % (CYBEX 6 %, Momcozy 10 %, Lovevery UK 10 %)", "2–60", "CYBEX, Momcozy, Babylist (C)", 4, 3, 2, 3, "HIGH", 3, "2–4", "nein (EN nicht belegt – I)", "gering", "US/DE", "verworfen", "Sicherheitsprodukte + Eltern-Trust → HIGH"),
 ("Hobby", "LEGO / Collectibles", "Sets, Figuren, Karten", "20–800", "3–4 % (LEGO EU 3,57 %, eBay 3 %/24 h)", "1–20", "LEGO (Daisycon), eBay Partner Network (D)", 3, 4, 2, 3, "MEDIUM", 3, "1–3", "ja (DE: Promobricks – J)", "Q4", "DE", "Longlist", "Marken-/IP-Risiko bei AI-Darstellung; niedrige Provision"),
 ("Wellness", "Supplements / Nahrungsergänzung", "Protein, Vitamine", "20–80", "Amazon Health 1 %; Brands 10–30 % (TikTok Shop)", "1–15", "(bewusst nicht recherchiert)", 4, 3, 2, 4, "HIGH", 3, "1–3", "teilweise (KI-Supplement-Video TikTok Shop – K, CS5)", "Jan.", "US", "verworfen", "HCVO/FTC-Claims-Risiko; Auftrag: nur wenn regulatorisch sinnvoll"),
]
cols = ["nr", "bereich", "nische", "beispielprodukte", "typischer_aov_eur", "typische_provision", "provision_pro_bestellung_eur",
        "hauptprogramme_beleg", "kaufintention_1_5", "visual_viral_1_5", "ai_fit_1_5", "passivitaet_1_5", "compliance_trust_risiko",
        "cross_platform_1_5", "produkte_pro_content", "theme_page_affiliate_belegt", "saisonalitaet", "markt_hypothese",
        "status", "hauptgrund", "datenqualitaet"]
with open(os.path.join(ROOT, "01_longlist_niches.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(cols)
    for i, r in enumerate(L, 1):
        w.writerow([i, *r, "Provisionen/AOV: VERIFIED/THIRD-PARTY laut 03_affiliate_programs.csv; Rubriken 1–5: MODEL ASSUMPTION mit Begründung; Belege: quellen/*.md (Buchstabe in Klammern)"])
print("01:", len(L), "Nischen")

# ---------------------------------------------------------------- 02 Marktvergleich
M = {  # Markt-Grunddaten (quellen/F_marktvergleich_de_us_uk_intl.md)
    "DE/DACH": dict(ig="38,5 Mio. (DE 31,3 · AT 3,35 · CH 3,8) – VERIFIED DataReportal 2026", ecom="≈137 Mrd. USD (DE 92,3 Mrd. € netto) – VERIFIED HDE", kaufkraft=4,
                    amazon="Amazon.de 63,3 % des DE-Onlinehandels (VERIFIED HDE/IFH); Wohnen/Möbel/Küche/Baumarkt 5 %, Elektronik/Garten/Haustier 3 %",
                    geo="≈80 % DACH-Publikum bei deutschsprachigen Kanälen (NexLev, THIRD-PARTY)", cpm="Meta-CPM ≈14,8 € (THIRD-PARTY)"),
    "US": dict(ig="182 Mio. – VERIFIED", ecom="1.233,7 Mrd. USD – VERIFIED US Census", kaufkraft=5,
               amazon="Amazon ≈40,5 % (THIRD-PARTY); Home/Furniture/Garden/Pets 3 %, Kitchen 4,5 %, Electronics 4 %",
               geo="EN-Content: nur ≈42 % US-Publikum (NexLev-Beispiel)", cpm="Meta-CPM 23,4 USD"),
    "UK": dict(ig="35,5 Mio. – VERIFIED", ecom="≈132,8 Mrd. £ (≈175 Mrd. USD), Onlineanteil 27,5 % – VERIFIED ONS", kaufkraft=3,
               amazon="Amazon ≈25 % (schwache Drittquelle); Home/Kitchen/DIY 5 %",
               geo="teilt EN-Content-Pool mit US; UK-Anteil EN-Publikum ≈14 %", cpm="Meta-CPM 17,4"),
    "International-EN": dict(ig="≈259 Mio. EN-Kern (+481 Mio. Indien, kaum monetarisierbar)", ecom="Summe EN-Kern", kaufkraft=3,
                             amazon="Mix: US 3–4,5 %, UK/CA/AU über OneLink/Geniuslink; Indien nicht routbar",
                             geo="≈24 % Indien im EN-Finds-Beispiel unmonetarisierbar", cpm="Mix; Indien 1,35 USD"),
}
N = [  # Nische: {Markt: (konkurrenz 1–5 [5 = wenig], grosse_theme_pages, ai_pages, programme, aov, conversion_hinweis, versand, reichweite_monat12, gesamt 1–5, begruendung)}
 ("Interior / Home Decor Finds", {
   "DE/DACH": (4, "keine faceless DE-Home-Finds-Page >100k gefunden; solebich/inspowelt__ (Personen/Community) – I", "keine belegt", "Amazon.de 5 %, Connox 8 %/60 T, Nordic Nest ≥8 %; home24/Maisons du Monde/IKEA ohne Programm", "25–150 €", "Amazon.de-CVR 5,94 % (Geniuslink 2022)", "gut (DE+AT)", "2 Mio. / 7 Mio.", 4, "Content-Lücke 19,5× + 5 % Provision"),
   "US": (1, "≥12 EN Home-Theme-Pages >100k (trendyhomefinds1 1,3 Mio., divaa.finds 774k) – I", "wenige; AI-Interior ohne Links", "Amazon 3 %, AllModern 8 %/45 T, WSI 1 %/1 Tag", "30–200 $", "Amazon.com 11,1 %", "gut", "5 Mio. / 20 Mio.", 3, "größter Markt, stärkste Konkurrenz"),
   "UK": (2, "teilt EN-Pool", "–", "Amazon.co.uk 5 %, John Lewis/Dunelm (Raten nicht öffentlich)", "25–150 £", "UNKNOWN", "gut", "Teil des EN-Pools", 3, "5 % wie DE, aber EN-Konkurrenz"),
   "International-EN": (1, "wie US", "–", "Geo-Routing nötig", "Mix", "verwässert (Indien)", "mittel", "5 Mio. / 20 Mio.", 2, "Streuverlust")}),
 ("Küche / Küchengadgets / Kitchen & Coffee Setups", {
   "DE/DACH": (4, "keine DE-Küchen-Theme-Page gefunden – I; DE-Tags nicht messbar – F", "keine", "Amazon.de Küche 5 %, Zwilling 6,4–8 %, KitchenAid 7 %, De'Longhi 7 %, SharkNinja 5 %", "35–300 €", "Amazon.de 5,94 %; Küchengeräte IRP 2,98 % (UK)", "gut", "2 Mio. / 7 Mio.", 4, "hohe Intention + 5 % + Lücke (ungesichert)"),
   "US": (1, "Justice Buys 616k IG / 2,1 Mio. YT – I", "US Shop (AI-Produktvideos, 642 Mio. YT-Views) – H", "Amazon Kitchen 4,5 %, Breville bis 8 %, KitchenAid 5 %", "35–700 $", "Amazon.com 11,1 %", "gut", "5 Mio. / 20 Mio.", 4, "höchster Reichweiten-Deckel; Konkurrenz hoch"),
   "UK": (2, "teilt EN-Pool", "–", "Amazon.co.uk 5 %, Sage 8 %, Lakeland 2,5 %/15 T", "40–300 £", "UNKNOWN", "gut", "Teil EN-Pool", 3, "Sage 8 % stark"),
   "International-EN": (1, "wie US", "–", "Mix", "Mix", "verwässert", "mittel", "5 Mio. / 20 Mio.", 3, "Geo-Routing Pflicht")}),
 ("Kaffee / Espresso-Setups", {
   "DE/DACH": (3, "keine Kaffee-Affiliate-Page belegt; DE-Kaffee-Community pro Nutzer ähnlich aktiv (1,6×) – F", "keine", "De'Longhi DE 7 %, Coffee Circle 60 T, Coffee Friend 10 %, Kaffee24 5–6 %", "70–700 €", "UNKNOWN (Elektronik-Proxy)", "gut", "1 Mio. / 4 Mio.", 3, "gute Programme, keine Lücke"),
   "US": (2, "baristadaily u. a. ohne Kauflinks – I", "keine", "Breville bis 8 %, De'Longhi US bis 15 % (CLAIMED)", "70–900 $", "UNKNOWN", "gut", "3 Mio. / 10 Mio.", 4, "hohe Provision pro Sale"),
   "UK": (2, "–", "–", "Sage 8 %, De'Longhi UK bis 10 %", "150–300 £", "UNKNOWN", "gut", "Teil EN-Pool", 3, "–"),
   "International-EN": (2, "–", "–", "Mix", "Mix", "verwässert", "mittel", "3 Mio. / 10 Mio.", 3, "–")}),
 ("BBQ / Pizzaöfen / Outdoor Kitchen", {
   "DE/DACH": (3, "DE-Grill-Community stark personenzentriert; faceless nicht belegt", "keine", "SANTOS 10 %/7 %, Ooni 10 %, Kuppelofen Ø766 €/90 T, Gozney 5 %", "60–800 €", "UNKNOWN (Home-Proxy)", "gut, Speditionsware", "1 Mio. / 4 Mio.", 4, "starke Programme, Saison März–Aug."),
   "US": (2, "nicht gezielt belegt", "keine", "BBQGuys 6 %, Ooni 10 %, Solo Stove 5–10 %, Blackstone/BGE 5 %", "60–5.000 $", "UNKNOWN", "gut", "3 Mio. / 10 Mio.", 4, "Outdoor-Küchen = High-Ticket"),
   "UK": (3, "–", "–", "Ooni 10 %, Gozney 5 %; Weber UK inaktiv", "100–600 £", "UNKNOWN", "gut", "Teil EN-Pool", 3, "Programmangebot dünn"),
   "International-EN": (2, "–", "–", "Ooni global", "Mix", "verwässert", "mittel", "3 Mio. / 10 Mio.", 3, "–")}),
 ("Backyard Wellness (Sauna, Plunge, Whirlpool, Pool)", {
   "DE/DACH": (3, "nicht gezielt belegt", "keine", "Mein-Saunashop Ø851 €, Sauna24 8 %/90 T, AIDA 10 %, primepool 7 % Ø628 €", "300–10.000 €", "sehr niedrig (High-Ticket)", "Speditionsware, DE/AT", "0,5 Mio. / 2 Mio.", 3, "gemessene Warenkörbe hoch, Reichweite klein"),
   "US": (3, "nicht gezielt belegt", "keine", "Sun Home 5 % (Social erlaubt), RecoSauna 7 %, Sweat Kingdom 5–10 %, Renu 7 %", "1.000–45.000 $", "sehr niedrig", "Lower 48 only (Peak)", "1,5 Mio. / 5 Mio.", 3, "Provision pro Sale 200–2.000 $, CVR unbekannt"),
   "UK": (3, "–", "–", "Bast Sauna UK 6 %, Wave Spas", "UNKNOWN", "UNKNOWN", "–", "Teil EN-Pool", 2, "dünn"),
   "International-EN": (3, "–", "–", "US-Programme nur für US-Käufer", "–", "–", "schlecht (Versand)", "1,5 Mio. / 5 Mio.", 2, "Versand begrenzt")}),
 ("Desk Setups / Home Office", {
   "DE/DACH": (4, "keine DE faceless Setup-Page relevanter Größe; @cleandesksetup (48k, amazon.de-Links) – J", "keine", "Amazon.de 3–5 %, noblechairs 5 %, FlexiSpot DE 4 %, nbb 2 %", "40–600 €", "Amazon.de 5,94 %", "gut", "1 Mio. / 4 Mio.", 3, "Lücke, aber DE-Gamer nutzen EN-Content (F)"),
   "US": (2, "11 von 23 Setup-Pages monetarisieren (thedreamsetup 374k, setuputic 241k) – J", "@topdailysetups (67k, 3D + Storefront) – J", "FlexiSpot, Logitech 4–10 %, Herman Miller 4 % (US-only), Amazon 2,5–4 %", "60–2.300 $", "Amazon.com 11,1 %", "gut", "3 Mio. / 10 Mio.", 3, "Modell bewiesen; Markt reif (Follower −8 bis −16 %)"),
   "UK": (2, "teilt EN-Pool", "–", "FlexiSpot UK 4–8 % AOV 292 £, Currys 3 % Creator", "–", "–", "gut", "Teil EN-Pool", 3, "–"),
   "International-EN": (2, "wie US", "–", "Mix", "Mix", "verwässert", "mittel", "3 Mio. / 10 Mio.", 3, "–")}),
 ("Gaming Setups", {
   "DE/DACH": (4, "#zockerzimmer 3,6k Posts – DE-Ökosystem fehlt (F)", "–", "Amazon.de Spiele 1 %, Elektronik 3 %", "30–1.500 €", "–", "gut", "1 Mio. / 4 Mio.", 2, "Gamer konsumieren EN-Content"),
   "US": (2, "@killergamingsetups 213k u. a. – J", "–", "Amazon PC 2,5 %, Spiele 1 %", "30–1.500 $", "Billigprodukt-Tendenz (J)", "gut", "5 Mio. / 20 Mio.", 2, "Provision zu niedrig"),
   "UK": (2, "–", "–", "Scan 1 %, Overclockers bis 2 %, Currys 3 %", "–", "–", "gut", "Teil EN-Pool", 2, "–"),
   "International-EN": (2, "–", "–", "–", "–", "stark verwässert", "mittel", "5 Mio. / 20 Mio.", 3, "global viral, aber junge/globale Zuschauer")}),
 ("Tech Gadgets / Amazon Finds", {
   "DE/DACH": (4, "kein dedizierter DE-Finds-Kanal in Top-20 (F); mydealz 546k = Deals, anderes Format (I)", "–", "Amazon.de 2,5–3 %", "15–80 €", "Amazon.de 5,94 %", "gut", "2 Mio. / 7 Mio.", 3, "Lücke 25,6×, aber 3 % und niedriger AOV"),
   "US": (1, "Justice Buys, JayFindsThings 7,8 Mio., Money Saving Man 3,9 Mio. – F", "US Shop (AI) – H", "Amazon 4 %", "15–80 $", "Amazon.com 11,1 %", "gut", "5 Mio. / 20 Mio.", 2, "hyper-gesättigt"),
   "UK": (1, "–", "–", "Amazon.co.uk 2,5–5 %", "–", "–", "gut", "Teil EN-Pool", 2, "–"),
   "International-EN": (1, "–", "–", "–", "–", "stark verwässert (24 % Indien)", "mittel", "5 Mio. / 20 Mio.", 2, "–")}),
 ("Hunde-/Haustierprodukte", {
   "DE/DACH": (2, "#hundeliebe 13,7 Mio.; DE-Community pro Nutzer ähnlich aktiv (2,0×) – F", "–", "Fressnapf 8 % Neukunden/60 T, ZooRoyal 11 %, zooplus 3 % (erste 3 Bestellungen)", "35–70 €", "DY Pet 4,71 %", "gut", "2 Mio. / 7 Mio.", 3, "kein Konkurrenzvorteil"),
   "US": (1, "round.boys, dogsofinstagram – I", "–", "Farmer's Dog 50 $ CPA, Litter-Robot 8 %/90 T, Chewy 1 %", "30–700 $", "DY Pet 4,71 %", "gut", "5 Mio. / 20 Mio.", 3, "hohe Viralität, gesättigt"),
   "UK": (2, "–", "–", "Butternut Box 40 £ (Social ausdrücklich), zooplus UK 7 %", "40–80 £", "zooplus UK Konv. >22 %", "gut", "Teil EN-Pool", 3, "Butternut Box stark"),
   "International-EN": (1, "–", "–", "–", "–", "verwässert", "mittel", "5 Mio. / 20 Mio.", 2, "–")}),
 ("Beauty / Skincare / Devices", {
   "DE/DACH": (2, "personenzentriert", "–", "The Ordinary 13–20 %, Sephora DE 12 %, Lookfantastic 12 %", "30–80 €", "DY Beauty 5,39 %", "gut", "2 Mio. / 7 Mio.", 2, "hohe Raten, aber HIGH Compliance"),
   "US": (2, "personenzentriert", "–", "medicube 20 %, Foreo 6 %/60 T; Sephora/Ulta Impact (nicht öffentlich)", "40–400 $", "DY Beauty 5,39 %", "gut", "3 Mio. / 10 Mio.", 2, "HIGH Compliance"),
   "UK": (2, "–", "–", "Lookfantastic 15 %, Cult Beauty (keine Influencer via Awin)", "–", "–", "gut", "Teil EN-Pool", 2, "–"),
   "International-EN": (2, "–", "–", "–", "–", "–", "mittel", "–", 2, "–")}),
 ("Fashion (faceless)", {
   "DE/DACH": (2, "Theme-Pages existieren (K: D01)", "–", "Breuninger 12 %, Lounge 12 %, OTTO bis 15 % (nur via Stylink/Metapic); Zalando/ABOUT YOU ohne Programm", "40–150 €", "DY Fashion 2,77 %", "Retouren 45–55 %", "2 Mio. / 7 Mio.", 2, "Retouren fressen Provision"),
   "US": (2, "–", "–", "Nike bis 15 %/7 T, Revolve 5 %, LTK/ShopMy (Personen)", "50–300 $", "–", "Retouren 25 %", "5 Mio. / 20 Mio.", 2, "Creator-Plattformen personengebunden"),
   "UK": (2, "–", "–", "adidas UK 6 %, Mytheresa 4 %", "–", "–", "–", "Teil EN-Pool", 2, "–"),
   "International-EN": (2, "–", "–", "–", "–", "–", "mittel", "–", 2, "–")}),
 ("Travel Gear", {
   "DE/DACH": (3, "–", "–", "Koffer.de 5 %, Eastpak 6 %, Horizn DE schließt", "50–300 €", "–", "gut", "1 Mio. / 4 Mio.", 2, "Programme schwach"),
   "US": (3, "–", "–", "NOMATIC 15 %, Tortuga 10 % (AOV >250 $), Travelpro 8–10 %/45 T, Bellroy 7 %", "45–400 $", "–", "gut", "3 Mio. / 10 Mio.", 4, "starke Brand-Programme"),
   "UK": (3, "–", "–", "Db 3 %", "–", "–", "gut", "Teil EN-Pool", 2, "–"),
   "International-EN": (3, "–", "–", "eSIM global (Saily 15 %, Airalo 10 %)", "10–60 $", "–", "gut (digital)", "3 Mio. / 10 Mio.", 4, "eSIM global lieferbar")}),
 ("Golf / Golf-Simulatoren", {
   "DE/DACH": (4, "–", "–", "Golf House 6 %, Golfshop.de 2,5–6 %", "50–500 €", "–", "gut", "0,5 Mio. / 2 Mio.", 2, "klein"),
   "US": (4, "keine Golf-Affiliate-Theme-Page belegt; Shorts mit Mio.-Views ohne Links – J", "–", "SkyTrak 10–15 %, 2nd Swing 5–15 %", "80–5.000 $", "–", "gut", "1,5 Mio. / 5 Mio.", 3, "High-Ticket, kleine Nische"),
   "UK": (3, "–", "–", "American Golf (nicht öffentlich)", "–", "–", "–", "–", 2, "–"),
   "International-EN": (3, "–", "–", "–", "–", "–", "–", "–", 2, "–")}),
]
cols = ["nische", "markt", "instagram_werbereichweite", "e_commerce_markt", "kaufkraft_1_5", "amazon_und_provision", "publikums_geo",
        "cpm_kaufkraft_proxy", "konkurrenz_1_5_(5=wenig)", "grosse_theme_pages_beleg", "professionelle_ai_pages", "affiliate_programme",
        "typischer_aov", "conversion_hinweis", "versand_verfuegbarkeit", "erreichbare_views_monat12_base_strong",
        "gesamtbewertung_1_5", "begruendung", "datenqualitaet"]
with open(os.path.join(ROOT, "02_market_comparison.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(cols)
    n = 0
    for niche, mk in N:
        for m, v in mk.items():
            md = M[m]
            w.writerow([niche, m, md["ig"], md["ecom"], md["kaufkraft"], md["amazon"], md["geo"], md["cpm"], *v,
                        "Marktdaten VERIFIED/THIRD-PARTY (quellen/F); Konkurrenz aus quellen/F, I, J; Bewertungen & Reichweite: MODEL ASSUMPTION"])
            n += 1
print("02:", n, "Zeilen")
