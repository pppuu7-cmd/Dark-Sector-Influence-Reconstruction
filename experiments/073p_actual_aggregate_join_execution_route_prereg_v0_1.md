# Exp073P actual aggregate-prerequisite join execution route — preregistration v0.1

**Frozen:** 2026-08-29 (EEST), before implementation of the production route and
before any terminal output from canonical Exp073R1 v0.6 run `33212521957`.

## Purpose and scientific boundary

This experiment freezes the GitHub Actions route that will collect the real
Actions metadata and immutable prerequisite records required by the already
preregistered evaluator
`ci/exp073p_aggregate_prerequisite_join_v0_1.py`.

The route is an execution/provenance gate only.  It may emit the existing
prerequisite status

`PASS_EXP073P_PREREQUISITE_BINDING_V0_1`

only by running that unchanged evaluator on real evidence.  This is not a
physical-support classification.  It must not build support rows, compute
`f_invalid`, count retained coordinates, read covariance or nuisance data, or
inspect relation/null, held-out, G8 or G9 quantities.

At freeze time:

- R1 run `33212521957`, job `98988824629`, is `queued`;
- the required R1 artifact does not exist;
- no R1 terminal summary, mask hash, artifact ID or artifact digest has been
  inspected;
- `support_executor_authorized=false`;
- G7, G8 and G9 are OPEN.

## Sole admitted R1 authority

The route must remain bound to:

- repository `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`;
- run `33212521957`;
- job `98988824629`, `metacal-map-longrun`;
- head `79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`;
- workflow path
  `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`;
- workflow name `Exp073R1 DESY1 self-hosted long-run Stage-B v0.6`;
- artifact name
  `exp073r1-v06-selfhosted-longrun-79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`.

The future artifact ID and `sha256:` digest are unknown at freeze time.  A
production dispatch must supply both values after the run is terminal.  The
collector must independently retrieve the live run, job and artifact metadata
from the GitHub API and require the supplied ID/digest to match the unique,
non-expired artifact.  A supplied value is never authority by itself.

If R1 is incomplete, cancelled, unsuccessful, duplicated, expired, renamed, or
fails its internal interlock, the route must fail closed.  No other R1 run or
partial mask may be substituted under v0.1.

## Frozen production architecture

The implementation must add one manually dispatched production workflow and a
separate synthetic route self-test.  The production workflow must have no
`push`, `schedule` or automatic downstream trigger.

The production workflow must:

1. run on a GitHub-hosted Linux runner with only `contents: read` and
   `actions: read` permissions;
2. require explicit `r1_artifact_id` and `r1_artifact_digest` dispatch inputs;
3. verify unchanged hashes of this preregistration, the existing aggregate
   evaluator and the new metadata collector before reading live evidence;
4. retrieve in the same run the Actions run/job/artifact metadata for all ten
   parents frozen in
   `experiments/073p_aggregate_prerequisite_join_evaluator_prereg_v0_1.md`;
5. reject incomplete pagination, missing jobs, duplicate artifacts and any
   identity drift;
6. download only the exact large-source, large-metacal, P2 and canonical R1
   artifacts by their frozen run/name bindings;
7. use the exact committed preflight, S0 key-metrics and BOSS key-metrics files,
   whose byte hashes are already frozen by the aggregate evaluator;
8. invoke the existing evaluator with explicit `--classifying`; this flag
   classifies only the prerequisite join, not Exp073P physical support;
9. write and upload a receipt even when evidence is incomplete or rejected,
   whenever the evaluator can run;
10. leave a non-PASS workflow conclusion for `INCOMPLETE` or `REJECTED` and
    succeed only for the genuine real prerequisite PASS.

Downloading an artifact is not evidence of its admissibility.  The collector
and aggregate evaluator must re-bind live metadata, record bytes and semantic
fields independently.

## Metadata bundle schema

The collector output must use schema

`dsir.exp073p.aggregate-prerequisite-metadata.v0.1`

and repository

`pppuu7-cmd/Dark-Sector-Influence-Reconstruction`.

It must contain exactly the ten parent keys already frozen by the aggregate
evaluator.  Each parent must include:

- run ID, head SHA, workflow path/name, status and conclusion;
- the required job IDs, names, statuses and conclusions;
- artifact ID, name, digest, expiry flag and workflow-run binding for every
  required artifact.

The collector must request enough API rows for every job/artifact list and
fail if `total_count` exceeds the returned list.  It must not silently accept a
truncated first page.

## Fail-closed taxonomy

The production receipt taxonomy remains unchanged:

- genuine complete binding: `PASS_EXP073P_PREREQUISITE_BINDING_V0_1`;
- deterministic identity/schema/semantic mismatch:
  `REJECTED_EXP073P_PREREQUISITE_BINDING_V0_1`;
- missing, expired, queued, interrupted or otherwise unavailable evidence:
  `INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_1`.

The synthetic route self-test must use a distinct label and must always retain
`support_executor_authorized=false`.  It may not emit the real PASS label.

## Mandatory receipt firewall

Every real or synthetic output must state:

- `scientific_classification=null`;
- `support_fraction_evaluated=false`;
- `f_invalid_computed=false`;
- `retained_dimension_evaluated=false`;
- `covariance_read=false`;
- `whitening_read=false`;
- `nuisance_svd_read=false`;
- `relation_null_read=false`;
- `heldout_read=false`;
- `G8_read=false`;
- `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

Only a genuine real prerequisite PASS may set
`support_executor_authorized=true`, and that authorizes only the separately
preregistered physical-support executor.  Covariance remains closed.

## Frozen downstream criteria — unchanged

This route does not modify:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- positive absolute final-response support envelope;
- signed production Wm response;
- invalid radial tails outside the frozen rectangle;
- the prohibition on crop-before-normalization, effective ell,
  fiducial-P/model weighting and post-hoc cuts;
- the order physical support -> covariance/whitening -> nuisance SVD/rank ->
  quotient/relation/null -> fresh G8 withheld family.

## Permitted pre-output validation

Before R1 terminates, implementation may be compiled and exercised only on
fabricated API responses and synthetic records.  The mutation suite must cover
at least run/head/path/name drift, missing or unsuccessful required jobs,
missing/duplicate/expired artifacts, R1 artifact ID/digest mismatch and
truncated API pagination.  Such validation is infrastructure evidence only.
