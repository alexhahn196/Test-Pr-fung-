# Dossier: @pinecommerce ("Pine Commerce")

Zugriffsdatum aller Daten: 2026-09-24 (Profil/Video-Abfragen per tt_profile.sh / tt_video.sh, TikTok-SSR-JSON). Kennzeichnung: **Verified** = direkt in TikTok-Daten gesehen; **Claimed** = Behauptung Dritter/des Inhabers; **Estimated** = eigene Rechnung mit offengelegten Inputs.

## 1. Stammdaten (Verified)

| Feld | Wert |
|---|---|
| Username / URL | pinecommerce — https://www.tiktok.com/@pinecommerce |
| Anzeigename | Pine Commerce |
| Existiert | ja (statusCode 0) |
| Bio | "Ur mom" (kein Shop-/Showcase-Hinweis, kein Bio-Link) |
| Account erstellt | 2020-12-25 (createTime 1608923063) |
| Follower | 628 |
| Likes (heartCount) | 2.958 |
| Videos | 509 |
| Following | 336 |
| verified | nein |
| ttSeller | **true** |
| commerceUserInfo.commerceUser | **true**, Kategorie "Shopping & Retail" |
| Land | US (Verified: Preisangabe "$7.99 + Free 3 Day Shipping" im Video; Reddit-Inhaber spricht von TikTok Shop/Facebook Shops/Google Shopping; region-Feld = null) |
| Modelltyp | E/F: Marken-/Seller-Account, gesichtslos, KI-generierte POV-Produktclips mit synthetischer Stimme (8–12 s) |
| Nische | Schädlingsbekämpfung (Ultraschall-Schädlingsvertreiber, Haushalt) |
| Content-Typ | 8–12-Sekunden-Produkt-Ads, "POV"-Stil, Hand hält Produktbox, Preis-Overlay, TTS-Voiceover, Hashtag #pestcontrol |

## 2. Gesampelte Videos (n = 4, Verified per tt_video.sh, 2026-09-24)

Hinweis zur Stichprobe: TikTok gibt die Videoliste nicht an Headless-Clients heraus; die WebSearch-Quote dieser Session war ausgeschöpft (200/200), DuckDuckGo/Bing/Brave/Yandex/Startpage per curl lieferten keine Treffer für site:tiktok.com/@pinecommerce. Die 4 Videos stammen aus den Reddit-Posts des Inhabers (siehe Abschnitt 4) und sind daher **vom Inhaber ausgewählte Top-Performer** – die Stichprobe ist nach oben verzerrt. 505 der 509 Videos sind nicht einsehbar.

| Video-ID | Datum (createTime) | Dauer | Views | Likes | Kommentare | Shares | Saves | Produkt-Anchor | AI-Label (aigcLabelType) | isAd | isECVideo | Hashtags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7583656838365711629 | 2025-12-21 | 8 s | 136.200 | 335 | 15 | 97 | 105 | keiner | null | true | 1 | #pestcontrol |
| 7586169769242496269 | 2025-12-29 | 12 s | 22.200 | 116 | 0 | 9 | 36 | keiner | null | true | 1 | #pestcontrol |
| 7586616961094749495 | 2025-12-31 | 8 s | 25.700 | 157 | 1 | 18 | 37 | keiner | null | true | 1 | #pestrepellent #kitchenhacks |
| 7591510508851825975 | 2026-01-04 | 8 s | 58.900 | 239 | 6 | 51 | 84 | keiner | **2 (Plattform-AI-Label)** | true | 1 | #pestcontrol |

URLs:
- https://www.tiktok.com/@pinecommerce/video/7583656838365711629
- https://www.tiktok.com/@pinecommerce/video/7586169769242496269
- https://www.tiktok.com/@pinecommerce/video/7586616961094749495
- https://www.tiktok.com/@pinecommerce/video/7591510508851825975

Kennzahlen der Stichprobe (Estimated aus n = 4): Ø 60.750 Views, Median 42.300, Max 136.200, Min 22.200. Engagement-Rate (Likes/Views) 0,25–0,6 %. Kommentare nahezu null (0–15) → typisch für beworbene Ad-Clips, nicht für organische Community-Inhalte.
Alle vier Videos tragen `isAd = true` und `isECVideo = 1` (Verified): TikTok markiert sie als beworbene E-Commerce-Videos (Promote/GMV Max). Kein Video hat einen Produkt-Anchor im Feed-Objekt; die Verkaufsverknüpfung läuft über den Seller-Status des Accounts (Shop-Tab), nicht über Affiliate-Produktkarten.

## 3. KI-Analyse

- **Verified (TikTok-Daten):** Video 7591510508851825975 trägt `aigcLabelType = 2` (von der Plattform gesetztes AI-Label); die drei anderen Videos sind nicht gelabelt (null), obwohl der Inhaber alle vier ausdrücklich als "ai videos I made programmatically with prompts" bezeichnet (Claimed, s. u.).
- **Claimed (Inhaber, Reddit, 2026-04-14):** "started generating POV-style UGC videos entirely with AI — programmatically using prompts" / "Here are some examples of ai videos I made programmatically with prompts".
- **Video-Sichtung (Gemini-Analyse aus vorheriger Sweep-Runde, Datei research/sweep_tiktok_direct.md, zu Video 7591510508851825975):** Stimme = "AI-generated (95 % confidence) … synthetic text-to-speech"; Bildmaterial = "Real (90 %) … real hand holding the product box"; Produkt "Multifunction Ultrasonic Pest Repeller"; On-Screen "$7.99 + Free 3 Day Shipping"; Hook "This device removed rodents from my home"; keine sichtbare AI-Kennzeichnung im Bild.
  Eine erneute Sichtung von 1–2 weiteren Videos war in dieser Runde nicht möglich: NexLev-Tool `watch_tiktok_video_and_ask` meldete "RATE LIMIT EXCEEDED 15/15 calls in 24 h". Struktur/CTA/Schnittzahl der übrigen Videos daher **nicht öffentlich verifizierbar** in dieser Runde.
- **Einordnung ai_level: teilweise AI** – synthetische Stimme + Plattform-AI-Label auf einem Video sind belegt; das Bildmaterial wirkt laut Sichtung real (bzw. fotorealistisch generiert – der Inhaber nennt es KI-generiert). "vollständig AI" nur als Claimed.

## 4. Shop-Aktivität

| Indikator | Befund |
|---|---|
| ttSeller | true (Verified) |
| commerceUser | true, "Shopping & Retail" (Verified) |
| Bio-Hinweis auf Shop | nein ("Ur mom") |
| Produkt-Anchors in Videos | keine in allen 4 Samples |
| #tiktokshop-Hashtags | keine; nur #pestcontrol, #pestrepellent, #kitchenhacks |
| isAd / isECVideo | true / 1 auf allen 4 Videos (Verified) |
| Rolle | **Eigener Seller/Brand-Shop**, kein Affiliate (Claimed: "I run a small TikTok Shop store", "Cut 30–50 affiliates") |

**shop_active = ja** (Seller-Flags + E-Commerce-Videos + Preis-Overlay + Inhaberaussage).

Produkt (Verified per Video-Sichtung + Claimed): Multifunktions-Ultraschall-Schädlingsvertreiber, $7,99 inkl. "Free 3 Day Shipping". Preisspanne: ~$8 (Einzelprodukt, Low-Ticket).

## 5. Einkommensbehauptungen (Claimed) und Quellen

Autor "Life-Programmer7808" (Reddit), vier nahezu identische Posts am 2026-04-14 (Zugriff über zwischengespeicherte JSON-Dateien research/reddit/*.json und research/sweep/post_1skyy9f.json, da reddit.com in dieser Session 403/"unable to fetch" lieferte):

1. r/googleads "AI-generated UGC is outperforming my paid creative. Not even close." — https://www.reddit.com/r/googleads/comments/1sl02pq/aigenerated_ugc_is_outperforming_my_paid_creative/ (2 Upvotes)
   > "$200–$300+/day in revenue, purely organic · Some videos hitting 100K+ views, zero ad spend · Working across TikTok Shop, Facebook Shops, Google Shopping, and YouTube Shorts … Cut 30–50 affiliates who were either making garbage content or just taking free product and ghosting · Production cost is practically nothing compared to $150–$300 per UGC creator video"
   > "100K views: …/video/7583656838365711629 — 31.5K views: …/video/7591510508851825975"
2. r/PPC, gleicher Text — https://www.reddit.com/r/PPC/comments/1sl00yw/ (2 Upvotes, Ratio 0,75)
3. r/FacebookAds "$200–$300/day from AI-generated UGC videos. Felt like I had to share this." — https://www.reddit.com/r/FacebookAds/comments/1skzto9/ (1 Upvote, Ratio 0,6)
   > "A single batch is pulling in $200–$300+ per day in revenue. … I'm still a small brand so my volume is limited"
4. r/TikTokShopAffiliate "Ai Videos on TikTok Shop Making $200-$300+ per day." — https://www.reddit.com/r/TikTokShopAffiliate/comments/1skyy9f/ (1 Upvote, 1 Kommentar)
   > "I have a tiktok store called pinecommerce feel free to search it up. … A batch of my ai videos POV style have generated $100+ a day. I just wanted to know if anyone would be interested in such a service I could do for their store … Please dm"
   (Hier nennt er nur "$100+ a day" und bietet den Dienst zum Verkauf an → Werbe-/Lead-Motiv.)

Widersprüche (Verified vs. Claimed):
- "purely organic / zero ad spend" ↔ alle vier verlinkten Videos sind `isAd = true` (beworben) – **die TikTok-Daten widersprechen der Organik-Behauptung**.
- Die Views sind seit April gestiegen (Claimed 100K/31,5K/25K/21K → Verified 136,2K/58,9K/25,7K/22,2K), d. h. die Zahlen der Videos selbst sind plausibel; das Umsatzbild ist es nicht belegbar.
- 509 Videos bei 628 Followern seit 2020 → praktisch kein Follower-Aufbau; Reichweite ist eingekauft/gepusht, nicht organisch.
- Kein Kalodata/FastMoss-Screenshot, kein Dashboard, keine Drittquelle. GMV/Umsatz: **Nicht öffentlich verifizierbar.**

## 6. Upload-Frequenz (Estimated)

- Stichprobe: 4 Videos zwischen 2025-12-21 und 2026-01-04 (15 Tage) – nur die vom Inhaber genannten, Frequenz daraus nicht ableitbar.
- Account-Alter 2020-12-25 → 2026-09-24 ≈ 69 Monate; 509 Videos / 69 Monate ≈ **7,4 Videos/Monat** im Schnitt. Da der Inhaber von "Batches" programmatisch erzeugter Videos spricht, ist ein Großteil vermutlich seit Ende 2025 in Schüben hochgeladen worden (Claimed/Estimated; nicht verifizierbar).

## 7. Umsatz-/Einkommensschätzung (Estimated – keine Fakten)

Formel: monatliche Views × CTR 2 % × CVR 5 % × Preis × Marge (Eigenmarke: keine Affiliate-Provision, sondern Bruttomarge).
Inputs:
- Preis: $7,99 (Verified On-Screen)
- Views/Monat: unbekannt. Die Stichprobe (Ø 60.750) ist inhaberselektiert; 505 Videos ungesehen. Szenarien: 30 Uploads/Monat × 2.000 Views (niedrig) = 60.000 bis 30 × 20.000 Views (hoch) = 600.000 Views/Monat.
- Bestellungen = Views × 0,02 × 0,05 = Views × 0,001 → 60–600 Bestellungen/Monat
- GMV = Bestellungen × $7,99 → **≈ $480 – $4.800/Monat (Estimated)**
- Marge des Sellers (statt Provision) bei angenommen 40–60 % nach Warenkosten/Versand/TikTok-Gebühr (~6–9 %) → **≈ $190 – $2.900/Monat (Estimated)**; abzüglich Ad-Spend (isAd = true, Höhe unbekannt).
- Vergleich mit Claim: $200–300/Tag ≈ $6.000–9.000/Monat GMV läge beim 1,3- bis 19-fachen der Schätzung; nur erreichbar, wenn nahezu jedes der ~30 Monatsvideos sechsstellige Views hätte oder erheblicher Ad-Spend fließt. **income_confidence = LOW.**

Provision (commission_est): nicht anwendbar – Brand-Seller verdient Marge, keine Affiliate-Provision.

## 8. Warum es funktioniert / nicht funktioniert

Funktioniert (teilweise): Extrem kurze (8–12 s) Produktclips mit Preis-Hook ("$7.99 + Free 3 Day Shipping"), Problem-Lösung-Hook ("This device removed rodents from my home"), Low-Ticket-Impulsprodukt, massenhaft variierbar per Prompt-Pipeline; Reichweite über bezahlte Distribution (isAd) statt Community. Vier verlinkte Videos erreichen 22K–136K Views.
Funktioniert nicht / Risiken: 628 Follower nach 509 Videos = kein organischer Asset-Aufbau; Kommentare ≈ 0; nur 1 von 4 Videos AI-gelabelt trotz eigener Aussage "entirely with AI" → Verstoß gegen TikToks Kennzeichnungspflicht möglich; Umsatzclaims stammen ausschließlich vom Inhaber, der gleichzeitig den Service verkauft ("Please dm"); Posts haben 1–2 Upvotes, keine externe Bestätigung. Als Nachweis für "AI-Videos → $200–300/Tag organisch" ist der Account **nicht belastbar**, als Beispiel für das Modell F (gesichtslose KI-Ad-Massenproduktion eines Sellers) aber verifiziert.

## 9. Datenqualität

- data_quality: **Verified profile+videos** (Profil + 4 Videos live geprüft; Stichprobe klein und inhaberselektiert).
- Nicht erreichbar in dieser Runde: Videoliste (TikTok-API), WebSearch (Quote 200/200 erschöpft), reddit.com live (403), NexLev-Videosichtung (Rate-Limit 15/15).

## 10. Quellen

- https://www.tiktok.com/@pinecommerce (Profil-JSON, 2026-09-24)
- https://www.tiktok.com/@pinecommerce/video/7583656838365711629 (2026-09-24)
- https://www.tiktok.com/@pinecommerce/video/7586169769242496269 (2026-09-24)
- https://www.tiktok.com/@pinecommerce/video/7586616961094749495 (2026-09-24)
- https://www.tiktok.com/@pinecommerce/video/7591510508851825975 (2026-09-24)
- https://www.reddit.com/r/googleads/comments/1sl02pq/aigenerated_ugc_is_outperforming_my_paid_creative/ (Cache, Post vom 2026-04-14)
- https://www.reddit.com/r/PPC/comments/1sl00yw/ (Cache, 2026-04-14)
- https://www.reddit.com/r/FacebookAds/comments/1skzto9/ (Cache, 2026-04-14)
- https://www.reddit.com/r/TikTokShopAffiliate/comments/1skyy9f/ai_videos_on_tiktok_shop_making_200300_per_day/ (Cache, 2026-04-14)
- research/sweep_tiktok_direct.md (frühere Gemini-Videosichtung, 2026-09-24)
