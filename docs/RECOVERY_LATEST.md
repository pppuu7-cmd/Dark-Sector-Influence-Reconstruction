# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_GA_LEDGER_SYNC_V27.md` (creation commit `d4ec802705fc4b3d6f2e0a424b244c1b279b2533`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and **`S2_S3`**. `WW_S3_S3` remains **NOT_YET_ADMITTED** while the final frozen heavy gate is active.

## Exp073FY S2->S3 authority

Preserved source evidence remains Exp073FY run `34160898921`, home job `101862390771`, artifact `10040351900`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

HE established exact FY candidate equality; HF run `34189183845`, job `101943539978`, emitted `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s2_s3_authority_created=true`. Therefore `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`. HD/HE infrastructure/provenance failures remain historical `+0/+0`, not scientific FAIL.

## Active final heavy successor

Current single active heavy workflow: Exp073GA `WW_S3_S3`, run **`34189540992`**, head **`10e6fb67af7d6485fca3d1ecf2362e4622883417`**. Hosted job `101944582891` is `SUCCESS`; self-hosted job `101944608861` is `IN_PROGRESS` on the frozen A/B gate. Live global reconciliation found exactly one in-progress workflow and zero queued workflows. Do not launch a duplicate heavy run.

Checkpoint root: `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`. Candidate token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Only frozen GB output `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s3_s3_authority_created=true` may create final authority.

V27 repaired stale process-ledger governance only: `docs/CURRENT_PROCESS.md` is synchronized to live V26/V27 authority in commit `8e168bd9bb1f2a3177d493197e610aaaaaae1b52`. No scientific code, arithmetic, source ordering, domain, thresholds, tolerances or checkpoint semantics changed. No partial GA numerical output was inspected.

Next allowed transition: wait for terminal GA evidence; consume raw log/artifact/provenance/checkpoint identity and exact A/B result, then permit only frozen GB admission if the candidate passes.

Research log: `docs/research_log/RESEARCH_LOG_2026-09-08_GA_LEDGER_SYNC_V27.md` (creation commit `e1d19544113b7464398a12ef6b9416f4d24128d5`).

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
