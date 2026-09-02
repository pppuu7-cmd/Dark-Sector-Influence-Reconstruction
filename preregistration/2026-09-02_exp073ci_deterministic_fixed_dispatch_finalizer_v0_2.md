# Exp073CI — deterministic fixed-dispatch Wm_S2 finalizer v0.2

Date: 2026-09-02
Class: NEW_VERSION_EXACT_REPEATABILITY_EXPERIMENT

## Historical authority boundary

Exp073CF finalizer v0.1 remains a permanent exact scientific repeatability FAIL. Exp073CI is a NEW prospectively versioned finalizer contract. No Exp073CI outcome may retroactively reclassify Exp073CF or select a preferred historical replica.

Exp073CH diagnostic run `33645970816` isolated the v0.1 divergence to CPU-dependent native OpenBLAS solve dispatch with identical compact input and identical K:
- native Zen -> historical-A W SHA `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`;
- native Cooperlake -> historical-B W SHA `bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e`;
- forced dispatch was internally and cross-worker exact per fixed core.

## Prospective deterministic dispatch choice

The v0.2 contract freezes:
- `OPENBLAS_CORETYPE=Nehalem`
- `OPENBLAS_NUM_THREADS=1`
- `OMP_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`
- historical visible numerical package/build pins used in Exp073CF/CH.

`Nehalem` is selected prospectively as the conservative fixed x86 OpenBLAS kernel among the tested regimes, avoiding CPU-native dispatch and avoiding post-hoc preference for either historical A or historical B. Its diagnostic W SHA differs from BOTH historical replicas, so v0.2 cannot be interpreted as preferred-replica rescue.

Expected fixed-dispatch exact hashes observed before this preregistration in the nonclassifying Exp073CH diagnostic and frozen here prospectively:
- K SHA256 `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`
- v0.2 fixed-Nehalem W SHA256 `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`

These are validation targets for the NEW contract, not a rewrite of v0.1.

## Immutable compact authority inputs

Two independently produced Exp073CF compact artifacts are used to test both artifact provenance lanes even though the compact comparator established exact content equality:

A:
- source run `33601943300`
- artifact `9841348367`
- artifact digest `sha256:d6703819745b22eadc9c6557c4d89d926ed9675c09bd41cb19e79d4050ef399b`

B:
- source run `33601943300`
- artifact `9848067175`
- artifact digest `sha256:7e655144c07959f4ba7c6c6d82db0685b58e425958fa308e6b9e698ad6e30737`

Both must fail closed on canonical compact `<f8 [39,12288]` SHA256:
`963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`.

The original production finalizer arithmetic source remains `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`, authority path-history commit `d77b7ba88801f6788f3d386e72b445c7859c7153`. Exp073CI changes the numerical backend dispatch contract, not K construction or `np.linalg.solve(K,A)` algebra.

## Execution contract

Hosted-only `ubuntu-24.04`, four independent workers R1..R4. No self-hosted runner.

Each worker:
1. captures CPU/runtime/OpenBLAS metadata and verifies `OPENBLAS_VERBOSE=2` reports `Core: Nehalem` for every solve process;
2. independently consumes both compact-A and compact-B artifacts;
3. runs three fresh-process solves per artifact;
4. requires exact canonical K and W hashes for every repeat;
5. requires A/B artifact lanes exact-equal under the new finalizer contract.

Final comparator requires exact equality across all workers, both artifact lanes, all repeats, expected K SHA, and expected v0.2 W SHA. No tolerance, ULP, rounding, smoothing, averaging, majority vote, or preferred-replica rescue.

## Preregistered classification

PASS token:
`PASS_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2`

PASS requires ALL:
- every worker and fresh-process repeat valid;
- `Core: Nehalem` confirmed in every solve process;
- compact input SHA exact in both A/B lanes;
- K SHA exact expected value in all solves;
- W SHA exact expected v0.2 value in all solves;
- exact equality across A/B lanes and R1..R4.

Otherwise FAIL token:
`SCIENTIFIC_REPEATABILITY_FAIL_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2`

An infrastructure failure before valid complete comparator inputs is `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CI`, +0/+0.

A PASS establishes exact repeatability only for NEW finalizer v0.2. A FAIL is permanent for this v0.2 contract. Neither changes Exp073CF v0.1 history.

## Readiness boundary

This experiment alone does not increment Article-3 readiness. Readiness remains frozen until the repository readiness ledger prospectively accepts the new version and its downstream semantic/criteria binding. `readiness_delta=[0,0]` for this execution.
