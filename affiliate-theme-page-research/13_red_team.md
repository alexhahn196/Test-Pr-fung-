# 13 – Red Team: Die Top 10 bewusst widerlegen (Teil 25)

**Stand:** 26.09.2026 · Grundlage: [12_top10.md](12_top10.md), Quellen A–K in [`quellen/`](quellen/)

**Vorgehen:** Für jede Kombination suche ich das **stärkste** Gegenargument, nicht das bequemste. Danach frage ich: Hält die Kombination trotzdem? Muss sie umgebaut, abgewertet oder gestrichen werden?

---

## 1. Red Team gegen das Gesamtmodell (gilt für alle Nischen)

| # | Gegenargument | Beleg | Schwere | Was daraus folgt |
|---|---|---|---|---|
| R1 | **Die Klickrate ist die große Unbekannte.** Für Profilbesuche pro Reel-View, Bio-Link-CTR und Comment-to-DM-Klickrate gibt es **keinen** methodisch sauberen Benchmark, nur Tool-Anbieter-Angaben | [E, Datenlücken 1–3](quellen/E_funnel_benchmarks.md) | **kritisch** | Liegt die reale Klickrate beim Conservative-Wert (0,25/1.000), bringt jede Nische < 10 € pro 1 Mio. Views. Das Modell ist dann tot. **Der 90-Tage-Test misst das in den ersten 30 Tagen.** |
| R2 | **Keine einzige belegte faceless IG-Page mit ≥ 5.000 € Affiliate-Gewinn/Monat.** Der klarste faceless Datenpunkt: 14,4 Mio. Views → 45 $ | [K, Abschn. 0, CS2](quellen/K_einkommens_evidenz_case_studies.md) | **kritisch** | Das Ziel ist nicht beobachtet, nur modelliert. Die Beweislast liegt beim Test, nicht bei der Studie. |
| R3 | **Der Markt bewertet Theme-Pages fast mit null.** 144 Mio. Views in 55 Tagen → 2 $/Monat Gewinn; eine 65k-Page mit Reels bis 22 Mio. Views wird für 60–80 $ angeboten | K, CS6 (Flippa, Reddit) | hoch | Reichweite allein hat keinen Wert. Nur Kaufintention monetarisiert. |
| R4 | **Instagram-Reichweite schrumpft.** Reels-Reach −35 % (2024→2025), Engagement −24 % YoY | [E, A](quellen/E_funnel_benchmarks.md) (Metricool, Socialinsider, VERIFIED) | hoch | Die Reichweitenannahmen für Monat 12 könnten zu hoch sein. Cross-Posting auf YT Shorts, TikTok und Pinterest ist Pflicht, kein Bonus. |
| R5 | **Originalitätsregel und KI-Labels.** Aggregator-Accounts werden seit 30.04.2026 nicht mehr empfohlen. Fotorealistische KI-Videos brauchen ein Label. „AI-generated profile“-Label seit 31.08.2026 (nur für KI-Personen) | [G, 1](quellen/G_plattform_policy_compliance.md) (VERIFIED) | mittel | Selbst generierte KI-Szenen gelten als original. **Slideshows aus Händlerbildern nicht** → dieses Format scheidet aus. Ob das „AI info“-Label die Reichweite senkt, ist UNKNOWN. |
| R6 | **Große Pages wählen oft Eigenshop/Dropshipping statt Affiliate** (myhousesdecors 4,1 Mio., @dog, Worldwide Gadgets) | [I, Abschn. 0/5](quellen/I_konkurrenz_home_lifestyle.md) | mittel | Indiz, dass Affiliate pro View weniger abwirft. Laut Auftrag ausgeschlossen, aber als Warnsignal ernst zu nehmen. |
| R7 | **Bessere Programme lehnen reine Kuratoren ab.** Beispiele: B03 („nur kuratiert“), Williams-Sonoma-Gruppe schließt Accounts ohne Creator-Identität aus, Thomann erst ab 5.000 Followern, Contorion ohne Influencer, OTTO nur über Stylink/Metapic | K (B03), A, B, C, D | mittel | Start mit Amazon und offenen Awin-/Impact-Programmen. Premium-Programme erst mit Traffic-Nachweis. Einnahmen der ersten 60 Tage laufen fast nur über Amazon. |
| R8 | **Amazon-Hürden.** Social-Account mit exakter URL registrieren; ~3 Verkäufe in 180 Tagen, sonst Schließung. Creators API (Produktfeed) erst ab 10 Verkäufen in 30 Tagen. **Pinterest ist kein zugelassener Kanal für Amazon-Links.** Seit 14.04.2026 keine Provision auf bezahlte/geboostete Werbung | [A](quellen/A_affiliate_programme_amazon_home_sleep_smarthome.md) (VERIFIED) | mittel | Automatisierung der Amazon-Produktdaten erst nach Traktion. Pinterest nur mit Nicht-Amazon-Programmen. Kein Ads-Boost auf Affiliate-Reels. |
| R9 | **Plattform-Risiko Konto.** Ein TikTok-Shop-Deal-Account wurde nach 5 Mio. Views wegen „unoriginal content“ gesperrt, ~3.000 $ Provision eingefroren | K, CS4 | mittel | Keine Re-Uploads, keine Duplikate. Mehrere Plattformen als Risikostreuung. |
| R10 | **Survivorship Bias.** Erfolgsgeschichten stammen oft von Kurs- und Tool-Verkäufern (CreatorFlow, Guide-Verkäufer) | K, Abschn. 7 | mittel | Alle CLAIMED-Werte bleiben im Modell höchstens Strong/Exceptional, nie Base. |

**Fazit Gesamtmodell:** Die ökonomische Logik steht. Ihre zwei wichtigsten Stellgrößen, **Klicks pro View** und **erreichbare Views**, sind aber unbelegt. Der Test muss beide messen, bevor skaliert wird.

---

## 2. Die Beispiel-Einwände aus dem Auftrag

| Nische | Behauptete Stärke | Stärkstes Gegenargument (mit Beleg) | Urteil |
|---|---|---|---|
| **Furniture** | hoher Warenkorb | CVR Home & Furniture nur **1,22 %** sitewide (Dynamic Yield), für Social-Traffic geschätzt 0,3–0,7 %. Williams-Sonoma/Pottery Barn/West Elm: **1 % bei 1 Tag** Attribution. home24, Maisons du Monde und IKEA ohne Programm (A). Regionale Speditionslieferung | **Widerlegt als Stand-alone.** Möbel nur als Beiwerk in Deko-/Setup-Szenen |
| **Fashion** | starke Infrastruktur (Breuninger 12 %, LTK) | DE-Retouren **45–55 %** → effektiv −54 % Provision. Zalando/ABOUT YOU ohne öffentliches Programm, OTTO nur über Stylink/Metapic. LTK/ShopMy funktionieren über Personen. KI-Outfits zeigen nie exakt das verlinkte Teil | **Widerlegt** (Score 46,0) |
| **Tech** | hohe Kaufabsicht | Amazon PC 2,5 %, Spiele 1 %, TV 2 %. Gadget-Finds hyper-gesättigt (Justice Buys 2,1 Mio., JayFindsThings 7,8 Mio., Offshore-Fabriken mit 15 Shorts/Woche). KI-Funktionsdemos sind irreführend | **Gadgets widerlegt** (49,0). **Desk Setups überleben** (Belege + Premium-Brands) |
| **Garden** | guter Warenkorb | Saison März–August; Plantura-**Stornoquote 41 %**; DE-Garten-Community pro Nutzer ähnlich aktiv wie EN (1,9×), also keine Lücke | **Widerlegt** als Stand-alone (43,6) |
| **Gaming** | perfekter KI-Fit | Economics-Score 1,0: Spiele 1 %, PC 2,5 %; junges globales Publikum (Geo 45 %). Gaming-Shorts werden mit Billigprodukten und Windows-Key-Codes monetarisiert (J) | **Widerlegt** (53,8) trotz AI 5 / Viral 5 |

---

## 3. Red Team gegen jede Top-10-Kombination

### #1 Küche & Küchengadgets – DE (63,7)
- **Stärkstes Gegenargument:** **1,74 € pro Bestellung** und ein Deckel bei ~37 Mio. deutschsprachigen IG-Nutzern. Strong × Strong ergibt nur **≈1.100 € Gewinn/Monat**. Für 10k bräuchte es 44 Mio. Views pro Monat, das Sechsfache der realistischen DE-Strong-Reichweite. Dazu kommt: Küchen-*Gadgets* leben von Funktionsdemos, und eine KI-Demo des Gadgets wäre irreführend (G).
- **Hält es?** Als Gadget-Page **nein**. Als **Setup-Page mit Geräten** (Siebträger, Küchenmaschine, Messer, Kochgeschirr) steigt die Provision pro Bestellung auf ~3,7 €. Statische Geräte lassen sich per Freisteller exakt darstellen. → **Umbau zu „Küchen- & Kaffee-Setups“ (K31)**.

### #2 BBQ & Outdoor Kitchen – US (60,2)
- **Stärkstes Gegenargument:** **Saisonalität.** Ein 90-Tage-Test ab Oktober 2026 fällt komplett in die Nebensaison. Die Ergebnisse wären nicht aussagekräftig, und ein Start im März verschiebt alles um 5 Monate. Außerdem ist die CVR für Outdoor-Küchen (5.000 $+) unbekannt. Food/Feuer per KI wirkt oft künstlich.
- **Hält es?** **Ja, als #2**, mit Start im Februar/März. Die beste Economics unter den LOW/MEDIUM-Risk-Nischen (Strong × Strong ≈4.400 €).

### #3 Espresso-Setups – EN/US (59,9)
- **Stärkstes Gegenargument:** Die hohen Raten (Breville bis 8 %, De'Longhi US bis 15 %) sind **„bis zu“-Angaben** (CLAIMED), die Standardrate ist nicht öffentlich. Espresso-Käufer recherchieren lange auf YouTube, kaufen also selten direkt aus einem Reel (niedrige CVR). Die Kaffee-Community erkennt und kritisiert KI-Visuals.
- **Hält es?** **Ja, zusammen mit Küche.** Allein ist die Zielgruppe zu klein (Reichweitenklasse „mittel“). Die Kombination „Kitchen & Coffee Setups“ (K32) verbreitert das Publikum und erhält die hohe Provision pro Bestellung.

### #4 Grill & Pizzaofen – DE (59,8)
- **Stärkstes Gegenargument:** Saison **und** DE-Deckel. Strong × Strong ergibt ≈1.600 €, selbst mit Strong-Funnel und DE-Ausnahme-Reichweite (10 Mio. Views) nur ≈4.800 €. **5k ist praktisch unerreichbar, 10k ausgeschlossen.**
- **Hält es?** **Abgewertet.** Taugt als saisonaler Zweit-Account oder als DE-Spiegel einer US-BBQ-Page, nicht als Hauptprojekt.

### #5 Küche & Küchengadgets – US (59,3)
- **Stärkstes Gegenargument:** **Sättigung.** Justice Buys (616k IG, 2,1 Mio. YT, Agentur-Management), JayFindsThings 7,8 Mio., dazu Offshore-„Finds“-Fabriken mit ~15 Shorts/Woche und Median 140k Views (dealify). Eine neue KI-Page konkurriert gegen Teams.
- **Hält es?** Als Gadget-Format **nein**. Als „Setup“-Format (Geräte in inszenierten Küchen) ist die Konkurrenz **deutlich dünner**: Kaffee-/Küchen-Setup-Pages mit Affiliate-Links wurden nicht gefunden (I). → **aufgehen in K32**.

### #6 Travel Gear – EN/US (58,9)
- **Stärkstes Gegenargument:** **Kaufseltenheit.** Einen Koffer kauft man alle paar Jahre. Reise-Content zieht Träumer und Planer an, nicht Käufer. Die starken Programme (Tortuga, Travelpro, NOMATIC) sind US-zentriert. eSIMs zahlen hohe Raten, aber bei 10–60 $ Warenkorb.
- **Hält es?** **Ja, als #3**, mit Abstrichen. Die beste Cross-Platform-Nische (Pinterest-Travel, Brand-Links dort erlaubt), evergreen und mit guter Produkttreue (Flat-Lays).

### #7 Home Decor Finds – DE/DACH (58,0)
- **Stärkstes Gegenargument:** **Produkttreue im Detail.** Eine Deko-Szene hat 8–15 kleine Objekte (Vasen, Kissen, Kerzen). Die Versuchung ist groß, KI-Deko zu zeigen und „ähnliche“ Produkte zu verlinken, was die Compliance-Grenze (c) berührt ([17](17_compliance.md)). EPC nur 1,99 €, Deckel wie bei #1. Pinterest bietet in Home Decor einen „weniger KI“-Filter (UNKNOWN\*).
- **Hält es?** **Ja, als bestes DE-Argument.** Es ist die einzige Nische mit **gemessener** Content-Lücke (19,5×) **und** belegter DE-Nachfrage (Personen-Storefronts mit 400k–1,3 Mio. Followern). Voraussetzung ist ein strenger Prozess: jedes Objekt ein echter Freisteller. → **#4**.

### #8 Desk Setups – EN/INT (57,9)
- **Stärkstes Gegenargument:** **Reifer, schrumpfender Markt.** Die großen Setup-Pages verlieren seit 2023 Follower (−8 bis −16 %). **Kit.co wurde am 11.05.2026 eingestellt**, viele Pages haben jetzt tote Linklisten. Herman Miller nimmt nur US-Partner. Setup-Enthusiasten erkennen KI-Renderings schnell.
- **Hält es?** **Ja, als #5.** Das Modell ist hier am besten **bewiesen** (11 von 23 Pages monetarisieren, @topdailysetups mit KI-Setups und Storefront). Die Kit.co-Schließung ist zugleich eine Chance: ~650k-Follower-Pages haben gerade keine funktionierenden Produktlisten.

### #9 Espresso-Setups – DE/DACH (57,4)
- **Stärkstes Gegenargument:** Die deutsche Kaffee-Community ist pro Nutzer ähnlich aktiv wie die englische (1,6×), also **keine Lücke**. Dazu der DE-Deckel (Strong × Strong ≈1.000 €).
- **Hält es?** **Nur als Teil von K31** (Küchen- & Kaffee-Setups DE).

### #10 Backyard Wellness – US (56,6)
- **Stärkstes Gegenargument:** **Die CVR ist komplett unbelegt.** Eine 10.000-$-Sauna wird nicht aus einem Reel heraus gekauft. Die Entscheidung dauert Monate und liegt meist außerhalb des 30-Tage-Cookies (Sun Home). Versand nur Lower 48. Das Modell unterstellt 0,05 % CVR für High-Ticket. Ist sie 0,01 %, bleiben nur die Amazon-Zubehörbestellungen.
- **Hält es?** **Als Wildcard.** Höchster AI-Fit (5), gute Passivität, gegenläufige Saison zu BBQ. Aber zu viel Unbekanntes für den Haupttest. Sinnvoll als späterer Zweit-Account, wenn der Funnel erprobt ist.

---

## 4. Was nach dem Red Team übrig bleibt

| Ergebnis | Kombinationen |
|---|---|
| **Umgebaut und zusammengeführt** | #1 + #3 + #5 + #9 → **Kitchen & Coffee Setups** (K32 EN/US, K31 DE als Spiegel). Die Gadget-Formate entfallen, stattdessen Geräte in KI-Szenen |
| **Bestätigt** | BBQ & Outdoor Kitchen US (mit Frühjahrsstart), Travel Gear EN/US, Home Decor Finds DE, Desk Setups EN |
| **Abgewertet** | Grill & Pizzaofen DE (Saison + Deckel → nur DE-Spiegel), Backyard Wellness US (Wildcard) |
| **Gestrichen** | Gadgets DE/US, Furniture stand-alone, Fashion, Garden, Gaming, Beauty (Compliance), AI Dream Interiors (keine Economics) |

**Ehrlicher Hinweis zur Synthese:** K31/K32 wurden erst **nach** dem ersten Ranking gebildet. Ihr Score (63,8 / 65,6) liegt nur 0,1 bzw. 1,9 Punkte über dem ursprünglichen #1 (K06, 63,7), also innerhalb der Modellunsicherheit. **Die Synthese ist nicht durch den Score gerechtfertigt, sondern durch die Red-Team-Befunde:**
- höhere Provision pro Bestellung (3,7 € statt 1,7 €)
- exakte Produkttreue über statische Geräte statt KI-Funktionsdemos
- keine belegte Affiliate-Konkurrenz im Setup-Format
- Q4 (Black Friday, Weihnachten) fällt als vermutliche Hauptsaison für Küchengeräte und Kaffeemaschinen genau in den Testzeitraum. Das ist eine Branchenannahme; in dieser Studie ist es nicht gemessen (MODEL ASSUMPTION)
