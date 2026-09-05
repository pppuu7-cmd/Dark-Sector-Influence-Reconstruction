#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import pymaster as nmt

TOKEN_EXACT='COMPLETE_EXP073EE_WW_CROSS_FORMULA_EXACT_V0_1'
TOKEN_MISMATCH='COMPLETE_EXP073EE_WW_CROSS_FORMULA_MISMATCH_V0_1'

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return a,b

def reconstruct(m,edges,ncls,nl):
    nb=len(edges)-1
    K=np.zeros((ncls*nb,ncls*nb),dtype=np.float64)
    for a in range(ncls):
      for b in range(ncls):
       for ib2 in range(nb):
        w=1.0/float(edges[ib2+1]-edges[ib2])
        for ib3 in range(nb):
         s=0.0
         for l2 in range(edges[ib2],edges[ib2+1]):
          r=ncls*l2+a
          for l3 in range(edges[ib3],edges[ib3+1]):
           c=ncls*l3+b; s += m[r,c]*w
         K[ncls*ib2+a,ncls*ib3+b]=s
    R=np.zeros((ncls*nb,ncls*nl),dtype=np.float64)
    for a in range(ncls):
      for ib1 in range(nb):
       w=1.0/float(edges[ib1+1]-edges[ib1]); rb=ncls*ib1+a
       for l1 in range(edges[ib1],edges[ib1+1]):
        r=ncls*l1+a
        for b in range(ncls):
         for l2 in range(nl): R[rb,ncls*l2+b] += m[r,ncls*l2+b]*w
    X=np.linalg.solve(K,R)
    out=np.empty((ncls,nb,ncls,nl),dtype=np.float64)
    for a in range(ncls):
      for ib in range(nb):
       r=ncls*ib+a
       for b in range(ncls):
        for l in range(nl): out[a,ib,b,l]=X[r,ncls*l+b]
    return canon(out)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--prereg-blob',required=True); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    nside=16; nl=48; ncls=4; edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)
    s0,s1=masks(nside); f0=nmt.NmtField(s0,None,spin=2,lmax=47,lmax_mask=47); f1=nmt.NmtField(s1,None,spin=2,lmax=47,lmax_mask=47); bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins); fp=out/'w01.fits'; w.write_to(str(fp)); del w
    wr=nmt.NmtWorkspace(); wr.read_from(str(fp)); m=canon(wr.get_coupling_matrix()); ref=canon(wr.get_bandpower_windows()); rec=reconstruct(m,edges,ncls,nl)
    ref_ee=canon(ref[0,:,0,:]); rec_ee=canon(rec[0,:,0,:])
    checks={'distinct_masks':not np.array_equal(s0,s1),'full_shape':list(ref.shape)==[4,8,4,48] and list(rec.shape)==[4,8,4,48],'full_sha_equal':sha(ref)==sha(rec),'full_array_equal':bool(np.array_equal(ref,rec)),'selected_sha_equal':sha(ref_ee)==sha(rec_ee),'selected_array_equal':bool(np.array_equal(ref_ee,rec_ee)),'finite':bool(np.all(np.isfinite(ref)) and np.all(np.isfinite(rec))),'no_tolerance_rescue':True}
    exact=all(checks.values()); result={'experiment':'Exp073EE','classification':'FORMULA_EXACT' if exact else 'FORMULA_MISMATCH','token':TOKEN_EXACT if exact else TOKEN_MISMATCH,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'pymaster_version':importlib.metadata.version('pymaster'),'source_head':a.source_head,'prereg_blob':a.prereg_blob,'checks':checks,'reference_sha256':sha(ref),'reconstructed_sha256':sha(rec),'reference_selected_ee_sha256':sha(ref_ee),'reconstructed_selected_ee_sha256':sha(rec_ee),'full_max_abs_difference_diagnostic_only':float(np.max(np.abs(ref-rec))),'no_tolerance_rescue':True}
    (out/'terminal_diagnostic_receipt.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token']); print(json.dumps(result,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()
