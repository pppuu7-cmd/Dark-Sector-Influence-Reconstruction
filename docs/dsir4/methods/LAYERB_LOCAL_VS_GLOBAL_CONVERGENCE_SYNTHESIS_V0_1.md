# Layer-B local-vs-global convergence synthesis v0.1

Date: 2026-09-10. Scope: DSIR Article 3 numerical-method interpretation. Frozen while Exp073JL attempt 2 remains in progress; no JL numerical output used.

## Existing validated evidence
The historical native-grid Exp073IR maximum was `0.9998247463807295`, motivating targeted diagnostics at its historically worst original-pair probes.

Exp073JF (`SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`) showed for the targeted original probes that shared-grid native-kpd10-vs-kpd20 differences were exactly zero at N=384 and N=512. At N=512, relative errors to the exact-k reference were approximately:
- alpha-left: `0.00010245604306152275`;
- beta-symmetric: `0.026575285704422986` for the then-used linear bracket interpolation.

Exp073JG then compared local interpolation curvature choices at the same targeted diagnostic setting. With the centered-cubic ln(k) rule subsequently adopted by the guarded shared-grid architecture, its relative errors to exact-k were:
- alpha-left: `1.2105247820888992e-07`;
- beta-symmetric: `0.00016088505716613062`.
Both are strictly below the frozen `REL_TOL=1e-3`. Native-kpd10-vs-kpd20 difference was zero for every tested local interpolation candidate.

By contrast, the later full inherited-support convergence gates using centered-cubic interpolation produced:
- Exp073JJ, base N=512 vs N=1024: global maximum relative component difference `0.037280144773915974`;
- Exp073JK, base N=1024 vs N=2048: global maximum `0.016330535730270664`.

## New synthesis
The full-support non-convergence in JJ/JK cannot be explained simply by persistence of the two historically worst Exp073IR original-pair probe errors. Under the adopted centered-cubic shared-grid rule, those targeted probes were already locally below `1e-3` at the JG diagnostic resolution, while the later global maximum over the full inherited support remained orders of magnitude larger.

Therefore at least one of the following must hold for the JJ/JK full-support maximum:
1. the maximizing atom lies elsewhere in the 107-row inherited support;
2. the maximizing atom changes with refinement (argmax migration);
3. a different response scale/near-zero component dominates the max-relative statistic;
4. a full-support derived-response numerical regime exists that was not represented by the historical two-probe diagnostic.

This materially strengthens the rationale for recording exact argmax metadata in any activated post-JL refinement. It also weakens a simplistic narrative that the current residual is merely the old native-grid worst pair converging slowly.

## Interpretation boundary
This is a synthesis of already validated support-only authorities. It does not alter any gate, threshold, interpolation rule, atom inclusion, physical domain, finite-difference step, row accounting, covariance authorization or Wm_S3 state. Exp073IR remains numerically unresolved historically; JF/JG do not retroactively pass it. Exp073JJ/JK remain valid NOT_CONVERGED support-only results.
