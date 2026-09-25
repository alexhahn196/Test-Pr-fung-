# Reverse-Engineering: @megs.homefinds ("Megshomefinds🎀") — Modell B (realistische KI-Persona, Apparel, US)

Stand: 2026-09-25 (Datenabruf 2026-09-24/25). Quellen: TikTok-SSR-JSON (tt_profile.sh / tt_video.sh / Embed-Seite), heruntergeladene MP4s + Frame-Sheets (OpenCV), TikTok-Shop-Produktseite (shop.tiktok.com), TikTok-Kommentar-API, Jon Reiter (YouTube FtYeKKh0gqs, Transkript aus research/sweep_youtube.md).
Einschränkungen: NexLev-Watch-Tool 15/15 Tageslimit erschöpft -> visuelle Analyse über eigene Frame-Extraktion (8 Frames/Video, 4 Videos) statt Audio-/Video-KI. WebSearch nicht verfügbar. Nur die 10 neuesten Videos listbar (TikTok exponiert keine ältere Videoliste); 3 von 5 Produktseiten hinter "Security Check". Instagram 429, YouTube @megs.homefinds 404.

## 1. Profil (Verified, tt_profile.sh 2026-09-25)
| Feld | Wert |
|---|---|
| Handle / Name | @megs.homefinds / "Megshomefinds🎀" |
| Bio | "Cute fashion finds💗" (kein Link, kein Shop-Tab: ttSeller=false, commerceUser=false) |
| Follower / Likes / Videos | 33.700 / 731.100 / 272 (am 24.09.: 269 -> +3 in 1 Tag) |
| Account erstellt | 2026-02-14 (createTime 1771035586) -> 272 Videos in 223 Tagen = **1,2 Videos/Tag** (Lifetime), zuletzt **~4,3/Tag** (10 Videos zwischen 22.09. 19:22 UTC und 25.09. 03:13 UTC) |
| Sprache/Region | language=en, Embed-Seite region US |
| Following | 24 |

Interpretation: Kein Bio-Link, kein Shop-Tab, alle Videos mit Produktanker -> reines TikTok-Shop-Affiliate-Konto (Verkauf ausschließlich über die Produktkarte im Video).

## 2. Videoset (n = 10, alle Verified via tt_video.sh 2026-09-25, Views-Stand 25.09. ~11:00 UTC)

| # | Video-ID | Datum (UTC) | Dauer | Views | Likes | Komm. | Shares | Saves | Hook (On-Screen-Sticker ab 0,0 s, gesamte Laufzeit stehend) | Caption (Suchkeywords) | Produkt (Anker) | Musik | AI-Label |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7688442044301249823 | 22.09. 19:22 | 7 s | 1.389 | 14 | 0 | 1 | 7 | "soft girl moment 🤍" | "the back detail got me #whitedress #summerdress #romanticdress #datenightoutfit #floraldress" | Elegant Layered Long Dress (1732546023030231954) | "kiss me" | aigc 1 |
| 2 | 7688471569298967838 | 22.09. 21:16 | 6 s | 814 | 5 | 0 | 0 | 3 | "romantic girl era✨" | "the prettiest little dress 🤍 #floraldress #whitedress #romanticdress #datenightdress #summerdress" | dito | original sound | aigc 1 |
| 3 | 7688546502641257759 | 23.09. 02:07 | 9 s | 851 | 11 | 0 | 0 | 5 | "the perfect fall top🍂" | "this fit is everything 🤎 #datenightoutfit #wraptop #lacetop #browntop #falloutfitinspo" | Y2K Balletcore Wrap Crop Top (1732417152162173788) | "So Easy ROMANTIK. Remix" | aigc 2 |
| 4 | **7688758796826479902** | 23.09. 15:51 | 9 s | **37.800** | 501 | 0 | 15 | 181 | "the cutest brown top 🤎" | "#wraptop #datenightoutfit #lacetop #browntop #falloutfitinspo" (nur Hashtags) | dito | original sound | aigc 2 + moderationAigc 1 |
| 5 | 7688812608396234015 | 23.09. 19:20 | 7 s | 396 | 3 | 0 | 0 | 2 | "the prettiest holiday dress" | "the perfect velvet mini ✨ #holidaydress #christmasdress #velvetdress #minidress #classydress" | Cider Velvet Boat Neck Bowknot A-line Mini Dress (1732684744822788183) | original sound (ASR: "Have a holly, jolly Christmas / XOXO Gossip Girl" = Sound-Lyrics) | aigc 2 |
| 6 | 7688819236780772638 | 23.09. 19:45 | 5 s | 245 | 6 | 0 | 0 | 6 | "the cutest velvet mini✨" | "the perfect holiday dress 🤍 #velvetdress #minidress #holidaydress #christmasdress #reddress" | dito | "santa tell me" | aigc 2 |
| 7 | 7688903652689333535 | 24.09. 01:13 | 6 s | 1.471 | 16 | 0 | 1 | 8 | "this top is everything 🫶🏽" | "simple but sooo good 🖤 #blackcutouttop #datenightop #cutetops #falloutfitinspo #cutouttop" | Cider Cotton-blend Cut Out Metal Detail Long Sleeve Top (1732594016232771671) | original sound | aigc 2, **isAd=true** |
| 8 | 7689268518377852191 | 25.09. 00:49 | 8 s | 317 | 5 | 0 | 0 | 2 | "the color is everything 🥀" | "obsessed with this fit ❤️‍🔥 #burgandytop #wraptop #datenightoutfit #falloutfit #goingouttop" | Wrap Crop Top (dito #3/#4, Farbvariante burgundy) | original sound | aigc 2 |
| 9 | 7689298084915858719 | 25.09. 02:43 | 6 s | 47 | 3 | 0 | 0 | 1 | "this set is everything 🫶🏽" | "immediately one of my favorites #acta #actasweatshirt #matchingset #oversizedsweatshirt #casualoutfit" | Women's Cotton Pullover Sweatshirt – ACTA (1732577410274332893) | "som original - starn🧸" | aigc 2 |
| 10 | 7689305669601692958 | 25.09. 03:13 | 7 s | 30 | 2 | 0 | 0 | 2 | "so effortlessly cute 🖤" | "the easiest matching set to style #actasweatshirt #matchingset #acta #sweatsets #comfyoutfit" | dito | "it girl" (ASR: "People call you that phrase it girl…" = Lyrics) | aigc 2 |

Kennzahlen der Stichprobe (Verified/Estimated): Summe 43.258 Views; Top-Video = **87 %** aller Views; Median 605 Views; Ø ohne Top-Video 607. Like-Rate 1,31 % (Top-Video 1,33 %). Saves/Likes ≈ 0,36 (hohes Save-Verhältnis = "Outfit merken"-Verhalten). **Kommentare: 0 auf allen 10 Videos** (Kommentar-API liefert total=0, itemCommentStatus=0 = erlaubt) — bei 37.800 Views/501 Likes praktisch nur durch Kommentarfilter/-löschung erklärbar (Verified: Zustand; Estimated: Ursache). Alle Videos 5–9 s, Hochformat 720×1280, 30 fps, isECVideo=1, je genau 1 Produktanker (Typ 35 -> Shop-Produkt), Sticker-Typ 4 (Text-Sticker).

## 3. Sichtung (eigene Frame-Sheets, 8 Frames/Video; Bilder in research/reverse/_megs/sheet_*.jpg, faces.jpg, covers_grid.jpg)

**Format (identisch in allen 10 Covern + 4 gesichteten Videos):** Spiegel-Selfie einer jungen brünetten Frau (20–28, lange dunkle Haare, "Latina/Mediterranean-Look"), Handy vor dem Gesicht (mal schwarzes, mal weißes/goldenes iPhone), Ganzkörper -> leichter Zoom auf Oberkörper -> zurück; leichtes Posen (Hand an Hüfte, Haare hinters Ohr, Drehung). Kein Sprechen, keine Voiceover, nur Musik/Trend-Sound (Audio -18 bis -19 dB mean, durchgehend; ASR-Untertitel enthalten nur Song-Lyrics). Ein Sticker in Serifenschrift (Editorial-Look) mit Emoji, klein, mittig/rechts auf Brusthöhe, steht das ganze Video über — das ist der komplette "Hook". Kein gesprochener oder geschriebener CTA ("link", "cart", "shop") in keinem Video; der Kauf-Trigger ist ausschließlich die TikTok-Shop-Produktkarte (Anchor), die im Web-SSR als "Eligible for commission"-Disclosure (bc_disclosure_tag_ecommerce_us) hinterlegt ist.

| Video | Struktur mit Timestamps | Schnitte/Szenen | Setting | KI-Indizien |
|---|---|---|---|---|
| #4 Top (37,8k) | 0,0–3,9 s Ganzkörper im Spiegel (Schlafzimmer, Bett, Holzboden, Bilderrahmen), Hand an Hüfte, leichte Drehung; 3,9 s Zoom auf Halbtotale; 5,2–9,1 s Halbtotale, Posen/Kopfneigung, Ende ohne CTA | 1 durchgehende Aufnahme mit 1 digitalem Zoom (evtl. 2 Generierungen aneinander) | Schlafzimmer, Tageslicht | glatte, "schwebende" Bewegung, extrem gleichmäßiges Licht, Haare bewegen sich kaum, Phone-Haltung leicht wechselnd; Look = typisches Image-to-Video (Kling/Seedance/Veo) auf KI-Standbild |
| #10 Neuestes (30) | 0,0–7,5 s Ganzkörper im Flur (Treppe, Sideboard, Haustür), Gewichtsverlagerung, Lächeln, Blick ins Handy | 1 Clip, 0 Schnitte | Flur eines Einfamilienhauses | Outfit = 1:1 Produktfoto (ACTA-Set) mit anderem Model; Gesicht wirkt "geglättet", Hände/Phone teils unscharf |
| #5 Velvet (396) | 0,0–3,1 s Ganzkörper (goldener Spiegel, begehbarer Kleiderschrank, Kerzen), 4,1–6,2 s Halbtotale mit Lächeln, 7,3 s wieder Ganzkörper | 3 Segmente (2 Zooms) | Walk-in-Closet, warmes Abendlicht | Rock schwingt physikalisch unplausibel; Beine/Strumpfhose flackern; identische Pose wie Produktfoto-Stil |
| #7 Black Top (1,5k, isAd) | 0,0–2,6 s Ganzkörper (Wohnzimmer, TV, Couch), 3,5–6,1 s Halbtotale, Handtasche | 2 Segmente | Wohnzimmer | wie oben |

**Persona-Konsistenz:** "Gleicher Typ, nicht dieselbe Frau" — Gesichter in #4/#10/#5/#7 sind ähnlich (Haarfarbe, Alter, Hautton), aber Gesichtsform, Nase und Augenbrauen unterscheiden sich sichtbar (faces.jpg); jedes Video spielt in einem anderen Raum, mit anderem Handy. Das spricht für einen Prompt-/Referenzbild-Workflow ("brunette girl mirror selfie wearing [Produktbild]") statt für einen festen Charakter-LoRA. Produktbild-Abgleich (pcovers.jpg): Wrap-Top und ACTA-Set im Video entsprechen exakt den Shop-Produktfotos (Farbe, Schnitt, Spitzenkante, Streifen); beim "Elegant Layered Long Dress" zeigt die Shop-Seite ein schwarzes Kleid, das Video die weiße Variante -> Produkt wird per Bild-Referenz "angezogen" (Virtual-Try-on-artig).
**AI-Label:** Alle 10 Videos tragen ein Creator-seitiges KI-Label (aigcLabelType 1 bzw. 2; IsAigc=false, ShowAIGC=false), das Top-Video zusätzlich moderationAigcLabelType=1 (TikTok-seitig). Damit ist das Label in der App sichtbar ("Creator labeled as AI-generated") — das Konto verheimlicht KI nicht, verzichtet aber auf jeden weiteren Hinweis.
**UGC/Realclips/Stock:** 0 % — keine Realaufnahmen, keine Packaging-Shots, kein Before/After, kein Stock. Reine KI-Standbild->Video-Clips.
**Kommentar-Reaktion:** nicht bewertbar (0 Kommentare überall, siehe oben). Der fehlende Social Proof wird durch Kommentarunterdrückung offenbar bewusst in Kauf genommen ("this is AI"-Pushback wird so vermieden).

## 4. Angebot / Offer

| Produkt (Anker) | Preis | Shop | Sold / Rating | Tag |
|---|---|---|---|---|
| Y2K Balletcore Wrap Crop Top (Videos #3, #4, #8) | **$17.54–37.24** (SKU-Spanne; Größe S = $37.24), Free Shipping, 6–11 Tage Global Standard (= China-Direktversand) | "Chic And Simple" (Seller-ID 8647431132544144220; 781 Follower, **3.120 Affiliate-Videos**, 24,9k Items sold, 82 % positiv, Shop-Rating 4,4) | 834 sold; Produkt-Rating **3,6** (17 Reviews) | Verified (shop.tiktok.com 2026-09-25) |
| Cider Cotton-blend Cut Out Metal Detail Long Sleeve Top (#7, isAd=true) | **$45.49** | Cider (Official; 1,1 M Follower, 1,7 M sold, 82 % positiv, 98 % on-time) | 52 sold; 4,3 Sterne | Verified |
| Elegant Layered Long Dress (#1, #2) | n/a (Security Check) | n/a | n/a | Nicht öffentlich verifizierbar |
| Cider Velvet Boat Neck Bowknot A-line Mini Dress (#5, #6) | n/a (Security Check); Cider-Kleider liegen typisch $30–60 | Cider | n/a | Estimated |
| ACTA Cotton Pullover Sweatshirt/Set (#9, #10) | n/a (Security Check) | ACTA (Marke) | n/a | Nicht öffentlich verifizierbar |

- **Provision:** Nicht öffentlich verifizierbar (kein Kalodata/FastMoss-Zugang; FastMoss-URL 404). Apparel-Open-Plans auf TikTok Shop US liegen typisch bei 10–20 % (Estimated, aus Benchmarks-Recherche). Cider fährt häufig 10–15 %-Pläne; Kleinst-Seller wie "Chic And Simple" meist 15–20 % + Samples.
- **Rabatt/Coupon:** keine Streichpreise auf der Wrap-Top-Seite; nur "Log in to check your coupons". Keine Rabatt-Kommunikation im Video/Caption (Verified).
- **Impulskauf-Potenzial:** hoch: $17–45, Free Shipping, "Datenight/Holiday/Fall"-Anlässe, saisonale Vorlaufplanung (Christmas-Dress bereits am 23.09.; laut Reiter Anfang September Halloween-T-Shirt "Tis the Season"). Problem/Lösung existiert nicht — reine Aspiration ("so sieht das Outfit an einem hübschen Körper aus").
- **Zielgruppe:** Frauen 18–30 US, "clean girl / soft girl / it girl"-Ästhetik, Pinterest-Outfit-Inspo-Suchende. Hashtags zielen auf Outfit-Suchbegriffe (#datenightoutfit, #falloutfitinspo, #holidaydress, #whitedress), nicht auf Produkt-/Markennamen (Ausnahme #acta).
- **Warnsignale:** 3,6-Sterne-Produkt mit 6–11 Tagen Versand als Top-Seller-Anker; Video zeigt eine KI-idealisierte Passform, die das reale Produkt (17 Reviews, 3,6) nicht liefert -> Retourenrisiko bei Apparel ohnehin 15–30 % (Estimated).

## 5. Distribution

- **Organisch (FYP) dominiert:** 87 % der Stichproben-Views in einem Video; die übrigen 9 liegen bei 30–1.500 Views. Die Verteilung ist die klassische Lotterie: viele Varianten, ein Treffer. Top-Video hat Caption nur aus Hashtags -> kein Suchtext, trotzdem 37,8k -> FYP-getrieben.
- **Suche:** Captions und Hashtags sind konsequent als Outfit-Suchbegriffe formuliert (Kleidungsstück + Anlass + Saison). Gewichtung Estimated: 70–85 % FYP, 10–25 % Suche/Hashtag, <5 % Shop-Tab (kein Shop-Tab am Profil, isECVideo bringt aber Ausspielung in Shop-Feeds).
- **Volumen:** Lifetime 1,2/Tag, aktuell 4/Tag; Produkte werden in **Serien** gepostet: 5 Produkte in 10 Videos, je 2–3 Varianten pro Produkt mit anderem Sticker-Hook, anderer Caption, anderem Sound, anderem Raum, teils anderer Farbe (Wrap-Top braun/burgundy). Genau das "gleiches Produkt, verschiedene Hooks"-Muster (Verified in Stichprobe).
- **Views lifetime (Estimated):** 731.100 Likes ÷ 1,3 % Like-Rate ≈ **55 Mio. Views** seit Feb 2026 (Spanne 40–90 Mio. bei Like-Rate 0,8–1,8 %) ≈ 5–10 Mio. Views/Monat im Schnitt. Followerzahl (33,7k) ist relativ dazu winzig -> Views kommen aus FYP-Ausspielung, nicht aus Abonnenten; das Profil wird kaum besucht (kein Bio-Link nötig).
- **Sister-Accounts / Crossposting:** nicht nachweisbar. Bio/Captions nennen keine anderen Handles; Instagram 429 (nicht prüfbar), YouTube @megs.homefinds 404 (Verified). Das Format (Spiegel-Selfie-KI-Girl, 5–9 s, Serifen-Sticker) ist allerdings identisch mit dem von @realdavidmar beschriebenen "15 Accounts"-System (research/sweep_youtube.md) — ein Netzwerk ist wahrscheinlich, aber nicht belegt.
- **isAd=true bei #7 (Cider):** Paid-Partnership-Flag -> mindestens ein Video ist als bezahlte Kooperation/Spark-Ad-berechtigt markiert; Cider nutzt häufig GMV Max/Spark-Ads auf Affiliate-Videos (Estimated).

## 6. Fazit: Wo liegt der Wettbewerbsvorteil?

1. **Produktionskosten ≈ 0 und Testgeschwindigkeit (stärkster Faktor, Verified):** 5–9 s, ein KI-Clip, ein Sticker, ein Trend-Sound. Kein Skript, keine Stimme, kein Schnitt. Damit 4 Videos/Tag und 2–3 Hook-Varianten pro Produkt möglich; ein Treffer (37,8k) finanziert 9 Nieten.
2. **Perfekte "Passform-Illusion" durch KI (Verified visuell):** Das Produktfoto wird auf eine attraktive, glaubwürdige Spiegel-Selfie-Persona übertragen, in einem aspirativen Zuhause. Für Apparel ist genau das der Kaufauslöser ("wie sieht es an mir aus"), und Taro/Reiter-Erkenntnis aus der Benchmark-Recherche bestätigt: Kleidung/Fit konvertiert auch als offen gelabeltes KI-Video, Supplements nicht.
3. **Produktwahl (Verified/Estimated):** Trend-/Saison-Apparel $17–45, hohe Anker-Provision (15–20 % bei Kleinst-Sellern), Free Shipping, frühe Saisonbesetzung (Halloween Anfang Sept., Christmas-Dress Ende Sept.). Mischung aus Marken-Shops (Cider, ACTA — Vertrauen, Volumen) und No-Name-Dropshippern (höhere Provision).
4. **Suchoptimierte Captions (Verified):** Outfit-Keywords statt Produktnamen -> Long-Tail-Traffic zusätzlich zum FYP.
5. **Kommentarkontrolle (Verified Zustand):** 0 Kommentare überall -> "this is AI"-Pushback wird unsichtbar gehalten; Preis: kein Social Proof.
6. **Nicht** der Vorteil: kein besonderer Hook (Sticker-Text ist generisch), keine Persona-Konsistenz (Gesicht variiert), kein Voiceover, keine Story, keine Marke, kein Sister-Netzwerk nachweisbar.

**Bewertung der Evidenz:** Format, Volumen, Produkte, Preise, AI-Label, Views-Verteilung, Kommentarlage = Verified (eigene TikTok-Daten und Frames). KI-Generierung = Verified über TikTok-Label + visuelle Indizien (kein Watch-Tool verfügbar, daher keine Bewegungsanalyse). Umsatz = nur Claimed (Reiter, verkauft Mentorship). Provision/Traffic-Split = Estimated.

## 7. Einkommensschätzung (Estimated; Formel: Views × Produkt-CTR × CVR × AOV × Provision − Retouren)

Inputs: Views/Monat 4–8 Mio. (Estimated aus Like-Rate, s. o.); Produkt-CTR 1–2 % (nur Produktkarte, kein CTA); CVR 2–4 % (Apparel, Impulse, aber 3,6-Sterne-Produkt); AOV $22–35; Provision 12–18 %; Retouren/Storno 10–20 %.

| Szenario | Rechnung | GMV/Monat | Netto-Provision/Monat |
|---|---|---|---|
| Low | 4 Mio × 1,0 % × 2,0 % × $22 = $17.600 GMV × 12 % × 0,85 | ~$18k | **~$1.800** |
| Mid | 6 Mio × 1,3 % × 2,5 % × $28 = $54.600 GMV × 15 % × 0,85 | ~$55k | **~$7.000** |
| High | 8 Mio × 1,5 % × 3,0 % × $30 = $108.000 GMV × 18 % × 0,85 | ~$108k | **~$16.500** |

Abgleich mit Reiters "a little over $22,000 in the past month" (Claimed, Metrik unklar, Screenshot-Tool nicht genannt): Als **GMV** passt es in den Low-/Mid-Korridor und impliziert ~**$2.300–3.500 Netto-Provision** bei 12–18 %. Als Provision wäre GMV ~$150k nötig — bei 33,7k Followern und 37,8k Views für das beste Video der Woche unwahrscheinlich. **Band: $2.000–6.000 Netto-Provision/Monat (Estimated), Mittelwert ~$3.000**, mit hoher Monatsvolatilität (Lotterieverteilung, Saisonprodukte). Nicht enthalten: mögliche Spark-Ad-/Paid-Partnership-Pauschalen (isAd=true bei Cider, Höhe nicht öffentlich).

## 8. Übertragbare Playbook-Elemente
- 5–9 s Spiegel-Selfie-KI-Clip aus Produktfoto (Referenzbild) + Serifen-Sticker (3–5 Wörter, Emoji) + Trend-Sound, kein Sprechen, kein CTA — Produktkarte macht die Arbeit.
- Pro Produkt 2–3 Varianten (Sticker/Caption/Sound/Raum/Farbe) innerhalb von 24 h; 3–5 Produkte parallel; Saison 6–10 Wochen voraus.
- Captions = Kleidungsstück + Anlass + Saison als Hashtags (Suchtraffic), kein Markenname außer bei bekannten Marken.
- KI-Label setzen (alle Videos gelabelt; kein Reichweitenkiller bei Apparel), Kommentare filtern.
- Risiko: Passform-Illusion vs. 3,6-Sterne-Realität -> Retouren, Trust; keine Persona-Konsistenz -> kein Community-Aufbau (33,7k Follower bei ~55 Mio. Views = 0,06 % Follow-Rate, Estimated).

## Quellen
- https://www.tiktok.com/@megs.homefinds (SSR, 2026-09-24/25); Embed https://www.tiktok.com/embed/@megs.homefinds (2026-09-25)
- Video-URLs: https://www.tiktok.com/@megs.homefinds/video/<ID> für alle IDs in Tabelle 2 (tt_video.sh 2026-09-25); MP4/Frames: research/reverse/_megs/
- https://shop.tiktok.com/view/product/1732417152162173788 und /1732594016232771671 (2026-09-25); 1732546023030231954, 1732684744822788183, 1732577410274332893 -> "Security Check"
- Kommentar-API https://www.tiktok.com/api/comment/list/?aweme_id=7688758796826479902 (2026-09-25): total 0
- Jon Reiter, "exactly how I make $100k/month with Ai Tiktok Shop", https://www.youtube.com/watch?v=FtYeKKh0gqs (~2026-09-22), Transkript [4:31]/[4:52] via research/sweep_youtube.md; YouTube-Seite per WebFetch heute nicht lesbar
- https://www.instagram.com/megs.homefinds/ (429), https://www.youtube.com/@megs.homefinds (404), https://www.fastmoss.com/en/tiktok-shop/creator-detail/megs.homefinds (404) — alle 2026-09-25
