# DSIR response basis v0.1 — frozen conventions

**Frozen:** 2026-08-24  
**Machine-readable specification:** `config/response_basis_v0_1.json`  
**Implementation:** `src/dsir/response_basis.py`

This document freezes the coordinate conventions used for the first six-family DSIR response matrix. It does **not** claim that these coordinates are the final optimal basis.

## 1. Why relative/logarithmic coordinates

For a positive response quantity `X`, use

`r_X = ln(X/X_ref)`.

This is dimensionless, converts multiplicative changes into additive ones, and prevents arbitrary output units from entering the physical response vector. A change of units applied consistently to `X` and `X_ref` cancels exactly.

Signed quantities for which a logarithm is undefined are not admitted to the common core until a gauge-invariant signed normalization has been separately validated.

## 2. Background coordinate

The common background coordinate is the calibration-free relative expansion response

`r_E(z;z*) = ln[(H(z)/H(z*))/(H_ref(z)/H_ref(z*))]`,

with frozen anchor

`z* = 0.51`.

A common multiplicative calibration `H -> lambda H` cancels exactly. This matches the logic of the calibration-independent AP reconstruction already used in G6A.

Frozen redshift nodes:

`z = {0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33}`.

The anchor coordinate itself is identically zero and is not counted as an independent dimension.

## 3. Geometry identities are derived coordinates

For flat-FLRW AP geometry

`F_AP = D_M/D_H = D_M H/c`.

Therefore the log-response obeys the exact identity

`r_FAP = r_DM + r_H`.

Consequently DSIR must not concatenate `F_AP`, `D_M`, and `H` as if all three were independent law-discovery coordinates. Native observational coordinates may contain them, but exact geometry identities are projected/quotiented before rank or law claims.

## 4. Matter-power coordinate

The first common perturbation coordinate is

`r_P(k,z) = ln[P_m(k,z)/P_m,ref(k,z)]`.

For raw theory-response comparisons the primordial parameters (`A_s`, `n_s`, etc.) are held fixed unless an explicit nuisance projection is performed. This preserves real late-time growth-amplitude differences.

**Never normalize each model independently to `D(a=1)=1` when amplitude information is being compared.** That failure mode was already identified in Experiment 007.

`P_m` means the total clustering non-relativistic matter spectrum for an explicitly matched solver component definition. Before comparing solvers, the matter-component bookkeeping must be checked (CDM/GDM/interacting-DM/WDM/etc.).

### Frozen k blocks

Linear core:

`k/(h Mpc^-1) = {0.001, 0.003, 0.01, 0.03, 0.1}`.

Diagnostic extension:

`{0.2, 0.5, 1.0}`.

The extension is not mixed into a linear-rank claim without a separate nonlinear-validity gate.

For the pinned GDM_CLASS regression, `k < 0.001 h/Mpc` is retained as an ultra-large-scale diagnostic sector but excluded from the first common six-family rank block because the zero-closure implementation has a documented finite-start initial-condition sensitivity there. This is a bookkeeping separation, not deletion of evidence.

## 5. Shape-only quotient

If the constant log-amplitude mode must be removed from a k-block, use the same covariance/precision metric as the analysis.

For response vector `r`, precision `W=C^-1`, and constant vector `1`, fit

`a = (1^T W r)/(1^T W 1)`

and define

`r_perp = r - a 1`.

Then

`1^T W r_perp = 0`.

The raw `r_P` block and its amplitude-quotiented copy must never both be counted as independent directions in the same rank calculation.

## 6. Optional discriminant blocks

The following are frozen as optional/derived channels but are not mandatory in the first complete six-family matrix:

- growth-rate response `r_f=ln(f/f_ref)`;
- CMB lensing response `ln(C_ell^{phi phi}/C_ell,ref^{phi phi})` at ell `{10,30,100,300,800}`;
- gauge-invariant Weyl/metric responses after a cross-solver extractor is validated.

Raw gauge-specific metric variables are forbidden as common response coordinates.

## 7. Rank rules

Before any `R_obs` or `R_model(pi)` claim:

1. use a complete/common channel block or a separately validated missing-data method;
2. transform the covariance with every coordinate transformation;
3. whiten before rank estimation;
4. quotient exact definitions, conservation/Bianchi identities, calibration modes, and known measurement-induced directions;
5. do not duplicate derived coordinates and their parents;
6. propagate theory-family weights into null calibration;
7. record solver SHA, gauge, component definition, and precision settings.

## 8. Meaning of G2

G2 means these **conventions are frozen for v0.1**, not that every optional response channel has already been implemented for every theory. Any future change to the core definitions, grids, normalization rules, or identity policy requires a version bump (v0.2 or later) and a compatibility note rather than silently rewriting v0.1.
