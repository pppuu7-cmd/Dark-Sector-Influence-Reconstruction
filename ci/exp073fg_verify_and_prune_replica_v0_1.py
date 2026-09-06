#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

SCHEMA='dsir.exp073fg.ww_s0_s3.durable_ab_production.v0.1'
STAGES=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
SOURCE_HEAD='de83e20a68f79ccf25b89b0d33eb4206e294c757'
CONTRACT='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
NAMESPACES={'A':'checkpoints/exp073fg-ww-s0-s3-a-v0-1','B':'checkpoints/exp073fg-ww-s0-s3-b-v0-1'}
FULL_SHAPE=(4,39,4,12288); EE_SHAPE=(39,12288); SOURCE_SHAPE=(12*4096*4096,)

def sha(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()

def canon_npy(p:Path)->str:
    a=np.load(p,mmap_mode='r',allow_pickle=False)
    if a.dtype.str!='<f8' or tuple(a.shape)!=SOURCE_SHAPE: raise RuntimeError(f'fail-closed source geometry {p}')
    h=hashlib.sha256(memoryview(np.ascontiguousarray(np.asarray(a,dtype='<f8'))).cast('B')).hexdigest(); del a
    return h

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--checkpoint-root',required=True); ap.add_argument('--replica',choices=['A','B'],required=True); a=ap.parse_args()
    r=Path(a.checkpoint_root)/a.replica; ns=NAMESPACES[a.replica]
    manifests={}
    manifest_sha={}
    for st in STAGES:
        p=r/(st+'.json')
        if not p.is_file(): raise RuntimeError(f'fail-closed missing stage manifest {st}')
        o=json.loads(p.read_text())
        if o.get('schema')!=SCHEMA+'.checkpoint' or o.get('stage')!=st or o.get('complete') is not True or o.get('replica')!=a.replica or o.get('checkpoint_namespace')!=ns or o.get('source_head')!=SOURCE_HEAD or o.get('contract_fingerprint')!=CONTRACT or o.get('historical_ww_numerical_import') is not False or o.get('other_replica_output_read') is not False:
            raise RuntimeError(f'fail-closed stage identity {st}')
        manifests[st]=o; manifest_sha[st]=sha(p)
    src=manifests['fresh_sources_complete']['payloads']; p0=r/'s0_count_map.npy'; p3=r/'s1_count_map.npy'
    if not p0.is_file() or not p3.is_file(): raise RuntimeError('fail-closed missing source payload before prune')
    h0=canon_npy(p0); h3=canon_npy(p3)
    if h0!=src['s0_count_map']['canonical_sha256'] or h3!=src['s1_count_map']['canonical_sha256'] or src.get('ordered_source_indices')!=[0,3]: raise RuntimeError('fail-closed source payload hash/order before prune')
    wp=r/'fresh_workspace.fits'; full=r/'exact_route'/'full_window.bin'; ee=r/'exact_route'/'selected_ee.bin'; rp=r/'replica_receipt.json'
    for p in (wp,full,ee,rp):
        if not p.is_file(): raise RuntimeError(f'fail-closed missing payload before prune {p.name}')
    hwp=sha(wp); hfull=sha(full); hee=sha(ee); hrp=sha(rp)
    if hwp!=manifests['fresh_workspace_mcm_complete']['payloads']['workspace_fits']['sha256'] or hwp!=manifests['mcm_fits_verified']['payloads']['workspace_fits']['sha256']: raise RuntimeError('fail-closed workspace hash chain')
    if hfull!=manifests['full_window_complete']['payloads']['full_window']['sha256']: raise RuntimeError('fail-closed full-window hash chain')
    if hee!=manifests['selected_ee_complete']['payloads']['selected_ee']['sha256'] or hee!=manifests['replica_receipt_complete']['payloads']['selected_ee']['sha256']: raise RuntimeError('fail-closed selected-EE hash chain')
    if hrp!=manifests['replica_receipt_complete']['payloads']['replica_receipt']['sha256']: raise RuntimeError('fail-closed receipt hash chain')
    rec=json.loads(rp.read_text())
    expected={'replica':a.replica,'source_pair':'S0->S3','ordered_source_indices':[0,3],'same_field_object_handoff':False,'source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'checkpoint_namespace':ns,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False}
    for k,v in expected.items():
        if rec.get(k)!=v: raise RuntimeError(f'fail-closed terminal receipt identity {k}')
    if rec.get('selected_ee_sha256')!=hee: raise RuntimeError('fail-closed terminal selected SHA')
    out={'schema':'dsir.exp073fg.post_receipt_prune.v0.1','replica':a.replica,'checkpoint_namespace':ns,'source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'selected_ee_sha256':hee,'replica_receipt_sha256':hrp,'complete_chain_verified_before_prune':True,'preserved_complete_receipt':True,'pruned_only_after_receipt':True,'stage_manifest_sha256':manifest_sha,'verified_payload_sha256':{'s0_count_map':h0,'s3_count_map':h3,'workspace_fits':hwp,'full_window':hfull,'selected_ee':hee,'replica_receipt':hrp},'ordered_source_indices':[0,3],'source_pair':'S0->S3','no_tolerance_rescue':True}
    q=r/'post_receipt_prune.json'; q.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    # Only after the complete six-stage chain and all current payload hashes are bound above may large intermediates be removed.
    for p in (p0,p3,wp,full): p.unlink()
    print(f'PASS_EXP073FG_REPLICA_{a.replica}_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1')

if __name__=='__main__': main()
