#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path

import numpy as np

PASS = "PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2"
FAIL = "FAIL_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2"
INVALID = "INVALID_FOR_SCIENCE_EXP073IM"
REP = "FACTORIZED_BROAD_SUPPORT_V0_2"


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical(a: np.ndarray, dtype: str = "<f8") -> np.ndarray:
    return np.ascontiguousarray(np.asarray(a, dtype=np.dtype(dtype)))


def ah(a: np.ndarray, dtype: str = "<f8") -> dict:
    x = canonical(a, dtype)
    return {"dtype": x.dtype.str, "shape": list(x.shape), "sha256": sha_bytes(x.tobytes())}


def sha_lines(lines: list[str]) -> str:
    return sha_bytes(("\n".join(lines) + "\n").encode())


def json_digest(rows: list[dict]) -> str:
    payload = "\n".join(json.dumps(x, sort_keys=True, separators=(",", ":")) for x in rows) + "\n"
    return sha_bytes(payload.encode())


def load_json_candidate(root: Path, required_key: str) -> dict:
    hits = []
    for p in root.rglob("*.json"):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(obj, dict) and required_key in obj:
            hits.append((p, obj))
    if len(hits) != 1:
        raise AssertionError(f"expected one JSON carrying {required_key}, got {[str(x[0]) for x in hits]}")
    return hits[0][1]


def find_npz_array(root: Path, name: str, spec: dict) -> np.ndarray:
    matches = []
    for p in root.rglob("*.npz"):
        with np.load(p, allow_pickle=False) as z:
            for key in z.files:
                x = z[key]
                h = ah(x, spec["dtype"])
                if h == spec:
                    matches.append((p, key, canonical(x, spec["dtype"])))
    if not matches:
        raise AssertionError(f"no exact radial array for {name} / {spec['sha256']}")
    # Multiple byte-identical carriers are allowed; logical authority is the canonical bytes.
    return matches[0][2]


def find_angular(root: Path, spec: dict) -> tuple[np.ndarray, list[str]]:
    target = spec["canonical_sha256"]
    shape = tuple(spec["shape"])
    dtype = spec["dtype"]
    expected_nbytes = int(np.prod(shape)) * np.dtype(dtype).itemsize
    matches: list[tuple[str, np.ndarray]] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        try:
            if p.suffix == ".bin" and p.stat().st_size == expected_nbytes:
                raw = p.read_bytes()
                if sha_bytes(raw) == target:
                    matches.append((str(p), np.frombuffer(raw, dtype=np.dtype(dtype)).reshape(shape).copy()))
            elif p.suffix == ".npy":
                x = canonical(np.load(p, allow_pickle=False), dtype)
                if x.shape == shape and sha_bytes(x.tobytes()) == target:
                    matches.append((str(p), x))
            elif p.suffix == ".npz":
                with np.load(p, allow_pickle=False) as z:
                    for key in z.files:
                        x = canonical(z[key], dtype)
                        if x.shape == shape and sha_bytes(x.tobytes()) == target:
                            matches.append((f"{p}::{key}", x.copy()))
        except Exception:
            continue
    if not matches:
        raise AssertionError(f"no exact angular logical array {target} in {root}")
    return matches[0][1], [m[0] for m in matches]


def parse_des_row(cid: str, ordinal: int, pair_to_ww_index: dict[tuple[int, int], int]) -> dict:
    if cid.startswith("Wm|"):
        ml = re.search(r"DESgc__(\d+)", cid)
        ms = re.search(r"DESwl__(\d+)", cid)
        mb = re.search(r"bp=(\d+)", cid)
        if not (ml and ms and mb):
            raise AssertionError(f"unparseable Wm id {cid}")
        lens, src, band = int(ml.group(1)), int(ms.group(1)), int(mb.group(1))
        if not (0 <= lens < 5 and 0 <= src < 4 and 0 <= band < 39):
            raise AssertionError("Wm index outside frozen inventory")
        return {
            "coordinate_id": cid, "ordinal": ordinal, "block": "Wm",
            "slot": f"Wm_S{src}", "band_index": band,
            "lens_bin": lens, "source_bin": src,
            "radial_index": lens * 4 + src, "representation": REP,
        }
    if cid.startswith("WW|"):
        ss = [int(x) for x in re.findall(r"DESwl__(\d+)", cid)]
        mb = re.search(r"bp=(\d+)", cid)
        if len(ss) != 2 or not mb:
            raise AssertionError(f"unparseable WW id {cid}")
        i, j = ss
        band = int(mb.group(1))
        if i > j or (i, j) not in pair_to_ww_index or not (0 <= band < 39):
            raise AssertionError("WW index outside frozen inventory")
        return {
            "coordinate_id": cid, "ordinal": ordinal, "block": "WW",
            "slot": f"WW_S{i}_S{j}", "band_index": band,
            "source_bin_i": i, "source_bin_j": j,
            "radial_index": pair_to_ww_index[(i, j)], "representation": REP,
        }
    raise AssertionError(f"non-DES row in DES prefix: {cid}")


def write(out: Path, obj: dict) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--inputs", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        manifest = json.loads(Path(a.manifest).read_text(encoding="utf-8"))
        assert manifest["schema"] == "EXP073IM_C2_REAL_INPUT_MANIFEST_V0_3"
        root = Path(a.inputs)

        # Exact inherited observation order from Exp073U.
        skel = load_json_candidate(root / "presupport", "ordered_coordinate_ids")
        ids = skel["ordered_coordinate_ids"]
        assert len(ids) == manifest["presupport_order"]["full_row_count"] == 1410
        assert sha_lines(ids) == manifest["presupport_order"]["full_order_sha256"]
        des_ids = ids[:1170]
        assert sha_lines(des_ids) == manifest["presupport_order"]["des_order_sha256"]
        assert sum(x.startswith("Wm|") for x in des_ids) == 780
        assert sum(x.startswith("WW|") for x in des_ids) == 390

        # Exact Exp073Z2 arrays.
        rroot = root / "radial"
        rspec = manifest["radial"]["arrays"]
        z = find_npz_array(rroot, "z_fine", rspec["z_fine"])
        chi = find_npz_array(rroot, "chi_Mpc", rspec["chi_Mpc"])
        wm = find_npz_array(rroot, "Wm_radial", rspec["Wm_radial"])
        ww = find_npz_array(rroot, "WW_radial", rspec["WW_radial"])
        if not (np.isfinite(z).all() and np.isfinite(chi).all() and np.isfinite(wm).all() and np.isfinite(ww).all()):
            raise AssertionError("non-finite frozen radial/geometry array")
        if not (np.all(np.diff(z) > 0) and np.all(np.diff(chi) >= 0) and z.size == 2001):
            raise AssertionError("radial geometry ordering failure")
        if np.any(wm < 0) or np.any(ww < 0):
            raise AssertionError("frozen positive radial envelope became negative")

        # Verify all 14 immutable angular byte authorities, without recomputation.
        angular: dict[str, np.ndarray] = {}
        carriers = {}
        expected_slots = [x["slot"] for x in manifest["angular"]]
        for spec in manifest["angular"]:
            slot = spec["slot"]
            x, hits = find_angular(root / "angular" / slot, spec)
            if not np.isfinite(x).all():
                raise AssertionError(f"nonfinite exact angular authority {slot}")
            angular[slot] = x
            carriers[slot] = hits
        assert list(angular) == expected_slots and len(angular) == 14

        # Frozen pair/index ordering from Exp073Z2: lens-major Wm, i<=j WW.
        ww_pairs = [(i, j) for i in range(4) for j in range(i, 4)]
        pair_to_ww_index = {p: q for q, p in enumerate(ww_pairs)}
        rows = [parse_des_row(cid, q, pair_to_ww_index) for q, cid in enumerate(des_ids)]
        assert len({r["coordinate_id"] for r in rows}) == 1170
        assert [r["ordinal"] for r in rows] == list(range(1170))
        assert set(r["slot"] for r in rows) == set(expected_slots)
        assert {r["radial_index"] for r in rows if r["block"] == "Wm"} == set(range(20))
        assert {r["radial_index"] for r in rows if r["block"] == "WW"} == set(range(10))

        trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
        wm_norm = np.asarray(trapz(wm, z, axis=1), dtype=np.float64)
        ww_norm = np.asarray(trapz(ww, z, axis=1), dtype=np.float64)
        radial_good = bool(np.isfinite(wm_norm).all() and np.isfinite(ww_norm).all() and np.all(wm_norm > 0) and np.all(ww_norm > 0))

        # All released bands must have a nonempty exact angular envelope. This is an
        # upstream-integrity diagnostic; no physical-domain cut is performed here.
        band_nonempty = {}
        for slot, x in angular.items():
            sums = np.sum(np.abs(x), axis=1)
            band_nonempty[slot] = bool(np.isfinite(sums).all() and np.all(sums > 0))
        if not all(band_nonempty.values()):
            raise AssertionError("exact admitted angular authority contains empty/nonfinite band")

        # Attach only authority pointers and radial normalizations. No scalar z/k and
        # no physical-support score are emitted by this gate.
        angular_specs = {x["slot"]: x for x in manifest["angular"]}
        for r in rows:
            ri = r["radial_index"]
            r["angular_canonical_sha256"] = angular_specs[r["slot"]]["canonical_sha256"]
            if r["block"] == "Wm":
                r["radial_canonical_sha256"] = rspec["Wm_radial"]["sha256"]
                r["radial_normalization"] = float(wm_norm[ri])
            else:
                r["radial_canonical_sha256"] = rspec["WW_radial"]["sha256"]
                r["radial_normalization"] = float(ww_norm[ri])

        d1 = json_digest(rows)
        d2 = json_digest(sorted(reversed(rows), key=lambda x: x["ordinal"]))
        assert d1 == d2

        status = PASS if radial_good else FAIL
        result = {
            "experiment": "Exp073IM",
            "schema": "EXP073IM_C2_REAL_RADIAL_SUPPORT_RESULT_V0_2",
            "status": status,
            "scientific_radial_pass": radial_good,
            "representation": REP,
            "angular_authorities_verified": 14,
            "Wm_rows": 780, "WW_rows": 390, "total_rows": 1170,
            "Wm_radial_indices": 20, "WW_radial_indices": 10,
            "Wm_radial_normalization_min": float(wm_norm.min()),
            "WW_radial_normalization_min": float(ww_norm.min()),
            "ordered_broad_row_manifest_sha256": d1,
            "permutation_replay_identical": True,
            "effective_ell_override": False,
            "effective_z_override": False,
            "effective_k_override": False,
            "physical_support_evaluated": False,
            "covariance_read": False,
            "nuisance_read": False,
            "relation_null_read": False,
            "selection_reads": [],
            "angular_carriers": carriers,
            "radial_array_authorities": {k: ah(v) for k, v in {"z_fine":z,"chi_Mpc":chi,"Wm_radial":wm,"WW_radial":ww}.items()},
            "rows": rows,
        }
        write(out, result)
        print(status, d1)
        return 0
    except Exception as e:
        write(out, {
            "experiment": "Exp073IM", "status": INVALID,
            "classification": "PROVENANCE_INTERFACE_OR_EXECUTION_INVALID_NOT_SCIENCE_FAIL",
            "error": f"{type(e).__name__}: {e}",
            "physical_support_evaluated": False,
            "downstream_reads": [],
        })
        print(INVALID, repr(e), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
