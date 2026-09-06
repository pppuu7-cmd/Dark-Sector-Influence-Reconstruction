# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`. `WW_S0_S1` remains admitted by Exp073EZ run/job `34017921734 / 101444964371`, token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Exp073EY S0_S1 candidate authority source remains run/job `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, selected exact A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`.

## Current frontier

`WW_S0_S2`, frozen as Exp073FA by prereg blob `edc044792be8ac7b796c8469943924942ae91932`. Ordered pair `(S0,S2)`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, checkpoint namespaces `checkpoints/exp073fa-ww-s0-s2-{a,b}-v0-1`, expected candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Exp073FA prerequisite static audit `34018080500 / 101445404866` = SUCCESS, raw token `PASS_EXP073FA_WW_S0_S2_PREREQUISITE_STATIC_AUDIT_V0_1`, classification support `+0/+0`, no authority.

## Exp073FB implementation transformation

Prereg blob `7ff28ad4239728c14d05094b55ffc713c52210e6` freezes the permitted transformation from the already validated Exp073EY durable driver architecture to Exp073FA `(S0,S2)`.

Historical first run/job `34018169771 / 101445653251` = **INFRASTRUCTURE/IMPLEMENTATION STATIC FAIL +0/+0**. Frozen inputs and code generation passed; both generated Python files compiled. The first static semantic assertion failed because the generator replaced hyphenated `s0-s1` and uppercase `S0_S1` identities but omitted lowercase underscore schema identity `s0_s1`. No home/scientific computation ran and no generated artifact was admitted.

Minimal repair changed only the transformation identity substitution by adding `s0_s1 -> s0_s2`. No arithmetic, geometry, source index, checkpoint, public-BPW, storage, exactness or scientific criterion changed. Repair commit: `28c7afc1a83a5a5bf7019218eccc382abcdf0c3a`.

## Authoritative current process

- workflow: `Exp073FB Exp073FA S0_S2 driver transformation v0.1`;
- repaired run **`34018241319`**;
- job **`101445845648`**;
- head **`28c7afc1a83a5a5bf7019218eccc382abcdf0c3a`**;
- state at ledger update: **IN_PROGRESS** on GitHub-hosted runner;
- expected token `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`;
- expected artifact `exp073fb-exp073fa-s0-s2-generated-drivers-v0-1`;
- PASS classification support/governance `+0/+0`, never WW authority.

**Runner ownership:** no self-hosted DSIR job currently owns `DSIR-HOME-PC`; Exp073FB is hosted-only. No Exp073FA science checkpoint exists yet.

On repaired FB PASS: consume raw token and generated-driver artifact/digest; freeze exact generated driver identities plus dedicated fail-closed home envelope; hosted-audit that envelope; verify live zero competing home jobs; then launch exactly one Exp073FA A/B S0_S2 science run. On FB failure: diagnose the first causal defect and preserve the frozen FA science contract.

## Frozen global boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.