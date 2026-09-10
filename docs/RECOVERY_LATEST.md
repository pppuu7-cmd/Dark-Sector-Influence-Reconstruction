# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_IX_NEUTRAL_IY_RUNNING_V61.md`, creation commit `dfa0d81ab160147241ce87a7327ce9f2f345a245`. Earlier notes remain immutable history.

## Preserved authority
All earlier admitted DSIR scientific authority remains unchanged. Article-3 Exp073IQ Layer-A remains PASS with retained set 107. Repaired Exp073IR run/job `34432102035 / 102729564736`, artifact `10134905199`, remains exactly `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, f_B=0, retained 107, exact convergence maximum `0.9998247463807295 > 1e-3`, covariance restriction unauthorized. Exp073IV remains historical `SUPPORT_INVALID_PLUS_0_PLUS_0`; no tolerance rescue.

## Newly closed — Exp073IX
Run/job `34443359314 / 102762823702`, head `b05ce738c904cc49e683570868edccf2cf3eb610`, artifact `10138827841`, digest `sha256:4b855d37c36bb1d066f8688f8933e3f6397f85d1bf2ab039e2cb425bb8e8f588`, is `INSTRUMENTATION_NEUTRAL_PLUS_0_PLUS_0`. Raw token `PASS_EXP073IX_INSTRUMENTATION_NEUTRAL_V0_1`. Direct and IV-wrapped outputs are byte-identical, each SHA256 `6dea43dcc0eadaf91887f181732d20dceef04866d5687aa231b747312fec0cb1`, and both exact maxima equal the authoritative parent `0.9998247463807295`. Durable authority commit `e3d1b9d9b41c3c9bbf2a2288dd673d6b194afeaa`. Scientific effect `+0/+0` only.

Historical environment audit found the same logged semantic solver/package/image lineage across IR/IV/IX; differing ephemeral CAMB wheel archive SHA is not sufficient to explain the IV mismatch because IX also rebuilt a different wheel archive while reproducing the parent exactly. The IV wrapper and IR producer were unchanged between IV and IX.

## Current process — Exp073IY cross-build reproducibility
Preregistration commit `73c9139c51acc0e4c450dd5aafcecbc9a48e21e0`; workflow commit `d6fc0a82072ff91b5021b005760c8856c537999f`; trigger/head `c210f15138b4597de13edd21ee124272529227c7`.

Authoritative workflow/run: `exp073iy-article3-layerb-cross-build-reproducibility-v0-1 / 34447756148`. Replica jobs: B `102776221490`, A `102776221732`, both IN_PROGRESS at this recovery update; verifier awaits both. GitHub-hosted `ubuntu-24.04`; checkpoint N/A; home/self-hosted ownership none.

Exp073IY independently rebuilds the exact frozen environment twice and executes repaired Exp073IR uninstrumented. Exact A/B/authoritative-parent output byte equality is required. Valid classifications are `CROSS_BUILD_EXACT_PLUS_0_PLUS_0`, `CROSS_BUILD_DRIFT_PLUS_0_PLUS_0`, or `INVALID_INFRA_PLUS_0_PLUS_0`. No scientific threshold or arithmetic is changed.

Exact next action: terminal-consume run `34447756148`; verify both replica logs/artifacts, build provenance and verifier artifact/digest. On `CROSS_BUILD_EXACT_PLUS_0_PLUS_0`, prospectively freeze the smallest uninstrumented numerical-resolution mechanism diagnostic for the genuine Exp073IR convergence failure. On drift, isolate the first reproducible build/environment cause before numerical-resolution work.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.