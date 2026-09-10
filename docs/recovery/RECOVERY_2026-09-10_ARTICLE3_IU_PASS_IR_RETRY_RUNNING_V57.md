# DSIR recovery V57 — Exp073IU PASS; repaired Exp073IR Layer-B retry running

Date: 2026-09-10. Scope: DSIR only. Supersedes V56 as latest pointer; all prior recovery notes remain immutable history.

## Preserved authority
All earlier admitted DSIR scientific authority remains unchanged. Article-3 Exp073IQ Layer-A remains PASS: run/job `34423479633 / 102703685034`, artifact `10131794281`, digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, retained set 107.

The original Exp073IR run/job `34428699659 / 102719344981` remains `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`, not scientific FAIL. Artifact `10133682066`, ZIP SHA256 `6d84e6ab94ea66d9b9f857727b7e6089cfb4cacc60e141660cd713e42d30a876`, reported no exact public `d_m` key from pinned CLASS-IV. It created no Layer-B/covariance authority.

Exp073IS run/job `34431475914 / 102727713276` is support-only hypothesis rejection `+0/+0`: public transfer writer contains separate `d_tot/index_tp_delta_tot` but no `d_m/index_tp_delta_m`; aliasing `d_tot` to `d_m` is forbidden.

Exp073IT run/job `34431545882 / 102727918512`, head `cd8fb5e069bd8b404d15b04bea4c823e54ca90c8`, is raw-log PASS `SUPPORT_PLUS_0_PLUS_0` with token `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`. Exact safe target is the pre-existing gauge-invariant source `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;` at pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`, pre-patch `source/perturbations.c` blob `92a48331658c5941ed4eb43b0e98ee78e39b8385`.

## Newly closed — Exp073IU support PASS
Prospective prereg commit `5a752298f4fa6bd6b6f0e832d5754e7bfe2c2ea8`; deterministic patch-script commit `e2e36bcb81cf3f34ecb079f57b14c94ccbe590da`.

Primary authoritative support run/job `34431740917 / 102728498891`, head `34f5c9640cd87c68df68d573538e1fa18dceef76`, completed SUCCESS and its raw log was inspected. It verified exact pinned upstream/hash, exact one-time deterministic patch anchors, preserved internal `index_tp_delta_m <- ppw->delta_m`, distinct public `d_m`, preserved separate `d_tot`, full CLASS/Python build/import, and no cosmological execution. Exact terminal token: `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1`; classification `SUPPORT_PLUS_0_PLUS_0`.

Because immediate Actions registration lag caused an orchestration retrigger before the first run appeared, two additional hosted build/static runs also completed with the same raw PASS: `34431769157 / 102728585401`, head `7c4be1d6652ac4324290bb1c508ddb37b61ff96b`, and `34431885548 / 102728934900`, head `addf04e30ee08e163aa9fe74525cc8fde280c8fb`. They are redundant `+0/+0` evidence only and create no duplicate authority. No cosmological numerical result was computed in any IU run. Workflow concurrency was added at commit `150dc1d22237079645e435650b28c6ff576ab896`; no further IU run is permitted.

## Repaired Exp073IR implementation frozen prospectively
Implementation-control v0.2 was frozen at commit `3f1b819ac291f3cf217fd28bb2dd51c351f3c82b`. Existing Exp073IR workflow was changed only to bind the audited IU interface repair at commit `2b1befe68791e51088aeae170ac435b21dce125f`.

The scientific script `ci/exp073ir_article3_real_layerb_common_response_v0_1.py`, frozen response components, h=1e-4, parent 107 rows, production/dense native-k settings 10/20, ln(k) interpolation/no extrapolation, BOSS 64/128 Gauss-Legendre support, Layer-B invalid-row threshold <=0.05, retained dimension >=15 and downstream covariance firewall remain unchanged. The only new solver-interface behavior is to expose the already-computed exact gauge-invariant `index_tp_delta_m <- ppw->delta_m` as public `d_m`, while preserving `d_tot` separately.

## Current authoritative process — repaired Exp073IR
Trigger/head commit `38604061abe6cbcccbf9614b22e3ca0ca6a9ec0f`.
Workflow/run ID: `34432102035`.
Job ID: `102729564736`.
Runner: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership: none.
Checkpoint namespace: N/A (hosted deterministic Layer-B run).
State at note creation: IN_PROGRESS; lineage enforcement passed and frozen numerical/build stack installation had started.
Expected terminal classification is exactly one of `PASS_PHYSICAL_SUPPORT_ARTICLE3`, `FAIL_PHYSICAL_SUPPORT_ARTICLE3`, `NUMERICALLY_UNRESOLVED_EXP073IR`, `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT` from the frozen script/accounting gate.

### Exact next transition
When run `34432102035` becomes terminal, inspect raw job log and artifact, independently verify the artifact ZIP digest and provenance, and classify from the raw JSON. Workflow SUCCESS alone is insufficient. Only valid `PASS_PHYSICAL_SUPPORT_ARTICLE3` with Layer-B invalid-row fraction <=0.05, retained-after-Layer-B >=15, convergence PASS and covariance firewall intact can create Layer-B scientific support authority and authorize the next covariance restriction gate. A valid `FAIL_PHYSICAL_SUPPORT_ARTICLE3` is a scientific negative result. `NUMERICALLY_UNRESOLVED_EXP073IR` is unresolved under the exact contract. Any source/hash/build/runtime/interface/provenance defect is `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`/infrastructure and must be repaired prospectively without changing science.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.