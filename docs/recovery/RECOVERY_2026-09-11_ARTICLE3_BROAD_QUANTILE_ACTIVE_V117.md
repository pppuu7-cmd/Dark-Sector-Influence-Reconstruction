# DSIR recovery — Article III broad quantile localization V117

Date: 2026-09-11. Scope: DSIR only.

## Preserved scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen REL_TOL=1e-3, h=1e-4, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction <=0.05, retained >=15, unsupported=0 and lookup <=1e-12 are unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened; no 32769 science execution is authorized.

## Prior root-cause authority
V116 and `docs/dsir4/authority/LAYERB_POST_16385_ROOTCAUSE_DIAGNOSTICS_V0_1.json` remain authoritative for the completed five-node controls. Those controls showed machine-precision analytic interpolation behavior, max raw cross-grid difference `1.5949311416969764e-10`, and max frozen-h cross-grid response difference `5.808781687987132e-06`; they did not reproduce the full-traversal plateau.

## Frozen broad support plan
Plan `docs/dsir4/prereg/LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_PLAN_V0_1.md`, commit `4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6`, fixes 15 uniform interior canonical-8193 indices `[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]`, the same two z anchors, four roles, h=1e-4 and pinned solver/interpolation stack. Both lanes are support-only +0/+0.

Implementation helper: `ci/layerb_post_16385_broad_quantile_localization_v0_1.py`, creation commit `799bdf1c916d2a5777bc21e95103474c8676c0ac`.

## Attempt 1 infrastructure-only failure
Workflow/run `layerb-post-16385-broad-quantile-localization-v0-1 / 34585571329`, head `104b40827002134796ab3c980fc09d51aa6930ee`, jobs `103218877133` broad-raw and `103218877333` broad-conditioning, both failed before numerical-stack installation at the identity gate. Cause: path-history guards used `git log` under the default shallow `actions/checkout` fetch depth, so older file creation commits were not available locally. No CLASS execution occurred and no scientific artifact was created. Classification: infrastructure/software +0/+0.

## Minimal repair and active execution
Repair is workflow-only: add `fetch-depth: 0` to checkout; frozen science/helper/plan are unchanged.

Repaired workflow/run: `layerb-post-16385-broad-quantile-localization-v0-2 / 34585873905`, head `ef7f12195b4bc491c09f107fcba58e2bdf350881`.
- broad-raw job `103219830602`: IN_PROGRESS on GitHub-hosted ubuntu-24.04; setup, full checkout and frozen identity gate PASS; numerical/build stack stage entered.
- broad-conditioning job `103219831011`: IN_PROGRESS on a separate GitHub-hosted ubuntu-24.04 runner; setup, full checkout and frozen identity gate PASS; numerical/build stack stage entered.
- no home runner ownership.

Independent no-CLASS static contract audit workflow was launched at commit `b5300df08e8a313e781811940438af345302f13c`; it checks exact 15-index selection, tokens and closed downstream authorities without reading scientific responses.

## Anti-duplication / no-idle state
Exactly two numerical broad-quantile lanes are active and independent. Do not launch duplicates. Use other available runner capacity only for independent static/provenance/response-blind work that cannot bias these frozen outputs. Stale superseded self-hosted run/job `34550495778 / 103112190909` must not receive home-runner ownership.

## Readiness
ARTICLE3_REPOSITORY_READINESS: 68%. Funnel-freeze readiness: 67%.

## Exact next action
Consume broad-raw and broad-conditioning artifacts independently when terminal; verify artifact hashes, exact 15-index/z identities, 4-construction/max-one-live/final-zero lifecycles, unsupported=0, lookup<=1e-12 and no downstream authorization. If broad response differences remain orders below `0.012484060640679777`, freeze the next response-blind diagnostic around z/row aggregation or edge/stencil structure before execution. If a large deterministic hotspot appears, preregister any follow-up before execution. Do not rerun the full 8193->16385 traversal and do not execute 32769.
