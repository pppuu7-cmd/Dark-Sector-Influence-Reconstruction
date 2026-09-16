# DSIR Funnel Auditor — V0.26 R1 failure-funnel v0.3 dispatch-history guard audit

Date: 2026-09-16. Scope: DSIR only. GitHub repository and Actions are the durable scientific source of truth; chat is not authority.

Reviewed main baseline: `9dc360c420c116fe5196757122305bdeb98d09c1`.

Reviewed frozen prospective candidate head: `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c` on `audit/v026-r1-failure-funnel-v03-schema-runtime-closure`.

Authoritative hosted static-compatibility run remains `35046173814`, workflow `359235031`, run #7 / attempt #1, exact head `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c`. At this review it remains queued/nonterminal. Its only job `104636353665` is queued, has `runner_id=0`, empty runner identity, no steps and no artifacts. Exact-head Actions enumeration returns exactly one run. No partial substantive result from this run is used.

## Scope and authorization boundary

Current terminal authority still permits only response-blind source/provenance review while the exact hosted static workflow is nonterminal. It does not authorize promotion or dispatch of v0.3, rerun of science run `35033268924`, a same-nonce second attempt, successor sentinel science, full 107 rows, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, or downstream statistical/physical inference.

The frozen V0.26 R1 scientific object is unchanged. No threshold, tolerance, denominator, sampling rule, numerical solver object or interpretation ceiling is modified by this audit.

## Exact source reviewed

The reviewed hosted workflow is `.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-3.yml`, blob `1b73d49539470dad89dff4aa7e660529e5f5a72a`.

Its one-dispatch guard currently:

- enumerates visible `workflow_dispatch` runs;
- filters them by exact workflow path;
- requires `len(exact)==1`;
- requires the only visible run id to equal `GITHUB_RUN_ID`;
- requires both API and environment run attempt to equal 1;
- requires `head_branch=='main'`.

The guard does **not** require the monotonic workflow run number to equal 1 (`only['run_number']==1` / `GITHUB_RUN_NUMBER==1`). It also records the dispatch-history snapshot only once, early in the run, before the forensic download, frozen PR190 auditor execution and artifact persistence.

The exact v0.3 static compatibility auditor, blob `47c27ab3179e9e803e945e9c7779353d18d0c4d0`, checks producer/consumer receipt schema closure and the future runtime-binding authority hook, but does not verify a monotonic run-number first-dispatch invariant and does not verify a post-execution live dispatch-history recheck.

## Counterexample 1 — visible-history deletion gap

Consider an earlier dispatch of the same workflow path that is no longer present in the current visible Actions run list, followed by a second dispatch. The second dispatch can satisfy every currently frozen in-workflow check if the visible list contains only the current run: `len(exact)==1`, current id matches, run attempt is 1 and branch is main.

The candidate does not inspect the current run's workflow `run_number`. Therefore the one-dispatch claim is not tamper-evident against loss of an earlier visible run-history entry. A current run with `run_number>1` can pass the frozen guard if the current list contains only that run.

This is a concrete provenance counterexample to the prior source-audit statement that any premature/duplicate dispatch necessarily consumes or blocks the gate. The current implementation proves only uniqueness in the *currently visible list*, not historical first-dispatch identity.

## Counterexample 2 — early-snapshot TOCTOU gap

The visible-history check occurs before the main failure-funnel work and before artifact persistence. A second dispatch created after the first run passes that early check is not represented in the already-written `safe/current_workflow_runs.json` snapshot. The first run can therefore continue and persist evidence while the total dispatch-event count has become greater than one.

A later independent terminal result audit could catch such a late duplicate if it performs a fresh live enumeration after the hosted run terminates, but the frozen v0.3 workflow does not itself make this invariant self-contained and the current static auditor does not require that downstream post-run control.

## Qualification

The known v0.2 producer/consumer schema mismatch remains prospectively corrected in v0.3, and the future runtime-binding authority hook remains acyclic. Those improvements survive this audit.

However the exact v0.3 candidate is not execution-ready because its exact-one-dispatch provenance condition is weaker than the authority it claims to enforce. A future green result from static run `35046173814` cannot close this source-level counterexample because the frozen static auditor does not test it.

The queued run must not be rerun or used selectively. If it later completes, preserve its terminal state as historical evidence for the exact frozen v0.3 source; it does not authorize v0.3 dispatch after this qualification.

## Required prospective correction

Do not rewrite the frozen v0.3 object. Create a new prospectively frozen successor candidate and independently re-audit it. The successor must, at minimum:

1. require exact first-dispatch monotonic identity: API `run_number==1` and runtime `GITHUB_RUN_NUMBER==1`, in addition to run attempt 1;
2. retain the current exact path/current-id/main/ref/nonce/blob checks;
3. define an explicit post-run live dispatch-history control for terminal result validation, after the hosted run is terminal, rejecting any workflow-path dispatch history other than the single authorized run and requiring its `run_number==1` / attempt 1;
4. require the successor static auditor to verify these exact first-dispatch and post-run-history invariants against the frozen hosted workflow source;
5. preserve all existing science prohibitions and all historical BLOCKED/FAIL states.

A final in-run re-enumeration immediately before artifact persistence is a useful additional control, but it is not a substitute for the post-run terminal live-history audit because a later unauthorized dispatch can occur after any finite in-run check.

## Interpretation ceiling

This review is governance/provenance/static implementation only. No CLASS solve, scientific response, covariance read, interpolation/resolution/tolerance check, numerical reproducibility test, statistical/model inference, nuisance removal or dark-sector inference was performed. Scientific effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## Review result

Verdict: **QUALIFIED**.

Classification: `V0_3_EXACT_ONE_DISPATCH_PROVENANCE_NOT_TAMPER_EVIDENT_OR_POST_RUN_CLOSED`.

Authorized next stage: prospectively freeze a successor hosted failure-funnel candidate that closes the run-number/history gap and subject it to a fresh independent response-blind static audit. Do not promote or dispatch frozen v0.3. Do not rerun run `35046173814`; if it terminates, archive/audit it as historical exact-v0.3 evidence only.
