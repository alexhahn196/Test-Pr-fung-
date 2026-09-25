# Reverse-Engineering: @healthysmartdeals (TikTok Shop Affiliate, US, Supplements, Modell E/F)

**Stand:** 2026-09-25 (Datenerhebung 2026-09-24/25). **Analyst:** Growth-Reverse-Engineering-Agent.
**Datenbasis:** TikTok-Profil-SSR-JSON (tt_profile.sh), 20 Video-Detailseiten (tt_video.sh), 4 heruntergeladene Videodateien inkl. TikTok-ASR-Untertitel (WebVTT) und Frame-/Szenenanalyse per ffmpeg (3 Videos), YouTube-Kalodata-Breakdown (Victor Decodes Ecom, NNIhmKGmpVY, Transkript + Videodetails via NexLev), Markenwebsite topluxnutrition.com.
**Tagging:** *Verified* = selbst in TikTok-Daten/Primärquelle gesehen; *Claimed* = Behauptung Dritter; *Estimated* = eigene Rechnung (Formel angegeben).
**Einschränkung:** Das NexLev-Watch-Tool war heute ausgeschöpft (15/15). Ersatz: die Videos wurden direkt heruntergeladen; Hook/Struktur/CTA stammen aus TikToks eigenen ASR-Untertiteln (wortgenau, mit Timestamps), Visuals aus 1-fps-Frame-Sheets und ffmpeg-Szenenerkennung. Die **Stimme** konnte nicht angehört werden (kein Audio-Verständnis) – die Einstufung "AI-Voice" ist deshalb *Claimed* (YouTuber) + Indizien.

---

## 0. Kurzfazit

- Affiliate-Account (kein Seller), US-TikTok-Shop-Supplements (Toplux Magnesium Complex, Goli Zero Sugar Trio, Cutler Nutrition Liquid Carnitine, Strength Cartel Creatine Gummies, Leefar Cutting Mix, Vev Nutra Magnesium). Hinweis zur Vorgabe "UK": Die Produkte, "Made in USA"-Claims und die Kalodata-Daten sind US; der YouTube-Beleg trägt lediglich den Hashtag #TikTokShopUK. -> **Land: USA** (Verified über Produktset/Sprache; UK nicht belegt).
- **Format (Verified per Frames):** vollständig AI-gerenderte 3D-Animation mit einer **wiederkehrenden Figur** – ein "Röntgen-Skelett-Charakter" (rot glühend = Problemzustand, blau glühend = Lösungszustand, mit Stirnband und Igelfrisur) – plus Produktflasche als 3D-Objekt, Wort-für-Wort-Captions in Großbuchstaben, eingebranntes Wasserzeichen "@healthysmartdeals", TikTok-Shop-Grafiken (oranger Warenkorb, Produktkarte, "LOW STOCK") und **in den letzten ~1–2 s ein echter Handclip** mit dem physischen Produkt.
- **Skript-Template (Verified per ASR, 4 Videos):** Pain-Hook (0–3 s) -> Symptomliste (3–17 s) -> "Ursache" (Magnesiummangel/Cortisol/Regeneration) -> Produkt + USP (8 Formen, 1.000 mg …) -> Trust-Signale (Non-GMO, Made in USA, lab tested, free shipping) -> Social Proof ("rated 4.6, over 700.000/1,2 Mio sold") -> Rabatt/Knappheit -> CTA "tap the orange cart/product icon … there's stock left but it won't stay that way" (letzte 6–8 s).
- **Distribution:** 19/20 Videos `isAd = true` -> die Videos laufen als Spark-/GMV-Max-Anzeigen (vom Seller bezahlt, Affiliate kassiert Provision). Organische Engagement-Rate winzig (1,17 %), Kommentare praktisch null (11 auf 258.664 Views) -> Views sind ad-getrieben, kein Community-/Search-Account.
- **Wettbewerbsvorteil:** Kombination aus (1) ad-tauglicher, wiedererkennbarer AI-Creative-Sprache (Skelett-Charakter, Retention-Editing, 17–28 Schnitte/50 s), (2) striktem, wiederverwendbarem Skript-Template über alle Produkte, (3) Produktauswahl (hochmargige US-Supplement-Bestseller mit hohen Sold-Zahlen), (4) Hook-Varianten pro Produkt (9 von 20 Videos = Toplux Magnesium mit verschiedenen Hooks), (5) Compliance-Signale (Handclip, Disclaimer, Wasserzeichen) – **nicht** Volumen (nur ~7 Videos/Monat im Schnitt) und **nicht** organische Reichweite.
- **Einkommen:** Claimed $68.670 GMV/30 Tage (Kalodata, Mai 2026). Estimated aus verifizierten Views: GMV ~$6k–27k/Monat, Provision **~$1.000–5.000/Monat** in aktiven Monaten; Peak-Monat laut Claimed-GMV ~$7k–14k Provision. **Seit 2026-05-06 keine Uploads mehr** -> aktuell wahrscheinlich nahe null. Confidence: **LOW**.

---

## 1. Profil (Verified, tt_profile.sh 2026-09-25)

| Feld | Wert |
|---|---|
| URL | https://www.tiktok.com/@healthysmartdeals |
| Follower / Likes / Videos | 95.500 / 3.200.000 / 208 |
| Following | 3 |
| Erstellt | 2024-03-27 (createTime 1711579853) |
| Bio | leer; kein bioLink |
| ttSeller / commerceUser | false / false -> Affiliate-Creator, kein Shop-Betreiber |
| verified | false |
| Video-Liste | öffentlich nur die 9 neuesten über die Embed-Seite; neuestes Video 2026-05-06 |

Likes pro Video (Estimated): 3,2 Mio / 208 ≈ 15.400 – deutlich über den Likes der 20 Stichproben-Videos (Ø 125) -> die großen Reichweiten liegen bei älteren Videos (2024–Anfang 2026), die nicht mehr listbar sind (konsistent mit dem Claimed 1,6-Mio-Views-Video).

## 2. Analysierte Videos (n = 20 Verified; 4 davon mit Transkript, 3 mit Frame-Analyse)

Quellen der IDs: Embed-Seite (9 neueste) + Suchmaschinen-Treffer aus dem Vor-Dossier (11). Alle Stats via tt_video.sh am 2026-09-25.

| # | Video-ID (Link) | Datum | Produkt | Views | Likes | Komm. | Shares | Saves | Dauer | isAd | AI-Label | Hook (0–3 s, ASR) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7622112558178143501](https://www.tiktok.com/@healthysmartdeals/video/7622112558178143501) | 2026-03-28 | Leefar Cutting Mix | 16.300 | 102 | 0 | 2 | 7 | 33 s | ja | keins | n. e. (Caption: "Tap the product icon before it's gone.") |
| 2 | [7627866302937337101](https://www.tiktok.com/@healthysmartdeals/video/7627866302937337101) | 2026-04-12 | Strength Cartel Creatine Gummies | 21.000 | 328 | 0 | 13 | 40 | 49 s | ja | keins | n. e. |
| 3 | [7627907941391207694](https://www.tiktok.com/@healthysmartdeals/video/7627907941391207694) | 2026-04-12 | Strength Cartel Creatine Gummies | 7.246 | 63 | 0 | 1 | 4 | 43 s | ja | keins | n. e. (Variante von #2) |
| 4 | [7628745092307668255](https://www.tiktok.com/@healthysmartdeals/video/7628745092307668255) | 2026-04-14 | Toplux Magnesium | 4.630 | 78 | 3 | 4 | 16 | 51 s | ja | keins | n. e. |
| 5 | [7629902645209173261](https://www.tiktok.com/@healthysmartdeals/video/7629902645209173261) | 2026-04-18 | Goli Trio | 1.559 | 12 | 0 | 1 | 1 | 47 s | ja | keins | n. e. |
| 6 | [7630107962530336013](https://www.tiktok.com/@healthysmartdeals/video/7630107962530336013) | 2026-04-18 | Toplux Magnesium | **95.800** | 1.096 | 1 | 30 | 224 | 50 s | ja | keins | 0:00–3,6 s "magnesium is the one thing your body uses every day" / On-Screen: MAGNESIUM |
| 7 | [7630572586782428430](https://www.tiktok.com/@healthysmartdeals/video/7630572586782428430) | 2026-04-19 | Cutler Liquid Carnitine | 6.318 | 50 | 0 | 0 | 5 | 46 s | ja | keins | n. e. |
| 8 | [7630800207780826382](https://www.tiktok.com/@healthysmartdeals/video/7630800207780826382) | 2026-04-20 | Toplux Magnesium | 2.259 | 12 | 0 | 1 | 1 | 49 s | ja | keins | n. e. |
| 9 | [7631176909543525645](https://www.tiktok.com/@healthysmartdeals/video/7631176909543525645) | 2026-04-21 | Cutler Liquid Carnitine | 13.700 | 159 | 0 | 7 | 15 | 48 s | ja | keins | 0:00–1,9 s "You ever push hard at the gym, feel great, then wake up the next day barely able to move?" |
| 10 | [7633599038251666701](https://www.tiktok.com/@healthysmartdeals/video/7633599038251666701) | 2026-04-28 | Goli Trio | 16.100 | 67 | 0 | 16 | 12 | 48 s | ja | keins | n. e. |
| 11 | [7635099527178882317](https://www.tiktok.com/@healthysmartdeals/video/7635099527178882317) | 2026-05-02 | Goli Zero Sugar Trio (Muttertag) | 22.500 | 87 | 3 | 4 | 8 | 50 s | ja | keins | 0:00–3,4 s "If your mom looks in the mirror and doesn't like what she sees." / On-Screen: IF / MOM / MIRROR |
| 12 | [7636412488162037006](https://www.tiktok.com/@healthysmartdeals/video/7636412488162037006) | 2026-05-05 | Toplux Magnesium | 2.459 | 32 | 0 | 7 | 11 | 51 s | ja | keins | n. e. |
| 13 | [7636426709885144333](https://www.tiktok.com/@healthysmartdeals/video/7636426709885144333) | 2026-05-05 | Vev Nutra Deep Calm Magnesium | 1.339 | 10 | 0 | 0 | 4 | 51 s | ja | keins | n. e. |
| 14 | [7636438082656537869](https://www.tiktok.com/@healthysmartdeals/video/7636438082656537869) | 2026-05-05 | Toplux Magnesium | 3.761 | 35 | 1 | 1 | 9 | 48 s | ja | keins | n. e. |
| 15 | [7636548512762645773](https://www.tiktok.com/@healthysmartdeals/video/7636548512762645773) | 2026-05-05 | Vev Nutra Deep Calm Magnesium | 6.864 | 53 | 0 | 0 | 12 | 48 s | ja | keins | n. e. |
| 16 | [7636591701489995022](https://www.tiktok.com/@healthysmartdeals/video/7636591701489995022) | 2026-05-06 | Goli Trio | 13.100 | 53 | 1 | 4 | 6 | 45 s | ja | keins | n. e. |
| 17 | [7636755918213909774](https://www.tiktok.com/@healthysmartdeals/video/7636755918213909774) | 2026-05-06 | Toplux Magnesium | 5.875 | 56 | 0 | 1 | 5 | 41 s | ja | keins | n. e. |
| 18 | [7636782470456691982](https://www.tiktok.com/@healthysmartdeals/video/7636782470456691982) | 2026-05-06 | Toplux Magnesium | 1.850 | 18 | 0 | 2 | 2 | 50 s | ja | keins | n. e. |
| 19 | [7636795064089447694](https://www.tiktok.com/@healthysmartdeals/video/7636795064089447694) | 2026-05-06 | Toplux Magnesium | 14.900 | 139 | 0 | 14 | 25 | 44 s | ja | keins | n. e. |
| 20 | [7636932117317864718](https://www.tiktok.com/@healthysmartdeals/video/7636932117317864718) | 2026-05-06 | Toplux Magnesium (neuestes Video) | 1.104 | 47 | 2 | 1 | 12 | 49 s | **nein** | keins | 0:00–3,4 s "What happens when your body finally has enough magnesium?" / On-Screen: WHAT |

n. e. = nicht extrahiert (kein Download). AI-Label: `aigcLabelType = null`, `AIGCDescription = ""` bei allen 20 (Verified) – **kein TikTok-AI-Label**, obwohl die Visuals komplett AI-generiert sind. Jedes Video hat 5 Hashtags, keinen `anchors`-Eintrag im SSR (Produktkarte bei Ad-Videos headless nicht sichtbar; im Video selbst ist die TikTok-Shop-Karte als Grafik eingebaut, s. u.).

**Stichproben-Kennzahlen (Verified/Estimated):** Summe 258.664 Views, Ø 12.933, Median 6.591, Max 95.800. Top-Video = 37 % aller Views, Top-3 = 54 %. Likes/Views 0,97 %, Gesamt-Engagement (Likes+Komm.+Shares+Saves)/Views **1,17 %**, nur 11 Kommentare insgesamt. Views je Produkt: Toplux 9 Videos / 132.638 (Ø 14.738), Goli 4 / 53.259, Strength Cartel 2 / 28.246, Cutler 2 / 20.018, Vev Nutra 2 / 8.203, Leefar 1 / 16.300.

### 2.1 Video 6 – Top-Video, Toplux Magnesium Complex (95.800 Views, 50 s, 17 Schnitte bei Schwelle 0,25)

Struktur (Timestamps aus ASR + Szenenerkennung, Verified):
- **0:00–3,6 Hook:** "magnesium is the one thing your body uses every day" – Bild: rotes, glühendes Skelett kauert im dunklen Schlafzimmer über einem Wäschekorb (Erschöpfung), Wort-Caption "MAGNESIUM".
- **3,6–12,7 Problem-Verstärkung:** "and nobody has enough of it / you burn through it when you're stressed / … working out / … when you don't sleep / food doesn't come close" – rotes Skelett beim Kochen, an der Hantelbank (Schnitte 5,2 / 7,1 / 10,5), Skelett-Arzt im Kittel mit Schild "NOT ENOUGH".
- **12,7–19,6 Symptome:** "that's why you feel tight, wired and worn out even on good days / you just need to give your body what it needs most" – rotes Skelett am Frühstückstisch im Park.
- **19,6–24,2 Produkt-Reveal + USP:** "magnesium pills have one form – Toplux put eight into one capsule" – Farbwechsel auf **blau** (Lösungszustand), Skelett mit Stirnband hält die Flasche, 8 Formen als Labels (Glycinate, Citrate, Malate, Oxide, Taurate, Carbonate, Aspartate, Orotate); Kapsel fällt in die Flasche.
- **24,2–32,6 Nutzen:** "1,000 mg per serving supports relaxation, restful sleep and muscle and leg cramps" – 3D-Badges "1000 MG", Leucht-Icons.
- **32,6–35,5 Trust:** "non GMO, made in USA, lab tested" – Siegel-Badges vor dem Skelett.
- **35,5–41,0 Social Proof:** "1.2 million sold / people who switched say they wind down at night, sleep through and wake up without the tightness" – Counter "1,100,000+ BOTTLES SOLD" -> "1,200,000+", Sprechblasen mit Review-Zitaten, Skelett im Sessel.
- **41,0–48,0 Angebot + CTA (gesprochen):** "if this is what you've been missing I recommend – TikTok Shop has an 82% off – if you see the product icon there's stock left but it won't stay that way" – schwarze TikTok-Figur überreicht die Flasche, gelbes "82 % OFF"-Badge, dann **eingebaute Shop-Grafik**: TikTok-Logo, oranger Warenkorb, Produktkarte "TOPLUX MAGNESIUM COMPLEX – LOW STOCK".
- **~49,1–50,3 Handclip:** echte Hand hält die Toplux-Flasche vor Bett/Sofa (Realfootage, ~1,2 s).

### 2.2 Video 20 – neuestes Video, gleiches Produkt, Benefit-Hook (1.104 Views, 49 s, 20 Schnitte, isAd = false)

- **0:00–3,4 Hook:** "What happens when your body finally has enough magnesium?" – rotes Skelett sitzt gebeugt auf Bettkante bei Nachtlampe.
- **3,5–16,6 Nutzen-Liste (statt Schmerz):** "Your shoulders actually unclench / fall asleep without the racing thoughts / wake up before your alarm / your face stops looking puffy / the 3 PM crash just stops" – blaues Skelett im Bett, Bad, Büro.
- **16,7–21,2 Problem-Rahmung:** "Most people never feel this. They've been low for years without knowing it." – rote Skelette im Wartezimmer.
- **21,2–36,6 Produkt + 8 Formen:** "That's why I switched to Toplux magnesium complex. Eight forms in one capsule at 1,000 mg. Glycinate for sleep… Citrate for the bloat… Malate for muscles… Carbonate for puffiness" – Skelett auf Tron-artigem Grid, Skelett-Arzt zeigt auf Tafel mit 8 Kapseln.
- **36,6–46,8 Trust + Social Proof:** "Most magnesium has one form. Your body uses all eight. Non GMO, lab tested, free shipping, rated 4.6 with over 700,000 sold" – eingebaute Grafik "TikTok Shop ★★★★★ 4.6 – 700,000+ SOLD".
- **46,8–49,8 CTA:** "If you want that, tap the orange cart while stock lasts." – oranger Warenkorb neben Flasche; **Handclip** (ca. 48,8–49,8 s).
- Bemerkung: Dasselbe Produkt wie Video 6, 18 Tage später, mit umgedrehtem Hook (Benefit statt Pain) und variierter Social-Proof-Zahl (700k statt 1,2 Mio) -> klassisches **Hook-Variantentesten**.

### 2.3 Video 11 – Goli Zero Sugar Trio, Muttertags-Angle (22.500 Views, 50 s, 28 Schnitte)

- **0:00–3,4 Hook:** "If your mom looks in the mirror and doesn't like what she sees." – rotes Skelett mit dunklen Haaren (weibliche Figur) vor Badezimmerspiegel.
- **3,4–15,2 Symptome:** "face looks puffy in every photo / belly won't go away / wakes up exhausted and can't stop snacking at night".
- **15,2–23,0 Ursache:** "That isn't getting older. That isn't her fault. She just has high cortisol. When cortisol stays high, sleep breaks, face puffs, cravings spike" – Skelett-Arzt vor "CORTISOL"-Tafel, Skelett im Bett um 3:11 Uhr.
- **23,0–35,9 Produkt:** "This Mother's Day, give her the Goli Zero Sugar Trio. Three best sellers in one. ACV for cravings and bloating, Ashwagandha for stress and sleep, pre/pro/postbiotic for gut health" – blaues Skelett öffnet rosa Geschenkbox, drei Flaschen mit Icon-Labels.
- **35,9–42,9 Trust/Proof:** "Zero sugar, vegan, gluten free, free shipping. Rated 4.5 with over 800,000 sold" – Badges, Counter "291,835+ -> 800,000+ SOLD", Sterne-Grafik.
- **42,9–48,4 Emotionaler Abschluss + CTA:** "She's been giving everything. Give her something back. Tap the orange card if you see the shopping cart icon. There's stock left, but it won't stay that way." – Produktkarte "GOLI ZERO SUGAR TRIO – IN STOCK", oranger Warenkorb.
- **~49,4–50,8 Handclip:** Hand hält die rote Goli-Geschenkbox mit den drei Flaschen auf einem Bett.

### 2.4 Video 9 – Cutler Nutrition Liquid Carnitine (13.700 Views, 48 s; nur ASR)

Hook 0:00–1,9 "You ever push hard at the gym, feel great, then wake up the next day barely able to move?" -> Skip-Spirale (5,7–12,9) -> Ursache "Your body just isn't recovering fast enough" (13–18) -> Identitäts-Hook "That version of you that hits the gym four or five times a week exists" (18–22) -> Produkt "liquid carnitine by Cutler … 3,000 mg in one tablespoon, stimulant free, sour gummy worm flavour" (24–33) -> "Over 1 million sold, reviews say…" (33–42) -> "TikTok Shop has it on a flash sale. If you see the product icon, there's stock left. But it won't stay that way." (42–48).

## 3. Content-Formel (Verified aus Frames/ASR, sofern nicht anders markiert)

| Element | Befund |
|---|---|
| **Hook-Pattern** | 100 % Pain-/Symptom- oder "What happens when"-Hook, direkt an "you"/"your mom"; erstes Wort als große Caption; Szene = rote Skelett-Figur in Alltagssituation (Schlafzimmer, Spiegel, Gym). Kein Gesicht, kein Creator. Kein Texttitel-Overlay außer dem Wort-für-Wort-Caption. |
| **Struktur** | 8-Stufen-Template (Pain -> Symptomliste -> Ursache -> Produkt+USP -> Nutzen -> Trust-Badges -> Social Proof mit Sold-Counter -> Rabatt/Knappheit -> CTA). Dauer 41–51 s (Ø ~47 s), CTA immer in den letzten 6–8 s. |
| **CTA** | "Tap the orange cart/card (if you see the product/shopping-cart icon) – there's stock left but it won't stay that way" (wortgleich in 4/4 Transkripten); Rabatt-Anker "82 % off" / "53 % off" / "flash sale" (Claimed im Video, nicht verifiziert). Visuell: eingebaute TikTok-Shop-Grafik (Logo, oranger Warenkorb, Produktkarte "LOW STOCK"/"IN STOCK") – d. h. die Produktkarte wird **im Video nachgebaut**, nicht nur vom Player eingeblendet. |
| **Produktdarstellung** | AI-gerendertes 3D-Modell der echten Verpackung in ~60–70 % der Szenen (vom Skelett gehalten, auf Tisch, im Geschenkkarton, mit Badges); Sold-Counter; Review-Sprechblasen; **1 realer Handclip (~1–2 s) am Ende**. Kein Before/After, keine Stock-Footage, kein Packaging-Unboxing. |
| **Voice-over** | Männliche, ruhige, erklärende Stimme (Claimed: YouTuber "obviously AI generated"). Indiz aus ASR: Markenname wird als "toplox" / "2+ magnesium" erkannt – typisch für TTS-Aussprache; nicht verifiziert. |
| **Captions** | Ein Wort pro Frame, Versalien, fett, blaue Füllung mit weißer/dunkler Kontur, zentriert im unteren Drittel (~65 % Höhe); darunter dauerhaft Wasserzeichen "@healthysmartdeals". |
| **Musik** | "original sound" (Verified) – Hintergrundmusik laut YouTuber vorhanden (Claimed). |
| **Schnittrate** | 17 / 20 / 28 Szenenwechsel in 49–50 s (Schwelle 0,25) -> Ø 1,8–2,9 s pro Szene; zusätzlich Zoom-/Whip-Transitions und Motion-Blur-Übergänge. |
| **AI-Avatar** | Ja, **konsistente Figur** über alle 3 gesichteten Videos: Röntgen-Skelett (rot = krank, blau = gesund), Igelfrisur + Stirnband; für den Goli-Muttertagsspot als weibliche Variante mit langen Haaren. Zusätzlich Skelett-Arzt und schwarze "TikTok-Figur" als Nebenrollen. Look: Kling/Veo/Sora-artige 3D-Renderings mit leichtem Morphing (Verified Frames). |
| **Realfootage / UGC** | Nur der Handclip am Ende (gleiche Hand, gleiches Bett-Setting in allen 3 Videos -> vermutlich eigenes Material mit physischem Produkt; Estimated). Kein UGC, kein Gesicht. |
| **AI-Label** | Kein TikTok-AIGC-Label (Verified: aigcLabelType null, 20/20). Nur Caption-Disclaimer "This is a visual animation for general information only. Not medical advice." (Verified) – als zweiter Caption-Block (`contents[1]`). |
| **Commission-Badge / Produktkarte** | `anchors = []` im SSR (Verified) -> headless nicht sichtbar; die Karte ist als Grafik im Video; TikToks eigene "Creator earns commission"-Kennzeichnung nicht verifizierbar. |
| **Kommentar-Reaktion** | 11 Kommentare auf 258.664 Views (Verified) -> weder Social Proof noch "this is AI"-Pushback messbar; Kommentare sind nicht deaktiviert (itemCommentStatus 0). Ad-Views erzeugen kaum Kommentare. |
| **Posting-Frequenz** | 208 Videos in 30 Monaten (Ø ~7/Monat, Estimated); in der Stichprobe 9 Uploads am 05./06.05.2026 (Batch-Posting 4–5/Tag), davor 1–2/Tag. Letzter Upload 2026-05-06 -> seit 4,5 Monaten inaktiv (Verified). |

## 4. Offer

| Feld | Befund | Tag |
|---|---|---|
| Produkte | Toplux Nutrition Magnesium Complex (8-in-1, 1.000 mg, 90 Kapseln) – 9/20 Videos; Goli Zero Sugar Trio (ACV + Ashwagandha + Pre/Pro/Postbiotic Gummies) – 4/20; Cutler Nutrition Liquid L-Carnitine 3.000 mg – 2/20; Strength Cartel "Killer" Creatine Gummies – 2/20; Vev Nutra Deep Calm Magnesium – 2/20; Leefar Cutting Drink Mix – 1/20 | Verified (Captions/Frames) |
| Preis | Toplux Magnesium Complex auf topluxnutrition.com: regulär $40,00, Sale $29,97 (Zugriff 2026-09-25). TikTok-Shop-Preis nicht headless abrufbar; im Video "82 % off" behauptet. Goli/Cutler/Strength-Cartel-Preise: nicht öffentlich verifizierbar (Shop-Seiten 404/blockiert); typische Spanne $18–35 | Verified (Toplux-Website) / Claimed (Rabatt) / Estimated (Rest) |
| Rabatt/Coupon | "82 % off", "53 % off on a flash sale", "flash sale" – nur im Voice-over; kein Code | Claimed |
| Provision | Nicht öffentlich verifizierbar (kein Anchor, keine Affiliate-Seite von Toplux erreichbar; @topluxnutrition-Bio: "Creator? Email us for collabs: Affiliate@topluxnutrition.com", Verified im Vor-Dossier). Supplement-Open-Collab-Provisionen in US-TikTok-Shop typischerweise 10–20 % | Estimated |
| Impulskauf-Potenzial | hoch: <$35, Rabatt-/Knappheits-Anker, Symptom-Identifikation ("puffy face", "3 PM crash"), Sold-Counter; Muttertags-Geschenk-Angle als saisonaler Trigger | Estimated |
| Problem/Lösung | Schlaf, Bloating, Cortisol/Stress, Muskelkater/Regeneration, Heißhunger -> jeweils "ein Mangel" als Ursache, Produkt als Ein-Kapsel-Lösung | Verified (Skripte) |
| Zielgruppe | US-Erwachsene 25–55, gestresste Berufstätige / Mütter (Goli), Gym-Gänger (Cutler, Strength Cartel), Abnehm-Interessierte (Leefar); direkte "you"-Ansprache | Estimated |

## 5. Distribution

- **Paid vs. organisch:** 19/20 Videos `isAd = true` (Verified). Das ist das Signatur-Muster von Seller-finanziertem GMV Max / Spark Ads auf Affiliate-Content: der Seller bezahlt die Ausspielung, der Affiliate erhält die Provision. Der YouTube-Beleg bestätigt: "All of them are coming up as ads … part of the TikTok GMV Max system" (Claimed). Das einzige Nicht-Ad-Video (#20) hat mit 1.104 Views die geringste Reichweite -> **organische Baseline ≈ 1–2k Views/Video**, alles darüber ist Ad-Reichweite (Estimated).
- **Search-Traffic:** Captions sind SEO-artig ("Magnesium glycinate can help with relaxation and sleep quality…"), TikTok hängt `suggestedWords` wie "magnesium glycinate", "magnesium complex", "types of magnesium" an (Verified) und `diversificationLabels` = Health & Wellness / Fitness & Health. Search-Anteil trotzdem gering geschätzt (<10 %), weil die Reichweite an isAd hängt und die Hashtags Markennamen statt Suchbegriffe sind (Estimated).
- **Shop-Tab/Produktkarte:** nicht messbar (kein Anchor im SSR).
- **Verteilung:** Top-Video 37 % der Stichproben-Views, Top-3 54 %, Median 6,6k -> Reichweite hängt an wenigen von GMV Max "ausgewählten" Creatives; der Rest sind Tests.
- **Varianten:** Ja – 9 Toplux-Videos in 3 Wochen mit unterschiedlichen Hooks (Pain vs. Benefit vs. "8 Formen"), 2 Creatine-Videos am selben Tag, 2 Vev-Nutra-Videos am selben Tag -> **Hook-Variantentesten pro Produkt** (Verified über Captions/Datum, Hooks nur bei 4 Videos gelesen).
- **Schwester-Accounts / Crossposting:** Bio leer, keine Handles in Captions, keine Handles im YouTube-Beleg. instagram.com/healthysmartdeals -> 429 (nicht prüfbar); youtube.com/@healthysmartdeals -> 404 (nicht vorhanden). **Keine Schwester-Accounts belegbar.** Das eingebrannte Wasserzeichen "@healthysmartdeals" spricht gegen Multi-Account-Recycling desselben Materials.
- **Volumen:** ~7 Videos/Monat im Langzeitschnitt, Bursts von 4–5/Tag; kein Massen-Volumen-Play (im Vergleich: pinecommerce 509 Videos).

## 6. Wettbewerbsvorteil – Bewertung

| Faktor | Beitrag | Evidenz |
|---|---|---|
| AI-Produktion (wiedererkennbarer 3D-Skelett-Charakter, Retention-Editing) | **hoch** – die Creatives sind ad-tauglich, ohne Gesicht, ohne UGC-Kosten; Format hebt sich von generischem AI-Avatar-Slop ab | Verified (Frames) |
| Skript-Template + Hook-Varianten | **hoch** – gleiche 8-Stufen-Struktur, wortgleiche CTA, pro Produkt mehrere Hooks | Verified (ASR 4/4, Datum/Captions) |
| Produktauswahl (US-Supplement-Bestseller mit >700k "sold", Toplux mit Claimed $2,7 Mio/30 T. Produkt-GMV) | **hoch** – hohe Marge/Provision, Impulspreis, bereits massiv beworbene Marken | Claimed (Kalodata via YouTube) / Verified (Sold-Claims im Video) |
| Paid Distribution durch Seller (GMV Max/Spark) | **entscheidend** – 19/20 isAd; ohne Seller-Ads läge das Video bei ~1k Views | Verified |
| Compliance-Signale (Handclip, Disclaimer, Wasserzeichen, Produkt sichtbar) | mittel – reduziert Slop-/Flag-Risiko, macht Creatives für GMV Max annehmbar | Verified (Frames/Caption) |
| Volumen | gering – ~7/Monat | Verified |
| Organische Reichweite / Community / Search | gering – 1,17 % Engagement, 11 Kommentare | Verified |
| Trend-Arbitrage | gering/situativ – Muttertags-Angle | Verified (1 Video) |

**Fazit:** Der reale Vorteil ist die **Kombination aus günstig produzierbaren, ad-tauglichen AI-Creatives mit konsistentem Charakter + striktem Conversion-Skript + Auswahl hochvolumiger Supplement-Produkte, deren Seller die Ausspielung per GMV Max bezahlen**. Der Account "kauft" keine Reichweite selbst und ist kein organischer Creator; er liefert Anzeigen-Material im Affiliate-Modell. Evidenzstärke: Format/Skript/isAd **hoch (Verified)**, Umsatz **niedrig (nur Kalodata-Claim)**.

## 7. Einkommensschätzung

**Claimed:** $68.670 GMV in 30 Tagen (Kalodata-Screenshot, beschrieben von Victor Decodes Ecom, YouTube 2026-05-04, 192 Views); Top-Video $23.180 Umsatz bei 1,6 Mio Views. Screenshot nicht selbst gesehen; Kalodata = Drittanbieter-Schätzung. Nicht öffentlich verifizierbar.

**Estimated (Formel: Views × CTR × CVR × Preis × Provision):**
- Views: 258.664 Views / 40 Tage (Verified) ≈ 6.470/Tag ≈ **194.000/Monat** (aktive Phase, inkl. Ad-Views im playCount).
- CTR 2–5 % (Produktkarte), CVR 3–8 %, Preis $25–35, Provision 10–20 %.
- Mittelwert: 194.000 × 3 % × 6 % × $30 = **$10.500 GMV** -> × 15 % = **~$1.570 Provision/Monat**.
- Spanne: 194.000 × 2 % × 3 % × $25 × 10 % ≈ **$290** bis 194.000 × 5 % × 8 % × $35 × 20 % ≈ **$5.400** Provision/Monat; GMV-Spanne $2.900–27.000.
- Claimed-basiertes Peak-Szenario: $68.670 × 10–20 % = **$6.900–13.700 Provision** im Mai 2026 – setzt Ad-Views/ältere Viralvideos voraus, die in unserer Stichprobe nicht sichtbar sind (Faktor 2,5–7 über Estimated-Mittel).
- **Aktuell (Sept. 2026):** keine Uploads seit 2026-05-06; Rest-Umsatz nur, falls Seller alte Creatives weiter in GMV Max laufen lassen -> **Estimated ≈ $0–1.000/Monat**.
- **Band für den Bericht:** aktive Monate ~$1.000–5.000 Provision (Estimated), Peak-Monat bis ~$10k (Claimed-basiert). **Confidence: LOW.**

Kostenseite (Estimated, für die Marge des Betreibers): AI-Video-Tools (Kling/Veo/Runway-Klasse + ElevenLabs-Klasse + Editing) ~$100–300/Monat; keine Ad-Kosten, da Seller-finanziert; Produktmuster kostenlos (Affiliate-Samples, Handclip).

## 8. Risiken / Warum es (nicht mehr) läuft

- Kein AIGC-Label bei komplett AI-generierten Visuals (Verified) – Verstoßrisiko gegen TikToks AI-Kennzeichnungspflicht; Shop-Content-Policy gegen "AI-slop"; gesundheitsbezogene Claims ("puffy face", "cortisol", "sold"-Zahlen) FTC-/Shop-sensibel; Rabatt-Claims ("82 % off") nicht belegt.
- Vollständige Abhängigkeit vom Seller-Ad-Budget (isAd) – fällt die Aufnahme in GMV Max weg, bleibt ~1k organische Views/Video.
- Inaktivität seit 06.05.2026 und leere Bio (früherer Snapshot: "Promoting Products I Truly Believe In" + Gmail, Claimed) sprechen für Pause, Einschränkung oder Abschaltung – Ursache nicht öffentlich verifizierbar.

## 9. Übertragbares Playbook (aus den Verified-Mustern)

1. Einen **konsistenten AI-Charakter** (nicht-menschlich, kein Gesicht -> weniger Uncanny-Valley, kein Likeness-Risiko) mit Problem-/Lösungs-Farbcode etablieren.
2. **8-Stufen-Skript** (Pain-Hook -> Symptome -> Ursache -> Produkt+USP -> Nutzen -> Trust -> Social Proof -> Knappheit+CTA), 45–50 s, CTA in den letzten 7 s, wortgleicher CTA-Satz.
3. Wort-für-Wort-Captions, Schnitt alle ~2 s, Produkt-3D-Modell in >60 % der Szenen, Sold-Counter und Review-Bubbles als Grafik.
4. **Realer Handclip** mit dem physischen Produkt (1–2 s am Ende) + Caption-Disclaimer + Wasserzeichen.
5. Pro Produkt 3–9 Hook-Varianten in wenigen Tagen posten; Produkte mit hohen Sold-Zahlen und aktiven GMV-Max-Sellern wählen; Ziel ist die Aufnahme des Creatives in Seller-Ads, nicht organische Viralität.
6. Für DE/EU: AI-Label setzen (TikTok/AI Act), Health-Claims-VO beachten – das US-Skript ist 1:1 nicht compliant.

## 10. Quellen (Zugriff 2026-09-24/25)

1. https://www.tiktok.com/@healthysmartdeals (Profil-SSR) und https://www.tiktok.com/embed/@healthysmartdeals (neueste 9 IDs).
2. 20 Video-Detailseiten (Tabelle oben), tt_video.sh; Downloads + ASR-WebVTT für 7630107962530336013, 7636932117317864718, 7635099527178882317, 7631176909543525645 (lokal: scratchpad/hsd/, Frames in hsd/fr_<id>/).
3. YouTube: Victor Decodes Ecom, "You've Been Lied To About Tiktok Shop AI UGC", 2026-05-04, 554 s, 192 Views, https://www.youtube.com/watch?v=NNIhmKGmpVY (Transkript research/yt_transcripts/NNIhmKGmpVY.txt; Beschreibung via NexLev youtube_video_details); Re-Upload HowEcomWorks https://www.youtube.com/watch?v=b7POUuz16xc (2026-07-26).
4. https://topluxnutrition.com/products/magnesium-complex (Preis $40 / Sale $29,97; 1.192 Reviews).
5. Vor-Dossier research/accounts/healthysmartdeals.md und research/sweep_product_side.md (Toplux-Brand-Account @topluxnutrition: 137.200 Follower, ttSeller true, Bio "Creator? Email us for collabs: Affiliate@topluxnutrition.com").
6. Nicht erreichbar: instagram.com/healthysmartdeals (429), youtube.com/@healthysmartdeals (404), TikTok-Shop-Suchseiten (kein SSR), goli.com-Produktseiten (404), amazon.com (503), topluxnutrition.com/pages/affiliate (404).
