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

## Experiment 035 — calibration-free AP / DH-over-DM observation operator

The next observation-space layer was derived from the exact flat-FLRW identity

\[
F_{AP}(z)=\frac{D_M}{D_H}=E(z)\int_0^z \frac{dz'}{E(z')}.
\]

Writing

\[
E_{model}(z)=A E_{ref}(z)e^{r_E(z)}
\]

with arbitrary constant calibration `A` gives

\[
\frac{F_{AP,model}}{F_{AP,ref}}
=e^{r_E(z)}
\frac{\int_0^z e^{-r_E(z')}dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}.
\]

Thus the constant calibration mode cancels exactly. In particular, anchoring the DSIR expansion response at `z*=0.51` removes only an irrelevant additive constant and retains all AP information. The ShapeFit geometry coordinate follows exactly from

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

The first-order operator is

\[
\Delta\ln F_{AP}(z)=r_E(z)-
\frac{\int_0^z r_E(z')dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}+O(r_E^2).
\]

Hard thresholds were frozen before the first run: direct wCDM bridge `<1e-11`, additive-calibration invariance `<1e-12`, `DH/DM` sign identity `<1e-14`, and quadratic-remainder halving ratio `<0.27`.

### Provenance of the first failed attempt

Run `32778406204` stopped before the hard script because a unit-level assertion demanded a cumulative-integration residual `<2e-15`; the observed floating-point residual was `2.6367796834847468e-15`. This was a few-ulp numerical tolerance issue, not a scientific failure. The unit-only threshold was changed to `1e-14`; **none of the pre-frozen hard scientific thresholds changed**.

### Successful hard run

Run `32778635058` passed; regression suite run `32778634861` also passed. Experiment status:

`PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1`.

Numerical controls:

- direct wCDM `ln F_AP` bridge error: `1.0047518372857667e-14`;
- additive calibration-mode error: `7.829674408821319e-15`;
- `DH/DM = 1/F_AP` sign-identity error: exactly `0` at reported precision;
- exact-minus-linear remainders at amplitudes `1e-3` and `5e-4`: `3.975002712972237e-09` and `9.93737139288759e-10`;
- halving ratio: `0.24999659397608562`, consistent with the expected quadratic remainder.

Artifact ID `9538896209`; artifact ZIP SHA256:

`f4a70ff9c67bdf45b520f7a2babaf63280fde6b841c45539a9c6fc22e3479d9f`.

A synthetic `w=-0.93` control gives `Delta ln(DH/DM)` at `z=(0.51,0.71,0.92,1.32,1.49)` equal to

`(-0.00642012,-0.00536682,-0.00366556,-0.000285506,+0.000970297)`.

These values are a method control only, not a fit to DESI and not the production C1 tangent.

### New hard input requirement discovered

The AP operator contains an integral from `z=0` to the measurement redshift. The current seven-node structure atlas begins at `z=0.295`; extrapolating those nodes to zero would inject an uncontrolled geometry response. Therefore a production family comparison must supply validated background `H(z)` response histories covering `z=0` through all target bins.

The existing C1 smooth-w and C2 interacting-vacuum solver workflows already write full `background.dat` tables into their artifacts. The next experiment will extract/re-run these full histories with the exact production baselines rather than infer the missing `0<z<0.295` interval from the structure atlas.

## Gate consequences after Experiments 034–035

- G5 remains **PARTIAL**. We now have one real-covariance shape proxy and a hard-validated exact AP observation operator, but not yet a family-complete joint geometry/growth/shape response matrix.
- G7 remains **OPEN**. No residual-law search is resumed.
- G8 remains **OPEN**. No discovery claim.
- The hard discriminant-graph conclusion remains unchanged: metric slip, small-scale transfer, and time/sign evolution are the established theory-level separator set for the currently frozen graph.

## Immediate continuation

1. Extract or regenerate validated full `z=0..2.33` background histories for C1 smooth-w and C2 IDE on the same solver baselines used for their local tangents/cone.
2. Prove and encode exact/background-equivalent zero AP responses for perturbation-only directions only where the model definition justifies them; never use zero as missing-data imputation.
3. Map those histories through the Experiment 035 operator into the DESI `DH/DM` geometry block and apply its covariance consistently.
4. Build a family-complete gauge-safe `f_sigma_s8` growth operator.
5. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware shape response or propagate compression-model error.
6. Only after these pieces exist, form the full corrected ShapeFit block `Z=C^{-1/2} Delta O`, freeze rank/null thresholds, and stress-test family priors and solver precision.
7. In parallel construct observational lensing/slip and small-scale-transfer blocks, because those are the highest-value hard separators for GDM `cs2/cv2` and WDM respectively.
