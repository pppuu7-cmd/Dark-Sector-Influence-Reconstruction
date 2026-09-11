# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_POST16385_ROOTCAUSE_V115.md`, creation commit `f6a24b17104acabd31ae6c8a747d7f0b23b19dea`. V114 and all earlier recovery notes remain immutable history; V115 supersedes them for current-front recovery.

## Scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened. No 32769 execution is authorized.

## Current diagnostic process
Frozen support-only plan: `docs/dsir4/prereg/LAYERB_POST_16385_PLATEAU_ROOTCAUSE_PLAN_V0_1.md`, commit `95cf0a3bb217a49cf3e683ed4134613bec51f5d3`.

Initial run `34576898342` was infrastructure/software +0/+0 because the diagnostic helper incorrectly required exact 8193⊂16385 nesting. Minimal repair commit `f23ed0d16fb7b54bb812bb91c9e0e8a8e04cf171` removes only that mistaken prerequisite and measures nesting instead; no science setting changed.

Repaired run `34577119805`, head `257ddd3bf3310a8913deb6c60d078a6ac5d4211c`:
- static job `103192003676` is terminal and independently consumed; artifact `10190073447`, ZIP SHA256 `42ae9f7f454271782492ab3af81f2f5db6f0a2e51e70646e59e3747d25e90a72`, result SHA256 `56f9d53c014d868b92d1ffab98b83508b440a2bbb7fa2fd43bc5bef4980332ea`, classification `POST_16385_CANONICAL_INTERPOLATION_CONTROL_PASS_PLUS_0_PLUS_0`;
- exact full every-other nesting is false and the two canonical arrays share only 2 exact binary64 nodes; the five fixed 8193 diagnostic targets are not exact 16385 members, with nearest relative coordinate mismatch about `4.96e-5..1.984e-4`;
- centered-cubic synthetic smooth/log-cubic residual controls remain at machine precision, max cross-grid difference `8.881784197001252e-16`;
- raw-localization job `103192003971` and cancellation-conditioning job `103192003878` are still in progress and must be terminal-consumed independently.

All diagnostic outcomes remain +0/+0 and cannot authorize 32769, covariance restriction or Wm_S3.

## Runner ownership
Two useful GitHub-hosted diagnostic lanes are active. No home runner ownership. Stale superseded self-hosted run/job `34550495778 / 103112190909` must not receive ownership.

## Retained interpretation
Ordinary cross-VM nondeterminism remains strongly disfavored by earlier reproducibility controls. The new static control establishes that canonical 8193 and 16385 grids are not exact nested refinements, while independently showing that the centered-cubic formula itself is machine-precision accurate on smooth analytic controls at the frozen selected requests. The active raw/conditioning lanes are required before ranking deterministic solver-grid sampling versus finite-difference amplification more strongly.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** under the stable repository rubric.

## Exact next action
Consume raw-localization `103192003971` and cancellation-conditioning `103192003878` as soon as terminal; verify artifact hashes/provenance/lifecycle and combine only as support-only root-cause evidence. Do not rerun the full 8193->16385 scientific traversal and do not invent or execute 32769.
