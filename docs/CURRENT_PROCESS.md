# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. Historical outcomes are not rewritten.

## Current owner/process
- **DSIR-HOME-PC: FREE.** No self-hosted heavy/scientific process is active or authorized.
- Exp073BU numerical Wm_S3 science: **NOT ACTIVATED**.
- Current process: hosted-only Exp073BV v0.1 stock wrapper/raw-layout exact-equivalence QA.
- Workflow run: `33820184200`.
- Job: `100860976434` (`hosted-static-and-synthetic-qa`).
- Branch/head SHA: `main` / `dd91b8dd9c7f8c0acc059b7f7133087701a3f2ad`.
- Start/creation: `2026-09-04T00:03:20Z`.
- Current state at ledger write: `QUEUED`.
- Checkpoint namespace: none; hosted synthetic support QA only.
- Frozen preregistration: `experiments/073bv_support_stock_wrapper_raw_layout_equivalence_v0_1_prereg.md`, prereg commit `4f05c390f3fc0f3bd3086acc7ba2c40fbaed514b`, prereg blob `c54ee6422183bc8f1c5f9ba8c38d617a4104e2f0`.
- Frozen helper: `ci/exp073bv_stock_wrapper_raw_layout_equivalence_v0_1.py`, helper commit `f73c7a722fda54bf328741079a9beee771115983`, helper blob `73d8cb082712f887f35eb522137a0fd6dcc81fb0`.
- Workflow implementation commit: `e21f6e995c9b24de851171bdf46a62048996fcd2`.
- Activation/head commit: `dd91b8dd9c7f8c0acc059b7f7133087701a3f2ad`.
- Expected classifications: `R1_EXACT_WRAPPER_RAW_LAYOUT_EQUIVALENCE`, `R2_WRAPPER_RAW_LAYOUT_MISMATCH`, `R3_SOURCE_LINEAGE_MISMATCH`, or `R4_INFRASTRUCTURE_INCOMPLETE`.
- Accounting: always `+0/+0`; Wm_S3 authority forbidden.
- Exact terminal action: inspect job logs and raw JSON artifact. R1 permits only prospective stock-C/GSL operation-order emulator/equivalence QA; R2 requires wrapper/layout diagnosis; R3/R4 require provenance/infrastructure diagnosis and smallest prospective repair. Workflow SUCCESS alone is not R1.

## Newly closed support authority — Exp073BU NaMaster 2.7 source audit S1

Run/job/head `33816987697` / `100851195938` / `d80042807faf26f29eeb2a11e026632bba0083b4` completed SUCCESS and the raw receipt was consumed.

- status: `S1_STOCK_OPERATION_ROUTE_IDENTIFIED`;
- token: `PASS_EXP073BU_NAMASTER27_STOCK_WINDOW_SOURCE_AUDIT_EXECUTED_V0_1`;
- artifact: `9916910028`;
- artifact digest: `sha256:edde986db34cd3311ff52936ba20db1bb2732e51f0061d9942da8b60fdc0047e`;
- upstream authority: `LSSTDESC/NaMaster` tag `v2.7`, commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- installed/pinned `pymaster/workspaces.py` SHA256: `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`;
- classification: support source-audit PASS S1, `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING.

Immutable recovery: `recovery/2026-09-04_exp073bu_namaster27_stock_window_source_audit_s1.md`, commit `28644526ea0950492f490b8dd6958a7e284c98b7`.

S1 identifies the stock route `NmtWorkspace.get_bandpower_windows()` -> SWIG `lib.get_bandpower_windows` -> pinned C implementation using the binned/unbinned coupling matrices, stock GSL LU route and source-order bandpower-window accumulation. It does not rescue the previously observed Q2 selected-compact mismatch.

## Prospective scientific gate — Exp073BU v0.1
- preregistration `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`;
- intended namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`;
- required science token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`;
- state: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**.

Scientific A/B PASS remains exact canonical SHA256 equality plus `numpy.array_equal` on complete canonical `<f8 [39,12288]` after valid isolated provenance. No tolerance rescue.

## Preserved support/resource/science history
- Selected compact support run/job `33816670145` / `100850227684`: `Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE`, exact equality false, max abs difference `1.4710455076283324e-15`, `+0/+0`, NON-AUTHORIZING. Historical first attempt `33816536157` was Q4 infrastructure incomplete before numerical execution; repair changed only freeze binding.
- Exp073BU frozen input staging PASS `+0/+0`: run/job `33815944381` / `100848002128`, artifact `9916526843`.
- Exp073BU fresh-PCL static implementation PASS `+0/+0`: run/job `33816258925` / `100848963246`, helper SHA `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`.
- Exp073CR v0.3 RESOURCE PASS `+0/+0`: run/job `33771269117` / `100701857748`, checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`, fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`, CPU fraction `0.9623990689242612`, swap `0 KiB`.
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority remain preserved.
- Old Wm_S3 route remains blocked by authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`.
- Exp073BT v0.3 remains Q5 incomplete `+0/+0`.
- **Wm_S3 scientific authority remains absent.**

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
