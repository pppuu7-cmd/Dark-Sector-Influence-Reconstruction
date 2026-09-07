#!/usr/bin/env python3
"""Fail-closed deterministic C2 IDE Delta_m arithmetic/serialization layer.

Support implementation only. It consumes source-bound arrays; it does not run CLASS and
cannot by itself create DSIR-4 scientific authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

SOLVER_REPO = "kaeonikc/class_iv"
SOLVER_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
HYPOTHESIS_ID = "C2_IDE_LOCAL_TANGENT_CONE"
Z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]
K = [0.00067, 0.00201, 0.0067, 0.0201]
POINTS = {
    "reference": [0.0, 0.0],
    "alpha_left": [-0.0001, 0.0],
    "beta_plus": [0.0, 0.0001],
    "beta_minus": [0.0, -0.0001],
}
REQUIRED_NATIVE = ["delta_m", "theta_m", "w_m", "Hconf"]
SHAPE = [7, 4]


class ContractError(RuntimeError):
    pass


def _require(cond: bool, msg: str) -> None:
    if not cond:
        raise ContractError(msg)


def _finite_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(float(x))


def _matrix_7x4(x: Any, name: str) -> list[list[float]]:
    _require(isinstance(x, list) and len(x) == 7, f"{name}: expected 7 rows")
    out: list[list[float]] = []
    for i, row in enumerate(x):
        _require(isinstance(row, list) and len(row) == 4, f"{name}[{i}]: expected 4 columns")
        _require(all(_finite_number(v) for v in row), f"{name}[{i}]: non-finite/non-number")
        out.append([float(v) for v in row])
    return out


def _vector_7(x: Any, name: str) -> list[float]:
    _require(isinstance(x, list) and len(x) == 7, f"{name}: expected length 7")
    _require(all(_finite_number(v) for v in x), f"{name}: non-finite/non-number")
    return [float(v) for v in x]


def _canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def _validate_global_manifest(m: dict[str, Any]) -> None:
    _require(m.get("hypothesis_id") == HYPOTHESIS_ID, "wrong hypothesis_id")
    _require(m.get("solver_repository") == SOLVER_REPO, "wrong solver_repository")
    _require(m.get("solver_commit") == SOLVER_COMMIT, "wrong solver_commit")
    _require(m.get("z") == Z, "z grid mismatch")
    _require(m.get("k_Mpc^-1") == K, "k grid mismatch")
    _require(m.get("matched_primordial_normalization_and_phase") is True,
             "matched primordial normalization/phase not explicitly proven")
    ids = m.get("native_source_identities")
    _require(isinstance(ids, dict), "native_source_identities missing")
    _require(set(ids) == set(REQUIRED_NATIVE), "native source identity key mismatch")
    for key in REQUIRED_NATIVE:
        value = ids[key]
        _require(isinstance(value, str) and value.strip() != "", f"ambiguous native source identity: {key}")
    pts = m.get("points")
    _require(isinstance(pts, dict) and set(pts) == set(POINTS), "point set mismatch")


def _compute_point(name: str, p: dict[str, Any]) -> dict[str, Any]:
    _require(p.get("alpha_beta") == POINTS[name], f"{name}: alpha_beta mismatch")
    branch = p.get("physical_branch")
    _require(isinstance(branch, dict), f"{name}: physical_branch missing")
    _require(branch.get("rho_idm_positive_all_history") is True, f"{name}: rho_idm branch failure")
    _require(branch.get("rho_iv_nonnegative_all_history") is True, f"{name}: rho_iv branch failure")
    delta = _matrix_7x4(p.get("delta_m"), f"{name}.delta_m")
    theta = _matrix_7x4(p.get("theta_m"), f"{name}.theta_m")
    wm = _matrix_7x4(p.get("w_m"), f"{name}.w_m")
    hconf = _vector_7(p.get("Hconf"), f"{name}.Hconf")
    out: list[list[float]] = []
    for iz in range(7):
        row: list[float] = []
        for ik in range(4):
            k = K[ik]
            v = delta[iz][ik] + 3.0 * (1.0 + wm[iz][ik]) * hconf[iz] * theta[iz][ik] / (k * k)
            _require(math.isfinite(v), f"{name}.Delta_m non-finite")
            row.append(v)
        out.append(row)
    return {
        "alpha_beta": POINTS[name],
        "physical_branch": branch,
        "Delta_m": out,
        "Delta_m_shape": SHAPE,
        "Delta_m_finite": True,
    }


def generate(manifest: dict[str, Any]) -> dict[str, Any]:
    _validate_global_manifest(manifest)
    computed = {name: _compute_point(name, manifest["points"][name]) for name in POINTS}
    ref = computed["reference"]["Delta_m"]
    for name in ("alpha_left", "beta_plus", "beta_minus"):
        response: list[list[float]] = []
        model = computed[name]["Delta_m"]
        for iz in range(7):
            row: list[float] = []
            for ik in range(4):
                denom = ref[iz][ik] * ref[iz][ik]
                numer = model[iz][ik] * model[iz][ik]
                _require(denom > 0.0 and numer > 0.0, f"{name}.r_Delta requires positive matched powers")
                v = math.log(numer / denom)
                _require(math.isfinite(v), f"{name}.r_Delta non-finite")
                row.append(v)
            response.append(row)
        computed[name]["r_Delta"] = response
        computed[name]["r_Delta_shape"] = SHAPE
        computed[name]["r_Delta_finite"] = True

    payload: dict[str, Any] = {
        "hypothesis_id": HYPOTHESIS_ID,
        "solver_repository": SOLVER_REPO,
        "solver_commit": SOLVER_COMMIT,
        "generator_repository_commit": manifest.get("generator_repository_commit"),
        "generator_script_blob_sha": manifest.get("generator_script_blob_sha"),
        "document_blob_identities": manifest.get("document_blob_identities"),
        "baseline_cosmology_identity": manifest.get("baseline_cosmology_identity"),
        "precision_identity": manifest.get("precision_identity"),
        "native_source_identities": manifest["native_source_identities"],
        "matched_primordial_normalization_and_phase": True,
        "z": Z,
        "k_Mpc^-1": K,
        "points": computed,
        "prediction_ready": True,
    }
    for key in ("generator_repository_commit", "generator_script_blob_sha", "document_blob_identities",
                "baseline_cosmology_identity", "precision_identity"):
        value = payload[key]
        _require(value not in (None, "", {}, []), f"missing provenance identity: {key}")
    digest = hashlib.sha256(_canonical_bytes(payload)).hexdigest()
    payload["payload_sha256"] = digest
    verify = dict(payload)
    verify.pop("payload_sha256")
    _require(hashlib.sha256(_canonical_bytes(verify)).hexdigest() == digest, "payload SHA self-check failed")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    manifest = json.loads(Path(args.input).read_text(encoding="utf-8"))
    payload = generate(manifest)
    Path(args.output).write_bytes(_canonical_bytes(payload) + b"\n")
    print(payload["payload_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
