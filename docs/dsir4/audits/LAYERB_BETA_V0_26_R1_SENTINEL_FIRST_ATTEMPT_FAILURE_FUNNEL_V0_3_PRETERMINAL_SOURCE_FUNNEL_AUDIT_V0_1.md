# DSIR Funnel Auditor — V0.26 R1 failure-funnel v0.3 preterminal source/provenance audit

Date: 2026-09-16. Scope: DSIR only. GitHub repository and Actions are the sole durable scientific source of truth.

Reviewed default-branch baseline: `6176a5086fb1fd3fe59e68db2ccaa8c030e23a0a`.

Reviewed prospective candidate head: `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c` on `audit/v026-r1-failure-funnel-v03-schema-runtime-closure`.

## Gate state

The current default-branch terminal state authorizes only prospective correction and independent re-audit of the hosted failure-funnel interface. It does not authorize failure-funnel dispatch, science rerun, same-nonce second attempt, successor sentinel science, full 107-row execution, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, or downstream statistical/physical inference.

The exact v0.3 hosted static compatibility run is Actions run `35046173814`, workflow `359235031`, exact head `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c`, run #7 / attempt #1. At review time it is `queued`, its only job `104636353665` is `queued`, and the run has zero artifacts. Exact-head Actions enumeration returns exactly one run for `d71c8d7a...`. Therefore no terminal hosted receipt exists and no outcome-dependent values from that run are admissible.

The older v0.2 runtime-binding run `35044374801` is also still queued/nonterminal. Its exact v0.2 implementation remains independently qualified as not execution-ready because of the already-durable producer/consumer schema mismatch, irrespective of any later CI color.

## Prospective chronology and identities

The v0.3 branch is 14 commits ahead of reviewed main and changes only the hosted failure-funnel governance/audit package. No V0.26 scientific thresholds, denominator, CLASS executor, sentinel decision logic, final L, covariance object, or full-replay object are changed.

Exact candidate identities reviewed:

- hosted workflow: `.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-3.yml`, blob `1b73d49539470dad89dff4aa7e660529e5f5a72a`;
- execution-authority candidate: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_3.json`, blob `c9a03bff716fac3b2a19a2e16fed08f4edcb809b`;
- review-confirmation candidate: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_3.json`, blob `fff04da57136b48902b9d6dad38f2d7df2e8087d`;
- frozen PR190 producer/auditor: head `5731b605afdc35bd85d3a2014a9e135719a07697`, blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`;
- v0.3 static compatibility auditor: `ci/dsir_v026_r1_sentinel_first_attempt_failure_funnel_v03_static_compatibility_audit_v0_1.py`, blob `47c27ab3179e9e803e945e9c7779353d18d0c4d0`;
- hosted static compatibility workflow: `.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-v03-static-compatibility-audit-v0-1.yml`, blob `2ba18f30f78041e3b9378c2cb987e92bae15f907`;
- v0.3 machine contract: `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_CANDIDATE_V0_3.json`, blob `d6f440ac1063486cd8dbdda77d7e366c66180f6b`.

The v0.3 contract is frozen before the exact hosted audit run at `d71c8d7a...`; no result-dependent threshold or science-object tuning is present.

## Independent source/code control

The previously identified v0.2 deterministic interface defect is prospectively corrected in the exact v0.3 workflow. The hosted post-auditor consumer now requires `successor_science_authorized_by_this_receipt`, which is exactly the field emitted by frozen PR190 producer blob `f7eff337...`; it no longer requires the nonexistent v0.2 key `successor_science_authorized`.

The v0.3 static compatibility auditor reconstructs the frozen producer's literal output-dictionary keys from the exact PR190 source and compares them with every direct `d['...']` receipt access in the exact hosted workflow. For the exact frozen workflow, the consumed set is compatible and includes the corrected successor-science field.

The second-order v0.2 runtime-authority weakness is also prospectively closed in the exact v0.3 workflow: dispatch requires a fixed future terminal runtime-binding audit-authority path, an exact caller-supplied blob SHA1 for that file, runtime equality between the file blob and supplied SHA1, and semantic binding from that future authority back to exact workflow/A/review blobs, nonce, ref, event, one-dispatch policy, run-attempt policy, consumer-schema confirmation, and all science prohibitions.

The resulting dependency graph is acyclic: W/A/review can be frozen first; a later terminal runtime-binding audit authority can bind those exact blobs; dispatch then supplies the exact terminal-authority blob as an input. The workflow does not hard-code a not-yet-existing future authority hash.

The one-dispatch guard is fail-closed: on an actual dispatch it enumerates workflow-dispatch history and requires exactly one run for the exact workflow path, that run to be the current run, attempt 1, on `main`. Any premature/duplicate dispatch consumes or blocks the gate rather than creating a false PASS.

The hosted workflow independently refreshes the consumed science-run history, filters the frozen science workflow/head/event inside the frozen PR190 auditor, pins the forensic artifact ZIP digest, and re-runs the hardened recursive artifact/manifest checks. No CLASS scientific computation is added.

No new deterministic source-level counterexample was identified in this exact v0.3 set during this review. This statement is source-scoped only and is not a substitute for the queued hosted audit.

## Provenance and selection control

Run #7 reflects development history of the static-audit workflow, but the exact frozen head `d71c8d7a...` currently has exactly one run and attempt 1. Because that run is nonterminal, there is no successful/failed exact-head outcome available to select. Earlier development-head runs cannot be used as evidence for the frozen exact head.

No artifact or receipt exists for run `35046173814` at review time. Accordingly, no ZIP digest, inner receipt hash, terminal classification, or promotion authorization is recorded here.

## Interpretation ceiling

This audit is limited to prospective governance/provenance/static implementation. It does not establish numerical reproducibility, interpolation stability, resolution stability, tolerance stability, execution-order independence, statistical/model validity, nuisance removal, covariance validity, or physical dark-sector inference. Scientific effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## Review result

Verdict: **BLOCKED**.

Reason: the exact authoritative hosted static compatibility workflow is still nonterminal and has no artifact. The independent source/code review found that the two known v0.2 defects are prospectively corrected and found no new deterministic source blocker, but gate-chain rules prohibit confirming, promoting, or executing the v0.3 object before terminal hosted evidence and independent artifact verification.

Next admissible action: wait for exact run `35046173814` to become terminal without rerunning it. If it succeeds, independently verify its job completion, unique exact-head attempt, artifact count, Actions ZIP digest, inner receipt/manifest hashes, and exact bound blobs before authoring any separate terminal runtime-binding audit authority. If it fails, preserve the failure and audit it; do not tune the frozen candidate or select a rerun. Until a later terminal authority explicitly says otherwise, do not promote/dispatch v0.3, do not rerun science run `35033268924`, do not create a same-nonce second attempt, do not modify/remove/recreate final L, and keep full 107-row and all downstream gates closed.
