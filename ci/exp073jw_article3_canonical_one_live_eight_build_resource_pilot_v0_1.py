#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
import numpy as np

H=1e-4; REL_TOL=1e-3; LOOKUP_REL_TOL=1e-12; NATIVE_KPD=20.0; CAPACITY=4608
COARSE_N=2049; FINE_N=4097
COARSE_TEXT_SHA='72c732a02b9f6f4adeab70c7792f16e4490f038544c221aed9b72a14e5b1ec47'
FINE_TEXT_SHA='290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7'
COARSE_NODE_SHA='6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46'
FINE_NODE_SHA='f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb'
CLASS_COMMIT='ac627d54e9ce196a08878d1ba33999819925d19c'
MODELS=(('reference',0.0,0.0),('alpha_minus',-H,0.0),('beta_plus',0.0,H),('beta_minus',0.0,-H))
REQUESTS=(('A',float.fromhex('0x1.3851eb851eb85p-1'),np.asarray([0.0013,0.0047,0.013,0.041],dtype=np.float64)),('B',float.fromhex('0x1.1c28f5c28f5c3p+0'),np.asarray([0.0019,0.0073,0.021,0.057],dtype=np.float64)))

def sha(b): return hashlib.sha256(b).hexdigest()
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def load_nodes(path,count,text_sha,node_sha):
    raw=Path(path).read_bytes()
    if sha(raw)!=text_sha: raise SystemExit('canonical text sha mismatch')
    lines=raw.decode().splitlines()
    if len(lines)!=count: raise SystemExit('canonical line count mismatch')
    words=np.asarray([int(x,16) for x in lines],dtype='<u8')
    nodes=np.ascontiguousarray(words.view('<f8'),dtype=np.float64)
    if sha(np.ascontiguousarray(nodes,dtype='<f8').tobytes())!=node_sha: raise SystemExit('canonical node sha mismatch')
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

def run_lattice(jj,Class,nodes,baseline,precision,label):
    raw={q:{} for q,_,_ in REQUESTS}; receipts=[]; max_lookup=0.0; unsupported=0; builds=0
    for role,aa,bb in MODELS:
        c=Class(); builds+=1
        c.set(jj.class_params(Path(baseline),Path(precision),aa,bb,nodes)); c.compute(['transfer'])
        try:
            r={'role':role,'requests':{},'k_keys':set()}
            for q,z,t in REQUESTS:
                v,valid,mx,key=evaluate(jj,c,nodes,z,t); raw[q][role]=v
                u=int(np.count_nonzero(~valid)); unsupported+=u; max_lookup=max(max_lookup,mx); r['k_keys'].add(key)
                r['requests'][q]={'payload_sha256':sha(v.tobytes()),'shape':list(v.shape),'unsupported':u,'max_lookup':mx}
            r['k_keys']=sorted(r['k_keys']); receipts.append(r)
        finally:
            try: c.struct_cleanup()
            except Exception: pass
    responses={}
    for q,_,_ in REQUESTS:
        ref=raw[q]['reference']; al=raw[q]['alpha_minus']; bp=raw[q]['beta_plus']; bm=raw[q]['beta_minus']
        responses[q]=np.ascontiguousarray(np.column_stack((np.abs((al-ref)/(-H)),np.abs((bp-bm)/(2*H)))),dtype='<f8')
    return {'label':label,'builds':builds,'max_lookup':max_lookup,'unsupported':unsupported,'model_receipts':receipts},responses

def main():
    ap=argparse.ArgumentParser()
    for x in ('jv-authority','jt-authority','coarse','fine','jj-script','baseline','precision','out'): ap.add_argument('--'+x,required=True)
    a=ap.parse_args(); jv=json.loads(Path(a.jv_authority).read_text()); jt=json.loads(Path(a.jt_authority).read_text())
    if jv.get('artifact_verified_independently') is not True or jv.get('classification')!='SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZED_PLUS_0_PLUS_0' or jv.get('recovered_jl_preregistration_permitted') is not True: raise SystemExit('JV authorization invalid')
    if jt.get('artifact_verified_independently') is not True or jt.get('classification')!='CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0': raise SystemExit('JT authority invalid')
    coarse=load_nodes(a.coarse,COARSE_N,COARSE_TEXT_SHA,COARSE_NODE_SHA); fine=load_nodes(a.fine,FINE_N,FINE_TEXT_SHA,FINE_NODE_SHA)
    jj=load_module('jj_jw',a.jj_script)
    if jj.H!=H or jj.REL_TOL!=REL_TOL or jj.LOOKUP_REL_TOL!=LOOKUP_REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD: raise SystemExit('JJ constants mismatch')
    jj.CAPACITY=CAPACITY
    from classy import Class
    cre,cr=run_lattice(jj,Class,coarse,a.baseline,a.precision,'coarse')
    fre,fr=run_lattice(jj,Class,fine,a.baseline,a.precision,'fine')
    diagnostics={}; finite=True
    for q,_,_ in REQUESTS:
        x=cr[q]; y=fr[q]; finite &= bool(np.all(np.isfinite(x)) and np.all(np.isfinite(y)))
        den=np.maximum(np.abs(x),np.abs(y)); ad=np.abs(x-y); rel=np.divide(ad,den,out=np.zeros_like(ad),where=den!=0)
        diagnostics[q]={'coarse_response_sha256':sha(x.tobytes()),'fine_response_sha256':sha(y.tobytes()),'shape':list(x.shape),'max_abs_decision_neutral':float(np.max(ad)),'max_rel_decision_neutral':float(np.max(rel))}
    builds=cre['builds']+fre['builds']; unsupported=cre['unsupported']+fre['unsupported']; max_lookup=max(cre['max_lookup'],fre['max_lookup'])
    passed=bool(builds==8 and unsupported==0 and max_lookup<=LOOKUP_REL_TOL and finite and all(d['shape']==[4,2] for d in diagnostics.values()))
    cls='CANONICAL_ONE_LIVE_EIGHT_BUILD_RESOURCE_PILOT_PASS_PLUS_0_PLUS_0' if passed else 'RESOURCE_OR_INFRA_NOT_FEASIBLE_PLUS_0_PLUS_0'
    out={'schema':'EXP073JW_ARTICLE3_CANONICAL_ONE_LIVE_EIGHT_BUILD_RESOURCE_PILOT_RESULT_V0_1','experiment':'Exp073JW','classification':cls,'effect':'+0/+0','class_commit':CLASS_COMMIT,'h':H,'rel_tol_lineage_only':REL_TOL,'native_kpd':NATIVE_KPD,'max_live_instances':1,'total_solver_constructions':builds,'coarse_node_sha256':COARSE_NODE_SHA,'fine_node_sha256':FINE_NODE_SHA,'coarse':cre,'fine':fre,'all_instances_unsupported':unsupported,'all_instances_max_lookup':max_lookup,'responses_finite':finite,'decision_neutral_coarse_fine_diagnostics':diagnostics,'full_recovered_jl_preregistration_permitted':passed,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'article3_repository_readiness_percent':68,'funnel_freeze_readiness_percent':67,'token':cls}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(cls); print(json.dumps(out,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
