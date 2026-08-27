# DSIR recovery checkpoint — Exp073N provenance FAIL -> Exp073O

**Date:** 2026-08-27

## Last completed gate

Exp073N is frozen as `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`.

Execution provenance:

- merge SHA `6868ed9113e2697675756f23fae8d350a9239bf6`;
- run `33062650033`;
- job `98484967582`;
- artifact `9642372335`;
- artifact digest `sha256:914d23e9d708a7b8cb9e097a69845e2630ec265b5ccc489ce9a8d389d4e198db`;
- result JSON SHA256 `e4eb6cd10ac964030e84596ee352f22c5c2d4fae91e917a68db567cef2b6adeb`.

The frozen DES operator pin reproduces exactly, but it exposes only Y3 FLASK YAMLs and its public GGL driver only executes the FLASK branch. Exact published DES Y3 real-data Wm NaMaster workspace/input provenance therefore cannot be reproduced under Exp073N section 3.

No support fraction or retained dimension was computed. Do not reinterpret this as a 5% physical-support FAIL.

## Preserved state

- Exp073M operator-class candidate result preserved;
- Exp073L nonnormalizable KiDS absolute-response result preserved;
- BOSS mm remains 54/240 retained, non-classifying;
- common rectangle remains `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- future threshold remains `f_invalid <= 0.05`;
- future minimum retained dimension remains 15;
- covariance/whitening, nuisance rank/SVD, quotient/relation/null and G8 are still forbidden.

## Next admissible experiment

Exp073O is prospectively frozen before candidate classification:

`experiments/073o_public_realdata_finite_harmonic_wm_replacement_prereg_v0_1.md`.

Search source/operator provenance only. Preferred first branch: exact public DES Y1 real-data harmonic GGL lineage; then other public finite pseudo-C_ell galaxy-shear operators. Do not evaluate physical-support fractions in Exp073O.

Only `PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O` may authorize a separately preregistered replacement-route physical-support audit.

G7 OPEN. G8 OPEN. G9 OPEN.
