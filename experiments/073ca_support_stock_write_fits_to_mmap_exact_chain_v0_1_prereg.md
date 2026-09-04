# Exp073CA v0.1 — stock write_to -> FITS memmap row-stream -> mmap downstream exact chain

Date frozen: 2026-09-04
Scope: DSIR only; hosted synthetic support/resource QA; accounting always `+0/+0`.

## Purpose
Validate at runtime the memory-stable full-stock chain permitted by Exp073BZ P1 and Exp073BY M1 without using `get_coupling_matrix()`: construct a fresh stock NaMaster-2.7 workspace from synthetic masks, compute the stock full bandpower-window tensor, persist the workspace with stock `NmtWorkspace.write_to()`, release the workspace, open the persisted FITS MCM through read-only memory mapping, stream at most one MCM row at a time into the exact Exp073BY little-endian durable raw layout, and feed that durable file to the frozen Exp073BY mmap downstream emulator.

## Frozen identities
NaMaster runtime version 2.7; GSL 2.7. Reuse frozen Exp073BY C emulator blob `acafb095deafae7602101d8305e239341010ba79` and operation order. Synthetic masks/edges are the same three NSIDE=16/lmax=47 cases used by Exp073BY.

## Memory contract
Forbidden: `w.get_coupling_matrix()`; any second complete in-memory unbinned MCM; `np.array(full_mcm)` / full-image endian copy. FITS must be opened with memmap enabled. Conversion to the durable raw input may materialize at most one source MCM row at a time as canonical `<f8`, then discard it. After stock `write_to()`, the workspace must be destroyed before downstream mmap execution.

## Frozen outcomes
- `C1_EXACT_STOCK_WRITE_TO_MMAP_CHAIN`: all three complete `<f8 [2,8,2,48]` downstream tensors exactly equal the live stock `get_bandpower_windows()` tensor under SHA256 and `numpy.array_equal`, with max abs difference exactly 0.0; memory contract passes.
- `C2_STOCK_WRITE_TO_MMAP_NUMERIC_MISMATCH`: valid lineage/memory contract but any exact mismatch.
- `C3_MEMORY_CONTRACT_FAIL`: full MCM duplicate/materialization or workspace-retention rule violated.
- `C4_SOURCE_LINEAGE_MISMATCH`: frozen NaMaster/GSL/Exp073BY helper identity mismatch.
- `C5_INFRASTRUCTURE_INCOMPLETE`: no valid runtime classification.

No tolerance/closeness acceptance. Workflow success alone is not C1. No DES or historical numerical data may be read. No scientific authority can be created.

## Consequence
C1 closes the full-stock construction/persistence/downstream memory path on synthetic exactness and permits prospective DES-scale resource sizing/checkpoint design for Exp073BU. C2 is a negative exact support result. C3 requires architecture repair without changing arithmetic. C4/C5 require causal repair only.
