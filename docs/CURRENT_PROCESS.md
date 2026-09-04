# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. Historical outcomes are not rewritten.

## Current owner/process
- **DSIR-HOME-PC: FREE.** No self-hosted heavy/scientific process is active or authorized.
- Exp073BU numerical Wm_S3 science: **NOT ACTIVATED**.
- Current process: hosted-only Exp073BW v0.1 GSL selected-solver exact-equivalence isolation QA.
- Workflow run: `33820436824`.
- Job: `100861744518` (`hosted-static-and-gsl-qa`).
- Branch/head SHA: `main` / `0b5ad0f0addb22ce4691ae6c3349b323095a342e`.
- Start/creation: `2026-09-04T00:06:54Z`.
- State at ledger write: `QUEUED`.
- Checkpoint namespace: none; hosted deterministic synthetic support QA only.
- Frozen preregistration: `experiments/073bw_support_gsl_selected_solver_equivalence_v0_1_prereg.md`, commit `c43cce294816e04e25e59c6e9410185d0962d621`, blob `e66c1e5d7a2f4593bfa8daf302663887790d44d2`.
- Frozen Python helper: commit `d58e57925f1dd1a9abab9b50ce4a50a798e720d0`, blob `22c0cb391931e578f92c7ce75c4dba3429e09265`.
- Frozen C/GSL helper: commit `b87405206145228f0e0fbde6ae0447407fe8a308`, blob `c247d449ecaec12ab05975181f0a05e4c3ac52fe`.
- Workflow implementation commit: `f0dd8538b986ad6f7a9427fee9230a5ddc254ad3`.
- Activation/head commit: `0b5ad0f0addb22ce4691ae6c3349b323095a342e`.
- Frozen outcomes: `G1_EXACT_SELECTED_GSL_EQUIVALENCE`, `G2_SELECTED_CONSTRUCTION_NOT_EXACT`, `G3_SOURCE_LINEAGE_MISMATCH`, `G4_INFRASTRUCTURE_INCOMPLETE`.
- Accounting: always `+0/+0`; Wm_S3 authority forbidden.
- Exact terminal action: inspect raw receipt/artifact. G1 means stock GSL LU is sufficient to remove the selected compact Q2 discrepancy under all frozen cases, but still requires a later full-component stock-C/GSL exact QA. G2 means solver substitution alone is insufficient and full-component stock operation order is mandatory. G3/G4 require provenance/infrastructure diagnosis and prospective smallest repair.

## Newly closed — Exp073BV R1 exact wrapper/raw-layout equivalence
Run/job/head `33820184200` / `100860976434` / `dd91b8dd9c7f8c0acc059b7f7133087701a3f2ad`; artifact `9917999087`, digest `sha256:418fa4b29bcf1cce247615f1309c5a945386dea1899510ee86430c8c7f5fd771`.

Raw receipt status `R1_EXACT_WRAPPER_RAW_LAYOUT_EQUIVALENCE`. All three frozen deterministic synthetic cases produced exact full `[2,8,2,48]` `<f8` equality between public `w.get_bandpower_windows()` and direct stock SWIG raw buffer followed only by stock reshape/transpose. For every case: SHA equal, `numpy.array_equal=true`, max absolute difference exactly `0.0`.

Case SHAs: `b442ac07b7cef6da102319330b181c13cbbe4b8bcfeb64822d523b76158a8d94`, `1e4c1b5faaf9100f8e8218e9ff83eead408db6fa9784df3cf8f1fd207a61069d`, `0fb60918684226fafae86c8d77b6f1d819cd8b37959ffcc0e11c26caa0160a0f`.

Classification: R1 support PASS `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING. It isolates the prior Q2 discrepancy away from Python wrapper/layout and into the replacement of the stock C/GSL computation path. Immutable recovery: `recovery/2026-09-04_exp073bv_wrapper_raw_layout_r1_exact.md`, commit `eb1ef3f4f437952692ee483e2ab427b9d751d128`.

## Previously closed — Exp073BU NaMaster 2.7 source audit S1
Run/job/head `33816987697` / `100851195938` / `d80042807faf26f29eeb2a11e026632bba0083b4`; status `S1_STOCK_OPERATION_ROUTE_IDENTIFIED`; artifact `9916910028`, digest `sha256:edde986db34cd3311ff52936ba20db1bb2732e51f0061d9942da8b60fdc0047e`; upstream NaMaster v2.7 commit `24365fa59a38c15732f4f37e8b29265b75c442d5`; `+0/+0`, no science authority. Immutable recovery commit `28644526ea0950492f490b8dd6958a7e284c98b7`.

## Prospective scientific gate — Exp073BU v0.1
Preregistration `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`; intended namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`; required science token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

State: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**. Scientific PASS remains exact canonical SHA256 plus `numpy.array_equal` on complete canonical `<f8 [39,12288]` after valid isolated provenance. No tolerance rescue.

## Preserved authority/history
- Selected compact support run/job `33816670145` / `100850227684`: Q2 numeric-only, max abs `1.4710455076283324e-15`, exact equality false, `+0/+0`, NON-AUTHORIZING.
- Exp073BU input staging PASS `+0/+0`: run/job `33815944381` / `100848002128`.
- Exp073BU fresh-PCL static PASS `+0/+0`: run/job `33816258925` / `100848963246`, helper SHA `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`.
- Exp073CR v0.3 RESOURCE PASS `+0/+0`: run/job `33771269117` / `100701857748`, checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`, fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`, CPU fraction `0.9623990689242612`, swap 0.
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority preserved.
- Old Wm_S3 route remains blocked by authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`.
- **Wm_S3 scientific authority remains absent.**

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
