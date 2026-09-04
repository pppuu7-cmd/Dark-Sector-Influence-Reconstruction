# Exp073BW v0.1 — G2 selected construction not exact

Date: 2026-09-04
Scope: DSIR only.
Accounting: `+0/+0`; no Wm_S3 scientific authority.

## Frozen authority
Preregistration: `experiments/073bw_support_gsl_selected_solver_equivalence_v0_1_prereg.md`, commit `c43cce294816e04e25e59c6e9410185d0962d621`, blob `e66c1e5d7a2f4593bfa8daf302663887790d44d2`.
Python helper: `ci/exp073bw_gsl_selected_solver_equivalence_v0_1.py`, commit `d58e57925f1dd1a9abab9b50ce4a50a798e720d0`, blob `22c0cb391931e578f92c7ce75c4dba3429e09265`.
C/GSL helper: `ci/exp073bw_gsl_selected_solver_equivalence_v0_1.c`, commit `b87405206145228f0e0fbde6ae0447407fe8a308`, blob `c247d449ecaec12ab05975181f0a05e4c3ac52fe`.
Workflow implementation: `f0dd8538b986ad6f7a9427fee9230a5ddc254ad3`.
Activation/head: `0b5ad0f0addb22ce4691ae6c3349b323095a342e`.

## Terminal run consumed
- workflow run `33820436824`
- job `100861744518`
- head `0b5ad0f0addb22ce4691ae6c3349b323095a342e`
- job conclusion SUCCESS
- artifact `9918084336`
- artifact digest `sha256:ec51bf2b0e66a9eaf1c2dcda4afbfd83b0bc6ba2d983a60366a5f1126967368a`
- runtime PyMaster `2.7`
- GSL runtime/header exactly `2.7`

Workflow success alone was not used for classification. The uploaded JSON artifact was downloaded and inspected directly.

## Raw result
Status: `G2_SELECTED_CONSTRUCTION_NOT_EXACT`.

The frozen C helper successfully compiled against the conda GSL 2.7 environment and used `gsl_linalg_LU_decomp` once followed by `gsl_linalg_LU_solve` for each RHS ell column in increasing frozen order. Thus the gate directly tested whether substituting stock-family GSL LU for NumPy/OpenBLAS solve is sufficient while keeping the selected/general-coupling A/K construction fixed.

All three prospectively frozen synthetic cases remained non-exact against stock:

### Case 0
- stock SHA256 `c015d6a2b33bdc4ba5572d90e30a0144f49e8de927fdc5ab338687bc0e5a6c30`
- GSL-selected SHA256 `91d724a20bc8bc85f319de67530f784f2bd60a63952af5c202bfc28d111adf42`
- NumPy-selected SHA256 `30ec42f1f6dc01888dfed12079ba17017e710187a714b92ead0cfed0b4d693e1`
- stock-vs-GSL `numpy.array_equal=false`, SHA unequal
- max abs stock-vs-GSL `1.4710455076283324e-15`
- max abs stock-vs-NumPy `1.4710455076283324e-15`

### Case 1
- stock SHA256 `73a680485f140669b46aeb42ad724b55fc55e57742ebd8df3f4706e039736859`
- GSL-selected SHA256 `6bfce1c27b26b2bf029fa8635aeeafe3043139242221b28da3708aa938a51bd4`
- NumPy-selected SHA256 `faceb8798c488f0306ed5992a227d288c734cc0b1f3ac558a5eaf8d3888f410d`
- stock-vs-GSL exact false
- max abs stock-vs-GSL `1.3600232051658168e-15`
- max abs stock-vs-NumPy `1.3739009929736312e-15`

### Case 2
- stock SHA256 `96d49270b1ebc8989f1ed3aaaaaeac1c1e04860b8f0f44ec4a2f413ca66f8900`
- GSL-selected SHA256 `052054ad3967640e8fdf5650b25232420d39bacb7a00df59d1ef46eb22b6036a`
- NumPy-selected SHA256 `9fca198777649d59540ee5a94da6674ac17baba1530bfe66a9db3a08e3b008a8`
- stock-vs-GSL exact false
- max abs stock-vs-GSL `1.4155343563970746e-15`
- max abs stock-vs-NumPy `1.4016565685892601e-15`

Receipt explicitly records `historical_or_des_data_read=false`, `science_gate_scored=false`, `wm_s3_authority_created=false`, and `no_tolerance_rescue=true`.

## Classification
**G2_SELECTED_CONSTRUCTION_NOT_EXACT — negative support result `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING.**

The frozen hypothesis that the earlier Exp073BU Q2 discrepancy is caused solely by NumPy/OpenBLAS solve order is falsified. Replacing only `np.linalg.solve` with GSL LU does not recover exact stock NaMaster output.

Together with Exp073BV R1, the remaining exact discrepancy is localized deeper: the selected/general-coupling reduction (including its single-component construction and/or accumulation order) is not an exact substitute for the full stock spin-0 x spin-2 `ncls=2` C/GSL operation route.

No tolerance, rounding, smoothing or averaging may rescue this result. Historical Q2 and G2 remain immutable negative support findings.

## Exact next permitted gate
Implement and prospectively test the **full-component stock C/GSL operation order**, preserving the stock `ncls=2` block structure, stock unbinned-to-binned accumulation order, GSL LU decomposition and stock bandpower-window solve/accumulation before selecting TE. The first test must remain hosted/synthetic `+0/+0` and require exact complete-tensor SHA256 plus `numpy.array_equal` against stock NaMaster 2.7 on multiple deterministic masks. Only exact full-component equivalence can authorize later integration into Exp073BU scientific A/B; it does not itself create Wm_S3 authority.