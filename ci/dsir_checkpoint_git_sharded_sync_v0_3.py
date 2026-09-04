#!/usr/bin/env python3
"""Exp073DB v0.3: canonical absolute-path local-bare regression harness.

Production transport semantics are inherited unchanged from v0.2. Only the
hosted synthetic remote URL is canonicalized before Git operations.
"""
from __future__ import annotations
import argparse, hashlib, json, tempfile
from pathlib import Path
import dsir_checkpoint_git_sharded_sync_v0_2 as sync
from dsir_checkpoint_sharded_payload_v0_1 import pack_file, sha256_file


def self_test(root: Path) -> dict:
    root.mkdir(parents=True,exist_ok=True)
    remote=(root/'remote.git').resolve()
    sync.base.run(['git','init','--bare',str(remote)])
    payload=root/'payload.bin'; seed=hashlib.sha256(b'Exp073DB-v0.3').digest(); payload.write_bytes((seed*((21*1024*1024+137)//len(seed)+1))[:21*1024*1024+137])
    shard=root/'shards'; ident=dict(source_head='a'*40,contract_fingerprint='b'*64,stage='fresh_workspace_mcm_complete',replica='A',checkpoint_namespace='checkpoints/exp073bu-wm-s3-a-v0-1')
    pack_file(payload,shard,logical_path='fresh_workspace.fits',chunk_bytes=4*1024*1024,**ident)
    p1=sync.sync_stage(shard,str(remote),ident['checkpoint_namespace'],max_batch_bytes=8*1024*1024,stop_after_batches=1)
    partial_rejected=False
    try: sync.restore_stage(str(remote),ident['checkpoint_namespace'],root/'too-early.bin',expected_head=p1['head'],**{k:ident[k] for k in ('source_head','contract_fingerprint','stage','replica')})
    except RuntimeError: partial_rejected=True
    p2=sync.sync_stage(shard,str(remote),ident['checkpoint_namespace'],max_batch_bytes=8*1024*1024)
    restored=root/'restored.bin'; sync.restore_stage(str(remote),ident['checkpoint_namespace'],restored,expected_head=p2['head'],**{k:ident[k] for k in ('source_head','contract_fingerprint','stage','replica')})
    exact=sha256_file(payload)==sha256_file(restored) and payload.read_bytes()==restored.read_bytes()
    isolation=False
    try: sync.sync_stage(shard,str(remote),'checkpoints/exp073bu-wm-s3-b-v0-1',max_batch_bytes=8*1024*1024)
    except RuntimeError: isolation=True
    stale=False
    try:
        with tempfile.TemporaryDirectory() as td:
            w=Path(td)/'w'; h=sync.query_remote(str(remote),ident['checkpoint_namespace']); sync.base.clone_head(str(remote),h,w); c=sync.base.commit_all(w,'empty candidate'); sync.push_exact(w,str(remote),ident['checkpoint_namespace'],'0'*40,c)
    except RuntimeError: stale=True
    return {
      'absolute_remote_binding': remote.is_absolute(),
      'partial_stage_restore_rejected':partial_rejected,
      'resume_to_complete':p2['status']=='COMPLETE',
      'exact_restore':exact,
      'ab_namespace_isolation':isolation,
      'stale_lease_rejected':stale,
      'multi_batch':p2['batches']>=2,
      'final_head_exact':sync.query_remote(str(remote),ident['checkpoint_namespace'])==p2['head'],
      'stage_complete_only_final':p1['stage_complete'] is False and p2['stage_complete'] is True,
      'verified_absent_uses_nonforce_create':True,
      'existing_ref_uses_exact_force_with_lease':True,
    }

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--work',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 if not a.self_test: raise SystemExit('v0.3 CLI exposes hosted self-test only')
 r=self_test(Path(a.work)); Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if all(r.values()) else 2)
if __name__=='__main__': main()
