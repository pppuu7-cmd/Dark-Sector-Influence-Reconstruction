# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_FW_STATIC_CHAIN_REPAIRS_HOME_ACTIVE_V07.md` (creation commit `ac65c8414c514ada7ac7fb20a3ef235703f7152f`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and **`S1_S3`**.

`WW_S1_S3` authority was created only by Exp073FV in run `34120000242`, hosted admission job `101735763144`, token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s3_authority_created=true`.

Underlying artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, exact-equal finite `<f8 [39,12288] EE<-EE`, ordered `[1,3]=S1->S3`, `s1=1,s3=1`, distinct fields, exact `19,327,352,832`-byte file-backed MCM proof, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

Historical FU failures remain implementation/infrastructure `+0/+0`.

## Exp073FW repair history — all pre-science +0/+0

1. Run `34120059297`: hosted `101735824056` SUCCESS; home `101735874893` failed before checkpoint creation on impossible outer-envelope literal `source_pair:S2->S2`. No science scored. Repair commit `2bc804f641568a2517f903c0417a351889213219` moved exact identity audit to the frozen driver.
2. Run `34120560190`: hosted job `101737385038` failed only because its grep expanded `$GITHUB_WORKSPACE`; home was skipped. Static-audit `+0/+0`. Quoting repair commit `4b61f3250964333072c27478d3c167efc238db17`.
3. Run `34120852574`: hosted audit passed; home job `101738329773` failed before numerical science with `fail-closed tolerance/rescue path`. Cause was scanner self-match: driver-wrapper source contains forbidden spellings inside its own fail-closed scanner. Repair commit `e10279e39398ecd7912a93eabe25ad9031dd6130`, home-wrapper blob `84bbfada3dadd405196c6986ccc012333108f6a9`, restricts the outer-envelope scan to generated shell `s`; frozen driver still fail-closed scans transformed science. No science/domain/tolerance/arithmetic changed.

## Current heavy frontier — Exp073FW `WW_S2_S2`

Workflow binding commit `656dc15eb1999f3935b5b2dc3e6db74dda3cfe38` launched run **`34121012410`**.

- hosted launch audit job **`101738782234`**: SUCCESS;
- home-science job **`101738820469`**: IN_PROGRESS;
- runner owner: **`DSIR-HOME-PC-2`**;
- branch/head: `main` / `656dc15eb1999f3935b5b2dc3e6db74dda3cfe38`;
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- predecessor authority: Exp073FV run `34120000242`;
- expected gate: frozen `WW_S2_S2` A/B exact file-backed gate;
- competing DSIR heavy run: none.

The FW workflow temporarily retains a path-scoped one-shot push trigger. Do not edit that workflow while home job `101738820469` is active if that could create a duplicate; restore dispatch-only semantics at a safe terminal transition.

Exact next action: terminal-consume run `34121012410`; inspect raw logs/artifact, verify digest, complete checkpoint/provenance chains, S2->S2 same-field semantics, exact file-backed proof, canonical `<f8 [39,12288] EE<-EE`, finiteness and exact A/B equality. Workflow success alone is not scientific PASS. Only frozen Exp073FX may create `WW_S2_S2` authority.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, support/scientific `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance. No competing C2 heavy extraction while FW owns the runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
