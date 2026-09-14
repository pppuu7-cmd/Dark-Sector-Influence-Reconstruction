# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Current terminal authority — V0.17 numerical runtime-state fingerprint audit

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json`, creation commit `ae9d1532d7ad7479a8eee52d04e974ebf9ab7d17`.

Preregistration: `prereg/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.md`, commit `7a52ef36718f319e85f4fd62729fdf72b08d6876`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json`, commit `cb0eeb9d899433c4fe8705a2c822a0973e79ebdb`.
Executor: `ci/layerb_beta_numerical_runtime_state_fingerprint_v0_17.py`, commit `f934d4c2edc2295709a1adda8556059c7c1d4357`, blob `3d846cc128d57b9bc76392b0c0caef1cdcf96ac6`.
Workflow: `.github/workflows/layerb-beta-numerical-runtime-state-fingerprint-v0-17.yml`, commit `90812dd35753758086dcc0cee8d74909471bb519`.
Launch/head: `57af57896bb2f92e347eed84b08233e05a07b184`.

Run `34817501445` is terminal `success`: invariant + 32 independent runtime-state lanes + decision all succeeded. Decision job `103894789121`; decision artifact `10337134088`, digest `sha256:24bf51b3993353dceefe4908955d0e14eb48de06675174e1b7b9ede3ab3f7ae4`.

Classification: `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`, effect `+0/+0`.

Within the exact frozen `AMD EPYC 9V74 80-Core Processor` subgroup (`n=8`), the same-CPU-model cross-job variation was reproduced. The two failure witnesses have spreads `1.4832557923366384e-4` and `1.0478978062540487e-5`; the anchor spread is `1.0758876522574515e-6` and exact requested-node binding remains within `1.6551974349255386e-16`.

The preregistered hierarchy selected `cpu_capability_key` as the first admissible stable stratifier: at least two repeated capability groups are internally stable below `1e-5` on both failure cells and their group means separate by at least `1e-5` on both cells. `fpu_control_key` and `binary_runtime_key` do not explain the split. `numpy_runtime_key` also stratifies and is correlated with CPU capability. This is observational numerical-runtime stratification only, not causal proof, Layer-B validation, or dark-sector evidence.

Authorized next stage exactly: `PROSPECTIVELY_FROZEN_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## Frozen boundaries / anti-duplication

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/determinism threshold `<1e-5`; production sampling `0.00035`; `tol_perturb_integration=1e-12`; exact binding `<=1e-12`; CLASS/baseline/precision/JJ/extraction identities frozen. No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or downstream science gate is authorized.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`.

## Exact next order

1. Do not repeat V0.17.
2. Prospectively preregister the controlled CPU-capability dispatch intervention before substantive execution.
3. Freeze the intervention, target host/capability eligibility, exact native/control conditions, all thresholds, PASS/FAIL/BLOCKED/INVALID branches, and interpretation ceiling before result.
4. Prefer within-host paired intervention so hardware/software/binary identity is held fixed; use independent hosted jobs only as independent replications.
5. Keep all downstream science gates closed unless a later terminal authority explicitly opens them.
