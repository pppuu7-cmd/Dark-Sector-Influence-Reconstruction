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
- **G5 PARTIAL:** synthetic whitening/prior/missingness protections pass; Experiment 034 adds the first real-covariance cross-family shape proxy, but family-complete observational whitening/rank stress tests remain.
- **G6A/G6B PASS:** DESI DR2 AP and corrected DESI DR1 ShapeFit real-data response layers.
- **G7 OPEN:** no residual-law claim before family-complete observation kernels and data-whitened rank/manifold stability.
- **G8 OPEN:** no discovery before a withheld physical prediction.

Comparison readiness hard run: Experiment 030, run `32772758188`, `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON`, `failures=[]`.

First cross-family raw-theory comparison: Experiment 031 complete. Hard conditional separators: Experiments 031/032 PASS. Hard-evidence discriminant graph: Experiment 033 run `32775055341` PASS.

First partial observational whitening: Experiment 034 run `32777716140` PASS with status `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`.

---

## 2. Frozen response basis v0.1.1

Redshift nodes:

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

Never identify global SVD span with microscopic dimension. For a smooth manifold use the local Jacobian

\[
J_{ai}=\partial r_a/\partial\theta_i,
\]

and use a tangent cone when viability truncates parameter space.

---

## 3. Validated family atlas

- **C0 LambdaCDM/GR:** common response origin.
- **C1 smooth non-phantom DE:** one-sided `epsilon_w=1+w -> 0+` ray; smallest resolved step `1e-4`.
- **C2 interacting vacuum:** `Q=H(alpha rho_idm + beta rho_iv)`; `alpha>0` invalid under full-history `rho_iv>=0`; use negative-alpha ray plus central beta line. Structure angle `58.9338 deg`, background angle `10.8306 deg`.
- **C3 GDM:** pinned GDM_CLASS; zero-limit PASS. `cs2/cv2` low-k matter-power angle `0.322616 deg`, local two-axis `sigma2/sigma1=2.572e-3`.
- **C4 thermal WDM:** intentionally separate small-scale block; 3 keV control `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375`.
- **C5 designer f(R):** official H-EFTCAMB; MG-S0/MG-S1 PASS; production `B0={1e-6,1e-5,1e-4,1e-3}`.

Undefined theory/channel cells remain masked, never zero-imputed.

---

## 4. Raw-theory comparison and hard discriminants

The six nonzero low-k response objects are C1 smooth-w, C2 negative-alpha, C2 beta, C3 cs2, C3 cv2, C5 designer-f(R). C0 is the origin; C4 is a separate small-scale block.

Raw normalized six-direction singular ratios:

`(1,0.52046,0.26140,0.20087,0.08299,5.9178e-4)`.

**Do not call this `R_model=5`.** No intrinsic-rank threshold was frozen.

Hard theory-level separators:

- GDM `cs2/cv2`: low-k P/Weyl nearly collinear, but metric slip hard run `32774501069` gives Weyl `0.300737 deg`, slip `137.943212 deg`, equalized combined `56.963212 deg`.
- GDM vs designer f(R): leading scale shapes nearly identical (`0.07813/0.10169 deg`), but time modes differ `25.18/25.49 deg` and full physical rays have opposite orientation (`154.82/154.51 deg`).
- WDM: low-k blindness broken by the small-scale transfer block.

Experiment 033 hard graph run `32775055341` gives the exact unique minimum hitting set for the **current frozen hard-evidence graph**:

\[
\{\text{metric slip},\text{small-scale transfer},\text{time/sign evolution}\}.
\]

This is not a universal survey design.

---

## 5. Experiment 034 — first real-covariance cross-family bridge

The corrected DESI DR1 ShapeFit covariance is ordered as

`[DV/rd, DH/DM, f_sigma_s8, m+n]`.

The frozen atlas does not yet predict all four coordinates for every family, so using the full inverse covariance would falsely insert zero response in unpredicted channels. Experiment 034 therefore uses only a conservative marginal `m+n` shape block.

Finite-node ShapeFit proxy:

\[
r_\Delta(k,z)\approx A(z)+\frac{m(z)}{a}\tanh\left[a\ln\frac{k}{k_p}\right]+n(z)\ln\frac{k}{k_p},
\]

with `a=0.6`, `k_p=0.03 h/Mpc`, and

\[
K_{shape}[r_\Delta](z)=\hat m(z)+\hat n(z).
\]

Whitening on `LRG1,LRG2,LRG3,ELG2,QSO` is

\[
Z_i^{shape}=\frac{\Delta(m+n)_i}{\sqrt{C_{ii}^{m+n,m+n}}}.
\]

The Schur-complement conditional shape error is diagnostic only; it is not used as evidence until the other channels are predicted.

Hard run `32777716140`:

- unit tests `3 passed`;
- exact synthetic ShapeFit recovery error `8.326672684688674e-17`;
- status `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`;
- artifact ID `9538572755`;
- artifact ZIP SHA256 `b1c6dc98d933e564d1c74ee549917621e5b4e2fbdc4e37d760bf80c2b13c4a38`.

Key shape-history angles:

- GDM `cs2/cv2`: raw acute `0.190257 deg`, whitened acute `0.189582 deg` — degeneracy survives real `m+n` covariance weighting.
- GDM `cs2/f(R)`: raw acute `20.771942 deg`, whitened acute `22.995730 deg`.
- GDM `cv2/f(R)`: raw acute `20.956124 deg`, whitened acute `23.178674 deg`.
- smooth-w/GDM `cs2`: raw acute `12.132482 deg`, whitened acute `12.795598 deg`.

Descriptive unit-direction spectrum in this five-bin shape proxy:

`(1,0.2055855,0.0106523,0.00194843,1.37046e-6)`.

**No rank claim.**

Critical limitation discovered: the finite-node ShapeFit template residual is small for smooth-w (`<=1.33%`) and moderate for IDE (`<=5.87%`), but about `36%` for GDM `cs2`, GDM `cv2`, and designer f(R). Therefore the roughly `23 deg` GDM/f(R) whitened proxy angle is **not** a full DESI distinguishability result. A survey/window-aware shape operator or explicit compression-model-error propagation is required.

Frozen machine-readable result:

`data/derived/observational_whitening/experiment_034_shapefit_shape_whitening_v0_1.json`.

Detailed chronology:

`docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-24.md`.

---

## 6. Real-data context already available

DESI DR2 AP supplies a calibration-free geometry response via `F_AP=D_M/D_H`. Corrected DESI DR1 ShapeFit supplies joint geometry/growth/shape covariance; superseded uncorrected Appendix-A growth/covariance numbers must not be used.

The existing conditional-innovation aggregate is null-consistent:

\[
\chi^2\simeq5.53/5,\qquad p\simeq0.355.
\]

This remains a null result, not a dark-sector law.

---

## 7. Exact continuation sequence from this checkpoint

1. Build a family-complete `DH/DM` / AP observation operator on the DESI ShapeFit redshift support.
2. Build a family-complete gauge-safe `f_sigma_s8` growth operator from the validated solver lineages.
3. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware ShapeFit map or explicitly propagate compression-model error.
4. Only after 1–3 form the full corrected ShapeFit block

\[
Z=C^{-1/2}\Delta O.
\]

5. Report raw-theory and data-whitened pairwise geometry side by side.
6. Stress-test local Jacobian/global spectra and `R_model(pi)` under family priors, channel removal, solver precision, and within-family sampling; freeze rank/null thresholds before interpreting the spectrum.
7. In parallel build an observational lensing/slip block, because the hard graph says metric slip is the best established separator for the GDM `cs2/cv2` degeneracy.
8. Build/ingest a small-scale-transfer observational block for WDM.
9. Resume G7 residual-law search only after family-complete observationally whitened manifold/rank stability.
10. Any candidate relation must predict a withheld physical channel before G8 can PASS.

**Never claim discovery before G8.**
