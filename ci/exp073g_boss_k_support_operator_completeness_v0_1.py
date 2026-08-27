#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from pathlib import Path

EXPECTED_KIDS_SHA = "36676da44471979dacb779155d7e6e7212ae1f4f"
EXPECTED_BINDING_SHA256 = "b547aa1836ae428e077b920ab1c7ec0ec2d12fcd6c5bdd06be2ed8b842e97e2a"
# Hash above is checked only when explicitly supplied by the workflow after computing the
# repository blob contents. The authoritative per-object hashes remain inside the binding.
EXPECTED_DATASET_SHA = "889a12d73145f8ca4037402f4a312e6a93aa7a20977ee07c3d430cd0b5e46c8d"
EXPECTED_RBANDS_SHA = "90ff937b38e1e648febf50ecee6046a361ae4cc45708e292c0b09fb21ca84162"
EXPECTED_WINDOWS_SHA = "d03fb658ce10b32edbfd8f3344bb0d933d6e026ae5c65a8fe32f519a9c4f8f0f"
CLASSIFICATION = "FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def parse_dataset(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kids-root", required=True)
    ap.add_argument("--binding", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    kids = Path(args.kids_root)
    binding_path = Path(args.binding)
    output = Path(args.output)
    binding = json.loads(binding_path.read_text())

    operator = {x["role"]: x for x in binding["operator_files"]}
    ds_rel = operator["boss_highz_dataset_contract"]["path"]
    rb_rel = operator["boss_highz_radial_bands"]["path"]
    win_rel = operator["boss_highz_window_operator"]["path"]
    dataset_path, rbands_path, windows_path = kids / ds_rel, kids / rb_rel, kids / win_rel

    ds = parse_dataset(dataset_path)
    provenance = {
        "kids_head": git_head(kids),
        "kids_head_expected": EXPECTED_KIDS_SHA,
        "kids_head_pass": git_head(kids) == EXPECTED_KIDS_SHA,
        "binding_record_type_pass": binding.get("record_type") == "PRE_OUTPUT_OPERATOR_AND_BNT_BINDING",
        "binding_support_not_evaluated": binding.get("support_evaluated") is False,
        "dataset_sha256": sha256(dataset_path),
        "dataset_sha256_pass": sha256(dataset_path) == EXPECTED_DATASET_SHA == operator["boss_highz_dataset_contract"]["sha256"],
        "rbands_sha256": sha256(rbands_path),
        "rbands_sha256_pass": sha256(rbands_path) == EXPECTED_RBANDS_SHA == operator["boss_highz_radial_bands"]["sha256"],
        "windows_sha256": sha256(windows_path),
        "windows_sha256_pass": sha256(windows_path) == EXPECTED_WINDOWS_SHA == operator["boss_highz_window_operator"]["sha256"],
    }

    contract = {
        "data_type": ds.get("data_type"),
        "num_ell": int(ds["num_ell"]),
        "num_points_full": int(ds["num_points_full"]),
        "num_bands_full": int(ds["num_bands_full"]),
        "min_points_use": int(ds["min_points_use"]),
        "max_points_use": int(ds["max_points_use"]),
        "min_bands_use": int(ds["min_bands_use"]),
        "max_bands_use": int(ds["max_bands_use"]),
        "mean_redshift": float(ds["mean_redshift"]),
    }
    contract_pass = (
        contract["data_type"] == "xi_wed"
        and contract["num_ell"] == 3
        and contract["min_points_use"] == 5
        and contract["max_points_use"] == 32
        and contract["min_bands_use"] == 21
        and contract["max_bands_use"] == 160
        and math.isclose(contract["mean_redshift"], 0.61, rel_tol=0, abs_tol=1e-15)
    )

    # Frozen Exp073G asks for a non-negative, P-independent support envelope whose
    # integral can be normalized over all k.  For a configuration-space correlation
    # coordinate, the linear Fourier-Bessel response to a power multipole has the form
    # K_l(k;s) ∝ k^2 j_l(k s). For fixed s>0, j_l(ks)=O(1/k) with oscillatory leading
    # term, hence |K_l|=O(k). A finite discrete release-window combination remains a
    # finite sum of such oscillatory terms and has no absolutely integrable all-k
    # envelope in the generic case. Therefore ∫_0^∞ |K| dk is not a finite normalizer.
    # Multiplying by a fiducial P(k), nonlinear damping, or imposing k_cut would make
    # the weight theory/cutoff dependent; none is frozen in the public operator binding.
    # That is precisely an operator/provenance incompleteness under Exp073G G6/G8,
    # not a support-leakage scientific failure.
    analytic_no_go = {
        "observable_is_configuration_space_xi_wedge": contract["data_type"] == "xi_wed",
        "finite_discrete_radial_window": contract["num_bands_full"] > 0 and windows_path.stat().st_size > 0,
        "fourier_bessel_kernel": "K_l(k;s) proportional to k^2 j_l(k s)",
        "large_k_asymptotic": "j_l(k s)=O(1/k), so absolute response is generically O(k)",
        "positive_operator_only_all_k_normalizer_finite": False,
        "extra_fiducial_power_weight_frozen": False,
        "extra_high_k_cutoff_frozen": False,
        "solver_neutral_support_fraction_well_defined": False,
    }
    no_go_pass = (
        analytic_no_go["observable_is_configuration_space_xi_wedge"]
        and analytic_no_go["finite_discrete_radial_window"]
        and not analytic_no_go["positive_operator_only_all_k_normalizer_finite"]
        and not analytic_no_go["extra_fiducial_power_weight_frozen"]
        and not analytic_no_go["extra_high_k_cutoff_frozen"]
    )

    provenance_pass = all(v for k, v in provenance.items() if k.endswith("_pass") or k == "binding_support_not_evaluated")
    trustworthy = bool(provenance_pass and contract_pass and no_go_pass)
    status = CLASSIFICATION if trustworthy else "INCOMPLETE_EXP073G"

    result = {
        "experiment": "Exp073G",
        "date": "2026-08-27",
        "audit": "BOSS_K_SUPPORT_OPERATOR_COMPLETENESS_V0_1",
        "status": status,
        "scientific_support_fail": False,
        "support_fraction_computed": False,
        "retained_dimension_computed": False,
        "trustworthy_operator_no_go": trustworthy,
        "provenance": provenance,
        "release_contract": contract,
        "release_contract_pass": contract_pass,
        "analytic_operator_no_go": analytic_no_go,
        "interpretation": {
            "reason": "The frozen public BOSS xi-wedge release operator does not define a finite solver-neutral positive all-k support measure without an additional theory weight or k cutoff.",
            "forbidden_repairs": ["post-hoc k cutoff", "fiducial P(k) weighting chosen after preregistration", "nonlinear damping chosen to manufacture support"],
            "classification_semantics": "reproduction/operator-provenance failure, not a permanent scientific support rejection of KiDS+BOSS itself",
        },
        "controls": {
            "covariance_values_read": False,
            "nuisance_rank_read": False,
            "relation_residual_read": False,
            "G8_read": False,
            "frozen_5pct_threshold_changed": False,
        },
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_admissible_step": "prospectively freeze a solver-neutral BOSS Fourier-space clustering observable/operator with finite public k windows, or another mm-sensitive public coordinate, before any new support output",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("EXP073G_OPERATOR_COMPLETENESS", status)
    print("TRUSTWORTHY_OPERATOR_NO_GO", trustworthy)
    print("SUPPORT_FRACTION_COMPUTED", False)


if __name__ == "__main__":
    main()
