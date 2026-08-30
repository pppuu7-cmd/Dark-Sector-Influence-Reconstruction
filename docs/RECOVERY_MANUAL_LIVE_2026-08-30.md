# DSIR RECOVERY MANUAL — live 2026-08-30 overlay

This is the active overlay to `docs/RECOVERY_MANUAL.md`. Read it with `docs/RECOVERY_LATEST.md`, the DSIR cross-chat consolidation, and the newest recovery checkpoint.

## Active state

- Article-2 repository-for-writing readiness: **100%** for declared scope; not global G7/G8/G9 closure.
- Strict Article-3 scientific repository readiness: **52%**.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED.
- synthetic/infrastructure/governance/forensic/reproducibility QA adds **0 scientific-readiness points** unless a future prospective scientific-accounting rule explicitly states otherwise.
- DSIR remains independent of RTK/RQIR.

## Frozen Article-3 boundaries

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid row fraction `<=0.05` inclusive;
- minimum final retained dimension `15`;
- DES classifying route `NSIDE=4096`;
- positive absolute operator/window envelopes only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening, nuisance SVD/rank, quotient/relation/null or G8 during support selection;
- exact-threshold ambiguity remains `numerically_unresolved`.

## Established prerequisite chain

Preserve historical categories distinctly:

- Exp073R1/U/V/W/Y/Z2/AB: established real/non-classifying authorities/prerequisites.
- Exp073Z v0.1: numerical implementation failure, not science.
- Exp073AD/AE/AF/AG: hosted synthetic/governance PASSes, +0 readiness.
- Exp073X: `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`.

## Primary P authority

Primary X2 run `33300997298` produced two successful immutable replicas. Its original aggregator failed before comparison because NumPy was absent; preserve that event as `INCOMPLETE_INFRASTRUCTURE_MISSING_NUMPY_BEFORE_REPEATABILITY_CLASSIFICATION`.

Prospectively frozen Exp073X2R repaired only the lightweight aggregator runtime with `numpy==2.1.3` and ran the unchanged comparator. Hosted run `33305930375`, job `99242380374`, artifact `9730454167`, digest `sha256:f054b7fb30935f77fe7b187ba5130d23ebc99185c482e3682ae56b840ed5fea0` established exact within-P repeatability.

Canonical P Wm_S0 SHA:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

Classification: `REAL_HOSTED_NONCLASSIFYING_EXACT_WM_S0_REPEATABILITY_AUTHORITY_PASS_PLUS_0_READINESS`.

## Historical Q exact-repeatability FAIL

Q run `33301058260` produced two valid replica artifacts, but its frozen comparator reached numerical comparison and found unequal canonical SHA / `numpy.array_equal`.

Preserve Q permanently as:

`SCIENTIFIC_REPEATABILITY_FAIL`.

This is failure of the prospectively frozen angular-operator reproducibility criterion, not failure of a dark-sector model.

Exp073AH2 later established hosted forensic class `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE` with no detected frozen input/contract drift:

- Q-A canonical SHA exactly equals P: `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`;
- Q-B SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- `472922/479232` elements differ across all 39 bands;
- max absolute difference `2.0816681711721685e-17`.

Interpretation boundary: consistent with low-level runtime/hardware/thread floating-point nondeterminism, but root cause unproven. Tiny magnitude cannot retroactively weaken the exact criterion. Q remains FAIL.

The old route remains blocked by Exp073AF:

`P PASS + Q SCIENTIFIC_REPEATABILITY_FAIL -> BLOCK_PRODUCTION`.

Therefore do not launch the remaining 13 Exp073AA tasks under that route.

## Exp073AI — new prospective single-thread exact reproducibility route

Exp073AI was frozen only after the Q FAIL and AH2 forensic localization. It does not reclassify Q and cannot rescue the historical route.

Scientific/angular contract remains exactly the same as Exp073X2:

- real DES Y1 Exp073R1 source-mask authority;
- genuine DES Y1 redMaGiC lens mask with original positive weights retained iff `mask>0.5`;
- `NSIDE=4096`, RING/C;
- NaMaster/PyMaster 2.7;
- 39 frozen bandpowers;
- true ell `0..12287`;
- spin-0 x spin-2;
- selected `TE <- TE` response;
- canonical `<f8 [39,12288]` window;
- no effective ell/z/k, radial/support/fiducial-P/covariance/nuisance/quotient/relation/null/G8 information.

Exact replica implementation is reused unchanged from commit `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`.

### Frozen deterministic execution controls

Both replicas A/B run with:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

No tolerance, rounding, ULP allowance or majority vote is allowed.

### Stronger environment capture

Before workspace construction each replica persists a diagnostic environment receipt with OS/image labels, `uname`, `lscpu`, processor count, memory/filesystem/ulimit, all thread variables, Python/PyMaster/NumPy/Healpy/Astropy versions and NumPy build configuration. These receipts may explain a result later but cannot be used to choose a preferred replica post hoc.

### Prospective identity chain

- prereg `033d8502a9bfb3e44f4a8adc20a9e08457032277`;
- Exp073AI comparator `98e1518c34e30b0a7e59724ae60b7586f8c52f9c`;
- workflow `a0135ba38290d30e8c98e06882aafe3044bba8f4`;
- workflow freeze `63877ad51da61eb28a1b2385c046a6b19d132202`;
- trigger/head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`;
- hosted run `33310888983`;
- replica A job `99255607805`;
- replica B job `99255607640`.

At the current manual update both jobs have started; authority is pending.

### Frozen outcome semantics

If both replicas reach comparison:

- exact SHA equality and `numpy.array_equal(A,B)==True` -> `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`;
- otherwise -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1`.

If comparison is never reached, classify only the appropriate infrastructure-INCOMPLETE state.

Both PASS and FAIL are nonclassifying for dark-sector physics, preserve Article-3 readiness at 52%, and leave G7/G8/G9 OPEN.

### Production succession firewall

Even a future Exp073AI PASS does **not** authorize the remaining 13 Exp073AA tasks. A separate prospectively frozen succession/authority-selection amendment must be created only after the Exp073AI outcome exists. This prevents retroactive substitution for the failed Q route.

## Current route status

Historical route:

`X2 P/Q -> Exp073AA`

remains blocked by Q FAIL.

Active research route:

`Exp073AI deterministic single-thread reproducibility test -> outcome authority -> only then consider a prospective succession rule`.

Do not duplicate Exp073AI while run `33310888983` is active. If it remains active, work only on independent non-conflicting validation/provenance prerequisites.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/RECOVERY_LATEST.md`
4. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
5. `recovery/2026-08-30_exp073ai_single_thread_exact_reproducibility_launched.md`
6. `experiments/073ai_article3_single_thread_exact_reproducibility_v0_1_prereg.md`
7. `experiments/073ai_article3_single_thread_exact_reproducibility_v0_1_workflow_freeze.md`
8. `experiments/073ah2_article3_q_repeatability_forensic_binding_v0_2_prereg.md`
9. `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`
10. `experiments/073ag_article3_exact_14window_authority_aggregator_schema_v0_1_prereg.md`
11. `experiments/073ae_article3_presupport_authority_join_schema_v0_1_prereg.md`.
