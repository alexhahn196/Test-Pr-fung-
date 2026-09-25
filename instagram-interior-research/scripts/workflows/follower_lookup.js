export const meta = {
  name: 'ig-follower-lookup',
  description: 'Look up follower/post counts for discovered handles via public Instagram reel embed pages',
  phases: [{ title: 'Lookup', detail: 'embed page per handle' }],
}
const OUT = '/home/user/Test-Pr-fung-/instagram-interior-research/data/raw/accounts'
const FILE = args.file
const N = args.count
const tag = args.tag
const B = 22
const ranges = []
for (let i = 0; i < N; i += B) ranges.push([i, Math.min(N, i + B)])
log(`${N} handles in ${ranges.length} batches`)

const SCHEMA = { type: 'object', properties: { file_written: { type: 'string' }, ok: { type: 'integer' }, failed: { type: 'array', items: { type: 'string' } } }, required: ['file_written', 'ok', 'failed'] }

function prompt(a, b, id) {
  return `You transcribe public Instagram data. NEVER invent or estimate numbers. Use only the WebFetch tool for Instagram (load with ToolSearch "select:WebFetch"). Do not use curl on Instagram, do not bypass rate limits or login walls.

First get your items: run  python3 -c "import json;d=json.load(open('${FILE}'))[${a}:${b}];print('\\n'.join(x['h']+' | '+x['sc'] for x in d))"
(h = expected handle, sc = reel shortcode). You have ${b - a} items.

For each item, WebFetch https://www.instagram.com/reel/<sc>/embed/captioned/ with EXACTLY this prompt:
"Transcribe exactly as displayed: account handle, account display name, follower count text, posts count text, likes count text, comments count text, verified badge yes/no, and the first 200 characters of the caption. Write NOT SHOWN for anything missing. Do not round or paraphrase numbers."
Run up to 6 WebFetch calls in parallel. If a fetch fails (404/429/error), retry it once at the end; if it still fails, record the status. If the handle shown differs from the expected handle, record the shown handle and set handle_mismatch true.

Write ONE strict-JSON file with the Write tool to ${OUT}/followers_${tag}_${id}.json :
{"fetched_at":"2026-09-25","source":"instagram reel embed page","accounts":[{"handle":"<expected>","handle_shown":"<as shown>","handle_mismatch":false,"shortcode":"<sc>","url":"https://www.instagram.com/reel/<sc>/embed/captioned/","status":"ok|404|429|error","display_name":"...","followers_text":"<exact e.g. 547K>","posts_text":"<exact>","likes_text":"<exact>","comments_text":"<exact>","verified":"yes|no|unknown","caption_200":"..."}]}
Use null for NOT SHOWN values. Validate with: python3 -c "import json;print(len(json.load(open('${OUT}/followers_${tag}_${id}.json'))['accounts']))" and fix if it errors. Return the summary.`
}

phase('Lookup')
const res = await parallel(ranges.map(([a, b], i) => () => agent(prompt(a, b, String(i).padStart(2, '0')), { label: `lookup ${tag}#${i}`, phase: 'Lookup', schema: SCHEMA })))
const ok = res.filter(Boolean)
return { batches: ranges.length, done: ok.length, ok: ok.reduce((a, r) => a + r.ok, 0), failed: ok.flatMap(r => r.failed) }
