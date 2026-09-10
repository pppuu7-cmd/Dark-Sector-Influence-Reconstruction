#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
import numpy as np

H=1e-4; REL_TOL=1e-3; LOOKUP_REL_TOL=1e-12; CAPACITY=4608; NATIVE_KPD=20.0
BASE_N=4096; EXPECTED_N=4097; CLASS_COMMIT='ac627d54e9ce196a08878d1ba33999819925d19c'
MODELS={'reference':(0.0,0.0),'alpha_minus':(-H,0.0),'beta_plus':(0.0,H),'beta_minus':(0.0,-H)}
ORDER=('reference','alpha_minus','beta_plus','beta_minus')
REQUESTS=(('A',float.fromhex('0x1.3851eb851eb85p-1'),np.asarray([0.0013,0.0047,0.013,0.041],dtype=np.float64)),('B',float.fromhex('0x1.1c28f5c28f5c3p+0'),np.asarray([0.0019,0.0073,0.021,0.057],dtype=np.float64)))

def sha(b): return hashlib.sha256(b).hexdigest()
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path));
    if spec is None or spec.loader is None: raise RuntimeError(path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

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
    a,b=MODELS[role]; c=Class(); c.set(jj.class_params(Path(baseline),Path(precision),a,b,nodes)); c.compute(['transfer'])
    out={}; max_mx=0.0; unsup=0; keys=set()
    try:
        for label,z,t in REQUESTS:
            v,valid,mx,key=evaluate(jj,c,nodes,z,t); out[label]=v; max_mx=max(max_mx,mx); unsup+=int(np.count_nonzero(~valid)); keys.add(key)
    finally:
        try: c.struct_cleanup()
        except Exception: pass
    return out,max_mx,unsup,sorted(keys)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--model',choices=ORDER,required=True); ap.add_argument('--jj-script',required=True); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    jj=load_module('jj_js',a.jj_script)
    if jj.H!=H or jj.REL_TOL!=REL_TOL or jj.LOOKUP_REL_TOL!=LOOKUP_REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD: raise SystemExit('frozen constants mismatch')
    jj.CAPACITY=CAPACITY; nodes,r,nlo,nhi=jj.guarded_lattice(BASE_N)
    if (nlo,nhi,len(nodes))!=(0,1,EXPECTED_N): raise SystemExit('lattice mismatch')
    from classy import Class
    before,bmx,buns,bkeys=run_role(jj,Class,nodes,a.baseline,a.precision,a.model)
    intervening=[]; all_mx=bmx; all_uns=buns
    for role in ORDER:
        if role==a.model: continue
        vals,mx,uns,keys=run_role(jj,Class,nodes,a.baseline,a.precision,role); all_mx=max(all_mx,mx); all_uns+=uns
        intervening.append({'role':role,'A_sha256':sha(vals['A'].tobytes()),'B_sha256':sha(vals['B'].tobytes()),'max_lookup':mx,'unsupported':uns,'k_keys':keys})
    after,amx,auns,akeys=run_role(jj,Class,nodes,a.baseline,a.precision,a.model); all_mx=max(all_mx,amx); all_uns+=auns
    checks={}; exact=True
    for label,_,_ in REQUESTS:
        x=before[label]; y=after[label]; den=np.maximum(np.abs(x),np.abs(y)); ad=np.abs(x-y); rel=np.divide(ad,den,out=np.zeros_like(ad),where=den!=0)
        ae=bool(np.array_equal(x,y)); se=sha(x.tobytes())==sha(y.tobytes()); fe=bool(np.array_equal(np.isfinite(x),np.isfinite(y))); pe=bool(np.array_equal(x>0,y>0)); exact &= ae and se and fe and pe
        checks[label]={'before_sha256':sha(x.tobytes()),'after_sha256':sha(y.tobytes()),'array_equal':ae,'byte_sha_equal':se,'finite_masks_equal':fe,'positive_masks_equal':pe,'max_abs_diagnostic':float(np.max(ad)),'max_rel_diagnostic':float(np.max(rel))}
    passed=bool(exact and all_uns==0 and all_mx<=LOOKUP_REL_TOL)
    cls='FINE4097_CROSS_MODEL_LIFECYCLE_ISOLATION_PASS_PLUS_0_PLUS_0' if passed else 'FINE4097_CROSS_MODEL_LIFECYCLE_ISOLATION_FAIL_PLUS_0_PLUS_0'
    d={'schema':'EXP073JS_ARTICLE3_FINE4097_CROSS_MODEL_LIFECYCLE_ISOLATION_RESULT_V0_1','experiment':'Exp073JS','model':a.model,'classification':cls,'effect':'+0/+0','base_n':BASE_N,'requested_node_count':len(nodes),'guard_counts':[nlo,nhi],'ratio_hex':float(r).hex(),'node_payload_sha256':sha(np.ascontiguousarray(nodes,dtype='<f8').tobytes()),'h':H,'rel_tol_lineage_only':REL_TOL,'native_kpd':NATIVE_KPD,'class_commit':CLASS_COMMIT,'max_live_instances':1,'execution_order':[a.model]+[q for q in ORDER if q!=a.model]+[a.model],'before_max_lookup':bmx,'after_max_lookup':amx,'all_instances_max_lookup':all_mx,'before_unsupported':buns,'after_unsupported':auns,'all_instances_unsupported':all_uns,'before_k_keys':bkeys,'after_k_keys':akeys,'intervening_receipts':intervening,'requests':checks,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'article3_readiness_percent':68,'funnel_freeze_readiness_percent':67,'token':('PASS_EXP073JS_' if passed else 'FAIL_EXP073JS_')+cls}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n'); print(d['token']); print(json.dumps(d,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
