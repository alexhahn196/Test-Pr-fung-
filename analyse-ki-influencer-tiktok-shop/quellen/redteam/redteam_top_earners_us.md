# Red-Team: US-Top-Earner auf TikTok Shop – Format-Check (Net-Influencer-Monatsrankings)

Stand: 2026-09-25. Rolle: Red-Team gegen den Bericht `/home/user/Test-Pr-fung-/analyse-ki-influencer-tiktok-shop/README.md` (C1–C7).
Leitfrage: Hat der Bericht die umsatzstärksten „menschlichen“ Creator als Nicht-KI/Nicht-Faceless verbucht, ohne ihr **Format** zu prüfen, und war er deshalb zu pessimistisch?

## 0. Kurzfazit (Befund vor Details)

1. **Datenbasis:** 10 Monatsausgaben „Top 10 independent creators“ von Net Influencer (Nov 2025 bis Aug 2026, Datenquelle laut Artikeln Kalodata) = **100 Monatseinträge, 41 eindeutige Creator**. Frühere Ausgaben (Aug–Okt 2025) werden im Nov-Artikel zitiert, sind aber per Site-Search und Google News nicht auffindbar. Alle Umsatzzahlen = **GMV (Claimed, Analytics-Schätzung)**, keine Provision.
2. **Schwelle:** Platz 10 lag in jedem Monat bei **0,85–1,16 Mio. USD GMV** (Median aller 100 Einträge 1,215 Mio. USD). Bei 10/15/20 % Provision entspricht das **≈ 85.000–230.000 USD Provision pro Monat** je Creator (Estimated, vor Retouren). Jeder der 41 liegt damit um den Faktor 8–40 über der 10k-USD-Schwelle.
3. **Format-Check der 24 umsatzstärksten bzw. vorgegebenen Creator** (2–3 geprüfte Shop-Videos je Account, Contact-Sheets angesehen):
   - **Kein einziger Fall A (virtueller KI-Influencer) oder B (KI-Avatar).** C1 wird durch diese Daten **bestätigt**.
   - **14 von 24 = rein „human-face“** (Person im Bild), GMV-Anteil ≈ 52 %.
   - **10 von 24 (42 %) nutzen im Stichprobenmaterial faceless bzw. hybride Formate**, GMV-Anteil ≈ **48 %** (59,6 von 124,6 Mio. USD kumuliertem GMV):
     - **2 überwiegend faceless (F, Hände + Produkt + Voice-over):** @hannahbentley (#2 kumuliert, 13,4 Mio. USD, 9 von 10 Monaten in den Top 10) und @cakedfinds (#6, 9,3 Mio. USD, 8 Monate in Folge; ≈ 19 Videos/Tag; KI-Stimme laut Reddit-Nutzer vermutet = D-Verdacht).
     - **6 gemischt human-face + faceless-Voice-over (F):** @myfamilypov, @be.lush, @kid.shops, @ericsfindss, @jordantheodore, @bestiebriitt.
     - **2 gemischt mit TikTok-AI-Label bzw. sichtbar KI-generierten Produktclips (G/H):** @kevin.finds und @airgeeksrc (beide refurbished-Apple-Deals, beide mit `aigcLabelType = "2"` auf einzelnen Shop-Videos). Zusätzlich 1 AI-gelabelter Foto-Post bei @magnificentwalnut.
4. **Konsequenz:** Der Bericht hat recht, dass **reine KI-Influencer (A/B)** in den Top-Umsatzdaten nicht vorkommen. Er ist aber **zu pessimistisch bzw. zu eng**, wenn er „KI-/Automatisierungs-taugliche“ Formate mit „virtuellen Influencern“ gleichsetzt: Das **faceless Voice-over-Format (F)** – also genau das Format, das sich mit TTS (D), KI-Skripten (E) oder KI-B-Roll (G) industrialisieren lässt – erzeugt nachweislich (Analytics, Claimed) **Monats-GMV von 1–2,4 Mio. USD pro Account, über 8–9 Monate stabil**. C3 („dauerhaft vierstellige Provisionen mit KI-Content selten“) ist für **faceless** Formate falsch; für **nachweislich KI-generierten** Content bleibt er in diesen Daten unwiderlegt (die zwei KI-nutzenden Top-Accounts verdienen ihr Geld offenbar mit Human-Face- und LIVE-Content, die AI-gelabelten Clips haben nur 900–2.800 Views).
5. **C6/C7 (830 bzw. 1.650 Videos/Monat):** Die Top-Accounts posten geschätzt **10–600 Videos/Monat** und erzielen dennoch das 10- bis 30-Fache des 20k-EUR-Ziels. Der Engpass ist nicht die Videozahl, sondern **Views pro Video** (Top-Accounts: grob 50.000–500.000 im Schnitt statt 4.000) und **AUP** (21–265 USD). C6/C7 sind als *modellbedingte* Aussagen korrekt gerechnet, aber als *allgemeine* Aussage irreführend: Der GMV/1.000-Views-Parameter des Berichts (30 USD) liegt **genau im Median der Top-Creator (25,9 USD)** – die Top-Creator sind also nicht „bessere Konverter“, sondern haben **25- bis 100-fach mehr Reichweite pro Video**.

## 1. Quellen und Methode

| Quelle | Inhalt | Evidenz | Bias |
|---|---|---|---|
| Net Influencer, 10 Monatsartikel (URLs in Abschnitt 7), Zugriff 2026-09-25 | Rang, „revenue“ (= GMV), Items, AUP, Follower, Content-Views, Debüt-Datum | analytics_platform / Claimed („Data from Kalodata“; Nov-2025-Artikel ohne Quellenangabe) | Fachmedium; Kalodata ist Analytics-Anbieter (Schätzungen, nicht TikTok-Rohdaten). Keine Kurs-/Tool-Verkäufer. |
| TikTok öffentliche Daten via `tt_profile.sh`, `tt_recent.sh`, `tt_video.sh` (2026-09-24/25) | Follower, Videozahl, Account-Alter, `isECVideo`, `isAd`, `aigcLabelType`, Plays | Verified | – |
| `tt_media.py` (Video-Download, 6 Frames, Contact-Sheet, ASR) – Sheets mit dem Read-Tool angesehen | Format-Klassifikation | Verified (visuell) / Stimme = nicht hörbar | Stichprobe 2–3 Videos pro Account |
| Frühere Recherche-Dateien (`quellen/claims_analytics_official.md` B5/B6, `quellen/sweep_reddit_x.md` 1.5) | Brandon-Hans-Interview (@be.lush), Reddit-Hinweis KI-Stimme @cakedfinds | Claimed | s. dort |

Datenqualität der Rankings (Red-Team-Hinweis, gegen die eigene These): Die Artikel enthalten **redaktionelle Widersprüche** – z. B. März 2026: „@dealswithty enters the top ten for the first time“, obwohl der Account Nov–Jan auf Platz 1–2 stand; Feb 2026 nennt für @trending_ttok „seventh in December at $1.56m“, der Dez-Artikel führt ihn als #4 mit 1,92 Mio.; identische AUP-Werte (60,81 USD) bei @hannahbentley in Feb und März, 61,00 USD bei @trending_ttok (Feb) und @dealswithty (März). Die GMV-Größenordnung ist dennoch konsistent (Platz 10 immer ≈ 0,85–1,16 Mio. USD). Kalodata-„Revenue“ kann **LIVE-GMV** enthalten und ist **vor Retouren**; bei @trending_ttok und @kevin.finds meldet TikTok `ttSeller = true` (evtl. Mischung aus Creator- und Seller-Umsatz). Stärke der GMV-Zahlen daher **medium**.

Format-Kategorien (Vorgabe): A = 100 % virtueller KI-Influencer; B = KI-Avatar + echtes Produkt; C = KI-Stimme + echtes Produktvideo; D = echte Hände + Produkt + TTS; E = echtes UGC, aber Skript/Stimme/Schnitt/Varianten per KI; F = faceless Produktvideo (Hände/Produkt, menschliche oder unbekannte Stimme); G = KI-generiertes B-Roll + echtes Produkt; H = Hybrid, KI für Zuschauer vermutlich nicht erkennbar; „human-face“ = reale Person vor der Kamera.

Hinweis zu `aigcLabelType`: In den TikTok-Webdaten taucht `aigcLabelType = "1"` bei vom Creator als KI markierten Videos auf, `"2"` bei Videos, die TikTok als KI-Inhalt kennzeichnet (Interpretation aus früheren Fällen dieser Recherche; die Wertebedeutung ist von TikTok nicht öffentlich dokumentiert, `IsAigc` war bei allen geprüften Videos `false`). Deshalb: „AI-Label gesetzt“ = Verified als Feldwert, Bedeutung = Estimated.

## 2. Format-Klassifikation der Top-Earner (Kernergebnis)

GMV-Werte = Summe über alle Top-10-Monate (Claimed, Kalodata via Net Influencer). Videos = geprüfte Shop-Videos (isECVideo = 1 bzw. Produkt-Anker), Plays Verified (2026-09-24/25).

| # kum. GMV | Creator | Kum. GMV (USD) / Monate | Geprüfte Videos (ID, Plays) | Was die Contact-Sheets zeigen | Kategorie | AI-Nutzung gefunden |
|---|---|---|---|---|---|---|
| 1 | @trending_ttok | 17,99 Mio. / 10 | 7689258510520995085 (6.891), 7689271433783954702 (1.825), 7606928625702554894 (2.383, Feb) | Mann spricht in die Kamera; Split-Screen-„Welches ist besser?“-Sketch mit sich selbst (zwei Takes) | human-face | keine (IsAigc false, kein Label) |
| 2 | @hannahbentley | 13,42 Mio. / 9 | 7688418962152901901 (23.000), 7688430894322961678 (4.602), 7603860160955632909 (587.000, Feb) | **nur Hände + Produkt** (Handtücher, Bettdecke), Voice-over, Text-Sticker; kein Gesicht in 3/3 Videos | **F** (Stimme wirkt laut ASR natürlich, Füllwörter „like, I don’t even know…“ → vermutlich menschlich) | kein Label; Stimme nicht hörbar |
| 3 | @dealswithty | 13,14 Mio. / 6 | 7689297266468769055 (7.138), 7689246743086533918 (5.200) | Mann hält Produkt (Kindle, Beats) in die Kamera | human-face | keine |
| 4 | @myfamilypov | 11,89 Mio. / 7 | 7689223073333054750 (1.908), 7689200538000362783 (1.668), 7601723591821987103 (318.700, Feb) | Video 1: Gesicht nur im Hook, dann Füße/Hände; Video 2: **nur Hände + Waschmaschine, Voice-over**; Feb-Video: Familien-Sketch mit Frau im Bild | gemischt human-face + **F** | keine; **Bio verkauft System/Kurs** („How We Run $100K+/mo TikTok Shop – Learn the system“, stan.store) |
| 5 | @be.lush | 11,75 Mio. / 6 | 7688976100755574030 (11.200), 7688943187171314957 (8.049), 7622084928053857549 (34.400, März-Rekordmonat) | 2× Brandon im Bild; März-Video: **faceless Staubsauger-Vergleich, nur Produkt/Füße, Voice-over** | gemischt human-face + **F** | keine; Interview: „faceless voiceover format“ brachte ein Video mit „over a million dollars in sales“ (Claimed) |
| 6 | @cakedfinds | 9,28 Mio. / 8 | 7680788024334077215 (21.600), 7677790952005668126 (18.600), 7609234293906328862 (5.223, Feb) | **nur Hände + Karton/Produkt**, POV; identische Caption „It’s on such a good deal today 😳“ auf 9 von 10 neuesten Videos; Skript-Template („not one, not two, but three…“) | **F, D-Verdacht** | Reddit-Nutzer fragt „exact AI voice that Cakefinds … uses“ (Claimed); Audio-Hüllkurven zweier Videos mit identischem Satzanfang korrelieren 0,80 vs. 0,21–0,25 bei verschiedenen Anfängen (Estimated, **nicht beweisend**); kein TikTok-Label |
| 7 | @highland.fashion7 | 4,74 Mio. / 3 | 7689179290910346510 (14.400), 7689165908031425806 (7.656), 7594824582951996685 (4.565) | Mitschnitte aus Studio-LIVE: Moderatorinnen („Host: T“), Preis-Overlays, Countdown; 9.596 Videos | human-face (LIVE-Studio-Betrieb, kein Solo-Creator) | keine |
| 8 | @torijflow | 4,39 Mio. / 4 | 7688551437130927390 (99.300), 7688844830927015199 (70.600) | Spiegel-Selfie-Try-on, Gesicht teils hinter dem Handy | human-face | keine |
| 9 | @dj.foof | 4,16 Mio. / 4 | 7569020147126603039 (11,1 Mio.), 7539681636422569246 (7,1 Mio.) | Fashion-Try-on, Person voll im Bild | human-face | keine |
| 10 | @anniedanner | 3,47 Mio. / 3 | 7688545809872309518 (9.489), 7688554459076644109 (5.030) | Try-on, Gesicht im Bild | human-face | keine |
| 11 | @mikaylanogueira | 3,36 Mio. / 2 | 7586792309128203533 (10,4 Mio.), 7572258910120217911 (8,7 Mio.) | Make-up-Talking-Head (17,4 Mio. Follower) | human-face | keine |
| 12 | @kid.shops | 3,30 Mio. / 3 | 7688914157948685599 (10.900), 7688874883152973087 (10.200) | Video 1 Talking Head; Video 2 **nur Hände + CarPlay-Display, Voice-over** | gemischt human-face + **F** | keine |
| 13 | @ericsfindss | 3,26 Mio. / 2 | 7688837043840945422 (3.024), 7688769107793136909 (2.330), 7657584864127962382 (**3,7 Mio.**) | 2× Mann vor Ninja-Regal; virales Video: **nur Staubsauger + Hand + Handy-Screenshot, Voice-over** | gemischt human-face + **F** | keine; Business-Mail @proecomltd.com (Firma/Agentur dahinter – Hinweis, nicht verifiziert) |
| 14 | @kajsa.ziebell | 3,16 Mio. / 3 | 7688948680958741774 (8.155), 7688872329396505869 (2.674) | Skincare-Talking-Head | human-face | keine |
| 15 | @sarahgibbons_ | 2,94 Mio. / 2 | 7681354577811098911 (397.600), 7681751862604877086 (124.800) | Frau im Bild mit Schuhen | human-face; **E-Verdacht** (25.000 Videos, formelhafte Captions mit Gedankenstrichen „…—they’re so co…“, „basically permission to…“) | kein Label; KI-Captions nicht verifizierbar |
| 16 | @kevin.finds | 2,15 Mio. / 2 | **7688905577250032926 (2.072, `aigcLabelType = 2`)**, 7689192075023158558 (1.345) | Video 1: **cineastische MacBook-Szenen auf Teppich mit verformtem Apple-Logo, generischer KI-Kunst auf dem Display**, Text-Overlays; ASR „fully updated to the 2027 Golden Gate“ (sinnlos, TTS/KI-typisch). Video 2: Mann mit MacBook (LIVE-Rest-Deal) | gemischt human-face + **G (KI-generierter Produktclip) mit TTS-Verdacht** | **ja: TikTok-AI-Label (Verified Feldwert) + sichtbare KI-Artefakte**; `ttSeller = true` |
| 17 | @prettypickedd | 1,97 Mio. / 2 | 7689248998405721358 (17.000), 7689248565746486542 (2.351) | Jeans-Try-on, Gesicht im Bild | human-face | keine |
| 18 | @jordantheodore | 1,82 Mio. / 1 | 7688829790756818207 (18.900), 7688831520706022687 (17.300) | Video 1: **nur Hände/Auto/Handtuch, Voice-over**; Video 2: Split-Sketch mit zwei Takes derselben Person, dann Hände | gemischt **F** + human-face | keine |
| 19 | @aleximorales12 | 1,62 Mio. / 1 | 7686858513867377951 (10.600), 7686608365799116063 (8.168) | Mann präsentiert Jacke/Schirm (Spanisch) | human-face | keine |
| 20 | @bestiebriitt | 1,60 Mio. / 1 | 7688963027655249183 (3.925), 7689182665890647326 (2.443) | Video 1 Talking Head im Auto; Video 2 **POV-Hand sprüht Reiniger, nur Text + Musik** | gemischt human-face + **F** | keine |
| (21) | @magnificentwalnut | 1,58 Mio. / 1 | 7685930900462341406 (23.000); Foto-Post 7686554662308285726 (2.230, `aigcLabelType = 2`) | Video: junger Mann mit Scooter; Foto-Carousel: Mann auf E-Bike + Produktfoto | human-face (+1 AI-gelabelter Foto-Post, H) | Label gesetzt (Feldwert), Ursache unklar |
| (22) | @natiscart | 1,44 Mio. / 1 | 7672887142812618015 (2,8 Mio.), 7681783445785283871 (1,6 Mio.) | Skincare-Selbsttest, Gesicht | human-face | keine |
| (28) | @airgeeksrc | 1,09 Mio. / 1 | **7688760943236500750 (2.817, `aigcLabelType = 2`)**, 7688547081010580749 (17.900), 7611067129126849806 (**12,4 Mio.**), 7666464793829690637 (1,2 Mio.), 7681476215349316878 (1.261) | AI-gelabeltes Video: **MacBook-Produktszenen, Letterbox, verstümmelter Schriftzug „MacBoo M“**, keine Sprache; virales 12,4-Mio.-Video: **faceless RC-Auto, keine Sprache**; übrige: Mann im Bild, bewirbt LIVE | gemischt human-face + **F** + **G** | **ja: 4 von 12 neuesten Shop-Videos mit `aigcLabelType = 2`** (Plays 63–2.817) |
| (32) | @huntergrazianoo | 1,04 Mio. / 1 | 7688812477068496142 (189.700), 7688801238355430669 (15.800), 7681342790390910221 (154.700) | BH-Try-on; Split-Screen mit drei Takes derselben Person | human-face | keine |

Nicht geprüft (Rang 23–41, je 1 Monat): @sadiejonesuploading, @yandi.perez2, @styledbylilea, @bennettfinds, @jordyn_gunderson, @themaddiehaven, @sophmademebuyit, @mydlvz1, @victoriaaa131313, @skincarepronikki, @alreviews0, @midlife.nursing, @ediedricks_, @sharpafedc, @therealmustbecindy, @quinclips3, @vanessesencials.

### 2.1 Anteile (Deliverable 2)

| Gruppe | Anzahl (von 24) | Kum. GMV (USD) | GMV-Anteil |
|---|---|---|---|
| rein human-face | 14 | 65,0 Mio. | 52,2 % |
| überwiegend faceless (F, D-Verdacht bei @cakedfinds) | 2 | 22,7 Mio. | 18,2 % |
| gemischt human-face + faceless Voice-over (F) | 6 | 33,6 Mio. | 27,0 % |
| gemischt mit AI-Label / KI-Produktclips (G) | 2 | 3,2 Mio. | 2,6 % |
| **faceless oder hybrid (C/D/E/F/G/H) gesamt** | **10 (42 %)** | **59,6 Mio.** | **47,8 %** |
| A/B (virtuell / KI-Avatar) | 0 | 0 | 0 % |

Nur Top 20 nach kumuliertem GMV: 9 von 20 (45 %) faceless/hybrid, GMV-Anteil 58,5 von 119,4 Mio. USD = **49,0 %**.
Einschränkung: „gemischt“ heißt, dass mindestens eines der 2–3 geprüften Shop-Videos ohne Gesicht auskommt; der tatsächliche Anteil faceless Videos im Gesamtkatalog ist nicht bekannt. Welche Videos das GMV tragen, zeigt Kalodata nicht in den Artikeln.

### 2.2 Gefundene KI-Nutzung (Deliverable 3)

- **Verified (Feldwert + visuell):** @kevin.finds (1 von 10 neuesten Videos, KI-typische Artefakte, sinnlose Sprachzeile) und @airgeeksrc (4 von 12 neuesten Videos mit `aigcLabelType = 2`, eines visuell mit verstümmeltem Schriftzug). Beide verkaufen refurbished MacBooks/iPads mit AUP 131–187 USD und bewerben LIVE-Streams. Die AI-gelabelten Clips erreichen **nur 63–2.817 Plays**; die Umsätze stammen nach allem Sichtbaren aus Human-Face-Videos, einem faceless Viral-Hit (12,4 Mio.) und LIVE (GMV/1.000 Content-Views 135–170 USD, d. h. das meiste GMV lässt sich nicht aus Video-Views erklären → LIVE-Anteil wahrscheinlich hoch, Estimated).
- **Verified (Feldwert), Bedeutung offen:** @magnificentwalnut Foto-Carousel mit `aigcLabelType = 2`.
- **Claimed:** @cakedfinds nutzt eine KI-Stimme (Reddit-Frage, 2026-07-30, Beitrag von Mods entfernt). Eigene Audio-Prüfung nur Indiz.
- **Nicht verifizierbar, Verdacht:** KI-geschriebene Captions bei @sarahgibbons_ (E).
- **Keine KI erkennbar** bei 19 von 24 Accounts; `IsAigc` war bei allen 50+ geprüften Videos `false`.
- **Formatmuster, die sich industrialisieren lassen, aber menschlich produziert sind:** Split-Screen-Sketches mit mehreren Takes derselben Person (@trending_ttok, @huntergrazianoo, @jordantheodore) – leicht mit KI-Varianten verwechselbar, hier aber echtes Filmmaterial.

## 3. Ökonomie der Top-Earner (Estimated)

- **GMV pro 1.000 Content-Views** (72 Monatseinträge mit Views): Median **25,9 USD**, Interquartil 18,2–36,9 USD, Spanne 4,7 (@quinclips3) bis 170,1 USD (@kevin.finds, LIVE-lastig). Der Bericht nimmt „realistisch 30 USD“ an – **das ist Top-Creator-Niveau, nicht zu pessimistisch**.
- **Faceless-Beispiele:** @hannahbentley gepoolt 24,4 USD/1.000 Views; @cakedfinds 30,3 USD.
- **Implizierte Provision** (Formel: GMV × Satz; vor Retouren ~10 %): Median-Eintrag 1,215 Mio. USD → 121.500 / 182.250 / 243.000 USD bei 10/15/20 %. Faceless @hannahbentley Ø 1,49 Mio. USD/Monat → **149.000–298.000 USD/Monat**; @cakedfinds Ø 1,16 Mio. → **116.000–232.000 USD/Monat**. Plausibilitätsanker: Brandon Hans (@be.lush) sagt, er habe „$100,000 per month in commission … for almost two years“ verdient; höchster bekannter Einzelmonat „over $200,000“ (Claimed, Net Influencer 2026-06-15).
- **Views und Videozahl:** Content-Views der Top-10 je Monat 6,9–196 Mio. Posting (Estimated aus Account-Alter bzw. neuesten 10 Videos, verrauscht): @hannahbentley ≈ 1–3/Tag, @cakedfinds ≈ 19/Tag (12.700 Videos in 681 Tagen), @trending_ttok ≈ 5+/Tag, @myfamilypov ≈ 3–20/Tag, @sarahgibbons_ ≈ 11/Tag (25.000 Videos). Daraus grob: @hannahbentley Juni 2026 47,5 Mio. Views / ≈ 90 Videos ≈ **500.000 Views/Video**; @cakedfinds Juni 54,5 Mio. / ≈ 570 Videos ≈ **96.000 Views/Video** und ≈ 2.800 USD GMV/Video (≈ 420 USD Provision bei 15 %) gegenüber 4.000 Views und 14,97 EUR Provision pro Video im „realistischen“ Berichtsmodell (Faktor ≈ 25–30).
- **Dauerhaftigkeit:** Faceless @hannahbentley 9 von 10 Monaten in den Top 10 (Nov 2025–Jul 2026), @cakedfinds 8 Monate in Folge (Jan–Aug 2026). Gegenindiz: @cakedfinds’ neuestes öffentliches Video datiert vom **2026-09-02** (tt_recent, 2026-09-25) – ≈ 3 Wochen Pause bei einem 19-Videos/Tag-Account (Ursache unbekannt: Sperre, Strategie, Embed-Grenze).

## 4. Was das für C3, C4, C6, C7 bedeutet (Deliverable 4)

**C3 – „Dauerhafte vierstellige Monatsprovisionen mit KI-Content sind selten.“**
- *Gegenbeweis (stark für faceless, schwach für echte KI):* Zwei überwiegend faceless Accounts halten sich 8–9 Monate mit ≈ 1–2,4 Mio. USD GMV/Monat in den Top 10 (Claimed Analytics) → **sechsstellige** Provision/Monat (Estimated). Sechs weitere Top-Accounts nutzen faceless Voice-over als festen Formatbaustein; bei @be.lush stammt laut Interview der umsatzstärkste Einzelhit aus dem faceless Voice-over-Format.
- *Was bleibt:* Kein Top-Account ist nachweislich *KI-generiert*; die zwei Accounts mit AI-Label nutzen KI nur für Nebenclips mit Mini-Reichweite. Die Aussage ist also für **A/B/G als Hauptformat** gedeckt, für **„KI-unterstützte“ faceless Produktion (D/E/F)** zu pessimistisch formuliert: Das Format, das man mit TTS/KI-Skript/KI-Schnitt nachbauen würde, *ist* bewiesen profitabel – offen ist nur, ob es mit synthetischer Stimme genauso konvertiert (Indiz @cakedfinds).
- Empfehlung Formulierung: „Dauerhaft hohe Provisionen mit vollständig KI-generiertem Content sind in öffentlichen Daten nicht belegt; faceless Voice-over-Formate (in denen KI Teilaufgaben übernehmen kann) erreichen dagegen belegt sechsstellige Monatsprovisionen.“

**C4 – „10.000+ USD-Einkommensbehauptungen kommen vor allem von Kursverkäufern.“**
- *Gegenbeweis:* Die Analytics-Daten zeigen **41 unabhängige Creator** mit je ≥ 0,85 Mio. USD GMV in mindestens einem Monat – bei jedem Provisionssatz ≥ 5 % über 10k USD. Die Mehrheit verkauft **keine** Kurse (Bios: Collab-Mails, keine Funnel).
- *Aber:* Diese Zahlen sind keine Selbstaussagen, sondern Drittanalysen; C4 betrifft die *Quelle von Claims*, nicht die Existenz von Top-Verdienern. Und selbst unter den Top-Earnern monetarisiert @myfamilypov („How We Run $100K+/mo TikTok Shop – Learn the system“) über ein System/Kurs → C4 als Beobachtung über **Claims** bleibt korrekt, als Aussage über die **Realität** wäre sie falsch. Der Bericht sollte ausdrücklich sagen, dass 10k+ real existiert, aber auf ein sehr kleines, fast nur US-amerikanisches, Human-/Faceless-geführtes Top-Segment konzentriert ist.

**C6/C7 – „10.000 EUR brauchen ~830, 20.000 EUR ~1.650 Videos/Monat (vermutlich Team).“**
- *Gegenbeweis:* Top-Accounts erreichen das 10- bis 30-Fache des 20k-EUR-Ziels mit geschätzt **10–600 Videos/Monat**; faceless @hannahbentley mit nur ≈ 1–3 Videos/Tag. Die Videozahl ist also keine notwendige Bedingung, sondern Folge der Modellannahme 4.000 Views/Video.
- *Rechnung (Estimated):* 10.000 EUR Gewinn ≈ 10.870 USD (1 USD = 0,92 EUR) + Toolkosten ≈ 11.500 USD Provision → bei 15 % ≈ 77.000 USD GMV → bei 25,9 USD/1.000 Views (Top-Median) ≈ **3,0 Mio. Views/Monat**. Das sind ≈ 750 Videos à 4.000 Views (Berichtslogik bestätigt), aber nur **30 Videos à 100.000 Views** oder **6 Videos à 500.000 Views**. Entscheidend ist die Verteilung der Views, nicht die Anzahl.
- *Was bleibt:* Die geprüften Top-Accounts sind fast alle schon 1–7 Jahre alt, haben 15.000–850.000 Follower und posten teils sehr viel (@cakedfinds ≈ 570, @sarahgibbons_ ≈ 330, @highland.fashion7 ≈ 270 Videos/Monat, Estimated) – Volumen ist bei den faceless/Deal-Accounts also sehr wohl Teil des Rezepts. @highland.fashion7 (LIVE-Studio) und @ericsfindss (Firmen-E-Mail) deuten auf **Teams/Firmen** hinter „independent creators“ → C7 („vermutlich Team“) wird eher gestützt.
- Empfehlung: C6/C7 als „bei 4.000 Views/Video“ kennzeichnen und eine zweite Zeile mit Views-pro-Video als Hebel ergänzen; der Bericht unterschätzt nicht die Konversion, sondern stellt Reichweite als fix dar.

**C1/C2/C5 (Randnotizen):** C1 bestätigt (0 von 41 A/B). C2 hier nicht getestet (Top-Earner sind Home/Beauty/Fashion/Elektronik-Deals, keine Supplement-Netzwerke – das stützt eher die These, dass *langlebige* Top-Umsätze nicht aus Supplement-KI-Netzwerken kommen). C5: Der GMV/1.000-Views-Parameter von 30 USD ist durch diese Daten gedeckt (Median 25,9 USD); pessimistisch ist allenfalls die Views-Annahme.

## 5. Ehrliche Einordnung / Gegen-Gegenargumente

- **Survivorship:** 41 Accounts von ≈ 2 Mio. „commissioned creator-marketers“ (Net Influencer Q3 2026, Claimed); die Top 10 sind das oberste 0,001 %. Ein faceless Format, das bei @hannahbentley funktioniert, sagt nichts über die Erfolgsquote neuer Accounts.
- **Kalodata-GMV ≠ Provision:** unbekannte Provisionssätze (Shark/Ninja-Kampagnen häufig 10–15 %, teils Retainer/Boni), Retouren, LIVE-Anteil, mögliche Seller-Umsätze (`ttSeller = true` bei @trending_ttok, @kevin.finds).
- **Stichprobe klein:** 2–3 Videos pro Account; „faceless“-Anteil pro Account kann über- oder unterschätzt sein.
- **Stimme nicht hörbar:** D (TTS) vs. F (menschliche Stimme) kann aus Frames + ASR nicht sicher unterschieden werden.
- **Kein Beleg für reine KI-Accounts mit Top-Umsatz** – das bleibt die stärkste Stütze des Originalberichts.

## 6. Ausreißer-Videos (Verified Plays; GMV pro Video nicht öffentlich)

| Video | Creator | Format | Plays | Bemerkung |
|---|---|---|---|---|
| https://www.tiktok.com/@airgeeksrc/video/7611067129126849806 | @airgeeksrc | F (faceless RC-Auto, keine Sprache) | 12,4 Mio. | isAd, isECVideo 1 |
| https://www.tiktok.com/@dj.foof/video/7569020147126603039 | @dj.foof | human-face | 11,1 Mio. | Fashion-Try-on |
| https://www.tiktok.com/@ericsfindss/video/7657584864127962382 | @ericsfindss | F (faceless Voice-over) | 3,7 Mio. | Staubsauger |
| https://www.tiktok.com/@natiscart/video/7672887142812618015 | @natiscart | human-face | 2,8 Mio. | Skincare-Selbsttest |
| https://www.tiktok.com/@hannahbentley/video/7603860160955632909 | @hannahbentley | F | 587.000 | Bettdecke (Mellow) |
| https://www.tiktok.com/@myfamilypov/video/7601723591821987103 | @myfamilypov | human-face Sketch | 318.700 | Matratzen-Topper |
| https://www.tiktok.com/@huntergrazianoo/video/7688812477068496142 | @huntergrazianoo | human-face Split-Sketch | 189.700 | OEAK Jelly-BH |
| https://www.tiktok.com/@kevin.finds/video/7688905577250032926 | @kevin.finds | G + TTS-Verdacht, `aigcLabelType 2` | 2.072 | KI-Clip, geringe Reichweite |
| https://www.tiktok.com/@airgeeksrc/video/7688760943236500750 | @airgeeksrc | G, `aigcLabelType 2` | 2.817 | KI-Artefakt im Schriftzug |

## 7. Quellen-URLs (Zugriff 2026-09-25)

- Nov 2025: https://www.netinfluencer.com/tiktok-shop-top-10-creators-made-20-million-in-november/ (publ. 2025-12-23)
- Dez 2025: https://www.netinfluencer.com/the-10-tiktok-creators-who-generated-the-most-sales-in-december-2025/ (2026-01-16)
- Jan 2026: https://www.netinfluencer.com/top-10-sales-by-independent-creators-on-tiktok-in-january-2026/ (2026-02-06)
- Feb 2026: https://www.netinfluencer.com/top-10-independent-tiktok-creators-who-generated-the-most-sales-in-february-2026/ (2026-03-03)
- Mär 2026: https://www.netinfluencer.com/top-10-sales-by-independent-creators-on-tiktok-in-march-2026/ (2026-04-11)
- Apr 2026: https://www.netinfluencer.com/10-independent-creators-who-drove-the-most-tiktok-shop-sales-in-april-2026/ (2026-05-07)
- Mai 2026: https://www.netinfluencer.com/top-10-independent-creator-sales-on-tiktok-shop-in-may-2026/ (2026-06-04)
- Jun 2026: https://www.netinfluencer.com/top-10-independent-creator-sales-on-tiktok-shop-in-june-2026/ (2026-07-20)
- Jul 2026: https://www.netinfluencer.com/top-10-independent-creator-sales-on-tiktok-shop-in-july-2026/ (2026-08-06)
- Aug 2026: https://www.netinfluencer.com/top-10-sales-by-independent-creators-on-tiktok-in-august-2026/ (2026-09-24)
- Brandon Hans (@be.lush): https://www.netinfluencer.com/for-brandon-hans-23m-usd-in-tiktok-shop-sales-starts-with-getting-someone-to-stop-scrolling/ (2026-06-15)
- Reddit-Hinweis KI-Stimme @cakedfinds: https://www.reddit.com/r/TikTokshop/comments/1vakqqr/ (2026-07-30, entfernt; via frühere Recherche)
- Site-Search: https://www.netinfluencer.com/?s=top+10+independent , https://www.netinfluencer.com/?s=independent+creators , weitere Suchbegriffe (keine Ausgaben vor Nov 2025 gefunden)
- TikTok-Profile/Videos: https://www.tiktok.com/@<handle> bzw. die Video-URLs in Abschnitt 2 und 6; Rohdaten (Profile, Video-Metadaten, Kontaktbögen) lagen in der Arbeitsumgebung und sind nicht Teil des Repos.

## 8. Vollständige Creator-Tabellen (Deliverable 1)

### Tabelle 1: Alle 100 Monatseinträge (GMV/Items/AUP/Follower/Views = Claimed, Kalodata via Net Influencer; GMV/1k Views und Provision = Estimated)

| Monat | Rang | Creator | GMV (USD) | Items | AUP (USD) | Follower | Content-Views | GMV/1.000 Views (USD) | Provision 10 / 15 / 20 % (USD) |
|---|---|---|---|---|---|---|---|---|---|
| 2025-11 | 1 | @dealswithty | 4.870.000 | – | – | 127.400 | – | – | 487.000 / 730.500 / 974.000 |
| 2025-11 | 2 | @hannahbentley | 1.940.000 | – | – | 29.900 | – | – | 194.000 / 291.000 / 388.000 |
| 2025-11 | 3 | @highland.fashion7 | 1.900.000 | – | – | – | – | – | 190.000 / 285.000 / 380.000 |
| 2025-11 | 4 | @myfamilypov | 1.810.000 | – | – | 173.300 | – | – | 181.000 / 271.500 / 362.000 |
| 2025-11 | 5 | @be.lush | 1.650.000 | – | – | – | – | – | 165.000 / 247.500 / 330.000 |
| 2025-11 | 5 | @sarahgibbons_ | 1.650.000 | – | – | – | – | – | 165.000 / 247.500 / 330.000 |
| 2025-11 | 7 | @mikaylanogueira | 1.630.000 | – | – | 17.400.000 | – | – | 163.000 / 244.500 / 326.000 |
| 2025-11 | 8 | @aleximorales12 | 1.620.000 | – | – | 333.800 | – | – | 162.000 / 243.000 / 324.000 |
| 2025-11 | 9 | @magnificentwalnut | 1.580.000 | – | – | 50.400 | – | – | 158.000 / 237.000 / 316.000 |
| 2025-11 | 10 | @trending_ttok | 1.560.000 | – | – | 143.800 | 72,95 Mio. | 21,4 | 156.000 / 234.000 / 312.000 |
| 2025-12 | 1 | @dealswithty | 2.720.000 | – | – | 136.500 | 86,65 Mio. | 31,4 | 272.000 / 408.000 / 544.000 |
| 2025-12 | 2 | @hannahbentley | 2.370.000 | – | – | 35.900 | 97,72 Mio. | 24,3 | 237.000 / 355.500 / 474.000 |
| 2025-12 | 3 | @myfamilypov | 2.000.000 | – | – | 206.600 | 155,04 Mio. | 12,9 | 200.000 / 300.000 / 400.000 |
| 2025-12 | 4 | @trending_ttok | 1.920.000 | – | – | 164.100 | 120,27 Mio. | 16,0 | 192.000 / 288.000 / 384.000 |
| 2025-12 | 5 | @highland.fashion7 | 1.830.000 | – | – | 240.700 | 16,83 Mio. | 108,7 | 183.000 / 274.500 / 366.000 |
| 2025-12 | 6 | @be.lush | 1.750.000 | – | – | 231.600 | 45,22 Mio. | 38,7 | 175.000 / 262.500 / 350.000 |
| 2025-12 | 7 | @mikaylanogueira | 1.730.000 | – | – | 17.400.000 | 326,99 Mio. | 5,3 | 173.000 / 259.500 / 346.000 |
| 2025-12 | 8 | @anniedanner | 1.370.000 | – | – | 32.800 | 62,91 Mio. | 21,8 | 137.000 / 205.500 / 274.000 |
| 2025-12 | 9 | @sarahgibbons_ | 1.290.000 | – | – | 249.400 | 35,26 Mio. | 36,6 | 129.000 / 193.500 / 258.000 |
| 2025-12 | 10 | @sadiejonesuploading | 1.160.000 | – | – | 37.100 | 38,81 Mio. | 29,9 | 116.000 / 174.000 / 232.000 |
| 2026-01 | 1 | @anniedanner | 1.230.000 | – | 21,16 | 38.500 | 74,93 Mio. | 16,4 | 123.000 / 184.500 / 246.000 |
| 2026-01 | 2 | @dealswithty | 1.200.000 | – | 129,46 | 141.000 | 41,96 Mio. | 28,6 | 120.000 / 180.000 / 240.000 |
| 2026-01 | 3 | @cakedfinds | 1.180.000 | – | 52,59 | 37.600 | 45,43 Mio. | 26,0 | 118.000 / 177.000 / 236.000 |
| 2026-01 | 4 | @jordyn_gunderson | 1.110.000 | – | – | 150.800 | 47,31 Mio. | 23,5 | 111.000 / 166.500 / 222.000 |
| 2026-01 | 5 | @prettypickedd | 1.050.000 | – | 32,47 | 112.300 | 134,18 Mio. | 7,8 | 105.000 / 157.500 / 210.000 |
| 2026-01 | 6 | @highland.fashion7 | 1.010.000 | – | 20,13 | 245.900 | 12,50 Mio. | 80,8 | 101.000 / 151.500 / 202.000 |
| 2026-01 | 7 | @trending_ttok | 1.000.000 | – | 40,02 | 171.400 | 74,94 Mio. | 13,3 | 100.000 / 150.000 / 200.000 |
| 2026-01 | 8 | @hannahbentley | 989.560 | – | 62,34 | 40.500 | 46,02 Mio. | 21,5 | 98.956 / 148.434 / 197.912 |
| 2026-01 | 9 | @midlife.nursing | 947.230 | – | 60,92 | 31.100 | 36,73 Mio. | 25,8 | 94.723 / 142.084 / 189.446 |
| 2026-01 | 10 | @kid.shops | 907.200 | – | 41,06 | 170.300 | 124,28 Mio. | 7,3 | 90.720 / 136.080 / 181.440 |
| 2026-02 | 1 | @hannahbentley | 1.370.000 | – | 60,81 | 44.900 | 71,09 Mio. | 19,3 | 137.000 / 205.500 / 274.000 |
| 2026-02 | 2 | @trending_ttok | 1.140.000 | – | 61,00 | 178.100 | 52,30 Mio. | 21,8 | 114.000 / 171.000 / 228.000 |
| 2026-02 | 3 | @cakedfinds | 975.760 | – | 55,17 | 43.900 | 31,48 Mio. | 31,0 | 97.576 / 146.364 / 195.152 |
| 2026-02 | 4 | @skincarepronikki | 956.630 | – | 48,22 | 137.600 | 29,55 Mio. | 32,4 | 95.663 / 143.494 / 191.326 |
| 2026-02 | 5 | @sharpafedc | 929.320 | – | 61,47 | 172.500 | 54,56 Mio. | 17,0 | 92.932 / 139.398 / 185.864 |
| 2026-02 | 6 | @prettypickedd | 919.690 | – | 36,58 | 127.700 | 69,46 Mio. | 13,2 | 91.969 / 137.954 / 183.938 |
| 2026-02 | 7 | @myfamilypov | 918.590 | – | 26,38 | 242.200 | 96,37 Mio. | 9,5 | 91.859 / 137.788 / 183.718 |
| 2026-02 | 8 | @therealmustbecindy | 888.540 | – | 47,09 | 1.100.000 | 24,01 Mio. | 37,0 | 88.854 / 133.281 / 177.708 |
| 2026-02 | 9 | @quinclips3 | 871.990 | – | 15,45 | 64.400 | 185,89 Mio. | 4,7 | 87.199 / 130.798 / 174.398 |
| 2026-02 | 10 | @anniedanner | 868.540 | – | 23,35 | 43.000 | 37,01 Mio. | 23,5 | 86.854 / 130.281 / 173.708 |
| 2026-03 | 1 | @be.lush | 3.970.000 | 18.620 | ≈213,21 (Est.) | 249.100 | – | – | 397.000 / 595.500 / 794.000 |
| 2026-03 | 2 | @dealswithty | 2.150.000 | 10.610 | ≈202,64 (Est.) | 146.400 | – | – | 215.000 / 322.500 / 430.000 |
| 2026-03 | 3 | @hannahbentley | 1.530.000 | – | – | 52.600 | – | – | 153.000 / 229.500 / 306.000 |
| 2026-03 | 4 | @trending_ttok | 1.450.000 | – | – | 185.800 | – | – | 145.000 / 217.500 / 290.000 |
| 2026-03 | 5 | @yandi.perez2 | 1.160.000 | 3.860 | ≈300,52 (Est.) | 12.300 | – | – | 116.000 / 174.000 / 232.000 |
| 2026-03 | 6 | @cakedfinds | 1.150.000 | – | – | 50.100 | – | – | 115.000 / 172.500 / 230.000 |
| 2026-03 | 7 | @themaddiehaven | 1.060.000 | 5.970 | ≈177,55 (Est.) | 31.800 | – | – | 106.000 / 159.000 / 212.000 |
| 2026-03 | 8 | @mydlvz1 | 1.040.000 | 28.610 | ≈36,35 (Est.) | 37.400 | – | – | 104.000 / 156.000 / 208.000 |
| 2026-03 | 9 | @kajsa.ziebell | 1.030.000 | – | – | 33.600 | – | – | 103.000 / 154.500 / 206.000 |
| 2026-03 | 10 | @victoriaaa131313 | 971.730 | 21.740 | ≈44,70 (Est.) | 30.800 | – | – | 97.173 / 145.760 / 194.346 |
| 2026-04 | 1 | @trending_ttok | 2.150.000 | 22.740 | ≈94,55 (Est.) | 195.700 | 60,57 Mio. | 35,5 | 215.000 / 322.500 / 430.000 |
| 2026-04 | 2 | @be.lush | 1.690.000 | 9.810 | ≈172,27 (Est.) | 257.700 | 28,60 Mio. | 59,1 | 169.000 / 253.500 / 338.000 |
| 2026-04 | 3 | @bestiebriitt | 1.600.000 | 13.940 | ≈114,78 (Est.) | 130.100 | 40,71 Mio. | 39,3 | 160.000 / 240.000 / 320.000 |
| 2026-04 | 4 | @hannahbentley | 1.320.000 | 18.440 | ≈71,58 (Est.) | 57.900 | 51,77 Mio. | 25,5 | 132.000 / 198.000 / 264.000 |
| 2026-04 | 5 | @cakedfinds | 960.660 | 21.050 | ≈45,64 (Est.) | 55.500 | 30,95 Mio. | 31,0 | 96.066 / 144.099 / 192.132 |
| 2026-04 | 6 | @ediedricks_ | 945.600 | 6.780 | ≈139,47 (Est.) | 104.700 | 17,46 Mio. | 54,2 | 94.560 / 141.840 / 189.120 |
| 2026-04 | 7 | @dj.foof | 927.700 | 29.820 | 31,10 | 835.600 | 59,85 Mio. | 15,5 | 92.770 / 139.155 / 185.540 |
| 2026-04 | 8 | @dealswithty | 917.010 | 6.550 | ≈140,00 (Est.) | 148.300 | 21,64 Mio. | 42,4 | 91.701 / 137.552 / 183.402 |
| 2026-04 | 9 | @torijflow | 863.260 | 25.010 | ≈34,52 (Est.) | 283.900 | 48,76 Mio. | 17,7 | 86.326 / 129.489 / 172.652 |
| 2026-04 | 10 | @vanessesencials | 853.750 | 12.890 | 41,06 | 28.500 | 7,27 Mio. | 117,4 | 85.375 / 128.062 / 170.750 |
| 2026-05 | 1 | @jordantheodore | 1.820.000 | 9.190 | 197,62 | 283.300 | 37,58 Mio. | 48,4 | 182.000 / 273.000 / 364.000 |
| 2026-05 | 2 | @trending_ttok | 1.780.000 | 24.680 | 72,03 | 204.300 | 57,67 Mio. | 30,9 | 178.000 / 267.000 / 356.000 |
| 2026-05 | 3 | @ericsfindss | 1.640.000 | 6.190 | 265,18 | 13.400 | 29,04 Mio. | 56,5 | 164.000 / 246.000 / 328.000 |
| 2026-05 | 4 | @be.lush | 1.540.000 | 9.410 | 163,08 | 262.300 | 32,45 Mio. | 47,5 | 154.000 / 231.000 / 308.000 |
| 2026-05 | 5 | @myfamilypov | 1.320.000 | 39.240 | 33,60 | 276.400 | 93,96 Mio. | 14,0 | 132.000 / 198.000 / 264.000 |
| 2026-05 | 6 | @hannahbentley | 1.310.000 | 21.480 | 60,76 | 62.600 | 42,06 Mio. | 31,1 | 131.000 / 196.500 / 262.000 |
| 2026-05 | 7 | @dealswithty | 1.280.000 | 9.290 | 137,99 | 154.800 | 62,68 Mio. | 20,4 | 128.000 / 192.000 / 256.000 |
| 2026-05 | 8 | @kajsa.ziebell | 1.100.000 | 22.300 | 49,41 | 54.700 | 46,67 Mio. | 23,6 | 110.000 / 165.000 / 220.000 |
| 2026-05 | 9 | @sophmademebuyit | 1.060.000 | 22.040 | 47,35 | 25.500 | 34,39 Mio. | 30,8 | 106.000 / 159.000 / 212.000 |
| 2026-05 | 10 | @cakedfinds | 1.040.000 | 21.110 | 49,35 | 61.100 | 32,26 Mio. | 32,2 | 104.000 / 156.000 / 208.000 |
| 2026-06 | 1 | @myfamilypov | 2.560.000 | 82.850 | 30,84 | 292.200 | 195,73 Mio. | 13,1 | 256.000 / 384.000 / 512.000 |
| 2026-06 | 2 | @trending_ttok | 1.970.000 | 23.810 | 82,58 | 210.500 | 63,41 Mio. | 31,1 | 197.000 / 295.500 / 394.000 |
| 2026-06 | 3 | @ericsfindss | 1.620.000 | 6.190 | 261,55 | 15.000 | 30,13 Mio. | 53,8 | 162.000 / 243.000 / 324.000 |
| 2026-06 | 4 | @cakedfinds | 1.590.000 | 30.870 | 51,65 | 67.500 | 54,54 Mio. | 29,2 | 159.000 / 238.500 / 318.000 |
| 2026-06 | 5 | @natiscart | 1.440.000 | 77.300 | 18,62 | 92.900 | 127,19 Mio. | 11,3 | 144.000 / 216.000 / 288.000 |
| 2026-06 | 6 | @hannahbentley | 1.320.000 | 27.150 | 48,58 | 67.900 | 47,52 Mio. | 27,8 | 132.000 / 198.000 / 264.000 |
| 2026-06 | 7 | @kid.shops | 1.280.000 | 16.200 | 79,12 | 183.700 | 60,66 Mio. | 21,1 | 128.000 / 192.000 / 256.000 |
| 2026-06 | 8 | @torijflow | 1.200.000 | 37.540 | 32,05 | 309.600 | 55,21 Mio. | 21,7 | 120.000 / 180.000 / 240.000 |
| 2026-06 | 9 | @dj.foof | 1.200.000 | 35.070 | 34,18 | 845.800 | 55,32 Mio. | 21,7 | 120.000 / 180.000 / 240.000 |
| 2026-06 | 10 | @be.lush | 1.150.000 | 11.560 | 99,93 | 265.100 | 30,64 Mio. | 37,5 | 115.000 / 172.500 / 230.000 |
| 2026-07 | 1 | @trending_ttok | 1.650.000 | 18.830 | 87,69 | 215.200 | 56,77 Mio. | 29,1 | 165.000 / 247.500 / 330.000 |
| 2026-07 | 2 | @myfamilypov | 1.500.000 | 62.810 | 23,93 | 303.900 | – | – | 150.000 / 225.000 / 300.000 |
| 2026-07 | 3 | @cakedfinds | 1.350.000 | – | – | – | – | – | 135.000 / 202.500 / 270.000 |
| 2026-07 | 4 | @hannahbentley | 1.270.000 | – | – | – | – | – | 127.000 / 190.500 / 254.000 |
| 2026-07 | 5 | @styledbylilea | 1.160.000 | 36.100 | 32,05 | – | – | – | 116.000 / 174.000 / 232.000 |
| 2026-07 | 6 | @dj.foof | 1.040.000 | – | – | 849.800 | – | – | 104.000 / 156.000 / 208.000 |
| 2026-07 | 7 | @kajsa.ziebell | 1.030.000 | 19.060 | 54,02 | 75.600 | – | – | 103.000 / 154.500 / 206.000 |
| 2026-07 | 8 | @torijflow | 1.000.000 | 30.580 | 32,76 | 325.400 | – | – | 100.000 / 150.000 / 200.000 |
| 2026-07 | 9 | @kevin.finds | 975.780 | 7.420 | 131,47 | 222.300 | – | – | 97.578 / 146.367 / 195.156 |
| 2026-07 | 10 | @alreviews0 | 954.840 | 46.520 | 20,53 | 112.200 | – | – | 95.484 / 143.226 / 190.968 |
| 2026-08 | 1 | @trending_ttok | 3.370.000 | 29.060 | 115,97 | 229.300 | 90,70 Mio. | 37,2 | 337.000 / 505.500 / 674.000 |
| 2026-08 | 2 | @myfamilypov | 1.780.000 | 47.940 | 37,22 | 318.900 | 100,01 Mio. | 17,8 | 178.000 / 267.000 / 356.000 |
| 2026-08 | 3 | @torijflow | 1.330.000 | 36.560 | 36,28 | 336.800 | 69,06 Mio. | 19,3 | 133.000 / 199.500 / 266.000 |
| 2026-08 | 4 | @kevin.finds | 1.170.000 | 7.490 | 155,80 | 235.200 | 6,88 Mio. | 170,1 | 117.000 / 175.500 / 234.000 |
| 2026-08 | 5 | @bennettfinds | 1.130.000 | 8.940 | 126,14 | 53.900 | 24,05 Mio. | 47,0 | 113.000 / 169.500 / 226.000 |
| 2026-08 | 6 | @kid.shops | 1.110.000 | 12.340 | 89,98 | 189.300 | 50,20 Mio. | 22,1 | 111.000 / 166.500 / 222.000 |
| 2026-08 | 7 | @airgeeksrc | 1.090.000 | 5.860 | 186,96 | 209.800 | 8,07 Mio. | 135,1 | 109.000 / 163.500 / 218.000 |
| 2026-08 | 8 | @huntergrazianoo | 1.040.000 | 47.490 | 21,83 | 15.700 | 79,14 Mio. | 13,1 | 104.000 / 156.000 / 208.000 |
| 2026-08 | 9 | @cakedfinds | 1.030.000 | 18.430 | 55,84 | 76.900 | 29,29 Mio. | 35,2 | 103.000 / 154.500 / 206.000 |
| 2026-08 | 10 | @dj.foof | 989.400 | 28.630 | 34,56 | 853.800 | 45,51 Mio. | 21,7 | 98.940 / 148.410 / 197.880 |

### Tabelle 2: 41 eindeutige Creator, aggregiert (Nov 2025 – Aug 2026)

| # | Creator | Monate in Top 10 | Summe GMV (USD) | Max-Monat (USD) | Ø GMV je gelistetem Monat (USD) | GMV/1.000 Views gepoolt (USD) | Ø Provision/Monat bei 10 / 15 / 20 % (USD, Est.) |
|---|---|---|---|---|---|---|---|
| 1 | @trending_ttok | 10 (2025-11; 2025-12; 2026-01; 2026-02; 2026-03; 2026-04; 2026-05; 2026-06; 2026-07; 2026-08) | 17.990.000 | 3.370.000 | 1.799.000 | 25,5 | 179.900 / 269.850 / 359.800 |
| 2 | @hannahbentley | 9 (2025-11; 2025-12; 2026-01; 2026-02; 2026-03; 2026-04; 2026-05; 2026-06; 2026-07) | 13.419.560 | 2.370.000 | 1.491.062 | 24,4 | 149.106 / 223.659 / 298.212 |
| 3 | @dealswithty | 6 (2025-11; 2025-12; 2026-01; 2026-03; 2026-04; 2026-05) | 13.137.010 | 4.870.000 | 2.189.502 | 28,7 | 218.950 / 328.425 / 437.900 |
| 4 | @myfamilypov | 7 (2025-11; 2025-12; 2026-02; 2026-05; 2026-06; 2026-07; 2026-08) | 11.888.590 | 2.560.000 | 1.698.370 | 13,4 | 169.837 / 254.756 / 339.674 |
| 5 | @be.lush | 6 (2025-11; 2025-12; 2026-03; 2026-04; 2026-05; 2026-06) | 11.750.000 | 3.970.000 | 1.958.333 | 44,8 | 195.833 / 293.750 / 391.667 |
| 6 | @cakedfinds | 8 (2026-01; 2026-02; 2026-03; 2026-04; 2026-05; 2026-06; 2026-07; 2026-08) | 9.276.420 | 1.590.000 | 1.159.552 | 30,3 | 115.955 / 173.933 / 231.910 |
| 7 | @highland.fashion7 | 3 (2025-11; 2025-12; 2026-01) | 4.740.000 | 1.900.000 | 1.580.000 | 96,8 | 158.000 / 237.000 / 316.000 |
| 8 | @torijflow | 4 (2026-04; 2026-06; 2026-07; 2026-08) | 4.393.260 | 1.330.000 | 1.098.315 | 19,6 | 109.832 / 164.747 / 219.663 |
| 9 | @dj.foof | 4 (2026-04; 2026-06; 2026-07; 2026-08) | 4.157.100 | 1.200.000 | 1.039.275 | 19,4 | 103.928 / 155.891 / 207.855 |
| 10 | @anniedanner | 3 (2025-12; 2026-01; 2026-02) | 3.468.540 | 1.370.000 | 1.156.180 | 19,8 | 115.618 / 173.427 / 231.236 |
| 11 | @mikaylanogueira | 2 (2025-11; 2025-12) | 3.360.000 | 1.730.000 | 1.680.000 | 5,3 | 168.000 / 252.000 / 336.000 |
| 12 | @kid.shops | 3 (2026-01; 2026-06; 2026-08) | 3.297.200 | 1.280.000 | 1.099.067 | 14,0 | 109.907 / 164.860 / 219.813 |
| 13 | @ericsfindss | 2 (2026-05; 2026-06) | 3.260.000 | 1.640.000 | 1.630.000 | 55,1 | 163.000 / 244.500 / 326.000 |
| 14 | @kajsa.ziebell | 3 (2026-03; 2026-05; 2026-07) | 3.160.000 | 1.100.000 | 1.053.333 | 23,6 | 105.333 / 158.000 / 210.667 |
| 15 | @sarahgibbons_ | 2 (2025-11; 2025-12) | 2.940.000 | 1.650.000 | 1.470.000 | 36,6 | 147.000 / 220.500 / 294.000 |
| 16 | @kevin.finds | 2 (2026-07; 2026-08) | 2.145.780 | 1.170.000 | 1.072.890 | 170,1 | 107.289 / 160.934 / 214.578 |
| 17 | @prettypickedd | 2 (2026-01; 2026-02) | 1.969.690 | 1.050.000 | 984.845 | 9,7 | 98.484 / 147.727 / 196.969 |
| 18 | @jordantheodore | 1 (2026-05) | 1.820.000 | 1.820.000 | 1.820.000 | 48,4 | 182.000 / 273.000 / 364.000 |
| 19 | @aleximorales12 | 1 (2025-11) | 1.620.000 | 1.620.000 | 1.620.000 | – | 162.000 / 243.000 / 324.000 |
| 20 | @bestiebriitt | 1 (2026-04) | 1.600.000 | 1.600.000 | 1.600.000 | 39,3 | 160.000 / 240.000 / 320.000 |
| 21 | @magnificentwalnut | 1 (2025-11) | 1.580.000 | 1.580.000 | 1.580.000 | – | 158.000 / 237.000 / 316.000 |
| 22 | @natiscart | 1 (2026-06) | 1.440.000 | 1.440.000 | 1.440.000 | 11,3 | 144.000 / 216.000 / 288.000 |
| 23 | @sadiejonesuploading | 1 (2025-12) | 1.160.000 | 1.160.000 | 1.160.000 | 29,9 | 116.000 / 174.000 / 232.000 |
| 24 | @yandi.perez2 | 1 (2026-03) | 1.160.000 | 1.160.000 | 1.160.000 | – | 116.000 / 174.000 / 232.000 |
| 25 | @styledbylilea | 1 (2026-07) | 1.160.000 | 1.160.000 | 1.160.000 | – | 116.000 / 174.000 / 232.000 |
| 26 | @bennettfinds | 1 (2026-08) | 1.130.000 | 1.130.000 | 1.130.000 | 47,0 | 113.000 / 169.500 / 226.000 |
| 27 | @jordyn_gunderson | 1 (2026-01) | 1.110.000 | 1.110.000 | 1.110.000 | 23,5 | 111.000 / 166.500 / 222.000 |
| 28 | @airgeeksrc | 1 (2026-08) | 1.090.000 | 1.090.000 | 1.090.000 | 135,1 | 109.000 / 163.500 / 218.000 |
| 29 | @themaddiehaven | 1 (2026-03) | 1.060.000 | 1.060.000 | 1.060.000 | – | 106.000 / 159.000 / 212.000 |
| 30 | @sophmademebuyit | 1 (2026-05) | 1.060.000 | 1.060.000 | 1.060.000 | 30,8 | 106.000 / 159.000 / 212.000 |
| 31 | @mydlvz1 | 1 (2026-03) | 1.040.000 | 1.040.000 | 1.040.000 | – | 104.000 / 156.000 / 208.000 |
| 32 | @huntergrazianoo | 1 (2026-08) | 1.040.000 | 1.040.000 | 1.040.000 | 13,1 | 104.000 / 156.000 / 208.000 |
| 33 | @victoriaaa131313 | 1 (2026-03) | 971.730 | 971.730 | 971.730 | – | 97.173 / 145.760 / 194.346 |
| 34 | @skincarepronikki | 1 (2026-02) | 956.630 | 956.630 | 956.630 | 32,4 | 95.663 / 143.494 / 191.326 |
| 35 | @alreviews0 | 1 (2026-07) | 954.840 | 954.840 | 954.840 | – | 95.484 / 143.226 / 190.968 |
| 36 | @midlife.nursing | 1 (2026-01) | 947.230 | 947.230 | 947.230 | 25,8 | 94.723 / 142.084 / 189.446 |
| 37 | @ediedricks_ | 1 (2026-04) | 945.600 | 945.600 | 945.600 | 54,2 | 94.560 / 141.840 / 189.120 |
| 38 | @sharpafedc | 1 (2026-02) | 929.320 | 929.320 | 929.320 | 17,0 | 92.932 / 139.398 / 185.864 |
| 39 | @therealmustbecindy | 1 (2026-02) | 888.540 | 888.540 | 888.540 | 37,0 | 88.854 / 133.281 / 177.708 |
| 40 | @quinclips3 | 1 (2026-02) | 871.990 | 871.990 | 871.990 | 4,7 | 87.199 / 130.798 / 174.398 |
| 41 | @vanessesencials | 1 (2026-04) | 853.750 | 853.750 | 853.750 | 117,4 | 85.375 / 128.062 / 170.750 |

<!-- stats: n=100 min=853750 median=1215000.0 -->
<!-- gpm n=72 median=25.9 p25=18.2 p75=36.9 min=4.7 max=170.1 -->

### Verifikation TE1

Prüfer: Verifikations-Agent, 2026-09-25. **Urteil: PARTIALLY** (Richtung hält, Details und Reichweite der Gegenbeweise zu korrigieren).

- **Quellen erneut geöffnet:** Alle 10 Net-Influencer-URLs liefern HTTP 200 (Veröffentlichung 2025-12-23 bis 2026-09-24). Dez–Aug nennen „Data (source) from Kalodata“; **der Nov-2025-Artikel nennt keine Datenquelle** (Kalodata dort nur angenommen). Stichproben im Live-Text stimmen mit den Tabellenwerten überein (Nov #1 @dealswithty 4,87 Mio., Nov #10 @trending_ttok 1,56 Mio., Apr #10 @vanessesencials 853,75k). Der Nov-Artikel zitiert Aug/Okt-Werte (z. B. @be.lush Okt. 918.970 USD) → frühere Ausgaben existierten.
- **Arithmetik nachgerechnet** (100 Einträge, 41 eindeutige Handles – bestätigt): Median 1,215 Mio. USD → 121.500 / 182.250 / 243.000 USD bei 10/15/20 % (korrekt, Estimated, vor Retouren). Min 853.750, Max 4,87 Mio. USD (korrekt).
- **Fehler:** „Platz 10 brauchte jeden Monat 0,85–1,16 Mio. USD“ stimmt nicht für Nov 2025 (#10 = 1,56 Mio.). Korrekt: **0,85–1,56 Mio. USD**. Weiterer Widerspruch in den Artikeln: Juli 2026 schreibt, die #10-Schwelle falle „erstmals“ unter 1 Mio. USD, obwohl sie Jan–Apr bereits darunter lag (907k, 869k, 972k, 854k) → Stärke „medium“ ist angemessen, eher medium-niedrig.
- **Metrik:** GMV („revenue“, Kalodata-Schätzung), nicht Provision; teils LIVE-GMV, bei @trending_ttok `ttSeller = true` (Verified, 2026-09-25) → Umrechnung in Affiliate-Provision mit 10–20 % ist eine Obergrenzen-Näherung.
- **TikTok-Nachprüfung (2026-09-25):** @hannahbentley existiert, 74.500 Follower, 2.704 Videos, Konto seit 2019; 4 neueste Videos alle `isECVideo = 1`, kein AI-Label; `tt_media.py` auf 7689214812047428877 (999 Plays): Contact-Sheet zeigt **nur Hände + Diffusor-Produkt, Voice-over** → Kategorie **F**, keine KI sichtbar, `IsAigc = false`. @dealswithty: 2 neueste Videos Shop-Videos, kein Label. @trending_ttok: ttSeller true.
- **Zuordnung zu C3/C4:** Gegen **C4** trägt TE1 nur als Existenzbeleg (10k+ USD real, aber Drittschätzung, keine Selbstaussage – C4 betrifft die Herkunft von *Claims*). Gegen **C3** trägt TE1 **nicht** für KI-Content: 0 von 41 sind A/B, die Umsatzträger sind human-face oder faceless-F mit (vermutlich) menschlicher Stimme. TE1 widerlegt C3 nur, wenn man faceless (F) mit „KI-Content“ gleichsetzt.
- **Korrigierte Zahlen:** GMV je Top-10-Eintrag 0,85–4,87 Mio. USD/Monat; Provision (Estimated) ≈ 85.000–974.000 USD, Median-Eintrag 121.500–243.000 USD. Kategorie: Top-Earner-Datensatz, human-face + faceless F, **keine A/B**.

### Verifikation TE3
Stand 2026-09-25. **Urteil: PARTIALLY** (Richtung hält, Einordnung gegen C3 und die Views-pro-Video-Aussage zu stark).
- **Quellen neu geöffnet:** Net Influencer Juni 2026 bestätigt @hannahbentley #6, 1,32 Mio. USD, 27.150 Artikel, AUP 48,58 USD, 67.900 Follower, 47,52 Mio. Content-Views (Claimed, Kalodata-Analytics). Das ist **GMV**, keine Provision, vor Retouren, eventuell inklusive LIVE.
- **TikTok-Nachprüfung:** Profil existiert, 74.500 Follower, 2.704 Videos, Konto seit 2019-10, ttSeller false, Bio „Cozy Home Finds“ plus Gmail-Adresse (Verified). Die 10 neuesten Videos (2026-09-21 bis 09-24, also ca. 3/Tag) sind alle Shop-Videos ohne AI-Label. `tt_media.py` auf 7689222778175622414 zeigt nur Hände und einen Diffusor, dazu Voice-over. Das ASR ist natürlich gesprochen („Seth Rogen, I love you for making this…“), `IsAigc = false`. Damit ist die **Kategorie F bestätigt**. Eine KI-Nutzung ist nicht erkennbar.
- **Arithmetik:** Die Summe beträgt 13,42 Mio. USD über 9 Monate, im Schnitt also 1,491 Mio. USD. Das ergibt 149.000–298.000 USD bei 10–20 % (Estimated, korrekt). Gepoolter Wert: 8,69 Mio. USD GMV auf 356,2 Mio. Views = 24,4 USD je 1.000 Views (korrekt). Nach ca. 10 % Retouren liegt die Provision bei **≈ 134.000–298.000 USD/Monat** (Estimated). Die Provisionssätze der Marken (Mellow, Shark, Ninja) sind nicht öffentlich.
- **Neue Einschränkungen:**
  - (1) **8 von 10 neuesten Videos haben `isAd = true`**, ebenso das Feb-Video mit 587.000 Views. Ein Teil der Views bzw. des GMV ist also wahrscheinlich bezahlte Reichweite (Spark Ads oder Branded Content), die Marken mitfinanzieren. Views pro Video sind damit kein reiner organischer Hebel.
  - (2) Die aktuellen Plays der 10 neuesten Videos liegen bei 741–23.000, Median ≈ 3.400. Die „≈ 500.000 Views/Video“ sind ein von wenigen Hits bzw. Ads getriebener Durchschnitt, kein typischer Wert.
  - (3) Im August 2026 war der Account nicht in den Top 10. Die neuesten Plays deuten auf einen Rückgang hin (Ursache offen).
- **Bezug zu den Claims:**
  - **C3:** Kein Gegenbeweis. Der Account ist menschlich produziertes Faceless-Material (F), kein KI-Content. Er widerlegt C3 nur, wenn man F mit KI gleichsetzt.
  - **C6/C7:** Der Einwand hält in der Richtung: Hohe Provisionen sind mit ca. 60–90 Videos/Monat möglich. Voraussetzung sind aber ein 7 Jahre alter Account, Markenbeziehungen und bezahlte Reichweite. Die These zeigt keine allgemeine Machbarkeit (Survivorship).
- **Stärke:** medium für die GMV-Existenz, low für die Übertragbarkeit.

### Verifikation TE2

Stand 2026-09-25, unabhängige Nachprüfung. **Urteil: PARTIALLY.** Die Richtung stimmt, die Größenordnung hängt aber stark von der Stichprobe ab, und die Kategorie überdehnt C3.

- **Arithmetik (bestätigt):** Das kumulierte GMV wurde aus Tabelle 1 neu summiert: 100 Einträge, 41 Creator, die Werte je Creator stimmen. Human-face ergibt 65,0 Mio. USD, 2×F 22,7 Mio., 6× gemischt 33,6 Mio., 2×G 3,24 Mio. Zusammen sind das 124,56 Mio. USD; faceless/hybrid macht 59,56 Mio. = 47,8 % aus. In den Top 20 sind es 9 von 20 mit 58,47 von 119,41 Mio. = 49,0 %.
- **Quelle (Stichprobe):** Der Net-Influencer-Artikel für März 2026 wurde neu geladen. @be.lush hat 3,97 Mio., @dealswithty 2,15 Mio., @hannahbentley 1,53 Mio. und @cakedfinds 1,15 Mio. USD. Das deckt sich mit der Tabelle. Die Kennzahl ist GMV (Kalodata, Claimed) und keine Provision; das hat TE2 korrekt angegeben.
- **TikTok-Nachprüfung (Verified):** `aigcLabelType = "2"` ist bei @kevin.finds 7688905577250032926 und bei @airgeeksrc 7688760943236500750 bestätigt. Das Sheet von @kevin.finds zeigt einen generierten MacBook-Clip mit verformtem Apple-Logo, also G. Die Sheets von @hannahbentley (7688418962152901901 und das neu gezogene 7689244856186588430) zeigen nur Hände und Handtücher, also F. @cakedfinds zeigt nur Hände und Karton (F), der @be.lush-Staubsaugervergleich nur Produkt und Füße (F). Bei allen ist `IsAigc` false.
- **Stichprobenfehler (wichtig):** Ein neu gezogenes Shop-Video von @trending_ttok (7689301513776270606, Bissell CrossWave) zeigt **kein Gesicht**, nur Beine und Produkt. Das ist dasselbe Muster, das bei @be.lush als F gezählt wurde. @trending_ttok (Platz 1, 17,99 Mio.) wurde aber als „rein human-face“ verbucht. Nach der eigenen Regel von TE2 („mind. 1 geprüftes Video ohne Gesicht = gemischt“) wären es **11/24 und 77,6/124,6 Mio. = 62 %**. Der Anteil „gemischt“ steigt also mit jeder zusätzlichen Stichprobe. Er misst, ob ein Account das Format *irgendwann* nutzt, nicht welcher GMV-Anteil *aus* faceless Content stammt. Zwei weitere neue Stichproben blieben human-face: @dealswithty 7689241791031266591 und das Split-Sketch von @trending_ttok 7689292917470481677.
- **Belastbarer Kern:** 2/24 Accounts sind **überwiegend faceless (F)**, das sind 22,7 Mio. = **18,2 %** des GMV. Nachweislich **KI-gestützt (G, AI-Label)** sind 2/24 mit 3,2 Mio. = **2,6 %**, wobei die gelabelten Clips nur rund 2.000 bis 2.800 Plays haben. Für D (TTS) gibt es nur einen Verdacht bei @cakedfinds (Claimed, Reddit). A/B kommen nicht vor; das ist bestätigt.
- **Kategorie und Bezug zu C3:** F bedeutet menschlich produziertes faceless Material und ist kein KI-Content. Gegen C3 („mit KI-Content selten“) spricht deshalb nur der G/D-Anteil, und der ist klein. Die 42 % bzw. 48 % belegen, dass faceless Formate *KI-tauglich* sind. Dass KI-Content dauerhaft verdient, belegen sie nicht. Bias: Survivorship (Top 0,001 %), Kalodata-GMV vor Retouren, möglicher LIVE- und Seller-Anteil.
- **Korrigierte Formulierung:** „Unter 24 US-Top-Earnern (124,6 Mio. USD GMV) sind 2 überwiegend faceless (18 % GMV). Mindestens 9 weitere (6 gemischt F, 2 G, dazu @trending_ttok laut Nachprüfung) nutzen gelegentlich faceless Formate; die Zahl hängt von der Stichprobe ab. Nur 2 (2,6 % GMV) nutzen nachweislich KI-Clips, und die haben kaum Reichweite.“
