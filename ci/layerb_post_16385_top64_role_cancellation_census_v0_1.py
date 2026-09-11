#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np

H=1e-4
LOOKUP_TOL=1e-12
SOURCE_PASS='POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_PASS_PLUS_0_PLUS_0'
TOP1_AUTH_PASS='POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
PASS='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
FAIL='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_INVALID_INFRA_PLUS_0_PLUS_0'
MODELS=(('reference',0.0,0.0),('alpha_minus',-H,0.0),('beta_plus',0.0,H),('beta_minus',0.0,-H))


def load(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path))
    if s is None or s.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def rel(a,b):
    a=float(a); b=float(b)
    if not (math.isfinite(a) and math.isfinite(b)): return None
    den=max(abs(a),abs(b))
    if den==0.0: return 0.0 if a==b else None
    return abs(a-b)/den


def rel_repro(a,b):
    a=float(a); b=float(b)
    if a==0.0 and b==0.0: return 0.0
    den=max(abs(a),abs(b))
    return None if den==0.0 else abs(a-b)/den


def rankdata(a):
    x=np.asarray(a,dtype=float); order=np.argsort(x,kind='mergesort'); ranks=np.empty(len(x),dtype=float)
    i=0
    while i<len(x):
        j=i+1
        while j<len(x) and x[order[j]]==x[order[i]]: j+=1
        ranks[order[i:j]]=0.5*(i+j-1)+1.0
        i=j
    return ranks


def spearman(x,y):
    if len(x)<2: return None
    rx=rankdata(x); ry=rankdata(y)
    sx=float(np.std(rx)); sy=float(np.std(ry))
    if sx==0.0 or sy==0.0: return None
    return float(np.corrcoef(rx,ry)[0,1])


def validate_source(source_path,auth_path):
    s=json.loads(Path(source_path).read_text()); a=json.loads(Path(auth_path).read_text())
    if not (s.get('classification')==SOURCE_PASS and s.get('shared_call_count')==441 and s.get('des_call_count')==377 and s.get('boss_gl64_call_count')==64 and s.get('shared_plan_bitwise_identical') is True and s.get('execution_lifecycle')=={'constructions':8,'live':0,'max_live':1} and s.get('unsupported_target_evaluations')==0 and float(s.get('max_requested_node_coordinate_rel_mismatch',1.0))<=LOOKUP_TOL and s.get('scientific_authority_created') is False and s.get('next_rung_authorized') is False and s.get('covariance_restriction_authorized') is False and s.get('Wm_S3_opened') is False): raise RuntimeError('invalid exact-hotspot source')
    top=s.get('top_64_response_atoms',[])
    if len(top)!=64: raise RuntimeError('source top64 length')
    if not (a.get('classification')==TOP1_AUTH_PASS and a.get('scientific_authority_created') is False and a.get('next_rung_authorized') is False and a.get('covariance_restriction_authorized') is False and a.get('Wm_S3_opened') is False): raise RuntimeError('invalid top1 terminal authority')
    if int(a.get('source_hotspot_run_id',-1))!=34592951737 or a.get('source_result_sha256')!='4023403aaae03481507f778ce4a85c119160cebd785c9c91a534260783049394': raise RuntimeError('top1 source identity mismatch')
    if a.get('selected_atom')!=top[0]: raise RuntimeError('top1 selected atom mismatch')
    return s,top


def eval_grid(engine,jj,nodes,atoms,baseline,precision,label,tracker):
    from classy import Class
    rows=[{'raw_roles':{},'max_lookup':0.0,'kkeys':set(),'valid':None} for _ in atoms]
    for role,alpha,beta in MODELS:
        c=None; tracker['constructions']+=1; tracker['live']+=1; tracker['max_live']=max(tracker['max_live'],tracker['live'])
        try:
            c=Class(); c.set(jj.class_params(Path(baseline),Path(precision),alpha,beta,nodes)); c.compute(['transfer'])
            for i,t in enumerate(atoms):
                z=float.fromhex(t['z_binary64_hex']); k=float.fromhex(t['target_k_binary64_hex'])
                if z.hex()!=t['z_binary64_hex'] or k.hex()!=t['target_k_binary64_hex']: raise RuntimeError(f'{label}/{i} binary64 roundtrip')
                vals,valid,mx,kkey=engine.evaluate_call(jj,c,nodes,z,np.asarray([k],dtype='<f8'))
                if valid.shape!=(1,) or vals.shape!=(1,): raise RuntimeError(f'{label}/{role}/{i} shape')
                if rows[i]['valid'] is None: rows[i]['valid']=bool(valid[0])
                elif rows[i]['valid']!=bool(valid[0]): raise RuntimeError(f'{label}/{i} validity role mismatch')
                if not bool(valid[0]) or not math.isfinite(float(vals[0])): raise RuntimeError(f'{label}/{role}/{i} invalid')
                rows[i]['raw_roles'][role]=float(vals[0]); rows[i]['max_lookup']=max(rows[i]['max_lookup'],float(mx)); rows[i]['kkeys'].add(str(kkey))
        finally:
            if c is not None:
                try:c.struct_cleanup()
                except Exception:pass
            tracker['live']-=1
    for i,r in enumerate(rows):
        if r['max_lookup']>LOOKUP_TOL or not r['valid']: raise RuntimeError(f'{label}/{i} lookup/validity')
        raw=r['raw_roles']; an=raw['alpha_minus']-raw['reference']; bn=raw['beta_plus']-raw['beta_minus']
        r['alpha_numerator']=an; r['alpha_response']=abs(an/(-H)); r['beta_numerator']=bn; r['beta_response']=abs(bn/(2*H))
        r['alpha_cancellation_scale']=abs(an)/max(abs(raw['alpha_minus']),abs(raw['reference']))
        r['beta_cancellation_scale']=abs(bn)/max(abs(raw['beta_plus']),abs(raw['beta_minus']))
        r['kkeys']=sorted(r['kkeys']); r['label']=label
    return rows


def execute(a):
    source,atoms=validate_source(a.source_result,a.top1_authority)
    engine=load('census_engine',a.engine_script); jj=load('census_jj',a.jj_script)
    if engine.H!=H or jj.H!=H or engine.LOOKUP_REL_TOL!=LOOKUP_TOL: raise RuntimeError('frozen constants mismatch')
    jj.CAPACITY=18432
    coarse=engine.load_nodes(a.coarse,8193,'90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6','6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515')
    fine=engine.load_nodes(a.fine,16385,'7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69','3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975')
    tracker={'constructions':0,'live':0,'max_live':0}
    cr=eval_grid(engine,jj,coarse,atoms,a.baseline,a.precision,'canonical_8193',tracker)
    if tracker!={'constructions':4,'live':0,'max_live':1}: raise RuntimeError('coarse lifecycle')
    fr=eval_grid(engine,jj,fine,atoms,a.baseline,a.precision,'canonical_16385',tracker)
    if tracker!={'constructions':8,'live':0,'max_live':1}: raise RuntimeError('full lifecycle')
    rows=[]; repro=[]; rawmax=0.0; cancel=[]; dx=[]; dy=[]
    for i,(t,c,f) in enumerate(zip(atoms,cr,fr)):
        roles={r:rel(c['raw_roles'][r],f['raw_roles'][r]) for r,_,_ in MODELS}
        rawmax=max(rawmax,max(float(v) for v in roles.values() if v is not None))
        alpha_rel=rel(c['alpha_response'],f['alpha_response']); beta_rel=rel(c['beta_response'],f['beta_response'])
        primary=alpha_rel if int(t['component_index'])==0 else beta_rel
        rr=rel_repro(primary,float(t['relative_difference']))
        if rr is None or rr>1e-12: raise RuntimeError(f'atom {i} primary reproduction {rr}')
        cs=min(c['alpha_cancellation_scale'],f['alpha_cancellation_scale']) if int(t['component_index'])==0 else min(c['beta_cancellation_scale'],f['beta_cancellation_scale'])
        row={'rank':i+1,'source_atom':t,'cross_grid_raw_role_relative_differences':roles,'alpha_numerator_cross_grid_relative_difference':rel(c['alpha_numerator'],f['alpha_numerator']),'alpha_response_cross_grid_relative_difference':alpha_rel,'beta_numerator_cross_grid_relative_difference':rel(c['beta_numerator'],f['beta_numerator']),'beta_response_cross_grid_relative_difference':beta_rel,'alpha_cancellation_scale_8193':c['alpha_cancellation_scale'],'alpha_cancellation_scale_16385':f['alpha_cancellation_scale'],'beta_cancellation_scale_8193':c['beta_cancellation_scale'],'beta_cancellation_scale_16385':f['beta_cancellation_scale'],'primary_response_cross_grid_relative_difference':primary,'primary_reproduction_relative_error':rr,'primary_min_cancellation_scale':cs,'canonical_8193_raw_roles':c['raw_roles'],'canonical_16385_raw_roles':f['raw_roles']}
        rows.append(row); repro.append(rr); cancel.append(cs)
        if cs>0.0 and primary is not None and primary>0.0 and math.isfinite(cs) and math.isfinite(primary): dx.append(math.log10(cs)); dy.append(math.log10(primary))
    out={'schema':'LAYERB_POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_V0_1','classification':PASS,'effect':'+0/+0','source_hotspot_run_id':34592951737,'selection_rule':'exact complete ordered source_result.top_64_response_atoms','atom_count':64,'atoms':rows,'max_primary_reproduction_relative_error':max(repro),'median_primary_reproduction_relative_error':float(np.median(np.asarray(repro,dtype=float))),'max_cross_grid_raw_role_relative_difference':rawmax,'minimum_primary_cancellation_scale':min(cancel),'source_atoms_ge_1e_3_count':sum(float(t['relative_difference'])>=1e-3 for t in atoms),'spearman_log10_min_cancellation_scale_vs_log10_primary_response_discrepancy':spearman(dx,dy),'spearman_pair_count':len(dx),'execution_lifecycle':tracker,'unsupported_target_evaluations':0,'max_requested_node_coordinate_rel_mismatch':max(max(r['max_lookup'] for r in cr),max(r['max_lookup'] for r in fr)),'alternative_h_evaluated':False,'scientific_107_row_replay_executed':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':PASS}
    return out


def main():
    p=argparse.ArgumentParser()
    for x in ('source-result','top1-authority','engine-script','jj-script','coarse','fine','baseline','precision','out'): p.add_argument('--'+x,required=True)
    a=p.parse_args()
    try:r=execute(a)
    except Exception as e:r={'schema':'LAYERB_POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_V0_1','classification':FAIL,'effect':'+0/+0','error':f'{type(e).__name__}: {e}','scientific_107_row_replay_executed':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':FAIL}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(r['token']); return 0

if __name__=='__main__': raise SystemExit(main())
