# DSIR current-process ledger

Updated: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 `34005373819 / 101411448176`. `WW_S0_S1` remains admitted by Exp073EZ `34017921734 / 101444964371`, token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Frontier

`WW_S0_S2`, frozen as Exp073FA, prereg blob `edc044792be8ac7b796c8469943924942ae91932`; ordered `(S0,S2)`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, durable namespaces `checkpoints/exp073fa-ww-s0-s2-{a,b}-v0-1`, exact candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Exp073FA prerequisite static audit `34018080500 / 101445404866` = PASS `+0/+0`.

Exp073FB first run `34018169771 / 101445653251` remains implementation-static FAIL `+0/+0`: missing lowercase schema identity transform `s0_s1 -> s0_s2`; no science ran. Minimal repair commit `28c7afc1a83a5a5bf7019218eccc382abcdf0c3a` changed only that identity substitution.

Repaired Exp073FB run/job `34018241319 / 101445845648` = SUCCESS. Raw token `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`, classification support `+0/+0`, no authority. Artifact `9984600349`, name `exp073fb-exp073fa-s0-s2-generated-drivers-v0-1`, GitHub digest and independently downloaded ZIP SHA256 `b371821a77cb4a62051ceee45f82764a5486ea3b0bcf0939a9bcac0eff624cda`. Transformation receipt binds generated driver SHA256s `fe354b95e9aeefe0772f4c7eecbba6e1944fb1f4955fceb3e9e72ed1c06b293a` and `77f321e22c923d8d5996105487cae9afb6eecc5863174d849b092164a26824ba`, science pair `S0->S2`, ordered `[0,2]`, no historical numerical import.

Those exact generated sources are now committed as `ci/exp073fa_ww_s0_s2_durable_ab_production_v0_1.py` and `_v0_2.py`.

## Authoritative current process — Exp073FC

Purpose: independently bind committed Exp073FA drivers byte-for-byte to the repaired Exp073FB generated artifact before any home science envelope is allowed.

- workflow `Exp073FC Exp073FA committed driver binding v0.1`;
- run **`34018341064`**;
- job **`101446155067`**;
- head **`3910e16b18e62464b1aa32b57e158552b6321b45`**;
- state at ledger update: **QUEUED** on GitHub-hosted runner;
- prereg `experiments/073fc_exp073fa_committed_driver_binding_v0_1_prereg.md`, blob `9e194c2617114b88c46fa349c10dddf70cccd6da`;
- expected token `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1`;
- PASS is support/governance `+0/+0`, never WW authority.

**Runner ownership:** `DSIR-HOME-PC` currently has no DSIR owner; no Exp073FA science checkpoint exists yet.

On FC PASS: consume raw audit; freeze a dedicated fail-closed home execution envelope referencing exact committed driver blobs, qualified read patch, R1 authority, resource/exclusivity checks and dedicated FA checkpoints; hosted-audit that envelope, verify zero competing self-hosted jobs, then launch exactly one Exp073FA A/B science run. On FC failure: diagnose first causal binding defect without changing science.

Frozen global boundaries remain: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `<=0.05`; Layer-B `<=0.05`; retained dimension `>=15`; NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.