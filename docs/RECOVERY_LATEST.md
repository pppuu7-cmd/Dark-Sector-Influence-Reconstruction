# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-31.  
**Strict Article-3 scientific repository readiness:** **52%**.  
**Article-2 repository-for-writing readiness:** **100%** for declared scope; not G7/G8/G9 closure.

Repository/hosted authority outranks chat wording. RTK/RQIR are excluded from DSIR authority/readiness.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `recovery/2026-08-31_local_compute_namaster_oom_benchmark_aq_b_complete_a_active.md`
4. `docs/LOCAL_COMPUTE_BENCHMARK_2026-08-31.md`
5. `recovery/2026-08-31_exp073ay_runtime_budget_prereg_aq_active_forecast.md`
6. `experiments/073ay_article3_controlled_twin_runtime_budget_policy_v0_1_prereg.md`
7. `docs/ARTICLE3_52_PERCENT_BARRIER_FORECAST_2026-08-31.md`
8. `docs/DSIR_ALL_CHAT_REPOSITORY_RECONCILIATION_2026-08-30.md`
9. `docs/RECOVERY_MANUAL_ADDENDUM_EXP065B_EXP067E_2026-08-30.md`
10. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
11. Exp073AT/AU/AV/AW/AX addenda as needed.

## Current scientific state

- strict Article-3 readiness: `52%`;
- Layer A: OPEN;
- Layer B: OPEN;
- covariance/whitening: BLOCKED;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.

Synthetic, infrastructure, provenance, governance, numerical-QA, forecasting and local benchmark work add `+0` readiness.

## Exp073AQ — current real Wm_S1 authority gate

Frozen run:

`33327372191`.

### Replica B

Job `99299799338` completed successfully.

- exact compute started `2026-08-30T18:13:24Z`;
- exact compute completed `2026-08-30T21:17:56Z`;
- duration approximately `3 h 04 min 32 s`;
- replica artifact `9739045909`;
- artifact digest `sha256:4069f4deb3c608f6fb2c1fa686181746901befbe945cc07374c7d32346778e2f`.

The B numerical/window payload has **not** been inspected while A remains active. Only status, timing and artifact provenance were read.

### Replica A

Job `99299799192` remained `IN_PROGRESS` in `Compute exact controlled Wm_S1 replica` at the latest inspection.

Therefore:

- no valid AQ comparator authority yet;
- Wm_S1 is not admitted yet;
- do not launch Wm_S2;
- individual replica success earns +0 readiness.

Valid terminal comparator classes remain only:

- `PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`;
- `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Failure/timeout before valid comparator authority is infrastructure-INCOMPLETE, not repeatability FAIL.

## Exp073AY runtime-budget policy

Prospectively frozen before AQ output at commit

`3aeffe02afd44c5474cc15cc53007f9beec2b160`.

For future separately preregistered exact angular tasks:

- standard GitHub-hosted `ubuntu-24.04`;
- replica budget `timeout-minutes: 360`;
- same PyMaster/NaMaster 2.7 lineage;
- same physical runner `ci/exp073aa_article3_des_angular_task_runner_v0_1.py@45ed8d8d1e90cdaf314e0384b6f3cdfef369925b` unless separately prospectively superseded;
- exact single-thread controls unchanged;
- two independent fresh replicas;
- exact canonical SHA equality and `numpy.array_equal == True`;
- no tolerance/rounding/ULP/majority-vote/preferred-replica rescue;
- no partial-output reuse;
- +0 readiness for individual angular authority.

If current AQ terminates before comparator as infrastructure-INCOMPLETE, only a separately frozen fresh two-replica Wm_S1 recovery may use the 360-minute budget.

## Local compute benchmark — completed

Durable record:

`docs/LOCAL_COMPUTE_BENCHMARK_2026-08-31.md`

latest benchmark result commit:

`90c77f92e273a526803a2a1f20e2efeffbe87ef4`.

### Local capability observed

- 5 Xeon Platinum 8370C vCPU exposed;
- actual cgroup hard memory limit exactly 4 GiB;
- immutable Exp073R1 artifact `9720335366` materialized locally;
- exact S1 NSIDE=4096 source-count map reproduced frozen occupancy SHA in `3.39 s` process wall time;
- two fully touched NSIDE=4096 float64 maps fit simultaneously at ~3.1 GiB RSS;
- single-thread SciPy 8192x8192 float64 `rfft2`: `1.736 s`.

### True NaMaster bottleneck test

A relocatable exact benchmark environment was built only for non-authoritative local testing:

- run `33337005305`;
- job `99325597211`;
- artifact `9739351741`;
- digest `sha256:be3886f11b47c665e7494f6a7edb50d01df30c133565666b326dc482a88f0c79`;
- pymaster `2.7`, healpy `1.20.0`, Python `3.11.16`.

A real local `WW_S1_S1` `NSIDE=4096` spin-2 x spin-2 `NmtWorkspace.compute_coupling_matrix` was then started using the exact R1 S1 source authority and the frozen 39 bandpower edges.

Before coupling:

- exact source map: `2.185 s`;
- `NmtField` build: `5.374 s`;
- RSS after field: ~1.80 GiB.

During coupling the local process was killed by cgroup OOM:

- process wall time ~`24.02 s`;
- max RSS before kill `3898528 KiB`;
- `memory.max = 4294967296` bytes;
- `memory.peak = 4294967296` bytes;
- `oom=1`, `oom_kill=1`.

Classification:

`LOCAL_INFRASTRUCTURE_OOM_BENCHMARK_ONLY`.

This is not a scientific/numerical FAIL and produced no selected angular window/hash. The current model execution environment therefore cannot replace the hosted NSIDE=4096 NaMaster authority route because of its 4 GiB memory ceiling, despite strong CPU/map-preparation performance.

## 52% barrier forecast

Planning-only record:

`docs/ARTICLE3_52_PERCENT_BARRIER_FORECAST_2026-08-31.md`.

Current planning range remains conditional on exact-twin success and active serial continuation:

- earliest plausible: `1-2 September 2026`;
- central estimate: `2-4 September 2026`;
- infrastructure-risk case: `4-8 September 2026 or later`.

The local benchmark does not accelerate the authoritative route unless a future higher-memory execution route is separately prospectively qualified.

## Minimum chain to the next >52% opportunity

`resolve Wm_S1 exact twin`

`-> Wm_S2`

`-> Wm_S3`

`-> WW_S0_S0`

`-> WW_S0_S1`

`-> WW_S0_S2`

`-> WW_S0_S3`

`-> WW_S1_S1`

`-> WW_S1_S2`

`-> WW_S1_S3`

`-> WW_S2_S2`

`-> WW_S2_S3`

`-> WW_S3_S3`

`-> real Exp073AR execution-qualified 14-window aggregate`

`-> real Exp073AS complete immutable 1410-row pre-support finite-operator candidate manifest`.

Only then is a strict readiness increase above 52% eligible. Individual angular authorities remain +0.

## Controlled successor authority

Controlled Wm_S0 anchor:

`8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.

Authority class:

`controlled_single_thread_exact_v1`.

Required environment:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

No tolerance/ULP/rounding equivalence contract exists.

## Frozen Article-3 support boundaries

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid observation-row fraction `<= 0.05` inclusive;
- minimum final retained observation dimension `15`;
- DES classifying route `NSIDE=4096`;
- 39 frozen bandpowers, true ell `0..12287`;
- Wm `TE <- TE`; WW `EE <- EE`;
- selected window `<f8 [39,12288]`;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening/nuisance/quotient/relation/null/G8 information during support selection;
- exact threshold ambiguity remains `numerically_unresolved`.

## Resume order

1. re-check Exp073AQ run `33327372191` and artifacts;
2. if valid AQ comparator PASS: admit Wm_S1 +0, then prospectively freeze/run Wm_S2 with Exp073AY 360-minute budget;
3. if valid comparator repeatability FAIL: preserve FAIL and block successor progression;
4. if AQ ends before comparator as infrastructure-INCOMPLETE: only a separately frozen fresh Wm_S1 recovery is allowed; no partial reuse;
5. continue remaining angular tasks one-by-one;
6. real Exp073AR aggregate;
7. real Exp073AS complete 1410-row candidate manifest;
8. only then consider the first legitimate readiness increase above 52%;
9. then real Layer A -> Layer B -> covariance/whitening -> nuisance quotient -> G7 -> frozen relation -> fresh G8.
