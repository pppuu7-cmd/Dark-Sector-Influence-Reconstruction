# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-16. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Terminal scientific/numerical baseline

V0.25 remains terminal: `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Its historical producer provenance defect was separately corrected without rewriting the historical authority/result. Numerical/reproducibility chain remains terminal through V0.25; statistical/model and physical dark-sector layers remain unopened.

V0.26 R1 is prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain: 107 rows = DES 53 + BOSS 54; alpha route `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. None of the current governance work changes those values.

## Sentinel implementation and consumed first attempt

Frozen identities remain W `19907175f0f3417ddee2aba6916d961c6be02e26`; executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`; decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`; implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`; corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`; corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`; corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` triggered science run `35033268924`, workflow `359060727`, run #1 / attempt #1. It is terminal failure before science at frozen W event guard `assert added.count(launch)==1`; materialize-plan and lane were skipped; science artifact count is zero; no CLASS scientific response, covariance or sentinel classification exists.

Historical fail-closed authority remains binding: **never rerun run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L.** No full-107 or downstream science follows from this failure.

## Immutable forensic and hardened PR190 chain

Forensic head `c5502bc124f502cb4ef1c19300fcdf87f260089b`; run `35033678449`, run #3 / attempt #1; job `104597783801`; terminal success. Exactly one artifact `10422924571`; ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`; producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`; producer classification `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`. This is immutable response-blind forensic evidence, not science PASS.

Hardened open/draft PR #190 exact head `5731b605afdc35bd85d3a2014a9e135719a07697` remains frozen for review use. Auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`; contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`. Independent hardened re-audit run `35036894735` is terminal success; Funnel Auditor confirmation authority blob `d2fe264e2866b9f490a7523a32f341fb7cc08d0b` verdict `CONFIRMED_SCOPED`. This confirms hardened static logic only and does not authorize execution.

## PR #193 terminal static authority

Main merge `8493f247b3095a139626cf11cfaa80e85daad293` persisted `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_AUTHORITY_V0_1.json`, status `TERMINAL_STATIC_AUDIT_AUTHORITY`, verdict `QUALIFIED`, classification `HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_EXECUTION_AUTHORITY_REVIEW_ONLY`.

It binds hosted-workflow candidate head `1a1f33df835218b7c6232e2a9078d6681081b16f`, workflow blob `71d054036e251dce50d0bcfc8429b6d875ceb9c4`, contract blob `2152e952e37fd1f22f5f38b976379540103de2ef`, static audit run `35040852174` run #1 / attempt #1, job `104620152031`, artifact `10424714637`, ZIP SHA256 `e993e323ed7c78aceece8f877d9056b0f6a8c355e1bbd1c977109f5aea56e0d6`, receipt SHA256 `b49dc127cfc6c59ed9e1b56de880c182ad38279851e0a15adfc03e7df1ecf9fa`. It never authorized dispatch.

## V0.2 defects remain historical and binding

Execution-authority compatibility run `35041244978` is terminal and classified the earlier hosted chain as runtime-binding incomplete. The later exact v0.2 candidate head `4c8a59b68791c0320840652dff65f1a106e89634` added several runtime guards, but independent source review found a deterministic consumer-schema mismatch: hosted code consumed `successor_science_authorized`; frozen PR190 producer blob `f7eff337...` emits `successor_science_authorized_by_this_receipt`. A second-order source audit also showed v0.2 did not runtime-bind a future exact terminal audit-authority blob.

Therefore v0.2 is not execution-ready regardless of any later CI color. Its runtime-binding Actions run `35044374801`, workflow `359223774`, run #1 / attempt #1 remains queued/nonterminal in the latest review and no partial result is used.

## V0.3 prospective correction — current frontier

A new prospective branch `audit/v026-r1-failure-funnel-v03-schema-runtime-closure` freezes exact head `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c`, 14 commits ahead of the previously reviewed main.

Exact v0.3 identities:
- hosted workflow blob `1b73d49539470dad89dff4aa7e660529e5f5a72a`;
- execution-authority candidate blob `c9a03bff716fac3b2a19a2e16fed08f4edcb809b`;
- independent review-confirmation candidate blob `fff04da57136b48902b9d6dad38f2d7df2e8087d`;
- frozen PR190 producer/auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`;
- v0.3 static compatibility auditor blob `47c27ab3179e9e803e945e9c7779353d18d0c4d0`;
- hosted static compatibility workflow blob `2ba18f30f78041e3b9378c2cb987e92bae15f907`;
- v0.3 machine contract blob `d6f440ac1063486cd8dbdda77d7e366c66180f6b`.

Independent source/provenance audit found that exact v0.3 prospectively closes both known v0.2 defects: it consumes exact frozen producer field `successor_science_authorized_by_this_receipt`, and the hosted workflow requires a fixed future terminal runtime-binding audit-authority path plus an exact runtime-supplied blob SHA1 and semantic back-binding to exact workflow/A/review/nonce/ref/event/attempt/policy fields. The dependency graph is acyclic. No new deterministic source-level blocker was found in this exact frozen source set.

However the authoritative hosted static compatibility run `35046173814`, workflow `359235031`, exact head `d71c8d7a...`, run #7 / attempt #1 is still **queued/nonterminal**. Its only job `104636353665` is queued and there are zero artifacts. Exact-head Actions enumeration returns exactly one run. No partial substantive values or local support receipt may substitute for a terminal hosted artifact.

Durable preterminal source audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_PRETERMINAL_SOURCE_FUNNEL_AUDIT_V0_1.md`, commit `7491389d59ad58121d4e4f9773304e92615b3261`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_PRETERMINAL_SOURCE_V0_1.md`, commit `d67e8f3316c1aa491dba299138929dd2b87ca137`.

Current-process reconciliation commit: `3b7927a445c804deb00c7798b52b2643314fcd80`.

## Current funnel position and interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> EXACT SENTINEL ATTEMPT CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> FORENSIC EVIDENCE TERMINAL -> HARDENED PR190 CONFIRMED_SCOPED -> PR193 HOSTED-WORKFLOW STATIC AUTHORITY QUALIFIED -> V0.2 RUNTIME/SCHEMA DEFECTS -> V0.3 PROSPECTIVE CORRECTION FROZEN -> EXACT HOSTED STATIC COMPATIBILITY AUDIT QUEUED/NONTERMINAL -> FAILURE-FUNNEL DISPATCH CLOSED -> FULL 107 ROW CLOSED`.

Interpretation ceiling remains governance/provenance/static implementation only. No CLASS solve or scientific response was reviewed. Green CI is not numerical science, statistical/model validity, nuisance removal or physical dark-sector evidence. Effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## Exact authorized next stage

`WAIT_FOR_AND_INDEPENDENTLY_VERIFY_EXACT_V0_3_HOSTED_STATIC_COMPATIBILITY_RUN_35046173814` only.

Next admissible sequence:
1. Do **not** dispatch or promote v0.2 or v0.3 while run `35046173814` is nonterminal.
2. Do not rerun run `35046173814`; let the existing exact-head attempt terminate.
3. If terminal success, independently verify exact run/job/attempt uniqueness, artifact count, Actions ZIP digest, inner receipt and manifest hashes, exact source/blob bindings, and zero-dispatch evidence.
4. Only after that verified terminal success may a **separate** terminal runtime-binding audit authority be authored and independently reviewed before any promotion/dispatch decision.
5. If the run fails, preserve the failure and audit it; any source correction requires a prospectively frozen successor, not rerun selection.

Until then: **never rerun run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; do not dispatch the failure funnel; do not run successor sentinel science; do not run full 107 rows; keep covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537 and all downstream statistical/model/physical science closed.**
