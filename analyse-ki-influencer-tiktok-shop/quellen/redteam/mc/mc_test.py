"""
Falsifikationstest-Design: Wie gut trennen 60/90 Shopping-Videos im ersten Monat (Hochlauf) die Archetypen?
Beobachtbar in TikTok Studio / Affiliate-Center: Views je Video, Bestellungen, GMV.
Kennzahlen: n10k = Videos >= 10.000 Views; orders; GPM_real = GMV/Views*1000 (USD); Bestellungen je 1.000 Views.
Regel-Kandidaten werden auf Fehlerraten geprueft (modellbedingt).
"""
import numpy as np, json
S_ACC=0.8; S_FIT=0.6; S_AOV=0.35; TAIL_MIN=10_000; CAP=20_000_000
LEVELS={
 'einsteiger': dict(m=300,  s_body=1.4, p_tail=0.020, alpha=1.10, g=4.0,  s_gpm=1.0, aov=28),
 'kompetent':  dict(m=600,  s_body=1.5, p_tail=0.040, alpha=1.00, g=9.0,  s_gpm=1.0, aov=32),
 'sehr_gut':   dict(m=1000, s_body=1.5, p_tail=0.060, alpha=0.95, g=18.0, s_gpm=0.9, aov=38),
}
def sim(level,nv,ramp,n=40000,seed=3):
    P=LEVELS[level]; rng=np.random.default_rng(seed)
    q=np.exp(rng.normal(0,S_ACC,n)); f=np.exp(rng.normal(0,S_FIT,n)); aov=P['aov']*np.exp(rng.normal(0,S_AOV,n))
    V=np.exp(np.log(P['m']*q*ramp)[:,None]+P['s_body']*rng.normal(0,1,(n,nv)))
    tail=rng.random((n,nv))<np.clip(P['p_tail']*np.sqrt(q)*ramp,0,0.5)[:,None]
    V=np.minimum(np.where(tail,np.maximum(V,TAIL_MIN*(rng.random((n,nv))**(-1/P['alpha']))),V),CAP)
    gpm=np.exp(np.log(P['g']*f)[:,None]+P['s_gpm']*rng.normal(0,1,(n,nv)))
    O=rng.poisson(V/1000*gpm/aov[:,None]); G=O*aov[:,None]
    return dict(n10k=(V>=1e4).sum(1),orders=O.sum(1),views=V.sum(1),gpm=G.sum(1)/V.sum(1)*1000,opk=O.sum(1)/V.sum(1)*1000,medv=np.median(V,1))
out={}
for nv in (60,90):
    for ramp in (0.4,0.7):
        R={l:sim(l,nv,ramp) for l in LEVELS}
        d={}
        for l,r in R.items():
            d[l]={'n10k_P10_P50_P90':[int(np.percentile(r['n10k'],p)) for p in (10,50,90)],'orders_P10_P50_P90':[int(np.percentile(r['orders'],p)) for p in (10,50,90)],
                  'views_P50':int(np.median(r['views'])),'gpm_P10_P50_P90':[round(float(np.percentile(r['gpm'],p)),1) for p in (10,50,90)],
                  'orders_per_1k_P50':round(float(np.median(r['opk'])),2),'median_views_P50':int(np.median(r['medv']))}
        # Regeln: STOP (Hypothese "mind. kompetent" verworfen), wenn ...
        rules={
         'A: orders<10': lambda r: r['orders']<10,
         'B: orders<15': lambda r: r['orders']<15,
         'C: n10k==0 und orders<20': lambda r: (r['n10k']==0)&(r['orders']<20),
         'D: GPM<5 USD (bei >=20k Views)': lambda r: (r['gpm']<5)&(r['views']>=20000),
         'E: orders<10 oder (GPM<5 und Views>=20k)': lambda r: (r['orders']<10)|((r['gpm']<5)&(r['views']>=20000)),
        }
        rr={}
        for name,fn in rules.items():
            rr[name]={l:round(float(fn(R[l]).mean()),3) for l in LEVELS}
        out[f'{nv}|ramp={ramp}']={'stats':d,'P(STOP)':rr}
        print('==',nv,'videos ramp',ramp)
        for l,v in d.items(): print('  ',l,v)
        for k,v in rr.items(): print('   STOP-rate',k,v)
json.dump(out,open('mc_test_results.json','w'),indent=1,ensure_ascii=False)
