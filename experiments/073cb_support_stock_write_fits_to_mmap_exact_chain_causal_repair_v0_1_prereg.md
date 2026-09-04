# Exp073CB v0.1 — causal repair of Exp073CA stock write_to -> FITS memmap -> mmap exact chain

Date frozen: 2026-09-04
Scope: DSIR only; hosted synthetic support/resource QA; accounting always `+0/+0`.
Parent: Exp073CA v0.1, failed Actions run `33827950939` with `C5_INFRASTRUCTURE_INCOMPLETE`-type execution failure before three-case classification.

## Causal diagnosis
Exp073CA passed its frozen helper identity audit, exact NaMaster 2.7 runtime/GSL lineage checks, and compilation of the frozen Exp073BY mmap downstream emulator. Execution then stopped because the Python helper's forbidden-operation guard searched its own source for the contiguous token `.get_coupling_matrix(` while embedding that exact token inside the assertion itself. This is a self-referential infrastructure guard defect, not a numerical or scientific result.

## Frozen repair scope
The only permitted behavioral change relative to Exp073CA is construction of the forbidden source token from split string fragments before checking the source. The contiguous forbidden token remains absent from the helper source. No masks, bin edges, NSIDE, lmax, stock NaMaster operations, FITS persistence route, row-stream layout, Exp073BY emulator, exactness criteria, memory criteria, or outcomes may change.

Frozen repaired helper Git blob: `d7921bfb58aa88b6f4c20121ca3c41209d0e590b` (`ci/exp073cb_stock_write_fits_to_mmap_exact_chain_v0_1.py`).
Frozen Exp073BY downstream emulator Git blob: `acafb095deafae7602101d8305e239341010ba79` (`ci/exp073by_mmap_full_mcm_downstream_v0_1.c`).
NaMaster runtime version: 2.7; GSL lineage: 2.7.
Synthetic masks/edges: exactly the same three NSIDE=16/lmax=47 cases as Exp073CA/Exp073BY.

## Memory contract
Forbidden at runtime: `NmtWorkspace.get_coupling_matrix()`; any second complete in-memory unbinned MCM; `np.array(full_mcm)` / full-image endian copy. FITS must be opened with memmap enabled. Conversion to durable raw input may materialize at most one source MCM row at a time as canonical `<f8`, then discard it. After stock `write_to()`, the workspace must be destroyed before downstream mmap execution.

## Frozen outcomes
- `C1_EXACT_STOCK_WRITE_TO_MMAP_CHAIN`: all three complete `<f8 [2,8,2,48]` downstream tensors exactly equal live stock `get_bandpower_windows()` under SHA256 and `numpy.array_equal`, with max abs difference exactly 0.0; memory contract passes.
- `C2_STOCK_WRITE_TO_MMAP_NUMERIC_MISMATCH`: valid lineage/memory contract but any exact mismatch.
- `C3_MEMORY_CONTRACT_FAIL`: full MCM duplicate/materialization or workspace-retention rule violated.
- `C4_SOURCE_LINEAGE_MISMATCH`: frozen NaMaster/GSL/Exp073BY/helper identity mismatch.
- `C5_INFRASTRUCTURE_INCOMPLETE`: no valid runtime classification.

No tolerance/closeness acceptance. Workflow success alone is not C1. No DES or historical numerical data may be read. No scientific authority can be created.

## Consequence
C1 closes the synthetic exact full-stock construction/persistence/downstream memory route after the causal repair and permits prospective DES-scale resource sizing/checkpoint design for Exp073BU. C2 is a negative exact support result. C3 requires architecture repair without changing arithmetic. C4/C5 require causal repair only.
