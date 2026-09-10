#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

import numpy as np

PARENT_RETAINED_SHA = "44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7"
FULL_ORDER_SHA = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
KMAX = 0.06664762008318016
ZMIN = 0.295
ZMAX = 2.33


def sha_lines(xs):
    return hashlib.sha256(("\n".join(xs) + "\n").encode()).hexdigest()


def put(h, tag, payload):
    tb = tag.encode("utf-8")
    pb = bytes(payload)
    h.update(struct.pack("<I", len(tb)))
    h.update(tb)
    h.update(struct.pack("<Q", len(pb)))
    h.update(pb)


def arr_bytes(a, dtype):
    return np.ascontiguousarray(np.asarray(a, dtype=dtype), dtype=dtype).tobytes()


def main():
    ap = argparse.ArgumentParser()
    for x in (
        "ir-script", "parent-root", "parent-authority", "manifest", "angular-root",
        "expim-root", "boss-root", "source", "lens", "camb-root", "expz2-script",
        "exp073iq-script", "out"
    ):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()

    # Import frozen helpers only. This audit never imports classy and never evaluates a CLASS response.
    import importlib.util

    def load_module(name, path):
        spec = importlib.util.spec_from_file_location(name, Path(path))
        if spec is None or spec.loader is None:
            raise RuntimeError(f"cannot import {path}")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return m

    ir = load_module("exp073ir_request_plan_parent", a.ir_script)
    iq = load_module("exp073iq_request_plan_parent", a.exp073iq_script)

    if ir.KMAX != KMAX or ir.ZMIN != ZMIN or ir.ZMAX != ZMAX:
        raise SystemExit("IR physical-domain constants mismatch")
    if ir.PARENT_RETAINED_SHA != PARENT_RETAINED_SHA or ir.FULL_ORDER_SHA != FULL_ORDER_SHA:
        raise SystemExit("IR parent hashes mismatch")

    auth = json.loads(Path(a.parent_authority).read_text())
    if not (
        auth.get("status") == ir.LAYERA_PASS
        and auth.get("workflow_run") == 34423479633
        and auth.get("workflow_job") == 102703685034
        and auth.get("artifact_id") == 10131794281
        and auth.get("combined_retained_count") == 107
        and auth.get("retained_id_sha256") == PARENT_RETAINED_SHA
        and auth.get("full_order_sha256") == FULL_ORDER_SHA
    ):
        raise SystemExit("parent authority mismatch")

    parent = ir.load_one_json(
        a.parent_root,
        lambda d: d.get("schema") == "EXP073IQ_ARTICLE3_REAL_LAYERA_SUPPORT_RESULT_V0_1",
    )
    retained = parent["retained_coordinate_ids"]
    if not (
        parent.get("status") == ir.LAYERA_PASS
        and len(retained) == 107
        and len(set(retained)) == 107
        and sha_lines(retained) == PARENT_RETAINED_SHA
        and parent.get("full_order_sha256") == FULL_ORDER_SHA
    ):
        raise SystemExit("parent payload mismatch")

    manifest = json.loads(Path(a.manifest).read_text())
    if manifest.get("schema") != "EXP073IM_C2_REAL_INPUT_MANIFEST_V0_4":
        raise SystemExit("manifest schema mismatch")
    angular = {
        s["slot"]: iq.find_angular(Path(a.angular_root) / s["slot"], s)
        for s in manifest["angular"]
    }
    expim = ir.load_one_json(a.expim_root, lambda d: d.get("status") == ir.EXPIM_PASS)
    if len(expim.get("rows", [])) != 1170 or expim.get("scientific_radial_pass") is not True:
        raise SystemExit("Exp073IM payload mismatch")
    expim_map = {r["coordinate_id"]: r for r in expim["rows"]}

    rad = iq.reconstruct_radials(
        iq.import_expz2(Path(a.expz2_script)), a.source, a.lens, a.camb_root, manifest
    )["fine"]
    zdes = np.asarray(rad["z"], dtype=np.float64)
    chides = np.asarray(rad["chi"], dtype=np.float64)
    if zdes.shape != (2001,) or chides.shape != (2001,):
        raise SystemExit("DES radial geometry mismatch")

    des_parent = {r["coordinate_id"]: r for r in parent["des_rows"] if r["retained"]}
    if len(des_parent) != 53:
        raise SystemExit("DES retained-count mismatch")
    des_meta = [expim_map[cid] for cid in retained if cid in des_parent]
    if len(des_meta) != 53:
        raise SystemExit("DES metadata-count mismatch")

    boss_ids, boss_w, boss_k = ir.boss_geometry(a.boss_root)
    boss_index = {cid: i for i, cid in enumerate(boss_ids)}
    boss_ret = [cid for cid in retained if cid in boss_index]
    if len(boss_ret) != 54:
        raise SystemExit("BOSS retained-count mismatch")

    hc = hashlib.sha256()
    hf = hashlib.sha256()

    def both(tag, payload):
        put(hc, tag, payload)
        put(hf, tag, payload)

    both("schema", b"RECOVERED_EXP073JL_RESPONSE_BLIND_REQUEST_PLAN_V0_1")
    both("parent_retained_ids", ("\n".join(retained) + "\n").encode())
    both("domain", struct.pack("<ddd", ZMIN, ZMAX, KMAX))
    both("des_z", arr_bytes(zdes, "<f8"))
    both("des_chi", arr_bytes(chides, "<f8"))

    des_request_count = 0
    des_total_targets = 0
    des_row_bindings = 0
    des_empty_z = 0

    ell = np.arange(12288, dtype=np.float64) + 0.5
    for iz, z in enumerate(zdes):
        with np.errstate(divide="ignore", invalid="ignore"):
            k = ell / chides[iz]
        inD = (k > 0.0) & (k <= KMAX) & (z >= ZMIN) & (z <= ZMAX)
        union = np.zeros(12288, dtype=bool)
        active_by_row = []
        for r in des_meta:
            B = rad["wm" if r["block"] == "Wm" else "ww"][int(r["radial_index"])]
            if not (float(B[iz]) > 0.0):
                continue
            active = (np.abs(angular[r["slot"]][int(r["band_index"])]) > 0.0) & inD
            if np.any(active):
                active_by_row.append((r["coordinate_id"], active))
                union |= active

        both(f"des/{iz:04d}/z", struct.pack("<d", float(z)))
        if not np.any(union):
            both(f"des/{iz:04d}/empty", b"1")
            des_empty_z += 1
            continue

        idx = np.flatnonzero(union).astype("<u4", copy=False)
        targets = np.asarray(k[union], dtype="<f8")
        both(f"des/{iz:04d}/indices", idx.tobytes())
        both(f"des/{iz:04d}/targets", targets.tobytes())
        des_request_count += 1
        des_total_targets += int(targets.size)
        for cid, active in active_by_row:
            mask = np.asarray(active[union], dtype=np.uint8)
            both(f"des/{iz:04d}/row/{cid}", mask.tobytes())
            des_row_bindings += 1

    needed = np.zeros(1200, dtype=bool)
    for cid in boss_ret:
        i = boss_index[cid]
        needed |= (boss_w[i] > 0.0) & (boss_k > 0.0) & (boss_k <= KMAX)
    kt = np.asarray(boss_k[needed], dtype="<f8")
    both("boss/retained_ids", ("\n".join(boss_ret) + "\n").encode())
    both("boss/needed_mask", np.asarray(needed, dtype=np.uint8).tobytes())
    both("boss/targets", kt.tobytes())
    for cid in boss_ret:
        i = boss_index[cid]
        am = ((boss_w[i] > 0.0) & (boss_k > 0.0) & (boss_k <= KMAX))[needed]
        both(f"boss/row/{cid}", np.asarray(am, dtype=np.uint8).tobytes())

    zb64, _ = ir.gl_nodes(64)
    zb128, _ = ir.gl_nodes(128)
    both("boss/gl64_z", arr_bytes(zb64, "<f8"))
    put(hf, "boss/gl128_z", arr_bytes(zb128, "<f8"))

    coarse_calls_per_role = des_request_count + 64
    fine_calls_per_role = des_request_count + 64 + 128
    total_get_transfer_calls = 4 * coarse_calls_per_role + 4 * fine_calls_per_role
    coarse_scalars_per_role = des_total_targets + 64 * int(kt.size)
    fine_scalars_per_role = des_total_targets + (64 + 128) * int(kt.size)

    result = {
        "schema": "RECOVERED_EXP073JL_RESPONSE_BLIND_REQUEST_PLAN_AUDIT_RESULT_V0_1",
        "classification": "RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0",
        "effect": "+0/+0",
        "scientific_response_read": False,
        "class_solver_invoked": False,
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "parent_retained_count": len(retained),
        "parent_retained_id_sha256": PARENT_RETAINED_SHA,
        "parent_full_order_sha256": FULL_ORDER_SHA,
        "des": {
            "z_count": int(zdes.size),
            "retained_rows": len(des_meta),
            "nonempty_solver_request_count_per_role": des_request_count,
            "empty_z_count": des_empty_z,
            "total_target_scalars_per_role": des_total_targets,
            "active_row_bindings": des_row_bindings,
        },
        "boss": {
            "retained_rows": len(boss_ret),
            "target_scalar_count_per_request": int(kt.size),
            "gl64_z_count": int(zb64.size),
            "gl128_z_count_fine_only": int(zb128.size),
        },
        "execution_shape_if_recovered_one_live": {
            "coarse_solver_constructions": 4,
            "fine_solver_constructions": 4,
            "total_solver_constructions": 8,
            "max_live_instances": 1,
            "coarse_get_transfer_calls_per_role": coarse_calls_per_role,
            "fine_get_transfer_calls_per_role": fine_calls_per_role,
            "total_get_transfer_calls_all_roles": total_get_transfer_calls,
            "coarse_raw_scalar_count_per_role": coarse_scalars_per_role,
            "fine_raw_scalar_count_per_role": fine_scalars_per_role,
            "coarse_four_role_raw_bytes_flat_f8": 4 * coarse_scalars_per_role * 8,
            "fine_four_role_raw_bytes_flat_f8": 4 * fine_scalars_per_role * 8,
        },
        "coarse_common_plan_sha256": hc.hexdigest(),
        "fine_plan_with_gl128_sha256": hf.hexdigest(),
        "article3_repository_readiness_percent": 68,
        "funnel_freeze_readiness_percent": 67,
        "token": "RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0",
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
