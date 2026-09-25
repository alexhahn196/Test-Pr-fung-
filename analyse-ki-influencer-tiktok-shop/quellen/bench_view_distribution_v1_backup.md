# Benchmark: View-Verteilung pro Video bei neuen/kleinen TikTok-Accounts und TikTok-Shop-Affiliate-Videos

Zugriffsdatum aller Quellen: 2026-09-24. Tag-Legende: **Verified** = in einem Primärdokument / in TikTok-Daten gesehen; **Claimed** = von Creator/Anbieter/Redditor behauptet, nicht prüfbar; **Estimated** = eigene Rechnung (Formel und Inputs angegeben).

Methodik-Hinweis: Das WebSearch-Budget der Session war vor diesem Task aufgebraucht. Genutzt wurden daher direkte WebFetch-Abrufe bekannter Primär-URLs (TikTok Newsroom, TikTok Shop Academy, Socialinsider, Metricool, Buffer, Rival IQ, arXiv, PNAS Nexus), die arXiv-Suchseite, die Arctic-Shift-Reddit-API, NexLev-YouTube-Suche + Transkripte (10 neue Videos) sowie lokal bereits vorliegendes Material (EchoTik-Q1-2025-PDF, 30+ YouTube-Transkripte, Reddit-Dumps, TikTok-Shop-Academy-Essays). Semantic Scholar antwortete nur mit HTTP 429 (Rate-Limit); Kalodata-Blog (Cloudflare 403), Tabcut/FastMoss/EchoTik-Blogs lieferten keine Reports mit View-Verteilungen. Bing/DuckDuckGo über Fetch lieferten nur Bot-Junk.

---

## 1) Kurzfazit

1. **Es gibt keinen öffentlichen Datensatz mit Median-Views oder View-Klassen (<1k / 1k–10k / 10k–100k / 100k+) für neue Accounts oder für TikTok-Shop-Affiliate-Videos.** Kalodata/EchoTik/Tabcut/FastMoss veröffentlichen GMV- und Kategorie-Reports, keine View-Verteilungen pro Video. Benchmark-Reports (Socialinsider, Metricool, Buffer, Rival IQ) liefern nur **Durchschnitte** (Mittelwerte), keine Mediane oder Perzentile — und Mittelwerte werden bei einer stark rechtsschiefen Verteilung von wenigen Ausreißern dominiert. Nicht öffentlich verifizierbar: Median-Views neuer Accounts.
2. Der beste veröffentlichte Ankerwert: **Socialinsider TikTok Benchmarks 2026** (2 Mio. Videos, 214.507 Profile, Jan 2024–Dez 2025): Accounts mit 1–5k Followern erzielten 2025 im Schnitt **350 Views pro Post** (2024: 860; –59 %). 5–10k Follower: 945 Views. Das ist ein Mittelwert über alle (auch inaktive/schlechte) Accounts; der Median liegt darunter (Verified als Report-Zahl; nicht als Rohdaten).
3. **TikTok selbst** sagt (Newsroom, Juni 2020): Follower-Zahl und frühere Hits sind „keine direkten Faktoren" der Empfehlung; Videos größerer Accounts bekommen aber „wahrscheinlich mehr Views" wegen der Follower-Basis. Eine offizielle Aussage zu „Testgruppen von 200/1.000 Nutzern" gibt es **nicht**; das ist Creator-Folklore (Claimed).
4. **Praktiker-Evidenz** (12+ selbst dokumentierte Challenge-Accounts, alle Claimed) ist auffallend konsistent: Bei neuen Affiliate-Accounts bleiben **die meisten Videos bei 100–500 Views**; typischerweise „ein Winner pro 15–40 Videos", Winner-Videos 30k–900k Views. Vollständige Flop-Serien (0–100 Views über Wochen bei 5–10 Posts/Tag) sind bei generischen Sora-2-Clips dokumentiert.
5. **Pareto:** Kein Datensatz. Claims: „98 % meines Geldes kommen aus Videos von 2 Wochen im April/Mai", „17 Posts, ein Video mit 900k Views = praktisch der ganze Umsatz", „die meisten Videos 100–300 Views, ein bis zwei bei 1 Mio. bzw. 200k kompensieren alles". Estimated: Top-5 % der Videos ≈ 70–85 % der Views; GMV-Anteil eher höher, weil GMV-Max-Werbebudget der Brands auf die bereits konvertierenden Videos konzentriert wird (Claimed-Mechanik, mehrfach beschrieben).
6. **Videos bis zum ersten Sale:** Berichtete Bandbreite 15–70 Videos (5–14 Tage bei 3–10 Posts/Tag); Ausreißer von „Tag 1" bis „3–6 Monate". Häufiger Bremsfaktor: Creator-Pilot-Programm (Shoppable-Video-Limit/24h-Throttling) — nicht öffentlich verifizierbar als Regelwerk.
7. **AI-Label und Reichweite:** TikTok Shop Academy (EU/IE-Version, Verified): „Content that is auto-disclosed will not face additional penalties or distribution restrictions solely due to the label." Ein unabhängiger A/B-Test „mit vs. ohne AI-Label" existiert öffentlich nicht. Publikums-Ebene: Altay & Gilardi (PNAS Nexus 2024, n = 4.976) finden einen **kleinen** negativen Effekt eines „AI-generated"-Labels auf wahrgenommene Genauigkeit und Teil-Absicht (0,11–0,17 Punkte auf 6er-Skala; dreimal kleiner als ein „falsch"-Label). Vendor-Claims (Creatify „2,7x mehr Leads", „1,7x ROI") vergleichen Video vs. Standbild, nicht AI vs. Mensch; die kursierende „350 % höhere Engagement"-Zahl ist in keiner Primärquelle auffindbar → Nicht öffentlich verifizierbar.
8. **Halbwertszeit / Shop-Tab / Suche:** Keine öffentlichen Zahlen zum Sales-Anteil aus Suche/Shop-Tab vs. FYP (Nicht öffentlich verifizierbar). Metricool (2,3 Mio. Posts): 7 von 10 Views kommen aus der For-You-Page (alle TikTok-Inhalte, nicht Shop-spezifisch). TikTok Shop Academy nennt eigene „Shop Tab Eligibility Requirements". Praktiker: Videos „ziehen oft erst nach 7–10 Tagen an", ein Winner verkauft noch Wochen später.
9. **Abgeleitete 100-Video-Verteilung (kompetenter neuer AI-Affiliate-Account, Estimated):** konservativ 90 / 8 / 2 / 0, realistisch 80 / 15 / 4 / 1, aggressiv 65 / 22 / 10 / 3 (Klassen <1k / 1k–10k / 10k–100k / 100k+). Details und Herleitung in Abschnitt 3.

---

## 2) Daten und Benchmarks (mit Tag, Quelle, Datum)

### 2.1 Plattform-Benchmarks (Vendor-Reports; nur Mittelwerte, keine Mediane)

| Kennzahl | Wert | Tag | Quelle / Datum |
|---|---|---|---|
| Ø Views pro Post, Accounts 1–5k Follower | 2025: **350** (2024: 860, –59 %) | Verified (Report-Zahl) | Socialinsider „TikTok Benchmarks 2026", publ. 2026-04-22, 2 Mio. Videos / 214.507 Profile, Jan 2024–Dez 2025 — https://www.socialinsider.io/blog/tiktok-benchmarks/ |
| Ø Views pro Post, 5–10k Follower | 2025: 945 (2024: 1.575) | Verified (Report-Zahl) | ebd. |
| Ø Views pro Post, 10–50k / 50–100k / 100k–1M | 3.240 / 9.900 / 34.900 (2025) | Verified (Report-Zahl) | ebd. |
| Ø Likes pro Post, 1–5k Follower | 330 (2025) — Hinweis: Likes > Views/2 zeigt, dass der Views-Mittelwert durch die Tier-Definition (Follower-Zählung zum Messzeitpunkt) verzerrt ist | Verified (Report-Zahl) | ebd. |
| Engagement-Rate nach Views (alle Tiers) | 4,20 % (2025); Q2 2026: 3,85 % | Verified (Report-Zahl) | ebd. |
| Views-Entwicklung gesamt | –23 % YoY; kleinste Accounts ~–50 % | Verified (Report-Zahl) | ebd. |
| Ø Views pro TikTok-Post (Brands) | 6.268 (2024) → 6.496 (2025) | Verified (Report-Zahl) | Socialinsider „Social Media Benchmarks 2026", 70 Mio. Posts, Jan 2024–Dez 2025 — https://www.socialinsider.io/blog/social-media-benchmarks/ |
| Anteil Views aus For-You-Page | „7 von 10 Views" | Verified (Report-Zahl) | Metricool TikTok Study 2026, 2.314.756 Posts / >92.000 Accounts — https://metricool.com/tiktok-study/ |
| Video vs. Bild-Post | Video: 5x Views, 6x Interaktionen | Verified (Report-Zahl) | ebd. |
| Anteil Accounts <100k, die 2025→2026 wuchsen | 44 % | Verified (Report-Zahl) | ebd. |
| Posting-Frequenz vs. Views/Post | 3–5 Posts/Woche: +17 %; 6–10: +29 %; 11+: +34 % Views pro Post | Verified (Report-Zahl) | Buffer, Analyse von 11 Mio. TikTok-Videos — https://buffer.com/resources/tiktok-algorithm/ |
| Median-Views, Perzentile, View-Rate | **nicht enthalten** | — | Socialinsider (explizit nur Durchschnitte), Buffer (7,1 Mio. Posts, nur Engagement-Rate: https://buffer.com/resources/best-time-to-post-on-tiktok/), Rival IQ 2025 (150 Firmen × 14 Branchen, nur Engagement-Rate pro Video: https://www.rivaliq.com/blog/social-media-industry-benchmark-report/) |

Einordnung (Estimated): Mit 350 Views/Post × 100 Videos ergibt der Socialinsider-Mittelwert **~35.000 Gesamt-Views pro 100 Videos** für einen durchschnittlichen 1–5k-Follower-Account. Zwei der AI-Challenge-Accounts unten (Ecom King: 20–30k Views in 30 Tagen; Deniz Sancar: ~35 Videos, „meist ~500 Views") liegen genau in dieser Größenordnung.

### 2.2 TikTok-eigene Aussagen zur Verteilung neuer Videos

| Aussage | Tag | Quelle / Datum |
|---|---|---|
| „neither follower count nor whether the account has had previous high-performing videos are direct factors in the recommendation system" | Verified (Zitat) | TikTok Newsroom „How TikTok recommends videos #ForYou", 2020-06-18 — https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you |
| „a video is likely to receive more views if posted by an account that has more followers, by virtue of that account having built up a larger follower base" | Verified (Zitat) | ebd. |
| Frisch hochgeladene oder in Prüfung befindliche Videos sowie Spam „may be ineligible for recommendation into anyone's For You feed" | Verified (Zitat) | ebd. |
| Keine Aussage zu Testgruppen-Größen (200/1.000 Nutzer), Batch-Rollouts oder Video-Lebensdauer | Verified (Fehlanzeige) | ebd.; Support-Seite „How TikTok recommends content" (https://www.tiktok.com/support/faq_detail?id=7655285288050104852) lieferte per Fetch keinen Body |
| Creator-Folklore: „Dein Video wird an 200 Leute ausgespielt, bei guter Performance an 1.000 …" | Claimed | Human-Affiliate rMA5MKeyym8 [9:22]; Mike Yanda „How to BEAT the TikTok Algorithm" (YouTube VgUZJo0qDRc, ~Feb 2026): „TikTok intentionally stalls videos at 200 views and it runs a small test"; Reddit r/TikTokShopAffiliate 2024-06 („as long as you're getting at least 200 views you're not shadow banned") |
| Shop-Content muss zusätzlich „Shop Tab Eligibility Requirements (rules for showing content on the Shop tab)" erfüllen, um „on the homepage or in recommendations" zu erscheinen | Verified (Zitat) | TikTok Shop Academy US „Content Policy" — https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617&lang=en |

### 2.3 Akademische Evidenz zur View-Verteilung

| Befund | Tag | Quelle / Datum |
|---|---|---|
| Douyin-Datensatz, >260.000 Kurzvideos über 3 Monate: „the most popular Douyin videos follow Zipf's law on video popularity, but the rest of the videos do not"; Views und Likes stark korreliert. Keine Prozent-Aufteilung publiziert. | Verified (Abstract) | Chen, He, Mao, Chung, Maharjan, arXiv:1903.12399, 2019-03-29 — https://arxiv.org/abs/1903.12399 |
| Audit-Studien zu TikTok (arXiv-Suche „tiktok recommendation algorithm audit", 11 Treffer 2022–2026) untersuchen Personalisierung/Amplifikation aus **Nutzersicht** (z. B. „rapid reinforcement typically occurring within the first 200 videos watched", arXiv:2503.20231, März 2025), **nicht** die Exposure neuer Creator. Kein Paper mit View-Verteilung für neue Accounts gefunden. | Verified (Fehlanzeige) | https://arxiv.org/search/?query=tiktok+recommendation+algorithm+audit&searchtype=all ; https://arxiv.org/abs/2503.20231 |
| arXiv-Suche „AI-generated label engagement social media experiment": 0 Treffer | Verified (Fehlanzeige) | arXiv-Suche 2026-09-24 |
| Semantic Scholar: HTTP 429 (Rate-Limit), keine Ergebnisse | — | api.semanticscholar.org, 2026-09-24 |

### 2.4 Praktiker-Beobachtungen: View-Verteilung neuer (AI-)Affiliate-Accounts (alle **Claimed**, selbstberichtet in YouTube-Videos/Reddit)

| # | Wer / Setting | Beobachtete Verteilung | Quelle / Datum |
|---|---|---|---|
| 1 | Deniz Sancar, UK, brandneuer AI-Faceless-Affiliate-Account, 5 Tage, 5–8 Videos/Tag (≈30–40 Videos) | „most videos got stuck around 500 views, which, to be honest, is to be expected"; ein Video 7.000 Views → 8 Verkäufe (>1 Sale/1.000 Views); 24h Posting-Sperre durch Creator-Pilot-Programm; Erlös < £50 | YouTube Tsv7Zt9w9-4 [4:14, 4:54, 5:16] |
| 2 | Patryk Marketer, Sora-2-AI-Clips (Kleidung), 5–10 Videos/Tag über Wochen | „a lot of these videos didn't even go past 100 views… stuck in the 30, 15 views"; nächste Woche: „anything from zero to 100 views… a couple that got 200" | YouTube NKxTt215kus „I WASTED 30 Days…" [5:55–6:02, 8:20–8:35], ~Dez 2025 |
| 3 | Patryk Marketer, nach Formatwechsel (Bodycam-Style) | „a lot of videos that week that got over 100,000, 500,000, 200,000 views"; Ergebnis $13.000 GMV / ~$2.000 Commission im Monat | YouTube 3Axh5s_iUyA [12:54–13:01] |
| 4 | Nadorb, UK, 7-Tage-Challenge auf umgewidmetem Gaming-Account, AI-Influencer | „Most of these videos didn't even get over 1,000 views"; £2 Commission | YouTube SAuvpusxX4g [11:10] |
| 5 | The Ecom King (Kamil Sattar), Sora-2-AI-Avatare, 30 Tage | Account gesamt „around about 20 to 30,000 views"; $200–300 Umsatz | YouTube W5ThaDXg2ss [13:51], ~Nov/Dez 2025 |
| 6 | Turner (BatchBot), voll-AI-Account, 5–10 Videos/Tag | erster Sale nach „a whole week"; danach $3,5k Commission in Monat 1 und 2; neuer Test-Account Tag 1: 6 Items, $11 Commission, $104 GMV | YouTube DHZ8iI0Sbj0 [0:44, 18:06–18:13], ~Aug 2025 |
| 7 | Human-Affiliate (UK), 30 Tage, 17 Posts im September | ein Video 900.000 Views („4,000 saved, 23,000 likes"), „a few on like 8K", „the rest kind of flopped"; nahezu gesamter Umsatz aus dem einen Video; Heuristik: „3 to 5K views within the first 12 to 24 hours" = Winner | YouTube rMA5MKeyym8 [9:02, 22:24, 23:30], Herbst 2025 |
| 8 | tommycetty, AI-Content, 3–5 Posts/Tag + Zweitaccount, ~11 Accounts | Top-Videos 226k / 168k / 67k Views; „You're not going to have every single video pop off"; $7,41 Netto pro 1.000 Views auf den Winnern | YouTube kjCyL4Vn4P4 [1:39–2:48, 10:27], ~März 2026 |
| 9 | Jhonatas Silva beobachtet fremden Veo-3-AI-Account (Shirts) | „the videos don't have that many views, 100, 200, 300, but most have that, but one or two get 1 million, another gets 200,000 and these videos compensate and then bring in a lot of commission" | YouTube Bg5fs8ctzqM, ~Jul 2026 |
| 10 | Amber Sharniece (human, kein AI), 1 Video/Tag | Monat 1 (30 Videos): 12 Items, ~$84 Commission; Monat 2: 103 Items, $5.300 GMV, ~$539 Commission; 1.–9. Juli: 47 Items, $1,5k GMV, $172,67 | YouTube CgPX3Po7WFo, ~Jul 2026 |
| 11 | Reddit r/passive_income, 8k Follower, AI-Videos aus Programm, 3–5 Posts/Tag | „Initially, videos sat around 1k views with 0 sales. But on day 5 of posting, I got my first sale… Then, one video suddenly went viral: 100k views and almost $10k in GMV… So far, I've had 4 viral videos"; ~$2k/Monat | https://www.reddit.com/r/passive_income/comments/1u9s0zn/ , 2026-06-19 |
| 12 | Reddit r/passive_income, Faceless-Finance (Stock-Footage + TTS) | „Posted 8 videos over two weeks. Best one got 340 views. Most got under 100." | https://www.reddit.com/r/passive_income/comments/1rdiwob/ , ~2026-02-24 |
| 13 | Reddit r/TikTokShopAffiliate, 2.600 Follower | „I average 200-300 every video. Now they're not even hitting 50-100." | /r/TikTokShopAffiliate/comments/1dsuss1/ , 2024-07-02 |
| 14 | Reddit r/TikTokShopAffiliate | „I've hardly ever see anything over 200 views… have not made any sells"; „Stuck literally at 100 and 200 views from getting million of views" | /r/TikTokShopAffiliate/comments/1draeqq/ , 2024-06/07 |
| 15 | Reddit r/TikTokShop | „Its taken me 2 weeks to get my first sale, I average 500 - 1 k views." | /r/TikTokshop/comments/1uf1zxj/ , ~2026-06-25 |
| 16 | Buzz, neuer Clip-Account (kein Affiliate) | Video 1: 800 Views, Video 2: 800.000, Video 3: 500.000; „all the views are coming from the FYP" — zeigt, dass Null-Follower-Accounts sofort Massenreichweite erhalten können | YouTube 0eQDpN4lmNE, ~Feb 2026 |
| 17 | Modern Millie (human, Lifestyle) | 126 TikToks in 108 Tagen → +251 Follower (≈2,3/Tag) | YouTube AoCT5YZycp0, ~Nov 2025 |
| 18 | 404 Media über Rosabella/„poormaninla"-Netzwerk (AI-Ärzte-Videos) | einzelne AI-Videos „hundreds of thousands or millions of views", ein Video 1,3 Mio. Views; Account @poormaninla am 2026-09-24 **nicht mehr auffindbar** (tt_profile.sh → statusCode 10221) | 404 Media „Inside an AI TikTok Shop Slop Factory That Shills Supplements Recalled By the FDA" (lokaler Dump 404media.html); Handle-Check Verified |

Beobachtung (Estimated): Über alle Fälle hinweg liegt der **Modus** neuer Affiliate-Videos bei 100–500 Views, der **Median** eines kompetenten Accounts bei ca. 200–500 Views; „Winner" (≥10k) treten etwa alle 15–40 Videos auf, „Big Winner" (≥100k) etwa 0–3 pro 100 Videos.

### 2.5 „X von N Videos"-Ratios (alle Claimed)

| Ratio | Quelle |
|---|---|
| 1 von 17 Posts (900k Views), „a few" bei 8k, Rest Flop | rMA5MKeyym8 [23:30] |
| 1 von 3 Videos = 800k (Clip-Account) | 0eQDpN4lmNE |
| „ein bis zwei" Millionen-/200k-Videos bei einem Account, dessen Masse bei 100–300 Views liegt | Bg5fs8ctzqM |
| 4 virale Videos in ~3 Monaten bei 3–5 Posts/Tag (≈300–450 Videos → ≈1 %) | Reddit 1u9s0zn |
| „Give a product 3 to 5 videos before you write it off, since the first one almost never moves" | /r/TikTokShopAffiliate/comments/1wba5a1/ , ~2026-09-09 |
| Brand-Erwartung: „1 sale from every 5k views"; Creator: „1k views before first sale" | /r/TikTokShopAffiliate/comments/1d1xgd3/ , 2024-05-27 |
| „If it converts at one sale per 200 views…" (Rechenbeispiel Mentor) | YouTube I_1fpXpUdbE [3:30] |
| Eine explizite Aussage „X von 100 Videos erreichen 10k+" wurde in keiner Quelle gefunden | — |

### 2.6 Pareto / GMV-Konzentration

| Befund | Tag | Quelle |
|---|---|---|
| „All my videos that's currently making me 98% of my money was posted in late April/early May" | Claimed | /r/TikTokShopAffiliate/comments/1dleq94/ , 2024-06-21 |
| 17 Posts, ein 900k-Video = praktisch der gesamte 30-Tage-Umsatz; „the video is going to still print me money passively" | Claimed | rMA5MKeyym8 |
| Mechanik: Brands/GMV Max legen Ad-Budget auf das Video mit der höchsten CTR: „This video with 200 views… with the ad spend is going to turn into over a million views" | Claimed | I_1fpXpUdbE [3:09–3:36]; ähnlich EMUALbMNV94 [6:19], dgb-xCkZpyc [10:33] |
| Kategorie-Ebene (kein Video-Level): Thailand Q1 2025: Top-10-Kategorien = 86 % des GMV; Beauty = 87 % der Top-10 („winner-takes-all"); 850.000 Creator bei nur ~110.000–200.000 Videos/Monat (→ die große Mehrheit der registrierten Creator postet gar nicht) | Verified (Report-Zahl) | EchoTik „TikTok Shop 2025 Q1 Report" (lokal echotik_q1_2025.pdf, S. 3–5), https://echotik.ai |
| Anteil der Top-1–5 % Videos am Affiliate-GMV | **Nicht öffentlich verifizierbar** | — |

Estimated: In der realistischen 100-Video-Verteilung (Abschnitt 3) entfallen ~81 % der Views auf die Top-5-Videos. Da GMV-Max-Budget zusätzlich auf konvertierende Winner fließt (Claimed-Mechanik), ist der GMV-Anteil der Top-5 % eher **≥ 85–90 %** anzusetzen.

### 2.7 Videos / Tage bis zum ersten Sale (alle Claimed)

| Fall | Posts/Tag | Zeit bis 1. Sale | ≈ Videos bis 1. Sale (Estimated = Posts/Tag × Tage) | Quelle |
|---|---|---|---|---|
| Turner (AI) | 5–10 | 1 Woche | 35–70 | DHZ8iI0Sbj0 |
| Reddit 1u9s0zn (AI) | 3–5 | Tag 5 | 15–25 | r/passive_income 2026-06-19 |
| Reddit 1w2nfnu-Kommentar | 20 | „20 videos per day to get my first sale" | ≥ 20 | /r/TikTokshop/comments/1w2nfnu/ , ~2026-08-30 |
| Reddit 1uf1zxj | k. A. | 2 Wochen (Ø 500–1k Views) | k. A. | ~2026-06-25 |
| Thread „TikTok affiliates – How long till you started selling" (OP: 2–3 Shoppable/Tag, Pilot-Programm) | 2–3 | Antworten: „a day or 2"; „first week zero sales"; „10 days in" (3/Tag → ≈30 Videos; 8 Items im 1. Monat); „15 days in… no sales yet, pretty low views" (≈30–45 Videos); „two weeks in… 1.1k in commission"; „after that week… 11 sales because one video went off"; „a week, a month, 3 months, 6 months, a year, and literally everything in between"; „If you're not willing to post for 3-6 months without many sales then don't even bother" | 5–45+ | /r/TikTokshop/comments/1w2ubvm/ , ~2026-08-30 bis 09-09 |
| Amber Sharniece (human) | 1 | innerhalb Monat 1 (12 Items) | ≤ 30 | CgPX3Po7WFo |
| Deniz Sancar (AI) | 5–8 | innerhalb 5 Tagen | ≤ 40 | Tsv7Zt9w9-4 |
| Neuer Test-Account Turner | ~10 | Tag 1 (6 Items) | ~10 | DHZ8iI0Sbj0 [18:06] |
| Human, M231JK1yr_k | k. A. | Tag 1 | k. A. | YouTube M231JK1yr_k |
| Vendor-Claim: „70% of beta testers made their first sale within the first week" | — | Claimed (Anbieter, Reddit-Wiedergabe) | — | /r/Entrepreneurs/comments/1snwa7t/ , 2026-04-17 |

Estimated Zusammenfassung: Median ≈ 7–10 Tage bzw. ≈ 20–40 Videos bis zum ersten Sale bei 3–5 Posts/Tag; 10–20 % der Starter berichten ≥ 4 Wochen ohne Sale. Selektionsbias: Erfolglose posten seltener Rückblicke.

### 2.8 AI-Label / „AI-Look" und Reichweite

| Befund | Tag | Quelle / Datum |
|---|---|---|
| „Once content is automatically labeled by the platform, creators cannot remove the label. Content that is auto-disclosed will not face additional penalties or distribution restrictions solely due to the label." | **Verified (Zitat)** | TikTok Shop Academy (EU/IE) „AI-Generated Content Restrictions and Requirements" — https://seller-ie.tiktok.com/university/essay?knowledge_id=6752261875877653&lang=en-GB (lokal aigc_eu_en.html); dieselbe Policy US: https://seller-us.tiktok.com/university/essay?knowledge_id=491489038501663&lang=en (Satz dort im Extrakt nicht enthalten) |
| TikTok Newsroom zu AI-Labels (2023-09-19; 2024-05-09, C2PA-Auto-Labeling): **keine** Aussage zu Reichweiten-Effekten des Labels; verboten ist „harmfully misleading AI-generated content — whether it's labeled or not" | Verified (Fehlanzeige/Zitat) | https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content ; https://newsroom.tiktok.com/en-us/partnering-with-our-industry-to-advance-ai-transparency-and-literacy |
| Labor-Experimente (2 präregistrierte Studien, n = 1.976 + 3.003): „AI-generated"-Label senkt wahrgenommene Genauigkeit und Teil-Absicht um 0,17 (Studie 1, p = 0,010) bzw. 0,11 Punkte (Studie 2, p = 0,006) auf 6er-Skala; Effekt „three times smaller than" ein „false"-Label; Skepsis verschwindet, wenn Nutzer realistische Definitionen teilweiser AI-Beteiligung erhalten | Verified (Studie; Headlines, nicht Video) | Altay & Gilardi, PNAS Nexus 3(10), Okt 2024 — https://academic.oup.com/pnasnexus/article/3/10/pgae403/7810648 |
| Konsumenten-Umfrage: „Nearly a third of consumers say they're less likely to choose a brand that uses AI ads" (eMarketer 2025; Stichprobe nicht angegeben) | Claimed (Umfrage, Sekundärzitat) | Hootsuite Social Trends — https://www.hootsuite.com/research/social-trends |
| Vendor Creatify: „2.7x More leads vs. static image ads", „1.7x Higher ROI", „90% Lower production cost" — Quellenangabe nur „Meta, Wistia, HubSpot, Creatify benchmarks", keine Methodik; Vergleich Video vs. Standbild, **nicht** AI vs. Mensch | Claimed (Vendor) | https://creatify.ai/ |
| Vendor Arcads: „1 billion views with ads created with arcads", Case-Study-Deltas ohne Methodik | Claimed (Vendor) | https://www.arcads.ai/ |
| „350 % höheres Engagement" für AI-UGC | **Nicht öffentlich verifizierbar** (in keiner geprüften Primär-/Vendorquelle gefunden) | — |
| Praktiker: „Not one person has ever said anything about it being ai. They dont care." (Clips „doing decent numbers") | Claimed | /r/passive_income/comments/1w7nihc/ , 2026-09-05 |
| Praktiker: AI-Videos von Netzwerk-Accounts mit 100k–1,3 Mio. Views; Accounts später gelöscht/gebannt (@poormaninla, @melisogn9dl: statusCode 10221 am 2026-09-24) — das eigentliche Reichweiten-Risiko von AI-Content ist **Enforcement**, nicht das Label | Claimed (Views) / Verified (Handle-Status) | 404 Media (s. o.); sweep_analytics_press.md |
| Unabhängige A/B-Tests „gleiches Video mit/ohne AI-Label" oder Agentur-Daten „AI-Avatar vs. Mensch" auf TikTok Shop | **Nicht öffentlich verifizierbar** | arXiv/Semantic Scholar/YouTube-Suche ohne Treffer |

Bewertung (Estimated): Für die 100-Video-Verteilung wird **kein algorithmischer Label-Malus** angesetzt (TikTok-Policy-Aussage), aber ein moderater **Publikums-Malus** von ~10–20 % auf Engagement/Weiterempfehlung bei erkennbar synthetischem Look (abgeleitet aus Altay & Gilardi: ~0,1–0,2 Skalenpunkte ≈ 2–4 % der Skala bei Headlines; bei Video-Avataren mit „Uncanny"-Effekt konservativ höher angesetzt). Das größere Risiko ist die Account-Ebene (Violations, Bans, Pilot-Programm-Limits), die ganze Posting-Serien auf 0 setzen kann.

### 2.9 Content-Halbwertszeit und Shop-Tab-/Such-Traffic

| Befund | Tag | Quelle |
|---|---|---|
| Anteil der Views aus FYP: 7 von 10 (alle TikTok-Inhalte) | Verified (Report-Zahl) | Metricool TikTok Study 2026 |
| Anteil TikTok-Shop-Sales aus Suche / Shop-Tab / Product-Card vs. FYP-Video vs. LIVE | **Nicht öffentlich verifizierbar** (Kalodata/EchoTik/FastMoss-Reports nicht zugänglich; TikTok publiziert keine Aufteilung) | — |
| Südostasien (EchoTik Q1 2025): in VN/MY/PH/SG „Livestreaming became the dominant sales method, with video marketing also contributing"; Thailand: Beauty-GMV „driven by KOL/KOC and short video promotions" (qualitativ, ohne Prozentwerte) | Verified (Report-Text) | echotik_q1_2025.pdf |
| Shop-Tab: eigene „Shop Tab Eligibility Requirements"; Health-Rating kann „visibility of the creator's content across the platform" reduzieren oder „limit search results to include the creator" | Verified (Zitat) | TikTok Shop Academy US „Content Policy" (knowledge_id=6837891779151617) und „Creator Health Rating Overview" (lokale Essays) |
| Halbwertszeit: „takes about 7 to 10 days for them to start picking up with the new algorithm"; „View suppression was lifted in 14 days" | Claimed | /r/TikTokShopAffiliate/comments/1dleq94/ (2024-06-21); /1brsw1u/ (2024-04-18) |
| Ein Winner-Video „kept printing cash" nach Ende der Challenge; „every so often we are seeing these five figures… 24K, 12K, 25K, 161,000 views" auf älteren Videos | Claimed | YouTube-Transkripte (26:08; 6:xx in yt_tx) |
| Quantitative Halbwertszeit (Stunden/Tage bis 50 % der Lebenszeit-Views) | **Nicht öffentlich verifizierbar** | — |

---

## 3) Annahmen-Set: 100-Video-Verteilung für einen kompetenten neuen AI-Content-Affiliate-Account (Estimated)

Definition „kompetent": Produktwahl datengestützt (Kalodata o. ä.), Hooks/Skripte aus bewährten Winnern nachgebaut, 3–5 Posts/Tag, US/UK-Markt, keine Violations. Klassen: A = <1k Views, B = 1k–10k, C = 10k–100k, D = ≥100k.

| Szenario | A (<1k) | B (1k–10k) | C (10k–100k) | D (≥100k) | Ø-Views je Klasse (Annahme) | Gesamt-Views (Formel) | Median | Top-5-Video-Anteil |
|---|---|---|---|---|---|---|---|---|
| **Konservativ** | 90 | 8 | 2 | 0 | 250 / 3.000 / 20.000 / – | 90×250 + 8×3.000 + 2×20.000 = **86.500** | ~250 | (2×20k + 3×3k) / 86,5k ≈ **57 %** |
| **Realistisch** | 80 | 15 | 4 | 1 | 300 / 3.500 / 30.000 / 200.000 | 80×300 + 15×3.500 + 4×30.000 + 1×200.000 = **396.500** | ~300–400 | (200k + 4×30k) / 396,5k ≈ **81 %** |
| **Aggressiv** | 65 | 22 | 10 | 3 | 400 / 4.000 / 35.000 / 400.000 | 65×400 + 22×4.000 + 10×35.000 + 3×400.000 = **1.664.000** | ~600–800 | (3×400k + 2×35k) / 1,664M ≈ **76 %** |

Begründung je Szenario:

- **Konservativ** entspricht den dokumentierten „Grind-Phasen": Deniz Sancar (~35 Videos, meist ~500 Views, ein 7k-Video → hochgerechnet ≈ 60k Views/100 Videos), Ecom King (20–30k Views in 30 Tagen), Nadorb (meist <1k), Socialinsider-Mittelwert 350 Views/Post (≈ 35k/100 Videos). Kein 100k-Video; 2 Videos im 10k-Bereich sind das, was Praktiker als „ein Winner pro 30–50 Videos" beschreiben. Wahrscheinlichkeit eines ≥100k-Videos pro Video hier < 0,5 %.
- **Realistisch** entspricht Accounts nach Format-Fit: rMA5MKeyym8 (1/17 bei 900k, wenige bei 8k), Reddit 1u9s0zn (Masse ~1k, dann 100k-Video am Tag 5, 4 Virals in ~3 Monaten ≈ 1 %), Jhonatas' beobachteter Veo-3-Account (Masse 100–300, 1–2 Videos bei 200k–1M). Genau 1 Video ≥100k pro 100 (≈1 %/Video) und 4 Videos 10k–100k. Die Top-5-Videos tragen ~81 % der Views — konsistent mit den Pareto-Claims („98 % des Geldes aus wenigen Videos").
- **Aggressiv** entspricht den besten dokumentierten Serien: Patryk Marketer nach Formatwechsel („viele Videos über 100k/200k/500k in einer Woche"), tommycetty (Top 226k/168k/67k bei 3–5 Posts/Tag), Rosabella-Netzwerk (mehrere Videos im 100k–1,3M-Bereich). 3 Videos ≥100k und 10 im 10k-Bereich pro 100 setzen voraus, dass Brand-Ad-Budget (GMV Max) auf die Winner fließt und der Account nicht gebannt wird.

Korrekturen und Risiken (Estimated):
- **Account-Risiko** dominiert: 24h-Throttles (Pilot-Programm), Violations, Bans (@poormaninla, @melisogn9dl nicht mehr auffindbar; tommycetty: „my main primary account did get banned"). Für Erwartungswert-Rechnungen die Views des jeweiligen Szenarios mit einer Überlebenswahrscheinlichkeit des Accounts multiplizieren (Vorschlag: 0,6 / 0,75 / 0,85 für 90 Tage — reine Annahme, keine Quelle).
- **AI-Publikums-Malus** –10–20 % auf Klasse-B/C-Views bei sichtbar synthetischem Look (Abschnitt 2.8); kein Label-Malus.
- **Markt DE/EU**: Alle Praktiker-Daten stammen aus US/UK; für DE ist die Nutzerbasis kleiner und TikTok Shop jünger → Konservativ-Szenario als Basis (siehe W5-Datei).
- **View → GMV**: Praktiker-Konversion 1 Sale pro 200–5.000 Views je nach Produkt (Abschnitt 2.5); Brand-Erwartung 1/5.000. Für Umsatzmodelle die Klassen-Views mit einer produktabhängigen Rate multiplizieren, nicht mit einem Pauschalwert.

---

## 4) Nicht verfügbar / offen

- **Median-Views neuer Accounts** und **Anteil der Videos je View-Klasse** (öffentlicher Datensatz): Nicht öffentlich verifizierbar. Benchmark-Reports liefern ausschließlich Mittelwerte; Socialinsider bestätigt auf Nachfrage-Prompt explizit „average" ohne Perzentile.
- **Kalodata/Tabcut/EchoTik-Reports zur Video-Performance-Verteilung**: Kalodata-Blog per Cloudflare blockiert (403), Tabcut- und EchoTik-Blogs ohne solche Reports, FastMoss-Blog 404. Der lokal vorliegende EchoTik-Q1-2025-Report enthält nur SEA-Kategorie-GMV.
- **TikTok-Aussage zu Testgruppen/Batch-Rollout**: nicht existent; die Support-Seite „How TikTok recommends content" lieferte per Fetch keinen Text (JS-Rendering).
- **GMV-Anteil der Top-1–5 %-Videos**: nur Einzel-Claims; kein Datensatz.
- **AI-Label-A/B-Test / Agentur-Daten AI-Avatar vs. Mensch auf TikTok Shop**: keine öffentliche Studie gefunden; arXiv 0 Treffer, Semantic Scholar Rate-Limit (429), YouTube-Suche nur Meinungsvideos.
- **„350 % höheres Engagement" (AI-UGC)**: Ursprung nicht auffindbar.
- **Sales-Anteil Suche/Shop-Tab vs. FYP vs. LIVE**: keine öffentliche Aufteilung (US/UK/DE).
- **Halbwertszeit von Shop-Videos**: keine quantitative Quelle.
- **Reddit-Threads 1uf1zxj, 1w2nfnu, 1dsuss1 (Kommentare)**: Arctic-Shift-Timeouts; nur Einzelkommentare aus der Suche verfügbar. Reddit direkt und via r.jina.ai blockiert.
- **Semantic-Scholar-Abfragen**: HTTP 429; keine Ergebnisse.
- Alle YouTube-Publikationsdaten sind aus „x months ago" (Stand 2026-09-24) geschätzt.

---

## 5) Quellen mit Zugriffsdatum (alle 2026-09-24)

Primär / Plattform:
- TikTok Newsroom, „How TikTok recommends videos #ForYou" (2020-06-18): https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
- TikTok Newsroom, „New labels for disclosing AI-generated content" (2023-09-19): https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content
- TikTok Newsroom, „Partnering with our industry to advance AI transparency and literacy" (2024-05-09): https://newsroom.tiktok.com/en-us/partnering-with-our-industry-to-advance-ai-transparency-and-literacy
- TikTok Support, „How TikTok recommends content" (kein Body per Fetch): https://www.tiktok.com/support/faq_detail?id=7655285288050104852
- TikTok Shop Academy (EU/IE), „AI-Generated Content Restrictions and Requirements": https://seller-ie.tiktok.com/university/essay?knowledge_id=6752261875877653&lang=en-GB
- TikTok Shop Academy (US), „AI-Generated Content Restrictions and Requirements": https://seller-us.tiktok.com/university/essay?knowledge_id=491489038501663&lang=en
- TikTok Shop Academy (US), „Content Policy" (Shop Tab Eligibility): https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617&lang=en
- tt_profile.sh-Handle-Checks: @poormaninla, @melisogn9dl → statusCode 10221 (nicht gefunden)

Benchmark-Reports:
- Socialinsider, „TikTok Benchmarks 2026" (publ. 2026-04-22): https://www.socialinsider.io/blog/tiktok-benchmarks/
- Socialinsider, „Social Media Benchmarks 2026": https://www.socialinsider.io/blog/social-media-benchmarks/
- Metricool, „TikTok Study 2026": https://metricool.com/tiktok-study/
- Buffer, „TikTok Algorithm" (11 Mio. Videos): https://buffer.com/resources/tiktok-algorithm/ ; „Best time to post on TikTok" (7,1 Mio. Posts): https://buffer.com/resources/best-time-to-post-on-tiktok/
- Rival IQ, „Social Media Industry Benchmark Report 2025" (2025-02-25): https://www.rivaliq.com/blog/social-media-industry-benchmark-report/
- EchoTik, „TikTok Shop 2025 Q1 Report" (PDF, lokal echotik_q1_2025.pdf): https://echotik.ai
- Hootsuite Social Trends (eMarketer-Zitat): https://www.hootsuite.com/research/social-trends

Akademisch:
- Chen et al., „A Study on the Characteristics of Douyin Short Videos and Implications for Edge Caching", arXiv:1903.12399 (2019-03-29): https://arxiv.org/abs/1903.12399
- Altay & Gilardi, „People are skeptical of headlines labeled as AI-generated, even if true or human-made…", PNAS Nexus 3(10), Okt 2024: https://academic.oup.com/pnasnexus/article/3/10/pgae403/7810648
- „Dynamics of Algorithmic Content Amplification on TikTok", arXiv:2503.20231 (März 2025): https://arxiv.org/abs/2503.20231
- arXiv-Suchen: https://arxiv.org/search/?query=tiktok+recommendation+algorithm+audit&searchtype=all ; https://arxiv.org/search/?query=tiktok+popularity+views+distribution&searchtype=all

Vendor-Seiten (Claims):
- Creatify: https://creatify.ai/ ; Arcads: https://www.arcads.ai/

YouTube (Transkripte via NexLev; Daten ≈ aus „x months ago"):
- Deniz Sancar, „I Tried Faceless AI TikTok Shop Affiliate for 1 Hour…": https://www.youtube.com/watch?v=Tsv7Zt9w9-4
- Patryk Marketer, „I WASTED 30 Days Trying To Make Money With AI Videos on TikTok": https://www.youtube.com/watch?v=NKxTt215kus ; „How I Made $13,000 In One Month With AI Videos…": https://www.youtube.com/watch?v=3Axh5s_iUyA
- Nadorb, „I Tried TikTok Shop for 7 Days (Real Results)": https://www.youtube.com/watch?v=SAuvpusxX4g
- The Ecom King, „I Tried TikTok Shop Affiliate With Sora 2 for 30 Days": https://www.youtube.com/watch?v=W5ThaDXg2ss
- Turner (BatchBot), „I tried AI TikTok Shop Affiliate for 7 days…": https://www.youtube.com/watch?v=DHZ8iI0Sbj0
- Human-Affiliate UK, „I tried TikTok affiliate for 30 days…": https://www.youtube.com/watch?v=rMA5MKeyym8
- tommycetty, „I Had 30 Days to Make $10K With AI Content on TikTok Shop": https://www.youtube.com/watch?v=kjCyL4Vn4P4
- Jhonatas Silva, „HOW I MADE $974 IN 24H ON TIKTOK SHOP WITH POV VIDEOS": https://www.youtube.com/watch?v=Bg5fs8ctzqM
- Amber Sharniece, „I Tried TikTok Shop Affiliates and Here's My Honest Results": https://www.youtube.com/watch?v=CgPX3Po7WFo
- Buzz, „How I Monetized My Faceless TikTok in 7 Days": https://www.youtube.com/watch?v=0eQDpN4lmNE
- Modern Millie, „I posted to TikTok EVERY DAY for 108 days": https://www.youtube.com/watch?v=AoCT5YZycp0
- Mike Yanda, „How to BEAT the TikTok Algorithm in 12 minutes": https://www.youtube.com/watch?v=VgUZJo0qDRc
- David Margaryan, „$0-$33,821 In 30 Days With Faceless Ai TikTok Shop Automation": https://www.youtube.com/watch?v=I_1fpXpUdbE
- Jon Knowles: https://www.youtube.com/watch?v=EMUALbMNV94 ; Moe Alamawi: https://www.youtube.com/watch?v=dgb-xCkZpyc

Reddit (Arctic-Shift-API / lokale Dumps; Daten aus created_utc umgerechnet):
- r/TikTokShop, „TikTok affiliates – How long till you started selling" (~2026-08-30): https://www.reddit.com/r/TikTokshop/comments/1w2ubvm/
- r/TikTokShop, „be honest is anyone here pulling a decent income" (~2026-06-25): https://www.reddit.com/r/TikTokshop/comments/1uf1zxj/
- r/TikTokShop, „reasons why people dont sell" (~2026-08-30): https://www.reddit.com/r/TikTokshop/comments/1w2nfnu/
- r/TikTokShopAffiliate, „tiktok shop for creator" (~2026-09-09): https://www.reddit.com/r/TikTokShopAffiliate/comments/1wba5a1/
- r/TikTokShopAffiliate, „Anyone else having extremely low views" (2024-07-02): https://www.reddit.com/r/TikTokShopAffiliate/comments/1dsuss1/
- r/TikTokShopAffiliate, „I am so lost" (2024-06/07): https://www.reddit.com/r/TikTokShopAffiliate/comments/1draeqq/
- r/TikTokShopAffiliate, „Low views" (2024-06-21): https://www.reddit.com/r/TikTokShopAffiliate/comments/1dleq94/
- r/TikTokShopAffiliate, „Is this normal" (2024-05-27): https://www.reddit.com/r/TikTokShopAffiliate/comments/1d1xgd3/
- r/TikTokShopAffiliate, „Would this affect my views…" (2024-04-18): https://www.reddit.com/r/TikTokShopAffiliate/comments/1brsw1u/
- r/passive_income, „My rollercoaster journey with the TikTok Shop affiliate program" (2026-06-19): https://www.reddit.com/r/passive_income/comments/1u9s0zn/
- r/passive_income, „Running a faceless finance TikTok for 8 months" (~2026-02-24): https://www.reddit.com/r/passive_income/comments/1rdiwob/
- r/passive_income, „nobody scrolling actually cares that your video is ai" (2026-09-05): https://www.reddit.com/r/passive_income/comments/1w7nihc/
- r/Entrepreneurs, „Ai agents are turning random people into ecommerce content sellers…" (2026-04-17): https://www.reddit.com/r/Entrepreneurs/comments/1snwa7t/

Presse:
- 404 Media, „Inside an AI TikTok Shop Slop Factory That Shills Supplements Recalled By the FDA" (lokal 404media.html; Datum im Dump nicht extrahiert): https://www.404media.co/

## Verifikation (adversarial)

Zweitprüfung am 2026-09-24 (alle Quellen per WebFetch erneut geöffnet).

| Metrik | Verdict | Notiz |
|---|---|---|
| Ø Views/Post, TikTok 1–5k Follower (2025: 350; 2024: 860, –59 %) | CONFIRMED | Socialinsider TikTok Benchmarks, veröffentlicht 2026-04-22: Tabelle 1–5K 860 → 350 (–59 %). Basis: 2 Mio. TikTok-Videos von 214.507 aktiven Profilen, Jan 2024–Dez 2025. Nicht spezifiziert, ob organisch oder inkl. Paid; Definition „views per post" = Durchschnitt pro Post im Tier. |
| Ø Views/Post 5–10k / 10–50k / 50–100k / 100k–1M (2025) | CONFIRMED | Gleiche Quelle: 945 / 3.240 / 9.900 / 34.900 (2024: 1.575 / 3.655 / 8.688 / 25.198; Δ –40 % / –11 % / +14 % / +39 %). Kleine Accounts verlieren, große gewinnen. |
| Anteil TikTok-Views aus der For-You-Page (7 von 10) | CONFIRMED | Metricool TikTok Study 2026: wörtlich „The For You Page drives 7 out of every 10 views". Sample 2.314.756 Posts von >92.000 Accounts weltweit. Es handelt sich um Traffic-Quelle (Views), nicht Follower-Anteil. |
| Views-Uplift pro Post bei 11+ Posts/Woche (+34 %; 3–5: +17 %; 6–10: +29 %) | PARTIALLY | Buffer „TikTok algorithm" (Artikel datiert 2025-12-17, Datenbasis 11 Mio. TikToks): Tabelle nennt 2–5x/Woche +17 %, 6–10x +29 %, 11+x +34 %. Abweichung: unterste Stufe ist „2–5", nicht „3–5" (die „3–5 = Sweet Spot" ist eine separate Empfehlung im Text). Die Vergleichsbasis („vs. Basis") wird im Artikel nicht definiert – vermutlich Accounts mit ≤1 Post/Woche, aber nicht belegt. Zahlen als Buffer-eigene Analyse ohne Methodikdetails. |
| TikTok Newsroom: Follower-Zahl und frühere Hits „keine direkten Faktoren"; keine Aussage zu 200/1.000-Testgruppen | CONFIRMED | Newsroom-Post vom 2020-06-18, wörtlich: „neither follower count nor whether the account has had previous high-performing videos are direct factors in the recommendation system." Keine Erwähnung von Testgruppen, Batches oder Initial-Audience-Größen. Achtung: Quelle ist 6 Jahre alt. |
| TikTok Shop Academy: auto-gelabelter AI-Content „no additional penalties or distribution restrictions solely due to the label" | CONFIRMED | Seite „Artificial Intelligence Generated Content (AIGC)" (seller-ie, Stand 28/08/2026), Abschnitt „Platform-Initiated Disclosure": „Content that is auto-disclosed will not face additional penalties or distribution restrictions solely due to the label." Gilt explizit nur für den Label-Effekt; andere Policy-Verstöße werden weiterhin durchgesetzt. Aussage bezieht sich auf Platform-initiierte (automatische) Labels. |
| Effekt „AI-generated"-Label auf wahrgenommene Genauigkeit/Teil-Absicht (n=4.976, 6er-Skala; –0,11 bis –0,17; 3x kleiner als „false") | CONFIRMED | PNAS Nexus 3(10) pgae403, Okt. 2024 (Altay & Gilardi). Studie 1: n=1.976 (US), Effekt –0,17 [–0,29; –0,04]; Studie 2: n=3.003 (US+UK), Effekt –0,11 [–0,19; –0,03]; 6-Punkte-Skalen. „3x kleiner" bezieht sich auf Prozentpunkte: AI-Label 2,66 pp vs. False-Label 9,33 pp. Kontext: Nachrichten-Headlines, nicht TikTok-Videos – Übertragbarkeit auf Shop-Content ist eine Annahme. |
| Douyin-Datensatz 260k Videos: nur populärste Videos folgen Zipf; keine Prozentaufteilung | CONFIRMED | arXiv 1903.12399 (eingereicht 2019-03-29), „A Study on the Characteristics of Douyin Short Videos and Implications for Edge Caching": >260.000 Douyin-Videos über drei Monate; „the most popular Douyin videos follow Zipf's law on video popularity, but the rest of the videos do not." Keine Prozentaufteilung der Views im Abstract. Alt (2019) und Douyin ≠ TikTok-International. |
