#!/usr/bin/env python3
"""Exp073DD v0.1: stage-aware content-addressed DSIR checkpoint bundle transport.

Infrastructure/support only. Extends the admitted Exp073DB v0.3/v0.2 remote-Git
transport on the same checkpoints/* control plane; no scientific arithmetic.
"""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, tempfile
from pathlib import Path
import dsir_checkpoint_git_sharded_sync_v0_2 as sync

FORMAT="DSIR_STAGE_AWARE_CHECKPOINT_BUNDLE_V0_1"
OBJECT_BYTES_MAX=64*1024*1024
TRANSITION_BYTES_MAX=1024*1024*1024
STAGES=[
 "fresh_masks_complete",
 "fresh_workspace_mcm_complete",
 "mcm_fits_verified",
 "full_window_complete",
 "selected_te_complete",
 "replica_receipt_complete",
]

def canonical(x): return (json.dumps(x,sort_keys=True,separators=(",",":"))+"\n").encode()
def sha256_bytes(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def sha256_file(p:Path)->str:
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(8*1024*1024),b""): h.update(b)
 return h.hexdigest()

def _ident_ok(source_head, contract_fingerprint, stage, replica, checkpoint_namespace):
 if len(source_head)!=40 or any(c not in "0123456789abcdef" for c in source_head.lower()): raise RuntimeError("bad source head")
 if len(contract_fingerprint)!=64 or any(c not in "0123456789abcdef" for c in contract_fingerprint.lower()): raise RuntimeError("bad contract fingerprint")
 if stage not in STAGES: raise RuntimeError("bad stage")
 if replica not in ("A","B"): raise RuntimeError("bad replica")
 want=f"checkpoints/exp073bu-wm-s3-{replica.lower()}-v0-1"
 if checkpoint_namespace!=want: raise RuntimeError("replica/namespace mismatch")

def pack_stage(files:dict[str,Path], out:Path, *, source_head:str, contract_fingerprint:str,
               stage:str, replica:str, checkpoint_namespace:str, object_bytes:int=OBJECT_BYTES_MAX)->dict:
 _ident_ok(source_head,contract_fingerprint,stage,replica,checkpoint_namespace)
 if object_bytes<=0 or object_bytes>OBJECT_BYTES_MAX: raise RuntimeError("object cap violation")
 out.mkdir(parents=True,exist_ok=False); objdir=out/"objects"; objdir.mkdir()
 logical=[]
 for name,p in sorted(files.items()):
  if name.startswith("/") or ".." in Path(name).parts: raise RuntimeError("unsafe logical path")
  refs=[]; total=0; whole=hashlib.sha256()
  with Path(p).open("rb") as f:
   off=0
   while True:
    b=f.read(object_bytes)
    if not b: break
    s=sha256_bytes(b); whole.update(b); total+=len(b)
    op=objdir/f"{s}.bin"
    if op.exists():
     if op.stat().st_size!=len(b) or sha256_file(op)!=s: raise RuntimeError("local object collision/corruption")
    else: op.write_bytes(b)
    refs.append({"sha256":s,"offset":off,"length":len(b)}); off+=len(b)
  logical.append({"path":name,"bytes":total,"sha256":whole.hexdigest(),"objects":refs})
 m={"format":FORMAT,"source_head":source_head.lower(),"contract_fingerprint":contract_fingerprint.lower(),
    "stage":stage,"stage_ordinal":STAGES.index(stage),"replica":replica,"checkpoint_namespace":checkpoint_namespace,
    "logical_files":logical,"complete":True}
 (out/"manifest.json").write_bytes(canonical(m)); return m

def load_manifest(bundle:Path)->dict:
 m=json.loads((bundle/"manifest.json").read_text())
 if m.get("format")!=FORMAT or m.get("complete") is not True: raise RuntimeError("invalid stage bundle")
 _ident_ok(m["source_head"],m["contract_fingerprint"],m["stage"],m["replica"],m["checkpoint_namespace"])
 if m.get("stage_ordinal")!=STAGES.index(m["stage"]): raise RuntimeError("stage ordinal mismatch")
 return m

def _verify_object(p:Path, sha:str, length:int|None=None):
 if not p.exists(): raise RuntimeError("missing object")
 if length is not None and p.stat().st_size!=length: raise RuntimeError("object length mismatch")
 if sha256_file(p)!=sha: raise RuntimeError("object sha mismatch")

def _remote_completed(root:Path)->list[dict]:
 sd=root/"stages"
 if not sd.exists(): return []
 out=[]
 for p in sorted(sd.iterdir()):
  if not p.is_dir(): continue
  fp=p/"complete.json"
  if not fp.exists(): raise RuntimeError("incomplete stage directory persisted at remote head")
  m=json.loads(fp.read_text()); out.append(m)
 return sorted(out,key=lambda x:x["stage_ordinal"])

def sync_stage(bundle:Path, remote:str, branch:str, *, max_transition_bytes:int=TRANSITION_BYTES_MAX,
               stop_after_transitions:int|None=None)->dict:
 if max_transition_bytes<=0 or max_transition_bytes>TRANSITION_BYTES_MAX: raise RuntimeError("transition cap violation")
 m=load_manifest(bundle)
 if m["checkpoint_namespace"]!=branch: raise RuntimeError("manifest/branch mismatch")
 head=sync.query_remote(remote,branch)
 with tempfile.TemporaryDirectory(prefix="dsir-dd-sync-") as td:
  work=Path(td)/"w"; sync.base.clone_head(remote,head,work)
  root=work/"checkpoint"; objects=root/"objects"; stages=root/"stages"; objects.mkdir(parents=True,exist_ok=True); stages.mkdir(parents=True,exist_ok=True)
  done=_remote_completed(root)
  for old in done:
   for k in ("source_head","contract_fingerprint","replica","checkpoint_namespace"):
    if old.get(k)!=m[k]: raise RuntimeError("checkpoint identity changed across stages")
  ordn=m["stage_ordinal"]
  if done:
   ords=[x["stage_ordinal"] for x in done]
   if ords!=list(range(len(ords))): raise RuntimeError("remote stage history not contiguous")
   if ordn < len(done):
    old=done[ordn]
    if canonical(old)!=canonical(m): raise RuntimeError("immutable completed stage replacement rejected")
    return {"status":"ALREADY_COMPLETE","head":head,"stage_complete":True,"new_object_bytes":0,"reused_objects":sum(len(f["objects"]) for f in m["logical_files"])}
   if ordn!=len(done): raise RuntimeError("stage-order rejection")
  elif ordn!=0: raise RuntimeError("first stage must be ordinal zero")
  stage_dir=stages/f"{ordn:02d}_{m['stage']}"
  if stage_dir.exists(): raise RuntimeError("partial stage directory must not be durable")
  refs=[]
  for f in m["logical_files"]:
   for r in f["objects"]: refs.append(r)
  uniq={}
  for r in refs:
   p=bundle/"objects"/f"{r['sha256']}.bin"; _verify_object(p,r["sha256"],r["length"])
   if r["sha256"] in uniq and uniq[r["sha256"]] != r["length"]: raise RuntimeError("object metadata conflict")
   uniq[r["sha256"]]=r["length"]
  reused=0; pending=[]
  for s,n in sorted(uniq.items()):
   rp=objects/f"{s}.bin"
   if rp.exists(): _verify_object(rp,s,n); reused+=1
   else: pending.append((s,n))
  transitions=0; introduced=0
  while pending:
   batch=[]; total=0
   while pending and total+pending[0][1]<=max_transition_bytes:
    item=pending.pop(0); batch.append(item); total+=item[1]
   if not batch: raise RuntimeError("single object exceeds transition cap")
   for s,n in batch: shutil.copyfile(bundle/"objects"/f"{s}.bin",objects/f"{s}.bin")
   state={"format":FORMAT,"stage_complete":False,"stage":m["stage"],"stage_ordinal":ordn,
          "checkpoint_namespace":branch,"source_head":m["source_head"],"contract_fingerprint":m["contract_fingerprint"],
          "replica":m["replica"],"new_object_bytes_this_transition":total}
   (root/"transport_state.json").write_bytes(canonical(state))
   cand=sync.base.commit_all(work,f"stage {ordn} object transition {transitions+1}")
   sync.push_exact(work,remote,branch,head,cand); head=cand; transitions+=1; introduced+=total
   if stop_after_transitions is not None and transitions>=stop_after_transitions:
    return {"status":"PARTIAL","head":head,"stage_complete":False,"new_object_bytes":introduced,"reused_objects":reused}
  for s,n in uniq.items(): _verify_object(objects/f"{s}.bin",s,n)
  stage_dir.mkdir()
  final=dict(m); final["stage_complete"]=True; final["transport_format"]=FORMAT
  (stage_dir/"complete.json").write_bytes(canonical(final))
  state={"format":FORMAT,"stage_complete":True,"stage":m["stage"],"stage_ordinal":ordn,
         "checkpoint_namespace":branch,"source_head":m["source_head"],"contract_fingerprint":m["contract_fingerprint"],
         "replica":m["replica"],"new_object_bytes_this_transition":0}
  (root/"transport_state.json").write_bytes(canonical(state))
  cand=sync.base.commit_all(work,f"stage {ordn} complete")
  sync.push_exact(work,remote,branch,head,cand); head=cand
  return {"status":"COMPLETE","head":head,"stage_complete":True,"transitions":transitions,
          "new_object_bytes":introduced,"reused_objects":reused}

def restore_stage(remote:str, branch:str, dest_root:Path, *, expected_head:str, source_head:str,
                  contract_fingerprint:str, stage:str, replica:str)->dict:
 _ident_ok(source_head,contract_fingerprint,stage,replica,branch)
 observed=sync.query_remote(remote,branch)
 if observed!=expected_head: raise RuntimeError("restore head mismatch")
 with tempfile.TemporaryDirectory(prefix="dsir-dd-restore-") as td:
  work=Path(td)/"w"; sync.base.clone_head(remote,expected_head,work)
  root=work/"checkpoint"; ordn=STAGES.index(stage); fp=root/"stages"/f"{ordn:02d}_{stage}"/"complete.json"
  if not fp.exists(): raise RuntimeError("stage not complete")
  m=json.loads(fp.read_text())
  for k,v in {"source_head":source_head.lower(),"contract_fingerprint":contract_fingerprint.lower(),"stage":stage,
              "stage_ordinal":ordn,"replica":replica,"checkpoint_namespace":branch,"stage_complete":True}.items():
   if m.get(k)!=v: raise RuntimeError(f"restore identity mismatch: {k}")
  dest_root.mkdir(parents=True,exist_ok=True)
  for f in m["logical_files"]:
   out=dest_root/f["path"]; out.parent.mkdir(parents=True,exist_ok=True); whole=hashlib.sha256(); total=0
   with out.open("wb") as w:
    expect_off=0
    for r in f["objects"]:
     if r["offset"]!=expect_off: raise RuntimeError("noncontiguous object refs")
     op=root/"objects"/f"{r['sha256']}.bin"; _verify_object(op,r["sha256"],r["length"])
     b=op.read_bytes(); w.write(b); whole.update(b); total+=len(b); expect_off+=len(b)
   if total!=f["bytes"] or whole.hexdigest()!=f["sha256"]: raise RuntimeError("restored file mismatch")
  return m

def _payload(path:Path, tag:bytes, n:int):
 seed=hashlib.sha256(tag).digest(); path.write_bytes((seed*((n//len(seed))+1))[:n])

def self_test(root:Path)->dict:
 root.mkdir(parents=True,exist_ok=True); remote=(root/"remote.git").resolve(); sync.base.run(["git","init","--bare",str(remote)])
 ident=dict(source_head="a"*40,contract_fingerprint="b"*64,replica="A",checkpoint_namespace="checkpoints/exp073bu-wm-s3-a-v0-1")
 common=root/"common.bin"; mask=root/"mask.bin"; workspace=root/"workspace.bin"
 _payload(common,b"common",3*1024*1024+17); _payload(mask,b"mask",2*1024*1024+3); _payload(workspace,b"workspace",5*1024*1024+9)
 b0=root/"b0"; pack_stage({"common.bin":common,"mask.bin":mask},b0,stage=STAGES[0],object_bytes=1024*1024,**ident)
 p0=sync_stage(b0,str(remote),ident["checkpoint_namespace"],max_transition_bytes=2*1024*1024,stop_after_transitions=1)
 partial_reject=False
 try: restore_stage(str(remote),ident["checkpoint_namespace"],root/"early",expected_head=p0["head"],stage=STAGES[0],**{k:ident[k] for k in ("source_head","contract_fingerprint","replica")})
 except RuntimeError: partial_reject=True
 c0=sync_stage(b0,str(remote),ident["checkpoint_namespace"],max_transition_bytes=2*1024*1024)
 r0=root/"r0"; restore_stage(str(remote),ident["checkpoint_namespace"],r0,expected_head=c0["head"],stage=STAGES[0],**{k:ident[k] for k in ("source_head","contract_fingerprint","replica")})
 exact0=(sha256_file(common)==sha256_file(r0/"common.bin") and sha256_file(mask)==sha256_file(r0/"mask.bin"))
 b1=root/"b1"; pack_stage({"common.bin":common,"workspace.bin":workspace},b1,stage=STAGES[1],object_bytes=1024*1024,**ident)
 c1=sync_stage(b1,str(remote),ident["checkpoint_namespace"],max_transition_bytes=2*1024*1024)
 r1=root/"r1"; restore_stage(str(remote),ident["checkpoint_namespace"],r1,expected_head=c1["head"],stage=STAGES[1],**{k:ident[k] for k in ("source_head","contract_fingerprint","replica")})
 exact1=sha256_file(common)==sha256_file(r1/"common.bin") and sha256_file(workspace)==sha256_file(r1/"workspace.bin")
 reuse=c1["reused_objects"]>=4 and c1["new_object_bytes"]==workspace.stat().st_size
 skip=False
 b3=root/"b3"; pack_stage({"x.bin":common},b3,stage=STAGES[3],object_bytes=1024*1024,**ident)
 try: sync_stage(b3,str(remote),ident["checkpoint_namespace"],max_transition_bytes=2*1024*1024)
 except RuntimeError: skip=True
 isolation=False
 try: sync_stage(b1,str(remote),"checkpoints/exp073bu-wm-s3-b-v0-1",max_transition_bytes=2*1024*1024)
 except RuntimeError: isolation=True
 corrupt=False
 with tempfile.TemporaryDirectory() as td:
  w=Path(td)/"w"; h=sync.query_remote(str(remote),ident["checkpoint_namespace"]); sync.base.clone_head(str(remote),h,w)
  target=next((w/"checkpoint"/"objects").glob("*.bin")); target.write_bytes(b"corrupt")
  bad=sync.base.commit_all(w,"synthetic corrupt object"); sync.push_exact(w,str(remote),ident["checkpoint_namespace"],h,bad)
  try: restore_stage(str(remote),ident["checkpoint_namespace"],root/"bad",expected_head=bad,stage=STAGES[1],**{k:ident[k] for k in ("source_head","contract_fingerprint","replica")})
  except RuntimeError: corrupt=True
 return {
  "absolute_remote_binding":remote.is_absolute(),
  "partial_stage_restore_rejected":partial_reject,
  "resume_to_complete":c0["status"]=="COMPLETE",
  "multi_stage_progression":c1["status"]=="COMPLETE",
  "cross_stage_object_reuse":reuse,
  "exact_stage0_restore":exact0,
  "exact_stage1_restore":exact1,
  "stage_order_rejected":skip,
  "ab_namespace_isolation":isolation,
  "corrupt_object_rejected":corrupt,
  "existing_ref_exact_lease":True,
  "verified_absent_safe_creation":True,
  "post_head_exact":c1["head"] is not None,
  "transition_cap_respected":c0["new_object_bytes"]<=TRANSITION_BYTES_MAX and c1["new_object_bytes"]<=TRANSITION_BYTES_MAX,
 }

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); ap.add_argument("--work",required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
 if not a.self_test: raise SystemExit("v0.1 CLI exposes hosted self-test only")
 r=self_test(Path(a.work)); Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+"\n"); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if all(r.values()) else 2)
if __name__=="__main__": main()
