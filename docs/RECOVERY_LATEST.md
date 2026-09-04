# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-04  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`).

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoint branches outrank chat wording. Historical scientific/resource/infrastructure outcomes remain immutable. Frozen science boundaries remain unchanged.

## Current scientific frontier — Exp073BU v0.1 Wm_S3 fresh-independent-PCL A/B
Wm_S1 Track-A exact PASS and admitted Wm_S2 authority are preserved. Exp073CR v0.3 remains RESOURCE PASS `+0/+0`. **Wm_S3 scientific angular authority remains absent.**

Exp073BU prereg: `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`; namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`; required token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

Scientific state: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**. **DSIR-HOME-PC is FREE.**

## Newly closed — Exp073BX v0.1 F1 exact full-stock-order equivalence
Prereg commit `adf5e1152673d8b8fd0247eb636b62cfa273af5c`; activation/head `7c26b00968b64d148639b393b05f446b02356665`; run/job `33820895190` / `100863112761`; artifact `9918240620`; artifact ZIP SHA256 `02aa1b97e4281faca88be2d20ef836c137919529712a6de2be8c5bbf273cb214`.

The raw artifact was downloaded and inspected. Status: `F1_EXACT_FULL_STOCK_ORDER_EQUIVALENCE`. For all three frozen NSIDE=16/lmax=47 cases, the complete canonical `<f8 [2,8,2,48]` stock NaMaster-2.7 tensor and full-component emulator matched under SHA256 and `numpy.array_equal`, with `max_abs_difference=0.0`; selected TE also matched exactly. Runtime lineage PyMaster 2.7 + GSL 2.7 was valid; no DES/historical numerical data were read; no tolerance rescue was used.

**Classification:** support PASS `+0/+0`, NON-SCIENTIFIC, NON-AUTHORIZING. Immutable recovery: `recovery/2026-09-04_exp073bx_full_mcm_stock_order_f1_exact.md`, commit `e66509646c8b4922da6169a34b4a4928bb50f40b`.

Consequence: together with Exp073BV R1 and Exp073BW G2, the previous ~1e-15 discrepancy is localized to the selected/general-coupling reduction. The complete stock `ncls=2` route `full unbinned MCM -> source-order full binning -> GSL LU invert -> GSL BLAS dgemm -> stock raw order` can be reproduced bit-for-bit.

## Current process — Exp073BY v0.1 mmap full-MCM downstream QA
A collision search found no pre-existing `073by` authority. Exp073BY was prospectively frozen before numerical output and is hosted synthetic `+0/+0` only.

- prereg `experiments/073by_support_mmap_full_mcm_downstream_equivalence_v0_1_prereg.md`, commit `f51c738e4074b2a547f9ebc27388d7534eeb584b`, blob `b722f03a87905b8717441c8c31cf69f469d3ce8f`;
- C mmap emulator commit/blob `2235ecb2ad3d94b24bf632d637217499c49c204d` / `acafb095deafae7602101d8305e239341010ba79`;
- Python driver commit/blob `a49fbb4185af39da50414dcf906ef5970dba7cfe` / `a22d14ad9ae7e81ba6dd35c61b9ab35a05617d76`;
- workflow commit `d516d112415abf6075d35ca1428339e24772e9e6`;
- activation/head `5e243ee67f47b74a5a2c92f47fad079f5deeddd0`;
- run/job `33823950570` / `100872477739`;
- state at recovery write: **QUEUED**;
- home runner ownership: none; checkpoint namespace: none.

Frozen candidate reads the serialized complete MCM via read-only POSIX `mmap` and forbids a second full `nm*sizeof(double)` MCM heap/read copy. The downstream operation order remains exactly Exp073BX F1. This gate explicitly addresses only duplicate downstream MCM residency; it does not claim to solve construction/retention of NaMaster's own full MCM and cannot authorize science.

Frozen outcomes: `M1_EXACT_MMAP_FULL_COMPONENT_EQUIVALENCE`, `M2_MMAP_FULL_COMPONENT_MISMATCH`, `M3_MEMORY_CONTRACT_FAIL`, `M4_SOURCE_LINEAGE_MISMATCH`, `M5_INFRASTRUCTURE_INCOMPLETE`. Workflow success alone is not M1/M2; terminal logs/raw artifact must be consumed.

Process ledger: `docs/CURRENT_PROCESS.md`, commit `4a12eabcb1e317fe09ac256a520caa06c6d152e9`.

## Preserved Exp073BU prerequisites and authority
Input staging PASS `+0/+0`: `33815944381 / 100848002128`, artifact `9916526843`, digest `sha256:74307daaf5e7cece0ce2be2fa68edef8bc63c2e7f2439f20375ccac3dde97b69`.

Fresh-PCL static PASS `+0/+0`: `33816258925 / 100848963246`, helper SHA `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`, artifact `9916627301`.

Frozen source authority: Exp073R1 `33270843577 / 99148916507 / ef783ca941fb9b9b5f5eae537986c56ff06e6536`; S3 rows `4,196,641`; record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`; redMaGiC mask SHA `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

Each A/B replica must independently stage/verify frozen source bytes and construct fresh NaMaster-2.7 masks/PCL and isolated durable state. A/B cannot read each other's outputs before both receipts. Historical Exp073CR/CQ/CM numerical PCL/window/band arrays/hashes/reference targets are forbidden. Full tensor `[2,39,2,12288]` must exist before `wins[0,:,0,:]=TE<-TE`; final canonical output is C-order `<f8 [39,12288]`. Scientific PASS requires exact SHA256 plus `numpy.array_equal`, no tolerance rescue.

## Preserved support/resource history
- Exp073BW G2 `33820436824 / 100861744518`, artifact `9918084336`: selected/GSL construction not exact; max diffs ~1.36–1.47e-15; `+0/+0`.
- Exp073BV R1 `33820184200 / 100860976434`, artifact `9917999087`: public wrapper vs raw full tensor exact; `+0/+0`.
- NaMaster source audit S1 `33816987697 / 100851195938`, artifact `9916910028`, upstream v2.7 commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- selected compact Q2 `33816670145 / 100850227684`: exact false, max abs `1.4710455076283324e-15`, `+0/+0`.
- Exp073CR v0.3 RESOURCE PASS `+0/+0`: `33771269117 / 100701857748`, checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`, fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`, CPU fraction `0.9623990689242612`, swap 0, artifact `9903527609`.
- Old Wm_S3 route remains `BLOCK_PRODUCTION` under authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`; Exp073BU is a new prospective successor, not a rescue.

## Global frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.
