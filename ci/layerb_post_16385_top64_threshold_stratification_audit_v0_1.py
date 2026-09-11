#!/usr/bin/env python3
import argparse,json,statistics
from collections import Counter,defaultdict
from pathlib import Path

PASS='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
AUTH='POST_16385_TOP64_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
OUT='POST_16385_TOP64_THRESHOLD_STRATIFICATION_AUDIT_PASS_PLUS_0_PLUS_0'

def q(sorted_x,p):
    n=len(sorted_x); assert n
    if n==1:return float(sorted_x[0])
    x=(n-1)*p; lo=int(x); hi=min(lo+1,n-1); f=x-lo
    return float(sorted_x[lo]*(1-f)+sorted_x[hi]*f)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--census',required=True); ap.add_argument('--authority',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    c=json.loads(Path(a.census).read_text()); au=json.loads(Path(a.authority).read_text())
    assert c['classification']==PASS and c['atom_count']==64 and len(c['atoms'])==64
    assert au['classification']==AUTH and au['atom_count']==64 and au['max_primary_reproduction_relative_error']==0.0
    vals=[float(r['primary_response_cross_grid_relative_difference']) for r in c['atoms']]
    sv=sorted(vals)
    blocks=defaultdict(list); comps=defaultdict(list)
    for r in c['atoms']:
        t=r['source_atom']; v=float(r['primary_response_cross_grid_relative_difference'])
        blocks[str(t['block'])].append(v); comps[str(t['component'])].append(v)
    def pack(d):
        return {k:{'count':len(v),'count_ge_1e_3':sum(x>=1e-3 for x in v),'median':statistics.median(v),'max':max(v)} for k,v in sorted(d.items())}
    out={'schema':'LAYERB_POST_16385_TOP64_THRESHOLD_STRATIFICATION_AUDIT_V0_1','classification':OUT,'effect':'+0/+0','atom_count':64,
         'threshold_counts':{'ge_1e_3':sum(x>=1e-3 for x in vals),'ge_2e_3':sum(x>=2e-3 for x in vals),'ge_5e_3':sum(x>=5e-3 for x in vals),'ge_1e_2':sum(x>=1e-2 for x in vals)},
         'quantiles':{'q00':q(sv,0),'q25':q(sv,.25),'q50':q(sv,.5),'q75':q(sv,.75),'q90':q(sv,.9),'q95':q(sv,.95),'q100':q(sv,1)},
         'by_block':pack(blocks),'by_component':pack(comps),'class_solver_invoked':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False}
    assert out['threshold_counts']['ge_1e_3']==21
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
