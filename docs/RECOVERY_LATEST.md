# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IV_INVALID_IW_REPEATABILITY_RUNNING_V59.md`, creation commit `4d20c9cfd45ed868e5e5c3b959c2d6360daba0e8`. Earlier notes remain immutable history.

## Preserved authority
All earlier admitted DSIR scientific authority remains unchanged. Article-3 Exp073IQ Layer-A remains PASS: run/job `34423479633 / 102703685034`, artifact `10131794281`, digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, retained set 107.

Original Exp073IR remains invalid-for-science history; repaired Exp073IR run/job `34432102035 / 102729564736` remains exactly `NUMERICALLY_UNRESOLVED_EXP073IR` with 0 invalid rows, f_B=0, retained 107, convergence maximum `0.9998247463807295 > 1e-3`, and covariance restriction unauthorized.

## Newly closed — Exp073IV
Exp073IV run/job `34435415273 / 102739350045`, head `f20b31bef9178ab3097ed606d8fcc983952222c8`, is `SUPPORT_INVALID_PLUS_0_PLUS_0`, not scientific FAIL. Artifact `10136032028`, ZIP digest `sha256:a32fb7e8bc357f1818e5ac7eeb0ff5d90c4685b3907e064fcd73ba68d7210ade`.

Its unchanged Exp073IR rerun remained `NUMERICALLY_UNRESOLVED_EXP073IR`, with 0 invalid rows, f_B=0, retained 107 and intact firewall, but exact parent-max equality failed: rerun max `0.9998247463807128` versus parent `0.9998247463807295`. No tolerance rescue is permitted. Recorded maxima: alpha-left at z=0.7000000000000001, k=0.002502504647141259 Mpc^-1, production 15.004842008323749, dense 0.0026296528687907994; beta-symmetric at z=0.9351, k=0.01860440444314368 Mpc^-1, production 12.060403106488593, dense 0.0038719963413313963.

## Current process — Exp073IW exact repeatability diagnostic
Preregistration commit `577e41714b813142113a0cacfbed93272b30c0a4`; workflow commit `a173451f5a3836bcf27cb53e33360497bdd86fc3`; trigger/head `70cf145eae559c57cbc2c8105c9d4c05ce097fb1`.

Authoritative run `34439055218`, GitHub-hosted `ubuntu-24.04`, checkpoint N/A, home/self-hosted ownership none; queued at registration. It executes the unchanged repaired Exp073IR twice sequentially in one pinned environment with independent scratch directories and compares complete output bytes plus exact binary64 convergence maxima.

Valid outcomes are `REPEATABLE_EXACT_PLUS_0_PLUS_0` or `NONREPEATABLE_EXACT_PLUS_0_PLUS_0`; infrastructure/lineage failure is `INVALID_INFRA_PLUS_0_PLUS_0`. Every outcome is support-only: no Layer-B/covariance/model authority is created and no frozen threshold/arithmetic/domain is modified.

Exact next action: terminal-consume run `34439055218`; verify raw log and artifact digest; classify exact A/B repeatability. Repeatable means the parent/IV cross-run mismatch must be isolated to environment/build provenance before a numerical-resolution experiment. Nonrepeatable within one job requires localization of the first exact-drift field. Infrastructure invalid requires smallest-causal repair only.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.