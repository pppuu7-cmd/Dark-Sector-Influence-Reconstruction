#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

PREREG_COMMIT = "c10580116420a4c01d73dc6307b0a9b100c3ac69"
PREREG_BLOB = "f1244ebf0f0b70cc624aa12cd62710438cb2fbf4"
ADAPTER_COMMIT = "5883481af17401d048e26d1a3b7816193e825653"
ADAPTER_BLOB = "72870dc0946f94b421ef104feea2daf34047434f"
A1_RECOVERY_COMMIT = "aee00943f483bcac88612f61133c13b49945e55d"
POLICY_BLOB = "101e81bc5886df0a4ea7f4eb80e38ab2750d6c77"
SYNC_V02_BLOB = "1895b98d9533e56d405bc66344accae3a48ecdfd"
PRODUCTION_DRIVER_BLOB = "5c8d5d3463e455389a1ca3df2639bf06a3b7b603"
MCM_PAYLOAD_BYTES = 603_979_776 * 8
NSIDE = 4096
DENSE_MAP_PAYLOAD_BYTES = 12 * NSIDE * NSIDE * 8
GIT_OBJECT_LIMIT = 100 * 1024 * 1024
GIT_PUSH_LIMIT = 2 * 1024 * 1024 * 1024
CHUNK_CAP = 64 * 1024 * 1024
BATCH_CAP = 1024 * 1024 * 1024
CHECKPOINT_ORDER = [
    "fresh_masks_complete", "fresh_workspace_mcm_complete", "mcm_fits_verified",
    "full_window_complete", "selected_te_complete", "replica_receipt_complete",
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def blob(path: str) -> str:
    return git("rev-parse", f"HEAD:{path}")


def ancestor(commit: str) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], check=False).returncode == 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-head", required=True)
    ap.add_argument("--selftest-receipt", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    checks = {}
    checks["source_head_exact"] = git("rev-parse", "HEAD") == args.source_head
    checks["prereg_ancestor"] = ancestor(PREREG_COMMIT)
    checks["adapter_commit_ancestor"] = ancestor(ADAPTER_COMMIT)
    checks["a1_recovery_ancestor"] = ancestor(A1_RECOVERY_COMMIT)
    checks["prereg_blob"] = blob("experiments/073da_wm_s3_large_stage_checkpoint_transport_v0_1_prereg.md") == PREREG_BLOB
    checks["adapter_blob"] = blob("ci/dsir_checkpoint_sharded_payload_v0_1.py") == ADAPTER_BLOB
    checks["policy_blob"] = blob("docs/SELF_HOSTED_CHECKPOINT_POLICY.md") == POLICY_BLOB
    checks["sync_v02_blob"] = blob("ci/dsir_checkpoint_git_sync_v0_2.sh") == SYNC_V02_BLOB
    checks["production_driver_blob"] = blob("ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py") == PRODUCTION_DRIVER_BLOB

    a1 = Path("recovery/2026-09-04_exp073cx_v0_4_a1_activation_readiness_pass.md").read_text()
    policy = Path("docs/SELF_HOSTED_CHECKPOINT_POLICY.md").read_text()
    sync = Path("ci/dsir_checkpoint_git_sync_v0_2.sh").read_text()
    prod = Path("ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py").read_text()
    adapter = Path("ci/dsir_checkpoint_sharded_payload_v0_1.py").read_text()
    checks["a1_token"] = "A1_EXP073BU_ACTIVATION_READINESS_PASS" in a1 and "exp073bu_activated=false" in a1
    checks["policy_remote_durability"] = "persist checkpoints remotely under a dedicated `checkpoints/*` namespace" in policy
    checks["existing_sync_whole_tree"] = ('cp -a "$checkpoint_dir/." "$work/checkpoint/"' in sync and 'new_tree="$(git -C "$work" write-tree)"' in sync)
    checks["checkpoint_order"] = all(x in prod for x in CHECKPOINT_ORDER) and prod.index("fresh_masks_complete") < prod.index("fresh_workspace_mcm_complete") < prod.index("mcm_fits_verified") < prod.index("full_window_complete") < prod.index("selected_te_complete") < prod.index("replica_receipt_complete")
    checks["ab_namespace_isolation"] = "checkpoints/exp073bu-wm-s3-a-v0-1" in prod and "checkpoints/exp073bu-wm-s3-b-v0-1" in prod
    checks["mcm_size_frozen"] = MCM_PAYLOAD_BYTES == 4_831_838_208
    checks["dense_map_size_frozen"] = DENSE_MAP_PAYLOAD_BYTES == 1_610_612_736
    checks["existing_transport_object_incompatible"] = MCM_PAYLOAD_BYTES > GIT_OBJECT_LIMIT and DENSE_MAP_PAYLOAD_BYTES > GIT_OBJECT_LIMIT
    checks["existing_transport_push_incompatible"] = MCM_PAYLOAD_BYTES > GIT_PUSH_LIMIT
    checks["chunk_cap_margin"] = CHUNK_CAP < GIT_OBJECT_LIMIT and "CHUNK_BYTES = 64 * 1024 * 1024" in adapter
    checks["batch_cap_margin"] = BATCH_CAP < GIT_PUSH_LIMIT and "BATCH_BYTES_MAX = 1024 * 1024 * 1024" in adapter
    checks["science_firewall"] = "historical_wm_s3_numerical_import" in adapter and "science_gate_scored" in adapter

    st = json.loads(Path(args.selftest_receipt).read_text())
    for key in ["roundtrip_exact", "corruption_rejected", "missing_rejected", "reordered_rejected", "race_model_failclosed", "chunk_cap_below_git_object_limit", "batch_cap_below_git_push_limit"]:
        checks[f"selftest_{key}"] = st.get(key) is True
    checks["selftest_sha_exact"] = st.get("source_sha256") == st.get("restored_sha256")

    ok = all(checks.values())
    status = "K1_LARGE_STAGE_SHARDED_CHECKPOINT_TRANSPORT_PASS" if ok else "K2_LARGE_STAGE_TRANSPORT_IMPLEMENTATION_FAIL"
    rec = {
        "schema": "dsir.exp073da.wm_s3.large_stage_checkpoint_transport.v0.1",
        "status": status,
        "accounting": "+0/+0",
        "source_head": args.source_head,
        "checks": checks,
        "mcm_payload_bytes": MCM_PAYLOAD_BYTES,
        "dense_map_payload_bytes_each": DENSE_MAP_PAYLOAD_BYTES,
        "git_object_limit_bytes": GIT_OBJECT_LIMIT,
        "git_push_limit_bytes": GIT_PUSH_LIMIT,
        "chunk_cap_bytes": CHUNK_CAP,
        "batch_cap_bytes": BATCH_CAP,
        "existing_whole_tree_transport_sufficient": False,
        "exp073bu_activated": False,
        "wm_s3_authority_created": False,
        "science_gate_scored": False,
        "no_des_scale_numerics_executed": True,
        "no_tolerance_rescue": True,
        "permitted_successor": "prospective remote_git_batch_orchestration_binding_audit",
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    print(status)
    print(json.dumps(rec, indent=2, sort_keys=True))
    raise SystemExit(0 if ok else 2)


if __name__ == "__main__":
    main()
