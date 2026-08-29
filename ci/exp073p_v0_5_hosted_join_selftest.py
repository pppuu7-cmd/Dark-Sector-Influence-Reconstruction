#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

EVALUATOR = Path(__file__).with_name("exp073p_v0_5_hosted_r1_authority_join.py")
HEAD = "ef783ca941fb9b9b5f5eae537986c56ff06e6536"
ARTIFACT_NAME = "exp073r1-v08-hosted-wholestream-" + HEAD
GATES = {"G7":"OPEN","G8":"OPEN","G9":"OPEN"}

REQUIRED_STEPS = (
    "Verify frozen evaluator and v0.8 preregistration firewall",
    "Require trigger-parent authority binding when push-triggered",
    "Re-bind immutable Stage-A and Exp073R0 metadata",
    "Re-bind downloaded parent internal contracts",
    "Execute frozen mapper through hosted rate-qualified whole-stream retries",
    "Assert genuine frozen reproduction PASS and v0.8 transport firewall",
)


def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj), encoding="utf-8")


def fixture(root: Path):
    art = root / "artifact"
    art.mkdir(parents=True)
    run = {
        "id":33270843577,
        "head_sha":HEAD,
        "path":".github/workflows/exp073r1-desy1-github-hosted-wholestream-retry-v0-8.yml",
        "workflow_id":345506303,
        "event":"push",
        "status":"completed",
        "conclusion":"success",
    }
    jobs = {"jobs":[{
        "id":99148916507,
        "status":"completed",
        "conclusion":"success",
        "steps":[{"name":name,"conclusion":"success"} for name in REQUIRED_STEPS],
    }]}
    artifacts = {"artifacts":[{
        "id":123456789,
        "name":ARTIFACT_NAME,
        "expired":False,
        "digest":"sha256:"+"a"*64,
        "size_in_bytes":123,
    }]}
    provenance = {
        "status":"PASS_EXP073R1_V08_HOSTED_RATE_QUALIFIED_WHOLESTREAM",
        "scope":"TRANSPORT_EXECUTION_ONLY_NO_SCIENCE_GATE",
        "http_range_requests":0,
        "whole_object_attempts_from_zero":True,
        "complete_whole_object_routes":1,
        "routes":[{"network_bytes":84075649920,"started_from_byte":0,"range_header_sent":False}],
        "science_gate_scored":False,
        "f_invalid_computed":False,
        "covariance_read":False,
        "G8_read":False,
        "gate_state":GATES,
    }
    summary = {
        "status":"PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1",
        "metacal_sha256":"39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8",
        "expected_metacal_sha256":"39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8",
        "observed_bytes_metacal":84075649920,
        "expected_bytes_metacal":84075649920,
        "source_identity_binding":{
            "source_whole_sha256":"491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5",
            "source_index_sha256":"dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628",
        },
        "rows_read_source_index":136930995,
        "rows_read_metacal":136930995,
        "selection":"zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0",
        "mapper":{"nside":4096,"ordering":"RING","coords":"C","lonlat":True},
        "out_of_range_pixel_count":0,
        "selected_rows_per_bin":{"0":1,"1":1,"2":1,"3":1},
        "repeatability_from_pixel_records":{
            "0":{"record":True},"1":{"record":True},"2":{"record":True},"3":{"record":True}
        },
        "parent_r0":{"checks":{"parent":True}},
        "science_gate_scored":False,
        "f_invalid_computed":False,
        "covariance_read":False,
        "G8_read":False,
        "gate_state":GATES,
    }
    return art, run, jobs, artifacts, provenance, summary


def evaluate(root: Path, run, jobs, artifacts, provenance, summary):
    art = root / "artifact"
    dump(root/"run.json", run)
    dump(root/"jobs.json", jobs)
    dump(root/"artifacts.json", artifacts)
    dump(art/"exp073r1_v0_8_transport_provenance.json", provenance)
    dump(art/"exp073r1_desy1_hosted_wholestream_v0_8_summary.json", summary)
    out=root/"receipt.json"
    subprocess.run([
        sys.executable, str(EVALUATOR),
        "--run-json",str(root/"run.json"),
        "--jobs-json",str(root/"jobs.json"),
        "--artifacts-json",str(root/"artifacts.json"),
        "--artifact-root",str(art),
        "--out",str(out),
    ], check=True)
    return json.loads(out.read_text())


def main():
    results=[]
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)/"pass"; root.mkdir(parents=True)
        art, run, jobs, artifacts, provenance, summary = fixture(root)
        d=evaluate(root,run,jobs,artifacts,provenance,summary)
        ok=d["status"]=="PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED" and d["support_executor_authorized"] is True
        results.append({"case":"genuine_shaped_pass","pass":ok,"status":d["status"]})

    with tempfile.TemporaryDirectory() as td:
        root=Path(td)/"incomplete"; root.mkdir(parents=True)
        art, run, jobs, artifacts, provenance, summary = fixture(root)
        run["conclusion"]="failure"
        d=evaluate(root,run,jobs,artifacts,provenance,summary)
        ok=d["status"]=="INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED" and d["support_executor_authorized"] is False
        results.append({"case":"upstream_infrastructure_non_success","pass":ok,"status":d["status"]})

    with tempfile.TemporaryDirectory() as td:
        root=Path(td)/"invalid"; root.mkdir(parents=True)
        art, run, jobs, artifacts, provenance, summary = fixture(root)
        summary["metacal_sha256"]="0"*64
        d=evaluate(root,run,jobs,artifacts,provenance,summary)
        ok=d["status"]=="INVALID_FOR_SCIENCE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED" and d["support_executor_authorized"] is False
        results.append({"case":"success_claim_with_hash_contradiction","pass":ok,"status":d["status"]})

    if not all(r["pass"] for r in results):
        raise AssertionError(results)
    print(json.dumps({
        "status":"PASS_EXP073P_V05_HOSTED_JOIN_SYNTHETIC_BRANCH_SELFTEST",
        "scope":"SYNTHETIC_ONLY_NO_REAL_R1_ARTIFACT",
        "scientific_credit":False,
        "tests":results,
    }, indent=2, sort_keys=True))


if __name__=="__main__":
    main()
