# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention/reproducibility threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; full 107-row Layer-B remains closed.

## Closed runtime/replay chain through V0.23

V0.18R/V0.19 false-invalid outcomes came from the wrong NumPy validation observable. V0.19D diagnosed raw non-dispatch AVX-512 capability bits as the wrong target. V0.20 response-free validated the actual NumPy dispatch mask; V0.21 causally localized the hosted branch to NumPy AVX-512 runtime dispatch; V0.22 showed the forced non-AVX512 NumPy baseline collapses the witness cross-host split to zero spread.

V0.23 terminal authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.json`, creation commit `2aa8ff62a47c1aa367f102032bdb7b2267a9fa94`.
Run `34878651714` terminal `success`; invariant job `104092079570`; invariant artifact `10361618142`, digest `sha256:d8bc4761cd1c2b4a3031e6c7fdbd1f4acbf12323cce14d5d96067b25f92f1228`; decision job `104107495389`; decision artifact `10364150389`, digest `sha256:f787799c177bba95e0630206108a1448169b6e76b17a36b20f4439f7b58a17cd`.
Classification `FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_REVALIDATED`, effect `+0/+0`.

All 32 candidate lanes were eligible. Native dispatch classes: 12 active / 20 inactive. The complete frozen V0.12 production-h pure-common-grid replay subset — `GRID512,640,768,896,1024` × the three frozen V0.12 targets = 15 cells at `h=1e-4` — is cross-host reproducible under the validated forced NumPy baseline. Every one of the 15 cells has cross-host maximum pairwise relative spread `0.0` and native-class mean relative separation `0.0`. Both original V0.13 production-h replay failures are repaired. Maximum exact requested-node mismatch is `1.6564666256119906e-16`; binary/software control key counts are both one. No forbidden downstream object was touched.

This closes the original **production-h hosted replay reproducibility blocker** for the exact frozen 15-cell object. It does not itself re-establish the full V0.12 interpolation-mechanism classification, because V0.12 also contains the `h=2e-4` replay/object and mixed/exact/direct mechanism comparisons. It does not validate full Layer-B or authorize physical inference.

## Workflow hardening carried forward

V0.23 `replay-lane` lacked an explicit YAML `needs: invariant-audit`. Outcome-blind audit found this before terminal result; in the actual run invariant completed successfully before the first substantive lane began, so V0.23 remains valid. Every successor substantive workflow must include an explicit invariant-to-substantive DAG edge.

## Authorized next stage

V0.23 authorizes exactly:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT`.

## Exact next order

1. Prospectively freeze the forced-baseline production-h common-grid interpolation reassessment before any substantive execution.
2. Preserve the V0.12 production-h interpolation object, identities and scientific/replay thresholds needed for the reassessment; do not retune parent violation cells or targets.
3. Force the exact V0.20 NumPy non-AVX512 mask before NumPy/classy import and validate the active dispatch response-free.
4. Add explicit `needs: invariant-audit` on every substantive lane.
5. Keep historical unforced numerical branches descriptive/non-gating wherever branch identity is ambiguous; comparisons used as PASS/FAIL must be generated under a common controlled baseline or be otherwise prospectively justified.
6. Do not open full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 or any physical-science gate.
7. Follow only the terminal reassessment `next_stage`.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
