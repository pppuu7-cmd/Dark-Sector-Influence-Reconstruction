# DSIR-I support-operator eligibility provenance extension

**Date:** 2026-08-27  
**Scope:** late DSIR3 results that refine the observation-space eligibility boundary after the Exp072A--Exp073E chain.

This extension is part of the DSIR-I manuscript claim boundary. It records results that are too late for the original P1--P23 matrix snapshot but are now used in the manuscript. They remain subordinate to the same submission rule: a numerical sentence is manuscript-eligible only when its frozen source, status, and interpretation boundary are explicit.

| ID | Manuscript-safe claim | Evidence / status | Run / commit | Artifact | Digest | Frozen control | Key result | Mandatory boundary |
|---|---|---|---|---:|---|---|---|---|
| P24 | The frozen KiDS absolute-response route does not define a finite positive support normalizer. | Exp073L — `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L` | run `33049366874`; execution head `1c7064bf88afb868af7691eb33520c165ac3a245` | `9637070322` | `sha256:03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684` | extended cutoffs `ell=[120000,240000,480000]`; half-step tolerance `0.005`; no physics/downstream weighting | `8/8` Wm and `8/8` WW nonnormalizable; finite components `0`; final local exponent ranges Wm `1.49444..1.51803`, WW `1.49267..1.51570`; final shell fractions `~0.64465..0.65084`; half-step max relative difference `1.94e-6` | normalizability result only; no support fraction, covariance restriction, post-hoc ell cut, or fiducial-power weighting authorized; G7/G8/G9 remain OPEN |
| P25 | A finite-positive three-block observational support operator candidate exists under frozen pre-output criteria. | Exp073M — `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M` | result commit `3834695fd9c494062d287c90107b8823454e7745` | n/a | commit-bound | M1--M8 all true: public immutable provenance, finite positive normalization by construction, no model/downstream weighting, signed Wm semantics, independent WW semantics, redshift information, later 5% audit possible, no downstream leakage | selected Wm=`DES_Y3_harmonic_galaxy_galaxy_lensing`, WW=`DES_Y1_harmonic_cosmic_shear`, mm=`BOSS_finite_matrix_component_unchanged` | candidate/precondition result only; physical support fraction not evaluated; covariance/nuisance/relation/G8 unread; threshold unchanged; G7/G8/G9 remain OPEN |
| P26 | Exact public-input identity and small-input reproduction prerequisites for the DES harmonic route have been closed without support scoring. | Exp073P2 `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2` + Exp073S0 `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0` | P2 result commit `ba91cdaf43f3a7c08471bbd25e82408c064904ab`; S0 run `33086762750`, execution `82c5804b1fcbbdc100f09a9878643ddc51975d8e` | S0 `9652504743` | S0 `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e` | full-stream SHA256 before support output; native `Nside=4096` reproduction; no covariance/SVD/G8 read | all frozen DES Y1 release objects checksum-bound; S0 retains `6,536,725` mask pixels `>0.5`, `f_sky=0.0324682643`; lens/source `n(z)` each 400 rows with 5/4 bins | provenance/reproduction PASS only; no physical support fraction, covariance, nuisance rank, detectability, or G7/G8/G9 conclusion |

## Corroborating but non-promoted record

Exp073G (`FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`, run `33036220112`, artifact `9632090063`) is retained as a methodological corroboration rather than a scientific-support row. Its operator analysis shows why a configuration-space Fourier--Bessel absolute response can fail to possess a finite positive all-k normalizer: with `K_l(k;s) proportional to k^2 j_l(ks)` and `j_l(ks)=O(1/k)`, the absolute response is generically `O(k)`. The record itself explicitly states `scientific_support_fail=false` and `support_fraction_computed=false`; it must not be upgraded into a support FAIL.

## Analytic support-measure note

For a dyadic power-law normalization in which the cumulative positive response scales as `L^p`, the fractional contribution of the newest shell `[L,2L]` is

`f_shell = 1 - 2^(-p)`.

Exp073L's measured local exponents near `p~1.5` therefore imply an order-unity shell fraction near `0.646`, consistent with the frozen numerical shell fractions. This relation is used only to interpret the nonnormalizability mechanism; it does not introduce a new scientific threshold.

## Pending exclusion

Exp073R0 is not a manuscript result. Its latest state at source commit `5ee34c3fc80ab1091b7e925d321d880dbadade3c` is a retry after an infrastructure timeout with unchanged frozen science. No R0 output may enter a claim until a completed frozen result exists.

## Submission boundary

P24--P26 extend, but do not close, the observation-space quotient programme. The required order remains: finite positive support measure -> physical support eligibility -> physically justified theory providers -> covariance restriction/whitening -> nuisance quotient -> relation/null tests. `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
