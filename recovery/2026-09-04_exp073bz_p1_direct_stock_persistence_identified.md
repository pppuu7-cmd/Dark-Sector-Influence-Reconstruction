# Exp073BZ v0.1 — P1 direct stock persistence route identified

Date: 2026-09-04
Scope: DSIR only.

## Authority
- prereg commit `7b195315923ffb13594242a6555afa9589259f72`
- workflow commit `fd40f2290eaa2dc9c6f11b09f8b794176e1c821f`
- activation/head `0e8bba344a704e489fd56b96ad4bfe076ce8d0de`
- run/job `33827802518` / `100884088964`
- artifact `9920579918`
- artifact ZIP SHA256 `b41c6ceca73a18ac01ee7c742b06e3e947ad345ea217155a67893891cc003db8`
- upstream NaMaster commit `24365fa59a38c15732f4f37e8b29265b75c442d5`
- exact source SHA256: `src/nmt_io.c` = `b910ae1acc3e80c3bb2e263ebed8b7fc591650c9eb4194f8a465774e687ca012`; `pymaster/workspaces.py` = `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`.

## Raw result
`P1_DIRECT_STOCK_PERSISTENCE_WITHOUT_SECOND_FULL_MCM_COPY_IDENTIFIED`.

Exact source evidence shows `NmtWorkspace.write_to()` calls `lib.write_workspace(self.wsp, "!"+fname)` directly after `check_unbinned()`. In `src/nmt_io.c`, `nmt_workspace_info_tohdus` iterates rows and calls `fits_write_pix(..., w->coupling_matrix_unbinned[ii], ...)`, writing each workspace-owned unbinned-MCM row directly to CFITSIO. The stock persistence path therefore does not require `get_coupling_matrix()` or a second complete full-MCM materialization.

## Classification
Support/source PASS `+0/+0`, NON-SCIENTIFIC, NON-AUTHORIZING. Wm_S3 authority remains absent; Exp073BU remains NOT ACTIVATED.

## Next permitted gate
Prospectively test the runtime chain: stock `write_to()` -> durable FITS -> bounded-memory row/chunk conversion or direct mapped view -> Exp073BY exact mmap downstream, requiring full stock tensor exact SHA256 + `numpy.array_equal` against the live workspace result on multiple synthetic masks. No DES/historical numerical data and no tolerance rescue.
