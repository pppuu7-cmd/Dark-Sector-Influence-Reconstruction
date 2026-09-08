# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

All prior scientific authority remains unchanged, including scientifically admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HX_PLAN_PASS_HY_TANGENT_RUNTIME_FRONT_V44.md`, creation commit `df69e399d812a1da9f72349215318308e7ad59cc`.

## Closed C2 front

HT/HU/HV/HW are validated through reference common-coordinate authority. HX `34243153985 / 102118219475` is raw-log validated `SUPPORT_PLUS_0_PLUS_0` with exact 9×28=252 tangent runtime plan and no reference recomputation.

Current C2 boundary: `raw_record_set_admitted=true`, `decoded=true`, `mapped_reference_coordinate=true`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Current process — Exp073HY tangent raw runtime producer v0.1

- prereg `docs/dsir4/prereg/EXP073HY_C2_TANGENT_RAW_RUNTIME_PRODUCER_V0_1.md`;
- prereg commit `7ab623edfaa1fc27c62d020fc93d0679844286e6`;
- prereg blob `5b7f9d3ce989f524e1d9555a219b692e44793821`;
- workflow `.github/workflows/exp073hy-c2-tangent-raw-runtime-producer-v0-1.yml`;
- workflow implementation commit `4a50791ce0493ee69084224a834ac2902f0580f5`;
- workflow blob `93d476850f8c388d3e91f9f41283e7b436b99268`;
- binding/head commit `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`;
- workflow/run ID `34243515299`;
- branch/head `main / ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`;
- checkpoint namespace: GitHub-hosted complete model-point artifacts, one namespace/artifact per frozen model point; no home checkpoint owner;
- start time `2026-09-08T15:14:55Z`;
- runner ownership GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: matrix queued/in_progress;
- known job IDs at first live reconciliation: `tangent-alpha_m1e3=102119471057` IN_PROGRESS; `beta_m1e2=102119471334`, `beta_p1e3=102119471369`, `beta_m1e3=102119471373`, `beta_m1e4=102119471483`, `beta_p1e4=102119471486`, `beta_p1e2=102119471600`, `alpha_m1e2=102119471655`, `alpha_m1e4=102119471802` queued;
- final manifest-verifier job ID not yet allocated at this ledger snapshot;
- expected terminal token `PASS_EXP073HY_C2_TANGENT_RAW_RUNTIME_CANDIDATES_V0_1`;
- classification ceiling `TANGENT_RAW_RUNTIME_CANDIDATES_PLUS_0_PLUS_0`.

Each model job is a complete durable unit: exactly 28 endpoint records ×64 bytes, 1792-byte aggregate, digest and run/job/head/model receipt. `fail-fast:false` preserves successful model artifacts if another model fails. No reference recomputation, decoding, Delta_m mapping, derivative, response, prediction or science is allowed in HY.

### Exact next actions

If HY is terminal, consume every matrix job plus manifest raw log immediately. On complete PASS, independently verify all nine GitHub artifact digests and receipts and only then preregister tangent raw-set provenance admission/decode/mapping. On a model FAIL, preserve all successful complete model artifacts, diagnose that model's first causal defect and repair prospectively without changing model points/grid/source/precision/ABI/endpoint criteria. If HY remains running, do not duplicate it.

Global frozen DSIR boundaries remain unchanged.
