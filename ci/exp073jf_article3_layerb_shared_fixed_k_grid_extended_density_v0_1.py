#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import exp073je_article3_layerb_shared_fixed_k_grid_scaling_v0_1 as je

NS=(384,512)


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
        'schema':'EXP073JF_ARTICLE3_LAYERB_SHARED_FIXED_K_GRID_EXTENDED_DENSITY_RESULT_V0_1',
        'experiment':'Exp073JF','classification':'INVALID_INFRA_PLUS_0_PLUS_0','effect':'+0/+0',
        'scientific_authority_created':False,'covariance_restriction_authorized':False,
        'h':je.H,'rel_tol':je.REL_TOL,'fixed_k_min':je.KMIN,'fixed_k_max':je.KMAX,
        'node_counts':list(NS),'k_per_decade_ladder':list(je.KPDS),'capacity_patch':patch,'observations':{}
    }
    try:
        for n in NS:
            nodes=np.geomspace(je.KMIN,je.KMAX,n,dtype=np.float64)
            for _,_,target,_ in je.PROBES:
                if float(np.min(np.abs(nodes-target))/abs(target)) <= je.TARGET_COINCIDENCE_REL:
                    raise AssertionError(f'target accidentally coincides with fixed node N={n}')
            nrec=result['observations'][str(n)]={'by_kpd':{},'scaling_candidate':False}
            for kpd in je.KPDS:
                cs={}
                try:
                    for name,alpha,beta in je.MODELS:
                        c=Class(); c.set(je.class_params(a.baseline,a.precision,alpha,beta,kpd,nodes)); c.compute(['transfer']); cs[name]=c
                    prec={}
                    for pname,z,target,exact in je.PROBES:
                        vals={}; provenance={}
                        for name,_,_ in je.MODELS:
                            vals[name],provenance[name]=je.fixed_interp(cs[name],z,target,nodes)
                        if pname=='alpha_left': signed=(vals['alpha_left']-vals['ref'])/(-je.H)
                        else: signed=(vals['beta_plus']-vals['beta_minus'])/(2*je.H)
                        response=abs(float(signed)); err=je.reldiff(response,exact)
                        prec[pname]={'response':response,'signed_response':float(signed),'exact_k_reference':exact,
                                    'relative_error_to_exact_k':err,'below_rel_tol_reference':bool(err is not None and err<je.REL_TOL),
                                    'model_provenance':provenance}
                    nrec['by_kpd'][format(kpd,'.17g')]=prec
                finally:
                    for c in cs.values():
                        try: c.struct_cleanup()
                        except Exception: pass
            allok=True
            for pname,_,_,_ in je.PROBES:
                r10=nrec['by_kpd']['10'][pname]['response']; r20=nrec['by_kpd']['20'][pname]['response']; kd=je.reldiff(r10,r20)
                nrec.setdefault('kpd_crosscheck',{})[pname]={'relative_difference':kd,'below_rel_tol_reference':bool(kd is not None and kd<je.REL_TOL)}
                allok=(allok and nrec['by_kpd']['10'][pname]['below_rel_tol_reference']
                       and nrec['by_kpd']['20'][pname]['below_rel_tol_reference']
                       and bool(kd is not None and kd<je.REL_TOL))
            nrec['scaling_candidate']=bool(allok)
        candidates=[n for n in NS if result['observations'][str(n)]['scaling_candidate']]
        result['scaling_candidates']=candidates; result['smallest_scaling_candidate']=min(candidates) if candidates else None
        result['classification']='SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0'
        result['token']='PASS_EXP073JF_SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_V0_1'
    except Exception as e:
        result['error']=repr(e); result['token']='INVALID_EXP073JF_SHARED_FIXED_K_GRID_EXTENDED_DENSITY_V0_1'
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['classification']=='SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0' else 2)

if __name__=='__main__': main()
