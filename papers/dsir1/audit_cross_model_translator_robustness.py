#!/usr/bin/env python3
"""Reproduce the DSIR-I cross-model translator robustness audit.

This script intentionally uses only repository-frozen summary products and
reports discrete nearest-neighbour identities / cycle counts.  It does not
claim new distance precision because k_geo and z_centroid are rounded in the
summary JSON.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
P047A = ROOT / "data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json"
P048B = ROOT / "data/derived/comparison_readiness/experiment_048b_finite_amplitude_localization_flow_v0_1_summary.json"
OUT = ROOT / "papers/dsir1/evidence/cross_model_translator_robustness_reproduction_v0_1.json"

C3_PARAMS = [1e-8, 1e-7, 1e-6, 1e-5, 1e-4]
C5_PARAMS = [1e-6, 1e-5, 1e-4, 1e-3]
SCALINGS = ("pooled_zscore", "pooled_minmax", "pooled_median_MAD")
NORMS = ("L1", "L2", "Linf")


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def coordinate_arrays(d47: dict, d48: dict) -> tuple[np.ndarray, np.ndarray]:
    s3 = d48["series_summary"]["GDM_cv2"]
    s5 = d48["series_summary"]["designer_fR"]
    chi3 = [row[1] for row in d47["selected_chi_I_sequences"]["GDM_cv2"]]
    chi5 = [row[1] for row in d47["selected_chi_I_sequences"]["designer_fR"]]

    q3 = np.column_stack(
        [np.log(np.asarray(s3["k_geo"], float)), np.asarray(s3["z_centroid"], float), np.log(np.asarray(chi3, float))]
    )
    q5 = np.column_stack(
        [np.log(np.asarray(s5["k_geo"], float)), np.asarray(s5["z_centroid"], float), np.log(np.asarray(chi5, float))]
    )
    return q3, q5


def scale_pair(a: np.ndarray, b: np.ndarray, mode: str) -> tuple[np.ndarray, np.ndarray]:
    x = np.vstack([a, b])
    if mode == "pooled_zscore":
        loc = x.mean(axis=0)
        scl = x.std(axis=0, ddof=0)
    elif mode == "pooled_minmax":
        loc = x.min(axis=0)
        scl = x.max(axis=0) - x.min(axis=0)
    elif mode == "pooled_median_MAD":
        loc = np.median(x, axis=0)
        scl = np.median(np.abs(x - loc), axis=0)
    else:
        raise ValueError(mode)
    if np.any(scl <= 0) or np.any(~np.isfinite(scl)):
        raise RuntimeError(f"invalid scale in {mode}: {scl}")
    return (a - loc) / scl, (b - loc) / scl


def distance(a: np.ndarray, b: np.ndarray, norm: str) -> float:
    d = np.abs(a - b)
    if norm == "L1":
        return float(d.sum())
    if norm == "L2":
        return float(math.sqrt(float(np.dot(d, d))))
    if norm == "Linf":
        return float(d.max())
    raise ValueError(norm)


def translate(a: np.ndarray, b: np.ndarray, norm: str) -> list[int]:
    return [int(np.argmin([distance(x, y, norm) for y in b])) for x in a]


def audit_variant(q3: np.ndarray, q5: np.ndarray, dims: tuple[int, ...], scaling: str, norm: str) -> dict:
    a, b = scale_pair(q3[:, dims], q5[:, dims], scaling)
    m35 = translate(a, b, norm)
    m53 = translate(b, a, norm)
    closed = [bool(m53[j] == i) for i, j in enumerate(m35)]
    return {
        "scaling": scaling,
        "norm": norm,
        "C3_to_C5_indices": m35,
        "C3_to_C5_B0": [C5_PARAMS[j] for j in m35],
        "C5_to_C3_indices": m53,
        "cycle_closed_C3": closed,
        "cycle_closure_count_C3_of_5": int(sum(closed)),
    }


def family(q3: np.ndarray, q5: np.ndarray, dims: tuple[int, ...]) -> list[dict]:
    return [audit_variant(q3, q5, dims, s, n) for s in SCALINGS for n in NORMS]


def main() -> None:
    d47, d48 = load(P047A), load(P048B)
    q3, q5 = coordinate_arrays(d47, d48)

    full = family(q3, q5, (0, 1, 2))
    kz = family(q3, q5, (0, 1))
    zchi = family(q3, q5, (1, 2))
    kchi = family(q3, q5, (0, 2))

    # Frozen audit invariants.
    assert {r["cycle_closure_count_C3_of_5"] for r in full} == {2}
    assert sum(r["C3_to_C5_B0"] == [1e-6, 1e-6, 1e-6, 1e-6, 1e-3] for r in full) == 8
    assert all(r["C3_to_C5_B0"][-1] == 1e-3 for r in full)
    assert {r["cycle_closure_count_C3_of_5"] for r in kz} == {2}
    assert all(r["C3_to_C5_B0"] == [1e-6, 1e-6, 1e-6, 1e-6, 1e-3] for r in kz)
    assert {r["cycle_closure_count_C3_of_5"] for r in zchi} == {1}
    assert all(r["C3_to_C5_B0"] == [1e-3] * 5 for r in zchi)
    assert sorted(r["cycle_closure_count_C3_of_5"] for r in kchi).count(3) == 2
    assert sorted(r["cycle_closure_count_C3_of_5"] for r in kchi).count(2) == 7

    single = {}
    for name, dim in (("ln_k_geo", 0), ("z_centroid", 1), ("ln_chi_I", 2)):
        r = audit_variant(q3, q5, (dim,), "pooled_zscore", "L2")
        single[name] = {
            "C3_to_C5_B0": r["C3_to_C5_B0"],
            "cycle_closure_count_C3_of_5": r["cycle_closure_count_C3_of_5"],
        }

    assert single["ln_k_geo"]["C3_to_C5_B0"] == [1e-6, 1e-6, 1e-5, 1e-5, 1e-3]
    assert single["ln_k_geo"]["cycle_closure_count_C3_of_5"] == 3
    assert single["z_centroid"]["C3_to_C5_B0"] == [1e-3] * 5
    assert single["z_centroid"]["cycle_closure_count_C3_of_5"] == 1
    assert single["ln_chi_I"]["C3_to_C5_B0"] == [1e-3] * 5
    assert single["ln_chi_I"]["cycle_closure_count_C3_of_5"] == 1

    result = {
        "schema": "dsir.paper1.cross_model_translator_robustness.reproduction.v0.1",
        "status": "PASS_RETROSPECTIVE_TRANSLATOR_METRIC_AND_COORDINATE_ROBUSTNESS_V0_1",
        "coordinate": ["ln_k_geo", "z_centroid", "ln_chi_I"],
        "full": full,
        "ablations": {
            "ln_k_geo_plus_z_centroid": kz,
            "z_centroid_plus_ln_chi_I": zchi,
            "ln_k_geo_plus_ln_chi_I": kchi,
        },
        "single_coordinate_pooled_zscore_L2": single,
        "precision_boundary": "discrete nearest-neighbour identities and cycle counts only; rounded summary inputs do not authorize new distance precision",
        "non_claims": ["not prospective validation", "not observational precision", "not G7/G8/G9"],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"])
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
