# Exp073HW — C2 reference common-Delta_m bridge v0.1

Status: **prospectively frozen before execution**. Scope: DSIR only, `C2_IDE_LOCAL_TANGENT_CONE` reference point `(alpha,beta)=(0,0)` only.

## Purpose and ceiling

Consume only the admitted+decoded Exp073HV reference records and apply the already-frozen C2 common-coordinate bridge from `C2_IDE_DELTAM_EXTRACTION_CONTRACT_V0_1.md` and `C2_IDE_NATIVE_SOURCE_BINDING_AUDIT_V0_1.md`:

`Delta_m = delta_m + 3*a*H*theta_m/k^2`

because the frozen matter partition is pressureless (`w_m=0`) and `Hconf=aH`.

This gate is a deterministic reference-coordinate semantic bridge only. It MUST NOT form alpha/beta tangent derivatives, same-solver model/reference responses, likelihoods, ranks, predictions, or scientific/model authority. It cannot set `prediction_ready=true` and cannot decide `G_DOMAIN_MAPPING`.

Maximum PASS classification: `REFERENCE_DELTAM_BRIDGE_PLUS_0_PLUS_0` with `raw_record_set_admitted=true`, `decoded=true`, `mapped_reference_coordinate=true`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Frozen upstream identity

- HV authority file `docs/dsir4/authority/EXP073HV_C2_RAW_RECORD_ABI_DECODE_AUTHORITY_V0_1.txt`, blob `36df02975587d7c1b456cee982b01210185dbda2`;
- HV run/job/head `34242333899 / 102115404956 / 0687ca5ac973dc50340090213ceaaff70ecc6e04`;
- HV artifact `10062495891`, digest `sha256:8ea9cf3baca04f181b97f58f19f04c798bfb14b02af271580c83e82f2900c49e`;
- decoded JSONL SHA256 `95c5b71d5bbbe3492f5bddccaea572644ff84823b244c3c3bc46fd18b389d552`;
- HT raw aggregate SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`.

## Frozen arithmetic

For every one of the 28 rows, parse only exact binary64 hex fields from HV. Require finite `k,a,H,delta_m,theta_m` and exact `k>0`. Compute once, in IEEE-754 binary64 evaluation with explicitly frozen operation order:

1. `hconf = a * H`
2. `velocity_term = ((3.0 * hconf) * theta_m) / (k * k)`
3. `Delta_m = delta_m + velocity_term`

No fused/reassociated alternate expression is admitted. No tolerance, decimal rounding, smoothing or averaging is permitted. Emit exact `float.hex` strings for `hconf`, `velocity_term`, and `Delta_m` in the original 28-row order.

The `k` used in the bridge MUST be the decoded native packet `k` field; `k_literal` remains provenance metadata and MUST NOT silently replace it. The gate may bit-compare decoded `k` against an exact independently parsed literal only as an audit, but any mismatch is fail-closed rather than repaired.

## Physical-branch boundary

The decoded `rho_idm_iv` and `rho_iv` values may be checked at these 28 sampled coordinates only for finite/sign diagnostics (`rho_idm_iv>0`, `rho_iv>=0`). Passing such node checks MUST NOT be promoted to the extraction contract's stronger required-history physical-branch proof.

## Canonical output

Emit 28 newline-terminated compact JSON objects in original order with keys exactly:

`request_id,z_literal,k_literal,k_hex,a_hex,H_hex,delta_m_hex,theta_m_hex,hconf_hex,velocity_term_hex,Delta_m_hex,rho_idm_iv_hex,rho_iv_hex,node_rho_idm_positive,node_rho_iv_nonnegative`

and SHA256 of the canonical JSONL. No approximate decimal scientific values are allowed in the artifact.

## PASS token

`PASS_EXP073HW_C2_REFERENCE_DELTAM_BRIDGE_V0_1`

PASS boundary must include:

- `classification=REFERENCE_DELTAM_BRIDGE_PLUS_0_PLUS_0`
- `raw_record_set_admitted=true`
- `decoded=true`
- `mapped_reference_coordinate=true`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any provenance, ABI, finiteness, exact-k, arithmetic/canonicalization or sampled-node sign failure is `+0/+0`, not a scientific rejection. No tolerance or altered bridge may rescue it.

## Exact next transition

Only after HW raw-log/artifact PASS may the next gate address the still-missing prospectively frozen nonzero alpha/beta tangent runtime records and matched-reference response construction required by the original C2 extraction contract.