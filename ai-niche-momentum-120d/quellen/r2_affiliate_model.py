"""
R2 – Affiliate-Economics für 19 KI-Short-Form-Momentum-Cluster (EN/US + DE).

Formel (identisch zu affiliate-theme-page-research/10_affiliate_funnel_models.md, Abschnitt 1):
  Provision pro 1 Mio. Views = 1.000.000 × Klicks/1.000 Views × Intent-Faktor × Geo-Anteil
                               × Σ_Kanal [Klickanteil × CVR × AOV × Provision × Netto-Faktor] × (1 − Retouren)
Einzige Erweiterung: Retouren werden je Kanal abgezogen (Bücher/digitale Keys ≠ Trikots im selben Cluster);
bei Fixprovisionen (CPA, z. B. Audible-Bounty) entfallen AOV×Rate und Netto-Faktor.

Parameter-Herkunft:
  CLICKS, INTENT, GEO, CVR, RET, FX, NET, Kosten -> scripts/model.py bzw. quellen/E_funnel_benchmarks.md (M2–M5)
  Programm-Raten -> 03_affiliate_programs.csv (P-IDs) + neue Recherche 26.09.2026 (siehe R2_affiliate_fit_momentum_clusters.md)
Ausführen: python3 r2_affiliate_model.py  -> raw_affiliate_economics_clusters.csv + r2_model_output.json
"""
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SC = ["Base", "Strong"]

CLICKS_PER_1K = [1.2, 3.0]                                  # E M2 / model.py
INTENT_FACTOR = {1: 0.3, 2: 0.5, 3: 0.75, 4: 1.0, 5: 1.2}  # model.py
GEO = {"EN": [0.55, 0.62], "DE": [0.80, 0.85],
       # model.py K03 (Gaming, jüngeres/globaleres Publikum): Base 0,45 / Strong 0,55 – MODEL ASSUMPTION,
       # hier für Kids-/Fußball-/Fandom-/Roblox-Cluster mit EN-Content verwendet
       "EN_YOUNG": [0.45, 0.55]}
CVR = {  # E M3 (Base, Strong)
    "AMZ_US": [0.04, 0.07], "AMZ_DE": [0.03, 0.05],
    "HOME": [0.007, 0.015], "ELEC": [0.009, 0.018], "SPORT": [0.009, 0.018],
    "FASHION": [0.01, 0.02], "PETS": [0.018, 0.03], "LUX": [0.003, 0.006],
    "HIGHTICKET": [0.0005, 0.0012], "TRAVEL": [0.005, 0.010],
    # NEU, kein Kategorie-Benchmark in E: Bücher-/Spielwaren-/Game-Key-/Collectible-Händler
    # -> analog "Elektronik/Sport" (DY Consumer Goods / IRP Sports) – MODEL ASSUMPTION
    "RETAIL": [0.009, 0.018],
}
RET = {  # E M5 (Base, Strong), Provisionsverlust
    ("fashion", "EN"): [0.25, 0.20], ("fashion", "DE"): [0.45, 0.35],
    ("elec", "EN"): [0.10, 0.08], ("elec", "DE"): [0.14, 0.10],
    ("home", "EN"): [0.10, 0.07], ("home", "DE"): [0.12, 0.09],
    ("pets", "EN"): [0.05, 0.03], ("pets", "DE"): [0.06, 0.04],
    ("sport", "EN"): [0.12, 0.09], ("sport", "DE"): [0.20, 0.14],
    ("lux", "EN"): [0.20, 0.15], ("lux", "DE"): [0.25, 0.18],
    # NEU/abgeleitet – MODEL ASSUMPTION:
    ("books", "EN"): [0.05, 0.03], ("books", "DE"): [0.06, 0.04],      # analog Consumables (E M5)
    ("toys", "EN"): [0.10, 0.07], ("toys", "DE"): [0.12, 0.09],        # analog Home
    ("digital", "EN"): [0.03, 0.02], ("digital", "DE"): [0.03, 0.02],  # Keys: Storno/Chargeback, kaum Retoure
    ("travel", "EN"): [0.25, 0.20], ("travel", "DE"): [0.25, 0.20],    # model.py (Stornos, Zahlung nach Reise)
    ("cpa", "EN"): [0.05, 0.03], ("cpa", "DE"): [0.05, 0.03],          # Trial-Bounty-Stornos
}
FX = {"EUR": 1.0, "USD": 0.86, "GBP": 1.16}
NET = {"EN": 0.97, "DE": 1 / 1.19}
COST = 600.0

# Kanal: (Name, Klickanteil, CVR-Key, CVR-Mult, AOV, Währung, Provision, Retouren-Key, CPA-Fixbetrag oder None)
CL = []


def cl(**kw):
    CL.append(kw)


INTENT_LABEL = {1: "ENTERTAINMENT", 2: "ASPIRATION / ENTERTAINMENT (schwacher Produktbezug)",
                3: "PRODUCT DESIRE (indirekt)", 4: "PRODUCT DESIRE", 5: "DIRECT BUYING INTENT"}

# ---------------------------------------------------------------- 1 Story-Serien
cl(nr=1, name="KI-Story-Serien (Roblox/3D, Rettungs-/Moral-Storys)", market="EN", geo="EN_YOUNG", intent=1,
   produkte="Spielzeug/Plüsch, Kinderbücher; Roblox-Gift-Cards (0 % Provision)",
   programme="Amazon US Toys 3 % (P-A023), Amazon US Books 4,5 % (P-A006); Amazon Gift Cards 0 % (P-A036); Roblox Creator Affiliate eingestellt 24.07.2025",
   cookie="Amazon 24 h", ch=[("Amazon Toys", 0.6, "AMZ_US", 1.0, 35, "USD", 0.03, "toys", None),
                             ("Amazon Books (Kinderbuch)", 0.4, "AMZ_US", 1.0, 30, "USD", 0.045, "books", None)],
   dq="Provision VERIFIED (Amazon); Roblox-Programm VERIFIED eingestellt; Intent/Geo/CVR MODEL ASSUMPTION",
   quellen="03_affiliate_programs.csv P-A006/P-A023/P-A036; create.roblox.com/docs/affiliates",
   note="Publikum überwiegend minderjährig/global; Gift-Cards 0 %; kein natürlicher Produktbezug der Story. Structural LOW.")
cl(nr=1, name="KI-Story-Serien (Roblox/3D, Rettungs-/Moral-Storys)", market="DE", geo="DE", intent=1,
   produkte="Spielzeug, Kinderbücher; Roblox-Guthaben (0 %)",
   programme="Amazon.de Alle anderen (Spielzeug) 3 % (P-A059), Bücher 5 % (P-A048), Geschenkkarten 0 % (P-A060); Thalia Spielware 8 % / Buch 11 % (Awin)",
   cookie="Amazon 24 h; Thalia 30 T", ch=[("Amazon.de Spielzeug", 0.5, "AMZ_DE", 1.0, 35, "EUR", 0.03, "toys", None),
                                          ("Amazon.de Bücher", 0.3, "AMZ_DE", 1.0, 30, "EUR", 0.05, "books", None),
                                          ("Thalia (Buch 11 % / Spielware 8 %)", 0.2, "RETAIL", 1.0, 25, "EUR", 0.095, "books", None)],
   dq="Provision VERIFIED (Amazon, Thalia-Awin-Profil); Rest MODEL ASSUMPTION",
   quellen="P-A048/P-A059/P-A060; ui.awin.com/merchant-profile/14158; thalia.de/vorteile/partnerprogramm",
   note="Wie EN; DE-Kids-Content zusätzlich klein. Structural LOW.")

# ---------------------------------------------------------------- 2 Fußball
cl(nr=2, name="KI-Fußball-/Promi-Sketche", market="EN", geo="EN_YOUNG", intent=2,
   produkte="Trikots (Spieler-Trikots), Fußballschuhe, Fan-Artikel, Bälle",
   programme="Fanatics US 5–10 % (Impact, 7 T, THIRD-PARTY), Nike bis 15 % (CJ, 7 T, CLAIMED), Amazon Sports 3 %/Apparel 4 %",
   cookie="Fanatics 7 T; Nike 7 T; Amazon 24 h",
   ch=[("Fanatics (Trikots)", 0.45, "FASHION", 1.0, 100, "USD", 0.05, "fashion", None),
       ("Amazon (Bälle, Schuhe, Fan-Artikel)", 0.35, "AMZ_US", 1.0, 40, "USD", 0.035, "sport", None),
       ("Nike (Schuhe/Trikots)", 0.20, "FASHION", 1.0, 120, "USD", 0.05, "fashion", None)],
   dq="Fanatics/Nike-Raten THIRD-PARTY/CLAIMED (Modell nutzt 5 %, nicht 'bis zu'); AOV ESTIMATED; Rest MODEL ASSUMPTION",
   quellen="getlasso.co/affiliate/fanatics; P-D073 (Nike), P-D151 (Fanatics UNKNOWN in Altbestand); P-A007/P-A021",
   note="Größen -> Fashion-Retouren. KI-Sketche mit realen Spielern: Persönlichkeits-/Markenrecht, Nike/adidas/Fanatics-Brand-Safety-Risiko. Globales, junges Publikum (IN/ID/NG/BR) -> EN_YOUNG-Geo.")
cl(nr=2, name="KI-Fußball-/Promi-Sketche", market="DE", geo="DE", intent=2,
   produkte="Trikots, Fußballschuhe, Teamsport, Fan-Artikel",
   programme="11teamsports 7 % (Top 10 %, Awin, 30 T, VERIFIED), Kitbag/Fanatics EU 3,8–5 % (THIRD-PARTY), Amazon.de Bekleidung 6 %/Sport 4 %, adidas DE 2 % (THIRD-PARTY)",
   cookie="11teamsports 30 T; Kitbag UNKNOWN; Amazon 24 h",
   ch=[("Amazon.de (Sport 4 % / Bekleidung 6 %)", 0.40, "AMZ_DE", 1.0, 45, "EUR", 0.05, "sport", None),
       ("11teamsports", 0.30, "FASHION", 1.0, 80, "EUR", 0.07, "fashion", None),
       ("Kitbag / Fanatics EU", 0.20, "FASHION", 1.0, 90, "EUR", 0.038, "fashion", None),
       ("adidas DE", 0.10, "FASHION", 1.0, 100, "EUR", 0.02, "fashion", None)],
   dq="11teamsports VERIFIED (Awin-Profil 22165); Kitbag/adidas THIRD-PARTY; AOV ESTIMATED; Rest MODEL ASSUMPTION",
   quellen="ui.awin.com/merchant-profile/22165; affiliate-marketing.de/partnerprogramme/kitbag.com; P-D074; P-A037/P-A053",
   note="Unisport: Cookie 3 T, Rate nicht öffentlich. DE-Retouren Fashion 45 %. Rechte-Risiko wie EN.")

# ---------------------------------------------------------------- 3 Film/Anime/Marvel
cl(nr=3, name="Film/Anime/Marvel What-if-3D", market="EN", geo="EN_YOUNG", intent=2,
   produkte="Funko Pop, Actionfiguren (Marvel Legends), Statuen, Blu-ray/Artbooks; Streaming (kein belastbares Programm)",
   programme="Amazon Toys 3 %, Funko 4 % (CJ, THIRD-PARTY), Entertainment Earth bis 10 % cash/15 % Guthaben (SELF-REPORTED), eBay Collectibles 3 % (VERIFIED)",
   cookie="Amazon 24 h; Funko/EE UNKNOWN; eBay 24 h",
   ch=[("Amazon (Figuren/Funko)", 0.60, "AMZ_US", 1.0, 35, "USD", 0.03, "toys", None),
       ("Funko.com / Entertainment Earth", 0.30, "RETAIL", 1.0, 55, "USD", 0.05, "toys", None),
       ("eBay Collectibles", 0.10, "RETAIL", 1.0, 60, "USD", 0.03, "toys", None)],
   dq="Amazon/eBay VERIFIED; Funko THIRD-PARTY; EE SELF-REPORTED ('bis zu'); Streaming UNKNOWN",
   quellen="P-A023, P-D146, P-D152; entertainmentearth.com/affiliate-program (Suchergebnis, Seite 403)",
   note="Disney/Marvel-IP in KI-What-ifs: Urheber-/Markenrisiko, Takedown-Risiko. Crunchyroll/Disney+: Raten dynamisch/unbekannt -> nicht gerechnet.")
cl(nr=3, name="Film/Anime/Marvel What-if-3D", market="DE", geo="DE", intent=2,
   produkte="Funko Pop, Figuren, Merch, Artbooks/Manga",
   programme="Amazon.de Spielzeug 3 %/Bücher 5 %, Thalia Spielware 8 %/Buch 11 % (Awin, 30 T, VERIFIED), eBay Collectibles 3 %",
   cookie="Amazon 24 h; Thalia 30 T",
   ch=[("Amazon.de (Figuren)", 0.55, "AMZ_DE", 1.0, 35, "EUR", 0.03, "toys", None),
       ("Thalia (Manga/Spielware)", 0.30, "RETAIL", 1.0, 30, "EUR", 0.095, "books", None),
       ("eBay Collectibles", 0.15, "RETAIL", 1.0, 60, "EUR", 0.03, "toys", None)],
   dq="Raten VERIFIED (Amazon, Thalia, eBay); Rest MODEL ASSUMPTION",
   quellen="P-A048/P-A059, P-D146; ui.awin.com/merchant-profile/14158",
   note="IP-Risiko wie EN.")

# ---------------------------------------------------------------- 4 Surreal/VFX
cl(nr=4, name="KI-Surreal/VFX/What-if", market="EN", geo="EN_YOUNG", intent=1,
   produkte="keine natürlichen Produkte (höchstens generische Amazon-Links)",
   programme="Amazon US All Other 4 % (P-A035)", cookie="Amazon 24 h",
   ch=[("Amazon generisch", 1.0, "AMZ_US", 0.7, 35, "USD", 0.035, "elec", None)],
   dq="Rate VERIFIED; Produktbezug fehlt -> Rechnung = theoretische Obergrenze",
   quellen="P-A035", note="Kein Kaufanlass im Content. Structural LOW.")
cl(nr=4, name="KI-Surreal/VFX/What-if", market="DE", geo="DE", intent=1,
   produkte="keine natürlichen Produkte", programme="Amazon.de Alle anderen 3 % (P-A059)", cookie="Amazon 24 h",
   ch=[("Amazon.de generisch", 1.0, "AMZ_DE", 0.7, 35, "EUR", 0.03, "elec", None)],
   dq="Rate VERIFIED; Produktbezug fehlt", quellen="P-A059", note="Structural LOW.")

# ---------------------------------------------------------------- 5 Tiere/Tierrettung
cl(nr=5, name="KI-Tiere & Tierrettung/Wholesome", market="EN", geo="EN", intent=2,
   produkte="Hundespielzeug, Futter-/Kratzbaum-Produkte, Pet-Gadgets; Tierschutz-Spenden (keine Provision)",
   programme="Amazon Pets 3 %, Chewy 1 %/4 % (Impact, 15 T), PETLIBRO 8 %, Tuft + Paw 12 %, Litter-Robot 8 %",
   cookie="Amazon 24 h; Chewy 15 T; Brands 30–90 T",
   ch=[("Amazon Pets", 0.70, "AMZ_US", 1.0, 35, "USD", 0.03, "pets", None),
       ("Pet-Brands (PETLIBRO/Tuft+Paw/Litter-Robot)", 0.30, "PETS", 1.0, 90, "USD", 0.09, "pets", None)],
   dq="Raten VERIFIED (03_affiliate_programs.csv); AOV Brands ESTIMATED",
   quellen="P-A019, P-C117, P-C122, P-C123, P-C126",
   note="Wal-/Hai-/Wildtierrettung hat keinen Produktbezug; nur Haustier-Content (Hund/Katze) verlinkbar. KI-Tiere, die Produkte 'benutzen' = irreführend (G).")
cl(nr=5, name="KI-Tiere & Tierrettung/Wholesome", market="DE", geo="DE", intent=2,
   produkte="Hunde-/Katzenzubehör, Futter; Spenden (0 €)",
   programme="Amazon.de 3 %, Fressnapf 8 % Neukunde (60 T), ZooRoyal 3–12 %, wildfang 10–13 %",
   cookie="Amazon 24 h; Shops 30–60 T",
   ch=[("Amazon.de Haustier", 0.60, "AMZ_DE", 1.0, 35, "EUR", 0.03, "pets", None),
       ("Shops (Fressnapf/ZooRoyal/wildfang)", 0.40, "PETS", 1.0, 55, "EUR", 0.09, "pets", None)],
   dq="Raten VERIFIED; Kanalmix = model.py K23", quellen="P-C129, P-C130, P-C135; model.py K23",
   note="Wie EN.")

# ---------------------------------------------------------------- 6 DIY/Cabin
cl(nr=6, name="KI-DIY/Hausbau/Cabin/Tiny House/Handwerk", market="EN", geo="EN", intent=3,
   produkte="Werkzeug/Akkugeräte, Holzbearbeitung, Cabin-/Tiny-House-Kits, Baustoffe",
   programme="Amazon Tools/Home Improvement 3 %, VEVOR 4–5 % (Impact, 30 T), Jamaica Cottage Shop Cabin-Kits 5 % (direkt), Home Depot 1 %/Lowe's 1 % (1 T)",
   cookie="Amazon 24 h; VEVOR 30 T; JCS UNKNOWN",
   ch=[("Amazon Tools", 0.60, "AMZ_US", 1.0, 55, "USD", 0.03, "home", None),
       ("VEVOR (Werkzeug/Equipment)", 0.25, "ELEC", 1.0, 150, "USD", 0.05, "home", None),
       ("Cabin-Kits (Jamaica Cottage Shop)", 0.15, "HIGHTICKET", 1.0, 8000, "USD", 0.05, "home", None)],
   dq="Amazon/VEVOR VERIFIED; JCS 5 % VERIFIED (Programmseite), AOV Cabin-Kit ESTIMATED; High-Ticket-CVR MODEL ASSUMPTION",
   quellen="P-A017/P-A020, P-C072, P-C068/P-C069; jamaicacottageshop.com/affiliate-signup",
   note="Allwood: kein Programm gefunden (UNKNOWN). KI-Bau-Content zeigt unrealistische Bauzeiten -> Werkzeug-Links ok, Kit-Versprechen nicht.")
cl(nr=6, name="KI-DIY/Hausbau/Cabin/Tiny House/Handwerk", market="DE", geo="DE", intent=3,
   produkte="Werkzeug, Holz/Baustoffe, Gartenhäuser/Tiny-House-Kits",
   programme="Amazon.de Baumarkt/Elektrowerkzeuge 5 %, hagebau Content 10 % (60 T), toom Content 8 %, BAUHAUS Content 7 %, OBI Content 7 %, GartenHaus GmbH Content 7 % (Awin, 30 T), Gartenhausfabrik 7 %",
   cookie="Amazon 24 h; Baumärkte 30–60 T; GartenHaus 30 T",
   ch=[("Amazon.de Baumarkt/Werkzeug", 0.50, "AMZ_DE", 1.0, 55, "EUR", 0.05, "home", None),
       ("Baumärkte Content-Raten (hagebau/toom/BAUHAUS/OBI)", 0.35, "HOME", 1.0, 150, "EUR", 0.08, "home", None),
       ("Gartenhaus-/Tiny-House-Kits (GartenHaus GmbH, Gartenhausfabrik)", 0.15, "HIGHTICKET", 2.0, 2000, "EUR", 0.07, "home", None)],
   dq="Raten VERIFIED (Awin-Profile, 03); AOV Baumarkt/Gartenhaus ESTIMATED (hagebau nennt >260 € netto, SELF-REPORTED)",
   quellen="P-A044/P-A045, P-C075–P-C078, P-C022, P-C035; ui.awin.com/merchant-profile/22747",
   note="Stärkstes 'Kauf-nahes' KI-Ästhetik-Cluster in DE. Momentum auf YT aber verlangsamt (M5).")

# ---------------------------------------------------------------- 7 Restoration/ASMR
cl(nr=7, name="KI-Restoration/Satisfying/ASMR", market="EN", geo="EN", intent=3,
   produkte="Poliermittel, Car-Detailing, Reiniger, Hochdruckreiniger, Handwerkzeug",
   programme="Amazon Automotive 4,5 %/Tools 3 %, Chemical Guys bis 10 % (CJ, Ø-Sale >100 $), Kärcher UK bis 5 % (CJ, 30 T)",
   cookie="Amazon 24 h; Chemical Guys UNKNOWN; Kärcher 30 T",
   ch=[("Amazon (Auto/Tools/Reiniger)", 0.65, "AMZ_US", 1.0, 35, "USD", 0.04, "elec", None),
       ("Chemical Guys", 0.20, "ELEC", 1.0, 100, "USD", 0.07, "elec", None),
       ("Kärcher", 0.15, "ELEC", 1.0, 200, "USD", 0.05, "elec", None)],
   dq="Amazon VERIFIED; Chemical Guys 'bis 10 %' VERIFIED/SELF-REPORTED (Modell 7 %); Kärcher UK 'bis 5 %' VERIFIED (Programmseite); AOV teils SELF-REPORTED",
   quellen="P-A005/P-A020, P-C100; karcher.com/gb/en/home-and-garden/join-the-karcher-affiliate-program",
   note="Compliance: KI-Restaurationsergebnis darf nicht als Produktwirkung gezeigt werden (G) -> Links nur als 'Tools used in real restorations'.")
cl(nr=7, name="KI-Restoration/Satisfying/ASMR", market="DE", geo="DE", intent=3,
   produkte="Autopflege, Poliermaschinen, Reiniger, Hochdruckreiniger, Werkzeug",
   programme="Amazon.de Auto 5 %/Baumarkt 5 %, Kärcher AT 5 % (Awin, 30 T, AOV 230 €), Autodoc 8 %, kfzteile24 6–8 %",
   cookie="Amazon 24 h; Kärcher/Autodoc/kfzteile24 30 T",
   ch=[("Amazon.de (Auto/Baumarkt)", 0.65, "AMZ_DE", 1.0, 35, "EUR", 0.05, "elec", None),
       ("Kärcher (AT-Programm; DE UNKNOWN)", 0.15, "ELEC", 1.0, 230, "EUR", 0.05, "elec", None),
       ("Autodoc / kfzteile24", 0.20, "ELEC", 1.0, 80, "EUR", 0.07, "elec", None)],
   dq="Raten VERIFIED (Kärcher AT Awin 40254 inkl. AOV 230 €; Autodoc/kfzteile24 aus 03)",
   quellen="P-A044/P-A047, P-C107, P-C109; ui.awin.com/merchant-profile/40254",
   note="Kärcher DE-Programm nicht gefunden – AT-Programm (DE-sprachig) als Proxy, Lieferland beachten.")

# ---------------------------------------------------------------- 8 Geschichte/POV
cl(nr=8, name="KI-Geschichte/POV/Zeitreise", market="EN", geo="EN", intent=2,
   produkte="Geschichtsbücher, Hörbücher, Strategie-/Brettspiele, Museums-/Stadt-Touren",
   programme="Amazon Books 4,5 %, Bookshop.org 10 % (THIRD-PARTY), Audible Trial-Bounty 5 $ (THIRD-PARTY), GetYourGuide 8 % (31 T, CLAIMED), Viator 8 % (VERIFIED)",
   cookie="Amazon 24 h; Bookshop UNKNOWN; GYG 31 T; Viator 30 T",
   ch=[("Amazon Books", 0.45, "AMZ_US", 1.0, 35, "USD", 0.045, "books", None),
       ("Bookshop.org", 0.10, "RETAIL", 1.0, 30, "USD", 0.10, "books", None),
       ("Audible Free-Trial", 0.25, "AMZ_US", 0.5, 0, "USD", 0.0, "cpa", 5.0),
       ("GetYourGuide/Viator (Touren)", 0.20, "TRAVEL", 1.0, 70, "USD", 0.08, "travel", None)],
   dq="Amazon Books VERIFIED; Bookshop/Audible THIRD-PARTY; GYG CLAIMED; Tour-AOV ESTIMATED",
   quellen="P-A006, P-D026, P-D027; getlasso.co/affiliate/bookshop; bloggingtips.com/audible-affiliate-program",
   note="Audible-Bounty als Fixbetrag gerechnet (kein Netto-Faktor). Bildungs-Content -> Bücher logisch, aber Impulskauf schwach.")
cl(nr=8, name="KI-Geschichte/POV/Zeitreise", market="DE", geo="DE", intent=2,
   produkte="Sachbücher/Geschichte, Brettspiele, Touren",
   programme="Amazon.de Bücher 5 %, Thalia Buch 11 % (Awin, 30 T, VERIFIED), Milan-Spiele 5 % (THIRD-PARTY), GetYourGuide 8 %",
   cookie="Amazon 24 h; Thalia 30 T; GYG 31 T",
   ch=[("Amazon.de Bücher", 0.45, "AMZ_DE", 1.0, 35, "EUR", 0.05, "books", None),
       ("Thalia Bücher", 0.25, "RETAIL", 1.0, 25, "EUR", 0.11, "books", None),
       ("Milan-Spiele (Strategie-/Brettspiele)", 0.15, "RETAIL", 1.0, 45, "EUR", 0.05, "toys", None),
       ("GetYourGuide (Touren)", 0.15, "TRAVEL", 1.0, 60, "EUR", 0.08, "travel", None)],
   dq="Amazon/Thalia VERIFIED; Milan THIRD-PARTY; GYG CLAIMED; AOV ESTIMATED",
   quellen="P-A048, P-D026; ui.awin.com/merchant-profile/14158; affiliate-marketing.de/partnerprogramme/milan-spiele.de",
   note="Buchpreisbindung -> Thalia-Rate 11 % gilt auch für preisgebundene Bücher. Hugendubel: nicht geprüft (Suchbudget).")

# ---------------------------------------------------------------- 9 Babys/Familie
cl(nr=9, name="KI-Babys/Familie", market="EN", geo="EN", intent=2,
   produkte="Babyausstattung, Spielzeug, Schlaf-/Stillprodukte",
   programme="Amazon Baby 3 %, Momcozy 10 %, CYBEX 6 %, Target 3 % (7 T), Babylist 1 %",
   cookie="Amazon 24 h; Brands 30 T; Target 7 T",
   ch=[("Amazon Baby", 0.70, "AMZ_US", 1.0, 35, "USD", 0.03, "home", None),
       ("Baby-Brands (Momcozy/CYBEX)", 0.30, "HOME", 1.0, 150, "USD", 0.08, "home", None)],
   dq="Raten VERIFIED; AOV Brands ESTIMATED", quellen="P-A024, P-C138, P-C139, P-C146",
   note="Compliance HIGH (Eltern-Vertrauen, Sicherheitsclaims, KI-Babys mit Produkten). Content = Comedy, kein Kaufanlass.")
cl(nr=9, name="KI-Babys/Familie", market="DE", geo="DE", intent=2,
   produkte="Babyausstattung, Kinderwagen, Spielzeug",
   programme="Amazon.de 3 %, babymarkt 5 %, baby-walz 6 % (10 T), Babybrands 2–7 % (AOV 224 €)",
   cookie="Amazon 24 h; babymarkt 30 T; baby-walz 10 T",
   ch=[("Amazon.de Baby", 0.65, "AMZ_DE", 1.0, 35, "EUR", 0.03, "home", None),
       ("babymarkt / baby-walz", 0.35, "HOME", 1.0, 90, "EUR", 0.055, "home", None)],
   dq="Raten VERIFIED; AOV ESTIMATED", quellen="P-A059, P-C151, P-C152, P-C154",
   note="Compliance HIGH.")

# ---------------------------------------------------------------- 10 Kochen
cl(nr=10, name="KI-Kochen/Village-Food/Cozy Cooking", market="EN", geo="EN", intent=3,
   produkte="Gusseisen (Lodge), Dutch Oven, Messer, Feuer-/Outdoor-Küche",
   programme="Amazon Kitchen 4,5 % (Lodge nur via Amazon – kein eigenes Programm gefunden), Zwilling/Staub US 6 % (CJ, THIRD-PARTY), Le Creuset US 4 % (THIRD-PARTY)",
   cookie="Amazon 24 h; Zwilling UNKNOWN",
   ch=[("Amazon Kitchen (Lodge u. a.)", 0.70, "AMZ_US", 1.0, 45, "USD", 0.045, "home", None),
       ("Zwilling/Staub, Le Creuset", 0.30, "HOME", 1.0, 180, "USD", 0.055, "home", None)],
   dq="Amazon VERIFIED; Zwilling/Le Creuset THIRD-PARTY; Lodge-Programm UNKNOWN (nicht gefunden)",
   quellen="P-A004, P-B068, P-B071; lodge.knoji.com / viglink (kein Programm)",
   note="Village-Cooking-Ästhetik (offenes Feuer) passt zu Gusseisen; Momentum ONE-OFF (M5).")
cl(nr=10, name="KI-Kochen/Village-Food/Cozy Cooking", market="DE", geo="DE", intent=3,
   produkte="Gusseisen/Feuertopf, Messer, Kochgeschirr",
   programme="Amazon.de Küche 5 %, Petromax 4–12 % (Adcell, 60 T, Ø-WK 96 €), Zwilling/Staub DE 6,4–8 % (Awin), WMF 5 %",
   cookie="Amazon 24 h; Petromax 60 T; Zwilling UNKNOWN",
   ch=[("Amazon.de Küche", 0.55, "AMZ_DE", 1.0, 45, "EUR", 0.05, "home", None),
       ("Petromax", 0.20, "HOME", 1.0, 96, "EUR", 0.08, "home", None),
       ("Zwilling/Staub, WMF", 0.25, "HOME", 1.0, 150, "EUR", 0.064, "home", None)],
   dq="Amazon/Petromax VERIFIED (Adcell-Ø-WK); Petromax-Rate Mitte der Spanne = ESTIMATED; Zwilling THIRD-PARTY",
   quellen="P-A043, P-C020, P-B065, P-B066",
   note="Solider Produktbezug; Petromax passt zur Feuerküche.")

# ---------------------------------------------------------------- 11 Reise
cl(nr=11, name="KI-Reise-Traumorte/Nature", market="EN", geo="EN", intent=2,
   produkte="Touren/Aktivitäten, Hotels, Travel Gear",
   programme="GetYourGuide 8 % (31 T, CLAIMED), Viator 8 % (30 T, VERIFIED), Booking.com Anteil (THIRD-PARTY), Amazon Luggage 4 %",
   cookie="GYG 31 T; Viator 30 T; Booking ~30 T",
   ch=[("GetYourGuide/Viator", 0.50, "TRAVEL", 1.0, 80, "USD", 0.08, "travel", None),
       ("Booking.com (Hotel)", 0.30, "TRAVEL", 1.0, 400, "USD", 0.04, "travel", None),
       ("Amazon Travel Gear", 0.20, "AMZ_US", 0.8, 45, "USD", 0.04, "sport", None)],
   dq="Viator VERIFIED; GYG CLAIMED; Booking THIRD-PARTY (Anteil an Booking-Provision ≈4 % Buchungswert = ESTIMATED); AOV ESTIMATED",
   quellen="P-D024, P-D026, P-D027, P-A010; model.py K30",
   note="'Places that don't feel real' = teils fiktive Orte -> Link nur bei realen Zielen, sonst irreführend. Provision erst nach Reise.")
cl(nr=11, name="KI-Reise-Traumorte/Nature", market="DE", geo="DE", intent=2,
   produkte="Touren, Hotels, Reisegepäck",
   programme="GetYourGuide 8 %, Booking.com (Awin), Amazon.de Gepäck 4 %",
   cookie="GYG 31 T; Booking ~30 T",
   ch=[("GetYourGuide", 0.50, "TRAVEL", 1.0, 70, "EUR", 0.08, "travel", None),
       ("Booking.com (Hotel)", 0.30, "TRAVEL", 1.0, 350, "EUR", 0.04, "travel", None),
       ("Amazon.de Gepäck", 0.20, "AMZ_DE", 0.8, 45, "EUR", 0.04, "sport", None)],
   dq="wie EN", quellen="P-D024, P-D026, P-A051", note="wie EN.")

# ---------------------------------------------------------------- 12 Horror/Mystery
cl(nr=12, name="KI-Horror/Mystery", market="EN", geo="EN_YOUNG", intent=2,
   produkte="Horror-Bücher, Horror-Games (Keys), Horror-Brettspiele",
   programme="Amazon Books 4,5 %, Green Man Gaming bis 5 % (Impact, SELF-REPORTED), Humble 4–10 % (THIRD-PARTY), Fanatical 2–5 % (THIRD-PARTY), Miniature Market 5 % (7 T, VERIFIED); Steam: kein Affiliate-Programm",
   cookie="Amazon 24 h; Miniature Market 7 T; Keyshops UNKNOWN",
   ch=[("Amazon Books", 0.40, "AMZ_US", 1.0, 35, "USD", 0.045, "books", None),
       ("Game-Keys (GMG/Humble/Fanatical)", 0.40, "RETAIL", 1.0, 25, "USD", 0.04, "digital", None),
       ("Miniature Market (Brettspiele)", 0.20, "RETAIL", 1.0, 60, "USD", 0.05, "toys", None)],
   dq="Amazon/Miniature Market VERIFIED; GMG SELF-REPORTED ('up to'); Humble/Fanatical THIRD-PARTY",
   quellen="P-A006, P-D154; greenmangaming.com/affiliates; affiliateroll.com (Humble vs GMG); uppromote.com (Fanatical)",
   note="Roblox-Mystery-Publikum jung. Momentum hängt an Einzelkanal (M5).")
cl(nr=12, name="KI-Horror/Mystery", market="DE", geo="DE", intent=2,
   produkte="Horror-/Mystery-Bücher, Game-Keys, Brettspiele",
   programme="Amazon.de Bücher 5 %, Thalia 11 %, Instant Gaming ~3 % (dynamisch, THIRD-PARTY), GMG bis 5 %",
   cookie="Amazon 24 h; Thalia 30 T; Instant Gaming 24 h (THIRD-PARTY)",
   ch=[("Amazon.de Bücher", 0.40, "AMZ_DE", 1.0, 35, "EUR", 0.05, "books", None),
       ("Game-Keys (Instant Gaming/GMG)", 0.35, "RETAIL", 1.0, 25, "EUR", 0.035, "digital", None),
       ("Thalia Bücher", 0.25, "RETAIL", 1.0, 25, "EUR", 0.11, "books", None)],
   dq="Amazon/Thalia VERIFIED; Keyshops THIRD-PARTY", quellen="P-A048; Awin 14158; cuelinks/linkmydeals (Instant Gaming)",
   note="Keyshop-Raten dynamisch; Grey-Market-Keys (G2A u. ä.) bewusst ausgeschlossen.")

# ---------------------------------------------------------------- 13 Autos/Luxus
cl(nr=13, name="KI-Autos/Luxus", market="EN", geo="EN", intent=2,
   produkte="Autozubehör, Car Care, Modellautos/LEGO Technic",
   programme="Amazon Automotive 4,5 %/Toys 3 %, Chemical Guys bis 10 % (CJ), Nextbase 5 %",
   cookie="Amazon 24 h; Nextbase 14 T",
   ch=[("Amazon Automotive", 0.50, "AMZ_US", 1.0, 35, "USD", 0.045, "elec", None),
       ("Amazon Modellautos/LEGO", 0.30, "AMZ_US", 1.0, 40, "USD", 0.03, "toys", None),
       ("Chemical Guys", 0.20, "ELEC", 1.0, 100, "USD", 0.07, "elec", None)],
   dq="Amazon VERIFIED; Chemical Guys 'bis' VERIFIED (Modell 7 %)", quellen="P-A005, P-A023, P-C100, P-C104",
   note="Luxusautos selbst nicht affiliate-fähig; Publikum aspirativ/jung.")
cl(nr=13, name="KI-Autos/Luxus", market="DE", geo="DE", intent=2,
   produkte="Autozubehör, Autopflege, Modellautos",
   programme="Amazon.de Auto 5 %, CK-Modelcars 7 % Neukunde/4 % (Awin, 30 T, Ø-WK 160 €), Autodoc 8 %",
   cookie="Amazon 24 h; CK-Modelcars 30 T; Autodoc 30 T",
   ch=[("Amazon.de Auto", 0.50, "AMZ_DE", 1.0, 35, "EUR", 0.05, "elec", None),
       ("CK-Modelcars", 0.25, "RETAIL", 1.0, 160, "EUR", 0.06, "toys", None),
       ("Autodoc", 0.25, "ELEC", 1.0, 80, "EUR", 0.08, "elec", None)],
   dq="Raten VERIFIED (CK-Modelcars Awin 115681 inkl. Ø-WK 160 €, SELF-REPORTED); Mischsatz 6 % ESTIMATED",
   quellen="P-A047, P-C107; ui.awin.com/merchant-profile/115681", note="Modellautos = logischster Produktbezug.")

# ---------------------------------------------------------------- 14 Interior
cl(nr=14, name="KI-Interior/Architektur/Dream Rooms", market="EN", geo="EN", intent=2,
   produkte="Deko, Leuchten, Möbel ('ähnliche' Produkte)",
   programme="Amazon Home/Furniture 3 %, AllModern 8 % (45 T), Wayfair",
   cookie="Amazon 24 h; AllModern 45 T",
   ch=[("Amazon ('ähnliche' Deko)", 0.60, "AMZ_US", 0.7, 60, "USD", 0.03, "home", None),
       ("Möbel-Shops (AllModern 8 %)", 0.40, "HOME", 0.7, 400, "USD", 0.06, "home", None)],
   dq="= model.py K29 (Raten VERIFIED, Rest MODEL ASSUMPTION)", quellen="model.py K29; P-A015/P-A016",
   note="Unverändert aus Vorstudie übernommen.")
cl(nr=14, name="KI-Interior/Architektur/Dream Rooms", market="DE", geo="DE", intent=2,
   produkte="Deko, Leuchten, Möbel",
   programme="Amazon.de Wohnen/Möbel 5 %, Connox 8 % (60 T), Westwing 4,9–6 %, Nordic Nest 8 %",
   cookie="Amazon 24 h; Connox 60 T; Westwing 30 T",
   ch=[("Amazon.de Wohnen", 0.60, "AMZ_DE", 0.7, 45, "EUR", 0.05, "home", None),
       ("Shops (Connox/Westwing/Nordic Nest)", 0.40, "HOME", 0.7, 150, "EUR", 0.07, "home", None)],
   dq="Raten VERIFIED/THIRD-PARTY (03); Kanalmix analog K04/K29", quellen="P-A041/P-A042, P-A100; model.py K04",
   note="KI-Traumräume ≠ kaufbare Produkte (Abschlag CVR ×0,7 wie K29).")

# ---------------------------------------------------------------- 15 Fashion/AI-Personas
cl(nr=15, name="KI-Fashion/AI-Personas", market="EN", geo="EN", intent=3,
   produkte="Kleidung, Schuhe, Accessoires (Shop the look)",
   programme="Amazon Apparel/Shoes 4 %, REVOLVE 5 %, Shopbop 4 % (THIRD-PARTY), Walmart Creator Fashion 20 % (CLAIMED)",
   cookie="Amazon 24 h; Shops UNKNOWN",
   ch=[("Amazon Fashion", 0.40, "AMZ_US", 1.0, 40, "USD", 0.04, "fashion", None),
       ("Fashion-Shops (REVOLVE/Shopbop)", 0.60, "FASHION", 1.0, 110, "USD", 0.05, "fashion", None)],
   dq="Amazon VERIFIED; Shops THIRD-PARTY; Walmart 20 % CLAIMED (nicht gerechnet)", quellen="P-A007/P-A011, P-D127, P-D128, P-A092",
   note="AI-Persona trägt nicht existierende Outfits -> nur 1:1 reale Artikel verlinken (G). Retouren hoch.")
cl(nr=15, name="KI-Fashion/AI-Personas", market="DE", geo="DE", intent=3,
   produkte="Kleidung, Schuhe, Accessoires",
   programme="Amazon.de Bekleidung 6 %, Breuninger 12 %, Lounge by Zalando 12 %, Mango 6 %, OTTO bis 15 % (CLAIMED)",
   cookie="Amazon 24 h; OTTO 30 T; Rest UNKNOWN",
   ch=[("Amazon.de Fashion", 0.30, "AMZ_DE", 1.0, 45, "EUR", 0.06, "fashion", None),
       ("Shops (Breuninger/Lounge/Mango/OTTO)", 0.70, "FASHION", 1.0, 120, "EUR", 0.10, "fashion", None)],
   dq="= model.py K20 (Raten THIRD-PARTY/VERIFIED)", quellen="model.py K20; P-A037, P-D119–P-D121, P-D129",
   note="DE-Fashion-Retouren 45 % (Base).")

# ---------------------------------------------------------------- 16 Nostalgie
cl(nr=16, name="KI-Nostalgie (80er/90er, BRD/DDR)", market="EN", geo="EN", intent=2,
   produkte="Retro-Konsolen/Mini-Konsolen, Retro-Spielzeug, Vinyl, Bücher, Nostalgie-Süßigkeiten",
   programme="Amazon Physical Video Games & Consoles 1 %, Amazon Toys 3 %/All other 4 %, Retro-Shops 5–10 % (SELF-REPORTED, klein), Amazon Books 4,5 %",
   cookie="Amazon 24 h; Retro-Shops UNKNOWN",
   ch=[("Amazon Retro-Konsolen", 0.30, "AMZ_US", 1.0, 60, "USD", 0.01, "elec", None),
       ("Amazon Retro-Spielzeug/Vinyl/Candy", 0.40, "AMZ_US", 1.0, 35, "USD", 0.035, "toys", None),
       ("Retro-Shops (Retro vGames/GoRetrogame)", 0.15, "RETAIL", 1.0, 60, "USD", 0.10, "elec", None),
       ("Amazon Books", 0.15, "AMZ_US", 1.0, 35, "USD", 0.045, "books", None)],
   dq="Amazon VERIFIED; Retro-Shops SELF-REPORTED; Nostalgie-Süßwaren-Programme UNKNOWN",
   quellen="P-A031, P-A023, P-A035, P-A006; retrovgames.com/affiliates, goretrogame.com/affiliate-program (Suchergebnisse)",
   note="Konsolen nur 1 % bei Amazon -> Kernprodukt schlecht vergütet.")
cl(nr=16, name="KI-Nostalgie (80er/90er, BRD/DDR)", market="DE", geo="DE", intent=2,
   produkte="Retro-Konsolen, Retro-Spielzeug, Vinyl, Bücher, Ostprodukte/Süßigkeiten",
   programme="Amazon.de Videospiele 1 %/Spielzeug 3 %/Bücher 5 %, HHV Vinyl bis 8 % (Webgains, 30 T, VERIFIED), Thalia Buch 11 %/Spielware 8 %",
   cookie="Amazon 24 h; HHV 30 T; Thalia 30 T",
   ch=[("Amazon.de Retro-Konsolen", 0.25, "AMZ_DE", 1.0, 60, "EUR", 0.01, "elec", None),
       ("Amazon.de Spielzeug/Sonstiges", 0.25, "AMZ_DE", 1.0, 35, "EUR", 0.03, "toys", None),
       ("HHV (Vinyl)", 0.15, "RETAIL", 1.0, 45, "EUR", 0.08, "toys", None),
       ("Thalia (Buch/Spielware)", 0.20, "RETAIL", 1.0, 25, "EUR", 0.095, "books", None),
       ("Amazon.de Bücher", 0.15, "AMZ_DE", 1.0, 35, "EUR", 0.05, "books", None)],
   dq="Raten VERIFIED (HHV-Programmseite 'bis zu 8 %', Thalia, Amazon); HHV-AOV ESTIMATED",
   quellen="P-A058/P-A059/P-A048; hhv.de/en-US/help/affiliate-partner-program; Awin 14158",
   note="DDR-/Ostprodukte-Shops: kein Programm gefunden (UNKNOWN). DE-Publikum älter/kaufkräftiger als EN – Upside nicht belegt.")

# ---------------------------------------------------------------- 17 Garten
cl(nr=17, name="KI-Garten/Obst/Pflanzen", market="EN", geo="EN", intent=2,
   produkte="Saatgut, Pflanzen, Gartenwerkzeug, Hochbeete",
   programme="Amazon Lawn & Garden 3 %, The Sill 10 %, Eden Brothers 2 %/10 % Creator, Gardener's Supply 4 %",
   cookie="Amazon 24 h; Shops 30 T",
   ch=[("Amazon Garden", 0.50, "AMZ_US", 1.0, 35, "USD", 0.03, "home", None),
       ("Garten-Shops (The Sill/Eden Brothers/Gardener's Supply)", 0.50, "HOME", 1.0, 70, "USD", 0.07, "home", None)],
   dq="Raten VERIFIED (03); AOV ESTIMATED", quellen="P-A018, P-C057–P-C059",
   note="KI-Fantasie-Obst ('Regenbogen-Früchte') -> Saatgut-Scam-Nähe; nur reale Sorten verlinken.")
cl(nr=17, name="KI-Garten/Obst/Pflanzen", market="DE", geo="DE", intent=2,
   produkte="Pflanzen, Saatgut, Gartengeräte",
   programme="Amazon.de Garten 3 %/Baumarkt 5 %, STIHL 8 %, BALDUR 8 % (90 T), Plantura 10 %, hagebau Content 10 %",
   cookie="Amazon 24 h; Shops 30–90 T",
   ch=[("Amazon.de Garten/Baumarkt", 0.50, "AMZ_DE", 0.9, 45, "EUR", 0.04, "home", None),
       ("Shops (STIHL/Baldur/Plantura/hagebau)", 0.50, "HOME", 1.0, 120, "EUR", 0.08, "home", None)],
   dq="= model.py K26 Kanalmix (Raten VERIFIED)", quellen="model.py K26; P-C048–P-C052",
   note="Plantura-Stornoquote 41 % (C) nicht separat modelliert.")

# ---------------------------------------------------------------- 18 Gadgets-Konzepte
cl(nr=18, name="KI-Produkte/Gadget-Konzepte", market="EN", geo="EN", intent=3,
   produkte="reale Gadgets, die dem Konzept ähneln (Amazon Finds)",
   programme="Amazon All other 4 %, Ugreen 8 %, Casetify 10 %, Nomad 10 %",
   cookie="Amazon 24 h",
   ch=[("Amazon.com", 0.90, "AMZ_US", 1.0, 35, "USD", 0.04, "elec", None),
       ("Brands (Ugreen/Casetify/Nomad)", 0.10, "ELEC", 1.0, 80, "USD", 0.08, "elec", None)],
   dq="= model.py K14 (Raten VERIFIED)", quellen="model.py K14",
   note="Konzept-Produkte existieren nicht -> Intent 3 statt 5 (K14). Irreführungsrisiko, wenn Link 'das Produkt' suggeriert.")
cl(nr=18, name="KI-Produkte/Gadget-Konzepte", market="DE", geo="DE", intent=3,
   produkte="reale ähnliche Gadgets",
   programme="Amazon.de Alle anderen 3 %, Ugreen 8 %, Govee 5–12 %", cookie="Amazon 24 h",
   ch=[("Amazon.de", 0.90, "AMZ_DE", 1.0, 35, "EUR", 0.03, "elec", None),
       ("Brands (Ugreen/Govee)", 0.10, "ELEC", 1.0, 70, "EUR", 0.07, "elec", None)],
   dq="= model.py K15", quellen="model.py K15", note="wie EN.")

# ---------------------------------------------------------------- 19 Kids/Game-Figuren
cl(nr=19, name="Kids/Game-Figuren (Poppy Playtime, Sonic, Minecraft, KPop Demon Hunters)", market="EN", geo="EN_YOUNG", intent=2,
   produkte="Plüsch/Figuren, LEGO Minecraft, Spielzeug; Gaming-Gift-Cards (0 %)",
   programme="Amazon Toys 3 %, Target 3 % (7 T), Smyths 5–10 % (UK, THIRD-PARTY), LEGO US UNKNOWN; Gift Cards 0 %",
   cookie="Amazon 24 h; Target 7 T; Smyths 30 T (THIRD-PARTY)",
   ch=[("Amazon Toys", 0.75, "AMZ_US", 1.0, 35, "USD", 0.03, "toys", None),
       ("Target / Smyths (UK)", 0.25, "RETAIL", 1.0, 40, "USD", 0.04, "toys", None)],
   dq="Amazon/Target VERIFIED; Smyths THIRD-PARTY; LEGO US UNKNOWN",
   quellen="P-A023, P-A036, P-A094, P-D147; flexoffers.com (Smyths)",
   note="Minderjährige Zielgruppe (YouTube 'made for kids' -> keine Kommentare/Links; COPPA/JMStV). Fan-Figuren = fremde IP.")
cl(nr=19, name="Kids/Game-Figuren (Poppy Playtime, Sonic, Minecraft, KPop Demon Hunters)", market="DE", geo="DE", intent=2,
   produkte="Spielzeug, LEGO, Plüsch",
   programme="Amazon.de Spielzeug 3 %, LEGO 3,57 % (Daisycon, THIRD-PARTY), Thalia Spielware 8 %; myToys nicht geprüft",
   cookie="Amazon 24 h; Thalia 30 T; LEGO UNKNOWN",
   ch=[("Amazon.de Spielzeug", 0.60, "AMZ_DE", 1.0, 35, "EUR", 0.03, "toys", None),
       ("LEGO (Daisycon)", 0.20, "RETAIL", 1.0, 70, "EUR", 0.0357, "toys", None),
       ("Thalia Spielware", 0.20, "RETAIL", 1.0, 30, "EUR", 0.08, "toys", None)],
   dq="Amazon/Thalia VERIFIED; LEGO THIRD-PARTY", quellen="P-A059, P-D148; Awin 14158",
   note="wie EN; Jugendschutz.")


# ------------------------------------------------------------------ Rechnung
def compute(c):
    m = c["market"]
    net = NET[m]
    geo = GEO[c["geo"]]
    out = {}
    for i, s in enumerate(SC):
        clicks = 1e6 / 1000 * CLICKS_PER_1K[i] * INTENT_FACTOR[c["intent"]] * geo[i]
        orders = gross = netc = 0.0
        for (n, sh, ck, mu, aov, cur, rate, rk, cpa) in c["ch"]:
            o = clicks * sh * CVR[ck][i] * mu
            per = cpa * FX[cur] if cpa else aov * FX[cur] * rate * net
            g = o * per
            r = RET[(rk, m)][i]
            orders += o
            gross += g
            netc += g * (1 - r)
        out[s] = {"clicks": clicks, "orders": orders, "cvr": orders / clicks, "comm_gross": gross,
                  "rev": netc, "ret_w": 1 - netc / gross if gross else 0}
    # Struktur (Base-Bestellgewichte): AOV, nominaler Satz, Provision/Sale nominal
    w = [(sh * CVR[ck][0] * mu, aov * FX[cur], rate, cpa) for (n, sh, ck, mu, aov, cur, rate, rk, cpa) in c["ch"]]
    ws = sum(x[0] for x in w)
    aov_w = sum(x[0] * x[1] for x in w if not x[3]) / sum(x[0] for x in w if not x[3])
    comm_nom = sum(x[0] * (x[3] * FX["USD"] if x[3] else x[1] * x[2]) for x in w) / ws
    rate_w = sum(x[0] * x[1] * x[2] for x in w if not x[3]) / sum(x[0] * x[1] for x in w if not x[3])
    out["struct"] = {"aov": aov_w, "rate": rate_w, "comm_nom": comm_nom,
                     "comm_eff_base": out["Base"]["rev"] / out["Base"]["orders"]}
    return out


def views(rev, profit):
    return (profit + COST) / rev * 1e6


def fit(c, r):
    s = r["Strong"]["rev"]
    structural = c["nr"] in (1, 4, 19)  # kein Produktbezug / minderjährige Zielgruppe / 0 %-Gift-Cards
    if structural or s < 100 or (c["intent"] <= 2 and s < 120):
        return "LOW"
    if c["intent"] >= 4 and s >= 250:
        return "HIGH"
    return "MEDIUM"


def de(x, d=0):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


rows, js = [], []
for c in CL:
    r = compute(c)
    st = r["struct"]
    f = fit(c, r)
    rb, rs = r["Base"]["rev"], r["Strong"]["rev"]
    js.append({"nr": c["nr"], "cluster": c["name"], "market": c["market"], "intent": c["intent"], "geo": c["geo"],
               "fit": f, "rev_base": rb, "rev_strong": rs, "aov": st["aov"], "rate": st["rate"],
               "comm_nom": st["comm_nom"], "comm_eff_base": st["comm_eff_base"],
               "cvr_base": r["Base"]["cvr"], "cvr_strong": r["Strong"]["cvr"],
               "ret_base": r["Base"]["ret_w"], "ret_strong": r["Strong"]["ret_w"],
               "clicks_base": r["Base"]["clicks"], "clicks_strong": r["Strong"]["clicks"],
               "orders_base": r["Base"]["orders"], "orders_strong": r["Strong"]["orders"],
               "v5_strong": views(rs, 5000), "v10_strong": views(rs, 10000), "v10_base": views(rb, 10000),
               "channels": [(n, sh, ck, mu, aov, cur, rate, rk, cpa) for (n, sh, ck, mu, aov, cur, rate, rk, cpa) in c["ch"]]})
    rows.append([
        f"{c['nr']:02d} {c['name']}", "EN/US" if c["market"] == "EN" else "DE", c["produkte"], c["programme"],
        de(st["rate"] * 100, 1), c["cookie"], de(st["aov"], 0), de(st["comm_nom"], 2),
        f"Base {de(r['Base']['cvr']*100, 2)} % / Strong {de(r['Strong']['cvr']*100, 2)} % (Klick->Bestellung, gemischt; E M3)",
        f"Base {de(r['Base']['ret_w']*100, 0)} % / Strong {de(r['Strong']['ret_w']*100, 0)} % (provisionsgewichtet; E M5)",
        INTENT_LABEL[c["intent"]], c["intent"], f, round(rb), round(rs),
        round(views(rs, 5000)), round(views(rs, 10000)),
        c["dq"], c["quellen"],
        f"Provision/Sale effektiv (nach USt & Retouren, Base) {de(st['comm_eff_base'], 2)} €; Geo {c['geo']} "
        f"{GEO[c['geo']][0]:.2f}/{GEO[c['geo']][1]:.2f}; " + c["note"],
    ])

HEAD = ["nische_cluster", "markt", "produkte", "hauptprogramme", "provision_pct", "cookie", "aov_eur",
        "provision_pro_sale_eur", "cvr_benchmark", "retourenquote", "purchase_intent", "intent_1_5", "affiliate_fit",
        "umsatz_pro_1m_views_base_eur", "umsatz_pro_1m_views_strong_eur", "views_fuer_5k_strong", "views_fuer_10k_strong",
        "datenqualitaet", "quellen", "notizen"]
with open(os.path.join(HERE, "raw_affiliate_economics_clusters.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(HEAD)
    w.writerows(rows)
with open(os.path.join(HERE, "r2_model_output.json"), "w", encoding="utf-8") as fh:
    json.dump(js, fh, ensure_ascii=False, indent=1)

for x in sorted(js, key=lambda x: -x["rev_strong"]):
    print(f"{x['nr']:>2} {x['market']} {x['fit']:<6} I{x['intent']} base {x['rev_base']:7.1f}  strong {x['rev_strong']:7.1f}  "
          f"AOV {x['aov']:6.1f} rate {x['rate']*100:4.1f}% nom {x['comm_nom']:5.2f} eff {x['comm_eff_base']:5.2f} "
          f"v10S {x['v10_strong']/1e6:7.1f}M  {x['cluster'][:40]}")
