# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts and terminal authorities are authoritative. Chat is not authority.

## Scientific baseline and closed boundary

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Frozen science boundary is unchanged: 107 retained rows = DES 53 + BOSS 54; alpha route tolerance `3e-10`; beta exact-target tolerance `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full-replay accounting 738 CLASS constructions. No governance correction below changes these values.

There is no full-107 execution authority. Covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Frozen sentinel and consumed first attempt

Frozen implementation identities remain W `19907175f0f3417ddee2aba6916d961c6be02e26`, executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`, decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`, implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`, corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`, corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`, corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` consumed the one-run L gate and triggered science run `35033268924`, workflow `359060727`, run #1 / attempt #1. It failed before science at frozen W guard `assert added.count(launch)==1`; materialize-plan and lane were skipped; there are zero science artifacts and no CLASS scientific response, covariance read or sentinel classification. Historical fail-closed authority remains binding: never rerun `35033268924`, never create a same-nonce second attempt, and never modify/remove/recreate final L.

## Immutable forensic and hardened PR190 evidence

Forensic producer head `c5502bc124f502cb4ef1c19300fcdf87f260089b`, run `35033678449` run #3 / attempt #1, job `104597783801`, is terminal success. Single artifact `10422924571` has ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`; producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`. This is pre-science forensic evidence, not a science PASS.

Hardened open/draft PR #190 exact head remains `5731b605afdc35bd85d3a2014a9e135719a07697`; failure-funnel auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`; contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`. Independent hardened-PR190 re-audit run `35036894735` is terminal success. Funnel Auditor confirmation authority blob `d2fe264e2866b9f490a7523a32f341fb7cc08d0b` has verdict `CONFIRMED_SCOPED`. This authorizes hosted-workflow authoring/auditing only, not execution.

## PR #193 hosted-workflow static authority — terminal

Main merge `8493f247b3095a139626cf11cfaa80e85daad293` persisted terminal hosted-workflow static-audit authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_AUTHORITY_V0_1.json`, status `TERMINAL_STATIC_AUDIT_AUTHORITY`, verdict `QUALIFIED`, classification `HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_EXECUTION_AUTHORITY_REVIEW_ONLY`.

It binds candidate head `1a1f33df835218b7c6232e2a9078d6681081b16f`, workflow blob `71d054036e251dce50d0bcfc8429b6d875ceb9c4`, contract blob `2152e952e37fd1f22f5f38b976379540103de2ef`, static audit run `35040852174` run #1 / attempt #1, job `104620152031`, artifact `10424714637`, ZIP SHA256 `e993e323ed7c78aceece8f877d9056b0f6a8c355e1bbd1c977109f5aea56e0d6`, receipt SHA256 `b49dc127cfc6c59ed9e1b56de880c182ad38279851e0a15adfc03e7df1ecf9fa`. Failure-funnel execution and all science remain unauthorized.

## V0.2 runtime-binding and schema defects

Execution-authority compatibility run `35041244978`, workflow `359203695`, head `319204c384be5b67fba9b05e85f29f5cb4198ba4`, run #1 / attempt #1, is terminal success. Its substantive classification was `HOSTED_FAILURE_FUNNEL_EXECUTION_AUTHORITY_RUNTIME_BINDING_INCOMPLETE`.

The exact v0.2 correction candidate head `4c8a59b68791c0320840652dff65f1a106e89634` added ref/blob/nonce/attempt binding, but independent source review found a deterministic producer/consumer mismatch: the hosted workflow consumed `successor_science_authorized` while frozen producer blob `f7eff337...` emits `successor_science_authorized_by_this_receipt`. The v0.2 static auditor also did not verify every consumed receipt field against the exact frozen producer schema. Durable qualification: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_2_CONSUMER_SCHEMA_QUALIFICATION_V0_1.json`, verdict `QUALIFIED`.

A second-order source audit additionally showed that v0.2 only required the future hosted runtime-binding audit procedurally; it did not runtime-bind a future exact terminal audit-authority blob. V0.2 is therefore not execution-ready even if its still-nonterminal run `35044374801` later becomes green. Do not dispatch it.

## V0.3 prospective correction — frozen source set, hosted audit nonterminal

A new prospective branch `audit/v026-r1-failure-funnel-v03-schema-runtime-closure` is 14 commits ahead of the previously reviewed main and freezes exact head `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c`.

Exact v0.3 identities:
- hosted workflow blob `1b73d49539470dad89dff4aa7e660529e5f5a72a`;
- execution-authority candidate blob `c9a03bff716fac3b2a19a2e16fed08f4edcb809b`;
- review-confirmation candidate blob `fff04da57136b48902b9d6dad38f2d7df2e8087d`;
- frozen PR190 producer/auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`;
- v0.3 static compatibility auditor blob `47c27ab3179e9e803e945e9c7779353d18d0c4d0`;
- hosted static compatibility workflow blob `2ba18f30f78041e3b9378c2cb987e92bae15f907`;
- v0.3 machine contract blob `d6f440ac1063486cd8dbdda77d7e366c66180f6b`.

Independent preterminal source audit confirms only that the two known v0.2 defects are prospectively closed in this exact source set: the consumer now uses exact frozen producer key `successor_science_authorized_by_this_receipt`, and the hosted workflow now requires a fixed future terminal runtime-binding audit-authority path plus an exact runtime-supplied blob hash and semantic back-bindings to W/A/review/nonce/ref/event. No new deterministic source-level blocker was found in the exact frozen v0.3 set.

However the authoritative hosted static compatibility run `35046173814`, workflow `359235031`, exact head `d71c8d7a...`, run #7 / attempt #1 remains `queued`. Its only job `104636353665` is queued and the run has zero artifacts. Exact-head Actions enumeration currently returns exactly one run. No partial substantive output is admissible and no hosted receipt exists yet.

Durable preterminal audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_PRETERMINAL_SOURCE_FUNNEL_AUDIT_V0_1.md`, commit `7491389d59ad58121d4e4f9773304e92615b3261`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_PRETERMINAL_SOURCE_V0_1.md`, commit `d67e8f3316c1aa491dba299138929dd2b87ca137`.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> SENTINEL RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> FORENSIC EVIDENCE TERMINAL -> HARDENED PR190 CONFIRMED_SCOPED -> PR193 HOSTED-WORKFLOW STATIC AUTHORITY QUALIFIED -> V0.2 RUNTIME/SCHEMA DEFECTS -> V0.3 PROSPECTIVE CORRECTION FROZEN -> EXACT HOSTED STATIC COMPATIBILITY AUDIT QUEUED/NONTERMINAL -> FAILURE-FUNNEL DISPATCH CLOSED -> FULL 107 ROW CLOSED`.

Interpretation ceiling remains governance/provenance/static implementation only. Effect `+0/+0`; readiness `68%`; scientific frontier `67%`.

## Exact next admissible action

1. Do not dispatch v0.2 or v0.3 and do not promote the v0.3 source set while run `35046173814` is nonterminal.
2. Do not rerun exact run `35046173814`; wait for its existing attempt to become terminal.
3. If terminal success: independently verify exact run/job/attempt uniqueness, artifact count, Actions ZIP digest, inner receipt and manifest hashes, exact bound blobs, and zero-dispatch evidence before authoring any separate terminal runtime-binding audit authority.
4. If terminal failure: preserve the failure, audit it, and require a prospective successor if source changes are needed; do not tune the frozen exact head and select a rerun.
5. Never rerun science run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; no successor sentinel science; no full-107 replay or downstream science.
