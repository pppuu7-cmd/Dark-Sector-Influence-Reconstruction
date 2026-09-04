# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. Historical outcomes are not rewritten.

## Current owner/process
- **DSIR-HOME-PC: FREE.** No self-hosted heavy/scientific process is active or authorized.
- Exp073BU numerical Wm_S3 science: **NOT ACTIVATED**.
- Current process: hosted-only Exp073BX v0.1 full-MCM stock-order exact-equivalence QA.
- Workflow run `33820895190`; job `100863112761` (`hosted-static-and-full-mcm-qa`).
- Branch/head `main` / `7c26b00968b64d148639b393b05f446b02356665`.
- Creation/start `2026-09-04T00:13:16Z`.
- State at ledger write: `IN_PROGRESS`.
- Checkpoint namespace: none; hosted deterministic synthetic support QA only.
- Prereg `experiments/073bx_support_full_mcm_stock_order_equivalence_v0_1_prereg.md`, commit `adf5e1152673d8b8fd0247eb636b62cfa273af5c`, blob `a52c7cba9c8b7f5b248f88a0fc7b1c7e2e21d6b3`.
- C helper commit/blob `bc0ea4f9f86083995a2cdd26579ab12252f2cd94` / `bdfc756e83baa27319090f6aab20272f4144177e`.
- Python helper commit/blob `513d6b950c54d1d67cd3ebe31923cdce17ad9d49` / `ae0282cbbcdd298f00765d8de68545fe214cec0e`.
- Workflow commit `14a2635ebbc93cbf3e08b284730378cb813b01a4`; activation/head `7c26b00968b64d148639b393b05f446b02356665`.
- Frozen outcomes: `F1_EXACT_FULL_STOCK_ORDER_EQUIVALENCE`, `F2_FULL_STOCK_ORDER_MISMATCH`, `F3_SOURCE_LINEAGE_MISMATCH`, `F4_INFRASTRUCTURE_INCOMPLETE`.
- Accounting always `+0/+0`; Wm_S3 authority forbidden.
- Exact terminal action: inspect job logs and raw artifact. F1 permits only later prospectively frozen memory-scalable full-component MCM/window QA; F2 requires exact source/order diagnosis; F3/F4 require provenance/infrastructure diagnosis and smallest prospective repair. Workflow SUCCESS alone is not F1/F2.

## Newly closed — Exp073BW G2 selected construction not exact
Run/job/head `33820436824` / `100861744518` / `0b5ad0f0addb22ce4691ae6c3349b323095a342e`; artifact `9918084336`, digest `sha256:ec51bf2b0e66a9eaf1c2dcda4afbfd83b0bc6ba2d983a60366a5f1126967368a`.

Raw artifact status `G2_SELECTED_CONSTRUCTION_NOT_EXACT`; PyMaster 2.7 and GSL 2.7 lineage valid. Replacing NumPy solve by compiled `gsl_linalg_LU_decomp` + `gsl_linalg_LU_solve` did not recover stock exact equality in any of the three frozen cases. Stock-vs-GSL max abs differences were `1.4710455076283324e-15`, `1.3600232051658168e-15`, `1.4155343563970746e-15`; all SHA and `numpy.array_equal` comparisons failed. Classification: negative support result `+0/+0`, NON-SCIENTIFIC/NON-AUTHORIZING. Immutable recovery `recovery/2026-09-04_exp073bw_gsl_selected_solver_g2_not_exact.md`, commit `a53f2885910663a33a0a2dc625afc1ebfdf7c5b6`.

Together with Exp073BV R1, G2 localizes the exact discrepancy deeper than Python layout or solver choice: selected/general-coupling reduction is not an exact substitute for the full stock `ncls=2` C/GSL operation route.

## Preserved Exp073BV / source-audit results
- Exp073BV R1 run/job `33820184200` / `100860976434`, artifact `9917999087`, digest `sha256:418fa4b29bcf1cce247615f1309c5a945386dea1899510ee86430c8c7f5fd771`: all three full `[2,8,2,48]` tensors exact between public wrapper and direct SWIG raw buffer; `+0/+0`, no science authority. Immutable commit `eb1ef3f4f437952692ee483e2ab427b9d751d128`.
- NaMaster 2.7 source audit S1 run/job `33816987697` / `100851195938`, artifact `9916910028`, digest `sha256:edde986db34cd3311ff52936ba20db1bb2732e51f0061d9942da8b60fdc0047e`; upstream commit `24365fa59a38c15732f4f37e8b29265b75c442d5`; `+0/+0`, no science authority.

## Prospective scientific gate — Exp073BU v0.1
Prereg `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`; intended namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`; required science token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

State: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**. Scientific PASS remains exact canonical SHA256 plus `numpy.array_equal` on complete canonical `<f8 [39,12288]` after valid isolated provenance. No tolerance rescue.

## Preserved authority/history
- Selected compact Q2 run/job `33816670145` / `100850227684`: exact false, max abs `1.4710455076283324e-15`, `+0/+0`.
- Exp073BU input staging PASS `+0/+0`: `33815944381` / `100848002128`.
- Exp073BU fresh-PCL static PASS `+0/+0`: `33816258925` / `100848963246`.
- Exp073CR v0.3 RESOURCE PASS `+0/+0`: `33771269117` / `100701857748`, checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`, fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`, CPU fraction `0.9623990689242612`, swap 0.
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority preserved.
- Old Wm_S3 route remains blocked by authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`.
- **Wm_S3 scientific authority remains absent.**

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
