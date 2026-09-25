# TikTok: Reichweite, Monetarisierung, Automatisierung – was ist dokumentiert? (AI-Content, TikTok Shop, Multi-Accounts)

Stand der Recherche: 2026-09-24. Alle Zitate im englischen Original. Tag-Legende: **Verified** = in der Primärquelle selbst gelesen (TikTok-Dokument, Developer-Doku, Newsroom, Originalartikel). **Claimed** = nur aus Sekundärquelle bzw. Behauptung Dritter (Reddit, Blogs, Tool-Anbieter). Zahlen ohne Primärbeleg werden ausdrücklich als nicht verifizierbar markiert.

Methodischer Hinweis: support.tiktok.com leitet heute auf www.tiktok.com/support/faq_detail?id=… um; die Seiten werden clientseitig gerendert. Die Texte wurden über den Support-Backend-Endpunkt (`/feedback/1/faq_detail_by_id/`) abgerufen, der exakt dieselben FAQ-IDs liefert. Die Community Guidelines wurden aus dem eingebetteten Seiten-JSON (`__remixContext`) dekodiert. Web-Search-Budget war nach den ersten Abfragen erschöpft; Reddit/X und einige Verlage (WSJ, Wired, The Verge, NYT) waren aus dieser Umgebung nicht abrufbar – siehe Abschnitt 3.

---

## 1) Kurzfazit

1. **Ein AI-Label allein senkt die Reichweite laut TikTok nicht** – aber nur, solange der Inhalt regelkonform ist. Zwei Primärquellen sagen es wörtlich: Support-FAQ „Turning on the AI-generated content setting won't affect the distribution of your video as long as it doesn't violate our Community Guidelines" und TikTok-Shop-Policy „Content will not be demoted or restricted solely because the AI-generated content setting is enabled". Gleichzeitig können Nutzer seit Nov. 2025 im For-You-Feed per „Manage Topics"-Slider **weniger AI-Content** wählen (Verified, Newsroom 19.11.2025); TikTok betont, das entferne Inhalte nicht, sondern „tailor" die Mischung. Unsichtbare Wasserzeichen + C2PA-Auto-Label machen AI-Content zunehmend maschinell erkennbar (1,3 Mrd. gelabelte Videos bis Nov. 2025, Verified; „3 Mrd." Juli 2026 nur Claimed).
2. **Für Monetarisierung gelten härtere Regeln als für bloße Sichtbarkeit.** Creator Rewards Program verlangt „original and high-quality content that is filmed, designed, and produced entirely by yourself"; Slideshows, reine Text-Overlays, Loops, Lip-Sync und **Werbung/gesponserte Inhalte** sind ausgeschlossen (Verified) – AI-Affiliate-Videos sind damit faktisch nicht Rewards-fähig. Im TikTok Shop (US) ist AI zwar erlaubt, aber: Kein AI-Voice in LIVEs, keine Still-Frame-/Slideshow-Videos ohne Gesicht + physisches Produkt, keine AI-„Ärzte"/digitalen Menschen als Experten, keine AI-veränderten Produktdarstellungen (Verified, Seller-University-Dokumente Stand 09/2026). Verstöße kosten Creator-Health-Rating-Punkte; ab ≤150 Punkten **50 % Traffic-Kürzung**, ≤100 → 90 %, ≤50 → 100 %, 0 → Permanent-Ban (Verified).
3. **Die Grenze erlaubter Automatisierung ist klar dokumentiert:** Erlaubt sind das Content Posting API (nur nach Audit öffentlich; unauditierte Clients posten nur privat; 6 Requests/Min pro Token; Nutzer muss jedem Upload explizit zustimmen), der TikTok-Desktop-/Studio-Scheduler (bis 10 Tage voraus) und Drittanbieter über diese API (Later/Metricool nennen sich „approved/official partner" – Claimed). Verboten sind lt. Community Guidelines (in Kraft seit 24.09.2026) „automation tools, scripts, or other tricks designed to bypass our systems", „Using automation to run many accounts or send repetitive content", „Using AI or bot accounts to drive traffic", Kauf/Verkauf von Engagement und Anleitungen dazu (Verified). Device-Farmen, Engagement-Pods, „Account-Warming" und Proxies werden nicht namentlich genannt, fallen aber eindeutig unter diese Klauseln.
4. **Mehrere Accounts sind erlaubt, aber pro Telefonnummer/E-Mail nur ein Account; bis zu 5 TikTok-Shop-Creator-Accounts pro Ausweis** (Verified). Verboten ist das Verteilen von Verstößen über mehrere Accounts oder die Umgehung von Sperren; TikTok Shop sperrt zusätzlich Accounts, die „associated with accounts that have had e-commerce permissions revoked" sind (Verified) – genau das ist die häufigste Ban-Ursache in den Reddit-Berichten zur „Spring 2026 Ban Wave" (Claimed). Ein Limit „X Accounts pro Gerät" ist in keiner Primärquelle auffindbar.
5. **Investigativ dokumentiert ist v. a. der Missbrauch, nicht die Reichweiten-Drosselung:** 404 Media (30.07.2026) beschreibt eine AI-„Slop Factory" für das FDA-zurückgerufene Supplement Rosabella (Accounts liverboosthub11, poormaninla; Tools VEO 3, HeyGen, ElevenLabs; Behauptung „$51,000/month profit"); Business Insider (20.07.2026) berichtet, dass GMV Max AI-Videos aktiv ausspielt und Marken „hundreds of times a month" per AI posten; WSJ/eMarketer/Affiverse: SharkNinja verbietet AI-Affiliate-Content und streicht Provisionen. Harte Belege für einen „AI-Shadowban" gibt es nicht; die Reddit-Fälle beschreiben eher niedrige Reichweite von **produkt-getaggten** Videos generell und Bans wegen gekaufter/verbundener Accounts (alle Claimed).

---

## 2) Regel für Regel (Zitat, URL, Datum, Jurisdiktion, Tag)

### 2.1 Creator Rewards Program (support.tiktok.com) – Originalität, AI, Ausschlüsse

**Quelle:** TikTok Support „Creator Rewards Program", FAQ-ID 7581821550694013452 (alte URL https://support.tiktok.com/en/business-and-creator/creator-rewards-program leitet dorthin um). Kein sichtbares Seitendatum. Jurisdiktion: global (Programm in ausgewählten Ländern; DE/EU: nicht verfügbar laut Programmliste, hier nicht geprüft). **Tag: Verified** (Abruf 2026-09-24 über Support-API).

- Zulassung: „Have at least 10,000 followers." / „Have at least 100,000 video views in the last 30 days." / „Post videos that are at least one minute long." / „Have a Personal Account. Business Accounts … aren't eligible."
- Verhaltensregeln nach Aufnahme:
  > „No engagement in malicious or fraudulent activities, such as acquiring fake video views or inflating follower counts."
  > „Must not tamper or attempt to tamper with the program, the reward system, or the recommendation system."
  > „Must not create malicious software or modify code to artificially register, post, or increase likes, follows, views, comments, shares, and more."
- Video-Anforderungen:
  > „Post original and high-quality content that is filmed, designed, and produced entirely by yourself."
  > Nicht erlaubt u. a.: „Suspicious or unusual account activity." / „Advertisements, paid promotions, sponsored content, or videos linked to a Series." / „Account details or content that was copied from others."
- Definition „nicht original" (relevant für AI-/Faceless-Formate):
  > „Content that contains different videos or pictures originating from other people, creators, or sources without new and personal ideas."
  > „Content that contains looping videos, single or multiple photos, or only text overlays."
  > „Content that contains lip syncs or copyrighted music that plays for over one minute."
- Qualified Views:
  > „Qualified views are unique video views from the For You feed and exclude views with fraud, paid views, disliked views, views with less than 5 seconds watched, promoted views, and artificial views. Videos must reach 1,000 For You feed views to start generating earnings."
- Review-Ergebnis bei Ablehnung:
  > „It may violate Community Guidelines due to, for example, unoriginal or low-quality content, dangerous activities, spam, or deceptive behavior."
  > „Any rewards previously accumulated from the video will be deducted from your balance."

**Einordnung:** Das Wort „AI" kommt auf der Rewards-Seite **nicht** vor (Nicht in Primärquelle auffindbar). Die Ausschlüsse „produced entirely by yourself", „single or multiple photos", „only text overlays", „sponsored content" schließen typische AI-Slideshow-/TTS-/Affiliate-Formate aber faktisch aus. Sekundärquellen (z. B. auditsocials.com „4-Tier Labels & Penalties", storrito.com) behaupten ein spezifisches Strike-System für ungelabelte AIGC („second … seven-day posting restriction … fourth … permanent monetization ban") – **Nicht in Primärquelle auffindbar**, Tag Claimed/unbelegt.

### 2.2 AI-Content im For-You-Feed: Label, Ranking, „see less AI", unsichtbare Wasserzeichen

**(a) Support-FAQ „About AI-generated content"**, ID 7636670084747893268 (alte URL https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content). Kein Seitendatum. Global. **Verified.**
> „We also require creators to label all AI-generated content that contains realistic images, audio, and video, as explained in our Community Guidelines."
> „Auto label: TikTok may automatically apply the 'AI-generated' label to content we identify as completely generated or significantly edited with AI. This may happen when a creator uses TikTok AI effects or uploads AI-generated content that has Content Credentials attached … (C2PA)."
> „Note: Once your content is labeled as AI-generated with an auto label, you won't be able to remove the label from your post."
> „We may remove content that violates our Community Guidelines policies by depicting misleading information or unlabeled AI-generated content."
> „Note: Turning on the AI-generated content setting won't affect the distribution of your video as long as it doesn't violate our Community Guidelines."
> Falsches Labeln: „misleadingly labeling unaltered content with this label is a violation of our Terms of Service and may result in the removal of content."

**(b) Community Guidelines, Abschnitt „Integrity & Authenticity" → „Edited Media and AI-Generated Content (AIGC)"**, https://www.tiktok.com/community-guidelines/en/integrity-authenticity . Version „2026H2update": „Released August 25, 2026 / Effective September 24, 2026". Global. **Verified.**
> „we require creators to label AI-generated or significantly edited content that shows realistic-looking scenes or people. Unlabeled content may be removed, restricted, or labeled by our team, depending on the harm it could cause."
> „Disclosure isn't needed when: Making small edits like color correction, reframing, or cropping / Using artistic styles, like anime / Using generic text-to-speech (TTS) narration, when the TTS isn't a recognizable voice of a known individual"
> Nicht erlaubt u. a.: „Using the likeness of private figures without consent" / „A public figure taking political stances, supporting products, or commenting on public issues they haven't actually addressed" / „Any content that breaks our Community Guidelines … even if it's AI-generated"
> Unoriginal Content: „Content is also ineligible for the FYF if it includes unoriginal or reused material without anything new." Nicht erlaubt: „Reused or unoriginal content posted without creative edits, such as clips that show someone else's watermark or logo" / „Low-quality or minimally edited content, such as short clips made from GIFs only"

**(c) TikTok Newsroom „More ways to spot, shape and understand AI-generated content"**, https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en , 19.11.2025. Global. **Verified.**
> AI-Slider: Nutzer können in Manage Topics „see more of this content, while those who'd rather see less can choose to dial things down." Und: die Funktion ist „intended to help people tailor the diverse range of content in their feed, rather than removing or replacing content in feeds entirely."
> Unsichtbare Wasserzeichen: „a robust technological 'watermark' that only we can read, making it harder for others to remove." / „Over the coming weeks, we'll start adding invisible watermarks to AI-generated content made with TikTok tools like AI Editor Pro, and content uploaded with C2PA Content Credentials."
> C2PA: „embeds metadata into content that lets us—as well as other platforms who use C2PA—know when something is AI-generated."
> Label-Zahl: „These efforts helped label over 1.3 billion videos to date."
> **Keine Aussage** zu Ranking/Down-Ranking gelabelter AIGC im FYF (Nicht in Primärquelle auffindbar).
Sekundär (TechCrunch 18.11.2025, Social Media Today 19.11.2025): Pfad „Settings > Content Preferences > Manage Topics"; „$2 million AI literacy fund" – **Claimed** (deckt sich mit Newsroom).

**(d) Support-FAQ „Manage topics"**, ID 7636676986101996052. **Verified.**
> „Tap Content preferences, then tap Manage topics. Move the slider to adjust how much you want to see of each topic."
> „The preference you set on different topics only applies to content in your For You feed—other areas of TikTok are not affected, such as your Following feed, profile, and inbox."

**(e) Newsroom „Partnering with our industry to advance AI transparency and literacy"**, https://newsroom.tiktok.com/en-us/partnering-with-our-industry-to-advance-ai-transparency-and-literacy , 09.05.2024. **Verified.**
> „Starting today, we're expanding auto-labeling to AIGC created on some other platforms by launching the ability to read Content Credentials"
> „We label AIGC made with TikTok AI effects, and have required creators to label realistic AIGC for over a year." / Label-Tool: „over 37 million creators have used" it.

**(f) Newsroom „New labels for disclosing AI-generated content"**, https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content , 19.09.2023. **Verified.** Einführung des Creator-Labels; Test eines automatischen „AI-generated"-Labels.

**(g) TikTok Transparency Center „Supporting responsible, transparent AI-generated content"**, https://www.tiktok.com/transparency/en-us/supporting-responsible-transparent-ai-generated-content/ (ohne Datum). **Verified.**
> „We detect AI-generated content through a combination of proactive technologies, alerts from experts and fact-checking partners, searches for clips or keywords related to known AI-generated content, and user reports."
> „When we've identified misleading video or audio content that is spreading elsewhere online and violates our policies, we endeavor to automatically catch and take action on similar versions of that content"

**(h) Support-FAQ „Likeness Detection for AI-generated content (AIGC)"**, ID 7670780803776944661. **Verified.** Verifizierte Creator/18+ können per Ausweis + Gesichtsscan (Jumio) AI-Videos mit ihrem Gesicht finden: „The tool only scans content marked or detected as AI-generated." → Relevanz: AI-Avatare, die reale Personen nachbilden, werden zunehmend meldbar.

**(i) TikTok Shop (US) „AI-Generated Content Restrictions and Requirements"**, https://seller-us.tiktok.com/university/essay?knowledge_id=491489038501663&lang=en , 09/02/2026, „Applies to: United States". **Verified.**
> „Content will not be restricted or penalized solely for using AI, provided it complies with TikTok's Community Guidelines, TikTok Shop policies, and all relevant platform standards and requirements."
> „Content will not be demoted or restricted solely because the AI-generated content setting is enabled, provided it complies with platform rules"
> FAQ: „Will my content be restricted if I enable the AI-generated content label? No, your content will not be restricted."
(Weitere Inhalte dieses Dokuments in 2.5.)

**Sekundär / nicht verifizierbar:** TechTimes (13.07.2026) zitiert eine TikTok-Ankündigung vom 10.07.2026 („labeled more than 3 billion videos as AI-generated content", C2PA-Steering-Committee, erweiterte Spam-Erkennung in Politik/Finanzen/Medizin, „$4 million" Literacy-Programm, „200 million views"). Die dort genannte Newsroom-URL (https://newsroom.tiktok.com/helping-people-spot-and-understand-aigc-on-tiktok) leitet am 24.09.2026 auf die Newsroom-Startseite um → **Claimed**, Primärquelle nicht auffindbar. TechTimes-Angabe „detection identified between 35 and 45 percent of AI-generated content as of late 2025" – ohne Quelle, **Claimed**.

### 2.3 Transparenz-/Enforcement-Zahlen zu AIGC

| Zahl | Quelle | Datum | Tag |
|---|---|---|---|
| „over 1.3 billion videos" mit AI-Label | Newsroom (2.2c) | 19.11.2025 | Verified |
| „over 37 million creators" nutzten das AI-Label-Tool | Newsroom (2.2e) | 09.05.2024 | Verified |
| „Between July and December 2025, we removed around 112 million pieces of content" (Videos, LIVEs, Ads, Produktlistings, Kommentare, EU) | Newsroom „Digital Services Act: Our sixth transparency report…", https://newsroom.tiktok.com/digital-services-act-our-sixth-transparency-report-on-content-moderation-in-europe?lang=en-150 | 29.04.2026 (Berichtszeitraum H2 2025), EU/EWR | Verified |
| „Automated systems actioned 93.8% of all violating content without human review." / „97.6% of automated enforcement decisions being confirmed as correct." | ebd. | 29.04.2026, EU | Verified |
| AIGC-spezifische Removal-Zahlen im DSA-Bericht | ebd. | – | **Nicht in Primärquelle auffindbar** (keine AIGC-Kategorie ausgewiesen) |
| TikTok Shop: „rejected more than 70 [million] products before being listed, a 40 [percent] increase from the previous six months" (H1 2025) | TikTok-Shop-Bericht vom 06.11.2025, zitiert in Mashable (Christianna Silva, 07.11.2025, Update 18.11.2025), https://mashable.com/article/tiktok-shop-fake-products-ai | H1 2025 | Claimed (Mashable-Korrektur: Zahl umfasst alle Verstöße, nicht nur AI) |
| „3 billion" AI-gelabelte Videos | TechTimes 13.07.2026 | – | Claimed (siehe 2.2) |
| „51,618 synthetic media videos … second half of 2025 … 340% increase … permanently banned 8,600 accounts" | storrito.com (Scheduling-Tool-Blog), https://storrito.com/resources/tiktok-removed-51000-ai-videos-creators-feeling-it/ | undatiert | **Claimed, keine Primärquelle angegeben; nicht verifizierbar** |
| Quartals-„Community Guidelines Enforcement Report" (Q4 2025 / Q1 2026 / Q2 2026), https://www.tiktok.com/transparency/en-us/community-guidelines-enforcement-2025-4/ usw. | Seiten laden Daten clientseitig; Inhalt aus dieser Umgebung nicht extrahierbar | – | **Nicht in Primärquelle auffindbar (technisch)** |

Enforcement-Einzelfälle mit Primärbezug: 404 Media (07.10.2024) – Accounts „melisogn9dl" und „Mothers in Healing" (AI-Slideshows für Reus Research NAD+-Supplement, ein Video „more than 3 million views") wurden nach Anfrage gelöscht; TikTok „did not provide a statement about which rules it had broken". Eigene Prüfung 2026-09-24: `tt_profile.sh melisogn9dl` → statusCode 10221 (Account existiert nicht) – **Verified** (Account weg), Ursache Claimed.

### 2.4 Investigative Berichterstattung zu „AI Slop" in TikTok-Shop-Affiliate-Videos

**404 Media – „Inside an AI TikTok Shop Slop Factory That Shills Supplements Recalled By the FDA"**, Jason Koebler, 30.07.2026, https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/ . **Verified** (Artikel gelesen).
- Marke/Produkte: Rosabella (Ambrosia Brands; Gründer Luca Washenko, MNY Ventures); Produkte „Nigerian SECRET to CLEAN LIVER", Beetroot-Powder; FDA-Rückruf wegen „extensively drug-resistant salmonella"; Klage des Wettbewerbers Humann (SuperBeets) wegen AI-„Ärzten".
- Accounts: **liverboosthub11**, **poormaninla** (Video 14.06.2025 mit AI-„doctor in a whitecoat"). Eigene Prüfung 2026-09-24: `liverboosthub11` existiert (2.669 Follower, 60.200 Likes, 137 Videos, angelegt 06/2025, ttSeller false) – **Verified**; `poormaninla` → 10221, nicht mehr vorhanden – **Verified**.
- Produzenten/Tools: YouTuber Harry Chang (NZ) und Jimmy Farley; Google VEO 3, HeyGen, ElevenLabs (Stimme „Latisha 1"), CapCut; Anleitung „strong African American accent"; ein Video 1,3 Mio. TikTok-Views.
- Geldbehauptungen (Claimed, Selbstauskunft im Artikel): Chang „$51,000/month profit"; Washenko: „we paid out over $400,000 last month to creators", Einzelne „$300,000".
- TikTok-Reaktion: im Artikel keine Stellungnahme dokumentiert.

**Business Insider – „TikTok Shop creators are facing an AI reckoning"**, Dan Whateley, 20.07.2026, https://www.businessinsider.com/tiktok-shop-creators-brands-using-ai-to-replace-human-slop-2026-7 . **Verified** (Volltext per curl).
> „Brands — and TikTok's algorithm — are increasingly embracing videos with AI-generated influencers and product imagery."
> „These AI-generated product videos are increasingly showing up in the feed as TikTok's automated ads system, GMV Max, surfaces them. They can be lucrative: One AI-video maker drove tens of thousands of dollars in product sales, according to a screenshot of their affiliate profile that was viewed by Business Insider."
> „A TikTok Shop employee said it had become a 'hot topic' internally."
> „Some brands are now using AI to recreate multiple versions of an influencer's post that performed well, three Shop marketers said. Others are using the tech to post hundreds of times a month without having to pay creators or send them free samples"
> „TikTok, which didn't respond to requests for comment, wrote in its seller documentation that generative AI is permissible as long as the videos are labeled, don't misrepresent a product or imitate a real person, and respect intellectual property rights."
> Beispiele: AI-Influencerin mit Hoodie („good amount of give to it"); „synthetic avatars used power washers and propane torches, pet brushes, and microfiber dusters to spotlessly clean their driveways, pets, and air conditioner vents in seconds." Nutzerkommentar: „Never seen green grass burn like that. Stupid AI"
> Genannte Firmen/Personen: Socialscale.ai (Fabian Ouwehand), Social Tale (Ashley Wright), Third (Anish Dalal), Anwalt Robert Freund (FTC-„honest opinions"-Risiko), Nicolas Waldmann (TikTok Shop Governance). BFCM: „about 10 million shoppable videos".

**Wall Street Journal – „AI Videos Are Flooding TikTok Shop"**, https://www.wsj.com/cmo-today/ai-videos-are-flooding-tiktok-shop-c86a88e0 (Juli 2026; nicht abrufbar). Inhalte über Sekundärquellen – **Claimed**:
- SharkNinja-Memo: TikToks AI Video Maker sei „not permitted under our affiliate program's No AI-Generated Content policy"; Provisionen werden gestrichen; CCO Neil Shah: „We didn't want an AI-generated Shark vacuum cleaning an AI-generated floor. We want real consumers seeing real products being used by real people." (Affiverse 17.07.2026, https://www.affiversemedia.com/tiktok-shop-ai-generated-videos-affiliate-trust/ ; eMarketer, Rachel Wolff, 15.07.2026, https://www.emarketer.com/content/ai-reshapes-tiktok-shop-affiliate-playbook : „using AI-generated content to promote its products will result in forfeited commissions").
- Rare Beauty distanziert sich von AI-Affiliate-Videos („digital duplicates") (Affiverse, https://www.affiversemedia.com/rare-beauty-ai-tiktok-shop-affiliate-videos/ ).
- Charm.io-Daten via WSJ: „11.3 million creators" mit Affiliate-Umsatz 2026 YTD, „945,000" in den USA, „2.3 million" global 2024.

**Business Insider (Nov. 2025) via Mashable 07.11.2025** – Claimed: Nicolas Waldmann: „It's organized crime, to be honest … They're trying to basically go through and sell, and of course, never deliver anything, and then run with the money."; TikTok nutze „AI to basically deal with AI"; AI-generierte Fake-Storefronts.

**404 Media – „Hack Reveals the a16z-Backed Phone Farm Flooding TikTok With AI Influencers"**, Emanuel Maiberg, 17.12.2025, https://www.404media.co/hack-reveals-the-a16z-backed-phone-farm-flooding-tiktok-with-ai-influencers/ (Paywall, Intro gelesen – Verified für Intro): Doublespeed, „more than 1,000 smartphones", „at least hundreds of AI-generated social media accounts", „often without the required disclosure that these are advertisements". Ergänzend New York Magazine/Intelligencer (Doublespeed-Reportage, https://nymag.com/intelligencer/article/doublespeed-tech-founder-creating-an-army-of-ai-influencers.html ) – Claimed: „1,200 smartphones" vor Ort, ca. 4.500 insgesamt, „$450 per month" pro Kunde; Zitat Autoviral-Betreiber Zachary Thompson: „On any platform, you want to be cognizant of something called a trust score, which is basically how trustworthy your phone is." (belegt, dass Device-Farmen gezielt Anti-Spam-Signale umgehen – genau das verbieten die CG, s. 2.6).

**404 Media – „AI-Generated Pro-North Korean TikToks Are Also Bizarre Ads for Supplements"**, 07.10.2024 (s. 2.3). **Verified.**

**404 Media – „Inside the World of TikTok Spammers and the AI Tools That Enable Them"**, 05.03.2024, https://www.404media.co/inside-the-world-of-tiktok-spammers-and-the-ai-tools-that-enable-them/ (teilweise Paywall): Crayo.ai, Reddit-Story-/Minecraft-Splitscreen-Spam, Monetarisierung über Creativity Program Beta. **Verified** (Intro).

**Rest of World – „Livestream shopping stars face off against trolls, hagglers, and AI rivals"**, Linda Yulisman, 02.10.2025, https://restofworld.org/2025/indonesia-tiktok-shop-livestream-sellers-ai-rivals/ . **Verified.** AI-Hosts in Indonesien (Social Bread; Imagine8 Studio/„Lentari Pagi"); „We are ready with the technology. But no one can afford to pay."; AI-Bots seien schlechter im „banter". Keine TikTok-Stellungnahme.

**Modern Retail – „Marketplace Briefing: How a cartoon frog wizard is helping Clorox sell Pine-Sol on TikTok Shop"**, Allison Smith, 02.07.2026 (Member-only) – Cartoon-Maskottchen, **nicht** als AI beschrieben; kein „AI-Slop"-Artikel von Modern Retail auffindbar.

**New York Times – „AI avatars … supplements … social media"**, 09.03.2026, https://www.nytimes.com/2026/03/09/technology/ai-avatars-supplements-social-media.html (403). Via eMarketer (https://www.emarketer.com/content/ai-doctor-fakes-wellness-influencers-fuel-health-scam-ads-on-social-media ): „Hundreds of ads featuring AI-generated doctors and fake wellness influencers…"; „TikTok told the NYT that it removes and bans ads with false health claims" – **Claimed**.

**Wired, The Verge:** keine passenden Artikel zu TikTok-Shop-AI-Slop auffindbar/abrufbar (Wired 2023-Artikel zu „Virtual Human"-Livestreams in China existiert, nicht abrufbar). eMarketer: nur der o. g. Artikel (15.07.2026).

### 2.5 TikTok Shop: Creator Health Rating (CHR) & Enforcement gegen Low-Quality-/AI-Content (US)

**Creator Health Rating Overview and Requirements**, https://seller-us.tiktok.com/university/essay?knowledge_id=5054301796321070&lang=en , 09/21/2026, US. **Verified.**
> „The Creator Health Rating (CHR) is a score from 0-1,000 … You lose points for violating policy rules or having performance issues."
> „All new TikTok Shop creators start with 200 points." Green 200–1.000 / Orange 151–199 / Red 1–150 / 0 = „all e-commerce permissions are banned."
> „Point deduction will be automatically reset after 90 days" / „After a set number of deductions, you may be limited to posting up to 3 pieces of content per day for 7 days."
> Punkte verdienen: „Earn 1 point for every 10 completed orders generated through policy-compliant content." / „Each piece of content can earn up to 20 points, and you can earn up to 65 points per week."
> Enforcement: „150 points and below: 50% account-level traffic reduction until your CHR recovers above 150 points." / „100 points and below: 90% account-level traffic reduction" / „50 points and below: Full account-level traffic reduction" / „0 points: Permanent removal of all e-commerce creator permissions."
> „TikTok Shop may take immediate action (including suspensions or permission removal) for repeated or high-risk violations, regardless of your CHR score."

**Creator Enforcement Policy**, https://seller-us.tiktok.com/university/essay?knowledge_id=6837869503317761&lang=en , 07/31/2026, US. **Verified.**
> Auslöser: „Attempt to bypass platform rules or manipulate features. This may include … Miscategorizing content / Engaging in fake engagement / Using multiple accounts to avoid enforcement"
> Wiederholte Verstöße u. a.: „Misleading Promotions / Low Quality Content / Weight Management / Medical Claims / Unoriginal Content"
> „Creators who commit the same policy violation 6 times within a 90-day period may have their e-commerce permissions removed immediately, and their commissions frozen, regardless of their Creator Health Rating (CHR) points."
> Maßnahmen: „Shoppable Video Limits", „Monetization Suspension", „Freezing Payments: TikTok Shop may permanently freeze all payments", „Audience Reach: TikTok Shop may reduce the visibility of the creator's content across the platform or limit search results to include the creator."
> „Scheduled shoppable videos count towards your limit the moment they are scheduled"

**Content Policy (TikTok Shop)**, https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617&lang=en , 09/17/2026, US. **Verified.**
> „AI-generated content is not allowed if it: Misleads or deceives viewers / Impersonates others / Changes or exaggerates a promoted product / Fabricates product effects or functions"
> „AI-generated content may be considered misleading or low-quality if it replaces real product demonstration with synthetic visuals that do not help shoppers understand the product accurately."
> Verboten: „Content that lacks active engagement, such as videos or LIVEs where the creator does not speak, interact with viewers, appear on screen, or meaningfully present or demonstrate the product." / „Exclusively Graphics Interchange Format (or GIF-based) videos"
> Spam/Fraud: „Manipulating platform mechanisms in order to artificially generate orders, views, likes, comments, follows, positive customer feedback, or ratings" / „Promoting artificial traffic generation services" / „Creating malicious software or modifying code to artificially increase orders, views, likes, followers, shares, or comments"

**Requirements for High-Quality Videos and LIVEs**, https://seller-us.tiktok.com/university/essay?knowledge_id=4581457528243969&lang=en , 09/17/2026, US. **Verified.**
> Video: „Include engaging and dynamic visuals, ensuring they feature your face and the physical product." / „Do not use still, looping, or scrolling images through the entire video without featuring your face and the physical product." / „Aim for at least 3 seconds of dynamic content without any still images or looping visuals"
> Still-Frame-Definition umfasst: „Still images / Screenshots / Scrolling image / Screen recordings / Slideshows / Animated content"
> LIVE: „Do not use non-real-time verbal interaction such as AI-generated voices, audio recordings, or radio." / „Do not use animated figures or content that covers more than 50% of the screen."
> „Content that relies heavily on still frames or static visuals may be subject to enforcement actions that impact your account health."

**AI-Generated Content Restrictions and Requirements** (s. 2.2i), 09/02/2026, US. **Verified.**
> „Disclosure is especially important when: The video or audio includes synthetic faces, voices, digital humans, or highly realistic virtual figures"
> Label-Text: „Once enabled, a label stating 'Disclosed by creator as AI-generated' will appear in the bottom-left corner of the content."
> „False disclosure is a violation, including: … Failing to disclose AI use when AI plays a significant role in content creation. Such violations may result in content removal or account restrictions."
> „Using virtual digital humans or AI-generated 'professional' images, packaged in formats like news broadcasts or expert lectures, to endorse the efficacy of health-related products" – „will be a key focus of governance."
> Verbotene AI-Effekte: „Shampoo that 'instantly grows hair'", „Showing a vacuum removing deep stains instantly", „Turn flat (2D) products into fake 3D or rotating visuals", „Fear-based or shocking visuals"
> Enforcement: „Restricting content distribution or visibility / Removing product links or shopping cart functionality / Deducting applicable Creator Health Rating (CHR) points"; Account: „limiting posting capabilities, permanently disabling commission withdrawal privileges, or suspending or banning the account entirely."

**Best Practices for Promotional Content**, https://seller-us.tiktok.com/university/essay?knowledge_id=5769635937191681&lang=en , 06/24/2026, US. **Verified.**
> „Do not use AI-generated audio or voiceover narrations in your LIVEs." / „Do not repost your own content." / „Whether you manage one account or many, each post should offer something new for your audience to discover." / „Do not manipulate your videos using edits, effects, or filters to disguise copied or repetitive content."

**TikTok Shop Creator Terms of Use**, https://seller-us.tiktok.com/university/essay?knowledge_id=6314510387906350&lang=en , 09/15/2026, US. **Verified.**
> „You agree not to generate, encourage, or induce non-authentic clicks, conversions, or impressions of your Creator Content, including through fraud, automation, deception, collusion, or any other means."
> „18.7 … You agree that we can use automated tools and human reviewers to review your content"

**Creator Eligibility Policy**, https://seller-us.tiktok.com/university/essay?knowledge_id=6939143037667118&lang=en , 07/31/2026, US. **Verified.**
> „Must have no prior record of having e-commerce permissions revoked by TikTok Shop" / „Must not be associated with accounts that have had e-commerce permissions revoked by TikTok Shop"
> Pilot-Programm: Affiliates <5.000 Follower mind. 30 Tage eingeschränkt; frühere Freigabe u. a. bei „at least 176 Creator Health Rating points".
**Affiliate Marketing Policy**, https://seller-us.tiktok.com/university/essay?knowledge_id=2244964886103809&lang=en , 09/02/2026: Voraussetzung „Creator Health Rating … of 150 or higher". **Verified.**
**What You Need to Know Before Becoming a TikTok Shop Creator**, https://seller-us.tiktok.com/university/essay?knowledge_id=7608640301074219&lang=en , 06/30/2026: „Creators with fewer than 5,000 followers can post up to 5 shoppable videos per week." **Verified.**
**Account Health Rating (AHR) Requirements** (Seller-Pendant), https://seller-us.tiktok.com/university/essay?knowledge_id=6750828276418350&lang=en , 06/29/2026: Start 200 Punkte, 180-Tage-Fenster, Sperren bei 150/100/50, „permanently deactivated" bei 0. **Verified.**

**Enforcement-„Wellen" 2025–2026 – nur Sekundär/Community (Claimed):**
- AdBeacon (27.07.2026): Violation-Points-System durch AHR/CHR ersetzt (Juli 2026); Livestream-Verbot von „AI-generated voices, pre-recorded audio tracks, and radio-style scripted narration" – deckt sich mit den Verified-Dokumenten oben.
- Allymatic (26.06.2026) / Affiverse: „May bans": TikTok habe im Mai 2026 AI-Stimmen, Standbilder >50 % und vorproduziertes Audio aus Shop-Content verbannt; Creator Enforcement Policy vom 02.06. mit 90-Tage-Fenster; PPS (Promotion Performance Score) ab 27.08.2026 in 6 SEA-Märkten, Sichtbarkeit „may" leiden unter 3,0.
- Reddit r/TikTokShopAffiliate, u/future_flora, 13.04.2026, „Affiliates Talk About the Spring 2026 TikTok Shop Ban Wave", https://www.reddit.com/r/TikTokShopAffiliate/comments/1sjw8xg/ : gesammelte Creator-Zitate – gekaufte Accounts gebannt („seeing a lot of bought accounts being banned"), Backup-Accounts wegen „impersonation" gebannt, Bans wegen „associated with previously revoked accounts" trotz „all organic accounts", rückwirkende Violations auf Videos von 2024/2025, Provisionen 60 Tage eingefroren. **Claimed** – aber konsistent mit den Verified-Regeln (Creator Eligibility „associated with…", Creator Enforcement „Using multiple accounts to avoid enforcement").
- Eine offizielle TikTok-Mitteilung über eine „Enforcement-Welle gegen AI-Affiliate-Content" ist **nicht in Primärquelle auffindbar**.

### 2.6 Grenze erlaubte Automatisierung vs. verbotenes Verhalten

**Erlaubt / offiziell:**

*Content Posting API – Get Started*, https://developers.tiktok.com/doc/content-posting-api-get-started , „Last updated August 4, 2026". **Verified.**
> „All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restrictions on content visibility, your API client must undergo an audit to verify compliance with our Terms of Service."

*Content Sharing Guidelines*, https://developers.tiktok.com/doc/content-sharing-guidelines , August 4, 2026. **Verified.**
> „API Clients must only start sending content materials to TikTok after the user has expressly consent to the upload."
> „The users of API Clients must have full awareness and control of what is being posted to their TikTok accounts."
> „API Clients should facilitate authentic creators to post original content to TikTok." (Kopieren beliebiger Inhalte anderer Plattformen ausdrücklich untersagt)
> Privacy-Dropdown ohne Default („no default value"); keine Promo-Wasserzeichen der App.
> Limits laut Dokument: unauditierte Clients max. 5 Nutzer pro 24 h; Posting-Cap pro Creator-Account ca. 15 Posts/Tag, Creator-Cap richtet sich nach der im Audit angegebenen Schätzung (Verified, Wortlaut der Extraktion zusammengefasst).

*Direct Post API Reference*, https://developers.tiktok.com/doc/content-posting-api-reference-direct-post , August 24, 2026. **Verified.**
> „Each user access_token is limited to 6 requests per minute." / „Unaudited clients can only post to a private account." / Fehlercode, wenn „daily post cap from the API is reached for the current user" (Zahl nicht genannt).

*Media Transfer Guide* (August 4, 2026): Video max. 4 GB, max. 10 Min. via API; Fehler „rate_limit_exceeded". **Verified.**

*TikTok Developer Terms of Service*, https://www.tiktok.com/legal/page/global/tik-tok-developer-terms-of-service/en , „Last Updated: Dec 26, 2025", global. **Verified.**
> nicht erlaubt: „use the TikTok Developer Services or TikTok Services, without TikTok's express written consent, for any commercial or unauthorized purpose, including without limitation communicating or facilitating any commercial advertisement or solicitation or spamming"
> „use any robot, spider, site search or retrieval application, or other device to collect information about users … for any unauthorized purposes"
> Nutzung, die „exceeds reasonable request volume, constitutes excessive or abusive usage"

*Support-FAQ „Schedule video"*, ID 7078299678101477893. **Verified.**
> „Only a 'Business Account' or over with a 10,000 followers or more can access desktop scheduling." / „You can schedule a minimum of 15 minutes and a maximum of 10 days in advance of publishing." / „This feature is not available for TikTok Mobile Web."
(Hinweis: FAQ ist älter; Drittanbieter berichten, dass Creator-/Business-Accounts im TikTok Studio planen können – Claimed.)

*Support-FAQ „Connect to third-party apps"*, ID 7543604785694562872. **Verified.**
> „If you allow an app to have access to your public content, your Tiktok posts will contain a watermark." / Missbrauch melden: „If you believe your data is being misused by the app, such as creating spam, contact us at tiktokplatform@tiktok.com."

*Scheduling-Partner (Selbstauskünfte, alle Claimed):* Later: „Later is an approved TikTok Content Marketing Partner" (later.com/blog/tiktok-scheduler). Metricool: „Metricool is an official TikTok partner and allows scheduling for all account types, including Personal." (metricool.com/schedule-tiktok, 01.01.2026). Buffer: „Trending TikTok sounds cannot be added when auto-publishing through Buffer because TikTok's API does not provide access to its full music library." (buffer.com/tiktok). Hootsuite: Partnerstatus **nicht auffindbar** (Seiten 404). Offizielles TikTok-Marketing-Partner-Verzeichnis war nicht abrufbar.

**Verboten (Plattformregeln):**

*Community Guidelines „Deceptive Behavior & Fake Engagement" / „Spam"*, https://www.tiktok.com/community-guidelines/en/integrity-authenticity , Effective September 24, 2026, global. **Verified.**
> „we don't allow accounts that mislead or try to manipulate our platform, or the trade of services that artificially boost engagement or trick the recommendation system."
> „You can have multiple accounts—for example, for fan content or creative expression—but not to deceive others or break the rules. If we find deceptive account behavior, we may: Ban your account / Ban additional or new accounts you create / Restrict your account, which could include limiting your ability to post new content, appear in top search results, or in the FYF"
> „We strictly prohibit automation tools, scripts, or other tricks designed to bypass our systems. These can result in content removal, account bans, or other enforcement. If your account is restricted or banned, you may not create or use another account to get around it."
> „If we detect accounts or content with inauthentic metrics, we'll remove fake likes, followers, or other inflated signals. Content that tries to manipulate people into giving gifts or inflating likes or follows isn't eligible for the FYF."
> Spam-Liste: „Using automation to run many accounts or send repetitive content" / „Posting a large amount of irrelevant material" / „Buying or selling followers or engagement for financial gain" / „Using bots or scripts to write fake reviews or comments, or to increase likes or shares"
> Umgehung: „Spreading violative content across multiple accounts" / „Using a different account to continue violating policies after being banned" / „Using another account to avoid restrictions, such as comment blocks or FYF-ineligible content restrictions"
> Engagement-Dienste: „Trading, marketing, or providing access to services that artificially increase engagement, such as: Followers or likes / Fake reviews / Using AI or bot accounts to drive traffic / Sharing how-to guides or tips for boosting engagement in fake or deceptive ways"
> Regulated Goods: „Engagement services like selling likes or followers" (verbotene Dienstleistung)
> Wörter „account farm", „device farm", „emulator", „engagement pod", „account warming", „proxy" kommen **nicht** vor (Nicht in Primärquelle auffindbar) – die Klauseln „automation … to run many accounts", „tricks designed to bypass our systems" und „AI or bot accounts to drive traffic" decken sie sachlich ab.

*Terms of Service (USA)*, https://www.tiktok.com/legal/page/us/terms-of-service/en , „Last Updated: July 15, 2026". **Verified.**
> Sec. 3.4 nicht erlaubt: „engage in inauthentic commercial behaviors, such as by operating spam or impersonation accounts or any other means further detailed in our Community Guidelines" / „scrape, crawl, export or otherwise extract any data or content … using any automated system or software, including automated 'bots,' except as approved in writing" / „use TikTok Content …, another user's content or generative AI-enabled features for commercial purposes unless permitted"
> Sec. 3.10: Verbot, zu behaupten, „that your Output is human-generated or otherwise generated without the use of AI" (bei TikTok-eigenen GenAI-Features).
*Terms of Service (EWR/UK/CH)*, https://www.tiktok.com/legal/page/eea/terms-of-service/en , July 2026. **Verified.** Sec. 4.5: „engage in inauthentic commercial behaviours such as operating spam or impersonation accounts" / „engage in fake review activity (including … paying others to post fake reviews or offering services to facilitate fake reviews)" / Datenextraktion nur mit „automated system or software that is … approved in writing by TikTok".

*Support-FAQ „Content violations and bans"*, ID 7543604781940791864. **Verified.** Strikes: erste Entfernung = Warnung, dann Strikes pro Policy-Bereich/Feature; „Strikes on your TikTok account will expire after 90 days"; Permanent-Ban u. a. wenn „Your account exists solely to violate our rules."

### 2.7 Mehrere Accounts – Limits und „suspicious activity"

| Regel | Zitat | Quelle | Tag |
|---|---|---|---|
| 1 Telefonnummer / 1 E-Mail / 1 Social-Login = 1 Account | „Each phone number, email address, and social media account can only be linked to one TikTok account." | Support „Creating an account", ID 7581821549574052364 | Verified |
| Mehrere Accounts pro Gerät erlaubt | „You can add additional accounts to your device and switch between them on TikTok." | ebd. | Verified |
| Anzahl Accounts pro Gerät | – | – | **Nicht in Primärquelle auffindbar** (die kursierende „3 pro Gerät"-Regel ist in keiner TikTok-Quelle belegt) |
| Nummer erst nach Löschung (30 Tage) neu nutzbar | „The deleted account will be deactivated for 30 days and then removed permanently. After that, the phone number can be linked to a new account." | Support „This phone number is already registered", ID 7078299664386103813; ebenso „Email and phone number", ID 7581820709597583928 | Verified |
| Mehrfach-Accounts erlaubt, Umgehung nicht | „You can create multiple accounts on TikTok. However, we may restrict or permanently ban your account if you make any attempts to avoid a restriction or ban imposed on another account you own, including: Create a new account after your account has been banned for a severe violation. / Post violative content on a new or existing account. / Spread content violations across multiple accounts." | Support „Content violations and bans" | Verified |
| CG: Mehrfach-Accounts nur ohne Täuschung | „You can have multiple accounts … but not to deceive others or break the rules." + „Ban additional or new accounts you create" | Community Guidelines (2.6) | Verified |
| TikTok Shop: bis zu 5 Creator-Accounts je Ausweis | „1 ID can be used to verify up to 5 TikTok Shop creator accounts." | Seller University, knowledge_id=7608640301074219, 06/30/2026 | Verified |
| TikTok Shop: Verbindung zu gesperrten Accounts | „Must not be associated with accounts that have had e-commerce permissions revoked by TikTok Shop" | Creator Eligibility Policy, 07/31/2026 | Verified |
| TikTok Shop: Multi-Account zur Umgehung | „Using multiple accounts to avoid enforcement" (Enforcement-Auslöser) | Creator Enforcement Policy, 07/31/2026 | Verified |
| Creator Rewards: verdächtige Aktivität | Ausschluss bei „Suspicious or unusual account activity." | Support Creator Rewards | Verified |
| Geräte-Signale | „Manage trusted devices. (If we detect unfamiliar devices, we'll ask you to review them.)" | Support „Account safety", ID 7543604780950624824 | Verified |
| Account „nicht empfohlen" | „If you repeatedly post content that is unsuitable for the For You feed, your account and posts won't appear in the For You feed and will be harder to find in search." | Support „Why is my account not being recommended?", ID 7543604783110969862 | Verified |

Was konkret „suspicious activity" auslöst (IP/Proxy, Emulator, Gerätefingerprint), beschreibt TikTok **nicht** öffentlich (Nicht in Primärquelle auffindbar). Sekundär: Proxy-Anbieter GoLogin behauptet in einem Reddit-Werbepost (u/GoLoginS, 02.07.2026) „Device-Level shadowbans" – **Claimed, Eigeninteresse des Anbieters**.

### 2.8 Dokumentierte Shadowban-/Reichweiten-Fälle für AI-UGC-Accounts (alle Claimed)

Reddit war aus dieser Umgebung nicht direkt abrufbar; die folgenden Fälle stammen aus dem lokal gespeicherten Reddit-Dump anderer Recherche-Agents (research/reddit_posts_dump*.md) und sind Selbstauskünfte ohne Prüfmöglichkeit.

1. r/TikTokshop, u/QuickRevenue6534, 27.06.2026, Score 22, https://www.reddit.com/r/TikTokshop/comments/1ugrszw/ – Markeninhaber („close to $400,000 in sales" 2025): „whenever an affiliate tags a product, that video's reach is much lower than the creator's normal content." Test: getaggtes Video „stalled at around 800 views", gleiches Produkt ohne Tag „roughly 10 times more views". Ausdrücklich: „I'm not saying I can prove that's how TikTok's algorithm works". → Betrifft Produkt-Tags, nicht AI-Label.
2. r/TikTokshop, u/sfcoolgirl, 17.02.2026, https://www.reddit.com/r/TikTokshop/comments/1r7h6jy/ – „Most affiliate videos are sitting at 0 views." Frage: „Does TikTok throttle affiliate views unless the brand puts ad spend behind the videos?"
3. r/TikTokShopSellers, u/khaleddoesecom, 26.07.2026, https://www.reddit.com/r/TikTokShopSellers/comments/1v7i0lp/ – Seller erwägt Creatify/Arcads/HeyGen/Argil: „What I don't know is how the algorithm treats it because there's the AI-generated labelling thing and i'm wary of pumping AI video into an account that's finally getting decent reach." (Unsicherheit, kein Befund)
4. r/TikTokShopAffiliate, 13.04.2026, „Spring 2026 TikTok Shop Ban Wave" (s. 2.5) – Bans gekaufter Accounts, Backup-Accounts („impersonation"), „associated with previously revoked accounts"; keine AI-Bezüge.
5. r/passive_income, 24.02.2026, „Running a faceless finance TikTok for 8 months…", https://www.reddit.com/r/passive_income/comments/1rdiwob/ – Canva+TTS: „Best one got 340 views. Most got under 100."; nach Wechsel auf AI-Avatar „Averaged around 800 views" – kein Shadowban, eher Qualitäts-/Retention-Effekt.
6. r/Bloggers, 27.11.2025, ShopReelAI-Review (Affiliate-Werbung), https://www.reddit.com/r/Bloggers/comments/1p80o00/ – automatisierte Videos „500–1,200 views", „a few hovered around 200–300" (neuer Account).
7. r/AI_ecommerce, „AI-generated UGC is doing $200–$300/day organically", https://www.reddit.com/r/AI_ecommerce/comments/1sl050c/ – „47 videos posted (31 AI-generated, 16 creator)"; Einkommensbehauptung ohne Beleg.
8. Reddit-Kommentar (Dump): Account „phone w no sim-card and with NY residential vpn (proxy) … my videos are getting 0 views now" – Hinweis auf Reichweitenverlust bei Proxy/VPN-Setup.
9. 404 Media (2.3): AI-Slideshow-Accounts melisogn9dl / „Mothers in Healing" nach Presseanfrage gelöscht (2024) – Verified (Löschung), Grund nicht genannt.
10. X/Twitter: **nicht abrufbar**, keine Fälle dokumentiert.

**Befund:** Kein einziger Fall belegt kausal einen „AI-Label-Shadowban". Dokumentierte Reichweitenverluste betreffen (a) produkt-getaggte Affiliate-Videos generell, (b) Accounts unter CHR-Traffic-Kürzung (50/90/100 %), (c) Ban-/Restriktionsgründe wie Multi-Account-Assoziation, gekaufte Accounts, Proxy-Setups, (d) FYF-Ineligibility wegen „unoriginal or reused material" / Still-Frame-Content. TikToks eigene Aussage: Label allein ändert Distribution nicht (2.2a, 2.2i).

---

## 3) Offene Punkte / nicht auffindbar

- **Ranking gelabelter AIGC im FYF:** Keine TikTok-Primärquelle beschreibt eine algorithmische Abwertung gelabelter AI-Videos; belegt sind nur (1) Nutzer-Slider „see less", (2) FYF-Ineligibility für „unoriginal or reused material" und (3) Shop-Traffic-Kürzungen über CHR. Wie stark der Slider die Ausspielung tatsächlich reduziert: nicht dokumentiert.
- **AIGC-Enforcement-Zahlen:** Quartals-Enforcement-Reports (community-guidelines-enforcement-2025-4 / 2026-1 / 2026-2) sind clientseitig gerendert und konnten nicht ausgelesen werden; der DSA-Bericht (H2 2025) enthält keine AIGC-Kategorie. Die kursierenden Zahlen „51,618 videos / 8,600 accounts / +340 %" (storrito.com) und das „4-Tier-Strike-System für ungelabelte AIGC" (auditsocials.com) haben keine Primärquelle → nicht verwenden.
- **„3 Mrd. gelabelte Videos" (Juli 2026):** Newsroom-URL nicht erreichbar; nur TechTimes.
- **WSJ „AI Videos Are Flooding TikTok Shop" (Juli 2026), NYT (09.03.2026), Wired, The Verge, Modern Retail (Member-only):** Volltexte nicht abrufbar; Inhalte nur über eMarketer/Affiverse/Business Insider.
- **Accounts pro Gerät, Trigger für „suspicious activity", Proxy-/Emulator-Erkennung:** Nicht in Primärquelle auffindbar.
- **Offizieller Partnerstatus von Later/Buffer/Metricool/Hootsuite:** nur Selbstauskünfte; TikTok-Partnerverzeichnis nicht abrufbar.
- **Content Posting API:** exakter täglicher Post-Cap pro Nutzer wird in der Doku nicht beziffert; Audit-Dauer/Kriterien nur per Login einsehbar.
- **Offizielle Ankündigung einer „Enforcement-Welle gegen AI-Affiliate-Content":** nicht auffindbar; belegt sind nur die Policy-Updates (05–09/2026) und Community-Berichte.
- **Reddit/X-Direktzugriff** war blockiert (403); Reddit-Belege stammen aus einem lokal gespeicherten Dump (siehe 2.8) und sind ausschließlich Claimed.
- **DE/EU-Spezifika:** Die Shop-Dokumente gelten „United States"; EU-Creator-Terms (seller-de) wurden hier nicht auf AI-/Automatisierungsklauseln geprüft (Aufgabe W1).

---

## 4) Quellenliste (Zugriff 2026-09-24)

**TikTok-Primärquellen**
- Support „Creator Rewards Program" – https://www.tiktok.com/support/faq_detail?id=7581821550694013452 (Redirect von https://support.tiktok.com/en/business-and-creator/creator-rewards-program)
- Support „About AI-generated content" – https://www.tiktok.com/support/faq_detail?id=7636670084747893268
- Support „Manage topics" – https://www.tiktok.com/support/faq_detail?id=7636676986101996052
- Support „Likeness Detection for AI-generated content" – https://www.tiktok.com/support/faq_detail?id=7670780803776944661
- Support „Content violations and bans" – https://www.tiktok.com/support/faq_detail?id=7543604781940791864
- Support „Why is my account not being recommended?" – https://www.tiktok.com/support/faq_detail?id=7543604783110969862
- Support „Creator code of conduct" – https://www.tiktok.com/support/faq_detail?id=7543604783417137669
- Support „Creating an account" – https://www.tiktok.com/support/faq_detail?id=7581821549574052364
- Support „Email and phone number" – https://www.tiktok.com/support/faq_detail?id=7581820709597583928
- Support „This phone number is already registered" – https://www.tiktok.com/support/faq_detail?id=7078299664386103813
- Support „Account safety" – https://www.tiktok.com/support/faq_detail?id=7543604780950624824
- Support „Schedule video" – https://www.tiktok.com/support/faq_detail?id=7078299678101477893
- Support „TikTok Studio" – https://www.tiktok.com/support/faq_detail?id=7581820705491229240
- Support „Connect to third-party apps" – https://www.tiktok.com/support/faq_detail?id=7543604785694562872
- Community Guidelines, Integrity & Authenticity (Released 25.08.2026, Effective 24.09.2026) – https://www.tiktok.com/community-guidelines/en/integrity-authenticity
- Community Guidelines Overview – https://www.tiktok.com/community-guidelines/en/overview
- Terms of Service US (15.07.2026) – https://www.tiktok.com/legal/page/us/terms-of-service/en
- Terms of Service EEA/UK/CH (Juli 2026) – https://www.tiktok.com/legal/page/eea/terms-of-service/en
- Developer Terms of Service (26.12.2025) – https://www.tiktok.com/legal/page/global/tik-tok-developer-terms-of-service/en
- Content Posting API Get Started (04.08.2026) – https://developers.tiktok.com/doc/content-posting-api-get-started
- Content Sharing Guidelines (04.08.2026) – https://developers.tiktok.com/doc/content-sharing-guidelines
- Direct Post Reference (24.08.2026) – https://developers.tiktok.com/doc/content-posting-api-reference-direct-post
- Media Transfer Guide (04.08.2026) – https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide
- Newsroom 19.11.2025 – https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en
- Newsroom 09.05.2024 – https://newsroom.tiktok.com/en-us/partnering-with-our-industry-to-advance-ai-transparency-and-literacy
- Newsroom 19.09.2023 – https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content
- Newsroom DSA 6. Bericht 29.04.2026 – https://newsroom.tiktok.com/digital-services-act-our-sixth-transparency-report-on-content-moderation-in-europe?lang=en-150
- Transparency „Supporting responsible, transparent AI-generated content" – https://www.tiktok.com/transparency/en-us/supporting-responsible-transparent-ai-generated-content/
- Transparency „Promoting originality on TikTok" (Dez. 2025) – https://www.tiktok.com/transparency/en-us/ip-update-blog/
- Seller University US: AI-Generated Content Restrictions and Requirements (02.09.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=491489038501663&lang=en
- Seller University US: Requirements for High-Quality Videos and LIVEs (17.09.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=4581457528243969&lang=en
- Seller University US: Content Policy (17.09.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617&lang=en
- Seller University US: Creator Health Rating Overview (21.09.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=5054301796321070&lang=en
- Seller University US: Creator Enforcement Policy (31.07.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=6837869503317761&lang=en
- Seller University US: Creator Eligibility Policy (31.07.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=6939143037667118&lang=en
- Seller University US: Affiliate Marketing Policy (02.09.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=2244964886103809&lang=en
- Seller University US: Best Practices for Promotional Content (24.06.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=5769635937191681&lang=en
- Seller University US: TikTok Shop Creator Terms of Use (15.09.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=6314510387906350&lang=en
- Seller University US: What You Need to Know Before Becoming a TikTok Shop Creator (30.06.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=7608640301074219&lang=en
- Seller University US: Account Health Rating (AHR) Requirements (29.06.2026) – https://seller-us.tiktok.com/university/essay?knowledge_id=6750828276418350&lang=en

**Presse / Sekundär**
- 404 Media, Koebler, 30.07.2026 – https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/
- 404 Media, Maiberg, 17.12.2025 – https://www.404media.co/hack-reveals-the-a16z-backed-phone-farm-flooding-tiktok-with-ai-influencers/
- 404 Media, Koebler, 07.10.2024 – https://www.404media.co/ai-generated-pro-north-korean-tiktoks-are-also-bizarre-ads-for-supplements/
- 404 Media, Koebler, 05.03.2024 – https://www.404media.co/inside-the-world-of-tiktok-spammers-and-the-ai-tools-that-enable-them/
- Business Insider, Whateley, 20.07.2026 – https://www.businessinsider.com/tiktok-shop-creators-brands-using-ai-to-replace-human-slop-2026-7
- Mashable, Silva, 07.11.2025 – https://mashable.com/article/tiktok-shop-fake-products-ai
- eMarketer, Wolff, 15.07.2026 – https://www.emarketer.com/content/ai-reshapes-tiktok-shop-affiliate-playbook
- eMarketer (NYT-Zusammenfassung) – https://www.emarketer.com/content/ai-doctor-fakes-wellness-influencers-fuel-health-scam-ads-on-social-media
- WSJ (nicht abrufbar) – https://www.wsj.com/cmo-today/ai-videos-are-flooding-tiktok-shop-c86a88e0
- NYT (nicht abrufbar) – https://www.nytimes.com/2026/03/09/technology/ai-avatars-supplements-social-media.html
- Affiverse 17.07.2026 – https://www.affiversemedia.com/tiktok-shop-ai-generated-videos-affiliate-trust/ ; Rare Beauty – https://www.affiversemedia.com/rare-beauty-ai-tiktok-shop-affiliate-videos/ ; PPS – https://www.affiversemedia.com/tiktok-shop-pps-affiliate-content-visibility/
- Rest of World, Yulisman, 02.10.2025 – https://restofworld.org/2025/indonesia-tiktok-shop-livestream-sellers-ai-rivals/
- Modern Retail, Smith, 02.07.2026 – https://www.modernretail.co/marketing/marketplace-briefing-how-a-cartoon-frog-wizard-is-helping-clorox-sell-pine-sol-on-tiktok-shop/
- New York Magazine/Intelligencer (Doublespeed) – https://nymag.com/intelligencer/article/doublespeed-tech-founder-creating-an-army-of-ai-influencers.html
- TechCrunch, Malik, 18.11.2025 – https://techcrunch.com/2025/11/18/tiktok-now-lets-you-choose-how-much-ai-generated-content-you-want-to-see/
- Social Media Today, 19.11.2025 – https://www.socialmediatoday.com/news/tiktok-adds-option-to-limit-ai-content-in-your-for-you-feed/805952/
- TechTimes, 13.07.2026 – https://www.techtimes.com/articles/320282/20260713/tiktok-has-labeled-3-billion-ai-videos.htm
- Storrito (unbelegt) – https://storrito.com/resources/tiktok-removed-51000-ai-videos-creators-feeling-it/
- AdBeacon 27.07.2026 – https://www.adbeacon.com/tiktok-shop-account-health-rating-violation-points/ ; Allymatic 26.06.2026 – https://www.allymatic.com/en/academy/tiktok-shop-affiliate-dual-health-gate/ ; EcomCrew 26.08.2026 – https://www.ecomcrew.com/tiktok-shops-new-creator-score-ties-your-product-ratings-to-who-promotes-you/
- Later Blog – https://later.com/blog/tiktok-scheduler/ ; Metricool – https://metricool.com/schedule-tiktok/ ; Buffer – https://buffer.com/tiktok
- Reddit (aus lokalem Dump, nicht live geprüft): r/TikTokshop 1ugrszw (27.06.2026), 1r7h6jy (17.02.2026); r/TikTokShopSellers 1v7i0lp (26.07.2026); r/TikTokShopAffiliate 1sjw8xg (13.04.2026); r/passive_income 1rdiwob (24.02.2026); r/Bloggers 1p80o00 (27.11.2025); r/AI_ecommerce 1sl050c; u/GoLoginS 1uld6dl (02.07.2026)

---

## Verifikation (adversarial)

Prüfung am 2026-09-24 durch einen unabhängigen Fact-Check-Agenten. Alle fünf Primärquellen wurden **frisch und unabhängig** abgerufen (nicht aus den vorhandenen Scratchpad-Kopien): Support-FAQs über `www.tiktok.com/feedback/1/faq_detail_by_id/?faq_id=…&country=US&lang=en&app_id=1284&app_key=tiktok-web` (WebFetch der `faq_detail`-Seiten liefert nur den Titel „TikTok Support", da clientseitig gerendert); Community Guidelines aus dem `__remixContext`-JSON (URL-encodiert) der Seite; Seller University und Newsroom per curl. Jedes Zitat wurde per exakter String-Suche im dekodierten Quelltext gesucht. Verdikte: CONFIRMED / PARTIALLY / NOT_FOUND / CONTRADICTED.

| # | Regel | Verdikt | Prüfnotiz |
|---|---|---|---|
| 1 | AI-Label allein ändert die Distribution nicht (solange regelkonform) | **CONFIRMED** | Zitat wörtlich in FAQ 7636670084747893268 („About AI-generated content") als „Note:" unter der Anleitung zum Einschalten des AI-Settings. Kein Datumsfeld in der API-Antwort (`IsAITranslated: false`) → „undated" korrekt. Interpretation deckungsgleich; Einschränkung „as long as it doesn't violate our Community Guidelines" ist im Regeltext berücksichtigt. |
| 2 | TikTok Shop US: AI-Content wird nicht allein wegen AI-Nutzung/Label gedrosselt | **CONFIRMED** | Zitat wörtlich vorhanden. Seitenkopf: „AI-Generated Content Restrictions and Requirements 09/02/2026 Applies to: United States"; `modify_time` 1788372136 = 2026-09-02, konsistent. Zusätzlich belegt derselbe Text „Content will not be restricted or penalized solely for using AI" und die FAQ „Will my content be restricted if I enable the AI-generated content label? No…" – deckt beide Teile der Regel (AI-Nutzung + Label) ab. |
| 3 | Labelpflicht für realistische AIGC; ungelabelte Inhalte können entfernt/eingeschränkt werden; generische TTS-Stimme braucht kein Label | **CONFIRMED** | Beide Sätze wörtlich im Abschnitt „Edited Media and AI-Generated Content (AIGC)" (Zitat beginnt mitten im Satz nach „…what they are viewing,", inhaltlich unverändert). TTS-Ausnahme wörtlich: „Disclosure isn't needed when: … Using generic text-to-speech (TTS) narration, when the TTS isn't a recognizable voice of a known individual". Version `2026H2update`, `lastUpdate`: „Released August 25, 2026 Effective September 24, 2026" – für alle Abschnitte inkl. integrity-authenticity bestätigt. |
| 4 | Nutzer-Slider „see less/more AI-generated content" in Manage Topics; entfernt Inhalte nicht | **PARTIALLY** | Zitat wörtlich vorhanden, Datum 2025-11-19 bestätigt (`publishedDate` 2025-11-19). **Aber:** Der Newsroom-Text kündigt die Funktion nur als Test an: „In the coming weeks, we'll start testing a new AI-generated content control in our 'Manage topics' feature". Die Regel stellt den Slider als bestehendes Feature dar; die Support-FAQ „Manage topics" (7636676986101996052, frisch abgerufen) erwähnt AI/AIGC **nicht**. Ein Primärbeleg für den tatsächlichen (globalen) Rollout fehlt; „global" ist nur die Newsroom-Zuordnung, nicht belegt. Der Teil „entfernt Inhalte nicht" ist korrekt („rather than removing or replacing content in feeds entirely"). Formulierung „see less/more" ist Paraphrase („see more of this content … dial things down"). |
| 5 | Unsichtbare Wasserzeichen für AI-Content (TikTok-Tools + C2PA-Uploads); 1,3 Mrd. Videos gelabelt | **CONFIRMED** | Beide Zitate wörtlich, Datum 2025-11-19 bestätigt. Hinweis zur Einordnung: Wasserzeichen waren zum Zeitpunkt des Posts eine Ankündigung („Over the coming weeks, we'll start…"), kein Vollzug; die „1.3 billion" beziehen sich auf alle Label-Maßnahmen zusammen (Creator-Label, Detection-Modelle, C2PA) „to date" (Stand Nov. 2025), nicht auf Wasserzeichen. |
| 6 | Creator Rewards: nur selbst produzierter Original-Content; Slideshows/Text-Overlays/Loops/Werbung nicht rewards-fähig | **CONFIRMED** | Alle drei Zitatteile wörtlich in FAQ 7581821550694013452 („Creator Rewards Program"). „looping videos, single or multiple photos, or only text overlays" steht in der Liste „Content not considered original under the program includes, but is not limited to:"; „Advertisements, paid promotions, sponsored content…" in der Liste nicht zulässiger Videos. Kein Datumsfeld → „undated" korrekt. „global (eligible countries)": FAQ verlangt „Be based in one of the countries where the Creator Rewards Program is available", Länderliste nicht in der FAQ → Zusatz korrekt vorsichtig. |
| 7 | Creator Rewards: Verbot von Fake-Views/Bots/Manipulation des Empfehlungssystems | **CONFIRMED** | Zitat wörtlich; flankiert von „No engagement in malicious or fraudulent activities, such as acquiring fake video views or inflating follower counts" und „Must not tamper or attempt to tamper with the program, the reward system, or the recommendation system" (beide wörtlich vorhanden). Interpretation gedeckt. |
| 8 | Unoriginaler/wiederverwendeter Content ist FYF-ineligible | **CONFIRMED** | Zitat wörtlich im Unterabschnitt „Unoriginal Content and Intellectual Property Rights" (`2026-H2-integrity-subpost4`). Effective September 24, 2026 bestätigt. Interpretation gedeckt. |
| 9 | Automatisierungstools/Skripte zum Umgehen der Systeme strikt verboten; Konsequenz Bans auch für neue Accounts, FYF-Restriktion | **CONFIRMED** | Zitat wörtlich im Unterabschnitt „Deceptive Behaviors and Fake Engagement". „Ban additional or new accounts you create" / „Restrict your account … in the FYF" stehen im unmittelbar vorangehenden Satz zu „deceptive account behavior", nicht im Automations-Satz selbst – die Regel fasst beides zulässig zusammen. Wichtig für die Auslegung: Verboten sind Tools „designed to bypass our systems", nicht Automatisierung per se (Content Posting API/Scheduler bleiben davon unberührt) – die Regel formuliert das korrekt („zum Umgehen der Systeme"). |
| 10 | Spam-Definition: Automatisierung vieler Accounts, Bots für Likes/Reviews, AI-/Bot-Accounts für Traffic, Engagement-Kauf und Anleitungen dazu | **PARTIALLY** | Alle vier Zitatfragmente wörtlich vorhanden, Datum bestätigt. **Aber** die Überschrift „Spam-Definition" ist strukturell ungenau: Nur „Using automation to run many accounts…", „Buying or selling followers or engagement for financial gain" und „Using bots or scripts to write fake reviews…" stehen unter „Spam, such as:". „Using AI or bot accounts to drive traffic" und „Sharing how-to guides or tips for boosting engagement…" stehen unter dem separaten Punkt „Trading, marketing, or providing access to services that artificially increase engagement, such as:" (gleicher NOT-ALLOWED-Block des Abschnitts „Deceptive Behaviors and Fake Engagement"). Inhaltlich alles verboten; Etikett sollte „Deceptive Behaviors & Fake Engagement (Spam + Engagement-Dienste)" lauten. |

**Gesamtbefund:** 8× CONFIRMED, 2× PARTIALLY (Nr. 4: Slider im Quelltext nur als angekündigter Test, Rollout nicht primär belegt; Nr. 10: Zuordnung „Spam" für zwei der vier Punkte falsch), 0× NOT_FOUND, 0× CONTRADICTED. Kein Zitat ist erfunden oder sinnentstellend gekürzt; alle Daten (undatiert / 09/02/2026 / Released 25.08.2026–Effective 24.09.2026 / 19.11.2025) stimmen mit den Quellen überein.
