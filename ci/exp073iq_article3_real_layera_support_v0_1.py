#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
from pathlib import Path

import numpy as np
import camb

PASS = "PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1"
FAIL = "FAIL_ARTICLE3_OPERATOR_SUPPORT_V0_1"
INVALID = "INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1"
UNRES = "NUMERICALLY_UNRESOLVED_AT_5PCT_BOUNDARY"
ZMIN = 0.295
ZMAX = 2.33
KMAX = 0.06664762008318016
THRESH = 0.05
CONV = 5e-4
FULL_ORDER_SHA = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
BOSS_MASK_SHA = "249f4d6facd52e640ba170898a91191a6c918a58ab5cb04870687bf5a8c9ac32"
BOSS_F_SHA = "4e561cac60c76af3ccc4a858cd7510a7e0c7196e1f71aaba261e3b97715bfff7"
EXPIM_PASS = "PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2"


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical(a, dtype):
    return np.ascontiguousarray(np.asarray(a, dtype=np.dtype(dtype)))


def ah(a, dtype):
    x = canonical(a, dtype)
    return {"dtype": x.dtype.str, "shape": list(x.shape), "sha256": sha_bytes(x.tobytes())}


def sha_lines(lines: list[str]) -> str:
    return sha_bytes(("\n".join(lines) + "\n").encode())


def load_one_json(root: Path, predicate) -> dict:
    hits = []
    for p in root.rglob("*.json"):
        try:
            x = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(x, dict) and predicate(x):
            hits.append((p, x))
    if len(hits) != 1:
        raise AssertionError(f"expected one matching JSON, got {[str(p) for p,_ in hits]}")
    return hits[0][1]


def find_angular(root: Path, spec: dict) -> np.ndarray:
    target = spec["canonical_sha256"]
    shape = tuple(spec["shape"])
    dtype = spec["dtype"]
    nbytes = int(np.prod(shape)) * np.dtype(dtype).itemsize
    hits = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        try:
            if p.suffix == ".bin" and p.stat().st_size == nbytes:
                raw = p.read_bytes()
                if sha_bytes(raw) == target:
                    hits.append(np.frombuffer(raw, dtype=np.dtype(dtype)).reshape(shape).copy())
            elif p.suffix == ".npy":
                x = canonical(np.load(p, allow_pickle=False), dtype)
                if x.shape == shape and sha_bytes(x.tobytes()) == target:
                    hits.append(x)
            elif p.suffix == ".npz":
                with np.load(p, allow_pickle=False) as z:
                    for key in z.files:
                        x = canonical(z[key], dtype)
                        if x.shape == shape and sha_bytes(x.tobytes()) == target:
                            hits.append(x.copy())
        except Exception:
            pass
    if not hits:
        raise AssertionError(f"missing exact angular authority {target} under {root}")
    return hits[0]


def pl_integral(z, y, a, b):
    z = np.asarray(z, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if np.any(~np.isfinite(z)) or np.any(~np.isfinite(y)) or np.any(np.diff(z) <= 0):
        raise AssertionError("invalid piecewise-linear representation")
    if np.any(y < 0):
        raise AssertionError("negative radial support")
    a = max(float(a), float(z[0])); b = min(float(b), float(z[-1]))
    if b <= a:
        return 0.0
    inner = z[(z > a) & (z < b)]
    x = np.concatenate(([a], inner, [b]))
    yy = np.interp(x, z, y)
    trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trapz(yy, x))


def inverse_chi(z, chi, target):
    z = np.asarray(z, dtype=np.float64); chi = np.asarray(chi, dtype=np.float64)
    if np.any(np.diff(chi) <= 0):
        raise AssertionError("chi must be strictly increasing")
    if target <= chi[0]: return float(z[0])
    if target > chi[-1]: return None
    j = int(np.searchsorted(chi, target, side="left"))
    if chi[j] == target: return float(z[j])
    i = j - 1
    return float(z[i] + (target-chi[i])*(z[j]-z[i])/(chi[j]-chi[i]))


def radial_valid_vector(z, chi, B):
    total = pl_integral(z, B, z[0], z[-1])
    if not math.isfinite(total) or total <= 0:
        raise AssertionError("nonpositive radial total")
    cz0 = float(np.interp(ZMIN, z, chi)); cz1 = float(np.interp(ZMAX, z, chi))
    vals = np.zeros(12288, dtype=np.float64)
    for ell in range(12288):
        req = (ell + 0.5) / KMAX
        if req <= cz0:
            lo = ZMIN
        elif req > cz1:
            continue
        else:
            zk = inverse_chi(z, chi, req)
            if zk is None: continue
            lo = max(ZMIN, zk)
        vals[ell] = pl_integral(z, B, lo, ZMAX)
    return total, vals


def classify_mass(window, radial_total, valid_by_ell):
    a = np.abs(np.asarray(window, dtype=np.float64))
    if a.shape != (12288,) or np.any(~np.isfinite(a)):
        raise AssertionError("bad angular row")
    asum = math.fsum(float(x) for x in a)
    D = asum * float(radial_total)
    terms = (float(a[i]) * float(valid_by_ell[i]) for i in range(12288))
    N = math.fsum(terms)
    if not (math.isfinite(D) and D > 0 and math.isfinite(N)):
        raise AssertionError("bad positive masses")
    if N < -1e-12*D or N > (1+1e-12)*D:
        raise AssertionError("valid mass outside total mass")
    N = min(D, max(0.0, N))
    c1 = (D - N) <= THRESH * D
    c2 = N >= (1.0 - THRESH) * D
    state = "retained" if c1 and c2 else "rejected" if (not c1 and not c2) else UNRES
    return {
        "D": D, "N": N, "f_invalid": (D-N)/D,
        "mass_check_invalid": bool(c1), "mass_check_valid": bool(c2),
        "state": state, "retained": state == "retained",
    }


def import_expz2(path: Path):
    spec = importlib.util.spec_from_file_location("exp073z2_frozen", path)
    if spec is None or spec.loader is None: raise AssertionError("cannot import frozen Exp073Z2")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def reconstruct_radials(mod, source, lens, camb_root, manifest):
    if mod.git_head(Path(camb_root)) != mod.CAMB_PIN:
        raise AssertionError("CAMB pin mismatch")
    zs, src, _ = mod.load(Path(source), 1, 4, mod.SOURCE_BYTES, mod.SOURCE_SHA, mod.SOURCE_BIN_SHA)
    zl, lns, _ = mod.load(Path(lens), 7, 5, mod.LENS_BYTES, mod.LENS_SHA, mod.LENS_BIN_SHA)
    if not np.array_equal(zs, zl): raise AssertionError("source/lens z mismatch")
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.0,ombh2=0.0224,omch2=0.1200,mnu=0.0,nnu=3.046,TCMB=2.7255,YHe=0.24,tau=0.0)
    pars.set_dark_energy(w=-1.0,wa=0.0)
    bg = camb.get_background(pars)
    chi_raw = np.asarray(bg.comoving_radial_distance(zs), dtype=np.float64)
    out = {}
    for name, step in (("coarse",0.005),("fine",0.0025)):
        z = mod.grid(step, zs)
        chi,H,g,wm,ww,*_ = mod.kernels(z,zs,src,lns,bg,chi_raw)
        out[name] = {"z":z,"chi":chi,"wm":wm,"ww":ww}
    fs = manifest["radial"]["arrays"]
    fine = out["fine"]
    for key, arr in (("z_fine",fine["z"]),("chi_Mpc",fine["chi"]),("Wm_radial",fine["wm"]),("WW_radial",fine["ww"])):
        if ah(arr, fs[key]["dtype"]) != fs[key]:
            raise AssertionError(f"fresh fine radial mismatch {key}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--inputs", required=True)
    ap.add_argument("--expim-result-root", required=True)
    ap.add_argument("--boss-root", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--lens", required=True)
    ap.add_argument("--camb-root", required=True)
    ap.add_argument("--expz2-script", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(); outp = Path(a.out)
    try:
        manifest = json.loads(Path(a.manifest).read_text())
        assert manifest["schema"] == "EXP073IM_C2_REAL_INPUT_MANIFEST_V0_4"
        expim = load_one_json(Path(a.expim_result_root), lambda x: x.get("status") == EXPIM_PASS)
        assert expim["scientific_radial_pass"] is True and len(expim["rows"]) == 1170
        assert expim["physical_support_evaluated"] is False
        des_rows = sorted(expim["rows"], key=lambda r:r["ordinal"])
        assert [r["ordinal"] for r in des_rows] == list(range(1170))

        angular = {}
        for s in manifest["angular"]:
            angular[s["slot"]] = find_angular(Path(a.inputs)/s["slot"], s)
        assert len(angular) == 14

        mod = import_expz2(Path(a.expz2_script))
        rad = reconstruct_radials(mod, a.source, a.lens, a.camb_root, manifest)
        precalc = {}
        for gridname in ("coarse","fine"):
            rr = rad[gridname]; precalc[gridname] = {"Wm":[],"WW":[]}
            for B in rr["wm"]:
                precalc[gridname]["Wm"].append(radial_valid_vector(rr["z"],rr["chi"],B))
            for B in rr["ww"]:
                precalc[gridname]["WW"].append(radial_valid_vector(rr["z"],rr["chi"],B))

        des_out=[]; changed=0; maxdelta=0.0; unresolved=[]
        for r in des_rows:
            block=r["block"]; ri=int(r["radial_index"]); band=int(r["band_index"])
            w=angular[r["slot"]][band]
            c=classify_mass(w,*precalc["coarse"][block][ri])
            f=classify_mass(w,*precalc["fine"][block][ri])
            delta=abs(c["f_invalid"]-f["f_invalid"]); maxdelta=max(maxdelta,delta)
            if c["retained"] != f["retained"] or c["state"] != f["state"]: changed += 1
            if c["state"]==UNRES or f["state"]==UNRES: unresolved.append(r["coordinate_id"])
            des_out.append({
                "coordinate_id":r["coordinate_id"],"ordinal":r["ordinal"],"block":block,"slot":r["slot"],"band_index":band,
                "f_invalid_coarse":c["f_invalid"],"f_invalid_fine":f["f_invalid"],"delta":delta,
                "D_fine":f["D"],"N_fine":f["N"],"mass_check_invalid":f["mass_check_invalid"],"mass_check_valid":f["mass_check_valid"],
                "state":f["state"],"retained":f["retained"],
            })
        if unresolved: raise AssertionError(f"numerically unresolved rows: {unresolved[:5]}")
        if changed != 0 or maxdelta > CONV:
            raise AssertionError(f"DES coarse/fine convergence failed changed={changed} maxdelta={maxdelta}")

        bossj = load_one_json(Path(a.boss_root), lambda x:x.get("classification")=="PASS_EXP073W_BOSS_LOWER_K_COMPATIBILITY_V0_1")
        assert bossj["candidate_count"] == 240 and bossj["radial_support"]["entire_selection_inside_article3_domain"] is True
        bossnpz = next(Path(a.boss_root).rglob("*.npz"))
        with np.load(bossnpz, allow_pickle=False) as z:
            ords=canonical(z["ordinal"],"<i8"); mask=canonical(z["current_retained_mask"],"|u1"); bf=canonical(z["current_f_invalid"],"<f8")
        if sha_bytes(mask.tobytes()) != BOSS_MASK_SHA or sha_bytes(bf.tobytes()) != BOSS_F_SHA:
            raise AssertionError("BOSS logical authority mismatch")
        if list(ords) != list(range(1170,1410)) or int(mask.sum()) != 54:
            raise AssertionError("BOSS order/retained count mismatch")
        boss_ids=bossj["ordered_coordinate_ids"]
        assert len(boss_ids)==240
        boss_out=[{"coordinate_id":boss_ids[i],"ordinal":int(ords[i]),"block":"BOSS","f_invalid":float(bf[i]),"retained":bool(mask[i])} for i in range(240)]

        all_ids=[r["coordinate_id"] for r in des_out]+boss_ids
        if len(set(all_ids))!=1410 or sha_lines(all_ids)!=FULL_ORDER_SHA:
            raise AssertionError("full 1410 order authority mismatch")
        retained_ids=[r["coordinate_id"] for r in des_out if r["retained"]]+[boss_ids[i] for i in range(240) if mask[i]]
        des_ret=sum(r["retained"] for r in des_out); total_ret=len(retained_ids)
        status=PASS if total_ret>=15 else FAIL
        result={
            "experiment":"Exp073IQ","schema":"EXP073IQ_ARTICLE3_REAL_LAYERA_SUPPORT_RESULT_V0_1","status":status,
            "parent_exp073im":{"run":34419165956,"job":102690618922,"artifact":10130241439,"status":EXPIM_PASS},
            "candidate_count":1410,"des_candidate_count":1170,"boss_candidate_count":240,
            "des_retained_count":int(des_ret),"boss_retained_count":54,"combined_retained_count":total_ret,
            "des_coarse_fine":{"changed_label_count":changed,"max_abs_delta_f_invalid":maxdelta,"tolerance":CONV,"pass":changed==0 and maxdelta<=CONV},
            "retained_id_sha256":sha_lines(retained_ids),"full_order_sha256":sha_lines(all_ids),
            "frozen_domain":{"z_min":ZMIN,"z_max":ZMAX,"k_positive":True,"k_max_Mpc^-1":KMAX,"threshold":THRESH,"minimum_retained":15},
            "covariance_read":False,"whitening_read":False,"nuisance_read":False,"relation_null_read":False,"G8_read":False,"selection_reads":[],
            "layer_b_evaluated":False,"covariance_restriction_authorized":False,
            "des_rows":des_out,"boss_rows":boss_out,"retained_coordinate_ids":retained_ids,
        }
        outp.parent.mkdir(parents=True,exist_ok=True); outp.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
        print(status, "DES",des_ret,"BOSS",54,"TOTAL",total_ret,"maxdelta",maxdelta)
        return 0
    except Exception as e:
        outp.parent.mkdir(parents=True,exist_ok=True); outp.write_text(json.dumps({"experiment":"Exp073IQ","status":INVALID,"error":f"{type(e).__name__}: {e}","covariance_read":False,"downstream_reads":[]},indent=2)+"\n")
        print(INVALID,repr(e)); return 2

if __name__ == "__main__":
    raise SystemExit(main())
