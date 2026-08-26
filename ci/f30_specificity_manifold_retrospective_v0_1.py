#!/usr/bin/env python3
"""Exp071A: retrospective specificity/manifold audit after the already-unblinded F30 C9 PASS.

This is deliberately DESCRIPTIVE/RETROSPECTIVE.  C9 has already been seen.  The script
must not be used as a preregistered test, must not change F30, and cannot close G7/G8/G9.
It asks two post-unblinding questions:
  (1) how selective is the F30 no-self-intersection topology under all 5! orderings?
  (2) does withheld C9 actually lie near the pooled C3+C5+C7+C8 linear PCA subspace?
It also reports within-family centered-SVD spectra as a descriptive dimensionality audit.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], float)
Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], float)

RUN_PROVENANCE = {
    "C3_GDM": 32904158849,
    "C5_fR": 32907619613,
    "C7_IDM_DR": 32920776596,
    "C8_IDM_photon": 32926084015,
    "C9_IDM_baryon_F30": 32957427686,
}
ARTIFACT_DIGESTS = {
    "C3_GDM": "sha256:892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a",
    "C5_fR": "sha256:bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942",
    "C7_IDM_DR": "sha256:fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a",
    "C8_IDM_photon": "sha256:eb44e29725ace326e707d396158e7c4ed6fd4dccdd86d9ad18e67f42526750b1",
    "C9_IDM_baryon_F30": "sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed",
}


def j(x: Any) -> Any:
    if isinstance(x, dict): return {str(k): j(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [j(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, np.generic): return x.item()
    if isinstance(x, (str, int, float, bool)) or x is None: return x
    return str(x)


def readj(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def unique(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise ValueError(f"expected exactly one {name} under {root}; got {hits}")
    return hits[0]


def validate_matrix(r: Any) -> np.ndarray:
    a = np.asarray(r, float)
    if a.shape != (7, 5) or not np.all(np.isfinite(a)) or np.linalg.norm(a) == 0:
        raise ValueError(f"bad response matrix {a.shape}")
    return a


def load_gdm(root: Path) -> list[np.ndarray]:
    d = readj(unique(root, "exp049b_gdm_cv2_intermediate_scan.json"))
    if not np.allclose(np.asarray(d["core_k_h_mpc"], float), K, rtol=0, atol=1e-14):
        raise ValueError("C3 k mismatch")
    if not np.allclose(np.asarray(d["z_nodes"], float), Z, rtol=0, atol=1e-10):
        raise ValueError("C3 z mismatch")
    out = []
    for m in sorted(d["models"], key=lambda x: float(x["cv2"])):
        files = sorted(m["files"], key=lambda x: float(x["z"]))
        out.append(validate_matrix([x["r_core"] for x in files]))
    return out


def load_fr(root: Path) -> list[np.ndarray]:
    payload: dict[float, dict[str, Any]] = {}
    for p in root.rglob("exp049c_B0_*.json"):
        d = readj(p)
        b = float(d["B0"])
        if b > 0:
            payload[b] = d
    if len(payload) != 5:
        raise ValueError(f"expected 5 positive-B0 C5 points; got {sorted(payload)}")
    out = []
    for b in sorted(payload):
        d = payload[b]
        if not np.allclose(np.asarray(d["k_h_mpc"], float), K, rtol=0, atol=1e-14):
            raise ValueError("C5 k mismatch")
        if not np.allclose(np.asarray(d["z_nodes"], float), Z, rtol=0, atol=1e-10):
            raise ValueError("C5 z mismatch")
        out.append(validate_matrix(d["r_Delta"]))
    return out


def load_models_json(root: Path, name: str) -> list[np.ndarray]:
    d = readj(unique(root, name))
    if len(d["models"]) != 5:
        raise ValueError(f"expected five models in {name}")
    return [validate_matrix(m["response_matrix_z_by_k"]) for m in d["models"]]


def unitvec(r: np.ndarray) -> np.ndarray:
    v = validate_matrix(r).reshape(-1)
    return v / np.linalg.norm(v)


def centered_svd(models: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    X = np.stack([unitvec(r) for r in models])
    C = X - np.mean(X, axis=0)
    s = np.linalg.svd(C, full_matrices=False, compute_uv=False)
    var = s * s
    frac = var / np.sum(var)
    return s, frac


def orient(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> float:
    return float((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]))


def on_segment(a: np.ndarray, b: np.ndarray, p: np.ndarray, tol: float = 1e-10) -> bool:
    return bool(min(a[0], b[0])-tol <= p[0] <= max(a[0], b[0])+tol and
                min(a[1], b[1])-tol <= p[1] <= max(a[1], b[1])+tol)


def segments_intersect(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray,
                       tol: float = 1e-10) -> bool:
    oo = [orient(a,b,c), orient(a,b,d), orient(c,d,a), orient(c,d,b)]
    def sgn(x: float) -> int: return 1 if x > tol else (-1 if x < -tol else 0)
    s1, s2, s3, s4 = map(sgn, oo)
    if s1*s2 < 0 and s3*s4 < 0:
        return True
    return bool((s1 == 0 and on_segment(a,b,c,tol)) or
                (s2 == 0 and on_segment(a,b,d,tol)) or
                (s3 == 0 and on_segment(c,d,a,tol)) or
                (s4 == 0 and on_segment(c,d,b,tol)))


def simple_path(xy: np.ndarray) -> bool:
    xy = np.asarray(xy, float)
    if xy.shape != (5,2):
        raise ValueError(f"expected five 2D points, got {xy.shape}")
    if np.any(np.linalg.norm(np.diff(xy, axis=0), axis=1) <= 1e-10):
        return False
    for i in range(4):
        for k in range(i+2, 4):
            if segments_intersect(xy[i], xy[i+1], xy[k], xy[k+1], 1e-10):
                return False
    return True


def path_length(xy: np.ndarray) -> float:
    return float(np.sum(np.linalg.norm(np.diff(np.asarray(xy, float), axis=0), axis=1)))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--gdm-root", required=True)
    p.add_argument("--fr-root", required=True)
    p.add_argument("--c7-root", required=True)
    p.add_argument("--c8-root", required=True)
    p.add_argument("--c9-root", required=True)
    p.add_argument("--json", required=True)
    a = p.parse_args()

    roots = {k: Path(v) for k, v in {
        "gdm": a.gdm_root, "fr": a.fr_root, "c7": a.c7_root,
        "c8": a.c8_root, "c9": a.c9_root}.items()}

    c9_json = readj(unique(roots["c9"], "idm_baryon_multicoordinate_prospective_v0_1.json"))
    if c9_json.get("status") != "PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1":
        raise ValueError("Exp061A/F30 immutable source is not the recorded prospective PASS")

    fam = {
        "C3_GDM": load_gdm(roots["gdm"]),
        "C5_fR": load_fr(roots["fr"]),
        "C7_IDM_DR": load_models_json(roots["c7"], "idm_dr_common_source_response_slope_v0_1.json"),
        "C8_IDM_photon": load_models_json(roots["c8"], "idm_photon_endpoint_half_transition_prospective_v0_1.json"),
        "C9_IDM_baryon": [validate_matrix(m["response_matrix_z_by_k"]) for m in c9_json["models"]],
    }
    if any(len(v) != 5 for v in fam.values()):
        raise ValueError({k: len(v) for k, v in fam.items()})

    xy = np.asarray(c9_json["full"]["standardized_xy"], float)
    loo_xy = [np.asarray(e["standardized_xy"], float) for e in c9_json["leave_one_z"]]
    permutations = list(itertools.permutations(range(5)))
    simple = [q for q in permutations if simple_path(xy[list(q)])]
    robust = [q for q in simple if all(simple_path(x[list(q)]) for x in loo_xy)]
    physical = tuple(range(5))
    if physical not in robust:
        raise ValueError("recorded physical F30 ordering unexpectedly fails retrospective reconstruction")
    simple_lengths = np.asarray([path_length(xy[list(q)]) for q in simple], float)
    physical_length = path_length(xy)

    training = [r for key in ("C3_GDM","C5_fR","C7_IDM_DR","C8_IDM_photon") for r in fam[key]]
    X = np.stack([unitvec(r) for r in training])
    mean = np.mean(X, axis=0)
    C = X - mean
    _, s_pool, vt = np.linalg.svd(C, full_matrices=False)
    pool_frac = s_pool*s_pool / np.sum(s_pool*s_pool)
    C9 = np.stack([unitvec(r) for r in fam["C9_IDM_baryon"]]) - mean
    denom = np.linalg.norm(C9, axis=1)
    transfer: dict[str, Any] = {}
    for dim in (1,2,3,4):
        proj = (C9 @ vt[:dim].T) @ vt[:dim]
        residual = np.linalg.norm(C9-proj, axis=1) / denom
        transfer[str(dim)] = {
            "c9_fraction_of_centered_distance_outside_training_subspace": residual.tolist(),
            "max": float(np.max(residual)),
            "mean": float(np.mean(residual)),
        }

    family_svd = {}
    for key, models in fam.items():
        sf, vf = centered_svd(models)
        family_svd[key] = {
            "singular_values": sf.tolist(),
            "variance_fraction": vf.tolist(),
            "cumulative_variance_fraction": np.cumsum(vf).tolist(),
        }

    out = {
        "schema": "dsir.f30_specificity_manifold_retrospective.v0.1",
        "experiment": "Exp071A",
        "date": "2026-08-27",
        "status": "DESCRIPTIVE_RETROSPECTIVE_F30_SPECIFICITY_MANIFOLD_AUDIT_V0_1",
        "epistemic_status": "POST_UNBLINDING_RETROSPECTIVE_ONLY",
        "immutable_run_provenance": RUN_PROVENANCE,
        "immutable_artifact_digests": ARTIFACT_DIGESTS,
        "f30_preserved_status": "PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1",
        "topology_specificity": {
            "total_permutations": len(permutations),
            "simple_path_permutations_full": len(simple),
            "simple_path_fraction_full": len(simple)/len(permutations),
            "simple_path_permutations_robust_all_leave_one_z": len(robust),
            "robust_fraction": len(robust)/len(permutations),
            "physical_order": list(physical),
            "physical_path_length": physical_length,
            "simple_path_length_median": float(np.median(simple_lengths)),
            "number_simple_paths_with_length_le_physical": int(np.sum(simple_lengths <= physical_length)),
            "interpretation": "F30 remains a genuine prospective PASS, but no-self-intersection alone is only moderately selective for these five fixed C9 points: one third of all orderings also pass and remain leave-one-z robust.",
        },
        "pooled_training_centered_svd": {
            "training_families": ["C3_GDM","C5_fR","C7_IDM_DR","C8_IDM_photon"],
            "training_vectors": 20,
            "features": 35,
            "singular_values": s_pool.tolist(),
            "variance_fraction": pool_frac.tolist(),
            "cumulative_variance_fraction": np.cumsum(pool_frac).tolist(),
            "withheld_c9_subspace_transfer": transfer,
            "interpretation": "High in-sample PCA compression of pooled training responses does not imply a common transferred linear manifold: some withheld C9 states remain far outside the first two to four training PCs.",
        },
        "within_family_centered_svd": family_svd,
        "descriptive_synthesis": [
            "single universal scalar laws were already falsified prospectively by F27/F29",
            "a single fixed pooled linear 2D response plane is not supported as a transferred description of all C9 states",
            "each tested one-parameter family is nevertheless strongly locally low-dimensional on the frozen 7x5 response window",
            "C3/C5/C7 are nearly one-shape-direction families, while C8/C9 require a materially stronger second family-local shape direction",
            "the surviving candidate object is therefore a branched/nonlinear atlas of family-local response trajectories, not one universal scalar or one fixed global PCA plane"
        ],
        "not_a_claim": [
            "not a preregistered discovery",
            "not evidence that the dark sector is fundamentally two-dimensional",
            "not proof that the response geometry is specific to dark physics rather than generic smooth parameter variation",
            "not an observational detection and not a closure of G7, G8, or G9"
        ],
        "required_next_specificity_test": "prospectively freeze known-sector control families before computing their responses; if the same path/low-dimensional geometry appears for ordinary parameters, it is not dark-sector-specific",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    Path(a.json).write_text(json.dumps(j(out), indent=2) + "\n")
    print(json.dumps(j(out), indent=2))


if __name__ == "__main__":
    main()
