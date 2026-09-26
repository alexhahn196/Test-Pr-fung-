# I – Konkurrenz- & Case-Study-Datenbank: Home-/Lifestyle-Nischen

**Studie:** Welche Nische + Markt eignet sich für eine KI-generierte, faceless Instagram-Reels-Theme-Page mit Affiliate-Monetarisierung (Content → Reichweite → Link in Bio → Affiliate-Kauf)?
**Teilbereich:** Home/Lifestyle (Interior/Home Decor inkl. Luxury Homes & AI Architecture/Interior, Möbel, Smart Home, Küche, Kaffee, Garten/Outdoor/Pool/BBQ, Cleaning/Organization, Haustiere, Baby/Parenting, Schlaf, allgemeine „Amazon (Home) Finds“), jeweils EN und DE/DACH.
**Prüfdatum:** 2026-09-26
**Rohdaten:** `raw_competitors_home.csv` (95 Accounts, 27 Spalten)

---

## 0. Kurzfazit

| Kennzahl | Wert |
|---|---|
| Accounts in der Datenbank | **95** (72 Instagram, 23 YouTube Shorts; TikTok-/Threads-/Pinterest-Daten als Zusatzinfo in den Notizen) |
| davon deutschsprachig | **26** |
| Accounts mit belegtem Affiliate-Modell (= Case Studies) | **32** (davon 17 Theme-/Marken-Accounts ohne Person im Vordergrund – inkl. Justice Buys auf IG und YT separat – und 15 personengeführte Vergleichsfälle) |
| Affiliate „ja“ / „nein“ / „unklar“ / „wahrscheinlich“ | 35 / 31 / 27 / 2 |
| Größenklassen | 1M+: 30 · 500k–1M: 29 · 100k–500k: 21 · 10k–100k: 14 · <10k: 1 |

**Kernaussagen**

1. **Das Modell ist im EN-Markt belegt** – am deutlichsten bei *Amazon Home Finds / Home Decor* (trendyhomefinds1, divaa.finds, stylerior, home.interior1, cool_amazon_homefinds), *Küchen-/Home-Gadgets* (Justice Buys), *Organization* (thatorganizedhome) und *Haustiere* (round.boys, dogsofinstagram, Sathi Mart). Die Nachweise sind Amazon-Storefronts mit Associate-Tag, Linktree-Seiten mit Amazon-Disclosure oder Walmart-/Impact-Links.
2. **Viele große Theme-Pages monetarisieren anders:** über einen eigenen Shop bzw. Dropshipping (myhousesdecors 4,1 Mio., @dog, niopets1, Worldwide Gadgets, Pawmemories), über bezahlte Link-Platzierungen (catsofinstagram), über Shoutouts (pitbullz_zone), über Kurse (d.signers, parametric.architecture) oder über Lead-Gen (beautyofhouses). Affiliate ist also nur *ein* Modell unter mehreren.
3. **AI-Interior-/Architektur-Pages erreichen sehr viele Menschen, nutzen aber kein Produkt-Affiliate.** Belegt für Dreamy Interior (315k Abos, AI), Kou Yang AI, Jeremiah Carter, UnrealLife, Bau Rausch (DE, 620k) und midjourney.architecture. Wenn sie Geld verdienen, dann über App-Referrals (Isla → RenoMuse), Workshops/Promotions, E-Books (Home Graphix) oder den Shorts-Fonds.
4. **DE-Markt:** Wir haben **keine einzige deutschsprachige, faceless „Amazon (Home) Finds“-Theme-Page mit mehr als 100k Followern gefunden.** Affiliate läuft in DE über Personen-Creator mit Amazon.de-Storefront (mi.interieur, dekokrams, villa_karole, cima.villa, homestory_pictures, landhaus_garten), über Deal-Pages mit Story-Format (dealbunny.de 987k, mydealz.de 546k) und über DIY-Tool-Shorts (Malerart). Weil die Recherche methodisch eingeschränkt war (siehe Abschnitt 1), heißt das nur „nicht gefunden“, nicht „existiert nicht“.
5. **Die größte Ineffizienz:** Sehr viel Reichweite läuft ohne Kauflink. Beispiele sind Smart Design (4,37 Mrd. Views, Klappmöbel-Konzepte), CraftWorks (Garten-DIY), CrazyClean01 (Cleaning-ASMR), Herr Zogg (DE-Haushaltshacks, Median 775k), Daily latte art (Maschine im Bild) sowie IG-Pages wie homeinspirehacks (2,3 Mio.), smart_tech.__ (2,6 Mio.), design.only (2,7 Mio.) und baristadaily (886k).

---

## 1. Methodik & Grenzen

### 1.1 Vorgehen
1. **Discovery (Kandidaten finden)**
   - Rankings: orbitvibe.com (IG Home Decor, Pets, Real Estate, Tech, Shopping), HypeAuditor-Top-50 (DIY & Design DE/US, Shopping & Retail DE, Animals DE, Food & Cooking DE, Computers & Gadgets DE), Pikory (Home Decor).
   - NexLev-Shorts-Nischensuche mit semantischen Queries: AI-Interior/Architektur, Amazon Home Finds, Kaffee, Pets, Garten/Pool/BBQ, deutsche Amazon-Funde.
   - Gezielte Prüfung plausibler Handles (z. B. `amazonpetfinds`, `kitchengadgets`, `dealbunny.de`).
   - WebSearch-Snippets, **nur für die ersten Abfragen**: Das Sitzungsbudget für WebSearch war erschöpft (Limit 200, geteilt mit anderen Agenten). Ab da wurde ohne Suchmaschine gearbeitet; Bing, DDG, Yahoo, Startpage und Brave blockieren automatisierte Abfragen.
2. **Existenz & Follower**
   - Instagram selbst ist per Login-Wall bzw. 302/429 gesperrt.
   - Follower und Postzahl stammen deshalb aus dem Cache von *insta-stories-viewer.com*, aus orbitvibe, HypeAuditor, Pikory, Threads-Profilmeta und WebSearch-Snippets. Datenqualität: **ESTIMATED**.
   - YouTube-Abos aus `youtube_channel_about` (NexLev → YouTube) gelten als **VERIFIED**. TikTok-Werte aus dem SSR-JSON der Profilseite ebenfalls als **VERIFIED**.
3. **Affiliate-Nachweis (Primärquellen)**
   - **Linktree:** Das `__NEXT_DATA__`-JSON wurde ausgelesen (Link-Typen wie AMAZON_SHOP/AMAZON_PRODUCT, Domains, Beschreibung, verknüpfte Social-Profile).
   - **Amazon-Storefronts:** `amazon.com/shop/<handle>` und `amazon.de/shop/<handle>`, jeweils mit Titel und **Associate-Tag** (`'tag': 'xyz-20/-21'`) aus dem Seitenquelltext.
   - **Weitere Quellen:** LTK-Explore-Seite, Websites (Disclosure-Texte, z. B. dealbunny.de, justicebuys.com), YouTube-Kanal-Links.
   - Wenn Instagram-Account und Linktree/Storefront nur über den gleichen Handle verbunden sind (also keine gegenseitige Verlinkung besteht), steht das in `notizen` bzw. `affiliate_nachweis`.
4. **Views**
   - Für Instagram sind Views praktisch nicht öffentlich abrufbar.
   - Einzelne Reel-*Likes* ließen sich über die Meta-Tags mit Crawler-User-Agent auslesen (VERIFIED, nur Stichproben).
   - Median-/Top-Views für YouTube Shorts stammen aus der NexLev-Datenbank (ESTIMATED).
5. **Format-Check:** Ein Reel (divaa.finds) wurde mit dem NexLev-Videoanalyse-Tool angesehen. Die zurückgegebenen Metadaten widersprachen den Instagram-Meta-Daten; das Ergebnis wird deshalb nur qualitativ genutzt.

### 1.2 Datenqualitäts-Definitionen
- **VERIFIED:** direkt auf Plattform/Primärquelle gesehen (Linktree-JSON, Amazon-Storefront inkl. Tag, TikTok-Profil-JSON, YouTube-About, IG-Reel-Meta-Likes, Website-Disclosure).
- **ESTIMATED:** Drittanbieter (Viewer-Cache, orbitvibe, HypeAuditor, Pikory, Threads-Follower, NexLev-Views), Suchsnippets.
- **UNKNOWN:** nicht bestimmbar.
- **CLAIMED:** Selbstangaben der Accounts (z. B. „1M on Instagram“).

### 1.3 Grenzen / Bias
- **Größen-Bias:** Die Discovery über Rankings bevorzugt große Accounts. Kleine Pages (10k–100k) sind unterrepräsentiert (14 Einträge). Ohne Hashtag-Suche lassen sich neue, schnell wachsende kleine Pages kaum finden.
- **Follower-Diskrepanzen** zwischen den Quellen sind teils erheblich und in `notizen` dokumentiert:
  - myhousesdecors: 4,1 Mio. (Viewer) vs. 1,5 Mio. (orbitvibe)
  - trendyhomefinds1: 1,3 Mio. vs. 2 Mio. (Snippet)
  - thatorganizedhome: 417k vs. 875k
  - homecraft.designer: 2,5 Mio. vs. 4,1 Mio.
- **Link-in-Bio-Lücke:** Beacons, lnk.bio und solo.to sind per Cloudflare gesperrt. Pages, die solche Dienste oder direkte Links nutzen, erscheinen als „unklar“, obwohl sie womöglich Affiliate nutzen. Die Zahl der Affiliate-Nutzer ist daher eine **Untergrenze**.
- **Faceless-Status** ist meist aus Bio/Format abgeleitet (Repost-Hinweise wie „DM for credit/removal“), nicht durch Ansehen der Videos.
- **DE-Discovery** ist am schwächsten: Es gibt keine DE-Suche und nur wenige HypeAuditor-DE-Listen. Die Aussage „keine DE-Finds-Theme-Page >100k“ ist deshalb ein Befund mit mittlerer Sicherheit.

---

## 2. Befunde je Nische (EN vs. DE)

### 2.1 Interior / Home Decor / „Amazon Home Finds“
**EN: stark besetzt, Modell belegt.**
- **Große Theme-Pages mit >1 Mio. Followern:** d.signers (4,4 Mio.), myhousesdecors (4,1 Mio.), design.only (2,7 Mio.), the_real_houses_of_ig (2,5 Mio.), homeinspirehacks (2,3 Mio.), noruxhome (1,6 Mio.), trendyhomefinds1, home.interior1 und glam_style_living_ (je ~1,3 Mio.).
- **Affiliate belegt:** trendyhomefinds1, divaa.finds, stylerior, home.interior1, glam_style_living_, d.signers, cool_amazon_homefinds (89k).
- **Andere Monetarisierung:** myhousesdecors nutzt einen Eigenshop; homeinspirehacks, homedecoration330, myhouselooks und design.only zeigen keinen Nachweis.
- **Personen-Benchmarks:** jodie.thedesigntwins (2,3 Mio., Amazon + LTK, „All links earn commission“), decor.snippets (3,1 Mio.), toponlinefinds (528k).
- **Wiederkehrende Muster:**
  - Repost-/Kurationsseiten mit Hinweisen wie „DM for credit/removal“.
  - Instagram-native Pages: Die TikTok-Präsenz ist fast null (trendyhomefinds1 55, divaa.finds 133, stylerior 2, homeinspirehacks 1.455 TikTok-Follower).
  - Zweites Affiliate-Programm neben Amazon: Temu (divaa.finds, stylerior).

**DE: kaum Theme-Pages.**
- Die Top-Liste wird von Händlern (westwingde 1,8 Mio., ikeadeutschland 1,5 Mio.) und Personen-Creatorinnen dominiert: mi.interieur 1,3 Mio., haus_plan_b 1,2 Mio., homestory_pictures 765k, homeheartmade 704k, dekokrams 530k, villa_karole 440k, cima.villa 400k.
- **Sechs dieser Personen haben eine Amazon.de-Storefront mit Associate-Tag.** Affiliate ist in DE also etabliert, aber personengebunden.
- Einzige Community-/Theme-Accounts: solebich (548k, Plattform, kein Affiliate-Nachweis) und inspowelt__ (321k, „Dauerwerbung“, also bezahlte Promos).
- interiorby_selinda (113k, Person) betreibt eine „Home Finds“-Linkliste mit 52 Links (Amazon + Temu). Das kommt dem Finds-Format in DE am nächsten.

### 2.2 Luxury Homes
**EN:** zahlreiche große Theme-Pages: zillowgonewild 2,3 Mio., luxury_homes 1,3 Mio., themillionaires_mindset 854k, mansionsonig 827k, housesofcelebs 659k, beautyofhouses 610k, millionaire_homes 421k.
- **Kein einziger Produkt-Affiliate-Nachweis.** Stattdessen: Lead-Gen (beautyofhouses, „Powered by KEYLEAD“), Newsletter (mansionsonig), eigenes Spiel/Brand Deals (zillowgonewild), Makler-Umfeld (luxury_homes).
- Grund: Das Hauptobjekt (die Immobilie) ist nicht per Affiliate kaufbar.

**DE:** keine Luxury-Theme-Page gefunden.

### 2.3 AI Architecture / AI Interior
**EN:** Reichweite ist klar belegt.
- Dreamy Interior: 315k Abos, Median ~580k Views, AI-Raum-Makeovers.
- Kou Yang AI: 72k Abos, Median ~623k.
- Jeremiah Carter: 100k Abos, AI-Backyard.
- UnrealLife: 95k Abos, „Choose your dream bedroom“.
- Adam Smart Home: 17k Abos, AI, Median ~270k.
- midjourney.architecture: 162k auf IG.
- Smart Design (2,13 Mio., Median 28 Mio.) nutzt laut eigener Beschreibung AI-Visualisierung; NexLev stuft den Kanal als 3D-Animation ein.

**Affiliate: nirgends.** Die Monetarisierung läuft so:
- App-Referral: Isla → go.renomuse.com.
- Workshops/Promotions: midjourney.architecture → Nordfy-AI-Workshop, RD Studio.
- E-Book: Home Graphix → homedesignbook.com.
- AI-Tool-Links: Smart Design, UnrealLife.
- Sonst Shorts-Fonds/AdSense. NexLev schätzt z. B. Dreamy Interior auf ~15k USD Lebenszeit-AdSense.

**DE:** Bau Rausch (620k Abos in ~5 Monaten, Median 1,2 Mio., AI-Timelapse-Bauten „[KI-Konzept]“) ist der stärkste DE-AI-Beleg im Sample, hat aber **keine Affiliate-Links**.

### 2.4 Möbel / Smart Home / Home-Gadgets
**EN:**
- **Justice Buys** ist der Referenzfall (Details in Abschnitt 3).
- Worldwide Gadgets (484k YT, Median 3,65 Mio.) nutzt dasselbe Format mit „🔗 Link in Bio“ im Titel, monetarisiert aber über einen **Eigenshop mit Rabattcode**.
- smart_tech.__ (2,6 Mio. IG, Repost) ohne Nachweis.
- LifeHacks_DreamBuilding und Adam Smart Home ohne Links.
- Affiliate-Media-Marken: uncrate (Storefront, Tag `uncrate-20`), coolmaterial (Shop/Deals), thisiswhyimbroke (IG klein, Website-first).

**DE:** keine Smart-Home-Theme-Page gefunden. Die HypeAuditor-Liste „Computers & Gadgets DE“ enthält nur Gaming, Hardware und Industrie.

### 2.5 Küche / Küchengadgets
**EN:** Justice Buys („BEST Amazon Kitchen Gadgets“ 81 Mio. Views). Auf Linktree existieren Handles wie `kitchengadgets` (Storefront „Kitchen Gadgets“, Tag `josuerodrig05-20`) und `kitchenhacks` (amzn.to). Die zugehörigen IG-Accounts ließen sich aber nicht verifizieren; sie sind deshalb **nicht** in der CSV.

**DE:** Die Küchen-Nische ist rezeptgetrieben (chefkoch 785k; HypeAuditor-Food-DE nur Koch-Creator). Herr Zogg (DE-Haushalts-/Küchenhacks, 60k Abos, **Median 775k**, Outlier-Score 3,7) hat keine Links. **Einen DE-Küchengadget-Affiliate-Account haben wir nicht gefunden.**

### 2.6 Kaffee / Espresso-Setups
**EN:**
- baristadaily (886k) ist die größte Kaffee-Theme-Page. Die Bio sagt „Shop Coffee Gear Below 👇“, das Linkziel war nicht ermittelbar; „Get Featured“ deutet auf bezahlte Features.
- Daily latte art (12k YT, ein Viral-Hit mit 27 Mio.) zeigt die DeLonghi Dedica im Bild, **ohne Affiliate-Link**.
- Die Storefront `amazon.com/shop/coffeegeek` gehört Mark Prince (CoffeeGeek, Tag `coffeekid-20`). Ein verknüpfter IG-Account wurde nicht verifiziert, daher nicht in der CSV.

**DE:** nichts gefunden (Datenlücke).

### 2.7 Garten / Outdoor Living / Pool / BBQ
**EN:**
- YouTube: CraftWorks (401k, Median 1,1 Mio., Backyard-Pond 112 Mio.) und Jeremiah Carter (AI) – beide ohne Affiliate.
- Instagram-Benchmark: gardenwithjonny (2,1 Mio., Person; Buch + Rabattcode).
- **Keine EN-IG-Garten/BBQ/Pool-Theme-Page mit Affiliate gefunden.**

**DE:** Personen mit Amazon-Affiliate: landhaus_garten (488k, Storefront), stillers.home (556k; Beatbot-Poolroboter über amzn.to plus Marken-Kooperation), cima.villa (Gartenprojekte). Dazu das Magazin mein_schoener_garten (910k).

### 2.8 Cleaning / Home Organization
**EN:**
- thatorganizedhome (417k): „Shop now“ plus Storefront, Theme-/Marken-Page.
- thehomeedit (6,2 Mio.): der Benchmark für einen Multi-Netzwerk-Stack aus Amazon, LTK, Rakuten und CJ, aber personengeführt.
- anna_louisa_at_home (4,4 Mio., Person, Storefront).
- CrazyClean01 (234k YT, Top 139 Mio.): ohne Links. Der Titel „It costs $450 on Amazon and I paid $15“ zeigt Produktbezug, der nicht monetarisiert wird.

**DE:** keine Cleaning-Theme-Page gefunden.

### 2.9 Haustiere
**EN: das zweitbeste Belegfeld.**
- round.boys (1,1 Mio.): „we own no content posted“, also eine Repost-Page, plus Amazon-Storefront „Pet Essentials“ und Merch.
- dogsofinstagram (5,6 Mio.): Storefront-Tag `greatpetcare-20`, also betrieben von einer Pet-Media-Firma.
- Sathi Mart (25k YT): 28 amzn.to-Links, CTA „Link in my profile“.
- **Weitere Pet-Modelle:**
  - catsofinstagram: bezahlte Link-Placements, erkennbar an `utm_medium=themepage`.
  - Eigenshops: @dog (shopdog.com), niopets1, Pawmemories, SnuggoPaws.
  - Shoutouts: pitbullz_zone.
  - Netzwerk-Werbung: cutest.farm.

**DE:** daniel.labbi (200k, Person, Impact-Affiliate über pxf.io plus Eigenprodukt), gnocchi.thekitten (124k, Pet-Persona, kein Nachweis), katze.schatz (YT 24k, Memes, keine Links).

### 2.10 Baby / Parenting
- **EN:** Nur Kontext – babylist (Registry-Marke mit Storefront) und Hasnan Hafid (505k YT „3 coolest baby gadgets“, keine Links geprüft). **Keine EN-Baby-Finds-Theme-Page verifiziert** (Linktree `amazonbabyfinds`/`babyfinds` existieren, IG-Zuordnung nicht belegt).
- **DE:** **echtemamas** (526k, Mütter-Community, Amazon.de-Storefront Tag `echmam-21`) ist der einzige DE-Baby-Account mit belegtem Affiliate.

### 2.11 Schlaf
Einzig UnrealLife (AI, „Choose your dream bedroom“) und divaa.finds (Cozy Bedroom/Vanity). **Keine dedizierte Sleep-Theme-Page gefunden, weder EN noch DE** (Datenlücke).

### 2.12 Allgemeine „Amazon Finds“ und Deals
- **EN:** Amazon selbst besetzt das Feld (amazonhome 5,7 Mio., amazonfinds 403k). Kleine Pages wie onlinee_finds (18k, 2,8k Posts, 887 Likes/Post) zeigen die Sättigung am unteren Ende.
- **DE:** Die „Finds“-Energie läuft über **Deal-Pages im Story-Format**:
  - dealbunny.de (988k): Website mit Affiliate-Disclosure.
  - mydealz.de (546k): Deal-Plattform.
  - shoppaholic (802k): personengeführt („Rabiosa x Shoppaholic“), Amazon.de-Storefront.

---

## 3. Case Studies (ausführlich)

> Auswahl: die Theme-/Marken-Pages ohne Person im Vordergrund zuerst, danach die personengeführten Vergleichsfälle gebündelt. Alle Nachweise wurden am 2026-09-26 abgerufen.

### CS1 – trendyhomefinds1 (IG, EN, ~1,3 Mio.)
- **Modell:** Home-Decor-Produkt-Reels („Products you didn’t know you needed“) → Linktree mit 25+ Amazon-Produkten, sortiert nach Raum/Zweck (Deko, Bett, Bad, Küche).
- **Nachweis:** Linktree-Beschreibung „✨ Curated home finds 🏡 | Amazon favorites 🛒 … **As an Amazon Associate I earn from qualifying purchases.**“ Die Links sind amzn.to bzw. `amazon.com/dp/…&tag=tiktok2025000-20`.
- **Lernen:**
  - Ohne Storefront reicht eine kuratierte Linkliste mit Associate-Disclosure.
  - Die Linkliste funktioniert wie ein „Katalog“ zu den Reels.
  - Kaum TikTok-Präsenz (55 Follower) → reine IG-Strategie.
  - Die Follower-Zahlen widersprechen sich (1,3 vs. 2 Mio.). Hinweis auf Volatilität bzw. Datenstand.

### CS2 – divaa.finds (IG, EN/US, ~774k)
- **Modell:** Cozy-Room-/Vanity-Reels mit dem Hook „Shop my faves & makeover must-haves“ → Linktree → Amazon-Storefront plus Temu plus eigener Shop (divafinds.us).
- **Nachweis:** Linktree verlinkt instagram.com/divaa.finds. Link „Diva’s Amazon Storefront“ → amazon.com/shop/divaaa.finds (Tag `gamecraft07-20`); Produktlinks mit gleichem Tag; „Diva’s Temu | Fav Picks“.
- **Reel-Stichprobe:** 3.815 bzw. 3.649 Likes je Reel (VERIFIED). Bei 774k Followern entspricht das rund 0,5 % Like-Rate, also ein eher schwaches Engagement.
- **Lernen:** Drei Einnahmekanäle parallel (Amazon, Temu, Eigenshop). Die Nische „Aesthetic Bedroom/Vanity“ verbindet Schlaf-/Bedroom- und Beauty-Kaufintention. Die Videoanalyse deutet auf Reposts fremder Creator mit Keyword-Kommentar-CTA hin. Das ist rechtlich riskant (Urheberrecht), für eine AI-Page aber vermeidbar.

### CS3 – stylerior (IG, EN, ~670k)
- **Modell:** Interior-Inspiration → Linktree → Amazon-Storefront, die unter anderem Namen läuft (`urban.homedesign`, Tag `urbanhomedesi-20`), plus Temu-Deals.
- **Nachweis:** Linktree (mit IG-Verknüpfung) → „Amazon Storefront“ → Seitentitel „Stylerior’s Amazon Page“.
- **Lernen:** Eine Storefront kann markenneutral benannt sein und von mehreren Pages bespielt werden; das ist netzwerkfähig.

### CS4 – home.interior1 (IG, EN, ~1,3 Mio.)
- **Modell:** Kuratierte Modern-Interior-Posts → Storefront (Tag `homeinterior1-20`) plus eigenes digitales Produkt („Simple routines for an always-clean home“ auf homeinterior1.com).
- **Lernen:** Kombination aus Affiliate und eigenem Info-Produkt. Die Interior-Inspirations-Audience wird über ein Cleaning-/Routine-Produkt monetarisiert, eine Brücke in eine Nachbarnische.

### CS5 – cool_amazon_homefinds (IG, EN, ~89k, 2.555 Posts)
- **Modell:** Klassische Amazon-Home-Finds-Page → Storefront (Titel „Chamli Nawod Shops’s Amazon Page“, Tag `ndaamazon1220-20`).
- **Lernen:** Auch unter 100k gibt es eine aktive Storefront. Der Betreibername deutet auf einen Offshore-Betreiber einer reinen Theme-Page. Die sehr hohe Postzahl bei moderater Followerzahl zeigt: Volumen allein skaliert nicht.

### CS6 – thatorganizedhome (IG, EN/UK, ~417k; orbitvibe 875k)
- **Modell:** Organizing-, Decluttering- und Storage-Tipps → „Shop now🔽“ → Storefront (Tag `thatorganiz02-20`).
- **Lernen:** Cleaning/Organization hat eine **eingebaute Produktlogik** (Boxen, Körbe, Regale). Anders als bei AI-Interior ist jedes gezeigte Objekt kaufbar.

### CS7 – Justice Buys (IG `justice_buys` ~616k; YT `@justicebuys1` 2,13 Mio.; TikTok `@justicebuys` 1,5 Mio.)
- **Modell:** Faceless Produktreview-/Kompilations-Shorts (Küche, Home, Tech) → Linktree bzw. Website justicebuys.com („All products are linked“).
- **Nachweis:**
  - Linktree: „**As an affiliate, I earn from qualifying purchases.**“, 20 × goto.walmart.com (Walmart Creator), Impact-Links (sjv.io, pxf.io).
  - Website: amzn.to-Links und amazon.com-Links mit `maas`-Attribution.
- **Zahlen:**
  - YT: Median 26,5 Mio. Views, Top 81 Mio. („BEST Amazon Kitchen Gadgets“), 1,91 Mrd. Kanal-Views (VERIFIED).
  - AdSense-Schätzung (NexLev) ~191k USD Lebenszeit, **exklusive** Affiliate.
  - Management durch die Agentur Undercurrent.
- **Lernen:**
  - Das professionellste Beispiel im Sample.
  - Plattform-übergreifend (IG, YT, TikTok, FB) mit einer zentralen Link-Website statt einer Storefront.
  - **Mehrere Händlerprogramme** (Amazon, Walmart, Impact-Marken) reduzieren die Abhängigkeit von Amazon.
  - Küchengadgets sind „impulskauffähig“ und demonstrierbar.

### CS8 – uncrate (IG, EN/US, ~141k)
- **Modell:** Affiliate-Media-Marke (seit 2005) mit Produktfotos; Storefront mit Tag `uncrate-20`.
- **Lernen:** Etablierte Affiliate-Publisher nutzen Instagram nur als Nebenkanal. Das Geld kommt über die Website bzw. die Storefront.

### CS9 – round.boys (IG, EN/US, ~1,1 Mio.)
- **Modell:** Repost-Tierclips („we own no content posted. Dm for removal!“) → Linktree → „Pet Essentials for your Round Boys/Girls“ = amazon.com/shop/round.boys (Tag `noahperiord-20`) plus Merch.
- **Lernen:** Das klarste Beispiel für das Zielmodell in der Pet-Nische: faceless, reiner Unterhaltungscontent, Monetarisierung über eine thematisch passende Storefront. Die Conversion hängt nicht am einzelnen Video, sondern an der Community-Identität.

### CS10 – dogsofinstagram (IG, EN/US, ~5,6 Mio.)
- **Modell:** UGC-Feature-Page → Linktree (Spenden, Gewinnspiele, Rabattcode-Partner) plus Storefront (Tag `greatpetcare-20`).
- **Lernen:** Ein Premium-Handle wird von einem Pet-Media-Unternehmen betrieben (der Tag deutet auf „GreatPetCare“). Große Theme-Pages sind oft **Assets von Media-Firmen**, keine Solo-Projekte.

### CS11 – Sathi Mart (YT, EN, 25,5k Abos)
- **Modell:** Faceless Produktdemos mit Titel-CTA „Get this … – Link in my profile!“ → Linktree mit 28 amzn.to- und 5 link.amazon-Links.
- **Zahlen:** Median 39k, Top 35 Mio. (Interactive Cat Water Mat), ~11 Uploads/Woche.
- **Lernen:** Kleinkanäle können über **Viral-Ausreißer** ernten. Das Format „Produkt zeigen + Link-CTA im Titel“ ist nischenübergreifend (Pet, Beauty, Haushalt).

### CS12 – dealbunny.de (IG, DE, ~988k)
- **Modell:** Tägliche Deals in **Stories** („Täglich Storys schauen & Geld sparen“) → Website/App.
- **Nachweis:** dealbunny.de: „Diese Website enthält Affiliate-Links, für die ich möglicherweise eine Vergütung erhalte … kann dies dazu führen, dass diese Website eine Provision erhält.“
- **Lernen:** Die größte DE-Affiliate-Theme-Page im Sample ist eine **Deal**-Page, keine Inspirations-Page. Conversion läuft über Stories mit Link-Sticker statt über Reels plus Link in Bio.
- **Achtung:** linktr.ee/dealbunny.de ist eine fremde Scam-Seite.

### CS13 – echtemamas (IG, DE, ~526k)
- **Modell:** Mütter-Community-Content → Amazon.de-Storefront (Tag `echmam-21`).
- **Lernen:** Auch in DE funktioniert Community + Storefront. In Baby/Parenting ist die Kaufintention hoch, und das Vertrauen in eine „Community-Marke“ ersetzt das Gesicht.

### CS14 – Malerart (YT DE 461k; TikTok 508k; IG `malerart_` 89k)
- **Modell:** Maler-Lifehacks und Wall-Art (Hände im Bild) → Linktree mit Amazon.de-Produkten (Tags `malerart2107-21`, `malerart0c-21`): Werkzeuge wie Tesa Easy Cover oder Pinselkamm.
- **Zahlen:** Median 10,5 Mio. Views, Top 194 Mio.; AdSense-Schätzung ~124k USD.
- **Lernen:** Der **stärkste DE-Beleg** für den Pfad „Short → Link in Bio → Amazon.de“. Tool-/Hack-Content liefert kaufbare Produkte direkt im Bild. IG ist bei Malerart der schwächste Kanal.

### CS15 – glam_style_living_ (IG, EN/CA, ~1,3 Mio.) und CS16 – d.signers (IG, ~4,4 Mio.)
- **glam_style_living_:** Storefront unter dem gleichen Handle (Tag `glamstyelivin-20`). Die Bio („Elizabeth“) deutet auf eine Person im Hintergrund.
- **d.signers:** hybrid mit Schwerpunkt Kurse (Academy) plus „Shop DS Amazon Store“. Der Storefront-Tag `eduardocarvaj-20` passt zu den in der Bio genannten Gründern.
- **Lernen:** Bei großen Design-Pages ist Amazon oft **Zusatz**-Umsatz, nicht Hauptmodell.

### Personengeführte Vergleichsfälle (Affiliate belegt)
| Account | Markt | Follower | Nachweis |
|---|---|---|---|
| jodie.thedesigntwins | EN | 2,3 Mio. | Bio „All links earn commission“, Amazon Shop + LTK |
| decor.snippets | EN | 3,1 Mio. | Storefront, Tag `decorue.inc-20` |
| toponlinefinds | EN | 528k | Storefront |
| thehomeedit | EN | 6,2 Mio. | Storefront + LTK + Rakuten + CJ |
| anna_louisa_at_home | EN | 4,4 Mio. | Storefront, Tag `annalouisax21-20` |
| shoppaholic | DE | 802k | Amazon.de-Storefront, Tag `rabiaodabas07-21`; Talent-Management |
| mi.interieur | DE | 1,3 Mio. | Storefront, Tag `michelelederh-21` |
| homestory_pictures | DE | 765k | Storefront, Tag `carmenrein-21` |
| stillers.home | DE | 556k | amzn.to Beatbot-Poolroboter + Kooperation |
| dekokrams | DE | 530k | Storefront, Tag `catharinajung-21` |
| landhaus_garten | DE | 488k | Storefront, Tag `andre094-21` |
| villa_karole | DE | 440k | Storefront, Tag `katharinalint-21` |
| cima.villa | DE | 400k | Linktree → Storefront, Tag `cindykukuc-21` |
| daniel.labbi | DE | 200k | Impact-Links (pxf.io) |
| interiorby_selinda | DE | 113k | 52 Links: amzn.eu/Temu/Rabattcodes |

**Lernen:** In DE ist Amazon.de-Storefront plus Instagram **Standard** bei Home-/DIY-Creatorinnen. Die Infrastruktur und die Kaufbereitschaft sind also da. Was fehlt, ist das **faceless** Format.

---

## 4. Antworten auf die qualitativen Fragen

### 4.1 Welche Home-/Lifestyle-Nischen beweisen, dass „Theme-Page + Affiliate“ funktioniert?
| Nische | Beweislage | Belege (Theme-/Marken-Pages ohne Person) |
|---|---|---|
| Amazon Home Finds / Home Decor (EN) | **stark** | trendyhomefinds1 (Associate-Disclosure), divaa.finds, stylerior, home.interior1, cool_amazon_homefinds, glam_style_living_ |
| Küchen-/Home-/Tech-Gadgets (EN) | **stark** | Justice Buys (Amazon + Walmart + Impact; 2,1 Mio. YT, 616k IG), uncrate |
| Haustiere (EN) | **stark** | round.boys, dogsofinstagram, Sathi Mart |
| Cleaning/Organization (EN) | **mittel** | thatorganizedhome (+ Personen-Benchmarks thehomeedit, anna_louisa_at_home) |
| Deals (DE) | **stark, aber anderes Format** (Stories) | dealbunny.de, mydealz.de |
| Baby/Parenting (DE) | **mittel** (1 Beleg) | echtemamas |
| DIY-Tools (DE) | **mittel** | Malerart |
| Garten/Pool (DE) | nur Personen | stillers.home, landhaus_garten |
| Luxury Homes | **kein Affiliate** | Lead-Gen/Newsletter/Brand Deals |
| AI Interior/Architektur | **kein Produkt-Affiliate** | App-Referral, Kurse, E-Book, AdSense |
| Kaffee, Smart Home (IG), Schlaf, Baby (EN) | **unbelegt / Datenlücke** | baristadaily („Shop Coffee Gear“) ohne ermittelbares Linkziel |

### 4.2 Wie professionell ist die DE-Konkurrenz vs. EN?
- **Anzahl gefundener DE-Theme-Pages >100k** (ohne Person im Vordergrund):
  - Instagram: dealbunny.de, mydealz.de, echtemamas, solebich, inspowelt__.
  - YouTube: Bau Rausch; Malerart mit Einschränkung (Hände im Bild).
  - Grenzfall: gnocchi.thekitten (Pet-Persona).
  - **Davon im Home-Decor/„Finds“-Format: 0.** In EN sind es im Sample ≥ 12 Home-/Produkt-Theme-Pages >100k.
- **Professionalität:**
  - **EN:** Page-Netzwerke (@discover.animal), Media-Firmen hinter Premium-Handles (dogsofinstagram → GreatPetCare-Tag), Agentur-Management (Justice Buys → Undercurrent), Multi-Netzwerk-Stacks (Amazon + LTK + Rakuten + CJ bei thehomeedit; Amazon + Walmart + Impact bei Justice Buys), dazu Temu als zweites Programm.
  - **DE:**
    - Professionell sind die **Deal-Plattformen** (mydealz, dealbunny mit App) und die **Personen-Creatorinnen**, die Storefronts konsequent nutzen (6 Amazon.de-Storefronts in der DIY-/Interior-Top-50).
    - Faceless-Home-Content in DE ist dagegen eher „unmonetarisiert“: Herr Zogg (Median 775k, keine Links), Mugs von Alfred (6,6k), Bau Rausch (keine Links).
    - NexLevs deutsche Shorts-Datenbank liefert bei „Amazon Funde Haushalt Gadgets Küche Wohnen“ **keinen einzigen echten Amazon-Funde-Kanal**, nur lose verwandte DIY-/Life-Hack-Kanäle.
- **Fazit:** DE ist im faceless Home-Finds-Segment **deutlich weniger besetzt und weniger professionell**. Die Nachfrage- und Monetarisierungsinfrastruktur (Amazon.de-Storefronts, Deal-Affinität) ist aber nachweislich vorhanden.

### 4.3 Gibt es erfolgreiche AI-generierte Interior-/Architektur-Pages – und monetarisieren sie über Affiliate?
**Ja, erfolgreich nach Reichweite. Nein, kein Produkt-Affiliate.**
- **Reichweite:**
  - Dreamy Interior: 315k Abos, Median ~580k, Top 32 Mio.
  - Bau Rausch (DE): 620k Abos, Median 1,2 Mio., Top 127 Mio.
  - Kou Yang AI: Median ~623k.
  - Jeremiah Carter: Median 425k.
  - UnrealLife: Top 22 Mio.
  - midjourney.architecture: 162k IG.
- **Monetarisierung:**
  - App-Referral: Isla → RenoMuse; Performance-Marketing einer AI-Interior-App mit Persona-Kanal.
  - Promotions/Workshops: midjourney.architecture.
  - E-Book: Home Graphix.
  - AI-Tool-Links: UnrealLife, Smart Design.
  - Sonst AdSense bzw. Shorts-Fonds.
- **Ursache (Hypothese bestätigt):** Die gezeigten Möbel und Räume sind nicht kaufbar, es gibt keine Produkt-URL. Der Affiliate-Pfad endet deshalb bei Software (AI-Design-Apps), nicht bei Möbeln.
- **Implikation:** Eine AI-Home-Page braucht einen **Brückenmechanismus**, etwa AI-Szenen um *reale, verlinkbare* Produkte herum, „Get the look“-Listen oder Organization/Cleaning-Produkte statt Fantasiemöbel. Sonst bleibt nur Shorts-Fonds bzw. App-Affiliate.

### 4.4 Welche Content-Formate dominieren bei Accounts mit Affiliate?
1. **Produktdemo-/Review-Shorts mit Link-CTA im Titel oder Overlay:** „🔗 Link in Bio …“, „Get this … – Link in my profile!“ (Justice Buys, Sathi Mart; formal auch Worldwide Gadgets mit Eigenshop). Das ist das skalierbarste Format für Gadgets, Küche und Pet-Produkte.
2. **„Amazon Finds“/„Products you didn’t know you needed“-Kompilationen** mit kuratierter Linkliste nach Raum (trendyhomefinds1, onlinee_finds, Justice Buys „Top 15 Amazon Products“).
3. **Aesthetic-Room-Slideshows** (Cozy Bedroom/Vanity) mit Text-Overlay und Keyword-Kommentar-CTA (divaa.finds; per Videoanalyse nur qualitativ). Echte „Comment LINK“-DM-Automation konnten wir nicht direkt verifizieren.
4. **Problem→Lösung/Organization-Tipps** (thatorganizedhome) und **Before/After-Makeovers** (d.signers, DE-DIY-Creatorinnen).
5. **UGC-/Repost-Unterhaltung plus thematische Storefront** (round.boys, dogsofinstagram). Der Content verkauft nicht direkt, die Storefront ist das „Community-Regal“.
6. **Deals in Stories** (dealbunny.de, mydealz.de) – das DE-Muster.
7. **Tool-/Hack-Videos** mit Werkzeug im Bild (Malerart).

### 4.5 Hinweise auf Einnahmen
- **Selbst genannte Affiliate-Einnahmen (CLAIMED) wurden bei keinem Account gefunden.**
- **Reichweiten-Claims (CLAIMED):**
  - Justice Buys: „1M on Instagram, 1M on TikTok, 800k Facebook“; laut Viewer hat Instagram tatsächlich 616k.
  - d.signers: „7M+ design lovers“.
  - mydealz: „33 Mio. Besuche pro Monat“.
- **Schätzungen durch Drittanbieter (ESTIMATED):**
  - HypeAuditor-Snippet homeinspirehacks: 4.280–5.863 USD Einkommen im Mai 2025, bei einer ER von nur 0,03 %.
  - NexLev-AdSense (Lebenszeit, **ohne** Affiliate):
    - Smart Design ~437k USD
    - Justice Buys ~191k USD
    - Malerart ~124k USD
    - Bau Rausch ~38,6k USD
    - Dreamy Interior ~15,4k USD
    - Hasnan Hafid ~2,7k USD (505k Abos!)
- **Indirekte Hinweise auf Profitabilität:**
  - Agentur-Management (Justice Buys/Undercurrent).
  - Media-Firmen-Tags in Storefronts (dogsofinstagram → `greatpetcare-20`).
  - Page-Netzwerke (cutest.farm → @discover.animal).
  - Talent-Management (shoppaholic → gl-management.net).

---

## 5. Auffällige Ineffizienzen & Opportunities
1. **Reichweite ohne Kauflink (EN):**
   - Smart Design: 4,37 Mrd. Views mit Multifunktionsmöbeln. Kaufbare Pendants (Klapptische, Schrankbetten) existieren.
   - CraftWorks: Garten-DIY, Median 1,1 Mio.
   - CrazyClean01: Cleaning-Tools im Bild.
   - Daily latte art: DeLonghi Dedica im Bild.
   - IG-Pages ohne Nachweis: homeinspirehacks (2,3 Mio.), smart_tech.__ (2,6 Mio.), design.only (2,7 Mio.), the_real_houses_of_ig (2,5 Mio.).
2. **Reichweite ohne Kauflink (DE):** Herr Zogg (Haushaltshacks, Median 775k bei 60k Abos) und Bau Rausch (AI, 620k Abos) – beide ohne Links.
3. **DE-White-Space:** kein faceless Home-Finds-/Küchengadget-/Cleaning-/Smart-Home-Theme-Account >100k gefunden. Gleichzeitig zeigen sechs Personen-Storefronts in der DE-DIY-Top-50 sowie dealbunny.de (988k) und mydealz.de (546k), dass Nachfrage und Kaufbereitschaft existieren.
4. **Plattform-Silos:** Viele IG-Theme-Pages haben praktisch keine TikTok-/YT-Präsenz (trendyhomefinds1 55, divaa.finds 133, stylerior 2 TikTok-Follower). Andersherum sind YT-Faceless-Kanäle auf IG schwach (Malerart IG 89k vs. YT 461k). Cross-Posting ist ungenutzt.
5. **Schwaches Engagement großer Repost-Pages** (homeinspirehacks ER 0,03 %; divaa.finds ~0,5 % Like-Rate): Follower-Masse ≠ Kaufkraft. Das spricht für kleinere, nischenschärfere Pages mit klarer Produktlogik (Organization, Pet Essentials, Küche).
6. **Monetarisierungs-Mix als Standard:** Amazon plus Temu (divaa.finds, stylerior, interiorby_selinda), plus Walmart/Impact (Justice Buys), plus Eigenprodukt (home.interior1, d.signers). Ein reines Amazon-Setup ist eher die Ausnahme.
7. **AI-Interior-Paradox:** Hohe Views, aber kein kaufbares Objekt. Wer AI nutzen will, sollte AI für *Szenen/Hooks* einsetzen und **reale Produkte** verlinken, oder den App-Affiliate-Pfad bewusst wählen.
8. **Eigenshop-Sog:** Viele große Pages (myhousesdecors, @dog, niopets1, Worldwide Gadgets, Pawmemories, SnuggoPaws) wählen Dropshipping bzw. einen Eigenshop statt Affiliate. Das ist ein Indiz dafür, dass Affiliate-Provisionen bei gleicher Reichweite weniger abwerfen. Provisionssätze waren nicht Teil dieser Recherche.
9. **Risiko Reposts:** Mehrere Theme-Pages bauen auf fremdem Content („we own no content“, „DM for credit/removal“). Eine AI-generierte Page umgeht dieses Urheberrechts- und Takedown-Risiko. Das ist ein struktureller Vorteil.

---

## 6. Datenlücken
- **Instagram-Views:** Median/Top-Views sind für IG durchgehend UNKNOWN. Nur Likes-Stichproben liegen vor (divaa.finds 3.815/3.649; onlinee_finds 887). Für eine belastbare View-Analyse bräuchte man einen IG-Login oder ein Tool (HypeAuditor/Modash Pro).
- **Postingfrequenz IG:** nur Gesamt-Postzahlen, keine Zeitreihen.
- **Link-in-Bio hinter Cloudflare** (Beacons, lnk.bio, solo.to) und direkte Bio-Links waren nicht abrufbar. „Unklar“ kann also Affiliate bedeuten; z. B. homeinspirehacks, baristadaily, dogtrainingdawg („Click the link below“).
- **Nischen ohne belastbare Theme-Page-Belege:** Schlaf (EN+DE), Baby EN, Garten/BBQ/Pool EN-IG, Smart Home IG, Kaffee mit Affiliate, alle DE-Küchen-/Cleaning-/Smart-Home-Theme-Pages.
- **Linktree-/Storefront-Handles ohne verifizierten IG-Account** wurden bewusst **nicht** aufgenommen: `kitchengadgets` (Storefront), `kitchenhacks`, `amazonkitchenfinds`, `smarthomefinds`, `amazonbabyfinds`, `babyfinds`, `cleaningfinds`, `momfinds` (Storefront + LTK), `amazonpetfinds` (→ IG `amazon_pet_finds`, nicht verifizierbar), `coffeegeek` (Storefront Mark Prince).
- **Follower-Diskrepanzen** zwischen Viewer-Cache, orbitvibe, HypeAuditor und Snippets (siehe `notizen`). Werte sind ESTIMATED und sollten vor einer Entscheidung stichprobenartig im IG-App-Login geprüft werden.
- **Faceless-Status** wurde nur bei einem Reel per Video-Analyse geprüft, sonst aus Bio und Format abgeleitet.
- **DE-Discovery:** Ohne Suchmaschine und Hashtag-Zugriff ist die DE-Abdeckung lückenhaft. Der Befund „0 DE-Home-Finds-Theme-Pages >100k“ sollte mit einer manuellen Hashtag-Suche (#amazonfunde, #amazonfundstücke, #wohnideen, #haushaltstipps) gegengeprüft werden.

---

## 7. Quellenliste (Auswahl, alle abgerufen 2026-09-26)

**Rankings/Listen**
- https://orbitvibe.com/rankings/instagram/lifestyle/home-decor
- https://orbitvibe.com/rankings/instagram/pets
- https://orbitvibe.com/rankings/instagram/real-estate
- https://orbitvibe.com/rankings/instagram/tech · https://orbitvibe.com/rankings/instagram/shopping-retail
- https://hypeauditor.com/top-instagram-diy-design-germany/
- https://hypeauditor.com/top-instagram-shopping-retail-germany/
- https://hypeauditor.com/top-instagram-animals-germany/
- https://hypeauditor.com/top-instagram-food-cooking-germany/
- https://hypeauditor.com/top-instagram-computers-gadgets-germany/
- https://hypeauditor.com/top-instagram-diy-design-united-states/
- https://pikory.com/explore/category/home-decor

**Affiliate-Nachweise – Linktree** (`https://linktr.ee/<handle>`): trendyhomefinds1, divaa.finds, stylerior, home.interior1, d.signers, myhousesdecors, justice_buys, worldwidegadgets01, sathimart, Malerart, round.boys, dogsofinstagram, catsofinstagram, dog, thehomeedit, jodie.thedesigntwins, coolmaterial, thisiswhyimbroke, midjourney.architecture, architecture_hunter, cima.villa, stillers.home, interiorby_selinda, daniel.labbi, homeheartmade, gardenwithjonny, anna_louisa_at_home.

**Affiliate-Nachweise – Amazon-Storefronts** (Titel und Associate-Tag aus dem Seitenquelltext)
- amazon.com/shop/: divaaa.finds, urban.homedesign, home.interior1, glam_style_living_, d.signers, cool_amazon_homefinds, decor.snippets, toponlinefinds, thatorganizedhome, thehomeedit, anna_louisa_at_home, uncrate, dogsofinstagram, round.boys, babylist.
- amazon.de/shop/: shoppaholic, echtemamas, mi.interieur, dekokrams, villa_karole, cima.villa, homestory_pictures, landhaus_garten.

**Weitere Primärquellen**
- https://www.shopltk.com/explore/thehomeedit
- https://www.justicebuys.com/
- https://www.dealbunny.de/ (Affiliate-Disclosure)
- https://www.mydealz.de/ (Quelltext)
- https://www.homedesignbook.com/
- TikTok-Profile: @justicebuys, @worldwidegadgets01, @malerart, @shoppaholic, @trendyhomefinds1, @divaa.finds, @stylerior, @homeinspirehacks
- Threads-Profile: @homeinspirehacks, @niopets1, @pitbullz_zone, @mydealz.de, @shoppaholic, @gadgetflow
- IG-Reel-Meta: https://www.instagram.com/reel/DPuNhtKk80T/ · https://www.instagram.com/reel/DO397VJiDtc/ · https://www.instagram.com/p/DFfP9YnNyMD/

**Follower-/Profil-Daten (Drittanbieter)**
- `https://insta-stories-viewer.com/<handle>/` (Cache-Viewer, ESTIMATED)
- WebSearch-Snippets (erste Abfragen): instagram.com/cool_amazon_homefinds, instagram.com/jodie.thedesigntwins, instagram.com/trendyhomefinds1, hypeauditor.com/instagram/homeinspirehacks/, instagram.com/toponlinefinds, instagram.com/divaa.finds

**YouTube/NexLev**
- NexLev `search_shorts_niche_finder_channels`: Queries „AI generated interior design and dream house architecture shorts“, „Amazon home finds gadgets must haves shorts“, „Amazon Funde Haushalt Gadgets Küche Wohnen“ (German), „espresso coffee setup home barista asmr“, „pet products gadgets for dogs and cats amazon finds“, „backyard pool garden outdoor living BBQ ideas“.
- NexLev `youtube_channel_about` (Justice Buys, Worldwide Gadgets, Dreamy Interior, Isla | Interior Designer).
- YouTube-Kanalseiten (`https://www.youtube.com/channel/<ID>`) für Beschreibungen und Links, IDs siehe CSV.
