# DSIR immutable recovery V41 — Exp073HU admitted / Exp073HV decode front

Date: 2026-09-08. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved scientific authority

All earlier scientific authority remains unchanged, including Wm_S1 Track-A exact PASS, admitted Wm_S2/Wm_S3 and scientifically admitted `WW_S3_S3`. No C2 scientific/model authority is created here.

## Newly closed provenance authority — Exp073HU

Exp073HU run `34242025242`, job `102114346415`, head `e2e6a2c1633b48553b99aac34df0801283ddd0b5` is terminal `SUCCESS`. Raw job log was inspected. All frozen admission checks completed successfully and the log contains exact token:

`PASS_EXP073HU_C2_RAW_RECORD_SET_PROVENANCE_ADMISSION_V0_1`

and exact boundary:

- `classification=RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0`
- `raw_record_set_admitted=true`
- `decoded=false`
- `mapped=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

The gate independently reverified upstream HT artifact metadata/digest, downloaded ZIP hash, complete producer receipt, 28 request identities/order, exactly 28 opaque 64-byte packets, byte-exact reassembly to the admitted 1792-byte aggregate, aggregate SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`, 28 endpoint evidence files and embedded HN/HQ/HS/HT binding byte equality against producer head `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`.

HU therefore creates **raw-record-set provenance admission authority only**. It does not decode or map packet values and is `+0/+0` scientifically.

Durable authority file: `docs/dsir4/authority/EXP073HU_C2_RAW_RECORD_SET_ADMISSION_AUTHORITY_V0_1.txt`, creation commit `ac86946104ffe223d1be6573801a41e70a46e22e`, blob `dbcc251cb6534112929c937deb9da6323d3be4f7`.

## Next prospectively frozen gate — Exp073HV ABI decode v0.1

The next allowed gate was designed from the pre-existing producer-side recorder/serializer ABI, not from result-dependent payload inspection.

- prereg `docs/dsir4/prereg/EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1.md`;
- prereg creation commit `5ba5a4a2ca8d6ffa620efb9ead7fbee904202555`;
- prereg blob `8da26d9a051d3de2e8b957123b7019036fdfa3e9`;
- frozen recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`;
- frozen serializer blob `40f361d06fc2732f5c0ad384ed729e5d483810f5`;
- workflow `.github/workflows/exp073hv-c2-raw-record-abi-decode-v0-1.yml`;
- workflow implementation commit `792625ee7fdc20b934f1df9152d41ddbb72a5282`;
- workflow blob `67ee3ff170ba3314958befc915be79222fc844da`;
- binding/launch commit `0687ca5ac973dc50340090213ceaaff70ecc6e04`;
- run `34242333899`;
- job `102115404956`;
- branch/head `main / 0687ca5ac973dc50340090213ceaaff70ecc6e04`;
- runner ownership GitHub-hosted `ubuntu-24.04`; home/self-hosted heavy owner none;
- state at note creation: `QUEUED`.

HV is limited to exact deterministic ABI decoding of the already-admitted packets as eight little-endian IEEE-754 binary64 values in the frozen order `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`, exact bitwise comparison against producer endpoint hexadecimal evidence, and canonical exact-hex JSONL emission. It may create only `decoded=true`; `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE` must remain.

Expected token: `PASS_EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1`.

## Exact next transition

On HV terminal state, inspect raw log and decoded artifact. Workflow success alone is insufficient. On PASS, verify decoded artifact digest/receipt and exact upstream bindings before recording decode authority. Only then may a separate prospectively frozen semantic/domain mapping gate be considered.

Global frozen DSIR scientific boundaries remain unchanged.