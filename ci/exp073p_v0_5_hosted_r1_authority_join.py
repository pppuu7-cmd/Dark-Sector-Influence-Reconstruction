#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

RUN_ID = 33270843577
JOB_ID = 99148916507
HEAD = "ef783ca941fb9b9b5f5eae537986c56ff06e6536"
WORKFLOW_PATH = ".github/workflows/exp073r1-desy1-github-hosted-wholestream-retry-v0-8.yml"
WORKFLOW_ID = 345506303
ARTIFACT_NAME = "exp073r1-v08-hosted-wholestream-" + HEAD
METACAL_SHA = "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8"
SOURCE_WHOLE_SHA = "491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5"
SOURCE_INDEX_SHA = "dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628"
PASS = "PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED"
INCOMPLETE = "INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED"
INVALID = "INVALID_FOR_SCIENCE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED"
GATES = {"G7":"OPEN","G8":"OPEN","G9":"OPEN"}

REQUIRED_STEPS = (
    "Verify frozen evaluator and v0.8 preregistration firewall",
    "Require trigger-parent authority binding when push-triggered",
    "Re-bind immutable Stage-A and Exp073R0 metadata",
    "Re-bind downloaded parent internal contracts",
    "Execute frozen mapper through hosted rate-qualified whole-stream retries",
    "Assert genuine frozen reproduction PASS and v0.8 transport firewall",
)

def load(path):
    return json.loads(Path(path).read_text())

def base(status, authorized=False):
    return {
        "schema":"dsir.exp073p.v0.5.hosted_r1_v0.8_prerequisite_receipt",
        "status":status,
        "synthetic":False,
        "support_executor_authorized":bool(authorized),
        "scientific_classification":None,
        "science_gate_scored":False,
        "f_invalid_computed":False,
        "covariance_read":False,
        "G8_read":False,
        "gate_state":GATES,
        "bound":{"run_id":RUN_ID,"job_id":JOB_ID,"head_sha":HEAD,
                 "workflow_path":WORKFLOW_PATH,"workflow_id":WORKFLOW_ID,
                 "artifact_name":ARTIFACT_NAME},
    }

def invalid(reason, extra=None):
    d=base(INVALID, False); d["reason"]=reason
    if extra: d.update(extra)
    return d

def incomplete(reason, extra=None):
    d=base(INCOMPLETE, False); d["reason"]=reason
    if extra: d.update(extra)
    return d

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--run-json", required=True)
    ap.add_argument("--jobs-json", required=True)
    ap.add_argument("--artifacts-json", required=True)
    ap.add_argument("--artifact-root", required=True)
    ap.add_argument("--out", required=True)
    a=ap.parse_args()

    run=load(a.run_json)
    jobs=load(a.jobs_json)
    arts=load(a.artifacts_json)
    result=None
    try:
        identity = {
            "id": run.get("id")==RUN_ID,
            "head": run.get("head_sha")==HEAD,
            "path": run.get("path")==WORKFLOW_PATH,
            "workflow_id": run.get("workflow_id")==WORKFLOW_ID,
            "event": run.get("event")=="push",
        }
        if not all(identity.values()):
            result=invalid("bound run identity mismatch", {"run_identity_checks":identity})
        elif run.get("status")!="completed" or run.get("conclusion")!="success":
            result=incomplete("bound R1 v0.8 run did not complete successfully",
                              {"run_status":run.get("status"),"run_conclusion":run.get("conclusion")})
        else:
            job_list=jobs.get("jobs",[])
            matches=[j for j in job_list if j.get("id")==JOB_ID]
            if len(matches)!=1:
                result=invalid("bound job identity missing/ambiguous")
            else:
                job=matches[0]
                if job.get("status")!="completed" or job.get("conclusion")!="success":
                    result=invalid("run success but bound job not successful")
                else:
                    step_map={s.get("name"):s.get("conclusion") for s in job.get("steps",[])}
                    step_checks={name:step_map.get(name)=="success" for name in REQUIRED_STEPS}
                    if not all(step_checks.values()):
                        result=invalid("required v0.8 authority step not success",
                                       {"step_checks":step_checks})
                    else:
                        art_list=[x for x in arts.get("artifacts",[]) if x.get("name")==ARTIFACT_NAME]
                        if len(art_list)!=1:
                            result=invalid("expected artifact missing/ambiguous",
                                           {"matching_artifact_count":len(art_list)})
                        else:
                            art=art_list[0]
                            if art.get("expired") is True:
                                result=invalid("bound artifact is expired")
                            elif not isinstance(art.get("digest"),str) or not art["digest"].startswith("sha256:"):
                                result=invalid("GitHub artifact digest missing/malformed")
                            else:
                                root=Path(a.artifact_root)
                                pp=list(root.rglob("exp073r1_v0_8_transport_provenance.json"))
                                ss=list(root.rglob("exp073r1_desy1_hosted_wholestream_v0_8_summary.json"))
                                if len(pp)!=1 or len(ss)!=1:
                                    result=invalid("downloaded authority files missing/ambiguous",
                                                   {"provenance_files":len(pp),"summary_files":len(ss)})
                                else:
                                    p=load(pp[0]); s=load(ss[0])
                                    checks = {
                                        "transport_status": p.get("status")=="PASS_EXP073R1_V08_HOSTED_RATE_QUALIFIED_WHOLESTREAM",
                                        "transport_scope": p.get("scope")=="TRANSPORT_EXECUTION_ONLY_NO_SCIENCE_GATE",
                                        "no_ranges": p.get("http_range_requests")==0 and p.get("whole_object_attempts_from_zero") is True,
                                        "complete_route": p.get("complete_whole_object_routes",0)>=1 and any(r.get("network_bytes")==84075649920 for r in p.get("routes",[])),
                                        "all_routes_zero": bool(p.get("routes")) and all(r.get("started_from_byte")==0 and r.get("range_header_sent") is False for r in p.get("routes",[])),
                                        "transport_no_science": p.get("science_gate_scored") is False and p.get("f_invalid_computed") is False and p.get("covariance_read") is False and p.get("G8_read") is False and p.get("gate_state")==GATES,
                                        "mapper_status": s.get("status")=="PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1",
                                        "metacal_sha": s.get("metacal_sha256")==METACAL_SHA and s.get("expected_metacal_sha256")==METACAL_SHA,
                                        "metacal_bytes": s.get("observed_bytes_metacal")==84075649920 and s.get("expected_bytes_metacal")==84075649920,
                                        "source_whole": s.get("source_identity_binding",{}).get("source_whole_sha256")==SOURCE_WHOLE_SHA,
                                        "source_index": s.get("source_identity_binding",{}).get("source_index_sha256")==SOURCE_INDEX_SHA,
                                        "rows": s.get("rows_read_source_index")==136930995 and s.get("rows_read_metacal")==136930995,
                                        "selection": s.get("selection")=="zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0",
                                        "mapper": s.get("mapper")=={"nside":4096,"ordering":"RING","coords":"C","lonlat":True},
                                        "pixels": s.get("out_of_range_pixel_count")==0,
                                        "selected": bool(s.get("selected_rows_per_bin")) and all(v>0 for v in s["selected_rows_per_bin"].values()),
                                        "repeatability": bool(s.get("repeatability_from_pixel_records")) and all(all(x is True for x in v.values()) for v in s["repeatability_from_pixel_records"].values()),
                                        "r0_parent": bool(s.get("parent_r0",{}).get("checks")) and all(s["parent_r0"]["checks"].values()),
                                        "mapper_no_science": s.get("science_gate_scored") is False and s.get("f_invalid_computed") is False and s.get("covariance_read") is False and s.get("G8_read") is False and s.get("gate_state")==GATES,
                                    }
                                    if not all(checks.values()):
                                        result=invalid("downloaded v0.8 contract check failed", {"contract_checks":checks})
                                    else:
                                        result=base(PASS, True)
                                        result.update({
                                            "run_status":"completed",
                                            "run_conclusion":"success",
                                            "job_conclusion":"success",
                                            "step_checks":step_checks,
                                            "artifact":{
                                                "id":art.get("id"),
                                                "name":art.get("name"),
                                                "digest":art.get("digest"),
                                                "expired":art.get("expired"),
                                                "size_in_bytes":art.get("size_in_bytes"),
                                            },
                                            "transport_pass_token":p["status"],
                                            "mapper_pass_token":s["status"],
                                            "contract_checks":checks,
                                        })
    except Exception as exc:
        result=invalid(f"join evaluator exception: {type(exc).__name__}: {exc}")

    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":result["status"],"support_executor_authorized":result["support_executor_authorized"]},sort_keys=True))

if __name__=="__main__":
    main()
