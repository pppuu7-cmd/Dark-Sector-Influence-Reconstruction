#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
import exp073cv_wm_s3_production_exact_adapter_v0_1 as base

SCHEMA='dsir.exp073do.ww_s0_s0.production_exact_adapter.v0.1'

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))

def execute(args):
    edges=np.asarray(json.loads(Path(args.edges_json).read_text()),dtype=np.int32)
    if edges.ndim!=1 or len(edges)<2 or edges[0]!=0 or edges[-1]!=args.nl or np.any(np.diff(edges)<=0): raise RuntimeError('invalid edges')
    if args.ncls!=4: raise RuntimeError('WW production contract requires ncls=4')
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    canonical=out/'mcm_canonical.bin'; full_path=out/'full_window.bin'; ee_path=out/'selected_ee.bin'; receipt_path=out/'receipt.json'
    mem=base.stream_fits_to_canonical_input(Path(args.workspace_fits),canonical,args.ncls,args.nl,edges)
    mmap_ok=('mmap.mmap' in mem['canonical_base_chain'] and mem['canonical_proc_maps'] and mem['fits_proc_maps'])
    if not mmap_ok: raise RuntimeError('fail-closed mmap proof failed')
    if mem['max_row_buffer_bytes'] != args.ncls*args.nl*8: raise RuntimeError('row-buffer contract failed')
    full=base.run_downstream(Path(args.emulator),canonical,full_path,args.ncls,len(edges)-1,args.nl)
    if tuple(full.shape)!=(4,len(edges)-1,4,args.nl): raise RuntimeError('WW full shape mismatch')
    ee=canon(full[0,:,0,:])
    if ee.shape!=(len(edges)-1,args.nl) or not np.all(np.isfinite(ee)): raise RuntimeError('selected EE invalid')
    ee_path.write_bytes(memoryview(ee).cast('B'))
    rec={
      'schema':SCHEMA,'status':'PRODUCTION_ADAPTER_EXECUTED','accounting':'+0/+0','science_gate_scored':False,
      'ww_s0_s0_authority_created':False,'ncls':4,'nl':args.nl,'nb':len(edges)-1,
      'workspace_fits_sha256':base.file_sha(args.workspace_fits),'canonical_mcm_sha256':base.file_sha(canonical),
      'full_window_sha256':base.file_sha(full_path),'selected_ee_sha256':base.file_sha(ee_path),
      'full_shape':[4,len(edges)-1,4,args.nl],'selected_ee_shape':[len(edges)-1,args.nl],
      'selected_semantics':'wins[0,:,0,:] = EE<-EE','memory':mem,'source_head':args.source_head,
      'contract_fingerprint':args.contract_fingerprint,'checkpoint_namespace':args.checkpoint_namespace,
      'component_blob_ids':json.loads(Path(args.component_blobs_json).read_text()),
      'durable_boundaries':['fresh_s0_mask_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete'],
      'no_tolerance_rescue':True,'get_coupling_matrix_materialization_forbidden':True,'historical_ww_numerical_import':False
    }
    receipt_path.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    del full
    return rec

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--workspace-fits',required=True); ap.add_argument('--edges-json',required=True); ap.add_argument('--ncls',type=int,required=True); ap.add_argument('--nl',type=int,required=True); ap.add_argument('--emulator',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--contract-fingerprint',required=True); ap.add_argument('--checkpoint-namespace',required=True); ap.add_argument('--component-blobs-json',required=True)
    a=ap.parse_args(); execute(a)
if __name__=='__main__': main()
