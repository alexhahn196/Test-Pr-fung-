# Reverse-Engineering: @healthiswealthfyp (US) — "Granny"-AI-Avatar × Goli Beets Cardio Gummies

Stand: 2026-09-24/25. Modell C (voll-AI-Avatar, Long-Form-Testimonial, TikTok-Shop-Affiliate). Alle TikTok-Zahlen per `tt_profile.sh` / `tt_video.sh` / TikTok-SSR-JSON (Verified, Abruf 2026-09-25). Transkripte = TikToks eigene ASR-Untertitel (WebVTT, `subtitleInfos`, Source "ASR"), On-Screen-Texte = `stickersOnItem` aus dem SSR-JSON. Das Watch-Tool (`watch_tiktok_video_and_ask`) war für diese Session ausgeschöpft (15/15); die Sicht-Analyse stützt sich daher auf (a) die im Vorlauf (2026-09-24) dokumentierte Watch-Auswertung des Top-Videos, (b) die heruntergeladenen Cover-Frames (4 Stück, gesichtet) und (c) die ASR-Transkripte mit Zeitstempeln.

Tags: **Verified** = in TikTok-Daten/Primärquelle gesehen · **Claimed** = jemand behauptet es · **Estimated** = eigene Rechnung mit Formel.

---

## 1. Account-Steckbrief (Verified)

| Feld | Wert |
|---|---|
| Handle | @healthiswealthfyp, Nickname "healthiswealthfyp" |
| Bio | "Showing you the best videos that support our culture 👍🏿💕" — kein Bio-Link |
| Erstellt | 2025-10-29 (createTime 1761714237) |
| Follower / Likes / Videos | 25.700 / 100.300 / 108 |
| Following | 1 |
| commerceUser / ttSeller | false / false (kein Shop-Badge im Profil; Affiliate-Status nicht aus dem Profil ablesbar) |
| Letztes Video | 2025-12-10 (7582309243169131831). Seitdem **kein** Upload → Account seit ~9,5 Monaten inaktiv |
| Betreiber | Claimed: tommycetty (YouTube kjCyL4Vn4P4 [3:30]: "These are my own accounts that I posted before … This one is healthiswealthfyp"). Zusätzlich Verified-Script-Match: In 1XO4S9ZKLDY [37:11–37:33] spielt er "one of my videos that popped off … made me just around 10K in commission … December of 2025" ab; das eingespielte Audio ("This ain't new. My mama's mama used this. Beetroot helps your body produce nitric oxide which opens up your blood vessels") entspricht wörtlich dem Top-Video 7577483914822913294 [01:16–01:27]. Zuordnung damit **sehr wahrscheinlich** (nicht beweisbar, da Handle-Ownership nicht öffentlich). |
| Schwester-Account | **@holistic.granny** (Verified, siehe §6): erstellt 2025-11-04, 6.936 Follower, 22.500 Likes, 128 Videos, Bio "Helping my dear friends better their lives 👍🏿" (gleiche Emoji-Signatur), identisches Format/Produkt/Hashtags/Disclaimer, Uploads am selben Tag im Minutenabstand, ebenfalls letzter Upload 2025-12-10. |

---

## 2. Analysierte Videos (Verified-Statistik, Abruf 2026-09-25)

Alle Videos: `anchors=[]` (heute kein Produkt-Anker mehr in den Daten — der TikTok-Shop-Link wurde entfernt oder ist mit dem Affiliate-Status erloschen), `aigcLabelType=null`, `music="original sound"`, `diversificationLabels` = Health & Wellness / Fitness & Health. `isAd=true` = TikTok-Feld "isAd" (Spark-Ads-/Werbeautorisierung), **nicht** ein sichtbares "Paid partnership"-Label.

| # | Video-ID (Datum UTC) | Länge | Plays | Likes | Komm. | Shares | Saves | isAd | AI-Label (ShowAIGC) | Hook 0–3 s (gesprochen, ASR) | On-Screen-Hook (Sticker) | CTA (Zeit) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7572439019821288717 (2025-11-14) | 10 s | **242.800** | 45.900 | 6.126 | 876 | 1.798 | false | **ja** | [00:00] "Hey, guys. We just got done with our shift. I'm Sergeant Miler. And I'm Staff Sergeant Jackson." | – (kein Sticker) | keine — reines Follower-Bait-Video (#backtheblue #followme #armylife), zwei Soldaten im Humvee |
| 2 | **7577483914822913294 (2025-11-27)** | 152 s | **287.100** | 10.500 | 704 | 1.617 | 1.388 | true | nein | [00:00] "I'm 82 years old, raised five children, 12 grandchildren, and I'm still here cooking Sunday dinner while folks half my age can barely walk up the stairs without losing their breath." | "Granny's secret to 82 years on this Earth 💕" / "Don't take her for granted… 👂" | [02:14] "Goli got a sale going on TikTok Shop. If you see that orange card at the bottom, tap it and get you some." |
| 3 | 7581235294125509902 (2025-12-07) | 171 s | 1.454 | 53 | 6 | 4 | 12 | true | nein | [00:00] "I'm 82 years old, raised five children …" (identisch zu #2) | "POV: Asking my GRANNY her best advice for a good life 💕😳" / "82 YEARS YOUNG 👀" / "STELLA RYAN" | [02:28] "Goli sells out every single time this goes viral. If you see that orange card … Tap it immediately" |
| 4 | 7581530187116973367 (2025-12-08) | 163 s | 1.533 | 39 | 0 | 0 | 5 | true | nein | [00:00] "I'm 82 years old, raised five children, 12 grandchildren …" | "POV: Your granny is a holistic QUEEN 😳" / "GRANNY'S secret after 82 YEARS on this Earth" | [02:24] "Goli is running a sale right now … [02:32] If that orange cart is still on your screen, tap it right now before somebody else takes your bottle." |
| 5 | 7581553951821122871 (2025-12-08) | 136 s | 1.096 | 15 | 0 | 0 | 3 | true | nein | [00:00] "I'm 82 years old, raised five children, 12 grandchildren …" | "The ONE thing that change my life for the BETTER‼️😳" / "LISTEN CAREFFULY 👂" | [02:01] "they're gone within days. If you still see that orange cart, that's your sign. Tap it right now." |
| 6 | 7581594903277227319 (2025-12-08) | 123 s | 1.224 | 21 | 2 | 1 | 4 | true | nein | [00:00] "They don't want us knowing this. Baby, I'm 86 years old, still cooking Sunday dinner, and I got more energy than my own daughters." | "WE need to EDUCATE each other ✊🏿💕" / "THEY don't want us knowing THIS 😳" | [01:54] "If you see that orange cart, tap it now before they're gone." |
| 7 | 7581907677987507470 (2025-12-09) | 124 s | 1.524 | 36 | 2 | 1 | 6 | true | nein | [00:00] "They pray we never figure this out. Baby, I'm 82 years old, and I just realized they've been hiding this from our community my whole life." | "THEY don't want us educated and exposing THEM 👀✊🏿" / "LISTEN CAREFULLY 👂" | [01:56] "…this goes viral. If you see that orange cart, tap it now." |
| 8 | 7581928988357004599 (2025-12-09) | 125 s | 1.780 | 32 | 3 | 0 | 7 | true | nein | [00:00] "You want to know why nobody in our community knows this? Because they can't make money off us if we're healthy." | "GRANNYS' secret after 82 years on this Earth 🌎💕" / "Pay attention, SHE KNOWS 😳" | [01:56] "Tap that orange cart right now." |
| 9 | 7581957291071655223 (2025-12-09) | 110 s | 1.342 | 21 | 0 | 2 | 3 | true | nein | [00:00] "Obsessed? Baby, I'm not obsessed. I'm educated. There's a difference." | "POV: Asking GRANNY why she's OBSESSED with these 'gummies' 😳💕" / "SHE KNOWS SOMETHING 👀" | [01:42] "Tap that orange cart before they sell out." |
| 10 | 7581980253350808845 (2025-12-09) | 109 s | 1.650 | 23 | 2 | 5 | 8 | true | nein | [00:00] "Baby, you really wanna know? Because I've been waiting for somebody to ask me this. The secret is something our ancestors knew that they made us forget. Beetroot." | "POV: Asking GRANNY how she's so active at 86 👀💕" / "LISTEN CAREFULLY 👂" | [01:38] "if you see that orange cart, tap it. Goli sells out fast." |
| 11 | 7582004938746727694 (2025-12-09) | 125 s | 2.722 | 55 | 3 | 3 | 20 | true | nein | [00:00] "I buried too many people who didn't know what I'm about to tell you. And I refuse to stay quiet anymore. I'm 82 years old …" | "Is my GRANNY delusional? 😳👀" | [01:55] "If you see that orange cart, tap it before it sells out." |
| 12 | **7582309243169131831 (2025-12-10, neuestes)** | 121 s | 2.784 | 49 | 4 | 1 | 10 | false | **ja** | [00:00] "Come here, baby. Sit down. Grandma needs to tell you something, and I need you to really hear me. [00:07] I'm 89 years old." | "Asking my 89 year old GRANNY what her secret is….💕😳" / "Listen Carefully, She KNOWS" | [01:44] "The sale is on right now, but Goli sells out fast. If that orange card is on your screen, tap it. Don't wait until it's too late." |

Summen der 12 verifizierten Videos: 547.009 Plays; Top-Produktvideo = 52,5 % davon, die beiden viralen Videos (#1 + #2) = 96,9 %. Die 10 Dezember-Produktvideos liegen bei 1.096–2.784 Plays (Median ≈ 1.500).

Auf allen Produktvideos steht zusätzlich als Sticker der Disclaimer: "The information provided does not constitute medical advice. Consult a healthcare professional or doctor before use. Individual results may vary. This is not professional advice" plus "GOLI BEETROOT GUMMIES" (im Top-Video mit Tippfehler "Goli Beeteoot Gummies"). Derselbe Disclaimer steht ab 2025-12-07 auch in der Beschreibung.

---

## 3. Content-Analyse

### 3.1 Top-Video 7577483914822913294 (287.100 Plays) — Story-Struktur mit Zeitstempeln (ASR, Verified)

| Zeit | Segment | Wortlaut / Inhalt |
|---|---|---|
| 00:00–00:13 | **Hook / Autorität** | "I'm 82 years old, raised five children, 12 grandchildren, and I'm still here cooking Sunday dinner while folks half my age can barely walk up the stairs without losing their breath." |
| 00:14–00:29 | **Problem + Emotion** | "I'm tired of watching our people, my people, have their life come to an abrupt end from things we can prevent. High blood pressure, heart disease, diabetes, strokes." |
| 00:30–00:49 | **Verlust-Story** | "I've buried too many friends … too many young black men and women who didn't have to go that early … Nobody taught them how to take care of their bodies. Nobody told them the truth." |
| 00:50–01:12 | **Feindbild / Verschwörung** | "back in my day, we ate from the earth … Now look what they got y'all eating. Fast food on every corner. Sugar in everything … And they put it right in our neighborhoods on purpose. Don't get me started, baby." |
| 01:12–01:24 | **Wendepunkt** | "But I ain't here to just complain. I'm here to help. Let me tell you about something my mama used to give us. Beetroot. This ain't new." |
| 01:24–01:41 | **"Wissenschaft"/Nutzen** | "Beetroot helps your body make nitric oxide, which opens up your blood vessels … better heart health, more energy, less swelling in your legs and feet. And, yes, it helps the men perform better, too. Don't act shocked. I'm 82." |
| 01:43–02:01 | **Produkt-Reveal** | "I take Goli Beetroot gummies every morning. They taste good, they're easy on my stomach. And they got CoQ10 in there for extra energy. Clean ingredients, no mess, no nasty powders." (ab ≈01:32 orange TikTok-Shop-Karte sichtbar — laut Watch-Auswertung vom 2026-09-24) |
| 02:02–02:09 | **Disclaimer + Proof** | "Results vary, of course. Everybody's different. But, baby, I feel stronger than I did 10 years ago." |
| 02:14–02:19 | **CTA** | "Goli got a sale going on TikTok Shop. If you see that orange card at the bottom, tap it and get you some." |
| 02:19–02:32 | **Emotionaler Outro** | "Take care of yourself, baby. Because our community needs you here. Your family needs you here. And grandma ain't ready to lose nobody else." |

- **Produkt-Darstellung:** kein Hands-on, keine Packshots, kein Before/After, keine echten Produktclips; das Produkt existiert nur als (a) Nennung im Script, (b) Sticker "Goli Beeteoot Gummies" oben im Bild, (c) orange TikTok-Shop-Produktkarte. Im Schwester-Account-Cover (holistic.granny 7582011401456078094) liegen AI-gerenderte rohe Rüben auf dem Tisch — ebenfalls kein reales Produkt.
- **Avatar (Cover gesichtet + Watch-Auswertung 2026-09-24):** ältere Schwarze Frau, dunkles Sweatshirt, holzvertäfelte Küche mit Weinranken-Bordüre, Kunstblumen, Familienfoto, Mikrowelle — "Talking-Head-UGC-Selfie"-Look. Watch-Auswertung: Lip-Sync-Artefakte, statischer Hintergrund → AI-Avatar mit AI-Stimme (tommycetty nennt seine Pipeline: Nano Banana Pro → ElevenLabs → HeyGen/Hedra-Lip-Sync). Eingeblendeter Hinweis laut Watch: "This video may contain AI-generated content and is for entertainment purposes" — obwohl das TikTok-Feld `ShowAIGC=false` ist (also kein offizielles TikTok-AI-Label, sondern ein eigener Einblendtext).
- **Stimme:** AI-Voice, "ältere Schwarze Frau, Southern/AAVE-Register" ("baby", "y'all", "ain't"), langsames Predigt-Tempo (361 Wörter / 152 s ≈ 143 wpm).
- **Captions:** gelb-weiße Word-by-Word-Karaoke-Captions in Blockschrift-Italic (im Cover: "I'M 82 YEARS", Schlüsselwort gelb) unten im unteren Drittel; darüber zwei weiße Text-Sticker (Hook-Box + Subline). Kein Musikbett (`music: original sound`).
- **Schnitte/Szenen:** ein durchgehender Talking-Head-Shot (1 Szene); Bewegung nur durch Gesten (Hand an der Stirn im Cover). Kein B-Roll, kein Stock, kein UGC-Material, kein Text-Overlay-Wechsel außer Captions.
- **Kommentarsektion (704 Kommentare, 617 gelesen, Verified):** praktisch ausschließlich religiöse Zustimmung älterer Schwarzer Frauen ("Amen", "God bless you Queen", "Thank you grandma", "She's not lying about that"). **Kein einziger** "this is AI"/"fake"-Kommentar in 617 Kommentaren. Kaufsignale: 7 Treffer, z. B. "Im gonna buy me some beet roots", "let me gone and order", "at not there anymore how order" (→ Produktkarte war später schon weg), "Angela: Amen mom I need some of that." → Social Proof vorhanden, aber niedrig (≈1 % der Kommentare).
- **Gesundheits-Claims (verbatim):** "High blood pressure, heart disease, diabetes, strokes" (Prävention impliziert), "opens up your blood vessels", "better heart health, more energy, less swelling in your legs and feet", "it helps the men perform better, too", "I feel stronger than I did 10 years ago". → aus Compliance-Sicht Krankheits-bezogene Claims für ein Supplement (US: FTC/FDA-kritisch; in DE/EU nach HCVO unzulässig).

### 3.2 Neuestes Video 7582309243169131831 (2.784 Plays, ShowAIGC=true) — Struktur

| Zeit | Segment | Wortlaut |
|---|---|---|
| 00:00–00:06 | Hook (Intimität) | "Come here, baby. Sit down. Grandma needs to tell you something, and I need you to really hear me." |
| 00:07–00:17 | Autorität + Beobachtung | "I'm 89 years old. I've watched three generations of our family come up, and I've noticed something that breaks my heart." |
| 00:18–00:38 | Problem-Spiegel | "Y'all are tired all the time. Your legs swelling up, no energy … you think that's normal … that ain't normal. That's your body begging you for help." |
| 00:39–01:06 | Herkunfts-Story + Mechanismus | "I never stopped doing what my mama taught me. She gave us beetroot straight from the garden … Beetroot can help your body produce nitric oxide, which may help support healthy circulation." (weichere "may help support"-Formulierung als im Top-Video) |
| 01:07–01:16 | Einwand-Behandlung | "I know you're not going to eat raw beets every day. They taste terrible. And you'd need so many just to get what's in two gummies." |
| 01:16–01:34 | Produkt | "So I take Goli beetroot gummies. Concentrated extract … CoQ10 for cellular energy. B12, third party tested. No cheap fillers." |
| 01:35–01:44 | Disclaimer + Proof | "Results vary. Everybody responds different. But look at me. I'm 89. Still cooking, still moving, still here." |
| 01:44–01:53 | CTA + Scarcity | "The sale is on right now, but Goli sells out fast. If that orange card is on your screen, tap it. Don't wait until it's too late." |
| 01:54–01:58 | Emotionaler Outro | "Like so many people I've loved. Take care of yourself, baby. Grandma needs you here for a long time." |

Cover: **dieselbe** Avatar-Figur und Küche wie im Top-Video (grünes Henley statt blauem Sweatshirt, Hand an der Stirn) — d. h. konsistenter Charakter über die meisten Videos, **aber** das Alter wechselt im Script (82 / 86 / 89) und mind. ein zweiter Avatar existiert (Video #6: andere Frau, grüne Strickjacke, weiße Küche, Fenster; holistic.granny: dritte Frau mit Headwrap im Garten vor roter Scheune). Es gibt also 3 "Grannies" mit gleichem Script-Skelett.

### 3.3 Muster über alle 11 Produktvideos (Verified aus ASR)

- **Ein Master-Script, ≥ 11 Varianten:** Videos #2, #3, #4, #5 beginnen wortgleich ("I'm 82 years old, raised five children, 12 grandchildren, and I'm still here cooking Sunday dinner …"); #6–#12 tauschen nur den Hook (Verschwörung "They don't want us knowing this", Verlust "I buried too many people", Q&A "Obsessed? Baby, I'm not obsessed", Intimität "Come here, baby. Sit down"). Der Mittelteil (Beetroot → Nitric Oxide → Kreislauf → Schwellungen/Energie; "you'd need a whole pile of raw beets"; CoQ10 + B12 + "third party tested"; "Results vary") und die CTA-Formel ("orange cart/card … tap it … sells out") sind in allen Varianten identisch. Script-Länge 214–361 Wörter, 109–171 s → Mittelfunnel-Long-Form, wie von tommycetty beschrieben ("2 to 3-minute long videos").
- **Hook-Familien (On-Screen):** (a) "Granny's secret to 82/86 years", (b) "POV: Asking my GRANNY …", (c) "THEY don't want us knowing/educated …" (Verschwörungs-Frame, ✊🏿), (d) "Is my GRANNY delusional?", (e) "The ONE thing that changed my life". → klassisches Hook-Testing bei konstantem Body.
- **Demografie-Targeting:** alle Videos mit #blacktiktok/#blacktok/#blacktiktokcommunity/#blackhealth; Script-Marker "our people", "our community", "young black men and women", "they put it right in our neighborhoods on purpose". tommycetty dazu wörtlich (kjCyL4Vn4P4 [11:31–12:13]): "lean into demographics and racism … If you're selling a blood pressure gummy … A black character. Why? Because black people tend to have higher blood pressure." Zielgruppe: Schwarze US-Amerikaner 45+, v. a. Frauen (Kommentar-Namen und -Ton: "Queen", "Amen", Kirchen-Register).
- **Compliance-Layer ab 07.12.2025:** #resultsmayvary, Disclaimer in Beschreibung + Sticker, "Results vary" im Script, weichere Claims ("may help support"). Im Top-Video vom 27.11. fehlt das noch weitgehend (nur "Results vary, of course").
- **Keine Suchoptimierung:** Beschreibungen sind emotional ("GRANNY loves you all! 💕"), keine Produkt-Suchbegriffe außer #beetrootgummies/#beetroot; kein Produkt-Titel-Format. → Traffic ist FYP-/Ads-getrieben, nicht Search.

---

## 4. Offer

| Feld | Wert | Tag |
|---|---|---|
| Produkt | **Goli Beets Cardio Gummies** (im Script "Goli Beetroot gummies"): Beetroot-Extrakt + 100 mg CoQ10 + B12, vegan, "third party tested" | Verified (goli.com Shopify-Katalog `products.json`, 2026-09-25: "Goli Beets Cardio Gummy - Beet Root Extract & 100mg CoQ10") |
| Preis (Hersteller-Shop) | 1 Flasche **$15.98** (Streichpreis $25.00); 3 Flaschen $44.98 (statt $75); 5 Flaschen $54.98 (statt $125); Einzel-Listing "Goli Beets Cardio Gummy" $24.97; 4-Pack + 1 ACV $69.00 | Verified (goli.com, 2026-09-25). TikTok-Shop-Preis nicht abrufbar (Anker entfernt; Shop-Seiten liefern nur Header) |
| Discount | Script: "Goli got a sale going on TikTok Shop" / "The sale is on right now" — konkreter Rabatt/Coupon nie beziffert | Claimed (Script) |
| Commission | **Nicht öffentlich verifizierbar.** tommycetty: Health/Beauty "10 to 25% commission" (kjCyL4Vn4P4 [8:43]); "Net profit on TikTok Shop is usually anywhere from 20% to 35%"; außerdem "1% method" (1XO4S9ZKLDY [38:37–38:58]): Plattform-Provision auf 0–1 % gesetzt, Marke zahlt manuell off-platform → in Kalodata/FastMoss wäre für dieses Video kaum Provision sichtbar. Kalodata/FastMoss-Seiten via WebFetch 403/404. | Claimed / Estimated 10–25 % |
| Impulse-Buy-Potenzial | Mittel-hoch: $16–25, Gummies (kein "Pillen"-Widerstand — Script adressiert das explizit: "no nasty powders, no horse pills"), bekannte Marke (Goli: 600.500 TikTok-Follower, verifizierter Seller @golinutrition), Scarcity-CTA ("sells out fast") | Estimated |
| Problem → Lösung | Müdigkeit, geschwollene Beine, Bluthochdruck/Herz, "Männer-Performance" → Nitric-Oxide-Narrativ → Gummies | Verified (Script) |
| Zielgruppe | Schwarze US-Community 45+, religiös-familiäres Milieu; Ansprache "baby", "our community" | Verified (Hashtags, Script, Kommentare) |

---

## 5. Distribution

- **Traffic-Quellen (Estimated):** ≈ 95 % FYP/Feed + Spark-Ads-Boost; Search ≈ 0–5 % (keine Suchbegriffe in Titeln, keine Produktnamen-Formate); Shop-Tab: nicht messbar, da kein Produkt-Anker mehr vorhanden. Alle 10 Dezember-Produktvideos außer dem letzten tragen `isAd=true` → Werbe-Autorisierung gesetzt (Spark Ads durch Marke oder Creator möglich; tatsächlicher Ad-Spend nicht öffentlich). Das Top-Video ist ebenfalls `isAd=true`; ob die 287k Plays organisch oder bezahlt kamen, ist nicht verifizierbar.
- **View-Verteilung:** Top-Produktvideo 287.100 Plays vs. Median der Folge-Videos ≈ 1.500 → Faktor ≈ 190. Über die 12 verifizierten Videos: 52,5 % im Top-Produktvideo, 96,9 % in den zwei viralen Videos. Account-Gesamtviews (Estimated): 100.300 Likes gesamt − 56.400 Likes der zwei viralen Videos = 43.900 Likes für die übrigen ~106 Videos; bei der beobachteten Like-Rate der Produktvideos (1,8–3,6 %) ⇒ ≈ 1,2–2,4 Mio. Plays für den Rest ⇒ Account gesamt ≈ 1,7–2,9 Mio. Plays, d. h. es gab vermutlich weitere mittelgroße Videos (Nov 2025), die nicht mehr listbar sind.
- **Follower-Farming:** Video #1 (Soldaten, 10 s, #backtheblue #followme, 242.800 Plays, 45.900 Likes, 6.126 Kommentare "thank you for your service") ist ein reines Reichweiten-/Follower-Video ohne Produkt — plausibel zum Erreichen der 5.000-Follower-Affiliate-Schwelle (Account 2 Wochen alt). Seit dem Watch-Tool-Ausfall nicht sichtbar geprüft; TikTok setzt hier `ShowAIGC=true` (AI-Label), das Cover wirkt wie ein reales Selfie-Video (möglich: KI-animiertes/übernommenes Material).
- **Posting-Volumen (Verified):** 108 Videos zwischen 2025-10-29 und 2025-12-10 (43 Tage) ≈ **2,5 Videos/Tag**; am 09.12.2025 allein 5 Produktvideos (17:14, 18:37, 20:27, 21:56, 23:31 UTC), am 08.12. drei. Danach Stopp.
- **Schwester-Accounts (Verified):** @holistic.granny — 128 Videos in 36 Tagen (≈ 3,6/Tag), Uploads am 07.–10.12.2025 jeweils 1–10 Minuten vor/nach den healthiswealthfyp-Uploads (z. B. 7582309243169131831 um 19:13 UTC vs. 7582311866911821111 um 19:23 UTC), gleiche Hashtags, gleicher Disclaimer, gleiches Script-Skelett mit anderem Avatar (Headwrap, Garten, rohe Rüben), Reichweite deutlich kleiner (232–1.707 Plays). Zwei weitere getestete Handles (@stellaryan — Sticker-Name im Video #3 — und @healthiswealth) sind fremde/leere Accounts. tommycetty nennt zudem @holistic.sophia (heute brasilianischer Privataccount, Handle recycelt) und betreibt laut eigener Aussage "~11 phones" mit je einem Account. Instagram/YouTube-Crossposting unter dem Handle: instagram.com/healthiswealthfyp → HTTP 429 (nicht prüfbar), youtube.com/@healthiswealthfyp → 404 (existiert nicht).
- **Varianten:** ja — mind. 11 Varianten desselben Beetroot-Scripts mit 5 Hook-Familien und 3 Avataren auf zwei Accounts innerhalb von 4 Tagen (07.–10.12.2025) = systematisches Hook-Testing nach dem Viral-Treffer vom 27.11.

---

## 6. Schwester-Account @holistic.granny (Verified, Abruf 2026-09-25)

| Video-ID | Datum (UTC) | Länge | Plays | Likes | isAd | Beschreibung (Auszug) |
|---|---|---|---|---|---|---|
| 7582311866911821111 | 2025-12-10 19:23 | 94 s | 780 | 25 | true | "They don't want to see us be educated but GRANNY has you covered!" |
| 7582011401456078094 | 2025-12-09 23:57 | 83 s | 1.707 | 48 | true | "We NEED to stand together!" — Hook [00:00] "Baby, let me tell you something, they never wanted us to know this." CTA [01:17] "Tap that orange cart before it sells out." Script: "If your legs swell up every evening, you need beetroot. If you're exhausted before lunch, you need Q10 … if you go buy all that separately, you're spending $80, $90 … That's why I take Goli Beetroot gummies, one bottle, everything I just said." |
| 7581981494025932045 | 2025-12-09 22:01 | 83 s | 811 | 22 | true | "Pay attention!" |
| 7581962668857232654 | 2025-12-09 20:48 | 82 s | 665 | 18 | true | "It's time to listen to GRANNY!" |
| 7581926239384980750 | 2025-12-09 18:26 | 84 s | 840 | 20 | true | "Take action TODAY!" |
| 7581903771215613239 | 2025-12-09 16:59 | 80 s | 568 | 11 | true | "I hope Granny's words help you!" |
| 7581600499699338509 | 2025-12-08 21:22 | 125 s | 877 | 15 | true | "GRANNY is onto something" |
| 7581558291470290190 | 2025-12-08 18:38 | 120 s | 886 | 15 | true | "GRANNY knows a thing or two" |
| 7581521511362628919 | 2025-12-08 16:16 | 99 s | 881 | 15 | true | "GRANNY loves you all!" |
| 7581237515126951182 | 2025-12-07 21:54 | 120 s | 232 | 13 | false | "I hope this helps you!" (ShowAIGC=true) |

Auf dem Schwester-Account wurde parallel eine **kürzere** Variante (80–95 s, "Stacking"-Pitch: Beetroot + CoQ10 + B12 statt "$80–90 für fünf Pillen") getestet. Reichweite ohne Viral-Treffer: Median ≈ 830 Plays.

---

## 7. Wettbewerbsvorteil — was ist es wirklich?

**Kernaussage:** Der Vorteil ist **nicht** die AI-Technik an sich, sondern die Kombination aus (1) einem präzise auf eine unterversorgte Demografie zugeschnittenen Avatar + Script (Schwarze Großmutter, Kirchen-/Familien-Register, Verschwörungs-Frame "they don't want us to know") und (2) sehr billiger, schneller Variantenproduktion (11+ Scriptvarianten in 4 Tagen auf 2 Accounts). AI ist der Enabler, der (1) überhaupt erst möglich macht ("with AI, we have an unfair advantage of literally being able to be anybody we want" — tommycetty), und (2) auf ~$0 Grenzkosten drückt.

| Faktor | Evidenz | Gewicht |
|---|---|---|
| **Demografie-/Persona-Arbitrage** (AI-Avatar als "Trusted Messenger" einer Community, die kaum von echten Creators mit diesem Produkt bespielt wird) | Verified: Script, Hashtags, 617 Kommentare ohne AI-Pushback, 100 % Zustimmungston; Claimed: tommycetty erklärt die Strategie explizit | **hoch** |
| **Script/Story (Mittelfunnel-Long-Form, 2–3 min, Verlust → Feindbild → Ahnenwissen → Mechanismus → Produkt → Scarcity)** | Verified: 11 Varianten mit identischem Skelett; 704 Kommentare + 1.617 Shares + 1.388 Saves (Share-Rate 0,56 %, Save-Rate 0,48 % — hoch für Werbe-Content) | **hoch** |
| **Billige Produktion + schnelles Hook-Testing** | Verified: 2,5–3,6 Videos/Tag, 5 Hook-Familien, 3 Avatare, kein B-Roll, 1 Szene, keine Musik | mittel-hoch |
| **AI-Avatar/-Stimme** | Verified (Watch 2026-09-24): AI-Avatar, AI-Stimme; kein einziger AI-Kommentar in 617 → Realismus reicht für die Zielgruppe aus | mittel (Enabler) |
| **Produktwahl** (bekannte Marke Goli, $16–25, Gummy-Format, "Bluthochdruck"-Nische mit hoher Prävalenz in der Zielgruppe) | Verified Preis/Marke; Claimed Provision 10–25 % | mittel |
| **Paid Boost** | Verified `isAd=true` auf 10 von 11 Produktvideos → Spark-Ads-Autorisierung; Spend unbekannt | unklar (kann den 287k-Ausreißer teilweise erklären) |
| **Volumen/Multi-Account** | Verified: 2 Accounts, 236 Videos in 6 Wochen; Claimed: 11 Geräte | mittel |
| **Kommission/Deal** | Claimed: "1% method" (off-platform-Zahlung) — falls wahr, Netto-Marge höher als Standard-Affiliate, aber nicht replizierbar für Einsteiger | niedrig (unbelegt) |
| **Trend-Arbitrage** | nein — "Granny"-Testimonials und Beetroot/NO sind Evergreen | – |

**Gegenevidenz/Grenzen:** (a) Reichweite ist extrem schief: 1 von ≈ 106 Produktvideos trägt >50 % der verifizierten Views; die Hook-Varianten nach dem Hit erreichten nur 1–3k Plays trotz `isAd=true` — das Format skaliert **nicht** planbar. (b) Beide Accounts wurden am 10.12.2025 abrupt beendet (Ban, Affiliate-Verlust oder Umzug auf die Januar-Challenge-Accounts — nicht verifizierbar; tommycetty berichtet selbst von Bans). (c) Produktanker heute entfernt → Long-Tail-Umsatz = 0. (d) Regulatorik: Krankheits-Claims + fiktive 82-jährige "Nutzerin" ohne echtes Testimonial = in USA FTC-Risiko (Endorsement Guides), in DE/EU nicht zulässig (HCVO, UWG, KI-Kennzeichnung).

---

## 8. Einkommensschätzung (Estimated — keine Quelle publiziert GMV)

Formel: Provision = Views × CTR (Klick auf Produktkarte) × CVR (Klick→Order) × Preis × Provisionssatz.
Annahmen: CTR 1–5 % (Mittel 3 %), CVR 2–10 % (Mittel 5 %), Preis $16–25 (Mittel $20; TikTok-Shop-Preis unbekannt, goli.com $15.98–24.97), Provision 10–25 % (Mittel 15 %; Claimed-Spanne).

**A) Top-Video allein (287.100 Plays, Verified):**
- Min: 287.100 × 1 % × 2 % = 57 Orders × $16 × 10 % ≈ **$92**
- Mittel: 287.100 × 3 % × 5 % = 431 Orders × $20 × 15 % ≈ **$1.290** (GMV ≈ $8.600)
- Max: 287.100 × 5 % × 10 % = 1.436 Orders × $25 × 25 % ≈ **$8.970** (GMV ≈ $35.900)
- Claimed (tommycetty, 1XO4S9ZKLDY [37:11]): "This video alone made me just around 10K in commission … December of 2025" → entspräche bei 20–25 % Provision $40–50k GMV ≈ $140–175 GMV pro 1.000 Views — 2–5× über seinen eigenen Best-Case-Benchmarks ($29–71 GMV/1k Views, kjCyL4Vn4P4 [1:24]) und nur mit gleichzeitigem Maximum aller Parameter (oder mit nicht im playCount enthaltenen Ad-Views) erreichbar. → Konfidenz für "$10K aus diesem Video": niedrig.

**B) Account-Lebenszeit (≈ 6 Wochen, Nov–Dez 2025), Produktvideos gesamt (Estimated 1,2–2,4 Mio. Plays, s. §5):**
- Long-Tail konvertiert schlechter als der Hit; Ansatz: Hit wie A) + Rest mit halber Mittel-Rate: 1,5 Mio. × 3 % × 2,5 % × $20 × 15 % ≈ $3.400 (Mittel), Spanne ≈ $300–15.000.
- **Band für den besten Monat (Nov/Dez 2025): ≈ $1.500–5.000 Provision** (Mittel ≈ $3–4k; inkl. Schwester-Account +10–20 %), Claimed-Obergrenze $10k+.
- **Aktuell (seit 2025-12-10): ≈ $0/Monat** — keine Uploads, Produktanker entfernt, Kommentar "at not there anymore how order" belegt die tote Produktkarte.

Kostenseite (Estimated): AI-Stack (Nano Banana Pro/Gemini, ElevenLabs, HeyGen/Hedra) ≈ $100–300/Monat, kein Produktkauf nötig ("You don't even have to have the product" — tommycetty), Zeit ≈ 1–2 h/Tag für 3–5 Videos.

---

## 9. Fazit (Konfidenz)

- **Verified:** Format (AI-Granny, 2–3-min-Mittelfunnel-Testimonial, Goli Beets Cardio Gummies, orange Shop-Karte als CTA), 12 Videos mit Statistiken, 11 Script-Varianten, 5 Hook-Familien, Schwester-Account @holistic.granny mit synchronem Posting, Preisniveau $16–25, Kommentar-Reaktion (kein AI-Pushback), Inaktivität seit 2025-12-10.
- **Claimed:** Betreiber tommycetty (Script-Match stark), "$10K Provision aus dem Video", Provision 10–25 %/"1% method".
- **Estimated:** bester Monat $1,5–5k Provision; heute $0.
- **Konfidenz Gesamtbewertung: MEDIUM** — Content-Mechanik und Distribution sind aus Primärdaten belegt; Umsatz und Provision hängen an Selbstauskünften eines Kursverkäufers.
- **Übertragbarkeit DE/EU:** gering — Krankheits-Claims (HCVO), fingiertes Testimonial (UWG §5a, Anhang Nr. 23b), KI-Kennzeichnungspflicht (AI Act Art. 50 ab 08/2026) und deutlich kleinerer TikTok-Shop-Supplement-Katalog.

---

## Quellen (Zugriff 2026-09-24/25)
- https://www.tiktok.com/@healthiswealthfyp (Profil-JSON) · Videos: /video/7572439019821288717, /video/7577483914822913294, /video/7581235294125509902, /video/7581530187116973367, /video/7581553951821122871, /video/7581594903277227319, /video/7581907677987507470, /video/7581928988357004599, /video/7581957291071655223, /video/7581980253350808845, /video/7582004938746727694, /video/7582309243169131831 (SSR-JSON, ASR-WebVTT, stickersOnItem, Cover); Kommentar-API `api/comment/list` (617 von 704 Kommentaren des Top-Videos; je 3–6 Kommentare der Dezember-Videos; 49 des Soldaten-Videos).
- https://www.tiktok.com/@holistic.granny (Profil + 10 Videos, 2 ASR-Transkripte, 1 Cover).
- https://www.tiktok.com/@golinutrition (Verified Seller, 600.500 Follower) · https://goli.com/products.json (Preise Beets Cardio Gummies).
- YouTube tommycetty: kjCyL4Vn4P4 (Transkript [3:30], [8:43], [10:29], [11:31–12:13]) und 1XO4S9ZKLDY ([10:34–12:42], [29:28], [36:29–38:58]) — lokal research/yt_tx/.
- Watch-Auswertung des Top-Videos vom 2026-09-24 (research/claims_checked.md).
- Nicht erreichbar: Kalodata (403), FastMoss (404), Amazon (503), Walmart (Bot-Check), Instagram (429), goli.com Produktseiten (404; nur Shopify-JSON lieferte Preise).
- Rohdaten: research/reverse/_hw/ (JSON, VTT, JPG, Kommentare).
