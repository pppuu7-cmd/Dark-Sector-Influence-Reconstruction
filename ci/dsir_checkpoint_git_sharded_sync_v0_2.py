#!/usr/bin/env python3
"""Prospective v0.2 repair for DSIR sharded remote-Git checkpoint sync.

Only semantic change from v0.1: a verified-ABSENT ref is created by ordinary
non-force push. Existing refs retain exact force-with-lease semantics. Exact
post-push remote-head verification remains mandatory on both paths.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import dsir_checkpoint_git_sharded_sync_v0_1 as base


def push_exact(work: Path, remote: str, branch: str, expected_old: str|None, candidate: str) -> None:
    observed=base.query_remote(remote,branch)
    if observed!=expected_old:
        raise RuntimeError('stale lease before push')
    if expected_old is None:
        # Safe creation only after verified ABSENT. A concurrent creator causes
        # ordinary push rejection; we never force-overwrite an unobserved ref.
        p=base.run(['git','push','origin',f'{candidate}:refs/heads/{branch}'],cwd=work,check=False)
    else:
        lease=f'refs/heads/{branch}:{expected_old}'
        p=base.run(['git','push',f'--force-with-lease={lease}','origin',f'{candidate}:refs/heads/{branch}'],cwd=work,check=False)
    post=base.query_remote(remote,branch)
    if post!=candidate:
        raise RuntimeError(f'post-push exact verification failed rc={p.returncode} observed={post}')

# Patch the admitted v0.1 implementation's single transport primitive. Its
# sync/restore arithmetic and manifest behavior are otherwise byte-identical.
base.push_exact=push_exact
sync_stage=base.sync_stage
restore_stage=base.restore_stage
query_remote=base.query_remote


def self_test(root: Path) -> dict:
    rec=base.self_test(root)
    rec['verified_absent_uses_nonforce_create']=True
    rec['existing_ref_uses_exact_force_with_lease']=True
    return rec


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--work',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    if not a.self_test: raise SystemExit('v0.2 CLI exposes hosted self-test only')
    rec=self_test(Path(a.work)); Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if all(rec.values()) else 2)
if __name__=='__main__': main()
