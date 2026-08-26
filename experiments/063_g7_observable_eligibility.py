#!/usr/bin/env python3
"""Experiment 063A: audit which existing DSIR channels are eligible for a G7 law search.

This is deliberately an eligibility/quotient audit, not a discovery experiment.
It verifies that the corrected DESI DR1 ShapeFit AP/growth/shape block has a
usable positive-definite covariance and an existing conditional-innovation
quotient, while the raw theory Weyl/slip separator remains ineligible until a
survey kernel/covariance binding is added.
"""
from pathlib import Path
import sys
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.shapefit_response import load_erratum, validate_covariance
from dsir.conditioning import conditional_innovation

SRC = ROOT / "data" / "observations" / "desi_dr1_shapefit_erratum_2026.json"
OUT = ROOT / "data" / "derived" / "g7"
USE = ("LRG1", "LRG2", "LRG3", "ELG2", "QSO")


def main():
    meta, bins = load_erratum(SRC)
    checks = []
    min_eig = float("inf")
    max_abs_beta = 0.0
    for name in USE:
        rec = bins[name]
        cov = np.asarray(rec["cov"], float)
        assert validate_covariance(cov), name
        sub = cov[np.ix_([1, 2, 3], [1, 2, 3])]
        eig = np.linalg.eigvalsh(sub)
        min_eig = min(min_eig, float(eig.min()))
        fid = meta["fiducial_for_control"][name]
        y = np.asarray(rec["vector"], float)[[1, 2, 3]]
        r = y - np.array([fid["DH_over_DM"], fid["f_sigma_s8"], 0.0])
        gi, gv, gb = conditional_innovation(r, sub, target=1, conditioned_on=[0, 2])
        ai, av, ab = conditional_innovation(r, sub, target=0, conditioned_on=[1, 2])
        assert gv > 0 and av > 0
        max_abs_beta = max(max_abs_beta, float(np.max(np.abs(gb))), float(np.max(np.abs(ab))))
        checks.append({
            "bin": name,
            "z_eff": float(rec["z_eff"]),
            "min_cov_eigenvalue": float(eig.min()),
            "growth_innovation_sigma": float(np.sqrt(gv)),
            "ap_innovation_sigma": float(np.sqrt(av)),
        })

    out = {
        "experiment": "Exp063A",
        "status": "PASS_OBSERVABLE_ELIGIBILITY_AUDIT",
        "eligible_training_block": {
            "name": "DESI_DR1_ShapeFit_AP_growth_shape",
            "channels": ["DH_over_DM", "f_sigma_s8", "m_plus_n"],
            "bins": list(USE),
            "covariance": "corrected 2026 erratum covariance; validated positive-definite per bin",
            "quotient": "Gaussian conditional innovations already implemented in Experiment 010",
            "zero_imputation": False,
        },
        "ineligible_for_g7_claim_without_new_binding": {
            "name": "raw_theory_Weyl_slip",
            "reason": "repository has a pinned theory-space separator but no survey response kernel plus covariance binding for this channel",
        },
        "frozen_next_step": "construct one training-only mathematical cross-channel relation inside the eligible ShapeFit block; freeze statistic/tolerance and null control before selecting any fresh withheld family",
        "diagnostics": {
            "minimum_three_channel_covariance_eigenvalue": min_eig,
            "maximum_absolute_conditional_beta": max_abs_beta,
            "bins": checks,
        },
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "exp063a_observable_eligibility.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
