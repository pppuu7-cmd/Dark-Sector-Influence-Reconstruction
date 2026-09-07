# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities now include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, **`S1_S3`**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_FV_S1S3_AUTHORITY_FW_ACTIVE_V05.md`, creation commit `de41fc32e9c65f28b849182bfeafd18412917df4`.

## Newly closed — Exp073FU/FV `WW_S1_S3`

Authoritative run `34120000242`; home job `101735669327` SUCCESS on `DSIR-HOME-PC-2`; artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, exact-equal finite `<f8 [39,12288] EE<-EE`. FV hosted job `101735763144` emitted `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s3_authority_created=true`.

Historical FU implementation/infrastructure failures remain `+0/+0` history and do not alter this admitted scientific authority.

## Authoritative current process — Exp073FW `WW_S2_S2`

- workflow/run: **Exp073FW `34120059297`**
- event: `workflow_dispatch` chained by successful FV admission
- branch/head: `main` / **`d45bf07026956e0bbd95da4f0bfb5840393390e1`**
- hosted launch audit job: **`101735824056` SUCCESS**
- home-science job: **`101735874893` IN_PROGRESS** at latest reconciliation
- runner ownership: **`DSIR-HOME-PC-2`** exclusively while active
- expected gate: frozen `WW_S2_S2` A/B exact file-backed science gate
- predecessor authority: Exp073FV run `34120000242`
- queued competing heavy runs: none observed
- exact next action on SUCCESS: consume raw artifact/logs, verify all frozen provenance/science gates, then admit/chain only under the preregistered contract
- exact next action on FAIL/BLOCKED: classify first causal failure; preserve valid durable checkpoints; smallest prospective repair/resume; never weaken science

Do not inspect partial numerical output to tune criteria and do not launch a competing home job.

## Independent C2 frontier

C2 remains support-only: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`. Runtime sampling/provenance is frozen at exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]` and k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; do not start competing cosmological heavy extraction while FW owns the runner.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
