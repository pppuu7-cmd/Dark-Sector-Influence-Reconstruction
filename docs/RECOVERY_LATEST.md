# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-29 15:14 UTC

**Stable historical manual:** `docs/RECOVERY_MANUAL.md`

**Current detailed checkpoint:**
`recovery/2026-08-29_exp073r1_v07_attempt2_runner_assignment_audit.md`

**Active execution:** Exp073R1 v0.7 run `33240490287`, attempt 2, job
`99080934021` (`queued` and unassigned at `2026-08-29T15:14:27Z`; no
artifacts)

**Recovered main:** `fcd771a286301d811ec4f4dd9aa759df746d5371`

**Merged production route:** PR #166 merged to main as `e3eaa47`; main push
self-test `33258423809` completed successfully.

**Production-route byte freeze:** main `fcd771a`; hosted guard run
`33259873639`, job `99119863197`, completed successfully.

DSIR remains independent of RTK.  Preserve all negative and infrastructure
results, preregistration chronology, missing-domain masks, and the distinction
between reproduction, prerequisite and scientific classifications.

## Current frontier

The G7 chain remains blocked immediately before the real Exp073P
physical-support evaluation:

`validated physical providers -> genuine R1 reproduction -> aggregate prerequisite join -> physical support -> covariance/whitening -> nuisance SVD/rank -> quotient/relation/null -> fresh G8`

Current state:

- C3 physical provider: certified;
- C5 physical provider: certified with corrected raw-k provenance;
- BOSS finite mm component: frozen `54/240`, `27/120` per cap, `9/40` in each
  P0/P2/P4 block;
- DES public-input, large-object, P2 and S0 parents: immutable and
  validator-compatible;
- Exp073R0 raw-row/HEALPix equivalence: PASS;
- original v0.6 run `33212521957`: `INCOMPLETE_EXP073R1` at the PEP 668
  runtime boundary, before data;
- replacement v0.6 run `33222848695`, attempts 1 and 2: terminal repeated
  remote whole-object EOF infrastructure failures, no admissible R1 result;
- v0.7 transport-stabilized run `33240490287`, attempt 1: terminal runner loss
  during acquisition, no artifact;
- v0.7 exact rerun attempt 2/job `99080934021`: queued with `runner_id=0`
  and no runner name, sole heavy candidate;
- Exp073P aggregate join v0.1 and v0.2: immutable and permanently fail-closed
  for their frozen failed R1 authorities;
- Exp073P aggregate join v0.3: canonical main preregistration and production
  route are merged, with authority, live-metadata, archive and cross-member
  guards; the real route has not run because no admissible R1 evidence exists;
- Exp073P physical support and every later stage: BLOCKED;
- `support_executor_authorized=false`;
- G7/G8/G9: OPEN.

## R1 authority and classifications

### v0.6 runtime-boundary authority

Run `33212521957`, job `98988824629`, head
`79abf2a9694e57e7a2ba1fbb563a0f6413e891f9` passed evaluator and parent
metadata checks, then failed on pip's PEP 668 guard before download.  Zero
metacal rows were read and no artifact exists.  It is infrastructure
`INCOMPLETE_EXP073R1`, not scientific FAIL.

### v0.6 direct-stream replacement

Run `33222848695`, head
`98c4b8783a95932949947d9e214706c4ec7eaf8c`, workflow blob
`2cdcb0c60f464c0c65c3bafdde23daec7732215e`, unchanged evaluator blob
`46fe1271d97ddd9e2164d24e7d79cf27bfda805d`:

- attempt 1/job `99020389131`: mapper EOF after the last reported
  `37,748,736` rows; partial artifact `9709998972`, digest
  `sha256:d770bbfdda55788661b2676d4768e1da38d2e7310cbf96d2bfe52f41a3616351`;
- attempt 2/job `99062223326`: mapper EOF in the first row chunk; empty-record
  artifact `9710626213`, digest
  `sha256:453259db5d09c6f65c15d470216ab1b6cd631f0018cc63e3f8199f35428b4a9a`.

Both artifacts use the same canonical name, contain no terminal summary or
masks, and are inadmissible.  The two same-name artifact IDs are preserved as
infrastructure evidence; no partial map statistic may be used.

Classification:
`INFRASTRUCTURE_TRANSPORT_FAILURE_REMOTE_WHOLE_OBJECT_EOF_REPEATED`.

### Active v0.7 transport-stabilized route

- preregistration: `401b6bc6f28fcef369d83dd0bc893bb35f9c722e`;
- acquisition helper: `50ce6d2f430dbbeff973358f75348adbb768885a`;
- workflow: `17aea62e7addb6d5c12326afaeab7a2065b58585`;
- trigger/head: `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- run `33240490287`;
- attempt 1/job `99068879596`: runner loss while acquisition step was reported
  in progress, no cleanup/upload artifact;
- exact rerun attempt 2/job `99080934021`: still queued and unassigned at
  `2026-08-29T15:14:27Z`; `runner_id=0`, runner name/group are empty, and the
  run artifact list is empty.

v0.7 changes transport staging only: each remote attempt restarts a no-Range
whole-object GET from byte zero; exact size `84075649920` and SHA256
`39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`
are required before loopback replay to the unchanged evaluator.  The queued
job is the only authorized heavy candidate.  Do not dispatch a duplicate.

### Attempt-2 runner-assignment diagnosis

Attempt 1 of this exact run used the same `[self-hosted, linux]` labels and was
assigned to runner `DSIR-HOME-PC` (runner ID `21`, group `Default`).  Attempt 2
has identical authority and labels but no assigned runner.  Thus the label
contract is compatible; the current infrastructure blocker is an unassigned
self-hosted runner, classified
`BLOCKED_EXP073R1_SELF_HOSTED_RUNNER_UNASSIGNED`.

The public job response cannot distinguish offline from busy or a transient
Actions service failure.  Start or restart the existing listener with
`cd ~/actions-runner-dsir && ./run.sh`; do not reconfigure it, change workflow
labels, cancel the queued attempt or dispatch a duplicate.

## Artifact-delivery firewall observation

The frozen active v0.7 workflow blob
`99ce26540f15620c9c6a7acd9198b9d5fe81ecb6` has one `always()` artifact upload
named only by `github.sha`; it mixes diagnostics and possible complete results
and lacks run-attempt identity.  This has not materialized in the active run
because attempt 1 produced no artifact and attempt 2 is not terminal.  The
active snapshot is not modified.

Before any later new execution after a failed v0.7 artifact upload, freeze a
delivery-only repair with distinct result/diagnostic names containing run ID
and attempt, strict files, and terminal-PASS gating.  This observation does not
authorize another heavy run or any scientific stage.

The hosted synthetic audit self-test, run `33245678070`, completed with
`success`; it reproduced the committed audit and its no-leakage assertions.

Before any attempt-2 output existed, main commit `e58bddf` froze the canonical
Exp073P v0.3 authority for the exact run attempt/job/branch/event/workflow.
Its preregistration SHA256 is
`e27761b2db4a81283bb9fbac1decb95f62fadb785c40cb3e3f676f8651711f40`.
Main then added independently hosted authority, live-metadata-set and
archive-member guards through `72c0278`.  PR #166 has been reconciled with
those canonical bytes and extends them into the actual route with exact raw-ZIP
ID/digest download and full 11-member archive validation.  The earlier
PR-branch preregistration commit `940fbca` remains historical but is not the
canonical byte authority.

## Exp073P aggregate-join state

Synthetic evaluator/route readiness remains PASS, including hosted v0.2
self-test run `33234248213`, job `99052307444`, artifact `9709418334`, digest
`sha256:84a6a8c2740ad539c6a48a59e47b876122f6fd5bf4b5665e9653ecfc7c1debfc`.

Real joins remain closed:

- v0.1 is frozen to the original PEP-668-failed R1 authority;
- v0.2 is frozen to run `33222848695`, job `99020389131`, which failed;
- v0.2 also requires exactly one canonical-name R1 artifact, while that run
  now has two same-name inadmissible artifacts;
- neither route may be repointed to attempt 2 or v0.7;
- v0.3 is frozen only to run `33240490287`, attempt `2`, job `99080934021` and
  the exact v0.7 artifact name; any later attempt/job or duplicate same-name
  artifact fails closed;
- v0.3 requires the unique artifact ID/digest, job/run success, full-from-zero
  acquisition provenance and the complete summary/runtime/acquisition plus four
  records and four masks with byte/hash cross-binding;
- the integrated production route downloads the raw artifact ZIP by numeric ID,
  verifies its server-recorded digest before extraction, requires the exact
  11-member archive set, and never forwards the GitHub bearer token to the
  signed redirect;
- hosted v0.3 self-test run `33248034308`, job `99088793819`, succeeded;
  artifact `9713466820` has digest
  `sha256:d53b87eec234c3533fd9d167bfdae7433db27e4aa106a614c2dd5812a9f6019e`;
- synthetic v0.3 PASS retains `support_executor_authorized=false`; the manual
  real workflow has not run and must not be dispatched until exact admissible
  R1 evidence exists.
- current-main supplemental hosted guards also passed: authority run
  `33250019007`, metadata-set run `33252122146`, and archive-member run
  `33254539043`; these are implementation-validation PASS results only;
- cross-member consistency guard run `33257187305` also passed 19 negative
  mutations and is preserved from current main `f2d1043`;
- current-main-integrated hosted self-test run `33257888770`, job
  `99114673638`, succeeded; artifact `9716362579` has digest
  `sha256:f78ed9f12c54bd585c9f5b8022e8fcb468dee7583e842c0c76363af2dfde7b33`.
- merged-main push self-test run `33258423809`, job `99116067842`, succeeded;
  artifact `9716520508` has digest
  `sha256:e9ff6bfbbe33b092dde5b19493dba00e1fce89fa4e0fd0069a89b3ac8a875907`.
- additive production-route byte-freeze guard run `33259873639`, job
  `99119863197`, succeeded; it freezes the actual v0.3 workflow blob
  `2950750312c153f75fe79c2c16fca6f74c7df5dc` and the canonical preregistration
  without modifying either file or authorizing support.

## Frozen scientific boundaries

Never modify post hoc:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- support uses the positive absolute final-response envelope;
- production Wm remains signed;
- all radial tails outside the rectangle remain invalid;
- no crop-before-normalization, effective ell, fiducial-P/model weighting or
  post-hoc cuts;
- no covariance, nuisance SVD/rank, quotient/relation/null, held-out or G8
  leakage into support selection.

## Exact next actions

1. Keep run `33240490287`, attempt 2/job `99080934021`, as the sole heavy R1
   candidate.  Start or restart the already registered listener with
   `cd ~/actions-runner-dsir && ./run.sh`, keep it alive, and do not duplicate.
2. If it starts, retain the frozen no-Range, full-from-zero, exact-size/SHA and
   unchanged-evaluator route.
3. On termination, record exact attempt/job/step boundary, acquisition
   provenance, runtime, artifact ID/digest and internal assertion.  A transport
   or runner failure is infrastructure only.
4. Require genuine internal
   `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`; Actions success or an
   upload alone is insufficient.
5. Use only canonical v0.3 for this exact attempt.  Verify the preregistration
   SHA256 `e27761...1711f40`, merged main commit `e3eaa47`, and main push run
   `33258423809`, then require the production-route byte-freeze guard from
   main `fcd771a` / hosted run `33259873639`.  PR #166 is merged; do not
   dispatch the manual real route until R1 supplies admissible evidence.
   Never repoint or run v0.1/v0.2.
6. If attempt/job/head/artifact multiplicity differs, reject v0.3 and freeze a
   new version before another candidate.  Never edit v0.3 post hoc.
7. Require aggregate prerequisite PASS, then physical-support PASS, before
   covariance/whitening.
8. Preserve downstream order: nuisance SVD/rank -> quotient/relation/null ->
   fresh G8.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_LATEST.md`
3. `recovery/2026-08-29_exp073r1_v07_attempt2_runner_assignment_audit.md`
4. `recovery/2026-08-29_exp073p_v03_production_route_main_guard_integration.md`
5. `experiments/073p_aggregate_prerequisite_join_v07_r1_authority_prereg_v0_3.md`
6. `recovery/2026-08-29_exp073p_v03_production_route_byte_freeze_guard.md`
7. `ci/exp073p_v03_production_route_byte_freeze_v0_1.py`
8. `ci/exp073r1_v0_7_runner_assignment_audit.py`
9. `data/derived/g7/exp073r1_v07_runner_assignment_snapshot_v0_1.json`
10. `data/derived/g7/exp073r1_v07_runner_assignment_audit_v0_1.json`
11. `recovery/2026-08-29_exp073p_v03_v07_authority_prereg_and_attempt_aware_selftest.md`
12. `recovery/2026-08-29_exp073p_v03_live_metadata_set_guard_and_r1_v07_queue_checkpoint.md`
13. `recovery/2026-08-29_exp073p_v03_archive_member_guard_pass_and_r1_v07_queue_checkpoint.md`
14. `recovery/2026-08-29_exp073p_v03_cross_member_consistency_guard_pass_r1_v07_queued.md`
15. `ci/exp073p_aggregate_prerequisite_join_v0_3.py`
16. `ci/exp073p_actions_metadata_bundle_v0_3.py`
17. `ci/exp073p_v03_artifact_zip_download_v0_1.py`
18. `ci/exp073p_v07_r1_payload_bundle_v0_3.py`
19. `ci/exp073p_v03_cross_member_consistency_failclosed_selftest.py`
20. `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml`
21. `recovery/2026-08-29_exp073p_v03_v07_attempt2_authority_ready.md`
22. `recovery/2026-08-29_exp073r1_v07_attempt2_queued_artifact_delivery_firewall.md`
23. `recovery/2026-08-29_exp073r1_v07_runner_loss_attempt1_exact_rerun_attempt2.md`
24. `recovery/2026-08-29_exp073r1_v07_live_acquisition_firewall_audit.md`
25. `experiments/073r1_v0_7_transport_stabilized_exact_byte_replay_prereg.md`
26. `ci/exp073r1_v0_7_whole_object_acquire.py`
27. `.github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml`
28. `data/derived/g7/exp073r1_v06_repeated_remote_eof_artifact_audit_v0_1.json`
29. `ci/exp073r1_v0_7_artifact_delivery_audit.py`
30. `data/derived/g7/exp073r1_v07_artifact_delivery_risk_audit_v0_1.json`
31. `experiments/073p_aggregate_prerequisite_join_superseding_r1_authority_prereg_v0_2.md`
32. `recovery/2026-08-28_exp073r1_to_exp073p_execution_integrity_matrix.md`
33. `experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`
