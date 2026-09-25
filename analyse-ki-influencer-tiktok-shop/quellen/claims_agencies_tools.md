# Claims: AI-UGC vendors, TikTok Symphony, TikTok Shop agencies, LinkedIn (access date 2026-09-24)

Scope: published case studies / claims from AI video vendors (Arcads, Creatify, MakeUGC, HeyGen, Captions/Mirage, Icon, Topview, Higgsfield, Syllaby, Crayo, AutoShorts, Poppy, Argil, Synthesia, Veed), TikTok's own Symphony material, TikTok Shop agencies/TSPs and LinkedIn. Tags: **Verified** = seen in TikTok data / primary doc; **Claimed** = asserted by source; **Estimated** = my calculation (formula shown).

Method note: WebSearch budget was exhausted after 5 queries; Bing/DDG/Startpage/Mojeek via curl through the proxy either block or truncate multi-word queries (Bing honours only the first token). Remaining work was done with direct WebFetch of vendor pages and NexLev YouTube search/transcripts. LinkedIn profile pages return HTTP 999; only /posts/ URLs render.

Headline finding: **No AI-UGC vendor publishes a TikTok Shop *organic affiliate commission* case study with a dollar figure.** Vendor case studies are (a) paid-ads metrics (ROAS/CPA/CPO/CTR), (b) views-only organic lifts, or (c) unnamed "accounts made $30K/month" marketing copy without evidence. The only concrete AI-affiliate dollar claims come from YouTube coaches (with course/mentorship bias) using Kalodata-style third-party revenue screenshots.

---

## A. AI-content claims (vendor-published, TikTok Shop related)

### A1. Creatify — LAIFE (longevity/supplement brand) — AI avatars on TikTok Shop
- URL: https://creatify.ai/case-study/laife (published 2026-04-22)
- Quotes (Claimed): "$3.89 / Cost per order achieved"; "50 / Ad creatives tested per week (up from 10)"; "After integrating Creatify, they test 200+ videos per month (50 per week)"; "Almost all videos on their TikTok account (@liioo_kko) are Creatify-generated AI UGC."; "LAIFE's product cards (TikTok's organic shopping feature) started generating consistent orders."
- Customer quote: "We like Creatify because the characters look more realistic and we have a wider variety to choose from. Almost all the videos on our TikTok account are made using Creatify."
- Metric type: cost per order (paid; "ad creatives", GMV Max context) + unquantified organic orders. No GMV/revenue/commission number.
- Evidence: none (no dashboard, no screenshots). Bias: vendor-published.
- **Verified via tt_profile.sh (2026-09-24)**: handle is `@liioo.kko` (with dot; `liioo_kko` = not found). followerCount 222, videoCount 68, hearts 1,272, created 2025-10-21, bio "TikTok shop :Laife Health", commerceUser=false, ttSeller=false.
- Plausibility (Estimated): 68 videos on the account over ~11 months (Oct 2025 → Sep 2026) ≈ 6/month, vs. claimed "200+ videos per month" → the 200/month are ad creatives, not organic posts. 222 followers / 1,272 likes = negligible organic reach. Organic-affiliate relevance: **low**; this is a paid-ads case.

### A2. Creatify — Imalent (flashlight brand) — organic TikTok views, AI vs conventional
- URL: https://creatify.ai/case-study/imalent (dated Jul 2, 2024)
- Quotes (Claimed): "a more than sevenfold rise in organic views"; "a conventionally produced video reached 13.9K views, its AI-generated counterpart skyrocketed to 170.3K views"; "even the least viewed AI videos doubled the viewership"; likes 4x, saves 7x, comments 2x; paid: "AI-generated videos, on identical ad budgets, received twice the views"; cost "AIGC videos cost as little as $4 each" vs "$150 to $1,000 per video".
- Metric: views only — no sales/GMV/commission. Evidence: none. Bias: vendor. Handle: not given.

### A3. Creatify — Twist Digital (affiliate marketing agency) — paid ads
- URL: https://creatify.ai/case-study/twist-digital (Dec 19, 2024)
- Quotes (Claimed): CTR "Doubled from 4-5% to 9-10%"; "produces approximately 100 videos per day"; "$30 per video (actor + editor) to just $2"; "$36,000 Video production cost saved per month"; title "Boosts ROAS 4x" (not substantiated in body).
- Metric: CTR/cost; platform not specified; not TikTok Shop. Evidence: none. Bias: vendor.

### A4. MagicUGC blog — "From 0 to $30K: Monetizing TikTok with AI-Generated UGC"
- URL: https://www.magicugc.com/blog/from-0-to-dollar30k-monetizing-tiktok-with-ai-generated-ugc-videos (2025-03-14)
- Quotes (Claimed): "Using AI-generated videos through MagicUGC, TikTok accounts pulled in average monthly revenues of $30K, with some accounts hitting $60K."; "Accounts reached about $20K per month by posting 1–4 times daily." (months 1–2); "around $40K" (months 3–4); "$30K-$60K … with 65% profit margins" (months 5–6); "some reaching over 20 million views and monthly revenues of $30,000, $100,000, or even $200,000."; "Beta users of MagicUGC Boost™ have reported a 275% increase in conversion rates."
- Metric: "revenue" — ambiguous (seller revenue vs affiliate commission not stated). Handles: none. Evidence: none. Bias: vendor marketing copy. Volume driver: 1–4 posts/day. Credibility: very low (no named account, no screenshots, round numbers).

### A5. TikTok Symphony (TikTok-published) — paid-ads case studies with AI creatives
- Symphony Creative Studio announcement, https://ads.tiktok.com/business/en-US/blog/symphony-creative-studio (2025-06-03):
  - Meoky (US drinkware): "achieved a 1.8x increase in purchases and a +13% boost in return on ad spend (ROAS)" using Generate TikTok Ads from product URL. (Claimed, paid ads)
  - Vodafone (stock avatars): "45% lower cost per lead (CPL) than other channels' branded assets"; "24% lower CPL than branded assets within TikTok". (paid, lead-gen, not Shop)
  - VOGGSMEDIA (DE): "doubling conversions and reducing CPA by 50%" via Translate & Dub. (paid)
- Symphony AI tools blog, https://ads.tiktok.com/business/en-US/blog/tiktok-symphony-ai-tools (2025-06-16):
  - American Eagle (Showcase Products): "60% higher traffic return on ad spend (ROAS) compared to business-as-usual assets" (paid). Note: TikAdSuite (secondary) says this used "Showcase Products + Digital Avatar"; TikTok's page only names Showcase Products.
  - YOOX (Image to Video): "15% lower cost per add-to-cart" (paid).
- Aporia LTD (Avatar API): "12.3x increase in creative output, a 19% CTR lift, and a 6.2% ROAS improvement" — **secondary only** (TikAdSuite, https://tikadsuite.com/blog/tiktok-symphony-ai/, updated 2026-09-08, attributes to TikTok); primary TikTok page not located.
- LuisaViaRoma (Symphony avatars, Italy): from WebSearch snippet of https://ads.tiktok.com/business/en/inspiration/luisaviaroma-case-study — "71% click-through rate and an 11% lower CPA", "80% of the brand's clicks were driven through avatars", avatars "70% of the brand's budget in Italy", campaigns from July 2024, 10–13 weeks, 3 generic avatars. Primary page could not be rendered (all locale variants redirect to the case-study hub) → treat as Claimed via snippet; "71% CTR" is almost certainly "+71% CTR". Paid ads.
- Symphony Avatars newsroom (2024-06-17) and Symphony Agent blog (2026-06-22): no case-study numbers.
- **All Symphony numbers are paid-ads metrics. TikTok publishes no organic TikTok Shop / affiliate commission result for AI avatars.** No "AI Cast" material found.

### A6. MakeUGC (makeugc.ai) homepage testimonials
- Eileen Lee (Senior Marketing, Nano Foam): "$19K in ad spend → $69K in total sales with a 3.73x ROAS" (paid ads, platform unspecified). Waynes Reeves: "3X–4X ROAS across campaigns". Jordan Welch: "strong performance … green screen avatars over B-roll" (no number). Evidence: none. Bias: vendor. Not TikTok Shop-specific.

### A7. Arcads (arcads.ai) homepage
- Only app/paid-ads carousels: Glam "Revenue Generated $16K (+195%)", MellowFlow "$10.1K–$32K (+5% to +270%)"; "1 billion views with ads created with arcads"; AI-agent social accounts (@ameliabeautytips +12K followers, @amymorgans +18K, @myiq_com, @holmisthename) — follower/like deltas only. **No TikTok Shop / affiliate / GMV claim published.** /customers, /blog, /case-studies → 404.

### A8. Topview.ai — iLive by SHOPNOW: "+80% Revenue growth in AI video production services", "−50% Labor and production cost". This is an agency's own service revenue, not TikTok Shop sales. No affiliate claims.

### A9. Vendors with **no** TikTok Shop sales/commission claims found (checked 2026-09-24): HeyGen (/customers, /customer-stories: no TikTok/e-com metrics; Yang Mun story = 2.5M IG followers), Captions/Mirage (mirage.app/research; captions.ai/blog: "How a dental student made $100K creating content" — not Shop), Icon.com (explicitly "6 Human UGC ads … (no AI / 100% real)"; revenue logos like "Obvi $100M+" are client company sizes, not results), Higgsfield (no case studies; "4.5M video generations per day"), Syllaby (YouTube 0→50K only), Crayo (no numbers), AutoShorts (none), Argil (blog only, no numbers), Synthesia (/customers 404), Veed (404), Poppy AI (Jason Cooperson "$10.5K from Poppy content", Antek "36X ROAS on Meta" — not TikTok Shop).

### A10. Superscale "AI Generated UGC vs Traditional UGC: Performance Study" (cited by Short Form Nation, videoai.me, etc.)
- URL: https://superscale.ai/learn/ai-vs-traditional-ugc-complete-comparison/ (2026-01-02)
- Quotes (Claimed): "Up to 350% higher engagement rates on TikTok campaigns (18.5% vs. 5.3% for human UGC)"; "2.8x more views and 3.5x more shares"; AI "68% consumer quality approval"; human "81% perceived authenticity rating vs. 63% for AI UGC".
- Methodology: none stated (no sample size, platform, period); many stats are third-party links. No TikTok Shop sales data. Bias: Superscale sells AI UGC (~$2/video). → Not usable as an income benchmark.

---

## B. AI-content claims found via vendor-tool YouTube content (coaches; course bias) — cross-reference claims_youtube.md

### B1. HowEcomWorks — "This AI Is A Cheat-code For TikTok Shop" (Kalodata/KaloClip)
- URL: https://www.youtube.com/watch?v=5UlUqbUKT0s (published 2026-09-11)
- Claim (Claimed, third-party data): a 10-second AI faceless TikTok Shop video for a magnesium complex supplement "generated $21,218 in revenue in just 30 days", "over 1 million views and sold 1,420+ units"; product "$16 per unit. 25% revenue if you sell this product as a TikTok Shop affiliate"; product listing "$2.1 million in revenue … in just the last 30 days"; "the affiliate here took home 25% of this total revenue amount, which is around 4,000 4,200 or something like that."
- Metric: GMV attributed to one video (Kalodata "revenue"); commission = creator's estimate. Estimated check: 25% × $21,218 = $5,305 (his "$4,000–4,200" is lower; Kalodata revenue ≠ net of returns). $21,218 / 1,420 units = $14.94/unit (consistent with $16 price less discounts).
- Evidence: Kalodata video-detail page shown on screen (per narration/description). Affiliate handle: not named. AI: "this one is AI" (Kalodata-listed AI video; faceless, no avatar). Bias: Skillshare classes; affiliate links to Arcads, InVideo, Kalodata.

### B2. tommycetty — "Leaking My $30K/Month AI TikTok Shop Affiliate Strategy"
- URL: https://www.youtube.com/watch?v=qE8oJSYFxYU (published 2026-09-15)
- Quotes (Claimed): "exposing my 30k profit per month Tik Tok shop AI strategy workflow that went down from January 2026 to April 2026"; "my record day of 22K right here in a single day of [GMV]. Next day following was a 10K day"; "On average, it was about 12 to 15 videos per day"; "videos are around a minute and a half to 2 and 1/2 minutes long"; "podcast style with very, very attractive female characters"; "we did multiple six-figure months every single month for this brand"; "average commission rate was 10 to 25% commission" (cologne dupes; brand-name cologne "5% or less"); top videos "3 million 3 million 3 million a million 766,000 900,000" views; one page banned ("character that looked too similar to a famous adult actress").
- Description: "did $30K in profit per month … 12 to 15 videos a day, cologne dupes"; tools: Claude (scripts), ElevenLabs V3 (voice), HeyGen (avatar video).
- Metric: stated "profit", but record day is stated as GMV → ambiguous; "we" includes community members. Evidence: "as you can see" dashboard shown on screen — could not be inspected (watch tool rate-limited); not verifiable. Handle: says he leaks one (banned) page; not named in transcript. Bias: strong — sells Simple Media "AI accelerator" (join.simplemedia.ai).
- Estimated sanity check: $30K commission/month at ~15% avg commission ⇒ ~$200K GMV/month; at 12–15 videos/day (~400/month) ⇒ ~$500 GMV per video. Possible only with repeated multi-million-view hits as claimed.

### B3. Adam Willis — "How an AI Tiktok makes this affiliate $20,000/month in PROFIT"
- URL: https://www.youtube.com/watch?v=p7q9GahGd7Q (published 2026-02-18)
- Quotes (Claimed): "an AI creator made just under $20,000 in commissions with an AI generated video for a product on Tik Tok shop … the brand made over $300,000 in sales"; product "a book called The Only Living Trust … print-on-demand"; "Over the past 30 days, they did $300,000 in revenue"; "they were selling it for about $35 a unit"; affiliate "drove $92,000 in revenue … 20% commission … 20% on $92,000 is $18,000 in 30 days"; script hook "If your name's on the deed, you don't control your house"; also "natural squads has 483,000 followers all AI generated videos … $2 million in sales just on Amazon … $4 million in sales a month" (Rosabella moringa capsules).
- Description: "Gemini (script/image), Veo 3 (B-roll), ElevenLabs (Voice), HeyGen (Avatar), and CapCut … assets for under $100".
- Metric: commission (derived: 20% × $92K GMV). Evidence: on-screen analytics screenshots ("I just want to prove this to you here") — tool not named in transcript (Kalodata-style product/affiliate revenue view); not independently verifiable. Affiliate handle: not named. Bias: sells mentorship (typeform application).
- Note: video is titled "$20,000/month in PROFIT" but body says commissions; AI B-roll + AI voice (faceless "authority" style), not necessarily an avatar.

### B4. Osher — "TikTok Shop + Higgsfield AI" (https://www.youtube.com/watch?v=dpVz6diMb5M, ~May 2026): only "a video that makes me thousands of dollars on TikTok Shop" — no figure, no evidence; sells 1-on-1 mentorship, Higgsfield/Kalodata affiliate links. Not a concrete claim.

---

## C. Human benchmarks (needed for plausibility maths)

### C1. Sohun Sanka (Reacher) — LinkedIn post, affiliate GMV distribution
- URL: https://www.linkedin.com/posts/sohun-sanka_only-16-of-tiktok-shop-affiliates-drive-activity-7401650316624113664-ujjT (≈ Dec 2025; "9 months ago")
- Quotes (Claimed, from 3.3M-creator database): "Only 1.6% of TikTok Shop affiliates drive over $1k in GMV"; tiers: 16% > $1; 4.6% > $100; 2.3% > $500; 1.6% > $1,000; 0.4% > $10,000; 0.09% > $50,000 GMV.
- Period: not stated (reads as cumulative/lifetime GMV per affiliate). Evidence: internal DB, no screenshot. Bias: Reacher sells affiliate-outreach SaaS. **Human benchmark** (all affiliates, AI not separated). Estimated: at ~15% commission, ">$1k GMV" = >$150 commission → ~1.6% of affiliates; ">$10k GMV" (~$1.5k commission) → 0.4%.

### C2. Hamster Garage — "TikTok Shop Affiliate Case Study 2026: Terms & 67% GMV Math"
- URL: https://www.hamstergarage.com/article/tiktok-shop-affiliate-case-study-glossary-benchmarks (2026-06-16)
- Quotes (Claimed): Blissim (FR): "1,000 videos, 7,000 sales, and more than €280,000 in turnover" from "700 samples" (≈ "€400 in revenue per sample shipped"); Divi: "$4.7 million in GMV in 9 months"; Love & Pebble: "1,194% sales increase, 3.2x ROAS"; U.S. avg commission 13.02% (range 5–30%); conversion "3-6%" per affiliate video; "$1M monthly revenue requires 1,000+ videos per month"; "20% of creators typically drive 80% of GMV"; "brands keep an average of 67.3%" of GMV.
- Estimated from Blissim: €280,000 / 1,000 videos = €280 GMV per video; 7 sales per video; €40 AOV; at 13% commission ≈ €36 commission per video.
- Evidence: none shown (aggregated from public case studies). Bias: affiliate-marketing consultancy. **Human benchmark.**

### C3. Top Growth Marketing / Cruva — C Curl & Playboy TikTok Shop case studies
- URL: https://topgrowthmarketing.com/tiktok-shop-case-study/ (2025-12-26)
- Quotes (Claimed): C Curl: GMV $7,906.42, "63 creator assets now live", 9,970 DMs, 10,600 invites, 347 sample requests; Playboy: GMV $14,694.16, 110 videos, 7,555 DMs, 876 sample requests, 259 replies. Organic (pre-amplification).
- Estimated: $125 GMV/video (C Curl), $134 GMV/video (Playboy) in the initial phase. Evidence: Cruva dashboard screenshots. Bias: Cruva sells outreach software. **Human benchmark.**

### C4. Qazi Hamad — LinkedIn (profile blocked, HTTP 999; from WebSearch snippet only)
- URL: https://www.linkedin.com/in/qazihamad/ — snippet: analysis of "an account doing $215K GMV with $170K from affiliates, 4.5M views, and 809 videos".
- Estimated: $266 GMV per video; $47.8 GMV per 1,000 views; affiliates = 79% of GMV. Date unknown. Evidence: not viewable. **Human benchmark (unverified snippet).**

### C5. Kelly Landsman — LinkedIn headline "UGC Creator & TikTok Shop Affiliate … $800K+ GMV in Under a Year" (https://www.linkedin.com/in/kelly-landsman/, profile blocked). No volume drivers → excluded from structured list.

### C6. Creatify Agency (creatify-agency.com — TSP, human creators, not the Creatify.ai tool)
- Quotes (Claimed): "$1.3BN annual managed GMV"; "$700M+ in GMV Max"; "7.2x avg brand ROI"; "6 days first sale"; "3x GMV in 60 days" (top-5 beauty brand); "$2.4M first quarter" (skincare); "0 → 50K units/month"; "$2M to $15M" in 45 days; "47K orders in 9 days"; "Typically 50-200+ creators per campaign"; "20,000+ creators". Testimonial handles: @nutrl_official, @glow.rx, @liq.electrolyte, @oli.soda, @magicspn, @popp.co, @hydra.dtc, @bloom.beverage (brands, not affiliates). "No mention of AI-generated video content."
- Evidence: charts/testimonials on own site, no third-party. Bias: agency. **Human benchmark (agency scale, no per-video drivers).**

### C7. LeadsPro agency (2025-11-30): anonymous beauty brand "500% month-over-month sales growth", "200,000+ video views within a week" — no GMV, no video count, no AI → excluded.

---

## D. Bottom line for the report
1. Vendor case studies (Creatify, Symphony, MakeUGC) prove only **paid-ads efficiency** (CPO $3.89, ROAS +13%/+60%, CTR ×2). None gives organic TikTok Shop affiliate commission with an AI account.
2. The only AI-specific dollar claims with any evidence are **Kalodata-style screenshots** in coach videos: one 10-s faceless AI video ≈ $21K GMV/30 d (≈$4–5K commission); one AI-B-roll affiliate ≈ $92K GMV/30 d (≈$18K commission at 20%). Both are single outliers on high-margin products (supplement, POD book), not account-level averages.
3. Human benchmarks: 1.6% of all affiliates ever exceed $1K GMV (Reacher); typical organic yield ≈ $125–$280 GMV per video (Cruva, Blissim); $30K commission/month at 15% needs ≈ $200K GMV/month ≈ 400+ videos/month at those yields — matching tommycetty's claimed 12–15 videos/day but only if multiple multi-million-view videos occur.
