# DSIR recovery checkpoint — local numerical structure audit while Exp073BJ computes

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Classification:** nonclassifying numerical audit, `+0/+0`.

## Hosted Track-A state

Exp073BJ run `33379013167` remains active. Jobs:

- compact A `99446854065`;
- compact B `99446854363`.

Both have passed prospective freeze, NaMaster 2.7 setup, BI_Q1 authority binding and Exp073AZ canonical PCL binding and are inside `Compute two-thread compact Wm_S1 replica`.

Do not duplicate this heavy run.

## Local compute result 1 — structural identity

For the frozen low-memory finalizer:

`K=AQ`, `W=solve(K,A)`, hence exact arithmetic gives `WQ=I_39` whenever K is nonsingular.

New reusable diagnostic committed as:

`ci/article3_window_structure_diagnostic_v0_1.py`

commit `6163c15cb7390d27864a682e405506e14fbf0425`.

It is explicitly nonclassifying and introduces no threshold.

## Local compute result 2 — historical Exp073AQ Wm_S1 windows

Immutable hosted FAIL artifacts inspected locally only after their authority result:

- A artifact `9739721339`, SHA `979c61faea99cf60146078ccdd5a9c75547dcc5a689ee48c4c5f309cf6a10b69`;
- B artifact `9739045909`, SHA `5b02a691607dd21ede7601f081767ac3713e300abd5a9e358e4593a6ec486225`.

Results:

- A `max(abs(WQ-I)) = 6.816769371198461e-14`;
- B `max(abs(WQ-I)) = 6.816769371198461e-14`;
- difference between the two residual matrices: max `5.551115123125783e-16`;
- rowwise L1 relative A/B difference: min `1.4418241028863924e-16`, median `2.376678224927234e-16`, max `5.083524651408262e-16`.

AQ remains permanently `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`. These diagnostics do not rescue it. They show that the two failed windows retain nearly identical band-normalization structure despite their exact byte mismatch, so there is no evidence here for a gross finalizer/band-expansion error.

## Local compute result 3 — real DES-derived provisional Wm_S2 conditioning

Track-P Exp073BD run `33342265114`, branch-B artifact `9746250767` inspected locally. It remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and cannot be upgraded to authority.

Verified payloads:

- compact A SHA `a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`;
- final W SHA `63199de7f8cbf8662866d1262f5068a0852cb938fd31034b3fc11fe21e518186`.

Frozen fixed-order reconstruction gives:

- `sigma_max(K)=0.0366106399822293`;
- `sigma_min(K)=0.01669516419847395`;
- `cond_2(K)=2.1928888836909883`;
- `max(abs(WQ-I))=9.992007221626409e-16`;
- `||KW-A||/||A||=3.2380349152387473e-16`;
- min absolute row norm `1.0086619965901689`.

This real DES-derived provisional task has a very well conditioned 39x39 finalizer. Therefore the observed multi-hour BA/BH bottleneck is not plausibly the small `solve(K,A)` step for this task; it remains concentrated in creation of the full general-coupling matrix before deterministic compression.

Wm_S1 conditioning remains unknown until a valid compact Wm_S1 artifact exists.

## Local compute result 4 — conditioning stress test

Synthetic frozen-shape `[39,12288]` systems with exact structural `WQ=I` were generated locally. Observed `max(abs(WQ-I))` after recomputing `W=solve(AQ,A)`:

- cond 1 -> `5.326143e-16`;
- cond 1e2 -> `5.354875e-15`;
- cond 1e4 -> `3.037726e-13`;
- cond 1e6 -> `3.606570e-11`;
- cond 1e8 -> `3.731592e-09`;
- cond 1e10 -> `1.677183e-07`;
- cond 1e12 -> `2.432915e-05`;
- cond 1e14 -> `1.061369e-03`.

This demonstrates that exact replica equality alone is not a complete numerical-health statement. A future classifying conditioning criterion, if ever desired, must be preregistered prospectively. It cannot be added to BJ after trigger.

Full note:

`docs/ARTICLE3_LOCAL_NUMERICAL_STRUCTURE_AUDIT_2026-08-31.md`

commit `19be06f8ded2206c420589feadb33b48f58c156e`.

## Accounting

`Verified: 52.0% | Draft/data: 53.7%`

No readiness change. Layer A/B, covariance/whitening, G7/G8/G9 remain unauthorized. Exp073AQ remains permanent FAIL. No G8 jump.

## Exact next action

Keep Exp073BJ as the sole heavy Track-A control plane. When compact artifacts appear, preserve the frozen exact comparator classification first. Then the nonclassifying structure diagnostic may measure Wm_S1 K conditioning and structural residuals without influencing BJ PASS/FAIL.
