#!/usr/bin/env python3
from __future__ import annotations
import argparse, concurrent.futures as cf, json, time
from pathlib import Path
import exp073co_wm_s3_full39_checkpoint_resource_v0_1 as co

PREREG_COMMIT='451e947d44b325b1089441a0a62c24b1dcdeba5e'
SYNC_COMMIT='c20127b6762c6fc9b21875a321aecd7a4cd5f88e'
NAMESPACE='checkpoints/exp073cp-wm-s3-full39-resource-v0-1'
PASS='PASS_EXP073CP_WM_S3_FULL39_8WORKER_TRANSPORT_HARDENED_RESOURCE_V0_1'
FAIL_EXACT='FAIL_EXP073CP_WM_S3_FULL39_EXACT_EQUIVALENCE_V0_1'; FAIL_SWAP='FAIL_EXP073CP_WM_S3_FULL39_SWAP_SAFETY_V0_1'; FAIL_CPU='FAIL_EXP073CP_WM_S3_FULL39_CPU_TARGET_V0_1'
co.PREREG_COMMIT=PREREG_COMMIT; co.SYNC_COMMIT=SYNC_COMMIT; co.PASS=PASS; co.FAIL_EXACT=FAIL_EXACT; co.FAIL_SWAP=FAIL_SWAP; co.FAIL_CPU=FAIL_CPU

def contract(source_head:str,driver_commit:str):
    d=co.contract(source_head,driver_commit); d.pop('fingerprint',None)
    d.update({'experiment':'Exp073CP','version':'v0.1','prereg_commit':PREREG_COMMIT,'checkpoint_sync_commit':SYNC_COMMIT,
              'checkpoint_namespace':NAMESPACE,'transport_contract':'bounded_retry_timeout_http1.1_exact_head_v0.3',
              'scheduler_contract':'max8_inflight_refill_before_durability_bounded_abort'})
    d['fingerprint']=co.jhash(d); return d

def import_upstream(root:Path,cm:Path):
    c=co.load_contract(root); pcl,ref=co.cn.validate_cm(cm); d=root/'upstream'; d.mkdir(parents=True,exist_ok=True)
    co.np.save(d/'pcl.npy',co.canon(pcl),allow_pickle=False); co.np.save(d/'reference_0_7.npy',co.canon(ref),allow_pickle=False)
    co.atomic_json(d/'receipt.json',{'format':c['format'],'experiment':'Exp073CP','stage':'upstream','complete':True,'contract_fingerprint':c['fingerprint'],'upstream_cm_head':co.UPSTREAM_CM_HEAD,'upstream_cm_contract_fingerprint':co.UPSTREAM_CM_FINGERPRINT,'pcl_sha256':co.chash(pcl),'reference_sha256':co.chash(ref),'dtype':'<f8'})

def store_band(root:Path,b:int,a,tel:dict):
    c=co.load_contract(root); d=co.band_dir(root,b); d.mkdir(parents=True,exist_ok=True); a=co.canon(a); co.np.save(d/'payload.npy',a,allow_pickle=False)
    r={'format':c['format'],'experiment':'Exp073CP','task':'Wm_S3','stage':'band','complete':True,'contract_fingerprint':c['fingerprint'],'band':b,'ell_interval':[int(co.EDGES[b]),int(co.EDGES[b+1])],'shape':[co.L],'dtype':'<f8','payload_sha256':co.chash(a),'pcl_sha256':co.PCL_SHA,'outer_workers':8,'nested_threads':1,**tel}; co.atomic_json(d/'receipt.json',r); return r

def _abort(ex):
    for f in list(getattr(ex,'_pending_work_items',{}).values()):
        try: f.future.cancel()
        except Exception: pass
    for p in list(getattr(ex,'_processes',{}).values()):
        try: p.terminate()
        except Exception: pass
    ex.shutdown(wait=False,cancel_futures=True)

def compute(root:Path,ca_so:Path,branch:str,sync_script:Path):
    co.validate_upstream(root)
    for b in co.BANDS: co.load_band(root,b)
    missing=[b for b in co.BANDS if co.load_band(root,b) is None]
    if not missing: print('all bands already checkpointed; no compute',flush=True); return
    swap0=co.swap_used_kib(); wall0=time.monotonic(); transport=0.0; worker_tels=[]; admitted=[]; pending=iter(missing); ex=cf.ProcessPoolExecutor(max_workers=8); futs={}
    try:
        for _ in range(min(8,len(missing))):
            b=next(pending); futs[ex.submit(co.timed_worker,b,str(root/'upstream/pcl.npy'),str(ca_so))]=b
        while futs:
            done,_=cf.wait(tuple(futs),return_when=cf.FIRST_COMPLETED)
            for fut in done:
                b=futs.pop(fut); b2,a,tel=fut.result(); assert b2==b
                store_band(root,b,a,tel)
                # Refill before durability postcheck, but never exceed 8 in-flight numerical units.
                try:
                    nb=next(pending); futs[ex.submit(co.timed_worker,nb,str(root/'upstream/pcl.npy'),str(ca_so))]=nb
                except StopIteration: pass
                transport += co.sync(root,branch,sync_script,f'band-{b:02d}-complete')
                worker_tels.append(tel); admitted.append(b)
        ex.shutdown(wait=True)
    except BaseException:
        _abort(ex); raise
    wall=time.monotonic()-wall0; swap1=co.swap_used_kib()
    if sorted(admitted)!=sorted(missing): raise RuntimeError('not all missing bands durably admitted')
    starts=[int(t['numerical_start_epoch_ns']) for t in worker_tels]; ends=[int(t['numerical_end_epoch_ns']) for t in worker_tels]; cpus=[float(t['worker_cpu_seconds']) for t in worker_tels]
    active_span=(max(ends)-min(starts))/1e9; cpu_sum=sum(cpus); eff=cpu_sum/active_span if active_span>0 else 0.0
    seg={'bands_completed':sorted(admitted),'compute_active_wall_seconds':active_span,'sum_worker_numerical_cpu_seconds':cpu_sum,'compute_active_effective_cores':eff,'cpu_fraction_of_8_compute':eff/8.0,'end_to_end_wall_seconds':wall,'checkpoint_transport_wall_seconds':transport,'checkpoint_push_count':len(admitted),'swap_used_kib_before':swap0,'swap_used_kib_after':swap1,'swap_increase_kib':max(0,swap1-swap0)}
    co.atomic_json(root/'telemetry'/'full39.json',seg); co.sync(root,branch,sync_script,'full39-telemetry'); print(json.dumps(seg,sort_keys=True),flush=True)

def finalize(root:Path):
    c=co.load_contract(root); _,ref=co.validate_upstream(root); rows=[]
    for b in co.BANDS: co.load_band(root,b); rows.append(co.exact_array(co.band_dir(root,b)/'payload.npy',(co.L,),f'band {b}'))
    target=co.canon(co.np.stack(rows)); first8=co.canon(target[:8]); exact=bool(co.np.array_equal(first8,ref)) and co.chash(first8)==co.REFERENCE_SHA
    t=json.loads((root/'telemetry'/'full39.json').read_text()); cpu=float(t['cpu_fraction_of_8_compute']); swap=int(t['swap_increase_kib']); status=FAIL_EXACT if not exact else FAIL_SWAP if swap>0 else FAIL_CPU if cpu<co.CPU_FRACTION_MIN else PASS
    rec={'format':c['format'],'experiment':'Exp073CP','task':'Wm_S3','stage':'final','complete':True,'contract_fingerprint':c['fingerprint'],'target_shape':[39,co.L],'dtype':'<f8','array_equal_reference_0_7':bool(co.np.array_equal(first8,ref)),'first8_sha256':co.chash(first8),'reference_sha256':co.REFERENCE_SHA,'sha_equal_reference_0_7':co.chash(first8)==co.REFERENCE_SHA,'cpu_fraction_of_8_compute':cpu,'cpu_fraction_min':co.CPU_FRACTION_MIN,'swap_increase_kib':swap,'status':status,'verified_delta':0.0,'draft_data_delta':0.0,'no_tolerance_rescue':True}; co.atomic_json(root/'final'/'receipt.json',rec); print(json.dumps(rec,indent=2,sort_keys=True),flush=True); return 0 if status==PASS else 42

co.contract=contract; co.import_upstream=import_upstream; co.store_band=store_band

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('init'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--source-head',required=True); p.add_argument('--driver-commit',required=True)
    p=sp.add_parser('import-upstream'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--cm-dir',required=True)
    p=sp.add_parser('validate'); p.add_argument('--checkpoint-dir',required=True)
    p=sp.add_parser('compute'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--ca-so',required=True); p.add_argument('--branch',required=True); p.add_argument('--sync-script',required=True)
    p=sp.add_parser('finalize'); p.add_argument('--checkpoint-dir',required=True)
    a=ap.parse_args(); root=Path(a.checkpoint_dir)
    if a.cmd=='init': co.init(root,a.source_head,a.driver_commit)
    elif a.cmd=='import-upstream': import_upstream(root,Path(a.cm_dir))
    elif a.cmd=='validate': raise SystemExit(co.validate(root))
    elif a.cmd=='compute': compute(root,Path(a.ca_so),a.branch,Path(a.sync_script))
    elif a.cmd=='finalize': raise SystemExit(finalize(root))
if __name__=='__main__': main()
