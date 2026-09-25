# Web search sweep (English terms) – AI / faceless TikTok Shop accounts
Agent: sweep_web_terms · Access date for all URLs: 2026-09-24 (run 1) / 2026-09-25 (run 2 = retry with WebSearch; see section 'RUN 2' at the end)

## Method / caveats
- Run 1: WebSearch budget was exhausted (200/200) before this agent started; Bing via curl truncated multi-word queries to the first word. Working substitute: DuckDuckGo HTML rendered through r.jina.ai (`./dsearch.sh "<query>"`, raw results in research/ddg_batch1..10.txt). All 15 required queries plus ~40 variants were run.
- Articles opened with WebFetch (or r.jina.ai for BI/WSJ-summaries). YouTube evidence via NexLev video details/transcripts. NexLev "watch" tools hit their daily cap (15/15) – no visual verification of TikTok videos was possible in this session; AI evidence therefore comes from TikTok's own `aigcLabelType` field (tt_video.sh), captions/hashtags, and third-party reporting.
- Every handle below was sanity-checked with `./tt_profile.sh` (statusCode 0 = exists). Numbers are tagged Verified (TikTok SSR data, seen today), Claimed (asserted by a source) or Estimated.
- Key finding of the sweep: almost all "AI TikTok Shop" articles (Influencer Daily, Business Insider, WSJ summaries, shortformnation, duoplus, hooc.ai, viraladsnow, pops4, lawsnap, OECD.AI …) name NO concrete accounts. Concrete handles came from: 404 Media, Media Matters, WSJ (via charm.io summary), a YouTube case-study channel (Victor Decodes Ecom), TikTok result pages surfaced by DDG, and creator self-promotion.

## Search log (queries → useful hits)
| Query | Useful result |
|---|---|
| AI TikTok Shop affiliate | krafie.com guide; shortformnation "70/30 framework" (no handles) |
| AI influencer TikTok Shop | Influencer Daily 2026-07-24 (no handles); Business Insider 2026-07-20; feedspot "Top 40 AI TikTok influencers" (human AI-educators, not virtual) |
| AI UGC TikTok Shop | tool vendors only (ugcfirst, clipnova, prizmad, ugcvids.ai) + reddit r/dropship thread |
| faceless TikTok Shop | tiktok.com/tag/FacelessShop; skool.com/faceless-ai; guides (no handles) |
| TikTok Shop affiliate automation | vendor pages (Reacher, Euka, Cruva, AffiliateBot Chrome ext.) |
| AI avatar TikTok affiliate | avatarfactory.io, syntopia.ai (AI live hosts), onemarsmedia policy-violation write-up |
| TikTok Shop case study AI | generic; "$1M AI Dropshipping Case Study" (Michael Bernstein YouTube) |
| TikTok Shop affiliate earnings AI | duoplus.net "$200K/month" (no named accounts), hooc.ai "$675K" case (anonymised) |
| AI generated TikTok product videos | vendors (Pippit, CreatOK, BatchBot, ClipMove) |
| virtual influencer TikTok Shop | tiktok.com/tag/virtualinfluencer, syntopia virtual host, iatikshop.com (BR tool) |
| faceless TikTok affiliate | earnfacts.com, riffkit.ai, financialbinder (no handles) |
| TikTok Shop AI videos | WSJ "AI Videos Are Flooding TikTok Shop" (paywalled; summaries at charm.io, shopifreaks, aiweekly) |
| AI slop TikTok Shop | @ai_slop_merch; 404 Media "AI TikTok Shop Slop Factory" (Rosabella); veonib.com; Mashable (blocked) |
| AI UGC creator account TikTok example | @alex.prompt video; tokportal; ezugc |
| TikTok Shop AI avatar account @ | percify.io, moras.ai, onemarsmedia (AI-avatar LIVE strike) |
| "Rosabella" tiktok AI doctor | shop.tiktok.com Rosabella listings; aiweekly/dailysynapse summaries; 404 Media names @liverboosthub11 and @poormaninla |
| "Harry Chang" … | 404 Media; magica summaries; YouTube videos Iv8DddAIXLw & TXMLLnGGwFY now "removed for violating YouTube ToS" (verified via NexLev transcript error 403) |
| "Healthy Smart Deals" | no web hits; handle @healthysmartdeals resolved by tt_profile |
| site:tiktok.com "#ai" … propane torch / magnesium | @ttsemily7, @gardenmolly, @vanover7, @highlightdiscovery, @dlhblingbling, @yalltakecare |
| Daria Simhony | @dariasimhony (WSJ-named AI-avatar creator) |
| Granny Spills | @grannyspills (Time, 2026) |
| Josh Adkins AI creator £60K | @joshadk (account named in his own YouTube video), @josh.ttsa |
| Mikey Again veo 3 | @mikey.again02 (his AI avatar accounts were banned; not named) |

## Candidates (with evidence)

### 1. @healthysmartdeals  — Model F (mass-produced AI videos) / C (AI voice + AI visuals)  — US/UK unclear
- Verified (tt_profile 2026-09-24): 95,500 followers · 3.2 M likes · 208 videos · created 2024-03-27 · no bio · commerceUser false.
- Claimed (YouTube "You've Been Lied To About Tiktok Shop AI UGC", Victor Decodes Ecom, 2026-05-04, https://www.youtube.com/watch?v=NNIhmKGmpVY): "a seller who has generated $68,670 in the last 30 days in revenue using exclusively AI generated content … they're called Healthy Smart Deals"; top video "$23,180 in revenue, 1.6 million views"; "All of them are coming up as ads, which means more than likely they are part of the TikTok GMV Max system". Products: Toplux Magnesium Complex, Leaf bar cutting drink mix, Cutler Nutrition liquid carnitine, apple cider vinegar, magnesium glycinate. Format: "obviously AI generated video … retention style editing … bright big font captions … product images throughout … a video clip of someone with their hand holding the product".
- Failure signal: top comment (2026-06-24) "i think they got banned. mainly because their content is wildly violative of FTC guidelines" (account still resolves today).
- Video-level data: not obtainable (no video URLs found by search).

### 2. @liverboosthub11  — Model H/D (faceless "health hub", script source of the Rosabella AI videos)  — US
- Verified: 2,668 followers · 60,200 likes · 137 videos · created 2025-06-04 · nickname "Health u1s1".
- Source: 404 Media, Jason Koebler, 2026-07-30, https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/ — "Chang explains that he copy-pasted the script from a video posted by an account called 'liverboosthub11'". Also names @poormaninla (statusCode 10221 today → gone) and creators Harry Chang / Jimmy Farley; Rosabella (Ambrosia Brands, sued by Humann Feb 2026) "boasted about paying out over $400,000 to creators in a single month"; Chang's AI video "1.3 million views … tens of thousands of dollars in affiliate sales" (Claimed). Chang's YouTube videos ("This AI TikTok Shop Video Made Me $67,420", "$320,000 … Asian grandma") are now removed by YouTube.

### 3. @dariasimhony  — Model B (realistic AI avatar UGC/affiliate creator + educator)  — US
- Verified: 128,700 followers · 2.1 M likes · 918 videos · bio "Helping mamas make $ online with AI" · commerceUser false.
- Verified video https://www.tiktok.com/@dariasimhony/video/7660244768810683678 ("UGC Example of AI Avatar promoting her favorite skincare - Jumiso"): aigcLabelType=1 (TikTok AI label), isECVideo=1, product anchor attached, 34,800 plays, 256 likes, 7 s, posted 2026-07-08.
- Claimed (WSJ via charm.io summary https://blog.charm.io/charm-in-the-press/ai-videos-are-flooding-tiktok-shop): creates "at least one fully AI-generated promotional TikTok post every day"; income "mix of affiliate commissions and fixed-fee brand deals"; clients Jumiso, AI-tool startups. Own captions: "AI Avatars Income: How I Made $3 Million This Year", "I just make AI Avatar content and I've become a multimillionaire in one year" (video 7683686556074265887: 131 s, no AI label). Not publicly verifiable.

### 4. @grannyspills  — Model A (fully virtual AI influencer)  — US
- Verified: bio "Spilling tea & designer receipts since 1950 · granny@blurstudios.ai"; bioLink = Artlist affiliate link; created 2025-07-04. (Full stats in raw section below.)
- Claimed (Time, https://time.com/7329699/ai-influencers-tiktok-granny-spills/): 400,000 TikTok followers, 1 M Instagram; operators Eric Suerez & Adam Vaserstein (Blur Studios); made with Claude + Veo 3, "one video can be 5-10 minutes"; videos flagged "unoriginal" and de-monetised from Creator Rewards; monetisation = brand sponsorships, Cameo, affiliate link. No TikTok Shop evidence → relevant as A-model benchmark and as example of TikTok's "unoriginal content" enforcement against AI personas.

### 5. @highlightdiscovery  — Model E (AI product visualisation) / F  — US
- Verified: 96,600 followers · 7.7 M likes · 348 videos · created 2023-06-07 · empty bio.
- Verified video https://www.tiktok.com/@highlightdiscovery/video/7670710917667032351 caption "Toplux Magnesium Capsules - *** AI-generated product visualization. Flash sale shown was current at the time of posting…": aigcLabelType=1, isAd=true, isECVideo=1, product anchor, 8 s, 1,445 plays, 5 likes (2026-08-06). Same Toplux product as @healthysmartdeals; caption self-discloses AI. Low per-video reach despite 96K followers.

### 6. @gardenmolly  — Model E/F (AI product demo, home/garden tools)  — US
- Verified: 835 followers · 14,800 likes · 549 videos · created 2025-07-09 · empty bio.
- Verified video https://www.tiktok.com/@gardenmolly/video/7666099130065784078 "…this Saker propane torch… #PropaneTorch #ai #summerwins #TikTokShopDealsforYouDays": aigcLabelType=1, isAd=true, 37 s, 9,248 plays, 24 likes (2026-07-26). Matches Business Insider's description of AI clips where "synthetic avatars used power washers and propane torches … to spotlessly clean their driveways" (https://www.businessinsider.com/tiktok-shop-creators-brands-using-ai-to-replace-human-slop-2026-7).

### 7. @ttsemily7  — Model E/F (AI product demos, same tool cluster; low performer)  — US
- Verified: 351 followers · 4,694 likes · 488 videos · created 2025-07-09 (same creation day as @gardenmolly → probably same operator network) · bio "Smart tools. Less effort. More savings."
- Verified videos: 7654477746499783950 "#propanetorch … #ai" (isAd, no AI label, 2,080 plays, 4 likes); 7654495377059581197 Saker torch (isAd, 28 s). 488 videos for 351 followers = textbook mass-produced low performer.

### 8. @vanover7  — Model E / H (seller account posting torch demos)  — US
- Verified: ttSeller=true, commerceUser=true (category "Shopping & Retail") · 1,000 followers · 21,000 likes · 217 videos · created 2025-09-11.
- Video 7660852055963110670 "#propanetorch #tiktokshop": isAd, isECVideo, product anchor + CapCut anchor, 45 s. AI not labelled – "probable AI" only by format cluster. Include as H.

### 9. @ai_slop_merch  — Model D (faceless AI-slop merch; failure)  — US
- Verified: 0 followers · 0 likes · 3 videos · created 2026-07-09 · bio "suq1y2-we.myshopify.com · extremely online shirts · $19.99". Sells via Shopify, not TikTok Shop. Zero traction.

### 10. @wellnesswelfare  — Model H/D (fabricated storytime slideshows selling supplements)  — US
- Source: Media Matters, Olivia Little, 2025-03-04, https://www.mediamatters.org/tiktok/scammers-seem-be-using-deepfake-and-ai-generated-influencers-tiktok-sell-you-wellness — account "Wellness Welfare" ran fabricated storytime slideshows selling "Hey Girl" supplements to women with PCOS/fertility issues; second account "Holistic Health Finds" used deepfake influencer personas to sell batana oil (handle @holistichealthfinds → 10221 today). Update 2025-03-10: "All of the accounts included within this piece appear to have been removed".
- Verified today: @wellnesswelfare exists, created 2025-04-23 (i.e. re-created after removal), 2,506 followers · 53,500 likes · 381 videos · Facebook bio link. Whether same operator: not publicly verifiable.

### 11. @chad_wellness (+ @chad.wellness, @chadwellness)  — Model H (AI wellness persona; claim/reality gap)  — US
- Claimed (magica summary of removed Harry Chang video): "Chad Wellness – grew to 125K followers and earns thousands monthly".
- Verified: @chad_wellness 214 followers, bio "Wellness tips your Dr. won't tell you", created 2025-04-18; @chad.wellness 5 followers/14 videos (created 2026-03-08); @chadwellness 1 follower/0 videos. Facebook page 8,064 likes; YouTube 1.16K subs. → low performer on TikTok; the 125K claim is not reproducible on TikTok.

### 12. @tommycetty  — Model G (operator/educator of AI TikTok Shop accounts)  — US
- Verified: 1,991 followers · 37,600 likes · created 2025-12-14 · bio "Ai Affiliate Discord" · link simplemedia.ai.
- Claimed (YouTube 1XO4S9ZKLDY "I Made $60K in 10 Days with AI TikTok Shop", 2026-01-14, 39.5K views): "I've spent the last year building, testing, failing, getting banned, rebuilding"; hooc.ai blog: "over $90,000 through AI content". Tools listed: Claude, Sora, Veo 3, ElevenLabs, Nano Banana, Kling/Higgsfield/Wan/Seedream. Related YouTube 3UpJfDnmTdA (Simple Media interview "Jimmy"): "more than five banned accounts … 27k in commission frozen … my first video like for 1.2 million view with the new character, and I made 20k followers in the first two three days" (avatar holding an ice cube) – account not named.

### 13. @joshadk  — Model G/H (human affiliate who posts AI-remade viral videos)  — UK
- Verified: 70,400 followers · 1.9 M likes · 1,299 videos · created 2020-01-16 · bio "follow for the best products".
- Claimed (YouTube J3w1uyT50ts "it took 1 hour to make $61,218 with this AI video", transcript): "I posted it on this account called Josh ADK … I actually stole somebody else's video completely using AI … 8 million views in just 2 weeks … $61,000 in complete GMV and $9,000 of that was complete profit"; X post: "The AI creator below made £60K in two months". Teaching account @josh.ttsa: 18,400 followers (Verified).

### 14. @adanghyt  — Model G (Indonesian affiliate/educator using Veo 3 for affiliate content)  — ID
- Verified: 76,400 followers · 853,900 likes · 752 videos · bio "Produktif Pakai AI Biar Bisa Dapet Pasif Income · Jualan & Monetize" · link adanghdyt.com.
- Evidence: video 7560546805583334667 "Konten Affiliate Sukses dengan VEO 3" (975 likes, 51 comments per DDG snippet). Non-US market example.

### 15. @mikey.again02  — Model G (operator; AI-avatar affiliate accounts banned)  — UK/US
- Verified: commerceUser=true; 3,292 followers (DDG snippet), bio "To learn directly from me for free".
- Claimed (YouTube d9oQ9mudR-o, 491K views, transcript): Veo 3 characters ("70-year-old grandma", street-interview men) selling beetroot + oregano supplements on a UK and a US phone; "$20,000 in sales from 1.7 million views … $3,000 in profit" in one month; "two violations saying that my content was unoriginal"; "I did eventually end up losing those accounts like a month later … $3,722 frozen"; now "20 accounts going". Avatar accounts not named → cannot be listed separately.

### 16. @sweatsuitbillionaire  — Model G/H (Claude + Higgsfield "AI twin" TikTok Shop content)  — US
- Verified: bio "no guru cape · just chasing the AI bag"; video 7662639195961216287 "Claude and Higgsfield TikTok Shop: How to Make Money With an AI Twin" (DDG). Stats in raw section.

### 17. @lou.mercado  — Model B (AI fashion UGC agency; B2B, not affiliate)  — US
- Verified: bio "You've bought our Ai Fashion! $3M+sold using Ai · Fndr @TheLuKrativeAgency"; video 7673959690526657806 "ai ugc video ads and ai tiktok shop video is taking over" (30 likes). Claim "$3M+ sold" not publicly verifiable.

### 18. @alex.prompt  — Model B (AI UGC creator/educator)  — US
- Verified: 48,500 followers · 290,600 likes · 147 videos · bio "CLAUDE CODE & AI UGC". Video 7597763306081815830 "Creating Authentic AI UGC Content". No TikTok Shop selling evidence → context only.

### 19. @leya.love / @leyaloveproducts  — Model A (virtual influencer "Leya Love"; TikTok low performer)
- Verified: @leya.love 36 followers/175 likes; @leyaloveproducts 766 followers · 2,793 likes · 2 videos (created 2024-04-06). Claimed (amraandelma list): 549K TikTok followers – not reproducible today. Instagram 494K. No shop evidence.

### Excluded / false positives
- @haha_what ("Sora", 326,600 followers, 1,972 videos, 13.7 M likes; crevideo: "$0-$5k GMV last 30 days") – matched only because the creator's display name is "Sora"; appears to be a human creator. Not AI.
- @rosemarieandolive (12,900 followers, bio "TikTok shop affiliate behind the scenes · 4M+ GMV") – WSJ's human counter-example ("I create ads for products that I have in person—real reviews").
- @yalltakecare (145,000 followers, 1,705 videos) and @dlhblingbling (20,300 followers, 1,181 videos) post the same propane-torch Shop ads (isAd, isECVideo) but carry no AI label/hashtag → not evidenced as AI.
- Feedspot "Top 40 AI TikTok influencers" = human AI educators, not virtual sellers.
- @mrs_perkins4 (Rosabella review) – human.

### Named but no handle found (for the report's narrative)
- Rosabella / Ambrosia Brands (seller) – AI "doctor" avatars, Discord-coached creator network, "$400,000 paid to creators in one month" (Claimed, 404 Media).
- Harry Chang (NZ) – "$67,420 from one AI video", "$320,000 revenue / $65,000 profit from one video (15.2 M views)" (Claimed; source videos removed by YouTube).
- Nikki Teaches AI (YouTube xJMTnEuxcIw, 2026-06-10): AI influencer grown to 1,064 TikTok followers, approved for TikTok Shop, "only made two TikTok Shop sales … 370 views, $21 made" – handle not shown in transcript. Good low-performer datapoint.
- onemarsmedia.com: AI-avatar TikTok Shop LIVE struck "within minutes" for "Reproduced/Unoriginal Content Violation (Livestream)"; LIVE suspended, Compliance Health -30, commission withdrawal blocked.
- SharkNinja (brand) bans AI content in its affiliate programme (WSJ/BI); Cider and Rare Beauty AI-labelled affiliate posts (charm.io / Independent).

## Raw profile re-checks (tt_profile.sh, 2026-09-24)
- @grannyspills: {"statusCode": 0, "statusMsg": "", "uniqueId": "grannyspills", "nickname": "Granny Spills", "signature": "✨ Spilling tea & designer receipts since 1950\n📧 granny@blurstudios.ai", "verified": false, "createTime": 1751671936, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://artlist.io/artlist-70446/?artlist_aid=granny-spills_4134&utm_source=affiliate_p&utm_medium=granny-spills_4134&utm_campaign=granny-spills_4134", "isOrganization": 0, "stats": {"followerCount": 932800, "followingCount": 4, "heart": 13200000, "heartCount": 13200000, "videoCount": 552, "diggCount": 0, "friendCount": 4}}
- @dariasimhony: {"statusCode": 0, "statusMsg": "", "uniqueId": "dariasimhony", "nickname": "dariasimhony", "signature": "30yr old girlie🩷Boy Mom\nSpicy Mama🌶️\nHelping mamas make 💰 online with AI\n💌PR/Opportunities: dariasimhony@gmail.com", "verified": false, "createTime": 1576839951, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "Dariasimhony.com", "isOrganization": 0, "stats": {"followerCount": 128700, "followingCount": 1207, "heart": 2100000, "heartCount": 2100000, "videoCount": 918, "diggCount": 0, "friendCount": 942}}
- @sweatsuitbillionaire: {"statusCode": 0, "statusMsg": "", "uniqueId": "sweatsuitbillionaire", "nickname": "AyeDre | Sweatsuit Billionaire", "signature": "no guru cape 🦸🏿‍♂️ \njust chasing the AI bag 💸 \nits gonna get weird 🙄\nbeacons.ai/sweatsuitbillionaire", "verified": false, "createTime": 1728253125, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 166, "followingCount": 33, "heart": 2479, "heartCount": 2479, "videoCount": 132, "diggCount": 0, "friendCount": 18}}
- @lou.mercado: {"statusCode": 0, "statusMsg": "", "uniqueId": "lou.mercado", "nickname": "𝕃𝕠𝕦 𝕂𝕣𝕒𝕥𝕚𝕧𝕖", "signature": "You've bought our Ai Fashion!😉\n$3M+sold using Ai🏆\nFndr @TheLuKrativeAgency \n𝕋𝕙𝕖 𝕍𝕠𝕚𝕔𝕖 𝕠𝕗 𝔸𝕚 𝔽𝕒𝕤𝕙𝕚𝕠𝕟\nHelping Creators&Brands scale with AI👇", "verified": false, "createTime": 1675592413, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://stan.store/LouKrative", "isOrganization": 0, "stats": {"followerCount": 9518, "followingCount": 725, "heart": 35500, "heartCount": 35500, "videoCount": 951, "diggCount": 981, "friendCount": 48}}
- @tommycetty: {"statusCode": 0, "statusMsg": "", "uniqueId": "tommycetty", "nickname": "TommyCetty", "signature": "Ai Affiliate Discord ⬇️", "verified": false, "createTime": 1765687696, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://simplemedia.ai/d/SIMPLEZRGGEG", "isOrganization": 0, "stats": {"followerCount": 1991, "followingCount": 1, "heart": 37600, "heartCount": 37600, "videoCount": 168, "diggCount": 0, "friendCount": 1}}
- @joshadk: {"statusCode": 0, "statusMsg": "", "uniqueId": "joshadk", "nickname": "Josh", "signature": "follow for the best products 🤝\njoshinfo02@gmail.com 📩", "verified": false, "createTime": 1579195733, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 70400, "followingCount": 93, "heart": 1900000, "heartCount": 1900000, "videoCount": 1299, "diggCount": 0, "friendCount": 36}}
- @josh.ttsa: {"statusCode": 0, "statusMsg": "", "uniqueId": "josh.ttsa", "nickname": "Josh Adkins | TikTok Shop", "signature": "Teaching TikTok Affiliate\nFree Group Below ⬇️", "verified": false, "createTime": 1690919301, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "skool.com/affiliateacademyfree", "isOrganization": 0, "stats": {"followerCount": 18400, "followingCount": 2, "heart": 144700, "heartCount": 144700, "videoCount": 285, "diggCount": 0, "friendCount": 1}}
- @adanghyt: {"statusCode": 0, "statusMsg": "", "uniqueId": "adanghyt", "nickname": "adanghyt", "signature": "Produktif Pakai AI Biar Bisa Dapet Pasif Income 🤑\nJualan & Monetize ✅️", "verified": false, "createTime": 1671805807, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://adanghdyt.com", "isOrganization": 0, "stats": {"followerCount": 76400, "followingCount": 49, "heart": 853900, "heartCount": 853900, "videoCount": 752, "diggCount": 0, "friendCount": 19}}
- @alex.prompt: {"statusCode": 0, "statusMsg": "", "uniqueId": "alex.prompt", "nickname": "alex.prompt", "signature": "Create visuals with AI\nAll the info needed in my link 🔗 \n📩Alex.prompt@outlook.com\n⬇️CLAUDE CODE & AI UGC⬇️", "verified": false, "createTime": 1749821147, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 48400, "followingCount": 1367, "heart": 290600, "heartCount": 290600, "videoCount": 147, "diggCount": 0, "friendCount": 860}}
- @mikey.again02: {"statusCode": 0, "statusMsg": "", "uniqueId": "mikey.again02", "nickname": "Mikey Again", "signature": "To learn directly from me for free👇👇", "verified": false, "createTime": 1764589017, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": true, "downLoadLink": {"ios": "", "android": ""}, "category": "Others", "categoryButton": false}, "bioLink": "https://forms.gle/c2zC76rs5CJ7sredA", "isOrganization": 0, "stats": {"followerCount": 3383, "followingCount": 0, "heart": 454800, "heartCount": 454800, "videoCount": 114, "diggCount": 0, "friendCount": 0}}
- @healthysmartdeals: {"statusCode": 0, "statusMsg": "", "uniqueId": "healthysmartdeals", "nickname": "healthysmartdeals", "signature": "", "verified": false, "createTime": 1711579853, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 95500, "followingCount": 3, "heart": 3200000, "heartCount": 3200000, "videoCount": 208, "diggCount": 0, "friendCount": 3}}
- @highlightdiscovery: {"statusCode": 0, "statusMsg": "", "uniqueId": "highlightdiscovery", "nickname": "highlightdiscovery", "signature": "", "verified": false, "createTime": 1686126596, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 96600, "followingCount": 40, "heart": 7700000, "heartCount": 7700000, "videoCount": 348, "diggCount": 0, "friendCount": 0}}
- @gardenmolly: {"statusCode": 0, "statusMsg": "", "uniqueId": "gardenmolly", "nickname": "gardenmolly", "signature": "", "verified": false, "createTime": 1752041860, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 835, "followingCount": 14, "heart": 14800, "heartCount": 14800, "videoCount": 549, "diggCount": 0, "friendCount": 5}}
- @ttsemily7: {"statusCode": 0, "statusMsg": "", "uniqueId": "ttsemily7", "nickname": "TTSEmily", "signature": "Smart tools. Less effort. More savings. \nFollow for my best finds.💡", "verified": false, "createTime": 1752044705, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 351, "followingCount": 43, "heart": 4694, "heartCount": 4694, "videoCount": 488, "diggCount": 760, "friendCount": 15}}
- @vanover7: {"statusCode": 0, "statusMsg": "", "uniqueId": "vanover7", "nickname": "Vanover", "signature": "Follow me to start a new era of tool hoarding!🥰", "verified": false, "createTime": 1757572059, "region": null, "ttSeller": true, "commerceUserInfo": {"commerceUser": true, "downLoadLink": {"android": "", "ios": ""}, "category": "Shopping & Retail", "categoryButton": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 1000, "followingCount": 1, "heart": 21000, "heartCount": 21000, "videoCount": 217, "diggCount": 0, "friendCount": 0}}
- @liverboosthub11: {"statusCode": 0, "statusMsg": "", "uniqueId": "liverboosthub11", "nickname": "Health u1s1", "signature": "", "verified": false, "createTime": 1749021020, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 2668, "followingCount": 9, "heart": 60200, "heartCount": 60200, "videoCount": 137, "diggCount": 0, "friendCount": 5}}
- @wellnesswelfare: {"statusCode": 0, "statusMsg": "", "uniqueId": "wellnesswelfare", "nickname": "wellness welfare", "signature": "Healthy Living, Happy Vibes 🌼🤍", "verified": false, "createTime": 1745426690, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://www.facebook.com/share/18nAzSKPM4/", "isOrganization": 0, "stats": {"followerCount": 2508, "followingCount": 0, "heart": 53500, "heartCount": 53500, "videoCount": 381, "diggCount": 0, "friendCount": 0}}
- @chad_wellness: {"statusCode": 0, "statusMsg": "", "uniqueId": "chad_wellness", "nickname": "Chad.wellness", "signature": "Wellness tips your Dr. won't tell you\nFix your sh!t naturally", "verified": false, "createTime": 1744926943, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 214, "followingCount": 0, "heart": 2516, "heartCount": 2516, "videoCount": 82, "diggCount": 0, "friendCount": 0}}
- @ai_slop_merch: {"statusCode": 0, "statusMsg": "", "uniqueId": "ai_slop_merch", "nickname": "AI SLOP MERCH", "signature": "suq1y2-we.myshopify.com \n· extremely online shirts \n· $19.99", "verified": false, "createTime": 1783613719, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 0, "followingCount": 0, "heart": 0, "heartCount": 0, "videoCount": 3, "diggCount": 0, "friendCount": 0}}
- @leyaloveproducts: {"statusCode": 0, "statusMsg": "", "uniqueId": "leyaloveproducts", "nickname": "leya 🩶", "signature": "cutie patooties", "verified": false, "createTime": 1712440167, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 766, "followingCount": 991, "heart": 2793, "heartCount": 2793, "videoCount": 2, "diggCount": 0, "friendCount": 470}}


---
# RUN 2 (retry, 2026-09-25): WebSearch sweep actually executed

## Method
- All 15 required WebSearch queries plus 25 variants were run via the WebSearch tool (budget hit 200/200 again after ~40 queries; remaining lookups via WebFetch, r.jina.ai, DuckDuckGo helper `./dsearch.sh`, NexLev YouTube tools, `./tt_profile.sh`, `./tt_video.sh`).
- TikTok /discover pages no longer ship video items in their SSR JSON (only `webapp.kap-detail` shell) → discover scraping yielded nothing this run (raw: research/sweep/disc_faceless_ai_examples.html).
- Confirmed again: the big 2026 press wave (WSJ 2026-07-15 "AI Videos Are Flooding TikTok Shop", Business Insider 2026-07-20, eMarketer, The Keyword, Affiverse, Affnext, Shopifreaks, YPulse, AI Weekly, Carusele, Raisink, Veonib, E&P) names almost no handles. Only the Independent/AOL syndication of WSJ names two creators (Daria Simhony, Kiya Chanel). Trade/vendor blogs (Krafie, shortformnation, LitCommerce, percify, clipcat, syntopia, creatorev, influencers-time) use anonymised "$174K / $370K monthly GMV" accounts.

## WebSearch log (run 2) – query → handle-bearing hits
| Query | Handle-bearing result |
|---|---|
| AI TikTok Shop affiliate | emarketer (no handles); Medium "ShopReel AI" (403); krafie (anonymised $174K/$370K GMV accounts) |
| AI influencer TikTok Shop | thekeyword.co 2026-07-22 (no handles); tiktok.com/discover pages (no SSR data) |
| AI UGC TikTok Shop | vendors only (Creatify, Tagshop, CreateUGC, videoai.me) |
| faceless TikTok Shop | guides only (faceless.my, Medium J. Levitt) |
| TikTok Shop affiliate automation | vendor/bots (Reacher, Euka, Cruva, Rewarx, GitHub outreach bot) |
| AI avatar TikTok affiliate | affiversemedia (no handles); syntopia AI live hosts |
| TikTok Shop case study AI | Medium moneytent "$35k … starts with an AI video" (403; jina: no handle) |
| TikTok Shop affiliate earnings AI | YouTube 3Axh5s_iUyA (Patryk Marketer → @patrykmarketer) |
| AI generated TikTok product videos | vendors (Viggle, Renderforest, Creatify, Pippit, CreatOK) |
| virtual influencer TikTok Shop | generic (Miquela/Shudu/Imma – not shop sellers) |
| faceless TikTok affiliate | guides (Medium Simoliunas/Levitt, ClickBank) |
| TikTok Shop AI videos | YouTube a-INhZE9aII (Isa does AI, Higgsfield) & lStctO8yakY (Janson Smith) – educators, no seller handle |
| AI slop TikTok Shop | 404 Media Rosabella; SAN "AI slop shop" (pro-war disinfo, 30 % of accounts pivot to products, no handles); Futurism |
| AI UGC creator account TikTok example | @alex.prompt (already listed) |
| TikTok Shop AI avatar account @ | tiktok.com/@zachbtts/video/7606377842565303574 → @zachbtts |
| "tiktok.com/@" AI avatar TikTok Shop affiliate earning | goodreads blog (Sabri Suby podcast) → @electricfinger0 |
| Business Insider … synthetic avatars power washers | AOL/Independent syndication of WSJ → Kiya Chanel (@phicsbykiya, @earthtewkiya), @dariasimhony |
| "AI-generated" TikTok Shop … fake doctor | Science Feedback Feb 2026 → @wellnesstips66, @healthytips86, @health.tips.88, @wellness6868, @healthvibes888, @kellycruz_67 |
| site:tiktok.com "#aiugc" "tiktokshop" | tiktok.com/@shedoesai/video/7540652157427715351 → @shedoesai |
| "AI twin" TikTok Shop … | tiktok.com/@lifesrad/video/7630878408733396255 (human affiliate complaining about "AI remix") |
| site:x.com "TikTok Shop" AI avatar affiliate | x.com/drewecom (Andrew, "96k in profit last month … ai avatars", ReelFarm) – TikTok handle not found |
| "AI influencer" TikTok Shop "made" sales "first month" | x.com/maverickecom article (Noah Frydberg → @noahfrydberg) |
| Media Matters … | @wellnesswelfare / Holistic Health Finds (already listed) |
| Kalodata AI … / Arcads OR HeyGen … / "digital twin" … / UK … BBC OR Guardian | no handles |

## New candidates (run 2)

### 20. @phicsbykiya (secondary: @earthtewkiya)  — Model B (realistic AI twin of a real creator, affiliate videos)  — US
- Source: WSJ 2026-07-15 via The Independent/AOL syndication https://www.aol.com/articles/brands-urge-tiktok-shop-creators-164209000.html (accessed 2026-09-25): "In May, creator Kiya Chanel used an AI version of herself to promote Selena Gomez's Rare Beauty products in affiliate videos … Chanel's video is marked by both the 'eligible for commission' and 'contains AI-generated media' labels … also promotes an ebook about using AI twins for TikTok Shop … did not respond to requests for comment." Rare Beauty: "does not work with AI creators or digital duplicates". Also https://www.affiversemedia.com/rare-beauty-ai-tiktok-shop-affiliate-videos/.
- Verified (tt_profile 2026-09-25): @phicsbykiya 20,300 followers · 422,700 likes · 586 videos · created 2021-11-18 · bio "creator & director of AfterDarkAngels & ICON · 1MILL+ views WORLDWIDE · Helping brands go viral with cinematic AI · Learn Ai - AUGUST COHORT". commerceUser false, ttSeller false.
- Verified videos (tt_video 2026-09-25): https://www.tiktok.com/@phicsbykiya/video/7642182226028858638 "Natural mug but the blush is carrying the entire look @Rare Beauty #rarebeauty #grwm" → aigcLabelType=2 (AI label), isECVideo=1, product anchor (type 35), 13 s, 1,738 plays, 13 likes, posted 2026-05-20. https://www.tiktok.com/@phicsbykiya/video/7642184174631210254 "literally obsessed @Rare Beauty #tiktokshop #rarebeauty" → aigcLabelType=2, isECVideo=1, product anchor, 13 s, 2,006 plays, 22 likes, 2026-05-20. → The WSJ-cited AI-twin affiliate posts are real, labelled, and low-reach (≈2K plays each).
- @earthtewkiya (handle as printed in the AOL/Independent piece): exists, same bio text, 5 followers · 12 likes · 27 videos · created 2026-09-22 → freshly created duplicate/backup account (Verified).

### 21. @electricfinger0  — Model D/H (faceless AI-voice + AI-image affiliate video; now dormant = failure/burn-out case)  — US
- Source: blog "This AI-Generated TikTok Video is Earning $1000/Day" (2024-07-11, mirrored on goodreads https://www.goodreads.com/author_blog_posts/24921803-this-ai-generated-tiktok-video-is-earning-1000-day , accessed 2026-09-25), based on Sabri Suby's MFM podcast segment: "@electricfinger0 … 11K followers … The video has racked up more than 5 million views in ~3 months and Kalodata estimates that it has earned $77.7K in commissions over a recent 30-day period … likely earned $270K+ total since publishing"; product "sketchy health supplement for men"; method: Kalodata → model top video → ElevenLabs voice + Midjourney images (all Claimed).
- Verified (2026-09-25): account exists, 13,500 followers · 0 likes · **0 videos** · ttSeller=true · bio "Block adult websites on iPhone and Android" · link Shamefull.io · created 2024-03-27. → All videos removed/hidden; account repurposed to promote an app. Video-level data no longer obtainable. Good "2024 winner, 2026 gone" datapoint.

### 22. @zachbtts  — Model G (UK affiliate/educator teaching AI-avatar TikTok Shop videos)  — UK
- Verified: 3,641 followers · 22,100 likes · 45 videos · created 2024-10-05 · bio "TikTok Shop Affiliate · £800k+ GMV" (Claimed by owner, not verifiable).
- Verified video https://www.tiktok.com/@zachbtts/video/7606377842565303574 (WebSearch title "Create Your Own AI Avatar for TikTok Shop"; caption "#ai #tiktokshopaffiliate #tts #ttsaffiliate"): 99 s, 23,500 plays, 1,100 likes, 1,170 saves, 21 comments, posted 2026-02-13; no AI label, no product anchor (tutorial, not a sales video).

### 23. @patrykmarketer  — Model G/C (operator: AI avatar + AI voice product clips riding GMV Max; also Krafie tool founder)  — US/PL
- Verified: 328 followers · 2,569 likes · 38 videos · created 2025-06-07 · commerceUser=true (category "Education & Training") · link Krafie.com.
- Claimed (YouTube https://www.youtube.com/watch?v=3Axh5s_iUyA "How I Made $13,000 In One Month With AI Videos On TikTok Shop Affiliate", 2026-05-04, 12,870 views, transcript saved research/yt_tx/patryk_3Axh5s_iUyA.txt): "I made $13,000 in GMV, which is equivalent to $2,000 in commission … all with AI videos"; "Last time I did it … total profit was like $200. So, now I basically 10x it"; "I spent about $100 on all of these AI videos"; "some videos got over 100,000 views. I think there's one that got 200,000 views"; strategy = "find a product that is spending money on ads … you're just playing this game of trying to be picked by GMV Max"; videos "7 to 9 seconds long"; switched from Sora 2 (shut down 2026-04-28 per him) to Kling 3 / Seedance 2, prompts via a custom Claude skill, custom avatar ("thicker girl … putting on these body trimmers", "Southern accent"); products: supplements, waist trainers/body shapers; text overlay "Oh my god, this is on sale". Selling account not named (videos shown on screen, not in transcript).
- Krafie blog (2026-04-03, https://krafie.com/blog/how-to-make-money-with-ai-on-tiktok-shop-affiliate-step-by-step-guide): anonymised "example account … $174,000 in monthly GMV, another about $370,000" (Claimed, unverifiable).

### 24. @shedoesai  — Model G/B (AI educator; AI-UGC affiliate tutorial sponsored by invideo)  — DK
- Verified: 219,200 followers · 1.6 M likes · 546 videos · created 2023-04-11 · nickname "Gunhild Johanne Reumert" · bio "Make AI work as you, not just for you".
- Verified video https://www.tiktok.com/@shedoesai/video/7540652157427715351 (2025-08-20): "How to become a TikTok shop affiliate without showing your face … insert into this AI video generator. You will instantly generate an AI UGC video … @invideo #aiugc #tiktokshop #tiktokaffiliate" → 57 s, 2,470 plays, 72 likes, 22 comments, 60 saves, no AI label, CapCut anchor only. Low reach vs 219K followers.

### 25. @noahfrydberg  — Model G (agency/educator selling "AI influencer" affiliate coaching)  — US
- Verified: 4,182 followers · 231,200 likes · 1,197 videos · created 2023-09-14 · bio "I scale 8 figure ecom brands with affiliates · 1B views, $1M+ Generated, 37K+ Creators · helping affiliates print with ai" · link go.maverickcreative.org.
- Claimed (X article https://x.com/maverickecom/article/2093366724401803582 "How to become a millionaire with AI influencers", WebSearch snippet; page itself 402): a student's AI influencer "made $10,000 in commission in their first full month (August)", "$1,570 in commission" in one week, "hair-growth brand with a stylist avatar". Student's TikTok handle not given → not publicly verifiable.

### 26. @health.tips.88 (+ removed sister accounts)  — Model H (AI "doctor" avatars impersonating real physicians; health-product funnel)  — US
- Source: Science Feedback, Feb 2026, https://science.feedback.org/beware-ai-generated-doctors-health-advice-tiktok/ (accessed 2026-09-25): 18 AI-doctor accounts found; @health.tips.88 "impersonated orthopedic surgeon Brad Weening"; @wellnesstips66 impersonated Paul Zalzal (linked FB/YT accounts); @healthytips86 impersonated Garth Davis ("analysis showed AI-generated speech"); @wellness6868 ("raw cacao and beetroot unclog arteries"); @healthvibes888 "hundreds of thousands of followers … two of the most popular videos … more than 14 million views"; @kellycruz_67 "more than seven million views". Motivation per article: engagement farming + selling "health products and e-books, shilajit".
- Verified (2026-09-25): @health.tips.88 exists – 10,000 followers · 30,000 likes · 101 videos · created 2019-07-10 · commerceUser false. All five others → statusCode 10221 (removed). TikTok Shop linkage: not publicly verifiable (no shop flags on the surviving account).

### 27. @lifesrad  — counter-example (human affiliate, 331,700 followers) — US
- Verified video https://www.tiktok.com/@lifesrad/video/7630878408733396255 (2026-04-20, 289 s, 111,700 plays, 11,700 likes, 1,919 comments): "…don't even get me started on the AI remix 😤 @TikTok Shop Creator #tiktokshopaffiliate" → human creator backlash against TikTok's AI remix of affiliate videos. Not an AI account; keep for narrative.

### Named in run 2 but no TikTok handle found
- Andrew "@drewecom" (X, 2025-03-07): "How I create the ai avatars that helped me make 96k in profit last month on tiktok shop. Shoutout to @_mattwelter for the software" (ReelFarm). TikTok @drewecom → 10221. Claimed only.
- "Isa does AI" (YouTube, 67K subs, https://www.youtube.com/watch?v=a-INhZE9aII 2026-07-15, 15,764 views): full Higgsfield workflow (GPT Image 2 character → Marketing Studio avatar+product slot from Amazon link → 26 modes/hooks/settings → Eleven v3 voice swap) for a patio umbrella; no account or results shown. TikTok @isadoesai → 10221.
- Janson Smith / Honest Brands (YouTube lStctO8yakY, 2026-03-22, 39,188 views): Kling + ElevenLabs "realistic AI ads" for TikTok Shop brands (seller-side, UK).
- Harry Chang (NZ, YouTube "This AI TikTok Shop Video Made Me $67,420", "How I print $51,000/month profit with AI influencers" – titles per AI Weekly https://aiweekly.co/alerts/rosabella-ai-doctor-supplement-videos-hit-fda-recall-lawsuit ; videos removed). Rosabella founder Luca Washenko: "paid out over $400,000 last month to creators" (Claimed).
- SAN 2026-06-15 (https://san.com/cc/how-an-ai-slop-shop-is-flooding-tiktok-with-pro-war-disinformation/): ">100 inauthentic TikTok accounts … some 30% later pivoted to promoting products" – no handles.
- Business Insider 2026-07-20 (via YPulse/Raisink/AI Weekly): AI influencer "using a power washer and propane torch to clean their driveway in seconds"; comment "Never seen green grass burn like that" → matches the @gardenmolly / @ttsemily7 / @vanover7 cluster already listed (candidates 6–8).

## Raw profile re-checks run 2 (tt_profile.sh, 2026-09-25)
- @phicsbykiya: {"statusCode": 0, "statusMsg": "", "uniqueId": "phicsbykiya", "nickname": "phicsbykiya", "signature": "creator & director of AfterDarkAngels🩸& ICON 🪩💅🏽\n✨1MILL+ views WORLDWIDE\n• Helping brands go viral with cinematic AI 🎥🖤\nLearn Ai - AUGUST COHORT ↓ 🖥️", "verified": false, "createTime": 1637216233, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://linktr.ee/kiyachanel", "isOrganization": 0, "stats": {"followerCount": 20300, "followingCount": 106, "heart": 422700, "heartCount": 422700, "videoCount": 586, "diggCount": 0, "friendCount": 36}}
- @earthtewkiya: {"statusCode": 0, "statusMsg": "", "uniqueId": "earthtewkiya", "nickname": "earthtewkiya", "signature": "creator & director of AfterDarkAngels💧 & ICON🌍💅\n\n🌉1MILL+ views WORLDWIDE\n\nHelping brands go viral with cinematic Al", "verified": false, "createTime": 1790093187, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 5, "followingCount": 58, "heart": 12, "heartCount": 12, "videoCount": 27, "diggCount": 0, "friendCount": 4}}
- @electricfinger0: {"statusCode": 0, "statusMsg": "", "uniqueId": "electricfinger0", "nickname": "Shamefull", "signature": "Block adult websites on iPhone and Android", "verified": false, "createTime": 1711495103, "region": null, "ttSeller": true, "commerceUserInfo": {"commerceUser": false}, "bioLink": "Shamefull.io", "isOrganization": 0, "stats": {"followerCount": 13500, "followingCount": 13, "heart": 0, "heartCount": 0, "videoCount": 0, "diggCount": 0, "friendCount": 1}}
- @zachbtts: {"statusCode": 0, "statusMsg": "", "uniqueId": "zachbtts", "nickname": "Zach TTS", "signature": "TikTok Shop Affiliate 🤝🏻\n£800k+ GMV 📈\n\n-", "verified": false, "createTime": 1728154532, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 3641, "followingCount": 58, "heart": 22100, "heartCount": 22100, "videoCount": 45, "diggCount": 0, "friendCount": 25}}
- @patrykmarketer: {"statusCode": 0, "statusMsg": "", "uniqueId": "patrykmarketer", "nickname": "patrykmarketer", "signature": "Try Krafie!", "verified": false, "createTime": 1749256201, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": true, "downLoadLink": {"android": "", "ios": ""}, "category": "Education & Training", "categoryButton": false}, "bioLink": "Krafie.com", "isOrganization": 0, "stats": {"followerCount": 328, "followingCount": 23, "heart": 2569, "heartCount": 2569, "videoCount": 38, "diggCount": 0, "friendCount": 1}}
- @shedoesai: {"statusCode": 0, "statusMsg": "", "uniqueId": "shedoesai", "nickname": "Gunhild Johanne Reumert", "signature": "🤖 | Make AI work as you, not just for you\n📧 | hello@shedoesai.com", "verified": false, "createTime": 1681212116, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "www.shedoesai.com", "isOrganization": 0, "stats": {"followerCount": 219200, "followingCount": 480, "heart": 1600000, "heartCount": 1600000, "videoCount": 546, "diggCount": 0, "friendCount": 142}}
- @noahfrydberg: {"statusCode": 0, "statusMsg": "", "uniqueId": "noahfrydberg", "nickname": "Noah Frydberg", "signature": "💎 I scale 8 figure ecom brands with affiliates \n🤳 1B views, $1M+ Generated, 37K+ Creators\n📲 helping affiliates print with ai👇", "verified": false, "createTime": 1694700549, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://go.maverickcreative.org/?utm_source=ntb", "isOrganization": 0, "stats": {"followerCount": 4172, "followingCount": 116, "heart": 231200, "heartCount": 231200, "videoCount": 1197, "diggCount": 0, "friendCount": 23}}
- @health.tips.88: {"statusCode": 0, "statusMsg": "", "uniqueId": "health.tips.88", "nickname": "Healthtips88", "signature": "", "verified": false, "createTime": 1562776444, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": null, "isOrganization": 0, "stats": {"followerCount": 10000, "followingCount": 10, "heart": 30000, "heartCount": 30000, "videoCount": 101, "diggCount": 0, "friendCount": 0}}
- @lifesrad: {"statusCode": 0, "statusMsg": "", "uniqueId": "lifesrad", "nickname": "Lifesrad", "signature": "✨syd✨ \n31 | pnw oregon 🏔️ \naffordable fashion•coffee•beauty•lifestyle\n💌 sydney@pdmediacollabs.com", "verified": false, "createTime": 1582737058, "region": null, "ttSeller": false, "commerceUserInfo": {"commerceUser": false}, "bioLink": "https://linktr.ee/Lifesradical", "isOrganization": 0, "stats": {"followerCount": 331700, "followingCount": 2147, "heart": 15300000, "heartCount": 15300000, "videoCount": 2100, "diggCount": 0, "friendCount": 438}}
- removed (10221): @wellnesstips66, @healthytips86, @wellness6868, @healthvibes888, @kellycruz_67, @drewecom, @isadoesai, @kiyachanel
