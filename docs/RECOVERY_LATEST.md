# DSIR RECOVERY LATEST — observational-whitening live overlay

**Date:** 2026-08-24  
**Read first:** `docs/RECOVERY_MANUAL.md`  
Then read this file, `docs/GATES.md`, `docs/STATUS.md`, `docs/RESEARCH_LOG_COMPARISON_2026-08-24.md`, `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-24.md`, `docs/PROVENANCE.md`, `docs/DISCRIMINANT_GRAPH.md`, and the response-basis specifications.

Hard boundary: **DSIR is separate from RTK. Do not modify, use, overwrite, or merge the RTK repository/project while continuing DSIR.**

---

## 1. Current scientific state

DSIR is a reconstruction/meta-inference framework, **not a fundamental theory**, and no new law of nature is claimed.

Current gates:

- **G1 PASS v0.1.1:** conservation/gauge contract and comoving total-matter response validated.
- **G2 PASS v0.1.1:** same-solver `r_Delta` basis and cross-solver smooth-w bridge validated.
- **G3A PASS v0.1:** six control families embedded at background level.
- **G3B PASS v0.1 block-aware:** six-family beyond-background atlas comparison-ready.
- **G4 PASS:** synthetic low-rank recovery.
- **G5 PARTIAL:** synthetic robustness protections pass; Experiment 034 adds first real-covariance shape whitening; Experiment 035 adds a hard-validated exact AP observation operator. Family-complete joint observation kernels/rank stress tests remain.
- **G6A/G6B PASS:** DESI DR2 AP and corrected DESI DR1 ShapeFit real-data layers.
- **G7 OPEN:** no residual-law claim before family-complete observation kernels and data-whitened rank/manifold stability.
- **G8 OPEN:** no discovery before a withheld physical prediction.

Hard chronology:

- Exp.030 comparison readiness run `32772758188`: PASS, `failures=[]`.
- Exp.031 first raw-theory cross-family comparison: complete.
- Exp.032 GDM slip discriminator: hard PASS.
- Exp.033 discriminant graph run `32775055341`: hard PASS.
- Exp.034 ShapeFit `m+n` marginal real-covariance proxy run `32777716140`: `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`.
- Exp.035 AP operator run `32778635058`: `PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1`.

---

## 2. Frozen response basis v0.1.1

Structure redshift nodes:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

Low-k nodes:

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Background response:

\[
r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right],\qquad z_*=0.51.
\]

Total-matter comoving contrast:

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},\qquad
\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}.
\]

Production perturbation response:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_{\Delta,model}^{S}(k,z)}{P_{\Delta,ref}^{S}(k,z)}}.
\]

`S` must be the same solver lineage with matched numerical settings for model/reference whenever possible. Cross-solver smooth-w response bridge mismatch is `2.3747404043e-10 < 1e-9`.

Never identify a global SVD span with microscopic dimension. For a smooth manifold use the local Jacobian `J_ai=partial r_a/partial theta_i`; use a tangent cone when viability truncates parameter space.

---

## 3. Validated family atlas

- **C0 LambdaCDM/GR:** common response origin.
- **C1 smooth non-phantom DE:** one-sided `epsilon_w=1+w -> 0+` ray; smallest resolved step `1e-4`.
- **C2 interacting vacuum:** `Q=H(alpha rho_idm + beta rho_iv)`; `alpha>0` invalid under full-history `rho_iv>=0`; use negative-alpha ray plus central beta line. Structure angle `58.9338 deg`, background angle `10.8306 deg`.
- **C3 GDM:** pinned GDM_CLASS; zero-limit PASS. `cs2/cv2` low-k P angle `0.322616 deg`, local two-axis `sigma2/sigma1=2.572e-3`.
- **C4 thermal WDM:** separate small-scale block; 3 keV control `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375`.
- **C5 designer f(R):** official H-EFTCAMB; MG-S0/MG-S1 PASS; production `B0={1e-6,1e-5,1e-4,1e-3}`.

Undefined theory/channel cells remain masked, never zero-imputed.

---

## 4. Raw-theory comparison and hard discriminants

The six nonzero low-k response objects are C1 smooth-w, C2 negative-alpha, C2 beta, C3 cs2, C3 cv2, C5 designer-f(R). C0 is the origin; C4 is a separate small-scale block.

Raw normalized six-direction singular ratios:

`(1,0.52046,0.26140,0.20087,0.08299,5.9178e-4)`.

**Do not call this `R_model=5`.** No intrinsic-rank threshold was frozen.

Hard theory-level separators:

- GDM `cs2/cv2`: low-k P/Weyl nearly collinear; metric slip run `32774501069` gives slip `137.943212 deg`, equalized combined angle `56.963212 deg`.
- GDM vs designer f(R): scale modes nearly identical (`0.07813/0.10169 deg`), but time modes differ `25.18/25.49 deg` and full physical rays have opposite orientation (`154.82/154.51 deg`).
- WDM: low-k blindness broken by the small-scale transfer block.

Exp.033 hard graph run `32775055341` gives the exact unique minimum hitting set for the **current frozen hard-evidence graph**:

\[
\{\text{metric slip},\text{small-scale transfer},\text{time/sign evolution}\}.
\]

This is not a universal survey design.

---

## 5. Experiment 034 — first real-covariance cross-family bridge

Corrected DESI DR1 ShapeFit covariance order:

`[DV/rd, DH/DM, f_sigma_s8, m+n]`.

Because the atlas does not yet predict all four coordinates for every family, Exp.034 deliberately uses only the marginal `m+n` block instead of inserting false zeros into the other channels.

Finite-node proxy:

\[
r_\Delta(k,z)\approx A(z)+\frac{m(z)}{0.6}\tanh\left[0.6\ln\frac{k}{0.03}\right]+n(z)\ln\frac{k}{0.03},
\]

and `K_shape[r_Delta]=m+n`.

Hard run `32777716140`:

- exact synthetic ShapeFit recovery error `8.326672684688674e-17`;
- status `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`;
- artifact ID `9538572755`;
- artifact SHA256 `b1c6dc98d933e564d1c74ee549917621e5b4e2fbdc4e37d760bf80c2b13c4a38`.

Key results:

- GDM `cs2/cv2`: whitened acute shape-history angle `0.189582 deg`; degeneracy survives real `m+n` weighting.
- GDM/f(R): whitened acute angles about `23 deg`, **but** finite-node ShapeFit residual is about `36%` for GDM and f(R), so this is not a full DESI distinguishability claim.
- smooth-w proxy residual <=`1.33%`; IDE <=`5.87%`.
- unit-direction spectrum `(1,0.2055855,0.0106523,0.00194843,1.37046e-6)` is descriptive only; no rank claim.

Frozen result:

`data/derived/observational_whitening/experiment_034_shapefit_shape_whitening_v0_1.json`.

---

## 6. Experiment 035 — exact calibration-free AP operator

For flat FLRW,

\[
F_{AP}(z)=\frac{D_M}{D_H}=E(z)\int_0^z\frac{dz'}{E(z')}.
\]

If

\[
E_{model}(z)=A E_{ref}(z)e^{r_E(z)},
\]

then

\[
\boxed{\frac{F_{AP,model}}{F_{AP,ref}}
=e^{r_E(z)}
\frac{\int_0^z e^{-r_E(z')}dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}}.
\]

The arbitrary constant calibration `A` cancels exactly. Therefore the anchored DSIR response `r_E(z;z*=0.51)` retains all AP information. ShapeFit geometry obeys

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

First-order form:

\[
\Delta\ln F_{AP}(z)=r_E(z)-
\frac{\int_0^z r_E(z')dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}+O(r_E^2).
\]

Pre-frozen hard thresholds were not changed after first execution:

- direct wCDM bridge `<1e-11`;
- constant calibration-mode residual `<1e-12`;
- DH/DM sign identity `<1e-14`;
- linear-remainder halving ratio `<0.27`.

First attempt run `32778406204` stopped before the hard script because a unit-only assertion `<2e-15` saw a few-ulp cumulative-integration residual `2.6367796834847468e-15`. Unit tolerance was made robust at `1e-14`; **scientific hard thresholds were unchanged**.

Successful run `32778635058`:

- unit tests `4 passed`;
- direct wCDM error `1.0047518372857667e-14`;
- calibration-mode error `7.829674408821319e-15`;
- DH/DM sign identity error `0`;
- linear remainder halving ratio `0.24999659397608562`;
- status `PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1`;
- artifact ID `9538896209`;
- artifact SHA256 `f4a70ff9c67bdf45b520f7a2babaf63280fde6b841c45539a9c6fc22e3479d9f`.

Frozen result:

`data/derived/observational_whitening/experiment_035_ap_operator_v0_1.json`.

### Critical production requirement

The AP operator integrates from `z=0`. The seven-node structure atlas starts at `z=0.295`, so **do not extrapolate it to zero**. The C1 and C2 solver workflows already write full same-solver `background.dat` tables to their artifacts. The next experiment must use those full histories (or regenerate them with the exact pinned setup) to build production AP responses.

---

## 7. Real-data context already available

DESI DR2 AP supplies a calibration-free geometry response via `F_AP=D_M/D_H`. Corrected DESI DR1 ShapeFit supplies joint geometry/growth/shape covariance; superseded uncorrected Appendix-A growth/covariance values must not be used.

Existing conditional-innovation aggregate remains null-consistent:

\[
\chi^2\simeq5.53/5,\qquad p\simeq0.355.
\]

This is a null result, not a dark-sector law.

---

## 8. Exact continuation sequence from this checkpoint

1. **Experiment 036:** extract/regenerate full `z=0..2.33` same-solver background histories for C1 smooth-w and C2 IDE from their pinned workflows; retain full provenance and physical validity masks.
2. Map these histories through the Exp.035 operator to `Delta ln(DH/DM)` on the corrected DESI ShapeFit redshift support.
3. For C3/C5 and other perturbation-only/background-matched rays, encode exact-zero geometry response only after explicit theory/solver validation; never use zero for an unavailable response.
4. Whiten the family-complete geometry block using its measured covariance without pretending unpredicted growth/shape channels are zero.
5. Build a family-complete gauge-safe `f_sigma_s8` growth operator.
6. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware map or explicitly propagate compression-model error.
7. Only after geometry+growth+shape are family-complete form the full corrected ShapeFit block `Z=C^{-1/2} Delta O`.
8. Freeze rank/null thresholds before interpreting any data-whitened singular spectrum; stress-test family priors, channel removal, solver precision, and within-family sampling.
9. In parallel build observational lensing/slip and WDM small-scale-transfer blocks.
10. Resume G7 only after observationally whitened manifold/rank stability; any candidate law must predict a withheld physical channel before G8 can PASS.

**Never claim discovery before G8.**
