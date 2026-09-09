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
- current state: **BLOCKED / NOT_YET_TESTABLE at `G_RADIAL_SUPPORT`, but the external source-payload search has materially advanced**;
- last durable scientific result: Exp073IL authority above;
- newest support audit: `docs/dsir4/audits/DSIR4_RADIAL_AUTHORITY_LOCATOR_AUDIT_V0_1.md`, creation commit `55e62ae8b721ee672ade3c1469ab7d53e120af84`;
- self-hosted/home ownership: none; runner free.

### Narrowed blocker after radial-authority locator audit
The funnel still requires radial multiplication/support construction and the admitted angular evidence still records `radial_kernel_read=False` and `physical_k_computed=False`. However, a concrete high-confidence external source-radial candidate has now been located:

`des-y3/2pt_NG_final_2ptunblind_02_24_21_wnz_covupdate.v2.fits`

DES analysis code uses this exact file as a fiducial `DATAFILE`, and a public loader of the exact filename reads `nz_source/Z_MID` plus four source columns `BIN1..BIN4`. This materially narrows the S0..S3 data blocker, but no ordinal mapping is admitted yet: authoritative proof is still required that frozen `zbin_mcal=[0,1,2,3]` corresponds exactly to `BIN1..BIN4`, together with exact schema/edges, normalization/weighting convention and immutable payload digest.

The WW two-source radial operator and the Wm matter-side radial/line-of-sight factor are still not bound. Existing angular `TE<-TE` / `EE<-EE` authority is insufficient to infer them.

Prospective support prerequisite remains `docs/dsir4/contracts/DSIR4_RADIAL_SUPPORT_INPUT_REQUIREMENTS_V0_1.md`, creation commit `9064b6e948e328df00439f31c54c6b08e8ea933e`, blob `3fa4a41b3c53f4d8e879a105f0f5621cc60a9f98`.

### Exact next permitted action
Acquire/inspect the exact fiducial DES Y3 FITS bytes and authoritative DES metadata/code linking metacal source-bin labels to `nz_source/BIN1..BIN4`; record immutable digest/schema/coordinates/units/normalization. Locate and freeze the actual observation-model equations or implementation that constructs the WW weak-lensing radial kernels and the Wm matter-side LOS kernel. Only after those prerequisites are bound prospectively may a new `G_RADIAL_SUPPORT` experiment be preregistered and launched.

No seven-z proxy, angular-mask proxy, interpolation/extrapolation, smoothing, rounding, effective ell/z/k or fiducial-P substitution may be used.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.