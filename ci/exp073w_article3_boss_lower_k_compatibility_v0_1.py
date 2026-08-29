#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

KMIN_LEGACY = 0.000704833374744468
KMAX = 0.06664762008318016
H_FID = 0.676
THRESH = 0.05
NK = 400
Z3_LO = 0.5
Z3_HI = 0.75
Z_DOMAIN_LO = 0.295
Z_DOMAIN_HI = 2.33
BOSS_OFFSET = 1170
EXP073U_FULL_ORDER_SHA256 = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
EXP073U_BOSS_ORDER_SHA256 = "7315944adea1a36c0bdb162d57c567330151018dd2058f80e2cb6cb20c153ea0"
LEGACY_RETAINED_ID_SHA256 = "29f7f0a724f7f4ff6b1b4b8933e43d9b08545a4056fdeb65e1c5fe831deda084"

EXPECTED_SOURCE_SHA = {
    "NGC": {
        "W": "a308dc562d1a7224cefcf91d32580877929e0daa33806517e0d2d53710236827",
        "M": "3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042",
    },
    "SGC": {
        "W": "2a542a2d48f3e8c8299f58a885d5273238e4ade32c0f0de020d8b9f23afe7759",
        "M": "3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042",
    },
}

EVEN_ROWS = (("P0", 0, 40), ("P2", 80, 120), ("P4", 160, 200))

PASS = "PASS_EXP073W_BOSS_LOWER_K_COMPATIBILITY_V0_1"
FAIL = "FAIL_EXP073W_BOSS_LOWER_K_COMPATIBILITY_V0_1"
INVALID = "INVALID_FOR_SCIENCE_EXP073W_BOSS_AUTHORITY"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha_lines(values: list[str]) -> str:
    return hashlib.sha256(("\n".join(values) + "\n").encode("utf-8")).hexdigest()


def canonical_array_hash(a: np.ndarray, dtype: str) -> dict:
    arr = np.ascontiguousarray(np.asarray(a, dtype=np.dtype(dtype)))
    return {
        "dtype": arr.dtype.str,
        "shape": list(arr.shape),
        "sha256": hashlib.sha256(arr.tobytes(order="C")).hexdigest(),
    }


def coordinate_inventory() -> tuple[list[str], list[tuple[str, str, int]]]:
    ids: list[str] = []
    selectors: list[tuple[str, str, int]] = []
    for cap in ("NGC", "SGC"):
        for multipole, lo, hi in EVEN_ROWS:
            for row in range(lo, hi):
                ids.append(f"BOSS|{cap}|{multipole}|matrix_row={row:03d}")
                selectors.append((cap, multipole, row))
    assert len(ids) == 240 and len(set(ids)) == 240
    assert sha_lines(ids) == EXP073U_BOSS_ORDER_SHA256
    return ids, selectors


def fractions(weights: np.ndarray, valid_columns: np.ndarray) -> np.ndarray:
    den = weights.sum(axis=1)
    if not np.isfinite(den).all() or not np.all(den > 0):
        raise AssertionError("non-finite/non-positive absolute BOSS row normalization")
    invalid = weights[:, ~valid_columns].sum(axis=1)
    result = invalid / den
    if not np.isfinite(result).all():
        raise AssertionError("non-finite support fractions")
    return result


def block_counts(mask: np.ndarray, selectors: list[tuple[str, str, int]]) -> dict:
    out: dict[str, dict[str, int]] = {}
    for cap in ("NGC", "SGC"):
        out[cap] = {}
        for multipole, _, _ in EVEN_ROWS:
            idx = [i for i, s in enumerate(selectors) if s[0] == cap and s[1] == multipole]
            out[cap][multipole] = int(mask[idx].sum())
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--output-json", required=True)
    ap.add_argument("--output-npz", required=True)
    args = ap.parse_args()

    root = Path(args.root)
    ids, selectors = coordinate_inventory()

    kh400 = 0.0005 + 0.001 * np.arange(NK, dtype=np.float64)
    kphys400 = H_FID * kh400
    kphys = np.tile(kphys400, 3)
    assert kphys.shape == (1200,)
    assert np.all(np.isfinite(kphys)) and np.all(kphys > 0)

    weights_blocks: list[np.ndarray] = []
    source_sha: dict[str, dict[str, str]] = {}
    matrix_shapes: dict[str, dict[str, list[int]]] = {}

    for cap in ("NGC", "SGC"):
        wp = root / f"W_{cap}_z3"
        mp = root / f"M_{cap}_z3"
        observed_w = sha256_file(wp)
        observed_m = sha256_file(mp)
        if observed_w != EXPECTED_SOURCE_SHA[cap]["W"]:
            raise AssertionError(f"{cap} W source SHA mismatch: {observed_w}")
        if observed_m != EXPECTED_SOURCE_SHA[cap]["M"]:
            raise AssertionError(f"{cap} M source SHA mismatch: {observed_m}")
        source_sha[cap] = {"W_decompressed_sha256": observed_w, "M_decompressed_sha256": observed_m}

        W = np.loadtxt(wp, dtype=np.float64)
        M = np.loadtxt(mp, dtype=np.float64)
        if W.shape != (200, 2000) or M.shape != (2000, 1200):
            raise AssertionError(f"{cap} matrix shape mismatch W={W.shape} M={M.shape}")
        if not np.isfinite(W).all() or not np.isfinite(M).all():
            raise AssertionError(f"{cap} matrix contains non-finite values")
        C = W @ M
        if C.shape != (200, 1200) or not np.isfinite(C).all():
            raise AssertionError(f"{cap} composed C invalid")

        # Deterministic repeatability from independent copies.
        C2 = W.copy() @ M.copy()
        if not np.array_equal(C, C2):
            raise AssertionError(f"{cap} composed operator is not bitwise repeatable")

        selected = []
        for multipole, lo, hi in EVEN_ROWS:
            selected.append(np.abs(C[lo:hi, :]))
        block = np.concatenate(selected, axis=0)
        assert block.shape == (120, 1200)
        weights_blocks.append(block)
        matrix_shapes[cap] = {"W": list(W.shape), "M": list(M.shape), "C": list(C.shape)}

    weights = np.concatenate(weights_blocks, axis=0)
    assert weights.shape == (240, 1200)
    assert np.isfinite(weights).all() and np.all(weights >= 0)
    den = weights.sum(axis=1)
    assert np.isfinite(den).all() and np.all(den > 0)

    valid_legacy = (kphys >= KMIN_LEGACY) & (kphys <= KMAX)
    valid_current = (kphys > 0.0) & (kphys <= KMAX)
    lowk_columns = (kphys > 0.0) & (kphys < KMIN_LEGACY)

    f_legacy = fractions(weights, valid_legacy)
    f_current = fractions(weights, valid_current)
    lowk_fraction = weights[:, lowk_columns].sum(axis=1) / den
    mask_legacy = f_legacy <= THRESH
    mask_current = f_current <= THRESH

    legacy_retained_ids = [cid for cid, keep in zip(ids, mask_legacy) if bool(keep)]
    current_retained_ids = [cid for cid, keep in zip(ids, mask_current) if bool(keep)]
    changed_idx = np.flatnonzero(mask_legacy != mask_current)
    changed_ids = [ids[int(i)] for i in changed_idx]

    legacy_counts = block_counts(mask_legacy, selectors)
    current_counts = block_counts(mask_current, selectors)

    # Historical-authority reproduction is an integrity precondition.
    legacy_ok = (
        int(mask_legacy.sum()) == 54
        and legacy_counts == {
            "NGC": {"P0": 9, "P2": 9, "P4": 9},
            "SGC": {"P0": 9, "P2": 9, "P4": 9},
        }
        and sha_lines(legacy_retained_ids) == LEGACY_RETAINED_ID_SHA256
    )
    if not legacy_ok:
        classification = INVALID
    else:
        classification = PASS if changed_idx.size == 0 else FAIL

    # Find closest row to the threshold under either rule.
    distances = np.minimum(np.abs(f_legacy - THRESH), np.abs(f_current - THRESH))
    nearest_i = int(np.argmin(distances))

    row_ptr = np.arange(0, (weights.shape[0] + 1) * weights.shape[1], weights.shape[1], dtype=np.int64)
    ordinals = np.arange(BOSS_OFFSET, BOSS_OFFSET + 240, dtype=np.int64)

    array_authority = {
        "row_ptr": canonical_array_hash(row_ptr, "<i8"),
        "k_phys_Mpc^-1": canonical_array_hash(kphys, "<f8"),
        "operator_abs_weight": canonical_array_hash(weights, "<f8"),
        "ordinal": canonical_array_hash(ordinals, "<i8"),
        "legacy_retained_mask": canonical_array_hash(mask_legacy.astype(np.uint8), "|u1"),
        "current_retained_mask": canonical_array_hash(mask_current.astype(np.uint8), "|u1"),
        "legacy_f_invalid": canonical_array_hash(f_legacy, "<f8"),
        "current_f_invalid": canonical_array_hash(f_current, "<f8"),
        "lowk_fraction": canonical_array_hash(lowk_fraction, "<f8"),
    }

    result = {
        "experiment": "Exp073W",
        "classification": classification,
        "record_type": "ARTICLE3_BOSS_LOWER_K_COMPATIBILITY_AND_BROADROW_AUTHORITY_V0_1",
        "parent_authority": {
            "exp073u_full_order_sha256": EXP073U_FULL_ORDER_SHA256,
            "exp073u_boss_order_sha256": EXP073U_BOSS_ORDER_SHA256,
            "legacy_exp073j_retained_id_sha256": LEGACY_RETAINED_ID_SHA256,
            "source_semantics": "fbeutler/pk_tools@707eb2a6a4691c34eae19d7f72047ca4892f528e",
            "source_sha256": source_sha,
            "matrix_shapes": matrix_shapes,
        },
        "radial_support": {
            "representation": "interval_subset_certificate_not_effective_z",
            "sample": "BOSS_DR12_z3",
            "z_selection": {"lower_exclusive": Z3_LO, "upper_exclusive": Z3_HI},
            "article3_domain": {"lower_inclusive": Z_DOMAIN_LO, "upper_inclusive": Z_DOMAIN_HI},
            "entire_selection_inside_domain": bool(Z_DOMAIN_LO <= Z3_LO and Z3_HI <= Z_DOMAIN_HI),
            "effective_z_used": False,
        },
        "k_rules": {
            "legacy": {"k_min_inclusive_Mpc^-1": KMIN_LEGACY, "k_max_inclusive_Mpc^-1": KMAX},
            "current": {"k_strictly_positive": True, "k_max_inclusive_Mpc^-1": KMAX, "positive_lower_cutoff": None},
            "h_fid": H_FID,
            "threshold_inclusive": THRESH,
            "effective_k_used": False,
        },
        "candidate_count": 240,
        "ordered_coordinate_ids": ids,
        "ordered_coordinate_id_sha256": sha_lines(ids),
        "legacy": {
            "retained_count": int(mask_legacy.sum()),
            "retained_ids": legacy_retained_ids,
            "retained_id_sha256": sha_lines(legacy_retained_ids),
            "block_counts": legacy_counts,
        },
        "current": {
            "retained_count": int(mask_current.sum()),
            "retained_ids": current_retained_ids,
            "retained_id_sha256": sha_lines(current_retained_ids),
            "block_counts": current_counts,
        },
        "compatibility": {
            "mask_identical": bool(changed_idx.size == 0),
            "changed_row_count": int(changed_idx.size),
            "changed_ids": changed_ids,
            "max_abs_delta_f_invalid": float(np.max(np.abs(f_current - f_legacy))),
            "max_lowk_positive_envelope_fraction": float(np.max(lowk_fraction)),
            "nearest_threshold_row": {
                "coordinate_id": ids[nearest_i],
                "legacy_f_invalid": float(f_legacy[nearest_i]),
                "current_f_invalid": float(f_current[nearest_i]),
                "lowk_fraction": float(lowk_fraction[nearest_i]),
                "distance_to_threshold": float(distances[nearest_i]),
            },
        },
        "array_authority": array_authority,
        "controls": {
            "legacy_authority_reproduced": bool(legacy_ok),
            "source_hashes_verified": True,
            "matrix_dimensions_verified": True,
            "finite_operator_verified": True,
            "positive_row_normalization_verified": True,
            "exp073u_boss_order_verified": True,
            "z3_interval_subset_verified": bool(Z_DOMAIN_LO <= Z3_LO and Z3_HI <= Z_DOMAIN_HI),
            "effective_z_used": False,
            "effective_k_used": False,
            "fiducial_P_weighting_used": False,
            "covariance_read": False,
            "nuisance_geometry_read": False,
            "relation_null_read": False,
            "G8_read": False,
        },
        "science_boundary": {
            "full_1410_manifest_closed": False,
            "global_layer_a_classified": False,
            "layer_b_classified": False,
            "covariance_authorized": False,
            "article3_scientific_readiness_percent": 52,
            "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        },
    }

    out_json = Path(args.output_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")

    out_npz = Path(args.output_npz)
    out_npz.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        out_npz,
        row_ptr=row_ptr,
        k_phys_Mpc_1=kphys,
        operator_abs_weight=weights,
        ordinal=ordinals,
        legacy_retained_mask=mask_legacy.astype(np.uint8),
        current_retained_mask=mask_current.astype(np.uint8),
        legacy_f_invalid=f_legacy,
        current_f_invalid=f_current,
        lowk_fraction=lowk_fraction,
    )

    print(classification)
    print("legacy_retained", int(mask_legacy.sum()), "current_retained", int(mask_current.sum()), "changed", int(changed_idx.size))
    print("max_abs_delta_f_invalid", float(np.max(np.abs(f_current - f_legacy))))

    if classification == INVALID:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
