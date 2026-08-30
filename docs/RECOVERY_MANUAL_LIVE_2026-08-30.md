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

## Historical authority/negative record

Preserve categories distinctly:

- Exp073R1/U/V/W/Y/Z2/AB: established real/non-classifying authorities/prerequisites.
- Exp073Z v0.1: numerical implementation failure, not science.
- Exp073AD/AE/AF/AG: hosted synthetic/governance PASSes, +0 readiness.
- Exp073X: `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`.
- Exp073X2R primary P: hosted exact repeatability PASS / +0 readiness, canonical Wm_S0 SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.
- Exp073X2 Q: immutable `SCIENTIFIC_REPEATABILITY_FAIL` for exact operator repeatability, not dark-sector model physics.
- Exp073AH2: hosted forensic PASS / +0 readiness, class `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE`; Q-A equals P exactly, Q-B SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`, with `472922/479232` differing entries and max absolute difference `2.0816681711721685e-17`; no frozen input/contract drift detected.

Historical production route remains blocked by Exp073AF:

`P PASS + Q SCIENTIFIC_REPEATABILITY_FAIL -> BLOCK_PRODUCTION`.

Do not launch the remaining 13 Exp073AA tasks under that route.

## Exp073AI — active prospective deterministic exact reproducibility route

Run `33310888983`, head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d` is the only active heavy route.

Replica jobs:

- A `99255607805`;
- B `99255607640`.

Latest inspection: both remain inside `Compute exact single-thread replica`; latest run artifact count is `0`. Do not duplicate AI.

Frozen physical/angular contract is unchanged: real DES Y1, genuine weighted redMaGiC lens mask, `NSIDE=4096`, RING/C, PyMaster 2.7, 39 frozen bandpowers, true ell `0..12287`, spin-0 x spin-2, selected `TE <- TE`, canonical `<f8 [39,12288]`, no effective ell/z/k, radial/support/fiducial-P/covariance/nuisance/quotient/relation/null/G8 information.

Both replicas prospectively force one-thread controls:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

No tolerance, rounding, ULP allowance or majority voting.

Frozen replica job timeout is `240` minutes; aggregate timeout `20` minutes.

Valid AI numerical outcome semantics only after valid comparison:

- exact SHA equality + `numpy.array_equal(A,B)==True` -> `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`;
- complete authorities reaching comparison but exact disagreement -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1`.

AI PASS/FAIL contributes +0 readiness and never reclassifies historical Q. Even AI PASS does not automatically authorize Exp073AA production; a future succession amendment must be separately prospective.

## Exp073AJ2 — environment provenance firewall

Exp073AJ v0.1 failed synthetically before reading real AI because of an `unhashable dict` implementation error. Preserve that as implementation failure, not science.

Exp073AJ2 narrow repair obtained hosted synthetic PASS:

- run `33313584914`;
- artifact `9732737233`;
- digest `sha256:087ae5f1e01feac476317afcf4cfea3c8f4ee491c4edc0127b338c8ba7ffb49a`;
- token `PASS_EXP073AJ2_AI_ENVIRONMENT_PROVENANCE_CLASSIFIER_SYNTHETIC_V0_2`.

AJ2 can later label environment provenance only (`CONTROL_DRIFT`, `SOFTWARE_BUILD_DRIFT`, `CONTROLLED_SOFTWARE_AND_HOST_MATCH`, `CONTROLLED_SOFTWARE_MATCH_HOST_RUNTIME_DIVERGENCE`). It cannot inspect the AI numerical outcome while producing the label, change AI PASS/FAIL, select a preferred replica, introduce tolerance, release production or read support/covariance/nuisance/G8.

## Exp073AK / Exp073AK2 — completion authority firewall

### AK v0.1 retained implementation failure

Frozen chain reached hosted run `33316169150`, job `99269912588`. Prospective freeze passed; synthetic matrix failed because several test-harness `check(...)` calls omitted the fixture argument. No real AI receipt/token was read.

Permanent classification:

`IMPLEMENTATION_FAILURE_SYNTHETIC_HARNESS_MISSING_FIXTURE_ARGUMENT_BEFORE_CLASSIFICATION_NOT_SCIENCE`.

### AK2 v0.2 narrow repair

Only self-test call sites were repaired; classifier semantics were unchanged.

Frozen chain:

- prereg `61b725cc3e98acb6374b9165acbbb77deba10284`;
- implementation `6ca671ad6145ae5b78977958999ec5bdae380fbb`;
- workflow `14f5c3ebafe663479b454c7944d95cb9277207cf`;
- workflow freeze `d82ed284e80d2157f55418b205bb7b00f7fa87c2`;
- trigger/head `8f2d7a2d5b909c475dcd1940f82d9332129462ce`;
- hosted run `33316242357`, job `99270113118` = success;
- artifact `9733523834`;
- digest `sha256:f08e772acab3a0c08269fa637d8dc8fe6a4839a73630e04048d86680e8ab94bb`;
- token `PASS_EXP073AK2_AI_COMPLETION_AUTHORITY_CLASSIFIER_SYNTHETIC_V0_2`.

Classification: `HOSTED_SYNTHETIC_COMPLETION_CLASSIFIER_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

Hosted-tested state semantics:

- queued/in-progress -> `PENDING_EXP073AI`;
- both complete replica authorities + successful aggregate + valid frozen final token -> `VALID_HOSTED_EXP073AI_CLASSIFICATION`, preserving the exact AI token;
- replica non-success before complete authority -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_EXECUTION`;
- replica success but incomplete/missing artifact -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_ARTIFACT`;
- complete replicas but aggregate job non-success -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATOR_EXECUTION`;
- aggregate success but final artifact/token missing or malformed -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATE_AUTHORITY`;
- unknown/conflicting control-plane state -> `INVALID_CONTROL_PLANE_STATE_NO_SCIENCE_CLASSIFICATION`.

Therefore timeout, cancellation, artifact loss or aggregator failure can never be silently promoted to repeatability FAIL. A repeatability FAIL may be recorded only if the frozen AI comparator actually emits its frozen FAIL token in a valid final hosted authority.

AK2 reads no angular values/support/covariance/nuisance/G8, cannot release production and adds +0 readiness.

## Current authorized route

`Exp073AI active -> Exp073AK2 terminal/control-plane classification -> immutable hosted AI token only if valid -> AJ2 independent environment-provenance label when both receipts exist -> only then consider a separately prospectively frozen succession rule`.

Do not duplicate AI and do not launch the remaining 13 Exp073AA tasks while AI is active or absent a future explicit succession authority.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/RECOVERY_LATEST.md`
4. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
5. `recovery/2026-08-30_exp073ak_failure_exp073ak2_hosted_pass_ai_still_running.md`
6. `experiments/073ai_article3_single_thread_exact_reproducibility_v0_1_prereg.md`
7. `experiments/073aj2_article3_ai_environment_provenance_classifier_v0_2_prereg.md`
8. `experiments/073ak2_article3_ai_completion_authority_classifier_v0_2_prereg.md`
9. `experiments/073ah2_article3_q_repeatability_forensic_binding_v0_2_prereg.md`
10. `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`
11. `experiments/073ag_article3_exact_14window_authority_aggregator_schema_v0_1_prereg.md`
12. `experiments/073ae_article3_presupport_authority_join_schema_v0_1_prereg.md`.
