# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention/reproducibility threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; full 107-row Layer-B remains closed.

## Root cause and validated repair

V0.18R/V0.19 false-invalid intervention outcomes came from validating raw non-dispatch AVX-512 `__cpu_features__` capability bits instead of actual NumPy runtime dispatch. V0.19D (`f29190ead75225d8e8862e44ba06b51555c580b2`) diagnosed the defect. V0.20 response-free validated the exact NumPy 1.26.4 dispatch mask. V0.21 then causally established `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`; glibc-only dispatch did not explain the branch.

## V0.22 terminal forced-baseline reproducibility authority

Authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, creation commit `2b3cb46863fb85e6456a5a11e30183acf3b6de10`.
Preregistration `20403f5dbd2a3772752852c0c84ce306d7971c43`; executor `82684fa591911761720e744e5462e51902569fa2`, blob `7921f856f468d9b73889130df39148ccca3d048d`; contract `bc10698aa746747955d27ce2099867de236ef598`; workflow `8c36fdeece4cfc6b6f6c8477282a40c9a2ccff25`; launch/head `d2e4e2cfbc122683d2390369dc087b55e89fb2fc`.

Run `34875798025` terminal success: invariant + 32 lanes + decision. Decision job `104089235776`; decision artifact `10360469338`; digest `sha256:12769549f5d44da9dc01ee82d426dd07e171cefe27282e92e40df15b43ea2ba0`.
Classification `FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED`, effect `+0/+0`.

All 32 lanes were eligible under the exact forced NumPy non-AVX512 runtime baseline. Native classes were represented by 10 AVX512-active and 22 AVX512-inactive hosts. One binary identity and one software-control identity were shared across eligible lanes. Maximum requested-node coordinate mismatch was `1.6551974349255386e-16`.

Terminal numerical result: both replay-failure cells and the anchor had cross-host relative spread `0.0`; native-class mean separation was `0.0` on both failure cells; every forced failure response matched the frozen V0.17 alternate branch with relative mismatch `0.0`. Therefore the validated forced NumPy baseline repairs the specific hosted cross-job numerical reproducibility defect on the frozen witness cells across heterogeneous native dispatch classes.

Interpretation ceiling remains numerical only: no full Layer-B validation, no covariance/whitening/nuisance/relation-null, no `Wm_S3`, no global 65537, no dark-sector or physical-signal claim.

V0.22 authorizes exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT`.

## Exact next order

1. Prospectively freeze the forced-baseline production-h replay revalidation before execution.
2. Keep the exact validated NumPy mask and response-free forced-profile validation as a mandatory preflight.
3. Revalidate only the original production-h numerical replay object; do not open the 107-row Layer-B traversal.
4. Preserve frozen production `h=1e-4`, grid, sampling, `tol_perturb_integration=1e-12`, exact-binding and `<1e-5` technical replay threshold.
5. Materialize terminal authority and follow only its encoded `next_stage`.
6. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%` until a later authority explicitly changes them.
