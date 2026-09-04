# Exp073CC v0.1 — causal verification of Exp073CB FITS mmap backing

Date frozen: 2026-09-04
Scope: DSIR only; hosted synthetic support/resource verification; accounting always `+0/+0`.
Parent: Exp073CB v0.1 run `33829545473`, whose raw numerical result was exact but whose evaluator classified C1 without requiring its recorded `fits_memmap` field to be true.

## Frozen purpose
Verify prospectively whether Astropy `fits.open(..., memmap=True)` for the exact Exp073CB route is genuinely backed by an OS mmap even when the immediate NumPy `.base` is not `np.memmap`. This repairs verification only; masks, NSIDE=16, lmax=47, bin edges, NaMaster-2.7 arithmetic, stock `write_to()`, row-stream conversion, Exp073BY downstream arithmetic and exact equality criteria are unchanged.

## Memory contract
For every frozen case: workspace is destroyed before FITS downstream; `get_coupling_matrix()` remains forbidden; FITS is opened `memmap=True`; the array base-chain must reach `mmap.mmap` and `/proc/self/maps` must show the persisted FITS path while open; at most one source row (`96*8=768` bytes) is canonicalized at a time. No second full MCM materialization is permitted.

## Frozen outcomes
- `V1_VERIFIED_OS_MMAP_AND_EXACT_CHAIN`: all three cases have mmap backing evidence and exact full tensor equality (SHA256 + `numpy.array_equal`, max diff 0.0).
- `V2_NOT_OS_MMAP_BACKED`: numerical exactness valid but any case lacks required mmap backing evidence.
- `V3_MEMORY_CONTRACT_FAIL`: row/materialization/workspace rule fails.
- `V4_SOURCE_LINEAGE_MISMATCH`: frozen source/runtime identities fail.
- `V5_INFRASTRUCTURE_INCOMPLETE`: no valid classification.

No tolerance rescue. No DES/historical numerical data. No Wm_S3 scientific authority can be created. V1 permits Exp073BU DES-scale resource sizing/checkpoint design; V2/V3 require architecture repair.