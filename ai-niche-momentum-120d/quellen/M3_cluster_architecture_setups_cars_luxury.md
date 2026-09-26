# M3 – AI Architecture, Interior, Homes, Setups, Cars, Luxury, Travel, Nature, Gadgets, Sneaker

Prüfdatum: 2026-09-26 · Betrachtungsfenster: ca. 28.05.–26.09.2026 (30/60/90/120 Tage) · Rohdaten: `raw_accounts_M3.csv` (69 Zeilen)

## 1. Methodik & Grenzen

**Vorgehen**
1. 25 WebSearch-Abfragen (Kontingent ausgeschöpft), meist auf `instagram.com` eingeschränkt. Follower- und Post-Zahlen stammen aus den Such-Snippets. Wann der Suchindex sie erfasst hat, ist unbekannt, deshalb stehen sie als `THIRD-PARTY OBSERVED` ohne Stichtag in der CSV.
2. NexLev `search_shorts_niche_finder_channels` (isAiChannel=true, firstUploadAfter=2025-10-01) in 8 semantischen Abfragen: Interior/Build, Cars/Luxus, Gaming-Rooms, Travel/Nature, Gadgets/Sneaker, Luxus-Mansion, Garten/Pool/Organisation, Car-Transformation. Damit wurden junge **Cross-Plattform-Zwillinge** (YouTube Shorts) mit datierten Startpunkten gefunden. Für 6 Top-Shorts wurden Veröffentlichungsdatum und Views zusätzlich über `youtube_video_details` geprüft (VERIFIED).
3. Öffentliche TikTok-Profile (Follower, Videos, Erstellungsdatum, Bio-Link), YouTube-About-Seiten, Linktree, Amazon-Storefronts (`amazon.com/shop/<handle>`), Creator-Website vukovic.ink und die Parametric-Architecture-Liste (08/2025).
4. NexLev `watch_instagram_video_and_ask`: 4 Reels analysiert (danach war das gemeinsame Tageslimit 15/15 erreicht). Das Tool nennt **keine Handles**, taugte also nur zur Format- und AI-Prüfung, nicht zum Finden neuer Accounts.

**Harte Grenzen (keine Umgehung versucht)**
- Instagram-Profil- und Reel-Seiten liefern ohne Login keine Daten (HTML ohne Meta/JSON, WebFetch HTTP 429).
- Social Blade (403), HypeAuditor, Heepsy, Starngage, Feedspot, alici.ai (Cloudflare-Challenge) und speeedy.ai (503) waren nicht erreichbar.
- **Es gibt daher keinen einzigen datierten Instagram-Follower-Snapshot.** Alle Felder `follower_vor_30/60/90/120d` sind für Instagram `UNKNOWN`. Wachstum wurde nirgends aus aktuellen Zahlen hochgerechnet.
- Wachstumsaussagen sind nur für YouTube- und TikTok-Zwillinge möglich, und zwar über das Kanal-Erstellungsdatum bzw. den ersten Upload. Beispiel: Ein Kanal, der am 01.07.2026 erstellt wurde, hatte vor 90 Tagen 0 Abonnenten.
- **Ziel von 55 Instagram-AI-Accounts nicht erreicht:** 43 Instagram-Accounts sind AI VERIFIED/LIKELY (40/3), dazu kommen 18 AI-Zwillinge auf YouTube/TikTok (zusammen 61 AI-Accounts) und 8 Instagram-Kontext-Accounts mit AI-Status UNKNOWN. Die meisten Instagram-Treffer sind Legacy-, App- oder Mini-Accounts. Junge, schnell wachsende Instagram-Accounts ließen sich über den Suchindex kaum finden.

## 2. Cluster-Befunde je Unter-Nische

| Unter-Nische | Stärkster belegter Account (Plattform) | Momentum-Beleg | Einschätzung |
|---|---|---|---|
| **AI House-Build-Timelapse / Tiny Houses / Cabins** | Bau Rausch (YT) / @not_your_basic_build (IG) / @vukovic_vlad (TT) | YT: erster Upload 13.04.2026, 621K Abos, 53 Videos, Top-Short 127,8 Mio Views vom **12.07.2026** mit AI-Disclaimer. TT: 1,47 Mio Follower | **Stärkster Cluster.** Creator bezeichnet sich als „first in the AI Timelapse Building niche“ und verkauft Guides. Weitere: CreativeAIConcept (Schulbus zum Traumhaus, 12M), BuildFlow (Erdbeer-Tiny-House, 24M), Granny Builder (TikTok-Account 27.03.2026, 173.852 Follower) |
| **AI Nature / „unreal places“ / Dream Destinations** | Mistora (YT, IG @mistoraearth) | 629K Abos, Median 5,3 Mio, Top-Short 325 Mio Views (07.01.2026) | Größte Einzel-Reichweiten. **Copycat-Welle belegt:** Aura Earth (Kanal 22.05.2026, identischer Beschreibungstext, 123K Abos, 84,7 Mio am 02.07.2026), Avena Earth (Kanal 01.07.2026, 86K), Ecliptic World (erster Upload 14.08.2026, 14,9K, Top 11M) |
| **AI Interior / Dream Rooms / Room Makeover** | Dreamy Interior (YT) | erster Upload 18.03.2026, 316K Abos, Top-Short 32,7 Mio (11.07.2026) | Stark auf YouTube. Instagram-Seite nicht zuordenbar. Sub-Format „Epoxy-/Aquarium-Boden“: Aura Frame (101M), Momentum Builds (74M), Aesthetic Redesign (50M bei 18 Videos) |
| **AI Sneaker / Product-Konzepte** | Panda Paw (YT) | 130K Abos, Top-Short 155,6 Mio (03.01.2026), Keyword „Sora AI Video“ | Sehr hohe Views bei geringer Abo-Konversion. Auf IG nur kleinere, ältere Accounts (@ai.shoe.factory 56K, @artificial.sneakers 19K, @aisneakerconcepts 3K/34 Posts) |
| **AI Architecture / Concept Buildings** | @midjourney.architecture (IG, 161–172K) | keine Wachstumsdaten | Legacy-Nische aus der Midjourney-Bildära 2022–2024 mit vielen Architekten-Accounts (Parametric-Liste). Kein junger Breakout gefunden |
| **AI Luxury (Mansions/Yachten)** | @trillionaireestates (IG 362K, TT 105.699) | TikTok-Bio „200k?“, keine Datierung | Legacy-Mischaccount (AI + echte Objekte), Amazon-Storefront. Kleine Copycats (@mansions.ai 63, @theaimansion 37). Absurdes Luxusformat: Rogue Clip „Million Dollar Jelly Bed“ (YT 253K) |
| **AI Cars / Concept / Transformation** | @cartuner.ai (IG 47K, 5.686 Posts) | keine | Auf IG vor allem Bild-Legacy. Car-Transform-Effekte laufen als Higgsfield-Preset/Tutorial (@higgsfield.creators 226K), was schnelle Sättigung bedeutet. storycar.barnfind (YT 147K, ~14 Uploads/Woche) |
| **AI Garden / Backyard / Pool** | Granny Builder (Zen-Garten-Topiary 35,4M) | siehe oben | Auf IG nur Apps (@rescapeai 123) und reale DIY-Accounts. **Instagram-Lücke** |
| **AI Home Organization** | — | — | Kein AI-Account gefunden, echte Datenlücke |
| **AI Desk/Gaming Setups** | @topdailysetups (IG 67K) | keine | 3D-Renderings, **nicht als AI verifiziert**, Amazon-Storefront vorhanden |
| **AI Tech Gadgets / Concept Devices** | — | — | IG-Gadget-Seiten (@nextgen_gadget 899K, @futureideagadget 218K, @gadget_with_ai 320K) ohne AI-Beleg, daher UNKNOWN |
| **AI Travel / Hotels / Capsule Hotels** | — | — | Keine AI-Hotel-Creator gefunden. Treffer waren echte Hotels oder „sieht aus wie AI, ist aber echt“-Posts |

## 3. Emerging Outliers (Views weit über Follower/Abos)

1. **Ecliptic World** (YT): 14,9K Abos, Top-Short 11 Mio, erster Upload 14.08.2026. Choose-one-Format „Which place was your favorite 1/2/3?“.
2. **Aesthetic Redesign** (YT): 45,2K Abos, 18 Videos, Top 50 Mio (Epoxy-Treppe).
3. **CreativeAIConcept** (YT): 40,9K Abos, Top 12 Mio, Median nur 14K (hit-getrieben).
4. **Avena Earth** (YT): 86K Abos, Kanal jünger als 90 Tage, zwei Shorts mit 18–19 Mio.
5. **BuildFlow** (YT): 83K Abos, Top 24 Mio.
6. **Isla | Interior Designer** (YT): 50,9K Abos, Median 585K, App-Promo.
7. **Aura Earth** (YT): 84,7 Mio auf einem einzigen Short bei 123K Abos, Kanal jünger als 6 Monate.

Auf Instagram konnte **kein Outlier numerisch belegt werden**, weil Reel-Views ohne Login nicht öffentlich sind.

## 4. Formate & Hooks

- **Bau-Timelapse vom Aushub bis zur Luxusvilla** (IG-Reel DSJPMatjHuw: Bagger und Fundament in den ersten 3 Sekunden, dann „wachsende“ Holzrahmen; Reel DUwGYnbjsBM: **sichtbares Veo-Wasserzeichen**, Sonnenuntergangs-Aushub als Hook). Beide AI-generiert, Handles nicht ermittelbar.
- **Unmögliches Bauprojekt:** schwimmende Hütte auf Plastikflaschen, Erdbeer-Haus, Schulbus zur Villa, Flugzeug zur Dschungelvilla. Die Unmöglichkeit selbst ist der Hook. Bau Rausch setzt dabei auf lange Keyword-Beschreibungen plus AI-Disclaimer.
- **Charakter-Serie:** „90-jährige Oma baut Luxusbunker“ (Granny Builder). Figur plus Bau-Satisfaction.
- **Choose-one / Voting:** „Which place did you like the most 1 or 2 or 3“ (Avena Earth, Ecliptic World), „Which bedroom are you choosing?“ (IG-Reel DO63dUEgEh_). Kommentar-Köder.
- **„Places that don’t feel real“:** 16-Sekunden-Natur-Loops ohne Beschreibung, nur Hashtags (Mistora, Aura Earth).
- **„AI-designed [Produkt] just changed … forever“:** 9-Sekunden-Konzeptclip (Panda Paw).
- **Car-Edit mit AI-Dreamhouse** (IG-Reel DPeDdKujB9L: „LET HIM COOK“-Text, Bugatti im Schnee, futuristisches AI-Haus, erkennbare Morphing-Artefakte).

## 5. Copycats / Sättigung

- **Textklon:** Aura Earth übernimmt den Mistora-Beschreibungstext wörtlich („Join me as I capture hidden wonders…“). TikTok-Klon @mistora.earth wurde am 26.08.2026 erstellt.
- **Epoxy-Böden:** mindestens 5 Kanäle mit demselben Motiv (Aura Frame, Momentum Builds, Aesthetic Redesign, The Bitter Trade, Drin Apex).
- **Jelly Bed:** Rogue Clip und @RuangPensiun1 mit demselben Motiv.
- **Tool-getriebene Sättigung:** Higgsfield und Kling bewerben Car-Transform-Effekte als Presets. Guides („AI Timelapse Builder“, Medium- und Tool-Anleitungen, timelapsestudio.io, revid.ai) senken die Einstiegshürde. Die AI-Timelapse-Nische ist damit **im Übergang zur Sättigung**.
- Auf Instagram gibt es im Architektur-, Mansion- und Car-Art-Segment viele Mini-Copycats mit unter 150 Followern (@mansions.ai, @theaimansion, @house_designs_by_ai, @carart_ai).

## 6. Sichtbare Monetarisierung (Affiliate)

| Account | Monetarisierung | Beleg |
|---|---|---|
| @topdailysetups | **Amazon-Storefront** („The products in our posts“, „Earns revenue“) + 3D-Room-Design-Service | amazon.com/shop/topdailysetups |
| @trillionaireestates | **Amazon-Storefront** (4 Idea Lists) | amazon.com/shop/trillionaireestates |
| @thedreamsetup / @interiorraura / @nextgen_gadget (keine AI) | Amazon-Storefronts (5 / 16 / 5 Posts) | amazon.com/shop/… |
| Vukovic (@not_your_basic_build, Bau Rausch, @vukovic_vlad) | **Info-Produkte** statt Affiliate: Guides 9,99–24,99 €, Mentoring 199,99 € | vukovic.ink |
| Isla / RenoMuse | App-Install-Promotion | YouTube-Beschreibung |
| BuildFlow | „YouTube automation“-Coaching | YouTube-Beschreibung |
| @intelligent.designer.ai | Kurs-Funnel („comment INFO“) | IG-Reel-Caption |
| App-Brands (@homeaiapp, @arch.interior.ai, @reroom_ai …) | eigene App | Bios |

**Befund:** In den reinen AI-Nischen (Timelapse, Nature, Konzeptprodukte) ist **kein Shop-the-Look-Affiliate sichtbar**. Die Motive sind fiktiv, es gibt also nichts zu kaufen. Monetarisiert wird über Guides, Coaching und App-Promo. Amazon-Affiliate findet sich vor allem bei **Setup- und Interior-Theme-Pages mit realen oder 3D-Produkten**. Ob Zuschauer in Kommentaren nach Produkten fragen, konnte **nicht geprüft werden**: Kommentare sind ohne Login nicht sichtbar, und das Reel-Analyse-Tool liest keine Kommentare.

## 7. Datenlücken

- Instagram-Follower-Historie (30/60/90/120 Tage): durchgehend UNKNOWN.
- Instagram-Reel-Views, Median und Top-5: UNKNOWN.
- Instagram-Handles der YouTube-Breakouts (Dreamy Interior, Aura Frame, Granny Builder, Panda Paw u. a.) nicht auffindbar. Nur Mistora (→ @mistoraearth) und Torque vibe (→ @torquevibe_official) sind im YouTube-About verlinkt.
- Nicht selbst verifiziert: AI-Status von 14 YouTube-Zwillingen. LIKELY stützt sich dort auf den NexLev-Klassifikator plus physikalisch unmögliche Motive. Die Kanäle mit Epoxy-Böden könnten teilweise echtes Material nutzen.
- Home Organization, Capsule Hotel und AI Gadgets: kein belastbarer AI-Account gefunden.
- Offene nächste Schritte: IG-Snapshots mit Login-freiem Analytics-Zugang (z. B. bezahltes Social-Blade-API), Instagram-Suche nach Handles der YouTube-Breakouts, Reel-Analyse nach Reset des NexLev-Limits.

## 8. Quellenliste (Auswahl)

- Instagram-Profile/Reels (Suchindex): instagram.com/midjourney.architecture, /midjourney.architect, /trillionaireestates/reel/Czek4OzJB7H, /trillionaireestates/p/C4axwbCO33U, /not_your_basic_build, /bau_rausch_, /homeaiapp, /arch.interior.ai, /intelligent.designer.ai/reel/DCRadsYyqAf, /cartuner.ai, /automotive.ai, /carart_ai, /ai.shoe.factory, /artificial.sneakers, /aisneakerconcepts, /yumayanagisawa/p/Cr0tUViNYK3, /topdailysetups, /3dgamingsetups, /higgsfield.creators, Reels DSJPMatjHuw, DUwGYnbjsBM, DPeDdKujB9L, DWasA13ADMN, DO63dUEgEh_
- https://parametric-architecture.com/top-10-ai-design-pages-instagram-2025/ (06.08.2025)
- https://vukovic.ink/ · https://www.tiktok.com/@vukovic_vlad · https://www.tiktok.com/@grannybuilder · https://www.tiktok.com/@trillionaireestates · https://www.tiktok.com/@storycar.barnfind
- https://linktr.ee/trillionaireestates · https://www.amazon.com/shop/topdailysetups · https://www.amazon.com/shop/trillionaireestates · https://www.amazon.com/shop/thedreamsetup · https://www.amazon.com/shop/interiorraura · https://www.amazon.com/shop/nextgen_gadget
- YouTube: @BauRausch (Video BMlCqeKWe5Y), @DreamyInterior (ABCQ2EDzW7U), @MistoraEarth (QLxUsSn9NGQ), @AurasEarth (8vU6dgSep2Y), @Panda-Paw (d9FRo5MkHco), @grannybuilder (DVsH8-zd-xo), @AvenaEarth, @EclipticWorld, @AuraaFrame, @Momentum.Builds, @Aesthetic_Redesign, @CreativeAIConcept, @BuildFlow-11, @RogueClip-m9q, @storycar.barnfind, @IslaInteriorDesigner, @LuxBuild_Timelapse, @torqueCAREDITOR
- NexLev search_shorts_niche_finder_channels / youtube_channel_about / youtube_video_details (Abruf 2026-09-26)
- Trend-Kontext: https://www.revid.ai/category/home-renovation · https://timelapsestudio.io/ · https://shahmeerajk.com/make-free-ai-home-renovation-videos-using-timelapse-prompts/
