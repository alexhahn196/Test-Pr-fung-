# 18 – Automatisierungsplan mit Claude Code / Codex (Teil 21)

**Stand:** 26.09.2026 · Tool-Preise, API-Limits und Quellen: [`quellen/H_ai_tools_kosten_automation.md`](quellen/H_ai_tools_kosten_automation.md)

## 1. Pipeline und Automatisierungsgrad

| # | Schritt | Automatisierbar | Werkzeuge / APIs | Mensch bleibt nötig für … | Belegte Einschränkung |
|---|---|---|---|---|---|
| 1 | Trend-/Nischenrecherche | mittel | NexLev (YT-Shorts-Outlier), eigene IG-Insights, Awin/Impact-Feeds | Themen- und Saisonentscheidung | Keine offene Trend-API für TikTok/IG (TikTok Research API nur akademisch) |
| 2 | Produktfeed | hoch (Awin/Impact sofort), Amazon erst später | Awin Publisher API, Impact Catalogs (3.000 Req/h), **Amazon Creators API ab 10 Verkäufen in 30 Tagen** | Programmfreischaltungen | **PA-API 5 abgeschaltet** (VERIFIED). Am Start werden 40–60 Amazon-Produkte manuell kuratiert |
| 3 | Produktauswahl | mittel–hoch | LLM-Scoring: Provision × AOV × Rating × Visual Appeal × Verfügbarkeit | Wöchentliche Freigabeliste (10–15 min) | Qualitäts- und Reputationsrisiko schlechter Produkte |
| 4 | Creative-Konzept | hoch | Claude Code mit Format-Templates (F1–F5, [16](16_90_day_test.md)) | Stichprobe | – |
| 5 | Prompt-Erstellung | hoch | modellspezifische Prompt-Templates, Referenzbild-Mapping | – | – |
| 6 | Produkt-Freisteller + KI-Szene | hoch (technisch) | Freisteller aus lizenzierten Herstellerbildern; Nano Banana Pro/2 (≤ 6–10 Objekt-Referenzen), FLUX Kontext ($0,04/Bild) | **Produkttreue-QA** (Form, Farbe, Logo) | **Keine Amazon-Bilder als Input** (Amazon-Lizenz – A/G) |
| 7 | KI-Video | hoch (technisch) | Veo 3.1 Lite $0,05/s · Fast $0,12/s; Kling 3.0 via fal $0,084–0,168/s; Wan 2.5 $0,05/s; Higgsfield (Ultra 129 €/3.000 Credits) | **Pflicht-QA jedes Clips** (Artefakte, Produktdrift) | **Sora-API seit 24.09.2026 abgeschaltet** (VERIFIED). Logo-/Textdrift in 30–60 % der Produktclips (MODEL ASSUMPTION) |
| 8 | Hook / On-Screen-Text | hoch | LLM, 2–3 Varianten pro Reel | Stichprobe | – |
| 9 | Voice / Musik | hoch | ElevenLabs Creator ($22, deckt 120 Reels), Meta Sound Collection | Aussprache von Markennamen | Business-Accounts haben eingeschränkte IG-Musik; lizenzierte Musik nicht per API setzbar |
| 10 | Schnitt, Captions, Render | hoch | **Remotion** (React, kostenlos ≤ 3 Personen) + FFmpeg + Whisper-Timing | Endabnahme (~30 s/Reel) | – |
| 11 | Caption + Offenlegung | hoch (Text) / niedrig (Recht) | LLM-Bausteine; IG `is_paid_partnership`, TikTok `is_aigc` + `brand_content_toggle` | **Compliance-Check** | Haftung liegt beim Betreiber ([17](17_compliance.md)) |
| 12 | Affiliate-Zuordnung | hoch | Awin Link Builder, Impact-Tracking-Links, Amazon-Tag-Links + Geniuslink ($6 + $3,50/1.000 Klicks), Linkseite mit Reel-ID | – | Kürzer müssen Amazon als Ziel erkennbar lassen (A) |
| 13 | Posting | hoch (IG, YT, Pinterest) / mittel (TikTok) | IG Graph API (**100 Posts/24 h**, Reels + Trial Reels), YouTube (100 Uploads/Tag; unverifiziert nur privat), Pinterest v5; TikTok per Scheduler | Wöchentlicher Kalender-Check | TikTok Direct Post erst nach Audit; reine Privat-Tools sind ausgeschlossen |
| 14 | Comment-to-DM | hoch | CreatorFlow ($15) / Inrō (€12,99) / ManyChat | Moderation von Fragen und Beschwerden | DMs nur „solicited“ (Amazon) |
| 15 | Analytics | hoch | IG Insights API, YT Analytics, Pinterest (90 Tage), TikTok Display API (nur Zählwerte) | – | – |
| 16 | Affiliate-Reporting | mittel | Awin API (20 Calls/min), Impact API, CJ | **Amazon: manueller CSV-Export** | **Amazon hat keine Reporting-API** (VERIFIED) |
| 17 | Winner Detection | hoch | Skript-Score pro Reel (s. u.) | Interpretation, Hypothesen | kleine Stichproben → Fehlalarme |
| 18 | Neue Varianten | hoch | Re-Generierung von Hook und ersten 3 s; IG Trial Reels | Budget- und Themenentscheidung | – |

## 2. Zielarchitektur (von Claude Code gebaut und gepflegt)

```
pipeline/
  products/            # kuratierte Produkt-JSONs: SKU, Programm, Link, Specs (nur aus Feed/Datenblatt), Bildlizenz, Freisteller
  concepts/            # Format-Templates F1–F5 (YAML): Szenen, Hooks, CTA-Keyword, Produkt-Slots
  generate/            # Bild-/Video-Jobs (Gemini/Veo, fal/Kling, FLUX) mit Retry-Logik, Kostenlog pro Reel
  qa/                  # Vision-LLM-Vorfilter: Freisteller vs. Referenz (Farbe/Form/Logo), Artefakt-Score -> Freigabeliste
  render/              # Remotion-Templates: nummerierte Produktkarten, End-Card mit echten Fotos, Labels "Werbung"/"KI-generiert"
  publish/             # IG Graph API (Reels, Trial Reels), YT Data API, Pinterest v5, Scheduler für TikTok
  links/               # Linkseite (Next.js/Vercel): /r/<reel-id> -> Produktliste mit Disclosure; Geniuslink-Mapping
  analytics/           # tägliche Pulls: IG Insights, DM-Tool, Geniuslink, Awin/Impact; Amazon-CSV-Import
  reports/             # Wochenreport: Views, Klicks/1k, EPC, Provision/1 Mio. Views, Winner/Loser, Stop-Kriterien-Ampel
```

**Winner-Score pro Reel** (MODEL ASSUMPTION, mit Daten nachzujustieren):
`score = 0,35 × z(Views) + 0,20 × z(Shares+Saves pro 1k) + 0,25 × z(Keyword-Kommentare pro 1k) + 0,20 × z(Affiliate-Klicks pro 1k)`.
Die Top-20 % liefern Hook- und Format-Varianten für die nächste Woche, die unteren 20 % streichen das Format nach 3 Wochen.

## 3. Manueller Aufwand pro Woche nach dem Aufbau

| Tätigkeit | 60 Reels/Monat | 120 Reels/Monat |
|---|---|---|
| Produkt- und Konzeptfreigabe | 0,7–0,9 h | 1,4–1,9 h |
| **Clip-QA inkl. Produkttreue** (größter Block) | 2,3–3,5 h | 4,7–7,0 h |
| Endabnahme + Caption/Offenlegung | 0,9–1,4 h | 1,9–2,8 h |
| Fehlerbehandlung (API, Re-Renders) | 0,5–0,9 h | 0,9–1,9 h |
| Analytics/Winner-Review, Amazon-CSV | 1–2 h | 1,5–2,5 h |
| Community/DMs (nicht automatisierbar) | 1–2 h | 1,5–2,5 h |
| Pipeline-Wartung (Modell- und Preiswechsel) | 1–2 h | 1–2 h |
| **Summe** | **≈ 7,5–13 h/Woche** | **≈ 13–20 h/Woche** |

**Einmaliger Aufbau:** ≈ 40–80 h (Skripte, Templates, API-Freigaben, Accounts). Ein Vision-LLM-Vorfilter kann die QA-Zeit nach Schätzung um 30–50 % senken, die finale Freigabe aber nicht ersetzen (H 10.3, MODEL ASSUMPTION).

**Wochenendproduktion ist realistisch:** 120 Reels × ~10 Generierungen ergeben ≈ 300 Jobs pro Wochenende. Bei 6–20 parallelen Jobs und 1–3 min pro Job sind das 1–3 h Maschinenzeit. Der Engpass ist die menschliche QA (≈ 4–7 h), nicht die Rechenzeit.

## 4. Monatliche Kosten (MODEL ASSUMPTION, H 9.4)

| Stack | 60 Reels | 120 Reels |
|---|---|---|
| Günstig (Veo 3.1 Lite / Wan) + Lean-Fixkosten | ≈ 320 $ | ≈ 530 $ |
| Günstig B (Kling 3.0 Std) + Lean | ≈ 440 $ | ≈ 775 $ |
| Mittel (Veo 3.1 Fast) | ≈ 585–810 $ | ≈ 1.065–1.290 $ |
| Premium (Veo 3.1 Standard) + Komfort | ≈ 1.870 $ | ≈ 3.400 $ |

Das Modell rechnet mit **600 €/Monat bei ~90 Reels** (günstiger/mittlerer Mix). Ein **Hybrid-Ansatz** senkt die Videokosten um ~40–60 % und verbessert zugleich die Produkttreue: 1–2 KI-Clips plus animierte Stills und Parallax auf echten Produktfotos in Remotion.

## 5. Wo KI **nicht** automatisieren sollte

- **Produkteigenschaften erfinden oder ändern.** Specs kommen nur aus Feed oder Datenblatt.
- **Erfahrungsaussagen** („ich nutze das seit Monaten“).
- **Preise im Video** (Amazon-Regel) und Rabattbehauptungen.
- **Community-Antworten auf Produktfragen**, die über das Datenblatt hinausgehen.
- **Finale Veröffentlichung ohne menschliche Sichtprüfung** von Produkttreue und Kennzeichnung.
