"""Erzeugt Markdown-Tabellen aus model_output.json für die Berichte (python3 scripts/md_tables.py > scripts/generated_tables.md)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(os.path.join(ROOT, "scripts", "model_output.json"), encoding="utf-8"))
by = {d["id"]: d for d in D}
def n(x, d=0):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")
def mio(x):
    return n(x / 1e6, 1) + " Mio."
TOP = ["K32", "K31", "K06", "K13", "K09", "K12", "K07", "K17", "K04", "K01", "K08", "K10"]

print("## T1 – Provision pro Bestellung und benötigte Bestellungen (Teil 12)\n")
print("| # | Kombination | AOV gewichtet (€) | Provision gewichtet | Provision/Bestellung nominal (€) | effektiv nach USt & Retouren (€) | Bestellungen für 3.000 € | 5.000 € | 10.000 € | 20.000 € |")
print("|---|---|---|---|---|---|---|---|---|---|")
for d in D:
    s = d["struct"]; e = s["comm_per_order_eff_eur"]
    print(f"| {d['rank']} | {d['label']} | {n(s['aov_eur'])} | {n(s['comm_rate_weighted']*100,1)} % | {n(s['comm_per_order_nominal_eur'],2)} | {n(e,2)} | {n(3000/e)} | {n(5000/e)} | {n(10000/e)} | {n(20000/e)} |")

print("\n## T2 – Rückrechnung wie im Beispiel (Teil 14), Base-Szenario, Ziel 10.000 € Provision\n")
print("| Kombination | Provision/Bestellung eff. (€) | Bestellungen | Ø CVR Klick→Bestellung | Shop-Besucher (monetarisierbare Klicks) | Klicks pro 1.000 Views (monetarisierbar) | benötigte Views |")
print("|---|---|---|---|---|---|---|")
for k in TOP:
    d = by[k]; e = d["struct"]["comm_per_order_eff_eur"]; b = d["Base"]
    orders = 10000 / e; clicks = orders / b["blended_cvr"]; ctr = b["clicks_monetizable_per_1m"] / 1e3
    print(f"| {d['label']} | {n(e,2)} | {n(orders)} | {n(b['blended_cvr']*100,2)} % | {n(clicks)} | {n(ctr,2)} | {mio(clicks/ctr*1000)} |")

print("\n## T3 – Funnel je Szenario (pro 1 Mio. Views)\n")
for k in TOP:
    d = by[k]
    print(f"\n**{d['label']}** (Score {n(d['score'],1)})\n")
    print("| Szenario | monetarisierbare Klicks | Ø CVR | Bestellungen | Provision (€) | EPC (€/Klick) | Views für 5k Gewinn | 10k | 20k |")
    print("|---|---|---|---|---|---|---|---|---|")
    for s in ["Conservative", "Base", "Strong", "Exceptional"]:
        x = d[s]
        print(f"| {s} | {n(x['clicks_monetizable_per_1m'])} | {n(x['blended_cvr']*100,2)} % | {n(x['orders_per_1m'],1)} | {n(x['revenue_per_1m_eur'])} | {n(x['epc_eur'],3)} | {mio(x['views_5k'])} | {mio(x['views_10k'])} | {mio(x['views_20k'])} |")

print("\n## T4 – Provision pro 1 Mio. Views, alle Kombinationen (Teil 15)\n")
print("| Rang | Kombination | Conservative | Base | Strong | Exceptional |")
print("|---|---|---|---|---|---|")
for d in sorted(D, key=lambda x: -x["Base"]["revenue_per_1m_eur"]):
    print(f"| {d['rank']} | {d['label']} | {n(d['Conservative']['revenue_per_1m_eur'])} € | {n(d['Base']['revenue_per_1m_eur'])} € | {n(d['Strong']['revenue_per_1m_eur'])} € | {n(d['Exceptional']['revenue_per_1m_eur'])} € |")

print("\n## T5 – Views für Gewinnziele vs. realistische Reichweite (Teil 16)\n")
print("| Kombination | Views für 5k (Base / Strong) | 10k (Base / Strong) | 20k (Base / Strong) | realist. Views Monat 12 (Base / Strong / Ausnahme) | Gewinn/Monat: Base×Base · Strong×Strong · Exc×Exc |")
print("|---|---|---|---|---|---|")
for k in TOP + ["K19", "K14", "K15", "K05", "K03", "K29", "K20", "K18", "K11", "K02", "K23"]:
    d = by[k]
    print(f"| {d['label']} | {mio(d['Base']['views_5k'])} / {mio(d['Strong']['views_5k'])} | {mio(d['Base']['views_10k'])} / {mio(d['Strong']['views_10k'])} | {mio(d['Base']['views_20k'])} / {mio(d['Strong']['views_20k'])} | {mio(d['reach_base'])} / {mio(d['reach_strong'])} / {mio(d['reach_exc'])} | {n(d['profit_base_reach_base'])} € · {n(d['profit_strong_reach_strong'])} € · {n(d['profit_exc_reach_exc'])} € |")

print("\n## T6 – Scorecard (Teil 23)\n")
print("| Rang | Kombination | Score | Econ (20 %) | Intent (15 %) | Viral (15 %) | Comp (10 %) | AI (10 %) | Passiv (10 %) | Markt (5 %) | Vielfalt (5 %) | Compliance (5 %) | Cross (5 %) |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for d in D:
    v = d["vals"]
    print(f"| {d['rank']} | {d['label']}{' *' if d['synth'] else ''} | **{n(d['score'],1)}** | {n(v['econ'],1)} | {v['intent']} | {v['viral']} | {v['comp']} | {v['ai']} | {v['passiv']} | {v['intl']} | {v['variety']} | {v['compliance']} | {v['cross']} |")
