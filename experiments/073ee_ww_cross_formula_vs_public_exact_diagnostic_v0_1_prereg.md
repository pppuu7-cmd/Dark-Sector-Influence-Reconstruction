# Exp073EE — WW distinct-field reconstruction formula vs public exact diagnostic v0.1

Status: PROSPECTIVELY FROZEN SUPPORT-ONLY `+0/+0`.

Purpose: after Exp073DX excluded FITS orientation and Exp073ED excluded the PyMaster 2.7 low-level/public tensor-layout bridge, isolate whether the current saved-FITS downstream emulator's mathematical reconstruction formula (before choice of GSL LU/BLAS backend) is itself exactly equivalent to official serialized→reloaded PyMaster 2.7 `get_bandpower_windows()` for a distinct spin-2 S0→S1 workspace.

Frozen setup: PyMaster 2.7; nside=16; lmax=47; `nl=48`; four spectra; edges `[0,6,12,18,24,30,36,42,48]`; deterministic distinct masks exactly as Exp073DW; construct W01, serialize to FITS, reload through `NmtWorkspace.read_from`; materialize the reloaded coupling matrix only inside this small hosted diagnostic.

Frozen formula under test: reproduce the current emulator exactly in NumPy: row/column flattened index `ncls*ell+icl`; binned coupling `K[(b2,a),(b3,b)] = sum_{ell2 in b2} sum_{ell3 in b3} M[(ell2,a),(ell3,b)] / width(b2)`; unbinned right matrix `R[(b1,a),(ell2,b)] = sum_{ell1 in b1} M[(ell1,a),(ell2,b)] / width(b1)`; reconstructed window is `solve(K,R)` and is reshaped only to canonical `[ncls,nb,ncls,nl]` in the same output ordering as the C emulator.

Exact-only comparisons: canonical SHA256 and `numpy.array_equal` between reconstructed and official public reloaded windows; selected `EE<-EE` SHA/equality; no tolerance, allclose, rounding, smoothing or averaging may affect classification. Max-abs difference may be recorded for diagnosis only.

Frozen classification: `FORMULA_EXACT` iff full and selected arrays are bitwise equal and SHA-equal; otherwise `FORMULA_MISMATCH`. Either result is support-only `+0/+0`, creates no WW authority and does not alter any frozen science gate. If `FORMULA_MISMATCH`, do not test or tune rescue variants in this experiment; subsequent diagnostics must be separately preregistered. If `FORMULA_EXACT`, a later separately preregistered diagnostic may isolate solver/backend arithmetic.
