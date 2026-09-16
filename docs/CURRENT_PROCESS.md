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

Current reviewed default-branch baseline before this audit was main `8493f247b3095a139626cf11cfaa80e85daad293`, merge PR #193. It persists `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_AUTHORITY_V0_1.json`, status `TERMINAL_STATIC_AUDIT_AUTHORITY`, verdict `QUALIFIED`, classification `HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_EXECUTION_AUTHORITY_REVIEW_ONLY`.

PR193 authority binds hosted-workflow candidate head `1a1f33df835218b7c6232e2a9078d6681081b16f`, workflow blob `71d054036e251dce50d0bcfc8429b6d875ceb9c4`, contract blob `2152e952e37fd1f22f5f38b976379540103de2ef`, static audit run `35040852174` run #1 / attempt #1, job `104620152031`, artifact `10424714637`, ZIP SHA256 `e993e323ed7c78aceece8f877d9056b0f6a8c355e1bbd1c977109f5aea56e0d6`, receipt SHA256 `b49dc127cfc6c59ed9e1b56de880c182ad38279851e0a15adfc03e7df1ecf9fa`. It explicitly leaves failure-funnel execution, rerun, same-nonce second attempt, successor sentinel science, full 107 rows and downstream science unauthorized.

## Execution-authority runtime-binding chain

Execution-authority compatibility run `35041244978`, workflow `359203695`, head `319204c384be5b67fba9b05e85f29f5cb4198ba4`, run #1 / attempt #1, is terminal success. Job `104621354119` succeeded. Artifact `10424693735` has ZIP digest `sha256:0e4b94d8b6f1b08884870eab5aeed8883025aa7afe7704d9753cb9073f799f54`. Its substantive classification was `HOSTED_FAILURE_FUNNEL_EXECUTION_AUTHORITY_RUNTIME_BINDING_INCOMPLETE`; required corrections were prospective.

The exact v0.2 correction candidate is head `4c8a59b68791c0320840652dff65f1a106e89634`:
- hosted workflow blob `670a771e1d2e2854c33d71cc1c37ea6beea85566`;
- execution-authority candidate blob `47788695c3ab7050099ed44cacbb6f507cbbf03d`;
- review-confirmation candidate blob `f8824d107a7fbfb260e5c5946a9d05f71131c94b`;
- runtime-binding auditor blob `66f4c9352c8efa0732d625689c4ba582535dfb73`.

The candidate correctly adds runtime enforcement of `refs/heads/main`, exact authority/review/workflow blobs, exact nonce, one dispatch, run attempt 1, and retains all science prohibitions. Its independent runtime-binding Actions run `35044374801`, workflow `359223774`, run #1 / attempt #1, was still `queued` during the current Funnel Auditor review. No partial outcome or artifact from that nonterminal run was used.

## Independent source/code counterexample — terminal qualification

Independent exact-source audit found a deterministic producer/consumer receipt-schema mismatch in the v0.2 hosted workflow. After executing frozen PR190 auditor blob `f7eff337...`, the hosted workflow requires JSON key `successor_science_authorized`. The frozen producer emits `successor_science_authorized_by_this_receipt` instead. Therefore the exact hosted workflow would raise `KeyError` at post-auditor receipt validation if it reaches that step and cannot reach intended successful evidence persistence without prospective correction.

The v0.2 runtime-binding static auditor does not verify the frozen producer output schema against all hosted receipt-consumer fields, so even a later green result from run `35044374801` cannot by itself close this counterexample.

Durable audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_2_CONSUMER_SCHEMA_FUNNEL_AUDIT_V0_1.md`, commit `be24de86d097654cb2946195d8733e72ae55b0dc`.

Terminal qualification authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_2_CONSUMER_SCHEMA_QUALIFICATION_V0_1.json`, commit `6b9fccfca804b36f855c0f497da212b4c26845cb`, verdict `QUALIFIED`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_2_CONSUMER_SCHEMA_V0_1.md`, commit `1e2bcd8085d2cecc409f395fae51b7fa73d594b4`.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> SENTINEL RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> FORENSIC EVIDENCE TERMINAL -> HARDENED PR190 CONFIRMED_SCOPED -> PR193 HOSTED-WORKFLOW STATIC AUTHORITY QUALIFIED -> EXECUTION-AUTHORITY RUNTIME-BINDING BLOCKER -> V0.2 CORRECTION CANDIDATE -> NONTERMINAL RUNTIME-BINDING AUDIT + INDEPENDENT SOURCE COUNTEREXAMPLE -> V0.2 CONSUMER-SCHEMA QUALIFIED/NOT EXECUTION-READY -> FAILURE-FUNNEL DISPATCH CLOSED -> FULL 107 ROW CLOSED`.

Interpretation ceiling remains governance/provenance/static implementation only. Effect `+0/+0`; readiness `68%`; scientific frontier `67%`.

## Exact next admissible action

1. Do not dispatch exact v0.2 candidate head `4c8a59b...`, irrespective of any later green result of its incomplete static auditor.
2. Prospectively create a new exact corrected candidate head whose hosted receipt consumer uses the exact frozen producer key `successor_science_authorized_by_this_receipt` or a separately frozen equivalent schema mapping.
3. Harden the independent static auditor to verify every consumed hosted receipt key against the exact frozen PR190 producer output schema.
4. Run a fresh independent response-blind static audit of that corrected exact candidate; only a later terminal authority may consider promotion and exactly one hosted failure-funnel dispatch.
5. Never rerun science run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; no successor sentinel science; no full-107 replay or downstream science.
