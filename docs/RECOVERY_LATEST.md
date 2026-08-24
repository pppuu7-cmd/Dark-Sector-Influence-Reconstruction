# DSIR RECOVERY LATEST — live overlay

**Date:** 2026-08-24  
**Read after:** `docs/RECOVERY_MANUAL.md`

This is the authoritative live delta to the long recovery manual. Then read `docs/GATES.md`, `docs/STATUS.md`, `docs/CONSERVATION_GAUGE_V0_1.md`, `docs/RESPONSE_BASIS_V0_1_GAUGE_ERRATUM.md`, `docs/RESEARCH_LOG.md` and `docs/PROVENANCE.md`.

Hard boundary: **do not modify/use RTK as a DSIR prior.**

---

## 1. Current gate state

- **G1 PARTIAL:** conservation/Bianchi bookkeeping contract is frozen, but a gauge-safe common perturbation coordinate is not yet fully validated across solver families.
- **G2 REOPENED:** Experiment 017 background/identity conventions remain valid; raw solver `mPk` is rejected as a common cross-gauge perturbation coordinate. Successor basis v0.1.1 is under construction.
- **GDM-S0 PASS; GDM-S1 PASS.**
- **IDE-S0 PASS; IDE-S1 PASS.**
- **G3B PARTIAL:** solver-specific embeddings are ready, but the common six-family perturbation matrix is blocked by G1/G2.
- **G7 OPEN:** no residual dark-sector law claimed; law search is blocked until the perturbation coordinate is repaired.
- **G8 OPEN:** no discovery claim is permitted before withheld prediction.

---

## 2. Response basis v0.1: what survives and what is blocked

Historical machine schema: `config/response_basis_v0_1.json`  
Historical human spec: `docs/RESPONSE_BASIS_V0_1.md`  
Gauge erratum: `docs/RESPONSE_BASIS_V0_1_GAUGE_ERRATUM.md`

Still valid:

- anchored relative expansion
  `r_E(z;z*)=ln[(H(z)/H(z*))/(H_ref(z)/H_ref(z*))]`, `z*=0.51`;
- frozen z nodes `{0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- fixed primordial normalization rule;
- AP identity bookkeeping `r_FAP=r_DM+r_H`;
- covariance-metric amplitude quotient;
- frozen linear domain `k={0.001,0.003,0.01,0.03,0.1} h/Mpc` as working support.

Blocked implementation:

`r_P=ln[P_m/P_m,ref]` **must not be populated with raw solver `mPk` across families that use different gauges.**

Reason: identical LambdaCDM cosmology in the same pinned GDM_CLASS code, changing only Newtonian versus synchronous gauge, differs by up to `9.8434e-5` in raw `mPk` over `1e-3<=k<=1e-1 h/Mpc`. This is much larger than solver zero-limit tolerances.

G2 was therefore correctly reopened rather than hiding the mismatch.

---

## 3. GDM zero-limit status — S1 PASS

Pinned upstream:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Source zero closure remains:

`w=ca2=cs2=cv2=0`, `rho_gdm~a^-3`, `Pi_nad=0`, pressureless CDM continuity/Euler limit, zero dynamic shear preserved, leading adiabatic IC match CDM.

Finite-start negative control:

`start_small_k_at_tau_c_over_tau_h={1e-6,3e-7,1e-7,3e-8}` showed that making this single start parameter smaller does **not** monotonically improve the full calculation. Do not tune tolerance with it. Working start remains `1e-6`.

Linear-core precision calibration p1->p8 at fixed start was then performed. Full-core maxima on `1e-3<=k<=1e-1 h/Mpc` include approximately:

- p1 `5.93e-4`
- p2 `1.79e-4`
- p3 `8.43e-5`
- p4 `3.66e-5`
- p5 `1.63e-5`
- p6 `4.70e-6`
- p7 `2.96e-6`
- p8 `1.47e-6`

The location of the maximum moves with precision, supporting a numerical-floor interpretation rather than a stable physical residual.

A conservative hard tolerance was frozen **before** the final hard rerun:

`max |Delta P/P| <= 5e-6` for `1e-3<=k<=1e-1 h/Mpc`.

The p8 hard run passed with actual

`global_linear_core_max_abs_relative = 1.471014806e-6`.

**GDM-S1 PASS.**

`k<1e-3 h/Mpc` remains a separate finite-start/IC-sensitive diagnostic sector and is not discarded.

---

## 4. Interacting-vacuum zero-limit status — S1 PASS

Pinned upstream:

`kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Source convention:

`Q/H = alpha rho_m + beta rho_v`,

`d rho_m/d ln a = -(3+alpha)rho_m - beta rho_v`,

`d rho_v/d ln a = alpha rho_m + beta rho_v`.

Internal transfer cancels exactly on addition:

`d(rho_m+rho_v)/d ln a = -3 rho_m`.

At `alpha=beta=0`, matter is pressureless and vacuum constant. The explicit perturbation path is supported only in synchronous gauge in this pinned fork.

### Pinned-source compatibility caveats

The exact upstream pin contains one premature closing brace before `case IDM_IV`; it also assumes legacy compiler/linker behavior. DSIR uses:

- assertion-checked removal of exactly that one brace;
- `-fcommon` for old tentative-global semantics;
- `-Wl,--no-as-needed` with GSL libraries.

These are provenance-tracked source/toolchain compatibility adaptations; no cosmological equation/coefficient is changed.

Two clean-room calibrations established the numerical floor. Before the final hard run the following tolerances were frozen:

- linear-core `max |Delta P/P| <= 2e-8` on `1e-3<=k<=1e-1 h/Mpc`;
- semantic-background peak-normalized mismatch `<=2e-12`.

The hard run passed both gates on

`z={0,0.295,0.51,0.706,0.934,1,1.317,1.491,2.33}`.

Semantic background includes

`rho_cdm^(LCDM)=rho_cdm^(IDE)+rho_idm_iv^(IDE)`

at about `8.1e-13` worst relative active discrepancy and `rho_Lambda=rho_iv` at output precision.

**IDE-S1 PASS.**

---

## 5. G1 conservation/gauge contract

Controlling document: `docs/CONSERVATION_GAUGE_V0_1.md`.

For internal interactions:

`nabla_mu T_i^{mu nu}=Q_i^nu`,

`sum_i Q_i^nu=0`,

therefore

`nabla_mu T_tot^{mu nu}=0`.

Exact Bianchi/conservation identities are projected before rank estimation, not rediscovered as laws.

At first order the convention-independent gauge rule is

`delta T -> delta T - L_xi Tbar`.

Therefore raw gauge-specific density, velocity and metric perturbations are forbidden as common cross-family coordinates without an explicit invariant mapping.

---

## 6. Raw matter-power gauge audit — negative result

Same pinned GDM_CLASS code, identical LambdaCDM parameters, identical output settings; only gauge changed:

`newtonian` versus `synchronous`.

Result on `1e-3<=k<=1e-1 h/Mpc`:

`max raw-mPk gauge difference = 9.843415778e-5`.

This is about twenty times the frozen GDM-S1 tolerance and orders of magnitude above the IDE-S1 floor.

**Conclusion:** raw solver `mPk` is rejected as the common six-family perturbation coordinate.

This is an anti-artifact success of G1, not a failure of either physical model.

---

## 7. Candidate gauge-invariant/comoving matter response — current active work

The transfer-level audit outputs `d_i=delta rho_i/rho_i` and `t_i=theta_i` in both gauges. In synchronous CDM-comoving gauge `t_cdm` is absent, i.e. CDM velocity is zero by gauge choice.

From the actual Newtonian/synchronous transfer outputs, the empirical transformation coefficient

`[(delta_m^syn-delta_m^Newt) k^2] / [Hconf (theta_m^Newt-theta_m^syn)]`

approaches `3` on the well-conditioned low-k core points. This independently fixes the candidate sign/coefficient in the pinned convention:

`Delta_m = delta_m + 3 Hconf theta_m/k^2`,

with `Hconf=aH` and `k` converted from `h/Mpc` to `1/Mpc`.

At default solver precision this reduces the huge raw density-gauge difference but leaves a residual around `5e-5`, consistent with needing a precision-controlled audit rather than immediately promoting the formula.

Active branch workflow:

`.github/workflows/gauge-transfer-audit.yml`

now runs the same candidate at the p8 precision used by the GDM-S1 hard gate. Script:

`ci/gauge_invariant_matter_audit.py`.

No gauge tolerance has yet been frozen. First measure the p8 invariant floor, then freeze a tolerance, then rerun as a hard gauge gate.

---

## 8. Exact continuation sequence

1. Read the p8 `comoving_gauge_audit.json` artifact from the transfer-level Newtonian/synchronous run.
2. If `Delta_m` gauge residual collapses substantially below raw `mPk`, repeat/calibrate as needed and freeze a gauge tolerance **before** the final hard rerun.
3. If the hard gauge gate passes, create response-basis **v0.1.1** without rewriting historical v0.1; use a response derived from the validated comoving matter quantity.
4. Build the same transfer/invariant extractor for repaired pinned `class_iv` and verify its zero-coupling response against the common LambdaCDM invariant definition.
5. Only after cross-solver compatibility passes, re-close G2 and G1-GAUGE.
6. Build the first genuinely common six-family response matrix: LambdaCDM, smooth wCDM/quintessence-like, thermal WDM, designer-f(R), GDM, interacting vacuum.
7. Project exact identities/nuisance directions, transform covariance consistently, whiten, and estimate `R_model(pi)` across defensible family priors.
8. Resume G7 residual-law search only after that matrix is stable.
9. Never claim discovery before G8 withheld prediction.
