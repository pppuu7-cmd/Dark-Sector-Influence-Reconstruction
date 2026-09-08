# Exp073IA — C2 tangent raw ABI decode v0.1

Status: PROSPECTIVELY FROZEN AFTER Exp073HZ ADMISSION PASS AND BEFORE DECODE EXECUTION.

## Authority input
Exp073HZ run `34248477503`, job `102136488451`, head `edaa94d42b18f45a6e0659dc23399793e0228830`, exact raw-log token `PASS_EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1`, classification `TANGENT_RAW_SET_ADMITTED_PLUS_0_PLUS_0`, `tangent_raw_set_admitted=true`, `decoded=false`.

## Purpose
Deterministically decode the admitted nine Exp073HY raw aggregates under the frozen native C ABI only. No physical mapping, `Delta_m`, derivative, fit, extrapolation, prediction, smoothing, tolerance, rounding or model interpretation is permitted.

Frozen record ABI from blob `c6144598b9f75908ee27a517d31eda509f7947f6`: eight native binary64 values in this exact order:
`tau, k, a, H, delta_m, theta_m, rho_idm_iv, rho_iv`.
Each packet is exactly 64 bytes; each model aggregate is 28 packets in exact z-major/k-minor order.

The decoder must use Python `struct.unpack('=8d', packet)` on the GitHub-hosted little-endian x86_64 runner after explicitly asserting `sys.byteorder == 'little'`, `struct.calcsize('=8d') == 64`, and all decoded values finite. This is an ABI decode, not a numerical transformation.

Canonical output per model is UTF-8 JSON Lines with 28 lines, one per `z00k00..z06k03`, keys in exact order `request_id,tau_hex,k_hex,a_hex,H_hex,delta_m_hex,theta_m_hex,rho_idm_iv_hex,rho_iv_hex`, compact separators, newline terminated. Every numerical value is represented by Python `float.hex()` so the binary64 payload is represented exactly and can be bitwise round-tripped.

The gate must also round-trip every decoded field via `float.fromhex` + `struct.pack('=8d', ...)` and require byte equality to the original 64-byte packet. It must output per-model canonical JSONL SHA256 and a manifest binding the nine model labels, HY artifact IDs/aggregate SHA256, HZ authority and IA decoder identity.

PASS token: `PASS_EXP073IA_C2_TANGENT_RAW_ABI_DECODE_V0_1`.

On PASS only:
- `classification=TANGENT_DECODED_RECORD_SET_PLUS_0_PLUS_0`
- `tangent_raw_set_admitted=true`
- `decoded=true`
- `mapped=false`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any ABI/size/order/finiteness/round-trip/provenance mismatch is fail-closed. A PASS here does not authorize tangent derivative calculation; a separate prospectively frozen physical common-coordinate mapping gate is required first.