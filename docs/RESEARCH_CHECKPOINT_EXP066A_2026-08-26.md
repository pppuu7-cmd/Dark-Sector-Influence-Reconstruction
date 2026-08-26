# DSIR recovery checkpoint — Exp066A (2026-08-26)

## Prior boundary

Exp065B hard PASS established that the official `XCorrACT` Blue/Green `Clgg + Clkg` selected covariance is usable without regularization. That was observational eligibility only; G7/G8/G9 remained OPEN.

## Frozen Exp066A question

Can the raw ACT × unWISE projection basis be expressed through a solver-neutral interface rather than inheriting the pinned likelihood's CAMB provider layer?

The frozen interface exposes geometry (`chi`, inverse `z(chi)`, `H`, `f_K`, `H0`, `h`, `Omega_m`, curvature, `chi_star`) and **three independent spectra** in physical `k[Mpc^-1]`: `P_WW`, `P_Wm`, `P_mm`. No GR Poisson reconstruction between these spectra is permitted.

Exp066A tests only the no-CLEFT raw basis against the exact pinned upstream `compute_raw_spectra` algebra on deterministic analytic mock inputs. It does not fit ACT data and does not claim CLEFT is unnecessary for the published baseline likelihood.

## Hard result

Workflow run `32980938654`, job `98217145957` returned:

`PASS_SOLVER_NEUTRAL_RAW_PROJECTION_EQUIVALENCE_V0_1`.

Frozen nodes were `ell={10,30,80,150,300}`, `z=[0,3]`, Gauss-Legendre order 96, `kmax=1000 Mpc^-1`, equivalence tolerance `5e-13` times `max(1,max|reference|)`.

Every compared raw component had the same shape, was finite, and matched the pinned upstream reference; the observed maximum absolute difference was exactly zero for this deterministic regression. Algebraically zero no-CLEFT basis slots were zero in both implementations, including the dN/dz-PC-dependent tensor shapes.

The independent spectrum controls also passed exactly:

- scaling only `P_WW` by 1.1 changed only `kg/kmu` and `gg/mumu`, each by 10%;
- scaling only `P_Wm` by 1.1 changed only `kg/kg_b` and `gg/gmu_b`, each by 10%;
- scaling only `P_mm` by 1.1 changed only `gg/gg_bsq`, by 10%;
- all other raw components and `bdndz_norm` stayed unchanged.

This is an explicit anti-collapse check: the projection adapter does not infer Weyl from matter through a hidden GR Poisson relation.

## Scientific meaning

The ACT × unWISE raw cosmological projection layer is now separated from the CAMB-specific provider layer for the frozen no-CLEFT branch. This is a bridge/infrastructure PASS, not a G7 physical-law result.

## Next action

Exp066B must separately freeze and validate the closure from raw basis to selected observable bandpowers, including nuisance/bias handling, CLEFT/nonlinear contributions where used by the public baseline, transfer functions and released bandwindow matrices. The cleanest regression is against the pinned official backend on one fixed reference cosmology, with the full numerical settings and nuisance point committed before inspecting the comparison.

Only after the selected-bandpower bridge passes may a covariance-whitened training-only cross-channel relation/null statistic be preregistered. A fresh withheld theory family for G8 must not be chosen before that relation is frozen.

Top-level state: **G7 OPEN, G8 OPEN, G9 OPEN**.
