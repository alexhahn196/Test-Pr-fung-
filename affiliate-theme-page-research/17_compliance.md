# 17 – Compliance und Trust: KI darf nicht irreführen (Teil 10)

**Stand:** 26.09.2026 · Detailquelle mit wörtlichen Zitaten und 63 Primärquellen: [`quellen/G_plattform_policy_compliance.md`](quellen/G_plattform_policy_compliance.md)
**Keine Rechtsberatung.** Vor dem Start sollte eine kurze anwaltliche Prüfung von Impressum, Kennzeichnung und DM-Flow erfolgen.

## 1. Die acht Regeln, die das Geschäftsmodell direkt formen

| # | Regel | Quelle | Status | Folge für die Page |
|---|---|---|---|---|
| 1 | **Amazon: Links in DMs nur „solicited“.** *„You may include Special Links in emails, SMS and direct messaging from your social media Sites; provided, that such communications are solicited (i.e., opted into by the receiving customer)“* | Amazon Associates Program Policies US/DE/UK (Stand 14.04.2026) | VERIFIED | Comment-to-DM (Nutzer kommentiert Keyword) ist gedeckt, das ist eine Auslegung. Massen-DMs sind verboten. Ein DM pro Kommentar, kein Follow-Gate |
| 2 | **Amazon: keine veränderten Amazon-Bilder, keine Preise/Sterne ohne API, keine verschleiernden Kürzer, keine Provision auf geboostete Posts, Pinterest kein zugelassener Kanal** | Amazon Operating Agreement/Policies | VERIFIED | Produktbilder für KI-Compositing **nicht von Amazon** nehmen, sondern Hersteller-Pressebilder mit Lizenz oder eigene Fotos. Keine Preise im Video |
| 3 | **Instagram-Originalität:** Aggregatoren werden nicht empfohlen. Mehrheit der Posts in 30 Tagen muss original sein. Selbst erzeugte KI-Szenen gelten als original, Slideshows aus Händlerbildern nicht | creators.instagram.com (30.04.2026) | VERIFIED | Nur eigene Renders, keine Reposts, keine Händler-Slideshows |
| 4 | **KI-Labels:** Fotorealistische KI-Videos kennzeichnen (Meta). Seit 31.08.2026 gibt es ein Label „AI-generated profile“ für KI-Personen; fehlt es, wird das Profil nicht empfohlen | Meta (2024), creators.instagram.com (08/2026) | VERIFIED | „AI info“ setzen. **Keine KI-Person/Avatar** als Gesicht der Page |
| 5 | **EU AI Act Art. 50(4)** gilt seit 02.08.2026. „Deep fake“ umfasst realistische *„objects, places“* → fotorealistische Produktszenen offenlegen. Der Digital Omnibus (VO 2026/1744) hat nur Art. 50(2) (Anbieter-Markierung) bis 02.12.2026 verschoben | Normtext VERIFIED, Omnibus-Status THIRD-PARTY | VERIFIED/THIRD-PARTY | Sichtbarer Hinweis „KI-generierte Szene“ im Video |
| 6 | **FTC Consumer Reviews Rule (16 CFR 465) + Endorsement Guides §255.1(c):** keine Testimonials, die eine nicht existierende Person oder Nutzung vortäuschen; bis 53.088 $ pro Verstoß. UK DMCC Sch. 20, DE UWG Anhang Nr. 23c analog | eCFR (01.09.2026) | VERIFIED | **Kein „I tested it“, keine KI-Kundenstimmen.** Aussagen nur aus Datenblättern |
| 7 | **DE-Werbekennzeichnung** (Leitfaden der Medienanstalten, 05/2025): Affiliate-Link mit „*“ und Erläuterung direkt am Link. Steht das Produkt im Mittelpunkt: dauerhafte Einblendung „Werbung“; „ad“ reicht nicht. § 5 DDG: Impressum auch für faceless Accounts | Medienanstalten, BGH 2021 | VERIFIED | „Werbung“ im Video + Caption-Anfang; Impressum auf der Linkseite |
| 8 | **TikTok/YouTube:** TikTok verlangt AIGC-Label und „content disclosure setting“; wiederverwendeter Content ist nicht FYF-fähig. YouTube: „inauthentic content“ (15.07.2025) betrifft die Monetarisierung (YPP), die KI-Offenlegung *„won't limit a video's audience“* | TikTok (2026-08), YouTube Help | VERIFIED | Pro Plattform die Labels setzen; keine Template-Massenware |

## 2. Risikomatrix nach Content-Typ

| Typ | Beispiel | Gesamtrisiko | Bedingung für den Betrieb |
|---|---|---|---|
| **(a) KI-Szene + „ähnliche echte Produkte“** | KI-Wohnzimmer, darunter „Build a similar look“ | **MEDIUM** | Ausdrücklich „ähnlich, nicht identisch“ + KI-Label. Die Produkte müssen tatsächlich ähnlich sein |
| **(b) Echtes Produkt korrekt in KI-Szene** | Freisteller des echten Siebträgers in einer KI-Küche | **MEDIUM → LOW-MEDIUM bei sauberem Prozess** | Produktpixel unverändert (Freisteller), Maße, Farben und Features per QA gegen das Datenblatt geprüft, KI-Label, Bildrechte am Produktfoto |
| **(c) KI erfindet Produkt, verlinkt anderes als „dasselbe“** | KI-Sofa → beliebiges Sofa verlinkt | **HIGH – ausgeschlossen** | Täuschung über wesentliche Merkmale (UWG § 5, FTC § 5), Meta „Misleading Links“, Amazon-Vertrag |
| **(d) KI-Avatar: „I tested this and it changed my life“** | synthetische Person mit Erfahrungsbericht | **HIGH – ausgeschlossen** | per se unzulässig (FTC 465.2, UWG Anh. 23c, DMCC) |
| **(e) Slideshow aus Händler-/Amazon-Bildern** | 5 Amazon-Produktbilder mit Musik | **HIGH – ausgeschlossen** | Originalitätsregeln, Amazon-Bildlizenz, Urheberrecht |
| **(f) Vergleich/Ranking nach Datenblatt** | „3 Espressomaschinen: Druck, Boiler, Mahlwerk“ | **LOW-MEDIUM** | „laut Herstellerangaben, nicht selbst getestet“; keine „Testsieger“-Anmutung; keine Preise/Sterne |

**Betriebsregel für die empfohlene Page:** Nur die Typen **(b)** und **(f)** werden genutzt, (a) nur ausnahmsweise mit expliziter „ähnlich“-Kennzeichnung. (c), (d) und (e) sind ausgeschlossen.

## 3. Compliance-/Trust-Risiko je Nische (alle 58 Nischen der Longlist)

| Risiko | Nischen | Hauptgrund |
|---|---|---|
| **LOW** | Luxury Homes, Luxury Lifestyle, Food/Rezepte | keine Affiliate-Produkte bzw. keine Claims. Wirtschaftlich aber irrelevant |
| **LOW-MEDIUM** | Küchengeräte & Kochgeschirr, Kaffee/Espresso, Desk Setups, Gaming Setups, PC-Zubehör, Smart Home, Travel Gear, Golf, Camping, Power Stations, BBQ/Pizzaöfen, Backyard Wellness (ohne Health-Claims), Pools, Smartphone-Zubehör, Home Organization, Balkon | unregulierte Produkte. Risiken: Spec-Fehler durch KI, Preisangaben |
| **MEDIUM** | Interior/Home Decor, Möbel, Outdoor Living/Gartenmöbel, AI-Interiors, Küchengadgets (Funktionsdemos), Cleaning, Schlaf, Garten (Pflanzenschutz = MEDIUM+), Hunde, Katzen, Aquaristik, Consumer Electronics, Audio, Music, 3D-Druck, EDC (Messer), Autozubehör, Tools/DIY, Home Gym, Running, Cycling, Hiking, Sneakers, LEGO/Collectibles, Home Bar (Alkohol) | „ähnliche“ Produkte, Funktionsdarstellungen, Marken/IP, Tier-/Fitness-Claims |
| **MEDIUM-HIGH** | Tech Gadgets/Amazon Finds (KI-Funktionsdemos), Fashion, Schmuck, Uhren, Haircare, Car Detailing (Vorher/Nachher), Fotografie, Kinderzimmer, Travel Destinations | KI verfälscht Passform, Material und Details; Marken- und Fälschungsnähe; KI-Bilder realer Orte |
| **HIGH** | Skincare, Beauty Devices, Baby/Parenting, Supplements, Taschen/Luxury Resale | Wirkversprechen (Kosmetik-VO, HCVO, FTC-Substantiierung), Sicherheitsclaims, Eltern-Vertrauen, Fälschungsrisiko |

## 4. Checkliste vor dem ersten Reel (Kurzfassung, vollständig in G, Abschn. 12)

**DE**
- [ ] Gewerbe angemeldet
- [ ] Impressum und Datenschutzerklärung auf der Linkseite (DM-Tool als Auftragsverarbeiter)
- [ ] PartnerNet: Social-Accounts eingetragen; Pflichttext *„Als Amazon-Partner verdiene ich an qualifizierten Verkäufen“*
- [ ] Jedes Reel: „Werbung“ im Video und am Caption-Anfang; KI-Label; Hinweis „KI-generierte Szene“
- [ ] Jeder Affiliate-Link mit „*“ und Erläuterung (Linkseite, DM-Text)

**US**
- [ ] *„As an Amazon Associate I earn from qualifying purchases.“*
- [ ] FTC-Disclosure „clear and conspicuous“ im Video und am Caption-Anfang

**Beide Märkte**
- [ ] Keine Preise, Sterne, Rezensionszitate, Countdown-Rabatte im Content
- [ ] Keine Amazon-Bilder, auch nicht als KI-Input
- [ ] Produkt-QA gegen das Datenblatt (Farbe, Maße, Features)
- [ ] Nur „laut Hersteller“-Aussagen; kein „ich“ als Nutzer
- [ ] DMs nur auf Kommentar-Anforderung; Link parallel frei zugänglich
- [ ] Kein Boosten von Posts mit Amazon-Links
- [ ] Cross-Posting mit Labels je Plattform (TikTok AIGC + Content Disclosure; YouTube „altered or synthetic“)
