# Dossier: @poormaninla (TikTok) — Account nicht mehr auffindbar

Prüfdatum: 2026-09-24 (Zweitprüfung „Erneut versuchen“ 2026-09-25). Analyst: Due-Diligence-Subagent.
Kennzeichnung aller Zahlen: **Verified** (in TikTok-Daten / Primärdokument gesehen), **Claimed** (Behauptung Dritter), **Estimated** (eigene Rechnung).

## 1. Kurzfazit

| Feld | Wert |
|---|---|
| Username | poormaninla |
| TikTok-URL | https://www.tiktok.com/@poormaninla |
| Existiert (2026-09-24/25) | **Nein** — TikTok-API statusCode **10221 (user not found)** (Verified, zwei Prüfläufe) |
| Modelltyp | C — KI-„Arzt im weißen Kittel“-Avatare für Supplement-Affiliate (Rosabella / Ambrosia Brands) |
| Land | US (Claimed: Rechtsstreit W.D. Tex.; „LA“ im Handle) |
| Nische | Supplements (Rosabella Beetroot-Kapseln), Zielgruppe u.a. schwarze Frauen („slim stomach“) |
| Content-Typ | KI-generierte Talking-Head-Videos („doctor in a whitecoat“, zweiter Sprecher in Scrubs eingeblendet) — Claimed (Klage ¶55, 404 Media) |
| AI-Level | **vermutlich AI** — „its videos are almost entirely AI-generated“ (404 Media, Claimed); Klage: „All or nearly all of the ‘doctors’ … are AI-generated and fictitious“ (¶54). Eigene Sichtung nicht möglich (Account weg). |
| Shop aktiv | **unklar** — Klage ¶66/67: Ambrosia „profits … through commission and consumer redirect links“ und „is compensating influencers like poormaninla“ (Claimed). ttSeller/commerceUserInfo/Anchors nicht abrufbar. |
| Follower / Likes / Videoanzahl / Account-Erstellung | Nicht öffentlich verifizierbar (Profil nicht mehr vorhanden; kein Wayback-Snapshot) |
| Datenqualität | **Unverified** |
| Einkommens-Konfidenz | LOW |

## 2. Prüfschritte und Ergebnisse

1. `tt_profile.sh poormaninla` → `{"statusCode": 10221, ...}` (Verified, 2026-09-24 und 2026-09-25).
2. Handle-Varianten geprüft (`poor.man.in.la`, `poor_man_in_la`, `poormanla`, `poormaninla_`, `poormaninla1`) → alle 10221 (Verified).
3. WebFetch https://www.tiktok.com/@poormaninla → nur generischer Titel „TikTok - Make Your Day“, kein Profilinhalt.
4. Wayback-Machine-CDX (`tiktok.com/@poormaninla*`) → **keine Snapshots** (leeres Ergebnis).
5. 404-Media-Artikel-HTML durchsucht: enthält **keine** TikTok-Video-URL des Accounts; die eingebetteten Clips (storage.ghost.io …/2026/07/0730--1-.mp4 u.a.) sind redaktionelle Zusammenschnitte ohne Zuordnung zu einem Handle.
6. Klageschrift (Humann v. Ambrosia Brands, 1:26-cv-00374-ADA-ML, Doc. 14, eingereicht 2026-06-04) — lokale Kopie `research/product_side/humann_manual.txt` — nennt kein Video-URL, nur „Exhibit K“ (Screenshots, nicht öffentlich im Textdokument).
7. WebSearch: Budget dieser Session erschöpft (200/200) — keine weiteren Suchen möglich. Video-Sampling (tt_video.sh) und Video-Sichtung (NexLev watch) daher **nicht durchführbar**: 0 Videos gesampelt.

## 3. Belege (Zitate)

**Klageschrift Humann, Inc. v. Ambrosia Brands, LLC (W.D. Tex., Case 1:26-cv-00374-ADA-ML, Document 14, filed 06/04/26)** — https://storage.courtlistener.com/recap/gov.uscourts.txwd.1172890758/gov.uscourts.txwd.1172890758.14.0_3.pdf (Zugriff über lokale Kopie, 2026-09-24):
- ¶54: „In several TikTok Posts, the post purports to show a doctor, medical professional, or other medical authority espousing the health benefits of Defendant's products. All or nearly all of the ‘doctors’ featured in the TikTok Posts are AI-generated and fictitious…“
- ¶55: „For example, in a June 14, 2025 TikTok post, influencer ‘poormaninla’ purports to depict a doctor in a whitecoat that promotes the alleged health benefits of Defendant's products. Before the ‘doctor’ begins speaking, a separate speaker is imposed on the screen in a surgeon's or nurse's scrubs. Representative screenshots of this post are attached as Exhibit K.“
- ¶60: „in the June 14 TikTok post referenced above, the nurse or doctor speaking at the beginning of the video says ‘Just because he's black, doesn't mean he's joking.’“
- ¶66: „Defendant profits from the TikTok Posts through commission and consumer redirect links, which are used to compensate the creators of the TikTok Posts…“
- ¶67: „Defendant is compensating influencers like poormaninla, trinibof8dl, and badobadi86 for these claims.“
- ¶68: Privater Discord, „10-hour course“, Skripte, „Defendant provides a commission on the influencer's sales“.
- ¶72: Recruiter Luca Washenko: „Defendant paid out ~$400,000 last month to creators“; Screenshot einer Zahlung von $317,710 an einen Creator „Michel“ (Claimed; nicht poormaninla).

**404 Media, „Inside an AI TikTok Shop Slop Factory That Shills Supplements Recalled by the FDA“ (2026-07-30)** — https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/ (Zugriff 2026-09-24):
- „The ‘poormaninla’ account is still up on TikTok and its videos are almost entirely AI-generated. Several of the videos have hundreds of thousands of views.“
- Zitat aus einem Video: „The best food for Black women to eat if they want a slim stomach is not turmeric, it's not ginger, and it's definitely not blueberries. Just one teaspoon of this food reduces gut inflammation,“ an AI-generated man in a lab coat says in one.

## 4. Sampled-Video-Tabelle

| id | Datum | Views | Likes | Kommentare | Anchors | AI-Label |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

n = 0. Kein Video-URL auffindbar (Account gelöscht/umbenannt; keine Archiv-Snapshots; Presse/Klage nennen keine URLs). Einziges Datum aus Primärquelle: Post vom **2025-06-14** (Claimed, Klage ¶55).

## 5. Metriken

- Ø / Median / Max Views: nicht berechenbar (n = 0). Einziger Reichweiten-Hinweis: „hundreds of thousands of views“ für mehrere Videos (404 Media, Claimed).
- Upload-Frequenz: nicht öffentlich verifizierbar. Kontext (Claimed, Klage ¶52): Netzwerk-Creator wie badobadi86 posteten seit 2025-07-10 täglich.

## 6. Einkommens-/GMV-Schätzung

Keine veröffentlichte GMV-/Sales-Zahl für poormaninla (kein Kalodata/FastMoss-Beleg gefunden; WebSearch-Budget erschöpft).

**Estimated (nur Größenordnung, Formel wie vorgegeben, Inputs weitgehend Annahmen):**
- Monatliche Views: Annahme 0,5–2 Mio. (aus „several videos with hundreds of thousands of views“, Claimed; Frequenz unbekannt, angenommen 15–30 Posts/Monat à 30–70k)
- CTR 2 % → 10.000–40.000 Klicks; CVR 5 % → 500–2.000 Bestellungen
- Preis Rosabella Beetroot-Kapseln: Annahme ~$25–35/Bestellung (Claimed: „much lower prices compared to Humann's SUPERBEETS“, ¶77; genauer Preis nicht verifiziert)
- GMV: 500×$25 = **$12.500** bis 2.000×$35 = **$70.000/Monat** (Estimated)
- Provision 10–20 % → **$1.250–14.000/Monat** (Estimated)
- Konfidenz: **LOW** — kein einziger Input verifiziert; Account existiert nicht mehr, Einnahmen (falls vorhanden) sind beendet. Klage ¶69 („Defendants have the power to demonetize posts“) zeigt außerdem, dass Auszahlung von der Marke abhängt.

## 7. Bewertung: Warum es (nicht) funktioniert

Das Konto ist der dokumentierte **Failure Case** des Modells „KI-Arzt-Avatar × Supplement-Affiliate“: Reichweite laut Presse im sechsstelligen Bereich pro Video (Claimed), aber (a) medizinisch unbelegte und rassifizierende Claims (Klage ¶59–60), (b) fiktive „Ärzte“ ohne Kennzeichnung als AI (¶64–65 „separate layer of deception“), (c) Produkt mit FDA-Recall-Kontext (404 Media Titel), (d) Abhängigkeit vom Marken-Discord und dessen Demonetisierungs-Hebel (¶68–69). Innerhalb von ~2 Monaten nach Klage (Juni 2026) und Bericht (30.07.2026 „still up“) ist der Handle verschwunden (Verified 10221 am 24.09.2026) — ob durch TikTok-Sperre, Löschung oder Umbenennung, ist nicht öffentlich verifizierbar. Lehre: kurzfristige Reichweite, kein nachhaltiges Einkommen, hohes Rechts- und Plattformrisiko.

## 8. Quellen (Zugriff 2026-09-24/25)

- https://www.tiktok.com/@poormaninla — 10221 not found (Verified)
- https://www.404media.co/inside-an-ai-tiktok-shop-slop-factory-that-shills-supplements-recalled-by-the-fda/
- https://storage.courtlistener.com/recap/gov.uscourts.txwd.1172890758/gov.uscourts.txwd.1172890758.14.0_3.pdf (Humann v. Ambrosia Brands, Doc. 14)
- https://web.archive.org/cdx/search/cdx?url=tiktok.com/@poormaninla* — keine Snapshots
