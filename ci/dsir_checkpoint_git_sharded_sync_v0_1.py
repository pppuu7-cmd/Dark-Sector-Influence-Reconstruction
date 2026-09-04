#!/usr/bin/env python3
"""Fail-closed remote Git orchestration for DSIR sharded checkpoint payloads.

Infrastructure only. Preserves the existing checkpoints/* authority model.
"""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, subprocess, tempfile
from pathlib import Path

from dsir_checkpoint_sharded_payload_v0_1 import (
    BATCH_BYTES_MAX, CHUNK_BYTES, canonical_json, restore_file,
)

FORMAT = "DSIR_REMOTE_GIT_SHARDED_SYNC_V0_1"


def run(cmd, cwd=None, check=True):
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if check and p.returncode: raise RuntimeError(f"cmd failed rc={p.returncode}: {' '.join(cmd)}\n{p.stdout}\n{p.stderr}")
    return p


def query_remote(remote: str, branch: str) -> str|None:
    if not branch.startswith('checkpoints/'): raise RuntimeError('invalid checkpoint namespace')
    p=run(['git','ls-remote','--heads',remote,f'refs/heads/{branch}'],check=False)
    if p.returncode: raise RuntimeError('UNKNOWN_TRANSPORT_FAILURE querying remote')
    lines=[x for x in p.stdout.splitlines() if x.strip()]
    if not lines: return None
    if len(lines)!=1: raise RuntimeError('ambiguous remote state')
    sha,ref=lines[0].split()
    if ref!=f'refs/heads/{branch}' or len(sha)!=40: raise RuntimeError('malformed remote binding')
    return sha.lower()


def clone_head(remote: str, head: str|None, work: Path) -> None:
    run(['git','init',str(work)])
    run(['git','config','user.name','dsir-checkpoint-bot'],cwd=work)
    run(['git','config','user.email','dsir-checkpoint-bot@users.noreply.github.com'],cwd=work)
    run(['git','remote','add','origin',remote],cwd=work)
    if head:
        run(['git','fetch','--no-tags','origin',head],cwd=work)
        run(['git','checkout','--detach','FETCH_HEAD'],cwd=work)
    else:
        # Orphan checkpoint-only history.
        run(['git','checkout','--orphan','checkpoint-root'],cwd=work)
        for p in work.iterdir():
            if p.name!='.git': shutil.rmtree(p) if p.is_dir() else p.unlink()


def commit_all(work: Path, message: str) -> str:
    run(['git','add','-A'],cwd=work)
    run(['git','commit','--allow-empty','-m',message],cwd=work)
    return run(['git','rev-parse','HEAD'],cwd=work).stdout.strip().lower()


def push_exact(work: Path, remote: str, branch: str, expected_old: str|None, candidate: str) -> None:
    observed=query_remote(remote,branch)
    if observed!=expected_old: raise RuntimeError('stale lease before push')
    lease=f'refs/heads/{branch}:{expected_old or ""}'
    p=run(['git','push',f'--force-with-lease={lease}','origin',f'{candidate}:refs/heads/{branch}'],cwd=work,check=False)
    # Never trust push rc alone. Query exact post-state.
    post=query_remote(remote,branch)
    if post!=candidate:
        raise RuntimeError(f'post-push exact verification failed rc={p.returncode} observed={post}')


def load_pack_manifest(shard_dir: Path) -> dict:
    m=json.loads((shard_dir/'manifest.json').read_text())
    if m.get('complete') is not True or m.get('format')!='DSIR_SHARDED_CHECKPOINT_PAYLOAD_V0_1': raise RuntimeError('invalid shard manifest')
    return m


def sync_stage(shard_dir: Path, remote: str, branch: str, *, max_batch_bytes: int=BATCH_BYTES_MAX, stop_after_batches: int|None=None) -> dict:
    if max_batch_bytes<=0 or max_batch_bytes>BATCH_BYTES_MAX: raise RuntimeError('batch cap violation')
    m=load_pack_manifest(shard_dir)
    if m['checkpoint_namespace']!=branch: raise RuntimeError('manifest/branch namespace mismatch')
    head=query_remote(remote,branch)
    with tempfile.TemporaryDirectory(prefix='dsir-git-shards-') as td:
        work=Path(td)/'w'; clone_head(remote,head,work)
        root=work/'checkpoint'; chunks_dir=root/'chunks'; chunks_dir.mkdir(parents=True,exist_ok=True)
        existing={p.name for p in chunks_dir.glob('chunk_*.bin')}
        expected_names=[c['name'] for c in m['chunks']]
        extra=existing-set(expected_names)
        if extra: raise RuntimeError('extra checkpoint chunks present')
        # Verify already-present chunks before resume.
        for c in m['chunks']:
            p=chunks_dir/c['name']
            if p.exists():
                b=p.read_bytes()
                if len(b)!=c['bytes'] or hashlib.sha256(b).hexdigest()!=c['sha256']: raise RuntimeError('existing chunk corrupt')
        pending=[c for c in m['chunks'] if c['name'] not in existing]
        batches=0
        while pending:
            batch=[]; total=0
            while pending and total+pending[0]['bytes']<=max_batch_bytes:
                c=pending.pop(0); batch.append(c); total+=c['bytes']
            if not batch: raise RuntimeError('single chunk exceeds batch cap')
            for c in batch: shutil.copyfile(shard_dir/c['name'],chunks_dir/c['name'])
            state={'format':FORMAT,'stage_complete':False,'checkpoint_namespace':branch,'source_head':m['source_head'],'contract_fingerprint':m['contract_fingerprint'],'stage':m['stage'],'replica':m['replica'],'uploaded_chunks':len(expected_names)-len(pending),'total_chunks':len(expected_names),'new_payload_bytes_this_transition':total}
            (root/'transport_state.json').write_bytes(canonical_json(state))
            candidate=commit_all(work,f'checkpoint transport batch {batches+1}')
            push_exact(work,remote,branch,head,candidate); head=candidate; batches+=1
            if stop_after_batches is not None and batches>=stop_after_batches:
                return {'status':'PARTIAL','head':head,'batches':batches,'stage_complete':False}
        # Final completion commit contains manifest only after every chunk is durable.
        final=dict(m); final['transport_format']=FORMAT; final['stage_complete']=True
        (root/'final_manifest.json').write_bytes(canonical_json(final))
        state={'format':FORMAT,'stage_complete':True,'checkpoint_namespace':branch,'source_head':m['source_head'],'contract_fingerprint':m['contract_fingerprint'],'stage':m['stage'],'replica':m['replica'],'uploaded_chunks':len(expected_names),'total_chunks':len(expected_names),'new_payload_bytes_this_transition':0}
        (root/'transport_state.json').write_bytes(canonical_json(state))
        candidate=commit_all(work,'checkpoint stage complete')
        push_exact(work,remote,branch,head,candidate); head=candidate
        return {'status':'COMPLETE','head':head,'batches':batches,'stage_complete':True}


def restore_stage(remote: str, branch: str, dest: Path, *, expected_head: str, source_head: str, contract_fingerprint: str, stage: str, replica: str) -> dict:
    observed=query_remote(remote,branch)
    if observed!=expected_head: raise RuntimeError('restore head mismatch')
    with tempfile.TemporaryDirectory(prefix='dsir-restore-') as td:
        work=Path(td)/'w'; clone_head(remote,expected_head,work)
        root=work/'checkpoint'; fp=root/'final_manifest.json'
        if not fp.exists(): raise RuntimeError('partial checkpoint is not stage-complete')
        m=json.loads(fp.read_text())
        if m.get('stage_complete') is not True or m.get('checkpoint_namespace')!=branch: raise RuntimeError('final manifest mismatch')
        shard=Path(td)/'shards'; shard.mkdir()
        # Recreate DA shard-dir layout and use the admitted exact reassembler.
        base={k:v for k,v in m.items() if k not in {'transport_format','stage_complete'}}
        (shard/'manifest.json').write_bytes(canonical_json(base))
        for c in base['chunks']: shutil.copyfile(root/'chunks'/c['name'],shard/c['name'])
        restore_file(shard,dest,source_head=source_head,contract_fingerprint=contract_fingerprint,stage=stage,replica=replica,checkpoint_namespace=branch)
        return m


def self_test(root: Path) -> dict:
    from dsir_checkpoint_sharded_payload_v0_1 import pack_file, sha256_file
    root.mkdir(parents=True,exist_ok=True); remote=root/'remote.git'; run(['git','init','--bare',str(remote)])
    payload=root/'payload.bin'; seed=hashlib.sha256(b'Exp073DB-v0.1').digest(); payload.write_bytes((seed*((21*1024*1024+137)//len(seed)+1))[:21*1024*1024+137])
    shard=root/'shards'; ident=dict(source_head='a'*40,contract_fingerprint='b'*64,stage='fresh_workspace_mcm_complete',replica='A',checkpoint_namespace='checkpoints/exp073bu-wm-s3-a-v0-1')
    pack_file(payload,shard,logical_path='fresh_workspace.fits',chunk_bytes=4*1024*1024,**ident)
    # Force multiple transitions and an interruption.
    p1=sync_stage(shard,str(remote),ident['checkpoint_namespace'],max_batch_bytes=8*1024*1024,stop_after_batches=1)
    partial_rejected=False
    try: restore_stage(str(remote),ident['checkpoint_namespace'],root/'too-early.bin',expected_head=p1['head'],**{k:ident[k] for k in ('source_head','contract_fingerprint','stage','replica')})
    except RuntimeError: partial_rejected=True
    p2=sync_stage(shard,str(remote),ident['checkpoint_namespace'],max_batch_bytes=8*1024*1024)
    restored=root/'restored.bin'; restore_stage(str(remote),ident['checkpoint_namespace'],restored,expected_head=p2['head'],**{k:ident[k] for k in ('source_head','contract_fingerprint','stage','replica')})
    exact=sha256_file(payload)==sha256_file(restored) and payload.read_bytes()==restored.read_bytes()
    # A/B isolation: same manifest cannot be synced to B.
    isolation=False
    try: sync_stage(shard,str(remote),'checkpoints/exp073bu-wm-s3-b-v0-1',max_batch_bytes=8*1024*1024)
    except RuntimeError: isolation=True
    # Stale expected head must be rejected by exact push helper.
    stale=False
    try:
        with tempfile.TemporaryDirectory() as td:
            w=Path(td)/'w'; h=query_remote(str(remote),ident['checkpoint_namespace']); clone_head(str(remote),h,w); c=commit_all(w,'empty candidate'); push_exact(w,str(remote),ident['checkpoint_namespace'],'0'*40,c)
    except RuntimeError: stale=True
    return {'partial_stage_restore_rejected':partial_rejected,'resume_to_complete':p2['status']=='COMPLETE','exact_restore':exact,'ab_namespace_isolation':isolation,'stale_lease_rejected':stale,'multi_batch':p2['batches']>=2,'final_head_exact':query_remote(str(remote),ident['checkpoint_namespace'])==p2['head'],'stage_complete_only_final':p1['stage_complete'] is False and p2['stage_complete'] is True}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--work',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    if not a.self_test: raise SystemExit('v0.1 CLI exposes hosted self-test only')
    rec=self_test(Path(a.work)); Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if all(rec.values()) else 2)
if __name__=='__main__': main()
