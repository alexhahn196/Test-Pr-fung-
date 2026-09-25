# Reverse-Engineering: @wellness.tips07 (USA, Rosabella-Beetroot-Netzwerk, vollständig KI)

Stand: 2026-09-24/25. Datenquellen: TikTok-Public-Data (tt_profile.sh / tt_video.sh / tt_recent.sh, Verified), TikTok-eigene ASR-Untertitel (eng-US, Verified aus SSR-JSON), Cover-/Origin-Cover-Bilder aller 10 Videos (Verified, gesichtet), öffentlicher TikTok-Kommentar-Endpoint (`/api/comment/list/`, Verified, 109 Kommentare geladen), Gerichtsakte *Human Power of N Co. v. Ambrosia Brands, LLC*, W.D. Tex. 1:26-cv-00374, First Amended Complaint 04.06.2026 (Verified Zitate; Inhalt = Claimed „on information and belief"), Produktseite tryrosabella.com (Verified 2026-09-25), Review-Seiten superfoodprofiles.com / snoopviews.com (Claimed), Bestandsdossier research/accounts/wellness.tips07.md.
**Einschränkungen:** WebSearch war nicht verfügbar (Budget 200/200); das NexLev-Watch-Tool war heute erneut 15/15 erschöpft – alle drei Watch-Versuche (826k-Video, Karussell, 179-s-Variante) wurden mit „RATE LIMIT EXCEEDED" abgewiesen. Ersatz: ASR-Untertitel mit Cue-Zeitstempeln + Cover-Bilder + Kommentar-API. Ältere Videos (126 von 136) sind für Headless-Clients nicht listbar. Kalodata/FastMoss/EchoTik-Daten zu diesem Account: **nicht öffentlich verifizierbar.**

---

## 0. Kernbefund in drei Sätzen

1. @wellness.tips07 ist ein **reiner KI-Avatar-Affiliate-Account** (Modell C/E) des Rosabella-Beetroot-Netzwerks (Ambrosia Brands LLC): ein 3-Minuten-„Fake-Patient/Behandler"-Skript, das auf die TikTok-Shop-Produktkarte („orange button down here") verkauft. Gerichtsakte ¶51/52 nennt den Account namentlich als Teil der „viral misinformation campaign" mit KI-Sprecher und KI-Label.
2. Der eigentliche Mechanismus ist **nicht** Volumen und nicht Community, sondern **Avatar-/Hook-Variantentest + Re-Upload des Gewinners**: Am 3./4.12.2025 wurden 8 Uploads desselben Skripts mit mindestens sechs verschiedenen KI-Präsentatoren (3 Männer, 2 Frauen, 2 Küchen-Sets, Wasserzeichen „AI Host") gepostet; nur die Variante „grauhaariger Mann + Reaction-PIP-Frau mit Sex-Hook" ging viral (790k), und genau diese Datei wurde am 11.12. erneut hochgeladen (826k). Die sechs anderen Varianten blieben bei 122–4.229 Views.
3. Verifizierbare Einnahmen: **keine** (keine Anchors mehr sichtbar, keine GMV-Quelle). Schätzband (Formel unten): **Spitzenmonat Dez 2025 ≈ 1.500–13.000 $ Provision, typischer Monat 2026 ≈ 0 $, Lebenszeit-Mittel ≈ 200–2.200 $/Monat** – income_confidence LOW. Seit August 2026 postet der Account produktfreie Foto-Karussells; das Modell ist faktisch eingestellt (Klage, FDA-Recall, entfernte Produktkarten).

---

## 1. Profil (Verified, tt_profile.sh 2026-09-25)

| Feld | Wert |
|---|---|
| Handle / Name | @wellness.tips07 / „Wellness Tips 🌿" |
| Bio | „All the health tips you won't find in textbooks 🤫 / Follow me ✅" – **kein Link, kein Showcase, keine Schwester-Handles** |
| Follower / Likes / Videos | 5.760 / 37.300 / 136 |
| Erstellt | 2024-07-22; alle Videos locationCreated = US |
| ttSeller / commerceUser | false / false |
| Verifiziert | nein |

---

## 2. Video-Set (10 Videos = alle über die Embed-Seite listbaren; Verified tt_video.sh 2026-09-25)

Alle 9 Videos: Caption ausschließlich Hashtags `#barbaraoneill #menshealth #womenshealth #resultsmayvary #holistichealth`, Länge 179 s oder 185 s, „original sound", aigcLabelType = „1" (Creator-KI-Label), isAd = false, adAuthorization = true (Spark-Ads-Freigabe), **anchors = [] (keine Produktkarte im Web-SSR)**, Kommentare offen (itemCommentStatus 0). Cover-Text bei allen 9: „He/She EXOSED the SECRET to get a FLAT TUMMY 😳 / Listen carefully 👂" (Tippfehler „EXOSED" in allen Varianten → eine Vorlage). Unten links auf allen Covern ein schwaches Wasserzeichen „AI Host" (Verified, Cover gesichtet; Tool-Zuordnung nicht verifizierbar).

| # | Video-ID | Upload (UTC) | Länge | Avatar-Variante (Cover, Verified) | Hook 0:00–0:04 (ASR, Verified) | Views | Likes | Komm. | Shares | Saves | Like-Rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7579753481087536397 | 03.12. 23:10 | 179 s | **Frau A** (grau-blond, Brille, grüner Cardigan, Küche) | 0:00,1 „White people are fucking lying to you, okay?" | 970 | 6 | 0 | 0 | 0 | 0,6 % |
| 2 | 7579753753973165367 | 03.12. 23:10 | 185 s | **Mann A + PIP-Reaction-Frau** (grauhaarig, Brille, dunkles Polo, weiße Küche) | 0:00,06 PIP-Frau: „Why is nobody talking about how he looks so fuckable in his 60s? Listen to what he said." → 0:04,3 Mann: „White people are fucking lying to you…" | **790.400** | 4.749 | 113 | 910 | 1.252 | 0,60 % |
| 3 | 7579754966353562893 | 04.12. 00:11 | 179 s | Frau A (grüner Cardigan, andere Küche) | „White people are fucking lying…" | 158 | 0 | 0 | 0 | 0 | 0 |
| 4 | 7579755037824404791 | 04.12. 00:12 | 179 s | **Mann B** (Glatze, Bart, schwarzes T-Shirt, graue Küche) | dito | 366 | 0 | 0 | 0 | 1 | 0 |
| 5 | 7579756276830244110 | 04.12. 02:13 | 179 s | **Frau B** (brünett, Brille, brauner Cardigan) | dito | 4.229 | 25 | 1 | 1 | 8 | 0,6 % |
| 6 | 7579756326889213239 | 04.12. 02:14 | 179 s | Mann B (Glatze, weiße Küche) | dito | 128 | 0 | 0 | 0 | 0 | 0 |
| 7 | 7579757590293269773 | 04.12. 04:14 | 179 s | Mann A ohne PIP (Küche mit rotem Wasserkocher) | dito | 122 | 0 | 0 | 0 | 0 | 0 |
| 8 | 7579758370454834446 | 04.12. 04:15 | 179 s | Mann A ohne PIP (graue Hochglanzküche) | dito | 142 | 1 | 0 | 0 | 0 | 0,7 % |
| 9 | 7581857176763763981 | 11.12. 02:16 | 185 s | **Mann A + PIP-Reaction-Frau = Re-Upload von #2** | identisch mit #2 (Cue 0:00,06–0:04,3) | **826.000** | 3.042 | 58 | 459 | 820 | 0,37 % |
| 10 | 7670209223866813709 | 04.08.2026 | Karussell 6 Bilder | Foto lächelnde Frau im Café → Collage Haut/Haare/Bauch | Slide 1: „Everything changes when you realize that…"; „Cortisol is not your enemy…" | 1.292 | 14 | 0 | 2 | 2 | 1,1 % |

Aggregat (Estimated aus Verified-Werten): Summe 1.623.807 Views; **Top-Video 50,9 %, Top-2 99,5 %** aller Views; Median 668; 7 von 9 Skript-Uploads < 5.000 Views. Zwei weitere IDs vom 11.12. (7689390677642446367, 7689390681554929182) liefern „item doesn't exist" (gelöscht/privat). Der in der Klage genannte Post vom 29.10.2025 (Arthritis/Durchblutungs-Skript, #womenhealth #health) ist nicht listbar → älterer Skript-Cluster mit anderen Hashtags.

### 2.1 Was der Variantentest zeigt (Verified Cover + Stats; Interpretation Estimated)

- **Gleiches Skript, gleicher Overlay-Text, gleiche Caption, gleiche Länge**, aber ≥ 6 verschiedene KI-Präsentatoren und 4 Küchen-Sets: klassischer Avatar-/Set-Split-Test aus einem Avatar-Tool („AI Host"-Wasserzeichen). Die ASR-Transkripte von #1 (Frau) und #9 (Mann) sind bis auf Interpunktion identisch – **die Frau sagt ebenfalls „I'm 64 … too tired to play with my kids"**, d. h. das Skript wurde nicht einmal auf das Avatar-Geschlecht angepasst.
- Einziger inhaltlicher Unterschied der Gewinner-Variante: **die 4,3 s Reaction-Hook-Einblendung** (Frau unten links, provokativer Satz „…looks so fuckable in his 60s") vor dem eigentlichen Skript. Die 179-s-Varianten starten direkt mit „White people are fucking lying to you".
- Ergebnis: 2 × ~800k vs. 6 × < 5k. Das ist kein Zufalls-Lotto, sondern ein reproduzierter Gewinner (Re-Upload nach 7 Tagen brachte erneut 826k).
- Kommentar „his left hand watch changed too" (Video #2, 4 Likes) – Zuschauer bemerken KI-Artefakte (Verified Kommentar).

---

## 3. Videoanalyse Gewinner-Video 7581857176763763981 (185 s; identisch mit 7579753753973165367)

Methode: ASR-Cues (Verified), Cover (Verified), Frames aus dem Vorlauf-Dossier (Verified), Kommentar-API (Verified). Keine NexLev-Sichtung möglich.

| Element | Befund | Tag |
|---|---|---|
| Hook gesprochen 0:00–0:04 | PIP-Frau: „Why is nobody talking about how he looks so fuckable in his 60s? Listen to what he said." | Verified (ASR) |
| Hook On-Screen 0:00 | „He EXOSED the SECRET to get a FLAT TUMMY 😳 / Listen carefully 👂" (Dauer-Overlay) | Verified (Cover) |
| 0:04–0:14 Provokation | „White people are fucking lying to you, okay? Because we age like a sack of potatoes … I'm 64, by the way" | Verified |
| 0:14–0:38 Vorher-Story | „This is what I looked like 12 months ago. I was puffy, swollen, too tired to play with my kids … anxious … couldn't sleep … craving sweets … hair started falling out … tried what my doctor told me … Nothing changed." | Verified |
| 0:38–1:00 Falsche Ursache → wahre Ursache | „It wasn't my metabolism, it wasn't my age, it wasn't my thyroid. It was my gut … stops producing something called nitric oxide" | Verified |
| 1:00–1:35 Angst-Eskalation | „Here's the terrifying part … Your vessels harden, your organs suffocate, your inflammation becomes permanent until one day it's sadly too late to reverse the damage." | Verified |
| 1:35–1:55 Autorität + Social Proof | „a natural healer I've been recommending for years … Three weeks later, they come back in tears, thanking me" | Verified |
| 1:55–2:10 Enthüllung + Zahl | „Just one teaspoon of this food can reduce gut inflammation 73% more than turmeric and ginger combined … This ancient remedy is called beetroot." | Verified |
| 2:10–2:30 Differenzierung | „Not all beetroot is created equal … cheap fillers … pesticides … You just bought the wrong one … must be third party tested by independent U.S. laboratories." | Verified |
| 2:30 Produkt-Nennung | „**Rosabella beetroot is the only one I recommend** … one ingredient, 100% pure … no fillers" | Verified |
| 2:46–2:56 Social Proof + Preis + Knappheit | „Over 200,000 people bought it … Usually $39 a bottle. But right now, three bottles for the price of one, thanks to the Christmas sale. The problem? They keep selling out." | Verified |
| **CTA 2:58–3:05** | „**If there's an orange button down here, they might have a few bottles left. Hurry**, because when they sell out, my clients waited months to find them again." + rote Pfeile nach unten links ab ~2:30 (Frames, Vorlauf-Dossier) | Verified |
| Produktdarstellung | **Kein Packshot, kein Hands-on, keine B-Roll, kein Vorher/Nachher-Bild** – Produkt wird nur genannt; der Kauf-Impuls hängt komplett an der Shop-Karte | Verified (Cover/Frames) |
| Sprecher | KI-Avatar (Lip-Sync auf Personen-Clip): grauhaariger Mann ~60, Brille, dunkles Polo, weiße Küche, statisches Framing über 185 s; „AI Host"-Wasserzeichen; TikTok-Feld aigcLabelType = 1; Klage ¶51 „AI-generated speaker" | Verified (Label/Cover) / Claimed (Klage) |
| KI-Avatar konsistent? | **Nein** – 6+ Avatare im selben Skript-Batch; keine Serienfigur | Verified |
| Voiceover | synthetische Stimme, ruhiger „Behandler"-Ton, exakt am Skript (ASR ohne Füllwörter) – Audio-Forensik nicht möglich | Claimed (KI-Label) |
| Captions | wortweise Untertitel weiß/cyan, mittig unten; Dauer-Overlay oben in Schwarz-auf-Weiß-Box | Verified (Frames/Cover) |
| Musik | keine („original sound") | Verified |
| Schnitte / Szenen | 1 Szene, 0 Schnitte; PIP-Overlay 0–4 s | Verified |
| Stock / UGC / echte Produkt-Clips | keine | Verified |
| Sichtbares KI-Label / Shop-Karte / Commission-Badge | KI-Label wird von TikTok als UI aus aigcLabelType gerendert (Klage bestätigt Sichtbarkeit in der App); **Shop-Karte heute nicht mehr angehängt** (anchors = []); Commission-Badge nicht verifizierbar | Verified / Nicht verifizierbar |

### 3.1 Kommentar-Reaktion (Verified, /api/comment/list/, 109 Kommentare geladen)

- Video #2 (790k, 113 Komm.): Top-Kommentar „What kids are you playing with at 64?" (70 Likes, 9 Antworten) – der ungeprüfte Skript-Satz wird zum Meme. Weitere: „Used for 3 months, doesn't work" (8), „People will believe anything lol" (8), „his left hand watch changed too" (4, KI-Artefakt), „I don't think we needed to bring race into this" (3), „Is this FDA approved?" (3), „Best TikTok opening line ever 👏👏👏" (2), „Doesn't work" (0). Kaufabsicht: „I will give it a try!" (1), „marilyn67070: Iv been doing this for months have not lost weight but my blood pressure is awesome" (0).
- Video #9 (826k, 58 Komm.): „Says he's been saying this for years yet he shows a picture of him 12 months ago…" (14, 3 Antworten), „Genetics are a huge factor" (12), „If that was you 12 months ago, how could you be recommending this product for years. Who writes this stuff?" (4), „what gets me it's only on tictoc and it cost billions to get it.bull." (6), „What's he selling" (2), „Just get to the point" (2). Kaufabsicht: „beet root I will try for sure" (1), „Is it ok to take for people with high iron?" (1).
- **Auffällig:** Auf beiden Videos je 20–30 Kommentare aus reinen Dreifach-Emojis (😳😳😳, 🥰🥰🥰, 😁😁😁, ❤️❤️❤️) von generischen Usernamen mit 0–1 Likes – Muster von Engagement-Seeding/Bot-Kommentaren (Estimated; nicht beweisbar).
- Zeitfenster: Kommentare vom 08.12.2025 bis 23.03.2026 (Video #2) bzw. 11.12.2025 bis 26.02.2026 (#9) – die Reichweite lief ca. 3 Monate, nicht nur 48 h → spricht für Spark-Ads-Boost (adAuthorization = true) oder Long-Tail-FYP (Estimated).
- Fazit Social Proof: **überwiegend Pushback/Spott** (Logikfehler im Skript, Race-Bait, „doesn't work", „AI-Artefakt"), nur vereinzelt Kaufabsicht; kein einziger „I bought it and it works"-Kommentar.

### 3.2 Karussell 7670209223866813709 (04.08.2026, 6 Bilder, Musik „Simple Life")

Produktfrei: Slide 1 lächelnde Frau im Café „Everything changes when you realize that…", dann Collage Haut/Haare/Bauch „This is what happens when your cortisol levels stays high for too long / Here's 3 simple ways to lower your cortisol levels" (Verified Bilder aus Vorlauf-Dossier). Kein Anchor, kein KI-Label (ShowAIGC = true), 1.292 Views. Hashtags #cortisol #womenshealth #healthylifestyle. → Pivot zu KI-Bild-Slideshows ohne Produkt.

---

## 4. Offer

| Feld | Befund | Tag |
|---|---|---|
| Produkt | Rosabella Organic Beetroot Capsules, 1.300 mg, 60 Kapseln/30 Tage; Marke von Ambrosia Brands LLC (New York); Weißlabel-Produkt (Review: baugleich „Valora" u. a., Herstellung China) | Verified (tryrosabella.com) / Claimed (snoopviews) |
| Preis | Website 2026-09-25: 34,99 $ (durchgestrichen 49,99 $, „SAVE 30%"), 90-Tage-Geld-zurück; Klage ¶21: 39,95 $ bzw. 35,96 $ Abo, „sometimes as low as $10 per container" im TikTok Shop; Video: „Usually $39 a bottle … three bottles for the price of one" | Verified / Claimed |
| Rabatt/Coupon | kein Code; Knappheit + „Christmas sale 3-für-1" im Skript; Website-Default = Abo (Auto-Refill) | Verified |
| Provision | **Nicht öffentlich verifizierbar.** Klage ¶66/68/95: Provision + „direct bonuses" + Redirect-Links; Netzwerk-Benchmark neue Supplement-Marken 20–30 % (claims_analytics_official.md); Netzwerk-Claim ¶72: „~$400,000 last month to creators", ein Creator 317.710 $ | Claimed / Estimated |
| Impulskauf-Potenzial | hoch: 35–40 $-Ticket, Gesundheitsangst, 3-für-1, „sell out"-Knappheit, Ein-Klick-Shop-Karte | Estimated |
| Problem/Lösung | Bauchfett/Bloating/Müdigkeit/Haarausfall → „Gut-Inflammation durch fehlendes Nitric Oxide" → Beetroot → nur Rosabella ist „rein/third-party-tested" | Verified (Skript) |
| Zielgruppe | US-Frauen und -Männer 50+ (Sprecher „64", Hashtag #barbaraoneill = Alt-Health-Community, Kommentatoren nennen sich „60/62/64") | Verified (Kommentare) / Estimated |
| Risiko | FDA-Recall (Salmonella), 348 BBB-Beschwerden, 1.005 negative Trustpilot-Reviews (Abo-Fallen), Lanham-Act-Klage; Skript mit unbelegten Zahlen („73 % more than turmeric and ginger", „200,000 people") | Claimed (superfoodprofiles) / Verified (Klage) |

---

## 5. Distribution

| Kanal | Befund | Tag |
|---|---|---|
| Organisch FYP | Hauptkanal: 2 Ausreißer à ~800k, Like-Rate 0,37–0,6 % (sehr niedrig für 3-Min-Content), Kommentare über 3 Monate verteilt | Verified Stats / Estimated |
| Paid/Spark | adAuthorization = true bei allen 9 Skript-Videos (Creator hat Ad-Nutzung freigegeben); isAd = false im organischen Listing. Ob Ambrosia die Gewinner als Spark Ads geboostet hat: nicht verifizierbar, aber plausibel (bimodale Verteilung, 3-Monats-Kommentarfenster) | Verified Feld / Estimated |
| Suche/Hashtags | Caption = nur Hashtags, keine Produkt-Keywords → kein Produkt-Suchtraffic; #barbaraoneill (Hashtag-ID 1690241293380614) zielt auf die Alt-Health-Community 50+; #resultsmayvary = Disclaimer-Tag | Verified |
| Shop-Tab | keine Anchors mehr → aktuell 0 Shop-Tab-Traffic; zum Zeitpunkt Dez 2025 lt. Skript Produktkarte vorhanden | Verified / Claimed |
| Anteil Top-Video | 50,9 % (Top-2: 99,5 %) | Estimated |
| Posting-Volumen | 136 Videos / 26 Monate ≈ 5,2/Monat, aber stoßweise: 8 Uploads in 5 h (03./04.12.), 1 Re-Upload 11.12., danach bis Aug 2026 nur Karussell in der Stichprobe | Verified/Estimated |
| Varianten | **ja, systematisch**: 1 Skript × ≥ 6 Avatare × 4 Sets; Gewinner re-uploadet | Verified |
| Schwester-Accounts | keine Handles in Bio/Captions; instagram.com/wellness.tips07 → HTTP 429 (nicht verifizierbar); youtube.com/@wellness.tips07 → 404 (nicht existent); Bing „wellness.tips07" → keine Treffer. Netzwerk-Geschwister lt. Klage: @badobadi86 (53.400 Follower, 678 Videos, kein KI-Label, Body-Butter/Skincare/„cleannutra"-Videos, Verified), @poormaninla, @trinibof8dl; Skript-Quelle für Harry-Chang-Fall: @liverboosthub11 (2.668 Follower, 137 Videos – gleiche Größenordnung wie wellness.tips07) | Verified / Claimed |
| Crossposting | nicht nachweisbar | – |

---

## 6. Wettbewerbsvorteil – was funktioniert wirklich?

**Bewertung: Kombination aus (a) fremdem Skript/Coaching + (b) Avatar-Split-Test mit Re-Upload des Gewinners + (c) Sex/Race-Bait-Reaction-Hook + (d) Fear-Selling auf ein Impulsprodukt mit Shop-Karte.** KI ist dabei nur der Kostensenker, nicht der Vorteil.

| Faktor | Evidenz | Stärke |
|---|---|---|
| Skript + Coaching vom Brand (10-h-Kurs, Skripte, Messaging-Guides, Discord) | Klage ¶68 (Claimed); Skript identisch über alle Varianten, Vorlage-Tippfehler „EXOSED" | mittel–hoch |
| Avatar-/Set-Variantentest, Winner-Re-Upload | 8 Uploads in 5 h, 6+ Avatare, Gewinner 2× ~800k, Verlierer < 5k | **hoch (Verified)** |
| Reaction-PIP-Hook mit Provokation | nur die PIP-Variante ging viral; Kommentar „Best TikTok opening line ever" | hoch (Verified, n = 2) |
| Fear-Selling-Struktur (Fehldiagnose → „organs suffocate" → Enthüllung → Knappheit) | ASR-Transkript | hoch (Verified) |
| Produktwahl: 35–40 $-Supplement mit 3-für-1, Auto-Abo, hoher Provision | Klage ¶21/72, Website | mittel (Claimed) |
| Cheap Production | 1 Szene, 0 Schnitte, keine B-Roll, KI-Avatar-Tool mit Wasserzeichen | hoch (Verified) |
| Volumen | nein – 136 Videos in 26 Monaten, 5.760 Follower | niedrig |
| Community/Follower | nein – Reichweite ohne Follower-Aufbau | – |
| Nachhaltigkeit | negativ: Pushback in Kommentaren, Klage, Recall, Produktkarten entfernt, Pivot zu produktfreien Slideshows | – |

Evidenz-Rating gesamt: **MEDIUM** – Mechanik und Reichweite sind verifiziert, Vergütung und Boost-Einsatz nur Claimed/Estimated.

---

## 7. Einkommensschätzung (alles Estimated; keine GMV-Quelle → „Nicht öffentlich verifizierbar")

Formel: Einnahmen = Views × CTR (Shop-Karte) × CVR × Warenkorb × Provision.
Inputs: CTR 1–3 % (3-Min-Fear-Sell, Pfeile auf Karte), CVR 3–8 % (Impuls-Supplement), Warenkorb 30–40 $ (Klage: 39,95 $ Liste, TikTok-Shop-Aktionen bis 10 $; Skript „3 für 1"), Provision 15–25 % (Supplement-Neumarke; Rosabella-Satz nicht öffentlich). Plausibilitätsanker aus dem Benchmark-File: 4–5 $ GMV/1k Views (gut laufende Affiliate-Kampagne) bis 13–54 $ GMV/1k Views (Top-Creator).

| Szenario | Views | Bestellungen | GMV | Provision |
|---|---|---|---|---|
| Spitzenmonat Dez 2025 (2 Gewinner, 1,616 Mio. Views) – konservativ (1 % × 3 % × 30 $ × 15 %) | 1,62 Mio. | ~485 | ~14.500 $ | **~2.200 $** |
| Spitzenmonat – Mittel (2 % × 5 % × 35 $ × 20 %) | 1,62 Mio. | ~1.620 | ~56.700 $ | **~11.300 $** |
| Spitzenmonat – Benchmark-Anker 5–40 $ GMV/1k × 20 % | 1,62 Mio. | – | 8.100–64.600 $ | **1.600–12.900 $** |
| Typischer Monat 2026 (Median 668 Views × 5 Posts) | ~3.400 | 0–3 | < 100 $ | **< 25 $** |
| Lebenszeit (37.300 Likes ÷ 0,5 % Like-Rate ≈ 7 Mio. Views; 5–40 $ GMV/1k × 20 %) | ~7 Mio. | – | 35.000–280.000 $ | **7.000–56.000 $ kumuliert ≈ 270–2.150 $/Monat über 26 Monate** |

**Band: Spitzenmonat 1.500–13.000 $, typischer Monat ≈ 0–25 $, Lebenszeit-Mittel ≈ 200–2.200 $/Monat.** income_confidence = **LOW** (CTR/CVR reine Annahmen; ob die Produktkarte während der viralen Phase aktiv war, ist nur aus dem Skript ableitbar; Boost-Kosten unbekannt; Kommentare zeigen kaum Kaufabsicht).

---

## 8. Übertragbarkeit / Lehren

- Replizierbar ist nur die **Methode** (1 Skript → n Avatare/Sets → 24-h-Test → Gewinner re-uploaden, ggf. boosten); nicht replizierbar sind Skript und Produkt: unbelegte Health-Claims, fiktive Behandler-Autorität, Race-/Sex-Bait – in den USA bereits Gegenstand einer Lanham-Act-Klage, in DE/EU Verstoß gegen Health-Claims-VO, UWG und TikTok-Shop-KI-Disclosure-Regeln; Supplements sind in der EU zusätzlich TikTok-Shop-restriktiv.
- Der Account zeigt das typische Ende dieses Modells: Produktkarten verschwinden (Sperre/Recall/Klage), Reichweite bricht auf < 1.500 Views ein, Pivot zu produktfreiem Content, 5.760 Follower bleiben wertlos.

---

## 9. Quellen (Abruf 2026-09-24/25)

- https://www.tiktok.com/@wellness.tips07 · https://www.tiktok.com/embed/@wellness.tips07
- Videos: https://www.tiktok.com/@wellness.tips07/video/7581857176763763981 (826k; ASR sub_7581857176763763981.vtt; Cover cover_7581857176763763981.jpg), …/7579753753973165367 (790k), …/7579753481087536397 (179-s-Frau-Variante; sub_7579753481087536397.vtt), …/7579754966353562893, …/7579755037824404791, …/7579756276830244110, …/7579756326889213239, …/7579757590293269773, …/7579758370454834446, …/7670209223866813709 (Karussell). Cover-Grid: scratchpad/covers_grid.jpg
- Kommentare: https://www.tiktok.com/api/comment/list/?aweme_id=7581857176763763981 und …=7579753753973165367 (cm_*.json)
- Gerichtsakte: https://storage.courtlistener.com/recap/gov.uscourts.txwd.1172890758/gov.uscourts.txwd.1172890758.14.0_3.pdf (¶21, ¶47–52, ¶64–72, ¶95; lokal research/product_side/humann_manual.txt)
- https://tryrosabella.com/ (Preise) · https://superfoodprofiles.com/rosabella-beetroot-scam · https://snoopviews.com/rosabella-beetroot-review/
- Netzwerk: https://www.tiktok.com/@badobadi86 (tt_profile/tt_video) · research/claims_analytics_official.md (Benchmarks, Harry-Chang/liverboosthub11-Fall)
- Nicht erreichbar: instagram.com/wellness.tips07 (429), youtube.com/@wellness.tips07 (404), amazon.com (503), tryrosabella.com/pages/affiliate (404); NexLev watch_tiktok_video_and_ask 15/15 (3 Versuche abgewiesen)
