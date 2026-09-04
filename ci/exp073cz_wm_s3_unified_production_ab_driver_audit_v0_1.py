#!/usr/bin/env python3
from __future__ import annotations
import ast, argparse, hashlib, json
from pathlib import Path

EDGES=[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
ORDER=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']
NAMESPACES={'A':'checkpoints/exp073bu-wm-s3-a-v0-1','B':'checkpoints/exp073bu-wm-s3-b-v0-1'}
THREADS={'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'}

def blob_sha(path:Path):
    b=path.read_bytes(); return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()

def calls_in(fn):
    return [n for n in ast.walk(fn) if isinstance(n,ast.Call)]
def call_name(c):
    f=c.func
    if isinstance(f,ast.Name): return f.id
    if isinstance(f,ast.Attribute):
        parts=[]
        while isinstance(f,ast.Attribute): parts.append(f.attr); f=f.value
        if isinstance(f,ast.Name): parts.append(f.id)
        return '.'.join(reversed(parts))
    return ''

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--driver',required=True); ap.add_argument('--prereg',required=True); ap.add_argument('--fresh-helper',required=True); ap.add_argument('--adapter',required=True); ap.add_argument('--expected-driver-blob',required=True); ap.add_argument('--expected-prereg-blob',required=True); ap.add_argument('--expected-fresh-blob',required=True); ap.add_argument('--expected-adapter-blob',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    p=Path(a.driver); src=p.read_text(); tree=ast.parse(src); funcs={n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
    provenance={
      'driver_blob':blob_sha(p)==a.expected_driver_blob,
      'prereg_blob':blob_sha(Path(a.prereg))==a.expected_prereg_blob,
      'fresh_helper_blob':blob_sha(Path(a.fresh_helper))==a.expected_fresh_blob,
      'adapter_blob':blob_sha(Path(a.adapter))==a.expected_adapter_blob,
    }
    run=funcs.get('run_replica'); cmpf=funcs.get('compare_replicas'); maskf=funcs.get('fresh_or_restore_masks')
    run_calls=[call_name(c) for c in calls_in(run)] if run else []
    mask_calls=[call_name(c) for c in calls_in(maskf)] if maskf else []
    checks={
      'exact_edges':repr(EDGES).replace(' ','') in src.replace(' ',''),
      'checkpoint_order':all(repr(x) in src for x in ORDER) and src.index("'fresh_masks_complete'") < src.index("'fresh_workspace_mcm_complete'") < src.index("'mcm_fits_verified'") < src.index("'full_window_complete'") < src.index("'selected_te_complete'") < src.index("'replica_receipt_complete'"),
      'isolated_namespaces':all(v in src for v in NAMESPACES.values()),
      'reconstruct_lens_once_in_mask_builder':mask_calls.count('reconstruct_lens_mask')==1,
      'reconstruct_source_once_in_mask_builder':mask_calls.count('reconstruct_s3_count_map')==1,
      'exactly_two_field_constructors':run_calls.count('nmt.NmtField')==2,
      'same_fields_feed_workspace':"w.compute_coupling_matrix(f0,f2,b)" in src.replace(' ',''),
      'same_fields_feed_pcl':"f0.get_mask_alms()" in src and "f2.get_mask_alms()" in src,
      'stock_write_to':'.write_to(str(workspace_path))' in src,
      'no_get_coupling_matrix_materialization':'.get_coupling_matrix(' not in src,
      'adapter_composed':'execute_exact_adapter' in run_calls,
      'te_semantics':'wins[0,:,0,:] = TE<-TE' in src,
      'exact_sha_comparator':"a['selected_te_sha256']==b['selected_te_sha256']" in src.replace(' ',''),
      'numpy_array_equal':'np.array_equal' in ast.unparse(cmpf) if cmpf else False,
      'no_tolerance_rescue':all(x not in src for x in ['allclose','isclose','rtol','atol']),
      'worker_contract':'OUTER_COMPUTE_WORKERS=8' in src.replace(' ',''),
      'nested_threads':all((repr(k)+':'+repr(v)) in src.replace(' ','') for k,v in THREADS.items()),
      'failclosed_identity':'fail-closed checkpoint identity mismatch' in src,
      'resume_final_before_expensive':src.index('validated_finished_receipt(root') < src.index("load_manifest(root,'fresh_workspace_mcm_complete'") < src.index('fresh_or_restore_masks(root'),
      'source_head_binding':'source_head' in src and 'contract_fingerprint' in src,
      'historical_import_false':"'historical_wm_s3_numerical_import':False" in src,
      'cross_replica_false':"'other_replica_output_read':False" in src,
    }
    if not all(provenance.values()): status='Z4_PROVENANCE_BINDING_FAIL'
    elif not checks['exact_sha_comparator'] or not checks['numpy_array_equal'] or not checks['checkpoint_order'] or not checks['failclosed_identity']: status='Z3_EXACT_COMPARATOR_OR_CHECKPOINT_FAIL'
    elif not all(checks.values()): status='Z2_IMPLEMENTATION_CONTRACT_FAIL'
    else: status='Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS'
    out={'schema':'dsir.exp073cz.wm_s3.unified_production_ab_driver_audit.v0.1','status':status,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'source_head':a.source_head,'provenance':provenance,'checks':checks,'frozen_edges':EDGES,'checkpoint_order':ORDER,'namespaces':NAMESPACES,'no_des_scale_numerics_executed':True}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0 if status.startswith('Z1_') else 3)
if __name__=='__main__': main()
