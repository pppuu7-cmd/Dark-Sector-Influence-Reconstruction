# Exp073L — KiDS absolute-response extended asymptotic result v0.1

**Date:** 2026-08-27  
**Scientific classification:** `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`

## Immutable provenance

- frozen parent: Exp073K = `INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K`;
- implementation/head bound by the workflow artifact: `1c7064bf88afb868af7691eb33520c165ac3a245`;
- workflow run: `33049366874`;
- artifact: `9637070322`;
- artifact digest: `sha256:03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684`;
- extracted result JSON SHA256: `000d45efd38c4e7b0b1bc2d5b9b1656809d60e73adb0d42bc76220161daedb78`;
- KiDS source pin: `36676da44471979dacb779155d7e6e7212ae1f4f`;
- `xi2bandpow` SHA256: `3a2311c06432b131696caa9c8cd46799fd85f8316335cad6dc76a4d8eee92e7a`.

The CI job completed successfully and all frozen P1–P4 controls passed. This is therefore a scientific asymptotic result, not an infrastructure failure.

## Frozen test and result

The preregistered primary ladder was

`ell_max = [120000, 240000, 480000]`

with the unchanged Exp073K non-normalizable box:

- final local exponent in `[1.35,1.65]`;
- final dyadic shell fraction in `[0.55,0.75]`;
- strictly increasing positive normalization;
- final shell fraction at least `0.10`.

Result:

- Wm/GGL: `8/8` bands satisfy the non-normalizable box;
- WW/shear: `8/8` bands satisfy the non-normalizable box;
- finite-saturation count: `0/8` for Wm and `0/8` for WW.

Final local exponents cluster tightly around the expected `p≈3/2` behavior:

- Wm range: approximately `1.4944 ... 1.5180`;
- WW range: approximately `1.4927 ... 1.5157`.

Final `240000 -> 480000` positive shell fractions remain approximately `0.6446 ... 0.6508`, far from saturation and close to `1-2^(-3/2)=0.646446...`.

The preregistered `Delta ell=0.5` convergence checks for Wm bands 0/6/7 and WW bands 0/6/7 all pass. The largest relative half-step discrepancy is below `2e-6`, versus the frozen `5e-3` tolerance.

## Scientific interpretation

For the released finite-theta KiDS `xi2bandpow` estimator, the P-independent absolute-response normalization used by Exp073J does not approach a finite cutoff-independent value. The extended ladder supports the discrete finite-theta endpoint/node mechanism already indicated by Exp073J/K: the absolute response grows approximately as `ell_max^(3/2)`.

This is a negative result for the attempted **absolute positive-support definition of this released operator**. It is not a failure of KiDS cosmology, BNT, GDM, designer-f(R), or DSIR.

Exp073K remains permanently `INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K`; Exp073L is an independent larger-cutoff result and does not relabel its parent.

## Frozen downstream boundary

The Exp073J `5%` threshold is unchanged. This result does **not** authorize:

- a post-hoc `ell` cutoff;
- fiducial `P(k)`/`C_ell` weighting to force normalizability;
- oscillatory cancellation inside the positive support measure;
- covariance restriction/whitening;
- nuisance SVD/rank;
- relation/null fitting;
- G8 information.

By the prospectively frozen Exp073L consequence rule, the only newly authorized branch is a separately preregistered search for a finite-positive-support observational operator or support definition whose normalization is finite without downstream/model weighting.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
