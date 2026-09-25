# 09 – Monetarisierung: Möbel-Affiliate-Konkurrenz, Einnahmen der Konkurrenz und eigene Roadmap (Teil 19 + 20)

**Stand:** 25.09.2026 · **Für:** neuen internationalen (englischsprachigen) Instagram-Account mit überwiegend KI-generierten Reels, Betreiber mit Sitz in Deutschland · **Positionierung** (bindend, aus dem [Strategy Brief](data/processed/strategy_brief.md)): KI-Architektur-Studio für *„Homes that shouldn't exist (yet)"* mit Originalentwürfen, **keine** Repost-Theme-Page.

**Dateien zu diesem Kapitel**

| Datei | Inhalt |
|---|---|
| [scripts/monetization_stats.py](scripts/monetization_stats.py) | Reproduziert alle Zählungen und Kontraste dieses Kapitels aus den Rohdaten |
| [data/processed/stats/monetization_accounts.csv](data/processed/stats/monetization_accounts.csv) | 72 tief profilierte Accounts: strikte Monetarisierungs-Flags, Follower, Median-`adj_factor` |
| [data/processed/stats/monetization_summary.csv](data/processed/stats/monetization_summary.csv) | Anzahl Accounts je Einnahmequelle: gesamt, nach Content-Modus, nach Account-Typ |
| [data/processed/stats/monetization_contrasts.csv](data/processed/stats/monetization_contrasts.csv) | Explorative Kontraste: Kommentar-Keyword-CTA, Link-CTA, Kaufbarkeit bei KI-Reels, Monetarisierungsklasse |
| [02_competitor_database.csv](02_competitor_database.csv) | 111 Accounts inkl. `has_*`-Flags (Überzählung beachten, siehe 1.2) |
| `data/raw/accounts/profile_<handle>.json` | Rohbelege je Account: `link_in_bio.offers`, `monetization_evidence`, `brand_deals_seen` |

**Kennzeichnung:** `[VERIFIED]` = in der Quelle gesehen (bei Profilen: öffentliche Linktree-, Threads-, Website- oder Embed-Seite). `[ESTIMATED]` = eigene Ableitung oder KI-gestützte Codierung. `[THIRD-PARTY ESTIMATE]` = Zahl eines Dritten, auch Selbstauskünfte. `[UNKNOWN]` = nicht belegbar. **S** = Setzung bzw. Annahme ohne externe Evidenz (nur in Rechenbeispielen). Follower und Views von öffentlichen Seiten sind VERIFIED (gerundet, Stand 25.09.2026). CTA-Typ, Kaufbarkeit (`shoppability`), Realismus und Account-Typ sind KI-gestützte Codes, also ESTIMATED. Ihre Reliabilität (Cohen's κ, n=36) liegt bei 0,96 für den CTA-Typ, 0,63 für die Kaufbarkeit und 0,79 für den Account-Typ ([Digest](data/processed/analysis_digest.md), Abschnitt „Coding reliability").

> **Keine Rechtsberatung.** Vor der ersten bezahlten Kooperation und vor dem ersten Affiliate-Link sollte ein Anwalt Kennzeichnung, KI-VO Art. 50, UWG/MStV und Markenfragen prüfen ([q07](quellen/q07_legal_ai_risk.md)).

---

## 0. Kurzfassung

1. **Möbel-Affiliate ist bei den KI-Konkurrenten ein Nebenschauplatz.** 13 der 72 tief profilierten Accounts zeigen belegte Affiliate-Wege: 7 davon Amazon, 3 mit Amazon-Storefront, 2 LTK, 0 ShopMy. Unter den 37 KI-Accounts sind es 6, meist Low-Ticket-Produkte (Amazon-Garten- und Deko-Artikel) oder Tool-Referral-Links. Einzige Ausnahme mit Möbelmarken-Codes ist die Repost-Seite @deirdres_design. Affiliate-Werkzeuge wie Storefront, Listen, Codes und LTK nutzen vor allem die **„Finds"- und Home-Creator mit echten Wohnungen**: 6 von 8 Lifestyle-Accounts zeigen Affiliate. `[VERIFIED Einzelbelege; Zählung ESTIMATED]`
2. **Der häufigste Geldweg ist B2B.** 30 der 72 Accounts verkaufen Dienstleistungen, bei den Designer-Studios 12 von 14. Das Muster: KI- oder 3D-Visuals dienen als Lead-Funnel für Aufträge, etwa bei @aiforarchitects (1M): *„For private commissions and inquiries"*. Preise und Auftragsvolumen sind nirgends öffentlich. `[VERIFIED Angebote / UNKNOWN Umsätze]`
3. **Theme-Pages zeigen am seltensten einen Geldweg.** Bei 11 von 17 ist weder ein Geldweg noch ein Kontakt sichtbar. Gleichzeitig schneiden sie in der Reichweite am schwächsten ab (`adj_factor` 0,74, n=503, gegenüber AI-Creators 1,09, n=276; Kontrast 0,68×, p<0,001). Das stützt die Studio-Positionierung. Es ist aber eine Korrelation und kein Kausalbeleg.
4. **Commerce ohne Werbe-Anmutung funktioniert über fünf beobachtete Muster:** (a) Kommentar-Keyword → DM mit „kuratierter Kollektion", (b) Transformation → „shop the key pieces", (c) Finds-Listen nach Raum, (d) Commerce außerhalb des Posts (Bio, Blog, Website), (e) Tool-als-Inhalt. Im Reel-Datensatz gehen Keyword-CTAs mit **6,6× mehr Kommentaren pro View** einher (n=144 vs. 1.071, p<0,001), bei KI-Reels mit 10,0× (n=31 vs. 322). Bei der **Reichweite gibt es keinen messbaren Unterschied** (`adj_factor` 0,86 vs. 0,98, p=0,87).
5. **Kaufbarkeit geht unter den Top-Reels mit keinem nachweisbaren Reichweitenverlust einher.** Über alle Reels liegt „high" bei 0,98 (n=530) und „low" bei 0,97 (n=1.217), p=0,91 (Mann-Whitney; Kruskal über drei Stufen p=0,83). Bei KI-Reels liegt „high" bei 1,13 (n=85) und „low" bei 0,93 (n=397), p=0,78 (n. s.). Fantasy-/Impossible-Reels sind dagegen zu **0 % hoch kaufbar** (n=62). An dieser Stelle setzt der Hybrid-Test *„Impossible places, possible furniture"* an (5.3).
6. **Die Programmbedingungen sind für Möbel dünn und für KI-Tools vergleichsweise gut.** Möbel: Amazon Home 3 % bei 24-h-Fenster, **keine Provision für Käufe über geboostete oder bezahlte Anzeigen mit Amazon-Link** (seit 14.04.2026); Wayfair „bis 7 %" bei 7 Tagen (Drittangabe); LTK Ø 10–25 % laut Selbstauskunft, ab 5K Followern. KI-Tools: Runway zahlt 15 USD pro neuem Abo ohne Cap und für alle Account-Größen, Higgsfield bis 25 % für bis zu 12 Monate, Higgsfield Earn bis 2.500 USD pro Video, Planner 5D 25–50 % bei 90 Tagen Cookie. `[VERIFIED, außer wo anders angegeben]`
7. **Roadmap, sortiert nach Evidenz:** (1) KI-Tool-Affiliate und -Sponsoring ab Tag 1, (2) B2B-Visualisierung, sobald ein Portfolio steht, (3) digitale Produkte nur nach einem Nachfragetest, (4) Möbel-Affiliate nur über Choice- und Transformationsformate und nach dem Hybrid-Test, (5) Real Estate nur als B2B mit Compliance-Prüfung, (6) Newsletter als eigener Kanal ab Start, bezahlte Platzierungen darin erst ab 50K.
8. **Unit Economics (ANNAHMEN, keine Prognose):** Möbel-Affiliate bringt etwa 0,02–3,08 USD pro 1.000 Views (Basis 0,65), Tool-Affiliate etwa 0,08–3,00 USD (Basis 0,60). Sponsoring-Benchmarks liegen bei 9–20 USD pro 1.000 Views, gelten aber nur für die gesponserten Reels. **Ein B2B-Auftrag über 1.000 USD (S) entspricht rund 1,5 Mio. Views Möbel-Affiliate im Basisszenario.** Die größte Unbekannte ist die Klickrate; sie wird ab Tag 1 gemessen ([15_kpi_framework.md](15_kpi_framework.md), 3.8).
9. **Recht:** Doppelt kennzeichnen („Werbung | Ad" plus Label „Paid partnership"). Affiliate-Links mit `*` und Erläuterung direkt am Link, dazu der Amazon-Pflichtsatz. KI-Label sichtbar ab der ersten Sekunde: Nach KI-VO Art. 50(4) gilt das seit 02.08.2026, und wer mit dem Account regelmäßig Geld verdient, gilt als Deployer. Keine Preis- oder Ortsbehauptungen für fiktive Objekte, keine Dupes von Designklassikern. Bei VAE-Immobilien gilt die Advertiser-Permit-Pflicht.
10. **Für keinen KI-Interior-Account ist ein Einkommen verifiziert.** Alle Einkommenszahlen in diesem Kapitel sind Drittangaben (THIRD-PARTY ESTIMATE) oder ausdrücklich als Annahme markiert.

---

## 1. Datenbasis, Definitionen, Grenzen

### 1.1 Was ausgewertet wurde

| Quelle | Umfang | Was sie liefert | Status |
|---|---|---|---|
| Tiefe Profile `data/raw/accounts/profile_*.json` | 72 Accounts (37 KI, 16 real, 19 3D/gemischt/unklar) | Bio-Link-Angebote, Monetarisierungsbelege (typisiert, je mit Status), gesehene Marken und Partner, CTA-Muster | VERIFIED je Beleg-URL |
| [02_competitor_database.csv](02_competitor_database.csv) | 111 Accounts, 72 davon tief profiliert | Follower, Views, `has_*`-Flags | VERIFIED Follower (gerundet); Flags siehe 1.2 |
| Reel-Datensatz ([Digest](data/processed/analysis_digest.md), `reels_master.pkl`) | 2.498 Reels von 239 Topic-Seiten, 2.393 codiert | CTA-Typ, Kaufbarkeit, Realismus, `adj_factor`, Kommentare/View | Views VERIFIED; Codes ESTIMATED |
| Quellennotizen | [q01](quellen/q01_instagram_platform_rules.md), [q02](quellen/q02_furniture_affiliate_commerce.md), [q03](quellen/q03_sponsors_brand_deals.md), [q04](quellen/q04_interior_trends_demand.md), [q06](quellen/q06_ai_theme_page_case_studies.md), [q07](quellen/q07_legal_ai_risk.md), [q08](quellen/q08_cross_platform_signals.md), [q09](quellen/q09_reels_format_benchmarks.md) | Programmkonditionen, Preis-Benchmarks, Fallstudien, Recht | Tags wie in den Notizen |

### 1.2 Strikte Flags statt `has_*`-Spalten

Die `has_*`-Spalten in `02_competitor_database.csv` zählen zu viel. `has_brand_deals` wird auch dann gesetzt, wenn ein Belegtyp das Wort „brand" enthält, also schon bei einem bloßen `brand_contact`. `has_affiliate` greift auf Freitexttreffer wie „amazon" oder „wayfair", auch in Sätzen wie „keine Amazon-Storefront gesehen". Dieses Kapitel verwendet deshalb **strikte Flags**, die nur aus typisierten Belegen entstehen ([scripts/monetization_stats.py](scripts/monetization_stats.py)):

| Kennzahl (72 Profile) | `has_*`-Spalte | strikt | Unterschied erklärt durch |
|---|---|---|---|
| Affiliate | 21 | **13** | Freitexttreffer ohne Affiliate-Beleg (z. B. Agentur-, Makler- und Hotelseiten) |
| Marken-Deals | 39 | **20** konkret benannte Partner; **8** mit typisiertem Sponsoring-Beleg | `brand_contact` wird als Deal mitgezählt |

### 1.3 Grenzen, die jede Aussage einschränken

- **Auswahlbias:** Die profilierten Accounts stammen von Topic-Seiten, die **Top-Reels** zeigen, und aus einer Shortlist. Es sind also erfolgreiche Accounts. Gescheiterte Commerce-Accounts fehlen.
- **Sichtbarkeit:** Erfasst ist nur, was öffentlich sichtbar war. Die Instagram-Bios selbst wurden meist **nicht** gelesen, weil das WebSearch-Budget der Profil-Session erschöpft war (steht in den `notes` der JSONs). Stattdessen kamen die Daten von Threads, Linktree, Websites und Embed-Seiten. Paid-Partnership-Labels wurden nur stichprobenartig geprüft. **„Nicht beobachtet" heißt deshalb nicht „nicht vorhanden"** `[UNKNOWN]`.
- **Keine Umsätze:** Kein Profil nennt Einnahmen. Einkommenszahlen gibt es nur als Drittangaben aus den Quellennotizen (3.4).
- **Reel-Kontraste:** Auch dort gilt, dass Topic-Seiten nur Reels zeigen, die es nach oben geschafft haben. „Keine Reichweiten-Einbuße bei Commerce" bedeutet also nur: **unter den sichtbaren Top-Reels ist keine Einbuße erkennbar.** Wie viele Commerce-Reels gar nicht erst oben landen, lässt sich damit nicht messen.

---

## 2. Teil 19 – Konkurrenz beim Möbel-Affiliate

### 2.1 Wer verlinkt was? (Teil 19)

**Tabelle 19-A: Commerce-Kanäle unter den 72 tief profilierten Accounts**

| Kanal | alle (n=72) | KI (n=37) | real (n=16) | 3D/gemischt/unklar (n=19) | Accounts (Auswahl) | Status |
|---|---|---|---|---|---|---|
| Affiliate gesamt | 13 | 6 | 5 | 2 | siehe Tabelle 19-B | VERIFIED je Beleg |
| Amazon (Storefront, Listen, amzn.to, eigene Website) | 7 | 4 | 3 | 0 | deirdres_design, digitaldesign.lab, divaa.finds, ell.glamhome, karissa.brighton, luxquisit, neuraltransform | VERIFIED (Tag-Status bei digitaldesign.lab ungeprüft) |
| davon Amazon-Storefront | 3 | 1 | 2 | 0 | deirdres_design (amazon.com/shop), divaa.finds, ell.glamhome (amazon.de/shop) | VERIFIED (Storefront-Seiten teils HTTP 503) |
| LTK | 2 | 0 | 2 | 0 | em_henderson, eloisepreen | VERIFIED |
| ShopMy | 0 | 0 | 0 | 0 | – | nicht beobachtet `[UNKNOWN]` |
| Wayfair (Links, Kollektion, Sponsor) | 2 | 0 | 1 | 1 | roomify.design (Kollektion per DM, Affiliate-Status unbelegt), em_henderson (gesponserter Blogpost) | VERIFIED; Provision bei roomify UNKNOWN |
| Marken-Codes, KOL-Links | 4 | 1 | 2 | 1 | deirdres_design (Hulala Home, Z Gallerie), ell.glamhome (Homary via GoAffPro), homeofmerve (Eureka), karissa.brighton (Tineco) | VERIFIED |
| Eigener Shop oder Katalog | 6 | 4 | 2 | 0 | divaa.finds (divafinds.us), archibible (Etsy), ai.perfect.world (Redbubble), zaxzaaafrica (Möbel-Vorbestellung), myplants.uae, paulmarkkitchens | VERIFIED |
| Kommentar-Keyword → DM | 6 | 3 | 1 | 2 | roomify.design, divaa.finds, soothenests, montani3d, rendair.ai, hafezi.architects | VERIFIED (Captions/Threads) |

Quelle: [monetization_summary.csv](data/processed/stats/monetization_summary.csv). Die Zeilen „Wayfair" und „Marken-Codes" sind manuell aus den Profil-JSONs gezählt.

**Tabelle 19-B: Accounts mit Möbel-, Home- oder Deko-Affiliate im Detail**

| Account | Follower | Typ · Modus | Was verlinkt wird | Wo | Offenlegung gesehen | Status |
|---|---|---|---|---|---|---|
| @deirdres_design | 1M | Theme-Page · KI-Reposts mit Credit | Amazon-Storefront; Codes „DED15" (Hulala Home) und „DED5" (Z Gallerie) mit `utm_medium=kol`; dazu ein branchenfremder Finanz-Affiliate | Linktree | UNKNOWN | VERIFIED |
| @divaa.finds | 764K | Lifestyle · real | Amazon-Storefront plus ca. 15 Produktlinks, Temu, eigener Katalog | Linktree, Caption-Keyword, Website | Website: *„As an Amazon Associate, I earn from qualifying purchases."* | VERIFIED |
| @ell.glamhome | 1M | Lifestyle · real | Amazon.de-Storefront mit 4 Idea Lists nach Raum (166 Artikel), Homary-Sofa via GoAffPro | Threads- und TikTok-Bio | Amazon-Label „Erhält Provisionen" | VERIFIED |
| @em_henderson | 1M | Lifestyle/Designmedien · real | LTK-Links (24 im Shop), gesponserte Blogposts (u. a. Wayfair, AllModern, Article) | Bio → Blog | *„Thank you to Wayfair for partnering with us"* | VERIFIED |
| @eloisepreen | UNKNOWN | Lifestyle · real | LTK-Sets nach Raum („Items currently in my loft", 23 Plätze) mit UK-Händlern | TikTok-Bio „shop ltk" | UNKNOWN | VERIFIED |
| @karissa.brighton | UNKNOWN | Finds-Creator · real | Amazon „Kitchen/Home Finds List", Rabattcode, Partner-Hashtag, Temu-Code | Caption, Bio | #ad beim Temu-Post | VERIFIED |
| @roomify.design | 62K | Theme-Page · Modus unklar (digital gestagt) | *„curated Wayfair collection + room links"* per DM | Kommentar-Keyword → DM | UNKNOWN | Funnel VERIFIED, Provision UNKNOWN |
| @digitaldesign.lab | 164K | AI-Creator · KI | Benable-Listen, darunter „Amazon Home Finds" (Vasen, Dosen, Krüge) | Linktree | UNKNOWN (Associates-Tag nicht geprüft) | VERIFIED / ESTIMATED |
| @luxquisit | 190K | AI-Creator · KI (Fantasy-Häuser) | eigene Website mit Amazon-Produkten und Expedia-„Unique Stays" | Linktree → Website | *„As an Amazon Associate, Luxquisit earns …"* | VERIFIED |
| @neuraltransform | 83K | AI-Creator · KI (Garten-/Pool-Transformation) | 12 amzn.to-Gartenprodukte (Solarleuchten, Pflanzkübel, Werkzeug) | Linktree | *„Affiliate link. I may earn a commission from qualifying purchases."* | VERIFIED |

**Was die Tabelle zeigt** `[ESTIMATED Synthese]`

- **Real-Footage-Creator verlinken das exakte Produkt**, weil es in ihrer eigenen Wohnung steht. Sie haben entsprechend den kompletten Werkzeugkasten: Storefront, Listen nach Raum, Codes und LTK.
- **KI-Accounts umgehen das „exaktes Produkt"-Problem.** Sie verlinken Kategorie- oder Nutzprodukte, die nicht im Bild sein müssen (neuraltransform: Gartenwerkzeug und Solarleuchten statt des gerenderten Pools), allgemeine Kuratierungslisten (digitaldesign.lab) oder etwas ganz anderes (luxquisit: reale Reiseunterkünfte). Möbel-Affiliate im engeren Sinn zeigt unter den KI-Accounts nur die Repost-Seite @deirdres_design: Amazon-Storefront und Codes für ein Sofa (Hulala Home) und Esszimmerstühle (Z Gallerie). Ihre Reels liegen im Datensatz bei einem Median-`adj` von 0,08 (n=4, **niedrige Konfidenz**). Von eigenen KI-Entwürfen mit Möbel-Affiliate gibt es keinen Beleg.
- **Keiner der 37 KI-Accounts nutzt LTK oder ShopMy**, und [q02](quellen/q02_furniture_affiliate_commerce.md) fand keinen verifizierten Account, der KI-Räume systematisch mit „similar items"-Listen kombiniert `[UNKNOWN → Marktlücke oder Warnsignal]`.

### 2.2 Wie die Konkurrenz Commerce einbindet, ohne nach Werbung auszusehen (Teil 19)

Die Beispiele unten sind **beobachtete Auszüge**: kurz, mit Handle, nur zur Analyse. Übernommen wird das Prinzip, nicht der Wortlaut. Eigene Texte stehen in 5.5.

| # | Muster | Beobachtete Beispiele (Auszug · Handle) | Abgeleitetes Prinzip | Datenlage | Übertragbar auf uns? |
|---|---|---|---|---|---|
| 1 | **Kommentar-Keyword → DM mit kuratierter Kollektion** | *„Comment "SUNROOM" and I'll send you my curated Wayfair collection …"* · @roomify.design (Threads); *„… comment "ROOM" below and I'll DM you the full list"* · @divaa.finds; *„Comment SHOP and I'll send you the link"* · @sagephillipshome (3,0 Mio. Views); *„Comment "BEDROOM" and I'll send you the links to everything featured …"* · @roxy_carretero (2,8 Mio.) | Der CTA ist ein **Service** („ich schicke dir die Liste"), kein Kaufaufruf. Der Link steht nicht im öffentlichen Post, sondern kommt per DM. | Keyword-CTA: 6,6× Kommentare/View, kein nachweisbarer Reichweitenunterschied (p=0,87; siehe Tabelle unten) | **Ja**, als Brücke von Choice-Formaten zu Commerce (5.3) |
| 2 | **Transformation → „shop the key pieces"** | *„You can shop the key pieces to recreate the look"* · @roomify.design; KI-Gartenumbauten plus Amazon-Gartenprodukte · @neuraltransform | Das Produkt ist das „Wie" der Verwandlung, das Reel ist die Geschichte | Transformations-Storys gelten laut Brief (Kernbefund 6) als Gewinnerformat, gestützt nur auf Einzelbeispiele und einen YouTube-Proxy (n klein, kein Test) | **Ja**: P3 „From Nothing" mit kaufbaren Outdoor- und Bad-Stücken |
| 3 | **Finds-Listen nach Raum oder Look** | *„Shop it on my Amazon Kitchen Finds List!"* · @karissa.brighton (37,7 Mio. Views auf der Topic-Seite); Amazon.de-Idea-Lists „Classy LivingRoom" (36), „Everything about BedRoom" (91) · @ell.glamhome | Kuratierung als Dienstleistung, geordnet nach dem, was Zuschauer suchen (Raum, Stil) | Keine Segmentdaten zu Listen | Teilweise: nur als „similar"-Listen je Serie |
| 4 | **Commerce außerhalb des Posts** | Titel-Captions ohne CTA, Shop auf eigener Website · @luxquisit; *„… a list of everything we used - link in my bio!"* · @em_henderson | Das Reel bleibt Inspiration, der Shop liegt eine Ebene tiefer (Bio, Blog, Website) | Link-in-Bio- und Shop-CTAs: `adj` 0,82 vs. 0,98 (p=0,045 nominal, nicht robust, konfundiert). Mosseri: „link in bio" senkt die Reichweite **nicht** ([q01](quellen/q01_instagram_platform_rules.md)) | **Ja**: Standard für Reichweiten-Pillars (P1, P4) |
| 5 | **Tool als Inhalt** (KI-Tool-Promo) | *„Comment "Dreamina" and I'll send you the exact prompt + link"* · @soothenests (#dreaminapartner); *„In collaboration with @artlist.io"* · @ifonly.ai; erster Linktree-Button „TRY LUMA AI!" · @archibible; *„Comment SPACE for the link"* (KI-Staging, Link per Kommentar) · @nomadatoast (2,40 Mio. Views, `adj` 76,9); Staging-App-Empfehlung für Makler · @danielseanmaguire (287K, `adj` 23,4) | Das Versprechen („so entsteht das") liefert den Mehrwert, das Visual ist der Beweis | Einzelfälle. Gegenbeispiele: Tool-Promo-Reel @aigardendesigner mit 2.564 Views (`adj` 0,02); Dreamina-Partnerpost von soothenests auf Threads mit 460 Views ([q06](quellen/q06_ai_theme_page_case_studies.md)) | **Ja**, Rang 1 der Roadmap (5.1) |
| 6 | **Signatur-CTA für Aufträge** | *„For private commissions and inquiries: …"* · @aiforarchitects; *„DM for commissions"* · @archibible; *„Send me a message if you would like to design your space"* · @georgios_tataridis; Disclaimer *„Transformation shown is based on conceptual visualizations. Actual project results may vary."* · @idw.design | Eine dezente Signaturzeile statt Verkaufs-Caption, dazu ein ehrlicher Konzept-Disclaimer | Designer-Studios: `adj` 0,88 (n=382) | **Ja**: B2B-Funnel (Rang 2) |
| 7 | **Marken-Codes und KOL-Links** | Codes „DED15"/„DED5" mit `utm_medium=kol` · @deirdres_design; Eureka-Link mit `utm_medium=kol` · @homeofmerve | Messbar für die Marke, kaum Aufwand für den Creator | – | Später, nur mit passenden Möbel- oder Leuchtenmarken |

**Was die Reel-Daten zu Commerce-CTAs sagen** ([Digest](data/processed/analysis_digest.md), „CTA type"; [monetization_contrasts.csv](data/processed/stats/monetization_contrasts.csv))

| CTA-Typ in der Caption | n (adj) | Median `adj_factor` | Median Kommentare/View |
|---|---|---|---|
| none | 1.273 | 0,98 | 0,000307 |
| question_engagement | 335 | 1,05 | 0,000358 |
| dm | 231 | 0,93 | 0,000371 |
| comment_keyword | 145 | 0,86 | **0,00203** |
| link_in_bio | 99 | 0,82 | 0,000315 |
| shop_product | 51 | 0,82 | 0,000339 |

- **Kruskal-Wallis über alle CTA-Typen:** p=0,62 für `adj`. Kein CTA-Typ unterscheidet sich in der größen- und themenbereinigten Reichweite signifikant von den anderen.
- **Keyword vs. kein CTA:** 6,6× Kommentare pro View (0,00203 vs. 0,000307; n=144 vs. 1.071; p<0,001), `adj` 0,88× (p=0,87, n. s.). **Bei KI-Reels:** 10,0× Kommentare pro View (n=31 vs. 322; p<0,001), `adj` 0,94 vs. 0,82 (n=32 vs. 402; p=0,74, n. s.).
- **Einordnung:** Der Kommentareffekt ist **mechanisch**, weil jeder Interessent kommentieren muss. Er beweist weder ein besseres Ranking noch Käufe. Die drei wichtigsten Ranking-Signale sind laut Mosseri Watch Time, Likes und Sends ([q01](quellen/q01_instagram_platform_rules.md)). Mit den Daten vereinbar ist nur: **Keyword-Funnels zeigen unter den Top-Reels keinen nachweisbaren Reichweitennachteil und gehen mit einer messbaren Handlung (Kommentar) einher.** „Nicht signifikant" heißt dabei nicht „kein Effekt". Ob daraus Klicks und Käufe werden, ist `[UNKNOWN]`. Das prüft unser eigener Test.
- **Choice als Commerce-Brücke:** Choice-Hooks gehen mit 5,67× mehr Kommentaren pro View einher (95-%-CI 2,05–14,3; p=6,4e-08; n=39 vs. 1.971). Der Reichweiten-Effekt (`adj`) von 1,65× ist **nicht belastbar** (95-%-CI 0,87–4,67; p=0,053; n=40). Choice (P2 „Pick One") kann also die Kommentare liefern, an die ein Keyword-Funnel anknüpft (Korrelation, im eigenen Test prüfen).

![Performance nach Caption-Hook (adj_factor)](charts/adj_by_caption_hook.png)

### 2.3 Kostet Kaufbarkeit Reichweite? (Teil 19, Bezug zu Teil 18)

| Segment | n | Median `adj_factor` | Test |
|---|---|---|---|
| Alle Reels · Kaufbarkeit high | 530 | 0,98 | high vs. low 1,01× (95-%-CI 0,80–1,25; p=0,91); Kruskal über 3 Stufen p=0,83 → **n. s.** |
| Alle Reels · medium | 617 | 0,86 | |
| Alle Reels · low | 1.217 | 0,97 | |
| KI-Reels · high | 85 | 1,13 | high vs. low 1,22× (p=0,78); Kruskal p=0,27 → **n. s.** |
| KI-Reels · medium | 204 | 0,73 | |
| KI-Reels · low | 397 | 0,93 | |

**Anteil hoch kaufbarer Reels je Realismus-Stufe** ([Digest](data/processed/analysis_digest.md), Abschnitt 5): fantasy_impossible **0 %** (n=62, 95,2 % low), aspirational_realistic 27,6 %, real_existing 26,6 %, stylized_dreamy 0,3 %. Innerhalb derselben Accounts liegt der Anteil hoch kaufbarer Reels in den Top-10 % bei 17,9 % und in den Bottom-50 % bei 11,5 %, also +6,4 Prozentpunkte. Das beruht auf nur 25 Accounts und 172 Reels (davon 28 in den Top-10 %), die Konfidenz ist niedrig.

**Monetarisierungsklasse der 72 Accounts vs. Reichweite** (explorativ, Account-Ebene, Median der Reel-`adj`; 69 Accounts mit `adj`-Werten): Affiliate 1,85 (n=11 Accounts), Service/B2B 2,13 (n=23), digital/Kurs 1,02 (n=6, **niedrige Konfidenz**), nur Kontakt/sonstiges 1,95 (n=6, **niedrige Konfidenz**), nichts beobachtet 2,29 (n=23). Kruskal p=0,62, also **kein Unterschied nachweisbar**. Die hohen Absolutwerte kommen aus dem Auswahlbias der Shortlist.

![Performance: fantasy vs. realistic (adj_factor)](charts/adj_by_realism.png)

**Folgerung (Hypothese, kein Befund):** Nicht die Kaufbarkeit ist das Problem, sondern der generische KI-Realismus-Look (stylized_dreamy 0,70, n=335). Fantasy-Reels liegen in der Reichweite vorn (2,10, n=62; Korrelation unter Top-Reels), haben aber keine hoch kaufbaren Objekte. Die Lücke dazwischen soll der Hybrid *„Impossible places, possible furniture"* schließen. Er ist ein **Test**, siehe 5.3.

### 2.4 Fazit Teil 19: Chance und Risiken

**Die Chance:** Kein KI-Konkurrent verbindet nachweislich Fantasy-Reichweite mit „similar items"-Commerce. Die Werkzeuge dafür gibt es:

- visuelle Suche: Google Lens (+65 % YoY), Amazon Lens Live, LTK Visual Search, Spacely Furniture Finder
- Tagging als „ähnlich": LTK „Exact vs Similar"
- Instagram-Reel-Tags mit bis zu 30 Produkten

([q02](quellen/q02_furniture_affiliate_commerce.md)) `[VERIFIED]`

**Die Risiken, alle belegt:**

1. **Matching:** Selbst Wayfair ist bei der SKU-Zuordnung von KI-Bildern zurückgerudert. Muse zeigt nur noch Produkte, die vom Bild *„inspired by"* sind. `[VERIFIED]`
2. **Wahrnehmung als „Knockoff":** Instagrams KI-„Shop the Look"-Test (Feb. 2026) erntete Kritik wegen *„cheap knockoffs and random items"*. `[VERIFIED]`
3. **Programmregeln:**
   - LTK verbietet KI-Inhalte, die *„deceives or misrepresents"*.
   - Amazon zahlt onsite nur für dieselbe ASIN-Variante.
   - LTK schrieb 2022: *„Instagram does not have a cookie window"*.

   `[VERIFIED; LTK-Aussage Stand 2022]`
4. **Geografie:** Viele Programme sind US-Programme. Wayfair gilt laut Drittangabe nur für USA/Kanada. Die Instagram-Affiliate-Reels starteten nicht in Deutschland. `[THIRD-PARTY / VERIFIED / DE UNKNOWN]`
5. **Magere Ökonomie:** siehe 5.4.

---

## 3. Teil 20 – Monetarisierung der Konkurrenz

### 3.1 Überblick nach Einnahmequelle (Teil 20)

**Tabelle 20-A: Accounts mit Beleg je Einnahmequelle** (strikte Flags, [monetization_summary.csv](data/processed/stats/monetization_summary.csv))

| Einnahmequelle | alle (n=72) | KI (n=37) | real (n=16) | 3D/gemischt/unklar (n=19) | Typische Träger |
|---|---|---|---|---|---|
| Services/B2B (Design, Rendering, Beratung, Agentur) | **30** | 11 | 10 | 9 | Designer-Studios (12/14), Architekten (2/2), Agenturen |
| Affiliate | 13 | 6 | 5 | 2 | Lifestyle (6/8), AI-Creator (5/16), Theme-Pages (2/17) |
| Sponsoring mit typisiertem Beleg (Partnerpost, KOL-Kampagne, Werbeverkauf) | 8 | 3 | 4 | 1 | Lifestyle, Medien, 2 AI-Creator (Tools) |
| Konkret benannte Marken oder Partner (`brand_deals_seen`) | 20 | 4 | 13 | 3 | vor allem reale Accounts (13/16) |
| Kurse und digitale Produkte | 6 | 4 | 2 | 0 | montani3d, sunt_mrr, ai.perfect.world, rendair.ai, BD Academy (2 Medien-Accounts) |
| Eigener Shop | 6 | 4 | 2 | 0 | siehe 19-A |
| Newsletter | 8 | 2 | 6 | 0 | Medien, Lifestyle, Makler |
| Membership/Club | 3 | 2 | 1 | 0 | thetrillionairelife, luxquisit (Buy Me a Coffee, 1 Supporter), uniqchalets |
| Eigene App/Software | 2 | 1 | 0 | 1 | rendair.ai, harmosai |
| Real Estate / Buchung | 4 | 0 | 4 | 0 | glashaus.realestate, theluxuryhomeshow, wayup_media, uniqchalets |
| Kontakt für Kooperationen (E-Mail, „DM for collabs") | 38 | 17 | 15 | 6 | quer über alle Typen |
| **Weder Geldweg noch Kontakt sichtbar** | **24** | **15** | 1 | 8 | Theme-Pages (11/17), einige AI-Creator |

**Nach Account-Typ:**

| Typ | Accounts | Ergebnis |
|---|---|---|
| Theme-Page | 17 | 11 ohne jeden sichtbaren Weg, 3 Services, 2 Affiliate |
| AI-Creator | 16 | 5 Affiliate, 2 Services, 2 digital, 2 Sponsoring, 7 ohne Weg |
| Designer-Studio | 14 | 12 Services, 0 Affiliate |
| Lifestyle | 8 | 6 Affiliate, 7 mit benannten Partnern |

![Performance nach Account-Typ (adj_factor)](charts/adj_by_account_type.png)

**Einordnung:** Die Account-Typen unterscheiden sich in der bereinigten Reichweite robust (Kruskal p=3,0e-05, auch nach Bonferroni). Lifestyle-Accounts (7 von 8 mit sichtbarem Geldweg) liegen vorn (1,24, n=508 Reels), die Theme-Pages mit dem **niedrigsten** Anteil sichtbarer Geldwege (4 von 17) hinten (0,74, n=503). Ein durchgehendes Muster „mehr Geldwege = mehr Reichweite" gibt es aber nicht: AI-Creator liegen bei 1,09 (n=276) mit nur 8 von 16 Accounts mit Geldweg, Designer-Studios (12 von 14) bei 0,88 (n=382) und Medien (5 von 6) bei 0,79 (n=66). Wir lesen das als **Hypothese**: Eine erkennbare Identität könnte Reichweite und Monetarisierung zugleich tragen. Es ist keine Kausalaussage.

### 3.2 Tabelle Top-Accounts: KI- und 3D-Wettbewerber (Teil 20)

Legende: **V** = VERIFIED beobachtet · **E** = ESTIMATED (Hinweis gesehen, Bezahlung oder Provision unbelegt) · **–** = nicht beobachtet (`[UNKNOWN]`, kein Beleg für Abwesenheit). Follower = VERIFIED (Embed, gerundet, 25.09.2026). Keine Einkommensschätzungen.

| Account | Follower | Typ · Modus | Affiliate | Sponsored | Interior/Möbel-Marken | Real Estate | Kurse | Digitale Produkte/Shop | Services | Newsletter | Apps/Software | Beleg (kurz) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| @thetrillionairelife | 13M | Medien · KI | – | V | – | – | – | – | – | V | – | „Advertise"-Seite ohne Rate Card; Club „Trillion Circle"; Eigenmarke |
| @naturesms | 10M | Theme · KI | – | – | – | – | – | – | – | – | – | kein Weg sichtbar |
| @siyad_abdali | 4M | Theme · KI | – | – | – | – | – | – | – | – | – | kein Weg sichtbar (Top-Reel 282 Mio. Views) |
| @soothenests | 2M | AI-Creator · KI | E | V | – | – | – | – | – | – | – | #dreaminapartner (Threads, 460 Views); Gratis-Prompts per DM |
| @sunt_mrr | 2M | AI-Creator · KI | – | E | – | – | V | V | – | – | – | Kurse und Premium-Prompts gelistet, Store am 25.09. nicht erreichbar; Resort-Post ohne Label |
| @vrishtidesigns | 2M | Studio · 3D | – | – | – | – | – | – | V | – | – | WhatsApp-Projektanfrage, 8K-Renders |
| @aiforarchitects | 1M | Studio · KI | – | – | – | – | – | – | V | – | – | *„For private commissions"*, 5 Leistungen, keine Preise |
| @luxurydreamhub | 1M | Theme · KI | – | – | – | – | – | – | – | – | – | kein Weg sichtbar |
| @ifonly.ai | 1M | AI-Creator · KI | – | V | – | – | – | – | – | – | – | *„In collaboration with @artlist.io"* (2 Posts) |
| @deirdres_design | 1M | Theme · KI-Reposts | V | E | V | – | – | – | V | – | – | Amazon-Storefront, KOL-Codes Hulala Home/Z Gallerie, virtuelle Beratung |
| @miladeshtiyaghi | 642K | Architekt · KI | – | – | – | – | – | – | V | – | – | Architektur-, Interior- und Landschaftsdesign weltweit |
| @montani3d | 603K | Kurs · KI | – | – | – | – | V | – | V | – | – | Workshop R$ 29,90 (statt R$ 97), Replay R$ 197; Render-Studio; *„Comente WORKSHOP"* |
| @drcozyvibes | 584K | Theme · KI | – | – | – | – | – | – | – | – | – | „looking for collaborations"; YouTube-Funnel mit 1,13K Abos |
| @elarch.studio | 540K | Studio · 3D | – | – | – | – | – | – | V | – | – | Behance: Außenrender „starting from US$200" |
| @cozyzen.ai | 498K | AI-Creator · KI | – | E | – | – | – | – | – | – | – | *„For promos Dm"* (gleiche Kontaktadresse wie soothenests) |
| @georgios_tataridis | 321K | Studio · 3D | – | – | – | – | – | – | V | – | – | Interior-Design mit 3D-Visualisierung weltweit |
| @idw.design | 318K | Studio · KI | – | – | – | – | – | – | V | – | – | Beratungstermine, Design & Build, Konzept-Disclaimer |
| @archibible | 220K | AI-Creator · KI | V | – | – | – | – | V | V | – | – | Luma-Referral-Link, Etsy-Shop (Inhalt UNKNOWN), Commissions |
| @luxquisit | 190K | AI-Creator · KI | V | – | – | – | – | – | – | V | – | Amazon und Expedia auf eigener Website; Buy Me a Coffee mit 1 Supporter |
| @rendair.ai | 189K | Marke · KI | – | – | – | – | V | – | – | – | V | eigene SaaS für 19–190 USD/Monat; Academy; betreibt selbst ein Affiliate-Programm (20 %, 1 Jahr) |
| @digitaldesign.lab | 164K | AI-Creator · KI | E | – | – | – | – | – | – | – | – | Benable-Listen inkl. „Amazon Home Finds" |
| @myplants.uae | 123K | Handwerk · KI-Inspiration | – | – | – | – | – | V | V | – | – | *„AI-generated inspiration brought to life by MyPlants"*; Landschaftsbau, Shopify-Shop |
| @neuraltransform | 83K | AI-Creator · KI | V | – | – | – | – | – | – | – | – | 12 amzn.to-Gartenprodukte mit Offenlegung |
| @zaxzaaafrica | 65K | Studio · KI | – | – | – | – | – | V | V | – | – | Anfragen und Buchungen per Bio; Möbel-Vorbestellung |
| @roomify.design | 62K | Theme · unklar | E | – | E | – | – | – | – | – | – | Wayfair-Kollektion per Keyword-DM |
| @stylishnorrastudios | 40K | Studio · KI | – | – | – | – | – | – | V | – | – | *„Direct message our studio …"* |
| @ai.perfect.world | 14K | AI-Creator · KI | – | – | – | – | – | V | V | – | – | Gumroad-E-Book 29 € (Seitendaten: `sales_count` 1); Redbubble-Prints; KI-Werbevisuals für Marken |

### 3.3 Tabelle Benchmarks: reale Home-, Medien- und Immobilien-Accounts (Teil 20)

| Account | Follower | Typ · Modus | Affiliate | Sponsored | Interior/Möbel-Marken | Real Estate | Kurse | Digitale Produkte/Shop | Services | Newsletter | Apps/Software | Beleg (kurz) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| @beautifuldestinations | 24M | Medien · real | – | V | – | – | V | – | V | V | – | Reise-Marketingagentur (Kunden u. a. Accor, Saudi Tourism Authority); BD Academy |
| @beautifulhotels | 6M | Medien · real | – | V | – | – | V | – | V | V | – | gleiche Mutteragentur; Hotel-Features |
| @juliagal_ | 4M | Lifestyle · real | – | E | – | – | – | – | V | – | – | Content-Agentur; Hotel-Tags ohne Label |
| @theluxuryhomeshow | 2M | Medien · real | – | E | – | V | – | – | – | – | – | Feature-Bewerbung (ob bezahlt: UNKNOWN); YouTube 1,31M Abos |
| @em_henderson | 1M | Lifestyle · real | V | V | V | – | – | – | V | V | – | LTK, gesponserte Makeovers (Blog-Kategorie mit 70 Posts), Display-Ads, Newsletter |
| @ell.glamhome | 1M | Lifestyle · real | V | – | V | – | – | – | – | – | – | Amazon.de-Storefront, Homary-Affiliate |
| @wayup_media | 942K | Medien · real | – | E | – | V | – | – | V | – | – | Listing-Touren, Produktion; Netzwerk für *„sponsored house tours"* |
| @divaa.finds | 764K | Lifestyle · real | V | E | – | – | – | V | – | – | – | Amazon-Storefront, Temu, eigener Katalog |
| @uniqchalets | 684K | Theme · real | – | – | – | V | – | – | V | V | – | eigene Buchungsplattform, E-Mail-Deals-Club |
| @homeofmerve | 459K | Lifestyle | E | V | – | – | – | – | – | – | – | Eureka-KOL-Link, Talent-Management |
| @paulmarkkitchens | 304K | Handwerk · real | – | – | V (eigene Marken) | – | – | V | V | – | – | Küchenplanung, eigene Outdoor-Küchen |
| @glashaus.realestate | 296K | Makler · real | – | – | – | V | – | – | V | V | – | Makler bei Christie's; Listings anderer Makler mit Credit |
| @eloisepreen | UNKNOWN | Lifestyle · real | V | E | – | – | – | – | – | V | – | LTK-Shop, Substack |
| @karissa.brighton | UNKNOWN | Finds · real | V | V | – | – | – | – | – | – | – | Amazon-Listen, Tineco-Code, #delomopartner, Temu #ad |

### 3.4 Einkommen: was bekannt ist (nur Drittangaben, Teil 20)

Für **keinen** der 72 Accounts ist ein Umsatz belegt. Die folgenden Zahlen stammen ausschließlich aus den Quellennotizen und sind **keine Schätzung von uns**:

| Aussage | Wert | Einordnung | Quelle |
|---|---|---|---|
| LTK-Creator in UK | *„£1,200 a month if they post three times a week"* | Selbstauskunft von LTK, Durchschnitt über alle Kategorien | [q02](quellen/q02_furniture_affiliate_commerce.md) `[THIRD-PARTY ESTIMATE]` |
| Interior AI (SaaS, keine Theme-Page) | *„40K, 50K a month"* (2024) | Gründer-Selbstauskunft; Tool-Geschäft, nicht Content | [q06](quellen/q06_ai_theme_page_case_studies.md), [q04](quellen/q04_interior_trends_demand.md) `[THIRD-PARTY ESTIMATE]` |
| Cozy-KI-Theme-Page (Tutorial) | *„tens of thousands of dollars every month"* | reine Spekulation des Tutorial-Autors | [q06](quellen/q06_ai_theme_page_case_studies.md) `[THIRD-PARTY ESTIMATE]` |
| „Houses niche" (Tutorial) | *„$150 a day … about $45,000 a month"* | **rechnerisch falsch** (150 USD/Tag ≈ 4.500 USD/Monat); YouTube, nicht IG | [q06](quellen/q06_ai_theme_page_case_studies.md) `[THIRD-PARTY ESTIMATE]` |
| Sponsored Posts auf Theme-Pages | *„$10"* bis *„over $11,000 per post"* | Selbstauskunft eines Theme-Page-Verkäufers; allgemein, nicht KI- oder Interior-spezifisch | [q06](quellen/q06_ai_theme_page_case_studies.md) `[THIRD-PARTY ESTIMATE]` |
| KI-Architektur-Kurs (Tim Fu) | 150 € × 100 Plätze → theoretisch < 15.000 € brutto | Preise VERIFIED, Belegung UNKNOWN; namentlich bekannter Architekt | [q06](quellen/q06_ai_theme_page_case_studies.md) |
| montani3d | *„+10.000 PARTICIPANTES"*; Renderverträge *„de até R$ 80 mil"* | Werbeaussage auf der Landingpage | Profil-JSON `[THIRD-PARTY ESTIMATE]` |
| YouTube-Proxy RPM | Luxus-Home-Tours 4,77 USD; Regen-Ambience 6,62–8,22 USD; mehrere KI-Interior-Kanäle „Not monetized" | NexLev-Schätzung, YouTube ≠ Instagram | [q08](quellen/q08_cross_platform_signals.md) `[THIRD-PARTY ESTIMATE]` |

**Gegensignal aus Primärdaten:** Das Gumroad-E-Book von @ai.perfect.world (29 €) zeigt in den Seitendaten `sales_count` 1 `[VERIFIED Rohfeld, Stand 25.09.2026]`. Der Cross-Platform-Funnel von @drcozyvibes brachte trotz eines Reels mit 155 Mio. Views nur 1,13K YouTube-Abos `[VERIFIED]` ([q06](quellen/q06_ai_theme_page_case_studies.md)).

### 3.5 Muster und Lehren (Teil 20)

1. **Reichweite allein wird selten sichtbar zu Geld gemacht.** 15 von 37 KI-Accounts zeigen weder einen Geldweg noch einen Kontakt, darunter vier der größten (naturesms 10M, siyad_abdali 4M, elitebuildhq 2M, luxurydreamhub 1M). Der Verkauf von Reichweite (*„For promos Dm"*) ist zudem durch Instagrams Originalitäts-Update vom 30.04.2026 bedroht, zumindest für Repost-Seiten ([q03](quellen/q03_sponsors_brand_deals.md)).
2. **Das professionelle Standardmodell ist der Service-Funnel.** Visuals ziehen Anfragen an, die Signaturzeile verweist auf Aufträge. Bei KI-Studios gibt es das, aber ohne Preise und ohne Belege für Aufträge.
3. **Die Sponsoren reiner KI-Creator sind KI-Tools** (Dreamina, Artlist, Luma). Möbelmarken arbeiten überwiegend über Affiliate. Marken meiden KI-Gesichter und KI-Creator nach außen: Die Begeisterung für KI-Creator-Content fiel von 60 % auf 26 %, 89 % der Enterprise-Marketer planen nicht mit virtuellen Influencern. Gleichzeitig haben 79 % ihre KI-Investitionen erhöht ([q03](quellen/q03_sponsors_brand_deals.md)) `[VERIFIED]`. Für ein **gesichtsloses KI-Studio** sind Tools deshalb die natürlichen Sponsoren `[ESTIMATED]`.
4. **Die sichtbarsten Commerce-Accounts kombinieren mehrere Wege.** Beispiele: em_henderson mit LTK, Sponsoring, Display-Ads, Newsletter und Design-Services; deirdres_design mit Storefront, Codes und Beratung. Über alle 45 Accounts mit sichtbarem Geldweg ist das Bild aber gemischt: 22 zeigen mindestens zwei Einnahmearten, 23 nur eine (strikte Flags; „nicht beobachtet" heißt nicht „nicht vorhanden").
5. **Kein KI-Account verlinkt sichtbar „ähnliche Produkte" zu seinen eigenen KI-Räumen.** Die Möbelcodes der Repost-Seite deirdres_design gehören nicht zu eigenen Entwürfen. Das ist gleichzeitig Marktlücke und Warnsignal (2.4).

---

## 4. Programmbedingungen (Referenz aus q02/q03)

### 4.1 Möbel, Home, Deko

| Programm | Provision | Cookie/Fenster | Zugang | Wichtig für uns | Status |
|---|---|---|---|---|---|
| **Amazon Associates (US)**, Furniture/Home | **3,00 %** (Kitchen 4,50 %) | **24 h**; Artikel im Warenkorb zählen bis zu dessen Ablauf (meist 90 Tage) | Konditionen je Marktplatz; amazon.de-Sätze in den Quellen UNKNOWN | **Keine Provision** für Käufe über *„any paid or boosted advertisement linking to Amazon"* (seit 14.04.2026). Pflichtsatz *„As an Amazon Associate I earn from qualifying purchases."* Linkverkürzer dürfen Amazon nicht verschleiern. Produktbilder und Preise nur über API bzw. Program Content. | VERIFIED |
| Amazon Influencer (Storefront, Idea Lists), onsite | 3,00 % (Table A), Creator Ads 4,00 % (Table B), **nur dieselbe ASIN-Variante** | – | Kriterien nicht veröffentlicht; Dritte nennen „min. 1,000 followers" | „Similar"-Listen verdienen onsite nur am exakt verlinkten Artikel | VERIFIED / Schwelle THIRD-PARTY |
| **LTK** | Ø **10–25 %**, bis 30 % (Händler legen fest) | meist 7–30 Tage, Ø 7–14 (Stand 2022); *„Instagram does not have a cookie window"* | **≥5K Follower, ≥2 Posts/Woche** | Exact-vs-Similar-Tagging, 2–8 Produkte pro Post; Community Guidelines (18.03.2026) verbieten täuschende KI-Inhalte | VERIFIED (Selbstauskunft) |
| **ShopMy** | 10–30 % | „7 days is a common window" vs. „On average, it's 30 days" | kuratiert | Raten für Home-Marken UNKNOWN (Seite 404) | VERIFIED (widersprüchlich) |
| **Wayfair** (+AllModern, Perigold …) | bis 7 % | 7 Tage (auch „up to 14") | Creator Program, Schwelle UNKNOWN | AOV 332 USD (Q2 2026, VERIFIED); 7-Day-EPC 1,52 USD; „nur USA/Kanada" nur als Snippet | Provision THIRD-PARTY |
| Article | 5 % | 30 Tage | Awin | – | VERIFIED (Netzwerkseite) |
| Castlery | nicht genannt (Bonus „no cap") | ≥30 Tage | Impact; Ambassador-Programm (nur US) mit Möbeln bis 3.500 USD | – | VERIFIED |
| Arhaus | bis 4 % | 30 Tage | über Agentur | AOV 1.100 USD | VERIFIED (Agentur) |
| 1stDibs | 5–10 % | UNKNOWN | Partnerize/Skimlinks | AOV 2.850 USD (Median 1.500) | Rate THIRD-PARTY, AOV VERIFIED |
| Chairish | 10 % | 30 Tage | Ascend | AOV > 1.000 USD | THIRD-PARTY |
| Anthropologie | nicht genannt (Dritte: 6 %, Möbel 10 %) | 30 Tage | Rakuten | – | Fenster VERIFIED |
| West Elm / Williams-Sonoma | 1–5 % / 3–5 % | 30 / 7–30 Tage | Impact / CJ | Angaben widersprüchlich | THIRD-PARTY |
| Crate & Barrel / CB2 | 0,8 % / 0,8–12 % | 7 Tage | FlexOffers | EPC CB2 0,16 USD | THIRD-PARTY |
| Etsy | 4 % (UGC 2 %?) | 30 Tage Web / 7 Tage App | Creator Collective ab 500 Followern | – | Schwelle VERIFIED, Rate THIRD-PARTY |
| IKEA | nur Spanien: bis 5 % | – | – | USA/UK: kein Programm belegt | VERIFIED / UNKNOWN |
| RH, Minotti, B&B Italia, Poliform | kein Affiliate belegt | – | – | Luxus-Looks nur indirekt über 1stDibs, Chairish, DWR, Perigold verlinkbar | UNKNOWN |
| **Instagram-Affiliate-Reels** (Produkt-Tags) | Händlerprovision über Impact, Rakuten, Shopify Collabs | – | Start in US, BR, IN, ID, TH; **DE nicht in der Startliste** | bis 30 Produkte pro Reel; Produkte müssen im Meta-Katalog sein | VERIFIED / DE UNKNOWN |

**Provision pro Bestellung** (Rechnung aus [q02](quellen/q02_furniture_affiliate_commerce.md)) `[ESTIMATED]`:

| Händler | Rechnung | Provision pro Bestellung |
|---|---|---|
| Amazon Home | 3 % × 100 USD (hypothetischer Warenkorb) | ≈ 3 USD |
| Wayfair | bis 7 % × 332 USD | ≈ 23 USD |
| Arhaus | 4 % × 1.100 USD | ≈ 44 USD |
| 1stDibs | 5–10 % × 2.850 USD | ≈ 143–285 USD |

**Welche Produkte wir verlinken:** Kleine Deko-Stücke (Vasen, Spiegel, Teppiche, Kissen) sind laut Pinterest die meistgekauften Lens-Produkte `[VERIFIED, 2020]`. Sie eignen sich für Amazon mit 24-h-Fenster. Große Möbel verlinken wir besser bei Programmen mit 30-Tage-Fenster und hohem AOV `[ESTIMATED]`.

### 4.2 KI-Tools (für uns am relevantesten)

| Anbieter | Programm | Konditionen | Schwelle | Status |
|---|---|---|---|---|
| **Runway** | Affiliate | **15 USD pro neuem zahlenden Abo, kein Cap**, 3-Monats-Pilot, Auszahlung monatlich per Stripe, dazu Max-Plan mit 9.500 Credits/Monat | *„Every audience tier is welcome"* | VERIFIED |
| Runway | Creative Partners | Max-Plan gratis, Kollaborationen, kein Bargeld | Bewerbung | VERIFIED |
| **Higgsfield** | Affiliate | **bis 25 % des Planpreises für bis zu 12 Monate** | *„Anyone with an audience can apply"* | VERIFIED |
| **Higgsfield** | Earn (Instagram) | Zahlung je genehmigtem Video, dazu Boni nach 24 h und am 7. Tag; **max. 2.500 USD pro Video**, 1.000 USD Cap am ersten Tag; Instagram verbinden, Bio-Code | – | VERIFIED; Einstieg „$10–50 per video" THIRD-PARTY |
| Higgsfield | Creator Partnership | Abo, Credits, Early Access; Pflicht: *„tag or mention Higgsfield"* | laut Seite keine Schwelle (Drittseite: nur auf Einladung) | VERIFIED / widersprüchlich |
| Luma | Creative Partner | Credits, Awards; Attribution „Created with Luma" | **5.000+ engagierte Follower**, 2–3 Posts/Monat | VERIFIED |
| Planner 5D | Affiliate | 25 % (Silver), 50 % ab 500 Sales/Monat; **Cookie 90 Tage**; Auszahlung ab 100 USD | – | VERIFIED |
| REimagineHome | Affiliate | 30 % pro Referral (ob wiederkehrend: unklar) | – | VERIFIED |
| Collov AI | Affiliate | *„up to $150 for lifetime recurring commission"* | – | VERIFIED |
| Rendair AI | Affiliate (über Dub) | *„Earn 20% per sale for 1 year"*; Neukunden 10 % Rabatt | – | VERIFIED (Profil-JSON) |
| Freepik | Affiliate | 30 % einmalig, 60 Tage | – | THIRD-PARTY |
| Krea / Kling | Creative Partners / NextGen | Credits bzw. Filmförderung (bis 1 Mio. USD, ≥50 % KI) | Projekt | THIRD-PARTY / VERIFIED |
| Leonardo | Affiliate | **seit 07.04.2026 geschlossen** | – | VERIFIED |
| Midjourney, Interior AI, RoomGPT | – | kein Programm gefunden | – | UNKNOWN |
| Ampere (Vergleich) | Creator Program | 1,50 USD pro 1.000 IG-Views; 15 USD pro zahlendem Kunden; Cap 1.000 USD/Monat und 100 USD/Post | – | THIRD-PARTY |
| Dreamina, Artlist | bei Konkurrenten beobachtete Partnerschaften | Konditionen UNKNOWN | – | Posts VERIFIED |

**Marktumfeld:** Der Markt für KI-Interior-Apps ist groß und zersplittert. Bei Google Play liegt Planner 5D bei 50M+ Downloads, Home AI (HubX) bei 10M+. 10 von 30 Treffern haben unter 1M Downloads ([q04](quellen/q04_interior_trends_demand.md)) `[VERIFIED]`. Es gibt also viele potenzielle Werbekunden. Laut Gemlist zahlen aber *„Most Don't"* in bar, sondern in Credits ([q03](quellen/q03_sponsors_brand_deals.md)).

### 4.3 Sponsoring- und Preisbenchmarks (alle Drittangaben, außer wo vermerkt)

| Kennzahl | Wert | Quelle | Status |
|---|---|---|---|
| IG-Post nach Stufe | nano 10–100, micro 100–500, mid 500–5.000, macro 5.000–10.000 USD; Reels 1,2–1,5× Post; CPM 5–25 USD | IMH, 31.08.2026 | THIRD-PARTY |
| Home & Lifestyle Reels (US) | micro 750–5.000, mid 5.000–20.000 USD | Modash, 03.07.2026 | THIRD-PARTY |
| Home Decor pro 1.000 Views | 9–20 USD | usesnippet, 06/2026 | THIRD-PARTY |
| DACH | Reels-CPM 10–50 €; Nutzungsrechte +25–100 % | Modash | THIRD-PARTY |
| Mansion Global | IG-Post 2.000 USD bei 130K Followern (≈ 15,4 USD pro 1.000 Follower); Newsletter-Sponsoring 3.680 USD/Woche; Custom Email 7.000 USD/Versand | Rate Card (undatiert) | VERIFIED / Umrechnung ESTIMATED |
| Marriott Tribute Portfolio | 12.750 USD plus Aufenthalt für 1 Reel, 1 Carousel und Assets | Substack, 24.09.2026 | VERIFIED (so berichtet) |
| Dubai Immobilien-Creator | AED 3.500–5.500 pro Creator; Kampagne AED 50.000–200.000 | Agentur Yamammi | THIRD-PARTY |
| Theme-Page-Shoutout | ab 5 USD (Meme-Page mit 100K) | Fiverr (Snippet) | UNKNOWN |

Gesichtslose Seiten ohne Community-Vertrauen dürften **am unteren Rand** liegen, weil ihr Wert Reichweite ist und nicht Empfehlung ([q03](quellen/q03_sponsors_brand_deals.md)) `[ESTIMATED]`.

### 4.4 Instagram-eigene Monetarisierung ([q01](quellen/q01_instagram_platform_rules.md))

| Programm | Bedingung | Status |
|---|---|---|
| Gifts | ab 500 Followern, 18+, DE/AT gelistet | VERIFIED |
| Subscriptions | ab 10.000 Followern, DE/AT gelistet | VERIFIED |
| Content Monetization Policies | **Nicht monetarisierbar:** *„static images played in succession"*, Loops desselben Segments, Standbilder mit Textüberlagerung, unoriginale Inhalte. Unsere Reels brauchen echte Bewegung (siehe [16_automation_strategy.md](16_automation_strategy.md)). | VERIFIED |
| Breakthrough Bonus | nur USA | VERIFIED (Sekundärquelle) |
| Link in Bio | bis 5 Links; Mosseri: *„if you say 'link in bio' it's going to decrease your reach. That is not true."* | VERIFIED |

---

## 5. Eigene Monetarisierungs-Roadmap (Teil 20)

### 5.1 Einnahmequellen, sortiert nach Evidenz

| Rang | Einnahmequelle | Evidenz Wettbewerb | Programm- und Marktbelege | Passung zu „Homes that shouldn't exist (yet)" | Hauptrisiko | Start | Evidenzgrad |
|---|---|---|---|---|---|---|---|
| **1** | **KI-Tool-Affiliate und -Sponsoring** | 3 KI-Accounts mit Tool-Deals (soothenests: Dreamina, ifonly.ai: Artlist, archibible: Luma); Tool-Promo-Reels mit hohem `adj` (nomadatoast 76,9; danielseanmaguire 23,4), aber auch Flops | Runway, Higgsfield (Affiliate, Earn, CPP), Luma, Planner 5D, REimagineHome, Collov, Rendair: Konditionen VERIFIED | **Hoch.** Unser Publikum ist KI-affin; Tools sind die einzigen beobachteten Sponsoren, die KI-Creator nach außen zeigen | meist Credits statt Bargeld; Tool-Müdigkeit; Pflicht zur Kennzeichnung | Phase 0 | **mittel bis hoch** (Programme VERIFIED, Umsätze UNKNOWN) |
| **2** | **B2B-Visualisierung** (Konzept-Reels und Visuals für Architekten, Landschafts- und Poolbauer, Marken) | 30/72 Accounts mit Services; 12/14 Studios; KI-Beispiele: aiforarchitects, myplants.uae, idw.design, montani3d, ai.perfect.world | 29 % der Designer nutzen KI (2023: 9 %), 24 % sind *„strongly against"* ([q04](quellen/q04_interior_trends_demand.md)) | **Hoch.** Die Konzeptarchitektur ist selbst das Portfolio | Anfrage→Auftrag UNKNOWN; Vertrauensrisiko bei KI-Staging ([q06](quellen/q06_ai_theme_page_case_studies.md)); Staging-Tools ab 16 USD/Monat machen reines Staging zur Massenware | ab ca. 10K (Portfolio) | **mittel** (Angebote VERIFIED) |
| **3** | **Digitale Produkte** (Workflow-Guides, Prompt-Notizen, Workshops) | 6/72 (montani3d, sunt_mrr, ai.perfect.world, rendair Academy, BD Academy) | Tim Fu: 150 €, 100 Plätze; ai.perfect.world: `sales_count` 1 | **Mittel.** Wir sind ein Studio, keine Tutorial-Seite. „Instructional"-Hooks liegen niedrig (0,72, n=74; Caption-Hooks insgesamt n. s., Kruskal p=0,35) | schwache Nachfrage; Einkommensversprechen sind UWG-Risiko | Warteliste ab 10K, Launch ab 50K | **niedrig bis mittel** |
| **4** | **Möbel-Affiliate über Choice- und Transformationsformate** | 13/72 Affiliate; bei KI meist Low-Ticket oder Tool-Links (6/37; Möbelcodes nur bei der Repost-Seite deirdres_design) | Amazon 3 % bei 24 h; Wayfair ≤7 % bei 7 Tagen (Dritte); LTK 10–25 % (Selbstauskunft); High-AOV-Programme mit 30 Tagen | **Mittel**, nur mit „possible furniture" (Fantasy ist zu 0 % kaufbar) | dünne Ökonomie; Matching; Knockoff-Wirkung; US-Programme | Test in Monat 2, Ausbau ab 10–50K | **niedrig bis mittel** |
| **5** | **Real Estate / Projektentwickler** | 4/72, **alle mit realem Material**; ein Account mit vermutlich KI-Visuals (Modus unbestätigt) rahmt Villen als Investment ein (harmosai) | Mansion Global 2.000 USD/Post; Dubai AED 50–200K pro Kampagne (Dritte); VAE-Permit-Pflicht | **Niedrig** für Sponsoring (Makler wollen das echte Objekt zeigen, [q03](quellen/q03_sponsors_brand_deals.md)); **mittel** als B2B-Konzeptvisualisierung | Irreführung (§ 5 UWG, KI-VO), Lizenzpflichten | ab 50K, nur als B2B | **niedrig** |
| **6** | **Newsletter** | 8/72, überwiegend Medien und reale Accounts | Mansion Global: Newsletter-Sponsoring 3.680 USD/Woche (Verlag) | **Mittel** als eigener Kanal (Absicherung gegen Plattformrisiken wie Originalitäts-Update und KI-Filter) | Aufbauaufwand; für KI-Accounts nicht als Umsatzquelle belegt | Liste ab Phase 0; Monetarisierung ab 50–200K | **niedrig** als Umsatz, **hoch** als Absicherung `[ESTIMATED]` |

**Bewusst nicht empfohlen:**

- **Shoutout- und Promo-Verkauf wie bei einer Theme-Page.** Das ist ein Low-Trust-Segment (Fiverr ab 5 USD), durch das Originalitäts-Update bedroht und passt nicht zur Studio-Identität.
- **Branchenfremde Affiliates** wie der Finanz-Link bei deirdres_design. Sie kosten Glaubwürdigkeit `[ESTIMATED]`.
- **Instagram-Subscriptions vor einem echten Mehrwert-Angebot.** Dafür gibt es keine Evidenz.

### 5.2 Roadmap nach Phase (0–10K, 10–50K, 50–200K, 200K+)

**Übersicht**

| Phase | Fokus | Aktiv monetarisieren | Aufbauen und testen | Programmschwellen in dieser Phase | Nicht tun | Gate zur nächsten Phase (S) |
|---|---|---|---|---|---|---|
| **0–10K** „Beweis" | Reichweite und Follows ([15](15_kpi_framework.md)) | Tool-Affiliate **nur für tatsächlich genutzte Tools** (Runway für alle Stufen, Higgsfield „anyone with an audience"); Higgsfield Earn prüfen (bezahltes Video = Werbung) | Bio-Seite (max. 5 Links) mit Studio-Portfolio, Newsletter-Anmeldung und Offenlegung; Sub-ID-Tracking je Serie; ab Monat 2 den Test „Impossible places, possible furniture" (5.3) | Gifts ab 500; Etsy Creator Collective ab 500; Amazon Influencer „min. 1,000" (Drittangabe); Luma und LTK ab 5.000 | Shoutouts verkaufen; Amazon-Links in geboosteten Reels; Preise oder Orte für fiktive Objekte | ≥10K Follower **und** ≥30 Reels einer Serie als Portfolio **und** Klickrate je Serie gemessen |
| **10–50K** „Erste Umsätze" | Serien stabilisieren, Media-Kit | Tool-Deals als Pauschale pro Reel oder Serie (Anker: IMH micro 100–500 USD/Post; Modash-US-Home micro Reels 750–5.000 USD; gesichtslos eher unterer Rand); Luma CPP; **2–3 B2B-Piloten**; Möbel-Affiliate **nur bei bestandenem Test** | LTK- und ShopMy-Bewerbung mit „similar"-Tagging; Warteliste für ein digitales Produkt (Nachfragetest über „which tool / how"-Kommentare); Media-Kit-KPIs ([15](15_kpi_framework.md), 3.7) | Subscriptions ab 10K (optional) | Kursverkauf ohne Warteliste; Einkommensversprechen | ≥1 wiederkehrender Tool-Partner **oder** ≥2 bezahlte B2B-Projekte; Commerce-Test entschieden |
| **50–200K** „Portfolio" | Diversifizieren | Serien-Sponsoring („presented by"), Pakete aus Reel, Story und Nutzungsrechten (Aufschlag laut Modash 25–100 %, Dritte); B2B als Festpakete; High-AOV-Affiliate mit 30-Tage-Fenster für „possible furniture"-Listen | Digitales Produkt nur bei ≥300 Wartelisten-Einträgen (S); Newsletter-Sponsoring testen; B2B-Konzeptvisualisierung für Entwickler **mit Compliance-Check** (Abschnitt 6) | – | Immobilien-Listing-Werbung für reale Objekte mit KI-Bildern; fiktive „Investment"-Rahmung | stabiler Mix, kein Einzelstrom > 60 % des Umsatzes |
| **200K+** „Rechte und Skalierung" | Verträge und Rechte | Jahresverträge mit Tools; Lizenzierung von Clips oder Visuals an Medien; Workshops; Kollaborationen mit Möbel- und Leuchtenmarken als „Partner für die kaufbaren Stücke" | YouTube-Long-Form als Zweitkanal (RPM Luxus-Home-Tours 4,77 USD laut Dritten; Konversion IG→YT schwach belegt); Prints mit niedriger Priorität (Umsatz UNKNOWN) | – | Exklusivverträge, die Tool-Neutralität verhindern (S) | – |

**Phase 0–10K: Checkliste**

- [ ] Nur Tools bewerben, die tatsächlich in der Pipeline laufen ([16_automation_strategy.md](16_automation_strategy.md)); Credit-Zeile „Made with …" nach den Tool-AGB. Bei Higgsfield CPP ist Taggen Pflicht.
- [ ] Die Affiliate-Programme Runway und Higgsfield beantragen (Konditionen in 4.2); für jede Serie eine eigene Sub-ID bzw. einen eigenen Code.
- [ ] Bio-Seite mit maximal 5 Links: Studio/Portfolio, Newsletter, „Tools we use" (Affiliate, gekennzeichnet), später „Real pieces" (Möbel-Listen), Kontakt.
- [ ] Newsletter-Anmeldung ab Tag 1: eigener Kanal gegen Plattformrisiken (Originalitäts-Update, KI-Filter, [q01](quellen/q01_instagram_platform_rules.md), [q06](quellen/q06_ai_theme_page_case_studies.md)).
- [ ] Portfolio-Seite für B2B: nur Originalentwürfe, jeweils als „AI concept" gekennzeichnet, ohne reale Marken- oder Hotelnamen.
- [ ] Klickrate pro 1.000 Views je Serie messen. Sie ist die größte Unbekannte in 5.4.

**Phase 10–50K: Checkliste**

- [ ] Media-Kit mit Median-Reach, Nicht-Follower-Anteil, Sends- und Saves-Rate und Zielmarkt-Anteil (US-Anteil wichtig für US-Programme).
- [ ] Erste Tool-Pauschale verhandeln: Serie mit 3 Reels, Offenlegung doppelt (6.1), Musik aus der Sound Collection.
- [ ] B2B-Piloten (5.5): 2–3 Projekte mit Referenzrecht; Preise als Test-Variable (UNKNOWN), Untergrenze aus dem Wettbewerb: 3D-Außenrender „ab 200 USD" (elarch.studio).
- [ ] LTK-Bewerbung erst, wenn die Similar-Kennzeichnung und das KI-Label stehen (LTK verbietet täuschende KI-Inhalte).

**Phase 50–200K und 200K+: Checkliste**

- [ ] Kein Einzelstrom über 60 % (S). Für Tool-Verträge Kategorie-Exklusivität statt Voll-Exklusivität (S).
- [ ] Real-Estate-Anfragen nur als B2B-Konzeptvisualisierung. Bei VAE-Bezug Permit und Genehmigungen prüfen (6.1).
- [ ] Digitales Produkt erst nach Wartelisten-Schwelle; keine Umsatzversprechen im Marketing.

### 5.3 Test „Impossible places, possible furniture" (Teil 19/20, Hypothese aus Teil 18)

**Hypothese:** Eine unmögliche Architektur-Hülle, also Fantasy mit `adj` 2,10 (n=62) bzw. bei KI 2,27 (n=53), kombiniert mit 3–5 erkennbar realen, kaufbaren Möbel-Archetypen, verliert **nicht mehr als 20 % Reichweite (S)** gegenüber reiner Fantasy. Gleichzeitig erzeugt sie messbare Kaufabsicht (Keyword-Kommentare, Klicks).

**Warum die Daten das zulassen:** Kaufbarkeit zeigt unter den Top-Reels keinen nachweisbaren Reichweitenunterschied (p=0,83; bei KI p=0,27). Keyword-CTAs zeigen keinen nachweisbaren Reichweitennachteil (p=0,87) und gehen mit 6,6× bzw. bei KI 10× mehr Kommentaren pro View einher. Choice-Hooks gehen mit 5,7× mehr Kommentaren pro View einher. **Aber:** Das sind Korrelationen unter Top-Reels. Kausal testen wir es erst im eigenen Account.

**Design**

| Arm | Hülle | Interieur | CTA | Reels (mind.) |
|---|---|---|---|---|
| A (Kontrolle) | unmöglich (Fels, Klippe, Turm, unterirdisch) | generisch, nicht zuordenbar | Choice oder Frage, kein Link | 6 |
| B (Hybrid) | unmöglich | 3–5 klar lesbare Archetypen (z. B. Bouclé-Sessel, Travertin-Beistelltisch, Messing-Stehleuchte), **keine Marken** | Keyword → DM „closest real pieces (similar, not exact)" | 6 |
| C (Realistisch) | realistische Villa oder Terrasse | dieselben Archetypen | wie B | 6 |
| Optional D (Pick One) | 3 Varianten desselben Raums, eine davon mit realen Stücken | – | Choice plus Keyword | 6 |

- **Umfang:** 18–24 der 90 Launch-Reels (20–27 %), aufgeteilt auf P1/P2/P3. Reihenfolge über die Tage zufällig. Gleiche Slots und Lichtsignatur, damit nur das Interieur variiert.
- **Mindest-n und Entscheidungslogik** nach [15_kpi_framework.md](15_kpi_framework.md) (4.3/4.6): n ≥ 6 je Gruppe. Die Streuung innerhalb eines Accounts ist groß (SD log Views 1,38), deshalb lassen sich nur große Effekte erkennen, und Gewinner werden repliziert.
- **Produkt-Matching:** Zu jedem Archetyp per Google Lens, Amazon Lens, LTK Visual Search oder Spacely 1–3 reale Entsprechungen suchen. Liste mit „similar, not exact" und Preisstand-Datum. Keine Nachbildungen von Designklassikern ([q07](quellen/q07_legal_ai_risk.md)).

**Messgrößen**

| Messgröße | Definition | Quelle |
|---|---|---|
| Reichweite (primär) | `account_index` (views_24h ÷ Median der letzten 15 eigenen Reels) | App, [15](15_kpi_framework.md) |
| Kaufabsicht | Keyword-Kommentare pro 1.000 Views; DM-Öffnung → Link-Klick | App, DM-Tool |
| Klicks | Link-Klicks pro 1.000 Views (Sub-ID je Arm) | Redirect, Netzwerk |
| Qualität | Sends/Reach, F/1k (Follows pro 1.000 Views) | App |
| Reputation | Anteil negativer Kommentare mit „fake", „knockoff", „AI slop", „doesn't exist" (manuell codiert) | Kommentare |
| Umsatz (ab Monat 2) | EPC, RPM, Umsatz je Reel | Netzwerk ([15](15_kpi_framework.md), 3.7) |

**Entscheidungsregeln** (Schwellen S, anpassbar)

| Ergebnis | Bedingung | Folge |
|---|---|---|
| **SCALE Hybrid** | `account_index` B ≥ 0,8 × A **und** Klicks ≥ 1 pro 1.000 Views **und** negativer Anteil ≤ 5 % | B wird Standard für P2/P3; 30–40 % Commerce-Anteil wie im Brief |
| **ITERATE** | B zwischen 0,6 und 0,8 × A **oder** Klicks < 1 pro 1.000 Views bei guter Reichweite | Weniger oder anders platzierte Stücke, anderer CTA (Bio statt DM), andere Kategorie (Outdoor statt Wohnzimmer) |
| **KILL Hybrid** | Gruppen-Index < 0,6 ([15](15_kpi_framework.md)) **oder** negativer Anteil > 10 % | Fantasy bleibt „rein"; Monetarisierung über Tools und B2B (Rang 1–2) |
| **Realismus-Variante** | C ≥ B bei Klicks, aber C < 0,6 × A bei Reichweite | Commerce nur in P3-Transformationen, nicht in P1 |

### 5.4 Unit-Economics-Skizze (**ANNAHMEN, keine Prognose**)

**Formel:** RPM (USD pro 1.000 Views) = Klicks pro 1.000 Views × Conversion × Provision pro Bestellung (bzw. pro Abschluss). Das Basisszenario Möbel entspricht der Rechnung in [15_kpi_framework.md](15_kpi_framework.md) 3.8.

**Tabelle 5.4-A: Annahmen**

| Größe | Niedrig | Basis | Hoch | Herkunft |
|---|---|---|---|---|
| Klicks pro 1.000 Views | 0,5 | 2 | 5 | **S** (wird ab Tag 1 gemessen) |
| Conversion Möbel | 1,4 % | 1,4 % | 1,4 % | Referenz „~1,4 %" Home & Furniture, nur aus Snippets `[THIRD-PARTY / UNKNOWN]` |
| Provision pro Bestellung Möbel | 3 USD (Amazon) | 23,24 USD (Wayfair 7 % × 332) | 44 USD (Arhaus 4 % × 1.100) | 4.1 |
| Abschlussrate Tool (Klick → zahlendes Abo) | 1 % | 2 % | 4 % | **S** |
| Provision pro Tool-Abo | 15 USD | 15 USD | 15 USD | Runway `[VERIFIED]` |
| Sponsoring pro 1.000 Views (nur gesponserte Reels) | 5 USD | 9 USD | 20 USD | IMH-CPM-Untergrenze; usesnippet 9–20 `[THIRD-PARTY]` |
| B2B: Anfragen pro 1 Mio. Views × Abschluss × Projektwert | 1 × 20 % × 200 USD | 3 × 20 % × 1.000 USD | 10 × 20 % × 5.000 USD | Anfragen, Abschluss und Werte **S**; 200 USD = Untergrenze elarch.studio `[VERIFIED Listing]` |

**Tabelle 5.4-B: RPM je Einnahmequelle (USD pro 1.000 Views)**

| Einnahmequelle | Niedrig | Basis | Hoch | Bemerkung |
|---|---|---|---|---|
| Möbel-Affiliate | 0,02 | 0,65 | 3,08 | EPC-Gegencheck: 2 Klicks × 0,16–1,52 USD = 0,32–3,04 ([15](15_kpi_framework.md)) |
| KI-Tool-Affiliate (Runway-Logik) | 0,08 | 0,60 | 3,00 | ohne wiederkehrende Provisionen (Higgsfield bis 12 Monate: Planpreise UNKNOWN) |
| Sponsoring (nur auf gesponserte Reels) | 5 | 9 | 20 | gilt nur für die gesponserten Reels, nicht für alle Views |
| Pay-per-View (Ampere-Logik) | 1,50 | 1,50 | 1,50 | Cap 100 USD/Post, 1.000 USD/Monat `[THIRD-PARTY]` |
| B2B (auf Views umgelegt) | 0,04 | 0,60 | 10,00 | sehr ungleichmäßig; ein einziger Auftrag verändert alles |

**Tabelle 5.4-C: Monatsbeispiel** (Views/Monat = Ø Reel-Views laut Socialinsider H1 2026 × 90 Reels; Ø-Werte für Business-Accounts [q09](quellen/q09_reels_format_benchmarks.md) `[VERIFIED Quelle; Anwendung ESTIMATED]`; Möbel-Affiliate nur auf 35 % der Reels, der Mitte des Commerce-Anteils von 30–40 % im Brief; Beträge in USD, gerundet)

| Phase (Ø Views/Reel) | Views/Monat | Möbel-Affiliate (niedrig/Basis/hoch) | Tool-Affiliate | Sponsoring | B2B (niedrig/Basis/hoch) |
|---|---|---|---|---|---|
| 0–10K (658–1.035) | 59K–93K | ≈ 0 / 13–21 / 64–100 | 4–7 / 36–56 / 178–279 | nicht realistisch | Einzelfall |
| 10–50K (3.225) | 290K | 2 / 66 / 313 | 22 / 174 / 871 | 2 Reels: 58–129 (pro View) bzw. 200–1.000 (IMH micro pro Post) | 12 / 174 / 2.902 |
| 50–200K (4.915 als Untergrenze) | ≥ 442K | 3 / 101 / 477 | 33 / 265 / 1.327 | 3 Reels: 133–295 (pro View) bzw. 300–1.500 (IMH micro) | 18 / 265 / 4.424 |
| 200K+ (31.076, Stufe 100K–1M) | 2,8 Mio. | 21 / 637 / 3.015 | 210 / 1.678 / 8.391 | 4 Reels: 1.119–2.486 (pro View) bzw. 2.000–20.000 (IMH mid) | 112 / 1.678 / 27.968 |

Zusätzlich für Higgsfield Earn: 10–50 USD pro genehmigtem Video `[THIRD-PARTY]` × 8 Videos/Monat (S) ≈ 80–400 USD. Eine Follower-Schwelle nennen die Quellen nicht `[UNKNOWN]`; bezahlte Videos gelten als Werbung und müssen gekennzeichnet werden.

**Lesart:**

1. Unter 50K Followern bleibt **passiver Affiliate-Umsatz im niedrigen zwei- bis dreistelligen USD-Bereich pro Monat**, außer die Klickrate liegt deutlich über der Annahme.
2. **Ein einziger B2B-Auftrag über 1.000 USD entspricht ≈ 1,5 Mio. Views Möbel-Affiliate im Basisszenario.** Deshalb stehen B2B und Tools vor Möbeln.
3. Sponsoring bezahlt nur die gesponserten Reels. Pro-Post-Raten (IMH) und Pro-View-Benchmarks (usesnippet) weichen bei kleiner Reichweite stark voneinander ab. Gesichtslose Accounts dürften am unteren Rand verhandeln.
4. Die Durchschnittswerte von Socialinsider sind **keine Prognose** für uns. Die Strategie zielt auf Ausreißer, Views sind stark hit-getrieben ([q06](quellen/q06_ai_theme_page_case_studies.md)).

### 5.5 Angebotsbausteine und Beispieltexte (eigene Formulierungen, Englisch)

**B2B-Pakete** (Arbeitstitel; Preise sind Test-Variablen, da im Wettbewerb nicht veröffentlicht `[UNKNOWN]`)

| Paket | Zielkunde | Inhalt | Beleg für das Muster |
|---|---|---|---|
| **Concept Film** | Architekten, Design-Studios | 10–15 s Konzept-Reel eines ungebauten Entwurfs, Nachtlicht, menschlicher Maßstab, gekennzeichnet als Konzept | aiforarchitects, idw.design (Konzept-Disclaimer) |
| **Outdoor Preview Pack** | Landschafts- und Poolbauer | 3 Varianten (Choice-Format) einer Garten- oder Pool-Transformation als Verkaufshilfe | myplants.uae (*„AI-generated inspiration brought to life"*) |
| **Brand Scene** | Möbel-, Leuchten- und Deko-Marken | KI-Szenen rund um reale Produkte der Marke, mit Offenlegung | ai.perfect.world (KI-Werbevisuals) |
| **Unbuilt Estate** (nur Phase 50K+) | Projektentwickler (Off-Plan) | Stimmungsvisualisierung eines geplanten Projekts, ausdrücklich als Konzept, ohne Preis- oder Renditeaussagen | Compliance siehe 6.1 |

**Beispieltexte** (original; On-Screen- und Caption-Texte auf Englisch)

| Einsatz | Text |
|---|---|
| Hybrid-Hook (on-screen) | „The cliff is impossible. The armchair isn't." |
| Serien-Hook | „Unbuilt No. 031 — everything outside is fiction. Everything inside, you can find." |
| Choice plus Commerce | „Pick the one you'd move into: A, B or C? (C is built from real pieces.)" |
| Keyword-CTA (Caption) | „Comment PIECES and I'll DM you the closest real-world matches — similar, not exact." |
| Transformation | „Bare rock ledge → evening pool terrace. The loungers exist. The cliff doesn't." |
| Tool-Sponsoring | „Ad · Built with [Tool]: one sketch, three passes, one evening. Comment WORKFLOW for the breakdown." |
| B2B-Signatur | „Concept by [Studio]. Have an unbuilt project? We turn drawings into night-lit concept films — studio link in bio." |
| Newsletter | „Every Sunday: one house that shouldn't exist, the story behind it, and the real pieces inside. Link in bio." |

**Caption-Vorlage für ein Affiliate-Reel** (Kennzeichnung laut Abschnitt 6):

```
Werbung | Ad* · AI concept
The house can't exist. The lounge chair can.
Comment CHAIR and I'll send you 3 real pieces that come close (similar, not exact · prices as of 25 Sep 2026).
*Affiliate links: I earn a commission if you buy, at no extra cost to you. As an Amazon Associate I earn from qualifying purchases.
```

---

## 6. Recht und Kennzeichnung (Teil 20)

### 6.1 Pflichten-Matrix

| Situation | Pflicht bzw. Empfehlung | Quelle | Status |
|---|---|---|---|
| **Jeder monetarisierte Post (Betreiber in DE)** | Influencer mit Einnahmen betreiben ein Unternehmen, ihre Posts sind geschäftliche Handlungen. Beim Verlinken auf Hersteller liegt regelmäßig ein „werblicher Überschuss" vor. | BGH I ZR 90/20 u. a. ([q07](quellen/q07_legal_ai_risk.md)) | VERIFIED |
| **Affiliate-Link** | „Werbung" oder „Anzeige" als erstes Wort, erkennbar ohne Scrollen. **„#ad" allein reicht nach Auffassung der Landesmedienanstalten nicht.** Affiliate-Links mit `*` und Erläuterung direkt am Link, kein pauschaler Bio-Disclaimer. Instagram: Affiliate-Inhalte sollen das Label „Paid partnership" tragen (ohne Partner-Tag). | Leitfaden Medienanstalten 05/2025; Instagram-Hilfe ([q07](quellen/q07_legal_ai_risk.md)) | VERIFIED |
| Affiliate, US-Publikum | FTC: US-Recht gilt, wenn Folgen für US-Verbraucher absehbar sind. Offenlegung sichtbar, ohne „more" zu klicken, **im Video** und nicht nur in der Beschreibung. Plattform-Tools reichen allein nicht sicher aus. | FTC FAQ, Disclosures 101 | VERIFIED |
| Affiliate, UK-Publikum | „Ad" deutlich am Anfang; Kürzel wie „aff" oder „afflink" meiden; kein vager „some links might"-Hinweis | ASA/CAP 2023 | VERIFIED |
| **Amazon** | Pflichtsatz *„As an Amazon Associate I earn from qualifying purchases."* **Keine Provision über geboostete oder bezahlte Anzeigen** mit Amazon-Link. Linkverkürzer dürfen Amazon nicht verschleiern. Eigene Inhalte brauchen *„commentary, analysis or transformation"*. Produktbilder nur über die API. | Operating Agreement, Policies ([q02](quellen/q02_furniture_affiliate_commerce.md)) | VERIFIED |
| **LTK** | Keine täuschenden KI-Inhalte; Produktaussagen müssen *„reflect what someone could typically expect"*; Provisionen offenlegen; Exact-vs-Similar-Tagging nutzen | LTK Community Guidelines 18.03.2026 | VERIFIED |
| **Sponsoring (Tool-Deal)** | Label „Paid partnership" **und** Partner taggen; „Werbung/Ad" als erstes Wort. Wenn Werbung die Hauptrolle im Video spielt: Dauereinblendung „Werbung". Musik nur aus der Sound Collection oder lizenziert. Offenlegung nach ASA noch 12 Monate nach Ende der Beziehung fortführen. | Instagram-Hilfe, Medienanstalten, Meta Music Guidelines, ASA | VERIFIED |
| Bezahlte Videos (z. B. Higgsfield Earn) | Bezahlung pro Video ist eine Gegenleistung, also Werbung kennzeichnen. Nach § 5a Abs. 4 UWG wird die Gegenleistung vermutet. | § 5a UWG ([q07](quellen/q07_legal_ai_risk.md)) | VERIFIED Gesetz / Anwendung ESTIMATED |
| **KI-Kennzeichnung** | KI-VO Art. 50(4) gilt **seit 02.08.2026**. Wer aus der Nutzung regelmäßig wirtschaftlichen Nutzen zieht, ist Deployer. Das Label muss **bei der ersten Exposition** sichtbar sein; Metadaten oder Abspann reichen nicht. Auch realistische Gebäude und Objekte können Deepfakes sein. Bei kommerziellem Zweck greift die mildere Regel für „künstlerisch/fiktional" eher nicht. Bußgelder bis 15 Mio. € bzw. 3 % des Umsatzes (KMU-Verhältnismäßigkeit vorgesehen). Physikalisch unmögliche Szenen sind risikoärmer, ein Label setzen wir trotzdem immer. | EU-FAQ, Draft Guidelines ([q07](quellen/q07_legal_ai_risk.md)) | VERIFIED / Anwendung ESTIMATED |
| KI-Kennzeichnung auf Instagram | Fotorealistisches Video muss über das Meta-Tool offengelegt werden, sonst drohen Sanktionen. Provenienz-Signale (C2PA) nicht entfernen (Higgsfield-AGB). Accounts, die wiederholt fotorealistische KI-**Personen** prominent zeigen, werden ohne Profil-Label nicht empfohlen (kleine Figuren prüfen). | Meta, Instagram-Hilfe, Higgsfield ToS | VERIFIED |
| **Irreführung** | Keine Tatsachenbehauptungen über fiktive Objekte (*„$50M home in Dubai"*), schon gar nicht zusammen mit Affiliate- oder Sponsor-Links. „Similar, not exact" und Preisstand angeben. | § 5 UWG; KI-VO | VERIFIED Gesetz / ESTIMATED Anwendung |
| **Marken und Designs** | Keine Marken- oder Hotelnamen zur Beschreibung fiktiver Szenen (z. B. „Aman-inspired"), stattdessen Stilbegriffe. Keine erkennbaren Designklassiker, besonders nicht in einem „Dupe"-Kontext. Outputs auf halluzinierte Logos prüfen. Meta sperrt Accounts bei wiederholten IP-Verstößen. | § 14/§ 23 MarkenG, EuGH Mio/konektra, Meta IP Policy | VERIFIED / ESTIMATED |
| **Real Estate (VAE)** | Advertiser Permit Pflicht seit 01.02.2026, auch für Creator, die sich vorübergehend in den VAE aufhalten. Strafen AED 5.000–1.000.000. Immobilienwerbung braucht zusätzlich Vorabgenehmigung bzw. RERA- oder Trakheesi-Nummer (nur per Snippet belegt). Keine fiktiven Objekte als Angebot, keine Renditeaussagen. | [q03](quellen/q03_sponsors_brand_deals.md) | VERIFIED / Details UNKNOWN |
| Tool-AGB | Runway und Higgsfield erlauben kommerzielle Nutzung, Rechteklärung und Freistellung liegen aber beim Nutzer. Plan und Datum dokumentieren. | [q07](quellen/q07_legal_ai_risk.md) | VERIFIED |
| Durchsetzungsdruck | Im EU-Sweep 2024 (576 Influencer) hatten 97 % kommerzielle Inhalte, nur 20 % kennzeichneten systematisch; 358 wurden für weitere Prüfungen vorgemerkt. | EU-Kommission IP/24/708 | VERIFIED |
| Steuern, Gewerbe | nicht Teil der Quellen | – | UNKNOWN (Steuerberater) |

**Datenhinweis:** Offengelegte KI-Reels liegen bei `adj` 0,82× gegenüber nicht offengelegten (95-%-CI 0,58–1,18; p=0,15, **n. s.**; n=215 vs. 471). Die Kennzeichnung ist trotzdem **Pflicht und keine Option** (Brief, Abschnitt 5).

### 6.2 Pre-Publish-Checkliste für Commerce-Reels

- [ ] KI-Label im Bild ab Sekunde 0 **und** Meta-Tool „AI info" gesetzt; C2PA-Metadaten unverändert
- [ ] „Werbung | Ad" als erstes Wort der Caption; bei Sponsoring zusätzlich „Paid partnership" mit Partner-Tag; bei Affiliate „Paid partnership" ohne Tag
- [ ] Affiliate-Hinweis mit `*` direkt am Link bzw. in der DM-Nachricht; Amazon-Pflichtsatz, wenn Amazon verlinkt ist
- [ ] Links und DM-Liste mit „similar, not exact" und Preisstand-Datum
- [ ] Keine Preis- oder Ortsbehauptung zum fiktiven Objekt; kein Marken- oder Hotelname in der Szenenbeschreibung
- [ ] Keine erkennbaren Designklassiker, keine halluzinierten Logos
- [ ] Musik aus der Sound Collection oder lizenziert
- [ ] **Kein Boost** für Reels mit Amazon-Links; Boosts nur für Reels ohne Amazon-Bezug
- [ ] Sub-ID bzw. Code je Reel oder Serie hinterlegt ([15](15_kpi_framework.md), `affiliate_daily`)
- [ ] Mensch gibt jede Caption mit Affiliate-, Sponsor-, Orts- oder Preisbezug frei ([16](16_automation_strategy.md), G3)

---

## 7. Entscheidungsregeln (Kurzreferenz)

1. **Reihenfolge:** Tools → B2B → (Test) Möbel → digitale Produkte → Newsletter-Sponsoring → Real Estate (nur B2B). Diese Reihenfolge wird nur geändert, wenn eigene Daten aus 5.3 oder 5.4 sie widerlegen.
2. **Commerce-Anteil** höchstens 30–40 % der Reels (Brief). P1 „Impossible Homes" und P4 „Night Stories" bleiben commerce-frei, bis der Hybrid-Test SCALE ergibt.
3. **Keyword-Funnel stoppen**, wenn nach 6 Reels weniger als 1 Klick pro 1.000 Views zustande kommt (S) **oder** der Anteil negativer Kommentare über 10 % liegt (S).
4. **Tool-Deals nur mit Tools aus der eigenen Pipeline.** Wir werben nie für ein Tool, mit dem das gezeigte Reel nicht entstanden ist (Irreführung).
5. **B2B-Anfrage vor Affiliate-Link:** Bei knapper Bio-Fläche gewinnt der Studio-Link (5.4, Lesart 2).
6. **Keine bezahlte Reichweite** für Amazon-verlinkte Inhalte. Boost-Budget fließt nur in B2B-Portfolio-Reels ohne Amazon-Bezug.
7. **Real-Estate-Anfragen:** ablehnen, wenn fiktive Objekte als real vermarktet werden sollen oder Renditeversprechen verlangt werden. Bei VAE-Bezug gilt: ohne Permit-Klärung keine Veröffentlichung.

---

## 8. Offene Punkte (UNKNOWN, zu verifizieren)

1. Instagram-Affiliate-Produkt-Tags in Deutschland bzw. für den Markt des Accounts ([q01](quellen/q01_instagram_platform_rules.md)); Mindestfollower nur aus Snippets bekannt.
2. Konditionen von Amazon.de (Sätze, Pflichtsatz) und Zugang zu amazon.com Associates für einen Betreiber mit Sitz in Deutschland.
3. Haltung von LTK und ShopMy zu KI-generierten Räumen mit „similar"-Tagging (Zulassung, Durchsetzung der Guidelines).
4. Planpreise von Higgsfield (für wiederkehrende Provisionen) und die tatsächliche Auszahlungsmechanik von Higgsfield Earn (Einladung vs. offen; widersprüchlich).
5. Ob die Wayfair-Links von roomify.design Affiliate-Links sind und wie deren Konversion ausfällt.
6. Echte Umsätze irgendeines KI-Interior-Accounts: keiner verifiziert.
7. Die Instagram-Bios der 72 Accounts und ihre Paid-Partnership-Labels (in der Profil-Session nicht erhoben). Fehlende Belege können daher Lücken in der Erhebung sein.
8. Ob Meta-Labels die Offenlegungspflicht nach Art. 50 KI-VO erfüllen (keine Quelle sagt das).

---

## Quellen

- **Daten:** [analysis_digest.md](data/processed/analysis_digest.md) (Abschnitte 1, 3 „CTA type"/„Shoppability"/„Account type", 5, 7, 9, „Key contrasts", „Coding reliability"); [monetization_accounts.csv](data/processed/stats/monetization_accounts.csv), [monetization_summary.csv](data/processed/stats/monetization_summary.csv), [monetization_contrasts.csv](data/processed/stats/monetization_contrasts.csv) (erzeugt mit [scripts/monetization_stats.py](scripts/monetization_stats.py)); [02_competitor_database.csv](02_competitor_database.csv); `data/raw/accounts/profile_*.json` (72 Profile, Stand 25.09.2026); [strategy_brief.md](data/processed/strategy_brief.md).
- **Quellennotizen:**
  - [q01](quellen/q01_instagram_platform_rules.md): Shopping, Links, Monetarisierungsprogramme, Policies
  - [q02](quellen/q02_furniture_affiliate_commerce.md): Amazon, LTK, ShopMy, Händlerprogramme, visuelle Suche, KI-Commerce-Mechanik
  - [q03](quellen/q03_sponsors_brand_deals.md): KI-Tool-Programme, Möbelmarken, Immobilien, Preisbenchmarks, Markenhaltung zu KI
  - [q04](quellen/q04_interior_trends_demand.md): Markt für KI-Interior-Apps, Designer-KI-Nutzung
  - [q06](quellen/q06_ai_theme_page_case_studies.md): Fallstudien, Einkommensbehauptungen, Gegenbelege
  - [q07](quellen/q07_legal_ai_risk.md): KI-VO Art. 50, UWG, Werbekennzeichnung, Marken, Musik, Tool-AGB
  - [q08](quellen/q08_cross_platform_signals.md): YouTube-Monetarisierung und RPM (Proxy)
  - [q09](quellen/q09_reels_format_benchmarks.md): Reel-Views nach Follower-Stufe (Socialinsider)
- **Verknüpfte Kapitel:** [15_kpi_framework.md](15_kpi_framework.md) (Commerce-KPIs 3.7, RPM-Rechnung 3.8, Entscheidungsregeln 4), [16_automation_strategy.md](16_automation_strategy.md) (Freigabe-Gates, Compliance-Linter).
