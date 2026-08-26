# Exp071C — known-sector F30 specificity control preregistration v0.1

**Date:** 2026-08-27  
**Status:** PROSPECTIVE PREREGISTRATION — frozen before generating any K1/K2 control spectra.

## Question

F30 passed prospectively on withheld C9 IDM–baryon, but Exp071B subsequently motivated a specificity question: is the frozen two-coordinate path gate distinctive of dark-sector response geometry, or can ordinary cosmological parameter families produce the same non-self-intersecting microscopic-order trajectory?

Exp071C tests this with two **known-sector controls** that have not been generated for this question before this preregistration.

This experiment does not alter F30, does not train on K1/K2, and cannot close G7/G8/G9.

## Frozen solver and baseline

Use `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`, matching C7/C8/C9 solver provenance.

Ordinary-CDM reference cosmology:

- `h = 0.67`
- `T_cmb = 2.7255`
- `omega_b = 0.0224`
- `omega_cdm = 0.1200`
- `Omega_k = 0`
- `N_ur = 3.046`
- `YHe = 0.2404`
- `recombination = RECFAST`
- `reio_parametrization = reio_none`
- scalar adiabatic synchronous-gauge linear `mPk` only
- `A_s = 2.10e-9`
- `n_s = 0.965`
- `alpha_s = 0`
- `k_pivot = 0.05 Mpc^-1`
- `P_k_max_h/Mpc = 1.0`

Frozen output window, inherited unchanged from Exp058/060/061:

- `z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`
- `k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

Response is always `R(z,k)=ln[P_control(z,k)/P_reference(z,k)]` sampled by the same log-k interpolation semantics used by C7/C8/C9. No nonlinear power.

## K1 — primordial-tilt control

All cosmological parameters remain at the reference values except

`n_s = [0.970, 0.975, 0.980, 0.985, 0.990]`.

The physical order is exactly ascending `n_s`. All five points lie on the same side of the reference `n_s=0.965`; no sign-flip point is included.

Purpose: determine how the normalized F30 construction treats a standard primordial spectral-shape direction.

## K2 — baryon-fraction control at fixed total physical matter density

Freeze `omega_m = omega_b + omega_cdm = 0.1424` exactly and use

- `omega_b = [0.0228, 0.0232, 0.0236, 0.0240, 0.0244]`
- corresponding `omega_cdm = [0.1196, 0.1192, 0.1188, 0.1184, 0.1180]`.

The physical order is exactly ascending `omega_b` (equivalently ascending baryon fraction at fixed `omega_m`). All other parameters remain frozen.

Purpose: test a known standard-sector transfer/BAO shape mechanism rather than a dark interaction.

## Frozen operator and gate

The F30 operator is inherited **without retraining or recalibration** from Exp060A:

- training families only: C3 GDM + C5 f(R) + C7 IDM–DR + C8 IDM–photon;
- exact training artifacts/runs already frozen by Exp060A;
- coordinate `ell`: R^2-weighted log-k localization;
- coordinate `q`: projection of the unit response onto training-only centered-SVD PC2;
- affine standardization from training only;
- no K1/K2 information may enter operator construction.

For each control family separately, compute full coordinates for its five ordered points and seven leave-one-redshift rebuilds. The family **F30-control PASS** condition is exactly:

1. all four adjacent standardized `(ell,q)` step norms are `> 1e-10`;
2. no non-adjacent polyline segments intersect using the inherited `1e-10` orientation/on-segment tolerance;
3. the full path passes;
4. every one of seven leave-one-z rebuilt paths also passes.

No threshold may be changed after seeing K1/K2 output.

## Primary prospective specificity classification

Let `K1_pass` and `K2_pass` denote the exact family-level full+all-LOO F30-control results.

- If `K1_pass OR K2_pass`: classify **`F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL`**.
- If `NOT K1_pass AND NOT K2_pass`: classify **`NO_F30_SPECIFICITY_WEAKENING_FROM_K1_K2`**.

The second outcome is deliberately *not* called proof of dark specificity; two controls are insufficient for that claim.

## Secondary frozen diagnostics

For each K1/K2 family, using its five 35-component response matrices:

- flatten and unit-normalize each response;
- center the five unit vectors within the family;
- report centered-SVD singular values and explained/cumulative variance fractions;
- report the exact `(ell,q)` coordinates, adjacent step norms, and any intersecting segment pairs for full and LOO cases.

These secondary quantities are descriptive and do not alter the primary classification.

## Negative / integrity controls

The workflow must assert:

- pinned CLASS commit exactly matches the frozen SHA before and after execution;
- exactly five K1 and five K2 configurations are used in the frozen order;
- reference and all controls cover all seven z nodes and all five k nodes;
- no C9 response is used as training input;
- Exp071B outputs, if available, are not used to tune K1/K2 or the gate;
- G7/G8/G9 remain OPEN regardless of Exp071C outcome.

## Interpretation boundary

A known-sector PASS would be scientifically important because it would show that the current F30 topology is **not specific to unknown dark physics**. It would not invalidate the mathematical F30 PASS on C9; it would change its interpretation from candidate dark-sector organizing law toward a more generic response-geometry property.

Two known-sector FAILs would only mean the candidate specificity survives these two tests. They would not establish a fundamental dark-sector law.
