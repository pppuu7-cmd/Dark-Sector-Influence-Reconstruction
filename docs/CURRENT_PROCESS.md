# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

All prior scientific authority remains unchanged, including scientifically admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HS_PASS_HT_RAW_RUNTIME_FRONT_V39.md`, creation commit `4b6742b7b9d42fa3965c9bff77d58ca64c34a99d`.

## Newly closed C2 support gate

Exp073HS run `34230896860`, job `102076459069`, is terminal `SUCCESS`. Raw job log inspection confirmed exact frozen token `PASS_EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1`; classification is **SUPPORT_PLUS_0_PLUS_0** only. HS creates no runtime payload or scientific authority.

## Current process — Exp073HT raw runtime producer v0.3

- prereg `docs/dsir4/prereg/EXP073HT_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_3.md`;
- prereg blob `3bdbda16db2640dc68ab91cd34fbd85da787e2c8`;
- prereg commit `7c745691c6a6370f120fe7c65ccdf30c072d8b9d`;
- workflow `.github/workflows/exp073ht-c2-reference-raw-runtime-producer-v0-3.yml`;
- workflow blob `9d99107f0dc309e5c05810085d92c5149531e0c0`;
- workflow implementation commit `b75d7aa497beae88eaef3e8a353dc66c2249129e`;
- binding/head commit `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`;
- workflow/run ID `34235038323`;
- job ID `102090438079`;
- branch/head `main / bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`;
- checkpoint namespace: `N/A` — GitHub-hosted bounded raw producer, not home-heavy checkpoint work;
- start time `2026-09-08T13:55:58Z`;
- runner ownership GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: **IN_PROGRESS** in `Execute frozen 28-request raw producer v0.3`;
- last durable completed stages: frozen binding verification `SUCCESS`; exact post-HS solver + HN serializer build `SUCCESS`;
- expected token `PASS_EXP073HT_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_3`;
- candidate classification ceiling `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`.

Frozen runtime target: exactly 28 distinct requests in z-major/k-minor order, exactly one exact native endpoint observation per request, one 64-byte packet per request, canonical aggregate exactly 1792 bytes. No interpolation, tolerance, nearest-z/k/time, effective-coordinate, rounding or averaging rescue is permitted.

### Exact next actions

On HT terminal SUCCESS: inspect raw log and artifact; verify GitHub digest, run/job/head receipt binding, post-HS source/config fingerprints, 28 packet identities/order, 64-byte packet size, exact 1792-byte aggregate and aggregate SHA256. Only then classify the HT candidate `+0/+0`. Do **not** decode, map or create scientific authority in HT. After a validated candidate, dispatch only a separately prospectively frozen admission/receipt gate.

On HT FAIL/BLOCKED: diagnose the first causal implementation/runtime/provenance defect from logs, preserve any valid complete output unit, repair only the smallest causal defect prospectively, and do not change frozen scientific equations/arithmetic/model/grid/tolerances/ABI/provenance.

C2 remains `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE` until a later explicit admission gate says otherwise.

Global frozen DSIR boundaries remain unchanged.
