# Exp073HU — C2 raw-record-set provenance admission v0.1

Status: **prospectively frozen before Exp073HU execution**. Scope: DSIR only.

## Purpose and authority ceiling

Exp073HT produced a validated raw-runtime candidate, but HT explicitly left `raw_record_set_admitted=false`. Exp073HU is a separate hosted-only, receipt/provenance/byte-identity admission gate. It may create authority only for the identity and admissibility of the already-produced opaque raw record set. It MUST NOT decode packet payload values, map them to a physical domain, fit/average/smooth/round them, form a prediction, or create scientific/model authority.

On PASS the maximum classification is `RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0` with:

- `raw_record_set_admitted=true`;
- `decoded=false`;
- `mapped=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Frozen upstream candidate identity

The only admissible input is Exp073HT v0.3:

- producer run: `34235038323`;
- producer job: `102090438079`;
- producer head: `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`;
- artifact ID: `10061693504`;
- artifact name: `exp073ht-c2-reference-raw-runtime-v0-3`;
- GitHub artifact ZIP digest: `sha256:9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`;
- aggregate filename: `dsir_c2_reference_raw_v0_3.bin`;
- aggregate bytes: exactly `1792`;
- aggregate SHA256: `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`;
- packet count: exactly `28`;
- packet bytes: exactly `64` each;
- order: frozen z-major/k-minor request order from the HT plan/requests files.

Frozen solver/config provenance expected in the producer receipt:

- solver repo `kaeonikc/class_iv`;
- solver commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- post-HS `perturbations.c` SHA256 `483b481b48e50a6afb396b15b85258ac6c5a7a39b38fb1c6192e7e4a95c139ae`;
- post-HS `evolver_ndf15.c` SHA256 `3f12121ce2de319453e1ff5fadae9391fd96747731c0df3fa05fae1cd2608aa9`;
- baseline config SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`;
- precision config SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`.

## Frozen admission checks

The hosted verifier MUST fail closed unless all checks pass:

1. GitHub metadata for artifact ID `10061693504` binds it to run `34235038323`, head `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`, exact artifact name, and exact GitHub digest above.
2. The downloaded ZIP bytes hash exactly to `9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`.
3. `RECEIPT.txt` contains exactly the frozen producer run/job/head identity, run attempt `1`, solver/config fingerprints, `packet_count=28`, `packet_bytes=64`, `aggregate_bytes=1792`, `coordinate_order=z-major/k-minor`, and aggregate SHA256 above.
4. `RECEIPT.txt` from HT must still state `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`; HU is the gate that may change only the admission flag in its own output.
5. `plan.jsonl` and `requests.tsv` contain exactly 28 distinct request IDs and 28 distinct `(z_literal,k_mpc_literal)` pairs in identical z-major/k-minor order. No request may be missing, duplicated or reordered.
6. Exactly 28 `packets/<request_id>.bin` files exist, each exactly 64 bytes. No numeric interpretation of those 64 bytes is permitted in HU.
7. Concatenating those opaque packet bytes strictly in `requests.tsv` order is byte-for-byte identical to `dsir_c2_reference_raw_v0_3.bin`.
8. The aggregate is exactly 1792 bytes and hashes exactly to `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`; `aggregate.sha256` must contain exactly that hash.
9. Exactly 28 `.endpoint` evidence files exist, one per request ID. HU may verify file identity/presence and literal request binding only; it MUST NOT decode or scientifically interpret endpoint payload values.
10. Frozen HT/HN/HQ/HS binding files embedded in the artifact must be present. Their opaque bytes must match the repository blobs bound by the producer head or fail closed.

## Explicit prohibitions

Exp073HU MUST NOT:

- execute CLASS or any cosmological calculation;
- regenerate any of the 28 packets;
- alter any source/config/grid/model/arithmetic/tolerance/ABI;
- deserialize the 64-byte packet payload into physical/numerical fields;
- inspect payload values for result-dependent gate design;
- perform decoding, mapping, prediction, likelihood, rank or model comparison;
- use tolerance, rounding, smoothing, averaging, nearest-coordinate or effective-coordinate rescue;
- claim scientific/model authority.

## Frozen terminal tokens

PASS requires exact token:

`PASS_EXP073HU_C2_RAW_RECORD_SET_PROVENANCE_ADMISSION_V0_1`

and exact boundary lines:

- `classification=RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0`
- `raw_record_set_admitted=true`
- `decoded=false`
- `mapped=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any provenance, digest, receipt, order, file-count, byte-size, byte-equality or binding mismatch is an implementation/provenance FAIL `+0/+0`, not a scientific arithmetic FAIL. No repair may weaken this contract.

## Exact next transition

Only after raw-log inspection confirms HU PASS may a later, separately prospectively frozen decode/semantic-structure gate be designed. HU itself authorizes no decoding or mapping.