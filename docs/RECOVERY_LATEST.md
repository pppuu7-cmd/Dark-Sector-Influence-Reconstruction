# DSIR RECOVERY LATEST — live overlay

**Date:** 2026-08-24  
**Read first:** `docs/RECOVERY_MANUAL.md`  
Then read this file, `docs/GATES.md`, `docs/STATUS.md`, `docs/RESEARCH_LOG.md`, `docs/PROVENANCE.md`, `docs/CONSERVATION_GAUGE_V0_1.md`, and the response-basis specifications.

Hard boundary: **DSIR is separate from RTK. Do not modify, use, or overwrite the RTK repository/project while continuing DSIR.**

---

## 1. Scientific status

DSIR is still a reconstruction/meta-inference framework, **not yet a fundamental theory**. No new dark-sector law is claimed.

Current hard gates:

- **G1 PASS for v0.1.1 scope:** conservation/Bianchi bookkeeping and the common gauge-safe matter construction are validated.
- **G2 PASS v0.1.1:** production perturbation response is the same-solver comoving total-matter power response `r_Delta`; cross-solver hard bridge passed.
- **GDM-S0/S1 PASS.**
- **IDE-S0/S1 PASS.**
- **MG-S0 PASS:** exact designer-f(R) GR limit validated in pinned H-EFTCAMB with pre-frozen hard thresholds.
- **G3B PARTIAL but advanced:** all six control families now have a validated response path, but nonzero family-manifold sampling is incomplete.
- **G7 OPEN:** do not search/claim a new residual law until the family-balanced six-family response atlas and rank stability checks are complete.
- **G8 OPEN:** no discovery claim before a withheld observable/channel prediction.

Method guards already in `main`:

- validity masks/common-subspace rule — undefined cells are never zero/mean-imputed;
- family-balanced theory-atlas sampling — model multiplicity is treated as an explicit prior;
- WDM small-scale transfer block — low-k invisibility is not interpreted as absence of WDM physics.

---

## 2. Production response basis v0.1.1

Frozen redshift nodes:

`z = {0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33}`.

Frozen linear-core k nodes:

`k = {0.001, 0.003, 0.01, 0.03, 0.1} h/Mpc`.

Background coordinate:

\[
r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{\rm ref}(z)/H_{\rm ref}(z_*)}\right],
\qquad z_*=0.51.
\]

A common multiplicative H calibration cancels.

For the documented total-matter component set,

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},
\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\qquad
w_m=\frac{p_m}{\rho_m}.
\]

Production comoving matter contrast:

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}},
\qquad {\cal H}=aH.
\]

Pressureless limit:

\[
\Delta_m=\delta_m+3{\cal H}\theta_m/k^2.
\]

Production perturbation response:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_\Delta^{\rm model,S}(k,z)}{P_\Delta^{\rm ref,S}(k,z)}}.
\]

`S` means the same solver lineage and matched numerical settings for model and reference whenever possible. Absolute spectra from different solver vintages are not interpreted as a dark-sector response.

Cross-solver bridge: smooth `w0=-0.9`, `wa=0`, `cs2=1` calculated with matched p8 precision in pinned GDM_CLASS and repaired pinned class_iv gave

\[
\max|r_{GDM\_CLASS}-r_{class\_iv}|=2.3747404043\times10^{-10}.
\]

Hard threshold `1e-9` was frozen before the final rerun and passed.

---

## 3. Solver pins and validated zero limits

### GDM_CLASS

Pinned:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Source uses the generalized comoving correction

`delta_m += 3*(1+P_m/rho_m)*a*H*theta_m/k^2`.

GDM-S1 hard gate:

`max core zero-GDM/CDM residual <= 5e-6`.

Actual p8 hard result:

`1.471014806e-6`.

Keep `start_small_k_at_tau_c_over_tau_h=1e-6`; pushing only this parameter earlier was non-monotonic and is retained as a negative result. `k<1e-3 h/Mpc` remains a separate finite-start/IC-sensitive diagnostic sector.

Validated p8 preset used for nonzero GDM manifold and cross-solver bridge:

- `k_step_sub = 0.0010`
- `k_step_super = 0.000003`
- `k_step_super_reduction = 0.1`
- `start_small_k_at_tau_c_over_tau_h = 1e-6`
- `start_large_k_at_tau_h_over_tau_k = 0.05`
- `tight_coupling_trigger_tau_c_over_tau_h = 0.005`
- `tight_coupling_trigger_tau_c_over_tau_k = 0.008`
- `start_sources_at_tau_c_over_tau_h = 0.006`
- `tol_perturb_integration = 3e-10`
- `perturb_sampling_stepsize = 0.00035`
- `radiation_streaming_approximation = 2`
- `radiation_streaming_trigger_tau_over_tau_k = 240.`
- `radiation_streaming_trigger_tau_c_over_tau = 100.`
- `ur_fluid_approximation = 2`
- `ur_fluid_trigger_tau_over_tau_k = 50.`

Current new branch/PR: `research/gdm-cs2-manifold`, PR #9. First calibration fixes `w=0`, `cv2=0` and varies constant

`cs2 = {1e-8,1e-7,1e-6,1e-5,1e-4}`

relative to the same-solver zero-closure GDM reference. No hard threshold or rank claim is allowed from the first scan.

### interacting vacuum / class_iv

Pinned:

`kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

The fork requires an assertion-checked compile-only removal of one premature brace, plus legacy `-fcommon` and `--no-as-needed` link semantics. These are implementation/toolchain repairs only; no cosmological equation is altered.

IDE-S1 hard thresholds:

- linear-core power `<=2e-8`;
- semantic background `<=2e-12`.

Both passed.

The synchronous `vTk` header has an upstream title/index defect. Species-level `vTk` columns are diagnostic only. Internal total-matter `mPk` source is the production path.

---

## 4. H-EFTCAMB designer-f(R): MG-S0 closed

Pinned official H-EFTCAMB:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`, branch `eftcamb`.

Production designer configuration:

- `EFTflag=3`
- `DesignerEFTmodel=1`
- `EFTwDE=0` — LambdaCDM background
- `EFTB0=B0`

Physical parameter:

\[
B(a)=\frac{f_{RR}}{1+f_R}\frac{R'H}{H'},
\qquad B_0=B(a=1).
\]

First parallel build `make -j2 camb` failed because of an upstream Makefile dependency race (`camb.mod` not ready before `inidriver.f90`). Serial upstream-style `make camb` succeeds. Retain this negative result; it is not a physics failure.

Calibration sweep at z=0 showed maximum core responses approximately:

| B0 | max |r_Delta| |
|---:|---:|
| 1e-2 | 3.7805e-1 |
| 1e-3 | 2.0148e-1 |
| 1e-4 | 6.8778e-2 |
| 1e-5 | 1.1959e-2 |
| 1e-6 | 1.5963e-3 |
| 1e-7 | 2.0803e-4 |
| 1e-8 | ~1.1e-6 stock-export floor |

Exact `B0=0` is supported. The root finder reports approximately

\[
B_0^{found}=-2.22\times10^{-17}.
\]

Pinned H-EFTCAMB uses

`EFTCAMB_GR_threshold = 1e-8`.

For `B0=1e-8`, `Return to GR time = 1.1`; this point follows the GR branch through today and must not be treated as an independent nonzero atlas member. For `B0=1e-7`, return-to-GR time is about `a=0.7832`, and a nonzero response appears.

Stock interpolated matter power passes through `Transfer_GetMatterPowerS`, which casts the output array to ordinary `real`; the production hard tolerance therefore includes the documented export floor.

After calibration and **before** a new hard run, DSIR froze

\[
\boxed{\max_{k\in K_{core}}|r_\Delta(B_0=0)|\le2\times10^{-6}}
\]

and

\[
\boxed{|B_0^{found}|\le10^{-12}}
\]

plus mandatory theory-stability PASS.

Fresh hard Actions run `32738835354` passed:

\[
\max|r_\Delta(B_0=0)|=1.0926960404\times10^{-6}
\]

with node vector `(0,0,0,1.0926960404e-6,0)`, and

\[
B_0^{found}=-2.221\times10^{-17}.
\]

**MG-S0 PASS.** See `experiments/021_eftcamb_designer_fr_gr_limit.md`.

Next MG step is **MG-S1**: calculate nonzero stable B0 values safely above `1e-8` on all frozen z x k nodes, with same-solver GR reference. Compare to the old BZ toy only on its QS-safe `k={0.01,0.03,0.1}` subset.

---

## 5. WDM and scale-block rule

Thermal-WDM transfer control:

\[
T_{WDM}(k)=\left[1+(\alpha k)^{2\nu}\right]^{-5/\nu},
\qquad \nu\approx1.12.
\]

Power/transfer log response:

\[
r_T(k)=\ln(P_{WDM}/P_{CDM})=2\ln T(k).
\]

For 3 keV WDM the low-k core is nearly blind (`r_T(0.1)~ -3.9e-6`), while `r_T(10)~ -0.117` and `r_T(20)~ -0.539`. Therefore low-k and small-scale blocks must be reported separately. The small-scale transfer fingerprint is not relabeled as nonlinear z=0 P(k) and is not itself a Ly-alpha likelihood.

No global `R_model` number may be quoted without specifying the response/scale block.

---

## 6. Rank/manifold rules

Before rank:

\[
Z=C^{-1/2}\Delta O,
\qquad Z=U\Sigma V^T.
\]

No unwhitened rank claim is allowed. Exp.011 recovered rank 3 in 30/30 whitened tests while naive raw-space calibration produced false ranks 20–35.

Theory sampling is an explicit prior:

\[
\pi(i)=\pi(f)\pi(i|f),
\qquad R_{model}=R_{model}(\pi).
\]

Equal-total-family weighting is implemented as one defensible reference prior, not assumed uniquely correct. Report sensitivity to within-family sampling and stratified bootstrap.

Missing channels:

- undefined response = masked/NaN;
- never fill with zero/mean;
- ordinary SVD only on an exact common valid subspace unless a separately validated missing-data method is used.

Before law discovery project/quotient:

- exact definitions;
- Bianchi/conservation identities;
- calibration/nuisance directions;
- measurement-induced degeneracies;
- derived coordinates already determined by parent coordinates.

Current corrected DESI DR1 ShapeFit conditional-innovation aggregate remains null-consistent (`chi2~5.53/5`, `p~0.355`). **G7 stays OPEN.**

---

## 7. Exact continuation sequence

1. Merge the MG-S0 branch only after its final diff/CI review; the scientific hard gate is already PASS.
2. Create MG-S1 from updated `main` and run a family of nonzero stable `B0 > 1e-8` values on the complete frozen z x k grid.
3. Inspect PR #9 GDM `cs2` calibration; determine monotonicity, scale/redshift localization, solver stability, and whether sampling needs an expanded axis before freezing any production grid.
4. Build an IDE nonzero interaction manifold using the already validated repaired pinned `class_iv`; do not infer the perturbation manifold from the background equivalence map alone.
5. Populate model-instance records for all six families with solver SHA, parameters, basis id, validity mask and reference model.
6. Assemble low-k common response blocks first; keep WDM small-scale transfer as a separate block until an overlap-connected observable construction is validated.
7. Quotient identities/nuisance directions, whiten with the relevant covariance/precision model, and estimate `R_model(pi)` under multiple defensible theory priors.
8. Stress-test rank against family sampling density, solver precision, removal of individual families, and scale/redshift sub-blocks.
9. Only then reopen G7 residual-law search.
10. Any candidate relation must predict a withheld physical channel before G8 can pass.

**Never claim discovery before G8.**
