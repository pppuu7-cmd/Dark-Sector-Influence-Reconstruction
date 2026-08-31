#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

EDGES=np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288],dtype=np.int64)
NB=39
L=12288


def canon(x):
    y=np.ascontiguousarray(np.asarray(x,dtype='<f8'))
    return y,hashlib.sha256(y.tobytes(order='C')).hexdigest()


def band_sums(X):
    out=np.empty((X.shape[0],NB),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(X.shape[0],dtype=np.float64)
        for ell in range(int(lo),int(hi)):
            acc += X[:,ell]
        out[:,ib]=acc
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--window-npz',required=True)
    ap.add_argument('--compact-npz')
    ap.add_argument('--output-json',required=True)
    a=ap.parse_args()

    wraw=np.load(a.window_npz,allow_pickle=False)
    if 'window' not in wraw.files:
        raise AssertionError(('window key missing',wraw.files))
    W,wsha=canon(wraw['window'])
    if W.shape!=(NB,L) or not np.all(np.isfinite(W)):
        raise AssertionError((W.shape,np.isfinite(W).all()))

    WQ=band_sums(W)
    I=np.eye(NB,dtype=np.float64)
    E=WQ-I
    out={
        'classification':'NONCLASSIFYING_NUMERICAL_STRUCTURE_DIAGNOSTIC',
        'authority':False,
        'scientific_pass_claimed':False,
        'article3_scientific_readiness_increment':0,
        'draft_data_readiness_increment':0,
        'window_shape':[NB,L],
        'window_sha256':wsha,
        'wq_identity_max_abs':float(np.max(np.abs(E))),
        'wq_identity_fro':float(np.linalg.norm(E)),
        'wq_diag_max_abs_deviation':float(np.max(np.abs(np.diag(E)))),
        'wq_offdiag_max_abs':float(np.max(np.abs(E-np.diag(np.diag(E))))),
        'window_abs_norm_min':float(np.min(np.sum(np.abs(W),axis=1,dtype=np.float64))),
        'window_abs_norm_max':float(np.max(np.sum(np.abs(W),axis=1,dtype=np.float64))),
        'notes':['Diagnostic only; no PASS/FAIL threshold is defined here.','For the low-memory finalizer K=AQ and W=solve(K,A), exact arithmetic implies WQ=I.','This diagnostic may not reclassify Exp073AQ or alter any frozen Exp073BJ criterion.']
    }

    if a.compact_npz:
        craw=np.load(a.compact_npz,allow_pickle=False)
        if 'A' not in craw.files:
            raise AssertionError(('A key missing',craw.files))
        A,asha=canon(craw['A'])
        if A.shape!=(NB,L) or not np.all(np.isfinite(A)):
            raise AssertionError((A.shape,np.isfinite(A).all()))
        K=band_sums(A)
        s=np.linalg.svd(K,compute_uv=False)
        recon=K@W-A
        out.update({
            'compact_sha256':asha,
            'k_shape':[NB,NB],
            'k_sigma_max':float(s[0]),
            'k_sigma_min':float(s[-1]),
            'k_condition_2':float(s[0]/s[-1]),
            'kw_minus_a_relative_fro':float(np.linalg.norm(recon)/np.linalg.norm(A)),
            'kw_minus_a_max_abs_relative_to_a_max':float(np.max(np.abs(recon))/np.max(np.abs(A)))
        })

    Path(a.output_json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
