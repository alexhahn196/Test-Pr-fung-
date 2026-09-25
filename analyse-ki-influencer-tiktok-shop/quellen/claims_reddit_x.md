# Income / commission / GMV claims: TikTok Shop affiliate with AI / faceless content (Reddit, X, Skool)

Access date for all sources: 2026-09-24. Analyst stance: sceptical due diligence. Tag legend: **Claimed** = asserted by the claimant, no primary data seen; **Verified** = seen in TikTok/primary data (none in this file — every number below is self-reported); **Estimated** = my own arithmetic with the formula shown.

## Method and limitations (read first)

- WebSearch budget of this session was exhausted before this task started (200/200), so Google-style `site:reddit.com` / `site:x.com` queries could not be run. Substitutes used:
  - Cached Reddit search dumps already in `research/reddit/*.json` (8 keyword searches, 564 unique submissions, 2024-01 to 2026-09-24) plus fresh Pullpush submission searches (12 queries, 610 unique submissions). Filtered by regex for "TikTok Shop / TTS" AND a money/volume number, then read ~45 submissions in full.
  - Comment threads: Pullpush comment API (`api.pullpush.io/reddit/search/comment/?link_id=`) — worked for 24 threads (~530 comments read), then rate-limited (HTTP 429) for a further 12 threads (1uf1zxj "Be honest… is anyone pulling a decent income", 1umpzi8 "$10k+/month what got you there", 1r7h6jy, 1sok5cr, 1w7nihc, 1pbk5us, 1qegd4o, 1ufm37l …). reddit.com / old.reddit.com return 403 to this container and WebFetch refuses old.reddit.com, so those comment sections are **not covered** (submission bodies are).
  - X/Twitter: no working search route (Bing, DuckDuckGo, Brave, Startpage, Yandex, Mojeek all returned captcha/blocks or junk). Only tweets whose IDs were quoted inside Reddit posts could be pulled via the public syndication endpoint (`cdn.syndication.twimg.com/tweet-result?id=`). X coverage is therefore thin (4 tweets, 1 relevant).
  - Skool: `skool.com/discovery?q=tiktok shop` (public __NEXT_DATA__) + 4 community "about" pages. Whop/Discord: nothing indexable reached.
- Reddit realities that matter for weighting: many "success" posts in r/TikTokshop, r/passive_income, r/SideHustleGold are thinly disguised tool/course ads (Moras.ai, Virlo, ShopReelAI, TlkAlyzer, Orchardrun, ttsmastery.com, aiyoutube.sell.app). Where the same tool is name-dropped as the "turning point", I flag `bias = tool promo (probable)`. Genuine-looking negative reports are typically score 1–20, no product mentioned.
- No dashboard screenshot could be inspected (image hosts not fetched). "screenshot claimed" means the post embeds an image (preview.redd.it) that I could not verify.

---

## A. Claims involving AI-generated / faceless / mass-produced content

### A1. u/SmoothConnection1670 — "faceless TikTok Shop farms", $18k–25k/month commissions (Claimed)
- URLs: https://www.reddit.com/r/TikTokshop/comments/1turwwi/ (2026-06-02, score 2, 2 comments); cross-posts https://www.reddit.com/r/SideProject/comments/1turoe7/ and https://www.reddit.com/r/SideProject/comments/1turgw7/ (same day)
- Quotes: "Now, 4 months later, I'm on track for around $21k in clean commissions this month — working only 2-3 hours a day. No face, no inventory, no customer support. Just automated content with link in bio." / "I'm consistently hitting $18k–$25k/m in clean commissions." / "The first 30-45 days were brutal. Lost money on bad tests, videos flopped."
- Amount: $21k (this month), $18k–25k/month. Period: month. Metric: **commission** ("clean commissions"). 
- Evidence: none.
- AI usage: repurposing pipeline "scrape viral videos → transcribe → rewrite → voiceover → edit → post"; stack: n8n + TikTok scrapers, "Orchardrun" transcription API, Claude 3.5 / GPT-4o rewrite ("minimal changes"), ElevenLabs cloned voices, Captions.ai Pro + CapCut batch, scheduler. i.e. re-voiced copies of other creators' viral videos (plagiarism/"unoriginal content" risk).
- Bias: **tool promo (probable)** — third post is a stack list whose only non-mainstream item is Orchardrun (with a half-deleted sentence "in one month and it still runs smoothly. Best price/performance…"); the single substantive comment asks "what tool you use to transcribe high volumes of audio". Triple cross-post, new-ish account.
- Handles: none given. Volume drivers: niches dog joint supplements, anti-aging collagen, belly fat, menopause; "a few minutes per video once automated"; no views/videos-per-day stated. Note "link in bio" is not how TikTok Shop affiliate attribution works (product tags/showcase), which is a red flag for authenticity.

### A2. Moras.ai ("Bella", u/No_Budget_9771) — 300 affiliates, $1.5M GMV in 2 months; "0 to $100,000 GMV in 30 days" (Claimed, vendor)
- URL: https://www.reddit.com/r/TikTokshop/comments/1tkbv2x/ (2026-05-22, score 7, 16+ comments read)
- Quotes: "300+ affiliates made $1.5M GMV in just 2 months. Some went from 0 to $100,000 GMV in 30 days, while others hit $10k overnight. 80% of users make sales within 1 week." / "Before finding us … Even on a good day, they only make $50."
- Amount: $1.5M GMV aggregate (2 months, 300+ affiliates → Estimated average $2,500 GMV per affiliate per month = at ~10–15% commission ≈ $250–375/month per affiliate); $100k GMV/30 days (unnamed best case). Metric: **GMV**.
- Evidence: none. Comments: "Breaking rule #1" (s=5), "Ai slop garbage post" (s=1); vendor says "We charge low monthly fee + partly commissions", US creators only.
- AI usage: yes — Moras generates "high-converting shoppable videos" automatically for products the affiliate never received ("make videos for products even if they can't get free samples").
- Bias: **vendor** (AMA is an ad).

### A3. u/West_Competition_72 — $10k GMV / ~$1,000 commission last month with Moras + ChatGPT (Claimed)
- URL: https://www.reddit.com/r/SideHustleGold/comments/1sok5cr/ (2026-04-18, score 0, 6 comments — comments not retrievable)
- Quote: "I hit $10k in GMV last month, netting about $1,000 in commissions. It's not Ferrari money, but the ROI on my time is insane." / before: "doing the work of a whole production house just to get 300 views and zero sales" / "went from grinding 16 hours a week on manual edits to maybe 6 or 8 hours total" / warning "Don't go 100% bot: if your page … becomes pure AI trash, the algorithm will eventually bury you."
- Amount: $10k GMV → $1,000 commission (implied 10%). Period: month. Metric: GMV + commission (both given). Evidence: none.
- AI usage: "a tool called moras to handle the actual grunt work like filming and editing" + ChatGPT scripts.
- Bias: **tool promo (probable)** — same tool as A2, "happy to help", score 0.

### A4. u/Wrong-Inspection343 — "$2k/month"; ~$50k GMV in 3 months from AI-made videos (Claimed)
- URL: https://www.reddit.com/r/passive_income/comments/1u9s0zn/ (2026-06-19, score 0, 2 comments)
- Quotes: "I have around 8k followers on TikTok … Got $50 for the first month." → "my views tanked and 0 sale. I panicked and spent $80 on a group" → "found a program … They created AI videos with attractive hooks, selling angles, and captions. I stopped overthinking and just posted 3-5 times a day." → "Initially, videos sat around 1k views with 0 sales. But on day 5 of posting, I got my first sale! It was a bed frame." → "one video suddenly went viral: 100k views and almost $10k in GMV … I've had 4 viral videos and hit nearly $50k GMV within 3 months." Title: "now makes me $2k/month".
- Amount: ~$50k GMV / 3 months; $2k/month (title). Metric: GMV (body) vs ambiguous "$2k/month" (title; if commission, that is ~4% of GMV — inconsistent unless commissions were very low). Evidence: none. Top comment: "Fake fake fake." (s=10).
- Volume drivers: 3–5 posts/day; ~1k views/video before first sale; first sale on day 5; 100k views → ~$10k GMV (Estimated GPM ≈ $100 per 1,000 views — 5–20x the GPM range seen elsewhere; implausible for a bed frame without further data).
- AI usage: fully AI-generated videos supplied by "a program"; "soon I'll even be using my own AI avatar".
- Bias: **vendor/astroturf (probable)** — same account posted "[Hiring] US TikTok creators, up to $500/week, mobile app" in r/techugc (2026-08-16), i.e. a recruiter for an app, not a hobbyist.

### A5. u/Bulky-Resolution6265 — seller: "$3k/Month to $27k/Month" via AI creative flooding across 15 accounts (Claimed)
- URL: https://www.reddit.com/r/FacebookAds/comments/1q1l1ua/ (2026-01-02, score 0, 4 comments: "stop using ChatGPT and post like a human being", "Thanks chatgpt")
- Quotes (month-by-month): "Month 1 (Creator Model): $3,200 revenue – 7 creators, 19 videos posted, Average CPV $180" / "Month 2: $18,700 revenue – 47 videos posted (31 AI-generated, 16 creator), AI content converted 2.3x better" / "Month 3 (Full AI System): $67,400 revenue – 156 videos posted across 12 accounts" / "Month 4 (Current): $127,300 revenue (on track) – 203 videos posted across 15 accounts … Average production cost per video: $2.70". Single video: "1 hit 1.3M views and drove $11,400 in sales" (Estimated GPM ≈ $8.8/1k views). Cluster: "Video hits 847k views … 8 of those 12 videos break 100k views. Total sales from that cluster: $43,200".
- Metric: **revenue/GMV of own shop** (seller, not affiliate commission). Period: month. Evidence: none.
- AI usage: ChatGPT script variants, HeyGen/Synthesia avatars or hands-only product demos + voiceover, Runway; "10-15 burner accounts … Each account posts 2-3x per week maximum"; expects TikTok crackdown in "6-8 months".
- Bias: "Building a software tool to automate the entire loop"; title ($27k) contradicts body ($127k) → **low credibility**, reads as LLM-generated marketing copy.

### A6. u/Life-Programmer7808 — seller: AI POV-UGC doing "$200–$300+/day in revenue, purely organic" (Claimed)
- URL: https://www.reddit.com/r/AI_ecommerce/comments/1sl050c/ (2026-04-14, score 1, 0 comments)
- Quotes: "$200–$300+/day in revenue, purely organic. Some videos hitting 100K+ views, zero ad spend." / "I cut 30–50 affiliates who were either making garbage content or just taking free product and ghosting" / "Production cost is practically nothing compared to paying $150–$300 per UGC creator video."
- Metric: **revenue** (seller). Period: per day. Evidence: two embedded sample videos, no dashboard.
- AI usage: "POV-style UGC videos entirely with AI — programmatically using prompts".
- Bias: unclear (no tool named); subreddit r/AI_ecommerce is promo-heavy.

### A7. u/Available-Benefit-43 — seller running AI UGC as ads: "255k sessions, $588k revenue, 2.5% CVR" (Claimed, screenshot claimed)
- URL: https://www.reddit.com/r/dropshipping/comments/1t3ig8b/ (2026-05-04, score 1, 5 comments: "nah that's cap")
- Quote: "Attached my workflow + TikTok shop dashboard. 255k sessions, $588k revenue, 2.5% CVR." / "went from testing 2-3 creatives a week to pumping out 15-20 variations in a single afternoon".
- Metric: revenue (seller, **paid ads**, beauty/skincare). Period: not stated. Evidence: image embedded (not inspectable). Bias: probable tool promo (tool unnamed). Not organic affiliate economics.

### A8. u/That_Contribution750 — "$40k–$80k/month AI TikTok Shop affiliate pages are built exactly like this" (Claimed, no substantiation)
- URL: https://www.reddit.com/r/dropshipping/comments/1q85qqd/ (2026-01-09, video post, score 1, 0 comments)
- Quote: "one discount-style hook that feels like news / one short talking-head clip / reposted across multiple AI faces / same script, same urgency, same product / ai handles the avatars and posting volume … this is how faceless pages turn price drops into commissions at scale … i broke down the exact setup … If you need it let me know".
- Amount: $40k–80k/month (third-party pages, unnamed). Metric: ambiguous. Evidence: none. Bias: **lead-gen** ("If you need it let me know").

### A9. u/idoetsyforliving — seller: "I use mainly AI videos on my main shop posting 5-7 times a day and that bring 20-30k rev" (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1w0pwo5/ (2026-08-28, score 1, 8 comments)
- Quotes: "I have a store that makes 20-30k a month." / "I use mainly AI videos on my main shop posting 5-7 times a day and that bring 20-30k rev (not POD)" / "sending 1 tshirt is around $15 to affiliates and they post 2-3 times and call it a day. For $15 I get 100x 8s videos".
- Metric: revenue (seller). Period: month. Evidence: none. Bias: none obvious (asks for POD advice). Commenter u/Connor736: "My cost per ai video is way higher than yours" (i.e. $0.15/video claim disputed). Commenter u/Emotional_Fondant452: "Have done over $3M on the app" (seller, no detail).
- AI usage: AI-generated clips of "girls wearing tees", visual hooks only, no explanation.

### A10. u/Top-College-5008 — "Went from 2 sales a week to 40+" after switching to faceless AI videos (Claimed, no $)
- URL: https://www.reddit.com/r/SideHustleGold/comments/1t4ndy9/ (2026-05-05, score 4, 7 comments)
- Quote: "I started making faceless videos using AI which I didn't think would work as well as a face-cam but they actually outperform mine on most products … I'm not selling anything".
- Amount: 2 → 40+ sales/week (no price/commission). Metric: order count. Evidence: none. Bias: "started using a website to help me analyse product performance" (unnamed) — mild.

### A11. u/Dry_Alfalfa5405 — "Posted 15 videos in the last 2 weeks … starting to see some commission" (Claimed, no $)
- URL: https://www.reddit.com/r/smallbusiness/comments/1r1d4zc/ (2026-02-10, score 1)
- AI usage: AI product videos generated from supplier photos (tool unnamed). Bias: soft tool promo. No amounts.

### A12. u/sunsetgalaxy — guide "Make $30-50 daily by uploading just 1 TikTok video" (Claimed formula, not own results)
- URLs: https://www.reddit.com/r/passive_income/comments/1qu3vb7/ (2026-02-02, score 779, 65 comments) and repost https://www.reddit.com/r/passive_income/comments/1syv0bv/ (2026-04-29, score 0)
- Quotes: "Beginners often make 1 to 3 sales per day, around $10 to $30. After a few weeks, this can grow into $300 to $1,000 per month." (repost: "$100 to $1,000") / "If the product price is $25 and the commission is 40 percent, that is $10 per sale. One viral video with 50 sales per day equals about $500 per day. This is not consistent, but it is possible." / "even a new account without followers will get a few hundred to a few thousand views, which will end up with 1-3 sales per day" / "ideal price range is between $10 and $40, commission should be between 20 and 60 percent" / "Post 1 to 2 videos per day. Test one product with 5 to 10 different videos."
- Metric: commission (hypothetical). Evidence: none; not the author's own numbers.
- AI usage: recommends reposting sellers' approved promo videos, or AI videos via CapCut/Pika/Runway, Leonardo + Kling, Sora, Nano Banana; repost pushes "aiyoutube.sell.app (X-Tuber)".
- Bias: **serial guide-spammer** (links own "make 100k monthly with only 28$" post). Top comments: "everywhere says to turn on affiliates you have to have at least 5k followers" (s=32), "Fuck this spam shit" (s=36), "AI slop" (s=28), "its 0% passive" (s=17). No commenter reported results.

### A13. u/lucienbaba — "AI 'slop' is actually making money" (aggregation of X claims) + strong negative replies
- URL: https://www.reddit.com/r/passive_income/comments/1thv6m5/ (2026-05-19, score 39, 46 comments)
- Relayed X claim (fetched via syndication): **@robiartec**, https://x.com/robiartec/status/2056396829101527202 (2026-05-18, 273 likes): "This Japanese guy manages 10 social media accounts automatically with Claude Code and generates over $20,000/month through affiliate marketing." — Reddit post adds the offers are "affiliate tools, Amazon products, TikTok Shop products, SaaS tools". Metric: ambiguous (revenue/commission), period month, evidence: video clip only, subject unnamed → **not verifiable**.
- Other relayed tweets are not TikTok Shop: @w1nklerr ($100k/9 months faceless YouTube; debunked in-thread by u/Cute_Specific_1605: "dashboard also shows +29k subscriber … channel … shows 9k total subscribers. Garbage post full of lies"), @VadimStrizheus ($10k/month clipping), @DeRonin_ (Creatify Agent "$0.95" per AI ad vs "$500-800" creator UGC — cost claim, no income).
- Negative first-hand reports in comments: u/sindhichhokro "Tested those waters for 6 months with negative returns. Not worth it. Went as far as creating my own engine in python to mass produce clips and videos for 5 different niches. Nothing worked."; u/moscowramada (runs faceless YT) "it costs money to generate video and the cost can easily surpass the profit if you're not making winners … right out of the gate"; u/jay_0804 "most of it still fails, like 80 percent of clips get no traction"; u/Goldarr85 "I'm going to need some hard numbers" (s=38).
- Bias: OP mentions PixVerse in every workflow → probable PixVerse affiliate.

### A14. u/KING123767 — "nobody scrolling actually cares that your video is ai" (Claimed, no $)
- URL: https://www.reddit.com/r/passive_income/comments/1w7nihc/ (2026-09-05, score 1)
- Quote: "Been doing tiktok shop affiliate for about a year … Ive got clips doing decent numbers where the comments are just people arguing about the product. Not one person has ever said anything about it being ai." / "ai just means you find that out 20 times a day instead of twice a week." / "happy to help if anyones stuck".
- No amounts. Volume: implies ~20 AI posts/day. Bias: lead-gen phrasing.

### A15. u/SnooSuggestions301 (comment) — "Start doing ai bottom of funnel. I made $1200 this month nothing crazy" (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1vvqaa2/ (comment 2026-08-26)
- Also: "bottom of funnel … converts way better than top of funnel"; "having ad authorization on your posts" and avoiding listings with "1000+ people" matter more than content quality.
- Amount: $1,200/month. Metric: ambiguous (likely commission). Evidence: none. AI: yes (AI BOF videos). Bias: none visible.

### A16. u/joshmon4 — AI spokesperson: faceless affiliate attempt failed, pivoted to $25–40 clips for Etsy sellers (Claimed, negative for affiliate model)
- URL: https://www.reddit.com/r/SideHustleGold/comments/1uy88zb/ (2026-07-16, score 7)
- Quotes: "build a faceless product review account and try to monetize through whatever ad revenue or affiliate thing I could stack on it. I posted daily for five weeks. TikTok's creator payout thing paid me like four bucks. Brutal." / service income: "Last month hit four hundred eighty two … Usual months land around three hundred fifty to four hundred." / "past twenty seconds her face got weird and creepy. So that was my hard limit".
- Metric: revenue from service (not affiliate). AI: APOB AI character + TTS + CapCut. Evidence: none. Bias: none.

### A17. u/DesperatePresence630 — ShopReelAI 4-day test: 500–1,200 views/video, no sales reported (Claimed; affiliate review)
- URL: https://www.reddit.com/r/Bloggers/comments/1p80o00/ (2025-11-27)
- Quotes: "After about 4 days of posting: multiple videos reached 500–1,200 views, a few hovered around 200–300, some flopped … No huge viral hits yet" / "It let me post 10–15 videos a day without burnout" / "For TikTok Shop specifically, the successful accounts usually post 10–20 videos a day."
- Metric: views only; no revenue. AI: full auto tool (script, stock/UGC snippets, AI voice, auto-post). Bias: **affiliate review** (bonus link).

### A18. k2 lab (relayed by u/Dramatic_Spirit_8436) — "70% of beta testers made their first sale within the first week. one user hit $10k gmv in her first month" (Claimed, vendor via proxy)
- URL: https://www.reddit.com/r/Entrepreneurs/comments/1snwa7t/ (2026-04-17, score 1)
- Metric: GMV; period: first month. Evidence: none ("startup metrics … from a company thats fundraising"). AI: agent does research/scripts/editing/compliance/publishing; human still records. Bias: promotional post (also plugs "verdent").

### A19. Skool "Ai Influencer Network" (Zandela, 735 members, $37/month) — "Earn via AI TikTok Shop … 100% Faceless" (course marketing, no numbers)
- URL: https://www.skool.com/aiinfluencernetwork/about
- Only numeric testimonial: "I even hit 1,000 followers on TikTok in less than a month using Zandela methods." No income figure. Bias: course.
- Related: Skool "TikTok Shop AI Pro" (Jonny, 48 members, $49/mo, Spanish; https://www.skool.com/tiktokshopaipro/about) — no income claims at all.

### A20. X @DeRonin_ — cost benchmark only: "2026: $0.95. Creatify Agent. $19/month" vs "2024: $500-800" per creator UGC video
- URL: https://x.com/DeRonin_/status/2056452720660283733 (2026-05-18, 55 likes). Not an income claim; relevant to unit economics only (quotes Creatify launch tweet).

---

## B. Human benchmarks (needed to plausibilise the AI claims)

### H1. u/Gold-Management-9510 — "$500 in sales" in week 1, organic, 2–3 products (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1vwz2m8/ (2026-08-24, score 1)
- Quote: "Week 1 as a TikTok Shop affiliate: $500 in sales, zero paid ads, just organic content." / "Let GPM (GMV per thousand views) tell me which products to push harder". Metric: **GMV**. No commission %, views or post count given. Evidence: none. Bias: none. Reply (u/epichike): slideshow feature "randomly available", not unlockable.

### H2. u/nonamenoshameso — 1.5 years, "maybe $50 a month", 3–5 videos/day, 1.5k–10k views (Claimed, negative)
- URL: https://www.reddit.com/r/TikTokshop/comments/1vvqaa2/ (2026-08-22, 43 comments)
- Quotes: "Been a TTS affiliate for 1 1/2 years. Make maybe $50 a month." / "I post everyday 3-5 times a day. My views are anywhere from 1,500-10k with an outlier video hitting 20-50k but that's rare" / "I'll make maybe 1-10 sales on a product over a span of two months" / product filter: "<20k sold, in season, at least 10% commission"; pays for a community, used Kalodata and Daily Virals, replicated viral videos "and it still didn't do well".
- Estimated: 4 posts/day × 30 × ~4k views ≈ 480k views/month for ~$50 commission → GPM(commission) ≈ $0.10 per 1,000 views.
- Same thread, u/nkelly1101: "I've been doing TTS for 3 years and I'm in the same boat. I've tried posting 10 videos a day … I also had over 20,000 followers when I started TTS … my videos dont convert." u/Sea_Internal5816: "I went live and sold 2 products. Ive never had a video sale though." u/PrizeConcentrate73: "same experience".
- Seller counter-benchmark in same thread, u/portland83 (live selling own inventory): "I make 15k-35k a month … 24k with a total of 41 hours live last month", started with "$700".

### H3. u/Notyourchinita (TikTok @ihatsabuuty "Heav | TTS finds") — "$250 per week", 10 videos/day Mon–Fri (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1r1mf63/ (2026-02-11)
- Quotes: "I consistently post 10 videos per day Monday thru Friday … I'm very grateful to make $250 consistently every week" / top sellers: watercolor mess-free painting book, bilingual card reader, "BBL" sweats (low ticket) / 1 year, serious since Oct 2025.
- Estimated: ~200 videos/month → ~$1,000/month → ~$5 per video. Metric: ambiguous (likely commission). Evidence: none. Bias: none.
- Reply u/Riialk (2026-05-07): "Barely making $200 a week currently which I was making $300-500 a day before!" (decline attributed to ad-spend favouritism).

### H4. u/Wildcard-01 — "$12,000 dollars in commission" in ~6 months, "Have to post at least 10 a day" (Claimed)
- URL: https://www.reddit.com/r/passive_income/comments/1u3p7mh/ (2026-06-12, score 11, 33 comments)
- Quotes: "I started like 6 months ago and I'm not even good behind the camera and I've already made like $12,000 dollars in commission." / "Have to post atleast 10 a day … I use Kalodata … I just copy what the winning videos are doing" / "Kalodata and Claude Ai stack".
- Metric: commission, ~6 months total (Estimated ≈ $2k/month). Evidence: none. Bias: none obvious (does not sell). Same thread, u/Silent_Concentrate97: "been doing it for a year now, I average $200 a month in 'normal' commissions … frustrating to see 'coaches' claiming to make 10k 50k revenue per month" — admits gaming TikTok creator challenges by buying own products from an alt account and cancelling after the reward ("$209"). u/Ok_Rest9763: "I've made maybe a couple hundred bucks".

### H5. u/Fun-Basil4951 — "$2300 in the first 8 days", "$150–250 a week at first, then $700–2k weeks" (Claimed; Virlo promo)
- URL: https://www.reddit.com/r/TikTokMonetizing/comments/1sth76g/ (2026-04-23, score 1)
- Metric: ambiguous ("you earn commission" model described). Evidence: none. Tools: Virlo + Claude/ChatGPT + CapCut. Bias: **tool promo** — commenters: "The $2300 in 8 days claim with a specific tool mention (virlo) embedded in the 'strategy' is the promo tell", "Wow nice virlo ad bro."

### H6. u/Carl_Frochs_Chin (owner of r/tiktokshopsaffiliates) — "£1,400/$1,883 in 7 days", "consistently £10,000+ per month" (Claimed; sells $5 course ttsmastery.com)
- URLs: https://www.reddit.com/r/tiktokshopsaffiliates/comments/1qeh72v/ and https://www.reddit.com/r/tiktokshopsaffiliates/comments/1qegd4o/ (2026-01-16)
- Quotes: "I started small, £100 to £200 weeks in the beginning. Then it grew to £500 to £1,500 per week. Now I consistently make £10,000+ per month using my 'viral piggyback' system." / "Real results from people I've taught: $10,000+ first month. $500-$750 first week. Some went viral day 3." / "Trick to grow your and get Tiktok shop approved within a day … outside the US/UK" (i.e. account workaround).
- Metric: ambiguous (he says "earnings"). Evidence: claims to post earnings screenshots in his sub (not retrievable). Bias: **course seller**.

### H7. Chris Johnston (u/Double_Potato8151, TikTok @iamchrisjohnston) — "$1,000-2,000/day in commissions", "$20,000+" frozen after ban (Claimed; screenshots claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1oxv3z5/ (2025-11-15, score 9, 37 comments)
- Quotes: "May-June 2025: Became #1 affiliate for the brand [Meraki Blue methylene blue]. Earning $1,000-2,000/day in commissions. Achieved Platinum seller status." / "60+ videos created for this single product … Dedicated account" / "$20,000+ in unpaid commissions" / banned 2025-07-09 for "Trade of Regulated Goods". Resolution 2025-11-17: "The situation was resolved by Reddit TikTok Support today! They got access to my account and I was able to withdraw the money!"
- Metric: commission, per day. Evidence: violation screenshots claimed; dashboard inaccessible. Bias: none. Volume drivers: single supplement product, 60+ videos, lives.

### H8. u/TopOutlandishness317 (TikTok @officialwellnessvault) — "Over $10,000 in commissions pending, hundreds of fulfilled orders", banned (methylene blue) (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1ricbg4/ (2026-03-01, score 11, 28 comments) (+4 near-duplicate posts 2025-11-29)
- Metric: commission (pending). Evidence: none. Comments: u/Kind-Banana-3776 same; u/Old_Teach_9951 "they need to pay me 3.200€ too since June"; u/No_Championship_5720 "they owe me $5000 in rewards".

### H9. u/Admirable-Actuary227 — "20k GMV in my first month with TikTok Shop Affiliate, but the account was then permanently restricted" (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1viw6vz/ (2026-08-08). Second account (grown organically to 1,000 followers) flagged "high-risk" and blocked; uses real ID. Metric: GMV, first month. Evidence: none.

### H10. u/AnyStatistician2875 — "$1,400 of my SETTLED affiliate commission" withheld over "account association" (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1vl69rk/ (2026-08-11). Comments: u/Jumpy_Ad4495 "$1000 of mine", u/akaps36 "about the same amount", u/OkPsychology8056 "Got $3000 frozen".

### H11. u/Professional-Phone44 — 3 years, "just crossed over $100,000 in GMV"; "$20 to if I'm lucky $50 in a day in commissions" (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1ufm37l/ (2026-06-25)
- Quotes: "over these three years … I recently just crossed over $100,000 in GMV" / "in the past two months I had a big month that was above $10K in GMV" / "a gaming headset of maybe had like six sales … a book that I've made 20 sales with in one video" / "I'm tired of only making $20 to if I'm lucky $50 in a day in commissions". Estimated: $100k GMV over ~36 months ≈ $2.8k GMV/month ≈ $300–400/month commission at 10–15%.

### H12. u/QuickRevenue6534 (brand owner, headwraps) — "$400,000 in sales" Jan 2025–Jan 2026; tagged affiliate video stalled at ~800 views vs 10x untagged (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1ugrszw/ (2026-06-27, score 22, 52 comments)
- Quotes: "between January 2025 and January 2026 we did close to $400,000 in sales" / "one video with our TikTok Shop product tagged … stalled at around 800 views. Then … exact same product, but without tagging it … roughly 10 times more views" / GMV Max "spend upwards of $4000 a month" / flat-rate "$200 to post organically to 60k+ engaged followers" / "4.6/5 with over 33k units sold".
- Comments: u/RAL1111 "I was a top affiliate with 100m views and over $1m gmv and i can absolutely tell you they ended organic reach and made it pay for play … stopped doing affiliate after they banned my mega viral account" / u/Legal_Entertainer991 "product tagged videos … 10 views to 1000 views respectively" / u/Agile-Development-88 "Shoppable content gets 50 views" / u/Less-Marionberry-291: tagged carousels less throttled ("French market"). Relevance: any AI affiliate model must assume suppressed organic reach on tagged posts post-Jan 2026 (Claimed pattern, not proven).

### H13. u/sfcoolgirl (brand, women's probiotic $25) — "~50 samples … exactly 2 sales. Most affiliate videos are sitting at 0 views" (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1r7h6jy/ (2026-02-17, score 10, 43 comments — not retrievable). "Maybe 5-10% of creators make good content."

### H14. u/Consistent_Sink_2896 (apparel brand) — "56 orders out to affiliates … 15% commission … total shop sales of 75 and 10 of those were from affiliates" (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1rundke/ (2026-03-15). Brand sells 500–2,000 shirts/month on Shopify.

### H15. u/FancyCount7546 (tote-bag seller) — "highest … around $3k/month in revenue … while running GMV Max ads … without ads, usually under $1k/month"; 1 video/day; 50 samples sent (Claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1umpzi8/ (2026-07-03, score 16, 36 comments — not retrievable).

### H16. u/DirtyReseller (seller) — "$33k GMV in one week"; GMV Max "$1,500–$2,000 a week on ads … For every dollar I spent, I made $6 back"; "660 orders, ~$11k" from one boosted video (Claimed; screenshot claimed)
- URL: https://www.reddit.com/r/TikTokshop/comments/1pbk5us/ (2025-12-01, score 17). Bias: probable profit-tracking-tool promo.

### H17. u/ContractFast2465 (seller) — "$1M GMV on TikTok Shop last month… and still ended up in a loss"; "My ROI in gmv max is 6" (Claimed)
- URL: https://www.reddit.com/r/TikTokShopSellersClub/comments/1p2t337/ (2025-11-21, score 9). Comment u/TurbulentGuide4445: "No one doing big GMVs that I know are profitable, they use TikTok shop as top of funnel".

### H18. u/Professional_Tone210 — fee arithmetic (seller side): "$20K GMV … Referral fees -$1,200 … Affiliate commissions (15%) -$3,000 … Real net profit ~$7,010 (35% margin)" (Claimed model)
- URL: https://www.reddit.com/r/passive_income/comments/1t1rx2k/ (2026-05-02, cross-posted to 6 subs). Useful for GMV→net translation.

### H19. u/Galbatorix_69 — views→sales ratio: "4.8k views and 6 sales, then 6.2k views and 9 sales, then 5.4k views and 7 sales" after 3 months "stuck at 280-380 views" (Claimed; TlkAlyzer promo)
- URL: https://www.reddit.com/r/TikTokshop/comments/1pxs6fd/ (2025-12-28). Estimated ≈ 1.3 orders per 1,000 views (cleaning spray). Bias: tool promo ("not affiliated" but classic pattern).

### H20. Skool "Affiliate Academy 2.0" (Josh Adkins, 139 members, $250/month) — testimonial "over £74,000 in my first year, with £1,000+ days and nearly £16,000 in my best month" (Craig Dean) (Claimed; course)
- URL: https://www.skool.com/affiliate-academy/about. Headline "Learn How To Make £10k+/Mo With TikTok Shop Affiliate"; includes "Free AI Softwares (hookforge.ai & breakwave.ai)". Claire Viner: "increased my earning by 6x". Metric: ambiguous. Bias: course.

### H21. Skool "The Affiliate Fastlane" (John Scalia, 34 members, $249/month) — "$3M+ in sales and 200M+ views"; student "$10K+ months" after one year (Claimed; course)
- URL: https://www.skool.com/theaffiliatefastlane/about. "Students inside are going from $0 to their first sales within a week, and some are already hitting $10K+ months." Estimated from headline: $3M GMV / 200M views ≈ $15 GMV per 1,000 views (GPM). Metric: GMV ("sales"). Bias: course (also sold as "TikTok Shop Affiliate Blueprint" on r/coursesfornow).

### H22. Spring-2026 ban-wave compilation (u/future_flora, r/TikTokShopAffiliate) — "blackfridaybrian: got banned today doing bottom of funnel content. 2.8 million gmv was worth it"; "sherishares455: commission is currently frozen for 60 days"; multiple "bought accounts being banned", "backup … banned for impersonation" (Claimed)
- URL: https://www.reddit.com/r/TikTokShopAffiliate/comments/1sjw8xg/ (2026-04-13). Relevance: multi-account/bought-account strategies (which AI farms rely on) were the ones hit; retroactive violations on old videos.

### H23. u/UnableLeadership2326 — paid "$2,500 … plus a yearly $500 maintenance fee" for Media Labs community; retainers only for high-GMV affiliates (Claimed)
- URL: https://www.reddit.com/r/TikTokShopAffiliate/comments/1u5d6it/ (2026-06-14). Cost-side benchmark for the course/community ecosystem; r/TikTokshop 1vlzprr (u/Friendly_Sea8570): communities "$50 a month to $100 a month", live-sold courses "$1000-$5000".

---

## C. Cross-cutting observations for the plausibility check

1. **Metric confusion is systematic.** Vendors and course sellers quote GMV ("$100k GMV in 30 days", "$1.5M GMV", "$3M+ in sales"); affiliates quoting commission are far lower ($50/month, $200/month, $250/week, $1,000/month, $12k/6 months). Rule of thumb from the threads: commission ≈ 10–15% of GMV unless the product is a high-commission supplement (20–30%).
2. **Only two AI-specific claims give both GMV and commission** (A3: $10k GMV → $1,000; A4: ~$50k GMV/3 months → "$2k/month"), and both are tied to the same AI-video vendor ecosystem (Moras.ai) and got "fake"/"ad" replies. The headline AI claim (A1, $18–25k/month commission) has zero evidence and promo markers.
3. **Volume benchmarks (human):** 3–10 videos/day is the norm among affiliates reporting anything; 1,500–10k views per video typical for small accounts; sales per 1,000 views reported around 1–1.5 (H19) when a video converts; long-tail failure is common (H2: 1.5 years, ~480k views/month → $50).
4. **Negative AI/faceless reports:** u/sindhichhokro (6 months mass-produced clips, 5 niches, "negative returns"), u/joshmon4 (5 weeks daily faceless posting → "four bucks"), ShopReelAI test (10–15 AI videos/day → 200–1,200 views, no sales in 4 days), u/nkelly1101 (3 years incl. faceless, no conversions). Costs of generation "can easily surpass the profit" (u/moscowramada).
5. **Platform risk dominates 2025–26 threads:** frozen commissions ($1k–$20k+), bans for "account association"/bought accounts, retroactive violations, and a widely shared belief (H12 and 50+ comments) that organic reach of product-tagged videos collapsed after January 2026 unless brands run GMV Max. Both the "10-15 burner accounts" (A5) and "11 phones" style models depend on exactly the behaviour that the spring-2026 ban wave targeted.
6. **Course economics:** $37–$250/month Skool communities and $2,500 memberships sell the "£10k+/month" narrative; the only large testimonial with detail (£74k first year, £16k best month — Craig Dean, human, UK) is unverifiable and human-filmed.

## D. Threads identified but not readable (for a follow-up with a working Reddit route)
- https://www.reddit.com/r/TikTokshop/comments/1uf1zxj/ "Be honest... is anyone here pulling a decent income from TikTok Shop, or is it mostly guru hype" (2026-06-25, 57 comments)
- https://www.reddit.com/r/TikTokshop/comments/1umpzi8/ (36 comments), https://www.reddit.com/r/TikTokshop/comments/1r7h6jy/ (43 comments), https://www.reddit.com/r/SideHustleGold/comments/1sok5cr/ (6), https://www.reddit.com/r/passive_income/comments/1w7nihc/ (1), https://www.reddit.com/r/TikTokshop/comments/1pbk5us/ (15)
- X: no search possible this session; candidate handles to check with a working X route: @DeRonin_, @robiartec (relayed claims), plus whatever a `site:x.com "TikTok Shop" "AI UGC"` query returns.

Raw material kept in: `research/reddit_posts_dump.md`, `research/reddit_posts_dump2.md`, `research/reddit/comments/*.json`, `research/reddit/comments_dump.txt`, `research/x/*.json`.
