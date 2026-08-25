#!/usr/bin/env python3
import argparse
import json
import math
from pathlib import Path

import numpy as np


PAIR_IDS = [
    ("C3_GDM_cs2", "C3_GDM_cv2"),
    ("C3_GDM_cs2", "C5_designer_fR_B0"),
    ("C3_GDM_cv2", "C5_designer_fR_B0"),
    ("C2_IDE_alpha_negative", "C5_designer_fR_B0"),
    ("C2_IDE_alpha_negative", "C2_IDE_beta"),
]

MORPH_FLOOR = 1e-6
CONTROL_TOL = 1e-12


def ld_norm(x):
    a = np.asarray(x, dtype=np.longdouble).ravel()
    return np.sqrt(np.sum(a * a, dtype=np.longdouble), dtype=np.longdouble)


def decompose(R):
    x = np.asarray(R, dtype=np.longdouble)
    mu = np.mean(x, dtype=np.longdouble)
    T = np.mean(x, axis=0, dtype=np.longdouble) - mu
    tau = np.mean(x, axis=1, dtype=np.longdouble) - mu
    C = np.full_like(x, mu) + np.tile(T, (x.shape[0], 1)) + np.tile(tau[:, None], (1, x.shape[1]))
    I = x - C

    nr = ld_norm(x)
    nc = ld_norm(C)
    ni = ld_norm(I)
    if nr == 0:
        raise ValueError("zero response norm")

    recon = ld_norm(x - C - I) / nr
    orth = np.longdouble(0.0)
    if nc > 0 and ni > 0:
        orth = abs(np.sum(C * I, dtype=np.longdouble)) / (nc * ni)

    chi = (ni * ni) / (nr * nr)
    u = x / nr
    c = C / nr
    ii = I / nr
    return {
        "chi": chi,
        "u": u.ravel(),
        "c": c.ravel(),
        "i": ii.ravel(),
        "recon": recon,
        "orth": orth,
    }


def pair_eta(A, B):
    dot = np.sum(A["u"] * B["u"], dtype=np.longdouble)
    s = np.longdouble(1.0 if dot >= 0 else -1.0)
    d = A["u"] - s * B["u"]
    dc = A["c"] - s * B["c"]
    di = A["i"] - s * B["i"]
    nd2 = np.sum(d * d, dtype=np.longdouble)
    if nd2 <= 0:
        raise ValueError("zero pair distance")
    nc2 = np.sum(dc * dc, dtype=np.longdouble)
    ni2 = np.sum(di * di, dtype=np.longdouble)
    eta = ni2 / nd2
    pyth = abs(nd2 - nc2 - ni2) / nd2
    cos_abs = min(np.longdouble(1.0), abs(dot))
    angle = math.degrees(math.acos(float(cos_abs)))
    return {
        "eta_I": eta,
        "eta_core": nc2 / nd2,
        "pythagorean_residual": pyth,
        "pair_distance": np.sqrt(nd2, dtype=np.longdouble),
        "acute_deg": angle,
        "orientation_sign": int(s),
    }


def jsonable(obj):
    if isinstance(obj, dict):
        return {k: jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [jsonable(v) for v in obj]
    if isinstance(obj, tuple):
        return [jsonable(v) for v in obj]
    if isinstance(obj, np.generic):
        return obj.item()
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    src = json.loads(Path(args.input).read_text())
    z_nodes = list(src["z_nodes"])
    k_nodes = list(src["k_h_mpc"])
    nz, nk = len(z_nodes), len(k_nodes)
    raw = {d["id"]: np.asarray(d["vector"], dtype=np.longdouble).reshape(nz, nk) for d in src["directions"]}

    variants = [("full", None, None)]
    variants += [(f"drop_k_{i}", "k", i) for i in range(nk)]
    variants += [(f"drop_z_{i}", "z", i) for i in range(nz)]

    variant_rows = []
    max_recon = np.longdouble(0.0)
    max_orth = np.longdouble(0.0)
    max_pyth = np.longdouble(0.0)

    for name, axis, idx in variants:
        if axis == "k":
            matrices = {key: np.delete(val, idx, axis=1) for key, val in raw.items()}
            removed = {"axis": "k", "index": idx, "value": k_nodes[idx]}
        elif axis == "z":
            matrices = {key: np.delete(val, idx, axis=0) for key, val in raw.items()}
            removed = {"axis": "z", "index": idx, "value": z_nodes[idx]}
        else:
            matrices = raw
            removed = None

        D = {key: decompose(val) for key, val in matrices.items()}
        for d in D.values():
            max_recon = max(max_recon, d["recon"])
            max_orth = max(max_orth, d["orth"])

        pairs = {}
        for a, b in PAIR_IDS:
            p = pair_eta(D[a], D[b])
            max_pyth = max(max_pyth, p["pythagorean_residual"])
            pairs[f"{a}__{b}"] = p

        chi = {key: D[key]["chi"] for key in D}
        tier = bool(
            max(chi["C2_IDE_alpha_negative"], chi["C2_IDE_beta"]) < chi["C1_smooth_w_nonphantom"]
            and chi["C1_smooth_w_nonphantom"] < min(chi["C3_GDM_cs2"], chi["C3_GDM_cv2"])
            and max(chi["C3_GDM_cs2"], chi["C3_GDM_cv2"]) < chi["C5_designer_fR_B0"]
        )
        ide_near_null = bool(
            chi["C2_IDE_alpha_negative"] < MORPH_FLOOR and chi["C2_IDE_beta"] < MORPH_FLOOR
        )

        variant_rows.append({
            "variant": name,
            "removed": removed,
            "chi_I": chi,
            "pairwise": pairs,
            "tier_order_preserved": tier,
            "ide_both_below_morphology_floor": ide_near_null,
        })

    controls_pass = bool(max_recon <= CONTROL_TOL and max_orth <= CONTROL_TOL and max_pyth <= CONTROL_TOL)

    full = variant_rows[0]
    reduced = variant_rows[1:]
    direction_summary = {}
    for key, full_chi in full["chi_I"].items():
        vals = np.asarray([r["chi_I"][key] for r in reduced], dtype=np.longdouble)
        abs_drift = np.max(np.abs(vals - full_chi))
        row = {
            "full_chi_I": full_chi,
            "min_leave_one_out_chi_I": np.min(vals),
            "max_leave_one_out_chi_I": np.max(vals),
            "max_abs_drift": abs_drift,
            "all_leave_one_out_below_morphology_floor": bool(np.all(vals < MORPH_FLOOR)),
        }
        if full_chi >= MORPH_FLOOR:
            ratios = vals / full_chi
            row.update({
                "min_ratio_to_full": np.min(ratios),
                "max_ratio_to_full": np.max(ratios),
                "max_abs_log10_ratio": np.max(np.abs(np.log10(ratios))),
            })
        direction_summary[key] = row

    pair_summary = {}
    for a, b in PAIR_IDS:
        key = f"{a}__{b}"
        full_eta = full["pairwise"][key]["eta_I"]
        vals = np.asarray([r["pairwise"][key]["eta_I"] for r in reduced], dtype=np.longdouble)
        pair_summary[key] = {
            "full_eta_I": full_eta,
            "min_leave_one_out_eta_I": np.min(vals),
            "max_leave_one_out_eta_I": np.max(vals),
            "max_abs_drift": np.max(np.abs(vals - full_eta)),
        }

    out = {
        "schema": "dsir.scale_time_interaction.leave_one_node_stability.v0.1",
        "status": "PASS_INTERACTION_LEAVE_ONE_NODE_OPERATOR_CONTROLS_V0_1" if controls_pass else "FAIL_INTERACTION_LEAVE_ONE_NODE_OPERATOR_CONTROLS_V0_1",
        "scope": "common frozen low-k C1/C2/C3/C5 theory response; deterministic 5 leave-one-k plus 7 leave-one-z grids; C4 excluded by domain contract",
        "input": args.input,
        "frozen": {
            "operator_control_tol": CONTROL_TOL,
            "existing_interaction_morphology_floor_chi_I": MORPH_FLOOR,
            "scientific_stability_threshold": None,
            "number_leave_one_k": nk,
            "number_leave_one_z": nz,
        },
        "controls": {
            "max_relative_reconstruction_error": max_recon,
            "max_normalized_core_interaction_orthogonality": max_orth,
            "max_pairwise_pythagorean_residual": max_pyth,
            "pass": controls_pass,
        },
        "descriptive_robustness": {
            "tier_order_preserved_in_all_reduced_grids": bool(all(r["tier_order_preserved"] for r in reduced)),
            "ide_both_near_null_in_all_reduced_grids": bool(all(r["ide_both_below_morphology_floor"] for r in reduced)),
            "number_tier_order_failures": int(sum(not r["tier_order_preserved"] for r in reduced)),
            "number_ide_floor_crossings": int(sum(not r["ide_both_below_morphology_floor"] for r in reduced)),
        },
        "direction_summary": direction_summary,
        "pair_summary": pair_summary,
        "variants": variant_rows,
        "not_a_claim": [
            "leave-one-node robustness is not independent-data confirmation",
            "no post-hoc scientific stability threshold is applied",
            "eta_I is separation-power localization, not significance or detectability",
            "not observational whitening, intrinsic rank, universal mechanism law, or discovery",
        ],
    }

    rendered = json.dumps(jsonable(out), indent=2) + "\n"
    Path(args.json).write_text(rendered)
    print(rendered)
    raise SystemExit(0 if controls_pass else 2)


if __name__ == "__main__":
    main()
