# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_WW_S2_S3_ADMITTED_GA_ACTIVE_V26.md` (creation commit `f2ba0ea22a1008f41b10b1014d84fa3abd9905bd`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority now includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and **`S2_S3`**. `WW_S3_S3` remains **NOT_YET_ADMITTED** while the final frozen heavy gate is active.

## Exp073FY S2->S3 authority

No expensive FY recomputation was required. Preserved source evidence is Exp073FY run `34160898921`, home job `101862390771`, artifact `10040351900`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

HD/HE exposed only dependency/source-semantics/provenance implementation failures `+0/+0`. HE established exact FY candidate equality; HF run `34189183845`, job `101943539978`, then completed hosted provenance admission and emitted `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s2_s3_authority_created=true`.

Therefore `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`; no new scientific FAIL was created by the recovery chain.

## Active final heavy successor

The stale GA predecessor handoff was repaired at orchestration level to consume the admitted HF authority, without changing frozen GA/GB numerical logic, contracts, thresholds, source ordering, or hypothesis identities. A first hosted-only launch attempt `34189505842` stopped on a one-character pruner blob pin typo before home science and is `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`. Corrected workflow commit: `10e6fb67af7d6485fca3d1ecf2362e4622883417`.

Current single active heavy workflow: Exp073GA `WW_S3_S3`, run **`34189540992`**. Hosted job `101944582891` is `SUCCESS`; self-hosted job `101944608861` is `IN_PROGRESS` on the frozen A/B gate. Global reconciliation found exactly one in-progress workflow and zero queued workflows. Do not launch a duplicate heavy run.

Next allowed transition: wait for terminal GA evidence; if its frozen candidate succeeds, permit only the frozen GB provenance admission. Keep infrastructure failure, `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` distinct from scientific FAIL.

Full incident/recovery detail is in V26 and `docs/research_log/RESEARCH_LOG_2026-09-08_AUTOGUARD_TURN11_FY_ADMITTED_HE_HF_GA_RESUME.md`.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
