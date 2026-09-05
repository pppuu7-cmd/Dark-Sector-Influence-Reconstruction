# Exp073EI — WW distinct-field solver-operator exact localization v0.1

Status: prospectively frozen support diagnostic only; accounting `+0/+0`.

## Authority and purpose
Exp073EG localized the manual pre-solve mismatch to P/bin while Q/unbin was exact. Exp073EH then replaced P and Q with official PyMaster 2.7 operations and still found the full reconstructed serialized->reloaded bandpower-window matrix not bitwise equal to public `NmtWorkspace.get_bandpower_windows()`. Exp073EI isolates whether the remaining exact divergence is already present in the inverse/decoupling operator, before the final multiplication by R.

## Frozen setup
Use PyMaster 2.7, the same deterministic distinct spin-2 S0/S1 masks, nside=16, lmax=47, ncls=4 and eight bands `[0,6,12,18,24,30,36,42,48]`. Serialize the S0->S1 workspace to FITS, delete it, and reload it. Canonical arrays are contiguous little-endian `<f8`.

## Frozen operator construction
1. Reconstruct `R_official` only through public `NmtBin.bin_cell` applied column-by-column to the reloaded coupling matrix, with the same single fixed ell-major/band-major reshape convention used by Exp073EH.
2. Reconstruct `Q_official` only through public `NmtBin.unbin_cell` on every unit `(cls,band)` basis in fixed band-major then cls order.
3. Form `K_official = R_official @ Q_official` exactly once with NumPy matrix multiplication.
4. Define `D_numpy = np.linalg.inv(K_official)` exactly once.
5. Derive `D_public` column-by-column without alternate algebra: for every unit bandpower basis, unbin it only with public `NmtBin.unbin_cell`, pass the resulting coupled-spectrum-shaped array to reloaded `NmtWorkspace.decouple_cell` with default zero bias/noise, flatten the returned `[ncls,nband]` in band-major order, and insert as one column.
6. Compare `D_numpy` and `D_public` only by canonical SHA256 and `numpy.array_equal`.

## Frozen classification
- `SOLVER_OPERATOR_EXACT`: D_numpy and D_public are bitwise exact.
- `SOLVER_OPERATOR_MISMATCH`: they are not bitwise exact.

Both outcomes are support-only `+0/+0`, score no science gate and create no WW authority. Max absolute difference may be recorded diagnostic-only.

## Prohibitions
No tolerance/allclose, rounding, smoothing, averaging, alternate solver, alternate matrix inverse, alternate ordering/layout, alternate BLAS backend, or result-dependent retry.

## Frozen next action
If `SOLVER_OPERATOR_MISMATCH`, the remaining cross-workspace exactness problem is localized to solver/backend arithmetic and the next prospective architecture must preserve the official PyMaster decoupling backend rather than substituting NumPy/GSL arithmetic. If `SOLVER_OPERATOR_EXACT`, the next support gate may isolate only the final `D @ R` multiplication arithmetic/order. Exp073DV remains inactive.