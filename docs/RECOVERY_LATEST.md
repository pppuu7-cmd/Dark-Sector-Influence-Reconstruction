# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_HA_EXACT_ENDPOINT_STATIC_AUDIT_PASS_V29.md` (creation commit `f02ad2ff93f005c08ce3b7c17564bda490d3d3ea`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and `S2_S3`. `WW_S3_S3` remains **NOT_YET_ADMITTED**.

Exp073GA historical run `34189540992` remains implementation/infrastructure FAIL `+0/+0` after preserved expensive Replica A. Minimal pruner repair is commit `f52fa856eb029c64f744926eecf55f506fcf1da5`; repaired workflow binding/regression commit `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`.

## Current single heavy process

Exp073GA recovery run **`34197207582`**, head **`f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`**. Hosted job **`101967492875 SUCCESS`**. Home job **`101967543808 IN_PROGRESS`** on frozen `WW_S3_S3` A/B gate. Checkpoint root `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`; last verified durable checkpoint is Replica A `replica_receipt_complete` from run `34189540992`. Do not launch competing home-heavy work or inspect partial GA numerical output.

Candidate token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Final authority requires separate GB token `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s3_s3_authority_created=true`.

## Independent C2 advancement

Exp073GZ receipt-contract audit remains PASS `SUPPORT_PLUS_0_PLUS_0`.

Exp073HA native exact-endpoint extraction static audit is now raw-log validated PASS: run **`34207078292`**, job **`101998967311 SUCCESS`**, workflow head **`b02625a459dcc21f2497752becc5798a574db7b3`**, exact token `PASS_EXP073HA_C2_NATIVE_EXACT_ENDPOINT_EXTRACTION_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`, `cosmological_run_started=false`, `record_payload_created=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

HA verified pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` source blobs, native exact-k insertion route, solver-native literal-z coordinate resolution, standard nonzero-z interpolation route as forbidden for raw C2 records, and NDF15 terminal accepted-state mechanics. No runtime payload or science authority was produced.

HA PASS authorizes only prospective implementation and hosted build/static audit of the diagnostic-only exact-endpoint producer patch. Real 28-packet / 1792-byte C2 runtime remains blocked while GA owns the home-heavy runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
