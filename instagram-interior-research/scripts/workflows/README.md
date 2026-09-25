# Erhebungs-Workflows (Claude Code Workflow-Skripte)

Diese Skripte haben die Daten dieser Studie am 25.09.2026 erhoben bzw. die Dokumente erstellt. Sie laufen im Claude-Code-
`Workflow`-Tool (JavaScript, `agent()`/`parallel()`/`pipeline()`), Pfade sind absolut auf die damalige Session gesetzt.

| Skript | Zweck |
|---|---|
| `sweep_batches.js` | Topic-Sweep: öffentliche `/popular/<slug>/`-Seiten → `data/raw/topics/batch_*.json` |
| `follower_lookup.js` | Follower/Posts je Account über öffentliche Embed-Seiten → `data/raw/accounts/followers_*.json` |
| `code_covers.js` | Embed-Metadaten + Cover-Frame + Codebuch-Codierung je Reel → `data/raw/reels/cover_*.json` |
| `code_covers_rel.js` | Unabhängige Zweitcodierung (Reliabilität) → `data/raw/reliability/` |
| `profile_accounts.js` | Account-Profile (Bio, Links, Angebote, Brand Deals) → `data/raw/accounts/profile_*.json` |
| `yt_shorts.js` | YouTube-Shorts-Proxy über NexLev → `data/raw/youtube/shorts_*.json` |
| `market_research.js` | Desk Research q01–q09 inkl. automatisiertem Faktencheck → `quellen/` |
| `write_docs.js` | Schreiben + adversarialer Faktencheck der Dokumente 01–14 |

**Wichtig:** Instagrams `robots.txt` untersagt automatisierte Erhebung ohne ausdrückliche schriftliche Erlaubnis. Die Sweeps
waren eine einmalige Forschungs-Stichprobe. Für wiederkehrendes Monitoring gelten die Modi in
[../../17_competitor_monitor.md](../../17_competitor_monitor.md) (Graph API / manuell / nur mit Erlaubnis).
