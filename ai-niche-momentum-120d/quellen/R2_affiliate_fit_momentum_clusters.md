# R2 – Affiliate-Fit der KI-Short-Form-Momentum-Cluster

**Stand:** 26.09.2026 · **Rohdaten:** [`raw_affiliate_economics_clusters.csv`](raw_affiliate_economics_clusters.csv) (38 Zeilen = 19 Cluster × EN/US + DE) · **Rechenmodell:** [`r2_affiliate_model.py`](r2_affiliate_model.py) (`python3 r2_affiliate_model.py`, schreibt CSV und `r2_model_output.json`)
**Wiederverwendet:** `affiliate-theme-page-research/03_affiliate_programs.csv` (P-IDs), `quellen/E_funnel_benchmarks.md` (M2–M5), `10_affiliate_funnel_models.md` und `scripts/model.py` (Formel und Parameter)
**Rahmen:** Theme Page → organische Views → Affiliate-Produkte → Provision. Nicht eingerechnet sind Sponsoring, eigene Produkte, Kurse und B2B.

> **Kernbefund:** Keiner der 19 Momentum-Cluster erreicht **Affiliate-Fit HIGH**. Die Cluster mit dem stärksten Momentum (KI-Story-Serien, Fußball-Sketche, Marvel-What-if, Kids-Figuren, Surreal) liegen bei **21–77 € pro 1 Mio. Views**, und das schon im Strong-Szenario. Für 10.000 € Monatsgewinn bräuchten sie **137–499 Mio. Views pro Monat**.
> Brauchbar (**MEDIUM**) sind nur die „Handwerk-/Küche-/Pflege“-Cluster mit echtem Produktbezug: **DIY/Cabin DE 266 €**, **Fashion DE 218 €**, **DIY EN 189 €**, **Kochen DE 177 €**, **Restoration DE 156 €** pro 1 Mio. Views (Strong). Das entspricht 40–85 Mio. Views pro Monat für 10.000 € Gewinn. Damit liegen diese Cluster in derselben Größenordnung wie die Shopping-Nischen der Vorstudie, aber **unter** deren Top-Werten (Grill DE 544 €, BBQ US 497 € Strong), weil der Content unterhält und kein Produkt zeigt (Intent 3 statt 4–5).
> Momentum und Affiliate-Fit verlaufen **gegenläufig**: Die schnell wachsenden Cluster haben keinen Kaufanlass, und die kaufnahen Cluster (DIY, Restoration, Kochen) sind laut M5 auf YouTube gerade **verlangsamt**.

---

## 1. Methodik

### 1.1 Formel (unverändert aus 10_affiliate_funnel_models.md, Abschnitt 1)

```
Provision pro 1 Mio. Views = 1.000.000 × Klicks/1.000 Views × Intent-Faktor × Geo-Anteil
                             × Σ_Kanal [Klickanteil × CVR × AOV × Provision × Netto-Faktor] × (1 − Retouren)
Views für X € Gewinn = (X + 600 €) ÷ Provision pro 1 Mio. Views × 1 Mio.
```

**Kontrollrechnung:** Cluster 14 EN (KI-Interior) ist mit dem Kanalmix von K29 aus der Vorstudie gerechnet. Er reproduziert K29 exakt (Base 19 € / Strong 111 €). Fashion DE, Garten DE und die Gadget-Cluster unterscheiden sich von K20/K26/K14/K15 nur durch den Intent-Faktor.

**Zwei Erweiterungen, beide als MODEL ASSUMPTION markiert:**
1. **Retouren je Kanal** statt je Nische. In einem Cluster stehen z. B. Bücher (≈ 5 %) neben Trikots (25–45 %), deshalb wird je Kanal abgezogen. In der CSV steht die provisionsgewichtete Quote.
2. **Fixprovisionen (CPA)** wie die Audible-Trial-Bounty von 5 $ gehen als Festbetrag ein, also ohne AOV × Rate und ohne Netto-Faktor.

### 1.2 Parameter

| Baustein | Base | Strong | Herkunft | Qualität |
|---|---|---|---|---|
| Link-Klicks / 1.000 Views | 1,2 | 3,0 | E M2, model.py | MODEL ASSUMPTION |
| Intent-Faktor | 1→0,3 · 2→0,5 · 3→0,75 · 4→1,0 · 5→1,2 | | model.py | MODEL ASSUMPTION |
| Geo EN / DE | 0,55 / 0,80 | 0,62 / 0,85 | E/F, model.py | THIRD-PARTY → ASSUMPTION |
| Geo **EN_YOUNG** (Cluster 1, 2, 3, 4, 12, 19 EN) | 0,45 | 0,55 | model.py K03 (Gaming: jüngeres, globaleres Publikum) | MODEL ASSUMPTION |
| CVR Amazon.com / Amazon.de | 4 % / 3 % | 7 % / 5 % | E M3 (Geniuslink) | VERIFIED → ASSUMPTION |
| CVR Home / Elektronik+Sport / Fashion / Pets / Travel / High-Ticket | 0,7 / 0,9 / 1,0 / 1,8 / 0,5 / 0,05 % | 1,5 / 1,8 / 2,0 / 3,0 / 1,0 / 0,12 % | E M3, model.py | VERIFIED → ASSUMPTION |
| **CVR „Retail“ NEU** (Bücher-, Spielwaren-, Key-, Collectible-Händler) | 0,9 % | 1,8 % | kein Kategorie-Benchmark in E → analog Elektronik/Sport | MODEL ASSUMPTION |
| Retouren Fashion US/DE · Elektronik · Home · Pets · Sport | 25/45 · 10/14 · 10/12 · 5/6 · 12/20 % | 20/35 · 8/10 · 7/9 · 3/4 · 9/14 % | E M5 | VERIFIED → ASSUMPTION |
| **Retouren NEU:** Bücher · Spielzeug · digitale Keys · Reise · CPA-Trials | 5/6 · 10/12 · 3 · 25 · 5 % | 3/4 · 7/9 · 2 · 20 · 3 % | analog Consumables/Home (E M5); Reise aus model.py | MODEL ASSUMPTION |
| Netto-Faktor | DE 1/1,19 · EN 0,97 | | model.py | ASSUMPTION |
| FX | 1 USD = 0,86 € | | model.py | ASSUMPTION |
| Kosten | 600 €/Monat | | model.py / H | ASSUMPTION |
| Amazon-Warenkorb (inkl. Halo) | 35 USD/EUR Standard; Küche 45, Werkzeug 55, Konsolen 60 | | E M4 (Amazon-AOV UNKNOWN) | ESTIMATED |

**Provisionssätze:** Es werden keine „bis zu“-Werte verwendet. Chemical Guys „bis 10 %“ → 7 %, Nike „bis 15 %“ → 5 %, Fanatics „5–10 %“ → 5 %, Petromax „4–12 %“ → 8 % (Mitte der Spanne).

### 1.3 Intent-Rubrik (Content-Kontext, nicht Produktkategorie)

| Intent | Label | Bedeutung für KI-Content |
|---|---|---|
| 1 | ENTERTAINMENT | Story/Effekt ohne Produktbezug; Publikum oft minderjährig |
| 2 | ASPIRATION / ENTERTAINMENT | Thema hat reale Produkte, der Content zeigt sie aber nicht als Kaufobjekt |
| 3 | PRODUCT DESIRE (indirekt) | Werkzeug, Kochgeschirr oder Outfit ist sichtbarer Teil der Szene |
| 4 | PRODUCT DESIRE | Produkt steht im Mittelpunkt (Finds/Setup-Formate der Vorstudie) |
| 5 | DIRECT BUYING INTENT | „Amazon Finds“, Deal-Formate |

### 1.4 Fit-Regel

| Fit | Regel |
|---|---|
| **HIGH** | Intent ≥ 4 **und** Strong ≥ 250 €/1 Mio. |
| **LOW** | Strong < 100 €, **oder** Intent ≤ 2 und Strong < 120 €, **oder** struktureller Blocker. Blocker sind: kein Produkt (Cluster 4), minderjähriges Publikum und 0-%-Gift-Cards (Cluster 1, 19) |
| **MEDIUM** | alles andere |

---

## 2. Ranking nach Umsatz pro 1 Mio. Views (Strong)

| Rang | # | Cluster | Markt | Intent | Fit | €/1 Mio. Base | €/1 Mio. Strong | Views/Monat für 5k Gewinn (Strong) | für 10k (Strong) | für 10k (Base) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | KI-DIY/Hausbau/Cabin/Tiny House/Handwerk | DE | 3 | **MEDIUM** | 49 | 266 | 21,0 Mio. | 39,8 Mio. | 217 Mio. |
| 2 | 15 | KI-Fashion/AI-Personas | DE | 3 | **MEDIUM** | 36 | 218 | 25,7 Mio. | 48,7 Mio. | 294 Mio. |
| 3 | 6 | KI-DIY/Hausbau/Cabin/Tiny House/Handwerk | EN/US | 3 | **MEDIUM** | 32 | 189 | 29,6 Mio. | 56,0 Mio. | 330 Mio. |
| 4 | 10 | KI-Kochen/Village-Food/Cozy Cooking | DE | 3 | **MEDIUM** | 34 | 177 | 31,7 Mio. | 59,9 Mio. | 308 Mio. |
| 5 | 7 | KI-Restoration/Satisfying/ASMR | DE | 3 | **MEDIUM** | 31 | 156 | 35,8 Mio. | 67,8 Mio. | 341 Mio. |
| 6 | 10 | KI-Kochen/Village-Food/Cozy Cooking | EN/US | 3 | **MEDIUM** | 29 | 156 | 36,0 Mio. | 68,1 Mio. | 368 Mio. |
| 7 | 7 | KI-Restoration/Satisfying/ASMR | EN/US | 3 | **MEDIUM** | 23 | 124 | 45,1 Mio. | 85,4 Mio. | 456 Mio. |
| 8 | 13 | KI-Autos/Luxus | DE | 2 | **LOW** | 22 | 112 | 50,0 Mio. | 94,6 Mio. | 487 Mio. |
| 9 | 14 | KI-Interior/Architektur/Dream Rooms | EN/US | 2 | **LOW** | 19 | 111 | 50,5 Mio. | 95,6 Mio. | 554 Mio. |
| 10 | 17 | KI-Garten/Obst/Pflanzen | DE | 2 | **LOW** | 21 | 110 | 51,1 Mio. | 96,6 Mio. | 516 Mio. |
| 11 | 18 | KI-Produkte/Gadget-Konzepte | EN/US | 3 | **MEDIUM** | 21 | 107 | 52,5 Mio. | 99,3 Mio. | 508 Mio. |
| 12 | 15 | KI-Fashion/AI-Personas | EN/US | 3 | **MEDIUM** | 18 | 103 | 54,3 Mio. | 102,8 Mio. | 584 Mio. |
| 13 | 5 | KI-Tiere & Tierrettung/Wholesome | EN/US | 2 | **LOW** | 19 | 94 | 59,8 Mio. | 113,3 Mio. | 554 Mio. |
| 14 | 5 | KI-Tiere & Tierrettung/Wholesome | DE | 2 | **LOW** | 21 | 93 | 59,9 Mio. | 113,4 Mio. | 513 Mio. |
| 15 | 14 | KI-Interior/Architektur/Dream Rooms | DE | 2 | **LOW** | 17 | 89 | 62,9 Mio. | 119,0 Mio. | 610 Mio. |
| 16 | 8 | KI-Geschichte/POV/Zeitreise | EN/US | 2 | **LOW** | 16 | 82 | 68,1 Mio. | 128,8 Mio. | 662 Mio. |
| 17 | 18 | KI-Produkte/Gadget-Konzepte | DE | 3 | **LOW** | 17 | 81 | 69,0 Mio. | 130,7 Mio. | 622 Mio. |
| 18 | 2 | KI-Fußball-/Promi-Sketche | DE | 2 | **LOW** | 14 | 77 | 72,6 Mio. | 137,3 Mio. | 736 Mio. |
| 19 | 9 | KI-Babys/Familie | EN/US | 2 | **LOW** | 14 | 76 | 73,6 Mio. | 139,3 Mio. | 784 Mio. |
| 20 | 13 | KI-Autos/Luxus | EN/US | 2 | **LOW** | 14 | 76 | 74,2 Mio. | 140,4 Mio. | 731 Mio. |
| 21 | 11 | KI-Reise-Traumorte/Nature | DE | 2 | **LOW** | 13 | 73 | 76,4 Mio. | 144,7 Mio. | 792 Mio. |
| 22 | 8 | KI-Geschichte/POV/Zeitreise | DE | 2 | **LOW** | 13 | 65 | 85,7 Mio. | 162,3 Mio. | 787 Mio. |
| 23 | 11 | KI-Reise-Traumorte/Nature | EN/US | 2 | **LOW** | 11 | 64 | 87,7 Mio. | 165,9 Mio. | 959 Mio. |
| 24 | 2 | KI-Fußball-/Promi-Sketche | EN/US | 2 | **LOW** | 10 | 59 | 94,2 Mio. | 178,2 Mio. | 1.091 Mio. |
| 25 | 9 | KI-Babys/Familie | DE | 2 | **LOW** | 12 | 59 | 95,5 Mio. | 180,9 Mio. | 916 Mio. |
| 26 | 16 | KI-Nostalgie (80er/90er, BRD/DDR) | EN/US | 2 | **LOW** | 11 | 58 | 97,0 Mio. | 183,6 Mio. | 953 Mio. |
| 27 | 12 | KI-Horror/Mystery | DE | 2 | **LOW** | 11 | 55 | 102,7 Mio. | 194,4 Mio. | 931 Mio. |
| 28 | 17 | KI-Garten/Obst/Pflanzen | EN/US | 2 | **LOW** | 9 | 53 | 105,6 Mio. | 199,9 Mio. | 1.121 Mio. |
| 29 | 16 | KI-Nostalgie (80er/90er, BRD/DDR) | DE | 2 | **LOW** | 11 | 52 | 108,1 Mio. | 204,6 Mio. | 992 Mio. |
| 30 | 3 | Film/Anime/Marvel What-if-3D | DE | 2 | **LOW** | 10 | 49 | 114,9 Mio. | 217,6 Mio. | 1.067 Mio. |
| 31 | 19 | Kids/Game-Figuren | DE | 2 | **LOW** | 10 | 48 | 116,9 Mio. | 221,3 Mio. | 1.077 Mio. |
| 32 | 12 | KI-Horror/Mystery | EN/US | 2 | **LOW** | 7 | 41 | 135,9 Mio. | 257,2 Mio. | 1.457 Mio. |
| 33 | 19 | Kids/Game-Figuren | EN/US | 2 | **LOW** | 7 | 40 | 140,4 Mio. | 265,7 Mio. | 1.490 Mio. |
| 34 | 3 | Film/Anime/Marvel What-if-3D | EN/US | 2 | **LOW** | 7 | 40 | 140,7 Mio. | 266,3 Mio. | 1.527 Mio. |
| 35 | 1 | KI-Story-Serien (Roblox/3D, Moral) | DE | 1 | **LOW** | 7 | 35 | 162,2 Mio. | 307,1 Mio. | 1.433 Mio. |
| 36 | 1 | KI-Story-Serien (Roblox/3D, Moral) | EN/US | 1 | **LOW** | 6 | 32 | 174,6 Mio. | 330,5 Mio. | 1.816 Mio. |
| 37 | 4 | KI-Surreal/VFX/What-if | EN/US | 1 | **LOW** | 4 | 23 | 245,6 Mio. | 464,8 Mio. | 2.541 Mio. |
| 38 | 4 | KI-Surreal/VFX/What-if | DE | 1 | **LOW** | 5 | 21 | 263,4 Mio. | 498,5 Mio. | 2.310 Mio. |

**Lesart:**
- Die **DE-Varianten** liegen fast immer vor EN. Das liegt am höheren Geo-Anteil (0,85 statt 0,62 bzw. 0,55) und an den höheren Content-Raten (Baumärkte 7–10 %, Thalia 11 %, Amazon.de Werkzeug/Auto 5 %), obwohl die Amazon.de-CVR niedriger ist und USt abgezogen wird. DE hat aber den kleineren Reichweitendeckel (Vorstudie: DE-Strong-Reichweite 4–7 Mio. Views/Monat).
- **Sensitivität Intent:** Der Umsatz skaliert linear mit dem Intent-Faktor. Wird aus einem Unterhaltungs-Cluster ein produktzentriertes Format (Intent 4), dann gilt: DIY DE 266 → 355 €, Kochen DE 177 → 236 €, Fußball DE 77 → 154 €, Story-Serien EN 32 → 107 €. Selbst dann erreicht nur DIY DE die HIGH-Schwelle, und das Format wäre kein Momentum-Format mehr.

---

## 3. Cluster im Einzelnen

Die Werte je Cluster stehen in der Reihenfolge EN/US | DE. AOV, Satz und Provision pro Sale sind nach Bestellanteilen (Base) gewichtet. „eff.“ bedeutet: nach USt und Retouren (Base).

### 1. KI-Story-Serien (Roblox/3D, Rettungs-/Moral-Storys) – **LOW** (strukturell)
- **Produktlogik:** Die Story hat keinen natürlichen Kaufanlass. Roblox-Gift-Cards bringen **0 %** (Amazon US Gift Cards 0 %, P-A036; Amazon.de Geschenkkarten 0 %, P-A060). Das **Roblox Creator Affiliate Program ist seit 24.07.2025 eingestellt** und durch Creator Rewards ersetzt, das nur On-Platform-Neukunden vergütet (VERIFIED, create.roblox.com/docs/affiliates). Spielzeug und Kinderbücher lassen sich nur künstlich an die Story hängen.
- **Programme:** Amazon Toys 3 %, Books 4,5 % | Amazon.de 3 %/5 %, Thalia 11 %/8 %.
- **Rechnung:** AOV 28 | 33 €, Satz 3,5 | 4,0 %, Provision/Sale 1,01 | 1,30 € (eff. 0,90 | 1,00 €), CVR Base 4,0 | 2,6 %, Retouren 8 | 9 % → **6/32 € | 7/35 €** pro 1 Mio. Views (Base/Strong).
- **Warum LOW:** Das Publikum ist überwiegend minderjährig und global. „Made for Kids“ auf YouTube schaltet Kommentare und Links ab, Amazon-Associates-Links an Kinder sind heikel (COPPA/JMStV). Das Cluster hat das höchste Momentum der Studie, aber den schwächsten Affiliate-Fit.

### 2. KI-Fußball-/Promi-Sketche – **LOW**
- **Produktlogik:** Spieler-Trikots, Fußballschuhe und Fan-Artikel sind echte Produkte, die in Transferphasen und bei Turnieren auch gekauft werden. Die Sketche verkaufen aber den Gag, nicht das Trikot (Intent 2).
- **Programme US:** Fanatics 5–10 % (Impact, **7 T Cookie**, THIRD-PARTY; im Modell 5 %), Nike „bis 15 %“ (CJ, 7 T, CLAIMED; im Modell 5 %), Amazon Sports 3 %/Apparel 4 %.
- **Programme DE:** **11teamsports 7 %, Top-Partner 10 %, Gutscheinportale 4 %, 30 T (Awin-Profil 22165, VERIFIED)**, Kitbag 3,8 % (THIRD-PARTY) bis 5 % (THIRD-PARTY), adidas DE 2 %, Unisport 3 T Cookie (Rate nicht öffentlich).
- **Rechnung:** AOV 52 | 59 €, Satz 4,3 | 5,0 %, Provision/Sale 2,27 | 2,92 € (eff. 1,75 | 1,67 €), Retouren (provisionsgewichtet) 20 | 32 % → **10/59 € | 14/77 €**.
- **Risiken:** KI-Sketche mit realen Spielern berühren Persönlichkeits- und Markenrecht (Haaland, Mbappé, Yamal). Nike/adidas/Fanatics können Publisher aus Brand-Safety-Gründen ablehnen. Das Publikum ist stark außerhalb der Tier-1-Märkte (EN_YOUNG-Geo). Größen führen zu Fashion-Retouren.

### 3. Film/Anime/Marvel What-if-3D – **LOW**
- **Produktlogik:** Funko Pop, Marvel-Legends-Figuren und Artbooks passen thematisch. Streaming-Affiliate ist nicht belastbar: Crunchyroll hat laut Netzwerk-Listings dynamische Raten, Disney+ hat keine Rate gefunden (UNKNOWN), daher nicht gerechnet.
- **Programme:** Amazon Toys 3 %, Funko 4 % (CJ, THIRD-PARTY), **Entertainment Earth bis 10 % Cash / 15 % Store Credit (SELF-REPORTED)**, eBay Collectibles 3 % (VERIFIED) | Amazon.de 3 %, Thalia Spielware 8 %/Buch 11 %.
- **Rechnung:** AOV 32 | 36 €, Provision/Sale 1,07 | 1,34 € → **7/40 € | 10/49 €**.
- **Warum LOW:** Die What-ifs nutzen Disney/Marvel-IP. Das birgt ein Takedown- und Markenrisiko, und Merch-Links verstärken es eher. Das Publikum ist jung und global.

### 4. KI-Surreal/VFX/What-if – **LOW** (strukturell)
- **Produktlogik:** Es gibt keine. Gerechnet ist nur eine theoretische Obergrenze mit generischen Amazon-Links (CVR × 0,7).
- **Rechnung:** **4/23 € | 5/21 €**. Das ist der niedrigste Wert der Studie.

### 5. KI-Tiere & Tierrettung/Wholesome – **LOW**
- **Produktlogik:** Wal-, Hai- und Wildtierrettung hat keinen Produktbezug. Nur Haustier-Content (Hund/Katze) ist verlinkbar. Tierschutz-Spenden bringen keine Provision.
- **Programme:** Amazon Pets 3 %, Chewy 1 %/4 % (15 T), PETLIBRO 8 %, Tuft + Paw 12 %, Litter-Robot 8 % | Amazon.de 3 %, Fressnapf 8 % Neukunde (60 T), ZooRoyal 3–12 %, wildfang 10–13 % (alle VERIFIED, 03).
- **Rechnung:** AOV 38 | 41 €, Provision/Sale 1,88 | 2,16 €, Retouren 5 | 6 % → **19/94 € | 21/93 €**.
- **Einordnung:** Die gleichen Programme bringen in der Vorstudie mit Produkt-Content (K23, Intent 4) 187 € Strong. Der Abstand ergibt sich allein aus dem Wholesome-Kontext. Wenn KI-Tiere Produkte „benutzen“, ist das irreführend (G).

### 6. KI-DIY/Hausbau/Cabin/Tiny House/Handwerk – **MEDIUM** (bestes Cluster)
- **Produktlogik:** Werkzeug, Akkugeräte und Baustoffe sind in jeder Szene sichtbar. Gartenhaus- und Cabin-Kits sind der High-Ticket-Hebel.
- **Programme US:** Amazon Tools/Home Improvement 3 %, VEVOR 4–5 % (30 T), **Jamaica Cottage Shop Cabin-Kits 5 % (Programmseite, VERIFIED; Cookie unbekannt)**, Home Depot/Lowe's nur 1 % mit 1 T Cookie (ungeeignet). Allwood: **kein Programm gefunden** (UNKNOWN). Weitere Tiny-House-Programme laut Suchergebnissen (SELF-REPORTED, nicht gerechnet): Craftsman Tiny Homes 8 %, Tiny Home Builders 20 % auf Pläne/Bücher, Texas Tiny Homes 35 % auf Baupläne.
- **Programme DE:** Amazon.de Baumarkt/Elektrowerkzeuge 5 %, hagebau Content 10 % (60 T), toom Content 8 %, BAUHAUS 7 %, OBI Content 7 %, **GartenHaus GmbH Standard 5 %, Top-Partner/Content 7 %, 30 T (Awin-Profil 22747, VERIFIED)**, Gartenhausfabrik 7 %.
- **Rechnung:** AOV 74 | 85 €, Satz 3,8 | 6,1 %, Provision/Sale 2,83 | 5,21 € (eff. 2,47 | 3,85 €), Retouren 10 | 12 % → **32/189 € | 49/266 €**. Das Gartenhaus-Kit (15 % der Klicks, High-Ticket-CVR × 2, AOV 2.000 €) bringt in DE etwa ein Viertel der Provision.
- **Hinweis:** KI-Bauvideos zeigen unrealistische Bauzeiten und Ergebnisse. Werkzeug-Links sind unkritisch, Kit-Versprechen („in 2 Tagen gebaut“) nicht. Laut M5 ist das Momentum verlangsamt (6 Millionen-Shorts in 30 T).

### 7. KI-Restoration/Satisfying/ASMR – **MEDIUM**
- **Produktlogik:** Polier- und Reinigungsmittel, Car-Detailing und Hochdruckreiniger passen zum Satisfying-Content. **Compliance:** Das KI-Ergebnis darf nicht als Produktwirkung dargestellt werden (G). Links nur als „Tools für echte Restaurationen“.
- **Programme US:** Amazon Automotive 4,5 %/Tools 3 %, Chemical Guys bis 10 % (CJ, Ø-Sale > 100 $; im Modell 7 %), **Kärcher UK bis 5 %, 30 T, CJ (Programmseite, VERIFIED)**.
- **Programme DE:** Amazon.de Auto/Baumarkt 5 %, **Kärcher AT 5 % auf Netto-Warenkorb, 30 T, Ø-Warenkorb 230 € (Awin-Profil 40254, VERIFIED/SELF-REPORTED)**. Ein Kärcher-DE-Programm wurde nicht gefunden; Kärcher CH hat 6 %. Dazu Autodoc 8 % und kfzteile24 6–8 %.
- **Rechnung:** AOV 40 | 50 €, Provision/Sale 1,84 | 2,64 € → **23/124 € | 31/156 €**.
- **Hinweis:** Autopflege-Marken wie Petzoldt's, Koch Chemie und Liquid Elephant haben kein auffindbares Programm (UNKNOWN).

### 8. KI-Geschichte/POV/Zeitreise – **LOW**
- **Produktlogik:** Geschichtsbücher, Hörbücher, Strategie- und Brettspiele sowie Museums- und Stadttouren sind logisch. Die Neugier-Views lösen aber kaum Kaufimpulse aus.
- **Programme US:** Amazon Books 4,5 %, **Bookshop.org 10 % (THIRD-PARTY)**, **Audible 5 $ pro Free-Trial / 10 $ Plus/Premium-Plus (THIRD-PARTY)**, GetYourGuide 8 % (CLAIMED), Viator 8 % (VERIFIED).
- **Programme DE:** Amazon.de Bücher 5 %, **Thalia: Buch 11 % (auch preisgebunden), mit Gutschein 8 %, Spielware/Sonstiges 8 %, 30 T, Awin exklusiv, Social Media ausdrücklich zugelassen (Programmseite + Awin-Profil 14158, VERIFIED)**, **Milan-Spiele 5 % (THIRD-PARTY)**, GetYourGuide 8 %.
- **Rechnung:** AOV 31 | 36 €, Provision/Sale 2,13 | 2,04 € → **16/82 € | 13/65 €**. Thalia hebt den Satz, aber Buch-AOVs sind klein.

### 9. KI-Babys/Familie – **LOW**
- **Programme:** Amazon Baby 3 %, Momcozy 10 %, CYBEX 6 %, Target 3 % | Amazon.de 3 %, babymarkt 5 %, baby-walz 6 % (10 T), Babybrands 2–7 % (alle aus 03).
- **Rechnung:** **14/76 € | 12/59 €**.
- **Warum LOW:** Die Comedy mit KI-Kleinkindern schafft keinen Kaufanlass, und die **Compliance ist HIGH** (Eltern-Vertrauen, Sicherheitsclaims; 17_compliance.md).

### 10. KI-Kochen/Village-Food/Cozy Cooking – **MEDIUM**
- **Produktlogik:** Gusseisen, Dutch Oven, Feuertopf und Messer sind in der Szene sichtbar und kaufbar.
- **Programme US:** Amazon Kitchen 4,5 %. **Lodge hat kein eigenes Affiliate-Programm** (nicht auffindbar; Verkauf über Amazon). Zwilling/Staub US 6 % (CJ, THIRD-PARTY), Le Creuset US 4 % (THIRD-PARTY).
- **Programme DE:** Amazon.de Küche 5 %, Petromax 4–12 % (Adcell, 60 T, Ø-Warenkorb 96 €, VERIFIED), Zwilling/Staub 6,4–8 %, WMF 5 %.
- **Rechnung:** AOV 47 | 58 €, Provision/Sale 2,21 | 3,29 € → **29/156 € | 34/177 €**.
- **Hinweis:** Laut M5 ist das Momentum ONE-OFF (ein Kanal liefert 62 % der Hits).

### 11. KI-Reise-Traumorte/Nature – **LOW**
- **Programme:** GetYourGuide 8 % (31 T, CLAIMED), Viator 8 % (VERIFIED), Booking.com Anteil (THIRD-PARTY; im Modell ≈ 4 % des Buchungswerts, ESTIMATED), Amazon Gepäck 4 %.
- **Rechnung:** AOV 90 | 104 €, Provision/Sale 4,26 | 4,96 €, Retouren/Storno 22 | 24 % → **11/64 € | 13/73 €**. Grund ist die niedrige Buchungs-CVR (0,5–1,0 %).
- **Warum LOW:** „Places that don't feel real“ sind teils fiktiv. Ein Link ist nur bei realen Zielen zulässig. Die Provision fließt erst nach der Reise.

### 12. KI-Horror/Mystery – **LOW**
- **Produktlogik:** Horror-Bücher, Horror-Games und Horror-Brettspiele. **Steam hat kein Affiliate-Programm.** Alternativen:
  - **Green Man Gaming:** bis 5 %, 10 % auf Bundles, Impact + Influencer-Ambassador-Programm (Programmseite, SELF-REPORTED)
  - **Humble Bundle:** 4–10 %, Partner 15 % auf Bundles (THIRD-PARTY)
  - **Fanatical:** 2–5 % (THIRD-PARTY)
  - **Instant Gaming:** ~3–4 %, dynamisch, 24 h (THIRD-PARTY)
  - Miniature Market 5 % (7 T, VERIFIED) für Brettspiele
- **Rechnung:** AOV 30 | 32 €, Provision/Sale 1,37 | 1,72 € → **7/41 € | 11/55 €**. Grey-Market-Keyshops (G2A u. ä.) sind bewusst ausgeschlossen.

### 13. KI-Autos/Luxus – **LOW**
- **Produktlogik:** Die Luxusautos selbst sind nicht affiliate-fähig. Verlinkbar sind Zubehör, Car Care und Modellautos.
- **Programme:** Amazon Automotive 4,5 %/Toys 3 %, Chemical Guys 7 % (Modell) | Amazon.de Auto 5 %, **CK-Modelcars: Neukunde 7 %/4 % (hohe/niedrige Marge), Bestandskunde 6 %/3 %, 30 T, Ø-Warenkorb 160 € (Awin-Profil 115681, VERIFIED/SELF-REPORTED)**, Autodoc 8 %.
- **Rechnung:** **14/76 € | 22/112 €**. DE liegt knapp über der 100-€-Grenze, bleibt aber wegen Intent 2 LOW.

### 14. KI-Interior/Architektur/Dream Rooms – **LOW**
- EN entspricht K29 der Vorstudie (**19/111 €**). DE: Amazon.de Wohnen 5 %, Connox 8 %, Westwing 4,9–6 % (**17/89 €**). KI-Traumräume sind keine kaufbaren Produkte, daher CVR × 0,7 wie bei K29.

### 15. KI-Fashion/AI-Personas – **MEDIUM**
- **Programme:** Amazon Fashion 4 %, REVOLVE 5 %, Shopbop 4 % (THIRD-PARTY). Walmart Creator Fashion 20 % ist CLAIMED und wurde nicht gerechnet. | DE wie K20: Amazon.de Bekleidung 6 %, Breuninger 12 %, Lounge 12 %, OTTO bis 15 %.
- **Rechnung:** AOV 51 | 78 €, Satz 4,5 | 8,7 %, Provision/Sale 2,29 | 6,77 €, aber **eff. 1,67 | 3,13 €** wegen Retouren von 25 | 45 % → **18/103 € | 36/218 €**.
- **Einschränkung:** Die AI-Persona trägt oft nicht existierende Outfits. Verlinkt werden dürfen nur 1:1 reale Artikel (G). DE ist rechnerisch Platz 2, die Umsetzung aber aufwendig (Vorstudie: Passivität 1/5).

### 16. KI-Nostalgie (80er/90er, BRD/DDR) – **LOW**
- **Produktlogik:** Retro-Konsolen, Retro-Spielzeug, Vinyl, Bücher und Ostprodukte. Das Kernprodukt wird schlecht vergütet: **Konsolen bei Amazon nur 1 %** (US P-A031, DE P-A058).
- **Programme:** **HHV Vinyl bis 8 % netto, 30 T, Webgains, Social erlaubt (Programmseite, VERIFIED)**, Thalia 11 %/8 %, Retro-Shops 5–10 % (Retro vGames, GoRetrogame, RetroFam; SELF-REPORTED, Kleinhändler). **Programme für Nostalgie- und DDR-Süßwaren: keine gefunden (UNKNOWN).**
- **Rechnung:** AOV 38 | 43 €, Satz 2,8 | 3,0 % → **11/58 € | 11/52 €**.

### 17. KI-Garten/Obst/Pflanzen – **LOW**
- DE entspricht K26 (STIHL 8 %, Baldur 8 %/90 T, Plantura 10 %, hagebau 10 %), aber mit Intent 2 → **21/110 €**. EN: Amazon Garden 3 %, The Sill 10 %, Eden Brothers 10 % Creator-Kampagne → **9/53 €**.
- **Risiko:** KI-Fantasie-Obst wie „Regenbogenfrüchte“ steht in der Nähe von Saatgut-Betrug. Nur reale Sorten verlinken.

### 18. KI-Produkte/Gadget-Konzepte – **MEDIUM (EN) / LOW (DE)**
- Konzept-Gadgets existieren nicht, verlinkt werden nur ähnliche reale Produkte. Daher Intent 3 statt 5 wie in K14/K15. Rechnung: **21/107 € | 17/81 €**. Es besteht Irreführungsrisiko, wenn der Link „das Produkt“ suggeriert.

### 19. Kids/Game-Figuren (Poppy Playtime, Sonic, Minecraft, KPop Demon Hunters) – **LOW** (strukturell)
- **Programme:** Amazon Toys 3 %, Target 3 % (7 T), **Smyths Toys 5–10 %, 30 T (THIRD-PARTY, UK/IE)**, LEGO US UNKNOWN | Amazon.de 3 %, LEGO 3,57 % (Daisycon, THIRD-PARTY), Thalia Spielware 8 %. Gaming-Gift-Cards 0 %. myToys wurde nicht geprüft (Suchbudget).
- **Rechnung:** **7/40 € | 10/48 €**.
- **Warum LOW:** Die Zielgruppe ist minderjährig (Jugendschutz, „made for kids“), und Fan-Figuren sind fremde IP.

---

## 4. Neue Programmdaten (Recherche 26.09.2026, 20 WebSearch-Aufrufe)

| Programm | Markt | Provision | Cookie | AOV / Sonstiges | Label | Quelle |
|---|---|---|---|---|---|---|
| Thalia DE | DE/AT | Buch 11 % (auch preisgebunden), Buch mit Gutschein 8 %, Spielware/Nicht-Buch 8 % (mit Gutschein 4 %) | 30 T | Awin exklusiv; Social Media ausdrücklich zugelassen | **VERIFIED** | thalia.de/vorteile/partnerprogramm; ui.awin.com/merchant-profile/14158 |
| 11teamsports DE & AT | DE/AT | 7 %, Top-Partner bis 10 %, Gutscheinportale 4 % | 30 T | Google-/CSS-Werbung verboten | **VERIFIED** | ui.awin.com/merchant-profile/22165 |
| GartenHaus GmbH | DE | Standard 5 %, Top-Partner/Content 7 % | 30 T | „attraktive Warenkorbwerte“ ohne Zahl; Adware/Paid Content verboten | **VERIFIED** | ui.awin.com/merchant-profile/22747 |
| Kärcher AT | AT (DE-sprachig) | 5 % auf Netto-Warenkorb | 30 T | Ø-Warenkorb 230 € | **VERIFIED** (AOV SELF-REPORTED) | ui.awin.com/merchant-profile/40254 |
| Kärcher UK (Home & Garden) | UK | bis 5 % | 30 T | CJ; Produktfeed | **VERIFIED** („bis zu“) | karcher.com/gb/en/home-and-garden/join-the-karcher-affiliate-program |
| Kärcher CH | CH | 6 % | – | Awin | THIRD-PARTY | affiliate-marketing.de/partnerprogramme/kaercher.ch |
| CK-Modelcars DE | DE | Neukunde 7 %/4 %, Bestandskunde 6 %/3 % (Marge hoch/niedrig); Gutschein/Cashback 1,5–3,5 % | 30 T | Ø-Warenkorb 160 € | **VERIFIED** (AOV SELF-REPORTED) | ui.awin.com/merchant-profile/115681 |
| HHV (Vinyl/Streetwear) | DE/EU | bis 8 % netto | 30 T | Webgains; Retouren/Stornos provisionsfrei; Facebook/Social erlaubt | **VERIFIED** („bis zu“) | hhv.de/en-US/help/affiliate-partner-program |
| Jamaica Cottage Shop (Cabin-Kits) | US | 5 % | UNKNOWN | keine Rabattcodes ohne Freigabe | **VERIFIED** | jamaicacottageshop.com/affiliate-signup |
| Green Man Gaming | global | bis 5 %, Bundles 10 % | UNKNOWN | Impact (Business) + Influencer-Ambassador | SELF-REPORTED | greenmangaming.com/affiliates |
| Roblox Creator Affiliate | global | **eingestellt 24.07.2025**, ersetzt durch Creator Rewards; zuvor bis 50 % der Robux-Käufe von Neukunden (max. 100 $) | – | keine Gift-Card-Vergütung | **VERIFIED** | create.roblox.com/docs/affiliates |
| Fanatics (US/Global) | US | 5–10 % (Quellen widersprüchlich: 5 %, 8 %, bis 10 %) | 7 T | Impact | THIRD-PARTY | getlasso.co/affiliate/fanatics (Suchergebnis); affiliate-marketing.de (Impact, Stand 23.07.2025) |
| Kitbag (Fanatics Int.) | UK/EU | 3,8 % bzw. 5 % (Quellen widersprüchlich) | UNKNOWN | – | THIRD-PARTY | affiliate-marketing.de/partnerprogramme/kitbag.com; getlasso.co/affiliate/kitbag-uk |
| Unisport | DE/EU | nicht öffentlich | **3 T** | – | SELF-REPORTED (Cookie) | unisportstore.de (Suchergebnis) |
| Bookshop.org | US/UK | 10 % | UNKNOWN | – | THIRD-PARTY | getlasso.co/affiliate/bookshop; linkclicky.com |
| Audible (via Amazon Associates) | US/UK | 5 $ Free-Trial, 10 $ Plus/Premium-Plus, 0,50 $ Einzeltitel | – | – | THIRD-PARTY | bloggingtips.com/audible-affiliate-program; Amazon-Seite 404 |
| Humble Bundle | global | 4–10 %, Partner 15 % auf Bundles | UNKNOWN | – | THIRD-PARTY | affiliateroll.com; affiliateotter.com |
| Fanatical | global | 2–5 % | UNKNOWN | CJ (Web) / direkt (Streamer) | THIRD-PARTY | uppromote.com |
| Instant Gaming | EU | ~3–4 %, dynamisch | 24 h | – | THIRD-PARTY | instant-deals.com; linkmydeals.com |
| Entertainment Earth | US | bis 10 % Cash / 15 % Store Credit | UNKNOWN | Auszahlung ab 20 $ | SELF-REPORTED (Seite 403) | entertainmentearth.com/affiliate-program |
| Smyths Toys | UK/IE | 5–10 % | 30 T | – | THIRD-PARTY | flexoffers.com; affiversemedia.com |
| Milan-Spiele | DE | 5 % | UNKNOWN | 1.500+ Artikel | THIRD-PARTY | affiliate-marketing.de/partnerprogramme/milan-spiele.de |
| Retro vGames / GoRetrogame / RetroFam | US | 10 % | UNKNOWN | Kleinhändler | SELF-REPORTED | retrovgames.com/affiliates; goretrogame.com/affiliate-program; retrofam.com/pages/affiliates |
| Craftsman Tiny Homes / Texas Tiny Homes / Tiny Home Builders | US | 8 % / 35 % auf Pläne / 20 % auf Pläne & Bücher | UNKNOWN | nicht gerechnet | SELF-REPORTED (Suchergebnis) | craftsmantinyhomes.com/affiliates; texastinyhomes.com/affiliate-program; tinyhomebuilders.com/affiliates |
| Lodge Cast Iron | US | **kein Programm gefunden** | – | Verkauf über Amazon | UNKNOWN | lodge.knoji.com; viglink/sovrn-Listing |
| Allwood (Kit Cabins) | US | **kein Programm gefunden** | – | – | UNKNOWN | Suchergebnis ohne Treffer |
| Crunchyroll / Disney+ | global | dynamisch / nicht gefunden | 24 h (Crunchyroll, THIRD-PARTY) | nicht gerechnet | UNKNOWN | cuelinks.com; getlasso.co/affiliate/disney |

**Wiederverwendet aus 03_affiliate_programs.csv:** Amazon US/DE/UK-Kategoriesätze (P-A001–P-A083), Baumärkte (P-C075–P-C078), Petromax (P-C020), Gartenhausfabrik (P-C022), Chemical Guys (P-C100), Autodoc/kfzteile24 (P-C107/P-C109), Pets (P-C117–P-C136), Baby (P-C137–P-C156), Garten (P-C048–P-C067), Fashion (P-D119–P-D131), Travel (P-D024–P-D035), LEGO/Funko/eBay/Miniature Market (P-D146–P-D155), Nike/adidas (P-D073/P-D074), Zwilling/WMF/Le Creuset (P-B065–P-B071).

---

## 5. Datenlücken und Grenzen

1. **Keine eigenen CVR-Benchmarks** für Bücher-, Spielwaren-, Game-Key- und Collectible-Händler. Verwendet wird „Retail“ = Elektronik/Sport-Niveau (0,9/1,8 %), MODEL ASSUMPTION.
2. **Keine Retourendaten** für Bücher, Spielzeug und digitale Keys. Werte sind aus Consumables/Home abgeleitet.
3. **Geo-Anteil für junge und globale Publika** (Roblox, Fußball, Kids) ist aus dem Gaming-Wert der Vorstudie übernommen. Für die Cluster gibt es keine Publikums-Geografie-Daten. Die Minderjährigen-Quote ist über Intent 1–2 nur grob abgebildet.
4. **Fanatics/Kitbag/Nike/adidas-US:** Die Raten stammen nur aus Drittlisten und widersprechen sich. Die Programmseiten von fanatics.de und kitbag.com lieferten 403. Ein Kärcher-DE-Programm und ein Hugendubel-Programm wurden nicht gefunden bzw. nicht geprüft. myToys wurde nicht geprüft.
5. **AOV** ist für viele neue Programme ESTIMATED (Trikots 80–120, Touren 60–80, Vinyl 45, Gartenhaus-Kit 2.000 €, Cabin-Kit 8.000 $). Die Tiny-House-/Cabin-Kits laufen über den High-Ticket-CVR ohne Benchmark (0,05/0,12 %).
6. **Streaming-Affiliate** (Disney+, Crunchyroll, Netflix) ist nicht belastbar und wurde nicht gerechnet.
7. **Rechtliche Risiken** sind nicht quantifiziert: Persönlichkeitsrecht bei Fußball-Sketchen, Disney/Marvel-IP und Fan-Figuren, Jugendschutz bei Kids-Clustern. Sie können einen Cluster unabhängig von der Rechnung ausschließen.
8. **Klickraten** (1,2/3,0 pro 1.000 Views) stammen aus Shopping-Kontexten (E M2). Für reine Unterhaltungs-Pages gibt es keinen Benchmark, abgebildet wird das nur über den Intent-Faktor. Die Vorstudie zeigt als Realitätsanker ≈ 3 $/1 Mio. Views für eine Repost-Theme-Page (K). Die Base-Werte der LOW-Cluster (4–22 €) liegen in dieser Größenordnung.
