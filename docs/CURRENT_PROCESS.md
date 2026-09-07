# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, **`S1_S3`**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_FW_STATIC_CHAIN_REPAIRS_HOME_ACTIVE_V07.md`, creation commit `ac65c8414c514ada7ac7fb20a3ef235703f7152f`.

## Closed authority — Exp073FU/FV `WW_S1_S3`

Run `34120000242`; home job `101735669327` SUCCESS; artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`. FV job `101735763144` admitted authority with `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Exp073FW pre-science repair history

- `34120059297`: home `101735874893` implementation FAIL `+0/+0`, impossible outer-shell source-pair literal; no checkpoint/science.
- `34120560190`: hosted `101737385038` static-audit FAIL `+0/+0`, `$GITHUB_WORKSPACE` grep expansion; home skipped.
- `34120852574`: hosted passed, home `101738329773` implementation FAIL `+0/+0` before science due tolerance-scanner self-match on driver-wrapper audit strings; no scientific gate.

Prospective repairs: outer-envelope/driver separation commit `2bc804f641568a2517f903c0417a351889213219`; hosted quoting commit `4b61f3250964333072c27478d3c167efc238db17`; self-match repair commit `e10279e39398ecd7912a93eabe25ad9031dd6130`, current home-wrapper blob `84bbfada3dadd405196c6986ccc012333108f6a9`. Frozen science/domain/arithmetic/tolerances unchanged.

## Authoritative current process — Exp073FW `WW_S2_S2`

- workflow/run: **Exp073FW `34121012410`**
- event: one-shot path-scoped push
- branch/head: `main` / **`656dc15eb1999f3935b5b2dc3e6db74dda3cfe38`**
- hosted launch audit job: **`101738782234` SUCCESS**
- home-science job: **`101738820469` IN_PROGRESS**
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`
- predecessor authority: Exp073FV `34120000242`
- expected gate: frozen WW `S2->S2`, same-field semantics, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality, exact file-backed MCM proof, no tolerance rescue
- exact next action on terminal SUCCESS: consume raw artifact/log and run frozen Exp073FX provenance admission only after independent validation
- exact next action on FAIL/BLOCKED: preserve completed checkpoints, diagnose first causal defect, smallest prospective repair/resume; numerical mismatch is scientific FAIL, never repaired post hoc

The workflow still has a temporary path-scoped push trigger. Do not edit it while home job `101738820469` is active if that could trigger a duplicate. Restore dispatch-only semantics at the safe terminal transition.

No competing DSIR heavy run is permitted. Partial numerical output must not be inspected to tune criteria.

## Independent C2 frontier

C2 remains support-only: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`; exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. No competing C2 heavy extraction while FW owns the runner.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
