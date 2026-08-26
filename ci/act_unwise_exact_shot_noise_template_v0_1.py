#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import numpy as np
import yaml

PINNED_COMMIT = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
PINNED_ARCHIVE_SHA256 = "1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570"
SAMPLES = ("Blue_ACT", "Green_ACT")
C1_TOL = 5e-11
C2_RTOL = 5e-12
C3_MIN_DELTA = 1e-6
EXPECTED_RANGES = {
    "gg": {"Blue_ACT": [100, 402], "Green_ACT": [100, 402]},
    "kg": {"Blue_ACT": [51, 402], "Green_ACT": [51, 402]},
}
EXPECTED_ELL = {
    "gg": [126.5, 176.5, 226.5, 276.5, 326.5, 376.5],
    "kg": [76.5, 126.5, 176.5, 226.5, 276.5, 326.5, 376.5],
}
LOG10SN = {"Blue_ACT": -7.05, "Green_ACT": -6.79}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def find_data_root(root: Path) -> Path:
    candidates = []
    for p in [root, *root.rglob("*")]:
        if p.is_dir() and all((p / x).is_dir() for x in ("bandpowers", "covariances", "aux_data")):
            candidates.append(p)
    if not candidates:
        raise FileNotFoundError("no directory contains bandpowers/, covariances/, aux_data/")
    candidates.sort(key=lambda p: (len(p.parts), str(p)))
    return candidates[0]


def load_defaults_yaml(path: Path) -> dict:
    text = path.read_text()
    text = re.sub(r"!defaults\s*\[[^\]]*\]", "null", text)
    return yaml.safe_load(text)


def select_mask(rec: dict, ranges: list[int]) -> tuple[np.ndarray, list[float]]:
    edges = np.asarray(rec["ell_bin_edges"], dtype=float)[:60]
    centers = (edges[:-1] + edges[1:]) / 2.0
    cond = (ranges[0] <= edges[:-1]) & (edges[1:] < ranges[1])
    return cond, [float(x) for x in centers[cond]]


def direct_exact_template(coupling, window, transfer):
    c = np.asarray(coupling, dtype=np.float64)
    w = np.asarray(window, dtype=np.float64)
    t = np.asarray(transfer, dtype=np.float64)
    ones = np.ones(c.shape[0], dtype=np.float64)
    w2 = float(np.sum(c[0, :], dtype=np.float64))
    rhs = w2 * ones
    x = np.linalg.solve(c, rhs)
    residual = c @ x - rhs
    rel = float(np.max(np.abs(residual)) / max(np.max(np.abs(rhs)), 1e-300))
    cond = float(np.linalg.cond(c))
    bp = (w @ x) * t
    return x, bp, w2, rel, cond


def upstream_reference_template(coupling, window, transfer, w2):
    c = np.asarray(coupling, dtype=np.float64)
    w = np.asarray(window, dtype=np.float64)
    t = np.asarray(transfer, dtype=np.float64)
    # Pinned NaMasterPowerSpectrumBinning algebra: D = W C^{-1}; D (w2 * 1) * T.
    decoupling = w @ np.linalg.inv(c)
    ref = (decoupling @ (float(w2) * np.ones(c.shape[0], dtype=np.float64))) * t
    return ref


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--external-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    repo = Path(args.external_repo).resolve()
    data_root = find_data_root(Path(args.extracted_root).resolve())
    archive = Path(args.archive).resolve()
    output = Path(args.output).resolve()

    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    digest = sha256(archive)
    provenance_ok = commit == PINNED_COMMIT and digest == PINNED_ARCHIVE_SHA256

    pkg = repo / "unWISExLens_lklh"
    defaults = load_defaults_yaml(pkg / "unWISExLensLklh.yaml")
    binning = yaml.safe_load((pkg / "config_files" / "binning_setup.yaml").read_text())
    helper_source = (pkg / "auxiliary" / "binning_helpers.py").read_text().replace(" ", "")
    source_contract = all(tok in helper_source for tok in (
        "bandpower_windows@np.linalg.inv(self.__coupling_matrix)",
        "self.__decoupling_matrix@(self.__coupling_matrix@padded_cells",
        "white_noise*self.__w2",
    ))

    shared_path = data_root / "aux_data" / "bandwindow_matrices" / binning["Blue_ACT"]["bandwindow_matrix_path"]
    same_path = all(binning[s]["bandwindow_matrix_path"] == binning["Blue_ACT"]["bandwindow_matrix_path"] for s in SAMPLES)
    obj = np.load(shared_path, allow_pickle=True).item()

    coupling = np.asarray(obj["gg"]["coupling"], dtype=np.float64)
    window_gg = np.asarray(obj["gg"]["bandwindow"], dtype=np.float64)
    window_kg = np.asarray(obj["kg"]["bandwindow"], dtype=np.float64)
    shape_ok = coupling.shape == (6144, 6144) and window_gg.shape == (59, 6144) and window_kg.shape == (59, 6144)
    finite_inputs = bool(np.all(np.isfinite(coupling)) and np.all(np.isfinite(window_gg)) and np.all(np.isfinite(window_kg)))

    sample_records = {}
    final_vector = []
    final_order = []
    c1_all = provenance_ok and source_contract and same_path and shape_ok and finite_inputs
    c2_all = True
    c3_all = True
    c4_all = True

    rng = np.random.default_rng(20260826 + 3)
    signal_gg = 2e-7 * (1.0 + 0.15 * np.sin(np.arange(6144) / 137.0)) + 1e-9 * rng.normal(size=6144)
    signal_kg = 9e-8 * (1.0 + 0.11 * np.cos(np.arange(6144) / 163.0)) + 7e-10 * rng.normal(size=6144)

    for sample in SAMPLES:
        rec = binning[sample]
        transfer_data = np.asarray(np.loadtxt(data_root / "aux_data" / "transfer_functions" / rec["transfer_path"]), dtype=np.float64)
        transfer_shape_ok = transfer_data.shape == (59, 3)
        tgg, tkg = transfer_data[:, 1], transfer_data[:, 2]

        x, exact_unit, w2, rel, condnum = direct_exact_template(coupling, window_gg, tgg)
        c1 = bool(np.all(np.isfinite(x)) and np.isfinite(condnum) and rel <= C1_TOL)
        c1_all &= c1

        ref_unit = upstream_reference_template(coupling, window_gg, tgg, w2)
        gg_ranges = [int(v) for v in defaults["lranges_gg"][sample]]
        kg_ranges = [int(v) for v in defaults["lranges_kg"][sample]]
        gg_mask, gg_ell = select_mask(rec, gg_ranges)
        kg_mask, kg_ell = select_mask(rec, kg_ranges)
        selected_exact = exact_unit[gg_mask]
        selected_ref = ref_unit[gg_mask]
        max_abs_diff = float(np.max(np.abs(selected_exact - selected_ref)))
        threshold = float(C2_RTOL * max(1.0, float(np.max(np.abs(selected_ref)))))
        c2 = bool(selected_exact.shape == selected_ref.shape and np.all(np.isfinite(selected_exact)) and np.all(np.isfinite(selected_ref)) and max_abs_diff <= threshold)
        c2_all &= c2

        max_nonconst = float(np.max(np.abs(x - 1.0)))
        c3 = bool(max_nonconst > C3_MIN_DELTA)
        c3_all &= c3

        range_ok = gg_ranges == EXPECTED_RANGES["gg"][sample] and kg_ranges == EXPECTED_RANGES["kg"][sample]
        ell_ok = gg_ell == EXPECTED_ELL["gg"] and kg_ell == EXPECTED_ELL["kg"]
        noise_amp = float(10.0 ** LOG10SN[sample])
        gg_bp = (window_gg @ signal_gg) * tgg + noise_amp * exact_unit
        kg_bp = (window_kg @ signal_kg) * tkg
        gg_sel = gg_bp[gg_mask]
        kg_sel = kg_bp[kg_mask]
        vec = np.concatenate([gg_sel, kg_sel])
        expected_len = 13
        c4 = bool(transfer_shape_ok and range_ok and ell_ok and vec.shape == (expected_len,) and np.all(np.isfinite(vec)))
        c4_all &= c4
        final_vector.extend(float(v) for v in vec)
        final_order.extend([f"{sample}:gg:{ell}" for ell in gg_ell] + [f"{sample}:kg:{ell}" for ell in kg_ell])

        sample_records[sample] = {
            "C1": {"relative_residual": rel, "threshold": C1_TOL, "condition_number": condnum, "w2": w2, "pass": c1},
            "C2": {"selected_count": int(selected_exact.size), "max_abs_difference": max_abs_diff, "threshold": threshold, "pass": c2},
            "C3": {"max_abs_x_minus_one": max_nonconst, "minimum_required": C3_MIN_DELTA, "pass": c3},
            "C4": {"gg_ranges": gg_ranges, "kg_ranges": kg_ranges, "gg_ell": gg_ell, "kg_ell": kg_ell, "sample_vector_length": int(vec.size), "pass": c4},
        }

    expected_order = (
        [f"Blue_ACT:gg:{x}" for x in EXPECTED_ELL["gg"]]
        + [f"Blue_ACT:kg:{x}" for x in EXPECTED_ELL["kg"]]
        + [f"Green_ACT:gg:{x}" for x in EXPECTED_ELL["gg"]]
        + [f"Green_ACT:kg:{x}" for x in EXPECTED_ELL["kg"]]
    )
    global_c4 = bool(c4_all and len(final_vector) == 26 and final_order == expected_order and np.all(np.isfinite(final_vector)))
    passed = bool(c1_all and c2_all and c3_all and global_c4)
    status = "PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1" if passed else "FAIL_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1"

    result = {
        "experiment": "Exp066C",
        "status": status,
        "scope": "exact shot-noise forward-operator correction only; no observational fit, G7 law search, or withheld-family evaluation",
        "pinned_external_repo": "ACTCollaboration/unWISExLens_lklh",
        "pinned_commit": commit,
        "archive_sha256": digest,
        "provenance_pass": provenance_ok,
        "frozen_criteria": {"C1_relative_solve_tolerance": C1_TOL, "C2_relative_equivalence_factor": C2_RTOL, "C3_min_nonconstant_delta": C3_MIN_DELTA},
        "operator_contract": {"source_contract_pass": source_contract, "shared_blue_green_bandwindow_path": same_path, "matrix_shapes_pass": shape_ok, "finite_inputs": finite_inputs},
        "checks": {
            "C1_exact_linear_solve_closure": {"pass": bool(c1_all)},
            "C2_upstream_bandpower_equivalence": {"pass": bool(c2_all)},
            "C3_nonconstant_template_control": {"pass": bool(c3_all)},
            "C4_selected_vector_closure": {"pass": global_c4, "final_vector_length": len(final_vector), "final_order": final_order},
        },
        "samples": sample_records,
        "anti_retuning": "No pseudoinverse, jitter, regularisation, threshold relaxation, cut changes, ordering changes, nuisance changes, or reclassification of Exp066B.",
        "immutable_lineage": {"Exp066B": "FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1"},
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
