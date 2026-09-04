#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, json, subprocess
from pathlib import Path

SCHEMA='dsir.exp073cx.wm_s3.activation_readiness.v0.3'
PREREG='experiments/073cx_wm_s3_activation_readiness_v0_3_prereg.md'
BU='experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md'
CW='ci/exp073cw_single_mask_integrated_driver_v0_1.py'
CV='ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py'
DRIVER='ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py'
CZREC='recovery/2026-09-04_exp073cz_v0_2_z1_scoped_driver_integration_pass.md'
EXPECTED={PREREG:'deee125339cd8725db4cbcf0449296322e81cb47',BU:'816542c7eb7a8ba4e72d6e01228aa62d05c7c805',CW:'f61b4e42ace7e2ab7220c0df0b38d8663136896c',CV:'dafe86086a470c852106f0d4ecccbda1d389e397',DRIVER:'5c8d5d3463e455389a1ca3df2639bf06a3b7b603',CZREC:'140b65be4901af3893a75f770ab20a9eed9f2f14'}
AUTH={
 'cw':('a763a83275c4105903b0dbee272a9ca72fc61ca0','recovery/2026-09-04_exp073cw_v0_1_h1_single_mask_integrated_driver_pass.md',['H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS','33860891989 / 100984835847','9932088071','historical_wm_s3_numerical_import=false']),
 'cv':('df49dcb50d5ccffb7b29d030ed8f1f99cbf4cdd6','recovery/2026-09-04_exp073cv_v0_3_i1_exact_production_integration_pass.md',['I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS','33847132443 / 100941396500 / 77cc6ba35aac41d2f6af12c7b865787db2bb3e44','9926971841','historical_wm_s3_numerical_import=false']),
 'cz':('d0f70ac07707af960d2accd708ea1064fc05f523','recovery/2026-09-04_exp073cz_v0_2_z1_scoped_driver_integration_pass.md',['Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS','33871304159 / 101017678531 / b7cc90467006718a115b4dba40962cc8275f1c69','9935990587','03938c3b2f2759a60be1f4d5bfdd6eb23018e9507e0a6688ba20364e02eaa5b1'])}
EDGES=[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
ORDER=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']
NAMESPACES=['checkpoints/exp073bu-wm-s3-a-v0-1','checkpoints/exp073bu-wm-s3-b-v0-1']
THREADS={'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'}

def git_blob(p): return subprocess.check_output(['git','hash-object',p],text=True).strip()
def ancestor(commit,head): return subprocess.run(['git','merge-base','--is-ancestor',commit,head]).returncode==0
def frozen_text(commit,path): return subprocess.check_output(['git','show',f'{commit}:{path}'],text=True)
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
 ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); ap.add_argument('--source-head',required=True); a=ap.parse_args()
 r={'schema':SCHEMA,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'source_head':a.source_head,'no_des_scale_numerics_executed':True,'no_tolerance_rescue':True,'checks':{}}
 try:
  blobs={p:git_blob(p) for p in EXPECTED}; r['blob_ids']=blobs; c=r['checks']; c['blob_binding']=all(blobs[p]==v for p,v in EXPECTED.items())
  if not c['blob_binding']: r['status']='A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL'
  else:
   auth={}; texts={}
   for name,(commit,path,tokens) in AUTH.items():
    ok_ancestor=ancestor(commit,a.source_head); txt=frozen_text(commit,path) if ok_ancestor else ''; texts[name]=txt
    auth[name]={'commit':commit,'ancestor':ok_ancestor,'tokens':all(t in txt for t in tokens)}
   r['authorities']=auth; c['immutable_authorities']=all(x['ancestor'] and x['tokens'] for x in auth.values())
   drv=Path(DRIVER).read_text(); compact=drv.replace(' ',''); low=drv.lower(); bu=Path(BU).read_text(); pr=Path(PREREG).read_text(); tree=ast.parse(drv); funcs={n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}; run=funcs.get('run_replica'); cmpf=funcs.get('compare_replicas'); run_calls=[call_name(x) for x in ast.walk(run) if isinstance(x,ast.Call)] if run else []; cmp_src=ast.unparse(cmpf) if cmpf else ''
   c['no_historical_import']=("'historical_wm_s3_numerical_import':False" in compact and "'other_replica_output_read':False" in compact and not any(x in low for x in ['exp073cr','exp073cq','exp073cm']))
   c['frozen_edges']=repr(EDGES).replace(' ','') in compact and '39 bands' in pr and '12288' in bu
   c['namespace_isolation']=all(x in drv for x in NAMESPACES)
   c['checkpoint_order']=all(repr(x) in drv for x in ORDER) and drv.index("'fresh_masks_complete'")<drv.index("'fresh_workspace_mcm_complete'")<drv.index("'mcm_fits_verified'")<drv.index("'full_window_complete'")<drv.index("'selected_te_complete'")<drv.index("'replica_receipt_complete'")
   c['failclosed_identity']=all(x in drv for x in ['fail-closed checkpoint identity mismatch','source_head','contract_fingerprint','checkpoint_namespace'])
   c['single_field_handoff']=run_calls.count('nmt.NmtField')==2 and 'f0.get_mask_alms()' in drv and 'f2.get_mask_alms()' in drv and 'w.compute_coupling_matrix(f0,f2,b)' in compact
   c['stock_persistence_exact_route']='.write_to(str(workspace_path))' in drv and '.get_coupling_matrix(' not in drv and 'execute_exact_adapter' in run_calls and 'wins[0,:,0,:] = TE<-TE' in drv
   c['exact_comparator']=("a['selected_te_sha256']==b['selected_te_sha256']" in cmp_src.replace(' ','') and 'np.array_equal' in cmp_src and all(x not in drv for x in ['allclose','isclose','rtol','atol']))
   c['execution_contract']='OUTER_COMPUTE_WORKERS=8' in compact and all((repr(k)+':'+repr(v)) in compact for k,v in THREADS.items())
   c['hosted_non_science']=all(x in texts['cz'] for x in ['science_gate_scored=false','wm_s3_authority_created=false','exp073bu_activated=false'])
   if not c['immutable_authorities']: r['status']='A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL'
   elif not c['no_historical_import']: r['status']='A4_HISTORICAL_IMPORT_FAIL'
   elif not all(c[k] for k in ['namespace_isolation','checkpoint_order','failclosed_identity','exact_comparator']): r['status']='A3_CHECKPOINT_FAILCLOSED_FAIL'
   elif not all(c[k] for k in ['frozen_edges','single_field_handoff','stock_persistence_exact_route','execution_contract','hosted_non_science']): r['status']='A2_IMPLEMENTATION_CONTRACT_FAIL'
   else: r['status']='A1_EXP073BU_ACTIVATION_READINESS_PASS'
 except Exception as e:
  r['status']='A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL'; r['error']=repr(e)
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(r['status']); print(json.dumps(r,indent=2,sort_keys=True)); return 0 if r['status'] in {'A1_EXP073BU_ACTIVATION_READINESS_PASS','A2_IMPLEMENTATION_CONTRACT_FAIL','A3_CHECKPOINT_FAILCLOSED_FAIL','A4_HISTORICAL_IMPORT_FAIL'} else 4
if __name__=='__main__': raise SystemExit(main())
