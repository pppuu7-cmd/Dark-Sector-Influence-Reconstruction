"""Utilities for corrected DESI DR1 ShapeFit response vectors."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

ORDER = ("DV_over_rd", "DH_over_DM", "f_sigma_s8", "m_plus_n")


def load_erratum(path):
    data = json.loads(Path(path).read_text())
    scale = float(data["covariance_scale"])
    out = {}
    for name, rec in data["bins"].items():
        v = np.asarray(rec["vector"], dtype=float)
        c = np.asarray(rec["covariance"], dtype=float) * scale
        out[name] = {"z_eff": float(rec["z_eff"]), "vector": v, "cov": c}
    return data, out


def correlation(cov):
    cov = np.asarray(cov, dtype=float)
    d = np.sqrt(np.diag(cov))
    return cov / np.outer(d, d)


def validate_covariance(cov, atol=1e-12):
    cov = np.asarray(cov, dtype=float)
    if not np.allclose(cov, cov.T, atol=atol, rtol=0):
        return False
    return bool(np.min(np.linalg.eigvalsh(cov)) > 0)


def ap_growth_correlation(cov):
    return float(correlation(cov)[1, 2])


def fiducial_chi2_three_channel(vector, cov, fid_ap, fid_growth):
    """Chi2 in [DH/DM, f sigma_s8, m+n] against fiducial [AP,g,0]."""
    idx = [1, 2, 3]
    y = np.asarray(vector, float)[idx]
    c = np.asarray(cov, float)[np.ix_(idx, idx)]
    r = y - np.array([fid_ap, fid_growth, 0.0])
    return float(r @ np.linalg.solve(c, r))
