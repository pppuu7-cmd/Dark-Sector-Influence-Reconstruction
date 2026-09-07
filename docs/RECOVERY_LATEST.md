# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_C2_GV_SUPPORT_PASS_FW_ACTIVE_V12.md` (creation commit `827b38daa93f6b7fbe1da1f739063f8ef5b0956d`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and **`S1_S3`**. `WW_S2_S2` is **NOT ADMITTED**.

`WW_S1_S3` authority was created only by Exp073FV run `34120000242`, admission job `101735763144`, token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, exact-equal finite `<f8 [39,12288] EE<-EE`, ordered `[1,3]=S1->S3`, distinct fields, exact `19,327,352,832`-byte file-backed proof.

## Current heavy frontier — Exp073FW `WW_S2_S2`

Authoritative live run: **`34125785882`**, head **`1c635f5192d26e76e0ec82a308363b666e5a248b`**.

- hosted launch audit job **`101754018941`**: SUCCESS, token `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, classification support `+0/+0`;
- home-science job **`101754061309`**: IN_PROGRESS at latest reconciliation inside frozen `WW_S2_S2` A/B gate;
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`;
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- no competing DSIR heavy run observed; partial numerical output not inspected.

Historical FW implementation/static failures remain `+0/+0`; current direct frozen-FA repair authority is commit `820b0f8c082e45b2f51c3ff9d076a197ee3848f2`, wrapper blob `c4ef9587d5f4b54179304a44741eece2cec0a7a5`, binding head `1c635f5192d26e76e0ec82a308363b666e5a248b`.

Exact next heavy action: terminal-consume `34125785882`; inspect raw final logs/artifact, verify GitHub artifact digest/ZIP, complete checkpoint/provenance chain, frozen S2->S2 same-field semantics, exact `19,327,352,832`-byte file-backed proof, canonical finite `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only frozen Exp073FX may create `WW_S2_S2` authority.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance/effective-coordinate/fiducial-P rescue. No real C2 extraction while FW owns the home runner.

Preserved support chain: Exp073GR/GS/GT/GU raw-validated support PASS as recorded in V11 recovery. Exp073GV prospective prereg `6bf70f7ebdc164a63c2896dc5afeebd6b2972866`, fixture `23217fa330c550f9bd543e03989c90ac5836d6b2`, workflow `54e844ce0db3ebddc5f27b4dda60c98c57bc4421`; hosted run **`34135739339`**, job **`101786143296`**, raw-validated exact token `PASS_EXP073GV_C2_IDE_RECORD_PACKET_ADMISSION_STATIC_AUDIT_V0_1`. It used only a clearly synthetic deterministic 64-byte vector, rejected byte/length/ordinal/coordinate/provenance/digest mutations fail-closed, and emitted `scientific_record_admitted=false`, `cosmological_run_started=false`, `self_hosted_science_started=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `classification=SUPPORT_PLUS_0_PLUS_0`.

GV freezes only the future exact-record packet admission boundary; it creates no scientific payload or authority. Exact independent next C2 work must remain hosted-only metadata/support work while FW owns the runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
