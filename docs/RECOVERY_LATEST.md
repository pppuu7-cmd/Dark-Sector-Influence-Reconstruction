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

## Newly closed support gate — Exp073BV R1 exact wrapper/raw-layout equivalence

Exp073BU stock source audit first closed S1: run/job/head `33816987697` / `100851195938` / `d80042807faf26f29eeb2a11e026632bba0083b4`; status `S1_STOCK_OPERATION_ROUTE_IDENTIFIED`; artifact `9916910028`, digest `sha256:edde986db34cd3311ff52936ba20db1bb2732e51f0061d9942da8b60fdc0047e`; upstream `LSSTDESC/NaMaster` v2.7 commit `24365fa59a38c15732f4f37e8b29265b75c442d5`; immutable recovery `recovery/2026-09-04_exp073bu_namaster27_stock_window_source_audit_s1.md`, commit `28644526ea0950492f490b8dd6958a7e284c98b7`. Classification S1 support PASS `+0/+0`, no Wm_S3 authority.

On that authority, collision-free hosted support experiment Exp073BV v0.1 was prospectively frozen before output:
- prereg `experiments/073bv_support_stock_wrapper_raw_layout_equivalence_v0_1_prereg.md`, commit `4f05c390f3fc0f3bd3086acc7ba2c40fbaed514b`, blob `c54ee6422183bc8f1c5f9ba8c38d617a4104e2f0`;
- helper commit `f73c7a722fda54bf328741079a9beee771115983`, blob `73d8cb082712f887f35eb522137a0fd6dcc81fb0`;
- workflow commit `e21f6e995c9b24de851171bdf46a62048996fcd2`;
- activation/head `dd91b8dd9c7f8c0acc059b7f7133087701a3f2ad`.

Terminal run/job `33820184200` / `100860976434` completed SUCCESS. Raw artifact `9917999087`, digest `sha256:418fa4b29bcf1cce247615f1309c5a945386dea1899510ee86430c8c7f5fd771`, was inspected and gives exactly `R1_EXACT_WRAPPER_RAW_LAYOUT_EQUIVALENCE`.

Across all three prospectively frozen deterministic NSIDE=16/lmax=47 synthetic mask pairs, complete stock `[2,8,2,48]` `<f8` tensors from public `w.get_bandpower_windows()` exactly equal the direct `pymaster.nmtlib.get_bandpower_windows(w.wsp,size)` raw buffer followed only by stock reshape/transpose: `numpy.array_equal=true`, SHA equal and max absolute difference exactly `0.0` in every case. Case SHAs: `b442ac07b7cef6da102319330b181c13cbbe4b8bcfeb64822d523b76158a8d94`, `1e4c1b5faaf9100f8e8218e9ff83eead408db6fa9784df3cf8f1fd207a61069d`, `0fb60918684226fafae86c8d77b6f1d819cd8b37959ffcc0e11c26caa0160a0f`.

**Classification:** R1 support PASS `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING. The earlier selected compact Q2 discrepancy is therefore not caused by Python wrapper/layout semantics; under the frozen evidence it lies in replacing the stock C/GSL numerical route. Immutable recovery: `recovery/2026-09-04_exp073bv_wrapper_raw_layout_r1_exact.md`, commit `eb1ef3f4f437952692ee483e2ab427b9d751d128`.

## Current process — Exp073BW v0.1 GSL selected-solver isolation QA

R1 prospectively permits the next source-level isolation gate. Exp073BW was frozen before output and remains hosted synthetic support only.

- prereg `experiments/073bw_support_gsl_selected_solver_equivalence_v0_1_prereg.md`, commit `c43cce294816e04e25e59c6e9410185d0962d621`, blob `e66c1e5d7a2f4593bfa8daf302663887790d44d2`;
- Python helper commit `d58e57925f1dd1a9abab9b50ce4a50a798e720d0`, blob `22c0cb391931e578f92c7ce75c4dba3429e09265`;
- C/GSL helper commit `b87405206145228f0e0fbde6ae0447407fe8a308`, blob `c247d449ecaec12ab05975181f0a05e4c3ac52fe`;
- workflow implementation commit `f0dd8538b986ad6f7a9427fee9230a5ddc254ad3`;
- activation/head `0b5ad0f0addb22ce4691ae6c3349b323095a342e`;
- run `33820436824`;
- job `100861744518`;
- state at recovery write: **IN_PROGRESS**, exact NaMaster 2.7 + GSL environment installation;
- home runner ownership: none; checkpoint namespace: none.

The frozen question is whether the historical Q2 exact mismatch is explained solely by NumPy/OpenBLAS solve order. For each of the same three deterministic synthetic masks, Exp073BW holds the selected/general-coupling A/K construction fixed, replaces `np.linalg.solve` with compiled GSL 2.7 `gsl_linalg_LU_decomp` + `gsl_linalg_LU_solve` in frozen RHS order, and compares the resulting selected tensor against stock by exact canonical SHA and `numpy.array_equal` only.

Frozen outcomes:
- `G1_EXACT_SELECTED_GSL_EQUIVALENCE`: all three exact -> GSL LU is sufficient for the selected-route discrepancy under these frozen cases; still no science authority and full-component stock-C/GSL exact QA remains required.
- `G2_SELECTED_CONSTRUCTION_NOT_EXACT`: any exact mismatch -> solver substitution alone is insufficient; full-component stock operation-order implementation becomes mandatory. No tolerance rescue.
- `G3_SOURCE_LINEAGE_MISMATCH`: BLOCKED provenance mismatch.
- `G4_INFRASTRUCTURE_INCOMPLETE`: infrastructure failure; diagnose first causal defect and repair prospectively.

All outcomes are `+0/+0`. Workflow success alone is not G1/G2. Exact terminal action: inspect logs and raw artifact, classify, record immutable recovery, then dispatch only the frozen next branch.

Current process ledger: `docs/CURRENT_PROCESS.md`, commit `33fec51da425f10ee9b25f88c341d74f0b94b6c8`.

## Preserved selected-compact Q2 result

Run/job/head `33816670145` / `100850227684` / `a10ef5e664c4d1b20a668f080251ffdea98752a2`: `Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE`; stock selected SHA `dbc75e2d3977db6596a30c2fe204e2b68631ef6c9ce5b4cd1d8ba766b023a688`; compact SHA `5047b92334b72e163059271310acd2fbbafc349dbd76bbec65edc6dc9b492e2e`; `numpy.array_equal=false`; max abs `1.4710455076283324e-15`; artifact `9916798055`. Q2 remains `+0/+0`, NON-AUTHORIZING. Its historical `1e-12` support discriminator is not a scientific tolerance and cannot rescue exact equality.

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

Authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd` preserves old Wm_S3 history and `BLOCK_PRODUCTION`; Exp073BU is a new prospective successor, not a rescue. Exp073BT remains Q5 incomplete `+0/+0`.

## Global frozen boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.
