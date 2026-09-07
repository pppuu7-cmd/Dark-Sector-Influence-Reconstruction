# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_FV_S1S3_AUTHORITY_FW_ACTIVE_V05.md` (creation commit `de41fc32e9c65f28b849182bfeafd18412917df4`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities now include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and newly admitted **`S1_S3`**.

`WW_S1_S2` remains created only by Exp073FT run `34067352681`, job `101632852284`.

`WW_S1_S3` authority was created only by Exp073FV inside Exp073FU run **`34120000242`**, hosted admission job **`101735763144`**, exact token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, classification `SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s3_authority_created=true`.

Underlying successful FU evidence: home job `101735669327` on `DSIR-HOME-PC-2`; artifact **`10017795904`**; ZIP SHA256 **`91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`** independently matched; canonical A/B selected SHA256 **`aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`**, exact-equal finite `<f8 [39,12288] EE<-EE`. Frozen ordered `[1,3]=S1->S3`, reconstruction counts `s1=1,s3=1`, distinct fields, exact `19,327,352,832`-byte file-backed MCM proof, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251` all passed.

Historical FU failures remain implementation/infrastructure `+0/+0`, never rewritten as scientific failures. Repairs were interface/resume-only: comparator blob `08e91910da2b510ef92ab705dbbe360f57506a31`, terminal-resume wrapper blob `a32eb3c47b4e6c557d43a572a0af356c91134e1b`, FV verifier blob `0c17dae9172316563a0b09d1da07cceb152acb7a`; frozen science was unchanged.

## Current heavy frontier — Exp073FW `WW_S2_S2`

FV admission deterministically dispatched the next already-frozen heavy workflow.

- run: **`34120059297`** (`Exp073FW WW_S2_S2 autonomous audited home science v0.1`)
- head SHA: `d45bf07026956e0bbd95da4f0bfb5840393390e1`
- hosted launch audit job `101735824056`: SUCCESS
- home-science job **`101735874893`**: IN_PROGRESS at latest reconciliation
- owner: `DSIR-HOME-PC-2`
- expected gate: frozen `WW_S2_S2` A/B exact file-backed gate
- competing DSIR heavy runs: none

Exact next action: terminal-consume run `34120059297`; inspect raw logs and artifact, verify digest, complete checkpoint/provenance chain, frozen field/source semantics, exact file-backed proof, canonical finiteness and A/B equality, then classify under the preregistered contract. Workflow success alone is not scientific PASS.

## Independent C2 support frontier

C2 IDE remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. The prospectively frozen runtime sampling/provenance contract uses exact z grid `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]` and k grid `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`, pinned CLASS lineage and no interpolation/smoothing/averaging/tolerance. Do not start competing C2 cosmological heavy extraction while FW owns the home runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
