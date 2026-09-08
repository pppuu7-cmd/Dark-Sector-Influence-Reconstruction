# DSIR immutable recovery V44 — Exp073HX plan PASS / Exp073HY tangent runtime front

Date: 2026-09-08. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved authority

All earlier DSIR scientific authority remains unchanged. C2 still creates no scientific/model authority. The validated C2 reference chain remains HT raw candidate -> HU raw-set admission -> HV exact ABI decode -> HW reference `Delta_m` bridge.

## Newly closed support gate — Exp073HX

Exp073HX run `34243153985`, job `102118219475`, head `dd25da6aa9363c3a279e894595106b472b2375ad` is terminal `SUCCESS`; raw log was inspected and contains exact token `PASS_EXP073HX_C2_TANGENT_RUNTIME_PLAN_STATIC_AUDIT_V0_1`.

Exact classification/boundary:
- `classification=SUPPORT_PLUS_0_PLUS_0`
- `model_point_count=9`
- `requests_per_model=28`
- `total_requests=252`
- `reference_recomputed=false`
- `tangent_runtime_started=false`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

The plan exactly preserves the frozen one-sided alpha points `-1e-4,-1e-3,-1e-2`, symmetric beta `+/-1e-4,+/-1e-3,+/-1e-2`, 7 z × 4 admitted k per point, model-major then z-major/k-minor. The excluded `0.067 Mpc^-1` node remains absent.

## Current process — Exp073HY tangent raw runtime producer v0.1

After HX raw-log PASS, a separately prospectively frozen runtime producer was created. Solver input names were independently verified against the frozen baseline as `alpha_idm_iv` and `beta_idm_iv`; only these two lines may differ by frozen model point.

- prereg `docs/dsir4/prereg/EXP073HY_C2_TANGENT_RAW_RUNTIME_PRODUCER_V0_1.md`;
- prereg creation commit `7ab623edfaa1fc27c62d020fc93d0679844286e6`;
- prereg blob `5b7f9d3ce989f524e1d9555a219b692e44793821`;
- workflow `.github/workflows/exp073hy-c2-tangent-raw-runtime-producer-v0-1.yml`;
- workflow implementation commit `4a50791ce0493ee69084224a834ac2902f0580f5`;
- workflow blob `93d476850f8c388d3e91f9f41283e7b436b99268`;
- binding/head commit `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`;
- run `34243515299`;
- GitHub-hosted matrix; self-hosted/home heavy owner none;
- state at note creation: one model job `tangent-alpha_m1e3 / 102119471057` IN_PROGRESS; the other eight tangent model jobs queued; final manifest verifier waits on all model jobs.

HY reuses exactly the validated HT post-HS solver/endpoint/serializer lineage. Each matrix job is a complete durable model unit: 28 exact endpoint records, exactly 64 bytes each, 1792-byte aggregate, SHA256 and model-specific provenance receipt, then its own artifact. Matrix uses `fail-fast: false`, so successful complete units survive another model's failure. Reference `(0,0)` is not recomputed.

HY scientific ceiling remains `TANGENT_RAW_RUNTIME_CANDIDATES_PLUS_0_PLUS_0`; raw tangent set is not admitted and no decoding, Delta_m mapping, tangent derivative, response, prediction or science is permitted in HY.

Expected terminal token after all nine complete artifacts and manifest verification: `PASS_EXP073HY_C2_TANGENT_RAW_RUNTIME_CANDIDATES_V0_1`.

## Exact next transition

On HY terminal state, inspect every matrix job and the manifest-verifier raw log. Preserve all complete successful model artifacts. On PASS, independently verify all nine GitHub artifact digests, run/job/head receipts, 28×64-byte contents and per-model aggregate hashes before a separate tangent raw-set provenance admission/decode/mapping gate. On any matrix failure, diagnose the first causal defect for that model without invalidating completed model units and without changing frozen model points, grid, source patches, precision, ABI or endpoint criteria.

Global frozen DSIR boundaries remain unchanged.