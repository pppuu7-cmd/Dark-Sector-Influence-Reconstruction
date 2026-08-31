# DSIR recovery checkpoint — Exp073CA Wm_S2 checkpoint-streaming Track-A active

**Date:** 2026-09-01 (Europe/Helsinki)  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Readiness remains:** `Verified 52.0% | Draft/data 53.7%` until a separately frozen terminal authority receipt exists.

## Why this branch was opened

The live recovery pointer after Exp073BZ required the next heavy gate to be a prospectively preregistered full-scale checkpoint-capable streaming Track-A execution/authority successor bound to immutable Exp073BV source lineage, Exp073BW exact streaming equivalence, and Exp073BZ remote checkpoint/failover durability.

Wm_S1 is already terminal Track-A authority PASS under Exp073BJ. The next missing Wm angular object selected prospectively is Wm_S2. Exp073BD remains provisional/incomplete and is forbidden as comparator or downstream authority.

## Frozen Exp073CA lineage

- scientific preregistration commit: `564a8d48f2af26d4394521f3fb55d51d80bcafe9`;
- checkpoint-safe range helper commit: `fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`;
- checkpoint streaming driver commit: `583c34420d5f02a1ac8e77efb9625bbc3ab73de8`;
- inherited exact BW helper commit: `9fb0ecb79986cf5f542760377533a685745b31e2`;
- attempt-2 infrastructure-fix preregistration: `2b8da936926e04bc4a6e9a8dc7db40930902c115`;
- attempt-2 workflow commit: `ed25a0ab3f444e989549548b958099a443dacfb3`;
- attempt-2 binding commit: `ba4d89988881e16b47f355d6608bc589945f77a9`;
- attempt-2 trigger/head: `ef288c2b73df299ec5107b30659bfcb51867b748`.

Frozen execution is two independent self-hosted replicas A/B, sequential at job level (`max-parallel: 1`), each using up to 8 OpenMP threads only across independent complete bands, with no within-band arithmetic reordering. Checkpoints are accepted only at complete-band boundaries and remotely persisted after chunks of at most four bands.

## Attempt 1 — permanent infrastructure record

Run `33446586747` completed failure before any scientific computation. Home job `99666949361` ran on `DSIR-HOME-PC`, passed checkout, then stopped in the pre-environment binding verifier because the bare `python` command is absent on that runner (`exit 127`). All PCL, helper compilation, exact preflight, checkpoint and heavy compact steps were skipped.

Frozen interpretation:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`

No scientific payload was produced and the attempt contributes `+0/+0`.

## Attempt 2 — active run

Run `33446800388` was triggered from head `ef288c2b73df299ec5107b30659bfcb51867b748` after the separately preregistered infrastructure-only change `python -> python3` in the early binding verifier.

Home replica-A job `99667607114` is assigned to runner `DSIR-HOME-PC`. At this checkpoint it has already passed:

1. job setup;
2. repository checkout;
3. prospective Exp073CA freeze and binding verification;
4. proven NaMaster 2.7 environment verification;
5. immutable R1 artifact download.

It is currently binding/downloading the exact DES Y1 lens mask before fresh Wm_S2 PCL construction. Replica B job `99667606808` is intentionally queued behind A.

No terminal scientific claim is made at this active checkpoint.

## Still frozen

- task `Wm_S2`, Wm signature `(0,2,0,2)`;
- DES `NSIDE=4096`, true ell `0..12287`, 39 frozen bands;
- canonical compact and selected-final shapes `<f8 [39,12288]`;
- exact BW-vs-range preflight is mandatory before full-scale bands;
- exact A/B compact equality and SHA equality are mandatory;
- exact finalizer A/B equality and SHA equality are mandatory;
- no tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue;
- Exp073AQ historical FAIL preserved;
- Exp073BD remains forbidden;
- no Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7 or G8 authorization from this active state.
