# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_BROAD_QUANTILE_ACTIVE_V117.md`, creation commit `3afea26985097c197a6f93de269dbe9582eef02c`. V116 and all earlier recovery notes remain immutable history; V117 supersedes them for current-front recovery.

## Scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened. No 32769 execution is authorized.

## Closed post-16385 diagnostics
Repaired five-node run `34577119805`, head `257ddd3bf3310a8913deb6c60d078a6ac5d4211c`, is fully terminal and consumed.
- interpolation static control: exact shared-node count 2; smooth centered-cubic cross-grid control <=`8.881784197001252e-16`.
- raw localization: max raw 8193-vs-16385 symmetric-relative difference `1.5949311416969764e-10`; unsupported=0; lookup <=`1.657034302538322e-16`.
- conditioning: max cancellation amplification indicator `465188.89721799345`; max cross-grid response-relative difference `5.808781687987132e-06`; no alternative h evaluated.
Combined authority: `docs/dsir4/authority/LAYERB_POST_16385_ROOTCAUSE_DIAGNOSTICS_V0_1.json`, commit `8dd712368fcfc0d530945a5196af8693979294fe`.

The five-node controls do not reproduce the percent-scale full-traversal plateau. Ordinary cross-VM nondeterminism and centered-cubic arithmetic alone remain disfavored as sufficient explanations.

## Active broad-quantile support process
Prospectively frozen plan: `docs/dsir4/prereg/LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_PLAN_V0_1.md`, commit `4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6`. Exact indices: `[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]`; same two z anchors, four roles, h=1e-4, interpolation and pinned solver stack. Both lanes are +0/+0 support-only.

Implementation helper: `ci/layerb_post_16385_broad_quantile_localization_v0_1.py`, commit `799bdf1c916d2a5777bc21e95103474c8676c0ac`.

Attempt v0.1 run `34585571329` failed before numerical execution because path-history guards used `git log` under default shallow checkout. This is infrastructure/software +0/+0; no CLASS response was produced. Minimal workflow-only repair adds `fetch-depth: 0`.

Active repaired workflow/run: `layerb-post-16385-broad-quantile-localization-v0-2 / 34585873905`, head `ef7f12195b4bc491c09f107fcba58e2bdf350881`.
- broad-raw job `103219830602`: IN_PROGRESS; identity/provenance gate PASS.
- broad-conditioning job `103219831011`: IN_PROGRESS on a separate hosted runner; identity/provenance gate PASS.

Independent static contract audit run `34585938900`, artifact `10193569682`, is independently verified PASS 18/18. ZIP SHA256 `8d88e5b0ca8983f90fdda73604a99fce7e32439a04cea00b6b565e6ba2fd9e80`; result SHA256 `275027c2701457700cc3e24c03ab43f701223e27dbd3f3808429b8942306e065`. Durable static authority: `docs/dsir4/authority/LAYERB_POST_16385_BROAD_QUANTILE_STATIC_AUDIT_V0_1.json`, commit `bb16a22fe9d5601822019a8ae595deefc7c92908`.

Event-driven terminal consumer: `.github/workflows/layerb-post-16385-broad-quantile-terminal-consumer-v0-1.yml`, commit `2c4cd115ca9c0822cb6aa6363cc01b121201ca09`. It validates terminal artifacts and computes discrepancy/plateau ratios only; it cannot select or launch a scientific successor.

## Runner ownership
Two useful GitHub-hosted numerical lanes are active. No home runner ownership. Stale superseded self-hosted run/job `34550495778 / 103112190909` must not receive ownership. Do not duplicate the active broad lanes.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** under the stable repository rubric.

## Exact next action
Consume broad-raw and broad-conditioning artifacts independently when terminal. If broad response differences remain orders below `0.012484060640679777`, prospectively freeze the next response-blind diagnostic around z/row aggregation or edge/stencil structure before execution. If a large deterministic hotspot appears, preregister any follow-up before execution. Do not rerun full 8193->16385 and do not execute 32769.
