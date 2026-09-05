# Exp073EF — WW distinct-field K/R operator exact localization v0.1

Status: prospectively frozen support diagnostic only; scientific accounting `+0/+0`.

## Authority and purpose
Exp073EE terminal `FORMULA_MISMATCH +0/+0` showed that the current NumPy reconstruction of the saved-FITS bandpower-window formula is not bitwise identical to official serialized→reloaded PyMaster 2.7 windows. Exp073DX already excluded FITS orientation and Exp073ED excluded low-level/public output layout. Exp073EF must localize whether the mismatch is already present in the pre-solve operators `K=P M Q` and/or `R=P M`, rather than testing alternate rescue formulas.

## Frozen setup
Use PyMaster 2.7, deterministic distinct spin-2 S0/S1 masks, nside=16, lmax=47, ell 0..47, 8 bands with edges [0,6,12,18,24,30,36,42,48], ncls=4. Compute S0->S1 workspace, serialize to FITS, delete in-memory workspace, reload with `NmtWorkspace.read_from`.

Canonical arrays are contiguous little-endian `<f8`.

## Two independently defined operator paths
1. **Formula path**: reproduce exactly the Exp073EE flattened indexing and summation order up to but excluding the linear solve, yielding `K_formula` and `R_formula`.
2. **Public operational path**:
   - each column of `R_public` is obtained by a unit unbinned theory basis vector, `wr.couple_cell`, then `bins.bin_cell`;
   - each column of `K_public` is obtained by a unit bandpower basis expanded with the workspace bin's official `unbin_cell`, then `wr.couple_cell`, then `bins.bin_cell`.
No matrix inverse or solve is used in this experiment.

## Frozen exact classification
- `KR_OPERATORS_EXACT` iff K and R shapes match, SHA256 match and `numpy.array_equal` is true for both pairs.
- otherwise `KR_OPERATOR_MISMATCH`.
Both classifications are `+0/+0`, score no science gate and create no WW authority.

Diagnostic-only max absolute differences may be recorded but never used for acceptance. No tolerance, `allclose`, rounding, smoothing, averaging, effective-ell substitution or post-hoc alternate indexing is permitted.

## Next action frozen prospectively
If `KR_OPERATORS_EXACT`, a separately preregistered solver/backend exact-localization gate is allowed. If `KR_OPERATOR_MISMATCH`, a separately preregistered operator-only diagnostic must localize K versus R and bin/unbin semantics. Exp073DV remains inactive.
