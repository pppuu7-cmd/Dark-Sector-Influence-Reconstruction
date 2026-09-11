# DSIR current-process ledger

Updated: 2026-09-11. Scope: **DSIR only**; KMDSB/RTK/RQIR excluded.

## Scientific frontier
Canonical 8193->16385 is independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened; no 32769 execution is authorized.

## Completed post-16385 root-cause stage
Workflow/run/head: `layerb-post-16385-plateau-rootcause-v0-2 / 34577119805 / 257ddd3bf3310a8913deb6c60d078a6ac5d4211c` is **TERMINAL AND CONSUMED**.

- static control `103192003676 / artifact 10190073447`: `POST_16385_CANONICAL_INTERPOLATION_CONTROL_PASS_PLUS_0_PLUS_0`; ZIP SHA256 `42ae9f7f454271782492ab3af81f2f5db6f0a2e51e70646e59e3747d25e90a72`; result SHA256 `56f9d53c014d868b92d1ffab98b83508b440a2bbb7fa2fd43bc5bef4980332ea`; only 2 exact binary64 shared nodes, analytic cross-grid interpolation controls <=`8.881784197001252e-16`.
- raw localization `103192003971 / artifact 10191158698`: `POST_16385_FIXED_NODE_RAW_LOCALIZATION_PASS_PLUS_0_PLUS_0`; ZIP SHA256 `7425f42b37198f5fee7bdddfa71758f574a12a5e666ddac9812d5ce280c209a3`; result SHA256 `9b458393930bd6b1ca609cb5de2cd5ede97332c84835de75b473c5d97ebc0633`; max raw cross-grid symmetric-relative difference `1.5949311416969764e-10`, unsupported=0, lookup <=`1.657034302538322e-16`, 4 constructions/max-one-live/final-zero on both grids.
- cancellation conditioning `103192003878 / artifact 10190966126`: `POST_16385_FIXED_H_CANCELLATION_AUDIT_PASS_PLUS_0_PLUS_0`; ZIP SHA256 `a53f1857fb6a27010fde82ae5884104385b63e8d567db2c48ca892c33a33bfc6`; result SHA256 `341f25fb6d20e3e1d5e8c733de30c8c1a17024fdd3822de01aa32ebf8b2ed3f9`; h=`1e-4`, max cancellation amplification indicator `465188.89721799345`, but max cross-grid response-relative difference at the preregistered requests is only `5.808781687987132e-06`.

Combined durable authority: `docs/dsir4/authority/LAYERB_POST_16385_ROOTCAUSE_DIAGNOSTICS_V0_1.json`, commit `8dd712368fcfc0d530945a5196af8693979294fe`.

## Interpretation
The fixed five-node diagnostic does not reproduce the percent-scale full-traversal plateau. Strong cancellation exists, but measured local raw cross-grid discrepancies remain far too small at those requests to explain `0.012484060640679777`. Ordinary cross-VM nondeterminism is already strongly disfavored, and centered-cubic arithmetic on smooth controls is machine-precision accurate. Broader response-blind localization is justified; no denser science rung is authorized.

## Prospectively frozen next support process
Plan: `docs/dsir4/prereg/LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_PLAN_V0_1.md`, commit `4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6`.
State: **PREREGISTERED, EXECUTION NOT YET LAUNCHED**.
Frozen selection: 15 uniform interior canonical-8193 index quantiles `[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]`; same two z anchors, four roles, h, interpolation and pinned solver stack. Both planned lanes remain +0/+0 and cannot authorize 32769/covariance/Wm_S3.
Exact next action: implement and launch `broad-raw` and `broad-conditioning` in parallel, then independently consume artifacts.

## Runner ownership
Useful hosted lanes: **0 currently active**. No home runner ownership. Stale queued self-hosted run/job `34550495778 / 103112190909` is superseded and must not receive home-runner ownership.

## Recovery authority
Newest immutable note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_POST16385_ROOTCAUSE_V116.md`.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** under the stable rubric.
