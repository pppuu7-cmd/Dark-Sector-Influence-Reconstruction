# DSIR RECOVERY LATEST — live overlay

**Date:** 2026-08-24  
**Read first:** `docs/RECOVERY_MANUAL.md`  
Then read this file, `docs/GATES.md`, `docs/STATUS.md`, `docs/RESEARCH_LOG.md`, `docs/PROVENANCE.md`, `docs/CONSERVATION_GAUGE_V0_1.md`, `docs/NOVELTY_AUDIT_N0.md`, and the response-basis specifications.

Hard boundary: **DSIR is separate from RTK. Do not modify, use, or overwrite the RTK repository/project while continuing DSIR.**

---

## 1. Current gate state

- **N0 PASS-PROVISIONAL:** prior-art/non-duplication audit found extensive precedent for individual ingredients but no exact duplicate of the complete DSIR chain. This is not proof of global novelty. `docs/NOVELTY_AUDIT_N0.md` and `config/novelty_prior_art_n0.json` are authoritative for novelty wording.
- **N1 OPEN:** citation-graph/full-text audit of the closest competitors is required before manuscript-level claims such as “first”, “new framework”, or “novel methodology”.
- **G1 PASS for v0.1.1 scope:** conservation/Bianchi bookkeeping and a gauge-safe common total-matter construction are validated. Newtonian/synchronous comoving hard gate passed.
- **G2 PASS v0.1.1:** response basis upgraded from ambiguous raw `P_m` to explicit comoving total-matter `P_Delta` with same-solver reference quotients. Cross-solver hard bridge passed.
- **GDM-S0/S1 PASS.**
- **IDE-S0/S1 PASS.**
- **G3B PARTIAL:** common perturbation coordinate is ready, but the historical BZ-like f(R) control is only QS-safe on part of the k grid. A full designer-f(R) solver is now the main blocker to the first complete six-family matrix.
- **G7 OPEN:** no new residual dark-sector law is claimed.
- **G8 OPEN:** no discovery claim before a withheld-observable prediction.

---

## 2. Production response basis v0.1.1

Files:

- `config/response_basis_v0_1_1.json`
- `docs/RESPONSE_BASIS_V0_1_1.md`
- `experiments/018_solver_comoving_matter_source_audit.md`
- `experiments/020_cross_solver_response_bridge.md`
- `src/dsir/response_basis.py`
- `tests/test_response_basis_v011.py`

### Background coordinate

Retain the v0.1 anchored expansion response

\[
r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{\rm ref}(z)/H_{\rm ref}(z_*)}\right],
\qquad z_*=0.51.
\]

Frozen z nodes:

`{0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

A common multiplicative H calibration cancels.

### Gauge-safe matter variable

For the documented total-matter component set,

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},
\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\qquad
w_m=\frac{p_m}{\rho_m}.
\]

Use the comoving total-matter density contrast

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}},
\qquad {\cal H}=aH.
\]

For stable pressureless matter:

\[
\Delta_m=\delta_m+3{\cal H}\theta_m/k^2.
\]

The production perturbation response is

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_\Delta^{\rm model,S}(k,z)}{P_\Delta^{\rm ref,S}(k,z)}}
\]

with

\[
P_\Delta=P[\Delta_m].
\]

`S` means the **same solver lineage and matched numerical settings** for model and reference whenever possible. Do not compare absolute spectra from different solver vintages as a dark-sector response.

Frozen linear k nodes:

`{0.001,0.003,0.01,0.03,0.1} h/Mpc`.

`k<0.001 h/Mpc` remains a separate GDM finite-start/IC diagnostic sector.

---

## 3. Why v0.1 was reopened and how the issue was resolved

An identical CDM cosmology was run in pinned GDM_CLASS with only the gauge changed.

At default precision, raw `mPk` differed by up to

`9.8434e-5`

inside the frozen linear core. This was too large relative to the solver zero-limit floors, so G2 was correctly reopened instead of treating the difference as physics.

At p8 precision raw `mPk` gauge mismatch fell to roughly `5.1e-6`.

An explicit reconstruction of

`Delta_m=delta_m+3 Hconf theta_m/k^2`

for pressureless matter reduced the p8 Newtonian/synchronous mismatch to

`2.5514e-6`.

A hard tolerance

`max gauge mismatch <= 5e-6`

was frozen before the final rerun and passed.

Interpretation: the original `~1e-4` mismatch was a mixture of gauge-sensitive transfer quantities and numerical precision. Production DSIR therefore names and audits the comoving source explicitly rather than relying on ambiguous `P_m` labels.

---

## 4. Source-level compatibility of the two CLASS-family solvers

### GDM_CLASS

Pinned:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Its total-matter source explicitly uses the generalized comoving correction

`delta_m += 3*(1+P_m/rho_m)*a*H*theta_m/k^2`.

Thus nonzero GDM matter pressure is handled with the required `(1+w_m)` factor. At zero closure it reduces to the pressureless formula.

### class_iv

Pinned:

`kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

The explicit interacting matter component enters total matter as

`delta_rho_m += rho_idm_iv * delta_idm_iv`

and, when its velocity degree of freedom exists,

`rho_plus_p_theta_m += rho_idm_iv * theta_idm_iv`.

The code then forms `theta_m` and applies

`delta_m += 3*a*H*theta_m/k^2`.

At zero coupling in synchronous gauge the IDM_IV velocity is the comoving pressureless value zero.

### class_iv synchronous vTk header defect

The pinned fork has an output-label bug: in synchronous gauge no active `theta_idm_iv` source column is written, but `perturb_output_titles()` still inserts a velocity-block label named `d_idm_iv`. Subsequent velocity titles are therefore shifted by one column.

This does **not** affect the internal total-matter `mPk` source or IDE-S1. Species-level synchronous `vTk` from this fork is diagnostic only unless index order is recovered from source or the header is repaired and regression-tested.

---

## 5. Cross-solver response bridge — Experiment 020

Purpose: test whether same-solver response quotients remove code-lineage differences for a real nonzero deformation.

For each solver `S`:

\[
r_S=\ln(P_{w\mathrm{CDM}}^S/P_{\Lambda\mathrm{CDM}}^S)
\]

with common physical deformation

`w0=-0.9`, `wa=0`, `cs2=1`, matched cosmological parameters and frozen z/k nodes.

Then compare

\[
\Delta r_{\rm bridge}=r_{GDM\_CLASS}-r_{class\_iv}.
\]

### Calibration A: asymmetric precision

GDM_CLASS p8 versus class_iv default precision:

`max |Delta r_bridge| = 1.0474971491e-5`.

Largest discrepancies were concentrated at high k.

### Calibration B: identical p8 precision

Applying the same p8 precision preset to both lineages collapsed the residual to

\[
\boxed{\max|\Delta r_{\rm bridge}|=2.3747404043\times10^{-10}}.
\]

The physical response itself reaches about `5.0204e-2`, so the bridge residual is roughly `4.7e-9` of the signal amplitude.

### Hard gate

Before the final rerun DSIR froze

\[
\boxed{\max|\Delta r_{\rm bridge}|\le10^{-9}}.
\]

The clean hard regression passed, including the final repeat on PR #3 before merge into `main`.

Scope: this validates the response-quotient architecture for this overlapping smooth-wCDM deformation. It does not assert that all solvers/theories agree universally to `1e-9`.

---

## 6. Solver-specific zero limits already closed

### GDM-S1 PASS

Fixed start `start_small_k_at_tau_c_over_tau_h=1e-6`. Earlier-start-only sweep was non-monotonic and rejected as a tolerance-tuning method.

Precision p1->p8 reduced the full linear-core zero-GDM/CDM residual. A hard threshold

`max |Delta P/P| <= 5e-6`

was frozen before final p8 rerun; actual hard maximum was

`1.471014806e-6`.

### IDE-S1 PASS

Pinned class_iv needs a provenance-tracked compile-only repair removing exactly one premature brace plus legacy `-fcommon` and `--no-as-needed` linker semantics. No cosmological equation is changed.

Hard tolerances frozen before rerun:

- linear-core power `<=2e-8`;
- semantic background `<=2e-12`.

Both passed.

---

## 7. Modified-gravity control: current blocker

Historical `src/dsir/linear_controls.py` includes a BZ-like quasi-static f(R) toy. Experiment 019 audits its domain with

\[
\frac{k}{aH/c}.
\]

Minimum over the frozen redshift grid is approximately:

| k [h/Mpc] | min k/(aH/c) |
|---:|---:|
| 0.001 | 2.9 |
| 0.003 | 8.7 |
| 0.01 | 29 |
| 0.03 | 87 |
| 0.1 | 291 |

Therefore the BZ-like QS toy is **not** a production control at `k=0.001,0.003`. Provisional QS comparison is restricted to `{0.01,0.03,0.1}`.

The next full-MG candidate is official **H-EFTCAMB**, branch `eftcamb`, pinned initially at

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

The upstream designer-f(R) test uses

- `EFTflag=3`
- `DesignerEFTmodel=1`
- `EFTwDE=0` (LambdaCDM background)
- `EFTB0` as the designer-f(R) amplitude.

Do not use it in the production matrix until DSIR establishes its GR/small-`B0` control limit and response extraction.

---

## 8. Novelty contract after N0

Authoritative files:

- `docs/NOVELTY_AUDIT_N0.md`
- `config/novelty_prior_art_n0.json`

N0 explicitly establishes that these **cannot** be claimed as DSIR inventions:

- effective dark-sector stress tensor / moving MG to an effective source;
- dark degeneracy and non-uniqueness of DM/DE decomposition;
- GDM `(w,c_s^2,c_vis^2)` stress closure;
- PPF/EFT common theory dictionaries;
- PCA/SVD of representative cosmological/MG theory banks;
- entropy effective-rank formula;
- target/reference or LambdaCDM reaction ratios;
- model-independent reconstruction of interacting dark-sector functions;
- symbolic regression in dark-energy/cosmological reconstruction;
- organizing LambdaCDM as a point/fixed point in dark-sector theory space.

The current provisional DSIR-specific combination is:

`heterogeneous DM+DE+interaction+MG atlas`
` -> common observable response`
` -> same-solver quotient + cross-solver bridge`
` -> covariance whitening/noise calibration`
` -> R_model(pi) prior sensitivity`
` -> quotient of identities/calibration/measurement degeneracies`
` -> cross-channel law discovery`
` -> withheld physical-channel prediction`.

This is only a **methodological novelty hypothesis**. N1 remains OPEN and can still force a reframe.

The closest conceptual competitor identified in N0 is the July-2026 paper **“LambdaCDM as a fixed point: Controlled dark-sector deformations and late-time structure growth”**, which organizes controlled dark-sector deformations around LambdaCDM and maps them into late-time growth/lensing observables. Never claim DSIR is the first “dark-sector theory space”.

---

## 9. Rank/law-discovery rules that remain mandatory

Before any rank claim:

\[
Z=C^{-1/2}\Delta O,
\qquad Z=U\Sigma V^T.
\]

No unwhitened rank claim is allowed. Experiment 011 recovered injected rank 3 in 30/30 whitened cases while naive raw-space calibration produced false ranks 20–35.

Theory-catalog sampling is an implicit prior, so report

\[
R_{model}(\pi)
\]

rather than one prior-free-looking number. Experiment 012 showed a 900/90/10 family multiplicity can hide a real third mode.

Exact identities/Bianchi relations, calibration modes and measurement-induced degeneracy directions are quotiented before law discovery.

For observational conditional innovation use

\[
r_t^\perp=r_t-C_{tN}C_{NN}^{-1}r_N.
\]

Current DESI DR1 corrected ShapeFit aggregate remains null-consistent:

`chi2~5.53/5`, `p~0.355`.

Therefore **G7 is OPEN**.

---

## 10. Exact continuation sequence

1. Treat response basis v0.1.1 as merged/frozen in `main` at merge commit `71297dd1d73d9b3846d47a4d77c81b193cf584b8`.
2. Keep novelty work isolated in `research/novelty-n0` / PR #4 until reviewed; N0 is PASS-PROVISIONAL and N1 remains OPEN.
3. Create a separate MG research branch from updated `main`.
4. Clean-build pinned H-EFTCAMB `eftcamb@16d9c4e9...` with recursive submodules.
5. Run an author-provided designer-f(R) smoke test.
6. Establish **MG-S0** by comparing GR with a sequence of designer `EFTB0 -> 0` values; do not choose the tolerance after seeing the desired production point.
7. Choose a nonzero, stable designer-f(R) control and compute its same-solver `r_Delta(k,z)` on all frozen nodes.
8. Compare H-EFTCAMB full response with the old BZ-like toy only on the QS-safe `{0.01,0.03,0.1}` sub-block; disagreement at lower k is not a toy failure because the toy is out of domain there.
9. Assemble the first genuinely common six-family response matrix: LambdaCDM, smooth wCDM/quintessence-like, thermal WDM, full designer-f(R), GDM, interacting vacuum.
10. Project identities/nuisance modes, transform covariance consistently, whiten, and estimate `R_model(pi)` over defensible theory-family priors.
11. Resume G7 nonlinear/invariant/symbolic-law search only after matrix stability checks.
12. A candidate law must predict a withheld channel before G8 can pass.
13. Before any manuscript novelty claim, complete N1 citation-graph/full-text audit and rerun the novelty search immediately before preprint submission.

**Never claim discovery before G8. Never claim broad methodological novelty before N1.**
