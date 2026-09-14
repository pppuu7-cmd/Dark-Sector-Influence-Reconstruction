# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth. Older recovery notes are immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/determinism threshold `<1e-5`. Covariance/whitening/nuisance/relation-null remain unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed chain through V0.14

V0.5 `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`.
V0.6 `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`.
V0.7 `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`.
V0.8 `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`.
V0.9 `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`.
V0.10 `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`.
V0.11 `PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED`.
V0.12 `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`; cubic-interpolation dominance was supported on all three actual offending cells but a separately frozen replay invariant blocked promotion.
V0.13 `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`; the three replay-failure cells varied across independent hosted jobs while anchors passed.
V0.14 `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED`; all exact diagnostic cells were perfectly stable across three repeated solver sequences within one runner/process, localizing the remaining defect to cross-job/runner/environment variation.

## V0.15 — terminal cross-host fingerprint reproducibility audit

Authority: `docs/dsir4/authority/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, creation commit `e974d09d9fc4a687da582384da290c8fcb3989e6`.

Contract: `docs/dsir4/contracts/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, commit `8bdfee04fbdbeece06824d215088797866ed579a`.
Executor: `ci/layerb_beta_cross_host_fingerprint_v0_15.py`, commit `ad811e5da24bb20f654b0bc4d0646640e561150f`, blob `1a51344f0c571704b2b1d01bf4ecb04fe4508083`.
Workflow: `.github/workflows/layerb-beta-cross-host-fingerprint-v0-15.yml`, commit `c3003bf0c8862fee75167bd3afdc415db80e9a99`.
Launch/head: `64968099805f6701424881562b1b5263a56d0e0b`.

Run `34792546153` completed successfully. Required jobs: invariant + 16 independent `GRID768/GRID1024 × R1..R8` host lanes + decision, all terminal `success`. Decision job `103820921014`; decision artifact `10328836120`, SHA256 `147aedae7d660c7554078151ee5ed6ba5985b7317ad5b1f3e18e4cb0f75ca1a4`.

Frozen classification: `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED`, effect `+0/+0`.

All invariants pass: anchors valid; finite values; fingerprint integrity valid; no ephemeral runner/job identifier used in scientific grouping; max requested-node mismatch `1.6551974349255386e-16`.

The exact V0.13 numerical branches reproduce. Cross-job spreads on the three frozen failure cells are `1.5506392790000525e-4`, `2.4934371090895516e-5`, and `1.0478978062540487e-5`; anchors are `0` and `1.0945880590564914e-6`. Repeated jobs sharing the same prospectively recorded combined fingerprint have exactly zero within-group spread on every failure cell. Distinct repeated fingerprint groups have failure-cell group means separated at or above the unchanged `1e-5` threshold.

Thus the numerical defect is reproducibly stratified by the recorded host environment fingerprint. V0.15 does **not** identify which fingerprint field is causal and does not validate Layer-B science or a physical dark-sector signal.

## Authorized next stage

V0.15 authorizes exactly:

`PROSPECTIVELY_FROZEN_HOST_FACTOR_ISOLATION_AUDIT`.

Post-terminal comparison of representative repeated groups is allowed only for selecting prospective candidate factors. It shows:

- AMD EPYC 9V74 and Intel Xeon Platinum 8573C can share the same response branch and the same V0.15 software fingerprint despite different vendor/model;
- AMD EPYC 7763 occupies the alternate response branch;
- between AMD EPYC 9V74 and AMD EPYC 7763 all recorded software fields are equal except the NumPy-config hash, while CPU model/flags differ;
- therefore CPU vendor alone is not a sufficient candidate separator, and the next high-information factor family is runtime SIMD/AVX-512 capability versus finer CPU-model/runtime/toolchain confounding.

These are candidate-selection observations, not a causal conclusion.

## Exact next order

1. Prospectively freeze V0.16 host-factor isolation before generating new substantive values.
2. Preserve exact numerical identities and thresholds; use new independent hosted jobs rather than reclassifying the V0.15 sample as confirmation.
3. Predeclare a small hierarchy: AVX512F present/absent; exact CPU model key; runtime/NumPy SIMD signature; stable OS/kernel/toolchain controls.
4. Require repeated samples in each tested factor class. If factor classes are not populated or remain perfectly confounded, classify `UNDERPOWERED/CONFOUNDED`, not PASS/FAIL.
5. Keep all Layer-B downstream science gates closed until a later terminal authority explicitly opens them.

## Publication/readiness locks

Frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; numerical reproducibility progress alone does not change them. Article-II real cross-family G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation / ownership

No active DSIR ChatGPT automation and no repository cron/schedule research loop were found in the latest explicit check. Repository/Actions state wins over stale prompts. Avoid duplicate production gates.
