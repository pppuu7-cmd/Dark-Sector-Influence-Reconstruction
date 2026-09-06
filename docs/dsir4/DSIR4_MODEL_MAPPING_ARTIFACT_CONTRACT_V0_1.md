# DSIR-4 model mapping artifact contract v0.1

Frozen: 2026-09-06. Scope: existing-model mapping infrastructure only. No model scientific status is created here.

## Common interface

Every frozen hypothesis must be mapped to the same residual tensor convention

\[
X_{\mu\nu}=M_0^2 G_{\mu\nu}-T^{\rm known}_{\mu\nu}.
\]

The mapping artifact must make explicit what is included in `T_known`, the metric/sign/index conventions, frame/gauge choices used for intermediate expressions, and the transformation to gauge-invariant or explicitly gauge-bound observable quantities where applicable.

## Required tensor decomposition record

At minimum the mapping artifact must specify whether the hypothesis provides, on the certified domain:

- background residual density-like component;
- background residual pressure-like component;
- scalar density perturbation component;
- scalar momentum/velocity component;
- scalar isotropic pressure perturbation component;
- scalar anisotropic-stress / slip-generating component.

A component may be structurally zero, nonzero, derived, or outside the hypothesis domain, but it may not be silently omitted.

The mapping artifact must distinguish a genuine zero prediction from `NOT_YET_MAPPED` and from `OUTSIDE_DOMAIN`.

## Interaction bookkeeping

For interacting-dark-sector hypotheses, the mapping must explicitly state the sector partition and any transfer current/source convention. Re-labeling energy-momentum exchange between sectors must not create a false difference in total `X_{mu nu}`. The total residual prediction is authoritative for the common interface; sector decomposition is additional provenance.

## Modified-gravity bookkeeping

For modified-gravity hypotheses, terms moved to the effective source side must be algebraically bound to the original field equations and convention. A different effective-fluid rearrangement that leaves observables invariant is not automatically a distinct DSIR hypothesis; equivalence-class handling is required where appropriate.

## Certified domain

Each frozen hypothesis must provide an explicit certified domain with at least:

- `z_min`, `z_max`;
- `k_min_exclusive_mpc_inv`, `k_max_mpc_inv`;
- perturbative regime assumptions;
- stability/branch conditions required for the prediction;
- any quasi-static, sub-horizon, linear, or other approximation used.

No prediction may be extrapolated outside its certified domain to manufacture a DSIR gate result.

## Prediction artifact

A model hypothesis becomes testable only after a versioned prediction artifact is frozen. The artifact must bind:

- hypothesis ID and parameter values or equivalence-class definition;
- mapping artifact SHA-256;
- numerical code/version/commit or exact analytic expression identity;
- input cosmological/nuisance assumptions permitted by the frozen funnel;
- output grid/domain and units;
- deterministic hash of the prediction payload;
- provenance of any external transfer-function / Boltzmann / EFT computation.

## Required status separation

`mapping_ready`, `prediction_ready`, `numerically_evaluated`, and scientific gate status are separate concepts. A mapping or prediction artifact passing a static audit is support `+0/+0` and must not be promoted to `PASS` in the DSIR Model Funnel Matrix.

## Equivalence classes

If two hypotheses map to identical DSIR predictions over every currently authoritative gate, they may be grouped only under a prospectively defined `equivalence_class_id` with the equivalence criterion and comparison hashes recorded. This is observational equivalence under the stated gates, not proof that the underlying theories are physically identical.

## Anti-circularity

Mapping formulas and prediction-generation rules must be frozen before the hypothesis sees the gate used to evaluate it. Changing equations, parameterization, branch selection, approximation, or fitting rules after a gate failure creates a new hypothesis version.
