export const meta = {
  name: 'ig-account-profiles',
  description: 'Deep profile of competitor accounts: bio, CTA, links, link-in-bio offers, monetization evidence, reel sample shortcodes',
  phases: [{ title: 'Profile', detail: '4 accounts per agent' }],
}
const OUT = '/home/user/Test-Pr-fung-/instagram-interior-research/data/raw/accounts'
const B = args.batch || 4
const items = args.handles
const batches = []
for (let i = 0; i < items.length; i += B) batches.push(items.slice(i, i + B))
log(`${items.length} accounts in ${batches.length} batches`)
const SCHEMA = { type: 'object', properties: { files: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } }, required: ['files'] }

function prompt(hs, want_sample) {
  return `You are a competitive-intelligence researcher profiling Instagram accounts in the interior / luxury homes / architecture / AI-visuals niche. Use only PUBLIC information. Never log in, never bypass rate limits or login walls, never curl instagram.com. NEVER invent facts or numbers: every field is either taken from a source you saw (with URL) or null/UNKNOWN.
Tools: WebSearch, WebFetch (load via ToolSearch "select:WebSearch,WebFetch"). Note: web-search result SUMMARIES can hallucinate numbers — only trust numbers that appear verbatim in a result title/snippet or a fetched page, and mark search-index numbers as ESTIMATED (index snapshot, date unknown).

Accounts: ${hs.join(', ')}

For EACH account:
1. Bio & link: WebSearch '"@<handle>" instagram' and 'site:instagram.com <handle>'. From Instagram result titles/snippets extract: display name, bio text (verbatim fragments), external link(s) shown, category, and follower/post counts as ESTIMATED. Also try WebFetch https://www.threads.com/@<handle> (public) for the bio if Instagram snippets lack it (label source).
2. Link-in-bio: if an external link (linktr.ee, beacons.ai, stan.store, lnk.bio, bio.site, campsite.bio, koji, shopmy, ltk, amazon.com/shop, website) is found or guessable (try https://linktr.ee/<handle> and https://beacons.ai/<handle> ONCE each only if nothing found), WebFetch it and list every offer: affiliate storefronts (Amazon, LTK, ShopMy, other), own shop/products, digital products (prompt packs, presets, e-books, courses, templates), services (interior design, AI renders, virtual staging, consulting), newsletter, app, Patreon/membership, contact for collaborations/brand deals (email or form), real-estate listings.
3. Monetization evidence: WebSearch '<handle> instagram paid partnership OR sponsored OR collab' and '<handle> gumroad OR etsy OR course OR prompts OR amazon storefront'. Record concrete evidence with URLs (e.g. captions tagging brands, 'Paid partnership' mentions, storefront pages). Do NOT estimate income; if a third-party site shows an income estimate, record it as THIRD-PARTY ESTIMATE with URL.
${want_sample ? `4. Reel sample: run 3 searches — 'site:instagram.com/reel <handle>', 'site:instagram.com <handle> reel', '"<display name>" instagram reel' — and collect up to 30 distinct reel/post shortcodes that belong to THIS account (URL pattern instagram.com/reel/<code>/ or instagram.com/<handle>/reel/<code>/ or /p/<code>/). Keep the result title text (often the caption start). Only include codes whose result title/URL clearly belongs to this account.` : ''}
5. Classify: account_type (theme_page | ai_creator | designer_studio | architect | real_estate | brand_manufacturer | contractor_trade | lifestyle_influencer | media_publication | education_course | other), content_mode (AI | real | mixed | 3d_render | unknown) with the evidence, niche focus (1 line), language, CTA pattern seen in bio/captions.

Write one strict-JSON file per account with the Write tool to ${OUT}/profile_<handle>.json :
{"handle":"...","collected_at":"2026-09-25","display_name":null,"bio":null,"bio_source":null,"external_links":[],"category":null,"followers_index_text":null,"posts_index_text":null,"index_source":null,"link_in_bio":{"url":null,"offers":[{"type":"affiliate_amazon|affiliate_ltk|affiliate_shopmy|affiliate_other|shop|digital_product|course|service|newsletter|app|membership|brand_contact|real_estate|other","label":"...","url":"..."}]},"monetization_evidence":[{"type":"...","evidence":"...","url":"...","status":"VERIFIED|ESTIMATED|THIRD-PARTY ESTIMATE"}],"brand_deals_seen":[],"account_type":"...","content_mode":"...","content_mode_evidence":"...","niche_focus":"...","language":"...","cta_pattern":"...","reel_sample":[{"shortcode":"...","title":"...","source_query":"..."}],"sources":["..."],"notes":"..."}
Validate each with python json.load. Return the list of files written.`
}

phase('Profile')
const res = await parallel(batches.map((b, i) => () => agent(prompt(b.map(x => x.h), true), { label: 'profile ' + b.map(x => x.h).join(','), phase: 'Profile', schema: SCHEMA })))
return { done: res.filter(Boolean).length, files: res.filter(Boolean).flatMap(r => r.files) }
