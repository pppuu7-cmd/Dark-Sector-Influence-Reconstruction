# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

All prior scientific authority remains unchanged, including scientifically admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HU_ADMITTED_HV_DECODE_FRONT_V41.md`, creation commit `b24f4cb61c4841adf2a9f08957e27da5350dd855`.

## Closed C2 front

Exp073HT `34235038323 / 102090438079` is validated `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`, artifact `10061693504`, ZIP digest `sha256:9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`, aggregate SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`.

Exp073HU `34242025242 / 102114346415` is raw-log validated `RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0`; durable authority blob `dbcc251cb6534112929c937deb9da6323d3be4f7`. Current C2 boundary is `raw_record_set_admitted=true`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Current process — Exp073HV ABI decode v0.1

- prereg `docs/dsir4/prereg/EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1.md`;
- prereg commit `5ba5a4a2ca8d6ffa620efb9ead7fbee904202555`;
- prereg blob `8da26d9a051d3de2e8b957123b7019036fdfa3e9`;
- workflow `.github/workflows/exp073hv-c2-raw-record-abi-decode-v0-1.yml`;
- workflow implementation commit `792625ee7fdc20b934f1df9152d41ddbb72a5282`;
- workflow blob `67ee3ff170ba3314958befc915be79222fc844da`;
- binding/head commit `0687ca5ac973dc50340090213ceaaff70ecc6e04`;
- workflow/run ID `34242333899`;
- job ID `102115404956`;
- branch/head `main / 0687ca5ac973dc50340090213ceaaff70ecc6e04`;
- checkpoint namespace `N/A` — GitHub-hosted bounded decode, no home-heavy compute;
- start time `2026-09-08T15:03:55Z`;
- runner ownership GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: `QUEUED`;
- expected token `PASS_EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1`;
- classification ceiling `DECODED_RECORD_SET_PLUS_0_PLUS_0`.

HV may only prove the frozen 8×binary64 ABI, bitwise packet/endpoint equivalence and canonical exact-hex decoded JSONL. No mapping, prediction or scientific interpretation is allowed.

### Exact next actions

On HV terminal SUCCESS: inspect raw log and artifact, verify GitHub artifact digest, decoded receipt, 28 canonical rows, decoded JSONL SHA256, exact HU/HT/ABI provenance and bitwise proof. Only after all frozen checks record decode authority (`decoded=true`) and prospectively define a separate semantic/domain mapping gate.

On HV FAIL/BLOCKED: diagnose the first causal ABI/provenance/canonicalization defect and repair prospectively without tolerance/rounding or any scientific-boundary change.

Global frozen DSIR boundaries remain unchanged.
