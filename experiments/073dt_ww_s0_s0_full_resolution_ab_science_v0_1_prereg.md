# Exp073DT — WW_S0_S0 full-resolution A/B exact scientific activation v0.1

Frozen 2026-09-05 after validated Exp073DP exact-equivalence PASS, Exp073DQ durable A/B driver static PASS, Exp073DR hosted activation/resource PASS, and Exp073DS v0.2 self-hosted readiness PASS, before any full-resolution WW_S0_S0 scientific workspace or selected-EE output exists.

Scope: first scientific authority gate for `WW_S0_S0`. No prior WW_S0_S0 numerical output may be imported.

## Parent authority
- Wm_S3 exact PASS remains preserved and unrelated numerically.
- Exp073DP repaired run/job `33938446310 / 101230897808`, artifact `9960969007`, ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`, token `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`, NaMaster source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- Exp073DQ run/job `33938583879 / 101231302981`, artifact `9961000737`, token `PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_DRIVER_STATIC_ADMISSION_V0_1`, durable driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`.
- Exp073DR run/job `33938637212 / 101231459805`, artifact `9961019381`, token `PASS_EXP073DR_WW_S0_S0_HOSTED_ACTIVATION_RESOURCE_PREFLIGHT_V0_1`.
- Exp073DS v0.2 run `33938789513` attempt 2, jobs `101233076119 / 101233097355`, artifact `9961211035`, GitHub + independent ZIP SHA256 `d12693ce2b2ec17abfef7008e82eca2bf9f9a29b99f43b00c83e30b2313df53d`, raw token `PASS_EXP073DS_WW_S0_S0_HOME_READINESS_EXCLUSIVITY_V0_1`, continuous lock verified, affinity CPUs=8, PyMaster 2.7, actual runtime team=8, nested library threads=1.

## Frozen source and implementation binding
Frozen source authority head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`.
Required implementation:
- `ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py` exact SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`, Git blob `baff99c2b9d7866432bebda5844d2d450324d08a`;
- `ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py` exact SHA256 `ab85f76e724a9861837299ce29c0961e4adcd09954b9522d678d5e610267f641`, Git blob `d6f20600d6a206dd9fbb254b382e71a49c6b3c07`;
- `ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c` Git blob `be4f381de4c5c043a9c0fcd107e63ef3f2079578`;
- `ci/exp073aa_article3_des_angular_task_runner_v0_1.py` Git blob `050ed7dd3387c4fb031f877825e6b3f4d4ce3ef2`; activation must fail closed if repository blob differs.

Contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

## Frozen science
Task exactly `WW_S0_S0`, no lens mask. DES NSIDE=4096, ell=0..12287, 39 frozen bands. Same S0 spin-2 `NmtField` object on both sides. Persist full stock WW `[4,39,4,12288]`; select exactly `wins[0,:,0,:] = EE<-EE`; canonical selected payload `<f8 [39,12288]`.

Replica A and B must be independent fresh namespaces from the already frozen DQ contract:
`checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`.
Complete-stage order is immutable:
`fresh_s0_mask_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`.

No historical WW numerical import; no reading other-replica output before terminal A/B comparison. Verified complete checkpoints may be restored only after exact source-head, contract-fingerprint, namespace, payload SHA, shape/dtype and stage-order verification. A verified complete workspace must never be recomputed unnecessarily.

## Execution and resource contract
Exactly one self-hosted home scientific process. Hosted preflight must fail closed on any competing queued/in-progress self-hosted run. The entire home science body must hold one dedicated nonblocking flock continuously. CPU affinity exactly 8. `OMP_NUM_THREADS=8`, `OMP_DYNAMIC=FALSE`; `OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=NUMEXPR_NUM_THREADS=BLIS_NUM_THREADS=VECLIB_MAXIMUM_THREADS=1`. Compile the already-qualified downstream with `DSIR_WORKERS=8`; prove runtime `DSIR_OMP_TEAM=8` before science.

Stage exact Exp073R1 artifact id `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`, validate with frozen `validate_r1`. PyMaster exactly 2.7.x; no fallback.

Durable science root: `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`. Resume must fail closed and preserve verified complete stages.

## Scientific terminal classification
The underlying DQ driver emits only provisional comparator evidence. Exp073DT scientific PASS is allowed iff the final independently written A/B comparator has:
- provisional status exactly `PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_PROVISIONAL_EXACT_REPEATABILITY_V0_1`;
- `sha256_equal=true`;
- `numpy_array_equal=true`;
- `no_tolerance_rescue=true`;
- both selected payloads exist and each is exact `<f8 [39,12288]`;
- terminal A/B selected SHA values are identical;
- all source/contract/component/checkpoint provenance checks pass.

Then and only then emit scientific token:
`PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`
with `science_gate_scored=true`, `ww_s0_s0_authority_created=true`.

Any exact A/B inequality is `SCIENTIFIC_REPEATABILITY_FAIL`. Runner loss, missing/corrupt checkpoint, provenance mismatch, dependency/runtime failure, artifact failure or malformed receipt is infrastructure/BLOCKED `+0/+0`. Never use tolerance, allclose, rounding, ULP, smoothing or averaging rescue.

PASS advances the frozen frontier to `WW_S0_S1`; FAIL is a scientific result and also advances according to repository governance without rewriting this gate.
