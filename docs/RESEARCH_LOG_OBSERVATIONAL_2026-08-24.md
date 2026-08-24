# DSIR observational-whitening research log — 2026-08-24

This addendum continues `docs/RESEARCH_LOG_COMPARISON_2026-08-24.md`. Scientific claim status remains controlled by `docs/GATES.md`.

## Experiment 034 — first DESI ShapeFit observation-space bridge

The comparison-ready six-family atlas was mapped into the corrected DESI DR1 ShapeFit `m+n` shape channel using a frozen finite-node ShapeFit-basis operator.

For each redshift row of the theory response,

\[
r_\Delta(k,z)=\ln[P_{\Delta,model}/P_{\Delta,ref}],
\]

we fit

\[
A+\frac{m}{0.6}\tanh\left[0.6\ln(k/0.03)\right]+n\ln(k/0.03)
\]

on the frozen five-node low-k grid and use `m+n` as the shape proxy. The synthetic exact-template control recovered the expected `m+n=0.17` with absolute error `8.326672684688674e-17`.

Because the current atlas does not yet provide family-complete predictions for the other ShapeFit coordinates, the full 4x4 covariance inverse was deliberately **not** used. The production whitening is the conservative marginal shape block

\[
Z_i=(m+n)_i/\sqrt{C_{ii}^{m+n,m+n}}
\]

for `LRG1, LRG2, LRG3, ELG2, QSO`. Conditional Schur-complement errors were computed only as a diagnostic; their ratios to marginal errors are `0.9126, 0.9136, 0.9472, 0.8694, 0.8906`.

Hard GitHub Actions run `32777716140` passed. Unit tests: `3 passed`. Status:

`PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`.

Artifact ID: `9538572755`; artifact ZIP SHA256:

`b1c6dc98d933e564d1c74ee549917621e5b4e2fbdc4e37d760bf80c2b13c4a38`.

### Main numerical findings

- GDM `cs2` vs `cv2`: raw shape-history acute angle `0.190257 deg`; marginally whitened acute angle `0.189582 deg`. The low-k shape-history degeneracy therefore survives this real-covariance weighting.
- GDM `cs2` vs designer f(R): raw acute angle `20.771942 deg`; whitened acute angle `22.995730 deg`, oriented angle `157.004270 deg`.
- GDM `cv2` vs designer f(R): raw acute angle `20.956124 deg`; whitened acute angle `23.178674 deg`, oriented angle `156.821326 deg`.
- smooth non-phantom wDE vs GDM `cs2`: raw acute angle `12.132482 deg`; whitened acute angle `12.795598 deg`.

The unit-direction singular ratios in this five-bin shape-only block are

`(1, 0.2055855, 0.0106523, 0.00194843, 1.37046e-6)`.

This spectrum is descriptive only. No intrinsic-rank threshold was frozen, no `R_model` value is assigned, and G5 remains PARTIAL.

### Important negative/limiting result

The finite-node ShapeFit template is an excellent/adequate local proxy for smooth-w and the IDE directions (median fit residuals about `0.6%`, `5.5%`, and `3.4%` respectively), but it leaves roughly `36%` relative L2 residual for GDM `cs2`, GDM `cv2`, and designer f(R) across the full frozen `0.001-0.1 h/Mpc` range.

Therefore the approximately `23 deg` whitened GDM/f(R) shape-history angle is **not** promoted to a DESI distinguishability claim. The large template residual is retained as a methodological warning: strongly scale-dependent responses require a survey/window-aware projection or a richer measured-shape operator.

## Gate consequences

- G5: remains **PARTIAL**. A real covariance has now entered the cross-family comparison, but only in one proxy shape block.
- G7: remains **OPEN**. No residual-law search is resumed.
- G8: remains **OPEN**. No discovery claim.
- The hard discriminant-graph conclusion is unchanged: metric slip, small-scale transfer, and time/sign evolution remain the established theory-level separator set for the currently frozen graph.

## Immediate continuation after Experiment 034

1. Build a family-complete geometry operator for `DH/DM` / AP on the same DESI redshift support.
2. Build a family-complete `f_sigma_s8` growth operator using gauge-safe total-matter growth from the validated solver lineages.
3. Replace the finite-node shape proxy with a survey/window-aware ShapeFit response map, or explicitly quantify and propagate compression-model error.
4. Only after 1–3, form the full corrected ShapeFit block `Z=C^{-1/2} Delta O` and recompute pairwise geometry.
5. Then stress-test the data-whitened Jacobian/global spectrum under family priors, channel removal, solver precision, and within-family sampling.
6. In parallel, construct an observational metric-slip/lensing block because the discriminant graph identifies it as the highest-value separator for the GDM `cs2/cv2` degeneracy.
