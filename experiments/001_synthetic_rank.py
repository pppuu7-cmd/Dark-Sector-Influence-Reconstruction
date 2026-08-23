#!/usr/bin/env python3
"""DSIR Experiment 001: verify recovery of known latent influence rank."""
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.rank import effective_rank, variance_rank, noise_edge_rank


def make_case(n_models=180, n_obs=64, latent_rank=3, noise=1.0, signal=5.0, seed=338):
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.normal(size=(n_obs, latent_rank)))
    coeff = rng.normal(size=(n_models, latent_rank))
    signal_matrix = signal * coeff @ q.T
    z = signal_matrix + noise * rng.normal(size=(n_models, n_obs))
    return z


def main():
    z = make_case()
    r_eff = effective_rank(z)
    r99 = variance_rank(z, 0.99)
    r_edge, obs, edge = noise_edge_rank(z, n_null=300, quantile=0.95, seed=339)
    print("DSIR Experiment 001")
    print(f"matrix_shape={z.shape}")
    print("injected_latent_rank=3")
    print(f"effective_rank={r_eff:.3f}")
    print(f"variance_rank_99={r99}")
    print(f"noise_edge_rank_95={r_edge}")
    print("top_observed_singular_values=" + ",".join(f"{x:.3f}" for x in obs[:8]))
    print(f"null95_global_noise_edge={edge:.3f}")
    if r_edge != 3:
        raise SystemExit(f"G4 FAIL: expected noise-edge rank 3, got {r_edge}")
    print("G4_SYNTHETIC_RANK_RECOVERY=PASS")

if __name__ == "__main__":
    main()
