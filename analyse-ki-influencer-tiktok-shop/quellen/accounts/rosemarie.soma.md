# Dossier: @rosemarie.soma (rose soma • journals)

Zugriffsdatum aller Quellen: 2026-09-24 / 2026-09-25. Alle Zahlen sind gekennzeichnet als **Verified** (direkt aus öffentlichen TikTok-Daten bzw. Primärquelle), **Claimed** (Behauptung Dritter) oder **Estimated** (eigene Rechnung mit Formel).

## 1. Kurzfazit

- Der Account existiert (**Verified**), ist aber ein **menschlicher Junk-Journal-/Bastel-Account** (Zweitaccount der US-Creatorin Rose(marie) Soma), **kein AI-/Faceless-TikTok-Shop-Account**.
- Die Presse-Erwähnung (Analytics Insight, 16.07.2026) zitiert "Affiliate creator Rosemarie Soma" als Kritikerin von AI-Shopping-Videos. Handle, Land und Followerzahl werden dort **nicht** genannt; die Zuordnung zum Handle @rosemarie.soma ist plausibel (Instagram-Handle @rosemarie.soma laut Bio, Amazon-Associates-Tag `rosemariesoma-20` im Linktree), aber **nicht durch die Quelle selbst belegt**.
- Ländervermerk "UK" aus dem Sweep ist **vermutlich falsch**: Alle Indizien (Amazon.com-Affiliate-Tag, `rosesomallc@gmail.com`, US-Affiliate-Netzwerke impact.com/sjv.io, tiktokcdn-**us** CDN, Whatnot) sprechen für **USA** (Estimated/abgeleitet, nicht verifiziert).
- **Kein Video-Sample möglich**: TikTok liefert die Videoliste nicht an Headless-Clients, das WebSearch-Budget der Session war erschöpft, Bing/DDG/Yandex/Google-Fallbacks lieferten CAPTCHAs bzw. irrelevante Treffer, tikwm/urlebird 403. → data_quality = **Verified profile only**.
- Für den Bericht: **nur als Presse-Lead / Gegenposition** ("menschliche Affiliates fühlen sich von AI-Videos verdrängt") verwenden, nicht als Beispiel-Account fürs AI-Modell.

## 2. Profildaten (Verified, tt_profile.sh, 2026-09-25)

| Feld | @rosemarie.soma (Zweitaccount) | @rosesoma (Hauptaccount) |
|---|---|---|
| Nickname | rose soma • journals | rose soma |
| Bio | "we junk journal here 🤍 / main/old journal account: @rose soma / IG: @rosemarie.soma" | "collabs: rosesomallc@gmail.com / @rose soma • journals" |
| Follower | 24.500 | 120.800 |
| Likes (heartCount) | 3.000.000 | 14.700.000 |
| Videos | 39 | 7.491 |
| Following | 5 | 1.059 |
| Account erstellt (createTime) | 1768060680 = 2026-01-10 | 1611947329 = 2021-01-29 |
| verified | false | false |
| ttSeller | false | false |
| commerceUserInfo.commerceUser | **false** | **false** |
| bioLink | – | https://linktr.ee/rosesoma |
| privateAccount | false | – |
| region | null (nicht öffentlich) | null |

Weitere geprüfte Handles: @rose.soma (17 Follower, 0 Videos, statusCode 10222 = privat/leer), @rose_soma (8 Follower, 0 Videos) – irrelevant.

## 3. Linktree des Hauptaccounts (Verified, https://linktr.ee/rosesoma, 2026-09-25)

Enthält u. a.: Amazon-Affiliate-Links mit Tag `tag=rosemariesoma-20` (Amazon Associates **US**), amzn.to-Kurzlinks, impact.com/sjv.io-Affiliate-Links (Fabletics, Headspace, Babbel, Daily Harvest, Gobble, Purple Carrot, Maev), Rabattcodes (menminmade.com/discount/ROSE, paperwrld.com/?ref=ROSESOMA, grabieart.com/ROSESOMA, boxofknots.com/?club=Rosesoma), Whatnot-Link, Instagram https://instagram.com/rosemarie.soma, Pinterest "rose soma | crafts & junk journaling (rosesoma)".
→ Bestätigt: Rose Soma ist eine **Affiliate-Creatorin** (Amazon Associates + Impact-Netzwerke). Eine TikTok-Shop-Affiliate-Aktivität ist damit **nicht** belegt (commerceUser=false auf beiden Accounts, kein Showcase-Hinweis in Bio).

## 4. Presse-Quelle (Claimed)

- Analytics Insight, "TikTok Faces UK Probe Over Child Safety Checks and AI Shopping Videos", 16.07.2026, https://www.analyticsinsight.net/news/tiktok-faces-uk-probe-over-child-safety-checks-and-ai-shopping-videos (abgerufen 2026-09-24/25).
- Wörtlicher Absatz: "Some creators say the automated videos compete with reviews made by people who own and test the products. Affiliate creator Rosemarie Soma said she produces advertisements using physical products. She said it is 'very frustrating' when AI videos receive advertising support and generate sales."
- Weitere Zahlen im Artikel (Claimed): Ofcom-Bußgeld "up to £18 million or 10% of TikTok's qualifying worldwide revenue, whichever amount is higher"; Affiliate-Creator laut Charm.io 2,3 Mio. (2024) → 11,3 Mio. (2026).
- Der Artikel nennt **keinen** TikTok-Handle, keine Followerzahl, kein Land und keine Originalquelle für das Zitat.

## 5. Video-Sample

**Nicht möglich.** Versuchte Wege (alle 2026-09-25):
- Profilseite SSR-JSON: `itemList: []` (TikTok liefert keine Videoliste an Headless-Clients); r.jina.ai-Render zeigt "Something went wrong".
- TikTok-internes `api/post/item_list` (mit secUid): leere Antwort; `node/share/user`: 403.
- WebSearch: Session-Budget (200/200) erschöpft. Bing/Google/DuckDuckGo/Yandex/Startpage per WebFetch: CAPTCHA, leer oder irrelevante Treffer.
- tikwm.com: 403 (Cloudflare); urlebird.com: 403; TikTok-Discover-/Tag-Seiten: keine Treffer.

| Video-ID | Datum | Views | Likes | Kommentare | Anchors (Shop) | AI-Label |
|---|---|---|---|---|---|---|
| – | – | – | – | – | – | – |

n_videos_sampled = 0. Kein Video wurde angeschaut (watch_tiktok_video_and_ask nicht anwendbar ohne URL).

## 6. Metriken (abgeleitet aus Profildaten)

- Upload-Frequenz (Estimated): 39 Videos / ~8,5 Monate (10.01.2026 – 25.09.2026) ≈ **4,6 Videos/Monat** (≈ 1/Woche). Hauptaccount: 7.491 Videos / ~68 Monate ≈ 110/Monat (Claimed aus videoCount; enthält vermutlich viele Kurzclips/Slideshows).
- Likes pro Video (Estimated): 3,0 Mio. / 39 ≈ **77.000 Likes/Video** – ungewöhnlich hoch für 24,5k Follower → Hinweis auf einzelne virale Videos; ohne Sample nicht prüfbar.
- Views: **Nicht öffentlich verifizierbar** (kein Sample). Grobe Ableitung (Estimated): bei typischen Like-Raten von 5–10 % → ≈ 30–60 Mio. Lifetime-Views ≈ 3,5–7 Mio. Views/Monat. Sehr unsicher.

## 7. Einkommensschätzung (Estimated, LOW)

Keine Quelle publiziert GMV/Sales für diesen Account (Kalodata/FastMoss nicht abgerufen; kein Screenshot, keine Zahl im Artikel).

Hypothetische Rechnung **nur zur Einordnung**, falls der Account TikTok-Shop-Affiliate wäre (ist er laut commerceUser=false derzeit **nicht**):
- Inputs: 3,5–7 Mio. Views/Monat (Estimated s. o.) × CTR 2 % × CVR 5 % × Ø-Preis 15 USD (Bastel-/Journaling-Supplies) × Provision 10–20 %.
- Bestellungen: 3,5–7 Mio. × 0,02 × 0,05 = 3.500–7.000/Monat → GMV ≈ 52.500–105.000 USD/Monat → Provision ≈ **5.000–21.000 USD/Monat**.
- **Realistische Einordnung:** Da beide Accounts keinen TikTok-Shop-Commerce-Status haben, ist die TikTok-Shop-Provision **wahrscheinlich ~0**. Tatsächliche Affiliate-Einnahmen laufen (laut Linktree) über Amazon Associates (i. d. R. 1–4 % Provision, Sales nicht verifizierbar) und Impact-Programme. Insgesamt: **Nicht öffentlich verifizierbar.**

## 8. AI-Einstufung

- Keine Videos gesichtet → kein direkter Nachweis. Indizien: Presse beschreibt sie als Creatorin, die "advertisements using physical products" produziert und AI-Videos kritisiert; Nische Junk Journaling ist handwerklich (Hände/Papier vor Kamera). Einstufung: **kein AI erkennbar** (indirekt, LOW confidence).

## 9. Bewertung: Warum relevant / warum nicht

- Relevant als **Presse-Lead**: Zeigt die Gegenposition menschlicher Affiliates zur AI-Video-Welle und den regulatorischen Kontext (Ofcom-Probe, AI-Shopping-Videos) in UK.
- Nicht relevant als **Modell-Account**: menschlich, Bastel-Nische, kein TikTok-Shop-Flag, Zweitaccount mit 39 Videos. Für das AI-/Faceless-Modell des Berichts liefert er keine Benchmark-Daten.
- Datenqualität: Verified profile only; Zuordnung Person↔Handle plausibel (Instagram-Handle + Amazon-Tag "rosemariesoma"), aber nicht durch die Presse-Quelle selbst bestätigt.

## 10. Quellen

1. https://www.tiktok.com/@rosemarie.soma – Profil-SSR-Daten via tt_profile.sh (2026-09-25)
2. https://www.tiktok.com/@rosesoma – Profil-SSR-Daten via tt_profile.sh (2026-09-25)
3. https://linktr.ee/rosesoma (2026-09-25)
4. https://www.analyticsinsight.net/news/tiktok-faces-uk-probe-over-child-safety-checks-and-ai-shopping-videos (2026-09-24/25)
5. https://pin.it/7vYq3M6DG → Pinterest-Profil "rose soma | crafts & junk journaling (rosesoma)" (2026-09-25)
6. https://instagram.com/rosemarie.soma (nur als Link im Linktree/Bio; Inhalt nicht abrufbar, 302)
