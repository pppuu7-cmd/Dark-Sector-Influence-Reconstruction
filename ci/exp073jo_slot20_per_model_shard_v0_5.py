#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
import numpy as np

H=1e-4
REL_TOL=1e-3
NATIVE_KPD=20.0
BASE_N=4096
EXPECTED_NODE_COUNT=4097
CAPACITY=4608
PARSER_CAPACITY=131072
CLASS_COMMIT='ac627d54e9ce196a08878d1ba33999819925d19c'
CANONICAL_NODE_SHA='f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb'
CANONICAL_HEX_SHA='98cd360d0764a884471cb09b4504b79583e2ffaea4423389ec473e98b8656c2a'
PHASES=('slot20_after_history','slot20_fresh_tail')
MODELS={
 'reference':(0.0,0.0),
 'alpha_minus':(-H,0.0),
 'beta_plus':(0.0,H),
 'beta_minus':(0.0,-H),
}


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def sha(b): return hashlib.sha256(b).hexdigest()


def load_canonical(bin_path,hex_path,authority_path):
    raw=Path(bin_path).read_bytes(); hx=Path(hex_path).read_bytes(); auth=json.loads(Path(authority_path).read_text())
    if sha(raw)!=CANONICAL_NODE_SHA or sha(hx)!=CANONICAL_HEX_SHA: raise SystemExit('canonical payload SHA mismatch')
    if auth.get('classification')!='CANONICAL_4097_NODE_PAYLOAD_PERSISTED_PLUS_0_PLUS_0' or auth.get('node_payload_sha256')!=CANONICAL_NODE_SHA or auth.get('node_hex_sha256')!=CANONICAL_HEX_SHA: raise SystemExit('canonical authority mismatch')
    nodes=np.frombuffer(raw,dtype='<f8').copy(); hex_nodes=np.asarray([float.fromhex(x) for x in hx.decode().splitlines()],dtype='<f8')
    if len(nodes)!=EXPECTED_NODE_COUNT or len(hex_nodes)!=EXPECTED_NODE_COUNT or not np.array_equal(nodes,hex_nodes): raise SystemExit('canonical payload shape/roundtrip mismatch')
    if np.any(~np.isfinite(nodes)) or np.any(nodes<=0.0) or np.any(np.diff(nodes)<=0.0): raise SystemExit('canonical node validity mismatch')
    return nodes


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--phase',choices=PHASES,required=True)
    ap.add_argument('--model',choices=tuple(MODELS),required=True)
    ap.add_argument('--jj-script',required=True); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True)
    ap.add_argument('--canonical-bin',required=True); ap.add_argument('--canonical-hex',required=True); ap.add_argument('--canonical-authority',required=True)
    ap.add_argument('--out-json',required=True); ap.add_argument('--out-bin',required=True)
    a=ap.parse_args(); jj=load_module('jj_v05',a.jj_script)
    if jj.H!=H or jj.REL_TOL!=REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD: raise SystemExit('frozen JJ constants mismatch')
    jj.CAPACITY=CAPACITY
    nodes=load_canonical(a.canonical_bin,a.canonical_hex,a.canonical_authority)
    if nodes[0]!=np.float64(jj.KMIN) or nodes[BASE_N-1]!=np.float64(jj.KMAX): raise SystemExit('canonical endpoints mismatch')
    dummy=np.zeros(nodes.shape,dtype=np.float64); _,support=jj.cubic_centered(nodes,dummy,np.asarray([jj.TARGET_MIN,jj.TARGET_MAX],dtype=np.float64))
    if not bool(np.all(support)): raise SystemExit('canonical frozen-target support mismatch')
    ratio=np.float64(nodes[1]/nodes[0]); lo,hi=0,1
    alpha,beta=MODELS[a.model]
    from classy import Class
    c=Class(); c.set(jj.class_params(Path(a.baseline),Path(a.precision),alpha,beta,nodes)); c.compute(['transfer'])
    pre_z=float.fromhex('0x1.3851eb851eb85p-1'); tail_z=float.fromhex('0x1.1c28f5c28f5c3p+0')
    pre_targets=np.asarray([0.0013,0.0047,0.013,0.041],dtype=np.float64)
    tail_targets=np.asarray([0.0019,0.0073,0.021,0.057],dtype=np.float64)
    def evaluate(z,targets):
        tk=c.get_transfer(z=float(z),output_format='class'); dm=[q for q in tk if q.strip()=='d_m']
        if len(dm)!=1: raise AssertionError(f'expected exact d_m key, got {list(tk)}')
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
    try:
        pre_mx=None
        if a.phase=='slot20_after_history': _,pre_mx,_=evaluate(pre_z,pre_targets)
        tail,tail_mx,kkey=evaluate(tail_z,tail_targets)
    finally:
        try: c.struct_cleanup()
        except Exception: pass
    raw=tail.tobytes(order='C'); Path(a.out_bin).parent.mkdir(parents=True,exist_ok=True); Path(a.out_bin).write_bytes(raw)
    result={
      'schema':'EXP073JO_SLOT20_CANONICAL_PER_MODEL_SHARD_RECEIPT_V0_5','phase':a.phase,'model':a.model,'classification':'SLOT20_CANONICAL_PER_MODEL_SHARD_RECEIPT_PLUS_0_PLUS_0','effect':'+0/+0',
      'scientific_authority_created':False,'covariance_restriction_authorized':False,'alpha_hex':float(alpha).hex(),'beta_hex':float(beta).hex(),
      'native_kpd':NATIVE_KPD,'h':H,'rel_tol':REL_TOL,'base_n':BASE_N,'requested_node_count':len(nodes),'lower_guard_count':lo,'upper_guard_count':hi,
      'capacity':CAPACITY,'parser_capacity':PARSER_CAPACITY,'class_commit':CLASS_COMMIT,'grid_ratio_binary64':float(ratio),'grid_ratio_hex':float(ratio).hex(),'node_sha256':sha(nodes.astype('<f8',copy=False).tobytes()),
      'canonical_authority_sha':CANONICAL_NODE_SHA,'canonical_hex_sha':CANONICAL_HEX_SHA,
      'pre_z_hex':pre_z.hex(),'tail_z_hex':tail_z.hex(),'pre_targets_hex':[float(x).hex() for x in pre_targets],'tail_targets_hex':[float(x).hex() for x in tail_targets],
      'pre_query_executed':a.phase=='slot20_after_history','tail_values_shape':[4],'tail_values_dtype':'<f8','tail_values_nbytes':len(raw),'tail_values_sha256':sha(raw),
      'tail_all_finite':bool(np.all(np.isfinite(tail))),'tail_all_positive':bool(np.all(tail>0.0)),'pre_max_requested_node_coordinate_rel_mismatch':pre_mx,
      'tail_max_requested_node_coordinate_rel_mismatch':tail_mx,'k_key':kkey,'token':f'PASS_EXP073JO_V05_{a.phase.upper()}_{a.model.upper()}_SHARD'
    }
    if result['node_sha256']!=CANONICAL_NODE_SHA: raise SystemExit('runtime canonical node hash drift')
    Path(a.out_json).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token']); print(json.dumps(result,sort_keys=True)); return 0

if __name__=='__main__': raise SystemExit(main())
