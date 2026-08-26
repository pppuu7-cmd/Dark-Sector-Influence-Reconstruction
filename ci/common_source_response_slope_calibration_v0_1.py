#!/usr/bin/env python3
"""Exp054A: calibrate one full-response source/localization slope on immutable C3/C5 products."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

FROZEN_K=np.array([0.001,0.003,0.01,0.03,0.1],float)
FROZEN_Z=np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)


def unique(root: Path,name: str)->Path:
    hits=list(root.rglob(name))
    if len(hits)!=1:
        raise ValueError(f"expected one {name} under {root}, got {hits}")
    return hits[0]


def readj(p: Path):
    return json.loads(p.read_text())


def centroid(matrix,k=FROZEN_K,z=FROZEN_Z):
    r=np.asarray(matrix,float)
    if r.shape!=(len(z),len(k)) or not np.all(np.isfinite(r)):
        raise ValueError(f"bad response matrix shape/values: {r.shape}")
    e=r*r; total=float(e.sum())
    if not np.isfinite(total) or total<=0:
        raise ValueError("non-positive response power")
    qk=e.sum(axis=0)/total; qz=e.sum(axis=1)/total
    kres=float(np.exp(np.dot(qk,np.log(k))))
    zres=float(np.dot(qz,z))
    return {"k_R_geo_h_mpc":kres,"z_R":zres,"response_power":total,
            "q_k":qk.tolist(),"q_z":qz.tolist(),
            "q_k_norm_residual":float(abs(qk.sum()-1)),"q_z_norm_residual":float(abs(qz.sum()-1))}


def slopes(rows):
    out=[]
    for a,b in zip(rows[:-1],rows[1:]):
        dsrc=float(np.log(b["k_source_h_mpc"]/a["k_source_h_mpc"]))
        dresp=float(np.log(b["k_R_geo_h_mpc"]/a["k_R_geo_h_mpc"]))
        c=dresp/dsrc if dsrc!=0 else np.nan
        out.append({"from_amplitude":a["amplitude"],"to_amplitude":b["amplitude"],
                    "delta_ln_k_source":dsrc,"delta_ln_k_R":dresp,"C":float(c)})
    return out


def gdm(root: Path):
    scan=readj(unique(root,"exp049b_gdm_cv2_intermediate_scan.json"))
    gate=readj(unique(root,"gdm_window_crossing_validation_v0_1.json"))
    source={float(x["cv2"]):float(x["k_v_QS_at_zref_h_mpc"]) for x in gate["rows"]}
    rows=[]
    for m in sorted(scan["models"],key=lambda x:float(x["cv2"])):
        amp=float(m["cv2"])
        files=sorted(m["files"],key=lambda x:float(x["z"]))
        zs=np.array([float(x["z"]) for x in files])
        if not np.allclose(zs,FROZEN_Z,rtol=0,atol=1e-10):
            raise ValueError(f"GDM z mismatch {zs}")
        mat=np.array([x["r_core"] for x in files],float)
        c=centroid(mat)
        rows.append({"amplitude":amp,"k_source_h_mpc":source[amp],**c})
    return rows


def fr(root: Path):
    gate=readj(unique(root,"fr_window_crossing_validation_v0_1.json"))
    # Raw Exp049C gate schema stores the source statistic under the explicit
    # frozen-z minimum key. This is the same quantity later renamed to the
    # shorter k_compton_min_h_mpc in the immutable repository summary.
    source={float(x["B0"]):float(x["k_compton_frozen_z_min_h_mpc"]) for x in gate["models"]}
    payload={}
    for p in root.rglob("exp049c_B0_*.json"):
        j=readj(p); b=float(j["B0"])
        if b>0: payload[b]=j
    if set(payload)!=set(source):
        raise ValueError(f"fR B0 payload/source mismatch payload={sorted(payload)} source={sorted(source)}")
    rows=[]
    for amp in sorted(source):
        j=payload[amp]
        if not np.allclose(np.asarray(j["k_h_mpc"],float),FROZEN_K,rtol=0,atol=1e-14):
            raise ValueError(f"fR k mismatch B0={amp}")
        if not np.allclose(np.asarray(j["z_nodes"],float),FROZEN_Z,rtol=0,atol=1e-10):
            raise ValueError(f"fR z mismatch B0={amp}")
        c=centroid(j["r_Delta"])
        rows.append({"amplitude":amp,"k_source_h_mpc":source[amp],**c})
    return rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gdm-root',required=True)
    ap.add_argument('--fr-root',required=True)
    ap.add_argument('--json',required=True)
    a=ap.parse_args()
    families={"C3_GDM_dynamic_shear":gdm(Path(a.gdm_root)),
              "C5_designer_fR":fr(Path(a.fr_root))}
    allsl=[]; famout={}
    for name,rows in families.items():
        ss=slopes(rows); allsl.extend([x["C"] for x in ss])
        famout[name]={"rows":rows,"adjacent_slopes":ss}
    arr=np.asarray(allsl,float)
    finite=bool(np.all(np.isfinite(arr)))
    positive=bool(finite and np.all(arr>0))
    max_qres=max(max(r["q_k_norm_residual"] for r in rows) for rows in families.values())
    out={
      "schema":"dsir.common_source_response_slope_calibration.v0.1",
      "definition":"C = Delta ln(k_R_geo) / Delta ln(k_source), with k_R_geo from full R^2",
      "frozen_branching_rule":"reject before C7 if any C3/C5 adjacent C<=0; otherwise prospective C7 band=[0.5*min(C),2*max(C)]",
      "families":famout,
      "all_C":arr.tolist(),
      "all_finite":finite,
      "all_positive":positive,
      "max_profile_normalization_residual":float(max_qres),
      "prospective_C7_band":([float(0.5*arr.min()),float(2.0*arr.max())] if positive else None),
      "status":("CALIBRATION_COMMON_SLOPE_POSITIVE" if positive else "CALIBRATION_COMMON_SLOPE_REJECTED"),
      "not_a_claim":["retrospective calibration cannot close G7/G8","band is not refit after C7","no universal rank or fundamental parameter count"]
    }
    Path(a.json).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
    if max_qres>1e-12:
        raise SystemExit("profile normalization control failed")
    # A rejected common relation is a valid scientific outcome, not CI failure.

if __name__=='__main__': main()
