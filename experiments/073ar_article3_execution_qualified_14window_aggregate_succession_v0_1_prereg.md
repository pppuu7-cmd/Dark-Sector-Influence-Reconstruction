# Exp073AR — Article 3 execution-qualified 14-window aggregate succession v0.1

**Frozen:** 2026-08-30 while Exp073AQ real controlled-twin `Wm_S1` run `33327372191` is still in progress, before any Wm_S1 final comparator authority exists, before any remaining successor task after Wm_S1 is launched, before a real 14-window aggregate exists, and before any Layer-A support value exists.

## Purpose

Exp073AR is a **non-scientific provenance/reproducibility succession gate** for the future exact 14-window angular authority.

The earlier Exp073AG v0.1 schema was frozen before the empirical cross-route authority shift was known. It expected `canonical_exp073x2` for Wm_S0 and `exp073aa` for the other 13 windows. That historical schema remains valid documentation for its historical route, but it is **not** the future production authority after Exp073AO/AP authorized the prospective `controlled_single_thread_exact_v1` route.

Exp073AR freezes the replacement aggregation contract before observing any controlled Wm_S1 result. It does not compute an angular workspace, does not read the running AQ outputs, and does not perform support/covariance/nuisance/G8 science.

Hosted synthetic PASS adds **0 scientific-readiness points**. Strict Article-3 readiness remains `52%`; Layer A/B and G7/G8/G9 remain OPEN.

## Frozen authority succession

Binding upstream governance:

1. Exp073AO protocol commit `b5b7bffa2567e081367580e10c7e9eca276c8d86`;
2. Exp073AP real hosted decision `AUTHORIZE_EXECUTION_QUALIFIED_EXACT_SUCCESSOR_ROUTE`;
3. Exp073AP run `33324664267`, job `99292571445`, artifact `9735869454`, digest `sha256:8c60618717777a3c913053bcd5437c0ab548e294e98b72b9c5c869dcc52caacf`;
4. unchanged physical/angular one-task executor `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`, last modified at `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b`.

No tolerance/ULP/rounding numerical-equivalence contract exists.

## Controlled Wm_S0 anchor

The future aggregate must use exactly the controlled single-thread anchor established by Exp073AM:

- task `Wm_S0`;
- authority class `controlled_single_thread_exact_v1`;
- run `33321661835`;
- job `99284585530`;
- artifact `9735051043`;
- artifact digest `sha256:167c82d36266efc3b7bd058f0cc307ec636b6c8efdb6b39b6e88f52d6edb3d66`;
- exact internal-repeatability token `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`;
- canonical selected-window SHA256 `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- canonical selected window `<f8 [39,12288]`.

The historical primary-P Wm_S0 SHA
`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`
may not appear as the future aggregate Wm_S0 authority. Historical P remains historical-route authority only. Historical Q repeatability FAIL also remains immutable.

## Frozen ordered task set

Exactly once, exactly in this order:

1. `Wm_S0`
2. `Wm_S1`
3. `Wm_S2`
4. `Wm_S3`
5. `WW_S0_S0`
6. `WW_S0_S1`
7. `WW_S0_S2`
8. `WW_S0_S3`
9. `WW_S1_S1`
10. `WW_S1_S2`
11. `WW_S1_S3`
12. `WW_S2_S2`
13. `WW_S2_S3`
14. `WW_S3_S3`

## Successor-entry admission contract

For every task after Wm_S0, the aggregate may accept a window only after a real hosted task-specific controlled-twin comparator has classified exact admission.

Each successor entry must contain exactly:

- `task` — the frozen task identity;
- `authority_class` — exactly `controlled_single_thread_exact_v1`;
- `source_experiment` — a non-empty `Exp073...` identifier;
- `source_run` — positive hosted run id;
- `source_aggregate_job` — positive hosted comparator job id;
- `source_authority_artifact_id` — positive hosted final-authority artifact id;
- `source_authority_artifact_digest` — `sha256:` plus 64 lowercase hex;
- `exact_twin_status` — exactly `EXACT_TWIN_PASS`;
- `replica_a_sha256` — 64 lowercase hex;
- `replica_b_sha256` — 64 lowercase hex;
- `array_equal` — exactly `true`;
- `single_thread_controls_verified` — exactly `true`;
- `selected_window` with exactly:
  - `dtype: "<f8"`;
  - `shape: [39,12288]`;
  - `sha256` — 64 lowercase hex.

Admission requires

`replica_a_sha256 == replica_b_sha256 == selected_window.sha256`

and `array_equal == true`.

No single-replica authority is admissible. No majority vote, preferred replica, tolerance, rounding, ULP allowance, or closeness to historical P is admissible.

The 13 successor `source_experiment` values must be unique. The 14 selected-window SHA values must also be unique across distinct task identities; any genuine future equality requires a new prospective provenance review rather than silent acceptance.

## Exact execution controls inherited from Exp073AO

Every successor comparator receipt must certify the task was built from two replicas under exactly:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

Exp073AR stores only the boolean `single_thread_controls_verified=true` in the aggregate entry; the task-specific immutable hosted authority remains responsible for the detailed environment receipt.

## Frozen numerical/angular semantics

All 14 windows remain:

- genuine DES Y1 authority lineage;
- PyMaster/NaMaster 2.7;
- `NSIDE=4096`, RING/C;
- true ell axis `0..12287`;
- 39 frozen bandpowers;
- Wm `TE <- TE`;
- WW `EE <- EE`;
- canonical little-endian float64 `[39,12288]`;
- no effective ell/z/k shortcut.

Exp073AR does not recompute those quantities.

## Deterministic aggregate identity

The future aggregate must compute a deterministic metadata-manifest SHA256 over canonical UTF-8 JSON serialization of the ordered 14 authority entries using sorted keys and compact separators.

The manifest hash is provenance identity only, not a scientific statistic and not a replacement for the 14 numerical window hashes.

## Fail-closed supersession checks

Reject any aggregate containing:

- historical `canonical_exp073x2` or `exp073aa` future authority classes;
- historical primary-P Wm_S0 SHA;
- any Wm_S0 provenance other than the frozen Exp073AM anchor;
- duplicate, missing or reordered task;
- single-replica successor evidence;
- unequal twin SHA values;
- `array_equal=false`;
- unverified single-thread controls;
- malformed or zero hosted provenance;
- wrong dtype/shape;
- duplicate selected-window SHA across task identities;
- duplicate successor experiment identity;
- unknown top-level/nested fields;
- readiness or G7/G8/G9 drift;
- any downstream science/firewall activation.

## Anti-leakage firewall

The aggregate receipt must keep exactly false:

- `radial_kernel_read`;
- `physical_k_computed`;
- `physical_support_evaluated`;
- `operator_f_invalid_computed`;
- `retained_coordinates_evaluated`;
- `fiducial_P_weighting_used`;
- `covariance_read`;
- `whitening_performed`;
- `nuisance_geometry_read`;
- `nuisance_svd_performed`;
- `relation_null_read`;
- `chi_square_read`;
- `p_value_read`;
- `G8_read`;
- `scientific_pass_claimed`.

Also require:

- `readiness_increment = 0`;
- `article3_scientific_readiness_percent = 52`;
- G7/G8/G9 = `OPEN`.

## Hosted synthetic test matrix

At minimum:

1. exact valid synthetic successor aggregate -> accept;
2. deterministic manifest hash under dictionary insertion-order changes -> pass;
3. historical P Wm_S0 hash -> reject;
4. old `canonical_exp073x2` Wm_S0 class -> reject;
5. old `exp073aa` successor class -> reject;
6. wrong Exp073AM provenance -> reject;
7. task reorder -> reject;
8. duplicate/missing task -> reject;
9. successor twin SHA mismatch -> reject;
10. selected SHA differs from twin SHA -> reject;
11. `array_equal=false` -> reject;
12. single-thread verification false -> reject;
13. duplicate successor source experiment -> reject;
14. duplicate selected-window SHA -> reject;
15. malformed/zero hosted provenance -> reject;
16. malformed digest/SHA -> reject;
17. dtype/shape drift -> reject;
18. unknown field -> reject;
19. firewall activation -> reject;
20. readiness drift -> reject;
21. gate-state drift -> reject.

## Required hosted synthetic QA token

`PASS_EXP073AR_EXECUTION_QUALIFIED_14WINDOW_AGGREGATE_SUCCESSION_SYNTHETIC_V0_1`

This token is governance/provenance QA only. It does not read Exp073AQ outputs, does not admit Wm_S1, does not build the real 14-window authority, does not perform Layer A, and contributes **0** Article-3 scientific readiness.