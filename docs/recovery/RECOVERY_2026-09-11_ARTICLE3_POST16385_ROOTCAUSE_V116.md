# DSIR recovery — Article III post-16385 root-cause V116

Date: 2026-09-11. Scope: DSIR only.

## Preserved scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen REL_TOL=1e-3, h=1e-4, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, unsupported=0 and lookup <=1e-12 are unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened; no 32769 science execution is authorized.

## Root-cause run consumed
Repaired run `34577119805`, head `257ddd3bf3310a8913deb6c60d078a6ac5d4211c`, is fully terminal and independently consumed.

Static interpolation control: job/artifact `103192003676 / 10190073447`, ZIP SHA256 `42ae9f7f454271782492ab3af81f2f5db6f0a2e51e70646e59e3747d25e90a72`, result SHA256 `56f9d53c014d868b92d1ffab98b83508b440a2bbb7fa2fd43bc5bef4980332ea`, classification `POST_16385_CANONICAL_INTERPOLATION_CONTROL_PASS_PLUS_0_PLUS_0`. Canonical arrays share only 2 exact binary64 nodes, while analytic centered-cubic cross-grid controls remain <=8.881784197001252e-16.

Raw localization: job/artifact `103192003971 / 10191158698`, ZIP SHA256 `7425f42b37198f5fee7bdddfa71758f574a12a5e666ddac9812d5ce280c209a3`, result SHA256 `9b458393930bd6b1ca609cb5de2cd5ede97332c84835de75b473c5d97ebc0633`, classification `POST_16385_FIXED_NODE_RAW_LOCALIZATION_PASS_PLUS_0_PLUS_0`. At the prospectively selected five fixed k requests and two frozen z anchors, max raw symmetric-relative 8193-vs-16385 difference is `1.5949311416969764e-10`; lookup mismatch <=`1.657034302538322e-16`; unsupported=0; both grids preserve 4 constructions/max-one-live/final-zero.

Cancellation conditioning: job/artifact `103192003878 / 10190966126`, ZIP SHA256 `a53f1857fb6a27010fde82ae5884104385b63e8d567db2c48ca892c33a33bfc6`, result SHA256 `341f25fb6d20e3e1d5e8c733de30c8c1a17024fdd3822de01aa32ebf8b2ed3f9`, classification `POST_16385_FIXED_H_CANCELLATION_AUDIT_PASS_PLUS_0_PLUS_0`. Frozen h remains exactly `1e-4`; no alternative h evaluated. Maximum cancellation amplification indicator is `465188.89721799345`, but the independently calculated maximum cross-grid relative response difference at those preregistered requests is only `5.808781687987132e-06`, far below the full-traversal `0.012484060640679777` plateau.

Durable combined diagnostic authority: `docs/dsir4/authority/LAYERB_POST_16385_ROOTCAUSE_DIAGNOSTICS_V0_1.json`, creation commit `8dd712368fcfc0d530945a5196af8693979294fe`.

## Interpretation
The five-node fixed-request controls do not reproduce the percent-scale plateau. Strong finite-difference cancellation exists, but the measured local raw cross-grid differences are too small at these requests to be amplified to the observed full-traversal discrepancy. Ordinary cross-VM nondeterminism was already disfavored. Exact non-nesting and centered-cubic arithmetic alone are also insufficient. The evidence therefore justifies broader response-blind localization, not a denser science rung.

## Prospectively frozen next support step
`docs/dsir4/prereg/LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_PLAN_V0_1.md`, commit `4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6`, fixes 15 uniform interior canonical-8193 quantile indices before execution and preserves the same z anchors, four roles, h, interpolation, solver identities and +0/+0 governance. It cannot authorize covariance restriction, Wm_S3 or 32769.

## Live runner state
No useful hosted run is currently in progress. One stale superseded self-hosted run/job `34550495778 / 103112190909` remains queued and must not receive home-runner ownership.

## Readiness
ARTICLE3_REPOSITORY_READINESS: 68%. Funnel-freeze readiness: 67% under the stable rubric.

## Exact next action
Implement and launch the prospectively frozen broad quantile support lanes without changing science; then consume their artifacts independently. Do not rerun full 8193->16385 and do not execute 32769.
