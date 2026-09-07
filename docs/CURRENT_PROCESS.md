# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`. `WW_S2_S2` is **NOT ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_EXP073FW_COMPARATOR_NAMESPACE_REPAIR_AND_CHECKPOINT_ONLY_RESUME_V16.md`, creation commit `e71e5990ca976922e3c759c5645c24d566a044a3`.

## Terminal predecessor — Exp073FW run 34135965569

- head `f7e925e782983824b7e916ce8437fcf924ec5760`;
- hosted job `101786894169` SUCCESS; home job `101786993129` FAILURE; admission `101817055237` SKIPPED;
- classification `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific FAIL;
- first cause: terminal comparator `checkpoint_namespace` mismatch because transformed comparator omitted hyphenated `ww-s1-s1 -> ww-s2-s2`;
- artifact `10027545256`, independently verified ZIP SHA256 `0be01af5b522821fcdcd52be9fb2ef4ae5849efd2c4e439b9d7ad8462765cfb4`;
- complete A and B durable chains preserved;
- both canonical A/B selected arrays SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`, exact array equality true, both finite, max absolute difference `0.0`;
- frozen S2->S2, ordered `[2,2]`, same-field semantics and exact `19,327,352,832`-byte MCM proof preserved.

Minimal repair: commit `ced70da68cd148cfba4c7dec33b8140989557bee`, comparator blob `b5b828bd71eaf6da360c8ebfa279888165531e49`. Workflow binding/static audit commit `3835072cf580fc0a0950794385c028012f60a5cb`. Frozen science unchanged.

## Authoritative current process — Exp073FW checkpoint-only comparator resume

- workflow/run: **`34145888831`**;
- branch/head: `main` / **`3835072cf580fc0a0950794385c028012f60a5cb`**;
- hosted launch audit: **job `101817723744` SUCCESS**, raw `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_6`, support `+0/+0`;
- home-science: **job `101817765818` IN_PROGRESS**;
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`;
- checkpoint root: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- last durable authority: both complete Replica A and B identified above;
- expected gate: restored frozen WW `S2->S2`, same-field semantics, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality, exact file-backed MCM proof, no tolerance rescue;
- exact next action on SUCCESS: terminal-consume raw comparator/artifact and require frozen Exp073FX provenance admission before creating `WW_S2_S2` authority;
- exact next action on FAIL/BLOCKED: preserve both complete replicas, diagnose first causal defect and repair only implementation/infrastructure; a genuine exact numerical mismatch is scientific FAIL and is never repaired post hoc.

No competing heavy run is permitted. Do not inspect partial numerical output. The workflow retains a temporary path-scoped push trigger; do not edit it while `34145888831` is active. Restore dispatch-only semantics at a safe terminal transition.

## Independent C2 frontier

Exp073GW/GX/GY remain hosted support-only `+0/+0`. GY run `34141294357 / 101803642167` raw-validated `PASS_EXP073GY_C2_IDE_RUNTIME_PACKET_SET_ADMISSION_BOUNDARY_V0_1` with `scientific_record_set_admitted=false` and no model authority.

Exact next C2 action remains real runtime generation/admission of the 28-packet set under frozen GW/GX/GY provenance, **BLOCKED while FW owns home**. No further metadata-only scaffolding is justified.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.