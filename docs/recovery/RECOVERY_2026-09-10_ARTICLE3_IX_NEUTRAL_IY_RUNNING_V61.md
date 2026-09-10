# DSIR recovery — V61 — Exp073IX neutral; Exp073IY running

Date: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved scientific authority

All earlier admitted DSIR scientific authority is unchanged. Exp073IQ Article-3 Layer-A remains PASS with retained set 107. Repaired Exp073IR run/job `34432102035 / 102729564736`, artifact `10134905199`, remains exactly `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107, exact convergence maximum `0.9998247463807295 > 1e-3`; covariance restriction remains unauthorized. Exp073IV remains historical `SUPPORT_INVALID_PLUS_0_PLUS_0` and cannot be rescued by tolerance.

## Newly closed — Exp073IX

Run/job `34443359314 / 102762823702`, head `b05ce738c904cc49e683570868edccf2cf3eb610`, artifact `10138827841`, independently downloaded ZIP digest `sha256:4b855d37c36bb1d066f8688f8933e3f6397f85d1bf2ab039e2cb425bb8e8f588`.

Raw token: `PASS_EXP073IX_INSTRUMENTATION_NEUTRAL_V0_1`. Classification: `INSTRUMENTATION_NEUTRAL_PLUS_0_PLUS_0`.

Direct and exact Exp073IV-wrapped repaired Exp073IR outputs are byte-identical; each SHA256 is `6dea43dcc0eadaf91887f181732d20dceef04866d5687aa231b747312fec0cb1`; both exact convergence maxima equal authoritative parent `0.9998247463807295`. Therefore observational instrumentation is not causal under the frozen IX environment. Scientific effect remains `+0/+0`; covariance/model/manuscript authority is not created.

Historical provenance comparison additionally shows Exp073IR, Exp073IV and Exp073IX used the same logged semantic stack: runner 2.337.0, Hosted Compute Agent `20260828.587` commit `abac92662cab4cc7352de4f9f9d2e2419aad9c29`, Ubuntu 24.04.5, image `20260907.300.1`, numpy 1.26.4, Cython 0.29.37, scipy 1.17.1, astropy 7.2.2, CAMB source `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`, CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c` and the audited `d_m` patch. The CAMB wheel archive SHA differs across builds (`3145467e...` parent, `c86d35f5...` IV, another SHA in IX) while IX nevertheless reproduces parent output exactly, so wheel archive SHA difference alone is not causal scientific evidence. The Exp073IV wrapper and repaired IR producer were unchanged between IV head and IX head.

Durable IX authority: `docs/dsir4/authority/EXP073IX_ARTICLE3_LAYERB_INSTRUMENTATION_NEUTRALITY_V0_1.json`, creation commit `e3d1b9d9b41c3c9bbf2a2288dd673d6b194afeaa`.

## Current process — Exp073IY cross-build reproducibility

Purpose: prospectively isolate independent hosted rebuild reproducibility before any numerical-resolution experiment. It is support-only and does not change the frozen scientific gate.

Preregistration: `docs/dsir4/prereg/EXP073IY_ARTICLE3_LAYERB_CROSS_BUILD_REPRODUCIBILITY_V0_1.md`, commit `73c9139c51acc0e4c450dd5aafcecbc9a48e21e0`.
Workflow implementation commit: `d6fc0a82072ff91b5021b005760c8856c537999f`.
Trigger/head commit: `c210f15138b4597de13edd21ee124272529227c7`.
Workflow/run: `exp073iy-article3-layerb-cross-build-reproducibility-v0-1 / 34447756148`.
Active jobs at recovery write:
- replica B job `102776221490` — IN_PROGRESS;
- replica A job `102776221732` — IN_PROGRESS;
- verifier waits on both rebuild jobs.
Runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none. Checkpoint namespace: N/A; each replica is an independent complete hosted rebuild.

Frozen classifications: `CROSS_BUILD_EXACT_PLUS_0_PLUS_0`, `CROSS_BUILD_DRIFT_PLUS_0_PLUS_0`, or `INVALID_INFRA_PLUS_0_PLUS_0`. Exact output byte equality against each other and authoritative repaired Exp073IR artifact is required; no tolerance is allowed for the reproducibility comparison.

Exact transition on `CROSS_BUILD_EXACT_PLUS_0_PLUS_0`: terminal-consume both replica artifacts and verifier artifact, verify raw logs/digests/provenance, then prospectively freeze the smallest **uninstrumented** numerical-resolution mechanism diagnostic. Exact transition on drift: identify the first reproducible binary/environment provenance difference before numerical-resolution work. Infrastructure invalid: repair only the first causal infrastructure defect prospectively and rerun without changing science.

Global frozen science remains unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
