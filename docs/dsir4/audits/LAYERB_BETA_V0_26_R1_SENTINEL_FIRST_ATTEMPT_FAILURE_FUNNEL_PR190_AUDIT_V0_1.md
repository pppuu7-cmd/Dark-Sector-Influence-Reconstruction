# DSIR Funnel Auditor review — V0.26 R1 sentinel first-attempt failure funnel PR190 v0.1

Date: 2026-09-16  
Role: independent DSIR Funnel Auditor / Critic  
Reviewed repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction` only  
Reviewed main before this audit: `52662ca7a21b3a32377f9b3afe6cfe9d290d6cca`  
Reviewed candidate: PR #190, exact head `d38e9825ba7fa87558c7f729c3abdf67002e038f`  
Verdict: **QUALIFIED**  
Effect: `+0/+0`

## Scope

This review does not reinterpret V0.25 and does not create a sentinel scientific result. It reviews the fail-closed evidence/terminalization path for the already-consumed V0.26 R1 sentinel first attempt, run `35033268924`, and specifically the prospective independent failure-funnel candidate in PR #190.

The science attempt is already fail-closed by the historical interim authority. No rerun, same-nonce second attempt, full 107-row replay, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference, or physical dark-sector inference is authorized by this review.

## Repository reconstruction

Current durable state reconstructs the following chain:

- V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`.
- V0.26 R1 is prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.
- Frozen sentinel workflow W is blob `19907175f0f3417ddee2aba6916d961c6be02e26`; executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`; decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`.
- Corrected launch package identities are A `1c9945dd00b137f3e202efa14bf4112fffebf8af`, L `fa7014435f0a5688def2124898ddd01d0c0183aa`, Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.
- Exact one-run L-gate authority blob `1c1819ee6aa7a48597770d9bc9116185d061a49c` authorized one first attempt only and explicitly forbade rerun and full-107 execution.
- PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` created the exact final L and triggered exactly one science workflow run at that head.

The current `RECOVERY_LATEST.md` / `CURRENT_PROCESS.md` were correct about the consumed pre-science failure but stale about forensic run `35033678449`, which completed successfully while this audit was in progress. That stale recovery state is reconciled after this review.

## Authorization and chronology

Run `35033268924` was authorized by the exact one-run L-gate chain before execution. The first attempt itself is consumed and cannot be repeated under the same authority.

The failure-funnel object in PR #190 is a later governance/evidence audit, not a science executor. It changes only:

- `ci/dsir_v026_r1_sentinel_first_attempt_failure_funnel_audit_v0_1.py`;
- `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_CONTRACT_V0_1.json`.

At reviewed head `d38e9825ba7fa87558c7f729c3abdf67002e038f`, no hosted failure-funnel workflow exists and the contract explicitly forbids execution while forensic artifact identities remain null. Therefore no competing first-attempt terminal verdict has been executed from PR #190.

## Exact science-attempt evidence

GitHub Actions run `35033268924` is terminal `failure`, run #1 / attempt #1, event `push`, exact head `9a333294f3acb80201c5f6ed5b74918c1c767232`.

Jobs independently checked:

- `authorize` job `104596462857`: `failure`;
- `materialize-plan`: `skipped`;
- `lane`: `skipped`;
- `decision` job `104596495504`: `failure` because current-run authorization was absent;
- science-run artifact count: exactly zero.

Authorize log independently maps the failure to embedded Python `<stdin>` line 48, exactly:

`assert added.count(launch)==1`

All earlier sequential W/A/L/Q package assertions were reached without failure. No CLASS lane execution or scientific response artifact exists.

A live exact-head Actions query performed in this audit returned `total_count=1` for head `9a333294f3acb80201c5f6ed5b74918c1c767232`: the sole run is `35033268924`, attempt 1. Thus there is currently no rerun/duplicate exact-head selection contamination.

## Terminal forensic producer evidence

The exact frozen forensic producer is:

- branch `audit/v026-r1-sentinel-first-attempt-forensic`;
- head `c5502bc124f502cb4ef1c19300fcdf87f260089b`;
- producer auditor blob `63b6a0db41ff5e0e3c36be605596fb1c5aee0f1d`;
- producer workflow blob `4d09b78d3a586d3c4f7e42573a7bdac4454d3a48`;
- run `35033678449`, run #3 / attempt #1, event `push`.

During this audit that exact run became terminal `completed/success`. Its single job `104597783801` completed successfully and it emitted exactly one artifact:

- artifact id `10422924571`;
- name `dsir-v026-r1-sentinel-first-attempt-forensic-audit-v0-1`;
- Actions ZIP digest `sha256:226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`.

The artifact ZIP was independently downloaded and hashed. Independent SHA256 equals the Actions digest exactly. It contains exactly seven files and no nested entries:

- `first_attempt_forensic_audit.json`: 2374 bytes, SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`;
- `first_attempt_forensic_audit.sha256`: 105 bytes, SHA256 `f9b19f892d118fbe6cfc9f6e95955e90ba14d58321275bd339e2c209a8f965b2`;
- `input_evidence.sha256`: 332 bytes, SHA256 `cc9b489e0a18b5d1abf37da27746207707dc8e388995506ad40399e4bac4e02d`;
- `run.json`: 14819 bytes, SHA256 `48b1f484024dbf26020b96ef87562b0e9f79558d419ffdb60e102db72b434416`;
- `jobs.json`: 6811 bytes, SHA256 `9c7977b7dae185e6073bb0074e05fc66788b41419292744bec0ecb594913dd14`;
- `artifacts.json`: 32 bytes, SHA256 `244563f989470892c537c9a4622920af0d228ee4528f7d00c64a06d6cd95856c`;
- `authorize.log`: 31246 bytes, SHA256 `548c9b94cc07ffafc1e1d2155e82ad89fe26d48fbd2c2493da2236dc7d9d1a39`.

Both inner SHA256 manifests were independently checked against these bytes. The producer receipt records `TERMINAL_BLOCKED` / `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`, no CLASS invocation, no scientific response, no covariance read, no rerun authorization, and no full-107 authorization.

This producer artifact is valid immutable evidence. It is not itself the independent terminal first-attempt authority requested by the funnel.

## Platform-contract root cause

The frozen workflow reconstructs file changes using `github.event.commits[*].added`, `modified`, and `removed`, with `c.get(..., [])` fallback. The GitHub Actions push-event platform contract used by the repository states that the Actions push payload omits those commit-level file-list attributes. Under that platform contract, the frozen code obtains an empty `added` list, so `added.count(launch)` is zero even though the repository first-parent diff contains exactly one added L.

The repository/tree counterexample therefore goes in the opposite direction from a package-binding failure: the exact L-only change is present, yet the event guard rejects it. This localizes attempt #1 to a workflow/event-contract implementation failure before science. It does not test interpolation, resolution, tolerance, numerical nondeterminism, covariance, nuisance, statistical validity, or dark-sector physics.

## PR #190 candidate audit

The candidate correctly binds the exact science run, exact third-generation forensic producer run/head/code identities, rejects stale producer runs #1/#2, reconstructs the science trigger diff and traceback line, checks the producer ZIP digest, validates both inner hash manifests, checks the science jobs/artifact count, and preserves the interpretation ceiling.

However, two concrete fail-closed counterexamples prevent confirmation of the candidate as execution-ready.

### Counterexample 1 — rerun/selection invariant is not live-bound

The candidate auditor reads the immutable producer's captured `run.json` for science run `35033268924`, but it does not independently enumerate the science workflow runs for exact science head `9a333294f3acb80201c5f6ed5b74918c1c767232` at failure-funnel execution time.

Counterexample: a forbidden rerun or duplicate exact-head workflow run could occur after the producer artifact was captured. The candidate could still pass by consuming the old immutable artifact. This would violate the one-attempt/no-selection invariant without being detected.

The repository is currently clean — the live query finds exactly one exact-head run — but the prospective auditor must assert that fact itself and fail closed if it ever changes.

Required correction: bind/query the exact science workflow/head at hosted funnel execution and require exactly one run, id `35033268924`, run #1 / attempt #1, with no rerun or duplicate exact-head run.

### Counterexample 2 — claimed exact artifact file set is only top-level

The candidate computes:

`{p.name for p in producer_dir.iterdir() if p.is_file()}`

and compares it to the seven expected basenames. This does not recursively reject extra directories or nested files.

Counterexample: the expected seven top-level files plus `extra/response.json` would pass the current set check. The actual producer ZIP is clean and has exactly seven entries, but the prospective auditor's implementation is weaker than its stated exact-file-set requirement.

Required correction: recursively enumerate exact relative artifact paths and reject every unexpected file/directory/symlink; require exactly the seven frozen relative files.

### Additional manifest hardening

`parse_sha256_manifest` normalizes entries with `Path(name).name`. The hardened version should require exact frozen relative names and exact line cardinality, rejecting duplicate/basename-colliding entries rather than normalizing them away.

### Future hosted workflow graph requirement

The candidate independently resolves historical commits and diffs (`FORENSIC_HEAD`, science merge parents, first-parent/staging diffs). A future hosted failure-funnel workflow must therefore checkout full history or explicitly fetch every exact historical SHA required by the auditor. A shallow default checkout is not sufficient.

## Threshold tuning / scientific contamination

No threshold tuning after a scientific response is possible here because attempt #1 never reached materialization/lane execution and emitted no scientific response. PR #190 changes only audit/contract files and does not change the R1 hypothesis, scientific thresholds, numerical solver object, row denominator, input geometry, executor, decision code, W/A/L/Q science identities, or interpretation ceiling.

No partial substantive values were consumed in this review.

## Verdict

**QUALIFIED**.

The pre-science event-guard failure and its immutable forensic provenance are independently supported. The current repository also independently satisfies the no-rerun invariant. However, PR #190 head `d38e9825ba7fa87558c7f729c3abdf67002e038f` is not execution-ready because its contract still contains now-stale null producer artifact identities and its independent auditor does not fail closed against a later forbidden rerun/duplicate exact-head science run or nested artifact extras.

This qualification does not alter the historical interim `BLOCKED` authority and does not create a sentinel scientific classification.

## Required successor action

Prospectively revise PR #190 as a new exact candidate head, without changing science/runtime objects:

1. freeze producer artifact id `10422924571`, ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`, and producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`;
2. add live exact-head science-run enumeration and require exactly the single consumed run/attempt;
3. make artifact-entry validation recursive/exact and manifest parsing collision-free;
4. require full-history/exact-SHA availability in any future hosted funnel workflow;
5. subject the revised code+contract to a fresh response-blind static/funnel review before authoring or executing a hosted failure-funnel workflow.

Until that successor review passes, do not execute the independent failure funnel and do not write terminal first-attempt result authority. Rerun, same-nonce second attempt, successor science, full 107-row replay and all downstream layers remain closed.
