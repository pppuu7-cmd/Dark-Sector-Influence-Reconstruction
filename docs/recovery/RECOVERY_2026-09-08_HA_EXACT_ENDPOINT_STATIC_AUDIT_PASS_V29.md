# DSIR recovery — 2026-09-08 Exp073HA exact-endpoint static audit PASS V29

Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved authority

All authority from V28 is preserved. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW authority through `WW_S2_S3` remains admitted; `WW_S3_S3` remains NOT_YET_ADMITTED. Exp073GA recovery run `34197207582` remains the single home-heavy owner; do not duplicate it or inspect partial numerical output.

## Exp073HA hosted static audit

Prospective preregistration: `docs/dsir4/prereg/EXP073HA_C2_NATIVE_EXACT_ENDPOINT_EXTRACTION_STATIC_AUDIT_V0_1.md`, creation commit `33b7bc35401bef01f436b433e5c7ebf9bab0cb4f`, blob `f970da98a91f541e62aa957b16aaf4ea12bd98a7`.

Hosted workflow implementation commit: `b02625a459dcc21f2497752becc5798a574db7b3`.

Validated Actions result:

- run `34207078292`;
- job `101998967311`;
- status/conclusion: COMPLETED / SUCCESS;
- exact token: `PASS_EXP073HA_C2_NATIVE_EXACT_ENDPOINT_EXTRACTION_STATIC_AUDIT_V0_1`;
- classification: `SUPPORT_PLUS_0_PLUS_0`;
- `cosmological_run_started=false`;
- `record_payload_created=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

The raw hosted log was inspected, not merely workflow status. It verified the exact preregistration blob and cloned pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; Git blob identities for `source/perturbations.c` and `tools/evolver_ndf15.c` matched the frozen hashes `92a48331658c5941ed4eb43b0e98ee78e39b8385` and `790ced55f2eaa08e805d467734ad1435954bc5b7`.

The static audit fail-closed checked the native exact-k output-value route, solver-native `background_tau_of_z` coordinate resolution, the fact that normal nonzero-z output uses `perturb_sources_at_tau` interpolation and is therefore forbidden for the raw C2 record, and NDF15 terminal-step/accepted-state mechanics including explicit stretch to `tfinal`, `ynew`, output/derivative callback paths, and separation from `interp_from_dif`.

Scientific ceiling remains exactly +0/+0: no CLASS cosmological run, no payload, no decoding/mapping/prediction, and no model authority was created.

## Next permitted C2 action

Exp073HA PASS authorizes only prospective implementation plus hosted build/static audit of a diagnostic-only exact-endpoint producer patch under the frozen architecture. Real 28-packet / 1792-byte C2 runtime remains blocked while Exp073GA owns the self-hosted heavy runner. Any future diagnostic producer must preserve exact requested k insertion, literal-z native coordinate resolution, terminal accepted `ynew` capture, pre-transform `delta_m/theta_m`, no perturbation-state interpolation, no tolerance/nearest-neighbour rescue, and single-thread diagnostic side-channel semantics if global state is used.

## GA current process preserved

Authoritative GA recovery remains run `34197207582`, head `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`; hosted job `101967492875 SUCCESS`; home job `101967543808 IN_PROGRESS`; checkpoint root `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`; last verified durable checkpoint Replica A `replica_receipt_complete`. Candidate token remains `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; final authority requires separate GB token `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s3_s3_authority_created=true`.
