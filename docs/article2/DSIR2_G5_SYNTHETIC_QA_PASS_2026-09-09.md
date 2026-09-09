# DSIR-2 G5 data-whitened cross-family synthetic QA — PASS

Date: 2026-09-09. Scope: DSIR Article 2 only.

Status: IMPLEMENTATION QA PASS / NON-SCIENTIFIC.

This receipt records the synthetic fail-closed validation of `docs/article2/DSIR2_G5_DATA_WHITENED_CROSS_FAMILY_STRESS_CONTRACT_V0_1.md`. It does not close the real G5 stress gate and does not authorize a universal integer rank claim.

## GitHub Actions receipt

- workflow: `.github/workflows/dsir2-g5-data-whitened-cross-family-synthetic-qa-v0-1.yml`;
- head SHA: `de32907870f41e2b5178bb49d9cd86889be94652`;
- run: `34393024027`;
- job: `102605784509`;
- conclusion: `success`;
- `Run Article2 G5 synthetic QA`: success;
- `Assert exact PASS token and non-science boundary`: success;
- exact token: `PASS_DSIR2_G5_DATA_WHITENED_CROSS_FAMILY_SYNTHETIC_QA_V0_1`.

Artifact:

- ID: `10120389444`;
- name: `dsir2-g5-cross-family-synthetic-qa-de32907870f41e2b5178bb49d9cd86889be94652`;
- ZIP digest: `sha256:c7f78df0ee081096a0ed90f54b92ed5d69dc8db45da119a57a1f25a8aca5d012`.

## Synthetic properties validated

The implementation QA validates:

1. covariance/response shape mismatch rejection;
2. exact common-valid feature intersection without zero imputation;
3. exact equal-family mass under unequal family multiplicities;
4. distinction between catalog-multiplicity and equal-family spectra;
5. deterministic family-stratified bootstrap under frozen seed;
6. leave-one-family-out generation;
7. simultaneous response/covariance permutation invariance in whitened Gram geometry;
8. positive unit-rescaling invariance when covariance is transformed consistently;
9. response-only rescaling is not falsely declared invariant;
10. no inferred hard rank cutoff;
11. no real-data covariance read and no science gate scoring.

## Remaining Article-2 G5 blocker

The synthetic implementation prerequisite is closed. The remaining classifying task is the real compatible cross-family execution required by the frozen contract:

- bind a real observation/operator bridge acting on exactly the same theory-response coordinate vector;
- bind the exact corresponding real-data covariance;
- prove coordinate/order/unit compatibility;
- execute catalog-multiplicity, equal-family, alternative-within-family, stratified-bootstrap and leave-one-family-out stresses;
- record full spectra/geometry products without post-hoc rank cutoff;
- issue a durable G5 closure audit only after that real execution.

Article-2 readiness remains `83.3%` under the current strict publication-readiness ledger until the real G5 closure is admitted.
