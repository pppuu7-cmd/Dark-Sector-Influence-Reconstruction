# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IU_PASS_IR_RETRY_RUNNING_V57.md`, creation commit `4982a692fd3f5728a7b7a60a83817199c6b96f5c`.

## Preserved authority / newly closed
- All prior admitted DSIR scientific authority remains preserved. Article-3 Exp073IQ Layer-A PASS: `34423479633 / 102703685034`, artifact `10131794281`, SHA256 `ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, 107 retained rows.
- Original Exp073IR `34428699659 / 102719344981`: `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`, not scientific FAIL; no exact public `d_m`.
- Exp073IS `34431475914 / 102727713276`: support-only `+0/+0`; pinned public writer does not expose `d_m`, so `d_tot` alias forbidden.
- Exp073IT `34431545882 / 102727918512`: raw-log PASS `SUPPORT_PLUS_0_PLUS_0`, exact safe source target `index_tp_delta_m <- ppw->delta_m`.
- Exp073IU primary `34431740917 / 102728498891`, head `34f5c9640cd87c68df68d573538e1fa18dceef76`: raw-log PASS `SUPPORT_PLUS_0_PLUS_0`, exact token `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1`; exact pinned source/hash/patch/build/import verified, no cosmology. Redundant hosted runs `34431769157 / 102728585401` and `34431885548 / 102728934900` also PASS but are duplicate `+0/+0` evidence only.

## Current authoritative process — repaired Exp073IR
- workflow: `exp073ir-article3-real-layerb-common-response-v0-1`;
- run ID: `34432102035`;
- job ID: `102729564736`;
- head/launch commit: `38604061abe6cbcccbf9614b22e3ca0ca6a9ec0f`;
- implementation-control v0.2: `3f1b819ac291f3cf217fd28bb2dd51c351f3c82b`;
- workflow interface-repair commit: `2b1befe68791e51088aeae170ac435b21dce125f`;
- exact IU patch script commit: `e2e36bcb81cf3f34ecb079f57b14c94ccbe590da`;
- runner: GitHub-hosted `ubuntu-24.04`;
- home/self-hosted ownership: none; home runner free;
- checkpoint namespace / last durable checkpoint: N/A;
- current state at latest live inspection: IN_PROGRESS;
- observed stage: prospective lineage completed; frozen numerical/build stack installation running;
- expected accounting status: exactly one of `PASS_PHYSICAL_SUPPORT_ARTICLE3`, `FAIL_PHYSICAL_SUPPORT_ARTICLE3`, `NUMERICALLY_UNRESOLVED_EXP073IR`, `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`.

The repair changes only exposure of the already-existing gauge-invariant `index_tp_delta_m <- ppw->delta_m` as public `d_m` while preserving separate `d_tot`; the frozen numerical script, h=1e-4, response directions, interpolation, physical domain, parent 107 rows, Layer-B threshold `<=0.05`, retained minimum 15 and downstream covariance firewall are unchanged.

### Exact next transitions
SUCCESS/workflow terminal: download and inspect artifact and raw log; independently verify artifact digest/provenance. Workflow success alone is not scientific PASS. `PASS_PHYSICAL_SUPPORT_ARTICLE3` is admitted only if invalid-row fraction `<=0.05`, retained-after-Layer-B `>=15`, convergence PASS and anti-leakage/covariance firewall checks are intact; then freeze/launch the separately permitted covariance-restriction gate. `FAIL_PHYSICAL_SUPPORT_ARTICLE3` is a scientific negative result and must be preserved. `NUMERICALLY_UNRESOLVED_EXP073IR` is unresolved under exact contract. `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT` or build/runtime/source/provenance error triggers first-cause infrastructure diagnosis and smallest prospective repair, never a science change.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.