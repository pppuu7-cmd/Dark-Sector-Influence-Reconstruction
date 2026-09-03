# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative.

## Current owner/process
- **DSIR-HOME-PC: FREE.** No self-hosted heavy/scientific process is authorized.
- Exp073BU numerical Wm_S3 science: **NOT ACTIVATED**.
- Current support-only process: NaMaster-2.7 stock-window source audit run `33816987697`, job `100851195938`, head `d80042807faf26f29eeb2a11e026632bba0083b4`, hosted Ubuntu only, no home ownership, no science authority.
- Frozen audit preregistration: `experiments/073bu_support_namaster27_stock_window_source_audit_v0_1_prereg.md`, commit `798eabda7fa7ba2cbe28262fdb37fb4970327431`.
- Current state: freeze PASS; exact NaMaster 2.7 installation in progress.
- Exact terminal action: consume raw source-audit receipt/artifact and classify S1/S2/S3/S4. S1 only permits a later prospectively frozen exact-stock emulator/equivalence audit; it does not activate science. S2 remains partial/open; S3/S4 require provenance/infrastructure diagnosis.

## Prospective scientific gate — Exp073BU v0.1
- preregistration `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`;
- intended namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`;
- required science token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`;
- state: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**.

Scientific A/B PASS remains exact canonical SHA256 equality plus `numpy.array_equal` on complete canonical `<f8 [39,12288]` after valid isolated provenance. No tolerance rescue.

## Newly consumed selected-TE support result — Q2 NON-AUTHORIZING `+0/+0`
Support prereg commit `b31733b1047a39942118b409d63e4faa8d8c4b7a`; helper commit `bed56467b0d9f145ca9e1c5e896d92e02d5141fa`.

First run `33816536157` / job `100849813933` / head `9be393e6fb015ddfb4a262222866c879ede0c7f1` was Q4 infrastructure incomplete before numerical execution: shallow checkout could not resolve older commit-tree paths. Smallest repair commit `a10ef5e664c4d1b20a668f080251ffdea98752a2` changed only source freeze binding to already-frozen Git blob IDs; domain/arithmetic/Q rules unchanged.

Repaired run/job/head `33816670145` / `100850227684` / `a10ef5e664c4d1b20a668f080251ffdea98752a2` completed SUCCESS and raw receipt classified:
- `Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE`;
- PyMaster `2.7`;
- stock full shape `[2,8,2,48]`, selected `<f8 [8,48]`;
- stock SHA `dbc75e2d3977db6596a30c2fe204e2b68631ef6c9ce5b4cd1d8ba766b023a688`;
- low-memory selected SHA `5047b92334b72e163059271310acd2fbbafc349dbd76bbec65edc6dc9b492e2e`;
- `numpy.array_equal=false`, SHA equality false;
- max abs difference `1.4710455076283324e-15`;
- artifact `9916798055`, digest `sha256:2244e5ce5df5f48db40c51fca3dba1321fef1125424c7baea74edbaa4008f520`;
- immutable recovery `recovery/2026-09-04_exp073bu_selected_te_support_q2_numeric_only.md`, commit `a708f982a9ddffc39cf4d53924604f952f0e05aa`.

Frozen Q2 rule explicitly forbids using the `1e-12` support threshold to authorize scientific runtime substitution. Therefore the existing Exp073CR-style selected compact finalizer **cannot replace** preregistered full-stock Exp073BU window semantics.

## Closed input/PCL support gates
Input staging PASS `+0/+0`: run/job/head `33815944381` / `100848002128` / `00b8a2c25ec4e50ae1027a1a2141a0023a033ab9`; token `PASS_EXP073BU_FROZEN_INPUT_STAGING_CLOSURE_V0_1`; artifact `9916526843`, digest `sha256:74307daaf5e7cece0ce2be2fa68edef8bc63c2e7f2439f20375ccac3dde97b69`; recovery commit `60e5fcefbba9ab5701be207e88e6806426d6675e`.

Fresh-PCL static implementation PASS `+0/+0`: helper commit `e6ffda3b5c558c964cf486d78a792d40bf9c76e5`; run/job/head `33816258925` / `100848963246` / `04b0b29cbed039de6520eb6a738f78bdc9785885`; token `PASS_EXP073BU_FRESH_PCL_HOSTED_STATIC_AUDIT_V0_1`; helper SHA `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`; artifact `9916627301`, digest `sha256:35e4ace8514a3614bc697ceb398268789a9db7e81d049b1910ca7a428dccd65d`; recovery commit `3621235e56347fc9a65bbfaf41ba7aaf356a3ae3`.

Frozen input authority: Exp073R1 run/job/head `33270843577` / `99148916507` / `ef783ca941fb9b9b5f5eae537986c56ff06e6536`; artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`; S3 record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`; redMaGiC mask SHA `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

## Preserved resource/science history
Exp073CR v0.3 remains RESOURCE PASS `+0/+0`: run/job/head `33771269117` / `100701857748` / `023fcfa28f0eb904656c76e55c55d821e50c8155`; checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`; fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`; CPU fraction `0.9623990689242612`, swap `0 KiB`; artifact `9903527609`, digest `sha256:28f6141e641726351b6dd804c07db28b6c4152de5a71a0c0b098b539a6bc0256`. This is not Wm_S3 science.

Wm_S1 Track-A exact PASS and admitted Wm_S2 authority remain preserved. Old Wm_S3 route remains blocked by authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`. Exp073BT v0.3 remains Q5 incomplete `+0/+0`. **Wm_S3 authority remains absent.**

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
