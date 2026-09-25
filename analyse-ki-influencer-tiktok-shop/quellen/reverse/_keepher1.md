# Reverse-Engineering: @_keepher1 („EB | KeepHer1 Digital", USA)

Stand: 2026-09-25 (Datenabruf 2026-09-24/25). Quellen: TikTok-Public-Data (tt_profile.sh / tt_video.sh / Video-Seiten-SSR-JSON, **Verified**), TikTok-Shop-Produktseiten (shop.tiktok.com/us/pdp/…, **Verified**), heruntergeladene Videodateien + Frame-Extraktion mit OpenCV (3 Videos, **Verified [Sichtung]**), TikTok-ASR-Untertitel (3 Videos, **Verified**), Reddit-Claim via pullpush.io (aus dem Dossier `research/accounts/_keepher1.md`, **Claimed**).
Kennzeichnung: **Verified** = in Primärdaten gesehen · **Claimed** = Behauptung Dritter · **Estimated** = eigene Rechnung mit Formel.

**Einschränkungen:** WebSearch war nicht verfügbar (Budget erschöpft). Das NexLev-Watch-Tool (`watch_tiktok_video_and_ask`) war beim Start 15/15 erschöpft (Tageslimit) – **Ersatzmethode:** MP4-Download über die TikTok-Web-Seite (Cookie-Jar) und Frame-Extraktion alle 0,5–1 s mit OpenCV (Kontaktbögen in `research/reverse/_kh/sheet_*.jpg`), plus TikTok-eigene ASR-Untertitel. Damit sind Hook-Bild, Schnittfolge, Produktdarstellung, Charakter-Konsistenz und (bei Sprechvideos) der exakte Wortlaut verifiziert; **nicht** verifizierbar sind Stimmcharakter (KI-Stimme ja/nein – Audio wurde nicht angehört), Kommentare (nicht abrufbar) und eine On-Screen-Produktkarte im Player (nur aus Anchor-Daten ableitbar). Ältere Videos (vor Mai 2026) sind nicht listbar; Provisionssätze sind nicht öffentlich.

---

## 0. Kernbefund in drei Sätzen

1. @_keepher1 ist ein **vollständig KI-generierter „Try-on/Selfie"-Fashion-Affiliate-Account** (Modell C): Eine konsistente fotorealistische Persona (Schwarze Frau, ~25–30, langes dunkles Haar, Gold-Schmuck, immer dieselbe Luxus-Wohnung) präsentiert TikTok-Shop-Bestseller in 7–16-Sekunden-Clips im Stil von Spiegel-Selfie-Hauls und Talking-Head-Beauty-Demos; 11 von 12 Sample-Videos tragen eine Produktkarte (Verified), Preise 15,60–49,36 USD (Verified, PDP).
2. Der Wettbewerbsvorteil ist **nicht Reichweite** (1.910 Follower, Median ~320 Plays) und nicht Hook-Copy (keinerlei On-Screen-Text, meist nur Musik), sondern die **Kombination aus (a) extrem hoher Fotorealität + konsistentem Charakter und Set, (b) Produktwahl = bereits bewiesene Shop-Bestseller (Honey Oud 799.711 verkauft, Laka-Liner 189.250 verkauft, Verified) und (c) billiger täglicher Produktion mit Variantentests** (gleiches Outfit-Konzept in 3 Varianten mit 3 verschiedenen verlinkten Röcken in 8 Tagen; gleiches Produkt mit 2 Hooks).
3. Verifizierbares Einkommen: **keines**. Der einzige Ausreißer (Badeanzug, 161.900 Plays = 96 % aller Sample-Plays) kann rechnerisch einmalig 800–1.600 USD Provision erzeugt haben (Estimated) – das ist die einzige plausible Basis für den Reddit-Claim „$900 in one day" (Claimed, unbelegt). Laufendes Niveau: **30–120 USD/Monat** (Estimated); Lebenszeit-Durchschnitt (aus 39.200 Likes rückgerechnet) **200–700 USD/Monat** (Estimated). Confidence: LOW.

---

## 1. Profil (Verified, tt_profile.sh 2026-09-25)

| Feld | Wert |
|---|---|
| Handle | @_keepher1 · Nickname „EB \| KeepHer1 Digital" |
| Bio | „💕AI Influencer/Creator / 💰Helping creators build income / 💫with AI content" |
| Bio-Link | https://beacons.ai/keepher1digital (WebFetch: HTTP 403 – nicht prüfbar) |
| Follower / Following | 1.910 / 365 |
| Likes gesamt | 39.200 |
| Videos | 125 |
| Erstellt | 2024-12-03 (≈ 21,5 Monate alt) |
| ttSeller / commerceUser | false / false → kein eigener Shop, reines Affiliate-Modell |
| Schwesterkonten | Instagram @keepher1digital: HTTP 429 (nicht prüfbar); YouTube @keepher1digital: 404 (existiert nicht). Keine weiteren Handles in Bio/Captions. **Kein Beleg für Crossposting oder Sister-Accounts.** |

**Rückrechnung Lebenszeit-Reichweite (Estimated):** 39.200 Likes ÷ 125 Videos = 314 Likes/Video. Im Sample liegt die Like-Rate bei 1,1–3 % (Viral-Video 1,14 %; Kleinvideos 1–9 %). Bei 1,5–3 % Like-Rate → **≈ 1,3–2,6 Mio. Plays lifetime**, d. h. ≈ 60–120 k Plays/Monat im Durchschnitt über 21,5 Monate. Die aktuellen Videos (Median 319) liegen also **deutlich unter** dem historischen Schnitt – entweder gab es weitere ältere Ausreißer oder die Reichweite ist eingebrochen.

---

## 2. Video-Set (12 Videos, Verified via tt_video.sh 2026-09-25)

Quelle: Creator-Embed-Seite (11 neueste, inkl. angepinntem Viral-Video) + Evidence-URL aus dem Reddit-Post. Anchor = TikTok-Shop-Produktkarte (Typ 35; das Anchor-Objekt trägt ein **CapCut-Icon/Schema** → Videos wurden über CapCut geschnitten/exportiert, Verified). `ShowAIGC = true` bei allen 12; `aigcLabelType = 1` (KI-Label gesetzt) nur bei 3.

| # | Video-ID | Datum | Länge | Plays | Likes | Komm. | Shares | Saves | KI-Label | Produkt (Anchor, Verified) | Preis (PDP) | Hook (0:00–0:03) | Musik |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7638470337629261087 | 2026-05-11 | 16 s | **161.900** | 1.853 | 26 | 161 | 695 | – | One-Piece-Mesh-Badeanzug + Sarong (HearthVibe Studio) | 49,36 $ | **Bild:** Spiegel-Selfie, schwarzer Badeanzug mit Sarong im Flur, kein Text, keine Stimme; **Caption:** „Swimsuit season is here☀️" | „DJ SUAVE x DifferentAttention." (Remix-Sound) |
| 2 | 7685455401017429278 | 2026-09-14 | 10 s | 2.339 | 41 | 2 | 2 | 7 | **1** | Denim-Midirock „French Elegance" (Denim Distinction) | 27,21 $ | **Bild:** Persona läuft im Flur auf Kamera zu (Lauryn-Hill-Tee, Jeansrock, weiße Stiefel), kein Text; **Caption:** „The fit is giving 90s cool girl with a little edge" | „THROW IT IN THE BAG REMIX JTOM" |
| 3 | 7687602074762087711 | 2026-09-20 | 15 s | 843 | 7 | 3 | 1 | 4 | – | Bella Vita „Honey Oud" EdP 100 ml (BellaVitashop) | 22,99 $ (–15 %, UVP 26,99 $) | **Gesprochen (ASR):** „If you've been waiting for honey oud to come back in stock, this is your sign." | „Caprice Crusing" |
| 4 | 7687444102828395807 | 2026-09-20 | 15 s | 725 | 8 | 5 | 1 | 2 | – | Laka Easy Glide Lip Liner (Laka US, @-Tag in Caption) | 23,40–54,60 $ (–36/–44 %) | **Gesprochen (ASR):** „This lip combo, brown liner, honey love, then baby pink gloss."; **Bild:** Talking-Head im Marmorbad, 3 Produkte in den Händen | „Passionfruit (Instrumental)" |
| 5 | 7664803600756968734 (Evidence) | 2026-07-21 | 15 s | 565 | 50 | 5 | 0 | 4 | **1** | **kein Anchor** – Lifestyle („Home Sweet Home": Villa + Mercedes G-Klasse in der Abenddämmerung) | – | **Gesprochen (ASR):** „There's something about getting home before the day completely disappears." | original sound |
| 6 | 7687972329258880286 | 2026-09-21 | 8 s | 514 | 18 | 0 | 1 | 3 | – | Lauryn-Hill-Print-Vest (BOYHELP) | 15,60–18,20 $ | Caption: „SUPER stretchy denim skirt and graphic tee...my new fall essential!" | original sound |
| 7 | 7687659776070716703 | 2026-09-20 | 12 s | 319 | 11 | 2 | 1 | 2 | – | Yoga-Jumpsuit (hearuisavy) | 27,00–28,83 $ | Caption: „POV: you found the one-piece that SNATCHES without making you feel like you can't breathe" | оригинальный звук (= „original sound", russische Locale) |
| 8 | 7687380886626651422 | 2026-09-19 | 9 s | 303 | 13 | 1 | 1 | 2 | – | ETCYY 2-Piece Lounge-Set mit Schleifen (ETCYY-US) | 40,98 $ | Caption: „POV: you found the cutest cozy set without the $100+ price tag 🎀" | „I Love Your Girl – Instrumental" |
| 9 | 7688078404142353695 | 2026-09-21 | 8 s | 303 | 13 | 6 | 1 | 3 | – | Denim-Skirt „American Vintage Distressed" (Yichao) | 31,85–34,04 $ (–10/–15 %) | Caption: „the denim skirt my new fall accessory!" | original sound |
| 10 | 7689088862987078943 | 2026-09-24 | 7 s | 208 | 7 | 1 | 1 | 1 | – | Leopard-Tote-Bag (Chic&Crafted Bag) | 17,71–22,18 $ (–7/–43 %) | Caption: „🐆 The cutest keepall!" | „Uncasually" |
| 11 | 7685797751396928799 | 2026-09-15 | 8 s | 188 | 6 | 2 | 1 | 1 | **1** | Halloween-2-Piece-Set Kürbis/Geist (Design Snooze) | 22,78–35,91 $ (–9 %) | Caption: „Four colors, one spooky little obsession 🎃" | original sound |
| 12 | 7689083505879321886 | 2026-09-24 | 9 s | 66 | 2 | 1 | 1 | 1 | – | ETCYY Lounge-Set (**dasselbe Produkt wie #8**) | 40,98 $ | Caption: „🍂 Are you ready for fall?" | оригинальный звук |

**Aggregat (Verified-Basis, Rechnung Estimated):** Summe 168.273 Plays; **Top-Video = 96,2 %** aller Sample-Plays. Ohne Ausreißer: Ø 579, **Median 319** Plays. Like-Rate Top-Video 1,14 %, Save-Rate 0,43 % (695 Saves – für Fashion hoch: „merken für später"). Kommentare 0–26. Upload-Rhythmus 14.–24.09.: 10 Videos in 11 Tagen ≈ **1/Tag** (historisch 125/650 Tage ≈ 1,3/Woche → zuletzt stark hochgefahren). Länge 7–16 s.

---

## 3. Sichtungen (Frame-Extraktion + ASR, Verified [Sichtung])

Kontaktbögen: `research/reverse/_kh/sheet_<id>.jpg` (Frames alle 0,5–1 s, 360×640), Schnittdetektion via Frame-Differenz (Schwelle 25/255 auf 64×64-Downsample).

### 3.1 Viral-Video 7638470337629261087 – Badeanzug (16 s, 161.900 Plays)

| Zeit | Szene | Inhalt |
|---|---|---|
| 0:00–0:01,7 | Szene 1 (Totale) | Spiegel-Selfie im Wohnungsflur (Holztüren, Downlights), Persona hält weißes iPhone, **schwarzer** One-Shoulder-Mesh-Badeanzug mit Sarong, barfuß. **Kein On-Screen-Text, keine Stimme.** Der Hook ist rein visuell: Körper/Outfit + Luxus-Setting. |
| 0:01,75–0:03,7 | Szene 2 | identische Pose, **braune** Farbvariante |
| 0:03,75–0:05,5 | Szene 3 | identische Pose, **blaue** Farbvariante |
| 0:05,5–0:09,2 | Szene 4 (Halbnah) | näher, schwarz – Blick in die Kamera, Handbewegung |
| 0:09,25–0:13 | Szene 5 | näher, braun |
| 0:13–0:16 | Szene 6 | näher, blau; endet ohne Endcard/CTA |

- **Schnitte/Szenen:** 5 harte Schnitte, 6 Szenen (3 Totalen + 3 Halbnah je Farbe); ruhiges Tempo (≈ 2–3,7 s/Szene). Struktur = „Farbdurchlauf" (Color-Swatch-Haul) – klassisches Fashion-Format, hier ohne jede Sprache.
- **CTA:** nur im Caption-Text („And in 4 colors! #tiktokmademebuyit") + Produktkarte (Anchor). Kein verbaler/visueller CTA.
- **Produktdarstellung:** getragen von der KI-Persona (Try-on), keine Packaging-, Stock- oder Real-Produkt-Aufnahmen; 3 von 4 Farben gezeigt. Der Sarong ist halbtransparent, Haut/Slip sichtbar – **leichte Sexualisierung** als Aufmerksamkeitstreiber.
- **KI-Erkennung:** keine Artefakte in den Frames erkennbar (Hände, Stoff-Transparenz, Spiegelbild-Handy sauber). Fotorealität sehr hoch; Konsistenz von Setting, Pose und Handy über 6 Clips spricht für Image-to-Video aus einem Referenzbild-Set (Estimated: Kling/Veo/Higgsfield-Pipeline mit Charakter-Referenz). Kein sichtbares Wasserzeichen; TikTok-KI-Label **nicht** gesetzt (aigcLabelType null) trotz Bio „AI Influencer".
- **Musik:** „DJ SUAVE x DifferentAttention." (Sound eines DJ-Accounts, Remix-Trend-Sound).
- **Suchwörter, die TikTok dem Video zuordnet (suggestedWords, Verified):** „One Piece Swim", „Black One Piece Swim", „Affordable One Piece Swim", „2 piece sets women" → das Video wird in der **Shop-/Produktsuche** ausgespielt.

### 3.2 Video 7685455401017429278 – Denim-Rock + Graphic Tee (10 s, 2.339 Plays, KI-Label gesetzt)

| Zeit | Szene | Inhalt |
|---|---|---|
| 0:00–0:01 | Totale | Persona läuft im selben Flur auf die Kamera zu (Lauryn-Hill-Tank, grauer Denim-Midirock mit Schlitz, weiße spitze Stiefel). Kein Text, keine Stimme. |
| 0:01–0:03,5 | Torso, langsamer Zoom | Print des Tanks, Rockbund – Detailshot |
| 0:03,5–0:06,2 | Stiefel-Close-up | weiße Stiefel mit Schnallen (Cagole-Stil) – **nicht verlinkt** |
| 0:06,25–0:07,7 | Detail | Hand zieht Rockschlitz zur Seite (Stretch/Fit-Demo) |
| 0:07,75–0:10,3 | Totale | Blick in Kamera, Laufen, Ende |

- 4–5 Schnitte + kontinuierlicher Zoom, 5 Szenen, „Outfit-Walk + Detail-Zooms"-Format wie bei Fashion-B-Roll. Verlinkt ist nur der Rock (27,21 $); Tee und Stiefel sind Kontext-Styling.
- CTA nur in Caption: „Everything linked in the 🛒" (obwohl nur 1 Produkt verlinkt ist – Verified).
- Musik: „THROW IT IN THE BAG REMIX JTOM" (Trend-Remix, passt zum Cart-CTA).

### 3.3 Video 7687444102828395807 – Laka Lip Liner (15 s, 725 Plays, #TikTokShop)

| Zeit | Szene | Gesprochen (ASR, Verified) / Bild |
|---|---|---|
| 0:00–0:03 | Talking-Head im Marmorbad | „This lip combo, brown liner, honey love, then baby pink gloss." – Persona hält 3 Produkte (Laka-Liner, MAC-Lippenstift, pinkes Gloss) |
| 0:03–0:04,7 | Produkt in Kamera | Laka-Liner wird nah vor die Linse gehalten („And work fast with this liner. It sets quick. This is burnt brown.") |
| 0:04,75–0:11,7 | Extreme Lippen-Close-ups | Liner-Auftrag Kontur → MAC „honey love" in der Mitte → Gloss („It's so creamy and it applies really smoothly … just a little baby pink gloss on top.") |
| 0:11,75–0:15 | Talking-Head | **CTA gesprochen:** „If you love a creamy brown liner, you need to try this one. **I linked the liner in the orange cart below.**" – Liner wird in die Kamera gehalten |

- 6–7 Schnitte, 5 Szenen; Tempo 1,5–3 s. Klassische **Beauty-Demo-Struktur (Hook → Produkt → Anwendung → Ergebnis → CTA)**.
- Voiceover: vorhanden, Lip-Sync auf Persona; **Stimmcharakter nicht verifiziert** (nicht angehört). Da der Charakter KI ist, ist die Stimme mit hoher Wahrscheinlichkeit synthetisch (Estimated).
- Kein KI-Label (aigcLabelType null), obwohl Lippen-Makros KI-generiert sein müssen (Charakter existiert nicht).
- Fremdprodukte (MAC, Gloss) sichtbar, aber nur der Laka-Liner verlinkt; Brand @Laka US getaggt (mögliche Brand-Kooperation, nicht verifiziert).

### 3.4 Weitere Videos (nur Cover/ASR)
- **7687602074762087711 Honey Oud (15 s):** Cover: Persona hält Bella-Vita-Flakon vor sich, Hintergrund Ankleidezimmer. ASR: „If you've been waiting for honey oud to come back in stock, this is your sign. It's warm, sweet, a little woody. I completely get why this one keeps selling out. If you see the orange cart, grab it while it's still there." → **Scarcity-Hook + Cart-CTA**, Struktur identisch zum Liner-Video.
- **7664803600756968734 „Home Sweet Home" (Evidence-Video, KI-Label):** Cover = moderne Villa mit Mercedes G-Klasse; ASR: „There's something about getting home before the day completely disappears … Home has a way of reminding me what actually matters." → reines Lifestyle-/Persona-Building ohne Produkt (Aspiration = Reichtum). Genau dieses Video wurde im Reddit-Post als „$900 in one day"-Beleg verlinkt – es hat **keinen** Anchor.

### 3.5 Charakter-Konsistenz (Verified über 5 Cover + 3 Frame-Sets)
Ein und dieselbe Persona in allen Videos: Schwarze/gemischte Frau ~25–30, langes dunkles Haar (mal glatt, mal gewellt), Gold-Creolen/Armreifen, weißes iPhone, immer dieselbe Wohnung (Holz-Flur mit Einbauschränken, Marmorbad mit Doppelspiegel, Walk-in-Closet). Kleidung wechselt, Setting nicht → **Charakter-Lock über Referenzbilder** (Estimated). Keine On-Screen-Captions in keinem gesichteten Video; keine Stock-Aufnahmen; keine realen Produktclips (alle Produkte werden „von der Persona" gehalten/getragen, d. h. KI-gerendert – bei Bella Vita und Laka mit korrekt lesbarem Branding, also vermutlich Produktfoto als Referenz).

### 3.6 Kommentare / Social Proof
Nicht abrufbar (kein Kommentar-Endpoint ohne Login; Watch-Tool erschöpft). Indiz: 26 Kommentare beim Viral-Video bei 161.900 Plays (0,016 %) sind extrem wenig – typisch für Shop-Video-Traffic aus Suche/Shop-Tab statt aus der Community. **Nicht öffentlich verifizierbar**, ob „is this AI?"-Pushback vorkommt.

---

## 4. Offer (Produkte, Preise, Provision)

| Feld | Befund | Tag |
|---|---|---|
| Produkte | 10 verschiedene Shop-Produkte in 11 Anchor-Videos: Badeanzug, 3× Denim-Rock/Vest, Lounge-Set (2×), Halloween-Set, Yoga-Jumpsuit, Tote-Bag, Lip Liner, Parfum | Verified |
| Preise | **15,60–49,36 USD** (PDP, 2026-09-25); Ø ≈ 28 USD; Rabatte 7–44 % bei 6 von 10 | Verified |
| Verkaufsvolumen der Produkte (PDP „sold") | Honey Oud **799.711**, Laka-Liner **189.250**, Jumpsuit 20.966, Tote 9.563, Denim-Rock 7.028, Halloween-Set 6.944, Lounge-Set 4.925, Badeanzug 4.083, Yichao-Rock 1.148, Vest 52 | Verified |
| Shops | HearthVibe Studio, Denim Distinction, Design Snooze, ETCYY-US, Laka US, BellaVitashop, hearuisavy, BOYHELP, Yichao, Chic&Crafted Bag – Bewertungen 4,0–4,7 | Verified |
| Provision | **nicht öffentlich** (FastMoss-PDP ohne Daten, Kalodata 403). Typische Spanne US-Fashion/Beauty-Affiliate 10–20 % | Estimated (W5-Benchmark) |
| Coupon | keiner im Video/Caption; nur Shop-eigene Rabatte | Verified |
| Impulskauf-Potenzial | hoch: <50 USD, visuell (Outfit/Farbe/Duft), saisonal (Fall, Halloween, Swim), Scarcity-Sprache („keeps selling out", „grab it while it's available") | Estimated |
| Problem/Lösung | kaum Problem-Framing; primär **Aspiration/Ästhetik** („gives that what-perfume-are-you-wearing energy", „without the $100+ price tag", „SNATCHES without making you feel like you can't breathe") | Verified (Captions) |
| Zielgruppe | Frauen 18–35 USA, preisbewusst, Fashion/Beauty, Schwarze/PoC-Zielgruppe (Persona, Lauryn-Hill-Print, „brown lip combo") | Estimated |

**Produktstrategie:** Der Account wählt nahezu ausschließlich **bereits bewiesene Bestseller** (Honey Oud und Laka gehören zu den meistverkauften TikTok-Shop-Beauty-Artikeln 2026) und hängt sich an bestehende Nachfrage – **Trend-Arbitrage statt Produkt-Discovery**.

---

## 5. Distribution

| Frage | Befund | Tag |
|---|---|---|
| Organisch (FYP) vs. Suche vs. Shop-Tab | Captions sind **produktsuchoptimiert** (#denimskirt, #halloweenpajamas, #onepieceswimsuit, #lipliner, #honeyoud, Produktname im Text); TikTok hat allen Outfit-Videos Such-Keywords zugewiesen (suggestedWords: „denim skirt", „halloween pajama", „Two Piece Set", „Affordable One Piece Swim"); Kommentar-Rate 0,016 % beim Viral-Video. → Estimated: **Viral-Video überwiegend FYP/Shop-Empfehlung; Long-Tail-Videos überwiegend Such-/Shop-Tab-Traffic** (Mengenanteil Suche 30–50 %, nicht messbar) | Estimated |
| Shop-Empfehlungen | 11/12 Videos `isECVideo=1` → für Shop-Tab/Produktseiten-Videofeeds qualifiziert; Halloween-Video zeigt „20+ colors" = Katalog-Content | Verified |
| Anteil Top-Video | 96,2 % der Sample-Plays; 1 von 125 Videos >100k | Verified (Sample) |
| Volumen | aktuell ≈ 1 Video/Tag (10 in 11 Tagen), historisch ≈ 1,3/Woche; 125 Videos in 21,5 Monaten | Verified |
| Varianten | **ja:** Denim-Rock+Graphic-Tee-Konzept 3× in 8 Tagen (14./21./21.09.) mit **drei verschiedenen** verlinkten Produkten (Rock 27,21 $, Vest 15,60 $, Rock 31,85 $) und je anderem Caption-Hook; Lounge-Set 40,98 $ 2× (19.09. „POV: … without the $100+ price tag" vs. 24.09. „Are you ready for fall?"). → **Hook-/Produkt-Split-Tests** auf demselben Charakter-Set | Verified |
| Sister-Accounts / Crossposting | keine Handles genannt; IG 429, YT 404 → **nicht belegt** | Verified (negativ) |
| Bezahlte Reichweite | `isAd=false` bei allen 12 | Verified |
| Tooling-Indizien | Anchor-Objekt mit CapCut-Schema (Export via CapCut); zwei Sounds als „оригинальный звук" (russische Locale des Sound-Uploads → Tool-/Operator-Locale oder wiederverwendeter Sound) | Verified (Indiz) |

---

## 6. Wettbewerbsvorteil – Bewertung

| Faktor | Beleg | Stärke |
|---|---|---|
| **Fotorealistische, konsistente KI-Persona + festes Set** | 3 Frame-Sets, 5 Cover: kein Artefakt, dieselbe Wohnung/Handy/Schmuck; Lippen-Makros, lesbare Markenlogos | **hoch** (Verified) – das ist die eigentliche Produktionsleistung |
| **Produktwahl = Bestseller-Arbitrage** | PDP-Sold-Zahlen 4k–800k | **hoch** (Verified) |
| **Billige, schnelle Produktion + Variantentests** | 7–16 s, keine Captions, keine Sprache bei 7 von 12, 1 Video/Tag, 3 Varianten eines Konzepts in 8 Tagen | **mittel-hoch** (Verified) |
| Hooks | keine Text-Hooks; visueller Hook = Körper/Outfit/Luxus-Setting; gesprochene Hooks nur bei Beauty (Scarcity) | **niedrig** – austauschbar |
| Volumen | 125 Videos/21 Monate – moderat | niedrig-mittel |
| Provision/Deals | nicht öffentlich; @Laka-Tag deutet auf Brand-Kontakt | unbekannt |
| Reichweite/Community | 1.910 Follower, Median 319 Plays, Kommentare einstellig | **schwach** |
| Zweites Geschäftsmodell | Bio „Helping creators build income with AI content" + beacons.ai → Coaching/Sell-the-shovel; nicht prüfbar (403) | unbekannt |

**Fazit:** Der Vorteil ist eine **Kombination aus KI-Produktionsqualität (Charakter-Lock, Fotorealismus) × Bestseller-Trend-Arbitrage × billigem Testen**. Nichts davon erzeugt derzeit nennenswerte Reichweite; der Account lebt von einem Ausreißer. Als **Workflow-Blaupause** (Persona + Set + Bestseller + Cart-CTA + tägliche Varianten) ist er brauchbar, als **Einkommensbeleg** nicht. Evidenzqualität: Produktions- und Produktdaten Verified; Traffic-Quellen und Provision Estimated; Einkommen Claimed/unbelegt.

**Compliance-Risiko (Verified):** 9 von 12 Videos ohne KI-Label trotz Selbstdeklaration; Persona „trägt" und „testet" Produkte, die sie nie besessen hat (Lippen-Auftrag, Duft-Review) → verstößt gegen TikTok-Shop-Affiliate-Richtlinien zu irreführenden Produktdemos und die KI-Kennzeichnungspflicht; nachträgliche Sperre/Demonetarisierung möglich.

---

## 7. Einkommensschätzung (Estimated – keine Fakten; keine GMV-Quelle vorhanden)

Formel: **Plays × CTR × CVR × Ø Preis × Provision**. Inputs: CTR 2 %, CVR 5 % (W5-Benchmarks für Shop-Videos), Ø Preis 28 USD (Verified PDP-Mittel), Provision 10–20 % (Estimated).

| Szenario | Plays/Monat | Herleitung | Bestellungen | GMV | Provision |
|---|---|---|---|---|---|
| A – aktuelles Niveau | 10.000–17.000 | 30 Uploads × 320–580 Plays | 10–17 | 280–480 $ | **30–100 $** |
| B – Lebenszeit-Durchschnitt | 60.000–120.000 | 39.200 Likes ÷ 1,5–3 % Like-Rate ÷ 21,5 Monate | 60–120 | 1.700–3.400 $ | **170–680 $** |
| C – Viral-Monat (Mai 2026) | ~180.000 | 161.900 (Top-Video) + Grundrauschen | ~180 | 161.900 × 2 % × 5 % × 49,36 $ ≈ 8.000 $ | **800–1.600 $** (Einzelvideo) |

- **Monatsband: 50–500 USD/Monat**, in einem Viral-Monat einmalig 1.000–2.000 USD (Estimated).
- Reddit-Claim „$900 in one day" (Claimed, u/Tweetgirl, r/AIAdMakers, 2026-07-23): nur plausibel, wenn ein Großteil der 161.900 Plays des Badeanzug-Videos in 1–2 Tagen lief (Szenario C) – das Evidence-Video im Post ist das falsche Video (kein Anchor). **Nicht öffentlich verifizierbar.** Keine Kalodata-/FastMoss-/EchoTik-Daten öffentlich.
- Confidence: **LOW** (kein Verkaufsdatensatz, Provision unbekannt, Bio-Link nicht prüfbar, kleines Sample mit einem dominanten Ausreißer).

---

## 8. Quellen (Zugriff 2026-09-24/25)
- https://www.tiktok.com/@_keepher1 (Profil-JSON) · https://www.tiktok.com/embed/@_keepher1 (Video-Liste)
- Video-Seiten (SSR-JSON, MP4, ASR-VTT): https://www.tiktok.com/@_keepher1/video/7638470337629261087 · …/7685455401017429278 · …/7687444102828395807 · …/7687602074762087711 · …/7664803600756968734 · …/7685797751396928799 · …/7687380886626651422 · …/7687659776070716703 · …/7687972329258880286 · …/7688078404142353695 · …/7689083505879321886 · …/7689088862987078943
- TikTok-Shop-PDPs: https://www.tiktok.com/view/product/1732225485966644175 (Badeanzug, 49,36 $, HearthVibe Studio, 4.083 verkauft) · …/1731828685594858403 · …/1732438145575588742 · …/1731444454309794345 · …/1732301660493680745 · …/1729413742968869814 · …/1731487977761378562 · …/1732534470022107487 · …/1732417073078505811 · …/1731999649782272701
- Reddit-Claim: https://www.reddit.com/r/AIAdMakers/comments/1v42ogi/ai_creators_making_bank/ (via api.pullpush.io, aus Dossier; heute 429)
- https://beacons.ai/keepher1digital (403) · https://www.instagram.com/keepher1digital/ (429) · https://www.youtube.com/@keepher1digital (404)
- https://www.fastmoss.com/e-commerce/detail/1732225485966644175 (Seite ohne Daten) · https://www.kalodata.com/product/1732225485966644175 (403)
- Rohdaten: `research/reverse/_keepher1_fresh.jsonl`, `research/reverse/_kh/meta.json`, `research/reverse/_kh/pdp_*.html`, Frame-Bögen `research/reverse/_kh/sheet_*.jpg`, Untertitel `research/reverse/_kh/*.vtt`
