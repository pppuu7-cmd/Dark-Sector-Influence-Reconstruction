# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-31.  
**Strict Article-3 scientific repository readiness:** **52%**.  
**Article-2 repository-for-writing readiness:** **100%** for declared scope; not G7/G8/G9 closure.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `recovery/2026-08-31_exp073ay_runtime_budget_prereg_aq_active_forecast.md`
4. `experiments/073ay_article3_controlled_twin_runtime_budget_policy_v0_1_prereg.md`
5. `docs/ARTICLE3_52_PERCENT_BARRIER_FORECAST_2026-08-31.md`
6. `docs/DSIR_ALL_CHAT_REPOSITORY_RECONCILIATION_2026-08-30.md`
7. `docs/RECOVERY_MANUAL_ADDENDUM_EXP065B_EXP067E_2026-08-30.md`
8. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
9. Exp073AT/AU/AV/AW/AX recovery addenda as needed.

Repository/hosted authority outranks chat wording. RTK/RQIR remain excluded from DSIR authority/readiness.

## Current Article-3 scientific state

- strict readiness: `52%`;
- Layer A: OPEN;
- Layer B: OPEN;
- covariance/whitening: BLOCKED;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.

Synthetic, infrastructure, provenance, governance, numerical-QA and forecasting work adds `+0` readiness.

## Current real heavy gate — Exp073AQ Wm_S1

Frozen run:

`33327372191`.

Latest inspection on 2026-08-31:

- replica A job `99299799192`: `IN_PROGRESS` in `Compute exact controlled Wm_S1 replica`;
- replica B job `99299799338`: `IN_PROGRESS` in the same exact compute step;
- no replica artifact/comparator authority existed at the latest inspection.

The run started `2026-08-30T18:12:00Z` (`21:12` Europe/Helsinki). Current replica workflow timeout is 240 minutes, so current AQ has infrastructure budget only until about `2026-08-30T22:12Z` / `2026-08-31 01:12 Europe/Helsinki` unless the compute completes first.

Do not launch Wm_S2 while AQ is active.

Valid comparator terminal classes remain only:

- `PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`;
- `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Failure/cancellation/timeout before valid comparator authority remains infrastructure-INCOMPLETE and is not repeatability FAIL.

## Exp073AY — prospective runtime-budget policy

Preregistered while AQ was still active and before any AQ output:

`experiments/073ay_article3_controlled_twin_runtime_budget_policy_v0_1_prereg.md`

commit:

`3aeffe02afd44c5474cc15cc53007f9beec2b160`.

Frozen infrastructure-only rule:

- future separately preregistered controlled-twin angular replica jobs use `timeout-minutes: 360` on unchanged `ubuntu-24.04` standard GitHub-hosted route;
- NaMaster/PyMaster 2.7 lineage unchanged;
- physical runner remains `ci/exp073aa_article3_des_angular_task_runner_v0_1.py@45ed8d8d1e90cdaf314e0384b6f3cdfef369925b` unless separately prospectively superseded;
- exact single-thread controls unchanged;
- two independent fresh replicas;
- exact SHA equality and `numpy.array_equal == True` unchanged;
- no tolerance/rounding/majority-vote/preferred-replica rescue;
- no partial-output reuse;
- no scientific-readiness increment.

If current AQ reaches valid comparator PASS/FAIL, no Wm_S1 recovery is needed. If it ends before comparator specifically as infrastructure-INCOMPLETE, a separately frozen fresh Wm_S1 twin recovery may use 360 minutes while preserving all scientific/numerical criteria. If a standard hosted replica cannot finish within 360 minutes, no silent runner/hardware/algorithm change is allowed; a new execution-authority succession must be prospectively qualified.

## 52% barrier forecast

Planning-only forecast is recorded in:

`docs/ARTICLE3_52_PERCENT_BARRIER_FORECAST_2026-08-31.md`

commit:

`3740812af4398ed13b193ff3c9bfcc8bce374725`.

Under the strict current serial authority order and assuming active continuation with minimal idle gaps:

- earliest plausible move to a >52%-eligible real candidate manifest: `1-2 September 2026`;
- central/realistic estimate: `2-4 September 2026`;
- infrastructure-risk case: `4-8 September 2026 or later`.

These dates are operational estimates only.

## Why individual angular PASSes do not move readiness

The minimum authorized chain to the next readiness opportunity is:

`Wm_S1 exact twin admission`

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

Only then is an increase above the 52% plateau eligible under frozen accounting. Individual angular authorities remain +0 readiness.

## Controlled single-thread successor authority

Historical primary P exact Wm_S0 SHA

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`

remains historical-route authority only.

Historical Q remains immutable `SCIENTIFIC_REPEATABILITY_FAIL`.

Controlled successor Wm_S0 anchor from Exp073AM:

`8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.

Exp073AO/AP authorize authority class:

`controlled_single_thread_exact_v1`.

Required thread controls:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

No tolerance/ULP/rounding equivalence contract exists.

## Downstream successor prerequisites already frozen

All remain hosted synthetic/non-scientific and +0 readiness:

- Exp073AR — future execution-qualified 14-window aggregate schema;
- Exp073AS — future complete 1410-row pre-support join schema;
- Exp073AT — candidate -> Layer-A admission;
- Exp073AU — Layer-A PASS -> Layer-B admission;
- Exp073AV — same-authority A+B PASS -> covariance read admission;
- Exp073AW — target-independent nuisance SVD numerical-rank/resolvability rule;
- Exp073AX — G7 relation/statistic/null/fit protocol-admission firewall.

Exp073AW rank rule remains:

`tau_rank = eps64 * max(d,m) * sigma_max`.

Retain a singular mode only for `sigma_i > tau_rank`; equality is numerically unresolved and blocks quotient/G7. SVD is required; normal-equation inversion for rank is forbidden.

Exp073AX still requires a separate concrete G7 relation/statistic/decision/null/fit protocol to be content-hash frozen before fitting, with no withheld/G8 reads during discovery/fit.

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
- positive absolute window/operator envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening/nuisance/quotient/relation/null/G8 information during support selection;
- exact threshold ambiguity remains `numerically_unresolved`.

## Important historical negative/supersession records

The all-chat reconciliation remains authoritative for recovery:

- F27/Exp054C prospective C7 quantitative-law FAIL;
- F28 retrospective only;
- F29 prospective C8 FAIL;
- F30 withheld C9 multicoordinate PASS without universal-law closure;
- F31 covariance-null rejection of common-plane relation;
- Exp066B permanent selected-bandpower FAIL;
- Exp066C separate corrective PASS;
- Exp067B permanent CAMB<->CLASS convention HARD FAIL;
- Exp067C/D numerical-floor localization/causal diagnosis;
- Exp067E separate out-of-sample convention PASS;
- Exp068A permanent FAIL separate from Exp068B corrected PASS;
- Exp071C known-sector specificity weakening;
- Exp071L/M/N later representation/resolvability/line-subspace supersession.

Later PASSes never erase earlier frozen FAILs.

## Resume order

1. re-check Exp073AQ run `33327372191` and artifacts;
2. if valid AQ comparator PASS: admit Wm_S1 +0, then prospectively freeze/run Wm_S2 with Exp073AY 360-minute infrastructure budget;
3. if valid AQ comparator repeatability FAIL: preserve FAIL and block successor progression;
4. if AQ ends before comparator as infrastructure-INCOMPLETE: use only a separately frozen fresh Wm_S1 recovery compliant with Exp073AY; no partial reuse;
5. continue remaining angular tasks one-by-one in frozen order;
6. build real Exp073AR aggregate;
7. build real Exp073AS complete 1410-row candidate manifest;
8. only then consider the first legitimate readiness increase above 52%;
9. then real Layer A -> Layer B -> covariance/whitening -> nuisance quotient -> G7 -> frozen relation -> fresh G8.
