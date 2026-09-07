# Exp073GT — C2 IDE dry-run record-envelope assembly audit v0.1

Status: PROSPECTIVELY FROZEN after independently raw-validated Exp073GS support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Exp073GT freezes only the deterministic byte-layout envelope that would receive future validated recorder outputs. It must not create or serialize cosmological field values. The gate binds the 28 Exp073GS requests to 28 fixed 64-byte recorder slots while keeping every slot explicitly unfilled.

## Frozen upstream identities

- GR canonical contract SHA256: `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`;
- GS provenance-manifest SHA256: `1448d6d6ac3ef2a018af3df9b732a91d4006263bc2fb8b7d232e1eded87316b0`;
- solver lineage metadata only: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- recorder blob: `c6144598b9f75908ee27a517d31eda509f7947f6`;
- record ABI width: exactly 64 bytes, 8 binary64 fields;
- request count: exactly 28, exact z-major/k-minor order and ordinals `0..27` from Exp073GS.

## Frozen envelope semantics

For request ordinal `i` in `0..27`, the envelope descriptor must contain exactly:

- `ordinal=i`;
- literal request `z`;
- literal request `k_Mpc^-1`;
- `record_offset_bytes = 64*i`;
- `record_length_bytes = 64`;
- `record_status = UNFILLED_DRY_RUN_ONLY`.

The 28 descriptors therefore cover a future raw-record address space of exactly `28*64 = 1792` bytes with no gaps and no overlap. No 64-byte record payload may be created by this gate. No `delta_m`, `theta_m`, `rho_idm_iv`, `rho_iv`, `tau`, `a`, or `H` value may be synthesized or serialized.

The envelope must carry the exact GR contract fingerprint, GS manifest fingerprint, recorder blob identity, source-head metadata, request ordering and `prediction_ready=false`.

## Hosted audit

The hosted-only audit must:

1. assemble 28 unfilled descriptors from the exact GS request emitter;
2. verify exact ordinals, z/k values, offsets and lengths;
3. verify intervals are contiguous, non-overlapping and total exactly 1792 bytes;
4. verify every `record_status` is `UNFILLED_DRY_RUN_ONLY`;
5. verify no binary record/payload file is emitted;
6. static-scan the envelope fixture to ensure none of the seven non-coordinate recorder physics fields is synthesized or assigned;
7. verify no CLASS build/run invocation exists;
8. emit exact token `PASS_EXP073GT_C2_IDE_DRYRUN_RECORD_ENVELOPE_ASSEMBLY_AUDIT_V0_1`.

## Classification

PASS is only `SUPPORT_PLUS_0_PLUS_0`; `cosmological_run_started=false`, `self_hosted_science_started=false`, `record_payload_created=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any layout/identity/static mismatch is implementation/infrastructure `+0/+0`, never a scientific model FAIL. PASS may authorize a separately frozen hosted provenance-envelope serialization audit, but not real C2 extraction.
