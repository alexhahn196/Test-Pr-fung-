# Teil A – Affiliate-Programme: Amazon, Creator-Plattformen, Interior/Möbel, Schlaf, Smart Home

**Studie:** Welche Nische + welcher Markt (DE/DACH, USA, UK, International-Englisch) eignet sich am besten für eine KI-generierte, faceless Instagram-Reels-Theme-Page mit Affiliate-Monetarisierung?
**Prüfdatum:** 2026-09-26
**Rohdaten:** `raw_programs_A.csv` (199 Zeilen: 88 Amazon-Zeilen + 111 Programm-Zeilen)

---

## 1. Methodik

### 1.1 Quellenhierarchie und Datenqualitäts-Labels

| Label | Bedeutung in dieser Recherche |
|---|---|
| **VERIFIED** | Wert direkt auf einer Primärquelle gelesen: Amazon-Hilfe- und Vertragsseiten, offizielle Affiliate-Seite der Marke oder öffentliche **Impact-Vertragsvorschau** („Contract Terms“ auf `app.impact.com/campaign-promo-signup/<Marke>.brand`, dort als Base64-Objekt eingebettet und von mir dekodiert). Die Vertragsvorschau ist das Vertragstemplate, das Bewerber vor der Anmeldung akzeptieren. Sie nennt Default-Payout, Payout-Tabellen, Attributionsfenster, Sperr- und Zahlungsfristen und die Werbe-Restriktionen. |
| **CLAIMED** | Werbeaussage des Betreibers, z. B. „bis zu“, „as much as“ oder AOV-Angaben in der Programmbeschreibung. |
| **THIRD-PARTY ESTIMATE** | Wert aus dem Verzeichnis **affiliate-marketing.de**, das Netzwerk-Programmdaten aggregiert (Zeitstempel je Zeile, meist 26.09.2026), oder aus Branchenmedien. |
| **UNKNOWN** | Nicht auffindbar. Es wurden keine Werte geschätzt. |

### 1.2 Einschränkung: Suchbudget

Nach 3 Websuchen war das WebSearch-Budget der Session erschöpft (200 von 200, mit anderen Agenten geteilt). Die restliche Recherche lief deshalb ohne Suchmaschine. Genutzt wurden:

1. **Direkter Abruf** der Amazon-Vertragsseiten (US, DE, UK) als Rohtext. Die Zitate unten sind wörtlich übernommen.
2. **Brand-Homepages**, auf denen ich nach Affiliate-Links suchte, und anschließend der Abruf der verlinkten Programmseiten.
3. **Impact-Vertragsvorschauen**, deren Marken-Slugs ich über Namensvarianten ermittelt habe (z. B. `Crate-and-Barrel`, `West-Elm-US`).
4. **affiliate-marketing.de**, geparst nach Netzwerk, Provision, SEM-Regel, Produktdaten und Vertriebsgebiet.

### 1.3 Nicht erreichbare Quellen

- **Awin-Merchant-Profile** (`ui.awin.com/merchant-profile/<ID>`) waren nicht nutzbar. Ohne Suchmaschine ließen sich die IDs nicht ermitteln. Deshalb fehlen für Awin-Programme meist Cookie-Dauer, AOV und EPC.
- Viele US-Shops blockieren Bots, zum Beispiel Wayfair, Pottery Barn, Crate & Barrel (Web), Dyson, Lumens, Loaf und Soho Home.

### 1.4 Hinweis zu Sub-Netzwerk-Raten

Sub-Netzwerke wie FlexOffers, SaleGains, MyLead, cityads, AdPump oder MCANISM zeigen im Verzeichnis oft abweichende Raten. FlexOffers-Werte entsprechen auffällig oft etwa 80 % eines runden Direktsatzes (z. B. 3,2 = 4 × 0,8). Diese Raten wurden deshalb nur als Nebeninfo verwendet.

---

## 2. Amazon – Provisionen (Standard-Vergütungskatalog, Stand 26.09.2026)

### 2.1 USA (amazon.com)

Quelle: https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ

| Satz | Kategorien |
|---|---|
| 10 % | Luxury Beauty, Luxury Stores Beauty, Amazon Explore |
| 5 % | Handmade, Digital Music/Videos |
| 4,5 % | **Kitchen**, Automotive, Physical Books |
| 4 % | Apparel, Jewelry, Watches, Luggage, Shoes, Handbags & Accessories, Luxury Stores Fashion, Amazon-Geräte (Echo, Fire, Kindle, **Ring Devices**), „All Other Categories“ (u. a. Electronics, da nicht separat gelistet) |
| 3 % | **Furniture, Home, Home Improvement, Lawn & Garden, Pets**, Tools, Sports, Outdoors, Toys, Baby, Beauty, Headphones, Musical Instruments |
| 2,5 % | PC, PC Components |
| 2 % | Televisions, Digital Video Games |
| 1 % | Physical Video Games & Konsolen, Grocery/Amazon Fresh, Health & Personal Care |
| 0 % | Gift Cards, Alkohol, Wireless-Verträge u. a. |

### 2.2 Deutschland (amazon.de)

Quelle: https://partnernet.amazon.de/help/node/topic/GRXPHT8U84RAYDXZ

| Satz | Kategorien |
|---|---|
| 6 % | Bekleidung & Accessoires, Fashion-Eigenmarken, Luxus / Luxus Beauty / Luxus Fashion, Schuhe/Handtaschen, Uhren |
| 5 % | **Möbel, Wohnen, Küche & Esszimmer, Baumarkt, Elektro- & Handwerkzeuge**, Schmuck, Auto & Motorrad, Bücher, Handmade |
| 4 % | Beauty, Gepäck, Körperpflegegeräte, Sport & Fitness |
| 3 % | alle anderen Kategorien, vermutlich u. a. Elektronik, Computer, Spielzeug, Baby, Haustier, Garten und Beleuchtung (Zuordnung durch Amazon) |
| 2,5 % | Haushaltsgroßgeräte, Fire TV, Mobile Elektronik |
| 1 % | Lebensmittel, Videospiele & Konsolen |

### 2.3 UK (amazon.co.uk)

Quelle: https://affiliate-program.amazon.co.uk/help/node/topic/GRXPHT8U84RAYDXZ

Die Sätze sind identisch mit DE (EU-Anhang):

- 6 %: Fashion/Luxury/Shoes/Watches
- 5 %: Furniture, Home, Kitchen, Home Improvement, Tools, Jewellery
- 4 %: Beauty, Luggage, Sports
- 3 %: All Other
- 2,5 %: Appliances, Fire TV, Mobile Electronics
- 1 %: Grocery, Games

### 2.4 Cookie (alle drei Märkte)

Die Session endet nach **24 Stunden**. Legt der Kunde innerhalb der Session ein Produkt in den Warenkorb, zählt der Kauf, wenn er **„no later than 89 days after their initial click-through“** abgeschlossen wird. Die Angabe ist VERIFIED (US/UK-Commission-Statement, DE „spätestens 89 Tage“).

### 2.5 Befunde

- **Home/Möbel ist in DE und UK mit 5 % deutlich besser vergütet als in den USA mit 3 %.** Kitchen liegt in den USA bei 4,5 %, in DE/UK bei 5 %.
- **DE-Sätze wurden mehrfach gesenkt.** Laut ABAKUS-Forum galt ab 23.06.2025 z. B. Möbel/Wohnen/Beauty 6 % und Fashion 8 % (THIRD-PARTY). Heute gelten 5 % bzw. 6 %, es gab also eine weitere Senkung, deren Datum unbekannt ist.
- **Werbeaussage passt nicht zur Tabelle.** Die DE- und UK-Startseiten werben mit „bis zu 12 %“, die Standardtabelle reicht aber nur bis 6 %.
- **Individuelle Publisher-Deals gekürzt.** Laut Adweek (18.05.2026) wurden individuell verhandelte Publisher-Sätze um bis zu 50 % gekürzt und Meilenstein-Boni gestrichen. In den USA geschah das etwa ab 09.03.2026, zuvor schon in APAC. Die **öffentliche** US-Standardtabelle ist unverändert.
- **Änderungen zum 14.04.2026** (Operating Agreement, US und DE):
  - Käufe über **bezahlte/geboostete Anzeigen** sind disqualifiziert.
  - Es gilt eine **180-Tage**-Versand- und Zahlungsfrist.
  - **Onsite-Provision** gibt es nur noch auf die gleiche ASIN-Variante.
  - Eine **Originalinhalt-Definition** wurde eingeführt: „commentary, analysis or transformation“.
  - Alle registrierten Associates erhalten **Storefront + Unique Creator Link**.
- **Auszahlung (US):** „Commission income is paid approximately 60 days after the end of“ the month (US-Startseite).

---

## 3. Amazon-Regeln für Social Media, DMs, Linkkürzer und Bilder (wörtliche Zitate)

### 3.1 Social Media ist eine zulässige „Site“

> „The Associates Program permits you to monetize your website, social media user-generated content, online software application, or Alexa skill (referred to here as your “Site”)“
> – https://affiliate-program.amazon.com/help/operating/agreement

**Registrierung des Accounts ist Pflicht.** Die akzeptierten Netzwerke sind eine abschließende Liste. **Pinterest ist nicht dabei.**

> „We currently only accept the following social networks: Facebook (including open group pages and fan pages, but excluding personal pages), Instagram, Twitter, YouTube, Tik Tok and Twitch.tv. Your application must clearly list your social media page’s exact URL […]“
> „Your social network page or group must be established, with a substantive number of organic followers/likes (in most cases, at least 500).“
> „[…] we require at least three [qualified sales] within the first 180 days“ und „a good rule of thumb is at least 10 posts“
> – https://affiliate-program.amazon.com/help/node/topic/G8TW5AE9XL2VX9VM (DE identisch: https://partnernet.amazon.de/help/node/topic/G8TW5AE9XL2VX9VM – „in den meisten Fällen mindestens 500“)

Zusätzlich gilt: Kein Amazon-Markenname im Username.

> „include any trademark of Amazon […] in any username, group name, or other identifier on any social networking site“
> Das ist ein Grund für eine „Unsuitable Site“ – https://affiliate-program.amazon.com/help/operating/policies

### 3.2 Direktnachrichten (relevant für Comment-to-DM, z. B. ManyChat): erlaubt, aber nur „solicited“

> US/UK: „You may include Special Links in emails, SMS and direct messaging from your social media Sites; provided, that such communications are solicited (i.e., opted into by the receiving customer) and are otherwise in compliance with the Agreement, the Trademark Guidelines, and the Amazon Brand Usage Guidelines. […] you are the “Sender” of each communication containing any Special Links“
> – https://affiliate-program.amazon.com/help/operating/policies (UK wortgleich: https://affiliate-program.amazon.co.uk/help/operating/policies)

> DE: „Sie können spezielle Links in E-Mails, SMS und Direktnachrichten von Ihren Social-Media-Websites einfügen. vorausgesetzt, dass solche Mitteilungen angefordert werden (d. h. vom empfangenden Kunden angemeldet werden) […]“
> – https://partnernet.amazon.de/help/operating/policies

**Interpretation (nicht von Amazon bestätigt):** Ein Nutzer, der aktiv ein Keyword kommentiert, um den Link zu erhalten, fordert die Nachricht an. Das spricht dafür, dass eine Comment-to-DM-Automation als „solicited“ gilt. Unverlangte Massen-DMs sind dagegen nicht gedeckt.

Voraussetzungen für den zulässigen Einsatz:

- Der sendende Account muss als Site registriert sein.
- Das Keyword im Call-to-Action muss klar formuliert sein.
- Die Offenlegung muss auch in der DM stehen.
- Auf Anfrage muss man Amazon Musterkommunikation und eine Zertifizierung vorlegen können.

### 3.3 Linkkürzer

> „(w) You will not use a link shortening service, button, hyperlink or other ad placement in a manner that makes it unclear that you are linking to an Amazon Site.“
> DE: „(w) Sie werden keine Link-Verkürzungen […] in einer Weise vornehmen, die Unklarheit dahingehend hervorrufen, dass Sie auf eine Amazon-Website verlinken.“

Linkkürzer sind also nicht verboten, das Ziel muss aber erkennbar bleiben, z. B. amzn.to oder der Hinweis „(Amazon-Link)“. Verschleierte Redirects sind nach Regel (v) verboten.

### 3.4 Kennzeichnung

> „You must clearly and prominently state the following […]: “As an Amazon Associate I earn from qualifying purchases.”“
> – https://affiliate-program.amazon.com/help/operating/agreement

> DE: „„Als Amazon-Partner verdiene ich an qualifizierten Verkäufen““
> – https://partnernet.amazon.de/help/operating/agreement

Für Social Media gelten zwei Ebenen:

> „For social media user-generated content, this statement must be associated with your account.“ Zusätzlich braucht jeder Link eine Kennzeichnung, z. B. „(paid link)“, „#ad“ oder „#CommissionsEarned“.
> – https://affiliate-program.amazon.com/help/node/topic/GHQNZAU6669EZS98

> DE: „Eine klare Auskunft kann so einfach sein wie: „(bezahlter Link)“, „#Anzeige“ oder „#VerdientProvisionen“.“
> – https://partnernet.amazon.de/help/node/topic/GHQNZAU6669EZS98

### 3.5 Produktbilder, KI-Bilder und Originalinhalt

**Amazon-Programminhalte, also Bilder, die man von Amazon oder über die API bezieht, dürfen nicht verändert werden:**

> „(a) You will not add to, delete from, or otherwise alter any Program Content in any way, including by adding additional information, except that you may resize Program Content consisting of a graphic image in a manner that maintains the original proportions of the image […]“
> – https://affiliate-program.amazon.com/help/operating/policies

**Bilder aus der API dürfen nicht gespeichert werden:**

> „(h) You will not store or cache Product Advertising Content consisting of an image, but you may store a link to Product Advertising Content consisting of an image for up to 24 hours.“
> – ebd., IP License

**Interpretation:** Amazon-Produktfotos mit KI zu verändern, etwa ein Produkt per KI in einen Raum zu setzen, oder sie herunterzuladen und in Reels einzuschneiden, ist durch die Lizenz nicht gedeckt. Eigene KI-Visuals sind keine „Program Content“. Sie dürfen aber nicht irreführen (FTC bzw. UWG) und keine Amazon-Marken missbräuchlich nutzen.

**Originalinhalt** (verschärft zum 14.04.2026):

> „Original content utilizing third-party materials must contain significant commentary, analysis, or transformation to any materials you include.“
> – https://affiliate-program.amazon.com/help/operating/policies
> DE: „Originalinhalte […] müssen wesentliche Kommentare, Analysen oder Umwandlungen […] enthalten.“

**Risiko für eine KI-Theme-Page:** Reine Produkt-Slideshows ohne Einordnung sind angreifbar.

**Bewertungen und Sterne** dürfen nur über die Creators API bzw. PA-API angezeigt werden (Regel (t)).

### 3.6 Bezahlte Reichweite

> „Expanded disqualified purchases to include products purchased by customers referred through any paid or boosted advertisement linking to Amazon, regardless of whether prohibited keywords are used. Limited exceptions apply.“
> – https://affiliate-program.amazon.com/help/operating/compare (gültig ab 14.04.2026, DE gleichlautend)

Das Boosten von Reels mit Amazon-Links bringt also in der Regel keine Provision.

### 3.7 Incentives und Giveaways

> „(g) You will not offer any person or entity any consideration, reward, or incentive […] for using Special Links.“

### 3.8 Influencer Program, Storefront, Onsite-Provision und Creator Connections

- **Influencer Program:** Es existiert in **US, DE und UK**. Die Influencer-Richtlinie ist Teil der jeweiligen Programmrichtlinien, und die DE- und UK-Startseiten verweisen darauf.
- **Onsite Commission** gibt es nur mit spezieller Store-ID. Seit 14.04.2026 wird sie nur noch auf die gleiche ASIN-Variante gezahlt. Konkrete Onsite-Sätze sind nicht öffentlich.
- **Storefront und Unique Creator Link** stehen seit 14.04.2026 allen registrierten Associates zur Verfügung.
- **Creator Ads Boost:** Nur auf Einladung. Amazon nutzt dabei Creator-Inhalte in Anzeigen, u. a. bei Meta.
- **Creator Connections:** Der Status 2026 ist **nicht verifizierbar**. Es gibt keine öffentliche Seite, und die Richtlinien vom April 2026 erwähnen das Programm nicht.

### 3.9 API

Die **PA-API 5 ist „deprecated“**. Aufrufe liefern HTTP 403. Nachfolger ist die **Creators API**, mit folgender Voraussetzung:

> „Have at least 10 qualifying sales within the past 30 days“
> – https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction

---

## 4. Wichtigste Befunde je Nische und Markt (ohne Amazon)

### 4.1 Interior / Möbel / Deko / Licht

**DE/DACH – dünnes Direktprogramm-Angebot, Amazon DE mit 5 % konkurrenzfähig**

- **Connox** (Awin): 8 % ohne Gutschein, 4 % mit Gutschein, **60 Tage Cookie**, Produktfeed. VERIFIED, Brand-Seite.
- **Nordic Nest DE** (Adtraction): mindestens 8 %, **15 Tage** Cookie, täglicher Feed. VERIFIED.
- **Westwing:** Rakuten laut Brand-Seite, Daisycon-Listing 4,9–6 %, **30 Tage**, Social ausdrücklich erlaubt, Feed, Provision verhandelbar.
- **Lampenwelt** (Awin): 5–8 %. THIRD-PARTY.
- **Made in Design** (Daisycon): 3,15–7,7 %, 30 Tage. THIRD-PARTY.
- **Höffner** (Awin): 1–10 %. THIRD-PARTY.
- **OTTO** (Awin): Das Listing zeigt 30 %. Das ist unplausibel und muss geprüft werden.
- **Ohne aktives Programm im Verzeichnis:** home24, Maisons du Monde, Urban Outfitters, Beliani, Juniqe, Wayfair.de.
- **Keine öffentlichen Programme für DE/US/UK gefunden:** IKEA, H&M Home.

**UK**

- Nordic Nest UK: mindestens 8 %, 15 Tage. VERIFIED.
- Made in Design UK: 3,15–7,7 %.
- Wayfair UK: Awin 2 %, CJ 3 %. THIRD-PARTY.
- John Lewis (Impact), Soho Home (Rakuten), Anthropologie (Rakuten): Netzwerk bekannt, Rate UNKNOWN.

**US – das breiteste Angebot, aber stark gestaffelte Konditionen (alle VERIFIED über Impact)**

| Programm | Provision | Attribution |
|---|---|---|
| The Home Depot | **8 %** auf Interior Furniture, Area Rugs, Housewares, Mattresses, Bedding, Home Decor, Tabletop, Wallpaper; 1 % sonst (auch Lighting) | **1 Tag** |
| AllModern (Wayfair LLC) | **8 %** | **45 Tage** |
| Target | Home & Outdoor 5 % Basis, Volumen-Tiers 6–8 % ab 11 Aktionen/Monat | 7 Tage, nur US-Traffic |
| Castlery | 5 % (−20 % bei Rabatt > $120) | 30 Tage |
| Arhaus | 4 % | 30 Tage |
| Albany Park | 4 % (Sofas 2 %) | 30 Tage |
| Crate & Barrel | 4 %, Furniture 2 %, Sale 0 % | 7 Tage |
| CB2 | 2 % | 7 Tage |
| Ruggable | 3 % | 30 Tage |
| Society6 | 2 % | 30 Tage |
| Williams-Sonoma-Gruppe (Pottery Barn, West Elm, Williams-Sonoma, Rejuvenation) | **1 %** | **1 Tag** |
| Lowe’s | 1 % | 1 Tag |

Außerdem: Lulu & Georgia 10 % (Ascend, THIRD-PARTY), Joybird 3 % (CJ, THIRD-PARTY).

### 4.2 Schlaf / Matratzen / Bettwäsche

**US – höchste Einzelprovisionen der gesamten Recherche (VERIFIED über Impact)**

| Programm | Provision | Attribution / Besonderheit |
|---|---|---|
| DreamCloud | **$150 pro Order bzw. 12 %** | 30 Tage |
| Nectar | **8–12 %** | 30 Tage |
| Parachute | 10 % Neukunden / 5 % Bestandskunden | 7 Tage |
| Helix | 5 % („up to 6 %“) | 90 Tage First Click, nur US/CA-Traffic |
| Tuft & Needle | 2–5 % | 30 Tage |
| Buffy | 3 % | 30 Tage |
| Purple, Eight Sleep, Sleep Number | je 2 % | 30 Tage |
| Brooklinen | 0 % Default, 1 Tag (nur individuelle Deals) | – |
| Saatva | Partnerize, Rate UNKNOWN | – |

**UK**

- **Nectar UK:** £80 bzw. 12 %, 30 Tage. VERIFIED.
- **Emma UK** (Awin): 5–7 %. THIRD-PARTY.
- **Simba:** 5 % CPA, 30 Tage, **AOV £627** (CLAIMED). Die Provision fließt aber **erst nach der 200-Nächte-Probeschlafphase**.

**DE**

- **Emma** (Awin): 3–10 %, 30 Tage. THIRD-PARTY; die DE-Zeile im Verzeichnis ist von 2023.
- **bett1/BODYGUARD:** CJ 5 %, Programmtext „8 % CPA“, „Durchschnittlicher Warenkorbwert von über 320 €“ (CLAIMED).

### 4.3 Smart Home / Licht / Saugroboter

**Global und US (VERIFIED)**

| Programm | Provision | Attribution / Besonderheit |
|---|---|---|
| Nanoleaf | **10 % in allen Regionen** (US, CA, EU, GB, AU, JP, HK) | 30 Tage |
| Ring US | **10 %** (SKU-Ausnahmen) | 30 Tage |
| Anker | 8 % (US und DE-Store) | 30 Tage |
| eufy US | 7 % (Brand-Seite: 7–15 % CLAIMED, Social ausdrücklich zugelassen) | 30 Tage |
| Philips Hue US/DE | 7 % Basis, 10 % im ersten Monat | – |
| Philips Hue UK | 5 %, 7 % im ersten Monat | – |
| Roborock US | 4–7 %, AOV $400+ (CLAIMED) | 45 Tage |
| Dreame US | 5–6 % (CLAIMED), Instagram/YouTube ausdrücklich genannt | 30 Tage |
| Sonos | 3 % | 30 Tage |
| Dyson UK | 1 % | 30 Tage |

**DE (überwiegend THIRD-PARTY)**

- Govee (Awin): 5–12 %
- Arlo: 5–10 % (UK 10 %)
- tado°: 4–5 % (UK 5 %)
- Ecovacs: 5 %
- Dyson DE: 5 %
- Roborock DE: Webgains 4 %, Programmtext „6 %–10 %“, AOV €760 (CLAIMED)
- **eufy DE** (Impact): 4–6 %, **Social Media nur mit Genehmigung** (VERIFIED)

**Weitere Befunde**

- **Apple** hat nur ein Services-Programm (Partnerize) und **kein Hardware-Affiliate**.
- **Google Store:** kein Programm gefunden.
- **Eve, Netatmo:** keine aktiven Programme gefunden.

### 4.4 Creator-Plattformen

- **Target** (Impact, Target Partners): Konditionen siehe oben. Das ist die einzige Retailer-Creator-Plattform mit vollständig verifizierten Sätzen. **Nicht-US-Traffic wird nicht vergütet.**
- **Walmart Creator** (Impact-basiert, US/CA):
  - „Fashion commissions are now 20%!“
  - „Recent updates have changed some categories to a 0% commission rate“
  - Instagram-Login-Verbindung
- **LTK:** Nur per Bewerbung, verlangt werden „A public social media profile“ und „A high number of engaged followers“, idealerweise tägliches Posten. Die Provisionen sind nicht öffentlich.
- **Howl:** Kein Follower-Minimum, Auszahlung Net 30/60/90, kein Mindestbetrag.
- **Skimlinks** (ShopYourLikes für Creator): Revenue-Share, Auszahlung 92 Tage nach Monatsende, Minimum $65/£50/€55.
- **Sovrn Commerce:** Link-Optimierung und APIs, eher für Websites.
- **ShopMy, Shopify Collabs, Collective Voice:** keine öffentlichen Konditionen. ShopMy-Tracking ist aber auf society6.com und buffy.co eingebunden.
- **Etsy Creator Collective:** mindestens **500 Follower** auf einem autorisierten Kanal, Validierung nach 30 Tagen, Support auch auf Deutsch.
- **Geniuslink** (Tool): $6 Grundgebühr plus $3,50 je 1.000 Klicks, Geo-Routing auf den lokalen Amazon-Store.

---

## 5. Auffälligkeiten

### 5.1 Hohe Provision und hoher Warenkorb

- **Schlaf US/UK:** DreamCloud ($150 oder 12 %), Nectar US (8–12 %), Nectar UK (£80 oder 12 %).
- **Parachute:** 10 % auf Neukunden.
- **The Home Depot:** 8 % auf Möbel, Teppiche, Deko und Matratzen, aber nur **1 Tag** Attribution.
- **AllModern:** 8 % mit **45 Tagen**. Das ist die beste Kombination im US-Interior-Bereich.
- **Nanoleaf:** 10 % global. Für eine internationale englische Page ist das die einzige verifizierte, weltweit einheitliche Rate.
- **Ring:** 10 % (US).
- **Roborock:** AOV $400+ bzw. €760 (CLAIMED).
- **Simba:** AOV £627 (CLAIMED), aber Validierung erst nach 200 Nächten.
- **Connox DE:** 8 % mit 60 Tagen.

### 5.2 Sehr kurze Attributionsfenster

Für Reels ist das ein Problem, weil Käufe oft zeitversetzt passieren.

- **1 Tag:** Williams-Sonoma-Gruppe, Home Depot, Lowe’s, Brooklinen
- **7 Tage:** Target, Crate & Barrel, CB2, Parachute
- **Amazon:** 24 Stunden, mit Warenkorb-Verlängerung auf 89 Tage

### 5.3 Einschränkungen für Social Media und faceless Accounts

- **eufy DE:** Social Media nur mit vorheriger Genehmigung.
- **Arhaus:** Links auf Arhaus-eigenen Social-Seiten, Facebook-Ads mit dem Markennamen und die Marke im Account-Namen sind verboten.
- **Sonos:** keine Marke im Handle, keine Influencer- oder Mitarbeiter-Codes.
- **Williams-Sonoma-Gruppe:** Die Anti-Fraud-Klausel richtet sich gegen „fake or misrepresented creator, affiliate, publisher, or social media identities“ und gegen Accounts, „that cannot reasonably be tied to corresponding bona fide social, website, or promotional activity“. Das ist ein Prüfpunkt für anonyme KI-Pages.
- **Helix:** Traffic nur aus US/CA.
- **Target:** Nicht-US-Traffic wird mit 0 vergütet.
- **Amazon:** Pinterest ist nicht als Site zugelassen. Geboostete Posts sind disqualifiziert.
- **LTK:** Auswahl nach Creator-Profil und Engagement.

### 5.4 Gutscheine mindern die Provision

- Connox zahlt mit Gutschein nur 4 %.
- Castlery kürzt die Provision um 20 %, wenn der Rabatt über $120 liegt.
- Viele Programme erlauben nur Programm-Codes.

### 5.5 Widersprüchliche Daten

- **Buffy:** Impact 3 % (VERIFIED) gegenüber Awin-Listing 15 %.
- **OTTO:** Awin-Listing 30 %.
- **CB2:** Sub-Netzwerk „bis 12 %“, Impact-Vertrag 2 %.
- **Wayfair UK:** FlexOffers 10 %, Awin 2 %.

In allen Fällen gilt: Die Impact-Vorschau hat Vorrang.

### 5.6 Marktvergleich Amazon

Im Home-Bereich zahlt Amazon DE/UK 5 %, Amazon US 3 %. In den USA gibt es dafür deutlich mehr Direktprogramme mit 4–12 %.

---

## 6. Datenlücken

- **Awin-Merchant-Profile** (Cookie, AOV, EPC, Konversionsrate) konnten ohne Suchmaschine nicht gefunden werden. Die Cookie-Dauer fehlt bei fast allen Awin-, CJ- und Webgains-Programmen.
- **Wayfair** (US, UK, DE): Konditionen unbekannt, Bot-Schutz; der Impact-Slug „Wayfair“ gehört einer anderen Firma.
- **Weitere Programme mit Rate UNKNOWN:** John Lewis, Dunelm, Loaf, Soho Home, home24, Kave Home, Posterstore, Juniqe, Article, Burrow, Interior Define, Rove Concepts, YLighting, Coco-Mat, OTTY, Eve, Netatmo, Google Store, Saatva, Casper US.
- **Creator-Plattformen:** Die Provisionsmodelle von LTK, ShopMy, Shopify Collabs und Collective Voice sind nicht öffentlich. Die Walmart-Kategorietabelle ließ sich nicht abrufen (JS/API).
- **Amazon:** Onsite-Commission-Sätze, der Status von Creator Connections 2026 und das genaue Datum der letzten DE-Senkung sind unbekannt.
- **AOV** ist nur für Simba, Roborock (US/DE) und bett1 als CLAIMED bekannt. Für alle anderen fehlt ein AOV.
- **Philips Hue:** Die FAQ zu Netzwerk, Cookie und Ausschlüssen wurde nicht geladen.

---

## 7. Quellen

### 7.1 Amazon

- Commission Income Statement US: https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ
- Vergütungskatalog DE: https://partnernet.amazon.de/help/node/topic/GRXPHT8U84RAYDXZ
- Commission Income Statement UK: https://affiliate-program.amazon.co.uk/help/node/topic/GRXPHT8U84RAYDXZ
- Operating Agreement US: https://affiliate-program.amazon.com/help/operating/agreement
- Program Policies US (inkl. Participation Requirements, IP License, Influencer und Creator Ads Boost): https://affiliate-program.amazon.com/help/operating/policies
- Teilnahmevereinbarung und Programmrichtlinien DE: https://partnernet.amazon.de/help/operating/agreement · https://partnernet.amazon.de/help/operating/policies
- Program Policies UK: https://affiliate-program.amazon.co.uk/help/operating/policies · https://affiliate-program.amazon.co.uk/help/operating/agreement
- Änderungen 14.04.2026: https://affiliate-program.amazon.com/help/operating/compare · https://partnernet.amazon.de/help/operating/compare
- Social-Media-Offenlegung: https://affiliate-program.amazon.com/help/node/topic/GHQNZAU6669EZS98 · https://partnernet.amazon.de/help/node/topic/GHQNZAU6669EZS98
- Application Review: https://affiliate-program.amazon.com/help/node/topic/G8TW5AE9XL2VX9VM · https://partnernet.amazon.de/help/node/topic/G8TW5AE9XL2VX9VM
- Creators API: https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction · https://affiliate-program.amazon.com/creatorsapi/docs/en-us/paapiv5-deprecation
- Startseiten und Influencer: https://affiliate-program.amazon.com/ · https://partnernet.amazon.de/ · https://affiliate-program.amazon.co.uk/ · https://affiliate-program.amazon.com/influencers

### 7.2 Sekundärquellen zu Amazon-Kürzungen

- Adweek: https://www.adweek.com/media/amazon-associates-affiliate-rate-cuts-publishers/
- eMarketer: https://www.emarketer.com/content/amazon-cuts-affiliate-commissions-by-up-50--raising-pressure-on-publishers
- ABAKUS-Forum (Juni 2025): https://forum.abakus-internet-marketing.de/viewtopic/t-147041.html
- wortfilter: https://wortfilter.de/amazon-partnerprogramm-aenderungen-2026/

### 7.3 Impact-Vertragsvorschauen

Alle unter `https://app.impact.com/campaign-promo-signup/<Slug>.brand`, abgerufen am 26.09.2026:

- Interior/Möbel und Retail: AllModern, Pottery-Barn-US, Pottery-Barn (WSI Influencer), West-Elm-US, Williams-Sonoma, Rejuvenation, Crate-and-Barrel, CB2, Arhaus, Castlery-US, Albany-Park, Ruggable, Society6, The-Home-Depot, Lowes, Target
- Schlaf: Purple, Nectar-Sleep, Nectar-UK, DreamCloud, Helix-Sleep, Tuft-and-Needle, Eight-Sleep, Sleep-Number, Brooklinen, Parachute-Home, Buffy, Casper
- Smart Home: Nanoleaf, Ring, Sonos, Dyson (UK), Anker, Eufy-US, Eufy-DE

### 7.4 Brand-Seiten

- https://www.connox.de/ueber-uns/medien/partnerprogramm.html
- https://www.westwing.de/i/affiliate-program/
- https://www.nordicnest.de/uber-uns/affiliate/ · https://www.nordicnest.com/about-us/affiliate/
- https://www.castlery.com/us/affiliate-program
- https://www.etsy.com/affiliates
- https://simbasleep.com/pages/affiliate
- https://purple.com/affiliate-program
- https://www.nectarsleep.com/p/affiliates · https://www.dreamcloudsleep.com/p/affiliates
- https://www.emma-matratze.de/partnerprogramm/
- https://nanoleaf.me/en-us/pages/affiliate-program
- https://www.philips-hue.com/en-us/explore-hue/affiliate-programme · https://www.philips-hue.com/de-de/explore-hue/affiliate-programme · https://www.philips-hue.com/en-gb/explore-hue/affiliate-programme
- https://www.eufy.com/affiliate
- https://us.roborock.com/pages/roborock-affiliate-program
- https://www.dreametech.com/pages/affiliate-program
- https://performance-partners.apple.com/home
- https://www.luluandgeorgia.com/pages/affiliates

### 7.5 Creator-Plattformen

- https://company.shopltk.com/en/creator · https://company.shopltk.com/en/company
- https://creator.walmart.com/ · https://affiliates.walmart.com/
- https://www.skimlinks.com/creators/ · https://www.skimlinks.com/terms-of-service/
- https://www.sovrn.com/commerce/
- https://www.howl.link/
- https://geniuslink.com/pricing/
- https://shopmy.us/terms · https://docs.shopmy.us/
- https://www.shopify.com/collabs/creators
- https://app.collectivevoice.com

### 7.6 Verzeichnis (THIRD-PARTY)

`https://www.affiliate-marketing.de/partnerprogramme/<slug>` mit den Slugs:

- Interior: westwing, otto, lampenwelt.de, connox.de, madeindesign, hoeffner.de, xxxlutz.de, home24.de, maisonsdumonde.com, beliani.de, wayfair.de, wayfair.co.uk, wayfair.com, nordicnest.de, nordicnest.com, desenio.com, juniqe.de, hm.com, urbanoutfitters.com, ikea.com, johnlewis.com, dunelm.com, sohohome.com, anthropologie.com, luluandgeorgia.com, joybird.com, lumens.com
- Schlaf: emma, bett1.de, simbasleep.com, casper.com, saatva.com, snowehome.com
- Smart Home: govee.com, tado.com, arlo.com, ecovacs.com, roborock.com, dreametech.com, dyson.de, irobot.com, switch-bot.com, aqara.com, ring.com, anker.com, eufy.com, nanoleaf.me, philips-hue.com, netatmo.com
