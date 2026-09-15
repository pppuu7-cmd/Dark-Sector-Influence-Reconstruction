# DSIR authoritative recovery — latest

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts, terminal authorities, `docs/CURRENT_PROCESS.md`, and this file are the durable source of truth. Chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains the prospectively frozen successor: preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`, contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`, 107 rows (DES 53/BOSS 54), alpha canonical-32769 tolerance `3e-10`, beta exact-target tolerance `1e-12`, scientific strict `<1e-3`, technical strict `<1e-5`, exact-node binding `<=1e-12`, full-replay accounting 738 CLASS constructions.

Full 107-row replay, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Frozen implementation and corrected launch package

Frozen W/executor/decision identities:

- W `19907175f0f3417ddee2aba6916d961c6be02e26`;
- executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`.

Historical A/Q schema blockers were corrected by the governance-only A-L-Q v0.2 package:

- corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`;
- corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`;
- corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

Correction static run `35025081430` and independent correction funnel run `35025283328` passed. Terminal correction-funnel confirmation authority blob `019efc37f9a1110e70574c381482b1bef3310700` authorized authority-first corrected A/Q replacement without L.

PR #184 merge `41ef654d7552b670c20d3202249d7687bae5f870` replaced final A/Q exactly. Separate post-replacement hosted audit `35032839418` and independent funnel `35032991806` passed and observed zero sentinel-science runs at the replacement head.

A separate one-run L-gate authority was promoted by PR #185 merge `2ca2d4c35f9dcfe2be00e573598e6189f987508d`:

`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_EXACT_L_GATE_AUTHORITY_V0_1.json`, blob `1c1819ee6aa7a48597770d9bc9116185d061a49c`.

It authorizes one exact new-file L trigger / one first attempt only, with rerun forbidden and full-107 false.

## Exact L trigger and first attempt

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` created exact final L as the only runtime file change:

`docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json`, blob `fa7014435f0a5688def2124898ddd01d0c0183aa`.

This produced exactly one sentinel workflow run:

- run `35033268924`;
- workflow `layerb-beta-v026-r1-sentinel-science-v0-1`;
- event `push`;
- run #1 / attempt #1;
- head `9a333294f3acb80201c5f6ed5b74918c1c767232`;
- terminal conclusion `failure`.

This attempt is consumed. **Never rerun it.**

## Failure localization: pre-science event guard

Hosted job outcomes:

- authorize job `104596462857`: failure;
- materialize-plan: skipped;
- lane matrix: skipped;
- decision job `104596495504`: failure due to missing authorization;
- decision finalizer: skipped;
- artifact count: 0.

No CLASS scientific solve, lane operand, substantive scientific response or sentinel decision artifact exists from run `35033268924`.

Authorize log ends at embedded Python `<stdin>` line 48. Exact frozen W maps line 48 to:

`assert added.count(launch)==1`

All package/blob predicates before that line were reached before the failure and independently reproduce as passing. Repository state is also correct: staging commit `657e5d6b2fe3ad7f7c11bcd2af873cffe800cc96` and merge `9a333294f3acb80201c5f6ed5b74918c1c767232` both add exact L; net first-parent-to-merge diff is exactly one added L.

The defect is in event validation. Frozen W uses `github.event.commits[*].added`. GitHub Actions documents that its push payload does **not include** commit-level `added`, `removed`, and `modified` attributes. Source checked 2026-09-16:

`https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#push`

Because W uses `c.get('added', [])`, the missing attribute becomes an empty list and effective `added.count(launch)` is 0. The frozen guard therefore fails before science even for the correct L-only repository change.

This is an implementation/event-contract failure, not a numerical/scientific result.

## Interim fail-closed authority on main

PR #187 merge `f85d679fd4e8a16b83e7b44fd74911149e868746` persisted the preliminary audit and interim authority:

- audit blob `387e13ac2f1c88d0405c7b3f7a41886cd1e276af`;
- interim authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAIL_CLOSED_INTERIM_V0_1.json`, blob `8f898f3579ac55db4bfd3b7cc6a12cad04a4a613`.

It forbids rerun of `35033268924`, same-nonce second attempt, final-L modification/removal/recreation, full replay and downstream science. It does not claim a sentinel scientific PASS or refutation.

## Current evidence gate

Hosted forensic branch: `audit/v026-r1-sentinel-first-attempt-forensic`.

Exact current forensic head: `c5502bc124f502cb4ef1c19300fcdf87f260089b`. Exact forensic run: `35033678449`; currently pending GitHub-hosted runner execution. It will persist run/jobs/artifacts snapshots and authorize log, reproduce all pre-event package assertions, map traceback line 48 to exact W source, and record the documented Actions push-payload file-list omission.

After immutable forensic evidence, perform a separate independent first-attempt failure funnel. Only then persist a terminal first-attempt result authority.

## Recovery invariant

Do not rerun `35033268924`. Do not use rerun-failed-jobs or rerun-job actions. Do not modify, remove, or recreate final L. Do not silently patch W and call that a continuation of attempt #1. Full 107-row replay remains closed.

Any future scientific sentinel must be a **new prospectively frozen successor launch-governance package/workflow with a new trigger identity**, independently audited before activation. A corrected successor guard should validate the aggregate `before...after` repository diff (or equivalent first-parent tree diff), not absent commit-level file lists in the Actions push payload.

Current funnel:

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> CORRECTED A/Q PROMOTED -> EXACT L-GATE AUTHORITY -> EXACT L TRIGGER -> RUN #1/ATTEMPT #1 CONSUMED -> AUTHORIZE EVENT-GUARD FAILURE BEFORE SCIENCE -> RERUN FORBIDDEN -> FORENSIC/FUNNEL TERMINALIZATION PENDING -> FULL 107 ROW CLOSED`.

Effect remains `+0/+0`; readiness `68%`; scientific frontier `67%`.
