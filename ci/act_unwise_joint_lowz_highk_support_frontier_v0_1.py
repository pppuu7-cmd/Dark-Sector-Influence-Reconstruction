#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import healpy as hp
import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
PARENT_IMPL = ROOT / "ci" / "act_unwise_angular_support_leakage_mask_v0_1.py"
spec = importlib.util.spec_from_file_location("exp072a_parent_impl", PARENT_IMPL)
parent_impl = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(parent_impl)
base = parent_impl.base

UPSTREAM_PIN = parent_impl.UPSTREAM_PIN
CAMB_PIN = parent_impl.CAMB_PIN
ARCHIVE_SHA256 = parent_impl.ARCHIVE_SHA256

EXP072A_RUN = 33029362485
EXP072A_ARTIFACT = 9629763833
EXP072A_DIGEST = "sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d"
EXP072A_JSON_SHA256 = "56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3"
EXP072A_HEAD = "553f6867f1cf71d4661a9f7b1f739a970648d05d"
EXP072A_STATUS = "FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1"

EXP072B_RUN = 33030657898
EXP072B_JOB = 98382166843
EXP072B_ARTIFACT = 9630210086
EXP072B_DIGEST = "sha256:5bbca5717d29d24f8ba3b5ae24d8cc752bd5d90460859ae79f5212ca764615ad"
EXP072B_JSON_SHA256 = "d90b387b6acb5b48c6daae0f25da9adb7ea6ed851e3b22c8a79c6bc56b2d0f1d"
EXP072B_HEAD = "3dce5449e9d23dbc71091905ad51bd8c7b45bba2"
EXP072B_STATUS = "DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B"

THRESHOLD = 0.05
Z0 = 0.295
ZMAX = 2.33
KMIN = 0.000704833374744468
K0 = 0.06664762008318016
NINT = 96
ELL = np.arange(6144, dtype=np.int64)
NSIDE = 2048
EPS128 = 128.0 * np.finfo(np.float64).eps
REPRO_TOL = 5e-13
SAMPLES = ("Blue_ACT", "Green_ACT")
CHANNEL_BLOCKS = {"gg": ("mm", "Wm", "WW"), "kg": ("Wm", "WW")}

FOUND = "DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C"
NOT_FOUND = "DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_NOT_FOUND_EXP072C"
FAIL = "FAIL_EXP072C_REPRODUCTION_OR_PROVENANCE"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def bind_artifact(json_path: Path, meta_path: Path, *, run: int, artifact: int, digest: str, head: str, json_sha: str, status: str) -> tuple[dict, dict]:
    d = json.loads(json_path.read_text())
    m = json.loads(meta_path.read_text())
    wr = m.get("workflow_run") or {}
    checks = {
        "artifact_id": m.get("id") == artifact,
        "artifact_digest": m.get("digest") == digest,
        "workflow_run": wr.get("id") == run,
        "workflow_head": wr.get("head_sha") == head,
        "json_sha256": sha256(json_path) == json_sha,
        "classification": d.get("status") == status,
        "gate_state": d.get("gate_state") == {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    return d, {"run": run, "artifact": artifact, "digest": digest, "json_sha256": json_sha, "checks": checks, "pass": bool(all(checks.values()))}


def pair_req_for_z(weight: np.ndarray, z: np.ndarray, k_grid: np.ndarray, Z: float, sort_idx: np.ndarray, uniq_k: np.ndarray, uniq_end: np.ndarray) -> dict:
    den = float(np.sum(weight))
    if not np.isfinite(den) or den <= 0.0:
        raise ValueError("pair denominator is not finite positive")

    zout = (z[:, None] < Z) | (z[:, None] > ZMAX)
    lowk = k_grid < KMIN
    irreducible = zout | lowk
    irred_w = float(np.sum(weight[irreducible]))
    eligible = (~zout) & (~lowk)
    eligible_w = np.where(eligible, weight, 0.0)
    eligible_total = float(np.sum(eligible_w))
    closure = abs((irred_w + eligible_total) / den - 1.0)

    current_valid = (z[:, None] >= Z) & (z[:, None] <= ZMAX) & (k_grid >= KMIN) & (k_grid <= K0)
    current_leak = float(1.0 - np.sum(weight[current_valid]) / den)

    irred_frac = irred_w / den
    kreq = None
    k_monotonic = True
    if irred_frac <= THRESHOLD:
        sw = eligible_w.ravel()[sort_idx]
        cum = np.cumsum(sw)[uniq_end]
        bad_frac = (irred_w + eligible_total - cum) / den
        k_monotonic = bool(np.all(np.diff(bad_frac) <= EPS128))
        good = (uniq_k >= K0) & (bad_frac <= THRESHOLD)
        if np.any(good):
            kreq = float(uniq_k[np.flatnonzero(good)[0]])

    return {
        "Z": float(Z),
        "irreducible_fraction": irred_frac,
        "current_K0_leakage": current_leak,
        "bookkeeping_closure_abs": closure,
        "K_req_pair_Mpc^-1": kreq,
        "K_req_pair_is_infinite": kreq is None,
        "k_monotonic": k_monotonic,
    }


def route_at_z(coord_rows: list[dict]) -> tuple[float | None, dict | None]:
    finite = sorted({float(c["K_req_coord_Mpc^-1"]) for c in coord_rows if c["K_req_coord_Mpc^-1"] is not None})
    for K in finite:
        retained = [c for c in coord_rows if c["K_req_coord_Mpc^-1"] is not None and c["K_req_coord_Mpc^-1"] <= K]
        cov = {}
        ok = len(retained) >= 15
        for sample in SAMPLES:
            cov[sample] = {}
            for ch in ("gg", "kg"):
                n = sum(c["sample"] == sample and c["channel"] == ch for c in retained)
                cov[sample][ch] = n
                ok &= n >= 1
        if ok:
            return K, {"retained_dimension": len(retained), "by_sample_channel": cov, "retained_indices": [c["index"] for c in retained]}
    return None, None


def nondominated(points: list[dict]) -> list[dict]:
    out = []
    for i, p in enumerate(points):
        dominated = False
        for j, q in enumerate(points):
            if i == j:
                continue
            no_more_z = q["z_min"] >= p["z_min"]
            no_more_k = q["k_max_Mpc^-1"] <= p["k_max_Mpc^-1"]
            strict = q["z_min"] > p["z_min"] or q["k_max_Mpc^-1"] < p["k_max_Mpc^-1"]
            if no_more_z and no_more_k and strict:
                dominated = True
                break
        if not dominated:
            out.append(p)
    return sorted(out, key=lambda x: (-x["z_min"], x["k_max_Mpc^-1"]))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream-repo", required=True)
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--exp072a-json", required=True)
    ap.add_argument("--exp072a-meta", required=True)
    ap.add_argument("--exp072b-json", required=True)
    ap.add_argument("--exp072b-meta", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    upstream_repo = Path(args.upstream_repo).resolve()
    camb_repo = Path(args.camb_repo).resolve()
    extracted_root = Path(args.extracted_root).resolve()
    archive = Path(args.archive).resolve()
    output = Path(args.output).resolve()

    a, a_bind = bind_artifact(Path(args.exp072a_json), Path(args.exp072a_meta), run=EXP072A_RUN, artifact=EXP072A_ARTIFACT, digest=EXP072A_DIGEST, head=EXP072A_HEAD, json_sha=EXP072A_JSON_SHA256, status=EXP072A_STATUS)
    b, b_bind = bind_artifact(Path(args.exp072b_json), Path(args.exp072b_meta), run=EXP072B_RUN, artifact=EXP072B_ARTIFACT, digest=EXP072B_DIGEST, head=EXP072B_HEAD, json_sha=EXP072B_JSON_SHA256, status=EXP072B_STATUS)

    b_specific = bool(
        b.get("K_target_route_Mpc^-1") is None
        and len(b.get("coordinates", [])) == 26
        and len(b.get("coordinate_block_pairs", [])) == 64
        and all(v is True for v in b.get("hard_controls", {}).values())
    )

    upstream_head = git_head(upstream_repo)
    camb_head = git_head(camb_repo)
    archive_hash = base.sha256(archive)
    src_contract = parent_impl.source_contract(upstream_repo)
    provenance = {
        "upstream_commit": upstream_head,
        "expected_upstream_commit": UPSTREAM_PIN,
        "CAMB_commit": camb_head,
        "expected_CAMB_commit": CAMB_PIN,
        "archive_sha256": archive_hash,
        "expected_archive_sha256": ARCHIVE_SHA256,
        "source_contract": src_contract,
    }
    provenance["pass"] = bool(upstream_head == UPSTREAM_PIN and camb_head == CAMB_PIN and archive_hash == ARCHIVE_SHA256 and src_contract["pass"])

    _, CosmoFromCamb, Dndz, DndzHelper, upstream_theory_contract = base.load_exact_upstream(upstream_repo)
    data_root = base.find_data_root(extracted_root)
    tracers, _ = base.build_real_tracers(data_root, Dndz, DndzHelper)
    camb_results, _, _, _ = base.build_camb_physical()
    cosmo = CosmoFromCamb(camb_results, include_nu_OmegaM=True)

    pix = np.asarray(hp.pixwin(NSIDE), dtype=np.float64)[: ELL.size]
    pix_ok = bool(pix.shape == (ELL.size,) and np.all(np.isfinite(pix)))
    cfg = upstream_repo / "unWISExLens_lklh" / "config_files"
    binning_cfg = yaml.safe_load((cfg / "binning_setup.yaml").read_text())
    operators = {s: parent_impl.load_operator(data_root, binning_cfg, s, pix) for s in SAMPLES}
    operator_pass = bool(pix_ok and all(operators[s]["pass"] for s in SAMPLES))

    # Geometry is common to both tracers; derive the frozen discrete candidate sets from it.
    _, _, z_geom, _, k_geom = parent_impl.build_kernel_envelopes(cosmo, tracers[0])
    z_candidates = sorted(set([Z0] + [float(x) for x in z_geom if 0.0 <= float(x) <= Z0]), reverse=True)
    flat_k = k_geom.ravel()
    sort_idx = np.argsort(flat_k, kind="mergesort")
    sorted_k = flat_k[sort_idx]
    uniq_k, first, counts = np.unique(sorted_k, return_index=True, return_counts=True)
    uniq_end = first + counts - 1
    sampled_k_set = set(float(x) for x in uniq_k[uniq_k >= K0])

    pair_order_pass = True
    parent_repro_pass = True
    closure_pass = True
    k_monotonic_pass = True
    z_monotonic_pass = True
    discrete_pass = True

    # Prebuild exact pair weights/order matching Exp072B.
    pair_defs = []
    coord_defs = []
    pair_index = 0
    coord_index = 0
    for s_idx, sample in enumerate(SAMPLES):
        kernels, _, z, _, k_grid = parent_impl.build_kernel_envelopes(cosmo, tracers[s_idx])
        if not np.array_equal(z, z_geom) or not np.array_equal(k_grid, k_geom):
            pair_order_pass = False
        for channel in ("gg", "kg"):
            rows = operators[sample]["channels"][channel]["selected_row_indices"]
            centers = operators[sample]["channels"][channel]["selected_ell_midpoints"]
            bw = np.asarray(operators[sample]["channels"][channel]["bandwindow"], dtype=np.float64)
            tr = np.asarray(operators[sample]["channels"][channel]["transfer"], dtype=np.float64)
            pw = np.asarray(operators[sample]["channels"][channel]["pixel_window"], dtype=np.float64)
            for row, center in zip(rows, centers):
                coord_pair_indices = []
                op = np.abs(bw[int(row)] * tr[int(row)] * pw)
                for block in CHANNEL_BLOCKS[channel]:
                    weight = np.asarray(kernels[channel][block], dtype=np.float64)[:, None] * op[None, :]
                    pair_defs.append({
                        "pair_index": pair_index,
                        "coordinate_index": coord_index,
                        "sample": sample,
                        "channel": channel,
                        "ell_midpoint": float(center),
                        "block": block,
                        "weight": weight,
                    })
                    coord_pair_indices.append(pair_index)
                    pair_index += 1
                coord_defs.append({"index": coord_index, "sample": sample, "channel": channel, "ell_midpoint": float(center), "pair_indices": coord_pair_indices})
                coord_index += 1

    pair_order_pass &= bool(pair_index == 64 and coord_index == 26)
    b_pairs = b.get("coordinate_block_pairs", [])
    if len(b_pairs) != 64:
        pair_order_pass = False

    pair_curves = []
    pair_curve_map = {}
    for pd in pair_defs:
        bi = b_pairs[pd["pair_index"]] if pd["pair_index"] < len(b_pairs) else {}
        pair_order_pass &= bool(
            bi.get("pair_index") == pd["pair_index"]
            and bi.get("coordinate_index") == pd["coordinate_index"]
            and bi.get("sample") == pd["sample"]
            and bi.get("channel") == pd["channel"]
            and bi.get("block") == pd["block"]
            and abs(float(bi.get("ell_midpoint", np.nan)) - pd["ell_midpoint"]) <= 1e-12
        )

        curve = []
        previous_current_leak = None
        previous_kreq = None
        for zi, Z in enumerate(z_candidates):
            rec = pair_req_for_z(pd["weight"], z_geom, k_geom, Z, sort_idx, uniq_k, uniq_end)
            closure_pass &= rec["bookkeeping_closure_abs"] <= EPS128
            k_monotonic_pass &= rec["k_monotonic"]
            if zi == 0:
                # z_candidates starts at exact current Z0.
                parent_leak = float(bi.get("reproduced_leakage_V0", np.nan))
                parent_repro_pass &= bool(np.isfinite(parent_leak) and abs(rec["current_K0_leakage"] - parent_leak) <= REPRO_TOL)
            if previous_current_leak is not None:
                # Lowering Z cannot increase leakage at fixed K0.
                z_monotonic_pass &= rec["current_K0_leakage"] <= previous_current_leak + EPS128
            previous_current_leak = rec["current_K0_leakage"]

            kr = rec["K_req_pair_Mpc^-1"]
            if kr is not None:
                discrete_pass &= kr in sampled_k_set and kr >= K0
                if previous_kreq is not None:
                    z_monotonic_pass &= kr <= previous_kreq + EPS128 * max(1.0, abs(previous_kreq))
                previous_kreq = kr
            curve.append(rec)

        key = pd["pair_index"]
        pair_curve_map[key] = curve
        pair_curves.append({k: v for k, v in pd.items() if k != "weight"} | {"curve": curve})

    z_rows = []
    for zi, Z in enumerate(z_candidates):
        coords = []
        for cd in coord_defs:
            reqs = []
            inf = False
            for pi in cd["pair_indices"]:
                kr = pair_curve_map[pi][zi]["K_req_pair_Mpc^-1"]
                if kr is None:
                    inf = True
                    break
                reqs.append(float(kr))
            kcoord = None if inf else max(reqs)
            if kcoord is not None:
                discrete_pass &= kcoord in sampled_k_set
            coords.append({**cd, "K_req_coord_Mpc^-1": kcoord, "K_req_coord_is_infinite": kcoord is None})
        kroute, snap = route_at_z(coords)
        if kroute is not None:
            discrete_pass &= kroute in sampled_k_set
        z_rows.append({"z_min": float(Z), "K_route_Mpc^-1": kroute, "route_snapshot": snap, "coordinates": coords})

    current_route_repro = bool(z_rows and z_rows[0]["z_min"] == Z0 and z_rows[0]["K_route_Mpc^-1"] is None)
    finite_points = [
        {"z_min": r["z_min"], "k_max_Mpc^-1": r["K_route_Mpc^-1"], "route_snapshot": r["route_snapshot"]}
        for r in z_rows if r["K_route_Mpc^-1"] is not None
    ]
    frontier = nondominated(finite_points)

    frontier_pass = True
    for i, p in enumerate(frontier):
        discrete_pass &= p["k_max_Mpc^-1"] in sampled_k_set
        for j, q in enumerate(frontier):
            if i == j:
                continue
            dominates = q["z_min"] >= p["z_min"] and q["k_max_Mpc^-1"] <= p["k_max_Mpc^-1"] and (q["z_min"] > p["z_min"] or q["k_max_Mpc^-1"] < p["k_max_Mpc^-1"])
            frontier_pass &= not dominates

    min_z_extension = None
    min_k_extension = None
    if frontier:
        zbest = max(p["z_min"] for p in frontier)
        zc = [p for p in frontier if p["z_min"] == zbest]
        min_z_extension = min(zc, key=lambda p: p["k_max_Mpc^-1"])
        kbest = min(p["k_max_Mpc^-1"] for p in frontier)
        kc = [p for p in frontier if p["k_max_Mpc^-1"] == kbest]
        min_k_extension = max(kc, key=lambda p: p["z_min"])

    hard_controls = {
        "C1_exact_Exp072A_Exp072B_binding": bool(a_bind["pass"] and b_bind["pass"] and b_specific),
        "C2_exact_external_operator_and_ordering": bool(provenance["pass"] and upstream_theory_contract["pass"] and operator_pass and pair_order_pass),
        "C3_reproduce_Exp072B_current_boundary": bool(parent_repro_pass and current_route_repro),
        "C4_positive_weight_bookkeeping_closure_128eps": bool(closure_pass),
        "C5_lower_z_and_upper_k_monotonicity": bool(z_monotonic_pass and k_monotonic_pass),
        "C6_all_reported_k_values_are_sampled": bool(discrete_pass),
        "C7_frontier_nondominance_and_extrema": bool(frontier_pass),
        "C8_no_downstream_or_new_provider_output_read": True,
    }
    hard_pass = bool(all(hard_controls.values()))
    if not hard_pass:
        status = FAIL
    elif frontier:
        status = FOUND
    else:
        status = NOT_FOUND

    result = {
        "experiment": "Exp072C",
        "date": "2026-08-27",
        "status": status,
        "scope": "joint discrete lower-z/upper-k support-frontier diagnostic only; no provider extension or observational covariance/nuisance/G7 evaluation",
        "preregistration": "experiments/072c_joint_lowz_highk_support_frontier_prereg_v0_1.md",
        "Exp072A_binding": a_bind,
        "Exp072B_binding": b_bind,
        "Exp072A_preserved": EXP072A_STATUS,
        "Exp072B_preserved": EXP072B_STATUS,
        "provenance": provenance,
        "fixed_boundaries": {"z_max": ZMAX, "k_min_Mpc^-1": KMIN, "threshold": THRESHOLD, "z_min_current": Z0, "k_max_current_Mpc^-1": K0},
        "candidate_sets": {
            "z_min_candidates_descending": z_candidates,
            "z_candidate_count": len(z_candidates),
            "sampled_k_candidate_count_ge_current": int(np.sum(uniq_k >= K0)),
        },
        "z_route_rows": z_rows,
        "pair_curves": pair_curves,
        "finite_route_point_count": len(finite_points),
        "pareto_frontier": frontier,
        "pareto_frontier_count": len(frontier),
        "minimal_redshift_extension_endpoint": min_z_extension,
        "minimal_k_extension_endpoint": min_k_extension,
        "hard_controls": hard_controls,
        "controls": {
            "covariance_read": False,
            "cholesky_or_whitener_read": False,
            "nuisance_SVD_or_rank_read": False,
            "G7_relation_or_null_read": False,
            "G8_response_read": False,
            "article_selection_quantity_read": False,
            "physical_provider_extended": False,
            "threshold_changed": False,
            "Exp072A_reclassified": False,
            "Exp072B_reclassified": False,
        },
        "next_step_if_frontier_found": "Freeze a separate C3+C5 physical provider-extension target chosen only from the frozen Pareto frontier, then independently certify native/raw support before any new angular leakage gate.",
        "next_step_if_frontier_not_found": "Current two-boundary extension is insufficient; a later prospective diagnostic must address the remaining fixed upper-z and/or lower-k support without rewriting Exp072A/B/C.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
