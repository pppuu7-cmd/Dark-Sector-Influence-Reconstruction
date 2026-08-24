# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-25  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific interpretation register:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Current status:** `docs/STATUS.md`  
**Gates:** `docs/GATES.md`  
**Latest observational logs:** `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-24.md`, `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-25.md`

This file is the mandatory **per-iteration recovery layer**. The long `RECOVERY_MANUAL.md` contains the stable derivations/architecture; this overlay must be updated every substantive iteration so a new chat can recover the exact live state without relying on conversation memory.

Hard boundary: **DSIR is separate from RTK. Do not modify, import, overwrite, or merge the RTK project while continuing DSIR.**

---

## 1. Scientific state and claim boundary

DSIR is a reconstruction/meta-inference framework, **not a fundamental theory**. No new law of nature or discovery is claimed.

Current gates:

- **G1 PASS v0.1.1:** conservation/gauge contract and comoving total-matter response validated.
- **G2 PASS v0.1.1:** same-solver `r_Delta` basis and cross-solver smooth-w bridge validated.
- **G3A PASS v0.1:** six control families embedded at background level.
- **G3B PASS v0.1 block-aware:** six-family beyond-background atlas comparison-ready.
- **G4 PASS:** synthetic low-rank recovery.
- **G5 PARTIAL:** synthetic robustness passes; real-covariance shape proxy, exact AP operator, and C1/C2 production AP geometry now exist, but family-complete joint observation kernels/rank stress tests do not.
- **G6A/G6B PASS:** DESI DR2 AP and corrected DESI DR1 ShapeFit real-data layers.
- **G7 OPEN:** no residual-law claim before family-complete observation kernels and data-whitened rank/manifold stability.
- **G8 OPEN:** no discovery before a withheld physical prediction.

Hard chronology relevant to the current comparison:

- Exp.030 run `32772758188`: comparison readiness PASS.
- Exp.031: first raw-theory cross-family comparison complete.
- Exp.032: GDM slip discriminator hard PASS.
- Exp.033 run `32775055341`: discriminant graph hard PASS.
- Exp.034 run `32777716140`: `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`.
- Exp.035 run `32778635058`: `PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1`.
- Exp.036 first attempt `32782445280`: infrastructure-only failure while downloading a prior artifact; scientific hard script did not run and thresholds were unchanged.
- Exp.036 successful run `32782545098`: `PASS_AP_FAMILY_GEOMETRY_V0_1`.

---

## 2. Frozen response basis v0.1.1

Structure redshift nodes:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

Low-k nodes:

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Anchored background response:

\[
r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right],\qquad z_*=0.51.
\]

Total-matter comoving contrast:

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},\qquad
\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}.
\]

Production structure response:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_{\Delta,model}^{S}(k,z)}{P_{\Delta,ref}^{S}(k,z)}}.
\]

`S` must be the same solver lineage/model-reference numerical setup whenever possible. Never identify a raw global SVD span with microscopic dimension; use local Jacobians or tangent cones under viability boundaries.

---

## 3. Frozen family atlas

- **C0 LambdaCDM/GR:** common response origin.
- **C1 smooth non-phantom DE:** one-sided `epsilon_w=1+w -> 0+` ray; production step `1e-4`.
- **C2 interacting vacuum:** `Q=H(alpha rho_idm + beta rho_iv)`; positive alpha violates the frozen full-history positivity condition, so use the physical negative-alpha ray plus central beta line.
- **C3 GDM:** pinned GDM_CLASS; `cs2/cv2` are independent perturbation/closure directions with `w_gdm=0` in the frozen manifold.
- **C4 thermal WDM:** separate small-scale transfer block.
- **C5 designer f(R):** pinned H-EFTCAMB; production `B0={1e-6,1e-5,1e-4,1e-3}`.

Undefined theory/channel cells are masked. **Never zero-impute missing responses.**

---

## 4. Hard comparison findings before observational AP completion

Raw six-direction normalized singular ratios:

`(1,0.52046,0.26140,0.20087,0.08299,5.9178e-4)`.

This is descriptive only. **Do not call it `R_model=5`; no intrinsic-rank threshold is frozen.**

Hard pairwise structure/discriminator findings:

- GDM `cs2/cv2`: low-k matter-power angle `0.322616 deg`; metric slip `137.943212 deg` oriented; equalized two-block angle `56.963212 deg`.
- GDM versus designer f(R): leading scale-mode angles `0.07813/0.10169 deg`, time-mode separation `25.18/25.49 deg`, full oriented rays around `154.82/154.51 deg`.
- WDM 3 keV control: `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375`; low-k blindness is broken by the high-k transfer block.

Exp.033 unique minimum hitting set for the **current frozen evidence graph**:

\[
\{\text{metric slip},\text{small-scale transfer},\text{time/sign evolution}\}.
\]

Not a universal survey design.

---

## 5. Experiment 034 — first real-covariance shape bridge

Corrected DESI DR1 ShapeFit covariance order:

`[DV/rd, DH/DM, f_sigma_s8, m+n]`.

Finite-node proxy:

\[
r_\Delta(k,z)\approx A(z)+\frac{m(z)}{0.6}\tanh\left[0.6\ln\frac{k}{0.03}\right]+n(z)\ln\frac{k}{0.03},
\]

with `K_shape[r_Delta]=m+n`.

Production uses only the marginal `m+n` variance because all four ShapeFit coordinates are not yet predicted for every family; full covariance inversion with fake zeros is forbidden.

Hard result:

- run `32777716140`;
- status `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`;
- artifact ID `9538572755`;
- SHA256 `b1c6dc98d933e564d1c74ee549917621e5b4e2fbdc4e37d760bf80c2b13c4a38`.

Key findings:

- GDM `cs2/cv2` whitened acute shape-history angle `0.189582 deg`: degeneracy survives real covariance weighting.
- GDM/f(R) proxy angle about `23 deg`, but the finite-node ShapeFit basis leaves about `36%` residual for GDM/f(R), so **no DESI distinguishability claim** is allowed.
- smooth-w/IDE compression residuals are much smaller.

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

The arbitrary constant `A` cancels exactly, so the anchored DSIR `r_E` retains all AP information. ShapeFit geometry obeys

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

First-order form:

\[
\Delta\ln F_{AP}(z)=r_E(z)-
\frac{\int_0^z r_E(z')dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}+O(r_E^2).
\]

Successful hard run `32778635058`:

- direct wCDM bridge error `1.0047518372857667e-14`;
- additive calibration error `7.829674408821319e-15`;
- `DH/DM` sign identity error `0`;
- linear-remainder halving ratio `0.24999659397608562`;
- artifact ID `9538896209`;
- SHA256 `f4a70ff9c67bdf45b520f7a2babaf63280fde6b841c45539a9c6fc22e3479d9f`.

Critical requirement discovered: AP integrates from `z=0`. Never extrapolate the seven-node structure atlas from `z=0.295` down to zero; use full solver background histories.

---

## 7. Experiment 036 — hard production AP geometry for C1/C2

Exact frozen source artifacts:

**C1 smooth-w**
- run `32771133024`;
- artifact `9536242626`;
- digest `sha256:ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b`;
- upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

**C2 IDE**
- run `32760042765`;
- artifact `9532491954`;
- digest `sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- upstream `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Hard thresholds frozen before scientific CI:

- relative L2 tangent convergence `<0.005` for C1, C2 alpha, C2 beta comparing `1e-3` with production `1e-4`;
- finite/nonzero direction checks;
- **no angular threshold and no rank threshold**.

Hard successful run `32782545098`:

- status `PASS_AP_FAMILY_GEOMETRY_V0_1`;
- result artifact ID `9540273287`;
- artifact SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`;
- frozen result `data/derived/observational_whitening/experiment_036_ap_family_geometry_v0_1.json`.

Convergence relative L2 at `1e-3` vs production `1e-4`:

- C1 smooth-w `0.0015563369`;
- C2 negative-alpha ray `0.00013881894`;
- C2 beta `2.25987e-7`.

Corrected DESI `DH/DM` marginally whitened angles:

- smooth-w vs IDE negative-alpha: acute `72.803493 deg`;
- smooth-w vs IDE beta: acute `64.151094 deg`;
- IDE negative-alpha vs beta: oriented `170.962099 deg`, acute

\[
\boxed{9.0379006^\circ}.
\]

The same IDE alpha/beta directions have frozen structure-block angle about `58.9338 deg`.

**Hard interpretation:** these two IDE mechanism directions are nearly antiparallel/degenerate in AP geometry despite being substantially separated in structure. AP alone cannot identify the IDE interaction mechanism and cannot replace growth/structure information.

Do not interpret whitened tangent norms as detection significance or parameter constraints; parameter units are heterogeneous and no full likelihood was formed.

C3/C5 expected zero-geometry cells are **not hard-tested by Exp.036** and remain deferred; they must not be inserted as zeros merely from missing data.

---

## 8. Live scientific findings protocol

Read `docs/SCIENTIFIC_FINDINGS_REGISTER.md` before interpreting new results. It currently records:

- **F1:** observational degeneracy is channel-dependent — HARD for current examples; broader principle supported, not universal.
- **F2:** GDM density-shape compression erases pressure/viscosity distinction — HARD in frozen blocks.
- **F3:** scale shape alone is insufficient for GDM vs designer f(R) — HARD theory-level, survey interpretation partial.
- **F4:** finite-node ShapeFit `m+n` is not a universal new-physics operator — HARD negative/limit result.
- **F5:** AP is invariant to the arbitrary normalization of anchored `r_E` — HARD exact identity.
- **F6:** IDE alpha/beta AP degeneracy (`9.0379 deg` acute) versus structure separation — HARD Exp.036.
- **F7:** current discriminant graph requires complementary channel types — HARD for the frozen graph.
- **F8:** model identity as a multi-channel influence trajectory — SUPPORTED HYPOTHESIS, not a law.

Every substantive iteration must re-evaluate touched findings and change status explicitly. If later work contradicts a result, mark it `SUPERSEDED/RETRACTED`; preserve the old result and chronology rather than deleting it.

---

## 9. Exact continuation sequence from this checkpoint

1. **C3 AP-zero audit:** use the pinned GDM_CLASS artifact/config to numerically verify that `cs2/cv2` directions with `w_gdm=0` leave the background/AP response at zero within a pre-frozen numerical tolerance. Do not assume zero merely because the parameters are perturbative.
2. **C5 AP-zero audit:** inspect the pinned H-EFTCAMB designer-f(R) artifact. If full background histories are present, audit `EFTwDE=0` Lambda-like background numerically; otherwise create a dedicated background-output workflow with the existing pinned solver/config.
3. Only after C3/C5 audits form a family-complete AP geometry cell. Keep C4 WDM in its separate small-scale block unless a validated geometry response is explicitly defined.
4. Build a family-complete, gauge-safe `f_sigma_s8` growth operator from validated total-matter solver lineages and the corrected ShapeFit convention. Be careful that ShapeFit `sigma_s8` contains a sound-horizon-rescaled smoothing/shape convention; do not substitute a naive `f sigma8` mapping without an explicit bridge/control.
5. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware response or explicitly propagate compression-model error.
6. Only after geometry+growth+shape are family-complete form the full corrected ShapeFit block `Z=C^{-1/2} Delta O`.
7. Freeze null/rank thresholds **before** interpreting any data-whitened spectrum; stress-test family prior `pi`, within-family sampling, solver precision, and channel removal.
8. In parallel construct observational lensing/slip and WDM small-scale-transfer blocks because the hard discriminant graph identifies them as high-value independent separators.
9. Resume G7 residual-law search only after the observationally whitened manifold/rank structure is stable. Any law candidate must make a withheld physical prediction before G8 can PASS.

**Never claim discovery before G8.**
