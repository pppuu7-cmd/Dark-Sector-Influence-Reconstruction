#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,py_compile,tempfile
ROOT=Path(__file__).resolve().parents[1]
DRV=ROOT/'ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py'; PR=ROOT/'experiments/073dr_ww_s0_s0_activation_resource_preflight_v0_1_prereg.md'; OUT=ROOT/'exp073dr_ww_s0_s0_activation_resource_preflight_v0_1.json'; PASS='PASS_EXP073DR_WW_S0_S0_HOSTED_ACTIVATION_RESOURCE_PREFLIGHT_V0_1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 d=DRV.read_text(); p=PR.read_text(); compile_ok=True
 try:
  with tempfile.TemporaryDirectory() as td: py_compile.compile(str(DRV),cfile=str(Path(td)/'x.pyc'),doraise=True)
 except Exception: compile_ok=False
 checks={'dq_parent_bound':all(x in p for x in ['33938583879 / 101231302981','9961000737','93a3db6b27ee9fba9f4d0549b9d6e03c2a50cb7f6ad224c41e773a85b969682c','0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b']),'dp_parent_bound':all(x in p for x in ['33938446310 / 101230897808','9960969007','e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8','24365fa59a38c15732f4f37e8b29265b75c442d5']),'syntax_compile':compile_ok,'s0_only_imports':'source_count_map, validate_r1' in d and 'execute_ww_adapter' in d and 'reconstruct_lens_mask' not in d,'dedicated_ab':all(x in d for x in ['checkpoints/exp073dq-ww-s0-s0-a-v0-1','checkpoints/exp073dq-ww-s0-s0-b-v0-1']),'workspace_complete_stage':all(x in d for x in ["w.compute_coupling_matrix(f,f,b)","w.write_to(str(wp))","fresh_workspace_mcm_complete","fail-closed workspace restore SHA mismatch"]),'same_field_auto':"w.compute_coupling_matrix(f,f,b)" in d and "'same_field_object_handoff':True" in d,'exact_ww_route':all(x in d for x in ['ncls=4','[4,39,4,12288]','selected_ee.bin','EE<-EE']),'exact_comparator':'np.array_equal(aa,bb)' in d and "'no_tolerance_rescue':True" in d,'home_preflight_required':'self-hosted environment/exclusivity preflight' in p.lower(),'no_home_science_auth':'not the a/b scientific computation' in p.lower()}
 if not all(checks.values()):raise SystemExit('BLOCKED_EXP073DR_WW_S0_S0_HOSTED_ACTIVATION_RESOURCE_PREFLIGHT '+json.dumps([k for k,v in checks.items() if not v]))
 rec={'experiment':'Exp073DR','classification':'SUPPORT_HOSTED_ACTIVATION_RESOURCE_PASS_PLUS_0_PLUS_0','token':PASS,'science_gate_scored':False,'ww_authority_created':False,'home_science_execution_authorized':False,'home_readiness_preflight_authorized':True,'checks':checks,'sha256':{'driver':sha(DRV),'prereg':sha(PR)},'next_gate':'tiny self-hosted environment/exclusivity preflight; no full workspace'};OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n');print(PASS)
if __name__=='__main__':main()
