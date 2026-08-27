# DSIR recovery checkpoint — Exp073O FOUND → Exp073P preregistered

**Date:** 2026-08-27

## Verified parent

Research resumed from `main@228d62faffa7d0ed9216b578037781ac5039b89b`.

## Closed in this iteration

Exp073O is now classified prospectively under its frozen O1–O8 decision rule as:

`PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.

The satisfying candidate is the public DES Y1 redMaGiC density × Metacalibration shear pseudo-`C_ell` operator in:

`Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.

Exact source paths:

- `cosmotheka/mappers/mapper_DESY1gc.py`
- `cosmotheka/mappers/mapper_DESY1wl.py`
- `cosmotheka/cls/cl.py`
- `input/DESY1_eBOSS_P18CMBK.yml`

Exact DES Y1 public products to bind in the next execution:

- `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits`
- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`
- `y1_source_redshift_binning_v1.fits`
- `y1_redshift_distributions_v1.fits`
- `2pt_NG_mcal_1110.fits`

No physical-support fraction was evaluated in Exp073O.

## Frozen next step

Before any new support fraction, Exp073P has been preregistered in:

`experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`.

Exp073P must preserve without modification:

- common rectangle `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension `15`;
- frozen BOSS mm record `54/240`, non-classifying until combined with valid Wm/WW masks;
- signed Wm through the observable; absolute value only in support-envelope construction;
- no covariance, nuisance SVD/rank, quotient/relation/null, G8 or article-selection information before support PASS.

Classifying Cosmotheka route uses `nside=4096` and the exact frozen bandpower edges recorded in the Exp073P preregistration.

## Permanent parent classifications

Do not change:

- Exp073N = `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`
- Exp073L = `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`
- Exp073J KiDS component = `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`
- Exp073M = `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`

## Gate state

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance restriction/whitening: CLOSED pending Exp073P PASS

## Exact continuation instruction

1. Merge the Exp073O result + Exp073P preregistration before implementation/output.
2. Build a provenance-first Exp073P implementation that checksum-binds every consumed DES public object before calculating any support fraction.
3. Reproduce Cosmotheka map/bin/workspace semantics and explicit physical-k unit controls.
4. Evaluate Wm and WW positive support masks independently, then combine only with the frozen BOSS mm mask.
5. Apply the unchanged `5%` and `>=15` classification rule.
6. Only an Exp073P PASS may open covariance restriction/whitening.
