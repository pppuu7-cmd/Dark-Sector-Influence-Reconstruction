# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities are `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and `S2_S3`. `WW_S3_S3` remains **NOT_YET_ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-08_HA_EXACT_ENDPOINT_STATIC_AUDIT_PASS_V29.md` (creation commit `f02ad2ff93f005c08ce3b7c17564bda490d3d3ea`).

## Authoritative current heavy process — Exp073GA recovery

- workflow/run: **`34197207582`**;
- workflow: `.github/workflows/exp073ga-ww-s3-s3-home-science-v0-1.yml`;
- branch/head: `main` / **`f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`**;
- run start: `2026-09-08T07:00:11Z`;
- hosted launch-audit job: **`101967492875 SUCCESS`**;
- hosted tokens: `PASS_EXP073GA_PRUNER_TRANSFORM_SOURCE_STATIC_REGRESSION_V0_1`, `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_3`, classification `SUPPORT_PLUS_0_PLUS_0`;
- self-hosted home-science job: **`101967543808 IN_PROGRESS`**;
- active step: `Run frozen WW_S3_S3 A/B gate with durable checkpoints`;
- runner ownership: **single self-hosted DSIR owner; no competing home-heavy work**;
- checkpoint root: `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`;
- last verified durable checkpoint: Replica A `replica_receipt_complete` from historical run `34189540992`, to be restored/verified rather than recomputed;
- expected candidate token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- final authority token: `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` plus `classification=SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s3_s3_authority_created=true`.

SUCCESS action: consume raw home log/artifact and verify exact digest, code/source/contract/checkpoint identities, complete A+B chains, same-field `S3->S3/[3,3]`, exact file-backed MCM evidence, finite canonical arrays, exact SHA equality and `numpy.array_equal`; only then accept GB admission. FAIL action: diagnose first causal defect, preserve verified checkpoint stages, and never weaken science.

Historical GA run `34189540992` remains implementation/infrastructure FAIL `+0/+0`; its expensive Replica A is valid and preserved. Minimal repair commit `f52fa856eb029c64f744926eecf55f506fcf1da5`; rebinding/regression commit `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`.

## Independent C2 frontier

Exp073GZ receipt-contract audit remains PASS `SUPPORT_PLUS_0_PLUS_0`.

Exp073HA static audit is now **PASS `SUPPORT_PLUS_0_PLUS_0`**:

- prereg commit `33b7bc35401bef01f436b433e5c7ebf9bab0cb4f`, prereg blob `f970da98a91f541e62aa957b16aaf4ea12bd98a7`;
- workflow implementation head `b02625a459dcc21f2497752becc5798a574db7b3`;
- run `34207078292`, job `101998967311 SUCCESS`;
- exact token `PASS_EXP073HA_C2_NATIVE_EXACT_ENDPOINT_EXTRACTION_STATIC_AUDIT_V0_1`;
- `cosmological_run_started=false`, `record_payload_created=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Next C2 action: prospectively implement and hosted-build/static-audit a diagnostic-only exact-endpoint producer patch under the frozen HA architecture. Real 28-packet / 1792-byte runtime remains `BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY` while GA owns the self-hosted runner. No home C2 job may be launched concurrently.

## Frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
