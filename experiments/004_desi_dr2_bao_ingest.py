"""Experiment 004: ingest and validate the compressed DESI DR2 BAO likelihood.

This is a data/covariance readiness gate, not a cosmological-model fit.
It also constructs the sound-horizon-free Alcock-Paczynski contrast
F_AP = D_M / D_H at redshifts with anisotropic BAO measurements.
"""
from __future__ import annotations

from pathlib import Path
import csv
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "desi_dr2_bao"
DERIVED = ROOT / "data" / "derived" / "desi_dr2_bao"
MEAN = RAW / "desi_gaussian_bao_ALL_GCcomb_mean.txt"
COV = RAW / "desi_gaussian_bao_ALL_GCcomb_cov.txt"
OUT = DERIVED / "f_ap.csv"


def load_measurements(path: Path):
    rows = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            z, value, quantity = line.split()
            rows.append((float(z), float(value), quantity))
    return rows


def main() -> None:
    rows = load_measurements(MEAN)
    cov = np.loadtxt(COV)
    n = len(rows)
    assert cov.shape == (n, n) == (13, 13)
    symmetry_error = float(np.max(np.abs(cov - cov.T)))
    eig = np.linalg.eigvalsh(cov)
    min_eig = float(eig.min())
    assert symmetry_error < 1e-14
    assert min_eig > 0.0
    L = np.linalg.cholesky(cov)
    W = np.linalg.solve(L, np.eye(n))
    whitening_error = float(np.max(np.abs(W @ cov @ W.T - np.eye(n))))
    assert whitening_error < 1e-10
    by_z: dict[float, dict[str, tuple[int, float]]] = {}
    for i, (z, value, quantity) in enumerate(rows):
        by_z.setdefault(z, {})[quantity] = (i, value)
    derived = []
    for z in sorted(by_z):
        group = by_z[z]
        if "DM_over_rs" not in group or "DH_over_rs" not in group:
            continue
        i_dm, dm = group["DM_over_rs"]
        i_dh, dh = group["DH_over_rs"]
        f_ap = dm / dh
        grad = np.zeros(n)
        grad[i_dm] = 1.0 / dh
        grad[i_dh] = -dm / (dh * dh)
        sigma = float(np.sqrt(grad @ cov @ grad))
        corr = float(cov[i_dm, i_dh] / np.sqrt(cov[i_dm, i_dm] * cov[i_dh, i_dh]))
        derived.append((z, dm, dh, f_ap, sigma, corr))
    DERIVED.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["z", "DM_over_rd", "DH_over_rd", "F_AP", "sigma_F_AP_delta", "corr_DM_DH"])
        for row in derived:
            writer.writerow([f"{x:.10g}" for x in row])
    print(f"n_measurements={n}")
    print(f"covariance_shape={cov.shape}")
    print(f"covariance_symmetry_max_error={symmetry_error:.3e}")
    print(f"covariance_min_eigenvalue={min_eig:.9g}")
    print(f"covariance_condition_number={np.linalg.cond(cov):.6g}")
    print(f"whitening_max_error={whitening_error:.3e}")
    print("F_AP sound-horizon-free contrasts:")
    for z, dm, dh, f_ap, sigma, corr in derived:
        print(f"  z={z:.3f}: F_AP={f_ap:.6f} +/- {sigma:.6f}; corr(DM,DH)={corr:.3f}")
    print("G_DATA_INGEST=PASS")
    print("G6_REAL_DATA_RESPONSE_RECONSTRUCTION=OPEN")

if __name__ == "__main__":
    main()
