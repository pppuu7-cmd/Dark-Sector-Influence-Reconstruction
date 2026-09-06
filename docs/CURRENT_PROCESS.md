# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`. Exp073EL remains resource/readiness support PASS +0/+0.

`WW_S0_S1` is admitted by Exp073EZ run/job `34017921734 / 101444964371`, raw token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, classification `SCIENTIFIC_AUTHORITY_ADMITTED`. Its candidate is Exp073EY resume `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, exact selected A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`.

Historical Exp073EZ first admission `34017884048 / 101444857315` remains `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0`; minimal audit-only NumPy repair did not change science.

## Current frontier

`WW_S0_S2`, prospectively frozen as Exp073FA.

Exp073FA prereg:
- `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`;
- commit `a1ce88850d037b408eb5f8cdd3275dbc7cf629b4`;
- blob `edc044792be8ac7b796c8469943924942ae91932`;
- ordered distinct `(S0,S2)` using source indices `[0,2]`;
- source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- checkpoint namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `...-b-v0-1`;
- candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- candidate PASS alone creates no authority.

Exp073FA prerequisite static audit run/job `34018080500 / 101445404866` is terminal SUCCESS with raw token `PASS_EXP073FA_WW_S0_S2_PREREQUISITE_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`, `ww_s0_s2_authority_created=false`. It verified exact prereg/task-runner/read-patch identities, authoritative source-2 support, upstream Exp073EZ terminal success, and the frozen no-rescue contract.

## Authoritative current process — Exp073FB

Purpose: generate and statically audit the dedicated Exp073FA S0_S2 durable A/B drivers before any home science launch.

- workflow `Exp073FB Exp073FA S0_S2 driver transformation v0.1`;
- run **`34018169771`**;
- job **`101445653251`**;
- activation/head **`fdfbfa161e5661f9eb32dc70804f5ac9cd145adf`**;
- prereg `experiments/073fb_exp073fa_s0_s2_driver_transformation_v0_1_prereg.md`;
- prereg blob `7ff28ad4239728c14d05094b55ffc713c52210e6`;
- state at ledger update: **IN_PROGRESS** on GitHub-hosted runner;
- expected token `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`;
- classification on PASS: support/governance `+0/+0`, no WW authority;
- output artifact if PASS: generated S0_S2 v0.1/v0.2 driver candidates plus transformation receipt.

**Runner ownership:** `DSIR-HOME-PC` currently has no DSIR owner; Exp073FB is hosted-only. No Exp073FA science checkpoint exists yet.

On Exp073FB PASS: consume generated artifact and digest, freeze exact generated driver identities plus a dedicated fail-closed home envelope, run hosted implementation audit, live-check zero competing self-hosted jobs, then launch exactly one Exp073FA A/B science computation. On FB failure: diagnose first causal transformation/audit defect and repair without changing Exp073FA science preregistration.

## Frozen global boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.