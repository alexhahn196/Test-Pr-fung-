# F – Marktvergleich DE/DACH vs. US vs. UK vs. International-Englisch

**Studie:** Welche Nische und welcher Markt eignen sich für eine KI-generierte, faceless Instagram-Reels-Theme-Page mit Affiliate-Monetarisierung?
**Teil F:** Marktvergleich mit belastbaren Daten
**Stand:** 26.09.2026 · **Rohdaten:** `raw_market_data.csv` (283 Zeilen, gleiche Labels)

**Datenqualitäts-Labels**
- **VERIFIED**: Zahl direkt aus Primärquelle oder offiziellem Aggregat abgerufen (Statistikamt, Verband, Plattform-Werbetools über DataReportal, Amazon-Programmseite).
- **THIRD-PARTY ESTIMATE**: Schätzung/Snapshot eines Drittanbieters (z. B. Hashtag-Tools, Statista-Teaser, CPM-Benchmarks, NexLev-Modelle).
- **CLAIMED**: Anbieteraussage mit Eigeninteresse (z. B. Geniuslink über Geniuslink).
- **UNKNOWN**: nicht belastbar ermittelbar, Datenlücke.
- **ANNAHME**: eigene Modellannahme in Rechnungen, keine Messung.

> **Methodik-Hinweis:** Im Verlauf der Recherche war das WebSearch-Kontingent der Sitzung aufgebraucht. Danach habe ich nur noch bekannte Primärquellen direkt abgerufen (WebFetch, offizielle APIs von IMF, EZB und ONS, Sitemaps der Verbände). Einige Wunschquellen (TikTok Creative Center, Statista-Paywall, HypeAuditor-Länderreports) waren nicht zugänglich. Sie stehen unter „Datenlücken“.

---

## 0. Kurzfazit (Executive Summary)

1. **Reichweite:** Der englischsprachige Kernmarkt (US, UK, CA, AU, IE, NZ) hat **≈259 Mio. Instagram-Werbereichweite**, DACH hat **≈38,5 Mio.** (deutschsprachig ≈37 Mio.). Das ist ein Faktor von **≈7**. Allein die USA kommen auf 182 Mio. (VERIFIED, DataReportal 2026).
2. **E-Commerce:** US **1.233,7 Mrd. USD** (2025), UK **≈132,8 Mrd. GBP** (≈175 Mrd. USD), DACH **≈137 Mrd. USD** (DE 92,3 Mrd. € netto + AT 12,3 Mrd. € + CH 15,8 Mrd. CHF). Der Onlineanteil liegt in DE bei nur **13,5 %**, in UK bei **27,5 %** und in den USA bei **16,4 %**.
3. **Amazon-Dominanz in DE:** Amazon.de (Eigenhandel + Marketplace) steht für **63,3 %** des deutschen Onlinehandels (HDE/IFH 2026). In den USA sind es **≈40,5 %** (Statista), in UK **≈25 %** (schwache Drittquelle). Für eine Amazon-Affiliate-Page ist DE damit der konzentrierteste Markt. Österreich wird über amazon.de mitbedient.
4. **Provisionen:** Amazon zahlt in **DE und UK 5 %** auf Möbel, Wohnen, Küche und Baumarkt, in den **USA 3 %** (Kitchen 4,5 %). In den typischen Theme-Page-Nischen ist die Provision pro Euro Umsatz in DE und UK also **+11 % (Küche) bis +67 % (Möbel/Wohnen/Baumarkt)** höher als in den USA (VERIFIED).
5. **Content-Konkurrenz:** Bei Wohnen/Interior und Amazon-Finds ist das englische Hashtag-Volumen **137–180× größer** als das deutsche. Pro adressierbarem Nutzer ist es **≈20–26× dichter**, bei globaler Basis ≈3×. Bei Hund, Garten, Kaffee und Putzen ist die deutsche Community **pro Nutzer ähnlich aktiv** (EN-Dichte nur 1,3–2×, global sogar niedriger). Dort gibt es **keinen Konkurrenzvorteil DE**.
6. **Rechnung:** Eine deutschsprachige Page ist wirtschaftlich überlegen, wenn sie in ihrem Markt einen **≈3- bis 11-fach höheren Reichweitenanteil** erzielt als eine vergleichbare englische Page in ihrem. Das ist plausibel in **Wohnen/Deko, „Amazon-Fundstücke“/Haushalts-Gadgets, Küche und Heimwerken**, also dort, wo die Content-Dichte-Lücke ≥3–20× beträgt und DE 5 % Provision zahlt. In **Hund, Garten und Kaffee** gilt das eher nicht (Details in Abschnitt 12).

---

## 1. Plattform-Nutzer nach Land

Quelle aller Länderwerte: DataReportal „Digital 2026“-Länderreports. Die Daten stammen aus den Werbetools der Plattformen, Stand Okt./Ende 2025. Ad Reach ist **nicht** identisch mit Unique Users (Duplikate, Fake-Accounts, Altersgrenzen).

### 1.1 DACH

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| 31,3 Mio. (37,2 % Bev.) | Instagram-Werbereichweite DE (44,2 % der 18+) | https://datareportal.com/reports/digital-2026-germany | 2025 | VERIFIED |
| 23,7 Mio. (33,9 % der 18+) | TikTok-Werbereichweite DE, nur 18+ | https://datareportal.com/reports/digital-2026-germany | 2025 | VERIFIED |
| 64,7 Mio. (77,1 %) | YouTube-Werbereichweite DE | https://datareportal.com/reports/digital-2026-germany | 2025 | VERIFIED |
| 22,7 Mio. (27,1 %) | Pinterest DE, relativ stark (UK: 22,3 %) | https://datareportal.com/reports/digital-2026-germany | 2025 | VERIFIED |
| 64,7 Mio. | Social-Media-Identitäten DE, erstmals −0,8 Mio. ggü. Vorjahr | https://datareportal.com/reports/digital-2026-germany | 2025 | VERIFIED |
| 3,35 Mio. / 2,49 Mio. / 6,98 Mio. / 2,39 Mio. | AT: Instagram / TikTok 18+ / YouTube / Pinterest | https://datareportal.com/reports/digital-2026-austria | 2025 | VERIFIED |
| 3,80 Mio. / 2,46 Mio. / 7,27 Mio. / 2,38 Mio. | CH: Instagram / TikTok 18+ / YouTube / Pinterest | https://datareportal.com/reports/digital-2026-switzerland | 2025 | VERIFIED |
| 66 % | TikTok-Nutzung bei 16- bis 19-Jährigen in DE (+5 Pp.) | https://einzelhandel.de/images/presse/Pressekonferenz/2026/onlinemonitor26/Online_Monitor_2026.pdf | 2025 | VERIFIED (Befragung IFH) |

### 1.2 Englischsprachige Märkte

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| 182 Mio. (52,3 %) | Instagram USA (64,1 % der 18+) | https://datareportal.com/reports/digital-2026-united-states-of-america | 2025 | VERIFIED |
| 153 Mio. (55,7 % der 18+) | TikTok USA 18+ | dto. | 2025 | VERIFIED |
| 254 Mio. / 96,9 Mio. | YouTube / Pinterest USA | dto. | 2025 | VERIFIED |
| 35,5 Mio. (50,9 %) | Instagram UK (62,6 % der 18+) | https://datareportal.com/reports/digital-2026-united-kingdom | 2025 | VERIFIED |
| 26,8 Mio. / 55,5 Mio. / 15,5 Mio. | UK: TikTok 18+ / YouTube / Pinterest | dto. | 2025 | VERIFIED |
| 21,0 Mio. / 16,6 Mio. | Kanada: Instagram / TikTok 18+ (inkl. frankophoner Nutzer) | https://datareportal.com/reports/digital-2026-canada | 2025 | VERIFIED |
| 15,2 Mio. / 10,9 Mio. | Australien: Instagram / TikTok 18+ | https://datareportal.com/reports/digital-2026-australia | 2025 | VERIFIED |
| 2,60 Mio. / 2,59 Mio. | Irland: Instagram / TikTok 18+ | https://datareportal.com/reports/digital-2026-ireland | 2025 | VERIFIED |
| 2,65 Mio. / 2,04 Mio. | Neuseeland: Instagram / TikTok 18+ | https://datareportal.com/reports/digital-2026-new-zealand | 2025 | VERIFIED |
| 481 Mio. | Instagram Indien (nur Teil englischsprachig, geringe Kaufkraft; TikTok gesperrt) | https://datareportal.com/reports/digital-2026-india | 2025 | VERIFIED |

### 1.3 Aggregierte Reichweite nach Sprachraum (eigene Summen)

| Plattform | DACH | davon deutschsprachig* | EN-Kern (US+UK+CA+AU+IE+NZ) | Faktor EN-Kern/DACH |
|---|---|---|---|---|
| Instagram | 38,45 Mio. | ≈36,9 Mio. | 258,95 Mio. | **6,7×** (7,0× vs. dt.-sprachig) |
| TikTok (18+) | 28,65 Mio. | – | 211,93 Mio. | 7,4× |
| YouTube | 78,95 Mio. | – | 372,0 Mio. | 4,7× |
| Pinterest | 27,47 Mio. | – | 131,51 Mio. | 4,8× |

\*ANNAHME: etwa 60 % der Schweizer Nutzer sind deutschsprachig. Der BFS-Wert liegt nur als Grafik vor und ist deshalb nicht exakt extrahiert. Die Größenordnung ist jedoch belastbar.

**Angebotsseite als Proxy:** Laut W3Techs (26.09.2026) sind **49,5 %** aller Websites englischsprachig und **5,9 %** deutschsprachig (THIRD-PARTY ESTIMATE). Das Verhältnis von Content-Angebot (~8:1) zu Nutzern (~7:1) ist im Web also ähnlich. Auf Social Media weicht es je nach Nische stark ab (Abschnitt 7).

---

## 2. E-Commerce-Markt

### 2.1 Gesamtmarkt

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| **92,3 Mrd. €** netto (+3,9 %) | DE B2C-Onlinehandel (HDE/IFH, inkl. digitaler Güter, ohne Dienstleistungen) | https://einzelhandel.de/images/presse/Pressekonferenz/2026/onlinemonitor26/Online_Monitor_2026.pdf | 2025 | VERIFIED |
| **96,3 Mrd. €** (+4,3 %) | DE Prognose HDE | https://einzelhandel.de/presse/aktuellemeldungen/15196-online-handel-als-wachstumstreiber-fuer-den-einzelhandel-marktplaetze-von-grosser-bedeutung-nutzer-werden-aelter | 2026 | VERIFIED (Prognose) |
| 83,1 Mrd. € brutto (+3,2 %) | DE E-Commerce mit Waren laut bevh (andere Abgrenzung). Inkl. digitaler Dienstleistungen 97,5 Mrd. €, Prognose 2026 +3,8 % | https://bevh.org/detail/wachstum-im-e-commerce-lichtblick-in-der-deutschen-wirtschaft | 2025 | VERIFIED |
| 13,5 % | Onlineanteil am DE-Einzelhandel (Vorjahr 13,4 %) | HDE Online-Monitor 2026 (s. o.) | 2025 | VERIFIED |
| **12,3 Mrd. €** (+3 %) | AT Online-/Distanzhandelsausgaben, Onlineanteil 13 %, 5,8 Mio. Onlineshopper | https://www.handelsverband.at/publikationen/studien/ecommerce-studie-oesterreich/ecommerce-studie-oesterreich-2026/ | 2026 (Befragung 04/2026) | VERIFIED |
| 47 % (5,8 Mrd. €) | Anteil der österreichischen Online-Ausgaben, der an ausländische Anbieter fließt | dto. | 2026 | VERIFIED |
| **15,8 Mrd. CHF** (+6 %) | CH Onlinemarkt, davon Inland 13,0 Mrd., Ausland 2,8 Mrd. CHF | https://handelsverband.swiss/news/schweizer-online-konsum-waechst-im-jahr-2025-erneut-um-6-das-wachstum-der-einkaeufe-im-ausland-flacht-ab/ | 2025 | VERIFIED |
| **1.233,7 Mrd. USD** (+5,4 %) | US Retail-E-Commerce, 16,4 % des Einzelhandels (2024: 16,1 %) | https://www2.census.gov/retail/releases/historical/ecomm/25q4.pdf | 2025 | VERIFIED |
| 27,5 % | UK (GB) Internetanteil am Einzelhandel, Jahreswert NSA (2024: 27,1 %) | https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/j4mc/drsi | 2025 | VERIFIED |
| **≈132,8 Mrd. GBP** | UK Online-Retail: ONS-Serie JE2J mit Ø 2.546 Mio. £/Woche × 52,14. Zur Plausibilisierung liefert dieselbe Methode für 2024 127,1 Mrd. £, eine Drittquelle nennt 127,4 Mrd. £ | https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/je2j/drsi | 2025 | VERIFIED (Hochrechnung eigene) |

**Umgerechnet** (EZB-Jahresdurchschnitt 2025: 1 € = 1,1300 USD = 0,8568 GBP = 0,9370 CHF; VERIFIED):

| Markt | E-Com 2025 in Mrd. USD | Faktor vs. DACH |
|---|---|---|
| DACH (DE+AT+CH, Abgrenzungen gemischt) | ≈137 | 1,0 |
| UK | ≈175 | 1,3 |
| USA | 1.234 | 9,0 |

### 2.2 Kategorien – Deutschland (HDE/IFH, netto 2025)

| Branche | Onlineumsatz | Anteil am Online-Gesamt | Onlineanteil an der Branche | Datenqualität |
|---|---|---|---|---|
| Fashion & Accessoires | 21,2 Mrd. € | 22,9 % | **44,2 %** (2024: 43,1 %) | VERIFIED |
| CE/Elektro | 19,7 Mrd. € | 21,3 % | ≈45,1 % | VERIFIED (Umsatz) / Anteil aus PDF-Layout zugeordnet |
| Freizeit & Hobby (inkl. Spielwaren, Sport) | 14,1 Mrd. € | 15,3 % | ≈37,6–38,9 % | VERIFIED (Umsatz) / Anteil THIRD-PARTY-Interpretation |
| FMCG (Lebensmittel + Drogerie) | 13,4 Mrd. € | 14,5 % | 5,0 % (Wachstum +10,4 %) | VERIFIED |
| **Wohnen & Einrichten** | **8,1 Mrd. €** | 8,8 % | **≈21,6 %** | VERIFIED (Umsatz) / Anteil rekonstruiert |
| Gesundheit & Wellness | 6,1 Mrd. € | 6,6 % | ≈17,5 % | VERIFIED / rekonstruiert |
| **Heimwerken & Garten** (DIY-Kernsortiment) | **3,3 Mrd. €** | 3,6 % | **7,6 %**, einzige Branche mit negativer CAGR 2020–25 (−0,5 %) | VERIFIED |
| Heimtierbedarf (FMCG-Warengruppe) | – | – | ≈26,6 % (Zuordnung unsicher) | THIRD-PARTY-Interpretation |

Quelle: https://einzelhandel.de/images/presse/Pressekonferenz/2026/onlinemonitor26/Online_Monitor_2026.pdf. Zu bevh-Warengruppen (Möbel/Lampen/Deko +3,3 %, Haushaltsgeräte +4,8 %, Tierbedarf +5–5,4 %, Spielwaren +3,8 %) liegen nur Sekundärzitate mit widersprüchlichen Absolutwerten vor. Ich übernehme deshalb nur die Wachstumsraten (THIRD-PARTY).

**Lesart für Theme-Pages:** In Wohnen/Einrichten und Heimwerken/Garten liegt der Onlineanteil in DE noch niedrig (21,6 % bzw. 7,6 %). Das spricht für Aufholpotenzial, die Wachstumsraten sind jedoch moderat (+2–3 %). Bei Fashion und Elektronik ist der Onlineanteil hoch. Dort treffen aber hohe Retouren (Fashion) auf niedrige Provisionen (Elektronik 2,5–3 %).

### 2.3 Kategorien – AT, CH, UK

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| 2,4 / 1,5 / 1,0 Mrd. € | AT: Bekleidung / Elektronik / Möbel | https://www.handelsverband.at/publikationen/studien/ecommerce-studie-oesterreich/ecommerce-studie-oesterreich-2026/ | 2026 | VERIFIED |
| 28 % / 16 % / 15 % | CH: Anteil Home Electronics (+11 %) / Fashion / Home & Living am Onlinemarkt | https://handelsverband.swiss/news/schweizer-online-konsum-waechst-im-jahr-2025-erneut-um-6-das-wachstum-der-einkaeufe-im-ausland-flacht-ab/ | 2025 | VERIFIED |
| 28,3 % | UK Internetanteil Textil/Bekleidung/Schuhe | https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/ms76/drsi | 2025 | VERIFIED |
| 24,7 % | UK Internetanteil „Household goods stores“ (2023: 27,0 %) | https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/ms77/drsi | 2025 | VERIFIED |
| – | US-Kategorien (Census MRTS nach Branche) | nicht abgerufen | – | UNKNOWN |

---

## 3. Kaufkraft

| Markt | BIP/Kopf PPP 2025 (Int.$) | Proj. 2026 | BIP/Kopf nominal 2025 (USD) | Online-Ausgaben/Kopf 2025 (abgeleitet) | Datenqualität |
|---|---|---|---|---|---|
| DE | 74.004 | 76.747 | 60.439 | 1.100 € (≈1.243 USD). Pro Onlineshopper ≈1.873 € (35,2 Bestellungen × Ø 53,2 €, HDE) | VERIFIED (IMF) / abgeleitet |
| AT | 75.825 | 78.334 | 63.161 | 1.350 € je Einwohner, 2.120 € je Onlineshopper (HV) | VERIFIED |
| CH | 102.096 | 105.680 | 115.620 | 1.759 CHF (≈2.122 USD) | VERIFIED / abgeleitet |
| US | 89.991 | 94.430 | 89.991 | **3.545 USD** | VERIFIED / abgeleitet |
| UK | 65.525 | 67.585 | 57.608 | 1.905 £ (≈2.513 USD) | VERIFIED / abgeleitet |
| CA | 67.013 | 70.006 | 55.765 | – | VERIFIED |
| AU | 72.132 | 74.755 | 66.352 | – | VERIFIED |
| IE | 152.632 | 159.129 | 130.652 (durch Konzernsitze verzerrt) | – | VERIFIED |
| NZ | 55.840 | 58.308 | 48.621 | – | VERIFIED |
| IN | 11.789 | 12.801 | 2.675 | – | VERIFIED |

Quelle BIP: IMF World Economic Outlook DataMapper (PPPPC, NGDPDPC), abgerufen am 26.09.2026. https://www.imf.org/external/datamapper/PPPPC@WEO
**Verfügbares Einkommen (OECD):** nicht abgerufen, siehe Datenlücken.

**Gewichtete Online-Ausgaben pro Kopf:** DACH ≈ **1.346 USD**, US+UK ≈ **3.373 USD**, also 2,5× (eigene Berechnung).

---

## 4. Amazon-Marktanteil und Händlerlandschaft

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| **63,3 %** | Amazon.de gesamt am DE-Onlinehandel: Eigenhandel 17,2 % + Marketplace 46,1 %. Institutionell betrachtet, also inkl. Auslandsumsätze über amazon.de | https://einzelhandel.de/images/presse/Pressekonferenz/2026/onlinemonitor26/Online_Monitor_2026.pdf | 2025 | VERIFIED |
| 56,7 % / 10,8 % | Marktplätze gesamt / andere Marktplätze (eBay, Otto, Zalando/About You, TikTok Shop …) | dto. | 2025 | VERIFIED |
| 5,0 % (≈4,7 Mrd. €) | Temu + Shein am DE-Onlinehandel | dto. + HDE-PM | 2025 | VERIFIED |
| ≈220 Mio. € | TikTok-Shop-Umsatz DE im Startjahr. 9 % der Internetnutzer haben dort schon gekauft | dto. (nach PwC/charm.io) | 2025 | THIRD-PARTY ESTIMATE |
| 15.004,6 / 4.410,0 / 2.581,9 / 2.115,7 Mio. € | Onlineshop-Umsatz netto: amazon.de / otto.de / zalando.de / mediamarkt.de. Weiter: apple.com 1.710, ikea.com 1.434, shein.com 1.120 | https://www.ehi.org/news/top-100-onlineshops-in-deutschland/ | 2024 | VERIFIED |
| 4,3 Mrd. € (>40 %) | Amazon-GMV mit österreichischen Kunden (kein eigener AT-Store, Abwicklung über amazon.de). Zalando 607 Mio. € | https://www.ots.at/presseaussendung/OTS_20250605_OTS0015/handelsverband-und-ecdb-praesentieren-e-commerce-report-2025-amazon-zalando-und-shop-apotheke-sind-groesste-online-haendler-in-oesterreich | 2024/25 | VERIFIED |
| – | CH: Marktführer Digitec Galaxus, 13 Marktplätze unter den Top 30. Amazon ist nicht dominant | https://handelsverband.swiss/news/schweizer-online-konsum-waechst-im-jahr-2025-erneut-um-6-das-wachstum-der-einkaeufe-im-ausland-flacht-ab/ | 2025 | VERIFIED (qualitativ) |
| **40,5 %** | Amazon-Anteil am US-E-Commerce, Walmart 9,2 %, Apple 3,2 % | https://www.statista.com/statistics/274255/market-share-of-the-leading-retailers-in-us-e-commerce/ | 2025 | THIRD-PARTY ESTIMATE |
| ≈25 % | Amazon-Anteil am UK-Onlinehandel („roughly a quarter“). Wettbewerber: eBay, Argos, Tesco, Temu | https://businesstats.com/e-commerce-in-the-uk/ | 2024/25 | THIRD-PARTY ESTIMATE (schwach) |

**Implikation:** Ein einziges Partnerprogramm (Amazon.de) deckt in DE fast zwei Drittel und in AT über 40 % des Onlinemarkts ab. In den USA fließen etwa 60 % des E-Commerce an Nicht-Amazon-Händler (Walmart, Target, Brand-Shops). Dort lohnen zusätzliche Programme, die mehr Aufwand, aber auch mehr Optionen bedeuten.

---

## 5. Affiliate- und Influencer-Markt

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| **932 Mio. €** (+8 %) | DE Affiliate- & Partner-Marketing-Investitionen, 80 % erfolgsbasiert vergütet | https://www.bvdw.org/news-und-publikationen/apmc-studie-macht-marktpotenzial-von-affiliate-und-partner-marketing-sichtbar/ | 2025 | VERIFIED |
| **18,7 Mrd. €** (+12 %) | DE über Affiliate vermittelter Umsatz, 228 Mio. Transaktionen (≈625.000/Tag) | dto. | 2025 | VERIFIED |
| **≈16 %** | Anteil des DE-E-Commerce-Umsatzes, der auf Affiliate-Links zurückgeht | dto. | 2025 | VERIFIED |
| **19,1 %** | Anteil von Content-Publishern + Influencern/Social Content an den DE-Affiliate-Investitionen | dto. | 2025 | VERIFIED |
| 13 % (30–39 J.: 23 %) | DE-Internetnutzer, die ein Produkt nach einem Social-Media-Beitrag gekauft haben | HDE Online-Monitor 2026 | 2025 | VERIFIED (Befragung) |
| 554 Mio. £ | UK Affiliate-Spend mit 8,9 Mrd. £ Sales (**veraltet**) | https://www.iabuk.com/press-release/affiliate-marketing-spend-increases-151-topping-ps550-million | 2017 | VERIFIED (alt) |
| **966 Mio. £** → 1,2 Mrd. £ (P) | UK Creator-Partnership-Umsatz 2025, Prognose 2026 | https://www.iabuk.com/value-uk-creator-partnership | 2025/26 | VERIFIED |
| 40,5 Mrd. £ (+10 %) | UK Digital Adspend gesamt | https://www.iabuk.com/adspend | 2025 | VERIFIED |
| 29,5 / **37** / 44 Mrd. USD | US Creator Ad Spend 2024 / 2025 / 2026P (IAB-Zahl, zitiert) | https://influencermarketinghub.com/influencer-marketing-statistics/ | 2024–26 | THIRD-PARTY ESTIMATE |
| 32,55 Mrd. USD | Globaler Influencer-Marketing-Markt (Schätzung) | dto. | 2025 | THIRD-PARTY ESTIMATE |
| – | US Affiliate-Spend (Statista/AffiliateBLOG, Paywall) | https://www.statista.com/statistics/693438/affiliate-marketing-spending/ | 2023–25 | UNKNOWN |
| 560 Mio. € / ≈30.000 | DACH Influencer-Marketing-Volumen / deutschsprachige Influencer (**veraltet**) | https://www.goldmedia.com/studie/goldmedia-marktstudie-influencer-marketing-in-der-region-dach/ | 2017/2018 | VERIFIED (alt) |

### 5.1 Typische Provision – Amazon Associates (Standardsätze, abgerufen am 26.09.2026)

| Kategorie (Theme-Page-relevant) | **DE** (partnernet.amazon.de) | **UK** (affiliate-program.amazon.co.uk) | **US** (affiliate-program.amazon.com) |
|---|---|---|---|
| Möbel / Wohnen (Home) | **5,0 %** | **5,0 %** | 3,0 % |
| Küche | **5,0 %** | **5,0 %** | 4,5 % |
| Baumarkt / Home Improvement / Werkzeug | **5,0 %** | **5,0 %** | 3,0 % |
| Garten | 3,0 % (alle anderen) | 3,0 % (alle anderen) | 3,0 % (Lawn & Garden) |
| Haustier | 3,0 % (alle anderen) | 3,0 % (alle anderen) | 3,0 % |
| Spielzeug | 3,0 % (alle anderen) | 3,0 % (alle anderen) | 3,0 % |
| Beauty | 4,0 % | 4,0 % | 3,0 % (Luxury Beauty 10 %) |
| Sport & Fitness / Outdoor | 4,0 % | 4,0 % | 3,0 % |
| Fashion / Schuhe / Uhren | 6,0 % | 6,0 % | 4,0 % |
| Mobile Elektronik / Haushaltsgroßgeräte | 2,5 % | 2,5 % | – (TV 2 %, PC 2,5 %) |
| Videospiele / Konsolen | 1,0 % | 1,0 % | 1,0 % |
| Alle anderen | 3,0 % | 3,0 % | 4,0 % |

URLs: https://partnernet.amazon.de/help/node/topic/GRXPHT8U84RAYDXZ · https://affiliate-program.amazon.co.uk/help/node/topic/GRXPHT8U84RAYDXZ · https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ (VERIFIED, ohne Gültigkeitsdatum auf den Seiten). Garten, Haustier und Spielzeug sind in DE/UK nicht explizit gelistet. Ich interpretiere sie als „alle anderen“ (3 %).

**Wichtigste Erkenntnis:** In **Wohnen, Küche und Heimwerken** zahlen DE und UK **5 %** gegenüber 3 % in den USA. Pro Euro vermitteltem Umsatz verdient eine deutsche Page also **+67 %** (Home) bzw. **+11 %** (Kitchen).

---

## 6. Retouren-Kultur

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| **24,2 %** der Pakete | DE, „fast jedes vierte Paket geht zurück“; DE ist „Retouren-Europameister“, CH und AT knapp dahinter | https://www.retourenforschung.de/info-ergebnisse-des-europaeischen-retourentachos-veroeffentlicht.html | 2021 (PM 07.09.2022) | VERIFIED |
| ≈530 Mio. Sendungen / ≈1,3 Mrd. Artikel | DE-Retourenvolumen | dto. | 2021 | VERIFIED |
| 83 % / 91 % | Fashion-Anteil an retournierten Sendungen / Artikeln | dto. | 2021 | VERIFIED |
| 6,95 € / 2,85 € | Ø Kosten je Retourensendung / je Artikel | dto. | 2021 | VERIFIED |
| **849,9 Mrd. USD** (15,8 % des Umsatzes) | US-Retouren gesamt | https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025 | 2025 | VERIFIED |
| **19,3 %** | US-Online-Retourenquote (bezogen auf Umsatz) | dto. | 2025 | VERIFIED |
| bis 30 % / 62 % | UK: Fashion-Retouren „können 30 % erreichen“ / Anteil Konsumenten mit „Bracketing“ | https://ti-insight.com/briefs/uk-e-commerce-growth-and-the-evolving-returns-landscape/ | 2025 | THIRD-PARTY ESTIMATE |
| – | Amazon behält Vergütungen ein, „um Stornierungen oder Rücksendungen zu berücksichtigen“ | https://partnernet.amazon.de/help/operating/agreement | 2026 | VERIFIED |

**Lesart:** Die Metriken sind nicht direkt vergleichbar (DE Paketquote vs. US Umsatzquote). Die deutsche Retourenlast ist **fashion-getrieben** (83–91 % der Retouren). In Wohnen/Deko, Küche und Gadgets ist der Retouren-Nachteil für DE deshalb geringer als die Schlagzeile „Retouren-Weltmeister“ nahelegt. Ich setze in der Rechnung nur 3 Prozentpunkte mehr Provisionsverlust für DE an (ANNAHME).

---

## 7. Konkurrenz-Indikatoren auf Content-Ebene

### 7.1 Instagram-Hashtag-Volumen (Posts gesamt)

Quelle: best-hashtags.com, abgerufen am 26.09.2026 (https://best-hashtags.com/hashtag/{tag}/). **THIRD-PARTY ESTIMATE.** Die Snapshot-Daten der Drittquelle schwanken zwischen **10/2024 und 09/2026** (Datum je Tag in der CSV). Instagram zeigt Post-Zahlen nicht mehr öffentlich. Für Umlaut-Tags (#küchenhelfer, #amazonfundstücke, #siebträger, #küchenideen) liefert das Tool keine Daten (UNKNOWN).

| Nische | Englische Tags (Posts) | Deutsche Tags (Posts) | Roh-Verhältnis EN:DE |
|---|---|---|---|
| **Wohnen/Interior** | #interiordesign 210,2 Mio. · #homedecor 172,4 Mio. · #livingroom 22,8 Mio. · #homeinspo 12,9 Mio. · #livingroomdecor 8,6 Mio. | #wohnen 904k · #wohnzimmer 696k · #inneneinrichtung 516k · #einrichtung 496k · #wohnideen 280k · #wohnzimmerideen 225k · #einrichtungsideen 109k | **≈137:1** (Cluster), #homedecor:#wohnideen ≈616:1 |
| **Amazon-Finds** | #amazonfinds 6,25 Mio. · #amazonhome 275k · #founditonamazon 125k | #amazonde 37k (#amazonfundstücke: n/a) | **≈180:1** |
| **Gaming-Setup** | #gamingsetup 4,07 Mio. · #desksetup 987k · #pcsetup 966k · #gamingroom 875k · #setupwars 384k | #zockerzimmer 3,6k · #gamingzimmer 0,9k (#zocken 650k, generisch) | ≈1.600:1. Deutsche Gamer nutzen englische Tags, ein eigenes DE-Ökosystem fehlt |
| **Küche** | #kitchendesign 19,2 Mio. · #kitchengadgets 229k · #kitchenhacks 148k | #küchenhelfer / #küchenideen: n/a | UNKNOWN |
| **Garten** | #garden 85,5 Mio. · #gardening 35,0 Mio. · #gardenideas 376k | #garten 8,0 Mio. · #gartenliebe 996k · #gartenideen 186k | ≈13:1 (#gardenideas:#gartenideen nur 2:1) |
| **Kaffee** | #coffeelover 31,9 Mio. · #espresso 15,4 Mio. · #homebarista 366k | #kaffee 3,5 Mio. · #kaffeeliebe 767k (#siebträger: n/a) | ≈11:1 |
| **Hund** | #dogsofinstagram 334,6 Mio. · #dogstagram 144,1 Mio. | #hund 16,7 Mio. · #hundeliebe 13,7 Mio. · #hundeleben 3,9 Mio. | ≈14:1 |
| **Katze** | #catsofinstagram 212,4 Mio. | #katzenliebe 4,4 Mio. | ≈49:1 |
| **Putzen/Haushalt** | #cleaningmotivation 806k · #cleaninghacks 558k | #putzen 143k · #haushaltstipps 4k | ≈9:1 |
| Gadgets/Produkte | #gadgets 8,1 Mio. | #produkttest 620k | ≈13:1 |

### 7.2 Content-Dichte pro adressierbarem Nutzer (eigene Berechnung)

Dichte = Hashtag-Posts ÷ Instagram-Reichweite des Sprachraums. EN-Kern = 259 Mio., DE = 36,9 Mio. Die Spalte „global“ zeigt die Sensitivität: Englische Tags werden weltweit genutzt, deshalb dort ≈1,95 Mrd. Nicht-DACH-IG-Reichweite (THIRD-PARTY-Größenordnung).

| Nische | Dichte-Verhältnis EN/DE (EN-Kern) | Dichte-Verhältnis EN/DE (global) | Lesart |
|---|---|---|---|
| Gaming-Setup | 230× | 30× | DE-Tag-Ökosystem praktisch nicht vorhanden, Messung nur bedingt aussagekräftig |
| **Amazon-Finds** | **25,6×** | **3,4×** | klare DE-Lücke |
| **Wohnen/Interior** | **19,5×** | **2,6×** | klare DE-Lücke |
| Katze | 6,9× | 0,9× | neutral |
| Hund | 2,0× | 0,3× | **DE-Community pro Nutzer ähnlich aktiv, kein Vorteil** |
| Garten | 1,9× | 0,2× | kein Vorteil |
| Kaffee | 1,6× | 0,2× | kein Vorteil |
| Putzen/Haushalt | 1,3× | 0,2× | kein Vorteil |

**Einschränkungen:** Hashtag-Posts messen alle Posts, überwiegend von Privatnutzern, nicht nur Theme-Pages. Deutsche Creator taggen oft zusätzlich englisch. Der Instagram-Algorithmus verteilt Reels interessenbasiert und nur teilweise hashtagbasiert. Englischer Content wird auch deutschen Nutzern ausgespielt, eine deutsche Page konkurriert im Feed also auch mit EN-Content.

### 7.3 Große Theme-Pages / faceless Kanäle (Indikatoren, YouTube Shorts als Proxy)

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| 57.689 vs. 380 | Faceless-YouTube-Kanäle in der NexLev-Datenbank: Englisch vs. Deutsch (≈152:1). Die Datenbank ist englisch-lastig kuratiert, daher **starker Selektionsbias** | NexLev Niche Finder (MCP-Abfrage) | 2026 | THIRD-PARTY ESTIMATE |
| 2,13 Mio. Abos / 1,91 Mrd. Views | „Justice Buys“: englischer Amazon-Finds-Shorts-Kanal. Weitere: JayFindsThings 7,77 Mio. Abos, Money Saving Man 3,93 Mio. | https://www.youtube.com/channel/UCKaWD4ZM7ixlot6ysBVKP_g | 2026 | THIRD-PARTY ESTIMATE |
| 0 von Top 20 | Bei semantischer Suche „amazon finds gadgets product recommendations“ mit Sprachfilter Deutsch findet sich **kein dedizierter deutschsprachiger Produktempfehlungs-Kanal** unter den Top 20. Treffer sind DIY-/Lifehack-/Story-Kanäle (z. B. Malerart 461k, Herr Zogg 60k) | NexLev Shorts Niche Finder | 2026 | THIRD-PARTY ESTIMATE (qualitativ) |
| ≈30.000 | deutschsprachige Influencer in DACH (**veraltet**) | https://www.goldmedia.com/studie/goldmedia-marktstudie-influencer-marketing-in-der-region-dach/ | 2018 | VERIFIED (alt) |
| – | Instagram-Creator-Zahlen DE vs. US (HypeAuditor, Upfluence) | nicht zugänglich | – | UNKNOWN |

**Qualitative Bewertung:** In der englischen Produkt- und „Amazon-Finds“-Nische gibt es mehrere Millionen-Accounts mit professioneller Serienproduktion. In deutscher Sprache sind in denselben Datenbanken keine vergleichbaren dedizierten Produkt-Theme-Kanäle sichtbar. Das ist ein Indiz, aber kein Beweis für eine Lücke auf Instagram.

---

## 8. Versand, Lieferbarkeit und Geo-Linking

| Zahl | Kontext | Quelle-URL | Jahr | Datenqualität |
|---|---|---|---|---|
| **US 41,7 % · IN 24,1 % · UK 13,9 % · CA 10,5 % · AU 9,8 %** | Zuschauer-Geo (Top-5, normiert) eines englischen Amazon-Finds-Shorts-Kanals (Justice Buys) | NexLev get_geography_revenue | 2026 | THIRD-PARTY ESTIMATE (Modell) |
| **DE 52,3 % · CH 17,8 % · AT 12,9 %** · US 9,4 % · BE 7,6 % | Zuschauer-Geo eines deutschsprachigen faceless DIY-Shorts-Kanals (Malerart) | NexLev | 2026 | THIRD-PARTY ESTIMATE (Modell) |
| **DE 52,4 % · AT 14,8 % · CH 12,3 %** · NL 10,3 % · US 10,2 % | Zuschauer-Geo eines deutschsprachigen Lifehack-Shorts-Kanals (Herr Zogg) | NexLev | 2026 | THIRD-PARTY ESTIMATE (Modell) |
| 13 Länder | Amazon OneLink: AU, CA, FR, DE, IT, JP, NL, PL, SA, SG, ES, SE, UK. **Indien nicht enthalten** | https://geniuslink.com/blog/amazon-associates-earn-globally-initiative/ | 2026 (Update) | CLAIMED |
| 6 Länder | Amazon „Earn Globally“: CA, UK, DE, FR, IT, ES über einen US-Account. Hinweis vom 27.02.2024: OneLink-Weiterleitungseinstellungen zeitweise defekt | dto. | 2024–26 | CLAIMED |
| 75 % Umsatzverlust (Beispiel) | Beispielrechnung von Geniuslink: 50 % Absprung + 25 % Tag-Verlust bei falschem Amazon-Store. Geniuslink-„Choice Pages“ sollen ≈2× EPC bringen | https://geniuslink.com/blog/recapture-amazon-affiliate-international-traffic/ | 2026 | CLAIMED (hypothetisch) |
| 47 % | Anteil der AT-Online-Ausgaben bei ausländischen Anbietern (u. a. amazon.de) | Handelsverband AT 2026 | 2026 | VERIFIED |
| 2,8 Mrd. CHF | Schweizer Online-Einkäufe im Ausland (+8 %) | HANDELSVERBAND.swiss | 2025 | VERIFIED |

**Lesart:**
- **Deutsche Sprache wirkt als Geo-Filter.** Etwa 80 % der Top-5-Zuschauer deutschsprachiger faceless Kanäle kommen aus DACH. DE und AT (≈67 %) sind direkt über amazon.de monetarisierbar, CH (12–18 %) nur teilweise (Import, Galaxus-Dominanz).
- **Englischer Content zieht Streuverluste an.** Im Beispiel entfallen nur ≈42 % auf die USA. Mit OneLink oder Geniuslink kommen UK/CA/AU hinzu (≈76 %). **≈24 % Indien bleiben praktisch unmonetarisierbar** (nicht in OneLink, Meta-CPM Indien 1,35 USD).

---

## 9. Sprache und KI-Produktion

| Aspekt | Befund | Datenqualität |
|---|---|---|
| Produktionskosten DE vs. EN | Bei KI-Pipeline (Bild/Video-Generierung, TTS-Voiceover, Captions) ist der Mehraufwand für eine zweite Sprache marginal: Text übersetzen, TTS neu rendern, Captions tauschen. Die Visuals sind identisch wiederverwendbar | ANNAHME (plausibel, nicht gemessen) |
| Voiceover DE vs. sprachneutrale (Musik/Text) Reels | Keine belastbare Studie gefunden | **UNKNOWN** |
| Indirekte Evidenz | Deutschsprachige Kanäle haben laut NexLev-Geo ≈80 % DACH-Publikum (Abschnitt 8). Eine **deutsche Tonspur bzw. Captions bündeln die Reichweite auf den monetarisierbaren amazon.de-Raum**. Sprachneutrale Reels maximieren die Reichweite, verteilen sie aber global mit Streuverlust | THIRD-PARTY ESTIMATE / Ableitung |

**Praxisfolgerung:** Beide Sprachen lassen sich parallel aus demselben KI-Asset-Pool bespielen, als zwei Accounts mit länderspezifischen Links. Die Grenzkosten der zweiten Sprache sind nahe null. Die Frage „DE oder EN“ ist deshalb eher eine Frage des **Fokus** (Account-Aufbau, Community-Management) als der Produktionskosten.

---

## 10. CPM und Monetarisierungsniveau als Kaufkraft-Proxy

| Zahl | Kontext | Quelle-URL | Zeitraum | Datenqualität |
|---|---|---|---|---|
| **23,42 USD** | Meta/Facebook Median-CPM USA (Ø 13 Monate, Peak 27,47 im Nov. 2025) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/united-states | 07/2025–07/2026 | THIRD-PARTY ESTIMATE |
| **17,38** | UK (15–16 % unter globalem Schnitt, Währung nicht angegeben) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/united-kingdom | dto. | THIRD-PARTY ESTIMATE |
| **≈14,8 (€)** | DE (28 % unter global, sehr volatil: 9,81–32,28) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/germany | dto. | THIRD-PARTY ESTIMATE |
| 13,05 / 14,38 USD | CA / AU | …/canada, …/australia | dto. | THIRD-PARTY ESTIMATE |
| **1,35 USD** | Indien | …/india | dto. | THIRD-PARTY ESTIMATE |
| 20,59 USD | Global | https://www.superads.ai/facebook-ads-costs/cpm | dto. | THIRD-PARTY ESTIMATE |
| – | YouTube-RPM nach Land | nicht abgerufen | – | UNKNOWN |

**Lesart:** Werbetreibende zahlen für einen US-Nutzer etwa das **1,6-Fache** eines deutschen und das **1,35-Fache** eines britischen, für einen indischen etwa ein Siebzehntel. Ich nutze das in der Rechnung als Obergrenze für einen „Kaufkraft-/Conversion-Uplift“ US vs. DE (×1,5).

---

## 11. Vergleichsmatrix (1 = ungünstig, 5 = günstig für eine faceless Affiliate-Theme-Page)

| Dimension | DE/DACH | US | UK | International-Englisch | Begründung | Datenqualität |
|---|---|---|---|---|---|---|
| **Marktgröße** | **2** | **5** | **3** | **5** | IG-Reichweite 38,5 / 182 / 35,5 / ≈259 Mio. (+481 Mio. IN). E-Com ≈137 / 1.234 / ≈175 Mrd. USD | VERIFIED |
| **Konkurrenz (Content)** | **4** (nischenabhängig 2–5) | **1** | **2** | **1** | Wohnen/Amazon-Finds: EN-Dichte 20–26× (Kern) bzw. ≈3× (global) höher. Hund/Garten/Kaffee: kaum Unterschied. UK teilt den EN-Content-Pool mit den USA | THIRD-PARTY ESTIMATE |
| **Anzahl großer Theme-Pages** | **4** | **1** | **2** | **1** | EN: mehrere Millionen-Accounts (z. B. Justice Buys 2,1 Mio., JayFindsThings 7,8 Mio.). DE: in der Datenbank keine dedizierten Produkt-Theme-Kanäle sichtbar | THIRD-PARTY ESTIMATE (qualitativ, Bias) |
| **Kaufkraft** | **4** | **5** | **3** | **3** | PPP/Kopf DE 74k, AT 76k, CH 102k vs. US 90k, UK 66k, IN 12k. Online-Ausgaben/Kopf DE 1.243 USD vs. US 3.545 vs. UK 2.513. CPM US 23,4 vs. UK 17,4 vs. DE ≈14,8 | VERIFIED / THIRD-PARTY |
| **Affiliate-Infrastruktur** | **4** | **5** | **4** | **3** | DE: Amazon 63 % des Onlinehandels, AT mitbedient, 16 % des E-Com via Affiliate, 932 Mio. € Markt. CH fragmentiert. US: größtes Ökosystem, Amazon 40,5 % plus Walmart u. a. UK: Creator-Markt 966 Mio. £. Intl: 6+ Amazon-Programme, Geo-Routing nötig | VERIFIED / CLAIMED |
| **Typische Provision** (Home/Küche/DIY) | **5** | **2** | **5** | **3** | DE/UK 5 % vs. US 3 % (Kitchen 4,5 %). Intl = Mix | VERIFIED |
| **Conversion-Unterschiede** | **3** | **4** | **4** | **2** | Keine direkten Affiliate-CR-Daten (UNKNOWN). Proxies: Onlineanteil DE 13,5 % vs. UK 27,5 % vs. US 16,4 %. DE-Shopper aktiv (35,2 Bestellungen/Jahr). Retouren DE hoch (fashion-lastig). Intl verwässert durch Low-CPM-Publikum | UNKNOWN / Proxy |
| **Versand/Verfügbarkeit** | **5** | **4** | **3** | **2** | DE-Sprache bündelt ≈80 % DACH-Publikum, amazon.de liefert DE+AT (CH eingeschränkt). US-Page: ≈42 % US-Anteil ohne Routing. Intl: ≈24 % IN nicht routbar | THIRD-PARTY / CLAIMED |
| **Erreichbare Reichweite** (Deckel) | **2** | **5** | **3** | **5** | Theoretische Obergrenze ≈37 Mio. (IG) / 28,7 Mio. (TikTok 18+) vs. ≈259 / 212 Mio. EN-Kern | VERIFIED |
| **Summe (ungewichtet, max. 45)** | **33** | **32** | **29** | **25** | DE punktet bei Monetarisierung pro View und Konkurrenz, EN bei Größe und Deckel | – |

*Die Summe dient nur zur Orientierung. Die Entscheidung hängt an der Gewichtung „Reichweite vs. Monetarisierung pro View“, siehe Abschnitt 12. **EU (FR/IT/ES/NL/PL/SE)** ist nicht bewertet: Jede Sprache wäre ein eigener, kleinerer Markt. Die Amazon-Programme existieren und sind laut Geniuslink über OneLink bzw. Earn Globally verknüpfbar (CLAIMED).*

---

## 12. Ableitung: Wann ist „kleinerer Markt + weniger Konkurrenz“ (DE) wirtschaftlich überlegen?

### 12.1 Rechnung A – Top-down (adressierbare Nutzer × Kaufkraft × Provision × Geo)

Potenzial = N (IG-Reichweite) × s (erreichbarer Anteil) × K (Online-Ausgaben/Kopf) × p (Provision) × g (Geo-Monetarisierbarkeit) × r (1 − Retourenverlust)

| Faktor | DACH-Page | EN-Page (US+UK-fokussiert) | Verhältnis EN/DE | Quelle |
|---|---|---|---|---|
| N × K („Markt-Index“) | 38,45 Mio. × 1.346 USD = **51,7 Mrd. USD** | 217,5 Mio. × 3.373 USD = **733,6 Mrd. USD** | **14,2×** | VERIFIED / abgeleitet |
| p (Home/Küche/DIY) | 5,0 % | 3,74 % (gewichtet: US 3,5 %, UK 5 %) | 0,75× | VERIFIED / ANNAHME Mix |
| g (Geo) | 0,73 (ohne Routing) bis 0,90 (mit Routing) | 0,42 bis 0,76 | 0,47× bis 1,04× | THIRD-PARTY / ANNAHME |
| r (Retouren) | 0,90 | 0,93 | 1,03× | ANNAHME |
| **Monetarisierbares Potenzial** | | | **≈5,2× bis 11,4×** | abgeleitet |

**Break-even:** Die DE-Page ist überlegen, wenn **s_DE ≥ 5–11 × s_EN**, also wenn sie in ihrem Markt einen 5- bis 11-mal höheren Anteil erreicht als die EN-Page in ihrem.

### 12.2 Rechnung B – Bottom-up pro 1 Mio. Reel-Views

Einnahmen = Views × CTR × CR × AOV × Provision × Geo × (1 − Retourenverlust)

| Parameter | DE-Page | EN-Page | Quelle |
|---|---|---|---|
| CTR (View → Affiliate-Klick über Bio-Link/DM/Story) | 0,3 % | 0,3 % | ANNAHME (gleich) |
| CR (Klick → Kauf) | 8 % | 8 % (Sensitivität ×1,5 = 12 %, entspricht CPM-Verhältnis US/DE) | ANNAHME |
| AOV | 53,2 € (HDE Ø pro Bestellung) | 60 USD | VERIFIED (DE-Ø allgemein) / ANNAHME |
| Provision | 5,0 % (Wohnen/Küche) | 3,5 % US; 3,775 % gemischt mit Routing | VERIFIED / ANNAHME Mix |
| Geo monetarisierbar | 0,73 / 0,90 | 0,417 / 0,759 | THIRD-PARTY (NexLev-Geo) / ANNAHME |
| Retourenabzug | 10 % | 7 % | ANNAHME |
| **Provision je 1 Mio. Views** | **474 USD** (ohne Routing), **584 USD** (mit Routing) | **196 USD** (nur US), **384 USD** (mit Routing), **575 USD** (Routing + Kaufkraft-Uplift ×1,5) | abgeleitet |

Verhältnis Monetarisierung pro View m_EN/m_DE ≈ **0,41 bis 1,21**.
Zur Ableitung: DE-Reichweite ≈ 36,9 Mio. dt.-sprachig, EN-Kern ≈ 259 Mio., also Faktor 7,0.
→ **Break-even-Anteil:** s_DE/s_EN ≥ 7,0 × (0,41…1,21) = **≈2,9× bis 8,5×**

In Views ausgedrückt ist die DE-Page überlegen, wenn Views_DE ≥ (0,41…1,21) × Views_EN. Umgekehrt darf die EN-Page höchstens das **≈0,8- bis 2,4-Fache** der DE-Views erreichen.

**Zahlenbeispiel:** Die EN-Page erreicht 3 Mio. Views/Monat, die DE-Page 1,5 Mio. Views, also nur die Hälfte der absoluten Views. Die DE-Page kommt auf ≈711–876 USD. Die EN-Page kommt auf 588 USD ohne Geo-Routing, 1.152 USD mit Routing und 1.726 USD mit Routing plus Kaufkraft-Uplift. Mit halber Reichweite schlägt DE also nur eine EN-Page **ohne** Geo-Routing. Gegen eine EN-Page mit Routing braucht DE ≈66–81 % der EN-Views, gegen eine voll optimierte EN-Page ≈98–121 %.

### 12.3 Abgleich mit der gemessenen Konkurrenz-Lücke

| Nische | Content-Dichte EN/DE (Kern … global) | Benötigter Anteilsvorteil DE | Urteil |
|---|---|---|---|
| **Wohnen/Deko/Interior** | 19,5× … 2,6× | 2,9–11× | **DE plausibel überlegen**: hohe Lücke **und** 5 % vs. 3 % Provision |
| **Amazon-Fundstücke / Haushalts-Gadgets** | 25,6× … 3,4× | 2,9–11× | **DE plausibel überlegen** |
| **Küche** (Gadgets, Helfer) | DE-Tags nicht messbar (UNKNOWN) | 2,9–11× | wahrscheinlich DE, weil Provision 5 % vs. 4,5 % und #kitchengadgets auch EN klein ist. Ungesichert |
| **Heimwerken/DIY** | nicht gemessen | 2,9–11× | DE-Provision 5 % vs. US 3 %; DE-Onlineanteil nur 7,6 %, also Aufholpotenzial. Zu prüfen |
| Gaming-Setup | 230× … 30× (DE-Tag-Ökosystem fehlt) | 2,9–11× | Lücke real, aber Provision niedrig (Konsolen/Spiele 1 %, Elektronik 2,5–3 %) und die Zielgruppe nutzt ohnehin EN-Content. Eher EN oder sprachneutral |
| Hund / Katze | 2,0× / 6,9× … ≤0,9× | 2,9–11× | **kein DE-Vorteil**; DE-Community aktiv, Provision 3 % überall gleich |
| Garten | 1,9× … 0,2× | 2,9–11× | **kein DE-Vorteil** (Garten 3 % überall) |
| Kaffee/Siebträger | 1,6× … 0,2× | 2,9–11× | **kein DE-Vorteil** bei Hashtags. Küchengeräte-Provision DE 5 % könnte das teilweise ausgleichen |

### 12.4 Bedingungen, unter denen DE überlegen ist

1. **Provisionskategorie mit DE-Aufschlag:** Möbel, Wohnen, Küche, Baumarkt/Werkzeug (5 % statt 3 %) sowie Fashion (6 % statt 4 %, aber hohe Retouren).
2. **Messbare Content-Lücke ≥3×**, auch bei globaler Betrachtung. Aktuell gilt das nur für Wohnen/Interior und Amazon-Finds.
3. **Amazon-lastiges Sortiment:** Amazon.de hält 63 % des DE-Onlinemarkts, der Link „passt“ also fast immer.
4. **Realistische Reichweitenerwartung:** Eine neue EN-Page in gesättigten Nischen erreicht höchstens das ≈0,8- bis 2,4-Fache der Views einer vergleichbaren DE-Page. Das entspricht einem Anteilsvorteil der DE-Page von 2,9–8,5× im eigenen Markt. Das ist bei starker EN-Konkurrenz und algorithmischer Kaltstart-Phase plausibel, aber **nicht gemessen**.
5. **Kein Geo-Routing verfügbar oder gewollt:** Ohne OneLink/Geniuslink verliert eine EN-Page ≈58 % des Publikums für die Monetarisierung. Eine DE-Page verliert ≈27 %.

### 12.5 Bedingungen, unter denen EN überlegen ist

- **Viral-Potenzial und Obergrenze:** Wenn Reels sprachneutral global viral gehen können, dominiert der ≈7-mal größere Nutzerpool plus höhere US-Kaufkraft.
- **Nischen ohne DE-Lücke** (Hund, Garten, Kaffee, Putzen) oder mit geringer DE-Provisionsprämie (Garten/Haustier/Spielzeug überall 3 %).
- **Diversifizierte US-Monetarisierung:** Mehrere Programme (Walmart, Brand-Programme), Creator-Ökosystem 37 Mrd. USD.
- **Langfristige Skalierung:** Die DE-Page stößt bei ≈37 Mio. deutschsprachigen IG-Nutzern an einen harten Deckel. Bei der ANNAHME von 20 % Wohn-Interesse sind das nur ≈7 Mio. Nutzer in der Nische.

**Empfehlung für die Studie:** Starte mit **DE in Wohnen/Deko bzw. „Amazon-Fundstücke für Zuhause/Küche“**, weil dort Content-Lücke und 5 %-Provision zusammenfallen. Parallel sollte ein **sprachneutrales EN-Spiegel-Account** aus denselben KI-Assets laufen (Grenzkosten ≈0) mit Geo-Routing-Links. Nach 60–90 Tagen entscheiden die tatsächlichen Views und EPC pro Markt. Das ersetzt die ungesicherten CTR/CR-Annahmen durch eigene Messwerte.

---

## 13. Datenlücken

| Lücke | Status | Auswirkung |
|---|---|---|
| TikTok-Hashtag-Views DE vs. EN (Creative Center, tiktok.com/tag) | JS/Login-geschützt, nicht abrufbar → **UNKNOWN** | Konkurrenzanalyse nur auf Instagram-Hashtags |
| Instagram-Hashtag-Zahlen | nur Drittquelle, Snapshots 10/2024–09/2026; Umlaut-Tags fehlen | Größenordnungen belastbar, Einzelwerte nicht |
| Anzahl Instagram-Creator/Theme-Pages DE vs. US (HypeAuditor, Upfluence) | nicht zugänglich; nur Goldmedia 2018 (≈30.000 DACH) | „Große Theme-Pages“ nur qualitativ bewertet |
| Affiliate-Conversion-Raten nach Land (CTR, CR, EPC) | **UNKNOWN** | Kernparameter der Rechnung sind ANNAHMEN → eigener Test nötig |
| US-Affiliate-Marktvolumen | Paywall (Statista) | Nur US-Creator-Spend (THIRD-PARTY) verfügbar |
| UK-Affiliate-Marktvolumen aktuell | nur IAB/PwC 2017 | veraltet |
| Influencer-Marketing-Markt DE aktuell | Statista-Paywall; Goldmedia 2017 veraltet | – |
| Verfügbares Haushaltseinkommen (OECD) | nicht abgerufen | Kaufkraft über BIP-PPP und Online-Ausgaben approximiert |
| YouTube-RPM nach Land | nicht abgerufen | nur Meta-CPM als Proxy |
| Amazon-Marktanteil UK | nur schwache Drittquelle (≈25 %) | – |
| US-Kategoriedaten (Census nach Branche) | nicht abgerufen | – |
| Voiceover vs. musik-/textbasierte Reels (Performance) | keine Studie gefunden → **UNKNOWN** | Nur indirekte Evidenz (Geo-Bündelung durch Sprache) |
| HDE-Onlineanteile je Branche | Zuordnung für Wohnen & Einrichten (21,6 %), CE (45,1 %), Freizeit (≈38 %) und Heimtier (26,6 %) aus PDF-Layout rekonstruiert | mittlere Sicherheit; Umsätze selbst VERIFIED |
| Deutschsprachiger Anteil Schweiz | BFS-Wert nur als Grafik, 60 % angenommen | ±0,5 Mio. Nutzer, vernachlässigbar |
| Retouren UK/US nach Kategorie; DE-Daten von 2021 | nicht aktueller verfügbar | Retourenabzug in Rechnung = ANNAHME |
| Amazon.de-Lieferung in die Schweiz (Zölle, Gebühren) | nicht verifiziert | CH-Monetarisierbarkeit auf 50 % geschätzt (ANNAHME) |

---

## 14. Quellenliste

**Plattformnutzer**
- DataReportal Digital 2026 – Germany: https://datareportal.com/reports/digital-2026-germany
- DataReportal Digital 2026 – Austria: https://datareportal.com/reports/digital-2026-austria
- DataReportal Digital 2026 – Switzerland: https://datareportal.com/reports/digital-2026-switzerland
- DataReportal Digital 2026 – United States: https://datareportal.com/reports/digital-2026-united-states-of-america
- DataReportal Digital 2026 – United Kingdom: https://datareportal.com/reports/digital-2026-united-kingdom
- DataReportal Digital 2026 – Canada / Australia / Ireland / New Zealand / India: https://datareportal.com/reports/digital-2026-canada · …-australia · …-ireland · …-new-zealand · …-india
- DataReportal Digital 2026 Mid-Year Global Update: https://datareportal.com/reports/digital-2026-mid-year-global-update-report
- W3Techs Content Languages: https://w3techs.com/technologies/overview/content_language

**E-Commerce und Händler**
- HDE Online-Monitor 2026 (PDF): https://einzelhandel.de/images/presse/Pressekonferenz/2026/onlinemonitor26/Online_Monitor_2026.pdf
- HDE Pressemitteilung 03.06.2026: https://einzelhandel.de/presse/aktuellemeldungen/15196-online-handel-als-wachstumstreiber-fuer-den-einzelhandel-marktplaetze-von-grosser-bedeutung-nutzer-werden-aelter
- bevh Jahresbilanz 2025: https://bevh.org/detail/wachstum-im-e-commerce-lichtblick-in-der-deutschen-wirtschaft
- EHI/ECDB Top 100 Onlineshops: https://www.ehi.org/news/top-100-onlineshops-in-deutschland/
- Handelsverband Österreich eCommerce-Studie 2026: https://www.handelsverband.at/publikationen/studien/ecommerce-studie-oesterreich/ecommerce-studie-oesterreich-2026/
- Handelsverband/ECDB E-Commerce-Report AT 2025: https://www.ots.at/presseaussendung/OTS_20250605_OTS0015/handelsverband-und-ecdb-praesentieren-e-commerce-report-2025-amazon-zalando-und-shop-apotheke-sind-groesste-online-haendler-in-oesterreich
- HANDELSVERBAND.swiss Onlinemarkt 2025: https://handelsverband.swiss/news/schweizer-online-konsum-waechst-im-jahr-2025-erneut-um-6-das-wachstum-der-einkaeufe-im-ausland-flacht-ab/
- US Census Quarterly Retail E-Commerce Q4 2025: https://www2.census.gov/retail/releases/historical/ecomm/25q4.pdf
- ONS Zeitreihen J4MC, JE2J, MS76, MS77: https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/j4mc/drsi (analog je2j, ms76, ms77)
- ONS Retail Sales Dezember 2025: https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/december2025
- Statista US E-Commerce-Marktanteile: https://www.statista.com/statistics/274255/market-share-of-the-leading-retailers-in-us-e-commerce/
- businesstats UK E-Commerce: https://businesstats.com/e-commerce-in-the-uk/

**Kaufkraft und Wechselkurse**
- IMF WEO DataMapper (PPPPC, NGDPDPC): https://www.imf.org/external/datamapper/PPPPC@WEO
- EZB Referenzkurse (Jahresdurchschnitt): https://data-api.ecb.europa.eu/service/data/EXR/A.USD.EUR.SP00.A

**Affiliate, Influencer, Provision**
- BVDW/APMC Affiliate-Studie 2025: https://www.bvdw.org/news-und-publikationen/apmc-studie-macht-marktpotenzial-von-affiliate-und-partner-marketing-sichtbar/
- IAB UK Value of UK Creator Partnership: https://www.iabuk.com/value-uk-creator-partnership
- IAB UK Digital Adspend: https://www.iabuk.com/adspend
- IAB UK/PwC Affiliate 2017: https://www.iabuk.com/press-release/affiliate-marketing-spend-increases-151-topping-ps550-million
- Influencer Marketing Hub Statistics: https://influencermarketinghub.com/influencer-marketing-statistics/
- Goldmedia Influencer-Marketing DACH: https://www.goldmedia.com/studie/goldmedia-marktstudie-influencer-marketing-in-der-region-dach/
- Amazon PartnerNet DE Vergütungssätze: https://partnernet.amazon.de/help/node/topic/GRXPHT8U84RAYDXZ
- Amazon Associates UK Vergütungssätze: https://affiliate-program.amazon.co.uk/help/node/topic/GRXPHT8U84RAYDXZ
- Amazon Associates US Vergütungssätze: https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ
- Amazon PartnerNet Teilnahmebedingungen: https://partnernet.amazon.de/help/operating/agreement

**Retouren**
- Uni Bamberg, Europäischer Retourentacho: https://www.retourenforschung.de/info-ergebnisse-des-europaeischen-retourentachos-veroeffentlicht.html
- NRF/Happy Returns 2025: https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025
- Transport Intelligence UK Returns: https://ti-insight.com/briefs/uk-e-commerce-growth-and-the-evolving-returns-landscape/

**Content-Konkurrenz und Geo**
- best-hashtags.com (je Tag): https://best-hashtags.com/hashtag/homedecor/ (analog für alle Tags der CSV)
- NexLev Niche Finder / get_geography_revenue (MCP-Abfragen 26.09.2026); Kanäle: https://www.youtube.com/channel/UCKaWD4ZM7ixlot6ysBVKP_g · https://www.youtube.com/channel/UCwbavnCSKqngeIqr78TNguA · https://www.youtube.com/channel/UCvDH8wB5bjZPeXb9Gmmj0RA
- Geniuslink Earn Globally/OneLink: https://geniuslink.com/blog/amazon-associates-earn-globally-initiative/
- Geniuslink International Traffic: https://geniuslink.com/blog/recapture-amazon-affiliate-international-traffic/

**CPM**
- Superads Facebook CPM Benchmarks (global + Länder): https://www.superads.ai/facebook-ads-costs/cpm und https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/{united-states|united-kingdom|germany|canada|australia|india}
