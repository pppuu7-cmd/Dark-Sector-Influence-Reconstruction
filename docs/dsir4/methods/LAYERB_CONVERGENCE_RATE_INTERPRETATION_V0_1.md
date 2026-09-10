# Layer-B convergence-rate interpretation v0.1

Date: 2026-09-10. Scope: DSIR Article 3 numerical methodology. Response-blind with respect to Exp073JL.

## Motivation
Validated shared-grid convergence maxima are currently known for Exp073JJ (base 512->1024: `0.037280144773915974`) and Exp073JK (base 1024->2048: `0.016330535730270664`). Their ratio is about 2.28285, which corresponds to an interpretation-level empirical order near 1.19 under approximately halved ln(k) spacing. This empirical order MUST NOT be identified automatically with the formal interpolation order of the centered four-node Lagrange rule.

## Local interpolation versus derived response
For a smooth transfer quantity `y(theta,x)` with `x=ln(k)`, a four-node cubic interpolant on a regular local x lattice has a local interpolation remainder proportional to a product of four node offsets and therefore nominally scales as `Delta x^4` when the same smooth regime and comparable target phase are followed under refinement.

The Layer-B quantities are not direct interpolants. They are finite-difference parameter responses built from separately solved/interpolated transfer tables:
- alpha-left: `abs((y(-h)-y(0))/(-h))`;
- beta-symmetric: `abs((y(+h)-y(-h))/(2h))`;
with frozen `h=1e-4`.

If interpolation error is a smooth function of the model parameter, its correlated part also differences and can retain high-order grid scaling. Solver/roundoff/interpolation residuals that are not correlated between neighboring parameter models can instead be amplified by the finite-difference subtraction and division by `h`. This is a diagnostic hypothesis only; it cannot justify changing h or the estimator.

## Why the global maximum can show a lower apparent order
The frozen convergence statistic is atomwise
`abs(R_coarse-R_fine)/max(abs(R_coarse),abs(R_fine))`
and the reported gate statistic is the maximum over every positive finite response component in the inherited support.

Consequently the empirical order of the global maximum can differ substantially from local cubic truncation order for at least three non-exclusive reasons:
1. **small-response denominator:** a small absolute response can turn a modest absolute numerical difference into the largest relative difference;
2. **argmax switching:** different atoms can attain the global maximum at successive resolutions, so ratios of global maxima need not follow the local asymptotic series of any single atom;
3. **derived-response cancellation/noise:** finite-difference subtraction can expose residual numerical components that do not scale like the smooth interpolation remainder over the tested range.

Absolute value at the response level can further make behavior non-smooth near a response zero. None of these mechanisms licenses denominator flooring, atom removal, clipping, averaging, tolerance weakening, h changes or estimator substitution.

## Pre-frozen discriminating diagnostic
The already-frozen `LAYERB_CONVERGENCE_ARGMAX_DIAGNOSTIC_STANDARD_V0_1` is sufficient to discriminate these explanations in a future activated refinement without changing the gate. It records the exact unchanged relative-error argmax, its absolute denominator and response values, whether it also maximizes absolute error, and denominator quantiles/counts.

Interpretation after such a run:
- very small argmax denominator with ordinary absolute error supports a near-zero-response explanation;
- changing argmax `(block,component,z,k)` across refinements supports maximum-switching;
- stable argmax with ordinary denominator but slow reduction points toward non-asymptotic derived-response/solver behavior and motivates a separate prospective numerical-method audit rather than tolerance rescue.

## Boundary
This note is explanatory and support-only. It does not modify Exp073IR/JJ/JK/JL/JM/JN, their classifications, any threshold, interpolation rule, finite-difference step, masks, domain, row accounting, covariance authorization or Wm_S3 state.
