# Exp073DE v0.3 — hosted runtime repair for exact full-window resume gate

Date: 2026-09-04. Scope DSIR only. Support/infrastructure `+0/+0`.

## Historical predecessor
Exp073DE v0.2 run/job `33885325120 / 101063561505` is immutable `Q4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL +0/+0`. Its source-freeze step passed, but raw artifact `9941575908` (independently verified ZIP SHA256 `348a55e4754cb472f62bb95efdfacb4d5c783664a756245ddb57bf595eae5876`) contained only an empty stdout log and no receipt/classification. Thus exactness was never evaluated.

## Frozen repair
The exact resume helper remains byte-for-byte unchanged at blob `210775ebf9b3f1aad9ade0ea0d095848c1481c0f`. This version changes only the hosted execution shell:
1. provision an explicit Python `numpy` dependency before running the helper;
2. capture stderr and stdout together into the durable raw log;
3. if receipt creation fails, emit an explicit `Q4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL` classification artifact rather than relying on a later file-open exception;
4. preserve all v0.2 exactness and fail-closed criteria unchanged.

The same frozen classifications apply: Q1 exact PASS, Q2 exactness FAIL, Q3 fail-closed semantics FAIL, Q4 infrastructure/source-binding FAIL. No DES-scale science, Exp073BU activation or Wm_S3 authority creation is permitted.
