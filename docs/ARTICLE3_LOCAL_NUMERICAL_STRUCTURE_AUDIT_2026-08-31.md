# Article-3 local numerical structure audit — 2026-08-31

**Project:** DSIR only.  
**Classification:** `NONCLASSIFYING_NUMERICAL_STRUCTURE_DIAGNOSTIC`.  
**Authority:** false.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.  

This note records numerical work performed outside the hosted classifying chain while Exp073BJ is active. It may not change any frozen Exp073AQ/Exp073BJ PASS/FAIL rule and may not be used to rescue a failed exact comparator.

## 1. Structural identity

For the frozen 39-band expansion matrix `Q`, the low-memory finalizer is

`K = A Q`,

`W = solve(K, A)`.

Therefore, in exact arithmetic and whenever `K` is nonsingular,

`W Q = I_39`.

This gives a useful nonclassifying numerical-health invariant. It is independent of downstream support/covariance/nuisance/G8 information.

A generic diagnostic implementation is frozen in:

`ci/article3_window_structure_diagnostic_v0_1.py`

The diagnostic reports `WQ-I`, optional `K` singular values/condition number, and `KW-A` reconstruction residual. It defines no PASS/FAIL threshold.

## 2. Historical Exp073AQ Wm_S1 authority artifacts — diagnostic only

Source authority remains the permanent hosted FAIL from run `33327372191`:

- replica A artifact `9739721339`, selected-window SHA256 `979c61faea99cf60146078ccdd5a9c75547dcc5a689ee48c4c5f309cf6a10b69`;
- replica B artifact `9739045909`, selected-window SHA256 `5b02a691607dd21ede7601f081767ac3713e300abd5a9e358e4593a6ec486225`.

Local diagnostic on the immutable `<f8 [39,12288]` selected windows:

- A: `max(abs(WQ-I)) = 6.816769371198461e-14`;
- B: `max(abs(WQ-I)) = 6.816769371198461e-14`;
- A: Frobenius `||WQ-I|| = 8.585510963074038e-14`;
- B: Frobenius `||WQ-I|| = 8.595121614472007e-14`;
- maximum absolute difference between the two `WQ-I` residual matrices: `5.551115123125783e-16`;
- Frobenius difference between the two residual matrices: `1.4479371223796423e-15`.

The already-frozen AQ window mismatch remains:

- `array_equal = false`;
- maximum absolute window difference `2.0816681711721685e-17`;
- mean absolute window difference `2.5248672723363528e-20`.

Additional local relative row-difference diagnostics:

- rowwise L1 relative difference min `1.4418241028863924e-16`;
- median `2.376678224927234e-16`;
- max `5.083524651408262e-16`.

Interpretation: AQ remains a permanent exact-repeatability scientific FAIL. However, both failed replicas preserve the band-expansion identity to nearly the same floating-point residual. This provides no evidence for a gross band-normalization/finalizer-structure failure and is consistent with the existing diagnosis of extremely small environment-sensitive floating-point nondeterminism. It does not establish causality and does not rescue AQ.

## 3. Exp073BD provisional Wm_S2 branch-B artifact — conditioning diagnostic only

Source is the terminal Track-P/provisional run `33342265114`, branch-B artifact `9746250767`, which remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and is not Track-A authority.

Locally verified artifact payloads:

- compact `A` SHA256 `a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`, shape `[39,12288]`;
- final `W` SHA256 `63199de7f8cbf8662866d1262f5068a0852cb938fd31034b3fc11fe21e518186`, shape `[39,12288]`.

Using the same frozen fixed-order band summation as the low-memory implementation:

- `sigma_max(K) = 0.0366106399822293`;
- `sigma_min(K) = 0.01669516419847395`;
- `cond_2(K) = 2.1928888836909883`;
- `max(abs(WQ-I)) = 9.992007221626409e-16`;
- Frobenius `||WQ-I|| = 2.463427596999841e-15`;
- relative Frobenius reconstruction `||KW-A||/||A|| = 3.2380349152387473e-16`;
- max reconstruction error relative to `max(abs(A)) = 8.505999430164826e-16`;
- minimum final-window absolute row norm `1.0086619965901689`;
- maximum final-window absolute row norm `1.229326851436743`.

Interpretation: for this real DES-derived provisional Wm_S2 payload, the 39x39 finalizer system is very well conditioned. The final solve is therefore not a plausible explanation for the multi-hour full-scale execution bottleneck seen in BA/BH. The dominant expensive stage remains construction of the full general-coupling matrix before deterministic compression.

This conclusion is diagnostic and task-specific; Wm_S1 `K` must still be measured from a valid compact artifact when one exists.

## 4. Synthetic conditioning stress test on local compute

A deterministic synthetic family was constructed with exact `WQ=I` and prescribed `cond_2(K)` while preserving the frozen `[39,12288]` geometry. Re-running the same `K=AQ`, `W=solve(K,A)` structure showed the expected conditioning amplification:

| target cond(K) | observed max abs(WQ-I) |
|---:|---:|
| `1` | `5.326143e-16` |
| `1e2` | `5.354875e-15` |
| `1e4` | `3.037726e-13` |
| `1e6` | `3.606570e-11` |
| `1e8` | `3.731592e-09` |
| `1e10` | `1.677183e-07` |
| `1e12` | `2.432915e-05` |
| `1e14` | `1.061369e-03` |

This demonstrates why exact repeatability alone is not a complete numerical-health statement: two replicas could in principle be exactly identical while solving a badly conditioned system. Therefore `cond_2(K)`, `WQ-I`, and `KW-A` are useful post-authority diagnostics.

No threshold is introduced retroactively for Exp073BJ. Any future use as a classifying criterion requires a separate prospective preregistration.

## 5. Current implication for Exp073BJ

Exp073BJ run `33379013167` is still active. Both compact replicas have already passed:

- prospective freeze enforcement;
- exact NaMaster 2.7 environment installation;
- immutable BI_Q1 artifact download;
- immutable Exp073AZ PCL authority download;
- exact BI execution and AZ PCL binding.

Both are currently inside `Compute two-thread compact Wm_S1 replica`.

Do not start a duplicate heavy run. When a valid compact Wm_S1 artifact exists, run this diagnostic only after preserving the frozen BJ exact comparator semantics. The diagnostic is supplementary and must not influence the already-frozen BJ classification.

## 6. Scientific accounting

- Exp073AQ remains permanent exact-repeatability FAIL.
- Exp073BD remains provisional/incomplete and non-authority.
- this local audit is `+0/+0`.
- Article-3 verified readiness remains `52.0%`.
- Article-3 draft/data readiness remains `53.7%`.
- Layer A/B remain OPEN.
- covariance/whitening remains unauthorized.
- G7/G8/G9 remain OPEN.
- no G8 jump is permitted.
