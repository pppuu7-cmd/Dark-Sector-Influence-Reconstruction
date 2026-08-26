#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
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
SEED = 20260826
NELL_SYNTH = 64
TOL = 5e-13
CONSTANT_MODE_TOL = 1e-10
SAMPLES = ("Blue_ACT", "Green_ACT")
EXPECTED_RANGES = {
    "gg": {"Blue_ACT": [100, 402], "Green_ACT": [100, 402]},
    "kg": {"Blue_ACT": [51, 402], "Green_ACT": [51, 402]},
}
EXPECTED_ELL = {
    "gg": [126.5, 176.5, 226.5, 276.5, 326.5, 376.5],
    "kg": [76.5, 126.5, 176.5, 226.5, 276.5, 326.5, 376.5],
}
NUISANCE = {
    "Blue_ACT": {
        "b": 1.6,
        "log10SN": -7.05,
        "s": 0.455,
        "pca": [-0.5843837663087972, -0.3985951242854526, -0.14460224245714698],
        "cb2": [1.0, 0.5551969885793376],
        "cbs": [1.0, 0.16830370991953963],
        "cb3": [1.0, 0.0],
    },
    "Green_ACT": {
        "b": 2.3,
        "log10SN": -6.79,
        "s": 0.653,
        "pca": [-0.30320235632661185, -0.3042716635545827, -0.30615305724122277, -0.0945228819723003, -0.23779156954362762],
        "cb2": [1.0, 0.41552846311201563],
        "cbs": [1.0, 0.21990237272388719],
        "cb3": [1.0, 0.0],
    },
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.act_unwise_bandpower import (  # noqa: E402
    assemble_free_cleft_coeff,
    coupling_constant_mode_residual,
    evaluate_free_cleft_sample,
    namaster_constant_noise_bandpowers,
    namaster_signal_bandpowers,
)


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


def load_upstream_free_cleft_reference(repo: Path):
    model_path = repo / "unWISExLens_lklh" / "theory_modules" / "unWISExkappa_model_freeCLEFT.py"
    source = model_path.read_text()
    tree = ast.parse(source, filename=str(model_path))
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "unWISExLens_theory_model")
    mod = ast.Module(body=[cls], type_ignores=[])
    ast.fix_missing_locations(mod)
    ns = {"np": np, "base_model": object}
    exec(compile(mod, str(model_path), "exec"), ns)
    klass = ns["unWISExLens_theory_model"]
    return klass, source


def load_upstream_coeff_reference(repo: Path):
    helper_path = repo / "unWISExLens_lklh" / "theory_modules" / "model_helpers_unWISExLens.py"
    source = helper_path.read_text()
    tree = ast.parse(source, filename=str(helper_path))
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "CleftInterpolationHelperFreeCleft")
    mod = ast.Module(body=[cls], type_ignores=[])
    ast.fix_missing_locations(mod)
    ns = {"np": np, "CleftInterpolationHelper": object}
    exec(compile(mod, str(helper_path), "exec"), ns)
    klass = ns["CleftInterpolationHelperFreeCleft"]
    obj = object.__new__(klass)
    obj._use_second_order = True
    obj._use_shear = True
    obj._use_third_order = True
    return obj, source


def finite_random(rng, shape, scale=1.0, offset=0.0):
    return offset + scale * rng.normal(size=shape)


def synthetic_raw(rng, n_pca: int):
    L = NELL_SYNTH
    raw = {
        "kg": {
            "kg_b": finite_random(rng, (L, n_pca), 0.03, 0.12),
            "kg_nob": finite_random(rng, (L, 3, 2), 0.02, 0.04),
            "kmu": finite_random(rng, (L,), 0.01, 0.03),
        },
        "gg": {
            "gg_bsq": finite_random(rng, (L, n_pca * n_pca), 0.03, 0.15),
            "gg_b": finite_random(rng, (L, n_pca, 3, 2), 0.015, 0.03),
            "gg_nob1": finite_random(rng, (L, 3, 2), 0.012, 0.02),
            "gg_nob2": finite_random(rng, (L, 3, 4), 0.012, 0.02),
            "gmu_b": finite_random(rng, (L, n_pca), 0.01, 0.025),
            "gmu_nob": finite_random(rng, (L, 3, 2), 0.008, 0.015),
            "mumu": finite_random(rng, (L,), 0.006, 0.012),
        },
    }
    noise = {
        "kg": {"kg_b": finite_random(rng, (L,), 0.001, 0.002)},
        "gg": {
            "gg_bsq": finite_random(rng, (L,), 0.001, 0.003),
            "gg_b": finite_random(rng, (L, 3, 2), 0.0008, 0.0015),
            "gmu_b": finite_random(rng, (L,), 0.0006, 0.0012),
        },
    }
    return raw, noise


def max_abs_diff(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.shape != b.shape:
        return None, None, False
    scale = max(1.0, float(np.max(np.abs(a))) if a.size else 0.0)
    diff = float(np.max(np.abs(a - b))) if a.size else 0.0
    threshold = TOL * scale
    ok = bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b)) and diff <= threshold)
    return diff, threshold, ok


def zero_cleft(raw):
    out = {
        "kg": {k: np.array(v, copy=True) for k, v in raw["kg"].items()},
        "gg": {k: np.array(v, copy=True) for k, v in raw["gg"].items()},
    }
    out["kg"]["kg_nob"].fill(0.0)
    for k in ("gg_b", "gg_nob1", "gg_nob2", "gmu_nob"):
        out["gg"][k].fill(0.0)
    return out


def run_b1(repo: Path):
    Upstream, model_source = load_upstream_free_cleft_reference(repo)
    helper, helper_source = load_upstream_coeff_reference(repo)
    ref_kg = getattr(Upstream, "_unWISExLens_theory_model__kg")
    ref_gg = getattr(Upstream, "_unWISExLens_theory_model__gg")
    source_tokens = [
        "np.einsum('lij, ij->l'",
        "np.einsum('lpij, ij->lp'",
        "np.outer(pca_coeff, pca_coeff).flatten()",
    ]
    source_pass = all(t in model_source for t in source_tokens) and "assemble_cleft_coeff" in helper_source

    rng = np.random.default_rng(SEED)
    samples = {}
    all_ok = source_pass
    for sample in SAMPLES:
        nu = NUISANCE[sample]
        full_pca = np.array([1.0, 1.0, *nu["pca"]], dtype=float)
        raw, noise = synthetic_raw(rng, len(full_pca))

        ours_c1, ours_c2 = assemble_free_cleft_coeff(nu["cb2"], nu["cbs"], nu["cb3"])
        ref_c1, ref_c2 = helper.assemble_cleft_coeff(
            cb2=tuple(nu["cb2"]), cbs=tuple(nu["cbs"]), cb3=tuple(nu["cb3"])
        )
        d1, t1, coeff1_ok = max_abs_diff(ref_c1, ours_c1)
        d2, t2, coeff2_ok = max_abs_diff(ref_c2, ours_c2)

        ours_gg, ours_kg = evaluate_free_cleft_sample(
            raw, b=nu["b"], s=nu["s"], pca_coeff=full_pca,
            cleft_coeff1=ours_c1, cleft_coeff2=ours_c2, noise_bias=noise,
        )
        ref_kg_val = ref_kg(
            raw, nu["b"], nu["s"], ref_c1, full_pca, noise,
        )
        ref_gg_val = ref_gg(
            raw, nu["b"], nu["s"], ref_c1, ref_c2, full_pca, noise,
        )
        dkg, tkg, kg_ok = max_abs_diff(ref_kg_val, ours_kg)
        dgg, tgg, gg_ok = max_abs_diff(ref_gg_val, ours_gg)

        zraw = zero_cleft(raw)
        zgg, zkg = evaluate_free_cleft_sample(
            zraw, b=nu["b"], s=nu["s"], pca_coeff=full_pca,
            cleft_coeff1=ours_c1, cleft_coeff2=ours_c2, noise_bias=noise,
        )
        cleft_delta_gg = float(np.max(np.abs(ours_gg - zgg)))
        cleft_delta_kg = float(np.max(np.abs(ours_kg - zkg)))
        cleft_nonzero = bool(cleft_delta_gg > 1e-12 and cleft_delta_kg > 1e-12)

        ok = bool(coeff1_ok and coeff2_ok and kg_ok and gg_ok and cleft_nonzero)
        all_ok &= ok
        samples[sample] = {
            "n_pca_full": int(len(full_pca)),
            "coeff1": {"max_abs_difference": d1, "threshold": t1, "pass": coeff1_ok},
            "coeff2": {"max_abs_difference": d2, "threshold": t2, "pass": coeff2_ok},
            "kg": {"max_abs_difference": dkg, "threshold": tkg, "pass": kg_ok},
            "gg": {"max_abs_difference": dgg, "threshold": tgg, "pass": gg_ok},
            "cleft_zero_control": {
                "max_abs_delta_gg": cleft_delta_gg,
                "max_abs_delta_kg": cleft_delta_kg,
                "pass": cleft_nonzero,
            },
            "pass": ok,
        }
    return bool(all_ok), {"source_contract": source_pass, "samples": samples}


def small_matrix_operator_regression():
    rng = np.random.default_rng(SEED + 1)
    n = 16
    m = 5
    a = rng.normal(size=(n, n))
    C = a @ a.T + 2.0 * np.eye(n)
    W = rng.normal(size=(m, n))
    T = 0.8 + 0.4 * rng.random(m)
    x = rng.normal(size=n)
    ref = (W @ np.linalg.inv(C)) @ (C @ x) * T
    ours = namaster_signal_bandpowers(x, W, T)
    diff, threshold, ok = max_abs_diff(ref, ours)
    return ok, {"max_abs_difference": diff, "threshold": threshold, "pass": ok}


def run_b2_b3_b4(repo: Path, data_root: Path):
    pkg = repo / "unWISExLens_lklh"
    defaults = load_defaults_yaml(pkg / "unWISExLensLklh.yaml")
    binning = yaml.safe_load((pkg / "config_files" / "binning_setup.yaml").read_text())
    helper_source = (pkg / "auxiliary" / "binning_helpers.py").read_text()
    source_tokens = [
        "bandpower_windows@np.linalg.inv(self.__coupling_matrix)",
        "self.__decoupling_matrix@(self.__coupling_matrix@padded_cells",
        "white_noise*self.__w2",
    ]
    source_pass = all(t in helper_source.replace(" ", "") for t in [s.replace(" ", "") for s in source_tokens])

    small_ok, small_rec = small_matrix_operator_regression()

    shared_path = data_root / "aux_data" / "bandwindow_matrices" / binning["Blue_ACT"]["bandwindow_matrix_path"]
    same_path = all(binning[s]["bandwindow_matrix_path"] == binning["Blue_ACT"]["bandwindow_matrix_path"] for s in SAMPLES)
    obj = np.load(shared_path, allow_pickle=True).item()

    channel_records = {}
    actual_operator_ok = source_pass and small_ok and same_path
    constant_mode_ok = True
    selected_records = {}
    ordering = []

    rng = np.random.default_rng(SEED + 2)
    for channel in ("gg", "kg"):
        coupling = np.asarray(obj[channel]["coupling"], dtype=float)
        window = np.asarray(obj[channel]["bandwindow"], dtype=float)
        coupling_shape_ok = coupling.shape == (6144, 6144)
        window_shape_ok = window.shape == (59, 6144)
        finite = bool(np.all(np.isfinite(coupling)) and np.all(np.isfinite(window)))
        cm_resid, w2 = coupling_constant_mode_residual(coupling)
        cm_pass = bool(cm_resid <= CONSTANT_MODE_TOL)
        if channel == "gg":
            constant_mode_ok &= cm_pass
        cells = 2e-7 * (1.0 + 0.15 * np.sin(np.arange(6144) / 137.0)) + 1e-9 * rng.normal(size=6144)
        # Transfer is sample dependent; evaluate below.
        channel_records[channel] = {
            "coupling_shape": list(coupling.shape),
            "bandwindow_shape": list(window.shape),
            "finite": finite,
            "constant_mode_relative_residual": cm_resid,
            "constant_mode_threshold": CONSTANT_MODE_TOL,
            "constant_mode_pass": cm_pass,
            "w2": w2,
            "test_cells": cells,
            "window": window,
        }
        actual_operator_ok &= bool(coupling_shape_ok and window_shape_ok and finite)

    range_ok = True
    for sample in SAMPLES:
        rec = binning[sample]
        transfer_data = np.asarray(np.loadtxt(data_root / "aux_data" / "transfer_functions" / rec["transfer_path"]), dtype=float)
        transfer_shape_ok = transfer_data.shape == (59, 3)
        sample_rec = {"transfer_shape": list(transfer_data.shape), "channels": {}}
        for channel, col in (("gg", 1), ("kg", 2)):
            ranges = [int(x) for x in defaults[f"lranges_{channel}"][sample]]
            expected_ranges = EXPECTED_RANGES[channel][sample]
            range_match = ranges == expected_ranges
            range_ok &= range_match
            edges = np.asarray(rec["ell_bin_edges"], dtype=float)[:60]
            centers = (edges[:-1] + edges[1:]) / 2.0
            cond = (ranges[0] <= edges[:-1]) & (edges[1:] < ranges[1])
            selected = [float(x) for x in centers[cond]]
            expected_ell = EXPECTED_ELL[channel]
            ell_match = selected == expected_ell
            range_ok &= ell_match
            if channel == "gg":
                ordering.extend([f"{sample}:gg:{x}" for x in selected])
            else:
                ordering.extend([f"{sample}:kg:{x}" for x in selected])

            transfer = transfer_data[:, col]
            ch = channel_records[channel]
            bp = namaster_signal_bandpowers(ch["test_cells"], ch["window"], transfer)
            finite_bp = bool(bp.shape == (59,) and np.all(np.isfinite(bp)))
            noise_bp = None
            noise_finite = True
            if channel == "gg" and ch["constant_mode_pass"]:
                noise = float(10.0 ** NUISANCE[sample]["log10SN"])
                noise_bp = namaster_constant_noise_bandpowers(noise, ch["window"], transfer)
                noise_finite = bool(noise_bp.shape == (59,) and np.all(np.isfinite(noise_bp)))
            sample_rec["channels"][channel] = {
                "ranges": ranges,
                "range_match": range_match,
                "selected_ell_midpoints": selected,
                "selected_ell_match": ell_match,
                "selected_count": int(np.sum(cond)),
                "signal_bandpowers_finite": finite_bp,
                "noise_template_finite": noise_finite,
            }
            actual_operator_ok &= bool(transfer_shape_ok and finite_bp and noise_finite)
        selected_records[sample] = sample_rec

    expected_order = (
        [f"Blue_ACT:gg:{x}" for x in EXPECTED_ELL["gg"]]
        + [f"Blue_ACT:kg:{x}" for x in EXPECTED_ELL["kg"]]
        + [f"Green_ACT:gg:{x}" for x in EXPECTED_ELL["gg"]]
        + [f"Green_ACT:kg:{x}" for x in EXPECTED_ELL["kg"]]
    )
    order_ok = ordering == expected_order and len(ordering) == 26

    # Strip the large arrays from JSON records.
    for ch in channel_records.values():
        ch.pop("test_cells", None)
        ch.pop("window", None)

    b2_ok = bool(actual_operator_ok)
    b3_ok = bool(constant_mode_ok)
    b4_ok = bool(range_ok and order_ok)
    return b2_ok, b3_ok, b4_ok, {
        "upstream_source_contract": source_pass,
        "small_matrix_signal_identity_regression": small_rec,
        "shared_act_bandwindow_path": str(shared_path.relative_to(data_root)),
        "same_blue_green_bandwindow_path": same_path,
        "channels": channel_records,
        "samples": selected_records,
        "final_order_length": len(ordering),
        "final_order": ordering,
        "order_pass": order_ok,
    }


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

    b1_ok, b1 = run_b1(repo)
    b2_ok, b3_ok, b4_ok, bridge = run_b2_b3_b4(repo, data_root)

    passed = bool(provenance_ok and b1_ok and b2_ok and b3_ok and b4_ok)
    status = "PASS_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1" if passed else "FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1"
    result = {
        "experiment": "Exp066B",
        "status": status,
        "scope": "forward-operator bridge only; no G7 law search and no withheld-family selection",
        "pinned_external_repo": "ACTCollaboration/unWISExLens_lklh",
        "pinned_commit": commit,
        "archive_sha256": digest,
        "provenance_pass": provenance_ok,
        "frozen_numerics": {
            "rng_seed": SEED,
            "synthetic_ell_count": NELL_SYNTH,
            "equivalence_tolerance": TOL,
            "constant_mode_tolerance": CONSTANT_MODE_TOL,
        },
        "checks": {
            "B1_free_cleft_nuisance_algebra": {"pass": b1_ok, **b1},
            "B2_released_bandwindow_transfer_operator": {"pass": b2_ok, **bridge},
            "B3_shot_noise_constant_mode": {"pass": b3_ok},
            "B4_selected_ordering": {"pass": b4_ok},
        },
        "upstream_fixed_point_endpoint": {
            "value": -62.1652,
            "role": "diagnostic_only",
            "reason": "upstream README does not pin exact Cobaya/CAMB dependency versions",
        },
        "anti_retuning": "No nuisance, seed, tensor-shape, scale-cut, ordering, CLEFT-sector, constant-mode threshold, algebraic reduction, or equivalence-tolerance retuning after execution.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
