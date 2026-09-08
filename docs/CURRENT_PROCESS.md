# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority
All prior scientific authority is unchanged, including admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. No C2 scientific/model authority exists.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HY_RAW_CANDIDATE_HZ_ADMISSION_FRONT_V45.md`, creation commit `c3d7e3d2b8852eef035ae9094f465cc7d83940ff`.

## Newly closed process — Exp073HY
HY run `34243515299`, head `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`, all nine complete tangent model units plus manifest verifier terminal SUCCESS. Raw logs and all nine independently downloaded artifacts verify exact 28×64-byte packet sets, exact z-major/k-minor 1792-byte aggregate reassembly, receipts, source fingerprints, GitHub ZIP SHA256 and aggregate SHA256. Classification `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`; `tangent_raw_set_admitted=false`, `decoded=false`, `mapped=false`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`.

## Current process — Exp073HZ tangent raw-set provenance admission v0.1
- prereg: `docs/dsir4/prereg/EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1.md`;
- prereg creation commit: `308a4acd0a4cc5dcc16175235dc2659a8c59cc37`;
- prereg blob: `a4be5047b2968e8b9bc844a3d2bdbd2bc3e6e966`;
- workflow: `.github/workflows/exp073hz-c2-tangent-raw-set-provenance-admission-v0-1.yml`;
- workflow/head commit: `edaa94d42b18f45a6e0659dc23399793e0228830`;
- workflow/run ID: `34248477503`;
- job ID: `102136488451`;
- branch/head: `main / edaa94d42b18f45a6e0659dc23399793e0228830`;
- checkpoint namespace: N/A; hosted provenance-only admission over immutable HY artifacts;
- start time: `2026-09-08T16:01:21Z`;
- expected gate/token: `PASS_EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home owner **none**;
- state at ledger update: IN_PROGRESS;
- last durable payload: nine independently validated HY complete model-point artifacts; exact IDs/digests/job IDs/aggregate SHA256 frozen in the HZ prereg and V45 note.

### Exact next action on SUCCESS
Consume HZ raw log and require the exact PASS token plus `classification=TANGENT_RAW_SET_ADMITTED_PLUS_0_PLUS_0`, `tangent_raw_set_admitted=true`, `decoded=false`, `mapped=false`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. Only then prospectively freeze a **separate deterministic tangent ABI decode gate**. Do not calculate tangent derivatives yet.

### Exact next action on FAIL
Diagnose the first causal infrastructure/provenance mismatch. Preserve the validated HY artifacts. Do not alter model points, coordinate grid, solver/source fingerprints, packet ABI, aggregate ordering, or acceptance criteria.

### Exact next action on BLOCKED
Preserve HY raw candidate and keep tangent derivatives/prediction forbidden.

Global frozen DSIR boundaries remain unchanged.
