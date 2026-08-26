#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
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
EXPECTED_ELL = {
    "gg": [126.5, 176.5, 226.5, 276.5, 326.5, 376.5],
    "kg": [76.5, 126.5, 176.5, 226.5, 276.5, 326.5, 376.5],
}
A2_SYMMETRY_TOL = 1e-12
A3_CHOLESKY_RECON_TOL = 5e-12
A4_WHITENING_IDENTITY_TOL = 5e-10
A5_ROUNDTRIP_TOL = 5e-12
A5_SEED = 20260826 + 67

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.covariance_whitening import (  # noqa: E402
    build_direct_whitener,
    select_from_matrix,
    unwhiten_vector,
    whiten_vector,
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_array(x: np.ndarray) -> str:
    arr = np.ascontiguousarray(np.asarray(x, dtype=np.float64))
    return hashlib.sha256(arr.view(np.uint8)).hexdigest()


def find_data_root(root: Path) -> Path:
    candidates: list[Path] = []
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


def make_expected_order() -> list[str]:
    order: list[str] = []
    for sample in SAMPLES:
        order.extend(f"{sample}:gg:{ell}" for ell in EXPECTED_ELL["gg"])
        order.extend(f"{sample}:kg:{ell}" for ell in EXPECTED_ELL["kg"])
    return order


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
    output = Path(args.output).resolve()

    commit = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()
    archive_digest = sha256_file(archive)
    provenance_pass = commit == PINNED_COMMIT and archive_digest == PINNED_ARCHIVE_SHA256

    pkg = repo / "unWISExLens_lklh"
    defaults = load_defaults_yaml(pkg / "unWISExLensLklh.yaml")
    cfg = pkg / "config_files"
    binning = yaml.safe_load((cfg / "binning_setup.yaml").read_text())
    data_names = yaml.safe_load((cfg / "data_filenames.yaml").read_text())
    cov_names = yaml.safe_load((cfg / "covmat_filenames_cmbmarg.yaml").read_text())
    source = (pkg / "unWISExLensLklh.py").read_text()

    # A1: reconstruct the exact sample/channel ordering from the pinned source
    # and config metadata.  No fallback/reordering is allowed.
    source_contract = all(
        token in source
        for token in (
            "residuals.append(np.concatenate([residual_gg, residual_kg]))",
            "ell_selection = np.concatenate(self._ell_selections[i])",
            "select_from_matrix(cov, ell_selection)",
            "cross_cov = select_from_matrix",
            "= cross_cov.T",
        )
    )

    selections: dict[str, np.ndarray] = {}
    selected_covs: dict[str, np.ndarray] = {}
    sample_records: dict[str, dict] = {}
    reconstructed_order: list[str] = []
    a1_samples_pass = True

    for sample in SAMPLES:
        rgg = [int(v) for v in defaults["lranges_gg"][sample]]
        rkg = [int(v) for v in defaults["lranges_kg"][sample]]
        ranges_pass = (
            rgg == EXPECTED_RANGES["gg"][sample]
            and rkg == EXPECTED_RANGES["kg"][sample]
        )

        rec = binning[sample]
        transfer = np.asarray(
            np.loadtxt(data_root / "aux_data" / "transfer_functions" / rec["transfer_path"]),
            dtype=np.float64,
        )
        edges = np.asarray(rec["ell_bin_edges"], dtype=np.float64)[: transfer.shape[0] + 1]
        centers = (edges[:-1] + edges[1:]) / 2.0
        cond_gg = (rgg[0] <= edges[:-1]) & (edges[1:] < rgg[1])
        cond_kg = (rkg[0] <= edges[:-1]) & (edges[1:] < rkg[1])
        selection = np.concatenate([cond_gg, cond_kg])
        selections[sample] = selection

        selected_gg = [float(x) for x in centers[cond_gg]]
        selected_kg = [float(x) for x in centers[cond_kg]]
        ell_pass = selected_gg == EXPECTED_ELL["gg"] and selected_kg == EXPECTED_ELL["kg"]
        count_pass = int(np.sum(cond_gg)) == 6 and int(np.sum(cond_kg)) == 7 and int(np.sum(selection)) == 13

        data = np.asarray(
            np.loadtxt(data_root / "bandpowers" / data_names[sample]),
            dtype=np.float64,
        )
        data_order_pass = bool(
            data.ndim == 2
            and data.shape[0] == centers.size
            and np.allclose(data[:, 0], centers, rtol=0.0, atol=1e-10)
        )

        cov = np.asarray(
            np.loadtxt(data_root / "covariances" / cov_names[sample]),
            dtype=np.float64,
        )
        cov_shape_pass = cov.shape == (2 * centers.size, 2 * centers.size)
        if cov_shape_pass:
            selected_covs[sample] = select_from_matrix(cov, selection)

        reconstructed_order.extend(f"{sample}:gg:{ell}" for ell in selected_gg)
        reconstructed_order.extend(f"{sample}:kg:{ell}" for ell in selected_kg)

        sample_ok = bool(
            ranges_pass and ell_pass and count_pass and data_order_pass and cov_shape_pass
        )
        a1_samples_pass &= sample_ok
        sample_records[sample] = {
            "ranges": {"gg": rgg, "kg": rkg},
            "selected_counts": {
                "gg": int(np.sum(cond_gg)),
                "kg": int(np.sum(cond_kg)),
                "total": int(np.sum(selection)),
            },
            "selected_ell_midpoints": {"gg": selected_gg, "kg": selected_kg},
            "data_rows_and_ell_order_pass": data_order_pass,
            "full_covariance_shape": list(cov.shape),
            "pass": sample_ok,
        }

    cross_key = "Blue_ACT_X_Green_ACT"
    cross = np.asarray(
        np.loadtxt(data_root / "covariances" / cov_names[cross_key]),
        dtype=np.float64,
    )
    cross_shape_pass = cross.shape == (
        selections["Blue_ACT"].size,
        selections["Green_ACT"].size,
    )
    if cross_shape_pass:
        xsel = select_from_matrix(
            cross, selections["Blue_ACT"], selections["Green_ACT"]
        )
        sigma = np.block(
            [
                [selected_covs["Blue_ACT"], xsel],
                [xsel.T, selected_covs["Green_ACT"]],
            ]
        )
    else:
        xsel = np.empty((0, 0), dtype=np.float64)
        sigma = np.empty((0, 0), dtype=np.float64)

    expected_order = make_expected_order()
    ordering_pass = reconstructed_order == expected_order and len(reconstructed_order) == 26
    a1_pass = bool(
        provenance_pass
        and source_contract
        and a1_samples_pass
        and cross_shape_pass
        and xsel.shape == (13, 13)
        and ordering_pass
        and sigma.shape == (26, 26)
    )

    # A2: evaluate the released selected covariance exactly as assembled.  No
    # symmetrisation is performed before this or any later hard check.
    if sigma.shape == (26, 26):
        finite = bool(np.all(np.isfinite(sigma)))
        diag = np.diag(sigma)
        positive_diagonal = bool(np.all(diag > 0.0))
        max_abs_sigma = float(np.max(np.abs(sigma)))
        asymmetry_ratio = float(
            np.max(np.abs(sigma - sigma.T)) / max(max_abs_sigma, 1e-300)
        )
    else:
        finite = False
        positive_diagonal = False
        asymmetry_ratio = float("inf")
    a2_pass = bool(
        sigma.shape == (26, 26)
        and finite
        and positive_diagonal
        and asymmetry_ratio <= A2_SYMMETRY_TOL
    )

    # A3: direct Cholesky on the unmodified covariance.
    L = None
    W = None
    cholesky_success = False
    cholesky_reconstruction_residual = None
    lambda_min = None
    lambda_max = None
    if sigma.shape == (26, 26) and finite:
        try:
            eigvals = np.linalg.eigvalsh(sigma)
            lambda_min = float(eigvals[0])
            lambda_max = float(eigvals[-1])
        except np.linalg.LinAlgError:
            pass
        try:
            L, W = build_direct_whitener(sigma)
            cholesky_success = True
            denom = max(float(np.linalg.norm(sigma, ord=np.inf)), 1e-300)
            cholesky_reconstruction_residual = float(
                np.linalg.norm(L @ L.T - sigma, ord=np.inf) / denom
            )
        except np.linalg.LinAlgError:
            pass
    a3_pass = bool(
        cholesky_success
        and cholesky_reconstruction_residual is not None
        and cholesky_reconstruction_residual <= A3_CHOLESKY_RECON_TOL
    )

    # A4: whitening identity from the solve-built W=L^{-1}.
    whitening_identity_residual = None
    if W is not None:
        whitened_cov = W @ sigma @ W.T
        whitening_identity_residual = float(
            np.linalg.norm(
                whitened_cov - np.eye(26, dtype=np.float64), ord=np.inf
            )
        )
    a4_pass = bool(
        whitening_identity_residual is not None
        and whitening_identity_residual <= A4_WHITENING_IDENTITY_TOL
    )

    # A5: frozen deterministic vector round-trip.  Both directions use direct
    # solves; no pseudoinverse or explicit covariance inverse is used.
    roundtrip_relative_inf = None
    vector_hash = None
    if L is not None and W is not None:
        rng = np.random.default_rng(A5_SEED)
        vector = rng.standard_normal(26).astype(np.float64)
        vector_hash = sha256_array(vector)
        whitened = whiten_vector(L, vector)
        recovered = unwhiten_vector(W, whitened)
        roundtrip_relative_inf = float(
            np.linalg.norm(recovered - vector, ord=np.inf)
            / max(float(np.linalg.norm(vector, ord=np.inf)), 1e-300)
        )
    a5_pass = bool(
        roundtrip_relative_inf is not None
        and roundtrip_relative_inf <= A5_ROUNDTRIP_TOL
    )

    passed = bool(a1_pass and a2_pass and a3_pass and a4_pass and a5_pass)
    status = (
        "PASS_ACT_UNWISE_OBSERVATIONAL_COVARIANCE_WHITENING_V0_1"
        if passed
        else "FAIL_ACT_UNWISE_OBSERVATIONAL_COVARIANCE_WHITENING_V0_1"
    )

    result = {
        "experiment": "Exp067A",
        "status": status,
        "scope": "observational covariance selection/whitening closure only; no law fit, null statistic, or withheld-family evaluation",
        "immutable_lineage": {
            "Exp066B": "FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1",
            "Exp066C": "PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1",
        },
        "pinned_external_repo": "ACTCollaboration/unWISExLens_lklh",
        "pinned_commit": commit,
        "archive_sha256": archive_digest,
        "covariance_convention": "raw released selected covariance inherited from Exp065B; no Hartlap rescaling or any other covariance modification in Exp067A",
        "frozen_criteria": {
            "A2_symmetry_ratio_tolerance": A2_SYMMETRY_TOL,
            "A3_cholesky_reconstruction_relative_inf_tolerance": A3_CHOLESKY_RECON_TOL,
            "A4_whitening_identity_inf_tolerance": A4_WHITENING_IDENTITY_TOL,
            "A5_roundtrip_relative_inf_tolerance": A5_ROUNDTRIP_TOL,
            "A5_rng_seed": A5_SEED,
        },
        "checks": {
            "A1_provenance_and_ordering": {
                "pass": a1_pass,
                "provenance_pass": provenance_pass,
                "source_contract_pass": source_contract,
                "sample_metadata_pass": a1_samples_pass,
                "cross_covariance_shape": list(cross.shape),
                "selected_cross_covariance_shape": list(xsel.shape),
                "cross_covariance_shape_pass": cross_shape_pass,
                "reconstructed_order": reconstructed_order,
                "expected_order": expected_order,
                "ordering_pass": ordering_pass,
                "selected_dimension": int(sigma.shape[0]) if sigma.ndim == 2 else 0,
                "samples": sample_records,
            },
            "A2_covariance_symmetry_finite": {
                "pass": a2_pass,
                "shape": list(sigma.shape),
                "finite": finite,
                "strictly_positive_diagonal": positive_diagonal,
                "symmetry_ratio": asymmetry_ratio,
                "threshold": A2_SYMMETRY_TOL,
            },
            "A3_direct_cholesky": {
                "pass": a3_pass,
                "success": cholesky_success,
                "reconstruction_relative_inf": cholesky_reconstruction_residual,
                "threshold": A3_CHOLESKY_RECON_TOL,
                "lambda_min_diagnostic": lambda_min,
                "lambda_max_diagnostic": lambda_max,
            },
            "A4_whitening_identity": {
                "pass": a4_pass,
                "identity_inf_residual": whitening_identity_residual,
                "threshold": A4_WHITENING_IDENTITY_TOL,
            },
            "A5_deterministic_roundtrip": {
                "pass": a5_pass,
                "rng_seed": A5_SEED,
                "input_vector_sha256_float64_bytes": vector_hash,
                "relative_inf_error": roundtrip_relative_inf,
                "threshold": A5_ROUNDTRIP_TOL,
            },
        },
        "operator_hashes": {
            "selected_covariance_float64_bytes_sha256": sha256_array(sigma) if sigma.shape == (26, 26) else None,
            "cholesky_L_float64_bytes_sha256": sha256_array(L) if L is not None else None,
            "whitener_W_float64_bytes_sha256": sha256_array(W) if W is not None else None,
        },
        "anti_regularization": "No symmetrization, Hartlap rescaling, jitter, shrinkage, eigenvalue clipping, diagonal loading, pseudoinverse, nearest-PSD projection, or scale-cut/order retuning is applied.",
        "interpretation": "PASS makes a covariance-whitened observational residual law eligible for later preregistration only; it does not itself close G7.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
