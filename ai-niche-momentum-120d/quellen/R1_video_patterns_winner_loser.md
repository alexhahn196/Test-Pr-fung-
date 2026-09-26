# R1 – Video-Muster: Winner vs. Loser in KI-Short-Form-Nischen (YouTube-Proxy)

**Stand:** 2026-09-26 · **Rohdaten:** `raw_video_codings.csv` (100 codierte Shorts) · **Basis:** `raw_youtube_proxy_channels.csv`, `raw_youtube_proxy_top_shorts.csv`, `M5_youtube_proxy_momentum.md`

> **PROXY-HINWEIS:** Alle Befunde beruhen auf **YouTube Shorts**, nicht auf Instagram Reels. Das Tool für Instagram war am Tageslimit. Viele KI-Theme-Kanäle posten dieselben Clips auf YT, IG und TikTok. Ob die Befunde auf Reels übertragbar sind, ist plausibel, aber **nicht belegt**.

> **WICHTIGSTE EINSCHRÄNKUNG:** Nur **15 von 100** Shorts wurden als Video analysiert (Gemini über `watch_youtube_video_and_ask`). Danach griff das Tageslimit von **15 Aufrufen in 24 h**. Die übrigen **85** wurden über Transkript, Titel und Metadaten codiert. Bei 20 davon gab es kein Transkript (keine Sprache oder gesperrt), dort blieben nur Titel und Beschreibung. Visuelle Merkmale (erster Frame, Loop, Kamera, On-Screen-Text, Szenen) liegen deshalb **nur für 15 Videos** vor, alle aus den Clustern Story-Serien und Fußball. Die Aussagen zu Hook, Trigger und Struktur sind Codierungen des Analysten aus Audio und Titel. Sie wurden **nicht blind** erstellt, der Codierer kannte also die Gruppe.

---

## 1. Methodik

| Schritt | Vorgehen |
|---|---|
| Kanalauswahl | 30 Kanäle aus 17 Clustern (1–3 je Cluster), gewählt nach Millionen-Shorts in 120 T bzw. 30 T laut M5 und Kanal-CSV. Clusternamen stammen aus `nische_cluster`. **3 Ersatzkanäle:** Veclo FX (Surreal), Jessie Liu (Tierrettung) und storycar.barnfind (Restoration) posten aktuell andere oder kaum noch Formate (Pivot, siehe Abschnitt 7). Ersetzt durch BaconingRq, Faunex TV und CUT CRAZE. ZawPolyShorts hatte nur 10 Uploads und wurde durch Asoka ersetzt. |
| Stichprobe je Kanal | `youtube_channel_shorts` (neueste zuerst). Die 3 neuesten Shorts wurden übersprungen (Alters-Bias), danach die nächsten **25** genommen (Virexa 16, History Dude 17). Insgesamt 733 Shorts mit Titel und Views. |
| Gruppen | Je Kanal nach Views sortiert: **top20** = oberste round(0,2·n), **bottom50** = unterste n/2, Rest mid. |
| Analyse-Auswahl | Je Kanal 2 Top- und 1–2 Bottom-Shorts, zusammen **100 Shorts (60 top20 / 40 bottom50)**. |
| Video-Analyse | 15 × `watch_youtube_video_and_ask`: Bacon Story, Sailor Blox und Tyler (je 3–4), HappyHM (4), Golazo (1). Danach meldete das Tool das **RATE LIMIT 15/15 in 24h**; weitere 6 Aufrufe wurden abgelehnt. Die kostenpflichtige Erweiterung wurde bewusst nicht aktiviert. |
| Fallback | `get_bulk_video_transcripts` für alle 100 (80 mit Sprache, 20 ohne). `youtube_video_details` für Länge, Datum und Beschreibung bei 36 Shorts. Upload-Datum der Shorts unter 1 Mio. zusätzlich aus dem publishDate von youtube.com. |
| Codierung | Jeder Short bekam: Hook-Typ (A–H, siehe unten), bekannte Figur/IP/Marke (ja/nein), Extrem- bzw. Paradox-Prämisse (ja/nein, **subjektiv**), Voice-Klasse, Länge, Trigger (primär/sekundär aus der Vorgabeliste), Engagement-CTA, Produkte, Purchase-Intent. |
| Sättigung | Je Kanal Millionen-Shorts der letzten 30 T (ab 2026-08-27) gegen die Monatsrate der Tage 31–120. Die Rate ist auf die tatsächlich aktiven Tage normiert, weil viele Kanäle jünger als 120 T sind. Dazu die Median-Views der datierten Millionen-Shorts und der View-Median der Listenpositionen 4–15 (neu) gegen 28–48 (älter). |

**Hook-Typen:**
- A = Rätsel-, Paradox- oder Regelwelt-Prämisse
- B = Schock-, Konflikt- oder Gefahr-Aussage
- C = Wissensfrage oder Kuriosität
- D = Vergleich oder Pick-one
- E = Alltags- oder Beschreibungs-Einstieg
- F = kein Sprach-Hook (nur Musik oder Visual)
- G = Meme-Audio-Zeile
- H = visueller Gag bzw. Aktion ab Frame 1 (nur bei gesehenen Videos codierbar)

## 2. Stichprobe

| Cluster (CSV) | Kanäle (analysiert) | top20 / bottom50 | Datenqualität |
|---|---|---|---|
| KI-Story-Serien (animiert/Roblox/Moral) | Bacon Story, Sailor Blox, Tyler | 6 / 4 | 10× Video-Analyse |
| KI-Fußball-/Promi-Sketche | HappyHM, Golazo Fx | 4 / 3 | 5× Video, 2× Transkript |
| Film/Anime/Promi-Edits & Commentary | Super Labs | 2 / 2 | Transkript |
| KI-Surreal/VFX/What-if | Pixel Siuu, BaconingRq* | 4 / 3 | Transkript/Metadaten |
| KI-Tiere & Haustiere (Humor/Fakten) | ShadeMew, Asoka* | 4 / 2 | Transkript |
| KI-Tierrettung & Wholesome-Tierstorys | Animal Voices*, Faunex TV | 4 / 3 | Transkript |
| KI-DIY/Bau/Cabin/Handwerk | Prime Production, Bau Rausch | 4 / 4 | nur Titel/Metadaten (keine Sprache) |
| KI-Restoration/Satisfying/ASMR | Virexa Build*, CUT CRAZE* | 4 / 2 | Metadaten / Label-Transkript |
| KI-Geschichte/POV/Zeitreise | History Dude*, Silent Mastery* | 4 / 2 | Transkript |
| KI-Babys/Kinder/Familien-Comedy | Christina Kingston, Basile Khaber* | 4 / 3 | Transkript |
| KI-Kochen/Village-Food | Feels Like HOME, Ai ka churcha | 4 / 3 | Metadaten / Transkript |
| KI-Reise-Traumorte | Avena Earth, Valor Rise* | 4 / 2 | Transkript |
| KI-Horror/Mystery/True Crime | Emori Films | 2 / 2 | Transkript |
| KI-Autos/Luxus | Abhi Hub | 2 / 1 | Metadaten |
| KI-Produkte/Gadgets | Azero Shorts, Mr.Dumblings | 4 / 2 | Transkript |
| KI-Interior/Architektur/Smart Home | Adam Smart Home | 2 / 1 | Transkript (nur Song) |
| Kids/Cartoon-/Game-Figuren | DuyB* | 2 / 1 | Metadaten |

\* ai_status = UNVERIFIZIERT: Der Kanal ist nicht AI-geflaggt, sondern nur thematisch passend. Basile Khaber enthält hörbar **reale Familienaufnahmen**, ein KI-Einsatz ist nicht belegt.

## 3. Winner vs. Loser – Gesamt (100 analysierte Shorts)

### 3a. Häufigkeiten (Top20 n=60, Bottom50 n=40)

| Merkmal | Top20 | Bottom50 | Diff (pp) |
|---|---|---|---|
| **Sprach-Hook ab 0:00 mit Konflikt/Rätsel/Frage (A+B+C)** | 33/60 (55 %) | 10/40 (25 %) | **+30** |
| Hook B Schock/Konflikt/Gefahr | 15/60 (25 %) | 2/40 (5 %) | **+20** |
| Hook A Rätsel/Paradox/Regelwelt | 13/60 (22 %) | 4/40 (10 %) | +12 |
| Hook C Wissensfrage | 5/60 (8 %) | 4/40 (10 %) | −2 |
| Hook D Vergleich/Pick-one | 6/60 (10 %) | 2/40 (5 %) | +5 |
| **Hook E Alltags-/Beschreibungs-Einstieg** | 1/60 (2 %) | 11/40 (28 %) | **−26** |
| Hook F kein Sprach-Hook (Musik/Visual) | 17/60 (28 %) | 10/40 (25 %) | +3 |
| Hook G Meme-Audio-Zeile | 1/60 (2 %) | 3/40 (8 %) | −6 |
| **Bekannte Figur/IP/Marke zentral** | 21/60 (35 %) | 8/40 (20 %) | +15 |
| **Extrem-/Paradox-Prämisse** (subjektiv) | 30/60 (50 %) | 12/40 (30 %) | +20 |
| Engagement-CTA (Audio/Beschreibung/Titel) | 16/60 (27 %) | 10/40 (25 %) | +2 |
| Voice: Erzähler-Sprechertext (TTS nicht bestätigt) | 22/60 (37 %) | 13/40 (32 %) | +4 |
| Voice: TTS-Erzähler (im Video bestätigt) | 6/60 (10 %) | 4/40 (10 %) | 0 |
| Voice: keine Sprache | 13/60 (22 %) | 8/40 (20 %) | +2 |
| Voice: Song/Gesang ohne Erzähler | 7/60 (12 %) | 3/40 (8 %) | +4 |
| Voice: Meme-Audio | 2/60 (3 %) | 3/40 (8 %) | −4 |
| Länge ≤15 s / 16–30 / 31–60 / 61–120 / >120 s | 15/13/28/23/20 % | 18/12/35/25/10 % | – |
| Median-Länge | 51,5 s | 45 s | – |
| Trigger Moral/Wholesome (primär oder sekundär) | 10/60 (17 %) | 2/40 (5 %) | +12 |
| Trigger Cute | 10/60 (17 %) | 4/40 (10 %) | +7 |
| Trigger Status | 7/60 (12 %) | 2/40 (5 %) | +7 |
| Trigger Fantasy | 9/60 (15 %) | 4/40 (10 %) | +5 |
| Trigger Choice/Pick-one | 6/60 (10 %) | 2/40 (5 %) | +5 |
| Trigger Nostalgie | 7/60 (12 %) | 3/40 (8 %) | +4 |
| Trigger Shock | 14/60 (23 %) | 9/40 (22 %) | +1 |
| Trigger Transformation | 7/60 (12 %) | 5/40 (12 %) | −1 |
| Trigger Wissen | 8/60 (13 %) | 9/40 (22 %) | −9 |
| Trigger Curiosity | 12/60 (20 %) | 12/40 (30 %) | −10 |
| **Trigger Humor** | 14/60 (23 %) | 16/40 (40 %) | **−17** |
| Purchase-Intent ENTERTAINMENT / ASPIRATION / PRODUCT DESIRE / DIRECT | 70 / 18 / 12 / 0 % | 75 / 15 / 10 / 0 % | – |

### 3b. Robusterer Test: Paarvergleich innerhalb desselben Kanals

Die Unterschiede zwischen Kanälen (Nische, Abozahl) verzerren den Gesamtvergleich. Deshalb wird hier je Kanal der Anteil eines Merkmals bei den eigenen Top-Shorts mit dem bei den eigenen Bottom-Shorts verglichen (30 Kanäle).

| Merkmal | Kanäle Top > Bottom | Top < Bottom | gleich |
|---|---|---|---|
| **Hook A/B/C (Konflikt/Rätsel/Frage ab 0:00)** | **10** | **0** | 20 |
| **Hook E Alltags-Einstieg** | 0 | **10** | 20 |
| Extrem-/Paradox-Prämisse | 10 | 3 | 17 |
| Hook B Schock/Konflikt | 8 | 1 | 21 |
| Bekannte Figur/IP/Marke | 7 | 1 | 22 |
| Trigger Fantasy | 5 | 1 | 24 |
| Trigger Moral/Wholesome | 5 | 1 | 24 |
| Trigger Shock | 5 | 3 | 22 |
| Trigger Cute | 3 | 0 | 27 |
| Trigger Humor | 2 | **8** | 20 |
| Engagement-CTA | 2 | 2 | 26 |

### 3c. Nur die 15 als Video analysierten Shorts (Story-Serien + Fußball)

| Merkmal | Top (n=9) | Bottom (n=6) |
|---|---|---|
| Loop (Ende führt zurück zum Anfang) | 4/9 | 2/6 |
| Median-Szenen / Median-Länge | 18 / 40 s | 17 / 41 s |
| Schnitte pro Sekunde (Median) | 0,58 | 0,50 |
| Mitlaufende Untertitel bzw. Keyword-Text | Story: 6/6; Fußball: nur Wasserzeichen oder Songtext | Story: 4/4; Fußball: Wasserzeichen bzw. Caption |
| POV-Perspektive | 0/9 | 0/6 |
| Erster Frame mit Waffe bzw. Bedrohung oder Flucht (Messer, Flucht am Strand, Mbappé mit Messer) | 3/9 | 0/6 (sitzend, stehend, gehend, Karte zeigen, essen) |

Die Zahlen sind zu klein für Schlüsse. Tendenziell haben Top-Shorts etwas mehr Schnitte, häufiger einen Loop und häufiger einen Bedrohungs-Frame zum Start. Untertitel und Keyword-Text sind Standard und unterscheiden nicht.

### 3d. Die 5 stärksten Winner-Merkmale (gesamt)

1. **Sprach-Hook ab Sekunde 0 mit Konflikt, Rätsel oder Frage** (55 % vs. 25 %; in 10 von 10 differenzierenden Kanälen Top > Bottom).
2. **Kein beschreibender Alltags-Einstieg:** 28 % der Loser beginnen mit Kontext („A man went fishing…“, „This man is about to go crazy from the heat…“), aber nur 2 % der Winner.
3. **Schock-, Gefahr- oder Konflikt-Aussage im ersten Satz** („If I find you, I'll kill you“, „MOM, CAN I BURY A BODY…“, „Pablo Escobar was a lot scarier…“): 25 % vs. 5 %.
4. **Extreme bzw. regelbrechende Prämisse** (Regelwelt, Superlativ, Material- oder Physik-Bruch): 50 % vs. 30 %; 10:3 Kanäle.
5. **Bekannte Figur, IP oder Marke zentral** (Iron Man, Deadpool, Escobar, Henry VIII, Pelé, NeeDoh, MotoGP): 35 % vs. 20 %; 7:1 Kanäle.

Zusätzlich:
- **Emotionaler Payoff (Moral/Wholesome, Opfer, Dankbarkeit)** verstärkt Winner (17 % vs. 5 %).
- **Reiner Humor ohne Einsatz** ist ein Loser-Merkmal (23 % vs. 40 %; 8 Kanäle Bottom > Top).
- Engagement-CTAs und Voice-Typ unterscheiden **nicht**.

### 3e. Gegenbefund: Template- und Repost-Varianz („Algorithmus-Lotterie“)

In 9 Kanälen haben Top und Bottom **dasselbe Audio, Template oder sogar denselben Inhalt**. Der Unterschied bei den Views lässt sich dort nicht durch Formatmerkmale erklären:

| Kanal | Identischer Inhalt/Template | Views-Spanne |
|---|---|---|
| Basile Khaber | „Kid vaccination 😂“ als Post A / B / C | 279K / 200K / **3,4M** (17×) |
| Basile Khaber | „Twins With Completely Different Personalities“ A / B / C | 65K / 210K / 560K |
| CUT CRAZE | „Which Material Can Cut Pear“ vs. „…Pear (B)“ | 42K vs. **1,9M** (45×) |
| Golazo Fx | „Roberto Carlos Prime 🤯“ zweimal gepostet | 903K vs. **8,8M** |
| Avena Earth | gleiche Länderfolge China–Japan–Dubai (#7 vs. #28) | 1,2M vs. 50K |
| Mr.Dumblings | nahezu identisches Butter-Squishy-Skript | 4,7M vs. 10K |
| Adam Smart Home | identischer Song, identisches Titel-Template (#1–#28) | 11K – 1,5M |
| Asoka | identischer Song, Then-&-Now-Katzen | 60K – 4,5M |
| Golazo Fx | identischer PT-Phonk in Top und Bottom | 121K – 11M |

**Folge:** In Kompilations- und Repost-Formaten ist ein Hit zum großen Teil Varianz aus Timing und Seeding. Winner-Merkmale greifen vor allem in **Erzählformaten** (Story, What-if, Geschichte, Horror, Tierstory). Mehrfach-Posting desselben Clips (Post A/B/C) ist bei Basile, CUT CRAZE und Golazo eine **aktiv genutzte Taktik**.

## 4. Muster, Winner vs. Loser und WARUM – je Cluster

Format der Einträge: **Top** = was die Top-Shorts zeigen · **Bottom** = was die Bottom-Shorts zeigen · **Warum (Haupttreiber)** · **Purchase-Intent** (Einstufung und Begründung aus dem Gezeigten).

**KI-Story-Serien (Roblox/Moral)** – 10 Shorts, alle als Video gesehen
- **Top:**
  - Schock- oder Rätsel-Hook in Satz 1 (Messer, Morddrohung, „Stift 25 Jahre im Magen“, „leerer Sarg“, „Glas Wasser + Notiz“).
  - TTS-Erzähler, Roblox-3D, 24–62 s, 14–45 Szenen, Keyword-Einblendungen, Twist oder Moral am Ende.
- **Bottom:** Alltags-Einstieg („Stuhl bricht“, „ich musste aufs Klo“). Auch bei Schock-Hook fehlt die Personalisierung (Ranger mit 7 Blitzen), bzw. die Rätsel-Auflösung ist abstrakt („Room 118“).
- **Warum:** Storytelling + Überraschung (Schock-Einstieg, Twist) + Emotion/Moral als Payoff. Identifikation über Kinder und Familie.
- **Purchase-Intent:** **ENTERTAINMENT**. Sichtbare Marken (Nike-Logo, Spongebob-Shirt, Sony-Logo) sind Kulisse und werden weder thematisiert noch verlinkt.

**KI-Fußball-/Promi-Sketche** – 7 Shorts, 5 als Video gesehen
- **Top:**
  - HappyHM: fotorealistische Deepfake-Sketche Haaland/Mbappé, 8–15 s, Loop, absurde Pointe (Apfel/Messer, Bubble-Tea-Strohhalm „IQ370“).
  - Golazo: KI-upgescaltes historisches Material von Legenden (Pelé, Roberto Carlos) auf PT-Phonk, 25 s.
- **Bottom:**
  - HappyHM: statisch mit 1 Szene (Zaubertrick) bzw. Food-Guarding-Gag.
  - Golazo: Nischen-Thema „Bald XI“ bei identischem Song.
- **Warum:** Status und Identifikation (Superstars, „Prime“-Legenden), Nostalgie, Überraschung/Humor.
- **Purchase-Intent:** **ENTERTAINMENT**. Trikots (Adidas/Puma, Real/City) sind sichtbar und teils kaufbar, werden aber nie thematisiert.

**Film/Anime/Promi-Edits & Commentary (Super Labs)** – 4 Shorts
- **Top:** What-if- bzw. Wie-funktioniert-Frage zu **Mainstream-Helden** direkt ab 0:00 (Iron-Man-Nanobots, Deadpool vs. Wolverine), 29–32 s, Pointe am Ende.
- **Bottom:** obskurer Tierfakt, die Frage kommt erst bei 0:05 (Heuschreckenmaus-DNA) bzw. Nischen-Lore (Green-Lantern-Serienregel).
- **Warum:** Fantasie + Wissen, gebunden an bekannte IP (Identifikation mit Fandom).
- **Purchase-Intent:** **ENTERTAINMENT**.

**KI-Surreal/VFX/What-if** – 7 Shorts
- **Top:**
  - Pixel Siuu: 5–6-s-Einbild-Gags ohne Sprache mit Auswahlfrage (Toiletten-Koordinatengitter) bzw. Meme-Reaktion.
  - BaconingRq: 66–79-s-Fabeln mit **surrealer Regel** („Isaac fell upward“, 7-Uhr-Zeitschleife) und emotionaler Auflösung.
- **Bottom:** Meme-Zeilen-Gags ohne Interaktion bzw. klassische Parabel ohne Fantasy-Regel (Millionen-Frage).
- **Warum:** Fantasie + Überraschung. Bei den Kurz-Gags zusätzlich Interaktion (Pick-one im Kommentar).
- **Purchase-Intent:** **ENTERTAINMENT**.

**KI-Tiere & Haustiere** – 6 Shorts
- **Top:**
  - ShadeMew: 92–97-s-Erzählung mit Tier-**Ungerechtigkeit** (schwarzer vs. weißer Hund) bzw. Mini-Rätsel (Pfotenabdruck im Teig) und Kommentar-Frage.
  - Asoka: 19-s-Then-&-Now-Kompilation „berühmter“ Meme-Katzen auf Pop-Song.
- **Bottom:**
  - ShadeMew: Hitze-Absurditäten ohne Tier-Emotionskern.
  - Asoka: identisches Format mit Titel ohne „famous“.
- **Warum:** Niedlichkeit + Emotion (Mitleid, Gerechtigkeitssinn), bei Asoka Nostalgie/Wiedererkennung.
- **Purchase-Intent:** **ENTERTAINMENT**.

**KI-Tierrettung & Wholesome-Tierstorys** – 7 Shorts
- **Top:** 99–158-s-TTS-Erzählungen mit einem **seltsamen bzw. unbekannten niedlichen Wesen** („sahen aus wie Erdbeer-Gummibärchen“) oder einem **Rollentausch-Twist** (Hai hilft Schildkröte, Schildkröte bringt Geschenk, Hase überlistet Falke).
- **Bottom:**
  - Standard-Rettung (Meeresschildkröten-Rettung 5× in 25 Kanal-Titeln, davon 3× Fischernetz, 8K–44K).
  - Unspezifischer Fund („kleines Tier im Blumenbeet“).
  - Trauriges Ende (Kätzchen geht).
- **Warum:** Niedlichkeit + Überraschung (Reveal, Rollentausch) + Emotion/Moral.
- **Purchase-Intent:** **ENTERTAINMENT**.

**KI-DIY/Bau/Cabin/Handwerk** – 8 Shorts, ohne Sprache
- **Top:** Titel mit **extremem Materialsprung** hin zum Luxus („From Cardboard Mold to Luxury…“, „From Baby Dungarees to Luxury Planter“, „Floating Cabin on Plastic Bottles“, „Schulbus vergraben → Luxus-Bunker“), 45–64 s, Zeitraffer, Reveal.
- **Bottom:** gleiche Mechanik mit kleinerem Kontrast (Gartenweg, Becherhalter-Hack) bzw. Naturraum statt Alltagsobjekt als Ausgangspunkt (Höhle, Baum).
- **Warum:** Transformation + Fantasie + Status (Luxus-Endzustand).
- **Purchase-Intent:** **ASPIRATION**. Bau Rausch schreibt ausdrücklich „KI-Konzept, nicht nachbauen“. Bei Prime („Grandpa DIY“) sind generische Baumarktmaterialien sichtbar (LED-Streifen, Kies, Beton), das ergibt nur schwachen Produktbezug ohne Marke oder Link.

**KI-Restoration/Satisfying/ASMR** – 6 Shorts
- **Top:**
  - Virexa: Ikonen-Objekt (1966 Ford GT40) bzw. Fantasie-Shelter (Amazonas) mit ASMR, 164–167 s.
  - CUT CRAZE: eskalierende Materialreihe („leaf… razor blade… BMW“), die sich in Top und Bottom kaum unterscheidet.
- **Bottom:** Erkundung ohne Transformation (Utah-Sandhöhle); Material-Template mit Alltagsobjekt (Softdrink).
- **Warum:** Transformation + visuelle Schönheit + Nostalgie (Oldtimer); bei CUT CRAZE Neugier bzw. Satisfying.
- **Purchase-Intent:** **ASPIRATION** (GT40 nicht kaufbar) bzw. **ENTERTAINMENT** (CUT CRAZE).

**KI-Geschichte/POV/Zeitreise** – 6 Shorts
- **Top:**
  - History Dude: Superlativ-These zu **bekannten Figuren mit Gewalt- oder Ekel-Bezug** („Escobar was scarier…“, „Henry VIII most disgusting…“), 63 s, Eskalationsliste („But it gets worse…“).
  - Silent Mastery: Täuschungs-Hook „sieht aus wie X, ist aber Y“ mit starkem Kontrast (Kürbisblätter → leuchtendes Gelee; „giftiger“ Flussschleim → Delikatesse).
- **Bottom:** gleiches Template mit schwächerem Einsatz („Napoleon was weird“; Wintermelone → Kandis).
- **Warum:** Überraschung/Kontroverse (Dark History), Wissen, Transformation.
- **Purchase-Intent:** **ENTERTAINMENT**.

**KI-Babys/Kinder/Familien-Comedy** – 7 Shorts
- **Top:**
  - Christina Kingston: Chat-Verläufe als KI-Song (Jam AI) mit **Schock-Frage Kind → Mutter** („MOM, CAN I BURY A BODY…“, „…WILL I GO TO JAIL…“).
  - Basile: reale Kinder-Momente (Impfung, Zwillinge).
- **Bottom:** Erwachsenen-Dating-Themen (Optiker-Ex, Fremdgehen; letzteres nicht familientauglich markiert) bzw. kleine Alltagsausreden.
- **Warum:** Humor + Schock-Kontrast (Kind sagt Ungeheuerliches), Identifikation (Eltern).
- **Purchase-Intent:**
  - Christina: **PRODUCT DESIRE**. Die App „Jam AI“ steht im Titel, in anderen Kanaltiteln der Code „TINAAA“ („use my code TINAAA for free songs in jam AI“). Ein Link wurde nicht geprüft, deshalb nicht DIRECT.
  - Basile: **ENTERTAINMENT**.

**KI-Kochen/Village-Food** – 7 Shorts
- **Top:**
  - Feels Like HOME: #ghibli-Dorfalltag + Kochen + „Family Love“, 109–154 s, ohne Sprache.
  - Ai ka churcha: Hindi/Urdu-Moraldramen (Dienstmädchen am Esstisch, Vater von 4 Töchtern). Das ist inhaltlich kein Kochen mehr (Pivot).
- **Bottom:** Konflikt- oder Event-Clips (Affen am Papayabaum, Rath-Yatra-Reise mit 10 s Stille am Anfang) bzw. Vlog „enjoying at mall“.
- **Warum:** Nostalgie + visuelle Wärme (Cozy), Moral/Wholesome, Identifikation (Familie, soziale Normen).
- **Purchase-Intent:** **ENTERTAINMENT**. Weder Produkte noch Rezeptzutaten werden als kaufbar gezeigt, laut Metadaten.

**KI-Reise-Traumorte** – 6 Shorts
- **Top:**
  - Avena: 14–15-s-Pick-one aus drei Orten (Brazil/Dubai/China).
  - Valor: 171–177-s-Superlativ-Fakten („Japan is living in 2050“, „closest place to the sky“) mit Follow-Köder.
- **Bottom:** Avena identisch (Varianz); Valor mit Kuriosität statt Traumort (Kindergarten in China).
- **Warum:** Aspiration/Fernweh + Choice-Interaktion, Wissen/Status (Superlativ).
- **Purchase-Intent:** **ASPIRATION**. Valor zeigt japanische Gadgets (essbare Becher, tragbare Klimaanlage): **PRODUCT DESIRE** im Einzelfall.

**KI-Horror/Mystery (Emori Films)** – 4 Shorts
- **Top:** **Universelle Regelwelt** ab 0:00 („Every person is born with a glowing timer…“, „In this world everyone is born with a silhouette…“), 37–39 s, Opfer- oder Horror-Twist.
- **Bottom:** Ich-Erzähler-Alltagscomedy (Gym) bzw. lokale Regel (Aufzugknopf 606).
- **Warum:** Fantasie + Überraschung + Emotion (Opfer).
- **Purchase-Intent:** **ENTERTAINMENT**.

**KI-Autos/Luxus (Abhi Hub)** – 3 Shorts
- **Top:** 7–9-s-BMW-Meme-Clips mit Meme-Audio bzw. ohne Sprache.
- **Bottom:** No-Name-Go-Kart-Stunt.
- **Warum:** Status, Humor, Marke (BMW M5).
- **Purchase-Intent:** **ASPIRATION**. Die Luxusmarke ist sichtbar (laut Hashtag), Link oder Preis fehlen.

**KI-Produkte/Gadgets** – 6 Shorts
- **Top:**
  - Mr.Dumblings: **reale Marken- bzw. Trendprodukte** (NeeDoh als Handyhülle mit Preisanker „$150“, Butter-Squishy) mit DIY- oder Sound-Reveal.
  - Azero: Wissens-Hook (Kelp in Alaska, MotoGP-Narbe) mit „double tap“-Köder, **ohne** Produkte.
- **Bottom:** nahezu identisches Squishy-Skript (Varianz) bzw. Titel-Only.
- **Warum:** Kaufwunsch/Neugier (Mr.Dumblings), Wissen/Neugier (Azero).
- **Purchase-Intent:** Mr.Dumblings **PRODUCT DESIRE** (Handelsware, kein Link belegt); Azero **ENTERTAINMENT**.

**KI-Interior/Smart Home (Adam Smart Home)** – 3 Shorts
- **Top und Bottom:** identischer Song „Big boom… heart go kaboom“, Titel „Smart home ideas #n“, ca. 60 s. Kein Unterschied erkennbar.
- **Warum:** Kaufwunsch/Aspiration (laut Titel; nicht visuell bestätigt).
- **Purchase-Intent:** **PRODUCT DESIRE** (abgeleitet aus Titel und Kanalkategorie, nicht aus gesehenem Bild).

**Kids/Cartoon-/Game-Figuren (DuyB)** – 3 Shorts
- **Top:** Roblox-„Steal an Egg“: Power-Scaling („Jump 9999+ VS GIANT Bosses“, 31 s) bzw. Niedlichkeits-Vergleich („Which One is Whale Cute?“, 14 s).
- **Bottom:** Gameplay-Mini-Pointe ohne Frage.
- **Warum:** Fantasie/Status (Power-Fantasie) + Niedlichkeit, Choice.
- **Purchase-Intent:** **ENTERTAINMENT** (Roblox-Spiel, kein Kaufbezug).

### 4a. Purchase-Intent je Cluster – Übersicht

| Cluster | Einstufung | Begründung aus dem Gezeigten |
|---|---|---|
| Story-Serien, Fußball, Film/What-if, Surreal, Tiere, Tierrettung, Geschichte, Horror, Kochen, Kids/Game | **ENTERTAINMENT** | keine thematisierten oder verlinkten Produkte; Marken höchstens als Kulisse |
| DIY/Bau/Cabin | **ASPIRATION** | Luxus-Endzustand; KI-Konzepte „nicht nachbauen“; generisches Material ohne Marke |
| Restoration | **ASPIRATION** (Virexa) / ENTERTAINMENT (CUT CRAZE) | Oldtimer-Ikone nicht kaufbar |
| Reise | **ASPIRATION** (Einzelfall PRODUCT DESIRE: Japan-Gadgets) | Traumorte, Pick-one |
| Autos/Luxus | **ASPIRATION** | BMW als Statussymbol |
| Babys/Familie | **ENTERTAINMENT**, Ausnahme Christina **PRODUCT DESIRE** | KI-App im Titel, Code in anderen Titeln |
| Produkte/Gadgets | **PRODUCT DESIRE** (Mr.Dumblings) / ENTERTAINMENT (Azero) | reale Trendprodukte im Fokus |
| Interior/Smart Home | **PRODUCT DESIRE** (nur aus Titel abgeleitet) | „Smart home ideas“ |
| **DIRECT BUYING INTENT** | **in keinem analysierten Video belegt** | Links bzw. Shop-Tags wurden in keiner geprüften Beschreibung gefunden |

## 5. Copycats (identische Formate)

**Über Kanäle hinweg**
- **Roblox-TTS-Story-Template** (Schock-Hook, TTS, Keyword-Text, Twist) bei Bacon Story, Sailor Blox, Tyler und in Regelwelt-Variante bei Emori. Gleiche Titel-Prämisse „ALLERGIC TO WATER“ bei Sailor Blox (2,1M) und Tyler (2,1M).
- **Geheim-Bunker/Luxus-Umbau** bei Bau Rausch (mindestens 8 Bunker- bzw. Luxus-Umbau-Titel in 25 Shorts), Virexa („Underground Shelter“, „Sand Cave“) und ShadeMew („Secret Underground Bunker…“, 13K).
- **Tierfund- bzw. Rettungs-Template** „A man/woman found … and then…“ (Animal Voices) sowie „…Then Something Incredible Happened / Then They Saw…“ (Faunex).
- **Engagement-Köder:**
  - Azero („double tap the screen, your like will turn into…“)
  - Mr.Dumblings („if you're team X, like & subscribe“)
  - Valor Rise („If you're not following, you're probably never going to see us again“)
  - Prime Production („Comment YES or NO“)

**Innerhalb eines Kanals** (Serien-Templates und Reposts)
- „X Prime 🤯“ (Golazo, 25 von 25 Stichproben-Titeln)
- „Which place did you like the most 1 or 2 or 3? (#n)“ (Avena, 25 von 25)
- „Smart home ideas (#n)“ (Adam, 25 von 25, identischer Song)
- „Which Material Can Cut …?“ (CUT CRAZE)
- „How Ancient China Turned … Into …“ (Silent Mastery)
- „X Was [HORRIFYING/DISGUSTING/WEIRD]“ (History Dude)
- „Famous cats then and now“ (Asoka, identischer Song)
- Post-A/B/C-Reposts (Basile)
- Doppelpost „Roberto Carlos Prime“ (Golazo)
- Squishy-Skript doppelt (Mr.Dumblings)
- Meeresschildkröten-Rettung 5× (Faunex)

**Befund:** Gerade die am stärksten „templatisierten“ Kanäle haben eine hohe Streuung und fallende Bottom-Werte. Sie sind eher Lotterie als Formel (siehe 3e).

## 6. Sättigung: letzte 30 Tage vs. davor (je Kanal)

Spalten:
- **Rate-Ratio** = Millionen-Shorts in 30 T geteilt durch die normierte Monatsrate der Tage 31–120 (aktive Tage). Marktdurchschnitt laut M5: 0,69.
- **Median-Views** der datierten Millionen-Shorts.
- **Listen-Ratio** = View-Median der Positionen 4–15 geteilt durch 28–48 (nicht datiert, jüngere Shorts mit Alters-Nachteil).

| Kanal | Cluster | ≥1M 120T / 30T | Rate-Ratio | Median ≥1M: 30T vs. davor | Listen-Ratio neu/alt | Befund |
|---|---|---|---|---|---|---|
| Tyler | Story | 24 / 23 | 6,9 (Start 18.08.) | 2,3M vs. 1,7M | 7,5 | **wächst** (neuer Kanal) |
| Sailor Blox | Story | 31 / 13 | 2,2 | 3,4M vs. 3,6M | 4,1 | **wächst** |
| Bacon Story | Story | 52 / 12 | 0,9 | 1,7M vs. 4,3M | 0,31 | Hits stabil, Reichweite je Hit sinkt |
| Super Labs | Film | 36 / 21 | 4,2 | 2,9M vs. 2,2M | 1,5 | **wächst** |
| Golazo Fx | Fußball | 19 / 19 | n/a (Start 28.08.) | 2,6M | 0,82 | neu, bereits leicht fallend |
| HappyHM | Fußball | 74 / 23 | 0,59 | **4,3M vs. 23,2M** | 0,16 | **Sättigung** (Reichweite je Hit −80 %) |
| Pixel Siuu | Surreal | 46 / 31 | 1,45 | 2,3M vs. 4,5M | 0,23 | viele Hits, sinkende Median-Views |
| BaconingRq | Surreal | 10 / 1 | 0,33 | – | 10,1 | Erholung in neuesten Uploads |
| Veclo FX | Surreal | 22 / 0 | 0,0 | – vs. 2,9M | 0,06 | **eingebrochen / Pivot** |
| ShadeMew | Tiere | 11 / 4 | 0,72 | 2,1M vs. 2,0M | 5,4 (niedrige Basis) | stabil, sehr volatil |
| Asoka | Tiere | 17 / 0 | 0,0 | – vs. 2,5M | 0,16 | **gesättigt** |
| Animal Voices | Tierrettung | 14 / 3 | 0,82 | 1,7M vs. 2,2M | 0,46 | abkühlend |
| Faunex TV | Tierrettung | 7 / 2 | 0,41 | 3,0M vs. 2,0M | 0,61 | abkühlend (Template-Wiederholung) |
| Jessie Liu | Tierrettung | 33 / 0 | 0,0 | – vs. 1,9M | 0,28 | **eingebrochen / Pivot** |
| Prime Production | DIY | 31 / 6 | 0,72 | 1,9M vs. 3,5M | 0,36 | abkühlend |
| Bau Rausch | DIY | 19 / 0 | 0,0 | – vs. 3,5M | 2,9 | **keine Hits in 30 T**, neueste Uploads erholen sich |
| Virexa Build | Restoration | 9 / 3 | 1,0 | 1,4M vs. 9,5M | – | Reichweite je Hit stark gesunken |
| CUT CRAZE | Restoration | 16 / 1 | 0,2 | 1,1M vs. 3,6M | 0,19 | **gesättigt** |
| storycar.barnfind | Restoration | 22 / 4 | 0,67 | 1,1M vs. 2,6M | 0,81 | abkühlend, Pivot |
| History Dude | Geschichte | 12 / 1 | 0,25 | 1,2M vs. 5,3M | – | **abkühlend** |
| Silent Mastery | Geschichte | 10 / 2 | 0,75 | 4,9M vs. 1,4M | 0,55 | volatil |
| Christina Kingston | Babys | 29 / 0 | 0,0 | – vs. 2,1M | 0,50 | **keine Hits in 30 T** |
| Basile Khaber | Babys | 15 / 0 | 0,0 | – vs. 5,3M | 0,07 | **gesättigt** |
| Feels Like HOME | Kochen | 26 / 0 | 0,0 | – vs. 4,4M | 0,36 | **keine Hits in 30 T** |
| Ai ka churcha | Kochen | 16 / 3 | 0,52 | 1,1M vs. 4,6M | 0,22 | abkühlend + Pivot zu Moraldrama |
| Avena Earth | Reise | 11 / 0 | 0,0 | – vs. 2,4M | 0,46 | **gesättigt** |
| Valor Rise | Reise | 10 / 8 | 4,3 | 4,2M vs. 1,7M | 1,34 | **wächst** |
| Emori Films | Horror | 27 / 12 | 2,4 | 2,0M vs. 5,6M | 0,10 | mehr Hits, aber kleinere |
| Abhi Hub | Autos | 27 / 9 | 1,5 | 3,0M vs. 3,2M | 0,51 | stabil |
| Azero Shorts | Produkte | 14 / 7 | 1,9 | 1,7M vs. 1,4M | 4,5 (niedrige Basis) | wächst leicht |
| Mr.Dumblings | Produkte | 7 / 1 | 0,37 | 5,7M vs. 3,4M | 0,06 | abkühlend |
| Adam Smart Home | Interior | 6 / 2 | 0,85 | 1,3M vs. 2,6M | 1,0 | stabil, klein |
| DuyB | Kids/Game | 139 / 36 | 0,91 | 3,2M vs. 3,3M | 0,31 | Hits stabil, Listen-Median fällt |

**Zusammenfassung Sättigung**
- **Gesättigt oder eingebrochen** (0 Millionen-Shorts in 30 T trotz starker Tage 31–120): Bau Rausch, Asoka, Christina Kingston, Basile Khaber, Feels Like HOME, Avena Earth sowie die Pivot-Kanäle Veclo FX und Jessie Liu. Das betrifft vor allem die Ästhetik- und Kompilations-Cluster **DIY/Cabin, Tiere-Kompilation, Babys, Village-Food, Reise-Pick-one, Tierrettung** und deckt sich mit M5 (verlangsamt).
- **Reichweite je Hit sinkt stark:** HappyHM (23,2M → 4,3M), Virexa (9,5M → 1,4M), History Dude, Emori, Bacon Story.
- **Wachsend:** Story-Serien-Neulinge (Tyler, Sailor Blox), Super Labs (Marvel-What-if), Valor Rise (Reise-Fakten), Azero (klein).
- Die Wachstumskanäle nutzen die Winner-Merkmale aus Abschnitt 3 (Konflikt-, Rätsel- oder What-if-Hook ab 0:00, bekannte IP, Regelwelt). Gesättigte Kanäle sind überwiegend musik- oder template-basiert und haben keinen Sprach-Hook.

## 7. Format-Baupläne je Cluster (abstrahiert, keine Kopie fremder Videos)

| Cluster | Hook-Prinzip | Story-Struktur | Länge | Rhythmus | Visuelle Mechanik | Psychologischer Trigger |
|---|---|---|---|---|---|---|
| Story-Serien | Bedrohung oder Rätsel mit Kind/Familienmitglied im **ersten Satz** | Eskalation in 3 Beats → Twist → Moral in 1 Satz | 25–60 s | 0,5–0,9 Schnitte/s, Keyword-Text je Satz | 3D-Figuren, Action-Frame zum Start, Loop-Ende möglich | Schock → Erleichterung/Moral |
| Fußball/Promi | Bekannter Star in absurder Alltagssituation ab Frame 1 | Setup → visuelle Pointe | 7–15 s | 5–7 Schnitte, Loop | Nahaufnahme-Reaktion; Legenden-Archiv mit Upscaling | Status, Identifikation, Humor |
| Film/What-if | „Was passiert, wenn [Mainstream-Held] X?“ bei 0:00 | Frage → Prozess in 3–4 Schritten → Pointe | 25–35 s | Prozess-Visualisierung | 3D-Explainer | Fantasie + Wissen |
| Surreal | Eine gebrochene Naturregel bzw. ein Einbild-Rätsel | Regel → Konsequenz → emotionale Auflösung, oder Bild → Auswahlfrage | 5 s (Gag) oder 60–80 s (Fabel) | Gag: 1 Einstellung; Fabel: ruhig | Surreale Einzelbilder | Fantasie, Choice |
| Tiere | Tier-Ungerechtigkeit oder Mini-Rätsel im ersten Satz | Rätsel → Täter-Reveal → Kommentar-Frage | 60–100 s bzw. 15–20 s (Kompilation) | ruhig | Nahaufnahmen Tierreaktion | Niedlichkeit, Gerechtigkeitssinn |
| Tierrettung | Unbekanntes bzw. seltsam-niedliches Wesen oder Rollentausch (Jäger hilft Beute) | Fund → Pflege → Identitäts-Reveal → Happy End | 90–150 s | langsam, TTS | Fund-Moment als erster Frame | Niedlichkeit + Überraschung |
| DIY/Bau | Titel und erster Frame mit **maximalem Materialsprung** (Alltagsobjekt → Luxus) | Rohzustand → Zeitraffer → Reveal | 45–65 s | Zeitraffer, ASMR | Vorher-Frame mit Absurditäts-Objekt | Transformation, Status |
| Restoration | Ikonisches Objekt im Verfall oder eskalierende Materialreihe | Zerlegen → Prozess → Final-Reveal | 60–170 s | ASMR-Takt | Detail-Nahaufnahmen | Transformation, Nostalgie |
| Geschichte | Superlativ-These zu bekannter Figur („X war schlimmer als gedacht“) bzw. „sieht aus wie X, ist Y“ | These → 3–5 eskalierende Belege → Schluss-Pointe | 60 s bzw. 150–180 s | Aufzählungsrhythmus | Historische Szenen bzw. Prozess | Überraschung, Kontroverse, Wissen |
| Babys/Familie | Ungeheuerliche Kinderfrage als erste Zeile | Frage → absurde Eskalation → Konter-Pointe | 45–55 s | Song-Rhythmus | Chat-Visualisierung | Humor, Schock-Kontrast, Identifikation |
| Kochen/Village | Cozy-Stimmung (Wetter, Familie) statt Konflikt; Moraldrama mit Tischszene | Alltag → Kochen → Familienwärme bzw. Konflikt → Moral | 100–150 s | ruhig, ohne Sprache | Warmes Licht, Anime- bzw. Ghibli-Stil | Nostalgie, Wholesome |
| Reise | Pick-one aus 3 Orten bzw. Superlativ-Ort | Ort 1-2-3 → Frage, oder These → Belege → Follow | 15 s bzw. 170 s | Schnitt je Ort | Drohnen- bzw. Postkartenbild | Aspiration, Choice |
| Horror | **Universelle Regelwelt** („Jeder Mensch wird geboren mit…“) | Regel → Figur mit Nachteil → Regelbruch → Twist | 35–45 s | TTS, mittleres Tempo | Symbol der Regel im ersten Frame | Fantasie, Schock, Opfer |
| Autos | Status-Meme zu Luxusmarke | Clip → Meme-Zeile | 7–10 s | Loop | Fahrzeug-Close-up | Status |
| Produkte | Bekanntes Trendprodukt + ungewöhnliche Umnutzung + Preisanker | Problem/Neugier → Prozess → Reveal | 25–45 s | TTS | Produkt im ersten Frame | Kaufwunsch, Neugier |
| Interior | Ideen-Kompilation | Idee 1…n | ca. 60 s | Song | Vorher/Nachher (unbestätigt) | Kaufwunsch |
| Kids/Game | Power-Scaling-Zahl oder Niedlichkeits-Vergleich | Setup → Eskalation bzw. Auswahl | 14–31 s | schnell | Game-Figuren | Fantasie/Status, Choice |

## 8. Datenlücken und Grenzen

1. **Nur 15 Video-Analysen** (Tageslimit von `watch_youtube_video_and_ask`). Visuelle Felder (erster Frame, Loop, Kamera, On-Screen-Text, Szenen, POV) fehlen für 85 Shorts und für 15 von 17 Clustern (UNKNOWN in der CSV).
2. **TTS nicht bestätigt:** Bei Erzählstimmen außerhalb der 10 gesehenen Story-Videos ist unklar, ob es TTS oder eine menschliche Stimme ist.
3. **Codierung nicht blind und subjektiv:** Hook-Typ, Extrem-Prämisse und Trigger stammen von einem Codierer, der die Gruppe kannte. Die Paarvergleiche (3b) sind deshalb eher Hypothesen als Tests. Es gab keine Signifikanzprüfung, weil n je Cluster nur 3–10 beträgt.
4. **Unausgewogene Gruppen:** 60 top20 vs. 40 bottom50. Mid-Shorts wurden nicht analysiert.
5. **Große Varianz bei identischem Inhalt** (3e). Ein Teil der Top/Bottom-Unterschiede ist nicht formatbedingt.
6. **KI-Status:** 11 der 30 Kanäle sind UNVERIFIZIERT. Basile Khaber zeigt offenbar reale Aufnahmen. Prime Production und Bau Rausch deklarieren KI in der Beschreibung, Virexa „AI-assisted“.
7. **Ersatzkanäle** in Surreal, Tierrettung und Restoration: Die ursprünglich stärksten Kanäle posten die Formate nicht mehr.
8. **Sättigung:** Die 30-Tage-Werte haben einen Alters-Nachteil (M5-Marktratio 0,69). Kanäle, die nach dem 29.05. gestartet sind, wurden auf aktive Tage normiert. Golazo (Start 28.08.) hat keine Vorperiode. Die Listen-Ratio beruht auf gerundeten Views ohne Datum.
9. **Purchase-Intent** ist nur aus Titel, Audio und Beschreibung abgeleitet. Links, Shop-Tags und Pinned Comments wurden nicht geprüft (bei Adam Smart Home sind Produkte nicht visuell bestätigt).
10. **Übertragbarkeit auf Instagram Reels ist nicht belegt.** TikTok wurde nicht analysiert (`watch_tiktok_video_and_ask` ungenutzt).
11. **Nicht erhoben:** Kommentare, Retention, Thumbnail bzw. Cover und Titel-Muster der übrigen 633 Stichproben-Shorts (nur Titel und Views vorhanden, nicht codiert).
