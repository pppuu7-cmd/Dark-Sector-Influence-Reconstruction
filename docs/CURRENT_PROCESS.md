# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IV_INVALID_IW_REPEATABILITY_RUNNING_V59.md`, creation commit `4d20c9cfd45ed868e5e5c3b959c2d6360daba0e8`.

## Newly closed
- Earlier admitted DSIR scientific authority remains preserved.
- Repaired Exp073IR `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`; convergence max `0.9998247463807295 > 1e-3`; covariance unauthorized.
- Exp073IV `34435415273 / 102739350045`, artifact `10136032028`, ZIP digest `a32fb7e8bc357f1818e5ac7eeb0ff5d90c4685b3907e064fcd73ba68d7210ade`, is `SUPPORT_INVALID_PLUS_0_PLUS_0`: its rerun stayed unresolved with intact firewall but exact max was `0.9998247463807128`, not the frozen parent `0.9998247463807295`. No tolerance rescue.

## Current authoritative process — Exp073IW
- workflow: `exp073iw-article3-layerb-exact-repeatability-diagnostic-v0-1`;
- run ID: `34439055218`;
- job ID: pending at registration;
- branch/head: `main / 70cf145eae559c57cbc2c8105c9d4c05ce097fb1`;
- preregistration commit: `577e41714b813142113a0cacfbed93272b30c0a4`;
- workflow commit: `a173451f5a3836bcf27cb53e33360497bdd86fc3`;
- checkpoint namespace / last durable checkpoint: N/A;
- start/registration: `2026-09-10T04:55:31Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- current state at registration: QUEUED;
- expected valid support outcomes: `PASS_EXP073IW_LAYERB_EXACT_REPEATABILITY_DIAGNOSTIC_V0_1` (`REPEATABLE_EXACT_PLUS_0_PLUS_0`) or `NONREPEATABLE_EXP073IW_LAYERB_EXACT_REPEATABILITY_DIAGNOSTIC_V0_1` (`NONREPEATABLE_EXACT_PLUS_0_PLUS_0`);
- scientific effect: always `+0/+0`; no Layer-B/covariance/model authority.

### Exact next transitions
Terminal valid REPEATABLE: verify raw log/artifact hashes and exact A/B identity, then prospectively isolate cross-run environment/build fingerprint differences that explain parent-vs-IV binary64 drift.

Terminal valid NONREPEATABLE: verify raw log/artifact hashes, then prospectively localize the first exact solver/output field that drifts within one pinned job; do not introduce tolerance.

INVALID/infra: diagnose first causal defect and repair only that support diagnostic. Do not alter Exp073IR science or its frozen `REL_TOL=1e-3`.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.