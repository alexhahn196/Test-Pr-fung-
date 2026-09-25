# TikTok Plattformregeln: AI-generierte Inhalte (AIGC), Automatisierung, Spam, Mehrfach-Accounts

Stand der Recherche: 2026-09-24 (alle Zugriffe an diesem Tag). Perspektive: Due-Diligence, nicht Marketing.
Quellenlage: Die Community Guidelines (CG) wurden am 25.08.2026 veröffentlicht und sind **seit heute (24.09.2026) wirksam** ("Released August 25, 2026 / Effective September 24, 2026"). Alle CG-Zitate stammen aus dieser aktuellen Version (Website-Payload dekodiert, da die Seiten clientseitig gerendert werden). Support-Artikel wurden über den offiziellen Help-Center-Endpunkt (`/feedback/1/faq_detail_by_id/`) gelesen, weil die HTML-Seiten reine JS-Shells sind; die Artikel tragen **kein sichtbares "zuletzt aktualisiert"-Datum**.

Tag-Legende: **Verified** = im Primärdokument selbst gelesen. **Claimed** = nur Sekundärquelle.

---

## 1) Kurzfazit

- **Labelpflicht:** Realistisch wirkende AI- oder stark bearbeitete Inhalte (Personen/Szenen) müssen gekennzeichnet werden (TikTok-AIGC-Label ODER eigene klare Caption/Sticker/Wasserzeichen). Nicht nötig bei Farbkorrektur/Crop, Anime-Stil und generischem TTS ohne erkennbare echte Stimme. Ungelabelte Inhalte "may be removed, restricted, or labeled by our team, depending on the harm it could cause". (CG, Verified)
- **Verboten (auch mit Label):** Likeness privater Personen ohne Einwilligung, alle Minderjährigen, sexualisierte/mobbende AI-Likenesses, AIGC, das über Themen von öffentlichem Interesse täuscht (fake News-Quelle, Krisenereignis, Public Figure mit erfundenem Endorsement/Produktwerbung/politischer Aussage). Realistische, noch nicht bestätigte AIGC zu Themen von öffentlichem Interesse ist FYF-ineligible. (CG, Verified)
- **Reichweite:** Das Setzen des AI-Labels "won't affect the distribution of your video as long as it doesn't violate our Community Guidelines" (Support, Verified). ABER: Seit Nov. 2025 gibt es den Nutzer-Regler "AI-generated content" in *Manage topics* (Settings > Content preferences), mit dem Zuschauer weniger/mehr AIGC im For-You-Feed sehen können (Newsroom 24.11.2025 + AI Literacy Guide, Verified; "isn't available everywhere"). Zusätzlich: unsichtbare Wasserzeichen + C2PA-Content-Credentials → Auto-Label, das der Creator nicht entfernen kann.
- **FYF-ineligible:** Wiederverwendete/unoriginale Inhalte ohne kreative Bearbeitung (z. B. fremdes Wasserzeichen/Logo), Low-Quality/minimal bearbeitet (z. B. nur GIF-Clips), Engagement-Bait ("like-for-like"), realistische unbestätigte AIGC zu Public-Interest-Themen. Accounts, die wiederholt FYF-ineligible Inhalte posten, werden **als ganzer Account** aus dem FYF genommen und in der Suche schwerer auffindbar. (CG + Support, Verified)
- **Mehrere Accounts & Automatisierung:** Mehrere Accounts sind erlaubt ("You can have multiple accounts … but not to deceive others or break the rules"); eine Zahl pro Gerät nennt keine Primärquelle. Jede Telefonnummer/E-Mail/Social-Login kann nur mit **einem** Account verknüpft sein. "Using automation to run many accounts or send repetitive content" ist Spam; "automation tools, scripts, or other tricks designed to bypass our systems" sind strikt verboten. Automatisiertes Posten ist nur über die offizielle Content Posting API zulässig: unauditierte Clients dürfen nur **privat (SELF_ONLY)** posten, max. 5 Nutzer/24 h; auch auditierte Clients haben ein Posting-Cap (~15 Posts/Tag/Creator); reine "Upload-Utility für eigene Accounts" wird im Audit explizit als "Not acceptable" genannt. (CG, ToS, Dev-Docs, Verified)

---

## 2) Regel-für-Regel mit Zitatblock, URL, Datum, Tag

### 2.1 Community Guidelines – Edited Media and AI-Generated Content (AIGC)

**Quelle:** https://www.tiktok.com/community-guidelines/en/integrity-authenticity — Released August 25, 2026, Effective September 24, 2026 — Jurisdiktion: global (US-Version, "en") — **Verified**

**Grundregel + Enforcement-Hinweis**
> "We welcome creativity, including when it comes from new digital tools like generative artificial intelligence (AI). But generative AI and editing can blur the line between fact and fiction. To help keep content on TikTok trustworthy and provide people with important context about what they are viewing, we require creators to label AI-generated or significantly edited content that shows realistic-looking scenes or people. Unlabeled content may be removed, restricted, or labeled by our team, depending on the harm it could cause.
> Even with labels, some edited or AI-generated content can still be harmful. We don't allow content that's misleading about matters of public importance or harmful to individuals."

**Definitionen ("More information")**
> "AI-Generated Content (AIGC): Any image, video, or audio made or changed by AI. This can include realistic scenes or artistic styles, like anime, cartoons, or paintings.
> Significantly Edited Content: Media that makes it seem like someone did or said something they didn't, or alters their appearance so much that they're unrecognizable. This includes:
> - Cropping or cutting phrases to change meaning
> - Rearranging or combining clips
> - Changing speed or adding/removing audio or video parts
> Realistic-Appearing Scenes or People: Content that looks like it could be real, such as AI-generated images that look like real photographs or footage.
> Likeness: A recognizable image, video, or audio representation of a person, including their face, body, voice, and gestures.
> Public Figures: People 18 and older with a significant public role, such as a government official, politician, business leader, or celebrity. We don't identify people under 18 as public figures.
> Private Figures: All people under 18, and adults who aren't public figures."

**REQUIRED DISCLOSURE (using the AIGC label or a clear caption, watermark, or sticker)**
> "You must label content that uses AI or includes significant edits to show realistic-looking people or scenes. You can add your own clear caption, sticker, or watermark. For AI-generated content, you can also use our AIGC label.
> Disclosure is needed when content isn't harmful but could be confusing, including when:
> - A face is replaced with someone else's
> - AI tools make it look like someone said something they didn't
> - A background, object, or person is added or removed in a misleading way
> - AI-generated audio mimics the voice of a real person
> Disclosure isn't needed when:
> - Making small edits like color correction, reframing, or cropping
> - Using artistic styles, like anime
> - Using generic text-to-speech (TTS) narration, when the TTS isn't a recognizable voice of a known individual"

**NOT ALLOWED**
> "- Using the likeness of private figures without consent
> - Sexualized, fetishized, or victimizing depictions
> - AI-created likenesses made to bully or harass
> - Accounts focused on AI images of youth in clothing suited for adults, or sexualized poses or facial expressions
> - AIGC or significantly edited content that misleads about a matter of public importance, such as:
>   - Content made to look like it comes from a real news source
>   - A crisis event, like a natural disaster or conflict
>   - A public figure being degraded, harassed, or linked to criminal behavior
>   - A public figure taking political stances, supporting products, or commenting on public issues they haven't actually addressed
>   - A political endorsement or condemnation that never happened
> - Any content that breaks our Community Guidelines, including those on impersonation, misinformation, and hate speech, even if it's AI-generated"

**FYF INELIGIBLE**
> "- Any realistic-appearing content which isn't yet confirmed to be AIGC or significantly edited content, but presents matters of public importance in a way that could lead to misinterpretation, or cause harm to private figures"

**ALLOWED**
> "- Humor or art, such as a spoof, meme, or TikTok dance"

Einordnung (Analyst): Für AI-Avatar-/AI-Voice-Produktvideos ist damit (1) ein Label Pflicht, sobald Personen/Szenen realistisch wirken; (2) das Nachahmen der Stimme/des Gesichts realer Personen (auch Prominenter, die ein Produkt "empfehlen") verboten; (3) generisches TTS ohne erkennbare Stimme ist labelfrei.

### 2.2 Community Guidelines – Unoriginal Content and Intellectual Property Rights

**Quelle:** wie 2.1 — **Verified**
> "You should only post content you created or have the right to share. We don't allow content that violates someone else's intellectual property (IP) rights. If we become aware of content that breaks these rules, we will remove it. […]
> Content is also ineligible for the FYF if it includes unoriginal or reused material without anything new."

NOT ALLOWED:
> "- Content that violates someone else's copyrights, trademarks, or other IP rights"

FYF INELIGIBLE:
> "- Reused or unoriginal content posted without creative edits, such as clips that show someone else's watermark or logo
> - Low-quality or minimally edited content, such as short clips made from GIFs only"

Hinweis: Begriffe wie "mass produced" oder "repetitive" kommen in der aktuellen CG-Version **nicht wörtlich** vor; das Konzept wird über "unoriginal/reused without anything new", "low-quality or minimally edited" und in der Spam-Definition über "send repetitive content" / "Posting a large amount of irrelevant material" abgedeckt.

### 2.3 Community Guidelines – Deceptive Behaviors and Fake Engagement (Spam, Automatisierung, Mehrfach-Accounts)

**Quelle:** wie 2.1 — **Verified**
> "That's why we don't allow accounts that mislead or try to manipulate our platform, or the trade of services that artificially boost engagement or trick the recommendation system. This includes behaviors like covert influence operations, impersonation, spam, fake reviews, and sharing hacked materials in harmful ways. You can have multiple accounts—for example, for fan content or creative expression—but not to deceive others or break the rules. If we find deceptive account behavior, we may:
> - Ban your account
> - Ban additional or new accounts you create
> - Restrict your account, which could include limiting your ability to post new content, appear in top search results, or in the FYF
> We strictly prohibit automation tools, scripts, or other tricks designed to bypass our systems. These can result in content removal, account bans, or other enforcement. If your account is restricted or banned, you may not create or use another account to get around it.
> If we detect accounts or content with inauthentic metrics, we'll remove fake likes, followers, or other inflated signals. Content that tries to manipulate people into giving gifts or inflating likes or follows isn't eligible for the FYF."

NOT ALLOWED (Auszug, Spam/Automation/Umgehung):
> "- Spam, such as:
>   - Using automation to run many accounts or send repetitive content
>   - Posting a large amount of irrelevant material
>   - Buying or selling followers or engagement for financial gain
> - Using bots or scripts to write fake reviews or comments, or to increase likes or shares
> - Impersonation by pretending to be someone else without clearly stating that the account is a fan or parody account in the display name
> - Pretending to be a fake person or organization with the goal of misleading people
> - Circumvention of our policies, which includes:
>   - Spreading violative content across multiple accounts
>   - Using a different account to continue violating policies after being banned
>   - Returning to TikTok after being permanently banned for severe violations
>   - Using another account to avoid restrictions, such as comment blocks or FYF-ineligible content restrictions
> - Trading, marketing, or providing access to services that artificially increase engagement, such as:
>   - Followers or likes
>   - Fake reviews
>   - Using AI or bot accounts to drive traffic
> - Sharing how-to guides or tips for boosting engagement in fake or deceptive ways"

FYF INELIGIBLE:
> "- Tricking others into increasing engagement, such as:
>   - "Like-for-like" promises
>   - False incentives for gifting or following
>   - Misleading claims meant to boost views or popularity"

### 2.4 Community Guidelines – Platform Security (nicht autorisierter Zugriff, automatisierte Tools)

**Quelle:** https://www.tiktok.com/community-guidelines/en/ (Abschnitt Privacy and Security > Platform Security; identischer Payload) — **Verified**
NOT ALLOWED:
> "- Giving someone else your login information or letting them break TikTok's rules on your account
> - Using unauthorized ways to access TikTok or creating fake versions of the platform
> - […]
> - Trying to steal personal information, hack accounts, or access data using tricks like phishing, smishing, or automated tools
> - Trying to reverse-engineer TikTok's code, systems, or algorithms—or create your own versions based on them"

### 2.5 Community Guidelines – For You feed Eligibility Standards

**Quelle:** https://www.tiktok.com/community-guidelines/en/fyf-standards — Released August 25, 2026 / Effective September 24, 2026 — **Verified**
> "We maintain content eligibility standards for the FYF that prioritize safety, and are informed by the diversity of our community and cultural practices. […] We make ineligible for the FYF certain content that may not be suitable for a broad audience. Learn more about the types of content we leave out from the FYF in the "FYF Ineligible" sections throughout our Community Guidelines.
> Even if a video doesn't make it to the FYF, people may still find it through search or by going to a creator's account. If a video isn't getting many views, it also doesn't necessarily mean it broke a rule. Creators can check TikTok's analytics to see how their videos are performing, including if there were any made ineligible for recommendation.
> Our recommendation system is built to help people discover and enjoy a wide range of content—not just the same kinds of videos over and over. We aim to prevent our systems from repeatedly recommending content that could lead to a negative experience […]"

Overview-Box (https://www.tiktok.com/community-guidelines/en/):
> "The For You Feed is designed to help you discover a variety of content and creators […] However, not all content is guaranteed to be recommended. When we identify content that falls under the "FYF Ineligible" standards in our Community Guidelines, it won't be recommended in the FYF."

### 2.6 Community Guidelines – Accounts (Enforcement-Leiter auf Account-Ebene)

**Quelle:** https://www.tiktok.com/community-guidelines/en/ (Accounts and Features > Accounts) — Released August 25, 2026 / Effective September 24, 2026 — **Verified**
> "We'll also take action if someone breaks our Community Guidelines. That can mean a warning, temporary feature or account restriction, or a full account ban, depending on what happened. In some cases, users may be given the opportunity to complete optional policy training to restore full access to the platform.
> We may ban an account or user for:
> - Repeated rule violations
> - A single, severe violation
> - Trying to avoid enforcement
> - Running accounts that are dedicated to breaking the rules, like spreading hate, the unauthorized trading of regulated, prohibited (e.g. counterfeit), or high-risk goods, or inauthentic behavior (e.g. pretending to be someone else)
> If someone seriously breaks the rules or tries to dodge enforcement, we may ban all of their accounts, including associated accounts.
> […]
> Sometimes, accounts that don't break the rules still post a lot of content that's ineligible for the FYF. In those cases, we may make the account and its content ineligible for the FYF and harder to find."

### 2.7 Community Guidelines – Enforcement (Public-Interest-Ausnahmen, Detection, Appeals)

**Quelle:** https://www.tiktok.com/community-guidelines/en/enforcement — Released August 25, 2026 / Effective September 24, 2026 — **Verified**
> "Even if we allow content under a public interest exception, we might still:
> - Make it ineligible for the FYF
> - Add a warning screen
> - Add a context label"

> "We aim to remove content or accounts that violate our rules before they are viewed or shared. Content first goes through an automated review process. If content is identified as a potential violation, it will be automatically removed, or flagged for additional review by our moderators. Additional review will occur if content gains popularity or has been reported."

> "If your content breaks a rule, we seek to explain to you why it was removed. If your account is banned, you'll see a message in the app. If your content is made ineligible for the FYF or otherwise restricted, this information will appear in the TikTok analytics tool.
> If your account was banned, or your content was removed, made ineligible for the FYF, or otherwise restricted, and you believe this was an error, you may appeal the decision."

Overview-Boxen (https://www.tiktok.com/community-guidelines/en/):
> "Everyone on TikTok can share content, but when we identify content that falls under the "Not Allowed" rules in our Community Guidelines, we'll remove it."
> "Some content may not be appropriate for people under 18. When we identify content that falls under the "Age-Restricted" standards in our Community Guidelines, we make it viewable only for adults."

### 2.8 Help Center – "About AI-generated content"

**Quelle:** https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content (leitet auf https://www.tiktok.com/support/faq_detail?id=7636670084747893268 weiter) — kein Datum auf der Seite — global (en) — **Verified**

Definition/Beispiele:
> "AI-generated content (AIGC) includes images, video and/or audio that is generated or modified by artificial intelligence, such as artificial visuals, videos, or sounds that may portray realistic human likenesses or depictions created in a particular artistic style (e.g. painting, cartoons, and anime).
> Examples of AI-generated content include the following:
> • Video featuring a real person speaking, whose image, voice, and/or words are altered or modified by AI.
> • Video or image featuring a scene or event that occurred in the real world, but has been altered or modified by AI.
> • Entirely AI-generated videos or images of real or fictional people, places, and events."

Anforderungen ("significantly edited" = über kleine Korrekturen hinaus):
> "To support authentic and transparent experiences for our community, we encourage creators to label content that has been either completely generated or significantly edited by AI. We consider content that's significantly edited by AI as that which uses real images/video as source material, but has been modified by AI beyond minor corrections or enhancements, including synthetic images/video in which:
> • The primary subjects are portrayed doing something they didn't do, for example, dancing.
> • The primary subjects are portrayed saying something they didn't say, for example, AI-generated speech.
> • The appearance of the primary subject(s) has been substantially altered, such that the original subject(s) is no longer recognizable, for example, with an AI face-swap.
> We also require creators to label all AI-generated content that contains realistic images, audio, and video, as explained in our Community Guidelines."

Labelarten, Auto-Label (C2PA), Nicht-Entfernbarkeit, Missbrauch des Labels:
> "Creator label: Creators apply this label to indicate that their content was completely generated or significantly edited by AI. The label will read "creator labeled as AI-generated". Please note that misleadingly labeling unaltered content with this label is a violation of our Terms of Service and may result in the removal of content.
> Keep in mind that if you made your AI-generated content using only TikTok effects, you may not need to label it as we automatically label content made with TikTok effects if they use AI. […]
> Auto label: TikTok may automatically apply the "AI-generated" label to content we identify as completely generated or significantly edited with AI. This may happen when a creator uses TikTok AI effects or uploads AI-generated content that has Content Credentials attached, a technology from the Coalition for Content Provenance and Authenticity (C2PA). […]
> Note: Once your content is labeled as AI-generated with an auto label, you won't be able to remove the label from your post."

Verbotene AIGC + Enforcement:
> "Some AI-generated content or edited media can still cause harm, even if properly labeled. We do not allow AI-generated content that shows:
> • Fake authoritative sources or crisis events, or falsely shows public figures in certain contexts. This includes being bullied, making an endorsement, or being endorsed.
> • The likeness of young people under the age of 18, or the likeness of adult private figures used without their permission."
> "We may remove content that violates our Community Guidelines policies by depicting misleading information or unlabeled AI-generated content."

**Reichweite bei gesetztem Label (zentrale Aussage):**
> "Note: Turning on the AI-generated content setting won't affect the distribution of your video as long as it doesn't violate our Community Guidelines."

### 2.9 Help Center – "Content violations and bans" (Strikes, 90 Tage, Permanent-Ban)

**Quelle:** https://support.tiktok.com/en/safety-hc/account-and-user-safety/content-violations-and-bans (→ faq_detail?id=7543604781940791864) — kein Datum — **Verified**
> "If your TikTok content is under review, it will be reviewed by our Trust and Safety team to determine whether it should be removed or made ineligible for the For You feed according to our Community Guidelines. This may happen when you upload content, if it gains popularity, or if it's reported."
> "The first time your content is removed because of a Community Guidelines violation, you'll receive a warning strike on your account. […] Keep in mind that if your first violation is severe, this won't apply and you'll receive a strike instead of a warning. We may also ban your account.
> Our system counts the number of times your account has violated our Community Guidelines, and for each violation after your first warning, you'll receive a strike on your account.
> We count strikes by policy area as listed in our Community Guidelines (for example, safety and civility) or by feature (for example, comments or direct messages). Your account will receive a strike based on the severity of the policy violation. We'll count the strikes until your account reaches the threshold for a permanent account ban. We'll notify you of any consequences of violations, including if you're on the verge of being banned."
> "Strikes on your TikTok account will expire after 90 days and will no longer be taken into consideration for a permanent account ban."
> "We may permanently ban accounts if we identify the following violations […] including:
> • You don't meet the minimum age or other requirements as indicated in our Terms of Service.
> • The account impersonates another person or entity in a deceptive manner.
> • You have a severe violation on your account: […]
> • Create or use another TikTok account to intentionally avoid restrictions or a permanent ban imposed on another account.
> • Your account has reached the strike threshold for multiple violations within a policy or feature.
> • Multiple violations of our Intellectual Property Policy.
> • Your account exists solely to violate our rules."
> "Note: Deleting your content does not remove strikes, and we may still issue strikes after you delete violative content."
> "Can you create a new TikTok account after a ban?
> You can create multiple accounts on TikTok. However, we may restrict or permanently ban your account if you make any attempts to avoid a restriction or ban imposed on another account you own, including:
> • Create a new account after your account has been banned for a severe violation.
> • Post violative content on a new or existing account.
> • Spread content violations across multiple accounts.
> This applies for as long as the restriction remains active on your other account."

Hinweis: Die konkrete **Strike-Schwelle** (Anzahl bis Permanent-Ban) wird in der Primärquelle **nicht beziffert** ("threshold").

### 2.10 Help Center – "Why is my account not being recommended?" (Account-weite FYF-Ineligibility)

**Quelle:** https://support.tiktok.com/en/safety-hc/account-and-user-safety/why-is-my-account-not-being-recommended (→ faq_detail?id=7543604783110969862) — kein Datum — **Verified**
> "If you repeatedly post content that is unsuitable for the For You feed, your account and posts won't appear in the For You feed and will be harder to find in search.
> We may automatically restore your account to good standing at any time, depending on how much content on your account isn't suitable for the For You feed. Otherwise, you can submit an appeal."
> "If your account becomes ineligible for recommendation, we'll notify you in your inbox notifications and profile […]"

### 2.11 Help Center – "Your account status" (Account check)

**Quelle:** https://support.tiktok.com/en/safety-hc/account-and-user-safety/account-status (→ faq_detail?id=7543604781319756294) — kein Datum — **Verified**
> "You can review the following account issues:
> • Login: Restricted from logging in
> • Posts: Restricted from posting
> • Comments: Restricted from commenting
> • Profile: Restricted from editing your profile
> • Direct messages: Restricted from sending messages"
> "You can check the status of your account from TikTok Studio and the Safety Center. […] Within More tools, tap Account check."

### 2.12 Help Center – "Creating an account" (Mehrere Accounts, Gerät, Login-Bindung)

**Quelle:** https://support.tiktok.com/en/getting-started/creating-an-account/creating-an-account (→ faq_detail?id=7581821549574052364) — kein Datum — **Verified**
> "• Each phone number, email address, and social media account can only be linked to one TikTok account."
> "How to add or switch between accounts
> You can add additional accounts to your device and switch between them on TikTok.
> To add or switch between accounts:
> 1. In the TikTok app, tap Profile at the bottom.
> 2. Tap your nickname.
> 3. Tap Add account to create another TikTok account, or choose to switch accounts."

**Nicht in Primärquelle auffindbar:** eine konkrete Höchstzahl von Accounts pro Gerät/Telefonnummer. Ein eigener Help-Center-Artikel "Multiple accounts" existiert unter der vorgegebenen URL nicht mehr (die Navigation des Help Centers enthält keinen solchen Eintrag; der Inhalt ist in "Creating an account" aufgegangen). Sekundärquellen nennen häufig ein In-App-Limit von drei Accounts pro Gerät – **Claimed**, hier nicht verifiziert.

### 2.13 Help Center – "Manage topics" und AI Literacy Guide (Nutzer-Regler für AI-Inhalte)

**Quelle A:** https://support.tiktok.com/en/account-and-privacy/account-privacy-settings/manage-topics (→ faq_detail?id=7636676986101996052) — kein Datum — **Verified**
> "You can tailor your For You feed to see more or less content from creators outside of your followed accounts. Content is categorized by topic (sports, food & drinks, lifestyle, etc.) and you can customize each topic based on your preference."
> "3. Tap Content preferences, then tap Manage topics.
> 4. Move the slider to adjust how much you want to see of each topic."
> "The preference you set on different topics only applies to content in your For You feed—other areas of TikTok are not affected, such as your Following feed, profile, and inbox."
(Der Artikel nennt AIGC nicht ausdrücklich als Topic.)

**Quelle B:** AI Literacy Guide, https://www.tiktok.com/safety/en/tools-and-guides/ai-literacy-guide — kein Datum sichtbar — **Verified**
> "Managing your AI experience
> You can control how much AI-generated content shows up in your feed by managing your topics on TikTok. You can use the AI-Generated Content setting in "Manage topics" to help you choose whether you want to see more or less AIGC. Keep in mind that this feature isn't available everywhere.
> You can also set up keyword filters to block specific AI-related words. Additionally, you can tap Not interested on any post to tell us what to skip next time."
> "On TikTok:
> - For transparency, we require you to label AIGC that shows realistic-looking scenes or people.
> - Depending on the harm that unlabeled content may cause, we may remove it, make it ineligible for the For You feed, or label it to meet our rules."
> "When you upload content, we will scan it for watermarks and signals to determine if an AI-generated label will be automatically applied. If not, you'll see an option to label the content as AI-generated.
> If your content features realistic AI-generated images, audio, or video of people, places, or events, you must use an AIGC label - either TikTok's label or your own clearly visible caption, sticker, or watermark.
> A label is also required when AI tools put together real images and/or videos of a critical event."

### 2.14 Newsroom – Zeitleiste der AI-Label-Maßnahmen

**(a) 19.09.2023 – "New labels for disclosing AI-generated content"**
https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content — **Verified**
> "This week, we will begin launching a new tool to help creators label their AI-generated content. We'll also start testing ways to label AI-generated content automatically."
> "The policy requires people to label AI-generated content that contains realistic images, audio or video, in order to help viewers contextualize the video and prevent the potential spread of misleading content. Creators can now do this through the new label (or other types of disclosures, like a sticker or caption)."
> "This week, we will begin testing an "AI-generated" label that we eventually plan to apply automatically to content that we detect was edited or created with AI."

**(b) 09.05.2024 – "Partnering with our industry to advance AI transparency and literacy" (C2PA)**
https://newsroom.tiktok.com/en-us/partnering-with-our-industry-to-advance-ai-transparency-and-literacy — **Verified**
> "TikTok is starting to automatically label AI-generated content (AIGC) when it's uploaded from certain other platforms. To do this, we're partnering with the Coalition for Content Provenance and Authenticity (C2PA) and becoming the first video sharing platform to implement their Content Credentials technology."
> "[…] we label AIGC made with TikTok AI effects, and have required creators to label realistic AIGC for over a year. We also built a first-of-its-kind tool to make this easy to do, which over 37 million creators have used since last fall."
> "Content Credentials attach metadata to content, which we can use to instantly recognize and label AIGC. This capability started rolling out today on images and videos, and will be coming to audio-only content soon.
> Over the coming months, we'll also start attaching Content Credentials to TikTok content, which will remain on content when downloaded."

**(c) 24.11.2025 (Seitendatum; TechCrunch berichtete am 18.11.2025) – "More ways to spot, shape and understand AI-generated content"**
https://newsroom.tiktok.com/en-gb/more-ways-to-spot-shape-and-understand-ai-generated-content — **Verified** (nur in der en-gb-Ausgabe abrufbar; der en-us-Slug fällt auf die Newsroom-Startseite zurück)
> "In the coming weeks, we'll start testing a new AI-generated content control in our 'Manage topics' feature to empower people to choose how much AIGC they want to see in their For You feeds.
> Manage Topics already enables people to adjust how often they see content related to over 10 categories like Dance, Sports, and Food & Drinks. Like those controls, the AIGC setting is intended to help people tailor the diverse range of content in their feed, rather than removing or replacing content in feeds entirely. This means that people who love AI-generated history content can see more of this content, while those who'd rather see less can choose to dial things down."
> "To bolster our AI-generated content labels, we're also testing a solution called "invisible watermarking."
> We require people to label realistic AI-generated content on TikTok and layer multiple strategies to apply that rule. This includes labeling tools we offer creators as well as our own detection models. We also use a cross-industry technology called C2PA Content Credentials […] These efforts helped label over 1.3 billion videos to date."
> "However, a common industry challenge is that these kinds of labels may be removed when content is reuploaded or edited elsewhere. "Invisible watermarks" add another layer of safeguards with a robust technological "watermark" that only we can read, making it harder for others to remove.
> Over the coming weeks, we'll start adding invisible watermarks to AI-generated content made with TikTok tools like AI Editor Pro, and content uploaded with C2PA Content Credentials."
> "Now, we're launching a $2M AI literacy fund for experts like GirlsWhoCode to create For You feed content that teaches people about AI literacy and safety."
> "For example, over the last year, we enhanced our AIGC labels by adding more context around whether content was labeled due to our AI detection, creator labels, or TikTok AI tools."

Sekundärquelle (Claimed, deckungsgleich): TechCrunch, 18.11.2025, https://techcrunch.com/2025/11/18/tiktok-now-lets-you-choose-how-much-ai-generated-content-you-want-to-see/ — "You can access the new capability by going into Settings > Content Preferences > Manage Topics. […] The change is rolling out in the coming weeks, TikTok says."

**(d) Newsroom-Posts 2026 zu AI-Labels:** Nicht in Primärquelle auffindbar. Die Newsroom-Kategorieseiten werden clientseitig geladen; Sitemap/RSS sind nicht erreichbar (404/Redirect). Eine gezielte Suche war wegen ausgeschöpftem Suchkontingent nicht möglich. Die aktuelle CG-Version (Aug./Sept. 2026) ist die maßgebliche Primärquelle für den Stand 2026.

### 2.15 Transparency Center – "Supporting responsible, transparent AI-generated content" und "Identifying content made with TikTok AI Tools"

**Quelle A:** https://www.tiktok.com/safety/en/transparency/supporting-responsible-transparent-ai-generated-content — kein Datum sichtbar — **Verified**
> "We require creators to label AIGC that shows realistic-appearing scenes or people, and were the first content sharing platform to build a tool that helps them do this easily. We also prohibit AIGC that could mislead viewers about the truth of real world events, including content that was misleadingly edited or taken out of context, shows fake authoritative sources or crisis events, or falsely shows public figures who are being bullied, or impersonated, including making an endorsement, or being endorsed.
> In line with our commitment to protecting peoples' privacy, we do not allow content that contains the likeness of people under the age of 18, or the likeness of adult private figures used without their permission."
> "We detect AI-generated content through a combination of proactive technologies, alerts from experts and fact-checking partners, searches for clips or keywords related to known AI-generated content, and user reports."
> "In addition to providing a tool for our creators to easily label their own AIGC uploaded to TikTok, we automatically label AIGC made with TikTok AI effects. We also label AIGC from certain other platforms by using Content Credentials […]"

**Quelle B:** https://www.tiktok.com/safety/en/transparency/ai-content-identification — kein Datum sichtbar — **Verified**
> "On TikTok, we require users to label realistic AI-generated content, and build three layers of AI transparency into creation features by design: visible labels, C2PA Content Credentials, and our proprietary invisible watermarks. However, sometimes, content may be downloaded, edited or viewed off TikTok without its on-platform label. This tool provides further transparency into content made with our AI tools, by letting you search for C2PA Content Credentials and invisible watermarks within the content itself."
> "- Invisible watermarks: Watermarks embedded directly into the content, which are robust and harder for people to remove."

### 2.16 Terms of Service – USA

**Quelle:** https://www.tiktok.com/legal/page/us/terms-of-service/en — "Last updated: July 15, 2026" — Jurisdiktion: USA (Vertragspartner "TikTok USDS Joint Venture") — **Verified**

Abschnitt 3.4 "What you can't do on the Platform" (Auszug):
> "For example, you must not use, or help anyone else use, the Platform to:
> - do anything misleading or harmful,
> - […]
> - reverse engineer, disassemble, or decompile the Platform or any of its components, including its algorithms, code, or infrastructure, without explicit written authorization from TikTok USDS Joint Venture,
> - engage in inauthentic commercial behaviors, such as by operating spam or impersonation accounts or any other means further detailed in our Community Guidelines,
> - […]
> - scrape, crawl, export or otherwise extract any data or content in any form, for any purpose, from the Platform using any automated system or software, including automated "bots," except as approved in writing by TikTok USDS Joint Venture,
> - use or attempt to use another user's account without authorization,
> - use TikTok Content (as defined in Section 3.5), another user's content or generative AI-enabled features for commercial purposes unless permitted by TikTok USDS Joint Venture or the user, respectively (including via applicable account settings),"

Abschnitt 3.10 "Using our generative AI features" (Auszug, Bullet):
> "- Use generative AI-enabled features via any automated system or software, including automated "bots," unless otherwise authorized,"
> "- Provide, create, or otherwise use Input or Output in a fraudulent manner or to deceive, mislead or impersonate others,"

Moderation / Umgehung nach Ban (Klausel im US-ToS; Abschnittsnummer nicht separat geprüft):
> "You agree that we can use automated tools and human moderators to review Your Content (as defined in Section 3.5) and associated metadata on the Platform, to identify, detect, and enforce potential or actual violations of these Terms, our Community Guidelines, and other conditions or policies […]"
> "If we have previously banned or suspended your account, but you use our Platform again (for example, by opening another account), we are entitled to ban or suspend any such accounts."

**Nicht in Primärquelle auffindbar (US-ToS):** ein ausdrückliches Verbot, Inhalte per automatisiertem System/Scheduler zu **posten** (die ToS regeln Scraping/Extraktion, Bots bei GenAI-Features und "spam accounts"; das Posting-Verbot per Automatisierung steht in den CG und den Developer-Regeln). Ebenfalls nicht enthalten: eine Klausel zur Höchstzahl von Accounts oder zum Verkauf/Transfer von Accounts.

### 2.17 Terms of Service – EWR (EEA)

**Quelle:** https://www.tiktok.com/legal/page/eea/terms-of-service/en — "Last updated: July 2026" — Jurisdiktion: EWR/EU (inkl. Deutschland) — **Verified**

Abschnitt 4.5 "What you can't do on the Platform" (Auszug):
> "Also, you must not use the Platform to:
> - do anything illegal […];
> - […]
> - undermine the Platform's operations or security;
> - engage in inauthentic commercial behaviours such as operating spam or impersonation accounts;
> - submit appeals, reports, notices or complaints which are clearly unfounded;
> - extract any data or content from the Platform using any automated system or software that is not provided by TikTok or approved in writing by TikTok;
> - use or attempt to use another user's account without their permission;
> - engage in fake review activity (including posting reviews that do not reflect your genuine experience, paying others to post fake reviews or offering services to facilitate fake reviews). See our Review Policy here; or
> - post, live stream or otherwise distribute any content on the Platform which:
>   - infringes anyone else's rights (such as intellectual property, privacy and/or personality rights of living or deceased people);
>   - […]
>   - spreads harmful misinformation […]"

Abschnitt 4.2 "Account details":
> "You must not create an account if we have previously terminated an account in your name for breaching these Terms or our Community Guidelines."

Abschnitt 4.6 "Your content" (DSA-konforme Moderation/Notice):
> "We review content both proactively and reactively. […] To do this we use a combination of technology and human moderators."
> "If we remove or restrict access to your content, we will notify you without undue delay and let you know the reasons for our decision, unless it is not appropriate for us to do so […]"

**Nicht in Primärquelle auffindbar (EEA-ToS):** Klauseln zu "bots"/"scripts" beim Posten, zu Mehrfach-Accounts (Anzahl) oder zum Verkauf/Transfer von Accounts.

### 2.18 TikTok for Developers – Content Posting API (automatisiertes Posten, Audit, Private-by-default)

**Quelle A:** Content Sharing Guidelines, https://developers.tiktok.com/doc/content-sharing-guidelines — "Last updated August 4, 2026" — global — **Verified**
> "Direct Post API enables developers to build "Share to TikTok" experiences in their app, which allows creators to share content directly to their TikTok profile. As a developer, you can use this API in an unverified status, but all content uploaded via this endpoint will be restricted to private viewing mode. To lift this restriction, your API client must undergo an audit to verify compliance with our Terms of Service.
> If your API client has not been audited, the following restrictions will apply:
> - User cap: Unaudited API Clients can allow up to 5 users to post in a 24 hour window. All user accounts using the API client to post must be set to private at the time of posting.
> - Private Viewership: Unaudited API Clients can only post contents in SELF_ONLY viewership. To make the contents publicly viewable later on, the account owner must first change their account visibility to public, and then change the privacy settings of each content to "Everyone."
> Additionally, both audited and unaudited API clients will be subject to the following caps:
> - Creator cap: There will be a 24-hour active creator cap for each API client based on the usage estimates provided in the audit application form.
> - Posting cap: There is a limit on the number of posts that can be made to a creator account in a 24-hour window via Direct Post API. The upper limit may vary among creators (typically around 15 posts per day/ creator account) and is shared across all API Clients using Direct Post."

"Intended Use" (relevant für Content-Fabriken / Multi-Account-Tools):
> "1) API Clients should facilitate authentic creators to post original content to TikTok.
> Not acceptable: An app that copies arbitrary contents from other platforms to TikTok.
> 2) API Clients must not be limited to test applications and should be intended for a wide audience, not limited to internal groups/private use.
> Not acceptable: A utility tool to help upload contents to the account(s) you or your team manages."

Pflicht-UX (Nutzer muss manuell wählen, keine Defaults):
> "- Users must manually select the privacy status from a dropdown and there should be no default value."
> "- Users must manually turn on these interaction settings and none should be checked by default."
> "a. API Clients should display a preview of the to-be-posted content.
> b. API Clients should not add promotional watermarks/logos to creators' content. Preset text, including any text in the title field or hashtags, should be allowed to be edited by the user before posting content."
> "3) API Clients must allow users to disclose Commercial Content: a. Content Disclosure Setting - Indicate whether this content promotes yourself, a brand, product or service, with this feature turned off by default."

Watermark Guidelines:
> "We expect you to avoid adding unwanted material to content posted to TikTok. That means your apps and integrations should not superimpose or otherwise include any brand name, logo, watermark, other promotional branding, link or promotional text, on or in any content which is shared to TikTok. Doing so is a violation of these guidelines, and may also lead to deleted content or disabled accounts."

**Quelle B:** Direct Post API Reference, https://developers.tiktok.com/doc/content-posting-api-reference-direct-post — "Last updated August 24, 2026" — **Verified**
> "Note: All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restriction on content visibility, your API client must undergo an audit to verify compliance with our Terms of Service."
> "Note: Each user access_token is limited to 6 requests per minute."
> Feld `is_aigc`: "If set, the video will be labelled with Creator labeled as AI-generated tag in video's description."
> Fehlercodes: "spam_risk_too_many_posts – The daily post cap from the API is reached for the current user." / "spam_risk_user_banned_from_posting" / "reached_active_user_cap" / "unaudited_client_can_only_post_to_private_accounts – Unaudited clients can only post to a private account. The publish attempt will be blocked when calling /publish/video/init/."

**Quelle C:** Upload Video (Inbox) Reference, https://developers.tiktok.com/doc/content-posting-api-reference-upload-video — "Last updated August 4, 2026" — **Verified**
> "There may be at most 5 pending shares within any 24-hour period" (Fehlercode "spam_risk_too_many_pending_share"); "You should inform users that they must click on inbox notifications to continue the editing flow in TikTok and complete the post."

**Quelle D:** Query Creator Info, https://developers.tiktok.com/doc/content-posting-api-reference-query-creator-info — "Last updated August 4, 2026" — **Verified**
> "spam_risk_too_many_posts – The daily post cap from the API is reached for the current user." / "reached_active_user_cap – The daily quota for active publishing users from your client is reached."

**Nicht in Primärquelle auffindbar:** Eine Regel in den Developer-Docs, die AI-generierte Inhalte via API ausdrücklich zur Kennzeichnung verpflichtet – es existiert nur das optionale Feld `is_aigc`; die Labelpflicht folgt aus den CG.

---

## 3) Antworten auf die Leitfragen (a)–(f)

**(a) Wann muss AI-Content gelabelt werden; was ist "realistic" / "significantly edited"?**
Pflicht, wenn AI-generierter oder stark bearbeiteter Inhalt "realistic-looking scenes or people" zeigt. "Realistic-Appearing" = "Content that looks like it could be real, such as AI-generated images that look like real photographs or footage." "Significantly Edited" = Medien, die jemanden etwas tun/sagen lassen, was nicht geschah, oder das Aussehen bis zur Unkenntlichkeit ändern (Cropping/Cutting zur Sinnänderung, Neuanordnung/Kombination von Clips, Speed-Änderung, Hinzufügen/Entfernen von Audio/Video). Support präzisiert: "modified by AI beyond minor corrections or enhancements" (Tanzen lassen, AI-Speech, Face-Swap). Keine Pflicht bei Farbkorrektur/Reframing/Cropping, Anime-Stil, generischem TTS. Label-Optionen: TikTok-AIGC-Label, eigene Caption, Sticker oder Wasserzeichen. Auto-Label bei TikTok-AI-Effekten, C2PA-Credentials und (seit Nov. 2025 im Test) unsichtbaren Wasserzeichen; Auto-Label nicht entfernbar. Falsches Labeln unveränderter Inhalte verstößt gegen die ToS. (Alle: Verified)

**(b) Welche AIGC ist komplett verboten?**
Likeness privater Personen ohne Einwilligung; alle Personen unter 18 (auch als "Private Figures" definiert); sexualisierte/fetischisierte/viktimisierende Darstellungen; AI-Likenesses zum Mobben; Accounts mit AI-Bildern von Jugendlichen in Erwachsenenkleidung/sexualisierten Posen; AIGC, das über Themen von öffentlichem Interesse täuscht (fake News-Quelle, Krisenereignis, Public Figure herabgewürdigt/kriminalisiert, Public Figure mit nicht getätigten politischen Aussagen, **Produkt-Endorsements** oder Kommentaren, erfundene politische Endorsements); jeder sonstige CG-Verstoß (Impersonation, Misinformation, Hate Speech) unabhängig von AI. FYF-ineligible: realistische, noch unbestätigte AIGC zu Public-Interest-Themen, die zu Fehlinterpretation führen oder Privatpersonen schaden könnte. (Verified)

**(c) Reichweite von gelabeltem AI-Content; Nutzer-Setting "weniger AI"?**
TikTok sagt ausdrücklich: "Turning on the AI-generated content setting won't affect the distribution of your video as long as it doesn't violate our Community Guidelines." (Support, Verified). Es gibt aber seit **Nov. 2025** (Newsroom 24.11.2025: "In the coming weeks, we'll start testing a new AI-generated content control in our 'Manage topics' feature") einen Regler "AI-Generated Content" unter Settings > Content preferences > Manage topics, mit dem Zuschauer mehr/weniger AIGC im FYF sehen; der AI Literacy Guide bestätigt die Funktion ("isn't available everywhere"). Konsequenz für Creator: Gelabelte (und per Wasserzeichen/C2PA erkannte) AIGC ist für Nutzer herunterregelbar – eine indirekte Reichweitenwirkung, die TikTok als "tailor … rather than removing or replacing content" beschreibt. Zusätzlich kann jeder Nutzer per Keyword-Filter AI-Begriffe blocken. Über 1,3 Mrd. Videos wurden bis Nov. 2025 als AIGC gelabelt (Newsroom, Verified).

**(d) Was ist FYF-ineligible (unoriginal, repetitiv, Spam, Low-Quality)?**
"Reused or unoriginal content posted without creative edits, such as clips that show someone else's watermark or logo"; "Low-quality or minimally edited content, such as short clips made from GIFs only"; "unoriginal or reused material without anything new"; Engagement-Bait ("like-for-like", falsche Anreize, irreführende Popularitätsclaims); realistische unbestätigte AIGC zu Public-Interest-Themen; ferner alle "FYF INELIGIBLE"-Listen anderer Kapitel (z. B. sexualisiert/mature). Wiederholtes Posten solcher Inhalte → **gesamter Account** FYF-ineligible und "harder to find in search" (Support), ggf. automatische Wiederherstellung. "Repetitive content" ist als Spam-Merkmal ("Using automation to run many accounts or send repetitive content"; "Posting a large amount of irrelevant material") sogar "Not allowed", nicht nur FYF-ineligible. (Verified)

**(e) Mehrere Accounts; wie viele pro Gerät/Nummer; automatisiertes Posten via API/Scheduler?**
Mehrere Accounts sind erlaubt ("You can have multiple accounts … but not to deceive others or break the rules"; Support: "You can create multiple accounts on TikTok"). Bindung: "Each phone number, email address, and social media account can only be linked to one TikTok account." Eine Obergrenze pro Gerät nennt **keine** Primärquelle (Nicht in Primärquelle auffindbar). Verboten: Automatisierung zum Betreiben vieler Accounts, Verteilen violativer Inhalte über mehrere Accounts, Umgehen von Restriktionen/Bans per Zweitaccount (→ Ban aller "associated accounts"). Automatisiertes Posten: Die CG verbieten "automation tools, scripts, or other tricks designed to bypass our systems"; die ToS verbieten automatisiertes Scraping und Bots bei GenAI-Features. Legitimer Weg sind Drittanbieter-Scheduler, die die offizielle Content Posting API nutzen: unauditiert nur privat/SELF_ONLY, max. 5 Nutzer pro 24 h; nach Audit öffentlich, aber mit Posting-Cap (~15 Posts/Tag/Creator, geteilt über alle API-Clients), 6 Requests/Min pro Token, Pflicht zur manuellen Privacy-Auswahl, Vorschau, Commercial-Disclosure; Apps, die "arbitrary contents from other platforms" kopieren oder nur eigene/Team-Accounts befüllen, werden als "Not acceptable" bezeichnet. (Verified)

**(f) Enforcement-Leiter**
1. **Label durch TikTok** (Auto-Label per AI-Effekt, C2PA, Wasserzeichen; oder nachträglich "labeled by our team") bzw. Context-Label/Warning-Screen bei Public-Interest-Ausnahmen.
2. **FYF-ineligible** (Post) – sichtbar in Analytics, appellierbar; bei Häufung **Account** FYF-ineligible + schlechter auffindbar in Suche.
3. **Removal** – erstes Mal i. d. R. "warning strike"; danach Strikes je Policy-Bereich/Feature; Strikes verfallen nach 90 Tagen; Löschen des Inhalts entfernt Strikes nicht.
4. **Temporäre Feature-/Account-Restriktionen** (Posten, Kommentieren, DMs, Login, Profil) – einsehbar unter "Account check"/Account status; optionales Policy-Training zur Wiederherstellung.
5. **Permanent-Ban** bei Erreichen der Strike-Schwelle (nicht beziffert), schwerer Einzelverletzung, Impersonation, Umgehung, "account exists solely to violate our rules"; Ban kann auf alle zugehörigen Accounts ausgeweitet werden; Neu-Account nach Ban ist untersagt (CG + ToS US/EEA).
6. Bei Fake-Engagement zusätzlich: Entfernung gefälschter Likes/Follower ("inflated signals").
(Alle Punkte: Verified)

---

## 4) Offene Punkte / nicht auffindbar

- **Anzahl Accounts pro Gerät/Telefon:** Keine Primärquelle nennt eine Zahl; der Help-Center-Artikel "Multiple accounts" unter der vorgegebenen URL existiert nicht mehr (Redirect auf Kategorie/Shell). Sekundär oft "3 pro Gerät" – Claimed, nicht verifiziert.
- **Konkrete Strike-Schwelle bis Permanent-Ban:** Nur "threshold", keine Zahl in Support-Artikel oder CG.
- **Rollout-Status des "AI-Generated Content"-Reglers je Land (z. B. DE/EU):** Nur "isn't available everywhere" (AI Literacy Guide); keine Länderliste.
- **Aussage, ob gelabelte AIGC algorithmisch geringer verteilt wird:** TikTok verneint für das Creator-Label ausdrücklich ("won't affect the distribution"); Auswirkungen der Nutzerregler/Wasserzeichen-Auto-Labels auf Reichweite werden nicht quantifiziert.
- **Newsroom-Posts 2026 zu AI-Labels:** nicht auffindbar (Newsroom-Listing/Sitemap technisch nicht abrufbar; Suchkontingent erschöpft). Maßgeblich ist die CG-Version vom 25.08./24.09.2026.
- **Datumsangaben der Support-Artikel:** Das Help Center zeigt keine "Last updated"-Daten; Artikel-IDs (2025/2026er Generation) belegen aktuelle Fassungen, ein exaktes Datum ist nicht auslesbar.
- **ToS-Klausel gegen automatisiertes Posten:** Weder US- noch EEA-ToS enthalten ein wörtliches Verbot von Posting-Automation/Schedulern; Verbot ergibt sich aus CG ("automation tools, scripts") und Dev-Guidelines. Ebenso keine ToS-Klausel zu Account-Verkauf/-Transfer gefunden.
- **Developer-Pflicht zur AIGC-Kennzeichnung via API:** nur optionales Feld `is_aigc`; keine explizite Pflichtregel in den Dev-Docs.

---

## 5) Quellenliste (alle Zugriffe 2026-09-24)

Primärquellen (Verified):
1. TikTok Community Guidelines – Integrity and Authenticity (AIGC, Unoriginal Content, Deceptive Behaviors): https://www.tiktok.com/community-guidelines/en/integrity-authenticity — Released 2026-08-25, Effective 2026-09-24
2. TikTok Community Guidelines – Overview (inkl. Platform Security, Accounts): https://www.tiktok.com/community-guidelines/en/ — Released 2026-08-25, Effective 2026-09-24
3. TikTok Community Guidelines – For You feed Eligibility Standards: https://www.tiktok.com/community-guidelines/en/fyf-standards — Released 2026-08-25, Effective 2026-09-24
4. TikTok Community Guidelines – Enforcement: https://www.tiktok.com/community-guidelines/en/enforcement — Released 2026-08-25, Effective 2026-09-24
5. Help Center – About AI-generated content: https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content (→ https://www.tiktok.com/support/faq_detail?id=7636670084747893268) — kein Datum
6. Help Center – Content violations and bans: https://support.tiktok.com/en/safety-hc/account-and-user-safety/content-violations-and-bans (→ faq_detail?id=7543604781940791864) — kein Datum
7. Help Center – Your account status: https://support.tiktok.com/en/safety-hc/account-and-user-safety/account-status (→ faq_detail?id=7543604781319756294) — kein Datum
8. Help Center – Why is my account not being recommended?: https://support.tiktok.com/en/safety-hc/account-and-user-safety/why-is-my-account-not-being-recommended (→ faq_detail?id=7543604783110969862) — kein Datum
9. Help Center – Creating an account (Add/switch accounts): https://support.tiktok.com/en/getting-started/creating-an-account/creating-an-account (→ faq_detail?id=7581821549574052364) — kein Datum
10. Help Center – Manage topics: https://support.tiktok.com/en/account-and-privacy/account-privacy-settings/manage-topics (→ faq_detail?id=7636676986101996052) — kein Datum
11. Help Center – Connect to third-party apps: https://support.tiktok.com/en/safety-hc/account-and-user-safety/connect-to-third-party-apps (→ faq_detail?id=7543604785694562872) — kein Datum
12. AI Literacy Guide: https://www.tiktok.com/safety/en/tools-and-guides/ai-literacy-guide — kein Datum
13. Transparency – Supporting responsible, transparent AI-generated content: https://www.tiktok.com/safety/en/transparency/supporting-responsible-transparent-ai-generated-content — kein Datum
14. Transparency – Identifying content made with TikTok AI Tools: https://www.tiktok.com/safety/en/transparency/ai-content-identification — kein Datum
15. Newsroom – New labels for disclosing AI-generated content: https://newsroom.tiktok.com/en-us/new-labels-for-disclosing-ai-generated-content — 2023-09-19
16. Newsroom – Partnering with our industry to advance AI transparency and literacy: https://newsroom.tiktok.com/en-us/partnering-with-our-industry-to-advance-ai-transparency-and-literacy — 2024-05-09
17. Newsroom – More ways to spot, shape and understand AI-generated content: https://newsroom.tiktok.com/en-gb/more-ways-to-spot-shape-and-understand-ai-generated-content — Seitendatum 2025-11-24 (en-us-Slug nicht erreichbar)
18. Terms of Service (US): https://www.tiktok.com/legal/page/us/terms-of-service/en — Last updated 2026-07-15
19. Terms of Service (EEA): https://www.tiktok.com/legal/page/eea/terms-of-service/en — Last updated July 2026
20. TikTok for Developers – Content Sharing Guidelines: https://developers.tiktok.com/doc/content-sharing-guidelines — Last updated 2026-08-04
21. TikTok for Developers – Direct Post API Reference: https://developers.tiktok.com/doc/content-posting-api-reference-direct-post — Last updated 2026-08-24
22. TikTok for Developers – Upload Video Reference: https://developers.tiktok.com/doc/content-posting-api-reference-upload-video — Last updated 2026-08-04
23. TikTok for Developers – Query Creator Info: https://developers.tiktok.com/doc/content-posting-api-reference-query-creator-info — Last updated 2026-08-04
24. TikTok for Developers – Get Started (Content Posting API): https://developers.tiktok.com/doc/content-posting-api-get-started — Last updated 2026-08-04

Sekundärquellen (Claimed):
25. TechCrunch – "TikTok will let you choose how much AI-generated content you want to see": https://techcrunch.com/2025/11/18/tiktok-now-lets-you-choose-how-much-ai-generated-content-you-want-to-see/ — 2025-11-18
26. Newsroom – Community Guidelines Update (ältere Version, Kontext): https://newsroom.tiktok.com/en-us/community-guidelines-update — 2023-03-21 (via WebFetch-Zusammenfassung; nur als historischer Kontext, keine Regelgrundlage)

Methodische Anmerkung: Die Seiten tiktok.com/community-guidelines, /safety und /support werden clientseitig gerendert; die Zitate wurden aus dem URL-kodierten Remix-Loader-Payload bzw. dem Help-Center-API-Endpunkt `https://www.tiktok.com/feedback/1/faq_detail_by_id/?faq_id=…` extrahiert und sind wortgetreu (HTML-Tags entfernt). Die Newsroom-Kategorieseiten liefern ohne JS nur den jeweils neuesten Artikel; unbekannte Slugs fallen auf die Startseite zurück – deshalb wurde der AI-Controls-Post über die en-gb-Ausgabe verifiziert.

---

## Verifikation (adversarial)

Prüfung am 2026-09-24 durch zweiten Agenten. Methode: Jede source_url wurde unabhängig erneut geladen (WebFetch; bei JS-Shells curl + Dekodierung des Remix/React-Payloads; Help-Center-Artikel über `https://www.tiktok.com/feedback/1/faq_detail_by_id/?faq_id=…&country=US&lang=en&app_id=1284&app_key=tiktok-web` — die Parameterform stammt aus dem Support-Bundle `main.634d25ef.js`; ohne `app_id=1284` liefert der Endpunkt HTTP 400). Zitate wurden per exakter Zeichenkettensuche im dekodierten Text geprüft; Daten aus den Versions-Metadaten (`lastUpdate`, `updatedAt`) bzw. der sichtbaren Datumszeile. WebSearch stand nicht zur Verfügung (Sitzungskontingent erschöpft), war aber nicht nötig, da alle Primärquellen direkt lesbar waren.

| # | Regel | Verdict | Anmerkung |
|---|-------|---------|-----------|
| 1 | Labelpflicht für AI-/stark bearbeitete Inhalte mit realistischen Szenen/Personen; ungelabelt → remove/restrict/label | **CONFIRMED** | Zitat wörtlich im Payload `cg_richText/2026-H2-integrity-subpost3-text1` (Slug `integrity-authenticity`, Version `2026H2update`, lastUpdate "Released August 25, 2026 / Effective September 24, 2026"). Formatierung im Original mit Hervorhebungen ("we require creators to **label** …"), Wortlaut identisch. |
| 2 | Definitionen "Significantly Edited Content" / "Realistic-Appearing Scenes or People" | **CONFIRMED** | Beide Definitionen wörtlich in "More information" (inkl. der drei Unterpunkte Cropping/Rearranging/Changing speed). Datum wie #1. |
| 3 | Keine Disclosure bei kleinen Edits, Anime-Stil, generischem TTS | **CONFIRMED** | Liste "Disclosure isn't needed when:" mit exakt den drei Punkten unter dem Toggle "REQUIRED DISCLOSURE (using the AIGC label or a clear caption, watermark, or sticker)". Datum wie #1. |
| 4 | Verbotene AIGC auch mit Label (private Likeness ohne Consent, Minderjährige, sexualisiert/mobbend, täuschende Public-Interest-Inhalte inkl. Public Figures mit erfundenen Product-Endorsements) | **CONFIRMED** | Alle drei Zitatfragmente wörtlich im Toggle "NOT ALLOWED". Hinweis zur Interpretation "Minderjährige": Die NOT-ALLOWED-Liste nennt Minderjährige nicht als eigenen Punkt; das Verbot folgt aus "likeness of private figures without consent" i. V. m. der Definition "Private Figures: All people under 18 …" sowie dem Punkt "Accounts focused on AI images of youth …" – Ableitung ist korrekt, aber eine Synthese, kein Einzelzitat. |
| 5 | FYF-ineligible: realistische, noch unbestätigte AIGC zu Themen von öffentlichem Interesse | **CONFIRMED** | Wörtlich im Toggle "FYF INELIGIBLE" (`…subpost3-toggle1-text2`). Datum wie #1. |
| 6 | Creator-AI-Label beeinflusst Verteilung nicht (solange kein CG-Verstoß); Auto-Label nicht entfernbar; falsches Labeln = ToS-Verstoß | **CONFIRMED** | Artikel "About AI-generated content" (FaqId 7636670084747893268) über den FAQ-API-Endpunkt geladen; alle drei Sätze wörtlich vorhanden ("Note: Turning on the AI-generated content setting won't affect the distribution of your video as long as it doesn't violate our Community Guidelines." / "Note: Once your content is labeled as AI-generated with an auto label, you won't be able to remove the label from your post." / "misleadingly labeling unaltered content with this label is a violation of our Terms of Service and may result in the removal of content"). Kein Datumsfeld in der API-Antwort → Angabe "kein Datum" ist korrekt. Kontext: Der Distribution-Satz steht als "Note" unter der Schritt-für-Schritt-Anleitung zum Setzen des Labels. |
| 7 | Nutzer-Regler "AI-generated content" in Manage topics (angekündigt Nov. 2025); unsichtbare Wasserzeichen; 1,3 Mrd. gelabelte Videos | **CONFIRMED** | Newsroom en-gb, Seitendatum "November 24, 2025"; alle drei Zitate vorhanden (Wasserzeichen-Satz im Original mit Anführungszeichen um "Invisible watermarks" – near-verbatim). Präzisierung: Der Text kündigt einen **Test** an ("In the coming weeks, we'll start testing"), keinen vollständigen Rollout – "angekündigt" ist damit die richtige Formulierung. Die Nebenangabe "Presse 2025-11-18 (TechCrunch)" konnte mangels Suchkontingent nicht gegengeprüft werden; sie bleibt Claimed. |
| 8 | AI-Generated-Content-Setting in Manage topics existiert, aber nicht überall verfügbar | **CONFIRMED** | Abschnitt "Managing your AI experience" im AI Literacy Guide wörtlich vorhanden. Kein sichtbares Datum; Payload-Metadatum `sc_post/AI-literacy-guide` → `updatedAt: 2026-07-21T23:12:37Z` (nicht auf der Seite angezeigt, nur im Loader-Payload). |
| 9 | Drei Transparenz-Ebenen: sichtbare Labels, C2PA Content Credentials, unsichtbare Wasserzeichen | **CONFIRMED** | Wörtlich im Payload `cg_richText/aiwatermark-text` der Seite "Identifying content made with TikTok AI Tools". Kein Datum auffindbar (weder sichtbar noch als updatedAt-Feld für diesen Post). |
| 10 | Automatisches Labeln via C2PA Content Credentials seit Mai 2024 | **CONFIRMED** | Newsroom en-us, Seitendatum "May 09, 2024"; Zitat "Starting today, we're expanding auto-labeling to AIGC created on some other platforms by launching the ability to read Content Credentials, a technology from the Coalition for Content Provenance and Authenticity (C2PA)." wörtlich vorhanden. |

Gesamtbild: 10/10 CONFIRMED. Kein Zitat erfunden, verfälscht oder falsch datiert. Zwei Randnotizen: (a) #4 ist bei "Minderjährige" eine (zutreffende) Ableitung aus Definition + Liste, kein Einzelzitat; (b) #7 beschreibt einen angekündigten Test, keinen bestätigten Rollout – die Datei formuliert das bereits korrekt ("isn't available everywhere"). Die TechCrunch-Sekundärquelle (#7) bleibt ungeprüft.
