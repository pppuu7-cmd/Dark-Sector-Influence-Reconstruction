# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth. Older recovery notes are immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/determinism threshold `<1e-5`. Covariance/whitening/nuisance/relation-null remain unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed numerical/reproducibility chain through V0.14

V0.5 `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`.

V0.6 `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`.

V0.7 `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`.

V0.8 `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`.

V0.9 `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`.

V0.10 `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`.

V0.11 authority `docs/dsir4/authority/LAYERB_BETA_COMMON_GRID_DISCREPANCY_V0_11.json`, run `34748453026`: `PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED`.

V0.12 authority `docs/dsir4/authority/LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_V0_12.json`, run `34749034836`: `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`, effect `+0/+0`. All three actual offending cells supported cubic-interpolation dominance, but the separately frozen replay invariant failed on three non-offending cells; no scientific promotion.

V0.13 authority `docs/dsir4/authority/LAYERB_BETA_REPLAY_SEQUENCING_V0_13.json`, commit `e62158ab101f3da7ff334d39afbfd75520a82699`, run `34773514342`: `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`, effect `+0/+0`. Three frozen failure cells showed independent-job same-profile spreads `1.5506392790000525e-4`, `2.4934371090895516e-5`, `1.0478978062540487e-5`; anchors remained below `1e-5`.

V0.14 authority `docs/dsir4/authority/LAYERB_BETA_SAME_RUN_SOLVER_DETERMINISM_V0_14.json`, creation commit `1a752a42223043b6efed79dd1294406532d2b48e`, run `34787822995`: `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED`, effect `+0/+0`. All six required jobs were terminal success. Decision job `103810023014`; decision artifact `10327458719`, SHA256 `12e9ea528dfbb12d2041ae927be6f551e84abff8478c74e19508e7b5e3345576`. Every exact diagnostic cell had within-profile max spread `0.0` across three sequential identical repeats in one process; max node mismatch `1.6527975532062504e-16`. Therefore V0.13 variation was not reproduced as a same-run solver-state defect and the remaining blocker is cross-job/runner/environment scoped.

V0.14 authorizes exactly `PROSPECTIVELY_FROZEN_CROSS_HOST_ENVIRONMENT_FINGERPRINT_REPRODUCIBILITY_AUDIT`.

## V0.15 — active cross-host environment fingerprint audit

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, commit `8bdfee04fbdbeece06824d215088797866ed579a`.

Executor: `ci/layerb_beta_cross_host_fingerprint_v0_15.py`, commit `ad811e5da24bb20f654b0bc4d0646640e561150f`, blob `1a51344f0c571704b2b1d01bf4ecb04fe4508083`.

Workflow: `.github/workflows/layerb-beta-cross-host-fingerprint-v0-15.yml`, commit `c3003bf0c8862fee75167bd3afdc415db80e9a99`.

Launch head: `64968099805f6701424881562b1b5263a56d0e0b`. Authoritative active run: `34792546153`; exactly one run exists for this launch. Frozen invariant is terminal success.

V0.15 contains exactly 16 independent hosted jobs: `GRID768/GRID1024 × R1..R8`, `PURE_PAIR` only, with `max-parallel: 16`. It uses the exact V0.13/V0.14 diagnostic cells and unchanged thresholds/numerical identities. The jobs record a prospectively fixed normalized hardware/software fingerprint. Ephemeral runner name, GitHub run/job IDs, run attempt, timestamps and dynamic CPU frequency are provenance only and are forbidden from defining scientific fingerprint groups.

Frozen classifier distinguishes: invariant failure; V0.13 cross-job variation not reproduced; variation persisting inside identical recorded fingerprint groups; stable fingerprint stratification across distinct repeated fingerprint groups; or underpowered/mixed fingerprint evidence. No partial lane values may be used before the single terminal decision barrier.

## Exact next order

1. Continue only V0.15 run `34792546153`; do not launch a duplicate.
2. Wait for invariant plus all 16 frozen lanes and the single decision job to become terminal; do not inspect partial substantive values.
3. Verify every required lane identity and terminal artifact/hash.
4. Materialize a durable V0.15 authority from the frozen classifier.
5. Follow only its encoded `next_stage`.
6. Keep full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and all downstream science gates closed unless a later prospectively frozen terminal authority explicitly opens them.

## Publication/readiness locks

Frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; numerical reproducibility progress alone does not change them. Article-II real cross-family G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation / ownership

Repository/Actions state wins over any stale automation prompt. No active DSIR automation was found in the current task-state check. Avoid duplicate production gates. This chain is GitHub-hosted diagnostic compute, not a self-hosted `DSIR-HOME-PC` heavy-science run.
