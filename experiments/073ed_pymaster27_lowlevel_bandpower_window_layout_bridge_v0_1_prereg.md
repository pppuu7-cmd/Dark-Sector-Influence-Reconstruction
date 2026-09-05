# Exp073ED — PyMaster 2.7 low-level bandpower-window layout bridge audit v0.1

Scope: DSIR only. Hosted support/diagnostic only `+0/+0`; no WW authority may be created.

Motivation: Exp073DZ established the actual PyMaster 2.7 reload-state API: `NmtWorkspace.bpws`, `mcm`, and `mcm_binned` are absent; `wsp.bin`, `wsp.ncls`, `wsp.lmax`, `wsp.lmax_fields`, and `wsp.norm_type` are present. The frozen PyMaster 2.7 source implements `NmtWorkspace.get_bandpower_windows()` by calling `pymaster.nmtlib.get_bandpower_windows(self.wsp, size)`, reshaping the returned 1-D buffer as `[n_bands,ncls,lmax+1,ncls]`, then transposing axes `[1,0,3,2]`.

Frozen diagnostic: on GitHub-hosted Ubuntu with PyMaster 2.7, construct a deterministic distinct spin-2 S0→S1 cross-workspace at NSIDE=16 and `ell=0..47`, serialize and reload it, then obtain (a) the public `wr.get_bandpower_windows()` tensor and (b) the direct low-level `pymaster.nmtlib.get_bandpower_windows(wr.wsp, size)` buffer. Reconstruct the public tensor using exactly the source-defined reshape `[n_bands,ncls,lmax+1,ncls]` and transpose `[1,0,3,2]`. Compare direct-low-level reconstruction with public output using SHA256 and `numpy.array_equal` only. Also record the direct buffer shape/dtype and the exact tensor shape.

Frozen classifications:
- `LOWLEVEL_LAYOUT_EXACT`: direct low-level reconstruction has identical canonical `<f8` SHA256 and `numpy.array_equal=true` against public output.
- `LOWLEVEL_LAYOUT_MISMATCH`: the exact comparison fails.
- Any exception, missing symbol, version mismatch, malformed shape or artifact is `INFRASTRUCTURE/SOFTWARE_INCOMPLETE +0/+0`.

No tolerance, allclose, rounding, smoothing, averaging, permutation search, transpose search, numerical rescue, science scoring, adapter modification or WW authority is allowed. This experiment does not decide whether a future scalable adapter is admissible; it only establishes the exact authoritative buffer/layout bridge prospectively.