# Red-Team-Audit: Haben wir erfolgreiche KI-TikTok-Shop-Modelle übersehen?

Stand: 25.09.2026. Gegenstand: der Bericht `README.md` in diesem Ordner („alter Bericht"). Auftrag: den eigenen Bericht wie ein skeptischer Investor angreifen, aktiv Gegenbeweise suchen, Aussagen korrigieren. Dies ist kein neuer allgemeiner Bericht. Belege: `quellen/redteam/` (zehn Gegenbeweis-Protokolle mit Prüfvermerken, Monte-Carlo-Skripte und -Ergebnisse).

Kennzeichnung wie im alten Bericht: **Verified** (in TikTok-Rohdaten, Primärdokument oder selbst gesichtetem Dashboard), **Claimed** (Behauptung, auch Drittanbieter-Analytics wie Kalodata/FastMoss), **Estimated** (eigene Rechnung). „Nicht öffentlich verifizierbar", wo Daten fehlen. Alle Gewinnangaben sind **vor Arbeitszeit und Steuern**, sofern nicht anders gesagt.

## 0. Ergebnis vorab

### Haben wir erfolgreiche KI-TikTok-Shop-Modelle übersehen?

**Teilweise. Übersehen haben wir vor allem erfolgreiche Nicht-KI-Formate, die KI nachbauen könnte. Beim KI-Nachweis selbst sind die neuen Belege dünner, als sie auf den ersten Blick wirken.**

1. **Faceless-Formate mit echtem Produkt wurden unterschätzt, sind aber menschlich produziert.** Von 24 formatgeprüften US-Top-Verdienern sind 2 überwiegend faceless (18,2 % des kumulierten GMV) und 6 weitere mischen faceless Voice-over-Videos bei. Die zwei faceless Accounts standen 8–9 Monate in den US-Top-10 mit 0,96–2,37 Mio. USD GMV pro Monat (Kalodata, Claimed). KI ist dort **nicht nachgewiesen**. Bei einem Account gibt es einen unbestätigten Verdacht auf KI-Stimme. Nachweislich KI-Clips nutzen nur 2 der 24 Accounts (2,6 % des GMV), und diese Clips erreichen 63–2.817 Views. In UK, dem DE-nächsten Markt, machen rein faceless Accounts nur 1,6 % des GMV der Top-25 aus. Alle 13 UK-Creators mit geschätzt ≥ 3.000 € zeigen ihr Gesicht.
2. **Ein aktiver KI-Account wurde falsch eingeordnet.** @spongebobprodsz postet KI-gelabelte Produktvideos mit KI-Szenen um echte Produktbilder. Verified sind: 28.800 Follower, 1.172 Videos, die zehn neuesten Videos mit KI-Label und Produktlink (Median ca. 390 Plays). Dass der Account seit rund sieben Monaten so arbeitet, sagt nur ein Kursverkäufer. Das TikTok-Konto selbst stammt von 2021, eine frühere Nutzung oder ein Kauf ist möglich. Für einen Monat (Juli 2026) zeigt eine vom Kursverkäufer vorgeführte Kalodata-Karte 302.090 USD GMV (Claimed). Das wären geschätzt 12.000–54.000 USD Provision. Der alte Bericht hatte den Account als unbelegte Zeile unter falschem Format geführt.
3. **Einzelne fünfstellige Spitzenmonate mit KI-Anteil sind belegt oder behauptet.** Ein Slideshow-Account mit vermutlich fremden oder KI-generierten Personenbildern zeigt im Dashboard 51.700 USD geschätzte Provision in 28 Tagen (Screenshot gesichtet, danach Absturz). Ein Affiliate-Center-Screenshot zeigt 174.000 USD GMV für einen Account, den ein Tool-Verkäufer als KI bezeichnet (Handle und KI-Status nicht prüfbar).
4. **Top-down** legen die Biverse-Zahlen (514 KI-gelabelte Videos mit über 10.000 USD GMV in einem US-Monat, Methodik unveröffentlicht, Biverse verkauft selbst KI-Content) nahe: US-Betreiber mit ≥ 3.000 USD Provision im Monat liegen im zweistelligen bis niedrigen vierstelligen Bereich, mit ≥ 10.000 USD im einstelligen bis niedrigen dreistelligen Bereich (Estimated). Das ist ein Monat. Über Dauerhaftigkeit sagt es nichts.
5. **Nicht übersehen:** Vollvirtuelle KI-Influencer verkaufen weiterhin nicht. In den prüfbaren Listen (24 US- und 25 UK-Top-Accounts formatgeprüft) ist kein Account Kategorie A oder B. Dem steht eine unprüfbare Gegenaussage einer UK-Creatorin gegenüber.

### Sind 3k, 5k, 10k, 20k+ unrealistisch, oder hatten wir die falschen Accounts?

**Beides zum Teil. Die Stichprobe war einseitig, und das Modell hat wichtige Mechanismen nur erwähnt, aber nicht gerechnet.**

- **Stichprobe:** Die KI-Accounts des alten Berichts wurden über Presse, Klagen und Kursverkäufer gefunden, also überwiegend gescheiterte Accounts. Die erfolgreichen faceless Accounts standen in Analytics-Rankings, wurden aber nicht formatgeprüft.
- **Modell:** Das alte Modell rechnete mit Mittelwerten. Die Spitzenaccounts **konvertieren nicht besser**: Die fünf untersuchten Engine-Accounts liegen bei 0,29–0,68 Bestellungen je 1.000 Views, die gesamte Top-10 im Median bei 0,42. Das ist weniger als die 0,8 im alten „realistischen" Szenario. Sie haben aber 29–196 Mio. Views im Monat. Ein Teil davon stammt **vermutlich** aus Anzeigen, in denen Seller Affiliate-Videos ausspielen. TikTok zahlt darauf Provision, zu einem vom Seller wählbaren Satz. Wie groß dieser Teil ist, ist öffentlich nicht messbar. Das `isAd`-Flag in den Rohdaten steht auch auf Videos mit wenigen Hundert Views. Es beweist also keine bezahlte Reichweite. Der alte Bericht hatte diesen Kanal genannt, aber nicht modelliert.
- **Was bleibt:** 3k bis 20k+ sind im US-Markt **beobachtet**, und zwar vor allem mit menschlich produzierten Formaten (Gesicht oder faceless). Mit KI-Anteil gibt es einzelne Spitzenmonate und einen aktiven Account mit behauptetem fünfstelligem Monat. Die Fälle stammen aus dem obersten Promille. Sie hängen an Account-Alter, Seller-Beziehungen und vermutlich Werbebudgets und brechen häufig ein. Für DE/EU gibt es **keinen verifizierten** Fall über rund 3.000 €. Claimed sind im alten Bericht 4.700 €/Monat (DE, überwiegend Hands-only) und 23.400–32.000 €/Monat (menschliche Creators einer DE-Agentur). Für einen neuen Betreiber in DE bleiben 5.000 €+ in 90 Tagen **very unlikely**.

### Die wichtigsten Korrekturen am alten Bericht

| Alte Aussage | Korrektur |
|---|---|
| „Realistischer Account mit 5 Videos/Tag ≈ 1.650 € Gewinn" | War ein Mittelwert. Mit der alten Kostenannahme (589 €) liegt der Median beim kompetenten Archetyp bei rund 284 €, 36 % der Monate sind negativ. Mit 5 € je Creative plus Tools liegt der Median bei −29 €. In den ersten 30 Tagen sind ohnehin nur 3 Shopping-Videos/Tag erlaubt. |
| „10.000 € brauchen ca. 830 Videos, 20.000 € ca. 1.650" | Als allgemeine Regel falsch. Die Zahl hängt an Konversion, Reichweite und Seller-Verstärkung. Für KI-Betreiber ist sie eher bestätigt: Der einzige KI-Selbstbericht mit Videozahl nennt ca. 1.050 Videos für ca. 10.000 USD. |
| Faceless-Formate ohne Formatprüfung als „menschlich" gezählt | Faceless mit echtem Produkt ist eine eigene, starke Kategorie. Sie ist aber kein KI-Beleg. Ob KI die Stimme liefern kann, ohne Konversion zu kosten, ist die offene Frage. |
| „Dauerhafte vierstellige KI-Provisionen sind selten" | Im Kern bestätigt. Belegt sind KI-Spitzenmonate, aber kein über Monate verifizierter Verlauf. Absolut gibt es vermutlich zwei- bis dreistellig viele US-KI-Betreiber über 3.000 USD in einem Monat. |
| „KI-Accounts = Supplement-Netzwerke" | Zu eng. KI-Accounts mit Umsatz gibt es auch in Beauty, Home, Mode, Spielzeug und Sneakern. |
| DE-Markt als sehr klein beschrieben | Rund 43 Mio. EUR Affiliate-GMV pro Monat (Kalodata via Lengow, Claimed). Das Problem sind Warenkorb und Provisionssatz der meistverkauften Produkte. |
| Automatisierung und VA-Einsatz | Zu optimistisch. Shopping-Videos lassen sich über die öffentliche API nicht mit Produktlink posten. Die Weitergabe von Passwörtern verstößt gegen die US-Nutzungsbedingungen. |
| Portfolios | Eine Person darf in den USA höchstens 5 Creator-Accounts verifizieren. 10 Accounts gehen nur als Agentur echter Creators. |

### Was als Nächstes zu testen ist

Das Audit **bestätigt im Kern die Test-Empfehlung des alten Berichts** (30 Tage DE, echtes Produkt in echten Händen, KI hinter der Kamera). Es schärft sie an vier Stellen: eine Vorab-Prüfung des Produktangebots vor jeder Ausgabe, eine vorab festgelegte STOP-Regel mit Stückkosten-Kriterium, ein randomisierter Vergleich eigene Stimme vs. KI-Stimme (nur große Effekte erkennbar) und aktive Seller-Ansprache. Als Alternative steht E (eigenes Gesicht plus KI-Produktion), denn in UK verdienen alle Spitzenaccounts mit Gesicht. Der Test kann nicht beweisen, dass 10.000 € möglich sind. Er kann schnell und billig zeigen, dass Operator, Format und Markt nicht funktionieren (Kapitel 15).

### Aufbau

1 Audit der sieben Kernaussagen · 2 Gegenbeweise · 3 Kategorien A–H · 4 Monte Carlo · 5 Ausreißer-Hypothese · 6 Produkt-Ökonomie · 7 Portfolio · 8 Sales-Engine der stärksten Accounts · 9 Winner-Definition · 10 Creator-Ökonomie · 11 Echte vs. theoretische KI-Vorteile · 12 Solo-Operator nach 90 Tagen · 13 Creative Factory · 14 Verdict-Tabelle · 15 30-Tage-Test · Anhang Methodik und Grenzen.

## 1. Audit der sieben Kernaussagen

Jede Aussage des alten Berichts wird gegen die neue Evidenz gestellt. „Konfidenz" meint die Konfidenz in die **ursprüngliche** Aussage nach dem Audit. Die Spalte „Korrektur" sagt, wie die Aussage heute lauten müsste.

### Übersicht

| # | Ursprüngliche Aussage | Konfidenz nach Audit | Korrektur |
|---|---|---|---|
| C1 | Vollvirtuelle KI-Influencer funktionieren für TikTok Shop praktisch nicht | **HIGH** für Personas (A); **MEDIUM** für KI-Personen als Produktpräsentatoren (B) | Gilt für Influencer-Personas. Für KI-Personen, die ein echtes Produkt zeigen, gibt es behauptete Spitzenmonate (ein Screenshot mit sechsstelligem GMV, KI-Status nur behauptet), aber keinen prüfbaren Fall. |
| C2 | KI-Shop-Accounts mit hohen Views sind meist kurzlebige Supplement-Netzwerke | **MEDIUM** für „meist kurzlebig", **LOW** für „Supplement" | Die Mehrheit bricht nach Wochen bis Monaten ein. KI-Accounts mit Umsatz gibt es aber auch in Beauty, Home, Mode, Spielzeug, Sneakern und Handyhüllen. |
| C3 | Dauerhafte vierstellige Provisionen mit KI sind selten | **MEDIUM–HIGH** | Bestätigt, aber falsch gerahmt: Vierstellige Monate sind für **alle** Affiliates selten. Mit KI-Anteil gibt es einzelne belegte oder behauptete fünfstellige **Monate**, aber keinen über mehrere Monate verifizierten Verlauf. Menschlich produzierte faceless Formate erreichen dauerhaft vier- bis sechsstellige Monate. Das ist ein Hinweis auf ein kopierbares Format, kein Beleg für KI. |
| C4 | 10.000+ USD-Behauptungen stammen meist von Kursverkäufern | **HIGH** für **KI-bezogene** Behauptungen; **falsch** als Aussage über den Markt | 10.000+-Verdiener existieren in großer Zahl und meist ohne Kurs, nachweisbar in Analytics-Rankings. Die KI-bezogenen 10k-Zahlen kommen dagegen fast alle über Verkäufer, teils als weitergereichte Analytics-Schätzungen über fremde Accounts. |
| C5 | Ein realistischer Account mit 5 Videos/Tag bringt ca. 1.650 EUR Gewinn | **LOW** als „typisches Ergebnis"; **MEDIUM** als Größenordnung eines funktionierenden Kategorie-Führers | Der Wert war ein Mittelwert. Der Median ist deutlich niedriger, die Streuung riesig. 5 Videos/Tag sind in den ersten 30 Tagen regelbedingt nicht möglich (Pilotprogramm: max. 3 Shopping-Videos/Tag). |
| C6 | 10.000 EUR brauchen ca. 830 Videos/Monat | **LOW** als allgemeine Regel; **MEDIUM** für KI-Betreiber | Für langjährige menschliche Spitzenaccounts falsch (60–600 Videos). Für KI-Betreiber stützt der einzige Selbstbericht mit Videozahl die Größenordnung (ca. 1.050 Videos für ca. 10.000 USD). |
| C7 | 20.000 EUR brauchen ca. 1.650 Videos/Monat und vermutlich ein Team | **LOW** für die Videozahl, **MEDIUM** für „Team" | Teams sind bei einigen Spitzenaccounts sichtbar, bei anderen nicht. Die Regeln erlauben einer Person bis zu 5 US-Accounts mit je 30 Shopping-Videos/Tag nach dem Pilot. |

### C1: Vollvirtuelle KI-Influencer funktionieren praktisch nicht

- **Stützende Daten:** 0 von 24 formatgeprüften US-Top-Creators (aus 41 Creators der Kalodata-Monatslisten November 2025 bis August 2026) und 0 von 25 UK-Top-Creators (FastMoss H1 2026) sind Kategorie A oder B. Kein bekannter virtueller Influencer hat Shop-Flags. Clorox' animierte Markenfiguren erzeugten 8,4 Mio. Impressions und gut 300 Pine-Sol-Bestellungen. Creator-geführte Kampagnen derselben Firma brachten über 60.000 (Modern Retail, Claimed).
- **Stichprobe:** rund 56 formatgeprüfte Spitzenaccounts (24 US, 25 UK, ca. 7 aus einem weiteren US-Ranking) plus 55 Accounts aus dem alten Bericht.
- **Gegenbeispiele:** Ein Affiliate-Center-Screenshot mit 174.000 USD GMV in 30 Tagen für einen Account, den ein Tool-Verkäufer als KI bezeichnet (Handle nicht lesbar, im Video eingeblendet sind 184.000). Eine menschliche UK-Creatorin nennt zwei KI-Funnel-Accounts auf UK-Rang 2 und 3 im Januar 2026, ohne Handle. @virtuosos2 erreichte 1,2 Mio. Plays mit einem komplett KI-generierten Sketch (Verified); laut Betreiber wurde der Account danach für Shop-Inhalte gesperrt.
- **Fehlende Daten:** Handles der B-Accounts; TikToks AIGC-Label erfasst unmarkierte KI-Inhalte nicht; es gibt keine öffentliche Liste „KI-Accounts nach GMV".
- **Selektions-Bias:** Die Top-Listen zeigen nur „independent creators". Seller-eigene Accounts mit KI-Figuren fallen heraus. 17 der 41 US-Creators wurden nicht formatgeprüft.
- **Survivorship-Bias:** gering, denn die Aussage ist negativ und würde durch Überlebende eher widerlegt.
- **Risiko versteckter Erfolgreicher:** mittel für B. Betreiber haben Gründe, sich zu verstecken (Regelrisiko, Nachahmer).
- **Konfidenz:** HIGH für A, MEDIUM für B.

### C2: KI-Accounts mit hohen Views sind meist kurzlebige Supplement-Netzwerke

- **Stützende Daten:** 6 von 9 KI-Accounts aus dem alten Bericht sind tot oder inaktiv. Neu: @pinecommerce seit Juni 2026 inaktiv, @turnersells seit 16.08.2026, der Handle eines früheren InVideo-Fallbeispiels ist 2026 neu registriert, @virtuosos2 laut Betreiber gesperrt, @wellness.tips07 hat 117 von 253 Videos gelöscht. Coaching-Fälle berichten von mehreren Sperren. Ein Anbieter berichtet, TikTok habe ihn aufgefordert, alles zu löschen.
- **Stichprobe:** ca. 20 KI-Accounts mit Verlaufsdaten.
- **Gegenbeispiele:** @spongebobprodsz (KI-gelabelte Beauty-/Home-Videos, heute aktiv; Dauer nur laut Kursverkäufer rund 7 Monate); KI-Accounts in Mode, Deko, Spielzeug, Sneakern (Tool-Verkäufer-Screenshots), Handyhüllen (@turnersells), Fashion (@megs.homefinds, noch aktiv).
- **Fehlende Daten:** Verlaufsdaten gesperrter Accounts; Zahl der KI-Accounts, die unauffällig weiterlaufen.
- **Selektions-Bias:** KI-Accounts werden meist über Skandale oder Kursverkäufer bekannt. Beides überrepräsentiert Supplements.
- **Survivorship-Bias:** umgekehrt, denn wir sehen vor allem die Toten.
- **Risiko versteckter Erfolgreicher:** mittel.
- **Konfidenz:** MEDIUM für „meist kurzlebig", LOW für „Supplement".

### C3: Dauerhafte vierstellige Provisionen mit KI sind selten

- **Stützende Daten:** 67 von 80 zufällig gezogenen US-Affiliates hatten in 28 Tagen null GMV (FastMoss-Ziehung eines Reddit-Analysten, Claimed; der Nenner enthält auch inaktive Affiliates). Bei einer Marke mit 21.365 Affiliates hat nur etwa jeder achte überhaupt gepostet, rund 99 % hatten keinen Umsatz. Bei Built Bar verdiente der Durchschnitts-Affiliate rund 7 USD in 28 Tagen. Die KI-gelabelten Clips zweier Top-Accounts erreichen 63–2.817 Views. Für kein KI-Format gibt es einen über mehr als drei Monate verifizierten vierstelligen Verlauf.
- **Stichprobe:** Verteilungsdaten über zehntausende Affiliates; ca. 20 KI-Accounts.
- **Gegenbeispiele mit KI-Anteil:** @spongebobprodsz (ein behaupteter Monat mit 302.090 USD GMV, geschätzt 12.000–54.000 USD Provision); @mackfinds_ (vermutlich fremde oder KI-Bilder, 51.700 USD geschätzte Provision in 28 Tagen, Screenshot gesichtet, danach Absturz); Top-down aus den Biverse-Zahlen: zwei- bis niedrig vierstellig viele US-Betreiber ≥ 3.000 USD in einem Monat (Estimated, Vendor-Daten).
- **Gegenbeispiele ohne KI-Nachweis:** @hannahbentley (faceless, Stimme laut Transkript vermutlich menschlich, 9 von 10 Monaten Top-10); @cakedfinds (faceless, unbestätigter Verdacht auf KI-Stimme, 8 Monate Top-10); ein italienischer Affiliate mit ca. 3.000 EUR/Monat seit 7 Monaten (faceless, Stimme unbekannt). Diese Fälle zeigen ein erfolgreiches Format, nicht erfolgreiche KI.
- **Fehlende Daten:** Ob die Stimme bei @cakedfinds synthetisch ist; Provisionen statt GMV; Anteil werbefinanzierter Views; Verlauf von @spongebobprodsz über mehr als einen Monat.
- **Selektions-Bias:** stark, denn die Gegenbeispiele stammen aus den obersten 0,002 % (41 von rund 2 Mio. Affiliates) oder aus Verkäufer-Material.
- **Survivorship-Bias:** stark bei den Gegenbeispielen.
- **Risiko versteckter Erfolgreicher:** hoch für D/E. KI-Skripte und KI-Stimmen tragen kein Label und sind von außen nicht zu erkennen.
- **Konfidenz:** MEDIUM–HIGH. Die Aussage war falsch gerahmt: Nicht KI macht vierstellige Monate selten, sondern die Plattform-Ökonomie für alle.

### C4: 10.000+-Behauptungen kommen meist von Kursverkäufern

- **Stützende Daten:** Alle YouTube-Zahlen dieser Suche sind Selbstauskünfte, fast alle von Coaches, Tool- oder Kursverkäufern. Auf Reddit wurde Astroturfing nachgewiesen (identische Texte eines Kursverkäufers und eines angeblich neutralen Nutzers). Selbst ein Top-10-Account verkauft in der Bio ein System („How We Run $100K+/mo TikTok Shop – Learn the system").
- **Stichprobe:** ca. 60 Einkommensbehauptungen aus YouTube, Reddit, X, Blogs; 100 Monatseinträge aus Analytics-Rankings.
- **Gegenbeispiele:** 41 Creators mit mindestens 0,85 Mio. USD GMV in einem Monat, meist ohne Kurs. Mehrere organisch geprüfte Reddit-Nutzer berichten 4.000–36.000 USD/Monat, meist menschlich oder LIVE. Ein Top-Creator nennt öffentlich „$100,000 per month in commission".
- **Fehlende Daten:** Provisionen der Ranking-Accounts (nur GMV); KI-bezogene 10k-Fälle ohne Verkäufer als Überbringer.
- **Selektions-Bias:** Wer öffentlich Zahlen nennt, hat meist etwas zu verkaufen. Erfolgreiche Betreiber ohne Produkt schweigen eher.
- **Survivorship-Bias:** mittel.
- **Risiko versteckter Erfolgreicher:** hoch. Das ist der Kern der Aussage: Die Behauptungsquelle sagt wenig über die Realität.
- **Konfidenz:** HIGH für KI-bezogene Behauptungen. Als Aussage über den gesamten Affiliate-Markt war sie irreführend. Einige KI-Zahlen sind Analytics-Schätzungen über fremde Accounts, die Verkäufer nur weiterreichen. Sie pauschal zu verwerfen, wäre zu streng. Sie ungeprüft zu übernehmen, wäre zu leichtgläubig.

### C5: 5 Videos/Tag ≈ 1.650 EUR Gewinn

- **Stützende Daten:** Ein Massen-Poster berichtet rund 11 USD Provision pro Video über 900 Videos (Modell: 14,97 EUR). Mittelklasse-Faceless-Accounts in UK liegen bei geschätzt 1.100–1.900 EUR Provision/Monat, allerdings nach über 30 Monaten.
- **Stichprobe:** ca. 10 Accounts mit Monatswerten, dazu Verteilungsdaten.
- **Gegenbeispiele nach unten:**
  - 67 von 80 zufälligen US-Affiliates ohne GMV in 28 Tagen.
  - Die Kalodata-Top-10 haben im Median 25,9 USD GMV je 1.000 Views. Die 30,4 USD des alten „realistischen" Szenarios liegen also **über** dem Niveau der Spitzenaccounts. Für einen normalen Account war die Konversionsannahme zu optimistisch.
  - @annsdailydeals ist UK-Food-Nr.-1 in 6 von 6 Monaten und kommt mit ca. 186 Beiträgen/Monat auf geschätzt ca. 1.800 EUR **Provision**. Wenn selbst ein Kategorie-Führer nur dort landet, ist 1.650 EUR **Gewinn** kein „realistischer" Wert für einen neuen Account.
  - Monte Carlo (Kapitel 4): Für den kompetenten Archetyp mit 150 Videos und der alten Kostenannahme liegt der Mittelwert bei 1.362 EUR, der **Median bei 284 EUR**, 36 % der Monate sind Verlustmonate.
- **Gegenbeispiele nach oben:** Italiener mit ca. 3.000 EUR/Monat, faceless (1,8× Modell, aber Top 100 seiner Kategorie).
- **Fehlende Daten:** echte Monatsverläufe neuer Accounts; Kosten der Berichtenden.
- **Selektions-Bias:** Die Stützfälle sind Kategorie-Führer.
- **Survivorship-Bias:** hoch, denn gescheiterte Accounts berichten selten.
- **Risiko versteckter Erfolgreicher:** mittel.
- **Regelkorrektur:** Im Pilotprogramm (US unter 5.000 Follower mindestens 30 Tage, EU 30 Tage) sind höchstens 3 Shopping-Videos/Tag erlaubt.
- **Konfidenz:** MEDIUM als Größenordnung eines funktionierenden Kategorie-Führers, LOW als Erwartung für einen neuen Account.

### C6: 10.000 EUR ≈ 830 Videos/Monat

- **Stützende Daten:** Der einzige KI-Selbstbericht mit Videozahl (Coaching-Kunde) nennt ca. 1.050 Videos/Monat auf mehreren Accounts für ca. 10.000 USD, die meisten Accounts gesperrt. Massen-Poster liegen bei 1,67–11 USD pro Video.
- **Stichprobe:** ein KI-Selbstbericht mit Videozahl, zwei Massen-Poster, drei menschliche Spitzenaccounts mit geschätzter Videozahl.
- **Gegenbeispiele:** @hannahbentley mit ca. 60–90 Videos/Monat im sechsstelligen GMV-Bereich (menschlich produziert, Account seit 2019). @mackfinds_ mit 191 Beiträgen in 12 Monaten und einem fünfstelligen Monat.
- **Fehlende Daten:** Videozahlen und Provisionen neuer KI-Accounts über mehrere Monate.
- **Selektions-Bias:** Die Gegenbeispiele sind die obersten 0,002 %. Ihr Erfolg beruht auf Account-Alter und vermutlich Seller-Verstärkung.
- **Survivorship-Bias:** stark.
- **Risiko versteckter Erfolgreicher:** mittel.
- **Fehler im alten Modell:** feste mittlere Reichweite von 3.965 Views, keine modellierte Seller-Verstärkung.
- **Konfidenz:** LOW als allgemeine Regel, MEDIUM für KI-Betreiber.

### C7: 20.000 EUR ≈ 1.650 Videos/Monat, vermutlich Team

- **Stützende Daten:** Teams oder Firmen hinter „unabhängigen" Creators sind bei einigen Accounts sichtbar (LIVE-Studio mit Hosts, Firmen-E-Mail, Agentur). Drei Accounts posten geschätzt 270–570 Videos pro Monat.
- **Stichprobe:** ca. 24 Spitzenaccounts.
- **Gegenbeispiele:** Ein Creator nennt 20–30 Videos pro Tag allein. @hannahbentley wirkt solo. Die Regeln erlauben einer Person bis zu 5 US-Creator-Accounts mit je 30 Shopping-Videos/Tag nach dem Pilot.
- **Fehlende Daten:** Wer hinter den Accounts arbeitet, ist öffentlich nicht sichtbar.
- **Selektions-Bias und Survivorship-Bias:** wie C6.
- **Risiko versteckter Erfolgreicher:** mittel.
- **Konfidenz:** LOW für die Videozahl, MEDIUM für „Team" als häufige, aber nicht notwendige Bedingung.

### Gemeinsamer Fehler aller sieben Aussagen

Der alte Bericht hat zwei Dinge **erwähnt, aber nicht modelliert**:

1. **Faceless-Formate mit echtem Produkt.** Sie standen als Modell „Reale Produktclips + KI-Voiceover" im Bericht, aber die Spitzenverdiener wurden nicht formatgeprüft. Deshalb fehlte die Beobachtung, dass dieses Format, menschlich produziert, zu den dauerhaftesten US-Spitzenformaten gehört.
2. **Seller-finanzierte Ausspielung.** Der Bericht nannte sie als Wettbewerbsvorteil einzelner KI-Accounts, rechnete aber nur mit organischer Reichweite. Die Stichprobenmethode (neueste 10–20 Videos) unterschätzt die Monatsreichweite der Spitzenaccounts um den Faktor 4,7 bis 1.560. Wie viel davon bezahlt ist, bleibt offen.

Beides ändert nichts daran, dass der **typische** Account wenig verdient. Es ändert das Urteil über den **oberen Rand** im US-Markt. Dort war der alte Bericht zu pessimistisch, vor allem für menschlich produzierte Formate.

## 2. Aktive Suche nach Gegenbeweisen

### 2.1 Wie gesucht wurde, und wo die Suche selbst verzerrt ist

Zehn Such-Agenten mit je einem eigenen Suchwinkel hatten den Auftrag, den alten Bericht zu widerlegen. Sie arbeiteten mit einem **gemeinsamen Briefing**. Darin stand ausdrücklich, die Red-Team-Frage sei, ob der alte Bericht zu pessimistisch war. Das kippt die Fundlage bewusst in Richtung optimistischer Funde. Bei zwei Agenten (US- und UK-Top-Verdiener) wurden die drei stärksten Funde von getrennten Prüfern erneut geöffnet. Die übrigen acht haben ihre drei stärksten Funde selbst gegengeprüft. Zwei unabhängige Gutachter haben den Entwurf dieses Audits anschließend auf Zahlen und auf Verzerrung in beide Richtungen geprüft. Die Korrekturen sind eingearbeitet. Alle Protokolle liegen in `quellen/redteam/`.

**Abdeckung nach Quelle**

| Quelle | Was gemacht wurde | Beste Fundstelle | Grenze oder Null-Ergebnis |
|---|---|---|---|
| TikTok direkt | Profile, neueste Videos, KI-Label, `isAd`, Frame-Analyse von 2–3 Videos je Account für ca. 80 Accounts | Formatprüfung der US-/UK-Spitzenaccounts; @spongebobprodsz | Discover- und Tag-Seiten liefern Bots keine Inhalte; nur neueste Videos abrufbar |
| YouTube | alle 15 vorgegebenen Suchbegriffe plus zwei Zusatzbegriffe (TTS, Voice-over), 12 Transkripte | Aussage einer menschlichen UK-Creatorin über KI-Konkurrenz; Coaching-Fälle | Kein Affiliate-Dashboard direkt gesichtet (Video-Analyse-Kontingent erschöpft, Downloads blockiert) |
| Reddit | Archiv-Suche in 7 Shop-Subreddits (444 Posts, 313 Kommentare), Autorenhistorien | italienischer Faceless-Affiliate; Negativbelege; Astroturfing-Nachweis | Allgemeine Subreddits (passive_income, sidehustle u. a.) teils wegen API-Drosselung ausgefallen |
| X | 5 Suchen, Tweets mit Bildern geladen | Dashboard-Screenshot von @mackfinds_ | wenig Treffer |
| Google/News, Blogs | Google-News-RSS und Websuche mit den vorgegebenen Begriffen; Net Influencer, Modern Retail, Digiday, Affiverse, FastMoss-, Kalodata-, EchoTik-Blogs | 10 Monatsrankings US; UK-Ranking H1 2026; Produkt- und Videofallstudien | Keine Primärdatenbanken zugänglich, nur Blogs und Screenshots |
| Communities (Skool, Whop) | öffentliche Seiten gelesen | Mitgliederzahlen, Verkaufsversprechen | keine prüfbaren Einkommenszahlen |
| Interviews | Net-Influencer-Interviews mit Spitzen-Creators | @be.lush: „$100,000 per month in commission" | Selbstauskunft |
| Podcasts | gesucht | – | nichts mit prüfbaren Zahlen gefunden |
| Discord | – | – | nicht erreichbar |
| Agenturen, Netzwerke | Websuche, Presse | Faceless-Netzwerk mit 21.000 Mitgliedern (Digiday) | Zahlen betreffen Markendeals, nicht Shop-Provision |
| Affiliate-Software-Anbieter | Tool-Blogs und -Videos (Krafie, BatchBot, Kalodata/Kaloclip, Colaba) | Affiliate-Center-Screenshot mit 174.000 USD GMV | starker Verkäufer-Bias |
| Analytics-Plattformen | Kalodata/FastMoss/EchoTik über Blogs und Presse | Top-10-Listen mit GMV, Items, Views | Schätzungen, keine Provisionen |
| TikTok-Regeln | Seller University US/UK/DE/IE, Developer-Doku, Ads Help | Account-Limits, Pilot, Provision auf Ads-GMV | – |

### 2.2 Die stärksten Gegenbeweise

| # | Fund | Kategorie | Metrik und Höhe | Evidenz | Prüfergebnis | Trifft |
|---|---|---|---|---|---|---|
| G1 | @hannahbentley: nur Hände + Produkt + Voice-over, 9 von 10 Monaten in den US-Top-10 | F (menschlich produziert) | 0,99–2,37 Mio. USD GMV/Monat, Ø 1,49 Mio. → geschätzt 67.000–201.000 USD Provision (5–15 %) bzw. 134.000–268.000 USD (10–20 %), nach Retouren | Analytics (Kalodata, Claimed) + Format Verified | Teilweise bestätigt: Format F korrekt, Stimme laut Transkript vermutlich menschlich, 8 von 10 neuesten Videos `isAd`, Account seit 2019. **Kein KI-Beleg.** | C6, C7 |
| G2 | @cakedfinds: Hände + Karton + Skript-Template, 8 Monate in Folge Top-10, geschätzt ca. 19 Videos/Tag | F, Verdacht D | Ø 1,16 Mio. USD GMV/Monat → geschätzt 52.000–157.000 USD (5–15 %) bzw. 104.000–209.000 USD (10–20 %) | Analytics + Format Verified; KI-Stimme nur Claimed (Coach, Reddit-Frage), Audio-Ähnlichkeit nur Indiz | Teilweise bestätigt; seit 02.09.2026 kein neues Video | C6; C3 nur falls KI-Stimme bestätigt |
| G3 | Top-US-Liste: Formatanteile unter 24 geprüften Top-Verdienern | F, G | 2 überwiegend faceless (18,2 % des GMV); 2 mit nachweislich KI-Clips (2,6 % des GMV, Clips mit 63–2.817 Views); 6 mischen faceless Voice-over bei | Analytics + Format Verified | Teilweise bestätigt: Der „gemischt"-Anteil wächst mit jedem zusätzlich geprüften Video und misst, ob ein Account das Format überhaupt nutzt, nicht, wie viel er damit verdient | C3 nur als Definitionsfrage |
| G4 | @mackfinds_: Foto-Slideshows mit vermutlich fremden oder KI-Personenbildern + echtem Produktfoto | H | 51.700 USD geschätzte Provision in 28 Tagen (Mai/Juni 2026), 30 % Satz | Dashboard-Screenshot selbst angesehen (in einem Tweet), Account Verified | Teilweise bestätigt: echter Spitzenmonat, danach Absturz (heute Median ca. 1.600 Plays), Persona gewechselt, Vorher-nachher-Muster regelwidrig | C3 (Monat), C6 |
| G5 | Affiliate-Center-Screenshot, von einem Tool-Verkäufer als KI-Account vorgestellt | unbekannt (laut Verkäufer KI) | 174.000 USD GMV in 30 Tagen (im Video eingeblendet: 184.000), 5.330 Artikel, 26,6 USD GMV je 1.000 Views → geschätzt 15.700–23.500 USD Provision | Screenshot gesehen; Handle nicht lesbar; KI-Status und Format nur behauptet | Teilweise bestätigt (GMV-Wert), Rest nicht prüfbar | C1 (schwach) |
| G6 | UK-Creatorin (menschlich, selbst Rang 4) nennt UK-Rang 2 und 3 im Januar 2026 „AI accounts doing a funnel" | B | nicht beziffert | Selbstauskunft gegen eigenes Interesse | Nicht prüfbar (kein Handle; in den geprüften FastMoss-H1-Listen kein A/B-Account) | C1 (schwach) |
| G7 | Italienischer Affiliate, faceless, seit 7 Monaten | F | 25.000–30.000 EUR GMV, ca. 3.000 EUR Provision pro Monat | Selbstauskunft, Autorenhistorie organisch | Teilweise bestätigt (plausibel, kein Handle; Top 100 seiner Kategorie) | C5 (nach oben), DE/EU-Einschätzung |
| G8 | Konversion der Spitzenaccounts | – | Fünf Engine-Accounts: 0,29–0,68 Bestellungen und 10–59 USD GMV je 1.000 Views. Ganze Top-10: Median 0,42 Bestellungen (Spanne 0,10–4,01) und 25,9 USD GMV (Spanne 4,7–170) | Analytics | Bestätigt als Rechnung | C5 (Konversion war zu optimistisch angesetzt), C6 |
| G9 | Provision auf Anzeigen-GMV von Affiliate-Videos | – | TikTok: „affiliate creative commission … based on qualified GMV generated by affiliate videos when used in ads"; Seller kann eigenen Satz setzen. 70–100 % der neuesten Videos der Top-Accounts tragen `isAd = true`. Monatsreichweite 4,7- bis 1.560-mal höher als organische Hochrechnung | TikTok Ads Help (Stand März 2026) Verified; `isAd` Verified als Feldwert | **Mechanismus bestätigt, Umfang offen.** `isAd` steht auch auf Videos mit 61–534, ca. 390 oder 422–24.700 Plays. Das Flag beweist also keine bezahlte Reichweite | C5, C6, C7 (als Hypothese) |
| G10 | @virtuosos2: 100 % KI-generierte Veo-Sketche mit Produkt-CTA | A/G | 1,2 Mio. Plays, 6,5 % Like-Rate (Verified); „over $100k GMV" kumuliert (Claimed) | TikTok Verified, GMV Claimed | Laut Betreiber für „automated content" gesperrt, 1.500 USD eingefroren; Profil zeigt noch Beiträge vom Juni 2026 | C1 (schwach), stützt C2 |
| G11 | Reddit-Nutzer, organisch geprüft: „$5-$8k a month using ai to create my TTS videos. Been at it since April" | unbekannt | 5.000–8.000 USD/Monat | Selbstauskunft, ein Satz | Nicht prüfbar. „TTS" bedeutet in dieser Community meist „TikTok Shop", nicht Text-to-Speech. Kein Beleg für Kategorie D | C3 (schwach) |
| G12 | DE-Markt größer als angenommen | – | 174,7 Mio. EUR GMV vom 11.04. bis 09.07.2026, 73,8 % über Affiliates → ca. 43 Mio. EUR Affiliate-GMV pro Monat | Kalodata via Lengow (Claimed) | nicht separat geprüft | alter Bericht Kapitel 9 |
| G13 | @spongebobprodsz: KI-Szenen um echte Produktbilder, Skript-Voice-over, 6–10 Beiträge/Tag | G | Ein behaupteter Monat (Juli 2026) mit 302.090 USD GMV → geschätzt 12.000–54.000 USD Provision | Verified: 28.800 Follower, 1.172 Videos, 10 von 10 neuesten Videos mit KI-Label und Produktlink, 5 von 10 `isAd`, Median ca. 390 Plays. Claimed: Umsatzkarte und Aktivitätsdauer (Kursverkäufer). Konto angelegt 2021 | Teilweise bestätigt: aktiv und KI-gelabelt; Umsatz und Dauer nicht unabhängig prüfbar; möglicherweise älteres oder gekauftes Konto | C2, C3 (Monat), C6 |
| G14 | Top-down aus Biverse (514 KI-Videos > 10.000 USD, 76.314 mit 100–10.000 USD GMV im August 2026, US) | – | 49–143 Mio. USD GMV/Monat aus KI-gelabelten Videos; robust nur als Band: zwei- bis niedrig vierstellig viele Betreiber ≥ 3.000 USD, einstellig bis niedrig dreistellig ≥ 10.000 USD in diesem Monat | Estimated auf Vendor-Daten (Methodik unveröffentlicht; Biverse ist offizieller TikTok-Shop-Partner und verkauft KI-Content); Label-Zählung enthält Marken-Accounts, Betreiberzahl angenommen | Größenordnung plausibel, Punktwerte Faktor 10 unsicher, keine Aussage zur Dauer | C3, C4 |

### 2.3 Gegenbeweise, die sich als schwach oder falsch herausstellten

- **„Top-Verdiener sind heimlich KI":** nicht bestätigt. Die KI-gelabelten Clips der beiden Top-Accounts mit KI-Anteil (@kevin.finds, @airgeeksrc) erreichen 63–2.817 Views. Deren Umsatz kommt aus menschlichen Videos, LIVE und einem faceless Viralhit.
- **„Hohes GMV pro Follower = faceless":** widerlegt. @girlybeautyessentialshq (6.747 Follower, 693.183 GBP GMV in H1) zeigt eine echte Frau vor der Kamera.
- **KI-Einkommensbehauptungen auf Reddit/X:** mehrfach Astroturfing. Ein angeblich neutraler Nutzer postete wortgleiche Texte wie ein Kursverkäufer. Ein viraler „$4,078 today"-Screenshot war kein TikTok-Shop-Dashboard.
- **InVideo-Fallbeispiel:** Ein 100 %-KI-Video soll rund 30.000 USD in 7 Tagen gemacht haben (Kalodata, vom Tool-Anbieter gezeigt). Die oft zitierten „$155,000 in the last 7 days" waren der Umsatz des Top-Creators des Produkts (@kevin.colson0), dessen KI-Status unbekannt ist. Sein Handle ist 2026 neu registriert.
- **„0 → 132.324 USD in 45 Tagen" (KI):** Laut Erzähler forderte TikTok die Löschung aller Videos. Die Top-Videos sind gelöscht.

### 2.4 Negativbelege, die neu hinzukamen

- 1 Mio. Views mit einem faceless Sneaker-Video brachten 300 USD Provision. Ein per Anzeige verstärktes Video mit 2,5 Mio. Views brachte rund 150 USD Umsatz (beide Reddit, Claimed).
- Faceless + KI-Avatare über 3 Monate: 35 GBP. KI-Videos: 18 Verstöße vor dem 25. Post (Reddit, Claimed).
- Mehrere organisch geprüfte Affiliates berichten Einbrüche von 5.000–10.000 USD auf unter 1.000 USD pro Monat im ersten Quartal 2026 sowie Sperren wegen Verknüpfung mit anderen Accounts oder „unoriginal content" (Reddit, Claimed).
- Ein Massen-Poster wurde ab Mitte Mai 2026 auf 3 Shopping-Videos pro Woche gedrosselt (Reddit, Claimed). Das entspricht dem US-Limit „Extended Pilot".

### 2.5 Zwischenfazit

Die Suche hat erfolgreiche Modelle gefunden, die der alte Bericht nicht formatgeprüft hat. Es sind aber **nicht** die Modelle, nach denen gefragt war (virtuelle KI-Influencer, KI-Avatare). Es sind vor allem **menschlich produzierte faceless Formate mit echten Produkten**, in der Spitze fast immer mit `isAd`-Flag. KI-generierte Bilder erscheinen im Spitzenbereich als kurzlebige Spitzenmonate (H, behauptet B), als reichweitenschwache Nebenclips oder in einem aktiven Account mit behauptetem fünfstelligem Monat (G). Obwohl das Briefing optimistische Funde begünstigte, ist kein KI-Fall über mehrere Monate verifiziert.

## 3. Kategorien A–H: Was ist tatsächlich beobachtet?

Die wichtigste Korrektur ist begrifflich. Der alte Bericht hat die Spitzenverdiener nicht formatgeprüft und pauschal als „menschlich" gezählt. Die Gegenbeweis-Suche zeigt: Ein Teil davon ist **faceless**, also Hände, Produkt und Voice-over. Das ist genau die Produktionsform, die KI am billigsten unterstützen kann. Ein faceless Video ist aber **kein KI-Video**. In keinem geprüften faceless Spitzenaccount ist KI nachgewiesen. Die Tabelle trennt deshalb zwischen „Format, das KI ersetzen könnte" und „Format, in dem KI nachweislich eingesetzt wird".

| Kat. | Beschreibung | Stärkste gefundene Beispiele (Evidenz) | Output | Konversion | Lebensdauer | Policy-Risiko | Skalierbarkeit | Befund |
|---|---|---|---|---|---|---|---|---|
| **A** | 100 % virtueller KI-Influencer (Persona) | Keines mit Shop-Umsatz. 0 von 24 formatgeprüften US-Top-Creators, 0 von 25 UK-Top-Creators. Clorox-Figuren: 8,4 Mio. Impressions, gut 300 Pine-Sol-Bestellungen gegenüber über 60.000 bei Creator-Kampagnen (Modern Retail, Claimed). @virtuosos2 (KI-Sketche ohne feste Persona): 1,2 Mio. Plays (Verified), „over $100k GMV" kumuliert (Claimed), laut Betreiber gesperrt. | hoch | nicht belegt | kurz | hoch | hoch in der Produktion, niedrig im Verkauf | keine glaubwürdige Evidenz für Shop-Umsatz |
| **B** | KI-Avatar/KI-Person + echtes Produkt | Affiliate-Center-Screenshot: 174.000 USD GMV in 30 Tagen für einen Account, den ein Tool-Verkäufer als KI bezeichnet (Handle nicht lesbar, KI-Status behauptet). UK-Creatorin nennt UK-Rang 2 und 3 im Januar 2026 KI-Funnel-Accounts (Claimed, ohne Handle). @healthiswealthfyp: „Granny"-Avatar, 287.100 Plays, bester Monat geschätzt 1.500–5.000 USD, danach tot. Coaching-Kunde: 8.000 USD „profit" mit Avatar-Videos (Claimed, mehrere Sperren). | hoch | im Screenshot 26,6 USD GMV je 1.000 Views | kurz, Sperren häufig | **sehr hoch**: Fake-Testimonial (FTC, UWG, DMCC), KI-VO Art. 50, AIGC-Label | mittel | sechsstellige GMV-Monate **behauptet**, nicht prüfbar |
| **C** | KI-Stimme + fremdes oder gerendertes Produktvideo | @healthysmartdeals: 3D-KI-Figur + TTS-Verdacht, 19 von 20 Videos `isAd`, Claimed 68.670 USD GMV in 30 Tagen, aktive Monate geschätzt 1.000–5.000 USD, heute inaktiv. @pinecommerce: TTS + Stock, seit Juni 2026 inaktiv, Median 38 Views. InVideo-Beispiel: ein 100 %-KI-Video mit rund 30.000 USD GMV in 7 Tagen (Claimed, Tool-Anbieter). | hoch | niedrig bis mittel | kurz | mittel–hoch (EU: TTS ohne kreativen Beitrag = minderwertig) | hoch | schwache Evidenz, kurzlebig |
| **D** | Echte Hände + echtes Produkt + KI-/TTS-Stimme | @cakedfinds: 8 Monate in Folge US-Top-10, identisches Skript-Template; ein Coach nennt eine KI-Stimme, ein Reddit-Nutzer fragt danach. **Unbestätigt**, die Audio-Ähnlichkeit zweier Videos ist nur ein Indiz. @beautypickshub: Template-Voice-over (TTS oder Mensch unbekannt), Spitze im Juli 2026, danach eingebrochen. | 10–20/Tag möglich | falls @cakedfinds: 0,57–0,68 Bestellungen je 1.000 Views | falls @cakedfinds: 8+ Monate | mittel (US: generisches TTS labelfrei; EU/UK: Offenlegung, „minderwertig"-Klausel) | hoch | **möglich, aber nicht belegt**: Das Format ist an der Spitze beobachtet, die KI-Stimme dort nicht |
| **E** | Echtes UGC, aber Skript/Stimme/Schnitt/Varianten mit KI | Von außen nicht messbar, weil KI-Skripte kein Label bekommen. Indizien: Skript-Templates bei @cakedfinds („not one, not two, but three…"), KI-artige Captions bei @sarahgibbons_ (25.000 Videos). | beliebig | wie menschliches UGC | wie menschliches UGC | niedrig | hoch | Format beobachtet, KI-Anteil nicht öffentlich verifizierbar |
| **F** | Faceless-Produktvideos mit menschlicher oder unbekannter Stimme | @hannahbentley: 9 von 10 Monaten US-Top-10, 0,99–2,37 Mio. USD GMV/Monat, Stimme laut Transkript vermutlich menschlich. @bennettfinds: 1,13 Mio. USD GMV im August 2026. @shop_shiesty: „870k in GMV in 30 Tagen" (Coach-Aussage). UK: @truehealthsource, @thedealshunter mit geschätzt 1.100–1.900 EUR Provision/Monat, über 30 Monate aktiv. **Aber in UK machen rein faceless Accounts nur 1,6 % des GMV der Top-25 aus, und alle 13 UK-Creators mit geschätzt ≥ 3.000 € zeigen ihr Gesicht.** Italien: Reddit-Nutzer mit ca. 3.000 EUR Provision/Monat seit 7 Monaten (Claimed). | 1–19/Tag | 0,36–0,57 Bestellungen je 1.000 Views (@hannahbentley) | Monate bis Jahre | niedrig (echtes Produkt, echte Demo) | mittel (Muster, Filmen) | **menschlich produziert beobachtet** bis sechsstellig (US); in UK/EU selten an der Spitze |
| **G** | KI-Szene/KI-B-Roll + echtes Produktbild | **@spongebobprodsz**: KI-Szenen (Küche, Garten, Weihnachten) um ein echtes Produktbild, Skript-Voice-over, 10–12 s. Verified am 25.09.2026: 28.800 Follower, 1.172 Videos, 10 von 10 neuesten Videos mit KI-Label und Produktlink, 5 von 10 `isAd`, Median ca. 390 Plays. Claimed (Kursverkäufer): rund 7 Monate Aktivität und eine Kalodata-Karte mit 302.090 USD GMV in 30 Tagen (Juli 2026) → geschätzt 12.000–54.000 USD Provision. Konto seit 2021, frühere Nutzung oder Kauf möglich. Gegenbeispiele: @kevin.finds/@airgeeksrc (KI-Clips mit 63–2.817 Views), @turnersells (inaktiv seit 16.08.2026), Coaching-Kunde mit ca. 1.050 Videos/Monat, „majority got banned". | sehr hoch | im Spitzenfall mittel bis hoch (behauptet), sonst niedrig | ein aktiver Fall, sonst kurz | mittel–hoch (KI-Rendering statt Produktdemo verboten, Label Pflicht) | hoch, über Masse | ein aktiver Account mit **behauptetem** fünfstelligem Monat; sonst schwache Evidenz |
| **H** | Hybrid, KI für Zuschauer nicht erkennbar | @mackfinds_: Foto-Slideshows mit wechselnden, vermutlich fremden oder KI-generierten Personenbildern + echtem Produktfoto. Dashboard-Screenshot in einem Tweet: **51.700 USD geschätzte Provision in 28 Tagen** (18.05.–14.06.2026, 30 % Satz, 11.700 Artikel), selbst angesehen. Account seit 09/2025, Beiträge heute bei 422–24.700 Plays. UK-Food-Nr.-1 @annsdailydeals: unmarkiertes KI-Bild-Karussell mit 194.600 Views (Verified), Rest des Accounts menschlich oder Hände. | hoch | im Spitzenmonat hoch | Spitze, dann Abfall | **hoch** (Vorher-nachher-Bilder bei Zahnpasta = erfundene Ergebnisse; fehlendes Label) | hoch | ein **belegter Spitzenmonat**, kein Dauerzustand |

### 3.1 Was die Tabelle bedeutet

- **Die Grenze verläuft nicht zwischen „KI" und „Mensch", sondern zwischen „echtes Produkt im Bild" und „KI-Person oder KI-Rendering des Produkts".** Die dauerhaften Spitzenaccounts zeigen echte Produkte in echten Händen. Accounts mit KI-Personen als Testimonial (A, B) und mit KI-Stimmen über fremdem oder gerendertem Material (C) sind nach Wochen bis Monaten eingebrochen oder gesperrt, soweit man sie verfolgen kann. @spongebobprodsz (G) zeigt ein echtes Produktbild, trägt konsequent das KI-Label und nutzt keine KI-Person. Er ist ein einzelner Fall, aus dem sich keine Regel ableiten lässt.
- **Die Stimme ist die offene Frage.** Wäre die Stimme bei @cakedfinds synthetisch, gäbe es einen Kategorie-D-Account mit fünf- bis sechsstelliger Monatsprovision über acht Monate. Das ist nicht bewiesen und auf öffentlichem Weg nicht beweisbar.
- **Kurzfristige fünfstellige Monate mit KI-Anteil existieren** (H: 51.700 USD Provision, gesichtet; G und B: behauptet). Alle liegen in Formaten mit hohem Regelrisiko oder hängen an einer einzigen Verkäufer-Quelle. Der alte Bericht hat diese Spitzen unterschätzt. Belege für Dauer fehlen weiterhin.
- **In UK, dem DE-nächsten Markt, spielt faceless an der Spitze kaum eine Rolle.** Das dämpft die Übertragbarkeit der US-Befunde auf DE und spricht dafür, im Test auch das eigene Gesicht (E) als Alternative zu prüfen.
- **Der alte Satz „virtuelle KI-Influencer funktionieren nicht" bleibt richtig.** Er war zu breit, wenn er als „KI-Content funktioniert nicht" gelesen wurde.

## 4. Video-Level-Modell mit Heavy-Tail und Monte-Carlo-Simulation

### 4.1 Warum das alte Einkommensmodell falsch gebaut war

Das Einkommensmodell des alten Berichts (Kapitel 5.4) rechnete mit **Mittelwerten**: 3.965 Views pro Video × 30,4 USD GMV je 1.000 Views × 15 % Provision × 0,9 (Retouren) × 0,92 (Kurs) = 14,97 EUR pro Video. Daraus folgten „150 Videos = 1.650 EUR" und „830 Videos = 10.000 EUR". Kapitel 10 des alten Berichts beschrieb die schiefe View-Verteilung zwar (Median 300–400, Top-5 % = 81 % der Views), das Einkommensmodell nutzte sie aber nicht. Bei einer Verteilung, in der wenige Videos fast den ganzen Umsatz machen, liegt der Mittelwert weit über dem, was ein typischer Betreiber erlebt. Das alte Modell hat deshalb zwei Fehler gleichzeitig gemacht: Es hat den **typischen** Monat überschätzt und die **Chance auf einen sehr guten Monat** nicht ausgewiesen.

### 4.2 Modellaufbau (Skripte in `quellen/redteam/mc/`)

Jedes Video wird einzeln simuliert:

1. **Views:** Log-Normal-Körper (Median m × Account-Qualität q, Streuung σ = 1,4–1,5) plus mit Wahrscheinlichkeit p_tail × √q ein Pareto-Ausreißer ab 10.000 Views (α ≈ 1, Obergrenze 20 Mio.).
2. **Konversion:** GMV pro 1.000 Views (GPM) log-normal um den Median g × Produkt-Fit f, Streuung je Video σ ≈ 1.
3. **Bestellungen:** Poisson(Views / 1.000 × GPM / Warenkorb).
4. **Provision:** Bestellungen × Warenkorb × Provisionssatz × (1 − 10 % Retouren) × 0,92 EUR/USD.
5. **Account-Risiko:** Sperre/Einschränkung mit 4–6 % pro Monat; der betroffene Monat verliert 30–100 %. Der Account stirbt im Modell nie (siehe 4.7).
6. **Mehrere Accounts derselben Person:** 60 % der Standardabweichung (36 % der Varianz) von Qualität und Produkt-Fit sind gemeinsamer Betreiber-Effekt. Ab mehr als 5 Videos pro Tag und Account sinkt die Reichweite je Video (Faktor (5/Videos pro Tag)^0,2). Publikumsüberlappung zwischen Accounts und Verbund-Sperren enthält erst das Portfolio-Modell in Kapitel 7.

Drei **Ergebnis-Archetypen**. Sie sind keine Skill-Stufen, sondern Klassen beobachtbarer Kennzahlen. Welcher Archetyp ein Betreiber ist, zeigt erst sein eigener Test.

| Archetyp | Median-Views je Video | Ausreißer-Parameter p_tail | Tatsächlicher Anteil Videos ≥ 10.000 Views | GPM-Median | Provision | Warenkorb |
|---|---|---|---|---|---|---|
| Einsteiger | 300 | 2 % | 3,3–3,6 % | 4 USD | 8–15 % | 28 USD |
| Kompetent | 600 | 4 % | 8,2–9,1 % | 9 USD | 10–20 % | 32 USD |
| Sehr gut | 1.000 | 6 % | 13,3–14,6 % | 18 USD | 15–25 % | 38 USD |

**Kalibrierung** (`calib.py`, Ausgabe `calib_out.txt`). Die Mischungsgewichte sind Annahmen, keine gemessenen Bevölkerungsanteile.

| Prüfgröße | Modell | Anker | Quelle / Tag |
|---|---|---|---|
| Verkaufende Videos < 100 USD / 100–10.000 / > 10.000 USD GMV (Mischung 70/25/5) | 72,2 % / 27,6 % / 0,22 % | 78 % / 22 % / 0,15 % | Biverse via Chosun Ilbo 07.09.2026, Claimed |
| Anteil Betreiber mit ≥ 11.000 USD Provision/Monat (Mischung 70/25/5) | 2,0 % | Top-down aus Biverse: ca. 0,03–1 % der KI-Betreiber | Estimated |
| Anteil Betreiber mit ≥ 1.100 USD Provision/Monat (Mischung 55/35/10) | 32 % | Zielband 20–35 %, Nenner unbekannt | abgeleitet aus TikTok: 16.000 Creator ≥ 100k USD GMV/Jahr, Estimated |
| Median-Views je Video (Einsteiger) | 308 | 350–490 | Socialinsider/Buffer, Verified als Studienwert |

Das Modell ist damit **im oberen Rand deutlich optimistisch**: Es erzeugt mehr Videos mit hohen Umsätzen als Biverse und etwa doppelt bis 60-mal so viele Betreiber über 11.000 USD wie die Top-down-Schätzung. Auch das Verhältnis Spitzenvideo zu Median-Video pro Account liegt mit rund 130–145× über den 64× aus der Literatur (Munger). Alle Ergebnisse unten sind daher eher Obergrenzen.

### 4.3 Ergebnis: Provision pro Monat im eingeschwungenen Zustand (ab Monat 3)

20.000 Simulationen je Zelle, bis 10 Videos pro Tag und Account. Ab 500 Videos laufen mehrere Accounts, hier **naiv**, also ohne Publikumsüberlappung und ohne Verbund-Sperren (dafür Kapitel 7). Beträge in EUR, **Provision vor Kosten**.

**Basisfall (Konversion unabhängig von Viralität):**

| Archetyp | Videos/Monat | Accounts | P10 | P25 | Median | P75 | P90 | Mittelwert | Videos ohne Verkauf | Anteil der Top-5-%-Videos an der Provision |
|---|---|---|---|---|---|---|---|---|---|---|
| Einsteiger | 100 | 1 | 14 | 33 | 74 | 164 | 335 | 171 | 85 % | 73 % |
| Einsteiger | 300 | 1 | 54 | 113 | 238 | 497 | 967 | 495 | 86 % | 79 % |
| Einsteiger | 500 | 2 | 148 | 262 | 487 | 897 | 1.585 | 846 | 86 % | 80 % |
| Einsteiger | 1.000 | 4 | 408 | 657 | 1.105 | 1.852 | 3.137 | 1.668 | 86 % | 81 % |
| Kompetent | 100 | 1 | 119 | 251 | 544 | 1.187 | 2.408 | 1.312 | 67 % | 64 % |
| Kompetent | 300 | 1 | 433 | 866 | 1.768 | 3.670 | 7.404 | 3.727 | 69 % | 72 % |
| Kompetent | 500 | 2 | 1.150 | 1.966 | 3.618 | 6.723 | 12.033 | 6.328 | 69 % | 74 % |
| Kompetent | 1.000 | 4 | 3.079 | 4.893 | 8.230 | 14.113 | 24.060 | 12.847 | 69 % | 76 % |
| Sehr gut | 100 | 1 | 558 | 1.120 | 2.393 | 5.101 | 10.301 | 5.452 | 51 % | 60 % |
| Sehr gut | 300 | 1 | 2.009 | 3.885 | 7.827 | 16.106 | 31.957 | 15.798 | 53 % | 68 % |
| Sehr gut | 500 | 2 | 5.091 | 8.696 | 15.754 | 28.986 | 53.417 | 27.306 | 53 % | 71 % |
| Sehr gut | 1.000 | 4 | 13.595 | 21.615 | 36.032 | 61.934 | 105.614 | 54.503 | 52 % | 74 % |

**Gleichwertiger Co-Basisfall: virale Videos konvertieren schlechter (ρ = −0,3).** Kapitel 5 zeigt über Produkte hinweg eine starke negative Rangkorrelation zwischen Viralität und Konversion. Dieser Fall ist daher mindestens so plausibel wie der Basisfall (`mc_revision.py`).

| Archetyp | Videos | P10 | P25 | Median | P75 | P90 | Mittelwert |
|---|---|---|---|---|---|---|---|
| Einsteiger | 100 / 300 / 500 / 1.000 | 10 / 39 / 99 / 265 | 23 / 76 / 169 / 409 | 50 / 151 / 299 / 663 | 101 / 296 / 526 / 1.085 | 193 / 548 / 889 / 1.695 | 96 / 272 / 458 / 917 |
| Kompetent | 100 / 300 / 500 / 1.000 | 87 / 297 / 753 / 1.949 | 175 / 557 / 1.240 / 2.988 | 355 / 1.098 / 2.150 / 4.782 | 712 / 2.135 / 3.766 / 7.853 | 1.345 / 3.988 / 6.414 / 12.341 | 705 / 2.000 / 3.349 / 6.717 |
| Sehr gut | 100 / 300 / 500 / 1.000 | 405 / 1.363 / 3.291 / 8.547 | 773 / 2.495 / 5.428 / 13.066 | 1.533 / 4.789 / 9.351 / 20.953 | 3.032 / 9.269 / 16.274 / 33.840 | 5.635 / 17.155 / 27.372 / 53.769 | 2.926 / 8.409 / 14.165 / 28.592 |

**Gewinn-Median** im Basisfall nach Produktionskosten je Creative (plus 100 EUR Fixkosten und 50 EUR je Account, **vor Arbeitszeit**):

| Archetyp | Videos | 2 € je Creative | 5 € | 10 € | 20 € |
|---|---|---|---|---|---|
| Einsteiger | 100 / 300 / 500 / 1.000 | −276 / −512 / −713 / −1.195 | −576 / −1.412 / −2.213 / −4.195 | −1.076 / −2.912 / −4.713 / −9.195 | −2.076 / −5.912 / −9.713 / −19.195 |
| Kompetent | 100 / 300 / 500 / 1.000 | 194 / 1.018 / 2.418 / 5.930 | −106 / 118 / 918 / 2.930 | −606 / −1.382 / −1.582 / −2.070 | −1.606 / −4.382 / −6.582 / −12.070 |
| Sehr gut | 100 / 300 / 500 / 1.000 | 2.043 / 7.077 / 14.554 / 33.732 | 1.743 / 6.177 / 13.054 / 30.732 | 1.243 / 4.677 / 10.554 / 25.732 | 243 / 1.677 / 5.554 / 15.732 |

### 4.4 Was das Modell über die alten Aussagen sagt

- **Der Archetyp wiegt mehr als die Videozahl.** Ein „sehr guter" Betreiber erreicht mit 300 Videos im Median fast so viel Provision wie ein „kompetenter" mit 1.000 Videos (7.827 gegenüber 8.230 EUR). Ein Einsteiger kommt mit bezahlten Creatives bei keiner Videozahl in die Gewinnzone. Für 10.000 EUR Provision im Median braucht „sehr gut" im Basisfall rund 400–500 Videos, im Co-Basisfall 500–1.000. „Kompetent" braucht im Basisfall über 1.000 Videos auf mehreren Accounts (naiv gerechnet), im Co-Basisfall erreicht er es mit 1.000 Videos nicht. Die alte Regel „10.000 EUR = 830 Videos" ist als allgemeine Regel wertlos. Für einen kompetenten Betreiber ist sie eher zu optimistisch.
- **C5 war der Mittelwert, nicht das typische Ergebnis.** Für den Archetyp „kompetent" mit 150 Videos und der alten Kostenannahme (589 EUR) liefert das Modell: Mittelwert 1.362 EUR Gewinn, **Median 284 EUR**, 36 % Verlustmonate, 20 % der Monate über 1.650 EUR. Für „sehr gut": Median 3.255 EUR. Mit 5 € je Creative plus Tools liegt der kompetente Median bei −29 EUR (Kapitel 7).
- **Die Verteilung ist extrem schief.** Bei „kompetent" haben rund 69 % der Videos keinen einzigen Verkauf. Die besten 5 % der Videos bringen rund drei Viertel der Provision. Die besten 10 Videos eines 300-Video-Monats liefern im Median 64 % (bei 150 Videos 73 %).
- **Der Median wächst schneller als der Mittelwert.** Mehr Videos erhöhen vor allem die Chance, überhaupt einen Ausreißer zu treffen. Deshalb steigt der Median überproportional (kompetent: ×15 von 100 auf 1.000 Videos, Mittelwert ×9,8). Das gilt nur, solange die Reichweite pro Video nicht sinkt. Publikumsüberlappung zwischen mehreren Accounts ist hier nicht enthalten (Kapitel 7).

### 4.5 Sensitivität

| Stellschraube | Kompetent, 300 Videos: Median / P90 |
|---|---|
| Basis (Konversion unabhängig von Viralität) | 1.768 / 7.404 |
| Virale Videos konvertieren schlechter (ρ = −0,3), Co-Basisfall | 1.098 / 3.988 |
| Virale Videos konvertieren besser (ρ = +0,3) | 3.043 / 14.654 |
| Monat 1 (Hochlauf, 40 % Reichweite) | 636 / 2.784 |
| Monat 2 (70 %) | 1.192 / 5.103 |

Die Richtung der Korrelation zwischen Viralität und Konversion verschiebt das Ergebnis um den Faktor 2–3.

### 4.6 Zusatzszenario: bezahlte Verstärkung durch Seller (GMV Max / Shop Ads)

Seller können gut konvertierende Affiliate-Videos in Anzeigen nutzen. Der Affiliate bekommt Provision auf das werbefinanzierte GMV, zu einem Satz, den der Seller separat festlegen kann (TikTok Ads Help, Stand März 2026, Verified). 70–100 % der neuesten Videos der Top-Accounts tragen `isAd = true`. Das Flag steht aber auch auf Videos mit wenigen Hundert Views, beweist also keine bezahlte Reichweite. Das Szenario ist **nicht kalibriert**. Es zeigt nur, wie stark dieser Hebel wäre, wenn er greift.

Annahmen: Ein Video mit mindestens 3 organischen Bestellungen wird mit Wahrscheinlichkeit p verstärkt. Bezahlte Views = organische Views × Log-Normal (Median 30). Konversion der bezahlten Views = 70 % der organischen. Provision auf Ads-GMV = 50–100 % des Standardsatzes.

| Archetyp | Videos | p = 0 (Basis): Median / P90 | p = 10 %: Median / P90 | p = 30 %: Median / P90 | Anteil Monate ≥ 10.000 € Gewinn bei p = 0 / 10 % / 30 % |
|---|---|---|---|---|---|
| Kompetent | 150 | 875 / 3.837 | 1.707 / 11.075 | 4.299 / 25.901 | 2 % / 10 % / 26 % |
| Kompetent | 300 | 1.935 / 7.944 | 4.172 / 22.702 | 10.393 / 51.651 | 5 % / 22 % / 47 % |
| Sehr gut | 150 | 3.849 / 16.659 | 8.679 / 48.234 | 22.245 / 108.319 | 18 % / 43 % / 70 % |
| Sehr gut | 300 | 8.508 / 34.496 | 20.603 / 94.322 | 50.256 / 216.019 | 38 % / 68 % / 87 % |

Provision in EUR pro Monat (eigener Simulationslauf ohne Betreiber-Effekt, deshalb leicht abweichende Basiswerte). Gewinn nach 5 € je Creative und 160 € Tools.

**Lesart:** Seller-Verstärkung ist ein **plausibler** Hebel, der die Spitzenaccounts erklären könnte. Schon wenn jedes zehnte verkaufende Video verstärkt wird, verdoppelt sich im Modell der Median. Das passt zu den 50.000–500.000 Views pro Video, die Spitzenaccounts im Mittel haben. Die entscheidende Größe p ist **öffentlich nicht messbar**: Wie oft wählt ein Seller gerade meine Videos für seine Anzeigen, und zu welchem Satz? Das hängt an Konversion, Produktwahl und Seller-Beziehungen, nicht an KI.

### 4.7 Zusatzrisiko für KI-visuelle Formate: Account-Tod

Das Modell kennt nur zeitweise Einbußen, keinen endgültigen Verlust eines Accounts. Beobachtet sind für KI-visuelle Formate (A, B, C) 6 von 9 toten oder inaktiven Accounts nach 5 Tagen bis 6 Monaten. Das entspricht grob 15–20 % Ausfallrisiko pro Monat. Bei 15–20 % bleibt ein Account im Erwartungswert rund 4,7–5,7 von 12 Monaten aktiv. Bei den geprüften faceless Accounts mit echtem Produkt, die teils über 30 Monate laufen, liegt das Risiko eher bei wenigen Prozent (etwa 10 von 12 Monaten). **Für KI-visuelle Formate ist der Jahreswert daher grob zu halbieren.** Das gilt auch für die Werte in Kapitel 9, 10 und 13.

### 4.8 Grenzen

- Die Archetyp-Parameter sind **nicht direkt beobachtet**. Sie sind so gewählt, dass die Mischung die wenigen öffentlichen Verteilungsdaten trifft. Sie überzeichnen den oberen Rand (4.2).
- Kein Lernen über die Zeit, keine Saisonalität (Q4 bringt laut Branchendaten deutlich mehr GMV), kein Produkt-Lebenszyklus.
- GPM und Provisionen sind US-Niveau. Für DE/EU liegen die Werte näher am Einsteiger-Archetyp (Provision 5–15 %, niedrige Warenkörbe).
- Alle Wahrscheinlichkeiten in diesem Kapitel sind **modellbedingt**. Sie sagen: „Wenn die Kennzahlen eines Betreibers so aussehen, streut der Monat so." Sie sind keine empirischen Erfolgsquoten und gelten nicht für einen konkreten Betreiber, dessen Archetyp unbekannt ist.

## 5. Die Ausreißer-Hypothese: Ein Video mit 2 Mio. Views = 8.400 EUR?

### 5.1 Die Kette und was sie implizit annimmt

200 Videos → 1 Video mit 2 Mio. Views → 40.000 Klicks (2 %) → 1.200 Käufe (3 %) → 35 € Warenkorb → 42.000 € GMV → 20 % → 8.400 € Provision.

Implizit sind das **0,6 Bestellungen je 1.000 Views**, **21 € GMV je 1.000 Views** und **7 € Provision je Verkauf**. Die Frequenz „1 von 200" ist die eigentliche Annahme.

### 5.2 Echte Gewinner-Videos

28 dokumentierte Gewinner-Videos wurden gefunden, 15 davon mit Plattformdaten (FastMoss, EchoTik, Kalodata). Views, Bestellungen und GMV sind **Claimed**: Drittanbieter-Schätzungen, bei den zwei mit „Beispiel eines YouTubers" markierten Zeilen Selbstauskünfte. Die Raten sind **Estimated**.

| Video (Produkt) | Format | Views | Bestellungen | GMV (USD) | Bestellungen je 1.000 Views | GMV je 1.000 Views |
|---|---|---|---|---|---|---|
| @quinclips3 (DR.DENT, Zahnaufhellung) | Mensch, Vorher-nachher | 81,5 Mio. | 27.300 | 430.000 | 0,33 | 5,3 |
| @quinclips3 (DR.DENT, 2. Video) | Mensch | 28,8 Mio. | 10.700 | 170.100 | 0,37 | 5,9 |
| @simplysammyk (Fußmassagegerät) | Mensch | 14,5 Mio. | 6.000 | ca. 496.800 | 0,41 | 34,3 |
| Kfz-Ladegerät (Beispiel eines YouTubers) | F | 9,0 Mio. | – | 245.000 | – | 27,2 |
| Luftreiniger (dito) | F | 8,5 Mio. | – | 317.000 | – | 37,4 |
| @grantsdealz (Fanttik Powerstation) | F | 3,7 Mio. | 411 | 62.000 | 0,11 | 16,8 |
| Built Bar (@demi_does.it) | Mensch | 3,0 Mio. | 745 | 19.900 | 0,25 | 6,6 |
| MREGB Steckdosen-Ventilator (von Kalodata als KI markiert) | vermutlich G/B | 1,92 Mio. | 883 | 22.950 | 0,46 | 12,0 |
| MREGB (KI + Anzeige markiert) | vermutlich G/B | 0,74 Mio. | 3.160 | 82.130 | 4,27 | 111,0 |
| Built Bar (@lorienwright) | unbekannt | 0,60 Mio. | 549 | ca. 15.300 | 0,92 | 25,6 |
| Hundesitzbezug | unbekannt | 0,83 Mio. | 734 | 96.770 | 0,89 | 116,9 |

Ergebnisse über alle dokumentierten Fälle:

- **Videos mit 1 Mio.+ Views:** Median 14,5 USD GMV und 0,37 Bestellungen je 1.000 Views. Videos unter 1 Mio.: Median 81 USD und 1,02 Bestellungen.
- **Konversion fällt mit Viralität** über Produkte und Creators hinweg (Rangkorrelation −0,82). Innerhalb eines Creatives bleibt sie konstant: @quinclips3 lag bei 14,6 Mio. wie bei 81,5 Mio. Views bei 0,33–0,38. Die Top-Listen sind nach GMV selektiert, ein Teil des Zusammenhangs ist also mechanisch.
- **1.000+ Bestellungen bei 1 Mio.+ Views** kamen in 5 von 14 dokumentierten Fällen vor. Das passiert pro Top-Produkt und Monat nur eine Handvoll Mal, oft durch denselben Creator.
- **Alle plattformbelegten Gewinner mit 5.000+ Bestellungen zeigen echte Menschen.** KI-markierte Gewinner existieren (MREGB), sind kleiner, nicht zuordenbar und von Anzeigen gestützt.
- **Bezahlte Verstärkung:** Viele große Gewinner laufen zu einem großen Teil als Anzeige. Beim Hundesitzbezug kamen 57 % der Views und 80 % des Umsatzes aus Anzeigen (Kalodata). Beim Built-Bar-Hauptprodukt waren es 50,5 %.

### 5.3 Was ein 2-Mio.-Video wirklich bringt

| Annahme | Bestellungen je 1.000 Views | GMV je 1.000 Views | Provision aus 2 Mio. Views |
|---|---|---|---|
| Median der 1-Mio.+-Videos, 15 % Satz | 0,37 | 14,5 USD | ca. 4.000 EUR vor Retouren, ca. 3.600 EUR danach |
| Spanne der dokumentierten Median-Raten | – | – | 1.450–5.100 EUR |
| Nutzer-Kette | 0,6 | 21 EUR | 8.400 EUR |
| Bestfall (1,11 Bestellungen, 25 % Supplement-Satz) | 1,11 | – | ca. 15.300 EUR |
| Monte Carlo, Median aller Videos mit 2 Mio.+ Views | – | – | Einsteiger 1.754 / kompetent 4.694 / sehr gut 13.670 EUR |

**Die Kette ist pro Gewinner optimistisch, aber möglich.** Sie liegt beim 1,6- bis 5,8-fachen der dokumentierten Median-Erträge und unter dem Bestfall.

### 5.4 Die eigentliche Frage: Wie oft passiert es?

| Quelle | Wahrscheinlichkeit, dass ein Video 2 Mio.+ Views erreicht | Umgerechnet auf 200 Videos |
|---|---|---|
| Monte Carlo Einsteiger | 1 zu 16.500 | 1,2 % |
| Monte Carlo kompetent | 1 zu 4.750 | 4,1 % |
| Monte Carlo sehr gut | 1 zu 2.320 | 8,3 % |
| @quinclips3 (Top-Mensch-Creator) | ca. 1 zu 160 | ca. 70 % |
| @mackfinds_ (Spitzenmonat, 191 Beiträge gesamt) | mindestens 3 von 191 über 3 Mio. | – |

„1 von 200" ist für Spitzenaccounts beobachtet, deren Videos von Sellern verstärkt werden. Für neue oder KI-Accounts ist das nirgends belegt. Im Modell liegt es 12- bis 80-mal über der Rate normaler Archetypen.

### 5.5 Wirkung auf die Schwellen 3k / 5k / 10k / 20k

- Wahrscheinlichkeit, dass ein Monat mit 300 Videos **mindestens ein Video mit ≥ 8.400 EUR Provision** enthält (Monte Carlo): Einsteiger 0,4 %, kompetent 2,9 %, sehr gut 14,1 %.
- Über 12 Monate ergäbe das im Modell für den Archetyp „kompetent" etwa 30 %, für „sehr gut" etwa 84 % Chance auf mindestens einen solchen Monat. Beides ist modellbedingt, gilt im optimistischeren Basisfall und nicht für einen Betreiber, dessen Archetyp unbekannt ist. Im Co-Basisfall (virale Videos konvertieren schlechter) sind solche Monate deutlich seltener.
- Ein einzelner 8.400-EUR-Ausreißer hebt **einen Monat** über 5.000 EUR. Er macht aus keinem Account ein 5.000-EUR-Geschäft. Die Spitzenmonate der gefundenen Accounts (@mackfinds_: 51.700 USD, danach Absturz; KI-Coaching-Kunden: ein Monat, dann Sperren) zeigen genau dieses Muster.
- **Die Hypothese verschiebt die 3k/5k-Schwellen in einzelnen Monaten, nicht im Durchschnitt.** Für 10k/20k im Durchschnitt braucht es wiederkehrende Ausreißer. Die gibt es in den Daten nur bei Accounts mit bezahlter Seller-Verstärkung.

## 6. Produkt-Ökonomie: Gibt es die Produkte, die 10.000 EUR tragen?

### 6.1 Die drei Rechenbeispiele gegen echte Produkte (US, Kalodata/FastMoss, Claimed)

| Beispiel | Rechnung | Nötige Verkäufe für 10.000 EUR | Realer Gegenpart | Provision je Verkauf | Volumen des Produkts | Konkurrenz | Nötiger Anteil am Produktvolumen |
|---|---|---|---|---|---|---|---|
| A | 39 € × 20 % = 7,80 € | 1.282/Monat = 43/Tag | Goli Zero Sugar Trio: 25,17 USD × 34 % | 7,87 € | 75.240 Einheiten (Mai 2026) | 3.380 Creators | 1,7 % |
| A | | | Dr.Melaxin-Set | 8,17 € | 44.630 Einheiten | 2.010 Creators | ca. 2,7 % |
| A | | | NeoCell Collagen | 6,61 € | ca. 88.600 Bestellungen/Monat (Q1 2026) | – | ca. 1,7 % |
| B | 69 € × 25 % = 17,25 € | 580/Monat = 19/Tag | **Nicht gefunden** mit sichtbarem Volumen. Nächste: medicube Gatekeeping 72,38 USD × 18 %; Glass Glow 89,11 USD × 15 %; Mellow Bettdecke 83,63 USD × 15 % | 11,5–12,3 € | 18.840–27.400 Einheiten | 3.380–4.550 Creators | 3–4,3 % |
| C | 99 € × 30 % = 29,70 € | 337/Monat = 11/Tag | **Nicht gefunden.** Nächste: Nex Playground ca. 250 USD × 20 % | ca. 46 € | 27.384 Einheiten (Nov 2025, nur Q4) | 5.875 Creators | 0,8 % |

### 6.2 Was daraus folgt

- **Die Nachfrage ist nicht der Engpass, der Anteil ist es.** Für 10.000 EUR mit Beispiel A braucht ein Affiliate 1,7 % des gesamten Produktvolumens. Bei 3.380 Creators auf dem Produkt ist das das 55- bis 72-fache des durchschnittlichen Creator-Anteils. Das schaffen nur die obersten 0,5–2 % der Creators eines Produkts.
- **Die Verteilung auf Produkten ist extrem.** Bei einer Marke machten 38 von 21.365 Affiliates 80 % des Affiliate-GMV, ein einzelner Creator rund 30 %. Bei Built Bar verdienten 18.800 Affiliates in 28 Tagen im Schnitt rund 7 USD Provision. Die drei besten Nicht-Marken-Affiliates erzielten je 5.000–10.400 USD. Über 298 Produkte hinweg lag der Median bei rund 350 Bestellungen, egal ob mit 10 % oder 20 % Provision.
- **Wer auf den Beispiel-A-Produkten gewinnt, ist in den geprüften Fällen menschlich.** Die Top-Affiliates von NeoCell (bis 941.600 USD GMV kumuliert) und DR.DENT (685.000 USD GMV aus 3 Videos in 28 Tagen) zeigen, soweit prüfbar, echte Menschen: Testimonial, Make-up auf echter Haut, Sketch. Das Profil des größten NeoCell-Affiliates war nicht abrufbar, sein Format ist unbekannt. Diese Formate sind mit KI nicht regelkonform nachbaubar, denn die AIGC-Policy verbietet erfundene Ergebnisse, Vorher-nachher und KI-„Ärzte". Ein Top-Affiliate war nach rund 4 Monaten wieder weg.
- **Die Hochprovisions-Produkte sind genau die, bei denen KI-Content am stärksten reguliert ist.** Supplements zahlen bis 34 %, Hautpflege-Sets 15–18 %. Technik, Heim und Saisonware sind KI-tauglicher, zahlen aber meist 5–20 %.
- **Provision pro 1.000 Views hängt am Produkt:** Bei gleicher Konversion liegt sie zwischen dem 0,4- und 3,3-fachen der 4,10 USD des alten Modells. Teure Produkte mit 18–20 % Provision liegen beim 2,3- bis 3,3-fachen, die meistverkauften billigen Produkte beim 0,4- bis 0,8-fachen. Umgerechnet in Videozahlen würde das die mittelwertbasierte Logik wiederholen, die Kapitel 4 verwirft. Der Faktor zeigt nur: **Produktwahl verschiebt den Ertrag je View um bis zu eine Größenordnung.**

### 6.3 Deutschland und UK

Unter den volumenstärksten Produkten in DE und UK findet sich keines der drei Beispiele. Die fünf DE-Top-Produkte im April 2026 hatten zusammen 60.794 Bestellungen und 764.819 USD GMV bei 5–15 % Provision und 13,83 EUR Durchschnittspreis. Das DE-Top-Produkt zahlt rund 1,40 EUR je Verkauf. 10.000 EUR Provision wären **31 % des gesamten Produktvolumens**. UK-Dauerbrenner zahlen 0,37–3,07 GBP je Verkauf. Produkte im mittleren Preissegment wurden für DE nicht systematisch geprüft. Das ist eine Lücke dieses Audits und wird in Kapitel 15 zur Vorab-Prüfung.

Gleichzeitig ist der DE-Markt größer, als der alte Bericht unterstellt hat: rund 43 Mio. EUR Affiliate-GMV pro Monat (Kalodata via Lengow, Q2 2026, Claimed). Das Problem in DE sind nicht fehlende Umsätze, sondern **niedrige Warenkörbe und niedrige Sätze**.

**Urteil:** Beispiel A ist real und in den USA mit ausreichend Nachfrage vorhanden. B ist nur mit etwa zwei Dritteln der angenommenen Provision real. C existiert nur als Hochpreis- oder Saisonprodukt. Unter den DE-Top-5 funktioniert keines der drei. Ob es in DE Mittelpreis-Produkte mit ausreichender Provision und Nachfrage gibt, ist offen.

## 7. Portfolio-Modell: 1, 3, 5 oder 10 Accounts

### 7.1 Was die Regeln erlauben (Stand 25.09.2026, TikTok-Primärquellen)

| Regel | USA | DE/EU |
|---|---|---|
| Accounts pro Person | 1 Ausweis kann bis zu **5 Creator-Accounts** verifizieren | keine veröffentlichte Obergrenze pro Person |
| Einstieg | 1.000 Follower (Affiliate), US-Wohnsitz, US-Ausweis, SSN | 500 Follower **im jeweiligen Mitgliedstaat**, Zugriff aus dem Registrierungsland |
| Pilotphase | unter 5.000 Follower: mind. 30 Tage, max. 3 Shopping-Videos/Tag, nur Produkte mit Shop-Score ≥ 95 %; „Extended Pilot" 3/Woche | 30 Tage, max. 21 Shopping-Videos/Woche, verlängerbar; Abschluss über eine Aufgabe + Account-Health > 176 |
| Nach dem Pilot | 30 Shopping-Videos + 60 Foto-Posts pro Tag und Account | 25 Shopping-Videos + 50 Foto-Posts pro Tag und Account |
| Gleiche Inhalte auf mehreren Accounts | „Do not repost your own content … Whether you manage one account or many, each post should offer something new" | Spam: „Mehrere Konten zu erstellen, um denselben E-Commerce-Inhalt zu verbreiten"; minderwertig: „Koordinierte Massenveröffentlichungen über mehrere Konten hinweg" |
| Verknüpfte Accounts | „we may ban all of their accounts, including associated accounts"; „Must not be associated with accounts that have had e-commerce permissions revoked" | frühere Entzüge zählen für „previous accounts of the Creator"; UK: häufige Logins mehrerer Accounts vom selben Gerät = Indiz für koordinierte Steuerung. Getrennte Geräte oder Netzwerke ändern an der Zuordnung nichts; entscheidend ist echtes getrenntes Eigentum. Dieses Audit empfiehlt keine technischen Trennmaßnahmen |
| Team/Agentur | Creator Agency Partners dürfen verwalten und Provision abrechnen; Passwort-Weitergabe ohne Erlaubnis verboten | Agenturen ausdrücklich vorgesehen; Owner-Zugangsdaten nie teilen |
| Automatisches Posten | Content Posting API hat **keinen Produktlink-Parameter**, ca. 15 Posts/Tag, interne Multi-Account-Uploader nicht zulässig | wie USA |

Neu gegenüber dem alten Bericht: Seller-gebundene **Marketing-Accounts** (1 Official + 4 Marketing je Shop, ohne Follower-Minimum) sind ein legitimer Multi-Account-Weg, aber nur für Seller oder als vertraglich vereinbarter Content-Arm eines Sellers. Sie sind kein Weg, Follower-Schwellen für eigene Affiliate-Accounts zu umgehen. Das Content Authorization Tool erlaubt Reposts **zwischen verschiedenen Creators** mit Zustimmung, nicht die Verteilung eigener Inhalte über eigene Accounts.

### 7.2 Portfolio-Simulation

Annahmen: 5 Videos pro Tag und Account (150/Monat), 5 € je Creative, Tools 100 € + 60 € je Account, VA/Schnitt 0 / 600 / 1.500 / 3.500 €. „Naiv" = Accounts unabhängig. „Realistisch" = gleiche Nische teilt Publikum (Reichweite je Account × Accounts^−0,15) und korreliertes Verbund-Risiko (3 % pro zusätzlichem Account und Monat, trifft alle Accounts mit 50–100 % Verlust). Gewinn in EUR pro Monat im eingeschwungenen Zustand.

| Archetyp | Accounts | Videos | Variante | Gewinn P10 | Median | P90 | Verlustmonate | Std./Woche | Innerhalb der Regeln? |
|---|---|---|---|---|---|---|---|---|---|
| Kompetent | 1 | 150 | – | −711 | −29 | 2.954 | 51 % | 20 | ja |
| Kompetent | 3 | 450 | naiv / realistisch | −1.919 / −2.255 | 394 / −217 | 8.275 / 6.574 | 45 % / 53 % | 40 | ja, bei eigenständigen Inhalten |
| Kompetent | 5 | 750 | naiv / realistisch | −3.219 / −4.311 | 744 / −933 | 12.837 / 8.752 | 44 % / 58 % | 55 | US: an der Obergrenze; EU: Risiko „koordinierte Massenveröffentlichung" |
| Kompetent | 10 | 1.500 | naiv / realistisch | −5.843 / −10.031 | 2.268 / −3.423 | 24.999 / 13.392 | 40 % / 65 % | 80 | **Nein** für eine Person in den USA; nur als Agentur mehrerer echter Creators |
| Sehr gut | 1 | 150 | – | 32 | 2.922 | 15.969 | 10 % | 20 | ja |
| Sehr gut | 3 | 450 | naiv / realistisch | 2.192 / 767 | 12.149 / 9.549 | 46.112 / 39.078 | 2 % / 7 % | 40 | ja |
| Sehr gut | 5 | 750 | naiv / realistisch | 4.979 / 240 | 22.296 / 14.878 | 73.413 / 57.343 | 2 % / 10 % | 55 | US: an der Obergrenze |
| Sehr gut | 10 | 1.500 | naiv / realistisch | 13.959 / −4.517 | 49.548 / 24.802 | 143.745 / 95.923 | 1 % / 16 % | 80 | **Nein** für eine Person in den USA |

Einsteiger verlieren in jeder Portfolio-Größe Geld (Median −790 bis −10.599 EUR). Alle Gewinne sind **vor Arbeitszeit**. Bei 15 €/Stunde kosten 20 / 40 / 55 / 80 Stunden pro Woche rund 1.300 / 2.600 / 3.600 / 5.200 € pro Monat. Nach Arbeitszeit bleibt beim kompetenten Betreiber im Median in keiner Portfolio-Größe etwas übrig. Der sehr gute Betreiber bleibt deutlich positiv (1 Account: rund 1.600 €, 3 Accounts: rund 6.900 € im realistischen Szenario).

### 7.3 Was daraus folgt

- **Mehr Accounts multiplizieren den Archetyp, nicht die Qualität.** Ein kompetenter Betreiber verliert mit 5 oder 10 Accounts im realistischen Szenario im Median Geld, weil Kosten linear wachsen, Reichweite sich aber teilt und ein Verbund-Ereignis alle Accounts trifft. Ein sehr guter Betreiber gewinnt mit 3 Accounts deutlich. Ab 5 Accounts frisst das Verbund-Risiko einen großen Teil des Zuwachses.
- **Die sinnvolle Portfolio-Größe ist 1–3 Accounts** mit klar getrennten Nischen und eigenständigen Inhalten. Das ist regelkonform, von einer Person mit 20–40 Stunden pro Woche machbar und begrenzt das Verbund-Risiko.
- **10 Accounts sind kein Solo-Modell.** In den USA verbietet es die Obergrenze. In der EU macht es die Spam-Klausel zu koordinierter Massenveröffentlichung riskant. Regelkonform geht das nur als Agentur, in der jeder Account einem echten, selbst verifizierten Creator gehört.
- **Automatisierung ist enger als im alten Bericht beschrieben.** Shopping-Videos lassen sich über die öffentliche API nicht mit Produktlink posten. Posten bleibt Handarbeit in App oder TikTok Studio. Ein VA mit Passwort eines persönlichen Accounts verstößt gegen die US-Nutzungsbedingungen, sofern TikTok es nicht erlaubt.
- Keine der hier genannten Strukturen dient dazu, Sperren zu umgehen. Wer nach einer Sperre neue Accounts eröffnet, verstößt ausdrücklich gegen die Regeln („Using multiple accounts to avoid enforcement").

## 8. Sales-Engine der fünf wirtschaftlich stärksten gefundenen Accounts

### 8.1 Auswahl und Datenlage

Der alte Bericht hat neun KI- oder Faceless-Accounts und einen menschlichen Benchmark rekonstruiert. Keiner davon hat einen belegbaren fünfstelligen Monatsumsatz. Für dieses Kapitel wurden die fünf wirtschaftlich stärksten Accounts der Gegenbeweis-Suche genommen, die **faceless Anteile** haben. Zwei davon sind überwiegend faceless (@hannahbentley, @cakedfinds). Drei zeigen überwiegend Menschen vor der Kamera und nutzen faceless Videos nur als Baustein (@trending_ttok, @be.lush, @myfamilypov). Zum Vergleich stehen die zwei stärksten KI-Accounts daneben.

Datenquelle für Umsatz, Artikel, Views und Follower sind die monatlichen „Top 10 independent creators"-Listen von Net Influencer mit Kalodata-Daten (November 2025 bis August 2026, **Claimed**, Drittanbieter-Schätzung, GMV vor Retouren, eventuell inklusive LIVE). Format, `isAd`-Anteil und Posting-Frequenz wurden am 24./25.09.2026 direkt auf TikTok geprüft (**Verified**). Provisionen sind **Estimated**: durchschnittliches Monats-GMV × 5–15 % × 0,9 (weil ein Teil über Anzeigen mit möglicherweise niedrigerem Satz laufen kann) und zum Vergleich × 10–20 % × 0,9.

### 8.2 Die Kennzahlen der Engine

| Account | Format (geprüft) | Monate in US-Top-10 | GMV/Monat (Ø) | Content-Views/Monat | Bestellungen je 1.000 Views | Warenkorb (AUP) | GMV je 1.000 Views | `isAd` bei neuesten Videos | Videos/Monat (Est.) | Provision/Monat (Est.) bei 5–15 % / 10–20 % |
|---|---|---|---|---|---|---|---|---|---|---|
| @hannahbentley | überwiegend F: Hände + Produkt, Voice-over, Stimme laut Transkript vermutlich menschlich | 9 von 10 | 0,99–2,37 Mio. USD (Ø 1,49 Mio.) | 42–98 Mio. | 0,36–0,57 | 49–72 USD | 19–31 USD | 8 von 10 | ca. 60–90 | 67.000–201.000 / 134.000–268.000 USD |
| @cakedfinds | überwiegend F, unbestätigter Verdacht auf TTS-Stimme; identische Caption, Skript-Template | 8 in Folge | 0,96–1,59 Mio. USD (Ø 1,16 Mio.) | 29–55 Mio. | 0,57–0,68 | 46–56 USD | 26–35 USD | 10 von 10 | ca. 270–570 | 52.000–157.000 / 104.000–209.000 USD |
| @trending_ttok | überwiegend Mensch vor der Kamera, einzelne Videos nur Hände/Beine + Produkt | 10 von 10 | 1,00–3,37 Mio. USD (Ø 1,80 Mio.) | 52–120 Mio. | 0,32–0,43 | 40–116 USD | 13–37 USD | 7 von 10 | ca. 150+ | 81.000–243.000 / 162.000–324.000 USD |
| @be.lush | heute Mensch vor der Kamera; bester Einzelhit laut Interview faceless Voice-over | 6 von 10 | 1,15–3,97 Mio. USD (Ø 1,96 Mio.) | 29–45 Mio. | 0,29–0,38 | 100–213 USD | 38–59 USD | 9 von 10 | – | 88.000–265.000 / 176.000–353.000 USD; selbst genannt: „$100,000 per month in commission" |
| @myfamilypov | überwiegend Mensch (Familien-Sketch), dazu Hände/Voice-over; verkauft Kurs („Learn the system") | 7 von 10 | 0,92–2,56 Mio. USD (Ø 1,70 Mio.) | 94–196 Mio. | 0,42–0,48 | 24–37 USD | 10–18 USD | 8 von 10 | ca. 80–600 | 77.000–230.000 / 153.000–306.000 USD |
| *KI-Vergleich:* @spongebobprodsz | G: KI-Szenen um echtes Produktbild, KI-Label | – | Claimed 302.090 USD in einem Monat (Kalodata-Karte eines Kursverkäufers) | nicht öffentlich | nicht öffentlich | nicht öffentlich | nicht öffentlich | 5 von 10 | ca. 180–300 | 12.000–54.000 USD (aus der Claimed-Karte) |
| *KI-Vergleich:* @healthysmartdeals | C: 3D-KI-Figur, TTS-Verdacht, Supplements | – | Claimed 68.670 USD in 30 Tagen | Stichprobe 20 Videos: 258.664 Views | nicht öffentlich | ca. 30 USD | nicht öffentlich | 19 von 20 | ca. 7 | 1.000–5.000 USD in aktiven Monaten, heute inaktiv |

### 8.3 Die Engine in fünf Schritten

1. **Traffic.** Die Spitzenaccounts erreichen 29–196 Mio. Content-Views pro Monat. Das sind bei 60–600 Videos im Schnitt 50.000–500.000 Views pro Video. Die neuesten Videos derselben Accounts zeigen meist nur 1.000–25.000 Views wenige Tage nach Upload. Der Monatswert entsteht also aus wenigen Videos, die sehr groß werden. 70–100 % der neuesten Videos tragen das Flag `isAd = true`. **Hypothese:** Seller spielen diese Videos in bezahlten Anzeigen aus (GMV Max, Spark Ads). TikTok dokumentiert eine Provision auf Anzeigen-GMV von Affiliate-Videos, deren Satz der Seller wählt. **Gegen eine einfache Deutung spricht**, dass das Flag auch auf Videos mit wenigen Hundert Views steht (alter Bericht: 61–534 Views; @spongebobprodsz: Median ca. 390; @mackfinds_: 422–24.700). Es kann auch nur eine Anzeigen-Freigabe bedeuten. Wie groß der bezahlte Anteil an der Reichweite ist, ist öffentlich nicht messbar.
2. **Klick.** Produktklicks sind öffentlich nicht verfügbar. Nicht öffentlich verifizierbar.
3. **Konversion.** 0,29–0,68 Bestellungen je 1.000 Views. Das ist **niedriger** als die 0,8 im „realistischen" Szenario des alten Berichts. Die Spitzenaccounts konvertieren also nicht besser. Sie haben mehr Reichweite.
4. **Warenkorb.** 24–213 USD. Unter den fünf hat @be.lush mit teuren Produkten (Staubsauger, bis 213 USD Warenkorb) den höchsten GMV je View. @myfamilypov verkauft die billigsten Produkte und hat den niedrigsten GMV je View. In der gesamten Top-10 liegen Apple-Refurb- und E-Bike-Accounts mit 135–170 USD GMV je 1.000 Views am höchsten.
5. **Provision.** Bei 5–20 % und 10 % Retouren ergeben sich geschätzt fünf- bis sechsstellige USD-Beträge pro Monat. @be.lush bestätigt die Größenordnung selbst: „$100,000 per month in commission … for almost two years" (Interview, Claimed).

### 8.4 Welcher Anteil kommt aus den Top-10-Videos?

Für diese Accounts **nicht öffentlich verifizierbar**. Umsätze pro Video veröffentlicht Kalodata nicht frei, und öffentlich abrufbar sind nur die neuesten Videos. Drei Indizien:

- @hannahbentley postet rund 3 Videos pro Tag. Die neuesten erreichen 741–23.000 Views, der Monat hat aber 42–98 Mio. Views. Selbst wenn jedes Video 25.000 Views hätte, wären das bei 90 Videos nur 2,3 Mio. Views. Mindestens rund 95 % der Monatsreichweite müssen also aus wenigen Videos kommen.
- Im Interview führt @be.lush das umsatzstärkste Video („over a million dollars in sales") auf ein einzelnes faceless Voice-over-Video zurück.
- Das Monte-Carlo-Modell ohne Seller-Verstärkung ergibt: Die besten 10 von 150 Videos liefern 69–82 %, die besten 3 von 300 Videos rund 40 %.

Die Antwort auf „20 Videos bringen 80 % oder 5 Videos bringen 90 %?" lautet daher: **Bei organischen Accounts eher 10 → 65–80 %. Bei Spitzenaccounts deuten die Indizien auf noch stärkere Konzentration, eher 5 → 90 %.** Der zweite Teil ist ein Indizienschluss, kein Messwert.

### 8.5 Was das für KI heißt

- **Keiner** der fünf stärksten Accounts ist nachweislich KI-produziert. Zwei andere Top-Accounts mit Apple-Refurb-Geräten (@kevin.finds, @airgeeksrc) mischen KI-gelabelte Clips bei. Diese erreichen nur 63–2.817 Views.
- Das Format der beiden überwiegend faceless Accounts ist genau das Format, das KI am billigsten nachbauen kann: Hände + Produkt + Voice-over + Skript-Template. Bei @cakedfinds besteht ein unbestätigter Verdacht auf TTS-Stimme. Wäre er richtig, wäre @cakedfinds ein Kategorie-D-Account mit geschätzt fünf- bis sechsstelliger Monatsprovision.
- Die Engine hängt an drei Dingen, die KI nicht liefert: **echte Produkte in echten Händen** (Muster, Footage), **Beziehungen zu Sellern** (höhere Sätze, eventuell Anzeigen-Verstärkung) und **Account-Historie** (die Accounts sind 1–7 Jahre alt, @hannahbentley seit 2019).
- Die beiden stärksten KI-Accounts liegen nach Claimed-Daten bei einem Fünftel bis einem Zwanzigstel des GMV der faceless Spitzenaccounts. Der eine ist heute inaktiv, beim anderen ist nur ein Monat belegt.

**Korrektur am alten Bericht:** Der alte Bericht hat die Spitzenverdiener nicht formatgeprüft. Faceless Formate mit echten Produkten (F, eventuell D) gehören zu den dauerhaftesten US-Spitzenformaten, meist als Baustein neben Gesichts-Videos. Richtig bleibt: Nachweislich KI-generierte Bilder (A, B, G) treiben bei keinem der geprüften Spitzenaccounts den Umsatz.

## 9. Was ist ein „Winner"? Trefferquoten und Monatsgewinn

### 9.1 Vier Definitionen, die man nicht vermischen darf

Der Begriff „Winner" wird in Kursen und Foren für völlig verschiedene Dinge benutzt. Wer „1 von 10 Videos ist ein Winner" hört, muss fragen, welche Definition gemeint ist. Im Modell (300 Videos pro Monat, ein Account) ergeben sich diese Trefferquoten und Werte:

| Definition | Einsteiger: Quote / Ø-Provision je Winner / Anteil an Monatsprovision | Kompetent | Sehr gut |
|---|---|---|---|
| ≥ 10.000 Views | 1:30 / 37 € / 54 % | 1:12 / 125 € / 70 % | 1:7 / 342 € / 78 % |
| ≥ 100.000 Views | 1:543 / 385 € / – | 1:184 / 1.189 € / 18 % | 1:99 / 2.990 € / 30 % |
| ≥ 1 Verkauf | 1:7 / 12 € / 100 % | 1:3 / 41 € / 100 % | 1:2 / 113 € / 100 % |
| ≥ 10 Verkäufe | 1:114 / 125 € / 35 % | 1:24 / 246 € / 64 % | 1:10 / 481 € / 78 % |
| ≥ 100 € Provision | 1:641 / 520 € / – | 1:69 / 611 € / 44 % | 1:17 / 748 € / 69 % |
| ≥ 500 € Provision | 1:4.523 / 2.516 € / – | 1:427 / 2.748 € / – | 1:86 / 2.976 € / 39 % |

„–" bedeutet: Im typischen Monat kommt kein solches Video vor, der Median-Anteil ist 0.

**Empfohlene Arbeitsdefinitionen** für einen Test:

1. **Signal-Winner** (für Iterationsentscheidungen nach 48–72 Stunden): ≥ 10× Median-Views des eigenen Accounts **und** mindestens ein Produktklick. Er entsteht schnell und oft genug, um daraus zu lernen.
2. **Verkaufs-Winner** (für Skalierungsentscheidungen): ≥ 10 Verkäufe. Das ist die kleinste Einheit, bei der Konversion kein Zufall mehr ist.
3. **Ökonomischer Winner:** Provision ≥ Produktionskosten des ganzen Test-Batches, aus dem er stammt. Bei 5 € je Creative und einer Trefferquote von 1:20 sind das 100 €.

Die Definition „≥ 10.000 Views" ist für Geldfragen irreführend. Im Modell liefert ein solches Video beim Einsteiger im Schnitt 37 €, weil Reichweite ohne Kaufabsicht nichts wert ist.

### 9.2 10 Varianten pro Tag = 300 pro Monat: Was bringt welche Trefferquote?

Monatsgewinn = Winner × Ø-Provision je Winner − 1.660 € Kosten (300 × 5 € + 160 € Tools), vor Arbeitszeit. Alle Trefferquoten stammen aus dem optimistischeren Basisfall; im Co-Basisfall (Kapitel 4.3) und bei KI-visuellen Formaten mit Ausfallrisiko (4.7) liegen sie niedriger. Die Provision der Nicht-Winner ist weggelassen, das Ergebnis ist also leicht konservativ. K = Winner-Werte des Archetyps „kompetent", S = „sehr gut".

| Trefferquote → Winner/Monat | Winner = ≥ 1 Verkauf | Winner = ≥ 10 Verkäufe | Winner = ≥ 100 € Provision | Winner = ≥ 500 € Provision |
|---|---|---|---|---|
| 1:5 → 60 | K 788 € / S 5.132 € | K 13.076 € / S 27.218 € | K 35.000 € / S 43.244 € | K 163.232 € / S 176.906 € |
| 1:10 → 30 | K −436 € / S 1.736 € | K 5.708 € / S 12.779 € | K 16.670 € / S 20.792 € | K 80.786 € / S 87.623 € |
| 1:20 → 15 | K −1.048 € / S 38 € | K 2.024 € / S 5.559 € | K 7.505 € / S 9.566 € | K 39.563 € / S 42.981 € |
| 1:50 → 6 | K −1.415 € / S −980 € | K −186 € / S 1.227 € | K 2.006 € / S 2.830 € | K 14.829 € / S 16.196 € |
| **Im Modell beobachtete Quote** | E 1:7 · K 1:3 · S 1:2 | E 1:114 · K 1:24 · S 1:10 | E 1:641 · K 1:69 · S 1:17 | E 1:4.523 · K 1:427 · S 1:86 |

**Lesart:** Die Matrix ist nur dort realistisch, wo die angenommene Trefferquote in der Nähe der beobachteten liegt.

- „1:10 bei ≥ 10 Verkäufen" ist genau das Niveau des Archetyps „sehr gut" und ergibt 5.700–12.800 €.
- „1:20 bei ≥ 100 € Provision" liegt ebenfalls bei „sehr gut" (1:17) und ergibt 7.500–9.600 €.
- „1:5 bei ≥ 100 €" liegt 3,4× über der Rate, die das Modell selbst für sehr gute Betreiber erzeugt, „1:50 bei ≥ 500 €" 1,7×. Für kompetente Betreiber liegen beide 8- bis 14-mal darüber. Solche Kombinationen stammen typischerweise aus Kurs-Screenshots eines einzelnen Spitzenmonats.

### 9.3 Rückwärts gerechnet: Wie gut muss ein Winner sein?

Nötige Ø-Provision je Winner bei 300 Varianten, 5 € je Creative und 160 € Tools:

| Trefferquote | Winner/Monat | Break-even | 3.000 € | 5.000 € | 10.000 € | 20.000 € |
|---|---|---|---|---|---|---|
| 1:5 | 60 | 28 € | 78 € | 111 € | 195 € | 361 € |
| 1:10 | 30 | 56 € | 156 € | 222 € | 389 € | 722 € |
| 1:20 | 15 | 111 € | 311 € | 444 € | 778 € | 1.444 € |
| 1:50 | 6 | 277 € | 777 € | 1.110 € | 1.944 € | 3.610 € |

Wie oft erreicht im Modell ein einzelnes Video diesen Wert? Einige Beispiele:

| Ziel bei 1:10 | Einsteiger | Kompetent | Sehr gut |
|---|---|---|---|
| 3.000 € (Winner ≥ 156 €) | jedes 1.116. Video | jedes 112. Video | jedes 25. Video |
| 10.000 € (Winner ≥ 389 €) | jedes 3.303. Video | jedes 317. Video | jedes 65. Video |
| 20.000 € (Winner ≥ 722 €) | jedes 6.818. Video | jedes 642. Video | jedes 130. Video |

Ein „kompetenter" Betreiber müsste also eine rund 10- bis 30-mal bessere Trefferquote haben, als sein eigener Output hergibt, um mit 300 Varianten 3.000–10.000 € zu verdienen. Ein „sehr guter" braucht für 3.000 € eine 2,5-mal und für 10.000 € eine 6,5-mal bessere Trefferquote. Das ist der Kern: **Varianten-Volumen hilft nur, wenn die Winner-Qualität stimmt.** Die Qualität kommt aus Produkt, Warenkorb und Konversion, nicht aus der Anzahl der Varianten.

### 9.4 Wie viel Umsatz tragen die Top-Videos?

Die Nutzerfrage „20 Videos → 80 % des Umsatzes oder 5 Videos → 90 %?" beantwortet das Modell so:

| Archetyp | 150 Videos: Top 10 = Anteil | 300 Videos: Top 10 | 300 Videos: Top 3 |
|---|---|---|---|
| Einsteiger | 82 % | 70 % | 43 % |
| Kompetent | 73 % | 64 % | 40 % |
| Sehr gut | 69 % | 61 % | 39 % |

Im Modell liefern also 3 Videos rund 40 % und 10 Videos zwei Drittel bis vier Fünftel des Monats. Für echte Accounts ist der Anteil pro Video nicht öffentlich messbar. Die Indizien in Kapitel 8.4 deuten bei Spitzenaccounts auf noch stärkere Konzentration.

## 10. Creator-Ökonomie pro Creative

### 10.1 Umsatz, Gewinn und Erwartungswert je Video

Ein Account bis 300 Videos, darüber mehrere Accounts, **naiv** gerechnet (ohne Publikumsüberlappung und Verbund-Sperren, siehe Kapitel 7). Fixkosten 100 € plus 50 € je Account. Alle Werte in EUR pro Monat, **vor Arbeitszeit**, Basisfall. Im Co-Basisfall (virale Videos konvertieren schlechter) liegen die Provisionen im Median um rund 37–39 %, im Mittel um rund 45–47 % niedriger. Für KI-visuelle Formate kommt das Ausfallrisiko aus Kapitel 4.7 hinzu.

| Archetyp | Videos | Provision Median / Mittel | Gewinn-Median bei 2 € / 5 € / 10 € / 20 € je Creative | Erwartungswert je Video bei 2 € / 5 € / 10 € / 20 € | Verlustmonate bei 2 € / 5 € / 10 € / 20 € |
|---|---|---|---|---|---|
| Einsteiger | 100 | 74 / 172 | −275 / −575 / −1.075 / −2.075 | −1,77 / −4,77 / −9,77 / −19,77 | 90 / 96 / 99 / 99 % |
| Einsteiger | 300 | 238 / 501 | −511 / −1.411 / −2.911 / −5.911 | −0,83 / −3,83 / −8,83 / −18,83 | 85 / 95 / 98 / 99 % |
| Einsteiger | 500 | 480 / 855 | −719 / −2.219 / −4.719 / −9.719 | −0,69 / −3,69 / −8,69 / −18,69 | 84 / 96 / 99 / 100 % |
| Einsteiger | 1.000 | 1.097 / 1.703 | −1.202 / −4.202 / −9.202 / −19.202 | −0,60 / −3,60 / −8,60 / −18,60 | 82 / 96 / 99 / 100 % |
| Kompetent | 100 | 546 / 1.310 | 196 / −103 / −603 / −1.603 | 9,61 / 6,61 / 1,61 / −8,39 | 35 / 56 / 74 / 88 % |
| Kompetent | 300 | 1.771 / 3.879 | 1.021 / 121 / −1.378 / −4.378 | 10,43 / 7,43 / 2,43 / −7,57 | 21 / 47 / 70 / 87 % |
| Kompetent | 500 | 3.597 / 6.365 | 2.397 / 897 / −1.602 / −6.602 | 10,33 / 7,33 / 2,33 / −7,67 | 11 / 37 / 66 / 86 % |
| Kompetent | 1.000 | 8.230 / 12.706 | 5.930 / 2.930 / −2.069 / −12.069 | 10,41 / 7,41 / 2,41 / −7,59 | 5 / 28 / 61 / 86 % |
| Sehr gut | 100 | 2.415 / 5.591 | 2.065 / 1.765 / 1.265 / 265 | 52,41 / 49,41 / 44,41 / 34,41 | 5 / 12 / 25 / 46 % |
| Sehr gut | 300 | 7.849 / 16.336 | 7.099 / 6.199 / 4.699 / 1.699 | 51,95 / 48,95 / 43,95 / 33,95 | 2 / 7 / 19 / 41 % |
| Sehr gut | 500 | 15.735 / 26.772 | 14.535 / 13.035 / 10.535 / 5.535 | 51,15 / 48,15 / 43,15 / 33,15 | 0 / 2 / 10 / 31 % |
| Sehr gut | 1.000 | 35.909 / 53.236 | 33.609 / 30.609 / 25.609 / 15.609 | 50,94 / 47,94 / 42,94 / 32,94 | 0 / 0 / 5 / 22 % |

### 10.2 Break-even je Video

Bei Median-Konversion des Archetyps braucht ein einzelnes Video diese Verkäufe bzw. Views, um seine eigenen Kosten zu decken:

| Archetyp | Provision je Verkauf | 2 € | 5 € | 10 € | 20 € |
|---|---|---|---|---|---|
| Einsteiger | 2,67 € | 0,75 Verkäufe / 5.250 Views | 1,9 / 13.127 | 3,8 / 26.254 | 7,5 / 52.509 |
| Kompetent | 3,97 € | 0,5 / 1.789 | 1,3 / 4.473 | 2,5 / 8.946 | 5,0 / 17.892 |
| Sehr gut | 6,29 € | 0,3 / 670 | 0,8 / 1.677 | 1,6 / 3.354 | 3,2 / 6.709 |

### 10.3 Was daraus folgt

- **Die maximal tragbaren Kosten je Creative** entsprechen der mittleren Provision je Video: rund 1,70 € (Einsteiger), 12,40 € (kompetent) und 54 € (sehr gut) im Basisfall, im Co-Basisfall etwa 1 €, 7 € und 28 €. Darüber ist der Erwartungswert negativ, egal wie viele Videos produziert werden. **Arbeitszeit ist darin nicht enthalten.** Wer für ein Video 15 Minuten braucht und seine Stunde mit 15 € ansetzt, hat bereits 3,75 € Zeitkosten je Video. Damit ist der kompetente Archetyp im Co-Basisfall bei jeder bezahlten Produktion nahe null.
- **Premium-KI-Videos für 18–35 USD** (alter Bericht, Kapitel 12.2) rechnen sich nur im Archetyp „sehr gut". Für alle anderen muss eine Variante unter 2–5 € kosten. Das geht praktisch nur, wenn echtes Footage wiederverwendet und KI für Skript, Stimme, Schnitt und Hook-Varianten genutzt wird.
- **Das typische Video deckt nie seine Kosten.** Beim kompetenten Archetyp liegt der Median bei rund 600 Views, der Break-even bei 5 € aber bei rund 4.500 Views. Der Monat wird ausschließlich über die wenigen Ausreißer profitabel. Wer nach 30 Videos aufhört, weil „die Videos nichts verkaufen", hat die Verteilung nicht verstanden. Wer nach 300 Videos ohne einen Verkaufs-Winner weitermacht, hat sie auch nicht verstanden.

## 11. Die Chancenseite: Welche KI-Eigenschaften sind echte Wettbewerbsvorteile?

Maßstab: Ein Vorteil ist **real**, wenn er (a) eine der drei Stellschrauben des Modells bewegt (Reichweite je Video, Konversion je View, Kosten je Video), (b) regelkonform nutzbar ist und (c) nicht sofort von allen Wettbewerbern kopiert wird. Er ist **theoretisch**, wenn er nur in Kurs-Präsentationen oder unter Regelverstoß funktioniert.

| KI-Eigenschaft | Wirkt auf | Einordnung | Begründung und Evidenz |
|---|---|---|---|
| 10× mehr Tests | Kosten, Chance auf Ausreißer | **Real, aber gedeckelt** | Kosten je Variante sinken von 20–100 € (UGC-Creator) auf 0,50–2 € (vorhandenes Footage + KI-Skript/-Stimme/-Schnitt). Deckel: EU-Pilotprogramm max. 21 Shopping-Videos pro Woche; EU-Inhaltsrichtlinie 4.9.4 wertet „große Mengen nahezu identischer Videos" und „koordinierte Massenveröffentlichungen über mehrere Konten" als minderwertig. Mehr Tests erhöhen im Modell vor allem den Median, nicht die Qualität der Winner (Kapitel 9). |
| Hook-Testing | Reichweite je Video | **Real, stärkster Produktionshebel** | Einziger Mechanismus, der in allen zehn früher rekonstruierten Accounts vorkam (Hook-Split-Tests mit ca. 1:10 Trefferquote). KI macht Hook-Varianten fast kostenlos. **Regelgrenze:** Die EU-Richtlinie 4.9.4 wertet „nahezu identische Videos mit minimalen kreativen Unterschieden" als minderwertig, die US-Regeln verlangen, dass jeder Post „something new" bietet. Eine Variante sollte sich daher mindestens in Kaufargument oder Szene unterscheiden, nicht nur in den ersten zwei Sekunden. Sinnvoll ist eine Obergrenze von etwa 3–5 Varianten je Konzept. |
| Varianten von Winnern | Reichweite, Kosten | **Real, moderat** | Explore/Exploit-Simulation (Kapitel 13): −12 bis +73 % Provision bei gleicher Videozahl, ohne extreme Ermüdungsannahmen −6 bis +31 %, dazu rund 27 % weniger Produktionskosten. Kein Faktor 10. Beobachtet: fünf fast identische Varianten an zwei Tagen streuten zwischen 1.700 und 184.600 Plays (@beautypickshub). Das zeigt das Lernsignal, aber auch genau das Muster, das die EU-Regeln als minderwertig einstufen. |
| Skript-Analyse fremder Winner | Reichweite, Konversion | **Real, erodiert** | ASR-Transkripte und LLM-Klassifikation von Top-Videos kosten Cent-Beträge. Vorteil schrumpft, weil Analytics-Anbieter (FastMoss, Kalodata) dieselbe Funktion für alle verkaufen. |
| Winner-Analyse eigener Daten | Konversion | **Real** | Wer Views, Klicks und Bestellungen je Video systematisch mit Hook, Länge, Produkt und Uhrzeit verknüpft, lernt schneller als der Wettbewerb. Datenbasis: nur eigene Accounts; Drittanbieter-Zahlen sind Schätzungen. |
| Angles (Problem/Lösung, Vergleich, Geschenk, Preisanker) | Konversion | **Real** | Konversion hängt stärker am Kaufargument als am Bild. KI erzeugt Angles schnell; der Test zeigt, welcher verkauft. |
| Trend-Reaktion | Reichweite | **Teilweise real** | Skript und Schnitt in Stunden statt Tagen. Engpass bleibt das physische Produkt (Muster-Versand dauert Tage) und das Footage. |
| Übersetzung/Lokalisierung | Marktgröße | **Teilweise real** | US-Policy erlaubt KI-Dubbing ausdrücklich; EU-Bedingungen nennen Creator-Dubbing-Funktionen. Aber: Affiliate-Rechte sind an das Registrierungsland und den Zugriffsort gebunden. Ein DE-Account kann nicht einfach FR/IT/ES bedienen. Jedes Land braucht einen eigenen, dort registrierten und von dort genutzten Account. |
| KI-B-Roll | Reichweite | **Teilweise real** | Für Kontextszenen erlaubt; als Ersatz für die Produktdemo verboten (Shop-AIGC-Policy: keine KI-Renderings statt echter Produktwirkung). |
| KI-Personas | Reichweite, Vertrauen | **Theoretisch / riskant** | Vollvirtuelle Influencer haben keine Shop-Aktivität (C1). Eine KI-Person, die ein Produkt „getestet hat", ist rechtlich ein Fake-Testimonial (FTC, UWG, DMCC, KI-VO Art. 50). Einzige Ausnahme sind klar gekennzeichnete, erkennbar fiktive Figuren ohne Nutzungsbehauptung. |
| KI-Stimme statt eigener Stimme | Kosten | **Real in den USA, riskant in der EU** | US-Community-Guidelines: generisches TTS braucht kein Label. EU-Inhaltsrichtlinie 4.9.4: „standardisierte Erzählformen, z. B. Text-zu-Sprache … ohne sinnvollen kreativen Beitrag" gelten als minderwertig. UK/EU-AIGC verlangt Offenlegung, sobald KI „materially contributes to … voice". |

**Gesamturteil:** KI ist ein echter Kostenvorteil und ein echter Geschwindigkeitsvorteil beim Testen. Sie ist kein eigenständiger Reichweiten- oder Konversionsvorteil. Die Größen, die im Modell über 3.000 oder 10.000 € entscheiden (GMV je 1.000 Views, Provisionssatz, Warenkorb, Ausreißer-Wahrscheinlichkeit), werden von Produktwahl, Kaufargument und Glaubwürdigkeit bestimmt. KI hilft, diese Größen schneller zu finden. Sie ersetzt sie nicht.

**Was die Gegenbeweis-Suche dazu zeigt:**

- Die Spitzenaccounts nutzen genau die Vorteile aus der oberen Tabellenhälfte: Skript-Templates, Volumen, Varianten, schnelle Produktwechsel. Die Stimme ist bei den dauerhaftesten Accounts menschlich oder nicht bestimmbar.
- Die „theoretischen" Vorteile (Personas, KI-Stimme als Ersatz für echte Präsenz) finden sich vor allem bei Accounts, die nach Wochen bis Monaten gesperrt oder eingebrochen sind.
- Der größte Hebel der Spitzenaccounts, die bezahlte Verstärkung durch Seller, ist kein KI-Vorteil. KI kann ihn nur indirekt erhöhen, indem mehr gut konvertierende Creatives entstehen, aus denen Seller auswählen.

## 12. Der sehr kompetente Solo-Operator: Was ist nach 90 Tagen realistisch?

Profil laut Aufgabe: technisch stark, gute Copywriting-Fähigkeiten, versteht TikTok, kann automatisieren, arbeitet datengetrieben, testet aggressiv, Budget 1.000–3.000 €, 30–60 Stunden pro Woche, 90 Tage.

### 12.1 Strategie, die dieser Operator wählen sollte

1. **Markt:** Für einen Betreiber mit Wohnsitz in Deutschland ist DE der legale Weg: 500 Follower, Zugriff aus DE, Pilotphase mit max. 21 Shopping-Videos pro Woche. Die USA gehen nur, wenn eine Person in den USA **selbst der Creator** ist: Sie verifiziert den Account mit eigenem Ausweis, führt ihn selbst und erhält die Provision selbst oder über den offiziellen Agentur-Split (Creator Agency Partner). Der deutsche Betreiber kann dann nur als beauftragter Produktionsdienstleister arbeiten, ohne geteilte Zugangsdaten. Gekaufte Accounts, VPN oder Strohleute sind Vertragsbruch mit Totalverlustrisiko.
2. **Format:** F mit KI-Unterstützung, oder E mit eigenem Gesicht. Echte Produkte in echten Händen, eigene Stimme oder gekennzeichnete KI-Stimme. KI für Skripte, Hook-Varianten, Schnitt, Untertitel und Winner-Analyse. Keine KI-Personen, keine KI-Renderings statt Produktdemo, keine Vorher-nachher-Bilder. In UK zeigen alle geprüften Spitzenaccounts über 3.000 € ihr Gesicht. Das spricht dafür, E ernsthaft mitzuprüfen.
3. **Produktwahl:** Produkte mit 15–20 %+ Provision, 25–70 € Warenkorb, sichtbarer Seller-Aktivität und nicht mehr als einigen Hundert aktiven Creators. In DE gibt es solche Produkte nur vereinzelt (Kapitel 6.3).
4. **Seller-Beziehungen:** Ab der ersten Woche Target-Collab-Anfragen an 10–20 Seller der getesteten Produkte. Höhere Sätze und die Chance, dass ein Seller Videos in Anzeigen nutzt, sind der größte bekannte Hebel (Kapitel 4.6, dort als Hypothese).
5. **Rhythmus:** Tag 1–10 organischer Aufbau auf 500 Follower mit Produktinhalten ohne Link. Gekaufte Follower sind tabu. Danach Pilotphase mit 3 Shopping-Videos pro Tag. Ab Monat 2 5–10 pro Tag auf einem Account. Ein zweiter Account in getrennter Nische frühestens in Monat 3.
6. **Datenschleife:** Jedes Video mit Hook-ID, Produkt, Länge und Uhrzeit protokollieren. Wöchentliche Auswertung: Median-Views, 3-Sekunden-Hold, Produktklicks und Bestellungen je 1.000 Views. Varianten nur von Videos mit mindestens 10-facher Median-Reichweite **und** Bestellungen.

### 12.2 Einschätzung nach 90 Tagen

Hier stehen **keine Prozentzahlen**, weil es keine belastbare empirische Basis für echte Wahrscheinlichkeiten gibt. Die Monte-Carlo-Werte aus Kapitel 4, 5 und 15 gelten nicht für diesen Operator, denn sein Archetyp ist unbekannt.

**Definition der Stufen** (vom stärksten zum schwächsten Befund):

- **frequently observed:** viele dokumentierte Fälle, die diese Stufe innerhalb von rund 90 Tagen ab Null erreichen.
- **observed:** mindestens ein glaubwürdig dokumentierter Fall innerhalb von rund 90 Tagen ab Null.
- **plausible:** Fälle auf dieser Stufe existieren, aber nur nach längerer Zeit oder in einem Nachbarmarkt; der Mechanismus ist belegt.
- **uncommon:** Fälle existieren nur nach deutlich längerer Zeit (6+ Monate), nur als behaupteter Einzelfall oder nur als kurzer Spitzenmonat.
- **very unlikely:** kein Fall in diesem Markt auf dieser Stufe, oder nur bei Accounts, die mehrere Jahre alt sind.

Die Tabelle bezieht sich auf den **Gewinn im dritten Monat vor Arbeitszeit**. Bei jeder Evidenz steht, ob es um Provision oder Gewinn geht.

| Gewinn im Monat 3 | DE (legaler Heimatweg) | USA (nur mit echtem US-Creator als Partner) | Evidenz |
|---|---|---|---|
| **0–1.000 €** | **frequently observed** | **frequently observed** | 67 von 80 zufällig gezogenen US-Affiliates ohne GMV in 28 Tagen (Nenner inkl. inaktiver Affiliates); bei einer Marke postete nur etwa jeder achte von 21.365 Affiliates überhaupt, rund 99 % hatten keinen Umsatz; Built-Bar-Durchschnitt 7 USD Provision in 28 Tagen; dokumentierte DE/UK-Kleinversuche mit zweistelligen Provisionen; gesichtetes Dashboard eines KI-Accounts mit 154,78 USD Provision auf 325.400 Views |
| **1.000–3.000 €** | **plausible** | **observed** | DE: Selbstberichte mit 1.000–1.500 € Provision/Monat bei 30 Videos/Tag und „deutlich über 1.000 € Provision in einer Woche" nach einem 90-Tage-Test (beide Claimed, alter Bericht); UK-Faceless-Mittelklasse mit geschätzt 1.100–1.900 € Provision, allerdings nach über 30 Monaten. US: Massen-Poster mit rund 10.000 USD Provision in etwa drei Monaten, organisch geprüfter Reddit-Autor (Claimed) |
| **3.000–5.000 €** | **uncommon** | **plausible** | DE/EU: 4.700 € Provision/Monat über 2–3 Accounts, überwiegend Hands-only, Zeitraum unklar (Claimed, Coaching-Bias); Italien ca. 3.000 € Provision nach 7 Monaten, Top 100 seiner Kategorie (Claimed). Das DE-Top-Produkt zahlt ca. 1,40 € je Verkauf. US: mehrere organisch geprüfte Selbstberichte mit 4.000–8.000 USD Provision, teils nach 4–5 Monaten (Claimed). Im US-Pilot sind bis 5.000 Follower nur 3 Shopping-Videos pro Tag erlaubt, und ein Partner-Split kann den Ertrag des deutschen Betreibers leicht halbieren |
| **5.000–10.000 €** | **very unlikely** | **uncommon** | DE: kein Fall innerhalb von 90 Tagen; 23.400–32.000 € Provision/Monat nur für langjährige menschliche Creators einer Agentur (Claimed). US: Coaching-Fälle mit 8.000–10.000 USD nach mehreren Monaten, jeweils mit Sperren mehrerer Accounts (Claimed) |
| **10.000–20.000 €** | **very unlikely** | **very unlikely** | nur bei Accounts beobachtet, die Monate bis Jahre alt sind (@mackfinds_: Spitzenmonat im 9. Monat nach Anlage; Top-10-Accounts 1–7 Jahre alt) |
| **20.000 €+** | **very unlikely** | **very unlikely** | kein glaubwürdig belegter Fall innerhalb von 90 Tagen ab Null; alle Fälle sind langjährige Accounts oder unbelegte Verkäufer-Zahlen |

### 12.3 Was diese Einschätzung verschieben würde

- **Nach oben:** ein bestehender Account mit Reichweite; ein Seller, der Videos in Anzeigen nutzt; ein Produkt mit 20 %+ Provision und Werbebudget im Wachstum; Q4-Saison.
- **Nach unten:** jede AIGC- oder Originalitäts-Violation in der Pilotphase; Produkte in Supplement/Skincare (strengste KI-Regeln); reines TTS in der EU (Richtlinie 4.9.4); Arbeitszeit als Kosten (bei 30–60 Stunden pro Woche und 15 €/Stunde sind das 1.950–3.900 € pro Monat).
- **Nicht durch Kompetenz ersetzbar:** Account-Alter und Seller-Beziehungen. Beide wachsen nur mit der Zeit.

## 13. Sweet-Spot-Hypothese: „AI-powered TikTok Shop Creative Factory"

### 13.1 Definition

Echte Produkte, echtes Footage (Hände, Produkt, eventuell UGC), dazu KI für Skripte, Stimme, B-Roll, Schnitt, Hook-Varianten und Datenanalyse. Schnelle Iteration auf Gewinner. Posten bleibt manuell, weil die öffentliche API keine Produktlinks setzen kann.

### 13.2 Was dafür spricht

| Beleg | Art | Was er zeigt |
|---|---|---|
| Faceless Top-Accounts (@hannahbentley, @cakedfinds, @bennettfinds) | Analytics (Claimed) + Format Verified | Das Format „Hände + Produkt + Voice-over", menschlich produziert, erreicht in den USA dauerhaft sechsstellige GMV-Monate. |
| @cakedfinds: Skript-Template, identische Caption auf 9 von 10 Videos, geschätzt ca. 19 Videos/Tag | Verified (Caption, Template); Videozahl Estimated | Eine Fabrik-Logik (Template × Produkt × Volumen) funktioniert an der Spitze. Ob KI die Stimme liefert, ist offen. |
| @spongebobprodsz: KI-Szenen um echte Produktbilder, 6–10 Beiträge/Tag | Verified (Format, Label, aktuelle Aktivität); Dauer und Umsatz Claimed | Ein einzelner Fall zeigt, dass ein KI-gelabeltes Format mit echtem Produktbild aktiv bleiben kann. Eine Regel lässt sich daraus nicht ableiten. |
| @beautypickshub: fünf fast identische Varianten an zwei Tagen mit 184.600 / 86.900 / 70.800 / 2.600 / 1.700 Plays | Verified | Varianten-Tests liefern starke Streuung und damit Lernsignal. Sie zeigen zugleich das Muster „nahezu identische Videos", das die EU-Regeln als minderwertig einstufen. Kein Vorbild für die Umsetzung. |
| Rekonstruktion von zehn Accounts im alten Bericht | Verified/Claimed | Hook-Split-Tests mit ca. 1:10 Trefferquote waren der einzige Mechanismus, der überall vorkam. |
| Creative-Ökonomie (Kapitel 10) | Modell | Bei 0,50–2 € je Variante bleibt der Erwartungswert je Video für „kompetent" positiv, bei 10 € nur knapp, bei 20 € ist er negativ. Arbeitszeit ist dabei nicht eingerechnet. |

**Dagegen spricht:** In UK, dem DE-nächsten Markt, machen rein faceless Accounts nur 1,6 % des GMV der Top-25 aus. Alle 13 UK-Creators mit geschätzt ≥ 3.000 € zeigen ihr Gesicht.

### 13.3 Was die Simulation sagt

Explore/Exploit-Simulation mit 300 Videos pro Monat (`mc_factory.py`): Woche 1 testet 25 Konzepte mit je 3 Varianten. Danach gehen pro Woche 50 Varianten an die bisher besten 5 Konzepte, dazu 25 neue Konzepte. Neue Konzepte kosten 8 €, Varianten 1,50 €. Das flache Posten kostet 5 € je Video.

| Archetyp | Anteil des Erfolgs, der am Konzept hängt | Provision Median flach → Factory | Gewinn-Median flach → Factory |
|---|---|---|---|
| Kompetent | 20 % | 2.032 → 1.929 € | 372 → 669 € |
| Kompetent | 40 % | 2.017 → 2.275 € | 357 → 1.015 € |
| Kompetent | 60 % | 1.981 → 2.588 € | 321 → 1.328 € |
| Sehr gut | 40 % | 8.747 → 9.777 € | 7.087 → 8.517 € |
| Sehr gut | 60 % | 8.588 → 11.093 € | 6.928 → 9.833 € |
| Kompetent, 40 %, ohne Publikumsermüdung | 40 % | 2.017 → 3.497 € | 357 → 2.237 € |
| Kompetent, 40 %, starke Ermüdung (−15 % je Variante) | 40 % | 2.017 → 1.782 € | 357 → 522 € |

Alle Werte gelten im Basisfall, vor Arbeitszeit und ohne Ausfallrisiko für KI-visuelle Formate (Kapitel 4.7).

**Lesart:** Die Factory bringt im Median **−6 % bis +31 % Provision** bei gleicher Videozahl, mit den Extremannahmen zur Publikumsermüdung **−12 % bis +73 %**, und **rund 27 % geringere Produktionskosten** (1.100 statt 1.500 €). Im Gewinn-Median macht das beim kompetenten Archetyp den Unterschied zwischen knapp Null und rund 1.000 €. Sie macht aber keinen kompetenten Betreiber zum sehr guten. Der Hebel „10× mehr Varianten" ist real, aber durch Publikumsermüdung und die Originalitätsregeln begrenzt.

Der größere Hebel liegt außerhalb der Factory: **bezahlte Seller-Verstärkung** (Kapitel 4.6). Eine Factory, die zuverlässig gut konvertierende Creatives liefert, erhöht die Chance, dass Seller diese Videos in Anzeigen nutzen. Diese Kette ist plausibel, aber öffentlich nicht messbar.

### 13.4 Regelrahmen

| Element | USA | DE/EU |
|---|---|---|
| Echtes Produkt, echte Hände | unkritisch | unkritisch |
| KI-Skript | unkritisch, kein Label nötig | unkritisch; die AIGC-Definition nennt „scripts", Offenlegung vorsichtshalber |
| KI-Stimme | generisches TTS ohne erkennbare echte Stimme: kein Label nötig; realistische Stimme: Label | Offenlegung, sobald KI „materially contributes to … voice"; TTS-Vorlagen ohne kreativen Beitrag = „wenig ansprechend" (Richtlinie 4.9.4) |
| KI-B-Roll | Label; nicht als Ersatz der Produktdemo | Label; KI-VO Art. 50 für realistische Szenen |
| Hook-Varianten | „each post should offer something new"; reine Re-Uploads verboten | „nahezu identische Videos mit minimalen kreativen Unterschieden" = minderwertig |
| Mehrere Accounts | bis 5 je Ausweis, eigenständige Inhalte | Verteilung derselben Inhalte über mehrere Konten = Spam |
| Automatisches Posten | nicht mit Produktlink möglich | dito |

### 13.5 Urteil

Die Creative Factory ist **das plausibelste der untersuchten Modelle**, aber nicht, weil KI nachweislich funktioniert. Ihr Format (F) ist in den USA an der Spitze **menschlich produziert beobachtet**. Ein KI-Format mit echtem Produktbild (G) ist aktiv und hat einen behaupteten fünfstelligen Monat. Vier Einschränkungen bleiben:

1. **Der KI-Beitrag zum Erfolg ist nirgends isoliert.** Die dauerhaftesten faceless Spitzenaccounts sind menschlich produziert oder nicht als KI nachweisbar. Die Factory-Hypothese sagt: „Mit KI schneller und billiger dasselbe." Ob KI-Stimme oder KI-Szenen dabei Konversion kosten, ist offen. Ältere Tests zeigen ähnliche Klickraten, aber schwächere Vertrauens- und Kaufsignale.
2. **Die Spitze hängt an Account-Alter, Seller-Beziehungen und vermutlich Seller-Budgets**, nicht an der Produktionsgeschwindigkeit.
3. **In UK und vermutlich DE spielt faceless an der Spitze kaum eine Rolle.** Die US-Befunde lassen sich nicht einfach übertragen.
4. **In der EU ist der Spielraum enger:** TTS-Vorlagen gelten als minderwertig, und die Offenlegungspflicht greift früher.

## 14. Aktualisiertes Verdict

Schwellen = Gewinn pro Monat in EUR vor Arbeitszeit. Die Stufen hier bewerten die **Stärke der Evidenz**, nicht die Wahrscheinlichkeit für einen neuen Betreiber (dafür Kapitel 12):

- **Observed:** Die Stufe ist durch mindestens eine neutrale Analytics-Quelle (Branchenmedien-Ranking) oder ein gesichtetes Dashboard belegt, **und** das Format dieses Modells ist für den Account geprüft. Bei KI-Modellen muss der KI-Einsatz nachgewiesen sein.
- **Plausible:** Account und Format sind geprüft, der Umsatz stammt aber nur aus einer interessierten Quelle; oder das sichtbare Ergebnis ist identisch mit einem beobachteten menschlichen Format.
- **Possible but weak evidence:** nur Einzelbehauptungen, nicht zuordenbare Screenshots oder ein unbewiesener KI-Verdacht.
- **No credible evidence found:** nichts Belastbares gefunden.

„Observed" heißt: Es kommt vor. Es heißt nicht: Es ist wahrscheinlich.

| Modell | 3k | 5k | 10k | 20k+ | Evidenz | Hauptrisiko |
|---|---|---|---|---|---|---|
| *Referenz: faceless mit echtem Produkt, menschlich produziert (kein KI-Modell)* | Observed | Observed | Observed | Observed | @hannahbentley, @cakedfinds, @bennettfinds (0,96–2,37 Mio. USD GMV/Monat, Kalodata via Net Influencer, Claimed); UK-Mittelklasse 1.100–1.900 € Provision (Estimated). Nur US-Markt ab 5k | Survivorship (oberste 0,002 %); Account-Alter und Seller-Beziehungen nicht kopierbar |
| **Virtual AI Influencer (A)** | Possible but weak evidence | No credible evidence found | No credible evidence found | No credible evidence found | 0 von 49 formatgeprüften US/UK-Top-Accounts; Clorox-Figuren mit 8,4 Mio. Impressions und rund 300 Bestellungen; ein KI-Sketch-Account mit „over $100k GMV" kumuliert (Claimed), laut Betreiber gesperrt | Keine Kaufkonversion; Fake-Testimonial-Recht (FTC, UWG, DMCC, KI-VO) |
| **AI UGC Avatar (B)** | Possible but weak evidence | Possible but weak evidence | Possible but weak evidence | No credible evidence found | Affiliate-Center-Screenshot mit 174.000 USD GMV in 30 Tagen, KI-Status und Handle nur vom Tool-Verkäufer behauptet; UK-Creatorin über KI-Funnel-Accounts (ohne Handle); „Granny"-Avatar mit geschätzt 1.500–5.000 USD im besten Monat, danach tot | Regel- und Rechtsrisiko (Testimonial einer nicht existierenden Person); Sperren; Kurzlebigkeit |
| **Faceless AI** (G: KI-Szene + echtes Produktbild; C: KI-Stimme über fremdes oder gerendertes Material) | Plausible | Plausible | Plausible | Possible but weak evidence | G: @spongebobprodsz aktiv und KI-gelabelt (Verified), ein Monat mit 302.090 USD GMV nur über eine Kalodata-Karte eines Kursverkäufers (Claimed) → geschätzt 12.000–54.000 USD Provision. C: @healthysmartdeals Claimed 68.670 USD GMV in 30 Tagen, heute inaktiv. Viele Gegenbeispiele mit Mini-Reichweite | Account-Ausfall (Kapitel 4.7); AIGC-Regeln (kein KI-Rendering statt Demo); Massen-Inhalte als „unoriginal"; mögliche Abhängigkeit von Seller-Budgets |
| **Real Product + AI Voice (D)** | Possible but weak evidence | Possible but weak evidence | Possible but weak evidence | Possible but weak evidence | Einziger Kandidat @cakedfinds (8 Monate Top-10) mit **unbewiesenem** KI-Stimmen-Verdacht (Coach-Aussage, Reddit-Frage, Audio-Indiz). Der Reddit-Satz „ai … TTS videos" meint wahrscheinlich „TikTok Shop videos" und zählt nicht | EU: TTS-Vorlagen = minderwertig, Offenlegungspflicht; unbekannt, ob KI-Stimme Konversion kostet |
| **Real UGC + AI Scaling (E)** | Plausible | Plausible | Plausible | Plausible | Menschliches UGC mit Gesicht ist auf allen Stufen beobachtet, in UK stellen Gesichts-Accounts alle 13 Creators ≥ 3.000 €. KI hinter der Kamera (Skript, Schnitt, Varianten) verändert das sichtbare Ergebnis nicht. Der KI-Anteil ist von außen nicht messbar | Braucht eine Person vor der Kamera; KI senkt Kosten, erzeugt aber keine Glaubwürdigkeit |
| **AI Creative Factory / Hybrid (F + KI, inkl. optionaler KI-Stimme und B-Roll)** | Plausible | Plausible | Possible but weak evidence | Possible but weak evidence | Das Format F ist menschlich produziert auf allen Stufen beobachtet (Referenzzeile). Mit eigener Stimme ist die Factory im Ergebnis identisch mit F. Mit KI-Stimme oder KI-B-Roll fehlt jeder Nachweis oberhalb einzelner Monate. In UK spielt faceless an der Spitze kaum eine Rolle (1,6 % des Top-25-GMV) | Survivorship; Konversionsverlust durch KI-Elemente unbekannt; Originalitätsregeln bei Varianten |

**Zusatz für den DE-Markt:** Alle belegten Fälle ab 5.000 € liegen im US-Markt. Für DE/EU gibt es keinen verifizierten Fall über rund 3.000 €. Claimed sind 4.700 €/Monat (DE, überwiegend Hands-only, mit KI-Nebenaccounts) und 23.400–32.000 €/Monat für langjährige menschliche Creators einer DE-Agentur. Eine creator-genaue DE-Rangliste ist nicht öffentlich. Die DE-Top-Produkte nach Volumen zahlen 1–3 € je Verkauf.

**Nicht in der Tabelle, aber belegt:** Slideshows mit fremden oder KI-Personenbildern und Vorher-nachher-Muster (H). Ein Spitzenmonat mit 51.700 USD Provision ist per Dashboard gesichtet, danach folgte der Absturz. Das Format ist regelwidrig (erfundene Ergebnisse, fehlendes Label) und wird nicht empfohlen.

**Veränderung gegenüber dem alten Bericht:**

- Der alte Bericht hat keine formale Verdict-Tabelle mit diesen Modellen geführt. Seine Einschätzungen lagen im Text (Modelle 3, 4 und 6, Kapitel 7 und 14).
- Neu ist die Referenzzeile: Menschlich produzierte faceless Formate sind in den USA auf allen Stufen beobachtet. Der alte Bericht hatte die Spitzenverdiener nicht formatgeprüft.
- Faceless AI (G) steigt durch @spongebobprodsz auf „plausible", steht aber auf einer einzigen Verkäufer-Quelle.
- D bleibt schwach belegt. Der vermeintliche Reddit-Beleg ist ein Übersetzungsfehler („TTS" = TikTok Shop).
- A und B bleiben unten.
- „20.000 € sind ein Team-Geschäft" wird ersetzt durch „20.000 € sind ein Geschäft für langjährige Accounts, vermutlich mit Seller-Verstärkung". Ob dahinter ein Team steht, variiert.

## 15. Welche Hypothese in 30 Tagen testen?

### 15.1 Bewertung der Kandidaten

Punkte 1–5 je Kriterium, 5 = am besten. „Kapital" 5 = wenig Kapital nötig, „Regulatorisches Risiko" 5 = geringes Risiko. „Upside" ist für den DE-Markt bewertet; im US-Markt läge es für D, E, F und G je einen Punkt höher. Produkt = Upside × Testbarkeit × Kapital × Feedback × Regulatorik.

| Hypothese | Upside (DE) | Testbarkeit in 30 Tagen | Kapital | Feedback-Geschwindigkeit | Regulatorisches Risiko | Produkt |
|---|---|---|---|---|---|---|
| Virtual AI Influencer (A) | 1 | 1 | 3 | 1 | 1 | 3 |
| AI UGC Avatar (B) | 2 | 3 | 4 | 4 | 1 | 96 |
| Faceless AI, KI-Szenen (G) | 2 | 4 | 4 | 4 | 2 | 256 |
| Real UGC + AI Scaling (E) | 3 | 3 | 5 | 3 | 5 | 675 |
| Real Product + AI Voice (D) | 3 | 4 | 5 | 4 | 3 | 720 |
| **Creative Factory, Format F + KI** | **3** | **5** | **5** | **4** | **4** | **1.200** |

Die Creative Factory liegt vorn. D wird **innerhalb** des Factory-Tests als Stimm-Arm geprüft. E ist die beste Alternative, wenn Kamera-Präsenz akzeptabel ist. Die Upside bleibt in DE **niedrig bis mittel**. Hoch wäre sie nur bei einem späteren, regelkonformen Transfer in den US-Markt.

**Verhältnis zum alten Bericht:** Das Audit bestätigt dessen Empfehlung (30-Tage-Test in DE, echtes Produkt in echten Händen, KI für Skripte, Stimme, B-Roll, Schnitt, harte Abbruchkriterien). Sie überlebt, weil keiner der neuen Befunde ein anderes Format mit besserer Evidenz und geringerem Regelrisiko zeigt. Geändert sind:

- eine Vorab-Prüfung vor jeder Ausgabe (Stufe 0);
- eine schärfere STOP-Regel (10 statt 3 Bestellungen, plus Konversions- und Stückkosten-Kriterium);
- ein randomisierter Stimm-Vergleich;
- aktive Seller-Ansprache;
- E als ausdrückliche Alternative.

### 15.2 Die Hypothese

> **H:** Ein kompetenter Solo-Operator erreicht mit echten Produkten in echten Händen und KI-beschleunigter Produktion (Skript, Hook-Varianten, Schnitt, optional gekennzeichnete KI-Stimme) im DE-Markt innerhalb von 30 Tagen mindestens 10 Bestellungen, mindestens 0,15 Bestellungen je 1.000 Views und eine Provision je Shopping-Video, die einen erkennbaren Weg zur Deckung der Sachkosten zeigt.

Was der Test **nicht** prüfen kann: ob 10.000 € erreichbar sind. Dafür sind 30 Tage und 60–90 Videos zu wenig. Er kann aber schnell und billig zeigen, dass Operator, Format und Markt **nicht** funktionieren. Genau das ist ein Falsifikationstest.

### 15.3 Der kleinste Falsifikationstest

**Stufe 0 (7 Tage, ohne Ausgaben):** Im DE-Affiliate-Marktplatz mindestens 6 Produkte finden mit ≥ 12 % Provision, 20–60 € Preis, mindestens 3 € Provision je Verkauf, echter Demo-Möglichkeit, außerhalb von Supplements und Wirkversprechen-Kosmetik, mit aktivem Seller (Target-Collabs oder erkennbare Werbung) und höchstens einigen Hundert Creators. **STOP, wenn weniger als 6 solche Produkte existieren.** Dann ist die DE-Variante widerlegt, bevor Geld fließt.

**Aufbau:**

1. **Account:** ein DE-Account. Tag 1–10: Produktinhalte ohne Link bis 500 Follower. Diese Phase liefert bereits Reichweitendaten (Median-Views, 3-Sekunden-Hold). Keine gekauften Follower. **Rückfallregel:** Sind die 500 Follower bis Tag 14 nicht erreicht, verlängert sich die Phase einmalig um 7 Tage. Ist die Schwelle auch an Tag 21 nicht erreicht, gilt die Reichweiten-Hypothese als verworfen. Existiert bereits ein Account mit 500+ DE-Followern, entfällt die Phase.
2. **Pilotphase (Tag 11–30):** 3 Shopping-Videos pro Tag, also ca. 60 Shopping-Videos. Mit bestehendem Account ca. 90.
3. **Produkte:** die 6 Produkte aus Stufe 0 aus 2 Nischen, je Produkt 10–15 Videos.
4. **Varianten-Protokoll:** Pro Produkt 3 Hook-Konzepte mit je höchstens 3–5 Varianten. Jede Variante unterscheidet sich mindestens im Kaufargument oder in der Szene, nicht nur im Einstieg. Keine Re-Uploads.
5. **Stimm-Vergleich:** Pro Posting-Slot entscheidet ein Münzwurf, ob das Video mit eigener Stimme oder mit gekennzeichneter KI-Stimme erscheint. Gleiche Produkte, gleiche Hook-Konzepte. Das Label ist Teil der Behandlung, denn in der EU ist es Pflicht. Vorab festgelegt: Bestellungen je 1.000 Views je Arm. Nebenwerte: Hold, Wiedergabezeit, Produktklicks. Mit rund 30 Videos je Arm und stark streuenden Views sind nur **große** Unterschiede erkennbar, etwa ein Faktor 2.
6. **Seller-Test:** Target-Collab-Anfragen an 10–20 Seller der Testprodukte.
7. **Budget:** Muster 150–400 € (sofern keine Gratismuster), KI-Tools 50–100 €, Licht/Stativ ca. 100 €. Summe 300–600 € Sachkosten, also rund 5–7 € je Shopping-Video, plus 30–60 Stunden pro Woche.

**Vorab festgelegte Messgrößen:** Views je Video (Median, Anzahl Videos mit mindestens 10-fachem Median); Bestellungen gesamt und je 1.000 Views; Provision gesamt und je Shopping-Video; Violations (AIGC, Originalität, „Reduced Visibility"); Stimm-Arme wie oben.

**STOP-Regel (Hypothese verworfen), geprüft nach ≥ 60 Shopping-Videos:**

- weniger als **10 Bestellungen** insgesamt, **oder**
- weniger als **0,15 Bestellungen je 1.000 Views** bei mindestens 20.000 Gesamt-Views, **oder**
- **eine** AIGC- oder Originalitäts-Violation.

**Teil-STOP für die KI-Stimme:** Liegen die Bestellungen je 1.000 Views im KI-Arm bei weniger als der Hälfte des Arms mit eigener Stimme, fliegt die KI-Stimme raus. KI bleibt dann nur für Skript, Schnitt und Varianten. Kleinere Unterschiede kann dieser Test nicht zeigen.

**GO für die nächsten 60 Tage:** kein STOP, mindestens ein Video mit 10-fachem Median **und** mindestens 3 Bestellungen, mindestens eine positive Seller-Antwort, und in den letzten 30 Shopping-Videos eine Provision je Video von mindestens einem Drittel der Sachkosten je Video (also rund 2 €). In der zweiten Stufe gilt zusätzlich: ≥ 0,4 Bestellungen je 1.000 Views über ≥ 150 Shopping-Videos und Provision je Video ≥ Sachkosten je Video. Erst danach lohnt ein zweiter Account.

### 15.4 Wie scharf ist dieser Test?

Monte-Carlo-Werte (`mc_test.py`, Ergebnisse in `mc_test_results.json`). Sie sind **US-kalibriert** und gelten für den ersten Monat mit 40–70 % Reichweite. Für DE sind sie nur eine Orientierung. Sie sind Fehlerraten **des Tests im Modell**, keine Erfolgswahrscheinlichkeiten eines Betreibers.

| Wahrer Archetyp | Nur „< 10 Bestellungen": 60 Videos | 90 Videos | Volle STOP-Regel (ohne Violations): 60 Videos | 90 Videos |
|---|---|---|---|---|
| Einsteiger | 46–65 % | 31–51 % | 55–69 % | 45–58 % |
| Kompetent | 9–20 % | 4–10 % | 16–25 % | 12–17 % |
| Sehr gut | 1–5 % | 0,4–2 % | 4–7 % | 3–5 % |

**Lesart:** Ein STOP ist ein starkes Signal gegen „kompetent oder besser". Einen sehr guten Betreiber stoppt der Test nur selten fälschlich, einen kompetenten in 12–25 % der Fälle, meist wegen schlechter Produktwahl im ersten Monat. Ein Nicht-STOP ist dagegen nur ein schwaches Signal, denn 31–55 % der Einsteiger überstehen die STOP-Regel durch Glück. Das GO mit Stückkosten-Kriterium ist strenger, seine Fehlerraten sind nicht simuliert. Deshalb folgt auf ein GO die zweite Stufe von 60 Tagen.

**Was der Test zur offenen Frage dieses Audits beitragen kann:** Er zeigt, ob eine gekennzeichnete KI-Stimme bei echtem Produkt die Konversion **stark** senkt. Ist das der Fall, bleibt KI ein Werkzeug hinter der Kamera. Ist es nicht der Fall, wäre D ein Kandidat für die zweite Stufe. Mehr als ein Hinweis ist mit dieser Stichprobe nicht möglich.

## Anhang: Methodik, Grenzen und Dateien

**Vorgehen.** Zehn Such-Agenten mit je einem eigenen Suchwinkel und einem gemeinsamen Briefing hatten den Auftrag, den alten Bericht zu widerlegen. Das Briefing fragte ausdrücklich, ob der alte Bericht zu pessimistisch war. Die Fundlage ist dadurch bewusst in Richtung optimistischer Funde verschoben. Bei den zwei Agenten für US- und UK-Top-Verdiener hat je ein getrennter Prüfer die drei stärksten Funde erneut geöffnet, auf TikTok nachgeprüft (Profil, neueste Videos, Frame-Analyse eines Videos) und nachgerechnet. Die übrigen acht Agenten haben ihre drei stärksten Funde selbst gegengeprüft. Die Prüfvermerke stehen jeweils am Ende der Protokolle in `quellen/redteam/`. Der Lead-Analyst hat den stärksten KI-Fall (@spongebobprodsz) und die TikTok-Regel zur Provision auf Anzeigen-GMV selbst geprüft. Zwei unabhängige Gutachter haben den Entwurf dieses Audits auf Zahlen und auf Verzerrung in beide Richtungen geprüft. Ihre Korrekturen sind eingearbeitet.

**Grenzen.**

- Alle Umsatzzahlen der Spitzenaccounts sind Drittanbieter-Schätzungen (Kalodata, FastMoss, EchoTik) oder Selbstauskünfte. Provisionen sind durchgehend Estimated.
- Ob eine Stimme synthetisch ist, lässt sich aus öffentlichen Daten nicht beweisen. Die Stimmen wurden nicht angehört, nur transkribiert.
- Das `isAd`-Flag in TikToks Rohdaten ist nicht öffentlich dokumentiert. Die Deutung „vom Seller als Anzeige ausgespielt" ist eine Interpretation.
- Die Gegenbeispiele sind extrem selektiert (oberste 0,002 % der Affiliates). Sie zeigen, was möglich ist, nicht was wahrscheinlich ist.
- Das Monte-Carlo-Modell ist an wenigen öffentlichen Verteilungsdaten kalibriert und im oberen Rand optimistisch. Seine Wahrscheinlichkeiten sind bedingte Modellaussagen.
- Die Kapitel nutzen getrennte Simulationsläufe (andere Zufallszahlen, teils ohne Betreiber-Effekt). Gleiche Szenarien weichen daher um wenige Prozent voneinander ab, z. B. kompetent mit 300 Videos: Median 1.768 (Kapitel 4) gegenüber 1.771 (Kapitel 10), 1.935 (Kapitel 4.6) und 2.017 (Kapitel 13).
- Persönliche Details privater Reddit-Nutzer aus den Autorenprüfungen und E-Mail-Adressen aus Creator-Bios sind in den veröffentlichten Protokollen entfernt.

**Dateien in `quellen/redteam/`.**

| Datei | Inhalt |
|---|---|
| `redteam_top_earners_us.md` | 100 Monatseinträge der US-Top-10 (Nov 2025–Aug 2026), Formatprüfung von 24 Accounts, Prüfvermerke |
| `redteam_top_earners_uk_eu.md` | FastMoss UK H1 2026, Formatanteile, DE-Marktgröße, Prüfvermerke |
| `redteam_tiktok_hybrid.md` | Faceless- und Hybrid-Accounts, `isAd`-Anteile, Views-Hochrechnung vs. Kalodata |
| `redteam_ai_aggregate.md` | Biverse-Zahlen, Top-down-Schätzung, @spongebobprodsz |
| `redteam_youtube_dashboards.md` | YouTube-Fälle mit Einkommensangaben, Kursverkäufer-Bias |
| `redteam_web_agencies.md` | Agenturen, Tool-Anbieter, Affiliate-Center-Screenshots |
| `redteam_reddit_x.md` | Reddit/X mit Autorenprüfung, Astroturfing-Nachweise, Negativbelege |
| `redteam_product_top_videos.md` | 28 Gewinner-Videos mit Views/Bestellungen/GMV, Ausreißer-Rechnung |
| `redteam_product_economics.md` | Produkte zu den Beispielen A/B/C, Anteil am Produktvolumen |
| `redteam_portfolio_rules.md` | Account-Limits, Pilotphasen, Verbund-Regeln, Agenturen, API |
| `lead_notes.md` | eigene Zusatzprüfung: Provision auf Anzeigen-GMV |
| `mc/mc_final.py`, `mc_final_results.json` | kalibriertes Video-Level-Modell (Kapitel 4, 9, 10) |
| `mc/calib.py`, `calib_out.txt` | Kalibrierung gegen Biverse und TikTok-Creator-Zahlen |
| `mc/mc_extra.py`, `mc_extra_results.json` | Portfolio mit Verbund-Risiko, Winner-Definitionen, Creative-Ökonomie |
| `mc/mc_factory.py`, `mc_factory_results.json` | Explore/Exploit-Simulation der Creative Factory |
| `mc/mc_boost.py`, `mc_boost_results.json` | Szenario bezahlte Seller-Verstärkung |
| `mc/mc_test.py`, `mc_test_results.json` | Trennschärfe des 30-Tage-Tests (Regel aus Kapitel 15.3 unter `rule_audit_15_3`) |
| `mc/mc_revision.py`, `mc_revision_results.json` | C5-Vergleich und Co-Basisfall ρ = −0,3 |
