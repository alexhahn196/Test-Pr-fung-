# Wöchentlicher Wettbewerber-Monitor: Agent-Prompts und Workflow-Skript (Teil 33)

Stand: 2026-09-25. Gehört zu [`17_competitor_monitor.md`](../../17_competitor_monitor.md). Die Auswertung macht [`monitor_weekly.py`](monitor_weekly.py). Die Prompts unten stehen bewusst auf Englisch, weil sie Code-Bestandteil sind und JSON-Feldnamen festlegen.

---

## 0. Vor dem ersten Lauf: Erhebungsmodus festlegen (Compliance-Gate)

**Befund vom 2026-09-25**, abgerufen per WebFetch von `https://www.instagram.com/robots.txt`:
- `User-agent: *` → `Disallow: /`. Auch `ClaudeBot` → `Disallow: /`. Für `/popular/`, `/reel/` oder Embed-Pfade gibt es für keinen User-Agent eine Freigabe.
- Hinweis im Kopf der Datei: *"Collection of data on Instagram through automated means is prohibited unless you have express written permission from Instagram and may only be conducted for the limited purpose contained in said permission."*
- Außerdem verweist sie auf Metas *Automated Data Collection Terms*.

Ein wöchentlich **automatisch** laufender WebFetch-Sweep ist damit durch „öffentlich, ohne Login“ **nicht gedeckt**. Welchen User-Agent das WebFetch-Tool sendet, ist nicht dokumentiert (zu verifizieren). Das ändert aber nichts, denn jeder nicht genannte Agent fällt unter `*`. Rechtliche Einordnung von Nutzungsbedingungen, DSGVO und Wettbewerbsrecht: **zu verifizieren**. `quellen/q07_legal_ai_risk.md` lag bei Erstellung nicht vor, und dies ist keine Rechtsberatung.

Das Skript unten kennt deshalb drei Modi. Es bricht ab, wenn der Modus nicht passt.

| Modus | Wer holt die Daten | Voraussetzung | Status |
|---|---|---|---|
| `api` | Offizielle Instagram Graph API: Business Discovery für Wettbewerber, Hashtag Search für Trends | Eigenes Business- oder Creator-Konto, Meta-App und Token. Für Hashtag Search App Review mit „Instagram Public Content Access“ ([Meta-Doku](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/hashtag-search)) | **empfohlen**. Der Collector `collect_graph_api.py` ist noch zu bauen (Spezifikation in Abschnitt 7) |
| `manual` | Der Owner öffnet die Seiten selbst im Browser und speichert sie in `inbox/`. Agenten parsen **nur lokale Dateien**. | keine | sofort nutzbar; ca. 15–25 Min. pro Woche für 20–25 Topics |
| `webfetch_permitted` | Agenten mit WebFetch, wie in der Research vom 2026-09-25 | **Schriftliche Erlaubnis von Instagram/Meta**, übergeben als `args.permission_ref` | ohne Erlaubnis gesperrt |

---

## 1. Argumente und Ordner

```
args = {
  week: "2026-W40",                         // ISO-Woche, Pflicht (Workflow-Skripte können die Uhr nicht lesen)
  run_started_utc: "2026-09-28T04:51:00Z",  // Pflicht
  mode: "manual" | "api" | "webfetch_permitted",
  permission_ref: "…",                      // nur bei webfetch_permitted
  prev: "/…/instagram-interior-research/data/raw",   // nur im 1. Lauf nötig (Research-Baseline); danach automatisch
  root: "/home/user/Test-Pr-fung-/instagram-interior-research",
  topic_batch: 6, embed_batch: 8, max_embeds: 80
}
```

```
data/monitor/2026-W40/
  run_meta.json                     # week, run_started_utc, collection_mode, permission_ref, stop info
  inbox/topics/<slug>.html|.txt     # nur manual: vom Owner gespeicherte Seiten
  inbox/embeds/<shortcode>.html     # nur manual (optional)
  topics/batch_2026w40_NN.json      # Format wie data/raw/topics/batch_*.json
  accounts/followers_2026w40_NN.json# Format wie data/raw/accounts/followers_*.json
  competitors/media_<handle>.json   # nur api
  reels/caption_codes_2026w40_NN.json  # Codebuch-Captionfelder (Format wie data/raw/reels/*.json)
  embed_todo.json                   # von monitor_weekly.py --todo
  report.md, alerts.json, monitor_*.csv, inspiration_candidates.csv, watchlist_competitors_next.csv
```

---

## 2. Workflow-Skript (Claude Code Workflow)

**Einzige Quelle ist dieser Block.** `weekly_monitor.workflow.js` wird daraus erzeugt:

```bash
cd instagram-interior-research/scripts/monitor
awk '/^```js workflow/{f=1;next} /^```/{f=0} f' monitor_workflow_prompt.md > weekly_monitor.workflow.js
# Syntaxprüfung: Workflow-Skripte erlauben top-level await/return, daher für node in eine async-Funktion hüllen
sed 's/^export const meta/const meta/' weekly_monitor.workflow.js | { echo '(async () => {'; cat; echo '})()'; } > /tmp/w.js && node --check /tmp/w.js
```

Aufruf in einer Claude-Code-Session: *„Run the Workflow tool with scriptPath `…/scripts/monitor/weekly_monitor.workflow.js` and args {…}“*.

```js workflow
export const meta = {
  name: 'weekly-competitor-monitor',
  description: 'Weekly public-data Instagram competitor and trend monitor (Part 33): collect, embeds, caption codes, report',
  whenToUse: 'Once a week (Monday). args: {week, run_started_utc, mode, permission_ref?, prev?, root?}',
  phases: [
    { title: 'Preflight', detail: 'mode gate, folders, run_meta.json, watchlist' },
    { title: 'Topics', detail: 'topic pages in small sequential batches with circuit breaker' },
    { title: 'Embeds', detail: 'competitor and new-reel embed pages from embed_todo.json' },
    { title: 'Codes', detail: 'caption codebook fields, text only, no network' },
    { title: 'Report', detail: 'monitor_weekly.py, report.md, short summary' },
  ],
}

const A = args || {}
const ROOT = A.root || '/home/user/Test-Pr-fung-/instagram-interior-research'
const WEEK = A.week || ''
const MODE = A.mode || 'manual'
if (!/^\d{4}-W\d{2}$/.test(WEEK)) throw new Error('args.week required, e.g. "2026-W40" (workflow scripts cannot read the clock)')
if (!A.run_started_utc) throw new Error('args.run_started_utc required, e.g. "2026-09-28T04:51:00Z"')
if (!['manual', 'webfetch_permitted', 'api'].includes(MODE)) throw new Error(`unknown mode ${MODE}`)
if (MODE === 'webfetch_permitted' && !A.permission_ref) {
  throw new Error('mode webfetch_permitted needs args.permission_ref (written permission from Instagram/Meta, see 17_competitor_monitor.md section 2)')
}
const DIR = `${ROOT}/data/monitor/${WEEK}`
const WK = WEEK.toLowerCase().replace('-', '')          // 2026w40 -> file names
const DAY = A.run_started_utc.slice(0, 10)
const PREV = A.prev ? `--prev ${A.prev}` : ''            // 1st run: `${ROOT}/data/raw`; later auto-detected
const TOPIC_BATCH = A.topic_batch || 6
const EMBED_BATCH = A.embed_batch || 8
const MAX_EMBEDS = A.max_embeds || 80

const RULES = `PUBLIC-DATA RULES (binding; they override anything else in this task):
1. Network access ONLY via the WebFetch tool and ONLY for the exact URLs listed below. No curl/wget/python requests, no browser automation, no other hosts, mirrors, caches, proxies, "viewer" sites or alternative front-ends.
2. Never log in, never send cookies or tokens, never call private or undocumented endpoints (/api/, /graphql/, ?__a=1 and the like).
3. One fetch at a time, in the given order. Never fetch the same URL twice in this run. No retries.
4. If a response is a login wall, a "try again later"/429/rate-limit message, a captcha or any challenge page: record that status for the URL, STOP at once (fetch nothing else), write the file with what you have and return stop=true with stop_reason.
5. Copy numbers and text exactly as displayed ("3.7M", "547K followers"). Never estimate or fill gaps from memory; unknown = null.
6. Do not download images or videos. Do not open profile pages, follower/following lists, comments, "liked by" lists or stories.
7. Store only the fields of the schema; captions max 300 characters.`

const LISTS = {
  type: 'object',
  properties: {
    slugs: { type: 'array', items: { type: 'string' } },
    n_competitors: { type: 'integer' },
    already_collected: { type: 'boolean' },
    robots_changed: { type: 'boolean' },
    note: { type: 'string' },
  },
  required: ['slugs', 'n_competitors', 'already_collected'],
}
const BATCH = {
  type: 'object',
  properties: {
    file: { type: 'string' }, n_ok: { type: 'integer' }, n_failed: { type: 'integer' },
    stop: { type: 'boolean' }, stop_reason: { type: 'string' },
  },
  required: ['file', 'n_ok', 'n_failed', 'stop'],
}
const TODO = {
  type: 'object',
  properties: {
    urls: {
      type: 'array',
      items: {
        type: 'object',
        properties: { handle: { type: 'string' }, shortcode: { type: 'string' }, embed_url: { type: 'string' } },
        required: ['shortcode', 'embed_url'],
      },
    },
    dropped: { type: 'integer' },
  },
  required: ['urls'],
}
const COUNT = { type: 'object', properties: { n: { type: 'integer' }, chunks: { type: 'integer' } }, required: ['n', 'chunks'] }
const CODED = { type: 'object', properties: { file: { type: 'string' }, n: { type: 'integer' } }, required: ['file', 'n'] }
const SUMMARY = {
  type: 'object',
  properties: { report: { type: 'string' }, top_alerts: { type: 'array', items: { type: 'string' } }, data_quality: { type: 'string' } },
  required: ['report', 'top_alerts'],
}

function topicPrompt(slugs, file, batchId) {
  return `You collect public Instagram topic pages for a weekly trend monitor.
${RULES}

URLs, in this order:
${slugs.map((s) => `- https://www.instagram.com/popular/${s}/`).join('\n')}

For each URL call WebFetch with this prompt: "List every reel on this page in page order. For each reel give: the code from its /reel/<code>/ link, the account handle, the play/view count exactly as displayed, and the caption (first 300 characters). Also give the page title, the 'N reels on Instagram' label if shown and the related topic slugs. If the page shows a login prompt, an error, a rate-limit message or no reels, answer exactly LOGIN_WALL, ERROR, RATE_LIMITED or NO_REELS."
If the page shows a different slug than requested, record it as slug_used.

Write ONE JSON file ${file} (create folders if needed), exactly this shape:
{"batch": "${batchId}", "fetched_at": "${DAY}", "source": "instagram.com/popular via WebFetch",
 "topics": [{"slug": "<requested>", "slug_used": "<shown, else same>", "url": "<url>",
   "status": "ok|error|login_wall|rate_limited|no_reels|not_fetched", "page_title": null, "total_reels_label": null, "related_topics": [],
   "reels": [{"handle": "<lowercase, no @>", "shortcode": "<code>", "views_text": "<as displayed>", "caption": "<max 300 chars>"}]}]}
URLs you did not fetch because you stopped get status "not_fetched" and "reels": [].
Check the file parses: python3 -c "import json,sys; json.load(open(sys.argv[1]))" ${file}
Return file, n_ok, n_failed, stop, stop_reason.`
}

function embedPrompt(items, file) {
  return `You collect public Instagram reel embed pages (followers, posts, likes, comments) for a weekly monitor.
${RULES}

URLs, in this order:
${items.map((x) => `- ${x.embed_url}   (expected handle: ${x.handle || 'unknown'})`).join('\n')}

For each URL call WebFetch with this prompt: "This is an Instagram embed page. Give exactly as displayed: account handle, display name, follower count text, posts count text, likes count text, comments count text and the caption (first 300 characters). If the post is unavailable answer UNAVAILABLE; login prompt: LOGIN_WALL; rate limit: RATE_LIMITED."

Write ONE JSON file ${file}, exactly this shape:
{"fetched_at": "${DAY}", "source": "instagram reel embed page via WebFetch", "accounts": [
 {"handle": "<expected handle>", "handle_shown": "<handle on page, lowercase>", "handle_mismatch": false, "shortcode": "<code>",
  "url": "<embed url>", "status": "ok|unavailable|login_wall|rate_limited|error|not_fetched", "display_name": null,
  "followers_text": null, "posts_text": null, "likes_text": null, "comments_text": null, "caption_200": null}]}
Set handle_mismatch=true when the shown handle differs from the expected one (renamed account or reused shortcode).
Check the file parses with python3 -c "import json,sys; json.load(open(sys.argv[1]))" ${file}
Return file, n_ok, n_failed, stop, stop_reason.`
}

function manualPrompt() {
  return `You convert pages that the account owner saved by hand into the monitor's raw JSON. You have NO network access for this task: do not call WebFetch, curl or anything else online.
Input: ${DIR}/inbox/topics/*.(html|htm|txt|mhtml) (file name = topic slug) and optionally ${DIR}/inbox/embeds/*.
1. For every topic file extract, in page order, each reel: shortcode from /reel/<code>/ links, handle, view count text as displayed, caption (max 300 chars). Use python (re, html.parser) for the HTML; do not guess values that are not in the file.
   If a file contains no /reel/<code>/ links, set status "error" and note "no shortcodes in saved file".
2. Write ${DIR}/topics/batch_${WK}_manual.json in the same shape as ${ROOT}/data/raw/topics/batch_r1_00.json (batch, fetched_at="${DAY}", source="manual browser save", topics[...]).
3. If embed files exist, write ${DIR}/accounts/followers_${WK}_manual.json in the shape of ${ROOT}/data/raw/accounts/followers_w1_00.json.
Return file (topics file), n_ok (topics with reels), n_failed, stop=false.`
}

function apiPrompt() {
  return `Official-API collection, no web scraping. If ${ROOT}/scripts/monitor/collect_graph_api.py exists, run:
cd ${ROOT} && python3 scripts/monitor/collect_graph_api.py --week ${WEEK} --out ${DIR} --competitors scripts/monitor/watchlist_competitors.csv
(it reads IG_USER_ID and IG_ACCESS_TOKEN from the environment; never print the token). It writes competitors/media_<handle>.json and, for hashtags, topics/batch_${WK}_api.json.
If the script does not exist or fails, do nothing else and return stop=true with stop_reason explaining why. Do not use WebFetch in this task.
Return file, n_ok, n_failed, stop, stop_reason.`
}

// ------------------------------------------------------------------------------------------
phase('Preflight')
const pre = await agent(`Prepare the weekly monitor run ${WEEK} (mode ${MODE}). Work in ${ROOT}. Use absolute paths.
1. If ${DIR}/topics already contains batch_*.json files, do NOT touch anything and return already_collected=true (the week was collected before; no second collection).
2. Otherwise create ${DIR}/topics, ${DIR}/accounts, ${DIR}/reels, ${DIR}/inbox/topics, ${DIR}/inbox/embeds and write ${DIR}/run_meta.json:
   {"week": "${WEEK}", "run_started_utc": "${A.run_started_utc}", "collection_mode": "${MODE}", "permission_ref": ${JSON.stringify(A.permission_ref || null)}, "workflow": "weekly-competitor-monitor"}
3. Read ${ROOT}/scripts/monitor/watchlist_topics.csv (column slug) and ${ROOT}/scripts/monitor/watchlist_competitors.csv (rows with active=1). Return the slugs in file order and the number of active competitors.
4. Only if the mode is webfetch_permitted: fetch https://www.instagram.com/robots.txt once with WebFetch, save the notice lines and the rule blocks for "*" and "ClaudeBot" verbatim to ${DIR}/robots_snapshot.txt, compare with the newest older ${ROOT}/data/monitor/*/robots_snapshot.txt and set robots_changed. Fetch nothing else.
5. If the mode is manual and ${DIR}/inbox/topics is empty, set note="inbox empty".`, { schema: LISTS, effort: 'low', label: 'preflight' })
if (!pre) throw new Error('preflight agent failed')
log(`week ${WEEK}, mode ${MODE}: ${pre.slugs.length} topics, ${pre.n_competitors} competitors${pre.note ? ' - ' + pre.note : ''}`)
if (pre.robots_changed) log('robots.txt changed since last snapshot - check before trusting the permission scope')

let stopped = null
if (!pre.already_collected) {
  phase('Topics')
  if (MODE === 'webfetch_permitted') {
    const batches = []
    for (let i = 0; i < pre.slugs.length; i += TOPIC_BATCH) batches.push(pre.slugs.slice(i, i + TOPIC_BATCH))
    for (let b = 0; b < batches.length; b++) {           // sequential on purpose: pacing, one page at a time
      const nn = String(b).padStart(2, '0')
      const r = await agent(topicPrompt(batches[b], `${DIR}/topics/batch_${WK}_${nn}.json`, `${WK}_${nn}`),
        { schema: BATCH, label: `topics ${nn}`, phase: 'Topics' })
      if (r && r.stop) {
        stopped = `topics batch ${nn}: ${r.stop_reason || 'blocked'}`
        log(`STOP (${stopped}); ${batches.length - b - 1} topic batches not fetched, no retry this week`)
        break
      }
    }
  } else if (MODE === 'manual') {
    if (pre.note === 'inbox empty') {
      stopped = 'manual inbox empty'
    } else {
      await agent(manualPrompt(), { schema: BATCH, label: 'parse inbox', phase: 'Topics' })
    }
  } else {
    const r = await agent(apiPrompt(), { schema: BATCH, label: 'graph api', phase: 'Topics' })
    if (r && r.stop) stopped = `api: ${r.stop_reason || 'failed'}`
  }
}

// Embeds (network, sequential) and caption coding (no network, parallel) are independent -> run side by side
const embedChain = async () => {
  if (MODE !== 'webfetch_permitted' || stopped || pre.already_collected) return 'skipped'
  const todo = await agent(`cd ${ROOT} && python3 scripts/monitor/monitor_weekly.py ${DIR} ${PREV} --todo --todo-max ${MAX_EMBEDS}
Then read ${DIR}/embed_todo.json and return urls = all "competitors" entries followed by all "reels" entries (handle, shortcode, embed_url) and dropped = dropped_by_todo_max. No network access in this task.`,
  { schema: TODO, effort: 'low', label: 'embed todo', phase: 'Embeds' })
  const urls = (todo && todo.urls) || []
  if (todo && todo.dropped) log(`embed todo capped: ${todo.dropped} reels dropped (see embed_todo.json)`)
  for (let b = 0; b * EMBED_BATCH < urls.length; b++) {   // sequential: pacing
    const nn = String(b).padStart(2, '0')
    const r = await agent(embedPrompt(urls.slice(b * EMBED_BATCH, (b + 1) * EMBED_BATCH), `${DIR}/accounts/followers_${WK}_${nn}.json`),
      { schema: BATCH, label: `embeds ${nn}`, phase: 'Embeds' })
    if (r && r.stop) {
      stopped = `embeds batch ${nn}: ${r.stop_reason || 'blocked'}`
      log(`STOP (${stopped}); remaining embed batches skipped`)
      break
    }
  }
  return `${urls.length} embed urls`
}

const codeChain = async () => {
  if (stopped === 'manual inbox empty') return 'skipped'
  const cnt = await agent(`cd ${ROOT} && python3 scripts/monitor/monitor_weekly.py ${DIR} --dump-captions -1
Return n and chunks from the printed JSON. If it fails because there are no topic reels, return n=0, chunks=0. No network.`,
  { schema: COUNT, effort: 'low', label: 'caption count', phase: 'Codes' })
  if (!cnt || !cnt.chunks) return 'no captions'
  const idx = Array.from({ length: cnt.chunks }, (_, i) => i)
  const res = await parallel(idx.map((i) => () => agent(`Code Instagram captions with the project codebook. No network access (no WebFetch).
1. Run: cd ${ROOT} && python3 scripts/monitor/monitor_weekly.py ${DIR} --dump-captions ${i}
2. Read the "caption-derived" block of ${ROOT}/scripts/cover_codebook.md and use exactly its labels.
3. For every reel of the printed chunk code: caption_hook_category, caption_first_line (verbatim, max 120 chars), cta_type, location_claimed, price_claimed, ai_disclosed, language. Judge from the caption text only; empty caption -> caption_hook_category "none".
4. Write ${DIR}/reels/caption_codes_${WK}_${String(i).padStart(2, '0')}.json:
{"coded_at": "${DAY}", "coder": "caption-v1", "reels": [{"shortcode": "...", "handle": "...", "visual_status": "caption_only", "code": {"caption_hook_category": "...", "caption_first_line": "...", "cta_type": "...", "location_claimed": null, "price_claimed": null, "ai_disclosed": false, "language": "en"}}]}
Check it parses with python3 -c "import json,sys; json.load(open(sys.argv[1]))" <file>. Return file and n.`,
  { schema: CODED, effort: 'low', label: `codes ${i}`, phase: 'Codes' })))
  return `${res.filter(Boolean).length}/${cnt.chunks} caption chunks coded`
}

phase('Embeds')
const [embedInfo, codeInfo] = await parallel([embedChain, codeChain])
log(`embeds: ${embedInfo}; codes: ${codeInfo}`)

phase('Report')
const summary = await agent(`Create the weekly monitor report. No network access.
1. Add "stopped": ${JSON.stringify(stopped)} to ${DIR}/run_meta.json (keep the other fields).
2. Run: cd ${ROOT} && python3 scripts/monitor/monitor_weekly.py ${DIR} ${PREV}
3. Read ${DIR}/report.md. Return: report = its path; top_alerts = the first 5 alert lines of section 1 (verbatim, shortened to 200 chars each); data_quality = one sentence on coverage and anything that stopped the collection.
Do not interpret beyond the report and make no causal claims.`, { schema: SUMMARY, label: 'report', phase: 'Report' })
return { week: WEEK, mode: MODE, stopped, embeds: embedInfo, codes: codeInfo, summary }
```

---

## 3. Wöchentlicher Zeitplan

### Variante A: Claude Code Routine, empfohlen

Einrichten in einer Claude-Code-Session mit dem Satz *„Leg eine wöchentliche Routine an …“*. Dabei entsteht ein Trigger mit `create_new_session_on_fire = true`.

**Zeitpunkt:** Cron `CRON_TZ=Europe/Berlin 51 6 * * 1`, also Montag 06:51.
- Die Minute ist absichtlich nicht :00, damit der Lauf nicht mit anderen Routinen zur vollen Stunde startet.
- Im Modus `manual` Montag 10:51 wählen. Der Owner speichert die Seiten vorher, Kalender-Erinnerung Montag 09:30.

**Prompt der Routine** (steht allein, jede Ausführung startet frisch):

```
Weekly Instagram competitor monitor (Part 33, instagram-interior-research).
1. WEEK=$(date -u +%G-W%V); RUN=$(date -u +%Y-%m-%dT%H:%M:%SZ)
2. cd instagram-interior-research/scripts/monitor && awk '/^```js workflow/{f=1;next} /^```/{f=0} f' monitor_workflow_prompt.md > weekly_monitor.workflow.js
3. Run the Workflow tool with scriptPath = <abs path>/weekly_monitor.workflow.js and args
   {"week": "<WEEK>", "run_started_utc": "<RUN>", "mode": "manual"}.
   Add "prev": "<abs path>/instagram-interior-research/data/raw" only if data/monitor has no earlier week folder with topics/.
4. git add instagram-interior-research/data/monitor/<WEEK> ; git commit -m "monitor: <WEEK>" ; push to branch monitor/<WEEK>.
5. Reply with the report path and the top 5 alerts. Do not change the watchlists or any other file.
```

**Hinweise zur Routine:**
- Ob das Workflow-Tool in Routine-Sessions verfügbar ist: **zu verifizieren** beim ersten Lauf.
- Fehlt es, führt die Session die Schritte der Prompts nacheinander selbst aus.
- Interaktiv angemeldete MCP-Server fehlen in Headless-Läufen möglicherweise. WebFetch ist eingebaut und betrifft das nicht.

### Variante B: cron auf eigenem Server

```
51 6 * * 1  cd /pfad/zum/repo && claude -p "$(cat instagram-interior-research/scripts/monitor/routine_prompt.txt)" >> monitor.log 2>&1
```

Flags für Headless-Betrieb und Berechtigungen des `claude`-CLI sind **zu verifizieren**. `routine_prompt.txt` ist der Prompt aus Variante A.

---

## 4. Tempo und Abbruch (Pacing)

| Regel | Umsetzung |
|---|---|
| Nie parallel dieselbe Domain abrufen | Topic- und Embed-Batches laufen in einer `for`-Schleife **nacheinander**, innerhalb eines Batches Seite für Seite. Parallel läuft nur das Caption-Coding, und das ohne Netz. |
| Volumen klein halten | Pro Woche höchstens ca. 57 Topic-Seiten, 39 Wettbewerber-Embeds und 80 Reel-Embeds, also **≤ ~180 Abrufe**. Research zum Vergleich: 264 Topics plus Embeds an einem Tag. |
| Circuit Breaker | Die erste Login-Wall, der erste 429 oder Captcha setzt `stop=true`. Danach folgen **keine** weiteren Abrufe in dieser Woche, kein Retry und kein Ausweichen. |
| Keine Doppelabrufe | Liegen im Wochenordner schon `topics/batch_*.json`, wird nicht neu erhoben. Der 15-Minuten-Cache von WebFetch spielt bei wöchentlichem Takt keine Rolle. |
| Protokoll | `run_meta.json` enthält Modus, Erlaubnis-Referenz und Stoppgrund. Der Report zeigt fehlgeschlagene Topics. |

---

## 5. Prüfen ohne Netz (Trockenlauf)

```bash
cd instagram-interior-research
python3 scripts/monitor/monitor_weekly.py data/raw --only-watchlist --out-dir data/monitor/2026-W39_baseline   # Baseline-Report
python3 scripts/monitor/monitor_weekly.py data/raw --todo --out-dir /tmp/mon_test                           # Embed-Liste
python3 scripts/monitor/monitor_weekly.py data/raw --dump-captions -1                                       # Caption-Chunks
```

---

## 6. Menschliche Review nach dem Lauf

Siehe [`17_competitor_monitor.md`](../../17_competitor_monitor.md), Abschnitt 6. Kurz:
1. Report lesen.
2. `inspiration_candidates.csv` ausfüllen, und zwar nur mit **Prinzipien in eigenen Worten**.
3. Übernommene Prinzipien in `data/monitor/inspiration_board.csv` eintragen.
4. Höchstens 2 Tests für die Testmatrix der nächsten Woche anlegen.
5. `watchlist_competitors_next.csv` übernehmen.

---

## 7. Spezifikation `collect_graph_api.py` (Modus `api`, noch zu bauen)

**Grundlage** ist die Meta-Doku, abgerufen am 2026-09-25:
- **Business Discovery** liefert für andere *professionelle* Accounts `followers_count` und `media_count`, pro Medium `like_count`, `comments_count` und `view_count`.
- Daten altersbeschränkter Accounts gibt Business Discovery nicht zurück.
- Welche Berechtigungen nötig sind, nennt die Seite nicht ausdrücklich: **zu verifizieren**.
- **Hashtag Search** liefert `top_media` und `recent_media`. Es gilt *"a maximum of 30 unique hashtags … within a rolling, 7 day period"*. Nötig sind `Instagram Public Content Access` und `instagram_basic` per App Review. Welche Media-Felder zurückkommen, ist auf der Seite nicht angegeben: **zu verifizieren**.

| Ziel-Datei | Felder | Quelle |
|---|---|---|
| `competitors/media_<handle>.json` | `{"handle", "followers_count", "media_count", "fetched_at", "media": [{"permalink", "timestamp", "like_count", "comments_count", "view_count", "caption"}]}` | Business Discovery, pro Watchlist-Handle, letzte 25 Medien |
| `topics/batch_<wk>_api.json` | wie Topic-Batch; pro Hashtag ein Eintrag `slug = "hashtag-<tag>"`, Reels mit `likes_text` (und `views_text`, falls geliefert) | Hashtag Search `top_media`, höchstens 30 Hashtags pro 7 Tage |

`monitor_weekly.py` verarbeitet beide Dateitypen bereits. Die Tests liefen mit synthetischen Fixtures, nicht mit echten API-Antworten:
- Liefert eine Topic-Seite keine Views, rechnet es den topic_index auf Likes.
- Für Wettbewerber-Reels berechnet es einen **Account-Index**: Reel ÷ Median des Accounts.

Den Token hält der Collector nur in Umgebungsvariablen und schreibt ihn nie in Dateien oder Logs. Rate-Limits der Graph API: **zu verifizieren**.
