#!/usr/bin/env python3
"""Hosted static audit for Exp073CE v0.1. No Wm_S3 numerical science."""
from __future__ import annotations

import ast
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "exp073ce_exp073bu_integrated_contract_v0_1.py"
PREREG = ROOT / "experiments" / "073ce_exp073bu_integrated_driver_static_audit_v0_1_prereg.md"
PASS = "I1_EXP073BU_INTEGRATED_DRIVER_STATIC_AUDIT_PASS"
FAIL = "I2_INTEGRATION_CONTRACT_STATIC_FAIL"


def die(msg: str) -> None:
    print(json.dumps({"token": FAIL, "reason": msg}, sort_keys=True))
    raise SystemExit(2)


def main() -> None:
    if not TARGET.is_file() or not PREREG.is_file():
        die("missing frozen source or prereg")
    src = TARGET.read_text(encoding="utf-8")
    tree = ast.parse(src)
    if not tree.body:
        die("empty contract")

    spec = importlib.util.spec_from_file_location("exp073ce_contract", TARGET)
    if spec is None or spec.loader is None:
        die("cannot import contract")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    expected_stages = (
        "fresh_masks_complete", "fresh_workspace_mcm_complete", "mcm_fits_verified",
        "full_window_complete", "selected_te_complete", "replica_receipt_complete",
    )
    checks = {
        "contract_id": m.CONTRACT_ID == "EXP073CE_V0_1_EXP073BU_INTEGRATED_DRIVER",
        "namaster_2_7": m.NA_MASTER_VERSION == "2.7",
        "nside": m.NSIDE == 4096,
        "ell": (m.ELL_MIN, m.ELL_MAX) == (0, 12287),
        "bands": m.NBANDS == 39,
        "canonical": m.CANONICAL_DTYPE == "<f8" and m.CANONICAL_SHAPE == (39, 12288),
        "wm": m.WM_COMPONENT == "TE<-TE",
        "ww": m.WW_COMPONENT == "EE<-EE",
        "workers": m.OUTER_WORKERS == 8,
        "nested_one": all(v == "1" for v in m.NESTED_THREAD_ENV.values()),
        "stages": m.CHECKPOINT_STAGES == expected_stages,
        "replicas": m.REPLICAS == ("A", "B"),
        "stock_full": m.FULL_STOCK_ARITHMETIC == "namaster_2_7_full_ncls2_stock_operation_order",
        "write_to": m.REQUIRED_PERSISTENCE_API == "write_to",
        "os_mmap": m.MCM_CONSUMER == "read_only_os_mmap_row_stream",
        "forbid_mcm_materialization": m.FORBIDDEN_MCM_API == "get_coupling_matrix",
    }
    bad = sorted(k for k, v in checks.items() if not v)
    if bad:
        die("failed constants: " + ",".join(bad))

    # Check fail-closed checkpoint order and cross-replica isolation.
    previous = None
    for stage in expected_stages:
        try:
            m.validate_stage_transition(previous, stage)
        except Exception as exc:
            die(f"stage transition failed: {stage}: {exc}")
        previous = stage
    try:
        m.validate_stage_transition(None, "selected_te_complete")
        die("noncanonical stage transition accepted")
    except RuntimeError:
        pass
    try:
        m.validate_replica_isolation("A", m.checkpoint_namespace("B"))
        die("cross-replica restore accepted")
    except RuntimeError:
        pass

    # Fresh-input guard rejects explicitly historical numerical imports.
    try:
        m.validate_fresh_replica_inputs({
            "replica": "A", "fresh_masks": True, "fresh_replica_local_pcl": True,
            "numerical_imports": [m.FORBIDDEN_NUMERICAL_IMPORTS[0]],
        }, "A")
        die("historical numerical import accepted")
    except RuntimeError:
        pass

    # MCM lifecycle must prove stock writer, workspace destruction, mmap, no second copy.
    good_mcm = {
        "persistence_api": "write_to", "workspace_destroyed_before_consume": True,
        "mcm_consumer": "read_only_os_mmap_row_stream", "second_full_mcm_heap_copy": False,
        "apis_used": ["write_to"],
    }
    try:
        m.validate_mcm_lifecycle(good_mcm)
    except Exception as exc:
        die(f"valid MCM lifecycle rejected: {exc}")
    bad_mcm = dict(good_mcm, apis_used=["write_to", "get_coupling_matrix"])
    try:
        m.validate_mcm_lifecycle(bad_mcm)
        die("forbidden full MCM materialization accepted")
    except RuntimeError:
        pass

    # Final classifier must be exact-only and distinguish infrastructure identity failures.
    base = {
        "valid": True, "provenance_sha256": "p", "contract_fingerprint": "c",
        "source_head_sha": "h", "canonical_sha256": "x", "array_equal_peer": True,
        "dtype": "<f8", "shape": [39, 12288], "stage": "replica_receipt_complete",
    }
    if m.classify_final_ab(base, dict(base)) != "SCIENTIFIC_REPEATABILITY_PASS":
        die("exact PASS classifier broken")
    mismatch = dict(base, canonical_sha256="y", array_equal_peer=False)
    if m.classify_final_ab(base, mismatch) != "SCIENTIFIC_REPEATABILITY_FAIL":
        die("exact mismatch not classified as scientific repeatability fail")
    prov = dict(base, provenance_sha256="q")
    if m.classify_final_ab(base, prov) != "BLOCKED_PROVENANCE_OR_SOURCE_MISMATCH":
        die("provenance mismatch misclassified")
    incomplete = dict(base); incomplete.pop("source_head_sha")
    if m.classify_final_ab(base, incomplete) != "INFRASTRUCTURE_INCOMPLETE":
        die("incomplete identity misclassified")

    # No tolerance/smoothing/rounding rescue tokens are used in the classifier body.
    classifier = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "classify_final_ab")
    classifier_text = ast.get_source_segment(src, classifier) or ""
    banned_calls = ("isclose(", "allclose(", "round(", "smooth", "average(", "mean(")
    if any(tok in classifier_text.lower() for tok in banned_calls):
        die("tolerance/rounding/smoothing/averaging rescue found")

    fp = m.contract_fingerprint()
    if len(fp) != 64:
        die("invalid contract fingerprint")
    print(json.dumps({
        "token": PASS,
        "contract_fingerprint": fp,
        "accounting": "+0/+0",
        "wm_s3_authority_created": False,
        "exp073bu_activated": False,
        "checks": checks,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
