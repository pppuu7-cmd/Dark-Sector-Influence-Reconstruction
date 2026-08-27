# Recovery checkpoint — Exp073J KiDS-BNT component / Exp073K

**Date:** 2026-08-27

## Current verified state

1. `main` implementation parent for the KiDS-BNT component is `55a9fa869e79a0aac11c54aac0115ff281352f24`.
2. Exp073J full common-support criteria remain unchanged: physical rectangle `0.295<=z<=2.33`, `0.000704833374744468<=k<=0.06664762008318016 Mpc^-1`, positive invalid fraction `<=0.05`, final minimum retained dimension `15`.
3. BOSS finite-matrix component remains a completed **non-classifying** result: `54/240` rows retained, run `33042052616`. Do not reinterpret it as a full Exp073J PASS.
4. KiDS-BNT component run `33045812989` completed as infrastructure success but its prospectively frozen numerical trust controls classified the component as `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`.
5. Immutable KiDS artifact: `9635628042`, digest `sha256:907ac6130afb2292eac6e8cdd03493bb0f3b4507d5042e1ac15c282bbb901d3b`, extracted JSON SHA256 `7edbbc6d842ddfee63e59bcdf71f5cb1074fdf9a50ec0656ffd4c522a10b2a35`.
6. K1-K5 and K8-K10 passed. K6 angular normalization/tail and K7 support-fraction convergence failed.
7. The failure is dominated by huge positive high-ell tails: approximately 0.64--0.71 of the finite `ell<=60000` positive normalization lies above `ell=30000`. Coarse/fine integration below 30000 agrees around 1e-5, so the problem is not ordinary quadrature resolution.
8. Finite-cutoff retained counts `0/24 Wm` and `0/48 WW` are **not scientific support classifications**, because K6/K7 fail first.
9. Full Exp073J scientific classification is not authorized. Covariance restriction/whitening is not authorized.

## Mechanism hypothesis frozen for next step

For the released estimator, direct response to `C_ell` is a finite sum over 326 discrete theta nodes with an external factor `ell`. Since fixed-argument-node Bessel asymptotics are `J_n(ell theta)=O(ell^-1/2)` oscillatory, an uncancelled absolute envelope scales as `sqrt(ell)`, giving cumulative positive normalization `N(L)=O(L^(3/2))`.

The predicted dyadic shell fraction is

`1-2^(-3/2)=0.6464466094067263`,

numerically close to the observed 30k→60k tails. This is not yet promoted to a scientific/mechanism classification.

## Next admissible experiment

Exp073K is prospectively frozen in `experiments/073k_kids_finite_theta_absolute_response_normalizability_prereg_v0_1.md` **before** any new high-ell ladder output.

Execute the exact frozen dyadic ladder `[7500,15000,30000,60000,120000]`, primary `Delta ell=1`, and required secondary half-step checks. Classify only by the preregistered Exp073K boxes.

Do not:

- change the 5% Exp073J threshold;
- select an ell cutoff after seeing the tail;
- multiply the positive support measure by fiducial `C_ell` or `P(k)`;
- use oscillatory sign cancellation to define positive support;
- read covariance, nuisance rank/SVD, relation/null results or G8 outputs.

## Gate state

- G7: OPEN
- G8: OPEN
- G9: OPEN

The next allowed work remains inside physical-support/operator validation. No covariance step is yet authorized.
