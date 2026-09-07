# DSIR Auto-Guard — Exp073GZ hosted static audit PASS while Exp073FY remains active

Date: 2026-09-08
Scope: DSIR4 only. No frozen scientific logic, threshold, contract, ordering, or hypothesis ID changed.

## Primary heavy-chain status

- Active target: `Exp073FY / WW_S2_S3`.
- Run ID: `34160898921`.
- Head SHA: `b5c8a059a014bee5d318d6067f7a2fac37c5b173`.
- `hosted-launch-audit` job `101862362835`: `SUCCESS`.
- `home-science` job `101862390771`: `IN_PROGRESS` at the repaired frozen `WW_S2_S3 A/B gate` at this audit turn.
- Invalid S3-S3-labelled FY checkpoints were retired by the already-recorded prospective namespace repair; no historical scientific payload was relabelled into authority.
- No duplicate home-heavy run was started.
- Scientific state remains `WW_S2_S3 = NOT_YET_ADMITTED` until terminal FY evidence and the separately required Exp073FZ provenance admission.

No new primary infrastructure failure was observed in this turn. An in-progress heavy step is not classified as scientific FAIL and partial output is not interpreted.

## Exp073GZ recovery from execution-path block

Frozen preregistration:
- `docs/dsir4/prereg/EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1.md`
- prereg commit: `d5791df0c81169c9a3797ac1867b921028097579`.

Frozen audited object:
- `docs/dsir4/mappings/C2_IDE_RUNTIME_ADMISSION_RECEIPT_CONTRACT_V0_1.md`
- required and observed Git blob: `1c2e30e6563efe3976ee0b1825dfb250a902a529`.

The previous `BLOCKED_BY_AUDIT_EXECUTION_PATH` condition was infrastructure/tooling-only. A repository write path became available without altering the frozen object, so a dedicated hosted-only audit workflow was added:

- workflow: `.github/workflows/exp073gz-c2-runtime-admission-receipt-static-audit-v0-1.yml`
- binding commit: `a4961a87432f53bc55a13c7f542a8775634b90bd`
- GitHub Actions run: `34168323933`
- job: `101883674574`
- conclusion: `SUCCESS`
- exact PASS token emitted by the frozen check: `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`.

The hosted audit checks the frozen blob identity and the preregistered invariants for hypothesis ID, solver lineage, 28-packet grid/order, 64-byte packet/1792-byte aggregate widths, producer/artifact/SHA provenance, fail-closed pre-admission rules, and the distinctions among `INVALID_FOR_SCIENCE`, `OUTSIDE_DOMAIN`, `NOT_YET_TESTABLE`, and scientific FAIL.

## Scientific classification

Exp073GZ PASS classification is exactly:

- `SUPPORT_PLUS_0_PLUS_0`;
- `raw_record_set_admitted=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`;
- scientific FAIL contribution: `0`.

This audit does not execute CLASS, does not decode/mutate runtime records, does not run the home runner, and does not launch the next real C2 runtime producer while `Exp073FY` owns the heavy-run chain.

## Next allowed transitions

1. Primary DSIR4 path: wait for terminal `Exp073FY` evidence; only then run/accept Exp073FZ provenance admission. `Exp073GA / WW_S3_S3` remains forbidden before that authority transition.
2. C2 path: Exp073GZ now authorizes only the already-frozen future real runtime producer transition, and only when heavy-run exclusivity is clear. Decoding, observable mapping, and scientific comparison remain separate later gates.

Nothing in this turn converts infrastructure failure, `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, or `OUTSIDE_DOMAIN` into scientific FAIL.
