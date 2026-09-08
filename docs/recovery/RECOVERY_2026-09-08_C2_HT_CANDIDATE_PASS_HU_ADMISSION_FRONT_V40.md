# DSIR immutable recovery V40 — Exp073HT candidate PASS / Exp073HU admission front

Date: 2026-09-08. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved scientific authority

All earlier DSIR scientific authority remains unchanged, including Wm_S1 Track-A exact PASS, admitted Wm_S2/Wm_S3, and scientifically admitted `WW_S3_S3` from run `34218457380 / job 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

No C2 scientific/model authority has been created. Until Exp073HU itself passes raw-log verification, C2 remains `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Newly consumed result — Exp073HT v0.3

Exp073HT run `34235038323`, job `102090438079`, head `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`, completed `SUCCESS`. Workflow success was not treated as scientific PASS by itself. The raw job log and uploaded artifact were consumed independently.

Raw log contains exact token `PASS_EXP073HT_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_3` and boundary `classification=RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`.

Artifact identity:

- artifact ID `10061693504`;
- artifact name `exp073ht-c2-reference-raw-runtime-v0-3`;
- GitHub digest `sha256:9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`;
- independently downloaded ZIP SHA256 exactly `9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`.

Independent artifact verification established:

- exactly 28 request records in `plan.jsonl` and `requests.tsv`;
- 28 distinct request IDs and 28 distinct `(z_literal,k_mpc_literal)` pairs;
- request order preserved z-major/k-minor;
- exactly 28 packet files and every packet exactly 64 bytes;
- canonical packet concatenation in frozen request order is byte-for-byte identical to `dsir_c2_reference_raw_v0_3.bin`;
- aggregate size exactly `1792` bytes;
- aggregate SHA256 exactly `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`, matching `aggregate.sha256` and raw log;
- exactly 28 endpoint evidence files;
- receipt binds producer run `34235038323`, job `102090438079`, head `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`, solver commit `ac627d54e9ce196a08878d1ba33999819925d19c`, post-HS source SHA256s, baseline/precision SHA256s, packet count/bytes/order, aggregate bytes/SHA;
- HT receipt itself correctly preserves `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`.

Therefore HT is classified exactly as **`RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`**. It is not a raw-record admission and creates no decode/mapping/scientific authority.

## Prospectively frozen next gate — Exp073HU v0.1

A separate hosted-only provenance/opaque-byte admission gate was prospectively frozen after HT candidate consumption:

- prereg `docs/dsir4/prereg/EXP073HU_C2_RAW_RECORD_SET_PROVENANCE_ADMISSION_V0_1.md`;
- prereg creation commit `96d3499aaeaae65296b57691a28994f059434503`;
- prereg blob `88ee0157c501f7bb14a5688e37289709b9ccaf82`;
- workflow `.github/workflows/exp073hu-c2-raw-record-set-provenance-admission-v0-1.yml`;
- workflow implementation commit `bec2d02bc18d715f576cce5cefb8bb2015bfdd4a`;
- workflow blob `c722f4f31c89e88b83045078c039f6c839b5da52`;
- binding/launch commit `e2e6a2c1633b48553b99aac34df0801283ddd0b5`;
- run `34242025242`;
- job `102114346415`;
- branch/head `main / e2e6a2c1633b48553b99aac34df0801283ddd0b5`;
- runner owner GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner none;
- state at note creation: `QUEUED`.

HU may verify only artifact metadata/digest, receipt/provenance, request/order metadata, opaque 64-byte packet identities, byte-exact reassembly, aggregate digest, endpoint file/request binding, and frozen embedded binding equality. HU is explicitly forbidden to deserialize the packet payload into physical/numerical values or perform decoding, mapping, prediction, likelihood or scientific interpretation.

HU maximum PASS boundary is `classification=RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0`, `raw_record_set_admitted=true`, while `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE` remain exact.

Expected token: `PASS_EXP073HU_C2_RAW_RECORD_SET_PROVENANCE_ADMISSION_V0_1`.

## Exact next transition

On HU terminal state, inspect raw job log and exact failing/success step. Only raw-log confirmation of all frozen checks and exact PASS token may create raw-record-set admission authority. Workflow SUCCESS alone remains insufficient.

On HU PASS, design only a later separately prospectively frozen decode/semantic-structure gate; do not map or interpret in HU. On HU failure, classify as implementation/provenance `+0/+0`, diagnose the first causal defect, and repair prospectively without weakening any digest/provenance/order/byte-identity requirement.

Global frozen DSIR scientific boundaries remain unchanged.