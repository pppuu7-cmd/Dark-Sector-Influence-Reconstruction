# Exp073EG — WW distinct-field bin/unbin exact localization v0.1

Status: prospectively frozen support diagnostic only; scientific accounting `+0/+0`.

## Authority and purpose
Exp073EF terminal `KR_OPERATOR_MISMATCH +0/+0` established that both pre-solve K and R from the current manual reconstruction are not bitwise identical to independently operational public-PyMaster constructions. Exp073EG localizes whether the exact divergence is already introduced by the manual P/bin operator and/or manual Q/unbin operator. It does not alter, tune or rescue the reconstruction.

## Frozen setup
Use PyMaster 2.7, deterministic distinct spin-2 S0/S1 masks, nside=16, lmax=47, ell 0..47, ncls=4 and exactly 8 bands with edges `[0,6,12,18,24,30,36,42,48]`. Compute S0->S1 workspace, serialize to FITS, delete in-memory workspace and reload it. Canonical arrays are contiguous little-endian `<f8`.

## Frozen P/bin probes
Take deterministic coupled-spectrum probes directly from exact columns of the reloaded coupling matrix, reshaped into public `[ncls,nell]` order. For every frozen probe, compare:
1. `P_manual`: the same explicit per-band arithmetic used by Exp073EE/EF, weight `1/(edge_hi-edge_lo)` and ascending-ell accumulation;
2. `P_public`: `NmtBin.bin_cell` on the identical probe.
Concatenate all outputs in a fixed probe order and compare exact SHA256 and `numpy.array_equal`.

## Frozen Q/unbin probes
For every `(cls,band)` unit bandpower basis in fixed lexicographic order, compare:
1. `Q_manual`: explicit piecewise-constant unbinning corresponding to the frozen `NmtBin.from_edges` construction;
2. `Q_public`: `NmtBin.unbin_cell` on the identical unit basis.
Concatenate all outputs in fixed order and compare exact SHA256 and `numpy.array_equal`.

## Frozen classification
- `BIN_UNBIN_EXACT`: P exact and Q exact.
- `BIN_ONLY_MISMATCH`: P mismatch, Q exact.
- `UNBIN_ONLY_MISMATCH`: P exact, Q mismatch.
- `BIN_AND_UNBIN_MISMATCH`: P mismatch, Q mismatch.
All outcomes are support-only `+0/+0`, score no science gate and create no WW authority.

Diagnostic-only max absolute differences may be recorded but are never acceptance criteria. No tolerance, `allclose`, rounding, smoothing, averaging, alternate summation order, alternate weights, alternate indexing or post-hoc rescue is permitted.

## Frozen next action
If P is mismatched, the next support gate must be source-bound to the official PyMaster binning arithmetic/order before touching any solve. If P is exact and only Q is mismatched, localize official unbin semantics. If both are exact, only then may a separately preregistered coupling-multiplication/arithmetic-order diagnostic be launched. Exp073DV remains inactive.
