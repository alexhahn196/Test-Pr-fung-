# 16 – 90-Tage-Test und harte Stop-Kriterien (Teile 28–29)

**Testobjekt:** Kitchen & Coffee Setups ([15](15_winner.md)). Arm A = EN/US-Account (primär), Arm B = DE-Spiegel.
**Zeitraum:** 01.10.–31.12.2026 (13 Wochen) · **Budget:** 1.000–2.000 €, geplant ≈1.400 € · **Kein bezahlter Traffic** (Amazon vergütet seit 14.04.2026 ohnehin keine Käufe über geboostete Werbung – A).

## 1. Was der Test beweisen muss

Die Studie hat eine Lücke, die sich nur durch eigene Messung schließen lässt: **Wie viele Affiliate-Klicks und wie viel Provision erzeugt eine KI-Setup-Page pro 1.000 Views?** Alles andere (AOV, Provisionssätze, Retouren) ist recherchiert. Der Test misst deshalb vor allem vier Größen:

1. **Klicks pro 1.000 Views** (Modell: Base 1,2 · Strong 3,0 inkl. nicht monetarisierbarer Klicks)
2. **EPC** (Provision pro Klick; Modell Base 0,085 € EN / 0,067 € DE)
3. **Provision pro 1 Mio. Views** (Modell Base 56 € EN / 64 € DE · Strong 311 € / 335 €)
4. **Views-Wachstum** (braucht einen Pfad zu ≥ 20 Mio. Views pro Monat in EN bis Monat 12)

## 2. Budget (MODEL ASSUMPTION auf Basis [H, Abschn. 9](quellen/H_ai_tools_kosten_automation.md))

| Posten | Monat 1 | Monat 2 | Monat 3 | Summe |
|---|---|---|---|---|
| KI-Generierung (Veo 3.1 Lite/Fast, Kling 3.0, Nano Banana/FLUX; 2,5 Versuche pro Clip) | ≈ 220 € (≈ 60 Unikate + Tests) | ≈ 330 € (≈ 90) | ≈ 330 € (≈ 90) | ≈ 880 € |
| Fixkosten (LLM, ElevenLabs 22 $, DM-Tool ~15 $, Geniuslink 6 $ + Klicks, Vercel 20 $, Domain) | ≈ 90 € | ≈ 95 € | ≈ 100 € | ≈ 285 € |
| Impressum/Datenschutz-Generator, Markenrecherche Name | ≈ 60 € | – | – | ≈ 60 € |
| Reserve (Re-Generierungen, Scheduler für TikTok/YT, Tool-Wechsel) | – | ≈ 80 € | ≈ 100 € | ≈ 180 € |
| **Summe** | **≈ 370 €** | **≈ 505 €** | **≈ 530 €** | **≈ 1.405 €** |

Zeit (MODEL ASSUMPTION, H 10.3): Aufbau ≈ 40–80 h in den Wochen 1–3, danach ≈ 8–13 h/Woche.

## 3. Monat 1 (Oktober): Aufbau und Format-Test

**Woche 1 – Infrastruktur**
- 2 Instagram-Business-Accounts (EN, DE) anlegen, neutraler Markenname ohne Markennamen Dritter (Jackery-Regel u. ä. – D). Impressum und Werbe-Hinweis in der Bio bzw. auf der Linkseite.
- Amazon Associates US und PartnerNet DE mit exakten Social-URLs registrieren. Pflicht-Offenlegungstext in Bio/Linkseite. **Ziel: ≥ 3 Verkäufe je Programm in 180 Tagen** (sonst Schließung – A).
- Bei Awin, Impact und Adcell bewerben. Priorität haben Programme, die Social ausdrücklich erlauben: De'Longhi DE, Sage UK, Breville, Zwilling, KitchenAid, Coffee Circle, Kaffee24. Ablehnungen einplanen (R7 im [Red Team](13_red_team.md)).
- Linkseite (Vercel) mit Reel-ID-Liste („#17 → Produkte“), Geniuslink für Geo-Routing, DM-Tool mit Keyword-Flows (Amazon erlaubt Links in DMs nur auf Anforderung = Comment-Trigger – A/G).

**Woche 1–3 – Pipeline** (Details in [18](18_automation_plan.md))
- 40–60 Produkte manuell kuratieren, in 3 Preisstufen. Die Amazon Creators API steht erst nach 10 Verkäufen in 30 Tagen zur Verfügung.
- Produkt-Freisteller erzeugen, Szenen-Templates für 3 Stile, Video-Clips, Remotion-Templates, Caption- und Disclosure-Bausteine.

**Woche 2–4 – Posting**
- **EN:** 2 Reels/Tag (≈ 45). **DE:** 1 Reel/Tag (≈ 20), gleiche Visuals mit DE-Voice/Captions und DE-Links.
- **5 Formate × je ≥ 9 Reels:**
  - F1 „Build this coffee corner“
  - F2 „$500/$1.500/$3.000 espresso setup“
  - F3 „Same kitchen, 3 styles“
  - F4 „Countertop reset“
  - F5 „Morning routine ASMR“
- **Hooks:** je Format 2–3 Varianten als Instagram **Trial Reels** (nur an Nicht-Follower; per API steuerbar – H).
- **CTA:** Jedes Reel bekommt ein Keyword-CTA („Kommentiere COFFEE“) **und** eine nummerierte Produktliste auf der Linkseite. Ein Teil der Reels (≈ 20 %) läuft **ohne** DM-CTA als Kontrollgruppe, um den DM-Effekt zu messen.

**Messung ab Tag 1**
- **Automatisch:** IG Insights API (Views, Reach, Saves, Shares), DM-Tool (Keyword-Kommentare, gesendete DMs, Klicks), Geniuslink (Klicks nach Land), Awin/Impact-API.
- **Manuell:** Amazon-CSV (Amazon hat keine Reporting-API – H).

## 4. Monat 2 (November): Gewinner skalieren

- Die 2 schwächsten Formate streichen und die 2 besten auf je 3 Hook-Varianten ausbauen.
- **EN auf 3 Reels/Tag** erhöhen. DE bleibt bei 1/Tag, außer DE liefert pro View mindestens 1,5× die EN-Klickrate (dann 2/Tag).
- **Cross-Posting** derselben Renders auf YouTube Shorts und TikTok (per Scheduler; TikTok-Direct-Post braucht ein Audit – H). Dazu **Pinterest-Pins nur mit Nicht-Amazon-Links** (Amazon lässt Pinterest nicht zu – A).
- **Black-Friday-/Cyber-Monday-Serie** (27.–30.11.2026): „Espresso setups on sale“. Preise nicht statisch einbrennen, sondern auf die Linkseite verweisen (Amazon-Preisregel – G).
- Freigeschaltete Händlerprogramme in die Linklisten aufnehmen und die EPC Amazon vs. Händler vergleichen.

## 5. Monat 3 (Dezember): Beweis führen

- Serie „Geschenke für Kaffee-Fans unter 100 $ / 300 $“ bis ca. 18.12., danach „New Year kitchen reset“.
- **A/B-Tests:** Linkziel (Linkseite vs. direkter Produktlink in der DM), 1 vs. 3 Produkte pro DM, Preisstufen-Reihenfolge.
- **Entscheidung am Tag 90** nach den Kriterien unten: SCALE, CONTINUE, PIVOT (BBQ US ab Feb./März mit derselben Pipeline) oder STOP.

## 6. Harte STOP/CONTINUE/SCALE-Kriterien (Teil 29)

**Herleitung aus der Wirtschaftlichkeit** (nicht frei gewählt). Für 5.000 € Gewinn in Monat 12 braucht es ≈5.600 € Provision (inkl. 600 € Kosten). Daraus folgt die nötige **Provision pro 1 Mio. Views (R)**:

| Markt | bei Strong-Reichweite (Monat 12) | bei Ausnahme-Reichweite |
|---|---|---|
| EN (Kitchen & Coffee) | 20 Mio. Views → **R ≥ 280 €** | 50 Mio. Views → **R ≥ 112 €** |
| DE (Spiegel) | 7 Mio. Views → R ≥ 800 € | 20 Mio. Views → **R ≥ 280 €** |

Liegt R nach 90 Tagen **unter 110 €** (EN), reicht selbst eine Top-Page mit 50 Mio. Views pro Monat nicht für 5k. Das ist die harte STOP-Schwelle.

### Nach 30 Tagen (≈ 45 EN-Reels, ≈ 20 DE-Reels)

| Kennzahl | STOP, wenn … | CONTINUE, wenn … | starkes Signal | Herleitung |
|---|---|---|---|---|
| Keyword-Kommentare pro 1.000 Views (Reels mit CTA) | < 1,0 | ≥ 2,0 | ≥ 5,0 | organische Basis ohne CTA 1,1/1.000 (Metricool); Modell Conservative 2 / Base 5 / Strong 10 (E, M1) |
| Affiliate-Klicks pro 1.000 Views (alle Pfade) | **< 0,3** | ≥ 0,6 | ≥ 1,5 | Conservative 0,25 / Base 1,2 (E, M2). Unter 0,3 liegt jede Nische bei < 15 € pro 1 Mio. Views |
| Median-Views pro Reel (EN) | < 300 **und** kein Reel > 5.000 | ≥ 800 | ≥ 3.000 | Socialinsider: 1–5k-Follower-Accounts 580 Views/Reel, 10–50k 2.460 (VERIFIED) |
| Shares + Saves pro 1.000 Views | < 3 | ≥ 6 | ≥ 10 | Metricool Shares 5,9/1.000; Socialinsider Saves 1,7–6/1.000 |
| Follower pro 1.000 Views | < 0,3 | ≥ 1 | ≥ 3 | kein öffentlicher Benchmark → MODEL ASSUMPTION |

**STOP nach 30 Tagen nur, wenn die Klick-Zeile UND die Views-Zeile im STOP-Bereich liegen.** Liegt nur eine davon dort, wird das Format bzw. der Hook umgebaut, nicht die Nische aufgegeben.

### Nach 60 Tagen

| Kennzahl | STOP | CONTINUE | SCALE-Signal | Herleitung |
|---|---|---|---|---|
| Views in Monat 2 (EN) | < 300.000 | ≥ 1 Mio. | ≥ 3 Mio. | Pfad zu 20 Mio. in Monat 12 braucht ≥ 2 Mio. in Monat 3 bei +30 %/Monat |
| Affiliate-Klicks pro 1.000 Views | < 0,5 | ≥ 0,8 | ≥ 2,0 | zwischen Conservative und Strong |
| EPC (Provision pro Klick, inkl. pending) | < 0,03 € (bei ≥ 2.000 Klicks) | ≥ 0,05 € | ≥ 0,12 € | Modell Base 0,085 € / Strong 0,167 €; Geniuslink typ. 0,03–0,10 $ |
| **R = Provision pro 1 Mio. Views (Monat 2)** | **< 20 €** | ≥ 50 € | ≥ 150 € | Modell Base 56 € / Strong 311 € |
| Bestellungen gesamt (Amazon + Händler) | < 20 | ≥ 50 | ≥ 200 | Base: 15 Bestellungen pro 1 Mio. Views |
| DE vs. EN | – | – | Budget-Umschichtung, wenn R_DE × Views_DE ≥ 1,5 × R_EN × Views_EN | Marktentscheidung per Messung statt Annahme |

### Nach 90 Tagen (Go/No-Go)

| Entscheidung | Bedingung (EN-Arm) | Begründung |
|---|---|---|
| **SCALE** (4 Reels/Tag, zweite Nische BBQ vorbereiten) | R ≥ 280 € **und** Views Monat 3 ≥ 2 Mio. **und** Wachstum ≥ +30 %/Monat | 5k € Gewinn bei Strong-Reichweite (20 Mio.) rechnerisch erreichbar |
| **CONTINUE** (3 Monate verlängern, Funnel optimieren) | 110 € ≤ R < 280 € **und** Views Monat 3 ≥ 1 Mio. | 5k nur mit Ausnahme-Reichweite; Hebel Klickrate noch offen |
| **PIVOT** (Pipeline auf BBQ US ab Feb./März) | R ≥ 110 €, aber Views Monat 3 < 1 Mio. | Funnel funktioniert, Reichweite der Nische nicht |
| **STOP** | **R < 110 €** nach Funnel-Optimierung **oder** Views Monat 3 < 300.000 | Selbst 50 Mio. Views pro Monat ergäben < 5k Gewinn |
| DE-Arm STOP | R_DE < 280 € | Selbst DE-Ausnahme-Reichweite (20 Mio.) reicht nicht für 5k |

**Zusatzkennzahl „Provision pro Reel“:** Die Kosten liegen bei ≈ 6,7 € pro Reel (600 € / 90). Verdient ein durchschnittliches Reel nach 90 Tagen weniger als die Hälfte davon (R × Views pro Reel < 3,35 €), ist die Page ohne Reichweitensprung dauerhaft defizitär.

**Was „nach Funnel-Optimierung“ heißt:** mindestens zwei A/B-Runden an CTA, DM-Flow und Linkziel, jeweils ≥ 10 Reels pro Variante. Erst danach gilt ein niedriges R als Nischenurteil und nicht als Umsetzungsfehler.

## 7. Wöchentliche Routine (nach Aufbau)

| Tag | Aufgabe | Zeit |
|---|---|---|
| Sa/So | Batch: Produkt-/Konzeptfreigabe, Generierung läuft maschinell, Clip-QA (Produkttreue!), Endabnahme, Planung der Woche | 6–9 h |
| Mo | KPI-Review (automatischer Report), Winner-Varianten anstoßen | 1 h |
| Mi/Fr | DMs und Kommentare, die die Automation nicht beantwortet; Link-Check | 2 × 0,5–1 h |
| monatlich | Amazon-CSV, Programm-Abgleich, Preis- und Verfügbarkeitscheck der verlinkten Produkte | 1–2 h |
