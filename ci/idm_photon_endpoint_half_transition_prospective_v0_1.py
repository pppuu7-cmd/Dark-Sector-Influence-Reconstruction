#!/usr/bin/env python3
"""Exp056B: prospective C8 IDM-photon endpoint half-transition gate.

The complete scientific contract was committed at
84d05ad72af1aea4fe3beadf071ee20cadf93c19 before the first C8 P(k,z).
No C8 response may be used to alter this evaluator's scientific choices.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import re
from pathlib import Path

import numpy as np

Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], float)
K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], float)
LOGK = np.log(K)
SOURCE_K = np.array([
    0.08484582985947185,
    0.07347864406347489,
    0.05999506164903260,
    0.04647197492427811,
    0.03927598733289058,
], float)
FROZEN_U = np.array([
    1.9784961959913951e-13,
    2.7180740724473660e-13,
    4.2866377403625277e-13,
    7.7340788471244140e-13,
    1.1546648138593298e-12,
], float)
EXPECTED = ["idm1_", "idm2_", "idm3_", "idm4_", "idm5_"]


def header_redshift(path: str) -> float:
    with open(path) as f:
        for _ in range(16):
            line = f.readline()
            m = re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)", line, re.I)
            if m:
                return float(m.group(1))
    raise ValueError(f"could not recover redshift header: {path}")


def load_pk(path: str):
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[1] < 2:
        raise ValueError(f"bad P(k) table {path}: {a.shape}")
    k = np.asarray(a[:, 0], float)
    p = np.asarray(a[:, 1], float)
    mask = np.isfinite(k) & np.isfinite(p) & (k > 0) & (p > 0)
    k, p = k[mask], p[mask]
    order = np.argsort(k)
    k, p = k[order], p[order]
    if k.size < 25 or np.any(np.diff(k) <= 0):
        raise ValueError(f"insufficient/non-monotone k grid: {path}")
    if k.min() > K.min() or k.max() < K.max():
        raise ValueError(f"frozen low-k nodes not covered: {path}")
    return k, p


def by_z(directory: Path, prefix: str):
    hits = sorted(glob.glob(str(directory / (prefix + "*pk.dat"))))
    if len(hits) != 7:
        raise ValueError(f"expected seven pk files for {prefix}, found {len(hits)}")
    out = {header_redshift(p): p for p in hits}
    zs = np.asarray(sorted(out), float)
    if len(out) != 7 or not np.allclose(zs, Z, rtol=0, atol=1e-10):
        raise ValueError(f"wrong frozen redshift set for {prefix}: {zs}")
    return out


def nearest(mapping, z):
    key = min(mapping, key=lambda x: abs(x-z))
    if abs(key-z) > 1e-10:
        raise ValueError(f"missing frozen z={z}; nearest={key}")
    return key


def logp_nodes(path: str):
    k, p = load_pk(path)
    return np.interp(LOGK, np.log(k), np.log(p))


def response_matrix(refs, model):
    rows=[]
    for z in Z:
        zr=nearest(refs,float(z)); zm=nearest(model,float(z))
        r=logp_nodes(model[zm])-logp_nodes(refs[zr])
        if np.any(~np.isfinite(r)):
            raise ValueError(f"non-finite response z={z}")
        rows.append(r)
    return np.asarray(rows,float)


def half_crossing(row):
    r=np.asarray(row,float)
    if r.shape != (5,) or not np.all(np.isfinite(r)):
        raise ValueError("invalid response row")
    den=float(r[-1]-r[0])
    if not math.isfinite(den) or den == 0.0:
        raise ValueError("endpoint contrast zero/non-finite")
    u=(r-r[0])/den
    y=u-0.5
    crossings=[]
    for i in range(4):
        if y[i] == 0.0:
            crossings.append(float(K[i]))
        if y[i]*y[i+1] < 0.0:
            f=float((0.5-u[i])/(u[i+1]-u[i]))
            crossings.append(float(math.exp(LOGK[i]+f*(LOGK[i+1]-LOGK[i]))))
        elif y[i+1] == 0.0 and i == 3:
            crossings.append(float(K[i+1]))
    if len(crossings) != 1:
        raise ValueError(f"expected one u=1/2 crossing, found {crossings}; u={u.tolist()}")
    du=np.diff(u)
    nonmono=not (np.all(du>=0.0) or np.all(du<=0.0))
    return crossings[0], u, den, bool(nonmono)


def slopes(k50_by_model, keep=None):
    kres=[]
    for vals in k50_by_model:
        x=np.asarray(vals,float)
        if keep is not None:
            x=x[np.asarray(keep,int)]
        kres.append(float(np.exp(np.mean(np.log(x)))))
    return np.diff(np.log(np.asarray(kres,float)))/np.diff(np.log(SOURCE_K)), kres


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--directory", required=True)
    ap.add_argument("--reference-prefix", default="ref_")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--json", required=True)
    a=ap.parse_args()

    failures=[]
    models=[]
    k50_all=[]
    try:
        if a.models != EXPECTED:
            raise ValueError(f"model order frozen as {EXPECTED}, got {a.models}")
        if not np.all(np.diff(SOURCE_K)<0):
            raise RuntimeError("source ordering corrupted")
        if not np.all(np.diff(FROZEN_U)>0):
            raise RuntimeError("coupling ordering corrupted")
        root=Path(a.directory)
        refs=by_z(root,a.reference_prefix)
        for idx,prefix in enumerate(a.models):
            r=response_matrix(refs,by_z(root,prefix))
            ks=[]; endpoint=[]; nonmono=0
            row_records=[]
            for zi,row in enumerate(r):
                try:
                    k50,u,den,nm=half_crossing(row)
                    ks.append(k50); endpoint.append(den); nonmono += int(nm)
                    row_records.append({"z":float(Z[zi]),"k50_h_mpc":k50,"endpoint_contrast":den,"u":u.tolist(),"nonmonotone":nm})
                except Exception as e:
                    failures.append(f"model_{idx+1}_z_{Z[zi]}:{e}")
                    ks.append(float("nan")); endpoint.append(float("nan"))
                    row_records.append({"z":float(Z[zi]),"error":str(e)})
            k50_all.append(ks)
            finite=np.all(np.isfinite(ks))
            kgeo=float(np.exp(np.mean(np.log(ks)))) if finite else None
            models.append({
                "index":idx+1,"prefix":prefix,
                "u_idm_g":float(FROZEN_U[idx]),
                "k_source_h_mpc":float(SOURCE_K[idx]),
                "k50_by_z_h_mpc":[float(x) if math.isfinite(x) else None for x in ks],
                "k50_geo_h_mpc":kgeo,
                "nonmonotone_rows":nonmono,
                "response_matrix_z_by_k":r.tolist(),
                "rows":row_records,
            })
    except Exception as e:
        failures.append(f"hard_input_or_response_error:{e}")

    adjacent=[]; loo=[]; kgeo=[]
    if len(k50_all)==5 and all(np.all(np.isfinite(x)) for x in k50_all):
        c,kgeo=slopes(k50_all)
        for i,x in enumerate(c):
            ok=bool(np.isfinite(x) and x>0.0)
            adjacent.append({"pair":[i+1,i+2],"C50":float(x) if np.isfinite(x) else None,"positive":ok})
            if not ok: failures.append(f"nonpositive_C50_pair_{i+1}_{i+2}")
        for drop in range(7):
            keep=[i for i in range(7) if i!=drop]
            cc,kg=slopes(k50_all,keep)
            ok=bool(np.all(np.isfinite(cc)) and np.all(cc>0.0))
            loo.append({"dropped_z":float(Z[drop]),"C50_adjacent":cc.tolist(),"k50_geo_h_mpc":kg,"all_positive":ok})
            if not ok: failures.append(f"leave_one_z_nonpositive_drop_{Z[drop]}")
    elif not failures:
        failures.append("incomplete_valid_k50_grid")

    status=("PASS_IDM_PHOTON_ENDPOINT_HALF_TRANSITION_PROSPECTIVE_V0_1" if not failures else "FAIL_IDM_PHOTON_ENDPOINT_HALF_TRANSITION_PROSPECTIVE_V0_1")
    out={
        "schema":"dsir.idm_photon_endpoint_half_transition_prospective.v0.1",
        "date":"2026-08-26",
        "status":status,
        "failures":failures,
        "preregistered_contract":"experiments/056b_idm_photon_endpoint_half_transition_prospective_v0_1.md",
        "preregistered_contract_commit":"84d05ad72af1aea4fe3beadf071ee20cadf93c19",
        "pinned_CLASS":"lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540",
        "frozen_redshifts":Z.tolist(),"frozen_k_h_mpc":K.tolist(),
        "frozen_k_source_h_mpc":SOURCE_K.tolist(),"frozen_u_idm_g":FROZEN_U.tolist(),
        "operator":"u=(R-R(kmin))/(R(kmax)-R(kmin)); unique u=0.5 crossing linear in ln k; k50_geo=exp(mean_z ln k50); C50=Delta ln k50_geo/Delta ln k_source",
        "gate":"all four C50>0 and all 28 leave-one-redshift C50>0; no magnitude band",
        "models":models,"k50_geo_h_mpc":kgeo,"adjacent_tests":adjacent,"leave_one_z":loo,
        "no_recalibration_after_output":True,
        "not_a_claim":["not a universal numerical slope coefficient","not intrinsic rank or field count","not observation-space detectability","not a fundamental action reconstruction"],
    }
    text=json.dumps(out,indent=2,allow_nan=False)+"\n"
    Path(a.json).write_text(text); print(text)
    raise SystemExit(0 if not failures else 2)

if __name__ == "__main__":
    main()
