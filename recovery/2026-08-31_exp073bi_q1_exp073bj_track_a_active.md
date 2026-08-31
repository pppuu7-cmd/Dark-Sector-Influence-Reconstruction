# DSIR recovery — Exp073BI Q1 terminal; Exp073BJ two-thread Track-A active

**Date:** 2026-08-31  
**Scope:** DSIR / Article 3 only; RTK/RQIR excluded.  
**Scientific authority readiness:** **52.0%**  
**Draft/data readiness:** **53.714285714285715%** (display **53.7%**)

## Exp073BI terminal execution-feasibility result

Hosted run **33375467713** is terminal success and produced immutable artifact **9751718353**, digest `sha256:c857b24fdcc0a49b749fbfd538451a8e53bf98f4da9abd92cefce3c4a9df2752`.

Frozen classification:

`BI_Q1_PARALLEL_EXACT_QA_PASS`

Authority facts:

- independent two-thread synthetic outputs: `numpy.array_equal == true`;
- `sha_a == sha_b == 5e00c7377d50a71d88c98a324d53ef403617022c8dadd4a390eebbe7be4612ba`;
- shape `[6,48]`;
- stock-reference max abs difference `8.881784197001252e-16` under the prospectively frozen synthetic-only threshold `1e-12`;
- thread policy `2`;
- readiness increment `+0 Verified / +0 Draft-data`.

BI is synthetic/infrastructure QA only. It does not repair Exp073AQ and is not scientific Wm_S1 authority. Its preregistered consequence is only that a separately frozen full-scale two-thread Track-A successor may now be attempted.

## Exp073BJ prospective freeze

A new classifying successor was created without rewriting historical Exp073BA:

- preregistration commit: `199fc3188808a30d0f364005f9b584a92a262acb`;
- comparator adapter final commit: `66f9727acf7fc94294b6031eaeb34283e1a78058`;
- inherited exact BA comparator commit: `a0b5bd8065c590e20c648215b8d993452fb7339c`;
- inherited heavy implementation commit: `d77b7ba88801f6788f3d386e72b445c7859c7153`;
- workflow creation/freeze commit: `416b4d4717989f9c228c47614d1e9e48f9bc93e4`;
- immutable BJ binding receipt commit: `cbe5f57f9ae04eb335ad9f9b6e4984bdd82247c0`;
- trigger/head commit: `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`.

The binding receipt prospectively binds BI run/artifact/Q1 token, Exp073AZ run/head/PCL authority and canonical PCL SHA, implementation/comparator/workflow lineage, thread controls and the historical Exp073AQ FAIL.

## Only execution change

Relative to Exp073BA, scientific inputs, mathematical operations, shapes and exact acceptance rules are unchanged. The execution policy is:

- `OMP_NUM_THREADS=2`;
- `OPENBLAS_NUM_THREADS=2`;
- `MKL_NUM_THREADS=2`;
- `NUMEXPR_NUM_THREADS=2`;
- `BLIS_NUM_THREADS=2`;
- `OMP_DYNAMIC=FALSE`;
- historical Ubuntu-irrelevant `VECLIB_MAXIMUM_THREADS=1` retained;
- compact timeout remains `360` minutes.

No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue exists.

## Active hosted run

Exp073BJ hosted run **33379013167** was created from trigger/head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`.

At the checkpoint both fresh compact jobs are active:

- compact replica A job `99446854065`: `in_progress`;
- compact replica B job `99446854363`: `in_progress`.

Do not start a duplicate BJ heavy run while this run is active.

## Frozen BJ classification

- Two complete valid compact replicas that are exactly equal by `numpy.array_equal` and canonical byte-SHA equality -> compact PASS and finalizers may run.
- Two complete valid compact replicas with exact mismatch -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1`.
- Failure/cancellation/timeout before two complete valid comparator inputs -> `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073BJ`.
- Final exact PASS requires two finalizer outputs to be exactly equal, finite and have positive per-band absolute norms, yielding `PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`.
- Complete final exact mismatch -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_FINALIZER_EXACT_V0_1`.

A workflow-level success is not by itself scientific PASS; consume the immutable final authority artifact and frozen token.

## Permanent scientific state

- Exp073AQ remains permanent hosted exact-repeatability scientific FAIL.
- Exp073AZ remains predecessor PCL authority PASS only.
- Exp073BF/BE/BI remain QA/provenance only, +0 scientific readiness.
- Exp073BA remains infrastructure/execution incomplete, no scientific classification.
- Exp073BH remains D2 execution-boundary evidence only.
- Exp073BD remains P3 provisional incomplete with no downstream use.

## G7 firewall

Required order remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No covariance/whitening/nuisance/relation/null/G8 leakage is allowed. G8 remains forbidden before actual G7 authorization.

## Exact next operating gate

Inspect run **33379013167** without duplicating it. First verify both jobs pass prospective freeze, exact BI binding, exact AZ PCL binding and enter full-scale two-thread compact compute. When terminal, consume all immutable compact artifacts and exact comparator output. Only if compact PASS is frozen may finalizers/final exact authority be consumed. Classify strictly under the preregistered BJ decision classes above.

`Verified: 52.0% | Draft/data: 53.7%`
