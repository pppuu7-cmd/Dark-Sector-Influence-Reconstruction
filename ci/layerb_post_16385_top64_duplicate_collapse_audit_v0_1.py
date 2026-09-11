#!/usr/bin/env python3
import argparse,json,math
from collections import Counter
from pathlib import Path
PASS='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
OUT='POST_16385_TOP64_DUPLICATE_COLLAPSE_AUDIT_PASS_PLUS_0_PLUS_0'

def ranks(x):
    o=sorted(range(len(x)),key=lambda i:x[i]); r=[0.0]*len(x); i=0
    while i<len(o):
        j=i+1
        while j<len(o) and x[o[j]]==x[o[i]]: j+=1
        v=0.5*(i+j-1)+1.0
        for k in o[i:j]: r[k]=v
        i=j
    return r

def corr(x,y):
    n=len(x); mx=sum(x)/n; my=sum(y)/n
    dx=[v-mx for v in x]; dy=[v-my for v in y]
    den=math.sqrt(sum(v*v for v in dx)*sum(v*v for v in dy))
    return None if den==0 else sum(a*b for a,b in zip(dx,dy))/den

def spear(rows):
    x=[math.log10(float(r['primary_min_cancellation_scale'])) for r in rows]
    y=[math.log10(float(r['primary_response_cross_grid_relative_difference'])) for r in rows]
    return corr(ranks(x),ranks(y))

def key(r):
    t=r['source_atom']; return (t['block'],t['z_binary64_hex'],t['target_k_binary64_hex'],t['component'])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--census',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    c=json.loads(Path(a.census).read_text()); assert c['classification']==PASS and c['atom_count']==64
    rows=c['atoms']; counts=Counter(key(r) for r in rows)
    uniq={}
    for r in rows: uniq.setdefault(key(r),r)
    u=list(uniq.values())
    duplicate_groups=[{'key':list(k),'multiplicity':v} for k,v in counts.items() if v>1]
    full=spear(rows); collapsed=spear(u)
    assert len(u)==58 and len(duplicate_groups)==3 and all(x['multiplicity']==3 for x in duplicate_groups)
    assert abs(full-float(c['spearman_log10_min_cancellation_scale_vs_log10_primary_response_discrepancy']))<1e-15
    out={'schema':'LAYERB_POST_16385_TOP64_DUPLICATE_COLLAPSE_AUDIT_V0_1','classification':OUT,'effect':'+0/+0','source_atom_count':64,'unique_physical_atom_count':58,'duplicate_group_count':3,'duplicate_groups':duplicate_groups,'full_spearman':full,'collapsed_spearman':collapsed,'collapsed_count_ge_1e_3':sum(float(r['primary_response_cross_grid_relative_difference'])>=1e-3 for r in u),'class_solver_invoked':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
