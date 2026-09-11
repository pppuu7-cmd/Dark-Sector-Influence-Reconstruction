#!/usr/bin/env python3
import argparse,json,math,statistics
from pathlib import Path

PASS='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
AUTH='POST_16385_TOP64_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
OUT='POST_16385_TOP64_AMPLIFICATION_POPULATION_AUDIT_PASS_PLUS_0_PLUS_0'

def q(x,p):
    x=sorted(x); pos=(len(x)-1)*p; lo=int(pos); hi=min(lo+1,len(x)-1); f=pos-lo
    return x[lo]*(1-f)+x[hi]*f

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--census',required=True); ap.add_argument('--authority',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    c=json.loads(Path(a.census).read_text()); au=json.loads(Path(a.authority).read_text())
    assert c['classification']==PASS and c['atom_count']==64
    assert au['classification']==AUTH and au['atom_count']==64
    ratios=[]; rows=[]
    for r in c['atoms']:
        raw=max(float(v) for v in r['cross_grid_raw_role_relative_differences'].values())
        primary=float(r['primary_response_cross_grid_relative_difference'])
        ratio=primary/raw if raw>0 else math.inf
        ratios.append(ratio)
        rows.append({'rank':r['rank'],'block':r['source_atom']['block'],'component':r['source_atom']['component'],'primary_discrepancy':primary,'max_raw_role_relative_difference':raw,'amplification_factor':ratio,'primary_min_cancellation_scale':float(r['primary_min_cancellation_scale'])})
    assert all(math.isfinite(x) and x>0 for x in ratios)
    out={'schema':'LAYERB_POST_16385_TOP64_AMPLIFICATION_POPULATION_AUDIT_V0_1','classification':OUT,'effect':'+0/+0','atom_count':64,
         'amplification_distribution':{'min':min(ratios),'q25':q(ratios,.25),'median':statistics.median(ratios),'q75':q(ratios,.75),'q90':q(ratios,.9),'max':max(ratios)},
         'threshold_counts':{'ge_1e4':sum(x>=1e4 for x in ratios),'ge_1e5':sum(x>=1e5 for x in ratios),'ge_1e6':sum(x>=1e6 for x in ratios),'ge_1e7':sum(x>=1e7 for x in ratios),'ge_1e8':sum(x>=1e8 for x in ratios)},
         'top10_by_amplification':sorted(rows,key=lambda r:r['amplification_factor'],reverse=True)[:10],
         'class_solver_invoked':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
