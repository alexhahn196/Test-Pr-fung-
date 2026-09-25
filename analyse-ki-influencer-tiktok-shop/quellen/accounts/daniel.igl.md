# Dossier: @daniel.igl (TikTok) – Daniel Igl

Zugriffsdatum aller Quellen: 2026-09-24. Kennzeichnung: **Verified** = in TikTok-Rohdaten / Primärquelle gesehen, **Claimed** = Behauptung Dritter/des Creators, **Estimated** = eigene Schätzung mit Formel.

## 1. Steckbrief (Profil)

| Feld | Wert | Status |
|---|---|---|
| Username | daniel.igl | Verified |
| Anzeigename | Daniel Igl | Verified |
| TikTok-URL | https://www.tiktok.com/@daniel.igl | Verified (statusCode 0) |
| Existiert | ja | Verified |
| Land | DE (Impressum daniel-igl.de: Holzkirchen, Bayern; TikTok `region` = null) | Verified (Impressum) |
| Bio | „💡 Komplette Videos auf meinem YT Kanal "Daniel Igl"“ | Verified |
| Bio-Link | keiner | Verified |
| Follower | 102 | Verified |
| Following | 0 | Verified |
| Likes (heartCount) | 3.519 | Verified |
| Videos | 62 | Verified |
| Account erstellt | 2025-01-02 (createTime 1735848678) | Verified |
| Verifiziert | nein | Verified |
| ttSeller | false | Verified |
| commerceUserInfo.commerceUser | false | Verified |
| Modell-Typ | D (Creator/Coach-Funnel: TikTok als Zubringer zu YouTube → Gratis-Workshop → Beratungsgespräch/Coaching) | Einordnung |
| Nische | Online-Geld-verdienen / KI-Business-Coaching (deutsch) | Verified (Bio, YouTube-Beschreibung) |
| Content-Typ | Kurz-Clips des eigenen YouTube-Coachings (Person Daniel Igl vor Kamera laut YT-Kanal; Bio verweist auf „komplette Videos“ auf YT) | Ableitung, siehe Einschränkung unten |

Zweitaccount desselben Betreibers (Vergleich): **@igldaniel** „Daniel Igl | Business tipps“, 1.761 Follower, 11.200 Likes, 93 Videos, erstellt 2019-10-29, Bio-Link https://danieligl.de/gratis-training/, ttSeller false, commerceUser false (Verified, tt_profile.sh). Die YouTube-Beschreibung des Belegvideos verlinkt als TikTok ausschließlich @igldaniel, nicht @daniel.igl.

## 2. Video-Sample

**Ergebnis: Es konnte keine einzige Video-URL von @daniel.igl gefunden werden.**

Versuchte Wege (alle 2026-09-24):
- WebSearch: `site:tiktok.com/@daniel.igl`, `"@daniel.igl"`, `tiktok.com/@daniel.igl/video`, `"daniel.igl" tiktok video KI` → nur Treffer für @igldaniel und fremde Accounts.
- Bing/DuckDuckGo direkt (curl) mit `"tiktok.com/@daniel.igl/video"` → 0 Video-URLs.
- Profil-HTML (SSR-JSON): `itemList: []`, kein ItemModule; im HTML gefundene 19-stellige IDs sind keine Videos (tt_video.sh → 10204 „item doesn't exist“ für alle 12 getesteten IDs).
- TikTok `api/post/item_list` mit secUid → HTTP 200, leerer Body (headless blockiert).
- TikTok-Discover-Seite „daniel-igl-erfahrung“ → ohne JS keine Inhalte.
- Belegvideo (YouTube xnbooWSc6Ko) zeigt keine Videos/Statistiken von @daniel.igl (siehe Abschnitt 3).

Video-Tabelle (id, Datum, Views, Likes, Kommentare, Anchors, AI-Label): **leer – n = 0.** Views, Anchors und AIGC-Labels: Nicht öffentlich verifizierbar.

Damit: `data_quality = Verified profile only`. Ein Sichten mit watch_tiktok_video_and_ask war ohne Video-URL nicht möglich.

## 3. Belegvideo (YouTube) – Inhalt und Aussagen

Quelle: https://www.youtube.com/watch?v=xnbooWSc6Ko – „So verdiene ich online Geld mit KI TikTok Videos (Ohne Gesicht)“, Kanal Daniel Igl (UC0Ry_26cQ2hMzo_O7Iu7Reg, 17.900 Abonnenten), veröffentlicht 2026-09-12, 17:42 min, 8.563 Views, 88 Likes (Verified, youtube_video_details).

Ausgewertet mit watch_youtube_video_and_ask (multimodal), Kernpunkte:
1. **Kein Account gezeigt**: Zu Beginn nur Mock-ups mit Platzhalter „@username“; bei 00:04 ein Dashboard mit seinem Profilbild ohne TikTok-Handle. **Follower-/View-Zahlen von @daniel.igl werden im Video nicht gezeigt.**
2. **Einkommens-Claim**: Dashboard-Screenshot (00:04) „Gewinn dieser Monat 12.327€“ (+258 %) – **Claimed**, Quelle des Dashboards unklar, nicht TikTok-Shop-bezogen.
3. **Monetarisierung laut Video**: eigenes digitales Produkt (E-Book, Workbook, Notion-Template; 11:00–11:15) oder Affiliate-Produkte über **Digistore24** (12:22), Verkauf über Funnel/DMs (10:10, 12:45). **TikTok Shop wird nicht als Monetarisierung genannt.**
4. **KI-Tools**: ChatGPT (Nischen, Content), Canva (Design), Claude/Claude Code (07:02), Obsidian (07:13).
5. **Beispiel-Videos**: KI-generierte Bilder + Text-on-Screen, B-Roll; keine sprechenden KI-Avatare.
6. **CTA**: „…schau dir unbedingt den kostenlosen Workshop an“ (07:59) → https://www.daniel-igl.de/gratistraining; „…dann kannst du auch gerne auf den zweiten Link in der Videobeschreibung klicken“ (14:55) → Beratungsgespräch https://www.daniel-igl.de/termin-daniel-igl; WhatsApp-Community mit Prompts (16:15).

Landingpage https://www.daniel-igl.de/gratistraining (WebFetch): „50+ Stunden Schritt-für-Schritt Video Akademie“, Versprechen „300–500 € pro Tag“ bzw. „4-stelliges Monatseinkommen in 8–12 Wochen“, „über 1.000 Teilnehmer“ – alles **Claimed**. Kein Preis auf der Seite; CTA = Termin buchen. Impressum: Daniel Igl / Digital Idea, Franz-Obermayer-Str. 6, 83607 Holzkirchen, USt-ID DE327424770 (Verified, https://www.daniel-igl.de/impressum).

Reputation: ProvenExpert 5,0/5 bei nur 1 veröffentlichter von 10 Bewertungen (https://www.provenexpert.com/de-de/daniel-igl-online-business-masterclass/); kritische Beiträge zu Coaching-Verträgen/Rücktritt (https://www.freedom-online-business.de/daniel-igl-kritik/ – Abruf 429; https://www.justanswer.de/anwalt/swcb9-ich-steckte-finanziellen-schwierigkeiten-und-schloss.html) – Claimed, nicht geprüft.

## 4. KI-Einsatz

- **ai_level: unklar.** Keine Videos einsehbar, daher weder AIGC-Label noch Avatar/Stimme prüfbar.
- Indizien: Bio und Zweitaccount deuten auf Clips einer realen Person (Daniel Igl vor Kamera, Business-Tipps) hin; YouTube-Shorts des Kanals sind Real-Talking-Head-Clips. Die im Belegvideo beworbene „faceless KI“-Methode wird auf @daniel.igl **nicht nachweislich** selbst angewandt. Die Notiz aus dem Sweep („faceless KI TikTok page“) ist damit **nicht bestätigt** – der Account ist eher ein Coach-Zubringer-Account.

## 5. Shop-Aktivität

| Signal | Befund |
|---|---|
| ttSeller | false (Verified) |
| commerceUser | false (Verified) |
| Bio / Showcase | kein Shop, kein Link (Verified) |
| Produkt-Anchors in Videos | nicht prüfbar (keine Videos gefunden) |
| #tiktokshop-Hashtags | nicht prüfbar |
| Artikel/Belege als Affiliate | keine; Belegvideo empfiehlt Digistore24-Affiliate + eigene Digitalprodukte, nicht TikTok Shop |

**shop_active = nein.** Produkte: keine TikTok-Shop-Produkte; monetarisiert wird (falls überhaupt) über Coaching/Workshop-Funnel (Preis nicht öffentlich; „hochpreisig“ laut Kritik-Artikel – Claimed).

## 6. Metriken

- Views: n = 0 gesampelt → avg/median/max: Nicht öffentlich verifizierbar.
- Likes gesamt 3.519 / 62 Videos = **≈ 57 Likes pro Video** (Estimated aus Verified-Werten).
- Upload-Frequenz: 62 Videos in ~630 Tagen (2025-01-02 bis 2026-09-24, ≈ 20,7 Monate) → **≈ 3 Videos/Monat ≈ 0,7/Woche** (Estimated; tatsächliche Verteilung unbekannt, Posts können geballt sein).
- Follower/Video: 102 / 62 ≈ 1,6 neue Follower pro Video (Estimated).

## 7. Einkommensschätzung

Keine Quelle (Kalodata/FastMoss/Artikel) veröffentlicht GMV für diesen Account. Kein TikTok Shop → **TikTok-Shop-Provision: ≈ 0 € (Estimated, da commerceUser=false)**.

Rechenweg für einen hypothetischen Shop-Betrieb (nur zur Einordnung, Estimated):
- Views/Video: keine Daten; Proxy über Likes: 57 Likes ÷ Like-Rate 3–5 % ≈ **1.100–1.900 Views/Video**.
- Monatsviews: ≈ 3 Videos × 1.100–1.900 ≈ **3.300–5.700 Views/Monat**.
- Formel: Views × CTR 2 % × CVR 5 % × Preis × Provision 10–20 %.
- 3.300–5.700 × 0,02 × 0,05 = 3,3–5,7 Verkäufe/Monat × 20–40 € × 10–20 % = **≈ 7–46 €/Monat** Provision – selbst im Best Case unter 50 €/Monat.
- GMV hypothetisch: 66–228 €/Monat (Estimated).

Tatsächliche Creator-Einnahmen: Funnel-Einnahmen (Coaching) sind nicht dem TikTok-Account zurechenbar und nicht öffentlich verifizierbar. Der Dashboard-Claim „12.327 € Gewinn/Monat“ ist unbelegt und stammt nicht aus TikTok-Daten. **income_confidence = LOW.**

## 8. Warum es (nicht) funktioniert

- 102 Follower nach 62 Videos und ~21 Monaten = **Low-Performer**. Ursachen (Einschätzung): (a) reiner Re-Upload-/Teaser-Account („komplette Videos auf YT“), der ohne Bio-Link und ohne Hook-Optimierung keinen Grund zum Folgen liefert; (b) Nische „Online Geld verdienen“ ist auf DE-TikTok extrem gesättigt und wird von Nutzern skeptisch gesehen (siehe Kritik-Beiträge); (c) Betreiber nutzt TikTok offenbar nicht als Verkaufskanal (kein Shop, kein Link), sondern YouTube + Landingpage.
- Fürs Gesamtprojekt relevant: Der Coach, der „faceless KI-TikTok-Seiten“ als Einkommensquelle verkauft, weist auf seinem eigenen TikTok-Account keine Reichweite nach und zeigt im Tutorial keinen eigenen Beispiel-Account mit Zahlen. Das Beispiel taugt als **Gegenbeispiel** zu Einkommensversprechen (300–500 €/Tag), nicht als Beleg für ein funktionierendes AI-Shop-Modell.

## 9. Quellen (Zugriff 2026-09-24)

- https://www.tiktok.com/@daniel.igl (tt_profile.sh, SSR-JSON)
- https://www.tiktok.com/@igldaniel (tt_profile.sh)
- https://www.tiktok.com/@igldaniel/video/7228253614555270426 (tt_video.sh: 7.762 Views, 341 Likes, 2023-05-01, Vergleich Zweitaccount)
- https://www.youtube.com/watch?v=xnbooWSc6Ko (youtube_video_details, watch_youtube_video_and_ask)
- https://www.youtube.com/@DanielIgl (channel_resolver, youtube_channel_shorts: 18 Shorts, 165–4.300 Views)
- https://www.daniel-igl.de/gratistraining
- https://www.daniel-igl.de/impressum
- https://www.provenexpert.com/de-de/daniel-igl-online-business-masterclass/
- https://www.freedom-online-business.de/daniel-igl-kritik/ (429 beim Abruf; nur Suchsnippet)
- https://www.justanswer.de/anwalt/swcb9-ich-steckte-finanziellen-schwierigkeiten-und-schloss.html (Suchsnippet)
