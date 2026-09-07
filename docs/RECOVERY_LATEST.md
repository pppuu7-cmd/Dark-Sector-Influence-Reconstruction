# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_EXP073FW_A_PRESERVED_PRUNER_REPAIR_RESUME_V13.md` (creation commit `6940913d435609625ee52888e02915810f251c17`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and `S1_S3`. `WW_S2_S2` is **NOT ADMITTED**.

## Exp073FW terminal run 34125785882

Run `34125785882`, head `1c635f5192d26e76e0ec82a308363b666e5a248b`, is terminal FAILURE classified `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific FAIL. First causal failure: post-compute pruner raised `fail-closed missing FW pruner token 'WW_S1_S1'`. Hosted launch audit succeeded; provenance admission was skipped; no scientific authority was created.

Artifact `10023848524` independently downloaded: ZIP SHA256 `33b5999213247a9ad0c66957a021067f4f790f04d19eb1cf8d88910187eea66f`, exactly equal to GitHub digest. It contains a complete durable Replica-A chain through `replica_receipt_complete`, no B. A uses ordered `[2,2]`, same S2 map and same field object, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, exact `19,327,352,832`-byte file-backed MCM proof, full shape `[4,39,4,12288]`, selected `EE<-EE` shape `[39,12288]`, selected SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`. Expensive A must be reused unless its fail-closed chain later fails verification.

Prospective repair authority: commit `2a6a06f9d468879ca814ced15a56f82169507b3a`, repaired pruner blob `fb66e67d88a90b093a7da8b42ab0ac6fee13b504`; workflow binding commit `f7e925e782983824b7e916ce8437fcf924ec5760`, workflow blob `c7c651dfeac8a9d4a2d3da1dd6b11d7873af612a`. Only a nonexistent uppercase lexical requirement was removed; frozen science/arithmetic/domain/thresholds/source semantics/comparator remain unchanged.

## Authoritative current heavy process

Exp073FW recovery run **`34135965569`**, head **`f7e925e782983824b7e916ce8437fcf924ec5760`**.

- hosted audit job **`101786894169`**: SUCCESS, raw token `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, support `+0/+0`;
- home job **`101786993129`**: IN_PROGRESS at latest reconciliation inside frozen `WW_S2_S2` A/B gate;
- owner: `DSIR-HOME-PC-2`, checkpoint namespace `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- no competing heavy run observed;
- resume is checkpoint-first: validate/reuse complete A and compute only missing B/terminal comparison.

Exact next heavy action: terminal-consume `34135965569`; inspect raw logs/artifact and verify restoration provenance, complete A/B chains, same-field S2->S2 semantics, exact file-backed proof, finite canonical `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only frozen Exp073FX may create `WW_S2_S2` authority.

The FW workflow still has a path-scoped one-shot push trigger. Do not edit it while `34135965569` is active; restore dispatch-only semantics at a safe terminal transition to avoid duplicate launch.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance/effective-coordinate/fiducial-P rescue. No real C2 extraction while FW owns the home runner.

Exp073GR/GS/GT/GU remain raw-validated support authority as recorded in V11. Exp073GV prereg `6bf70f7ebdc164a63c2896dc5afeebd6b2972866`, fixture `23217fa330c550f9bd543e03989c90ac5836d6b2`, workflow `54e844ce0db3ebddc5f27b4dda60c98c57bc4421`; hosted run `34135739339`, job `101786143296`, raw-validated token `PASS_EXP073GV_C2_IDE_RECORD_PACKET_ADMISSION_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`. Synthetic 64-byte vector only; scientific record/prediction/model authority all false.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
