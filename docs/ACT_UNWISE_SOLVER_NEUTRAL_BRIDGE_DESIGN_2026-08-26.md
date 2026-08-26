# ACT DR6 × unWISE solver-neutral DSIR bridge design

Date: 2026-08-26
Status: design constraint recorded during Exp065A; not a scientific result and not a G7 closure claim.

## Motivation from existing DSIR evidence

Exp032/033 established a hard theory-space separator inside C3 GDM: sound-speed and viscosity rays remain nearly collinear in low-k matter power and Weyl amplitude, but rotate strongly in metric slip. That result explicitly stopped short of observational distinguishability because no survey kernel/covariance was applied.

Exp064A/F31 then rejected the simplest covariance-aware AP/growth/shape plane inside the five-bin DESI ShapeFit block. Therefore the next admissible route is to add a genuinely independent lensing/Weyl-sensitive measurement operator rather than increase flexibility on the same ShapeFit points.

## Why the official ACT × unWISE projector is structurally compatible

Pinned external source:

`ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

Its `unWISExkappa_model.py::compute_raw_spectra` accepts three physical spectra:

- `pk_weyl_weyl` — Weyl-potential auto power;
- `pk_weyl_dnonu` — Weyl × non-neutrino matter cross power;
- `pk_dnonu_dnonu` — non-neutrino matter auto power.

It projects those inputs through the CMB-lensing kernel, galaxy redshift distributions and angular geometry into raw `C_ell^{kappa g}` and `C_ell^{gg}` components. The official likelihood then applies its nuisance construction, transfer functions, band-window matrices and covariance.

This is a better DSIR bridge than a hand-made `C_ell^{kappa g}/C_ell^{gg}` ratio because bias, magnification, redshift-distribution PCs, transfer functions and correlated covariance are part of the declared measurement operator rather than silently cancelled.

## Solver-neutral interface required for the next experiment

The DSIR wrapper must not depend on CAMB object identity. It should expose, on a declared `(z,k)` support,

1. background geometry sufficient for `chi(z)`, `H(z)`, `Omega_m`, `H0`, and last-scattering distance used by the kappa kernel;
2. `P_WW(k,z)` in the exact Weyl normalization expected by the ACT projector;
3. `P_Wm(k,z)` with the same Weyl normalization and the declared matter species convention;
4. `P_mm(k,z)` for the same matter convention;
5. interpolation/extrapolation masks, with no zero filling outside valid support.

The convention bridge must be proved by a reference cosmology before any DSIR-family comparison. In particular, CLASS `phi/psi` transfer conventions may not be inserted as CAMB `Weyl` power without an explicit normalization/sign/unit audit.

## Required reference-reproduction gate before law search

A future Exp066A should be a **forward-operator reproduction audit**, not a model-law test. On one pinned reference cosmology it should compare a DSIR solver-neutral implementation against the official ACT implementation at multiple levels:

- raw `C_ell^{gg}` and `C_ell^{kappa g}` before transfer/binning;
- transferred/binned bandpowers;
- assembled data-vector ordering;
- covariance quadratic form / log-likelihood contribution for at least one fixed nuisance point.

Tolerances must be frozen before the comparison. Any discrepancy must be diagnosed as background, Weyl normalization, matter-species convention, non-linear prescription, nuisance model, transfer, binning, or covariance ordering. No family response should be interpreted until this reference bridge passes.

## Non-linear and nuisance caution

The official code can request nonlinear `Weyl/Weyl`, `Weyl/delta_nonu`, and `delta_nonu/delta_nonu` interpolators and includes CLEFT/bias, magnification and clustering-redshift corrections. DSIR must not claim a model-agnostic observational bridge by applying a GR-calibrated nonlinear prescription to arbitrary modified-gravity/interacting models without a validity declaration.

Therefore the first cross-channel law search should either:

- freeze a conservatively linear/quasi-linear multipole domain where the selected solver/model prescriptions are valid, or
- explicitly carry a model-specific nonlinear-validity mask.

## Gate semantics

Exp065A only decides whether the public ACT×unWISE release has enough immutable data/operator/covariance content to be eligible. Even an Exp065A PASS leaves G7/G8/G9 OPEN. Exp066A would only establish a trustworthy solver-to-survey bridge. A genuine G7 candidate still requires a separately frozen residual law, nuisance quotient, null control and withheld test.