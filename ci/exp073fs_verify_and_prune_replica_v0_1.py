#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np

SCHEMA='dsir.exp073fs.ww_s1_s2.durable_ab_production.v0.1'
STAGES=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
SOURCE_HEAD='de83e20a68f79ccf25b89b0d33eb4206e294c757'
CONTRACT='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
NAMESPACES={'A':'checkpoints/exp073fs-ww-s1-s2-a-v0-1','B':'checkpoints/exp073fs-ww-s1-s2-b-v0-1'}
SOURCE_SHAPE=(12*4096*4096,)

def sha(p:Path)->str:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''): h.update(b)
 return h.hexdigest()
def canon_npy(p:Path)->str:
 a=np.load(p,mmap_mode='r',allow_pickle=False)
 if a.dtype.str!='<f8' or tuple(a.shape)!=SOURCE_SHAPE: raise RuntimeError(f'fail-closed source geometry {p}')
 h=hashlib.sha256(memoryview(np.ascontiguousarray(np.asarray(a,dtype='<f8'))).cast('B')).hexdigest(); del a; return h

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--checkpoint-root',required=True); ap.add_argument('--replica',choices=['A','B'],required=True); a=ap.parse_args()
 r=Path(a.checkpoint_root)/a.replica; ns=NAMESPACES[a.replica]; manifests={}; manifest_sha={}
 for st in STAGES:
  p=r/(st+'.json')
  if not p.is_file(): raise RuntimeError(f'fail-closed missing stage manifest {st}')
  o=json.loads(p.read_text())
  if o.get('schema')!=SCHEMA+'.checkpoint' or o.get('stage')!=st or o.get('complete') is not True or o.get('replica')!=a.replica or o.get('checkpoint_namespace')!=ns or o.get('source_head')!=SOURCE_HEAD or o.get('contract_fingerprint')!=CONTRACT or o.get('historical_ww_numerical_import') is not False or o.get('other_replica_output_read') is not False: raise RuntimeError(f'fail-closed stage identity {st}')
  manifests[st]=o; manifest_sha[st]=sha(p)
 src=manifests['fresh_sources_complete']['payloads']; p1=r/'s1_count_map.npy'; p2=r/'s2_count_map.npy'
 if not p1.is_file() or not p2.is_file(): raise RuntimeError('fail-closed missing S1/S2 source payload before prune')
 h1=canon_npy(p1); h2=canon_npy(p2)
 if h1!=src['s1_count_map']['canonical_sha256'] or h2!=src['s2_count_map']['canonical_sha256'] or src.get('ordered_source_indices')!=[1,2] or src.get('reconstruction_counts')!={'s1':1,'s2':1} or src.get('same_source_map_both_sides') is not False: raise RuntimeError('fail-closed S1S2 source payload/order before prune')
 ws=manifests['fresh_workspace_mcm_complete']['payloads']; ids=ws.get('field_object_ids',[])
 if ws.get('ordered_source_indices')!=[1,2] or ws.get('same_field_object_handoff') is not False or ws.get('field_construction_count')!=2 or len(ids)!=2 or ids[0]==ids[1]: raise RuntimeError('fail-closed S1S2 distinct-field workspace semantics')
 wp=r/'fresh_workspace.fits'; full=r/'exact_route'/'full_window.bin'; ee=r/'exact_route'/'selected_ee.bin'; rp=r/'replica_receipt.json'
 for p in (wp,full,ee,rp):
  if not p.is_file(): raise RuntimeError(f'fail-closed missing payload before prune {p.name}')
 hwp=sha(wp); hfull=sha(full); hee=sha(ee); hrp=sha(rp)
 if hwp!=ws['workspace_fits']['sha256'] or hwp!=manifests['mcm_fits_verified']['payloads']['workspace_fits']['sha256']: raise RuntimeError('fail-closed workspace hash chain')
 if hfull!=manifests['full_window_complete']['payloads']['full_window']['sha256']: raise RuntimeError('fail-closed full-window hash chain')
 if hee!=manifests['selected_ee_complete']['payloads']['selected_ee']['sha256'] or hee!=manifests['replica_receipt_complete']['payloads']['selected_ee']['sha256']: raise RuntimeError('fail-closed selected-EE hash chain')
 if hrp!=manifests['replica_receipt_complete']['payloads']['replica_receipt']['sha256']: raise RuntimeError('fail-closed receipt hash chain')
 rec=json.loads(rp.read_text()); expected={'replica':a.replica,'source_pair':'S1->S2','ordered_source_indices':[1,2],'same_field_object_handoff':False,'source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'checkpoint_namespace':ns,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False}
 for k,v in expected.items():
  if rec.get(k)!=v: raise RuntimeError(f'fail-closed terminal receipt identity {k}')
 ad=rec.get('adapter_receipt',{})
 if ad.get('mcm_backing_bytes')!=19327352832 or ad.get('mcm_filebacked') is not True or ad.get('mcm_proc_maps') is not True or ad.get('read_unbinned_MCM') is not True or ad.get('route')!='public_get_bandpower_windows_after_filebacked_fits_read' or ad.get('no_tolerance_rescue') is not True: raise RuntimeError('fail-closed file-backed adapter evidence')
 out={'schema':'dsir.exp073fs.post_receipt_prune.v0.1','replica':a.replica,'checkpoint_namespace':ns,'source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'selected_ee_sha256':hee,'replica_receipt_sha256':hrp,'complete_chain_verified_before_prune':True,'preserved_complete_receipt':True,'pruned_only_after_receipt':True,'stage_manifest_sha256':manifest_sha,'verified_payload_sha256':{'s1_count_map':h1,'s2_count_map':h2,'workspace_fits':hwp,'full_window':hfull,'selected_ee':hee,'replica_receipt':hrp},'ordered_source_indices':[1,2],'source_pair':'S1->S2','same_field_object_handoff':False,'field_construction_count':2,'no_tolerance_rescue':True}
 (r/'post_receipt_prune.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 for p in (p1,p2,wp,full): p.unlink()
 print(f'PASS_EXP073FS_REPLICA_{a.replica}_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1')
if __name__=='__main__': main()
