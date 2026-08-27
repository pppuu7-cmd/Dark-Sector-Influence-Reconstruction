# DSIR recovery checkpoint — Exp073M FOUND -> Exp073N preregistered

**Date:** 2026-08-27

## Verified starting main

`39cd1c93f73717b56f02c8240392509ca3b7ec34`

## Newly closed gate

Exp073M is classified `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`.

Complete operator/source pair:

- Wm: DES Y3 harmonic galaxy-galaxy lensing pseudo-C_ell;
- WW: DES Y1 harmonic cosmic shear pseudo-C_ell;
- common operator repository: `hocamachoc/3x2hs_measurements@21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab`;
- BOSS remains the frozen mm component.

DES Y3 harmonic cosmic shear is not used because its paper states measurement code is available only upon request, which fails Exp073M M1.

No support fraction was computed in Exp073M.

## Key operator bindings

- `csh.py`: `4b81b23e0074d7e4bb8c1e1cb9c8b916c5549787`;
- `cshtest.py`: `33c4d3ae40098dec70a7a90f7115b16a7083aed4`;
- `etc/y1mcal_csh.yml`: `6cfb2291ab6f64116ed7a7df203fa0488bd45e81`;
- `etc/binNicola2020.txt`: `4230a1a3b10cc631e98a03d0ed6e288b35ed6cd4`;
- `ggltest.py`: `3b52360549230e5805252bfb2c5fdbaae885a01c`.

The code explicitly constructs finite NaMaster bins, computes mode-coupling workspaces, stores bandpower windows, and measures/decouples cross or shear-shear spectra without a P(k)-weighted normalization.

## Frozen next gate

Exp073N is preregistered before any support output.

Do **not** calculate leakage until exact public DES Y1/Y3 redshift/mask/operator inputs used by the calculation are checksum-bound. Then reproduce finite NaMaster bandpower responses and evaluate the unchanged common rectangle:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05`;
- retained full-observation dimension `>=15`.

No effective-redshift, effective-ell or post-hoc angular cutoff substitute is allowed. No covariance, nuisance SVD, relation/null or G8 may be read.

Only `PASS_DES_HARMONIC_COMMON_PHYSICAL_SUPPORT_EXP073N` may open preregistered covariance restriction/whitening.

## Gate state

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
