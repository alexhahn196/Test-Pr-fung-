# 08 – Video-Reverse-Engineering (Teil 10)

**Stand:** 26.09.2026 · **Rohdaten:** [`quellen/raw_video_codings.csv`](quellen/raw_video_codings.csv) · **Vollbericht:** [`quellen/R1_video_patterns_winner_loser.md`](quellen/R1_video_patterns_winner_loser.md)

## 1. Was tatsächlich analysiert wurde

| Auftrag | Umsetzung | Abweichung |
|---|---|---|
| 30 stärkste Accounts | 30 Kanäle aus 17 Clustern, gewählt nach Millionen-Shorts in 120 T bzw. 30 T | YouTube-Shorts statt Instagram-Reels (Instagram-Videotool am Tageslimit, Reel-Views meist nicht öffentlich) |
| 10–20 Reels je Account | **733 Shorts** mit Titel und Views (je Kanal 25, die 3 neuesten übersprungen); daraus **100 codiert** (60 aus den Top 20 %, 40 aus den Bottom 50 %) | 633 Shorts nur mit Titel und Views, nicht inhaltlich codiert |
| erster Frame, Szenen, Loop, Kamera, POV, Text | **nur 15 Videos** vollständig angesehen (Tageslimit 15 Aufrufe/24 h; kostenpflichtige Erweiterung bewusst nicht aktiviert) | 85 Shorts über Transkript, Titel und Metadaten codiert, 20 davon ohne Sprache |
| Hook, Story, Trigger | für alle 100 codiert | **nicht blind**: Der Codierer kannte die Gruppe; Ergebnisse sind Hypothesen, keine Signifikanztests |

Die Senioren-Charaktere auf Instagram konnten **nicht als Video** analysiert werden. Ihre Muster stammen aus Captions, Hooks und Kommentarzahlen (M1, THIRD-PARTY OBSERVED), siehe Abschnitt 4.

## 2. Formale Merkmale (15 gesehene Videos: Story-Serien + Fußball)

| Merkmal | Top (n = 9) | Bottom (n = 6) | Einordnung |
|---|---|---|---|
| Länge (Median) | 40 s | 41 s | kein Unterschied |
| Szenen (Median) | 18 | 17 | kein Unterschied |
| Schnitte pro Sekunde | 0,58 | 0,50 | Top leicht schneller |
| Loop (Ende führt zum Anfang) | 4/9 | 2/6 | Top etwas häufiger |
| Erster Frame mit Bedrohung, Waffe oder Flucht | 3/9 | 0/6 | Top-Tendenz |
| Mitlaufende Untertitel/Keyword-Text | Standard bei Story-Serien (6/6 bzw. 4/4) | Standard | unterscheidet nicht |
| POV-Perspektive | 0/9 | 0/6 | nicht genutzt |

n ist zu klein für Schlüsse; Richtung: etwas mehr Tempo, Loop und ein Bedrohungs-Frame zum Start.

## 3. Merkmale über alle 100 codierten Shorts

| Merkmal | Top 20 % | Bottom 50 % |
|---|---|---|
| Median-Länge | 51,5 s | 45 s |
| Länge ≤ 15 / 16–30 / 31–60 / 61–120 / > 120 s | 15 / 13 / 28 / 23 / 20 % | 18 / 12 / 35 / 25 / 10 % |
| Voice: Erzähler (TTS nicht bestätigt) | 37 % | 32 % |
| Voice: TTS bestätigt | 10 % | 10 % |
| keine Sprache | 22 % | 20 % |
| Song/Gesang | 12 % | 8 % |
| Engagement-CTA | 27 % | 25 % |

Voice-Typ, Länge und CTAs unterscheiden Gewinner nicht. Den Unterschied machen **Hook und Prämisse** ([`09_winner_vs_loser.md`](09_winner_vs_loser.md)).

## 4. Muster je Cluster (Kurzfassung)

| Cluster | Typisches Gewinnerformat | Länge | Voice/Musik | Haupt-Trigger |
|---|---|---|---|---|
| **Senioren-Charaktere (IG)** | Alters-Schock-Hook („92 today. I did my push-ups…“), Verbots-/Geheimnis-Hook („Pharmacies don't want you knowing…“), dann Rezept oder Tipp; Kommentar-Keyword („Comment RECIPE/BOOK“) → DM | UNKNOWN (nicht gesehen) | Figur spricht selbst | Überraschung, Identifikation, Wissen; extreme Kommentarquoten (cookwithgrace2026: 17K Kommentare bei 10K Likes) |
| Story-Serien | Bedrohung/Rätsel mit Kind oder Familie im ersten Satz → 3 Eskalations-Beats → Twist → Moral | 25–60 s | TTS-Erzähler, Keyword-Text | Schock → Moral |
| Fußball-Sketche | bekannter Star in absurder Alltagssituation ab Frame 1; Legenden-Archiv mit Upscaling | 7–15 s bzw. 25 s | ohne Sprache / Phonk | Status, Identifikation |
| Film-What-if | „Was passiert, wenn [Mainstream-Held] X?“ bei 0:00 → Prozess in 3–4 Schritten | 25–35 s | Erzähler | Fantasie + Wissen |
| Surreal | eine gebrochene Naturregel bzw. Einbild-Rätsel mit Auswahlfrage | 5 s oder 60–80 s | ohne Sprache / Erzähler | Fantasie, Choice |
| Tiere | Tier-Ungerechtigkeit oder Mini-Rätsel → Täter-Reveal → Kommentar-Frage | 60–100 s bzw. 15–20 s | Erzähler / Song | Niedlichkeit, Gerechtigkeitssinn |
| Tierrettung | seltsam-niedliches Wesen oder Rollentausch → Pflege → Identitäts-Reveal | 90–150 s | TTS | Niedlichkeit + Überraschung |
| DIY/Cabin | maximaler Materialsprung im Titel/ersten Frame (Alltagsobjekt → Luxus) → Zeitraffer → Reveal | 45–65 s | ohne Sprache, ASMR | Transformation, Status |
| Restoration | Ikonen-Objekt im Verfall bzw. eskalierende Materialreihe → Prozess → Final-Reveal | 60–170 s | ASMR | Transformation, Nostalgie |
| Geschichte | Superlativ-These zu bekannter Figur bzw. „sieht aus wie X, ist Y“ → 3–5 eskalierende Belege | 60 s bzw. 150–180 s | Erzähler | Überraschung, Kontroverse |
| Babys/Familie | ungeheuerliche Kinderfrage als erste Zeile → absurde Eskalation → Konter | 45–55 s | KI-Song | Humor, Schock-Kontrast |
| Village-/Cozy-Cooking | Cozy-Stimmung (Wetter, Familie) statt Konflikt → Kochen → Familienwärme | 100–150 s | ohne Sprache | Nostalgie, Wholesome |
| Reise | Pick-one aus 3 Orten bzw. Superlativ-Ort | 15 s bzw. 170 s | Erzähler | Aspiration, Choice |
| Horror | universelle Regelwelt („Jeder Mensch wird geboren mit…“) → Regelbruch → Twist | 35–45 s | TTS | Fantasie, Schock |
| Gadgets | bekanntes Trendprodukt + ungewöhnliche Umnutzung + Preisanker | 25–45 s | TTS | Kaufwunsch, Neugier |

## 5. Copycats (identische Formate über Kanäle)

- **Roblox-TTS-Story-Template:** Bacon Story, Sailor Blox, Tyler, Emori; gleiche Prämisse „ALLERGIC TO WATER“ bei zwei Kanälen mit je 2,1M.
- **Geheim-Bunker/Luxus-Umbau:** Bau Rausch (≥ 8 von 25 Titeln), Virexa, ShadeMew.
- **Tierfund-Template** („A man found … and then…“): Animal Voices, Faunex (Meeresschildkröten-Rettung 5× in 25 Titeln).
- **Serien-Templates innerhalb eines Kanals:** „X Prime 🤯“ (25/25), „Which place did you like the most 1 or 2 or 3?“ (25/25), „Smart home ideas #n“ (25/25, identischer Song).
- **Instagram:** Glass-Fruit-ASMR und KI-Katzen-Storys mit Dutzenden toter Mikro-Accounts; erste Grandma-Kopien (grandpabuilder 13 Follower, grannyremedies 8 Follower).

**Befund:** Stark templatisierte Kanäle haben die größte Streuung („Algorithmus-Lotterie“, siehe 09). Der Wiedererkennungswert entsteht über die Figur bzw. Serie, nicht über das kopierte Template.

## 6. Abstrahierte Format-Baupläne

Die Baupläne je Cluster (Hook-Prinzip, Struktur, Länge, Rhythmus, visuelle Mechanik, Trigger) stehen in [`quellen/R1_video_patterns_winner_loser.md`](quellen/R1_video_patterns_winner_loser.md), Abschnitt 7. Die daraus entwickelten **eigenen** Formate für die Top 5 stehen in [`17_top5_opportunities.md`](17_top5_opportunities.md).
