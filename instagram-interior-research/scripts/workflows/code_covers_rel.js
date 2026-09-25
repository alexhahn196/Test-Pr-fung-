export const meta = {
  name: 'ig-cover-coding-reliability',
  description: 'Per reel: public reel-page metadata + cover-frame download + visual/caption codebook coding by a multimodal agent',
  phases: [{ title: 'Code', detail: '12 reels per agent' }],
}
const ROOT = '/home/user/Test-Pr-fung-/instagram-interior-research'
const OUT = ROOT + '/data/raw/reliability'
const COVERS = '/tmp/claude-0/-home-user-Test-Pr-fung-/e932e7d2-1a29-5a3a-8ed1-4923529db247/scratchpad/covers'
const CODEBOOK = ROOT + '/scripts/cover_codebook.md'
const FILE = args.file
const N = args.count
const tag = args.tag
const B = args.batch || 12
const start = args.start || 0
const ranges = []
for (let i = start; i < N; i += B) ranges.push([i, Math.min(N, i + B)])
log(`${N - start} reels in ${ranges.length} batches (tag ${tag})`)

const SCHEMA = { type: 'object', properties: { file_written: { type: 'string' }, meta_ok: { type: 'integer' }, coded_visual: { type: 'integer' }, failed: { type: 'array', items: { type: 'string' } } }, required: ['file_written', 'meta_ok', 'coded_visual', 'failed'] }

function prompt(a, b, id) {
  return `You are a careful research coder in a study of Instagram interior/architecture reels. NEVER invent numbers or content; only record what tools return or what you actually see in the image.

Setup:
- Items: python3 -c "import json;d=json.load(open('${FILE}'))[${a}:${b}];print('\\n'.join(x['sc']+' | '+x['h'] for x in d))"   (sc = shortcode, h = expected handle). ${b - a} items.
- Codebook: cat ${CODEBOOK}   (read it fully; use exactly its keys and allowed values)
- mkdir -p ${COVERS}

For EACH reel:
1. WebFetch https://www.instagram.com/reel/<sc>/embed/captioned/ (load WebFetch via ToolSearch "select:WebFetch") with EXACTLY this prompt:
"Transcribe exactly as displayed: account handle, account display name, follower count text, posts count text, likes count text, comments count text, whether the post is a video/reel (play icon or 'Watch on Instagram') or a photo/carousel, and the FULL caption verbatim including all hashtags (do not summarize hashtags). Then output the URL of the main post image (the post media, NOT the profile picture) verbatim, character for character, on its own line prefixed with OGIMAGE: . Write NOT SHOWN for anything missing. Do not round or paraphrase numbers."
   Run up to 6 WebFetch calls in parallel. If one returns 429/error, retry once at the end. If the embed says the post is broken/removed, set meta_status "removed" and skip the reel (no coding).
2. Download the cover: curl -sS --max-time 30 -o ${COVERS}/<sc>.jpg '<OGIMAGE url>' -w '%{http_code}\\n' (quote the URL in single quotes; HTML entities like &amp; must be turned into &). Check it is a JPEG (file ${COVERS}/<sc>.jpg). If it fails (403 = URL was mangled), WebFetch https://www.instagram.com/reel/<sc>/ asking only for the og:image URL verbatim and try that once. If still failing, set visual_status "no_cover" and code only the caption-derived fields.
3. LOOK at the cover with the Read tool (Read ${COVERS}/<sc>.jpg) and code every visual field of the codebook from what you actually see. Code caption-derived fields from the caption.
Do not curl instagram.com pages, only the CDN image URL. Do not bypass any login wall or rate limit.

Write ONE strict-JSON file with the Write tool to ${OUT}/cover_${tag}_${id}.json :
{"coded_at":"2026-09-25","coder":"cover-v2-embed","reels":[{"shortcode":"<sc>","expected_handle":"<h>","meta_status":"ok|removed|429|404|error","source_url":"https://www.instagram.com/reel/<sc>/embed/captioned/","handle":"<as shown>","display_name":"...","followers_text":"<exact>","posts_text":"<exact>","media_type":"reel|photo|carousel|unknown","likes_text":"<exact>","comments_text":"<exact>","caption":"<full caption>","visual_status":"ok|no_cover","code":{ <all codebook keys> }}]}
Use null for NOT SHOWN. Validate: python3 -c "import json;d=json.load(open('${OUT}/cover_${tag}_${id}.json'));print(len(d['reels']), sum(1 for r in d['reels'] if r.get('visual_status')=='ok'))" and fix until it parses. Return the summary.`
}

phase('Code')
const res = await parallel(ranges.map(([a, b], i) => () => agent(prompt(a, b, String(i + Math.floor(start / B)).padStart(3, '0')), { label: `cover ${tag}#${i}`, phase: 'Code', schema: SCHEMA })))
const ok = res.filter(Boolean)
return { batches: ranges.length, done: ok.length, meta_ok: ok.reduce((s, r) => s + r.meta_ok, 0), coded_visual: ok.reduce((s, r) => s + r.coded_visual, 0), failed: ok.flatMap(r => r.failed) }
