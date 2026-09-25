# Quantitatives Modell v2: Views -> Klicks -> Bestellungen -> GMV -> Provision -> Kosten -> Gewinn
# Alle Annahmen dokumentiert; Quellen siehe Bericht Kapitel 5.
import json
FX = 0.92   # EUR je USD (Annahme; im Bericht ausgewiesen)
# Verteilung je 100 Videos (Kapitel 10): mittlere Views pro Video
DIST = {'konservativ': 86_500/100, 'realistisch': 396_500/100, 'aggressiv': 1_664_000/100}
SCEN = {
  # ctr = Views -> Produktklick; cvr = Klick -> Bestellung; aov in USD; comm = Provisionssatz; ret = Storno/Retoure-Quote
  'konservativ': dict(ctr=0.010, cvr=0.025, aov=30, comm=0.10, ret=0.15, cost_var=3.0, fixed=190, surv=0.60),
  'realistisch': dict(ctr=0.020, cvr=0.040, aov=38, comm=0.15, ret=0.10, cost_var=3.0, fixed=190, surv=0.75),
  'aggressiv':   dict(ctr=0.030, cvr=0.040, aov=35, comm=0.20, ret=0.07, cost_var=1.8, fixed=40,  surv=0.85),
}
TARGETS = [3000, 5000, 10000, 20000]
def per_view(p):
    orders_per_1k = p['ctr']*p['cvr']*1000
    gmv_per_1k = orders_per_1k*p['aov']
    comm_per_1k_usd = gmv_per_1k*p['comm']*(1-p['ret'])
    return orders_per_1k, gmv_per_1k, comm_per_1k_usd
def solve(target, name, p):
    mv = DIST[name]
    o1k, g1k, c1k = per_view(p)
    comm_per_video_eur = mv/1000*c1k*FX
    margin = comm_per_video_eur - p['cost_var']*FX
    if margin <= 0:
        return dict(status='nicht erreichbar', comm_per_video_eur=round(comm_per_video_eur,2), cost_per_video_eur=round(p['cost_var']*FX,2))
    videos = (target + p['fixed']*FX)/margin
    views = videos*mv
    clicks = views*p['ctr']; orders = clicks*p['cvr']; gmv = orders*p['aov']
    comm_usd = gmv*p['comm']*(1-p['ret'])
    cost = (p['fixed'] + videos*p['cost_var'])*FX
    return dict(status='ok', videos_monat=round(videos), videos_tag=round(videos/30,1), views_monat=round(views), mean_views_video=round(mv),
                klicks=round(clicks), bestellungen=round(orders), gmv_usd=round(gmv), provision_usd=round(comm_usd), provision_eur=round(comm_usd*FX),
                kosten_eur=round(cost), gewinn_eur=round(comm_usd*FX-cost), gewinner_100k=round(videos*({'konservativ':0,'realistisch':0.01,'aggressiv':0.03}[name]),1),
                gewinner_10k_plus=round(videos*({'konservativ':0.02,'realistisch':0.05,'aggressiv':0.13}[name]),1),
                orders_per_1k=round(o1k,2), gmv_per_1k_usd=round(g1k,2), comm_per_1k_usd=round(c1k,2), comm_per_video_eur=round(comm_per_video_eur,2))
out={}
for name,p in SCEN.items():
    out[name]={'annahmen':p,'mean_views':DIST[name],'per_1k':dict(zip(['orders','gmv_usd','comm_usd'],[round(x,2) for x in per_view(p)]))}
    for t in TARGETS: out[name][t]=solve(t,name,p)
print(json.dumps(out,indent=1,ensure_ascii=False))
