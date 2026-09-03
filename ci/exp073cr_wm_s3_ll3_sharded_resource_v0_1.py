#!/usr/bin/env python3
from __future__ import annotations
import argparse, concurrent.futures as cf, ctypes, hashlib, importlib, json, os, re, shutil, subprocess, time, traceback
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

EXP='Exp073CR'; VER='v0.1'; L=12288; LMAX=12287; BANDS=tuple(range(29,39)); CPU_MIN=.90
EDGES=np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288],dtype=np.int32)
PCL_SHA='ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d'
PARENT_NS='checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2'; PARENT_HEAD='32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0'; PARENT_FP='87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97'; PARENT_STATUS='FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET'
NS='checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-1'
PREREG='ecd6c8fb3723a05deaa982231afef22776567b73'; CAND_COMMIT='d27deaec49f175ac17267fce94bfe2214a02ab6d'; MAN_COMMIT='9fa7566f82ff61ba24e9f94b24d22f1264f0a8a5'; HELPER_COMMIT='bb856b8c49eea804fea73807c3eef53cc20ff3fa'; SYNC_COMMIT='c20127b6762c6fc9b21875a321aecd7a4cd5f88e'; POLICY='f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427'
CAND_SHA='15d8f15ae63cec84052f727c8f826e84aeb582671a95c152c565098c32a2c5b5'; QUEUE_SHA='3ba315d9bc24883ef746d92e785e0a040f9b13e751f59dda9a93e825a6390db4'; SYMBOL='exp073cr_stream_compress_band_ll3_range_v0_1'
THREAD_ENV=('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS')
PASS='PASS_EXP073CR_WM_S3_LL3_SHARDED_8CORE_RESOURCE_V0_1'; FAIL_EXACT='FAIL_EXP073CR_WM_S3_LL3_EXACT_EQUIVALENCE_V0_1'; FAIL_CPU='FAIL_EXP073CR_WM_S3_LL3_CPU_TARGET_V0_1'; FAIL_SWAP='FAIL_EXP073CR_WM_S3_LL3_SWAP_SAFETY_V0_1'

@dataclass(frozen=True,order=True)
class Shard: band:int; lo:int; hi:int

def canon(a): return np.ascontiguousarray(np.asarray(a,dtype='<f8'))
def ahash(a): return hashlib.sha256(memoryview(canon(a)).cast('B')).hexdigest()
def jhash(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def atom(p,o):
 p.parent.mkdir(parents=True,exist_ok=True); q=p.with_suffix(p.suffix+'.tmp'); q.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n'); os.replace(q,p)
def exact_array(p,shape,label):
 a=np.load(p,allow_pickle=False)
 if a.dtype.str!='<f8' or not a.flags.c_contiguous or tuple(a.shape)!=tuple(shape) or not np.all(np.isfinite(a)): raise RuntimeError(f'{label}: noncanonical')
 return a
def exact_commit(x,label):
 x=str(x).lower()
 if not re.fullmatch(r'[0-9a-f]{40}',x): raise RuntimeError(f'{label}: not 40-hex')
 return x

def geometry(cpath,mpath):
 raw=cpath.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=CAND_SHA: raise RuntimeError('candidate SHA mismatch')
 c=json.loads(raw); m=json.loads(mpath.read_text())
 if c.get('status')!='PREREGISTERED_RESOURCE_GATE' or c.get('bands')!=list(BANDS) or c.get('total_shards')!=64 or c.get('outer_workers')!=8 or c.get('nested_threads')!=1: raise RuntimeError('candidate invariants')
 shards=set()
 for b in BANDS:
  bb=list(map(int,c['ll3_boundaries_by_band'][str(b)])); n=int(c['allocation_by_band'][str(b)])
  if len(bb)!=n+1 or bb[0]!=2 or bb[-1]!=L or any(x>=y for x,y in zip(bb[:-1],bb[1:])): raise RuntimeError(f'band {b} geometry')
  shards|={Shard(b,x,y) for x,y in zip(bb[:-1],bb[1:])}
 q=m.get('queue')
 if len(shards)!=64 or not isinstance(q,list) or len(q)!=64: raise RuntimeError('shard cardinality')
 if hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()!=QUEUE_SHA: raise RuntimeError('queue SHA mismatch')
 queue=[Shard(int(x['band']),int(x['ll3_lo']),int(x['ll3_hi'])) for x in q]
 if set(queue)!=shards or len(set(queue))!=64: raise RuntimeError('queue geometry mismatch')
 keys=[(-int(x['proxy_cost']),int(x['band']),int(x['ll3_lo']),int(x['ll3_hi'])) for x in q]
 if keys!=sorted(keys): raise RuntimeError('queue not heavy-first')
 return c,m,queue

def contract(source,driver,workflow,binding):
 d={'format':'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1','experiment':EXP,'version':VER,'task':'Wm_S3','resource_only':True,'scientific_credit':'+0/+0','source_head':exact_commit(source,'source'),'driver_commit':exact_commit(driver,'driver'),'workflow_commit':exact_commit(workflow,'workflow'),'binding_commit':exact_commit(binding,'binding'),'prereg_commit':PREREG,'candidate_commit':CAND_COMMIT,'manifest_commit':MAN_COMMIT,'helper_commit':HELPER_COMMIT,'policy_commit':POLICY,'checkpoint_sync_commit':SYNC_COMMIT,'checkpoint_namespace':NS,'parent_checkpoint_namespace':PARENT_NS,'parent_checkpoint_head':PARENT_HEAD,'parent_contract_fingerprint':PARENT_FP,'bands':list(BANDS),'source_bin':3,'signature':[0,2,0,2],'lmax':LMAX,'row_length':L,'candidate_sha256':CAND_SHA,'heavy_first_queue_sha256':QUEUE_SHA,'helper_symbol':SYMBOL,'outer_workers':8,'max_inflight_futures':8,'nested_threads':1,'pcl_sha256':PCL_SHA,'dtype':'<f8','cpu_fraction_min':CPU_MIN,'swap_increase_kib_max':0,'cpu_metric':'sum_64_worker_cpu_seconds_div_earliest_to_latest_64_shard_numerical_start_end','checkpoint_boundary':'hosted_seed_or_swap_baseline_or_complete_shard_or_diagnostic_or_telemetry_or_final_only','durability_before_refill':True,'exact_complete_band_reference_required':True,'no_tolerance_rescue':True,'verified_delta':0.0,'draft_data_delta':0.0}
 d['fingerprint']=jhash(d); return d
def load_contract(root):
 c=json.loads((root/'contract.json').read_text()); fp=c.get('fingerprint'); x=dict(c); x.pop('fingerprint',None)
 if fp!=jhash(x) or c.get('experiment')!=EXP or c.get('checkpoint_namespace')!=NS: raise RuntimeError('contract mismatch')
 return c

def validate_parent(parent):
 pc=json.loads((parent/'contract.json').read_text()); fp=pc.get('fingerprint'); x=dict(pc); x.pop('fingerprint',None)
 if fp!=jhash(x) or fp!=PARENT_FP or pc.get('checkpoint_namespace')!=PARENT_NS: raise RuntimeError('CQ parent contract')
 fr=json.loads((parent/'final/receipt.json').read_text())
 if fr.get('complete') is not True or fr.get('contract_fingerprint')!=PARENT_FP or fr.get('status')!=PARENT_STATUS or fr.get('array_equal_reference_0_7') is not True or fr.get('sha_equal_reference_0_7') is not True or int(fr.get('swap_increase_kib',-1))!=0: raise RuntimeError('CQ parent terminal receipt')
 pcl=exact_array(parent/'upstream/pcl.npy',(L,),'parent PCL')
 if ahash(pcl)!=PCL_SHA: raise RuntimeError('parent PCL SHA')
 refs={}
 for b in BANDS:
  d=parent/'bands'/f'band_{b:02d}'; r=json.loads((d/'receipt.json').read_text()); a=exact_array(d/'payload.npy',(L,),f'parent band {b}')
  if r.get('complete') is not True or r.get('contract_fingerprint')!=PARENT_FP or r.get('band')!=b or r.get('payload_sha256')!=ahash(a): raise RuntimeError(f'parent band {b}')
  refs[b]=a
 return pcl,refs

def init_seed(root,parent,source,driver,workflow,binding):
 if root.exists() and any(root.iterdir()): raise RuntimeError('seed root not empty')
 pcl,refs=validate_parent(parent); root.mkdir(parents=True,exist_ok=True); c=contract(source,driver,workflow,binding); atom(root/'contract.json',c)
 (root/'upstream').mkdir(); np.save(root/'upstream/pcl.npy',canon(pcl),allow_pickle=False); atom(root/'upstream/receipt.json',{'complete':True,'contract_fingerprint':c['fingerprint'],'origin':'hosted_exact_seed_from_exp073cq_v0_2_terminal','parent_head':PARENT_HEAD,'pcl_sha256':PCL_SHA,'dtype':'<f8'})
 for b,a in refs.items():
  d=root/'references'/f'band_{b:02d}'; d.mkdir(parents=True); np.save(d/'payload.npy',canon(a),allow_pickle=False); atom(d/'receipt.json',{'complete':True,'contract_fingerprint':c['fingerprint'],'origin':'hosted_exact_reference_from_exp073cq_v0_2_terminal','parent_head':PARENT_HEAD,'band':b,'shape':[L],'dtype':'<f8','payload_sha256':ahash(a)})
 atom(root/'seed/receipt.json',{'complete':True,'contract_fingerprint':c['fingerprint'],'parent_head':PARENT_HEAD,'reference_bands':list(BANDS),'pcl_sha256':PCL_SHA})
 validate_seed(root); print(c['fingerprint'])
def validate_seed(root):
 c=load_contract(root); ur=json.loads((root/'upstream/receipt.json').read_text()); pcl=exact_array(root/'upstream/pcl.npy',(L,),'seed PCL')
 if ur.get('complete') is not True or ur.get('contract_fingerprint')!=c['fingerprint'] or ahash(pcl)!=PCL_SHA: raise RuntimeError('seed upstream')
 for b in BANDS:
  d=root/'references'/f'band_{b:02d}'; r=json.loads((d/'receipt.json').read_text()); a=exact_array(d/'payload.npy',(L,),f'seed ref {b}')
  if r.get('complete') is not True or r.get('contract_fingerprint')!=c['fingerprint'] or r.get('band')!=b or r.get('payload_sha256')!=ahash(a): raise RuntimeError(f'seed ref {b}')
 sr=json.loads((root/'seed/receipt.json').read_text())
 if sr.get('complete') is not True or sr.get('contract_fingerprint')!=c['fingerprint'] or sr.get('reference_bands')!=list(BANDS): raise RuntimeError('seed receipt')
 return c

def bind_helper(p):
 lib=ctypes.CDLL(str(p.resolve()))
 try: f=getattr(lib,SYMBOL)
 except AttributeError as e: raise RuntimeError('helper ABI symbol absent') from e
 dp=ctypes.POINTER(ctypes.c_double); ip=ctypes.POINTER(ctypes.c_int)
 f.argtypes=[ctypes.c_char_p,dp,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ip,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,dp]; f.restype=ctypes.c_int
 return f,dp,ip
def nmtlib(): return str(Path(importlib.import_module('_nmtlib').__file__).resolve()).encode()
def sdir(root,s): return root/'shards'/f'band_{s.band:02d}'/f'll3_{s.lo:05d}_{s.hi:05d}'
def load_shard(root,s):
 d=sdir(root,s); rp=d/'receipt.json'
 if not rp.exists(): return None
 c=load_contract(root); r=json.loads(rp.read_text()); a=exact_array(d/'payload.npy',(s.hi-s.lo,),f'shard {s}')
 want={'complete':True,'contract_fingerprint':c['fingerprint'],'band':s.band,'ll3_interval':[s.lo,s.hi],'candidate_sha256':CAND_SHA,'queue_sha256':QUEUE_SHA,'helper_symbol':SYMBOL,'payload_sha256':ahash(a)}
 if any(r.get(k)!=v for k,v in want.items()): raise RuntimeError(f'shard receipt mismatch {s}')
 return r
def store_shard(root,s,a,tel):
 c=load_contract(root); a=canon(a)
 if tuple(a.shape)!=(s.hi-s.lo,) or not np.all(np.isfinite(a)): raise RuntimeError('invalid shard payload')
 d=sdir(root,s); d.mkdir(parents=True,exist_ok=True); np.save(d/'payload.npy',a,allow_pickle=False); atom(d/'receipt.json',{'complete':True,'contract_fingerprint':c['fingerprint'],'origin':'new_numerical_exp073cr','band':s.band,'ll3_interval':[s.lo,s.hi],'shape':[s.hi-s.lo],'dtype':'<f8','payload_sha256':ahash(a),'candidate_sha256':CAND_SHA,'queue_sha256':QUEUE_SHA,'helper_symbol':SYMBOL,'outer_workers':8,'nested_threads':1,**tel})
def sync(root,branch,script,label):
 p=subprocess.run(['bash',str(script),'push',str(root),branch,label],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 if p.stdout: print(p.stdout,end='' if p.stdout.endswith('\n') else '\n',flush=True)
 if p.returncode: raise subprocess.CalledProcessError(p.returncode,p.args,output=p.stdout)
def swap_used():
 p=Path('/proc/meminfo')
 if not p.is_file(): raise RuntimeError('/proc/meminfo unavailable')
 total=free=None
 for ln in p.read_text().splitlines():
  if ln.startswith('SwapTotal:'): total=int(ln.split()[1])
  if ln.startswith('SwapFree:'): free=int(ln.split()[1])
 if total is None or free is None or total<0 or free<0 or free>total: raise RuntimeError('invalid swap telemetry')
 return total-free
def cpus():
 try: return len(os.sched_getaffinity(0))
 except Exception: return os.cpu_count() or 0

_W=[None]*6
def init_worker(pcl_path,helper_path):
 global _W
 for k in THREAD_ENV:
  if os.environ.get(k)!='1': raise RuntimeError(f'thread pin {k}')
 if os.environ.get('OMP_DYNAMIC','').upper()!='FALSE': raise RuntimeError('OMP_DYNAMIC')
 pcl=exact_array(Path(pcl_path),(L,),'worker PCL'); f,dp,ip=bind_helper(Path(helper_path)); _W=[pcl,f,dp,ip,nmtlib(),np.ascontiguousarray(EDGES,dtype=np.int32)]
def worker(s):
 pcl,f,dp,ip,nm,ed=_W; out=np.zeros(s.hi-s.lo,dtype=np.float64); st=time.time_ns(); t=time.monotonic(); c=time.process_time(); rc=f(nm,pcl.ctypes.data_as(dp),LMAX,0,2,0,2,ed.ctypes.data_as(ip),len(ed)-1,s.band,s.lo,s.hi,1,out.ctypes.data_as(dp)); en=time.time_ns()
 if rc: raise RuntimeError(f'helper rc={rc} {s}')
 return s,canon(out),{'numerical_start_epoch_ns':st,'numerical_end_epoch_ns':en,'worker_wall_seconds':time.monotonic()-t,'worker_cpu_seconds':time.process_time()-c}
def abort(ex):
 ps=list(getattr(ex,'_processes',{}).values())
 try: ex.shutdown(wait=False,cancel_futures=True)
 except Exception: pass
 for p in ps:
  try:
   if p.is_alive(): p.terminate()
  except Exception: pass

def diagnostic(root,e,queue,branch,script):
 durable=[]
 for s in queue:
  try:
   if load_shard(root,s): durable.append([s.band,s.lo,s.hi])
  except Exception: pass
 atom(root/'diagnostics/first_failure.json',{'complete':True,'experiment':EXP,'version':VER,'stage':'compute','contract_fingerprint':load_contract(root)['fingerprint'],'exception_type':type(e).__name__,'exception_string':str(e),'traceback':''.join(traceback.format_exception(type(e),e,e.__traceback__))[-12000:],'durable_shards':durable,'durable_count':len(durable),'timestamp_utc':datetime.now(timezone.utc).isoformat()})
 try: sync(root,branch,script,'diagnostic-first-failure')
 except Exception as de: print('DIAGNOSTIC_SYNC_FAILED',de,flush=True)

def compute(root,cpath,mpath,helper,branch,script):
 validate_seed(root); _,_,queue=geometry(cpath,mpath)
 if cpus()!=8: raise RuntimeError(f'visible CPU count must equal 8, got {cpus()}')
 for k in THREAD_ENV:
  if os.environ.get(k)!='1': raise RuntimeError(f'coordinator thread pin {k}')
 if os.environ.get('OMP_DYNAMIC','').upper()!='FALSE': raise RuntimeError('OMP_DYNAMIC')
 bind_helper(helper); base=root/'telemetry/swap_baseline.json'
 if not base.exists(): atom(base,{'complete':True,'contract_fingerprint':load_contract(root)['fingerprint'],'swap_used_kib_before_resource_gate':swap_used(),'timestamp_ns':time.time_ns()}); sync(root,branch,script,'swap-baseline')
 br=json.loads(base.read_text())
 if br.get('complete') is not True or br.get('contract_fingerprint')!=load_contract(root)['fingerprint'] or not isinstance(br.get('swap_used_kib_before_resource_gate'),int): raise RuntimeError('swap baseline receipt')
 missing=[s for s in queue if load_shard(root,s) is None]
 if not missing: print('all 64 shards durable'); return
 ex=cf.ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(str(root/'upstream/pcl.npy'),str(helper))); it=iter(missing); futs={}; rank={s:i for i,s in enumerate(queue)}
 try:
  for _ in range(min(8,len(missing))): s=next(it); futs[ex.submit(worker,s)]=s
  while futs:
   done,_=cf.wait(tuple(futs),return_when=cf.FIRST_COMPLETED)
   for fut in sorted(done,key=lambda f:rank[futs[f]]):
    exp=futs.pop(fut); got,a,tel=fut.result()
    if got!=exp: raise RuntimeError('worker identity')
    store_shard(root,got,a,tel); sync(root,branch,script,f'shard-b{got.band:02d}-l{got.lo:05d}-{got.hi:05d}')
    try: nxt=next(it); futs[ex.submit(worker,nxt)]=nxt
    except StopIteration: pass
  ex.shutdown(wait=True)
 except BaseException as e: abort(ex); diagnostic(root,e,queue,branch,script); raise

def assemble(root,queue,b):
 ss=sorted([s for s in queue if s.band==b],key=lambda s:s.lo); out=np.zeros(L,dtype='<f8'); cov=np.zeros(L,dtype=np.uint8)
 for s in ss:
  if load_shard(root,s) is None: raise RuntimeError(f'missing {s}')
  a=exact_array(sdir(root,s)/'payload.npy',(s.hi-s.lo,),f'assemble {s}');
  if np.any(cov[s.lo:s.hi]): raise RuntimeError('overlap')
  out[s.lo:s.hi]=a; cov[s.lo:s.hi]=1
 if np.any(cov[:2]) or np.any(cov[2:]!=1) or out[0]!=0 or out[1]!=0 or not np.all(np.isfinite(out)): raise RuntimeError(f'coverage/invariant band {b}')
 return canon(out)
def finalize(root,cpath,mpath):
 c=validate_seed(root); _,_,queue=geometry(cpath,mpath); rs=[load_shard(root,s) for s in queue]
 if any(r is None for r in rs): raise RuntimeError('not all 64 shards durable')
 exact=True; rows=[]
 for b in BANDS:
  a=assemble(root,queue,b); ref=exact_array(root/'references'/f'band_{b:02d}/payload.npy',(L,),f'ref {b}'); eq=bool(np.array_equal(a,ref)); se=ahash(a)==ahash(ref); exact &= eq and se; rows.append({'band':b,'array_equal':eq,'sha_equal':se,'candidate_sha256':ahash(a),'reference_sha256':ahash(ref)})
 active=(max(int(r['numerical_end_epoch_ns']) for r in rs)-min(int(r['numerical_start_epoch_ns']) for r in rs))/1e9; cpu=sum(float(r['worker_cpu_seconds']) for r in rs); eff=cpu/active if active>0 else 0.; frac=eff/8.
 br=json.loads((root/'telemetry/swap_baseline.json').read_text())
 if br.get('complete') is not True or br.get('contract_fingerprint')!=c['fingerprint'] or not isinstance(br.get('swap_used_kib_before_resource_gate'),int): raise RuntimeError('final swap baseline')
 swap1=swap_used(); inc=max(0,swap1-br['swap_used_kib_before_resource_gate']); status,rc=(FAIL_EXACT,41) if not exact else ((FAIL_SWAP,43) if inc>0 else ((FAIL_CPU,42) if frac<CPU_MIN else (PASS,0)))
 tel={'complete':True,'contract_fingerprint':c['fingerprint'],'shard_count':64,'compute_active_wall_seconds':active,'sum_worker_numerical_cpu_seconds':cpu,'compute_active_effective_cores':eff,'cpu_fraction_of_8_compute':frac,'cpu_fraction_min':CPU_MIN,'swap_used_kib_before_resource_gate':br['swap_used_kib_before_resource_gate'],'swap_used_kib_after_resource_gate':swap1,'swap_increase_kib':inc}; atom(root/'telemetry/final.json',tel)
 rec={'format':c['format'],'experiment':EXP,'version':VER,'task':'Wm_S3','stage':'final','complete':True,'contract_fingerprint':c['fingerprint'],'status':status,'resource_only':True,'scientific_credit':'+0/+0','candidate_sha256':CAND_SHA,'queue_sha256':QUEUE_SHA,'exact_all_bands_29_38':bool(exact),'per_band_exact':rows,'cpu_fraction_of_8_compute':frac,'cpu_fraction_min':CPU_MIN,'swap_increase_kib':inc,'no_tolerance_rescue':True,'verified_delta':0.0,'draft_data_delta':0.0}; atom(root/'final/receipt.json',rec); print(json.dumps(rec,sort_keys=True,indent=2)); return rc

def regression(parent,helper):
 pcl,_=validate_parent(parent); f,dp,ip=bind_helper(helper); nm=nmtlib(); ed=np.ascontiguousarray(EDGES,dtype=np.int32); parts=((2,3072,6144,9216,L),(2,1024,4097,7777,10000,L))
 for b in (0,7,15):
  d=parent/'bands'/f'band_{b:02d}'; r=json.loads((d/'receipt.json').read_text()); ref=exact_array(d/'payload.npy',(L,),f'control {b}')
  if r.get('complete') is not True or r.get('contract_fingerprint')!=PARENT_FP or r.get('payload_sha256')!=ahash(ref): raise RuntimeError(f'control parent {b}')
  for part in parts:
   out=np.zeros(L,dtype='<f8')
   for lo,hi in zip(part[:-1],part[1:]):
    z=np.zeros(hi-lo,dtype=np.float64); rc=f(nm,pcl.ctypes.data_as(dp),LMAX,0,2,0,2,ed.ctypes.data_as(ip),len(ed)-1,b,lo,hi,1,z.ctypes.data_as(dp));
    if rc: raise RuntimeError(f'regression rc={rc}')
    out[lo:hi]=z
   eq=bool(np.array_equal(out,ref)); se=ahash(out)==ahash(ref); finite=bool(np.all(np.isfinite(out))); print(json.dumps({'band':b,'partition':list(part),'array_equal':eq,'sha_equal':se,'finite':finite,'candidate_sha256':ahash(out),'reference_sha256':ahash(ref)},sort_keys=True))
   if not(eq and se and finite): raise RuntimeError('authoritative bitwise regression fail')
 print('PASS_EXP073CR_HOSTED_AUTHORITATIVE_LL3_BITWISE_REGRESSION_V0_1')

def main():
 ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
 p=sp.add_parser('validate-geometry'); p.add_argument('--candidate',required=True); p.add_argument('--manifest',required=True)
 p=sp.add_parser('init-seed'); p.add_argument('--root',required=True); p.add_argument('--parent-dir',required=True); p.add_argument('--source-head',required=True); p.add_argument('--driver-commit',required=True); p.add_argument('--workflow-commit',required=True); p.add_argument('--binding-commit',required=True)
 p=sp.add_parser('validate-seed'); p.add_argument('--root',required=True)
 p=sp.add_parser('compute'); p.add_argument('--root',required=True); p.add_argument('--candidate',required=True); p.add_argument('--manifest',required=True); p.add_argument('--helper',required=True); p.add_argument('--branch',required=True); p.add_argument('--sync-script',required=True)
 p=sp.add_parser('finalize'); p.add_argument('--root',required=True); p.add_argument('--candidate',required=True); p.add_argument('--manifest',required=True)
 p=sp.add_parser('regression'); p.add_argument('--parent-dir',required=True); p.add_argument('--helper',required=True)
 a=ap.parse_args()
 if a.cmd=='validate-geometry': c,m,q=geometry(Path(a.candidate),Path(a.manifest)); print(json.dumps({'candidate_sha256':CAND_SHA,'queue_sha256':QUEUE_SHA,'shards':len(q),'bands':c['bands']},sort_keys=True))
 elif a.cmd=='init-seed': init_seed(Path(a.root),Path(a.parent_dir),a.source_head,a.driver_commit,a.workflow_commit,a.binding_commit)
 elif a.cmd=='validate-seed': validate_seed(Path(a.root)); print('PASS_EXP073CR_SEED_VALIDATE_V0_1')
 elif a.cmd=='compute': compute(Path(a.root),Path(a.candidate),Path(a.manifest),Path(a.helper),a.branch,Path(a.sync_script))
 elif a.cmd=='finalize': raise SystemExit(finalize(Path(a.root),Path(a.candidate),Path(a.manifest)))
 elif a.cmd=='regression': regression(Path(a.parent_dir),Path(a.helper))
if __name__=='__main__': main()
