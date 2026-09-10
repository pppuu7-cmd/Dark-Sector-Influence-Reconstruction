#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import exp073je_article3_layerb_shared_fixed_k_grid_scaling_v0_1 as je

N=512
RULES=('linear_bracket','quadratic_left','quadratic_right','cubic_centered')
PARENT_RESPONSES={'alpha_left':11.515198203966293,'beta_symmetric':1.8700385146530607}


def lagrange_eval(xs,ys,xt):
    xs=[float(v) for v in xs]; ys=[float(v) for v in ys]; xt=float(xt)
    out=0.0
    for i in range(len(xs)):
        term=ys[i]
        for j in range(len(xs)):
            if i!=j:
                term *= (xt-xs[j])/(xs[i]-xs[j])
        out += term
    return float(out)


def node_value(c,z,q):
    k,y,kkey=je.transfer_arrays(c,z)
    v,idx,actual,rel=je.direct_requested(k,y,float(q))
    return v,{'requested':float(q),'actual':actual,'index':idx,'coordinate_rel_mismatch':rel,'k_key':kkey,'native_table_count':int(len(k))}


def interp_rules(c,z,target,nodes):
    j=int(np.searchsorted(nodes,target))
    if j<2 or j>len(nodes)-2:
        raise FloatingPointError('target lacks frozen local stencil')
    lo=float(nodes[j-1]); hi=float(nodes[j])
    if min(abs(target-lo),abs(hi-target))/abs(target)<=je.TARGET_COINCIDENCE_REL:
        raise AssertionError('target accidentally coincides with fixed node')
    qs=[float(nodes[j-2]),lo,hi,float(nodes[j+1])]
    vals=[]; prov=[]
    for q in qs:
        v,p=node_value(c,z,q); vals.append(v); prov.append(p)
    x=[math.log(q) for q in qs]; xt=math.log(float(target))
    t=(xt-math.log(lo))/(math.log(hi)-math.log(lo))
    linear=float(vals[1]+t*(vals[2]-vals[1]))
    out={
        'linear_bracket':linear,
        'quadratic_left':lagrange_eval(x[:3],vals[:3],xt),
        'quadratic_right':lagrange_eval(x[1:],vals[1:],xt),
        'cubic_centered':lagrange_eval(x,vals,xt),
    }
    return out,{'stencil_requested':qs,'stencil':prov,'target':float(target),'bracket_fraction_log':float(t)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--baseline',required=True)
    ap.add_argument('--precision',required=True)
    ap.add_argument('--capacity-patch-record',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    from classy import Class
    patch=json.loads(Path(a.capacity_patch_record).read_text())
    if patch.get('old_capacity')!=30 or patch.get('new_capacity')!=512 or patch.get('replacement_count')!=1:
        raise SystemExit('invalid k-output capacity patch record')
    if patch.get('parser_old_argument_capacity')!=1024 or patch.get('parser_new_argument_capacity')!=32768 or patch.get('parser_replacement_count')!=1:
        raise SystemExit('invalid parser capacity patch record')
    result={
        'schema':'EXP073JG_ARTICLE3_LAYERB_LOCAL_INTERPOLATION_CURVATURE_RESULT_V0_1',
        'experiment':'Exp073JG','classification':'INVALID_INFRA_PLUS_0_PLUS_0','effect':'+0/+0',
        'scientific_authority_created':False,'covariance_restriction_authorized':False,
        'h':je.H,'rel_tol':je.REL_TOL,'fixed_k_min':je.KMIN,'fixed_k_max':je.KMAX,
        'node_count':N,'k_per_decade_ladder':list(je.KPDS),'rules':list(RULES),
        'capacity_patch':patch,'observations':{},'parent_reproduction':{}
    }
    try:
        nodes=np.geomspace(je.KMIN,je.KMAX,N,dtype=np.float64)
        for _,_,target,_ in je.PROBES:
            if float(np.min(np.abs(nodes-target))/abs(target)) <= je.TARGET_COINCIDENCE_REL:
                raise AssertionError('target accidentally coincides with fixed node')
        for kpd in je.KPDS:
            key=format(kpd,'.17g'); cs={}
            try:
                for name,alpha,beta in je.MODELS:
                    c=Class(); c.set(je.class_params(a.baseline,a.precision,alpha,beta,kpd,nodes)); c.compute(['transfer']); cs[name]=c
                krec={}
                for pname,z,target,exact in je.PROBES:
                    model_vals={}; model_prov={}
                    for name,_,_ in je.MODELS:
                        model_vals[name],model_prov[name]=interp_rules(cs[name],z,target,nodes)
                    rrec={}
                    for rule in RULES:
                        vals={name:model_vals[name][rule] for name,_,_ in je.MODELS}
                        if pname=='alpha_left': signed=(vals['alpha_left']-vals['ref'])/(-je.H)
                        else: signed=(vals['beta_plus']-vals['beta_minus'])/(2*je.H)
                        response=abs(float(signed)); err=je.reldiff(response,exact)
                        rrec[rule]={
                            'response':response,'signed_response':float(signed),'exact_k_reference':exact,
                            'relative_error_to_exact_k':err,'below_rel_tol_reference':bool(err is not None and err<je.REL_TOL),
                            'signed_response_delta_from_linear':None
                        }
                    linear_signed=rrec['linear_bracket']['signed_response']
                    for rule in RULES[1:]:
                        rrec[rule]['signed_response_delta_from_linear']=float(rrec[rule]['signed_response']-linear_signed)
                    parent=PARENT_RESPONSES[pname]
                    if rrec['linear_bracket']['response'] != parent:
                        raise AssertionError(f'linear parent mismatch {pname} kpd={key}: {rrec["linear_bracket"]["response"]!r} != {parent!r}')
                    result['parent_reproduction'].setdefault(key,{})[pname]=True
                    krec[pname]={'rules':rrec,'model_provenance':model_prov}
                result['observations'][key]=krec
            finally:
                for c in cs.values():
                    try: c.struct_cleanup()
                    except Exception: pass
        candidates=[]
        for rule in RULES:
            allok=True; cross={}
            for pname,_,_,_ in je.PROBES:
                r10=result['observations']['10'][pname]['rules'][rule]['response']
                r20=result['observations']['20'][pname]['rules'][rule]['response']
                kd=je.reldiff(r10,r20)
                cross[pname]={'relative_difference':kd,'below_rel_tol_reference':bool(kd is not None and kd<je.REL_TOL)}
                allok=(allok and result['observations']['10'][pname]['rules'][rule]['below_rel_tol_reference']
                       and result['observations']['20'][pname]['rules'][rule]['below_rel_tol_reference']
                       and bool(kd is not None and kd<je.REL_TOL))
            result.setdefault('rule_summary',{})[rule]={'kpd_crosscheck':cross,'curvature_candidate':bool(allok)}
            if allok: candidates.append(rule)
        result['curvature_candidates']=candidates
        result['classification']='LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0'
        result['token']='PASS_EXP073JG_LOCAL_INTERPOLATION_CURVATURE_OBSERVED_V0_1'
    except Exception as e:
        result['error']=repr(e)
        result['token']='INVALID_EXP073JG_LOCAL_INTERPOLATION_CURVATURE_V0_1'
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token'])
    if result['classification']=='LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0':
        print('CURVATURE_CANDIDATES',result['curvature_candidates'])
        for rule in RULES:
            print('RULE',rule,'SUMMARY',result['rule_summary'][rule])
            for kpd in ('10','20'):
                print('ERR',rule,kpd,'alpha',result['observations'][kpd]['alpha_left']['rules'][rule]['relative_error_to_exact_k'],
                      'beta',result['observations'][kpd]['beta_symmetric']['rules'][rule]['relative_error_to_exact_k'])
    else:
        print('ERROR',result.get('error'))
    raise SystemExit(0 if result['classification']=='LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0' else 2)

if __name__=='__main__': main()
