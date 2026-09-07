# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, **`S1_S3`**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_FW_ENVELOPE_FAIL_REPAIR_RELAUNCH_V06.md`, creation commit `1f9bba600035a394ea9cb9a6ebf4bc87d8f0c6a2`.

## Newly closed — Exp073FU/FV `WW_S1_S3`

Run `34120000242`; home job `101735669327` SUCCESS on `DSIR-HOME-PC-2`; artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`. FV job `101735763144` admitted authority with `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Historical Exp073FW attempt 1 — implementation FAIL +0/+0

Run `34120059297`, head `d45bf07026956e0bbd95da4f0bfb5840393390e1`; hosted audit `101735824056` SUCCESS; home job `101735874893` FAILURE before science/checkpoint creation; admission skipped. First causal failure: outer wrapper demanded impossible literal `source_pair:S2->S2` inside a shell envelope. No FW artifact/files existed and no scientific gate was scored.

Repair commit `2bc804f641568a2517f903c0417a351889213219`, wrapper blob `3c7e64e9a359ced198c2cb56b9a7c93f6c54c3d1`: source-pair/order invariants are now checked directly against the frozen driver, with stale-token and no-tolerance checks retained. Science unchanged.

## Authoritative current process — repaired Exp073FW `WW_S2_S2`

- workflow/run: **Exp073FW `34120560190`**
- event: one-shot path-scoped push after verifying live queued=0 / in_progress=0
- branch/head: `main` / **`e71180515487fef117fe52f51fe9fdee983613df`**
- workflow binding commit: `e71180515487fef117fe52f51fe9fdee983613df`
- repaired home-wrapper blob: `3c7e64e9a359ced198c2cb56b9a7c93f6c54c3d1`
- hosted launch audit job: **`101737385038` IN_PROGRESS** at latest reconciliation
- home-science job: not assigned yet at this snapshot
- checkpoint namespace when home starts: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`
- predecessor authority: Exp073FV `34120000242`
- exact next action on hosted SUCCESS: allow exactly one home job; record runner ownership/job id; consume terminal result immediately
- exact next action on FAIL: classify first causal defect; no science repair/post-hoc threshold changes

No competing DSIR heavy process existed at launch. Do not inspect partial numerical output to tune criteria.

## Independent C2 frontier

C2 remains support-only `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`; exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. Do not start competing C2 heavy extraction while FW is queued/running.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
