# DSIR V0.17 preregistration — numerical runtime-state fingerprint audit

Status: **PROSPECTIVELY FROZEN BEFORE V0.17 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only.

Parent terminal authority: `docs/dsir4/authority/LAYERB_BETA_HOST_FACTOR_ISOLATION_V0_16.json` (`HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION`). Parent-authorized successor: `PROSPECTIVELY_FROZEN_NUMERICAL_RUNTIME_STATE_FINGERPRINT_AUDIT`.

## Frozen question

V0.16 showed that AVX512F classes are internally stable and separated, but the exact CPU-model group `AMD EPYC 9V74 80-Core Processor` spans both numerical response branches. V0.17 asks whether that same-model variation is stratified by a reproducible **numerical runtime state** rather than by CPU model name alone.

## Frozen sample/object

Run 32 independent GitHub-hosted `ubuntu-24.04` jobs, all using the unchanged pinned CLASS commit, baseline, precision file, TOL300=`1e-12`, production sampling `0.00035`, GRID1024 and PURE_PAIR response construction. Recompute exactly the two V0.16 replay-failure cells and the exact GRID1024 anchor. Do not read covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 or full 107-row Layer-B.

Primary target subgroup is frozen exactly as:

`AuthenticAMD / family 25 / model 17 / stepping 1 / AMD EPYC 9V74 80-Core Processor`.

Require at least 6 target-model jobs. Runtime-state groups used for factor promotion require at least 2 independent jobs each.

## Frozen runtime-state hierarchy

Within the exact target CPU model, evaluate in this fixed order:

1. `cpu_capability_key`: exact CPU model + microcode + full CPU-flags hash + selected SIMD bits + Linux `AT_HWCAP/AT_HWCAP2` + normalized glibc loader CPU/hwcaps diagnostics.
2. `fpu_control_key`: process rounding mode + MXCSR control bits + x87 control word.
3. `binary_runtime_key`: SHA256 of the loaded `classy` extension / CLASS binaries plus SHA256 set of actually loaded numerical shared libraries (`libc`, `libm`, GSL, OpenMP/OpenBLAS and related runtime libraries when present).
4. `numpy_runtime_key`: normalized NumPy build/runtime dispatch signatures and exact NumPy/SciPy versions.
5. `full_runtime_state_key`: composite of all preceding state plus stable software-control signature.

Ephemeral runner names, job IDs, process IDs, addresses and timing values are recorded only as provenance or excluded entirely; they are forbidden classifiers.

## Frozen invariants

Replay threshold remains `<1e-5`; exact-node binding `<=1e-12`; anchor cross-job spread must remain `<1e-5`; all responses finite; all 32 lanes present; frozen numerical identities unchanged; software-control signature must be constant across the sample; runtime fingerprint must be complete; no scientific/downstream gate opened.

## Frozen classifier

- invariant/control failure -> `NUMERICAL_RUNTIME_STATE_FINGERPRINT_AUDIT_INCONCLUSIVE`; no promotion.
- software-control variation -> `NUMERICAL_RUNTIME_STATE_FINGERPRINT_CONFOUNDED_BY_SOFTWARE_CONTROL_VARIATION`.
- fewer than 6 exact target-model jobs -> `NUMERICAL_RUNTIME_STATE_FINGERPRINT_UNDERPOWERED_TARGET_CPU_MODEL`.
- target-model replay-failure spread no longer reaches `1e-5` -> `V016_SAME_CPU_MODEL_VARIATION_NOT_REPRODUCED_IN_V017`.
- otherwise traverse the frozen factor hierarchy. A factor is supported only if at least two repeated factor groups exist, every repeated group is stable below `1e-5` on both failure cells, and at least one pair of repeated groups differs by `>=1e-5` on **both** failure cells.
  - capability -> `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED` and only a prospectively frozen controlled CPU-capability/dispatch intervention audit is authorized;
  - FPU -> `FPU_CONTROL_RUNTIME_STATE_STRATIFICATION_SUPPORTED` and only a controlled FPU-state intervention audit is authorized;
  - binary/runtime libraries -> `BINARY_RUNTIME_STATE_STRATIFICATION_SUPPORTED` and only a controlled binary-runtime isolation audit is authorized;
  - NumPy dispatch -> `NUMPY_DISPATCH_RUNTIME_STATE_STRATIFICATION_SUPPORTED` and only a controlled NumPy-dispatch intervention audit is authorized;
  - full composite -> `NUMERICAL_RUNTIME_STATE_STRATIFICATION_SUPPORTED` and only a controlled runtime-state intervention audit is authorized.
- if a repeated **full runtime-state** group still varies at/above `1e-5`, classify `RECORDED_NUMERICAL_RUNTIME_STATE_INSUFFICIENT_SAME_STATE_VARIATION` and authorize only a process-initialization/memory-layout audit.
- otherwise classify `NUMERICAL_RUNTIME_STATE_FINGERPRINT_UNDERPOWERED_OR_MIXED` and authorize only expanded prospective replication.

## Interpretation ceiling

V0.17 is a numerical reproducibility/localization audit only. Observational stratification cannot establish causality. It cannot validate full Layer-B, covariance/whitening/nuisance treatment, relation-null, `Wm_S3`, global traversal, dark-sector inference or any physical signal. Readiness remains frozen at Article-III repository readiness 68% and scientific frontier 67% unless a later independent terminal authority explicitly changes them.
