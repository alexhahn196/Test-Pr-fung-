# Red-Team: Aggregierte Daten zu KI-Content auf TikTok Shop US, Top-down-Schätzung und KI-gelabelte Ausreißer

Bearbeitet am 2026-09-25 (alle Abrufe an diesem Tag, sofern nicht anders vermerkt). Winkel: `_prompt_ai_aggregate_outliers.txt`. Rolle: Red Team, also nach den stärksten Gegenbelegen zu C1–C4 suchen (C5–C7 nur am Rand).
Tags: **Verified** = selbst in TikTok-Rohdaten (tt_profile.sh / tt_video.sh / tt_media.py) oder im Primärdokument gesehen; **Claimed** = jemand behauptet es (auch Analytics-Anbieter, die Schätzwerte ausweisen); **Estimated** = eigene Rechnung, Formel steht dabei.
Rohdaten und Hilfsdateien: `research/redteam/aggr/` (Artikel-HTML, Transkripte, `topdown.py` + `topdown_out.txt`, Profil- und Video-Stats), Kontaktbögen unter `media/<video-id>/sheet.jpg`.

---

## 0. Kurzfazit

1. **Die Biverse-Zahlen lassen sich nicht über den Chosun-Bericht hinaus zurückverfolgen.** Das koreanische Original (Chosun Ilbo, 07.09.2026) enthält keine weiteren Zahlen. Eine Originalstudie, eine Pressemitteilung oder ein Blog von Biverse ist nicht auffindbar (Google News KO/EN, Domain-Proben). Neu ist ein Hinweis zur Herkunft der Daten: Biverse ist seit August 2026 **offizieller TikTok Shop Partner** und wirbt mit einer eigenen Datenbank von **„5 Mio. globalen Influencer-Datensätzen“** (Startup Recipe, 11.08.2026). Die „TikTok-API-Daten“ sind also sehr wahrscheinlich Biverses eigene Crawl-/Schätzdaten. Umsätze pro Video für 347.588 fremde Videos gibt keine öffentliche TikTok-API her. Die Zahlen bleiben **Claimed** mit unveröffentlichter Methodik.
2. **Red-Team-Lesart von Biverse:** Der alte Bericht hat die Zahlen nur relativ gelesen („0,15 % > 10k“). In absoluten Zahlen bedeuten sie etwas anderes: **In einem einzigen Monat haben 514 KI-Videos in den USA jeweils mehr als 10.000 USD GMV erzeugt und 76.314 KI-Videos jeweils 100–10.000 USD.** Meine Top-down-Rechnung ergibt daraus **49–143 Mio. USD GMV pro Monat aus KI-gelabelten Videos** (Mitte ≈ 87 Mio.). Das sind ≈ 2,6–6,2 % des US-Shop-GMV. Der Provisionspool liegt bei **1,8–18 Mio. USD pro Monat** (Mitte ≈ 5,6 Mio.). Daraus folgen, je nach Konzentration, **grob 50–1.400 Betreiber mit ≥ 3.000 USD Provision im Monat** (Mitte ≈ 250–340), **≈ 25–80 mit ≥ 10.000 USD** (Mitte) und **≈ 5–35 mit ≥ 20.000 USD** (Mitte). Alles **Estimated**. Relativ zur Gesamtzahl der KI-Betreiber ist das „selten“ (≈ 1–4 %). Absolut sind es aber Hunderte, und die TikTok-Labels untererfassen hybride KI (TTS, KI-Skript) deutlich.
3. **Konkreter, frisch verifizierter Gegenbeleg: @spongebobprodsz („Finds4dayz“).**
   - **Was verifiziert ist:** Alle 10 neuesten Videos tragen TikToks **KI-Label** (aigcLabelType = 1). Alle 10 sind **shoppable** (isECVideo = 1, Produkt-Anker). 5 von 10 laufen als **Ads** (isAd = true, also Brand-Budget über GMV Max/Spark). Am 25.09.2026 gingen bis ca. 13 Uhr UTC 6 neue Videos online. Format **G**: KI-generierte Szenen (Küche, Weihnachtsdeko, Garten) um ein reales Produkt (medicube-Creme), Sticker „FLASH DEAL / LIMITED“ und ein Skript-Voiceover (Kontaktbogen gesichtet).
   - **Was nur Claimed ist:** Die Kalodata-Karte im Video eines Kursverkäufers zeigt **„Revenue $302.09k“ in 30 Tagen** (Juli 2026) und „$1.3M in <5 months“.
   - **Einordnung:** Bei 5–20 % Provision entspricht das ≈ **15–60 k USD Provision im Monat** (Estimated). Das Konto ist seit ≥ 7 Monaten aktiv (Start laut Kursverkäufer Februar 2026). Der alte Bericht führte es nur als Claimed-Zeile mit Kategorie „F/E“. Das KI-Label, die Shoppability und die laufenden Ads hat er nicht video-genau verifiziert, und in seine Schlussfolgerungen ist der Fall nicht eingegangen.
4. **Weitere Aggregat-/Anbieterdaten:** Colaba („AI vs Personal Content“, März 2026, n ≈ 30+) stuft das faceless Konto **@beautypickshub** als „AI content“ ein, mit „$97.85 revenue per follower“ bei ≈ 4.000 Followern (≈ 390k USD Umsatz in 4 Wochen, Estimated aus Claimed-Werten; Methodik fragwürdig: „163.24 % conversion“). Verifiziert habe ich: echte Hände + Produkt + Skript-Voiceover, ohne sichtbare Person, Format D/H. 9 von 10 neuesten Posts laufen als Ads (isAd = true), 3 KI-Labels auf den neuesten Posts. Daneben gibt es ein strukturelles Muster, das mehrere Quellen berichten (Business Insider, The Keyword, Kursverkäufer, RTIH): **GMV Max leitet Brand-Werbebudget auf Affiliate-Videos, die gut klicken**. Damit hängt der Umsatz eines KI-Kontos nicht mehr an organischer Reichweite. Das greift direkt die Modelllogik von C5 an (organische 4.000 Views × 30 USD GMV/1.000 Views).
5. **Keine KI-spezifische Statistik** gefunden bei Kalodata, FastMoss, EchoTik, Tabcut, Shoplus, Charm.io, Momentum Works (Cloudflare-Block), eMarketer, Marketplace Pulse, Digiday oder Modern Retail. Biverse bleibt die einzige Zählung KI-gelabelter shoppable Videos mit Umsatzklassen.

---

## 1. Biverse / Chosun Ilbo – erneut gelesen und zurückverfolgt

### 1.1 Primärtext (Verified als Artikelinhalt, Zahlen Claimed)
- Koreanisches Original: https://www.chosun.com/economy/tech_it/2026/09/07/ARR3UW4S5NGCNBDKWOK7QDMPJI/ („美 15초짜리 ‘AI 셀럽’ 영상이 1억 매출 올렸다“, 구동완 기자). Aus der lokal gespeicherten Kopie `cho_ko.html` erneut vollständig extrahiert.
- Wörtlich (KO): „7일 AX(인공지능 전환) 전문 업체 바이버스가 틱톡 API(응용 프로그램 인터페이스) 데이터를 수집해 분석한 자료에 따르면, 지난 8월 한 달간 미국 틱톡 계정에 올라온 AI 영상 34만7588건이 최소 1달러 이상의 매출을 낸 것으로 나타났다. 이 가운데 7만6314건이 100~1만달러의 매출을, 514건은 1만달러 넘는 수익을 거뒀다. 영상 대부분(92.5%)은 30초 이하의 쇼츠 영상이었다.“
- „미국 틱톡에서 팔로워 5만~50만명을 보유한 AI 인플루언서 계정은 2만6839개 … 50만~100만명인 계정은 1464개, 100만명이 넘는 계정도 808개“.
- **Mehr Zahlen enthält der Artikel nicht.** Es gibt keine Verteilung nach Account, keinen GMV-Anteil der Top-Accounts, keine Kategorien, keine Definition von „AI 영상“. Der Rest des Artikels behandelt die Which?-Umfrage (70 % erkennen KI-Videos nicht), den Guardian („40–60 % der Inhalte großer Marken KI-produziert, oft unter NDA“), den EU AI Act und die FTC.
- **Metrik:** „매출“ = Verkaufsumsatz = GMV (nicht Provision, nicht Gewinn). Beim 514er-Satz steht „수익“ (Ertrag), gemeint ist dieselbe Umsatzklasse.

### 1.2 Suche nach dem Biverse-Original (ohne Ergebnis)
- Google News KO (`gnews_ko.py`, hl=ko): „바이버스 틱톡“, „바이버스 AI 영상 매출“, „바이버스 신재인“, „34만7588“, „AI 인플루언서 계정 2만6839“, „AI 인플루언서 틱톡 매출 8만9000달러“. Die Zahlen tauchen nur bei Chosun auf (und laut Vorbericht in der Zweitverwertung von thepublic.kr). Einen eigenen Biverse-Report oder eine Pressemitteilung gibt es nicht.
- Google News EN „Biverse TikTok“: 0 Treffer.
- Domain-Proben biverse.ai, biverse.co.kr, biverse.io, biverse.kr: nicht erreichbar oder fremde Seite (biverse.ai leitet auf lumitarot.me um).
- **Neu gefundener Kontext zum Datenlieferanten (Verified als Artikelinhalt):**
  - Startup Recipe, „[AI서머리] 바이버스, 틱톡샵 파트너 선정“, 11.08.2026, https://startuprecipe.co.kr/archives/5829211: Biverse ist „틱톡샵 공식 파트너(TSP)“ und verkauft „바이버스 템포“ (Influencer-Marketing + TikTok-Shop-Betrieb). Zitat: „**500만 명 규모의 글로벌 인플루언서 데이터**와 축적된 AI 기술력을 활용해 …“.
  - Asia Business Daily via Daum, 22.02.2026, https://v.daum.net/v/1pkYbScno8: Biverse = AX-Startup (Produkt „Maestro“), Gründer Shin Jae-in (Ex-Toss-Entwickler, Ex-Modemarkenbetreiber), Kunden aus Mode und Handel.
  - Forbes Korea 30 under 30 (03.03.2026) und Seed-Runde 1,1 Mrd. KRW (Kakao Ventures u. a., 18.11.2025), nur Schlagzeilen.
- **Konsequenz:** Die Zählung stammt sehr wahrscheinlich aus Biverses eigenem Influencer-Crawl mit einer eigenen oder zugekauften Umsatzschätzung. Denkbar sind Produkt-„sold“-Zähler, die wie bei Kalodata/FastMoss auf Videos umgelegt werden. Die KI-Erkennung läuft vermutlich über TikToks AIGC-Label (öffentliches Feld `aigcLabelType` / `IsAigc`) oder einen eigenen Klassifikator. **Nicht öffentlich verifizierbar.** Bias: Biverse verkauft KI-Content-Produktion und Shop-Betrieb an K-Brands. „KI-Videos verkaufen“ ist deren Verkaufsargument.

### 1.3 Was die Zahlen für das Red Team bedeuten (Estimated)
- 514 Videos > 10.000 USD GMV in **einem** Monat. Als Affiliate mit 10–20 % Provision bringt jedes davon ≥ **1.000–2.000 USD Provision**, allein aus diesem einen Video.
- 76.314 Videos mit 100–10.000 USD GMV entsprechen je 10–2.000 USD Provision.
- Lognormal-Fit durch die beiden veröffentlichten Quantile (P(≥100 USD) = 22,1 %; P(≥10.000 USD) = 0,148 %): μ = 3,00, σ = 2,09 → Median ≈ **20 USD GMV** pro verkaufendem KI-Video, Mittelwert ≈ 178 USD. Bedingte Mittelwerte: 1–100 USD-Klasse ≈ 24 USD, 100–10k-Klasse ≈ 583 USD, > 10k-Klasse ≈ 22.750 USD. Nach dem Fit hätten ≈ 179 Videos ≥ 20k, ≈ 34 ≥ 50k und ≈ 11 ≥ 89k USD erreicht. Das 89.000-USD-Video wäre damit einer von grob einem Dutzend (Estimated, `topdown_out.txt`).
- Die Relativ-Lesart des alten Berichts („≥ 78 % unter 100 USD“) stimmt, trifft aber die falsche Frage. Für die Due-Diligence-Frage zählt nicht das Durchschnittsvideo, sondern die **Zahl der Betreiber im Tail** (siehe Abschnitt 3).

---

## 2. Andere Aggregat- und Anbieterstatistiken zu KI-Content auf TikTok Shop

| Quelle | Aussage | Tag / Metrik | Bias | URL |
|---|---|---|---|---|
| Colaba Blog, „TikTok Shop Creator Analysis 2026“ (21.04.2026), US, März 2026 (4 Wochen), n = „30+ active creators“, „Colaba internal dataset“ | „Beauty Picks Hub (AI content) generates aggressive spikes — $97.85 revenue per follower and 163.24% conversion — despite a smaller audience of about 4K followers.“ vs. „holisticglowupp (personal content) … $26.33 revenue per follower and 2.93% conversion … roughly 11K followers and 300K average video views.“ Fazit: „Yes, AI content can create sharp performance spikes. But personal content tends to be more stable“. | Claimed; „revenue“ = GMV (4 Wochen). Estimated: 97,85 × ≈ 4.000 ≈ **391k USD GMV/4 Wochen** → bei 10–20 % Provision 39–78k USD. Die „163 % conversion“ ist unmöglich (> 100 %), die Methodik ist also fragwürdig. | SaaS-Anbieter für Creator-Management; Footer: „All visuals are mock representations“ | https://www.colaba.us/blogs/tiktok-shop-creator-analysis-2026-who-actually-makes-money-what-sells-and-how-to-scale (Kopie von Schwester-Agent, `research/redteam/col_*.txt`) |
| Business Insider (20.07.2026), via The Keyword (22.07.2026) | Brands erzeugen KI-Kopien von Gewinner-Affiliate-Videos und posten sie „hundreds of times a month“, **ohne Provision** und ohne Samples; **GMV Max** spielt diese KI-Videos aus. Ein KI-Video-Macher: „tens of thousands of dollars in product sales“ (Screenshot von BI gesehen). | Claimed; GMV | BI-Quellen: Agenturen (Third, Socialscale.ai) | https://www.thekeyword.co/news/ai-videos-tiktok-shop-creators |
| RTIH, Gastbeitrag Yu Jiang (JOY22, TikTok-Shop-Creator), 19.05.2026 | „a single video reached approximately two million views and generated **$800,000 in GMV, with more than $90,000 in commission**“; Durchschnitt „approximately **$40 per 1,000 views**“; GMV Max skaliert gut konvertierende Affiliate-Videos „to an extreme level“. | Claimed (Selbstauskunft); GPM ≈ 400 USD/1k beim Ausreißer. Format unbekannt, nicht KI-spezifisch. | Strategieberaterin (JOY22) | https://retailtechinnovationhub.com/home/2026/5/19/the-hidden-economics-of-tiktok-shop-why-content-quality-outperforms-follower-count |
| Marketplace Pulse via Net Influencer (12.06.2026) | ≈ 100.000 US-Seller: **Top 1 % = 60 % des GMV**, Top 0,1 % (< 90 Seller) > 25 %, untere Hälfte ≈ 0,1 % (Lifetime-GMV, geschätzt aus Units × Preis). | Claimed (Analytics); Seller-Konzentration, nicht Creator | – | https://www.netinfluencer.com/tiktok-shop-is-more-top-heavy-than-amazon-with-1-percent-of-sellers-driving-60-percent-of-sales-per-report/ |
| Net Influencer „State of TikTok Shop Q3 2026“ (23.08.2026) | US H1 2026: **11,8 Mrd. USD** (Momentum Works); eMarketer 2026: **23,4 Mrd. USD**; „An estimated two million commissioned creator-marketers“; Kalodata und FastMoss als Branchenstandard. | Claimed; GMV | – | https://www.netinfluencer.com/the-state-of-tiktok-shop-q3-2026/ |
| WSJ/Charm.io (Vorbericht A3) | 945.000 US-Creator mit Sales 2026 (bis Juli) | Claimed | – | via affiversemedia.com |
| TikTok Newsroom / TechTimes (Vorbericht A6) | > 3 Mrd. Videos als KI gelabelt; automatische Erkennung fand Ende 2025 nur **35–45 %** der KI-Inhalte; Kapwing: 59 % KI im FYP neuer Accounts | Claimed | – | techtimes.com |
| FastMoss-Blog (11 Posts 2025/2026, von Schwester-Agent geladen) | **0 Erwähnungen** von „AI-generated/AIGC/AI video“ in Top-Produkt- und Top-Video-Analysen | – | – | `research/redteam/fm_*.txt` |
| Momentum Works „TikTok Shop on track to surpass US$100 billion GMV globally in 2026“ (06.08.2026) | nicht lesbar (Cloudflare 403) | – | – | thelowdown.momentum.asia |

**Nicht gefunden:** eine KI-spezifische Zählung von Kalodata, FastMoss, EchoTik, Tabcut, Shoplus oder Charm.io, ein Anteil KI-gelabelter Videos am Shop-GMV von TikTok selbst, und nichts von Digiday, Modern Retail oder The Information zu KI-Anteilen. Biverse ist die **einzige** Quelle mit Umsatzklassen für KI-Videos.

---

## 3. Top-down-Schätzung (alles Estimated; Code: `research/redteam/aggr/topdown.py`, Ausgabe `topdown_out.txt`)

### 3.1 GMV aus KI-gelabelten Videos, USA, August 2026
Formel: GMV_KI = n1·m1 + n2·m2 + n3·m3 mit n1 = 270.760 (1–100 USD), n2 = 76.314 (100–10k), n3 = 514 (> 10k) (Biverse, Claimed). m = angenommener Mittelwert je Klasse (die Mitte liegt nahe am Lognormal-Fit 24 / 583 / 22.750).

| Szenario | m1 / m2 / m3 (USD) | GMV_KI / Monat | Anteil Top-514-Videos | Anteil am US-Shop-GMV (1,9 / 2,1 / 2,3 Mrd. USD/Monat*) |
|---|---|---|---|---|
| low | 12 / 500 / 15.000 | **49,1 Mio. USD** | 16 % | 2,6 % |
| mid | 25 / 900 / 22.000 | **86,8 Mio. USD** | 13 % | 4,1 % |
| high | 40 / 1.500 / 35.000 | **143,3 Mio. USD** | 13 % | 6,2 % |

*US-Monats-GMV: H1 2026 = 11,8 Mrd. USD → Ø 1,97 Mrd./Monat (Momentum Works, Claimed); eMarketer 2026 = 23,4 Mrd. → Ø 1,95 Mrd./Monat. Für August habe ich 1,9–2,3 Mrd. angesetzt.
In allen Szenarien entfallen ≈ 92–93 % des KI-GMV auf die ≈ 22 % der Videos mit ≥ 100 USD.

### 3.2 Provisionspool
Pool = GMV_KI × Affiliate-Anteil × Provisionssatz × (1 − 10 % Retouren).
- Affiliate-Anteil 40 / 55 / 70 %. Ein Teil der KI-Videos läuft über Marken- oder Seller-eigene Konten ohne Provision (BI: Brands posten KI-Videos „hundreds of times a month“).
- Provisionssatz 10 / 13,1 / 20 % (13,1 % = Durchschnitt 2025 laut eMarketer/Momentum Works, Vorbericht).

| Szenario | Pool / Monat | mit Untererfassungs-Faktor für ungelabelte Hybrid-KI (×1,0 / ×1,5 / ×2,5)** |
|---|---|---|
| low | **1,77 Mio. USD** | 1,8 Mio. |
| mid | **5,63 Mio. USD** | 8,4 Mio. |
| high | **18,05 Mio. USD** | 45,1 Mio. |

**Begründung für den Faktor: TTS-Voiceover, KI-Skripte, KI-Varianten und KI-B-Roll ohne Label fallen durch jede label-basierte Zählung. TikToks eigene Detektion fand Ende 2025 nur 35–45 % der KI-Inhalte (TechTimes, Claimed). Bei @beautypickshub trägt das Top-Video (184.600 Plays, Skript-Voiceover) **kein** KI-Label.

### 3.3 Zahl der KI-Betreiber über Schwellen (Provision pro Monat)
Annahmen:
- Zahl der Betreiber mit ≥ 1 verkaufendem KI-Video: N = 8.000 / 15.000 / 30.000. Das entspricht 347.588 verkaufenden Videos ÷ 12–43 verkaufenden Videos je Betreiber. Ein Betreiber hat oft mehrere Konten. Zum Vergleich: 29.111 „AI influencer accounts“ ≥ 50k Follower laut Biverse.
- Verteilung lognormal mit σ = 1,5 / 2,0 / 2,5. Top-1-%-Anteil am Pool: 20 / 37 / 57 %. Top-5-%-Anteil: 44 / 64 / 80 %. Zum Vergleich: Seller-Top-1 % = 60 % (Marketplace Pulse).
- Ergebnis: Spannweite über N und σ, nur gelabelter Pool, ohne Hybrid-Faktor.

| Pool | ≥ 3.000 USD | ≥ 5.000 USD | ≥ 10.000 USD | ≥ 20.000 USD |
|---|---|---|---|---|
| low (1,8 Mio.) | 11–87 | 3–50 | 0–22 | 0–9 |
| **mid (5,6 Mio.)** | **141–344** | **49–190** | **10–83** | **2–38** |
| high (18,1 Mio.) | 690–1.389 | 460–802 | 131–326 | 30–146 |

Mit Hybrid-Faktor 1,5 (mid) steigen die Mid-Werte um grob 40–70 %: ≈ 250–500 Betreiber ≥ 3k, ≈ 20–120 ≥ 10k.

**Plausibilitätscheck von unten:**
- Allein @spongebobprodsz (Abschnitt 4.1) läge mit ≈ 302k USD GMV/30 Tage (Kalodata, Claimed) bei 15–60k USD Provision. Das ist ≈ 0,2–0,6 % des geschätzten KI-GMV und passt zu „einige Dutzend Betreiber ≥ 20k“ im Mid-/High-Szenario.
- Die 514 Videos > 10k USD verteilen sich mindestens auf einige Dutzend bis einige Hundert Konten. Schon diese Videos allein bringen ihren Betreibern je ≥ 1–2k USD Provision.

**Ergebnis:** Das Mid-Szenario ergibt **Hunderte** US-KI-Betreiber mit ≥ 3.000 USD und **Dutzende** mit ≥ 10.000 USD Provision in einem Monat. Anteilig sind das nur ≈ 1–4 % aller KI-Betreiber. „Selten“ stimmt also relativ, aber „praktisch nicht existent“ oder „nur Kursverkäufer“ stimmt absolut nicht. Die Unsicherheit ist groß: Faktor ≈ 10 zwischen low und high. Die größten Hebel sind die Mittelwerte der Klassen (Biverse-Rohdaten fehlen) und der Affiliate-Anteil.

**Einschränkungen:**
1. Biverse-Methodik unbekannt; Schätzwerte eines Vendors.
2. Ein Monat (August) sagt nichts über Dauerhaftigkeit; Churn ist unbekannt.
3. Die Kategorie „AI video“ bei Biverse ist wahrscheinlich label-basiert und enthält auch Brand-Accounts.
4. Ein Teil des GMV entsteht über GMV-Max-Werbung der Marke. Die Provision fließt trotzdem an den Affiliate, dessen Video genutzt wird, eventuell zu einem gesonderten Ads-Provisionssatz. Deshalb setze ich 5–20 % an.

---

## 4. Konkrete KI-(gelabelte) shoppable Konten und Videos mit hohen Umsätzen

### 4.1 @spongebobprodsz („Finds4dayz“) – Kategorie **G** (KI-generierte Szene/B-Roll + reales Produkt, Skript-Voiceover, KI-Label)
- **Quelle der Umsatzzahl:** Moe Alamawi (Momentum TT Academy, Kurs/1:1-Coaching; Kalodata- und Higgsfield-Links in der Beschreibung), „These Ai Videos Generated $1.3M in 5 months on TikTok Shop“, veröffentlicht 29.07.2026, 63.797 Views: https://www.youtube.com/watch?v=Yyq9Htlghg8.
  - Transkript [0:03]: „this creator who's done over 1.3 million dollars in less than 5 months. He started in February 2026 … He didn't post AI avatars … posting short AI videos“.
  - [0:29]: „in the last 30 days … he's tested over 320 different products“.
  - [2:10]: „to be able to do 300k within 30 days … with SpongeBob in his name and a fruit bowl as a profile picture with only 24,000 freaking followers“.
  - Mechanismus laut Sprecher: GMV Max („all of the brand's money will go behind your videos“).
  - Die Kalodata-Karte hat der Vorbericht per Watch-Tool bei 2:05–2:38 abgelesen: „@spongebobprodsz“, „24.5K“, „Revenue $302.09k“, „Video Revenue $301.81k“ (30 Tage).
  - Das Thumbnail (heute selbst angesehen, `aggr/yt/moe_thumb.jpg`) zeigt das Profil „Finds4dayz / spongebobprodsz, 24.8K Followers, 102.5K Likes“, Videos mit 1,2 Mio. (Terro-Ameisenköder), 856k und 732k Views sowie das Label „$1.3M“.
  - **Evidenztyp:** Analytics-Plattform (Kalodata-Schätzung), vorgeführt von einem Kursverkäufer. Keine Selbstauskunft des Kontoinhabers.
- **Heute verifiziert (tt_profile.sh / tt_recent.sh / tt_video.sh, 25.09.2026):**
  - Profil: 28.800 Follower (Ende Juli ≈ 24,8k → **wächst**), 149.700 Likes, 1.172 Videos, angelegt 19.11.2021, Bio „The best finds for health and beauty ❤️“, commerceUser = false.
  - 10 neueste Videos (24./25.09.2026): **10/10 aigcLabelType = 1 (KI-Label)**, **10/10 isECVideo = 1**, 10/10 Anker Typ 35 (Produkt) + 54 (CapCut), **5/10 isAd = true**, Dauer 10–12 s, Caption „Wonderful deal #tiktokshop #trending“.
  - Plays 48–8.880 (frisch gepostet, Median ≈ 390). Bis ≈ 13 Uhr UTC 6 Posts am 25.09. → **≈ 6–10 Videos/Tag**.
  - Der Vorbericht-Kommentar „doesnt have yellow basket“ ist damit für September 2026 widerlegt: Die Videos tragen Produkt-Anker.
- **tt_media.py auf Video 7688930509723831583** (8.880 Plays, 24.09.2026, isAd = true):
  - Kontaktbogen: medicube „Deep Vita C Capsule Cream“ (2 Dosen) auf Marmorplatte, wechselnde KI-generierte Szenen (Küche, Weihnachtsküche, Gartentisch), Sticker „🚨FLASH DEAL🚨 / LIMITED⏳“. **Keine Person, keine Hände.**
  - ASR: „This is gonna be the last day to get it for crazy prices like this. If you wanna get this, make sure you add it to your cart…“ Das ist dasselbe Skript, das der Kursverkäufer als Formel vorspielt. Leiser Ton (mean −43,7 dB).
  - IsAigc-Feld in tt_media = false, aigcLabelType im Video-JSON = 1. Das Label steht also im Label-Typ-Feld.
- **Rechnung (Estimated):**
  - 302.090 USD GMV / 30 Tage × 5–20 % Provision (reguläre oder GMV-Max-Ads-Provision; medicube, BPN, TIRTIR, Terro) × 0,9 Retouren ≈ **13,6–54,4k USD Provision / 30 Tage**.
  - 1,3 Mio. USD / 5 Monate ≈ 260k USD GMV/Monat → **11,7–46,8k USD/Monat**.
  - Toolkosten ≈ 7–10 Videos/Tag × 30 × 0,3–3 USD ≈ 60–900 USD/Monat. Hinzu kommt eventuell ein Account-Kauf.
  - → Gewinn **≈ 11–54k USD/Monat**, falls die Kalodata-Schätzung stimmt.
  - GMV pro Video ≈ 302k / (≈ 210–300 Videos) ≈ 1.000–1.440 USD Ø, stark schief verteilt.
- **Grenzen:**
  - Kalodata-Zahlen sind Schätzungen (Units × Preis, auf Videos umgelegt).
  - Ein Großteil des GMV kommt vermutlich aus Brand-GMV-Max-Budget. Die Plays auf den Top-Videos (1,2 Mio.) sind bezahlte plus organische Reichweite. Das hängt am Ads-Budget der Brands, ist also volatil.
  - Der aktuelle Monats-GMV ist nicht öffentlich. Die Views der neuesten Videos sind klein.
  - Die Ads-Provisionssätze sind unbekannt.

### 4.2 @beautypickshub („Beauty Picks Hub“) – Kategorie **D/H** (echte Hände + Produkt + Skript-Voiceover, TTS-artig; teils Foto-Slideshows mit KI-Label)
- Colaba (s. Abschnitt 2) nennt es „AI content“ mit 97,85 USD Umsatz pro Follower bei ≈ 4k Followern im März 2026 (Claimed).
- Verifiziert 25.09.2026: 7.363 Follower, 89.000 Likes, 427 Videos, angelegt 11.02.2025. Bio „Your Daily Beauty Picks We test pick&share what really works … The promotional discount event hasended the final price is based on the product's actual selling“. commerceUser = false.
- 10 neueste Posts (22.07.–24.09.2026):
  - 9/10 isAd = true, 9/10 isECVideo = 1, 7/10 mit Produkt-Anker. 3 Posts mit aigcLabelType = 2 (alles Foto-Slideshows mit Dauer 0).
  - Plays 449–**184.600**. Fünf fast identische Varianten gingen am 22./23.07. online: **70.800 / 184.600 / 86.900 / 2.569 / 1.688 Plays** bei nur 2–234 Likes. Das Likes/Plays-Verhältnis spricht für bezahlte Reichweite.
- tt_media.py auf 7665691177278082335 (184.600 Plays):
  - Kontaktbogen: Tarte-BB-Creme-Set im Autoinnenraum, **nur manikürte Hände**, keine Person.
  - ASR: „Oh my gosh! You get the Viral Tarte BB Blur Tinted Moisturizer! … Stock is crashing! Tap the cart below right now…“. Voiceover-Skript, Stimme menschlich oder TTS nicht bestimmbar.
  - **Kein KI-Label** auf diesem Top-Video.
- Estimated nach Colaba: ≈ 391k USD GMV/4 Wochen → 39–78k USD Provision. **Nicht plausibilisierbar.** Die Views der neuesten Videos (max. 184.600) würden bei 30–40 USD GMV/1k Views nur ≈ 7k USD GMV erklären. Die „163 % conversion“ ist unmöglich. → **weak**.
- Wert des Falls: Er zeigt, dass Analytics-Anbieter solche **ungelabelten Hybrid-Formate** als „AI content“ zählen und dass sie mit Ads-Verstärkung sechsstellige Plays erreichen. Das spricht gegen die enge KI-Definition des alten Berichts.

### 4.3 Biverse-„89.000-USD-in-30-Tagen“-Video (Kategorie A: zwei vollständig synthetische Frauen, Latzhosen-Jeans)
- Handle, Marke und Preis sind nicht genannt, das Video ist nicht identifizierbar. **UNVERIFIABLE** (siehe Vorbericht).

### 4.4 Nebenbefund Kursverkäufer-Claims zu KI-Videos
Diese Zahlen sind nicht weiter geprüft und Sache des YouTube-Dashboard-Agenten:
- Jon Knowles: „these 7-second AI videos … made me over $25,000 in the last 60 days from one account“ (EMUALbMNV94, Kalodata/Higgsfield-Affiliate). Self-report, Vendor.
- Moe Alamawi: Thumbnail „$37.8K Commissions“ (KFEsHHB--bs). Self-report, Vendor.
- Thailändischer Kanal: „Using AI to Create TikTok Product Review Videos, Spotting 13 Million in Sales with Kalodata“ (DvEczhPp8Ro). TH-Markt, nicht geprüft.

---

## 5. Schlussfolgerungen zu C1–C4 (Stand der Red-Team-Evidenz aus diesem Winkel)

- **C1 („voll virtuelle KI-Influencer funktionieren für TikTok Shop praktisch nicht“):**
  - Für **Kategorie A im engen Sinn** (Avatar-Persona) habe ich keinen verifizierten Umsatzbeleg gefunden. Das Biverse-89k-Video ist A, aber nicht identifizierbar.
  - Biverse zählt aber 29.111 „AI influencer accounts“ ≥ 50k Follower und 514 KI-Videos > 10k USD GMV in einem Monat. Wie viele davon A sind, ist unbekannt.
  - **Teilweise angegriffen:** Voll-KI-**Videos** ohne Persona (Kategorie G, @spongebobprodsz) funktionieren nachweislich im großen Stil. Die Grenze liegt beim Avatar, nicht bei der KI.
- **C2 („KI-Shop-Accounts mit hohen Views sind meist kurzlebige Supplement-Netzwerke“):**
  - **Angegriffen.** @spongebobprodsz ist Beauty/Home (medicube, Terro, TIRTIR, BPN), kein Supplement-Netzwerk. Es ist seit ≥ 7 Monaten aktiv, wächst weiter (24,8k → 28,8k Follower) und postete am Prüftag KI-gelabelte shoppable Videos.
  - Biverses 347.588 verkaufende KI-Videos in einem Monat sprechen gegen „meist Supplement-Netzwerke“. Kategorien liegen aber nicht vor.
- **C3 („dauerhafte vierstellige Monatsprovisionen mit KI-Content sind selten“):**
  - **Relativ korrekt, absolut zu pessimistisch.** Top-down (Mid-Szenario) ergibt ≈ 140–340 US-Betreiber ≥ 3k USD/Monat nur mit gelabeltem KI-Content, mit Hybrid-Untererfassung mehr. Ein konkretes Konto liegt nach Analytics-Schätzung bei ≈ 12–54k USD/Monat.
  - Die „Dauerhaftigkeit“ ist nur für ≈ 7 Monate belegt (spongebobprodsz). Sie hängt an Brand-Ads-Budgets (GMV Max) und Policy-Wellen.
- **C4 („10k+-USD-Claims kommen meist von Kursverkäufern“):**
  - **Teilweise korrekt, als Evidenzregel aber irreführend.** Die Überbringer hoher Zahlen sind tatsächlich Vendoren: Biverse = TSP/Agentur, Colaba = SaaS, Moe Alamawi = Kurs.
  - Die Zahlen selbst sind aber teils **Analytics-Schätzungen über Dritt-Accounts** (Kalodata-Karte zu @spongebobprodsz) und keine Selbstauskünfte. Solche Fälle mit dem Argument „Kursverkäufer“ komplett zu verwerfen, war zu streng.
- **Randbemerkung C5–C7:**
  - Das C5-Modell (Ø 4.000 organische Views, 30 USD GMV/1k Views, 5 Videos/Tag) bildet den tatsächlich genutzten Hebel nicht ab: GMV Max leitet Brand-Budget auf klickstarke Affiliate-Videos.
  - Das Top-Konto postet 6–10 Videos/Tag (≈ 200–300/Monat) und liegt laut Kalodata bei ≈ 300k USD GMV/Monat. Das ist ≈ 1.000–1.400 USD GMV pro Video. C5 unterstellt ≈ 120 USD GMV pro Video (4.000 × 30/1.000).
  - C6/C7 („830 bzw. 1.650 Videos/Monat für 10k/20k EUR“) wären für solche Konten um Faktor 3–8 zu hoch. Das gilt aber nur für die Tail-Betreiber mit Ads-Hebel, nicht für den Median, und die Kalodata-Werte sind Schätzungen.

---

### Verifikation F1 – Biverse-Aggregat (347.588 / 76.314 / 514; 26.839 / 1.464 / 808)
- **Quelle erneut geöffnet:** `cho_ko.html` (Chosun KO) vollständig re-extrahiert, die Zahlen stimmen wörtlich. Keine weiteren Zahlen, keine Methodik.
- **Handle-Check:** entfällt, es gibt keine Handles.
- **Metrik:** GMV (매출), Zeitraum August 2026, USA.
- **Bias:** Biverse ist TSP und verkauft KI-Content und Shop-Betrieb. Die Datenbasis ist vermutlich eine eigene Influencer-Datenbank (5 Mio.), keine offizielle TikTok-Umsatz-API.
- **Arithmetik nachgerechnet:**
  - 347.588 − 76.314 − 514 = 270.760 (Klasse 1–100 USD).
  - Anteile 77,9 % / 22,0 % / 0,148 %.
  - Lognormal-Fit σ = 2,09, Median 20 USD.
  - GMV 49–143 Mio. USD (Estimated).
- **Verdict: UNVERIFIABLE (Rohdaten), Zitat CONFIRMED.** Die Red-Team-Lesart (Hunderte Betreiber im Tail) ist eine Schätzung auf unverifizierter Basis. Als Größenordnung wird sie gestützt, weil ein Einzelkonto (spongebobprodsz) allein schon 0,2–0,6 % davon ausmacht.

### Verifikation F2 – @spongebobprodsz (Kategorie G, KI-gelabelt, Kalodata 302k USD GMV/30 Tage)
- **Quelle erneut geöffnet:** YouTube-Details (29.07.2026, 63.797 Views, Kalodata- und Higgsfield-Links, Coaching-Formular), Transkript (Zitate oben) und Thumbnail (Handle-Schreibweise „spongebobprodsz“ lesbar).
- **Kalodata-Karte:** Heute nicht erneut ablesbar. Das Watch-Tool-Kontingent ist erschöpft, der YouTube-Download scheiterte (HTTP 403, kein ffmpeg). Grundlage ist die Ablesung des Vorberichts („Revenue $302.09k“).
- **TikTok-Prüfung:** Profil live, 28.800 Follower. 10 neueste Videos: 10/10 KI-Label, 10/10 shoppable, 5/10 Ads, 6 Posts am Prüftag. Klassifikation per tt_media.py: KI-Szene + reales Produkt, keine Person → **G**.
- **Arithmetik:** 302.090 × 0,05–0,20 × 0,9 = 13.594–54.376 USD.
- **Metrik:** GMV (Kalodata-Schätzung), 30 Tage (≈ Juli 2026). Provision und Gewinn sind Estimated.
- **Bias:** Kursverkäufer mit Kalodata-/Higgsfield-Affiliate, führt das Konto als Vorbild vor.
- **Verdict: PARTIALLY.**
  - CONFIRMED sind Format (G), KI-Label, Shoppability, laufende Ads, Aktivität ≥ 7 Monate und Follower-Wachstum.
  - Die Umsatzhöhe ist nur Analytics-Schätzung über einen Vendor.
  - Korrigierte Provision: **≈ 12–54k USD/Monat (Estimated)**, statt „10–15 % = 30–45k“ im Vorbericht. Die Spanne ist breiter, weil der Ads-Provisionssatz unbekannt ist.
  - Die Kategorie im Vorbericht war „F/E“. Korrekt ist **G** (KI-generierte Szene, KI-Label).

### Verifikation F3 – Top-down: Zahl der KI-Betreiber ≥ 3k / 10k USD Provision
- **Nachgerechnet** mit `topdown.py` (deterministisch): Pool low/mid/high = 1,77 / 5,63 / 18,05 Mio. USD.
- **Sensitivität:** Die Zahl der Betreiber ≥ 3k variiert im Mid-Pool über N (8k–30k) und σ (1,5–2,5) zwischen 141 und 344.
- **Größte Unsicherheiten:**
  - Klassenmittelwert m2: 500–1.500 USD verschiebt den Pool um Faktor 3.
  - Affiliate-Anteil (40–70 %).
  - Biverse-Methodik.
  - Einmonatsbetrachtung ohne Churn.
- **Gegencheck gegen harte Daten:**
  - Die bekannten menschlichen Top-Affiliates liegen bei 1–4 Mio. USD GMV/Monat (Vorbericht). Der KI-Pool wird von keinem Einzelnen dominiert, das passt.
  - Seller-Konzentration Top 1 % = 60 % (Marketplace Pulse). Das liegt oberhalb von σ = 2,5 (57 %). Mein σ-Band ist daher eher **konservativ**, bei gegebenem Pool gäbe es tendenziell **weniger** Betreiber ≥ 3k und mehr ≥ 20k.
- **Verdict: PARTIALLY** (Größenordnung robust, Punktwerte nicht belastbar).
  - Belastbare Aussage: „**zweistellig bis niedrig vierstellig** US-KI-Betreiber ≥ 3k USD/Monat; **einstellig bis niedrig dreistellig** ≥ 10k USD/Monat“, Estimated.

---

## Quellen (Abruf 2026-09-25)
- Chosun Ilbo KO: https://www.chosun.com/economy/tech_it/2026/09/07/ARR3UW4S5NGCNBDKWOK7QDMPJI/ (lokal `cho_ko.html`); EN: https://www.chosun.com/english/industry-en/2026/09/07/ZYF2BRJVGZBWXKFRDP5Y67TUXU/ ; MSN: https://www.msn.com/en-xl/technology/artificial-intelligence/ai-influencers-generate-89-000-in-30-days/ar-AA2bGqjJ
- Startup Recipe 11.08.2026: https://startuprecipe.co.kr/archives/5829211 (`aggr/startuprecipe.html`)
- Asia Business Daily via Daum 22.02.2026: https://v.daum.net/v/1pkYbScno8 (`aggr/daum.html`)
- Forbes Korea (Schlagzeile): https://www.forbeskorea.co.kr/news/articleView.html?idxno=401372
- Colaba: https://www.colaba.us/blogs/tiktok-shop-creator-analysis-2026-who-actually-makes-money-what-sells-and-how-to-scale
- The Keyword 22.07.2026: https://www.thekeyword.co/news/ai-videos-tiktok-shop-creators
- RTIH 19.05.2026: https://retailtechinnovationhub.com/home/2026/5/19/the-hidden-economics-of-tiktok-shop-why-content-quality-outperforms-follower-count
- Net Influencer / Marketplace Pulse: https://www.netinfluencer.com/tiktok-shop-is-more-top-heavy-than-amazon-with-1-percent-of-sellers-driving-60-percent-of-sales-per-report/ ; https://www.netinfluencer.com/the-state-of-tiktok-shop-q3-2026/
- Affiverse 11.02.2026: https://www.affiversemedia.com/the-growth-of-ai-influencers-and-how-they-are-being-leveraged-to-drive-reels-and-tiktok-sales/ (Kontext: Charm.io US-GMV-Reihe, eMarketer 23,41 Mrd.)
- Momentum Works: https://thelowdown.momentum.asia/tiktok-shop-on-track-to-surpass-us100-billion-gmv-globally-in-2026/ (403)
- YouTube: https://www.youtube.com/watch?v=Yyq9Htlghg8 (Transkript `aggr/moe_1p3m.txt`, Thumbnail `aggr/yt/moe_thumb.jpg`); https://www.youtube.com/watch?v=EMUALbMNV94 (Transkript `aggr/jonknowles_25k.txt`); Thumbnails KFEsHHB--bs, dgb-xCkZpyc, DvEczhPp8Ro, vR1kLuCNDOo
- TikTok: https://www.tiktok.com/@spongebobprodsz (+ Videos 7689368021462289677, 7689364246806793486, 7689349556105956621, 7689344037765074189, 7689335177838972173, 7689310364248378638, 7688957358701104415, 7688930509723831583, 7688920476969667870, 7688898777058462989); https://www.tiktok.com/@beautypickshub (+ Videos 7689132417944227103, 7685301974258044190, 7683518279738035487, 7676107111083937054, 7671368646588943647, 7665766771110006047, 7665720128159370527, 7665699657099545886, 7665691177278082335, 7665389455573798174)
