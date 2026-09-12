#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, pathlib, statistics

TOL=0.001
H=1e-4

spec=importlib.util.spec_from_file_location('loc','ci/layerb_operand_localization_v0_2.py')
loc=importlib.util.module_from_spec(spec); spec.loader.exec_module(loc)


def dump(path,obj):
    pathlib.Path(path).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

def pct(xs,q):
    ys=sorted(xs)
    if not ys: return None
    if len(ys)==1: return ys[0]
    x=(len(ys)-1)*q; lo=int(math.floor(x)); hi=int(math.ceil(x)); f=x-lo
    return ys[lo]*(1-f)+ys[hi]*f

def load_common(operands,plan=None):
    CL,C,CV=loc.load_grid(operands,'coarse',True)
    FL,F,FV=loc.load_grid(operands,'fine',True)
    if len(CL)!=441 or len(FL)!=569 or CL!=FL[:441]: raise RuntimeError('common operand shape mismatch')
    calls=None
    if plan:
        _,calls,_,_=loc.pick_plans(loc.load_json(plan))
    return CL,C,CV,F,FV,calls

def beta_condition(raw,i,j):
    bp=raw['beta_plus'][i][j]; bm=raw['beta_minus'][i][j]
    den=abs(bp-bm)
    return math.inf if den==0 else (abs(bp)+abs(bm))/den

def metric(a,b):
    if not (math.isfinite(a) and math.isfinite(b)): return None
    d=max(abs(a),abs(b))
    return 0.0 if d==0 else abs(a-b)/d

def census(a):
    CL,C,CV,F,FV,calls=load_common(a.operands,a.plan)
    violations={'alpha':0,'beta':0,'DES':0,'BOSS_GL64':0}
    beta_cond_all=[]; beta_cond_fail=[]; fail_rows=[]; maxes={'alpha':0.0,'beta':0.0}
    for i,n in enumerate(CL):
        domain='DES' if i<377 else 'BOSS_GL64'
        for j in range(n):
            if CV['reference'][i][j]!=FV['reference'][i][j]: raise RuntimeError('validity mismatch')
            if not CV['reference'][i][j]: continue
            for q,name in ((0,'alpha'),(1,'beta')):
                cr=loc.response(C,i,j,q); fr=loc.response(F,i,j,q)
                if not (math.isfinite(cr) and math.isfinite(fr) and cr>0 and fr>0): continue
                r=loc.rel_metric(cr,fr); maxes[name]=max(maxes[name],r)
                if q==1:
                    k=max(beta_condition(C,i,j),beta_condition(F,i,j)); beta_cond_all.append(k)
                if r>TOL:
                    violations[name]+=1; violations[domain]+=1
                    if q==1:
                        k=max(beta_condition(C,i,j),beta_condition(F,i,j)); beta_cond_fail.append(k)
                        fail_rows.append({'relative_difference':r,'domain':domain,'call_index':i,'target_index':j,'z':loc.fhex(calls[i]['z_u64hex']),'target_k_Mpc^-1':loc.fhex(calls[i]['targets_u64hex'][j]),'condition_number_max_grid':k})
    fail_rows.sort(key=lambda x:x['relative_difference'],reverse=True)
    def stats(xs): return {'count':len(xs),'min':min(xs) if xs else None,'median':statistics.median(xs) if xs else None,'p99':pct(xs,0.99),'max':max(xs) if xs else None}
    des=[x for x in fail_rows if x['domain']=='DES']; boss=[x for x in fail_rows if x['domain']=='BOSS_GL64']
    out={'schema':'LAYERB_BETA_CANCELLATION_CONDITIONING_CENSUS_V0_3','classification':'CENSUS_COMPLETE','relative_tolerance':TOL,'strict_less_than':True,'violations':violations,'max_relative_difference_by_component':maxes,'all_frozen_tolerance_violations_beta_only':violations['alpha']==0 and violations['beta']>0,'beta_condition_number_all':stats(beta_cond_all),'beta_condition_number_failing':stats(beta_cond_fail),'failure_domain_counts':{'DES':len(des),'BOSS_GL64':len(boss)},'DES_failure_range':{'z_min':min(x['z'] for x in des) if des else None,'z_max':max(x['z'] for x in des) if des else None,'k_min_Mpc^-1':min(x['target_k_Mpc^-1'] for x in des) if des else None,'k_max_Mpc^-1':max(x['target_k_Mpc^-1'] for x in des) if des else None},'BOSS_failure_range':{'z_min':min(x['z'] for x in boss) if boss else None,'z_max':max(x['z'] for x in boss) if boss else None,'k_min_Mpc^-1':min(x['target_k_Mpc^-1'] for x in boss) if boss else None,'k_max_Mpc^-1':max(x['target_k_Mpc^-1'] for x in boss) if boss else None},'top_failures':fail_rows[:20],'class_solver_invoked':False,'scientific_operand_recomputed':False,'denser_successor_65537_authorized':False,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))

def raw(a):
    CL,C,CV,F,FV,_=load_common(a.operands,None)
    role_max={r:0.0 for r in loc.ROLES}; ampl=[]; arg=None
    for i,n in enumerate(CL):
        for j in range(n):
            if not CV['reference'][i][j]: continue
            rawrel={}
            for role in loc.ROLES:
                rr=metric(C[role][i][j],F[role][i][j]); rawrel[role]=rr
                if rr is not None: role_max[role]=max(role_max[role],rr)
            cr=loc.response(C,i,j,1); fr=loc.response(F,i,j,1)
            if not (math.isfinite(cr) and math.isfinite(fr) and cr>0 and fr>0): continue
            dr=loc.rel_metric(cr,fr)
            if arg is None or dr>arg['derived_beta_relative_difference']:
                arg={'call_index':i,'target_index':j,'derived_beta_relative_difference':dr,'coarse_roles':{r:C[r][i][j] for r in loc.ROLES},'fine_roles':{r:F[r][i][j] for r in loc.ROLES},'raw_role_relative_grid_shift':rawrel}
            if dr>TOL:
                rb=max(rawrel['beta_plus'] or 0.0,rawrel['beta_minus'] or 0.0)
                if rb>0: ampl.append(dr/rb)
    out={'schema':'LAYERB_RAW_ROLE_GRID_STABILITY_V0_3','classification':'RAW_ROLE_STABILITY_COMPLETE','raw_role_global_max_relative_grid_shift':role_max,'largest_raw_role_relative_grid_shift':max(role_max.values()),'authoritative_beta_derived_max_relative_difference':arg['derived_beta_relative_difference'],'derived_to_largest_raw_role_max_ratio':arg['derived_beta_relative_difference']/max(role_max.values()),'failing_beta_amplification_vs_local_raw_beta_shift':{'count':len(ampl),'min':min(ampl) if ampl else None,'median':statistics.median(ampl) if ampl else None,'max':max(ampl) if ampl else None},'global_beta_argmax_role_decomposition':arg,'class_solver_invoked':False,'scientific_operand_recomputed':False,'denser_successor_65537_authorized':False,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))

def identity(a):
    CL,C,CV,F,FV,_=load_common(a.operands,None)
    max_err=0.0; beta_viol=0; exact_count=0; atoms=0; global_rec=None
    for i,n in enumerate(CL):
        for j in range(n):
            if not CV['reference'][i][j]: continue
            cbp=C['beta_plus'][i][j]; cbm=C['beta_minus'][i][j]; fbp=F['beta_plus'][i][j]; fbm=F['beta_minus'][i][j]
            cn=cbp-cbm; fn=fbp-fbm
            cr=abs(cn)/(2*H); fr=abs(fn)/(2*H)
            if not (math.isfinite(cr) and math.isfinite(fr) and cr>0 and fr>0): continue
            drel=loc.rel_metric(cr,fr); nrel=abs(abs(cn)-abs(fn))/max(abs(cn),abs(fn)); err=abs(drel-nrel)
            atoms+=1; max_err=max(max_err,err)
            if err==0.0: exact_count+=1
            if drel>TOL: beta_viol+=1
            if global_rec is None or drel>global_rec['derived_relative_difference']:
                global_rec={'call_index':i,'target_index':j,'coarse_numerator':cn,'fine_numerator':fn,'coarse_beta_response':cr,'fine_beta_response':fr,'derived_relative_difference':drel,'numerator_relative_difference':nrel,'identity_absolute_error':err}
    out={'schema':'LAYERB_INDEPENDENT_BETA_NUMERATOR_IDENTITY_V0_3','classification':'BETA_NUMERATOR_IDENTITY_COMPLETE','beta_atoms_checked':atoms,'beta_tolerance_violations':beta_viol,'exact_binary64_identity_count':exact_count,'max_absolute_difference_between_derivative_and_numerator_relative_metrics':max_err,'global_argmax':global_rec,'identity_holds_to_1e-15':max_err<=1e-15,'class_solver_invoked':False,'scientific_operand_recomputed':False,'denser_successor_65537_authorized':False,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))

def decision(a):
    root=pathlib.Path(a.combined)
    def load(name):
        p=root/name; return json.loads(p.read_text()) if p.exists() else None
    c=load('conditioning_census.json'); r=load('raw_role_stability.json'); i=load('beta_numerator_identity.json')
    present=all(x is not None for x in (c,r,i))
    if present:
        beta_only=c['all_frozen_tolerance_violations_beta_only'] and c['violations']['beta']==31
        raw_small=r['largest_raw_role_relative_grid_shift'] < r['authoritative_beta_derived_max_relative_difference']/1000.0
        identity_ok=i['identity_holds_to_1e-15'] and i['beta_tolerance_violations']==31
        cond_sep=(c['beta_condition_number_failing']['min'] is not None and c['beta_condition_number_all']['median'] is not None and c['beta_condition_number_failing']['min']>c['beta_condition_number_all']['median'])
        supported=beta_only and raw_small and identity_ok and cond_sep
    else:
        beta_only=raw_small=identity_ok=cond_sep=supported=False
    cls='SYMMETRIC_BETA_SUBTRACTIVE_CANCELLATION_AMPLIFICATION_STRONGLY_SUPPORTED' if supported else ('CANCELLATION_CONDITIONING_DIAGNOSTIC_COMPLETE_BUT_CRITERIA_NOT_ALL_MET' if present else 'CANCELLATION_CONDITIONING_INFRASTRUCTURE_INCOMPLETE')
    out={'schema':'LAYERB_BETA_CANCELLATION_CONDITIONING_DECISION_V0_3','classification':cls,'all_streams_present':present,'beta_only_frozen_tolerance_violations':beta_only,'raw_role_grid_shift_at_least_three_orders_below_derived_beta_max':raw_small,'beta_derivative_numerator_identity_verified':identity_ok,'failing_condition_numbers_separated_above_full_population_median':cond_sep,'mechanism_supported':supported,'interpretation':'Diagnostic evidence for numerical conditioning only; no scientific gate acceptance and no permission to mutate h or convergence criterion.','next_permitted_stage':'PROSPECTIVELY_FROZEN_TARGETED_DIRECT_K_BETA_DIAGNOSTIC' if supported else 'AUDIT_CANCELLATION_CONDITIONING_DIAGNOSTIC','finite_difference_step_mutation_authorized':False,'criterion_mutation_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'denser_successor_65537_authorized':False,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    for name in ('census','raw','identity'):
        q=sub.add_parser(name); q.add_argument('--operands',required=True); q.add_argument('--out',required=True)
        if name=='census': q.add_argument('--plan',required=True)
    q=sub.add_parser('decision'); q.add_argument('--combined',required=True); q.add_argument('--out',required=True)
    a=ap.parse_args(); {'census':census,'raw':raw,'identity':identity,'decision':decision}[a.cmd](a)
if __name__=='__main__': main()
