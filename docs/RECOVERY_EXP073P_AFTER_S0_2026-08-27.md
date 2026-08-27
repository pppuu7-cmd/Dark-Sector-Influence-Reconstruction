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
- Exp073R0 attempt 1, run `33086178147`, ended `cancelled` during the frozen sampled raw-row audit because the workflow-level `timeout-minutes: 35` was reached. No result JSON was produced; infrastructure/incomplete only.
- Infrastructure-only repair PR `#151` changed only the Exp073R0 job timeout from 35 to 120 minutes; frozen scientific semantics were unchanged.
- Exp073R0 attempt 2, run `33092211100`, job `98587741090`, head `5ee34c3fc80ab1091b7e925d321d880dbadade3c`, ended during the sampled metacal byte-range transport after all retries failed with `TimeoutError: The read operation timed out`. This is `INCOMPLETE_EXP073R0`, not deterministic FAIL and not PASS. Upload artifact `9656933701` was preserved with ZIP digest `sha256:a5037b4e644ddd9faba48088b3bc6a394874d30c81a9cf84f9627ae71efcff6d`.
- A job-level rerun of Exp073R0 was requested without changing sample windows, row layouts, decoder, selection, HEALPix mapping or acceptance semantics. Treat it as attempt 3 of the same frozen equivalence audit; do not duplicate it while queued/running.
- Exp073R1 full one-pass weak-lensing mask contract is prospectively frozen in `experiments/073r1_desy1_full_onepass_weak_lensing_mask_prereg_v0_1.md`, before any attempt-2 scientific output. This freeze does not authorize execution before R0 PASS. It fixes exact catalogue hashes/layouts, `nside=4096`, `coords='C'`, four-bin row selection, `hp.ang2pix(...,lonlat=True)`, unweighted count-map construction, completeness/repeatability/provenance controls, and a strict ban on `f_invalid` or downstream covariance/G8 quantities.

## Frozen Exp073P scientific acceptance criteria — unchanged

Do not modify post hoc:

- common physical redshift support: `0.295 <= z <= 2.33`;
- common physical wavenumber ceiling: `k <= 0.06664762008318016 Mpc^-1`;
- positive invalid-support fraction threshold: `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension: `15`;
- classifying DES map resolution: `nside=4096`.

No covariance, whitening, nuisance SVD/rank, quotient/relation/null or G8 output may be read before a genuine Exp073P support PASS.

## Next admissible step

1. Resolve Exp073R0 attempt 3 under the unchanged frozen contract.
2. If R0 is `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`, execute the already-frozen Exp073R1 contract without changing it. Exp073R1 remains a reproduction/input-construction experiment and must not compute `f_invalid`.
3. If R0 is deterministic FAIL, preserve it; Exp073R1 execution remains forbidden. Repair only implementation equivalence under a new prospective record.
4. If R0 is again infrastructure/incomplete, preserve that distinction and harden only transport/runtime mechanics without changing scientific criteria or the frozen Exp073R1 contract.
5. Only after all Exp073P input/operator prerequisites are independently reproduced may the already-frozen physical-support leakage calculation be executed.

## Gate state

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance/whitening: CLOSED pending Exp073P support PASS
