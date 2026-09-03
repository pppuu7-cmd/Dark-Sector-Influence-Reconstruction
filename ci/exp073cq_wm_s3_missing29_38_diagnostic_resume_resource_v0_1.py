#!/usr/bin/env python3
from __future__ import annotations
import argparse, concurrent.futures as cf, hashlib, json, os, re, shutil, subprocess, time, traceback
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import exp073cp_wm_s3_full39_transport_resource_v0_1 as cp

PREREG_COMMIT='60c975edb35c13bd22907440f4ed767a5fc55712'
SYNC_COMMIT='c20127b6762c6fc9b21875a321aecd7a4cd5f88e'
POLICY_COMMIT='f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427'
PARENT_NAMESPACE='checkpoints/exp073cp-wm-s3-full39-resource-v0-1'
PARENT_HEAD='025629d9bb7b113bd0548ff6a32c6ee5812ae245'
PARENT_FINGERPRINT='32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc'
NAMESPACE='checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-1'
IMPORTED=tuple(range(29)); ALLOWED=tuple(range(29,39)); ALL=tuple(range(39))
L=cp.co.L; EDGES=cp.co.EDGES; PCL_SHA=cp.co.PCL_SHA; REFERENCE_SHA=cp.co.REFERENCE_SHA; CPU_MIN=0.90
PASS='PASS_EXP073CQ_WM_S3_MISSING29_38_8WORKER_DIAGNOSTIC_RESUME_RESOURCE_V0_1'
FAIL_EXACT='FAIL_EXP073CQ_WM_S3_EXACT_EQUIVALENCE_V0_1'; FAIL_SWAP='FAIL_EXP073CQ_WM_S3_SWAP_SAFETY_V0_1'; FAIL_CPU='FAIL_EXP073CQ_WM_S3_CPU_TARGET_V0_1'

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def chash(x):
    a=canon(x); return hashlib.sha256(memoryview(a).cast('B')).hexdigest()
def fhash(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def jhash(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def atomic_json(p:Path,o:dict):
    p.parent.mkdir(parents=True,exist_ok=True); q=p.with_suffix(p.suffix+'.tmp'); q.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n'); os.replace(q,p)
def exact_env_commit(k):
    v=os.environ.get(k,'').lower()
    if not re.fullmatch(r'[0-9a-f]{40}',v): raise RuntimeError(f'{k} is not an exact commit; fail closed')
    return v

def contract(source_head,driver_commit):
    d={'format':'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1','experiment':'Exp073CQ','version':'v0.1','task':'Wm_S3',
       'source_head':source_head,'driver_commit':driver_commit,'workflow_commit':exact_env_commit('DSIR_WORKFLOW_COMMIT'),
       'binding_commit':exact_env_commit('DSIR_BINDING_COMMIT'),'prereg_commit':PREREG_COMMIT,'policy_commit':POLICY_COMMIT,
       'checkpoint_sync_commit':SYNC_COMMIT,'checkpoint_namespace':NAMESPACE,'parent_checkpoint_namespace':PARENT_NAMESPACE,
       'parent_checkpoint_head':PARENT_HEAD,'parent_contract_fingerprint':PARENT_FINGERPRINT,'imported_parent_bands':list(IMPORTED),
       'compute_allowlist':list(ALLOWED),'source_bin':3,'signature':[0,2,0,2],'lmax':L-1,'row_length':L,'bands':list(ALL),
       'outer_workers':8,'max_inflight_futures':8,'nested_threads':1,'cpu_fraction_min':CPU_MIN,'dtype':'<f8',
       'pcl_sha256':PCL_SHA,'reference_sha256':REFERENCE_SHA,'transport_contract':'bounded_retry_timeout_http1.1_exact_head_v0.3',
       'checkpoint_boundary':'complete_parent_import_or_complete_new_band_or_diagnostic_or_telemetry_or_final_only',
       'cpu_metric':'sum_new_worker_cpu_seconds_div_earliest_to_latest_new_band_start_end_29_38_only',
       'verified_delta':0.0,'draft_data_delta':0.0}; d['fingerprint']=jhash(d); return d

def load_contract(root):
    c=json.loads((root/'contract.json').read_text()); fp=c.get('fingerprint'); x=dict(c); x.pop('fingerprint',None)
    if fp!=jhash(x): raise RuntimeError('successor contract fingerprint mismatch')
    return c

def init(root,source_head,driver_commit):
    root.mkdir(parents=True,exist_ok=True); want=contract(source_head,driver_commit); p=root/'contract.json'
    if p.exists() and json.loads(p.read_text())!=want: raise RuntimeError('successor checkpoint contract mismatch; fail closed')
    if not p.exists(): atomic_json(p,want)
    print(want['fingerprint'],flush=True)

def exact_array(p,shape,label):
    a=np.load(p,allow_pickle=False)
    if a.dtype.str!='<f8' or not a.flags.c_contiguous or tuple(a.shape)!=tuple(shape) or not np.all(np.isfinite(a)): raise RuntimeError(f'{label}: invalid canonical payload')
    return a

def band_dir(root,b): return root/'bands'/f'band_{b:02d}'
def load_band(root,b):
    c=load_contract(root); d=band_dir(root,b); rp=d/'receipt.json'
    if not rp.exists(): return None
    r=json.loads(rp.read_text()); a=exact_array(d/'payload.npy',(L,),f'band {b}')
    if r.get('complete') is not True or r.get('contract_fingerprint')!=c['fingerprint'] or r.get('band')!=b or r.get('payload_sha256')!=chash(a): raise RuntimeError(f'band {b}: successor checkpoint mismatch')
    if r.get('ell_interval')!=[int(EDGES[b]),int(EDGES[b+1])]: raise RuntimeError(f'band {b}: ell interval mismatch')
    if b in IMPORTED and r.get('origin')!='imported_exact_parent_exp073cp': raise RuntimeError(f'band {b}: imported provenance mismatch')
    if b in ALLOWED and r.get('origin')!='new_numerical_exp073cq': raise RuntimeError(f'band {b}: numerical provenance mismatch')
    return r

def validate_parent(parent):
    pc=cp.co.load_contract(parent)
    if pc.get('fingerprint')!=PARENT_FINGERPRINT or pc.get('checkpoint_namespace')!=PARENT_NAMESPACE: raise RuntimeError('parent contract authority mismatch')
    pcl,ref=cp.co.validate_upstream(parent)
    if chash(pcl)!=PCL_SHA or chash(ref)!=REFERENCE_SHA: raise RuntimeError('parent upstream SHA mismatch')
    for b in IMPORTED:
        if cp.co.load_band(parent,b) is None: raise RuntimeError(f'parent required band {b} absent')
    for b in ALLOWED:
        if cp.co.load_band(parent,b) is not None: raise RuntimeError(f'parent frozen head unexpectedly contains band {b}')
    return pc,pcl,ref

def import_parent(root,parent):
    c=load_contract(root); pc,pcl,ref=validate_parent(parent); u=root/'upstream'; u.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(parent/'upstream/pcl.npy',u/'pcl.npy'); shutil.copyfile(parent/'upstream/reference_0_7.npy',u/'reference_0_7.npy')
    atomic_json(u/'receipt.json',{'format':c['format'],'experiment':'Exp073CQ','stage':'upstream','complete':True,'contract_fingerprint':c['fingerprint'],'origin':'imported_exact_parent_exp073cp','parent_head':PARENT_HEAD,'parent_contract_fingerprint':pc['fingerprint'],'pcl_sha256':chash(pcl),'reference_sha256':chash(ref),'dtype':'<f8'})
    for b in IMPORTED:
        sd=cp.co.band_dir(parent,b); pd=band_dir(root,b); pd.mkdir(parents=True,exist_ok=True); pa=cp.co.exact_array(sd/'payload.npy',(L,),f'parent band {b}'); pr=json.loads((sd/'receipt.json').read_text())
        shutil.copyfile(sd/'payload.npy',pd/'payload.npy')
        atomic_json(pd/'receipt.json',{'format':c['format'],'experiment':'Exp073CQ','task':'Wm_S3','stage':'band','complete':True,'contract_fingerprint':c['fingerprint'],'origin':'imported_exact_parent_exp073cp','parent_head':PARENT_HEAD,'parent_contract_fingerprint':pc['fingerprint'],'parent_receipt_file_sha256':fhash(sd/'receipt.json'),'parent_payload_sha256':pr['payload_sha256'],'band':b,'ell_interval':[int(EDGES[b]),int(EDGES[b+1])],'shape':[L],'dtype':'<f8','payload_sha256':chash(pa),'pcl_sha256':PCL_SHA,'outer_workers':8,'nested_threads':1})
    validate(root,require_parent_import=True)

def validate_upstream(root):
    c=load_contract(root); u=root/'upstream'; r=json.loads((u/'receipt.json').read_text()); pcl=exact_array(u/'pcl.npy',(L,),'PCL'); ref=exact_array(u/'reference_0_7.npy',(8,L),'reference')
    if r.get('complete') is not True or r.get('contract_fingerprint')!=c['fingerprint'] or r.get('origin')!='imported_exact_parent_exp073cp': raise RuntimeError('successor upstream receipt mismatch')
    if chash(pcl)!=PCL_SHA or chash(ref)!=REFERENCE_SHA: raise RuntimeError('successor upstream SHA mismatch')
    return pcl,ref

def validate(root,require_parent_import=False):
    validate_upstream(root)
    for b in IMPORTED:
        if load_band(root,b) is None: raise RuntimeError(f'imported successor band {b} absent')
    missing=[]
    for b in ALLOWED:
        if load_band(root,b) is None: missing.append(b)
    if require_parent_import and tuple(missing)!=ALLOWED: raise RuntimeError(f'initial missing allowlist changed: {missing}')
    print(json.dumps({'complete_imported_bands':list(IMPORTED),'missing_new_bands':missing},sort_keys=True),flush=True); return missing

def store_band(root,b,a,tel):
    if b not in ALLOWED: raise RuntimeError(f'worker submission outside frozen allowlist: {b}')
    c=load_contract(root); d=band_dir(root,b); d.mkdir(parents=True,exist_ok=True); a=canon(a); np.save(d/'payload.npy',a,allow_pickle=False)
    r={'format':c['format'],'experiment':'Exp073CQ','task':'Wm_S3','stage':'band','complete':True,'contract_fingerprint':c['fingerprint'],'origin':'new_numerical_exp073cq','band':b,'ell_interval':[int(EDGES[b]),int(EDGES[b+1])],'shape':[L],'dtype':'<f8','payload_sha256':chash(a),'pcl_sha256':PCL_SHA,'outer_workers':8,'nested_threads':1,**tel}; atomic_json(d/'receipt.json',r); return r

def sync(root,branch,script,label):
    p=subprocess.run(['bash',str(script),'push',str(root),branch,label],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if p.stdout: print(p.stdout,end='' if p.stdout.endswith('\n') else '\n',flush=True)
    if p.returncode: raise subprocess.CalledProcessError(p.returncode,p.args,output=p.stdout)

def _abort(ex):
    for x in list(getattr(ex,'_pending_work_items',{}).values()):
        try: x.future.cancel()
        except Exception: pass
    procs=list(getattr(ex,'_processes',{}).values()); ex.shutdown(wait=False,cancel_futures=True)
    for p in procs:
        try:
            if p.is_alive(): p.terminate()
        except Exception: pass

def diagnostic(root,stage,exc,branch=None,script=None,admitted=None):
    try: c=load_contract(root); fp=c['fingerprint']
    except Exception: fp=None
    try: missing=[b for b in ALLOWED if not (band_dir(root,b)/'receipt.json').exists()]
    except Exception: missing=list(ALLOWED)
    rec={'format':'DSIR_DIAGNOSTIC_V0_1','experiment':'Exp073CQ','version':'v0.1','stage':stage,'complete':True,'exception_type':type(exc).__name__,'exception_string':str(exc),'traceback':''.join(traceback.format_exception(type(exc),exc,exc.__traceback__))[-16000:],'source_head':os.environ.get('GITHUB_SHA'),'driver_commit':os.environ.get('DSIR_DRIVER_COMMIT'),'workflow_commit':os.environ.get('DSIR_WORKFLOW_COMMIT'),'binding_commit':os.environ.get('DSIR_BINDING_COMMIT'),'contract_fingerprint':fp,'parent_checkpoint_head':PARENT_HEAD,'newly_admitted_bands':sorted(admitted or []),'still_missing_allowlist':missing,'timestamp_utc':datetime.now(timezone.utc).isoformat()}
    atomic_json(root/'diagnostics'/'first_failure.json',rec)
    if branch and script:
        try: sync(root,branch,Path(script),'diagnostic-first-failure')
        except Exception as de: print(f'DIAGNOSTIC_SYNC_FAILED {type(de).__name__}: {de}',flush=True)
    print(json.dumps(rec,sort_keys=True),flush=True)

def swap_used_kib(): return cp.co.swap_used_kib()
def compute(root,ca_so,branch,sync_script):
    missing=validate(root); illegal=[b for b in missing if b not in ALLOWED]
    if illegal: raise RuntimeError(f'illegal missing bands {illegal}')
    if not missing: print('all successor numerical bands already checkpointed',flush=True); return
    swap0=swap_used_kib(); wall0=time.monotonic(); admitted=[]; worker_tels=[]; ex=cf.ProcessPoolExecutor(max_workers=8); futs={}; pending=iter(missing)
    try:
        for _ in range(min(8,len(missing))):
            b=next(pending); futs[ex.submit(cp.co.timed_worker,b,str(root/'upstream/pcl.npy'),str(ca_so))]=b
        while futs:
            done,_=cf.wait(tuple(futs),return_when=cf.FIRST_COMPLETED)
            for fut in done:
                b=futs.pop(fut); b2,a,tel=fut.result()
                if b2!=b or b not in ALLOWED: raise RuntimeError(f'worker identity/allowlist mismatch expected={b} got={b2}')
                store_band(root,b,a,tel)
                try:
                    nb=next(pending); futs[ex.submit(cp.co.timed_worker,nb,str(root/'upstream/pcl.npy'),str(ca_so))]=nb
                except StopIteration: pass
                sync(root,branch,sync_script,f'band-{b:02d}-complete'); admitted.append(b); worker_tels.append(tel)
        ex.shutdown(wait=True)
    except BaseException as e:
        _abort(ex); diagnostic(root,'compute',e,branch,sync_script,admitted); raise
    if sorted(admitted)!=sorted(missing): raise RuntimeError('not all missing successor bands durably admitted')
    # Metric is reconstructed from all successor numerical receipts 29..38, making resume deterministic.
    tels=[]
    for b in ALLOWED:
        r=load_band(root,b)
        if r is None: raise RuntimeError(f'band {b} absent after compute')
        tels.append(r)
    starts=[int(t['numerical_start_epoch_ns']) for t in tels]; ends=[int(t['numerical_end_epoch_ns']) for t in tels]; cpus=[float(t['worker_cpu_seconds']) for t in tels]
    active=(max(ends)-min(starts))/1e9; cpu=sum(cpus); eff=cpu/active if active>0 else 0.0; swap1=swap_used_kib()
    seg={'bands_completed':list(ALLOWED),'imported_parent_bands':list(IMPORTED),'compute_active_wall_seconds':active,'sum_worker_numerical_cpu_seconds':cpu,'compute_active_effective_cores':eff,'cpu_fraction_of_8_compute':eff/8.0,'end_to_end_wall_seconds_current_attempt':time.monotonic()-wall0,'swap_used_kib_before_current_attempt':swap0,'swap_used_kib_after_current_attempt':swap1,'swap_increase_kib':max(0,swap1-swap0),'cpu_metric_frozen_to_new_bands_29_38_only':True}
    atomic_json(root/'telemetry'/'resume29_38.json',seg); sync(root,branch,sync_script,'resume29-38-telemetry'); print(json.dumps(seg,sort_keys=True),flush=True)

def finalize(root):
    c=load_contract(root); _,ref=validate_upstream(root); rows=[]
    for b in ALL:
        if load_band(root,b) is None: raise RuntimeError(f'cannot finalize missing band {b}')
        rows.append(exact_array(band_dir(root,b)/'payload.npy',(L,),f'band {b}'))
    target=canon(np.stack(rows)); first8=canon(target[:8]); exact=bool(np.array_equal(first8,ref)) and chash(first8)==REFERENCE_SHA
    t=json.loads((root/'telemetry'/'resume29_38.json').read_text()); cpu=float(t['cpu_fraction_of_8_compute']); swap=int(t['swap_increase_kib']); status=FAIL_EXACT if not exact else FAIL_SWAP if swap>0 else FAIL_CPU if cpu<CPU_MIN else PASS
    rec={'format':c['format'],'experiment':'Exp073CQ','task':'Wm_S3','stage':'final','complete':True,'contract_fingerprint':c['fingerprint'],'target_shape':[39,L],'dtype':'<f8','array_equal_reference_0_7':bool(np.array_equal(first8,ref)),'first8_sha256':chash(first8),'reference_sha256':REFERENCE_SHA,'sha_equal_reference_0_7':chash(first8)==REFERENCE_SHA,'cpu_fraction_of_8_compute':cpu,'cpu_fraction_min':CPU_MIN,'swap_increase_kib':swap,'status':status,'verified_delta':0.0,'draft_data_delta':0.0,'no_tolerance_rescue':True}; atomic_json(root/'final'/'receipt.json',rec); print(json.dumps(rec,indent=2,sort_keys=True),flush=True); return 0 if status==PASS else 42

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('init'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--source-head',required=True); p.add_argument('--driver-commit',required=True)
    p=sp.add_parser('import-parent'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--parent-dir',required=True)
    p=sp.add_parser('validate'); p.add_argument('--checkpoint-dir',required=True)
    p=sp.add_parser('compute'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--ca-so',required=True); p.add_argument('--branch',required=True); p.add_argument('--sync-script',required=True)
    p=sp.add_parser('finalize'); p.add_argument('--checkpoint-dir',required=True)
    a=ap.parse_args(); root=Path(a.checkpoint_dir)
    try:
        if a.cmd=='init': init(root,a.source_head,a.driver_commit)
        elif a.cmd=='import-parent': import_parent(root,Path(a.parent_dir))
        elif a.cmd=='validate': validate(root)
        elif a.cmd=='compute': compute(root,Path(a.ca_so),a.branch,Path(a.sync_script))
        elif a.cmd=='finalize': raise SystemExit(finalize(root))
    except SystemExit: raise
    except BaseException as e:
        if a.cmd!='compute': diagnostic(root,a.cmd,e)
        raise
if __name__=='__main__': main()
