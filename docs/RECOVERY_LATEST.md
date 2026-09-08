# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_HB_PROSPECTIVE_BUILD_AUDIT_V30.md` (creation commit `cf23007b16c27d9908a51b15eb76f92c0d29b83e`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and `S2_S3`. `WW_S3_S3` remains **NOT_YET_ADMITTED**.

Exp073GA historical run `34189540992` remains implementation/infrastructure FAIL `+0/+0` after preserved expensive Replica A. Minimal pruner repair is commit `f52fa856eb029c64f744926eecf55f506fcf1da5`; repaired workflow binding/regression commit `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`.

## Current single heavy process

Exp073GA recovery run **`34197207582`**, head **`f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`**. Hosted job **`101967492875 SUCCESS`**. Home job **`101967543808 IN_PROGRESS`** on frozen `WW_S3_S3` A/B gate. Checkpoint root `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`; last verified durable checkpoint is Replica A `replica_receipt_complete` from run `34189540992`. Do not launch competing home-heavy work or inspect partial GA numerical output.

Candidate token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Final authority requires separate GB token `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s3_s3_authority_created=true`.

## Independent C2 advancement

Exp073GZ receipt-contract audit remains PASS `SUPPORT_PLUS_0_PLUS_0`.

Exp073HA native exact-endpoint extraction static audit remains raw-log validated PASS `SUPPORT_PLUS_0_PLUS_0`: run `34207078292`, job `101998967311 SUCCESS`, exact token `PASS_EXP073HA_C2_NATIVE_EXACT_ENDPOINT_EXTRACTION_STATIC_AUDIT_V0_1`. HA produced no cosmological runtime or payload.

Exp073HB diagnostic exact-endpoint producer build/static audit is now prospectively frozen: prereg path `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1.md`, creation commit `4ca51c172c89c52a3f5a2613e30133a59d03d38e`, prereg blob `fc5f08889f84e628cb789070abd9179a74ef7e04`, expected token `PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1`, scientific ceiling `SUPPORT_PLUS_0_PLUS_0`.

HB authorizes only deterministic diagnostic producer implementation plus hosted build/static audit. It must preserve native exact-k insertion, literal-z native coordinate resolution, terminal accepted `ynew`, pre-transform `delta_m/theta_m`, no perturbation-state interpolation/rescue, and no scientific-path changes. It forbids cosmological execution and runtime payload creation during the audit.

Real 28-packet / 1792-byte C2 runtime remains `BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY` while GA owns the home-heavy runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
