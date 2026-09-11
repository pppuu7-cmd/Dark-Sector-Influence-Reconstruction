# DSIR current-process ledger

Updated: 2026-09-11. Scope: **DSIR only**; KMDSB/RTK/RQIR excluded.

## Scientific frontier
Canonical 8193->16385 is independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened; no 32769 execution is authorized.

## Completed root-cause support authority
Five-node post-16385 diagnostics are terminal and consumed under `docs/dsir4/authority/LAYERB_POST_16385_ROOTCAUSE_DIAGNOSTICS_V0_1.json` (commit `8dd712368fcfc0d530945a5196af8693979294fe`). They show analytic centered-cubic control <=`8.881784197001252e-16`, max raw cross-grid difference `1.5949311416969764e-10`, and max fixed-h response cross-grid difference `5.808781687987132e-06`; these do not reproduce the full `0.012484060640679777` plateau.

## Active process
Frozen plan: `docs/dsir4/prereg/LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_PLAN_V0_1.md`, commit `4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6`.
Implementation: `ci/layerb_post_16385_broad_quantile_localization_v0_1.py`, creation commit `799bdf1c916d2a5777bc21e95103474c8676c0ac`.
Frozen 15 canonical-8193 indices: `[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]`; same two z anchors, four roles, h=1e-4, native kpd20 and centered-cubic evaluation.

Initial workflow/run `layerb-post-16385-broad-quantile-localization-v0-1 / 34585571329`, head `104b40827002134796ab3c980fc09d51aa6930ee`, is terminal infrastructure/software +0/+0 before CLASS: shallow checkout made path-history identity tests unavailable. No science response or artifact authority was created.

Repaired workflow/run: `layerb-post-16385-broad-quantile-localization-v0-2 / 34585873905`, head `ef7f12195b4bc491c09f107fcba58e2bdf350881`.
- job `103219830602`, `broad-localization (broad-raw)`: **IN_PROGRESS** on GitHub-hosted ubuntu-24.04; setup/full checkout/identity gate PASS; numerical/build stage entered.
- job `103219831011`, `broad-localization (broad-conditioning)`: **IN_PROGRESS** on a separate GitHub-hosted ubuntu-24.04 runner; setup/full checkout/identity gate PASS; numerical/build stage entered.
- expected terminal tokens: `POST_16385_BROAD_QUANTILE_RAW_LOCALIZATION_PASS_PLUS_0_PLUS_0` and `POST_16385_BROAD_QUANTILE_CONDITIONING_PASS_PLUS_0_PLUS_0`.
- both remain support-only +0/+0 and cannot authorize 32769, covariance restriction, Wm_S3 or altered stopping rules.

## Independent validation / chaining
Static audit run `34585938900 / artifact 10193569682` is independently verified `POST_16385_BROAD_QUANTILE_STATIC_AUDIT_PASS_PLUS_0_PLUS_0`, 18/18 checks; ZIP SHA256 `8d88e5b0ca8983f90fdda73604a99fce7e32439a04cea00b6b565e6ba2fd9e80`, result SHA256 `275027c2701457700cc3e24c03ab43f701223e27dbd3f3808429b8942306e065`. Authority commit `bb16a22fe9d5601822019a8ae595deefc7c92908`.

Event-driven consumer commit `2c4cd115ca9c0822cb6aa6363cc01b121201ca09` is armed for this exact source head/run family. It only validates terminal artifacts and computes ratios to the full-traversal plateau; it cannot launch the next scientific branch.

## Runner ownership / anti-idle
Useful hosted numerical lanes: **2 in progress**. No home runner ownership. Do not duplicate either broad lane. Additional runner capacity may be used only for independent static/provenance/response-blind work that cannot inspect or bias partial broad outputs. Stale self-hosted run/job `34550495778 / 103112190909` remains superseded and must not receive ownership.

## Recovery authority
Newest immutable note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_BROAD_QUANTILE_ACTIVE_V117.md`, creation commit `3afea26985097c197a6f93de269dbe9582eef02c`. `docs/RECOVERY_LATEST.md` points to V117.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**.

## Exact next actions
1. Do not duplicate the active broad lanes.
2. On each terminal artifact, independently verify ZIP/result hashes, exact 15-index/z identities, lifecycle, unsupported/lookup and downstream-closed flags.
3. Let the event-driven consumer produce comparison ratios, but do not treat those ratios as an automatic scientific branch decision.
4. After both artifacts are independently consumed, prospectively freeze the next diagnostic according to the already-frozen decision boundary: z/row aggregation or edge/stencil structure if broad differences remain far below plateau; separately preregister hotspot follow-up if a large deterministic hotspot is found.
5. Do not rerun full 8193->16385 and do not execute 32769.
