# Exp073BV v0.1 — R1 exact wrapper/raw-layout equivalence

Date: 2026-09-04
Scope: DSIR only.
Accounting: `+0/+0`; no Wm_S3 authority.

## Frozen authority
Preregistration: `experiments/073bv_support_stock_wrapper_raw_layout_equivalence_v0_1_prereg.md`, commit `4f05c390f3fc0f3bd3086acc7ba2c40fbaed514b`, blob `c54ee6422183bc8f1c5f9ba8c38d617a4104e2f0`.
Helper: `ci/exp073bv_stock_wrapper_raw_layout_equivalence_v0_1.py`, commit `f73c7a722fda54bf328741079a9beee771115983`, blob `73d8cb082712f887f35eb522137a0fd6dcc81fb0`.
Activation/head: `dd91b8dd9c7f8c0acc059b7f7133087701a3f2ad`.

## Consumed run
- run `33820184200`
- job `100860976434`
- workflow/head `dd91b8dd9c7f8c0acc059b7f7133087701a3f2ad`
- workflow conclusion SUCCESS
- artifact `9917999087`
- digest `sha256:418fa4b29bcf1cce247615f1309c5a945386dea1899510ee86430c8c7f5fd771`
- runtime PyMaster `2.7`

Freeze/static identities passed before numerical execution. Runtime `pymaster/workspaces.py` SHA256 matched the S1 authority `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`.

## Raw result
Status: `R1_EXACT_WRAPPER_RAW_LAYOUT_EQUIVALENCE`.

All three prospectively frozen deterministic synthetic cases produced exact complete-tensor equality between public `w.get_bandpower_windows()` and direct `pymaster.nmtlib.get_bandpower_windows(w.wsp,size)` followed only by the stock reshape/transpose. Shape in every case: `[2,8,2,48]`, dtype `<f8`.

Case 0 SHA both routes: `b442ac07b7cef6da102319330b181c13cbbe4b8bcfeb64822d523b76158a8d94`.
Case 1 SHA both routes: `1e4c1b5faaf9100f8e8218e9ff83eead408db6fa9784df3cf8f1fd207a61069d`.
Case 2 SHA both routes: `0fb60918684226fafae86c8d77b6f1d819cd8b37959ffcc0e11c26caa0160a0f`.

For every case: `numpy.array_equal=true`, SHA equality true, max absolute difference exactly `0.0`.

## Classification
**R1 exact support PASS `+0/+0`, NON-SCIENTIFIC, NON-AUTHORIZING.**

This closes the Python wrapper/raw-layout layer as a source of the earlier Exp073BU Q2 ~1.47e-15 discrepancy. Under the frozen evidence, that discrepancy is downstream of replacing the stock C/GSL numerical computation, not in stock wrapper reshape/transpose semantics.

No tolerance, rounding, smoothing or averaging was used. No DES/physical DSIR data were read. Home runner was not used.

## Exact next permitted gate
Prospectively preregister and test the stock C/GSL operation-order path itself on deterministic synthetic workspaces. Exact whole-array equality remains required. The next QA must distinguish whether the earlier Q2 comes from (a) NumPy/OpenBLAS solution/decomposition order versus stock GSL LU, or (b) a deeper difference in the compact/general-coupling construction/accumulation. No science activation is permitted until an exact stock-compatible full-component implementation is demonstrated and separately audited.