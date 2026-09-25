export const meta = {
  name: 'ig-topic-sweep-batches',
  description: 'Sweep given batches of Instagram /popular/ topic pages (args.batches = [{id, slugs}])',
  phases: [{ title: 'Sweep', detail: 'fetch topic pages' }],
}
const BASE = '/home/user/Test-Pr-fung-/instagram-interior-research/data/raw/topics'
const TOPIC_SCHEMA = {
  type: 'object',
  properties: {
    file_written: { type: 'string' },
    topics_ok: { type: 'integer' },
    topics_failed: { type: 'array', items: { type: 'string' } },
    reels_total: { type: 'integer' },
    related_topics: { type: 'array', items: { type: 'string' }, description: 'slugs of related topic links found on the pages (e.g. luxury-bedroom-wallpaper)' },
    notes: { type: 'string' },
  },
  required: ['file_written', 'topics_ok', 'topics_failed', 'reels_total', 'related_topics'],
}

function sweepPrompt(slugs, batchId) {
  return `You are a data collector for a market-research project on Instagram interior / luxury homes / architecture content. Your ONLY job is to transcribe public data exactly. NEVER invent, estimate, round, or "fill in" numbers, handles or shortcodes. If something is not on the page, leave it out.

Data source: Instagram's PUBLIC topic pages at https://www.instagram.com/popular/<slug>/ . These are public SEO pages (no login). Use the WebFetch tool (load it with ToolSearch "select:WebFetch" if needed). Do NOT use curl, do NOT try to bypass rate limits or login walls, do NOT spoof user agents.

Topics for this batch (${slugs.length}): ${slugs.join(', ')}

For EACH slug:
1. WebFetch https://www.instagram.com/popular/<slug>/ with this prompt (copy it exactly):
   "Transcribe EVERY reel/post card on this page, in order, one per line, in the format: @handle | shortcode | views | caption-first-150-chars . Copy the view count exactly as displayed (e.g. 3.7M, 508K, 9,527). If a value is not shown write NA. Do not skip any card. Do not summarize. After the list, write 'RELATED:' followed by every related-topic link slug (the part after /popular/) shown on the page, comma-separated. Also state the page title and any total count of reels shown (e.g. '700+ reels')."
2. Issue several WebFetch calls in parallel (up to 6 at once) to go faster.
3. If a page returns 404, try ONE variant slug (e.g. plural form, or add '-design' / '-ideas'), and record the variant used. If a page returns 429 (rate limit), wait by doing other slugs first, then retry it ONCE at the end; if still failing, record status '429'. Never retry more than once.

Then write ONE JSON file with the Write tool to: ${BASE}/batch_${batchId}.json
Format (strict JSON, UTF-8):
{
  "batch": "${batchId}",
  "fetched_at": "2026-09-25",
  "topics": [
    {
      "slug": "<slug requested>",
      "slug_used": "<slug actually fetched>",
      "url": "https://www.instagram.com/popular/<slug_used>/",
      "status": "ok" | "404" | "429" | "error",
      "page_title": "<as shown or null>",
      "total_reels_label": "<e.g. '700+ reels' or null>",
      "reels": [ { "handle": "<without @>", "shortcode": "<code>", "views_text": "<exact as shown or NA>", "caption": "<first 150 chars>" } ],
      "related_topics": ["<slug>", ...]
    }
  ]
}
Rules: handles lowercase without '@'. Keep captions as shown (any language) but strip line breaks. Escape quotes properly so the file is valid JSON. After writing, run: python3 -c "import json;d=json.load(open('${BASE}/batch_${batchId}.json'));print(sum(len(t['reels']) for t in d['topics']))" to validate the JSON parses; fix and rewrite if it fails.

Return the structured summary (file path, counts, failed slugs, and the union of related topic slugs).`
}

phase('Sweep')
const res = await parallel(args.batches.map(b => () =>
  agent(sweepPrompt(b.slugs, b.id), { label: 'sweep ' + b.id, phase: 'Sweep', schema: TOPIC_SCHEMA })
))
const ok = res.filter(Boolean)
return { done: ok.length, reels: ok.reduce((a, r) => a + (r.reels_total || 0), 0), failed: ok.flatMap(r => r.topics_failed || []), related: [...new Set(ok.flatMap(r => r.related_topics || []))] }
