#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

PASS = "PASS_EXP073DM_WW_S0_S0_EXACT_AUTHORITY_PREFLIGHT_V0_1"
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "ci/exp073aa_article3_des_angular_task_runner_v0_1.py"
PREREG = ROOT / "experiments/073dm_article3_ww_s0_s0_exact_authority_preflight_v0_1_prereg.md"
OUT = ROOT / "exp073dm_ww_s0_s0_exact_authority_preflight_v0_1.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    source = SRC.read_text(encoding="utf-8")
    prereg = PREREG.read_text(encoding="utf-8")
    tree = ast.parse(source)

    checks: dict[str, bool] = {}
    checks["parent_wm_s3_bound"] = all(x in prereg for x in [
        "33910213781 / 101144660519",
        "c02c018ede6a1fcf7aef1a848c0118a0669ed67f",
        "b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da",
        "PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3",
        "d282ebdf98dc04e41a8c85f487e209634a8324ce7677107112b8abfd1660f749",
    ])
    checks["exp073dl_evidence_bound"] = all(x in prereg for x in [
        "33934918432 / 101220868663", "9959830267",
        "cc32969cba9802201ac8cf7eae32b430ec47285f3357a58d470850aff8ceb8ab",
    ])
    checks["successor_order_frozen"] = "Wm_S3 -> WW_S0_S0 -> WW_S0_S1" in prereg

    # Literal/structural source assertions. These audit the already-frozen executor;
    # they do not execute NaMaster or create numerical WW output.
    required = [
        "NSIDE=4096", "LMAX_PLUS_ONE=3*NSIDE",
        "'WW_S0_S0'", "'WW_S0_S1'", "'WW_S3_S3'",
        "return 'WW',[i,j]", "if i>j:",
        "fa=nmt.NmtField(a,None,spin=2)",
        "if bmap is a:", "fb=fa",
        "w.compute_coupling_matrix(fa,fb,b)",
        "expected=(4,39,4,LMAX_PLUS_ONE)",
        "selected_semantics={'output':'EE','input':'EE','full_component_order':['EE','EB','BE','BB']}",
        "selected=np.ascontiguousarray(wins[0,:,0,:],dtype='<f8')",
        "if a.lens_mask:", "raise AssertionError('WW must not receive/read lens mask')",
        "'radial_kernel_read':False", "'physical_k_computed':False",
        "'physical_support_evaluated':False", "'retained_coordinates_evaluated':False",
    ]
    for item in required:
        checks[f"source::{item[:48]}"] = item in source

    # Verify exact task list order and constants by evaluating only AST literals.
    assignments = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in {"NSIDE", "LMAX_PLUS_ONE", "ALL_TASKS"}:
                assignments[name] = node.value
    checks["nside_literal_4096"] = isinstance(assignments.get("NSIDE"), ast.Constant) and assignments["NSIDE"].value == 4096
    tasks = ast.literal_eval(assignments["ALL_TASKS"])
    expected_tasks = [
        'Wm_S0','Wm_S1','Wm_S2','Wm_S3',
        'WW_S0_S0','WW_S0_S1','WW_S0_S2','WW_S0_S3',
        'WW_S1_S1','WW_S1_S2','WW_S1_S3','WW_S2_S2','WW_S2_S3','WW_S3_S3'
    ]
    checks["exact_successor_task_order"] = tasks == expected_tasks
    checks["ww_s0_s0_next_after_wm_s3"] = tasks.index("WW_S0_S0") == tasks.index("Wm_S3") + 1

    # Ban result-rescue concepts in this support decision file itself.
    me = Path(__file__).read_text(encoding="utf-8").lower()
    banned_decision_terms = ["np.allclose", "isclose(", "round(", "smoothing", "majority vote", "preferred replica"]
    checks["no_tolerance_rescue_in_preflight"] = not any(t in me for t in banned_decision_terms)

    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise SystemExit("BLOCKED_EXP073DM_WW_S0_S0_PREFLIGHT: " + json.dumps(failed, sort_keys=True))

    receipt = {
        "experiment": "Exp073DM",
        "classification": "SUPPORT_READINESS_PASS_PLUS_0_PLUS_0",
        "token": PASS,
        "science_gate_scored": False,
        "ww_authority_created": False,
        "numerical_ww_payload_created": False,
        "source_path": str(SRC.relative_to(ROOT)),
        "source_sha256": sha256(SRC),
        "prereg_path": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": sha256(PREREG),
        "task": "WW_S0_S0",
        "full_window_shape": [4, 39, 4, 12288],
        "selected_semantics": "EE<-EE",
        "selected_canonical": {"dtype": "<f8", "shape": [39, 12288]},
        "checks": checks,
    }
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(PASS)


if __name__ == "__main__":
    main()
