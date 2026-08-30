#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
import numpy as np
PASS='PASS_EXP073AH2_Q_REPEATABILITY_FORENSIC_BINDING_V0_2'
P_SHA='6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f'
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}

def one(root:Path,name:str)->Path:
    h=list(root.rglob(name)); assert len(h)==1,(name,len(h)); return h[0]

def cdiff(a:Any,b:Any,p='')->list[str]:
    if type(a) is not type(b): return [p or '<root>']
    if isinstance(a,dict):
        if set(a)!=set(b): return [p or '<root>']
        out=[]
        for k in sorted(a): out+=cdiff(a[k],b[k],f'{p}.{k}' if p else k)
        return out
    if isinstance(a,list):
        if len(a)!=len(b): return [p]
        out=[]
        for i,(x,y) in enumerate(zip(a,b)): out+=cdiff(x,y,f'{p}[{i}]')
        return out
    return [] if a==b else [p]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--a-root',required=True); ap.add_argument('--b-root',required=True); ap.add_argument('--output-json',required=True); a=ap.parse_args()
    ma=json.loads(one(Path(a.a_root),'metadata.json').read_text()); mb=json.loads(one(Path(a.b_root),'metadata.json').read_text())
    with np.load(one(Path(a.a_root),'wm0_te_window.npz')) as z: assert z.files==['wm0_te_window']; A=np.array(z['wm0_te_window'],copy=True)
    with np.load(one(Path(a.b_root),'wm0_te_window.npz')) as z: assert z.files==['wm0_te_window']; B=np.array(z['wm0_te_window'],copy=True)
    A=np.ascontiguousarray(A,dtype='<f8'); B=np.ascontiguousarray(B,dtype='<f8')
    assert A.shape==B.shape==(39,12288); assert np.isfinite(A).all() and np.isfinite(B).all()
    asha=hashlib.sha256(A.tobytes(order='C')).hexdigest(); bsha=hashlib.sha256(B.tobytes(order='C')).hexdigest()
    assert ma['workspace']['te_window_authority']=={'dtype':'<f8','shape':[39,12288],'sha256':asha}
    assert mb['workspace']['te_window_authority']=={'dtype':'<f8','shape':[39,12288],'sha256':bsha}
    assert not np.array_equal(A,B)
    paths=cdiff(ma,mb)
    def allowed(p): return p in {'replica','saved_npz_sha256','workspace.te_window_authority.sha256'} or p.startswith('workspace.absolute_response_norms[')
    bad=[p for p in paths if not allowed(p)]; assert not bad,bad
    neq=A!=B; D=np.abs(A-B); nz=D[neq]; arg=tuple(np.unravel_index(int(np.argmax(D)),D.shape))
    r={
      'experiment':'Exp073AH2','status':PASS,'q_classification_preserved':'SCIENTIFIC_REPEATABILITY_FAIL','production_release':False,
      'forensic_classification':'WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE','q_run':33301058260,'q_head_sha':'730ae4951ab8cd8e1dd2c392e991c3120345678a',
      'replica_a':{'job':99229177604,'artifact':9730452251,'canonical_sha256':asha,'matches_primary_p':asha==P_SHA},
      'replica_b':{'job':99229177540,'artifact':9730346824,'canonical_sha256':bsha,'matches_primary_p':bsha==P_SHA},
      'primary_p_canonical_sha256':P_SHA,'array_equal':False,'mismatched_entries':int(neq.sum()),'total_entries':int(A.size),'mismatch_fraction':float(neq.mean()),
      'max_abs_difference':float(D.max()),'mean_abs_difference':float(D.mean()),'median_nonzero_abs_difference':float(np.median(nz)),
      'argmax_band_ell':[int(arg[0]),int(arg[1])],'a_at_argmax':float(A[arg]),'b_at_argmax':float(B[arg]),
      'affected_bands':int(sum(np.any(neq[i]) for i in range(39))),
      'mismatch_count_by_band':[int(neq[i].sum()) for i in range(39)],'max_abs_difference_by_band':[float(D[i].max()) for i in range(39)],
      'metadata_differing_paths':paths,'unexpected_metadata_differing_paths':bad,'input_or_contract_provenance_drift_detected':False,'root_cause_proven':False,
      'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':GATES,'science_gate_scored':False,'physical_support_evaluated':False,'covariance_read':False,'nuisance_geometry_read':False,'G8_read':False,'scientific_pass_claimed':False}
    p=Path(a.output_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__': main()
