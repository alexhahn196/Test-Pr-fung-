# Tool-Map & Preise: KI-Produktionspipeline für TikTok-Shop-Videos (Stand 2026-09-24)

Recherche-Regeln: Jede Zahl trägt ein Tag **Verified** (auf offizieller Preisseite / API-Doku / Plattformdaten gesehen), **Claimed** (Aussage Dritter, z. B. YouTube-Review) oder **Estimated** (eigene Rechnung mit Formel). Wo keine öffentliche Zahl existiert: **„Nicht öffentlich verifizierbar"**. Alle URLs mit Zugriffsdatum 2026-09-24. Preise in USD, sofern nicht anders angegeben (Higgsfield/n8n in EUR). WebSearch-Kontingent war in dieser Session erschöpft; alle Daten stammen aus direkten Seitenabrufen (WebFetch/curl), Higgsfield-MCP und YouTube-Transkripten (NexLev).

---

## 1) Kurzfazit

1. **Die Pipeline ist heute vollständig per API automatisierbar** – mit Ausnahme der Recherche-Tools (Kalodata/FastMoss/EchoTik/Shoplus haben keine öffentliche Self-Service-API; Enterprise-API nur auf Anfrage) und des TikTok-Postings (Content Posting API existiert, verlangt aber App-Audit; ungeprüfte Clients dürfen nur privat und für max. 5 Nutzer/24 h posten).
2. **Größter Kostenblock ist die Videogenerierung, nicht das LLM.** Skript-Erzeugung kostet pro Video < 0,05 USD (Sonnet 5: 2/10 USD pro MTok; Gemini 2.5 Flash-Lite: 0,10/0,40; GPT-5-mini: 0,25/2,00). Ein 24-s-Clip-Paket kostet je nach Modell 1,20 USD (Veo 3.1 Lite / Wan 2.5) bis > 10 USD (Veo 3.1 Standard, Seedance 2.5 via Runway-API).
3. **OpenAI Sora 2 fällt weg:** Die Sora-2-Modelle und die Videos-API wurden laut OpenAI-Doku am 24.09.2026 abgeschaltet, „no one-to-one replacement API is available" (Verified). Google Veo 3.1, Kling 2.6/3.0, MiniMax Hailuo/H3, Seedance 2.x, Wan 2.5–3.0 sind die verfügbaren API-Optionen.
4. **Konsistente KI-Persona:** Verlässlich nur über (a) Avatar-SaaS mit gespeichertem Custom-Avatar (HeyGen, Arcads „My Actors", Creatify Custom Avatars, Synthesia Personal Avatars) oder (b) Referenzbild-Workflows (Character-Sheet in Nano Banana / GPT Image / Flux Kontext / Ideogram Character → Image-to-Video mit Seedance 2.x, Kling 3.0, Veo 3.1). Reine Text-to-Video-Modelle liefern keine stabile Identität (Claimed, mehrere Tests).
5. **Realistisches Tool-Budget (Estimated, Formeln in Abschnitt 3):** ca. **283 USD/Monat bei 30 Videos (9,4 USD/Video)**, **475 USD bei 90 (5,3 USD/Video)**, **~1.180 USD bei 300 (3,9 USD/Video)**, **~3.130 USD bei 900 (3,5 USD/Video)**. Aggressiv (Billig-Stack, B-Roll statt Talking-Head): 1,4–2,5 USD/Video. Konservativ (Premium-Modelle + Lipsync-Pro): 18–34 USD/Video.
6. **TikTok-eigene Tools sind kostenlos:** Symphony Creative Studio (Digital Avatars, Skript, Dubbing) ist „available to all logged-in TikTok for Business users" und Teil von TikToks „free tools"; generierte Inhalte werden automatisch als „AI-generated" gelabelt (Verified). TikTok Creative Center, Affiliate Center und TikTok Studio sind ebenfalls kostenlos (Login nötig).
7. **Nutzungsbedingungen:** Kein geprüftes Tool verbietet KI-Werbevideos an sich, aber alle großen Anbieter verbieten Täuschung/Impersonation; HeyGen, Google und Anthropic verlangen ausdrücklich, KI-Herkunft nicht zu verschleiern bzw. offenzulegen; Anthropic verbietet „fake reviews, comments, or media"; Arcads verlangt Einhaltung der Werbe-/Influencer-Kennzeichnungsregeln. **Nicht-offengelegte synthetische Testimonials verstoßen damit gegen die AUP von Anthropic, Google, HeyGen und ElevenLabs** (Details Abschnitt 2.10).

---

## 2) Daten / Benchmarks (Tag + Quelle + Datum)

### 2.1 Produkt- & Wettbewerbsrecherche

| Tool | Zweck | Preis (exakt) | API | Automatisierbar | Tag / Quelle (2026-09-24) |
|---|---|---|---|---|---|
| **Kalodata** | TikTok-Shop-Produkt-/Creator-/Video-Daten | Preisseite hinter Cloudflare-Challenge (HTTP 403 / „Just a moment") – **Nicht öffentlich verifizierbar** | Nicht verifizierbar | nur manuell/Export | https://www.kalodata.com/pricing (403) |
| **FastMoss** | TikTok-Shop-Analytics (Produkte, Shops, Creator) | Pläne Basic / Pro / Team / Enterprise; Preise werden nur clientseitig gerendert – **Nicht öffentlich verifizierbar**. Features (Verified): 90-Tage-Historie, 150 Suchen/Tag/Kategorie, Top 300, 5 Creator-Kontakte/Tag, 10 Exporte/Monat; **API nur Enterprise** („Tailored API integration") | Enterprise only | Export/CSV | Verified: https://www.fastmoss.com/pricing |
| **EchoTik** | TikTok-Shop-Analytics | Free 0 USD; Basic 9,90 USD/Nutzer/Monat (jährlich); Pro 19,10 USD; Enterprise 29,10 USD (jährlich). Pro: 1.000 Detailansichten/Tag, 2.000 Exporte/Tag | FAQ erwähnt „API calls", keine Preise → nicht verifizierbar | Export | Verified: https://echotik.live/pricing |
| **Shoplus** | TikTok-Analytics | Basic 39 USD/Monat (Top 100, 100 Details/Tag); Premium 49 USD (Top 300, 300/Tag, 2 Sub-Accounts); Professional 79 USD (unlimited, 5 Sub-Accounts) | nein (nicht gelistet) | Export | Verified: https://www.shoplus.net/pricing |
| **Tabcut** | TikTok-Shop-Daten (100 M+ Produkte, 200 M+ Influencer, 5 M+ Shops laut Seite) | Preisseite 404; Navigation nennt „API" – **Nicht öffentlich verifizierbar** | angekündigt, keine Doku | – | Verified (Feature-Claims): https://www.tabcut.com/ |
| **TikTok Shop Affiliate Center / Seller Center** | Produktauswahl, Provisionen, Sample-Requests | kostenlos für Seller/Creator | Shop-API (Partner) | teilweise | Verified (Plattform) |
| **TikTok Creative Center (TikTok One)** | Top Ads, Trends, Hashtags, Songs | kostenlos, Login nötig; „API" als Creative-Tool gelistet | Marketing-API (Ads) | teilweise | Verified: https://ads.tiktok.com/business/creativecenter/... |

Bewertung: Für einen automatisierten Research-Schritt bleibt praktisch nur Export/Scraping oder ein Enterprise-API-Deal; alle vier Drittanbieter sind primär UI-Tools.

### 2.2 Skript-Generierung (LLM-APIs, Preis pro 1 Mio. Tokens, Input/Output)

| Modell | Input | Output | Cache-Read | Batch | Tag / Quelle |
|---|---|---|---|---|---|
| Claude Fable 5.1 | 10,00 | 50,00 | 0,25 | −50 % | Verified: https://platform.claude.com/docs/en/about-claude/pricing |
| Claude Opus 5.5 | 4,00 | 20,00 | 0,20 | −50 % | Verified (ebd.) |
| Claude Opus 5 | 5,00 | 25,00 | 0,50 | −50 % | Verified (ebd.) |
| Claude Sonnet 5 | 2,00 | 10,00 | 0,20 | −50 % (Einführungspreis wurde zum Standard; Erhöhung auf 3/15 am 1.9.2026 entfällt) | Verified (ebd.) |
| Claude Haiku 4.5 | 1,00 | 5,00 | 0,10 | −50 % | Verified (ebd.) |
| GPT-6 Astra | 10,00 | 50,00 | 1,00 | – | Verified: https://developers.openai.com/api/docs/pricing |
| GPT-6 Sol | 2,00 | 10,00 | 0,20 | – | Verified (ebd.) |
| GPT-6 Luna | 0,10 | 0,50 | 0,01 | – | Verified (ebd.) |
| GPT-5.5 | 5,00 | 30,00 | 0,50 | – | Verified (ebd.) |
| GPT-5-mini | 0,25 | 2,00 | 0,025 | – | Verified (ebd.) |
| Gemini 3.1 Pro Preview (≤200k) | 2,00 | 12,00 | – | – | Verified: https://ai.google.dev/gemini-api/docs/pricing |
| Gemini 3.5 Flash | 1,50 | 9,00 | – | – | Verified (ebd.) |
| Gemini 3.5 Flash-Lite | 0,30 | 2,50 | – | – | Verified (ebd.) |
| Gemini 3.8 / 3.7 Flash (Aktionspreis bis 31.12.2026) | 0,75 | 3,75 | – | – | Verified (ebd.) |
| Gemini 2.5 Flash-Lite | 0,10 | 0,40 | – | – | Verified (ebd.) |
| MiniMax M3 | 0,30 | 1,20 | – | – | Verified: https://platform.minimax.io/docs/guides/pricing-paygo.md |

**Kosten pro Skript (Estimated):** Annahme 3.000 Input-Tokens (Produktdaten + Hook-Bibliothek) + 1.000 Output-Tokens. Sonnet 5: 3.000×2/1e6 + 1.000×10/1e6 = **0,016 USD**; Haiku 4.5: 0,008 USD; Opus 5.5: 0,032 USD; Gemini 2.5 Flash-Lite: 0,0007 USD. Mit 2 Iterationen + Research-Zusammenfassung: 0,02–0,10 USD/Video. API: ja; Persona: n/a.

### 2.3 Konsistente KI-Charaktere / Bilder

| Tool | Preis | API | Konsistente Persona? | Tag / Quelle |
|---|---|---|---|---|
| **Higgsfield** (Soul V2, Soul ID, Character Sheet, Cinema Studio, Marketing Studio/UGC) | PLUS 49 EUR/Monat (39 EUR jährlich), 1.000 Credits („~4.800 Bilder oder ~200 Videos oder ~60 Character-Generierungen", „= 600 Nano Banana Pro Gens", „~200 Kling 3.0 Videos"); ULTRA 129 EUR/Monat (99 EUR jährlich), 3.000 Credits („~500 Videos, ~100 Character-Gens"). Auto-Refill: 18 Credits/USD. Zusatz: Soul-V2-„Free Gens" (3.000/5.000/10.000), 365-Tage-Unlimited für Nano Banana, Seedream 4.5/5.0 Lite, Flux.2 Pro (1K), Kling O1 Image, GPT Image; 7-Tage-Unlimited Kling 3.0 (720p/5 s) – Aktion „Buy until Sep 25". Unlimited-Modelle nur Web, **nicht** via MCP/CLI/API | Ja (MCP, CLI, API; Modelle: Seedance 2.0/2.5, Kling 2.6/3.0, Veo 3/3.1, MiniMax H3, Wan 2.6–3.0, Sync Lipsync 3 u. a.) | **Ja** – Soul ID / Character Sheet; Seedance-2.0-Modellkarte trägt Tags „identity, consistent, multi-sku, e-commerce" (Verified) | Verified: Higgsfield MCP `show_plans_and_credits` + `models_explore`, 2026-09-24 |
| **Google Nano Banana** (Gemini 3.1 Flash Image) | 0,067 USD/Bild (1K, Standard) | Ja | Ja (Referenzbild-Editing; Claimed) | Verified: https://ai.google.dev/gemini-api/docs/pricing ; fal.ai listet „Nanobanana" 0,0398 USD/Bild (Verified: https://fal.ai/pricing) |
| **FLUX.1 Kontext [pro]** | 0,04 USD/Bild (fal.ai) | Ja | Ja (Referenz-Edit; Claimed) | Verified: https://fal.ai/models/fal-ai/flux-pro/kontext |
| **BFL direkt** | Preisseite zeigt nur Video-Kalkulator „0,17 USD/s"; Bildpreise nicht im HTML → **Nicht öffentlich verifizierbar** | Ja | – | Verified (Teil): https://bfl.ai/pricing |
| **Ideogram V3 Character** | 0,10 USD (Turbo) / 0,15 (Balanced) / 0,20 (Quality) pro Bild auf fal.ai; „Generate consistent character appearances across multiple images" | Ja | **Ja** (dediziertes Feature) | Verified: https://fal.ai/models/fal-ai/ideogram/character ; offizielle Ideogram-Preisseiten 404/Cloudflare |
| **Midjourney** | Preisseite & Doku blockiert (403/leer) → **Nicht öffentlich verifizierbar**; keine offizielle API bekannt (nicht verifizierbar) | nein (nicht verifizierbar) | –cref/omni-ref (Claimed, nicht geprüft) | https://www.midjourney.com/pricing (leer), docs.midjourney.com (403) |
| **Leonardo.ai** | Preisseite Cloudflare-Block → **Nicht öffentlich verifizierbar** | Ja (API-Seite existiert, Preise nicht abrufbar) | – | https://leonardo.ai/pricing/ (JS-Challenge) |
| **Seedream V4** | 0,03 USD/Bild (fal.ai) | Ja | Claimed | Verified: https://fal.ai/pricing |
| **Runway Gen-4 Image / Turbo** | 5–8 Credits bzw. 2 Credits/Bild = 0,05–0,08 / 0,02 USD | Ja | Referenzen (Claimed) | Verified: https://docs.dev.runwayml.com/guides/pricing/ (0,01 USD/Credit) |

Qualitätsbefund Charakter-Konsistenz (Claimed, YouTube-Tutorial „How to Make Consistent AI Characters in Higgsfield AI", Youri van Hofwegen, 46 k Views, 2026-08): Rein textbasierte Prompts erzeugten „three different faces"; ein 3-Ansichten-Character-Sheet (GPT Image 2, 4K, grauer Hintergrund) als Referenz in Seedance 2.0 hielt Gesicht/Outfit über Szenen und Outfitwechsel stabil, inkl. Lipsync. Zweite Quelle (Tao Prompts, 69 k Views, 2026-08): Seedance 2.5 „gives the most realistic expressions"; Google Omni erzeugte Charaktere, die „looked nothing like my original character reference"; MiniMax H3 hielt die Referenz „pretty similar".

### 2.4 Text-to-Video / Image-to-Video (API-Preise)

| Modell | Preis | Audio | API | Tag / Quelle |
|---|---|---|---|---|
| **Google Veo 3.1 Standard** | 0,40 USD/s (720p/1080p), 0,60 USD/s (4K) | nativ | Ja (Gemini API) | Verified: https://ai.google.dev/gemini-api/docs/pricing |
| **Veo 3.1 Fast** | 0,10 USD/s (720p), 0,12 (1080p), 0,30 (4K) | nativ | Ja | Verified (ebd.) |
| **Veo 3.1 Lite** | 0,05 USD/s (720p), 0,08 (1080p) | s. Seite | Ja | Verified (ebd.) |
| Veo 3.1 auf fal.ai | 0,20 USD/s ohne / 0,40 mit Audio (720p/1080p); 4K 0,40/0,60 | optional | Ja | Verified: https://fal.ai/models/fal-ai/veo3.1/image-to-video |
| Gemini Omni Flash (Video-Output) | 17,50 USD/1 M Video-Output-Tokens | nativ | Ja | Verified: Gemini-Preisseite |
| **OpenAI Sora 2 / Sora 2 Pro** | 0,10 USD/s (720p) bzw. 0,30/0,50/0,70 USD/s – **„Sora 2 models and Videos API were shut down on September 24, 2026"; „No one-to-one replacement API is available"** | – | **nein (abgeschaltet)** | Verified: https://developers.openai.com/api/docs/models/sora-2 , https://developers.openai.com/api/docs/guides/video-generation |
| **Kling 2.6 Pro** (fal.ai) | 0,07 USD/s ohne Audio; 0,14 mit Audio; 0,168 mit Voice-Control | optional | Ja | Verified: https://fal.ai/models/fal-ai/kling-video/v2.6/pro/image-to-video |
| **Kling 3.0 Pro** (fal.ai) | 0,112 USD/s (Audio aus) / 0,168 (Audio an) / 0,196 (Voice-Control); 5 s = 0,56/0,84 USD | optional | Ja | Verified: https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video |
| Kling 2.5 Turbo Pro (fal.ai) | 0,07 USD/s | – | Ja | Verified: https://fal.ai/pricing |
| Kling offizielle Developer-Preisseite | nur clientseitig gerendert → **Nicht öffentlich verifizierbar** | | | https://kling.ai/dev/pricing |
| **Runway Gen-4.5** | 12 Credits/s = 0,12 USD/s | – | Ja | Verified: https://docs.dev.runwayml.com/guides/pricing/ |
| **Runway Gen-4 Turbo** | 5 Credits/s = 0,05 USD/s | – | Ja | Verified (ebd.) |
| Runway Act-Two (Motion/Performance) | 5 Credits/s = 0,05 USD/s | – | Ja | Verified (ebd.) |
| Runway Abo | Free 125 Credits einmalig; Standard 15 USD/Monat (12 jährlich) 625 Credits; Pro 35 (28) 2.250 Credits; Max 95 (76) 9.500 Credits | | UI | Verified: https://runway.com/pricing |
| **MiniMax Hailuo 02 / 2.3** (offiziell) | 0,10–0,56 USD/Video (512p–1080p, 6–10 s); Paket-Effektivpreis 768p/6 s = 0,27 USD, 1080p/6 s = 0,54 USD | – | Ja | Verified: https://platform.minimax.io/docs/guides/pricing-paygo.md , .../pricing-video.md |
| Hailuo 2.3 Pro (fal.ai) | 0,49 USD/Video | – | Ja | Verified: https://fal.ai/models/fal-ai/minimax/hailuo-2.3/pro/image-to-video |
| Hailuo 02 Pro (fal.ai) | 0,08 USD/s (6 s = 0,48 USD) | – | Ja | Verified: https://fal.ai/models/fal-ai/minimax/hailuo-02/pro/image-to-video |
| **MiniMax H3** | 0,08 USD/s (768p), 0,13 USD/s (2K); H3-Max 0,05 (480p) / 0,08 (768p) | nativ | Ja | Verified: pricing-paygo.md |
| **Seedance 1.0 Pro** (fal.ai) | ≈ 0,62–0,74 USD pro 1080p/5 s (2,5–3,0 USD pro 1 M Video-Tokens) | – | Ja | Verified: https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/image-to-video |
| **Seedance 2.0** (Runway-API) | 36 Credits/s (480p/720p) = 0,36 USD/s; 40 (1080p); 150 (4K) | nativ | Ja | Verified: Runway API pricing |
| **Seedance 2.5** (Runway-API) | 720p: 30 Credits/s Output + 15 Credits/s Input (min. 80) ≈ 0,45 USD/s; 1080p: 68+34 ≈ 1,02 USD/s | nativ | Ja | Verified (ebd.) |
| **Wan 2.5** (fal.ai) | 0,05 USD/s | – | Ja | Verified: https://fal.ai/pricing |
| **WAN 3** (Runway-API) | 5 / 10 / 20 Credits/s (480p/720p/1080p) = 0,05–0,20 USD/s | – | Ja | Verified: Runway API pricing |
| **Luma Ray3.2** | 720p 5 s = 0,30 USD, 10 s = 0,90; 1080p 5 s = 1,20, 10 s = 3,60 USD | – | Ja | Verified: https://lumalabs.ai/api/pricing |
| **Pika** | Starter 10 USD/Monat (900 Credits); Creator 35 (3.150); Fancy 95 (8.550+); API nur Enterprise laut Seite | – | Enterprise | Verified: https://pika.art/pricing |
| **Grok Imagine 1.5** (Runway-API) | 10/16/29 Credits/s (480p/720p/1080p) | – | Ja | Verified (Runway API) |

**Qualitätsbefund (Claimed, YouTube-Vergleiche 2026):**
- Tao Prompts (2026-08, 69 k Views, Image-to-Video mit gleichem Prompt): Seedance 2.5 „definitely the best result", beste Mimik, bis 30 s Clips, aber „by far the most expensive" (10 s/720p ≈ 4–5 USD); MiniMax H3 ≈ 3 USD/10 s (2K), Charakterreferenz gut; Kling 3.0 ≈ 1,20–1,50 USD/10 s, „budget option", wiederkehrende Lipsync-Fehler („you hear the audio, but the lips don't move"); Google Omni: Bewegungen inkonsistent, zensiert Szenen häufiger, „prototyping tool".
- AI Yourself (2026-09-01): Kling = „production pick" (Preis planbar, natives 4K), Veo = „cinematic pick" (nativer Ton), Seedance 2.5 = Qualitäts-Benchmark, aber nur via Developer-Plattformen; „OpenAI shut the Sora app down back in April of 2026".
- Bekannte Artefakte (Claimed, mehrere Quellen): Morphing bei Objektinteraktion (Schild „materialisiert" neu), Lipsync-Drift (Kling), Farbverschiebung ggü. Referenz (Google), Körperproportionen (Seedance), Gleiten statt Gehen (Kling).

### 2.5 AI-UGC / Avatar-Tools

| Tool | Preis (exakt) | API | Konsistente Persona | Qualität (Evidenz) | Tag / Quelle |
|---|---|---|---|---|---|
| **HeyGen** | Free 0 (3 Videos/Monat ≤1 min); Creator 29 USD/Monat (24 jährlich), 600 Credits, 1080p, 1+ Custom Avatar; Pro 49 USD, 1.000 Credits, 4K; Business 149 USD + 20 USD/Seat, 1.500 Credits, 5+ Custom Avatars; Enterprise auf Anfrage. API-Preise nur im eingeloggten Dashboard („Self-serve API plans" per-operation) → **API-Preise nicht öffentlich verifizierbar**; API-Limits: Pay-as-you-go 10 parallele Workflows, Skript max. 5.000 Zeichen, Video max. 30 min | Ja | **Ja** (Digital Twin / Photo Avatar, „Looks") | Claimed (Simon Crowe, 10 k Views, 2026-03): Avatar IV ≈ 20 Credits/Minute, 1 Credit pro „Look", 2 pro Bild; „the best AI video tool that I've used so far"; Review nennt 200/2.000 Credits – weicht von aktueller Preisseite (600/1.000) ab | Verified: https://www.heygen.com/pricing , https://developers.heygen.com/docs/usage-limits.md |
| **Arcads** | Preisseite 404; Website nennt „1,000+ AI Actors", „7-day unlimited generations (Seedance 2.5 promo)". Claimed: 70 USD erster Monat, dann 100 USD/Monat, „one credit per generation", Tester erzeugte 50 Ads für 100 USD (Software Scope, 2026-03); Tinkr nennt 110 USD/Monat | nicht verifizierbar | **Ja** („My Actors"-Bibliothek, Custom Actor aus Prompt, Produkt-Integration per „New version") | Claimed (Software Scope): vorgefertigte Actors „legitimately looks like you hired a UGC creator"; Custom Actors aus Prompt: „head barely moves … voice isn't quite human … background frozen"; Fashion-Try-on und Unboxing-Presets sehr realistisch | https://www.arcads.ai/ (Verified Claims), Transkript xRq9aUkf9WY |
| **Creatify** | Starter 39 USD/Monat, 100 Credits, Wasserzeichen, 2-min-Videos; Pro 99 USD (bis −50 % jährlich), 300 Credits, 1.500 AI Actors + **3 Custom Avatars**, kein Wasserzeichen, 5 parallele Generierungen, inkl. Competitor Ad Tracker; Enterprise custom; API „Volume Based Discount" – Credit-Wert je Video **nicht verifizierbar** | Ja | Ja (3 Custom Avatars auf Pro) | Vergleichsvideos überwiegend von Creatify selbst (89 k Views) → befangen; unabhängige Tests uneinheitlich | Verified: https://creatify.ai/pricing |
| **MakeUGC** | Startup 59 USD (500 Credits), Growth 79 (1.000), Pro 149 (2.000, „Product in hand"), Enterprise custom; **API Starter 99 USD/2.000 Credits, API Pro 299 USD/6.000 Credits (5× Concurrency)**; „Seedance 2.5 Unlimited" auf Plattformplänen (nach 1-USD-Trial) | Ja | Claimed (Custom Avatar) | Nicht unabhängig geprüft | Verified: https://www.makeugc.ai/pricing |
| **Captions (Mirage)** | Free 0; Max 24,99 USD/Monat (500 Credits, „digital twins"); Frontier 1x 69,99 (1.400), 2x 139,99 (2.800), 4x 279,99 (5.600); Enterprise custom; Mirage-Credit-Kosten pro Video nicht ausgewiesen | Ja (Mirage API, Preise nicht ausgewiesen) | Ja (Digital Twin) | – | Verified: https://www.captions.ai/pricing |
| **Icon.com** | „The Agency Plan": 0 USD heute, dann **1.000 USD/Monat** nach 3-Tage-Trial; 6 **menschliche** UGC-Ads/Bestellung („100% real, no AI"), 12–16 Tage Lieferung | nein | n/a (echte Creator) | – | Verified: https://icon.com/pricing |
| **Topview** | Pro 16 USD/Monat (jährlich, 960 Credits/Jahr, „~640 s Seedance 2.5 720P"); Business 44 USD (3.000 Credits/Jahr); Ultra 50 USD (500 Credits/Monat), „API access (not with plan credits)"; Team 56 USD/Seat | Ja | Claimed (bis 200–1.000 gespeicherte Avatare, Voice-Clones) | – | Verified: https://www.topview.ai/pricing |
| **Synthesia** | Basic Free 10 min/Monat; Starter 29 USD (18 jährlich) 10 min/Monat; Creator 89 USD (64 jährlich) 30 min/Monat, **5 Personal Avatars, API mit 360 min/Jahr**; Enterprise unlimited | Ja (ab Creator) | Ja | Corporate-Look, UGC-untypisch (Einschätzung) | Verified: https://www.synthesia.io/pricing |
| **Argil** | Preise laden nur dynamisch („Loading plans…") → **Nicht öffentlich verifizierbar** | nicht verifizierbar | Claimed (Clones) | – | https://www.argil.ai/pricing |
| **Higgsfield UGC / Marketing Studio** | in PLUS/ULTRA enthalten (s. 2.3); Marketing-Studio-Videomodell 12–15 s, Avatare + Produkt-IDs, Hooks/Settings, „ad_reference" zum Nachbauen bestehender Ads | Ja (MCP/API) | Ja (Custom Avatar + Product IDs) | – | Verified: Higgsfield MCP `models_explore` |
| **TikTok Symphony Creative Studio** | **kostenlos**: „now available to all logged-in TikTok for Business users"; „free tools to make the creative production process easier"; Features: Video-Generierung aus Produkt-URL, Symphony Digital Avatars (Stock), Skript-Generator, Übersetzung/Dubbing, Editor, „Refresh Ads"; **„All content generated … that meets the requirements for disclosing the use of AI from ad policy is automatically labeled as 'AI-generated'"** | nein (UI) | nur Stock-Avatare bzw. eigener Avatar (Ads) | – | Verified: https://ads.tiktok.com/business/en-US/blog/symphony-creative-studio |

### 2.6 Lipsync

| Tool | Preis | API | Tag / Quelle |
|---|---|---|---|
| **Sync Labs (sync.so)** | Hobbyist 5 USD/Monat (1-min-Videos, 0,05 USD/s); Creator 19 USD (5 min); Growth 49 USD (0,0475 USD/s, −5 %); Scale 249 USD (0,04 USD/s, −20 %). Auf fal.ai: lipsync-2 **3,00 USD/min**, lipsync-2-pro **5,00 USD/min** | Ja | Verified: https://sync.so/pricing , https://fal.ai/models/fal-ai/sync-lipsync/v2 |
| **Kling LipSync** (fal.ai) | **0,014 USD je angefangene 5 s** Input-Video (25 s ≈ 0,07 USD) | Ja | Verified: https://fal.ai/models/fal-ai/kling-video/lipsync/audio-to-video |
| **Hedra** | Basic 20 USD (2.000 Credits), Pro 50 (7.200), Ultra 100 (18.000), Teams 75 (14.400); Credit-Kosten/Video nicht ausgewiesen | Ja („Developer platform") | Verified: https://www.hedra.com/pricing |
| **HeyGen** | Lipsync in Avatar-Credits enthalten (s. 2.5) | Ja | Verified |
| **Veo 3.1 / Kling 3.0 / Seedance 2.x native Audio** | im Videopreis enthalten (Kling: +0,056 USD/s für Audio) | Ja | Verified (2.4) |
| Higgsfield „Sync Lipsync 3" | in Credits enthalten | MCP/API | Verified (models_explore) |

### 2.7 KI-Stimme (TTS)

| Tool | Preis | API | Tag / Quelle |
|---|---|---|---|
| **ElevenLabs** | Creative Plans: Free 10 k Credits (keine kommerzielle Lizenz), Starter 6 USD (30 k), Creator 22 USD (11 USD erster Monat; 121 k), Pro 99 USD (600 k), Scale 299 (1,8 M), Business 990 (6 M). **API-Preis: v3 & Multilingual v2 0,10 USD/1.000 Zeichen; v3 Conversational & Flash/Turbo 0,05 USD/1.000 Zeichen**; API-Pläne Starter 6 USD (10 k), Creator 22 USD (220 k v3-Zeichen), Pro 99 (220 k), Scale 299 (990 k), Business 990 (2,99 M) | Ja (Pro+ bei Creative-Plänen; alle API-Pläne) | Verified: https://elevenlabs.io/pricing , https://elevenlabs.io/pricing/api , fal.ai 0,10 USD/1 k Zeichen |
| **Fish Audio** | s2.1-pro / s2-pro / s1: **15,00 USD pro 1 M UTF-8 Bytes** („≈ 180.000 englische Wörter, ~12 h Sprache"); voice-design-1 0,01 USD/Request; Concurrency-Stufen 5/15/50 ab 0/100/1.000 USD Prepaid | Ja | Verified: https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits.md |
| **OpenAI TTS** | tts-1 15 USD/1 M Zeichen; tts-1-hd 30 USD/1 M Zeichen; gpt-4o-mini-tts 12 USD/1 M Audio-Output-Tokens; gpt-realtime-2.1 Audio 32 USD In / 64 USD Out pro 1 M Tokens | Ja | Verified: https://developers.openai.com/api/docs/pricing |
| **Google Cloud TTS** | Standard 4 USD/1 M Zeichen; WaveNet 4; Neural2 16; Chirp 3 HD **30 USD/1 M Zeichen**; Instant Custom Voice 60; Studio 160; Gemini 2.5 Flash TTS 0,50 USD/1 M Text-Tokens + 10 USD/1 M Audio-Tokens; Gemini 3.1 Flash TTS 1,00 / 20,00 | Ja | Verified: https://cloud.google.com/text-to-speech/pricing (curl) |
| **Gemini API TTS** | Gemini 3.8 Flash TTS 0,50 In / 9,00 Out pro 1 M Tokens (Aktionspreis bis 31.12.2026); 3.1 Flash TTS Preview 1,00 / 20,00 | Ja | Verified: Gemini-Preisseite |
| **Cartesia (Sonic)** | Free 0 (20 k Credits ≈ 27 min); Pro 5 USD (100 k ≈ 133 min); Startup 49 USD (1,25 M ≈ 1.667 min); Scale 299 USD (8 M ≈ 10.667 min) | Ja | Verified: https://cartesia.ai/pricing |
| **MiniMax Speech** | speech-2.8-hd **100 USD/1 M Zeichen**; speech-2.8-turbo 60 USD/1 M; Voice Cloning 1,50 USD/Stimme, Voice Design 3 USD; Audio-Abo Starter 5 USD (100 k Punkte) … Business 999 USD (20 M); speech-02-hd auf fal.ai 0,10 USD/1.000 Zeichen | Ja | Verified: pricing-paygo.md, pricing-speech.md, fal.ai |

**Kosten pro 30-s-Voiceover (≈ 450 Zeichen, Estimated):** ElevenLabs v3 0,045 USD; ElevenLabs Flash 0,023; Fish s1 0,007; OpenAI tts-1 0,007; Google Chirp 3 HD 0,014; MiniMax 2.8-turbo 0,027; Cartesia Pro ≈ 0,02 (5 USD/133 min).

### 2.8 Schnitt / Captions / programmatisches Rendering

| Tool | Preis | API | Tag / Quelle |
|---|---|---|---|
| **ffmpeg / Remotion** | ffmpeg kostenlos (Open Source); Remotion-Lizenz: nicht in dieser Session geprüft → **Nicht verifiziert** (Estimated Serverkosten 5–20 USD/Monat VPS) | ja (Code) | Estimated |
| **JSON2Video** | Free 600 Credits (Wasserzeichen); Hobby 16,95 USD/Monat (jährlich 203,40), 3.000 Credits ≈ 50 min Output, max. 1 min/Video; Professional 49,95 USD, 12.000 Credits ≈ 200 min, max. 10 min; Startup 99,95 USD, 30.000 Credits ≈ 500 min; 4K = 4× Credits | Ja | Verified: https://json2video.com/pricing/ |
| **Creatomate** | Essential 2.000 Credits („200+ Videos"); Growth 10.000 („1.000+ Videos"); Beyond 50.000; „One minute of video at 720p (25 fps) is about 14 credits"; **Dollarpreise nur dynamisch gerendert → Nicht öffentlich verifizierbar** | Ja | Verified (Credits): https://creatomate.com/pricing |
| **Shotstack** | Pay-as-you-go 0,30 USD/min (+75 USD einmalig); Subscription 0,20 USD/min (39 USD/Monat); 1 Credit = 1 min unabhängig von Auflösung | Ja | Verified: https://shotstack.io/pricing/ |
| **Submagic** | Starter 19 USD/Monat (12 jährlich), 45 Credits = 15 Videos, 10 API-min/Monat; Pro 39 (23), 120 Credits = 40 Videos; Business 69 (41), 300 Credits = 100 Videos, 100 API-min; API-Packs 250–10.000 min für 57–1.000 USD/Monat | Ja | Verified: https://www.submagic.co/pricing |
| **Opus Clip** | Free; Starter 15 USD; Pro 29 USD (Video Editing API, Scheduler API, MCP, Zapier 300 Credits/Monat); Business custom | Ja (ab Pro) | Verified: https://www.opus.pro/pricing |
| **Descript** | Free (60 min, 100 Credits einmalig); Hobbyist 16 / 24 USD (Seite listet „Monthly 16 / Annual 24" – vermutlich vertauscht, jährlich 16), 400 Credits; Creator 24 / 35 USD, 800 Credits, 4K; Business 50 / 65 USD, 1.500 Credits, Custom Avatars | eingeschränkt | Verified: https://www.descript.com/pricing |
| **Captions** | s. 2.5 | Ja | Verified |
| **CapCut** | Preisseiten 404/„Not Found" → **Nicht öffentlich verifizierbar**; keine öffentliche Render-API | nein | https://www.capcut.com/pricing |

### 2.9 Scheduling / Publishing / Automations-Glue

| Tool | Preis | API | Tag / Quelle |
|---|---|---|---|
| **TikTok Content Posting API** (Direct Post) | kostenlos; **„All content posted by unaudited clients will be restricted to private viewing mode"**; „Unaudited API Clients can allow up to 5 users to post in a 24 hour window"; nach Audit öffentlich. UX-Pflichten: Creator-Info live abrufen, Nickname anzeigen, Privacy manuell wählen (kein Default), Interaktions-Checkboxen unchecked, **Commercial-Content-Disclosure-Toggle („Your brand" / „Branded content")**, Branded Content darf nicht privat sein, Upload erst nach expliziter Nutzer-Zustimmung, Domain-Verifizierung für Video-URLs | Ja | Verified: lokale Kopien developers.tiktok.com (Content Posting API Get Started; Content Sharing Guidelines) |
| **Postiz** | Standard 29 USD/Monat (5 Kanäle, unlimited Posts, API); Team 39 (10 Kanäle); Pro 49 (30); Ultimate 99 (100); Open Source self-hosted möglich; 7 Tage Trial | Ja (alle Pläne) | Verified: https://postiz.com/pricing |
| **upload-post** | Free 0 (10 Uploads/Monat, ohne TikTok); Basic 16 USD/Monat (192/Jahr) unlimited Uploads inkl. TikTok, 1 Seat; Professional 33 USD (400/Jahr), 2 Seats; Advanced 118 USD (1.411/Jahr), 5 Seats; Business 350 USD (4.205/Jahr), 10 Seats; Zusatzprofile +120–1.150 USD/Jahr | Ja | Verified: https://www.upload-post.com/ (curl) |
| **Blotato** | Starter 29 USD (20 Accounts, 1.250 AI-Credits, bis 900 TikTok-Posts/Monat); Creator 97 USD (40 Accounts, 5.000 Credits); Agency 499 USD (28.000 Credits); jährlich −17 % | Ja (nicht im Trial) | Verified: https://www.blotato.com/pricing |
| **Metricool** | Free (1 Brand, 20 Posts/Monat); Starter 20 USD (5 Brands) – 36 USD (10); Advanced 53 USD (15) – 85 (25) – 159 (50); **API nur Advanced/Custom**; TikTok-Scheduling ab Starter | Ja (Advanced+) | Verified: https://metricool.com/pricing/ |
| **Later** | Starter 18,75 USD/Monat (jährlich, 30 Posts/Profil); Growth 37,50 (180 Posts/Profil); Scale 82,50 (unlimited); TikTok Auto-Publish ja; API nicht ausgewiesen | nicht ausgewiesen | Verified: https://later.com/pricing/ |
| **Buffer** | Free (3 Kanäle, 10 Posts/Kanal, API 3.000 Requests/Monat); Essentials 5 USD/Kanal/Monat (unlimited, API 7.500); Team 10 USD/Kanal (API 15.000) | Ja | Verified: https://buffer.com/pricing |
| **n8n** | Community self-hosted kostenlos; Cloud Starter 20 EUR/Monat (jährlich) 2.500 Executions, 5 parallel; Pro 50 EUR 10.000 Executions, 20 parallel; Business 667 EUR (self-hosted) 40.000; Enterprise custom | Ja | Verified: https://n8n.io/pricing/ |
| **Make** | Free 1.000 Credits; Core 12 USD (10.000 Ops); Pro 21 USD; Teams 38 USD; Enterprise custom; jährlich −15 % | Ja | Verified: https://www.make.com/en/pricing |
| **Zapier** | Free 100 Tasks (2-Step); Professional ab 19,99 USD/Monat (jährlich) bzw. 29,99 monatlich (750 Tasks) bis 3.389/5.099 USD (2 M Tasks); Team ab 69 / 103,50 USD | Ja | Verified: https://zapier.com/pricing |
| **Higgsfield TikTok-Publishing** | MCP-Tools `tiktok_connect`, `tiktok_prepare_publish`, `tiktok_publish_status`, `tiktok_music_trending` vorhanden (in Abo enthalten) | MCP | Verified (Tool-Liste) |

### 2.10 Analytics
- **TikTok Studio / Seller Center Analytics**: kostenlos (Verified, Plattform). 
- **Kalodata / EchoTik / Shoplus**: s. 2.1.

### 2.11 Nutzungsbedingungen: Täuschung / nicht offengelegte synthetische Endorsements

| Anbieter | Relevante Klausel (Zitat) | Tag / Quelle |
|---|---|---|
| **ElevenLabs Prohibited Use Policy** | „Do not engage in unauthorized, deceptive or harmful impersonation … creating or using ElevenLabs audio output to intentionally replicate the voice of another person … without consent … [or] in a manner intended to deceive others about whether the voice was generated by artificial intelligence"; KI-Agenten „must clearly and prominently disclose to their users they are interacting with AI"; sensible Bereiche verlangen „clear disclosure regarding the use and limitations of AI" | Verified: https://elevenlabs.io/use-policy |
| **HeyGen Terms** | Verboten: „Use or distribute User Output in a misleading way, including … representing that the User Output is entirely human generated"; Pflicht, „proactively disclose that such User Output was created using artificial intelligence technologies so as not to mislead others of its origin" (wo gesetzlich gefordert); keine Bilder Dritter ohne Zustimmung; Moderation Policy: Avatare realer Personen nur mit „explicit consent" | Verified: https://www.heygen.com/terms , https://www.heygen.com/moderation-policy |
| **Google Generative AI Prohibited Use Policy** | Verboten: „Misrepresenting the provenance of generated content by claiming it was created solely by a human, in order to deceive"; „Impersonating an individual … without explicit disclosure, in order to deceive"; „Frauds, scams, or other deceptive actions" | Verified: https://policies.google.com/terms/generative-ai/use-policy |
| **Anthropic Usage Policy** | Verboten: „Generate deceptive or misleading digital content such as **fake reviews, comments, or media**"; „Impersonate a human by presenting results as human-generated"; „create fake personas to falsely attribute content or mislead others about its origin" | Verified: https://www.anthropic.com/legal/aup |
| **Runway Usage Policy** | Verboten: „Use of the service to defraud, scam, or deliberately mislead others"; Impersonation; **keine explizite Kennzeichnungspflicht** | Verified: https://runway.com/safety/usage-policy |
| **Arcads Terms** | Verboten: „carry out misleading or deceptive advertising"; Videos dürfen nicht „infringe the rules of ads platforms" oder „the rules of influence or requires the addition of compulsory information (e.g. sponsored content)"; kein Deepfake der Creator; **keine eigene AI-Disclosure-Pflicht** | Verified: https://www.arcads.ai/terms |
| **Creatify ToS** | Verboten: „deceptive, fraudulent" Assets, „impersonate"; Moderation Policy referenziert | Verified: https://creatify.ai/terms |
| **Sync.so Terms** | Impersonation verboten; **keine explizite Synthetic-Media-Kennzeichnungspflicht** | Verified: https://sync.so/terms |
| **TikTok Symphony** | automatische „AI-generated"-Kennzeichnung | Verified (2.5) |
| **TikTok Content Posting API** | Commercial-Content-Disclosure-Toggle Pflicht in der UX; Branded Content nicht privat postbar | Verified (2.9) |
| **OpenAI Usage Policies** | Seite bot-geblockt (JS-Challenge) → **Nicht abrufbar**; Sora-API ohnehin abgeschaltet | – |
| **Synthesia Terms / Moderation** | alle getesteten URLs 404 → **Nicht abrufbar** | – |

**Folge:** Ein Workflow „KI-Persona empfiehlt Produkt ohne Kennzeichnung" verstößt gegen die AUP von Anthropic (fake media/personas), Google (Provenance), HeyGen (Disclosure) und ElevenLabs (Deception about AI voice); zusätzlich greifen TikToks eigene Regeln (AIGC-Label, Branded-Content-Disclosure) und Werberecht (W1-Report).

---

## 3) Annahmen-Set & Monatsbudget (Estimated)

### 3.1 Referenzvideo
25–30 s TikTok-Shop-Video = 4 Clips à 6 s (24 s generiert) + Voiceover 450 Zeichen + Captions + Produkt-Overlay. Retry-Faktor (Ausschuss/Regenerierung): aggressiv 1,3, realistisch 1,5, konservativ 1,5.

### 3.2 Variable Kosten pro Video (Formeln)

| Posten | Aggressiv | Realistisch | Konservativ |
|---|---|---|---|
| Skript (LLM) | Haiku 4.5, 4 k Tokens ≈ 0,01 USD | Sonnet 5, 2 Calls ≈ 0,03 USD | Opus 5.5, 3 Calls ≈ 0,10 USD |
| Charakter-/Keyframes | 1 × Flux Kontext 0,04 USD | 3 × Nano Banana 0,067 = 0,20 USD | 4 × Nano Banana + 1 × Ideogram Character (0,20) = 0,47 USD |
| Video (24 s) | Veo 3.1 Lite 720p 0,05 USD/s × 24 × 1,3 = **1,56 USD** (Alternative Wan 2.5 gleich) | Kling 2.6 Pro ohne Audio 0,07 USD/s × 24 × 1,5 = **2,52 USD** (Alt.: Hailuo 2.3 Pro 4 × 0,49 × 1,5 = 2,94) | Veo 3.1 Standard 0,40 USD/s × 24 × 1,5 = **14,40 USD** (Alt.: Seedance 2.5 via Runway 720p ≈ 0,45 USD/s × 24 × 1,5 = 16,20) |
| TTS (450 Zeichen) | Fish s1 0,007 USD | ElevenLabs v3 0,045 USD | ElevenLabs v3 0,045 USD |
| Lipsync | keine (Voiceover über B-Roll) | Kling LipSync 0,07 USD (25 s) | Sync lipsync-2-pro 5 USD/min × 0,5 = 2,50 USD |
| Rendering/Captions | ffmpeg self-host ≈ 0 | Shotstack 0,20 USD/min × 0,5 = 0,10 USD | JSON2Video Professional ≈ 0,25 USD/min × 0,5 + Submagic ≈ 0,40 USD |
| **Summe variabel** | **≈ 1,62 USD** | **≈ 2,97 USD** | **≈ 17,90 USD** |

Hinweis: HeyGen-Avatar-Route als Ersatz für Video+Lipsync: 30 s ≈ 10 Credits (Claimed 20 Credits/min) → Pro 49 USD/1.000 Credits ≈ **0,49 USD/Video** für ~100 Videos/Monat; darüber Business (1.500 Credits) bzw. Enterprise – für 900 Videos (9.000 Credits) nicht mit Standardplänen abdeckbar.

### 3.3 Fixkosten pro Monat (Tool-Stack)

| Posten | Aggressiv | Realistisch | Konservativ |
|---|---|---|---|
| Recherche | TikTok Affiliate/Creative Center 0 + EchoTik Basic 9,90 | EchoTik Pro 19,10 + Shoplus Basic 39 | Shoplus Professional 79 + EchoTik Enterprise 29,10 (Kalodata: Preis nicht verifizierbar, nicht eingerechnet) |
| Automation | n8n self-hosted 0 + VPS 10 | n8n Cloud Starter ≈ 22 (20 EUR) + VPS 10 | n8n Cloud Pro ≈ 55 (50 EUR) + VPS 20 |
| Publishing | upload-post Basic 16 | Postiz Standard 29 | Blotato Creator 97 |
| Avatar-SaaS (Backup/Talking-Head) | – | HeyGen Creator 29 | HeyGen Pro 49 + Higgsfield ULTRA ≈ 140 (129 EUR) |
| Schnitt/Captions | ffmpeg 0 | Submagic Pro 39 | Descript Creator 35 |
| **Summe fix** | **≈ 36 USD** | **≈ 187 USD** | **≈ 504 USD** |

Skalierungszuschlag: ab 300 Videos/Monat n8n Pro statt Starter (+33 USD) und mehr Rendering-Kapazität (+20 USD); ab 900 zusätzlich Postiz Team/mehr Seats und größerer VPS (+60 USD gesamt). Persönliche Arbeitszeit (QC, Kommentare, Produktbeschaffung) und Ads-Budget sind **nicht** enthalten.

### 3.4 Monatsbudget (Estimated; Formel: Fix + Zuschlag + Videos × variabel)

| Videos/Monat | Aggressiv | Realistisch | Konservativ |
|---|---|---|---|
| **30** | 36 + 30×1,62 = **85 USD (2,83/Video)** | 187 + 30×2,97 = **276 USD (9,20/Video)** | 504 + 30×17,90 = **1.041 USD (34,70/Video)** |
| **90** | 36 + 146 = **182 USD (2,02/Video)** | 187 + 267 = **454 USD (5,05/Video)** | 504 + 1.611 = **2.115 USD (23,50/Video)** |
| **300** | 36 + 33 + 486 = **555 USD (1,85/Video)** | 187 + 53 + 891 = **1.131 USD (3,77/Video)** | 504 + 53 + 5.370 = **5.927 USD (19,76/Video)** |
| **900** | 36 + 93 + 1.458 = **1.587 USD (1,76/Video)** | 187 + 113 + 2.673 = **2.973 USD (3,30/Video)** | 504 + 113 + 16.110 = **16.727 USD (18,59/Video)** |

Sensitivität: Der Videomodell-Preis dominiert. Wechsel von Kling 2.6 Pro (0,07 USD/s) auf Veo 3.1 Fast (0,10 USD/s) erhöht die realistischen Variablen um ≈ 1,08 USD/Video; auf Seedance 2.5 (≈ 0,45 USD/s) um ≈ 13,7 USD/Video. Higgsfield-Abo (1.000 Credits ≈ „~200 Kling-3.0-Videos" laut Anbieter) kann bei ≤ 200 Clips/Monat günstiger sein als API-Pay-per-use (49 EUR ≈ 0,27 USD/Clip), ist aber nicht headless nutzbar für Unlimited-Modelle.

### 3.5 Skalierungsgrenzen (Verified/Claimed)
- TikTok Direct Post: ungeprüfte Clients nur privat, 5 Nutzer/24 h (Verified). Tages-Post-Limits pro Account: in den abgerufenen Docs nicht beziffert → nicht verifizierbar.
- HeyGen API: 10 parallele Workflows Pay-as-you-go (Verified).
- Fish Audio: 5 parallele Requests < 100 USD Prepaid (Verified).
- Ideogram API: 10 Inflight-Requests Standard (Verified).
- n8n Starter: 2.500 Executions/Monat, 5 parallel (Verified) – bei ~5 Executions/Video reicht das für ≈ 500 Videos.

---

## 4) Nicht verfügbar / offen

- **Kalodata**-Preise (Cloudflare-Block), **FastMoss**-Preise (nur JS), **Tabcut**-Preise (404), **Midjourney**-Preise (Seite leer/403), **Leonardo**-Preise (JS-Challenge), **Ideogram**-Offizialpreise (404; nur fal.ai-Preise), **Kling**-Offizialpreise (JS; nur fal.ai/Higgsfield), **BFL**-Bildpreise (nicht im HTML), **Creatomate**-Dollarpreise (dynamisch), **CapCut**-Preise (404), **Argil**-Preise (dynamisch), **Arcads**-Preise (404; nur Claimed 100–110 USD/Monat), **HeyGen-API**-Preise (nur eingeloggt), **Creatify**/**Captions**/**Hedra** Credit-Kosten pro Video.
- **OpenAI Usage Policies** und **Synthesia Terms** nicht abrufbar (Bot-Block/404).
- **Remotion**-Lizenzkosten nicht geprüft.
- **TikTok-Shop-eigene Seller-KI-Tools** (z. B. „AI Cast"/Smart Creation im Seller Center) in dieser Session nicht verifiziert; belegt ist nur Symphony Creative Studio (TikTok for Business, kostenlos, Auto-Label).
- Tages-/Wochen-Limits für TikTok-Posts pro Account (Spam-Schwellen) nicht öffentlich beziffert.
- Unabhängige, quantitative Qualitäts-Benchmarks (Ausschussquote pro Modell) existieren nur als YouTube-Einzeltests (Claimed); die genannten Retry-Faktoren 1,3–1,5 sind Schätzungen.
- Descript-Preisseite listet Monats-/Jahrespreise möglicherweise vertauscht.

---

## 5) Quellen (alle Zugriff 2026-09-24)

- https://platform.claude.com/docs/en/about-claude/pricing ; https://claude.com/pricing
- https://developers.openai.com/api/docs/pricing ; https://developers.openai.com/api/docs/models/sora-2 ; https://developers.openai.com/api/docs/models/sora-2-pro ; https://developers.openai.com/api/docs/guides/video-generation
- https://ai.google.dev/gemini-api/docs/pricing ; https://cloud.google.com/text-to-speech/pricing ; https://policies.google.com/terms/generative-ai/use-policy
- https://www.anthropic.com/legal/aup
- https://elevenlabs.io/pricing ; https://elevenlabs.io/pricing/api ; https://elevenlabs.io/use-policy
- https://www.heygen.com/pricing ; https://developers.heygen.com/docs/usage-limits.md ; https://developers.heygen.com/docs/api-key.md ; https://www.heygen.com/terms ; https://www.heygen.com/moderation-policy
- Higgsfield MCP: `show_plans_and_credits`, `models_explore` (2026-09-24)
- https://www.fastmoss.com/pricing ; https://echotik.live/pricing ; https://www.shoplus.net/pricing ; https://www.tabcut.com/ ; https://www.kalodata.com/pricing (403)
- https://creatify.ai/pricing ; https://creatify.ai/terms ; https://www.arcads.ai/ ; https://www.arcads.ai/terms ; https://www.makeugc.ai/pricing ; https://www.captions.ai/pricing ; https://icon.com/pricing ; https://www.topview.ai/pricing ; https://www.synthesia.io/pricing ; https://www.argil.ai/pricing
- https://ads.tiktok.com/business/en-US/blog/symphony-creative-studio ; https://ads.tiktok.com/business/creativecenter/... ; developers.tiktok.com (Content Posting API Get Started; Content Sharing Guidelines – lokale Kopien)
- https://sync.so/pricing ; https://sync.so/terms ; https://fal.ai/models/fal-ai/sync-lipsync/v2 ; https://fal.ai/models/fal-ai/kling-video/lipsync/audio-to-video ; https://www.hedra.com/pricing
- https://fal.ai/pricing ; https://fal.ai/models/fal-ai/kling-video/v2.6/pro/image-to-video ; https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video ; https://fal.ai/models/fal-ai/veo3.1/image-to-video ; https://fal.ai/models/fal-ai/minimax/hailuo-02/pro/image-to-video ; https://fal.ai/models/fal-ai/minimax/hailuo-2.3/pro/image-to-video ; https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/image-to-video ; https://fal.ai/models/fal-ai/flux-pro/kontext ; https://fal.ai/models/fal-ai/ideogram/character ; https://fal.ai/models/fal-ai/minimax/speech-02-hd ; https://fal.ai/models/fal-ai/elevenlabs/tts/multilingual-v2
- https://docs.dev.runwayml.com/guides/pricing/ ; https://runway.com/pricing ; https://runway.com/safety/usage-policy ; https://runway.com/terms-of-use
- https://platform.minimax.io/docs/guides/pricing-paygo.md ; .../pricing-video.md ; .../pricing-speech.md
- https://lumalabs.ai/api/pricing ; https://pika.art/pricing ; https://bfl.ai/pricing
- https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits.md ; https://cartesia.ai/pricing
- https://json2video.com/pricing/ ; https://creatomate.com/pricing ; https://shotstack.io/pricing/ ; https://www.submagic.co/pricing ; https://www.opus.pro/pricing ; https://www.descript.com/pricing
- https://postiz.com/pricing ; https://www.upload-post.com/ ; https://www.blotato.com/pricing ; https://metricool.com/pricing/ ; https://later.com/pricing/ ; https://buffer.com/pricing ; https://n8n.io/pricing/ ; https://www.make.com/en/pricing ; https://zapier.com/pricing
- YouTube (NexLev-Transkripte, Claimed): „Arcads Review: I Spent $100 Making 50 UGC Ads" (Software Scope, xRq9aUkf9WY, 2026-03-16); „HeyGen Review 2026" (Simon Crowe, 3Qlz_FIbw5w); „How to Make Consistent AI Characters in Higgsfield AI" (Youri van Hofwegen, ZsrhdgG0I1E); „Seedance 2.5 vs Minimax H3 vs Google Omni vs Kling 3.0" (Tao Prompts, G5D053drKB8); „Veo 3.1 vs Kling 3.0 vs Seedance 2.5: Which Should You Pay For?" (AI Yourself, jtNvYY_ultg, 2026-09).

---

## Verifikation (adversarial)

Gegenprüfung am 2026-09-24 durch erneutes Öffnen aller Quell-URLs (WebFetch). Alle Preise in USD, Listenpreise ohne Volumen-/Enterprise-Rabatte.

| Metrik | Verdict | Notiz |
|---|---|---|
| OpenAI Sora 2 / Sora 2 Pro Videos API – Status | **CONFIRMED** | Guide-Seite (developers.openai.com/api/docs/guides/video-generation) sagt wörtlich: „The Sora 2 models and Videos API were shut down on September 24, 2026", „This guide is retained for historical reference", „No one-to-one replacement API is available". Modelle `sora-2`, `sora-2-pro`; keine Preise mehr auf der Seite. Achtung: Abschaltdatum = heutiges Datum, d. h. Aussage ist tagesaktuell und frisch. |
| Claude Sonnet 5 API-Preis (Input/Output je 1M Tokens) | **CONFIRMED** | Preistabelle: $2 / MTok Input, $10 / MTok Output; Batch-Tabelle $1 / $5 (= −50 %). Fußnote 3: Einführungspreis wurde zum Standardpreis, die für 1.9.2026 geplante Erhöhung auf $3/$15 entfällt. Cache-Hit $0.20 / MTok. |
| Claude Opus 5.5 / Haiku 4.5 je 1M Tokens | **CONFIRMED** | Opus 5.5: $4 / $20 (Batch $2 / $10; Cache-Hit $0.20 = 0,05× Basis; Fast Mode $8 / $40). Haiku 4.5: $1 / $5 (Batch $0.50 / $2.50; Cache-Hit $0.10). |
| OpenAI GPT-5-mini / GPT-6 Sol / GPT-6 Astra je 1M Tokens | **CONFIRMED** | Standard-Tier-Zeilen: `gpt-5-mini` $0.25 / $2.00 (cached $0.025); `gpt-6-sol` $2.00 / $10.00 (cached $0.20); `gpt-6-astra` $10.00 / $50.00 (cached $1.00). Keine Sora-/Videopreise mehr auf der Pricing-Seite. |
| Gemini 2.5 Flash-Lite / 3.5 Flash je 1M Tokens | **CONFIRMED** | 2.5 Flash-Lite: $0.10 (Text/Bild/Video; Audio $0.30) / $0.40; Batch $0.05 / $0.20. 3.5 Flash: Paid Tier $1.50 / $9.00, Batch $0.75 / $4.50; Free Tier existiert (kostenlos, Rate-Limits). |
| Veo 3.1 je Sekunde (Standard / Fast / Lite, 720p) | **CONFIRMED** | Standard $0.40/s (720p/1080p), $0.60 (4K); Fast $0.10/s (720p), $0.12 (1080p), $0.30 (4K); Lite $0.05/s (720p), $0.08 (1080p). Definition: Preis pro generierter Videosekunde, Gemini API. |
| Nano Banana (Gemini 3.1 Flash Image) je Bild | **CONFIRMED** | Gemini 3.1 Flash Image („Nano Banana 2"): Output $60 / 1M Tokens = „$0.067 per 1K image" (Standard); Batch $30 / 1M = $0.034 je 1K-Bild; Input $0.50 / 1M. Preis gilt für 1K-Auflösung; höhere Auflösungen kosten mehr Tokens. |
| Kling 2.6 Pro / Kling 3.0 Pro je Sekunde auf fal.ai (ohne Audio) | **CONFIRMED** | v2.6 Pro (fal.ai/models/fal-ai/kling-video/v2.6/pro/image-to-video): $0.07/s ohne Audio, $0.14/s mit Audio, $0.168/s mit Voice-Control; 5 s oder 10 s. v3 Pro (…/v3/pro/image-to-video): $0.112/s Audio aus, $0.168/s Audio an, $0.196/s Voice-Control; bis 15 s (5 s = $0.56 / $0.84). Basis: fal.ai-Marktplatzpreise, nicht Kling-Offizialpreise (letztere nicht verifizierbar, s. Abschnitt 4). |

Ergebnis: 8/8 CONFIRMED. Keine Abweichungen zwischen Bericht und Quellseiten gefunden.
