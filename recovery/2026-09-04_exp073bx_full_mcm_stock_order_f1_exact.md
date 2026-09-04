# Exp073BX v0.1 — F1 exact full-stock-order equivalence

Date: 2026-09-04
Scope: DSIR only; support QA `+0/+0`; no Wm_S3 scientific authority.

## Authority
- preregistration: `experiments/073bx_support_full_mcm_stock_order_equivalence_v0_1_prereg.md`, commit `adf5e1152673d8b8fd0247eb636b62cfa273af5c`
- activation/head: `7c26b00968b64d148639b393b05f446b02356665`
- workflow run/job: `33820895190` / `100863112761`
- artifact: `9918240620`
- artifact ZIP SHA256: `02aa1b97e4281faca88be2d20ef836c137919529712a6de2be8c5bbf273cb214`
- runtime: PyMaster 2.7; GSL 2.7; frozen `workspaces.py` SHA256 `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`

## Raw frozen result
`F1_EXACT_FULL_STOCK_ORDER_EQUIVALENCE`

All three prospectively frozen NSIDE=16/lmax=47 synthetic cases matched the stock NaMaster-2.7 complete canonical `<f8 [2,8,2,48]` tensor exactly under both SHA256 and `numpy.array_equal`; every max absolute difference was exactly `0.0`. The selected TE slice was also exact in every case. The artifact explicitly records `historical_or_des_data_read=false`, `science_gate_scored=false`, `wm_s3_authority_created=false`, and `no_tolerance_rescue=true`.

The exact emulated route was:
`stock full unbinned MCM -> source-order full ncls=2 binning -> GSL LU invert -> GSL BLAS dgemm -> stock raw ordering`.

## Classification
**F1 support PASS `+0/+0`, NON-SCIENTIFIC, NON-AUTHORIZING.** Workflow success alone was not used; the raw receipt and artifact digest were inspected.

## Consequence
Together with Exp073BV R1 and Exp073BW G2, F1 localizes the previous ~1e-15 exact discrepancy to the selected/general-coupling reduction, not to the Python wrapper, raw layout, GSL solver itself, or unavoidable floating-point nondeterminism. Full `ncls=2` stock operation order can reproduce stock output bit-for-bit.

F1 permits only a new prospectively frozen memory-scalable **full-component** MCM/window implementation QA. It does not activate Exp073BU science and does not permit importing historical Wm_S3 numerical PCL/window/band payloads.
