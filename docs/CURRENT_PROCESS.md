# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts and terminal authorities are authoritative. Chat is not authority.

## Scientific baseline and closed boundary

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Frozen science boundary is unchanged: 107 retained rows = DES 53 + BOSS 54; alpha route tolerance `3e-10`; beta exact-target tolerance `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full-replay accounting 738 CLASS constructions. There is no full-107 execution authority. Covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Consumed sentinel first attempt and immutable forensic chain

Frozen implementation identities remain W `19907175f0f3417ddee2aba6916d961c6be02e26`, executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`, decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`, implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`, corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`, corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`, corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` consumed the one-run L gate and triggered science run `35033268924`, workflow `359060727`, run #1 / attempt #1. It failed before science at frozen W guard `assert added.count(launch)==1`; materialize-plan and lane were skipped; zero science artifacts exist and no CLASS scientific response, covariance read or sentinel classification exists. Never rerun `35033268924`, never create a same-nonce second attempt, and never modify/remove/recreate final L.

Forensic producer head `c5502bc124f502cb4ef1c19300fcdf87f260089b`, run `35033678449` run #3 / attempt #1, job `104597783801`, is terminal success. Artifact `10422924571` has ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`; producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`. Hardened PR190 exact head `5731b605afdc35bd85d3a2014a9e135719a07697`, auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`, contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`, and independent re-audit run `35036894735` remain terminal static/governance evidence only.

PR #193 merge `8493f247b3095a139626cf11cfaa80e85daad293` persisted terminal hosted-workflow static-audit authority with verdict `QUALIFIED`; it never authorized dispatch.

## Historical v0.2 defects

V0.2 remains not execution-ready. Durable terminal qualification records the frozen producer/consumer schema mismatch (`successor_science_authorized` vs exact producer `successor_science_authorized_by_this_receipt`) and the missing exact future terminal runtime-binding authority binding. Any later CI color for the frozen v0.2 head cannot erase those historical defects.

## V0.3 prospective correction and new dispatch-history qualification

Exact frozen v0.3 head remains `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c` on `audit/v026-r1-failure-funnel-v03-schema-runtime-closure`.

Exact identities:
- hosted workflow blob `1b73d49539470dad89dff4aa7e660529e5f5a72a`;
- execution-authority candidate blob `c9a03bff716fac3b2a19a2e16fed08f4edcb809b`;
- review-confirmation candidate blob `fff04da57136b48902b9d6dad38f2d7df2e8087d`;
- frozen PR190 producer/auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`;
- v0.3 static compatibility auditor blob `47c27ab3179e9e803e945e9c7779353d18d0c4d0`;
- hosted static compatibility workflow blob `2ba18f30f78041e3b9378c2cb987e92bae15f907`;
- v0.3 machine contract blob `d6f440ac1063486cd8dbdda77d7e366c66180f6b`.

V0.3 prospectively closes the known v0.2 receipt-key mismatch and adds an acyclic exact future terminal runtime-binding audit-authority hook. Those controls survive.

The authoritative hosted static compatibility run `35046173814`, workflow `359235031`, exact head `d71c8d7a...`, run #7 / attempt #1 remains queued/nonterminal. Its only job `104636353665` is queued with runner id 0, empty runner identity, no steps and zero artifacts. Exact-head enumeration returns exactly one run. No partial substantive output or local receipt is admissible.

Independent source audit has now found a further fail-closed provenance defect in the frozen v0.3 one-dispatch guard. The hosted workflow enumerates currently visible `workflow_dispatch` runs and requires exactly one visible run, current run id, attempt 1 and `main`, but it does **not** require monotonic workflow `run_number==1`. Therefore an earlier dispatch that is no longer present in current visible Actions history does not prevent a later `run_number>1` dispatch from satisfying the frozen guard. The workflow also snapshots dispatch history before the main failure-funnel work and does not require a fresh post-run live-history closure, leaving a TOCTOU gap for a late duplicate dispatch.

Durable audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_DISPATCH_HISTORY_GUARD_AUDIT_V0_1.md`, commit `65ea92addfb28bea19947971774728c0d647bd59`.

Terminal qualification authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_DISPATCH_HISTORY_QUALIFICATION_V0_1.json`, verdict `QUALIFIED`, commit `853a50ebd2e652e090815291e9c65ff1731468a0`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_DISPATCH_HISTORY_V0_1.md`, commit `b493da52890f4cc18889eef0acea1e67d5394e2e`.

A later green terminal outcome from exact static run `35046173814` cannot authorize frozen v0.3 dispatch because the frozen static auditor does not test the new run-number/history counterexample. Do not rerun `35046173814`; if it terminates, preserve/audit it as historical exact-v0.3 evidence only.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> SENTINEL RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> FORENSIC EVIDENCE TERMINAL -> HARDENED PR190 CONFIRMED_SCOPED -> PR193 STATIC AUTHORITY QUALIFIED -> V0.2 RUNTIME/SCHEMA DEFECTS -> V0.3 SCHEMA/RUNTIME CORRECTION FROZEN -> V0.3 DISPATCH-HISTORY PROVENANCE QUALIFIED -> FAILURE-FUNNEL DISPATCH CLOSED -> FULL 107 ROW CLOSED`.

Interpretation ceiling remains governance/provenance/static implementation only. Effect `+0/+0`; readiness `68%`; scientific frontier `67%`.

## Exact next admissible action

1. Do not promote or dispatch frozen v0.3 regardless of later CI color.
2. Do not rerun static run `35046173814`; preserve its eventual terminal state as historical evidence only.
3. Prospectively freeze a new successor source set that requires API and runtime workflow `run_number==1` in addition to attempt 1, retains exact workflow/current-id/main/ref/nonce/blob bindings, and specifies a fresh **post-run terminal live dispatch-history audit** rejecting any history other than the single authorized run #1 / attempt #1.
4. Harden the successor static auditor to verify those exact first-dispatch and post-run-history invariants; run a fresh independent response-blind static audit on the new exact successor.
5. Never rerun science run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; keep successor sentinel science, full 107 rows and all downstream gates closed.
