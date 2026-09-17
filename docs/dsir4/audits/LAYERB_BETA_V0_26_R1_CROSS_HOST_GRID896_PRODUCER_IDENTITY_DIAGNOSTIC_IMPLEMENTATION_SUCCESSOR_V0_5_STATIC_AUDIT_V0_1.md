# DSIR Funnel Auditor — GRID896 diagnostic implementation successor V0.5 static audit V0.1

Date: 2026-09-17. Scope: DSIR only. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

Reviewed `main`: `28743d615e1e66da66c6ab49f08bdaf3480478f5`.

Reviewed exact frozen V0.5 identities:
- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_5.py`, blob `224a4b8472c6aa0081627894d31cf967a2f2fc78`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-5.yml`, blob `f2134d3f80ead145aaae1c1203eac0626cf914f7`;
- frozen implementation manifest `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_MANIFEST_V0_5.json`, blob `a19883ec25942664c89afe40b89ef5afa8cc8bf1`.

The active V0.5 workflow and launch marker are absent on reviewed main. Current Actions has zero queued and zero in-progress runs. No V0.5 execution or partial substantive values were used.

## Authorization and chronology

Terminal V0.4 qualification blob `f5d15887f88e6d9753e475d9c69572265babb2d6` authorized only prospective inert V0.5 authoring followed by a fresh independent static audit. That chronology is satisfied. No workflow promotion, implementation execution authority, marker creation, diagnostic execution or science gate is authorized by this review.

The V0.5 candidate preserves the V0.4 first-parent launch chronology controls: triggering checkout HEAD must equal `GITHUB_SHA`; launch must be a single-parent commit; terminal implementation authority and exact canonical active workflow must preexist unchanged in `HEAD^`; marker must be absent in `HEAD^`; and the launch first-parent diff must contain only addition of the exact marker.

## V0.4 defect closure

The specific V0.4 duplicate/rerun reachability defect is prospectively closed in V0.5 source. The lane matrix remains gated to push/main + run #1 + attempt #1. The decision job has `needs: grid896` plus `always()` and push/main, but no run-number/run-attempt job-level condition. Therefore, for the exact workflow identity, run #1/attempt #2, run #>1/attempt #1 and run #>1/attempt #>1 skip the lanes but still reach aggregate classification. The aggregate one-shot guard detects the non-1 run number/attempt, writes `INVALID_DIAGNOSTIC_PROVENANCE`, the workflow then attempts the decision-artifact upload, and the final step reflects non-PASS as failure.

The surviving V0.4 controls are also present: exact 897-line u64hex source checks; unsigned-u64 fixed little-endian producer; exact 7176-byte/SHA256 guard; true `<d` binary64 decode then immediate `<d` reserialize without arithmetic; frozen one-bit negative control; exact R01..R32 matrix; present-artifact validation before incomplete-population BLOCKED; present INVALID before incomplete-population BLOCKED; established FAIL before incomplete-population BLOCKED; outer Actions digest versus independently computed ZIP SHA256; exact one-file ZIP member; inner receipt SHA256; job/run/head/event/ref/code bindings; and no CLASS/scientific-response access.

## New deterministic counterexample — executing workflow identity is not bound

The frozen design requires one launch only, no lane replacement, no same-identity retry, and exact audited code/workflow identity. V0.5 does not bind the *workflow that is actually executing the run* to the canonical promoted workflow path or workflow identity.

The executor computes `workflow_blob` from the inert candidate path and `verify_launch_authorization()` checks that the canonical `ACTIVE_WORKFLOW_PATH` exists and has that same blob. It never checks the current run's actual workflow path/ID (`workflow_run.path` / workflow ID) and the workflow has no exact `github.workflow_ref`/executing-path guard. `discover_job_id()` binds only the current run ID and expected job name; receipt/artifact validation binds run ID/head/job and the candidate blob, but not the executing workflow path.

Concrete counterexample after an otherwise correct promotion/authority setup:

1. canonical active workflow `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-5.yml` preexists with the exact audited blob;
2. before the marker-only launch, a second workflow file at another `.github/workflows/...` path is present as an exact byte copy of the same audited workflow;
3. both workflows subscribe to the same launch-marker push path;
4. the marker-only launch push triggers both distinct workflow identities;
5. each workflow can have its own run #1 / attempt #1, so both lane matrices satisfy the current job-level one-shot condition;
6. in the alias-copy run, the executor still observes the canonical active path with the correct blob, the same candidate blob, the same authority and marker, and the same launch commit chronology. Nothing compares the current run's actual workflow path/ID to the canonical active path;
7. the alias-copy run can therefore produce a second 32-lane execution and a second decision under the same experiment identity while all current V0.5 runtime checks pass.

This is not a hypothetical threshold concern: it is a direct identity omission in the frozen source. `run_number==1` is only meaningful inside the currently executing workflow identity; it is not a repository-global one-shot token. A byte-identical alias workflow is not rejected because the implementation authenticates a repository file blob, not the workflow identity that GitHub actually executed.

Consequently V0.5 has not proven the frozen no-duplicate/no-replacement condition and cannot be promoted or executed. A green future run of this exact implementation would not repair the missing identity predicate.

## Required prospective successor

Do not rewrite V0.5. A new inert successor must preserve all surviving V0.5 controls and additionally bind the current Actions run to the exact canonical active workflow identity before any lane operation. At minimum it must:

1. verify the executing workflow path is exactly the canonical active V0.6 path, using a fail-closed current-run metadata check and/or exact `github.workflow_ref` path binding;
2. preferably bind the GitHub workflow ID after promotion in the later authority/launch object and verify the current run's workflow ID/path against it;
3. ensure the same executing-workflow identity check is revalidated by aggregate/decision, not only by lane code;
4. add a static negative case showing that a byte-identical alias workflow at another path cannot execute admissible lanes or produce an admissible PASS/FAIL decision;
5. retain V0.5 duplicate/rerun decision reachability, first-parent chronology, binary64/hash/negative-control, artifact provenance, classifier precedence, 32-lane topology and no-science boundary.

A later terminal authority may be considered only after a fresh independent static audit of that new exact successor.

## Interpretation ceiling

This is infrastructure/provenance/static implementation only. No GRID896 cross-host diagnostic was executed. No CLASS solve or scientific response was read. Numerical response reproducibility, exact-target/scientific validity, covariance, whitening, nuisance marginalization, relation-null, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`. Scientific effect remains `+0/+0`; no readiness/frontier increase is authorized.

## Review result

Verdict: **INVALID_IMPLEMENTATION**.

Classification: `GRID896_DIAGNOSTIC_SUCCESSOR_V0_5_EXECUTING_WORKFLOW_IDENTITY_NOT_BOUND`.

V0.5 remains historical frozen evidence. Workflow promotion, V0.5 terminal implementation execution authority, launch-marker creation, diagnostic execution, successor sentinel science, full107 and downstream science remain closed.