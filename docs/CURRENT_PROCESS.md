# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

All prior scientific authority remains unchanged, including scientifically admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HV_DECODE_PASS_HW_REFERENCE_BRIDGE_FRONT_V42.md`, creation commit `65f4ddf0701ece5fb60d656519c117da23581cfd`.

## Closed C2 front

- HT `34235038323 / 102090438079`: `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`, artifact `10061693504`, aggregate SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`.
- HU `34242025242 / 102114346415`: `RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0`, authority blob `dbcc251cb6534112929c937deb9da6323d3be4f7`.
- HV `34242333899 / 102115404956`: `DECODED_RECORD_SET_PLUS_0_PLUS_0`, artifact `10062495891`, digest `sha256:8ea9cf3baca04f181b97f58f19f04c798bfb14b02af271580c83e82f2900c49e`, exact-hex JSONL SHA256 `95c5b71d5bbbe3492f5bddccaea572644ff84823b244c3c3bc46fd18b389d552`, authority blob `36df02975587d7c1b456cee982b01210185dbda2`.

Current C2 boundary: `raw_record_set_admitted=true`, `decoded=true`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Current process — Exp073HW reference Delta_m bridge v0.1

- prereg `docs/dsir4/prereg/EXP073HW_C2_REFERENCE_DELTAM_BRIDGE_V0_1.md`;
- prereg commit `70bd7fb5dbe43fffa10394f245ea38ca4864ee15`;
- prereg blob `017ecaa735398e8e1515003c1a8092d61f5e284a`;
- workflow `.github/workflows/exp073hw-c2-reference-deltam-bridge-v0-1.yml`;
- workflow implementation commit `ab4f764418566a39c03a002eee9e2703b76aadf5`;
- workflow blob `19ef77c74162462843c66c7350c59d354a5727d9`;
- binding/head commit `0cc263daa9dafe22fecb29aa640a034caee1db3e`;
- run `34242852819`;
- job `102117188431`;
- branch/head `main / 0cc263daa9dafe22fecb29aa640a034caee1db3e`;
- checkpoint namespace `N/A` — GitHub-hosted bounded reference bridge;
- start time `2026-09-08T15:08:43Z`;
- runner ownership GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: `IN_PROGRESS`;
- last durable completed stages: frozen HW binding/HV authority verification SUCCESS; frozen bridge-contract verification SUCCESS;
- expected token `PASS_EXP073HW_C2_REFERENCE_DELTAM_BRIDGE_V0_1`;
- classification ceiling `REFERENCE_DELTAM_BRIDGE_PLUS_0_PLUS_0`.

Frozen arithmetic is `hconf=a*H`, `velocity_term=((3.0*hconf)*theta_m)/(k*k)`, `Delta_m=delta_m+velocity_term` on the decoded native k, with no tolerance/rounding/reassociation rescue. HW remains reference-only and cannot create tangent response/prediction/scientific authority.

### Exact next actions

On HW terminal SUCCESS: inspect raw log and artifact, verify GitHub artifact digest, bridge receipt, exact 28-row canonical JSONL SHA and all provenance/arithmetic boundaries. Only then record reference-bridge authority. Next permitted gate must generate/admit the missing nonzero alpha/beta tangent records and matched-reference response under the already frozen C2 contract.

On HW FAIL/BLOCKED: diagnose the first causal provenance/arithmetic/canonicalization defect; do not alter the bridge, source identity, grid, model, tolerances or science.

Global frozen DSIR boundaries remain unchanged.
