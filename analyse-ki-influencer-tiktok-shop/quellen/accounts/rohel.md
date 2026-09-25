# Dossier: @rohel (TikTok) — Rohel / "Creator Empire" (DE)

Zugriffsdatum aller Quellen: 2026-09-24. Kennzeichnung: **Verified** = in TikTok-/YouTube-Rohdaten gesehen, **Claimed** = Behauptung des Creators, **Estimated** = eigene Rechnung (Formel angegeben).

## 1. Kurzfazit

- Das TikTok-Konto **@rohel existiert, ist aber PRIVAT** (`privateAccount: true`, `secret: true`, statusCode 10222 "ErrBizUserSecret"). Öffentlich sichtbar sind nur Profil-Metadaten: **453.800 Follower, 6,5 Mio. Likes, 88 Following, Bio leer, kein Bio-Link, kein Seller-/Commerce-Flag** (Verified, TikTok-SSR-JSON, 2026-09-24).
- **Kein einziges Video ist abrufbar** (videoCount wird als 0 ausgeliefert, itemList leer). Alle Schritte, die Videos benötigen (Sample-Metriken, Produkt-Anchors, AIGC-Label, Sichtung per KI), sind daher **nicht durchführbar**. Datenqualität: *Verified profile only*.
- Die im Sweep notierten Einkommens-Claims stammen **nicht von diesem TikTok-Konto**, sondern aus dem YouTube-Kanal "Rohel" (@roohel, 60.500 Abonnenten, 12 Videos). Dort behauptet Rohel (Co-Founder der TikTok-Shop-Agentur "Creator Empire"), er und sein Partner "Wissam" betrieben Hands-only-Accounts mit "300 € Provision am Tag" und "zwei, drei" reine KI-Accounts mit "teilweise am Tag 3 bis 400 € Provision". **Die Handles dieser Accounts werden in keinem der beiden gesichteten Videos genannt.** Das private @rohel-Konto ist also mit hoher Wahrscheinlichkeit sein persönliches Konto und **nicht** einer der beschriebenen KI-Affiliate-Accounts.
- Kontext der Claims: Beide YouTube-Videos enden in einem Coaching-Funnel (Typeform-Bewerbung, "1:1-Mentorship", "diesen Monat sind aktuell noch drei Plätze frei"). Die Zahlen sind Verkaufsargumente ohne Dashboard-Screenshot in den Transkripten. Zudem widersprechen sich Titel ("4.700 €/Monat") und Inhalt ("3 bis 400 € am Tag" = 9.000–12.000 €/Monat; "hunderte Euros bis 1000 € am Tag").
- **Einordnung für das Projekt:** Als Vorbild-/Reverse-Engineering-Account unbrauchbar (privat, keine Videos, kein Shop-Signal). Als Quelle für Einkommensbehauptungen nur mit der Kennzeichnung "unbelegter Coaching-Claim" verwendbar.

## 2. Profil-Tabelle

| Feld | Wert | Status |
|---|---|---|
| Username / URL | @rohel — https://www.tiktok.com/@rohel | Verified |
| Existiert | ja | Verified |
| Privat | **ja** (privateAccount=true, secret=true, statusCode 10222) | Verified |
| Nickname | rohel | Verified |
| Follower | 453.800 | Verified (SSR shareMeta: "453.8k Followers, 88 Following, 6.5m Likes") |
| Likes (heartCount) | 6.500.000 | Verified |
| Following | 88 | Verified |
| Video-Anzahl | 0 sichtbar (privat; reale Zahl nicht öffentlich verifizierbar) | Verified (Feld) |
| Account erstellt | 2020-12-24 (createTime 1608809017) | Verified |
| Sprache (Profil) | de | Verified |
| Region | nicht ausgeliefert (null); Zuordnung DE nur über YouTube-Kanal/Sprache | Claimed/abgeleitet |
| Bio | leer | Verified |
| Bio-Link | keiner | Verified |
| ttSeller | false | Verified |
| commerceUserInfo.commerceUser | false | Verified |
| verified badge | nein | Verified |
| Modelltyp (Sweep-Notiz) | F | aus Sweep, nicht überprüfbar |
| Nische | Sweep-Notiz: "TikTok Shop DE affiliate, hands-only + 'nur mit KI'"; für @rohel selbst **nicht verifizierbar** (keine Videos). YouTube-Kanal: TikTok-Shop-/Dropshipping-Coaching DE | Claimed |
| Content-Typ | unbekannt (privat) | — |
| Upload-Frequenz | nicht öffentlich verifizierbar | — |
| AI-Level | unklar (keine Videos sichtbar) | — |
| Shop aktiv | **unklar** — keine Seller-/Commerce-Flags, keine Bio-Hinweise, keine sichtbaren Produkt-Anchors | — |

## 3. Handle-Prüfung (Verwechslungsgefahr)

| Handle | Befund (tt_profile.sh, 2026-09-24) |
|---|---|
| @rohel | privat, 453.8K Follower, Nickname "rohel", Sprache de — **Zielkonto** |
| @rohel.tiktok | heute bengalischsprachiges Konto ("পরিবারের দুষ্ট ছেলে"), 133 Follower, erstellt 2025-11-10. Suchmaschinen-Snippets zeigen unter diesem Handle alte deutsche Videos ("Zucker in Getränke", "Perfekte Dinge Teil 27"); beide Video-IDs (7192668381202418949, 7087898017986055430) liefern "item doesn't exist". Handle wurde offenbar neu vergeben; kein Bezug zum Zielkonto belegbar. |
| @rohel2023 | 15.700 Follower, 3.154 Videos, Nickname "rohel", nicht Seller — anderes Konto (nicht DE-TikTok-Shop). |
| @rohelkhan77, @rohel.rol, @md.rohel14 u. a. | andere Personen (Rohingya-Rapper, PH/BD-Nutzer). |

## 4. Video-Sample

**Keine Videos abrufbar.** Das Konto ist privat; die TikTok-Seite liefert `itemList: []`/`None`. WebSearch (`site:tiktok.com/@rohel`, `"tiktok.com/@rohel/video"`, `"@rohel" tiktok`) ergab **keine einzige URL unter /@rohel/video/**. Sichtung per `mcp__NexLev__watch_tiktok_video_and_ask` daher nicht möglich.

| id | Datum | Views | Likes | Kommentare | Anchors | AI-Label |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

n = 0. avg/median/max Views: nicht berechenbar.

## 5. Shop-Aktivität

- ttSeller: false; commerceUser: false (Verified).
- Bio leer, kein Showcase-/Shop-Hinweis, kein Bio-Link (Verified).
- Produkt-Anchors / #tiktokshop-Hashtags: nicht prüfbar (keine Videos).
- Externe Belege, dass @rohel selbst Affiliate ist: keine gefunden. Rohel bezeichnet sich auf YouTube als Co-Founder einer TikTok-Shop-Agentur (Claimed).
- **Klassifikation: unklar.**

## 6. Einkommens-/Umsatz-Claims (Quelle: YouTube, nicht TikTok)

Quelle A: https://www.youtube.com/watch?v=QLkfEq3xyTQ — "Wie ich 4.700€/Monat mit TikTok und KI verdiene (Kompletter Guide)", Kanal "Rohel" (@roohel, UChFph_P0mMZl0MH-CSI7lDw), veröffentlicht 2026-05-30, 13:51 min, **208 Views, 7 Likes, 0 Kommentare** (Verified, YouTube-Metadaten 2026-09-24). Kanal: 60.500 Abonnenten, 12 Videos; Kanalbeschreibung: "Mein Name ist Rohel, ich bin ein 18-jähriger sechsstellig verdienender E-Commerce-Unternehmer." (Claimed)

Wörtliche Zitate aus dem Auto-Transkript (Claimed):
- (0:25–1:10) "Wir haben Accounts hochgezogen, womit wir mittlerweile 300 € Provision am Tag machen und wir einfach nur … bisschen unsere Hände zeigen, die Produkte zeigen. Mittlerweile sind wir sogar auf so einem Punkt angekommen, wo wir halt nur mit KI … das ganze hochziehen. Da haben wir mittlerweile zwei, drei Accounts der Wissam und ich selber schon aufgebaut, wo wir teilweise am Tag 3 bis 400 € Provision machen, was komplett Cash in unsere Tasche geht."
- (5:00–6:00) Tool-Stack: "ChatGPT allgemein für die Promptgenerierung … Könnt auch natürlich Claude benutzen … dann natürlich noch Higgsfield für die Videogenerierung … dann bin ich jetzt hier als allererstes auf Kalodata gegangen … du brauchst jetzt auch nicht mal zwingend auf Kalodata ein Account." (Transkript-Schreibweisen: "Hixfield", "Kodata/Kell Data")
- (9:20–9:50) "Du hast Higgsfield, was dir wirklich alles erstellt, sei es von Stimme, sei es mit Video … Du musst deine Stimme nicht zeigen."
- (11:30–12:30) "auf die konstanten 2, 3, 4, 5000 € … zu kommen, das braucht Erfahrung … Ich will dir auch nicht versprechen, dass du irgendwie 5000 € konstant nächsten Monat … machen wirst. … wir selber haben bei uns gemerkt, dass wir hunderte Euros bis 1000 € am Tag rein an Provision verdienen."
- (12:30–13:40) Funnel: "unser eins zu eins Mentorship-Programm … personalisierte WhatsApp-Gruppe … zweimal die Woche Live Calls … diesen Monat sind aktuell noch drei Plätze frei … findest du den ersten Link in der Videobeschreibung."
- Videobeschreibung: "Bewirb dich für ein kostenloses Beratungsgespräch … https://ecomempire.typeform.com/to/SStJbcP5 … Ich bin Co-Founder von Creator Empire, einer der führenden TikTok Shop Agenturen in Deutschland mit über 120 Creatorn und €15M+ GMV" (Claimed; keine Belege im Video).

Quelle B: https://www.youtube.com/watch?v=NcrJPxXkd64 — "Schau mir zu, wie ich eine 10.000€ Faceless TikTok Seite aufbaue mit KI" (2026-02-24, 812 Views). Zitate (Claimed): "Das hier ist kein echter Mensch … und trotzdem verkauft es viel besser als die meisten Menschen"; "Leute verdienen sich damit … bis zu 10.000 € im Monat"; "Provisionssatz von sagen mal 10, 20 %"; "was ich bzw. wir aktuell benutzen ist Higgsfield". **Auch hier kein TikTok-Handle genannt.**

Weitere Kanaltitel (nur Titel, nicht gesichtet): "Diese TikTok Shop Strategie ist langweilig aber bringt 328€/Tag" (2025-12), "So bezahlt TikTok dir 450€ am Tag", "Wie Alessio (29) mit TikTok Shop in 30 Tagen von 32€ auf 2302€ Provision kam". Instagram @creatorempiree (Suchsnippet: "#1 fastest-growing TikTok Shop agency in Germany"; Seite selbst nicht abrufbar, HTTP 429).

Konsistenzprüfung der Claims:
- Titel "4.700 €/Monat" ≈ 157 €/Tag. Im Video: "300 € Provision am Tag" (Hands-only) und "3 bis 400 € am Tag" (KI-Accounts) ≈ 9.000–12.000 €/Monat; später "hunderte Euros bis 1000 € am Tag". Die Zahlen sind untereinander nicht konsistent und nirgends durch Dashboard/Kalodata-Screenshots belegt (Transkript; keine visuelle Sichtung durchgeführt).
- Reichweite des Claims minimal (208 YouTube-Views, 0 Kommentare) — keine unabhängige Bestätigung durch Dritte auffindbar.

## 7. Schätzung

**Für @rohel selbst: keine Schätzung möglich** — keine Views, keine Upload-Frequenz, kein Shop-Signal. Jede Zahl wäre reine Spekulation.

Einordnung der Claimed-Zahlen (nur Rechenweg, keine Bestätigung):
- Claimed 300–400 € Provision/Tag ⇒ 9.000–12.000 €/Monat Provision pro Account-Set. Bei Claimed 10–20 % Provisionssatz entspricht das ~45.000–120.000 € GMV/Monat. Rückwärtsgerechnet mit dem Projekt-Standardmodell (CTR 2 % × CVR 5 % = 0,1 % Käufe/View, AOV angenommen 25 €): benötigte Views ≈ GMV / (0,001 × 25 €) = **1,8–4,8 Mio. Views/Monat** pro Account-Set. Estimated (Formel: Views = GMV ÷ (CTR × CVR × Preis)); zeigt nur, welche Reichweite die Behauptung voraussetzen würde — nicht, dass sie erreicht wird.
- Konfidenz: **LOW**.

## 8. Warum funktioniert / funktioniert nicht

- Funktioniert **nicht** als Referenz-Account: privat, kein Shop-Flag, keine Videos → nichts zu reverse-engineeren. 453.8K Follower + 6,5 Mio. Likes belegen zwar frühere Reichweite (Konto seit Dez. 2020), aber nicht, womit sie erzielt wurde.
- Die KI-Affiliate-Claims sind ein Coaching-/Agentur-Funnel (Mentorship, Typeform, künstliche Verknappung "drei Plätze"). Ohne Handles der angeblichen KI-Accounts sind sie nicht überprüfbar. Der beschriebene Stack (Kalodata → ChatGPT-Prompts → Higgsfield Voice+Video) ist plausibel und deckt sich mit dem in anderen Dossiers dokumentierten Standard-Workflow, belegt aber keine Einnahmen.

## 9. Quellen

- https://www.tiktok.com/@rohel (SSR-JSON via tt_profile.sh, 2026-09-24)
- https://www.tiktok.com/@rohel.tiktok , https://www.tiktok.com/@rohel2023 (Handle-Prüfung, 2026-09-24)
- https://www.youtube.com/watch?v=QLkfEq3xyTQ (Metadaten + Auto-Transkript, 2026-09-24)
- https://www.youtube.com/watch?v=NcrJPxXkd64 (Auto-Transkript, 2026-09-24)
- https://www.youtube.com/channel/UChFph_P0mMZl0MH-CSI7lDw (Kanalliste, 2026-09-24)
- https://www.instagram.com/creatorempiree/ (nur Suchsnippet; Abruf HTTP 429, 2026-09-24)

## 10. Erneuter Prüfversuch (Retry, 2026-09-24/25)

Auf Anweisung "Erneut versuchen" wurde die komplette Prüfung wiederholt. Ergebnis: **unverändert**.

| Prüfung | Ergebnis (Retry) | Status |
|---|---|---|
| tt_profile.sh rohel | statusCode 10222 "ErrBizUserSecret", privateAccount=true, secret=true; 453.900 Follower (+100 ggü. Vortag), 6,5 Mio. Likes, 88 Following, 26 Freunde, videoCount 0, ttSeller=false, commerceUser=false, Bio leer, kein Bio-Link | Verified |
| WebSearch `site:tiktok.com/@rohel`, `"tiktok.com/@rohel/video"`, `"@rohel" "creator empire"/"wissam"`, `rohel tiktok 453.8K followers` | keine einzige URL unter /@rohel/video/; nur Fremdkonten (@rohel.tiktok, @rohel2023, @rohel.rol, @rohelkhan77, @md.rohel14, @rohel.yt, @rohelah91) | Verified (Suchergebnis) |
| TikTok-Discover-Seiten (tiktok-shop-deutschland, rohel-tiktok-videos) | liefern headless nur "TikTok - Make Your Day" ohne Inhalt | — |
| Suchsnippet (Google/Bing) zur Discover-Seite "TikTok Shop Deutschland" | erwähnt, dass "@Rohel" und "@Wisam" in einem TikTok-Shop-Affiliate-Post zum "TikTok Shop Summit 2026" getaggt wurden. Der Post selbst (Autor, URL) konnte nicht abgerufen werden. Stützt nur schwach, dass @rohel im DE-TikTok-Shop-Umfeld aktiv ist (Summit 15.–16.04.2026). | Claimed (Snippet, nicht abrufbar) |
| Agentur-Konten | @creatorempiree: 1.366 Follower, 6 Videos, Bio "Wir skalieren Brands und Creator / Offizielle Tiktok Shop Partner", Bio-Link join.creatorempire.de, kein Seller-Flag. @creatorempire: 1.312 Follower, 6 Videos (vermutlich anderer Betreiber). | Verified |
| YouTube-Seite QLkfEq3xyTQ (WebFetch) | nur Footer ausgeliefert; Transkript/Metadaten aus dem Erstlauf bleiben gültig | — |
| Video-Sichtung (watch_tiktok_video_and_ask) | nicht möglich, keine Video-URL vorhanden | — |

Schlussfolgerung Retry: Datenqualität bleibt **Verified profile only**; Shop-Status **unklar**; KI-Level **unklar**; keine Views/Frequenz/Schätzung für @rohel möglich. Die Einkommens-Claims bleiben unbelegte Coaching-Aussagen aus dem YouTube-Kanal.

Zusätzliche Quellen (Retry, 2026-09-24/25): https://www.tiktok.com/@creatorempiree , https://www.tiktok.com/@creatorempire (tt_profile.sh); https://www.tiktok.com/discover/tiktok-shop-deutschland (nur Suchsnippet).
