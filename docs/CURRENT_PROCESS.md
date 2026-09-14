# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Parent terminal authority — V0.16

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_HOST_FACTOR_ISOLATION_V0_16.json`, creation commit `3e9058d54ea19278eaa40c083ecae9e933be64dc`.

Run `34793440750`, launch head `cb30b8bad9dbebd22138e3a8a73c974e4625c0e3`; invariant + 24 independent host lanes + decision all terminal `success`. Decision job `103824243912`; decision artifact `10328803638`, digest `sha256:4302ca588a5e3c596e33cff89ed76b674546934f547327032e7049e808f35208`.

Classification: `HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION`, effect `+0/+0`.

AVX512F classes were both populated (`15` absent, `9` present), internally stable on the frozen failure cells and separated between class means. However, the exact `AMD EPYC 9V74 80-Core Processor` model group itself spanned the branches: maximum same-model failure-cell spreads were `1.4832557923366384e-4` and `1.0478978062540487e-5`. Therefore CPU model alone is insufficient and observational AVX512 stratification is not yet a causal mechanism.

Authorized next stage exactly: `PROSPECTIVELY_FROZEN_NUMERICAL_RUNTIME_STATE_FINGERPRINT_AUDIT`.

## Active authoritative frontier — V0.17 numerical runtime-state fingerprint audit

Preregistration: `prereg/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.md`, commit `7a52ef36718f319e85f4fd62729fdf72b08d6876`.

Contract: `docs/dsir4/contracts/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json`, commit `cb0eeb9d899433c4fe8705a2c822a0973e79ebdb`.

Executor: `ci/layerb_beta_numerical_runtime_state_fingerprint_v0_17.py`, commit `f934d4c2edc2295709a1adda8556059c7c1d4357`, blob `3d846cc128d57b9bc76392b0c0caef1cdcf96ac6`.

Workflow: `.github/workflows/layerb-beta-numerical-runtime-state-fingerprint-v0-17.yml`, commit `90812dd35753758086dcc0cee8d74909471bb519`.

Launch/head: `57af57896bb2f92e347eed84b08233e05a07b184`.

Authoritative active run: `34817501445`. Exactly one V0.17 run exists. It contains one invariant job, 32 independent GRID1024/PURE_PAIR runtime-state lanes (`R01..R32`) with `max-parallel: 32`, and one terminal decision barrier. Hosted-runner capacity may queue jobs; do not launch a duplicate.

The invariant identity/scientific checks have passed. Do not inspect partial substantive lane values before the terminal decision.

## Frozen V0.17 object/classifier

Primary subgroup is exact `AuthenticAMD / family 25 / model 17 / stepping 1 / AMD EPYC 9V74 80-Core Processor`, minimum `n=6`. Repeated runtime groups require minimum `n=2`.

Frozen hierarchy, in order: `cpu_capability_key` (full flags/microcode/HWCAP/glibc-hwcaps state), `fpu_control_key` (rounding/MXCSR/x87), `binary_runtime_key` (classy/CLASS + loaded numerical library hashes), `numpy_runtime_key`, then `full_runtime_state_key`.

Promotion requires at least two repeated groups, every repeated group stable below `1e-5` on both failure cells, and repeated-group means separated by at least `1e-5` on both failure cells. Any observational stratifier can authorize only a separately frozen controlled intervention; it is not causal evidence by itself.

## Frozen boundaries / anti-duplication

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/determinism threshold `<1e-5`; production sampling `0.00035`; `tol_perturb_integration=1e-12`; exact binding `<=1e-12`; CLASS/baseline/precision/JJ/extraction identities frozen. No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or downstream science gate is authorized.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`.

Do not launch another V0.17. Consume only the terminal frozen decision after invariant + all 32 lanes complete, verify artifacts/hashes, materialize durable V0.17 authority, then follow only its encoded `next_stage`.
