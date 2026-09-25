# Benchmark: View-Verteilung pro Video bei neuen/kleinen TikTok-Accounts und TikTok-Shop-Affiliate-Videos

Stand: 2026-09-24 (Erstlauf ohne WebSearch) / 2026-09-25 (Zweitlauf „Erneut versuchen" mit WebSearch + WebFetch + PDF-Volltexten). Zugriffsdatum aller Quellen: 2026-09-24/25.

Tag-Legende: **Verified** = in einem Primärdokument, Report-Volltext oder in TikTok-Daten selbst gesehen; **Claimed** = von Creator/Anbieter/Blog/Redditor behauptet, nicht prüfbar oder nur über Sekundärquelle gesehen; **Estimated** = eigene Rechnung (Formel und Inputs angegeben). „Nicht öffentlich verifizierbar" = keine öffentliche Quelle existiert bzw. auffindbar.

Methodik Zweitlauf: 40+ WebSearch-Abfragen, 45+ WebFetch-Abrufe (TikTok Shop Academy US, TikTok Newsroom, Buffer, Socialinsider, Metricool, Taboola, arXiv, OUP/JCR, Springer/Electronic Markets, Sprout Social, Momentum Works/Tabcut-Sekundärberichte, Graffius), vier Paper-PDFs per PyMuPDF im Volltext geprüft (Bandy & Diakopoulos 2020; Guinaudeau/Munger/Votta 2022; Seeger/Wessel/Lehrer 2026; Sprout Q1-2026-Pulse), dazu NexLev-YouTube-Transkripte. Gesperrt/403: Kalodata-Blog, Momentum-Works-Primärseiten, Inc.com, Dashboardly-Statistikseite, Nature-HSSC-Volltext, tiktok.com/support-FAQ (JS-Rendering). Das WebSearch-Budget der Session war nach ~40 Abfragen erschöpft; danach nur noch WebFetch.

---

## 1) Kurzfazit

1. **Es gibt weiterhin keinen öffentlichen Datensatz mit View-Klassen (<1k / 1k–10k / 10k–100k / 100k+) speziell für neue Accounts oder für TikTok-Shop-Affiliate-Videos.** Kalodata/EchoTik/Tabcut/FastMoss veröffentlichen GMV- und Kanal-Reports, keine Video-View-Verteilungen. → Nicht öffentlich verifizierbar. Es gibt aber jetzt drei belastbare Näherungen (Punkte 2–4).
2. **Bester Median-Anker (Verified):** Buffer, 2025-10-08, 11,4 Mio. TikTok-Posts von >150.000 Accounts: **Median 459–506 Views pro Post** (je nach Posting-Frequenz), **90. Perzentil 3.722 (1 Post/Woche) bis 14.401 Views (11+ Posts/Woche)**. Das heißt über alle Account-Größen hinweg: ~50 % der Videos < ~500 Views, ~90 % < ~4k–14k Views. Socialinsider (2026-04-22, 2 Mio. Videos): Accounts mit 1–5k Followern **Ø 350 Views/Post** (2024: 860; –59 %); Report enthält ausdrücklich keine Mediane.
3. **Bester Verteilungs-Anker aus einem Paper (Verified, aber 2020):** Bandy & Diakopoulos, FAccTRec 2020, 80.682 Videos von 616 gewöhnlichen Nutzern: **86 % der Videos ≤ 1.000 Plays, 37 % ≤ 100 Plays; Top-1 % der Videos = 76 % aller Plays, Top-10 % = 93 %.** Guinaudeau/Munger/Votta 2022 (Computational Communication Research): pro Account Gini der Views **0,70** (Median), das populärste Video eines Accounts hat im Median **64-mal** so viele Views wie sein Median-Video; **Top-20 % der Videos = 75,8 % der Views** eines Accounts.
4. **TikTok selbst (Verified, Zitat TikTok Shop Academy US, Stand 2025-11-26):** Neue Videos kommen in einen „Basic Traffic Pool", der „einer kleinen, diversen Gruppe (around 500 users)" gezeigt wird; bei guter Completion-Rate folgt ein „Larger Traffic Pool", bei Ausnahmeleistung der „Popular Traffic Pool". Das ist die erste offizielle TikTok-Seite, die eine konkrete Testgruppen-Größe nennt (Seller-Education-Text, keine Engineering-Doku). Newsroom (2020): Follower-Zahl und frühere Hits sind „keine direkten Faktoren".
5. **Praktiker-Evidenz** (18 dokumentierte Fälle, alle Claimed) bleibt konsistent: Masse der Videos neuer Affiliate-Accounts bei **100–500 Views**, „ein Winner pro 15–40 Videos", Winner 30k–900k Views. Neu: Ashley Howard (Claimed, verkauft Coaching): 100 Videos/Tag über 3 Accounts, 6 Monate → maximal 4.000 $ Commission/Monat; nach Strategiewechsel mit weniger Videos 20.000 $/Monat — Volumen allein skaliert nicht.
6. **Pareto/GMV (gemischt):** Momentum Works/Tabcut (Verified über zwei Sekundärberichte): 2025 erzielten in den USA **1.785 Creator > 1 Mio. $ GMV** (2024: 529), „mehr als die Hälfte aller US-Stores hatten null Umsatz". Dashboardly/Hamster Garage (Claimed): **Top-0,5 % der Creator = 38 % des Affiliate-GMV**; Inc.com-Fallstudie (Claimed): von 112 onboardeten Affiliates lieferten **18 (16 %) den gesamten GMV** (412.000 $), **27 % machten nie einen Sale**, ~60 % posteten kein zweites Video. Video-Level-Pareto (Top-1–5 % der Videos → GMV) bleibt nicht öffentlich verifizierbar; Estimated: Top-5 % der Videos ≈ 75–85 % der Views, GMV-Anteil ≥ 85 %.
7. **Videos bis zum ersten Sale (Claimed):** Bandbreite 15–70 Videos (5–14 Tage bei 3–10 Posts/Tag), Ausreißer Tag 1 bis 3–6 Monate; 27 % der Affiliates einer Brand-Kohorte nie. Strukturelle Bremse (Verified, TikTok Shop Academy 2025-06-23): **Creator Pilot Program** für 1.000–5.000 Follower: 30 Tage, **max. 5 Shoppable Videos + 3 Shoppable LIVEs pro Woche**, nur Produkte mit Shop-Performance-Rating ≥ 95 %, Aufhebung ab > 5.000 Follower.
8. **AI-Label und Reichweite — jetzt mit harter Evidenz:** (a) **Carney/Riveros/Tully, Journal of Consumer Research, 2026-05-07 (Verified, Abstract/Artikelseite):** 8 präregistrierte Experimente + Feldanalyse von **1.135.817 TikTok-Posts von 8.650 Creatorn**: Posts mit AIGC-Disclosure erhalten **„roughly 7 %–8 % fewer likes and 7 % less combined engagement"**; Mechanismus = geringere parasoziale Bindung (wahrgenommener Aufwand), nicht Qualität; Disclosures, die Aufwand signalisieren, mildern den Effekt. (b) Seeger/Wessel/Lehrer, Electronic Markets 2026-03-23 (Verified, Volltext): n = 325 + 371, simulierte Instagram-Profile: Labels „AI-generated"/„AI-enhanced" senken affektives und verhaltensbezogenes Engagement, stärker bei emotionalem Content; späte Disclosure hilft nur bei AI-enhanced. (c) TikTok-Policy (Verified): auto-gelabelter Content erhält „no additional penalties or distribution restrictions solely due to the label"; aber TikTok testet seit 2025-11-19 einen Nutzer-Regler „weniger AI-Content" (Manage Topics) — ein **nutzerseitiger** Reichweiten-Dämpfer für gelabelte Videos. (d) Taboola + Columbia/Harvard/TUM/CMU (2026-01-28, Verified Pressemitteilung, Native Ads, nicht TikTok): AI-Ads CTR 0,76 % vs. 0,65 % human; **AI-Ads, die nicht nach AI aussehen, performen am besten**, AI-Ads, die als künstlich erkannt werden, am schlechtesten. (e) Vendor-Zahlen: „350 % höheres Engagement" (videotok.app, ohne Quelle) und „AI-gelabelt 1,9 % vs. 3,4 % Engagement, Sprout Q1 2026" (greenfroglabs) sind **nicht** in den Primärquellen enthalten — das Sprout-Q1-2026-Pulse-PDF enthält keine solche Zahl → Nicht öffentlich verifizierbar / vermutlich erfunden.
9. **Halbwertszeit / Shop-Tab / Suche:** Graffius (2026-Edition, 5,6 Mio. Posts, Verified): TikTok-Halbwertszeit des Engagements **„0 Minuten, mit Ausnahmen"** (Instagram 18,3 h, YouTube 10,6 Tage) — Engagement ist extrem frontlastig, außer bei viralen Videos. **Kanal-Split US-TikTok-Shop 2025 (Momentum Works/Tabcut, Verified via TechNode + Contentgrip): Video 50 %, Shop-Tab 36 %, LIVE 14 % (2024: 10 %) des GMV.** Metricool (2,3 Mio. Posts): 7 von 10 Views kommen aus der For-You-Page. Die Blog-Behauptung „Suche treibt 48–65 % der TikTok-Shop-Sales" (Zonflip, 2026-03-27) ist unbelegt und widerspricht dem Tabcut-Split (Shop-Tab inkl. Suche insgesamt 36 %).
10. **Abgeleitete 100-Video-Verteilung (kompetenter neuer AI-Affiliate-Account, Estimated), Klassen <1k / 1k–10k / 10k–100k / ≥100k:** konservativ **90 / 8 / 2 / 0**, realistisch **80 / 15 / 4 / 1**, aggressiv **65 / 22 / 10 / 3**. Kalibrierung: Buffer-p90 (10 % der Videos ≥ 14k bei 11+ Posts/Woche, alle Account-Größen) ≈ Obergrenze „aggressiv"; Bandy-Verteilung (14 % > 1k, gewöhnliche Nutzer 2020) ≈ „konservativ"; AI-Disclosure-Malus –7…–8 % auf Likes (JCR) ist eingepreist. Herleitung in Abschnitt 3.

---

## 2) Daten und Benchmarks (mit Tag, Quelle, Datum)

### 2.1 Plattform-Benchmarks (Vendor-Reports)

| Kennzahl | Wert | Tag | Quelle / Datum |
|---|---|---|---|
| **Median Views pro Post** nach Posting-Frequenz (1 / 2–5 / 6–10 / 11+ Posts pro Woche) | **489 / 506 / 487 / 459** | Verified (Report-Zahl) | Buffer „How Often Should You Post on TikTok", publ. 2025-10-08, 11,4 Mio. Posts / >150.000 Accounts, Fixed-Effects-Regression — https://buffer.com/resources/how-often-should-you-post-on-tiktok/ |
| **90. Perzentil Views pro Post** (gleiche Klassen) | **3.722 / 6.983 / 10.092 / 14.401** | Verified (Report-Zahl) | ebd. |
| „Viral Ratio" (p90 / Median) | 7,6x / 13,8x / 20,7x / 31,4x | Verified (Report-Zahl) | ebd. |
| Views-Uplift pro Post vs. 1 Post/Woche | 2–5: +17 %; 6–10: +29 %; 11+: +34 % | Verified (Report-Zahl) | ebd.; identische Tabelle in https://buffer.com/resources/tiktok-algorithm/ |
| Ø Views pro Post, Accounts 1–5k Follower | 2025: **350** (2024: 860, –59 %) | Verified (Report-Zahl) | Socialinsider „TikTok Benchmarks 2026", publ. 2026-04-22, 2 Mio. Videos / 214.507 Profile, Jan 2024–Dez 2025 — https://www.socialinsider.io/blog/tiktok-benchmarks/ (Fetch 2026-09-25 bestätigt Tabelle; „presents only averages") |
| Ø Views pro Post, 5–10k / 10–50k / 50–100k / 100k–1M | 945 / 3.240 / 9.900 / 34.900 (2025) | Verified (Report-Zahl) | ebd. |
| Engagement-Rate nach Views | 4,20 % (2025) | Verified (Report-Zahl) | ebd. |
| Anteil Views aus For-You-Page | „7 von 10 Views" | Verified (Report-Zahl) | Metricool TikTok Study 2026, publ. 2026-05-12, 2.314.756 Posts / >92.000 Accounts — https://metricool.com/tiktok-study/ |
| Anteil Accounts <100k Follower, die 2025→2026 wuchsen | 44 % | Verified (Report-Zahl) | ebd. |
| Median Engagement-Rate (Brands, nach Followern) | 2,01 %; 2,0 Videos/Woche | Claimed (Suchtreffer-Zusammenfassung; Reportseite nicht direkt geladen) | Rival IQ 2026 Social Media Industry Benchmark Report, 150 Firmen × 18 Branchen — https://www.rivaliq.com/blog/social-media-industry-benchmark-report/ |
| Ø Views pro TikTok „~18.000" (747.000 Videos), Small Accounts <5k Follower „~43 Views je 100 Follower"; Median „vermutlich im niedrigen Tausender- oder Hunderterbereich" | — | Claimed (Vendor-Blog, Methodik nicht offengelegt) | AdManage.ai — https://admanage.ai/blog/average-tiktok-views |
| „Good/Great/Elite"-Views für Nano-Creator (1–10k Follower): 1–5k / 5–25k / 25k+ | — | Claimed (Blog-Aggregat aus Statista/Dash Hudson/Socialinsider, ohne eigene Daten) | MomentIQ — https://bemomentiq.com/blog/tiktok-shop-content-performance-benchmarks-what-good-great-elite |
| Median-Views **nur neuer Accounts** / View-Klassen für Shop-Videos | **nicht enthalten** | — | Buffer, Socialinsider, Metricool, Rival IQ: keine Aufschlüsselung nach Account-Alter oder Shop-Verknüpfung |

Einordnung (Estimated): Buffer-Median ≈ 490 gilt über alle Account-Größen (inkl. großer Accounts). Für einen neuen Account ohne Follower liegt der Median darunter; die Socialinsider-Klasse 1–5k Follower (Ø 350, Mittelwert, also nach oben verzerrt) und die Praktiker-Berichte (Modus 100–500) stützen einen Median von **~200–400 Views** für neue, kompetente Accounts. Bei 100 Videos ergibt der Socialinsider-Mittelwert **~35.000 Gesamt-Views** (350 × 100); mehrere AI-Challenge-Accounts (Ecom King 20–30k Views/30 Tage; Deniz Sancar ~35 Videos, „meist ~500 Views") liegen genau dort.

### 2.2 TikTok-eigene Aussagen zur Verteilung neuer Videos

| Aussage | Tag | Quelle / Datum |
|---|---|---|
| „When you post a video, it enters the **Basic Traffic Pool**, shown to a small, diverse group (**around 500 users**) to gauge initial engagement through watch time, likes, and comments." — „Strong performance, based on metrics like completion rate, propels the video to the **Larger Traffic Pool**." — „exceptional performance unlocks the coveted **Popular Traffic Pool**, where your video reaches a massive audience beyond your followers on the For You Page." | **Verified (Zitat TikTok Shop Academy US)** | „How TikTok Recommends Content to New Users", Stand 2025-11-26 — https://seller-us.tiktok.com/university/essay?knowledge_id=2410858052077355 (auch als Kurs: https://seller-us.tiktok.com/university/course?learning_id=2852280135698218&content_id=2410858052077355&lang=en). Hinweis: Seller-Education-Text; keine Aussage, wie viele Videos die Pools erreichen. |
| „neither follower count nor whether the account has had previous high-performing videos are direct factors in the recommendation system"; „a video is likely to receive more views if posted by an account that has more followers" | Verified (Zitat) | TikTok Newsroom „How TikTok recommends videos #ForYou", 2020-06-18 — https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you |
| Sechs Traffic-Quellen für Shop-Content: FYP (Feed Video Head / Feed Live Cell / Feed Follow), Following, Shop Tab, Live Merge, Search, Message Inbox — **keine Prozentangaben** | Verified (Fehlanzeige) | TikTok Shop Academy „6 Traffic Sources on TikTok Shop", Stand 2025-11-05 — https://seller-us.tiktok.com/university/course?learning_id=2852280135698218&content_id=2097818908297003&lang=en |
| **Creator Pilot Program**: „1,000 to 5,000 followers"; automatische Einschreibung für 30 Tage nach Affiliate-Freischaltung; „You can post a maximum of **5 Shoppable Videos and 3 Shoppable LIVEs each week**"; Produkte nur mit „shop performance rating of at least 95%"; „If your follower count goes beyond 5,000 during the program, you'll automatically lift restrictions" | Verified (Zitat) | TikTok Shop Academy US „Creator Pilot Program Feature Guide", Stand 2025-06-23 — https://seller-us.tiktok.com/university/essay?knowledge_id=7264111224227597&lang=en. Abweichung: Suchtreffer/andere Regionen nennen „3 Shoppable Videos pro Tag" (seller-mx knowledge_id=8901071687354128, nicht geladen) — Limits sind offenbar regional/zeitlich unterschiedlich. |
| Shop-Tab-/Search-Analytics: Traffic-Quellen „Shop Tab (recommendations and channels), Search, Order center, Livestream and video, Direct message, Other"; „Revenue generated through non-live and non-video channels is considered **Product Card revenue**" — keine Anteile | Verified (Zitat/Fehlanzeige) | „Shop Tab & Search Analytics", Stand 2026-05-22 — https://seller-us.tiktok.com/university/essay?knowledge_id=6276577063585582&lang=en |
| Shop Tab: Produkte sind automatisch enthalten („products listed on TikTok Shop are automatically included in the Shop Tab channel"); Discovery über „search, category feeds, and product recommendations"; Statistik nur als „TikTok Shop Internal Data from US market, August 2023" ohne Zahlen | Verified (Zitat/Fehlanzeige) | „The Seller Guide to Shop Tab Success", Stand 2026-05-14 — https://seller-us.tiktok.com/university/essay?knowledge_id=8750609034250026&lang=en |
| Shop-Content muss „Shop Tab Eligibility Requirements" erfüllen, um „on the homepage or in recommendations" zu erscheinen | Verified (Zitat) | TikTok Shop Academy US „Content Policy" — https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617&lang=en |
| Support-Seite „How TikTok recommends content" | kein Body per Fetch (JS) | — | https://www.tiktok.com/support/faq_detail?id=7655285288050104852 |
| Creator-Folklore „200 Leute, dann 1.000 …" | Claimed | YouTube rMA5MKeyym8 [9:22]; Mike Yanda VgUZJo0qDRc („stalls videos at 200 views"); Reddit r/TikTokShopAffiliate 2024-06 |

### 2.3 Akademische Evidenz zur View-Verteilung

| Befund | Tag | Quelle / Datum |
|---|---|---|
| **80.682 TikTok-Videos** von 616 Nutzern (bis zu 500 jüngste Videos je Nutzer, Juni 2020): „the overall distribution of play count was extremely skewed: **86% of videos had a play count of 1,000 or less, and 37% had a play count of 100 or less**. The play counts generally exhibited a 'long tail' distribution, as the **top 1% of videos in the dataset claimed 76% of all plays, and the top 10% of videos claimed 93%**." | **Verified (PDF-Volltext)** | Bandy & Diakopoulos, „#TulsaFlop: A Case Study of Algorithmically-Influenced Collective Action on TikTok", FAccTRec '20, arXiv:2012.07716 (eingereicht 2020-12-14) — https://arxiv.org/abs/2012.07716. Caveat: Nutzer wurden über politische Call-to-Action-Videos gesampelt (nicht zufällig), Baseline-Videos sind aber deren normale Uploads; Daten von 2020. |
| Pro Account: **Gini-Koeffizient der Views Median 0,70** auf TikTok (YouTube 0,62); **Peak-Median-Ratio Median 64** (populärstes Video = 64 × Median-Video; YouTube 40); „on TikTok the **top 20% of the videos rake in 75.76% of views**" (YouTube 72,52 %) | **Verified (PDF-Volltext)** | Guinaudeau, Munger, Votta, „Fifteen Seconds of Fame: TikTok and the Supply Side of Social Video", Computational Communication Research 4(2), 2022 — https://kmunger.github.io/pdfs/tiktok.pdf |
| 24.992.678 Videos von 6.973.120 Nutzern (Okt 2014–Dez 2019): „content production, and especially the most popular content, is mostly driven by a small elite of super-users" | Claimed (Abstract via Suchtreffer; Volltext hinter Cookie-Redirect) | „The broadcasting trap: TikTok and the 'democratization' of digital content production", Humanities & Social Sciences Communications 2025 — https://www.nature.com/articles/s41599-025-04797-w |
| Douyin, >260.000 Videos über 3 Monate: nur die populärsten Videos folgen Zipf; keine Prozentaufteilung | Verified (Abstract) | Chen et al., arXiv:1903.12399, 2019-03-29 |
| Audit-Studien untersuchen Nutzer-Personalisierung, nicht Creator-Exposure (z. B. „rapid reinforcement … within the first 200 videos watched") | Verified (Abstract) | arXiv:2503.20231 (März 2025); arXiv:2201.12271; arXiv:2607.17356 |
| „Understanding Indicators of Virality in TikTok Short Videos" (Ling et al., 2021): Prädiktoren von Viralität, **keine** Verteilungsprozente | Verified (PDF geprüft, Fehlanzeige) | arXiv:2111.02452 |

### 2.4 Praktiker-Beobachtungen: View-Verteilung neuer (AI-)Affiliate-Accounts (alle **Claimed**, selbstberichtet)

| # | Wer / Setting | Beobachtete Verteilung | Quelle / Datum |
|---|---|---|---|
| 1 | Deniz Sancar, UK, brandneuer AI-Faceless-Affiliate-Account, 5 Tage, 5–8 Videos/Tag (≈30–40 Videos) | „most videos got stuck around 500 views"; ein Video 7.000 Views → 8 Verkäufe; 24h-Sperre durch Pilot-Programm; Erlös < £50 | YouTube Tsv7Zt9w9-4 [4:14, 4:54, 5:16] |
| 2 | Patryk Marketer, Sora-2-AI-Clips (Kleidung), 5–10 Videos/Tag über Wochen | „a lot of these videos didn't even go past 100 views… stuck in the 30, 15 views"; nächste Woche „zero to 100 views… a couple that got 200" | YouTube NKxTt215kus, ~Dez 2025 [5:55–6:02, 8:20–8:35] |
| 3 | Patryk Marketer, nach Formatwechsel (Bodycam-Style) | „a lot of videos that week that got over 100,000, 500,000, 200,000 views"; 13.000 $ GMV / ~2.000 $ Commission im Monat | YouTube 3Axh5s_iUyA [12:54–13:01] |
| 4 | Nadorb, UK, 7-Tage-Challenge, AI-Influencer | „Most of these videos didn't even get over 1,000 views"; £2 Commission | YouTube SAuvpusxX4g [11:10] |
| 5 | The Ecom King, Sora-2-AI-Avatare, 30 Tage | Account gesamt „around about 20 to 30,000 views"; 200–300 $ Umsatz | YouTube W5ThaDXg2ss [13:51], ~Nov/Dez 2025 |
| 6 | Turner (BatchBot), voll-AI, 5–10 Videos/Tag | erster Sale nach „a whole week"; 3,5k $ Commission in Monat 1 und 2; Test-Account Tag 1: 6 Items, 11 $ Commission | YouTube DHZ8iI0Sbj0 [0:44, 18:06–18:13], ~Aug 2025 |
| 7 | Human-Affiliate (UK), 30 Tage, 17 Posts | ein Video 900.000 Views, „a few on like 8K", „the rest kind of flopped"; Winner-Heuristik „3 to 5K views within the first 12 to 24 hours" | YouTube rMA5MKeyym8 [9:02, 22:24, 23:30], Herbst 2025 |
| 8 | tommycetty, AI-Content, 3–5 Posts/Tag, ~11 Accounts | Top-Videos 226k / 168k / 67k; „You're not going to have every single video pop off"; 7,41 $ netto je 1.000 Views auf Winnern; Hauptaccount gebannt | YouTube kjCyL4Vn4P4 [1:39–2:48, 10:27], ~März 2026 |
| 9 | Jhonatas Silva über fremden Veo-3-Account | „100, 200, 300 … but one or two get 1 million, another gets 200,000 and these videos compensate" | YouTube Bg5fs8ctzqM, ~Jul 2026 |
| 10 | Amber Sharniece (human), 1 Video/Tag | Monat 1: 12 Items, ~84 $; Monat 2: 103 Items, 5.300 $ GMV, ~539 $ | YouTube CgPX3Po7WFo, ~Jul 2026 |
| 11 | Reddit r/passive_income, 8k Follower, AI-Videos, 3–5 Posts/Tag | „videos sat around 1k views with 0 sales. But on day 5 … first sale … one video 100k views and almost $10k in GMV … 4 viral videos"; ~2k $/Monat | https://www.reddit.com/r/passive_income/comments/1u9s0zn/ , 2026-06-19 |
| 12 | Reddit r/passive_income, Faceless-Finance | „Posted 8 videos over two weeks. Best one got 340 views. Most got under 100." | /r/passive_income/comments/1rdiwob/ , ~2026-02-24 |
| 13 | Reddit r/TikTokShopAffiliate, 2.600 Follower | „I average 200-300 every video. Now they're not even hitting 50-100." | /r/TikTokShopAffiliate/comments/1dsuss1/ , 2024-07-02 |
| 14 | Reddit r/TikTokShopAffiliate | „I've hardly ever see anything over 200 views… no sells" | /r/TikTokShopAffiliate/comments/1draeqq/ , 2024-06/07 |
| 15 | Reddit r/TikTokShop | „2 weeks to get my first sale, I average 500 - 1 k views." | /r/TikTokshop/comments/1uf1zxj/ , ~2026-06-25 |
| 16 | Buzz, neuer Clip-Account (kein Affiliate) | Video 1: 800, Video 2: 800.000, Video 3: 500.000 Views, „all from the FYP" | YouTube 0eQDpN4lmNE, ~Feb 2026 |
| 17 | Modern Millie (human) | 126 TikToks in 108 Tagen → +251 Follower | YouTube AoCT5YZycp0, ~Nov 2025 |
| 18 | 404 Media: AI-Ärzte-Netzwerk (@poormaninla) | einzelne AI-Videos „hundreds of thousands or millions of views"; Account am 2026-09-24 nicht mehr auffindbar (tt_profile.sh statusCode 10221) | 404 Media (lokaler Dump); Handle-Check Verified |
| 19 | **Ashley Howard**, 3 Shop-Accounts, „100 videos every single day" (20–40 je Account) über 6 Monate | „my biggest month ever on TikTok shop was $4,000 in commission"; nach Coaching-Strategiewechsel „$8,000 in my first week of March … over $20,000" bei „a fraction of the work" — Volumen ohne Produkt-/Skript-Strategie skaliert nicht (Interessenkonflikt: bewirbt Coaching) | YouTube b13n1YbKl9Q „What I Learned Posting 100 TikTok Shop Videos a Day (And Why It Failed)", ~Jan 2026 [0:00–1:22, 9:03–9:32] |

Beobachtung (Estimated): Modus neuer Affiliate-Videos 100–500 Views, Median eines kompetenten neuen Accounts ~200–400 Views; „Winner" (≥10k) etwa alle 15–40 Videos; „Big Winner" (≥100k) 0–3 pro 100 Videos. Das deckt sich mit Bandy (86 % ≤ 1k) und dem Buffer-Median (~490 über alle Accounts).

### 2.5 „X von N Videos"-Ratios (alle Claimed, außer wo markiert)

| Ratio | Tag | Quelle |
|---|---|---|
| 10 % der Videos ≥ 3.722 Views (1 Post/Woche) bzw. ≥ 14.401 Views (11+ Posts/Woche) — alle Account-Größen | **Verified (Report-Perzentil)** | Buffer 2025-10-08 |
| 14 % der Videos > 1.000 Plays; 1 % der Videos = 76 % der Plays (2020) | **Verified (Paper)** | Bandy & Diakopoulos 2020 |
| 1 von 17 Posts (900k), „a few" bei 8k, Rest Flop | Claimed | rMA5MKeyym8 |
| 1 von 3 Videos = 800k (Clip-Account, kein Shop) | Claimed | 0eQDpN4lmNE |
| „ein bis zwei" Millionen-/200k-Videos bei Masse 100–300 | Claimed | Bg5fs8ctzqM |
| 4 virale Videos in ~3 Monaten bei 3–5 Posts/Tag (≈300–450 Videos → ≈1 %) | Claimed | Reddit 1u9s0zn |
| „Give a product 3 to 5 videos before you write it off" | Claimed | /r/TikTokShopAffiliate/comments/1wba5a1/ , ~2026-09-09 |
| Brand-Erwartung „1 sale from every 5k views"; Creator „1k views before first sale" | Claimed | /r/TikTokShopAffiliate/comments/1d1xgd3/ , 2024-05-27 |
| „Creators posting five or more times per week see 3.2× higher GMV" als bei 2×/Woche | Claimed (Blog „Short Form Nation", ohne Methodik) | via Hamster Garage — https://www.hamstergarage.com/article/tiktok-shop-affiliate-statistics-benchmarks-roi |
| Eine explizite Aussage „X von 100 Videos erreichen 10k+" existiert in keiner Quelle | — | — |

### 2.6 Pareto / GMV-Konzentration

| Befund | Tag | Quelle |
|---|---|---|
| US-TikTok-Shop 2025: GMV 15,1 Mrd. $ (+68 %); **1.785 Influencer > 1 Mio. $ GMV** (2024: 529); „more than half of all US stores recorded zero sales"; „Nine of the top ten US TikTok Shop influencers by GMV in 2025 relied primarily on live commerce" | Verified (Report-Zahlen über zwei Sekundärberichte; Primär-PDF kostenpflichtig, Seiten 403) | Momentum Works × Tabcut „TikTok Shop in the U.S. 2025" (Feb 2026) — via https://www.contentgrip.com/tiktok-shop-data-analysis/ und https://thelowdown.momentum.asia/new-report-tiktok-shop-u-s-gmv-grew-68-to-reach-us15-1b-in-2025/ (403) |
| H1 2025 US: Top-Influencer „over 90 percent of their GMV coming from livestreams"; nur 1 LIVE > 1 Mio. $ (2024: 4) | Verified (Sekundärbericht) | TechNode Global, 2025-08-04 — https://technode.global/2025/08/04/tiktok-shop-doubles-global-gmv-in-h1-with-u-s-market-hitting-5-8b-momentum-works-tabcut-report/ |
| „top 0.5% of creators (roughly 4,000 accounts) drive 38% of all affiliate GMV"; „59% of affiliate creators churn by month 12"; „Affiliate creator content drives 42% of all US TikTok Shop GMV" | Claimed (Blog-Aggregat Dashboardly/Hamster Garage/Branvas, Methodik nicht offengelegt, Statistikseite nicht ladbar) | https://www.hamstergarage.com/article/tiktok-shop-affiliate-statistics-benchmarks-roi ; https://www.dashboardly.io/statistics/tiktok-shop-affiliate-creator-statistics ; https://www.branvas.com/blogs/news/tiktok-shop-statistics |
| Top-1 % der US-Seller ≈ 60 % des GMV; >50 % der 475.000 US-Shops null Umsatz | Claimed (Marketplace Pulse, via Branvas) | https://www.branvas.com/blogs/news/tiktok-shop-statistics |
| Brand-Fallstudie (Küchengadget, Anfang 2025): **112 Affiliates onboardet; ~60 % posteten nie ein zweites Video; 27 % machten nie einen Sale; 18 Creator (16 %) → 412.000 $ GMV / 92.000 $ Commission** | Claimed (Inc.com-Artikel; Seite 403, Text via Suchtreffer) | https://www.inc.com/temilola-agbede/tiktok-shop-is-booming-most-brands-still-arent-making-money/91378937 |
| Top-10 US-Creator (30 Tage): „82.3% of revenue came from video, just 17.7% from livestreams" | Claimed (Kalodata-X-Post, nicht geladen) | https://x.com/kalodata/status/2092265687536345597 |
| Kalodata: Content (Video + LIVE) ≈ 76 % des globalen GMV; „influencer-driven sales in the U.S. … as much as 70.9%" | Claimed (Kalodata-Blog, Cloudflare 403, via Suchtreffer) | https://www.kalodata.com/blog/tiktok/best-tiktok-shop-analytics-tool-2026/ |
| „All my videos that's currently making me 98% of my money was posted in late April/early May" | Claimed | /r/TikTokShopAffiliate/comments/1dleq94/ , 2024-06-21 |
| GMV-Max-Mechanik: Brands legen Ad-Budget auf das Video mit der höchsten CTR („This video with 200 views… is going to turn into over a million views") | Claimed | YouTube I_1fpXpUdbE [3:09–3:36]; EMUALbMNV94; dgb-xCkZpyc |
| Thailand Q1 2025: Top-10-Kategorien = 86 % GMV; 850.000 Creator bei ~110–200k Videos/Monat | Verified (Report-Zahl) | EchoTik Q1-2025-PDF (lokal) |
| **Anteil der Top-1–5 % Videos am Affiliate-GMV** | **Nicht öffentlich verifizierbar** | — |

Estimated: Auf Video-Ebene liefert Bandy (Top-1 % = 76 % der Plays, Top-10 % = 93 %) und Munger (Top-20 % = 76 % je Account) die Views-Seite. In der realistischen 100-Video-Verteilung (Abschnitt 3) entfallen ~81 % der Views auf die Top-5-Videos. Da Sales nichtlinear mit Views skalieren (nur Winner werden von GMV-Max-Budget verstärkt und in Shop-Tab-Empfehlungen gezogen), ist der GMV-Anteil der Top-5 % eher **≥ 85–90 %**. Auf Creator-Ebene (Dashboardly, Inc.-Fall) ist die Konzentration ähnlich: 16 % der Creator einer Kohorte = 100 % des GMV.

### 2.7 Videos / Tage bis zum ersten Sale

| Fall | Posts/Tag | Zeit bis 1. Sale | ≈ Videos (Estimated = Posts/Tag × Tage) | Tag | Quelle |
|---|---|---|---|---|---|
| Turner (AI) | 5–10 | 1 Woche | 35–70 | Claimed | DHZ8iI0Sbj0 |
| Reddit 1u9s0zn (AI) | 3–5 | Tag 5 | 15–25 | Claimed | r/passive_income 2026-06-19 |
| Reddit 1w2nfnu | 20 | „20 videos per day to get my first sale" | ≥ 20 | Claimed | /r/TikTokshop/comments/1w2nfnu/ , ~2026-08-30 |
| Reddit 1uf1zxj | k. A. | 2 Wochen (Ø 500–1k Views) | k. A. | Claimed | ~2026-06-25 |
| Thread „How long till you started selling" | 2–3 | „a day or 2" bis „3-6 months"; „15 days in… no sales yet" | 5–45+ | Claimed | /r/TikTokshop/comments/1w2ubvm/ , 2026-08/09 |
| Amber Sharniece (human) | 1 | innerhalb Monat 1 | ≤ 30 | Claimed | CgPX3Po7WFo |
| Deniz Sancar (AI) | 5–8 | innerhalb 5 Tagen | ≤ 40 | Claimed | Tsv7Zt9w9-4 |
| Turner Test-Account | ~10 | Tag 1 | ~10 | Claimed | DHZ8iI0Sbj0 [18:06] |
| Brand-Kohorte 112 Affiliates | k. A. | **27 % nie**; ~60 % nur 1 Video | — | Claimed | Inc.com (s. 2.6) |
| Vendor: „70% of beta testers made their first sale within the first week" | — | — | — | Claimed (Anbieter) | /r/Entrepreneurs/comments/1snwa7t/ , 2026-04-17 |
| Strukturelle Bremse: Pilot-Programm max. 5 Shoppable Videos/Woche (US, 2025-06-23) bis 5.000 Follower | — | — | → in 30 Tagen max. ~20 Shoppable Videos | **Verified** | TikTok Shop Academy (s. 2.2) |

Estimated Zusammenfassung: Median ≈ 7–10 Tage bzw. ≈ 20–40 Videos bis zum ersten Sale bei 3–5 Posts/Tag; ~15–25 % der Starter berichten ≥ 4 Wochen ohne Sale; in einer Brand-Kohorte 27 % nie. Wichtig: Wenn das Pilot-Programm greift (1.000–5.000 Follower, US-Regel „5 Shoppable Videos/Woche"), sind nur ~20 der ersten 100 Videos überhaupt shoppable — die übrigen 80 zählen für Reichweite, aber nicht für Sales. Selektionsbias: Erfolglose posten seltener Rückblicke.

### 2.8 AI-Label / „AI-Look" und Reichweite

| Befund | Tag | Quelle / Datum |
|---|---|---|
| **Feldanalyse: 1.135.817 TikTok-Posts von 8.650 Creatorn** + 8 präregistrierte Experimente: „posts with AIGC disclosures receive **roughly 7%–8% fewer likes and 7% less combined engagement**"; Mechanismus: „AIGC disclosures reduce parasocial connection … because disclosures signal lower perceived effort"; „disclosures that signal greater effort can mitigate reductions in engagement" | **Verified (Artikelseite/Abstract OUP)** | Carney, Riveros & Tully, „Made With AI: Consumer Engagement With Social Media Containing AI Disclosures", Journal of Consumer Research, publ. 2026-05-07, DOI 10.1093/jcr/ucag013 — https://academic.oup.com/jcr/advance-article/doi/10.1093/jcr/ucag013/8672493 ; Sekundär: Science Says 2026-06-30 (Effort –15,6 %, Connection –14,5 %; Paywall) — https://app.sciencesays.com/p/made-with-ai-gets-lower-engagement |
| Zwei Online-Experimente (n = 325; n = 371, Prolific, simulierte Instagram-Profile mit Labels human-created / AI-enhanced / AI-generated): „labeling content as AI-generated or AI-enhanced reduced both affective and behavioral engagement compared to human-created content", besonders bei emotionalem Content; späte Disclosure mildert nur bei AI-enhanced | **Verified (PDF-Volltext)** | Seeger, Wessel & Lehrer, Electronic Markets 36:31, angenommen 2026-02-03, publ. 2026-03-23 — https://link.springer.com/article/10.1007/s12525-026-00883-2 ; Open-Access-PDF https://www.db-thueringen.de/servlets/MCRFileNodeServlet/dbt_derivate_00071052/12525_2026_Article_883.pdf |
| „AI-generated"-Label senkt wahrgenommene Genauigkeit/Teil-Absicht um 0,17 bzw. 0,11 Punkte (6er-Skala), n = 1.976 + 3.003; dreimal kleiner als „false"-Label | Verified (Studie; Headlines, nicht Video) | Altay & Gilardi, PNAS Nexus 3(10), Okt 2024 — https://academic.oup.com/pnasnexus/article/3/10/pgae403/7810648 |
| Probability-Sample n = 3.861: AI-Label senkt wahrgenommene Genauigkeit und Interesse; keine Wirkung auf Policy-Support; „effects … are limited in scope" | Verified (Abstract) | Wang, Sturgis & de Kadt, arXiv:2506.16202 (rev. 2026-02-11) — https://arxiv.org/abs/2506.16202 |
| n = 7.579 (USA), zwei präregistrierte Experimente: alle getesteten Labels senkten Glauben an und Teil-Absicht für irreführende AI-Bilder | Verified (PDF) | Wittenberg, Epstein, Péloquin-Skulski, Berinsky & Rand, PNAS Nexus 4(6), Mai 2025 — https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/9/583/files/2026/01/labelingaigenerated_2025.pdf |
| Native-Ads-Feldstudie (>500 Mio. Impressions, 3 Mio. Klicks): **AI-Ads CTR 0,76 % vs. human 0,65 %**; „AI ads that did not 'look like AI' achieved the highest engagement of all groups, significantly outperforming both human-made ads and AI ads that were perceived as artificial"; „presence of a large, clear human face" als Trust-Cue; keine Conversion-Einbuße | Verified (Pressemitteilung; Vendor-Ko-Autorschaft, Taboola-Netzwerk, **nicht** TikTok) | Taboola × Columbia/Harvard/TUM/CMU, 2026-01-28 — https://www.taboola.com/press-releases/genai-ads-study-2026/ |
| 1,2 Mio. Posts, 15.000 Poster (TikTok u. a.): AI-**assistierte** Posts Median-Engagement 5,87 % vs. 4,82 %; TikTok 6,14 % vs. 4,17 % — Erklärung: mehr Output; AI-Assistenz ≠ AI-generiertes Video; Selbstselektion | Verified (Report) | Buffer, 2024-10-15 — https://buffer.com/resources/ai-assistant-post-performance/ |
| Konsumenten-Pulse (Q1 2026): Top-Wunsch an Brands = „Posting AI-generated content without labels (28 %)" aufhören; Vertrauensverlust u. a. durch „unregulated AI slop (20 %)". **Keine** Engagement-Zahl „1,9 % vs. 3,4 %" im Dokument | Verified (PDF-Volltext) | Sprout Social Q1 2026 Pulse Survey Analysis — https://media.sproutsocial.com/uploads/2026/03/Sprout-Social-Q1-2026-Pulse-Survey-Analysis.pdf |
| „AI-labeled TikTok content averages 1.9% engagement compared to 3.4%" (angeblich Sprout Q1 2026) | **Nicht öffentlich verifizierbar** (nicht in der Sprout-Quelle; nur Blog greenfroglabs) | https://greenfroglabs.com/blog/tiktok-trends |
| „AI UGC achieving up to 350% higher engagement" | **Nicht öffentlich verifizierbar** (videotok.app ohne Quelle; in keiner Primärquelle) | https://www.videotok.app/blog/avatar-and-ugc-ads/ugc-ads-rates-traditional-ugc-vs-ai-ugc |
| Vendor Creatify „2.7x more leads vs. static image ads", Arcads „1 billion views" — Video vs. Standbild, nicht AI vs. Mensch | Claimed (Vendor) | https://creatify.ai/ ; https://www.arcads.ai/ |
| TikTok-Policy: „Content that is auto-disclosed will not face additional penalties or distribution restrictions solely due to the label." | **Verified (Zitat)** | TikTok Shop Academy EU/IE „AIGC" — https://seller-ie.tiktok.com/university/essay?knowledge_id=6752261875877653&lang=en-GB |
| TikTok Newsroom 2025-11-19: >1,3 Mrd. Videos gelabelt; Test eines **AIGC-Reglers in „Manage Topics"** („help people tailor the diverse range of content in their feed, rather than removing or replacing content"); unsichtbares Watermarking; 2 Mio. $ AI-Literacy-Fonds | Verified (Zitat) | https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en |
| 2026-07-10: „more than 3 billion videos" gelabelt; erweiterte Detektion von AI-Spam in Politik/Finanzen/Medizin; „the label itself is not a demotion signal" (Interpretation Kompozy) | Claimed (Sekundär: TechTimes 2026-07-13, Kompozy; Newsroom-URL leitete auf anderen Artikel um) | https://www.techtimes.com/articles/320282/20260713/tiktok-has-labeled-3-billion-ai-videos-here-what-research-says-they-miss.htm ; https://kompozy.io/guides/tiktok-ai-labeling-at-scale |
| Praktiker: „Not one person has ever said anything about it being ai." | Claimed | /r/passive_income/comments/1w7nihc/ , 2026-09-05 |
| AI-Netzwerk-Accounts mit 100k–1,3 Mio. Views später gelöscht (@poormaninla, @melisogn9dl: statusCode 10221) — Reichweitenrisiko = Enforcement, nicht Label | Claimed (Views) / Verified (Handle-Status) | 404 Media; tt_profile.sh 2026-09-24 |
| Unabhängiger A/B-Test „gleiches Shop-Video mit vs. ohne Label" oder Agentur-Daten AI-Avatar vs. Mensch auf **TikTok Shop** | **Nicht öffentlich verifizierbar** | — |

Bewertung (Estimated): **Algorithmischer Label-Malus: keiner belegt** (TikTok-Policy). **Publikums-Malus: belegt und klein** — JCR-Feldanalyse –7…–8 % Likes / –7 % Engagement bei Disclosure; Experimente zeigen die Richtung konsistent (Seeger 2026; Altay 2024; Wang 2026). Da TikToks Recommender Engagement-Signale (Completion, Likes, Shares) zur Pool-Eskalation nutzt, wirkt ein –7 %-Engagement-Malus indirekt auf die Reichweite, vermutlich überproportional an den Pool-Schwellen. **Größerer Hebel als das Label ist der „AI-Look"**: Taboola-Studie — als künstlich erkannte AI-Creatives performen am schlechtesten, nicht erkennbare am besten; also realistische Avatare/Stimmen, klare Gesichter, sichtbarer Aufwand (Skript, Schnitt, Demonstration). Zwei nutzerseitige Dämpfer sind neu: der „weniger AI-Content"-Regler (TikTok, Test seit 11/2025) und die Spam-Detektion für AI-Massenaccounts. Für die 100-Video-Verteilung: kein Label-Abschlag auf die Klassenhäufigkeit, aber –10 % auf die Ø-Views je Klasse gegenüber einem menschlichen Account (JCR-Malus + Pool-Hebel, konservativ gerundet); Account-Risiko (Bans, Pilot-Limits) separat.

### 2.9 Content-Halbwertszeit und Shop-Tab-/Such-Traffic

| Befund | Tag | Quelle |
|---|---|---|
| **Halbwertszeit des Engagements TikTok: „0 minutes … with exceptions"** („Videos featuring uniquely compelling content or celebrity involvement can go viral"); Instagram 1.096 min = 18,27 h; YouTube 15.276 min = 10,6 Tage; Basis >5,6 Mio. Posts, 1.1.–31.12.2025; Definition: „time it takes for a post to receive half of its total engagement" | Verified (Seite; Methodik nur grob beschrieben) | Graffius, „Lifespan (Half-Life) of Social Media Posts: Update for 2026" — https://www.scottgraffius.com/blog/files/lifespan-halflife-of-social-media-posts-update-2026.html |
| Anteil der Views aus der For-You-Page: 7 von 10 (alle TikTok-Inhalte) | Verified (Report-Zahl) | Metricool 2026-05-12 |
| **GMV-Anteil US-TikTok-Shop nach Kanal 2025: Video 50 %, Shop-Tab 36 %, LIVE 14 % (LIVE 2024: 10 %)**; H1 2025 identischer Split | Verified (Report-Zahl über zwei Sekundärberichte) | Momentum Works × Tabcut, via TechNode 2025-08-04 und Contentgrip Feb 2026 (s. 2.6). Shop-Tab umfasst Suche, Kategorie-Feeds und Produktempfehlungen („Product Card"-Umsatz, s. 2.2). |
| Kalodata: Content (Video + LIVE) ≈ 76 % des **globalen** GMV | Claimed (Blog 403; Suchtreffer) | s. 2.6 |
| „Search now drives between 48% and 65% of TikTok Shop sales" / „page one of the Shop tab capture 38–52% of all clicks" — „documented in seller data from early 2026", **keine** Quelle/Link | Claimed (unbelegt; widerspricht Tabcut-Split, bei dem Shop-Tab inkl. Suche insgesamt 36 % ausmacht) | Zonflip, 2026-03-27 — https://zonflip.com/tiktok-shop-selling-the-data-driven-playbook-every-serious-seller-needs-in-2026/ |
| Sales-Anteil **Suche allein** vs. Shop-Tab-Empfehlung vs. FYP-Video für **Affiliate-Videos** | **Nicht öffentlich verifizierbar** (Academy-Seiten listen Quellen ohne Prozentwerte) | TikTok Shop Academy (s. 2.2) |
| Südostasien: LIVE dominant (VN/MY/PH/SG), Video „also contributing" (qualitativ) | Verified (Report-Text) | EchoTik Q1 2025 |
| Halbwertszeit Shop-Videos: „7 to 10 days for them to start picking up"; „View suppression was lifted in 14 days"; Winner „kept printing cash" wochenlang | Claimed | /r/TikTokShopAffiliate/comments/1dleq94/ ; /1brsw1u/ ; YouTube-Transkripte |
| Quantitative Halbwertszeit von **Shop**-Videos (Stunden bis 50 % der Lebenszeit-Views/Sales) | **Nicht öffentlich verifizierbar** | — |

Einordnung (Estimated): Graffius' „0 Minuten" und Metricools „7 von 10 Views aus FYP" beschreiben dieselbe Mechanik: Ein Video bekommt seinen Traffic in den ersten Stunden über die Pool-Eskalation (Abschnitt 2.2) oder gar nicht. Für Shop-Videos gibt es einen zweiten, langsameren Kanal: Ein Video mit Produkt-Anchor kann über Shop-Tab-Empfehlungen und Suche (zusammen 36 % des US-GMV) und über Brand-Ads (GMV Max) noch Tage bis Wochen später Sales erzeugen — das erklärt die Praktiker-Berichte „zieht nach 7–10 Tagen an". Für Planung: ~70 % der Views eines Videos innerhalb 48 h; ~30 % der Sales eines Winners nach Tag 7 (reine Annahme aus Kanal-Split + Berichten, keine Quelle).

---

## 3) Annahmen-Set: 100-Video-Verteilung für einen kompetenten neuen AI-Content-Affiliate-Account (Estimated)

Definition „kompetent": Produktwahl datengestützt (Kalodata o. ä.), Hooks/Skripte aus bewährten Winnern nachgebaut (Ashley Howard: 80/20-Nachbau), realistischer AI-Look mit klarem Gesicht/Stimme (Taboola-Befund), 3–5 Posts/Tag, US/UK-Markt, keine Violations, Pilot-Programm eingerechnet. Klassen: A = <1k Views, B = 1k–10k, C = 10k–100k, D = ≥100k.

| Szenario | A (<1k) | B (1k–10k) | C (10k–100k) | D (≥100k) | Ø-Views je Klasse (Annahme) | Gesamt-Views (Formel) | Median | Top-5-Video-Anteil |
|---|---|---|---|---|---|---|---|---|
| **Konservativ** | 90 | 8 | 2 | 0 | 250 / 3.000 / 20.000 / – | 90×250 + 8×3.000 + 2×20.000 = **86.500** | ~250 | (2×20k + 3×3k) / 86,5k ≈ **57 %** |
| **Realistisch** | 80 | 15 | 4 | 1 | 300 / 3.500 / 30.000 / 200.000 | 80×300 + 15×3.500 + 4×30.000 + 1×200.000 = **396.500** | ~300–400 | (200k + 4×30k) / 396,5k ≈ **81 %** |
| **Aggressiv** | 65 | 22 | 10 | 3 | 400 / 4.000 / 35.000 / 400.000 | 65×400 + 22×4.000 + 10×35.000 + 3×400.000 = **1.664.000** | ~600–800 | (3×400k + 2×35k) / 1,664M ≈ **76 %** |

Kalibrierung gegen die harten Anker:

- **Buffer (Verified, alle Account-Größen):** Median ~490, p90 = 14.401 bei 11+ Posts/Woche → 10 % der Videos ≥ ~14k. Unser „aggressiv" hat 13 % ≥ 10k, „realistisch" 5 %, „konservativ" 2 %. Ein neuer Account ohne Follower-Basis liegt unter dem Gesamt-p90, daher ist „realistisch" (5 % ≥ 10k) der Erwartungswert und „aggressiv" ≈ das Niveau etablierter Vielposter.
- **Bandy & Diakopoulos 2020 (Verified):** 86 % ≤ 1k, 37 % ≤ 100 → „konservativ" (90 % < 1k) entspricht der 2020-Verteilung gewöhnlicher Nutzer; „realistisch" (80 % < 1k) setzt voraus, dass Produkt-/Hook-Kompetenz ~6 Prozentpunkte aus Klasse A herausholt.
- **Munger 2022 (Verified):** Peak-Median-Ratio 64 → bei Median 300 ist ein Top-Video von ~20k Views der **Normalfall** für einen Account, nicht die Ausnahme; das rechtfertigt ≥ 2 Videos in Klasse C selbst im konservativen Fall. Top-20 % = 76 % der Views → unsere Top-5 %-Anteile (57–81 %) sind konsistent.
- **Socialinsider (Verified):** Ø 350 Views/Post bei 1–5k Followern → 35k Views/100 Videos; „konservativ" (86,5k) liegt darüber, weil „kompetent" definiert ist und Socialinsider auch inaktive/schlechte Accounts mittelt.
- **Praktiker (Claimed):** konservativ = Sancar/Ecom King/Nadorb-Grind; realistisch = rMA5MKeyym8 (1/17 bei 900k), Reddit 1u9s0zn (≈1 % Virals), Veo-3-Account (Masse 100–300, 1–2 Videos 200k–1M); aggressiv = Patryk nach Formatwechsel, tommycetty (226k/168k/67k), Rosabella-Netzwerk.
- **AI-Malus (Verified, JCR):** –7…–8 % Likes bei Disclosure → in den Ø-Views je Klasse bereits mit –10 % gegenüber einem menschlichen Vergleichsaccount berücksichtigt (Annahme: Engagement-Malus schlägt an Pool-Schwellen etwas stärker durch).

Korrekturen und Risiken (Estimated):
- **Shoppable-Anteil:** Im Pilot-Programm (1.000–5.000 Follower, US-Regel 5 Shoppable Videos/Woche) sind von 100 Videos in 30 Tagen nur ~20 shoppable → Sales-Modelle nur auf diesen Teil anwenden, bis 5.000 Follower erreicht sind. Unter 1.000 Followern ist Affiliate-Zugang regulär gar nicht möglich (Creator Eligibility Policy).
- **Account-Risiko** dominiert: Bans (tommycetty; @poormaninla), 24h-Throttles, AI-Spam-Detektion (TikTok 07/2026). Vorschlag Überlebenswahrscheinlichkeit 90 Tage: 0,6 / 0,75 / 0,85 (reine Annahme).
- **Nutzerseitiger AI-Regler** („weniger AI-Content", Test seit 11/2025): Effektgröße unbekannt; im realistischen Szenario nicht zusätzlich abgezogen.
- **Markt DE/EU:** Alle Praktiker-Daten stammen aus US/UK; Tabcut-Kanal-Split ist US. Für DE Konservativ-Szenario als Basis.
- **View → GMV:** Praktiker-Konversion 1 Sale je 200–5.000 Views je nach Produkt; Brand-Erwartung 1/5.000; MomentIQ „Good" für Nano-Creator: Product-CTR 1–2 %, CR 2–4 % (Claimed). Klassen-Views mit produktabhängiger Rate multiplizieren, nicht mit Pauschalwert. GMV konzentriert sich stärker als Views (GMV-Max-Verstärkung, Shop-Tab-Nachlauf): Top-5-Videos ≥ 85–90 % des GMV.

---

## 4) Nicht verfügbar / offen

- **View-Klassen-Verteilung speziell für neue Accounts oder TikTok-Shop-Affiliate-Videos** (öffentlicher Datensatz 2024–2026): Nicht öffentlich verifizierbar. Nächste Näherungen: Buffer-Median/p90 (alle Accounts, 2025) und Bandy 2020 (gewöhnliche Nutzer).
- **Kalodata/Tabcut/EchoTik/FastMoss-Reports mit Video-Performance-Verteilung:** nicht existent/öffentlich; Kalodata-Blog und Momentum-Works-Primärseiten 403; Tabcut-Daten nur über Momentum-Works-Sekundärberichte (Kanal-Split, Creator-Zahlen).
- **GMV-Anteil der Top-1–5 %-Videos:** nur Creator-Level-Konzentration (Dashboardly 0,5 % → 38 %, Claimed; Inc.-Fall 16 % → 100 %, Claimed) und Views-Level (Bandy/Munger, Verified). Video-Level-GMV: Nicht öffentlich verifizierbar.
- **Sales-Anteil Suche allein vs. Shop-Tab-Empfehlung vs. FYP-Video** für Affiliate-Content: Nicht öffentlich verifizierbar; nur Gesamt-Split Video 50 / Shop-Tab 36 / LIVE 14 (US 2025).
- **Quantitative Halbwertszeit von Shop-Videos:** Nicht öffentlich verifizierbar (Graffius nur plattformweit „0 Minuten mit Ausnahmen").
- **Unabhängiger A/B-Test AI-Label vs. ohne Label auf TikTok Shop / Agentur-Daten AI-Avatar vs. Mensch:** keine öffentliche Studie; beste Ersatzquellen JCR-Feldanalyse (Disclosure, alle TikTok-Inhalte) und Taboola (Native Ads).
- **Volltext-Effektgrößen** von Carney et al. 2026 (JCR, Paywall) und Seeger et al. 2026 (PDF geladen, Mittelwerte/η² nicht extrahiert) — nur Abstract-Zahlen bzw. Richtung.
- **„350 % Engagement"-Claim** und **„1,9 % vs. 3,4 % (Sprout)"-Claim:** Ursprung nicht auffindbar bzw. nicht in der genannten Primärquelle → als unbelegt behandeln.
- **TikTok-Support-FAQ „How TikTok recommends content"**: kein Body per Fetch; Momentum-Works-2024-Report (Kanal-Split 2024 außer LIVE 10 %) nicht zugänglich.
- **Creator-Pilot-Programm-Limit**: US-Academy sagt 5 Shoppable Videos/Woche (06/2025), andere Quellen 3/Tag — regional/zeitlich uneinheitlich; aktuelle Regel im Seller-Center prüfen.
- Alle YouTube-Publikationsdaten aus „x months ago" geschätzt; Reddit-Kommentare teils nur über Suche sichtbar (Arctic-Shift-Timeouts).
- WebSearch-Budget der Session nach ~40 Abfragen erschöpft; verbleibende Prüfungen nur per WebFetch.

---

## 5) Quellen mit Zugriffsdatum (2026-09-24/25)

Primär / Plattform:
- TikTok Shop Academy US, „How TikTok Recommends Content to New Users" (2025-11-26): https://seller-us.tiktok.com/university/essay?knowledge_id=2410858052077355
- TikTok Shop Academy US, „6 Traffic Sources on TikTok Shop" (2025-11-05): https://seller-us.tiktok.com/university/course?learning_id=2852280135698218&content_id=2097818908297003&lang=en
- TikTok Shop Academy US, „Creator Pilot Program Feature Guide" (2025-06-23): https://seller-us.tiktok.com/university/essay?knowledge_id=7264111224227597&lang=en
- TikTok Shop Academy US, „Shop Tab & Search Analytics" (2026-05-22): https://seller-us.tiktok.com/university/essay?knowledge_id=6276577063585582&lang=en
- TikTok Shop Academy US, „The Seller Guide to Shop Tab Success" (2026-05-14): https://seller-us.tiktok.com/university/essay?knowledge_id=8750609034250026&lang=en
- TikTok Shop Academy US, „Content Policy": https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617&lang=en
- TikTok Shop Academy EU/IE, „AIGC": https://seller-ie.tiktok.com/university/essay?knowledge_id=6752261875877653&lang=en-GB
- TikTok Newsroom, „How TikTok recommends videos #ForYou" (2020-06-18): https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
- TikTok Newsroom, „More ways to spot, shape and understand AI-generated content" (2025-11-19): https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en
- TikTok Newsroom, AI-Labels (2023-09-19; 2024-05-09): https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content ; https://newsroom.tiktok.com/en-us/partnering-with-our-industry-to-advance-ai-transparency-and-literacy

Benchmark-Reports:
- Buffer, „How Often Should You Post on TikTok" (2025-10-08): https://buffer.com/resources/how-often-should-you-post-on-tiktok/
- Buffer, „TikTok Algorithm Guide": https://buffer.com/resources/tiktok-algorithm/
- Buffer, AI-assisted vs. human posts (2024-10-15): https://buffer.com/resources/ai-assistant-post-performance/
- Socialinsider, „TikTok Benchmarks 2026" (2026-04-22): https://www.socialinsider.io/blog/tiktok-benchmarks/
- Metricool, „TikTok Study 2026" (2026-05-12): https://metricool.com/tiktok-study/
- Rival IQ, Social Media Industry Benchmark Report 2025/2026: https://www.rivaliq.com/blog/social-media-industry-benchmark-report/
- Graffius, „Lifespan (Half-Life) of Social Media Posts – Update 2026": https://www.scottgraffius.com/blog/files/lifespan-halflife-of-social-media-posts-update-2026.html
- Sprout Social Q1 2026 Pulse Survey (PDF): https://media.sproutsocial.com/uploads/2026/03/Sprout-Social-Q1-2026-Pulse-Survey-Analysis.pdf
- Momentum Works × Tabcut (Sekundär): https://technode.global/2025/08/04/tiktok-shop-doubles-global-gmv-in-h1-with-u-s-market-hitting-5-8b-momentum-works-tabcut-report/ ; https://www.contentgrip.com/tiktok-shop-data-analysis/ ; Primär (403): https://thelowdown.momentum.asia/new-report-tiktok-shop-u-s-gmv-grew-68-to-reach-us15-1b-in-2025/ ; https://momentum.asia/insights/detail/tiktok-shop-in-the-us-2025
- EchoTik, TikTok Shop 2025 Q1 Report (lokal echotik_q1_2025.pdf): https://echotik.ai

Akademisch:
- Bandy & Diakopoulos, #TulsaFlop, FAccTRec 2020: https://arxiv.org/abs/2012.07716
- Guinaudeau, Munger & Votta, Fifteen Seconds of Fame, CCR 2022: https://kmunger.github.io/pdfs/tiktok.pdf
- Broadcasting trap, HSSC 2025: https://www.nature.com/articles/s41599-025-04797-w
- Chen et al., Douyin, arXiv:1903.12399: https://arxiv.org/abs/1903.12399
- Ling et al., arXiv:2111.02452: https://arxiv.org/abs/2111.02452
- arXiv:2503.20231 (Amplification): https://arxiv.org/abs/2503.20231
- Carney, Riveros & Tully, JCR 2026: https://academic.oup.com/jcr/advance-article/doi/10.1093/jcr/ucag013/8672493
- Seeger, Wessel & Lehrer, Electronic Markets 2026: https://link.springer.com/article/10.1007/s12525-026-00883-2 ; PDF: https://www.db-thueringen.de/servlets/MCRFileNodeServlet/dbt_derivate_00071052/12525_2026_Article_883.pdf
- Altay & Gilardi, PNAS Nexus 2024: https://academic.oup.com/pnasnexus/article/3/10/pgae403/7810648
- Wang, Sturgis & de Kadt, arXiv:2506.16202: https://arxiv.org/abs/2506.16202
- Wittenberg et al., PNAS Nexus 2025 (PDF): https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/9/583/files/2026/01/labelingaigenerated_2025.pdf
- Taboola × Columbia/Harvard/TUM/CMU (2026-01-28): https://www.taboola.com/press-releases/genai-ads-study-2026/

Sekundär / Blogs / Claims:
- Science Says (2026-06-30): https://app.sciencesays.com/p/made-with-ai-gets-lower-engagement
- Hamster Garage: https://www.hamstergarage.com/article/tiktok-shop-affiliate-statistics-benchmarks-roi
- Dashboardly: https://www.dashboardly.io/statistics/tiktok-shop-affiliate-creator-statistics
- Branvas: https://www.branvas.com/blogs/news/tiktok-shop-statistics
- Inc.com (403): https://www.inc.com/temilola-agbede/tiktok-shop-is-booming-most-brands-still-arent-making-money/91378937
- Kalodata (403): https://www.kalodata.com/blog/tiktok/the-2026-tiktok-sales-report-best-selling-products-data-driven-insights/ ; https://www.kalodata.com/blog/tiktok/best-tiktok-shop-analytics-tool-2026/ ; X: https://x.com/kalodata/status/2092265687536345597
- Zonflip (2026-03-27): https://zonflip.com/tiktok-shop-selling-the-data-driven-playbook-every-serious-seller-needs-in-2026/
- AdManage.ai: https://admanage.ai/blog/average-tiktok-views ; Heistbrain: https://heistbrain.com/benchmarks/tiktok-views.html ; MomentIQ: https://bemomentiq.com/blog/tiktok-shop-content-performance-benchmarks-what-good-great-elite
- Kompozy: https://kompozy.io/guides/tiktok-ai-labeling-at-scale ; TechTimes (2026-07-13): https://www.techtimes.com/articles/320282/20260713/tiktok-has-labeled-3-billion-ai-videos-here-what-research-says-they-miss.htm
- videotok.app („350 %"): https://www.videotok.app/blog/avatar-and-ugc-ads/ugc-ads-rates-traditional-ugc-vs-ai-ugc ; greenfroglabs („1,9 % vs. 3,4 %"): https://greenfroglabs.com/blog/tiktok-trends
- Creatify: https://creatify.ai/ ; Arcads: https://www.arcads.ai/
- YouTube (NexLev-Transkripte): b13n1YbKl9Q (Ashley Howard), Tsv7Zt9w9-4, NKxTt215kus, 3Axh5s_iUyA, SAuvpusxX4g, W5ThaDXg2ss, DHZ8iI0Sbj0, rMA5MKeyym8, kjCyL4Vn4P4, Bg5fs8ctzqM, CgPX3Po7WFo, 0eQDpN4lmNE, AoCT5YZycp0, VgUZJo0qDRc, I_1fpXpUdbE
- Reddit: r/passive_income 1u9s0zn (2026-06-19), 1rdiwob, 1w7nihc; r/TikTokShopAffiliate 1dsuss1, 1draeqq, 1wba5a1, 1d1xgd3, 1dleq94, 1brsw1u; r/TikTokshop 1uf1zxj, 1w2nfnu, 1w2ubvm; r/Entrepreneurs 1snwa7t
- 404 Media (lokaler Dump 404media.html); tt_profile.sh-Checks @poormaninla, @melisogn9dl (2026-09-24)

## Verifikation (adversarial)

Zweitprüfung 2026-09-25 (unabhängiger Re-Fetch aller Quellen; beide Paper-PDFs erneut per PyMuPDF im Volltext geprüft: `research/arxiv_2012.07716.txt`, `research/munger_tiktok.txt`).

| Metrik | Verdict | Note |
|---|---|---|
| Median Views pro TikTok-Post nach Posting-Frequenz 1 / 2–5 / 6–10 / 11+ pro Woche = 489 / 506 / 487 / 459 | CONFIRMED | Buffer-Tabelle exakt so (489 / 506 / 487 / 459), publ. 2025-10-08, 11,4 Mio. Posts / >150.000 Accounts. Definition: Median Views pro Post, Accounts aller Größen gepoolt; Buffer sagt nur, dass die *relativen* Gewinne (Fixed-Effects-Regression) „across all account sizes" gelten — die absoluten Mediane sind nicht nach Account-Größe aufgeschlüsselt. Views organisch/gesamt, keine Ads-Trennung angegeben. |
| 90. Perzentil Views pro Post (gleiche Klassen) = 3.722 / 6.983 / 10.092 / 14.401; 11,4 Mio. Posts / >150k Accounts | CONFIRMED | Buffer-P90-Tabelle exakt so (3,722 / 6,983 / 10,092 / 14,401); Stichprobe 11.4M posts, 150,000+ accounts, Datum 2025-10-08 bestätigt. Gleiche Einschränkung: gepoolt über alle Account-Größen, Zeitfenster der Posts nicht auf der Seite spezifiziert. |
| Ø Views pro Post, Accounts 1–5k Follower: 350 (2025; 2024: 860) | CONFIRMED | Socialinsider „TikTok Benchmarks" (Stand 2026-04-22): Tier 1k–5k Follower 2025 = 350, 2024 = 860, −59 %. Basis: 2 Mio. TikTok-Videos von 214.507 Profilen, Jan 2024–Dez 2025. Es ist ein arithmetischer Mittelwert („average"), kein Median; „Views" nicht weiter definiert (Plattform-Metrik). |
| Anteil Videos ≤1.000 Plays / ≤100 Plays = 86 % / 37 % (80.682 Videos, 616 Nutzer, 2020) | CONFIRMED | Bandy & Diakopoulos, arXiv:2012.07716 (eingereicht 2020-12-14), Abschnitt 4.1 wörtlich: „86% of videos had a play count of 1,000 or less, and 37% had a play count of 100 or less". 80.682 Videos = bis zu 500 jüngste Videos je Nutzer von 616 Nutzern (Videos bis 2020-06-20). Metrik ist TikTok „play count" (Loops, nicht Unique Viewer). Caveat: Nutzer über politische #TulsaFlop-Call-to-Action-Videos gesampelt, nicht zufällig. Die Zahlen stehen nur im PDF, nicht im Abstract. |
| Anteil aller Plays auf Top-1 % / Top-10 % der Videos = 76 % / 93 % (gleicher Datensatz) | CONFIRMED | Ebd. wörtlich: „the top 1% of videos in the dataset claimed 76% of all plays, and the top 10% of videos claimed 93%" (dataset-weit über alle 616 Nutzer, nicht pro Account). Die 76 % werden in der Conclusion wiederholt. |
| Pro Account: Gini der Views (Median) 0,70 / Peak-Median-Ratio (Median) 64x / Top-20 % Videos = 75,76 % der Views | CONFIRMED | Guinaudeau, Munger & Votta, „Fifteen Seconds of Fame", Computational Communication Research 4(2), 2022, S. 479–480: Gini-Median 0,70 TikTok (YouTube 0,62); Peak-Median-Ratio Median 64 (YouTube 40); „on TikTok the top 20% of the videos rake in 75.76% of views" (YouTube 72,52 %, Mittelwert über Accounts). Basis: 11.546 politische TikTok-Accounts / 1.998.642 Videos (Hashtag- + Snowball-Sampling, politische Nische). Gini und Ratio sind Mediane über Accounts; der 75,76 %-Wert ist ein Mittelwert (mean) über Accounts. |
| TikTok Shop Academy: Größe des „Basic Traffic Pool" für neue Videos = around 500 users | CONFIRMED | Seller-US Academy „How TikTok Recommends Content to New Users", Stand 11/26/2025, wörtlich: „it enters the Basic Traffic Pool, shown to a small, diverse group (around 500 users) to gauge initial engagement through watch time, likes, and comments". Seller-Education-Text, keine Engineering-Spezifikation; keine Angabe, ob die 500 Nutzer als Impressions oder Unique User zählen. |
| Creator Pilot Program (1.000–5.000 Follower, 30 Tage): max. Shoppable Videos / Shoppable LIVEs pro Woche = 5 / 3 | CONFIRMED | Seller-US Academy „TikTok Shop Creator Pilot Program Feature Guide", Stand 06/23/2025, wörtlich: „You can post a maximum of 5 Shoppable Videos and 3 Shoppable LIVEs each week"; Zielgruppe „1,000 to 5,000 followers"; automatische Einschreibung für 30 Tage nach Affiliate-Freischaltung; nur Produkte mit Shop-Performance-Rating ≥ 95 %; Aufhebung ab > 5.000 Follower oder nach Milestone-Tasks. US-Regel; andere Regionen können abweichen (s. Abschnitt 4). |

Fazit der Zweitprüfung: 8/8 CONFIRMED. Keine Zahl widersprochen. Wichtigste Definitions-Hinweise: Buffer-Mediane sind über alle Account-Größen gepoolt; Socialinsider-350 ist ein Mittelwert; Bandy-Anteile sind dataset-weit (nicht pro Account) und stammen aus einer nicht-zufälligen 2020-Stichprobe; Guinaudeau/Munger/Votta beziehen sich auf politische Accounts; die 500-User-Angabe ist Seller-Education-Prosa.
