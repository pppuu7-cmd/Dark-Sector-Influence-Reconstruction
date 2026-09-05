# Exp073EJ — WW distinct-field public-decouple BPW exact closure v0.1

Status: prospectively frozen support diagnostic only; accounting `+0/+0`.

## Authority and purpose
Exp073EI terminal `SOLVER_OPERATOR_MISMATCH +0/+0` established that a NumPy inverse of the official-P/Q-derived K operator is not bitwise identical to the official PyMaster 2.7 decoupling operator. Exp073EJ therefore tests the official backend end-to-end without reconstructing an inverse: does public `NmtWorkspace.decouple_cell`, applied directly column-by-column to the serialized->reloaded coupling matrix, reproduce public `NmtWorkspace.get_bandpower_windows()` bitwise exactly?

This is a support diagnostic. It scores no science gate and creates no WW authority.

## Frozen setup
Use PyMaster 2.7, the same deterministic distinct spin-2 S0/S1 masks, nside=16, lmax=47, ncls=4 and eight bands `[0,6,12,18,24,30,36,42,48]`. Compute S0->S1 workspace, serialize to FITS, delete the in-memory workspace and reload it. Canonical arrays are contiguous little-endian `<f8`.

## Frozen comparison
1. Read the reloaded coupling matrix M.
2. For each column j of M in ascending order, reshape only as `[nell,ncls].T` to obtain the public coupled-spectrum layout `[ncls,nell]`.
3. Apply reloaded `NmtWorkspace.decouple_cell` directly to that column with default zero bias/noise.
4. Flatten returned `[ncls,nband]` in band-major order through transpose and insert as column j of `W_decouple`.
5. Convert public `get_bandpower_windows()` from `[ncls,nband,ncls,nell]` into the corresponding fixed two-dimensional band-major/ell-major matrix using only `transpose(1,0,3,2).reshape(...)`.
6. Compare exact canonical SHA256 and `numpy.array_equal`.

## Frozen classification
- `PUBLIC_DECOUPLE_BPW_EXACT`: exact SHA and array equality pass.
- `PUBLIC_DECOUPLE_BPW_MISMATCH`: either exact check fails.

Both outcomes are `+0/+0`. Diagnostic max absolute difference may be recorded but is not an acceptance criterion.

## Prohibitions
No tolerance/allclose, rounding, smoothing, averaging, manual bin/unbin, reconstructed inverse, alternate solver, alternate matrix multiplication, alternate layout, or result-dependent retry.

## Frozen next action
If exact, the next prospective adapter architecture must delegate the decoupling operation to the official PyMaster backend rather than reconstructing it algebraically; a separate production-readiness gate is still required before full-resolution WW_S0_S1 activation. If mismatch, the next support gate must inspect only the official public bandpower-window construction versus public decouple semantics, with no return to manual P/Q or alternate arithmetic. Exp073DV remains inactive.