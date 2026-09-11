#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json
from pathlib import Path
import numpy as np

PASS='LAYERB_16385_INTRA_VM_ROLE_REPEATABILITY_PASS_PLUS_0_PLUS_0'
FAIL='LAYERB_16385_INTRA_VM_ROLE_REPEATABILITY_FAIL_PLUS_0_PLUS_0'

def load(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path)); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def sha(a): return hashlib.sha256(np.ascontiguousarray(a,dtype='<f8').tobytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--role',required=True,choices=['reference','alpha_minus','beta_plus','beta_minus'])
    for x in ('role-script','canonical-authority','fine','jo-script','jj-script','baseline','precision','capacity-patch-record','out'):
        ap.add_argument('--'+x,required=True)
    a=ap.parse_args(); out=Path(a.out)
    try:
        rp=load('rp',a.role_script); jo=load('jo',a.jo_script); jj=load('jj',a.jj_script)
        rp.validate_authority(a.canonical_authority); rp.validate_patch(a.capacity_patch_record); nodes=rp.load_nodes(a.fine)
        assert rp.H==jo.H==jj.H==1e-4 and jj.LOOKUP_REL_TOL==1e-12
        jj.CAPACITY=rp.CAPACITY
        alpha,beta=rp.MODELS[a.role]
        from classy import Class
        repeats=[]; max_lookup=0.0; unsupported=0
        for rep in range(2):
            c=None; rec={'repeat':rep+1,'requests':{}}
            try:
                c=Class(); c.set(jj.class_params(Path(a.baseline),Path(a.precision),alpha,beta,nodes)); c.compute(['transfer'])
                for q,z,targets in rp.REQUESTS:
                    v,valid,mx,key=jo.evaluate(jj,c,nodes,z,targets); v=np.ascontiguousarray(v,dtype='<f8')
                    u=int(np.count_nonzero(~valid)); unsupported+=u; max_lookup=max(max_lookup,float(mx))
                    rec['requests'][q]={'values':[float(x) for x in v],'payload_sha256':sha(v),'unsupported':u,'max_lookup':float(mx),'k_key':str(key),'z_binary64_hex':float(z).hex()}
            finally:
                if c is not None:
                    try:c.struct_cleanup()
                    except Exception:pass
            repeats.append(rec)
        cmp={}
        for q in ('A','B'):
            x=np.asarray(repeats[0]['requests'][q]['values']); y=np.asarray(repeats[1]['requests'][q]['values']); d=np.abs(x-y); den=np.maximum(np.maximum(np.abs(x),np.abs(y)),np.finfo(float).tiny)
            cmp[q]={'sha_equal':repeats[0]['requests'][q]['payload_sha256']==repeats[1]['requests'][q]['payload_sha256'],'max_absolute_difference':float(d.max()),'max_symmetric_relative_difference':float((d/den).max()),'rms_absolute_difference':float(np.sqrt(np.mean(d*d)))}
        passed=unsupported==0 and max_lookup<=1e-12
        result={'schema':'LAYERB_16385_INTRA_VM_ROLE_REPEATABILITY_RESULT_V0_1','classification':PASS if passed else FAIL,'effect':'+0/+0','role':a.role,'canonical_node_sha256':rp.NODE_SHA,'canonical_text_sha256':rp.TEXT_SHA,'repeat_count':2,'total_solver_constructions':2,'max_live_instances':1,'final_live_instances':0,'unsupported_target_evaluations':unsupported,'max_requested_node_coordinate_rel_mismatch':max_lookup,'repeats':repeats,'repeat_comparison':cmp,'all_operand_hashes_equal_between_repeats':all(cmp[q]['sha_equal'] for q in cmp),'current_16385_scientific_result_read':False,'full_107_row_traversal_executed':False,'scientific_authority_created':False,'stopping_rule_changed':False,'next_rung_authorized':False,'token':PASS if passed else FAIL}
    except Exception as e:
        result={'schema':'LAYERB_16385_INTRA_VM_ROLE_REPEATABILITY_RESULT_V0_1','classification':FAIL,'effect':'+0/+0','role':a.role,'current_16385_scientific_result_read':False,'full_107_row_traversal_executed':False,'scientific_authority_created':False,'error':f'{type(e).__name__}: {e}','token':FAIL}
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token'],a.role); return 0
if __name__=='__main__': raise SystemExit(main())
