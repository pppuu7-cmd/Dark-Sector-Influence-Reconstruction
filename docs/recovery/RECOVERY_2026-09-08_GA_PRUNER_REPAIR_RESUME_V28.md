# DSIR recovery — 2026-09-08 GA pruner repair/resume V28

Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW authorities through `WW_S2_S3` remain admitted. `WW_S3_S3` remains **NOT_YET_ADMITTED**. No historical result is rewritten.

Frozen Exp073GA science remains exactly the prospective `WW_S3_S3`, `[3,3]`, `S3->S3`, same-field-object, DES NSIDE=4096, ell 0..12287, 39-band, canonical `<f8 [39,12288] EE<-EE` contract in `experiments/073ga_ww_s3_s3_filebacked_full_resolution_ab_science_v0_1_prereg.md`; final authority still requires the separate Exp073GB gate.

## Consumed failed GA run

Exp073GA run `34189540992`, head `10e6fb67af7d6485fca3d1ecf2362e4622883417`:

- hosted launch audit job `101944582891`: SUCCESS;
- home job `101944608861`: FAILURE;
- GB admission job `101964415971`: SKIPPED;
- evidence artifact `10043979600`, name `exp073ga-ww-s3-s3-filebacked-ab-v0-1`, GitHub digest `sha256:b859e658e1046c4d9905d589003a1d26aaf3e2601c51d9db361b48176226906a`; independently downloaded ZIP SHA256 matched exactly.

The first causal failure in the raw home log occurs **after Replica A completed its expensive six-stage production and replica receipt**, when `ci/exp073ga_verify_and_prune_replica_v0_1.py` raises:

`RuntimeError: fail-closed missing GA pruner token 'WW_S1_S1'`

The pinned FM base pruner contains the required lower-case/schema, hyphenated namespace, source-pair, index, payload and source-label tokens, but it does not contain the uppercase literal `WW_S1_S1`. Therefore the old GA wrapper imposed a false transformation requirement. Classification: **implementation/infrastructure FAIL `+0/+0`**, not a scientific arithmetic FAIL.

## Preserved expensive Replica A checkpoint evidence

The terminal artifact proves Replica A reached all six complete stages in namespace `checkpoints/exp073ga-ww-s3-s3-a-v0-1`, with frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, `historical_ww_numerical_import=false`, and `other_replica_output_read=false`.

A evidence includes:

- ordered source indices `[3,3]`, source pair `S3->S3`, same source map on both sides;
- S3 selected rows `4,196,641`, unique pixels `2,943,132`, source-map canonical SHA256 `2a65f24c7bed6a575118e7186c4596a11a2ffbd0c0260ea86981807275a12734`;
- one field construction, same field object handed to both coupling sides;
- file-backed public BPW route, MCM backing exactly `19,327,352,832` bytes, `/proc/self/maps` proof flags, and `no_tolerance_rescue=true`;
- full BPW SHA256 `fd7a6574d732f76fd2d8577937988b9e4f3683772f663b22014aaeebe995da04`;
- canonical selected `EE<-EE` `<f8 [39,12288]` SHA256 `e4aad74b8b733d280f4abfd6654778f0e037ab6060b12a908d30f8ec34c36c07`, independently read from the artifact as shape `[39,12288]` and all finite;
- replica receipt SHA256 chain preserved through `replica_receipt_complete`.

Replica B had not started. The durable home checkpoint root remains `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`; expensive A must be resumed/verified, not recomputed.

## Prospective minimal repair

A concurrent DSIR repository update committed the exact minimal wrapper repair as commit `f52fa856eb029c64f744926eecf55f506fcf1da5`, pruner blob `fc3e4d8444630e4b5a2dde0a052e1069b7887c01`: remove only the nonexistent uppercase `WW_S1_S1` transform requirement. Frozen science/arithmetic/domain/checkpoints/tolerances are unchanged.

Workflow binding was then prospectively updated in commit `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d` to pin that exact pruner blob and add a hosted regression asserting the real FM source-token set and explicitly asserting that `WW_S1_S1` is absent. Hosted audit emits `PASS_EXP073GA_PRUNER_TRANSFORM_SOURCE_STATIC_REGRESSION_V0_1` before allowing home compute.

## Current authoritative process

Exp073GA recovery run `34197207582`, head `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`:

- hosted launch-audit job `101967492875`: **SUCCESS**, including `PASS_EXP073GA_PRUNER_TRANSFORM_SOURCE_STATIC_REGRESSION_V0_1` and `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_3`, classification `SUPPORT_PLUS_0_PLUS_0`;
- home-science job `101967543808`: **IN_PROGRESS** on `Run frozen WW_S3_S3 A/B gate with durable checkpoints`;
- runner ownership: single self-hosted DSIR home owner; do not launch competing heavy work;
- checkpoint root: `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`;
- last verified durable checkpoint: Replica A `replica_receipt_complete` from failed run `34189540992`; this preserved A is valid pre-prune evidence and must be checkpoint-resumed/verified under the repaired wrapper.

## Exact next actions

If recovery GA succeeds, consume raw log and exact artifact, verify digest/provenance/complete A+B chains/same-field `S3->S3` semantics/file-backed proof/finiteness/exact SHA and `numpy.array_equal`, and require candidate token `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Only then may the frozen GB verifier admit authority using `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s3_s3_authority_created=true`.

If recovery GA fails, diagnose the first causal failure and preserve all verified checkpoints. No scientific criterion may be weakened. C2 real 28-packet runtime remains blocked while this home-heavy owner is active.
