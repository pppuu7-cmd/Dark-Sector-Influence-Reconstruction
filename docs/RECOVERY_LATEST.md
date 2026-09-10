# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IR_INVALID_DM_INTERFACE_IT_PATCH_TARGET_V55.md`, creation commit `dd6f9663ea3fc8a2ad18a01b4ba56cb41d1b635e`. Earlier recovery notes remain immutable history.

## Preserved authority
All earlier admitted DSIR authority remains unchanged, including Wm_S1 Track-A exact PASS, admitted Wm_S2/Wm_S3, admitted WW_S3_S3, C2 tangent/domain/angular/ordered-join authorities, and Article-3 Exp073IQ Layer-A PASS. Exp073IQ authority: run/job `34423479633 / 102703685034`, artifact `10131794281`, digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, retained set 107.

## Current Article-3 Layer-B state
Exp073IR run/job `34428699659 / 102719344981`, head `dac55828f7d1e1e033769d9fd4e43079d224758b`, is **INVALID_FOR_SCIENCE**, not scientific FAIL. Artifact `10133682066`, ZIP SHA256 `6d84e6ab94ea66d9b9f857727b7e6089cfb4cacc60e141660cd713e42d30a876`, reports exact error: expected public `d_m`, but pinned CLASS-IV returned `d_tot` and no `d_m` column. No Layer-B or covariance authority was created.

Exp073IS then prospectively audited the exact pinned source interface. Run/job `34431475914 / 102727713276` established support-only `+0/+0`: `index_tp_delta_m` exists separately from `index_tp_delta_tot` and is enabled by the number-count density route, but the pinned public transfer writer does not expose `d_m/index_tp_delta_m`; it only exposes `d_tot/index_tp_delta_tot`. Therefore aliasing `d_tot` to `d_m` is forbidden.

Pinned `source/perturbations.c` blob `92a48331658c5941ed4eb43b0e98ee78e39b8385` explicitly defines the desired source as gauge-invariant total matter overdensity and assigns `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;`.

## Current process
Exp073IT static patch-target audit is queued: run `34431545882`, head `cd8fb5e069bd8b404d15b04bea4c823e54ca90c8`, expected token `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`; GitHub-hosted only, no home/self-hosted ownership.

Exact next action: consume Exp073IT raw log. On PASS, prospectively freeze and hosted-build/static-audit the smallest CLASS-IV interface patch that exposes the existing `index_tp_delta_m <- ppw->delta_m` source and enables it for transfer output, without changing any physical variable, cosmology, finite-difference step, interpolation, domain, threshold, or downstream firewall. Only after that audit may Exp073IR numerical Layer B be rerun.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.