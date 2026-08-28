# DSIR checkpoint — actual Exp073P aggregate join route ready; R1 queued

**Date:** 2026-08-29 02:24 EEST  
**Scope:** manual continuation while the canonical self-hosted R1 executor is
waiting for its runner.

## Executive state

The sole canonical Exp073R1 v0.6 Stage-B execution remains:

- run `33212521957`;
- job `98988824629`, `metacal-map-longrun`;
- head `79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`;
- workflow
  `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`.

At this checkpoint the job is still `queued` and has no artifact.  The state is
`BLOCKED_EXP073R1_SELF_HOSTED_RUNNER_AVAILABILITY`: an infrastructure/liveness
block, not a reproduction failure and not a scientific failure.  No duplicate
heavy run was dispatched.

The previously missing execution route for the real Exp073P aggregate
prerequisite join is now prospectively frozen, implemented and synthetically
validated.  It has not been dispatched on real evidence.

## Preregistration chronology

Before production implementation and before any terminal R1 output, commit
`df9a9b06b01d1c81bbc64e58495772676872c6f1` added

`experiments/073p_actual_aggregate_join_execution_route_prereg_v0_1.md`.

It freezes:

- the sole admitted R1 run/job/head/workflow/artifact name;
- explicit future R1 artifact-ID and digest inputs, independently checked
  against the live GitHub API;
- manual dispatch only for the production workflow;
- read-only `contents` and `actions` permissions;
- complete ten-parent metadata collection with pagination closure;
- the unchanged PASS/REJECTED/INCOMPLETE taxonomy;
- all no-science/no-downstream-leakage fields;
- the unchanged physical rectangle, threshold, dimension and gate order.

The preregistration SHA256 is
`159407c5f5143e859114dc70d6d9c2284a0321c5be61fbae61ca275e9d066fa1`.

## Implemented execution route

Commit `0f9173eaf67925eeabceee9c27b6120f301aeec9` added:

1. `ci/exp073p_actions_metadata_bundle_v0_1.py`;
2. `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-1.yml`;
3. `.github/workflows/exp073p-aggregate-prerequisite-join-route-selftest-v0-1.yml`.

The collector retrieves the live run, job and artifact lists for all ten
parents frozen by the existing aggregate evaluator.  It requires complete API
pagination, normalizes the exact evaluator schema, validates the supplied R1
artifact ID/digest against the unique live artifact, and then invokes the
existing metadata validator.  It does not download science arrays or evaluate
support.

The real workflow:

- has `workflow_dispatch` only; no push, schedule or automatic downstream
  trigger;
- verifies frozen SHA256 values of the preregistration, metadata collector and
  existing aggregate evaluator before reading live evidence;
- accepts the future R1 artifact ID/digest only as assertions, never as
  authority by themselves;
- downloads the exact large-source, large-metacal, P2 and canonical R1
  artifacts by frozen run/name bindings;
- uses the byte-frozen committed preflight, S0 and BOSS records;
- calls the unchanged aggregate evaluator with explicit `--classifying`, whose
  scope is only the prerequisite join;
- uploads PASS, REJECTED or INCOMPLETE receipts and leaves non-PASS executions
  unsuccessful.

The production route must remain unrun until R1 is terminal and genuine.

## Synthetic route CI

Push of the implementation started only the separate synthetic self-test:

- run `33220212976`;
- job `99012479309`, `synthetic-route-selftest`;
- conclusion `completed/success`;
- artifact ID `9704867271`;
- artifact name
  `exp073p-actions-metadata-route-synthetic-selftest-0f9173eaf67925eeabceee9c27b6120f301aeec9`;
- artifact digest
  `sha256:25f242b3385842a8506b6d80985c033559297ee15820b8d0df1ce7b84c46fa64`;
- internal status
  `PASS_EXP073P_ACTIONS_METADATA_ROUTE_SYNTHETIC_SELFTEST_V0_1`.

The downloaded ZIP digest was independently checked against the Actions API.
Its receipt binds ten parents and ten fail-closed mutations, including
run/head/status drift, missing jobs, duplicate/missing/expired R1 artifacts,
R1 ID/digest disagreement and truncated pagination.

The synthetic receipt explicitly states:

- `support_executor_authorized=false`;
- `real_join_status_emitted=false`;
- `scientific_classification=null`;
- every support/covariance/nuisance/relation/held-out/G8 read flag is false;
- G7, G8 and G9 remain OPEN.

## Local and repository regression

- metadata-route synthetic self-test: PASS;
- full repository suite: `44 passed`;
- Python compileall: PASS;
- both new workflow YAML files parse: PASS;
- `git diff --check`: PASS.

Machine-readable audit:
`data/derived/g7/exp073p_actual_join_route_readiness_audit_v0_1.json`.

## Scientific interpretation

This iteration closes an execution-readiness gap only.  It supplies no evidence
for or against dark-sector physics.  Real R1 reproduction, the real aggregate
prerequisite join, Exp073P physical support, covariance/whitening, nuisance
rank, quotient/relation/null and G8 were not evaluated.

The frozen scientific contract remains:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- positive absolute final-response support envelope while Wm production
  remains signed;
- tails outside the rectangle remain invalid;
- no crop-before-normalization, effective ell, fiducial-P/model weighting,
  post-hoc cuts or covariance/SVD/relation/held-out leakage.

## Exact continuation order

1. Bring the configured self-hosted Linux runner online; preserve the single
   queued run `33212521957` and do not duplicate it.
2. On terminal completion, require Actions success and the exact internal
   `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` with every frozen
   byte/hash/row/mapper/selection/repeatability/R0/no-leakage control.
3. If interrupted, record only `INCOMPLETE_EXP073R1`; never reuse partial masks.
4. After genuine PASS, freeze the returned R1 artifact ID/digest as the two
   production-workflow dispatch inputs and manually run
   `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-1.yml`.
5. Require real `PASS_EXP073P_PREREQUISITE_BINDING_V0_1` before starting the
   separately preregistered physical-support executor.
6. Require real
   `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P` before opening
   covariance/whitening.
7. Continue strictly with nuisance SVD/rank -> quotient/relation/null -> fresh
   G8 withheld family.

G7, G8 and G9 remain OPEN.
