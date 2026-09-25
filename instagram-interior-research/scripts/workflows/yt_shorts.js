export const meta = {
  name: 'yt-shorts-proxy',
  description: 'Cross-platform proxy: sample YouTube Shorts (views, duration, titles) from interior/home AI channels via NexLev',
  phases: [{ title: 'Sample', detail: 'one agent per channel' }],
}
const OUT = '/home/user/Test-Pr-fung-/instagram-interior-research/data/raw/youtube'
const SCHEMA = { type: 'object', properties: { relevant: { type: 'boolean' }, n_shorts: { type: 'integer' }, n_details: { type: 'integer' }, file_written: { type: 'string' }, note: { type: 'string' } }, required: ['relevant', 'n_shorts', 'n_details', 'file_written'] }

function prompt(ch) {
  return `You collect public YouTube Shorts data for a market study (interior design / luxury homes / AI home content). NEVER invent numbers; record only tool outputs.
Channel: "${ch.name}" (YouTube channel id ${ch.id}).
Tools: load via ToolSearch "select:mcp__NexLev__youtube_channel_shorts,mcp__NexLev__youtube_video_details".
1. Call mcp__NexLev__youtube_channel_shorts with channel_id=${ch.id}, sort_by="popular" (1 page) and again with sort_by="newest" (1 page). Large outputs may be saved to a file — parse that file with python/jq. Collect every short: video_id, title, views text.
2. Relevance check: if fewer than half of the shorts are about interiors, rooms, houses, architecture, home transformations, cozy home ambience, hotels/villas or furniture, set relevant=false, still write the file with what you collected, and stop.
3. Otherwise call mcp__NexLev__youtube_video_details for up to 20 shorts: the 10 most-viewed from the popular list and the 10 most recent from the newest list (dedupe). Record duration (convert to seconds), publish date, views, likes, comments, title, and the first 200 chars of description.
Write strict JSON with the Write tool to ${OUT}/shorts_${ch.id}.json :
{"channel_id":"${ch.id}","channel_name":"${ch.name}","collected_at":"2026-09-25","source":"NexLev youtube_channel_shorts + youtube_video_details (THIRD-PARTY data provider)","relevant":true,"shorts":[{"video_id":"...","title":"...","views_text":"...","list":"popular|newest|both"}],"details":[{"video_id":"...","title":"...","duration_sec":0,"published":"YYYY-MM-DD","views":0,"likes":0,"comments":0,"description_200":"..."}]}
Validate with python json.load and fix until it parses. Return the summary.`
}

phase('Sample')
const res = await parallel(args.channels.map(ch => () => agent(prompt(ch), { label: 'yt ' + ch.name, phase: 'Sample', schema: SCHEMA })))
return res.map((r, i) => ({ ch: args.channels[i].name, ...(r || { failed: true }) }))
