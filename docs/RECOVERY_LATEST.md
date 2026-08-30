# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-31.  
**Strict Article-3 scientific repository readiness:** **52%**.  
**Article-2 repository-for-writing readiness:** **100%** for declared scope; not G7/G8/G9 closure.

Repository/hosted authority outranks chat wording. RTK/RQIR are excluded from DSIR authority/readiness.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
4. `docs/LOCAL_COMPUTE_BENCHMARK_2026-08-31.md`
5. `recovery/2026-08-31_exp073ay_runtime_budget_prereg_aq_active_forecast.md`
6. `experiments/073ay_article3_controlled_twin_runtime_budget_policy_v0_1_prereg.md`
7. `docs/ARTICLE3_52_PERCENT_BARRIER_FORECAST_2026-08-31.md` — historical planning record only; its success-conditioned dates are superseded by Exp073AQ FAIL.
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

Synthetic, infrastructure, provenance, governance, numerical-QA, forecasting and root-cause diagnostic work add `+0` readiness.

## Exp073AQ — terminal hosted Wm_S1 authority

Frozen run:

`33327372191`

Source head:

`fe89b6c64ee0cee5dbc40080973ec2af2ae683e0`

Run completed `2026-08-30T22:08:45Z` with workflow conclusion `success`; this means the preregistered comparator executed successfully, not that the scientific gate passed.

Jobs:

- replica A `99299799192`: completed/success;
- replica B `99299799338`: completed/success;
- comparator `99329163628`: completed/success.

Artifacts:

- replica A `9739721339`, digest `sha256:ec6ab1e6a602bd37f7a781a5e8030b09171905e5800b0cfeeba6fabe06e195a1`;
- replica B `9739045909`, digest `sha256:4069f4deb3c608f6fb2c1fa686181746901befbe945cc07374c7d32346778e2f`;
- comparator authority `9739725913`, digest `sha256:5184bb3034bd2c1bd497ad30db3dbd4e1550d09a0c25af328cdee553385fef03`.

Hosted terminal status:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`

Frozen comparator facts:

- `array_equal = false`;
- canonical SHA equality = false;
- replica A selected-window SHA `979c61faea99cf60146078ccdd5a9c75547dcc5a689ee48c4c5f309cf6a10b69`;
- replica B selected-window SHA `5b02a691607dd21ede7601f081767ac3713e300abd5a9e358e4593a6ec486225`;
- differing bands `39 / 39`;
- differing entries `472997 / 479232`;
- maximum absolute difference `2.0816681711721685e-17`;
- mean absolute difference `2.5248672723363528e-20`;
- frozen metadata identical = true;
- controlled single-thread requirements verified = true.

The numerical smallness of the discrepancy cannot alter classification. The frozen contract requires exact canonical SHA equality and `numpy.array_equal == True`; no tolerance, ULP, rounding, preferred-replica, majority-vote or historical-result rescue exists.

Consequences:

- Wm_S1 is not admitted;
- **do not launch Wm_S2**;
- current angular successor chain is blocked;
- no Exp073AR aggregate or Exp073AS candidate manifest may be built from the failed route;
- readiness remains `52%` and the FAIL earns `+0` readiness.

Durable authority checkpoint:

`recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`

## Post-authority diagnostic only

Inspection of the already-frozen replica artifacts found that nearly all selected-window entries differ at very small floating-point scale. Replica environment receipts also identify different GitHub-hosted AMD CPU models:

- A: AMD EPYC 7763;
- B: AMD EPYC 9V74.

This is a candidate environmental source of nondeterminism, not a proven cause. It does not reclassify Exp073AQ and does not authorize any tolerance rescue.

Any recovery from this blocked route requires a separately numbered **prospectively frozen authority succession/root-cause protocol**. Exp073AQ remains permanently FAIL.

## Exp073AY runtime-budget policy

Exp073AY was prospectively frozen before AQ output at commit

`3aeffe02afd44c5474cc15cc53007f9beec2b160`.

Its 360-minute budget was conditional infrastructure policy for separately preregistered exact successors/recovery. Because Exp073AQ reached a valid repeatability FAIL, Exp073AY does **not** authorize Wm_S2 and cannot convert AQ into infrastructure-INCOMPLETE.

The existing exact requirements remain historical/current-contract facts:

- PyMaster/NaMaster 2.7 lineage;
- fresh independent replicas;
- exact single-thread controls;
- exact canonical SHA equality and `numpy.array_equal == True`;
- no tolerance/rounding/ULP/majority-vote/preferred-replica rescue;
- no partial-output reuse.

## Local compute benchmark — completed

Durable record:

`docs/LOCAL_COMPUTE_BENCHMARK_2026-08-31.md`

Latest benchmark result commit:

`90c77f92e273a526803a2a1f20e2efeffbe87ef4`.

Observed local capability:

- 5 Xeon Platinum 8370C vCPU exposed;
- actual cgroup hard memory limit exactly 4 GiB;
- immutable Exp073R1 artifact `9720335366` materialized locally;
- exact S1 NSIDE=4096 source-count map reproduced frozen occupancy SHA;
- true local NSIDE=4096 NaMaster `WW_S1_S1` coupling test was killed at the 4 GiB cgroup ceiling.

Classification remains:

`LOCAL_INFRASTRUCTURE_OOM_BENCHMARK_ONLY`

It is not a scientific/numerical FAIL and earns `+0` readiness.

## 52% barrier state

The earlier `docs/ARTICLE3_52_PERCENT_BARRIER_FORECAST_2026-08-31.md` was explicitly conditional on exact-twin success. Exp073AQ failed that condition, so the previous calendar forecast is no longer operative.

There is currently **no authorized calendar path above 52%** under the failed controlled-route chain.

Before successor angular production can resume, a separately numbered prospective authority-succession protocol must be frozen and validated without erasing or rescuing Exp073AQ.

## Controlled exact authority contract preserved

Historical controlled Wm_S0 anchor:

`8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`

Authority class:

`controlled_single_thread_exact_v1`

Required controls:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

No tolerance/ULP/rounding equivalence contract exists.

## Frozen Article-3 support boundaries

Never alter post hoc:

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

## Resume order from this authority state

1. preserve Exp073AQ as permanent hosted repeatability FAIL;
2. do not launch Wm_S2 or later angular tasks under the failed route;
3. perform only nonclassifying root-cause/provenance diagnostics unless/until a separately numbered prospective authority succession is frozen;
4. any successor protocol must preserve all thresholds/firewalls and cannot use tolerance or a preferred AQ replica;
5. only after a new prospectively authorized execution route establishes its own required authority may the angular chain restart;
6. Exp073AR -> Exp073AS -> Layer A -> Layer B -> covariance/whitening -> nuisance quotient -> G7 -> frozen relation -> fresh G8 remain downstream and blocked until then.
