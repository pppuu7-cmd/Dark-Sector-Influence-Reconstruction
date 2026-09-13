# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth. Older recovery notes are immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/determinism threshold `<1e-5`. Covariance/whitening/nuisance/relation-null remain unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed chain through V0.12

V0.5: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`.

V0.6: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`.

V0.7: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`.

V0.8: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`.

V0.9: `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`; independent TOL300R=`1e-12` gives 16/20 recovery.

V0.10: `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`; GRID512 recovers 16/20 and GRID1024 14/20.

V0.11 authority `docs/dsir4/authority/LAYERB_BETA_COMMON_GRID_DISCREPANCY_V0_11.json`, run `34748453026`: `PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED`. Sparse coordinate/resolution-specific discrepancies exist rather than a uniform common-grid failure.

V0.12 authority `docs/dsir4/authority/LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_V0_12.json`, run `34749034836`: `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`, effect `+0/+0`. All three actual offending cells supported cubic-interpolation dominance, but three non-offending replay cells violated the separately frozen technical replay invariant `<1e-5`; no scientific promotion was authorized.

## V0.13 — terminal replay sequencing / reproducibility audit

Authority: `docs/dsir4/authority/LAYERB_BETA_REPLAY_SEQUENCING_V0_13.json`, creation commit `e62158ab101f3da7ff334d39afbfd75520a82699`.

Prospective contract: `docs/dsir4/contracts/LAYERB_BETA_REPLAY_SEQUENCING_V0_13.json`, commit `9105ff24f4561ec61cf286425bc143d6a98aabdf`.

Executor: `ci/layerb_beta_replay_sequencing_v0_13.py`, commit `d1825ec35c69c3dc62a3fdd77194a52c6829f87e`, blob `83ae5ff8ebd9cf2123099b354be8b6e724186705`.

Workflow: `.github/workflows/layerb-beta-replay-sequencing-v0-13.yml`, commit `7e2d8803bc41ddd3645eb518775961b9f81f5c8a`.

Run `34773514342`, head `7c0a10a24f38966f830b7fc2438d8c134e6b5853`; all 12 profile lanes, invariant and decision are terminal `success`. Decision job `103769308584`; decision artifact `10322573705`, ZIP SHA256 `b04db83d530c36e03f2b80ad33fb4be80747817bd08cb2b001d5c8c6375fd202`; total run artifacts `14`.

Frozen classification: `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`, effect `+0/+0`.

All invariants and both anchors passed. The three preregistered replay-failure cells each showed same-profile independent hosted-job spread at or above `1e-5`:

- `GRID1024,h=2e-4,z=0.4175,k≈0.0122344992`: max same-profile spread `1.5506392790000525e-4`;
- `GRID768,h=1e-4,z=0.62,k≈0.01551635149`: `2.4934371090895516e-5`;
- `GRID1024,h=1e-4,z=0.62,k≈0.01551635149`: `1.0478978062540487e-5`.

The two frozen anchors had max same-profile spread `0` and `1.0945880590564914e-6`, respectively. The observed failure-cell values switch between the immutable parent-like and V0.12-like response values. This supports **hosted-run numerical nondeterminism only**. It does not yet distinguish within-run repeated-solver variability from cross-job/runner environmental variability and does not authorize Layer-B scientific promotion.

Authorized next stage, exactly as encoded by V0.13 decision:

`PROSPECTIVELY_FROZEN_SAME_RUN_REPEATED_SOLVER_DETERMINISM_AUDIT`.

## Exact next order

1. Prospectively freeze a same-run repeated-solver determinism audit on the exact V0.13 diagnostic cells and immutable numerical identities.
2. Keep the `<1e-5` technical determinism threshold unchanged; do not use cross-profile differences as evidence of repeated-solver nondeterminism.
3. Run repeated identical solver constructions within one hosted job/process for each frozen GRID/profile lane, with the existing anchors as controls.
4. Only a terminal V0.14 authority may decide whether the variability is within-run or instead requires a cross-host environment/state audit.
5. Keep full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and all downstream science gates closed.

## Publication/readiness locks

Frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic/reproducibility progress alone does not change them. Article-II real cross-family G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation / ownership

Repository/Actions state wins over any stale automation prompt. Avoid duplicate production gates. This chain is GitHub-hosted diagnostic compute, not a self-hosted `DSIR-HOME-PC` heavy-science run.
