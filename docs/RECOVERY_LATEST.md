# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention/reproducibility threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; full 107-row Layer-B remains closed.

## Closed runtime-mechanism chain through V0.22

V0.18R/V0.19 were false-invalid because raw non-dispatch NumPy AVX-512 capability bits were used as the validation target. V0.19D diagnosed the error; V0.20 response-free validated the correct runtime-dispatch semantics; V0.21 causally established NumPy AVX-512 dispatch as the branch mechanism.

V0.22 terminal authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, creation commit `2b3cb46863fb85e6456a5a11e30183acf3b6de10`.
Run `34875798025`, decision job `104089235776`, decision artifact `10360469338`, digest `sha256:12769549f5d44da9dc01ee82d426dd07e171cefe27282e92e40df15b43ea2ba0`.
Classification `FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED`, effect `+0/+0`.
All 32 lanes were eligible; native classes 10 active / 22 inactive. Cross-host spread on both frozen replay-failure witness cells and anchor was `0.0`; native-class mean separation on both failure cells was `0.0`; forced responses exactly matched the frozen alternate branch. This is a numerical reproducibility repair, not dark-sector evidence.

V0.22 authorizes exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT`.

## V0.23 — active production-h replay revalidation

Preregistration `prereg/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.md`, commit `24b09db3069acbe875459f7ad6f2d2aea9f25830`.
Executor `ci/layerb_beta_forced_baseline_production_h_replay_revalidation_v0_23.py`, pre-freeze hardening commit `c96e80a0e075bd21b41351aa158ef997f0cc05cd`, blob `aa6c3aa298fc12aa65f4de2919ba9cc3f39a7fbe`.
Contract `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.json`, commit `d5d5665671fbfedaaf77022b0f7164ada90d49ee`.
Workflow `.github/workflows/layerb-beta-forced-baseline-production-h-replay-revalidation-v0-23.yml`, commit `a7ce06dc9cef76c934d5b5c2c289a0729aa64e04`.
Launch/head `ad5472244fdcffa05ecfd3826ac9c83db06f32ef`.
Authoritative run `34878651714`; exactly one run exists.

Invariant job `104092079570` is terminal `success`; invariant artifact `10361618142`, digest `sha256:d8bc4761cd1c2b4a3031e6c7fdbd1f4acbf12323cce14d5d96067b25f92f1228`. The first completed substantive lane observed was `R11`, terminal `success`, artifact `10362073981`; its contents were deliberately not inspected before the decision barrier. Multiple additional lanes are in progress and the remaining matrix is queued; no failure/cancellation has been observed.

Outcome-blind workflow audit found that `replay-lane` lacks an explicit YAML `needs: invariant-audit` dependency. This is a workflow-hardening omission, not a defect in the frozen classifier. In the actual authoritative run the invariant completed successfully before the first replay lane started substantive execution, so the current run is not invalidated. Do not rerun V0.23 for this omission. Add an explicit invariant-to-lane DAG barrier in the next workflow generated after V0.23 terminal classification.

Frozen V0.23 object: complete V0.12 production-h pure-grid replay subset = five frozen grids × three frozen targets = 15 cells at `h=1e-4`. The exact V0.20 NumPy mask must be validated response-free before substantive computation. Raw non-dispatch AVX-512 bits are forbidden as validation targets. No unmasked substantive response is allowed. Every eligible lane computes only the forced-baseline 15-cell object, with exactly 10 CLASS solver constructions.

Frozen power: eligible n>=6, including n>=3 native AVX512-active and n>=3 native AVX512-inactive. Supported requires every one of 15 cells to have cross-host max pairwise relative spread `<1e-5` and native-class mean separation `<1e-5`. Historical unforced response values are descriptive only and non-gating. The two original V0.13 production-h replay failures are fixed sub-controls; PASS still requires all 15 cells.

## Exact next order

1. Continue only run `34878651714`; do not create a duplicate.
2. Wait for all 32 lanes + the single decision barrier; invariant is already terminal success.
3. Do not inspect partial substantive V0.23 response values or completed lane artifact contents.
4. Verify the terminal decision artifact ID/digest and materialize V0.23 authority.
5. Follow only the encoded `next_stage`.
6. If supported, the only authorized successor is `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT`.
7. In the next generated workflow, add explicit `needs: invariant-audit` for substantive lanes as a hardening control.
8. Full Layer-B and all physical-science gates remain closed.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
