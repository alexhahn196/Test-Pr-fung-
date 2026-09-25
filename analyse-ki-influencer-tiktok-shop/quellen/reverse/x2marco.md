# Reverse-Engineering: @x2marco (TikTok, Italien) – Human-Benchmark für TikTok-Shop-Affiliate

Stand: 2026-09-25 (Zugriffsdatum aller Quellen 2026-09-24/25). Tags: **Verified** = in TikTok-Rohdaten / heruntergeladenen Videoframes gesehen, **Claimed** = Aussage des Creators (YouTube-Transkripte), **Estimated** = eigene Rechnung mit Formel.

Methodik-Hinweis: WebSearch (Budget erschöpft) und der NexLev-Watch-Tool (Tageslimit 15/15) standen nicht zur Verfügung. Ersatz: (a) `tt_recent.sh` → 10 neueste Videos über die öffentliche Creator-Embed-Seite, (b) `tt_video.sh` für verifizierte Stats, (c) drei Videos als MP4 über die Embed-Play-URL geladen und per OpenCV analysiert (Kontaktbögen mit Frames alle ~4 s, Histogramm-Cut-Erkennung, Sticker-Dauer), (d) YouTube-Transkripte der beiden TikTok-Shop-Videos von X2Marco über NexLev. **Audio/Gesprochenes konnte nicht transkribiert werden** (kein Whisper in der Umgebung) – gesprochene Hooks sind daher „nicht öffentlich verifizierbar", On-Screen-Hooks sind Verified.

## 1. Profil (Verified, tt_profile.sh 2026-09-25)

| Feld | Wert |
|---|---|
| Follower / Likes / Videos | 369.500 / 16,0 Mio. / 1.385 |
| Account seit | 2018-09-25 |
| Bio | „LO VOGLIO ADESSO📦 / 📧Collab. x2marco@arkadia.agency" |
| Bio-Link | amazon.it/dp/B0GY4M2J1T (Affiliate-Tag „maas") = realme P4 Lite 4G Smartphone (Verified via WebFetch; Preis nicht abrufbar) |
| ttSeller / commerceUser | false / false → Affiliate, kein eigener Shop |
| Verifizierungshaken | nein |
| Modell | G – menschlicher Creator, Face-on-Camera, eigenes Studio, Editor (Claimed: „Lorenzo, my editor") |

## 2. Analysierte Videos (n = 10 neueste, Verified via tt_video.sh 2026-09-25)

Alle 10 neuesten Videos sind TikTok-Shop-Videos (`isECVideo = 1`, Hashtag #tiktokshop). Das Feld `anchors` ist bei allen leer – TikTok liefert die Produktkarte headless nicht aus; `isECVideo=1` ist der belastbare Shop-Indikator. AI-Label: `aigcLabelType = null`, `AIGCDescription = ""` bei allen 10.

| # | Video-ID | Datum (UTC) | Dauer | Views | Likes | Komm. | Shares | Saves | Beschreibung | Hook (On-Screen, Verified) | Hook-Zeitfenster |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7687958951446596886 | 23.09. 11:00 | 95 s | 2.045 | 154 | 4 | 1 | 10 | Ecco cosa mi sono portato in Egitto! #tiktokshop | Kommentar-Sticker „andrea: Marco visto che sei stato in Egitto nelle ultime due settimane, ti sei portato dei prodotti da TikTok Shop?" | 0,0–4,3 s |
| 2 | 7687957988723658006 | 23.09. 10:30 | 40 s | 1.037 | 56 | 1 | 0 | 3 | Cuscino super comodo più virale di TikTok #tiktokshop | Kommentar-Sticker „samuele: Ma quel cuscino lì serve solo per la cervicale?" | 0,0–2,5 s |
| 3 | 7687957701460069654 | 22.09. 13:30 | 30 s | 2.113 | 128 | 3 | 3 | 10 | Maschera di Spiderman più virale di TikTok #spiderman #tiktokshop | nicht heruntergeladen (Variante Maske) | – |
| 4 | 7687957461009009942 | 22.09. 12:30 | 44 s | 1.190 | 69 | 1 | 0 | 7 | Maschera di Spiderman più virale di TikTok | Variante Maske | – |
| 5 | 7687957135677721878 | 22.09. 11:30 | 38 s | 1.688 | 68 | 2 | 1 | 7 | Maschera di Spiderman più virale di TikTok | Variante Maske | – |
| 6 | 7687956667379485985 | 22.09. 10:30 | 58 s | 2.068 | 97 | 0 | 1 | 5 | Cuscino super comodo più virale di TikTok | Variante Kissen | – |
| 7 | 7687943500872076566 | 21.09. 12:00 | 37 s | **4.177** | 294 | 3 | 2 | 31 | Troppo Bella questa Maschera! #spiderman #tiktokshop | Kommentar-Sticker „nicolo: Ma il meccanismo della maschera di spiderman fa tanto rumore?" | 0,0–1,8 s |
| 8 | 7687943250593844503 | 21.09. 11:40 | 40 s | 1.529 | 91 | 2 | 1 | 8 | Maschera di Spider-Man più virale di TikTok | Variante Maske | – |
| 9 | 7687939756046535958 | 21.09. 11:35 | 41 s | 2.214 | 73 | 3 | 4 | 8 | Questa maschera è una HIT! #spiderman #tiktokshop | Variante Maske | – |
| 10 | 7687939200980700438 | 21.09. 11:30 | 68 s | 1.426 | 42 | 2 | 2 | 8 | Maschera di Spider man più virale di TikTok | Variante Maske | – |

Kennzahlen (Verified, n = 10): Summe 19.487 Views, **Ø 1.949, Median ≈ 1.867, Max 4.177**; Likes/Views ≈ 5,5 %; Kommentare fast null (0–4). Top-Video-Anteil 21 % der Stichproben-Views – **keine Ausreißer**, die Shop-Videos laufen aktuell flach. Kontrast zur älteren Stichprobe im Dossier (n = 12, Storytime 2020–2025: Ø 132.830, Median 42.700, Max 774.700): der Wechsel auf reine Produktvideos kostet in dieser Phase ~95 % der Reichweite pro Video.

Posting-Rhythmus (Verified aus createTime): 4 Videos am 21.09. (11:30–12:00, im 5-Minuten-Takt hochgeladen → Batch-Upload), 4 am 22.09. (stündlich 10:30–13:30), 2 am 23.09. (10:30, 11:00). ≈ **3,3 Videos/Tag**; entspricht der Claimed-Strategie „von 1 auf 3 Videos/Tag".

## 3. Video-Analyse (3 Videos, Frames Verified, Audio nicht verifizierbar)

### Video A – 7687943500872076566 (Spiderman-Maske, 37 s, 4.177 Views, meistgesehen)
- **Hook 0–1,8 s:** TikTok-„Antwort auf Kommentar"-Sticker oben im Bild: „nicolo: Ma il meccanismo della maschera di spiderman fa tanto rumore?" (20-9). Marco sitzt mit aufgesetzter Spiderman-Maske am Holztisch, Handy in der Hand (er „liest" den Kommentar). Gesprochener Hook: nicht verifizierbar (kein Audio-Transkript).
- **Struktur:** 0–2 s Kommentar-Hook → 3–4 s legt Handy ab → 4–36 s demonstriert mit den Händen den Mechanismus der Maske (Augenlinsen öffnen/schließen, Hand am Ohr = Bedienknopf) → 33–37 s Abschluss, Maske wird angehoben. **Ein einziger durchgehender Take, 0 Schnitte** (Histogramm-Cut-Erkennung: 0), fester Bildausschnitt (Studio, dunkler Hintergrund, Holztisch).
- **CTA:** keine On-Screen-CTA-Grafik sichtbar; keine eingeblendete Produktkarte im Video-Bild (die Shop-Karte wird nur in der TikTok-App über dem Video gerendert; `isECVideo = 1` belegt die Verknüpfung). Beschreibung ohne CTA-Text.
- **Produktdarstellung:** 100 % hands-on / am Körper getragen; kein B-Roll, kein Packaging, kein Vorher/Nachher, kein Stock, kein AI-Rendering.
- **Voiceover/Person:** realer Mensch (bekanntes Gesicht in Video B/C), Live-Sprache in die Kamera; kein AI-Avatar, keine AI-Stimme erkennbar (kein AIGC-Flag).
- **Captions:** **keine** eingebrannten Untertitel (Kontrast zum Storytime-Format mit Wort-für-Wort-Captions).
- **Musik:** „som original" (Original-Ton).
- **AI-Label:** keines. **Kommentar-Reaktion:** 3 Kommentare (Verified Zahl), Inhalte nicht abrufbar; kein „das ist KI"-Pushback möglich, da offensichtlich echt.

### Video B – 7687958951446596886 (Ägypten-Haul, 95 s, 2.045 Views, neuestes)
- **Hook 0–4,3 s:** Sticker „andrea: Marco visto che sei stato in Egitto nelle ultime due settimane, ti sei portato dei prodotti da TikTok Shop?" (20-9). Marco mit Spiderman-Maske + Handy (Cross-Referenz zum Masken-Produkt!).
- **Struktur (Verified aus Frames):** 0–5 s Kommentar-Hook (maskiert) → ~9 s nimmt Maske ab, zeigt sie in die Kamera (Produkt 1: Maske) → 19–29 s MagSafe-Powerbank am iPhone, Nahaufnahme in die Kamera (Produkt 2) → 38–48 s tragbarer Mini-Ventilator / Clip-Ventilator, Nahaufnahme des Rotors (Produkt 3) → 57–86 s Anker-Powerbank mit Display und Trageschlaufe, Nahaufnahme, Vergleich mit Handy (Produkt 4) → 86–95 s Abschluss, alle Produkte auf dem Tisch. **1 Schnitt** (bei ~24 s), sonst ein Take; Produkte werden nacheinander in die Kamera gehalten (Handheld-Makro).
- **CTA:** nicht sichtbar als Grafik; Multi-Produkt-Video = mehrere Shop-Karten in der App (nicht verifizierbar).
- **Produktdarstellung:** hands-on, ohne Verpackung, keine Stock-/AI-Elemente. Person real (Cap, Brille abgelegt), keine Captions, Musik „suara asli – Gado-Gado Semesta" (Fremd-Sound, leise, wiederverwendet in Video 6 und 10).
- **AI-Label:** keines. Kommentare: 4.

### Video C – 7687957988723658006 (Ergonomisches Kissen, 40 s, 1.037 Views)
- **Hook 0–2,5 s:** Sticker „samuele: Ma quel cuscino lì serve solo per la cervicale?" (21-9). Marco mit Brille, Kissen liegt vorne im Bild, Handy in der Hand.
- **Struktur:** 0–3 s Kommentar-Hook → 4 s hebt Kissen hoch (Form zeigen) → 8–12 s erklärt mit erhobenem Finger, legt Kopf/Arm aufs Kissen (Nutzungsdemo „Arm nicht taub") → 16–28 s Kissen drehen, drücken, Seitenschläfer-Position → 32–40 s Kissen frontal in Kamera, Finger zeigt auf die Mulde, Abschluss. **0 Schnitte**, ein Take.
- **CTA:** nicht sichtbar. Musik: „Wii Shop Channel Trap" (Meme-Sound, leise). Keine Captions. Person real. AI-Label: keines. Kommentare: 1.

**Fazit Format (Verified):** Alle drei Videos folgen exakt derselben Vorlage: **„Antwort auf Kommentar"-Sticker als Hook (0–2/4 s) → ein durchgehender Take am Studiotisch → hands-on-Demo → Ende ohne Grafik-CTA.** Extrem billige Produktion (0–1 Schnitt, keine Captions, keine Grafiken), die 3–4 Varianten/Tag erlaubt. Dies ist die Umsetzung seiner Claimed-Regel: „One video plants the seed, the second waters it, the third harvests it" – pro Produkt 5–7 Varianten mit unterschiedlichen Kommentar-Fragen (Spiderman-Maske: 7 Varianten in 2 Tagen, Kissen: 2).

## 4. Offer

| Feld | Befund | Tag |
|---|---|---|
| Produkte (aktuell) | Spiderman-Maske mit mechanischen Augenlinsen (7 Videos), ergonomisches Nacken-/Seitenschläfer-Kissen (2), Ägypten-Haul: Maske, MagSafe-Powerbank, Mini-Ventilator, Anker-Powerbank (1) | Verified (Frames/Beschreibung) |
| Frühere Produkte | Projektor, Kinder-Lenkrad, Display-Schutzfolien, Kissen, Handy-Kühler, Ohrenreiniger mit WLAN-Kamera (4 Mio. Views), Mokka-Kanne, Handdruck-Reiniger, Bluetooth-Übersetzer-Kopfhörer (negativ rezensiert) | Claimed (YouTube h2_7JN9mzEE) |
| Preise | Nicht öffentlich verifizierbar (Anchors leer; Kalodata/FastMoss ohne WebSearch nicht erreichbar). Claimed: Impulsware „€ 20-30"; Ohrenreiniger-Zitat „Cosa? €10? Ma lo voglio adesso." | Claimed |
| Rabatt/Coupon | nicht sichtbar; er sagt, TikTok subventioniert Coupons („platform that is paying you to convince you that it works") | Claimed |
| Provision | 0,50–4 €/Stück (Projektor 2 €), Seller bieten nach Viralität 5–10 €/Stück; Live: 20–50 €/Sale; effektiv ≈ 10–20 % brutto, Feb 4.900 €/44.900 € GMV = 10,9 % | Claimed |
| Impulse-Potenzial | hoch: Gadgets < 30 €, Neuheitseffekt (Maske mit beweglichen Augen), Wow-Demo in 30 s | Estimated |
| Problem/Lösung | Kissen: taube Arme/Nackenschmerz beim Seitenschlaf; Powerbank/Ventilator: Reise/Hitze; Maske: reines Entertainment/Geschenk | Verified (Demo) / Estimated |
| Zielgruppe | Italienische Gen Z / junge Erwachsene (seine Gaming-/Storytime-Community, 370 K), teils Eltern (Kinderprodukte: Lenkrad, Maske); Verkäufe auch nach DE/FR (Claimed: 25 Lenkräder DE, 5 FR) | Claimed/Estimated |

## 5. Distribution

- **Organisch vs. Search vs. Shop-Tab (Estimated):** Beschreibungen sind kurz, italienisch, mit dem Suchmuster „<Produkt> più virale di TikTok" (7 von 10) → bewusst suchoptimiert für die TikTok-Suche „maschera spiderman"/„cuscino" (Search-Anteil geschätzt 20–40 %). Kommentar-Antwort-Format zieht Follower-Traffic (For-You der 370 K Follower). Kein Hinweis auf bezahlte Ads (`isAd=false`). Shop-Tab-Anteil nicht messbar.
- **Views-Konzentration (Verified, n=10):** Top-Video 21 %, alle 10 Videos zwischen 1.037 und 4.177 → flache Verteilung, aktuell kein viraler Treiber. Historisch (Claimed): einzelne Produktvideos mit 4 Mio. Views (Ohrenreiniger), 14 Mio. Views in 3 Wochen mit 1 Video/Tag (Nov./Dez. 2025), „497 units sold with a single video".
- **Volumen:** aktuell 3,3/Tag (Verified 21.–23.09.); Claimed: 25–30 Videos an einem Aufnahmetag, Wochenvorrat; Editor übernimmt Schnitt, Kommentare und Produktrecherche.
- **Schwester-Accounts / Crossposting:** Shelfy-Seite listet nur TikTok @X2Marco, Instagram @X2Marco, YouTube (Verified WebFetch shelfy.ai/X2Marco). Instagram nicht headless lesbar; YouTube-Kanalseite nicht gerendert. Keine zweiten TikTok-Handles in Bio/Beschreibungen. Zusatz-Monetarisierung: Kurs „TikTok Shop Affiliate – Guida pratica", Gratis-PDF „11 Prodotti TikTok shop che vendono davvero", „BREAK DOWN TIKTOK SHOP" (Verified auf Shelfy), plus Agentur Arkadia (Bio).
- **Varianten:** ja, massiv – 7 Masken-Videos in 48 h mit 4 verschiedenen Beschreibungen und 3 verschiedenen Kommentar-Hooks; 2 Kissen-Videos. Gleiche Kulisse, gleiche Kleidung → an einem Tag gedreht.

## 6. Competitive Advantage (Bewertung)

**Kern-Vorteil = Bestandspublikum + industrialisierte, extrem billige Produktion + Provisionsverhandlung.** Kein AI.

1. **Warm Audience (Verified 370 K Follower, 16 Mio. Likes; seit 2018):** Selbst mit 2 K-Views-Videos hat er tägliche Grundreichweite; sein Catchphrase „Lo voglio adesso" ist als Marke etabliert (Bio, Kurs, YouTube-Hook).
2. **Produktionskosten nahe null (Verified):** 1 Take, 0–1 Schnitt, keine Captions/Grafiken, fester Studio-Set. 25–30 Videos pro Drehtag (Claimed). Das ist das menschliche Pendant zu AI-Volumen-Accounts – nur mit echter Glaubwürdigkeit (Maske wird wirklich getragen, Kissen wirklich getestet).
3. **Kommentar-Hook-System (Verified):** Jede Variante beantwortet eine echte Zuschauerfrage → Social Proof + Einwandbehandlung + Suchbegriff im Bild; zugleich TikTok-native „Reply"-Funktion, die die Kommentar-Sektion des Originalvideos verlinkt.
4. **Multi-Touch pro Produkt (Claimed + Verified 7 Varianten):** „seed – water – harvest": Kauf nach 3. Kontakt.
5. **Provisions-Arbitrage (Claimed):** identisches Video, Seller-Wechsel von 2 € auf 10 €/Stück; Seller kontaktieren ihn per WhatsApp. Nur mit Reichweite möglich.
6. **Compound-Effekt (Claimed):** Während 1 Monat Krankheitspause weiter Einnahmen aus ~100 alten Videos; Einbruch aber −46 %.

Schwächen (Verified/Claimed): Produktvideos erreichen aktuell nur ~1,5 % der Reichweite seiner Storytime-Videos; hohe Abhängigkeit vom Dauer-Output; Retouren, 30-Tage-Auszahlungssperre, Steuern → ≈ 40 % Abschlag brutto→netto; Interessenkonflikt Kursverkauf.

**Evidenzstärke:** Format/Volumen/Varianten = HOCH (Verified in Rohdaten und Frames). Provision/Umsatz = MITTEL (detaillierte, konsistente Eigenangaben ohne Screenshots). Preise/Produkt-Links = NIEDRIG (Anchors nicht öffentlich).

## 7. Einkommensschätzung (Estimated)

Formel: Monats-Views × CTR × CVR × Ø Preis × Provisionssatz.

Szenario „aktuelle Neuvideos" (Verified Inputs): 1.949 Views × 100 Videos/Monat = 195.000 Views × CTR 2 % × CVR 5 % × 25 € (Claimed) × 11 % (Claimed effektiv) ≈ 195.000 × 0,001 × 25 × 0,11 ≈ **≈ 540 €/Monat** nur aus Neuvideos.
Szenario „mit Katalog/Compound + gelegentlichem Viral-Video" (Claimed-Inputs: 100+ aktive Alt-Videos, einzelne Videos mit 0,5–4 Mio. Views): 1–4 Mio. Views/Monat → 1.000–4.000 Verkäufe × 25 € × 11 % ≈ **2.750–11.000 €/Monat**.
Claimed Referenzpunkte: Nov 2025 750 €, Dez 2025 1.600 € (Zwischenstand), Feb 2026 4.900 € (GMV 44.900 €), 90 Tage Feb–Apr 15.800 € brutto, kumuliert ≈ 24.000 € brutto / ≈ 14.000 € netto (Quelle: YouTube Wc4jy37p2kI, h2_7JN9mzEE).

**Band: 500–5.000 €/Monat Provision (Estimated), Mittelwert-Erwartung ≈ 2.000–3.000 €/Monat brutto; Claimed-Peak 4.900 €/Monat.** Netto nach Retouren/Steuern ≈ 60 % davon. Konfidenz **MEDIUM** (konsistente Eigenangaben + verifizierter Output, keine GMV-Belege Dritter).

## 8. Übertragbare Learnings für AI-/Faceless-Accounts

- Das Format „Kommentar-Frage als Hook + 1-Take-Demo" ist mit AI-Avataren kopierbar, verliert aber den Kern (echte Nutzung, Glaubwürdigkeit). Menschliche Benchmarks: 5,5 % Like-Rate, 0,1–0,2 % Kommentar-Rate bei Produktvideos.
- Variantenlogik (5–7 Videos/Produkt, verschiedene Fragen) ist der eigentliche Hebel, nicht der einzelne Hook.
- Reichweite ohne Bestandspublikum: Erwartung ~1–2 K Views/Video für reine Produktvideos, virale Ausreißer selten aber entscheidend (1 Video = 497 Verkäufe, Claimed).
- Provisionen in IT/EU: 0,5–4 €/Stück Basis, verhandelbar auf 5–10 € (Claimed) – deutlich unter US-Sätzen.

## 9. Quellen
- https://www.tiktok.com/@x2marco – tt_profile.sh, 2026-09-25 (Verified)
- https://www.tiktok.com/embed/@x2marco – 10 neueste Video-IDs + Play-URLs, 2026-09-25 (Verified)
- https://www.tiktok.com/@x2marco/video/<ID> für alle 10 IDs aus Tabelle 2 – tt_video.sh, 2026-09-25 (Verified)
- MP4-Downloads 7687943500872076566, 7687958951446596886, 7687957988723658006 → Frames/Kontaktbögen in `research/reverse/_x2m/` (Verified, 2026-09-25)
- https://www.youtube.com/watch?v=h2_7JN9mzEE – „HO PROVATO TIKTOK SHOP PER 30 GIORNI", Transkript via NexLev, 2026-09-25 (Claimed)
- https://www.youtube.com/watch?v=Wc4jy37p2kI – „QUANTO HO GUADAGNATO SU TIKTOK SHOP DOPO 3 MESI?", Transkript via NexLev, 2026-09-25 (Claimed)
- https://shelfy.ai/X2Marco – WebFetch 2026-09-25 (Verified: Kurs/PDF-Angebote, Social-Handles)
- https://www.amazon.it/dp/B0GY4M2J1T – WebFetch 2026-09-25 (Verified: realme P4 Lite; Preis nicht abrufbar)
- https://www.instagram.com/x2marco/ und https://www.youtube.com/@X2Marco – WebFetch 2026-09-25, nicht renderbar
- Vorheriges Dossier: research/accounts/x2marco.md (Stichprobe n=12 Storytime-Videos, 2026-09-24)
