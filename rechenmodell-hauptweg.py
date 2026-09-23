"""Sechsmonats- und Liquiditätsmodell für den Hauptweg
(Festpreis-Website-Relaunch für Handwerksbetriebe + optionales Pflege-Abo).

Alle Werte netto (ohne USt). Alle Parameter sind MODELLANNAHMEN, keine Branchenfakten.
Monat 1 = 24.09.–23.10.2026 ... Monat 6 endet am 23.03.2027, Monat 9 am 23.06.2027.
Umsatz wird im Auftragsmonat verbucht (Fertigstellung binnen ~14 Tagen angenommen);
Zahlung: 50 % Anzahlung bei Auftrag, 50 % Schlussrechnung, bezahlt im Folgemonat.
"""

MONTHS = ["M1 (bis 23.10.26)", "M2 (bis 23.11.26)", "M3 (bis 23.12.26)", "M4 (bis 23.01.27)",
          "M5 (bis 23.02.27)", "M6 (bis 23.03.27)", "M7 (bis 23.04.27)", "M8 (bis 23.05.27)",
          "M9 (bis 23.06.27)"]


def run(p):
    rows = []
    cash = p["start_cash"] - p["one_off"]
    subs = 0.0
    receivable = 0.0
    cum = -p["one_off"]
    cum_hours = 0.0
    n_done = 0
    cash_min = cash
    for m, d in enumerate(p["deals"]):
        rev_proj = 0.0
        for _ in range(d):
            rev_proj += p["pilot_price"] if n_done < p["pilot_n"] else p["price"]
            n_done += 1
        # Pflege-Abos starten im Monat nach dem Launch
        new_subs = p["attach"] * (p["deals"][m - 1] if m >= 1 else 0)
        subs = subs * (1 - p["churn"]) + new_subs
        rev_sub = subs * p["sub_price"]
        revenue = rev_proj + rev_sub
        c_var = d * p["var_cost"] + subs * p["sub_cost"]
        c_bad = p["bad_debt"] * 0.5 * rev_proj
        c_ads = p["ads"][m]
        c_tools = p["tools"][m]
        c_help = p["help"][m]
        c_travel = p["travel"][m]
        costs = c_var + c_bad + c_ads + c_tools + c_help + c_travel
        profit = revenue - costs
        cum += profit
        cash_in = 0.5 * rev_proj + receivable * (1 - p["bad_debt"]) + rev_sub
        cash_out = c_var + c_ads + c_tools + c_help + c_travel
        receivable = 0.5 * rev_proj
        cash += cash_in - cash_out
        cash_min = min(cash_min, cash)
        hours = (d * p["h_proj"] + p["h_acq"][m] + p["h_admin"] + subs * p["h_sub"]
                 + p["h_setup"][m])
        cum_hours += hours
        rows.append(dict(month=MONTHS[m], deals=d, rev_proj=rev_proj, subs=subs, rev_sub=rev_sub,
                         revenue=revenue, var=c_var + c_bad, ads=c_ads, tools=c_tools,
                         help=c_help, travel=c_travel, profit=profit, cash_in=cash_in,
                         cash_out=cash_out, receivable=receivable, cash=cash, cum=cum,
                         hours=hours, cum_hours=cum_hours, contacts=p["contacts"][m]))
    return rows, cash_min


def fmt(x):
    return f"{x:,.0f}".replace(",", ".")


def show(name, p, own_rate=25.0):
    rows, cash_min = run(p)
    print(f"\n### {name}\n")
    hdr = ("Monat", "Kontakt-versuche", "Aufträge", "Umsatz netto", "davon Abos", "var. Kosten + Ausfall",
           "Werbung/Briefe", "Werkzeuge", "Fremdhilfe", "Fahrten", "**Gewinn**", "Einzahlungen",
           "Auszahlungen", "offene Forderung", "Kasse Monatsende", "kum. Ergebnis", "Std.",
           f"Gewinn − Eigenarbeit à {own_rate:.0f} €/h")
    print("| " + " | ".join(hdr) + " |")
    print("|" + "---|" * len(hdr))
    for r in rows:
        vals = [r["month"], str(int(r["contacts"])), str(r["deals"]), fmt(r["revenue"]), fmt(r["rev_sub"]), fmt(r["var"]),
                fmt(r["ads"]), fmt(r["tools"]), fmt(r["help"]), fmt(r["travel"]),
                "**" + fmt(r["profit"]) + "**", fmt(r["cash_in"]), fmt(r["cash_out"]),
                fmt(r["receivable"]), fmt(r["cash"]), fmt(r["cum"]), f"{r['hours']:.0f}",
                fmt(r["profit"] - r["hours"] * own_rate)]
        print("| " + " | ".join(vals) + " |")
    six = rows[5]
    print(f"\nStart-Kasse {fmt(p['start_cash'])} €, Einmalkosten {fmt(p['one_off'])} €; "
          f"niedrigster Kassenstand {fmt(cash_min)} €; Stunden M1–M6: {rows[5]['cum_hours']:.0f}; "
          f"kum. Ergebnis M6: {fmt(six['cum'])} €; M9: {fmt(rows[-1]['cum'])} €")
    # Monat, in dem das kumulierte Ergebnis >= 0 (Anfangsinvestition zurückverdient)
    be = next((r["month"] for r in rows if r["cum"] >= 0), "nach M9")
    print(f"Anfangsinvestition (Einmalkosten + Anlaufverluste) zurückverdient: {be}")
    cum_own = 0.0 - p["one_off"]
    be_own = "nach M9"
    for r in rows:
        cum_own += r["profit"] - r["hours"] * own_rate
        if cum_own >= 0 and be_own == "nach M9":
            be_own = r["month"]
    print(f"Kumuliert inkl. Eigenarbeit à {own_rate:.0f} €/h nach M9: {fmt(cum_own)} €; zurückverdient inkl. Eigenarbeit: {be_own}")
    print(f"Effektiver Stundenlohn M6 (Gewinn/Std.): {six['profit'] / six['hours']:.1f} €/h")
    return rows


BASE_TOOLS = 7 + 25 + 15 + 13 + 1 + 20  # Workspace, Rechtstexte, IT-Haftpflicht, Buchhaltung, Domain, Telefon-Anteil

weak = dict(
    start_cash=2500, one_off=490,
    deals=[0, 1, 1, 2, 1, 2, 1, 2, 1],
    pilot_price=790, pilot_n=2, price=1190,
    sub_price=39, attach=0.4, churn=0.03, sub_cost=2,
    var_cost=40, bad_debt=0.05,
    ads=[85, 250, 250, 130, 130, 130, 130, 130, 130],  # M1: 60 Test-Briefe
    tools=[BASE_TOOLS + 20] * 9,
    help=[0, 0, 0, 0, 0, 0, 0, 0, 0],
    travel=[60, 80, 80, 80, 80, 80, 80, 80, 80],
    h_proj=20, h_acq=[32, 50, 50, 50, 50, 50, 50, 50, 50], h_admin=12, h_sub=0.5,
    h_setup=[30, 20, 5, 5, 5, 5, 5, 5, 5],
    # M1 = Test: 40 Besuche (à 0,5 h) + 60 Briefe (à 0,2 h); danach 100 Versuche à Ø 0,5 h
    contacts=[100, 100, 100, 100, 100, 100, 100, 100, 100],
)

plausible = dict(weak)
plausible.update(
    deals=[0, 2, 2, 2, 3, 3, 3, 3, 3],
    price=1290, attach=0.6, churn=0.02, bad_debt=0.03,
    ads=[85, 250, 250, 200, 200, 200, 200, 200, 200],
    tools=[BASE_TOOLS + 20] + [BASE_TOOLS + 100 + 20] * 8,
    help=[0, 0, 0, 150, 150, 150, 150, 150, 150],
    travel=[60, 100, 120, 120, 120, 120, 120, 120, 120],
    h_proj=15,
)

target = dict(plausible)
target.update(
    deals=[0, 2, 3, 3, 4, 4, 4, 4, 4],
    price=1490, attach=0.7, churn=0.02, bad_debt=0.02,
    ads=[85, 250, 250, 400, 400, 400, 400, 400, 400],
    tools=[BASE_TOOLS + 100 + 20] * 9,
    travel=[60, 120, 150, 150, 150, 150, 150, 150, 150],
    h_proj=12,
    h_acq=[32, 50, 50, 50, 50, 50, 50, 50, 50],
)

if __name__ == "__main__":
    show("Schwaches Szenario (2.500 € Startkapital)", weak)
    show("Plausibles Planungsszenario (2.500 € Startkapital)", plausible)
    show("Ziel-Szenario 5.000 € (2.500 € Startkapital)", target)
    # Kapitalvarianten
    for sc in (1000, 2500, 5000):
        for nm, p in (("schwach", weak), ("plausibel", plausible), ("Ziel", target)):
            q = dict(p)
            q["start_cash"] = sc
            if sc == 1000:
                q["one_off"] = 90
                q["ads"] = [0] * 9
            rows, cmin = run(q)
            print(f"Kapital {sc}: {nm}: min Kasse {fmt(cmin)}, Kasse M6 {fmt(rows[5]['cash'])}, "
                  f"Gewinn M6 {fmt(rows[5]['profit'])}")
    # Kapazitätsrechnung nach Wochenstunden (Dauerzustand ab ca. M4)
    print("\n### Kapazität nach Wochenstunden (Dauerzustand)\n")
    print("| Wochenstunden | Szenario | verfügbare Std./Monat für Akquise+Projekte | Std. je Auftrag (Lieferung + Akquise) | max. Aufträge/Monat | Monatsgewinn bei dieser Menge |")
    print("|---|---|---|---|---|---|")
    for wh in (10, 20, 40):
        avail = wh * 4.33 - 12 - 5  # Admin, Pflege/Sonstiges
        for nm, p, cpd, price, fixed in (("schwach", weak, 60, 1190, 250),
                                          ("plausibel", plausible, 35, 1290, 600),
                                          ("Ziel", target, 25, 1490, 800)):
            h_deal = p["h_proj"] + cpd * 0.5
            n = avail / h_deal
            contrib = price - p["var_cost"] - p["bad_debt"] * 0.5 * price
            prof = n * contrib - fixed
            print(f"| {wh} | {nm} | {avail:.0f} | {h_deal:.1f} | {n:.1f} | {fmt(prof)} |")
