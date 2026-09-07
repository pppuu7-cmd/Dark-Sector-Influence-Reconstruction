# Exp073GX — C2 IDE packet-set provenance receipt static audit v0.1

Status: PROSPECTIVELY FROZEN after raw-validated Exp073GW support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Frozen upstream authority

Exp073GW repaired hosted run `34141027839`, job `101802824730`, raw-validated exact token `PASS_EXP073GW_C2_IDE_RECORD_PACKET_SET_ADMISSION_STATIC_AUDIT_V0_1`.

Inherited identities include GT manifest SHA256 `d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8`, GR contract SHA256 `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`, solver head `ac627d54e9ce196a08878d1ba33999819925d19c`, recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`, GU handoff SHA256 `5ed0b924379f8ae961acd5d5b14171f96b3692972b2348cba3022d669a343931`, GU receipt-set SHA256 `bbcfffbc9845dfb74ef4b8fffbcd5f9851cc45d27272cf39595d62ce9f0d8075`, GW packet-set schema `dsir.c2.record_packet_set.v0.1`, exactly 28 packets, total record bytes 1792. The deterministic synthetic GW aggregate SHA256 observed in the raw hosted audit is `a98f9ca1f10a9b2bfc957fac81ed837d85bbb203a5f5f0d7ff369a2061bc78b7`; it is test-fixture evidence only, not scientific data authority.

## Purpose and frozen receipt

Freeze a fail-closed provenance receipt schema which can later seal one complete GV/GW-valid runtime packet set before scientific interpretation. Receipt schema: `dsir.c2.packet_set_provenance_receipt.v0.1`. It must bind exact packet-set aggregate SHA256, packet count 28, total bytes 1792, all inherited identities above, exact coordinate-order identity `z-major/k-minor`, and flags `decoded_field_values_inspected=false`, `scientific_mapping_applied=false`.

The receipt digest is SHA256 of a canonical UTF-8 LF-terminated `key=value` stream using a prospectively fixed key order. No JSON serialization, float formatting, tolerance, rounding, interpolation, smoothing or averaging is permitted.

Hosted audit uses only the deterministic synthetic GW set. It must accept the exact receipt, recompute its digest independently, and fail closed on aggregate mutation, packet-count/byte-total mutation, any upstream provenance mutation, ordering mutation, schema mutation, or either forbidden flag becoming true. No CLASS build/run, no self-hosted job, no decoded scientific values.

Exact PASS token: `PASS_EXP073GX_C2_IDE_PACKET_SET_PROVENANCE_RECEIPT_STATIC_AUDIT_V0_1`.

PASS classification is only `SUPPORT_PLUS_0_PLUS_0`: `synthetic_test_vectors_only=true`, `scientific_record_set_admitted=false`, `cosmological_run_started=false`, `self_hosted_science_started=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. Any mismatch is implementation/infrastructure `+0/+0`, never scientific model FAIL.