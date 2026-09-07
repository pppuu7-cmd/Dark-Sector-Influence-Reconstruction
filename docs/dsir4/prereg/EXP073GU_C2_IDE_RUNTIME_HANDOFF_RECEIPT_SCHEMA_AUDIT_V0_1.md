# Exp073GU — C2 IDE runtime handoff/receipt schema audit v0.1

Status: PROSPECTIVELY FROZEN after raw-validated Exp073GT support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Frozen upstream authority

Exp073GT run `34131162547`, job `101771357352`, raw-validated exact token `PASS_EXP073GT_C2_IDE_DRYRUN_RECORD_ENVELOPE_AUDIT_V0_1` and deterministic dry-run envelope manifest SHA256 `d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8`.

Inherited immutable identities:
- GR contract SHA256 `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`;
- solver head `ac627d54e9ce196a08878d1ba33999819925d19c`;
- recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`;
- exactly 28 requests, ordinals `0..27`, z-major/k-minor;
- record ABI exactly 8 binary64 fields / 64 bytes;
- all GT payloads null, status `AWAITING_EXACT_RUNTIME_RECORD`.

## Purpose

Freeze only a deterministic metadata handoff and receipt schema for a future runtime producer. No CLASS build/run, no recorder payload, no cosmological value and no scientific prediction may be created.

## Frozen handoff schema

A handoff packet must contain exactly:
- `schema = dsir.c2.runtime_handoff.v0.1`;
- `gt_manifest_sha256` equal to the frozen GT manifest SHA256;
- `gr_contract_sha256` equal to the frozen GR contract SHA256;
- frozen `solver_head` and `recorder_blob_sha1`;
- `request_count = 28`, `record_bytes = 64`, `record_field_count = 8`;
- `ordering = z_major_k_minor`;
- `payload_state = ABSENT_BY_CONTRACT`;
- `prediction_ready = false`.

A receipt for request ordinal `i` must contain only metadata:
- `schema = dsir.c2.runtime_receipt.v0.1`;
- exact `ordinal`, `z`, `k_Mpc^-1` copied from the GT envelope;
- exact inherited GT/GR/source/recorder identities;
- `expected_record_bytes = 64`;
- `received_record_bytes = 0`;
- `receipt_status = DRY_RUN_NO_PAYLOAD`.

Exactly 28 receipts must be produced in ordinal order. Any coordinate/order/identity/count/width mutation must fail closed. No payload bytes may be accepted or synthesized in this gate.

## Hosted audit

Hosted-only audit must verify deterministic packet/receipt assembly, exact 28 receipt count/order/coordinates, zero received payload bytes, fail-closed mutations, deterministic canonical SHA256 fingerprints, absence of solver/build/rescue paths, and emit exact token:

`PASS_EXP073GU_C2_IDE_RUNTIME_HANDOFF_RECEIPT_SCHEMA_AUDIT_V0_1`

## Classification

PASS is only `SUPPORT_PLUS_0_PLUS_0`: `cosmological_run_started=false`, `self_hosted_science_started=false`, `record_payload_created=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any mismatch is implementation/infrastructure `+0/+0`, never scientific model FAIL. PASS does not authorize real cosmological extraction while Exp073FW owns the home runner.
