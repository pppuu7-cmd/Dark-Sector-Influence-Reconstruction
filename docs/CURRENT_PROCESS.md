# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, **`S1_S3`**. `WW_S2_S2` is **NOT ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_C2_GV_SUPPORT_PASS_FW_ACTIVE_V12.md`, creation commit `827b38daa93f6b7fbe1da1f739063f8ef5b0956d`.

## Exp073FW terminal implementation history

All prior FW static/wrapper failures remain `+0/+0`; none is a scientific arithmetic FAIL. Direct frozen-FA repair authority: commit `820b0f8c082e45b2f51c3ff9d076a197ee3848f2`, wrapper blob `c4ef9587d5f4b54179304a44741eece2cec0a7a5`, binding head `1c635f5192d26e76e0ec82a308363b666e5a248b`.

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
- last verified FW checkpoint before this run: none; preceding failed runs produced no checkpoint files
- exact next action on terminal SUCCESS: consume raw logs/artifact, verify GitHub digest/ZIP and full checkpoint/provenance chain, then permit only frozen Exp073FX admission after independent validation
- exact next action on FAIL/BLOCKED: preserve valid complete checkpoints, diagnose first causal defect, smallest prospective repair/resume; genuine frozen numerical mismatch is a scientific FAIL and is never repaired post hoc

No competing DSIR heavy run is permitted. Partial numerical output must not be inspected to tune criteria. Do not edit the path-triggered FW workflow while home job `101754061309` is active if that could create a duplicate; restore dispatch-only semantics at a safe terminal transition.

## Independent C2 frontier

C2 remains support-only: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`; exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. No real C2 extraction while FW owns the runner.

- Exp073GR/GS/GT/GU remain raw-validated support authority exactly as recorded in immutable V11 recovery.
- Exp073GV prereg `6bf70f7ebdc164a63c2896dc5afeebd6b2972866`, fixture `23217fa330c550f9bd543e03989c90ac5836d6b2`, workflow `54e844ce0db3ebddc5f27b4dda60c98c57bc4421`; run **`34135739339`**, hosted job **`101786143296`**, raw-validated support PASS with exact token `PASS_EXP073GV_C2_IDE_RECORD_PACKET_ADMISSION_STATIC_AUDIT_V0_1`. Only a deterministic synthetic 64-byte vector was used; byte, length, ordinal, coordinate, source-provenance and digest mutations all failed closed. `scientific_record_admitted=false`, `cosmological_run_started=false`, `self_hosted_science_started=false`, `prediction_ready=false`, `scientific_model_authority_created=false`.

Exact independent next C2 work must remain hosted-only metadata/support work while FW owns the runner. GV creates no scientific model authority and does not authorize a real C2 extraction.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
