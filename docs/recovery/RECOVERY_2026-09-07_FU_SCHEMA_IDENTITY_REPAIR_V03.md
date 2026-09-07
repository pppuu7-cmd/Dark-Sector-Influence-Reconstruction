# DSIR recovery — Exp073FU schema identity repair v0.3

Date: 2026-09-07. Scope: DSIR only; never mix RTK/RQIR.

## Preserved scientific authority

All previously admitted Wm and WW authorities remain unchanged. In particular, WW_S1_S2 remains admitted only by Exp073FT. WW_S1_S3 remains NOT ADMITTED.

## Terminal Exp073FU state

Exp073FU run 34089383137 is terminal infrastructure/implementation FAIL +0/+0; it created no WW_S1_S3 scientific authority and uploaded no authority artifact. Durable checkpoints under ~/.cache/dsir/exp073fu-ww-s1-s3-filebacked-ab-v0-1 are preserved and must not be recomputed unless their own fail-closed verification fails.

## Read-only diagnostic sequence

Run 34100007783 attempt 3, job 101674791800, reached user code and failed at `fail-closed stage identity fresh_sources_complete`; earlier transient checkout/SSL attempts are not the causal software defect.

Diagnostic v0.5 run 34103112711, job 101681869890, printed the preserved A-stage identity before running the pruner. The durable manifest is internally correct:
- schema = dsir.exp073fu.ww_s1_s3.durable_ab_production.v0.1.checkpoint
- stage = fresh_sources_complete
- complete = true
- replica = A
- checkpoint_namespace = checkpoints/exp073fu-ww-s1-s3-a-v0-1
- source_head = de83e20a68f79ccf25b89b0d33eb4206e294c757
- contract_fingerprint = b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251
- historical_ww_numerical_import = false
- other_replica_output_read = false

This proves the checkpoint identity itself is not the defect. The first causal implementation defect is the transformed FU pruner: it transformed `exp073fs`, source-pair and hyphenated checkpoint namespace, but omitted the underscore schema transform `ww_s1_s2 -> ww_s1_s3`, leaving the transformed expected SCHEMA inconsistent with the valid FU checkpoint.

## Prospective repair

Commit dabb334aecaf924ad5a48ac495a5447deb4c6583 updates only ci/exp073fu_verify_and_prune_replica_v0_2.py to add the missing underscore schema transform plus fail-closed required/stale checks. New blob: b9ed7d7178424fb656b4a7c7bfb2ee370c751cb0. No scientific arithmetic, source domain, acceptance criterion, source_head, contract fingerprint, source ordering, field semantics, or tolerance rule changed.

Commit 2f5e33324ef032bb048e43acc27e8e6a94ccb2cc binds the read-only validation workflow to that exact repaired blob. Run 34103206078, job 101682164394, was IN_PROGRESS at this note's creation. It runs only against a nonmutating symlink mirror and must prove original_checkpoint_mutated=false plus PASS_EXP073FU_REPLICA_A_REPAIRED_PRUNER_READONLY_VALIDATION_V0_6 before any FU resume is permitted.

## Exact next action

1. Consume run 34103206078 raw log when terminal.
2. On PASS, classify as infrastructure/support +0/+0 validation only, then prospectively resume Exp073FU from preserved verified durable checkpoints without competing home jobs.
3. On failure, diagnose the first new causal defect from raw log; do not weaken or alter frozen science.
4. Only a future fully validated FU candidate artifact may permit Exp073FV authority admission. Candidate workflow success alone is never scientific PASS.
