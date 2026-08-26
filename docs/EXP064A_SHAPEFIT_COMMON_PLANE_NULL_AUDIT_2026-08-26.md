# Exp064A — DESI ShapeFit common-plane null audit (2026-08-26)

## Purpose

Test one mathematically minimal training-side cross-channel relation inside the observationally eligible DESI DR1 ShapeFit AP/growth/shape block selected by Exp063A. This is a discovery-side training audit, **not** a withheld-family test and not a G7/G8 closure claim.

## Frozen observable coordinates

Use only `LRG1, LRG2, LRG3, ELG2, QSO` and the corrected 2026 erratum covariance. For bin i define

- `r_AP = (DH/DM)/(DH/DM)_fid - 1`,
- `r_G = (f sigma_s8)/(f sigma_s8)_fid - 1`,
- `r_S = m+n`.

Let `J_i = diag(1/AP_fid, 1/G_fid, 1)` and propagate the measured three-channel covariance as

`C_i^d = J_i C_i J_i^T`.

Undefined channels remain masked; no zero imputation is permitted.

## Single candidate relation

Fit exactly one homogeneous physical-coordinate plane through the fiducial origin,

`a_AP r_AP + a_G r_G + a_S r_S = 0`.

The normal is the smallest generalized-eigenvalue vector of

`S_R = sum_i r_i r_i^T`, `S_C = sum_i C_i^d`,

so `S_R a = lambda S_C a`. Normalize `||a||_2=1`; sign is fixed by `a_S >= 0` with a deterministic first-nonzero fallback.

This formulation avoids choosing a Cholesky ordering as a hidden channel rotation and keeps the relation in the declared dimensionless AP/growth/shape coordinates while still using the measured covariance metric.

## Nontriviality and overfit control

For each leave-one-bin split, refit the plane on the other four bins and evaluate the held-out standardized orthogonal residual

`z_i = |a_-i^T r_i| / sqrt(a_-i^T C_i^d a_-i)`.

The scalar predictive control is `LOO_RMS = sqrt(mean(z_i^2))`.

The null is fixed to independent Gaussian residuals `r_i ~ N(0,C_i^d)` in each bin. Use RNG seed `20260826`, exactly 20,000 null draws, and refit the same generalized-eigenvalue/LOO operator on every draw. Lower-tail empirical p-values include the standard `+1` correction.

A nontrivial common-plane candidate exists only if BOTH

- `p_lower(lambda_min) <= 0.05`, and
- `p_lower(LOO_RMS) <= 0.05`.

`LOO_max` is descriptive only and cannot rescue or veto the gate.

## Anti-retuning contract

If the dual nontriviality criterion fails, the fitted plane is not promoted to a law, no withheld family is selected to rescue it, and no coefficient, channel subset, redshift subset, centering convention, covariance transform, intercept, statistic, seed or alpha may be changed inside Exp064A. Any different proposal requires a new recorded experiment.

If it passes, the coefficients and an independently stated prospective tolerance must be frozen in a later preregistration **before** selecting or computing a fresh withheld family/mechanism.

## Gate semantics

Exp064A can at most identify a training-side candidate. G7/G8/G9 remain OPEN regardless of the numerical outcome of this audit; withheld survival is a separate future gate.