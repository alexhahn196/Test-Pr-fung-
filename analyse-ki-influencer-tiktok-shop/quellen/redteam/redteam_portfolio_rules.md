# Red-Team: Portfolio-Regeln (Mehrere Accounts, Team/Agentur, Cross-Account-Content, Scheduling, Pilot-Limits)

Stand: 25.09.2026. Alle Primärquellen wurden am **25.09.2026 neu abgerufen** (Rohtexte in `research/redteam/portfolio/essay_*.txt`), nicht nur aus dem Vorbericht übernommen. Tags: **Verified** = wörtlich in der Primärquelle gelesen; **Claimed** = Behauptung Dritter; **Estimated** = eigene Rechnung mit Formel. Beschrieben wird ausschließlich, was **innerhalb** der TikTok-Regeln zulässig ist. Methoden zur Umgehung von Sperren, Erkennung, Geräte- oder IP-Verknüpfungen werden bewusst nicht beschrieben.

Geprüfte Behauptungen des Vorberichts (README, Kap. 1, 11, 13): C5 bis C7 sowie die implizite Annahme, dass Skalierung über mehrere Accounts nur mit „verschiedenen Personen“, einem Team und hohem Regelrisiko möglich ist.

---

## 0. Kurzfazit (Red-Team-Sicht)

1. **Die Posting-Limits sind bei den Volumina aus C6/C7 nicht der Engpass.** Ein einziger US-Account nach dem Pilotprogramm darf 30 Shoppable-Videos pro Tag posten (≈ 900/Monat), ein DE-Account nach dem Pilot 25 pro Tag (≈ 750/Monat). C6 (≈ 830 Videos/Monat) passt regelkonform in **einen** US-Account, C7 (≈ 1.650/Monat) in **zwei** US- oder **drei** DE-Accounts. In den USA darf **eine Person mit einem Ausweis bis zu 5 Creator-Accounts** verifizieren (Verified, zwei Seiten, heute erneut gelesen). Der Satz des Vorberichts „20.000 EUR … mehrere Accounts über verschiedene Personen“ ist für die Posting-Kapazität in den USA also nicht zwingend. „Wahrscheinlich ein Team“ (C7) ist eine Arbeitszeit-Annahme, **keine Regelvorgabe**.
2. **Der eigentliche regulatorische Engpass ist Originalität, nicht Menge.** Jede Plattformebene verbietet das Vervielfachen **desselben** Contents über Accounts: US „Do not repost your own content … Whether you manage one account or many, each post should offer something new“; EU „Mehrere Konten zu erstellen, um denselben E-Commerce-Inhalt zu verbreiten“ und „Koordinierte Massenveröffentlichungen über mehrere Konten hinweg“ sind ausdrücklich Spam; UK/EU-AIGC: keine „near-identical videos“. Ein Portfolio multipliziert also nicht die Videos eines Accounts, sondern braucht **pro Account eigene Videos**. Damit bleibt die Stückzahl aus C6/C7 als Zahl **eigenständiger** Videos richtig. Der Vorbericht ist hier nicht zu pessimistisch.
3. **Teams und Agenturen sind ausdrücklich vorgesehen, aber nur über offizielle Kanäle.** Die US-Creator-Terms nennen „Creator Agency Partners … who can help manage your services and collect commissions on your behalf“. Es gibt eine offizielle Agentur-Verknüpfung mit Datenfreigabe und Provisionsaufteilung. Der EU-Sicherheitsleitfaden schreibt: „hiring an agency can help scale your business“. **Aber:** US-ToS „Do not give others access to your account … without our permission“. Team-Logins ohne Passwortweitergabe gibt es nur für **Organization Accounts** von Verkäufern, nicht für persönliche Affiliate-Accounts. Die VA-Rolle „Upload-Freigaben, Kommentare“ im Vorbericht (Phase 3) ist deshalb für persönliche Accounts regelseitig **optimistischer** dargestellt, als die Texte hergeben.
4. **Der Vorbericht übersieht drei regelkonforme Skalierungswege:** (a) **verkäufergebundene Marketing-Accounts**: kein Follower-Minimum, 1 Official- plus 4 Marketing-Accounts pro Shop, Pilot-Ende schon bei 1.000 Followern und 30 Tagen (US) statt 5.000 Followern; (b) das **Content Authorization Tool** (global seit 08/2026): Reposts fremder Creator-Inhalte mit Freigabe, bis zu 5 Accounts auf Account-Ebene; (c) US-Creator-Terms 4.6: freiwillige **Cross-Market-Verteilung mit TikTok-eigenem KI-Dubbing**. Keiner dieser Wege hebt das Originalitätsgebot für eigene Accounts auf.
5. **Pessimismus des Vorberichts, der bestätigt wird:** korrelierte Sperrrisiken („associated accounts“), die Graduierung im US-Pilot erst ab **5.000 Followern pro Account**, und der Befund, dass die offizielle Content Posting API **keinen Produktlink-Parameter** hat. Shoppable Videos lassen sich damit nicht über Drittanbieter-Scheduler automatisieren; Kapitel 13.2 des Vorberichts erwähnt diese Grenze nicht und ist dort eher zu optimistisch.

---

## 1. Wie viele TikTok-Shop-Creator-Accounts darf eine Person betreiben?

### 1.1 USA

| Regel | Zitat | Quelle (abgerufen 25.09.2026) | Tag |
|---|---|---|---|
| 1 Ausweis → bis zu 5 Creator-Accounts | „How many creator accounts can I have? 1 ID can be used to verify up to 5 TikTok Shop creator accounts.“ | What You Need to Know Before Becoming a TikTok Shop Creator, https://seller-us.tiktok.com/university/essay?knowledge_id=7608640301074219&lang=en (Seitendatum 06/30/2026) | Verified |
| dito, zweite Seite | „One ID can be used to verify up to five creator accounts.“ (Fließtext und FAQ) | Creator Identity Verification, https://seller-us.tiktok.com/university/essay?knowledge_id=8182993140467499&lang=en (10/29/2025) | Verified |
| Pro Account: Follower | Affiliate: „Have a minimum of 1,000 followers“; Official/Marketing: „no minimum follower requirement“ | Creator Eligibility Policy, https://seller-us.tiktok.com/university/essay?knowledge_id=6939143037667118&lang=en (**Seitendatum heute 09/25/2026**) | Verified |
| Pro Account: Wohnsitz, Alter, ID | „Be at least 18 years old … Must be based in the United States … Must pass the Creator Identity Verification process“ | ebd. | Verified |
| Verknüpfung mit gesperrten Accounts | „Must have no prior record of having e-commerce permissions revoked by TikTok Shop; Must not be associated with accounts that have had e-commerce permissions revoked by TikTok Shop“ | ebd. | Verified |
| Login-Daten | „Must not share the same or similar login information with TikTok Shop accounts with high violations.“ | 7608640301074219 (06/30/2026) | Verified |
| 1 Telefonnummer/E-Mail = 1 Account | „Each phone number, email address, and social media account can only be linked to one TikTok account.“ | Support „Creating an account“ (Kopie vom 24.09.2026 im Vorbericht) | Verified (Vorbericht) |
| Plattformweit mehrere Accounts erlaubt | „You can have multiple accounts—for example, for fan content or creative expression—but not to deceive others or break the rules.“ | Community Guidelines, Integrity & Authenticity (wirksam 24.09.2026) | Verified |

**Einordnung:** Eine US-Person darf regelkonform **bis zu 5** Affiliate-Creator-Accounts betreiben. Jeder Account braucht eigene Kontaktdaten und eigene 1.000 Follower und durchläuft ein eigenes Pilotprogramm (Abschnitt 5). Ein sechster Account braucht eine **zweite, real existierende US-Person** mit eigener Identitätsprüfung.

### 1.2 EU / Deutschland

| Regel | Zitat | Quelle | Tag |
|---|---|---|---|
| Zugang pro Account | „Access their TikTok account from the same Member State where it was registered; … Maintain the required 500 followers in the Member State for which they are applying; Be at least 18 years old; … Not have previously had Creator E-commerce Permissions that were revoked by TikTok Shop. This includes previous accounts of the Creator.“ | TikTok Shop EU Creator E-commerce Permissions Eligibility Policy, https://seller-ie.tiktok.com/university/essay?knowledge_id=747894062696212&lang=en-GB (03/09/2026, EU-13 inkl. DE) | Verified |
| KYC pro Auszahlung | Ausweis „von dem Land ausgestellt …, das du für die Registrierung deines TikTok Shop-Kontos verwendet hast“; Adressnachweis im Registrierungsland; bis zu 6 Versuche | https://seller-de.tiktok.com/university/essay?knowledge_id=740763580188436&lang=de-DE | Verified |
| **Höchstzahl Accounts pro Person/Ausweis** | Keine Zahl in EU-Eligibility, KYC-Leitfaden, Pilot-Seite, Binding-Artikel oder Sicherheitsleitfaden | alle oben genannten EU-Seiten | **Nicht in Primärquelle auffindbar** |
| Widerspruch Follower-Schwelle | Binding-Artikel: Affiliate „Maintain at least 1,000 followers in the EU … Have posted a video on TikTok in the last 28 days“ | Official Account Creators and Marketing Account Creator Binding, https://seller-ie.tiktok.com/university/essay?knowledge_id=7798861624510230&lang=en-GB (02/07/2026) | Verified. Die neuere Policy vom 03.09.2026 nennt 500 Follower; vermutlich ist der Binding-Artikel veraltet (Einordnung, nicht belegt). |

**Einordnung:** In der EU ist **keine Obergrenze** pro Person veröffentlicht. Das heißt nicht „unbegrenzt“: Die EU-Inhaltsrichtlinie verbietet Mehrfach-Accounts zur Verbreitung **desselben** Contents und koordinierte Massenveröffentlichung (Abschnitt 3). Wie TikTok „koordiniert“ auslegt, ist nicht beziffert.

### 1.3 Was passiert mit den übrigen Accounts, wenn einer gesperrt wird?

| Ebene | Zitat | Quelle | Tag |
|---|---|---|---|
| Plattform (schwer/Umgehung) | „If someone seriously breaks the rules or tries to dodge enforcement, we may ban all of their accounts, including associated accounts.“ | Community Guidelines (wirksam 24.09.2026) | Verified |
| Plattform (Täuschung) | „If we find deceptive account behavior, we may: Ban your account / Ban additional or new accounts you create / Restrict your account …“ | ebd. | Verified |
| Plattform (Umgehung) | „Spreading violative content across multiple accounts“; „Using another account to avoid restrictions“ | ebd. | Verified |
| US-Shop | Zulassung setzt voraus: „Must not be associated with accounts that have had e-commerce permissions revoked“; Enforcement-Auslöser „Using multiple accounts to avoid enforcement“ | Creator Eligibility Policy (09/25/2026); Creator Enforcement Policy, https://seller-us.tiktok.com/university/essay?knowledge_id=6837869503317761&lang=en (**Seitendatum 09/25/2026**) | Verified |
| US-Shop, Agentur | „If a creator violates the Creator Terms of Use, TikTok Shop may freeze the commissions tied to their account. If the creator is associated with an agency, that agency's commission split may also be blocked during the freeze.“ | Creator Enforcement Policy (09/25/2026) | Verified |
| US-Verkäufer | Bekommt ein gebundener Official- oder Marketing-Account einen EC-Bann, „TikTok Shop may conduct an additional review of the linked seller“. Bei 1 EC-Bann in 180 Tagen gibt es nur neue Bindungen, wenn weniger als 5 in 180 Tagen bestehen; bei 2–3 Banns werden neue Bindungen pausiert; ab 4 Banns „may permanently lose the ability to add new marketing creator bindings“. | Creator Bind Eligibility and Requirements, https://seller-us.tiktok.com/university/essay?knowledge_id=3753520906340139&lang=en (09/02/2026) | Verified |
| EU-Shop | Zulassung und **Erhalt**: kein früherer Entzug, „This includes previous accounts of the Creator.“ | EU Eligibility (03/09/2026) | Verified. Ob ein **gleichzeitig** betriebener Account eines Portfolios erfasst ist, bleibt offen: Der Text sagt „previous accounts“. |
| UK-Shop | „Fraudulent Account Activity … Abnormal login activity, e.g. frequent logins across multiple accounts from the same device, network, or other shared resources, which may indicate coordinated control. / Association with banned or penalised accounts“ | Creator Fraud, Abuse, and Misconduct, https://seller-uk.tiktok.com/university/essay?knowledge_id=651807580964640 (04/17/2026, UK) | Verified (UK; eine EU- oder US-Entsprechung wurde nicht gefunden) |
| CHR pro Account | CHR ist ein Account-Score („snapshot of the overall health of your creator account“). Eine Übertragung von Punktabzügen auf andere Accounts derselben Person | – | Nicht in Primärquelle auffindbar |

**Einordnung:** Gewöhnliche Content-Verstöße wie CHR-Abzug oder Video-Entfernung treffen den einzelnen Account. Ein Portfolio streut dieses Risiko. **Schwere** Verstöße, Umgehung und E-Commerce-Entzug können dagegen auf „associated accounts“ durchschlagen. Das Sperrrisiko ist also bei Bagatellen diversifiziert und bei schweren Fällen korreliert. Die UK-Regel stuft häufige Logins mehrerer Accounts vom selben Gerät als **Indiz für koordinierte Kontrolle** ein. Ein Einzelbetreiber mit mehreren eigenen Accounts trägt dadurch ein Plattformrisiko, auch wenn er sonst regelkonform arbeitet. Dieses Risiko lässt sich nur über klare, echte Kontoinhaberschaft senken, nicht über Verschleierung.

---

## 2. Dürfen Team, VA oder Agentur Accounts für den Kontoinhaber führen?

| Regel | Zitat | Quelle | Tag |
|---|---|---|---|
| US-ToS: kein fremder Zugriff ohne Erlaubnis | „It is important that you take reasonable steps to keep your account password confidential and that you do not disclose it to any third party. … Do not give others access to your account, or transfer your account to anyone else, without our permission.“ | U.S. Terms of Service, „Last updated: July 15, 2026“ (Kopie vom 24.09.2026, `research/tos_us.txt`, dekodiert) | Verified |
| EEA/UK-ToS | Nutzungsrecht „is only for you; cannot be given to anyone else by you“; Passwort „do not disclose it to any third party“ | EEA, UK and Switzerland Terms of Service, „Last updated: July 2026“ (`research/tos_eea.txt`) | Verified |
| US-Creator-Terms: Agenturen vorgesehen | „get connected with third parties, including creator agency partners (‚Creator Agency Partners') who can help manage your services and collect commissions on your behalf.“ 5.3: „if you choose to work with Affiliate Partners or Creator Agency Partners … You authorize us to disclose your data to such Affiliate Partners or Creator Agency Partners“ | TikTok Shop Creator Terms of Use, https://seller-us.tiktok.com/university/essay?knowledge_id=6314510387906350&lang=en (Last updated 28.08.2026) | Verified |
| US-Creator-Terms: Haftung für Mitnutzer | Freistellung für Schäden „arising out of a breach by you or any user of your account“ | ebd. | Verified. Die Terms setzen also voraus, dass es weitere Nutzer eines Accounts geben kann; der Creator haftet für sie. |
| US: offizielle Agentur-Verknüpfung | „link with agencies and give them access to your data … When linking with an agency, you are also setting a commission split“; Annahme und Aufhebung im Partnerships-Bereich | [Creators] Linking with Agencies, Data Authorization, & Commission Sharing, https://seller-us.tiktok.com/university/essay?knowledge_id=4011666679007022&lang=en (09/26/2024) | Verified. Freigegeben werden **Daten und Provisionsanteil**, keine Posting-Rechte. |
| EU: Agenturen, aber keine Passwortweitergabe | „While hiring an agency can help scale your business, it introduces significant security risks. … Never share your primary owner credentials. Use official ‚User Management' settings to limit permissions.“ | A Creator's Guide to Securing Your TikTok Shop Account, https://seller-ie.tiktok.com/university/essay?knowledge_id=5509564888303361&lang=en-GB (23/06/2026, EU-13) | Verified |
| US: Team-Zugang ohne Passwort nur für Organization Accounts | „you no longer need to share your password with team members. This functionality is available only on Organization Accounts.“ / „You will NOT have access to personal accounts associated with the shop.“ | How to Manage Team Access to Organization Account on TikTok Shop, https://seller-us.tiktok.com/university/essay?knowledge_id=2500395617929015&lang=en (01/07/2026) | Verified |
| Business Center: Kommentare/DMs | „Manage account“-Recht umfasst „replying to comments, sending direct messages, and managing profile details“ | About managing TikTok accounts in Business Center, https://ads.tiktok.com/help/article/about-managing-tiktok-accounts-in-business-center?lang=en (Last updated September 2026) | Verified (Rechtetext). Ob persönliche Affiliate-Creator-Accounts verknüpft werden können und ob es ein Posting-Recht gibt: **nicht verifiziert** (die Suchzusammenfassung nennt „Publish and manage new videos“, auf der Seite nicht gefunden: Claimed). |
| UK: Agentur-Provisionen | „TikTok Shop can now freeze agency commissions from eligible unsettled orders linked to creators subject to enforcement of inorganic growth tactics, such as account purchasing or posting unoriginal/irrelevant content, for up to 90 days“ | Creator Policy Pulse (August 2026), https://seller-uk.tiktok.com/university/essay?knowledge_id=289257470379798 (09/01/2026, UK) | Verified |
| TikTok One for Partners | „designed for all creator and creative agencies“; Ziel: „monetize creators managed on TikTok“ | https://ads.tiktok.com/help/article/about-tiktok-one-for-partners (Last updated March 2026) | Verified (nur Zweckbeschreibung, keine Account-Rechte) |
| CAP-Zulassungskriterien (US/UK) | Portal-Seiten laden nur per JavaScript (partner.tiktokshop.com, seller.tiktok.com/partner/creator-agency) | – | Nicht öffentlich verifizierbar |

**Regelkonforme Team-Architektur (nur was die Texte decken):**
- Team oder VA **produzieren außerhalb der Plattform**: Skripte, Schnitt, KI-Assets, Recherche, Datenauswertung. Das ist unproblematisch, weil es keinen Account-Zugriff braucht.
- **Posting und Kommentare** eines **persönlichen** Affiliate-Accounts macht der Kontoinhaber selbst oder ein Dienst über offiziell freigegebene Wege: audited Content-Posting-API-Clients, bei Business-Center-fähigen Accounts die dortigen Rollen. Passwortweitergabe an eine VA widerspricht den US-ToS, außer TikTok hat es erlaubt, und den EU-Empfehlungen.
- **Agenturmodell:** Eine Agentur betreut **mehrere echte Creator** (jede Person verifiziert sich selbst) und erhält per offizieller Verknüpfung einen Provisionsanteil. Das ist der sanktionierte Weg zu 10+ Accounts. Er entspricht dem „Team“-Szenario in C7, ist aber ein Agentur- und kein Solo-Modell.
- **Verkäufermodell:** Organization Accounts mit Sub-Account-Rollen „Affiliate Manager“ oder „Main Administrator“ (nur Verkäufer-Entität).

**Folge für den Vorbericht:** Phase 3 („VA … für Sichtprüfung, Upload-Freigaben, Kommentare“) ist nur dann regelkonform, wenn die VA nicht mit dem Passwort des Kontoinhabers arbeitet. Das schränkt die Delegierbarkeit **stärker** ein, als der Vorbericht annimmt. Die Aussage in C7, 20.000 EUR brauche „wahrscheinlich ein Team“, ist regelseitig **umsetzbar**, weil Agenturen offiziell vorgesehen sind.

---

## 3. Wiederholter oder doppelter Content über mehrere Accounts

| Regel | Zitat | Quelle | Tag |
|---|---|---|---|
| US: eigene Reposts verboten, auch bei mehreren Accounts | „Do not repost your own content. Once you have posted a TikTok video or LIVE recording, do not upload the same content again.“ / „Refresh your scripts. Develop a new original script for each video“ / „Whether you manage one account or many, each post should offer something new for your audience to discover.“ | Best Practices for Promotional Content, https://seller-us.tiktok.com/university/essay?knowledge_id=5769635937191681&lang=en (06/24/2026) | Verified |
| US: Verschleierung | „Do not manipulate your videos using edits, effects, or filters to disguise copied or repetitive content.“; AB-Frames „strictly prohibited“ | ebd.; 7608640301074219 | Verified |
| US: Massenproduktion → Extended Pilot | „Extended Pilot Creators are those who frequently publish and mass-produce low-cost content …“ → „up to 3 shoppable product videos per week“ | Affiliate Creator Pilot Program Introduction, https://seller-us.tiktok.com/university/essay?knowledge_id=5526872163927850&lang=en (05/13/2026); Creator Eligibility Policy (09/25/2026) | Verified |
| **EU: Mehrfach-Accounts mit gleichem Content = Spam** | Unter „4.9.4 Irreführender Traffic, Spam und Betrug“: „Mehrere Konten zu erstellen, um denselben E-Commerce-Inhalt zu verbreiten; … Das Hochladen großer Mengen nahezu identischer Videos mit minimalen kreativen Unterschieden; … Verwendung von standardisierten Erzählformen, z. B. Text-zu-Sprache oder einfache Texteinblendungen ohne sinnvollen kreativen Beitrag …; Koordinierte Massenveröffentlichungen über mehrere Konten hinweg, die Spam-Verhalten nachahmen“ | TikTok Shop-EU-Inhaltsrichtlinie, https://seller-de.tiktok.com/university/essay?knowledge_id=7404160497927968&lang=de-DE (21.09.2026, EU-13) | Verified |
| UK/EU-AIGC | „Creators must not use AI to mass-produce: Multiple identical or near-identical videos … Uploading multiple promotional videos that reuse the same script, visuals, or structure with minimal changes“; Sanktionsbeispiel „restricting an account to 15 videos within a 30-day period“ | AIGC, https://seller-uk.tiktok.com/university/essay?knowledge_id=5234615598237462 (08/28/2026, UK; laut Vorbericht wortgleiche EU-Fassung) | Verified |
| Plattform | Spam: „Using automation to run many accounts or send repetitive content“; Umgehung: „Spreading violative content across multiple accounts“ | Community Guidelines (24.09.2026) | Verified |
| **Neu: Content Authorization Tool (global)** | „The new Content Authorization Tool was launched globally, allowing creators to request authorization to use content from another account or grant authorization for others to use their content“; „A creator can authorize up to 5 other creator accounts at the account level.“; Freigabe max. „1 year“; „Authorization cannot be sub-licensed.“ | Creator Policy Pulse Aug 2026 (UK) und Content Authorization Tool Feature Guide, https://seller-uk.tiktok.com/university/essay?knowledge_id=1920527359182614 (08/20/2026) | Verified (UK-Seiten). Eine US-Fassung unter derselben ID gibt es nicht (404); „global“ steht nur im UK-Pulse. |

**Einordnung für Portfolios:**
- **Verboten:** dasselbe Video oder nahezu identische Varianten (gleiches Skript, gleiche Bilder, gleiche Struktur) auf mehreren **eigenen** Accounts; koordinierte Massenveröffentlichung; in der EU TTS oder Texteinblendung **ohne** kreativen Beitrag.
- **Erlaubt:** unterschiedliche Accounts mit eigenständigen Skripten und Visuals, auch für dasselbe Produkt. Ein neues Skript pro Video wird ausdrücklich verlangt, KI-Skripte sind erlaubt (US-AIGC-Policy, Vorbericht).
- **Graubereich mit offizieller Grundlage:** Das Content Authorization Tool erlaubt Reposts **fremder** Creator-Inhalte mit Einwilligung, etwa wenn ein UGC-Creator Material an Affiliates lizenziert. Es löst nur den Verstoß „unoriginal/pirated“. Das EU-Verbot „Mehrere Konten … denselben E-Commerce-Inhalt“ und das US-Verbot „Do not repost your own content“ bleiben bestehen. Der Vorbericht behandelt das Repost-Verbot als absolut; seit 08/2026 gilt das zwischen **verschiedenen** Creatorn nicht mehr uneingeschränkt.

---

## 4. Scheduling-Tools und Content Posting API für Multi-Account-Betreiber

| Regel | Zitat | Quelle | Tag |
|---|---|---|---|
| Unauditierte API | „Unaudited API Clients can allow up to 5 users to post in a 24 hour window“; nur „SELF_ONLY“ | Content Sharing Guidelines, developers.tiktok.com (Last updated August 4, 2026; Kopie `research/dev_content-sharing-guidelines.txt`) | Verified |
| Posting-Cap über API | „There is a limit on the number of posts that can be made to a creator account in a 24-hour window via Direct Post API. The upper limit may vary among creators (typically around 15 posts per day/ creator account) and is shared across all API Clients using Direct Post.“ | ebd. | Verified |
| Kein Eigenbau-Uploader | „API Clients must not be limited to test applications and should be intended for a wide audience, not limited to internal groups/private use. Not acceptable: A utility tool to help upload contents to the account(s) you or your team manages. ❌“ | ebd. | Verified. **Auslegung:** Ein Portfolio-Betreiber bekommt für ein eigenes internes Upload-Tool kein Audit. Regelkonform bleiben auditierte Drittanbieter-Tools für eine breite Nutzerschaft sowie TikTok Studio. |
| **Kein Produktlink über die API** | Parameter von `/v2/post/publish/video/init/`: privacy_level, title, disable_duet/stitch/comment, video_cover_timestamp_ms, brand_content_toggle, brand_organic_toggle, is_aigc, source_info. Einen Parameter für TikTok-Shop-Produkte oder Anchors gibt es nicht. | Direct Post API Reference (Last updated August 24, 2026; `research/dev_direct.txt`) | Verified (Fehlen des Parameters). Folge: **Shoppable Videos lassen sich über die öffentliche Posting-API nicht erzeugen.** Ob eine TikTok-Shop-Partner-API das kann, ist nicht öffentlich verifizierbar. |
| KI-Label und Werbekennzeichnung per API | `is_aigc` („Creator labeled as AI-generated“), `brand_content_toggle`, `brand_organic_toggle` | ebd. | Verified |
| In-App-/Studio-Scheduling zählt sofort | „Scheduled shoppable videos count towards your limit the moment they are scheduled, not at the time they are scheduled to post.“ | Creator Enforcement Policy (09/25/2026); Pilot-Seiten US/DE | Verified |
| Desktop-Scheduler | „Only a ‚Business Account' or over with a 10,000 followers or more can access desktop scheduling.“ / „maximum of 10 days in advance“ | Support-FAQ „Schedule video“ (Vorbericht, undatiert, vermutlich älter) | Verified (Vorbericht) |
| Automatisierung vieler Accounts | „Using automation to run many accounts or send repetitive content“ = Spam | Community Guidelines | Verified |

**Folge für den Vorbericht:** Kapitel 13.2 stuft Drittanbieter-Scheduler (Postiz, Blotato usw.) als „im Rahmen der TikTok-Regeln“ ein. Für **nicht-shoppable** Posts stimmt das, begrenzt auf ca. 15 Posts pro Tag und Account. Für **Shop-Videos** mit Produktlink führt die öffentliche API nicht weiter. Die Automatisierungskette ist beim Posting also **enger**, als der Vorbericht nahelegt. Hier wirkt der Red-Team-Befund zugunsten des Vorberichts: Der Posting-Aufwand pro Shop-Video bleibt manuell (App oder Studio).

---

## 5. Limits für neue Accounts (Pilotprogramme 2026)

### 5.1 USA

| Punkt | Wert / Zitat | Quelle | Tag |
|---|---|---|---|
| Affiliate-Pilot | unter 5.000 Followern ≥ 30 Tage: „A posting limit of up to 3 shoppable product videos per day and 3 shoppable LIVEs per week“, nur Produkte mit SPS ≥ 95 %, keine Kampagnen | Creator Eligibility Policy (09/25/2026) | Verified |
| Extended Pilot | „up to 3 shoppable product videos per week“, 1 LIVE pro Woche; keine Graduierung, solange der Tag aktiv ist | ebd. | Verified |
| Graduierung | „Reach at least 5,000 followers; and Remain in the program for at least 30 days“ | ebd. | Verified |
| Early Unlock | Quiz, CHR ≥ 176 und eine Aufgabe (6 Videos ≥ 8 s / 1 LIVE ≥ 5 min / 10 Bestellungen) → „restrictions related to TikTok Shop Product Marketplace access, shoppable LIVE features, and campaign participation lifted early“ | ebd. | Verified. Dass dabei auch das **Posting-Limit** fällt, steht nicht im Text; laut 7608640301074219 gibt es „unlimited shoppable videos“ erst nach Graduierung (5.000 Follower). |
| **Widerspruch** | Dieselbe Seite 7608640301074219 (06/30/2026), FAQ: „Creators with fewer than 5,000 followers can post up to 5 shoppable videos per week.“ Dazu: „quota refreshes every Monday at midnight PST“ | 7608640301074219 | Verified. 3/Tag (≈ 21/Woche) und 5/Woche widersprechen sich; die Policy (09/25/2026) nennt 3/Tag. |
| Official/Marketing (verkäufergebunden) | Early-Stage-Pilot: „up to 3 e-commerce videos per day“; Graduierung: 30 Tage gebunden, **1.000 Follower**, Risk-Checks | Creator Eligibility Policy; Creator Bind Eligibility (09/02/2026) | Verified |
| Nach dem Pilot | „Up to 30 shoppable short videos per day • Up to 60 shoppable photo posts per day“ (seit 11.05.2026) | Creator Eligibility Policy | Verified |
| Drosselung nach CHR-Abzügen | „limited to posting up to 3 pieces of content per day for 7 days“ | CHR Overview (Vorbericht) | Verified (Vorbericht) |

### 5.2 EU / Deutschland

| Punkt | Wert / Zitat | Quelle | Tag |
|---|---|---|---|
| Geltungsbereich | Pilot „applicable to Ireland, Spain, Italy, France and Germany only“ | EU Eligibility (03/09/2026) | Verified |
| Pilot | 30 Tage, „maximum of 21 shoppable videos per week“ / DE: „nur bis zu 3 Shopping-Videos pro Tag (21 Shopping-Videos pro Woche)“ | ebd.; Pilotprogramm für Creator*innen, https://seller-de.tiktok.com/university/essay?knowledge_id=5604780513855233&lang=de-DE (25.06.2026) | Verified |
| Abschluss | eine Aufgabe (1 LIVE ≥ 5 min ODER 6 Videos ≥ 8 s, „selbst wenn es auf ‚Nur ich' eingestellt ist“, ODER 10 Bestellungen) und CHR „mehr als 176“ (EN: „not have fewer than 176“); **keine Follower-Hürde über die 500 hinaus** | ebd. | Verified |
| Verlängerung | „Diese Probezeit kann unbegrenzt verlängert werden, bis alle Anforderungen erfüllt sind.“ | DE-Pilotseite | Verified |
| **Nach dem Pilot (neu gegenüber Vorbericht)** | „können sie maximal 50 Shopping-Fotos und 25 Shopping-Videos pro Tag veröffentlichen“ | DE-Pilotseite (25.06.2026) | Verified. Der Vorbericht verwendet für die Kapazität nur US-Werte (30/Tag). |
| Altfälle | „verified … prior to June 30, 2026 will not be retroactively enrolled“ | EU Eligibility | Verified |
| UK | kein Pilot in der EU-Liste; AIGC-Sanktionsbeispiel „15 videos within a 30-day period“ | UK AIGC | Verified |

**Einordnung:** In **DE** ist der Pilot für einen neuen Account nach 30 Tagen **ohne Follower-Wachstum** zu schaffen (500 Follower plus eine Aufgabe plus CHR). In den **USA** braucht jeder neue Affiliate-Account 5.000 Follower bis zur vollen Posting-Kapazität. Ein US-Portfolio wächst deshalb langsamer an, als Phase 2 des Vorberichts suggeriert („2 Accounts nach Pilotprogramm (je bis zu 30 Videos/Tag erlaubt)“). Für den DE-Plan des Vorberichts ist die Hürde **niedriger**, als die Formulierung „jeder Account braucht 500 Follower und durchläuft das 30-Tage-Pilotprogramm“ vermuten lässt.

---

## 6. Portfolio-Tabelle: Was ein Portfolio aus 1 / 3 / 5 / 10 Accounts innerhalb der Regeln darf und nicht darf

Kapazität = regelmäßige Obergrenze für Shoppable Videos nach dem Pilot (Estimated: Accounts × Tageslimit × 30). Das ist **keine** Prognose.

| Accounts | USA (eine Person, US-Wohnsitz) | EU/DE (eine Person, DE-Wohnsitz) | Darf (beide Märkte) | Darf nicht (beide Märkte) | Kapazitätsdecke/Monat (Estimated) |
|---|---|---|---|---|---|
| **1** | erlaubt; 1.000 Follower, Pilot bis 5.000 Follower (3/Tag), danach 30 Videos und 60 Foto-Posts pro Tag | erlaubt; 500 DE-Follower, Zugriff aus DE, KYC mit DE-Ausweis und DE-Adresse; Pilot 21/Woche, danach 25 Videos und 50 Fotos pro Tag | KI-Skripte, KI-Voice, gelabelte KI-B-Roll; TikTok-Studio-Scheduling; Agentur-Verknüpfung mit Provisionssplit (US) | Reposts eigener Videos; near-identical Serien; AB-Frames; Passwort an Dritte (US-ToS) | US 900; DE 750 |
| **3** | erlaubt (≤ 5 pro Ausweis); jeder Account eigene Telefonnummer/E-Mail, eigener Pilot, eigener CHR | **keine veröffentlichte Obergrenze**; jeder Account eigene 500 Follower, eigener Pilot, eigenes KYC | unterschiedliche Nischen oder Skripte pro Account; dasselbe Produkt mit eigenständigem Content | denselben Content auf mehreren Accounts (EU: ausdrücklich Spam); Automatisierung „to run many accounts“; koordinierte Massenveröffentlichung | US 2.700; DE 2.250 |
| **5** | erlaubt, **Maximum pro Ausweis** | keine veröffentlichte Obergrenze; mit wachsender Zahl steigt das Risiko, als „koordiniert“ eingestuft zu werden (unbeziffert) | wie oben; offizielle Agentur für Produktion und Daten | wie oben; zusätzlich: ein EC-Entzug bei einem Account gefährdet die Zulassung der „associated accounts“ | US 4.500; DE 3.750 |
| **10** | **nicht mit einer Person** als Affiliate (Ausweis-Limit 5). Regelkonform nur als (a) Agentur mit mehreren echten, selbst verifizierten US-Creatorn und offizieller Provisionsaufteilung, oder (b) Verkäufer mit 1 Official- und 4 Marketing-Accounts pro graduiertem Shop | formal keine Zahl, praktisch nahe an „Koordinierte Massenveröffentlichungen über mehrere Konten hinweg“; regelkonform eher als Agentur mit echten Creatorn | Agenturmodell; Verkäufermodell | Accounts kaufen („account purchasing“ ist UK-Enforcement-Ziel); Identitäten leihen (UK: „Identity theft … using … someone else's … identification documents“); fremde Accounts per Passwort führen | US (2 Personen) 9.000; DE 7.500 (theoretisch) |
| **Verkäufer** (Zusatz) | kein Follower-Minimum für Official/Marketing; 1 + 4 Bindungen pro graduiertem Shop, bis zu 10 Marketing-Bindungen in 180 Tagen ohne EC-Banns | EU identisch (1 + 4) | Marken-Portfolio ohne 1.000/5.000-Follower-Hürde; Marketing-Accounts dürfen den Shop sofort bewerben | Marktplatz-Produkte anderer Verkäufer erst ab 5.000 Followern (US) | 5 × 30 × 30 = 4.500 (US) |

Kapazitätsdecke × Stückökonomie des Vorberichts (Estimated): Modell C5 = 4.000 Views × 30 USD GMV/1.000 Views = 120 USD GMV pro Video; × 15 % Provision × 0,9 (Retouren) − 3 USD Tools = **13,20 USD pro Video**.
- 1 US-Account am Limit: 900 × 13,20 = **11.880 USD/Monat** (≈ C6-Niveau)
- 1 DE-Account am Limit: 750 × 13,20 = 9.900 USD
- 3 US-Accounts: 2.700 × 13,20 = 35.640 USD
- 5 US-Accounts: 4.500 × 13,20 = 59.400 USD

Das sind **Regel-Obergrenzen mal Durchschnitt**, keine realistischen Werte: Views pro Video sinken bei Volumen, und jedes Video muss eigenständig sein. Der Punkt ist nur: **Die Regeln verbieten C6/C7-Volumen für eine Einzelperson mit 1 bis 3 Accounts nicht.**

---

## 7. Befunde (Findings)

**P1 – Posting-Limits binden bei C6/C7 nicht (widerspricht C7 teilweise, C6 formal).** US 30/Tag und DE 25/Tag pro Account, US 5 Accounts pro Ausweis. 830 Videos/Monat passen in einen US-Account (900), 1.650 in zwei US- oder drei DE-Accounts. „Wahrscheinlich ein Team“ ist eine Kapazitätsannahme, keine Regel. Stärke: **medium**, weil Regelkapazität nicht dasselbe ist wie tatsächliche Produktions- und Reichweitenkapazität.

**P2 – Originalitätspflicht pro Video und Account (bestätigt C6/C7 als Zahl eigenständiger Videos).** US „each post should offer something new“ (auch bei vielen Accounts), EU „Mehrere Konten … denselben E-Commerce-Inhalt“ als Spam. Ein Portfolio vervielfacht die Reichweite nicht per Copy-Paste. Stärke: **strong**, stützt den Vorbericht.

**P3 – Offizielle Team- und Agenturstrukturen (widerspricht der Lesart „Team = Regelrisiko“, schränkt die VA-Rolle ein).** Creator Agency Partners mit Datenfreigabe und Provisionssplit (US), der EU-Leitfaden erkennt Agenturen an; Passwortweitergabe ist nach US-ToS ohne Erlaubnis verboten; Team-Login nur für Organization Accounts. Stärke: **strong**.

**P4 – Verkäufergebundene Marketing-Accounts als übersehener Portfolio-Weg (widerspricht dem impliziten Modell des Vorberichts, relevant für C1/C2).** Kein Follower-Minimum, 1 + 4 Bindungen pro Shop, Pilot-Ende bei 1.000 Followern (US). Marken können damit regelkonform 5 Accounts gleichzeitig betreiben und bis zu 10 Marketing-Bindungen in 180 Tagen eingehen, solange keine EC-Banns vorliegen. Dass „kurzlebige Supplement-Netzwerke“ (C2) oft solche verkäufergebundenen Accounts sind, ist eine **Hypothese**, nicht belegt. Stärke: **medium**.

**P5 – Content Authorization Tool (08/2026) weicht das absolute Repost-Verbot auf.** Reposts zwischen verschiedenen Creatorn mit Freigabe, bis zu 5 Accounts, max. 1 Jahr. Für eigene Portfolio-Accounts bleibt das EU-Verbot bestehen. Stärke: **weak/medium** (nur UK-Doku, US unbestätigt).

**P6 – Die API-Grenze macht die Posting-Automatisierung für Shop-Videos unmöglich (Korrektur am Vorbericht in Richtung „weniger automatisierbar“).** Die Direct Post API hat keinen Produktlink-Parameter; der API-Cap liegt bei ca. 15 Posts pro Tag und Account; Eigenbau-Upload-Tools sind nicht auditierbar. Stärke: **strong**.

**P7 – Korreliertes Bann-Risiko im Portfolio (stützt die Vorsicht des Vorberichts).** „associated accounts“ (CG), „Must not be associated with accounts that have had e-commerce permissions revoked“ (US), „previous accounts of the Creator“ (EU), UK-Fraud-Indiz „frequent logins across multiple accounts from the same device“. Stärke: **strong**.

**P8 – DE-Pilot leichter und DE-Tageslimit 25 statt 30 (Präzisierung).** Die DE-Graduierung braucht kein Follower-Wachstum über 500 hinaus, danach 25 Videos und 50 Fotos pro Tag. Stärke: **medium** (verbessert den Anlauf im DE-Plan des Vorberichts, senkt die DE-Tageshöchstmenge).

**P9 – Cross-Market-Distribution per KI-Dubbing (US-Creator-Terms 4.6).** „You may choose to make your Creator Content available to TikTok users in other markets … may translate and dub its audio … A dubbed video may use a synthetic voice“. Ob Shop-Links in fremden Märkten funktionieren, steht nicht im Text. Stärke: **weak** (Reichweite, nicht belegte Provision).

---

## 8. Selbstverifikation der drei stärksten Gegenbefunde

### Verifikation P1 (Posting-Limits binden nicht)
- **Quelle erneut geöffnet:** Creator Eligibility Policy (Seitendatum **09/25/2026**, also heute aktualisiert) enthält weiterhin „Up to 30 shoppable short videos per day • Up to 60 shoppable photo posts per day“. Identity Verification (10/29/2025) und die FAQ in 7608640301074219 (06/30/2026) nennen beide 5 Accounts pro Ausweis. Die DE-Pilotseite (25.06.2026) nennt „maximal … 25 Shopping-Videos pro Tag“.
- **Arithmetik neu gerechnet:** 30 × 30 = 900 ≥ 830 (C6). 1.650 / 30 Tage = 55 pro Tag → 2 US-Accounts (60/Tag) oder 3 DE-Accounts (75/Tag). Richtig.
- **Metrik:** Regel (Anzahl erlaubter Posts). Keine GMV-, Provisions- oder Gewinnaussage.
- **Einschränkungen:** (1) Die volle Kapazität gibt es in den USA erst ab 5.000 Followern pro Account; im Pilot sind es 3 pro Tag (FAQ widersprüchlich: 5 pro Woche). (2) Die Originalitätsregeln (P2) verlangen 830 bzw. 1.650 **eigenständige** Videos. (3) CHR-Drosselungen können auf 3 pro Tag fallen. (4) Der Vorbericht selbst setzt 30/Tag (US) an; er hat nie behauptet, Limits seien der Engpass. Sein „Team“-Argument ist ein Arbeitsaufwand-Argument.
- **Verdict: PARTIALLY.** Die Regeln erlauben einer Person C6/C7-Volumen mit 1 bis 3 Accounts (CONFIRMED als Regelbefund). Als Widerlegung von C7 („probably a team“) taugt das aber nur eingeschränkt, weil C7 den Arbeitsaufwand für eigenständige Videos meint und nicht die Regel.

### Verifikation P3 (Team/Agentur regelkonform, VA-Login nicht)
- **Quellen erneut geöffnet:** Creator Terms (Last updated 28.08.2026): „Creator Agency Partners … who can help manage your services and collect commissions on your behalf“, wörtlich vorhanden. Agentur-Artikel 4011666679007022 (09/26/2024): Datenfreigabe und „commission split“, kein Posting-Recht erwähnt. US-ToS (July 15, 2026): „Do not give others access to your account, or transfer your account to anyone else, without our permission.“, wörtlich vorhanden. EU-Sicherheitsleitfaden (23/06/2026): „hiring an agency can help scale your business … Never share your primary owner credentials. Use official ‚User Management' settings“. Organization-Account-Artikel (01/07/2026): „available only on Organization Accounts“, „You will NOT have access to personal accounts“.
- **Gegenprüfung:** Ein offizielles „User Management“ für **persönliche** Creator-Accounts habe ich in den Seller-University-Texten nicht gefunden. Der EU-Leitfaden verweist darauf, ohne es zu verlinken. Unklar bleibt also, **welches** Werkzeug für persönliche Affiliate-Accounts gemeint ist. Die Business-Center-Rolle „Manage account“ (Kommentare, DMs) ist Verified, die Kompatibilität mit Affiliate-Accounts nicht.
- **Verdict: CONFIRMED** für „Agenturen und Teams sind offiziell vorgesehen, Passwortweitergabe nicht“. **PARTIALLY** für die Frage, wie eine VA einen persönlichen Affiliate-Account regelkonform bedienen kann: Das ist nicht öffentlich verifizierbar.

### Verifikation P4 (Marketing-Accounts ohne Follower-Minimum)
- **Quellen erneut geöffnet:** Creator Bind Eligibility (US, 09/02/2026): „There is no minimum follower requirement to bind as a Marketing Account“, „Graduated shops can bind 1 official and 4 marketing creators“, Early-Stage-Pilot „up to 3 e-commerce videos per day“ bis „Reach 1,000+ followers“ und 30 Tage, „Shops without any EC bans … may bind up to 10 marketing creators within a 180-day period“. Die EU-Fassung (02/07/2026) nennt dieselben Werte (1 + 4, 10 Einladungen in 180 Tagen).
- **Gegenprüfung:** Marketing-Accounts bewerben den **gebundenen Shop**. Für Produkte **anderer** Verkäufer braucht es 5.000 Follower (US, 7608640301074219). Für einen reinen Affiliate-Betreiber ohne eigenen Shop oder Verkäuferpartnerschaft ist das also kein Weg. Die Kategorie (A–H) hängt am Content, nicht an der Regel; hier gilt „portfolio/policy“. Ein konkreter Handle wurde nicht geprüft, weil es um einen reinen Regelbefund geht.
- **Verdict: PARTIALLY.** Die Regel ist bestätigt. Für das Einzelperson-Affiliate-Modell des Vorberichts ist sie nur relevant, wenn der Betreiber als Content-Arm eines Verkäufers arbeitet (Vergütung dann vertraglich, nicht über Affiliate-Provision; nicht öffentlich verifizierbar). Den Zusammenhang mit C2 („kurzlebige Netzwerke“) stelle ich nur als Hypothese auf, es gibt dafür keinen Beleg.

---

## 9. Fazit zu C1–C7 (nur aus Regelsicht)

- **C5:** Nach dem Pilot liegen 5 Videos pro Tag weit unter dem Limit (US 30, DE 25). **Im Pilot** sind aber höchstens 3 pro Tag erlaubt (US bis 5.000 Follower und ≥ 30 Tage, DE ≥ 30 Tage). Für das 5-pro-Tag-Szenario sind im Anlauf also 2 Accounts nötig, oder das Szenario verschiebt sich um mindestens einen Monat. Kleine Präzisierung, keine Widerlegung.
- **C6:** Regelseitig mit **einem** graduierten US-Account möglich (900/Monat); in DE mit 2 Accounts (1.500/Monat). Die Regel verlangt keine mehreren Personen.
- **C7:** Regelseitig mit 2 US- oder 3 DE-Accounts **einer** Person möglich. „Team“ ist regelkonform, wenn es über offizielle Agentur- oder Organisationsstrukturen läuft oder nur produziert. Nicht regelkonform ist ein Team, das sich mit Passwörtern persönlicher Accounts einloggt (US-ToS), oder eines, das Content über Accounts dupliziert (EU-Spam-Tatbestand).
- **C1–C4:** Aus den Portfolio-Regeln folgt keine direkte Widerlegung. P4 (Marketing-Accounts) liefert eine regelkonforme Struktur für markengeführte Multi-Account-Netzwerke. Das passt zur Beobachtung in C2, erklärt sie aber nicht belegbar.

**Gesamturteil Red-Team (Regeln):** Der Vorbericht ist bei den Portfolio-Regeln **nicht zu pessimistisch**. Bei Posting-Automatisierung (API ohne Produktlinks) und VA-Delegation ist er eher **zu optimistisch**. Er unterschätzt, dass eine Einzelperson mit wenigen Accounts die C6/C7-Stückzahlen regelkonform posten **darf**. Er übersieht die Marketing-Account- und Content-Authorization-Wege sowie den leichteren DE-Pilot mit dem niedrigeren DE-Tageslimit von 25.

---

## 10. Quellen (alle abgerufen 25.09.2026, sofern nicht anders vermerkt)

- US Creator Eligibility Policy – https://seller-us.tiktok.com/university/essay?knowledge_id=6939143037667118&lang=en (09/25/2026)
- US What You Need to Know Before Becoming a TikTok Shop Creator – https://seller-us.tiktok.com/university/essay?knowledge_id=7608640301074219&lang=en (06/30/2026)
- US Creator Identity Verification – https://seller-us.tiktok.com/university/essay?knowledge_id=8182993140467499&lang=en (10/29/2025)
- US Affiliate Creator Pilot Program Introduction – https://seller-us.tiktok.com/university/essay?knowledge_id=5526872163927850&lang=en (05/13/2026)
- US Creator Enforcement Policy – https://seller-us.tiktok.com/university/essay?knowledge_id=6837869503317761&lang=en (09/25/2026)
- US Best Practices for Promotional Content – https://seller-us.tiktok.com/university/essay?knowledge_id=5769635937191681&lang=en (06/24/2026)
- US TikTok Shop Creator Terms of Use – https://seller-us.tiktok.com/university/essay?knowledge_id=6314510387906350&lang=en (Last updated 28.08.2026)
- US [Creators] Linking with Agencies, Data Authorization, & Commission Sharing – https://seller-us.tiktok.com/university/essay?knowledge_id=4011666679007022&lang=en (09/26/2024)
- US Creator Bind Eligibility and Requirements – https://seller-us.tiktok.com/university/essay?knowledge_id=3753520906340139&lang=en (09/02/2026)
- US How to Manage Team Access to Organization Account – https://seller-us.tiktok.com/university/essay?knowledge_id=2500395617929015&lang=en (01/07/2026)
- EU Creator E-commerce Permissions Eligibility Policy – https://seller-ie.tiktok.com/university/essay?knowledge_id=747894062696212&lang=en-GB (03/09/2026); DE: https://seller-de.tiktok.com/university/essay?knowledge_id=747894062696212&lang=de-DE
- EU Identitätsverifizierung (Provisionsabhebung) – https://seller-de.tiktok.com/university/essay?knowledge_id=740763580188436&lang=de-DE
- DE Pilotprogramm für Creator*innen – https://seller-de.tiktok.com/university/essay?knowledge_id=5604780513855233&lang=de-DE (25.06.2026)
- EU Inhaltsrichtlinie – https://seller-de.tiktok.com/university/essay?knowledge_id=7404160497927968&lang=de-DE (21.09.2026)
- EU A Creator's Guide to Securing Your TikTok Shop Account – https://seller-ie.tiktok.com/university/essay?knowledge_id=5509564888303361&lang=en-GB (23/06/2026)
- EU Official Account Creators and Marketing Account Creator Binding – https://seller-ie.tiktok.com/university/essay?knowledge_id=7798861624510230&lang=en-GB (02/07/2026)
- UK Creator Policy Pulse (August 2026) – https://seller-uk.tiktok.com/university/essay?knowledge_id=289257470379798 (09/01/2026)
- UK Content Authorization Tool Feature Guide – https://seller-uk.tiktok.com/university/essay?knowledge_id=1920527359182614 (08/20/2026)
- UK Creator Fraud, Abuse, and Misconduct – https://seller-uk.tiktok.com/university/essay?knowledge_id=651807580964640 (04/17/2026)
- UK AIGC – https://seller-uk.tiktok.com/university/essay?knowledge_id=5234615598237462 (08/28/2026)
- TikTok for Developers: Content Sharing Guidelines (Aug 4, 2026), Direct Post API Reference (Aug 24, 2026) – Kopien vom 24.09.2026 in `research/dev_*.txt`
- US ToS (July 15, 2026), EEA/UK ToS (July 2026) – Kopien vom 24.09.2026 in `research/tos_*.txt`
- Community Guidelines (wirksam 24.09.2026) – Kopien vom 24.09.2026 in `research/cg_*_decoded.txt`
- Business Center: https://ads.tiktok.com/help/article/about-managing-tiktok-accounts-in-business-center?lang=en (Sept 2026); TikTok One for Partners: https://ads.tiktok.com/help/article/about-tiktok-one-for-partners (March 2026)
- Nicht verwendet (Bias oder Umgehungsbezug): hidemyacc.com (Anti-Detect-Anbieter), Agentur-Blogs zu CAP-Kriterien (Claimed, ohne Primärbeleg).
