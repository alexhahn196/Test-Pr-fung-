# Reverse-Engineering: @dariasimhony (Daria Simhony, USA)

Stand: 2026-09-24/25. Datenquellen: TikTok-Public-Data (tt_profile.sh / tt_video.sh, Verified), Beacons-Bio-Seite dariasimhony.com (Verified, Rohdaten dekodiert), Skool-Seite skool.com/spicy-mama (Verified), Fanvue-Profil (Verified), YouTube-Kanal via NexLev (Verified), WSJ-Artikel "AI Videos Are Flooding TikTok Shop" (Patrick Coffee, 2026-07-16) über den Charm.io-Reprint blog.charm.io/charm-in-the-press/ai-videos-are-flooding-tiktok-shop (Verified Zitat, Inhalt = Claimed) und die AOL/Independent-Zusammenfassung (research/press/62917f4c.txt).
**Einschränkung:** WebSearch war nicht verfügbar; das NexLev-Watch-Tool (`watch_tiktok_video_and_ask`) war beim Start dieser Analyse bereits 15/15 erschöpft (Tageslimit) – ein Sichten der Videos (exakter Hook-Wortlaut, Schnitte, Kommentar-Reaktionen) war **heute nicht möglich**. Für das Jumiso-Video 7660244768810683678 liegt eine frühere NexLev-Sichtung aus dem Vorsweep vor (research/sweep_analytics_press.md). Alle Hook-Angaben unten stammen daher aus den Video-Captions (erste Zeile), nicht aus dem Bild – Tag: "Caption".

---

## 0. Kernbefund in drei Sätzen

1. @dariasimhony ist **kein TikTok-Shop-Affiliate-Account**, sondern ein **Coaching-Funnel-Account** (Modell B/C → tatsächlich "Sell-the-shovel"): 16 von 17 verifizierten Videos sind Pitches für die Skool-Community "Spicy Mama" (27 $/Monat bzw. 197 $/Jahr, 1.183 Mitglieder, Verified 2026-09-25); das einzige Produktvideo (Jumiso-Hautpflege) ist ausdrücklich ein "UGC Example", trägt das KI-Label, aber **keinen Shop-Anchor**. Der Account ist weder ttSeller noch commerceUser (Verified).
2. Der Wettbewerbsvorteil ist **nicht** KI-Produktion, sondern die Kombination aus **Presse-Autorität (WSJ-Feature) + eskalierenden Einkommens-Claims (2,5 M$ → 3 M$ → 4 M$ in 2,5 Monaten) + DM-Keyword-Funnel ("DM SPICY") + Niedrigpreis-Abo + Launch-Dringlichkeit ("Spicy Mama 2.0", Countdown 1.10.2026)**.
3. Verifizierbare TikTok-Shop-Provision über diesen Account: **0 $** (kein einziger Produkt-Anchor in 17 Videos). Verifizierbare Einnahmequelle: Skool-Abo → Schätzband **10–30 k$/Monat brutto** (Estimated, Formel unten). Die Selbstangaben ("4 M$ in 16 Monaten") sind **nicht öffentlich verifizierbar** und mit den verifizierten Reichweiten (Median 1.942 Plays/Video) nicht vereinbar.

---

## 1. Profil (Verified, tt_profile.sh 2026-09-24)

| Feld | Wert |
|---|---|
| Handle | @dariasimhony (Nickname "dariasimhony") |
| Follower | 128.700 |
| Likes gesamt | 2,1 Mio. |
| Videos | 918 |
| Account erstellt | 2019-12-20 (createTime 1576839951) |
| Bio | "30yr old girlie🩷Boy Mom / Spicy Mama🌶️ / Helping mamas make 💰 online with AI / 💌PR/Opportunities: dariasimhony@gmail.com" |
| Bio-Link | Dariasimhony.com (= Beacons-Seite) |
| ttSeller / commerceUser | **false / false** |
| verified | false |

Beacons-Seite dariasimhony.com (Verified, Rohdaten dekodiert 2026-09-25):
- Links: "Spicy Mama Course + Community" → skool.com/spicy-mama/about; "1:1 With Daria – 30 Minute Chat!" → payhip.com/b/5Ln6A (Preis: Cloudflare-403, nicht abrufbar); "Fanvue" → fanvue.com/dria ("Don't blame me if you get addicted💋"); Instagram @daria_simhony; YouTube @Daria_Simhony ("CEO of Spicy Mama / 125k on TikTok"); Foxy AI Referral-Link (foxy.ai/?referral_link=user_3HjC…); SoFi-Referral; "Featured in Wall Street Journal!" → WSJ-Artikel.
- Store-Item: "From Zero to Posted: The Spicy Mini Course", **47 $** (price 4700 Cent, product_type course, availability false = derzeit nicht kaufbar; angelegt 2026-09-20).
- Countdown-Block: "SPICY MAMA 2.0 DROPS – NEW Modules, Trainings, and MORE! Join Today before the drop!", target_unix_time 1790856000000 = **2026-10-01**.
- Zahlungs-Setup: Stripe (US) + PayPal Marketplace; Kontakt-Mail im Header: hello.shopwithdaria@gmail.com.

Skool "Spicy Mama" (Verified 2026-09-25): **1.183 Mitglieder**, Preis **27 $/Monat oder 197 $/Jahr**, Beschreibung "teaching men & women how to create, monetize & scale profitable AI-powered brands — no tech experience or showing your face required"; Themen: AI-Avatar-Erstellung, KI-Fotos/-Videos, IG/TikTok-Wachstum, Fanvue-Monetarisierung, TikTok Shop, UGC/Brand-Deals, Funnels, Automatisierung. Bewertung 3,9/5 (17 Reviews). Zweite Mentorin "Tamara". Reviews (Verified, zitiert): 5★ "I actually just made $20k last month with Daria's help in 1:1!" (Penelope DeMichele – Claimed, unbelegt); 1★ "She is super passive aggressive if you ask for proof or success stories … There's no one that's made money using her method"; 1★ "the course was repetitive, inconsistent, and often felt AI-generated … lack of guidance on AI disclosure and ethics … a member said they made a non-explicit avatar explicit; a moderator praised the work".

Fanvue "dria" (Verified, curl 2026-09-25): displayName "dria", **is_ai_creator = true**, Bio "Don't blame me if you get addicted💋", **18 Likes gesamt** → die KI-Persona, die laut Captions "thousands per post" verdienen soll, hat auf Fanvue praktisch keine sichtbare Reichweite.

YouTube @Daria_Simhony (Verified via NexLev 2026-09-25): 40 Abonnenten, 27 Videos (nur Shorts), 11.104 Views gesamt, beigetreten 2026-09-05, Link "Join Me Here" → dariasimhony.com. Instagram @daria_simhony: 429-blockiert, nicht verifizierbar. Instagram @dariaz_aicreator (241k Follower, "Higgsfield Creative Partner", aus DDG-Snippet) ist eine **andere Daria** – kein Beleg für Zugehörigkeit.

---

## 2. Video-Set (17 Videos, Verified via tt_video.sh 2026-09-24/25)

Quellen: tt_recent.sh (12 neueste, Embed-Seite) + 5 ältere URLs aus WSJ-Kontext/vorherigen DDG-Snippets. **Kein einziges Video hat einen Produkt-/Shop-Anchor**; nur das Jumiso-Video trägt ein KI-Label (aigcLabelType=1) und isECVideo=1.

| # | Video-ID | Datum | Länge | Plays | Likes | Komm. | Shares | Saves | KI-Label | Anchor | Hook (Caption-Zeile 1, ≙ 0:00–0:03) | Typ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7663557095567969567 | 2026-07-17 | 112 s | **281.900** | 18.600 | 1.185 | 2.953 | 7.321 | – | – | "WE HIT $3M DOLLARS🌶️🔥🥹❤️ My life changed in one year thanks to AI content" | Income-Claim → Kurs |
| 2 | 7662795430274551071 | 2026-07-15 | 73 s | 49.200 | 1.335 | 231 | 299 | 656 | – | – | "FEATURED ON WALL STREET JOURNAL 🤯🤯🤯 My AI journey has changed my life" | Presse-Autorität → Kurs |
| 3 | 7660244768810683678 | 2026-07-08 | 7 s | 34.800 | 256 | 8 | 104 | 135 | **1** | 1× type 35 (kein Produkt) | "UGC Example of AI Avatar promoting her favorite skincare - Jumiso 💦" | **einziges Produktvideo** (Portfolio-Beispiel) |
| 4 | 7657726708061097247 | 2026-07-02 | 72 s | 12.800 | 600 | 48 | 54 | 214 | – | – | "I'm giving you my $2.5M business playbook for $27." | Preis-Hook → Kurs |
| 5 | 7683686556074265887 | 2026-09-09 | 131 s | 4.827 | 196 | 14 | 12 | 33 | – | – | "The year didn't even end yet but I've accomplished so much🥹" | Story → Kurs |
| 6 | 7683283776897617182 | 2026-09-08 | 72 s | 3.492 | 210 | 41 | 28 | 93 | – | – | "AI Avatars are going to change your life🌶️" | Lifestyle → Kurs |
| 7 | 7684649522311466270 | 2026-09-12 | 10 s | 3.244 | 126 | 6 | 23 | 77 | – | – | "I just make AI Avatar content and I've become a multimillionaire in one year🤯" | Claim → Kurs (isAd=true lt. Vorsweep) |
| 8 | 7688365689962253598 | 2026-09-22 | 51 s | 2.645 | 184 | 26 | 9 | 46 | – | – | "8 DAYS UNTIL SPICY MAMA 2.0🌶️🤯 If you've been on the fence…" | Launch-Countdown |
| 9 | 7680924884289244446 | 2026-09-02 | 8 s | 1.942 | 63 | 1 | 5 | 14 | – | – | "Let me show you how to make AI money 💰 My AI Avatar literally makes thousands everyday" | Claim → Kurs |
| 10 | 7688745991154978079 | 2026-09-23 | 5 s | 1.705 | 97 | 4 | 2 | 21 | – | – | "AI AVATARS made me $4M in 16 months 🌶️✨" | Claim → Kurs |
| 11 | 7688756518891588895 | 2026-09-23 | 10 s | 1.473 | 81 | 7 | 6 | 14 | – | – | "Spicy Mama 2.0 is going to be 🌶️ AI Avatars & 🌶️Filmmaking 🌶️Dropshipping 🌶️High-ticket Sales" | Launch |
| 12 | 7688360097768017183 | 2026-09-22 | 56 s | 1.471 | 104 | 4 | 4 | 28 | – | – | "MY AI GIRL IS MAKING ME 💸💸💸💸 I didn't even have to show my face & I'm making thousands from this ONE post" | Claim → Kurs |
| 13 | 7688788655493713183 | 2026-09-23 | 13 s | 1.365 | 93 | 9 | 4 | 15 | – | – | "Claim this energy for you right now✨💸" | Manifestation → Kurs |
| 14 | 7688696875452468511 | 2026-09-23 | 55 s | 1.072 | 109 | 8 | 6 | 37 | – | – | "I might have to delete this soon because I've cracked the code 🤯🤯 $4M made with AI Avatars" | Claim → Kurs |
| 15 | 7689167819392535839 | 2026-09-24 | 12 s | 1.015 | 60 | 7 | 2 | 7 | – | – | "SPICY MAMA 2.0 is 6 days away🤯☕️🌶️" | Launch-Countdown |
| 16 | 7688742634273213727 | 2026-09-23 | 58 s | 865 | 40 | 11 | 0 | 10 | – | – | "LET THE COUNTDOWN BEGIN🌶️💸🎉 Be sure to ask any questions…" | Launch / Q&A |
| 17 | 7688787280676261151 | 2026-09-23 | 47 s | 831 | 106 | 14 | 1 | 17 | – | – | "AND SO IT SHALL BE🌶️💸✨ Your AI girl and you, deserve to be showered with abundance" | Manifestation → Kurs |

Aggregat (Verified-Basis, Estimated-Rechnung): Summe Plays 404.647; **Top-Video = 69,7 %** aller Plays des Sets; Median **1.942** Plays; ohne die drei Juli-Ausreißer (Nr. 1–3) Median 1.705. Engagement Top-Video: 6,6 % Likes/Plays, 1.185 Kommentare, 7.321 Saves (Save-Rate 2,6 % – hoch; typisch für "how to make money"-Content). Musik: fast durchgehend "original sound" (Talking-Head/Voiceover), zwei Videos mit Trend-Sounds ("Ring My Bell", "naddy"). Hashtag-Set nahezu identisch in allen Kurs-Videos: #spicymama #aicontentcreation #aicontentcreator #financialfreedom (+ #3million/#4million als Claim-Tag, #facelessmarketing, #ugccontentcreator).

### 2.1 Video-Sichtungen

**Jumiso-Video 7660244768810683678** (7 s, 34.800 Plays; NexLev-Sichtung aus dem Vorsweep, Verified [Vorsweep]): KI-Avatar-Presenterin (Fanvue-Persona "dria"-Typ) mit **synthetischer Stimme**, zeigt Jumiso-Niacinamide-Creme (Produkt im Bild, KI-gerendert/Image-to-Video – WSJ-Zitat: "turn still images into three-dimensional videos where their avatars appear to hold or sample products"), **kein TikTok-Shop-CTA, kein Produkt-Card**. TikTok-KI-Label gesetzt (aigcLabelType=1). Caption nennt es explizit "UGC Example" – d. h. Portfolio-Demo für Brand-Deals (Fixhonorar), nicht Affiliate. Kommentare: 8 (nicht abrufbar).
**Top-Video 7663557095567969567 "WE HIT $3M"** (112 s) und die 2026-09-Videos: Sichtung heute nicht möglich (Quota). Aus Metadaten: "original sound", 47–131 s lange Talking-Head-/Story-Formate (die 5–13-s-Videos sind Text-on-Screen-Teaser). CTA in jeder Caption identisch: **"DM me 'SPICY' or '🌶️' to get started"** + "🔗 in bio" – ein ManyChat-artiger DM-Keyword-Funnel (Estimated: Auto-DM mit Skool-Link). Ob im Bild Dashboards/Einnahmen-Screens gezeigt werden: **nicht verifizierbar** (keine Sichtung).
Kommentar-Reaktion: nicht abrufbar. Indiz: Skool-Reviews enthalten explizite "Proof?"-Pushback-Kritik (1★-Reviews oben).

---

## 3. Offer

| Feld | Befund | Tag |
|---|---|---|
| Produkt (Haupt) | Skool-Community "Spicy Mama" (Kurs + Community, Live "Tech Tuesdays", 1:1-Upsell) | Verified |
| Preis | 27 $/Monat oder 197 $/Jahr; Mini-Kurs "From Zero to Posted" 47 $ (Beacons-Store, derzeit inaktiv); 1:1 30-min-Call via Payhip (Preis nicht abrufbar, 403) | Verified |
| Rabatt/Coupon | keiner; stattdessen Launch-Dringlichkeit "join before the drop" (2.0 am 1.10.2026), "Spicy Scholarship" (angekündigt) | Verified (Captions/Beacons) |
| Provision | n/a – Eigenprodukt (Skool behält Zahlungsgebühren ~2,9 % + 0,30 $; Estimated). Foxy-AI-Referral und SoFi-Referral in Bio = Affiliate-Nebeneinnahmen (Höhe unbekannt). TikTok-Shop-Provision: **0 Anchors → nicht nachweisbar** | Verified/Estimated |
| Impulskauf-Potenzial | hoch: 27 $ Einstieg ("$2.5M playbook for $27"), Einkommens-Claims als Hook, DM-Funnel senkt Reibung | Estimated |
| Problem/Lösung | "Mom needs income without showing face / 9-5" → "AI girl makes money on Fanvue (PPV), TikTok Shop, UGC deals; I show you how" | Verified (Captions) |
| Zielgruppe | US-Mütter/"mamas" 25–40, Faceless-/Side-Hustle-Suchende; Sekundär: Männer ("men & women" in Skool-Beschreibung) | Verified |
| Jumiso (einziges Produkt) | K-Beauty-Creme; laut WSJ Client-Beziehung (Fixhonorar/UGC), nicht Affiliate; Preis nicht abrufbar (Estimated AOV ~18 $) | Claimed/Estimated |

---

## 4. Distribution

- **Traffic-Quelle (Estimated):** überwiegend For-You/organisch + Follower-Feed (128,7k Follower; die Kurs-Videos erreichen 0,6–2,7 % der Follower – typische Follower-Feed-Reichweite). Suchtraffic: gering; Captions sind Claim-/Story-Texte, keine Produkt-Suchbegriffe (nur das Jumiso-Video trägt #skincareroutine #jumiso). Shop-Tab: **0 %** (keine Anchors, kein Commerce-Account). Ein Video (Nr. 7) war laut Vorsweep isAd=true → mindestens punktuell **Paid Promotion** der Kurs-Videos.
- **Views-Konzentration:** Top-Video 69,7 % der Plays des Sets; die drei Juli-Videos (3 M$-Claim, WSJ-Feature, Jumiso-Demo) = 90,4 %. Alles nach dem WSJ-Peak (Sept.) liegt bei 0,8–4,8k Plays → der Account lebt von wenigen Ausreißern, der Grundpegel ist niedrig.
- **Posting-Volumen (Verified):** 918 Videos seit 12/2019 (~11/Monat langfristig); aktuell Launch-Burst: 2 Videos am 22.9., **6 Videos am 23.9.**, 1 am 24.9. (9 Videos in 3 Tagen). WSJ-Claim "≥1 vollständig KI-generiertes Promo-Video pro Tag" ist auf diesem Account **nicht** sichtbar (1 KI-gelabeltes Video in 17).
- **Sister-Accounts:** Fanvue "dria" (KI-Persona, 18 Likes); YouTube @Daria_Simhony (40 Abos, 27 Shorts – Crossposting der TikToks, seit 5.9.2026); Instagram @daria_simhony (nicht abrufbar). Separate TikTok-Shop-/Avatar-Accounts ("her AI avatar does TTshop") werden **nirgends benannt** → nicht öffentlich verifizierbar.
- **Varianten:** ja – dieselbe Botschaft in ≥10 Varianten innerhalb weniger Tage (5-s-Teaser "$4M in 16 months", 55-s "cracked the code $4M", 56-s "MY AI GIRL is making me $$$", 13-s "Claim this energy", Countdown 8/6 Tage). Klassisches Hook-Testing mit identischem CTA und Hashtag-Set. Claim-Eskalation als Messgröße: 2,5 M$ (2.7.) → 3 M$ (17.7.) → "multimillionaire" (9./12.9.) → 4 M$ (22./23.9.).

---

## 5. Wettbewerbsvorteil – Bewertung

| Faktor | Beitrag | Evidenz |
|---|---|---|
| Presse-Autorität (WSJ 16.7.2026) | **hoch** – das WSJ-Video ist ihr 2.-bestes (49,2k), das 3-M$-Video einen Tag später ihr bestes (281,9k); Beacons-Link "Featured in WSJ" | Verified |
| Einkommens-Claims als Hook | **hoch** – jedes Kurs-Video startet mit Dollar-Claim; Claims eskalieren | Verified (Captions), Beträge unbelegt |
| DM-Keyword-Funnel + Niedrigpreis-Abo (27 $) | **hoch** – 1.183 Mitglieder | Verified |
| Launch-Dringlichkeit ("2.0", Countdown, Scholarship) | mittel – treibt aktuellen Posting-Burst | Verified |
| Hook-Varianten-Testing / Volumen | mittel – 9 Videos/3 Tage, aber Reichweite <5k | Verified |
| KI-Avatar / billige Produktion | **gering** als Reichweiten-Treiber (1 KI-Video im Set; Fanvue-Persona ohne Publikum); hoch als **Verkaufsargument** ("no face needed") | Verified |
| Produktwahl / Provision / Trend-Arbitrage (TikTok Shop) | **nicht nachweisbar** (0 Anchors, kein Commerce-Account) | Verified (Abwesenheit) |

**Fazit:** Der reale Vorteil ist ein **Kurs-Funnel, der die KI-Avatar-Erzählung verkauft** ("sell the shovel"), verstärkt durch ein singuläres Presse-Ereignis. Für die Frage "Wie verdient man mit KI-Avataren auf TikTok Shop?" liefert dieser Account **keine** verwertbare Produktions- oder Provisions-Evidenz; er liefert Evidenz dafür, wie man aus der Erzählung Abo-Umsatz macht. Übertragbar: (a) Presse/Autoritäts-Signal als Content-Anker, (b) DM-Keyword-Funnel, (c) Varianten-Testing eines einzigen Claims. Nicht übertragbar/riskant: unbelegte Einkommens-Claims (FTC-Risiko), Fanvue-PPV-Persona als "Beweis".

---

## 6. Einkommensschätzung (Estimated)

**A) TikTok-Shop-Provision über @dariasimhony:** Formel Views × CTR × CVR × Preis × Provision. Verified-Anker: 0 Produkt-Anchors → Provisions-Traffic praktisch 0. Hypothetisch (falls 30 Produktposts/Monat wie WSJ-Claim): 30 × 1.942 (Median) = 58.260 Views × 1 % CTR × 3 % CVR × 18 $ × 15 % = **~5 $/Monat**; Best-Case mit 34.800 Views/Post (Jumiso-Niveau): 1,04 M Views × 1 % × 3 % × 18 $ × 15 % = **~840 $/Monat**. Band: **0–1 k$/Monat**, realistisch ~0 $, da keine Shop-Links.

**B) Skool "Spicy Mama" (Hauptquelle):** 1.183 Mitglieder (Verified) × Blended-ARPU 16,4–27 $/Monat (Jahresplan 197 $/12 = 16,4 $; Monatsplan 27 $) = **19,4–31,9 k$/Monat brutto**, abzüglich Gratis-/Scholarship-Plätze und Gebühren (Annahme 20–50 % nicht zahlend) → **10–30 k$/Monat** (Estimated). Plus 1:1-Calls (Payhip, Preis unbekannt), 47-$-Mini-Kurs (inaktiv), Foxy/SoFi-Referrals, Brand-Deals (Jumiso, Fixhonorar – Höhe nicht öffentlich).

**C) Fanvue "dria":** 18 Likes → vernachlässigbar (Estimated <100 $/Monat).

**Gesamtband: ~10–30 k$/Monat brutto, ≥90 % aus dem Kurs-Abo** (Estimated). Selbstangabe "4 M$ in 16 Monaten" (= 250 k$/Monat): **nicht öffentlich verifizierbar**; kein Dashboard, keine GMV-Quelle (Kalodata/FastMoss ohne Shop-Account nicht anwendbar); WSJ nennt keinen Betrag.

**Konfidenz:** Mechanik/Funnel/Preise = HIGH (alles verifiziert); Einkommenshöhe = LOW–MEDIUM (Mitgliederzahl verifiziert, Zahlungsquote unbekannt); TikTok-Shop-Aussage "0 $ nachweisbar" = HIGH. Gesamt: **MEDIUM**.

---

## 7. Quellen (Zugriff 2026-09-24/25)
- tt_profile.sh / tt_video.sh (TikTok Public Data) – 17 Video-IDs s. Tabelle; Rohdaten: research/reverse/_daria_videos.json, _daria_videos_extra.txt
- https://dariasimhony.com (Beacons; Rohdaten dekodiert; Kopie research/daria_site.html)
- https://www.skool.com/spicy-mama/about (1.183 Mitglieder, 27 $/197 $, Reviews)
- https://www.fanvue.com/dria (is_ai_creator=true, 18 Likes)
- YouTube @Daria_Simhony (NexLev youtube_channel_about: 40 Abos, 27 Videos, seit 2026-09-05)
- WSJ "AI Videos Are Flooding TikTok Shop", Patrick Coffee, 2026-07-16 – https://www.wsj.com/cmo-today/ai-videos-are-flooding-tiktok-shop-c86a88e0 (401/paywall); Reprint https://blog.charm.io/charm-in-the-press/ai-videos-are-flooding-tiktok-shop (research/charm_wsj.html); AOL/Independent-Zusammenfassung research/press/62917f4c.txt
- Vorsweep-Notizen: research/sweep_analytics_press.md, research/claims_interviews_podcasts.md, research/claims_verdicts_compact.md
- Nicht erreichbar: payhip.com/b/5Ln6A (403), instagram.com/daria_simhony (429), Google/DDG/Bing-Suche (Captcha/leer), archive.org/archive.ph (blockiert), NexLev-Watch (15/15 Quota)
