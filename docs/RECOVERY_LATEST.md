# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-16. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Terminal scientific/numerical baseline

V0.25 remains terminal: `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Numerical/reproducibility chain remains terminal through V0.25; statistical/model and physical dark-sector layers remain unopened.

V0.26 R1 is prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain: 107 rows = DES 53 + BOSS 54; alpha route `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. None of the current governance work changes those values.

## Consumed sentinel and immutable forensic chain

Frozen identities remain W `19907175f0f3417ddee2aba6916d961c6be02e26`; executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`; decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`; implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`; corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`; corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`; corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` triggered science run `35033268924`, workflow `359060727`, run #1 / attempt #1. It is terminal failure before science at frozen W event guard `assert added.count(launch)==1`; materialize-plan and lane were skipped; science artifact count is zero; no CLASS scientific response, covariance or sentinel classification exists.

Historical fail-closed authority remains binding: **never rerun run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L.**

Forensic run `35033678449`, run #3 / attempt #1, job `104597783801`, head `c5502bc124f502cb4ef1c19300fcdf87f260089b`, is terminal success. Exactly one artifact `10422924571`; ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`; producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`. Hardened PR190 head `5731b605afdc35bd85d3a2014a9e135719a07697`, auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`, contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`, and independent re-audit run `35036894735` remain terminal static/governance evidence only.

PR #193 merge `8493f247b3095a139626cf11cfaa80e85daad293` persisted a terminal hosted-workflow static authority with verdict `QUALIFIED`; dispatch was never authorized.

## Historical v0.2 defects

V0.2 remains not execution-ready. Durable qualification records its deterministic receipt consumer mismatch and missing exact future terminal runtime-binding audit-authority binding. Later CI color cannot erase these frozen historical defects.

## V0.3 frozen source set

Exact prospective v0.3 head: `d71c8d7a9e0d98369fdd2e46c843314e0307cd1c`.

Exact identities:
- hosted workflow `1b73d49539470dad89dff4aa7e660529e5f5a72a`;
- execution-authority candidate `c9a03bff716fac3b2a19a2e16fed08f4edcb809b`;
- review-confirmation candidate `fff04da57136b48902b9d6dad38f2d7df2e8087d`;
- frozen PR190 producer/auditor `f7eff337e511baa25d51e5b0c333a97534e1bbc3`;
- v0.3 static compatibility auditor `47c27ab3179e9e803e945e9c7779353d18d0c4d0`;
- hosted static compatibility workflow `2ba18f30f78041e3b9378c2cb987e92bae15f907`;
- machine contract `d6f440ac1063486cd8dbdda77d7e366c66180f6b`.

V0.3 prospectively closes the known v0.2 wrong receipt key and adds an acyclic exact runtime-binding audit-authority hook. Those corrections survive.

The authoritative hosted static compatibility run remains `35046173814`, workflow `359235031`, exact head `d71c8d7a...`, run #7 / attempt #1. At latest review it is still `queued/nonterminal`; only job `104636353665` is queued with runner id 0, empty runner identity, no steps and zero artifacts. Exact-head run count is one. No partial output is authority.

## New terminal audit qualification — dispatch-history provenance

Independent response-blind source review found a further concrete provenance defect in frozen v0.3.

The hosted one-dispatch guard enumerates currently visible `workflow_dispatch` runs for the exact workflow path and requires exactly one visible run, current run id, attempt 1 and main branch. It does **not** require monotonic workflow `run_number==1` / runtime `GITHUB_RUN_NUMBER==1`. Thus an earlier dispatch that is absent from current visible Actions history can be followed by a later run with `run_number>1` that still passes the frozen visible-list uniqueness guard.

A second concrete gap is temporal: dispatch history is captured before main failure-funnel work and artifact persistence. A late duplicate dispatch created after that snapshot is not represented in the stored history evidence. No fresh post-run live dispatch-history closure is required by frozen v0.3 or its frozen static auditor.

Therefore frozen v0.3 does not provide tamper-evident historical first-dispatch identity or post-run exact-one-dispatch closure. A future green terminal result from run `35046173814` cannot repair this source-level defect because the frozen static auditor does not test these invariants.

Durable audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_DISPATCH_HISTORY_GUARD_AUDIT_V0_1.md`, commit `65ea92addfb28bea19947971774728c0d647bd59`.

Terminal qualification authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_DISPATCH_HISTORY_QUALIFICATION_V0_1.json`, commit `853a50ebd2e652e090815291e9c65ff1731468a0`, verdict `QUALIFIED`, classification `V0_3_EXACT_ONE_DISPATCH_PROVENANCE_NOT_TAMPER_EVIDENT_OR_POST_RUN_CLOSED`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_DISPATCH_HISTORY_V0_1.md`, commit `b493da52890f4cc18889eef0acea1e67d5394e2e`.

Current-process reconciliation commit: `76969be63fc7291dfd24841848c519f0c63402a2`.

## Current funnel position and interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> SENTINEL FIRST ATTEMPT CONSUMED/PRE-SCIENCE FAILURE -> FORENSIC EVIDENCE TERMINAL -> HARDENED PR190 CONFIRMED_SCOPED -> PR193 STATIC AUTHORITY QUALIFIED -> V0.2 RUNTIME/SCHEMA DEFECTS -> V0.3 SCHEMA/RUNTIME CORRECTION FROZEN -> V0.3 DISPATCH-HISTORY PROVENANCE QUALIFIED -> FAILURE-FUNNEL DISPATCH CLOSED -> FULL 107 ROW CLOSED`.

Interpretation ceiling remains governance/provenance/static implementation only. No CLASS solve or scientific response was reviewed. Green CI is not numerical science, statistical/model validity, nuisance removal or physical dark-sector evidence. Effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## Exact authorized next stage

`PROSPECTIVELY_FREEZE_SUCCESSOR_FAILURE_FUNNEL_CANDIDATE_WITH_TAMPER_EVIDENT_FIRST_DISPATCH_AND_POST_RUN_HISTORY_CLOSURE` only.

Next admissible sequence:
1. Do **not** promote or dispatch frozen v0.3 regardless of later CI color.
2. Do not rerun exact static run `35046173814`; preserve its eventual terminal state as historical exact-v0.3 evidence only.
3. Create a new prospectively frozen successor requiring API and runtime workflow `run_number==1` plus attempt 1, retaining exact workflow path/current-id/main/ref/nonce/blob checks.
4. Freeze a fresh **post-run terminal live dispatch-history audit** that rejects any workflow-path dispatch history other than the single authorized run #1 / attempt #1. A final in-run recheck may be added, but does not replace the post-run control.
5. Harden the successor static auditor to verify these exact invariants and run a fresh independent response-blind static audit before any promotion/dispatch decision.
6. Never rerun science run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; do not run successor sentinel science; do not run full 107 rows; keep covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537 and all downstream statistical/model/physical science closed.
