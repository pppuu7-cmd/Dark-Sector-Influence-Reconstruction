#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import yaml

PINNED_COMMIT = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
PINNED_ARCHIVE_SHA256 = "1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570"
SEED = 20260827
TOL = 5e-13
SOLVE_RESIDUAL_TOL = 1e-10
EXPECTED_GG_ELL = [126.5, 176.5, 226.5, 276.5, 326.5, 376.5]
LOG10SN = {"Blue_ACT": -7.05, "Green_ACT": -6.79}
SAMPLES = ("Blue_ACT", "Green_ACT")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.act_unwise_noise import exact_namaster_noise_template  # noqa: E402


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


def compare(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if a.shape != b.shape or not (np.all(np.isfinite(a)) and np.all(np.isfinite(b))):
        return {"pass": False, "shape_reference": list(a.shape), "shape_test": list(b.shape)}
    diff = float(np.max(np.abs(a - b))) if a.size else 0.0
    scale = max(1.0, float(np.max(np.abs(a))) if a.size else 0.0)
    threshold = TOL * scale
    return {"pass": bool(diff <= threshold), "max_abs_difference": diff, "threshold": threshold}


def small_matrix_control():
    rng = np.random.default_rng(SEED)
    n, m = 32, 7
    C = np.eye(n) + 0.03 * rng.normal(size=(n, n))
    W = rng.normal(size=(m, n))
    T = 0.75 + 0.5 * rng.random(m)
    N = 2.7e-7
    ones = np.ones(n)
    w2 = float(np.sum(C[0]))
    reference = (W @ np.linalg.inv(C)) @ (N * w2 * ones) * T
    test, diag = exact_namaster_noise_template(C, W, T, noise=N)
    rec = compare(reference, test)
    rec.update({
        "solve_residual_inf": diag["solve_residual_inf"],
        "solve_residual_threshold": SOLVE_RESIDUAL_TOL,
        "solve_pass": bool(diag["solve_residual_inf"] <= SOLVE_RESIDUAL_TOL),
    })
    rec["pass"] = bool(rec["pass"] and rec["solve_pass"])
    return rec


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
    provenance_pass = commit == PINNED_COMMIT and digest == PINNED_ARCHIVE_SHA256

    helper_source = (repo / "unWISExLens_lklh" / "auxiliary" / "binning_helpers.py").read_text()
    compact = helper_source.replace(" ", "")
    source_tokens = [
        "self.__decoupling_matrix=bandpower_windows@np.linalg.inv(self.__coupling_matrix)",
        "self.__w2=np.sum(self.__coupling_matrix[0,:])",
        "self.__decoupling_matrix@(self.__coupling_matrix@padded_cells+white_noise*self.__w2)",
    ]
    source_contract = all(token in compact for token in source_tokens)

    small = small_matrix_control()

    binning = yaml.safe_load((repo / "unWISExLens_lklh" / "config_files" / "binning_setup.yaml").read_text())
    bw_name = binning["Blue_ACT"]["bandwindow_matrix_path"]
    same_matrix_path = all(binning[s]["bandwindow_matrix_path"] == bw_name for s in SAMPLES)
    bw_path = data_root / "aux_data" / "bandwindow_matrices" / bw_name
    obj = np.load(bw_path, allow_pickle=True).item()
    C = np.asarray(obj["gg"]["coupling"], dtype=np.float64)
    W = np.asarray(obj["gg"]["bandwindow"], dtype=np.float64)

    actual_shape_pass = C.shape == (6144, 6144) and W.shape == (59, 6144)
    ones = np.ones(C.shape[0], dtype=np.float64)
    y = np.linalg.solve(C, ones)
    solve_residual = float(np.max(np.abs(C @ y - ones)))
    solve_pass = bool(np.all(np.isfinite(y)) and solve_residual <= SOLVE_RESIDUAL_TOL)
    w2 = float(np.sum(C[0, :], dtype=np.float64))

    sample_records = {}
    sample_pass = True
    descriptive_diffs = {}
    for sample in SAMPLES:
        rec = binning[sample]
        transfer_data = np.asarray(
            np.loadtxt(data_root / "aux_data" / "transfer_functions" / rec["transfer_path"]),
            dtype=np.float64,
        )
        transfer = transfer_data[:, 1]
        exact_unit = w2 * (W @ y) * transfer
        shortcut_unit = (W @ np.ones(W.shape[1], dtype=np.float64)) * transfer
        exact_nonzero = bool(np.count_nonzero(exact_unit) > 0 and np.ptp(exact_unit) > 0)
        finite = bool(np.all(np.isfinite(exact_unit)))

        edges = np.asarray(rec["ell_bin_edges"], dtype=float)[:60]
        centers = (edges[:-1] + edges[1:]) / 2.0
        cond = (100 <= edges[:-1]) & (edges[1:] < 402)
        selected_ell = [float(x) for x in centers[cond]]
        ell_pass = selected_ell == EXPECTED_GG_ELL and int(np.sum(cond)) == 6
        selected = (10.0 ** LOG10SN[sample]) * exact_unit[cond]
        selected_pass = bool(selected.shape == (6,) and np.all(np.isfinite(selected)) and np.count_nonzero(selected) == 6)

        denom = max(float(np.max(np.abs(exact_unit))), 1e-300)
        shortcut_relative_difference = float(np.max(np.abs(exact_unit - shortcut_unit)) / denom)
        descriptive_diffs[sample] = shortcut_relative_difference

        ok = bool(transfer_data.shape == (59, 3) and finite and exact_nonzero and ell_pass and selected_pass)
        sample_pass &= ok
        sample_records[sample] = {
            "transfer_shape": list(transfer_data.shape),
            "selected_ell": selected_ell,
            "selected_noise_values": [float(x) for x in selected],
            "unit_template_min": float(np.min(exact_unit)),
            "unit_template_max": float(np.max(exact_unit)),
            "unit_template_nonconstant_nonzero": exact_nonzero,
            "shortcut_relative_difference_descriptive": shortcut_relative_difference,
            "pass": ok,
        }

    C1 = C @ np.ones(C.shape[1], dtype=np.float64)
    exp066b_residual = float(np.max(np.abs(C1 - w2)) / max(abs(w2), 1e-300))

    c2_pass = bool(actual_shape_pass and solve_pass and sample_pass)
    passed = bool(provenance_pass and source_contract and small["pass"] and c2_pass and same_matrix_path)
    status = "PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1" if passed else "FAIL_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1"

    result = {
        "experiment": "Exp066C",
        "status": status,
        "scope": "corrective survey-operator test after permanent Exp066B FAIL; no G7 law search",
        "pinned_external_repo": "ACTCollaboration/unWISExLens_lklh",
        "pinned_commit": commit,
        "archive_sha256": digest,
        "provenance_pass": provenance_pass,
        "frozen_numerics": {
            "rng_seed": SEED,
            "dtype": "float64",
            "equivalence_tolerance": TOL,
            "solve_residual_tolerance": SOLVE_RESIDUAL_TOL,
        },
        "upstream_source_contract_pass": source_contract,
        "C1_small_matrix_literal_upstream_equivalence": small,
        "C2_released_ACT_exact_solve": {
            "pass": c2_pass,
            "coupling_shape": list(C.shape),
            "bandwindow_shape": list(W.shape),
            "same_blue_green_matrix_path": same_matrix_path,
            "solve_residual_inf": solve_residual,
            "solve_residual_threshold": SOLVE_RESIDUAL_TOL,
            "solve_pass": solve_pass,
            "w2": w2,
            "samples": sample_records,
        },
        "C3_nonshortcut_diagnostic": {
            "exp066b_constant_mode_relative_residual_reproduced": exp066b_residual,
            "exact_vs_rejected_shortcut_relative_difference": descriptive_diffs,
            "role": "descriptive_only",
        },
        "combined_bridge_logic": {
            "Exp066B_B1_free_cleft": "PASS_IMMUTABLE",
            "Exp066B_B2_signal_operator": "PASS_IMMUTABLE",
            "Exp066B_B3_constant_mode_shortcut": "FAIL_IMMUTABLE_REPLACED_ONLY_BY_THIS_SEPARATELY_PREREGISTERED_EXACT_SOLVE",
            "Exp066B_B4_selected_ordering": "PASS_IMMUTABLE",
            "operator_bridge_closed_if_this_experiment_passes": passed,
        },
        "anti_retuning": "No solver, dtype, residual threshold, seed, scale cut, noise amplitude, selected ell, matrix file, or algebra change after execution.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
