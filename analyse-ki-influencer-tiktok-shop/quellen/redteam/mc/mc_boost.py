"""
Szenario: Seller-finanzierte Ausspielung (GMV Max / Shop Ads mit Affiliate-Video, isAd=true).
Mechanik (Annahmen, nicht kalibriert): Ein Video mit >= 3 organischen Bestellungen wird mit Wahrscheinlichkeit p_b vom Seller
in Ads genutzt. Zusaetzliche bezahlte Views = organische Views x LogN(Median 30, sigma 1,0), gedeckelt 20 Mio.
Konversion der bezahlten Views = 0,7 x organische GPM des Videos (kaelteres Publikum, aber kaufzielgerichtet).
Provision auf Ads-GMV = Standardsatz x U(0,5; 1,0) (Seller kann eine eigene 'Shop Ads commission rate' setzen).
Beleg fuer den Kanal: 70-100 % isAd bei den Kalodata-Top-10-Creators (Aug 2026), 19/20 isAd bei @healthysmartdeals (KI-3D-Figur);
monatliche Content-Views der Top-Accounts 5-1.500x ueber einer organischen Hochrechnung (redteam_tiktok_hybrid.md H4).
"""
import numpy as np, json
FX=0.92; RET=0.10; TAIL_MIN=10_000; CAP=20_000_000; S_ACC=0.8; S_FIT=0.6; S_AOV=0.35
LEVELS={
 'kompetent':  dict(m=600,  s_body=1.5, p_tail=0.040, alpha=1.00, g=9.0,  s_gpm=1.0, c_lo=0.10, c_hi=0.20, aov=32, p_ban=0.05),
 'sehr_gut':   dict(m=1000, s_body=1.5, p_tail=0.060, alpha=0.95, g=18.0, s_gpm=0.9, c_lo=0.15, c_hi=0.25, aov=38, p_ban=0.04),
}
def run(level,nv,p_b,n=20000,seed=21):
    P=LEVELS[level]; rng=np.random.default_rng(seed)
    q=np.exp(rng.normal(0,S_ACC,n)); f=np.exp(rng.normal(0,S_FIT,n)); aov=P['aov']*np.exp(rng.normal(0,S_AOV,n)); c=rng.uniform(P['c_lo'],P['c_hi'],n)
    V=np.exp(np.log(P['m']*q)[:,None]+P['s_body']*rng.normal(0,1,(n,nv)))
    tail=rng.random((n,nv))<np.clip(P['p_tail']*np.sqrt(q),0,0.5)[:,None]
    V=np.minimum(np.where(tail,np.maximum(V,TAIL_MIN*(rng.random((n,nv))**(-1/P['alpha']))),V),CAP)
    gpm=np.exp(np.log(P['g']*f)[:,None]+P['s_gpm']*rng.normal(0,1,(n,nv)))
    O=rng.poisson(V/1000*gpm/aov[:,None]); C=O*aov[:,None]*c[:,None]*(1-RET)*FX
    boost=(O>=3)&(rng.random((n,nv))<p_b)
    Vb=np.where(boost,np.minimum(V*np.exp(np.log(30)+1.0*rng.normal(0,1,(n,nv))),CAP),0)
    Ob=rng.poisson(Vb/1000*gpm*0.7/aov[:,None]); Cb=Ob*aov[:,None]*(c[:,None]*rng.uniform(0.5,1.0,(n,1)))*(1-RET)*FX
    tot=(C+Cb).sum(1)
    ban=rng.random(n)<P['p_ban']; tot=tot*(1-np.where(ban,rng.uniform(0.3,1.0,n),0.0))
    return tot,(V+Vb).sum(1),boost.sum(1)
out={}
for lvl in LEVELS:
    for nv in (150,300):
        for p_b in (0.0,0.1,0.3):
            t,views,nb=run(lvl,nv,p_b)
            k=f'{lvl}|{nv}|p_b={p_b}'
            out[k]={'commission':{f'P{p}':int(np.percentile(t,p)) for p in (10,25,50,75,90)},'mean':int(t.mean()),'views_P50':int(np.median(views)),'boosted_videos_P50':int(np.median(nb)),
                    'share_ge':{th:round(float((t-nv*5-160>=th).mean()),3) for th in (3000,5000,10000,20000)}}
            print(k,out[k])
json.dump(out,open('mc_boost_results.json','w'),indent=1)
