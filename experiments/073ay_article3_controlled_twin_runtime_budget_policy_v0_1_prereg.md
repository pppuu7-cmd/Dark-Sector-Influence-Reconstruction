# Exp073AY — Article-3 controlled-twin runtime-budget policy v0.1

**Date:** 2026-08-31 (prospectively frozen while Exp073AQ run `33327372191` is still IN_PROGRESS and before any Exp073AQ replica artifact or comparator authority exists).

**Classification:** infrastructure/provenance policy only; no science gate; +0 readiness.

## 1. Motivation observed before any AQ scientific output

Exp073AQ Wm_S1 began at `2026-08-30T18:12:00Z` on two independent `ubuntu-24.04` GitHub-hosted replicas with the already-authorized `controlled_single_thread_exact_v1` environment. At the time this policy is frozen, both replica jobs remain inside the exact Wm_S1 compute step and no replica artifact/comparator authority has appeared.

The Exp073AQ replica-job workflow budget is `timeout-minutes: 240`. The observed wall-clock consumption before any output therefore reveals an infrastructure-headroom risk, but it reveals no angular-window values and no scientific/support result.

GitHub-hosted standard jobs have a platform execution ceiling of 6 hours. For future controlled-twin production, a 240-minute workflow timeout is unnecessarily tighter than the platform ceiling.

## 2. Frozen infrastructure-only policy

For every **new separately preregistered successor angular task** after Exp073AQ, the replica job timeout SHALL be:

`timeout-minutes: 360`

while retaining all scientific/numerical authority conditions unchanged:

- runner label remains `ubuntu-24.04` unless a separately numbered future authority succession is prospectively frozen;
- PyMaster/NaMaster 2.7 lineage unchanged;
- exact physical/angular runner remains `ci/exp073aa_article3_des_angular_task_runner_v0_1.py` at commit `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b` unless separately superseded prospectively;
- `OMP_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- `VECLIB_MAXIMUM_THREADS=1`;
- `BLIS_NUM_THREADS=1`;
- `OMP_DYNAMIC=FALSE`;
- two independent hosted replicas per task;
- exact canonical selected-window SHA equality;
- `numpy.array_equal == True`;
- no tolerance/ULP/rounding/majority-vote/preferred-replica rescue;
- no partial-output reuse;
- no readiness increment from an individual angular authority.

A timeout change alone is explicitly **not** an execution-route scientific change and cannot alter an already frozen comparator criterion.

## 3. Conditional Exp073AQ timeout recovery

This policy does not alter the currently running Exp073AQ workflow and does not authorize a duplicate Wm_S1 while that run remains active.

Only if run `33327372191` terminates **before valid comparator authority** specifically because a replica is cancelled/timed out/fails infrastructure execution, the run remains:

`INCOMPLETE_INFRASTRUCTURE_NO_REPEATABILITY_CLASSIFICATION`

and a separately frozen fresh Wm_S1 recovery workflow MAY be created with replica `timeout-minutes: 360`, provided it preserves every item in Section 2 and starts two fresh replicas from zero.

Forbidden in such a recovery:

- reuse of any partial AQ workspace/window/output;
- treating one completed AQ replica as authority while recomputing only the other;
- changing task, masks, inputs, runner label, PyMaster lineage, thread controls, comparator semantics, dtype/shape, or exact-equality rule;
- calling infrastructure timeout a scientific/repeatability FAIL.

If Exp073AQ reaches a valid comparator PASS or repeatability FAIL before timeout, no Wm_S1 timeout recovery is authorized or needed.

## 4. Six-hour ceiling rule

If a future standard GitHub-hosted controlled replica fails to complete under `timeout-minutes: 360`, the result is infrastructure-INCOMPLETE before comparator authority. It MUST NOT be rescued by silently switching hardware/runner class, multiprocessing, tolerances, approximate windows, lower NSIDE, altered bandpowers, effective-ell shortcuts, or partial checkpoint reuse.

Any route beyond the standard hosted six-hour ceiling requires a **separately numbered, prospectively frozen execution-authority succession** with fresh reproducibility qualification before it can contribute to the 14-window scientific authority.

## 5. Anti-leakage

At freeze time:

- Exp073AQ final status unknown;
- AQ replica artifacts absent;
- AQ comparator authority absent;
- Wm_S2 and later windows not computed/read;
- radial kernels not read;
- physical-k support not evaluated;
- covariance/whitening not read;
- nuisance geometry not read;
- G7 relation/null not read;
- G8 not read.

This policy may be motivated only by elapsed infrastructure runtime and published platform job limits, not by any window value or downstream scientific outcome.

## 6. Accounting

`article3_scientific_readiness_percent = 52`

`readiness_increment = 0`

`Layer_A = OPEN`

`Layer_B = OPEN`

`covariance_whitening = BLOCKED`

`G7 = OPEN`

`G8 = OPEN`

`G9 = OPEN`

## 7. Forecast implication

Crossing the 52% barrier still requires, at minimum, completion/admission of all remaining exact angular tasks, the real execution-qualified 14-window aggregate, and the real complete 1410-row pre-support finite-operator candidate manifest. Exp073AY only reduces avoidable infrastructure timeout risk; it does not move readiness by itself.
