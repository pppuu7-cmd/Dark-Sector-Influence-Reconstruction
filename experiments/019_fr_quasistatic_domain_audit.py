#!/usr/bin/env python3
"""Experiment 019: horizon-scale audit of the BZ-like f(R) control.

The existing f(R) control solves a sub-horizon/quasi-static growth equation.
This experiment measures k/(aH/c) over the frozen DSIR redshift/k nodes and
prevents low-k extrapolation from entering a production six-family matrix.
The threshold labels below are DSIR engineering categories, not fundamental
boundaries of modified-gravity theory.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
Z = np.asarray([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33])
K = np.asarray([0.001, 0.003, 0.01, 0.03, 0.1])  # h/Mpc
C_KMS = 299792.458
OMEGA_M = 0.3


def main() -> None:
    a = 1.0 / (1.0 + Z)
    E = np.sqrt(OMEGA_M * a**-3 + 1.0 - OMEGA_M)
    # H=100 h E km/s/Mpc. Divide aH by c and express in h/Mpc;
    # the explicit h cancels, leaving 100*a*E/c.
    aH_over_c_hmpc = 100.0 * a * E / C_KMS
    ratio = K[:, None] / aH_over_c_hmpc[None, :]

    min_ratio = ratio.min(axis=1)
    # Descriptive categories only. "clearly_subhorizon" is a conservative
    # DSIR bookkeeping choice for the toy QS control, not a theorem.
    categories = []
    for r in min_ratio:
        if r < 5:
            categories.append("not_deep_subhorizon")
        elif r < 20:
            categories.append("borderline_for_qs_control")
        else:
            categories.append("clearly_subhorizon_for_provisional_qs_control")

    result = {
        "z_nodes": Z.tolist(),
        "k_nodes_h_mpc": K.tolist(),
        "k_over_aH_over_c": ratio.tolist(),
        "minimum_over_z": min_ratio.tolist(),
        "categories": categories,
        "provisional_qs_k_nodes_h_mpc": K[min_ratio >= 20].tolist(),
        "policy": (
            "Do not use the BZ-like phenomenological f(R) control as a production "
            "response below k=0.01 h/Mpc. Obtain a full linear MG solver before "
            "claiming a complete five-node six-family matrix."
        ),
    }

    out = ROOT / "data" / "derived" / "linear_controls"
    out.mkdir(parents=True, exist_ok=True)
    (out / "experiment_019_fr_qs_domain.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))

    assert min_ratio[0] < 5.0
    assert 5.0 <= min_ratio[1] < 20.0
    assert np.all(min_ratio[2:] >= 20.0)


if __name__ == "__main__":
    main()
