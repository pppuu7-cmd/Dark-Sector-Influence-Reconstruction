# Exp073R1 v0.7 attempt 2 queued; artifact-delivery firewall audit

Date: 2026-08-29
Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`
Recovered `main` head at audit start: `3ebcd03bddfa9a790e2dc3b63b0f4e733d0d67d5`
Scope: DSIR only; no RTK content.

## Recovery correction after concurrent repository progress

The repository was fetched again before recording this iteration.  `main` had
advanced from `f96d863` through commits `401b6bc`..`3ebcd03`: an independently
preregistered transport-stabilized v0.7 route already existed, attempt 1 had
lost its self-hosted runner during acquisition, and one exact rerun had already
been requested.  Therefore no competing v0.7 workflow and no duplicate heavy
run is introduced by this checkpoint.

## v0.6 repeated remote EOF: terminal evidence

Replacement run `33222848695` retained the frozen evaluator blob
`46fe1271d97ddd9e2164d24e7d79cf27bfda805d` and identical runtime provenance
on both attempts (`cp314`, NumPy `2.5.2`, healpy `1.20.0`).  Both attempts
passed setup, immutable-parent binding, artifact download and internal parent
rebinding before failing inside the unchanged whole-object reader:

- attempt 1, job `99020389131`: last progress report `37,748,736` rows, then
  `EOFError: whole stream ended after 18479432 of requested 40239104 bytes`;
- attempt 2, job `99062223326`: EOF occurred in the first row chunk, before
  any chunk was processed, with
  `EOFError: whole stream ended after 10839192 of requested 40239104 bytes`.

Both outcomes are
`INFRASTRUCTURE_TRANSPORT_FAILURE_REMOTE_WHOLE_OBJECT_EOF_REPEATED`, not a
scientific FAIL.  Neither terminal reproduction assertion ran.

The two failure uploads have distinct IDs but the same artifact name:

- attempt 1: artifact `9709998972`, ZIP digest
  `sha256:d770bbfdda55788661b2676d4768e1da38d2e7310cbf96d2bfe52f41a3616351`,
  four partial records and no summary/masks;
- attempt 2: artifact `9710626213`, ZIP digest
  `sha256:453259db5d09c6f65c15d470216ab1b6cd631f0018cc63e3f8199f35428b4a9a`,
  four zero-byte records and no summary/masks.

Both ZIP digests were independently verified.  Attempt-2's four members all
have the empty-file SHA256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Neither artifact is admissible as an R1 result, and no map/support statistic
was derived from partial records.

This actual rerun behavior corrects a preterminal operational prediction:
despite a head-only artifact name and `overwrite: false`, GitHub Actions
preserved attempt 1 and created a second same-name artifact for attempt 2.
The observation is infrastructure provenance, not science.

## Exp073P v0.2 remains fail-closed

Aggregate join v0.2 is frozen to run `33222848695`, job `99020389131`.  That
job failed, and the byte-frozen metadata collector also requires exactly one
canonical-name artifact while the run now exposes two.  The real join is thus
fail-closed for two independent reasons.  It must not be dispatched or
repointed to attempt 2 or v0.7.  `support_executor_authorized=false`.

## Active v0.7 authority at this checkpoint

The current preregistered route is:

- preregistration commit `401b6bc6f28fcef369d83dd0bc893bb35f9c722e`;
- acquisition helper commit `50ce6d2f430dbbeff973358f75348adbb768885a`;
- workflow commit `17aea62e7addb6d5c12326afaeab7a2065b58585`;
- trigger/head commit `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- run `33240490287`;
- attempt 1 job `99068879596`: terminal infrastructure runner loss during
  acquisition, no artifact;
- attempt 2 job `99080934021`: `queued` at `2026-08-29T09:21:58Z`, no
  artifact.

The queued job is the sole heavy R1 candidate.  Do not dispatch another run.
Its current queue state is an infrastructure availability/capacity wait, not a
scientific outcome.

## Artifact-delivery audit of the frozen active snapshot

The active workflow blob is
`99ce26540f15620c9c6a7acd9198b9d5fe81ecb6` (SHA256
`8ef3fb2305fe2789e6198547f5095969cfc107df1f0e17853b20a7aa5c601328`).
Its scientific/acquisition firewall remains unchanged.  A separate static
audit identified a future retry-delivery risk:

- one `always()` upload mixes provenance, summary, records and masks;
- its name is `exp073r1-v07-transport-stabilized-${{ github.sha }}` and lacks
  `github.run_id` and `github.run_attempt`;
- missing files only warn;
- result and diagnostic evidence are not separated by artifact identity.

The risk has not materialized in run `33240490287` because attempt 1 produced
no artifact and attempt 2 is not terminal.  The active frozen run is not
modified.  Before any later *new* run after a failed v0.7 upload, a prospective
delivery-only contract must require distinct result/diagnostic names including
run ID and attempt, strict complete-result files, and a result upload gated on
the terminal reproduction assertion.  No such new run is authorized here.

Executable audit:
`ci/exp073r1_v0_7_artifact_delivery_audit.py`.
Machine records:

- `data/derived/g7/exp073r1_v06_repeated_remote_eof_artifact_audit_v0_1.json`;
- `data/derived/g7/exp073r1_v07_artifact_delivery_risk_audit_v0_1.json`.

## Scientific firewall

No frozen scientific threshold, boundary, selection, mapper or parent was
changed.  This iteration read no support fraction, `f_invalid`, retained
dimension, covariance, whitening, nuisance rank/SVD, quotient/relation/null,
held-out or G8 quantity.  G7/G8/G9 remain OPEN.

## Exact recovery procedure

1. Keep run `33240490287`, attempt 2/job `99080934021`, as the only heavy
   candidate and wait for a compatible self-hosted runner; do not duplicate.
2. On start, preserve the frozen acquisition route: full-from-zero whole GETs,
   no Range/resume, exact 84,075,649,920 bytes and exact frozen SHA256 before
   loopback replay.
3. On terminal failure, classify the reached boundary exactly and preserve
   diagnostic evidence; do not infer a scientific result.
4. On genuine terminal R1 PASS, freeze the exact run attempt, job, head,
   workflow blob, artifact ID/digest and internal receipt before downstream
   use.
5. Do not use Exp073P join v0.1/v0.2 for v0.7.  Prospectively freeze a new
   aggregate authority/collector before inspecting a v0.7 result artifact.
6. Require aggregate prerequisite PASS before physical support, then preserve
   the order: covariance/whitening -> nuisance SVD/rank ->
   quotient/relation/null -> fresh G8.
7. If a failed v0.7 attempt creates an artifact and another new run is needed,
   preregister and implement attempt-specific result/diagnostic delivery before
   that new execution.

## Verification performed

- public Actions job/artifact metadata independently re-read for v0.6 and
  v0.7;
- both v0.6 ZIP SHA256 digests and attempt-2 member hashes independently
  verified;
- static artifact-delivery audit PASS, including three sensitivity checks;
- hosted audit self-test run `33245678070`: `success`;
- committed-audit byte reproduction, both new JSON syntax checks, BaseLoader
  parsing of the active and self-test workflows, `compileall`, and
  `git diff --check`: PASS;
- complete repository suite: `44 passed`.
