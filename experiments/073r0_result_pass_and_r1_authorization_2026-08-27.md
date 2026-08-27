# Exp073R0 result and Exp073R1 authorization — 2026-08-27

## Classification

`PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`

This is a reproduction / numerical-equivalence prerequisite PASS. It is **not** a physical-support PASS and does not score `f_invalid`.

## Immutable execution provenance

- GitHub Actions run: `33103083736`
- Job: `98625663930` (`raw-row-healpix-equivalence`)
- Executed head SHA: `94b05d307295d5e9263646983ece9514f9fa2e88`
- Immutable artifact ID: `9661445512`
- Artifact name: `exp073r0-row-healpix-equivalence-94b05d307295d5e9263646983ece9514f9fa2e88`
- Artifact ZIP digest: `sha256:bfa97a88218cda6e6e6c58d915e8e5b21500fa677a484205691f2f01662ed4d0`

The transport layer experienced one recoverable curl timeout during the run; the preregistered exact-range retry logic recovered, and the final frozen audit plus independent assertion both completed successfully.

## Frozen sample result

- sample rows: `131072`
- bins with selected rows: `[0,1,2,3]`
- selected rows by bin:
  - bin 0: `7674`
  - bin 1: `7667`
  - bin 2: `7272`
  - bin 3: `3618`
- `source_field_exact`: all frozen source fields matched Astropy decoding.
- `metacal_field_exact`: all frozen metacal fields matched Astropy decoding.
- `pixel_indices_exact`: true in every bin.
- mapper remained `nside=4096`, celestial coordinates, `hp.ang2pix(..., lonlat=True)`.
- `science_gate_scored = false`; gate state remains `G7 OPEN, G8 OPEN, G9 OPEN`.

## Consequence boundary

The prospectively frozen authorization condition for Exp073R1 is now satisfied. Exp073R1 may therefore execute its already-frozen full one-pass DES Y1 weak-lensing mask reconstruction using R0 run `33103083736` as its parent.

This authorization does **not** permit any of the following before Exp073R1 PASS and subsequent Exp073P execution:

- computing DES `f_invalid`;
- changing the Exp073P support rectangle or the 5% threshold;
- covariance restriction / whitening;
- nuisance SVD;
- relation / null / G8 tests.

## Independent pre-execution implementation audit

The merged R1 implementation was reviewed after R0 completion without changing scientific criteria. It binds a completed successful R0 run and exact PASS artifact before full-catalogue transport, recomputes the full source/metacal SHA256 byte streams, reads exactly `136930995` rows from each table, uses four disk-backed `uint32` count maps at `nside=4096`, records selected HEALPix indices, and independently reconstructs each binary mask from the saved pixel-index record. The disk-backed design avoids requiring four dense maps in resident RAM; no covariance or support scoring is present in R1.

No scientific criterion was altered as a consequence of the observed R0 result.
