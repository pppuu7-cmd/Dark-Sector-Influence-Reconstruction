#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

PASS="LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_PASS_PLUS_0_PLUS_0"
FAIL="LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_FAIL_PLUS_0_PLUS_0"
SRC_PASS="LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
IND_PASS="LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
CONTRACT_BLOB="71d77aa4d074bba1a2f53e7f9299a9db32e93ffc"

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def blob(b): return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p): return json.loads(Path(p).read_text())
def pos(x): return isinstance(x,int) and x>0
def gitsha(x): return isinstance(x,str) and len(x)==40 and all(c in "0123456789abcdef" for c in x)
def dig(x): return x[7:] if isinstance(x,str) and x.startswith("sha256:") else x if isinstance(x,str) else None
def one(xs,pred,label,errs):
    ys=[x for x in xs if isinstance(x,dict) and pred(x)]
    if len(ys)!=1: errs.append(f"{label}_count_{len(ys)}"); return None
    return ys[0]

def main():
    ap=argparse.ArgumentParser()
    for k in ("contract","source-run","source-jobs","source-artifacts","source-artifact-zip","source-result","independent-run","independent-jobs","independent-artifacts","independent-artifact-zip","independent-validation","chain-receipt","out"):
        ap.add_argument("--"+k,required=True)
    a=ap.parse_args(); e=[]
    cb=Path(a.contract).read_bytes(); c=json.loads(cb)
    if blob(cb)!=CONTRACT_BLOB: e.append("contract_blob")
    if c.get("packaging_output_is_candidate_only") is not True or c.get("durable_repository_authority_created_by_packaging") is not False or c.get("contents_write_permission_forbidden") is not True: e.append("contract_safety")
    sr=load(a.source_run); sj=load(a.source_jobs); sa=load(a.source_artifacts); src=load(a.source_result)
    ir=load(a.independent_run); ij=load(a.independent_jobs); ia=load(a.independent_artifacts); ind=load(a.independent_validation); ch=load(a.chain_receipt)
    sc=c["source_workflow"]; ic=c["independent_workflow"]
    srid=sr.get("id"); irid=ir.get("id")
    if not pos(srid) or sr.get("name")!=sc["name"] or sr.get("path")!=sc["path"] or sr.get("status")!="completed" or sr.get("conclusion")!=sc["required_conclusion"] or not gitsha(sr.get("head_sha")): e.append("source_run")
    if not pos(irid) or ir.get("name")!=ic["name"] or ir.get("path")!=ic["path"] or ir.get("status")!="completed" or ir.get("conclusion")!=ic["required_conclusion"] or not gitsha(ir.get("head_sha")): e.append("independent_run")
    sjob=one(sj.get("jobs",[]),lambda x:x.get("name")==sc["job_name"],"source_job",e); ijob=one(ij.get("jobs",[]),lambda x:x.get("name")==ic["job_name"],"independent_job",e)
    if sjob and (sjob.get("status")!="completed" or sjob.get("conclusion")!="success"): e.append("source_job_conclusion")
    if ijob and (ijob.get("status")!="completed" or ijob.get("conclusion")!="success"): e.append("independent_job_conclusion")
    sart=one(sa.get("artifacts",[]),lambda x:x.get("name")==sc["artifact_name"],"source_artifact",e)
    iname=ic["artifact_name_template"].format(source_run_id=srid)
    iart=one(ia.get("artifacts",[]),lambda x:x.get("name")==iname,"independent_artifact",e)
    szip=sha(a.source_artifact_zip); izip=sha(a.independent_artifact_zip)
    for label,art,z in (("source",sart,szip),("independent",iart,izip)):
        if art:
            if art.get("expired") is True: e.append(label+"_artifact_expired")
            d=dig(art.get("digest"))
            if d is not None and d!=z: e.append(label+"_artifact_digest")
    ssha=sha(a.source_result); isha=sha(a.independent_validation)
    if src.get("classification")!=SRC_PASS: e.append("source_classification")
    if src.get("capacity")!=c["required_point_capacity"] or src.get("parser_capacity")!=c["required_parser_capacity"]: e.append("source_capacity")
    if src.get("build_authority_classification")!=c["required_build_authority_classification"]: e.append("source_build")
    if not isinstance(src.get("candidate_memtotal_kb"),int) or src["candidate_memtotal_kb"]<=c["candidate_memtotal_kb_must_be_strictly_greater_than"] or src.get("candidate_strictly_higher_memory_than_exhausted_hosted") is not True: e.append("source_memory")
    for k,v in c["required_source_conditions"].items():
        if src.get(k)!=v: e.append("source_"+k)
    if ind.get("classification")!=IND_PASS or ind.get("valid") is not True or ind.get("errors")!=[]: e.append("independent_validity")
    if ind.get("source_result_sha256")!=ssha or ind.get("parser_capacity")!=c["required_parser_capacity"] or ind.get("candidate_memtotal_kb")!=src.get("candidate_memtotal_kb"): e.append("independent_binding")
    if ind.get("runner_agent_id")!=src.get("runner_agent_id") or ind.get("runner_name")!=src.get("runner_name"): e.append("runner_binding")
    rq=c["required_chain_conditions"]
    if ch.get("consumer_execution_completed")!=rq["consumer_execution_completed"] or ch.get("independent_valid")!=rq["independent_valid"] or ch.get("independent_errors")!=rq["independent_errors"] or ch.get("scientific_response_read")!=rq["scientific_response_read"] or ch.get("scientific_execution_authorized")!=rq["scientific_execution_authorized"]: e.append("chain_conditions")
    if ch.get("classification")!=ind.get("classification") or ch.get("source_run_id")!=srid or ch.get("source_head_sha")!=sr.get("head_sha") or ch.get("source_conclusion")!=sr.get("conclusion") or ch.get("independent_validation_sha256")!=isha: e.append("chain_binding")
    ids=(sjob.get("id") if sjob else None, ijob.get("id") if ijob else None, sart.get("id") if sart else None, iart.get("id") if iart else None)
    if not all(pos(x) for x in ids): e.append("positive_ids")
    valid=not e; cls=PASS if valid else FAIL
    out={"schema":"LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PROVENANCE_V0_2","classification":cls,"effect":"+0/+0","valid":valid,"errors":e,"candidate_only":True,"durable_repository_authority_created":False,"packaging_contract_git_blob":CONTRACT_BLOB,"packaging_contract_sha256":hashlib.sha256(cb).hexdigest(),"source_run_id":srid,"source_job_id":ids[0],"source_head_sha":sr.get("head_sha"),"source_artifact_id":ids[2],"source_artifact_zip_sha256":szip,"source_result_sha256":ssha,"independent_run_id":irid,"independent_job_id":ids[1],"independent_head_sha":ir.get("head_sha"),"independent_artifact_id":ids[3],"independent_artifact_zip_sha256":izip,"independent_validation_sha256":isha,"chain_receipt_sha256":sha(a.chain_receipt),"source_workflow_name":sr.get("name"),"independent_workflow_name":ir.get("name"),"source_artifact_name":sart.get("name") if sart else None,"independent_artifact_name":iart.get("name") if iart else None,"parser_capacity":src.get("parser_capacity"),"class_build_authority_git_blob":c["required_build_authority_git_blob"],"candidate_memtotal_kb":src.get("candidate_memtotal_kb"),"runner_agent_id":src.get("runner_agent_id"),"runner_name":src.get("runner_name"),"scientific_response_read":False,"scientific_execution_authorized":False,"high_memory_resource_lifecycle_preflight_pass_created_by_packaging":False,"covariance_restriction_authorized":False,"Wm_S3_opened":False,"token":cls}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(cls); print("ERRORS",",".join(e)) if e else None
    return 0 if valid else 31
if __name__=="__main__": raise SystemExit(main())
