# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities now include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, and newly admitted **`S1_S2`**.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-07_FS_ADMITTED_FU_WRAPPER_REPAIR_RUN5.md`, creation commit `3a21aecf36a0ec3add6c172f89d7a0cc6c8fb7d2`.

## Newly admitted WW_S1_S2

Exp073FS run `34067352681` attempt 2, home job `101592579318`, artifact `10005532345`, artifact ZIP SHA256 `f878a49241dde97eb0ef1d24561719cf896a77d111c3a3b91725d4989b894d23`. Candidate A/B exact SHA256 `77f3e314d76f85cb95ed8edade672575bfa0e40c3b10a831f380a6c6d5f977fd`; canonical `<f8 [39,12288] EE<-EE`; exact equality; finite; ordered `S1->S2`; distinct fields; complete pre-prune chains; exact `19,327,352,832`-byte file-backed proof. Exp073FT admission job `101632852284` emitted `PASS_EXP073FT_WW_S1_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s1_s2_authority_created=true`.

## Exp073FU historical implementation/infrastructure failures +0/+0

- run `34087011068`, home job `101632910644`: pre-science false positive from outer wrapper scanning inherited scanner literals; no checkpoint/science artifact;
- repair `07de7028dd2cb8baf1927ddcdbceef812bda45f3`, workflow binding `511d008b7b5ce74ade38e6d3cdc7faa537d95dc8`;
- run `34089005639`, home job `101638631901`: pre-science generated-shell syntax failure caused by transform-of-transform wrapper architecture;
- direct frozen-base repair `fa01c7d7a2d20cd222c1d208ac4e359ad1313710`;
- run `34089259696`, home job `101639297762`: direct wrapper parsed, then failed pre-science because FA-base-required `EM_GENERATOR_BLOB`/`EM_COMPARE_BLOB` were not exported;
- storage-identity repair `614c5bca01280792b5ea0affe93729fbea174d40`, wrapper blob `4e6d24fc26760c7e7d31545837239148269d81d5`, binding exact helper blobs `bd1795f2a2c2cf80341f212996eb8278e0be53d9` / `f0de92f3f121592b6d139eb7d948426946d901d1`.

All three FU failures are historical `IMPLEMENTATION/INFRASTRUCTURE_PLUS_0_PLUS_0`; no FU scientific gate was scored and no frozen criterion was changed.

## Authoritative current process — Exp073FU / WW_S1_S3

- workflow/run: **Exp073FU `34089383137`**;
- branch/head: `main` / **`11b62ebd73fe8bed03f31c559593756149c7fbc0`**;
- hosted launch job: **`101639612389` SUCCESS**;
- home job: **`101639652148`**, latest observed state **QUEUED** after hosted audit;
- predecessor authority run: **Exp073FS/FT `34067352681`**;
- checkpoint root: `~/.cache/dsir/exp073fu-ww-s1-s3-filebacked-ab-v0-1`, replicas `/checkpoints/A` and `/checkpoints/B`;
- last durable checkpoint: `NONE_YET_CONFIRMED`; no partial output inspected;
- expected gate: ordered `[1,3] = S1->S3`, distinct fields, DES NSIDE=4096, ell `0..12287`, 39 bands, public file-backed BPW, canonical `<f8 [39,12288] EE<-EE`, exact A/B SHA and array equality, all finite;
- frozen source/contract: `de83e20a68f79ccf25b89b0d33eb4206e294c757` / `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- exact next action on SUCCESS: consume candidate artifact, independently verify full provenance and only then allow Exp073FV admission;
- exact next action on infrastructure/resource FAIL: preserve verified complete checkpoints, diagnose first causal defect, smallest prospective repair/resume;
- exact next action on numerical mismatch: scientific FAIL, no tolerance rescue.

The live Actions reconciliation showed exactly one in-progress DSIR workflow (`34089383137`) and no competing heavy computation. Runner ownership must be taken from the live home job once assigned; no second home job may be launched.

Remaining deterministic queue after valid FV authority: `FW -> FX -> FY -> FZ -> GA -> GB -> STOP`.

## Independent C2 IDE status

Exp073GK deterministic generator/source-binding support remains unchanged: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Standard CLASS `d_m` is already gauge-invariant and cannot be fed through the frozen correction again. Exact independent next C2 step remains a prospectively frozen/static-audited pre-transform extraction hook; do not run it on home while FU owns the heavy frontier.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
