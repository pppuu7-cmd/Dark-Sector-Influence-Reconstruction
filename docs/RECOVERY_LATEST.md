# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-04  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`).

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoint branches outrank chat wording. Historical scientific/resource/infrastructure outcomes remain immutable. Frozen science boundaries remain unchanged.

## Current frontier — Exp073BU v0.1 Wm_S3 fresh-independent-PCL A/B

Wm_S1 Track-A exact PASS and admitted Wm_S2 authority are preserved. Exp073CR v0.3 remains RESOURCE PASS `+0/+0`. **Wm_S3 scientific angular authority remains absent.**

Exp073BU scientific preregistration: `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`. Intended A/B namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`. Required science PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

Current scientific state: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**.

**DSIR-HOME-PC is FREE.** No home/self-hosted scientific process is authorized. Current activity is hosted support-only Exp073BV v0.1; it cannot create Wm_S3 authority.

## Newly closed — Exp073BU NaMaster 2.7 stock-window source audit S1

Frozen source-audit preregistration: `experiments/073bu_support_namaster27_stock_window_source_audit_v0_1_prereg.md`, commit `798eabda7fa7ba2cbe28262fdb37fb4970327431`.

Terminal run/job/head `33816987697` / `100851195938` / `d80042807faf26f29eeb2a11e026632bba0083b4` completed SUCCESS. Workflow success was not treated as authority by itself; the raw receipt/artifact was inspected.

Validated receipt:
- status `S1_STOCK_OPERATION_ROUTE_IDENTIFIED`;
- raw token `PASS_EXP073BU_NAMASTER27_STOCK_WINDOW_SOURCE_AUDIT_EXECUTED_V0_1`;
- artifact `9916910028`;
- digest `sha256:edde986db34cd3311ff52936ba20db1bb2732e51f0061d9942da8b60fdc0047e`;
- runtime PyMaster `2.7`;
- upstream authority `LSSTDESC/NaMaster` tag `v2.7`, exact commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- installed/pinned `pymaster/workspaces.py` SHA256 `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`.

The exact stock route is sufficiently identified: public `NmtWorkspace.get_bandpower_windows()` calls SWIG `lib.get_bandpower_windows`, reshapes the returned stock buffer and transposes to `[ncls,n_bands,ncls,lmax+1]`. Pinned `src/nmt_master.c` identifies binned/unbinned coupling-matrix operation order, GSL LU decomposition and `nmt_compute_bandpower_windows` source-order accumulation. This closes the frozen S1 support gate.

**Classification:** S1 source-audit PASS, `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING. It does not rescue or rewrite the prior selected-compact Q2 result.

Immutable recovery: `recovery/2026-09-04_exp073bu_namaster27_stock_window_source_audit_s1.md`, commit `28644526ea0950492f490b8dd6958a7e284c98b7`.

## Current process — Exp073BV v0.1 wrapper/raw-layout exact-equivalence isolation QA

A collision search found no existing `073bv` experiment authority before preregistration. The next support gate was frozen prospectively before numerical output.

- helper: `ci/exp073bv_stock_wrapper_raw_layout_equivalence_v0_1.py`, introduction commit `f73c7a722fda54bf328741079a9beee771115983`, frozen Git blob `73d8cb082712f887f35eb522137a0fd6dcc81fb0`;
- preregistration: `experiments/073bv_support_stock_wrapper_raw_layout_equivalence_v0_1_prereg.md`, commit `4f05c390f3fc0f3bd3086acc7ba2c40fbaed514b`, blob `c54ee6422183bc8f1c5f9ba8c38d617a4104e2f0`;
- workflow implementation commit `e21f6e995c9b24de851171bdf46a62048996fcd2`;
- explicit activation/head commit `dd91b8dd9c7f8c0acc059b7f7133087701a3f2ad`;
- run `33820184200`;
- job `100860976434`;
- state at recovery write: `QUEUED`;
- runner: hosted Ubuntu only; no checkpoint namespace and no home ownership.

Frozen QA uses exactly three deterministic synthetic NSIDE=16, `lmax=47` weighted mask pairs and no DES/DSIR physical data. For each case it compares the complete public stock `w.get_bandpower_windows()` tensor against a direct call to the same frozen `pymaster.nmtlib.get_bandpower_windows(w.wsp,size)` raw buffer followed only by the exact stock wrapper reshape/transpose. Both sides are canonical C-order `<f8`; no closeness tolerance exists.

Frozen classifications:
- `R1_EXACT_WRAPPER_RAW_LAYOUT_EQUIVALENCE`: exact SHA256 and `numpy.array_equal` for all three cases. This isolates the prior Q2 discrepancy away from Python wrapper/layout and permits a later prospectively frozen stock-C/GSL emulator/equivalence QA; no science authority.
- `R2_WRAPPER_RAW_LAYOUT_MISMATCH`: valid provenance but any exact mismatch; negative support result, no tolerance rescue.
- `R3_SOURCE_LINEAGE_MISMATCH`: fail-closed provenance mismatch/BLOCKED.
- `R4_INFRASTRUCTURE_INCOMPLETE`: infrastructure failure before a valid receipt; diagnose first causal failure.

All Exp073BV outcomes are `+0/+0`. Workflow success alone is not R1. Exact terminal action is to inspect logs and the complete JSON artifact before classification, then continue according to the frozen branch.

Process ledger authority: `docs/CURRENT_PROCESS.md`, update commit `13833223672e27c0a7210536056c744f57d87cc8`.

## Preserved selected-compact Q2 negative support result

Repaired run/job/head `33816670145` / `100850227684` / `a10ef5e664c4d1b20a668f080251ffdea98752a2` produced `Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE`: stock selected SHA `dbc75e2d3977db6596a30c2fe204e2b68631ef6c9ce5b4cd1d8ba766b023a688`, compact SHA `5047b92334b72e163059271310acd2fbbafc349dbd76bbec65edc6dc9b492e2e`, `numpy.array_equal=false`, max abs difference `1.4710455076283324e-15`, artifact `9916798055`, digest `sha256:2244e5ce5df5f48db40c51fca3dba1321fef1125424c7baea74edbaa4008f520`.

Classification remains Q2 numeric-only `+0/+0`, NON-AUTHORIZING. The support-QA `1e-12` discriminator cannot be used as a scientific tolerance. The Exp073CR-style selected compact/general-coupling finalizer cannot silently substitute for Exp073BU stock semantics.

## Closed Exp073BU input/PCL prerequisites

Input staging PASS `+0/+0`: run/job/head `33815944381` / `100848002128` / `00b8a2c25ec4e50ae1027a1a2141a0023a033ab9`; token `PASS_EXP073BU_FROZEN_INPUT_STAGING_CLOSURE_V0_1`; artifact `9916526843`, digest `sha256:74307daaf5e7cece0ce2be2fa68edef8bc63c2e7f2439f20375ccac3dde97b69`.

Fresh-PCL static implementation PASS `+0/+0`: helper `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py`, commit `e6ffda3b5c558c964cf486d78a792d40bf9c76e5`; run/job/head `33816258925` / `100848963246` / `04b0b29cbed039de6520eb6a738f78bdc9785885`; helper SHA `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`; artifact `9916627301`, digest `sha256:35e4ace8514a3614bc697ceb398268789a9db7e81d049b1910ca7a428dccd65d`.

Frozen source authority: Exp073R1 run/job/head `33270843577` / `99148916507` / `ef783ca941fb9b9b5f5eae537986c56ff06e6536`; artifact `9720335366`; S3 selected rows `4,196,641`; record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique occupied pixels `2,943,132`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`; redMaGiC mask SHA `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

## Frozen Exp073BU scientific semantics

Each A/B replica independently stages/verifies frozen source bytes and constructs fresh NaMaster-2.7 masks/PCL and isolated durable state. A/B cannot read each other's output before both final receipts are durable. Historical Exp073CR/CQ/CM numerical PCL/window/band arrays/hashes/reference targets are forbidden.

Angular semantics: DES `NSIDE=4096`, `NPIX=201326592`, RING/C, ell `0..12287`, 39 bands, spin-0 lens x spin-2 S3, **full bandpower-window tensor `[2,39,2,12288]` before selecting `wins[0,:,0,:]` = `TE<-TE`**, canonical C-order `<f8 [39,12288]`, finite strictly positive band absolute-response norms. No effective ell/z/k, band-center replacement, fiducial-P shortcut, smoothing, averaging, rounding or tolerance rescue.

Scientific A/B PASS requires both exact canonical SHA256 equality and `numpy.array_equal` after provenance checks. Frozen outcomes remain `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`.

## Preserved Exp073CR resource authority and historical governance

Exp073CR v0.3 RESOURCE PASS `+0/+0`: run/job/head `33771269117` / `100701857748` / `023fcfa28f0eb904656c76e55c55d821e50c8155`; checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`; fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`; token `PASS_EXP073CR_V0_3_WM_S3_LL3_SHARDED_8CORE_RESOURCE`; CPU fraction `0.9623990689242612`; swap `0 KiB`; artifact `9903527609`, digest `sha256:28f6141e641726351b6dd804c07db28b6c4152de5a71a0c0b098b539a6bc0256`. Resource authority only.

Authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd` preserves old Wm_S3 history: Exp073X2 P=`INFRASTRUCTURE_INCOMPLETE`, Q=`SCIENTIFIC_REPEATABILITY_FAIL`; Exp073AF => `BLOCK_PRODUCTION`; old Exp073AA route never established Wm_S3 authority. Exp073BU is a new prospective successor, not a rescue. Exp073BT v0.3 remains Q5 incomplete `+0/+0`.

## Global boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.
