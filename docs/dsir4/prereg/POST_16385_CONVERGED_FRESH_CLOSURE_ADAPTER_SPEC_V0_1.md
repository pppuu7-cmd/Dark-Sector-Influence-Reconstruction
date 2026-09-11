# Post-16385 CONVERGED fresh Layer-B closure adapter — prospective dormant spec V0.1

Status at freeze: **DORMANT / response-blind**. This specification is frozen before any terminal result from canonical 8193→16385 run `34555022975` is consumed. It does not predict or assume that result.

## Activation
The adapter may activate only if an independently verified terminal authority from the frozen canonical 8193→16385 support run has classification exactly:

`COMMON_GRID_NEXT_REFINEMENT_CONVERGED_PLUS_0_PLUS_0`

Any NOT_CONVERGED, INVALID_INFRA, malformed or unverified result leaves this closure branch inactive.

## Scientific purpose
If activated, perform a **fresh** Layer-B scientific closure rerun. No response values, raw operands, interpolants or classification quantities from the 8193→16385 support gate may be reused. The closure must recompute fresh canonical responses in one process and replay the unchanged Exp073IR physical/accounting semantics.

## Frozen science inherited unchanged
- strict `REL_TOL=1e-3`; exact `1e-3` is not converged;
- `h=1e-4`;
- native k-per-decade = 20;
- centered-cubic interpolation and existing request-plan hashes;
- exact parent retained identity/order and 107-row traversal;
- Layer-B invalid-row fraction `<=0.05`;
- retained dimension `>=15`;
- unsupported target evaluations = 0;
- requested-node lookup relative mismatch `<=1e-12`;
- finite/nonzero status, row labels and BOSS dense-z consistency unchanged;
- no covariance/whitening/nuisance/relation-null read during this closure;
- covariance restriction remains unauthorized and Wm_S3 remains closed unless a later separately frozen gate authorizes them.

## Canonical execution adaptation only
Relative to dormant `ci/post_jm_converged_fresh_layerb_scientific_closure_v0_1.py`, the only allowed execution/provenance adaptations are:
1. activation token: fourth-refinement JM CONVERGED → next-refinement CONVERGED;
2. canonical coarse lattice: 4097 → 8193, exact decoded SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`, text SHA256 `90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6`;
3. canonical fine lattice: 8193 → 16385, exact decoded SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`, text SHA256 `7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69`;
4. CLASS input capacity: 18432; parser capacity: 524288;
5. require the already verified execution-only history-suppression patch `scripts/dsir4/classiv_k_output_history_suppression_patch_v0_1.py`, git blob `e20687e933d665973c3be40598180587701fa8e0`, with exact post-patch SHA256 `4e9a419d46471ffab74df3d14239e000bf92f2e198edad4d2c7b82f1335f7a4b`;
6. require durable dual-16385 resource authority `CLASSIV_HISTORY_SUPPRESSED_16385_DUAL_RESOURCE_PILOT_V0_1` before execution.

No change is allowed to tolerance, derivative step, estimator, physical support, masks, accounting, request-plan hashes or pass/fail semantics.

## Lifecycle
Exactly eight CLASS constructions: four coarse roles and four fine roles, role-major/sequential, maximum one live instance, final live count zero, no cross-process raw-operand combination. Total inherited `get_transfer` calls = 4040.

## Terminal closure classification
Use the same classification logic as the already frozen dormant fresh-closure lineage:
- structural/provenance failure → `INVALID_INFRA_PLUS_0_PLUS_0`;
- structurally valid but fresh numerical convergence no longer `<1e-3` → numerical unresolved closure, not physical FAIL;
- numerically converged but frozen Layer-B physical support requirements fail → scientific physical-support FAIL;
- numerically converged and frozen physical support requirements pass → physical-support PASS candidate.

A workflow green status is never sufficient by itself; terminal artifact must be independently consumed against a pre-result validator.

## NOT_CONVERGED branch
This spec grants **no** authority to create 32769 or any other denser rung. Repository audit frozen before the current result found no prospectively frozen 32769 successor. A future denser rung would require a separate prospective scientific justification and preregistration, not a post-result rescue.
