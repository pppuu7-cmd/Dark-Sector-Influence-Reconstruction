# DSIR authoritative recovery — latest

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts, terminal authorities, `docs/CURRENT_PROCESS.md`, and this file are the durable source of truth. Chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains the prospectively frozen numerical/reproducibility successor under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Frozen criteria remain: 107 rows = DES 53 + BOSS 54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full 107-row replay, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Frozen implementation and launch package

Sentinel W `19907175f0f3417ddee2aba6916d961c6be02e26`; executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`; decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`; implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`; corrected A/L/Q = `1c9945dd00b137f3e202efa14bf4112fffebf8af` / `fa7014435f0a5688def2124898ddd01d0c0183aa` / `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` consumed the one authorized first attempt and triggered science workflow run `35033268924`, workflow `359060727`, run #1 / attempt #1. The run failed before science: authorize `104596462857` failed, materialize-plan/lane skipped, decision `104596495504` failed from absent current-run authorization, science artifacts = 0. No CLASS solve, scientific response, covariance read or sentinel scientific classification exists.

Failure is frozen W event guard line 48: `assert added.count(launch)==1`. Repository diff is correct L-only; the Actions push payload omits commit-level file-list fields used by W, so `c.get('added', [])` yields zero. This is a pre-science workflow/event-contract failure only.

Historical interim authority blob `8f898f3579ac55db4bfd3b7cc6a12cad04a4a613` remains binding: **never rerun `35033268924`; never use rerun-failed-jobs/rerun-job; never create same-nonce attempt; never modify/remove/recreate final L; full-107 and downstream science remain forbidden.**

## Immutable forensic evidence

Exact forensic producer is terminal success:

- branch `audit/v026-r1-sentinel-first-attempt-forensic`;
- head `c5502bc124f502cb4ef1c19300fcdf87f260089b`;
- auditor `63b6a0db41ff5e0e3c36be605596fb1c5aee0f1d`;
- workflow `4d09b78d3a586d3c4f7e42573a7bdac4454d3a48`;
- run `35033678449`, run #3 / attempt #1;
- job `104597783801` success;
- artifact `10422924571`;
- ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`;
- producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`.

Producer verdict is `TERMINAL_BLOCKED` / `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`. It is immutable evidence but not by itself the independent terminal first-attempt authority.

## PR #190 current hardened target — do not mutate while re-audit is pending

The old reviewed PR190 head `d38e9825...` is historical. Qualification authority blob `74b10d5d326ec6984edec986fe1bbc368a73b4f6` authorized prospective hardening plus fresh static re-audit only.

Current PR #190 is open/draft at exact frozen head **`5731b605afdc35bd85d3a2014a9e135719a07697`** and changes exactly two non-runtime files:

- hardened independent failure-funnel auditor blob **`f7eff337e511baa25d51e5b0c333a97534e1bbc3`**;
- hardened machine contract blob **`3369e5cdd2086ca22dca6bfa575054286fd1dcd7`**.

The hardened candidate fixes all corrections required by the prior audit:

1. forensic artifact id / ZIP SHA256 / receipt SHA256 are exact and non-null;
2. failure-funnel execution would require a fresh live exact-head enumeration and accept only workflow `359060727`, head `9a333294f3acb80201c5f6ed5b74918c1c767232`, run `35033268924`, run #1 / attempt #1; duplicate/rerun blocks;
3. artifact member/extracted-tree checks are recursive and require exactly seven relative paths, rejecting nested extras;
4. SHA256 manifests require exact `safe/...` relative names/cardinality with no basename collision normalization;
5. any future hosted failure-funnel workflow must make exact historical SHAs available via full graph/explicit fetch.

The PR remains intentionally non-executable pending the independent re-audit below. Do not add a hosted failure-funnel workflow to PR190 now.

## Current gate: independent static re-audit of hardened PR #190

Independent branch: `audit/v026-r1-first-attempt-failure-funnel-pr190-reaudit`.

Frozen identities:

- re-auditor blob `4bf1b3867a953b61e62225735883628869218ded`;
- static re-audit workflow blob `5db1a2580c22ca2c65d9b0f0d87aa42940f402bd`;
- exact audit head `ece06ed801c65aa336a06ee8b421e9812b8e1e58`.

That branch differs from its main base only by the auditor and static workflow. It executes no failure funnel and no science. Its adversarial checks cover exact target bindings, duplicate/rerun selection, nested ZIP extras, nested extracted-tree extras and manifest basename collisions.

Hosted run **`35036894735`**, job **`104607902297`**, run #1 / attempt #1 is the only authoritative hosted re-audit attempt for this frozen target. Latest observed status: **queued**, conclusion null. Multiple repository Actions runs are also queued; queued status is not a PASS or failure verdict.

Do not mutate target PR190 head `5731b605...`, re-audit head `ece06ed8...`, or create another duplicate re-audit while this run is pending solely because of scheduler delay.

## Exact continuation procedure

1. Read current `main` and check run `35036894735` first.
2. If run remains queued/in-progress, preserve the frozen target and do response-blind supporting work only. Do not execute failure funnel, do not write terminal authority, do not alter science/runtime objects.
3. If run completes `success`, require exactly one re-audit artifact; download and independently hash its ZIP; verify the inner receipt and SHA manifest; require verdict `QUALIFIED`, classification `PR190_HARDENED_FAILURE_FUNNEL_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_HOSTED_WORKFLOW_AUTHORING_ONLY`, exact target head/blobs and all adversarial fail-closed checks true.
4. Only after step 3 passes, persist a **separate static re-audit qualification authority on main**. Its authorization ceiling is limited to authoring/auditing a separately frozen hosted failure-funnel workflow. It must not authorize the failure-funnel execution itself, terminal first-attempt result authority, rerun, same-nonce attempt, successor science or full-107.
5. If re-audit fails, inspect the exact failure and keep PR190/failure-funnel execution blocked. Any candidate correction requires a new frozen target head and a fresh independent audit; never reuse evidence from `35036894735` for a mutated target.
6. After a future separate hosted failure-funnel workflow is itself frozen/audited/authorized, its execution must live-enumerate exact science run history and independently verify immutable forensic artifact provenance. Only a terminal independent failure-funnel PASS may make terminal first-attempt result authority admissible.
7. Any future scientific sentinel is a separate prospective successor with a new trigger identity. Do not patch W and call it attempt #1 continuation.

## Current funnel

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> CORRECTED A/Q PROMOTED -> EXACT L-GATE AUTHORITY -> EXACT L TRIGGER -> RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> HISTORICAL INTERIM BLOCKED -> FORENSIC RUN #3 TERMINAL SUCCESS -> PR190 ORIGINAL CANDIDATE QUALIFIED WITH CORRECTIONS -> PR190 HARDENED HEAD 5731b605 -> INDEPENDENT STATIC RE-AUDIT RUN 35036894735 QUEUED -> FULL 107 ROW CLOSED`.

Effect remains `+0/+0`; readiness `68%`; scientific frontier `67%`.
