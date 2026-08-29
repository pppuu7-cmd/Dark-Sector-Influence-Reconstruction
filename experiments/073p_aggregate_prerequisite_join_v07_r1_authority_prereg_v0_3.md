# Exp073P aggregate prerequisite join — v0.7 R1 authority preregistration v0.3

**Frozen:** 2026-08-29 10:15 UTC, while Exp073R1 v0.7 run
`33240490287`, attempt `2`, job `99080934021` was still `queued` and its
Actions artifact list was empty.  No terminal mapper result, acquisition
provenance, selected-row count, record/mask hash or downstream science value
was available or inspected.

## Scope and supersession rule

This contract prospectively binds a new aggregate prerequisite join only to
the already-running v0.7 transport-stabilized Exp073R1 candidate.  It changes
no physical-support coordinate, threshold, dataset, selection, mapper,
semantic validator, classification boundary or downstream gate order.

Aggregate joins v0.1 and v0.2 are immutable historical records.  They remain
permanently bound to their failed v0.6 R1 authorities and may not be repointed
post hoc.  Implementation must use new v0.3 files.

## Sole admitted R1 execution authority

Aggregate join v0.3 may admit only:

- repository `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`;
- run `33240490287`, run attempt `2`;
- job `99080934021`, name `transport-stabilized-replay`;
- head/trigger commit `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- workflow path
  `.github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml`;
- workflow name
  `Exp073R1 DESY1 transport-stabilized exact-byte replay v0.7`;
- artifact name
  `exp073r1-v07-transport-stabilized-9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- workflow Git blob `99ce26540f15620c9c6a7acd9198b9d5fe81ecb6`;
- workflow SHA256
  `8ef3fb2305fe2789e6198547f5095969cfc107df1f0e17853b20a7aa5c601328`;
- unchanged evaluator Git blob
  `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- unchanged evaluator SHA256
  `5d4fcd8eebe0ae3a45b173a9f5ad261f014586ec81c5587e8720f3290254483e`;
- acquisition helper commit
  `50ce6d2f430dbbeff973358f75348adbb768885a`;
- workflow commit `17aea62e7addb6d5c12326afaeab7a2065b58585`;
- transport preregistration commit
  `401b6bc6f28fcef369d83dd0bc893bb35f9c722e`.

Attempt 1/job `99068879596` lost its self-hosted runner during acquisition and
produced no artifact.  It is infrastructure evidence only and is not admitted
by v0.3.  Any later run attempt, replacement job, new head, new workflow blob
or differently named artifact is also outside this authority.  If a later
attempt creates a second same-name artifact, the exact-one-artifact rule must
reject the route rather than choose one post hoc.

## Required Actions and artifact identity

The real collector must fetch live GitHub Actions metadata with complete
pagination and require all of the following:

- the frozen run is `completed/success`, has `run_attempt=2`, the exact
  head/workflow path/name above, and no identity drift;
- exactly one job exists in the frozen job registry and job `99080934021` is
  `completed/success` with the exact name above;
- exactly one non-expired artifact with the frozen name belongs to the frozen
  run across all attempts;
- the caller supplies that artifact's numeric ID and server digest, and both
  agree exactly with independently collected metadata;
- no v0.6 artifact, attempt-1 job, later-attempt job, duplicate artifact,
  expired artifact or partial diagnostic upload is selected.

Actions `success` or an upload by itself is insufficient.  Missing,
interrupted, unsuccessful, duplicate, expired, mismatched or incomplete
evidence must fail closed.

## Required complete v0.7 payload

The unique admitted artifact must contain exactly one nonempty copy of each
terminal control file:

- `exp073r1_desy1_transport_stabilized_replay_v0_7_summary.json`;
- `exp073r1_v0_7_remote_acquisition_provenance.json`;
- `exp073r1_v0_7_runtime_provenance.txt`;
- four nonempty pixel-record files, one for each source bin `0..3`;
- four nonempty bit-packed mask files, one for each source bin `0..3`.

The payload normalizer must reject duplicate basenames, missing bins, extra
bin identities, empty files and any record/mask whose bytes or SHA256 do not
match the terminal summary.  Partial products from `if: always()` upload are
not R1 authority.

## Acquisition-provenance interlock

The new v0.3 semantic wrapper must additionally require the exact v0.7
acquisition contract:

- route `v0.7_transport_stabilized_exact_byte_replay` and the authoritative
  DES Y1 metacal URL;
- `http_range_requests=0`, `whole_object_attempts_from_zero=true` and one or
  more recorded attempts;
- every attempt starts at byte zero, sends no Range header and never reports a
  `Content-Range` response;
- every nonterminal attempt is classified only as
  `INFRASTRUCTURE_TRANSPORT_FAILURE`;
- the last attempt has HTTP 200, outcome `PASS_EXACT_OBJECT_IDENTITY`, exact
  byte count `84,075,649,920` and SHA256
  `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- `authorized_for_replay=true`, terminal status
  `PASS_EXACT_OBJECT_IDENTITY_FOR_REPLAY`, and final bytes/hash agree with the
  last attempt and the R1 terminal summary;
- no identity-failed complete object is accepted;
- no science gate, `f_invalid`, covariance or G8 quantity was evaluated, and
  `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

## Unchanged R1 semantic and parent interlocks

The v0.3 evaluator must byte-freeze and privately reuse the v0.1 aggregate
validator:

- `ci/exp073p_aggregate_prerequisite_join_v0_1.py`, SHA256
  `9dc0b5a0ea82b8fb69d82e06b566b08d61c1982bd5e13ecd8db6752253bc0e46`;
- `ci/exp073p_actions_metadata_bundle_v0_1.py`, SHA256
  `cda5cb20c2d4f9be8a3068dacfead4db25e5dfbd867815005b754ab8cde955f3`.

Only the exact R1 execution registry and the additional attempt/acquisition/
payload-completeness interlocks may be added.  The existing validator must
still require the internal status
`PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`, exact source identity,
84,075,649,920 metacal bytes and frozen SHA256, `136930995` source/metacal
rows, exact selection, all four nonempty bins, finite coordinates,
`nside=4096` RING celestial-C `lonlat=True`, zero out-of-range pixels, all
independent mask-repeatability checks, every Exp073R0 parent check and all
nine unchanged non-R1 parents.

No partial pixel record, mask or acquisition log is authority.  No support,
covariance, whitening, nuisance, relation/null, held-out or G8 value may be
read to classify this prerequisite.

## Receipt taxonomy and synthetic firewall

The only real v0.3 receipt states are:

- `PASS_EXP073P_PREREQUISITE_BINDING_V0_3`;
- `REJECTED_EXP073P_PREREQUISITE_BINDING_V0_3`;
- `INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_3`.

Only a genuine real v0.3 PASS may set `support_executor_authorized=true`, and
it authorizes only the separately frozen physical-support executor.  Synthetic
self-tests must use a distinct synthetic PASS label, mutate run attempt,
attempt-1/later job, artifact multiplicity and all acquisition/payload
interlocks, and always retain `support_executor_authorized=false`.

## Frozen scientific firewall

No implementation or result may change post hoc:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- positive absolute final-response support envelope while production Wm stays
  signed;
- invalid radial tails outside the rectangle;
- no crop-before-normalization, effective ell, fiducial-P/model weighting or
  post-hoc cuts;
- order: prerequisite join -> physical support -> covariance/whitening ->
  nuisance SVD/rank -> quotient/relation/null -> fresh G8 withheld family.

At freeze time `support_executor_authorized=false`; G7, G8 and G9 are OPEN.
