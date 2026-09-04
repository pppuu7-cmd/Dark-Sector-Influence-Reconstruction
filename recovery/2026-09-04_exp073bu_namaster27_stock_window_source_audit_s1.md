# Exp073BU support — NaMaster 2.7 stock-window source audit S1

Date: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.
Accounting: `+0/+0`; no Wm_S3 scientific authority created.

## Prospective authority

Preregistration: `experiments/073bu_support_namaster27_stock_window_source_audit_v0_1_prereg.md`
Preregistration commit: `798eabda7fa7ba2cbe28262fdb37fb4970327431`
Frozen upstream: `LSSTDESC/NaMaster`, tag `v2.7`, commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.

Frozen classification S1 permits only a later prospectively frozen exact-stock emulator/equivalence QA. It does not activate Exp073BU Wm_S3 science.

## Terminal run consumed

- workflow run: `33816987697`
- hosted job: `100851195938`
- workflow/head SHA: `d80042807faf26f29eeb2a11e026632bba0083b4`
- workflow conclusion: SUCCESS
- raw receipt status: `S1_STOCK_OPERATION_ROUTE_IDENTIFIED`
- raw token: `PASS_EXP073BU_NAMASTER27_STOCK_WINDOW_SOURCE_AUDIT_EXECUTED_V0_1`
- artifact id: `9916910028`
- artifact digest: `sha256:edde986db34cd3311ff52936ba20db1bb2732e51f0061d9942da8b60fdc0047e`
- runtime PyMaster: `2.7`

Workflow SUCCESS alone was not treated as authority. The raw receipt and pinned source evidence were inspected.

## Exact source/provenance evidence

Pinned and installed `pymaster/workspaces.py` SHA256 agree:
`442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`.

Other pinned source SHA256 values recorded by the receipt:
- `pymaster/namaster.i`: `4d980d...` (receipt is authoritative for the full value)
- generated `namaster_wrap.c`: `35b5f6...`
- `pymaster/nmtlib.py`: `3c82b2...`
- `src/nmt_master.c`: `9492eb...`
- `src/namaster.h`: `ae293...`

The exact public Python wrapper route is identified as `NmtWorkspace.get_bandpower_windows()` -> `lib.get_bandpower_windows(...)`, returning the library result reshaped to `[n_bands,ncls,lmax+1,ncls]` and transposed to stock `[ncls,n_bands,ncls,lmax+1]`.

The pinned C route in `src/nmt_master.c` is also identified sufficiently to recover stock operation order. The source shows:
1. binning of the unbinned coupling matrix with explicit nested loops over spectrum blocks, output/input bands and ell indices;
2. GSL LU decomposition of the binned coupling matrix;
3. `nmt_compute_bandpower_windows` construction through `nmt_coupling_matrix_binning` and explicit source-order accumulation against the unbinned coupling matrix, beam product, bin weights and `f_ell` ratios.

This closes the prior source-opacity question prospectively as S1. It does not imply that the previously tested selected compact implementation is exact: that implementation remains Q2 numeric-only with `numpy.array_equal=false` and cannot substitute for stock semantics.

## Classification

**S1_STOCK_OPERATION_ROUTE_IDENTIFIED — PASS for this support source-audit gate, accounting `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING.**

No DES/R1/Wm numerical data were read by this audit. No home runner was used. No frozen science criterion, tolerance, domain or arithmetic was changed.

## Consequence / exact next permitted gate

A later support experiment may now be prospectively preregistered to test an exact-stock, memory-stable implementation against stock NaMaster 2.7 on deterministic synthetic masks. The QA must require exact canonical SHA equality and `numpy.array_equal`; numerical closeness alone must not authorize scientific substitution. It must remain hosted-only and `+0/+0` until exact equivalence is demonstrated. Only an exact-stock-compatible full-component path may later be integrated into Exp073BU A/B after its own static/provenance audits.

At time of consumption, Actions reconciliation showed no queued or in-progress DSIR run and `DSIR-HOME-PC` remained FREE. Wm_S3 scientific authority remains absent.