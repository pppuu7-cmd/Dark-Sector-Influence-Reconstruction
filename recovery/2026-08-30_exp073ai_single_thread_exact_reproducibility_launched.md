# DSIR recovery checkpoint — Exp073AI single-thread exact reproducibility launched

**Date:** 2026-08-30  
**Project:** Dark-Sector Influence Reconstruction (DSIR)

## Scientific-accounting headline

- Strict Article-3 scientific repository readiness: **52%**.
- Article-2 repository-for-writing readiness: **100%** for declared scope; not G7/G8/G9 closure.
- G7/G8/G9: **OPEN**.
- Layer A/B: **OPEN**.
- covariance/whitening: **BLOCKED**.
- Exp073X2 Q remains `SCIENTIFIC_REPEATABILITY_FAIL` under its frozen exact-equality criterion.
- No historical result is reclassified by Exp073AI.

## Pre-launch audit

Before creating any new workflow, latest commits, Actions and `docs/RECOVERY_LATEST.md` were inspected.

Current authoritative blocking state was:

- Exp073X2R P within-chain exact PASS with canonical Wm_S0 SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`;
- Exp073X2 Q exact comparator reached comparison and failed exact SHA/`numpy.array_equal`, permanently retained as `SCIENTIFIC_REPEATABILITY_FAIL` for the operator-repeatability criterion;
- Exp073AH2 hosted forensic PASS localized Q divergence to workspace numerical output with no detected frozen input/contract drift;
- Q-A equals historical P canonical exactly, Q-B differs at tiny floating-point amplitude (`max abs 2.0816681711721685e-17`), but no tolerance/rounding/ULP rule may retroactively rescue Q;
- Exp073AF therefore blocks the old production route;
- no newer user-launched or automation-launched reproducibility workflow existed.

## New prospective route — Exp073AI

Exp073AI asks a new question only:

> Is the exact frozen real-DES Wm_S0 NaMaster operator bitwise reproducible across two fresh independent hosted runners when relevant numerical thread controls are prospectively fixed to one thread and a much richer runtime/hardware receipt is captured?

It does **not** ask whether Q should be reclassified. Q remains FAIL regardless of Exp073AI outcome.

### Frozen scientific/angular contract

Unchanged from Exp073X2:

- real DES Y1 Exp073R1 source-mask authority;
- genuine DES Y1 redMaGiC lens mask with original positive weights retained iff `mask>0.5`;
- `NSIDE=4096`, RING/C;
- PyMaster/NaMaster 2.7 lineage;
- 39 frozen bandpowers;
- true ell `0..12287`;
- spin-0 x spin-2;
- selected `TE <- TE` response;
- canonical `<f8 [39,12288]` window;
- no effective ell/z/k, radial/support/fiducial-P/covariance/nuisance/quotient/relation/null/G8 information.

The exact replica implementation is reused unchanged from commit `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`.

### New frozen execution controls

For both A and B:

- `OMP_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- `VECLIB_MAXIMUM_THREADS=1`;
- `BLIS_NUM_THREADS=1`;
- `OMP_DYNAMIC=FALSE`.

No tolerance, rounding, ULP allowance or majority vote is permitted.

### Runtime/hardware capture

Each replica persists diagnostic environment information before workspace computation, including OS/image labels, `uname`, `lscpu`, CPU model/flags, processor count, memory/filesystem/ulimit, thread variables, Python/PyMaster/NumPy/Healpy/Astropy versions and NumPy build configuration.

These receipts are diagnostic only and may not be used post hoc to choose a preferred replica.

## Prospective commit chain

- preregistration `experiments/073ai_article3_single_thread_exact_reproducibility_v0_1_prereg.md`
  - commit `033d8502a9bfb3e44f4a8adc20a9e08457032277`;
- exact Exp073AI comparator `ci/exp073ai_compare_single_thread_replicas_v0_1.py`
  - commit `98e1518c34e30b0a7e59724ae60b7586f8c52f9c`;
- workflow `.github/workflows/exp073ai-article3-single-thread-exact-reproducibility-v0-1.yml`
  - commit `a0135ba38290d30e8c98e06882aafe3044bba8f4`;
- workflow freeze `experiments/073ai_article3_single_thread_exact_reproducibility_v0_1_workflow_freeze.md`
  - commit `63877ad51da61eb28a1b2385c046a6b19d132202`;
- trigger/head `ci/exp073ai_article3_single_thread_exact_reproducibility_v0_1.trigger`
  - commit `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`.

## Hosted execution

- run `33310888983`;
- head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`;
- replica A job `99255607805`;
- replica B job `99255607640`;
- state at checkpoint creation: both hosted replica jobs have started; authority pending.

## Frozen outcome semantics

If both replicas complete and exact comparison reaches the numerical arrays:

- exact SHA equality + `numpy.array_equal(A,B)==True` -> `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`;
- otherwise -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1`.

If execution ends before valid comparison, classify only the appropriate infrastructure-INCOMPLETE state.

Either PASS or FAIL is nonclassifying for dark-sector physics and contributes **0 readiness**.

## Production firewall

Even a future Exp073AI PASS does **not** release Exp073AA production automatically. A separate prospective succession/authority-selection amendment would be required after Exp073AI outcome exists. This deliberately prevents using the new route to retroactively bypass the failed Q branch.

## Resume instruction

First inspect run `33310888983`, jobs `99255607805` and `99255607640`, and any artifacts. Do not launch another Exp073AI while this run is active. If it remains active, work only on independent non-conflicting validation/provenance tasks. Preserve Article-3 readiness at 52%.
