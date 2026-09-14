# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/determinism threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed reproducibility chain through V0.16

V0.12: `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`; cubic interpolation supported on the three offending cells but replay invariant blocked promotion.

V0.13: `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`; frozen failure cells split across independent hosted jobs while anchors passed.

V0.14: `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED`; repeated identical solver construction within one runner/process was stable, localizing the defect to cross-job/host conditions.

V0.15 authority `docs/dsir4/authority/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, run `34792546153`: `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED`. Repeated identical recorded fingerprints had zero within-group failure spread; distinct fingerprints reproduced the response branches.

V0.16 authority `docs/dsir4/authority/LAYERB_BETA_HOST_FACTOR_ISOLATION_V0_16.json`, creation commit `3e9058d54ea19278eaa40c083ecae9e933be64dc`, run `34793440750`: `HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION`, effect `+0/+0`. Invariant + 24 host lanes + decision all succeeded. Decision artifact `10328803638`, SHA256 `4302ca588a5e3c596e33cff89ed76b674546934f547327032e7049e808f35208`.

V0.16 found both AVX512F classes well populated (`15` absent, `9` present), internally stable and separated on both failure witnesses. Yet the exact AMD EPYC 9V74 model group itself spans the response branches, with same-model spreads `1.4832557923366384e-4` and `1.0478978062540487e-5`. This excludes CPU model name as a sufficient factor. It does not prove AVX512 causality because other runtime state remains correlated.

V0.16 authorizes exactly `PROSPECTIVELY_FROZEN_NUMERICAL_RUNTIME_STATE_FINGERPRINT_AUDIT`.

## V0.17 — active prospectively frozen numerical runtime-state fingerprint audit

Preregistration: `prereg/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.md`, commit `7a52ef36718f319e85f4fd62729fdf72b08d6876`.

Contract: `docs/dsir4/contracts/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json`, commit `cb0eeb9d899433c4fe8705a2c822a0973e79ebdb`.

Executor: `ci/layerb_beta_numerical_runtime_state_fingerprint_v0_17.py`, commit `f934d4c2edc2295709a1adda8556059c7c1d4357`, blob `3d846cc128d57b9bc76392b0c0caef1cdcf96ac6`.

Workflow: `.github/workflows/layerb-beta-numerical-runtime-state-fingerprint-v0-17.yml`, commit `90812dd35753758086dcc0cee8d74909471bb519`.

Launch/head: `57af57896bb2f92e347eed84b08233e05a07b184`.

Authoritative active run: `34817501445`; exactly one V0.17 run exists. The frozen invariant audit has passed and 32 independent GRID1024/PURE_PAIR runtime-state lanes are distributed with `max-parallel: 32`; a single decision waits for all lanes.

Primary target subgroup is frozen to exact AMD EPYC 9V74, minimum six jobs. Runtime-state hierarchy is frozen before execution: full CPU capability/HWCAP state -> FPU control state -> exact CLASS/classy and loaded numerical-library hashes -> NumPy runtime dispatch -> full composite state. Repeated factor groups need at least two jobs. Ephemeral runner/job/process/address/timing fields are forbidden classifiers.

## Exact next order

1. Continue only V0.17 run `34817501445`; no duplicate.
2. Do not inspect partial substantive lane values.
3. After invariant + all 32 lanes + decision are terminal, verify decision artifact identity/digest and the frozen classifier.
4. Materialize durable V0.17 authority.
5. Follow only V0.17 `next_stage`; any observational stratification can authorize only a separate controlled intervention.
6. Keep full Layer-B/science gates closed unless a later terminal authority explicitly opens them.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`; numerical reproducibility work alone does not raise them.
