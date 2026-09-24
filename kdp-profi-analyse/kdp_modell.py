"""Ausführbares Rechenmodell: KDP-Rätselbuch-Portfolio (Stand der Parameter: 24.09.2026).

Aufruf:
    python3 kdp_modell.py            # alle Auswertungen
    python3 kdp_modell.py --test     # nur Plausibilitätsprüfungen

Kennzeichnung der Parameter:  [BF] belegter Fakt (Quelle in quellen.md),
[MA] Modellannahme, [SCH] Schätzung. Alle Beträge in EUR, sofern nicht anders angegeben.
Das Modell erzeugt KEINE Prognose, sondern zeigt, was unter den jeweiligen Annahmen folgt.
"""
import math
import random
import statistics
import sys

# --------------------------------------------------------------------------- Parameter
USD_EUR = 0.86                      # [MA] Wechselkurs; KDP rechnet mit eigenem Kurs um [BF]

MARKETS = {
    # Druckkosten Large Trim (8,5x11 in), s/w, 110–828 Seiten [BF, KDP G201834340]
    # Tantieme 60 % ab Listenpreis 9,99 (netto) sonst 50 % [BF, KDP G201834330]
    "amazon.de":  {"fix": 0.75, "per_page": 0.016, "fx": 1.0,     "vat": 0.19},
    "amazon.com": {"fix": 1.00, "per_page": 0.017, "fx": USD_EUR, "vat": 0.0},
}
# USt auf nicht-periodische Sudoku-Bücher in DE: 19 % laut Sekundärquelle (EuGH C-375/24) [SCH]
# Für US-Verkäufe wird Sales Tax aufgeschlagen; Listenpreis = Nettopreis [BF, KDP G8BKPU9AGVZSF9QF]

BOOK = {"pages": 130, "price": 10.99}          # [MA] 100 Rätsel + Lösungsteil, Listenpreis netto

PERF_CLASSES = {
    # Anteil der Titel [MA] und stabile Monatsverkäufe je Titel nach Anlauf [MA]
    # Gestützt nur auf: Pareto-Aussagen von Praktikern (80/20) [SCH] und Katalogwerte
    # geprüfter Inserate (~30–75 $ Gewinn je Titel und Monat) [BF, Empire Flippers/Flippa]
    "schwach":   {"hit": (0.02, 60), "mittel": (0.15, 12), "klein": (0.43, 3), "null": (0.40, 0.3)},
    "plausibel": {"hit": (0.05, 120), "mittel": (0.20, 20), "klein": (0.45, 5), "null": (0.30, 0.5)},
    "stark":     {"hit": (0.08, 250), "mittel": (0.25, 35), "klein": (0.42, 8), "null": (0.25, 1)},
}
RAMP = [0.2, 0.5, 0.8, 1.0]         # [MA] Anlauf in den ersten Monaten
DECAY_AFTER = 9                     # [MA] ab Monat 9 nach Start nachlassende Verkäufe
DECAY = 0.02                        # [MA] 2 % pro Monat
CANNIBAL_K = 0.10                   # [MA] Nachfragedämpfung je zusätzlichem Titel derselben Linie
LINE_SIZE = 10                      # [MA] Titel pro Produktlinie
SEASON = {1: 0.8, 2: 0.85, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.85, 7: 0.85, 8: 0.9,
          9: 1.0, 10: 1.2, 11: 1.8, 12: 2.2}   # [SCH] Q4-Spitze laut Praktikern (2–3x) [SCH]
START_CAL_MONTH = 10                # Monat 1 = Oktober 2026

AD_SHARE = 0.55                     # [MA] Anteil werbezugerechneter Verkäufe
CPA0 = {"schwach": 3.0, "plausibel": 2.2, "stark": 1.6}  # [MA] € je Werbeverkauf bei kleinem Volumen
CPA_GROWTH = 0.25                   # [MA] +25 % je Verzehnfachung des Werbevolumens
REFUND = 0.02                       # [MA] Rückgaben/Verrechnungen
PAYOUT_LAG = 2                      # [BF] ca. 60 Tage nach Monatsende

PLATFORM_CAP_PER_MONTH = 8          # [BF] max. 2 Titel je Format und Woche (KDP G202172740)
FIXED_COSTS = 45.0                  # [MA] Claude Pro 20 €, Buchhaltungs-Tool, Konto, Kleinkram

HOURS = {"per_title": 1.5,          # [MA] Prüfung 25 min, Metadaten 10, Upload 25, Rest
         "fixed": 3.5,              # [MA] Werbeentscheidung 4x30 min, Verwaltung, Mails
         "per_10_active": 0.3}      # [MA] Portfolio-Kontrolle
BUDGETS = {"A": 2 * 4.33, "B": 5 * 4.33}
OWN_RATE = 25.0                     # [MA] Wert einer eigenen Arbeitsstunde

TEAM = {"va_rate": 15 * USD_EUR * 1.0,   # [SCH] VA Median ~13 $/h (Upwork), gerundet 15 $
        "qa_rate": 40.0,                 # [SCH] Fach-/Satzprüfung je Stunde
        "ads_mgr_month": 800.0,          # [SCH] externer Werbe-Manager ab großem Portfolio
        "va_h_per_title": 1.0, "qa_h_per_title": 0.5,
        "owner_h_per_month_team": 12.0}  # [MA] deine Führungsarbeit mit Team (≈ 3 h/Woche)

# --------------------------------------------------------------------------- Formeln
def royalty(market, price=BOOK["price"], pages=BOOK["pages"]):
    """Tantieme je Verkauf in EUR = Satz × Listenpreis − Druckkosten (KDP-Formel)."""
    m = MARKETS[market]
    rate = 0.60 if price >= 9.99 else 0.50
    print_cost = m["fix"] + m["per_page"] * pages
    return (rate * price - print_cost) * m["fx"]


def end_customer_price(market, price=BOOK["price"]):
    return price * (1 + MARKETS[market]["vat"]) * MARKETS[market]["fx"]


def cpa(scenario, ad_sales):
    return CPA0[scenario] * (1 + CPA_GROWTH * math.log10(1 + ad_sales / 100))


def contribution(market, scenario, ad_sales=100):
    r = royalty(market) * (1 - REFUND)
    return r - AD_SHARE * cpa(scenario, ad_sales)


def break_even_acos(market):
    """Werbekosten dürfen je Werbeverkauf höchstens die Tantieme betragen.
    ACOS-Bezugsgröße: Werbekosten / Endkundenumsatz des Werbeverkaufs (Konsole, ob brutto/netto UNGEKLÄRT)."""
    return royalty(market) / BOOK["price"] / MARKETS[market]["fx"] * MARKETS[market]["fx"]

# --------------------------------------------------------------------------- Simulation
def simulate(scenario, budget, months=12, market="amazon.com", seed=0, pubs_override=None,
             start_cash=2500.0, test_ads=0.0):
    rng = random.Random(seed)
    classes = PERF_CLASSES[scenario]
    names = list(classes)
    weights = [classes[n][0] for n in names]
    titles = []                       # (start_month, base_sales, line)
    rows, roy_hist, cash, cum = [], [], start_cash, 0.0
    r_unit = royalty(market) * (1 - REFUND)
    for m in range(months):
        active = sum(1 for t in titles if t["alive"])
        h_fixed = HOURS["fixed"] + HOURS["per_10_active"] * active / 10
        cap_time = max(0, int((BUDGETS[budget] - h_fixed) // HOURS["per_title"]))
        new = min(PLATFORM_CAP_PER_MONTH, cap_time)
        if pubs_override is not None:
            new = min(new, pubs_override[m])
        for _ in range(new):
            cls = rng.choices(names, weights)[0]
            titles.append({"start": m, "base": classes[cls][1], "cls": cls,
                           "line": len(titles) // LINE_SIZE, "alive": True})
        cal = (START_CAL_MONTH - 1 + m) % 12 + 1
        sales = 0.0
        per_line = {}
        for t in titles:
            per_line[t["line"]] = per_line.get(t["line"], 0) + 1
        for t in titles:
            if not t["alive"]:
                continue
            age = m - t["start"]
            f = RAMP[min(age, len(RAMP) - 1)]
            if age > DECAY_AFTER:
                f *= (1 - DECAY) ** (age - DECAY_AFTER)
            f *= 1 / (1 + CANNIBAL_K * (per_line[t["line"]] - 1))
            s = t["base"] * f * SEASON[cal]
            # Einstellen: Titel ohne nennenswerte Verkäufe nach 4 Monaten -> keine Werbung mehr
            if age >= 4 and t["cls"] == "null":
                t["alive"] = False
            sales += s
        royalties = sales * r_unit
        ad_sales = sales * AD_SHARE
        ads = ad_sales * cpa(scenario, ad_sales) + (test_ads if m < 2 else 0)
        profit = royalties - ads - FIXED_COSTS
        cum += profit
        roy_hist.append(royalties)
        paid = roy_hist[m - PAYOUT_LAG] if m >= PAYOUT_LAG else 0.0
        cash += paid - ads - FIXED_COSTS
        hours = h_fixed + new * HOURS["per_title"]
        rows.append({"m": m + 1, "cal": cal, "new": new, "titles": len(titles),
                     "active": sum(1 for t in titles if t["alive"]), "sales": sales,
                     "revenue_customer": sales * end_customer_price(market),
                     "royalties": royalties, "ads": ads, "profit": profit, "paid": paid,
                     "cash": cash, "cum": cum, "hours": hours,
                     "profit_after_time": profit - hours * OWN_RATE,
                     "within_budget": hours <= BUDGETS[budget] + 1e-9})
    return rows


def monte_carlo(scenario, budget, months=12, n=300, market="amazon.com"):
    finals = [simulate(scenario, budget, months, market, seed=s)[-1]["profit"] for s in range(n)]
    finals.sort()
    return finals[int(0.1 * n)], statistics.median(finals), finals[int(0.9 * n)]

# --------------------------------------------------------------------------- Gewinnstufen
def stage_table(market="amazon.com"):
    out = []
    for target in (5000, 10000, 25000, 50000, 100000):
        row = {"ziel": target}
        for sc in ("schwach", "plausibel", "stark"):
            # iterativ, weil CPA mit Volumen steigt
            sales = target / max(contribution(market, sc), 0.01)
            for _ in range(20):
                c = contribution(market, sc, ad_sales=sales * AD_SHARE)
                sales = (target + FIXED_COSTS) / c if c > 0 else float("inf")
            classes = PERF_CLASSES[sc]
            mean_per_title = sum(w * s for w, s in classes.values())
            titles = sales / mean_per_title
            months_cap = titles / PLATFORM_CAP_PER_MONTH
            row[sc] = {"verkaeufe": sales, "tantiemen": sales * royalty(market) * (1 - REFUND),
                       "werbung": sales * AD_SHARE * cpa(sc, sales * AD_SHARE),
                       "titel": titles, "monate_nur_durch_upload_limit": months_cap,
                       "h_strict": HOURS["fixed"] + HOURS["per_10_active"] * titles / 10
                       + PLATFORM_CAP_PER_MONTH * HOURS["per_title"]}
        out.append(row)
    return out


def team_cost(titles_per_month, active_titles):
    va = titles_per_month * TEAM["va_h_per_title"] * TEAM["va_rate"]
    qa = titles_per_month * TEAM["qa_h_per_title"] * TEAM["qa_rate"]
    ads = TEAM["ads_mgr_month"] if active_titles > 150 else 0.0
    return va + qa + ads

# --------------------------------------------------------------------------- Prüfungen
def plausibility_checks():
    checks = []
    for mk in MARKETS:
        r = royalty(mk)
        checks.append((f"Tantieme {mk} positiv und kleiner als Listenpreis", 0 < r < BOOK["price"]))
    # Handrechnung amazon.de: 0,6*10,99 - (0,75+0,016*130) = 6,594 - 2,83 = 3,764
    checks.append(("Tantieme amazon.de = 3,76 € (Handrechnung)", abs(royalty("amazon.de") - 3.764) < 0.01))
    checks.append(("Unter 9,99 gilt 50 %", abs(royalty("amazon.de", price=8.99) -
                                              (0.5 * 8.99 - 2.83)) < 0.01))
    checks.append(("CPA steigt mit Volumen", cpa("plausibel", 10000) > cpa("plausibel", 10)))
    rows = simulate("plausibel", "A", 6)
    checks.append(("Budget A wird in keinem Monat überschritten", all(r["within_budget"] for r in rows)))
    rows = simulate("plausibel", "B", 6)
    checks.append(("Budget B wird in keinem Monat überschritten", all(r["within_budget"] for r in rows)))
    checks.append(("Upload-Limit eingehalten", all(r["new"] <= PLATFORM_CAP_PER_MONTH for r in rows)))
    checks.append(("Auszahlung verzögert (M1–M2 = 0)", rows[0]["paid"] == 0 and rows[1]["paid"] == 0))
    ok = True
    for name, res in checks:
        print(("OK   " if res else "FEHLER ") + name)
        ok &= res
    return ok


def fmt(x):
    return f"{x:,.0f}".replace(",", ".")


def print_sim(title, rows):
    print(f"\n#### {title}\n")
    print("| Monat | neue Titel | Titel ges. | Verkäufe | Endkundenumsatz | Tantiemen | Werbung | "
          "**op. Gewinn** | ausgezahlt | Kasse | kum. Gewinn | deine Std. | Gewinn − Zeit à 25 €/h |")
    print("|" + "---|" * 13)
    for r in rows:
        print(f"| M{r['m']} | {r['new']} | {r['titles']} | {fmt(r['sales'])} | {fmt(r['revenue_customer'])} | "
              f"{fmt(r['royalties'])} | {fmt(r['ads'])} | **{fmt(r['profit'])}** | {fmt(r['paid'])} | "
              f"{fmt(r['cash'])} | {fmt(r['cum'])} | {r['hours']:.1f} | {fmt(r['profit_after_time'])} |")


def main():
    print("## Plausibilitätsprüfungen\n")
    if not plausibility_checks():
        sys.exit(1)
    if "--test" in sys.argv:
        return
    print("\n## Stückökonomie\n")
    for mk in MARKETS:
        print(f"- {mk}: Listenpreis {BOOK['price']} netto, Endkundenpreis ≈ {end_customer_price(mk):.2f} €, "
              f"Tantieme {royalty(mk):.2f} €/Stück, Break-even-Werbekosten je Werbeverkauf {royalty(mk):.2f} €, "
              f"Deckungsbeitrag (plausibel, kleines Volumen) {contribution(mk, 'plausibel'):.2f} €")
    print("\n## Gewinnstufen (amazon.com-Ökonomie, stationär, ohne Saison)\n")
    print("| Ziel €/Monat | Szenario | nötige Verkäufe/Monat | Tantiemen | Werbung | bedingt nötige Titel | "
          "Monate allein wegen Upload-Limit (8/Monat) |")
    print("|---|---|---|---|---|---|---|")
    for row in stage_table():
        for sc in ("schwach", "plausibel", "stark"):
            d = row[sc]
            print(f"| {fmt(row['ziel'])} | {sc} | {fmt(d['verkaeufe'])} | {fmt(d['tantiemen'])} | "
                  f"{fmt(d['werbung'])} | {fmt(d['titel'])} | {d['monate_nur_durch_upload_limit']:.0f} |")
    print("\n## Monte-Carlo: Monatsgewinn in Monat 6 und 12 (P10 / Median / P90), 300 Läufe\n")
    print("| Szenario | Budget | M6 P10 | M6 Median | M6 P90 | M12 P10 | M12 Median | M12 P90 |")
    print("|---|---|---|---|---|---|---|---|")
    for sc in ("schwach", "plausibel", "stark"):
        for b in ("A", "B"):
            a6 = monte_carlo(sc, b, 6)
            a12 = monte_carlo(sc, b, 12)
            print(f"| {sc} | {b} | " + " | ".join(fmt(x) for x in a6 + a12) + " |")
    plan = [2, 2, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8]   # Test zuerst, Ausbau erst ab M4 [MA]
    for sc in ("schwach", "plausibel", "stark"):
        print_sim(f"Szenario {sc}, Budget B (5 h/Woche), Seed 1, Startkasse 2.500 €, "
                  f"Werbetest 250 €/Monat in M1–M2, Veröffentlichungsplan {plan}",
                  simulate(sc, "B", 12, seed=1, test_ads=250, pubs_override=plan))
    print_sim(f"Szenario plausibel, Budget A (2 h/Woche), Seed 1, Plan {plan} (durch Zeit begrenzt)",
              simulate("plausibel", "A", 12, seed=1, test_ads=250, pubs_override=plan))
    print("\n## Zielszenario: Welche Klassenverteilung bräuchte 5.000 € in Monat 6? (Budget B, Plan wie oben)\n")
    for hit_sales in (250, 500, 1000, 2000):
        PERF_CLASSES["ziel"] = {"hit": (0.08, hit_sales), "mittel": (0.25, 35), "klein": (0.42, 8), "null": (0.25, 1)}
        CPA0["ziel"] = 1.6
        runs = sorted(simulate("ziel", "B", 6, seed=s, test_ads=250, pubs_override=plan)[-1]["profit"] for s in range(300))
        print(f"- Hit-Titel mit {hit_sales} Verkäufen/Monat (8 % der Titel): M6-Gewinn Median {fmt(statistics.median(runs))} €, P90 {fmt(runs[270])} €")
    print("\n## Variante B (Team) – Kosten je Ausbaustufe (SCH)\n")
    print("| neue Titel/Monat | aktive Titel | Teamkosten/Monat | deine Führungsstunden/Monat |")
    print("|---|---|---|---|")
    for tpm, act in ((8, 50), (8, 150), (16, 300), (16, 600)):
        print(f"| {tpm} | {act} | {fmt(team_cost(tpm, act))} | {TEAM['owner_h_per_month_team'] + act / 100:.0f} |")
    print("\nHinweis: 16 Titel/Monat nur mit Taschenbuch + Hardcover (2 Formate) möglich; "
          "ein zweites KDP-Konto ist laut AGB nicht zulässig [BF].")


if __name__ == "__main__":
    main()
