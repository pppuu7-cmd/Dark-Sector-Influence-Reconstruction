# DSIR current-process ledger

Updated: 2026-09-06. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0` Exp073EO, `S0_S1` Exp073EZ, `S0_S2` Exp073FF, `S0_S3` **Exp073FN `34050154578 / 101532191756`**, token `PASS_EXP073FN_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Exp073FG candidate provenance remains run/job `34034377795 / 101489679508`, artifact `9993520467`, exact ZIP SHA256 `8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`, selected exact A/B SHA `db58af980e2997ebbe327ce91dfafb682c38fda1ba841c3d5acba78e429007d3`. Historical collided S0S3 admission run `34047839320 / 101525992295` remains `INFRASTRUCTURE_LOG_TRANSPORT_FAIL_PLUS_0_PLUS_0`; canonical Exp073FL remains the earlier S1S1 static audit.

## Newly closed hosted support for WW_S1_S1

- Exp073FO `34050224161 / 101532385479`: `PASS_EXP073FO_WW_S1_S1_PRODUCTION_TRANSFORMATION_READINESS_V0_1`, `SUPPORT_PLUS_0_PLUS_0`.
- Exp073FP `34050445433 / 101532983406`: `PASS_EXP073FP_WW_S1_S1_EXACT_PRODUCTION_DRIVER_STATIC_AUDIT_V0_1`, `SUPPORT_PLUS_0_PLUS_0`.
- Exp073FQ `34050588344 / 101533366352`: `PASS_EXP073FQ_WW_S1_S1_HOME_ENVELOPE_STATIC_AUDIT_V0_1`, `SUPPORT_PLUS_0_PLUS_0`.
All three create no authority and did not start scientific scoring.

Frozen committed Exp073FM implementation blobs: driver v0.1 `477647c5164264665cc16e20d1577fb25cd245f4`; driver v0.2 `8e3edff39aae95d3abc3196806802c5f0ae59832`; verify/prune `8e04e99084aed582f9586e3f316c023650ce6c63`; terminal comparator `02d69d5d517c676b3ec0963380f93d13f2b9874e`; home envelope `873232cc96f9a97afefeff1ff0a433fd5b49a5a2`.

## Authoritative current process — Exp073FM WW_S1_S1

- workflow/run: **`34050657030`**;
- current hosted-launch job: **`101533554310`**;
- branch/head: `main` / **`f0caca0c3e812710e5958ee13348a150d045a7d8`**;
- state at latest reconciliation: **IN_PROGRESS hosted launch audit**;
- home job: not yet created at this ledger write; `DSIR-HOME-PC` remains FREE until dependency passes;
- science checkpoint namespaces: `checkpoints/exp073fm-ww-s1-s1-a-v0-1`, `checkpoints/exp073fm-ww-s1-s1-b-v0-1`;
- expected candidate token: `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- next action on hosted-launch PASS: GitHub dependency may start exactly one self-hosted home job; do not duplicate it;
- next action on terminal home SUCCESS: download artifact, independently verify ZIP digest, both complete six-stage/prune chains, S1 same-object semantics, exact file-backed MCM proof, exact A/B canonical arrays, then classify candidate; separate provenance admission mandatory before authority;
- next action on infrastructure FAIL: diagnose first causal failure, preserve verified checkpoints, repair minimally, resume without changing frozen science;
- next action on scientific exact mismatch: record scientific FAIL and proceed to next prospectively allowed manifest branch.

## Frozen WW_S1_S1 science

Target `[1,1]`: authoritative S1 reconstructed exactly once per replica; exactly one spin-2 field; identical Python field object passed on both coupling sides; equal-but-distinct field forbidden; NSIDE=4096; ell `0..12287`; 39 bands; public file-backed BPW; canonical `<f8 [39,12288]` `EE<-EE`; exact SHA + `numpy.array_equal`; no tolerance/rounding/smoothing/averaging/manual/effective-coordinate/fiducial rescue. Candidate creates no authority.

## Global frozen boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
