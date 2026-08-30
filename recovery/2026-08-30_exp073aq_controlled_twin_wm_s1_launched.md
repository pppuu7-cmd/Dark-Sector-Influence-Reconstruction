# DSIR recovery checkpoint — Exp073AQ controlled twin Wm_S1 production launched

**Date:** 2026-08-30

## Scientific-accounting state

- Strict Article-3 scientific repository readiness: **52%**.
- Article-2 repository-for-writing readiness: **100%** for declared scope; not G7/G8/G9 closure.
- Layer A/B: OPEN.
- covariance/whitening: BLOCKED.
- G7/G8/G9: OPEN.
- No RTK/RQIR authority imported.

## Pre-launch duplicate audit

Before launching the next gate, recent commits, Actions and `docs/RECOVERY_LATEST.md` were checked.

Latest authoritative predecessor remained Exp073AO/AP:

- real Exp073AP decision `AUTHORIZE_EXECUTION_QUALIFIED_EXACT_SUCCESSOR_ROUTE`;
- controlled authority class `controlled_single_thread_exact_v1`;
- controlled Wm_S0 anchor SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- historical Q remains immutable `SCIENTIFIC_REPEATABILITY_FAIL`;
- no remaining 13-task production workflow or active heavy job existed after Exp073AP.

Therefore Wm_S1 was the first unexecuted task in the already-frozen successor task order and was selected as the next real non-duplicating production gate.

## Why only Wm_S1 was launched

Exp073AO/AP authorizes 13 remaining tasks but requires exact two-replica equality independently for each task. Launching all 26 heavy replica jobs simultaneously would unnecessarily consume resources before the new controlled production wrapper itself has demonstrated a successful real authority classification.

Exp073AQ therefore prospectively freezes and launches exactly the first remaining task, `Wm_S1`, as two independent hosted replicas. A PASS validates only Wm_S1 and does not automatically authorize admission of later tasks without their own twin checks.

## Exp073AQ frozen chain

### Preregistration

`experiments/073aq_article3_controlled_twin_wm_s1_production_v0_1_prereg.md`

commit `2794ed0a48e8e7f8019584461296661d1a83ae08`.

### Comparator implementation history

Initial comparator commit `64ae1eae3fc8902c0ec4368c2b7209be4fcbc67e` contained a pre-freeze JSON-selection harness error: it temporarily required exactly one JSON even though each replica artifact intentionally contains both operator JSON and environment JSON.

This was detected before workflow freeze, before trigger, and before any Wm_S1 output. The superseding comparator is:

`ci/exp073aq_compare_wm_s1_controlled_twin_v0_2.py`

commit `8772ff5550351d53dfa47aeb05cd83bd6f673750`.

The exact scientific/reproducibility criterion did not change.

### Unchanged physical/angular executor

`ci/exp073aa_article3_des_angular_task_runner_v0_1.py`

last-modifying commit `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b`.

This preserves genuine DES Y1, source S1 count-map semantics, public redMaGiC weighted lens mask with frozen `>0.5` rule, `NSIDE=4096`, PyMaster 2.7, true ell `0..12287`, 39 bandpowers, Wm `TE<-TE`, canonical `<f8 [39,12288]`, and all existing no-support/no-covariance/no-G8 firewalls.

### Workflow

`.github/workflows/exp073aq-article3-controlled-twin-wm-s1-production-v0-1.yml`

commit `42b6241dc90a253cc4d4e8f8dbf72a6a71b46c18`.

### Workflow freeze

`experiments/073aq_article3_controlled_twin_wm_s1_production_v0_1_workflow_freeze.md`

commit `a60c7a2020843e2ea800e361e54cb13ac6c39ac4`.

### Trigger

`ci/exp073aq_article3_controlled_twin_wm_s1_production_v0_1.trigger`

head/trigger commit `fe89b6c64ee0cee5dbc40080973ec2af2ae683e0`.

## Hosted execution state

Hosted run:

`33327372191`

was created at `2026-08-30T18:12:00Z`.

At the checkpoint inspection both independent jobs were running:

- replica A job `99299799192`;
- replica B job `99299799338`.

No aggregator classification or final authority artifact existed yet at this checkpoint.

## Frozen exact criterion

After both valid complete replica artifacts exist:

PASS only if canonical SHA values are exactly identical **and** `numpy.array_equal(A,B)` is true, after validating metadata, environment controls and self-consistent JSON/NPZ hashes.

PASS token:

`PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

If both valid replicas reach the comparator but exact equality fails:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Failure before a valid comparator classification remains infrastructure-INCOMPLETE, not repeatability FAIL.

No tolerance, rounding, ULP allowance, majority vote, preferred replica or closeness-to-P rescue exists.

## Frozen single-thread controls

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

## Scientific accounting

Regardless of Exp073AQ exact PASS or task-specific repeatability FAIL:

- readiness remains 52%;
- readiness increment = 0;
- no dark-sector model scientific PASS is claimed;
- support, covariance, nuisance geometry and G8 remain unread/unavailable to this gate.

A PASS would admit only Wm_S1 to the future controlled-route ordered 14-window authority.

## Next authorized action

First inspect run `33327372191`, both replica artifacts and the aggregator result. Do not launch Wm_S1 again while this run is active.

If Exp073AQ reaches a valid exact PASS, the next unexecuted successor task is `Wm_S2` and should be prospectively frozen/run as its own twin-replica gate under the same authority class. If Exp073AQ is repeatability FAIL, stop admission of Wm_S1 and preserve the negative result. If infrastructure-INCOMPLETE, repair only prospectively without weakening the exact criterion.
