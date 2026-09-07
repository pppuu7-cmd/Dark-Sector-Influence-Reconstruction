# DSIR recovery — Exp073FY active / Exp073GZ preregistered V20

Date: 2026-09-07. Scope: DSIR only.

## Heavy authority

Exp073FY `WW_S2_S3` run `34147009217`, head `f04346a8e6909cb4342e536a0e7328f5ca5e54c9`, remains the sole home-heavy owner. Hosted job `101821110137` is SUCCESS; home job `101821144414` remains IN_PROGRESS inside `Run frozen WW_S2_S3 A/B gate with durable checkpoints`. No competing heavy run was launched and no partial FY numerical result was inspected.

Frozen FY/FZ governance and the prospectively hardened GA successor remain unchanged from V19.

## Independent C2 progress while FY owns home

Repository commit `a8499c404aa2b862cc08634fe4ed20d2753c9f25` froze `docs/dsir4/mappings/C2_IDE_RUNTIME_ADMISSION_RECEIPT_CONTRACT_V0_1.md`, Git blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`. The contract remains support-only `+0/+0`: it binds a future complete 28-packet / 1792-byte raw runtime record set to exact producer/build/config/model-point/coordinate/provenance identities while keeping `decoded=false`, `mapped=false`, `prediction_ready=false`, and scientific authority false.

Exp073GZ was prospectively preregistered in commit `d5791df0c81169c9a3797ac1867b921028097579` at `docs/dsir4/prereg/EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1.md`. Its exact PASS token is `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`; PASS can only be `SUPPORT_PLUS_0_PLUS_0` and cannot authorize a home runtime launch while FY owns the runner.

A new hosted workflow installation was attempted after preregistration but was rejected by the connector/platform write-safety layer before any repository write occurred. This is an execution-tool limitation only; no workflow run, scientific result, contract change, or authority was produced. Do not weaken or bypass the audit contract. A later iteration may use an already-authorized hosted audit path or another repository-native non-home audit mechanism.

## Exact next actions

1. Terminal-consume FY `34147009217` immediately when it finishes; verify artifacts, complete A/B chains, provenance, ordered distinct S2->S3 semantics, exact file-backed proof, finiteness and exact A/B equality before FZ admission.
2. Do not launch GA unless the frozen FZ admission succeeds; GA remains prospectively hardened and dispatch-only.
3. Separately execute Exp073GZ using a hosted/non-home audit path when available. Until then GZ is PREREGISTERED/BLOCKED_BY_AUDIT_EXECUTION_PATH, not PASS/FAIL.
4. Real C2 28-packet runtime production remains BLOCKED while FY owns home and also requires GZ static-audit PASS first.
