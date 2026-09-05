# Exp073EM — NaMaster 2.7 file-backed unbinned-MCM exact-storage qualifier v0.1 preregistration

Prepared prospectively after Exp073DT attempt 5 was manually stopped for resource safety on DSIR-HOME-PC. This is infrastructure/support only `+0/+0`. It does not score a WW science gate and cannot create WW authority.

## Motivation
At frozen WW full resolution, `ncls=4` and `nl=12288`, so the unbinned MCM has `49152 x 49152` float64 elements: exactly `19,327,352,832` bytes = `18 GiB` before field, GSL, Python and temporary-memory overhead. Exp073DT attempt 5 telemetry on the 7.68-GiB host / 6-GiB WSL guest showed near-total RAM occupancy and rapid swap growth, establishing that the stock heap-backed full MCM is not operationally safe on DSIR-HOME-PC.

NaMaster 2.7 itself allocates `coupling_matrix_unbinned` as a complete dense matrix in `nmt_workspace_new` before computing or binning it. The scientific arithmetic is not to be changed in this qualifier.

## Candidate infrastructure repair
Build a pinned NaMaster/PyMaster 2.7 variant in which only the storage backend for `nmt_workspace::coupling_matrix_unbinned` is changed when an explicit DSIR low-memory environment switch is set.

Required implementation semantics:
- keep the public PyMaster API unchanged;
- keep all MCM element formulas, OpenMP loop bodies, loop ordering, `bin_coupling_matrix`, beam/bin factors, GSL LU decomposition/inversion/solve, FITS workspace serialization and public `get_bandpower_windows()` arithmetic unchanged;
- replace only the unbinned-MCM heap allocation with a regular-file-backed `mmap(MAP_SHARED)` region created by `mkstemp` + `ftruncate` and exposed through the same row-pointer interface expected by NaMaster;
- preserve fresh-zero initialization semantics of the stock `calloc` allocation;
- add explicit workspace bookkeeping so destruction performs `munmap`, `close` and unlink/cleanup rather than `free` on mapped rows;
- fail closed if the mmap file cannot be created, sized, mapped, or verified;
- do not use anonymous mmap/tmpfs/memfd as the full-resolution backing store, because that would move pressure back to RAM/swap instead of disk;
- nested BLAS/OpenMP/MKL/OpenBLAS/NumExpr/BLIS threads remain pinned exactly as in the frozen DSIR execution contract.

The backing file is infrastructure only and is not science authority. It may be unlinked immediately after successful mapping so the kernel cleans it on process termination, provided `/proc/<pid>/maps` and descriptor/stat evidence are captured before unlink semantics obscure provenance. Otherwise it must be atomically named under the frozen checkpoint namespace and removed only after the workspace is safely serialized.

## Exact qualifier matrix
Run stock PyMaster 2.7 and patched PyMaster 2.7 under the same compiler/runtime/thread contract on prospectively frozen small-NSIDE cases including:
1. spin-2 auto field `S0 -> S0`;
2. a second independent spin-2 auto field;
3. ordered distinct spin-2 cross field `S0 -> S1`.

For every case, compare without tolerance:
- serialized `WSP_PRIMARY` array shape/dtype and `numpy.array_equal`;
- canonical SHA256 of `WSP_PRIMARY` values;
- public `NmtWorkspace.get_bandpower_windows()` full tensor shape/dtype and `numpy.array_equal`;
- canonical full-window SHA256;
- selected `EE<-EE` shape/dtype, `numpy.array_equal` and canonical SHA256;
- finite-value checks;
- frozen bin edges and mask/source identities;
- proof that the patched unbinned matrix is backed by a regular filesystem mapping rather than anonymous memory/tmpfs;
- no tolerance, rounding, allclose, smoothing, averaging or fallback arithmetic.

A FITS-container byte-for-byte SHA is not itself required because container metadata may differ; the numerical arrays and frozen provenance are the authority for this storage qualifier.

## Acceptance tokens
`PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1` requires every exact check above to pass for every frozen case and the storage proof to be valid.

`FAIL_EXP073EM_NAMASTER27_FILEBACKED_MMAP_ARITHMETIC_V0_1` applies if any stock-vs-patched numerical array differs bitwise. Such a result forbids use of the patch for science.

`RESOURCE_FAIL_EXP073EM_FILEBACKED_MMAP_V0_1` applies only if the arithmetic remains well-defined but the mapped implementation cannot run inside the prospectively frozen small-NSIDE resource envelope. Dependency/build/provenance failures are `BLOCKED +0/+0`.

All outcomes are support-only `+0/+0`; `science_gate_scored=false`; `ww_authority_created=false`.

## Full-resolution activation prerequisite after PASS
No full-resolution run may use the patch until:
- the exact qualifier passes;
- the patched source tree, patch file, compiler identity and resulting PyMaster/libnmt build hashes are frozen;
- no competing self-hosted DSIR heavy process is queued or in progress;
- the WSL backing filesystem has sufficient real free disk for the mapped unbinned MCM plus serialized workspace and safety headroom. For the current WW geometry the raw mapped MCM alone is exactly 18 GiB, and mapping plus workspace serialization can temporarily require roughly 36 GiB; target at least 40 GiB genuinely free before activation;
- runtime telemetry captures RAM, swap, backing-file size, disk free space and process state throughout the full-resolution gate.

After Exp073EM PASS, the patched storage backend may be used first to re-run the frozen `WW_S0_S0` authority path without changing science arithmetic. Only after valid `WW_S0_S0` authority/provenance closure may the distinct-field frontier advance. Exp073EL remains preregistered but must not be activated on stock heap-backed NaMaster; it may be executed only after an exact-qualified low-memory storage path is bound prospectively to its resource gate.

Status: `PREREGISTERED_NOT_ACTIVATED`; `science_gate_scored=false`; `ww_authority_created=false`.
