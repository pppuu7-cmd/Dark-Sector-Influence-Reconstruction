#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os
from pathlib import Path
import numpy as np

H=1e-4
REL_TOL=1e-3
NATIVE_KPD=20.0
BASE_N=4096
CAPACITY=4608
EXPECTED_NODE_COUNT=4097
CANONICAL_NODE_SHA='f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb'
CANONICAL_HEX_SHA='98cd360d0764a884471cb09b4504b79583e2ffaea4423389ec473e98b8656c2a'
CLASS_COMMIT='ac627d54e9ce196a08878d1ba33999819925d19c'
MODELS={
 'reference':(0.0,0.0),
 'alpha_minus':(-H,0.0),
 'beta_plus':(0.0,H),
 'beta_minus':(0.0,-H),
}
PRE_Z=float.fromhex('0x1.3851eb851eb85p-1')
TAIL_Z=float.fromhex('0x1.1c28f5c28f5c3p+0')
PRE_TARGETS=np.asarray([0.0013,0.0047,0.013,0.041],dtype=np.float64)
TAIL_TARGETS=np.asarray([0.0019,0.0073,0.021,0.057],dtype=np.float64)


def sha(b: bytes)->str: return hashlib.sha256(b).hexdigest()

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def load_nodes(bin_path,hex_path,authority_path):
    raw=Path(bin_path).read_bytes(); hx=Path(hex_path).read_bytes(); auth=json.loads(Path(authority_path).read_text())
    if sha(raw)!=CANONICAL_NODE_SHA or sha(hx)!=CANONICAL_HEX_SHA: raise SystemExit('canonical SHA mismatch')
    if auth.get('node_payload_sha256')!=CANONICAL_NODE_SHA or auth.get('node_hex_sha256')!=CANONICAL_HEX_SHA: raise SystemExit('canonical authority mismatch')
    a=np.frombuffer(raw,dtype='<f8').copy(); b=np.asarray([float.fromhex(x) for x in hx.decode().splitlines()],dtype='<f8')
    if len(a)!=EXPECTED_NODE_COUNT or not np.array_equal(a,b): raise SystemExit('canonical roundtrip mismatch')
    if np.any(~np.isfinite(a)) or np.any(a<=0) or np.any(np.diff(a)<=0): raise SystemExit('canonical validity mismatch')
    return a

def evaluate(jj,c,nodes,z,targets):
    tk=c.get_transfer(z=float(z),output_format='class')
    dm=[q for q in tk if q.strip()=='d_m']
    if len(dm)!=1: raise AssertionError(f'exact d_m key missing: {list(tk)}')
    kkey=None; scale=None
    for q in tk:
        s=q.lower().replace(' ','')
        if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=float(c.h()); break
        if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
    if kkey is None: raise AssertionError('unrecognized CLASS k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
    if k.ndim!=1 or y.shape!=k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise AssertionError('invalid transfer table')
    yn,mx=jj.requested_values(k,y,nodes); v,valid=jj.cubic_centered(nodes,yn,targets)
    if not bool(np.all(valid)): raise AssertionError('unsupported frozen target')
    return np.ascontiguousarray(v,dtype='<f8'),float(mx),kkey

def run_instance(jj,Class,nodes,baseline,precision,alpha,beta,with_history):
    c=Class(); c.set(jj.class_params(Path(baseline),Path(precision),alpha,beta,nodes)); c.compute(['transfer'])
    try:
        pre_mx=None
        if with_history: _,pre_mx,_=evaluate(jj,c,nodes,PRE_Z,PRE_TARGETS)
        tail,tail_mx,kkey=evaluate(jj,c,nodes,TAIL_Z,TAIL_TARGETS)
        return tail,pre_mx,tail_mx,kkey
    finally:
        try: c.struct_cleanup()
        except Exception: pass

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--model',choices=tuple(MODELS),required=True)
    ap.add_argument('--jj-script',required=True); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True)
    ap.add_argument('--canonical-bin',required=True); ap.add_argument('--canonical-hex',required=True); ap.add_argument('--canonical-authority',required=True)
    ap.add_argument('--out-dir',required=True)
    a=ap.parse_args(); jj=load_module('jj_jq',a.jj_script)
    if jj.H!=H or jj.REL_TOL!=REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD: raise SystemExit('frozen JJ constants mismatch')
    jj.CAPACITY=CAPACITY; nodes=load_nodes(a.canonical_bin,a.canonical_hex,a.canonical_authority)
    if nodes[0]!=np.float64(jj.KMIN) or nodes[BASE_N-1]!=np.float64(jj.KMAX): raise SystemExit('canonical endpoint mismatch')
    alpha,beta=MODELS[a.model]
    from classy import Class
    # Frozen order: fresh_A -> after_history -> fresh_B.
    fresh_a,_,mx_a,k_a=run_instance(jj,Class,nodes,a.baseline,a.precision,alpha,beta,False)
    history,mx_pre,mx_h,k_h=run_instance(jj,Class,nodes,a.baseline,a.precision,alpha,beta,True)
    fresh_b,_,mx_b,k_b=run_instance(jj,Class,nodes,a.baseline,a.precision,alpha,beta,False)
    exact_fresh=bool(np.array_equal(fresh_a,fresh_b))
    exact_history_a=bool(np.array_equal(fresh_a,history))
    exact_history_b=bool(np.array_equal(fresh_b,history))
    if not exact_fresh:
        cls='SAME_RUN_FRESH_REEXECUTION_NOT_EXACT_PLUS_0_PLUS_0'
    elif not (exact_history_a and exact_history_b):
        cls='SAME_RUN_HISTORY_DEPENDENCE_CONFIRMED_PLUS_0_PLUS_0'
    else:
        cls='SAME_RUN_HISTORY_INDEPENDENCE_PASS_PLUS_0_PLUS_0'
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    payloads={'fresh_A':fresh_a,'after_history':history,'fresh_B':fresh_b}
    for name,v in payloads.items(): (out/f'{name}.f64').write_bytes(v.tobytes(order='C'))
    def maxdiff(x,y):
        ad=np.abs(x-y); den=np.maximum(np.abs(x),np.abs(y)); rel=np.divide(ad,den,out=np.zeros_like(ad),where=den!=0)
        return float(np.max(ad)),float(np.max(rel))
    fa_fb=maxdiff(fresh_a,fresh_b); fa_h=maxdiff(fresh_a,history)
    result={
      'schema':'EXP073JQ_SLOT20_SAME_RUN_CAUSAL_DISCRIMINATION_RESULT_V0_1','experiment':'Exp073JQ','model':a.model,'classification':cls,'effect':'+0/+0',
      'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,
      'alpha_hex':float(alpha).hex(),'beta_hex':float(beta).hex(),'h':H,'rel_tol_lineage_only':REL_TOL,'native_kpd':NATIVE_KPD,'class_commit':CLASS_COMMIT,
      'canonical_node_sha256':CANONICAL_NODE_SHA,'canonical_hex_sha256':CANONICAL_HEX_SHA,'requested_node_count':len(nodes),
      'execution_order':['fresh_A','after_history','fresh_B'],'same_job':True,'runner_name':os.environ.get('RUNNER_NAME'),'runner_os':os.environ.get('RUNNER_OS'),'runner_arch':os.environ.get('RUNNER_ARCH'),
      'pre_z_hex':PRE_Z.hex(),'tail_z_hex':TAIL_Z.hex(),'pre_targets_hex':[float(x).hex() for x in PRE_TARGETS],'tail_targets_hex':[float(x).hex() for x in TAIL_TARGETS],
      'fresh_A_sha256':sha(fresh_a.tobytes()),'after_history_sha256':sha(history.tobytes()),'fresh_B_sha256':sha(fresh_b.tobytes()),
      'fresh_A_equals_fresh_B_exact':exact_fresh,'fresh_A_equals_after_history_exact':exact_history_a,'fresh_B_equals_after_history_exact':exact_history_b,
      'finite_masks_all_equal':bool(np.array_equal(np.isfinite(fresh_a),np.isfinite(fresh_b)) and np.array_equal(np.isfinite(fresh_a),np.isfinite(history))),
      'positive_masks_all_equal':bool(np.array_equal(fresh_a>0,fresh_b>0) and np.array_equal(fresh_a>0,history>0)),
      'fresh_A_vs_fresh_B_max_abs_diagnostic':fa_fb[0],'fresh_A_vs_fresh_B_max_rel_diagnostic':fa_fb[1],
      'fresh_A_vs_history_max_abs_diagnostic':fa_h[0],'fresh_A_vs_history_max_rel_diagnostic':fa_h[1],
      'pre_max_requested_node_coordinate_rel_mismatch':mx_pre,'fresh_A_tail_max_requested_node_coordinate_rel_mismatch':mx_a,'history_tail_max_requested_node_coordinate_rel_mismatch':mx_h,'fresh_B_tail_max_requested_node_coordinate_rel_mismatch':mx_b,
      'k_keys':[k_a,k_h,k_b],
      'token':'PASS_EXP073JQ_'+cls
    }
    (out/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print(json.dumps(result,sort_keys=True)); return 0

if __name__=='__main__': raise SystemExit(main())
