# DSIR Funnel Auditor — cross-host GRID896 diagnostic implementation successor V0.4 static audit V0.1

Date: 2026-09-17. Scope: DSIR only. GitHub repository/Actions are the sole durable scientific source of truth.

Reviewed main: `a0bac968861608b6e1b758c1fbe2e25b74dfb7fd`.

Reviewed exact frozen V0.4 identities:
- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_4.py`, Git blob `81b352d586f5e13ff2f50d254b11384f3e326b86`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-4.yml`, Git blob `6f18bdd2e0924498a0a076abf9ee80b9b5da4580`;
- implementation manifest `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_MANIFEST_V0_4.json`, Git blob `4a0813c0935623e1f266038774ad6048897bbf39`.

Frozen parents remain preregistration `903c80709439cb790bd41316029b218a77d5695b`, machine contract `6ba6e5a6c946a1091680f8f44821d323c9a463f3`, canonical source `24fa61685ab45e42e3ab0d453f5cb223c247ced6`, preexecution confirmation `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`, and terminal V0.3 qualification `b20311d02c8fc0353e04c138b8ad4f121f4de0a2`.

At review time the V0.4 active workflow path and V0.4 launch marker are absent. Repository Actions have zero queued and zero in-progress runs. No V0.4 diagnostic execution, artifact, partial lane value, CLASS solve, scientific response, covariance read or downstream science result exists or is used by this review.

## Authorization and preregistration

V0.3 terminal authority authorized only prospective inert V0.4 authoring followed by an independent static audit. V0.4 was authored prospectively and remained inert. No scientific threshold, denominator, tolerance, sampling range, PASS/FAIL/BLOCKED scientific criterion or interpretation ceiling changed.

The frozen GRID896 design still requires one future experiment identity with exactly 32 lanes R01..R32, `ubuntu-24.04`, one launch, run #1 / attempt #1 only, no replacement or same-identity retry. It explicitly classifies a duplicated/rerun execution or `attempt != 1` as `INVALID_DIAGNOSTIC_PROVENANCE`.

## Controls that survive independent review

The V0.4 exact source prospectively closes the V0.3 chronology defect. `verify_launch_authorization()` requires checked-out `HEAD == GITHUB_SHA`, exactly one parent, exact implementation-authority bytes unchanged in `HEAD^`, exact promoted active-workflow bytes unchanged in `HEAD^` and equal to the audited candidate blob, marker absence in `HEAD^`, and a first-parent diff consisting only of addition of the exact marker. Therefore the required explicit chronology counterexamples are rejected at source level: authority created/modified in the launch commit, active workflow created/modified in the launch commit, marker already present in the parent, any extra changed path, and merge/zero-parent launch commits all fail closed.

The implementation also preserves the previously audited controls: exact prereg/contract/canonical/preexecution blobs; canonical 897-line lowercase u64hex source hash; unsigned-u64 little-endian producer; 7176-byte payload hash; real `<d` decode followed by immediate `<d` reserialization without arithmetic; frozen one-bit negative control; exact R01..R32 topology; no `workflow_dispatch`; API artifact id/name/run/head binding; API digest versus independently computed ZIP SHA256; single-member inner receipt; inner receipt SHA256; job/run/event/ref/code identity binding; present-artifact validation before incomplete-population BLOCKED; present INVALID precedence; established FAIL precedence over missing lanes; complete PASS only for 32 bound all-PASS receipts; and no CLASS/scientific-response access.

## Deterministic counterexample — duplicate/rerun INVALID path is unreachable

The frozen preregistration and contract require `INVALID_DIAGNOSTIC_PROVENANCE` when the run is duplicated/rerun or `run_attempt != 1`. The V0.4 Python aggregate contains a correct fail-closed guard for this case: if run number or attempt differs from 1 it raises `ProvenanceInvalid`, writes an INVALID decision, and returns nonzero.

However the exact V0.4 workflow prevents that classifier from executing in precisely those cases. The matrix job has a job-level condition requiring `github.run_number == 1 && github.run_attempt == 1`. More importantly, the `decision` job has the same job-level condition:

`if: ${{ always() && github.event_name == 'push' && github.ref == 'refs/heads/main' && github.run_number == 1 && github.run_attempt == 1 }}`

Therefore an Actions rerun with attempt 2, or any same-workflow duplicate with run number greater than 1, skips the decision job before the Python aggregate can classify it. No V0.4 decision artifact is then produced to durably record the contractually required `INVALID_DIAGNOSTIC_PROVENANCE` classification. The implementation's one-shot guard exists in code but is unreachable on the invalid executions it is supposed to adjudicate.

This is a direct implementation-versus-preregistration mismatch, not a hypothetical numerical concern. The exact same frozen implementation can therefore have an invalid duplicate/rerun Actions execution without emitting the frozen INVALID decision object required by the experiment contract. External reviewers may later notice the extra Actions run, but that does not make the exact candidate realize its frozen classifier or artifact semantics.

A green/neutral/skipped CI surface is not a substitute for a terminal INVALID receipt. The defect is upstream of any hosted diagnostic result and independent of all GRID896 values.

## Alternative explanations and scope

The defect is not interpolation, grid resolution, solver tolerance, execution-order numerical dependence, covariance, nuisance, look-elsewhere selection, or physical-systematics behavior. No numerical/scientific quantity is evaluated. It is a deterministic workflow reachability/provenance defect.

The chronology correction itself survives this audit and should be preserved in a successor. The binary64/hash/artifact/classifier-precedence/no-science controls also survive. The failure is narrower: duplicate/rerun provenance is declared INVALID by the frozen contract but the workflow suppresses the only decision path capable of emitting that classification.

## Required prospective correction

Do not modify the historical V0.4 blobs. Author a new inert successor V0.5 prospectively. At minimum:

1. keep the lane matrix one-shot-gated so duplicate/rerun executions do not produce replacement lane evidence;
2. make a provenance/decision job execute for every matching push/ref even when `run_number != 1` or `run_attempt != 1`;
3. let that job run the frozen aggregate/provenance guard so duplicate/rerun/attempt>1 produces and uploads a durable `INVALID_DIAGNOSTIC_PROVENANCE` decision artifact;
4. preserve all V0.4 first-parent chronology guards and all surviving V0.3 binary64/hash/artifact/classifier/no-science controls;
5. independently static-audit the exact V0.5 executor/workflow/manifest before any promotion, authority, marker or execution.

A fresh live workflow-history enumeration in the provenance/decision path is an admissible additional hardening, but no same-identity retry or execution is authorized by this audit.

## Interpretation ceiling and funnel effect

This is infrastructure/provenance/static implementation only. Scientific effect remains `+0/+0`. Numerical response reproducibility, exact-target/scientific criteria, covariance, whitening, nuisance marginalization, relation-null, statistical/model validity, identifiability and physical dark-sector inference remain `NOT_EVALUATED` or closed. No readiness/frontier increase is authorized.

## Verdict

**INVALID_IMPLEMENTATION**

Classification: `GRID896_DIAGNOSTIC_SUCCESSOR_V0_4_DUPLICATE_RERUN_INVALID_CLASSIFIER_UNREACHABLE`.

Frozen V0.4 remains historical and must not be promoted, given a launch marker, or executed. The next admissible gate is prospective inert V0.5 authoring with a reachable duplicate/rerun INVALID decision path, followed by a fresh independent static audit.
