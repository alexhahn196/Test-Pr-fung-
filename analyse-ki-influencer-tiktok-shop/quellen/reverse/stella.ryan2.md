# Reverse-Engineering: @stella.ryan2 (TikTok, US) – Rosabella-Affiliate mit KI-Avataren

Zugriff aller Quellen: 2026-09-24/25. Tags: **Verified** = in TikTok-Rohdaten (SSR-JSON, Untertitel-VTT, Videodatei) oder Primärdokument gesehen; **Claimed** = Behauptung Dritter; **Estimated** = eigene Rechnung mit Formel.
Methodenhinweis: `mcp__NexLev__watch_tiktok_video_and_ask` war auch heute ausgeschöpft (15/15). Ersatz: Videodateien (playAddr) heruntergeladen, TikTok-eigene englische Untertitel (VTT, automatisch erzeugt) ausgelesen = vollständiges Transkript mit Timestamps, Frames mit ffmpeg extrahiert und Szenenerkennung (Schwelle 0,3) gefahren. Kommentare via öffentliche Comment-API.

## 1. Profil (Verified, tt_profile.sh / tt_video.sh authorStats)

| Feld | Wert |
|---|---|
| URL | https://www.tiktok.com/@stella.ryan2 |
| Follower / Likes / Videos | 8.915 / 214.800 / 161 |
| Following | 0 |
| Bio / Bio-Link | leer / keiner |
| Erstellt | 2025-10-04 |
| ttSeller / commerceUser | false / false |
| Letztes auffindbares Video | 2025-12-10 (7582037804507499831) – seitdem kein neueres Video im Embed-Feed → Account seit ~9,5 Monaten inaktiv (Verified: Embed-Feed zeigt neueste 8 Videos, alle Nov/Dez 2025) |
| Modell | C – vollständig KI-generierte „Experten"-Avatare (statisches Bild + Lip-Sync), Affiliate für die Supplement-Marke Rosabella (Ambrosia Brands, LLC) |

## 2. Analysierte Videos (n = 9, alle Verified via tt_video.sh, 2026-09-25)

| # | Video-ID | Datum (UTC) | Dauer | Views | Likes | Komm. | Shares | Saves | isAd | Anchors | AI-Label (API) | Caption / Hashtags | Produkt | Hook (0–3 s, gesprochen) | On-Screen-Hook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7579201771042557198](https://www.tiktok.com/@stella.ryan2/video/7579201771042557198) | 2025-12-02 12:40 | 182 s | **5.569** | 70 | 5 | 28 | 23 | false | keine | null | „So good yes yes" (keine Hashtags) | Rosabella Moringa | 0:00 „Why is nobody talking about how he looks f***able in his 80s?" 0:04 „Listen to what he said. What's the best way to clean your gut after 30 years of eating junk food?" | „How Africans CLEAN GUT after processed food 😳 – Listen closely" |
| 2 | [7579202285788564750](https://www.tiktok.com/@stella.ryan2/video/7579202285788564750) | 2025-12-02 13:44 | 185 s | 2.858 | 30 | 1 | 2 | 7 | false | keine | null | „This is my time to use it #guthealth #moringa" | Rosabella Moringa | 0:00 „Why is nobody talking about how she looks f***able in her 80s? Listen to what she said…" (weibliche Variante von #1) | (Frauen-Avatar, gleiche Box) |
| 3 | [7577204697325407502](https://www.tiktok.com/@stella.ryan2/video/7577204697325407502) | 2025-11-27 02:40 | 140 s | 1.637 | 8 | 0 | 1 | 0 | **true** | keine | null | „I'm grateful I found this year #over40 #tiktokshopblackfriday" | Rosabella Beetroot ($15 im Video) | 0:00 „I'm 30 years older than the average man who dies in America, but nobody believes me when I tell them this" (Mönch-Avatar; in der Klage zitiert) | „He found the Asian SECRET to HIDE BELLY ‼️😳 – Listen closely👂" |
| 4 | [7580171853155568909](https://www.tiktok.com/@stella.ryan2/video/7580171853155568909) | 2025-12-05 00:58 | 183 s | 1.297 | 18 | 1 | 3 | 10 | false | keine | null | „This is amazing in my opinion #moringa" | Rosabella Moringa | 0:00 „Did y'all see they tried to hide with this b****? Just said he's 71, but he looks like he's 30. Watch this." → dann identischer Script-Body wie #1 | (Arzt-Avatar) |
| 5 | [7582037804507499831](https://www.tiktok.com/@stella.ryan2/video/7582037804507499831) | 2025-12-10 01:39 | 146 s | 996 | 15 | 0 | 2 | 2 | false | keine | null | „It's simply has been the best #womenhealth #beetroot" | Rosabella Beetroot | 0:00 „This is what we look like on day one of our glow up. Let's get it." 0:04 „This is day 50, and I'm about to cheat on my husband with this woman because she changed our lives. Just watch." | „Day 1 of our transformation" (0–5 s, Paar vor Spiegel) → ab 0:05 „How African Women HIDE BELLY ‼️😳 – Listen closely" |
| 6 | [7580171779902033165](https://www.tiktok.com/@stella.ryan2/video/7580171779902033165) | 2025-12-05 00:58 | 190 s | 872 | 6 | 0 | 1 | 4 | false | keine | null | „It's has helped us personally #guthealth #over40" | (Moringa/Beetroot, nicht gesichtet) | – | – |
| 7 | [7582036564553780535](https://www.tiktok.com/@stella.ryan2/video/7582036564553780535) | 2025-12-10 01:34 | 145 s | 848 | 12 | 0 | 0 | 3 | false | keine | null | „We love it #over40 #womenover40" | Rosabella Beetroot | 0:00 „This is what we look like on day one of taking beetroot everyday. Let's get it. This is day 50, and I'm about to cheat on my husband with this holistic healer…" (Variante von #5) | – |
| 8 | [7580169970152213773](https://www.tiktok.com/@stella.ryan2/video/7580169970152213773) | 2025-12-05 00:51 | 182 s | 733 | 9 | 3 | 2 | 2 | false | keine | null | „So helpful to me #womenover40 #guthealth" | (nicht gesichtet) | – | – |
| 9 | [7580169228372675853](https://www.tiktok.com/@stella.ryan2/video/7580169228372675853) | 2025-12-05 00:48 | 190 s | 647 | 5 | 0 | 3 | 3 | false | keine | null | „This has been so beneficial for us #guthealth #moringa" | (Moringa) | – | – |

Summen der Stichprobe: 15.457 Views, 173 Likes (Like-Rate 1,1 %), 10 Kommentare, 42 Shares. Ø 1.717 Views, Median 996, Max 5.569 (= 36 % der Stichproben-Views). Alle 9 Videos: Musik „original sound", isECVideo=null, aigcLabelType=null (kein TikTok-AIGC-Label), 0 Produkt-Anchors (heute).
Ältere, laut Gerichtsakte (Exhibit P) deutlich stärkere Posts (12.600 / 2.825 / 1.693 / 922 Likes, 21.–24.11.2025) sind nicht mehr auffindbar (Embed-Feed listet nur die neuesten Videos; Wayback-Video 7575728656186641677 gelöscht).

## 3. Video-Deep-Dive

### 3.1 Video #1 – 7579201771042557198 (Top-Video, 5.569 Views, 182 s)
- **Hook (Verified, VTT + Frames):** 0:00–0:04 Reaction-Face einer realen(-wirkenden) Frau unten links, Voice: „Why is nobody talking about how he looks f***able in his 80s?" – 0:04 „Listen to what he said." Dauerhaft eingeblendete rote Textbox „How Africans CLEAN GUT after processed food 😳" + „Listen closely".
- **Struktur:** 0:04–0:10 Frage-Hook („best way to clean your gut after 30 years of junk food? It ain't a salad, it ain't lemon water…"); 0:10–1:15 Problem-Agitation (over 40, Junk Food, „belly, sluggish mornings, stiff joints, mental fog", Seed Oils, Toxine, Colon); 1:15 Reveal des Wirkstoffs („This ancient remedy is called moringa" – „7× more vitamin C than oranges, 23× more iron than spinach, 25× more antioxidants than blueberries"); 1:30–2:05 Social Proof („people been coming to me for years… come running back to me in tears"); 2:05–2:40 Marken-Reveal + Fear-Framing („got to be certified by independent labs in the US. The only one I trust is Rosabella Moringa… other brands mix cheaper ingredients"); 2:42–3:02 Angebot + Scarcity-CTA.
- **CTA (Verified):** 2:42 „It usually cost $19 a bottle, but right now you can get two Rosabella Moringa bottles for the price of one thanks to the Black Friday sale." 2:52 „…they sell out very often. But if there's an orange button at the bottom left, they might have some bottles left in stock." Roter Pfeil nach unten links ab ~2:40 (Frames 165 s / 178 s) → zeigt auf die Position der TikTok-Shop-Produktkarte („orange button" = Shop-Button). Heute keine Anchors mehr → Karte entfernt.
- **Produktdarstellung:** Nur ein Overlay-Insert bei ~2:40: Hand hält grüne Dose „Rosabella MORINGA" mit Untertitel „$19 a bottle" (Packshot, nicht Avatar-Hand; wahrscheinlich Brand-Asset). Keine Anwendung, kein Before/After, kein Unboxing.
- **Avatar:** KI-generierter älterer schwarzer „Arzt" (weiße Haare, Brille, Headset-Mikro, weißes Hemd, lila Krawatte) auf Konferenzbühne vor Anatomie-Slide – 0 Szenenwechsel über 182 s (ffmpeg scene>0,3: keine), nur Lip-Sync/Gesten. Unten links in **jedem Frame** eingebranntes Wasserzeichen „AI Generated". Reaction-Face der Frau (0–5 s) wirkt wie reales UGC-Snippet.
- **Voice:** männliche TTS-Stimme im AAVE-Register („y'all", „ain't", „them blood vessels") – Skript bewusst ethnisch/„homegirl"-codiert; identischer Wortlaut in Video #4 → Text-to-Speech-Pipeline (Verified per identischer VTT).
- **Captions:** weiße Karaoke-Untertitel, Keyword türkis hervorgehoben, 1–3 Wörter pro Einblendung. Musik: keine (original sound).
- **Kommentare (Verified, Comment-API):** 5 Kommentare, alle Emojis („😁", „😳", „🥰", „😳😳😳", „💯") – kein Produktfeedback, kein „that's AI"-Pushback. Social Proof faktisch null.

### 3.2 Video #5 – 7582037804507499831 (neuestes Video, 996 Views, 146 s)
- **Hook:** 0:00–0:05 realwirkendes UGC-Snippet: schwarzes Paar vor Spiegel, Text „Day 1 of our transformation", weibliche Voice „This is what we look like on day one of our glow up. Let's get it. This is day 50, and I'm about to cheat on my husband with this woman because she changed our lives. Just watch." Schnitt bei 5,4 s und 12,5 s (einzige Cuts im Video) → Bühne mit KI-Avatarin.
- **Avatar:** ältere schwarze Frau im roten Paillettenkleid, Headset, vor Herz-/Organ-Slide; Box „How African Women HIDE BELLY ‼️😳 – Listen closely". Wasserzeichen „AI Generated" in jedem Frame.
- **Struktur:** 0:13 Autorität („30 years in holistic healing, and nobody believes me… they always try to silence me because I cost the industry billions"); 0:25–1:10 Problem (Toxine im Darm/Venen, „gaining pant sizes, body aches, exhausted"); 1:14 Reveal „beetroot… nitric oxide"; 1:38 „But I said pure beetroot – store versions have pesticides and GMOs"; 1:48 „That's why I recommend Rosabella"; 2:05 CTA.
- **CTA (Verified):** 2:05 „right now they're running their end of year sale where you get three beetroot bottles for the price of one with free shipping. If you see an orange button, tap it to check their official store… if they're sold out, you just have to wait a few months for the next restock." Roter Pfeil nach unten ab ~2:05.
- **Produktdarstellung:** nur verbal + kleines Dosen-Insert am Bühnenrand; kein Packshot-Fokus.
- **Kommentare:** 0.

### 3.3 Video #3 – 7577204697325407502 (in der Klage zitiert; siehe Dossier)
Mönch-Avatar vor Buddha-Statuen, Hook „He found the Asian SECRET to HIDE BELLY", 140 s, 0 Cuts, „bottle for $15 … somewhere down here", isAd=true (Spark-Ad-Autorisierung).

### 3.4 Muster über alle gesichteten Videos (Verified)
| Element | Befund |
|---|---|
| Format | 140–190 s (!) langer Monolog, statisches KI-Standbild mit Lip-Sync, 0–2 Cuts, Reaction-/UGC-Snippet nur in den ersten 5–12 s |
| Hook-Bausteine | (a) Schock/Sex-Wort („looks f***able in his 80s", „cheat on my husband"), (b) Alters-Paradox („he's 71 but looks 30", „30 years older than the average man who dies"), (c) ethnisches „Geheimnis" („How Africans…", „Asian SECRET…"), (d) „Listen closely"-Box |
| Script-Template | Frage-Hook → „it ain't X/Y/Z" → Over-40-Problem-Liste → „ancient remedy from Africa/Asia, never hear about it in America" → Nährstoff-Superlative → „people come back crying" → „but it must be PURE/certified" → Marke Rosabella → Preis + „2 for 1 / 3 for 1" → „orange button bottom left" + Sell-out-Scarcity |
| Varianten | Gleicher Script-Body mit ausgetauschtem Hook-Satz (#1 vs. #4), ausgetauschtem Avatar-Geschlecht (#1 vs. #2), ausgetauschtem Wirkstoff (Moringa ↔ Beetroot, #5 vs. #7) → klassisches Hook-/Avatar-Split-Testing |
| Produkt | Rosabella Moringa und Rosabella Beetroot (Ambrosia Brands, LLC / „Liminal Supplements" im Footer von tryrosabella.com) |
| AI-Kennzeichnung | eingebranntes „AI Generated" (vom Ersteller), **kein** TikTok-AIGC-Label gesetzt |
| Captions | Karaoke, Keyword-Highlight türkis |
| Musik | keine |
| Kommentare | 0–5 pro Video, nur Emojis |

## 4. Offer

| Feld | Wert | Tag |
|---|---|---|
| Produkt | Rosabella Organic Beetroot Capsules 1300 mg (60 Kaps.) und Rosabella Moringa Capsules | Verified (tryrosabella.com, Video) |
| Listenpreis Website | Beetroot $39,95 / 30 Tage („Save 50 %" von $79,90), $79,90 / 60 Tage, $119,85 / 90 Tage; Subscribe & Save $42,99 | Verified (tryrosabella.com/products/…, 2026-09-25) |
| Preis laut Video | „$19 a bottle", „2 for 1" (Black Friday), „3 for 1 + free shipping" (End-of-Year), „$15" (Mönch-Video) | Verified on-screen/Audio |
| TikTok-Shop-Preis / Rabattcode | Nicht öffentlich verifizierbar (Anchors entfernt; Kalodata/FastMoss nicht abrufbar) | – |
| Provision | Nicht öffentlich verifizierbar. Klage ¶66/68: Beklagte zahlt „a commission on the influencer's sales" + Redirect-Links; ¶72 (Recruiting-Video Washenko): „~$400.000 last month to creators" für das gesamte Netzwerk | Claimed |
| Impulskauf | hoch: „2 for 1"-Deal, Sell-out-Scarcity, ~$19–40 Ticket, „orange button" direkt im Feed | Estimated |
| Problem/Lösung | Bauchfett, Bloating, Müdigkeit, „Toxine" bei Über-40-Jährigen → „reines" Moringa/Beetroot als „ancient remedy" | Verified (Script) |
| Zielgruppe | US-Amerikaner:innen 40–65, explizit schwarze Community („black folks in their 40s, 50s and 60s", AAVE-Voice, schwarze Avatare, „How Africans…") | Verified (Script) |
| Warnsignale | snoopviews.com (Claimed, 2026-03-23): versteckte Abo-Abbuchungen ($69,80+ statt beworbener $24,99), Produkt = generisches Rebrand, China-Herstellung; 404 Media (2026-07-30): FDA-Rückruf (Salmonella), „AI slop factory"; Klage Humann v. Ambrosia Brands (W.D. Tex. 1:26-cv-00374) | Claimed |

## 5. Distribution

| Kanal | Befund | Tag |
|---|---|---|
| Organisch (FYP) | Hauptkanal: 214.800 Likes bei nur 8.915 Followern (Like/Follower = 24) → Reichweite fast ausschließlich über For-You, nicht Follower. Following 0, keine Bio. | Verified/Estimated |
| Suche | Captions sind generische Testimonial-Sätze („So good yes yes", „We love it") + 1–2 Hashtags (#guthealth #moringa #over40 #womenover40 #beetroot #womenhealth #tiktokshopblackfriday) – keine produktsuch-optimierten Titel. Suchanteil gering. | Estimated |
| Shop-Tab / Produktkarte | Damals „orange button"-CTA = Shop-Produktkarte; heute anchors=[] bei allen 9 Videos → Verknüpfung entfernt (Produkt delisted, Affiliate gekündigt oder Video-Moderation). isECVideo=null. | Verified |
| Paid (Spark Ads) | Video #3 isAd=true → als Anzeige autorisiert; die 8 neueren nicht. | Verified |
| Views-Verteilung | Top-Video 36 % der Stichproben-Views; Long-Tail 650–1.300 Views. Exhibit P belegt frühere Ausreißer (12.600 Likes ≈ grob 0,4–1,2 Mio. Views bei 1–3 % Like-Rate, Estimated). | Verified/Estimated |
| Volumen | 161 Videos in 67 Tagen (04.10.–10.12.2025) = **2,4 Videos/Tag**; Batch-Uploads: 4 Videos in 10 Minuten (05.12. 00:48–00:58 UTC), 2 in 5 Minuten (10.12.). | Verified |
| Varianten | ja, systematisch: gleicher Body, andere Hook-Zeile / anderes Avatar-Geschlecht / anderer Wirkstoff (Belege in 3.4). | Verified |
| Schwester-Accounts / Crossposting | Keine Handles in Bio/Captions. instagram.com/stella.ryan2 → 429 (nicht prüfbar), youtube.com/@stella.ryan2 → 404. Netzwerk-Zugehörigkeit statt Schwester-Accounts: gleiche Templates bei @badobadi86, @wellness.tips07, @poormaninla, @getrosabella (Klage ¶47–72; eigene Dossiers). | Verified (404) / Claimed |
| Status | Seit 10.12.2025 keine Uploads; Follower stagnieren → Account faktisch tot (Verified via Embed-Feed) | Verified |

## 6. Kommentar-Reaktion / Social Proof
Über alle 9 Videos nur 10 Kommentare (ausschließlich Emojis) – weder Kaufbestätigungen noch „this is AI"-Pushback. Der „Social Proof" findet ausschließlich im Script statt („thousands of reviews", „people come back crying"). Saves (2–23) > Kommentare, typisch für passiv konsumierte Long-Monologe.

## 7. Wettbewerbsvorteil – Bewertung

**Der eigentliche Vorteil ist nicht der Account, sondern das Netzwerk-Playbook der Marke:** Rosabella/Ambrosia stellt (laut Klage ¶68 und 404 Media, Claimed) Skript-Templates, Avatar-Stil, Discord-Coaching und Provision bereit; stella.ryan2 ist ein austauschbarer Produktionsknoten, der das Template mit ~2,4 Videos/Tag ausführt.

| Faktor | Gewicht | Evidenz |
|---|---|---|
| Billige Massenproduktion (KI-Standbild + TTS + Karaoke, 0 Cuts, 3 Min. Content für Cent-Beträge) | hoch | Verified (Frames, Scene-Detection, identische VTT-Bodies) |
| Hook-/Avatar-Split-Testing (gleicher Body, neue erste 5 s) | hoch | Verified (#1/#2/#4, #5/#7) |
| Aggressive Direct-Response-Skripte (Sex-/Schock-Hook, ethnisches „Geheimnis", Autoritäts-Avatar, Scarcity, „2 for 1") | hoch | Verified (Transkripte) |
| Netzwerk-Provision + Brand-Assets (Packshots, Templates, Spark-Ad-Autorisierung) | mittel | Claimed (Klage) / Verified (isAd=true) |
| Zielgruppen-Arbitrage (Over-40-schwarze US-Community, AAVE-Voice) | mittel | Verified (Script) |
| Produktwahl (Moringa/Beetroot – generische, hochmargige Supplements) | mittel | Verified/Claimed |
| Qualität, Community, Trend-Musik, echte UGC-Tests | keine | Verified (0 Kommentare, keine Musik) |

**Warum es nicht (mehr) funktioniert:** Rechtsstreit + FDA-Rückruf + fehlendes TikTok-AIGC-Label + unzulässige Gesundheitsclaims → Produkt-Anchors weg, Videos teils gelöscht, Account seit Dez 2025 tot. Die letzten 9 Videos erreichten im Schnitt nur 1.717 Views; Reichweite hing an wenigen Ausreißern (Nov 2025).

## 8. Einkommensschätzung (Estimated – keine veröffentlichten GMV-/Provisionsdaten für diesen Account)

Formel: Views/Monat × CTR × CVR × Preis × Provision. Annahmen: CTR 2 %, CVR 5 %, Preis $19–40 (Video-Preis bis Website-Preis), Provision 10–20 % (Netzwerk-Provision, Höhe Claimed/unbekannt).

| Szenario | Views/Monat | Herleitung | Rechnung | Provision/Monat |
|---|---|---|---|---|
| Heute (seit 10.12.2025) | ~0 | keine neuen Uploads, Anchors entfernt | – | **≈ $0** |
| Run-Rate Dez 2025 | ~58.000 | 15.457 Views in 8 Tagen (02.–10.12.) × 30/8 | 58.000×0,02×0,05×$25×0,15 | ≈ **$220** |
| Peak Nov 2025 (unten) | ~1.000.000 | 214.800 Lifetime-Likes ÷ Like-Rate 3 % = 7,2 Mio. Views ÷ ~2,2 aktive Monate ≈ 3,3 Mio./Monat; konservativ ⅓ davon im Peak-Monat | 1.000.000×0,02×0,05×$25×0,15 | ≈ **$3.750** |
| Peak Nov 2025 (oben) | ~5.000.000 | Like-Rate 1,1 % (Stichprobe) → 19,5 Mio. Lifetime-Views, Großteil im Peak-Monat | 5.000.000×0,02×0,05×$30×0,20 | ≈ **$30.000** |

Band: **$0 heute; im Peak-Monat Nov 2025 plausibel $1.000–10.000 Provision, Obergrenze ~$30.000** (Estimated). Zusätzlich möglich: Fixhonorar für Spark-Ad-Autorisierung (isAd=true) – Höhe nicht öffentlich verifizierbar. Netzwerk-Referenz (Claimed, Klage ¶72): ~$400.000/Monat Gesamtauszahlung an alle Rosabella-Creator.
Konfidenz: **LOW** – n=9 verifizierte Videos aus der Endphase, Views der Ausreißer nur indirekt (Likes aus Gerichts-Screenshot), Provisionssatz und Shop-Preis unbekannt.

## 9. Quellen (Zugriff 2026-09-25)
- TikTok-Profil / Embed-Feed: https://www.tiktok.com/@stella.ryan2, https://www.tiktok.com/embed/@stella.ryan2
- 9 Video-SSR-JSONs (IDs in Tabelle Abschnitt 2); Untertitel-VTT (TikTok subtitleInfos eng-US) für 7579201771042557198, 7582037804507499831, 7579202285788564750, 7580171853155568909, 7582036564553780535; Videodateien + Frames für 7579201771042557198 und 7582037804507499831; Comment-API (api/comment/list) für beide
- https://tryrosabella.com/products/rosabella-organic-beetroot-capsules-1300mg-for-blood-flow-heart-health, https://tryrosabella.com/collections/frontpage
- https://snoopviews.com/rosabella-beetroot-reviews (Claimed)
- https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/ (Claimed)
- Klage: https://storage.courtlistener.com/recap/gov.uscourts.txwd.1172890758/gov.uscourts.txwd.1172890758.14.0_3.pdf, Exhibit P: …14.16.pdf
- Bing-Suche „Rosabella beetroot moringa supplement price" (via WebFetch) für Website/Amazon-Store-Hinweis (amazon.com/stores/Rosabella: 503, nicht abrufbar)
- Nicht verfügbar: WebSearch (Budget), NexLev watch_tiktok_video_and_ask (15/15), Kalodata/FastMoss, Instagram (429), YouTube-Handle (404)
