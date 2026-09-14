# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/determinism threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed reproducibility chain through V0.17

V0.12: `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`; interpolation supported at the offending cells, but replay invariant blocked promotion.

V0.13: `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`; exact failure cells split across independent hosted jobs while anchors passed.

V0.14: `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED`; repeated identical solver construction within one process was stable.

V0.15: `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED`; repeated identical recorded host fingerprints were internally stable while distinct fingerprints reproduced the response branches.

V0.16 authority `docs/dsir4/authority/LAYERB_BETA_HOST_FACTOR_ISOLATION_V0_16.json`, run `34793440750`: `HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION`. AVX512F classes stratified, but the exact AMD EPYC 9V74 model itself spanned both branches; CPU model/AVX512 observation was not causal authority.

V0.17 authority `docs/dsir4/authority/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json`, creation commit `ae9d1532d7ad7479a8eee52d04e974ebf9ab7d17`, run `34817501445`: `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`, effect `+0/+0`. Invariant + 32 runtime-state lanes + decision are terminal `success`. Decision job `103894789121`; decision artifact `10337134088`, SHA256 `24bf51b3993353dceefe4908955d0e14eb48de06675174e1b7b9ede3ab3f7ae4`.

Within the prospectively frozen exact AMD EPYC 9V74 subgroup (`n=8`), the two failure-cell spreads are `1.4832557923366384e-4` and `1.0478978062540487e-5`, while the anchor spread is `1.0758876522574515e-6`. The preregistered hierarchy selects `cpu_capability_key`: repeated capability groups are internally stable below `1e-5` and their means separate by at least `1e-5` on both failure witnesses. FPU-control and exact binary/runtime-library identities are not explanatory. NumPy runtime dispatch also stratifies and remains correlated with capability state. This is observational numerical-runtime stratification only.

V0.17 authorizes exactly `PROSPECTIVELY_FROZEN_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## Exact next order

1. Do not repeat V0.17.
2. Prospectively freeze a controlled CPU-capability/dispatch intervention before substantive result.
3. Prefer paired native-versus-forced-dispatch conditions within the same hosted job so host, exact CPU model, binaries and software image are held fixed.
4. Require frozen intervention validation, finite responses, exact binding `<=1e-12`, anchor stability `<1e-5`, and unchanged production h/sampling/tolerance.
5. Treat causal support only as a numerical mechanism result; it still cannot open full Layer-B or dark-sector science by itself unless the successor terminal authority explicitly does so.
6. Keep covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and full 107-row traversal closed.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`; numerical reproducibility work alone does not raise them.
