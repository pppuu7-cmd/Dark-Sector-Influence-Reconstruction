#!/usr/bin/env python3
"""Exp055A retrospective endpoint-normalized half-transition candidate.

Uses only immutable C3/C5/C7 artifacts. This is deliberately NOT a G7/G8
prospective gate because the operator was motivated after C7 was unblinded.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], float)
Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], float)
LOGK = np.log(K)


def readj(path: Path):
    return json.loads(path.read_text())


def unique(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise ValueError(f"expected exactly one {name} under {root}, got {hits}")
    return hits[0]


def half_crossing(row):
    r = np.asarray(row, float)
    if r.shape != (5,) or not np.all(np.isfinite(r)):
        raise ValueError(f"invalid response row: {r}")
    den = float(r[-1] - r[0])
    if not math.isfinite(den) or den == 0.0:
        raise ValueError("endpoint contrast is zero/non-finite")
    u = (r - r[0]) / den
    y = u - 0.5
    crossings = []
    for i in range(4):
        if y[i] == 0.0:
            crossings.append(float(K[i]))
        if y[i] * y[i + 1] < 0.0:
            f = float((0.5 - u[i]) / (u[i + 1] - u[i]))
            crossings.append(float(math.exp(LOGK[i] + f * (LOGK[i + 1] - LOGK[i]))))
        elif y[i + 1] == 0.0 and i == 3:
            crossings.append(float(K[i + 1]))
    if len(crossings) != 1:
        raise ValueError(f"expected one u=1/2 crossing, found {crossings}; u={u.tolist()}")
    return crossings[0], u


def summarize_model(amplitude, k_source, matrix):
    r = np.asarray(matrix, float)
    if r.shape != (7, 5) or not np.all(np.isfinite(r)):
        raise ValueError(f"bad matrix shape/values: {r.shape}")
    crossings = []
    nonmonotone_rows = 0
    endpoint_contrasts = []
    for row in r:
        k50, u = half_crossing(row)
        crossings.append(k50)
        endpoint_contrasts.append(float(row[-1] - row[0]))
        du = np.diff(u)
        if not (np.all(du >= 0.0) or np.all(du <= 0.0)):
            nonmonotone_rows += 1
    crossings = np.asarray(crossings, float)
    return {
        "amplitude": float(amplitude),
        "k_source_h_mpc": float(k_source),
        "k50_by_z_h_mpc": crossings.tolist(),
        "k50_geo_h_mpc": float(np.exp(np.mean(np.log(crossings)))),
        "k50_min_h_mpc": float(crossings.min()),
        "k50_max_h_mpc": float(crossings.max()),
        "max_over_min_k50": float(crossings.max() / crossings.min()),
        "nonmonotone_rows": int(nonmonotone_rows),
        "endpoint_contrast_min": float(np.min(endpoint_contrasts)),
        "endpoint_contrast_max": float(np.max(endpoint_contrasts)),
    }


def adjacent_slopes(rows, keep_z=None):
    ksrc = []
    kres = []
    for row in rows:
        kk = np.asarray(row["k50_by_z_h_mpc"], float)
        if keep_z is not None:
            kk = kk[np.asarray(keep_z, int)]
        ksrc.append(float(row["k_source_h_mpc"]))
        kres.append(float(np.exp(np.mean(np.log(kk)))))
    ksrc = np.asarray(ksrc, float)
    kres = np.asarray(kres, float)
    return np.diff(np.log(kres)) / np.diff(np.log(ksrc))


def load_gdm(root: Path):
    scan = readj(unique(root, "exp049b_gdm_cv2_intermediate_scan.json"))
    gate = readj(unique(root, "gdm_window_crossing_validation_v0_1.json"))
    source = {float(x["cv2"]): float(x["k_v_QS_at_zref_h_mpc"]) for x in gate["rows"]}
    if not np.allclose(np.asarray(scan["core_k_h_mpc"], float), K, rtol=0, atol=1e-14):
        raise ValueError("GDM frozen k mismatch")
    if not np.allclose(np.asarray(scan["z_nodes"], float), Z, rtol=0, atol=1e-10):
        raise ValueError("GDM frozen z mismatch")
    rows = []
    for m in sorted(scan["models"], key=lambda x: float(x["cv2"])):
        amp = float(m["cv2"])
        files = sorted(m["files"], key=lambda x: float(x["z"]))
        z = np.asarray([float(x["z"]) for x in files], float)
        if not np.allclose(z, Z, rtol=0, atol=1e-10):
            raise ValueError(f"GDM per-model z mismatch at {amp}: {z}")
        mat = np.asarray([x["r_core"] for x in files], float)
        rows.append(summarize_model(amp, source[amp], mat))
    return rows


def load_fr(root: Path):
    gate = readj(unique(root, "fr_window_crossing_validation_v0_1.json"))
    source = {
        float(x["B0"]): float(x["k_compton_frozen_z_min_h_mpc"])
        for x in gate["models"]
    }
    payload = {}
    for p in root.rglob("exp049c_B0_*.json"):
        j = readj(p)
        b = float(j["B0"])
        if b > 0:
            payload[b] = j
    if set(payload) != set(source):
        raise ValueError(f"fR payload/source mismatch {sorted(payload)} vs {sorted(source)}")
    rows = []
    for amp in sorted(source):
        j = payload[amp]
        if not np.allclose(np.asarray(j["k_h_mpc"], float), K, rtol=0, atol=1e-14):
            raise ValueError(f"fR frozen k mismatch B0={amp}")
        if not np.allclose(np.asarray(j["z_nodes"], float), Z, rtol=0, atol=1e-10):
            raise ValueError(f"fR frozen z mismatch B0={amp}")
        rows.append(summarize_model(amp, source[amp], np.asarray(j["r_Delta"], float)))
    return rows


def load_c7(root: Path):
    j = readj(unique(root, "idm_dr_common_source_response_slope_v0_1.json"))
    if not np.allclose(np.asarray(j["frozen_k_h_mpc"], float), K, rtol=0, atol=1e-14):
        raise ValueError("C7 frozen k mismatch")
    if not np.allclose(np.asarray(j["frozen_redshifts"], float), Z, rtol=0, atol=1e-10):
        raise ValueError("C7 frozen z mismatch")
    if j["status"] != "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1":
        raise ValueError("Exp055A requires the immutable failed Exp054C science result")
    rows = []
    for m in j["models"]:
        rows.append(
            summarize_model(
                float(m["a_idm_dr_per_mpc"]),
                float(m["k_source_h_mpc"]),
                np.asarray(m["response_matrix_z_by_k"], float),
            )
        )
    return rows


def family_result(name, rows):
    slopes = adjacent_slopes(rows)
    loo = []
    for drop in range(7):
        keep = [i for i in range(7) if i != drop]
        s = adjacent_slopes(rows, keep_z=keep)
        loo.append({
            "dropped_z": float(Z[drop]),
            "C50_adjacent": s.tolist(),
            "all_positive": bool(np.all(np.isfinite(s)) and np.all(s > 0.0)),
        })
    return {
        "family": name,
        "rows": rows,
        "C50_adjacent": slopes.tolist(),
        "all_C50_positive": bool(np.all(np.isfinite(slopes)) and np.all(slopes > 0.0)),
        "min_C50": float(np.min(slopes)),
        "max_C50": float(np.max(slopes)),
        "leave_one_z": loo,
        "all_leave_one_z_positive": bool(all(x["all_positive"] for x in loo)),
        "total_nonmonotone_rows": int(sum(x["nonmonotone_rows"] for x in rows)),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gdm-root", required=True)
    ap.add_argument("--fr-root", required=True)
    ap.add_argument("--c7-root", required=True)
    ap.add_argument("--json", required=True)
    a = ap.parse_args()

    families = [
        family_result("C3_GDM_dynamic_shear", load_gdm(Path(a.gdm_root))),
        family_result("C5_designer_fR", load_fr(Path(a.fr_root))),
        family_result("C7_IDM_DR", load_c7(Path(a.c7_root))),
    ]

    all_rows = sum(len(f["rows"]) * 7 for f in families)
    all_positive = all(f["all_C50_positive"] for f in families)
    loo_positive = all(f["all_leave_one_z_positive"] for f in families)
    unique_ok = all_rows == 105  # every row reaching this point had one unique crossing
    qualified = bool(all_positive and loo_positive and unique_ok)

    out = {
        "schema": "dsir.endpoint_half_transition_retrospective.v0.1",
        "status": (
            "RETROSPECTIVE_COMMON_HALF_TRANSITION_CANDIDATE_POSITIVE_V0_1"
            if qualified else
            "RETROSPECTIVE_COMMON_HALF_TRANSITION_CANDIDATE_REJECTED_V0_1"
        ),
        "operator": {
            "u": "(R(k)-R(k_min))/(R(k_max)-R(k_min)) at each z",
            "crossing": "unique u=0.5 crossing, piecewise linear in ln(k)",
            "compression": "k50_geo=exp(mean_z ln(k50(z)))",
            "relation": "C50=Delta ln(k50_geo)/Delta ln(k_source) > 0",
            "k_h_mpc": K.tolist(),
            "z": Z.tolist(),
        },
        "families": families,
        "row_crossings_verified": int(all_rows),
        "expected_row_crossings": 105,
        "all_adjacent_C50_positive": bool(all_positive),
        "all_leave_one_z_adjacent_C50_positive": bool(loo_positive),
        "candidate_qualified_for_future_preregistration": qualified,
        "provenance": {
            "C3": {"run_id":32904158849,"artifact_id":9584180621,"sha256":"892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a"},
            "C5": {"run_id":32907619613,"artifact_id":9585579947,"sha256":"bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942"},
            "C7": {"run_id":32920776596,"artifact_id":9589768992,"sha256":"fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a"},
        },
        "interpretation_boundary": [
            "retrospective candidate search after C7 unblinding",
            "C7 is not withheld evidence for this operator",
            "does not rescue Exp054C/F27",
            "does not close G7 or G8",
            "no common slope-magnitude band is claimed",
            "future confirmation requires a genuinely fresh mechanism/family",
        ],
    }
    text = json.dumps(out, indent=2) + "\n"
    Path(a.json).write_text(text)
    print(text)


if __name__ == "__main__":
    main()
