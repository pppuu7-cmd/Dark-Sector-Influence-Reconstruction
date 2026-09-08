# Exp073IC — C2 tangent finite-difference response candidate v0.1

Status: PROSPECTIVELY FROZEN AFTER Exp073IB v0.2 MAP PASS AND BEFORE RESPONSE CALCULATION.

## Authority inputs
- Reference common-coordinate authority: Exp073HW run `34242852819`, artifact `10062705321`, ZIP SHA256 `7ea327f0d6e29e4b415c9f66201b266e9015d46a383e8867de94b05665517c00`, bridge JSONL SHA256 `2b6eb07c99273292bcb2cf929295071e401e81ed51cfe3f4c3b19d5a395518fb`.
- Tangent mapped authority: Exp073IB v0.2 run `34249229753`, job `102139059309`, artifact `10065286473`, ZIP SHA256 `965e921224f516e76e9cf2d2ac84ed51a5027b97d79c73c87620d55a83011201`, PASS `PASS_EXP073IB_C2_TANGENT_DELTAM_COMMON_COORDINATE_MAP_V0_2`.
- Frozen point definitions: Exp073HX prereg blob `e00d972504abb2ec102f9fc09f0e57af1bccf33e`. HX explicitly freezes one-sided alpha and symmetric beta definitions and derivative base step `1e-4`, with additional scales `1e-3` and `1e-2` already generated as controls.

## Purpose and ceiling
Compute deterministic finite-difference response **candidates** at all three prospectively frozen scales. This gate does not judge convergence/stability, select a scale post hoc, extrapolate to zero step, fit a model, smooth/average responses, create a prediction, or create scientific model authority.

## Frozen arithmetic
For each of the exact 28 request IDs, let `R` be reference `Delta_m` from HW, and tangent mapped values be `A_h = Delta_m(alpha=-h,beta=0)`, `B+_h = Delta_m(alpha=0,beta=+h)`, `B-_h = Delta_m(alpha=0,beta=-h)`.

For each `h` in exact ordered decimal set `1e-4,1e-3,1e-2`, interpreted as Python binary64 via `float(decimal_literal)`, execute exactly:

### Alpha one-sided response
1. `alpha_numerator = A_h - R`
2. `alpha_denominator = -h`
3. `dDelta_dalpha_h = alpha_numerator / alpha_denominator`

### Beta symmetric response
1. `beta_numerator = Bplus_h - Bminus_h`
2. `beta_denominator = 2.0 * h`
3. `dDelta_dbeta_h = beta_numerator / beta_denominator`

No algebraic reassociation, Richardson extrapolation, tolerance, rounding, smoothing, averaging, scale selection, effective coordinate or replacement result is permitted. Fail closed on any request-order mismatch or nonfinite input/output.

Canonical output is one compact newline-terminated JSONL with 28 rows in exact z-major/k-minor request order. Each row contains `request_id` followed by exact `float.hex()` fields, in this order:
- `dDelta_dalpha_h1e4_hex`, `dDelta_dbeta_h1e4_hex`
- `dDelta_dalpha_h1e3_hex`, `dDelta_dbeta_h1e3_hex`
- `dDelta_dalpha_h1e2_hex`, `dDelta_dbeta_h1e2_hex`

The h=`1e-4` pair is the frozen base-step response candidate. h=`1e-3` and `1e-2` remain controls only. No comparison between scales has acceptance meaning in this gate.

PASS token: `PASS_EXP073IC_C2_TANGENT_FINITE_DIFFERENCE_RESPONSE_CANDIDATE_V0_1`.

On PASS only:
- `classification=TANGENT_RESPONSE_CANDIDATE_PLUS_0_PLUS_0`
- `mapped_reference_coordinate=true`
- `mapped_tangent_coordinate=true`
- `response_candidate_created=true`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

A PASS authorizes only a separately prospectively frozen response stability/admission gate. It does not itself establish a scientifically admitted tangent response.