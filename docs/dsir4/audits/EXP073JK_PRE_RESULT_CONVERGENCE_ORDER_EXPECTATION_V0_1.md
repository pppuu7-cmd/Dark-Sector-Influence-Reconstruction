# Exp073JK pre-result convergence-order expectation v0.1

Date: 2026-09-10. Scope: DSIR Article 3 / numerical-method interpretation only.

Status: recorded while Exp073JK run 34495159732 / job 102931623100 was still IN_PROGRESS and before any Exp073JK response output was available. This note is +0/+0, does not preregister a later scientific gate, and cannot alter REL_TOL=1e-3 or any frozen DSIR boundary.

## Resolution spacings

For the exact geometric base grids on `[1e-4, 0.06664762008318016] Mpc^-1`, the uniform spacings in `x=ln(k)` are:

- N=512: 0.012724079121921797
- N=1024: 0.006355820558458058
- N=2048: 0.003176357807182428
- N=4096: 0.0015877910699152755

Hence the refinement ratios are approximately 2.001956947 for 512->1024 and 2.000977517 for 1024->2048.

## Method-order expectation

The frozen local interpolation is a four-node cubic Lagrange polynomial in `ln(k)`. For a sufficiently smooth response in the asymptotic regime, the interpolation remainder is nominally fourth order in local grid spacing. This is a method-level expectation only; finite-difference response construction, near-zero components, local non-smoothness or max-over-atoms selection can prevent the observed maximum relative component difference from following a pure fourth-order law.

The validated JJ maximum is 0.037280144773915974 for the 512->1024 comparison. Under an ideal fourth-order refinement law, the expected scale of the next 1024->2048 difference would be approximately:

`0.037280144773915974 / (2.001956947^4) = 0.0023209119033512373`.

This is still above the frozen REL_TOL=1e-3. To make the JK difference fall below 1e-3 in a single refinement step, the empirical convergence order corresponding to the prior JJ magnitude would need to exceed approximately 5.213 under the same simple scaling model.

Under the same ideal fourth-order model, one additional sequential 2048->4096 refinement would have an expected difference scale of approximately 1.4477e-4, below REL_TOL=1e-3.

## Governance consequence

These numbers are not a prediction of the Exp073JK outcome and must not be used to reinterpret it. They establish only that:

1. a valid JK NOT_CONVERGED result would be numerically plausible rather than surprising for a cubic interpolant;
2. if JK is NOT_CONVERGED, a further sequential refinement can be scientifically motivated without weakening the threshold or changing the estimator;
3. any such later gate still requires a separate prospective freeze after JK is terminal and must use adequate infrastructure capacity; and
4. if JK CONVERGES, its measured result governs and no later refinement is automatically required by this note.
