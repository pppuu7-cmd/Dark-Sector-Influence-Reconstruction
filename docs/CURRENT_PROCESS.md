# DSIR current-process ledger

Updated: 2026-09-09. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority
All prior DSIR authority remains preserved. Scientifically admitted `WW_S3_S3` remains `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_IL_ORDERED_JOIN_PASS_RADIAL_SUPPORT_BLOCKED_V54.md`, creation commit `95fc6416b350e1a41ab1bca8fa50cd2c665024c9`.

## Newly closed process — Exp073IL
- gate: C2 `G_ORDERED_JOIN` structural/provenance admission;
- prospective definition commit/blob: `a2d4db0c1a0763d064ca4a47cf73aa9e6a4ea376 / b594579c9f95fdb5085f5e9ba09f4dbc383d719a`;
- prereg creation commit/blob: `ae5d4aebab9467cd93fdbd594f8e940c50df6fc1 / 6da7eadd1d01344741c65d6e72a5fa02d7b35cc0`;
- repaired workflow commit/blob: `d13d6ab2f99a632b434c8e6ecad821ddf0aead3e / cbb7a9cfe247ecf4b15a81138c1cc11f0d01446d`;
- binding head/blob: `5bf6b492c3f4220a5c5aaf2276f6acd83507ad60 / d5a020b6c0e1acc2b6910265735d517059bca94d`;
- valid run/job: `34271954072 / 102215439354`;
- runner: GitHub-hosted `ubuntu-24.04`;
- checkpoint namespace: N/A;
- artifact ID: `10074157812`;
- independently verified ZIP SHA256: `acaaf9c00a3654b5e59c190470325a92818e8f2f94296ee45bce1ecfd27baa9e`;
- exact token: `PASS_EXP073IL_C2_ORDERED_JOIN_STRUCTURAL_ADMISSION_V0_1`;
- classification: `SCIENTIFIC_GATE_PASS`;
- durable authority commit/blob: `ad2768a11b306134129aca9f9f6639818b26d6f7 / 31bcde1737c782cbce16db2e447a76ab007d3bbb`;
- scientific state: `G_DOMAIN_MAPPING=PASS`, `G_ANGULAR_AUTHORITY=PASS`, `G_ORDERED_JOIN=PASS`, `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`, `scientific_model_authority_created=false`, `overall_status=NOT_YET_TESTABLE`.

Historical Exp073IL run/job `34271889927 / 102215228801` is infrastructure/implementation `+0/+0`; first causal failure was a JSON literal-format mismatch in the static audit. No scientific criteria changed.

## Current process
- workflow/run ID: none;
- job ID: none;
- branch/head: `main` current repository head;
- checkpoint namespace: N/A;
- start time: N/A;
- expected gate/token: none currently executable;
- current state: **BLOCKED / NOT_YET_TESTABLE at `G_RADIAL_SUPPORT`, with DES-Y1 survey/bin identity and historical LOS methodology now recovered**;
- last durable scientific result: Exp073IL authority above;
- newest support/provenance correction: `docs/dsir4/audits/DSIR4_RADIAL_AUTHORITY_DESY1_SUPERSESSION_V0_1.md`, creation commit `cf207b39b5f28accbb305b568604496005e425cf`;
- self-hosted/home ownership: none; runner free.

### Corrected blocker after DES-Y1 supersession audit
The funnel still requires a prospectively frozen radial multiplication/support interface, and the admitted angular evidence still records `radial_kernel_read=False` and `physical_k_computed=False`.

However, the survey/source identity is no longer unresolved. The current C2 source labels are DES Y1 Metacalibration bins, not DES Y3. Pinned Cosmotheka DES-Y1 code binds `zbin_mcal=0,1,2,3` directly to `y1_redshift_distributions_v1.fits` columns `BIN1..BIN4` through `BIN{zbin+1}`. Therefore the exact ordinal bridge is now recovered:

`S0 -> BIN1`, `S1 -> BIN2`, `S2 -> BIN3`, `S3 -> BIN4`.

The DES-Y3 payload previously located remains only a methodological analogue and is superseded as the active C2 radial candidate.

Wm physical identity is also recovered from the historical Exp073O/Exp073P route: it is the signed DES-Y1 galaxy-density x galaxy-shear observable. The lens mapper uses the five DES-Y1 redMaGiC bins `[0.15,0.30)`, `[0.30,0.45)`, `[0.45,0.60)`, `[0.60,0.75)`, `[0.75,0.90)` and reads the lens `n(z)` from `2pt_NG_mcal_1110.fits`. WW is the DES-Y1 source shear x source shear block.

Historical Exp073P additionally froze the physical support bookkeeping `k=(ell+1/2)/chi(z)`, positive absolute bandpower-response propagation, physical `k [Mpc^-1]`, and a strict prohibition on fiducial-`P(k)`, covariance, nuisance, relation/null or later-gate weighting. This methodology can constrain the current radial executor, but its historical `operator_f_invalid` statistic must not be aliased to the later Article-3 coordinate-count `f_invalid` statistic.

### Remaining exact blocker
Before a new C2 `G_RADIAL_SUPPORT` experiment can be preregistered and launched, the repository still needs:

1. immutable byte identity/SHA256/schema for every DES-Y1 radial payload actually consumed by the new C2 route;
2. exact source/lens normalization and allowed photo-z shift convention;
3. one explicit current C2 radial executor interface consuming the admitted 14-slot ordered join and emitting pre-physical-support coordinates without reading covariance/nuisance/relation information;
4. exact coordinate/ordinal schema connecting this radial output to the already-frozen later Article-3 `G_PHYSICAL_SUPPORT` contract;
5. synthetic fail-closed tests for source-bin permutation, unit mixing, zero/non-finite kernels, forbidden interpolation/effective coordinates and downstream leakage.

Prospective support prerequisite remains `docs/dsir4/contracts/DSIR4_RADIAL_SUPPORT_INPUT_REQUIREMENTS_V0_1.md`, creation commit `9064b6e948e328df00439f31c54c6b08e8ea933e`, blob `3fa4a41b3c53f4d8e879a105f0f5621cc60a9f98`, now interpreted together with the DES-Y1 supersession audit above.

### Exact next permitted action
Freeze a current DES-Y1 C2 radial-input manifest around `y1_redshift_distributions_v1.fits`, `2pt_NG_mcal_1110.fits` and the already-admitted angular 14-slot order; bind exact bytes/schema/normalization and implement a non-classifying synthetic radial-interface self-test. Only after that interface is prospectively frozen may a real `G_RADIAL_SUPPORT` run be authorized.

No seven-z proxy, DES-Y3 substitution, angular-mask proxy, interpolation/extrapolation, smoothing, rounding, effective ell/z/k or fiducial-P substitution may be used.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
