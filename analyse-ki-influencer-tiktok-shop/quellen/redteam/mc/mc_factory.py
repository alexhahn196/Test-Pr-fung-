"""
Creative-Factory-Modell (Explore/Exploit) vs. flaches Posten, gleiche Videozahl (300/Monat, 1 Account).
Annahme: log(Views) = log(m*q) + c_Konzept + e_Video; Anteil der Konzept-Varianz an der Body-Varianz = share_c
(unbekannt -> Sensitivitaet 0,2/0,4/0,6). Tail-Wahrscheinlichkeit skaliert mit Konzeptqualitaet (mittelwerterhaltend).
Konversion (GPM) haengt vom Produkt ab (Konzept teilt Produkt) + Video-Rauschen.
Flach: 300 Konzepte x 1 Video, 5 EUR/Video.
Factory: 4 Wochen-Zyklen; Woche 1: 25 Konzepte x 3 Varianten; ab Woche 2: je Woche 25 neue Konzepte x 1 Video (Explore)
 + 50 Varianten der bisher besten 5 Konzepte (Exploit, je 10). Auswahl nach BEOBACHTETEN Views der Varianten (verrauscht).
Varianten-Ermuedung: jede weitere Variante desselben Konzepts -8 % Reichweite (Publikum gesaettigt, TikTok drosselt Aehnliches).
Kosten: neues Konzept (echtes Footage, Skript, Schnitt) 8 EUR; Variante (neuer Hook/Voice/Schnitt aus vorhandenem Footage) 1,5 EUR.
"""
import numpy as np, json
FX=0.92; RET=0.10; TAIL_MIN=10_000; CAP=20_000_000
LEVELS={
 'einsteiger': dict(m=300,  s_body=1.4, p_tail=0.020, alpha=1.10, g=4.0,  s_gpm=1.0, c_lo=0.08, c_hi=0.15, aov=28),
 'kompetent':  dict(m=600,  s_body=1.5, p_tail=0.040, alpha=1.00, g=9.0,  s_gpm=1.0, c_lo=0.10, c_hi=0.20, aov=32),
 'sehr_gut':   dict(m=1000, s_body=1.5, p_tail=0.060, alpha=0.95, g=18.0, s_gpm=0.9, c_lo=0.15, c_hi=0.25, aov=38),
}
def videos(rng,P,q,f,aov,c,conc,n):
    """conc: array (n_sims, n_videos) concept effect incl. fatigue (log scale)"""
    s_e=np.sqrt(max(P['s_body']**2-SC2,1e-6))
    V=np.exp(np.log(P['m']*q)[:,None]+conc+s_e*rng.normal(0,1,conc.shape))
    kt=0.8; pt=P['p_tail']*np.sqrt(q)[:,None]*np.exp(kt*conc-0.5*kt**2*SC2)
    tail=rng.random(conc.shape)<np.clip(pt,0,0.6)
    V=np.minimum(np.where(tail,np.maximum(V,TAIL_MIN*(rng.random(conc.shape)**(-1/P['alpha']))),V),CAP)
    gpm=np.exp(np.log(P['g']*f)[:,None]+P['s_gpm']*rng.normal(0,1,conc.shape))
    O=rng.poisson(V/1000*gpm/aov[:,None]); C=O*aov[:,None]*c[:,None]*(1-RET)*FX
    return V,C
def run(level,share_c,n=20000,seed=5,fatigue=0.08):
    global SC2
    P=LEVELS[level]; rng=np.random.default_rng(seed); SC2=share_c*P['s_body']**2; sc=np.sqrt(SC2)
    q=np.exp(rng.normal(0,0.8,n)); f=np.exp(rng.normal(0,0.6,n)); aov=P['aov']*np.exp(rng.normal(0,0.35,n)); c=rng.uniform(P['c_lo'],P['c_hi'],n)
    # flach
    conc=rng.normal(0,sc,(n,300)); V,C=videos(rng,P,q,f,aov,c,conc,300); flat=C.sum(1); flat_cost=300*5
    # factory
    tot=np.zeros(n); cost=0
    k_new=25
    cq=rng.normal(0,sc,(n,k_new)); idx=np.repeat(np.arange(k_new),3)
    fat=np.tile(np.arange(3),k_new)
    conc=cq[:,idx]-fatigue*fat; V,C=videos(rng,P,q,f,aov,c,conc,75); tot+=C.sum(1); cost+=25*8+50*1.5
    # beobachtete Scores je Konzept
    lv=np.log(V).reshape(n,k_new,3).mean(2); pool_q=cq; pool_score=lv; pool_used=np.full((n,k_new),3)
    for wk in range(3):
        # Exploit: Top 5 Konzepte nach beobachtetem Score, je 10 Varianten
        top=np.argsort(-pool_score,axis=1)[:,:5]
        tq=np.take_along_axis(pool_q,top,1); tu=np.take_along_axis(pool_used,top,1)
        conc=np.repeat(tq,10,1)-fatigue*(np.repeat(tu,10,1)+np.tile(np.arange(10),5)[None,:])
        V,C=videos(rng,P,q,f,aov,c,conc,50); tot+=C.sum(1); cost+=50*1.5
        # Update Nutzung/Score der Top-Konzepte (Score = Mittel alt+neu)
        newlv=np.log(V).reshape(n,5,10).mean(2)
        rows=np.arange(n)[:,None]
        pool_used[rows,top]+=10
        pool_score[rows,top]=(pool_score[rows,top]+newlv)/2
        # Explore: 25 neue Konzepte x 1 Video
        nq=rng.normal(0,sc,(n,25)); V,C=videos(rng,P,q,f,aov,c,nq,25); tot+=C.sum(1); cost+=25*8
        pool_q=np.concatenate([pool_q,nq],1); pool_score=np.concatenate([pool_score,np.log(V)],1); pool_used=np.concatenate([pool_used,np.ones((n,25),int)],1)
    pc=lambda x:{f'P{p}':int(np.percentile(x,p)) for p in (10,25,50,75,90)}
    return {'flat_commission':pc(flat),'flat_mean':int(flat.mean()),'flat_cost':flat_cost,'flat_profit_P50':int(np.median(flat-flat_cost-160)),
            'factory_commission':pc(tot),'factory_mean':int(tot.mean()),'factory_cost':int(cost),'factory_profit_P50':int(np.median(tot-cost-160)),
            'ratio_mean':round(float(tot.mean()/flat.mean()),2),'ratio_median':round(float(np.median(tot)/np.median(flat)),2),
            'factory_share_ge':{t:round(float((tot-cost-160>=t).mean()),3) for t in (3000,5000,10000,20000)},
            'flat_share_ge':{t:round(float((flat-flat_cost-160>=t).mean()),3) for t in (3000,5000,10000,20000)}}
out={}
for lvl in LEVELS:
    for sh in (0.2,0.4,0.6):
        r=run(lvl,sh); out[f'{lvl}|share_c={sh}']=r
        print(lvl,sh,'flat',r['flat_commission'],'fac',r['factory_commission'],'ratio mean',r['ratio_mean'],'median',r['ratio_median'],'profitP50 flat/fac',r['flat_profit_P50'],r['factory_profit_P50'],'cost',r['factory_cost'])
for fat in (0.0,0.15):
    r=run('kompetent',0.4,fatigue=fat); out[f'kompetent|share_c=0.4|fatigue={fat}']=r
    print('fatigue',fat,r['factory_commission'],r['ratio_mean'],r['ratio_median'])
json.dump(out,open('mc_factory_results.json','w'),indent=1)
