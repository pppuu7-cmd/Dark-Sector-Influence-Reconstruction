# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority
All prior DSIR authority remains preserved. Scientifically admitted `WW_S3_S3` remains `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. C2 has no complete model authority/overall PASS.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_IF_IG_PASS_IH_DOMAIN_GATE_FRONT_V49.md`, creation commit `47ee3a9f79cf2a819d16c17fe8f28edb13a3b336`.

## Newly closed C2 processes
- IE `34250165394 / 102142253548`: six-component pinned-source audit raw PASS, support-only.
- IF `34250714613 / 102144147469`: mapping artifact admission raw PASS; `mapping_ready=true`, mapping blob `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`, mapping SHA256 `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`.
- IG `34251593341 / 102147045097`: local tangent prediction artifact admission raw PASS; 28-record payload SHA256 `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`; `prediction_ready=true`, scientific authority still false.

## Current process — Exp073IH C2 G_DOMAIN_MAPPING Scientific Gate v0.1
- prereg: `docs/dsir4/prereg/EXP073IH_C2_G_DOMAIN_MAPPING_SCIENTIFIC_GATE_V0_1.md`;
- prereg creation commit: `03208ce2b4cffba352dc927471594ea65873cb14`;
- prereg blob: `63ea9e9c11b1f77353af613eb8236b5c5961b1fd`;
- workflow: `.github/workflows/exp073ih-c2-g-domain-mapping-scientific-gate-v0-1.yml`;
- workflow/head commit: `08a3750cbbd59ad41102c59896231769b65eff93`;
- workflow/run ID: `34251721583`;
- job ID: `102147505217`;
- branch/head: `main / 08a3750cbbd59ad41102c59896231769b65eff93`;
- checkpoint namespace: N/A; GitHub-hosted structural/domain gate;
- start time: `2026-09-08T16:32:54Z`;
- expected gate/token: `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home owner **none**;
- state at ledger update: QUEUED;
- last durable scientific payload: admitted C2 tangent response ID h=`1e-4`; last durable mapping/prediction payloads are IF mapping artifact and IG 28-record local tangent basis.

### Exact next action on SUCCESS
Consume raw IH log. Require exact frozen gate token and verify it was derived from raw IF/IG authorities, six-component mapping, full certified DSIR mapping envelope and immutable prediction identity. On PASS record `G_DOMAIN_MAPPING=PASS` only. Preserve `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE`, all later mandatory gates `NOT_YET_TESTABLE`, `overall_status=NOT_YET_TESTABLE`, and `scientific_model_authority_created=false`. Then audit the exact required angular observational authority set before defining the next gate.

### Exact next action on FAIL
If execution/provenance defect: diagnose first causal defect and repair only that without changing the frozen scientific decision rule. If genuine frozen-hypothesis domain/mapping failure: record exactly `FAIL` or `OUTSIDE_DOMAIN`/`NUMERICALLY_UNRESOLVED` per preregistration and proceed scientifically; do not rescue by extrapolation or tolerance.

### Exact next action on BLOCKED
Preserve IF/IG admitted support authority and ID tangent authority; do not infer model acceptance/rejection.

Global frozen DSIR boundaries remain unchanged.
