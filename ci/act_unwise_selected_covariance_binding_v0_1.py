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
EXPECTED_RANGES = {
    "gg": {"Blue_ACT": [100, 402], "Green_ACT": [100, 402]},
    "kg": {"Blue_ACT": [51, 402], "Green_ACT": [51, 402]},
}
INV_TOL = 1e-8


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
    # The pinned defaults file contains Cobaya !defaults tags only in nuisance-prior
    # declarations, irrelevant to this audit. Replace their values by null while
    # preserving all likelihood range settings verbatim.
    text = path.read_text()
    text = re.sub(r"!defaults\s*\[[^\]]*\]", "null", text)
    return yaml.safe_load(text)


def select_from_matrix(mat: np.ndarray, selection_a: np.ndarray, selection_b: np.ndarray | None = None) -> np.ndarray:
    # Literal semantics of pinned auxiliary_functions.select_from_matrix.
    if selection_b is None:
        selection_b = selection_a
    assert mat.shape == (len(selection_a), len(selection_b))
    selection_matrix = np.outer(selection_a, selection_b)
    return mat[np.where(selection_matrix)].reshape(int(np.sum(selection_a)), int(np.sum(selection_b)))


def matrix_stats(x: np.ndarray) -> dict:
    finite = bool(np.all(np.isfinite(x)))
    symmetric = bool(np.allclose(x, x.T, rtol=1e-10, atol=1e-24))
    xs = (x + x.T) / 2.0
    eig = np.linalg.eigvalsh(xs)
    chol_ok = False
    inv_ok = False
    inv_resid = None
    if finite and symmetric:
        try:
            np.linalg.cholesky(xs)
            chol_ok = True
        except np.linalg.LinAlgError:
            pass
        try:
            inv = np.linalg.inv(xs)
            inv_resid = float(np.linalg.norm(xs @ inv - np.eye(xs.shape[0]), ord=np.inf))
            inv_ok = bool(np.isfinite(inv_resid) and inv_resid <= INV_TOL)
        except np.linalg.LinAlgError:
            pass
    return {
        "shape": list(x.shape),
        "finite": finite,
        "symmetric": symmetric,
        "lambda_min": float(eig[0]),
        "lambda_max": float(eig[-1]),
        "positive_definite": bool(finite and symmetric and eig[0] > 0.0),
        "cholesky_success": chol_ok,
        "inverse_residual_inf": inv_resid,
        "inverse_residual_pass": inv_ok,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--external-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    repo = Path(args.external_repo).resolve()
    data_root = find_data_root(Path(args.extracted_root).resolve())
    archive = Path(args.archive).resolve()
    outpath = Path(args.output).resolve()

    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    digest = sha256(archive)

    pkg = repo / "unWISExLens_lklh"
    defaults = load_defaults_yaml(pkg / "unWISExLensLklh.yaml")
    cfg = pkg / "config_files"
    binning = yaml.safe_load((cfg / "binning_setup.yaml").read_text())
    data_names = yaml.safe_load((cfg / "data_filenames.yaml").read_text())
    cov_names = yaml.safe_load((cfg / "covmat_filenames_cmbmarg.yaml").read_text())

    provenance_pass = commit == PINNED_COMMIT and digest == PINNED_ARCHIVE_SHA256
    range_pass = True
    sample_records = {}
    selections = {}
    selected_covs = {}
    sample_pass = True

    for s in SAMPLES:
        rgg = [int(x) for x in defaults["lranges_gg"][s]]
        rkg = [int(x) for x in defaults["lranges_kg"][s]]
        range_ok = rgg == EXPECTED_RANGES["gg"][s] and rkg == EXPECTED_RANGES["kg"][s]
        range_pass &= range_ok

        rec = binning[s]
        transfer = np.asarray(np.loadtxt(data_root / "aux_data" / "transfer_functions" / rec["transfer_path"]), float)
        edges_all = np.asarray(rec["ell_bin_edges"], float)
        edges = edges_all[: transfer.shape[0] + 1]
        centers = (edges[:-1] + edges[1:]) / 2.0

        data = np.asarray(np.loadtxt(data_root / "bandpowers" / data_names[s]), float)
        row_match = bool(data.ndim == 2 and data.shape[0] == len(centers))
        ell_match = bool(row_match and np.allclose(data[:, 0], centers, rtol=0.0, atol=1e-10))

        cond_gg = (rgg[0] <= edges[:-1]) & (edges[1:] < rgg[1])
        cond_kg = (rkg[0] <= edges[:-1]) & (edges[1:] < rkg[1])
        selection = np.concatenate([cond_gg, cond_kg])
        selections[s] = selection

        cov = np.asarray(np.loadtxt(data_root / "covariances" / cov_names[s]), float)
        shape_ok = cov.shape == (2 * len(centers), 2 * len(centers))
        if shape_ok:
            csel = select_from_matrix(cov, selection)
            selected_covs[s] = csel
            cstats = matrix_stats(csel)
        else:
            cstats = {"shape": list(cov.shape), "positive_definite": False, "cholesky_success": False, "inverse_residual_pass": False}

        counts_ok = int(np.sum(cond_gg)) > 0 and int(np.sum(cond_kg)) > 0
        ok = bool(range_ok and row_match and ell_match and shape_ok and counts_ok and cstats.get("positive_definite", False) and cstats.get("cholesky_success", False) and cstats.get("inverse_residual_pass", False))
        sample_pass &= ok
        sample_records[s] = {
            "ranges": {"gg": rgg, "kg": rkg},
            "range_match": range_ok,
            "n_bins": int(len(centers)),
            "bandpower_rows_match_bins": row_match,
            "bandpower_ells_match_bin_midpoints": ell_match,
            "selected_counts": {"gg": int(np.sum(cond_gg)), "kg": int(np.sum(cond_kg)), "total": int(np.sum(selection))},
            "selected_ell_midpoints": {
                "gg": [float(x) for x in centers[cond_gg]],
                "kg": [float(x) for x in centers[cond_kg]],
            },
            "full_covariance_shape": list(cov.shape),
            "selected_covariance": cstats,
            "pass": ok,
        }

    cross_key = "Blue_ACT_X_Green_ACT"
    cross_path = data_root / "covariances" / cov_names[cross_key]
    cross = np.asarray(np.loadtxt(cross_path), float)
    cross_shape_ok = cross.shape == (len(selections["Blue_ACT"]), len(selections["Green_ACT"]))
    if cross_shape_ok:
        xsel = select_from_matrix(cross, selections["Blue_ACT"], selections["Green_ACT"])
        combined = np.block([
            [selected_covs["Blue_ACT"], xsel],
            [xsel.T, selected_covs["Green_ACT"]],
        ])
        combined_stats = matrix_stats(combined)
    else:
        xsel = np.empty((0, 0))
        combined_stats = {"positive_definite": False, "cholesky_success": False, "inverse_residual_pass": False}

    source = (pkg / "unWISExLensLklh.py").read_text()
    source_checks = {
        "constructs_cond_gg": "cond_gg = (self.lranges_gg[s][0] <=" in source,
        "constructs_cond_kg": "cond_kg = (self.lranges_kg[s][0] <=" in source,
        "selects_auto_covariance": "select_from_matrix(cov, ell_selection)" in source,
        "selects_cross_covariance": "cross_cov = select_from_matrix" in source,
        "assembles_cross_transpose": "= cross_cov.T" in source,
    }
    source_pass = all(source_checks.values())

    combined_pass = bool(
        cross_shape_ok
        and combined_stats.get("positive_definite", False)
        and combined_stats.get("cholesky_success", False)
        and combined_stats.get("inverse_residual_pass", False)
    )
    passed = bool(provenance_pass and range_pass and sample_pass and combined_pass and source_pass)
    status = "PASS_ACT_UNWISE_SELECTED_COVARIANCE_ELIGIBLE_V0_1" if passed else "FAIL_ACT_UNWISE_SELECTED_COVARIANCE_ELIGIBILITY_V0_1"

    result = {
        "experiment": "Exp065B",
        "status": status,
        "scope": "corrective observational eligibility audit; no G7 law search and no withheld-family response",
        "pinned_external_repo": "ACTCollaboration/unWISExLens_lklh",
        "pinned_commit": commit,
        "archive_sha256": digest,
        "checks": {
            "provenance": {"pass": provenance_pass, "expected_commit": PINNED_COMMIT, "expected_archive_sha256": PINNED_ARCHIVE_SHA256},
            "default_ACT_ranges": {"pass": range_pass, "expected": EXPECTED_RANGES},
            "samples": {"pass": sample_pass, "records": sample_records},
            "cross_covariance": {"pass": cross_shape_ok, "path": str(cross_path.relative_to(data_root)), "full_shape": list(cross.shape), "selected_shape": list(xsel.shape)},
            "combined_selected_covariance": {"pass": combined_pass, **combined_stats},
            "likelihood_selection_source_contract": {"pass": source_pass, **source_checks},
        },
        "anti_regularization": "No jitter, eigenvalue clipping, diagonal loading, shrinkage, nearest-PSD projection, or scale-cut retuning is applied.",
        "interpretation": "PASS would establish eligibility of this selected observational kernel/covariance block only; it would not establish a DSIR law.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
