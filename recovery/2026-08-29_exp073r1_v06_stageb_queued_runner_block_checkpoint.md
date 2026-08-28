# DSIR checkpoint — canonical Exp073R1 v0.6 Stage-B queued on self-hosted runner

**Date:** 2026-08-29 02:15 MSK
**Scope:** autonomous continuation from current `main`; G7 execution-liveness/provenance check only.

## Authoritative state

- repository head inspected before this checkpoint: `accc1e81b68764eb9a60cb7d273ccbd6ef2480d6`;
- sole canonical Exp073R1 heavy authority: workflow run `33212521957`;
- canonical job: `98988824629`, `metacal-map-longrun`;
- workflow head: `79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`;
- workflow: `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`;
- current run state observed through the GitHub Actions API: `queued`;
- current repository-wide `in_progress` Actions count: `0`;
- repository-wide `queued` Actions count: `1`, exactly the canonical run above.

The earlier combined v0.6 run `33212040452` is terminal `cancelled`; its Stage-A job passed but its self-hosted Stage-B job was cancelled. It is not authority for Exp073R1 and must not supply a terminal R1 result.

## Classification

`BLOCKED_EXP073R1_SELF_HOSTED_RUNNER_AVAILABILITY`

This is an **infrastructure/execution-liveness block**, not a reproduction FAIL and not a scientific FAIL. No partial mask, support fraction, retained dimension, covariance quantity, nuisance rank, quotient/null statistic, held-out result or G8 quantity was read or computed in this continuation.

The queued state does not justify a duplicate heavy dispatch. The correct action is to preserve the single canonical run and allow it to start when a runner matching `[self-hosted, linux]` is available.

## Downstream readiness confirmed while blocked

The next non-science transition has already been prepared prospectively:

- Exp073P aggregate prerequisite evaluator preregistration: `c947a30cdcc1457c72e2501c6030f003ca9f037d`;
- implementation: `6d32ce32d16c33d3731031d543776e2045eb8115`;
- synthetic CI run `33217294341`: `completed/success`;
- synthetic internal status: `PASS_EXP073P_AGGREGATE_JOIN_SYNTHETIC_SELFTEST_V0_1`;
- real-parent compatibility audit: PASS;
- `support_executor_authorized=false` until genuine canonical R1 PASS is bound into the real join.

No real aggregate join may run before the canonical R1 artifact is terminal, unique, non-expired, digest-bound, and internally validates as `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` under the frozen R1-to-P interlock.

## Frozen boundaries unchanged

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- positive absolute final-response support envelope while production Wm remains signed;
- tails outside the common rectangle remain invalid;
- no crop-before-normalization, effective-ell substitution, fiducial-P/model weighting, post-hoc support cuts, covariance/SVD/relation/held-out leakage.

## Exact continuation order

1. Do not duplicate run `33212521957` while it remains queued.
2. When it starts, monitor the exact canonical job only.
3. On terminal completion, require both Actions `completed/success` and the exact internal R1 PASS plus all frozen identity, row-count, mapper, selection, repeatability, R0-parent and no-leakage controls.
4. If interrupted or cancelled, record `INCOMPLETE_EXP073R1`; never promote partial outputs.
5. On genuine PASS, freeze the returned R1 artifact ID/digest into the real Exp073P aggregate prerequisite join and require `PASS_EXP073P_PREREQUISITE_BINDING_V0_1`.
6. Only then run the separately frozen Exp073P physical-support evaluator.
7. Only genuine Exp073P support PASS may open covariance restriction/whitening; nuisance SVD/rank, quotient/relation/null and fresh G8 follow strictly afterward.

G7, G8 and G9 remain OPEN.
