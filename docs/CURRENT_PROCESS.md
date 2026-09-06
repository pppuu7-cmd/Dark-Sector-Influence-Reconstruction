# DSIR current-process ledger

Updated: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 `34005373819 / 101411448176`. `WW_S0_S1` remains admitted by Exp073EZ `34017921734 / 101444964371`, token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Frontier

`WW_S0_S2`, frozen as Exp073FA, prereg blob `edc044792be8ac7b796c8469943924942ae91932`; ordered `(S0,S2)`, R1 indices `[0,2]`; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; durable namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`; exact candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate alone never creates authority.

Exp073FC `34018341064 / 101446155067` is terminal raw-verified PASS `+0/+0`: `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`. It byte-binds the committed drivers to repaired Exp073FB output.

Exp073FD home-envelope prereg blob `6636766b565956d6af28ae04bcdeec1a410259a1`; fail-closed home shell blob `309c464bbfbe4896bd560165985ee7f643d9ee22`. First Exp073FD run `34020704615`, hosted job `101452648911`, is immutable infrastructure/static log-transport FAIL `+0/+0`; home science was skipped. Minimal repair changed only GitHub FC job-log parsing from erroneous ZIP handling to plain-text `grep -aF`; science was unchanged.

## Authoritative current process — Exp073FD / Exp073FA home science

- workflow: `Exp073FD Exp073FA audited home envelope and science v0.1`;
- run **`34020756634`**;
- hosted audit job **`101452788638`** = terminal SUCCESS, raw token `PASS_EXP073FD_EXP073FA_HOME_ENVELOPE_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`, no authority;
- home science job **`101452805620`** = **IN_PROGRESS**;
- branch `main`;
- run head **`894885b2c2b811954d1724c2733d2a810a486d70`**;
- run start `2026-09-06T08:02:37Z`;
- active step: `Run frozen ordered S0-to-S2 A/B gate with durable checkpoints`;
- checkpoint namespaces: `checkpoints/exp073fa-ww-s0-s2-a-v0-1`, `checkpoints/exp073fa-ww-s0-s2-b-v0-1`;
- expected candidate token: `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- last durable checkpoint: **`UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`** by explicit anti-bias policy.

**Runner ownership:** `DSIR-HOME-PC` is exclusively owned by Exp073FD/Exp073FA job `101452805620`. Do not launch another self-hosted DSIR task.

On terminal SUCCESS/candidate PASS: consume raw artifact/digest/provenance/checkpoint identities and exact A/B result; then freeze a dedicated hosted provenance admission bound to the exact terminal artifact. Only admission PASS may create `WW_S0_S2` authority. On scientific exact mismatch: record scientific FAIL and move to the next allowed branch. On infrastructure/software failure: diagnose the first causal defect and preserve/resume all validated complete checkpoints.

Frozen global boundaries remain: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `<=0.05`; Layer-B `<=0.05`; retained dimension `>=15`; NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.