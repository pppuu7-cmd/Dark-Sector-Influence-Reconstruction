# Exp073EL — WW_S0_S1 full-resolution ordered distinct-field resource-path admission v0.1

**Prospectively preregistered:** 2026-09-06 while Exp073EN `WW_S0_S0` remains terminally unresolved/in progress.

**Status:** `PREREGISTERED_NOT_ACTIVATED`.

**Accounting:** support/resource gate only, `+0/+0`; cannot create `WW_S0_S1` or any dark-sector science authority.

## Frontier lock
Exp073EL MUST NOT be activated unless and until:
1. Exp073EN has produced terminal candidate evidence; and
2. Exp073EO has independently emitted `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, thereby creating valid `WW_S0_S0` authority.

A PASS of Exp073EL may only make `WW_S0_S1` executable. It does not score the science gate.

## Motivation
`WW_S0_S1` is a spin-2 ordered distinct-field correlation. Its unbinned MCM geometry is unchanged from `WW_S0_S0`: `ncls=4`, `nl=12288`, therefore `49152 x 49152` float64 = exactly `19,327,352,832` bytes. Exp073EM/EN establish the regular-file file-backed construction path for this dominant object.

However, unlike auto `S0 -> S0`, exact PyMaster 2.7 public `compute_coupling_matrix()` obtains and retains two distinct mask ALMs while both `NmtField` objects retain their full masks. For NSIDE=4096:
- one float64 mask: `201,326,592 * 8 = 1,610,612,736` bytes = `1.500 GiB`;
- one complex128 mask ALM through `ell=12287`: `75,503,616 * 16 = 1,208,057,856` bytes = `1.125091552734375 GiB`;
- two masks plus two ALMs alone are about `5.25018 GiB` before SHT, Healpy, Python, GSL and NaMaster working memory.

On the current 6-GiB WSL guest this is a distinct resource hazard not closed by the S0 auto-field run.

## Frozen low-memory semantic route
The admissible route is sequential and must preserve the exact PyMaster/NaMaster arithmetic:

1. Reconstruct fresh authoritative `S0` only.
2. Create its exact mask-only spin-2 `NmtField`, compute `get_mask_alms()` with the frozen PyMaster 2.7 settings, persist the exact complex128 ALM payload to a regular file, verify byte hash, then destroy/release the field and full mask before constructing `S1`.
3. Reconstruct fresh authoritative `S1` only and repeat the same operation into a separate ALM file; release field and full mask.
4. Reopen both exact ALM payloads read-only by mmap and compute `healpy.alm2cl(alm0, alm1, lmax=12287)` in the same ordered orientation `S0 -> S1` as stock PyMaster 2.7. Persist/hash the resulting `pcl_mask`, then destroy both ALM mappings before MCM construction.
5. Invoke the exact same `pymaster.nmtlib.comp_coupling_matrix` call and argument order used by PyMaster 2.7 `NmtWorkspace.compute_coupling_matrix()` for isotropic MASTER-normalized spin-2 distinct fields: spins, lmax/lmax_mask, purity flags, `norm_type=0`, `wawb=0`, beam arrays, `pcl_mask.flatten()`, frozen bins, `is_teb=False`, `l_toeplitz=-1`, `l_exact=-1`, `dl_band=-1`.
6. The construction runtime MUST use the Exp073EM-qualified regular-file file-backed unbinned-MCM semantics, with an observed mapping of exactly `19,327,352,832` bytes and `49,152` rows.
7. Serialize the workspace through the ordinary NaMaster FITS writer. The construction workspace/process must then terminate and its temporary MCM backing file must be proven removed before reload.
8. A fresh PyMaster 2.7 process using the Exp073ER-qualified FITS-read file-backed semantics must call `NmtWorkspace.read_from(..., read_unbinned_MCM=True)` and then public `get_bandpower_windows()`. The read mapping must again be exactly `19,327,352,832` bytes / `49,152` rows and be fully cleaned after use.
9. Selected semantics remain exactly `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`.

No Toeplitz approximation, reduced ell range, effective-ell substitution, tolerance, rounding, smoothing, averaging, or numerical rescue is allowed.

## Mandatory prerequisite support chain
Before EL may PASS, all of the following immutable support evidence must be bound by exact artifact/run/blob identity:
- Exp073EM construction-storage exact PASS;
- Exp073EK serialized distinct-field public-BPW repeatability PASS;
- Exp073EP file-backed cross/public-BPW composition exact PASS;
- Exp073ER file-backed FITS-read/public-BPW exact PASS;
- Exp073ET sequential-ALM-spill/direct-lib exact qualifier PASS (prospectively required here; it may be created/run while EN is still unresolved because it is hosted-only and support-only).

A missing prerequisite makes EL `BLOCKED +0/+0`, not a science failure.

## Resource admission requirements
EL is an execution-readiness admission, not a duplicate full-resolution science computation. It must establish, before launching `WW_S0_S1` science:

- exact host identity/runner labels required by the future frozen science workflow;
- WSL available memory configuration at least equivalent to the successfully used EN environment (`memory=6GB`, `processors=8`, file-backed MCM enabled); raising WSL memory on a 7.68-GiB physical host is not required or presumed safe;
- at least **50 GiB free disk** at the chosen science/mmap filesystem before start;
- regular-file creation, `ftruncate`, mmap and cleanup sanity on that filesystem;
- enough disk for the staged peak where one ~18-GiB MCM backing and one ~18-GiB serialized workspace coexist, plus ALM spill files (~2.25 GiB total), BPW output, checkpoints and safety headroom;
- stage ordering that never intentionally retains construction MCM backing, serialized-read MCM backing, and obsolete ALM spills simultaneously when they are no longer needed;
- no competing self-hosted DSIR heavy job.

The `50 GiB` threshold is a conservative resource floor, not a scientific parameter. Failure is `RESOURCE_BLOCKED +0/+0`.

## Exact admission token
Only a future implementation satisfying this preregistration may emit:

`PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_1`

A PASS means only that the exact ordered distinct-field route is admissible for a subsequently frozen `WW_S0_S1` science A/B run.

## Prohibited interpretations
- EL PASS is not `WW_S0_S1` PASS.
- Resource failure is not a dark-sector science failure.
- No numerical result produced during support qualification may be promoted to science authority unless it was prospectively designated as part of a separately frozen science run.
