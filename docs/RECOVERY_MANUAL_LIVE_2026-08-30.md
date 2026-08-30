# DSIR RECOVERY MANUAL — live 2026-08-30 overlay

This is the active overlay to `docs/RECOVERY_MANUAL.md`. Read it with `docs/RECOVERY_LATEST.md`, `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`, and the newest recovery checkpoint.

## Active state

- Article-2 repository-for-writing readiness: **100%** for declared scope; not global G7/G8/G9 closure.
- Strict Article-3 scientific repository readiness: **52%**.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED.
- synthetic/infrastructure/governance/forensic/reproducibility/provenance QA adds **0 scientific-readiness points** unless a future prospectively frozen scientific-accounting rule explicitly states otherwise.
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

## Established historical authority chain

Preserve categories distinctly:

- Exp073R1/U/V/W/Y/Z2/AB: established real/non-classifying authorities/prerequisites.
- Exp073Z v0.1: numerical implementation failure, not science.
- Exp073AD/AE/AF/AG: hosted synthetic/governance PASSes, +0 readiness.
- Exp073X: `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`.
- Exp073X2 original P aggregate: `INCOMPLETE_INFRASTRUCTURE_MISSING_NUMPY_BEFORE_REPEATABILITY_CLASSIFICATION`.
- Exp073X2R primary P: hosted exact repeatability PASS / +0 readiness, canonical Wm_S0 SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.
- Exp073X2 Q: immutable `SCIENTIFIC_REPEATABILITY_FAIL`; this is a failure of the exact operator-repeatability criterion, not a dark-sector model-physics failure.
- Exp073AH v0.1: forensic transcription implementation failure, not science.
- Exp073AH2: hosted forensic PASS / +0 readiness, class `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE`.

Q-A canonical SHA equals P exactly. Q-B SHA is `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`. AH2 found `472922/479232` differing entries across all 39 bands with max absolute difference `2.0816681711721685e-17`; no frozen input/contract drift was detected. Tiny magnitude does not override the frozen exact criterion; Q remains FAIL.

Historical production route remains blocked by Exp073AF:

`P PASS + Q SCIENTIFIC_REPEATABILITY_FAIL -> BLOCK_PRODUCTION`.

Therefore do not launch the remaining 13 Exp073AA tasks under that route.

## Exp073AI — active prospective deterministic exact reproducibility route

Exp073AI was frozen only after the Q FAIL and AH2 forensic localization. It is a new route, not a Q rescue, and cannot reclassify historical Q.

Frozen scientific/angular contract remains unchanged:

- real DES Y1 Exp073R1 source-mask authority;
- genuine DES Y1 redMaGiC lens mask with original positive weights retained iff `mask>0.5`;
- `NSIDE=4096`, RING/C;
- NaMaster/PyMaster 2.7 lineage;
- 39 frozen bandpowers;
- true ell `0..12287`;
- spin-0 x spin-2;
- selected `TE <- TE` response;
- canonical `<f8 [39,12288]` window;
- no effective ell/z/k, radial/support/fiducial-P/covariance/nuisance/quotient/relation/null/G8 information.

Exact replica implementation is reused unchanged from commit `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`.

### Frozen deterministic execution controls

Both replicas use:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

No tolerance, rounding, ULP allowance or majority voting is allowed.

### Environment capture

Before workspace construction each replica persists OS/image labels, `uname`, `lscpu`, processor count, memory/filesystem/ulimit, all thread variables, Python/PyMaster/NumPy/Healpy/Astropy versions and NumPy build configuration. These receipts are provenance only; they cannot choose a preferred numerical output.

### Prospective identity

- prereg `033d8502a9bfb3e44f4a8adc20a9e08457032277`;
- comparator `98e1518c34e30b0a7e59724ae60b7586f8c52f9c`;
- workflow `a0135ba38290d30e8c98e06882aafe3044bba8f4`;
- workflow freeze `63877ad51da61eb28a1b2385c046a6b19d132202`;
- trigger/head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`;
- hosted run `33310888983`;
- replica A job `99255607805`;
- replica B job `99255607640`.

Latest inspection: both replica jobs are still inside `Compute exact single-thread replica`; no authority artifact exists yet.

### Frozen AI outcome semantics

If both replicas reach comparison:

- exact SHA equality and `numpy.array_equal(A,B)==True` -> `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`;
- otherwise -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1`.

If comparison is never reached, classify only the appropriate infrastructure-INCOMPLETE state. AI PASS/FAIL is nonclassifying for dark-sector physics and adds +0 readiness.

Even a future AI PASS does not automatically authorize Exp073AA production. A separate prospective succession/authority-selection amendment may be created only after the AI hosted outcome exists.

## Exp073AJ — prospective environment-provenance classifier v0.1

AJ was frozen while AI was still computing so later explanations of AI PASS/FAIL cannot cherry-pick environment differences.

Frozen AJ chain:

- prereg `361b86c7bb6215ea700e6a5c16578c059628987c`;
- implementation `4bea0c22c452916db0a6c20caef0782a1f3801f8`;
- workflow `bd8f98bac96d665db5c4cc44187610d83a792650`;
- freeze `39b666b9c214c873dab01f53dd7df512ed35f226`;
- trigger/head `eb423aa97fbc03635328ee2fff4519c9929ea041`;
- hosted run `33313517040`, job `99262678309`.

The run passed freeze enforcement but failed in the synthetic matrix with `TypeError: unhashable type: 'dict'` because the serializer attempted to use receipt dictionaries as dictionary keys. No real AI receipt or numerical output was read.

Preserve classification:

`IMPLEMENTATION_FAILURE_UNHASHABLE_DICT_BEFORE_CLASSIFICATION_NOT_SCIENCE`.

## Exp073AJ2 — narrow repaired environment-provenance classifier v0.2

AJ2 preserves every AJ classifier branch and changes only resource-SHA serialization to stable string keys `A` and `B`.

Frozen chain:

- prereg `33796a506ed375060a61c8ac22d7fdc1ee10bf5f`;
- implementation `d2ebf1769c2d0a86c8a0c3e2235e2da8ace074b5`;
- workflow `7a98eb2d763c8fa570f13dd22da839bde593b488`;
- workflow freeze `6e8733d656868eee615f4fcbe7dc631025312b15`;
- trigger/head `bcd287c8b648ab30568c7232d309dcffb4a7667f`;
- hosted run `33313584914` = success;
- artifact `9732737233`;
- digest `sha256:087ae5f1e01feac476317afcf4cfea3c8f4ee491c4edc0127b338c8ba7ffb49a`;
- token `PASS_EXP073AJ2_AI_ENVIRONMENT_PROVENANCE_CLASSIFIER_SYNTHETIC_V0_2`.

Classification: `HOSTED_SYNTHETIC_PROVENANCE_QA_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

Future AJ2 labels, produced without reading the AI numerical result:

- malformed receipt/accounting/firewall -> invalid;
- thread-control mismatch -> `CONTROL_DRIFT`;
- software/NumPy-build mismatch -> `SOFTWARE_BUILD_DRIFT`;
- controls/software equal and host fields equal -> `CONTROLLED_SOFTWARE_AND_HOST_MATCH`;
- controls/software equal but host fields differ -> `CONTROLLED_SOFTWARE_MATCH_HOST_RUNTIME_DIVERGENCE`.

Volatile memory/filesystem/ulimit fields are SHA-recorded for provenance but cannot determine numerical reproducibility. AJ2 cannot alter AI PASS/FAIL, introduce tolerance, select a preferred replica, release production, or read support/covariance/nuisance/G8.

## Current authorized route

`Exp073AI deterministic exact reproducibility -> immutable hosted AI outcome -> real AJ2 environment-provenance label when both receipts exist -> only then consider a separate prospectively frozen succession rule`.

Do not duplicate AI while run `33310888983` is active. Do not launch the remaining 13 Exp073AA tasks until a future explicit succession authority exists.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/RECOVERY_LATEST.md`
4. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
5. `recovery/2026-08-30_exp073aj_failure_exp073aj2_hosted_pass_ai_still_running.md`
6. `experiments/073ai_article3_single_thread_exact_reproducibility_v0_1_prereg.md`
7. `experiments/073aj2_article3_ai_environment_provenance_classifier_v0_2_prereg.md`
8. `experiments/073ah2_article3_q_repeatability_forensic_binding_v0_2_prereg.md`
9. `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`
10. `experiments/073ag_article3_exact_14window_authority_aggregator_schema_v0_1_prereg.md`
11. `experiments/073ae_article3_presupport_authority_join_schema_v0_1_prereg.md`.
