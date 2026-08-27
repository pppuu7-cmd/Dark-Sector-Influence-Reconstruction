# Exp073P — Cosmotheka DES Y1 Wm+WW + BOSS mm exact common physical-support audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073P SUPPORT FRACTION IS EVALUATED

## 1. Parent state

Bind and preserve:

- Exp073O = `PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`;
- Exp073N = `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`;
- Exp073L = `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`;
- Exp073J KiDS component = `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`;
- frozen BOSS finite-matrix mm component = `54/240` retained, non-classifying;
- common physical rectangle exactly `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- support acceptance exactly `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension exactly `15`.

No earlier classification is reopened by Exp073P.

## 2. Exact public harmonic source

Freeze the Wm/WW operator source to

`Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`

with source paths:

- `cosmotheka/mappers/mapper_DESY1gc.py`;
- `cosmotheka/mappers/mapper_DESY1wl.py`;
- `cosmotheka/cls/cl.py`;
- `input/DESY1_eBOSS_P18CMBK.yml`.

Freeze the real-data DES products by exact release filename before support evaluation:

- `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits`;
- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`;
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`;
- `y1_source_redshift_binning_v1.fits`;
- `y1_redshift_distributions_v1.fits`;
- `2pt_NG_mcal_1110.fits`.

The execution record must store URL, byte count where available and SHA256 for every actually consumed file. A mirror is allowed only if byte-identical to the prospectively bound release object.

## 3. Frozen angular operator

Use the real-data Cosmotheka map construction and NaMaster pseudo-`C_ell` operator without changing semantics.

Freeze:

- `nside=4096` unless an implementation-only lower-resolution convergence test is separately labelled non-classifying; the classifying route uses 4096;
- finite bandpower edges exactly
  `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`;
- lens redshift bins exactly `[0.15,0.30)`, `[0.30,0.45)`, `[0.45,0.60)`, `[0.60,0.75)`, `[0.75,0.90)`;
- source bins exactly as encoded by the released `y1_source_redshift_binning_v1.fits` and `y1_redshift_distributions_v1.fits`;
- direct signed density×shear cross for Wm;
- shear E-mode auto/cross block for WW;
- absolute value only when constructing the positive support envelope, never in the measured signed Wm observable.

## 4. Physical support mapping

For each finite harmonic response row, propagate the positive absolute bandpower-window envelope through the exact lens/source redshift kernels into `(k,z)` using the same physical convention already frozen in G7, including `k=(ell+1/2)/chi(z)` for Limber support bookkeeping.

The support numerator is the positive envelope weight outside the common rectangle; the denominator is the total positive envelope weight. No fiducial `P(k)`, nonlinear boost, covariance, nuisance weighting, relation residual or G8 information may enter either numerator or denominator.

A coordinate passes only if its complete required block support satisfies `f_invalid <= 0.05`.

## 5. Frozen P1–P8 controls

### P1 — immutable parent binding
Reproduce Exp073O classification and the frozen BOSS mm record exactly.

### P2 — DES input checksum binding
All consumed DES Y1 release objects must be checksum-bound before support fractions are evaluated.

### P3 — operator reproduction
Reproduce the finite NaMaster bin/workspace/bandpower-window semantics from the pinned source without changing masks, redshift selections, sign conventions or bin edges.

### P4 — positive-envelope normalization
Every classifying Wm/WW response row must have finite positive total envelope weight. Zero/non-finite normalization is reproduction/numerical failure, not a support FAIL.

### P5 — physical-unit convention
`ell`, comoving distance and physical `k [Mpc^-1]` conversions must pass explicit roundtrip/unit controls and must not mix `h/Mpc` with `Mpc^-1`.

### P6 — unchanged support threshold
Use only `f_invalid <= 0.05`, common `z` range `[0.295,2.33]`, and `k <= 0.06664762008318016 Mpc^-1`. No data-dependent threshold change is permitted.

### P7 — full-coordinate rule
Combine Wm, WW and the already frozen BOSS mm component only after each block has its own valid support mask. Retained dimension is counted only for complete observation coordinates. Minimum PASS dimension remains exactly `15`.

### P8 — no downstream leakage
Do not read covariance, whitening products, nuisance SVD/rank, quotient/relation/null residuals, G8 withheld-family outputs or article-selection results.

## 6. Frozen classifications

If P1–P8 pass and retained full-coordinate dimension is at least 15, classify

`PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P`.

If P1–P8 pass but retained full-coordinate dimension is below 15, classify

`FAIL_COMMON_PHYSICAL_SUPPORT_DIMENSION_EXP073P`.

If any coordinate-level support fractions are trustworthy but all Wm/WW coordinates are rejected by the unchanged 5% criterion, this remains the same scientific support-dimension FAIL; preserve the detailed block diagnostics.

If source/checksum/operator reproduction, positive normalization or unit controls fail before a trustworthy support classification, classify

`FAIL_EXP073P_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`.

Infrastructure interruption is `INCOMPLETE_EXP073P` and is not a scientific result.

## 7. Downstream boundary

Only `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P` authorizes covariance restriction/whitening. A scientific FAIL authorizes only a newly preregistered support/operator strategy; it does not authorize threshold relaxation.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
