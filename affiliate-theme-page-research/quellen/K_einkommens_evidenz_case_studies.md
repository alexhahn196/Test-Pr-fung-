# K – Einkommens-Evidenz & Case Studies (Reality Check)

**Forschungsfrage:** Kann eine einzelne, KI-generierte, faceless Social-Media-Theme-Page (Instagram Reels primär; TikTok / YouTube Shorts / Pinterest sekundär) **ausschließlich über Affiliate-Provisionen** 5.000 / 10.000 / 20.000 € **Gewinn** pro Monat erzielen?

**Prüfdatum:** 2026-09-26 · **Rohdaten:** `raw_income_evidence.csv` (69 Datenpunkte, gleiche IDs wie unten)

---

## 0. Kurzfazit

1. **Kein einziger verifizierter Fall** einer einzelnen faceless Instagram-Theme-Page mit ≥ 5.000 € Affiliate-Gewinn pro Monat gefunden. Alle Fälle über ~2.000 $/Monat sind entweder **Personen-Creator** (LTK, Amazon-Influencer, TikTok-Shop-Livestreamer), **Amazon-Onsite-Videos** (Traffic kommt von Amazon selbst, nicht aus Social Media), **Portfolios aus mehreren Pages**, **Schätzungen Dritter** oder **Guru-/Kurs-Claims mit Interessenkonflikt**.
2. **Views sind nicht der Engpass, Kaufabsicht ist es.** Die rechenbaren Datenpunkte streuen über mehr als vier Größenordnungen: Unterhaltungs-/Repost-Views auf Instagram bringen **~0–3 $ pro 1 Mio. Views** (B03, E04, E05), Pinterest-Impressions **~0,33 $ pro 1 Mio.** (B04). Shopping-nahe Inhalte liegen bei **~500–900 $ pro 1 Mio. Views** (C03, D01, B10, B11). Einzelne Ausreißer mit Werbeunterstützung erreichen laut Drittschätzung **~16.000 $** (C01, KI-Supplement-Video auf TikTok Shop).
3. **Plattform-Statistiken zeigen eine extreme Schiefverteilung.** Mavely zahlte 2024 im Schnitt **~27 $ pro Creator und Monat** (A03). Laut einer nicht verifizierten Schätzung erreichen nur die obersten ~1 % der TikTok-Shop-Affiliates im Schnitt ~6.500 $ Provision pro Monat (A09). In einer Umfrage unter Affiliates aller Kanäle verdienen ~12–17 % ≥ 5.000 $/Monat und < 4 % ≥ 20.000 $/Monat (A05).
4. **Urteil (Details in Abschnitt 6):** 5.000 € = *Possible but weak evidence*. 10.000 € = *Possible but weak evidence*, und zwar nur über TikTok-Shop-Ausreißer; für Instagram allein gibt es *No credible evidence*. 20.000 € = *No credible evidence* für einen nachhaltigen Monatsgewinn; es gibt nur eine einzelne Drittschätzung.

---

## 1. Methodik

**Suchwege (tatsächlich genutzt):**
- Web-Suche: Das Suchbudget der Session war nach wenigen Abfragen erschöpft. Danach wurde direkt abgerufen (WebFetch/curl) über:
  - Plattform-Seiten: LTK-Newsroom, TIME, TechCrunch-Archivsuche (Mavely, ShopMy), Goldman Sachs, Linktree Creator Report, IMH-Reports (PDF ausgewertet)
  - Kuratoren-Datenbank **eBiz Facts** (Site-Suche nach „faceless instagram“, „tiktok shop“, „amazon influencer“, „pinterest“ usw.)
  - **Reddit** über die öffentliche RSS-Suche: ~40 Suchanfragen in r/AffiliateMarket, r/Affiliatemarketing, r/Amazon_Influencer, r/TikTokshop, r/InstagramMarketing, r/juststart u. a. Die direkten Seiten und die JSON-API sind blockiert.
  - **Flippa**: Listing-JSON der Such-Seiten für Instagram-/TikTok-Konten, offene und verkaufte
  - **Fameswap**: Browse-Seite; Details erst nach Login
- Nicht erreichbar: Business Insider (Crawler-Sperre / HTTP 410), Reddit-Direktseiten, Medium-Artikel (403), Forbes (403), SocialTradia (Cloudflare), Flippa- und Fameswap-Details hinter Login.

**Klassifikation je Datenpunkt:**

| Feld | Werte | Bedeutung |
|---|---|---|
| Evidenztyp | Observed / Plausible / Possible but weak evidence / No credible evidence | *Observed* = Plattform-Statistik oder eigene Prüfung. *Plausible* = detaillierte, in sich konsistente Angabe ohne erkennbaren Verkaufsanreiz. *Possible but weak* = Einzelclaim, Schätzung, Interessenkonflikt oder unklare Einnahmeart. *No credible* = Modell, Widersprüche oder nicht prüfbar |
| Datenqualität | VERIFIED / THIRD-PARTY ESTIMATE / CLAIMED / UNKNOWN | *VERIFIED* heißt hier: offiziell publizierte Plattform-/Unternehmensangabe oder eigene Seitenprüfung. Diese Angaben sind **nicht unabhängig auditiert**. Kein einziger Einzel-Creator-Fall ist unabhängig verifiziert |
| Account-Typ | Person / faceless Theme-Page / Deal-Page / AI-Page / unklar | Personen-Creator werden strikt von faceless Pages getrennt (Abschnitt 8) |

**Rechenregeln:**
- „Provision pro 1 Mio. Views“ wird **nur** berechnet, wenn Views (bzw. Impressions) und Provision für denselben Zeitraum genannt sind. Der Rechenweg steht jeweils in der CSV.
- Annahmen sind markiert: Obergrenze (≤), GMV→Provision mit angenommenem Satz.
- Beträge bleiben in Originalwährung (meist USD). **Grobe Umrechnung: 1 $ ≈ 0,85–0,92 € (Annahme, nicht tagesaktuell geprüft).**
- **Gewinnziel ≠ Provision:** Für 5k/10k/20k € Gewinn braucht man grob **≈ 6k / 12k / 24k $ Provision pro Monat**, ohne Steuern und nur mit geringen Tool-, KI- und Assistenzkosten.
- **Interessenkonflikte** (Kurs-, Guide-, Tool-, Agentur- oder Verkäufer-Interesse) sind je Datenpunkt markiert. Guru-Claims werden nie höher als *Possible but weak evidence* eingestuft.

---

## 2. Datenpunkte-Tabelle (alle 69; vollständige Felder und Rechenwege in der CSV)

Legende: **A** = Plattform-/Studiendaten · **B** = Amazon (Associates/Influencer) · **C** = TikTok Shop · **D** = faceless/Theme-/AI-Pages · **E** = Marktplätze

| ID | Fall | Account-Typ | Plattform | Views/Follower | Umsatz/Provision (Zeitraum) | $ pro 1 Mio. Views | Evidenz | Qualität | Quelle |
|---|---|---|---|---|---|---|---|---|---|
| **A – Plattform-/Studiendaten** | | | | | | | | | |
| A01 | LTK Plattformstatistik (Unternehmensseite) | Person (überwiegend Gesichts-Creator) | LTK (Traffic v.a. Instagram) | – | >130 Creator mit ≥1 Mio. $ (kumuliert); Creator haben kumuliert 1 Mrd. $ über LTK verdient; ~5 Mrd. $ Händlerumsatz/Jahr (kumuliert bis 2026) | – | Observed | VERIFIED | [Link](https://company.shopltk.com/en/press) |
| A02 | LTK laut TIME100 Companies 2025 | Person | LTK | 40 Mio.+ Shopper/Monat | 'Hundreds of creators have made $1 million or more' (lt. Unternehmen); >5 Mrd. $ Jahresumsatz über Plattform (kumuliert bis 2025) | – | Observed | VERIFIED | [Link](https://time.com/collections/time100-companies-2025/7289649/ltk/) |
| A03 | Mavely Auszahlungen 2024 (TechCrunch) | Person (Micro/Nano 'Everyday Influencer… | Mavely (Instagram/TikTok-Links) | >85.000 Creator | 16 Mio. $ ausgezahlt (Provisionen+Kampagnenhonorare) Jan–Jul 2024; kumuliert 37 Mio. $ (Jan–Jul 2024) | – | Observed | VERIFIED | [Link](https://techcrunch.com/2024/08/27/mavely-influencer-social-commerce-platform-675m-gmv/) |
| A04 | ShopMy (TechCrunch 2024) | Person | ShopMy | – | 'tens of millions in commissions' kumuliert; Provisionssätze 10–30% (kumuliert bis 03/2024) | – | Observed | VERIFIED | [Link](https://techcrunch.com/2024/03/14/shopmy-influencer-marketing-platform-lands-18-5-million-funding-round/) |
| A05 | IMH Affiliate Marketing Benchmark Report (Umfrage) | gemischt (alle Affiliates inkl. Blogger) | kanalübergreifend | – | 57,55% <10k $/Jahr; 16,21% 10–50k; 5,15% 50–100k; 7,94% 100–150k; 3,78% >150k $/Jahr Affiliate-Einkommen (Umfrage 2022 (PDF 'Benchmark 2023')) | – | Plausible | THIRD-PARTY ESTIMATE | [Link](https://influencermarketinghub.com/ebooks/Affiliate_Marketing_Benchmark-Report-2023.pdf) |
| A06 | Linktree Creator Report 2022 (n=9.576) | Person/gemischt | kanalübergreifend | – | 12% der Vollzeit-Creator >50k $/Jahr; 46% <1k $; Affiliate (ohne Amazon) genutzt von 10–15% (Befragung 2021) | – | Plausible | THIRD-PARTY ESTIMATE | [Link](https://linktr.ee/creator-report/) |
| A07 | Goldman Sachs Creator Economy (2023) | gemischt | kanalübergreifend | – | ~4% der Creator gelten als 'professionell' (>100k $/Jahr) (2023) | – | Plausible | THIRD-PARTY ESTIMATE | [Link](https://www.goldmansachs.com/insights/articles/the-creator-economy-could-approach-half-a-trillion-dollars-by-2027) |
| A08 | IMH/NeoReach Creator Earnings Report 2025 (n>3.000) | Person/gemischt | kanalübergreifend | 1,1 Mrd. Follower aggregiert | >50% der Creator <15k $/Jahr; ~57% der Vollzeit-Creator unter US-Living-Wage; keine Affiliate-Aufschlüsselung (2025) | – | Plausible | THIRD-PARTY ESTIMATE | [Link](https://influencermarketinghub.com/creator-earnings-report-2025/) |
| A09 | TikTok-Shop-Affiliate-GMV-Verteilung (Short Form Nation, 1,2 Mio. Pro… | gemischt | TikTok Shop | 1,2 Mio. Creator-Profile | Top 1%: Ø 600k $ GMV/Jahr; Top 5%: 80k $; Top 20%: 8k $; untere 80%: 200–800 $ GMV/Jahr (ca. 2025/26) | – | Possible but weak evidence | THIRD-PARTY ESTIMATE | [Link](https://www.shortformnation.com/blog/tiktok-shop-affiliate-marketing-the-complete-2026-guide) |
| A10 | 'Amazon Influencer Program Statistics 2026' (SEO-Aggregator) | unklar | Amazon | – | u.a. 'Micro-Creator Ø 312 $/Monat' vs. 'Nano-Creator Median 1.340 $/Monat' (widersprüchlich); 'Median 7-Monats-Einkommen 24.360 $' bei ≥1.0… (2026 (angeblich)) | – | No credible evidence | UNKNOWN | [Link](https://www.amraandelma.com/amazon-influencer-program-statistics/) |
| **B – Amazon (Associates / Influencer / Onsite)** | | | | | | | | | |
| B01 | lgsagency: neues faceless IG-Konto -> Amazon Storefront | faceless Theme-Page (Home-Finds; 1x Sei… | Instagram Reels -> Amazon Influencer Storefr… | 216 -> 3.084 Follower in 48 Tagen; 61 Posts; mehrere Reels >100k Views; 11.232 Storefront… | 531,16 $ Provision (Mai) aus 13.145,50 $ versandtem Umsatz; gesamt 789,63 $ inkl. Boni/Brand-Deal in 48 Tagen (48 Tage (Apr.–Mai 2026; Artikel vom 02.…) | – | Plausible | CLAIMED | [Link](https://lgsagency.substack.com/p/i-started-a-brand-new-instagram-account) |
| B02 | lgsagency: Kunden-Claims 36k $ bzw. >100k $/Monat | unklar | Amazon Influencer Program | – | 'clients consistently generating $36,000 a month'; 'one client clearing over $100,000 a month' (unklar ob Umsatz oder Provision; unklar ob … (2026) | – | Possible but weak evidence | CLAIMED | [Link](https://lgsagency.substack.com/p/i-had-an-amazon-storefront-for-years) |
| B03 | Instagram-Repost-Theme-Page mit Amazon-Links (Reddit) | faceless Theme-Page (Repost/Kuratierung) | Instagram Reels -> Amazon Associates | ~3.000 Follower; 2 virale Reels mit 2,5 Mio. + 11,9 Mio. Views; sonst 2–3k Views/Post | 45 $ Amazon-Provision (3–4 Monate) | ~3,1 $ pro 1 Mio. Views | Plausible | CLAIMED | [Link](https://www.reddit.com/r/AffiliateMarket/comments/1l67bcn/feeling_lost_after_earning_my_first_45_from/) |
| B04 | Pinterest-Konto Food/Home mit Amazon-Links (Reddit) | faceless Pinterest-Konto | Pinterest -> Amazon Associates | 12 Mio. Impressions; 186,5k Saves; 435 Outbound-Klicks | 4 $ Provision (4 Monate) | ~0,33 $ pro 1 Mio. Impressions | Plausible | CLAIMED | [Link](https://www.reddit.com/r/AffiliateMarket/comments/1s9ljyd/low_pinterest_click_rates/) |
| B05 | Pinterest Mode-Pins mit Amazon-Links (Reddit) | faceless Pinterest-Konto | Pinterest -> Shopify-Landingpage -> Amazon | 'thousands of views', keine Outbound-Klicks | 0,80 $ gesamt (~3 Monate (ab 11/2024)) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/AffiliateMarket/comments/1nusbch/amazon_affiliate_marketing_through_pinterest/) |
| B06 | Amazon.ca Storefront Klicks vs. Provision (r/Amazon_Influencer) | unklar (Review-Videos) | Amazon Storefront (CA) | 751 Klicks (Sep 2024–Jan 2025) | 167,51 $ Provision in 5 Monaten (09/2024–01/2025) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/Amazon_Influencer/comments/1iwfn9l/amazon_canadian_storefront/) |
| B07 | Amazon-Associates via TikTok/IG Reels (Reddit, 'iTraky'-Posts) | unklar (Gadget-Videos) | TikTok + IG Reels -> Amazon | CTR top Videos 8% -> 14–16% | 400–500 $/Monat -> 850–950 €/Monat (Parallelpost: 600 -> 1.100 $) (2025/26) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/Affiliatemarketing/comments/1qj5ioo/how_i_doubled_my_amazon_affiliate_commissions/) |
| B08 | Multi-Plattform-Test Social-Affiliate (Reddit 2026) | faceless/unklar | TikTok, IG, Pinterest, YT Shorts -> Landingp… | 6 Monate: TikTok 2.100 Follower/~800 Klicks; IG 1.400/~300; Pinterest 900/~1.200; Shorts … | ~400–600 $/Monat Affiliate-Umsatz aus ~2.500 Social-Besuchen/Monat (CR ~2,3%) (6–8 Monate) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/Affiliatemarketing/comments/1qgvlgu/building_social_media_audiences_for_affiliate/) |
| B09 | Faceless TikTok (Voiceover) Kaffee-Nische, Amazon (Reddit) | faceless (Voiceover) | TikTok -> Amazon Associates | ~60 Videos, meist 200–400 Views; 1 Video 47k Views -> ~15 Klicks -> 0 Verkäufe | erste Provision 8,47 $ nach 4 Monaten (4 Monate) | 0 $ für das 47k-View-Video | Plausible | CLAIMED | [Link](https://www.reddit.com/r/Affiliatemarketing/comments/1r84c5r/got_my_first_affiliate_commission_after_4_months/) |
| B10 | Faceless YouTube (Text-to-Speech) Amazon-Reviews (Reddit 2023) | faceless (TTS) | YouTube -> Amazon | ~12.000 Views -> 1.500 Link-Klicks -> 7 Verkäufe | ~9 $ Provision (wenige Tage) | ~750 $ pro 1 Mio. Views | Plausible | CLAIMED | [Link](https://www.reddit.com/r/Affiliatemarketing/comments/1040ttu/youtube_12000_views_1500_clicks_only_7_sold/) |
| B11 | Faceless Tech-YouTube-Kanal Monate 1–3 (r/juststart 2022) | faceless | YouTube (Long-Form) -> Amazon | 41.275 Views, 243 Abos (3 Monate) | 36,68 $ Amazon-Provision (3 Monate (2022)) | ~889 $ pro 1 Mio. Views | Plausible | CLAIMED | [Link](https://www.reddit.com/r/juststart/comments/w1th77/faceless_tech_youtube_channel_month_3/) |
| B12 | Amazon Associates effektive Rate (Website-Affiliate, Reddit 04/2026) | Website (kein Social) | Blog -> Amazon | – | ~16.000 $ vermittelter Umsatz -> ~400 $ Provision; Klage über Senkung 'near 10% to around 3%' + Scope-Änderung April 2026 (2026) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/Affiliatemarketing/comments/1sadlbu/worrying_amazon_associates_update/) |
| B13 | 'State of the Amazon Influencer Program July 2026' (Reddit-Profilpost) | – | Amazon Influencer / Meta | – | Behauptet: seit 14.04.2026 Onsite-Provision nur auf exakte ASIN; Mai-2026-Satzkürzungen unbestätigt; Meta-IG/FB-Affiliate-Partnerschaft mit… (07/2026) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/u_MilesInsights/comments/1um3o54/state_of_the_amazon_influencer_program_july_2026/) |
| B14 | Amazon-Onsite-Videos faceless, erste 30 Tage (r/Amazon_Influencer 202… | faceless (Person ohne Gesicht) | Amazon Onsite-Videos (kein Social-Traffic) | 145 Videos; 1.050 Views; 398 Klicks; 54 versandte Artikel | 34 $ (30 Tage (2026)) | ~32.400 $ pro 1 Mio. ONSITE-Views (Kaufabsicht!) | Plausible | CLAIMED | [Link](https://www.reddit.com/r/Amazon_Influencer/comments/1rmzspz/first_30_days_checkin/) |
| B15 | Jewel Tolentino (eBiz Facts) | faceless (95% nur Hände+Stimme) | Amazon Onsite-Videos | 800 Videos im 1. Jahr | 14.331 $ im 1. Jahr (~1.200 $/Monat) (1. Jahr) | – | Plausible | CLAIMED | [Link](https://ebizfacts.com/jewel-tolentino-amazon-influencer-video-reviews-14k-first-year/) |
| B16 | Trevin Peterson (eBiz Facts, 09/2026) | faceless möglich ('no face required') | Amazon Onsite-Videos | – | 12.000 $ in 30 Tagen, davon nur 2.000 $ Standardprovision, Rest Creator Connections (Brand-Kampagnen) (30 Tage (2026)) | – | Possible but weak evidence | CLAIMED | [Link](https://ebizfacts.com/trevin-peterson-amazon-influencer-10k-month-video-reviews/) |
| B17 | John Muscarello (eBiz Facts, 09/2026) | unklar | Amazon Onsite-Videos | ~5.000 Videos | 27k $ und 35k $ Umsatz in jüngsten Monaten; nach Amazon-Satzkürzung (April) nur noch Brand-Kampagnen (≥10% vs. üblich 1–3%); kauft 70–100 P… (2026) | – | Possible but weak evidence | CLAIMED | [Link](https://ebizfacts.com/john-muscarello-amazon-influencer-30k-month-product-research/) |
| B18 | Andreea Matei (eBiz Facts, 02/2026) | Person | Amazon Onsite-Videos | 3.500 Videos | 181k $ kumuliert; 5–6k $/Monat (~2k Standard, ~4k Creator Connections, ~0,5k Brand Deals) (2022–2026) | – | Plausible | CLAIMED | [Link](https://ebizfacts.com/andreea-matei-amazon-influencer-5k-month-product-review-videos/) |
| B19 | Fortune 2023: Brooke JuLyn / UnderCurrent | Person | Amazon Inspire/Influencer | – | 5.000–50.000 $/Monat (Provisionen+Tools+Brand Deals; 'Fortune did not verify'); Top-Influencer der Agentur >1 Mio. $/Jahr Amazon-Provision;… (2023) | – | Possible but weak evidence | CLAIMED | [Link](https://www.fortune.com/2023/06/27/amazon-platform-attracting-creators-commerce-content-commissions-shopping) |
| B20 | Amazon PR: Amanda Heiser | Person | Amazon Influencer | – | 7 $ im 1. Monat (2020) -> 2023 ein Monatseinkommen = früheres Vollzeitgehalt (2020–2025) | – | Possible but weak evidence | CLAIMED | [Link](https://www.aboutamazon.com/news/retail/how-amazon-influencer-program-works) |
| B21 | Jared Bauman (eBiz Facts) | faceless möglich ('don't even have to s… | Amazon Onsite-Videos (Social-Konto nur für Z… | 1.200 Videos im 1. Jahr | 40.000 $ in 12 Monaten (~3.300 $/Monat) (1. Jahr) | – | Plausible | CLAIMED | [Link](https://ebizfacts.com/jared-bauman-amazon-influencer-program-40k-year-1/) |
| B22 | Hella Bella (eBiz Facts) | unklar | Amazon Onsite-Videos | 75 Videos im 1. Monat | 968 $ im 1. Monat (09/2024) | – | Plausible | CLAIMED | [Link](https://ebizfacts.com/hella-bella-amazon-influencer-968-first-month/) |
| B23 | Amazon-Influencer 2,5 Jahre Rückblick (r/Amazon_Influencer 01/2025) | unklar | Amazon Onsite-Videos | +600 Videos in 2024 | 2024 erstmals weniger Einkommen als Vorjahr trotz 600 zusätzlicher Videos; Ursachen: Video-Sättigung, Amazon-Platzierungsexperimente (2022–2024) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/Amazon_Influencer/comments/1i02yg2/my_experience_being_in_the_amazon_influencer/) |
| **C – TikTok Shop** | | | | | | | | | |
| C01 | electricfinger0: KI-Video Supplement (Kalodata-Schätzung) | AI-Page (faceless) | TikTok Shop | 11k Follower; >5 Mio. Views in ~3 Monaten | Kalodata: 77,7k $ in 30 Tagen (Text nennt 'commissions', Rechnung deutet auf GMV); Kurator: >270k $ gesamt; bei 30% Provision ~1.000 $/Tag (~3 Monate (bis 03/2025)) | ~16.000 $ pro 1 Mio. Views (Annahme) | Possible but weak evidence | THIRD-PARTY ESTIMATE | [Link](https://ebizfacts.com/tiktok-affiliate-marketing-electricfinger0-viral-video/) |
| C02 | David Margaryan: faceless KI-TikTok-Shop-Clips | AI-Page (mehrere Konten, VA) | TikTok Shop | 15–20 Clips/Tag über mehrere Konten | 'one client account hit $14K in its first 30 days' (GMV vs. Provision unklar) (30 Tage (2026)) | – | Possible but weak evidence | CLAIMED | [Link](https://ebizfacts.com/14k-30-days-faceless-ai-tiktok-shop-affiliate-videos/) |
| C03 | colesdeals (TikTok Shop, Reddit 12/2025) | Deal-Page (teils vor der Kamera) | TikTok Shop | 1 Video ~5 Mio. Views (Black Friday) | ~15.000 $ GMV in 1 Woche; 2.500–3.000 $ Provision – danach Sperre wegen 'unoriginal content', ~3.000 $ Provision eingefroren (1 Woche (11/2025)) | ~500–600 $ pro 1 Mio. Views | Plausible | CLAIMED | [Link](https://www.reddit.com/r/TikTokshop/comments/1pqbx8j/tiktok_shop_banned_my_account_and_locked_3000_in/) |
| C04 | Yandi Latino (Ranking, eBiz Facts 07/2026) | Person (Livestreams) | TikTok Shop | 12,3k Follower | 1,16 Mio. $ GMV im März 2026; bei ~13% ≈ 150k $ Provision (03/2026) | – | Possible but weak evidence | THIRD-PARTY ESTIMATE | [Link](https://ebizfacts.com/yandi-latino-tiktok-shop-1m-month-12k-followers/) |
| C05 | 'Shop with Brooke' Projektor-Video (Schätzung) | Person | TikTok Shop | 1 Video 21 Mio. Views; ~15k Follower | Schätzung 432.880 $ Umsatz in 7 Tagen (YouTuber-Tool-Schätzung); bei 5% ≈ 20k $/Woche (7 Tage (2024/25)) | – | Possible but weak evidence | THIRD-PARTY ESTIMATE | [Link](https://ebizfacts.com/shop-with-brooke-tiktok-ugc-affiliate-marketing-50k-month/) |
| C06 | UK-Creatorin (Reddit 05/2026) | Person | TikTok Shop | Affiliate-Videos 500k + 30k Views; organisches Video 6,5 Mio. | ~10.000 £ GMV im Mai (bis dato), inkl. Livestreams (1 Monat) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/TikTokshop/comments/1toxgzs/best_agencies_to_level_up_with/) |
| C07 | TikTok-Shop-Neuling (Reddit 09/2026) | unklar | TikTok Shop | Videos 500–1.000 Views | 2 Verkäufe, 4,40 $ Provision (~1 Monat) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/TikTokshop/comments/1w7qlfg/what_am_i_doing_wrong/) |
| C08 | Brand-Owner: Reichweiten-Drosselung getaggter Affiliate-Videos (Reddi… | – (Markensicht) | TikTok Shop | Test: getaggtes Video ~800 Views vs. ungetaggtes ~10× mehr | Shop ~400k $ Umsatz 01/2025–01/2026; seit 01/2026 Affiliate-Reichweite nur mit GMV-Max/Ads (2025–2026) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/TikTokshop/comments/1ugrszw/if_youre_a_tiktok_shop_affiliate_getting_low/) |
| C09 | Brand: 50 Samples, 2 Verkäufe (Reddit 02/2026) | – (Markensicht) | TikTok Shop | die meisten Affiliate-Videos 0 Views | 2 Verkäufe gesamt (2026) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/TikTokshop/comments/1r7h6jy/50_samples_sent_2_sales_total_is_tiktok_shop_just/) |
| C10 | Faceless TikTok-Shop-Konto (Reddit 07/2026, rückblickend) | faceless | TikTok Shop | – | 'made like $600' (gesamt) (~2024) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/TikTokshop/comments/1v7p0ew/is_tiktok_shop_still_worth_it_in_2026/) |
| **D – faceless / Theme- / AI-Pages** | | | | | | | | | |
| D01 | Herrenmode-Theme-Page (Pinterest-Fotos) + eigene Affiliate-Seite (Red… | faceless Theme-Page | Instagram Reels -> eigene Website -> ASOS/Za… | 2 Reels >1 Mio. Views, je ~4k neue Follower | 200+ Bestellungen, AOV 60 €, 10–15% -> ~1.200–1.800 € Provision ('first months') | ≤ ~600–900 € pro 1 Mio. Views (Obergrenze) | Plausible | CLAIMED | [Link](https://www.reddit.com/r/InstagramMarketing/comments/1fza89h/how_i_started_my_theme_page_on_instagram_and/) |
| D02 | 'CordBrick' Lifestyle-Theme-Page (u/optimizever, 2 Posts) | faceless Theme-Page (UGC vom Programm) | Instagram Reels -> Bio-Link -> Affiliate | keine Views genannt | 'just over $7K in affiliate commissions in 2 months' (2,4k in 3 Wochen); Parallelpost '$20–50/day' (2 Monate (2025)) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/InstagramMarketing/comments/1lgw22h/how_i_made_7000_in_60_days_with_a_physical/) |
| D03 | Faceless KI-Videos, '1M monthly views' (Reddit 11/2025) | AI-Page (faceless) | Instagram/Short-Form -> Affiliate-Produkt | ~1 Mio. Views/Monat | 'minimum of $1000 every month' Provisionen (~6 Monate) | ~1.000 $ pro 1 Mio. Views | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/digitalproductselling/comments/1onn49i/i_generated_1m_monthly_views_organically_through/) |
| D04 | Esther Luvv: Portfolio faceless IG-Pages (eBiz Facts) | faceless Theme-Pages (Comedy/Model), me… | Instagram | mehrere Pages | ~4.000 $/Monat 'passive profit' aus Story-Promotions, Affiliate-Deals, Account-Flips (2025) | – | Possible but weak evidence | CLAIMED | [Link](https://ebizfacts.com/esther-luvv-4k-month-passive-income-instagram/) |
| D05 | Basem Kamal: Theme-Page-Portfolio (WifiMoolah) | faceless Theme-Pages (mehrere) | Instagram | – | 16.045 $ in 60 Tagen (Portfolio; Shoutouts/Deals/Affiliate gemischt) (60 Tage) | – | Possible but weak evidence | CLAIMED | [Link](https://wifimoolah.com/p/idea-53) |
| D06 | WifiMoolah Follower-Stufen | faceless Theme-Page (generisch) | Instagram | 100k+ / 500k+ Follower | '500K+ followers can generate $10,000–25,000/month'; 100k+: 5–15k $/Monat (v.a. Shoutouts/Sponsoring); Affiliate nur bei 1–5k Follower '50–… (–) | – | No credible evidence | UNKNOWN | [Link](https://wifimoolah.com/p/idea-53) |
| D07 | faceless.my Umsatz-Schätzungen Top-Pages | faceless Theme-Pages | Instagram | z.B. @wealth 15 Mio.; @travly 212k | @wealth 80–200k $/Monat; @travly 0,5–2k $/Monat (modelliert: Follower × Sponsoring-Rate × Deals + Affiliate) (05/2026) | – | No credible evidence | THIRD-PARTY ESTIMATE | [Link](https://faceless.my/instagram/top-faceless-instagram-pages/) |
| D08 | Medium 'Faceless Instagram Theme Pages: $5K/Month Formula (2026)' | faceless Theme-Page | Instagram | 127k Follower in 4 Monaten (Reise) | lt. Such-Snippet 2,3k $/Monat (Shoutouts + Affiliate) (–) | – | No credible evidence | UNKNOWN | [Link](https://medium.com/write-a-catalyst/faceless-instagram-theme-pages-5k-month-formula-2026-5fbd3037ef3c) |
| D09 | CreatorFlow Modellrechnung Haul-Reel | faceless/generisch | Instagram Reels -> DM-Link -> Amazon | 300 Link-Anfragen | 5 Käufe -> 9 $ Provision bei 4% (explizit hypothetisch) (–) | – | No credible evidence | UNKNOWN | [Link](https://creatorflow.so/blog/amazon-influencer-scale-instagram-commissions/) |
| D10 | 'Brainrot'-Faceless-Page mit ManyChat (Reddit 2025) | faceless Theme-Page | Instagram Reels | 20k Views/Video, einzelne 50–500k | Sponsoring bis 5k $/Monat; danach eigener Digital-Guide – KEIN Affiliate (2025) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/socialmedia/comments/1mmi4js/how_i_growth_hacked_instagram_update/) |
| D11 | Liam James Kay: bezahlte IG-Shoutouts für Affiliate-Produkte | faceless/Shoutout-Einkauf | Instagram | – | 22 $ Gewinn nach 3 Tagen Test (3 Tage (2023)) | – | Possible but weak evidence | CLAIMED | [Link](https://ebizfacts.com/liam-james-kay-paying-instagram-influencers-to-promote-affiliate-products/) |
| D12 | KI-Influencerin Dating-Nische (Reddit 04/2026) | AI-Page (Avatar) | Instagram/TikTok | von 0 in 4 Monaten | 'nearly $80K' (Mix unklar); Autor selbst: TikTok 2.100 Follower, Affiliate + TikTok Shop (12/2025–03/2026) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/DigitalIncomePath/comments/1skcsbk/can_this_make_money_ai_influencers_77k_in_4_months/) |
| D13 | KI-Influencerin 33k Follower (Reddit 07/2026) | AI-Page (Avatar) | Instagram Reels | 33k Follower; Reels 5k–150k Views, max. 2,5 Mio. | 700 $ (Abos/Fans) + 529 $ wiederkehrende Affiliate-Einnahmen (2026) | – | Possible but weak evidence | CLAIMED | [Link](https://www.reddit.com/r/DigitalIncomePath/comments/1uozy8m/700_from_just_17_subs_and_32_fans_529_in/) |
| D14 | Theme-Page-Gründer nach 1 Jahr (Reddit r/Vent 02/2026) | faceless Theme-Pages | Instagram | 'daily posting high quality reels ... to 500 followers max' | ~0 $ (1–2 Jahre) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/Vent/comments/1r9cm0d/online_businesses_are_impossible/) |
| D15 | Kaml Abdel-Kader: faceless IG für eigene Apps (Vergleich, KEIN Affili… | faceless (Demos) | Instagram Reels | 150 Mio.+ Views gesamt; 1 Video ~3 Mio. Views -> ~10k Downloads | ~10.000 $/Monat Peak (eigene Apps) (Peak) | – | Possible but weak evidence | CLAIMED | [Link](https://ebizfacts.com/kaml-abdel-kader-9-apps-instagram-reels-10k-month/) |
| **E – Marktplätze** | | | | | | | | | |
| E01 | Flippa VERKAUFT: 'Style by Sanne' Fashion-IG | unklar (Personenmarke möglich) | Instagram | 347k Follower | ~1.805 $/Monat Umsatz; ~1.670 $ (≈1.420 €) Gewinn/Monat aus Affiliate + Brand-Kooperationen; Verkaufspreis 13.700 $ (Verkauf 2025/26) | – | Possible but weak evidence | CLAIMED | [Link](https://flippa.com/12292926) |
| E02 | Flippa VERKAUFT: Personal-Finance Multi-Plattform | faceless/unklar | IG+FB+TikTok+Threads | 18k Follower kombiniert | 42 $/Monat (Affiliate); Verkaufspreis 947 $ (2025/26) | – | Possible but weak evidence | CLAIMED | [Link](https://flippa.com/13049678) |
| E03 | Flippa VERKAUFT: ListBuzz (IG 115k + TikTok 62k) | faceless Theme-Page | Instagram+TikTok | 177k Follower gesamt | 0 $/Monat (Affiliate-Kategorie); Verkaufspreis 1.500 $ (2025/26) | – | Plausible | CLAIMED | [Link](https://flippa.com/13733914) |
| E04 | Flippa VERKAUFT: Wild-Food-IG | faceless Theme-Page | Instagram | 187k Follower; Videos mit 58 Mio.+ Views | 0 $/Monat; Verkaufspreis 1.709 $ (2025/26) | 0 $ | Plausible | CLAIMED | [Link](https://flippa.com/13553549) |
| E05 | Flippa ANGEBOT: 'Backstage Shorts' BTS/VFX-IG | faceless Theme-Page | Instagram | 254k Follower; 144 Mio.+ Views in 55 Tagen (Ø 771k Views/Post) | 2 $/Monat Gewinn (Monetarisierung 'Other'); Preis 2.549 $ (55 Tage (2026)) | ~0,03 $ pro 1 Mio. Views (gesamt, nicht nur Affiliate) | Plausible | CLAIMED | [Link](https://flippa.com/13921895) |
| E06 | Flippa ANGEBOT: Travels2Rome | faceless Theme-Page | Instagram | 160k Follower | ~1.300 $ ARR (Restaurant-Abos; Kategorie 'Affiliate Sales'); Gewinn 95 $/Monat; Preis 600 $ (2026) | – | Plausible | CLAIMED | [Link](https://flippa.com/13414294) |
| E07 | Flippa ANGEBOT: Curly-Hair-IG | faceless Theme-Page | Instagram | 127k Follower; Reel mit 4 Mio.+ Views | 0 $/Monat (Affiliate-Kategorie); Preis 4.999 $ (2026) | – | Plausible | CLAIMED | [Link](https://flippa.com/13088512) |
| E08 | Flippa ANGEBOT: TikTok @patrickgalugu1 | Person (Namenskonto) | TikTok Shop + Affiliate + Brand Deals | 272,2k Follower | Ø 5.089 $ Umsatz/Monat (Titel: 5,6k $), 4.289 $ Gewinn/Monat; Preis 12.000 $ (2025/26) | – | Possible but weak evidence | CLAIMED | [Link](https://flippa.com/12755755) |
| E09 | Flippa ANGEBOT: Moto-TikTok (Vergleich, nicht Affiliate) | faceless/unklar | TikTok | 671k Follower; 14 Mio. Views/Monat | 9.973 $ in 4 Monaten (Monetarisierung 'Other', vermutl. Creator Rewards) (4 Monate) | ~178 $ pro 1 Mio. Views (nicht Affiliate) | Possible but weak evidence | CLAIMED | [Link](https://flippa.com/13673243) |
| E10 | Reddit-Verkaufsangebot 65k Ocean-Page | faceless Theme-Page | Instagram | 65k Follower; einzelne Reels 22 Mio.+ Views | Preis 60–80 $ (08/2025) | – | Plausible | CLAIMED | [Link](https://www.reddit.com/r/InstagramMarketing/comments/1n1dsom/65k_instagram_page_for_sēll_ocean_niche/) |
| E11 | Fameswap Marktplatz-Check | – | Fameswap | Browse-Filter nur YouTube/TikTok/Twitter/Websites; keine Instagram-Listings sichtbar; Det… | keine Umsatzdaten abrufbar (Stand 2026-09-26) | – | Observed | VERIFIED | [Link](https://fameswap.com/browse-theme-pages-for-sale) |

---

## 3. Case Studies (vertieft)

### CS1 – Neues faceless Instagram-Konto → Amazon Storefront (B01): der beste faceless IG-Datensatz
- **Setup:** Ein ruhendes IG-Konto wurde reaktiviert. Inhalt: „affordable home finds“, faceless (einmal Seitenprofil gezeigt). 61 Inhalte in 48 Tagen, 216 → 3.084 Follower, mehrere Reels > 100k Views.
- **Zahlen (Mai 2026):**
  - 11.232 Storefront-Klicks → 571 Bestellungen
  - 13.145,50 $ versandter Umsatz → **531,16 $ Provision**
  - gesamt 789,63 $ in 48 Tagen, inkl. Creator-Rewards-Boni (90 $), Creator-Connections-Bonus (18,47 $) und eines Brand-Deals (150 $)
- **Abgeleitet:** EPC ≈ **0,047 $/Klick**, AOV ≈ 23 $, effektiver Provisionssatz ≈ 4,0 %.
- **Hochrechnung (nur Arithmetik, keine Evidenz):** 6.000 $ Provision/Monat bräuchten bei diesem EPC **~127.000 Storefront-Klicks pro Monat**, also das ~11-Fache.
- **Bewertung:** *Plausible / CLAIMED*. Detaillierte, in sich konsistente Zahlen, aber eine Agentur mit bezahltem Newsletter ist Autorin. Die Gesamt-Views fehlen, daher ist kein Wert pro 1 Mio. Views berechenbar.
- Die Kunden-Claims derselben Autorin („36.000 $/Monat“, „>100.000 $/Monat“, B02) sind **mehrdeutig**: Umsatz oder Provision? Social oder Onsite? Deshalb nur *Possible but weak*.

### CS2 – Instagram-Repost-Theme-Page: 14,4 Mio. Views → 45 $ (B03)
- Kuratierte Reposts, ~3.000 Follower, zwei virale Reels mit 2,5 Mio. und 11,9 Mio. Views. **45 $ Amazon-Provision über 3–4 Monate** → **≈ 3,1 $ pro 1 Mio. Views**.
- Zusätzlich: Programme mit höheren Provisionen lehnten den Betreiber ab, vermutlich weil er „nur kuratiert“.
- Das ist die **exakte Zielkonfiguration** der Studie (faceless, Repost/Theme, IG Reels, Amazon) und der klarste negative Datenpunkt.

### CS3 – Herrenmode-Theme-Page mit eigener Affiliate-Seite (D01)
- Reels aus Pinterest-Fotos, zwei Reels > 1 Mio. Views. Die Monetarisierung lief über eine **eigene Website** mit ASOS-, Zara- und H&M-Affiliate-Links.
- **200+ Bestellungen, AOV 60 €, 10–15 %** → ≈ 1.200–1.800 € Provision in den „ersten Monaten“ → **≤ 600–900 € pro 1 Mio. Views** (Obergrenze, da die Gesamt-Views über 2 Mio. lagen).
- Zeigt: Eine Mode-Nische mit hohem AOV, höheren Sätzen als Amazon und eine eigene Zwischenseite heben den Ertrag pro View um zwei Größenordnungen gegenüber CS2. Die absolute Summe bleibt trotzdem vierstellig.

### CS4 – TikTok-Shop-Deal-Account: 5 Mio. Views → 2,5–3k $ in einer Woche → Sperre (C03)
- Ein Black-Friday-Video mit ~5 Mio. Views brachte **~15.000 $ GMV** und **2.500–3.000 $ Provision** in einer Woche → **≈ 500–600 $ pro 1 Mio. Views** (Annahme: Das Wochen-GMV stammt überwiegend aus diesem Video).
- Danach folgte eine **Sperre wegen „unoriginal content“**, ausgelöst durch die mehrfache Nutzung der TikTok-Funktion „delete & re-edit“. **~3.000 $ Provision wurden eingefroren.**
- Relevanz: Die In-App-Checkout-Strecke konvertiert um Größenordnungen besser als Instagram → Bio-Link → Amazon. Für KI- und Repost-Pages ist aber genau das **Originalitäts- und Sperr-Risiko** zentral.

### CS5 – KI-generiertes Supplement-Video auf TikTok Shop (C01): der Ausreißer
- Das Konto hat 11k Follower; das Video > 5 Mio. Views in ~3 Monaten.
- Kalodata-Schätzung: 77,7k $ in 30 Tagen. Der Text sagt „commissions“, die Folgerechnung des Kurators behandelt den Wert aber als Umsatz.
- Kurator-Hochrechnung: > 270k $ gesamt; bei 30 % Provision „~1.000 $/Tag“.
- **Abgeleitet (Annahme: 270k $ = GMV, 30 % Provision):** ≈ 54.000 $ GMV bzw. **≈ 16.200 $ Provision pro 1 Mio. Views**.
- **Bewertung:** *Possible but weak / THIRD-PARTY ESTIMATE*.
  - Keine Creator-Bestätigung.
  - Health-Claims-Nische (Männer-Supplement), also Compliance-Risiko.
  - Werbeverstärkung durch die Marke ist nicht ausgeschlossen (vgl. C02, C08).
- Derselbe Kurator hält ausdrücklich fest, dass er für den Podcast-Claim „100k $/Tag mit faceless KI-TikTok-Konten“ **keine Belege** fand.

### CS6 – Marktplatzrealität: Views ≠ Umsatz, Theme-Pages sind billig (E01–E11)
- **Flippa, verkauft:**
  - Fashion-IG (347k Follower, Affiliate + Brand-Kooperationen, ~1.420 €/Monat Gewinn): 13.700 $, also ≈ 8 Monatsgewinne (E01)
  - Wild-Food-IG (187k Follower, 58 Mio.+ Views): **0 $ Umsatz**, verkauft für 1.709 $ (E04)
  - ListBuzz (177k Follower, Affiliate-Kategorie): 0 $ Umsatz, 1.500 $ (E03)
- **Flippa, offen:** BTS/VFX-IG mit **144 Mio. Views in 55 Tagen** (~78 Mio./Monat) weist **2 $/Monat Gewinn** aus (E05).
- **Reddit:** 65k-Ozean-Page mit Reels bis 22 Mio. Views wird für **60–80 $** angeboten (E10).
- **Fameswap** listet (Stand 26.09.2026) **keine Instagram-Konten** sichtbar, nur YouTube, TikTok, Twitter und Websites (E11).
- Fazit: Der Markt preist faceless Theme-Pages mit Millionen-Reichweite fast wie wertlos ein. Das spricht gegen verbreitete hohe Affiliate-Erträge.

### CS7 – Kontrast: Amazon-Onsite-Videos (B14–B18)
- Faceless-freundliche **Amazon-Onsite-Reviewvideos** erreichen ≈ **32.400 $ pro 1 Mio. Onsite-Views**. Datenbasis: 1.050 Views → 34 $ in 30 Tagen (B14). Grund ist die maximale Kaufabsicht der Zuschauer auf der Produktseite.
- Top-Beispiele erreichen 5–35k $/Monat (B16–B18). Ein großer Teil stammt aber aus **Creator Connections (Brand-Kampagnen)**, nicht aus Standardprovision: bei Trevin Peterson nur 2k von 12k $ (B16). Zudem werden **Satzkürzungen und Scope-Änderungen 2026** berichtet (B12, B13, B17).
- **Kein Social-Media-Theme-Page-Modell**, aber es belegt den Mechanismus: Der Ertrag pro View hängt an der Kaufabsicht, nicht am Gesicht.

---

## 4. Abgeleitete Spanne: Affiliate-Provision pro 1 Mio. Views

> **Warnung zur Datenqualität:** Alle Werte beruhen auf **Einzelfällen (n = 1 je Zeile), fast alle CLAIMED**, teils mit Annahmen. Es gibt keine repräsentative Stichprobe. Die Spanne eignet sich nur als **Größenordnungs-Kompass**, nicht als Prognose.

| Plattform / Content-Typ | Nische / Ziel | Datenpunkt(e) | $ pro 1 Mio. Views | Qualität |
|---|---|---|---|---|
| Instagram Reels, **faceless Repost-/Theme-Page** → Bio-Link → Amazon | gemischt/Trend | B03 | **≈ 3 $** | CLAIMED, *Plausible* |
| Instagram, faceless Unterhaltungs-Page (Monetarisierung gesamt, nicht nur Affiliate) | BTS/VFX, Food | E05, E04 | **≈ 0,03 $ bzw. 0 $** | CLAIMED (Verkäufer) |
| Pinterest (pro 1 Mio. **Impressions**) → Amazon | Food/Home | B04 (B05: 0,80 $ gesamt) | **≈ 0,33 $** | CLAIMED |
| TikTok → Bio-Link → Amazon, faceless Voiceover | Kaffee | B09 (47k Views → 15 Klicks → 0 Sales) | **0 $** (Einzelvideo) | CLAIMED |
| Instagram, **faceless Mode-Theme-Page** → eigene Seite → Mode-Händler | Herrenmode | D01 | **≤ 600–900 €** (Obergrenze) | CLAIMED, *Plausible* |
| YouTube (faceless, TTS bzw. Long-Form) → Amazon | Amazon-Reviews / Tech | B10, B11 | **≈ 750–890 $** | CLAIMED, Kleinststichproben |
| TikTok Shop, **Deal-Account** (teils Kamera) | Deals/Black Friday | C03 | **≈ 500–600 $** | CLAIMED, *Plausible* |
| Faceless KI-Videos (Plattform unklar, IG erwähnt) | Produkt-Edu | D03 | **≈ 1.000 $** | CLAIMED, **Guide-Verkäufer** |
| TikTok Shop, **KI-Page**, Supplement (Ausreißer) | Männer-Health | C01 | **≈ 16.000 $** (Annahme 30 %) | THIRD-PARTY ESTIMATE |
| *Vergleich:* Amazon-Onsite-Video (kein Social-Traffic) | Haushalt | B14 | *≈ 32.400 $* | CLAIMED |
| *Vergleich:* TikTok ohne Affiliate (vermutlich Creator Rewards) | Motorrad | E09 | *≈ 178 $* | CLAIMED (Verkäufer) |

**Ergänzende Klick-Kennzahlen (ohne View-Bezug):**
- EPC (Provision pro Klick) Amazon via Social/Storefront: **0,047 $** (B01) bis **0,22 $** (B06). Multi-Plattform-Test: 0,16–0,24 $ pro Besuch (B08).
- Klickraten Views → Klick: 0,03 % (B09, TikTok Bio-Link), 0,0036 % (B04, Pinterest Outbound).
- Beispielrechnung (Annahme, keine Evidenz): Bei 0,01 % Klickrate und 0,05–0,22 $ EPC ergäben sich **5–22 $ pro 1 Mio. Views**. Das liegt nahe am beobachteten B03-Wert.

**Empirische Spanne für die Zielkonfiguration (faceless IG-Reels-Theme-Page mit Affiliate):**
- **Unterhaltungs-/Repost-Content: ~0–3 $ pro 1 Mio. Views.** Beobachtet an B03, E04 und E05; B09 und B04 zeigen dasselbe Muster.
- **Shopping-naher Content** (Finds, Deals, Mode mit Zwischenseite): **~500–900 $ pro 1 Mio. Views** (C03, D01, B10/B11; YouTube und TikTok Shop sind effizienter als IG → Amazon).
- **Oberhalb ~1.000 $** gibt es nur Guru-Claims (D03) bzw. Drittschätzungen mit Werbeverdacht (C01).

**Benötigte Views pro Monat für das Gewinnziel** (reine Arithmetik: Provisionsziel ÷ Wert pro 1 Mio. Views)

| $ pro 1 Mio. Views | 5k € (≈ 6k $) | 10k € (≈ 12k $) | 20k € (≈ 24k $) |
|---|---|---|---|
| 3 $ (B03, IG-Repost → Amazon) | ≈ 1,9 **Mrd.** | ≈ 3,8 Mrd. | ≈ 7,7 Mrd. |
| 0,33 $ pro Mio. Impr. (B04, Pinterest) | ≈ 18 Mrd. Impr. | ≈ 36 Mrd. | ≈ 72 Mrd. |
| 500–600 $ (C03, TikTok-Shop-Deal) | 10–12 Mio. | 20–24 Mio. | 40–48 Mio. |
| 600–900 € (D01, Obergrenze; €-Basis) | ≥ 5,6–8,3 Mio. | ≥ 11–17 Mio. | ≥ 22–33 Mio. |
| 750–890 $ (B10/B11, YouTube) | 6,7–8 Mio. | 13,5–16 Mio. | 27–32 Mio. |
| 1.000 $ (D03, Guru-Claim) | 6 Mio. | 12 Mio. | 24 Mio. |
| 16.200 $ (C01, Ausreißer-Schätzung) | 0,37 Mio. | 0,74 Mio. | 1,5 Mio. |

**Lesart:** Faceless Unterhaltungs-Pages erreichen solche View-Volumina durchaus (E05: ~78 Mio. Views pro Monat). Sie verdienen damit aber praktisch nichts. Shopping-Content verdient pro View etwa 150- bis 300-mal mehr, doch in dieser Content-Form gibt es **keinen belegten Fall** stabiler 10–50 Mio. Views pro Monat einer einzelnen faceless IG-Page.

---

## 5. Verteilung der Affiliate-Einnahmen (Studien und Plattform-Statistiken)

| Quelle | Kernaussage | Implikation für ≥ 5k / 10k / 20k $ pro Monat |
|---|---|---|
| IMH Affiliate Benchmark (A05, Umfrage, alle Kanäle) | 57,6 % < 10k $/Jahr; 3,8 % > 150k $/Jahr | ≥ 5k: **~12–17 %**; ≥ 10k: **~4–12 %**; ≥ 20k: **< 4 %**. Selbstselektierte Befragte inkl. SEO-Blogger, also eher zu optimistisch für Social |
| Mavely 2024 (A03) | 16 Mio. $ an > 85.000 Creator in 7 Monaten | **Ø ~27 $/Monat pro Creator** |
| TikTok Shop GMV-Perzentile (A09, unverifiziert) | Top 1 % Ø 600k $ GMV/Jahr | Bei 13 %: nur die **Top ~1 %** erreichen Ø ~6.500 $ Provision pro Monat; Top 5 % ~870 $; Top 20 % ~87 $ |
| Linktree 2022 (A06) | 12 % der Vollzeit-Creator > 50k $/Jahr, **alle** Einnahmequellen | Affiliate-only liegt deutlich darunter |
| Goldman Sachs 2023 (A07) | ~4 % der Creator > 100k $/Jahr | ≈ 8,3k $/Monat, alle Quellen |
| IMH/NeoReach 2025 (A08) | > 50 % < 15k $/Jahr | – |
| LTK (A01/A02) | > 130 bzw. „hunderte“ Millionäre (kumuliert) | Ausschließlich Personen-Creator; Median nicht veröffentlicht |

**Keine Quelle weist faceless Pages separat aus.** Alle Verteilungen mischen Personen-Creator (höheres Vertrauen) mit anderen Typen. Für faceless Theme-Pages sind die Anteile nach der Evidenzlage aus Abschnitt 4 und 7 **eher niedriger** anzusetzen. Das ist eine Schlussfolgerung, keine Messung.

---

## 6. Urteil je Zielgröße (eine faceless Page, nur Affiliate, **Gewinn** pro Monat)

| Ziel | Instagram Reels (Primärfokus) | TikTok Shop (sekundär) | **Gesamturteil** |
|---|---|---|---|
| **5.000 €** | *Possible but weak evidence* | *Possible but weak evidence* (nahe *Plausible*) | **Possible but weak evidence** |
| **10.000 €** | *No credible evidence* | *Possible but weak evidence* | **Possible but weak evidence** (nur über TikTok-Shop-Ausreißer) |
| **20.000 €** | *No credible evidence* | *Possible but weak evidence* (1 Drittschätzung) | **No credible evidence** (für nachhaltigen Monatsgewinn) |

**Begründung 5.000 €:**
- Belegte faceless IG-Werte reichen von **45 $ in 3–4 Monaten (B03)** bis **~1.000 $ pro Monat** (B01 inkl. Boni; D03 als Claim eines Guide-Verkäufers).
- Näher an 5k kommen nur folgende Fälle:
  - Fashion-IG auf Flippa mit ~1.420 €/Monat Gewinn aus Affiliate plus Brand-Deals; Faceless-Status unklar (E01)
  - CordBrick-Claim über ~3.500 $/Monat, Autor rekrutiert per DM (D02)
  - D01 als Einzelphase
- Auf TikTok Shop zeigen C03 (2,5–3k $ pro Woche, danach Sperre) und Flippa-Listings mit 2–5k $/Monat (E08, Personenkonto), dass **5k-Monate erreichbar sind**. Belegt ist das aber vor allem für Personen und Deal-Accounts, nicht für KI-Theme-Pages.
- Kein unabhängig verifizierter Fall.

**Begründung 10.000 €:**
- Für Instagram existieren nur pauschale Guru-Spannen: „100k+ Follower 5–15k $“ (D06), überwiegend aus Shoutouts und Sponsoring, nicht aus Affiliate. Dazu kommen modellierte Schätzungen (D07) und mehrdeutige Agentur-Claims (B02).
- Auf TikTok Shop gibt es einzelne Hinweise:
  - C02: „14k $ in 30 Tagen“ eines Kundenkontos, GMV oder Provision unklar, Kursanbieter
  - C01: Drittschätzung
  - Personen-Fälle C04 und C05
- Die Perzentil-Schätzung A09 verortet ≥ 10k $/Monat im Bereich **unter dem obersten Prozent**.

**Begründung 20.000 €:**
- Die einzigen Fälle ≥ 20k $/Monat sind:
  - **Personen**: Livestream-Seller C04, Projektor-Creatorin C05, LTK- und Amazon-Top-Creator
  - **Amazon-Onsite-Creator** ohne Social-Traffic, überwiegend Brand-Kampagnen (B17)
  - **ein KI-Supplement-Video** mit nur 30-Tage-Drittschätzung, unklarer GMV-/Provisionsbasis, möglicher Werbeverstärkung und Health-Compliance-Risiko (C01)
- Für einen **nachhaltigen Gewinn** einer einzelnen faceless Page gibt es keine glaubwürdige Evidenz.

---

## 7. Negativ-Evidenz und Ursachen

| # | Befund | Datenpunkte | Ursache |
|---|---|---|---|
| 1 | **Millionen Views → fast kein Umsatz** | B03 (14,4 Mio. → 45 $), E04 (58 Mio. → 0 $), E05 (144 Mio. in 55 Tagen → 2 $/Monat), B09 (47k → 0 Sales) | Unterhaltungs- und Repost-Views haben **keine Kaufabsicht**; Theme-Page-Publikum folgt dem Content, nicht der Empfehlung |
| 2 | **Pinterest liefert kaum Outbound-Klicks** | B04 (12 Mio. Impr. → 435 Klicks → 4 $), B05 (0,80 $); r/Pinterest-Test: „business of teaching … bigger than the business they're teaching“ | Inspiration statt Kauf; Outbound-CTR ≈ 0,004 % |
| 3 | **Link-Friction** | B07 (In-App-Browser nicht bei Amazon eingeloggt; Tool-Werbung-Verdacht), B09; TikTok-Bio-Link erst ab 1.000 Followern (lt. [Reddit](https://www.reddit.com/r/Affiliatemarketing/comments/1u19zgj/i_will_not_promote_built_a_niche_affiliate_site/) und [eBiz Facts](https://ebizfacts.com/sleazy-greetings-viral-on-tiktok-921k-views/)) | IG Reels: kein klickbarer Caption-Link; Umweg über Bio oder DM |
| 4 | **Niedrige und sinkende Amazon-Sätze, enge Attribution** | B12 (16k $ Umsatz → ~400 $ = 2,5 %), B01 (4,0 % effektiv), B17 („usual 1–3 %“, Kürzung April 2026), B13 (ASIN-only-Regel ab 14.04.2026, CLAIMED) | Kleine Warenkörbe (AOV ~23 $) × 3–4 % ≈ 1 $ pro Bestellung; kurzes Session-Fenster (24 h laut [Reddit-Guide](https://www.reddit.com/r/sidehustle/comments/1i90dp4/how_i_made_my_first_500_online_with_amazon/)) |
| 5 | **TikTok Shop: organische Affiliate-Reichweite gedrosselt, „Pay to Play“** | C08 (getaggtes Video 800 Views vs. ~10× ungetaggt), C09 (50 Samples → 2 Sales), C07 (4,40 $) | Plattform bevorzugt Videos mit GMV-Max-/Ad-Budget der Marke (Markensicht, nicht bewiesen) |
| 6 | **Sperren und eingefrorene Provisionen** | C03 (~3.000 $ gesperrt wegen „unoriginal content“) | Originalitätsregeln treffen Repost- und KI-Pages besonders |
| 7 | **Ablehnung durch bessere Programme** | B03 (Kurator-Page von höher vergütenden Programmen abgelehnt) | Programme bevorzugen eigene Inhalte bzw. echte Creator |
| 8 | **Faceless-Pages monetarisieren eher über Nicht-Affiliate** | D10 (Sponsoring bis 5k $, dann Digital-Guide), D04/D05 (Shoutouts, Flips; Portfolio), D15 (eigene Apps) | Affiliate ist bei diesen Pages die schwächste Einnahmequelle |
| 9 | **Marktbewertung nahe null** | E03, E04, E10 (65k-Page, 22 Mio.-Reels: 60–80 $), E11 (Fameswap ohne IG) | Käufer sehen keine verlässlichen Erträge; Kontoverkäufe widersprechen zudem Plattform-AGB |
| 10 | **Frust- und Abbruchberichte** | D14 (Theme-Pages nach 1 Jahr ≤ 500 Follower), B09, C07, [r/Affiliatemarketing „first commission $8.47“](https://www.reddit.com/r/Affiliatemarketing/comments/1r84c5r/got_my_first_affiliate_commission_after_4_months/) | Survivorship-Bias der Erfolgsgeschichten |
| 11 | **Guru-Claims ohne Belege** | eBiz Facts fand für „100k $/Tag faceless KI-TikTok“ keine Belege (C01-Quelle); Syncly: TikTok-Shop-Statistiken „recur nearly word-for-word … with no attributed survey or dataset“ | Kurs- und Tool-Verkauf als eigentliches Geschäftsmodell |

---

## 8. Abgrenzung der Account-Typen

| Typ | Evidenz für ≥ 5k $/Monat Affiliate | Kommentar |
|---|---|---|
| **Person (Gesicht, Vertrauen)** | **Observed auf Plattformebene** (LTK-Millionäre, Amazon-Top-Influencer, TikTok-Livestreamer) | Hohe Einnahmen sind real, aber an Persönlichkeit, Live-Verkauf und Brand-Kampagnen gekoppelt → **nicht übertragbar** |
| **Amazon-Onsite (faceless möglich)** | Plausible (B15–B18, B21) | Kein Social-Media-Modell; Traffic von Amazon; Anteil Brand-Kampagnen hoch; Sättigung (B23) und Kürzungen 2024–2026 |
| **Deal-Page** | Possible but weak (C03) | Beste Nicht-Personen-Konversion, aber volatil (Einzelviralität, Black Friday) und sperranfällig |
| **faceless Theme-Page** | **Keine glaubwürdige Evidenz ≥ 5k** | Belegte Werte 0–~1.000 $/Monat; Theme-Content hat geringe Kaufabsicht |
| **AI-Page** | Possible but weak (C01, C02, D03, D12) | Nur Drittschätzungen und Claims mit Verkaufsinteresse; KI-Influencer verdienen oft über Fan-Abos statt Affiliate (D13) |

---

## 9. Datenlücken

1. **Keine unabhängig verifizierten Dashboards** (z. B. Screenshot in seriöser Presse) für eine faceless Theme-Page mit ≥ 5k Affiliate/Monat gefunden. Business Insider, das solche Fälle häufig bringt, war technisch nicht abrufbar; die dortigen Fälle betreffen überwiegend Personen.
2. **Suchbeschränkung:** Das Websuche-Budget war früh erschöpft. Reddit war nur über die RSS-Suche erreichbar (Snapshot des Post-Texts, ohne Screenshots und Kommentare). Die Abdeckung ist daher **nicht vollständig**.
3. **Keine DACH- bzw. Amazon.de-Social-Daten** zu faceless Pages. Einzige EU-Datenpunkte sind D01 (€), B07 (ES) und E01 (NL). Awin-, Impact- und Rakuten-Creator-Studien mit Einkommensverteilung wurden nicht gefunden.
4. **Geniuslink- und ManyChat-Fallstudien** mit Umsatzangaben wurden nicht abgerufen, weil keine URL auffindbar war. **Starter Story / Indie Hackers**: kein passender Fall erreichbar.
5. **TikTok-Shop-GPM** (GMV pro 1.000 Views) ist ohne Primärquelle. Perzentil-Zahlen (A09) stammen von einem Anbieter ohne offengelegte Methodik.
6. **Marktplatz-Finanzdaten** liegen bei Flippa und Fameswap hinter Login; SocialTradia war blockiert. Die Flippa-Werte sind unverifizierte Verkäuferangaben.
7. **Plattformregeln 2026** (Amazon-Scope- und Satzänderungen, Meta-Amazon-Affiliate-Partnerschaft, TikTok-Affiliate-Drosselung) sind nur als CLAIMED erfasst und sollten in Modul G (Policy) gegengeprüft werden.
8. **LTK, ShopMy und Mavely** veröffentlichen keine Mediane oder Verteilungen nach Account-Typ.
9. Keine Daten zum Effekt von **KI-Kennzeichnung** auf Klickrate und Konversion.

---

## 10. Quellenliste

**Plattform- und Studiendaten**
- LTK Newsroom: https://company.shopltk.com/en/press
- TIME100 Companies 2025 – LTK: https://time.com/collections/time100-companies-2025/7289649/ltk/
- TechCrunch – Mavely (27.08.2024): https://techcrunch.com/2024/08/27/mavely-influencer-social-commerce-platform-675m-gmv/
- TechCrunch – ShopMy (14.03.2024): https://techcrunch.com/2024/03/14/shopmy-influencer-marketing-platform-lands-18-5-million-funding-round/
- Influencer Marketing Hub – Affiliate Marketing Benchmark Report (PDF): https://influencermarketinghub.com/ebooks/Affiliate_Marketing_Benchmark-Report-2023.pdf
- Influencer Marketing Hub – Creator Earnings Report 2025: https://influencermarketinghub.com/creator-earnings-report-2025/
- Linktree Creator Report: https://linktr.ee/creator-report/
- Goldman Sachs – Creator Economy: https://www.goldmansachs.com/insights/articles/the-creator-economy-could-approach-half-a-trillion-dollars-by-2027
- Short Form Nation (TikTok-Shop-Perzentile): https://www.shortformnation.com/blog/tiktok-shop-affiliate-marketing-the-complete-2026-guide
- Hamster Garage (Sekundär-Aggregation TikTok Shop): https://www.hamstergarage.com/article/tiktok-shop-affiliate-statistics-benchmarks-roi
- Taylor Sicard (Sekundär-Aggregation TikTok Shop): https://taylorsicard.com/blog/tiktok-shop-affiliate-economics
- Syncly (Kritik an unbelegten TikTok-Shop-Statistiken): https://syncly.app/blog/tiktok-shop-affiliate-roi-in-2026-what-the-data-actually-shows
- Amra & Elma (SEO-Aggregator, nicht verwendet): https://www.amraandelma.com/amazon-influencer-program-statistics/

**Amazon**
- lgsagency (faceless IG → Storefront): https://lgsagency.substack.com/p/i-started-a-brand-new-instagram-account · https://lgsagency.substack.com/p/i-had-an-amazon-storefront-for-years · https://lgsagency.substack.com/p/amazon-storefront-the-setup-the-drives
- Fortune (2023): https://www.fortune.com/2023/06/27/amazon-platform-attracting-creators-commerce-content-commissions-shopping · https://fortune.com/2023/08/21/amazon-is-taking-its-low-wage-labor-model-to-influencers
- About Amazon: https://www.aboutamazon.com/news/retail/how-amazon-influencer-program-works
- eBiz Facts (Amazon-Influencer-Fälle): https://ebizfacts.com/jewel-tolentino-amazon-influencer-video-reviews-14k-first-year/ · https://ebizfacts.com/trevin-peterson-amazon-influencer-10k-month-video-reviews/ · https://ebizfacts.com/john-muscarello-amazon-influencer-30k-month-product-research/ · https://ebizfacts.com/andreea-matei-amazon-influencer-5k-month-product-review-videos/ · https://ebizfacts.com/jared-bauman-amazon-influencer-program-40k-year-1/ · https://ebizfacts.com/hella-bella-amazon-influencer-968-first-month/ · https://www.reddit.com/r/Amazon_Influencer/comments/1i02yg2/my_experience_being_in_the_amazon_influencer/
- Reddit: https://www.reddit.com/r/AffiliateMarket/comments/1l67bcn/feeling_lost_after_earning_my_first_45_from/ · https://www.reddit.com/r/AffiliateMarket/comments/1s9ljyd/low_pinterest_click_rates/ · https://www.reddit.com/r/AffiliateMarket/comments/1nusbch/amazon_affiliate_marketing_through_pinterest/ · https://www.reddit.com/r/Amazon_Influencer/comments/1iwfn9l/amazon_canadian_storefront/ · https://www.reddit.com/r/Affiliatemarketing/comments/1qj5ioo/how_i_doubled_my_amazon_affiliate_commissions/ · https://www.reddit.com/r/passive_income/comments/1quw5lt/how_i_went_from_600_to_1100month_in_amazon/ · https://www.reddit.com/r/Affiliatemarketing/comments/1qgvlgu/building_social_media_audiences_for_affiliate/ · https://www.reddit.com/r/Affiliatemarketing/comments/1r84c5r/got_my_first_affiliate_commission_after_4_months/ · https://www.reddit.com/r/Affiliatemarketing/comments/1040ttu/youtube_12000_views_1500_clicks_only_7_sold/ · https://www.reddit.com/r/juststart/comments/w1th77/faceless_tech_youtube_channel_month_3/ · https://www.reddit.com/r/Affiliatemarketing/comments/1sadlbu/worrying_amazon_associates_update/ · https://www.reddit.com/r/u_MilesInsights/comments/1um3o54/state_of_the_amazon_influencer_program_july_2026/ · https://www.reddit.com/r/Amazon_Influencer/comments/1rmzspz/first_30_days_checkin/ · https://www.reddit.com/r/sidehustle/comments/1i90dp4/how_i_made_my_first_500_online_with_amazon/ · https://www.reddit.com/r/Pinterest/comments/1w38c53/pinterest_for_buying_items_affiliate_marketing/

**TikTok Shop**
- eBiz Facts: https://ebizfacts.com/tiktok-affiliate-marketing-electricfinger0-viral-video/ · https://ebizfacts.com/14k-30-days-faceless-ai-tiktok-shop-affiliate-videos/ · https://ebizfacts.com/yandi-latino-tiktok-shop-1m-month-12k-followers/ · https://ebizfacts.com/shop-with-brooke-tiktok-ugc-affiliate-marketing-50k-month/ · https://ebizfacts.com/sleazy-greetings-viral-on-tiktok-921k-views/
- Reddit: https://www.reddit.com/r/TikTokshop/comments/1pqbx8j/tiktok_shop_banned_my_account_and_locked_3000_in/ · https://www.reddit.com/r/TikTokshop/comments/1toxgzs/best_agencies_to_level_up_with/ · https://www.reddit.com/r/TikTokshop/comments/1w7qlfg/what_am_i_doing_wrong/ · https://www.reddit.com/r/TikTokshop/comments/1ugrszw/if_youre_a_tiktok_shop_affiliate_getting_low/ · https://www.reddit.com/r/TikTokshop/comments/1r7h6jy/50_samples_sent_2_sales_total_is_tiktok_shop_just/ · https://www.reddit.com/r/TikTokshop/comments/1v7p0ew/is_tiktok_shop_still_worth_it_in_2026/ · https://www.reddit.com/r/Affiliatemarketing/comments/1u19zgj/i_will_not_promote_built_a_niche_affiliate_site/

**Faceless-, Theme- und AI-Pages**
- Reddit: https://www.reddit.com/r/InstagramMarketing/comments/1fza89h/how_i_started_my_theme_page_on_instagram_and/ · https://www.reddit.com/r/InstagramMarketing/comments/1lgw22h/how_i_made_7000_in_60_days_with_a_physical/ · https://www.reddit.com/r/InstagramMarketing/comments/1lihtcv/how_i_made_daily_affiliate_income_on_instagram/ · https://www.reddit.com/r/digitalproductselling/comments/1onn49i/i_generated_1m_monthly_views_organically_through/ · https://www.reddit.com/r/socialmedia/comments/1mmi4js/how_i_growth_hacked_instagram_update/ · https://www.reddit.com/r/DigitalIncomePath/comments/1skcsbk/can_this_make_money_ai_influencers_77k_in_4_months/ · https://www.reddit.com/r/DigitalIncomePath/comments/1uozy8m/700_from_just_17_subs_and_32_fans_529_in/ · https://www.reddit.com/r/Vent/comments/1r9cm0d/online_businesses_are_impossible/
- eBiz Facts: https://ebizfacts.com/esther-luvv-4k-month-passive-income-instagram/ · https://ebizfacts.com/liam-james-kay-paying-instagram-influencers-to-promote-affiliate-products/ · https://ebizfacts.com/kaml-abdel-kader-9-apps-instagram-reels-10k-month/
- Guru-, SEO- und Tool-Quellen (Interessenkonflikt): https://wifimoolah.com/p/idea-53 · https://faceless.my/instagram/top-faceless-instagram-pages/ · https://medium.com/write-a-catalyst/faceless-instagram-theme-pages-5k-month-formula-2026-5fbd3037ef3c (403) · https://creatorflow.so/blog/amazon-influencer-scale-instagram-commissions/ · https://fluxnote.io/guides/how-much-instagram-reels-pay-per-million-views (nur hypothetisches Rechenbeispiel, nicht verwendet)

**Marktplätze**
- Flippa: https://flippa.com/12292926 · https://flippa.com/13049678 · https://flippa.com/13733914 · https://flippa.com/13553549 · https://flippa.com/13921895 · https://flippa.com/13414294 · https://flippa.com/13088512 · https://flippa.com/12755755 · https://flippa.com/13673243 · Suche: https://flippa.com/search?filter%5Bproperty_type%5D=instagram
- Fameswap: https://fameswap.com/browse-theme-pages-for-sale
- Reddit-Verkaufsangebot: https://www.reddit.com/r/InstagramMarketing/comments/1n1dsom/65k_instagram_page_for_sēll_ocean_niche/
