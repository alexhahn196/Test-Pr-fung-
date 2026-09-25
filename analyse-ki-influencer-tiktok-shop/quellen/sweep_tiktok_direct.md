# Sweep: Direct TikTok discovery of AI / faceless TikTok-Shop accounts

Access date for everything below: **2026-09-24**. Tags: **Verified** = seen in TikTok's own SSR JSON via `tt_profile.sh` / `tt_video.sh` (follower counts, playCount, `aigcLabelType`, `ttSeller`, `commerceUser`, anchors) or in a primary document; **Claimed** = asserted by a third party (Reddit post, YouTube guru, press); **Estimated** = my calculation, formula shown. "Not publicly verifiable" where no public data exists.

TikTok field legend (Verified from SSR JSON): `aigcLabelType` 1 = creator self-labelled "AI-generated"; 2 = platform-applied AI label; null = no label. `ttSeller` = account runs a TikTok Shop; `commerceUserInfo.commerceUser` = business/commerce account flag. `isAd` = promoted/boosted post; `isECVideo` = e-commerce video flag; `anchors` = attached product/app links.

## 0. Method and what did / did not work

| Channel | Result |
|---|---|
| `tiktok.com/discover/<slug>` (ai-ugc-tiktok-shop, faceless-ai-tiktok-shop-examples, ai-influencer-tiktok-shop, ai-generated-ugc-lady, ai-tiktok-shop-affiliate, ai-avatar-tiktok-shop, ai-ugc-creator, ai-generated-tiktok-shop-videos) | Pages exist (SSR key `webapp.kap-detail`, canonical URL present) but **contain no item list** for headless clients (Chrome UA, Googlebot UA = 9-byte response, mobile UA). Only a meta description. No handles extractable. |
| `tiktok.com/tag/<tag>` (aiugc, aiinfluencer, aiavatar, tiktokshopfinds, aiugccreator, faceless, tiktokshopaffiliate, kiinfluencer) | Same: ~360 KB shell, no items. |
| Profile pages (`/@handle`) | SSR contains `userInfo` + `stats` only; **no video list** (as documented in TOOLS.md). |
| WebSearch tool | Budget exhausted (200/200) before this agent started. |
| Bing / Yahoo / DDG (html + lite) / Startpage / Yandex / Google / Mojeek via curl or WebFetch | Bing ignores `site:` for these queries; DDG = captcha; Yandex = captcha; Startpage / Google / NYT / BI / Independent / Straits Times = blocked for WebFetch; Mojeek = 355-byte stub. |
| **Brave Search via WebFetch** | **Works, but only ~1 query per turn** (parallel calls → HTTP 429). Source of most video URLs below. |
| Reddit JSON dumps already in `research/reddit/*.json` | 4 concrete TikTok video URLs + 1 short link; all verified below. Live Reddit API returns HTML (blocked). |
| Google News RSS + Bing News RSS via curl | Works; gave the press list in §4 (article bodies mostly paywalled/blocked). |
| 404 Media | Fetchable. Named accounts: `poormaninla`, `liverboosthub11` (Jul 2026 article); `melisogn9dl`, "Mothers in Healing" (Oct 2024 article). |
| NexLev `watch_tiktok_video_and_ask` | Works (used on 6 videos). `watch_youtube_video_and_ask` = daily limit exhausted (15/15). |
| NexLev YouTube transcripts / descriptions | Used for DE (TikFluencer) and EN case studies; gurus almost never speak their handles. |

## 1. Verified candidates (TikTok data seen on 2026-09-24)

Format: handle — model type — country — Verified numbers — evidence — AI check — assessment.

### 1.1 Fully virtual AI influencers (model A) checked for commerce activity

| Handle | Verified (tt_profile.sh) | Commerce flags | Notes |
|---|---|---|---|
| `lilmiquela` | nickname "LIL MIQUELA", verified ✓, 3,300,000 followers, 48.9M likes, 220 videos, bio "23 LA Robot… Prototype feat. John Liwag out now", bioLink ffm.to (music) | ttSeller **false**, commerceUser **false** | No TikTok-Shop activity. Monetises via brand deals/music, not Shop. Benchmark for "virtual influencer without Shop". |
| `bermudaisbae` | "Bermuda Is Bae", verified ✓, 43,300 followers, 143.4k likes, **5 videos**, bio "Robot/Unbothered… follow me on IG" | false / false | Dormant on TikTok. No Shop. |
| `kenza.layli` | "Kenza Layli", 47,200 followers, 76.6k likes, 53 videos, bio "First Moroccan Meta Humans powered by AI / Proudly First World miss AI 2024" | false / false | Real virtual influencer; no Shop flags, no bio link. |
| `magalu` (Lu do Magalu, Magazine Luiza) | "Lu do Magalu", 7,500,000 followers, 1,526 videos, bio "Oi, eu sou a Lu! Seja bem-vindo ao TikTok oficial do Magalu!" | ttSeller false, commerceUser false | Largest virtual-influencer retail account found; commerce happens off-platform (Magalu app), not via TikTok Shop flags. (Handles `magazineluiza`, `lu.magalu`, `lumagalu` = unrelated 0–50-follower accounts.) |
| `fit_aitana` | "Aitana Lopez✨\| Virtual Soul", 18 followers, 0 videos, bio "Based in Barcelona \| Digital Muse" | false/false | Aitana's TikTok is effectively empty. `aitana_lopez` (767 fol., 82 videos, bio "🤍👑💗") and `aitana.lopez` (101 fol., 0 videos) are not clearly the Clueless-agency account → not attributable. |
| `imma.gram` | "imma", 44 followers, 1 video | false/false | Not imma's real presence (imma is IG/YouTube-centred). |
| `noonoouri`, `noonoouri_` | placeholder accounts (12 / 1 followers, 0 videos) | – | No TikTok presence under these handles. |
| `emily_pellegrini` | 12 followers, 2 videos, bio links beacons.ai/emilypellegrini | false/false | Squatter/placeholder. |
| `lexi.love` | 27 followers, 0 videos | – | Empty. |
| `milla.sofia` | 2 followers, Finnish personal account | – | Not the AI influencer. |
| `shudu.gram` | statusCode 10222 (private), 0 followers | – | Not active. |
| `mia_zelu`, `rozy.gram`, `rozy_sidus`, `kyraonig`, `daisy.yoox`, `zeroxlucy`, `lilmiquela.ai` | statusCode 10221 (not found) | – | Do not exist on TikTok under these handles. `lucy.lotte` (9 fol.), `leyalove` (13 fol.), `imma_official` (28 fol.) = empty placeholders. |

**Finding:** none of the well-known virtual influencers has `ttSeller` or `commerceUser` set, and none has a TikTok-Shop-related bio. Model A + TikTok Shop is, on the evidence available, **not a thing at the top of the market**; it exists only in small AI-persona accounts (below).

### 1.2 AI persona / AI UGC / AI affiliate accounts (models B, C, H)

**`theamberjai`** — model B (realistic AI persona, lifestyle "it-girl") — US.
- Verified profile: nickname "Amber Jai", 22,800 followers, 149.7k likes, 36 videos, account created 2026-03-09 (createTime 1773024857), bio "Digital Content Creator / My only page / Helping people start and monetize with AI / 📧 theamberjai@gmail.com". ttSeller false, commerceUser false, no bio link.
- Verified video https://www.tiktok.com/@theamberjai/video/7661998341034757406 ("Solo diaries EP 1 ✨", 33 s, created 2026-07-13): **20,800 plays**, 1,348 likes, 93 comments, 189 shares, 436 saves; `aigcLabelType` **null** (no AI label); no anchors; not an ad.
- AI check (NexLev/Gemini watch, 2026-09-24): "highly likely an AI-generated virtual influencer… Confidence High (90%+)"; brands shown: Sephora, Dior perfume, Huda Beauty, Touchland, Danessa Myricks, Zara; "no explicit TikTok Shop card or affiliate CTA"; "Gossip-Girl-style" AI voiceover.
- Claimed (Reddit r/… post in `research/reddit/tiktok shop affiliate AI avatar.json`, 2026): "[She] monetizes her AI in a bunch of ways including weekly livestreams that make her $15K/mo" → **not publicly verifiable**.
- Assessment: AI persona doing beauty/fashion lifestyle content with product placement but **no TikTok-Shop anchors and no AI label** on the checked video. Monetisation appears to be "teach people AI" (bio) rather than Shop commissions. Engagement 20.8k plays / 22.8k followers ≈ 0.9 plays per follower (Estimated).

**`_keepher1`** — model A/B (self-declared "AI Influencer/Creator") — US.
- Verified profile: nickname "EB \| KeepHer1 Digital", 1,911 followers, 39,200 likes, 125 videos, created 2024-12-03, bio "💕AI Influencer/Creator 💰Helping creators build income 💫with AI content", bioLink beacons.ai/keepher1digital. ttSeller false, commerceUser false.
- Verified video https://www.tiktok.com/@_keepher1/video/7664803600756968734 ("Home Sweet Home😍", 15 s, created 2026-07-21): **565 plays**, 50 likes, 5 comments; **`aigcLabelType` = 1 (creator-labelled AI-generated)**; no anchors.
- AI check: Gemini watch returned "Real person… Aiyana Lewis… 100%" — **contradicted by TikTok's own creator-applied AI label (=1) and the bio**. I treat the TikTok label as authoritative; the vision model was fooled (or the clip is an AI likeness). Content: "COME HOME WITH ME MINI VLOG", G-Wagon, luxury house, scripted female voiceover; no Shop card.
- Claimed (same Reddit post): "This TikToker monetizes her page with TikTok Shop affiliate and made $900 in one day" → not publicly verifiable; the linked video has **no product anchor** and 565 plays, i.e. the claim cannot be tied to that video.
- Assessment: **low performer** (avg. 39.2k likes / 125 videos ≈ 314 likes per video, Estimated); sells "AI content" coaching via beacons. Good example of "AI influencer account that is labelled AI and gets ~500 plays".

**`clothing_findsj`** — model C/H (AI-generated model wearing the affiliate product, image→video) — Philippines.
- Verified profile: nickname "SJ cloᥫ᭡", 2,060 followers, 146 videos, bio "OUTFIT RECOS \| AI AFFILIATE ᥫ᭡ visit my showcase for more outfits". ttSeller false, commerceUser false.
- Verified video https://www.tiktok.com/@clothing_findsj/video/7620812741850303752 (127 s, created 2026-03-24): **182,700 plays**, 6,978 likes; **`aigcLabelType` = 1**; desc "This is how i make my AI Affiliate videos.🤍 …#aimodel #aia…".
- AI check (Gemini watch): full workflow shown — screenshot product from shop app → Pinterest background → **Gemini** image prompt ("A 5'6 thin body size confident girl… taking a mirror selfie no face. wearing the same exact products… 9:16") → **Meta AI** to remove watermark and animate ("don't walk… don't show the face") → save via Instagram story. Finished clip = faceless AI model in mirror-selfie pose wearing the "LNY FIRERIE 2 PIECE SET" (women's fashion). No AI label visible inside the tutorial; no Shop card in the tutorial itself (the account's product videos live in its showcase).
- Assessment: **the clearest documented "AI affiliate" workflow found**: zero-cost consumer AI tools, faceless AI model, product from TikTok Shop showcase. Follower base tiny (2k) but the tutorial itself out-performs (182.7k plays ≈ 89 plays per follower, Estimated). Income: not publicly verifiable.

**`cia_tuballas`** — model C/E (AI hands/arm holding the product) — Philippines.
- Verified profile: "★Cia Shop's★", 5,385 followers, 834 videos, bio "Thank u for visiting my TikTok Shop's🎀 … Open for Collab". ttSeller false, commerceUser false.
- Verified video https://www.tiktok.com/@cia_tuballas/video/7628827893702970644 (50 s, created 2026-04-15): **205,500 plays**, 8,420 likes; **`aigcLabelType` = 1**; desc "Tutorial Gamit ang 3 apps lang for ai affiliate videos #tutorial #aivideos #aiaffiliate".
- AI check: apps = **Pinterest, Gemini, Wan**; finished clip shows AI-generated hands in a red sweater holding red wedding shoes; **TikTok's "AI-generated" label visible top-left** of the result; Shop card shown with price ₱613.13 (from ₱1,048.07) and **commission ₱68.12 per sale** (≈11 %, Estimated 68.12/613.13).
- Assessment: mass-produced product-demo format (834 videos on a 5.4k-follower account ≈ 6.5 followers gained per video, Estimated). Low-ticket products, low commission per sale. Income not publicly verifiable.

**`jayflix_ai`** — model B/G (AI models for affiliate, sells course) — US.
- Verified profile: "jayflix", 54,500 followers, 142 videos, bio "Don't just consume AI. Become an AI Creator…", bioLink aicreatorsimplified.com. ttSeller false, commerceUser false.
- Verified video https://www.tiktok.com/@jayflix_ai/video/7542744999667043585 (20 s, created 2025-08-26): 34,700 plays, 295 likes; `isAd` **true** (boosted); desc "Tiktok affiliate marketing but only using AI models? Yes, possible! #aimodels #tiktokaffiliatemarketing".
- Assessment: guru account selling an AI-creator course; the "AI model affiliate" demo is a paid promotion with weak organic engagement (0.85 % like rate, Estimated 295/34,700).

**`andrewscizza`** — model B/G (AI influencers, 18-year-old guru) — US.
- Verified profile: "Andrew Scizza", 57,100 followers, 192 videos, bio "Road to $1 Million at 18 💰 I don't sell a course / Software I use to make AI Influencers👇", bioLink earshot.to.
- Verified video https://www.tiktok.com/@andrewscizza/video/7611128479274323222 (30 s, created 2026-02-28): 27,500 plays, 911 likes; desc "pretty crazy stuff #tiktokshopaffiliate #tiktokshop #aicontent" (Brave snippet: "TikTok shop is NOT cracking down on AI??").
- Assessment: commentary/guru; promotes an AI-influencer tool via affiliate link. Income claims: none verifiable.

**`zachbtts`** — model G (UK affiliate who builds AI avatars for Shop content) — UK.
- Verified profile: "Zach TTS", 3,641 followers, 22,100 likes, 45 videos, created 2024-10-05, bio "TikTok Shop Affiliate 🤝🏻 / **£800k+ GMV** 📈". ttSeller false, commerceUser false.
- Verified video https://www.tiktok.com/@zachbtts/video/7606377842565303574 ("Create Your Own AI Avatar for TikTok Shop", 99 s, created 2026-02-13): 23,500 plays, 1,100 likes, **1,170 saves**, 147 shares; hashtags #ai #tiktokshopaffiliate #tts #ttsaffiliate; no AI label, no anchors.
- Claimed: "£800k+ GMV" (bio, self-reported, no period given) → not publicly verifiable. Note GMV ≠ commission.
- Assessment: human affiliate moving to AI-avatar production; tutorial has a 5 % save rate (Estimated 1,170/23,500) = high intent audience.

**`liverboosthub11`** — model D/H (faceless supplement account; source of the script copied in the Rosabella case) — US.
- Verified profile: nickname "Health u1s1", 2,668 followers, 60,200 likes, 137 videos, created 2025-06-04, empty bio, no link. ttSeller false, commerceUser false.
- Evidence: 404 Media, "Inside an AI TikTok Shop Slop Factory That Shills Supplements Recalled By the FDA" (Jason Koebler, 2026-07-30, https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/): Harry Chang "copy-pasted the script from a video posted by an account called 'liverboosthub11' and tweaked it"; the resulting AI video (Veo 3 + HeyGen + ElevenLabs voice "Latisha 1", CapCut) "goes on to get 1.3 million views on TikTok and apparently earned him tens of thousands of dollars in affiliate sales" (Claimed by Chang in a now-deleted YouTube video, per 404 Media).
- Assessment: still live; 137 videos, 22 likes/follower. Whether its own videos are AI is not verified (no video URL obtainable). Included as the documented "script donor" of the AI supplement funnel.

**`poormaninla`** — model C (AI "doctor in a white coat" videos for Rosabella beetroot) — US — **removed/renamed**.
- Verified: statusCode **10221 (user not found)** on 2026-09-24.
- Evidence: Humann v. Ambrosia Brands lawsuit as quoted by 404 Media: "in a June 14, 2025 TikTok post, influencer 'poormaninla' purports to depict a doctor in a whitecoat that promotes the alleged health benefits of Defendant's products… The 'poormaninla' account is still up on TikTok and its videos are almost entirely AI-generated. Several of the videos have hundreds of thousands of views." (article dated 2026-07-30). Two months later the handle resolves to nothing → **failure case** (ban or rename after press/lawsuit).

**`melisogn9dl`** and "Mothers in Healing" — model D (AI-image slideshows shilling Reus Research NAD+) — **gone**.
- Evidence: 404 Media, 2024-10-07, "AI-Generated Pro-North Korean TikToks Are Also Bizarre Ads for Supplements": account "@melisogn9dl" posting the slideshows; "This account, called 'Mothers in Healing,' had dozens of slideshows with AI-generated cover images about North Korea, and all of them shilled Reus Research's Nicotinamide Riboside… one video that had more than 3 million views."
- Verified 2026-09-24: `melisogn9dl` = 10221 not found; `mothersinhealing`, `mothers.in.healing`, `mothers_in_healing` = not found. → **failure case** (accounts removed).

### 1.3 Sellers / brands using AI-labelled or AI-voiced product ads (models E, F)

**`pinecommerce`** — model E/F (seller running 8-second AI-voiced product ads, one platform-labelled AI) — US.
- Verified profile: "Pine Commerce", 628 followers, 2,958 likes, **509 videos**, created 2020-12-25, bio "Ur mom"; **ttSeller = true**, **commerceUser = true** (category "Shopping & Retail").
- Verified video A https://www.tiktok.com/@pinecommerce/video/7583656838365711629 ("#pestcontrol", 8 s, created 2025-12-21): **136,200 plays**, 335 likes, 97 shares; `isAd` **true**, `isECVideo` **1**; `aigcLabelType` null.
- Verified video B https://www.tiktok.com/@pinecommerce/video/7591510508851825975 ("#pestcontrol", 8 s, created 2026-01-04): **58,900 plays**, 239 likes; `isAd` true, `isECVideo` 1; **`aigcLabelType` = 2 (platform-applied AI label)**.
- AI check on B (Gemini watch): voice = "AI-generated (95 % confidence)… synthetic text-to-speech"; footage = "Real (90 %)… real hand holding the product box"; product = "Multifunction Ultrasonic Pest Repeller", on-screen "$7.99 + Free 3 Day Shipping"; hook "This device removed rodents from my home"; no visible AI disclosure in-frame.
- Claimed (Reddit post quoting the account owner, in `research/reddit/AI UGC tiktok shop.json`): "organic content is doing $200–$300 a day without spend… 100K views: [video A] 31.5K views: [video B]". The videos are flagged `isAd=true` in TikTok data, so "without spend" is contradicted by the data (Verified).
- Assessment: **mass-produced (509 videos), 8-second, TTS-voiced, price-overlay ads on a 628-follower seller account** – the purest model F example found; reach comes from ads/GMV-Max, not followers (217 plays per follower on video A, Estimated).

**`peakrevivalx`** — model E/F (supplement brand, 996 videos, cited by a newsletter as the "faceless supplements" example) — US.
- Verified profile: "Peak Revival-X", **91,700 followers**, 1.4M likes, **996 videos**, created 2022-07-06, bio "Peak Revival-X Amazon ⬇️", bioLink peakrevivalx.com/amazon; **commerceUser = true** (category "Others"), ttSeller false.
- Evidence: Reddit repost of the "brainstorms" newsletter ("Faceless YouTube channels: golden opportunities or risky gambles") listing "Supplements ([great example here](tiktok.com/@peakrevivalx))" as a faceless niche example.
- AI check: no video URL obtainable → **AI use not verified**; brand-run, drives to Amazon rather than TikTok Shop (bio). Included as a high-volume faceless supplement account of unknown production method (model H at most).

**`_tuanhoang_`** — model E/G (Vietnamese TikTok-Shop agency selling "AI sales videos" as a service) — Vietnam.
- Verified profile: "Lại là Tuấn đây", **467,000 followers**, 1,015 videos, bio "CEO TN Holding ✅ Đối tác chính thức của Tiktokshop Việt Nam 🇻🇳 Hỗ trợ vận hành shop – chạy ads – booking KOC…" (official TikTok Shop VN partner; shop operations, ads, KOC booking).
- Verified video https://www.tiktok.com/@_tuanhoang_/video/7508722889999256839 (70 s, created 2025-05-26): 32,100 plays, 773 likes; `isAd` true, `isECVideo` 1; anchor CapCut; desc "Cách làm video A.I bán hàng, làm affiliate kiếm thêm thu nhập, bằng mẫu tuỳ chọn…" (how to make AI sales videos for affiliate with your own templates).
- Assessment: agency-side evidence that AI product videos are sold as a service in the VN TikTok Shop ecosystem.

### 1.4 Human faceless / semi-automated affiliate mentors (model G context, not AI personas)

| Handle | Verified | Relevance |
|---|---|---|
| `teachingtts` | "Teaching TTS", 53,800 fol., 1,334 videos, link liinks.co/teachingtts; video 7565682305252085022 "How to make a faceless TikTok shop video fast" (5,174 plays, 2025-10-26) | Faceless-Shop mentor; low reach on that video. |
| `coachtotty` | "Totty \| Content Strategist", 74,800 fol., 659 videos, stan.store link; video 7347766447520812334 "Heres how I create my faceless videos as a tiktok shop affiliate #greenscreen" (19,500 plays, 2024-03-18, anchor Green Screen) | Faceless = green-screen, not AI. |
| `thefasttrackgirl` | "Fast Track Girl ⚡️", **290,500 fol.**, 4,874 videos, **commerceUser true**; video 7328937761442991402 (103,000 plays, 5 s, 2024-01-27) | Brave snippet: "claiming 20K profit in 30 days with 30K followers" (Claimed, human, not AI) → human benchmark. |
| `lifesrad` | 331,600 fol., 2,098 videos; video 7630878408733396255 (111,700 plays, 289 s, 2026-04-20) "…don't even get me started on the AI remix 😤 @TikTok" | Human affiliate complaining about TikTok's AI-remix feature (context for §4). |
| `leo_giovannii` | 3,800,000 fol., 1,919 videos (Indonesia); video 7568343117066259732 "Boleh ga pakai AI untuk Ngonten Affiliate??" (251,300 plays, isAd true) | ID-market debate on AI affiliate content. |
| `densancar` | Deniz Sancar, 1,996 fol., 308 videos | YouTuber behind the "faceless AI TikTok Shop for 1 hour → £25" test (see claims_youtube.md). |
| `tommycetty` | "TommyCetty", 1,991 fol., 168 videos, created 2025-12-14, bio "Ai Affiliate Discord ⬇️", link simplemedia.ai | Guru behind the "$10,218.52 in 25 days" claim; his named earlier accounts: `healthiswealthfyp` (25,700 fol., 108 videos, created 2025-10-29, bio "Showing you the best videos that support our culture" – identity match plausible but unverified) and `holistic.sophia` (43 fol., Brazilian personal bio → **not** his; handle reassigned or misheard). |
| `xiaoyi9955` | "Kitty Snug Life", 18,200 fol., 490 videos; video 7670067930607996191 "…giant Q-tips… #TikTokShopFinds" **1,600,000 plays**, 25,000 likes, 1,943 shares (2026-08-04) | **Control case**: a Reddit post asked "Be honest, can you tell this video is AI?" linking this clip. Gemini watch: "real camera footage… Confidence High (99 %)", human voiceover, TikTok Shop product anchor visible, CTA "the 6-pack is linked here ↓". → Not AI. Shows how easily real UGC is mislabelled as AI in forums. |

### 1.5 Official TikTok accounts relevant to AI-content rules (Verified)

- `tiktokshopacademy` video https://www.tiktok.com/@tiktokshopacademy/video/7613646922557000990 "Using AI for your shop? Must-know rules before you post ⚠️ Here's what's actually allowed 👀 #aigenerated" — 67,900 plays, 2026-03-05, isAd true.
- `sellwithtiktokshop_us` video https://www.tiktok.com/@sellwithtiktokshop_us/video/7649616927941250334 "…TikTok Shop's upgraded AI Video Maker helps you create engaging shoppable videos…" — 27,300 plays, 2026-06-18, isAd true. (TikTok itself sells AI video generation to sellers.)

## 2. Reddit-sourced claims (all **Claimed**, none verifiable)

From `research/reddit/tiktok shop affiliate AI avatar.json` (post "I found several AI accounts that are earning from their work", 2026):
- "This creator (in image) made almost 80k from her AI Instagram from December thru March" (no handle).
- "This TikToker [@_keepher1] monetizes her page with TikTok Shop affiliate and made $900 in one day" → see §1.2 (video has no anchor, 565 plays).
- "[@theamberjai] monetizes her AI in a bunch of ways including weekly livestreams that make her $15K/mo".
- Another post: "One AI creator made $1k roughly from one TikTok shop affiliate video for a fashion item / Another AI creator made just under $80k selling digital products from a 4-month old brand new AI avatar account / Be honest, can you tell this video is AI? [link → @xiaoyi9955, verified REAL footage]".
- `research/reddit/tiktok shop affiliate month.json`: an affiliate reports accounts "@release141 – Disabled with $3,000 locked", "@undergroundwellness – Banned February 10… my earlier MB-focused account", "Over $120,000 GMV in April alone / Over $300,000 GMV total before the bans" (methylene-blue supplements; human or AI not stated; handles not re-checked because they are stated as banned).

## 3. German-language evidence (DE/EU)

- **TikFluencer** (Ralf Schmitz & Robby Schadt, launched ~July 2026) = the only German "KI-Avatar verkauft auf TikTok Shop" system found. Review videos (NexLev transcripts, 2026-09-24): "Online Markt Check" 7z3ulffcs7I: "Ein KI-Avatar soll rund um die Uhr Produkte über TikTok Shop verkaufen – ganz ohne eigenes Gesicht und eigene Stimme… du brauchst definitiv noch ein KI Tool namens Hickfield [Higgsfield]… rund 19 € im Monat… Das allergrößte Problem für Anfänger ist die sogenannte 1000 Followerhürde". Examples quoted from the sales webinar are **human** creators: "eine Creatorin namens Lish… mit einem einzigen Video über diese Dubai Schokolade fast 14 000 € Umsatz" and "ein Account namens Lina Halal Suetes [sic], der sechsstellige Monatsumsätze macht" (Claimed by the webinar; handles `lish`, `lish.official`, `lina.halalsweets`, `linahalalsweets`, `halalsweets.lina`, `lina_halal_sweets`, `kickkitchen`, `kick.kitchen`, `kick_kitchen` → not found / unrelated on 2026-09-24). "Marketing Secrets" oRbIohy7jdk: "ein deutsches Beispiel, ein Kanal namens Kick Kitchen, der mit einem einzigen viralen Video über diese berühmte Dubai Schokolade fast 14 000 € Umsatz gemacht hat".
- **tkay** (DE YouTuber, RCXhDcP5xU0 / M7t2WRgOJWg): claims "in einem Monat auf einem Account in 28 Tagen 84 900 $ Umsatz", "$12,300 in a single day", "$63,400 on another account", "wovon ich als Creator ungefähr 30 % bekomme"; **recommends buying US TikTok accounts (~$200–400)** and says "absolutely no one in Germany is talking about doing TikTok Shop" and "if you get banned on an account, all your money will be gone… I lost over 6k". All Claimed; no TikTok handles disclosed.
- No German-language TikTok account with AI avatar + Shop could be surfaced: the two DE Brave sweeps (`site:tiktok.com/@ KI "TikTok Shop" Affiliate Avatar`, `…KI Avatar "TikTok Shop" Affiliate deutsch`) and the Rosabella "AI doctor" sweep were blocked (WebFetch → HTTP 429; curl → Brave captcha page) after the six successful English queries; `kiinfluencer` tag page empty; `mayaaai` (13 fol., "Schaffen wir 55 Fans bitte") is the only DE-language AI-ish handle hit and is irrelevant. → **Open item for a later run**: repeat these three Brave queries one per turn once the rate limit resets.

## 4. Press context found via Google/Bing News RSS (2026-09-24)

- WSJ, 2026-07-15, "AI Videos Are Flooding TikTok Shop" (paywalled). Secondary: Affiverse 2026-07-17 https://www.affiversemedia.com/tiktok-shop-ai-generated-videos-affiliate-trust/ — SharkNinja CCO Neil Shah: "We didn't want an AI-generated Shark vacuum cleaning an AI-generated floor. We want real consumers seeing real products being used by real people"; SharkNinja "warned that commissions would be removed" for AI affiliate content; 11.3 M creators generated Shop affiliate sales globally in 2026, 945,000 in the US (Charm.io, Claimed).
- Affiverse 2026-07-27 https://www.affiversemedia.com/rare-beauty-ai-tiktok-shop-affiliate-videos/ — Rare Beauty "does not work with AI-generated creators or digital duplicates" (to WSJ).
- Business Insider 2026-07-20 "TikTok Shop creators are facing an AI reckoning"; The Independent 2026-07-15 "Brands urge TikTok Shop creators to ditch AI fakes"; PPC Land 2026-06-08 "TikTok Shop's quality rules ban AI voices and still images from LIVEs"; NYT 2026-03-09 "An Amish Avatar and an A.I. Monk Are Pitching Supplements on Social Media"; NYT video 2026-07-21 "The Fake Influencers Selling Wellness on Your Feed"; Bing News: "'It's organized crime': TikTok Shop says it's fighting a new wave of AI scammers" — bodies not fetchable from this sandbox (blocked hosts).
- 404 Media 2025-12-17 "Hack Reveals the a16z-Backed Phone Farm Flooding TikTok With AI Influencers": Doublespeed "uses a phone farm to manage at least hundreds of AI-generated social media accounts", "1,100 mobile phone farm"; account names withheld in the free excerpt.

## 5. Bottom line of this sweep

- 13 handles with AI relevance verified live (theamberjai, _keepher1, clothing_findsj, cia_tuballas, jayflix_ai, andrewscizza, zachbtts, liverboosthub11, pinecommerce, peakrevivalx, _tuanhoang_, kenza.layli, lilmiquela/magalu/bermudaisbae as A-type controls) + 3 documented removals (poormaninla, melisogn9dl, "Mothers in Healing") + 1 false-positive control (xiaoyi9955) + 7 human faceless/affiliate context accounts.
- Only **two** accounts carry a creator AI label (`aigcLabelType 1`: _keepher1, clothing_findsj, cia_tuballas) and **one** a platform AI label (`aigcLabelType 2`: pinecommerce) among the ~20 videos verified; AI personas with real reach (theamberjai) post **unlabelled**.
- **No verified account combines a fully virtual influencer with TikTok-Shop flags.** The AI + Shop money, where documented, sits in (a) faceless/AI-voiced seller ads (pinecommerce, isAd/isECVideo), (b) low-cost "AI affiliate" product mock-ups in SEA markets (PH), and (c) the supplement "AI doctor" funnel now under lawsuit/press scrutiny with accounts disappearing.
- Every income figure attached to these accounts is **Claimed** (Reddit/YouTube/bio); no dashboard is public.
