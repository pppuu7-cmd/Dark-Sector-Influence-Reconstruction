# Exp073BY v0.1 preregistration — mmap full-MCM downstream exact equivalence

Date: 2026-09-04
Scope: DSIR support QA only; accounting always `+0/+0`; Exp073BU/Wm_S3 scientific authority forbidden.

## Motivation frozen before output
Exp073BX F1 established that the complete stock `ncls=2` downstream route can reproduce NaMaster-2.7 windows bit-for-bit when supplied the complete stock unbinned MCM. The next non-scientific engineering question is whether that complete MCM can be consumed from durable file-backed storage without allocating a second full `(ncls*L)^2` heap array, while preserving the exact stock operation order and output bits.

This gate addresses only the downstream duplicate-memory copy. It does **not** claim to solve the memory cost of constructing or retaining NaMaster's own stock MCM, and cannot authorize DES-scale science.

## Frozen inputs
Reuse exactly the three deterministic Exp073BX synthetic mask cases: NSIDE=16, lmax=47, `ncls=2`, band edges `[0,4,8,12,16,24,32,40,48]`, PyMaster/NaMaster 2.7 and GSL 2.7. No historical or DES numerical data may be read.

Baseline for each case is public stock `NmtWorkspace.get_bandpower_windows()` from that same freshly constructed synthetic workspace. The emulator input is the complete stock unbinned MCM serialized in canonical C-order `<f8` with frozen header/edges.

## Frozen candidate architecture
The C helper must map the serialized MCM payload read-only with POSIX `mmap` and index it directly. It must not allocate or read a second complete `nm*sizeof(double)` MCM heap buffer. All downstream loops and arithmetic must preserve the Exp073BX F1 order exactly:
1. full source-order `ncls=2` binned coupling matrix;
2. GSL LU decomposition;
3. complete source-order `mat_coupled_bin` construction;
4. GSL LU inverse;
5. GSL BLAS `dgemm`;
6. stock raw output order before any TE selection.

A hosted static audit must fail closed if the helper contains a full-MCM `malloc/calloc` or full-MCM `fread` path instead of the frozen read-only mmap path.

## Exact acceptance
For all three complete canonical `<f8 [2,8,2,48]` tensors, both SHA256 equality and `numpy.array_equal` against stock must hold. `max_abs_difference` must therefore be exactly `0.0`. Selected TE equality is recorded as a secondary invariant only. No tolerance or closeness threshold is an acceptance criterion.

## Frozen outcomes
- `M1_EXACT_MMAP_FULL_COMPONENT_EQUIVALENCE`: valid lineage/static memory contract and all three full tensors exact. Support PASS `+0/+0`; permits only a later prospectively frozen audit/implementation for obtaining or persisting a DES-scale full stock MCM without an additional resident duplicate, not science activation.
- `M2_MMAP_FULL_COMPONENT_MISMATCH`: valid lineage/static contract but any exact full-tensor mismatch. Negative support result `+0/+0`; inspect first operation-order/source discrepancy, no tolerance rescue.
- `M3_MEMORY_CONTRACT_FAIL`: source/static audit shows a second complete MCM heap/read copy or the frozen mmap contract is not met. Resource/implementation support FAIL `+0/+0`.
- `M4_SOURCE_LINEAGE_MISMATCH`: provenance BLOCKED `+0/+0`.
- `M5_INFRASTRUCTURE_INCOMPLETE`: infrastructure failure `+0/+0`; diagnose first causal defect prospectively.

Workflow success alone is never M1/M2. Raw receipt/artifact must be inspected. Exp073BU remains NOT ACTIVATED regardless of outcome.
