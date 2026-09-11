# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_POST16385_ROOTCAUSE_V116.md`, creation commit `a724594d203d7d007bdad53929eb6a90eb4bae1e`. V115 and all earlier recovery notes remain immutable history; V116 supersedes them for current-front recovery.

## Scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened. No 32769 execution is authorized.

## Newly closed diagnostics
Repaired run `34577119805`, head `257ddd3bf3310a8913deb6c60d078a6ac5d4211c`, is fully terminal and consumed.
- static `103192003676 / 10190073447`: exact shared-node count 2; smooth centered-cubic cross-grid control <=`8.881784197001252e-16`.
- raw `103192003971 / 10191158698`: classification `POST_16385_FIXED_NODE_RAW_LOCALIZATION_PASS_PLUS_0_PLUS_0`; ZIP SHA256 `7425f42b37198f5fee7bdddfa71758f574a12a5e666ddac9812d5ce280c209a3`; result SHA256 `9b458393930bd6b1ca609cb5de2cd5ede97332c84835de75b473c5d97ebc0633`; max raw 8193-vs-16385 symmetric-relative difference `1.5949311416969764e-10`; unsupported=0; lookup <=`1.657034302538322e-16`; exact lifecycle preserved.
- conditioning `103192003878 / 10190966126`: classification `POST_16385_FIXED_H_CANCELLATION_AUDIT_PASS_PLUS_0_PLUS_0`; ZIP SHA256 `a53f1857fb6a27010fde82ae5884104385b63e8d567db2c48ca892c33a33bfc6`; result SHA256 `341f25fb6d20e3e1d5e8c733de30c8c1a17024fdd3822de01aa32ebf8b2ed3f9`; max cancellation amplification indicator `465188.89721799345`; max cross-grid response-relative difference at the preregistered requests `5.808781687987132e-06`; no alternative h evaluated.

Durable combined authority: `docs/dsir4/authority/LAYERB_POST_16385_ROOTCAUSE_DIAGNOSTICS_V0_1.json`, commit `8dd712368fcfc0d530945a5196af8693979294fe`.

## Current interpretation
The five-node response-blind controls do not reproduce the percent-scale `0.012484060640679777` full-traversal plateau. Strong finite-difference cancellation exists, but the measured local raw cross-grid discrepancies remain too small at those requests to amplify to plateau scale. Ordinary cross-VM nondeterminism remains strongly disfavored; non-nesting plus centered-cubic arithmetic alone is insufficient. This ranks broader deterministic localization above another blind resolution increase.

## Current support process
Prospectively frozen plan: `docs/dsir4/prereg/LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_PLAN_V0_1.md`, commit `4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6`. It fixes 15 uniform interior canonical-8193 quantile indices before execution and preserves the same two z anchors, four roles, h=1e-4, interpolation and pinned solver stack. Planned broad-raw and broad-conditioning lanes are support-only +0/+0 and cannot authorize 32769, covariance restriction or Wm_S3.

Execution state: preregistered, not yet launched.

## Runner ownership
No useful hosted lane is currently in progress. No home runner ownership. Stale superseded self-hosted run/job `34550495778 / 103112190909` must not receive ownership.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** under the stable repository rubric.

## Exact next action
Implement and launch the two prospectively frozen broad-quantile support lanes in parallel, then independently consume their artifacts. Do not rerun the full 8193->16385 scientific traversal and do not execute 32769.
