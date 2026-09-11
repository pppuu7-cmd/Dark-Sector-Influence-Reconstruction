#!/usr/bin/env python3
from __future__ import annotations
import argparse,importlib.util,json,hashlib
from pathlib import Path
import numpy as np
H=1e-4
LOOKUP_REL_TOL=1e-12
PASS='CANONICAL_16385_CROSS_VM_NUMERIC_REPRO_PROBE_PASS_PLUS_0_PLUS_0'
FAIL='CANONICAL_16385_CROSS_VM_NUMERIC_REPRO_PROBE_FAIL_PLUS_0_PLUS_0'

def load(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path)); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def sha(a): return hashlib.sha256(np.ascontiguousarray(a,dtype='<f8').tobytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    for x in ('resource-script','canonical-authority','fine','jo-script','jj-script','baseline','precision','capacity-patch-record','out'):
        ap.add_argument('--'+x,required=True)
    a=ap.parse_args(); out=Path(a.out)
    try:
        rp=load('rp',a.resource_script); jo=load('jo',a.jo_script); jj=load('jj',a.jj_script)
        auth=rp.validate_authority(a.canonical_authority); rp.validate_patch(a.capacity_patch_record); nodes=rp.load_nodes(a.fine)
        assert rp.H==H and jo.H==H and jj.H==H and jj.LOOKUP_REL_TOL==LOOKUP_REL_TOL
        jj.CAPACITY=rp.CAPACITY
        from classy import Class
        raw={q:{} for q,_,_ in jo.REQUESTS}; receipts=[]; tracker={'constructions':0,'live':0,'max_live':0}; unsupported=0; lookup=0.0
        for role,alpha,beta in jo.MODELS:
            c=None; tracker['constructions']+=1; tracker['live']+=1; tracker['max_live']=max(tracker['max_live'],tracker['live'])
            try:
                c=Class(); c.set(jj.class_params(Path(a.baseline),Path(a.precision),alpha,beta,nodes)); c.compute(['transfer'])
                rr={'role':role,'requests':{}}
                for q,z,targets in jo.REQUESTS:
                    v,valid,mx,key=jo.evaluate(jj,c,nodes,z,targets); v=np.ascontiguousarray(v,dtype='<f8'); raw[q][role]=v
                    u=int(np.count_nonzero(~valid)); unsupported+=u; lookup=max(lookup,float(mx))
                    rr['requests'][q]={'z_binary64_hex':float(z).hex(),'k_key':key,'target_count':int(targets.size),'values':[float(x) for x in v],'payload_sha256':sha(v),'unsupported':u,'max_lookup':float(mx)}
                receipts.append(rr)
            finally:
                if c is not None:
                    try:c.struct_cleanup()
                    except Exception:pass
                tracker['live']-=1
        responses={}
        for q,_,_ in jo.REQUESTS:
            ref,am,bp,bm=(raw[q][r] for r in ('reference','alpha_minus','beta_plus','beta_minus'))
            r=np.ascontiguousarray(np.column_stack((np.abs((am-ref)/(-H)),np.abs((bp-bm)/(2*H)))),dtype='<f8')
            responses[q]={'values':[[float(x) for x in row] for row in r],'payload_sha256':sha(r),'shape':list(r.shape),'finite':bool(np.all(np.isfinite(r)))}
        ok=tracker=={'constructions':4,'live':0,'max_live':1} and unsupported==0 and lookup<=LOOKUP_REL_TOL and all(x['finite'] for x in responses.values())
        result={'schema':'LAYERB_16385_CROSS_VM_NUMERIC_REPRO_PROBE_RESULT_V0_1','classification':PASS if ok else FAIL,'effect':'+0/+0','canonical_authority_run_id':auth.get('run_id'),'canonical_node_sha256':rp.NODE_SHA,'canonical_text_sha256':rp.TEXT_SHA,'role_order':[r for r,_,_ in jo.MODELS],'model_receipts':receipts,'pilot_responses':responses,'execution_lifecycle':{'total_solver_constructions':tracker['constructions'],'max_live_instances':tracker['max_live'],'final_live_instances':tracker['live']},'unsupported_target_evaluations':unsupported,'max_requested_node_coordinate_rel_mismatch':lookup,'current_16385_scientific_result_read':False,'jm_result_read':False,'full_107_row_traversal_executed':False,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':PASS if ok else FAIL}
    except Exception as e:
        result={'schema':'LAYERB_16385_CROSS_VM_NUMERIC_REPRO_PROBE_RESULT_V0_1','classification':FAIL,'effect':'+0/+0','current_16385_scientific_result_read':False,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'error':f'{type(e).__name__}: {e}','token':FAIL}
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token']); return 0
if __name__=='__main__': raise SystemExit(main())
