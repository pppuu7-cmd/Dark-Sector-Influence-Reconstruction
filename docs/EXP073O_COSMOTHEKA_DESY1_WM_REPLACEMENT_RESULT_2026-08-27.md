# Exp073O — public real-data finite harmonic Wm replacement result

**Date:** 2026-08-27  
**Classification:** `PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`

## Result

A candidate satisfying the frozen O1–O8 criteria was found in the public Cosmotheka pipeline, pinned to:

`Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.

The candidate is the DES Y1 redMaGiC galaxy-density × DES Y1 Metacalibration galaxy-shear pseudo-`C_ell` cross operator.

## Why this resolves the previous O3 blocker

The earlier `hocamachoc/3x2hs_measurements` Y1 branch referenced site-local precomputed redMaGiC maps. The public Cosmotheka implementation instead exposes deterministic real-data mappers from exact DES Y1 released products:

- `mapper_DESY1gc.py` reads `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits` and `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`, applies the fixed five redshift bins and catalogue `weight`, and constructs the density map directly;
- `mapper_DESY1wl.py` reads `mcal-y1a1-combined-riz-unblind-v4-matched.fits`, `y1_source_redshift_binning_v1.fits` and `y1_redshift_distributions_v1.fits`, reproduces the Metacalibration selection response and shear maps;
- the official DES Y1 release pages explicitly publish these exact redMaGiC, mask, Metacalibration, source-bin and source-`n(z)` products;
- `input/DESY1_eBOSS_P18CMBK.yml` freezes the DES real-data tracer pairing, `nside=4096`, the exact product names and a finite bandpower-edge list.

The lens `n(z)` is read from the public DES Y1 3x2pt data-vector product `2pt_NG_mcal_1110.fits`.

## Finite operator and signed cross semantics

`cosmotheka/cls/cl.py` constructs finite `pymaster.NmtBin` objects, computes an `NmtWorkspace` mode-coupling matrix, obtains `get_bandpower_windows()`, evaluates the direct cross with `nmt.compute_coupled_cell(f1,f2)`, and decouples with the workspace.

Therefore:

- the harmonic domain is finite (`ell < 3*nside`);
- the positive absolute support envelope is normalizable without a fiducial power spectrum;
- the measured galaxy-shear cross remains signed through measurement/decoupling;
- no GR matter-to-Weyl closure is imposed;
- covariance, nuisance directions, relation/null residuals and G8 were not used to select or make the operator finite.

## Frozen O1–O8 classification

All O1–O8 pass for this candidate. Under the preregistered Exp073O decision rule this closes Exp073O as

`PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.

This does **not** constitute a physical-support PASS. No `f_invalid` value was computed in Exp073O.

## Parent preservation

Unchanged:

- Exp073N = `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`;
- Exp073L = `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`;
- Exp073J KiDS component = `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`;
- BOSS finite-matrix mm = `54/240` retained, still non-classifying;
- common rectangle = `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- future support threshold = `f_invalid <= 0.05`;
- minimum retained dimension = `15`.

G7/G8/G9 remain OPEN. Covariance restriction remains closed until the separately frozen support audit passes.
