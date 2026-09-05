# Exp073EH — WW distinct-field official-bin substitution exact closure v0.1

Status: prospectively frozen support diagnostic only; scientific accounting `+0/+0`.

## Authority and purpose
Exp073EG terminal `BIN_ONLY_MISMATCH +0/+0` established prospectively that the manual P/bin arithmetic used by Exp073EE/EF is not bitwise identical to PyMaster 2.7 `NmtBin.bin_cell`, while the corresponding Q/unbin operator is exact. Exp073EH asks one frozen causal question before any production adapter change: if P is replaced only by the official PyMaster 2.7 binning operation and Q is generated only through the official `NmtBin.unbin_cell`, does the reconstructed serialized->reloaded distinct-field bandpower-window operator become bitwise identical to public `NmtWorkspace.get_bandpower_windows()`?

This is a support diagnostic, not a rescue and not a science gate. No WW authority can be created.

## Frozen setup
Use PyMaster 2.7, deterministic distinct spin-2 S0/S1 masks, nside=16, lmax=47, ell 0..47, ncls=4, and exactly 8 bands with edges `[0,6,12,18,24,30,36,42,48]`. Compute the S0->S1 workspace, serialize to FITS, delete the in-memory workspace, and reload it. Canonical arrays are contiguous little-endian `<f8`.

## Frozen reconstruction
Let `M` be the exact reloaded coupling matrix in PyMaster's ell-major flattened ordering.

1. Build `R_official = P_public M` column-by-column. For every column `j` of `M`, reshape only as `[nell,ncls].T`, call the exact public `NmtBin.bin_cell`, then flatten the returned `[ncls,nband]` result in band-major ordering via transpose before insertion into column `j` of `R_official`.
2. Build `Q_official` column-by-column from every unit `(cls,band)` bandpower basis using only public `NmtBin.unbin_cell`; flatten its `[ncls,nell]` output in ell-major ordering via transpose.
3. Build `K_official = R_official @ Q_official` using NumPy's ordinary matrix product exactly once.
4. Build `W_reconstructed = np.linalg.inv(K_official) @ R_official` using NumPy's ordinary inverse and matrix product exactly once each.
5. Convert public `NmtWorkspace.get_bandpower_windows()` from `[ncls,nband,ncls,nell]` to the corresponding two-dimensional band-major/ell-major matrix using only transpose+reshape. No alternate layout is tried.

The frozen question is exact equality of `W_reconstructed` and the public bandpower-window matrix by both canonical SHA256 and `numpy.array_equal`.

## Frozen classification
- `OFFICIAL_BIN_SUBSTITUTION_FULL_EXACT`: full reconstructed BPW is exact.
- `OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH`: full reconstructed BPW is not exact.

Both outcomes are support-only `+0/+0`, score no science gate and create no WW authority. A max absolute difference may be recorded only as diagnostic metadata and is never an acceptance criterion.

## Prohibitions
No tolerance, `allclose`, rounding, smoothing, averaging, alternate summation order, alternate indexing/layout, alternate solver, alternate inverse, alternate BLAS backend, or result-dependent retry is permitted inside this gate.

## Frozen next action
If `OFFICIAL_BIN_SUBSTITUTION_FULL_EXACT`, the next prospective gate may validate a production-safe adapter architecture that delegates binning to the official PyMaster operation while preserving frozen full-resolution arithmetic and checkpoint semantics. If `OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH`, the next support gate must isolate the remaining matrix-multiplication/solver arithmetic after the official P/Q operators; it must not revisit bin/unbin semantics or use tolerance rescue. Exp073DV remains inactive.