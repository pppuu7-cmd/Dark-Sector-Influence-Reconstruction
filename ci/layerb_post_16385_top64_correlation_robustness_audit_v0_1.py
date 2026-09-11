#!/usr/bin/env python3
import argparse,json,math,statistics
from pathlib import Path

PASS='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
AUTH='POST_16385_TOP64_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
OUT='POST_16385_TOP64_CORRELATION_ROBUSTNESS_AUDIT_PASS_PLUS_0_PLUS_0'

def ranks(x):
    order=sorted(range(len(x)),key=lambda i:x[i]); r=[0.0]*len(x); i=0
    while i<len(order):
        j=i+1
        while j<len(order) and x[order[j]]==x[order[i]]: j+=1
        v=0.5*(i+j-1)+1.0
        for k in order[i:j]: r[k]=v
        i=j
    return r

def corr(x,y):
    n=len(x); assert n==len(y) and n>=2
    mx=sum(x)/n; my=sum(y)/n
    dx=[v-mx for v in x]; dy=[v-my for v in y]
    den=math.sqrt(sum(v*v for v in dx)*sum(v*v for v in dy))
    return None if den==0 else sum(a*b for a,b in zip(dx,dy))/den

def spear(x,y): return corr(ranks(x),ranks(y))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--census',required=True); ap.add_argument('--authority',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    c=json.loads(Path(a.census).read_text()); au=json.loads(Path(a.authority).read_text())
    assert c['classification']==PASS and c['atom_count']==64
    assert au['classification']==AUTH and au['atom_count']==64
    xs=[math.log10(float(r['primary_min_cancellation_scale'])) for r in c['atoms']]
    ys=[math.log10(float(r['primary_response_cross_grid_relative_difference'])) for r in c['atoms']]
    rho=spear(xs,ys); assert abs(rho-float(c['spearman_log10_min_cancellation_scale_vs_log10_primary_response_discrepancy']))<1e-15
    loo=[]
    for i in range(64): loo.append(spear(xs[:i]+xs[i+1:],ys[:i]+ys[i+1:]))
    excl1=spear(xs[1:],ys[1:]); excl3=spear(xs[3:],ys[3:]); excl5=spear(xs[5:],ys[5:])
    out={'schema':'LAYERB_POST_16385_TOP64_CORRELATION_ROBUSTNESS_AUDIT_V0_1','classification':OUT,'effect':'+0/+0','atom_count':64,'full_spearman':rho,
         'leave_one_out_spearman':{'min':min(loo),'median':statistics.median(loo),'max':max(loo),'all_negative':all(v<0 for v in loo)},
         'top_rank_exclusions':{'exclude_top1':excl1,'exclude_top3':excl3,'exclude_top5':excl5},
         'class_solver_invoked':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
