# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, **`S1_S3`**. `WW_S2_S2` is **NOT ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_C2_GR_GS_SUPPORT_PASS_FW_ACTIVE_V10.md`, creation commit `6a5b5f4ce9194f09f658b6e78479e381e12b3851`.

## Exp073FW terminal implementation history

All prior FW static/wrapper failures remain `+0/+0`; none is a scientific arithmetic FAIL. Run `34125530921`, hosted job `101753205410`, passed `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_4`; home job `101753245014` failed before numerical science with `continue: only meaningful in a for... loop` followed by shell syntax error. No checkpoint/evidence files existed and Exp073FX admission was skipped.

First causal defect: nested transform self-overwrite. The FW wrapper executed transformed FM, while inherited FM generated a second script at the same `$RUNNER_TEMP/exp073fw_home_filebacked_fullres_v0_1.transformed.sh` path currently being executed.

Prospective repair commit `820b0f8c082e45b2f51c3ff9d076a197ee3848f2` adopts the proven direct frozen-FA transform architecture, pins FA blob `309c464bbfbe4896bd560165985ee7f643d9ee22`, binds existing storage-audit helper identities, preserves frozen FW S2->S2 driver semantics and adds `bash -n` on the generated shell. Wrapper blob `c4ef9587d5f4b54179304a44741eece2cec0a7a5`. Binding commit: `1c635f5192d26e76e0ec82a308363b666e5a248b`.

## Authoritative current process — Exp073FW `WW_S2_S2`

- workflow/run: **Exp073FW `34125785882`**
- branch/head: `main` / **`1c635f5192d26e76e0ec82a308363b666e5a248b`**
- hosted launch audit job: **`101754018941` SUCCESS**
- hosted raw token: `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, `classification=SUPPORT_PLUS_0_PLUS_0`
- home-science job: **`101754061309` IN_PROGRESS**
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`
- predecessor authority: Exp073FV `34120000242`
- expected gate: frozen WW `S2->S2`, same-field semantics, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality, exact `19,327,352,832`-byte file-backed MCM proof, no tolerance rescue
- last verified FW checkpoint before this run: none; the preceding failed runs produced no checkpoint files
- exact next action on terminal SUCCESS: consume raw logs/artifact, verify GitHub digest/ZIP and full checkpoint/provenance chain, then permit only frozen Exp073FX admission after independent validation
- exact next action on FAIL/BLOCKED: preserve any valid complete checkpoints, diagnose first causal defect, smallest prospective repair/resume; genuine frozen numerical mismatch is a scientific FAIL and is never repaired post hoc

No competing DSIR heavy run is permitted. Partial numerical output must not be inspected to tune criteria. Do not edit the path-triggered FW workflow while home job `101754061309` is active if that could create a duplicate; restore dispatch-only semantics at a safe terminal transition.

## Independent C2 frontier

C2 remains support-only: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`; exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. No competing C2 heavy extraction while FW owns the runner.

- Exp073GR run `34130804754`, job `101770188173`: raw-validated `SUPPORT_PLUS_0_PLUS_0` PASS, token `PASS_EXP073GR_C2_IDE_RUNTIME_SAMPLING_PROVENANCE_CONTRACT_V0_1`; canonical contract SHA256 `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`; 28 exact unique z-major/k-minor requests; recorder blob verified; prohibited transformations all false.
- Exp073GS run `34130948407`, job `101770660311`: raw-validated `SUPPORT_PLUS_0_PLUS_0` PASS, token `PASS_EXP073GS_C2_IDE_RUNTIME_REQUEST_EMITTER_AUDIT_V0_1`; exact ordinals `0..27`; contract mutation fails closed before emission; provenance manifest SHA256 `1448d6d6ac3ef2a018af3df9b732a91d4006263bc2fb8b7d232e1eded87316b0`.

Exact independent next C2 gate permitted: prospectively frozen hosted-only dry-run record-envelope assembly binding each of the 28 deterministic requests to the validated 64-byte recorder ABI. It must not build/run CLASS, use the home runner, or create scientific model authority.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
