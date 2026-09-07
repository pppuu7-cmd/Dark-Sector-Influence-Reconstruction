# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities now include `S0_S0` Exp073EO, `S0_S1` Exp073EZ, `S0_S2` Exp073FF, `S0_S3` Exp073FN, and newly admitted **`S1_S1` Exp073FR**.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-07_EXP073FM_FR_ADMITTED_FS_RUNNING.md`.

## Newly closed — Exp073FM candidate and Exp073FR authority

Exp073FM run/job **`34050657030 / 101533574294`**, head `f0caca0c3e812710e5958ee13348a150d045a7d8`, is terminal SUCCESS and was independently consumed against the frozen contract.

- candidate token: `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- artifact `9998932628`, `exp073fm-ww-s1-s1-filebacked-ab-v0-1`, size `7380196`;
- ZIP SHA256 `db3aa00e060047f354c5374c78dba3808491cf61a1d810114d35b474badd49af`;
- selected A/B SHA256 `ff7215d5e523134e10ef4c9b512c6829d66fd63af33dc5655bd8e88dfd0c33ff`;
- canonical A/B `<f8 [39,12288]`, all finite, exact byte equality and `numpy.array_equal=true`;
- both complete six-stage/prune chains and exact `19,327,352,832`-byte file-backed MCM proof verified;
- frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757` and contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251` preserved.

Terminal consumer run/job `34065976761 / 101578311604` emitted `PASS_EXP073FM_TERMINAL_EVIDENCE_CONSUMED_FOR_CANONICAL_FR_V0_1`, classification `SUPPORT_TERMINAL_EVIDENCE_CONSUMED_PLUS_0_PLUS_0`, and created no authority.

Canonical Exp073FR run/job **`34067345251 / 101578330386`**, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458`, independently reverified the frozen terminal evidence and emitted:

`PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`

with `classification=SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s1_s1_authority_created=true`. Therefore **WW_S1_S1 is formally admitted**.

## Authoritative current process — Exp073FS WW_S1_S2

Exp073FR dispatched the already prospectively frozen successor. Live Actions reconciliation shows exactly one in-progress DSIR workflow; do not duplicate it.

- workflow/run: **Exp073FS `34067352681`**;
- hosted launch job: `101578350681`, SUCCESS, token `PASS_EXP073FS_HOSTED_LAUNCH_AUDIT_V0_1`, support `+0/+0`;
- home job: **`101578366531`**;
- branch/head: `main` / **`f3e49041a5b869ddf22be8ca7a612901ec9f9458`**;
- start: `2026-09-06T23:36:14Z`;
- current state: **IN_PROGRESS** in `Run frozen WW_S1_S2 A/B gate with durable checkpoints`;
- runner ownership: **`DSIR-HOME-PC` exclusively owned by job `101578366531`**;
- checkpoint root/namespaces: `~/.cache/dsir/exp073fs-ww-s1-s2-filebacked-ab-v0-1/checkpoints/A` and `/B`;
- last durable checkpoint: `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`; partial numerical output must not be inspected;
- science prereg blob: `80c6af017b47d51db3f588221749fb152577b0e5`;
- Exp073FT admission prereg blob: `072bdeae68e86312142e980fe2015f979e7b117f`;
- frozen source/contract: `de83e20a68f79ccf25b89b0d33eb4206e294c757` / `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- expected candidate token: `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Frozen pair semantics are ordered `[1,2] = S1->S2`: reconstruct S1 and S2 once each, build two distinct spin-2 fields, forbid same-object handoff and reversed order; DES NSIDE=4096; ell `0..12287`; 39 bands; public file-backed BPW; full `[4,39,4,12288]`; canonical `<f8 [39,12288] EE<-EE`; exact A/B SHA + array equality; all finite; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

### Exact next actions

On terminal SUCCESS, consume raw job log and artifact immediately; independently verify artifact digest/ZIP SHA, both complete stage chains before prune, ordered source/reconstruction counts, distinct field identities, source/contract/implementation/checkpoint provenance, exact `19,327,352,832`-byte mmap proof, finiteness and exact canonical A/B equality. Candidate PASS does not itself create authority. Only the prospectively frozen Exp073FT admission may create `WW_S1_S2` authority and then dispatch Exp073FU.

On infrastructure/resource failure, diagnose the first causal defect, preserve every verified complete-stage checkpoint, make the smallest prospective repair, and resume without changing frozen science. Exact numerical mismatch is a scientific FAIL and must never be tolerance-rescued.

The remaining prospectively frozen deterministic queue remains `FS -> FT -> FU -> FV -> FW -> FX -> FY -> FZ -> GA -> GB -> STOP`; every heavy successor is gated on the predecessor's explicit scientific authority token. No competing home job is permitted.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
