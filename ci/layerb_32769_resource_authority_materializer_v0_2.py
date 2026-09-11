#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

RESOURCE_PASS="LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
IND_PASS="LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
PROV_PASS="LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_PASS_PLUS_0_PLUS_0"
FAIL="LAYERB_32769_RESOURCE_AUTHORITY_MATERIALIZATION_NOT_VALID_PLUS_0_PLUS_0"
CONTRACT_BLOB="3e53992864ad10f23752df03a653f8073cc18ffa"
ROLES=["reference","alpha_minus","beta_plus","beta_minus"]

def bound(p):
    b=Path(p).read_bytes(); return json.loads(b),hashlib.sha256(b).hexdigest(),hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def synth(d): return d.get("synthetic_fixture") is True or d.get("synthetic_only") is True
def pos(x): return isinstance(x,int) and x>0
def sha256(x): return isinstance(x,str) and len(x)==64 and all(c in "0123456789abcdef" for c in x)
def gitsha(x): return isinstance(x,str) and len(x)==40 and all(c in "0123456789abcdef" for c in x)

def main():
    ap=argparse.ArgumentParser()
    for k in ("contract","source-result","independent-validation","provenance","out"): ap.add_argument("--"+k,required=True)
    a=ap.parse_args(); e=[]
    c,csha,cblob=bound(a.contract); src,ssha,sblob=bound(a.source_result); ind,isha,iblob=bound(a.independent_validation); prov,psha,pblob=bound(a.provenance)
    if cblob!=CONTRACT_BLOB: e.append("contract_blob")
    if c.get("output_classification_if_all_checks_pass")!=RESOURCE_PASS or c.get("authority_created_by_contract_file_itself") is not False or c.get("high_memory_resource_lifecycle_preflight_pass") is not False or c.get("materialization_requires_real_non_synthetic_inputs") is not True: e.append("contract_semantics")
    for label,d in (("source",src),("independent",ind),("provenance",prov)):
        if synth(d): e.append(label+"_marked_synthetic")
    ident=c["required_source_identity"]
    if src.get("classification")!=RESOURCE_PASS: e.append("source_classification")
    if src.get("canonical_32769_node_sha256")!=ident["canonical_32769_node_sha256"] or src.get("canonical_32769_text_sha256")!=ident["canonical_32769_text_sha256"]: e.append("source_canonical")
    if src.get("capacity")!=ident["point_capacity"] or src.get("parser_capacity")!=ident["parser_capacity"]: e.append("source_capacity")
    if src.get("build_authority_classification")!=ident["class_build_authority_classification"]: e.append("source_build")
    if src.get("runner_isolation_contract_git_blob")!=ident["runner_isolation_contract_git_blob"] or src.get("required_custom_label")!=ident["required_custom_label"] or src.get("runner_registration_evidence_valid") is not True: e.append("source_runner")
    mem=src.get("candidate_memtotal_kb")
    if not isinstance(mem,int) or mem<=ident["candidate_memtotal_kb_must_be_strictly_greater_than"] or src.get("candidate_strictly_higher_memory_than_exhausted_hosted") is not True: e.append("source_memory")
    life=src.get("execution_lifecycle",{})
    if life.get("total_solver_constructions")!=ident["total_solver_constructions"] or life.get("max_live_instances")!=ident["max_live_instances"] or life.get("final_live_instances")!=ident["final_live_instances"]: e.append("source_lifecycle")
    if src.get("role_order")!=ROLES: e.append("source_role_order")
    rr=src.get("role_receipts")
    if not isinstance(rr,list) or len(rr)!=4 or [x.get("role") for x in rr]!=ROLES or any(x.get("compute_completed") is not True for x in rr): e.append("source_role_receipts")
    else:
        if any(x.get("scientific_transfer_values_read") is not False or x.get("scientific_response_computed") is not False or x.get("scientific_response_serialized") is not False for x in rr): e.append("source_role_response_blind")
    for k,v in c["required_response_blind_bits"].items():
        if src.get(k)!=v: e.append("source_"+k)
    if ind.get("classification")!=IND_PASS or ind.get("valid") is not True or ind.get("errors")!=[]: e.append("independent_validity")
    if ind.get("source_result_sha256")!=ssha or ind.get("candidate_memtotal_kb")!=mem or ind.get("execution_lifecycle")!=life or ind.get("parser_capacity")!=ident["parser_capacity"]: e.append("independent_binding")
    if ind.get("runner_agent_id")!=src.get("runner_agent_id") or ind.get("runner_name")!=src.get("runner_name"): e.append("independent_runner_binding")
    if ind.get("scientific_response_read") is not False or ind.get("scientific_authority_created") is not False or ind.get("successor_execution_authorized") is not False: e.append("independent_response_blind")
    if prov.get("classification")!=c.get("required_provenance_classification",PROV_PASS) or prov.get("valid") is not True or prov.get("errors")!=[]: e.append("provenance_validity")
    if prov.get("packaging_contract_git_blob")!=c.get("required_provenance_packaging_contract_git_blob"): e.append("provenance_contract_binding")
    req=c.get("required_provenance_receipt_fields",[])
    if any(k not in prov for k in req): e.append("provenance_fields")
    for k in ("source_run_id","source_job_id","source_artifact_id","independent_run_id","independent_job_id","independent_artifact_id"):
        if not pos(prov.get(k)): e.append("provenance_"+k)
    for k in ("source_head_sha","independent_head_sha"):
        if not gitsha(prov.get(k)): e.append("provenance_"+k)
    for k in ("source_artifact_zip_sha256","independent_artifact_zip_sha256"):
        if not sha256(prov.get(k)): e.append("provenance_"+k)
    if prov.get("source_result_sha256") not in (None,ssha) or prov.get("independent_validation_sha256") not in (None,isha): e.append("provenance_hash_binding")
    if prov.get("parser_capacity")!=ident["parser_capacity"] or prov.get("class_build_authority_git_blob")!=ident["class_build_authority_git_blob"] or prov.get("candidate_memtotal_kb")!=mem: e.append("provenance_parser_build_memory")
    valid=not e; cls=RESOURCE_PASS if valid else FAIL
    out={"schema":c.get("output_schema_if_all_checks_pass") if valid else "LAYERB_32769_RESOURCE_AUTHORITY_MATERIALIZATION_FAILURE_V0_2","classification":cls,"effect":"+0/+0","artifact_verified_independently":valid,"high_memory_resource_lifecycle_preflight_pass":valid,"materialization_errors":e,"materialization_contract_json_sha256":csha,"materialization_contract_git_blob":cblob,"source_result_json_sha256":ssha,"source_result_git_blob":sblob,"independent_validation_json_sha256":isha,"independent_validation_git_blob":iblob,"provenance_receipt_json_sha256":psha,"provenance_receipt_git_blob":pblob,"source_run_id":prov.get("source_run_id"),"source_job_id":prov.get("source_job_id"),"source_head_sha":prov.get("source_head_sha"),"source_artifact_id":prov.get("source_artifact_id"),"source_artifact_zip_sha256":prov.get("source_artifact_zip_sha256"),"independent_run_id":prov.get("independent_run_id"),"independent_job_id":prov.get("independent_job_id"),"independent_head_sha":prov.get("independent_head_sha"),"independent_artifact_id":prov.get("independent_artifact_id"),"independent_artifact_zip_sha256":prov.get("independent_artifact_zip_sha256"),"candidate_memtotal_kb":mem,"execution_lifecycle":life,"role_order":src.get("role_order"),"peak_role_ru_maxrss_kb":max((x.get("ru_maxrss_kb_after_compute",0) for x in rr),default=0) if isinstance(rr,list) else 0,"telemetry_summary":ind.get("telemetry_summary"),"runner_agent_id":src.get("runner_agent_id"),"runner_name":src.get("runner_name"),"required_custom_label":ident["required_custom_label"],"parser_capacity":ident["parser_capacity"],"canonical_32769_node_sha256":ident["canonical_32769_node_sha256"],"canonical_32769_text_sha256":ident["canonical_32769_text_sha256"],"class_build_authority_git_blob":ident["class_build_authority_git_blob"],"runner_isolation_contract_git_blob":ident["runner_isolation_contract_git_blob"],"scientific_transfer_values_read":False,"scientific_response_read":False,"scientific_response_computed":False,"convergence_metric_computed":False,"convergence_classification_created":False,"scientific_authority_created":False,"successor_execution_authorized":False,"covariance_restriction_authorized":False,"Wm_S3_opened":False,"token":cls}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n"); print(cls)
    if e: print("ERRORS",",".join(e))
    return 0 if valid else 31
if __name__=="__main__": raise SystemExit(main())
