#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, os
from pathlib import Path
import numpy as np

H=1e-4
REL_TOL=1e-3
LOOKUP_REL_TOL=1e-12
NATIVE_KPD=20.0
CAPACITY=4608
MODELS=((0.0,0.0),(-H,0.0),(0.0,H),(0.0,-H))
REQUESTS=(
    ('A',float.fromhex('0x1.3851eb851eb85p-1'),np.asarray([0.0013,0.0047,0.013,0.041],dtype=np.float64)),
    ('B',float.fromhex('0x1.1c28f5c28f5c3p+0'),np.asarray([0.0019,0.0073,0.021,0.057],dtype=np.float64)),
)
JQ_AUTH='docs/dsir4/authority/EXP073JQ_ARTICLE3_SLOT20_SAME_RUN_HISTORY_INDEPENDENCE_V0_1.json'
JL_PREREG_BLOB='0c143dd5b3c1c38b24fbb5b529d03ff9a2afdc58'
JL_IMPL_BLOB='91723736fedd090fa1c81b1fcff4f1f3601d2ce2'
CLASS_COMMIT='ac627d54e9ce196a08878d1ba33999819925d19c'
CANONICAL_4097_SHA='f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb'


def sha(b: bytes)->str: return hashlib.sha256(b).hexdigest()

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def eval_one(jj,c,nodes,z,targets):
    tk=c.get_transfer(z=float(z),output_format='class')
    dm=[q for q in tk if q.strip()=='d_m']
    if len(dm)!=1: raise AssertionError(f'exact d_m key missing: {list(tk)}')
    kkey=None; scale=None
    for q in tk:
        s=q.lower().replace(' ','')
        if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=float(c.h()); break
        if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
    if kkey is None: raise AssertionError('unrecognized CLASS k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale
    y=np.asarray(tk[dm[0]],dtype=np.float64)
    if k.ndim!=1 or y.shape!=k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise AssertionError('invalid transfer table')
    yn,mx=jj.requested_values(k,y,nodes)
    v,valid=jj.cubic_centered(nodes,yn,targets)
    return np.ascontiguousarray(v,dtype='<f8'),np.asarray(valid,dtype=bool),float(mx),kkey

def form_response(vals):
    ref,al,bp,bm=vals
    return np.ascontiguousarray(np.column_stack((np.abs((al-ref)/(-H)),np.abs((bp-bm)/(2*H)))),dtype='<f8')

def reference_four_live(jj,nodes,baseline,precision):
    from classy import Class
    cs=[]
    try:
        for alpha,beta in MODELS:
            c=Class(); c.set(jj.class_params(Path(baseline),Path(precision),alpha,beta,nodes)); c.compute(['transfer']); cs.append(c)
        out={}; max_mx=0.0; unsupported=0; keys=set()
        for label,z,targets in REQUESTS:
            vals=[]; vref=None
            for c in cs:
                v,valid,mx,key=eval_one(jj,c,nodes,z,targets); vals.append(v); keys.add(key); max_mx=max(max_mx,mx)
                if vref is None: vref=valid
                elif not np.array_equal(vref,valid): raise AssertionError('reference model validity mismatch')
            unsupported += int(np.count_nonzero(~vref))
            out[label]=form_response(vals)
        return out,max_mx,unsupported,sorted(keys)
    finally:
        for c in cs:
            try: c.struct_cleanup()
            except Exception: pass

def sequential_one_live(jj,nodes,baseline,precision):
    from classy import Class
    by_request={label:[] for label,_,_ in REQUESTS}; valid_by_request={}; max_mx=0.0; unsupported=0; keys=set()
    for alpha,beta in MODELS:
        c=Class(); c.set(jj.class_params(Path(baseline),Path(precision),alpha,beta,nodes)); c.compute(['transfer'])
        try:
            for label,z,targets in REQUESTS:
                v,valid,mx,key=eval_one(jj,c,nodes,z,targets); by_request[label].append(v); keys.add(key); max_mx=max(max_mx,mx)
                if label not in valid_by_request: valid_by_request[label]=valid
                elif not np.array_equal(valid_by_request[label],valid): raise AssertionError('sequential model validity mismatch')
        finally:
            try: c.struct_cleanup()
            except Exception: pass
    out={}
    for label,_,_ in REQUESTS:
        unsupported += int(np.count_nonzero(~valid_by_request[label]))
        out[label]=form_response(by_request[label])
    return out,max_mx,unsupported,sorted(keys)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--lattice',choices=('coarse','fine'),required=True)
    ap.add_argument('--jj-script',required=True); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True)
    ap.add_argument('--jq-authority',required=True); ap.add_argument('--jl-prereg',required=True); ap.add_argument('--jl-implementation',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    jq=json.loads(Path(a.jq_authority).read_text())
    if jq.get('classification')!='SAME_RUN_HISTORY_INDEPENDENCE_PASS_PLUS_0_PLUS_0' or jq.get('artifact_verified_independently') is not True: raise SystemExit('invalid JQ authority')
    if jq.get('canonical_node_sha256')!=CANONICAL_4097_SHA or jq.get('checkpointed_JL_replay_authorized') is not False: raise SystemExit('JQ authority mismatch')
    if os.popen(f'git hash-object {a.jl_prereg}').read().strip()!=JL_PREREG_BLOB: raise SystemExit('JL prereg blob mismatch')
    if os.popen(f'git hash-object {a.jl_implementation}').read().strip()!=JL_IMPL_BLOB: raise SystemExit('JL implementation blob mismatch')
    jj=load_module('jj_jr',a.jj_script)
    if jj.H!=H or jj.REL_TOL!=REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD or jj.LOOKUP_REL_TOL!=LOOKUP_REL_TOL: raise SystemExit('JJ constants mismatch')
    jj.CAPACITY=CAPACITY
    n=2048 if a.lattice=='coarse' else 4096
    nodes,r,nlo,nhi=jj.guarded_lattice(n)
    expected=2049 if a.lattice=='coarse' else 4097
    if (nlo,nhi,len(nodes))!=(0,1,expected): raise SystemExit('guarded lattice mismatch')
    ref,ref_mx,ref_unsup,ref_keys=reference_four_live(jj,nodes,a.baseline,a.precision)
    seq,seq_mx,seq_unsup,seq_keys=sequential_one_live(jj,nodes,a.baseline,a.precision)
    checks={}; all_exact=True
    for label,_,_ in REQUESTS:
        x=ref[label]; y=seq[label]
        finite_equal=bool(np.array_equal(np.isfinite(x),np.isfinite(y)))
        positive_equal=bool(np.array_equal(x>0,y>0))
        array_equal=bool(np.array_equal(x,y)); byte_equal=sha(x.tobytes())==sha(y.tobytes())
        checks[label]={
          'reference_sha256':sha(x.tobytes()),'sequential_sha256':sha(y.tobytes()),
          'array_equal':array_equal,'byte_sha_equal':byte_equal,'finite_masks_equal':finite_equal,'positive_masks_equal':positive_equal,
          'max_abs_diagnostic':float(np.max(np.abs(x-y))),
          'max_rel_diagnostic':float(np.max(np.divide(np.abs(x-y),np.maximum(np.abs(x),np.abs(y)),out=np.zeros_like(x),where=np.maximum(np.abs(x),np.abs(y))!=0)))
        }
        all_exact = all_exact and array_equal and byte_equal and finite_equal and positive_equal
    valid_support=(ref_unsup==0 and seq_unsup==0 and max(ref_mx,seq_mx)<=LOOKUP_REL_TOL)
    passed=bool(all_exact and valid_support)
    classification='SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0' if passed else 'SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_NOT_EXACT_PLUS_0_PLUS_0'
    out={
      'schema':'EXP073JR_ARTICLE3_LAYERB_SAME_RUN_ATOMIC_ARCHITECTURE_PREFLIGHT_RESULT_V0_1','experiment':'Exp073JR','classification':classification,'effect':'+0/+0',
      'lattice':a.lattice,'base_n':n,'requested_node_count':len(nodes),'guard_counts':[nlo,nhi],'ratio_hex':float(r).hex(),
      'node_payload_sha256':sha(np.ascontiguousarray(nodes,dtype='<f8').tobytes()),'h':H,'rel_tol_lineage_only':REL_TOL,'native_kpd':NATIVE_KPD,'class_commit':CLASS_COMMIT,
      'same_job':True,'same_process':True,'reference_four_instances_live':True,'candidate_max_live_instances':1,
      'reference_max_requested_node_coordinate_rel_mismatch':ref_mx,'sequential_max_requested_node_coordinate_rel_mismatch':seq_mx,
      'reference_unsupported_target_evaluations':ref_unsup,'sequential_unsupported_target_evaluations':seq_unsup,
      'reference_k_keys':ref_keys,'sequential_k_keys':seq_keys,'requests':checks,
      'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'article3_readiness_percent':68,'funnel_freeze_readiness_percent':67,
      'token':'PASS_EXP073JR_'+classification if passed else 'FAIL_EXP073JR_'+classification
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token']); print(json.dumps(out,sort_keys=True)); return 0

if __name__=='__main__': raise SystemExit(main())
