#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import pymaster as nmt

TOKENS={
 'OFFICIAL_BIN_SUBSTITUTION_FULL_EXACT':'PASS_EXP073EH_OFFICIAL_BIN_SUBSTITUTION_FULL_EXACT_V0_1',
 'OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH':'COMPLETE_EXP073EH_OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH_V0_1'}

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return a,b

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--prereg-blob',required=True); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    nside=16; nl=48; ncls=4; edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32); nb=len(edges)-1
    s0,s1=masks(nside)
    f0=nmt.NmtField(s0,None,spin=2,lmax=47,lmax_mask=47); f1=nmt.NmtField(s1,None,spin=2,lmax=47,lmax_mask=47)
    bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins); fp=out/'w01.fits'; w.write_to(str(fp)); del w
    wr=nmt.NmtWorkspace(); wr.read_from(str(fp))
    m=canon(wr.get_coupling_matrix())

    r=np.zeros((ncls*nb,ncls*nl),dtype=np.float64)
    for j in range(ncls*nl):
        cl=canon(m[:,j].reshape(nl,ncls).T)
        bp=canon(bins.bin_cell(cl))
        r[:,j]=bp.T.reshape(-1)
    r=canon(r)

    q=np.zeros((ncls*nl,ncls*nb),dtype=np.float64)
    col=0
    for ib in range(nb):
      for cls in range(ncls):
        bp=np.zeros((ncls,nb),dtype=np.float64); bp[cls,ib]=1.0
        cl=canon(bins.unbin_cell(bp))
        q[:,col]=cl.T.reshape(-1)
        col += 1
    q=canon(q)

    k=canon(r @ q)
    wrec=canon(np.linalg.inv(k) @ r)
    wpub4=canon(wr.get_bandpower_windows())
    wpub=canon(wpub4.transpose(1,0,3,2).reshape(ncls*nb,ncls*nl))
    exact=sha(wrec)==sha(wpub) and bool(np.array_equal(wrec,wpub))
    cls='OFFICIAL_BIN_SUBSTITUTION_FULL_EXACT' if exact else 'OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH'
    checks={
      'distinct_masks':not np.array_equal(s0,s1),
      'm_shape':list(m.shape)==[ncls*nl,ncls*nl],
      'r_shape':list(r.shape)==[ncls*nb,ncls*nl],
      'q_shape':list(q.shape)==[ncls*nl,ncls*nb],
      'k_shape':list(k.shape)==[ncls*nb,ncls*nb],
      'public_shape':list(wpub4.shape)==[ncls,nb,ncls,nl],
      'matrix_shape':list(wrec.shape)==list(wpub.shape)==[ncls*nb,ncls*nl],
      'sha_equal':sha(wrec)==sha(wpub),
      'array_equal':bool(np.array_equal(wrec,wpub)),
      'finite':bool(np.all(np.isfinite(r)) and np.all(np.isfinite(q)) and np.all(np.isfinite(k)) and np.all(np.isfinite(wrec)) and np.all(np.isfinite(wpub))),
      'no_tolerance_rescue':True}
    result={'experiment':'Exp073EH','classification':cls,'token':TOKENS[cls],'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'pymaster_version':importlib.metadata.version('pymaster'),'source_head':a.source_head,'prereg_blob':a.prereg_blob,'checks':checks,'r_sha256':sha(r),'q_sha256':sha(q),'k_sha256':sha(k),'reconstructed_sha256':sha(wrec),'public_sha256':sha(wpub),'max_abs_difference_diagnostic_only':float(np.max(np.abs(wrec-wpub))),'no_tolerance_rescue':True}
    (out/'terminal_diagnostic_receipt.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
