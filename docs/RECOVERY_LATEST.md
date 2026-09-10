# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IT_PASS_IU_BUILD_AUDIT_RUNNING_V56.md`, creation commit `67b2100d731198d98e7ae5bbfd77d0aed8b2ce2e`. Earlier notes remain immutable history.

## Preserved authority
All earlier admitted DSIR scientific authority is unchanged. Article-3 Exp073IQ Layer-A remains PASS: run/job `34423479633 / 102703685034`, artifact `10131794281`, digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, retained set 107.

Exp073IR `34428699659 / 102719344981` is `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`, not scientific FAIL: artifact `10133682066`, ZIP SHA256 `6d84e6ab94ea66d9b9f857727b7e6089cfb4cacc60e141660cd713e42d30a876`, failed because pinned CLASS-IV public transfer output lacked exact `d_m` and returned separate `d_tot`. No Layer-B/covariance authority was created.

Exp073IS `34431475914 / 102727713276` is support-only `+0/+0`: it proved public `d_m/index_tp_delta_m` is absent in the pinned writer, so `d_tot` substitution is forbidden.

Exp073IT is now raw-log validated PASS `SUPPORT_PLUS_0_PLUS_0`: run/job `34431545882 / 102727918512`, head `cd8fb5e069bd8b404d15b04bea4c823e54ca90c8`, exact token `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`. Exact safe target is the already-computed gauge-invariant source `index_tp_delta_m <- ppw->delta_m`; `index_tp_delta_tot/d_tot` is forbidden as alias.

## Current process
Exp073IU prospectively tests only the minimal public-exposure patch/build path. Prereg commit `5a752298f4fa6bd6b6f0e832d5754e7bfe2c2ea8`; patch script commit `e2e36bcb81cf3f34ecb079f57b14c94ccbe590da`; workflow concurrency-hardened at `150dc1d22237079645e435650b28c6ff576ab896`.

Due to GitHub run-list registration latency, launch run `34431740917` was accidentally retriggered as run `34431769157` before the first appeared. Both are hosted support/build only, no cosmology. No further IU run is permitted. Concurrency ownership was added prospectively; at most one validated terminal PASS may be admitted, the duplicate is redundant `+0/+0`.

Exact next action: consume IU terminal raw log(s). Only exact token `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1` with successful pinned-source/static/build checks authorizes an implementation-only Exp073IR retry using this exact interface patch. Scientific equations, `h=1e-4`, interpolation, domains, thresholds, Layer-A set and covariance firewall remain frozen.

Global boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.