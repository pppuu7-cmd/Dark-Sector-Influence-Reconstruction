# DSIR authoritative recovery — latest

Updated: 2026-09-13. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth. Older recovery notes are immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`; stabilized `tol_perturb_integration=1e-12`. V0.13 additionally freezes a technical replay threshold `<1e-5`. Covariance/whitening/nuisance/relation-null remain unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this chain.

## Closed chain through V0.11

V0.5: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`.

V0.6: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`.

V0.7: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`.

V0.8: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`.

V0.9: `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`; independent TOL300R=`1e-12` gives 16/20 recovery.

V0.10: `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`; GRID512 recovers 16/20 and GRID1024 14/20.

V0.11 authority `docs/dsir4/authority/LAYERB_BETA_COMMON_GRID_DISCREPANCY_V0_11.json`, run `34748453026`: `PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED`. The tested resolution path `512→640→768→896→1024` shows sparse coordinate/resolution-specific discrepancies rather than a uniform common-grid failure. Frozen parent violations were `GRID640,h=2e-4:0.003709335890188209`, `GRID768,h=1e-4:0.004037659729341879`, and `GRID896,h=1e-4:0.0011351878950117023` versus independent direct TOL300.

## V0.12 — terminal interpolation audit with replay invariant blocker

Authority: `docs/dsir4/authority/LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_V0_12.json`, creation commit `b6f0f7e8f3042c55ba47f860cc03210d393a808b`.

Run `34749034836`, head `0daf43908e276482eb3b02e45d9d93af02bc43f2`; decision job `103703327770`; decision artifact `10314853600`, ZIP SHA256 `cee9d8d9c951fab434b7b32db4a97aa62d0e684e9df625da8dceb43272f30f16`.

Classification: `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`, effect `+0/+0`.

All three frozen parent violation cells reproduce. At all 3/3 offending cells: pure common-grid interpolation and mixed-grid interpolation are identical; mixed exact-target response agrees with independent direct-k TOL300; and the interpolated response retains the parent discrepancy. Thus the V0.12 diagnostic records `interpolation_supported_count=3` and `node_set_dependence_supported_count=0`.

Formal promotion is blocked by three non-offending replay failures against the stricter frozen `<1e-5` technical replay invariant. They are:

- `GRID1024`, `h=2e-4`, target `z=0.4175,k≈0.0122344992`: replay relative difference `0.00015506392790000525`.
- `GRID768`, `h=1e-4`, target `z=0.62,k≈0.01551635149`: replay relative difference `0.000024934371090895516`.
- `GRID1024`, `h=1e-4`, same `z=0.62` target: replay relative difference `0.000010478978062540487`.

All three are below the scientific `1e-3` threshold, but the frozen replay invariant may not be relaxed post hoc. V0.12 therefore authorizes no scientific promotion and only diagnosis of the replay invariant failure.

## V0.13 — active replay sequencing / reproducibility audit

Executor: `ci/layerb_beta_replay_sequencing_v0_13.py`, creation commit `d1825ec35c69c3dc62a3fdd77194a52c6829f87e`, blob `83ae5ff8ebd9cf2123099b354be8b6e724186705`.

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_BETA_REPLAY_SEQUENCING_V0_13.json`, creation commit `9105ff24f4561ec61cf286425bc143d6a98aabdf`.

Workflow: `.github/workflows/layerb-beta-replay-sequencing-v0-13.yml`, creation commit `7e2d8803bc41ddd3645eb518775961b9f81f5c8a`.

Launch commit `7c0a10a24f38966f830b7fc2438d8c134e6b5853`; active run `34773514342`.

V0.13 freezes 12 independent hosted lanes: `GRID768/GRID1024 × PURE_PAIR/INTERLEAVED × R1/R2/R3`. It tests the exact three V0.12 replay-failure cells plus two parent-like anchors. The classifier distinguishes execution-order/interleaving state dependence, cross-run parent non-reproducibility, same-profile hosted numerical nondeterminism, non-reproduced V0.12 replay failures, mixed replay behavior or invariant failure. No V0.13 outcome directly opens science gates; any positive diagnosis only authorizes a separately frozen confirmation/reproducibility successor.

At the latest write 10/12 profile lanes are already in progress, two are queued for hosted-runner capacity, and invariant is queued. No partial profile values may be used to change the frozen classifier.

## Exact next order

1. Continue only V0.13 run `34773514342`; no duplicate V0.13 run.
2. Wait for all 12 profile lanes, invariant and frozen decision barrier.
3. Verify decision artifact provenance and write a durable V0.13 authority.
4. Follow only the decision's encoded `next_stage`.
5. Keep full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and science gate closed unless a later prospectively frozen authority explicitly opens them.

## Publication/readiness locks

Frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic progress alone does not change them. Article-II real cross-family G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation / ownership

Repository/Actions state wins over any stale automation prompt. DSIR scheduled automation must not be assumed enabled unless a later explicit task-state check confirms it. Avoid a duplicate DSIR control plane while this chat is actively advancing V0.13.

V0.13 is GitHub-hosted diagnostic compute, not a self-hosted `DSIR-HOME-PC` heavy-science run.
