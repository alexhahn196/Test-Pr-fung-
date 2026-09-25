"""
Revisionsläufe nach Gutachter-Prüfung (25.09.2026):
 (1) C5-Vergleich: 1 Account, 150 Videos, alte Kostenannahme 589 EUR -> Mittelwert/Median/Verlustanteil.
 (2) Co-Basisfall rho = -0.3 (virale Videos konvertieren schlechter; Kap. 5 zeigt Rangkorrelation -0,82 ueber Produkte).
 (3) STOP-Regel Kap. 15.3 mit 0,15 Bestellungen je 1.000 Views.
 (4) Top-10-Anteil ohne Seller-Verstaerkung bereits in mc_extra; hier nichts Neues.
"""
import json, numpy as np, importlib.util
ns={}; exec(open('mc_final.py').read().split("P=lambda")[0], ns); simulate=ns['simulate']
out={}
c5={}
for lvl in ('einsteiger','kompetent','sehr_gut'):
    t=simulate(lvl,150,n=40000,per_acct_day=10)['total']; pr=t-589
    c5[lvl]={'commission_mean':int(t.mean()),'commission_median':int(np.median(t)),'profit_mean_oldcost':int(pr.mean()),'profit_median_oldcost':int(np.median(pr)),
             'share_loss':round(float((pr<0).mean()),3),'share_ge_1650':round(float((pr>=1650).mean()),3)}
out['c5_check_150_videos_oldcost_589']=c5
rho={}
for lvl in ('einsteiger','kompetent','sehr_gut'):
    for vol in (100,300,500,1000):
        t=simulate(lvl,vol,rho=-0.3)['total']
        rho[f'{lvl}|{vol}']={f'P{p}':int(np.percentile(t,p)) for p in (10,25,50,75,90)}; rho[f'{lvl}|{vol}']['mean']=int(t.mean())
out['co_base_rho_-0.3']=rho
json.dump(out,open('mc_revision_results.json','w'),indent=1)
print(json.dumps(c5,indent=0)); 
for k,v in rho.items(): print(k,v)
