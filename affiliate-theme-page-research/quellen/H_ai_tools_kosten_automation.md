# H – AI-Tools, Kosten & Automatisierung (Stand: 2026-09-26)

**Studie:** KI-generierte faceless Instagram-Reels-Theme-Page mit Affiliate-Monetarisierung; Ziel 2–4 hochwertige Reels/Tag (60–120/Monat), Batch-Produktion am Wochenende, maximale Automatisierung mit Claude Code/Codex.
**Rolle:** AI-Content-Production- & Automatisierungs-Analyst
**Prüfdatum aller Primärquellen:** 2026-09-26 (sofern nicht anders angegeben)

## Legende Datenqualität

| Label | Bedeutung |
|---|---|
| **VERIFIED** | Primärquelle (Preisseite, API-Doku, Hersteller-Doku oder Live-Preis-Config via Anbieter-MCP) am 2026-09-26 abgerufen |
| **THIRD-PARTY ESTIMATE** | Sekundärquelle (Blog, Vergleichsseite, Reseller) – Datum der Drittquelle angegeben |
| **CLAIMED** | Herstelleraussage zu Fähigkeiten/Qualität (Marketing), nicht unabhängig getestet |
| **UNKNOWN** | Nicht verifizierbar. **UNKNOWN\*** = Orientierungswert aus Vorwissen (≤ Mitte 2026), am Prüfdatum NICHT re-verifiziert – vor Nutzung prüfen |
| **MODEL ASSUMPTION** | Eigene Modellannahme mit offengelegtem Rechenweg |

Hinweis zur Methodik: Das Websuch-Kontingent der Session war nach der ersten Recherchephase erschöpft; danach wurden ausschließlich bekannte Primär-URLs direkt abgerufen (WebFetch/curl), ergänzt um read-only Abfragen des Higgsfield-MCP (`models_explore`, `show_plans_and_credits`) und der NexLev-Datenbank. Es wurden **keine** Generierungen gestartet und nichts gekauft. Preise für generative KI ändern sich monatlich – alle Zahlen sind Momentaufnahmen.

---

## Executive Summary (Kernbefunde)

1. **Sora ist raus:** OpenAI hat die Sora-App am 26.04.2026 eingestellt und die Videos-API inkl. `sora-2`/`sora-2-pro` am **24.09.2026 abgeschaltet** (VERIFIED, OpenAI Deprecations). Sora ist für die Pipeline keine Option mehr – auch die Frage nach EU/DE-Verfügbarkeit ist damit erledigt.
2. **Preisanker Video (API, pro generierter Sekunde):** Veo 3.1 Lite 720p **$0.05**, Veo 3.1 Fast 1080p **$0.12**, Veo 3.1 Standard 1080p **$0.40** (alle inkl. Audio, VERIFIED Google); Kling 3.0 Standard via fal **$0.084** (ohne Audio) / Pro **$0.112–0.168** (VERIFIED fal); Wan 2.5 via fal **$0.05** (VERIFIED); Seedance 2.5 720p **~$0.23–0.47** (THIRD-PARTY); Gemini Omni Flash 720p **~$0.10** (VERIFIED).
3. **Kosten pro Reel (nur Generierung, Mittelszenario 4 Clips × 6 s × 2,5 Versuche + 12 Bilder):** günstig **~$3.5–5.6**, mittel **~$8**, premium **~$12–26** (MODEL ASSUMPTION, Abschnitt 9).
4. **Monatlich inkl. Fixkosten (Mittelszenario):** 60 Reels ≈ **$320–440 (günstig)** / **~$1.9k (premium)**; 120 Reels ≈ **$530–775 (günstig)** / **~$3.4k (premium)**.
5. **Produkt-Treue ist der Engpass:** Alle führenden Modelle bieten Referenzbild-Funktionen (Veo „Ingredients" bis 3 Bilder, Kling 3.0 Omni „Elements", Seedance 2.x Multi-Reference, Nano Banana Pro bis 6 Objekt-Referenzen) – aber es existiert **kein unabhängiger quantitativer Benchmark** zur Logo-/Text-/Form-Treue. Empfehlung: „echte Pixel fürs Produkt" (Freisteller + generierte Szene, wenig Bewegung, echtes Produktfoto im End-Frame) statt Produkt komplett vom Videomodell rendern lassen.
6. **Posting-APIs:** Instagram Graph API unterstützt Reels (inkl. **Trial Reels** und Paid-Partnership-Label), Limit **100 API-Posts/24 h** (VERIFIED). TikTok Direct Post nur nach **Audit** öffentlich, typ. **~15 Posts/Tag/Creator**, Richtlinien schließen reine Privat-/Interne-Tools aus → praktisch Scheduler nutzen. YouTube: **100 Uploads/Tag** Default, unverifizierte Projekte laden nur **privat** hoch (VERIFIED).
7. **Manueller Aufwand (MODEL ASSUMPTION):** ~**7,5–13 h/Woche** bei 60 Reels/Monat, ~**13–20 h/Woche** bei 120 Reels/Monat (nach 40–80 h Initial-Setup). Human-in-the-Loop bleibt v. a. bei Video-QA/Produkt-Treue, Compliance (Werbe-/KI-Kennzeichnung) und Winner-Interpretation.

---

## 1. AI-Video-Modelle (Stand Sept. 2026)

### 1.1 Preis- und Fähigkeitsübersicht

| Tool / Modell | Fähigkeit (Länge, Auflösung, Audio, Referenzen) | Preis | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **Google Veo 3.1 (Standard)** | 4/6/8 s; 720p, 1080p & 4K (nur 8 s); 16:9 & **9:16**; native Audio immer an; **bis 3 Referenzbilder („asset")** – dann 8 s Pflicht; First/Last-Frame; Extension bis **148 s** (nur 720p); SynthID-Wasserzeichen; Videos 2 Tage auf Server | **$0.40/s** (720p/1080p), **$0.60/s** (4K) | https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/docs/veo | 2026-09-26 (Seite aktualisiert 24.09.2026) | VERIFIED |
| **Veo 3.1 Fast** | wie oben inkl. Referenzbilder/Extension | **$0.10/s** 720p, **$0.12/s** 1080p, **$0.30/s** 4K | wie oben | 2026-09-26 | VERIFIED |
| **Veo 3.1 Lite** | 720p/1080p (1080p nur 8 s); **keine** Referenzbilder, **keine** Extension/First-Last-Frame lt. Doku; I2V mit Startbild (lt. Higgsfield-Modellkatalog) | **$0.05/s** 720p, **$0.08/s** 1080p | wie oben; Higgsfield MCP `models_explore` | 2026-09-26 | VERIFIED |
| Veo 3.1 Fast via fal.ai | Reseller | $0.10/s ohne / $0.15/s mit Audio (720p/1080p); 4K $0.30/$0.35 | https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video | 2026-09-26 | VERIFIED (Reseller-Preisseite) |
| Veo – EU-Einschränkung | In EU/UK/CH/MENA nur `personGeneration=allow_adult` (keine Kinder-Darstellung) | – | https://ai.google.dev/gemini-api/docs/veo | 2026-09-26 | VERIFIED |
| **Google Gemini Omni Flash / 1.1** (neu) | Konversationelle Video-Generierung & -Editing mit Audio; Bild-/Video-Referenzen; 1.1 (Preview seit 27.08.2026): Extension in 10-s-Schritten bis 40 s, First/Last-Frame, 360p-Draft, 4K | **~$0.10/s bei 720p** (Token-basiert: $17.50/1M Video-Output-Token, 5.792 Token/s); 360p ~$0.03, 1080p ~$0.15, 4K ~$0.30/s | https://ai.google.dev/gemini-api/docs/pricing ; https://www.eesel.ai/blog/gemini-omni-1-1-flash-pricing | 2026-09-26 / eesel o. D. | VERIFIED (720p) / THIRD-PARTY ESTIMATE (übrige Auflösungen) |
| **Kling 3.0 (Standard) via fal** | I2V, 3–15 s, Elements (@Element1…) für Produkt/Charakter | **$0.084/s** ohne Audio, $0.126/s mit Audio, $0.154/s mit Voice-Control | https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video | 2026-09-26 | VERIFIED (Reseller) |
| **Kling 3.0 Pro via fal** | max. 15 s; Elements mit Frontal- + Seitenansicht als Referenz | **$0.112/s** ohne Audio, **$0.168/s** mit Audio, $0.196/s Voice | https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video | 2026-09-26 | VERIFIED (Reseller) |
| Kling offizielle API (kling.ai/dev) | Prepaid-Pakete (unabhängig vom Consumer-Abo); V3-Omni 1,0 Unit/s, V3 1,2 Units/s (1080p); Paket ab **$700 / 5.000 Units / 180 Tage**, 20 parallele Requests; fehlgeschlagene Tasks kosten nichts | ~$0.14/Unit → 5 s 1080p mit Audio (V3-Omni) ≈ **$0.70** | https://www.cloudzero.com/blog/kling-ai-pricing/ ; kling.ai/dev/pricing (JS, nicht auslesbar) | 18.09.2026 | THIRD-PARTY ESTIMATE |
| Kling Consumer-Abos | Standard $10, Pro $37, Premier $92, Ultra $180/Monat; Kling 3.0: 6 Credits/s (720p ohne Audio), 12 Credits/s (1080p mit Audio), 30 Credits/s (4K); Free = Wasserzeichen, **keine kommerziellen Rechte** | s. links | https://www.cloudzero.com/blog/kling-ai-pricing/ | 18.09.2026 | THIRD-PARTY ESTIMATE |
| **Kling 3.0 Omni** (Fähigkeiten) | bis 15 s, bis 6 Kameraschnitte/Generation, native Audio (EN/ZH/JA/KO/ES), Multi-Image- & Element-Referenz; „native level text rendering", Logos/Labels „precise lettering" | – | https://kling.ai/blog/kling-video-3-omni-multi-shot-native-audio-guide | 26.06.2026 | CLAIMED |
| **ByteDance Seedance 2.0** | 4–15 s, 480p–4K (4K/1080p nur „std"-Mode), Bild-/Video-/Audio-Referenzen, „consistent identity, multi-SKU, e-commerce" | BytePlus: $0.04–0.78/s je nach Auflösung; 720p t2v mit Audio ~$0.19/s (Apiframe) | https://apiframe.ai/models/seedance-2.0/pricing ; Higgsfield MCP | 2026 / 2026-09-26 | THIRD-PARTY ESTIMATE (Preis) / CLAIMED (Fähigkeit) |
| **Seedance 2.5** (Release 31.07.2026) | 4–30 s, nativ 480p/720p (1080p/4K bei Resellern = Upscale), Audio inklusive, Omni-Reference, Video-Edit, Video-Extension | 720p: Replicate **$0.231/s**, Atlas $0.30, fal **$0.473/s**; 480p ab $0.10/s; 1080p $0.21 (WaveSpeed Turbo) – ~$1.14/s (fal) | https://cellcog.ai/blog/seedance-2-5-pricing/ | 22.08.2026 (upd. 08.09.2026) | THIRD-PARTY ESTIMATE |
| **Runway Gen-4.5** (API) | – | **12 Credits/s = $0.12/s** ($0.01/Credit); über Runway-API auch Veo 3.1 (10–40 Cr/s), Seedance 2.5 (20–68 Cr/s), Wan 3 (5–20 Cr/s); „Product Ad"-Recipe 720p: 200 Cr für 4 s + 36 Cr/Zusatzsekunde | https://docs.dev.runwayml.com/guides/pricing/ | 2026-09-26 | VERIFIED |
| **Luma (Ray 3 / Ray 3.x)** | bis 18 s; Credits werden bei Submit (nicht bei Erfolg) abgezogen | Abos: Lite $9.99 (nicht kommerziell), Plus $29.99, Unlimited $94.99; Ray 2 API ~ $0.95/5 s 1080p; Ray 3 API ~ $0.21/s (Vergleichsseite, inkonsistent) | https://www.eesel.ai/blog/luma-ai-pricing ; https://www.buildmvpfast.com/api-costs/ai-video | 05.06.2026 / Juli 2026 | THIRD-PARTY ESTIMATE (niedrige Qualität) |
| **MiniMax Hailuo 2.3 / H3 / H3 Max** | Hailuo 2.3: 6/10 s, 768p–1080p; H3: 4–15 s, 2K, Keyframes + Bild/Video/Audio-Referenzen | Hailuo 02 ~ $0.045/s (Vergleichsseite); H3: UNKNOWN | Higgsfield MCP; https://www.buildmvpfast.com/api-costs/ai-video | 2026-09-26 / Juli 2026 | THIRD-PARTY ESTIMATE / UNKNOWN |
| Hailuo 2.3 Logo-Treue | „keeps logos and on-screen text sharp" | – | https://higgsfield.ai/blog/5-Best-AI-Video-Models-2026-Tested-Compared | 29.08.2026 | CLAIMED (Aggregator-Blog) |
| **Wan 2.5** (API) | Alibaba | **$0.05/s** (fal) | https://fal.ai/pricing | 2026-09-26 | VERIFIED (Reseller) |
| Wan 2.6 / 2.7 / 3.0 / 3.0 Prime | 2.6: 5/10/15 s, 720p/1080p; 3.0: 2–30 s, 480p–1080p, Multi-Reference, native Audio, „thinking"-Modus | Pika: Wan 3.0 720p 5 s = 33 Credits (60 Credits = $1 → **~$0.55/Clip ≈ $0.11/s**); Runway: Wan 3 5–20 Cr/s ($0.05–0.20/s) | Higgsfield MCP; https://pika.art/pricing ; Runway-Docs | 2026-09-26 | VERIFIED (Reseller-Preise) |
| **Wan 2.2 (Open Source)** | TI2V-5B: 720p, 24 fps, 5 s, läuft ab 24 GB VRAM (RTX 4090), 5-s-Clip < 9 min; **Apache 2.0**; Wan 2.5+ nicht als Open Weights auf HF | Self-Hosting: nur GPU-Kosten | https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B ; https://huggingface.co/Wan-AI | 2026-09-26 | VERIFIED |
| **LTX-2.5 (Lightricks, Open Weights)** | 19B, T2V/I2V mit **nativer Audio**, bis 3840×2176 (mit 2×-Upscaler), 121 Frames/Clip; Release 06.01.2026 | Self-Hosting kostenlos; **kommerziell frei < $10 Mio. Jahresumsatz** (LTX-2.x Community License) | https://huggingface.co/Lightricks/LTX-2.5 | 2026-09-26 | VERIFIED |
| **FLUX 3 Video** (Black Forest Labs, neu) | T2V, Multi-Frame-I2V, Continuation, Audio; 5–20 s, 720p/1080p | $0.17–0.80/s (T2V), Draft $0.06–0.12/s, Video-Edit $0.03/s | https://docs.bfl.ml/quick_start/pricing | 2026-09-26 | VERIFIED |
| **Pika** | Plattform mit Drittmodellen (Seedance 2.5, Wan 3.0) | Starter $10 (900 Cr, **keine kommerzielle Lizenz**), Creator $35 (3.150 Cr, kommerziell), Fancy ab $95; 60 Cr = $1; Seedance 2.5 720p 5 s = 122 Cr (~$2.03); Top-up-Credits **nicht** per API nutzbar | https://pika.art/pricing | 2026-09-26 | VERIFIED |
| **Midjourney Video (V1)** | Animiert MJ-Bilder, 5 s + Extensions bis ~20 s; 480p (HD nur höhere Pläne); **kein offizielles API** | Basic $10, Standard $30, Pro $60, Mega $120/Monat (–20 % jährlich); Firmen > $1 Mio. Umsatz brauchen Pro/Mega | https://www.eesel.ai/blog/midjourney-pricing ; docs.midjourney.com (403) | 2026 | THIRD-PARTY ESTIMATE / UNKNOWN\* (API, Umsatzregel) |
| **OpenAI Sora 2 / 2 Pro** | **Eingestellt:** App 26.04.2026, API (`sora-2`, `sora-2-pro`, Snapshots) abgeschaltet **24.09.2026**; kein Nachfolger angekündigt. Historischer Preis: $0.10/s (720p), Pro $0.30–0.70/s | – | https://developers.openai.com/api/docs/deprecations ; https://costgoat.com/pricing/sora | 2026-09-26 | VERIFIED |
| Sora EU/DE-Verfügbarkeit | Consumer-App war nach Vorwissen nie offiziell in der EU gestartet; API war in DE nutzbar – beides jetzt irrelevant | – | – | – | UNKNOWN\* |
| **xAI Grok Video 1.5** | 2–15 s, 480p–1080p, Bild- & Audio-Referenzen | Grok Imagine Video ~ $0.05/s | Higgsfield MCP; buildmvpfast | 2026-09-26 / Juli 2026 | THIRD-PARTY ESTIMATE |

### 1.2 Higgsfield (Aggregator)

| Aspekt | Befund | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|
| **Pläne (EUR, zzgl. MwSt.)** | **Plus €49/Monat** (jährlich €39/Monat) = 1.000 Credits/Monat, 6 parallele Videos/8 Bilder; **Ultra €129/Monat** (jährlich €99/Monat) = 3.000 Credits, 8 parallele Videos, „70 % cheaper per credit"; Auto-Refill-Kurs 18 Credits/$ (~$0.056/Credit); Top-up-Credits verfallen nach 90 Tagen | Higgsfield MCP `show_plans_and_credits` (Live-Pricing-Config) | 2026-09-26 | VERIFIED |
| Starter-Plan | $19/Monat, 270 Credits (im MCP-Widget nicht angezeigt) | https://www.scopeful.org/blog/higgsfield-pricing-2026 | 07.08.2026 | THIRD-PARTY ESTIMATE |
| Credits je Modell | Anbieterangabe: 1.000 Cr ≈ 200 Kling-3.0-Videos (≈ 5 Cr) ≈ 600 Nano-Banana-Pro-Bilder (≈ 1,7–2 Cr); 100 Cr ≈ 4 Seedance-2.0-Videos (≈ 25 Cr). Drittquelle: Kling 3.0 720p 5 s = 7 Cr, Seedance 2.0 720p 5 s = 22 Cr (1080p 45 Cr), Veo 3.1 4 s = 29 Cr, NB Pro = 2 Cr | MCP; scopeful.org | 2026-09-26 / 07.08.2026 | VERIFIED (Anbieter-Äquivalente) / THIRD-PARTY ESTIMATE |
| Preisdiskrepanzen | Higgsfield nennt für denselben Clip zwei Werte, die ~56 % auseinanderliegen; Unlimited-Modus: Wartezeiten 2–5 h berichtet | https://creatify.ai/blog/higgsfield-vs-kling-ai-quality-cost-per-second-and-which-to-use-for-ads-in-2026 | 26.09.2026 | THIRD-PARTY ESTIMATE |
| **Unlimited ≠ Automatisierung** | „Unlimited models and Free Generations are accessible only via higgsfield.ai and are **not accessible on MCP/CLI**" → für Claude-Code-Pipelines zählen nur Credits | MCP Compliance-Note | 2026-09-26 | VERIFIED |
| Modellkatalog (Video) | Kling 2.6/3.0/3.0 Turbo/3.0 Omni Edit; Seedance 1.5 Pro/2.0/2.0 Mini/2.5; Veo 3/3.1/3.1 Lite; Gemini Omni Flash/1.1; Wan 2.6/2.7/3.0/3.0 Prime; Hailuo 2.3, MiniMax H3/H3 Max; FLUX 3 Video; Grok Video 1.5; Cinema Studio 3.0; Topaz/ByteDance-Upscaler; Video-Background-Remover; Sync Lipsync 3 | MCP `models_explore` | 2026-09-26 | VERIFIED |
| **Marketing Studio** („Product-to-Video") | „One-click product ads, TikTok/Reels ready"; 12–15 s, 480p–1080p, Audio; Parameter `product_ids`, Avatar, Hook- & Setting-Bausteine (UGC, Tutorial, Unboxing, Product Review, Virtual Try-On) oder `ad_reference_id` (Szenario eines Referenz-Ads nachbauen) | MCP `models_explore` | 2026-09-26 | VERIFIED (Funktion) / CLAIMED (Qualität) |
| Genjutsu / Ad Multiplier | Objekt in bestehendem Video per Referenzbild ersetzen (`hf_mult_replace_object`); Ad Multiplier = Varianten eines Clips (Seedance 2.5) | MCP | 2026-09-26 | VERIFIED (Funktion) / CLAIMED (Qualität) |
| Soul | Bildmodell (Soul V2 / Soul Cinema) – aktuell Gratis-Generierungen als Kaufanreiz (nur Web) | MCP | 2026-09-26 | VERIFIED |
| Posting | MCP bietet TikTok-Connect/Publish-Tools | MCP-Toolliste | 2026-09-26 | VERIFIED (vorhanden), Funktionsumfang UNKNOWN |
| Kommerzielle Rechte | Free-Tier ohne kommerzielle Nutzung; bezahlte Pläne kommerziell | scopeful.org | 07.08.2026 | THIRD-PARTY ESTIMATE |

**Einordnung:** Higgsfield ist für die explorative Kreativphase sehr effizient (ein Credit-Pool für ~20 Modelle, Marketing-Studio-Presets). Für eine Claude-Code-Pipeline ist die Credit-Ökonomie (Kling 3.0 ≈ 5–7 Cr ≈ €0.17–0.34 pro 5-s-720p-Clip bei Ultra) günstiger als fal-Listenpreise, aber: keine Unlimited-Nutzung via MCP/CLI, Preisangaben teils widersprüchlich, Credits verfallen.

### 1.3 Kommerzielle Nutzungsrechte (Video) – Kurzmatrix

| Anbieter | Kommerziell? | Datenqualität |
|---|---|---|
| Google Veo/Gemini API | Output nutzbar; SynthID-Wasserzeichen immer | VERIFIED (Wasserzeichen) / UNKNOWN\* (ToS-Details) |
| Kling | nur bezahlte Pläne | THIRD-PARTY ESTIMATE |
| Pika | ab Creator ($35) | VERIFIED |
| Luma | ab Plus ($29.99) | THIRD-PARTY ESTIMATE |
| Higgsfield | bezahlte Pläne | THIRD-PARTY ESTIMATE |
| Wan 2.2 | Apache 2.0 | VERIFIED |
| LTX-2.5 | frei < $10 Mio. Umsatz | VERIFIED |
| Midjourney | bezahlte Pläne (>$1 Mio. Umsatz: Pro/Mega) | UNKNOWN\* |

---

## 2. AI-Bild-Modelle, Staging & Upscaler

### 2.1 Bildgeneratoren / Reference-Editing

| Tool | Fähigkeit (Produkt-Konsistenz / Reference-Editing) | Preis (API) | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **Nano Banana Pro** (Gemini 3 Pro Image) | bis **6 Objekt-Referenzbilder „high-fidelity"**, 5 Charakter-, 3 Stil-Referenzen; 1K–4K; „advanced text rendering"; SynthID | **$0.134** (1K/2K), $0.24 (4K); Batch $0.067/$0.12 | https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/docs/image-generation | 2026-09-26 | VERIFIED (Preis) / CLAIMED (Treue) |
| **Nano Banana 2** (Gemini 3.1 Flash Image) | bis **10 Objekt-Referenzen**, 4 Charakter-, 3 Stil-Ref.; 0.5K–4K | $0.045 (0.5K), **$0.067 (1K)**, $0.101 (2K), $0.151 (4K); Batch halbiert | wie oben | 2026-09-26 | VERIFIED |
| Nano Banana 2 Lite | – | $0.0336 (1K), Batch $0.0168 | wie oben | 2026-09-26 | VERIFIED |
| Nano Banana (2.5 Flash Image) | deprecated | $0.039 | wie oben | 2026-09-26 | VERIFIED |
| **GPT Image 2 / 2.5** (OpenAI) | Bild-Editing mit Referenzbildern | Token-basiert: Output $30/1M Token (gpt-image-2/2.5), Batch $15; ≈ **$0.005 (low) / $0.041 (medium) / $0.165 (high)** pro 1024×1536 | https://developers.openai.com/api/docs/pricing ; https://www.aifreeapi.com/en/posts/openai-image-generation-api-pricing | 2026-09-26 / 06.09.2026 | VERIFIED (Tokenpreise) / THIRD-PARTY ESTIMATE (Bildpreise) |
| **FLUX.2** (BFL) | Pro/Flex/Max mit Multi-Referenz-Editing | Klein 4B ab **$0.014/MP**, Klein 9B $0.015, **Pro ab $0.03/MP** (Edit $0.045), Flex $0.05, Max $0.07 | https://docs.bfl.ml/quick_start/pricing | 2026-09-26 | VERIFIED |
| **FLUX.1 Kontext** | Kontext-Editing (Objekt in Szene) | **Pro $0.04**, Max $0.08 pro Bild | wie oben | 2026-09-26 | VERIFIED |
| **Seedream 5.0 Pro** (ByteDance) | Multi-Referenz, Layer-Dekomposition | BytePlus: **$0.045** (≤ 2,36 MP), $0.09 darüber; 1. Referenz gratis, weitere $0.003 | https://www.byteplus.com/en/product/Seedream (via Suche) | 2026 | THIRD-PARTY ESTIMATE |
| Seedream V4 (fal) | – | $0.03 | https://fal.ai/pricing | 2026-09-26 | VERIFIED |
| **Midjourney V7/V8** | ästhetisch stark, schwache Produkt-Treue, kein API | s. 1.1 | – | – | UNKNOWN\* |
| **Ideogram** | Typografie-stark | Plus $15/20, Pro $42/60 (jährl./monatl.); API-Preise dynamisch geladen; Replicate: Ideogram v3 Quality $0.09 | https://ideogram.ai/pricing/?pricing_tab=api ; https://replicate.com/pricing | 2026-09-26 | VERIFIED (Abo) / VERIFIED (Replicate) |
| **Recraft V4 / V4.1** | Raster & Vektor, Brand-Styles | V4 $0.04, V4.1 $0.035, V4.1 Flash $0.007, V4.1 Pro $0.21; Vektor $0.08–0.30; Free-Plan-Bilder gehören Recraft, nicht kommerziell | https://www.recraft.ai/docs/api-reference/pricing ; https://www.recraft.ai/pricing | 2026-09-26 | VERIFIED |
| **Krea** | Aggregator (Bild/Video) | UNKNOWN (Seite nicht parsebar) | https://www.krea.ai/pricing | 2026-09-26 | UNKNOWN |
| Magnific (jetzt magnific.com) | Aggregator + Upscaler; API auf allen bezahlten Plänen | Premium $20 (Aktion $7.25 jährl.), Premium+ $45, Pro Starter $110/Monat; z. B. Kling 2.5 720p 140 Cr/5 s | https://www.magnific.com/pricing | 2026-09-26 | VERIFIED |

### 2.2 Virtuelles Staging (Interior-Nische)

| Tool | Fähigkeit | Preis | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **ReimagineHome** | Virtual Staging; ab Pro „Real Products Discovery & Visualization" (echte Produkte im Raum), Referenzfoto-Steuerung, Batch | Essential $14/Monat (30 Cr); Pro ~$50 (200 Cr), Advanced ~$75, Agency ~$99 (Preise auf Seite als geschätzt ausgegeben); 1 Cr/Design, 2 Cr mit echten Produkten | https://www.reimaginehome.ai/pricing | 2026-09-26 | VERIFIED (Essential) / THIRD-PARTY ESTIMATE (übrige) |
| **Interior AI** | Redesign, Virtual Staging (ab Premium), Walkthrough-Video, VR; kein API dokumentiert | Pro $49 (1.000 Renders), Premium $99 (5.000), Ultra $199 (25.000)/Monat; jährlich ab $29/Monat | https://interiorai.com/ | 2026-09-26 | VERIFIED |
| RoomGPT | Raum-Redesign | UNKNOWN | – | – | UNKNOWN |

### 2.3 Upscaler

| Tool | Preis | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|
| **Topaz Studio** (Video, Photo, Gigapixel) | Personal $399/Jahr bzw. $69/Monat (kommerziell nur für Orgs < $1 Mio. Umsatz); Pro $799/Jahr bzw. $79/Monat (jährl.); Einzel-App Topaz Video $59 (Personal)/$74 (Pro) pro Monat | https://www.topazlabs.com/pricing | 2026-09-26 | VERIFIED |
| Topaz / ByteDance Video-Upscale über Higgsfield | per Credits | Higgsfield MCP | 2026-09-26 | VERIFIED (verfügbar) |
| **Magnific** | s. 2.1 | https://www.magnific.com/pricing | 2026-09-26 | VERIFIED |
| Runway Upscaling | Bild 25–150 Cr; Video $0.007–0.012 pro Output-Frame | https://docs.dev.runwayml.com/guides/pricing/ | 2026-09-26 | VERIFIED |
| BFL Video-Upscale | $0.07–0.10 pro Megapixel-Sekunde | https://docs.bfl.ml/quick_start/pricing | 2026-09-26 | VERIFIED |

---

## 3. AI-Voice / Audio / Musik

| Tool | Fähigkeit | Preis | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **ElevenLabs (API/Abo)** | v3: 70+ Sprachen, v2 Multilingual: 29 Sprachen (Deutsch nach Vorwissen enthalten) | Starter $6 (60k Zeichen), **Creator $22** (220k; 1. Monat $11), Pro $99 (990k), Scale $299, Business $990; Overage v3/v2 **$0.10/1k Zeichen**, Flash/Turbo $0.05/1k | https://elevenlabs.io/pricing/api | 2026-09-26 | VERIFIED (Preise) / UNKNOWN\* (DE explizit, TTS-Kommerzrechte ab Starter) |
| **OpenAI TTS** | tts-1, tts-1-hd, gpt-4o-mini-tts | tts-1 **$15/1M Zeichen**, tts-1-hd $30/1M; gpt-4o-mini-tts $0.60/1M Text-In + $12/1M Audio-Out-Token | https://developers.openai.com/api/docs/pricing | 2026-09-26 | VERIFIED |
| **Gemini TTS** (3.8 Flash / Flash-Lite) | – | ≈ **$0.0015–0.0045 pro 10 s** Audio (Preise verdoppeln sich ab 01.01.2027) | https://ai.google.dev/gemini-api/docs/pricing | 2026-09-26 | VERIFIED |
| **Suno** | Musikgenerator | Free: keine Downloads, **keine kommerziellen Rechte**; Pro $8 ($6.40 jährl.), 2.500 Cr, **nur 20 Song-Downloads/Monat**, kommerziell; Premier $24 ($19.20), 10.000 Cr, **60 Downloads/Monat**, kommerziell | https://suno.com/pricing | 2026-09-26 | VERIFIED |
| **Udio** | – | Seite nicht auslesbar | https://www.udio.com/pricing | 2026-09-26 | UNKNOWN |
| **Instagram-Musikbibliothek** | „To make sure that the music in our licensed library is not used for commercial purposes, **certain business accounts** and certain types of posts do not have access to the library." Alternative: **Meta Sound Collection** (> 14.000 lizenzfreie Tracks, kommerziell nutzbar) | kostenlos | https://www.facebook.com/help/instagram/402084904469945 | 2026-09-26 | VERIFIED |
| Musik via Graph API | Content-Publishing-API kennt nur `audio_name` (Umbenennen der eingebetteten Tonspur); **keine Auswahl lizenzierter IG-Musik per API** dokumentiert → Musik muss im gerenderten Video stecken (lizenzfrei/eigen) | – | https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media | 2026-09-26 | VERIFIED |

**Konsequenz:** Für eine automatisierte Pipeline gilt: Musik = lizenzfrei (Meta Sound Collection, Suno Paid, Stock-Library) direkt ins Video rendern. Trending-Sounds aus der IG-Bibliothek sind per API nicht setzbar und für Business-Accounts ohnehin eingeschränkt → Creator-Account-Typ prüfen (Compliance/Plattform-Agent). Affiliate-Posts sind kommerziell – auch bei Creator-Accounts ist die Nutzung lizenzierter Musik für Werbezwecke riskant (UNKNOWN\*, rechtlich prüfen).

---

## 4. Editing / Captions / Rendering-Automation

| Tool | Fähigkeit / API | Preis | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **Remotion** (React → Video) | Programmatisches Rendering, ideal für Claude Code (Templates, Captions, Overlays, Ken-Burns auf echten Produktfotos) | **Frei für Einzelpersonen/Firmen bis 3 Personen** (kommerziell); ab 4 Personen: Creator $25/Seat/Monat oder Automator $0.01/Render (min. $100/Monat); Enterprise ab $500 | https://www.remotion.pro/license | 2026-09-26 | VERIFIED |
| **FFmpeg** | Schneiden, Concat, Audio-Mix, Untertitel-Burn-in | kostenlos (Open Source) | – | – | VERIFIED (allg. bekannt) |
| **Creatomate** | Template-API + No-Code; 1 Bild = 1 Credit, 1 min 720p ≈ 14 Credits | Essential 2.000 Cr, Growth 10–40k, Beyond 50–200k/Monat; €/$-Preise nicht angezeigt | https://creatomate.com/pricing | 2026-09-26 | VERIFIED (Credits) / UNKNOWN (Preise) |
| **Shotstack** | Render-API (JSON), bis 1080p (4K nur High Volume) | PAYG **$0.30/min**; Abo **$0.20/min**, ab **$39/Monat** | https://shotstack.io/pricing/ | 2026-09-26 | VERIFIED |
| **JSON2Video** | JSON-API inkl. TTS | Hobby $16.95 (50 min, max. 1 min/Video), Professional $49.95 (200 min), Startup $99.95 (500 min); 4K = 4× | https://json2video.com/pricing/ | 2026-09-26 | VERIFIED |
| **Submagic** | Auto-Captions/B-Roll; API | Starter $19, Pro $39, Business $69/Monat (jährl. $12/$23/$41); API inkl. 10 min (Starter/Pro) bzw. 100 min (Business); API-Packs $0.10–0.23/min | https://www.submagic.co/pricing | 2026-09-26 | VERIFIED |
| **Captions (captions.ai)** | Captions, Avatare, B-Roll; **kein API auf Preisseite** | Max $24.99 (500 Cr), Frontier $69.99–279.99 | https://www.captions.ai/pricing | 2026-09-26 | VERIFIED |
| **Opus Clip** | Long→Short-Clipping (für diese Pipeline wenig relevant); Editing-/Scheduler-API + MCP ab Pro | Starter $15, Pro $29/Monat | https://www.opus.pro/pricing | 2026-09-26 | VERIFIED |
| **Descript** | Text-basiertes Editing, Underlord | Hobbyist $16 (jährl.)/$24 (monatl.), Creator $24/$35, Business $50/$65; kein öffentliches Render-API auf Preisseite | https://www.descript.com/pricing | 2026-09-26 | VERIFIED (Werte; Zuordnung jährlich/monatlich aus Seitentext abgeleitet) |
| **CapCut** | Beliebter Editor; **kein öffentliches Editing-API**; Nutzung von Templates/Musik nur für als „kommerziell" markierte Assets | Preisseite 404/500 | capcut.com | 2026-09-26 | UNKNOWN |

**Empfehlung für maximale Automatisierung:** Remotion (lokal, $0 bei ≤ 3 Personen) + FFmpeg + Whisper-/Gemini-basierte Captions → komplett in Claude Code steuerbar, keine Render-Gebühren. Shotstack/Creatomate nur, wenn Cloud-Rendering ohne eigene Infrastruktur gewünscht (≈ $20–40/Monat bei 60–120 Reels à 0,5 min × 2 Renders).

---

## 5. Posting-Automation

### 5.1 Plattform-APIs

| Plattform / API | Reels/Shorts-Support & Limits | Account-Voraussetzung | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **Instagram Graph API – Content Publishing** | Bilder (nur JPEG), Videos, **Reels**, Stories, Karussells (≤ 10); **„100 API-published posts within a 24-hour moving period"**; **Trial Reels** (`trial_params`, Graduation `MANUAL` oder `SS_PERFORMANCE`); `share_to_feed`; bis 3 Collaborators; `is_paid_partnership` / `branded_content_sponsor_ids`; Produkt-Tags (≤ 5, Shop nötig); keine Filter | Professional Account (Business **oder** Creator); via „Instagram Login" **ohne** FB-Page oder via „Facebook Login for Business" mit verknüpfter Page | https://developers.facebook.com/docs/instagram-platform/content-publishing/ ; https://developers.facebook.com/docs/instagram-platform/overview | 2026-09-26 | VERIFIED |
| Reel-Specs (API) | MP4/MOV, H.264/HEVC, 23–60 fps, **3 s – 15 min**, **max. 300 MB**, empfohlen 9:16, max. 1920 px Breite, ≤ 25 Mbps, AAC ≤ 48 kHz | – | https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media | 2026-09-26 | VERIFIED |
| KI-Label via IG-API | Kein Parameter für „AI info"-Label in der Publishing-Doku gefunden | – | wie oben | 2026-09-26 | UNKNOWN (Datenlücke) |
| **TikTok Content Posting API – Direct Post** | **„All content posted by unaudited clients will be restricted to private viewing mode"**; Audit nötig; Cap **„typically around 15 posts per day / creator account"**; 6 Requests/min pro Token; Pflicht-UX: Vorschau, manuelle Privacy-Auswahl ohne Default, Einwilligungs-Hinweis; Felder `is_aigc` (KI-Label), `brand_content_toggle`, `brand_organic_toggle`; Richtlinie: Apps dürfen nicht „limited to internal groups/private use" sein, kein Wasserzeichen/Promo-Overlay durch die App | TikTok-Account (Business/Creator) + auditierte App | https://developers.tiktok.com/doc/content-posting-api-get-started ; https://developers.tiktok.com/doc/content-posting-api-reference-direct-post ; https://developers.tiktok.com/doc/content-sharing-guidelines | 2026-09-26 | VERIFIED |
| TikTok – Upload to Inbox (Drafts) | Nutzer muss im App-Posteingang manuell fertig posten; **max. 5 pending shares / 24 h** | – | https://developers.tiktok.com/doc/content-posting-api-reference-upload-video | 2026-09-26 | VERIFIED |
| **YouTube Data API v3** | `videos.insert`: **100 Aufrufe/Tag** Default, Kosten **1 Einheit im Upload-Bucket** (neues Quota-Modell; zusätzlich 100 `search.list` + 10.000 Units für Rest); max. 256 GB; **Uploads unverifizierter API-Projekte (nach 28.07.2020 erstellt) sind privat bis zum Audit** | Google-Projekt + OAuth; Audit für öffentliche Uploads | https://developers.google.com/youtube/v3/determine_quota_cost ; https://developers.google.com/youtube/v3/docs/videos/insert | 2026-09-26 | VERIFIED |
| **Pinterest API v5** | Video-Pins: 1) `/media` registrieren, 2) Upload in S3, 3) Status prüfen, 4) `pins/create` mit `source_type: video_id` + `cover_image_url`; Scopes `pins:write` etc. | Business-Account; Trial- vs. Standard-Access-Einschränkungen nicht dokumentiert gefunden | https://developers.pinterest.com/docs/work-with-organic-content-and-users/create-boards-and-pins/ | 2026-09-26 | VERIFIED (Flow) / UNKNOWN (Access-Tier-Limits) |

### 5.2 Scheduling-Tools

| Tool | Plattformen | Preis | API | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|---|
| **Metricool** | IG, FB, TikTok, YouTube, Pinterest, Threads, Bluesky, GBP, LinkedIn (Starter+), X (Add-on) | Free (1 Brand, 20 Posts/Monat); **Starter ab €16–29/Monat** (5–10 Brands, unbegrenzt*); Advanced ab €43–130 | **API (Zapier/Make/MCP) ab Advanced** | https://metricool.com/pricing/ | 2026-09-26 | VERIFIED |
| **Buffer** | IG, FB, TikTok, LinkedIn, X, YouTube, Threads, Pinterest, GBP, Bluesky, Mastodon, Substack | Free (3 Kanäle, 10 geplante Posts/Kanal); **Essentials $5/Kanal/Monat**; Team $10/Kanal (Fair Use 5.000 Posts/Kanal) | **API: Free 3.000, Essentials 7.500, Team 15.000 Requests/Monat** | https://buffer.com/pricing | 2026-09-26 | VERIFIED |
| **Later** | IG, FB, TikTok, Threads, YouTube, Pinterest, LinkedIn, Snapchat | Starter $18.75 (30 Posts/Profil), Growth $37.50 (180), Scale $82.50 (unbegrenzt) – jährl. Abrechnung; Link-in-Bio inkl. | nicht erwähnt | https://later.com/pricing/ | 2026-09-26 | VERIFIED |
| **Publer** | Multi-Plattform, Bulk-Scheduling | Seite JS-gerendert | API (Business-Plan) | https://publer.com/pricing | 2026-09-26 | UNKNOWN |
| **Hootsuite** | Multi-Plattform | Standard $99, Professional $199, Advanced $399/User/Monat | nicht angegeben | https://www.hootsuite.com/plans | 2026-09-26 | VERIFIED (überdimensioniert) |
| **Blotato** | 9 Plattformen, Cross-Posting, AI-Bild/Video/Voice | Starter $29 (1.250 AI-Cr, 20 Accounts), Creator $97, Agency $499 | **Social-Media-API + offizielle n8n-/Make-Nodes** | https://www.blotato.com/pricing | 2026-09-26 | VERIFIED |
| **Repurpose.io** | IG, TikTok, YouTube, FB, Pinterest, Snapchat, X, LinkedIn … | Starter $35 (3 Accounts/Netzwerk, 5.000 Videos), Pro $79, Agency $179/Monat | – | https://repurpose.io/pricing/ | 2026-09-26 | VERIFIED |

**Empfehlung Posting:** IG, YouTube, Pinterest direkt per API aus Claude-Code-Skripten (kostenlos; IG-Limit 100/24 h ist bei 2–4 Reels/Tag irrelevant). TikTok über auditierten Drittanbieter (Buffer Essentials $5/Kanal oder Metricool) – eine eigene Privat-App wird die TikTok-Audit-Richtlinie („not limited to private use") voraussichtlich nicht bestehen. YouTube-API-Projekt früh auditieren lassen (sonst private Uploads).

---

## 6. Analytics- & Affiliate-Reporting-APIs

### 6.1 Plattform-Analytics

| API | Verfügbare Metriken (Auszug) | Einschränkungen | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **Instagram Media Insights (Reels)** | `views`, `reach`, `saved`, `shares`, `reposts`, `likes`, `comments`, `total_interactions`, `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time`, `reels_skip_rate` (Skip-Rate erste 3 s, „in development"), `crossposted_views`, `facebook_views`, `profile_visits`, `profile_activity`, `follows` | `impressions` für Medien nach 02.07.2024 deprecated; **kein Link-Klick-Metric pro Reel** (Reels haben keine klickbaren Links → Klicks nur über Bio/DM-Tools/Shortlinks messbar) | https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights | 2026-09-26 | VERIFIED |
| **TikTok Display API** | Video-Objekt: `view_count`, `like_count`, `comment_count`, `share_count`, `duration`, `is_aigc` u. a. | **keine** Watch-Time/Retention; Research API nur für nicht-kommerzielle akademische/Non-Profit-Forschung (US/EWR/UK/CH/CA) → für uns **nicht** nutzbar | https://developers.tiktok.com/doc/tiktok-api-v2-video-object ; https://developers.tiktok.com/products/research-api/ | 2026-09-26 | VERIFIED |
| **YouTube Analytics API** | `views`, `engagedViews`, `averageViewDuration`, `averageViewPercentage`, `subscribersGained`, `shares`, `likes`, `comments` | Hinweis: YouTube ändert die View-Zählung für alle Formate (Revision 27.08.2026) | https://developers.google.com/youtube/analytics/metrics | 2026-09-26 | VERIFIED |
| **Pinterest Analytics (API v5)** | `IMPRESSION`, `OUTBOUND_CLICK`, `OUTBOUND_CLICK_RATE`, `SAVE`, `PIN_CLICK`, `VIDEO_MRC_VIEW`, `VIDEO_AVG_WATCH_TIME`, `VIDEO_V50_WATCH_TIME`, `QUARTILE_95_PERCENT_VIEW`, Profile Visits, Follows | max. **90 Tage** zurück, max. 90-Tage-Zeitraum | https://github.com/pinterest/api-description (openapi.yaml v5) | 2026-09-26 | VERIFIED |

### 6.2 Affiliate-Netzwerke & Produktdaten

| API | Fähigkeit | Zugang / Limits | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **Amazon PA-API 5.0** | **Deprecated**, ersetzt durch Creators API; Alt-Aufrufe erhalten **HTTP 403 AccessDeniedException** | – | https://affiliate-program.amazon.com/creatorsapi/docs/en-us/paapiv5-deprecation | 2026-09-26 | VERIFIED |
| **Amazon Creators API** | `SearchItems`, `GetItems`, `GetVariations`, `GetBrowseNodes` (Katalogdaten); Marktplätze u. a. **DE** | **„at least 10 qualifying sales within the past 30 days"**; Registrierung in Associates Central; **kein Reporting-/Earnings-Endpunkt** dokumentiert | https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction | 2026-09-26 | VERIFIED |
| Amazon Associates Reporting | Kein offizielles Reporting-API → Berichte in Associates Central (Download/CSV). Scraping = ToS-Risiko | – | wie oben (Abwesenheit) | 2026-09-26 | VERIFIED (kein API dokumentiert) |
| **Awin Publisher APIs** | Link Builder API (Deeplinks in Bulk), Offers API, Advertiser Performance API (Clicks, Sales); Bearer-Token | **20 Calls/min pro User** | https://help.awin.com/developers/apidocs/introduction | 2026-09-26 | VERIFIED |
| **impact.com Partner API v16** | REST: Actions, Clicks, Reports, Catalogs/ItemSearch (Produktsuche), Tracking-Links; **Partner-MCP-Server** (`query_performance` u. a.) | Hourly: Performance-Detail 500, Aggregate 250, **Product Search 3.000**, Other 1.000; ReportExport 100/Tag | https://integrations.impact.com/partner-api-reference/readme/rate-limits.md ; https://integrations.impact.com/ai-solutions/mcp-tools/partner-mcp-tools.md | 2026-09-26 | VERIFIED |
| **CJ (Commission Junction)** | Commission Detail API (GraphQL), Product-Feed/Search-API, Link Search; Personal Access Token | Portal-Seite ohne Details abrufbar | https://developers.cj.com/ | 2026-09-26 | UNKNOWN\* |
| **Rakuten Advertising** | Reporting-/Events-API, Produkt-API | nicht geprüft | – | – | UNKNOWN\* |

**Kritischer Befund Amazon:** Die automatische Produktdaten-Pipeline über Amazon ist erst nach **≥ 10 qualifizierten Verkäufen in 30 Tagen** möglich – in der Startphase also Produktauswahl manuell/SiteStripe bzw. über Awin/impact-Feeds (sofort per API verfügbar). Umsätze/Clicks von Amazon lassen sich nicht per API ziehen.

---

## 7. Link-/DM-Tools & Landingpage

| Tool | Fähigkeit | Preis | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|---|
| **ManyChat** | IG Comment-to-DM, Keywords, Follow-Gate, Flows, AI | Free (Vorwissen: bis 1.000 Kontakte), Pro ab ~ $15/Monat (kontaktabhängig), AI-Add-on ~ $29 | https://manychat.com/pricing (403) | 2026-09-26 | UNKNOWN\* |
| **LinkDM** | Post/Reels-Automation, Story-Auto-Reply; Comment-Auto-Reply ab Pro | Free 1.000 DMs/Monat; **Pro $19** (25.000 DMs, 3 Accounts); Platinum+ $99 (300.000) | https://linkdm.com/pricing | 2026-09-26 | VERIFIED |
| **CreatorFlow** | Comment-to-DM, Story-Replies, Link-Tracking, Geo-Analytics | Free 500 DMs; **Pro $15** ($12 jährl., 5.000 DMs); Growth $30 (10.000) | https://creatorflow.so/pricing | 2026-09-26 | VERIFIED |
| **Inrō** | Comment-to-DM, Story-Mentions/Replies, CRM | Free (100 aktive Kontakte, 3 Automationen); **Pro €12,99/Monat** | https://www.inro.social/pricing | 2026-09-26 | VERIFIED |
| **Linktree** | Link-in-Bio, Analytics, Monetarisierung | Free; Starter $6 (jährl.)/$8 (monatl.); **Pro $12/$15**; Premium $30/$35 | https://linktr.ee/s/pricing | 2026-09-26 | VERIFIED |
| Later Link-in-Bio | in Later-Plänen enthalten (Affiliate-Links via Mavely) | ab $18.75 | https://later.com/pricing/ | 2026-09-26 | VERIFIED |
| Metricool SmartLinks | Link-in-Bio ab Starter | ab €16 | https://metricool.com/pricing/ | 2026-09-26 | VERIFIED |
| Beacons / Stan / Koji | – | Seiten blockiert/404 | – | 2026-09-26 | UNKNOWN |
| **Geniuslink** | Amazon-Lokalisierung (Käufer → lokaler Store), Mobile Deep Links in Amazon-App, Choice Pages, Link-Monitoring | **$6/Monat inkl. 1.000 Klicks, +$3.50/1.000 Klicks**; Custom Domain $50/Monat; 14 Tage Trial | https://geniuslink.com/pricing | 2026-09-26 | VERIFIED |
| Amazon OneLink | Kostenlose Weiterleitung internationaler Besucher zu verknüpften Amazon-Stores | kostenlos | – | – | UNKNOWN\* |
| **Eigene Landingpage (Next.js + Vercel)** | Volle Kontrolle, eigene Klick-Messung, Link-Hub pro Reel | Vercel Hobby = „**personal, non-commercial use**" → für Affiliate **Pro $20/Monat**; Alternative statisch (Cloudflare Pages o. ä., UNKNOWN\*: kostenlos) + Domain ~€1/Monat | https://vercel.com/pricing | 2026-09-26 | VERIFIED (Vercel) / MODEL ASSUMPTION (Domain) |

**Empfehlung:** Comment-to-DM ist für IG-Affiliate der wichtigste Klickkanal (Reels ohne klickbare Links). Günstigster verifizierter Weg: CreatorFlow Pro $15 oder Inrō Pro €12,99; DM-Links zeigen auf eigene Landingpage (Next.js, statisch, UTM/Shortlink je Reel) → dort Geniuslink/Amazon-Links. So entsteht eine Klick-Attribution pro Reel, die Amazon selbst nicht per API liefert.

---

## 8. Evidenz zur Performance von AI-Content & Plattform-Maßnahmen

### 8.1 Studien / Daten

| Befund | Zahl | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|
| Anteil KI-Videos im YouTube-Shorts-Feed neuer Nutzer | **21 %** der ersten 500 Shorts KI-generiert, 33 % „Brainrot" | https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/ | 28.11.2025 (Daten Okt. 2025) | THIRD-PARTY ESTIMATE (Kapwing-Studie, Methode: Neu-Account-Simulation) |
| Top-KI-Slop-Kanäle | z. B. „Bandar Apna Dost" 2,07 Mrd. Views, geschätzt $4,25 Mio./Jahr | wie oben | 28.11.2025 | THIRD-PARTY ESTIMATE |
| Wachstum KI-Kanäle | „nearly one in 10 of the fastest growing YouTube channels globally are showing AI-generated content only" (Guardian-Analyse, Juli 2025) | zitiert bei Kapwing | 2025 | THIRD-PARTY ESTIMATE |
| **KI-Interior/Architektur-Shorts (Beispiele, YouTube)** | **Dreamy Interior**: 313k Abos, 154 Mio. Views, 88 Uploads (seit 03/2026), Top-Short 32 Mio.; **Kou Yang** (@KouYangAI): 72k Abos, 154 Mio. Views, 278 Uploads, Top 30 Mio.; **Bau Rausch** (deutschsprachig, „[KI-Konzept]"-Kennzeichnung): 620k Abos, 386 Mio. Views, 53 Uploads seit 04/2026, Top 127 Mio.; **Isla \| Interior Designer**: 51k Abos, 64 Mio. Views (App-Promotion für „RenoMuse") | NexLev-Datenbank via MCP (`search_shorts_niche_finder_channels`, isAiChannel=true) | abgerufen 2026-09-26 | THIRD-PARTY ESTIMATE |
| **KI-Produkt/Gadget-Shorts** | **US Shop** (@usshopnow): 1,7k Abos aber 642 Mio. Views, 61 Uploads, Outlier 40,5 (KI-Produktvideos mit Sale-Hooks); **Adam Life Hacks**: 137k Abos, 118 Mio. Views; **Smart Life 79**: 77k Abos, 92 Mio. Views | NexLev | 2026-09-26 | THIRD-PARTY ESTIMATE |
| Monetarisierung solcher Kanäle | Geschätzte **AdSense**-Gesamterlöse trotz 100+ Mio. Views nur ~$2k–74k je Kanal → Shorts-RPM niedrig; Erlös muss aus Affiliate/Produkten kommen | NexLev (Revenue-Schätzung) | 2026-09-26 | THIRD-PARTY ESTIMATE |
| Instagram-spezifische Reichweitendaten KI vs. real | **keine belastbare öffentliche Studie gefunden** | – | – | UNKNOWN (Datenlücke) |
| Konsumenten-Vertrauen („AI slop"-Backlash, Kaufabsicht) | Umfragen (z. B. Raptive 2025, NielsenIQ 2024) nach Vorwissen negativ für erkennbar KI-generierten Content; am Prüfdatum nicht verifiziert | – | – | UNKNOWN\* |

**Interpretation:** KI-Theme-Content erzielt nachweislich Massenreichweite (v. a. „Transformation/Before-After", „Dream Room", „Konzept-Bauten"), aber die Top-Beispiele sind **Spektakel-Content**, nicht Produkt-Showcases mit exakter Produkttreue. Für Affiliate ist die Übertragbarkeit von Views auf Klicks/Käufe unbelegt (Datenlücke).

### 8.2 Plattform-Maßnahmen gegen KI-Masse

| Plattform | Maßnahme | Quelle-URL | Datum | Datenqualität |
|---|---|---|---|---|
| **YouTube** | YPP-Policy „repetitious" → **„inauthentic content"** ab **15.07.2025**: untersagt u. a. „AI-generated content made with generic or unoriginal templates giving the impression of mass production" | https://support.google.com/youtube/answer/1311392 | 2026-09-26 | VERIFIED |
| YouTube CEO-Brief | „The rise of AI has raised concerns about low-quality content, aka 'AI slop'" – Ausbau der Spam-/Clickbait-Systeme gegen repetitiven KI-Content; Offenlegungspflicht für realistisch veränderte Inhalte | https://blog.youtube/inside-youtube/the-future-of-youtube-2026/ | 21.01.2026 | VERIFIED |
| **Meta (IG/FB)** | „AI info"-Labels bei erkannten Industrie-Signalen (C2PA/IPTC) oder Selbstauskunft; Selbstauskunft v. a. bei fotorealistischem Video/Audio | https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/ | 2024 (abgerufen 2026-09-26) | VERIFIED |
| Instagram-Ranking | Bevorzugung von Originalcontent ggü. Aggregatoren (2024) | – | – | UNKNOWN\* |
| **TikTok** | API-Feld `is_aigc` erzeugt Label „Creator labeled as AI-generated"; zusätzlich (Vorwissen, Nov. 2025) Nutzer-Regler für weniger KI-Content in „Manage Topics" + unsichtbares Wasserzeichen | https://developers.tiktok.com/doc/content-posting-api-reference-direct-post | 2026-09-26 | VERIFIED (`is_aigc`) / UNKNOWN\* (Regler) |
| **Pinterest** | „Gen AI"-Label via IPTC-Metadaten **und eigene Klassifikatoren** (auch ohne Marker); Appeal möglich; (Vorwissen, Okt. 2025) Option „weniger KI-Pins" in Kategorien wie Beauty, Kunst, Mode, Home Decor | https://help.pinterest.com/en/article/gen-ai-labels | 2026-09-26 | VERIFIED (Labels) / UNKNOWN\* („see fewer AI") |

**Relevanz:** Google-Modelle setzen SynthID, viele Tools schreiben C2PA-Metadaten → KI-Labels werden auf Meta/Pinterest teils automatisch vergeben. Gerade **Home Decor/Interior** ist auf Pinterest eine Kategorie mit Nutzerregler gegen KI-Pins (UNKNOWN\*, verifizieren). Massenproduktion nach Template ist auf YouTube explizit demonetarisierungsrelevant.

---

## 9. Kostenmodell (MODEL ASSUMPTION)

### 9.1 Annahmen (Format: 15–30-s-Reel)

| Parameter | Low | **Mid (Basisfall)** | High | Begründung |
|---|---|---|---|---|
| AI-Clips pro Reel | 3 | **4** | 6 | Vorgabe 3–6 |
| Clip-Länge (generiert) | 5 s | **6 s** | 8 s | Vorgabe 5–8 s; Veo mit Referenzbildern erzwingt 8 s |
| Versuche pro nutzbarem Clip | 2,0 | **2,5** | 3,0 | Vorgabe 2–3 (Fehlgenerierungen, Produktabweichungen) |
| → generierte Videosekunden/Reel | 30 s | **60 s** | 144 s | Clips × Länge × Versuche |
| AI-Bilder/Reel (inkl. Startframes & Retries) | 6 | **12** | 20 | 2–4 finale Bilder + Startframes je Clip, ×~2–3 Versuche |
| Bildpreis günstig / mittel / premium | $0.045 (Seedream 5 / FLUX Kontext Pro $0.04) | $0.067 (Nano Banana 2, 1K) | $0.134 (Nano Banana Pro) | VERIFIED Preise, s. Abschn. 2 |
| Voiceover | ~375 Zeichen/25 s DE × 2 Takes ≈ 750–1.000 Zeichen/Reel → 120 Reels ≈ 120k Zeichen → **ElevenLabs Creator $22 flat** (220k) deckt 60 & 120 Reels | | | VERIFIED Preis |
| Captions/Rendering | Remotion + FFmpeg lokal: **$0** (≤ 3 Personen) | | | VERIFIED Lizenz |

### 9.2 Generierungskosten pro Reel und Monat (USD, nur Video + Bild)

Rechenweg: Kosten/Reel = generierte Videosekunden × $/s + Bilder × $/Bild; Monat = × 60 bzw. × 120.

| Variante (Video-$/s, Bild-$/Bild) | Szenario | $/Reel | **60 Reels/Monat** | **120 Reels/Monat** |
|---|---|---|---|---|
| **Günstig A:** Veo 3.1 Lite 720p oder Wan 2.5 (fal) $0.05/s; Bild $0.045 | Low / **Mid** / High | 1.77 / **3.54** / 8.10 | 106 / **212** / 486 | 212 / **425** / 972 |
| **Günstig B:** Kling 3.0 Standard (fal, ohne Audio) $0.084/s; Bild $0.045 | Low / **Mid** / High | 2.79 / **5.58** / 13.00 | 167 / **335** / 780 | 335 / **670** / 1.560 |
| **Mittel:** Veo 3.1 Fast 1080p $0.12/s; Bild $0.067 | Low / **Mid** / High | 4.00 / **8.00** / 18.62 | 240 / **480** / 1.117 | 480 / **960** / 2.234 |
| **Premium A:** Kling 3.0 Pro mit Audio $0.168/s; Bild $0.134 | Low / **Mid** / High | 5.84 / **11.69** / 26.87 | 351 / **701** / 1.612 | 701 / **1.403** / 3.225 |
| **Premium B:** Veo 3.1 Standard 1080p $0.40/s; Bild $0.134 | Low / **Mid** / High | 12.80 / **25.61** / 60.28 | 768 / **1.536** / 3.617 | 1.536 / **3.073** / 7.234 |
| ~~Sora 2 / Sora 2 Pro~~ | – | API seit 24.09.2026 abgeschaltet | – | – |

**Abo-Variante Higgsfield (Kling 3.0 im Credit-Pool):** Mid = 10 Video-Generierungen × 5–7 Cr + 12 × Nano Banana Pro à 2 Cr = **74–94 Cr/Reel**.
- 60 Reels ≈ 4.440–5.640 Cr → Ultra €129 (3.000 Cr) + 1.440–2.640 Cr Nachkauf (≈ $80–147 bei 18 Cr/$) → **≈ €129 + $80–147/Monat**.
- 120 Reels ≈ 8.880–11.280 Cr → Ultra €129 + ≈ $327–460 Nachkauf.
- Mit Seedance 2.0 (~22–25 Cr/5-s-Clip) statt Kling ≈ 250–275 Cr/Reel → deutlich teurer (60 Reels ≈ €129 + ~$650–750).
- Quellen: MCP-Preiskonfiguration (VERIFIED), Credit-Kosten teils THIRD-PARTY → Ergebnis MODEL ASSUMPTION.

### 9.3 Fixkosten pro Monat

| Posten | Lean-Stack | Komfort-Stack | Quelle / Qualität |
|---|---|---|---|
| LLM / Coding-Agent | Claude Pro **$20** | Claude Max **$100** + ChatGPT Plus (Codex) ~$20 | VERIFIED (Claude) / UNKNOWN\* (ChatGPT, Seite 403) |
| Voice | ElevenLabs Creator **$22** | $22 | VERIFIED |
| Musik | Meta Sound Collection **$0** | Suno Premier **$24** | VERIFIED |
| Rendering/Captions | Remotion + FFmpeg **$0** | Shotstack **$39** oder Submagic Pro $39 | VERIFIED |
| Scheduler (TikTok + Backup) | Buffer Essentials **$5** (1 Kanal TikTok) | Metricool Advanced ~€43–54 (inkl. API/MCP) | VERIFIED |
| Comment-to-DM | CreatorFlow Pro **$15** / Inrō €12,99 | ManyChat Pro (~$15–30, UNKNOWN\*) | VERIFIED / UNKNOWN\* |
| Geo-Links | Geniuslink **$6 + $3.50/1.000 Klicks** (bei 5.000 Klicks ≈ $20) | ≈ $20–40 | VERIFIED |
| Landingpage | Vercel Pro **$20** (Hobby nicht kommerziell) | $20 | VERIFIED |
| Domain | **~$1** (~$10–15/Jahr) | ~$1 | MODEL ASSUMPTION |
| **Summe Fixkosten** | **≈ $103–110/Monat** | **≈ $300–350/Monat** | MODEL ASSUMPTION |

### 9.4 Gesamt-Monatskosten (Generierung Mid-Szenario + Fixkosten)

| Stack | 60 Reels/Monat | 120 Reels/Monat | Kosten/Reel inkl. Fix (60 / 120) |
|---|---|---|---|
| **Günstig A** (Veo Lite/Wan) + Lean | **≈ $320** (Spanne $210–590) | **≈ $530** (Spanne $320–1.080) | $5.3 / $4.4 |
| **Günstig B** (Kling 3.0 Std) + Lean | **≈ $440** (Spanne $270–885) | **≈ $775** (Spanne $440–1.665) | $7.3 / $6.5 |
| Higgsfield Ultra (Kling) + Lean | ≈ €129 + $185–255 | ≈ €129 + $430–570 | ~$5.5–6.5 / ~$4.8–5.9 (bei €≈$) |
| **Mittel** (Veo 3.1 Fast) + Lean/Komfort | ≈ $585–810 | ≈ $1.065–1.290 | $10–13.5 / $9–11 |
| **Premium A** (Kling 3.0 Pro Audio) + Komfort | ≈ $1.030 | ≈ $1.730 | $17 / $14 |
| **Premium B** (Veo 3.1 Standard) + Komfort | **≈ $1.870** (Spanne $1.100–3.950) | **≈ $3.400** (Spanne $1.870–7.560) | $31 / $28 |

**Sensitivität:** Der größte Hebel ist die **Fehlgenerierungsrate** (2,0 → 3,0 Versuche = +50 % Videokosten) und die **Videosekunden pro Reel**. Eine Hybrid-Strategie (1–2 AI-Clips + 2–3 animierte Stills/Parallax in Remotion auf echten Produktfotos) senkt die Videokosten um ~40–60 % und verbessert gleichzeitig die Produkt-Treue (MODEL ASSUMPTION). Nicht enthalten: eigene Arbeitszeit, Produktmuster, Steuern/USt (Higgsfield-Preise zzgl. MwSt.).

---

## 10. Automatisierbarkeit der Pipeline

### 10.1 Schritt-für-Schritt-Bewertung

| # | Pipeline-Schritt | Automatisierbar heute? | Tools / APIs | Human-in-the-Loop (HITL) | Begründung |
|---|---|---|---|---|---|
| 1 | Trend-/Produkt-Recherche | **Mittel** | NexLev (YouTube-Shorts-Outlier), Awin/impact-Feeds, Amazon Creators API (erst ab 10 Sales/30 Tage), LLM-Clustering | Nischen-/Saison-Entscheidung, Plausibilität | TikTok/IG haben keine offenen Trend-APIs für kommerzielle Nutzer (TikTok Research API nur akademisch) |
| 2 | Produktfeed | **Hoch** (Awin/impact sofort; Amazon nach Schwelle) | impact Catalogs (3.000 Req/h), Awin, Creators API | Initiale Programm-Freischaltungen | Amazon-Schwelle 10 Sales/30 Tage ist harte Hürde in Phase 1 |
| 3 | Produktauswahl | **Mittel–Hoch** | LLM-Scoring (Preis, Rating, Provision, „Visual Appeal", Saison) | Freigabe-Liste 1×/Woche (10–15 min) | Reputations-/Qualitätsrisiko schlechter Produkte |
| 4 | Konzept / Storyboard | **Hoch** | Claude/Codex mit Format-Templates (Before/After, „3 Finds", Dream-Room) | Stichprobe | – |
| 5 | Prompt-Erstellung | **Hoch** | LLM + Modell-spezifische Prompt-Templates, Referenzbild-Mapping | – | – |
| 6 | Bildgenerierung / Produkt-Compositing | **Hoch** (technisch) | Nano Banana Pro/2, FLUX Kontext/.2, Seedream; Freisteller + Outpaint | **Produkt-Treue-QA** (Form, Farbe, Logo, Text) | Kein Modell garantiert pixelgenaue Produktdetails |
| 7 | Videogenerierung | **Hoch** (technisch) | Veo 3.1 (Gemini API), Kling (fal/offiziell), Seedance/Wan (fal/Replicate), Higgsfield MCP | **Pflicht-QA** jedes Clips (Artefakte, Physik, Hände, Produktdrift) | Größter Zeitblock; Auto-Vorfilter per Vision-LLM möglich (Logo-/Farbvergleich zum Referenzbild), finale Freigabe menschlich |
| 8 | Hook / On-Screen-Text | **Hoch** | LLM, A/B-Varianten | Stichprobe | – |
| 9 | Voiceover / Musik | **Hoch** | ElevenLabs/Gemini TTS API; Meta Sound Collection/Suno | Aussprache-Check Markennamen | – |
| 10 | Schnitt / Captions / Render | **Hoch** | Remotion + FFmpeg (+ Whisper-Timing) | Endabnahme (30 s/Reel) | – |
| 11 | Caption / Hashtags / Disclosure | **Hoch** (Text) / **Niedrig** (Recht) | LLM; `is_paid_partnership` (IG), `is_aigc` + `brand_content_toggle` (TikTok) | **Compliance-Check** (Werbekennzeichnung, KI-Kennzeichnung, keine irreführenden Produktaussagen) | Haftungsrisiko liegt beim Betreiber |
| 12 | Affiliate-Zuordnung / Links | **Hoch** | Awin Link Builder, impact Tracking-Links, Amazon-Tag-Links + Geniuslink, Landingpage mit Reel-ID | – | – |
| 13 | Posting | **Hoch** (IG, YT, Pinterest) / **Mittel** (TikTok) | IG Graph API (100/24 h, Trial Reels), YouTube (100/Tag; Audit), Pinterest v5; TikTok via Buffer/Metricool oder Drafts (5 pending/24 h) | Wöchentlicher Kalender-Check | TikTok-Audit schließt Privat-Tools aus |
| 14 | Comment-to-DM | **Hoch** | CreatorFlow/Inrō/LinkDM/ManyChat | Moderation von Fragen/Beschwerden | – |
| 15 | Analytics-Sammlung | **Hoch** | IG Insights, YT Analytics, Pinterest (90 Tage), TikTok Display API (nur Zählwerte) | – | – |
| 16 | Affiliate-Reporting | **Mittel** | Awin (20 Calls/min), impact API/MCP, CJ | **Amazon: manueller CSV-Export** | Kein Amazon-Reporting-API |
| 17 | Winner Detection | **Hoch** (Regeln/Statistik) | Skript: Views/Reach, Skip-Rate, Saves/Shares-Rate, DM-Klicks/Reel → Score | Interpretation, Hypothesen | Kleine Stichproben → Fehlalarme |
| 18 | Varianten / Iteration | **Hoch** | Re-Generierung Hook/erste 3 s; IG **Trial Reels** mit `SS_PERFORMANCE`-Graduation | Budget-/Themen-Entscheid | Trial Reels erlauben Tests an Nicht-Follower ohne Feed-Belastung |

### 10.2 Befund Produkt-Treue (echtes Produkt in AI-Szene)

| Ansatz | Zuverlässigkeit Form/Farbe | Logo / Schrift | Aufwand | Datenqualität |
|---|---|---|---|---|
| **A) Echtes Produktfoto freistellen + Szene generieren (Outpaint/Inpaint, Relight)** – Produktpixel bleiben echt | sehr hoch | sehr hoch (Originalpixel) | niedrig–mittel | MODEL ASSUMPTION (technisch deterministisch) |
| **B) Bild-Reference-Editing** (Nano Banana Pro ≤ 6 Objekt-Refs „high-fidelity", NB2 ≤ 10, FLUX Kontext/.2, Seedream 5) | hoch bei einfachen, starren Produkten | mittel: kleine Schrift/Logos driften teils | niedrig | CLAIMED (Hersteller) / MODEL ASSUMPTION |
| **C) Image-to-Video aus A/B-Startframe, wenig Bewegung** (Veo 3.1, Kling 3.0, Seedance) | mittel–hoch in kurzen, ruhigen Shots | mittel–niedrig bei Rotation, Händen, Nahaufnahmen | mittel | MODEL ASSUMPTION |
| **D) Reference-to-Video** (Veo „Ingredients" ≤ 3 Bilder/8 s; Kling 3.0 Omni Elements; Seedance 2.x Multi-SKU; Higgsfield Marketing Studio `product_ids`) | mittel | Hersteller behaupten „precise lettering", unabhängige Tests fehlen | mittel | CLAIMED |
| **E) Objekt-Ersetzung in bestehendem Video** (Higgsfield Genjutsu, Kling 3.0 Omni Edit) | unbelegt | unbelegt | mittel | CLAIMED |

**Gesamturteil:** Ein **echtes** Produkt lässt sich 2026 auf **Bildebene** zuverlässig in AI-Szenen integrieren (Ansatz A/B). Auf **Videoebene** sind Form und Farbe in kurzen, ruhigen Einstellungen meist brauchbar, **Logos, Etikettentexte und feine Details bleiben der häufigste Fehlerpunkt** – ein unabhängiger, quantitativer Benchmark existiert nicht (Datenlücke). Arbeitshypothese (MODEL ASSUMPTION): 30–60 % der Produkt-Clips zeigen sichtbare Detailabweichungen → daher Versuchsfaktor 2–3 und Pflicht-QA. Praxisregel: Produkt-Nahaufnahmen und End-Card mit **echtem Foto**, AI-Video für Atmosphäre/Raum/Bewegung; keine AI-gerenderten Produkttexte zeigen; Produktaussagen nur aus Datenfeed.

### 10.3 Manueller Aufwand pro Woche (MODEL ASSUMPTION)

Annahme: Pipeline ist gebaut (einmalig ~40–80 h für Skripte, Templates, API-Audits, Accounts), Batch-Produktion am Wochenende.

| Tätigkeit | Minuten pro Reel | 60 Reels/Monat (~14/Woche) | 120 Reels/Monat (~28/Woche) |
|---|---|---|---|
| Produkt-/Konzeptfreigabe | 3–4 | 0,7–0,9 h | 1,4–1,9 h |
| Clip-QA inkl. Produkt-Treue (≈ 10 Generierungen sichten, Auswahl, Re-Runs anstoßen) | 10–15 | 2,3–3,5 h | 4,7–7,0 h |
| Endabnahme Reel + Caption/Disclosure-Check | 4–6 | 0,9–1,4 h | 1,9–2,8 h |
| Fehlerbehandlung (API-Fehler, Neu-Renders) | 2–4 | 0,5–0,9 h | 0,9–1,9 h |
| **Summe variabel** | **~19–29 min/Reel** | **~4,4–6,7 h** | **~8,9–13,5 h** |
| Fix: Analytics-/Winner-Review, Amazon-CSV, Planung | – | 1–2 h | 1,5–2,5 h |
| Fix: Community/DMs (nicht automatisierbare Antworten) | – | 1–2 h | 1,5–2,5 h |
| Fix: Pipeline-Wartung (API-/Preisänderungen, Modellwechsel) | – | 1–2 h | 1–2 h |
| **Gesamt pro Woche** | | **≈ 7,5–13 h** | **≈ 13–20 h** |

Begründung: Generierung/Rendering selbst ist Maschinenzeit (z. B. 120 Reels × 10 Generierungen = 1.200 Jobs/Monat ≈ 300 pro Wochenende; bei 6–20 parallelen Jobs und 1–3 min/Job ≈ 1–3 h Wall-Clock). Der menschliche Engpass ist die visuelle QA; ein Vision-LLM-Vorfilter (Vergleich mit Referenzfoto) kann die QA-Zeit schätzungsweise um 30–50 % senken, ersetzt die Freigabe aber nicht.

---

## Datenlücken

1. **Produkt-Treue:** Kein unabhängiger, quantitativer Test (Logo-/Text-/Form-Treue) für Veo 3.1, Kling 3.0 Omni, Seedance 2.x, Marketing Studio gefunden – nur Herstellerclaims. → Eigener Pilot-Test mit 5–10 realen Produkten empfohlen (Budget ~$20–50).
2. **Kling offizielle API-Preise** (kling.ai/dev, JS-gerendert) und **Hailuo/MiniMax-, Luma-API-Preise**: nur Drittquellen, teils widersprüchlich.
3. **ManyChat, Beacons, Stan, Publer, Krea, Udio, CapCut, ChatGPT-Preise**: Seiten blockiert (403) oder JS-gerendert → UNKNOWN/UNKNOWN\*.
4. **Instagram-spezifische Reichweitendaten KI vs. real**: keine Studie; vorhandene Belege betreffen YouTube Shorts (Kapwing, NexLev).
5. **Konsumenten-Trust-Studien 2025/26** (AI-Slop-Backlash, Kaufabsicht): nicht verifiziert.
6. **TikTok „weniger KI"-Regler, Pinterest „see fewer AI Pins"**: nur Vorwissen, Primärseiten nicht auffindbar.
7. **Instagram Graph API**: Kein dokumentierter Parameter für das „AI info"-Label; Musik aus IG-Bibliothek per API nicht setzbar.
8. **Pinterest API Access-Tiers** (Trial vs. Standard) und deren Limits für Video-Pins: nicht dokumentiert gefunden.
9. **Higgsfield-Credit-Kosten je Modell**: Anbieter-Äquivalente und Drittquellen weichen ab (5 vs. 7 Cr für Kling 3.0; ~56 % Diskrepanz laut Creatify).
10. **EU AI Act Art. 50** (Transparenzpflichten für KI-generierte Inhalte ab 02.08.2026) – Stand etwaiger Verschiebungen nicht geprüft → Compliance-Agent.
11. **Wechselkurs/USt**: Kosten in USD bzw. EUR netto; keine Umrechnung vorgenommen.

---

## Quellenliste (abgerufen 2026-09-26, sofern nicht anders angegeben)

**Video/Bild – Primär**
- Google Gemini API Pricing: https://ai.google.dev/gemini-api/docs/pricing (Seite aktualisiert 24.09.2026)
- Google Veo Doku: https://ai.google.dev/gemini-api/docs/veo
- Google Bildgenerierung Doku: https://ai.google.dev/gemini-api/docs/image-generation
- OpenAI Deprecations (Sora/Videos API): https://developers.openai.com/api/docs/deprecations
- OpenAI API Pricing: https://developers.openai.com/api/docs/pricing
- fal.ai Pricing: https://fal.ai/pricing
- fal Kling 3.0 Pro I2V: https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video
- fal Kling 3.0 Standard I2V: https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video
- fal Veo 3.1 Fast I2V: https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video
- Runway API Pricing: https://docs.dev.runwayml.com/guides/pricing/
- Black Forest Labs Pricing: https://docs.bfl.ml/quick_start/pricing
- Pika Pricing: https://pika.art/pricing
- Replicate Pricing: https://replicate.com/pricing
- Kling Omni Guide (Claims): https://kling.ai/blog/kling-video-3-omni-multi-shot-native-audio-guide (26.06.2026)
- Hugging Face Wan-AI: https://huggingface.co/Wan-AI ; https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B
- Hugging Face LTX-2.5: https://huggingface.co/Lightricks/LTX-2.5
- Higgsfield MCP (`models_explore` list/get/recommend, `show_plans_and_credits`) – Live-Abfrage 2026-09-26
- Recraft API Pricing: https://www.recraft.ai/docs/api-reference/pricing ; https://www.recraft.ai/pricing
- Ideogram Pricing: https://ideogram.ai/pricing/?pricing_tab=api
- Topaz Pricing: https://www.topazlabs.com/pricing
- Magnific Pricing: https://www.magnific.com/pricing
- ReimagineHome: https://www.reimaginehome.ai/pricing
- Interior AI: https://interiorai.com/

**Video/Bild – Drittquellen**
- CloudZero Kling Pricing: https://www.cloudzero.com/blog/kling-ai-pricing/ (18.09.2026)
- CellCog Seedance 2.5 Pricing: https://cellcog.ai/blog/seedance-2-5-pricing/ (22.08./08.09.2026)
- Apiframe Seedance 2.0: https://apiframe.ai/models/seedance-2.0/pricing
- BuildMVPFast AI-Video-API-Kosten: https://www.buildmvpfast.com/api-costs/ai-video (Juli 2026; teils inkonsistent)
- CostGoat Sora: https://costgoat.com/pricing/sora (Sept. 2026)
- eesel Gemini Omni 1.1: https://www.eesel.ai/blog/gemini-omni-1-1-flash-pricing
- eesel Luma: https://www.eesel.ai/blog/luma-ai-pricing (05.06.2026)
- eesel Midjourney: https://www.eesel.ai/blog/midjourney-pricing
- Scopeful Higgsfield: https://www.scopeful.org/blog/higgsfield-pricing-2026 (07.08.2026)
- Creatify Higgsfield vs Kling: https://creatify.ai/blog/higgsfield-vs-kling-ai-quality-cost-per-second-and-which-to-use-for-ads-in-2026 (26.09.2026)
- Higgsfield Blog Modellvergleich: https://higgsfield.ai/blog/5-Best-AI-Video-Models-2026-Tested-Compared (29.08.2026)
- AI Free API GPT-Image-Preise: https://www.aifreeapi.com/en/posts/openai-image-generation-api-pricing (06.09.2026)

**Audio**
- ElevenLabs API Pricing: https://elevenlabs.io/pricing/api
- Suno Pricing: https://suno.com/pricing
- Instagram Hilfe (Musik/Business-Accounts): https://www.facebook.com/help/instagram/402084904469945

**Editing/Rendering**
- Remotion Lizenz: https://www.remotion.pro/license
- Creatomate: https://creatomate.com/pricing
- Shotstack: https://shotstack.io/pricing/
- JSON2Video: https://json2video.com/pricing/
- Submagic: https://www.submagic.co/pricing
- Captions: https://www.captions.ai/pricing
- Opus Clip: https://www.opus.pro/pricing
- Descript: https://www.descript.com/pricing

**Posting/Analytics**
- IG Content Publishing: https://developers.facebook.com/docs/instagram-platform/content-publishing/
- IG Media-Referenz (Reel-Specs, trial_params, Paid Partnership): https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media
- IG Platform Overview: https://developers.facebook.com/docs/instagram-platform/overview
- IG Media Insights: https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights
- TikTok Content Posting (Get Started / Direct Post / Upload / Guidelines): https://developers.tiktok.com/doc/content-posting-api-get-started ; https://developers.tiktok.com/doc/content-posting-api-reference-direct-post ; https://developers.tiktok.com/doc/content-posting-api-reference-upload-video ; https://developers.tiktok.com/doc/content-sharing-guidelines
- TikTok Display API & Video-Objekt: https://developers.tiktok.com/doc/display-api-overview ; https://developers.tiktok.com/doc/tiktok-api-v2-video-object
- TikTok Research API: https://developers.tiktok.com/products/research-api/
- YouTube Quota & videos.insert: https://developers.google.com/youtube/v3/determine_quota_cost ; https://developers.google.com/youtube/v3/docs/videos/insert
- YouTube Analytics Metriken: https://developers.google.com/youtube/analytics/metrics
- Pinterest Video-Pins: https://developers.pinterest.com/docs/work-with-organic-content-and-users/create-boards-and-pins/
- Pinterest OpenAPI v5: https://github.com/pinterest/api-description
- Metricool: https://metricool.com/pricing/ ; Buffer: https://buffer.com/pricing ; Later: https://later.com/pricing/ ; Hootsuite: https://www.hootsuite.com/plans ; Blotato: https://www.blotato.com/pricing ; Repurpose.io: https://repurpose.io/pricing/

**Affiliate**
- Amazon Creators API: https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction
- Amazon PA-API-5-Deprecation: https://affiliate-program.amazon.com/creatorsapi/docs/en-us/paapiv5-deprecation
- Awin API: https://help.awin.com/developers/apidocs/introduction
- impact.com Partner API: https://integrations.impact.com/partner-api-reference/readme.md ; Rate Limits: https://integrations.impact.com/partner-api-reference/readme/rate-limits.md ; MCP: https://integrations.impact.com/ai-solutions/mcp-tools/partner-mcp-tools.md
- CJ Developer Portal: https://developers.cj.com/

**Link/DM/Landingpage**
- LinkDM: https://linkdm.com/pricing ; CreatorFlow: https://creatorflow.so/pricing ; Inrō: https://www.inro.social/pricing
- Linktree: https://linktr.ee/s/pricing
- Geniuslink: https://geniuslink.com/pricing
- Vercel: https://vercel.com/pricing
- Claude: https://claude.com/pricing

**Evidenz / Plattform-Policies**
- Kapwing AI-Slop-Report: https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/ (28.11.2025)
- YouTube YPP-Policies (inauthentic content): https://support.google.com/youtube/answer/1311392
- YouTube CEO-Brief 2026: https://blog.youtube/inside-youtube/the-future-of-youtube-2026/ (21.01.2026)
- Meta AI-Labeling: https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
- Pinterest Gen-AI-Labels: https://help.pinterest.com/en/article/gen-ai-labels
- NexLev-Datenbank (MCP `search_shorts_niche_finder_channels`, isAiChannel=true; Queries „AI interior/architecture" und „AI product/gadgets"), abgerufen 2026-09-26
