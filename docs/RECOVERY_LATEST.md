# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-25  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific findings:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Current status:** `docs/STATUS.md`  
**Gates:** `docs/GATES.md`  
**Latest observational log:** `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-25.md`

This is the mandatory **per-iteration recovery layer**. Update it after every substantive research iteration. `RECOVERY_MANUAL.md` contains the stable architecture/derivations; this file records the exact live state, newest formulas/results, negative findings, provenance, and next steps so another chat can resume without hidden context.

Hard boundary: **DSIR is independent of RTK. Never modify, import, overwrite, merge, or use the RTK repository as an unstated prior.**

---

## 1. Claim boundary and gates

DSIR is a reconstruction/meta-inference framework, not a fundamental theory. No new law of nature or discovery is claimed.

- **G1 PASS v0.1.1:** conservation/gauge contract and total-matter comoving response validated.
- **G2 PASS v0.1.1:** same-solver `r_Delta` basis and smooth-w cross-solver bridge validated.
- **G3A PASS v0.1:** six control families embedded at background level.
- **G3B PASS v0.1 block-aware:** six-family beyond-background atlas comparison-ready.
- **G4 PASS:** synthetic low-rank recovery.
- **G5 PARTIAL:** robustness tests plus real-covariance shape/AP layers exist, but family-complete geometry+growth+shape whitening/rank stress tests do not.
- **G6A/G6B PASS:** DESI DR2 AP and corrected DESI DR1 ShapeFit observational layers.
- **G7 OPEN:** no residual-law claim before family-complete observational kernels and stable whitened manifold/rank behavior.
- **G8 OPEN:** no discovery before a genuinely withheld physical prediction.

Hard chronology for current observational projection:

- Exp.034 run `32777716140`: `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`.
- Exp.035 run `32778635058`: `PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1`.
- Exp.036 run `32782545098`: `PASS_AP_FAMILY_GEOMETRY_V0_1`.
- Exp.037 run `32783243120`: `PASS_GDM_AP_ZERO_AUDIT_V0_1`.

---

## 2. Frozen response basis

Structure redshifts:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

Low-k grid:

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Anchored expansion response:

\[
r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right],\qquad z_*=0.51.
\]

Gauge-safe total-matter variables:

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\]

\[
\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}.
\]

Production structure response:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_{\Delta,model}^{S}(k,z)}{P_{\Delta,ref}^{S}(k,z)}}.
\]

Use matched same-solver model/reference lineage whenever possible. Never interpret a global catalog SVD span as microscopic dimension. Use local Jacobians or tangent cones where viability truncates parameter space.

---

## 3. Frozen family atlas

- **C0 LambdaCDM/GR:** common response origin.
- **C1 smooth non-phantom DE:** one-sided `epsilon_w=1+w -> 0+`, production tangent step `1e-4`.
- **C2 interacting vacuum:** `Q=H(alpha rho_idm+beta rho_iv)`; positive alpha excluded by frozen full-history positivity condition, so use negative-alpha physical ray `u=-alpha>=0` plus central beta line.
- **C3 GDM:** pinned GDM_CLASS; frozen closure manifold varies `cs2/cv2` with `w_gdm=0`.
- **C4 thermal WDM:** separate small-scale transfer block.
- **C5 designer f(R):** pinned H-EFTCAMB, production `B0={1e-6,1e-5,1e-4,1e-3}`.

Unknown response cells remain masked. A zero may be inserted only after an analytic or numerical contract establishes it; **missing is never zero**.

---

## 4. Key hard theory-level degeneracies/separators

- GDM `cs2/cv2`: low-k matter-power angle `0.322616 deg`; DESI `m+n` proxy angle `0.189582 deg`; metric slip `137.943212 deg` oriented and equalized two-block angle `56.963212 deg`.
- GDM versus designer f(R): leading scale modes nearly identical (`0.07813/0.10169 deg`), but time modes differ (`25.18/25.49 deg`) and full rays are oppositely oriented (`154.82/154.51 deg`).
- WDM 3 keV: nearly blind at `k=0.1` (`r_T=-3.46e-6`) but strong suppression by `k=10` (`r_T=-0.10375`).
- Current hard discriminant graph has unique minimum hitting set

\[
\{\text{metric slip},\text{small-scale transfer},\text{time/sign evolution}\}.
\]

This is for the current frozen evidence graph only, not a universal survey design.

Raw six-direction normalized singular ratios remain descriptive:

`(1,0.52046,0.26140,0.20087,0.08299,5.9178e-4)`.

**Do not assign `R_model=5`; no intrinsic-rank threshold was frozen.**

---

## 5. Experiment 034 — ShapeFit shape proxy

Corrected DESI DR1 ShapeFit parameter order:

`[DV/rd, DH/DM, f_sigma_s8, m+n]`.

Finite-node shape proxy:

\[
r_\Delta(k,z)\approx A(z)+\frac{m(z)}{0.6}\tanh\left[0.6\ln\frac{k}{0.03}\right]+n(z)\ln\frac{k}{0.03},
\]

with `K_shape[r_Delta]=m+n`.

Hard result run `32777716140`, artifact `9538572755`, SHA256 `b1c6dc98d933e564d1c74ee549917621e5b4e2fbdc4e37d760bf80c2b13c4a38`.

Important limit: finite-node ShapeFit residual is about `36%` for GDM `cs2`, GDM `cv2`, and designer f(R). Therefore the roughly `23 deg` GDM/f(R) whitened proxy angle is **not** a DESI distinguishability claim. A survey/window-aware shape mapping or explicit compression error is still required.

---

## 6. Experiment 035 — exact AP operator

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

The constant `A` cancels exactly, so anchored `r_E` retains all AP information. ShapeFit geometry is

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

First-order form:

\[
\Delta\ln F_{AP}=r_E(z)-
\frac{\int_0^z r_E(z')dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}+O(r_E^2).
\]

Hard run `32778635058`: direct wCDM bridge `1.00475e-14`, calibration-mode residual `7.82967e-15`, sign-identity error `0`, quadratic halving ratio `0.2499966`. Artifact `9538896209`, SHA256 `f4a70ff9c67bdf45b520f7a2babaf63280fde6b841c45539a9c6fc22e3479d9f`.

Critical production rule: AP integrates from `z=0`; never extrapolate the structure atlas from `z=0.295` to zero. Use full solver background histories.

---

## 7. Experiment 036 — C1/C2 production AP geometry

Exact source artifacts:

- C1: run `32771133024`, artifact `9536242626`, digest `sha256:ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b`.
- C2: run `32760042765`, artifact `9532491954`, digest `sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`.

Production convergence (`1e-3` vs `1e-4`, frozen relative-L2 ceiling `0.005`):

- C1 smooth-w `0.0015563369`;
- C2 negative-alpha `0.00013881894`;
- C2 beta `2.25987e-7`.

Corrected DESI `DH/DM` marginally whitened acute angles:

- smooth-w vs IDE negative-alpha `72.803493 deg`;
- smooth-w vs IDE beta `64.151094 deg`;
- IDE negative-alpha vs beta

\[
\boxed{9.0379006^\circ}
\]

with oriented angle `170.962099 deg`. Their frozen structure-block angle is about `58.9338 deg`.

Hard interpretation: the two IDE mechanism directions are nearly degenerate/antiparallel in AP geometry while substantially separated in structure. AP cannot replace growth/structure for IDE mechanism discrimination.

Run `32782545098`, result artifact `9540273287`, SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`.

---

## 8. Experiment 037 — C3 GDM background/AP-zero audit

Purpose: do **not** insert the expected GDM geometry zero by theory assumption. Reuse the exact immutable C3 artifact and prove the response numerically.

Source:

- run `32759738560`;
- artifact `9532247349`;
- digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`;
- upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Audited directions:

- `cs2={1e-8,1e-7,1e-6}`, with `w=0`, `cv2=0`;
- `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}`, with `w=0`, `cs2=0`.

Hard thresholds frozen before CI:

- redshift-grid mismatch `<=1e-12`;
- relative `H` mismatch `<=1e-12`;
- absolute `Delta ln(DH/DM)` at DESI target redshifts `<=1e-12`;
- INI contract must pass.

Hard run `32783243120` returned `PASS_GDM_AP_ZERO_AUDIT_V0_1`.

For every audited nonzero variant:

- redshift-grid mismatch = `0`;
- `max_abs_H=0`;
- `max_relative_H=0`;
- every saved numerical background column is exactly equal to reference;
- `Delta ln(DH/DM)=(0,0,0,0,0)` at `z=(0.51,0.71,0.92,1.32,1.49)`.

Result artifact `9540510596`; SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`. Frozen result:

`data/derived/observational_whitening/experiment_037_gdm_ap_zero_audit_v0_1.json`.

### Scientific consequence

Within the frozen `w_gdm=0` C3 manifold,

\[
K_{AP}t_{cs2}=K_{AP}t_{cv2}=0
\]

while established perturbation responses satisfy

\[
K_{structure}t_{cs2}\neq0,\qquad K_{structure}t_{cv2}\neq0.
\]

This is a hard example of **channel nullity / block-sparse influence**. The C3 AP cell is now a validated zero, not missing data and not zero-imputation.

Boundary: no claim for arbitrary nonzero/time-dependent `w_gdm`; GDM is not observationally null because perturbation/metric channels remain active.

---

## 9. Live scientific interpretation register

`docs/SCIENTIFIC_FINDINGS_REGISTER.md` is authoritative for evolving interpretations. Current entries:

- **F1 HARD for current examples / broader SUPPORTED:** degeneracy/nullity depends on observation channel.
- **F2 HARD:** GDM density-shape compression loses the pressure/viscosity distinction.
- **F3 HARD theory-level / observational PARTIAL:** scale shape alone does not separate GDM from designer f(R).
- **F4 HARD LIMIT:** finite-node ShapeFit `m+n` is not a universal operator for strongly scale-dependent new physics.
- **F5 HARD:** AP is invariant to arbitrary normalization of anchored `r_E`.
- **F6 HARD:** IDE alpha/beta AP acute angle `9.0379 deg` versus structure angle `58.9338 deg`.
- **F7 HARD for current graph:** complementary channel types are required by the present discriminant graph.
- **F8 SUPPORTED HYPOTHESIS:** model identity is a multi-channel influence trajectory; Exp.037 suggests the trajectory can be block-sparse.
- **F9 HARD:** frozen GDM `cs2/cv2` with `w=0` are background/AP-null but perturbation-active.

On contradiction, mark `SUPERSEDED/RETRACTED`; never erase the old result or chronology.

---

## 10. Exact continuation sequence

1. **C5 designer-f(R) AP audit:** existing frozen H-EFTCAMB artifact confirms the production configs use `EFTwDE=0` and that background writing was enabled, but no clearly usable full background file is preserved. Inspect the pinned workflow/output paths and create a dedicated background-output hard run if needed. Do not insert a C5 zero before numerical validation.
2. After C5 audit, build the family-complete AP geometry cell. C0 is the origin; C1/C2 are nonzero validated tangents; C3 is now hard zero; C4 remains a separate small-scale block unless an explicit validated AP mapping is defined; C5 is pending audit.
3. Build a family-complete gauge-safe `f_sigma_s8` growth operator. The corrected ShapeFit `sigma_s8` convention includes sound-horizon-rescaled smoothing/shape dependence; do not substitute naive textbook `f sigma8` without a controlled bridge.
4. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware shape map or propagate compression-model error explicitly.
5. Only after geometry+growth+shape are family-complete form the full corrected ShapeFit block

\[
Z=C^{-1/2}\Delta O.
\]

6. Freeze null/rank thresholds **before** inspecting data-whitened spectra. Stress-test family prior `pi`, within-family sampling, solver precision, covariance perturbations, and channel removal.
7. In parallel construct observational lensing/slip and WDM small-scale-transfer blocks because current hard evidence identifies them as high-value independent separators.
8. Resume G7 only after the observationally whitened manifold/rank structure is stable. Any candidate law must predict a withheld physical channel before G8 can PASS.

**Never claim discovery before G8.**
