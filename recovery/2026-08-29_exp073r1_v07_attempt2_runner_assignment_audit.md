# DSIR recovery checkpoint — Exp073R1 v0.7 attempt-2 runner assignment audit

**Date:** 2026-08-29  
**Live capture:** 2026-08-29T15:14:27Z  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Recovered main before the audit:**
`eddfa22142b5e519f7df00393d52762758eeb63f`  
**Scope:** DSIR infrastructure/provenance only; no RTK content.

After the live capture, `main` advanced independently to
`fcd771a286301d811ec4f4dd9aa759df746d5371`, adding a hosted production-route
byte-freeze guard.  That additive guard and its successful run `33259873639`
were incorporated unchanged before this audit branch was finalized.  It does
not duplicate or alter the runner-assignment result.

## Recovery result

Exp073R1 v0.7 run `33240490287`, attempt `2`, job `99080934021`
remained `queued`, `conclusion=null`, with no artifacts.  Public attempt-aware
job metadata adds a more precise diagnosis than the earlier generic
"compatible runner unavailable" statement:

- attempt 1/job `99068879596` used labels `[self-hosted, linux]` and was
  assigned to runner ID `21`, `DSIR-HOME-PC`, group `Default`;
- attempt 2 uses the identical labels for the identical run, workflow and
  head, but exposes `runner_id=0`, an empty runner name/group and no steps;
- therefore the recorded label contract is compatible with the configured
  DSIR runner, while attempt 2 was **unassigned** at capture time.

Classification:
`BLOCKED_EXP073R1_SELF_HOSTED_RUNNER_UNASSIGNED`.

This rules out a workflow-label mismatch for `DSIR-HOME-PC`.  It does not
distinguish whether the runner process is offline, the machine is asleep, the
runner is busy, or GitHub Actions has a transient assignment problem.  The
repository runner-inventory endpoint was not available through the public
read path, so the audit deliberately makes no stronger liveness claim.

## Evidence authority

The machine-readable source capture is
`data/derived/g7/exp073r1_v07_runner_assignment_snapshot_v0_1.json`, SHA256
`0d51868e9c29440d94fd5f8917ef42c172ddc84745e0b2a738e7ef943a5e78ac`.
It reduces the following public GitHub Actions responses without including a
credential:

1. run `33240490287`;
2. attempt-1 jobs collection;
3. attempt-2 jobs collection;
4. run-artifact collection.

Frozen identifiers checked by the executable audit:

- workflow ID `345172058`;
- workflow path
  `.github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml`;
- head `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- run `33240490287`;
- attempt-1 job `99068879596`;
- attempt-2 job `99080934021`;
- job name `transport-stabilized-replay`;
- required labels `[self-hosted, linux]`.

The captured attempt-1 job was terminal `failure`; its public step array still
showed the full-from-zero acquisition step as `in_progress` when the runner
was lost.  The terminal reproduction assertion did not start and no artifact
was uploaded.  That earlier result remains infrastructure runner loss, not a
scientific result.

## Executable fail-closed audit

`ci/exp073r1_v0_7_runner_assignment_audit.py` requires every identifier and
state above.  It emits
`data/derived/g7/exp073r1_v07_runner_assignment_audit_v0_1.json` only when:

- attempt 1 proves prior assignment of the exact label set to
  `DSIR-HOME-PC`/`Default`;
- attempt 2 is still queued and unassigned;
- the run head/workflow/attempt/job authority is exact;
- the artifact set is empty.

Seven sensitivity mutations are required to fail closed: attempt-2 label
change, unexpected assignment, attempt-1 runner change, artifact appearance,
run-head change, job-ID change and attempt-2 termination.  This is important:
the committed receipt is a timestamped infrastructure statement, not a live
oracle.  Once the job starts or terminates, the old receipt remains valid only
for its capture time and must not be reused as current state.

Reproduction command:

```bash
python3 ci/exp073r1_v0_7_runner_assignment_audit.py \
  --snapshot data/derived/g7/exp073r1_v07_runner_assignment_snapshot_v0_1.json \
  --out /tmp/exp073r1_v07_runner_assignment_audit_v0_1.json
cmp /tmp/exp073r1_v07_runner_assignment_audit_v0_1.json \
  data/derived/g7/exp073r1_v07_runner_assignment_audit_v0_1.json
```

The hosted self-test workflow is
`.github/workflows/exp073r1-v07-runner-assignment-audit-selftest.yml`.
It reproduces the committed receipt, runs all seven mutations and asserts the
no-science/no-authorization boundary.

## Exact operator recovery procedure

No new registration token and no second runner installation are needed.  The
same registered runner already accepted attempt 1.

1. In WSL, check whether the DSIR listener is already alive:

   ```bash
   pgrep -af 'Runner.Listener|run.sh'
   ```

2. If no DSIR listener is running, start the existing installation:

   ```bash
   cd ~/actions-runner-dsir
   ./run.sh
   ```

3. Keep that WSL process and the host machine awake.  Expected idle output is
   `Connected to GitHub` followed by `Listening for Jobs`.  The queued job
   should be accepted automatically; do not press rerun again.
4. Do **not** rerun `config.sh`, disclose or store a registration token,
   change `[self-hosted, linux]`, cancel attempt 2, or dispatch another heavy
   R1 workflow.  Those actions would not repair the captured assignment state
   and could invalidate the prospectively frozen Exp073P v0.3 authority.
5. When the listener reports `Running job: transport-stabilized-replay`,
   preserve the exact job/attempt.  Do not interpret `metacal-map-longrun` as
   this v0.7 authority; that name belongs to an earlier v0.6 route.
6. On terminal completion, re-read the exact attempt-2 job and complete
   artifact set.  Record runner identity, final step boundary, acquisition
   provenance, artifact ID/digest and the internal terminal assertion.
7. A runner, transport, acquisition, upload or workflow failure remains an
   infrastructure result.  Only internal
   `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` plus all frozen
   provenance and archive checks can supply admissible R1 evidence.
8. Dispatch the canonical Exp073P v0.3 real join only after the exact
   attempt-2 artifact passes that firewall and the production-route byte-freeze
   guard passes.  Never repoint v0.1/v0.2/v0.3.

## Scientific firewall

No support mask, response, `f_invalid`, retained dimension, covariance,
whitening, nuisance SVD/rank, quotient/relation/null, held-out statistic or G8
quantity was read.  No frozen rectangle, threshold, dimension floor, HEALPix
convention, response envelope, signed production weight or stage order was
changed.  `support_executor_authorized=false`; G7/G8/G9 remain OPEN.

No duplicate heavy run and no real aggregate join were dispatched.

## Verification checklist

- immutable snapshot JSON parse: PASS;
- executable runner-assignment audit: PASS;
- seven fail-closed mutations: PASS;
- committed receipt byte reproduction: PASS;
- hosted workflow YAML parse: required before merge;
- repository tests: required before merge;
- hosted self-test: required before merge.
