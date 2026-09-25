# Reverse-Engineering: @liverboosthub11 („Health u1s1", USA)

Stand: 2026-09-25. Datenquellen: TikTok-Public-Data (tt_profile.sh / tt_recent.sh / tt_video.sh, **Verified**), TikTok-ASR-Untertiteldatei (eng-US) des Top-Videos (**Verified**), die drei wichtigsten Videos als MP4 heruntergeladen und per ffmpeg in 5-Sekunden-Frame-Raster + Szenenschnitt-Zählung ausgewertet (**Verified, Sichtprüfung der Frames**), Cover-Bilder aller 10 Videos (**Verified**), 404 Media 2026-07-30 (**Claimed**, lokale Kopie research/404media.html). Rohdaten: research/accounts/liverboosthub11_raw_20260925.jsonl, Frames/Covers/MP4 in research/reverse/_lbh/.

**Einschränkungen:** WebSearch war nicht verfügbar (Budget 200/200). Das NexLev-Watch-Tool (`watch_tiktok_video_and_ask`) war beim Start bereits 15/15 erschöpft – **keine Tonspur-Auswertung möglich**. Ersatz: ASR-Transkript (nur beim englischen Top-Video vorhanden), Frame-Raster mit eingebrannten Wort-Captions (alle drei Videos), Cover-Bilder. Ob die Stimme TTS ist, konnte daher **nicht gehört** werden (Tag: wahrscheinlich, s. u.). Kommentarsektion: 0 Kommentare in allen 10 Videos (Verified) – keine Reaktionen auswertbar. Kalodata/FastMoss: 403/Login – nicht öffentlich verifizierbar.

---

## 0. Kernbefund in fünf Sätzen

1. @liverboosthub11 ist ein **vollständig KI-produzierter Supplement-Affiliate-Account** (Modell C: AI-„Arzt"/Sprecher + KI-Bild-Slideshow + TTS), der im Sample ein einziges Produkt bewirbt: **„Harvard Apparatus Regenerative Technology – Healthregen LIVER GUARD"** (Milk-Thistle-Kapseln, 60 Stk.), TikTok-Shop-Karte im Video: **„-60 % $19.99 (statt $49.99), Single Bottle Starter Pack"** (Verified, im Frame gelesen). Das ist **nicht** Rosabella – 404 Media nennt den Account nur als *Skript-Spender* für Harry Changs Rosabella-Video.
2. Das Skript ist eine Angst-→-Autorität-→-Heilversprechen-→-Verknappungs-Kette („I'm a liver specialist with over 40 years of experience … 100 percent cure … Tap the link in the bottom left corner for a 50 % discount. Final 30 minutes."), die gut genug war, dass ein anderer Affiliate sie kopierte und damit 1,3 Mio. Views erzielte (Claimed, 404 Media).
3. Der Account fährt **vier visuelle Template-Familien** für dasselbe Produkt (englischer KI-Arzt im weißen Kittel; spanischer KI-Dozent am Rednerpult; spanische KI-Bild-Slideshow „Mann in der Bierflasche"; spanische Fake-Nachrichtensendung „NNIT NEWSA" mit „verhaftetem Boston-Hepatologen") – klassisches Hook-/Format-Multivariantentesting bei identischem Endscreen (Produktkarte).
4. Ökonomisch ist der Account **tot**: die 10 jüngsten Videos (24.11.–07.12.2025) haben Median 197 Views, 6 Likes gesamt, 0 Kommentare, **keinen Produkt-Anchor** mehr; seit 07.12.2025 kein Upload. Die 60.200 Lebenszeit-Likes stammen aus früheren Videos (Jun–Nov 2025), die headless nicht auflistbar sind.
5. Der reale Wettbewerbsvorteil war **nicht** KI per se, sondern: **Skript-Formel + tägliche Massenproduktion (≈ 23 Videos/Monat) + Impulspreis $19.99 mit „-60 %" + Zielgruppe „heavy drinker / hombres" + Sprachvarianten (EN/ES)**. Der Nachteil: Heilversprechen + Fake-Autoritäten → Produktkarte weg, Reichweite weg. Einkommen heute ≈ 0 USD/Monat; historische Hochphase **500–5.000 USD/Monat** (Estimated, LOW).

---

## 1. Profil (Verified, tt_profile.sh 2026-09-24/25)

| Feld | Wert |
|---|---|
| Handle / Nickname | @liverboosthub11 / „Health u1s1" (u1s1 = chin. Netzslang 有一说一 „ehrlich gesagt") |
| Follower / Likes / Videos | 2.668–2.669 / 60.200 / 137 |
| Following | 9 |
| Erstellt | 2025-06-04 |
| Bio / Bio-Link | leer / keiner |
| ttSeller / commerceUser | false / false |
| Sprache im Profilobjekt | „zh"; Musikfeld aller Videos „原聲" (= „Originalton", chinesische App-Sprache) |
| locationCreated (Videos) | US |
| Letzter Upload (Embed-Liste) | 2025-12-07 → seit ~9,5 Monaten inaktiv |
| Schwester-Handles geprüft | liverboosthub, liverboosthub1/2/10/12, healthregenw, healthu1s1, health.u1s1 → 10221 (nicht vorhanden); healthregen → 10222 (privat, Nickname „health", erstellt 2022) – kein Beleg für Zugehörigkeit |
| Crossposting | youtube.com/@liverboosthub11 → 404; instagram.com/liverboosthub11 → 429 (nicht prüfbar) |

Interpretation: chinesischsprachiger Betreiber (App-Sprache, Reviews-Screenshot mit chinesischer Shop-Oberfläche „美国 / 已确认购买", s. § 3), der einen US-Shop-Artikel eines vermutlich chinesischen White-Label-Sellers bewirbt. Das Handle-Suffix „11" deutet auf eine Handle-Serie hin; Geschwister-Handles sind aber nicht (mehr) auffindbar.

---

## 2. Video-Set (n = 10, Verified per tt_video.sh 2026-09-25; alle Videos noch abrufbar)

Alle 10 URLs stammen aus der Embed-Seite (die 10 jüngsten). Ältere Videos sind headless nicht auflistbar. Hook-Zeitstempel: bei Video 1 aus den ASR-Cues (Verified), bei den anderen aus dem 5-s-Frame-Raster bzw. Cover (erstes eingebranntes Caption-Wort = 0–5 s, Estimated).

| # | Video-ID | Datum | Länge | Views | Likes | Komm. | Shares | Saves | isAd | AI-Label | Anchor | Sprache / Template | Hook (0–3 s) | Hashtags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7579984784156364045 | 2025-12-04 | 60 s | **534** | 1 | 0 | 0 | 1 | ja | null (im Bild aber „AI-generated content") | nur CapCut (Typ 54) | EN / KI-Arzt weißer Kittel | 0:00,18–0:01,78 „Want to know if your liver is healthy?" · 0:01,78–0:03,68 „Just take a look at your fingernails." On-Screen: „Evory Heavy Drinker Should Pay Attention to Their Liver Health" (sic) | liverhealth, tiktokshop, supplements, healthregen, harvardapparatus |
| 2 | 7578930630654741791 | 2025-12-01 | 86 s | **530** | 1 | 0 | 6 | 0 | ja | 1 | – | ES / KI-Bild-Slideshow „Mann in Bierflasche" | 0:00–0:05 Caption „DE LOS ALCOHÓLICOS" (Bild: Comic-Mann in Bierflasche); 0:05 „SEÑAL LOS SÍNTOMAS" (Beerdigungsszene) | man, liver, tiktokblackfriday, harvardapparatus, fvp |
| 3 | 7577080682405465374 | 2025-11-26 | 88 s | 230 | 0 | 0 | 1 | 0 | ja | 1 | – | ES / Fake-News „NNIT NEWSA" | 0:00–0:05 Caption „ES UN EMPLEADO"; Bauchbinde „Un empleado federal de 33 años fue arrestado por compartir un suplemento" + Häftlingsbild | liverhealth, tiktokshopblackfriday, supplements, healthregenw, man |
| 4 | 7577081504858148127 | 2025-11-26 | 88 s | 195 | 1 | 0 | 0 | 0 | ja | 1 | – | ES / Fake-News – **identisches Cover (Byte-gleich) wie #3** → Duplikat-Upload mit anderen Hashtags | wie #3 | liver, tiktokshopblackfriday, supplements, man, harvardapparatus |
| 5 | 7576330955179232525 | 2025-11-24 | 101 s | 217 | 0 | 0 | 0 | 0 | ja | 1 | – | ES / Fake-News „NNIT NEWS" (Arzt-Insert am Mikro) | Cover: Nachrichtensprecherin + „Dr." im Kittel; Caption nicht im Cover | liverhealth, tiktokshopblackfriday, supplements, healthregen, harvardapparatus |
| 6 | 7581131007449992479 | 2025-12-07 (neuestes) | 90 s | 199 | 0 | 0 | 0 | 0 | ja | 1 | – | ES / KI-Dozent am Rednerpult | 0:00–0:05 Caption „SI EL HÍGADO" / „COMIENZA POR REVISAR" über Anatomie-Skelett „Músculo trapecio" (Hook: Schulterschmerz = Leberzeichen) | liverhealth, tiktokshopsoringglowup (sic), supplements, healthregen, harvardapparatus |
| 7 | 7577799725806587167 | 2025-11-28 | 101 s | 127 | 2 | 0 | 0 | 0 | ja | 1 | – | ES / Fake-News „NNIT NEWSA – Salud del hombre" | Cover: Sprecherin + Arzt-Insert, Ticker „Salud del hombre" | man, liver, tiktokshopblackfriday, harvardapparatus, fvp |
| 8 | 7579325180682538271 | 2025-12-02 | 91 s | 117 | 1 | 0 | 5 | 0 | nein | 1 | – | ES / KI-Bild-Slideshow (Leber mit Skalpell) | 0:00–0:05 Caption „HÍGADO DESPUÉS DE" | liver, harvardapparatus, fvp, tiktokshopblackfriday, health |
| 9 | 7576726068787170590 | 2025-11-25 | 101 s | 165 | 0 | 0 | 0 | 0 | ja | 1 | – | ES / Fake-News „¿Fue arrestado por esto? Dr. Samuel Reyes, hepatólogo de Boston, detenido en Harvard" | Cover-Sticker „HOMBRES veanlo si les preocupa su matrimonio ⚠" · Caption „HEPATÓLOGO DE BOSTON" | liverhealth, tiktokshopblackfriday, supplements, harvardapparatus |
| 10 | 7579713166825884958 | 2025-12-03 | 70 s | 61 | 0 | 0 | 0 | 0 | nein | null | – | ES/EN / KI-Bild-Slideshow (Mann trinkt Bier im Bett, Hologramm-Leber) | 0:00–0:05 Caption „SENDS OUT IN" (englisches Caption-Fragment in spanischem Set → Pipeline-Fehler) | man, liver, harvardapparatus, tiktokblackfriday, fvp |

**Aggregat (Verified-Basis, Rechnung Estimated):** Summe 2.375 Views; Ø 237,5; Median 197; Top-Video-Anteil 22,5 % (534/2.375), Top-2-Anteil 44,8 %; Likes gesamt 6 → Like-Rate 0,25 %; Shares 12 (0,5 %); Kommentare 0; Saves 1. Ø Länge 87,6 s (60–101 s). isAd = true in 8/10 (TikTok kennzeichnet als Werbung/Promotion), isECVideo = null in 10/10, **Produkt-Anchor 0/10** (nur CapCut-Anchor in #1 → Schnitt in CapCut).
Beschreibungen: 6/10 mit identischem Satz „Take care of your liver!Nutritional detoxification and liver", 4/10 nur Hashtags. Kein Video-Titel im Produktsuche-Stil, keine Produktnamen in der Caption → **keine Search-Optimierung**; die Suchbegriffe „liver", „supplements", „tiktokshop" laufen nur über Hashtags.

---

## 3. Sichtungen (Frame-Raster 5 s, ffmpeg; Szenenschnitte per Scene-Detection)

### 3.1 Video #1 – 7579984784156364045 (EN, 60 s, 534 Views, Top-Video)

**Volltranskript (Verified, TikTok-ASR eng-US):**
> „Want to know if your liver is healthy? Just take a look at your fingernails. If you drink regularly and have vertical ridges on your nails, that's a clear sign your liver is overworked with toxins. The most obvious signs of liver toxin build up include vertical ridges on your nails, foamy, foul smelling urine, a growing belly, frequent gas, disquiet on the right side of your abdomen. I'm a liver specialist with over 40 years of experience. If you don't want to die of liver disease before 100, here's a natural solution I strongly recommend. It has already saved the livers of over 1 million heavy drinkers. Taken once a day can quickly flush out liver toxins. Your hearing becomes clearer, swelling goes down and your energy skyrockets. You'll sleep like a baby again. [100] percent cure, no additives, all natural. A 30 day money back guarantee if it doesn't work. Over 5 million Americans have left positive reviews. Tap the link in the bottom left corner for a 50% discount. Final 30 minutes. Miss it and you'll have to wait another year."

**Struktur mit Zeitstempeln (0–3 s Verified aus ASR-Cues, Rest Estimated aus 5-s-Raster):**

| Zeit | Inhalt | Bild |
|---|---|---|
| 0:00–0:04 | Hook: „Want to know if your liver is healthy? Just take a look at your fingernails." | KI-Arzt (weißer Kittel, Brille, Bart, Bücherwand) → Makro Fingernagel mit Längsrillen |
| 0:04–0:25 | Symptomliste (Nagelrillen, schaumiger Urin, Bauch, Blähungen, Schmerz rechts) | gesunde vs. verfettete Leber (KI-Render), Mann vor Toilette, Mann hält sich Bauch im Bett |
| 0:25–0:30 | Fake-Autorität: „I'm a liver specialist with over 40 years of experience" | Arzt-Avatar spricht |
| 0:30–0:35 | Angst: „If you don't want to die of liver disease before 100" | dicker Patient im Krankenbett, zwei Ärzte |
| 0:35–0:45 | Lösung + Produkt-Reveal: „natural solution … saved the livers of over 1 million heavy drinkers … once a day" | **zweiter KI-Mann (grau, jung) hält Flasche „LIVER GUARD" in die Kamera** – Talking-Head-Stil |
| 0:45–0:50 | Benefits: Energie, Schlaf | Mann beim Kreuzheben (KI/Stock-Look) |
| 0:50–0:53 | „all natural", Siegel | **Hands-on-Close-up der Flasche „HARVARD APPARATUS – Regenerative Technology – LIVER GUARD – Dietary Supplement 60"**, eingeblendete FDA- und GMP-Badges |
| 0:53–0:57 | Social Proof: „Over 5 million Americans have left positive reviews" | Screenshot von TikTok-Shop-Reviews (5 Sterne; Reviewer-Namen „Home Decor Customization", „Moon Customization Collection", „CC Custom Photo Frame", „Vigorous Bear Trendy Toys" – Shop-Konten, keine Privatpersonen; Oberfläche mit chinesischen Labels „美国", „已确认购买") |
| 0:57–1:00 | CTA + Verknappung: „Tap the link in the bottom left corner for a 50 % discount. Final 30 minutes." | Screenshot der **Produktkarte „SINGLE BOTTLE STARTER PACK … -60 % $19.99 (durchgestrichen $49.99)"** mit rotem Pfeil nach unten links, Caption „FINAL 30 MINUTES" |

- Szenenschnitte: 16 (Schwelle 0,3) / 9 harte Schnitte (0,5) auf 60 s → ≈ 1 Schnitt alle 4–7 s; überwiegend **statische KI-Bilder mit leichtem Zoom (Slideshow)**, Arzt-Avatar als wiederkehrender Anker (≈ 50 % der Frames).
- Captions: eingebrannte 2–3-Wort-Karaoke-Captions, weiße Versalien mit gelbem Keyword („LOOK **AT** YOUR", „TOXIN BUILD UP", „FINAL 30 MINUTES"), dazu gelber Titelbalken „Evory Heavy Drinker …" durchgehend.
- Dauerhafte Overlays: oben Disclaimer „This is not medical advice or a claim, this is based on mypersonal Oxocricnce, evervone's rosults mav varv, alwavs do vour own rosearch" (OCR-Fehler → automatisch aus Bild kopiert), unten links „AI-generated content", unten rechts „Focuses on healthy and positive content".
- Voiceover: ASR-Text ist fehlerfrei-glatt, Werbesprech, kein Versprecher → **wahrscheinlich TTS** (nicht gehört; nicht verifiziert). Männlich vermutet (Arzt-Avatar). Musik: keine erkennbare; Musikfeld „原聲 – Health u1s1" (Originalton).
- AI-Avatar: KI-Arzt (Kittel, Brille, Bart) – **derselbe Charakter wie das Cover**, aber **nicht** in den spanischen Videos (dort anderer KI-Dozent) → kein konsistenter Charakter über den Account.
- Reale Produkt-Clips: ja – die Hands-on-Flaschenaufnahme (Flasche vor anatomischem Torso-Modell) ist ein **echter Clip**, der in allen drei gesichteten Videos identisch wiederverwendet wird (mutmaßlich Seller-Materialkit).
- Sichtbare Shop-Karte / Commission-Badge: **nicht** als Live-Element (kein Anchor), nur als eingebrannter Screenshot. UGC: keins. Stock: Gym-/Krankenhaus-Bilder im Stock-Look, vermutlich ebenfalls KI.

### 3.2 Video #6 – 7581131007449992479 (ES, 90 s, 199 Views, neuestes Video)

Kein Untertitel vorhanden; Auswertung aus 18 Frames (5-s-Raster) mit eingebrannten Wort-Captions.

| Zeit | Caption (eingebrannt) | Bild |
|---|---|---|
| 0:00–0:05 | „COMIENZA POR REVISAR" / Cover „SI EL HÍGADO" | anatomisches Skelett/Muskelmodell „Músculo trapecio" → Hook: Schulter-/Trapezschmerz als Leberzeichen |
| 0:05–0:15 | „ACUMULACIÓN DE TOXINAS", „CUANDO LAS TOXINAS" | **KI-Dozent** (braunes Sakko, Brille, Rednerpult, blaue Leber-Hologramm-Wand) fasst sich an die Schulter |
| 0:15–0:25 | „DOLOR DE HOMBRO", „ORINA DE COLOR" | Muskelanatomie; Dozent mit Insets (Bauch, Toilette, Mann erbricht) |
| 0:25–0:45 | „EN TU CUERPO", „PENETRAR LOS HEPATOCITOS", „DOS CÁPSULAS AL" | Dozent; transparenter Körper mit Organen; **Dosierung „2 Kapseln"** |
| 0:45–0:60 | „LOS DESECHOS", „LA FUNCIÓN HEPÁTICA", „TOMANDO 30 CÁPSULAS" | Cartoon-Darm voller Junkfood; lachender Mann; **Vorher/Nachher: Mann mit zu weiter Hose** (Gewichtsverlust-Claim) |
| 0:60–0:70 | „POR COMPLETO", „CERTIFICADO POR SGS" | Leber-Render; **NSF-„Certificate of Conformity" + FDA-Dokument** (Aussteller lt. Frame „Gemini Pharmaceuticals, Inc.") |
| 0:70–0:75 | „HA VUELTO VIRAL" | TikTok-Shop-Review-Screenshot (identisch zu #1: „CC Custom Photo Frame", „Home Decor Customization", „ONEQUE Trendy Creation Factory", „user8263697280717") |
| 0:75–0:85 | „VER EL CARRITO", roter Pfeil ↓ | **Hands-on-Flasche, Kapseln in der Hand** (echter Clip, identisch zu #1/#2) |
| 0:85–0:90 | „REMEMBER" (englisch!) | Produktkarte „-60 % $19.99 $49.99" |

- 14 Schnitte (0,3) / 11 (0,5) auf 90 s → ≈ 1 Schnitt alle 6–8 s; Mischung aus KI-Video-Avatar (Dozent mit Handbewegung → Image-to-Video) und KI-Standbildern.
- Disclaimer unten (spanisch): „Esto no es consejo médico ni una garantía de pérdida de peso. Algunas imÃgenes son generadas por IA o mejoradas digitalmente solo con fines ilustrativos. Esto se basa en mi experiencia personal. Siempre investiga por tu cuenta y consulta a tu medico." – Mojibake „imÃgenes" = fehlerhafte Encoding-Pipeline. Kein „AI-generated content"-Overlay im Bild, aber TikTok-Label aigcLabelType = 1 gesetzt.
- CTA: „Ver el carrito" (= Shop-Warenkorb-Symbol unten links) + Pfeil; Endscreen englisch „REMEMBER" → Skript maschinell aus dem englischen Master übersetzt.

### 3.3 Video #2 – 7578930630654741791 (ES, 86 s, 530 Views, zweithöchstes)

| Zeit | Caption | Bild |
|---|---|---|
| 0:00–0:05 | „DE LOS ALCOHÓLICOS" | Comic-Mann in Bierflasche gefangen (KI-Illustration) |
| 0:05–0:25 | „SEÑAL LOS SÍNTOMAS", „FRECUENTE FATIGA Y", „HÍGADO ESTÁ GRAVEMENTE", „POR CIENTO EN" | Beerdigung (Angst), gähnender Mann, Bier fließt in eine Leber, Mann trinkt am Fenster |
| 0:25–0:45 | „PATICO CAUSADO POR" (Tippfehler für „hepático"), „SIN NECESIDAD DE", „EL HÍGADO DE", „ELIMINARÁN A TRAVÉS", „LA ROPA SE" | Mariendistel auf Leber, Mann trinkt Saft, **Hands-on-Flasche mit Kapseln**, Ausscheidungs-Metapher, Mann zeigt schrumpfenden Bauch |
| 0:45–0:70 | „HÍGADO RECUPERARÁ SU", „EN DOS CÁPSULAS", „EL PRODUCTO CUENTA", „ESTADOUNIDENSE Y SGS", „SI EL PRODUCTO" | leuchtende Leber, Cartoon-Labor, NSF/FDA-Zertifikate mit Kräutern, Review-Screenshot, Flasche |
| 0:70–0:86 | „EL ENLACE DE", „ESTA OFERTA SOLO", Pfeil ↓ | Kapseln in der Hand, Produktkarte „-60 % $19.99 $49.99" |

- 18 Schnitte (0,3) / 6 (0,5) → viele weiche Übergänge, reine **KI-Bild-Slideshow ohne Avatar**; Overlays wie #1 (englischer Disclaimer, „AI-generated content", „Focuses on healthy and positive content") obwohl Ton/Captions spanisch → Overlay-Vorlage wird ungeachtet der Sprache drübergelegt.

### 3.4 Fake-News-Familie (#3, #4, #5, #7, #9; nur Cover gesichtet)

Nachrichtenstudio-Look („NNIT NEWS(A)", Ticker „ÚLTIMA HORA", „NOTICIAS DE ÚLTIMA HORA", „SALUD DEL HOMBRE"), KI-Sprecherin, Inserts: Arzt mit Mikrofon im Kittel bzw. Häftling in orangefarbener Kleidung. Schlagzeilen: „¿Fue arrestado por esto? Dr. Samuel Reyes, hepatólogo de Boston, detenido en Harvard" · „Un empleado federal de 33 años fue arrestado por compartir un suplemento" · Sticker „HOMBRES veanlo si les preocupa su matrimonio ⚠". Der Ticker-Text ist teils unlesbarer Pseudo-Text (KI-generierte Buchstaben) → gesamte Kulisse KI-Bild/Video. Hashtag #harvardapparatus ist gleichzeitig Marke *und* Anknüpfung an die „detenido en Harvard"-Story. Diese „verhafteter Arzt enthüllt …"-Erzählung ist eine bekannte Scam-Ad-Vorlage (Conspiracy-Hook); hier in spanischer Sprache für US-Latino-Männer.

---

## 4. Offer

| Feld | Befund | Tag |
|---|---|---|
| Produkt | „Harvard Apparatus – Regenerative Technology – Healthregen LIVER GUARD", Dietary Supplement, 60 Kapseln, Milk-Thistle-(Mariendistel-)Extrakt lt. Etikett („Premium Blend of Natural Extracts … Milk Thistle Seed Extract … Supports Healthy Liver Function") | Verified (Etikett im Frame) |
| Markenname | „Harvard Apparatus" ist der Name eines realen Laborgeräte-Herstellers (Harvard Bioscience); hier offenkundig Namens-Trittbrett für Autorität („Harvard"). Kein Zusammenhang belegbar. | Estimated/Kontext |
| Preis | Produktkarte im Video: **$19.99, „-60 %", durchgestrichen $49.99**, „Single Bottle Starter Pack"; Bundles (2–3 Flaschen) im Screenshot sichtbar | Verified (im Frame), Produktseite selbst nicht abrufbar (kein Anchor mehr) |
| Rabatt/Coupon | Skript: „50 % discount, final 30 minutes" (fiktive Verknappung); Karte: -60 % Dauerrabatt. Kein Code. | Verified (ASR/Frame) |
| Provision | Nicht öffentlich verifizierbar (Kalodata 403, keine Anchor-ID). Typische Spanne für White-Label-Supplements chinesischer Seller im US-Shop: 15–30 %. | Estimated |
| Impulskauf-Potenzial | hoch: $19.99, „-60 %", Geld-zurück-Garantie, Countdown, One-Click-Karte unten links | Estimated |
| Problem/Lösung | „Heavy drinker → vergiftete Leber (Nagelrillen, Urin, Bauch, Schulterschmerz) → 1–2 Kapseln/Tag entgiften, Energie, Schlaf, Bauch weg, ‚100 % cure'" | Verified (Skript) |
| Zielgruppe | Männer 35+, regelmäßiger Alkoholkonsum; ab Nov 2025 gezielt **spanischsprachige US-Männer** („hombres", „matrimonio", #man) | Verified (Captions/Hashtags) |
| Regel-Risiko | Heilversprechen („100 percent cure", „saved 1 million livers"), Fake-Arzt („liver specialist, 40 years"), fingierte Zertifikate/FDA-Badge, gefälschte Reviews-Anzahl („5 million Americans") → verstößt gegen TikTok-Shop-Regeln für Nahrungsergänzung und US-Werberecht | Verified (Inhalt) / Bewertung |

Verbindung zu Rosabella: 404 Media (2026-07-30): Harry Chang „copy-pasted the script from a video posted by an account called ‚liverboosthub11' and tweaked it" – für ein **Rosabella**-Video („Nigerian SECRET to CLEAN LIVER!!", Veo 3 + HeyGen + ElevenLabs „Latisha 1" + CapCut, 1,3 Mio. Views, „tens of thousands of dollars"; alle Zahlen Claimed). Im verifizierten Sample bewirbt liverboosthub11 **kein Rosabella-Produkt**. Das im Skript beschriebene Angebot (Leber-Detox für Trinker, „50 % Rabatt, letzte 30 Minuten") ist eine **produktunabhängige Skriptvorlage**, die auf jedes Leber-Supplement gelegt werden kann – genau das hat Chang gemacht.

---

## 5. Distribution

| Frage | Befund | Tag |
|---|---|---|
| Organisch vs. Search vs. Shop-Tab | Keine Produktnamen/Suchbegriffe in Captions, keine Titel im Suchstil → Search-Anteil vernachlässigbar. Kein Anchor → kein Shop-Tab-Traffic („Shop-Empfehlungen" entfallen). Views = For-You-Ausspielung (#fvp) + evtl. Spark-Ads-Flag (isAd true in 8/10, aber Views-Niveau 61–534 spricht gegen bezahlte Reichweite) | Estimated |
| Views-Konzentration | Top-Video 22,5 % des Sample-Volumens, Top-2 44,8 %; Verteilung flach-niedrig (61–534) → kein Viral-Hit im Dezember-Set | Verified |
| Posting-Volumen | Sample: 10 Videos/14 Tage ≈ 5/Woche; Lebenszeit 137 Videos/≈ 6 Monate ≈ 22–23/Monat; 2 Uploads am 26.11. (Duplikat) | Verified/Estimated |
| Varianten desselben Videos | ja: 4 Template-Familien (EN-Arzt, ES-Dozent, ES-Slideshow, ES-Fake-News) + Byte-gleiches Duplikat (#3/#4) + Hashtag-Rotation (#tiktokshopblackfriday / #tiktokblackfriday / #tiktokshopsoringglowup) → **Multivariantentest: gleiches Produkt, gleicher Endscreen, andere Hooks/Sprachen** | Verified |
| Mehrere Accounts | Handle-Suffix „11" und Fließband-Produktion sprechen für ein Account-Netz; Geschwister nicht auffindbar (§ 1). 404 Media beschreibt für das Rosabella-Umfeld Discord-Coaching + Job-Anzeige „10 high-quality AI videos per day, following our preset scripts and styles" (Claimed) – gleiche Produktionslogik | Estimated / Claimed |
| Crossposting | YouTube-Handle 404; Instagram nicht prüfbar | Verified/n. v. |
| Virale Videos | Im Sample keins. Lebenszeit: 60.200 Likes bei 137 Videos → frühere Videos (Jun–Nov 2025) müssen deutlich mehr Reichweite gehabt haben (Ø 440 Likes/Video vs. 0,6 im Sample) | Verified (Likes) / Estimated (Verteilung) |

---

## 6. Wettbewerbsvorteil – was hat (zeitweise) funktioniert und warum nicht mehr

**Bewertung der Faktoren (Evidenz: ●●● stark / ●●○ mittel / ●○○ schwach):**

| Faktor | Beitrag | Evidenz |
|---|---|---|
| **Skript-Formel** (Symptom-Checkliste → Fake-Autorität → Todesangst → „natürliche Lösung" → Social-Proof-Zahlen → Rabatt + Countdown) | Kern des Modells; nachweislich kopierwürdig (Chang, 1,3 Mio. Views Claimed) | ●●● (ASR-Transkript + 404 Media) |
| **Volumen / billige Produktion** (≈ 23 Videos/Monat, KI-Bilder + TTS + CapCut, Overlays als Vorlage, MT-Übersetzung ins Spanische) | Erlaubt Dauer-Testing ohne Produktionskosten; Fehler (Tippfehler, Mojibake, englische Fragmente) belegen Fließband ohne QA | ●●● (Frames) |
| **Schnelles Testen / Varianten** (4 Formate, Duplikate, Hashtag-Rotation, Sprachwechsel) | Klassisches Hook-Multivariantentesting | ●●● (Verified) |
| **Produktwahl** (Leber-Detox für Trinker, $19.99, -60 %, generisches White-Label) | Hohes Problem-Bewusstsein, Impulspreis, keine Markenbindung nötig | ●●○ (Frames; Provision unbekannt) |
| **Trend-Arbitrage** (Black-Friday-Hashtags, Spanisch-Pivot auf US-Latinos, „verhafteter Arzt"-Conspiracy-Hook) | Reichweiten-Hebel über Saison und unterversorgte Sprachgruppe | ●●○ |
| **KI als solche** | Nur Kostenhebel; kein konsistenter Avatar, kein Charakter-Branding, kein Vertrauen (0 Kommentare) | ●○○ |
| **Provision** | nicht verifizierbar | – |

**Fazit:** Der Vorteil war die *Kombination* aus **Angst-Skript + Massenproduktion + Multivariantentest + Impulspreis-Produkt**, mit KI nur als Kostensenker. Das Modell ist strukturell kurzlebig: Heilversprechen, Fake-Ärzte, Fake-Zertifikate und Fake-Reviews-Zahlen sind Verstöße, die zum Verlust der Produktkarte (0/10 Anchors) und zur Reichweiten-Drosselung (Median 197 Views trotz 2,7 k Followern) führen; danach wird der Account aufgegeben (kein Upload seit 07.12.2025). Das ist ein **Burn-and-Churn-Account** eines Netzwerks – kein Beleg dafür, dass ein einzelner KI-Affiliate-Account dauerhaft Provision erwirtschaftet.

---

## 7. Einkommensschätzung (Estimated; keine veröffentlichte GMV-Quelle)

Formel: **Views/Monat × CTR × CVR × Preis × Provision**. Inputs: Preis $19.99 (Verified), CTR 1–2 %, CVR 3–5 %, Provision 15–30 % (alle Estimated).

**a) Aktueller Stand (Sample Nov/Dez 2025, dormant seit 12/2025):**
≈ 237,5 Views × 22 Videos ≈ 5.200 Views/Monat → 52–104 Klicks → 1,6–5,2 Bestellungen → GMV $31–104 → Provision **$5–31/Monat**; ohne Anchor (0/10) **tatsächlich ≈ $0**. Seit 12/2025 kein Upload → **0 USD/Monat heute**.

**b) Historische Hochphase (Jun–Nov 2025, Rückrechnung aus 60.200 Likes):**
Like-Rate 0,25 % (Sample) bis 1 % (typisch für Slop) → Lebenszeit-Views 6–24 Mio.; bei 1–3 % 2–6 Mio. Plausibler Korridor **2–10 Mio. Views in ≈ 6 Monaten = 0,3–1,7 Mio./Monat**.
- Unten: 330.000 × 1 % × 3 % × $19.99 × 15 % ≈ **$300/Monat**
- Mitte: 1.000.000 × 1,5 % × 4 % × $19.99 × 20 % ≈ **$2.400/Monat** (600 Bestellungen, GMV ≈ $12.000)
- Oben: 1.700.000 × 2 % × 5 % × $19.99 × 30 % ≈ **$10.200/Monat**
→ **Band 500–5.000 USD/Monat in der Hochphase, Konfidenz LOW** (Views-Verteilung der alten Videos unbekannt, CTR/CVR generisch, Provision unbekannt, Anchor-Historie unbekannt). Über die Lebenszeit ≈ 3.000–30.000 USD Provision gesamt (Estimated).

Dritt-Zahlen (Claimed, nicht auf diesen Account bezogen): Chang „$67,420" / „$51,000/month profit" (Rosabella-Video mit kopiertem Skript); Washenko „$400,000 last month to creators" (404 Media). Nicht übertragbar.

---

## 8. Was Nachahmer daraus lernen (ohne die Verstöße)

- Die *Struktur* des Skripts (Selbsttest-Hook „schau auf deine Fingernägel", Symptom-Checkliste, Lösung, Garantie, Preis-Anker) ist übertragbar; die *Inhalte* (Fake-Arzt, „100 % cure", Fake-Zertifikate, Fake-Countdown) sind es nicht und sind der Grund für das Ende des Accounts.
- Multivariantentest mit identischem Endscreen (Produktkarte, Preis, Pfeil) und wechselndem Front-End (Avatar/Slideshow/News-Format/Sprache) ist die eigentliche Methodik.
- Ohne Live-Produkt-Anchor (Showcase/Shop-Karte) ist die Reichweite wertlos – 0/10 Anchors = 0 Provision, egal wie viele Views.
- KI-Label: TikTok setzt aigcLabelType = 1 in 8/10 Videos; zusätzlich brennt der Betreiber „AI-generated content" ein. Das Label selbst hat die Ausspielung offenbar nicht verhindert – die Verstöße und die fehlende Vertrauensbasis (0 Kommentare, 0,25 % Likes) schon.

---

## 9. Quellen (Zugriff 2026-09-24/25)

- Profil: https://www.tiktok.com/@liverboosthub11 (tt_profile.sh)
- Embed-Liste: https://www.tiktok.com/embed/@liverboosthub11 (tt_recent.sh)
- Videos (tt_video.sh, MP4-Download/Frames für #1, #2, #6): https://www.tiktok.com/@liverboosthub11/video/7579984784156364045 · /7578930630654741791 · /7581131007449992479 · /7577080682405465374 · /7577081504858148127 · /7576330955179232525 · /7577799725806587167 · /7579325180682538271 · /7576726068787170590 · /7579713166825884958
- ASR-Untertitel (eng-US) zu 7579984784156364045: TikTok subtitleInfos-URL (Verified, research/reverse/_lbh/subs_out.txt)
- Frame-Raster/Covers: research/reverse/_lbh/sheet_*.jpg, cover_*.jpg; Rohdaten research/accounts/liverboosthub11_raw_20260925.jsonl
- 404 Media, Jason Koebler, 2026-07-30, „Inside an AI TikTok Shop Slop Factory That Shills Supplements Recalled By the FDA": https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/ (lokal research/404media.html)
- Vorheriges Dossier: research/accounts/liverboosthub11.md; Rosabella-Brand-Dossier: research/accounts/getrosabella.md
- Nicht abrufbar: Kalodata (403), Bing/DDG-Suche zum Produkt (nur Harvard-University-Treffer / Captcha), youtube.com/@liverboosthub11 (404), instagram.com/liverboosthub11 (429)
