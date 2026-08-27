# DSIR recovery checkpoint — Exp073P after Exp073S0

**Date:** 2026-08-27

## Current validated state

- Exp073P2 checksum identity binding: `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`.
- Exp073Q2 large-FITS schema/row-layout audit: PASS.
- Exp073S0 exact DES Y1 redMaGiC mask + released lens/source n(z) reproduction: `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`.
  - run `33086762750`, job `98568401949`, artifact `9652504743`;
  - artifact digest `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e`;
  - exact same-NSIDE `hp.ud_grade(...,4096)` identity passed;
  - redMaGiC retained pixels: `6536725`;
  - lens/source n(z) each contain 400 rows and reproduce the frozen schemas.
- Exp073R0 raw-row decoder + HEALPix mapper-equivalence audit is still running as GitHub Actions run `33086178147`; do not duplicate it. Its preregistered PASS is the only authorization for Exp073R1 full one-pass weak-lensing mask construction.

## Frozen Exp073P scientific acceptance criteria — unchanged

Do not modify post hoc:

- common physical redshift support: `0.295 <= z <= 2.33`;
- common physical wavenumber ceiling: `k <= 0.06664762008318016 Mpc^-1`;
- positive invalid-support fraction threshold: `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension: `15`;
- classifying DES map resolution: `nside=4096`.

No covariance, whitening, nuisance SVD/rank, quotient/relation/null or G8 output may be read before a genuine Exp073P support PASS.

## Next admissible step

1. First resolve Exp073R0 exactly as preregistered.
2. If R0 is `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`, prospectively freeze and execute Exp073R1 full one-pass DES Y1 weak-lensing mask construction using the already checksum-bound source-bin and metacal catalogues. R1 must remain a reproduction/input-construction experiment and must not compute `f_invalid`.
3. If R0 is deterministic FAIL, preserve it and repair only the implementation equivalence before any R1 or support calculation.
4. If R0 is infrastructure/incomplete, preserve that distinction and retry without changing frozen scientific criteria.
5. Only after all Exp073P input/operator prerequisites are independently reproduced may the already-frozen physical-support leakage calculation be executed.

## Gate state

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance/whitening: CLOSED pending Exp073P support PASS
