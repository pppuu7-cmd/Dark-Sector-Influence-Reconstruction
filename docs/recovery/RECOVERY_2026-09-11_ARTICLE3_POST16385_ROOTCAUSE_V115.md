# DSIR recovery V115 — post-16385 plateau/root-cause diagnostics

Date: 2026-09-11. Scope: **DSIR only**. This note is immutable after creation.

## Preserved scientific authority
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. Covariance restriction is unauthorized; Wm_S3 is closed; 32769 is not authorized.

Authoritative terminal science-support run/job/artifact remains `34555022975 / 103125734913 / 10186753737`, durable authority `docs/dsir4/authority/LAYERB_CANONICAL_8193_TO_16385_NOT_CONVERGED_V0_1.json`.

## Frozen diagnostic plan
Support-only plateau/root-cause plan: `docs/dsir4/prereg/LAYERB_POST_16385_PLATEAU_ROOTCAUSE_PLAN_V0_1.md`, creation commit `95cf0a3bb217a49cf3e683ed4134613bec51f5d3`. It permits only response-blind fixed-node raw localization, fixed-h `h=1e-4` cancellation conditioning, and canonical nesting/interpolation controls. Every outcome is +0/+0 and cannot authorize a denser rung, covariance restriction or Wm_S3.

## Initial implementation infrastructure failure
Initial helper commit `b3e14ed80d79e300ab90125d3cf48c9565ed424a`; initial workflow commit/head `d7430955a9b4ef84c9326455f6b92da0046cb4b8`; run `34576898342`.
Jobs: static `103191314779`, raw `103191314776`, conditioning `103191314658`.
All three terminated before producing valid diagnostic artifacts with the same first causal error: `RuntimeError: canonical nesting mismatch`. The helper had incorrectly made exact `8193 == 16385[::2]` nesting a prerequisite although the frozen diagnostic plan requires nesting to be measured. This is `INVALID_INFRA/SOFTWARE_PLUS_0_PLUS_0`; it is not a scientific or numerical failure and does not alter historical science.

## Minimal prospective repair
Only the diagnostic assumption was repaired. Commit `f23ed0d16fb7b54bb812bb91c9e0e8a8e04cf171`; repaired helper Git blob `49a2e1936cb6a63ac9fc4cce0fbea2b1bd40b900`.
The repaired helper keeps the same response-blind 8193 index selection `[1024,2048,4096,6144,7168]`, fixed JO z anchors and frozen four roles/h. It now measures exact shared-node membership, nearest 16385 coordinates, centered-cubic stencil identity and analytic residual controls rather than requiring nesting.

## Repaired run
Workflow commit/head `257ddd3bf3310a8913deb6c60d078a6ac5d4211c`; run `34577119805`.

### Static interpolation/nesting lane — independently consumed
Job `103192003676`; artifact `10190073447`.
Artifact ZIP SHA256 `42ae9f7f454271782492ab3af81f2f5db6f0a2e51e70646e59e3747d25e90a72`; `result.json` SHA256 `56f9d53c014d868b92d1ffab98b83508b440a2bbb7fa2fd43bc5bef4980332ea`.
Classification `POST_16385_CANONICAL_INTERPOLATION_CONTROL_PASS_PLUS_0_PLUS_0`.

Measured facts:
- exact full every-other nesting: false;
- exact binary64 shared-node count between the canonical 8193 and 16385 arrays: 2;
- none of the five preregistered 8193 fixed targets is an exact 16385 member;
- nearest-16385 relative coordinate mismatches at those targets range from about `4.9568e-5` to `1.98433e-4`;
- centered-cubic stencils are not binary64-identical at all five selected targets;
- deterministic log-cubic/smooth interpolation controls remain at machine precision, with maximum cross-grid control difference `8.881784197001252e-16`.
No CLASS solver or scientific result was read. No scientific authority or next-rung authority was created.

Interpretation allowed at this point: the two canonical lattices are genuinely non-nested, so deterministic solver-grid sampling can differ even at nominally corresponding refinement stages; however the centered-cubic interpolation formula itself does not reproduce an O(1e-2) discrepancy on smooth analytic controls. This is diagnostic evidence only, not causal proof.

### Still active at creation of this note
Raw-localization job `103192003971`: in progress. Exact terminal action: independently consume result/artifact and verify fixed request identities, lifecycle, unsupported/lookup and raw 8193-vs-16385 operand differences.
Cancellation-conditioning job `103192003878`: in progress. Exact terminal action: independently consume result/artifact and verify fixed `h=1e-4`, lifecycle, numerator scales and conditioning indicators.

## Runner ownership
Two useful GitHub-hosted diagnostic lanes are in progress. No home/self-hosted ownership is permitted. Stale superseded self-hosted run/job `34550495778 / 103112190909` remains forbidden from runner ownership.

## Readiness
`ARTICLE3_REPOSITORY_READINESS = 68%`; funnel-freeze readiness `67%` under the stable rubric. Support-only diagnostics do not themselves increment scientific readiness.

## Exact continuation
Consume both active repaired diagnostic jobs when terminal in the same iteration if possible. Combine evidence only under the frozen root-cause plan. Do not rerun full 8193->16385, do not change tolerance/h/grid/domain/masks/interpolation/estimator, and do not authorize 32769, covariance restriction or Wm_S3 from these +0/+0 diagnostics.
