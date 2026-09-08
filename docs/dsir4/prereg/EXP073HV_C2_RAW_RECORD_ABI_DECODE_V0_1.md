# Exp073HV — C2 raw-record ABI decode v0.1

Status: **prospectively frozen before execution**. Scope: DSIR only.

## Purpose

Exp073HU admitted the opaque 28×64-byte C2 raw record set by provenance and exact byte identity. Exp073HV is the first permitted decode gate. It is restricted to deterministic ABI decoding exactly as defined by the pre-existing HN recorder/serializer implementation. It MUST NOT perform physical-domain mapping, prediction, likelihood evaluation, fitting, smoothing, averaging, rounding, threshold rescue, or create scientific/model authority.

Maximum PASS classification:

`DECODED_RECORD_SET_PLUS_0_PLUS_0`

with exact boundary:

- `raw_record_set_admitted=true`;
- `decoded=true`;
- `mapped=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Frozen upstream admission authority

The gate MUST bind exactly to repository authority file:

`docs/dsir4/authority/EXP073HU_C2_RAW_RECORD_SET_ADMISSION_AUTHORITY_V0_1.txt`

with blob SHA `dbcc251cb6534112929c937deb9da6323d3be4f7` and upstream identities:

- HU run `34242025242`, job `102114346415`, head `e2e6a2c1633b48553b99aac34df0801283ddd0b5`;
- HT artifact ID `10061693504`;
- HT artifact ZIP digest `sha256:9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`;
- admitted aggregate SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`.

## Frozen ABI definition

The decode layout is not inferred from payload values. It is frozen from the pre-existing producer-side code at HT producer head `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`:

- `scripts/dsir4/fixtures/dsir_c2_recorder_v0_1.h`, blob `c6144598b9f75908ee27a517d31eda509f7947f6`;
- `scripts/dsir4/exp073hn_c2_endpoint_serializer_v0_1.c`, blob `40f361d06fc2732f5c0ad384ed729e5d483810f5`.

The recorder writes exactly eight C `double` values in this fixed order:

1. `tau`
2. `k`
3. `a`
4. `H`
5. `delta_m`
6. `theta_m`
7. `rho_idm_iv`
8. `rho_iv`

The HT runtime executed on GitHub-hosted Ubuntu 24.04 x86-64. HV MUST fail closed unless the verifier runtime establishes 8-byte IEEE-754 binary64 `double`, little-endian byte order, and the expected canonical binary64 behavior. No alternate endian or size reinterpretation is allowed in v0.1.

## Frozen decoding and exact-consistency checks

HV MUST:

1. verify the exact HU authority blob and fields above;
2. verify HT artifact metadata, GitHub digest and downloaded ZIP SHA exactly as admitted;
3. verify aggregate/packet identities exactly as in HU before decoding;
4. verify the frozen recorder and serializer blobs from HT producer head;
5. decode every 64-byte packet as exactly eight little-endian IEEE-754 binary64 values in the frozen field order;
6. require all 8×28 decoded values to be finite; non-finite is a decode/record FAIL `+0/+0`, not a scientific result;
7. independently parse each producer `.endpoint` evidence line using a C `strtod`/binary64-compatible path or an exact hexadecimal-float parser and require bitwise equality field-by-field between the eight parsed endpoint values and the eight decoded binary packet values;
8. bind each decoded row to the corresponding request ID from `requests.tsv`, preserving exact frozen z-major/k-minor order;
9. emit a canonical decoded artifact with one JSON object per row containing only request metadata plus exact `float.hex`/C99-hex representations of the eight binary64 values, never rounded decimal values;
10. hash that canonical decoded artifact and record its SHA256 in a receipt along with the upstream HU/HT identities and ABI blobs.

The canonical JSONL field order is frozen as:

`request_id,z_literal,k_literal,tau_hex,k_hex,a_hex,H_hex,delta_m_hex,theta_m_hex,rho_idm_iv_hex,rho_iv_hex`

JSON serialization MUST use compact separators, ASCII keys/values, one record per line, newline terminated, and preserve the 28-row request order. Hex values MUST be Python/C99-equivalent exact binary64 hex strings with no decimal rounding.

## Prohibitions

HV MUST NOT:

- alter/regenerate the raw HT artifact;
- run CLASS or cosmological calculations;
- use decoded numerical values to change any gate, threshold, model, grid or acceptance rule;
- convert values to approximate decimal for acceptance;
- map any decoded field into a downstream observable/domain decision;
- compute ratios, derivatives, fits, residuals, likelihoods, ranks or predictions;
- claim scientific/model authority.

## PASS token

Exact token:

`PASS_EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1`

with exact boundary lines:

- `classification=DECODED_RECORD_SET_PLUS_0_PLUS_0`
- `raw_record_set_admitted=true`
- `decoded=true`
- `mapped=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any ABI mismatch, non-finite decoded value, endpoint-vs-packet bit mismatch, provenance mismatch, ordering mismatch or canonicalization mismatch is `+0/+0` and must not be repaired by tolerance or rounding.

## Exact next transition

Only after HV raw-log and decoded-artifact verification may a separately prospectively frozen semantic/domain mapping gate be considered.