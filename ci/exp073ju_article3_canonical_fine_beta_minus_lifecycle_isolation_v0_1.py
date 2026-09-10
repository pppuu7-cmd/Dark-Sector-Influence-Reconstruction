#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
import numpy as np

H=1e-4; REL_TOL=1e-3; LOOKUP_REL_TOL=1e-12; CAPACITY=4608; NATIVE_KPD=20.0
EXPECTED_N=4097
CANONICAL_TEXT_SHA='290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7'
CANONICAL_NODE_SHA='f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb'
CLASS_COMMIT='ac627d54e9ce196a08878d1ba33999819925d19c'
MODELS={'reference':(0.0,0.0),'alpha_minus':(-H,0.0),'beta_plus':(0.0,H),'beta_minus':(0.0,-H)}
ORDER=('beta_minus','reference','alpha_minus','beta_plus','beta_minus')
REQUESTS=(('A',float.fromhex('0x1.3851eb851eb85p-1'),np.asarray([0.0013,0.0047,0.013,0.041],dtype=np.float64)),('B',float.fromhex('0x1.1c28f5c28f5c3p+0'),np.asarray([0.0019,0.0073,0.021,0.057],dtype=np.float64)))

def sha(b): return hashlib.sha256(b).hexdigest()
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def load_canonical(path):
    raw=Path(path).read_bytes()
    if sha(raw)!=CANONICAL_TEXT_SHA: raise SystemExit('canonical text sha mismatch')
    lines=raw.decode().splitlines()
    if len(lines)!=EXPECTED_N: raise SystemExit('canonical line count mismatch')
    words=np.asarray([int(x,16) for x in lines],dtype='<u8')
    nodes=np.ascontiguousarray(words.view('<f8'),dtype=np.float64)
    if sha(np.ascontiguousarray(nodes,dtype='<f8').tobytes())!=CANONICAL_NODE_SHA: raise SystemExit('canonical node sha mismatch')
    if not (np.all(np.isfinite(nodes)) and np.all(nodes>0) and np.all(np.diff(nodes)>0)): raise SystemExit('invalid canonical nodes')
    return nodes

def evaluate(jj,c,nodes,z,targets):
    tk=c.get_transfer(z=float(z),output_format='class'); dm=[q for q in tk if q.strip()=='d_m']
    if len(dm)!=1: raise AssertionError('d_m key')
    kkey=None; scale=None
    for q in tk:
        s=q.lower().replace(' ','')
        if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=float(c.h()); break
        if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
    if kkey is None: raise AssertionError('k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
    if k.ndim!=1 or y.shape!=k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise AssertionError('transfer table')
    yn,mx=jj.requested_values(k,y,nodes); v,valid=jj.cubic_centered(nodes,yn,targets)
    return np.ascontiguousarray(v,dtype='<f8'),np.asarray(valid,dtype=bool),float(mx),kkey

def run_role(jj,Class,nodes,baseline,precision,role):
    aa,bb=MODELS[role]; c=Class(); c.set(jj.class_params(Path(baseline),Path(precision),aa,bb,nodes)); c.compute(['transfer'])
    out={}; max_mx=0.0; unsup=0; keys=set()
    try:
        for label,z,t in REQUESTS:
            v,valid,mx,key=evaluate(jj,c,nodes,z,t); out[label]=v; max_mx=max(max_mx,mx); unsup+=int(np.count_nonzero(~valid)); keys.add(key)
    finally:
        try: c.struct_cleanup()
        except Exception: pass
    return out,max_mx,unsup,sorted(keys)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--jj-script',required=True); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True); ap.add_argument('--canonical-fine',required=True); ap.add_argument('--jt-authority',required=True); ap.add_argument('--js-audit',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    jt=json.loads(Path(a.jt_authority).read_text()); js=json.loads(Path(a.js_audit).read_text())
    if jt.get('classification')!='CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0' or jt.get('artifact_verified_independently') is not True: raise SystemExit('JT authority invalid')
    if jt.get('fine',{}).get('node_payload_sha256')!=CANONICAL_NODE_SHA or jt.get('fine',{}).get('u64hex_sha256')!=CANONICAL_TEXT_SHA: raise SystemExit('JT fine authority mismatch')
    if js.get('classification')!='LOCAL_LIFECYCLE_PASS_CANONICAL_FINE_COVERAGE_3_OF_4_PLUS_0_PLUS_0' or js.get('canonical_geometry_roles_missing')!=['beta_minus']: raise SystemExit('JS coverage audit mismatch')
    nodes=load_canonical(a.canonical_fine)
    jj=load_module('jj_ju',a.jj_script)
    if jj.H!=H or jj.REL_TOL!=REL_TOL or jj.LOOKUP_REL_TOL!=LOOKUP_REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD: raise SystemExit('JJ constants mismatch')
    jj.CAPACITY=CAPACITY
    from classy import Class
    before,bmx,buns,bkeys=run_role(jj,Class,nodes,a.baseline,a.precision,'beta_minus')
    intervening=[]; all_mx=bmx; all_uns=buns
    for role in ('reference','alpha_minus','beta_plus'):
        vals,mx,uns,keys=run_role(jj,Class,nodes,a.baseline,a.precision,role); all_mx=max(all_mx,mx); all_uns+=uns
        intervening.append({'role':role,'A_sha256':sha(vals['A'].tobytes()),'B_sha256':sha(vals['B'].tobytes()),'max_lookup':mx,'unsupported':uns,'k_keys':keys})
    after,amx,auns,akeys=run_role(jj,Class,nodes,a.baseline,a.precision,'beta_minus'); all_mx=max(all_mx,amx); all_uns+=auns
    exact=True; checks={}
    for label,_,_ in REQUESTS:
        x=before[label]; y=after[label]; den=np.maximum(np.abs(x),np.abs(y)); ad=np.abs(x-y); rel=np.divide(ad,den,out=np.zeros_like(ad),where=den!=0)
        ae=bool(np.array_equal(x,y)); se=sha(x.tobytes())==sha(y.tobytes()); fe=bool(np.array_equal(np.isfinite(x),np.isfinite(y))); pe=bool(np.array_equal(x>0,y>0)); exact &= ae and se and fe and pe
        checks[label]={'before_sha256':sha(x.tobytes()),'after_sha256':sha(y.tobytes()),'array_equal':ae,'byte_sha_equal':se,'finite_masks_equal':fe,'positive_masks_equal':pe,'max_abs_diagnostic':float(np.max(ad)),'max_rel_diagnostic':float(np.max(rel))}
    passed=bool(exact and all_uns==0 and all_mx<=LOOKUP_REL_TOL and all(checks[q]['max_abs_diagnostic']==0.0 and checks[q]['max_rel_diagnostic']==0.0 for q in checks))
    cls='CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_PASS_PLUS_0_PLUS_0' if passed else 'CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_FAIL_PLUS_0_PLUS_0'
    d={'schema':'EXP073JU_ARTICLE3_CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_RESULT_V0_1','experiment':'Exp073JU','classification':cls,'effect':'+0/+0','model':'beta_minus','execution_order':list(ORDER),'max_live_instances':1,'requested_node_count':len(nodes),'canonical_text_sha256':CANONICAL_TEXT_SHA,'node_payload_sha256':CANONICAL_NODE_SHA,'h':H,'native_kpd':NATIVE_KPD,'class_commit':CLASS_COMMIT,'before_max_lookup':bmx,'after_max_lookup':amx,'all_instances_max_lookup':all_mx,'before_unsupported':buns,'after_unsupported':auns,'all_instances_unsupported':all_uns,'before_k_keys':bkeys,'after_k_keys':akeys,'intervening_receipts':intervening,'requests':checks,'canonical_lifecycle_coverage_after_pass':'4/4' if passed else '3/4','sequential_execution_authorization_audit_permitted':passed,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'article3_repository_readiness_percent':68,'funnel_freeze_readiness_percent':67,'token':('PASS_EXP073JU_' if passed else 'FAIL_EXP073JU_')+cls}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n'); print(d['token']); print(json.dumps(d,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
