#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.metadata,json
from pathlib import Path
import numpy as np
import pymaster as nmt
TOKENS={'DIRECT_PUBLIC_BPW_ADAPTER_EXACT':'PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1','DIRECT_PUBLIC_BPW_ADAPTER_FAIL':'COMPLETE_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_FAIL_V0_1'}
def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def masks(n):
 p=np.arange(12*n*n,dtype=np.int64); a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0); b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0); return a,b
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--prereg-blob',required=True); a=ap.parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
 n=16; nl=48; edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32); nb=8; s0,s1=masks(n); f0=nmt.NmtField(s0,None,spin=2,lmax=47,lmax_mask=47); f1=nmt.NmtField(s1,None,spin=2,lmax=47,lmax_mask=47); bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins); fp=out/'w01.fits'; w.write_to(str(fp)); del w
 wa=nmt.NmtWorkspace(); wa.read_from(str(fp)); fa=canon(wa.get_bandpower_windows()); sa=canon(fa[0,:,0,:]); del wa
 wb=nmt.NmtWorkspace(); wb.read_from(str(fp)); fb=canon(wb.get_bandpower_windows()); sb=canon(fb[0,:,0,:]); del wb
 checks={'distinct_masks':not np.array_equal(s0,s1),'full_shape':list(fa.shape)==list(fb.shape)==[4,nb,4,nl],'selected_shape':list(sa.shape)==list(sb.shape)==[nb,nl],'full_sha_equal':sha(fa)==sha(fb),'full_array_equal':bool(np.array_equal(fa,fb)),'selected_sha_equal':sha(sa)==sha(sb),'selected_array_equal':bool(np.array_equal(sa,sb)),'finite':bool(np.all(np.isfinite(fa)) and np.all(np.isfinite(fb))),'no_tolerance_rescue':True}
 ok=all(checks.values()); cls='DIRECT_PUBLIC_BPW_ADAPTER_EXACT' if ok else 'DIRECT_PUBLIC_BPW_ADAPTER_FAIL'; r={'experiment':'Exp073EK','classification':cls,'token':TOKENS[cls],'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'pymaster_version':importlib.metadata.version('pymaster'),'source_head':a.source_head,'prereg_blob':a.prereg_blob,'checks':checks,'full_a_sha256':sha(fa),'full_b_sha256':sha(fb),'selected_a_sha256':sha(sa),'selected_b_sha256':sha(sb),'no_tolerance_rescue':True}; (out/'terminal_diagnostic_receipt.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(r['token']); print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__': main()
