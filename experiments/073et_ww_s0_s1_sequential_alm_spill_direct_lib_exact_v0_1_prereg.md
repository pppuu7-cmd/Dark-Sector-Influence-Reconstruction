# Exp073ET — WW_S0_S1 sequential mask-ALM spill + direct-lib exact qualifier v0.1

**Prospectively preregistered:** 2026-09-06 while Exp073EN remains in progress and before Exp073EL can be activated.

**Class:** hosted-only support qualifier, accounting `+0/+0`; no WW science authority may be created.

## Question
Can the memory-heavy public PyMaster 2.7 distinct-field preparation step be replaced, without any numerical change, by a sequential storage route that:
1. computes each mask ALM separately;
2. persists/reloads those ALMs exactly from regular files;
3. computes the same ordered cross-mask pseudo-spectrum with `healpy.alm2cl`;
4. calls the exact same `pymaster.nmtlib.comp_coupling_matrix` function with the exact argument order used internally by public `NmtWorkspace.compute_coupling_matrix()`;
5. wraps the returned workspace and uses ordinary public MCM/BPW/serialization operations?

This qualifier addresses only arithmetic equivalence at small NSIDE. Full-resolution resource admission remains Exp073EL.

## Frozen source and geometry
- NaMaster/PyMaster source commit: `24365fa59a38c15732f4f37e8b29265b75c442d5` (PyMaster 2.7).
- Ordered distinct-field spin-2 geometry: `S0 -> S1`.
- `NSIDE=16`, `lmax=lmax_mask=47`.
- Edges `[0,6,12,18,24,30,36,42,48]`, 8 bands.
- Isotropic masks, `purify_e=False`, `purify_b=False`.
- `normalization='MASTER'`, therefore `norm_type=0`, `wawb=0`.
- `is_teb=False`, `l_toeplitz=-1`, `l_exact=-1`, `dl_band=-1`.
- Unit beams exactly as public PyMaster uses when `beam=None`.
- Deterministic distinct masks identical in construction to the established EK/ER small-NSIDE ordered-cross support geometry.

## Stock route
Construct both mask-only spin-2 fields simultaneously and run ordinary public:
`NmtWorkspace.compute_coupling_matrix(f0, f1, bins)`.
Capture:
- ordered mask PCL from the same field mask ALMs;
- full unbinned coupling matrix via public `get_coupling_matrix()`;
- full public bandpower windows via `get_bandpower_windows()`;
- selected `EE<-EE` block.

## Sequential spill route
For S0 and S1 independently and in order:
- construct one mask-only field;
- call public `get_mask_alms()`;
- persist the exact complex128 array with NumPy lossless storage;
- verify exact SHA/array equality after mmap reload;
- release that field and mask before processing the other field.

Then mmap both persisted ALMs read-only and compute `healpy.alm2cl(alm0, alm1, lmax=47)`. No arithmetic transformation, rounding or dtype conversion is allowed.

Create a bare `NmtWorkspace`, set its internal workspace pointer to the result of the exact same `pymaster.nmtlib.comp_coupling_matrix` call and arguments appearing in PyMaster 2.7 `workspaces.py` for this frozen case, and set `has_unbinned=True`. Use ordinary public `get_coupling_matrix()`, `get_bandpower_windows()`, `write_to()`, fresh `read_from(..., read_unbinned_MCM=True)` and fresh public `get_bandpower_windows()`.

## Exact PASS requirements
`PASS_EXP073ET_WW_S0_S1_SEQUENTIAL_ALM_SPILL_DIRECT_LIB_EXACT_V0_1` requires all of the following bit-for-bit:
- each spilled ALM equals its pre-spill ALM by shape, canonical complex128 SHA256 and `numpy.array_equal`;
- stock ordered cross-mask PCL equals sequential-spill ordered cross-mask PCL by shape, canonical float64 SHA256, `numpy.array_equal` and max absolute difference `0.0`;
- stock public full unbinned MCM equals sequential/direct-lib MCM exactly;
- stock public full BPW equals sequential/direct-lib public BPW exactly;
- stock selected `EE<-EE` equals sequential/direct-lib selected `EE<-EE` exactly;
- direct-lib in-memory BPW equals BPW after ordinary FITS `write_to` then fresh public `read_from(..., read_unbinned_MCM=True)` exactly;
- all numerical arrays finite;
- ordered masks are demonstrably distinct;
- no tolerance, `allclose`, rounding, smoothing, averaging, approximate Toeplitz route, or rescue.

A mismatch is `FAIL_EXP073ET...`, support-only `+0/+0`, and does not constitute a dark-sector science failure.

## Frontier effect
A PASS only supplies the missing arithmetic prerequisite for Exp073EL. Exp073EL itself remains locked behind real Exp073EO admission of `WW_S0_S0` authority.
