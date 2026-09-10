# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IU_PASS_IR_RETRY_RUNNING_V57.md`, creation commit `4982a692fd3f5728a7b7a60a83817199c6b96f5c`. Earlier notes remain immutable history.

## Preserved authority
All earlier admitted DSIR scientific authority remains unchanged. Article-3 Exp073IQ Layer-A remains PASS: run/job `34423479633 / 102703685034`, artifact `10131794281`, digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, retained set 107.

Original Exp073IR `34428699659 / 102719344981` remains `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`, not scientific FAIL; artifact `10133682066`, ZIP SHA256 `6d84e6ab94ea66d9b9f857727b7e6089cfb4cacc60e141660cd713e42d30a876`, lacked exact public `d_m`. Exp073IS `34431475914 / 102727713276` is support-only `+0/+0` proving `d_tot` cannot be aliased. Exp073IT `34431545882 / 102727918512` is raw-log PASS `SUPPORT_PLUS_0_PLUS_0` proving the safe target is the existing gauge-invariant `index_tp_delta_m <- ppw->delta_m`.

Exp073IU primary run/job `34431740917 / 102728498891`, head `34f5c9640cd87c68df68d573538e1fa18dceef76`, is raw-log validated PASS `SUPPORT_PLUS_0_PLUS_0`, token `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1`: exact pinned source/hash, exact patch anchors, separate public `d_m`, preserved `d_tot`, successful CLASS/Python build/import, no cosmology. Runs `34431769157 / 102728585401` and `34431885548 / 102728934900` are redundant support-only duplicate evidence caused by Actions registration latency; they create no additional authority. No further IU run is permitted.

## Current process
The existing frozen Exp073IR Layer-B gate has been repaired only at the audited interface level. Implementation-control v0.2 commit `3f1b819ac291f3cf217fd28bb2dd51c351f3c82b`; workflow repair commit `2b1befe68791e51088aeae170ac435b21dce125f`; trigger/head `38604061abe6cbcccbf9614b22e3ca0ca6a9ec0f`.

Authoritative active run/job: `34432102035 / 102729564736`, GitHub-hosted `ubuntu-24.04`, checkpoint N/A, home/self-hosted ownership none. At latest inspection it is IN_PROGRESS. The exact frozen scientific script and criteria are unchanged.

Exact next action: terminal-consume run `34432102035`; inspect raw log and artifact/digest/provenance. Only raw `PASS_PHYSICAL_SUPPORT_ARTICLE3` with invalid-row fraction `<=0.05`, retained-after-Layer-B `>=15`, convergence PASS and intact covariance firewall creates Layer-B scientific support authority. `FAIL_PHYSICAL_SUPPORT_ARTICLE3` is scientific FAIL; `NUMERICALLY_UNRESOLVED_EXP073IR` is unresolved; source/hash/build/runtime/interface/provenance failure remains INVALID/infrastructure and must be repaired prospectively without science changes.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.