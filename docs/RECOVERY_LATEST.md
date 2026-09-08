# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HU_ADMITTED_HV_DECODE_FRONT_V41.md` (creation commit `b24f4cb61c4841adf2a9f08957e27da5350dd855`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

No C2 scientific/model authority exists.

## Newly validated C2 authorities

Exp073HT run `34235038323 / job 102090438079`, head `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`, is independently consumed as `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`. Artifact `10061693504` has GitHub and independently verified ZIP digest `sha256:9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`. Exactly 28×64-byte packets reassemble byte-for-byte to the 1792-byte aggregate SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4` with exact run/job/head/source/config receipt binding.

Exp073HU run `34242025242 / job 102114346415`, head `e2e6a2c1633b48553b99aac34df0801283ddd0b5`, raw-log PASS token `PASS_EXP073HU_C2_RAW_RECORD_SET_PROVENANCE_ADMISSION_V0_1`, creates provenance-only raw-record admission: `raw_record_set_admitted=true`, while `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. Durable authority file: `docs/dsir4/authority/EXP073HU_C2_RAW_RECORD_SET_ADMISSION_AUTHORITY_V0_1.txt`, blob `dbcc251cb6534112929c937deb9da6323d3be4f7`.

## Current frontier — Exp073HV ABI decode v0.1

Prospectively frozen from the pre-existing producer ABI, not from payload-result tuning:

- prereg `docs/dsir4/prereg/EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1.md`, commit `5ba5a4a2ca8d6ffa620efb9ead7fbee904202555`, blob `8da26d9a051d3de2e8b957123b7019036fdfa3e9`;
- recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`;
- serializer blob `40f361d06fc2732f5c0ad384ed729e5d483810f5`;
- workflow `.github/workflows/exp073hv-c2-raw-record-abi-decode-v0-1.yml`, implementation commit `792625ee7fdc20b934f1df9152d41ddbb72a5282`, blob `67ee3ff170ba3314958befc915be79222fc844da`;
- binding/head commit `0687ca5ac973dc50340090213ceaaff70ecc6e04`;
- run `34242333899`, job `102115404956`;
- GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner none;
- state at pointer update: `QUEUED`.

HV may only decode the already-admitted 64-byte packets as the frozen eight little-endian IEEE-754 binary64 fields, prove exact bit identity against producer hexadecimal endpoint evidence, and emit canonical exact-hex JSONL. PASS ceiling is `DECODED_RECORD_SET_PLUS_0_PLUS_0`: `decoded=true` only; mapping/prediction/scientific authority remain false.

Expected token: `PASS_EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1`.

## Exact next transition

On HV terminal state, inspect raw job log and decoded artifact; workflow success alone is insufficient. Verify artifact digest, decode receipt, 28 rows, canonical JSONL SHA, exact HU/HT/ABI provenance and bitwise endpoint-vs-packet equality. Only then record decode authority and prospectively freeze a separate semantic/domain mapping gate.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
