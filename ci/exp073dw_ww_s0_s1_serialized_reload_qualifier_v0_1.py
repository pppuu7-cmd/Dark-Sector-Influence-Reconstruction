#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import pymaster as nmt
from exp073do_ww_s0_s0_production_exact_adapter_v0_1 import execute as execute_adapter

PASS='PASS_EXP073DW_WW_S0_S1_SERIALIZED_RELOAD_EXACT_ADAPTER_V0_1'
FAIL='FAIL_EXP073DW_WW_S0_S1_SERIALIZED_RELOAD_EXACT_ADAPTER_V0_1'

def fsha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def csha(a):
    x=np.ascontiguousarray(np.asarray(a,dtype='<f8')); return hashlib.sha256(memoryview(x).cast('B')).hexdigest()
def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return a,b
def ws(fa,fb,bins,path):
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(fa,fb,bins); w.write_to(str(path)); return w

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--emulator',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--contract-fingerprint',required=True); ap.add_argument('--component-blobs-json',required=True); ap.add_argument('--nside',type=int,default=16); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True); nl=3*a.nside; edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32); (out/'edges.json').write_text(json.dumps(edges.tolist())+'\n')
    s0,s1=masks(a.nside); f0=nmt.NmtField(s0,None,spin=2); f1=nmt.NmtField(s1,None,spin=2); bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w01=ws(f0,f1,bins,out/'w01.fits'); w00=ws(f0,f0,bins,out/'w00.fits'); w11=ws(f1,f1,bins,out/'w11.fits')
    pre=np.asarray(w01.get_bandpower_windows(),dtype=np.float64)
    wr=nmt.NmtWorkspace(); wr.read_from(str(out/'w01.fits')); ref=np.asarray(wr.get_bandpower_windows(),dtype=np.float64); mref=np.asarray(wr.get_coupling_matrix(),dtype=np.float64)
    ns=argparse.Namespace(workspace_fits=str(out/'w01.fits'),edges_json=str(out/'edges.json'),ncls=4,nl=nl,emulator=a.emulator,out_dir=str(out/'adapter01'),source_head=a.source_head,contract_fingerprint=a.contract_fingerprint,checkpoint_namespace='qualifiers/exp073dw-ww-s0-s1-serialized-reload-v0-1',component_blobs_json=a.component_blobs_json)
    rec=execute_adapter(ns); shape=(4,8,4,48); full=np.memmap(out/'adapter01/full_window.bin',mode='r',dtype='<f8',shape=shape); ee=np.memmap(out/'adapter01/selected_ee.bin',mode='r',dtype='<f8',shape=(8,48)); ref_ee=np.ascontiguousarray(ref[0,:,0,:],dtype='<f8')
    checks={'distinct_source_masks':not np.array_equal(s0,s1),'distinct_field_objects':f0 is not f1,'reloaded_cross_differs_from_s0_auto':not np.array_equal(mref,np.asarray(w00.get_coupling_matrix())),'reloaded_cross_differs_from_s1_auto':not np.array_equal(mref,np.asarray(w11.get_coupling_matrix())),'adapter_full_exact_reloaded':bool(np.array_equal(full,ref)),'adapter_selected_exact_reloaded':bool(np.array_equal(ee,ref_ee)),'adapter_selected_sha_exact_reloaded':fsha(out/'adapter01/selected_ee.bin')==csha(ref_ee),'full_shape':list(full.shape)==list(shape),'selected_shape':list(ee.shape)==[8,48],'finite_reloaded':bool(np.all(np.isfinite(ref))),'finite_adapter':bool(np.all(np.isfinite(full))),'no_tolerance_rescue':rec.get('no_tolerance_rescue') is True}
    ok=all(checks.values()); result={'experiment':'Exp073DW','task':'WW_S0_S1','classification':'QUALIFIER_PASS' if ok else 'QUALIFIER_FAIL','token':PASS if ok else FAIL,'science_gate_scored':False,'ww_s0_s1_authority_created':False,'accounting':'+0/+0','pymaster_version':importlib.metadata.version('pymaster'),'checks':checks,'pre_serialization_vs_reloaded_full_array_equal':bool(np.array_equal(pre,ref)),'pre_serialization_selected_sha256':csha(pre[0,:,0,:]),'reloaded_selected_sha256':csha(ref_ee),'adapter_selected_sha256':fsha(out/'adapter01/selected_ee.bin'),'source_head':a.source_head,'contract_fingerprint':a.contract_fingerprint,'no_tolerance_rescue':True}
    (out/'terminal_qualifier_receipt.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token']); raise SystemExit(0 if ok else 2)
if __name__=='__main__': main()
