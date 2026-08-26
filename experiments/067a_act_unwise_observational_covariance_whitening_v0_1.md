# Exp067A — ACT DR6 × unWISE observational covariance whitening v0.1

Date: 2026-08-26
Status: preregistered before execution.

## Purpose

Exp066C repaired the exact forward operator but did not establish an observationally valid G7 relation. Exp067A is the next infrastructure gate: extract the released observational covariance consistently with the frozen 26-component `[Blue gg6, Blue kg7, Green gg6, Green kg7]` vector and construct a reproducible whitening transform before any cross-channel law fit or withheld-family test.

This experiment is covariance/whitening closure only. It must not optimize a residual law, choose a dark-sector family, tune cuts, change nuisance conventions, or reinterpret Exp066B/Exp066C.

## Immutable lineage

- Exp066B remains `FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`.
- Exp066C remains `PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`.
- likelihood source remains `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.
- public archive SHA256 remains `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.
- samples, multipole cuts and final 26-component order are unchanged from Exp066C.

## Frozen construction

Let `Sigma_full` be the released covariance in the exact data-vector order used by the pinned likelihood. Let `S` be the deterministic selection operator mapping that likelihood vector to the frozen Exp066C 26-component vector. Define

`Sigma = S Sigma_full S^T`.

Require a direct float64 Cholesky factorization

`Sigma = L L^T`,

with no covariance shrinkage, eigenvalue clipping, pseudoinverse, diagonal loading, jitter, or regularisation. Define the whitening operator by direct triangular solve

`W = L^{-1}`

conceptually, implemented by solves rather than explicit inversion where practical.

## Frozen subtests

### A1 — provenance and ordering closure

Require pinned source commit and archive SHA256 to match Exp066C. Reconstruct the exact released likelihood data-vector ordering from source/config metadata, apply the unchanged Blue/Green gg/kg cuts, and require exactly 26 selected coordinates in the frozen order `[Blue gg6, Blue kg7, Green gg6, Green kg7]`.

Hard requirement: exact order equality and dimension 26.

### A2 — covariance symmetry/finite closure

For selected `Sigma`, require shape `(26,26)`, all finite entries, strictly positive diagonal, and

`max_abs(Sigma-Sigma^T) / max(max_abs(Sigma),1e-300) <= 1e-12`.

No symmetrization is allowed before evaluating this check.

### A3 — positive-definite direct Cholesky closure

Require direct `numpy.linalg.cholesky(Sigma)` to succeed without modification of `Sigma`. Record the minimum and maximum eigenvalues diagnostically only; they cannot change the criterion.

Require Cholesky reconstruction residual

`||L L^T - Sigma||_inf / max(||Sigma||_inf,1e-300) <= 5e-12`.

### A4 — whitening identity closure

Construct `W` from direct triangular solves using `L`. Require

`||W Sigma W^T - I||_inf <= 5e-10`.

This is an operator identity test only; no observational goodness-of-fit statistic is evaluated here.

### A5 — deterministic round-trip control

Use one frozen deterministic 26-vector generated from a fixed RNG seed `20260826+67`. Whiten and unwhiten it with direct solves and require relative infinity-norm round-trip error `<= 5e-12`.

## Hard PASS / FAIL

PASS only if A1–A5 all pass under the frozen criteria:

`PASS_ACT_UNWISE_OBSERVATIONAL_COVARIANCE_WHITENING_V0_1`

Otherwise:

`FAIL_ACT_UNWISE_OBSERVATIONAL_COVARIANCE_WHITENING_V0_1`

Any FAIL is preserved as a scientific/infrastructure result and corrected only by a separately numbered experiment.

## Gate semantics

Even a PASS does not close G7. It only makes a covariance-whitened observational residual law eligible for preregistration. After PASS, a later experiment may freeze a training-only cross-channel relation and null statistic. Only after that relation is fixed may a fresh withheld-family test be used for G8.

Until then: `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
