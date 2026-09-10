# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority
All prior admitted DSIR authority remains preserved. Article-3 Exp073IQ Layer-A is PASS: `34423479633 / 102703685034`, artifact `10131794281`, digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, 107 retained rows.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IT_PASS_IU_BUILD_AUDIT_RUNNING_V56.md`, creation commit `67b2100d731198d98e7ae5bbfd77d0aed8b2ce2e`.

## Closed / classified
- Exp073IR `34428699659 / 102719344981`, head `dac55828f7d1e1e033769d9fd4e43079d224758b`: `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`, not scientific FAIL. Artifact `10133682066`, SHA256 `6d84e6ab94ea66d9b9f857727b7e6089cfb4cacc60e141660cd713e42d30a876`; exact cause: no public `d_m` key from pinned CLASS-IV.
- Exp073IS `34431475914 / 102727713276`: support-only hypothesis rejection `+0/+0`; public writer lacks `d_m/index_tp_delta_m` and retains distinct `d_tot/index_tp_delta_tot`.
- Exp073IT `34431545882 / 102727918512`, head `cd8fb5e069bd8b404d15b04bea4c823e54ca90c8`: raw-log PASS token `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`. Safe target is exact internal gauge-invariant `index_tp_delta_m <- ppw->delta_m`; `d_tot` alias is forbidden.

## Current process — Exp073IU
- gate: implementation-only CLASS-IV `d_m` public-exposure patch build/static audit;
- prereg commit: `5a752298f4fa6bd6b6f0e832d5754e7bfe2c2ea8`;
- patch script commit: `e2e36bcb81cf3f34ecb079f57b14c94ccbe590da`;
- initial workflow commit: `179ae882dc390499380d218b1ae22bf69f496ae7`;
- concurrency hardening commit: `150dc1d22237079645e435650b28c6ff576ab896`;
- primary workflow/run ID: `34431740917`;
- duplicate registration-latency run ID: `34431769157`;
- primary head: `34f5c9640cd87c68df68d573538e1fa18dceef76`;
- duplicate head: `7c4be1d6652ac4324290bb1c508ddb37b61ff96b`;
- jobs: GitHub-hosted `ubuntu-24.04`; exact job IDs to consume from live run state;
- checkpoint namespace: N/A;
- expected token: `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1`;
- current state at ledger write: IN_PROGRESS support/build audit;
- last durable checkpoint: N/A; no cosmological calculation authorized;
- self-hosted/home ownership: none; home runner free.

### Orchestration incident
The initial IU run had not appeared in the live Actions listing when the binding was checked, causing one accidental hosted retrigger. This is an orchestration duplicate only; both runs are support/build jobs and contain no scientific numerical computation. No further IU run may be launched. Workflow concurrency is now prospectively fail-closed with `cancel-in-progress: true`. If both historical runs finish, at most one fully validated PASS becomes support authority; the other is redundant `+0/+0`.

### Exact next action
On terminal IU: inspect raw job log and exact first causal failure if any. A valid PASS requires pinned upstream commit/blob, exact one-time patch anchors, preserved internal `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;`, distinct new public `d_m`, preserved separate `d_tot`, successful core/Python build, no Layer-B numerical execution, and exact PASS token. Then prospectively bind this exact patch into an implementation-only retry of the already-frozen Exp073IR Layer-B gate. Do not alter its science.

On IU infrastructure/build failure: repair only the first causal build/workflow defect prospectively, keep patch semantics and frozen science unchanged, and rerun only after a hosted static/build regression audit.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.