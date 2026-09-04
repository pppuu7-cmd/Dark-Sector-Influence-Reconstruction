# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-04  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`).

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoint branches outrank chat wording. Historical scientific/resource/infrastructure outcomes remain immutable. Frozen science boundaries remain unchanged.

## Current scientific frontier — Exp073BU v0.1 Wm_S3 fresh-independent-PCL A/B

Wm_S1 Track-A exact PASS and admitted Wm_S2 authority are preserved. Exp073CR v0.3 remains RESOURCE PASS `+0/+0`. **Wm_S3 scientific angular authority remains absent.**

Exp073BU scientific preregistration: `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`. Intended A/B namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`. Required science PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

Scientific state: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**.

**DSIR-HOME-PC is FREE.** No home/self-hosted scientific process is active or authorized.

## Newly closed — Exp073BW v0.1 GSL selected-solver isolation = G2 negative support result

Frozen preregistration `experiments/073bw_support_gsl_selected_solver_equivalence_v0_1_prereg.md`, commit `c43cce294816e04e25e59c6e9410185d0962d621`, blob `e66c1e5d7a2f4593bfa8daf302663887790d44d2`. Python/C helper blobs `22c0cb391931e578f92c7ce75c4dba3429e09265` / `c247d449ecaec12ab05975181f0a05e4c3ac52fe`. Activation/head `0b5ad0f0addb22ce4691ae6c3349b323095a342e`.

Terminal run/job `33820436824` / `100861744518` completed SUCCESS. Raw artifact `9918084336`, digest `sha256:ec51bf2b0e66a9eaf1c2dcda4afbfd83b0bc6ba2d983a60366a5f1126967368a`, was downloaded and inspected. Runtime PyMaster and GSL were exactly 2.7; helper compilation and frozen execution succeeded.

Raw status: `G2_SELECTED_CONSTRUCTION_NOT_EXACT`. Replacing the selected-route `np.linalg.solve` by compiled GSL `gsl_linalg_LU_decomp` + `gsl_linalg_LU_solve` did **not** recover stock exact equality in any of the three frozen synthetic cases. Stock-vs-GSL max absolute differences: `1.4710455076283324e-15`, `1.3600232051658168e-15`, `1.4155343563970746e-15`; every SHA and `numpy.array_equal` comparison failed.

**Classification:** G2 negative support result `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING. The frozen hypothesis that solver choice alone explains historical Q2 is falsified. Together with Exp073BV R1, the exact discrepancy is localized deeper than Python wrapper/layout or solver choice: the selected/general-coupling reduction is not an exact substitute for the full stock spin-0 x spin-2 `ncls=2` C/GSL route. No tolerance rescue.

Immutable recovery: `recovery/2026-09-04_exp073bw_gsl_selected_solver_g2_not_exact.md`, commit `a53f2885910663a33a0a2dc625afc1ebfdf7c5b6`.

## Preserved Exp073BV R1 + NaMaster source S1

Exp073BV run/job `33820184200` / `100860976434`, artifact `9917999087`, digest `sha256:418fa4b29bcf1cce247615f1309c5a945386dea1899510ee86430c8c7f5fd771`: raw status `R1_EXACT_WRAPPER_RAW_LAYOUT_EQUIVALENCE`; all three complete `[2,8,2,48]` tensors exactly equal between public `get_bandpower_windows()` and direct stock SWIG buffer + stock reshape/transpose, max diff `0.0`. Classification R1 support PASS `+0/+0`, no science authority. Immutable recovery commit `eb1ef3f4f437952692ee483e2ab427b9d751d128`.

NaMaster-2.7 source audit run/job `33816987697` / `100851195938`, artifact `9916910028`, digest `sha256:edde986db34cd3311ff52936ba20db1bb2732e51f0061d9942da8b60fdc0047e`: status `S1_STOCK_OPERATION_ROUTE_IDENTIFIED`; upstream `LSSTDESC/NaMaster` tag v2.7 commit `24365fa59a38c15732f4f37e8b29265b75c442d5`; installed/pinned `pymaster/workspaces.py` SHA256 `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`. Classification S1 support PASS `+0/+0`; no science authority.

## Current process — Exp073BX v0.1 full-MCM stock-order exact-equivalence QA

After G2, a collision search found no pre-existing `073bx` authority. Exp073BX was prospectively frozen before numerical output and remains hosted synthetic `+0/+0` only.

- prereg `experiments/073bx_support_full_mcm_stock_order_equivalence_v0_1_prereg.md`, commit `adf5e1152673d8b8fd0247eb636b62cfa273af5c`, blob `a52c7cba9c8b7f5b248f88a0fc7b1c7e2e21d6b3`;
- C emulator `ci/exp073bx_full_mcm_stock_order_v0_1.c`, commit `bc0ea4f9f86083995a2cdd26579ab12252f2cd94`, blob `bdfc756e83baa27319090f6aab20272f4144177e`;
- Python driver `ci/exp073bx_full_mcm_stock_order_v0_1.py`, commit `513d6b950c54d1d67cd3ebe31923cdce17ad9d49`, blob `ae0282cbbcdd298f00765d8de68545fe214cec0e`;
- workflow commit `14a2635ebbc93cbf3e08b284730378cb813b01a4`;
- activation/head `7c26b00968b64d148639b393b05f446b02356665`;
- run `33820895190`;
- job `100863112761`;
- state at recovery write: **IN_PROGRESS**;
- home runner ownership: none; checkpoint namespace: none.

Frozen Exp073BX begins from the exact stock complete unbinned MCM exported by `NmtWorkspace.get_coupling_matrix()` and reproduces the pinned downstream stock C order with full `ncls=2`: complete binned MCM loops, GSL LU decomposition, complete `mat_coupled_bin`, GSL LU inverse, GSL BLAS `dgemm`, and raw stock output order before any TE selection. Three deterministic NSIDE=16/lmax=47 cases are compared as entire canonical `<f8 [2,8,2,48]` tensors.

Frozen outcomes:
- `F1_EXACT_FULL_STOCK_ORDER_EQUIVALENCE`: all full tensors exact SHA + `numpy.array_equal`; permits only later prospectively frozen **memory-scalable full-component MCM/window construction QA**, not science activation.
- `F2_FULL_STOCK_ORDER_MISMATCH`: valid lineage but any exact mismatch; negative support result, inspect source/weights/order with no tolerance rescue.
- `F3_SOURCE_LINEAGE_MISMATCH`: BLOCKED provenance mismatch.
- `F4_INFRASTRUCTURE_INCOMPLETE`: infrastructure failure; diagnose first causal defect and smallest prospective repair.

Workflow success alone is not F1/F2; terminal logs and raw artifact must be consumed before classification. Process ledger authority: `docs/CURRENT_PROCESS.md`, commit `5424353dd7386867847e36258c7c3d303fcddd4a`.

## Closed Exp073BU input/PCL prerequisites

Input staging PASS `+0/+0`: run/job `33815944381` / `100848002128`, artifact `9916526843`, digest `sha256:74307daaf5e7cece0ce2be2fa68edef8bc63c2e7f2439f20375ccac3dde97b69`.

Fresh-PCL static implementation PASS `+0/+0`: run/job `33816258925` / `100848963246`, helper SHA `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`, artifact `9916627301`.

Frozen source authority: Exp073R1 run/job/head `33270843577` / `99148916507` / `ef783ca941fb9b9b5f5eae537986c56ff06e6536`; S3 rows `4,196,641`; record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`; redMaGiC mask SHA `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

## Frozen Exp073BU scientific semantics

Each A/B replica independently stages/verifies frozen source bytes and constructs fresh NaMaster-2.7 masks/PCL and isolated durable state. A/B cannot read each other's outputs before both final receipts are durable. Historical Exp073CR/CQ/CM numerical PCL/window/band arrays/hashes/reference targets are forbidden.

DES `NSIDE=4096`, `NPIX=201326592`, RING/C, ell `0..12287`, 39 bands, spin-0 lens x spin-2 S3, full window tensor `[2,39,2,12288]` before selecting `wins[0,:,0,:] = TE<-TE`, canonical C-order `<f8 [39,12288]`, finite strictly positive band absolute-response norms. No effective ell/z/k, band-center replacement, fiducial-P shortcut, smoothing, averaging, rounding or tolerance rescue.

Scientific A/B PASS requires both exact canonical SHA256 equality and `numpy.array_equal` after provenance checks. Frozen outcomes remain `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`.

## Preserved resource/science governance

Exp073CR v0.3 RESOURCE PASS `+0/+0`: run/job `33771269117` / `100701857748`; checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`; fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`; CPU fraction `0.9623990689242612`; swap `0 KiB`; artifact `9903527609`. Resource authority only.

Historical selected compact Q2 run/job `33816670145` / `100850227684` remains exact-false `+0/+0`, max abs `1.4710455076283324e-15`, NON-AUTHORIZING. Authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd` preserves old Wm_S3 `BLOCK_PRODUCTION`; Exp073BU is a new prospective successor, not a rescue.

## Global frozen boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.
