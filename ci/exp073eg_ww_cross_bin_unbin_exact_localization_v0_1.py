#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import pymaster as nmt

TOKENS={
 'BIN_UNBIN_EXACT':'COMPLETE_EXP073EG_BIN_UNBIN_EXACT_V0_1',
 'BIN_ONLY_MISMATCH':'COMPLETE_EXP073EG_BIN_ONLY_MISMATCH_V0_1',
 'UNBIN_ONLY_MISMATCH':'COMPLETE_EXP073EG_UNBIN_ONLY_MISMATCH_V0_1',
 'BIN_AND_UNBIN_MISMATCH':'COMPLETE_EXP073EG_BIN_AND_UNBIN_MISMATCH_V0_1'}

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return a,b

def p_manual(cl,edges):
    ncls,nl=cl.shape; nb=len(edges)-1
    out=np.zeros((ncls,nb),dtype=np.float64)
    for a in range(ncls):
      for ib in range(nb):
        w=1.0/float(edges[ib+1]-edges[ib]); s=0.0
        for ell in range(edges[ib],edges[ib+1]): s += cl[a,ell]*w
        out[a,ib]=s
    return canon(out)

def q_manual(bp,edges,nl):
    ncls,nb=bp.shape; out=np.zeros((ncls,nl),dtype=np.float64)
    for a in range(ncls):
      for ib in range(nb):
        for ell in range(edges[ib],edges[ib+1]): out[a,ell]=bp[a,ib]
    return canon(out)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--prereg-blob',required=True); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    nside=16; nl=48; ncls=4; edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32); nb=len(edges)-1
    s0,s1=masks(nside); f0=nmt.NmtField(s0,None,spin=2,lmax=47,lmax_mask=47); f1=nmt.NmtField(s1,None,spin=2,lmax=47,lmax_mask=47); bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins); fp=out/'w01.fits'; w.write_to(str(fp)); del w
    wr=nmt.NmtWorkspace(); wr.read_from(str(fp)); m=canon(wr.get_coupling_matrix())
    pm=[]; pp=[]
    for j in range(ncls*nl):
        cl=canon(m[:,j].reshape(nl,ncls).T)
        pm.append(p_manual(cl,edges)); pp.append(canon(bins.bin_cell(cl)))
    pm=canon(np.stack(pm)); pp=canon(np.stack(pp))
    qm=[]; qp=[]
    for cls in range(ncls):
      for ib in range(nb):
        bp=np.zeros((ncls,nb),dtype=np.float64); bp[cls,ib]=1.0
        qm.append(q_manual(bp,edges,nl)); qp.append(canon(bins.unbin_cell(bp)))
    qm=canon(np.stack(qm)); qp=canon(np.stack(qp))
    p_exact=sha(pm)==sha(pp) and bool(np.array_equal(pm,pp)); q_exact=sha(qm)==sha(qp) and bool(np.array_equal(qm,qp))
    if p_exact and q_exact: cls='BIN_UNBIN_EXACT'
    elif (not p_exact) and q_exact: cls='BIN_ONLY_MISMATCH'
    elif p_exact and (not q_exact): cls='UNBIN_ONLY_MISMATCH'
    else: cls='BIN_AND_UNBIN_MISMATCH'
    checks={'distinct_masks':not np.array_equal(s0,s1),'p_shape':list(pm.shape)==list(pp.shape)==[ncls*nl,ncls,nb],'q_shape':list(qm.shape)==list(qp.shape)==[ncls*nb,ncls,nl],'p_sha_equal':sha(pm)==sha(pp),'p_array_equal':bool(np.array_equal(pm,pp)),'q_sha_equal':sha(qm)==sha(qp),'q_array_equal':bool(np.array_equal(qm,qp)),'finite':bool(np.all(np.isfinite(pm)) and np.all(np.isfinite(pp)) and np.all(np.isfinite(qm)) and np.all(np.isfinite(qp))),'no_tolerance_rescue':True}
    result={'experiment':'Exp073EG','classification':cls,'token':TOKENS[cls],'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'pymaster_version':importlib.metadata.version('pymaster'),'source_head':a.source_head,'prereg_blob':a.prereg_blob,'checks':checks,'p_manual_sha256':sha(pm),'p_public_sha256':sha(pp),'q_manual_sha256':sha(qm),'q_public_sha256':sha(qp),'p_max_abs_difference_diagnostic_only':float(np.max(np.abs(pm-pp))),'q_max_abs_difference_diagnostic_only':float(np.max(np.abs(qm-qp))),'no_tolerance_rescue':True}
    (out/'terminal_diagnostic_receipt.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token']); print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
