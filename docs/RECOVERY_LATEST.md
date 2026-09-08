# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_WW_S3_S3_ADMITTED_C2_UNBLOCKED_V31.md` (creation commit `d99a6a3458402f3045cd4760c357046e7d516d3d`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority now includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**.

`WW_S3_S3` authority comes from hosted recovery-admission run `34218457380`, job `102035691774 SUCCESS`, head `4e5514b6077e1d70537586b43c9b5ca0e51abcf2`, which consumed the exact completed GA artifact `10051382493` with digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109` and emitted `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s3_s3_authority_created=true`.

Historical GA recovery run `34197207582` is implementation/provenance FAIL `+0/+0`, not scientific FAIL: both A and B completed full-chain verification before the terminal comparator failed on a stale hyphenated namespace expectation. Minimal prospective comparator repair is commit `becbbb58dc59a9f548ddb2c2628cbc5cb1404616`, blob `6e7b45578c647a70233fec7db7d0a1d3c88d1774`. No heavy recomputation was required.

## Current process

Live Actions reconciliation shows **0 queued and 0 in-progress workflows**. No self-hosted heavy owner is active.

The next permitted gate is Exp073HB: deterministic diagnostic exact-endpoint producer implementation plus **hosted-only** build/static audit. Prereg path `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1.md`, blob `fc5f08889f84e628cb789070abd9179a74ef7e04`, expected token `PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1`, scientific ceiling `SUPPORT_PLUS_0_PLUS_0`.

The previous real-C2 blocker `BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY` is released because GA no longer owns the home runner, but real 28-packet / 1792-byte C2 runtime remains **NOT YET AUTHORIZED** until raw-log validated HB PASS. HB itself must execute no cosmological run and create zero runtime payload records.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
