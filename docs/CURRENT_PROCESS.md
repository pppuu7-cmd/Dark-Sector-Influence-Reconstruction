# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IR_UNRESOLVED_IV_DIAGNOSTIC_RUNNING_V58.md`, creation commit `3cace1e607d8d1a89c866d53aec33e712b498a94`.

## Newly closed
- All earlier admitted DSIR scientific authority remains preserved.
- Article-3 Exp073IQ Layer-A PASS remains `34423479633 / 102703685034`, artifact `10131794281`, SHA256 `ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, retained set 107.
- Repaired Exp073IR `34432102035 / 102729564736`, head `38604061abe6cbcccbf9614b22e3ca0ca6a9ec0f`, artifact `10134905199`, ZIP SHA256 `165a85c8348fc4fc4c52f3926aa1a46989179efc8413a059f9fc2d6aa9dfbb21`: raw classification `NUMERICALLY_UNRESOLVED_EXP073IR`. Production Layer-B has 0 invalid rows, `f_B=0`, 107 retained, but frozen convergence max relative component difference `0.9998247463807295 > 1e-3`; convergence false, covariance restriction unauthorized. This is neither scientific PASS nor scientific FAIL.

## Current authoritative process — Exp073IV
- workflow: `exp073iv-article3-layerb-convergence-mechanism-diagnostic-v0-1`;
- run ID: `34435415273`;
- job ID: `102739350045`;
- branch/head: `main / f20b31bef9178ab3097ed606d8fcc983952222c8`;
- preregistration commit: `1e3398631973bc410a4c36a1bf06dd558a925863`;
- implementation commit: `c41ecdcca7fea456975868aa16bee38ecdda4ce4`;
- workflow commit: `628daeb44c84a8844f50540ec852222a95a2834d`;
- checkpoint namespace / last durable checkpoint: N/A;
- start/registration: 2026-09-10T03:59:31Z;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- current state at latest live inspection: QUEUED;
- expected token: `PASS_EXP073IV_LAYERB_CONVERGENCE_MECHANISM_DIAGNOSTIC_V0_1` only if support diagnostic reproduces the frozen unresolved parent exactly and records both per-component argmax diagnostics;
- scientific effect: always `+0/+0`; no Layer-B/covariance/model authority may be created by Exp073IV.

### Exact next transitions
SUCCESS/terminal: inspect raw log plus artifact/digest. Require parent rerun status exactly `NUMERICALLY_UNRESOLVED_EXP073IR`, exact reproduction of max relative difference `0.9998247463807295`, both component maxima finite with exact z/k and production/dense values, and intact covariance firewall. Then prospectively freeze the smallest numerical-resolution experiment justified by the diagnosed mechanism without weakening `REL_TOL=1e-3` or changing h/domains/arithmetic.

FAIL/INVALID: diagnose the first causal infrastructure/instrumentation defect; repair only that support diagnostic prospectively. Do not change Exp073IR science or rerun it blindly.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.