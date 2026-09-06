# RECOVERY — Exp073ES PASS; Exp073EL created prospectively; Exp073ET running

Date: 2026-09-06

## Science authority unchanged
Exp073EN run `33994398927`, self-hosted job `101382229273`, remains `IN_PROGRESS`. Partial numerical output was not inspected. Therefore `WW_S0_S0` is not yet authority and Article-3 science readiness remains unchanged.

## Exp073ES static EN-to-EO artifact interface PASS
Corrected static-interface workflow:
- run `34000744773`;
- job `101399048496`;
- head `120334d6aa0c86a57742fb7145f5e45cdf208399`;
- conclusion `SUCCESS`.

All steps passed, including frozen identities/syntax and `Verify complete EN-to-EO artifact interface`. The prior ES failure was only a false-positive literal-string check for `A_driver.log`/`B_driver.log`; the production EO auditor uses the correct dynamic expression `f'{rep}_driver.log'`. No EN collector evidence was missing and no production science/admission criterion was weakened.

Classification: support/static PASS `+0/+0`; no WW authority.

## Recovery correction: Exp073EL had been mentioned before it existed
A repository-wide check found no `073el` or `WW_S0_S1` prereg file despite an earlier recovery sentence saying Exp073EL was preregistered. That statement was premature. The inconsistency has now been corrected prospectively, before Exp073EN has any terminal numerical result, by creating:

`experiments/073el_ww_s0_s1_full_resolution_resource_path_v0_1_prereg.md`

Creation commit: `b9650942a83860e403000e59b7b863f247da9ae5`.

Status: `PREREGISTERED_NOT_ACTIVATED`. EL is strictly locked behind real Exp073EO PASS and is support/resource-only `+0/+0`.

## New full-resolution distinct-field memory risk
Exact PyMaster 2.7 source shows mask-only `NmtField` always retains `self.mask`; `lite=True` does not remove this mask. `get_mask_alms()` creates mask ALMs, and public `compute_coupling_matrix()` holds ordered `alm1` and `alm2` simultaneously to call `healpy.alm2cl`.

For NSIDE=4096 / lmax=12287:
- one dense float64 mask = `1,610,612,736` bytes = `1.500 GiB`;
- one complex128 mask ALM has `75,503,616` coefficients = `1,208,057,856` bytes = `1.125091552734375 GiB`;
- two masks plus two ALMs alone are about `5.25018 GiB`, before SHT/Healpy/Python/GSL/NaMaster working buffers.

This is a real distinct-field resource risk on the current 6-GiB WSL guest and cannot be inferred away from the successful auto-field S0->S0 route.

## Sequential low-memory semantic route
The prospective EL route therefore freezes a staged approach:
1. reconstruct one authoritative source count map at a time;
2. build one mask-only spin-2 field, compute exact mask ALM, persist/hash it, then release the field/map;
3. repeat for the other source bin;
4. mmap both exact ALMs read-only and compute the same ordered `healpy.alm2cl`;
5. release ALMs before unbinned MCM construction;
6. call the exact same `pymaster.nmtlib.comp_coupling_matrix` function and argument order used internally by PyMaster 2.7;
7. use Exp073EM-qualified file-backed construction and Exp073ER-qualified file-backed FITS reload/public BPW route.

The existing Article-3 task runner already provides `source_count_map(root, bin_index)` as a pure per-bin reconstruction/validation function. It verifies R1 pixel-record bytes/SHA, pixel range, total selected rows, unique pixels and occupancy SHA before returning the dense float64 map. The future low-memory driver should import and call this same function sequentially for bin 0 then bin 1 rather than changing source reconstruction semantics.

## Exp073ET prospective exact qualifier
Prereg:
`experiments/073et_ww_s0_s1_sequential_alm_spill_direct_lib_exact_v0_1_prereg.md`, blob `6b6ebdfedd0930a7f450ea50d4334d883fb9ab49`.

Qualifier code:
`ci/exp073et_sequential_alm_spill_direct_lib_exact_v0_1.py`, blob `d8054ac06a0037278feb84f59d231680738d7233`.

Hosted workflow activation:
- workflow `Exp073ET sequential ALM spill direct-lib exact v0.1`;
- run `34001003402`;
- activation head `7d06878f5c8ddad6c0c55e733654cfd3d103222b`;
- state at this note: exact PyMaster 2.7 build `IN_PROGRESS`.

ET compares stock public distinct-field semantics against the sequential ALM spill/direct-lib route exactly for ALM spill/reload, ordered mask PCL, full unbinned MCM, full BPW, selected EE<-EE, and direct-lib in-memory versus ordinary FITS fresh public reload. No tolerance rescue is permitted.

Only `PASS_EXP073ET_WW_S0_S1_SEQUENTIAL_ALM_SPILL_DIRECT_LIB_EXACT_V0_1` may satisfy this EL prerequisite. ET remains support-only `+0/+0`.
