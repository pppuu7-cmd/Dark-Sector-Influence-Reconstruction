# Exp073AJ — Article 3 Exp073AI environment-provenance classifier v0.1

**Frozen:** 2026-08-30 while Exp073AI run `33310888983` is still computing both exact replicas and before any AI replica artifact or numerical comparison result exists.

## Purpose

Exp073AJ is a non-scientific, non-classifying provenance gate. It prospectively freezes how the two Exp073AI runtime-environment receipts will be compared after the heavy run completes, so a later PASS/FAIL cannot be explained post hoc by selectively chosen environment differences.

It does **not** read the angular arrays, canonical hashes, support, covariance, nuisance geometry or G8, and it cannot release production. Hosted synthetic PASS contributes **0** Article-3 scientific readiness; readiness remains 52%, G7/G8/G9 remain OPEN.

## Frozen identity

- Exp073AI run: `33310888983`.
- replica jobs: A `99255607805`, B `99255607640`.
- required receipt experiment: `Exp073AI`.
- required replica labels: `A`, `B`.
- required readiness: `52`.
- required gates: `G7/G8/G9 = OPEN`.
- `science_gate_scored=false`, `production_release=false`.

## Frozen thread-control equality

Both receipts must contain exactly:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

Any missing, extra, or unequal thread-control value is `CONTROL_DRIFT`.

## Frozen software equality

The full `versions_and_numpy_config` string must be byte-identical between A and B. Any difference is `SOFTWARE_BUILD_DRIFT`.

## Frozen platform comparison

The following exact fields are compared but are not required to be equal for the provenance classifier to be valid:

- `github.runner_os`
- `github.runner_arch`
- `github.image_os`
- `github.image_version`
- `platform`
- `machine`
- `processor`
- `nproc`
- normalized `uname`
- normalized `lscpu`

Differences are recorded as `HOST_RUNTIME_DIVERGENCE` only; they do not retroactively modify the frozen Exp073AI numerical PASS/FAIL criterion.

Volatile resource fields `memory`, `filesystem`, and `ulimit` are retained and SHA256-recorded but are not used to label numerical reproducibility.

## Frozen classifier

1. malformed schema/identity/readiness/gates/firewall -> `INVALID_RECEIPT` hard failure;
2. thread-control drift -> `CONTROL_DRIFT`;
3. software/build-config drift -> `SOFTWARE_BUILD_DRIFT`;
4. controls and software identical, platform fields identical -> `CONTROLLED_SOFTWARE_AND_HOST_MATCH`;
5. controls and software identical, any platform field differs -> `CONTROLLED_SOFTWARE_MATCH_HOST_RUNTIME_DIVERGENCE`.

The classifier must never inspect the AI numerical result when producing this label.

## Required hosted synthetic token

`PASS_EXP073AJ_AI_ENVIRONMENT_PROVENANCE_CLASSIFIER_SYNTHETIC_V0_1`

This token means only that the preregistered provenance classifier behaves fail-closed. It is not scientific PASS, not an Exp073AI result, not production authority, and adds zero readiness.
