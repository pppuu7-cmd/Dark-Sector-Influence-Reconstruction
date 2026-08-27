# Exp073J — KiDS bandpower operator pre-output binding v0.1

**Date frozen:** 2026-08-27  
**Status:** BOUND BEFORE ANY KiDS-BNT SUPPORT FRACTION IS EVALUATED

## Purpose

This binding resolves the exact released KiDS bandpower-filter semantics needed by the already-preregistered Exp073J KiDS-BNT `Wm/WW` support audit. It does not change the common physical rectangle, the `5%` threshold, the minimum final retained dimension `15`, the BNT row selection, or any scientific classification rule.

## Immutable source

Use only `KiDS-WL/Cat_to_Obs_K1000_P1@36676da44471979dacb779155d7e6e7212ae1f4f` for the released bandpower operator:

- `src/bandpowers/xi2bandpow.c`, previously bound SHA256 `3a2311c06432b131696caa9c8cd46799fd85f8316335cad6dc76a4d8eee92e7a`;
- `Calc_2pt_Stats/doall_calc2pt.sh`, previously bound SHA256 `9e0d67d7def7a626a47f92bc422a17a2ad79438d1a361959950259af56e752be`.

No covariance file is part of this binding.

## Exact released arguments

The pinned master script fixes the production bandpower settings to:

- 8 logarithmic output ell bins;
- `ell_min=100`, `ell_max=1500`;
- nominal angular range `theta_min=0.5 arcmin`, `theta_max=300 arcmin`;
- apodisation enabled with `logwidth=0.5`;
- correlation type `corrtype=2` for galaxy-galaxy lensing (`Pgk`);
- correlation type `corrtype=1` for cosmic shear (`Pkk`).

The input correlation functions are finely sampled in 326 logarithmic theta bins spanning approximately `0.37895134266193781--395.82918204307509 arcmin`, so the apodised 0.5--300 arcmin support is explicitly covered.

## Exact transformation semantics

The pinned C implementation constructs logarithmic ell boundaries

`ell_bound[i] = ell_min * exp(i*log(ell_max/ell_min)/NOUT)`

and evaluates analytic integrated Bessel kernels at both boundaries. It does not use a top-hat at an effective ell or a band centre approximation.

For each input theta bin it computes the finite theta-bin width and the transformation-matrix coefficient. The relevant analytic primitives are:

- shear xi+ kernel: `K_ee(x,+) = x J1(x)`;
- shear xi- kernel: `K_ee(x,-) = (x-8/x) J1(x) - 8 J2(x)`;
- GGL gamma_t kernel: `K_ne(x) = -x J1(x) - 2 J0(x)`.

The apodisation is a prospectively fixed cos^2 taper in log(theta), with total logarithmic width `0.5`, applied around the nominal lower and upper theta boundaries.

For cosmic shear the E-mode bandpower combines xi+ and xi- through the exact transformation matrix. The default E-mode balance is `pfrac=0.5` unless an explicit `xi2bandpow_pmweights_<ident>.dat` file is present. A future evaluator must reproduce the released execution path and record whether such a pmweights file is actually supplied for the bound production vector; it may not assume a different balance.

For GGL the E/tangential bandpower uses the exact `corrtype=2` transformation. The cross/B-mode output is not a substitute for the signed physical `P_Wm`; support is evaluated with a non-negative operator envelope while the later physical forward model must preserve signed `P_Wm` semantics.

## Support-evaluator rule

The Exp073J support evaluator must derive its angular support from these exact released transformation semantics before combining with the prospectively frozen BNT transform and the line-of-sight kernels. It must not replace them by:

- effective ell;
- top-hat ell bins;
- delta-function theta or ell support;
- a covariance-weighted filter;
- a posterior/fiducial `P(k)` weighting;
- support clipping chosen after looking at leakage.

The non-negative support envelope may use absolute values of the complete linear operator coefficients only after the exact operator composition is established. Any required discretisation in ell/theta/z must be convergence-tested without changing the frozen 5% criterion.

## Downstream boundary

No KiDS-BNT support fraction, retained coordinate count, covariance value, nuisance rank/SVD, quotient/relation/null, held-out result or G8 information has been evaluated here.

The next implementation step is to reproduce the released KiDS angular-filter operator numerically, verify source hashes and deterministic/convergence controls, then compose it with BNT rows `[2,3,4]` and the exact lens/source n(z) kernels for the Wm/WW physical-support audit.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
