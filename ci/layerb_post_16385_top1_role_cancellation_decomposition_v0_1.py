#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np

H=1e-4
LOOKUP_TOL=1e-12
AUTH_MAX=0.012484060640679777
SOURCE_PASS='POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_PASS_PLUS_0_PLUS_0'
VALIDATION_PASS='POST_16385_EXACT_HOTSPOT_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
PASS='POST_16385_TOP1_ROLE_CANCELLATION_DECOMPOSITION_PASS_PLUS_0_PLUS_0'
FAIL='POST_16385_TOP1_ROLE_CANCELLATION_DECOMPOSITION_INVALID_INFRA_PLUS_0_PLUS_0'
MODELS=(('reference',0.0,0.0),('alpha_minus',-H,0.0),('beta_plus',0.0,H),('beta_minus',0.0,-H))


def load(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path))
    if s is None or s.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def rel(a,b):
    a=float(a); b=float(b)
    if not (math.isfinite(a) and math.isfinite(b)): return None
    den=max(abs(a),abs(b))
    return 0.0 if den==0.0 and a==b else (None if den==0.0 else abs(a-b)/den)


def validate_source(source_path,validation_path):
    s=json.loads(Path(source_path).read_text()); v=json.loads(Path(validation_path).read_text())
    if not (s.get('classification')==SOURCE_PASS and s.get('shared_call_count')==441 and s.get('des_call_count')==377 and s.get('boss_gl64_call_count')==64 and s.get('shared_plan_bitwise_identical') is True and s.get('execution_lifecycle')=={'constructions':8,'live':0,'max_live':1} and s.get('unsupported_target_evaluations')==0 and float(s.get('max_requested_node_coordinate_rel_mismatch',1.0))<=LOOKUP_TOL and s.get('scientific_authority_created') is False and s.get('next_rung_authorized') is False and s.get('covariance_restriction_authorized') is False and s.get('Wm_S3_opened') is False): raise RuntimeError('invalid exact-hotspot source')
    if not (v.get('classification')==VALIDATION_PASS and v.get('structural_valid') is True and v.get('exact_hotspot_provenance_reproduced') is True and float(v.get('relative_reproduction_error',1.0))<=1e-12 and v.get('next_rung_authorized') is False): raise RuntimeError('invalid terminal validation')
    top=s.get('top_64_response_atoms',[]); calls=s.get('call_maxima',[])
    if len(top)!=64 or len(calls)!=441: raise RuntimeError('source list lengths')
    t=top[0]; g=float(s['recomputed_shared_atom_global_max'])
    if float(t['relative_difference'])!=g or max(float(x['relative_difference']) for x in calls)!=g: raise RuntimeError('top1/global identity mismatch')
    if abs(g-AUTH_MAX)/AUTH_MAX>1e-12: raise RuntimeError('authoritative plateau not reproduced')
    return s,v,t


def eval_lattice(engine,jj,nodes,z,k,baseline,precision,label,tracker):
    from classy import Class
    raw={}; valid_receipt=None; lookup=0.0; kkeys=set()
    targets=np.asarray([k],dtype='<f8')
    for role,alpha,beta in MODELS:
        c=None; tracker['constructions']+=1; tracker['live']+=1; tracker['max_live']=max(tracker['max_live'],tracker['live'])
        try:
            c=Class(); c.set(jj.class_params(Path(baseline),Path(precision),alpha,beta,nodes)); c.compute(['transfer'])
            vals,valid,mx,kkey=engine.evaluate_call(jj,c,nodes,z,targets)
            if valid.shape!=(1,) or vals.shape!=(1,): raise RuntimeError(f'{label}/{role} shape')
            if valid_receipt is None: valid_receipt=valid.copy()
            elif not np.array_equal(valid_receipt,valid): raise RuntimeError(f'{label} validity role mismatch')
            if not bool(valid[0]) or not math.isfinite(float(vals[0])): raise RuntimeError(f'{label}/{role} invalid selected atom')
            raw[role]=float(vals[0]); lookup=max(lookup,float(mx)); kkeys.add(str(kkey))
        finally:
            if c is not None:
                try:c.struct_cleanup()
                except Exception:pass
            tracker['live']-=1
    if tracker['live']!=0 or lookup>LOOKUP_TOL: raise RuntimeError(f'{label} lifecycle/lookup')
    ar=raw['alpha_minus']-raw['reference']; bn=raw['beta_plus']-raw['beta_minus']
    alpha=abs(ar/(-H)); beta=abs(bn/(2*H))
    return {'label':label,'raw_roles':raw,'alpha_numerator':ar,'alpha_response':alpha,'beta_numerator':bn,'beta_response':beta,'max_lookup':lookup,'kkeys':sorted(kkeys),'selected_valid':True}


def execute(a):
    _,_,t=validate_source(a.source_result,a.terminal_validation)
    engine=load('decomp_engine',a.engine_script); jj=load('decomp_jj',a.jj_script)
    if engine.H!=H or jj.H!=H or engine.LOOKUP_REL_TOL!=LOOKUP_TOL: raise RuntimeError('frozen constants mismatch')
    jj.CAPACITY=18432
    coarse=engine.load_nodes(a.coarse,8193,'90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6','6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515')
    fine=engine.load_nodes(a.fine,16385,'7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69','3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975')
    z=float.fromhex(t['z_binary64_hex']); k=float.fromhex(t['target_k_binary64_hex'])
    if z.hex()!=t['z_binary64_hex'] or k.hex()!=t['target_k_binary64_hex']: raise RuntimeError('binary64 roundtrip mismatch')
    tracker={'constructions':0,'live':0,'max_live':0}
    c=eval_lattice(engine,jj,coarse,z,k,a.baseline,a.precision,'canonical_8193',tracker)
    if tracker!={'constructions':4,'live':0,'max_live':1}: raise RuntimeError('coarse lifecycle')
    f=eval_lattice(engine,jj,fine,z,k,a.baseline,a.precision,'canonical_16385',tracker)
    if tracker!={'constructions':8,'live':0,'max_live':1}: raise RuntimeError('full lifecycle')
    roles={r:rel(c['raw_roles'][r],f['raw_roles'][r]) for r,_,_ in MODELS}
    out={'schema':'LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_DECOMPOSITION_V0_1','classification':PASS,'effect':'+0/+0','selected_atom':t,'selection_rule':'exact_hotspot.top_64_response_atoms[0]','canonical_8193':c,'canonical_16385':f,'cross_grid_raw_role_relative_differences':roles,'alpha_numerator_cross_grid_relative_difference':rel(c['alpha_numerator'],f['alpha_numerator']),'alpha_response_cross_grid_relative_difference':rel(c['alpha_response'],f['alpha_response']),'beta_numerator_cross_grid_relative_difference':rel(c['beta_numerator'],f['beta_numerator']),'beta_response_cross_grid_relative_difference':rel(c['beta_response'],f['beta_response']),'alpha_cancellation_scale_8193':abs(c['alpha_numerator'])/max(abs(c['raw_roles']['alpha_minus']),abs(c['raw_roles']['reference'])),'alpha_cancellation_scale_16385':abs(f['alpha_numerator'])/max(abs(f['raw_roles']['alpha_minus']),abs(f['raw_roles']['reference'])),'beta_cancellation_scale_8193':abs(c['beta_numerator'])/max(abs(c['raw_roles']['beta_plus']),abs(c['raw_roles']['beta_minus'])),'beta_cancellation_scale_16385':abs(f['beta_numerator'])/max(abs(f['raw_roles']['beta_plus']),abs(f['raw_roles']['beta_minus'])),'execution_lifecycle':tracker,'alternative_h_evaluated':False,'scientific_107_row_replay_executed':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':PASS}
    primary='alpha_response_cross_grid_relative_difference' if int(t['component_index'])==0 else 'beta_response_cross_grid_relative_difference'
    out['primary_component_metric']=primary; out['primary_component_relative_difference']=out[primary]
    return out


def main():
    p=argparse.ArgumentParser()
    for x in ('source-result','terminal-validation','engine-script','jj-script','coarse','fine','baseline','precision','out'): p.add_argument('--'+x,required=True)
    a=p.parse_args()
    try:r=execute(a)
    except Exception as e:r={'schema':'LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_DECOMPOSITION_V0_1','classification':FAIL,'effect':'+0/+0','error':f'{type(e).__name__}: {e}','scientific_107_row_replay_executed':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':FAIL}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(r['token']); return 0

if __name__=='__main__': raise SystemExit(main())
