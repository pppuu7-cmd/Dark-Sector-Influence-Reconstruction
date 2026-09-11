# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_CANCELLATION_DIAGNOSIS_CLOSED_TOP64_RETRY_ACTIVE_V124.md`, creation commit `63ceb148870ab75c0057a223e8c7142eaa4a0fbd`. The two concurrently created V123 notes and all earlier recovery notes remain immutable history; V124 reconciles and supersedes them for current-front recovery.

## Scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. No 32769 execution is authorized; covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Closed top-1 cancellation diagnosis
Exact-hotspot/top-1 authority remains support-only `+0/+0`. Two additional independent support packages are now terminal and durable:

- `LAYERB_POST_16385_TOP1_PARALLEL_SUPPORT_TERMINAL_AUTHORITY_V0_1.json`, creation commit `d46ae6e2175502ed9b74444dc8f91fdc48cedb05`: beta-response discrepancy `0.012484060640679777` is `181304493.09733495` times the largest raw-role relative cross-grid shift; ±1 ULP perturbations of the already-rounded endpoint response values move the metric by at most `2.8622937353617317e-16`.
- `LAYERB_POST_16385_TOP1_DECOMPOSITION_ARITHMETIC_TERMINAL_AUTHORITY_V0_1.json`, creation commit `4392df8fe76680ee6e4bfed7e073263e4729e39f`: beta subtraction condition numbers are `207066036.01189664` on 8193 and `204481011.0632948` on 16385; exact Decimal replay from stored binary64 role operands has zero subtraction replay rounding-relative error and signed role shifts exactly reproduce the beta-numerator shift.

Combined interpretation: the local hotspot is strongly ill-conditioned and exhibits finite-difference cancellation amplification; ordinary endpoint binary64 rounding and ordinary arithmetic rounding of the subtraction do not explain the plateau. This is diagnostic support only and changes no scientific gate.

## Top-64 census retry
Attempt 1 of run `34614119149` remains infrastructure/numerical-reproducibility FAIL `+0/+0` at atom-0 exact reproduction. The single permitted unchanged retry is run attempt 2, job `103331912096`, launch head `6b684ac91c7a261e6b588da1a4922a411bd65614`; at the V124 update it remains **IN_PROGRESS**. No duplicate top-64 run is authorized.

If retry PASSes, independently consume/hash all artifacts and enforce exact source/provenance identity, 64 ordering, lifecycle `8/max1/final0`, unsupported=0, lookup `<=1e-12`, every primary reproduction error `<=1e-12`, and downstream-closed flags. If reproduction fails again, stop retries and classify the census BLOCKED by hosted numerical reproducibility; freeze a separate support-only cross-VM reproducibility diagnostic instead of relaxing the gate.

`DSIR Continuous Research` remains enabled hourly and aligned with this same repository-first, fail-closed, anti-idle front.

Stale superseded self-hosted run `34550495778 / 103112190909` must not receive home-runner ownership.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**.

## Exact next action
Track only the single unchanged top-64 retry `34614119149 / 103331912096`. On terminal state, consume and independently verify its artifact in the same iteration. Never execute 32769, covariance restriction or Wm_S3, and never alter frozen science to rescue this support gate.
