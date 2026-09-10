# Exp073JH static cubic-stencil boundary audit v0.1

Date: 2026-09-10. Scope: independent static audit while the already-frozen Exp073JH run is in progress. No partial numerical output was inspected and no Exp073JH acceptance criterion is changed.

## Frozen code inspected
`ci/exp073jh_article3_layerb_full_support_grid_invariant_feasibility_v0_1.py` defines `N=512`, `KMIN=1e-4`, `KMAX=0.06664762008318016`, common nodes `np.geomspace(KMIN,KMAX,N,dtype=float64)`, and centered-cubic target validity `(j>=2)&(j<=len(nodes)-2)` with `j=np.searchsorted(nodes,target)`.

For this exact frozen lattice:
- node[0] = `0.0001` Mpc^-1;
- node[1] = `0.00010128053746543492` Mpc^-1;
- node[510] = `0.065804962879393983` Mpc^-1;
- node[511] = `0.066647620083180162` Mpc^-1.

Therefore the centered-cubic response engine has a complete four-node stencil only for targets in the strict/interior interval approximately
`0.00010128053746543492 < k <= 0.065804962879393983 Mpc^-1`
under the exact `searchsorted` convention. The judged Exp073IR physical domain remains broader: `0 < k <= 0.06664762008318016 Mpc^-1`.

## Interpretation before any JH result
This is not evidence that any retained atom actually lies outside the cubic-stencil interval; that is exactly what the running full-support audit will determine through `unsupported_target_evaluations` and unchanged row accounting. It is only a source-level boundary-risk certificate.

If Exp073JH is terminally NOT_FEASIBLE solely or materially because otherwise-valid inherited atoms lack a complete stencil near either grid edge, the scientifically clean next architecture is **not** clipping, extrapolation, dropping atoms, changing the judged physical domain, changing REL_TOL, or switching the interpolation rule post hoc. A permissible next support-only experiment should instead prospectively add response-blind geometric guard nodes outside the judged physical interval while preserving every original N=512 JG/JH interior node and its logarithmic spacing. The judged atom masks and physical z/k domain must remain unchanged.

One deterministic candidate construction for a later preregistration is to extend the existing geometric lattice by the minimum whole number of same-ratio nodes below/above required to provide the full centered-cubic stencil for the minimum/maximum inherited target k. The required extension count must be derived solely from support geometry, before evaluating responses, with an explicit capacity bound and no tuning to numerical response values. Such a design would preserve the validated interior interpolation architecture while isolating boundary coverage as an infrastructure/evaluation-support question.

If JH is feasible without boundary failure, this conditional guard-node path is unnecessary and must not be launched.

This note creates no scientific authority, no covariance restriction, no Wm_S3 authority and no modification of the running Exp073JH contract.
