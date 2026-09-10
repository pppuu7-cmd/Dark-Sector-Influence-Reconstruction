# DSIR recovery — Article 3 IY exact / IZ running — V62

Date: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority
All prior admitted DSIR science remains unchanged. Repaired Exp073IR run `34432102035 / 102729564736`, artifact `10134905199`, remains `NUMERICALLY_UNRESOLVED_EXP073IR`: exact convergence maximum `0.9998247463807295 > 1e-3`, 0 invalid rows, `f_B=0`, retained dimension 107, covariance restriction unauthorized. No tolerance, rounding, smoothing, effective-coordinate or fiducial-P rescue is permitted.

## Newly closed — Exp073IY
Exp073IY cross-build reproducibility run `34447756148` is raw-log and artifact verified as `CROSS_BUILD_EXACT_PLUS_0_PLUS_0`, token `PASS_EXP073IY_CROSS_BUILD_EXACT_V0_1`.

Jobs: replica A `102776221732`, replica B `102776221490`, verifier `102776946041`; head `c210f15138b4597de13edd21ee124272529227c7`.

Artifacts and GitHub ZIP SHA256:
- replica A `10140370989`: `bb22031b82e5ca8425bb7944d91aba187280912b79d4715454705e46f499e701`;
- replica B `10140372425`: `fa76d5fa6cd9ac9783881b0ebb62288ca80ff135649bd07287fb34457f476fc6`;
- verifier `10140382915`: `625075318e1b1166a861decd495700f4a501506215cabaa9b1b2838e10a2851e`;
- authoritative parent artifact `10134905199`: `165a85c8348fc4fc4c52f3926aa1a46989179efc8413a059f9fc2d6aa9dfbb21`.

Replica A, replica B and parent are byte-identical, exact JSON SHA256 `6dea43dcc0eadaf91887f181732d20dceef04866d5687aa231b747312fec0cb1`, exact maximum `0.9998247463807295`. A used hosted image Ubuntu 24.04.5 / image `20260907.300.1`; B used Ubuntu 24.04.4 / image `20260831.293.1`, yet both produced identical `classy` binary SHA256 `76b142d4f308248fc61ebb6d635e65ba07326ee553a0394799359b40ef44f38a`, identical CAMB `camblib.so` SHA256 `2a49b376c6fc1e1da177090bc58defced2e90563c04d20359a357fec1e888a68`, and exact identical science output. This closes cross-build/environment reproducibility as support evidence. It does not create Layer-B, covariance or model authority.

Durable IY authority: `docs/dsir4/authority/EXP073IY_ARTICLE3_LAYERB_CROSS_BUILD_REPRODUCIBILITY_V0_1.json`, creation commit `25c02e0d61d7a7999531a9de4a46896eb1f6c0ff`.

## Prospectively frozen next diagnostic — Exp073IZ
Preregistration: `docs/dsir4/prereg/EXP073IZ_ARTICLE3_LAYERB_NATIVE_GRID_MECHANISM_DIAGNOSTIC_V0_1.md`, commit `fa5b1efba4f9765361a433c33b6fa47a271f2c65`.
Implementation: `ci/exp073iz_article3_layerb_native_grid_mechanism_v0_1.py`, commit `962974600d5d3b03270c52431ecd4a1768e937ac`.
Workflow/launch head: `.github/workflows/exp073iz-article3-layerb-native-grid-mechanism-v0-1.yml`, commit/head `2367abfb48538cac0750c024eebf77d47b4e057d`.

Purpose: support-only exact observation of native CLASS `d_m` bracketing/interpolation and unchanged Exp073IR finite-difference responses at the prospectively frozen historical diagnostic probes, for `k_per_decade_for_pk={10,20,40,80}`. `h=1e-4`, `REL_TOL=1e-3`, physical inputs/domains and interpolation arithmetic remain unchanged. Densities 40/80 are diagnostic only and do not redefine the Exp073IR gate.

## Current authoritative process — Exp073IZ
- workflow: `exp073iz-article3-layerb-native-grid-mechanism-v0-1`;
- run ID: `34452935477`;
- job ID: `102792610244`;
- branch/head: `main / 2367abfb48538cac0750c024eebf77d47b4e057d`;
- checkpoint namespace / durable checkpoint: N/A, complete GitHub-hosted support diagnostic;
- start: `2026-09-10T08:01:25Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- last observed state: IN_PROGRESS; prospective-contract/lineage audit SUCCESS, frozen stack installation active;
- expected valid classification: `NATIVE_GRID_MECHANISM_OBSERVED_PLUS_0_PLUS_0`; infrastructure invalid: `INVALID_INFRA_PLUS_0_PLUS_0`;
- scientific effect: always `+0/+0`; covariance/model authority forbidden.

## Exact next action
On terminal Exp073IZ, inspect job steps and first causal failure if any; read raw log and artifact, verify artifact digest/provenance and complete four-density/two-probe native bracket records. If valid, classify support-only and interpret the complete pattern to prospectively choose the smallest next numerical-resolution test that distinguishes native-grid interpolation sampling, finite-difference cancellation or another solver-resolution mechanism. Do not change the original Exp073IR `1e-3` criterion.

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.
