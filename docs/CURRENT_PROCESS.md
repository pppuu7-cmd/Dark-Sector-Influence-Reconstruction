# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoint branches are authoritative.

## Active process / ownership
- No self-hosted heavy process is authorized.
- DSIR-HOME-PC ownership: **FREE**.
- Exp073BU numerical Wm_S3 science is **NOT ACTIVATED**.
- Hosted support-only run `33816670145`, job `100850227684`, head `a10ef5e664c4d1b20a668f080251ffdea98752a2` is the only current process tracked by this ledger. It tests synthetic selected-TE semantic equivalence only and cannot create Wm_S3 authority.
- Expected support outcomes are frozen in `experiments/073bu_support_selected_te_semantic_equivalence_v0_1_prereg.md`: Q1 exact / Q2 numeric-only / Q3 mismatch / Q4 infrastructure incomplete, all `+0/+0`.
- Exact next action on terminal: consume raw receipt/artifact and classify Q1/Q2/Q3/Q4. Q2 cannot authorize a scientific runtime substitution; Q3 rejects that route; Q4 requires smallest infrastructure repair; Q1 still requires a separate prospective BU implementation-binding audit before any scientific activation.

## Prospective scientific gate — Exp073BU v0.1
- purpose: fresh-independent-PCL exact A/B successor for missing Wm_S3 angular authority;
- preregistration: `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`;
- prereg commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`;
- scientific PASS token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`;
- namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`;
- state: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / WINDOW-SEMANTIC IMPLEMENTATION BINDING OPEN / NOT ACTIVATED**.

## Closed input-staging gate
Workflow/head `exp073bu-input-staging-closure-v0-1.yml` / `00b8a2c25ec4e50ae1027a1a2141a0023a033ab9`; run/job `33815944381` / `100848002128`; raw token `PASS_EXP073BU_FROZEN_INPUT_STAGING_CLOSURE_V0_1`; artifact `9916526843`, digest `sha256:74307daaf5e7cece0ce2be2fa68edef8bc63c2e7f2439f20375ccac3dde97b69`; immutable note commit `60e5fcefbba9ab5701be207e88e6806426d6675e`. Classification: input/provenance PASS `+0/+0`, no scientific authority.

Bound inputs verified there:
- Exp073R1 run/job/head `33270843577` / `99148916507` / `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- S3 rows `4,196,641`, record bytes/SHA `16,786,564` / `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`, unique pixels `2,943,132`, occupancy bytes/SHA `25,165,824` / `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`;
- first-party redMaGiC mask bytes/SHA `104,595,840` / `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

## Closed fresh-PCL static implementation gate
Standalone helper `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py`, implementation commit `e6ffda3b5c558c964cf486d78a792d40bf9c76e5`.
Hosted audit run/job/head `33816258925` / `100848963246` / `04b0b29cbed039de6520eb6a738f78bdc9785885`; raw token `PASS_EXP073BU_FRESH_PCL_HOSTED_STATIC_AUDIT_V0_1`; helper SHA256 `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`; prereg SHA256 `4a7be4440e51197ef7811832b7ae00690750a57b4af3f4f9f0b3530ffe902622`; artifact `9916627301`, digest `sha256:35e4ace8514a3614bc697ceb398268789a9db7e81d049b1910ca7a428dccd65d`; immutable note commit `3621235e56347fc9a65bbfaf41ba7aaf356a3ae3`.
Classification: static implementation PASS `+0/+0`; no numerical PCL and no Wm_S3 authority.

The helper independently reconstructs exact S3/lens masks, binds PyMaster 2.7, constructs spin-0 x spin-2 mask ALMs and fresh `healpy.alm2cl`, persists canonical `<f8 [12288]` complete-stage PCL, and explicitly forbids historical numerical window/PCL references or other-replica reads.

## Current selected-TE support QA and repair history
Preregistration commit `b31733b1047a39942118b409d63e4faa8d8c4b7a`; helper commit `bed56467b0d9f145ca9e1c5e896d92e02d5141fa`.
Historical first attempt run/job/head `33816536157` / `100849813933` / `9be393e6fb015ddfb4a262222866c879ede0c7f1`: **Q4 infrastructure incomplete `+0/+0` before any numerical execution**. First causal failure was shallow-checkout binding: `git rev-parse <older-commit>:path` could not resolve the prereg path because checkout depth was 1. NaMaster install and numerical test were skipped.
Smallest prospective repair commit `a10ef5e664c4d1b20a668f080251ffdea98752a2`: only freeze verification changed to the already-frozen current Git blob IDs `04fc181fd3354a4a072d7b488e244486a096d3c0` (prereg) and `40e2a2c7a96032fcf3b5c7ff369a8cf416e33d1c` (helper). Synthetic domain, arithmetic and Q1-Q4 criteria are unchanged. Successor run `33816670145` has already passed the repaired freeze and is installing exact NaMaster 2.7.

## Window-semantic governance that remains open
Exp073BU prereg requires full stock NaMaster bandpower-window shape `[2,39,2,12288]` before selecting `wins[0,:,0,:]` (`TE <- TE`). The proven Exp073CR ll3 kernel computes selected compact/general-coupling rows and may be reused only as source-code/resource lineage, never as historical numerical lineage. It may not silently replace the full-shape BU semantics.

The current support QA therefore tests, on deterministic synthetic masks, stock full-window `[2,8,2,48]` selected `TE<-TE` versus `mask PCL -> get_general_coupling_matrix(pcl,0,2,0,2) -> ascending band compression -> K -> np.linalg.solve(K,A)`. Only prospective Q1 exact evidence can support a later implementation-binding decision; Q2 numeric-only explicitly cannot.

## Preserved resource authority — Exp073CR v0.3
Run/job/head `33771269117` / `100701857748` / `023fcfa28f0eb904656c76e55c55d821e50c8155`; raw token `PASS_EXP073CR_V0_3_WM_S3_LL3_SHARDED_8CORE_RESOURCE`; checkpoint head `db8221278798ea56b579a3dc96565fef4497bb7f`; fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`; artifact `9903527609`, digest `sha256:28f6141e641726351b6dd804c07db28b6c4152de5a71a0c0b098b539a6bc0256`; CPU fraction `0.9623990689242612`, swap increase `0 KiB`, 64-shard exact resource reconstruction PASS. Classification remains RESOURCE PASS `+0/+0`, never Wm_S3 science.

## Frozen boundaries / preserved science
Wm_S1 Track-A exact PASS and admitted Wm_S2 authority are preserved; Wm_S3 authority remains absent. Historical old Wm_S3 route remains blocked by authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`. Exp073BT v0.3 remains Q5 incomplete `+0/+0`.

Frozen global boundaries: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
