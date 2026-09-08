# Exp073IB — C2 tangent Delta_m common-coordinate map v0.2

Status: PROSPECTIVELY FROZEN AFTER v0.1 IMPLEMENTATION/PROVENANCE AUDIT AND BEFORE v0.2 EXECUTION.

## Why v0.2 exists
Exp073IB v0.1 run `34248841106 / 102137736842` completed and its 252 mapped binary64 outputs were independently checked. However, its implementation evaluated the algebraically equivalent direct expression `delta_m + 3*a*H*theta_m/(k*k)` rather than explicitly reproducing the already-authoritative Exp073HW receipt operation order `hconf_then_velocity_term_then_add`. Although an independent bitwise audit found `0/252` output differences for the realized records, v0.1 is retained historically as `IMPLEMENTATION_PROVENANCE_FAIL_PLUS_0_PLUS_0`; workflow success is not promoted to mapping authority.

This v0.2 freezes the smallest causal repair only. No model point, coordinate, source payload, formula, threshold, data domain, or physical criterion changes.

## Authority input
Exp073IA run `34248722000`, job `102137324616`, artifact `10065081303`, ZIP SHA256 `6bf115c76d538f0691c1fcfa9d9a26721b9b593f26aceb2a7a59bdb7cc9aa0ce`, decoded record-set PASS.

Reference operation-order authority: Exp073HW run `34242852819`, artifact `10062705321`, ZIP SHA256 `7ea327f0d6e29e4b415c9f66201b266e9015d46a383e8867de94b05665517c00`, bridge JSONL SHA256 `2b6eb07c99273292bcb2cf929295071e401e81ed51cfe3f4c3b19d5a395518fb`, receipt literal `operation_order=hconf_then_velocity_term_then_add`.

## Frozen exact mapping arithmetic
For each decoded tangent record, execute exactly in this order in binary64 Python float arithmetic:

1. `hconf = a * H`
2. `velocity_term = 3.0 * hconf * theta_m / (k * k)`
3. `Delta_m = delta_m + velocity_term`

No reassociation, fused alternative, second gauge correction, tolerance, rounding, smoothing, averaging, effective coordinate, or fiducial shortcut is permitted.

Fail closed unless for every 9×28=252 record: all inputs finite; `k>0`; `rho_idm_iv>0`; `rho_iv>=0`; `hconf`, `velocity_term`, `Delta_m` finite. Canonical output per model is compact newline-terminated JSONL in exact z-major/k-minor order with keys `request_id,Delta_m_hex`, where `Delta_m_hex=float.hex(Delta_m)`.

As a regression guard, v0.2 must compare every canonical `Delta_m_hex` against the historical v0.1 artifact and require exact equality, while still classifying v0.1 itself as non-authoritative due to implementation-order provenance.

PASS token: `PASS_EXP073IB_C2_TANGENT_DELTAM_COMMON_COORDINATE_MAP_V0_2`.

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

A PASS permits only a separately prospectively frozen tangent-response calculation. It does not itself create tangent/scientific authority.