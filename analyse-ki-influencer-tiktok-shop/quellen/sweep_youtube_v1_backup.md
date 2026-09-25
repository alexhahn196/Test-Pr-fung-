# YouTube sweep: real TikTok accounts selling via TikTok Shop with AI / faceless content

Access date for everything below: 2026-09-24. Method: NexLev youtube_search (14 task queries + 8 follow-ups), youtube_video_details (descriptions), get_video_transcript / get_bulk_video_transcripts (26 videos, plus 40 transcripts already on disk from the W3 sweep), youtube_video_comments (17 videos), WebFetch on tiktok.com profiles, and ./tt_profile.sh sanity checks for every handle. Tags: **Verified** = seen in TikTok SSR JSON via tt_profile.sh; **Claimed** = asserted by the YouTuber/interviewee; **Estimated** = my calculation (formula shown).

## Tool limits that shaped this sweep (important for the reader)
- `watch_youtube_video_and_ask` was exhausted (15/15 daily calls used by earlier agents) before the first call here, so **on-screen handles could not be read visually**. Handles were only obtainable when they were (a) spoken in the transcript, (b) printed in the description, or (c) reconstructable from a spoken display name and confirmable with tt_profile.sh.
- WebSearch budget was exhausted (200/200) at the start of this sweep. TikTok discover pages (`tt_discover.sh`) returned a 39-byte block page for all 11 slugs tried. TikTok profile pages do not expose video lists to headless clients, so **video-level AIGC-label verification was not possible for any account below** (every tt_video.sh call on ids scraped from profile HTML returned 10204 "item doesn't exist"; those ids were not video ids).
- Net effect: this sweep yields a small number of hard handles and a larger list of concretely described but unnamed accounts. The unnamed ones are documented in section C so a later agent with `watch_youtube_video_and_ask` quota can read the handle off screen (video URL + timestamp given).

---

## A. Candidates with a concrete TikTok handle (sanity-checked with tt_profile.sh)

### 1. @healthysmartdeals — Model E/F (AI product-demo / mass-produced supplement videos), UK
- TikTok: https://www.tiktok.com/@healthysmartdeals
- **Verified (tt_profile.sh, 2026-09-24):** followerCount 95,500; heartCount 3,200,000; videoCount 208; createTime 1711579853 (2024-03-28); bio empty; ttSeller false; commerceUser false (so the Shop links are affiliate/showcase, not a registered seller account on the creator profile). Note: WebFetch's summary of the same page read "395.5K" followers, but the SSR JSON says 95,500; the JSON value is used.
- Named by: Victor Decodes Ecom, "You've Been Lied To About Tiktok Shop AI UGC", https://www.youtube.com/watch?v=NNIhmKGmpVY (published 2026-05-04, 192 views, 9:14). Transcript [1:12]: "about the seller, they're called Healthy Smart Deals. If we look at the revenue they've generated over the last 30 days, $68,670 at the time of recording". Same claim repeated in HowEcomWorks "I Found the AI System Making $68,670/Month on TikTok Shop" https://www.youtube.com/watch?v=b7POUuz16xc (2026-07-26, 127 views) — same author (Victor Loyiso), second channel.
- Description of NNIhmKGmpVY: "This account made $68,670 in 30 days using exclusively AI-generated TikTok Shop videos ... top-performing videos from Healthy Smart Deals ... Why they include a human hand in every video (and what it signals to TikTok's flagging AI) ... The niche pattern that makes AI UGC work (supplements and why)". Hashtag #TikTokShopUK -> UK market.
- **Claimed:** $68,670 GMV in 30 days (Kalodata/ShopCreatorSpy screenshot claimed; metric is GMV, not commission). **Estimated** commission at 10–20 %: $6.9k–$13.7k (formula: GMV x commission rate).
- AI usage (claimed): "exclusively AI-generated" product videos, retention-style edits, human hand in frame, supplements.
- Risk signal: YouTube comment (@TheAdequateMedia, 2026-06): "i think they got banned. mainly because their content is wildly violative of FTC guidelines" — the profile still resolves on 2026-09-24 with 208 videos, so not verifiable.
- Bias of source: Victor sells ShopCreatorSpy (own tool) and a Skool community ("DECODED"); links in every description.

### 2. @megs.homefinds ("Megshomefinds🎀") — Model B (realistic AI avatar / AI UGC creator), US
- TikTok: https://www.tiktok.com/@megs.homefinds
- **Verified (tt_profile.sh):** followerCount 33,700; heartCount 730,300; videoCount 269; bio "Cute fashion finds💗"; ttSeller false; commerceUser false.
- Named by: Jon Reiter, "exactly how I make $100k/month with Ai Tiktok Shop" / "How I Make AI TikTok Shop Videos That Sell (Full Guide)", https://www.youtube.com/watch?v=FtYeKKh0gqs (published ~2026-09-22, 5,058 views, 33:53). Transcript [4:31]: "This is a creator on TikTok. Her name is Meg's Home Find. And so, she's making these videos over here of this t-shirt. She's promoting this Tis the Season Halloween t-shirt. This video is completely fake. This is not a real person. Megan here is not a real person." [4:52]: "this creator right here has done a little over $22,000 just in the past month. And she's completely fake ... she's doing a lot of these apparel products".
- Handle reconstruction: spoken name "Meg's Home Find(s)" -> tried megshomefind (not found), megshomefinds (exists but is "Megs Crafted", a different person, 3.7k followers), **megs.homefinds** (nickname "Megshomefinds🎀", bio "Cute fashion finds", 33.7k followers, 269 videos) — this matches the described apparel/t-shirt account. Confidence: high on name match; AI-persona claim is Jon Reiter's, not verified at video level (no video URL obtainable).
- **Claimed:** "a little over $22,000 just in the past month" (Kalodata-type screenshot; metric ambiguous, likely GMV).
- Bias: Jon Reiter sells "Inner Circle" mentorship and an "AI Video Prompt Builder".

### 3. @naturalsquads — Model A/E (fully AI-generated supplement page), US — HANDLE MISMATCH, unresolved
- Named by: Adam Willis, "How an AI Tiktok makes this affiliate $20,000/month in PROFIT (copy them)", https://www.youtube.com/watch?v=p7q9GahGd7Q (2026-02-18, 1,003 views, 33:01). Transcript [3:15]: "This page natural squads has 483,000 followers all AI generated videos. And guess what they're driving directly to this page which is Rosabella maringa capsules." Description: "Examples of AI pages doing $4 Million/month (like Natural Squads)".
- **Verified (tt_profile.sh):** @naturalsquads exists but has followerCount 90, videoCount 5, createTime 2024-11-20 — clearly not the 483k-follower page. Variants naturalsquad (4,483 followers, Brazilian), natural.squad (7), natural_squad, naturalsquads.official/_us/.co, naturalsquadshop, thenaturalsquads: not found or unrelated. The real handle is probably a spelling variant shown on screen at ~3:15 of the video; needs a visual read.
- **Claimed:** 483,000 followers; "$4 Million/month" (Adam Willis' words, GMV context, unverifiable); product: Rosabella moringa capsules, beetroot product.
- Bias: sells mentorship (typeform application).

### 4. @realdavidmar (David Margaryan) — Model G/H context account (guru's own TikTok promoting "TikTok Shop Ai Automation"), US
- TikTok: https://www.tiktok.com/@realdavidmar
- **Verified (tt_profile.sh):** followerCount 17,100; heartCount 835,600; videoCount 1,509; bio "💻 TikTok Shop Ai Automation 👇 apply to work with me 1:1"; commerceUser false.
- Source: YouTube channel David Margaryan — "$0-$33,821 In 30 Days With Faceless Ai TikTok Shop Automation" https://www.youtube.com/watch?v=I_1fpXpUdbE (2026-07, 5,728 views); "This AI TikTok Shop Strategy Makes Me $1,000/Day" https://www.youtube.com/watch?v=pekAa14SbOM (2026-06-25); "Steal my full tiktok shop ai automation strategy to 30k/month" https://www.youtube.com/watch?v=G-jt_41qoxY (2h10m).
- **Claimed (I_1fpXpUdbE transcript):** "$33,821 in profit" in 30 days on one account; "scale 15 accounts"; a student "Tyler ... four accounts ... this account alone makes him over $15,000 in profit every single month ... he has a bot that makes all the videos"; system = mirror-selfie AI avatar videos ("Excited to start my journey" hook), Kalodata product research, VAs (5–8 accounts per VA).
- Caveat: this is the coach's marketing account, not the affiliate account whose numbers are claimed (that handle is not spoken). Comment evidence of failures under the same video: "Been doing it for a week. Not one commission" (9 replies); "these kind of videos got me zero sales so far been doing this for a couple of weeks.. I'm in the UK"; "my TT Ads campaigns keep getting suspended when I promote the mirror 'So excited to start my journey' AI avatar videos".
- Bias: strong (1:1 inner circle).

### 5. @healthiswealthfyp — Model D/H (faceless health FYP page; tommycetty's earlier account), US
- TikTok: https://www.tiktok.com/@healthiswealthfyp
- **Verified (tt_profile.sh):** followerCount 25,700; heartCount 100,300; videoCount 108; bio "Showing you the best videos that support our culture 👍🏿💕"; createTime 1761714237 (2025-10-29); commerceUser false.
- Named by: tommycetty, "I Had 30 Days to Make $10K With AI Content on TikTok Shop" https://www.youtube.com/watch?v=kjCyL4Vn4P4 (2026-03-04, 17.9k views) — transcript [3:30] names earlier own accounts "holistic.sophia" and "healthiswealthfyp". Caveat: the handle could have been re-registered since; the current bio wording ("support our culture") and the Oct-2025 creation date are consistent with a black-demographic health page as tommycetty describes ("black character for blood-pressure gummy"), but ownership is not verifiable. @holistic.sophia now resolves to a Brazilian personal account (43 followers, Portuguese bio) — handle recycled, not a candidate.
- **Claimed (kjCyL4Vn4P4):** $10,218.52 net commission in 25 days across ~11 phones/accounts; "In January, I did 92K GMV. February, I did 54K GMV"; top videos "$32 / $29 / $71 per 1,000 views" (GMV-based); "my main primary account did get banned at the end of it". Fully AI: Nano Banana Pro + ElevenLabs + HeyGen/Hedra.
- Bias: sells Simple Media "AI Accelerator" (join.simplemedia.ai).

### 6. @tommycetty — coach's own TikTok (context only)
- **Verified:** followerCount 1,991; heartCount 37,600; videoCount 168; bio "Ai Affiliate Discord ⬇️". Not an affiliate results account.

### 7. @densancar (Deniz Sancar) — coach's own TikTok (context only)
- Listed in the description of https://www.youtube.com/watch?v=Tsv7Zt9w9-4. **Verified:** followerCount 1,998; heartCount 21,500; videoCount 308. Not the challenge account (the 5-day AI greeting-card account is not named; see C.4).

### 8. @taro4orte (Taro) — coach's own TikTok (context only)
- Listed in description of https://www.youtube.com/watch?v=1U8aFiP7ZXY. **Verified:** followerCount 7,471; heartCount 202,800; videoCount 772; bio "tiktok monetisation learn for free". Human-face monetisation coach; not an AI shop account.

### 9. @loadedlife — Liam James Kay's 2024 AI-video TikTok Shop challenge account, UK — probably dead
- Named by: Liam James Kay, "TikTok Shop Affiliate + AI Videos = These Results", https://www.youtube.com/watch?v=eJ7SOZHKMkY (2024-05-22, 114k views, 20:04). Transcript: "I created a Tik Tok account called loaded life now".
- **Verified (tt_profile.sh):** @loadedlife exists, followerCount 1, videoCount 0, createTime 2022-06 — either the wrong handle or wiped. loadedlifenow / loaded.life.now / loadedlife_now: not found.
- **Claimed:** InVideo-AI stock-footage videos (Model D, AI voice + stock b-roll, no avatar). Results quoted from transcript: "only made around 50p in commissions" at first; later "£13,000 in sales" and roughly "£1,226 in commissions" (the auto-caption reads "£1 1226 in commissions"), first commission on 17 April 2024; best videos 30,000 and 77,000 views. A low-to-modest performer; useful as a UK 2024 baseline.
- Bias: InVideo + Kalodata affiliate links.

---

## B. Concretely described accounts WITHOUT a readable handle (need a visual read; video + timestamp given)

| # | Source video (URL, date) | What is shown | Claimed numbers | Model | Handle status |
|---|---|---|---|---|---|
| C.1 | HowEcomWorks, "I Found A Faceless AI Tiktok Shop Page Making $43k/month" https://www.youtube.com/watch?v=n298aKAIRI4 (2026-06-05, 8,040 views) | The page is scrolled on screen from 1:35 ("I filtered on their TikTok page here by oldest ... 32K ... 1 million there for those books ... 161,000 views"); products: books, pet supplies, makeup, supplements, skincare; "mainly just images, mainly just POVs showing the product ... clearly AI generated"; tool stack claimed: Canva AI + Arcads | $43,000 in one month (GMV, Kalodata) | E/F | not spoken; visible on screen ~1:35–3:00. Comment under video: "this kind of account gets lots of violations and ends up getting banned" |
| C.2 | HowEcomWorks, "Exposing BORING AI Videos Making $118,019 on TikTok Shop" https://www.youtube.com/watch?v=uNwGwwK_AwQ (2026-07-29, 143 views) | Kalodata breakdown of a seller/creator with plain AI product videos | $118,019 (30-day GMV) | E/F | not spoken |
| C.3 | THE ECOM KING, "I Tried TikTok Shop Affiliate With Sora 2 for 30 Days" https://www.youtube.com/watch?v=W5ThaDXg2ss (2025-11-16, 31k views) | (a) his own test account revealed on screen at 12:57–13:39 ("this is the account we've been doing this on"); (b) a third-party page at ~2:38–3:00 "this page purely only creates ... AI UGC content ... it's got 118,000 followers"; (c) another AI creator "generated almost $2,000 in just the last 30 days" (heart/vein supplement video) | Own account: "20 to 30,000 views ... around about $200 to $300" in 30 days (low performer). Third-party: $163 per video x ~8 videos ≈ $1,000 | C (Sora 2 + Arcads avatar + b-roll) | not spoken; on screen 12:57 |
| C.4 | Deniz Sancar, "I Tried Faceless AI TikTok Shop Affiliate for 1 Hour and made…" https://www.youtube.com/watch?v=Tsv7Zt9w9-4 (2026-03-26) | Own 5-day UK account (Mother's Day greeting cards found on FastMoss); capped by TikTok "creator pilot program"; "most videos got stuck around 500 views" | "would have easily eclipsed £50 in these 5 days" (i.e., <£50 actual) — failure/low performer | D/E | not spoken |
| C.5 | Turner (BatchBot team), "I tried AI TikTok Shop Affiliate for 7 days…" https://www.youtube.com/watch?v=DHZ8iI0Sbj0 (2026-09-17, 10k views) | Own US account (older furniture/t-shirt AI videos; second furniture account mentioned). Transcript [18:13]: "six items sold, $11 in commissions, and a 104 GMV"; a t-shirt video "505,000 views in the past 7 days and has sold zero t-shirt"; "this account is getting around $5 to $10 in sales a day" | $11 commission / $104 GMV in 7 days — **low performer, with cost breakdown at 29:11** (tool credits) | E (BatchBot mass-generated product videos) | not spoken; description discloses "I am part of the BatchBot team" (bias) |
| C.6 | Moe Alamawi, "These Ai Videos Generated $1.3M in 5 months on TikTok Shop" https://www.youtube.com/watch?v=Yyq9Htlghg8 (2026-08, 63.7k views) | Kalodata profile of a creator "Daniel" who "started in February 2026", "tested over 320 different products", custom AI backgrounds; comment says "The model account spongebob doesnt have yellow basket" (viewer could not find the cart on the model account -> possible restriction) | $1.3M GMV in <5 months | E/F | not spoken |
| C.7 | Osher, "How this AI Influencer Makes Me $1,290/day on TikTok Shop" https://www.youtube.com/watch?v=DwrbSlG53Fs (2026-02-02, 41.9k views) | Own Higgsfield/Kling AI influencer account; comments: "20:39 bruh, you're gonna tell me ts looks realistic", "That example will get you violations", fat-burner products flagged by a commenter as auto-violations | $1,290/day (screenshot claimed) | A/B | not spoken |
| C.8 | Adam Willis p7q9GahGd7Q (see A.3) | Second case: AI affiliate for the print-on-demand book "The Only Living Trust" — "$18,000 in commissions in just 30 days promoting a single product"; brand did "$300,000 in revenue" that month; stack Gemini + Veo 3 + ElevenLabs + HeyGen + CapCut "under $100" | $18k commission / $92k affiliate revenue | C | affiliate handle not spoken; product name is (onlylivingtrust / only.living.trust: not found on TikTok) |
| C.9 | ducrez, "These 15 Second Faceless AI TikTok Shop Videos Generated $450,063 In The Last 30 Days" https://www.youtube.com/watch?v=Ldkgz8ptFUQ (2026-09-21) | Agency model: multiple accounts, VAs (account warm-up VA, product-research VA, manager), "1% invite" so commissions shown are 1 % of GMV; GMV Max ad spend on winning videos | $450,063 GMV / 30 days across many accounts | F/G (mass-produced + VA-automated) | no handles; bias: Scalex AI Inner Circle |
| C.10 | tommycetty, "He Made $60K His First Month With AI Influencers" https://www.youtube.com/watch?v=3UpJfDnmTdA (2026-05-28) | Interviewee "Jimmy" (YouTube commenter @jimmyjcastillo): "5 banned TikTok Shop accounts and $27,000 in frozen commissions", then "$60K+ GMV in his first month using AI content", "1.2M views on a single video and 20K followers in 2 days", runs TikTok + Meta accounts | $57–60k GMV month 1; $27k frozen | B (AI avatars) | not spoken |
| C.11 | Moe Alamawi, "How Dakota Made $10,224 in his first 60 days doing Ai TikTok Shop" https://www.youtube.com/watch?v=YK1OYb5g_bA (2026-07-21) | Student Dakota, one account, faceless AI | "$4,200 in profit in his first 30 days ... over $6k profit in his second month with only ONE account" | E | only Instagram given (dakota_ecom) |
| C.12 | tkay (DE), "Wie ich mit KI TikTok Shop Videos erstelle, die mir 10.000€ am Tag generieren" https://www.youtube.com/watch?v=hsu2OMVUcuw (2026-08-01, 706 views) | German creator running US-market accounts: Claude + Google Flow (Veo 3) faceless videos, slideshow meta, Ü40 "Facebook-Moms" targeting; shows his own account and a copied Spanish-language account (transformation/weight-loss product) | "45.300 $ im Monat"; one video "130.000 Views -> 10.500 $"; best AI video "~70.000 $ mit einem einzigen Video" | D/E | not spoken; sells 1:1 mentoring (joinmajorleague.de) |
| C.13 | Jhonatas Silva (BR), "Eu CRIEI uma INFLUENCIADORA DE IA para VENDER SEM APARECER no TIKTOK SHOP" https://www.youtube.com/watch?v=wayWM3TS6V4 (2026-09-01, 71.5k views) | Own Brazilian test account with an AI model wearing supplier clothes; transcript [30:38] "this account is a test account of mine ... It's not an account where I make thousands of reais" | "R$ 11.000 em 7 dias" (description) vs. "test account" (transcript) — inconsistent | A/B | not spoken; sells Tokfy subscription |
| C.14 | Seraphin (FR), "Cet AVATAR IA Me Rapporte 5000€/mois sur TIKTOK" https://www.youtube.com/watch?v=xi7w9ZczIy0 (2026-02-09, 80.7k views) | Own French AI avatar (Pinterest reference -> Syzel/Nano Banana image -> ElevenLabs voice -> HeyGen animation); commenter asks about "la fille qui danse" avatar | "5000 € par mois" | B/C | not spoken; sells "Accélérateur TikTok Shop" + Syzel affiliate |
| C.15 | Mark Tilbury, "I Tried The LAZIEST Way to Make Money With AI" https://www.youtube.com/watch?v=LlhTEttKcwQ (2026-09-21, 2.8M views) | Three Higgsfield AI influencers: "Amos Oldways" (101-year-old health/farm), "Sienna" (dating advice), "Grandma Vivian/Viven" (luxury wealth); accounts launched at 19:07; monetised with a digital product/e-book, not TikTok Shop; comment: Vivian's account "explode to 250k views" | not TikTok-Shop; 7-day test | A (fully virtual) | accounts are Instagram/Reels-first; TikTok handles not spoken — out of scope for Shop but useful as an A-model reference |
| C.16 | MediaLabs, "How He Made $47k Last Month On TikTok Shop (Faceless)" https://www.youtube.com/watch?v=77V4PEVWNyE (2026-07-30) | "Ben", 90 % faceless human-filmed product demos + long lives, seasonal fans | "7,800 units in May ... 47.4k take home commission ... $430,000 of GMV ... hit sapphire" | not AI (human faceless) — benchmark only | not spoken |
| C.17 | (bulk transcript, Taro Creates U8Y1Hj4r4mY / pHqKL58-zFE) | "a faceless creator called Deals with Tai ... the number one Tik Tok shop affiliate right now ... 99% of his content is completely faceless ... This video alone ... 19 million views, hundreds of thousands of dollars in commissions" | — | human faceless benchmark | dealswithtai / deals.with.tai / dealwithtai etc.: not found |
| C.18 | Patryk Marketer, "I WASTED 30 Days Trying To Make Money With AI Videos on TikTok" https://www.youtube.com/watch?v=NKxTt215kus (2026-01) | Own Sora-2 POD (print-on-demand hoodie) account; "you only got like 8-9% commission on each sale" (comment) | small/negative result per title | E | not spoken |

---

## C. Claimed-number summary (all **Claimed** unless marked)
| Claimant / account | Amount | Period | Metric | Bias |
|---|---|---|---|---|
| Healthy Smart Deals (@healthysmartdeals, Verified profile) | $68,670 | 30 d (Apr–May 2026) | GMV | Victor Loyiso sells ShopCreatorSpy/Skool |
| Meg's Home Finds (@megs.homefinds, Verified profile) | "$22,000+" | past month (Sep 2026) | ambiguous (likely GMV) | Jon Reiter mentorship |
| Natural Squads (handle unresolved) | "$4M/month"; 483k followers | — | GMV (unverifiable) | Adam Willis mentorship |
| Only Living Trust affiliate (handle unresolved) | $18,000 | 30 d | commission | same |
| David Margaryan (@realdavidmar) | $33,821 | 30 d | "profit" | inner circle |
| tommycetty (own accounts) | $10,218.52 | 25 d | net commission; 92k/54k GMV Jan/Feb | Simple Media course |
| Jimmy (tommycetty student) | $57–60k | month 1 | GMV; $27k frozen, 5 bans | same |
| ducrez agency | $450,063 | 30 d | GMV, many accounts | Scalex AI |
| Moe Alamawi "Daniel" | $1.3M | <5 months | GMV | Momentum academy |
| Dakota (Moe student) | $4,200 / $6,000+ | month 1 / month 2 | profit | same |
| Osher | $1,290/day | — | screenshot | mentorship + Higgsfield affiliate |
| tkay (DE) | $45,300/month; $70k one video | — | GMV | mentoring |
| Seraphin (FR) | €5,000/month | — | unclear | accelerator + Syzel |
| Ecom King own test | $200–300 | 30 d | GMV/commission unclear | Arcads affiliate |
| Turner (BatchBot) own test | $11 commission / $104 GMV | 7 d | dashboard | BatchBot team |
| Deniz Sancar own test | <£50 | 5 d | commission | FastMoss/Virlo affiliate |
| Liam James Kay (@loadedlife?) | ~£1,226 commission / £13,000 sales | ~Apr–May 2024 | dashboard | InVideo affiliate |
| Ben (MediaLabs, human faceless) | $47.4k commission / $430k GMV | May 2026 | dashboard | MediaLabs community |

## D. Recurring risk signals seen in comments/transcripts
- Bans/violations: tommycetty "main primary account did get banned"; Jimmy "5 banned accounts, $27,000 frozen"; Moe's comment thread "I just got a violation", "new restrictions for ai tiktok shop videos ... only upload up to 5 videos in one week" (unverified viewer claim), "more than 300 low quality violations"; n298aKAIRI4 comment "this kind of account gets lots of violations and ends up getting banned"; NNIhmKGmpVY comment "i think they got banned ... FTC guidelines"; Mikey Again admitted losing both accounts (d9oQ9mudR-o).
- Labeling: multiple comments assert that not tagging AI content causes violations while tagging kills reach (d9oQ9mudR-o, DHZ8iI0Sbj0, FtYeKKh0gqs "embedded watermark that tiktok is adding to all the AI output").
- Geography: UK users report zero sales with US-style mirror-avatar videos (I_1fpXpUdbE comments); Canadians "can't make money posting on TikTok" (3PsYkG-5T38 comment).

## E. Videos triaged but not useful for handles
Isa does AI a-INhZE9aII (Higgsfield workflow only), Alex Finds 00H1u5-B57E (4 AI influencer archetypes, no accounts), Ai Scope 8l7Ji1JDfnM (Oumomo sponsored; "seller" from FastMoss unnamed, product grew "$4K to over $390K GMV"), Derek Kumo 90MZx-l7mSI (2024, three human faceless videos: car charger 9M views/$245k, air purifier 8.48M/$317k, Fanttik screwdriver 3.38M/$181k — all human, not AI), Chase Fisher iODYPrE9Iws, Taro 1U8aFiP7ZXY (Creator Rewards commentary pages, not Shop), Mark Tilbury (Instagram, digital product).
