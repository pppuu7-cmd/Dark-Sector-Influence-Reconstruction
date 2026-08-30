#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

SHAPE=(39,12288)

def canon(x):
    y=np.ascontiguousarray(np.asarray(x,dtype='<f8'))
    return y,hashlib.sha256(y.tobytes(order='C')).hexdigest()

def load(path,key):
    d=np.load(path,allow_pickle=False)
    if key not in d.files: raise AssertionError((path,key,d.files))
    x,sha=canon(d[key])
    if x.shape!=SHAPE or not np.all(np.isfinite(x)): raise AssertionError((x.shape,np.isfinite(x).all()))
    return x,sha

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stage',choices=['compact','final'],required=True); ap.add_argument('--a-npz',required=True); ap.add_argument('--b-npz',required=True); ap.add_argument('--output-json',required=True); ap.add_argument('--output-npz'); a=ap.parse_args()
    key='A' if a.stage=='compact' else 'window'
    xa,sha_a=load(a.a_npz,key); xb,sha_b=load(a.b_npz,key)
    eq=bool(np.array_equal(xa,xb)); diff=np.abs(xa-xb)
    out={'experiment':'Exp073BA','task':'Wm_S1','stage':a.stage,'array_equal':eq,'canonical_sha256_identical':sha_a==sha_b,'sha_a':sha_a,'sha_b':sha_b,'shape':list(SHAPE),'differing_entries':int(np.count_nonzero(xa!=xb)),'differing_bands':int(np.count_nonzero(np.any(xa!=xb,axis=1))),'max_abs_difference':float(np.max(diff)),'mean_abs_difference':float(np.mean(diff,dtype=np.float64)),'article3_scientific_readiness_percent':52,'readiness_increment':0,'scientific_pass_claimed':False,'Exp073AQ_preserved_as_FAIL':True,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    if a.stage=='compact':
        out['status']='PASS_EXP073BA_WM_S1_COMPACT_EXACT_V0_1' if eq and sha_a==sha_b else 'SCIENTIFIC_REPEATABILITY_FAIL_EXP073BA_WM_S1_COMPACT_EXACT_V0_1'
    else:
        norms=np.sum(np.abs(xa),axis=1,dtype=np.float64)
        out['all_band_abs_norms_positive']=bool(np.all(np.isfinite(norms)) and np.all(norms>0))
        out['status']='PASS_EXP073BA_WM_S1_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1' if eq and sha_a==sha_b and out['all_band_abs_norms_positive'] else 'SCIENTIFIC_REPEATABILITY_FAIL_EXP073BA_WM_S1_FINALIZER_EXACT_V0_1'
    Path(a.output_json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    if eq and sha_a==sha_b and a.output_npz:
        if a.stage=='compact': np.savez(a.output_npz,A=xa)
        else: np.savez(a.output_npz,window=xa)
    print(out['status'])
if __name__=='__main__': main()
