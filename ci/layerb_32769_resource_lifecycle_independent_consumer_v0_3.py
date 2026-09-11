#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

SOURCE_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
CONSUMER_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
CONSUMER_FAIL = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_FAIL_PLUS_0_PLUS_0"
CANON = "CANONICAL_32769_STATIC_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
BUILD = "LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_V0_2_PASS_PLUS_0_PLUS_0"
HOSTED_MEMTOTAL_KB = 16373452
PARSER_CAPACITY = 1048576
POINT_CAPACITY = 32769
PAYLOAD_BYTES = 719273
NODE_SHA = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
TEXT_SHA = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
ISOLATION_BLOB = "d9d910d89889f6d3a27461a73c3dd72c2a9d2096"
CONFIGURATOR_SHA256 = "2cd02d1a7ac58ea3945a435272f03ea1abe2d7e3410191b5a17a9c62e0a297ce"
REQUIRED_LABEL = "dsir-32769-highmem"
ROLES = ["reference", "alpha_minus", "beta_plus", "beta_minus"]
POINT_PRE = "c83749338e435d85caf8f0cfb713aa9a77782a91072de93633187d9dc53a0876"
POINT_POST = "e6221887e19c0a576f77bbfcb2a030ff9cf8d84c62a2193ce52b8e3b541a8f0a"
PARSER_PRE = "2c17690a5549e12c8fac485281ca214a20c376e1e3beba714af0e1b84cdbb0eb"
PARSER_POST = "2d775ca12da2c79b3700672fa66d290d5a06458a5253ea1e2c51b44ac2374092"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def kv(path: Path) -> dict[str, str]:
    out = {}
    for line in path.read_text(errors="replace").splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def telemetry(path: Path) -> dict:
    samples = []
    for line in path.read_text(errors="replace").splitlines():
        if not line.startswith("TELEMETRY "):
            continue
        vals = {}
        for key in ("MemTotal", "MemAvailable", "SwapTotal", "SwapFree"):
            m = re.search(rf"{key}=(\d+)kB", line) or re.search(rf"{key}:(\d+)=kB", line)
            if m:
                vals[key] = int(m.group(1))
        if vals:
            samples.append(vals)
    return {
        "sample_count": len(samples),
        "memtotal_min_kb": min((x["MemTotal"] for x in samples if "MemTotal" in x), default=None),
        "memavailable_min_kb": min((x["MemAvailable"] for x in samples if "MemAvailable" in x), default=None),
        "swapfree_min_kb": min((x["SwapFree"] for x in samples if "SwapFree" in x), default=None),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact-dir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root = Path(a.artifact_dir)
    out_path = Path(a.out)
    paths = {name: root / fn for name, fn in {
        "result":"result.json", "patch":"capacity_patch.json", "mem":"candidate_memtotal_kb.txt",
        "before":"host_envelope_before.txt", "after":"host_envelope_after.txt", "stale":"stale_job_snapshot.json",
        "telemetry":"telemetry.log", "registration":"runner_registration_receipt.json", "runtime":"source_job_runtime.json"
    }.items()}
    errors = [f"missing_{k}" for k,p in paths.items() if not p.is_file()]
    if errors:
        d={"schema":"LAYERB_32769_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_V0_3","classification":CONSUMER_FAIL,"effect":"+0/+0","valid":False,"errors":errors,"scientific_response_read":False,"scientific_authority_created":False,"token":CONSUMER_FAIL}
        out_path.parent.mkdir(parents=True,exist_ok=True); out_path.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n"); return 31

    src=json.loads(paths["result"].read_text()); patch=json.loads(paths["patch"].read_text()); stale=json.loads(paths["stale"].read_text()); reg=json.loads(paths["registration"].read_text()); runtime=json.loads(paths["runtime"].read_text()); before=kv(paths["before"]); tele=telemetry(paths["telemetry"])
    try: mem=int(paths["mem"].read_text().strip())
    except Exception: mem=-1; errors.append("candidate_memtotal_parse")

    if src.get("classification")!=SOURCE_PASS: errors.append("source_classification")
    if src.get("canonical_authority_classification")!=CANON or src.get("build_authority_classification")!=BUILD: errors.append("authority_classification")
    if src.get("canonical_32769_node_sha256")!=NODE_SHA or src.get("canonical_32769_text_sha256")!=TEXT_SHA or src.get("canonical_32769_requested_node_count")!=32769: errors.append("canonical_identity")
    if src.get("capacity")!=POINT_CAPACITY or src.get("parser_capacity")!=PARSER_CAPACITY: errors.append("capacity")
    if src.get("candidate_memtotal_kb")!=mem or mem<=HOSTED_MEMTOTAL_KB or src.get("candidate_strictly_higher_memory_than_exhausted_hosted") is not True: errors.append("candidate_memory")
    if src.get("runner_isolation_contract_git_blob")!=ISOLATION_BLOB or src.get("required_custom_label")!=REQUIRED_LABEL: errors.append("isolation_binding")

    life=src.get("execution_lifecycle",{})
    if life.get("total_solver_constructions")!=4 or life.get("max_live_instances")!=1 or life.get("final_live_instances")!=0: errors.append("lifecycle")
    receipts=src.get("role_receipts")
    if not isinstance(receipts,list) or len(receipts)!=4: errors.append("role_receipts"); receipts=[]
    else:
        if [x.get("role") for x in receipts]!=ROLES: errors.append("role_order")
        for x in receipts:
            if x.get("compute_completed") is not True: errors.append("role_compute")
            if x.get("k_output_values_bytes_including_nul")!=PAYLOAD_BYTES: errors.append("role_payload")
            if x.get("scientific_transfer_values_read") is not False or x.get("scientific_response_computed") is not False or x.get("scientific_response_serialized") is not False: errors.append("role_response_blind")
            if not isinstance(x.get("ru_maxrss_kb_after_compute"),int) or x.get("ru_maxrss_kb_after_compute")<=0: errors.append("role_rss")

    for k in ("scientific_transfer_values_read","scientific_response_read","scientific_response_computed","convergence_metric_computed","convergence_classification_created","scientific_authority_created","successor_execution_authorized","covariance_restriction_authorized","Wm_S3_opened"):
        if src.get(k) is not False: errors.append(k)

    if patch.get("source_commit")!="ac627d54e9ce196a08878d1ba33999819925d19c" or patch.get("new_capacity")!=POINT_CAPACITY or patch.get("parser_new_argument_capacity")!=PARSER_CAPACITY: errors.append("patch_capacity")
    if patch.get("point_pre_sha256")!=POINT_PRE or patch.get("point_post_sha256")!=POINT_POST or patch.get("parser_pre_sha256")!=PARSER_PRE or patch.get("parser_post_sha256")!=PARSER_POST: errors.append("patch_hash")

    if reg.get("classification")!="LAYERB_32769_HIGH_MEMORY_RUNNER_REGISTRATION_CONFIGURED_PLUS_0_PLUS_0" or reg.get("configuration_script_sha256")!=CONFIGURATOR_SHA256 or reg.get("runner_isolation_contract_git_blob")!=ISOLATION_BLOB: errors.append("registration_identity")
    if reg.get("configured_labels")!=[REQUIRED_LABEL] or reg.get("no_default_labels") is not True: errors.append("registration_labels")
    agent=reg.get("runner_agent_id"); name=reg.get("runner_name")
    if runtime.get("runner_id")!=agent or runtime.get("runner_name")!=name or runtime.get("labels")!=[REQUIRED_LABEL] or runtime.get("name")!="resource-lifecycle-pilot": errors.append("runtime_binding")
    if src.get("runner_registration_receipt_sha256")!=sha(paths["registration"]) or src.get("source_job_runtime_sha256")!=sha(paths["runtime"]) or src.get("runner_registration_evidence_valid") is not True: errors.append("source_registration_hash_binding")
    if stale.get("id")!=103112190909 or stale.get("status")=="in_progress": errors.append("stale_job")
    if before.get("runner_name")!=name or before.get("required_custom_label")!=REQUIRED_LABEL or before.get("candidate_memtotal_kb")!=str(mem): errors.append("host_receipt")
    if not paths["after"].read_text(errors="replace").strip(): errors.append("host_after")
    if tele.get("sample_count",0)<1: errors.append("telemetry")

    valid=not errors; cls=CONSUMER_PASS if valid else CONSUMER_FAIL
    out={"schema":"LAYERB_32769_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_V0_3","classification":cls,"effect":"+0/+0","valid":valid,"errors":errors,"source_result_sha256":sha(paths["result"]),"capacity_patch_sha256":sha(paths["patch"]),"runner_registration_receipt_sha256":sha(paths["registration"]),"source_job_runtime_sha256":sha(paths["runtime"]),"telemetry_sha256":sha(paths["telemetry"]),"candidate_memtotal_kb":mem,"runner_name":name,"runner_agent_id":agent,"execution_lifecycle":life,"telemetry_summary":tele,"required_custom_label":REQUIRED_LABEL,"parser_capacity":PARSER_CAPACITY,"scientific_response_read":False,"scientific_authority_created":False,"successor_execution_authorized":False,"covariance_restriction_authorized":False,"Wm_S3_opened":False,"token":cls}
    out_path.parent.mkdir(parents=True,exist_ok=True); out_path.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n"); print(cls)
    if errors: print("ERRORS",",".join(errors))
    return 0 if valid else 31

if __name__=="__main__": raise SystemExit(main())
