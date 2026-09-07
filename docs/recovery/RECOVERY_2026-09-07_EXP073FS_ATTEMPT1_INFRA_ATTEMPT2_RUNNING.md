# DSIR recovery — Exp073FS attempt 1 infrastructure failure; attempt 2 running

Date: 2026-09-07. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved authority

All previously admitted authority is unchanged. In particular, `WW_S1_S1` remains admitted by canonical Exp073FR run/job `34067345251 / 101578330386`. No result in this note changes any frozen science criterion.

## Exp073FS attempt 1 — infrastructure failure +0/+0

Workflow/run: Exp073FS `34067352681`, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458`, attempt `1`.

- hosted-launch-audit job `101578350681`: SUCCESS;
- home-science job `101578366531`: terminal `failure` at `2026-09-07T01:18:06Z`;
- runner: `DSIR-HOME-PC`, runner id `21`;
- GitHub job metadata left step `Run frozen WW_S1_S2 A/B gate with durable checkpoints` marked `in_progress` at job termination; the `always()` evidence collection and artifact-upload steps remained pending and the provenance-admission job was skipped;
- no terminal scientific artifact was created by attempt 1;
- a post-rerun request for the old job log returned GitHub `BlobNotFound`, so no shell-level scientific/numerical exception is available for retrospective interpretation.

Classification: **INFRASTRUCTURE_RUNNER_ORCHESTRATION_FAIL_PLUS_0_PLUS_0**. The first observable causal boundary is abrupt termination/loss of the self-hosted job while the frozen compute step was still executing, before GitHub recorded a step-level completion and before evidence collection. This is not a scientific FAIL and must not be interpreted from any partial checkpoint.

Durable checkpoint state from attempt 1 is intentionally **UNKNOWN_NOT_INSPECTED**. Because the run failed before evidence collection, no claim is made that a particular complete stage survived or was restored.

## Exp073FS attempt 2 — authoritative current process

The same workflow run is now attempt `2`; no separate competing heavy run exists.

- run: `34067352681`, run attempt `2`;
- current home job: **`101592579318`**;
- current runner: **`DSIR-HOME-PC-2`**, runner id `22`;
- created `2026-09-07T01:18:30Z`, started `2026-09-07T01:31:27Z`;
- current state at reconciliation: `IN_PROGRESS` in the frozen `Run frozen WW_S1_S2 A/B gate with durable checkpoints` step;
- hosted launch audit is SUCCESS and remains support `+0/+0`;
- queued DSIR runs: `0`; in-progress DSIR runs: exactly `1`;
- checkpoint root remains `~/.cache/dsir/exp073fs-ww-s1-s2-filebacked-ab-v0-1/checkpoints/{A,B}`;
- partial numerical output/checkpoint contents were not inspected.

Runner-name transition is recorded explicitly. `DSIR-HOME-PC-2` is a different GitHub runner id from attempt 1. Until terminal evidence proves a valid restore chain, repository authority must not assume that attempt-1 local checkpoints were available to attempt 2. Terminal consumption must record which stages were restored versus newly computed and verify every restored payload/hash fail-closed.

## Frozen science remains unchanged

Target ordered pair `[1,2] = S1->S2`; one S1 and one S2 reconstruction; two distinct spin-2 field objects; reversed order and same-object handoff forbidden; DES NSIDE=4096; ell `0..12287`; 39 bands; public file-backed BPW; canonical `<f8 [39,12288] EE<-EE`; exact `19,327,352,832`-byte MCM backing; all finite; exact A/B SHA and `numpy.array_equal`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

Expected candidate token remains `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate PASS creates no authority; only prospectively frozen Exp073FT may admit `WW_S1_S2` and dispatch Exp073FU.

## Exact next action

Do not duplicate attempt 2. On terminal completion, consume the raw terminal evidence/artifact before any scientific classification. Verify artifact digest/independent ZIP SHA, both complete stage chains, restored-versus-new stage provenance, ordered reconstruction counts and distinct field identities, frozen source/contract/implementation/checkpoint identities, exact mmap proof, finiteness and exact A/B equality. If terminal evidence shows invalid/missing restore provenance, classify infrastructure/provenance failure rather than rescuing the science.
