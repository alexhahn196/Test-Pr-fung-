# Red-Team: YouTube-Gegenbelege mit Dashboards (Winkel „youtube_dashboards")

Stand: 2026-09-25 (Zugriffsdatum aller Quellen). Rolle: Angriff auf die Thesen C1–C7 des Berichts `/home/user/Test-Pr-fung-/analyse-ki-influencer-tiktok-shop/README.md`.
Tags: **Verified** = in TikTok-Rohdaten selbst gesehen (tt_profile.sh / tt_video.sh / tt_media.py) · **Claimed** = jemand behauptet es (hier: fast immer im YouTube-Video, Dashboard nur *beschrieben*) · **Estimated** = eigene Rechnung, Formel angegeben.
Kategorien A–H laut Briefing; „human-face" = echte Person vor der Kamera.

---

## 0. Methode, Umfang und harte Grenzen

- **Suche:** Alle 17 vorgegebenen Queries über `yt_search.py` (Relevanz) und eine Variante mit Upload-Datum-Sortierung (`research/redteam/ytd/yts.py`, Parameter `sp=CAI%3D`), je 20 Treffer → 216 eindeutige Videos, davon 39 schon in `quellen/claims_youtube.md` / `sweep_youtube.md`. Zusätzlich 8 eigene Queries für Nicht-Kursverkäufer („income report", „how much tiktok shop paid me faceless", „hands only videos income" …) und 3 NexLev-`youtube_search`-Abfragen (Sortierung nach Datum / letztes Jahr). Rohdaten: `research/redteam/ytd/q*_*.jsonl`.
- **Transkripte (NexLev `get_video_transcript`)**, verdichtet unter `research/redteam/ytd/tx/`: IYEm75hPtP4, f52ZNpJV5VI, puJkObRPQ6s, -Zjgb_PVxNM, QA2ca-gWaHU, Ip0JKfwNEMQ, TGi-EFrUkFg, 9NXR9taREjI, kF6nDe2vTCk, wCo8l9zpG54, JlT8_FB1uPM, 5V5_VsPQuGA, OFigTL0DSDQ, 7NXAJukvU1I, mBrk0BFWfkc, 0TlilGg6Tjg; dazu der Cache `research/yt_tx/fwyCSbPdgRs.txt`. Das sind 17 Transkripte (Ziel waren 12).
- **Dashboard-Ablesung ist gescheitert:** `watch_youtube_video_and_ask` meldete beim ersten Aufruf „RATE LIMIT EXCEEDED … 15/15 calls … in the last 24 hour(s)" (Kontingent vorher von anderen Agenten verbraucht). Ersatzwege: `yt-dlp` (installiert, 2026.08.19) → „Sign in to confirm you're not a bot"; Seitenabruf youtube.com/watch → HTTP 429. **Konsequenz: In diesem Winkel wurde kein einziges Affiliate-Center-Dashboard selbst gesehen.** Alle Einkommenszahlen unten sind *Claimed* (gesprochen oder als gezeigt beschrieben). Evidenztyp = `self_report`, nie `dashboard_seen`.
- **Handles:** TikTok-Handles werden in diesen Videos fast nie gesprochen; sie stehen nur im Bild. Geprüft per `tt_profile.sh`: rapsells/rapcells/rap.sells/rapsellz (für „Rap Cells" bei Moe Alamawi), scallyselects & Varianten (John Scalia), dailyfiles & Varianten (Cami), tylerblood, mosolegitt → alle nicht gefunden, privat oder falsche Person. Gefunden und geprüft: @kingmosolegitt, @turnersells, @kevin.colson0. Eine WebSearch („rapcells" OR „rap cells" tiktok shop) ergab nichts. WebSearch-Verbrauch dieses Agenten: 1 von 15.
- **Bias-Lage:** Von ~200 gesichteten Titeln ist die große Mehrheit von Kurs-, Mentoring-, Tool- oder Agenturverkäufern. Unter den neu transkribierten Videos gibt es nur **eine** Quelle, deren Aussage *gegen* ihr eigenes Interesse gerichtet ist (Cami, menschliche Top-Affiliate, über KI-Konkurrenz, siehe YD1). Der Auftrag, Creator ohne Kurs zu bevorzugen, war mit YouTube als Quelle kaum zu erfüllen. Die Suche nach „Einkommensberichten" (z. B. TATPLRL3H-g „My January Earnings", bwFoi76bO98, yNxREh5a0cQ) brachte nur kleine menschliche Creator, keinen KI-Fall.

---

## 1. Neue Fälle (nicht in claims_youtube.md), nach Stärke als Gegenbeleg

### YD1 – Cami (UK, human-face) sagt: Platz 2 und 3 der UK-Affiliates sind KI-Bottom-of-Funnel-Accounts
- Quelle: „she made £32,131 in ONE month with TikTok Shop affiliate", Kanal Cami, https://www.youtube.com/watch?v=0TlilGg6Tjg (~Feb 2026, 912 Views). Interview Mitte Januar 2026.
- Wörtlich [22:55–23:24]: „I became like top 10 pretty quickly … Now I've been stuck at four. Um, and then number two and three are AI accounts doing a funnel. >> What's it? Daily Files or something like that. >> Yeah, something like that. … they're not sharing it yet … maybe gatekeep." [24:45]: „it pisses me off that AI is beating me right now … if you can make a realistic AI avatar and convert that well on a … gaming chair that they went super viral on, creds to you." [25:12]: „But obviously it's a guy doing it cuz guys can't promote female products."
- Einordnung: Behauptung einer **menschlichen** Konkurrentin, die sich damit selbst herabstuft. Das ist eine Aussage gegen ihr eigenes Interesse und darum glaubwürdiger als die üblichen Kursverkäufer-Claims. Die Rangliste ist nicht benannt (vermutlich Kalodata/FastMoss, UK, nach GMV).
- Größenordnung: Cami nennt für sich selbst (UK, Provision in GBP) Sep 4,2–4,5k, Okt 18,9k, Nov 28,9k, Dez 28k, Jan „on track for more than a 30K month" [11:07–11:36], ohne Brand-Deals. **Estimated:** Wer bei GMV vor Platz 4 liegt, erzielt bei ähnlicher Provisionsquote mindestens so viel Provision: ≥ ca. £28k ≈ ≥ 35.000 USD pro Monat (Kurs 1,27). Bei niedrigerer Provision auf GMV-Max-Produkten (5–10 %) eher 15.000–35.000 USD. Das ist *nicht* belegt.
- Format: B (realistischer KI-Avatar + echtes Produkt, Bottom of Funnel). Handles: nicht genannt; „Daily Files" als dailyfiles / daily.files / thedailyfiles geprüft → Fremdaccounts mit 0–5 Followern (Verified, falsche Accounts).
- Widerspricht: C1 (wenn der Avatar als „virtuell" zählt), C2, C3. Stärke: **mittel** (einzige Nennung, ohne Handle, aber nicht interessengeleitet). Das ist die wichtigste Spur für die UK-/Top-Earner-Agenten: UK-Affiliate-Ranking Jan 2026, Plätze 2–3.
- Nebenbefund im Schwester-Interview „From £0 to £300K Profit in 9 Months" (Tom Whitey & Cami), https://www.youtube.com/watch?v=OFigTL0DSDQ (~Juli 2026) [8:48]: „I remember my first shop video … I posted like an AI apple cider vinegar video … it got over a million views and it was selling like three bottles every 1,000 views. So like made like 2 3k in profit." Aus dem Transkript ist der Sprecher nicht eindeutig (Tom Whitey oder Cami). Das zeigt: Auch „menschliche" Top-Leute haben mit KI-Videos angefangen. Das stützt die Hypothese, dass der Bericht menschliche Top-Earner ohne Formatprüfung als Nicht-KI gezählt hat (Kategorie H). Cami selbst ist heute human-face (sprechende Videos, Retainer £700 pro Post, „50k profit last month" inklusive 10–15k Retainer).

### YD2 – Coaching-Kunde „Lucas" (minderjährig laut Video, Brasilien → US-Markt, Client von ducrez; Nachname entfernt): 8.000 USD Provision aus ~50.000 USD GMV in einem Monat mit KI-Avatar-„Transformations"
- Quelle: ducrez, „This AI TikTok Shop Strategy Made Him $48,100 in GMV at 16 | Case Study", https://www.youtube.com/watch?v=wCo8l9zpG54 (~Juli 2026, 103 Views).
- Wörtlich [0:27]: „How much did you make in profit last month? >> … it was 8 grand, I think … Before the the bonus." [10:21]: „You made … $8,000 profit. How much is that in GMV? >> … like 50 50k GMV." Erstes Video „2 million views" [5:14]. Bans: „every time I got banned … we're not getting banned like it was before" [5:14]. Lernkurve: „when the woman like touch a lot on the legs … you probably got banned" [6:12–6:40]. GMV-Max-Taktik: Avatar-Ethnie nach der Zielgruppe wählen, die GMV Max gerade bespielt [11:44].
- Metrik: Provision („profit" = Provision, GMV separat genannt). **Estimated:** Provisionsquote 8.000/50.000 = 16 %; Titel nennt 48.100 USD GMV → 7.700–8.000 USD Provision in einem Monat.
- Format: B (KI-Avatar-Frau in Vorher/Nachher-Clips, wahrscheinlich Shapewear; Produkt real). Handle: nicht genannt. Longevity: mehrere Accounts gebannt, gekaufte Accounts. Bias: ducrez / Scalex AI Inner Circle (Testimonial), sehr stark.
- Widerspricht: C1 (teilweise), C3. Stärke: schwach bis mittel.

### YD3 – Tyler Blood (Client von David Margaryan): „10K a month" mit 10-Sekunden-KI-Videos. Das Volumen bestätigt eher C6.
- Quelle: David Margaryan, „How Tyler Makes 10k/mo with TikTok Shop Ai Automation (case study)", https://www.youtube.com/watch?v=kF6nDe2vTCk (2026-04-13, 1.349 Views).
- Wörtlich [0:30]: „right now, I'm making 10K a month in TikTok … in a matter of 5 months". [1:28]: „I've made eight accounts … Majority of those accounts got banned." [2:24]: „every day getting a violation, and then blocking up all your commissions". [5:15]: „I normally do 20, 30 videos a day." [6:12]: 10-Sekunden-Videos, das Produkt wird per KI in Szenen gesetzt („log house … beach house … mansion"). [7:35]: „I'm running two accounts right now, 35 videos in total. Takes me about 2 to 3 hours". [9:26] Margaryan: „You can be back on $400 days tomorrow on a new account."
- Metrik: „10K a month", nicht spezifiziert, im Kontext wohl Provision. Format: G (KI-Szene + echtes Produktbild, Text on Screen). Bias: Mentoring-Testimonial. Longevity: 8 Accounts, die meisten gebannt.
- **Wichtig für die Bewertung:** 35 Videos/Tag × 30 = **1.050 Videos/Monat** für ~10.000 USD → **Estimated 9,5 USD Provision pro Video**. Das ist *weniger* als die 14,97 EUR pro Video im Berichtsmodell. Dieser Selbstbericht *bestätigt* C6 (≈830 Videos für 10.000 EUR) und widerspricht ihm nicht.

### YD4 – Moe Alamawi (Momentum TT Academy): Drittanbieter-Account „Rap Cells" mit 38.000 USD GMV in 30 Tagen, reine KI-Bottom-of-Funnel-Videos mit Ad-Spend; Client Andrew mit 8.400 USD Provision in 7 Tagen
- Quellen: „Exposing my $42k/Mo Ai TikTok Shop System (copy me)", https://www.youtube.com/watch?v=TGi-EFrUkFg (2026-07-19, 8.639 Views); „These Ai Videos Make $8,400 per Week on TikTok Shop", https://www.youtube.com/watch?v=9NXR9taREjI (~Sep 2026, 3.955 Views).
- Wörtlich (TGi) [0:54]: „This creator's name is Rap Cells, and in the last 30 days, he generated over $38,000 in revenue. If we go to the last week, he's generated over $7,000. So, he's averaging around $1,000 per day." [6:01]: „every single one of these videos has this little purple ad sign … getting tens of thousands of dollars pushed behind them by the brands … these are all bottom of funnel product first AI generated videos". [13:31–14:26]: „post eight to 10 videos per day … more than enough … to make 5 to $10,000 per month". Produkte: „around $220, 5% … $11 in commission per sale", Filter „over $50 average unit price, and under 250 creators".
- (9NX) [1:25]: „My guy, Andrew, sent in this on September 2nd, where he made over $8,400 in pure commission". Produktbeispiel [6:05]: „It costs $414. We'll take 16% commission … we pocket $66".
- Metriken: „Rap Cells" = GMV (Kalodata-Revenue). **Estimated** Provision bei 5–20 %: 1.900–7.600 USD pro Monat. Andrew = Provision (Screenshot beschrieben, 7 Tage).
- Format: G (Nano Banana + Kling-Clip aus Listing-Bild, 5 s, Caption; kein Avatar, keine Stimme). Handle „Rap Cells": nicht auffindbar (siehe §0). Bias: Coaching mit „performance guarantee", sehr stark.
- Widerspricht: C3 (mittel), C5 (über die Ticketgröße, siehe §3). Stärke: schwach.

### YD5 – Mohamed Camara („mosolegitt"): 5.700 USD „profit" in wenigen Tagen mit Hybridformat (echte Hand-Clips + KI-Reaktionsfigur), Drittanbieter mit KI-Model 220.000 USD Umsatz pro Monat
- Quelle: „$5,700/week on TikTok Shop Affiliate with Ai - Just Copy Me", https://www.youtube.com/watch?v=QA2ca-gWaHU (2025-08-04, 84.667 Views).
- Wörtlich [0:00]: „In the last few days, I made 5.7K in profit just posting silly videos on Tik Tok using AI. And here's another creator … making 220K a month in actual revenue. Out of profit is maybe about 15 to 20% … They're clearing over 40, 50K". [0:40]: Affiliate-Center-„Spy": „around 13 maybe like 5K a day in revenue". Drittanbieter-Videos „4.35 million" und „1.96 million" Views, „The model is an AI. The product being posed by the pool … is AI as well" [1:22–1:43]. Eigenes Modell [5:36–8:14]: „10 to 20 videos a day … 300 videos a month … If you just get one or two of those videos to go viral, you're making 5K a week"; VA von onlinejobs.ph für „$7 an hour", „about $50 a week"; er filmt die Produkt-Clips selbst mit der Hand, der VA setzt einen Kling-AI-Clip davor („the character just being very surprised") und fügt eigenen Sound und Captions hinzu. Produkt: Physicians Choice, $36, 20 % („$7 or $8 per every sale").
- Metrik: „profit" = Provision (15–20 % von Revenue, von ihm selbst so erklärt). Format: H/G (echte Hände + echtes Produkt + KI-Hook-Figur, kein Voiceover). Drittanbieter: A/B (KI-Model mit KI-inszeniertem Produkt).
- **Verified Gegenprobe:** Sein verlinkter TikTok @kingmosolegitt (erstellt 2024-07-04): 5.082 Follower, 28.300 Likes, 171 Videos, commerceUser=false. Die vier neuesten Videos (24.–26.08.2026 und 17.04.2026) sind High-Ticket-Coaching-Clips (#highticketsales #coachingbusiness), ohne Shop-Anchor. Der Creator hat also zum Coaching gewechselt. Der Shop-Account ist nicht benannt.
- Widerspricht: C3 (schwach). Stärke: schwach. Longevity-Signal: Wechsel zum Coaching (passt zu C4).

### YD6 – Alfonso (Discord von Jayden Prints): „0 – $132,324 in 45 days AI Tiktok Shop Case Study", Videos mit 1,4 Mio. und ~0,8–1 Mio. Views, danach Löschaufforderung von TikTok
- Quelle: https://www.youtube.com/watch?v=IYEm75hPtP4 (~Aug 2026, 343 Views). Über 15 Minuten nur Mindset-Gespräch.
- Wörtlich [15:38]: „we're struggling with bans … Tik Tok … send me an email about, hey, you should … stop … doing this. You should delete everything or we're going to … ban your account and all the money I've made … disappear." [16:09]: „one video with 1.4 million views and another one with … over 800K or 900k … it was converting really good like 40 or 50 or even 60k per meal".
- Metrik: Titel 132.324 USD (wahrscheinlich GMV, 45 Tage); „per meal" ist mehrdeutig, vermutlich 40–60 USD GMV pro 1.000 Views (GPM). **Estimated** bei GPM 40–60: 1,4 Mio. Views → 56.000–84.000 USD GMV aus einem Video. Format: KI (Details nicht beschrieben), vorher „USA content style". Bias: Discord-Community.
- Bedeutung: Das ist ein direktes Enforcement-Signal. Die Einnahmen standen unter Löschandrohung, die Top-Videos wurden gelöscht. Das stützt C2 (Kurzlebigkeit). Stärke als Gegenbeleg: schwach.

### YD7 – Michael Bernstein, Student aus Schweden: „my first month was 75K" mit KI-Videos, in denen Personen sprechen
- Quelle: „$70k Using AI TikTok Shop Affiliate (Case Study)", https://www.youtube.com/watch?v=7NXAJukvU1I (~Sep 2025, 5.308 Views).
- Wörtlich [0:00]: „I switched completely from drop shipping to Tik Tok shop AI and my first month was 75K." [0:56]: „I went from 30K to like 50k and then from 50k to 75k." [1:23]: „You had people speaking in it. It was very real looking … You made 80 or 90K in a month without filming anything". Er arbeitet noch in der Altenpflege (1.300–1.500 Gehalt).
- Metrik: mehrdeutig, sehr wahrscheinlich GMV. **Estimated** Provision bei 10–20 %: 7.500–15.000 USD. Format: A/B (sprechende KI-Personen). Bias: Mentoring (Bernstein), stark. Stärke: schwach.

### YD8 – InVideo (Tool-Anbieter, 2024): ein 100 % KI-Video mit ~30.000 USD Umsatz in 7 Tagen; der damals genannte Top-Creator @kevin.colson0 existiert in dieser Form nicht mehr
- Quelle: „It took 15 mins to make $140,000 with this AI video (TikTok Shop Affiliate)", https://www.youtube.com/watch?v=mBrk0BFWfkc (~2024, 45.993 Views).
- Wörtlich [0:00]: „This one AI generated video made over $139,000 from TikTok Shop Affiliate". [5:33]: „kevin.colson0 has made $155,000 in revenue in the last 7 days from this product" (15-Day Cleanse). [6:01]: „this video is 100% AI generated and it's generated almost $30,000 in the last 7 days". Format des KI-Videos: KI-Stock-Bilder + KI-Männerstimme (InVideo), also C/G.
- **Verified Gegenprobe:** @kevin.colson0 heute: createTime 2026-08-07, 0 Follower, 0 Likes, 0 Videos laut Stats (tt_recent zeigt 1 URL). Der Handle wurde also neu registriert, der Account von 2024 ist verschwunden (gelöscht oder gebannt).
- Stützt C2 (Kurzlebigkeit) und zeigt zugleich, dass einzelne KI-Voiceover-Videos Umsätze im fünfstelligen GMV-Bereich erzielen können (Kalodata, Claimed). Bias: Tool-Anbieter.

### YD9 – John Scalia („Scally Selects"): faceless mit echten Händen (F), „six figures in profit"
- Quelle: „This Faceless TikTok Shop Video Made Me $20,000+ (Full Tutorial)", https://www.youtube.com/watch?v=fwyCSbPdgRs (~Juni 2026; Duplikat LUF2Wl5PxRA).
- Wörtlich [0:00]: „When I first started TikTok Shop back in 2024, I didn't show my face for the first probably year … and from that I was still able to make six figures in profit". [0:42]: „we are already at … $548 for the day" (Dashboard wird gezeigt, laut Transkript). Format: F (0,5×-Weitwinkel, Hände + Produkt, eigene Stimme, keine KI). Bias: eigene Community. Handle nicht auffindbar (siehe §0).
- Relevanz: Menschlicher F-Benchmark; kein KI-Beleg. Stärke als Gegenbeleg gegen C5: schwach bis mittel.

### YD10 – Kleinere / nachrangige Funde
- 5x Dashboard (Tool-Anbieter), „I Make $22,800/Month on TikTok Shop with 100% AI Content", https://www.youtube.com/watch?v=f52ZNpJV5VI (~Juli 2026, 256 Views): [0:09] „Our own in-house team is running accounts doing 10, 20, even $50,000 a month on TikTok shop purely with AI content." Kein Beleg im Transkript; der geklonte Referenzclip (Shark-Staubsauger, menschlich) habe „214,000 GMV" gemacht. Sehr schwach.
- ducrez, „How AI TikTok Shop Generates Me $342,927 GMV Per Month", https://www.youtube.com/watch?v=puJkObRPQ6s (~Sep 2026): Drittanbieter-Account „over 106K in GMV" in 30 Tagen mit simplen Produktvideos; „as a community, this year alone, we have easily generated over seven figures in GMV, all with AI content"; Methode: 30 Produkte/Tag testen, damit GMV Max die Videos mit Ad-Spend bespielt. Community-Aggregat, GMV. Schwach.
- Josh Adkins, „How This AI Made Me $250,000+", https://www.youtube.com/watch?v=-Zjgb_PVxNM (~Juli 2026): „$250,000 in pure profit" über ~3 Jahre, 5.000+ Videos; ein 700k-View-Video „making me like 100, 200 pound a day". Human; KI nur für die Recherche (Tool Breakwave.ai, eigenes Produkt). Kein KI-Content-Beleg.
- Annamaria Prideaux, „From Nursing To $90K PROFIT in a Month", https://www.youtube.com/watch?v=5V5_VsPQuGA (~Sep 2026): Krankenschwester, „$91,000", „weekly checks of $4,500" nach 1,5 Monaten Pause. Format human-face (Talking Head, Beauty). Nicht KI.
- Sydney Morgan, „I Bought EVERY Ai Ad From TikTok Shop", https://www.youtube.com/watch?v=Ip0JKfwNEMQ (~Mai 2026, 611.047 Views): Konsumententest von KI-beworbenen Shop-Produkten. Keine Einkommenszahlen, aber ein Beleg für die Masse an KI-Werbevideos im Shop-Feed und für Täuschungsrisiken (Produkte kleiner oder anders als im KI-Video). Relevant für Retouren und Enforcement, nicht für Einkommen.
- Hunter Chapman, „I Make Thousands Every Month With a FACELESS Account", https://www.youtube.com/watch?v=JlT8_FB1uPM (~2025): faceless, verwendet den viralen Intro-Clip eines Fremdvideos (7 Mio. Views) neu. Kein KI-Video; 460k Views. Keine Einkommenszahl im Transkript.

---

## 2. Stärkste Fälle nach Schwelle und Kategorie (alle Claimed, sofern nicht anders markiert)

| Kategorie | ≥ 3.000 USD/Monat Provision | ≥ 10.000 USD/Monat | ≥ 20.000 USD/Monat | Evidenzqualität |
|---|---|---|---|---|
| A (100 % virtuelle Influencerin) | Drittanbieter bei Camara (KI-Model am Pool, 220k Revenue → 33–44k Provision *Estimated* 15–20 %) | dito | dito | Selbstbericht über Dritte, Handle unbekannt, 2025: schwach |
| B (KI-Avatar + echtes Produkt) | Lucas 8.000 USD (YD2) | UK-Plätze 2–3 laut Cami (YD1), *Estimated* 15–35k | UK-Plätze 2–3 (YD1), nur bei ≥ 10 % Provision | YD1 mittel (gegen eigenes Interesse, ohne Handle); YD2 schwach |
| A/B | Bernstein-Student „75K" erster Monat (YD7, wohl GMV → 7,5–15k *Estimated*) | möglich | – | schwach |
| C (KI-Stimme + Produktvideo) | InVideo-Video ~30k GMV in 7 Tagen (YD8, 2024) → *Estimated* 3–6k Provision/Woche bei 10–20 % | – | – | Kalodata-Screen beschrieben, Account weg: schwach |
| D (echte Hände + TTS) | kein neuer YouTube-Fall mit Zahlen gefunden | – | – | – |
| E (echtes UGC + KI-Script/Varianten) | (bereits im Bericht: Moe UUuFlJ_MZEM 2,46 Mio. USD GMV / 5 Monate) | – | – | – |
| F (faceless Hände, menschliche Stimme) | John Scalia „six figures" im ersten Jahr (YD9) | – | – | schwach bis mittel |
| G (KI-Szene/B-Roll + echtes Produkt) | Andrew 8.400 USD / 7 Tage (YD4); „Rap Cells" 38k GMV → 1,9–7,6k (YD4); Turner/@turnersells, anderer Account 2,7–3,5k (Bericht 12b) | Tyler 10k (YD3) | – | schwach; Turner mittel (Account Verified, Zahlen klein) |
| H (Hybrid, KI kaum erkennbar) | Camara 5.700 USD „in the last few days" (YD5); KI-ACV-Video 2–3k (OFigTL0DSDQ) | Camara hochgerechnet 20k+ (nicht belegt) | – | schwach |

Befund: Für **≥ 20.000 USD/Monat** gibt es in diesem Winkel **keinen** Fall mit KI-Content, der einem benannten und prüfbaren Account zugeordnet ist. Die einzige nicht interessengeleitete Spur dorthin ist YD1 (UK-Plätze 2–3). Die Schwelle ≥ 3.000 USD ist in B, G und H mehrfach behauptet, bei tendenziell steigender Plausibilität.

---

## 3. Strukturkritik am Modell C5–C7 (was die YouTube-Playbooks anders machen)

1. **Ticketgröße: Das Modell rechnet mit AOV 30–38 USD, das KI-Playbook 2026 nimmt bewusst High-Ticket.** Der Grund: KI braucht kein Muster und keinen Kauf des Produkts. Genannte Beispiele (Claimed): 414 USD × 16 % = 66 USD pro Verkauf (9NXR9taREjI); 220 USD × 5 % = 11 USD (TGi-EFrUkFg); Filter „over $50 average unit price" (TGi); früher im Bericht: 539 USD × 18 % ≈ 97 USD, 159 USD × 12 % ≈ 18 USD, 140 USD × 10 % = 14 USD (Moe), Filter „avg unit price ≥ $40" (Margaryan). Das Modell (AOV 35 × 13–15 %) ergibt ~5 USD Provision pro Bestellung. **Estimated:** Bei gleicher Bestellrate pro 1.000 Views liegt die Provision pro Bestellung im High-Ticket-Playbook beim 2- bis 19-Fachen. Die Konversion fällt bei hohen Preisen, das ist nicht quantifiziert. Der Bericht kennt High-Ticket (Nex Playground 299 USD / 20 % ≈ 60 USD pro Order in `products.md`, README Z. 558), modelliert es aber nicht als Basisszenario.
2. **Die Reichweite kommt aus GMV Max (Werbebudget der Marke), nicht organisch.** In fast allen 2026er KI-Playbooks (ducrez, Moe, Margaryan, Lucas) ist Ad-Spend der Marke die Hauptquelle der Views. Die organischen Verteilungsbenchmarks des Berichts (Median 350–490 Views) beschreiben das nur teilweise. Verified-Indiz: 8 von 10 der neuesten @turnersells-Videos haben isAd=true (Werbefreigabe). Gegenargument: Die Views dieser Videos liegen bei 2.723–15.600 (Median ≈ 4.000, Verified). Das entspricht fast genau den ~4.000 mittleren Views im Berichtsmodell.
3. **Provision pro Video aus den Selbstberichten** (alle Claimed; eigene Rechnung, Formel = Provision ÷ Videos):
   - Turner (7 Tage, Ramp): 339 USD ÷ ~70 = **4,8 USD**
   - Tyler (YD3): 10.000 ÷ 1.050 = **9,5 USD**
   - Patryk (Apr 2026): 2.000 ÷ 60–90 = **22–33 USD**
   - Moe-Playbook: 5.000–10.000 ÷ 240–300 = **17–42 USD**
   - Camara: 5.700 ÷ 70–140 (eine Woche) = **41–81 USD**
   - tommycetty: 10.218 ÷ ~75–250 (25 Tage, 3–5 pro Tag, später 2. Account) = **41–136 USD**
   - Berichtsmodell: 14,97 EUR ≈ **16,3 USD**.
   - Median der Selbstberichte ≈ 25–40 USD. Mit der Berichtsformel V = (Zielgewinn + 175 EUR) ÷ (Provision pro Video − 2,76 EUR): Bei 30 EUR pro Video wären für 10.000 EUR **≈ 374 Videos** nötig statt 833, für 20.000 EUR ≈ 740 statt 1.652. Bei Tylers 8,7 EUR pro Video wären es **≈ 1.700 Videos** für 10.000 EUR.
   - Fazit: C6/C7 liegen innerhalb der Spannweite der Selbstberichte. Nur wenn man den (stark selektierten) Median der Erfolgsgeschichten ansetzt, halbiert sich das Volumen. Der einzige Fall mit genannter Videoanzahl im 10k-Band (Tyler) bestätigt C6.
4. **GMV pro 1.000 Views** (Claimed): tommycetty 29/32/71 USD auf Top-Videos; Alfonso „40–60" (mehrdeutig); Tom/Cami KI-ACV-Video „three bottles every 1,000 views" (bei ~15–20 USD pro Flasche *Estimated* 45–60 USD GPM). Modell: 30 USD. Top-Videos liegen beim 1,5- bis 2-Fachen, der Durchschnitt ist nicht belegt.

---

## 4. Longevity- und Enforcement-Signale (stützen C2 und C4)

- Tyler: 8 Accounts, „Majority … banned", tägliche Violations blockieren Provisionen (YD3).
- Lucas: wiederholte Bans bei Transformations-Videos (YD2).
- Alfonso: TikTok-Mail mit Aufforderung, alles zu löschen, sonst Bann und Verlust der Einnahmen; Top-Videos gelöscht (YD6).
- @kevin.colson0 (2024, 155k USD Revenue in 7 Tagen): Handle heute neu registriert (2026-08-07, 0 Follower) → Original weg (YD8, Verified).
- Mohamed Camara: TikTok heute ein High-Ticket-Coaching-Account (YD5, Verified).
- @turnersells: letzter Upload 2026-08-16, seitdem 5,5 Wochen inaktiv (Verified).
- Mehrere Quellen empfehlen offen gekaufte Accounts (Camara: „I just buy the accounts directly"; Moe: Guide zum Kauf von 5k-Accounts).

---

## 5. Verifikation der drei stärksten Gegenbefunde

### Verifikation YD1 (Cami: UK-Plätze 2–3 sind KI-BOF-Accounts)
- Quelle erneut geöffnet: Transkript 0TlilGg6Tjg [22:55–25:12] wörtlich wie oben. Der Satz fällt spontan im Gespräch über ihr Ziel „Number one in the UK", ohne Verkaufsabsicht. Das KI-Konto macht sie eher ärgerlich („pisses me off"), sie ist also keine KI-Befürworterin.
- Handle: nicht genannt. Probe „Daily Files" (dailyfiles, daily.files, dailyfilesuk, thedailyfiles, dailyfiles.uk): falsche oder nicht existierende Accounts (Verified, 0–5 Follower). Weder Rangliste noch Metrik (GMV?) noch Zeitraum sind genannt (Kontext: Mitte Jan 2026).
- Arithmetik: Ihre eigenen Provisionszahlen (Nov £28,9k, Dez £28k) sind Claimed. Die Ableitung „Plätze 2–3 ≥ £28k Provision" setzt ein GMV-Ranking und eine ähnliche Provisionsquote voraus; beides ist unbelegt.
- Kategorie: vermutlich B (realistischer KI-Avatar + Gaming Chair), eventuell G.
- **Urteil: UNVERIFIABLE** (plausibel, nicht interessengeleitet, aber ohne Handle und ohne Zahl). Korrigierte Lesart: Es gab im Jan 2026 laut einer Top-4-UK-Affiliate mindestens zwei KI-Bottom-of-Funnel-Accounts vor ihr im UK-Ranking. Die Einkommenshöhe ist nicht belegt (*Estimated* 15.000–35.000 USD pro Monat). Übergabe an die UK-Top-Earner-Suche: Kalodata/FastMoss UK Affiliate Ranking Dez 2025–Jan 2026, Gaming Chair, KI-Avatar, männlicher Betreiber.

### Verifikation YD3/YD4 plus Strukturkritik §3 (KI-G-Playbook mit High-Ticket und GMV Max → C5/C6 zu pessimistisch?)
- Quellen erneut geprüft: Die Zitate aus kF6nDe2vTCk, TGi-EFrUkFg und 9NXR9taREjI stimmen (siehe tx/). Metriktypen: Tyler „10K a month" = unklar; Andrew = „commission"; „Rap Cells" = Revenue/GMV (Kalodata); Produktbeispiele = Preis × Provisionssatz.
- Handle-Check: „Rap Cells" und Tyler nicht auffindbar (tylerblood = privater Account von 2015, sehr wahrscheinlich privat und nicht der Shop-Account). Als Stellvertreter für das G-Format: @turnersells (siehe unten).
- Arithmetik neu gerechnet: Mit Tylers 1.050 Videos pro Monat für 10.000 USD liegt die Provision pro Video *unter* dem Berichtsmodell. Nur Kursverkäufer-Zahlen (Camara, tommycetty, Moe) liegen deutlich darüber. Die High-Ticket-Rechnung (66 USD pro Verkauf) stimmt arithmetisch (414 × 0,16 = 66,2), die Konversion ist unbekannt.
- Bias: sämtlich Coaching/Tools.
- **Urteil: PARTIALLY.** Korrigiert: Das Modell unterschätzt vermutlich die Provision pro *Bestellung* im KI-High-Ticket-Playbook (≈ 11–66 statt ≈ 5 USD). Die Provision pro *Video* aus den Selbstberichten streut aber von 5 bis 136 USD, und der einzige 10k-Fall mit Videoanzahl bestätigt C6. C5 (1.650 EUR bei 5 Videos/Tag) ist für das G-High-Ticket-Playbook eher die Untergrenze eines Median-Szenarios; eine Widerlegung ist das nicht.

### Verifikation Turner/@turnersells (G, kein Kursverkäufer, sondern Tool-Mitarbeiter; ≥ 3k-Claim für einen anderen Account)
- Profil (Verified, tt_profile.sh 2026-09-25): 47.200 Follower, 2,8 Mio. Likes, 646 Videos, erstellt 2021-11-30, Bio „Shop Videos as they should be! … How I make all of my videos", Link batchbot.io, commerceUser=false im Profil-JSON.
- 10 neueste Videos (Verified, tt_video.sh): 11.–16.08.2026, alle 8 s, alle isECVideo=1, 9 von 10 mit Produkt-Anchor (type 35), 8 von 10 isAd=true. Views 8.444 / 5.434 / 5.884 / 4.123 / 15.600 / 3.766 / 3.850 / 2.752 / 2.723 / 3.295 (Summe 55.871; Median ≈ 4.000; Top 15.600 = 28 %). Kommentare 0–1. Kein aigcLabelType, IsAigc=false, aber die Caption endet mit „Contains AI Generated Media".
- tt_media.py für 7672657930323234061 (15.600 Views, Contact Sheet gesichtet): KI-generierte Laden-Szene (Regal in einem Elektronikmarkt) mit einer schwarzen Handyhülle („RETRO Horseshoe TPU Cover", Branding ähnlich Chrome Hearts, ein mögliches Marken- bzw. IP-Problem), Text-Overlay „Tap the orange cart to see if you have coupons at checkout!", nur Musik („INSIDE MY MIND"), keine Stimme, keine Person. **Kategorie G** (KI-Szene + echtes Produktbild); für Laien eher H (wirkt wie ein Handyvideo im Laden).
- Einnahmen: nicht öffentlich verifizierbar. Der ≥ 3k-Claim („first month … 3.5K in commissions … last month … only 2.7K") betrifft laut Video einen *anderen*, nicht benannten Account. Seit 2026-08-16 kein Upload.
- **Urteil: PARTIALLY.** Format und Aktivität sind bestätigt (G, Ad-gestützt, ~4.000 Views pro Video). Die Einkommensclaims sind UNVERIFIABLE. Die ≥ 3k-Monate gehören nicht zu diesem Account. Das Profil passt genau zum Berichtsmodell (≈ 4.000 Views pro Video) und widerlegt C5 nicht.

---

## 6. Schlussfolgerungen dieses Winkels

1. **YouTube liefert fast nur Claims von Kurs- und Tool-Verkäufern.** Dieser Winkel konnte kein Dashboard selbst ablesen (Watch-Tool 15/15 verbraucht, yt-dlp mit Bot-Check, YouTube 429). Kein Gegenbeleg erreicht die Stufe `dashboard_seen` oder `verified_tiktok_data` auf Einkommensebene.
2. **Der stärkste neue Gegenbeleg kommt von einer menschlichen Konkurrentin:** Laut Cami (UK #4, ~£28–29k Provision pro Monat) waren im Jan 2026 die UK-Plätze 2 und 3 KI-Bottom-of-Funnel-Accounts mit realistischem Avatar. Wenn das stimmt, ist C3 für den UK-Markt zu pessimistisch und C1 für B-Formate falsch. Der Beleg ist unbenannt und darum nicht geprüft.
3. **Das Erfolgsformat 2026 ist nicht „virtuelle Influencerin" (A), sondern B/G:** KI-Produktszenen oder KI-Avatare in 5–15-s-Bottom-of-Funnel-Clips, High-Ticket-Produkte ≥ 40–50 USD und Ad-Spend der Marken über GMV Max. C1 ist für A kaum widerlegt. Der Bericht sollte „KI-Content funktioniert nicht" aber auf A beschränken.
4. **C6/C7 werden eher bestätigt als widerlegt:** Der einzige 10k-Selbstbericht mit Videozahl (Tyler: ~1.050 KI-Videos pro Monat über 2 Accounts, 8 Accounts, die meisten gebannt) liegt sogar über den 830 Videos des Berichts. Niedrigere Volumina (≈ 300–400 für 10k EUR) ergeben sich nur mit den Zahlen der Kursverkäufer.
5. **C5 unterschätzt wahrscheinlich die Provision pro Bestellung im High-Ticket-Playbook** (11–66 statt ~5 USD). Die Konversion ist ungeklärt; als Szenario ergänzen statt ersetzen.
6. **Kurzlebigkeit bleibt ein durchgehendes Muster:** Bans, Löschaufforderungen, verschwundene Handles (@kevin.colson0), der Wechsel zum Coaching (@kingmosolegitt) und inaktive Demo-Accounts (@turnersells) stützen C2 und C4.
7. **Formatprüfung der menschlichen Top-Earner lohnt sich:** Im Tom-Whitey/Cami-Interview wird ein erstes KI-ACV-Video mit >1 Mio. Views als Durchbruch genannt. Menschliche Top-Earner können also KI-Anteile (H) haben, die im Bericht nicht erfasst sind.

Rohdaten: `research/redteam/ytd/` (Queries, Transkripte `tx/`, `turner_recent.txt`), Frames: `media/7672657930323234061/`.
