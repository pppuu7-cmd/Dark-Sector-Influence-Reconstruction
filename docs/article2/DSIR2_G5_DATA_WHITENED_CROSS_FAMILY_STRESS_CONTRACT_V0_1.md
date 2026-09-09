# DSIR-2 G5 data-whitened cross-family stress contract v0.1

Date frozen: 2026-09-09. Scope: DSIR Article 2 / G5 only.

Status: PROSPECTIVE CLOSURE CONTRACT. No real G5 closure output was read before this freeze.

## 1. Purpose

Close the one remaining Article-2 machinery item recorded in `docs/GATES.md`: data-whitened cross-family rank/geometry stress tests under the already-frozen missingness and family-prior rules.

This contract does **not** introduce an integer intrinsic-rank threshold. In particular, the historical normalized raw-theory singular ratios

`(1, 0.52046, 0.26140, 0.20087, 0.08299, 5.92e-4)`

must not be relabelled post hoc as `R_model=5` or any other hard rank statement.

## 2. Existing frozen methodology inherited unchanged

The test inherits:

- covariance whitening before observational rank/geometry interpretation;
- `R_model(pi)` theory-prior dependence rather than a unique catalog rank;
- exact common-valid feature blocks for global SVD; no zero imputation of missing family/channel cells;
- family prior decomposition `pi(i)=pi(f) pi(i|f)`;
- equal total family mass as the pilot balanced prior;
- catalog-multiplicity prior as an explicit sensitivity case, not the default objective prior;
- at least one explicit alternative within-family weighting;
- stratified bootstrap over families/model instances;
- identical row weights in the corresponding noise/null calibration.

Authoritative methodology files include `docs/THEORY_ATLAS_SAMPLING_V0_1.md` and `schemas/model_instance_v0_2.yaml`.

## 3. Required compatible real input

A classifying execution must bind a machine-readable manifest containing:

1. model-instance response rows with immutable IDs, family IDs, solver/provenance identity and validity masks;
2. a single exact common-valid feature block used by every family included in the global stress test;
3. an observational response/operator bridge that maps the frozen theory response coordinates into the same coordinate vector on which the covariance acts;
4. the exact real-data covariance matrix for that mapped vector, with immutable provenance/digest;
5. units and coordinate order for both response vector and covariance;
6. positive-definiteness or an already-prospectively-authorized regularization rule, with no output-dependent eigenvalue trimming.

A covariance defined on different observables or coordinate order is incompatible and must be rejected rather than interpolated/padded/relabelled.

DESI DR1 ShapeFit covariance, for example, may be used only if an exact frozen observation-operator map from the theory-atlas coordinates to that ShapeFit vector exists. The mere existence of a real covariance is insufficient.

## 4. Whitening

For an admitted covariance `C`, construct a fixed whitening map from the prospectively bound matrix, e.g. a Cholesky-equivalent `L` satisfying `C=L L^T`, and transform each mapped response row `r` as

`r_w = L^{-1} r`.

The implementation must record:

- covariance shape/order/digest;
- whitening method and numerical library versions;
- reconstruction residual for the factorization;
- condition diagnostics;
- exact whitened feature order.

No family label, theory amplitude, singular vector, relation score or downstream result may alter the whitening map.

## 5. Prior/weighting stress ensemble

The classifying report must include, at minimum:

A. `catalog_multiplicity` — equal mass per catalog/model row;

B. `equal_family` — total mass exactly `1/N_fam` per represented family with the frozen within-family default;

C. `alternative_within_family` — one prospectively named defensible coordinate/weighting choice, frozen before its singular spectrum is read;

D. `stratified_bootstrap` — family-stratified bootstrap using a prospectively frozen seed, draw count and within-family resampling rule;

E. `leave_one_family_out` diagnostics for every represented non-baseline family where the exact common-valid block remains nonempty.

All spectra must use the same admitted whitening map and corresponding weight-aware null/noise calibration.

## 6. Required outputs — no post-hoc rank cutoff

For every stress case, record:

- number of families and model instances;
- exact family weights and within-family weights;
- exact common-valid feature IDs;
- full singular-value spectrum and normalized spectrum;
- weight-aware null/noise spectrum or noise-edge diagnostics under the same weights;
- principal-subspace geometry diagnostics that are defined prospectively by the implementation;
- condition/factorization diagnostics;
- bootstrap distributions for each reported continuous spectral/geometric statistic;
- leave-one-family-out deltas;
- all invalid/incompatible cases separately.

No singular-value cutoff may be chosen after these outputs are viewed.

## 7. G5 closure criterion

Because no historical hard integer rank threshold was frozen, G5 closure is a **robustness-methodology closure**, not a claim that a particular integer rank is universally true.

`PASS_G5_DATA_WHITENED_CROSS_FAMILY_STRESS_V0_1` may be emitted only if:

1. all input/provenance/common-block/coordinate/unit checks pass;
2. the real covariance and theory-response vector are proven coordinate-compatible through the frozen observation bridge;
3. whitening factorization/roundtrip controls pass the prospectively coded numerical checks;
4. all required prior/weighting cases A–E execute without forbidden missing-value filling or data-dependent pruning;
5. the report includes the full required spectra/noise/subspace/bootstrap/leave-one-family-out products;
6. no conclusion depends on an unregistered hard rank cutoff;
7. implementation metamorphic controls show that benign coordinate representation changes already covered by G5 (permutation with matched covariance permutation, positive unit rescaling with matched covariance transformation) do not alter the physical whitened geometry beyond the prospectively coded numerical tolerance;
8. a durable closure audit explicitly limits the Article-2 claim to robustness of the **method/geometry report**, not a universal integer `R_model`.

A valid execution may reveal strong prior sensitivity. That is a scientific result about `R_model(pi)` and does not by itself fail G5, provided the sensitivity is faithfully reported rather than hidden.

## 8. Fail-closed taxonomy

- coordinate/covariance mismatch, bad units/order, missing provenance, duplicate IDs, forbidden zero imputation, data-dependent covariance regularization, or downstream leakage -> `INVALID_FOR_G5_SCIENCE`;
- infrastructure interruption -> `INCOMPLETE_G5_STRESS`;
- compatible execution completing all required stress products -> eligible for the PASS token above;
- no failed stress case may be rescued by changing family weights, common block, covariance, seed, rank cutoff or numerical threshold after output inspection.

## 9. Synthetic QA before real execution

Synthetic QA must test at least:

1. covariance/response shape mismatch rejection;
2. feature-order mismatch rejection;
3. exact common-valid intersection and no zero imputation;
4. equal-family weights sum to equal family mass despite unequal row counts;
5. catalog-multiplicity and equal-family priors are distinguishable when family multiplicities differ;
6. deterministic stratified bootstrap under a frozen seed;
7. leave-one-family-out generation;
8. covariance/response simultaneous permutation invariance;
9. positive coordinate-rescaling invariance when covariance is transformed consistently;
10. mismatch under response-only rescaling is detected rather than called invariant;
11. singular spectra are reported in full without an inferred hard rank label;
12. leakage/forbidden post-hoc cutoff metadata is rejected.

Synthetic PASS is implementation readiness only; Article-2 remains 83.3% until the compatible real data-whitened cross-family execution and durable G5 closure audit PASS.

## 10. Immediate next action

Implement and run the synthetic self-test for this contract while separately locating/freezing the real observational operator+covariance bridge that acts on the exact same response coordinates. These tasks may proceed in parallel.