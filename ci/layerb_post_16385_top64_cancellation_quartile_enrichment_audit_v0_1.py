#!/usr/bin/env python3
import argparse,json,statistics
from pathlib import Path
PASS='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
OUT='POST_16385_TOP64_CANCELLATION_QUARTILE_ENRICHMENT_AUDIT_PASS_PLUS_0_PLUS_0'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--census',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    c=json.loads(Path(a.census).read_text()); assert c['classification']==PASS and c['atom_count']==64
    rows=c['atoms']; scales=[float(r['primary_min_cancellation_scale']) for r in rows]; disc=[float(r['primary_response_cross_grid_relative_difference']) for r in rows]
    high=[scales[i] for i,d in enumerate(disc) if d>=1e-3]; low=[scales[i] for i,d in enumerate(disc) if d<1e-3]
    order=sorted(range(64),key=lambda i:scales[i]); quart=[]
    for q in range(4):
        idx=order[q*16:(q+1)*16]
        quart.append({'quartile':q+1,'count':16,'scale_min':min(scales[i] for i in idx),'scale_max':max(scales[i] for i in idx),'count_ge_1e_3':sum(disc[i]>=1e-3 for i in idx),'fraction_ge_1e_3':sum(disc[i]>=1e-3 for i in idx)/16.0,'median_discrepancy':statistics.median(disc[i] for i in idx)})
    mh=statistics.median(high); ml=statistics.median(low)
    out={'schema':'LAYERB_POST_16385_TOP64_CANCELLATION_QUARTILE_ENRICHMENT_AUDIT_V0_1','classification':OUT,'effect':'+0/+0','high_discrepancy_count':len(high),'low_discrepancy_count':len(low),'median_cancellation_scale_ge_1e_3':mh,'median_cancellation_scale_lt_1e_3':ml,'high_to_low_median_cancellation_scale_ratio':mh/ml,'cancellation_scale_quartiles_low_to_high':quart,'class_solver_invoked':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False}
    assert len(high)==21 and len(low)==43 and sum(q['count_ge_1e_3'] for q in quart)==21
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
