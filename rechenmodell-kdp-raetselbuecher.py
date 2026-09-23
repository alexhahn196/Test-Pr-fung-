"""Modell KDP-Rätselbücher (Großdruck, DE). Alle Parameter MODELLANNAHMEN.
Tantieme: 60 % x 9,99 € netto − Druck 0,75 + 0,012 x 120 S. = 2,19 € -> 3,80 €.
Auszahlung ca. 60 Tage nach Monatsende (KDP) -> Tantieme aus Monat m fließt in Monat m+2.
Werbung wird sofort bezahlt."""
ROY = 0.60*9.99 - (0.75+0.012*120)
M = ["M1","M2","M3","M4","M5","M6","M7","M8","M9"]
def run(name, pubs, spb, ad_share, cpa, fixed, one_off, start, h_book, h_fix, ramp=(0.2,0.6,1.0), refund=0.02):
    cash = start-one_off; live=[]; roy_hist=[]; cum=-one_off; rows=[]; minc=cash
    for m in range(9):
        live.append(pubs[m])
        # Verkäufe: jedes Buch braucht 3 Monate Anlauf
        sales=0
        for age_idx,n in enumerate(live):
            age=m-age_idx
            f=ramp[min(age,len(ramp)-1)]
            sales+=n*spb[m]*f
        roy=sales*ROY*(1-refund)
        ads=sales*ad_share[m]*cpa[m]
        profit=roy-ads-fixed
        cum+=profit
        roy_hist.append(roy)
        paid=roy_hist[m-2] if m>=2 else 0
        cash+=paid-ads-fixed
        minc=min(minc,cash)
        hours=pubs[m]*h_book+h_fix
        rows.append((M[m],sum(live),pubs[m],sales,roy,ads,fixed,profit,paid,cash,cum,hours))
    print(f"\n#### {name}\n")
    print("| Monat | neue Titel | Titel gesamt | Verkäufe | Tantiemen (Umsatz netto) | Werbung | Werkzeuge/Fix | **Gewinn** | ausgezahlt | Kasse Monatsende | kum. Ergebnis | deine Std. |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    f=lambda x:f"{x:,.0f}".replace(",",".")
    for r in rows:
        print(f"| {r[0]} | {r[2]} | {r[1]} | {f(r[3])} | {f(r[4])} | {f(r[5])} | {f(r[6])} | **{f(r[7])}** | {f(r[8])} | {f(r[9])} | {f(r[10])} | {r[11]:.1f} |")
    print(f"\nniedrigster Kassenstand: {f(minc)} €")
    return rows
fixed=40
# Budget B: 5 h/Woche ≈ 21,7 h/Monat; h_book 1,5 h; h_fix 5 h (Werbung, Verwaltung, Kontrolle)
pubsB=[2,4,8,10,10,10,10,10,10]
pubsA=[2,2,3,3,3,3,3,3,3]  # Budget A: 8,7 h/Monat; h_fix 3,5
if __name__=="__main__":
    print("Tantieme je Verkauf:", round(ROY,2))
    run("Schwach (Budget B, 5 h/Woche)", pubsB, [1]*9, [0.7]*9, [3.0]*9, fixed, 60, 2500, 1.5, 5)
    run("Plausibel (Budget B, 5 h/Woche)", pubsB, [4]*9, [0.6]*9, [2.0]*9, fixed, 60, 2500, 1.5, 5)
    run("Ziel 5.000 € (Budget B, 5 h/Woche)", pubsB, [60]*9, [0.5]*9, [1.2]*9, fixed, 60, 2500, 1.5, 5)
    run("Plausibel (Budget A, 2 h/Woche)", pubsA, [4]*9, [0.6]*9, [2.0]*9, fixed, 60, 2500, 1.5, 3.5)
