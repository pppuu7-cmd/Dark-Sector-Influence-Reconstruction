#!/usr/bin/env python3
"""Experiment 023: thermal-WDM visibility across DSIR scale blocks.

This is a response-domain diagnostic using the already frozen Viel-type thermal
WDM transfer control. It does not fit WDM parameters or claim new physics.
"""
from __future__ import annotations

import json
import numpy as np

from dsir.linear_controls import thermal_wdm_alpha, thermal_wdm_transfer

CORE = np.array([0.001, 0.003, 0.01, 0.03, 0.1])
EXTENSION = np.array([0.2, 0.5, 1.0])
SMALL_SCALE = np.array([2.0, 5.0, 10.0, 20.0])
MASSES = [2.0, 3.0, 5.0]


def log_power_response(k, mass):
    t = thermal_wdm_transfer(k, m_keV=mass)
    return 2.0 * np.log(t)


def main():
    rows=[]
    for mass in MASSES:
        rc=log_power_response(CORE,mass)
        re=log_power_response(EXTENSION,mass)
        rs=log_power_response(SMALL_SCALE,mass)
        rows.append({
            "m_keV": mass,
            "alpha_hinv_mpc": float(thermal_wdm_alpha(mass)),
            "r_core": rc.tolist(),
            "max_abs_r_core": float(np.max(np.abs(rc))),
            "r_extension": re.tolist(),
            "max_abs_r_extension": float(np.max(np.abs(re))),
            "r_small_scale": rs.tolist(),
            "max_abs_r_small_scale": float(np.max(np.abs(rs))),
            "abs_r_at_k10": float(abs(rs[2])),
            "small_to_core_visibility_ratio": float(np.max(np.abs(rs))/np.max(np.abs(rc))),
        })
    out={
        "status":"PASS_DIAGNOSTIC",
        "interpretation":"thermal WDM is nearly null on the first k<=0.1 cosmological core and requires a separate high-k/small-scale discriminant block",
        "core_k_h_mpc":CORE.tolist(),
        "extension_k_h_mpc":EXTENSION.tolist(),
        "small_scale_k_h_mpc":SMALL_SCALE.tolist(),
        "models":rows,
    }
    print(json.dumps(out,indent=2))

    # Regression bounds are deliberately broad and encode only the qualitative
    # visibility separation, not observational WDM constraints.
    for r in rows:
        assert r["max_abs_r_core"] < 2e-5
        assert r["max_abs_r_small_scale"] > 0.1 if r["m_keV"] <= 3 else r["max_abs_r_small_scale"] > 0.03


if __name__ == "__main__":
    main()
