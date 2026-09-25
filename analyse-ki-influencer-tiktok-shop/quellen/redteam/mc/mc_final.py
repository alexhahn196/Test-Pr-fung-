"""
Monte-Carlo-Modell auf Video-Ebene (Red-Team-Audit, 25.09.2026) - kalibrierte Fassung.
Kalibrierung (calib.py): Mischung 70/25/5 der drei Archetypen reproduziert die Biverse-Verteilung verkaufender KI-Videos
(Modell 72 % < 100 USD / 28 % 100-10k / 0,22 % > 10k; Biverse 78 / 22 / 0,15 -> Modell leicht optimistisch);
Mischung 55/35/10 ("ernsthafte Operatoren", 150 Videos/Monat) ergibt 32 % >= 1,1k USD Provision/Monat und 2,9 % >= 11k USD/Monat
(Anker: TikTok 16.000 Creator >= 100k USD GMV/Jahr, 1.785 >= 1 Mio. USD/Jahr bei ~945k US-Affiliates mit Umsatz; Nenner fuer
"ernsthafte" Operatoren unbekannt -> Zielband 20-35 % bzw. 2-5 %).
Archetypen sind ERGEBNIS-Klassen, keine Skill-Garantie: Einsteiger ~ typischer KI-Video-Operator; Kompetent ~ oberes Drittel;
Sehr gut ~ oberste ~10 % der ernsthaften Operatoren.
"""
import numpy as np, json
FX=0.92; S_ACC=0.8; S_FIT=0.6; S_AOV=0.35; RET=0.10; CAP=20_000_000; TAIL_MIN=10_000
LEVELS={
 'einsteiger': dict(m=300,  s_body=1.4, p_tail=0.020, alpha=1.10, g=4.0,  s_gpm=1.0, c_lo=0.08, c_hi=0.15, aov=28, p_ban=0.06),
 'kompetent':  dict(m=600,  s_body=1.5, p_tail=0.040, alpha=1.00, g=9.0,  s_gpm=1.0, c_lo=0.10, c_hi=0.20, aov=32, p_ban=0.05),
 'sehr_gut':   dict(m=1000, s_body=1.5, p_tail=0.060, alpha=0.95, g=18.0, s_gpm=0.9, c_lo=0.15, c_hi=0.25, aov=38, p_ban=0.04),
}
def simulate(level, videos, n=20000, per_acct_day=10, rho=0.0, ramp=1.0, seed=11, keep=False):
    P=LEVELS[level]; rng=np.random.default_rng(seed)
    n_acc=max(1,int(np.ceil(videos/(30*per_acct_day)))); per_acc=int(round(videos/n_acc)); vpa=per_acc/30
    dim=min(1.0,(5.0/vpa)**0.2) if vpa>5 else 1.0
    tot=np.zeros(n); allV=[]; allC=[]; allO=[]
    # Operator-Effekt (gleiche Person betreibt alle Accounts): gemeinsamer Anteil an Qualitaet und Produkt-Fit
    op_q=rng.normal(0,S_ACC*0.6,n); op_f=rng.normal(0,S_FIT*0.6,n)
    for a in range(n_acc):
        q=np.exp(op_q+rng.normal(0,S_ACC*0.8,n)); f=np.exp(op_f+rng.normal(0,S_FIT*0.8,n))
        aov=P['aov']*np.exp(rng.normal(0,S_AOV,n)); c=rng.uniform(P['c_lo'],P['c_hi'],n)
        z=rng.normal(0,1,(n,per_acc))
        V=np.exp(np.log(P['m']*q*dim*ramp)[:,None]+P['s_body']*z)
        tail=rng.random((n,per_acc))<np.clip(P['p_tail']*np.sqrt(q)*ramp,0,0.5)[:,None]
        V=np.minimum(np.where(tail,np.maximum(V,TAIL_MIN*(rng.random((n,per_acc))**(-1/P['alpha']))),V),CAP)
        zv=np.clip((np.log(V)-np.log(P['m']))/2.0,-3,3)
        gpm=np.exp(np.log(P['g']*f)[:,None]+rho*zv+P['s_gpm']*rng.normal(0,1,(n,per_acc)))
        O=rng.poisson(V/1000*gpm/aov[:,None]); C=O*aov[:,None]*c[:,None]*(1-RET)*FX
        ban=rng.random(n)<P['p_ban']; C=C*(1-np.where(ban,rng.uniform(0.3,1.0,n),0.0))[:,None]
        tot+=C.sum(1)
        if keep: allV.append(V); allC.append(C); allO.append(O)
    res=dict(total=tot,n_acc=n_acc,vpa=vpa)
    if keep: res.update(V=np.concatenate(allV,1),C=np.concatenate(allC,1),O=np.concatenate(allO,1))
    return res
P=lambda x,ps=(10,25,50,75,90): {f'P{p}':int(round(float(np.percentile(x,p)))) for p in ps}
out={}
# 1) Volumen x Archetyp: Provisions-Perzentile, Gewinn bei 2/5/10/20 EUR je Creative
tbl={}
for lvl in LEVELS:
    for vol in (100,300,500,1000):
        r=simulate(lvl,vol,keep=True); t=r['total']; C=r['C']
        row={'accounts':r['n_acc'],'videos_per_account_day':round(r['vpa'],1),'commission':P(t),'mean':int(t.mean())}
        fixed=100+50*r['n_acc']
        for cost in (2,5,10,20):
            pr=t-vol*cost-fixed; row[f'profit_{cost}']=P(pr); row[f'share_profit_{cost}']={th:round(float((pr>=th).mean()),3) for th in (3000,5000,10000,20000)}
        # Konzentration: Anteil der Top-1/5/10/20 % Videos an Provision (Median ueber Simulationen mit Provision>0)
        Cs=np.sort(C,axis=1)[:,::-1]; s=Cs.sum(1); ok=s>0; nv=C.shape[1]
        row['concentration']={f'top{p}pct':round(float(np.median(Cs[ok,:max(1,int(np.ceil(nv*p/100)))].sum(1)/s[ok])),2) for p in (1,5,10,20)}
        row['videos_with_zero_sales']=round(float((r['O']==0).mean()),3)
        row['commission_per_video_mean_eur']=round(float(t.mean()/vol),2)
        tbl[f'{lvl}|{vol}']=row
out['volume_table']=tbl
# 2) Treffer-Definitionen und Trefferquoten (je Video) + 300 Varianten/Monat
hits={}
for lvl in LEVELS:
    r=simulate(lvl,300,n=6000,keep=True); V=r['V'].ravel(); O=r['O'].ravel(); C=r['C'].ravel()
    med=np.median(r['V'],axis=1)[:,None]
    d={'views>=10k':float((V>=1e4).mean()),'views>=100k':float((V>=1e5).mean()),'views>=1M':float((V>=1e6).mean()),'>=10x Account-Median':float((r['V']>=10*med).mean()),
       '>=1 sale':float((O>=1).mean()),'>=10 sales':float((O>=10).mean()),'>=100 sales':float((O>=100).mean()),'commission>=100EUR':float((C>=100).mean()),'commission>=500EUR':float((C>=500).mean()),'commission>=2000EUR':float((C>=2000).mean())}
    hits[lvl]={k:{'per_video':round(v,5),'expected_per_300':round(v*300,1),'p_at_least_one_in_300':round(1-(1-v)**300,3)} for k,v in d.items()}
    # Wert eines "Gewinners" (commission>=500) : Median-Provision der Gewinner
    w=C[C>=500]; hits[lvl]['value_of_500EUR_winner']={'median':int(np.median(w)) if len(w) else 0,'P90':int(np.percentile(w,90)) if len(w) else 0}
out['hits']=hits
# 3) Nutzer-Hypothese: 1 Video mit 2 Mio. Views -> 1.200 Kaeufe -> 42.000 EUR GMV -> 8.400 EUR Provision
hyp={}
for lvl in LEVELS:
    r=simulate(lvl,300,n=6000,keep=True); V=r['V'].ravel(); C=r['C'].ravel()
    hyp[lvl]={'p_video_views>=2M':float((V>=2e6).mean()),'p_video_commission>=8400EUR':float((C>=8400).mean()),
              'p_month_has_>=1_video_commission>=8400_at_300':round(float((r['C']>=8400).any(1).mean()),3),
              'median_commission_of_2M+_videos_eur':int(np.median(C[V>=2e6])) if (V>=2e6).any() else None}
out['outlier_hypothesis']=hyp
# 4) Portfolio: 1/3/5/10 Accounts a 5 Videos/Tag (150/Monat), gleiche Person/Operator-Effekt
port={}
for lvl in LEVELS:
    for k in (1,3,5,10):
        vol=150*k; r=simulate(lvl,vol,per_acct_day=5)
        t=r['total']; tools=100+60*k; prod=vol*5; va=0 if k<=1 else (600 if k<=3 else (1500 if k<=5 else 3500))
        pr=t-tools-prod-va
        port[f'{lvl}|{k}']={'videos':vol,'commission':P(t),'profit_after_tools_prod5_va':P(pr),'share_profit>=':{th:round(float((pr>=th).mean()),3) for th in (3000,5000,10000,20000)},
                            'hours_per_week_est':{1:20,3:40,5:55,10:80}[k],'va_cost_eur':va}
out['portfolio']=port
# 5) Sensitivitaet: Korrelation Views<->Conversion (rho) und Hochlaufphase Monat 1-3
sens={}
for rho in (-0.3,0.0,0.3):
    t=simulate('kompetent',300,rho=rho)['total']; sens[f'kompetent|300|rho={rho}']=P(t)
for m,ramp in (('Monat1',0.4),('Monat2',0.7),('Monat3',1.0)):
    for lvl in LEVELS:
        t=simulate(lvl,300,ramp=ramp)['total']; sens[f'{lvl}|300|{m}']=P(t)
out['sensitivity']=sens
# 6) Break-even je Creative: benoetigte Views und Verkaeufe bei Median-GPM des Archetyps
be={}
for lvl,p in LEVELS.items():
    comm_per_sale=p['aov']*((p['c_lo']+p['c_hi'])/2)*(1-RET)*FX
    for cost in (2,5,10,20):
        sales=cost/comm_per_sale; views=sales/(p['g']/p['aov'])*1000
        be[f'{lvl}|{cost}EUR']={'commission_per_sale_eur':round(comm_per_sale,2),'break_even_sales':round(sales,2),'break_even_views_at_median_gpm':int(views)}
out['break_even']=be
json.dump(out,open('mc_final_results.json','w'),indent=1,ensure_ascii=False)
for k,v in tbl.items(): print(k,v['accounts'],v['commission'],'mean',v['mean'],'| share profit>=3/5/10/20k @5EUR',v['share_profit_5'],'| conc',v['concentration'],'| zero-sale videos',v['videos_with_zero_sales'])
print(json.dumps(hits,indent=0)[:3000]); print(json.dumps(hyp,indent=1)); print(json.dumps(sens,indent=0)); print(json.dumps(be,indent=0))
for k,v in port.items(): print(k,v['commission'],v['profit_after_tools_prod5_va'],v['share_profit>='])
