# Exp073IB — C2 tangent Delta_m common-coordinate map v0.1

Status: PROSPECTIVELY FROZEN AFTER Exp073IA DECODE PASS AND BEFORE MAPPING EXECUTION.

## Authority input
Exp073IA run `34248722000`, job `102137324616`, head `c0e738d271954c6eb936e2b418165e0b1500b593`, artifact `10065081303`, GitHub ZIP SHA256 `6bf115c76d538f0691c1fcfa9d9a26721b9b593f26aceb2a7a59bdb7cc9aa0ce`, exact PASS token `PASS_EXP073IA_C2_TANGENT_RAW_ABI_DECODE_V0_1`, classification `TANGENT_DECODED_RECORD_SET_PLUS_0_PLUS_0`.

## Purpose
Map every admitted+decoded tangent record to the same previously frozen reference common coordinate used by Exp073HW. This gate performs mapping only. It does not calculate tangent derivatives, regressions, fits, extrapolations, predictions, likelihoods, or scientific model authority.

## Frozen physical bridge
For matter with `w_m=0`, use exactly once:

`Delta_m = delta_m + 3*a*H*theta_m/(k*k)`

where every operand is the binary64 value decoded by Exp073IA from the native endpoint record. No second gauge correction, sign change, tolerance, rounding, smoothing, averaging, effective coordinate, or fiducial shortcut is permitted.

Fail closed unless for every one of 9×28=252 records:
- all decoded input fields are finite;
- `k > 0` exactly;
- `rho_idm_iv > 0` exactly;
- `rho_iv >= 0` exactly;
- computed `Delta_m` is finite.

Canonical output per model: newline-terminated compact JSONL, exact request order `z00k00..z06k03`, keys `request_id,Delta_m_hex`, with `Delta_m_hex=float.hex(Delta_m)`. Output SHA256 is recorded for every model.

PASS token: `PASS_EXP073IB_C2_TANGENT_DELTAM_COMMON_COORDINATE_MAP_V0_1`.

On PASS only:
- `classification=TANGENT_MAPPED_COMMON_COORDINATE_PLUS_0_PLUS_0`
- `tangent_raw_set_admitted=true`
- `decoded=true`
- `mapped=true`
- `mapped_tangent_coordinate=true`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

A PASS here permits, but does not itself perform, a separate prospectively frozen finite-difference tangent-response gate. The reference `(0,0)` remains the already admitted HW reference; it is not recomputed.