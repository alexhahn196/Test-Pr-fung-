"""
Ergaenzungen zum kalibrierten Monte-Carlo-Modell (mc_final.py), Red-Team-Audit 25.09.2026.
Gleiche Archetypen/Parameter wie mc_final.py. Neu:
 (a) Portfolio mit korreliertem Verbund-Risiko (eine Person, mehrere Accounts: Verstoss/Ueberpruefung trifft
     verknuepfte Accounts gemeinsam) und Produkt-/Zielgruppen-Saettigung (Accounts derselben Person teilen Nische).
 (b) Winner-Definitionen, Trefferquoten, benoetigter Winner-Wert fuer Gewinnziele.
 (c) Creative-Oekonomie 2/5/10/20 EUR x 100/300/500/1000 Videos.
 (d) Anteil der Top-10-Videos an der Monatsprovision.
Alle Wahrscheinlichkeiten sind MODELL-bedingt (Annahmen offengelegt), keine empirischen Erfolgsquoten.
"""
import numpy as np, json, math
FX=0.92; S_ACC=0.8; S_FIT=0.6; S_AOV=0.35; RET=0.10; CAP=20_000_000; TAIL_MIN=10_000
LEVELS={
 'einsteiger': dict(m=300,  s_body=1.4, p_tail=0.020, alpha=1.10, g=4.0,  s_gpm=1.0, c_lo=0.08, c_hi=0.15, aov=28, p_ban=0.06),
 'kompetent':  dict(m=600,  s_body=1.5, p_tail=0.040, alpha=1.00, g=9.0,  s_gpm=1.0, c_lo=0.10, c_hi=0.20, aov=32, p_ban=0.05),
 'sehr_gut':   dict(m=1000, s_body=1.5, p_tail=0.060, alpha=0.95, g=18.0, s_gpm=0.9, c_lo=0.15, c_hi=0.25, aov=38, p_ban=0.04),
}
def simulate(level, n_acc, per_acct_day, n=20000, rho=0.0, ramp=1.0, seed=11, keep=False,
             sat_exp=0.0, p_assoc_step=0.0, assoc_loss=(0.5,1.0)):
    P=LEVELS[level]; rng=np.random.default_rng(seed)
    per_acc=int(round(per_acct_day*30)); vpa=per_acct_day
    dim=min(1.0,(5.0/vpa)**0.2) if vpa>5 else 1.0
    sat=n_acc**(-sat_exp)            # Saettigung: gleiche Nische/Zielgruppe -> Reichweite je Account sinkt
    tot=np.zeros(n); allV=[]; allC=[]; allO=[]
    op_q=rng.normal(0,S_ACC*0.6,n); op_f=rng.normal(0,S_FIT*0.6,n)
    # korreliertes Verbund-Ereignis: trifft ALLE Accounts der Person im Monat
    p_assoc=min(0.5,p_assoc_step*(n_acc-1))
    assoc=rng.random(n)<p_assoc; assoc_cut=np.where(assoc,rng.uniform(*assoc_loss,n),0.0)
    for a in range(n_acc):
        q=np.exp(op_q+rng.normal(0,S_ACC*0.8,n))*sat; f=np.exp(op_f+rng.normal(0,S_FIT*0.8,n))
        aov=P['aov']*np.exp(rng.normal(0,S_AOV,n)); c=rng.uniform(P['c_lo'],P['c_hi'],n)
        z=rng.normal(0,1,(n,per_acc))
        V=np.exp(np.log(P['m']*q*dim*ramp)[:,None]+P['s_body']*z)
        tail=rng.random((n,per_acc))<np.clip(P['p_tail']*np.sqrt(q)*ramp,0,0.5)[:,None]
        V=np.minimum(np.where(tail,np.maximum(V,TAIL_MIN*(rng.random((n,per_acc))**(-1/P['alpha']))),V),CAP)
        zv=np.clip((np.log(V)-np.log(P['m']))/2.0,-3,3)
        gpm=np.exp(np.log(P['g']*f)[:,None]+rho*zv+P['s_gpm']*rng.normal(0,1,(n,per_acc)))
        O=rng.poisson(V/1000*gpm/aov[:,None]); C=O*aov[:,None]*c[:,None]*(1-RET)*FX
        ban=rng.random(n)<P['p_ban']; C=C*(1-np.where(ban,rng.uniform(0.3,1.0,n),0.0))[:,None]
        C=C*(1-assoc_cut)[:,None]
        tot+=C.sum(1)
        if keep: allV.append(V); allC.append(C); allO.append(O)
    res=dict(total=tot,p_assoc=p_assoc)
    if keep: res.update(V=np.concatenate(allV,1),C=np.concatenate(allC,1),O=np.concatenate(allO,1))
    return res
PC=lambda x,ps=(10,25,50,75,90): {f'P{p}':int(round(float(np.percentile(x,p)))) for p in ps}
out={}
# (a) Portfolio v2: 1/3/5/10 Accounts a 5 Videos/Tag; Varianten: naiv (unabhaengig) vs. realistisch (Saettigung + Verbund-Risiko)
port={}
COST=dict(creative=5, tools_fix=100, tools_acc=60)
STAFF={1:(0,20),3:(600,40),5:(1500,55),10:(3500,80)}   # (VA/Schnitt-Kosten EUR, Stunden/Woche Operator)
for lvl in LEVELS:
    for k in (1,3,5,10):
        vol=150*k
        for mode,kw in (('naiv',{}),('realistisch',dict(sat_exp=0.15,p_assoc_step=0.03))):
            r=simulate(lvl,k,5,**kw); t=r['total']
            va,h=STAFF[k]; cost=COST['tools_fix']+COST['tools_acc']*k+COST['creative']*vol+va
            pr=t-cost
            port[f'{lvl}|{k}|{mode}']={'videos':vol,'commission':PC(t),'profit':PC(pr),'mean_profit':int(pr.mean()),
               'share_profit_ge':{th:round(float((pr>=th).mean()),3) for th in (3000,5000,10000,20000)},
               'share_loss':round(float((pr<0).mean()),3),'p_assoc_month':round(r['p_assoc'],3),'cost_eur':int(cost),'hours_week':h}
out['portfolio_v2']=port
# (b) Winner-Definitionen (300 Videos/Monat, 1 Account a 10/Tag) + Top-10-Anteil
win={}; top10={}
DEFS={'views>=10k':lambda V,O,C:V>=1e4,'views>=100k':lambda V,O,C:V>=1e5,'>=1 Verkauf':lambda V,O,C:O>=1,
      '>=10 Verkaeufe':lambda V,O,C:O>=10,'Provision>=100EUR':lambda V,O,C:C>=100,'Provision>=500EUR':lambda V,O,C:C>=500}
for lvl in LEVELS:
    r=simulate(lvl,1,10,n=6000,keep=True); V,O,C=r['V'],r['O'],r['C']; tot=C.sum(1)
    d={}
    for name,fn in DEFS.items():
        m=fn(V,O,C); rate=float(m.mean())
        val=float(C[m].mean()) if m.any() else 0.0
        share=float(np.median(np.where(tot>0,(C*m).sum(1)/np.maximum(tot,1e-9),np.nan)[tot>0]))
        d[name]={'rate_per_video':round(rate,4),'one_in':(round(1/rate) if rate>0 else None),'winners_per_300':round(rate*300,1),
                 'mean_commission_per_winner_eur':round(val,1),'median_share_of_month_commission':round(share,2)}
    win[lvl]=d
    Cs=np.sort(C,1)[:,::-1]; ok=tot>0
    top10[lvl]={'300_videos_top10_share_median':round(float(np.median(Cs[ok,:10].sum(1)/tot[ok])),2),
                '300_videos_top3_share_median':round(float(np.median(Cs[ok,:3].sum(1)/tot[ok])),2)}
    r2=simulate(lvl,1,5,n=6000,keep=True); C2=r2['C']; t2=C2.sum(1); Cs2=np.sort(C2,1)[:,::-1]; ok2=t2>0
    top10[lvl]['150_videos_top10_share_median']=round(float(np.median(Cs2[ok2,:10].sum(1)/t2[ok2])),2)
    top10[lvl]['150_videos_top5pct_share_median']=round(float(np.median(Cs2[ok2,:8].sum(1)/t2[ok2])),2)
out['winners']=win; out['top10_share']=top10
# benoetigter Durchschnittswert je Winner fuer Gewinnziele bei 300 Varianten/Monat, 5 EUR/Creative, 160 EUR Tools
need={}
for hit,N in (('1:5',60),('1:10',30),('1:20',15),('1:50',6)):
    need[hit]={'winners':N, **{f'profit_{t}':int(math.ceil((t+300*5+160)/N)) for t in (0,3000,5000,10000,20000)}}
out['winner_value_needed']=need
# Wie haeufig erreicht ein Video im Modell diese Werte? (je Archetyp: Anteil Videos >= benoetigter Wert)
reach={}
for lvl in LEVELS:
    r=simulate(lvl,1,10,n=6000,keep=True); C=r['C'].ravel()
    reach[lvl]={hit:{t:(lambda v:(round(1/v) if v>0 else None))(float((C>=need[hit][f'profit_{t}']).mean())) for t in (3000,5000,10000,20000)} for hit in need}
out['model_one_in_N_videos_reaching_needed_value']=reach
# (c) Creative-Oekonomie
ce={}
for lvl in LEVELS:
    for vol in (100,300,500,1000):
        k=max(1,math.ceil(vol/300)); r=simulate(lvl,k,vol/k/30,n=20000); t=r['total']
        for cost in (2,5,10,20):
            fixed=100+50*k; pr=t-vol*cost-fixed
            ce[f'{lvl}|{vol}|{cost}']={'revenue_median':int(np.median(t)),'revenue_mean':int(t.mean()),'profit_median':int(np.median(pr)),
               'profit_mean':int(pr.mean()),'ev_per_video_eur':round(float(t.mean()/vol-cost-fixed/vol),2),'share_months_loss':round(float((pr<0).mean()),2)}
out['creative_economics']=ce
be={}
for lvl,p in LEVELS.items():
    cps=p['aov']*((p['c_lo']+p['c_hi'])/2)*(1-RET)*FX
    for cost in (2,5,10,20):
        s=cost/cps; be[f'{lvl}|{cost}']={'commission_per_sale':round(cps,2),'sales_per_video':round(s,2),'views_per_video_at_median_gpm':int(s/(p['g']/p['aov'])*1000)}
out['break_even']=be
json.dump(out,open('mc_extra_results.json','w'),indent=1,ensure_ascii=False)
for k,v in port.items(): print(k,v['commission'],'profit',v['profit'],'share',v['share_profit_ge'],'loss',v['share_loss'],'passoc',v['p_assoc_month'])
print(json.dumps(win,indent=0,ensure_ascii=False)); print(top10); print(need); print(reach)
for k,v in ce.items(): print(k,v)
print(be)
