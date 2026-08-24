# DSIR RECOVERY LATEST — live overlay

**Date:** 2026-08-24  
**Read after:** `docs/RECOVERY_MANUAL.md`

This file is the live delta to the long recovery manual. A new chat/researcher should read the manual first, then this file, then `docs/GATES.md`, `docs/STATUS.md`, `docs/RESEARCH_LOG.md`, and `docs/PROVENANCE.md`.

## 1. Current gate state

- **G2 PASS:** response basis v0.1 is frozen.
- **G3B PARTIAL:** LambdaCDM, smooth-wCDM, thermal-WDM and designer-f(R) controls exist; GDM and interacting-vacuum source-level zero limits pass; their full-solver numerical gates are still being finalized.
- **G7 OPEN:** no new residual dark-sector law is claimed.
- **G8 OPEN:** no discovery claim is allowed before withheld prediction.

Hard boundary: **do not modify/use RTK as a DSIR prior.**

---

## 2. Frozen response basis v0.1 (Experiment 017)

Machine schema: `config/response_basis_v0_1.json`  
Human specification: `docs/RESPONSE_BASIS_V0_1.md`  
Implementation: `src/dsir/response_basis.py`

### Core background coordinate

Use anchored relative expansion

`r_E(z;z*) = ln[(H(z)/H(z*))/(H_ref(z)/H_ref(z*))]`,

with `z*=0.51` and frozen nodes

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

A common calibration `H->lambda H` cancels exactly. The anchor coordinate is identically zero and is not counted as a dimension.

### Core perturbation coordinate

Use fixed-primordial matter-power response

`r_P(k,z)=ln[P_m(k,z)/P_m_ref(k,z)]`.

Do **not** independently normalize each model to `D(1)=1` when amplitude is part of the response. Hold primordial normalization (`A_s`, `n_s`, etc.) fixed unless an explicit nuisance quotient is documented.

Linear k core:

`k/(h Mpc^-1)={0.001,0.003,0.01,0.03,0.1}`.

Diagnostic extension:

`{0.2,0.5,1.0}`.

For the pinned GDM implementation, `k<0.001 h/Mpc` remains a separate ultra-large-scale diagnostic sector because its zero-limit branch has strong finite-start IC sensitivity. This sector is retained, not discarded, but is not mixed into the first common six-family rank block.

### Exact identities / quotient rule

For flat FLRW

`F_AP=D_M H/c`, hence

`r_FAP=r_DM+r_H`.

Never count a derived coordinate and its parent coordinates as independent response dimensions.

For removal of a constant log-power amplitude mode with precision `W=C^-1`, use

`a=(1^T W r)/(1^T W 1)`,

`r_perp=r-a 1`,

so exactly

`1^T W r_perp=0`.

Covariance whitening remains mandatory before rank claims.

Experiment 017 regression verifies calibration invariance, AP identity, fixed-primordial amplitude preservation, and W-orthogonality at floating-point precision.

---

## 3. Interacting vacuum — source convention and zero limit

Pinned upstream:

`kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Source convention:

`Q = H (alpha rho_m + beta rho_v)`.

Therefore

`d rho_m/d ln a = -(3+alpha) rho_m - beta rho_v`,

`d rho_v/d ln a = alpha rho_m + beta rho_v`.

Matrix form:

`y'=M y`,

`M=[[-(3+alpha),-beta],[alpha,beta]]`.

Eigen-exponents:

`lambda_+- = [-(alpha-beta+3) +- S]/2`,

`S=sqrt[(alpha+beta+3)^2-4 alpha beta]`.

At `alpha=beta=0`:

`rho_m=rho_m0 a^-3`, `rho_v=rho_v0`.

Experiment 013 compared the transcribed analytic solution with direct ODE integration; maximum normalized discrepancy is about `5.9e-12` over tested controls.

### Perturbations / gauge restriction (Experiment 016)

The explicit IDM_IV perturbation path in this pinned fork is **not supported in Newtonian gauge**. Use synchronous gauge for the control.

There the zero-coupling density equation reduces exactly to pressureless CDM, and upstream adiabatic IC assign the same `delta=3/4 delta_gamma`.

The authoritative intended zero-coupling configuration is upstream `test_idm_iv_lcdm.ini`:

- `alpha_idm_iv=0`
- `beta_idm_iv=0`
- `f_idm_iv=1`
- `f_iv=1`
- synchronous gauge
- `fluid_equation_of_state=IDM_IV` intentionally commented out (explicit separate-component path).

### Upstream compile caveat discovered during IDE-S1

The exact pinned commit does not compile unmodified on the clean runner. In `background_w_fld()` a premature closing brace immediately after the EDE branch leaves the subsequent `case IDM_IV` outside its switch, causing `case label not within a switch statement`.

This is an upstream syntax defect, **not** a physical result.

Calibration PR #2 (`calibration/ide-zero-limit-001`) therefore uses

`patches/apply_class_iv_ac627d54_compile_fix.py`

which:

1. requires the exact pinned source context to occur once;
2. removes exactly the single premature brace;
3. checks that the number of `case IDM_IV` labels is unchanged;
4. checks the edit size;
5. records the resulting `git diff` and repair-script SHA256;
6. changes no cosmological equation or coefficient.

**IDE-S1 remains OPEN until this repaired pinned source builds and the full zero-coupling spectra/background comparison is evaluated.**

---

## 4. GDM zero closure — source result

Pinned upstream:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

At all-zero closure:

`w=ca2=cs2=cv2=0`,

`rho_gdm(a)=rho_gdm0 a^-3`.

The non-adiabatic pressure term is

`Pi_nad=(cs2-ca2)[delta+3 Hconformal(1+w) theta/k^2]`,

hence `Pi_nad=0`.

The GDM continuity/Euler equations reduce to pressureless CDM when shear is zero. Dynamic shear obeys

`shear'=-3 Hconformal shear + (8/3) cv2/(1+w)(theta+M_shear)`,

so `cv2=0` preserves zero shear. Leading adiabatic IC reduce to CDM.

**GDM-S0 PASS.**

---

## 5. GDM finite-start failure mode

When GDM is enabled, the pinned solver uses an IC branch that omits several standard matter-radiation corrections proportional to `omega*tau`.

For the isolated photon-density example:

`delta_gamma_CLASS = -(k tau)^2/3 (1-omega tau/5) R`,

`delta_gamma_GDMbranch = -(k tau)^2/3 R`.

The local asymptotic discrepancy in that term is therefore `omega tau/5`.

However, a full-solver sweep of

`start_small_k_at_tau_c_over_tau_h={1e-6,3e-7,1e-7,3e-8}`

showed that decreasing this single parameter below `1e-6` **does not monotonically improve** the complete calculation and eventually worsens it. Therefore do not interpret this precision parameter as an independent `earlier = better` knob and do not tune a regression tolerance with it.

Working start remains `1e-6`.

---

## 6. GDM high-precision clean-room result

At fixed start `1e-6`, stronger pinned-solver precision settings substantially reduce the zero-GDM/CDM residual on working scales.

Scale-aware p1 artifact gives approximately (tested z output):

| k cut [h/Mpc] | max |Delta P/P| |
|---:|---:|
| >= 1e-4 | 1.10e-2 |
| >= 1e-3 | 8.28e-4 |
| >= 1e-2 | 5.55e-4 |
| >= 0.03 | 1.44e-4 |
| >= 0.05 | 3.89e-5 |
| >= 0.1 | 2.82e-5 |
| >= 0.5 | 1.67e-5 |

The median residual is much smaller than the maximum in most working-scale windows. Background quantities agree to numerical/interpolation accuracy.

The global fractional P(k) maximum is **not** a useful calibration statistic because it is dominated by very small `k~1e-5 h/Mpc`, where the pinned zero-closure IC branch is known to be finite-start sensitive and P is tiny. Track that sector separately.

Main CMB auto/lensing spectra are also close in peak-normalized metrics; local ratios near sign/zero crossings of cross spectra are not used as standalone tolerance metrics.

**GDM-S1 still OPEN:** a precision-convergence plateau must be demonstrated before freezing a hard tolerance.

A matrix workflow `gdm-precision-sweep.yml` was launched. Its first p2/p3/p4 jobs were terminated by GitHub runner shutdown (`exit 143`), not by solver/scientific failure. They must be rerun unchanged; do not classify those interrupted jobs as failed physics.

---

## 7. Exact continuation sequence

1. Finish unchanged GDM precision p2, p3, p4 reruns and collect `physics_windows.json` artifacts.
2. Compare p1->p4 in the frozen linear k core and primary CMB auto/lensing metrics. Determine whether a numerical plateau exists.
3. Freeze GDM-S1 tolerance **from convergence behavior**, not from desired PASS outcome; record tolerance/version in provenance.
4. Finish IDE PR #2 build with the assertion-checked compile-only source repair; inspect full zero-coupling background, P(k), CMB/lensing outputs.
5. If IDE numerical zero limit is stable, freeze IDE-S1 tolerance and provenance.
6. Build the first complete six-family response matrix in `dsir-response-v0.1` coordinates: LambdaCDM, smooth wCDM/quintessence-like, thermal WDM, designer-f(R), GDM, interacting vacuum.
7. Project exact identities/nuisance directions, transform covariance consistently, whiten, then estimate `R_model(pi)` across defensible family priors.
8. Only after the common matrix and observational projection are stable should G7 residual-law search resume.

**Never claim discovery before G8 withheld prediction.**
