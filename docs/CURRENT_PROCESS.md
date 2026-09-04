# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. Historical outcomes are not rewritten.

## Current owner/process
- **DSIR-HOME-PC: FREE.** No self-hosted heavy/scientific process is active or authorized.
- Exp073BU numerical Wm_S3 science: **NOT ACTIVATED**.
- Current process: hosted-only Exp073BY v0.1 mmap full-MCM downstream exact-equivalence QA.
- Workflow run `33823950570`; job `100872477739` (`hosted-static-and-mmap-qa`).
- Branch/head `main` / `5e243ee67f47b74a5a2c92f47fad079f5deeddd0`.
- Creation/start `2026-09-04T00:58:53Z`.
- State at ledger write: `QUEUED`.
- Checkpoint namespace: none; hosted deterministic synthetic support QA only.
- Prereg `experiments/073by_support_mmap_full_mcm_downstream_equivalence_v0_1_prereg.md`, commit `f51c738e4074b2a547f9ebc27388d7534eeb584b`, blob `b722f03a87905b8717441c8c31cf69f469d3ce8f`.
- C helper commit/blob `2235ecb2ad3d94b24bf632d637217499c49c204d` / `acafb095deafae7602101d8305e239341010ba79`.
- Python helper commit/blob `a49fbb4185af39da50414dcf906ef5970dba7cfe` / `a22d14ad9ae7e81ba6dd35c61b9ab35a05617d76`.
- Workflow commit `d516d112415abf6075d35ca1428339e24772e9e6`; activation/head `5e243ee67f47b74a5a2c92f47fad079f5deeddd0`.
- Frozen outcomes: `M1_EXACT_MMAP_FULL_COMPONENT_EQUIVALENCE`, `M2_MMAP_FULL_COMPONENT_MISMATCH`, `M3_MEMORY_CONTRACT_FAIL`, `M4_SOURCE_LINEAGE_MISMATCH`, `M5_INFRASTRUCTURE_INCOMPLETE`.
- Accounting always `+0/+0`; Wm_S3 authority forbidden.
- Exact terminal action: inspect logs and raw artifact. M1 permits only later prospective work on persisting/obtaining a DES-scale full stock MCM without an additional resident duplicate; M2 is a negative exact support result; M3 resource/implementation fail; M4/M5 provenance/infrastructure diagnosis and smallest prospective repair. Workflow SUCCESS alone is not M1/M2.

## Newly closed — Exp073BX F1 exact full-stock route
Run/job/head `33820895190` / `100863112761` / `7c26b00968b64d148639b393b05f446b02356665`; artifact `9918240620`, digest `sha256:02aa1b97e4281faca88be2d20ef836c137919529712a6de2be8c5bbf273cb214`.

Raw artifact status `F1_EXACT_FULL_STOCK_ORDER_EQUIVALENCE`. All three complete canonical `<f8 [2,8,2,48]` tensors matched stock NaMaster 2.7 under both SHA256 and `numpy.array_equal`; max abs difference exactly `0.0` in every case, and selected TE slices were exact. Runtime lineage PyMaster 2.7 + GSL 2.7 valid. Classification: support PASS `+0/+0`, NON-SCIENTIFIC/NON-AUTHORIZING. Immutable recovery `recovery/2026-09-04_exp073bx_full_mcm_stock_order_f1_exact.md`, commit `e66509646c8b4922da6169a34b4a4928bb50f40b`.

Together with Exp073BV R1 and Exp073BW G2, F1 proves the earlier ~1e-15 discrepancy belongs to the selected/general-coupling reduction; the complete stock `ncls=2` C/GSL operation order itself can be reproduced bit-for-bit.

## Prospective scientific gate — Exp073BU v0.1
Prereg `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`; intended namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`; required science token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

State: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**. Scientific PASS remains exact canonical SHA256 plus `numpy.array_equal` on complete canonical `<f8 [39,12288]` after valid isolated provenance. No tolerance rescue.

## Preserved authority/history
- Exp073BW G2 `33820436824 / 100861744518`, artifact `9918084336`: selected construction not exact, `+0/+0`.
- Exp073BV R1 `33820184200 / 100860976434`, artifact `9917999087`: wrapper/raw full tensor exact, `+0/+0`.
- NaMaster source audit S1 `33816987697 / 100851195938`, artifact `9916910028`, upstream commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- Selected compact Q2 `33816670145 / 100850227684`: exact false, max abs `1.4710455076283324e-15`, `+0/+0`.
- Exp073BU input staging PASS `+0/+0`: `33815944381 / 100848002128`.
- Exp073BU fresh-PCL static PASS `+0/+0`: `33816258925 / 100848963246`.
- Exp073CR v0.3 RESOURCE PASS `+0/+0`: `33771269117 / 100701857748`, checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`, fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`, CPU fraction `0.9623990689242612`, swap 0.
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority preserved.
- Old Wm_S3 route remains blocked by authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`.
- **Wm_S3 scientific authority remains absent.**

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
