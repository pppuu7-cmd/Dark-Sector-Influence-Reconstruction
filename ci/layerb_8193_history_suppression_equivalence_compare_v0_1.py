#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
PASS='LAYERB_8193_HISTORY_SUPPRESSION_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0'
FAIL='LAYERB_8193_HISTORY_SUPPRESSION_EXACT_EQUIVALENCE_FAIL_PLUS_0_PLUS_0'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def arr(xs): return np.asarray([int(x,16) for x in xs],dtype='<u8').view('<f8')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--baseline',required=True); ap.add_argument('--patched',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    b=json.loads(Path(a.baseline).read_text()); p=json.loads(Path(a.patched).read_text()); errors=[]
    for k in ('role','slice_start','slice_end','node_count','node_u64hex','node_payload_sha256','z_probes'):
        if b.get(k)!=p.get(k): errors.append(f'{k} mismatch')
    maxabs=0.0; maxnorm=0.0; equal=0; total=0; perz={}
    for z in b.get('responses_u64hex',{}):
        if z not in p.get('responses_u64hex',{}): errors.append(f'missing z {z}'); continue
        xb=np.asarray([int(x,16) for x in b['responses_u64hex'][z]],dtype='<u8'); xp=np.asarray([int(x,16) for x in p['responses_u64hex'][z]],dtype='<u8')
        if xb.shape!=xp.shape: errors.append(f'shape mismatch z={z}'); continue
        yb=xb.view('<f8'); yp=xp.view('<f8'); diff=np.abs(yb-yp); scale=np.maximum(np.maximum(np.abs(yb),np.abs(yp)),np.finfo(np.float64).tiny); norm=diff/scale
        ma=float(np.max(diff)) if len(diff) else 0.0; mn=float(np.max(norm)) if len(norm) else 0.0; eq=int(np.count_nonzero(xb==xp)); n=len(xb)
        maxabs=max(maxabs,ma); maxnorm=max(maxnorm,mn); equal+=eq; total+=n
        perz[z]={'max_absolute_difference':ma,'max_normalized_difference':mn,'exact_binary64_fraction':eq/n if n else 1.0,'n':n}
    exact=equal/total if total else 0.0
    if maxabs!=0.0: errors.append(f'max absolute difference {maxabs} != 0')
    if maxnorm!=0.0: errors.append(f'max normalized difference {maxnorm} != 0')
    if exact!=1.0: errors.append(f'exact binary64 fraction {exact} != 1')
    out={'schema':'LAYERB_8193_HISTORY_SUPPRESSION_EXACT_EQUIVALENCE_RESULT_V0_1','effect':'+0/+0','classification':PASS if not errors else FAIL,'role':b.get('role'),'baseline_dump_sha256':sha(a.baseline),'patched_dump_sha256':sha(a.patched),'max_absolute_response_difference':maxabs,'max_normalized_response_difference':maxnorm,'exact_binary64_fraction':exact,'per_z':perz,'errors':errors,'scientific_response_vectors_persisted':False,'convergence_metric_computed':False,'scientific_authority':False,'covariance_read':False,'Wm_S3_opened':False}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['classification']); return 0 if not errors else 47
if __name__=='__main__': raise SystemExit(main())
