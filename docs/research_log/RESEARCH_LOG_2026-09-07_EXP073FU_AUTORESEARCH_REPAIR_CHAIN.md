# Exp073FU auto-research repair chain — 2026-09-07

## Scope

This log records infrastructure/orchestration faults encountered while restoring the frozen `WW_S1_S3` Exp073FU chain. None of the failures below reached an admissible scientific terminal result. They therefore contribute **+0/+0 scientific support** and MUST NOT be interpreted as a DSIR model/gate FAIL.

Frozen scientific identity is unchanged throughout: source pair `S1->S3`, ordered source indices `[1,3]`, predecessor Exp073FS/FT authority, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, exact file-backed route, and no tolerance/rescue path.

## Incident 1 — false-positive rescue scanner

- Failed run: `34087011068`
- Failed self-hosted job: `101632910644`
- Symptom: immediate `fail-closed tolerance/rescue path` before any science computation or artifact.
- Root cause: the FU wrapper recursively transformed/scanned the inherited FS wrapper. The FS wrapper intentionally contains the forbidden strings (`np.allclose`, `np.isclose`, rescue labels) inside its own fail-closed detector, so the intermediate-wrapper scan matched guard text rather than an executable science rescue path.
- Classification: `INFRASTRUCTURE_ORCHESTRATION_FALSE_POSITIVE`, scientific contribution `+0/+0`.
- Repair commits in chronology: `07de7028dd2cb8baf1927ddcdbceef812bda45f3` (remove intermediate false-positive scan) and later direct-base hardening superseding the recursive transform.

## Incident 2 — recursive transformed-shell syntax failure

- Repaired attempt run: `34089002710`
- Hosted launch audit: PASS.
- Failed self-hosted job: `101638555789`.
- Exact terminal technical error: generated shell `exp073fu_home_filebacked_fullres_v0_1.transformed.sh: line 72: syntax error near unexpected token '('`.
- No science compute began; provenance admission was skipped.
- Classification: `INFRASTRUCTURE_GENERATOR_SYNTAX_FAILURE`, scientific contribution `+0/+0`.
- Repair: replace recursive FS-wrapper transformation with a direct transformation from the immutable FA authority wrapper and add `bash -n` on the generated executable before `exec`.
- Direct-base repair commit: `fa01c7d7a2d20cd222c1d208ac4e359ad1313710`.
- Repaired wrapper blob after this step: `7dcde986e4621a3bdf75562170444e1608114504`.

## Duplicate-run guard

A race between two one-shot recovery triggers produced two candidate repaired runs. The guard kept only one recovery path and issued an explicit cancellation for queued duplicate run `34089005639` through hosted helper run `34089131000` / job `101638888449`. No second heavy science computation was intentionally allowed to proceed from that duplicate recovery branch.

The duplicate/cancel helper is infrastructure-only and must never be read as science evidence.

## Incident 3 — inherited storage-audit provenance variables missing

- Run: `34089259696`
- Hosted launch audit: PASS.
- Failed self-hosted job: `101639297762`.
- Exact technical error before science compute: `EM_GENERATOR_BLOB: parameter null or not set`.
- Cause: direct generation from the frozen FA wrapper correctly restored the FA storage-activation path, but FU workflow did not export the two immutable Exp073EM storage-audit helper identities previously present in the FS lineage.
- Classification: `INFRASTRUCTURE_PROVENANCE_BINDING_FAILURE`, scientific contribution `+0/+0`.
- Repair: bind the exact inherited storage-audit identities inside the FU wrapper, without changing any science parameter:
  - `EM_GENERATOR_BLOB=bd1795f2a2c2cf80341f212996eb8278e0be53d9`
  - `EM_COMPARE_BLOB=f0de92f3f121592b6d139eb7d948426946d901d1`
- Commit: `614c5bca01280792b5ea0affe93729fbea174d40`.
- Resulting wrapper blob: `4e6d24fc26760c7e7d31545837239148269d81d5`.

## Current authorized recovery run

- Run: `34089383137` — Exp073FU `WW_S1_S3`.
- Trigger head: `11b62ebd73fe8bed03f31c559593756149c7fbc0`.
- Hosted launch audit job `101639612389`: **SUCCESS**.
- Self-hosted `home-science` job `101639652148`: **IN_PROGRESS** at the time of this log.
- This is the single authorized heavy recovery run to watch. Do not dispatch another Exp073FU heavy run while it is queued/in-progress.
- Do not interpret partial checkpoints. Only terminal evidence followed by frozen provenance admission can create scientific authority.

## Scientific status

No scientific FAIL was produced by any incident in this chain. All failures occurred before an admissible terminal scientific result.

C2/DSIR4 status is unchanged by these infrastructure repairs: `mapping_ready=true`, prediction/admission remains incomplete, and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE` until its own deterministic prediction artifact and Gate-1 admission are completed.

## Next guard action

1. Poll run `34089383137` to terminal state without launching a duplicate.
2. If `home-science` succeeds, verify hosted provenance admission and successor dispatch before calling the authority created.
3. If it fails, inspect the terminal log and classify infrastructure vs genuine frozen science outcome. Repair only technical faults; do not alter frozen equations, thresholds, contract fingerprint, source pair, or hypothesis ID.
4. In parallel only while the heavy run is healthy, continue the next allowed static DSIR4 mapping/prediction-preparation work.
