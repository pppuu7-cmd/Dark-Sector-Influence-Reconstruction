# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority
All prior scientific authority is unchanged, including admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. No C2 scientific/model authority exists.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HZ_IA_PASS_IBV02_MAP_PASS_IC_RESPONSE_FRONT_V46.md`, creation commit `f352ccb2ad11652a2b512c275bb6244a276332b7`.

## Newly closed C2 processes
- HZ `34248477503 / 102136488451`: tangent raw-set provenance admission PASS; `tangent_raw_set_admitted=true`.
- IA `34248722000 / 102137324616`: exact ABI decode PASS; artifact `10065081303`, ZIP SHA256 `6bf115c76d538f0691c1fcfa9d9a26721b9b593f26aceb2a7a59bdb7cc9aa0ce`.
- IB v0.1 `34248841106 / 102137736842`: historical `IMPLEMENTATION_PROVENANCE_FAIL_PLUS_0_PLUS_0` because implementation did not explicitly preserve the authoritative HW operation-order lineage; 0/252 realized binary64 outputs differed, so this is not scientific FAIL.
- IB v0.2 `34249229753 / 102139059309`: exact repaired mapping PASS; artifact `10065286473`, ZIP SHA256 `965e921224f516e76e9cf2d2ac84ed51a5027b97d79c73c87620d55a83011201`; exact HW operation order and 252/252 regression equality; `mapped_tangent_coordinate=true`, `tangent_response_ready=false`.

## Current process — Exp073IC tangent finite-difference response candidate v0.1
- prereg: `docs/dsir4/prereg/EXP073IC_C2_TANGENT_FINITE_DIFFERENCE_RESPONSE_CANDIDATE_V0_1.md`;
- prereg creation commit: `7d94f9f9bfaa3b320250c7b046d2a6c7a37309b5`;
- prereg blob: `9e1235a48a4288bb2083d69084f1cae7d79847bb`;
- workflow: `.github/workflows/exp073ic-c2-tangent-finite-difference-response-candidate-v0-1.yml`;
- workflow/head commit: `f3475f5d409a50c31fb1eda3870837542797e091`;
- workflow/run ID: `34249380208`;
- job ID: `102139612475`;
- branch/head: `main / f3475f5d409a50c31fb1eda3870837542797e091`;
- checkpoint namespace: N/A; GitHub-hosted deterministic transformation of immutable HW/IB v0.2 artifacts;
- start time: `2026-09-08T16:10:03Z`;
- expected gate/token: `PASS_EXP073IC_C2_TANGENT_FINITE_DIFFERENCE_RESPONSE_CANDIDATE_V0_1`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home owner **none**;
- state at ledger update: QUEUED;
- last durable payload: authoritative HW reference map and IB v0.2 9×28 tangent maps.

### Exact next action on SUCCESS
Consume IC raw log and artifact, verify source authority bindings, exact 28-row order, exact output SHA and finite binary64 response fields. Classify only `TANGENT_RESPONSE_CANDIDATE_PLUS_0_PLUS_0`; keep `tangent_response_ready=false`. Before inspecting scale relations for scientific acceptance, prospectively freeze a separate stability/admission rule. Never choose a favorable scale or threshold post hoc.

### Exact next action on FAIL
Diagnose the first causal infrastructure/provenance defect. Preserve HW, IA and IB v0.2 authorities and all frozen point definitions. Do not alter finite-difference definitions or scales to rescue the result.

### Exact next action on BLOCKED
Preserve the mapped coordinate sets and keep tangent-response authority/prediction forbidden.

Global frozen DSIR boundaries remain unchanged.
