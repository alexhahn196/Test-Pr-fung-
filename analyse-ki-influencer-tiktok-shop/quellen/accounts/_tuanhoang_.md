# Dossier: @_tuanhoang_ („Lại là Tuấn đây") — TikTok-Shop-Agentur Vietnam

Zugriffsdatum: 2026-09-24 / 2026-09-25 (Wiederholungslauf). Alle Zahlen sind als **Verified** (in TikTok-Rohdaten gesehen), **Claimed** (Behauptung Dritter/frühere Sweep-Notiz) oder **Estimated** (eigene Rechnung, Formel angegeben) markiert.

## 1. Kurzfazit

- Der Account existiert und ist öffentlich: Profil-JSON (statusCode 0) am 2026-09-25 abgerufen.
- Es handelt sich um einen **echten Menschen** (Tuấn, CEO „TN Holding"), der als **Agentur/Dienstleister** für TikTok-Shop-Betreiber in Vietnam auftritt (Shop-Betrieb, Ads, KOC-Booking, blauer Haken für Unternehmen). Er verkauft u. a. das **Erstellen von „A.I-Verkaufsvideos"** als Leistung bzw. erklärt in Tutorials, wie Affiliates solche Videos selbst bauen.
- **Kein AI-Avatar-Account.** Das Beweisvideo zeigt laut Thumbnail (heruntergeladen und gesichtet) einen realen Sprecher mit Mikrofon; AI ist hier das *Thema/Produkt*, nicht die Produktionsmethode des Accounts.
- **Kein eigener TikTok Shop**: `ttSeller false`, `commerceUser false`, kein Shop-Link in der Bio. Monetarisierung läuft über Agenturdienstleistungen (nicht öffentlich verifizierbar).
- Datenlage heute eingeschränkt: Das Beweisvideo liefert am 2026-09-25 `statusCode 10204 / filter_by_account_aom` (regionale/Account-Filterung für Headless-Clients); die Videometriken stammen aus dem Sweep vom 2026-09-24 (gleiches Tool). Weitere Video-URLs konnten nicht ermittelt werden (WebSearch-Budget erschöpft; Embed-Seite liefert leere `itemList`; Bing/DDG über den Proxy unbrauchbar).

## 2. Profil (Verified, tt_profile.sh, 2026-09-25)

| Feld | Wert | Status |
|---|---|---|
| Handle | `_tuanhoang_` | Verified |
| URL | https://www.tiktok.com/@_tuanhoang_ | Verified |
| Anzeigename | „Lại là Tuấn đây" | Verified |
| Bio | „CEO TN Holding ✅ / Đối tác chính thức của Tiktokshop Việt Nam 🇻🇳 / Hỗ trợ vận hành shop - chạy ads - booking KOC / Lên tích xanh cho doanh nghiệp" (dt.: CEO TN Holding; offizieller Partner von TikTok Shop Vietnam; Unterstützung bei Shop-Betrieb, Ads, KOC-Booking; blauer Haken für Unternehmen) | Verified |
| Follower | 466.900 | Verified |
| Likes (heartCount) | 5.600.000 | Verified |
| Videos | 1.015 | Verified |
| Following | 12 | Verified |
| Account erstellt | createTime 1558605666 = 2019-05-23 | Verified |
| Verifiziert (blauer Haken) | nein | Verified |
| ttSeller | false | Verified |
| commerceUserInfo.commerceUser | false | Verified |
| bioLink | keiner | Verified |
| Land | Vietnam (Sprache, Bio „Tiktokshop Việt Nam", region-Feld null) | Verified (indirekt) |
| Modelltyp | E/G: Agentur/Dienstleister (Shop-Operations, Ads, KOC), verkauft/zeigt AI-Produktvideos als Service | Einschätzung |
| Nische | TikTok-Shop-Operations, E-Commerce-Coaching, AI-Video-Tutorials | Einschätzung |

Quelle: https://www.tiktok.com/@_tuanhoang_ (Profil-SSR-JSON, 2026-09-25).

## 3. Gesampelte Videos (n = 1)

| Video-ID | Datum | Views | Likes | Kommentare | Shares | Dauer | Anchors | AI-Label | isAd / isECVideo | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 7508722889999256839 | 2025-05-26 | 32.100 | 773 | n/a | n/a | 70 s | CapCut (App-Anchor, **kein Produkt-Anchor**) | keiner (aigcLabelType nicht gesetzt) | isAd true / isECVideo 1 | Verified am 2026-09-24 (Sweep-Notiz); am 2026-09-25 nur noch per oEmbed bestätigt (Titel, Autor), Metriken heute nicht abrufbar (`10204 filter_by_account_aom`) |

- URL: https://www.tiktok.com/@_tuanhoang_/video/7508722889999256839
- Beschreibung (Verified via oEmbed 2026-09-25): „Cách làm video A.I bán hàng, làm affiliate kiếm thêm thu nhập, bằng mẫu tuỳ chọn của chính các bạn luôn #lailatuanday #theanh28 #affiliate #ai" (dt.: „Wie man A.I-Verkaufsvideos macht, als Affiliate Zusatzeinkommen verdient — mit euren eigenen frei wählbaren Vorlagen").
- Hashtags: #lailatuanday #theanh28 #affiliate #ai — **kein** #tiktokshop / #tiktokshopfinds.
- Musik: „nhạc nền - Lại là Tuấn đây" (Originalton des Creators).
- Thumbnail (gesichtet, lokal gespeichert: `research/accounts/tuanhoang_thumb_7508722889999256839.jpg`): realer Mann mit Brille, Podcast-Mikrofon, Neon-„hello"-Schild, Bilderrahmen im Hintergrund; Text-Overlay „Cách tạo VIDEO AI KIẾM THÊM THU NHẬP" („Wie man AI-Videos erstellt, um Zusatzeinkommen zu verdienen"). Talking-Head-Format.
- Interpretation der Flags: `isAd true` + `isECVideo 1` = das Video wurde als Werbung/Promoted-Post markiert bzw. gehört zum E-Commerce-Kontext (Anzeigenbudget dahinter wahrscheinlich; die 32.100 Views sind also **nicht** rein organisch).

Weitere Video-URLs: **nicht ermittelbar** (siehe Abschnitt 8). Die Embed-Seite https://www.tiktok.com/embed/@_tuanhoang_ liefert `itemList: []`; die einzige extrahierte ID (6632607371364433922) ist die User-ID, kein Video.

## 4. Video-Sichtung (Schritt 3)

`mcp__NexLev__watch_tiktok_video_and_ask` konnte **nicht** ausgeführt werden: Tageskontingent erschöpft (15/15 Aufrufe, Fehlermeldung „RATE LIMIT EXCEEDED" am 2026-09-25). Ersatz: Thumbnail-Sichtung (siehe oben) + oEmbed-Metadaten.

Ergebnis der Ersatzprüfung:
- Person: **realer Mensch** (Thumbnail; Studio-Setup mit Mikrofon; konsistent mit Bio „CEO TN Holding"). Nicht öffentlich verifizierbar: Stimme (synthetisch vs. echt) — angesichts Originalton „nhạc nền - Lại là Tuấn đây" und Talking-Head-Format sehr wahrscheinlich echte Stimme.
- AI-Label: kein `aigcLabelType` im Datensatz vom 2026-09-24.
- Hook: Text-Overlay „Cách tạo VIDEO AI KIẾM THÊM THU NHẬP" (Einkommensversprechen als Aufhänger). Gesprochener Hook: nicht öffentlich verifizierbar (kein Watch möglich).
- Länge: 70 s. Struktur/Cuts/CTA/Shop-Karte: nicht öffentlich verifizierbar; kein Produkt-Anchor, daher keine TikTok-Shop-Produktkarte im Video-Datensatz.
- Gezeigtes Produkt: kein physisches Produkt; beworben wird das Know-how/der Service „AI-Verkaufsvideos" (CapCut-Anchor deutet auf CapCut-AI-Vorlagen als genutztes Tool hin).

## 5. AI-Einstufung

- **ai_level: „kein AI erkennbar"** (für den Account selbst). Begründung: realer Sprecher, Originalton, kein AI-Label. AI kommt nur als *Inhalt/Dienstleistung* vor (Tutorial „Cách làm video A.I bán hàng").
- Relevanz für die Studie: Beleg aus der Agenturperspektive, dass „AI-Produktvideos für Affiliate/Shop" im vietnamesischen TikTok-Shop-Ökosystem 2025 als Standardleistung vermarktet werden (Video mit Ad-Budget beworben, isAd true).

## 6. Shop-Aktivität

| Indikator | Befund |
|---|---|
| ttSeller | false (Verified) |
| commerceUser | false (Verified) |
| Bio | Agenturleistungen, kein Showcase/Shop-Hinweis auf eigene Produkte (Verified) |
| Produkt-Anchors im Sample | keine; nur CapCut-App-Anchor (Verified 2026-09-24) |
| #tiktokshop-Hashtags | keine im Sample (Verified) |
| Artikel/Drittquellen zu Affiliate-Status | keine gefunden (Suche nicht möglich, s. Abschn. 8) |

**shop_active: „nein"** — kein eigener Shop/Showcase; der Account monetarisiert als B2B-Dienstleister (Ads, Shop-Operations, KOC-Booking, Verifizierungsservice). Umsätze daraus: **Nicht öffentlich verifizierbar.**

## 7. Kennzahlen und Schätzungen

Sample: n = 1 → avg = median = max = 32.100 Views (Verified 2026-09-24, aber beworbenes Video, daher nach oben verzerrt).

Upload-Frequenz (Estimated): 1.015 Videos / (2019-05-23 bis 2026-09-24 ≈ 88 Monate) ≈ **11,5 Videos/Monat ≈ 2,7/Woche** (Lebenszeit-Durchschnitt; aktuelle Frequenz nicht ermittelbar, da keine Videoliste).

Affiliate-Einkommensschätzung (nur als Rechenübung, **passt nicht zum Geschäftsmodell**, da kein Shop/Affiliate-Anchor):
- Monatliche Views (Estimated) = 32.100 × 11,5 ≈ 369.000 (extrem unsicher: n = 1, Ad-geboostet).
- Klicks = 369.000 × CTR 2 % = 7.380; Bestellungen = 7.380 × CVR 5 % ≈ 369/Monat.
- Typischer Warenkorb TikTok Shop VN (Annahme): 150.000–300.000 VND ≈ 6–12 USD.
- GMV (Estimated) ≈ 369 × 6–12 USD ≈ **2.200–4.400 USD/Monat**.
- Provision 10–20 % (Estimated) ≈ **220–885 USD/Monat**.
- Realistische Aussage: Da keine Produkt-Anchors existieren, liegt das Affiliate-Einkommen aus TikTok Shop vermutlich bei **~0**; das tatsächliche Einkommen stammt aus Agenturhonoraren und ist **nicht öffentlich verifizierbar**. income_confidence: **LOW**.

Keine Kalodata/FastMoss-Zahlen oder Dashboards gefunden (Claimed-Quellen: keine).

## 8. Methodik, Grenzen, Quellen

- `tt_profile.sh _tuanhoang_` (2026-09-25): statusCode 0, Daten wie oben.
- `tt_recent.sh _tuanhoang_` (2026-09-25): keine Videos (Embed `itemList` leer).
- `tt_video.sh 7508722889999256839` (2026-09-25): `{"statusCode": 10204, "statusMsg": "filter_by_account_aom"}` → Video für Headless-/Auslandsclients gefiltert; Metriken vom 2026-09-24 (Sweep `research/sweep_tiktok_direct.md`, Abschnitt zu `_tuanhoang_`) übernommen.
- oEmbed https://www.tiktok.com/oembed?url=https://www.tiktok.com/@_tuanhoang_/video/7508722889999256839 (2026-09-25): bestätigt Existenz, Titel, Hashtags, Autor, Musik.
- Thumbnail-Download und Sichtung (2026-09-25).
- WebSearch: Budget erschöpft (200/200). Bing (HTML + RSS) und DuckDuckGo über den Proxy: keine verwertbaren Ergebnisse (DDG-Captcha; Bing lieferte themenfremde Treffer). TikTok-Tag-Seiten (#lailatuanday, #theanh28) und Musik-Seite: keine Video-IDs extrahierbar (JS-gerendert).
- NexLev-Watch-Tool: Tageslimit erreicht.
- Folge: **data_quality = „Verified profile+videos" mit n = 1** (Profil live verifiziert; ein Video mit Metriken aus dem Vortag, heute nur per oEmbed bestätigt). Für ein belastbares Bild wären ≥ 5 Videos nötig — Empfehlung: erneuter Lauf mit WebSearch-Budget oder aus Vietnam-IP.

Evidenz-URLs:
- https://www.tiktok.com/@_tuanhoang_
- https://www.tiktok.com/@_tuanhoang_/video/7508722889999256839
- https://www.tiktok.com/oembed?url=https://www.tiktok.com/@_tuanhoang_/video/7508722889999256839
