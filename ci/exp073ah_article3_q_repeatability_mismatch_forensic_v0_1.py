#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np

PASS='PASS_EXP073AH_Q_REPEATABILITY_MISMATCH_FORENSIC_V0_1'
P_SHA='6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f'
A_SHA='6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f'
B_SHA='8ac59fc0c81b2c3ce60f5a5d13424ffba1dda3148f1d35dff4d338124f9b9220'
EXPECTED_MISMATCH=449676
EXPECTED_TOTAL=479232
EXPECTED_MAX=2.0816681711721685e-17
EXPECTED_MEAN=1.2536708729507546e-19
EXPECTED_MEDIAN_NZ=4.0657581468206416e-20
EXPECTED_ARGMAX=[0,33]
EXPECTED_A_MAX=0.028513752074989018
EXPECTED_B_MAX=0.028513752074988997
EXPECTED_COUNTS=[10177,10593,10598,10838,11836,11483,11675,11599,11714,11700,11778,11789,11795,11757,11796,11835,11830,11829,11809,11878,11840,11792,11684,11453,11394,11427,11566,11661,11651,11464,11546,11434,11483,11335,11182,10997,10814,10454,10395]
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}


def canonical(a: np.ndarray) -> tuple[np.ndarray,str]:
    x=np.ascontiguousarray(np.asarray(a,dtype=np.dtype('<f8')))
    return x,hashlib.sha256(x.tobytes(order='C')).hexdigest()


def only(root:Path,name:str)->Path:
    hits=list(root.rglob(name))
    if len(hits)!=1:
        raise AssertionError(f'expected exactly one {name}, got {len(hits)}')
    return hits[0]


def diffs(a:Any,b:Any,path:str='')->list[str]:
    out=[]
    if type(a) is not type(b):
        return [path or '<root>']
    if isinstance(a,dict):
        if set(a)!=set(b): return [path or '<root>']
        for k in sorted(a): out.extend(diffs(a[k],b[k],f'{path}.{k}' if path else k))
    elif isinstance(a,list):
        if len(a)!=len(b): return [path]
        for i,(x,y) in enumerate(zip(a,b)): out.extend(diffs(x,y,f'{path}[{i}]'))
    elif a!=b:
        out.append(path)
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--a-root',required=True)
    ap.add_argument('--b-root',required=True)
    ap.add_argument('--output-json',required=True)
    args=ap.parse_args()
    ar,br=Path(args.a_root),Path(args.b_root)
    ma=json.loads(only(ar,'metadata.json').read_text(encoding='utf-8'))
    mb=json.loads(only(br,'metadata.json').read_text(encoding='utf-8'))
    with np.load(only(ar,'wm0_te_window.npz')) as z:
        assert z.files==['wm0_te_window']
        a=np.array(z['wm0_te_window'],copy=True)
    with np.load(only(br,'wm0_te_window.npz')) as z:
        assert z.files==['wm0_te_window']
        b=np.array(z['wm0_te_window'],copy=True)
    a,asha=canonical(a); b,bsha=canonical(b)
    assert a.shape==b.shape==(39,12288)
    assert np.all(np.isfinite(a)) and np.all(np.isfinite(b))
    assert asha==A_SHA and bsha==B_SHA
    assert asha==P_SHA and bsha!=P_SHA
    assert not np.array_equal(a,b)
    neq=a!=b
    n=int(np.count_nonzero(neq)); total=int(a.size)
    d=np.abs(a-b)
    nz=d[neq]
    maxd=float(np.max(d)); meand=float(np.mean(d)); med=float(np.median(nz))
    arg=list(map(int,np.unravel_index(int(np.argmax(d)),d.shape)))
    counts=[int(np.count_nonzero(neq[i])) for i in range(39)]
    bandmax=[float(np.max(d[i])) for i in range(39)]
    assert n==EXPECTED_MISMATCH and total==EXPECTED_TOTAL
    assert maxd==EXPECTED_MAX and meand==EXPECTED_MEAN and med==EXPECTED_MEDIAN_NZ
    assert arg==EXPECTED_ARGMAX
    assert float(a[tuple(arg)])==EXPECTED_A_MAX and float(b[tuple(arg)])==EXPECTED_B_MAX
    assert counts==EXPECTED_COUNTS and sum(c>0 for c in counts)==39
    md=diffs(ma,mb)
    allowed={f'workspace.absolute_response_norms[{i}]' for i in range(39)}|{'workspace.selected_window_authority.sha256'}
    assert len(md)==40 and set(md)==allowed
    result={
      'experiment':'Exp073AH','status':PASS,
      'classification_preserved':'SCIENTIFIC_REPEATABILITY_FAIL',
      'production_release':False,
      'forensic_classification':'WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE',
      'q_run':33301058260,'q_head_sha':'730ae4951ab8cd8e1dd2c392e991c3120345678a',
      'replica_a':{'job':99229177604,'artifact':9730452251,'canonical_sha256':asha,'matches_primary_p':True},
      'replica_b':{'job':99229177540,'artifact':9730346824,'canonical_sha256':bsha,'matches_primary_p':False},
      'primary_p_canonical_sha256':P_SHA,
      'array_equal':False,'mismatched_entries':n,'total_entries':total,'mismatch_fraction':n/total,
      'max_abs_difference':maxd,'mean_abs_difference':meand,'median_nonzero_abs_difference':med,
      'argmax_band_ell':arg,'a_at_argmax':float(a[tuple(arg)]),'b_at_argmax':float(b[tuple(arg)]),
      'affected_bands':39,'mismatch_count_by_band':counts,'max_abs_difference_by_band':bandmax,
      'metadata_differing_paths':md,'metadata_differing_path_count':len(md),
      'input_provenance_drift_detected':False,
      'root_cause_proven':False,
      'interpretation':'tiny floating-point workspace-output divergence with no detected frozen input/provenance drift; runtime/hardware/thread nondeterminism remains only a possible explanation',
      'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':GATES,
      'science_gate_scored':False,'physical_support_evaluated':False,'covariance_read':False,'nuisance_geometry_read':False,'G8_read':False,'scientific_pass_claimed':False
    }
    p=Path(args.output_json); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': main()
