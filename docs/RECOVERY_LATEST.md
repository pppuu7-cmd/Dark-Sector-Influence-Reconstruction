# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-16. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Terminal scientific/numerical baseline

V0.25 remains terminal: `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Its historical producer provenance defect was separately corrected without rewriting the historical authority/result. Numerical/reproducibility chain remains terminal through V0.25; statistical/model and physical dark-sector layers remain unopened.

V0.26 R1 is prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain: 107 rows = DES 53 + BOSS 54; alpha route `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. None of the current governance work changes those values.

## Sentinel implementation and consumed first attempt

Frozen identities remain W `19907175f0f3417ddee2aba6916d961c6be02e26`; executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`; decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`; implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`; corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`; corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`; corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` triggered Actions science run `35033268924`, workflow `359060727`, run #1 / attempt #1. It is terminal failure before science at frozen W event guard `assert added.count(launch)==1`; materialize-plan and lane were skipped; science artifact count is zero; no CLASS scientific response, covariance or sentinel classification exists.

Historical fail-closed authority remains binding: **never rerun run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L.** No full-107 or downstream science follows from this failure.

## Immutable forensic and hardened PR190 chain

Forensic head `c5502bc124f502cb4ef1c19300fcdf87f260089b`; run `35033678449`, run #3 / attempt #1; job `104597783801`; terminal success. Exactly one artifact `10422924571`; ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`; producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`; producer classification `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`. This is immutable response-blind forensic evidence, not science PASS.

Hardened open/draft PR #190 exact head `5731b605afdc35bd85d3a2014a9e135719a07697` remains frozen for review use. Auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`; contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`. Independent hardened re-audit run `35036894735` is terminal success; Funnel Auditor confirmation authority blob `d2fe264e2866b9f490a7523a32f341fb7cc08d0b` verdict `CONFIRMED_SCOPED`. This confirms hardened static logic only and does not authorize execution.

## PR #193 authority now on main

The previous recovery was stale relative to current main. Main `8493f247b3095a139626cf11cfaa80e85daad293` merged PR #193 and persisted terminal hosted-workflow static-audit authority:

`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_AUTHORITY_V0_1.json`.

Status `TERMINAL_STATIC_AUDIT_AUTHORITY`; verdict `QUALIFIED`; classification `HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_EXECUTION_AUTHORITY_REVIEW_ONLY`; effect `+0/+0`.

It binds hosted workflow candidate head `1a1f33df835218b7c6232e2a9078d6681081b16f`, workflow blob `71d054036e251dce50d0bcfc8429b6d875ceb9c4`, contract blob `2152e952e37fd1f22f5f38b976379540103de2ef`, static audit run `35040852174` run #1 / attempt #1, job `104620152031`, artifact `10424714637`, ZIP SHA256 `e993e323ed7c78aceece8f877d9056b0f6a8c355e1bbd1c977109f5aea56e0d6`, receipt SHA256 `b49dc127cfc6c59ed9e1b56de880c182ad38279851e0a15adfc03e7df1ecf9fa`. It authorizes only separate one-run execution-authority authoring/review. Failure-funnel dispatch remains unauthorized.

## Runtime-binding blocker and v0.2 candidate

Execution-authority compatibility run `35041244978`, workflow `359203695`, head `319204c384be5b67fba9b05e85f29f5cb4198ba4`, run #1 / attempt #1, is terminal `completed/success`. Job `104621354119` succeeded. Its only artifact `10424693735` has digest `sha256:0e4b94d8b6f1b08884870eab5aeed8883025aa7afe7704d9753cb9073f799f54`. Its substantive result was a fail-closed runtime-binding classification: `HOSTED_FAILURE_FUNNEL_EXECUTION_AUTHORITY_RUNTIME_BINDING_INCOMPLETE`.

Prospective correction candidate head `4c8a59b68791c0320840652dff65f1a106e89634` contains:
- hosted workflow blob `670a771e1d2e2854c33d71cc1c37ea6beea85566`;
- execution authority candidate blob `47788695c3ab7050099ed44cacbb6f507cbbf03d`;
- independent review-confirmation candidate blob `f8824d107a7fbfb260e5c5946a9d05f71131c94b`;
- runtime-binding auditor blob `66f4c9352c8efa0732d625689c4ba582535dfb73`.

Its runtime-binding Actions run `35044374801`, workflow `359223774`, run #1 / attempt #1, remained **queued/nonterminal** during the current Funnel Auditor review. No partial substantive output was used and no competing outcome verdict was created for that run.

## Independent v0.2 consumer-schema audit — terminal QUALIFIED

Independent exact-source inspection found a deterministic software-interface counterexample before any execution is admissible. The hosted v0.2 workflow executes frozen hardened PR190 auditor blob `f7eff337...` and then requires receipt key:

`successor_science_authorized`

The frozen producer instead emits:

`successor_science_authorized_by_this_receipt`

Thus, if the hosted workflow reaches its post-auditor validation step, the exact consumer raises Python `KeyError` and cannot reach intended successful evidence persistence. Other adjacent consumed keys are present; this is a specific schema mismatch.

The v0.2 runtime-binding static auditor checks ref/blob/nonce/first-attempt binding but does not verify every hosted receipt-consumer field against the exact frozen producer output schema. Therefore any later green result of run `35044374801` would not, by itself, close this counterexample.

Durable audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_2_CONSUMER_SCHEMA_FUNNEL_AUDIT_V0_1.md`, commit `be24de86d097654cb2946195d8733e72ae55b0dc`.

Terminal qualification authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_2_CONSUMER_SCHEMA_QUALIFICATION_V0_1.json`, commit `6b9fccfca804b36f855c0f497da212b4c26845cb`, verdict **`QUALIFIED`**, classification `HOSTED_FAILURE_FUNNEL_V0_2_NOT_EXECUTION_READY_DUE_TO_FROZEN_PRODUCER_CONSUMER_SCHEMA_MISMATCH`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_2_CONSUMER_SCHEMA_V0_1.md`, commit `1e2bcd8085d2cecc409f395fae51b7fa73d594b4`.

`docs/CURRENT_PROCESS.md` reconciliation commit: `172fa76f076b60d887268d009030521c9abc5579`.

## Current funnel position and interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> EXACT SENTINEL ATTEMPT CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> FORENSIC EVIDENCE TERMINAL -> HARDENED PR190 CONFIRMED_SCOPED -> PR193 HOSTED-WORKFLOW STATIC AUTHORITY QUALIFIED -> EXECUTION-AUTHORITY RUNTIME-BINDING BLOCKER -> V0.2 CORRECTION CANDIDATE -> NONTERMINAL RUNTIME-BINDING AUDIT + INDEPENDENT SOURCE COUNTEREXAMPLE -> V0.2 CONSUMER-SCHEMA QUALIFIED/NOT EXECUTION-READY -> FAILURE-FUNNEL DISPATCH CLOSED -> FULL 107 ROW CLOSED`.

Interpretation ceiling remains governance/provenance/static implementation only. No CLASS solve or scientific response was reviewed. Green CI is not numerical science, statistical/model validity, nuisance removal or physical dark-sector evidence. Effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## Exact authorized next stage

`PROSPECTIVELY_CORRECT_AND_REAUDIT_HOSTED_FAILURE_FUNNEL_RECEIPT_CONSUMER_INTERFACE` only.

Next admissible sequence:
1. Do **not** dispatch exact v0.2 candidate head `4c8a59b...`, even if its currently incomplete static audit later becomes green.
2. Create a new exact prospective candidate whose hosted consumer uses frozen producer key `successor_science_authorized_by_this_receipt` or a separately frozen explicit equivalent schema mapping.
3. Harden its independent static auditor to verify every hosted receipt-consumer field against the exact frozen PR190 producer output schema.
4. Run a fresh independent response-blind static audit of the corrected exact candidate.
5. Only a later terminal authority may decide whether exact promotion and one hosted failure-funnel dispatch are admissible.

Until then: **never rerun run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; do not dispatch the v0.2 failure funnel; do not run successor sentinel science; do not run full 107 rows; keep covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537 and all downstream statistical/model/physical science closed.**
