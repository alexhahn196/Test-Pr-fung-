export const meta = {
  name: 'ig-market-research',
  description: 'Parallel desk research: Instagram platform rules, affiliate/commerce, sponsors, trends, competitor lists, case studies, legal, cross-platform',
  phases: [
    { title: 'Research', detail: 'one agent per research question, sources saved to /quellen/' },
    { title: 'Verify', detail: 'adversarial check of key numeric claims' },
  ],
}

const Q = '/home/user/Test-Pr-fung-/instagram-interior-research/quellen'

const FINDINGS = {
  type: 'object',
  properties: {
    source_file: { type: 'string' },
    summary: { type: 'string', description: '10-25 bullet summary, German or English' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          claim: { type: 'string' },
          numbers: { type: 'string', description: 'exact numbers quoted from the source, or empty' },
          source_url: { type: 'string' },
          source_type: { type: 'string', enum: ['meta_primary', 'instagram_public', 'analytics_platform', 'company_primary', 'news_media', 'industry_report', 'blog_case_study', 'forum', 'other'] },
          source_date: { type: 'string' },
          status: { type: 'string', enum: ['VERIFIED', 'ESTIMATED', 'THIRD-PARTY ESTIMATE', 'UNKNOWN'] },
          relevance: { type: 'string' },
        },
        required: ['claim', 'source_url', 'source_type', 'status'],
      },
    },
    accounts_found: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          handle: { type: 'string' }, followers_text: { type: 'string' }, category: { type: 'string' }, source_url: { type: 'string' }, note: { type: 'string' },
        },
        required: ['handle'],
      },
    },
  },
  required: ['source_file', 'summary', 'findings'],
}

const COMMON = `You are a senior research analyst. Today is 2026-09-25. Use WebSearch and WebFetch (load via ToolSearch "select:WebSearch,WebFetch" if not loaded). Only report facts you actually saw in a source; quote numbers exactly and attach the source URL and date. Never invent numbers, accounts, or quotes. If you cannot verify something, mark it UNKNOWN or ESTIMATED. Prefer primary sources (Meta/Instagram newsroom, creators.instagram.com, about.instagram.com, transparency.meta.com, company program pages) over blogs. Label any income/revenue estimate from a third party as THIRD-PARTY ESTIMATE. Actively look for DISCONFIRMING evidence too (e.g. signs of saturation, AI backlash, policy risk) — the goal is not to confirm that AI interior content works. Do not log in anywhere or bypass paywalls/rate limits. Do at least 12-25 searches/fetches; go deep.
Write a thorough Markdown source note (German, but keep original English quotes) with sections: Fragestellung, Kernbefunde (bullets with inline source links + status tags), Zahlen-Tabelle, Widersprüche/Unsicherheiten, Quellenliste (URL, Titel, Datum, Quellentyp). Save it with the Write tool to the path given below. Then return the structured findings.`

const TASKS = [
  { key: 'platform', file: 'q01_instagram_platform_rules.md', prompt: `Research question: What do Meta/Instagram PRIMARY sources (2024–2026) say about how Reels are ranked and recommended, and what matters for a new faceless theme account posting AI-generated interior/architecture videos? Cover: (1) ranking signals named by Adam Mosseri / Instagram (watch time, sends/shares per reach, likes per reach, saves), (2) originality policy: downranking/removal of reposted or aggregator/unoriginal content from recommendations (2024-2026 changes), replacement of reposts with originals, watermarks from other platforms, (3) AI labeling: "AI info" label, C2PA/IPTC metadata detection, disclosure requirements for photorealistic AI video, any evidence of reach impact, (4) Recommendation eligibility / Account Status, (5) Trial Reels feature, (6) Reels length limits (3 minutes), Edits app, (7) posting frequency guidance from Mosseri, (8) product tags/Instagram Shopping changes (Shop tab removal, product tagging availability), link in bio (up to 5 links), link stickers, (9) creator monetization programs available to theme pages (subscriptions, gifts, bonuses, branded content tool / partnership ads), (10) any 2025-2026 statements about AI-generated content ("AI slop") in feeds. Save note to ${Q}/q01_instagram_platform_rules.md` },
  { key: 'affiliate', file: 'q02_furniture_affiliate_commerce.md', prompt: `Research question: Furniture / home-decor affiliate and social-commerce ecosystem relevant to an Instagram interior account (international, English). Cover: Amazon Associates & Amazon Influencer Program (home & furniture commission rates, current rate table, cookie window, storefront/"idea lists"), LTK (how it works for home creators, commission model, invite/eligibility), ShopMy (home brands, commission ranges), Wayfair affiliate (network + rate), Williams-Sonoma/West Elm/Pottery Barn, RH, Crate & Barrel/CB2, Article, Castlery, Burrow, Arhaus, Anthropologie Home, IKEA (does it have affiliate?), 1stDibs, Chairish, Etsy, Houzz, luxury brands (Minotti, B&B Italia, Poliform – do they run affiliate?). For each: network (Impact/Rakuten/CJ/Awin), commission %, cookie days, average order value if published. Also: "shop the look" tooling — visual search (Google Lens, Amazon Lens, Pinterest Lens, LTK AI), and specifically HOW an AI-generated interior (items that don't exist) can be monetized with "similar items" / "get the look" lists; examples of accounts or tools doing that (e.g. Interior AI, Spacely, Collov, ReimagineHome shop-the-look features). Find evidence on conversion rates / earnings per click for home category if any (label THIRD-PARTY ESTIMATE). Save note to ${Q}/q02_furniture_affiliate_commerce.md` },
  { key: 'sponsors', file: 'q03_sponsors_brand_deals.md', prompt: `Research question: Who sponsors Instagram interior/architecture/luxury-homes theme pages and AI visual creators, and at what rates? Cover: (1) furniture/lighting/decor brands running creator programs; (2) real-estate developers and luxury real-estate brokerages sponsoring content; (3) AI tool companies sponsoring AI creators (Midjourney? Krea, Freepik, Higgsfield, Kling, Runway, Pika, Luma, Leonardo, Magnific, Interior AI, RoomGPT, Spacely, Collov, ReimagineHome, Planner 5D, etc.) — find concrete evidence of paid partnerships/ambassador or affiliate programs and their terms; (4) hotel/travel brands; (5) typical rates for theme-page posts/shoutouts/story placements (CPM or per-post, by follower tier) from reputable reports (label THIRD-PARTY ESTIMATE); (6) whether brands avoid AI-generated content (brand-safety, "AI" backlash), any survey data. Save note to ${Q}/q03_sponsors_brand_deals.md` },
  { key: 'trends', file: 'q04_interior_trends_demand.md', prompt: `Research question: Demand and trend indicators for interior design / luxury homes / architecture content 2025–2026. Cover: Pinterest Predicts 2025 and 2026 (home/interior trends), Pinterest trends data, Google Trends-related articles (e.g. 'japandi', 'organic modern', 'quiet luxury', 'dark academia interior', 'warm minimalism', 'cozy rain bedroom', 'future home', 'AI interior design'), Houzz/Etsy/1stDibs trend reports 2026, Instagram hashtag volume figures quoted by reputable sources (#interiordesign, #luxuryhomes, #architecture, #homedecor), size of global furniture e-commerce and home-decor markets (industry reports), interest in AI interior design apps (downloads/users of Interior AI, RoomGPT, Homestyler AI, etc.). Also look for evidence of saturation / fatigue: articles on "AI slop" interior videos, audience backlash, declining engagement for theme pages. Save note to ${Q}/q04_interior_trends_demand.md` },
  { key: 'competitors', file: 'q05_competitor_lists.md', prompt: `Research question: Build the broadest possible list of relevant Instagram accounts across these groups: A classic interior theme pages, B luxury homes / luxury real estate pages, C architecture pages (e.g. archdaily, dezeen, designboom, amazing.architecture, architecture_hunter, archdigest, homeadore, designmilk), D AI architecture creators (e.g. hassanragab? manasbhatia? tim_fu? search), E AI interior creators/pages, F dream homes / future homes pages, G luxury lifestyle pages with strong interior share (e.g. luxury, luxurylistings, millionaire lifestyle pages), H small accounts with extreme reel views. Sources: third-party rankings (hafi.pro top lists: try https://hafi.pro/top/most-followed-instagram/<category> for categories like architecture, home-decor, real-estate, luxury, interior-design, design, ai; scrumball rankings; Feedspot lists e.g. 'luxury homes instagram accounts', 'architecture instagram accounts', 'AI art instagram accounts'; articles 'best AI architecture instagram accounts', 'AI interior design instagram accounts'), plus WebSearch queries of the form 'site:instagram.com <keyword>' whose result snippets often show follower counts (e.g. '1M followers'). Record EVERY handle you find with the follower count text exactly as shown and the source URL; aim for 120+ handles. Put ALL of them in accounts_found with category = one of A..H. Save note to ${Q}/q05_competitor_lists.md` },
  { key: 'casestudies', file: 'q06_ai_theme_page_case_studies.md', prompt: `Research question: Case studies and evidence about faceless/AI-generated Instagram theme pages in interior, architecture, luxury homes, dream homes, cozy rooms — growth stories, view counts, what formats worked, how long it took, how they monetize (prompt packs, Gumroad/Etsy digital products, courses, AI render services, virtual staging, B2B, brand deals, affiliate). Look for: creator interviews, Reddit/Indie Hackers/X/Medium posts, YouTube video descriptions, news articles about viral AI houses (e.g. 'AI-generated house goes viral', 'this house doesn't exist'), accounts like soothenests (cozy AI bedrooms, ~2M followers), luxury AI pages. Also look for FAILURES / negative evidence: AI theme pages that stalled, got flagged as unoriginal, or faced audience backlash. Every figure must be sourced; income figures = THIRD-PARTY ESTIMATE or self-reported. Save note to ${Q}/q06_ai_theme_page_case_studies.md` },
  { key: 'legal', file: 'q07_legal_ai_risk.md', prompt: `Research question: Legal and platform risks for an international (EU-based operator, English-language) Instagram account publishing AI-generated interior/architecture images and videos with affiliate links and sponsorships. Cover: EU AI Act Article 50 transparency/deepfake labeling obligations and their application dates (Aug 2026?), Instagram/Meta AI labeling rules, copyright status of AI outputs (US Copyright Office reports 2025, EU/Germany position), risk of outputs resembling copyrighted designs or real buildings/hotels/furniture designs (design rights, trademark e.g. using brand names like 'Aman', 'Four Seasons', designer furniture), right of publicity if people appear, misleading claims ('this $50M home in Dubai' when fictional) under consumer-protection / UWG, affiliate/advertising disclosure (FTC Endorsement Guides, EU/German 'Werbung' labeling rules, Instagram Paid Partnership tool), terms of use of major AI generators (commercial use rights: Midjourney, Runway, Kling, Higgsfield, Google Veo, OpenAI Sora), music licensing on Reels for business accounts (commercial audio library restrictions). Save note to ${Q}/q07_legal_ai_risk.md` },
  { key: 'crossplatform', file: 'q08_cross_platform_signals.md', prompt: `Research question: Cross-platform demand signals for AI luxury homes / AI interior / dream house / future architecture / cozy bedroom short-form content on YouTube Shorts and TikTok, as a proxy for what performs on Instagram Reels. Use the NexLev MCP tools (load via ToolSearch, e.g. "+NexLev search_shorts_niche_finder_channels", "select:mcp__NexLev__search_shorts_niche_finder_channels,mcp__NexLev__faceless_outliers_videos,mcp__NexLev__search_viral_videos_small_channels,mcp__NexLev__search_niche_finder_channels,mcp__NexLev__get_niche_overview") to find YouTube channels/shorts in these niches: query ideas 'AI generated luxury houses', 'dream house AI', 'luxury interior design shorts', 'future architecture AI', 'cozy bedroom rain ambience', 'luxury villa tour', 'AI tiny house', 'mansion tour'. Record channel names, subscribers, views, upload frequency, faceless/AI flags, outlier scores, estimated revenue (THIRD-PARTY ESTIMATE, NexLev) and top-performing video titles/topics. Note which sub-themes have many small channels with outsized views (outliers). Also WebSearch for TikTok evidence (viral AI house videos, view counts reported by media). Save note to ${Q}/q08_cross_platform_signals.md` },
  { key: 'formats', file: 'q09_reels_format_benchmarks.md', prompt: `Research question: Published benchmarks and studies (2024–2026) on Instagram Reels performance relevant to our planning: average reel views / reach rate by follower tier, engagement rate benchmarks for home/interior/design/real-estate categories, optimal reel length data, posting frequency studies (e.g. Buffer's 2M-post analysis on posting frequency and follower growth, Later, Hootsuite, Socialinsider, Metricool, Rival IQ benchmark reports), saves/shares as signals, hook/first-3-seconds retention data, trending audio vs original audio impact, carousel vs reel reach 2025-2026. Record exact numbers with sources and dates. Note methodology limitations. Save note to ${Q}/q09_reels_format_benchmarks.md` },
]

phase('Research')
const results = await pipeline(
  TASKS,
  t => agent(`${COMMON}\n\n${t.prompt}\nThe structured return's source_file must be ${Q}/${t.file}.`, { label: 'research:' + t.key, phase: 'Research', schema: FINDINGS }),
  (res, t) => {
    if (!res) return null
    const numeric = (res.findings || []).filter(f => f.numbers && f.numbers.trim()).slice(0, 12)
    if (!numeric.length) return { key: t.key, res, verify: null }
    return agent(`You are a skeptical fact-checker. Below are numeric claims extracted by another analyst, each with a source URL. For EACH claim, open the source URL with WebFetch (load via ToolSearch "select:WebFetch,WebSearch") and check whether the source actually states the number in that context. Default to NOT_CONFIRMED if you cannot find it. Do not use other sources to "rescue" a claim, but you may note a correct figure if the source shows a different one.\n\nClaims:\n${numeric.map((f, i) => `${i + 1}. ${f.claim} | numbers: ${f.numbers} | ${f.source_url}`).join('\n')}\n\nThen append a section '## Faktencheck (automatisiert)' to the file ${Q}/${t.file} (use Edit/Write; keep existing content) listing each claim with CONFIRMED / NOT_CONFIRMED / CORRECTED(<value>) and a one-line reason. Return JSON.`, {
      label: 'verify:' + t.key, phase: 'Verify',
      schema: { type: 'object', properties: { checks: { type: 'array', items: { type: 'object', properties: { idx: { type: 'integer' }, verdict: { type: 'string', enum: ['CONFIRMED', 'NOT_CONFIRMED', 'CORRECTED'] }, corrected_value: { type: 'string' }, reason: { type: 'string' } }, required: ['idx', 'verdict'] } } }, required: ['checks'] },
    }).then(v => ({ key: t.key, res, verify: v }))
  },
)
const out = results.filter(Boolean)
return out.map(o => ({
  key: o.key,
  file: o.res.source_file,
  n_findings: (o.res.findings || []).length,
  n_accounts: (o.res.accounts_found || []).length,
  verify: o.verify ? o.verify.checks.reduce((a, c) => { a[c.verdict] = (a[c.verdict] || 0) + 1; return a }, {}) : null,
}))
