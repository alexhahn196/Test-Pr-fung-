# 01 – Marktanalyse: Ist die Nische attraktiv? (Teil 1)

**Stand:** 25.09.2026 · **Frage (Teil 1):** Lohnt sich Interior / Luxury Homes / (KI-)Architektur für einen neuen,
internationalen, englischsprachigen Instagram-Account mit überwiegend KI-generierten Reels, und in welchen Sub-Nischen?
Beantwortet werden die 10 Leitfragen des Auftrags (Teil 1.1–1.10). Es folgen eine Scoring-Matrix für 12 Sub-Nischen und
ein Urteil.

**Datenbasis:** 2.498 Reels von 239 öffentlichen Instagram-Topic-Seiten (`instagram.com/popular/<slug>/`, Abruf 25.09.2026).
Davon sind 2.393 visuell codiert und 2.397 mit Followerzahl versehen; sie stammen von 1.985 Accounts. Dazu kommen die
Wettbewerber-DB mit 111 Accounts (72 davon tief profiliert), 9 Recherche-Notizen mit Faktencheck und ein YouTube-Shorts-Proxy.
Die Kennzahlen stehen in [analysis_digest.md](data/processed/analysis_digest.md) und [stats/*.csv](data/processed/stats/).
Die Sub-Nischen-Kennzahlen dieses Kapitels sind eigene Auswertungen aus [04_reel_database.csv](04_reel_database.csv),
[topic_reels.csv](data/processed/topic_reels.csv) und [topics.csv](data/processed/stats/topics.csv). Mapping und Code
zum Nachrechnen stehen in Abschnitt 1 (M1).

**Status-Tags:** `VERIFIED` = öffentlich angezeigte Views/Follower (gerundet) bzw. Primärquelle · `ESTIMATED` = KI-gestützte
Codierung (Realismus, KI/real, Shoppability, Account-Typ) oder eigene Ableitung · `THIRD-PARTY ESTIMATE` = Angabe Dritter ·
`PROXY` = YouTube statt Instagram · `UNKNOWN` = nicht belegbar.
**Konfidenz:** `*` = n < 15, also geringe Konfidenz. Alle Zusammenhänge sind Korrelationen; wir formulieren sie als
Hypothesen, nicht als Ursachen.

---

## 0. Antwort in Kürze

| # | Leitfrage (Teil 1) | Kurzantwort | Kernbeleg |
|---|---|---|---|
| 1.1 | Audience-Größe | **Sehr groß, aber ungleich verteilt.** Die Oberthemen haben Hunderte Millionen Reels, KI-spezifische Themen nur 1–3 Mio. | „home-decor“ 901 Mio., „architecture“ 1 Mrd. ([q04](quellen/q04_interior_trends_demand.md)), „dream-home“ 151 Mio., „luxury-homes“ 128 Mio. Reels gegenüber „ai-interior-design“ 152K `VERIFIED` |
| 1.2 | Konkurrenz-Stärke | **Hoch.** Entscheidend ist aber, wie **verkrustet** eine Seite ist: Architektur ist offen, KI-Interior und Luxury Bedrooms sind fast geschlossen. | Anteil der Top-Reels jünger als 180 Tage: Architecture 57 %, Luxury Bedrooms 8 %, AI Interior Design 7 % |
| 1.3 | Anzahl großer Accounts | Viele, in jeder Sub-Nische. | Wettbewerber-DB (n=111): 26 × ≥1 Mio., 19 × 500K–1 Mio., 34 × 100–500K, 25 × <100K, 7 × UNKNOWN. Gesamtsample: 105 Accounts ≥1 Mio., davon 21 mehrheitlich KI |
| 1.4 | Schwierigkeit organischen Wachstums | **Schwer.** Die Accountgröße ist der stärkste gemessene Einzelfaktor (Korrelation). Kleine Accounts kommen nur mit Ausreißer-Reels auf Topic-Seiten. | Spearman ρ = 0,43 (Views ~ Follower); 10× Follower ≈ 2,9× Views; 1–5K-Accounts erzielen Ø 580–658 Views pro Reel ([q09](quellen/q09_reels_format_benchmarks.md)) |
| 1.5 | Übersättigte Unterkategorien | KI-Luxusräume (Schlafzimmer, Wohnzimmer, Küche) im „dreamy“-Look, KI-Interior-Topic-Seiten, KI-Cozy, Mansions | KI-Schlafzimmer adj 0,77 (n=110), KI-Wohnzimmer 0,69 (n=123), KI-Küche 0,67 (n=31); Dreamy-KI 0,70 (n=305) |
| 1.6 | Wachsende Unterkategorien | Architektur, Commerce-Decor, „dream-house“, Treehouse und Garten; der **KI-Anteil wächst insgesamt** (nach Postjahr, nicht in jeder Sub-Nische) | Neue Architektur-Reels adj 1,53 (n=34); KI-Anteil der Top-Reels 5 % (2023) → 33 % (2026) |
| 1.7 | AI-Eignung | **Hoch für ungebaute oder unmögliche Architektur, niedrig für realistische oder verträumte Räume** | KI fantasy/impossible 2,27× (n=53) vs. KI dreamy 0,70: Verhältnis 3,25×, p=0,001 |
| 1.8 | Kaufabsicht | Hoch bei Interior, Küchen und Wohnzimmern, fast null bei Architektur, Mansions und Dream Homes | Anteil Reels mit „high shoppability“: Interior Design 55 %, Architecture 2 %, Mansions 0 % `ESTIMATED` |
| 1.9 | Möbel-Affiliate-Eignung | **Schwach für einen KI-Account.** Taugt als Beimischung, nicht als Fundament. | Amazon Furniture/Home 3 % bei 24-h-Fenster; KI-Möbel existieren nicht, also nur „similar items“ ([q02](quellen/q02_furniture_affiliate_commerce.md)) |
| 1.10 | Sponsoren-Interesse | Am besten belegt sind **KI-Tool-Firmen**. Möbelmarken arbeiten affiliate-first, Makler und Hotels wollen Reales. | Higgsfield Earn bis 2.500 $ pro Video; Begeisterung für KI-Creator-Content 60 % → 26 % ([q03](quellen/q03_sponsors_brand_deals.md)) |

**Urteil (Details in Abschnitt 5):** Die Nische ist **attraktiv, aber nur unter Bedingungen.** Tragfähig ist sie als
**originäres KI-Architektur-Studio für „unmögliche“ Häuser und Räume**. In der Scoring-Matrix liegt dieser Querschnitt mit
31/45 vorn, Architecture folgt mit 28/45. **Nicht attraktiv** ist sie als KI-Theme-Page für Luxus-Schlafzimmer,
-Wohnzimmer oder -Küchen, für Mansions oder für KI-„Listings“. Diese Sub-Nischen scheitern am K.-o.-Kriterium
KI-Eignung ≤ 2 und haben zum Teil verkrustete Topic-Seiten.

---

## 1. Methodik für Teil 1 (bitte zuerst lesen)

### M1 – Wie wir Sub-Nischen messen

Jede Sub-Nische ist ein Bündel von Topic-Seiten. Pro Seite zeigt Instagram etwa 12 Top-Reels und die Zahl „X reels on
Instagram“, das Angebotslabel. Wir werten zwei Ebenen aus:

- **Seitenebene** ([topics.csv](data/processed/stats/topics.csv)): Median-Views der Top-Reels je Seite, p90, Maximum und
  Angebotslabel.
- **Reel-Ebene** (eindeutige Reels der Sub-Nische): Follower, Alter, KI/real, Realismus, Shoppability, adj_factor.

<details>
<summary><b>Mapping Topic-Seiten → Sub-Nischen (aufklappen)</b></summary>

| Sub-Nische | Topic-Slugs |
|---|---|
| Interior Design (allg.) | interior-design-ideas, interior-styling, furniture-design, home-decor, home-decor-ideas, room-makeover, amazon-home-finds, bedroom-design, bedroom-decor, living-room-design, living-room-decor, kitchen-design, kitchen-inspiration, modern-kitchen, modern-living-room, bathroom-design, walk-in-closet, home-library, home-office-design, home-theater, kids-room-design, outdoor-kitchen, rooftop-terrace (23) |
| Luxury Interiors (ohne Schlaf-/Wohnzimmer/Küche) | luxury-interior-design, luxury-interior, luxury-furniture, quiet-luxury, modern-luxury-house-interiors, luxury-room, luxury-bathroom-design, luxury-bathroom, quiet-luxury-bathroom, luxury-bathroom-interior-design-inspiration, luxury-closet, dream-closet, dreamy-walk-in-closet-designs-ideas, luxury-dining-room, dubai-luxury-interior-design-trends, luxury-apartment-interior-design-ideas-2026, luxury-home-theater-ideas, dark-luxury-interior (18) |
| Luxury Homes | luxury-house, luxury-homes, luxury-villa, luxury-real-estate, luxury-penthouse, penthouse-tour, luxury-house-tour, house-tour, modern-villa, modern-house, ultra-modern-luxury-house-design, luxury-modern-beautiful-house, luxury-apartment, jamesedition-luxury-homes, tropical-villa, mediterranean-villa (16) |
| Architecture | architecture, modern-architecture, architecture-design, architecture-photography, tropical-house-architecture-styles (5) |
| Future Architecture | futuristic-houses, futuristic-house, parametric-architecture, futuristic-interior, futuristic-home, future-home, futuristic-architecture, futuristic-architecture-designs-2026, future-houses-2050, future-house (10) |
| AI Architecture | ai-architecture, midjourney-architecture, ai-generated-architecture-designs, ai-generated-house, ai-house-design, ai-house, ai-render (7) |
| AI Interior Design | ai-interior-design, ai-interior-designer, ai-interior, ai-home-design, virtual-staging, ai-virtual-staging (6) |
| Dream Homes | dream-home, dream-house, dream-house-design (3) |
| Mansions | luxury-mansion, mansion-tour, beverly-hills-mansion, miami-mansion, luxury-real-estate-mansion-exterior (5) |
| Luxury Bedrooms | dream-bedrooms, dream-bedroom, dream-bedroom-decor-ideas, luxury-bedroom, luxury-bedroom-design, luxury-master-bedroom, luxury-master-bedroom-interior-design (7) |
| Luxury Living Rooms | luxury-living-room-design, luxury-living-room (2) |
| Luxury Kitchens | luxury-kitchen, luxury-kitchen-design, dream-kitchen, dream-kitchens (4) |
| *Querschnitt: Fantasy/Impossible* | keine Topic-Gruppe, sondern alle Reels mit Realismus-Code `fantasy_impossible` (n=62), verteilt über KI-, Future-Arch-, Unusual-Home- und weitere Seiten |

57 Reels liegen in mehr als einer Sub-Nische. Für den Signifikanztest in M2 wurden nur die 996 eindeutig zugeordneten
Reels verwendet.
</details>

<details>
<summary><b>Reproduktion (Python, aus dem Projektordner ausführen)</b></summary>

```python
import pandas as pd
r  = pd.read_csv("04_reel_database.csv", low_memory=False)
tr = pd.read_csv("data/processed/topic_reels.csv")          # topic x shortcode (Topic-Seiten-Slots)
tp = pd.read_csv("data/processed/stats/topics.csv")         # Kennzahlen je Topic-Seite
SUB = {"Architecture": ["architecture", "modern-architecture", "architecture-design",
                        "architecture-photography", "tropical-house-architecture-styles"]}  # usw., Mapping siehe oben
for name, topics in SUB.items():
    t    = tp[tp.topic.isin(topics)]
    rows = tr[tr.topic.isin(topics)].merge(r[["shortcode", "age_days", "adj_factor", "production"]], on="shortcode")
    d    = r[r.shortcode.isin(rows.shortcode)]                # eindeutige Reels der Sub-Nische
    rec  = rows[rows.age_days <= 180]
    print(name,
          "Median der Topic-Mediane:", t.median_views.median(),
          "| Frische:", round((rows.age_days <= 180).mean(), 3), "n=", len(rows),
          "| adj neuer Reels:", round(rec.adj_factor.median(), 2), "n=", len(rec),
          "| Median Follower:", d.followers.median(),
          "| KI-Anteil:", round((d.production == "ai_generated").sum() / d.production.notna().sum(), 3),
          "| KI adj:", round(d[d.production == "ai_generated"].adj_factor.median(), 2),
          "| Shoppability high:", round((d[d.production.notna()].shoppability == "high").mean(), 3))
# Ausgabe für Architecture: 285000 | 0.567 n=60 | 1.53 n=34 | 61000 | 0.418 | 0.98 | 0.018

# Tabelle D: Postingfrequenz (Obergrenze) und "neu & schnell" je Sub-Nische aus der Wettbewerber-DB
c = pd.read_csv("02_competitor_database.csv")
c["per_day"] = c.posting_freq_per_week_upper_bound / 7
c["new_fast"] = (pd.to_datetime(c.earliest_known_post) >= "2025-09-25") & (c.followers >= 100_000) \
                & (c.posting_freq_per_week_upper_bound <= 21)
for name, topics in SUB.items():
    s = c[c.topics.fillna("").str.split(";").apply(lambda t: bool(set(t) & set(topics)))]
    print(name, len(s), round(s.per_day.median(), 2), round((s.per_day.dropna() >= 3).mean(), 2), list(s[s.new_fast].handle))
# Ausgabe für Architecture: 9 3.77 0.56 ['elitebuildhq']
```
Die Frische wird wie in `scripts/analyze.py` je Topic-Slot berechnet und ist damit identisch mit
[freshness_by_group.csv](data/processed/stats/freshness_by_group.csv), wo die Gruppen übereinstimmen (z. B. Architecture,
Future Architecture).
</details>

### M2 – Vier Verzerrungen, die jede Zahl in diesem Kapitel betreffen

1. **Selektionsbias:** Topic-Seiten zeigen nur **Top-Reels**. Absolute Views sind daher nach oben verzerrt; der Median aller
   Reels im Datensatz liegt bei 233K, das p90 bei 3,9 Mio. Kleine Accounts, die dort auftauchen, sind Ausreißer: Accounts
   unter 10K Followern kommen auf einen Median-vpf von 9,3 (n=402, [seg_follower_bucket.csv](data/processed/stats/seg_follower_bucket.csv)).
   Ein typisches Reel eines neuen Accounts sieht ganz anders aus (Teil 1.4).
2. **Angebotslabels sind keine Nachfrage.** „X reels on Instagram“ zählt Reels, nicht Views oder Suchen. Wie Instagram
   zählt, ist undokumentiert ([q04](quellen/q04_interior_trends_demand.md), Abschnitt 2.8). Hashtag-Volumina aus
   seriösen Quellen: `UNKNOWN`.
3. **Alter und Akkumulation.** Ältere Reels hatten mehr Zeit, Views zu sammeln. Den Anteil junger Reels (≤ 180 Tage)
   nutzen wir deshalb als Maß dafür, **wie leicht neue Reels alte verdrängen**. Die Korrelation zwischen Views und Alter ist
   schwach (Spearman ρ = 0,049). Das Postjahr hängt aber signifikant mit adj zusammen (Kruskal p = 1,3·10⁻⁶): Ältere Reels,
   die noch auf Top-Seiten stehen, sind vermutlich überlebende Evergreen-Hits.
4. **adj_factor ist ein Innerhalb-Seite-Maß.** adj ist das Residuum einer Regression *innerhalb* jeder Topic-Seite. Ein
   Vergleich von Sub-Nischen **untereinander** über adj bleibt deshalb konstruktionsbedingt flach: Kruskal-Wallis über
   12 Sub-Nischen (996 eindeutig zugeordnete Reels, davon 952 mit adj) ergibt H = 1,03, p ≈ 1,0, für den topic_index
   p = 0,87. Der Digest zeigt dasselbe für die 16 Topic-Gruppen (p = 0,93 bzw. ≈ 1,0). **Konsequenz:** Sub-Nischen vergleichen wir über absolute Views, Angebot,
   Frische und Kontostruktur. adj nutzen wir nur für Vergleiche **innerhalb** derselben Seiten, etwa KI gegen real oder
   neue gegen alte Reels.

---

## 2. Datenüberblick je Sub-Nische

![Nachfrage vs. Angebot je Topic-Seite](charts/topics_demand_vs_supply.png)

*Lesehilfe:* Oben links stehen hohe Views bei wenigen konkurrierenden Reels. Kleine Angebotszahlen bedeuten meist enge
Suchphrasen, zum Beispiel „ai-interior-designer“ mit 700 Reels oder „futuristic-houses“ mit 650 Reels. Das sind Hinweise,
keine Marktgrößen.

### Tabelle A – Nachfrage und Angebot

| Sub-Nische | Topics | Reels (eindeutig) | Median der Topic-Mediane | Median p90 | Max | Angebot Σ „reels on Instagram“ (Topics mit Label) | Median-Angebot je Topic | Median vpf | Anteil vpf ≥ 5 |
|---|---|---|---|---|---|---|---|---|---|
| Interior Design (allg.) | 23 | 264 | 626K | 2,21 Mio. | 135 Mio. | 1,48 Mrd. (22/23) | 17 Mio. | 4,2 | 48 % |
| Luxury Interiors | 18 | 180 | 377K | 2,23 Mio. | 55,5 Mio. | 34,5 Mio. (9/18) | 1,0 Mio. | 2,2 | 35 % |
| Luxury Homes | 16 | 166 | 300K | 2,63 Mio. | 72,1 Mio. | 246,5 Mio. (12/16) | 2,2 Mio. | 2,4 | 38 % |
| Architecture | 5 | 59 | 285K | 1,48 Mio. | 55,2 Mio. | 195 Mio. (3/5); dazu „architecture“ 1 Mrd. laut [q04](quellen/q04_interior_trends_demand.md) | 36 Mio. | 15,7 | 64 % |
| Future Architecture | 10 | 103 | 232K | 1,50 Mio. | 13,0 Mio. | 10,6 Mio. (8/10) | 145K | 2,0 | 35 % |
| AI Architecture | 7 | 74 | 217K | 1,88 Mio. | 136 Mio. | 3,2 Mio. (5/7) | 87K | 2,0 | 32 % |
| AI Interior Design | 6 | 60 | 500K | 5,83 Mio. | 28,6 Mio. | 1,14 Mio. (5/6) | 66K | 1,7 | 37 % |
| Dream Homes | 3 | 34 | 862K | 3,36 Mio. | 13,5 Mio. | 169 Mio. (3/3) | 18 Mio. | 4,9 | 50 % |
| Mansions | 5 | 53 | 272K | 3,71 Mio. | 34,7 Mio. | 175K (3/5) | 32K | 0,75 | 12 % |
| Luxury Bedrooms | 7 | 65 | 348K | 4,42 Mio. | 55,5 Mio. | 3,2 Mio. (5/7) | 102K | 3,1 | 44 % |
| Luxury Living Rooms | 2 | 18 | 310K | 1,24 Mio. | 3,1 Mio. | 1,14 Mio. (2/2) | 572K | 1,7 | 12 % (n=16) |
| Luxury Kitchens | 4 | 39 | 522K | 2,58 Mio. | 8,2 Mio. | 12,8 Mio. (4/4) | 2,4 Mio. | 4,4 | 39 % |
| *Querschnitt Fantasy/Impossible* | – | 62 | Median der Reels: 317K | p90 der Reels: 6,05 Mio. | 97,2 Mio. | – | – | 4,1 | 48 % |

Views und Follower sind `VERIFIED` (gerundet). Die Angebotslabels sind `VERIFIED`, zählen aber Angebot, nicht Nachfrage.

### Tabelle B – Konkurrenz und Frische

| Sub-Nische | Frische: Anteil Top-Reels ≤ 180 Tage (n Slots) | adj neuer Reels (n) | Median-Follower auf den Seiten | Reels von Accounts < 10K | Reels < 100K | Reels ≥ 1 Mio. | Accounts ≥1 Mio. / 500K–1 Mio. / 100–500K / < 100K | Anteil Theme-Pages |
|---|---|---|---|---|---|---|---|---|
| Interior Design (allg.) | 39 % (276) | 1,12 (107) | 70K | 15 % | 54 % | 6 % | 16 / 19 / 71 / 127 | 11 % |
| Luxury Interiors | 27 % (216) | 1,03 (59) | 113K | 14 % | 47 % | 7 % | 6 / 15 / 53 / 78 | 16 % |
| Luxury Homes | 32 % (192) | 1,01 (61) | 115K | 8 % | 45 % | 10 % | 9 / 16 / 38 / 66 | 25 % |
| Architecture | **57 %** (60) | **1,53** (34) | 61K | **24 %** | 58 % | 7 % | 4 / 6 / 12 / 31 | 16 % |
| Future Architecture | 22 % (119) | 0,59 (26) | 78K | 15 % | 55 % | 10 % | 6 / 9 / 15 / 46 | 37 % |
| AI Architecture | 25 % (84) | 0,67 (21) | 150K | 14 % | 39 % | 12 % | 8 / 5 / 23 / 27 | 18 % |
| AI Interior Design | **7 %** (72) | 0,18 (5*) | 40K | 35 % | 68 % | 5 % | 3 / 4 / 10 / 41 | 10 % |
| Dream Homes | 39 % (36) | 2,28 (14*) | 116K | 15 % | 47 % | 12 % | 4 / 4 / 7 / 16 | 38 % |
| Mansions | 17 % (60) | 0,56 (10*) | **606K** | 2 % | 24 % | **31 %** | 7 / 9 / 10 / 12 | 27 % |
| Luxury Bedrooms | **8 %** (84) | 0,78 (7*) | 148K | 6 % | 44 % | 13 % | 5 / 8 / 16 / 22 | 38 % |
| Luxury Living Rooms | 17 % (24) | 0,68 (4*) | 316K | 19 % | 31 % | 12 % | 2 / 3 / 5 / 5 | 12 % |
| Luxury Kitchens | 35 % (48) | 0,81 (17) | 92K | 8 % | 55 % | 8 % | 3 / 2 / 11 / 18 | 16 % |
| *Querschnitt Fantasy/Impossible* | 42 % (62 Reels) | 1,87 (26) | 50K | 27 % | 53 % | 8 % | 4 / 6 / 13 / 30 | 15 % |

Zum Vergleich: Über den ganzen Datensatz sind 35 % der eindeutigen Reels jünger als 180 Tage.

### Tabelle C – KI-Anteil, KI-Performance und Commerce-Signale

| Sub-Nische | KI-Anteil der Top-Reels (n codiert) | KI-Anteil unter neuen Reels (Basis: codierte neue Slots) | adj KI-Reels (n) | adj reale Aufnahmen (n) | Anteil fantasy/impossible | „High shoppability“ (n) | Kommentare pro 10.000 Views (n) |
|---|---|---|---|---|---|---|---|
| Interior Design (allg.) | 17 % (250) | 28 % | 1,70 (42) | 0,89 (180) | 0 % | **55 %** (250) | 1,8 (212) |
| Luxury Interiors | 20 % (172) | 30 % | 1,01 (34) | 0,97 (90) | 0 % | 48 % (172) | 2,3 (141) |
| Luxury Homes | 22 % (162) | 18 % | 0,66 (35) | 1,15 (98) | 0 % | 9 % (162) | 3,6 (142) |
| Architecture | 42 % (55) | 44 % | 0,98 (23) | 0,91 (22) | 5 % | 2 % (55) | 2,2 (51) |
| Future Architecture | 70 % (102) | 69 % | 0,90 (69) | 2,62 (12*) | 13 % | 5 % (102) | 5,1 (77) |
| AI Architecture | 92 % (73) | 86 % | 0,97 (67) | – (1*) | **15 %** | 4 % (73) | **6,6** (64) |
| AI Interior Design | 63 % (60) | 60 %* | **0,53** (38) | 0,46 (11*) | 5 % | 37 % (60) | 5,7 (43) |
| Dream Homes | 44 % (34) | 21 %* | 0,69 (15) | 1,43 (15) | 0 % | 3 % (34) | 2,7 (29) |
| Mansions | 16 % (49) | 10 %* | 3,92 (8*) | 0,92 (38) | 0 % | 0 % (49) | 5,0 (47) |
| Luxury Bedrooms | 38 % (63) | 40 %* | 1,03 (24) | 0,71 (26) | 0 % | 44 % (63) | 2,1 (51) |
| Luxury Living Rooms | 33 % (15) | 75 %* | 0,28 (5*) | 0,83 (8*) | 0 % | 80 % (15) | 2,0 (14*) |
| Luxury Kitchens | 29 % (38) | 53 % | 1,18 (11*) | 1,44 (23) | 0 % | 55 % (38) | 3,2 (36) |
| *Querschnitt Fantasy/Impossible* | 85 % (62) | – | **2,27** (53) | – | 100 % | **0 %** (59 low, 3 medium) | 4,4 (50) |

Alle Codes (KI/real, Realismus, Shoppability) sind KI-gestützt und damit `ESTIMATED`. Die Reliabilität liegt bei κ = 0,95
für die Produktion, 1,0 für den Realismus und 0,63 für die Shoppability ([reliability.csv](data/processed/stats/reliability.csv)).
Keiner der KI-vs.-real-Unterschiede **innerhalb** einer Sub-Nische ist signifikant (Mann-Whitney, getestet bei n ≥ 5 je
Gruppe: p = 0,09–0,88; der kleinste Wert gilt für Mansions mit n=8 KI-Reels; AI Architecture hat nur 1 reales Reel).

### Tabelle D – Postingfrequenz und neue, schnell wachsende Accounts (Wettbewerber-DB)

Ein DB-Account zählt zu einer Sub-Nische, wenn mindestens eines seiner Reels auf einer ihrer Topic-Seiten stand (Feld
`topics` in [02_competitor_database.csv](02_competitor_database.csv); Mehrfachzählung möglich). Frequenz = Obergrenze
`posting_freq_per_week_upper_bound` ÷ 7 (`ESTIMATED`; kurze Beobachtungsfenster blähen sie auf, siehe
[05 §5.1](05_viral_patterns.md)). „Neu & schnell“ = ältestes gesehenes Reel ≥ 25.09.2025, ≥ 100K Follower, ≤ 21 Posts/Woche
(Definition und Grenzen in [03 §2.4 e](03_competitor_analysis.md); nur **Kandidaten**, `ESTIMATED`).

| Sub-Nische | DB-Accounts | Median Posts/Tag (Obergrenze) | Anteil ≥ 3 Posts/Tag | Neu & schnell (Kandidaten) |
|---|---|---|---|---|
| Interior Design (allg.) | 20 (18 mit Frequenz) | 1,76 | 39 % | 2: @watchthebuild, @olena_prykhodko_design |
| Luxury Interiors | 19 | 2,69 | 47 % | 1: @georgios_tataridis |
| Luxury Homes | 18 | 2,37 | 39 % | 0 |
| Architecture | 9* | 3,77 | 56 % | 1: @elitebuildhq |
| Future Architecture | 18 | 2,58 | 44 % | 1: @georgios_tataridis |
| AI Architecture | 15 | 1,70 | 20 % | 2: @elitebuildhq, @exploringdreamhomes |
| AI Interior Design | 4* | 2,83 | 50 % | 0 |
| Dream Homes | 7* | 2,47 | 14 % | 1: @exploringdreamhomes |
| Mansions | 8* | 2,14 | 38 % | 0 |
| Luxury Bedrooms | 18 | 2,24 | 28 % | 1: @georgios_tataridis |
| Luxury Living Rooms | 5* | 3,77 | 80 % | 0 |
| Luxury Kitchens | 6* | 9,72 | 67 % | 0 |
| *Querschnitt Fantasy/Impossible* (Accounts mit ≥ 1 Fantasy-Reel) | 12* | 2,23 | 33 % | 1: @luxquisit |
| *Alle DB-Accounts* | 111 (103 mit Frequenz) | 1,79 | 38 % | 11 |

**Lesart:** Die Wettbewerber posten in allen Sub-Nischen im Median rund 2–3 Mal pro Tag (Obergrenze). Einen Nischen-Unterschied
leiten wir daraus nicht ab: Die Gruppen sind klein (* = n < 15), die DB ist eine Auswahl prominenter Accounts, und der
Kitchen-Wert (9,72; n = 6) ist vermutlich ein Fenster-Artefakt. Neue, schnell wachsende Kandidaten gibt es in fast jeder
Sub-Nische höchstens 1–2; insgesamt posten 7 der 11 Kandidaten KI, meist Konzeptbauten oder Transformationen
([03 §2.4 e](03_competitor_analysis.md)).
Kommerzielle Angebote und Marken je Sub-Nische: Teil 1.8–1.10.

---

## 3. Die 10 Leitfragen

### Teil 1.1 – Audience-Größe

**Befund:** Die Oberthemen gehören zu den größten auf Instagram. Die KI-spezifischen Sub-Nischen sind dagegen um zwei bis
drei Größenordnungen kleiner.

| Größenklasse | Sub-Nischen | Größte Seiten (Angebotslabel, `VERIFIED`) | Median-Views der Top-Reels |
|---|---|---|---|
| **Sehr groß** (≥ 100 Mio. Reels) | Interior Design, Architecture, Luxury Homes, Dream Homes | home-decor 901 Mio., interior-styling 116 Mio., kitchen-design 102 Mio.; architecture 1 Mrd. ([q04](quellen/q04_interior_trends_demand.md)), architecture-photography 135 Mio.; luxury-homes 128 Mio., luxury-real-estate 85 Mio.; dream-home 151 Mio. | 626K / 285K / 300K / 862K (Median der Topic-Mediane) |
| **Mittel** (10–35 Mio.) | Luxury Interiors, Luxury Kitchens, Future Architecture | luxury-furniture 17 Mio., quiet-luxury 7 Mio., luxury-interior 6,4 Mio. („total“, [q04](quellen/q04_interior_trends_demand.md)); dream-kitchen 8 Mio.; future-house 6,9 Mio. | 377K / 522K / 232K |
| **Klein** (≤ 3,3 Mio.) | AI Architecture, AI Interior Design, Luxury Bedrooms, Luxury Living Rooms, Mansions | midjourney-architecture 1,7 Mio., ai-architecture 1,4 Mio.; virtual-staging 884K, ai-interior-design 152K; luxury-bedroom 1,8 Mio.; luxury-living-room 1,1 Mio.; mansion-tour 133K | 217K / 500K / 348K / 310K / 272K |

- Die Hauptseite `/popular/interior-design/` lieferte im Sweep keine Reels und zeigt laut [q04](quellen/q04_interior_trends_demand.md)
  keine Zahl. Ihre Größe ist `UNKNOWN`.
- **Größte beobachtete Accounts** (Auswahl; Follower gerundet, `VERIFIED` per Embed bzw. Wettbewerber-DB):
  beautifuldestinations 24 Mio., thetrillionairelife 13 Mio. (2 von 3 Reels KI-codiert; Future Architecture, Luxury Homes, Mansions), gautamsinghania99 12 Mio.,
  naturesms 10 Mio. (KI, Cozy/Unusual), architectanddesign 8,4 Mio., howthingsarebuilld 8 Mio. (KI), farahjmerhi 7,5 Mio.,
  siyad_abdali 4 Mio. (KI, Bedrooms/Dream Rooms). Laut Drittanbieter-Toplisten kommen archdigest mit 11,3 Mio. und
  art_dailydose mit 22,8 Mio. hinzu ([q05](quellen/q05_competitor_lists.md), `THIRD-PARTY ESTIMATE`).
- **Kontext Markt und Plattform** (`THIRD-PARTY ESTIMATE`, [q04](quellen/q04_interior_trends_demand.md)): Möbel-E-Commerce
  weltweit 280,84 Mrd. US$ (2026, Statista), Home Décor 126,84 Mrd. US$. Pinterest nennt als Eigenangabe 600 Mio. monatliche
  Nutzer. Diese Zahlen zeigen, dass Geld im Thema steckt. Sie sagen aber nichts über die Reel-Nachfrage.
- **Cross-Platform** (`PROXY`, [q08](quellen/q08_cross_platform_signals.md)): Auch auf YouTube Shorts gibt es große Nachfrage
  nach „Haus als Spektakel“. Beispiele: Bau Rausch mit 621K Abos und 386,9 Mio. Aufrufen, Home Graphix mit einem
  167-Mio.-Short. Die Nachfrage ist aber extrem hit-getrieben: Goodluck Psd hat Ø 1,21 Mio. Views pro Video bei einem
  Median von 910. Zukunftsarchitektur zeigt auf Shorts **kein eigenständiges Nachfragesignal**: Eine Suchstichprobe
  ergab 24 Shorts des letzten Monats mit 2–1.600 Views, die Neuabfrage im Faktencheck 25 Shorts mit 0–1.400 Views.

**Schlussfolgerung 1.1:** Die Audience ist groß genug. Das Nadelöhr ist nicht die Nachfrage, sondern die Verteilung
(Teil 1.2 und 1.4). Die „kleinen“ KI-Topic-Seiten sind kleine Suchphrasen, keine kleinen Zielgruppen: KI-Reels erreichen
Menschen auch über „dream-home“, „architecture“ oder „treehouse“.

### Teil 1.2 – Konkurrenz-Stärke

Wir messen Konkurrenz über vier Signale aus Tabelle B:

1. **Frische:** Wie viele Top-Slots gehören Reels aus den letzten 180 Tagen?
2. **Performance neuer Reels:** adj der jungen Reels.
3. **Kontogröße:** Median-Follower auf den Seiten und Anteil der Top-Reels von ≥1-Mio.-Accounts.
4. **Angebot:** Median-Label je Topic.

| Einstufung | Sub-Nischen | Warum |
|---|---|---|
| **Offen** (neue Reels verdrängen alte) | **Architecture** | 57 % frische Slots (Digest-Gruppe ebenfalls 57 %, [freshness_by_group.csv](data/processed/stats/freshness_by_group.csv)), neue Reels adj 1,53 (n=34), 24 % der Top-Reels von Accounts < 10K. Das Angebot ist allerdings riesig (Median 36 Mio.). |
| **Mittel** | Interior Design, Dream Homes, Luxury Homes, Luxury Kitchens, *Fantasy-Querschnitt* | 32–42 % frisch, neue Reels ≈ 0,8–1,1. Ausnahmen nach oben: Fantasy mit 1,87 (n=26) und Dream Homes mit 2,28 (n=14*). Bei Dream Homes ist „dream-house“ zu 83 % frisch, „dream-home“ nur zu 25 % (je n=12*). |
| **Verkrustet** (alte Hits blockieren die Seite) | AI Interior Design (7 %), Luxury Bedrooms (8 %), Mansions (17 %), Luxury Living Rooms (17 %), Future Architecture (22 %), AI Architecture (25 %), Luxury Interiors (27 %) | Bei dream-bedrooms, dream-bedroom, luxury-bedroom, luxury-bedroom-design, futuristic-houses, futuristic-home, ai-interior-design, ai-interior, virtual-staging und ai-house-design ist **keines** der ~12 Top-Reels jünger als 180 Tage. Das Median-Alter auf ai-interior-design beträgt 558 Tage. |
| **Größen-dominiert** | Mansions | 31 % der Top-Reels stammen von ≥1-Mio.-Accounts, Median-Follower 606K, nur 2 % von Accounts < 10K, vpf-Median 0,75. |

**Wichtiger Befund zur Qualität der Konkurrenz:** Die zahlreichste Konkurrenzform ist relativ zur Größe schwach.
Faceless-Theme-Pages erreichen adj 0,74 (n=503), KI-Creator 1,09 (n=276) und Lifestyle-Creator 1,24 (n=508). Der Kontrast
Theme-Page vs. KI-Creator beträgt 0,68× (95-%-KI 0,42–0,90, p < 0,001, [key_contrasts.csv](data/processed/stats/key_contrasts.csv)).
Auch Drittanbieter zeigen niedriges „Authentic Engagement“ großer Theme-Pages, etwa howthingsarebuilld mit 8,5 Mio. Followern
(laut HypeAuditor; Embed: 8 Mio.) und 1,6K bzw. westwingcom mit 8,7 Mio. und 781 ([q05](quellen/q05_competitor_lists.md), `THIRD-PARTY ESTIMATE`).

![adj nach Account-Typ](charts/adj_by_account_type.png)

**Schlussfolgerung 1.2:** Die Konkurrenz ist groß, aber **nicht gleich stark**. Offen sind Seiten mit hoher Frische
(Architektur). Gegen verkrustete Seiten (KI-Interior, Luxury Bedrooms) kämpft ein neuer Account gegen 1–2 Jahre alte
Mega-Hits. Die vielen Theme-Pages sind relativ zu ihrer Größe unterdurchschnittlich. Eine erkennbare Studio- oder
Creator-Identität ist deshalb der realistischste Wettbewerbsvorteil. Das ist eine Hypothese, kein Kausalbeweis.

### Teil 1.3 – Anzahl großer Accounts

**a) Wettbewerber-DB** ([02_competitor_database.csv](02_competitor_database.csv), n=111; Follower gerundet laut Embed,
`VERIFIED`; einmal `THIRD-PARTY`):

| Follower | Accounts | davon KI | davon real/3D | Modus unklar |
|---|---|---|---|---|
| ≥ 1 Mio. | **26** | 11 | 14 | 1 |
| 500K–1 Mio. | **19** | 6 | 9 | 4 |
| 100–500K | **34** | 14 | 15 | 5 |
| < 100K | **25** | 16 | 5 | 4 |
| UNKNOWN | 7 | – | – | – |

Die 26 Accounts ≥1 Mio. verteilen sich auf 7 Theme-Pages, 7 Lifestyle-Creator, 5 Medien, 4 KI-Creator, 2 Designstudios und
1 Immobilien-Account. KI/real ist `ESTIMATED`. Die DB ist eine **Auswahl** relevanter Accounts, keine Vollerhebung.

**b) Alle Accounts auf den Topic-Seiten** (1.985 Accounts, davon 1.913 mit Follower): **105** × ≥1 Mio. · **157** ×
500K–1 Mio. · **532** × 100–500K · 746 × 10–100K · 373 × < 10K · 72 UNKNOWN. Von den 105 Accounts ≥1 Mio. sind **21**
mehrheitlich KI-codiert (`ESTIMATED`).

**c) Toplisten und Recherche** ([q05](quellen/q05_competitor_lists.md), 354 Handles; Follower wie in hafi.pro, HypeAuditor oder
Embed angezeigt):

| q05-Gruppe | Handles | ≥ 1 Mio. | 500K–1 Mio. | 100–500K | < 100K | UNKNOWN |
|---|---|---|---|---|---|---|
| A Interior-Theme-Pages & -Creator | 121 | 40 | 15 | 64 | 2 | 0 |
| B Luxury Homes / Real Estate | 35 | 11 | 3 | 17 | 4 | 0 |
| C Architektur-/Designmedien | 39 | 11 | 8 | 19 | 1 | 0 |
| D AI-Architektur-Creator | 25 | 5 | 2 | 5 | 0 | 13 |
| E AI-Interior-Creator/-Pages | 25 | 5 | 1 | 4 | 4 | 11 |
| F Dream / Future Homes | 28 | 3 | 8 | 9 | 1 | 7 |
| G Luxury Lifestyle | 30 | 8 | 5 | 10 | 0 | 7 |
| H Kleine Accounts mit Extrem-Views | 51 | 0 | 0 | 2 | 49 | 0 |

Toplisten sind nach Größe bzw. Engagement sortiert. Große Accounts sind hier also systematisch überrepräsentiert.

**d) Je Sub-Nische:** siehe die Spalte „Accounts ≥1 Mio. / …“ in Tabelle B. Am dichtesten mit Großaccounts besetzt sind
Interior Design (16 × ≥1 Mio.), Luxury Homes (9), AI Architecture (8) und Mansions (7 bei nur 40 Accounts). Am dünnsten
sind Luxury Living Rooms (2) sowie AI Interior Design und Luxury Kitchens (je 3).

**Schlussfolgerung 1.3:** In jeder Sub-Nische gibt es Millionen-Accounts. Das ist aber kein Ausschlusskriterium. Relativ
zur Größe liegen ≥1-Mio.-Accounts bei adj 0,91 (n=127) und damit nicht über Accounts mit 10–100K (1,07, n=850). Ihr Vorteil
ist die absolute Reichweite, nicht die Effizienz.

### Teil 1.4 – Schwierigkeit organischen Wachstums

| Follower-Klasse | n Reels | Median-Views | topic_index | Anteil im Top-Quartil der Seite | Median vpf | Anteil vpf ≥ 5 | adj |
|---|---|---|---|---|---|---|---|
| < 10K | 402 | 20,5K | 0,40 | 15 % | 9,3 | 57 % | 0,89 |
| 10–100K | 850 | 187K | 0,82 | 28 % | 5,1 | 50 % | 1,07 |
| 100–500K | 674 | 320K | 1,13 | 37 % | 1,5 | 27 % | 0,86 |
| 500K–1 Mio. | 325 | 638K | 1,54 | 46 % | 0,84 | 17 % | 0,87 |
| ≥ 1 Mio. | 127 | 1,2 Mio. | 3,31 | 59 % | 0,27 | 9 % | 0,91 |

Quelle: [seg_follower_bucket.csv](data/processed/stats/seg_follower_bucket.csv), Views `VERIFIED`.

**Was die Daten sagen:**
- **Größe ist der stärkste gemessene Einzelfaktor (Korrelation, keine Kausalität belegt).** Views und Follower korrelieren
  mit Spearman ρ = 0,427 (n=2.378, [summary.json](data/processed/stats/summary.json)). Innerhalb derselben Topic-Seite
  steigen die Views mit Follower^0,468. Rechnerisch gehen 10× mehr Follower mit ≈ 2,9× mehr Views einher, eine Verdopplung
  mit ≈ +38 % (`ESTIMATED`, eigene Umrechnung der Steigung).
- **Kleine Accounts schaffen es trotzdem auf Topic-Seiten.** 402 Reels (≈17 %) stammen von Accounts < 10K. Diese Reels
  überschießen ihre Followerzahl massiv (57 % mit vpf ≥ 5). Das ist Selektionsbias: Wir sehen nur die Treffer.
- **Benchmarks für den Normalfall** (`VERIFIED` laut Anbieter, [q09](quellen/q09_reels_format_benchmarks.md)): Business-Accounts
  mit 1–5K Followern erzielen **Ø 580 (2025) bzw. 658 Views pro Reel (H1 2026)** bei einer Reach-Rate von 9,78 %. Das
  Follower-Wachstum dieser Stufe halbierte sich (38 % → 22 %, 2024 → 2025). Die Skip-Rate liegt bei 65,5 %, und das
  Interior-Design-Engagement ist mit 0,12 % pro Follower niedrig.
- **Plattformmechanik** ([q01](quellen/q01_instagram_platform_rules.md), `VERIFIED`): Seit April 2024 wird jeder *eligible*
  Inhalt zuerst einem kleinen Publikum gezeigt und dann nach Performance ausgeweitet, *"give all creators an equal chance"*.
  Eligible heißt: original, ohne sichtbares Wasserzeichen, regelkonform. Trial Reels gibt es laut Drittquelle erst ab
  ~1.000 Followern (`ESTIMATED`). Laut Socialinsider hängen Reels stärker an der bestehenden Audience als Shorts oder
  TikTok: Bei < 5K Followern erreichen Reels Ø 625 Views, Shorts 15.160, TikTok 350 ([q08](quellen/q08_cross_platform_signals.md)). Shorts-Zahlen
  sind deshalb **kein** Maßstab für Reels.
- **Decay nach Hits (Format-Müdigkeit, Indiz, keine Ursache):**

| Account / Kanal | Früherer Hit | Jüngere Reels bzw. Shorts | Quelle / Status |
|---|---|---|---|
| @cozyzen.ai (IG, KI-Cozy) | 4,1 Mio. (08/2024) | 27K und 18,3K (2026) | [q06](quellen/q06_ai_theme_page_case_studies.md), `ESTIMATED` (Projektdaten) |
| @kohlectcabins (IG, KI-Cabins) | 23,8 Mio. (07/2024) | 70,6K (01/2026) | [02_competitor_database.csv](02_competitor_database.csv), `ESTIMATED` |
| @siyad_abdali (IG, KI-Rooms) | 282 Mio. und 109 Mio. (2024) | 5,1 Mio. … 316K (01/2026) | [q06](quellen/q06_ai_theme_page_case_studies.md), `ESTIMATED` |
| @luxurydreamhub (IG, KI-Luxus) | 302.997 Likes (älterer Hit) | 2.315 bzw. 12.014 Likes | [q06](quellen/q06_ai_theme_page_case_studies.md), `ESTIMATED` |
| Kou Yang (YT, KI-Renovierung) | 30 Mio. | 48 neueste Shorts: Median 2.700, 0/48 ≥ 1 Mio. | [q08](quellen/q08_cross_platform_signals.md), `PROXY` |
| UnrealLife (YT, „Choose your dream bedroom“) | 22 Mio. | 48 neueste: Median 26.000 | [q08](quellen/q08_cross_platform_signals.md), `PROXY` |
| Dreamy Interior (YT) | 32 Mio. | 10 neueste: Median 81.500 | [q08](quellen/q08_cross_platform_signals.md), `PROXY` |
| Simple Vision / BuildFlow / Buildenza (YT) | ältere Hälfte: Median 24,0 / 4,4 / 7,75 Mio. | neuere Hälfte: 7.731 / 6.690 / 1.237 | [Digest](data/processed/analysis_digest.md), `PROXY`, altersverzerrt |
| **Gegenbeispiele:** Bau Rausch, Feels Like HOME (YT) | 127 Mio. / 59 Mio. | stabil: 25/48 bzw. 26/38 neueste ≥ 1 Mio. | [q08](quellen/q08_cross_platform_signals.md), `PROXY` |

  Die Kanäle mit **Story und Überraschung** laufen stabil (Bunker, Familie, Regen). Die **Template-Formate** verschleißen
  (48 × identischer Titel bei UnrealLife). Das ist eine Deutung von [q08](quellen/q08_cross_platform_signals.md), keine Ursache.
- **Positiver Einzelfall:** Tim Fu wuchs von „a few hundred“ auf über 100K Follower in weniger als 11 Monaten. Das ist eine
  Selbstauskunft, und er ist ein namentlich auftretender Architekt, keine anonyme Page. Übertragbar ist es daher nur
  begrenzt ([q06](quellen/q06_ai_theme_page_case_studies.md)).

**Schlussfolgerung 1.4:** Organisches Wachstum ist **schwer, aber nicht verschlossen**. Realistisch sind anfangs
Hunderte bis wenige Tausend Views pro Reel. Wachstum kommt über **seltene Ausreißer-Reels**, und jedes Format hat eine
Halbwertszeit. Daraus folgen zwei Anforderungen: ein Serien- und Novelty-System statt eines Einheits-Looks, und
Entscheidungsregeln, die schnell von schwachen Formaten weg rotieren ([15_kpi_framework.md](15_kpi_framework.md), Abschnitt 4).

### Teil 1.5 – Übersättigte Unterkategorien

Als „übersättigt“ gilt eine Kategorie, wenn mindestens zwei Signale zutreffen:
1. Die Seite ist verkrustet (Frische < 25 %).
2. Der KI-Anteil liegt bei ≥ 30 % **und** KI-Reels oder neue Reels performen unter Erwartung (< 0,8).
3. Der Stil bzw. das Format ist häufig und schwach.
4. Es gibt Decay-Evidenz.
5. Großaccounts dominieren (≥ 25 % der Top-Reels von ≥1-Mio.-Accounts).

| Unterkategorie | Signale | Zahlen | Einstufung |
|---|---|---|---|
| **KI-Luxus-Schlafzimmer** | 1, 2, 4 | Luxury Bedrooms 8 % frisch (n=84); dream-bedrooms 92 % KI (n=12*); KI-Schlafzimmer raumcodiert adj 0,77 (n=110); Decay bei siyad_abdali, Themenwechsel bei soothenests ([q06](quellen/q06_ai_theme_page_case_studies.md)) | übersättigt |
| **KI-Wohnzimmer** | 1, 2 | Luxury Living Rooms 17 % frisch (n=24); KI-Wohnzimmer adj 0,69 (n=123); Wohnzimmer gesamt 0,80 (n=355) | übersättigt |
| **KI-Luxusküchen** | – | KI-Küche adj 0,67 (n=31); die Luxury-Kitchens-Seiten selbst sind mittel frisch (35 %) und real dominiert (29 % KI) | nicht übersättigt im Sinne der Regel, aber für KI schwach |
| **„Dreamy“-KI-Look** (Stil-übergreifend) | 2, 3 | stylized_dreamy adj 0,70 (n=335); unter KI 0,70 (n=305); häufigster KI-Stil „modern luxury“ 0,79 (n=128); organic modern 0,57 (n=56), Scandinavian 0,28 (n=16) ([strategy_brief](data/processed/strategy_brief.md), Digest) | übersättigt (explorativ, Stil insgesamt n.s.) |
| **AI Interior Design (Topic-Seiten)** | 1, 2 | 7 % frisch; KI-Reels 0,53 (n=38); neue Reels 0,18 (n=5*); Suchinteresse „AI interior design“ und „Interior AI“ laut Exploding Topics auf **„Peaked“**, „virtual staging“ −24 % ([q04](quellen/q04_interior_trends_demand.md), `THIRD-PARTY ESTIMATE`) | übersättigt / verkrustet |
| **Future-Architecture-Topic-Seiten** | 1, 2 | 22 % frisch; neue Reels 0,59 (n=26), davon 69 % KI; KI-Reels insgesamt 0,90 (n=69) | verkrustet, KI-lastig |
| **KI-Cozy / Rain-Ambience** | 2, 4 | cozy_ambience 44 % frisch, aber 67 % der neuen Reels KI; KI-Cozy adj 0,68 (n=44) gegenüber real 1,82 (n=36); Decay bei cozyzen.ai, Einzel-Hit-Muster bei drcozyvibes (155 Mio. vs. 421K/251K, [q06](quellen/q06_ai_theme_page_case_studies.md)) | übersättigt (trotz hoher Views) |
| **Mansions** | 1, 5 | 17 % frisch; 31 % der Top-Reels von ≥1-Mio.-Accounts; vpf-Median 0,75 | für Neueinsteiger geschlossen |
| **Hotels/Resorts** (zur Einordnung) | – | hotel_resort 30 % frisch, neue Reels 0,71, KI-Anteil neuer Reels 11 % (Digest) | schwach, aber nicht KI-getrieben |

![adj nach Raumtyp](charts/adj_by_room.png)

**Hinweis zur Signifikanz:** Raumtyp (Kruskal p = 0,93) und Stil (p = 0,17) sind insgesamt **nicht signifikant**. Signifikant
ist die Gruppierung *innerhalb der KI-Reels*: KI-Outdoor/Bad/Treppe/Pool vs. KI-Schlafzimmer/Wohnzimmer/Küche ergibt ≈ 2,07×
(95-%-KI 1,45–3,0, p < 0,001). Diese Gruppierung wurde **post hoc** gebildet und muss im eigenen Test bestätigt werden
([key_contrasts.csv](data/processed/stats/key_contrasts.csv)).

**Makrosignal Sättigung** (`VERIFIED` als Zitate, [q01](quellen/q01_instagram_platform_rules.md) und [q04](quellen/q04_interior_trends_demand.md)):
- Mosseri schrieb Ende 2025: *"The feeds are starting to fill up with synthetic everything."*
- Meta hat mit Vibes (25.09.2025) einen eigenen KI-Video-Feed gestartet; dessen Clips lassen sich in Reels cross-posten.
- Pinterest bietet seit 16.10.2025 in „home decor“ und „architecture“ einen Regler, um weniger KI-Inhalte zu sehen.

### Teil 1.6 – Wachsende Unterkategorien

„Wachsend“ heißt hier: Der Anteil junger Top-Reels ist hoch, und junge Reels performen auf denselben Seiten mindestens wie
erwartet. Das ist ein Proxy aus einer Momentaufnahme, keine Zeitreihe.

| Feld / Topic | Frische | adj neuer Reels | KI-Anteil neuer Reels | Einordnung |
|---|---|---|---|---|
| **Architecture** (Gruppe) | 57 % (n=60) | **1,53** (n=34) | 44 % | wächst, offen für KI |
| modern-architecture / architecture-design | 75 % / 67 % (je n=12*) | – | Topic: 83 % / 27 % KI | Teil des Wachstums |
| **Commerce-Decor** (home-decor, home-decor-ideas, amazon-home-finds, room-makeover) | 60 % (n=48) | 0,86 (n=29) | 7 % | wächst, aber real und produktgetrieben |
| home-decor (einzeln) | 92 % (n=12*) | – | 0 % | sehr frisch |
| **dream-house** | 83 % (n=12*) | – | Topic: 25 % KI | frisch (anders als „dream-home“ mit 25 %) |
| **treehouse** / luxury-garden | 100 % / 75 % (je n=12*) | – | Topic: 67 % / 25 % KI | frisch |
| Unusual Homes (Gruppe) | 38 % (n=284) | 1,09 (n=108) | 41 % | stabil |
| Generische Räume (room_generic) | 32 % (n=192) | 1,38 (n=62) | 38 % | stabil bis wachsend |
| *Fantasy/Impossible* (Querschnitt) | 42 % (n=62 Reels) | **1,87** (n=26) | – (85 % KI gesamt) | wächst, **nur 2,6 %** der codierten Top-Reels |

Quellen: [freshness_by_group.csv](data/processed/stats/freshness_by_group.csv) und eigene Auswertung (Abschnitt M1).

**KI wächst insgesamt, und die Performance schwankt.** Nicht in jeder Sub-Nische: Bei Luxury Homes, Dream Homes, Mansions,
AI Architecture und AI Interior Design ist der KI-Anteil unter den neuen Reels niedriger als unter allen Top-Reels (Tabelle C).

| Postjahr | codierte Reels | KI-Anteil | adj KI (n) | adj reale Aufnahmen (n) |
|---|---|---|---|---|
| 2023 | 108 | 4,6 % | 0,70 (5*) | 1,94 (93) |
| 2024 | 245 | 22,4 % | 1,12 (53) | 1,45 (152) |
| 2025 | 679 | 29,2 % | 0,61 (194) | 0,85 (382) |
| 2026 | 1.313 | 33,2 % | 0,93 (434) | 0,82 (733) |

Die KI-Anteile stammen aus [summary.json](data/processed/stats/summary.json). Die adj-Werte je Jahr sind eigene Auswertung,
`ESTIMATED`, **nicht auf Signifikanz getestet**. Ältere Jahrgänge sind Überlebende (siehe M2, Punkt 3).
Gesamtvergleich KI vs. real: 0,92× (95-%-KI 0,75–1,09, p = 0,17), **nicht signifikant**.

**Externe Trendsignale** ([q04](quellen/q04_interior_trends_demand.md)):
- **Aufsteigend:** Maximalismus und Eklektik (1stDibs: 39 % bzw. 38 % der 468 befragten Designer) sowie Neo Deco / Art Deco
  („Art deco vintage“ +805 % in einem Pinterest-Saisonreport). Dazu warme Erdtöne wie „chocolate brown“ +153 %, Wellness-Räume
  +164 % und europäische Innenhöfe („French courtyards“ knapp 6×, Houzz).
- **Reif oder abklingend:** Quiet Luxury (Exploding Topics „Peaked“, obwohl die Seite „quiet-luxury“ zu 58 % frisch ist) und
  KI-Interior-Suchbegriffe.
- **Einschränkung:** Pinterest und Houzz veröffentlichen nur steigende Begriffe, ohne absolute Volumina.

**Cross-Platform** (`PROXY`, [q08](quellen/q08_cross_platform_signals.md)): Am stärksten wächst auf Shorts **„KI-Konzept-Bau /
Transformation“**. 10 von 13 Kanälen starteten 2026, und 7 kleine Kanäle erreichen Ø-Views ≥ 5× ihre Abozahl. Dasselbe
Cluster ist aber auch **am schnellsten besetzt**: In einer Suchstichprobe zu „AI dream house transformation“ hatten die
15 Treffer der letzten Woche 8–2.200 Views (Neuabfrage im Faktencheck: 25 Treffer, 0–2.400 Views). Das Muster gleicht einer Lotterie: hohe Varianz, niedriger Erwartungswert.

### Teil 1.7 – AI-Eignung

![adj nach Realismus-Grad](charts/adj_by_realism.png)

![adj nach Produktion (KI vs. real)](charts/adj_by_production.png)

**Kernbefund:** Ob ein Reel mit KI gemacht ist, hängt kaum mit seiner Performance zusammen. Deutlich stärker hängt sie
damit zusammen, **welches Konzept** die KI umsetzt (Korrelation, kein Kausalbeleg):

| Kontrast (adj, [key_contrasts.csv](data/processed/stats/key_contrasts.csv)) | Verhältnis | 95-%-KI | p | Aussage |
|---|---|---|---|---|
| KI vs. reale Aufnahmen | 0,92× | 0,75–1,09 | 0,17 | **n.s.**, kein messbarer Nachteil von KI an sich |
| KI fantasy/impossible (n=53) vs. KI stylized dreamy (n=305) | **3,25×** | 1,75–5,58 | 0,001 | signifikant |
| KI fantasy/impossible vs. KI aspirational realistic (n=328) | **2,53×** | 1,29–3,92 | 0,008 | signifikant |
| KI-Theme-Page (n=228) vs. KI-Creator (n=271) | 0,69× | 0,39–0,84 | < 0,001 | signifikant; Hinweis, dass Identität zählt (Korrelation) |
| KI mit Personen (n=106) vs. ohne (n=580) | 1,68× | 0,99–2,52 | 0,017 | nominal signifikant |
| KI offengelegt (n=215) vs. nicht (n=471) | 0,82× | 0,58–1,18 | 0,15 | n.s. (Kruskal nominal p = 0,006); Kennzeichnung ist trotzdem Pflicht |

**Eignung je Sub-Nische:**
- **Hoch:** Architecture, Future Architecture, AI Architecture, Fantasy-Querschnitt.
  - Der Gegenstand ist ungebaut oder visionär, das Täuschungsrisiko also gering. KI-Reels liegen bei ≈ 0,9–1,0 (n=23–69).
  - Unter den AI-Architecture-Reels sind 15 % fantasy (höchster Wert).
  - Fantasy-KI erreicht 2,27× (n=53).
- **Mittel:** Interior Design (allg.) und Luxury Interiors.
  - Auf den generischen Interior-Seiten liegen KI-Reels bei 1,70 (n=42) gegenüber real 0,89 (n=180). Der Unterschied ist
    n.s. (p = 0,14).
  - Das widerspricht den raumcodierten KI-Werten für Wohnzimmer (0,69), Küche (0,67) und Schlafzimmer (0,77).
  - **Hypothese:** KI-Räume stechen dort heraus, wo KI selten ist (17 % KI auf generischen Seiten), und gehen dort unter, wo
    KI dominiert (Dream-Bedrooms 92 %).
  - Bäder gehören zu den stärkeren KI-Raumtypen: KI-Bad raumcodiert 1,45 (n=28, alle Topics); innerhalb der
    Luxury-Interiors-Seiten 1,24 (n=14*).
- **Niedrig:** Luxury Bedrooms, Living Rooms, Kitchens, Dream Homes, Luxury Homes, Mansions, AI Interior Design.
  - KI liegt unter der Erwartung (0,53–0,77 bei n ≥ 15, raumcodiert oder gebäudecodiert: KI-Mansion 0,66, n=37).
  - Die Topic-basierten Ausreißer (Mansions 3,92, Kitchens 1,18) haben n < 15 und widersprechen den robusteren Codierungen.

**Regeln, Recht und Plattform** (für alle KI-Sub-Nischen):
- **Instagram:** Fotorealistische KI-Videos sind per Meta-Tool zu kennzeichnen. Der Reichweiteneffekt des „AI info“-Labels ist
  `UNKNOWN` ([q01](quellen/q01_instagram_platform_rules.md)).
- **Fotorealistische KI-Personen** ohne Offenlegung machen einen Account nicht empfehlbar ([q01](quellen/q01_instagram_platform_rules.md)).
  Das ist relevant, weil KI-Reels mit Personen tendenziell besser laufen (1,68×, nur nominal signifikant).
- **Monetarisierung:** Ausgeschlossen sind *"static images played in succession"* und *"content that loops"*. Das trifft typische
  Slideshow- und Loop-Interiors ([q01](quellen/q01_instagram_platform_rules.md)).
- **EU AI Act Art. 50:** gilt seit 02.08.2026. Auch realistische **Gebäude und Orte** können Deepfakes sein. Ein Account mit
  Affiliate- oder Sponsoring-Einnahmen gilt als „Deployer“ ([q07](quellen/q07_legal_ai_risk.md), `VERIFIED` Wortlaut,
  Anwendung `ESTIMATED`). Besonders heikel sind fiktive Luxusvillen mit Preis- oder Ortsangabe („This $50M home in Dubai“), also
  genau die Sub-Nischen Luxury Homes und Mansions ([q07](quellen/q07_legal_ai_risk.md) 2.6, § 5 UWG).
- **Cross-Posting:** Pinterest filtert KI in „home decor“ und „architecture“ auf Nutzerwunsch ([q04](quellen/q04_interior_trends_demand.md)).

### Teil 1.8 – Kaufabsicht

Direkt gemessene Kaufabsicht aus öffentlichen Instagram-Daten gibt es nicht (`UNKNOWN`). Wir nutzen drei Proxys:

| Proxy | Befund | Status |
|---|---|---|
| **Shoppability** (sind die gezeigten Dinge kaufbar?) | high: Interior Design 55 %, Luxury Kitchens 55 %, Luxury Interiors 48 %, Luxury Bedrooms 44 %, AI Interior Design 37 %, Luxury Living Rooms 80 % (n=15). Dagegen: Luxury Homes 9 %, Future Architecture 5 %, AI Architecture 4 %, Dream Homes 3 %, Architecture 2 %, Mansions 0 %, Fantasy 0 % | `ESTIMATED` (κ = 0,63) |
| **Commerce-Topics** | home-decor-ideas (1,40 Mio. Median), amazon-home-finds (795K), room-makeover (448K) existieren als große Seiten. Die Commerce-Gruppe hat die **höchste Kommentarrate** aller Topic-Gruppen mit n ≥ 15: 7,5 pro 10.000 Views (n=41 mit Kommentarzahl) gegenüber 3,5 im Gesamtdatensatz (n=2.019). Hypothese: „Wo gibt's das?“-Fragen; Kommentarinhalte nicht ausgewertet | Views `VERIFIED`, Deutung `UNKNOWN` |
| **Markt und Verhalten** | Möbel-E-Commerce 280,84 Mrd. US$ (2026). Visuelle Suche: 20 % der Google-Lens-Suchen sind shopping-bezogen; laut Pinterest ist ≈ die Hälfte der Lens-Treffer Mode oder Home Decor (2020) ([q02](quellen/q02_furniture_affiliate_commerce.md)). Houzz: 44 % sprechen vom „forever home“ ([q04](quellen/q04_interior_trends_demand.md)) | `THIRD-PARTY ESTIMATE` / `VERIFIED` (Zitate) |

**Gegenevidenz:** Interior-Design-Accounts haben ein niedriges Engagement (Reels 0,12 % pro Follower). Home Decor liegt laut
Rival IQ *"towards the bottom of the pack"* und verlor ≈ 30 % Engagement ([q09](quellen/q09_reels_format_benchmarks.md)). Die
Affiliate-Conversion sinkt (Impact: CVR −6 % YoY), und im Möbel-E-Com werden 86 % der Warenkörbe abgebrochen
([q02](quellen/q02_furniture_affiliate_commerce.md), `THIRD-PARTY ESTIMATE`).

**Wichtig für die Positionierung:** Kaufbarkeit geht nicht mit messbar weniger Reichweite einher (high vs. low 1,01×, 95-%-KI 0,80–1,25, p = 0,91).
Die reichweitenstärksten Konzepte (fantasy) sind aber zu 0 % „high shoppable“. Kaufabsicht und Reichweite liegen damit in
**verschiedenen** Sub-Nischen. Daraus folgt die Hybrid-Hypothese aus dem [Strategy Brief](data/processed/strategy_brief.md):
*„Impossible places, possible furniture.“* Sie ist ein Test, kein Befund.

### Teil 1.9 – Möbel-Affiliate-Eignung

| Programm | Konditionen | Status ([q02](quellen/q02_furniture_affiliate_commerce.md)) |
|---|---|---|
| Amazon Associates – Furniture/Home | **3 %**; 24 h plus Warenkorb-Regel; seit 14.04.2026 **keine Provision über geboostete Reels**; Onsite-Provision nur für die exakte ASIN | `VERIFIED` |
| Amazon – Kitchen | 4,5 % | `VERIFIED` |
| Wayfair (inkl. Perigold) | „up to 7 %“, 7 Tage; AOV 332 US$ (Q2 2026) | Rate `THIRD-PARTY`, AOV `VERIFIED` |
| LTK | 10–25 % (bis 30 %); Zulassung ab 5K Followern und ≥ 2 Posts pro Woche; „Exact vs. Similar“-Tagging vorgesehen | `VERIFIED` (Selbstauskunft) |
| Arhaus | bis 4 %, 30 Tage, AOV 1.100 US$ | `VERIFIED` (Agentur) |
| 1stDibs | 5–10 %; AOV 2.850 US$ | Rate `THIRD-PARTY`, AOV `VERIFIED` |
| Minotti / B&B Italia / Poliform / RH | kein öffentliches Affiliate-Programm gefunden | `UNKNOWN` |
| Instagram Affiliate-/Shoppable-Reels | bis 30 Produkte; Start in US, BR, IN, ID, TH – **Deutschland nicht in der Startliste** | `VERIFIED` ([q01](quellen/q01_instagram_platform_rules.md)); DE `UNKNOWN` |

**Warum das für einen KI-Account dünn ist:**
1. **KI-Möbel existieren nicht.** Möglich sind nur „similar items“ über visuelle Suche. Selbst Wayfair ist bei der
   SKU-Zuordnung zurückgerudert, und Instagrams „Shop the Look“-Test erntete Kritik wegen *"cheap knockoffs"*
   ([q02](quellen/q02_furniture_affiliate_commerce.md), `VERIFIED`).
2. **Kleine Beträge pro Bestellung:** Wayfair 7 % × 332 US$ ≈ 23 US$ (Obergrenze), Amazon 3 % × 100 US$ = 3 US$ (eigene
   Beispielrechnung in [q02](quellen/q02_furniture_affiliate_commerce.md), `ESTIMATED`).
3. **Kein verifiziertes Vorbild:** Einen KI-Interior-Account, der systematisch mit „similar items“-Affiliate arbeitet, fand
   die Recherche nicht (`UNKNOWN`). Beobachtet wurde ein Kommentar→DM-Funnel mit „kuratierter Wayfair-Kollektion“ bei
   @roomify.design; ob es Affiliate oder Partnerschaft ist, ist nicht verifiziert ([02_competitor_database.csv](02_competitor_database.csv)).
4. **Affiliate-Links in der Wettbewerber-DB** (72 tief profilierte Accounts): KI 9 von 37, real/3D 10 von 22. Beispiele
   sind die Amazon-Storefront und Rabattcodes bei @deirdres_design sowie Amazon.de und Homary bei @ell.glamhome.

**Eignung je Sub-Nische** (Scores in Abschnitt 4):
- **Brauchbar (Beimischung):** Interior Design, Luxury Bedrooms und Luxury Living Rooms (günstige Deko, Textilien, Leuchten).
  Laut Pinterest werden über Lens am häufigsten *"vases, mirrors, rugs… throw pillows"* gekauft ([q02](quellen/q02_furniture_affiliate_commerce.md)).
- **Kaum:** Luxury Interiors (Luxusmarken ohne Programm), Luxury Kitchens (Umbauprojekt, nur Kleinteile).
- **Keine:** Architecture, Luxury Homes, Mansions, Dream Homes, Fantasy.
- **Ausnahme:** KI-Tool-Affiliate für AI-Architecture- und AI-Interior-Inhalte (siehe Teil 1.10). Das ist ein anderes Produkt als
  Möbel, aber der realistischere Affiliate-Kanal.

### Teil 1.10 – Sponsoren-Interesse

| Sponsorentyp | Belegte Konditionen | Passt zu | Status ([q03](quellen/q03_sponsors_brand_deals.md)) |
|---|---|---|---|
| **KI-Tool-Firmen** | Higgsfield Earn: bis 2.500 US$ pro Video (Tag 1 bis 1.000 US$); Higgsfield Affiliate bis 25 % für 12 Monate; Runway 15 US$ pro Abo ohne Cap; Luma CPP ab 5.000 Followern (Credits, kein Cash); Planner 5D 25–50 %; REimagineHome 30 %; Collov bis 150 US$ | AI Architecture, AI Interior, Future Architecture, Fantasy | `VERIFIED` |
| Möbel- und Deko-Marken | überwiegend Affiliate (Wayfair, Castlery); bezahlte Partnerschaften als „Chance“; **keine Festhonorare für Theme-Pages gefunden** | Interior Design, Luxury Interiors, Bedrooms | `VERIFIED` (Programme) / `UNKNOWN` (Preise) |
| Immobilien, Makler, Verlage | Mansion Global: 2.000 US$ pro IG-Post bei 130K Followern; „+ Boost“ 7.000 US$ pro 3-Wochen-Flight. Makler wollen **echte** Objekte zeigen | Luxury Homes, Mansions (nur mit realen Listings) | `VERIFIED` (Rate Card) |
| Dubai-Entwickler | AED 50.000–200.000 pro Kampagne; seit 01.02.2026 Advertiser Permit Pflicht | Luxury Homes (real) | `THIRD-PARTY` / `VERIFIED` |
| Hotels und Travel | Marriott Tribute: 12.750 US$ plus Aufenthalt, für **echte** Aufenthalte | nicht KI | `VERIFIED` |

**Gegenevidenz:**
- Die Begeisterung für KI-Creator-Content fiel von 60 % (2023) auf 26 % (2025).
- 89 % der Enterprise-Marketer planen keine Arbeit mit virtuellen Influencern.
- 39 % der Gen Z sehen KI-Werbung negativ.
- Marketer steigern zugleich ihre KI-Budgets (79 %).
- Deutung: KI ist in der **Produktion** willkommen, als **Gesicht** nicht ([q03](quellen/q03_sponsors_brand_deals.md), `VERIFIED`).

**Belege aus der Wettbewerber-DB** (72 tief profilierte Accounts): Eine konkrete Marken- oder Partnernennung fand sich bei
KI-Accounts in 4 von 37 Fällen, bei real/3D in 14 von 22 und bei Lifestyle-Creatorn in 7 von 8.

**Beobachtete KI-Beispiele:**
- @soothenests: Dreamina-Partnerpost (#dreaminapartner) auf Threads, dort mit nur 460 Views.
- @ifonly.ai: Kooperation mit @artlist.io.
- @archibible: Luma-Link.
- @aiforarchitects: B2B-Aufträge. Beobachteter Caption-Schluss: *"For private commissions and inquiries"*.
- Quellen: [q06](quellen/q06_ai_theme_page_case_studies.md), [02_competitor_database.csv](02_competitor_database.csv).

**Schlussfolgerung 1.10:** Für einen KI-Account ist das Sponsoren-Interesse **real, aber schmal**. Es kommt von KI-Tools
(meist Credits oder Affiliate, selten Cash) und von B2B-Aufträgen. Klassische Home- und Immobilien-Sponsoren sind kaum
erreichbar. Shoutout-Preise für Theme-Pages sind `UNKNOWN`. Details zur Roadmap: [09_monetization.md](09_monetization.md).

---

## 4. Scoring je Sub-Nische (Teil 1 – Bewertungsmatrix)

**Skala 1–5 (5 = attraktiv).** R, K und KI folgen festen Datenregeln. Kauf, Affiliate und Sponsoren sind
**belegte Einschätzungen**, begründet in Teil 1.8–1.10.

| Dimension | Regel |
|---|---|
| **R – Reichweite** | Median der Topic-Mediane: ≥ 1 Mio. = 5 · 500K–1 Mio. = 4 · 250–500K = 3 · 150–250K = 2 · < 150K = 1. Korrektur ±1 nur mit Begründung. |
| **K – Konkurrenz** (5 = günstig) | Frische: ≥ 50 % = 5 · 40–50 % = 4 · 30–40 % = 3 · 20–30 % = 2 · < 20 % = 1. Abzug −1, wenn das Median-Angebot ≥ 10 Mio. Reels je Topic beträgt. |
| **KI – AI-Eignung** | Prüfreihenfolge 5 → 1 → 2 → 4 → 3. **5** = KI-Reels ≥ 1,5× (n ≥ 15), signifikant gegenüber den Alternativen, keine robuste Gegenmessung · **1** = KI < 0,6 (n ≥ 15) ohne strukturellen Vorteil · **2** = KI < 0,8 in mindestens einer Messung mit n ≥ 15 (Topic-, raum- oder gebäudecodiert) und kein Topic-Wert ≥ 1,5 · **4** = KI 0,9–1,5 (n ≥ 15) und Gegenstand ungebaut oder fiktiv (geringes Täuschungsrisiko) · **3** = KI ≥ 0,9 auf den Topic-Seiten, aber reale Objekte oder widersprüchliche Codierungen. Bei n < 15 auf den Topic-Seiten zählt die raum- bzw. gebäudecodierte Messung. |
| **Kauf – Kaufabsicht** | Anteil „high shoppability“: ≥ 50 % = 4 · 35–50 % = 3 · 15–35 % = 2 · < 15 % = 1. +1 bei belegter Tool- oder Service-Kaufabsicht (KI-Apps mit 10 Mio.+ Downloads, B2B, Kurse). |
| **Aff – Möbel-/Tool-Affiliate** | Einschätzung für einen **KI-first**-Account (similar items vs. Tool-Programme). |
| **Spon – Sponsoren** | Einschätzung für einen **KI-first**-Account. |

| Sub-Nische | R | K | KI | Kauf | Aff | Spon | Σ / 30 | Wachstum-gewichtet / 45 | K.-o.? |
|---|---|---|---|---|---|---|---|---|---|
| *Querschnitt: Fantasy/Impossible Architecture* | 3 | 4 | **5** | 1 | 2 | 4 | 19 | **31** | – |
| Architecture | 4 | **4** | 4 | 1 | 1 | 2 | 16 | **28** | – |
| Interior Design (allg.) | 4 | 2 | 3 | 4 | 3 | 2 | 18 | 27 | – (bedingt) |
| Luxury Kitchens | 4 | 3 | 2 | 4 | 2 | 2 | 17 | 26 | **KI ≤ 2** |
| AI Architecture | 2 | 2 | 4 | 2 | 3 | 4 | 17 | 25 | – |
| AI Interior Design | 3 | 1 | 2 | 4 | 4 | 4 | 18 | 24 | **KI ≤ 2, K = 1** |
| Luxury Interiors | 3 | 2 | 3 | 3 | 2 | 2 | 15 | 23 | – |
| Future Architecture | 2 | 2 | 4 | 1 | 2 | 3 | 14 | 22 | – |
| Dream Homes | 4 | 2 | 2 | 1 | 1 | 2 | 12 | 20 | **KI ≤ 2** |
| Luxury Bedrooms | 3 | 1 | 2 | 3 | 3 | 2 | 14 | 20 | **KI ≤ 2, K = 1** |
| Luxury Homes | 3 | 3 | 2 | 1 | 1 | 1 | 11 | 19 | **KI ≤ 2** |
| Luxury Living Rooms | 2 | 1 | 2 | 4 | 3 | 2 | 14 | 19 | **KI ≤ 2, K = 1** |
| Mansions | 3 | 1 | 2 | 1 | 1 | 1 | 9 | 15 | **KI ≤ 2, K = 1** |

**Wachstum-gewichtet** = 2 × (R + K + KI) + Kauf + Aff + Spon. Die Gewichtung folgt aus Teil 1.4: Ohne organisches
Wachstum gibt es nichts zu monetarisieren. **K.-o.-Regeln für einen KI-first-Account:**
(a) KI-Eignung ≤ 2 → höchstens Nebenformat, kein Kern.
(b) Konkurrenz = 1 (verkrustet) → nicht als Topic-Ziel oder Wachstumsmotor.

**Begründung je Zeile:**

| Sub-Nische | R | K | KI | Kauf / Aff / Spon |
|---|---|---|---|---|
| Fantasy/Impossible | Reel-Median 317K → 3. Topic-Seiten mit dem Namen sind winzig (impossible-architecture: Median 486 Views), das Konzept läuft über andere Seiten | 42 % frisch → 4; nur 2,6 % der codierten Top-Reels, 27 % der Reels von < 10K | 2,27× (n=53), signifikant vs. dreamy und realistisch → 5 | 0 % high shoppable → 1 / Tool-Affiliate plus Hybrid-Test → 2 / KI-Tools und B2B → 4 |
| Architecture | 285K → 3, +1: Hauptseiten „architecture“ 11,75 Mio. und „modern-architecture“ 2,95 Mio. Median, Reel-p90 19,4 Mio., vpf 15,7 → 4 | 57 % → 5, −1 (Angebot 36 Mio.) → 4 | 0,98 (n=23), visionär → 4 | 2 % → 1 / keine Produkte → 1 / Medien, B2B → 2 |
| Interior Design (allg.) | 626K → 4 | 39 % → 3, −1 (17 Mio.) → 2 | 1,70 (n=42, n.s.) gegen raumcodiert 0,67–0,77 → 3 | 55 % → 4 / Programme vorhanden, aber nur similar → 3 / Marken meiden KI → 2 |
| Luxury Kitchens | 522K → 4 | 35 % → 3 | Topic n=11*, raumcodiert KI-Küche 0,67 (n=31) → 2 | 55 % → 4 / Umbauprojekt, Kleinteile 4,5 % → 2 / Marken wollen reale Küchen → 2 |
| AI Architecture | 217K → 2 | 25 % → 2 | 0,97 (n=67), ungebaut → 4 | 4 % +1 (Kurse, B2B) → 2 / Tool-Affiliate → 3 / Tools und B2B (aiforarchitects) → 4 |
| AI Interior Design | 500K → 4, −1: 93 % der Top-Reels älter als 180 Tage → 3 | 7 % → 1 | 0,53 (n=38); Regel 1 entfällt, weil der Gegenstand KI-nativ ist (auch reale Reels dort nur 0,46, n=11*) → Regel 2 → 2 | 37 % +1 (Apps mit 10 Mio.+ Downloads) → 4 / Interior-Tool-Affiliates → 4 / Tool-Partnerschaften → 4 |
| Luxury Interiors | 377K → 3 | 27 % → 2 | 1,01 (n=34); KI-Bad 1,45 (n=28) → 3 | 48 % → 3 / Luxusmarken ohne Programm → 2 / → 2 |
| Future Architecture | 232K → 2 | 22 % → 2 | 0,90 (n=69), ungebaut → 4 | 5 % → 1 / Tool-Affiliate → 2 / KI-Tools → 3 |
| Dream Homes | 862K → 4 | 39 % → 3, −1 (18 Mio.) → 2 | 0,69 (n=15) → 2 | 3 % → 1 / → 1 / → 2 |
| Luxury Bedrooms | 348K → 3 | 8 % → 1 | Topic 1,03 (n=24), raumcodiert 0,77 (n=110), dreamy 0,70 → 2 | 44 % → 3 / günstige Deko → 3 / → 2 |
| Luxury Homes | 300K → 3 | 32 % → 3 | 0,66 (n=35) → 2; plus Irreführungsrisiko | 9 % → 1 / Immobilien → 1 / Makler wollen Reales → 1 |
| Luxury Living Rooms | 310K → 3, −1: niedrigste Spitzen (p90 1,24 Mio., Max 3,1 Mio.) → 2 | 17 % → 1 | Topic 0,28 (n=5*), raumcodiert 0,69 (n=123) → 2 | 80 % (n=15) → 4 / → 3 / → 2 |
| Mansions | 272K → 3 | 17 % → 1 (dazu 31 % der Top-Reels von ≥1-Mio.-Accounts) | Topic 3,92 (n=8*) gegen gebäudecodiert 0,66 (n=37) → 2 | 0 % → 1 / → 1 / → 1 |

**Robustheit:** Auch ohne Gewichtung (Σ / 30) liegt der Fantasy-Querschnitt vorn (19), und Mansions (9) sowie Luxury Homes
(11) bleiben hinten. Interior Design und AI Interior Design erreichen ungewichtet 18 Punkte, vor allem über Kauf, Affiliate
und Sponsoren. AI Interior Design scheitert an beiden K.-o.-Regeln, Interior Design bleibt wegen der widersprüchlichen
KI-Eignung (3) und der Konkurrenz (2) „bedingt“. Die Bewertung von Kauf, Affiliate und Sponsoren ist qualitativ. Selbst wenn
Interior Design in allen drei qualitativen Spalten einen Punkt mehr bekäme (30/45), bliebe der Fantasy-Querschnitt vorn
(31/45). Die K.-o.-Fälle hängen nur an den datenbasierten Spalten K und KI.

---

## 5. Urteil (Teil 1): Ist die Nische attraktiv?

**Ja, bedingt.** Die Nische ist groß, zahlungsnah (Möbel, Deko, KI-Tools) und KI-freundlich. Das gilt aber nur für einen
schmalen Korridor: **originäre, unmögliche bzw. zukunftsweisende Architektur als KI-Studio mit wiedererkennbarer
Identität**. Der naheliegende Einstieg „KI-Luxus-Interiors“ (Schlafzimmer, Wohnzimmer, Küchen, dreamy) ist in den Daten die
**schlechteste** KI-Variante. Er trifft auf verkrustete Seiten, einen übersättigten Look und Decay.

### 5.1 Unter welchen Bedingungen die Nische attraktiv ist

| # | Bedingung | Datengrundlage | Status |
|---|---|---|---|
| 1 | **Konzept statt Raumkatalog:** unmögliche oder ungebaute Architektur (z. B. in Fels gehauen, Turm, alpin), außen und innen. In den Daten hängt die Performance weniger an der Kulisse als an der Unmöglichkeit (explorativ): KI-Klippen-Settings liegen bei nur 0,48 (n=35), Unterwasser über alle Reels bei 0,39 (n=14*), KI in Berg- oder Küstenlage bei 1,80 (n=59) ([pillar_benchmarks.csv](data/processed/stats/pillar_benchmarks.csv), Digest) | Fantasy-KI 2,27× (n=53), 3,25× vs. dreamy (p = 0,001); nur 2,6 % der Top-Reels | belastbarster Befund; Hypothese für den eigenen Account |
| 2 | **Studio- oder Creator-Identität, keine Theme-Page:** eigene Originalwerke, Serien, keine Reposts | Theme-Page vs. KI-Creator 0,68× (p < 0,001); Instagram-Originalitätsregeln 2024/2026 ([q01](quellen/q01_instagram_platform_rules.md)) | signifikant bzw. Plattformregel |
| 3 | **Distribution über frische Kontexte:** Architektur, „dream-house“, Treehouse/Unusual. Verkrustete Seiten (AI Interior, Luxury Bedrooms, Future-Topic-Seiten) nicht als Ziel wählen | Frische 57 % / 83 % / 100 % (die beiden Einzel-Topics je n=12*) vs. 7–22 % | deskriptiv |
| 4 | **Novelty-Engine gegen Decay:** Serien mit wechselnden Konzepten, Story und Überraschung statt Template | Decay-Fälle (Teil 1.4); stabile YT-Kanäle mit Story ([q08](quellen/q08_cross_platform_signals.md)) | Indiz, `PROXY` |
| 5 | **Monetarisierungs-Mix:** KI-Tool-Affiliate/-Sponsoring, B2B-Visualisierung, digitale Produkte. Möbel-Affiliate nur als Hybrid-Beimischung („possible furniture“) | Teil 1.9, 1.10 | `VERIFIED` Programme, Umsätze `UNKNOWN` |
| 6 | **Transparenz:** KI-Kennzeichnung, keine fiktiven Objekte als real mit Preis und Ort, keine fotorealistischen KI-Personen ohne Offenlegung | [q01](quellen/q01_instagram_platform_rules.md), [q07](quellen/q07_legal_ai_risk.md) | Pflicht |
| 7 | **Realistische Erwartung:** anfangs Ø Hunderte bis wenige Tausend Views pro Reel; Wachstum über Ausreißer; wöchentliche KEEP/KILL-Entscheidungen | [q09](quellen/q09_reels_format_benchmarks.md), [15_kpi_framework.md](15_kpi_framework.md) | Benchmark |

### 5.2 Wo die Nische nicht attraktiv ist (für einen KI-first-Account)

- **KI-Luxury-Bedrooms, -Living-Rooms und -Kitchens als Kern.** KI liegt hier bei 0,67–0,77. Die Bedroom- und
  Living-Seiten sind verkrustet (8 % bzw. 17 % frisch). Auf dream-bedrooms sind 92 % der Top-Reels KI.
- **AI Interior Design als Topic-Strategie.** 93 % der Top-Reels sind älter als 180 Tage. KI-Reels liegen bei 0,53, und die
  Suchbegriffe gelten als „Peaked“.
- **Mansions und Luxury Homes als KI-„Listings“.** Großaccounts dominieren (Mansions: 31 % der Top-Reels von ≥1-Mio.-Accounts). KI liegt bei
  0,66. Die Sponsoren (Makler) wollen reale Objekte, und bei fiktiven Preis- oder Ortsangaben drohen Irreführung und
  AI-Act-Probleme.
- **Repost- bzw. Theme-Page-Modell** in jeder Sub-Nische. Es verliert strukturell (0,74) und riskiert den Ausschluss von
  Empfehlungen (Originalitätsregel).
- **Möbel-Affiliate als Hauptgeschäftsmodell.** 3 % bei 24 h, nur similar items, Affiliate-Reels in DE nicht bestätigt.

### 5.3 Rolle je Sub-Nische

| Sub-Nische | Rolle im Account | Kurzbegründung |
|---|---|---|
| Fantasy/Impossible (Querschnitt über Architecture, Future und AI Architecture) | **KERN** (Pillar P1 im [Strategy Brief](data/processed/strategy_brief.md)) | 31/45; stärkster KI-Befund; knappes Angebot |
| Architecture | **Distributionskontext für den Kern** | zweitfrischeste Gruppe (57 %, nach Commerce-Decor mit 60 %), neue Reels 1,53 |
| AI Architecture | **Identität und Monetarisierung** („AI-Architektur-Studio“), nicht Topic-Jagd | Tools/B2B → 4; Seiten 25 % frisch |
| Future Architecture | **nur konzeptionell und fantastisch**; Future-Topic-Seiten nicht als Ziel | KI-geeignet (4), aber Seiten verkrustet (neue 0,59) |
| Luxury Interiors (Bäder, Ankleide) plus Treppen/Hallen als Hero-Element | **Nebenformat** (Statement-Bäder, Transformationen) | KI-Bad 1,45 (n=28), KI-Treppe/Halle 2,24 (n=16) |
| Interior Design (allg.) | **Hybrid- bzw. Choice-Format** („Pick One“ mit kaufbaren Stücken) als Commerce-Brücke | Kauf 4, KI nur 3 (widersprüchlich) |
| Dream Homes | **Keyword bzw. Verpackung** („dream home“), nicht Dreamy-Look | Angebot 169 Mio., KI 0,69 |
| Luxury Bedrooms / Living Rooms | **nur als Varianten in Choice-Formaten** | K.-o. (KI ≤ 2, K = 1) |
| Luxury Kitchens | **nein** (für KI) | KI-Küche 0,67 |
| AI Interior Design | **nein als Content-Kern, ja als Monetarisierungskanal** (Interior-Tool-Affiliates) | K = 1, KI 0,53 |
| Luxury Homes / Mansions | **nein** | K.-o.; Irreführungs- und Sponsor-Mismatch |

Außerhalb der 12 Sub-Nischen gibt es einen zweiten Pfeiler: **Outdoor, Garten, Pool und Bad als KI-Transformation**.
KI-Garten liegt bei 1,61 (n=43), KI-Pool bei 1,16 (n=23), KI-Terrasse bei 1,06 (n=26); der Gruppenkontrast beträgt 2,07×
(post hoc). Details: [08_content_pillars.md](08_content_pillars.md), [10_market_gaps.md](10_market_gaps.md).

### 5.4 Was dieses Urteil kippen würde (Falsifikation im eigenen Account)

Die Entscheidungsregeln stehen in [15_kpi_framework.md](15_kpi_framework.md), Abschnitt 4.3.

| Signal nach 30 Tagen / ~90 Reels | Konsequenz |
|---|---|
| Pillar P1 (Impossible Homes): Gruppen-Index < 0,6 bei n ≥ 6, P(schlechter) ≥ 95 % und NS-Index < 0,6 → **KILL** (Regel 2) | Kernhypothese verwerfen; Architektur-Realismus oder Outdoor-Transformation als Kern testen |
| Choice- bzw. Hybrid-Formate (Interior, Bedrooms) erfüllen **SCALE** (Regel 4: n ≥ 6, Gruppen-Index ≥ 1,5, P(besser) ≥ 95 %, F/1k ≥ Konto) | Interior-Anteil erhöhen: Die öffentlichen Daten zeigten dafür keine Stärke, der eigene Account wäre dann die bessere Evidenz |
| Account Status meldet Originalitäts- oder Label-Einschränkungen → **KILL (Policy)** | Produktion und Kennzeichnung sofort anpassen |
| Tool-Affiliate-EPC liegt ab Monat 2 unter Möbel-Affiliate-EPC | Monetarisierungsgewichtung umdrehen ([09_monetization.md](09_monetization.md)) |

### 5.5 Hypothesen für die Testing-Matrix

Keine dieser Hypothesen ist kausal belegt. Soweit im eigenen Account testbar, stehen sie in
[13_testing_matrix.csv](13_testing_matrix.csv): H1 → T03, H2 teilweise → T03/T14, H3 → T09, H4 nur indirekt → T21.
H5 ist kein Content-Test der Matrix, sondern ein Monetarisierungsvergleich ab Monat 2 ([09_monetization.md](09_monetization.md)).

- **H1:** Unmögliche Konzeptarchitektur erzielt einen höheren account_index als realistische oder dreamy KI-Räume. Erwartung
  aus den Daten: Faktor ≥ 2.
- **H2:** KI-Innenräume performen besser, wenn sie realistisch und kaufbar aussehen und als Choice präsentiert werden, statt
  „dreamy“. Beleg: generische Interior-Seiten mit KI 1,70 (n=42, n.s.); Choice bringt 5,7× Kommentare pro View (p < 0,0001).
- **H3:** Kleine menschliche Figuren als Maßstab erhöhen die Performance von KI-Reels. Beleg: 1,68×, p = 0,017.
- **H4:** Eine Serienidentität („Unbuilt No. X“) schlägt Einzel-Posts im selben Stil. Grundlage ist der Theme-Page-Kontrast;
  im eigenen Account ist das nur indirekt testbar.
- **H5:** KI-Tool-Affiliate bringt pro 1.000 Views mehr als Möbel-Affiliate.

---

## 6. Offene Punkte (`UNKNOWN`)

- **Instagram-Hashtag-Volumina** und die Größe der Hauptseite `/popular/interior-design/`.
- **Wie Topic-Seiten Reels auswählen:** Algorithmus, Zeitfenster und Zählweise der Labels ([q04](quellen/q04_interior_trends_demand.md)).
- **Watch Time, Sends, Saves und Reel-Länge** sind öffentlich nicht messbar. Nur YouTube als `PROXY`
  ([05_viral_patterns.md](05_viral_patterns.md)).
- **Reichweiteneffekt des „AI info“-Labels** auf Instagram ([q01](quellen/q01_instagram_platform_rules.md)).
- **TikTok-Nachfrage** in diesen Sub-Nischen ([q08](quellen/q08_cross_platform_signals.md)).
- **Einnahmen** von KI-Interior- bzw. Architektur-Pages: Es gibt keine verifizierte Zahl ([q06](quellen/q06_ai_theme_page_case_studies.md)).
  Shoutout-Preise für Theme-Pages ([q03](quellen/q03_sponsors_brand_deals.md)).
- **Verfügbarkeit von Instagram-Affiliate-Reels in Deutschland** ([q01](quellen/q01_instagram_platform_rules.md), [q02](quellen/q02_furniture_affiliate_commerce.md)).

---

**Quellen dieses Kapitels:**

- **Daten:** [analysis_digest.md](data/processed/analysis_digest.md) · [strategy_brief.md](data/processed/strategy_brief.md) ·
  [topics.csv](data/processed/stats/topics.csv) · [freshness_by_group.csv](data/processed/stats/freshness_by_group.csv) ·
  [seg_topic_groups.csv](data/processed/stats/seg_topic_groups.csv) · [seg_follower_bucket.csv](data/processed/stats/seg_follower_bucket.csv) ·
  [seg_account_kind_hint.csv](data/processed/stats/seg_account_kind_hint.csv) · [seg_production.csv](data/processed/stats/seg_production.csv) ·
  [seg_realism.csv](data/processed/stats/seg_realism.csv) · [key_contrasts.csv](data/processed/stats/key_contrasts.csv) ·
  [summary.json](data/processed/stats/summary.json) · [04_reel_database.csv](04_reel_database.csv) ·
  [topic_reels.csv](data/processed/topic_reels.csv) · [02_competitor_database.csv](02_competitor_database.csv)
- **Recherche:** [q01](quellen/q01_instagram_platform_rules.md) · [q02](quellen/q02_furniture_affiliate_commerce.md) ·
  [q03](quellen/q03_sponsors_brand_deals.md) · [q04](quellen/q04_interior_trends_demand.md) · [q05](quellen/q05_competitor_lists.md) ·
  [q06](quellen/q06_ai_theme_page_case_studies.md) · [q07](quellen/q07_legal_ai_risk.md) · [q08](quellen/q08_cross_platform_signals.md) ·
  [q09](quellen/q09_reels_format_benchmarks.md)
