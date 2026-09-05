#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,tempfile
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt
import exp073cv_wm_s3_production_exact_adapter_v0_1 as wm_base
import exp073cv_wm_s3_production_exact_adapter_omp8_v0_3 as omp8
import exp073do_ww_s0_s0_production_exact_adapter_v0_1 as ww
PASS='PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1'
def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha_arr(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def synthetic(case,nside):
 npix=hp.nside2npix(nside); th,ph=hp.pix2ang(nside,np.arange(npix),nest=False)
 if case==0: x=(0.70+0.18*np.cos(th)+0.06*np.sin(2*ph))*((th>0.30)&(th<2.75)&(ph>0.20)&(ph<5.90))
 elif case==1: x=(0.63+0.20*np.sin(th)*np.cos(ph)+0.05*np.cos(3*ph))*((th>0.38)&(th<2.66)&(ph>0.35)&(ph<5.70))
 else: x=(0.67+0.15*np.cos(2*th)+0.07*np.sin(3*ph))*((th>0.26)&(th<2.80)&(ph>0.28)&(ph<5.82))
 return canon(x)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--emulator',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 nside=8; nl=24; edges=np.array([0,4,8,12,16,20,24],dtype=np.int32); rows=[]
 with tempfile.TemporaryDirectory() as td0:
  td=Path(td0); ej=td/'edges.json'; ej.write_text(json.dumps(edges.tolist())); cb=td/'components.json'; cb.write_text('{}')
  old=wm_base.run_downstream; wm_base.run_downstream=omp8.run_downstream_omp8
  try:
   for case in range(3):
    m=synthetic(case,nside); f=nmt.NmtField(m,None,spin=2,lmax=nl-1,lmax_mask=nl-1); b=nmt.NmtBin.from_edges(edges[:-1],edges[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f,f,b); ref=canon(w.get_bandpower_windows()); fp=td/f'case{case}.fits'; w.write_to(str(fp)); od=td/f'out{case}'
    ns=argparse.Namespace(workspace_fits=str(fp),edges_json=str(ej),ncls=4,nl=nl,emulator=a.emulator,out_dir=str(od),source_head='EXP073DP_SYNTHETIC',contract_fingerprint='EXP073DP_SYNTHETIC_V0_1',checkpoint_namespace=f'checkpoints/exp073dp/case{case}',component_blobs_json=str(cb))
    rec=ww.execute(ns); full=np.memmap(od/'full_window.bin',dtype='<f8',mode='r',shape=ref.shape); ee=np.fromfile(od/'selected_ee.bin',dtype='<f8').reshape(len(edges)-1,nl)
    full_eq=bool(np.array_equal(full,ref)); ee_ref=canon(ref[0,:,0,:]); ee_eq=bool(np.array_equal(ee,ee_ref))
    rows.append({'case':case,'reference_shape':list(ref.shape),'full_sha_equal':wm_base.file_sha(od/'full_window.bin')==sha_arr(ref),'full_array_equal':full_eq,'full_max_abs_difference':float(np.max(np.abs(full-ref))),'ee_sha_equal':wm_base.file_sha(od/'selected_ee.bin')==sha_arr(ee_ref),'ee_array_equal':ee_eq,'ee_max_abs_difference':float(np.max(np.abs(ee-ee_ref))),'semantics_ok':rec['selected_semantics']=='wins[0,:,0,:] = EE<-EE','firewall_ok':rec['science_gate_scored'] is False and rec['ww_s0_s0_authority_created'] is False,'mmap_ok':bool(rec['memory']['canonical_proc_maps'] and rec['memory']['fits_proc_maps'] and 'mmap.mmap' in rec['memory']['canonical_base_chain'])})
    del full
  finally: wm_base.run_downstream=old
 ok=all(r['reference_shape']==[4,6,4,24] and r['full_sha_equal'] and r['full_array_equal'] and r['full_max_abs_difference']==0.0 and r['ee_sha_equal'] and r['ee_array_equal'] and r['ee_max_abs_difference']==0.0 and r['semantics_ok'] and r['firewall_ok'] and r['mmap_ok'] for r in rows)
 out={'experiment':'Exp073DP','classification':'HOSTED_SYNTHETIC_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0' if ok else 'IMPLEMENTATION_EQUIVALENCE_FAIL_PLUS_0_PLUS_0','token':PASS if ok else 'FAIL_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1','science_gate_scored':False,'ww_authority_created':False,'home_execution_authorized':False,'no_tolerance_rescue':True,'cases':rows}; Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token']); raise SystemExit(0 if ok else 3)
if __name__=='__main__': main()
