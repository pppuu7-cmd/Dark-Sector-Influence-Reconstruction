# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_FW_ENVELOPE_FAIL_REPAIR_RELAUNCH_V06.md` (creation commit `1f9bba600035a394ea9cb9a6ebf4bc87d8f0c6a2`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and **`S1_S3`**.

`WW_S1_S3` authority was created only by Exp073FV inside Exp073FU run `34120000242`, hosted admission job `101735763144`, exact token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, classification `SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s3_authority_created=true`.

Underlying FU artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, exact-equal finite `<f8 [39,12288] EE<-EE`, ordered `[1,3]=S1->S3`, reconstruction counts `s1=1,s3=1`, distinct fields, exact `19,327,352,832`-byte file-backed MCM proof, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

Historical FU implementation/infrastructure failures remain `+0/+0` and are not scientific failures.

## Exp073FW attempt 1 — infrastructure/implementation FAIL +0/+0

FV chained Exp073FW run `34120059297`. Hosted launch audit `101735824056` succeeded, but home job `101735874893` failed immediately before any FW science/checkpoint creation with first causal log message:

`fail-closed missing FW home invariant "'source_pair':'S2->S2'"`.

Provenance admission `101735934811` was skipped and evidence collection found no FW files. Therefore no `WW_S2_S2` scientific gate was scored and no authority was created.

Diagnosis: the frozen FW driver already contained/hosted-audited `source_count_map(r1_root,2)`, ordered `[2,2]`, and `compute_coupling_matrix(f2,f2,b)`. The outer home shell incorrectly demanded driver serialization literals inside a transformed shell envelope that does not contain them.

Prospective smallest repair commit `2bc804f641568a2517f903c0417a351889213219`, repaired home-wrapper blob `3c7e64e9a359ced198c2cb56b9a7c93f6c54c3d1`: exact S2->S2 identities are audited directly in the frozen driver; stale FM-token rejection and no tolerance/rescue checks remain. Frozen science is unchanged.

## Current heavy frontier — repaired Exp073FW

Workflow binding/one-shot activation commit `e71180515487fef117fe52f51fe9fdee983613df` launched repaired run **`34120560190`** after live Actions showed queued=0 and in_progress=0.

- workflow: Exp073FW `WW_S2_S2`
- run: `34120560190`
- head SHA: `e71180515487fef117fe52f51fe9fdee983613df`
- hosted audit job: `101737385038`, IN_PROGRESS at latest reconciliation
- home job: not yet assigned at this snapshot
- checkpoint namespace when/if home starts: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`
- predecessor authority: Exp073FV run `34120000242`
- competing heavy runs: none at launch

Exact next action: consume hosted audit. Only if it succeeds may exactly one home-science job own the runner. On terminal home result, consume raw logs/artifact and verify the frozen S2->S2 provenance, exact file-backed proof, canonical `<f8 [39,12288] EE<-EE`, finiteness and exact A/B equality. Workflow success alone is not a scientific PASS; only frozen Exp073FX may create `WW_S2_S2` authority.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, support/scientific `+0/+0`. Exact z grid `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k grid `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance. Do not start a competing C2 cosmological heavy extraction while FW owns or is waiting to own the home runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
