# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_BROAD_PLUS_STENCIL_ACTIVE_V118.md`, creation commit `207e2aaae45010e6c457db1d46d0e657e10d492b`. V117 and all earlier recovery notes remain immutable history; V118 supersedes them for current-front recovery.

## Scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened. No 32769 execution is authorized.

## Closed post-16385 support diagnostics
Five-node root-cause controls remain authoritative under `docs/dsir4/authority/LAYERB_POST_16385_ROOTCAUSE_DIAGNOSTICS_V0_1.json`, commit `8dd712368fcfc0d530945a5196af8693979294fe`.

New response-blind stencil geometry census is independently verified `POST_16385_STENCIL_GEOMETRY_CENSUS_PASS_PLUS_0_PLUS_0`. Initial run `34586420903` was infrastructure/software +0/+0 at a shallow-history identity guard before computation. Minimal repair produced run `34586460549`, head `68fc951fd90cd74f6232ad813973da8119eb41a0`. Full job/artifact `103221704310 / 10193782924`: ZIP SHA256 `de6de7a539e4a599874bfc1eda47986bf57fc3052d1f9dd9de6bca36588037cb`, result SHA256 `16e1127f9e16cb1e21c8571f73b7c92d0beb907e1d81d4aec3a4c8066f1d93a0`. Edge job/artifact `103221704104 / 10193782592`: ZIP SHA256 `f69a4fbfb7bd4e746f1ae1d7e04869093f54f029d081cc6a0b37919665681de2`, result SHA256 `6c641bb466f80782c9c79e61e911a43a816163b687adb944729f5076408b95fc`. Durable authority: `docs/dsir4/authority/LAYERB_POST_16385_STENCIL_GEOMETRY_CENSUS_V0_1.json`, commit `dc4c545348f9c05d724b1f4b113977b5fe7c48ad`. This is support-only and opens no downstream science.

## Active broad-quantile support process
Prospectively frozen plan: `docs/dsir4/prereg/LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_PLAN_V0_1.md`, commit `4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6`. Exact indices `[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]`; same two z anchors, four roles, h=1e-4 and pinned interpolation/solver stack.

Active repaired workflow/run: `layerb-post-16385-broad-quantile-localization-v0-2 / 34585873905`, head `ef7f12195b4bc491c09f107fcba58e2bdf350881`.
- broad-raw job `103219830602`: IN_PROGRESS; frozen identity, stack and CLASS-IV build PASS; frozen lane executing.
- broad-conditioning job `103219831011`: IN_PROGRESS on a separate hosted runner; same prerequisite stages PASS; frozen lane executing.

## Runner ownership
Two useful GitHub-hosted numerical lanes are active. No home runner ownership. Stale superseded self-hosted run/job `34550495778 / 103112190909` must not receive ownership. Do not duplicate active broad lanes. No result-dependent successor is authorized until both broad artifacts are consumed.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** under the stable repository rubric.

## Exact next action
Consume broad-raw and broad-conditioning artifacts independently when terminal, verifying hashes, exact identities/selection, lifecycle, unsupported/lookup and closed downstream flags. If broad response differences remain orders below `0.012484060640679777`, prospectively freeze the next response-blind z/row-aggregation or edge/stencil-mechanism diagnostic before execution. If a large deterministic hotspot appears, preregister its follow-up before execution. Do not rerun full 8193->16385 and do not execute 32769.
