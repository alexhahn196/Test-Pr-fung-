# Dossier: @xiaoyi9955 („Kitty Snug Life") – Kontrollfall (Reddit: „AI?" → reale Aufnahmen)

Zugriffsdatum: 2026-09-24 (Nachprüfung 2026-09-25). Alle Zahlen sind als **Verified** (TikTok-Public-Data via tt_profile.sh / tt_video.sh / oEmbed), **Claimed** (Fremdbehauptung) oder **Estimated** (eigene Rechnung mit Formel) gekennzeichnet.

## 1. Stammdaten (Verified)

| Feld | Wert |
|---|---|
| Username | xiaoyi9955 |
| Anzeigename | Kitty Snug Life |
| URL | https://www.tiktok.com/@xiaoyi9955 |
| Existiert | ja (statusCode 0) |
| Verifiziert (blauer Haken) | nein |
| Account erstellt | 2025-07-04 (createTime 1751610287) |
| Land | US (Claimed aus Sweep; TikTok liefert `region: null`; Inhalt englisch, US-CDN `tiktokcdn-us.com`) |
| Follower | 18.200 |
| Likes gesamt | 191.000 |
| Videos | 490 |
| Following | 0 |
| Bio | leer (keine Shop-/Showcase-Erwähnung, kein Bio-Link) |
| ttSeller | false |
| commerceUserInfo.commerceUser | false |
| Nische | Katzenspielzeug („giant Q-tips" / Riesen-Wattestäbchen), #CatTok #TikTokShopFinds |
| Modelltyp | Kontrollfall: im Forum als „AI" verdächtigt, laut früherer Gemini-Sichtung reale Kameraaufnahmen (siehe §4) |

## 2. Video-Stichprobe (Verified, tt_video.sh, Zugriff 2026-09-24/25)

n = 11 (10 neueste Videos über die öffentliche Embed-Seite + das Evidence-Video). Ältere Videos sind headless nicht listbar; WebSearch-Budget war ausgeschöpft.

| Video-ID | Datum (UTC) | Views | Likes | Kommentare | Shares | Dauer | Anchors | AI-Label (aigcLabelType) | isECVideo |
|---|---|---|---|---|---|---|---|---|---|
| 7670067930607996191 (Evidence) | 2026-08-04 | 1.600.000 | 25.000 | 86 | 1.943 | 15 s | CapCut (type 54) | null / „" | null |
| 7674658759624379678 | 2026-08-16 | 705 | 6 | 0 | 1 | 15 s | CapCut | null | null |
| 7674639016012172574 | 2026-08-16 | 577 | 8 | 0 | 0 | 15 s | CapCut | null | null |
| 7672800516560260383 | 2026-08-11 | 420 | 47 | 2 | 1 | 15 s | CapCut | null | null |
| 7672764824262118686 | 2026-08-11 | 4.094 | 28 | 0 | 1 | 15 s | CapCut | null | null |
| 7672571644535164190 | 2026-08-11 | 1.995 | 8 | 0 | 0 | 15 s | CapCut | null | null |
| 7672389712992046367 | 2026-08-10 | 2.099 | 46 | 0 | 1 | 15 s | CapCut | null | null |
| 7672279894524546335 | 2026-08-10 | 580 | 23 | 1 | 0 | 15 s | CapCut | null | null |
| 7672251730200956190 | 2026-08-10 | 3.699 | 33 | 1 | 2 | 15 s | CapCut | null | null |
| 7672146967287352607 | 2026-08-09 | 678 | 9 | 1 | 1 | 15 s | CapCut | null | null |
| 7672085165044272415 | 2026-08-09 | 1.153 | 18 | 0 | 1 | 15 s | CapCut | null | null |

Beschreibungen (Verified):
- Evidence-Video und 8 der 10 neuesten Videos tragen wortgleich: „I was NOT ready for my cat's reaction to these giant Q-tips… best random purchase ever 😭 #CatTok #CatsOfTikTok #CatToys #IndoorCat #TikTokShopFinds"
- Die zwei Videos vom 2026-08-16: „Sorry I keep posting him. He's 13 and barely plays with toys anymore—I'm just so happy seeing him act like a kitten agai[n]…" (gleiche Hashtags).
- Musik: „original sound"; isAd: false; Kommentare offen.

Auffälligkeit: identische Caption, identische Länge (15 s), identische Hashtags über ≥ 9 Uploads in 8 Tagen → Massen-Reposting/Recycling desselben Produkt-Clips (typisches Affiliate-„Spray"-Muster), unabhängig davon, ob das Rohmaterial echt ist.

## 3. Kennzahlen (Estimated aus der Stichprobe)

- Views: Ø 146.909 (n = 11, durch den Ausreißer 1,6 M verzerrt); **Median 1.153**; Max 1.600.000; Ø ohne Ausreißer 1.600 (n = 10).
- Engagement Evidence-Video: 25.000 / 1.600.000 = 1,56 % Likes/View; Shares 0,12 %.
- Upload-Frequenz: 10 Videos zwischen 2026-08-09 und 2026-08-16 (8 Tage) ≈ 1,25/Tag; Lebenszeit 490 Videos / 448 Tage (2025-07-04 → 2026-09-24) ≈ 1,1/Tag. **Letzter Upload laut Embed-Seite: 2026-08-16** → seit ca. 5–6 Wochen keine neuen Uploads (Verified über tt_recent.sh am 2026-09-25).
- Follower/Video: 18.200 / 490 ≈ 37; Likes/Video ≈ 390.

## 4. AI-Prüfung

- TikTok-AI-Label: `aigcLabelType: null`, `AIGCDescription: ""` in allen 11 Videos (Verified) → kein AI-Label gesetzt.
- Frühere Gemini-Sichtung des Evidence-Videos (aus Sweep `research/sweep_tiktok_direct.md`, Zugriff 2026-09-24): „real camera footage… Confidence High (99 %)", menschliches Voiceover, TikTok-Shop-Produktkarte sichtbar, CTA „the 6-pack is linked here ↓".
- Erneute Sichtung am 2026-09-25 nicht möglich (NexLev-Watch-Quota 15/15 erschöpft) → die Sichtungsbefunde stammen aus der Vor-Session und konnten nicht wiederholt werden.
- Reddit-Auslöser: Ein Reddit-Post fragte „Be honest, can you tell this video is AI?" und verlinkte diesen Clip (Claimed; die Post-URL wurde im Sweep nicht gespeichert und Reddit ist über WebFetch nicht erreichbar → Nicht erneut verifizierbar).
- Einstufung: **kein AI erkennbar** (Verified: kein Label; Claimed/Sichtung: reales Material). Der Fall belegt, dass Forumsverdacht „AI" bei Shop-Videos unzuverlässig ist.

## 5. Shop-Aktivität

- Verified: `commerceUser: false`, `ttSeller: false`, Bio leer, kein Bio-Link; in der API sind bei allen 11 Videos nur CapCut-Anchors (type 54) sichtbar, **kein Produkt-Anchor** in den Anchor-Feldern; `isECVideo: null`.
- Verified: Hashtag #TikTokShopFinds in allen 11 Videos; oEmbed-Titel bestätigt Hashtags.
- Claimed (Gemini-Sichtung Vor-Session): Shop-Produktkarte + CTA „the 6-pack is linked here ↓" im Video sichtbar.
- Widerspruch: Die Public-API zeigt keinen Produkt-Anchor, die visuelle Sichtung wohl. Shop-Produktkarten werden von der Headless-API nicht immer im `anchors`-Feld ausgeliefert; `commerceUser: false` ist bei reinen Affiliates (ohne eigenen Shop) üblich.
- Einstufung: **wahrscheinlich** aktiv als TikTok-Shop-Affiliate (Cat-Toy-Nische), nicht abschließend verifizierbar.

## 6. Einnahmen-Schätzung (Estimated – keine veröffentlichten GMV-Daten gefunden)

Keine Kalodata-/FastMoss-/Artikel-Quelle mit GMV für diesen Account gefunden (WebSearch-Budget ausgeschöpft; Reddit nicht abrufbar). Alles Folgende ist **Estimated**.

Formel: Monats-Views × CTR 2 % × CVR 5 % × Preis × Provision 10–20 %.
Produktannahme: Riesen-Wattestäbchen-Katzenspielzeug, 6er-Pack, typischer TikTok-Shop-Preis ~10–20 USD (Annahme, Produkt-Listing nicht verifiziert; Mittelwert 15 USD).

Szenario A – Basisbetrieb ohne Viral-Hit: Median 1.153 Views × ~33 Videos/Monat ≈ 38.000 Views (Ø ohne Ausreißer 1.600 → ≈ 53.000).
→ 53.000 × 0,02 × 0,05 = 53 Bestellungen × 15 USD ≈ 795 USD GMV → **≈ 80–160 USD Provision/Monat**.

Szenario B – Lebenszeit-Durchschnitt über Likes-Ratio: 191.000 Likes / 1,56 % ≈ 12,2 M Lebenszeit-Views / 14,5 Monate ≈ 840.000 Views/Monat.
→ 840.000 × 0,02 × 0,05 = 840 Bestellungen × 15 USD ≈ 12.600 USD GMV → **≈ 1.260–2.520 USD Provision/Monat**.

Szenario C – nur das 1,6-M-Video (Einmaleffekt): 1.600.000 × 0,02 × 0,05 = 1.600 Bestellungen × 15 USD = 24.000 USD GMV → 2.400–4.800 USD Provision (einmalig).

Zusammenfassung: GMV ≈ 0,8–12,6 k USD/Monat; Provision ≈ 80–2.500 USD/Monat; Sales ≈ 50–840/Monat – alles Estimated, Konfidenz LOW (Shop-Status nicht hart verifiziert, Produktpreis angenommen, Uploads seit 2026-08-16 gestoppt → aktuelle Einnahmen vermutlich näher an 0).

## 7. Warum es (nicht) funktioniert

- Funktioniert: Eine echte, emotionale Katzenreaktion (13-jähriger Kater spielt wieder) + Kuriositätsprodukt („giant Q-tips") + 15-s-Länge + #CatTok-Reichweite → 1,6 M Views auf einem einzigen Clip, Shares 1.943 (Weiterleitbarkeit = Discovery-Hebel).
- Funktioniert nicht: Die Reichweite ist extrem konzentriert (Median 1.153 Views; 10 von 11 Videos < 4.100). Das Recycling desselben Clips mit identischer Caption bringt fast nichts und riskiert Deduplizierung/„unoriginal content"-Einstufung. 0 Following, leere Bio, kein Link → keine Marken-/Community-Bindung; Account seit Mitte August inaktiv.
- Lehre für den Bericht: (1) Forum-„AI"-Verdacht ≠ AI; (2) auch reale UGC-Shop-Videos folgen der „1 Viral-Hit, 400 tote Uploads"-Verteilung; (3) Public-API-Anchors sind kein zuverlässiger Nachweis für Shop-Verknüpfung – visuelle Prüfung nötig.

## 8. Quellen (Zugriff 2026-09-24/25)

- https://www.tiktok.com/@xiaoyi9955 (Profil, tt_profile.sh)
- https://www.tiktok.com/embed/@xiaoyi9955 (neueste Videos, tt_recent.sh)
- https://www.tiktok.com/@xiaoyi9955/video/7670067930607996191 (Evidence-Video, tt_video.sh)
- https://www.tiktok.com/oembed?url=https://www.tiktok.com/@xiaoyi9955/video/7670067930607996191 (oEmbed, Titel/Hashtags)
- 10 Videos 7674658759624379678 … 7672085165044272415 (siehe Tabelle, tt_video.sh)
- Interne Vor-Session-Notiz: research/sweep_tiktok_direct.md §1.4 (Gemini-Sichtung, Reddit-Hinweis ohne URL)
- Nicht verfügbar: Reddit-Post-URL (nicht gespeichert, Reddit via WebFetch blockiert); Kalodata/FastMoss-GMV (nicht öffentlich verifizierbar).
