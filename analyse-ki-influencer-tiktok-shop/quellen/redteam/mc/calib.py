import numpy as np, json, sys
FX=0.92; S_ACC=0.8; S_FIT=0.6; S_AOV=0.35; RET=0.10; CAP=20_000_000; TAIL_MIN=10_000
def gen_account_year(P, n, videos_month, months=12, rng=None):
    q=np.exp(rng.normal(0,S_ACC,n)); f=np.exp(rng.normal(0,S_FIT,n))
    aov=P['aov']*np.exp(rng.normal(0,S_AOV,n)); c=rng.uniform(P['c_lo'],P['c_hi'],n)
    V_all=[];gmv_all=[];orders_all=[];comm_months=[]
    for m in range(months):
        V=np.exp(np.log(P['m']*q)[:,None]+P['s_body']*rng.normal(0,1,(n,videos_month)))
        tail=rng.random((n,videos_month))<np.clip(P['p_tail']*np.sqrt(q),0,0.5)[:,None]
        par=TAIL_MIN*(rng.random((n,videos_month))**(-1.0/P['alpha']))
        V=np.minimum(np.where(tail,np.maximum(V,par),V),CAP)
        gpm=np.exp(np.log(P['g']*f)[:,None]+P['s_gpm']*rng.normal(0,1,(n,videos_month)))
        orders=rng.poisson(V/1000*gpm/aov[:,None])
        gmv=orders*aov[:,None]
        comm=gmv*c[:,None]*(1-RET)
        comm_months.append(comm.sum(1))
        if m==0: V_all=V; gmv_all=gmv; orders_all=orders
    return np.array(comm_months).T, V_all, gmv_all, orders_all

def report(LEVELS, weights, videos_month=150, n=6000, seed=7):
    rng=np.random.default_rng(seed); out={}
    pop=[]; vids=[]; gm=[]; od=[]
    for lvl,w in weights.items():
        k=int(n*w); cm,V,G,O=gen_account_year(LEVELS[lvl],k,videos_month,rng=rng)
        annual_avg_usd=cm.mean(1); pop.append(annual_avg_usd); vids.append(V.ravel()); gm.append(G.ravel()); od.append(O.ravel())
        # per-level stats
        Vr=V.ravel()
        out[lvl]={'p_views_10k':round(float((Vr>=1e4).mean()),4),'p_100k':round(float((Vr>=1e5).mean()),5),'p_1M':round(float((Vr>=1e6).mean()),6),
                  'median_views':int(np.median(Vr)),'peak_over_median_per_acct':round(float(np.median(V.max(1)/np.median(V,1))),1),
                  'p_video_sells':round(float((O.ravel()>0).mean()),3),
                  'annual_avg_comm_usd_pct':{p:int(np.percentile(annual_avg_usd,p)) for p in (10,25,50,75,90,97,99)}}
    pop=np.concatenate(pop); G=np.concatenate(gm); O=np.concatenate(od)
    sell=G[O>0]
    out['population']={'share_ge_1.1k_usd_month':round(float((pop>=1100).mean()),3),'share_ge_11k_usd_month':round(float((pop>=11000).mean()),4),
        'selling_videos_lt100':round(float((sell<100).mean()),3),'selling_100_10k':round(float(((sell>=100)&(sell<1e4)).mean()),3),'selling_gt10k':round(float((sell>=1e4).mean()),4),
        'p_video_sells':round(float((O>0).mean()),3)}
    srt=np.sort(pop)[::-1]; out['population']['top_0.5pct_share_of_commission']=round(float(srt[:max(1,int(len(srt)*0.005))].sum()/srt.sum()),3)
    return out
if __name__=='__main__':
    LEVELS=json.loads(sys.argv[1]); weights=json.loads(sys.argv[2]); vm=int(sys.argv[3]) if len(sys.argv)>3 else 150
    print(json.dumps(report(LEVELS,weights,vm),indent=1))
