# Red-Team: Top-Earner außerhalb der Net-Influencer-US-Listen – Format-Check UK/EU (+ US-Vergleich)

Stand: 25.09.2026 · Alle TikTok-Rohdaten abgerufen am 25.09.2026 (tt_profile.sh, tt_recent.sh, tt_video.sh, tt_media.py; Kontaktbögen mit Read gesichtet).
Evidenz-Tags: **Verified** = in TikTok-Rohdaten/Frames selbst gesehen · **Claimed** = Behauptung Dritter (FastMoss, Colaba, Kalodata/Lengow, Creator-Bio) · **Estimated** = eigene Rechnung (Formel angegeben).
Kategorien: A = 100 % virtuell · B = KI-Avatar + echtes Produkt · C = KI-Stimme + echtes Produktvideo · D = echte Hände + Produkt + KI-Stimme (TTS) · E = echtes UGC, aber Skript/Stimme/Schnitt/Varianten mit KI · F = Faceless-Produktvideo (nur Hände/Produkt, Stimme menschlich oder unbekannt) · G = KI-generierte B-Roll/Bilder + echtes Produkt · H = Hybrid, bei dem KI für Zuschauer vermutlich nicht erkennbar ist · human-face = echte Person vor der Kamera · unknown.

---

## 0. Kurzfazit (für den Audit)

1. **Die Hypothese „die Top-‚Human'-Earner sind in Wahrheit faceless/KI" trifft für UK/EU weitgehend NICHT zu.** In der einzigen öffentlich verfügbaren creator-genauen Rangliste für UK (FastMoss, H1 2026, 25 Creator, geschätzt 8,18 Mio. GBP GMV) sind 13 von 25 Creatorn in allen gesichteten Shop-Videos klar **human-face** (82,7 % des GMV). Nur 2 von 25 sind rein faceless (F), und die liegen mit zusammen 131.682 GBP bei **1,6 % des GMV**. Kein einziges Konto ist A oder B. Das TikTok-Feld aigcLabelType ist bei nur 2 von 318 geprüften UK-Beiträgen gesetzt, beide von @darrenrealdeal (KI-Grafik-Slides); IsAigc ist überall false (Verified).
2. **Hybrid-Formate kommen aber häufiger vor, als der Bericht unterstellt.** 11 von 25 UK-Top-Creatorn (44 %) nutzen in mindestens einem gesichteten Shop-Post ein Format, das KI ersetzen oder bereits nutzen kann: Hands-only mit Voiceover (F/D), Slideshow, KI-Bilder. Diese 11 stehen für rund 1,33 Mio. GBP, also 16,2 % des Top-25-GMV. Mehrere **virale Top-Clips** menschlicher Creator sind faceless (z. B. @truehealthsource 24,8 Mio. Views, @wanda_maxiwoof 2,4 Mio., @aesthetically_yours_x 4,1 Mio., @rob_1161 2,0 Mio., @alittlebitemily 1,9 Mio.; Verified).
3. **Neuer Fund, nicht im Bericht:** Zwei UK-Top-Creator posten KI-generierte Bilder zu echten Produkten (G/H). (a) @darrenrealdeal (UK Home #2, 105.353 GBP H1) veröffentlicht Sales-Grafiken mit KI-Karikatur auf der 10-Pfund-Note; TikTok hat dort aigcLabelType = 2 gesetzt (Verified, 5.588 Views). (b) Die Nr. 1 in UK Food, **@annsdailydeals** (7.463 Follower, 6/6 Monate im Ranking, 103.695 GBP H1, Claimed), hat eine Foto-Karussell-Anzeige mit **194.600 Views** gepostet, deren Bilder deutliche KI-Artefakte zeigen (verstümmelte Packungsschrift „BPRDCE", „SHARPBREAD RIRGS", „BARDER"). Das ist Format **G/H**, ohne KI-Label (Verified). Die übrige Content-Basis ist human-face mit einer echten Stimme. Das zeigt: Selbst UK-Top-Creator mischen unmarkierte KI-Bilder ein, und der Bericht hat solche Hybride nicht erfasst.
4. **Außerhalb UK/EU wird der Bericht klar angreifbar.** In Colabas „Top 10 TikTok Shop Creators by GMV – April 2026" (US, Claimed) sind 3 von 10 Konten faceless und hochvolumig: @cakedfinds (Hands + Voiceover, 2,05 Mio. USD), @jetskcqzy7m (reine Foto-Slideshows mit Stock-/Meme-Bildern, 1,69 Mio. USD) und @shop_shiesty (Hands + Voiceover, 0,98 Mio. USD). Das sind 34 % des GMV dieser Top 10. Sie posten laut Verified Videozahlen und Account-Alter rund 460–570 Beiträge pro Monat, also genau das „Volumen-Regime", das der Bericht in C6/C7 für unrealistisch hält. Dazu kommt @beautypickshub („AI content" laut Colaba, 97,85 USD Umsatz pro Follower bei ca. 4.000 Followern im März 2026, Claimed). Seine Bildposts zeigen KI-generierte Lifestyle-Motive, und TikTok hat dort das Feld aigcLabelType = 2 gesetzt (Verified).
5. **Folgen für die Claims:** C1 hält. C3 hält für UK/EU weitgehend, ist aber für den US-Markt zu pessimistisch: Faceless-Volumenkonten mit vierstelliger bis sechsstelliger Monatsprovision sind plausibel (Claimed/Estimated), wenn auch nicht öffentlich als Provision verifizierbar. **C6/C7 sind als lineare Hochrechnung irreführend.** Der Bericht rechnet mit rund 120 USD GMV pro Video. Das entspricht den *schwächsten* UK-Top-25 (£55–93 GMV pro Video). Die Spitzengruppe liegt bei £500–5.700 pro Video (Estimated), also 5- bis 60-mal höher. 13 der 25 UK-Creator erreichen geschätzt mindestens 3.000 EUR Provision im Monatsschnitt, und das mit 20–150 statt 830–1.650 Videos pro Monat. Diese Creator sind aber fast alle human-face.

---

## 1. Quellen und Datenbasis

| Quelle | Inhalt | Typ / Bias | URL (Zugriff 25.09.2026) |
|---|---|---|---|
| FastMoss, „Top TikTok Shop Creators UK (H1 2026)" (24.07.2026) | 25 Creator in 5 Kategorien, Follower, geschätztes Kategorie-GMV Jan–Jun 2026, Months ranked, Stil (Video/Mixed). Brand- und Liquidations-Reseller-Konten entfernt. „Video drives over 90% of sales for 26 of the 30 leaders." | Claimed; Tool-Anbieter mit Rabattcode-CTA (Bias: Toolverkauf). Die Summen sind laut FastMoss „conservative lower bounds" und erfassen nur das Kategorie-GMV. | https://www.fastmoss.com/blog/top-tiktok-shop-creators-uk-h1-2026/ |
| FastMoss, „Top-Selling TikTok Shop Products in Europe" (April 2026) | Top-5-Produkte UK/ES/DE/FR/IT; DE #1 GreatVita 22.910 Bestellungen, 261.861 USD/Monat; DE-Top-5 zusammen 764.819 USD. Provisionen 5–15 %. | Claimed; Tool-Anbieter | https://www.fastmoss.com/blog/tiktok-shop-europe-top-products-april-2026/ |
| FastMoss-Blog-Suche (creators/germany/europe/france/spain) | **Keine** creator-genaue Rangliste für DE/FR/ES/IT gefunden. Die einzige creator-genaue EU-Liste ist UK. | – | https://www.fastmoss.com/blog/?s=creators |
| Lengow/Kalodata, „TikTok Shop Europe, Q2 2026: €500m across four markets" | 11.04.–09.07.2026: DE 174,68 Mio. EUR GMV (35 %), 73,8 % Affiliate, 69,8 % Video, 12,6 % Live; FR 132,8 Mio. (73,4 % Affiliate); ES 104,7 Mio. (70,2 %); IT 86,6 Mio. (56,3 %); vier Märkte zusammen 69,9 % Affiliate. **Keine** Creator-Handles, keine Format-Angaben. | Claimed (Kalodata-Schätzung); Lengow ist Marktplatz-Softwareanbieter | https://blog.lengow.com/tiktok-shop-europe-q2-2026-e500m-across-four-markets/ |
| WebSearch-Snippet Lengow „Top 50 Shops Europe (April 2026)" | DE Top-50-Shops 12,4 Mio. EUR; svenja.walberg 1 Mio. EUR in 3 Monaten (founder-led Live, 4.000–5.000 Creator-Videos pro Monat). Das sind **Shops, keine Affiliates**. | Claimed | https://blog.lengow.com/top-50-shops-on-tiktok-shop-in-europe/ |
| Colaba, „Top 10 TikTok Shop Creators by GMV — April 2026" | US-Top-10 mit Follower, GMV, Units und Umsatz pro Follower | Claimed; Creator-Tool-Anbieter (Bias) | https://www.colaba.us/blogs/top-10-tiktok-shop-creators-by-gmv-april-2026-creator-analysis |
| Colaba, „TikTok Shop Creator Analysis 2026" (März 2026, US) | „Beauty Picks Hub (AI content) … $97.85 revenue per follower … ~4K followers"; homevibeswithmia 99,02 USD pro Follower; cakedfinds 45,49 USD pro Follower. „AI can scale attention fast, but personal content tends to build more predictable … revenue." | Claimed; Tool-Anbieter | https://www.colaba.us/blogs/tiktok-shop-creator-analysis-2026-who-actually-makes-money-what-sells-and-how-to-scale |

Methodik der Format-Prüfung: Für jeden UK-Creator habe ich das Profil (Verified) und die neuesten 10–13 Beiträge über die Embed-Seite (Verified; zusammen 318 Beiträge mit KI-Label-Feldern) gelesen. Von 1–2 Shop-Videos pro Konto habe ich mit tt_media.py je 6 Frames, einen Kontaktbogen und ein ASR-Transkript erzeugt und die Bögen visuell klassifiziert. Wo möglich, habe ich jeweils ein virales Top-Video und ein aktuelles Video geprüft. Visuell geprüft wurden rund 45 UK-Beiträge: 43 Videos, das Foto-Karussell von @annsdailydeals und 1 Grafik-Slide von @darrenrealdeal. Grenzen: Eine Stimme kann ich nicht hören. „Voiceover ohne sichtbaren Sprecher" heißt deshalb **Stimme unbekannt (Mensch oder TTS)**, außer das Transkript enthält klare menschliche Disfluenzen („uh", Dialekt, Versprecher).

---

## 2. UK-Top-25 (FastMoss H1 2026): Formatklassifikation

Follower (FM) = FastMoss-Angabe (Claimed). Follower heute = Verified am 25.09.2026. GMV = geschätztes H1-Kategorie-GMV (Claimed). „Top-Clip" = meistgesehener Shop-Beitrag in der Embed-Liste (Verified).

| # | Handle | Kat. | Follower FM / heute | GMV H1 (GBP) | Monate | Geprüfte Shop-Beiträge (Views, Verified) | Format | KI-Label | Voiceover |
|---|---|---|---|---|---|---|---|---|---|
| 1 | @officialsamanthalouise | Womenswear | 305,6k / 306,6k | 1.368.415 | 6/6 | 7688660732233141526 (4.288), 7689385201948052758 (2.376): Frau vor der Kamera, Make-up/Try-on | human-face | nein | nein, spricht selbst |
| 2 | @abbybeechx | Womenswear | 233,3k / 234,0k | 868.255 | 6/6 | 7688846661833051414 (2.531): Spiegel-Selfie-Try-on | human-face | nein | nein |
| 3 | @auntiechar11 | Womenswear | 49,2k / 51,9k | 435.064 | 6/6 | 7520269407436786966 (1,0 Mio.), 7689462243242806530: Try-on, Brauen-Tutorial | human-face | nein | nein |
| 4 | @rocknrollmama_x | Womenswear | 288,4k / 296,0k | 368.662 | 5/6 | 7537282892083367190 (3,2 Mio.): Try-on | human-face | nein | nein |
| 5 | @aesthetically_yours_x | Womenswear | 32,9k / 34,3k | 343.605 | 4/6 | **7571192189829680386 (4,1 Mio.): nur Produkt (LED-Zweige), keine Person, Voiceover** · 7689456600469261590: OOTD mit Gesicht | **gemischt F + human-face** | nein | Top-Clip: VO, Stimme menschlich wirkend (Erzählstil) |
| 6 | @chrisandjet.tts | Sports | 27,9k / 29,6k | 717.289 | 6/6 | 7566682129388702999 (1,2 Mio.): Mann baut Laufband auf, Handy-Screenshot · 7689451923992268065: Mann im Bild | human-face | nein | nein |
| 7 | @itsanewmeemj | Sports/Health | 161,5k / 169,5k | 268.128 | 6/6 | 7689163722559982870 (15.300): Frau mit Gerät | human-face | nein | nein |
| 8 | @rob_1161 | Sports | 8,4k / 9,6k | 232.057 | 4/6 | **7638697174393457942 (2,0 Mio.): POV-Hände + Laufband, kein Gesicht, Voiceover** · 7689456142770113814: Mann vor der Kamera | **gemischt F + human-face** | nein | Top-Clip: VO, Stimme unbekannt |
| 9 | @samantha.ugc.creator | Sports | 12,7k / 12,7k | 110.306 | 5/6 | 7607201317005675798 (300k): Frau mit CoQ10 · **7689458984021183747: nur Hände + Vax-Gerät, Text-Overlay, keine Sprache** | gemischt human-face + F | nein | – |
| 10 | @chloecr3 | Sports | 18,7k / 25,1k | 102.589 | 2/6 | 7595496660915031319 (3,9 Mio.): Frau auf Laufband · 7689367599154515222: Frau mit Zahnbürste | human-face | nein | nein |
| 11 | @girlybeautyessentialshq | Beauty | 6,7k / 8,1k | 693.183 | 2/6 | 7643067458202422550 (6,3 Mio.): Frau glättet Haare vor der Kamera · 7689434366556015894 | **human-face** (Hypothese „faceless" widerlegt) | nein | nein |
| 12 | @lucyandlittle | Beauty | 121,2k / 0 (Profil zeigt 0) | 580.821 | 1/6 | 7633382933193084182 (15,4 Mio.), 7689462340839820566: Frau vor der Kamera | human-face | nein | nein |
| 13 | @stephanievavron | Beauty | 718,9k / 724,6k | 481.240 | 3/6 | 7594913738071772438 (3,3 Mio.): Maske/Glass-Skin am eigenen Gesicht | human-face | nein | nein |
| 14 | @makeupbykaty_angelidi | Beauty | 195,1k / 196,1k | 424.563 | 5/6 | 7688834137611865346: Raum-/Möbel-Tour, danach Gesicht | human-face | nein | nein |
| 15 | @dfmakeupartist | Beauty | 114,2k / 115,8k | 412.836 | 5/6 | 7573773963722018070 (13,1 Mio.), 7689411129512037654: Tutorial am eigenen Gesicht | human-face | nein | nein |
| 16 | @three_reasons_why | Home | 24,8k / 26,7k | 117.486 | 5/6 | 7684285120014077216 (702k): Mann + Hände-Inserts · **7689451525692755232: nur Hände/TV, Wort-für-Wort-Captions, Voiceover** | gemischt human-face + F | nein | 2. Clip: VO, Stimme unbekannt |
| 17 | @darrenrealdeal | Home | 26,2k / 29,0k | 105.353 | 3/6 | 7657936707253325078 (1,1 Mio.), 7689277479739165975: Mann + Hände-Demo · **7689099249350397206 (5.588) und 7689096776330054934 (1.931): Foto-Slides mit KI-Werbegrafik (Süßigkeiten, KI-Karikatur auf 10-£-Note)** | **human-face + G** | **aigcLabelType = 2 an beiden Grafik-Posts** (IsAigc false) | nein |
| 18 | **@truehealthsource** | Home | 21,4k / 22,6k | 71.212 | 2/6 | **7629444796087651606 (24,8 Mio.): nur Hände + Abfluss, Wort-für-Wort-Captions, Voiceover** · **7689191276931173654: nur Hände/Studio-Licht, gleicher Stil** | **F, möglicherweise D** (Skript im Copywriting-Stil: „this isn't that diluted supermarket stuff") | nein (IsAigc = false) | ja; Stimme unbekannt, TTS nicht verifizierbar |
| 19 | @alittlebitemily | Home | 26,4k / 27,9k | 63.755 | 1/6 | **7679001366374747414 (1,9 Mio.): POV-Hände/Raum, kein Gesicht, VO** · 7689353229615861014: kurz Gesicht, dann Produkt | gemischt F + human-face | nein | Top-Clip: VO, menschlich wirkend (Schimpfwörter, Spontansprache) |
| 20 | **@thedealshunter** | Home | 28,7k / 30,8k | 60.470 | 3/6 | 7566616468994018582 (788,7k): Körper ohne Gesicht (Hosen-Try-on) · 7689455822727908630: nur Hände | **F** | nein | ja; menschlich (Disfluenzen „uh") |
| 21 | **@annsdailydeals** | Food | 7,5k / 7,6k | 103.695 | **6/6** | 7689462013356969248 und 7686071092884131104 (160,3k): Frau vor der Kamera bzw. menschliche Stimme mit Akzent · **7651963739092094230 (194,6k): Foto-Karussell mit 6 Bildern, KI-typische Artefakte (verstümmelte Markenschrift „BPRDCE", „SHARPBREAD RIRGS", „BARDER"), fotoreale Stock-Ästhetik; Caption im LLM-Ton** | **human-face + G/H (unmarkierte KI-Bilder)** | **nein**, obwohl realistische KI-Szenen | – |
| 22 | @positivetwo24 | Food | 158,5k / 163,9k | 87.778 | 2/6 | Unter den letzten 13 Beiträgen kein Shop-Video (Comedy-Paar, Vlogs) | unknown (Shop-Content nicht gesehen) | – | – |
| 23 | @wanda_maxiwoof | Food | 136,6k / 136,5k | 80.456 | 2/6 | **7634574189277564163 (2,4 Mio.): nur Hände + Proteinriegel, Voiceover** | F (Account sonst human-face mit Hund) | nein | ja; Stimme unbekannt |
| 24 | @shabzofficial | Food | 41,8k / 42,7k | 40.301 | 2/6 | 7681422881880067331 (165k), 7688095439211531552: Mann vor der Kamera. Captions sind wörtliche Seller-Produkttitel; bis zu 5 Posts in wenigen Minuten | human-face (Copy aus dem Katalog) | nein | nein |
| 25 | @charzreviews | Food | 223,4k / 225,3k | 37.871 | 2/6 | **7689092193352469792: nur Hände + Kaffeemaschine, Text-Overlay, keine Sprache (kein ASR)** · Award-Clips mit Gesicht | gemischt F + human-face | nein | – |

**Auszählung UK (Estimated aus der obigen Klassifikation, n = 25):**

| Format | Konten | Anteil | GMV H1 (GBP) | Anteil am GMV (8,18 Mio.) |
|---|---|---|---|---|
| A / B (virtuell, KI-Avatar) | 0 | 0 % | 0 | 0 % |
| rein F/D (faceless) | 2 (@truehealthsource, @thedealshunter) | 8 % | 131.682 | 1,6 % |
| gemischt human-face + F | 7 | 28 % | 985.536 | 12,1 % |
| human-face + G/H (KI-Bilder) | 2 (@annsdailydeals, @darrenrealdeal) | 8 % | 209.048 | 2,6 % |
| nur human-face | 13 | 52 % | 6.761.346 | 82,7 % |
| unknown | 1 (@positivetwo24) | 4 % | 87.778 | 1,1 % |
| **faceless/hybrid in mind. einem Shop-Beitrag** | **11** | **44 %** | **1.326.266** | **16,2 %** |

TikTok-KI-Label: Über alle 318 per Embed geprüften UK-Beiträge ist IsAigc = false. aigcLabelType = 2 steht nur bei den 2 KI-Grafik-Posts von @darrenrealdeal. Beim fotorealistischen KI-Karussell von @annsdailydeals fehlt jedes Label (Verified). Summe GMV Top 25 = 8.175.390 GBP.

---

## 3. Kennzahlen: GMV pro Follower, pro Video, pro 1.000 Views und implizite Provision

### 3.1 Implizite Provision (Estimated)

Formel: Provision/Monat (EUR) = GMV_H1 ÷ 6 × Kategorie-Provision × 0,9 (10 % Retouren, wie im Bericht) × 1,17 EUR/GBP.
Provisionssätze: Kategorie-Mediane laut Bericht bzw. FastMoss (n = 298; Womenswear 10 %, Sports 10 %, Beauty 15 %, Home 10–15 %, Food 10 %; Claimed).
„Ranking-Monate" = GMV_H1 ÷ Anzahl gerankter Monate. FastMoss summiert nur Monate, in denen ein Creator gerankt war. Der 6-Monats-Schnitt behandelt die übrigen Monate also als 0 und ist eine Untergrenze.

| Handle | Format | GMV/Monat Ø (GBP) | Provision Ø H1 (EUR/Monat) | Provision in Ranking-Monaten (EUR/Monat) | Videos/Monat* | GMV/Video* (GBP) |
|---|---|---|---|---|---|---|
| @officialsamanthalouise | human-face | 228.069 | 24.016 | 24.016 | ~86 | ~2.658 |
| @girlybeautyessentialshq | human-face | 115.530 | 18.248 | 54.744 | ~20 | ~5.676 |
| @lucyandlittle | human-face | 96.804 | 15.290 | 91.741 | ~68 | ~1.427 |
| @abbybeechx | human-face | 144.709 | 15.238 | 15.238 | ~93 | ~1.554 |
| @stephanievavron | human-face | 80.207 | 12.669 | 25.337 | ~154 | ~521 |
| @chrisandjet.tts | human-face | 119.548 | 12.588 | 12.588 | ~97 | ~1.236 |
| @makeupbykaty_angelidi | human-face | 70.760 | 11.177 | 13.412 | ~49 | ~1.442 |
| @dfmakeupartist | human-face | 68.806 | 10.868 | 13.041 | ~118 | ~583 |
| @auntiechar11 | human-face | 72.511 | 7.635 | 7.635 | ~53 | ~1.364 |
| @rocknrollmama_x | human-face | 61.444 | 6.470 | 7.764 | ~27 | ~2.252 |
| @aesthetically_yours_x | F + human-face | 57.268 | 6.030 | 9.045 | ~37 | ~1.565 |
| @itsanewmeemj | human-face | 44.688 | 4.706 | 4.706 | ~137 | ~325 |
| @rob_1161 | F + human-face | 38.676 | 4.073 | 6.109 | ~57 | ~676 |
| @three_reasons_why | F + human-face | 19.581 | 2.062–3.093 | 2.474–3.711 | ~64 | ~308 |
| @samantha.ugc.creator | F + human-face | 18.384 | 1.936 | 2.323 | ~149 | ~123 |
| @darrenrealdeal | human-face + G | 17.559 | 1.849–2.773 | 3.698–5.547 | ~102 | ~172 |
| @annsdailydeals | human-face + G/H | 17.282 | 1.820 | 1.820 | ~186 | ~93 |
| @chloecr3 | human-face | 17.098 | 1.800 | 5.401 | ~81 | ~210 |
| @positivetwo24 | unknown | 14.630 | 1.541 | 4.622 | ~27 | ~544 |
| @wanda_maxiwoof | F + human-face | 13.409 | 1.412 | 4.236 | ~82 | ~164 |
| **@truehealthsource** | **F (ggf. D)** | 11.869 | **1.250–1.875** | **3.749–5.624** | **~26** | **~465** |
| @alittlebitemily | F + human-face | 10.626 | 1.119–1.678 | 6.713–10.070 | ~77 | ~137 |
| **@thedealshunter** | **F** | 10.078 | **1.061–1.592** | 2.122–3.184 | ~185 | ~55 |
| @shabzofficial | human-face | 6.717 | 707 | 2.122 | ~59 | ~115 |
| @charzreviews | F + human-face | 6.312 | 665 | 1.994 | ~86 | ~74 |

\* Videos/Monat = Verified videoCount ÷ Monate seit Kontoerstellung (Verified createTime), also ein Lebenszeit-Durchschnitt. GMV/Video = GMV_H1 ÷ (6 × Videos/Monat). Beides ist Estimated und grob, weil nur Kategorie-GMV erfasst ist und die Posting-Rate schwankt.

**Ergebnis:** 13 von 25 UK-Top-Creatorn erreichen geschätzt mindestens 3.000 EUR Provision im H1-Monatsschnitt, 10 davon mindestens 6.000 EUR. Alle 13 sind human-face; bei 2 davon (@aesthetically_yours_x, @rob_1161) ist der virale Top-Clip faceless. Die beiden rein faceless Konten liegen im Schnitt bei 1,1–1,9 Tsd. EUR, in ihren Ranking-Monaten bei 2,1–5,6 Tsd. EUR (Estimated). Selbst angegeben ist nur @charzreviews: Bio „£11M+GMV", ein Post zu „1 million gmv in 30 days" als TikTok-Shop-Award (Claimed; Bias: Gründerin einer Creator-Agentur „CN MediaVerse").

### 3.2 GMV pro 1.000 Views

Nicht öffentlich verifizierbar. Weder FastMoss noch TikTok geben die H1-Views je Creator an. Hilfsrechnung (Estimated, hohe Unsicherheit): Lebenszeit-Views ≈ heartCount (Verified) ÷ viewgewichtete Like-Rate der gesichteten Videos (Verified). GMV_H1 ÷ Lebenszeit-Views ist dann eine **Untergrenze** für GMV pro 1.000 H1-Views. Werte: £0,08 (@wanda_maxiwoof) bis £15,6 (@officialsamanthalouise); @girlybeautyessentialshq ≥ £6,8, @rob_1161 ≥ £6,1, @truehealthsource ≥ £0,19. Weil Lebenszeit-Views nicht die H1-Views sind und nur das Kategorie-GMV zählt, taugt das **nicht**, um den C5-Wert (~30 USD pro 1.000 Views) zu widerlegen oder zu bestätigen. Belastbarer ist die Rechnung pro Video in 3.1.

### 3.3 Einordnung gegen das Modell im Bericht (C5–C7)

- Der Bericht rechnet (C5) mit 4.000 Views × 30 USD pro 1.000 Views = **~120 USD GMV pro Video (≈ £90)**. Das entspricht fast genau den **schwächsten** UK-Top-25: @thedealshunter ~£55, @charzreviews ~£74, @annsdailydeals ~£93 pro Video (Estimated). Der Durchschnittsfall aus C5 ist also realistisch für ein Deal-Volumenkonto. @annsdailydeals mit ~186 Posts pro Monat und ~1.800 EUR Provision pro Monat ist praktisch eine Live-Bestätigung von C5 (~150 Videos → ~1.650 EUR).
- **C6/C7 rechnen linear mit Volumen.** In den Daten ist die Streuung von GMV pro Video der dominante Hebel: £55 bis £5.676, Faktor ~100. 10.000 EUR pro Monat erreichen UK-Creator mit 20–120 Videos pro Monat, nicht mit 830. Die „830/1.650 Videos"-Aussage stimmt also nur unter der Annahme, dass der GMV pro Video beim Median bleibt. Als Aussage über den *Weg* zu 10–20 Tsd. EUR ist sie zu pessimistisch; als Aussage über die *Wahrscheinlichkeit* für einen neuen KI-Account eher nicht, denn alle UK-Konten mit hohem GMV pro Video sind human-face mit Vertrauens- oder Expertenbonus (z. B. MUA mit 30 Jahren Erfahrung, Mode-Try-on).

---

## 4. US-Vergleich außerhalb der Net-Influencer-Listen (Colaba April/März 2026)

| Handle | GMV (Claimed, Colaba) | Follower heute (Verified) | Videos / Alter (Verified) | Posts/Monat (Estimated) | Format (Verified über Frames) | KI-Label | Anmerkung |
|---|---|---|---|---|---|---|---|
| @cakedfinds | 2,05 Mio. USD (April 2026), 50.931 Units | 78.700 | 12.700 / seit 13.11.2024 | ~567 | **F/D**: nur Hände + Beauty-Sets (Celimax), Voiceover mit Skript-Template („Not one, not two, but three…"); **identische Caption** „It's on such a good deal today 😳" auf 9 von 10 Videos; 10/10 isAd = true | nein | Hochvolumen, templatisiert, Seller-bezahlte Ausspielung (isAd); Kontakt „ryshops09" deutet auf ein Shop-Team hin (Vermutung) |
| @jetskcqzy7m | 1,69 Mio. USD (April), 45.851 Units | 31.100 | 8.061 / seit 14.04.2025 | ~463 | **Slideshow** (Dauer 0): Stock-/Meme-/Filmstill-Bilder mit Hook-Text + Produktfoto in der Hand; keine Kamera, keine Stimme. Mindestens 1 Bild ist ein reales Stockfoto (Nürnberg, Pegnitz) | nein | Format voll KI- bzw. automatisierbar (G/H-nah); Fremdbilder, urheberrechtlich heikel |
| @shop_shiesty | 0,98 Mio. USD (April) | 23.300 | 3.419 / seit 07.03.2024 | ~113 | **F/D**: Hände + Produkt (Dashcam am Mercedes, Uhr), Voiceover; Captions teils „Posting for sample" | nein | Faceless |
| @homevibeswithmia | 99,02 USD/Follower (März) → bei ~11,6k Followern ≈ 1,1 Mio. USD (Estimated aus Claimed) | 11.600 | 764 / seit 04.08.2025 | ~59 | Brand-Footage (Bedlore) + englischer Voiceover. In einem Video (10,2 Mio. Views) **deutsche** Bildschirm-Texte („Ab 40 versteht man, wie wichtig ein gutes Bett ist") → wiederverwendetes Hersteller-Material, **H/E** | nein | **ttSeller = true** (Verified): Seller-eigenes Konto, **kein unabhängiger Affiliate** |
| @beautypickshub | 97,85 USD/Follower bei ~4k Followern (März) → ≈ 0,39 Mio. USD (Estimated aus Claimed); Colaba nennt es ausdrücklich „AI content" | 7.363 | 427 / seit 12.02.2025 | ~22 | Videos: Hände + Beauty-Sets im Auto, auf allen Clips identisches Voiceover-Skript („Caught it during this massive markdown … Stock is crashing! Tap the cart below") → **D/E**; Foto-Posts: KI-generierte Lifestyle-Bilder (**G**) | **aigcLabelType = 2** an 3 Posts (IsAigc = false; Bedeutung nicht offiziell dokumentiert) | Spitzen im Juli 2026 (184,6k / 86,9k Views), heute wenige Hundert bis wenige Tausend Views → **Spike-Muster**, deckt sich mit Colabas Aussage „aggressive spikes" |
| @be.lush | 1,12 Mio. USD (April) | 271.000 | 2.796 | – | human-face plus reine Produkt-B-Roll-Clips (Staubsauger) → gemischt | nein | „TikTok Shop Home Creator of the Year 2026" (Bio, Claimed) |

Von den Colaba-Top-10 (April, zusammen ≈ 13,95 Mio. USD, Claimed) sind 3 faceless (cakedfinds, jet, shop_shiesty) mit 4,72 Mio. USD, also **34 % des GMV** (Estimated). Die übrigen sind Live-Breaks (burtonbreaks, huntbreaks), human-face-Lifestyle (simplymandys, una_flor_cubana, dj.foof), Reviews (dudedealz) und gemischt (be.lush).
Implizite Provision (Estimated): @cakedfinds 2,05 Mio. USD × 10–15 % × 0,9 ≈ **185.000–277.000 USD** im April; @jetskcqzy7m 1,69 Mio. × 10–15 % × 0,9 ≈ **152.000–228.000 USD**. Nicht verifizierbar. Colaba-Werte sind Modellschätzungen eines Tool-Anbieters, und bei Seller-nahen Konten (isAd, Muster-Captions) kann ein Teil der Vergütung anders fließen (Retainer, Seller-bezahlte Ads).

---

## 5. Was das für die Claims bedeutet

| Claim | Red-Team-Urteil | Begründung |
|---|---|---|
| C1 Vollvirtuelle KI-Influencer funktionieren nicht | **Hält** | 0 von 25 UK- und 0 von 10 US-Top-Konten sind A/B (Verified über Frames). |
| C2 KI-Shop-Accounts mit hohen Views sind kurzlebige Supplement-Netzwerke | **Teilweise angreifbar** | @beautypickshub (KI-Content laut Colaba) ist Beauty, nicht Supplements, und zeigt ein Spike-Muster (bestätigt „kurzlebig"). Die faceless US-Konten cakedfinds/jet sind 11–22 Monate aktiv mit ~460–570 Posts pro Monat und keine Supplement-Netzwerke. Ob sie KI nutzen, ist nicht verifizierbar; das Format ist aber KI-kompatibel. |
| C3 Dauerhafte vierstellige Provisionen mit KI-Content sind selten | **UK/EU: hält weitgehend. US: zu pessimistisch, wenn man das Format statt des Labels zählt.** | UK: Die einzigen rein faceless Top-25-Konten erreichen Ø 1,1–1,9 Tsd. EUR pro Monat (Estimated), sind aber nur 2/6 bzw. 3/6 Monate gerankt, also nicht „dauerhaft". Der einzige Top-Creator mit KI-Bildern (@annsdailydeals, 6/6 Monate, ~1,8 Tsd. EUR pro Monat) nutzt sie nur als Beimischung. US: faceless Templat-Konten mit sechsstelliger Monatsprovision sind **plausibel, aber unverifiziert** (Claimed GMV). |
| C4 10k+-Behauptungen stammen meist von Kursverkäufern | **Hält in der Tendenz**, mit Ausnahme | Die großen Zahlen hier stammen von Tool-Anbietern (FastMoss, Colaba, Kalodata), nicht von Kursverkäufern. Sie sind ebenfalls interessengeleitet, aber systematische Schätzungen. Die Einkommen sind also nicht nur Kursmarketing, aber auch nicht verifiziert. |
| C5 ~1.650 EUR bei 5 Videos pro Tag | **Bestätigt als Median-Fall** | Das Modell entspricht dem GMV pro Video der schwächsten UK-Top-25 (£55–93). @annsdailydeals (~186 Posts pro Monat, ~1,8 Tsd. EUR) liegt fast exakt auf dem Modell. |
| C6 10k EUR brauchen ~830 Videos pro Monat | **Methodisch zu pessimistisch** | Lineare Hochrechnung bei konstantem GMV pro Video. Real reichen 20–120 Videos pro Monat bei hohem GMV pro Video (UK), oder Volumen mit ~460–570 Posts pro Monat plus Seller-Ads (US-faceless). Der Engpass ist die Trefferquote pro Video, nicht die Zahl der Videos. |
| C7 20k EUR brauchen ~1.650 Videos pro Monat und ein Team | **Teils bestätigt, teils zu pessimistisch** | Die US-Faceless-Spitzen arbeiten tatsächlich mit Team-Volumen (vermutlich; 8.000–12.700 Videos). UK-Creator mit ≥20k EUR pro Monat (@officialsamanthalouise, @girlybeautyessentialshq in Ranking-Monaten) brauchen <100 Videos, aber ein echtes Gesicht. |

**Wo der Bericht zu eng definiert hat:** Er klassifiziert „KI-Content" nach sichtbarer KI (Avatar, TTS-Label). Das KI-*ersetzbare* Format sind aber F/D/Slideshows: echte Hände oder Fremdbilder plus Voiceover oder Text. Es ist bei 44 % der UK-Top-Creator zumindest beigemischt und bei 30 % der US-Top-10 das Hauptformat. Dazu kommen KI-Bilder (G/H) bei zwei UK-Top-Creatorn (@annsdailydeals unmarkiert, @darrenrealdeal mit TikTok-Label) und Skript-Templates im LLM-Stil (@beautypickshub, @cakedfinds, Caption-Templates bei @annsdailydeals: „Price disclaimer: TikTok Shop prices can change fast…"). Ob Skripte KI-geschrieben sind (E), ist grundsätzlich nicht verifizierbar. Die Template-Uniformität spricht bei mehreren Konten aber dafür (Vermutung).

---

## 6. Bedeutung für den DE-Markt

- **Keine öffentliche creator-genaue Rangliste für DE/FR/ES/IT** (FastMoss-Blog, Lengow/Kalodata und News-RSS durchsucht). Lengow/Kalodata nennt keine Creator-Handles und keine Formate. Aussagen zu DE-Formaten sind daher **nicht öffentlich verifizierbar**.
- Marktgröße (Claimed, Kalodata über Lengow): DE 174,7 Mio. EUR GMV in 90 Tagen (11.04.–09.07.2026), davon 73,8 % über Affiliates und 69,8 % über Video. Estimated: 174,7 × 0,738 ÷ 3 ≈ **43 Mio. EUR Affiliate-GMV pro Monat**. Das ist mehr als der UK-Wert, den der Bericht implizit annahm („niedriger einstelliger Prozentbereich des US-Werts"). **Der Bericht unterschätzt DE vermutlich.** DE ist in Q2 2026 der größte der vier EU-Festlandmärkte (35 %).
- Übertragung (Estimated): Ein DE-Creator mit einem UK-Top-25-Profil (z. B. £10–20k GMV pro Monat wie die Home/Food-Deal-Konten) hätte bei 10–15 % Provision rund 1–3 Tsd. EUR pro Monat. Das ist genau die Zone, in der rein faceless Konten in UK real vorkommen (@truehealthsource, @thedealshunter).
- DE-Produktmix (FastMoss April 2026, Claimed): Wellness/Snacks/Supplements, höchster Ø-Preis der Top 5 (13,83 EUR), Supplement-Provision 15 %. Genau hier sind KI-Formate policy-seitig am stärksten eingeschränkt (siehe Bericht Kap. 1). Hands-only-Demo (F/D) ist das policy-konforme Faceless-Format mit realen Erfolgsbeispielen in UK.
- EU-KI-VO Art. 50: Unmarkierte fotoreale KI-Bilder, wie bei @annsdailydeals (UK, nicht EU) gesehen, wären in DE kennzeichnungspflichtig. Der UK-Fund zeigt, dass solche Hybride Reichweite bringen (194,6k Views), aber rechtlich nicht 1:1 übertragbar sind.

---

## 7. Ausreißer-Videos (Verified Views; GMV pro Video nicht öffentlich)

| Video | Handle | Format | Views (Verified) | Anmerkung |
|---|---|---|---|---|
| https://www.tiktok.com/@truehealthsource/video/7629444796087651606 | @truehealthsource | F/D (Hände, Wort-Captions, Voiceover) | 24.800.000 | Abflussreiniger (ENMALL); isAd = true |
| https://www.tiktok.com/@lucyandlittle/video/7633382933193084182 | @lucyandlittle | human-face | 15.400.000 | Dr.Melaxin-Set; isAd = true |
| https://www.tiktok.com/@dfmakeupartist/video/7573773963722018070 | @dfmakeupartist | human-face | 13.100.000 | Contour-Tutorial 40+ |
| https://www.tiktok.com/@homevibeswithmia/video/7659720589728337182 | @homevibeswithmia (US, Seller) | H/E (Brand-Footage, DE-Text, EN-VO) | 10.200.000 | Bedlore-Topper; ttSeller |
| https://www.tiktok.com/@girlybeautyessentialshq/video/7643067458202422550 | @girlybeautyessentialshq | human-face | 6.300.000 | Remington-Glätteisen ≤ £20 |
| https://www.tiktok.com/@aesthetically_yours_x/video/7571192189829680386 | @aesthetically_yours_x | F (nur Produkt + VO) | 4.100.000 | LED-Zweige, Black Friday |
| https://www.tiktok.com/@wanda_maxiwoof/video/7634574189277564163 | @wanda_maxiwoof | F (Hände + VO) | 2.400.000 | Warrior-Proteinriegel |
| https://www.tiktok.com/@rob_1161/video/7638697174393457942 | @rob_1161 | F (POV-Hände + VO) | 2.000.000 | UMAY-Laufband |
| https://www.tiktok.com/@alittlebitemily/video/7679001366374747414 | @alittlebitemily | F (POV + VO) | 1.900.000 | Wäscheständer |
| https://www.tiktok.com/@thedealshunter/video/7566616468994018582 | @thedealshunter | F | 788.700 | Fleece-Arbeitshose |
| https://www.tiktok.com/@annsdailydeals/video/7651963739092094230 | @annsdailydeals | G/H (KI-Bild-Karussell, unmarkiert) | 194.600 | Border-Kekse |
| https://www.tiktok.com/@beautypickshub/video/7665691177278082335 | @beautypickshub (US) | D/E (Hände + Template-Voiceover) | 184.600 | Tarte-BB-Set |

---

## 8. Offene Punkte und Unsicherheiten

- Alle GMV-Werte sind Tool-Schätzungen (Claimed). FastMoss-UK zählt nur Kategorie-GMV und nur gerankte Monate (Untergrenze). Colaba-US-Werte sind nicht mit einer zweiten Quelle abgeglichen.
- Provisionen sind nirgends verifiziert (kein Dashboard gesehen); alle Provisionswerte sind Estimated.
- TTS vs. menschliche Stimme ist aus Frames und ASR nicht sicher unterscheidbar. D ist bei @truehealthsource, @wanda_maxiwoof und @rob_1161 möglich, aber nicht belegt. @thedealshunter und @alittlebitemily klingen im Transkript menschlich.
- Pro Konto wurden nur 1–2 Beiträge visuell geprüft. Der Formatanteil kann in beide Richtungen verzerrt sein.
- @lucyandlittle zeigt heute followerCount = 0 (Verified; vermutlich Anzeigefehler oder Einschränkung).

Rohdaten: research/redteam/profiles_table.tsv, research/redteam/videos_by_author.json, research/redteam/uk2/vids.jsonl, research/redteam/uk2/vids_bph.jsonl, media/<id>/ (Frames, sheet.jpg, meta.json mit ASR), research/redteam/comp2/*.jpg (Kontaktbögen), research/redteam/img/7651963739092094230/ (KI-Karussell).

### Verifikation UK2

Urteil: **PARTIALLY.** Der Kernfund stimmt, Kategorie und Geldzuordnung sind zu grob. Prüfung am 25.09.2026:
- Profil @annsdailydeals (Verified): 7.625 Follower, 5.937 Beiträge, erstellt im Januar 2024, Bio „Mum of 2, Unboxing, Deals“. Das sind ca. 183 Beiträge pro Monat, passend zu ~186 im Bericht.
- Beitrag 7651963739092094230 (Verified): 194.600 Views, Foto-Karussell (duration 0), isECVideo = 1, IsAigc = false, aigcLabelType = null, isAd = **false**. Die Bezeichnung „Anzeige“ im Befund ist also falsch; gemeint ist ein Shop-Post. Gepostet am ca. 16.06.2026, also innerhalb von H1.
- Die 6 Bilder habe ich selbst angesehen. Sie sind eindeutig KI-generiert: generische Stock-Küchen- und Holztisch-Szenen und fehlerhafte Packungsschrift, z. B. verstümmelte „Shortbread Rings“-Beschriftungen, eine gespiegelte „BORDER“-Schrift und Pseudo-Siegel. Die Marke Border existiert, die Verpackungen sind aber nicht echt abgebildet. Es gibt kein KI-Label. Die Caption („honestly wasn’t expecting much … disappeared way faster than I’d like to admit 😅“) liest sich wie LLM-Text. Das ist plausibel, aber nicht beweisbar.
- 4 neue Beiträge geprüft: 7686071092884131104 (160,3k Views), 7689462013356969248, 7689444883160943904 und 7689406956506778912; keiner hat ein KI-Label. Kontaktbogen von 7689444883160943904 (tt_media): **nur Hände + echte Süßigkeitentüte, kein Gesicht, keine Sprache**. Das ist Format F. Die Aussage „Rest des Kontos human-face mit echter Stimme“ ist deshalb zu pauschal. Richtig ist: **gemischt human-face + F (Hände) + vereinzelt G/H (unmarkierte KI-Bilder)**.
- Arithmetik (Estimated): 103.695 GBP ÷ 6 = 17.282 GBP GMV pro Monat (Claimed, nur FastMoss-Kategorie-GMV, Untergrenze). Bei 10 % Provision und 10 % Retouren ergibt das 1.555 GBP, also ca. 1.980–2.110 USD pro Monat (1,27–1,36 USD/GBP). Bei 8–12 % Provision sind es ca. 1.600–2.500 USD. Die Spanne 1.700–2.500 USD ist damit für die **gesamte Kontoprovision** vertretbar. Sie beruht auf Schätzung von GMV, nicht auf tatsächlich ausgezahlter Provision.
- Einschränkung: Das Geld lässt sich **nicht** dem KI-Format zuschreiben. Das Karussell ist 1 von ca. 5.900 Beiträgen, und der Umsatz entsteht vor allem durch human-face- und Hände-Videos mit hohem Volumen. Welcher Anteil auf KI-Bilder entfällt, ist nicht öffentlich verifizierbar und wahrscheinlich gering.
- Der Fund belegt, dass Top-Creator unmarkierte KI-Bilder einmischen (Label-Lücke). Er ist aber kein Beleg für ein profitables KI-Content-Geschäftsmodell. Gegen C1 spricht er nur bei der Definitionsbreite (Hybride). Der Red-Team-Text sagt selbst: „C1 hält“.

### Verifikation UK7

**Urteil: PARTIALLY (Fakten bestätigt, Beweiskraft gegen C3 überzeichnet).** Geprüft am 2026-09-25.

- **Views neu abgerufen (tt_video.sh, Verified):** @aesthetically_yours_x 7571192189829680386 = 4,1 Mio. (erstellt 10.11.2025, 50 s, LED-Zweige); @wanda_maxiwoof 7634574189277564163 = 2,4 Mio. (30.04.2026, 18 s, Warrior-RAW-Proteinriegel); @rob_1161 7638697174393457942 = 2,0 Mio. (01.06.2026, 51 s, UMAY-Laufband); @alittlebitemily 7679001366374747414 = 1,9 Mio. (28.08.2026, 60 s, Wäscheständer). Alle isECVideo=1, IsAigc=False, kein KI-Label.
- **Format (Kontaktbögen gesichtet):** In allen vier Clips ist kein Gesicht zu sehen. Die LED-Zweige laufen als reines Produkt-Kameraschwenk mit Text-Overlay, die anderen drei zeigen Hände oder POV. Die Einstufung „F“ stimmt.
- **Die Konten sind human-face (Verified):** Ein neuer tt_media-Lauf auf @rob_1161 7689456142770113814 zeigt einen Mann vor der Kamera, der spricht (ASR: Remington-Glätteisen, 68 Views). Die Bios nennen reale Personen, bei @wanda_maxiwoof etwa „Declan & Wanda“. Das Etikett „virale faceless Clips menschlicher Creator“ ist also richtig.
- **Einschränkungen:**
  1. Die Clips sind ausgewählte Ausreißer. Die neuesten Posts derselben Konten liegen oft bei 68–158 Views. Andere Hits derselben Konten (z. B. 2,3 Mio. LED-Leuchten, 1,6 Mio. Parfüm und 1,4 Mio. Laufband bei rob, 1,7 Mio. Rituals bei wanda) wurden nicht einzeln auf das Format geprüft.
  2. Views sind kein GMV und keine Provision. Welcher Umsatz an diesen Clips hängt, ist nicht öffentlich verifizierbar.
  3. Ob die Stimme per TTS oder KI erzeugt ist, ist nicht belegt. @alittlebitemily klingt menschlich (Spontansprache, Fluchen). Im Clip von @aesthetically_yours_x ist das VO nicht sicher belegt, zu sehen ist nur ein Text-Overlay.
  4. Keines der Konten nutzt nachweislich KI.
- **Folge für C3:** Das Material zeigt, dass das Format funktioniert und sich mit KI-Voice replizieren ließe. Dass KI-Content dauerhaft vierstellige Provisionen bringt, zeigt es nicht. Als Gegenbeweis zu C3 ist es daher **moderat statt „strong“**. Es relativiert nur die C3-Definition von „KI-/faceless Content“. Kategorie viral_faceless_clips_of_human_creators, Format F: korrekt.

### Verifikation UK1

**Urteil: PARTIALLY.** Die Zahlen stimmen. Die Zuordnung „widerspricht C3/C6" stimmt so nicht.

- **Quelle erneut geprüft** (FastMoss-Seite, lokale Kopie fm_uk.txt, Zugriff 25.09.2026): Alle 25 Handles, Follower, GMV-Werte und „Months ranked" stimmen mit Tabelle 2 überein. FastMoss nennt die Werte „estimates … conservative lower bounds" und „not official earnings" (Claimed). Die Werte sind **Kategorie-GMV**, keine Provision. Zeitraum: Jan–Jun 2026. Bias: Rabattcode NEW000, Tool-CTA.
- **Rechnung nachgerechnet** (Python): Summe 8.175.390 GBP. Rein F: 2 Konten, 131.682 GBP (1,6 %). Gemischt: 7 Konten, 985.536 GBP (12,1 %). G/H: 2 Konten, 209.048 GBP (2,6 %). Nur human-face: 13 Konten, 6.761.346 GBP (82,7 %). Unknown: 87.778 GBP (1,1 %). Hybrid in mindestens einem Beitrag: 11 Konten, 1.326.266 GBP (16,2 %). **Alles korrekt.**
- **TikTok-Stichprobe** (25.09.2026, Verified):
  - @truehealthsource: 22.600 Follower, 816 Videos. tt_media auf 7621167038211443990 (2,4 Mio. Views, isAd = true): nur Hände, Waschbecken und Produkt, Text-Overlays, kein Gesicht. **F bestätigt.**
  - @thedealshunter: tt_media auf 7678017734696848662 (237,5k Views, isAd = true): nur Hände und Kamera-Gadget. Das ASR zeigt eine spontane menschliche Stimme („uh"). **F bestätigt.**
  - @girlybeautyessentialshq: tt_media auf 7689436583837109526. Frau vor der Kamera, spricht selbst. **Human-face bestätigt.**
  - In 15 aktuellen Beiträgen dieser drei Konten war kein aigcLabelType gesetzt, und IsAigc war false.
- **Einschränkungen:**
  1. „Nur human-face" beruht auf 1–2 gesichteten Shop-Videos pro Konto. Das ist eine Obergrenze, weil einzelne faceless Posts unentdeckt bleiben können.
  2. Die 16,2 % sind das **gesamte** Konto-GMV aller Creator mit mindestens einem Hybrid-Post. Das ist eine Obergrenze für GMV aus faceless oder KI-Formaten, kein gemessener Format-Anteil. Der formatreine Anteil (rein F) liegt bei 1,6 %.
  3. A/B = 0 und kein TikTok-KI-Label bei den Top-Verkäufern.
- **Einordnung gegen die Claims:** Für UK/EU **stützt** der Befund C3 („dauerhafte vierstellige Provisionen mit KI-Content sind selten"), statt ihm zu widersprechen. Die beiden rein faceless Konten kommen geschätzt auf nur ~1,1–1,9 Tsd. EUR pro Monat, und ein KI-Avatar-Konto gibt es nicht. Zu C6 sagt der Format-Anteil nichts. Der C6-Einwand (GMV pro Video streut um den Faktor ~100) ist ein eigener Befund und stammt fast nur von human-face-Konten.
- **Korrigierte Kategorie:** top_earners_uk_format_share, stützt C3 (UK). Kein Beleg gegen C3/C6.
