# Exp073S0 — DES Y1 redMaGiC mask + n(z) reproduction result

**Date:** 2026-08-27  
**Classification:** `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`

## Immutable execution provenance

- execution commit: `82c5804b1fcbbdc100f09a9878643ddc51975d8e`;
- workflow run: `33086762750`;
- workflow job: `98568401949`;
- artifact: `9652504743`;
- artifact digest: `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e`.

All substantive workflow steps completed successfully. This is therefore a completed reproduction PASS, not an infrastructure outcome.

## Frozen mask reproduction

The exact DES Y1 redMaGiC mask was reproduced under the preregistered `nside=4096`, celestial-coordinate and strict `mask>0.5` semantics.

- input NSIDE: `4096`;
- NPIX: `201326592`;
- same-resolution `hp.ud_grade(...,4096)` exact identity: `true`;
- UNSEEN pixels before zeroing: `194789867`;
- retained pixels: `6536725`;
- retained sky fraction: `0.03246826430161794`;
- retained mask mean: `0.985935010460131`;
- retained range: `[0.8125, 1.0]`;
- dense canonical SHA256: `7eb243d77febe59d1fb327095b385b40084f4b6140ae4421f1c45c787088e918`;
- sparse pixel/value SHA256: `c1449c30efb31ce0b7f6cab01f2ea11faad8156a3021033518015b3e853abd3b`.

This explicitly closes the same-resolution identity assumption rather than relying on it implicitly.

## Released redshift kernels

The pinned lens and source redshift-distribution schemas were reproduced without interpolation, normalization, photo-z shifts or support cuts.

### Lens redMaGiC n(z)

- rows: `400`;
- redshift range: `0.0051 <= z <= 3.9951`;
- bins: `BIN1..BIN5`;
- canonical numeric SHA256: `395e043566c3c06e960c95d8b7b617b29a42f5d4fa4e65d5dd66f2e5f674a383`.

### Source weak-lensing n(z)

- rows: `400`;
- redshift range: `0.0051 <= z <= 3.9951`;
- bins: `BIN1..BIN4`;
- canonical numeric SHA256: `ab4d447dc72e0fdf9cdd470b2eb9cb4d5aa5a6a1bd89f1b55bd047a18f972f97`.

## Scientific boundary

Exp073S0 does **not** score the Exp073P physical-support gate. No bandpower window, `f_invalid`, covariance, whitening, nuisance/SVD, relation/null or G8 information was read or computed.

The result closes only the small-input P3 prerequisite. The already frozen Exp073P acceptance criteria remain unchanged. G7/G8/G9 remain OPEN.
