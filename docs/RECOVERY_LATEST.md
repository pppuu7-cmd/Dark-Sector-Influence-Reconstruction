# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention/reproducibility threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; full 107-row Layer-B remains closed.

## Closed numerical runtime/replay chain through V0.23

V0.18R/V0.19 false-invalid outcomes were caused by the wrong NumPy validation observable. V0.20 response-free validated the actual runtime-dispatch mask; V0.21 causally localized the hosted branch to NumPy AVX-512 runtime dispatch; V0.22 established a deterministic forced NumPy non-AVX512 baseline across hosted witnesses.

V0.23 terminal authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.json`, creation commit `2aa8ff62a47c1aa367f102032bdb7b2267a9fa94`. Run `34878651714`, decision job `104107495389`, artifact `10364150389`, digest `sha256:f787799c177bba95e0630206108a1448169b6e76b17a36b20f4439f7b58a17cd`. Classification `FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_REVALIDATED`, effect `+0/+0`. All 32 lanes eligible; all 15 frozen V0.12 production-h pure-common-grid replay cells have cross-host spread `0.0` and native-class mean separation `0.0`; both original V0.13 production-h replay failures are repaired.

V0.23 authorizes exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT`.

## V0.24 — active forced-baseline production-h interpolation reassessment

Preregistration: `prereg/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_V0_24.md`, commit `67e92ef1fb11e8cf607d693f0b38d64a31003258`, blob `98867c67848fe0300acbd19599150be88296bcbd`.
Executor: `ci/layerb_beta_forced_baseline_production_h_common_grid_interpolation_reassessment_v0_24.py`, commit `8bddca0baaa72446a6ae230114193ce74a4c318d`, blob `8281b0c2ebb23e72f6bdaf2abc6b48edf1e137a8`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_V0_24.json`, commit `f71f6a957cd2f61659f87e4ec108c7ed0e18d4ce`, blob `3078645d3463241fa00e405c10c8d8f5fb1206da`.
Workflow: `.github/workflows/layerb-beta-forced-baseline-production-h-common-grid-interpolation-reassessment-v0-24.yml`, commit `3b6af7e97a21ea14992e3b5d13c91ff3394a9d87`, blob `5e408a4d052ddf396248abb21fd54e557032120f`.
Launch/head: `3a655cf12614955716898c7943e5d638d6a1cf1f`.
Authoritative run: `34884436750`; exactly one run observed.
Invariant job `104111442454` terminal `success`; invariant artifact `10363529948`, digest `sha256:a04bf9a69f4dc83bc66b4dd8c23d1f5c7588df478d3d654d6424b37603ed4669`.

The invariant reconstructed the historical direct-TOL300 object response-free and found exactly 38 deduplicated D-domain V0.4 probe rows and 38 unique direct k nodes. This is the frozen direct node set used by V0.24; no single-k shortcut is permitted.

The V0.23 workflow hardening omission is repaired: every `interpolation-lane` has explicit `needs: invariant-audit`. No substantive lane could start before the successful invariant.

V0.24 gates only the two immutable V0.12 production-h parent violations: GRID768/T2 and GRID896/T3. Each eligible lane computes 10 CLASS constructions: pure/mixed +/- for the two grids (8) plus fresh historical-semantics D-domain direct +/- (2), all under the exact validated forced NumPy baseline. Mixed grids retain the union with all three V0.12 audit target k values. Historical unforced direct numeric values are descriptive/non-gating.

Before any mechanism classification, all eight primitive response series (pure_interp, mixed_interp, mixed_exact, direct for each of two cells) must have cross-host spread `<1e-5` and native-class mean separation `<1e-5`. Frozen V0.12 scientific mechanism threshold remains `1e-3`, and support requires per-cell unanimity across all eligible lanes.

## Exact next order

1. Continue only run `34884436750`; do not create a duplicate or rerun lanes while they are active.
2. Do not inspect partial substantive lane artifacts or response values.
3. Wait for all 32 interpolation lanes and the single decision barrier.
4. Verify terminal decision artifact ID/digest; only then read `decision.json` and materialize V0.24 authority.
5. Follow only its encoded `next_stage`; do not prepare a successor based on partial values.
6. Full Layer-B and all physical-science gates remain closed.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
