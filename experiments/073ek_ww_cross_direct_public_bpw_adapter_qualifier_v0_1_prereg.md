# Exp073EK — WW distinct-field direct-public BPW adapter qualifier v0.1

Status: prospectively frozen support/readiness qualifier only; accounting `+0/+0`.

Exp073EJ established that even columnwise public `decouple_cell` composition is not bitwise identical to public `get_bandpower_windows()`. Therefore no algebraic or decouple-composed reconstruction is admissible for exact production authority. Exp073EK tests the minimal direct adapter: serialize one distinct S0->S1 PyMaster 2.7 workspace, reload it independently twice, call only `get_bandpower_windows()` on each reload, select exactly `EE<-EE` as `[0,:,0,:]`, canonicalize to contiguous little-endian `<f8`, and require exact SHA256 plus `numpy.array_equal` for both full `[4,8,4,48]` and selected `[8,48]` arrays.

Frozen PASS: `DIRECT_PUBLIC_BPW_ADAPTER_EXACT` only if both full and selected arrays are exact across independent reloads, shapes/version/distinct masks are correct, and no tolerance rescue is used. Otherwise `DIRECT_PUBLIC_BPW_ADAPTER_FAIL`. Both outcomes `+0/+0`; no WW authority.

No manual P/Q, inverse, decouple composition, alternate layout, tolerance/allclose, rounding, smoothing, averaging or result-dependent retry.

On PASS, direct serialized-FITS reload + public `get_bandpower_windows()` becomes the only qualified exact cross-workspace adapter candidate for a separate full-resolution resource/readiness gate; Exp073DV remains inactive until that gate and WW_S0_S0 authority prerequisites pass. On FAIL, exact cross-workspace adapter remains blocked.