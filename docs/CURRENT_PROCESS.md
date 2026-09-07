# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0` Exp073EO, `S0_S1` Exp073EZ, `S0_S2` Exp073FF, `S0_S3` Exp073FN, and `S1_S1` Exp073FR.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-07_EXP073FS_ATTEMPT1_INFRA_ATTEMPT2_RUNNING.md`.

## Exp073FS attempt 1 — historical infrastructure failure +0/+0

Exp073FS run `34067352681`, attempt `1`, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458`:

- hosted job `101578350681`: SUCCESS support-only;
- home job `101578366531`: terminal failure at `2026-09-07T01:18:06Z` on runner `DSIR-HOME-PC` / runner id `21`;
- GitHub metadata left the frozen compute step marked `in_progress`; evidence collection/upload remained pending and provenance admission was skipped;
- old terminal job log is no longer retrievable after rerun (`BlobNotFound`), so no scientific/numerical exception is inferred;
- classification: `INFRASTRUCTURE_RUNNER_ORCHESTRATION_FAIL_PLUS_0_PLUS_0`;
- no scientific artifact/authority created; checkpoint contents were not inspected.

## Authoritative current process — Exp073FS attempt 2 / WW_S1_S2

The same workflow run is now attempt `2`; this is not a competing second heavy run.

- workflow/run: **Exp073FS `34067352681`**, attempt **`2`**;
- branch/head: `main` / **`f3e49041a5b869ddf22be8ca7a612901ec9f9458`**;
- current home job: **`101592579318`**;
- runner ownership: **`DSIR-HOME-PC-2` / runner id `22`, exclusively owned by job `101592579318`**;
- home job created `2026-09-07T01:18:30Z`, started `2026-09-07T01:31:27Z`;
- state at latest reconciliation: **IN_PROGRESS** in `Run frozen WW_S1_S2 A/B gate with durable checkpoints`;
- latest-attempt hosted-launch audit job `101592593435`: SUCCESS (same frozen audit evidence, support `+0/+0`);
- live DSIR Actions state: exactly **1 in-progress run, 0 queued runs**;
- checkpoint root/namespaces: `~/.cache/dsir/exp073fs-ww-s1-s2-filebacked-ab-v0-1/checkpoints/A` and `/B`;
- last durable checkpoint: `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`;
- science prereg blob: `80c6af017b47d51db3f588221749fb152577b0e5`;
- Exp073FT admission prereg blob: `072bdeae68e86312142e980fe2015f979e7b117f`;
- frozen source/contract: `de83e20a68f79ccf25b89b0d33eb4206e294c757` / `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- expected candidate token: `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Runner transition is provenance-relevant: attempt 1 used runner id `21`, attempt 2 uses runner id `22`. Do not assume shared local checkpoint availability merely from the common `$HOME/.cache/dsir/...` path. Terminal evidence must prove which complete stages were validly restored and which were newly computed.

Frozen pair semantics remain ordered `[1,2] = S1->S2`: reconstruct S1 and S2 once each, build two distinct spin-2 fields, forbid same-object handoff and reversed order; DES NSIDE=4096; ell `0..12287`; 39 bands; public file-backed BPW; full `[4,39,4,12288]`; canonical `<f8 [39,12288] EE<-EE`; exact A/B SHA + array equality; all finite; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

### Exact next actions

Do not duplicate attempt 2 and do not inspect partial numerical output. On terminal SUCCESS, consume raw terminal log and artifact immediately and independently verify artifact digest/ZIP SHA, both complete stage chains before prune, restored-versus-new stage provenance, ordered source/reconstruction counts, distinct field identities, source/contract/implementation/checkpoint identities, exact `19,327,352,832`-byte mmap proof, finiteness and exact canonical A/B equality. Candidate PASS does not itself create authority. Only prospectively frozen Exp073FT may create `WW_S1_S2` authority and dispatch Exp073FU.

On infrastructure/resource failure, diagnose the first causal defect from terminal evidence, preserve every verified complete-stage checkpoint, make the smallest prospective repair, and resume without changing frozen science. Exact numerical mismatch is a scientific FAIL and must never be tolerance-rescued.

The remaining deterministic queue remains `FS -> FT -> FU -> FV -> FW -> FX -> FY -> FZ -> GA -> GB -> STOP`; every successor is gated on explicit predecessor scientific authority.

## Independent DSIR-4 work while heavy compute runs

Newest repository work has prospectively frozen the source-bound C2 IDE six-component residual mapping (`docs/dsir4/mappings/C2_IDE_RESIDUAL_MAPPING_V0_1.md`, commit `440a643917d56ecb4227b3f6eab88da9092521cf`). This is mapping readiness only, not a DSIR model PASS; dedicated prediction provenance remains required before C2 becomes scientifically testable.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
