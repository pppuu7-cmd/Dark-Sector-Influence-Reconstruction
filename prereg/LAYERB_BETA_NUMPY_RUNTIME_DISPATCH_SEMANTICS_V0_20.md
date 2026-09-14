# DSIR V0.20 preregistration — NumPy runtime dispatch semantics audit

Status: **PROSPECTIVELY FROZEN BEFORE V0.20 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only. This audit is response-free and contains no CLASS/DSIR scientific response computation.

## Parent authority

Parent diagnostic authority: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_VALIDATION_DIAGNOSIS_V0_19D.json`, diagnosis `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`, authorized successor exactly `PROSPECTIVELY_FROZEN_NUMPY_RUNTIME_DISPATCH_SEMANTICS_AUDIT`.

## PURPOSE

Establish the exact NumPy 1.26.4 runtime-dispatch profile on the hosted exact-target AMD EPYC 9V74 runners and validate a NumPy AVX-512 dispatch mask against NumPy's own dispatchable-feature set rather than against unrelated/raw capability bits.

This stage is purely technical. It cannot support or reject the DSIR response-branch hypothesis because no DSIR response is computed.

## OBJECT

Thirty-two independent `ubuntu-24.04` GitHub-hosted jobs. Each job installs exact `numpy==1.26.4` in a fresh venv and records:

- exact `/proc/cpuinfo` vendor/family/model/stepping/model-name and selected AVX features;
- NumPy version;
- `numpy.core._multiarray_umath.__cpu_baseline__`;
- `numpy.core._multiarray_umath.__cpu_dispatch__`;
- full `__cpu_features__` mapping;
- `active_dispatch = [f in __cpu_dispatch__ where __cpu_features__[f] is true]`;
- `avx512_dispatch = [f in __cpu_dispatch__ whose upper-case name starts with AVX512]`;
- `active_avx512_dispatch = avx512_dispatch intersect active_dispatch`;
- raw active AVX-512 capability names from the full `__cpu_features__` mapping for diagnostics only.

A job is target-eligible only if its exact CPU identity is `AuthenticAMD / family 25 / model 17 / stepping 1 / AMD EPYC 9V74 80-Core Processor`, `/proc/cpuinfo` reports AVX512F, and native `active_avx512_dispatch` is non-empty.

For each eligible job, after the native fingerprint, the lane constructs the mask **algorithmically from that lane's native NumPy dispatch list**:

`NPY_DISABLE_CPU_FEATURES = comma-joined sorted(avx512_dispatch)`.

It then launches a fresh child interpreter with that exact environment and records the same NumPy runtime objects. No response, CLASS build, interpolation, solver, covariance, likelihood, nuisance, relation-null, or science object is touched.

## FROZEN VALIDATION PREDICATES

For each eligible lane, `MASK_VALID` requires all of:

1. masked NumPy version remains exactly `1.26.4`;
2. masked `__cpu_baseline__` equals native `__cpu_baseline__` exactly;
3. masked `__cpu_dispatch__` equals native `__cpu_dispatch__` exactly (build capability list unchanged);
4. environment string equals the algorithmically derived comma-joined sorted native `avx512_dispatch` list;
5. every member of native `avx512_dispatch` has `__cpu_features__[feature] == false` under the mask;
6. `active_avx512_dispatch` is empty under the mask;
7. native and masked active non-AVX512 dispatch sets are identical;
8. physical `/proc/cpuinfo` AVX512 capability need not change and is not an intervention-success predicate;
9. residual raw AVX-512 `__cpu_features__` entries that are not members of `__cpu_dispatch__` are diagnostic only and are explicitly permitted to remain true.

## REPLICATION / CONSISTENCY

- required host lanes: 32;
- minimum exact-target eligible lanes: 3;
- promotion requires every eligible lane to satisfy `MASK_VALID`;
- promotion additionally requires all eligible lanes to share one exact native `__cpu_baseline__` list, one exact native `__cpu_dispatch__` list, one exact native `avx512_dispatch` list, and one exact native `active_avx512_dispatch` list;
- ephemeral runner/job/PID/timing values are forbidden classifiers.

## FROZEN DECISION

1. Any source/version/invariant failure or any accidental scientific/CLASS response computation -> `NUMPY_RUNTIME_DISPATCH_SEMANTICS_AUDIT_INCONCLUSIVE`; no promotion.
2. Fewer than 3 exact-target eligible lanes -> `NUMPY_RUNTIME_DISPATCH_SEMANTICS_AUDIT_UNDERPOWERED`; authorize only expanded response-free replication.
3. Exact-target eligible lanes disagree on native baseline/dispatch/AVX512-dispatch/active-AVX512-dispatch profile -> `NUMPY_RUNTIME_DISPATCH_PROFILE_HETEROGENEOUS`; authorize only response-free profile stratification/replication.
4. Any eligible lane fails `MASK_VALID` -> `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_NOT_VALIDATED`; authorize only response-free mask-mechanism diagnosis.
5. Otherwise -> `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`; terminal authority must record the exact common baseline list, dispatch list, AVX512 dispatch list, active AVX512 dispatch list, and exact validated mask string. It authorizes only `PROSPECTIVELY_FROZEN_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## INTERPRETATION CEILING

A PASS establishes only that the NumPy environment intervention is correctly defined and validated against NumPy 1.26.4's runtime-dispatch model on the exact target hosted CPU profile. It is not evidence that NumPy dispatch causes the DSIR numerical branch. It cannot salvage V0.18R/V0.19, cannot alter the frozen V0.17 branch references or scientific thresholds, cannot open full Layer-B, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537, or any physical/dark-sector gate. Effect remains `+0/+0`.
