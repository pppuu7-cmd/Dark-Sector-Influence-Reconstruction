# Exp073GT — C2 IDE dry-run record-envelope assembly audit v0.1

Status: PROSPECTIVELY FROZEN after Exp073GS hosted support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Authority inherited from Exp073GS

The only admitted sampling contract is `scripts/dsir4/fixtures/dsir_c2_runtime_sampling_provenance_contract_v0_1.json`, canonical SHA256 `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`. The only admitted deterministic request emitter is `scripts/dsir4/fixtures/dsir_c2_runtime_request_emitter_v0_1.py`. Solver lineage remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; recorder blob remains `c6144598b9f75908ee27a517d31eda509f7947f6`.

## Purpose

Exp073GT may assemble a dry-run envelope for each of the 28 already frozen runtime requests. It must not clone, build or execute CLASS, must not fabricate numerical recorder values, and must not create a scientific prediction. The envelope is orchestration metadata only.

## Frozen envelope semantics

For each request from Exp073GS, emit exactly one envelope containing:

- `ordinal`, `z`, and `k_Mpc^-1` copied exactly from the admitted request;
- `record_schema = dsir_c2_record_v0_1`;
- `record_fields = [tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv]` in that exact order;
- `record_field_count = 8` and `record_bytes = 64`;
- `solver_head = ac627d54e9ce196a08878d1ba33999819925d19c`;
- `recorder_blob_sha1 = c6144598b9f75908ee27a517d31eda509f7947f6`;
- `runtime_status = AWAITING_EXACT_RUNTIME_RECORD`;
- `record_payload = null`.

The assembler must reject any input request list that is not exactly the admitted 28-request z-major/k-minor sequence. It must fail closed if the contract fingerprint, solver identity, recorder identity, record width/count, units, ordering, or prohibited-transformation flags differ from the admitted contract.

No interpolation, extrapolation, smoothing, averaging, tolerance matching, nearest-neighbour selection, rounding rescue, effective-coordinate substitution, fiducial-P shortcut, synthetic cosmological value, or coordinate arithmetic may be introduced.

## Hosted audit

A hosted-only audit must independently verify:

1. exactly 28 envelopes and ordinals `0..27`;
2. exact equality of every envelope coordinate to its request coordinate;
3. exact recorder schema/field order/width/count and frozen solver/recorder identities;
4. every `record_payload` is null and every runtime status is `AWAITING_EXACT_RUNTIME_RECORD`;
5. mutation, reordering, deletion, duplication, or coordinate change of a request fails closed;
6. no solver invocation/build path exists in the assembler;
7. deterministic canonical SHA256 of the full envelope manifest;
8. exact token `PASS_EXP073GT_C2_IDE_DRYRUN_RECORD_ENVELOPE_AUDIT_V0_1`.

## Classification

PASS is only `SUPPORT_PLUS_0_PLUS_0` with `cosmological_run_started=false`, `self_hosted_science_started=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any implementation/static/provenance mismatch is infrastructure/support failure `+0/+0`, never a scientific model FAIL. PASS may authorize a separately frozen runtime handoff/receipt-schema audit, but not a real cosmological extraction while another heavy-run is active.
