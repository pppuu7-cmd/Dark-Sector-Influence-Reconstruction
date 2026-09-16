# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts and terminal authorities are authoritative. Chat is not authority.

## Scientific baseline and closed boundary

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains the prospectively frozen numerical/reproducibility successor under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Frozen science boundary remains unchanged: 107 retained rows = DES 53 + BOSS 54; alpha route tolerance `3e-10`; beta exact-target tolerance `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full-replay accounting 738 CLASS constructions.

There is still no full-107 execution authority. Covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Frozen sentinel and consumed first attempt

Frozen implementation identities remain W `19907175f0f3417ddee2aba6916d961c6be02e26`, executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`, decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`, implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`, corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`, corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`, corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` consumed the exact-one-run L-gate authorization and triggered sentinel science workflow run `35033268924`, workflow id `359060727`, run #1 / attempt #1. That attempt is terminal `failure` before science: authorize job `104596462857` failed, materialize-plan and lane jobs were skipped, decision job `104596495504` failed from missing current-run authorization, and science-run artifact count is zero. No CLASS scientific solve, scientific response, covariance read or sentinel decision occurred.

The exact failure is frozen W embedded Python line 48, `assert added.count(launch)==1`. Repository first-parent/staging diffs contain exactly one added L and all package/blob assertions before this guard pass. The Actions push-event payload used inside workflows omits commit-level `added/modified/removed`; frozen W falls back to `[]`, so the guard rejects the correct L-only trigger before science. This is a pre-science workflow/event-contract implementation failure, not a numerical or scientific result.

Historical interim authority blob `8f898f3579ac55db4bfd3b7cc6a12cad04a4a613` remains fail-closed: never rerun `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; full replay and downstream science remain forbidden.

## Terminal forensic producer

Exact forensic producer is terminal and immutable: branch `audit/v026-r1-sentinel-first-attempt-forensic`, head `c5502bc124f502cb4ef1c19300fcdf87f260089b`, auditor blob `63b6a0db41ff5e0e3c36be605596fb1c5aee0f1d`, workflow blob `4d09b78d3a586d3c4f7e42573a7bdac4454d3a48`, run `35033678449` run #3 / attempt #1, job `104597783801`, terminal success.

Its single artifact is id `10422924571`, ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`. Producer receipt `first_attempt_forensic_audit.json` is 2374 bytes, SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`. Receipt classification is `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`. This is evidence, not yet terminal first-attempt result authority.

## PR #190 is now hardened and frozen for re-audit

The earlier reviewed PR190 head `d38e9825...` is historical. The current open/draft PR #190 has been prospectively hardened under qualification authority blob `74b10d5d326ec6984edec986fe1bbc368a73b4f6`.

**Frozen target head for the current re-audit:** `5731b605afdc35bd85d3a2014a9e135719a07697`.

It still changes exactly two non-runtime files only:

- independent failure-funnel auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`;
- machine contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`.

The hardened contract freezes forensic artifact id `10422924571`, ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`, receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e` and requires a future live exact-head enumeration that accepts only science workflow `359060727`, head `9a333294f3acb80201c5f6ed5b74918c1c767232`, run `35033268924`, run #1 / attempt #1. Any duplicate or rerun must block.

Artifact checking is now recursive and fail-closed: exactly seven frozen ZIP members, exactly seven extracted relative paths, no nested extras, exact `safe/...` SHA256 manifest names/cardinality, no basename normalization/collision.

PR #190 remains **draft and non-executable**. No hosted failure-funnel workflow has been authorized or authored from this hardened target.

## Current independent static re-audit gate

A separate response-blind re-audit branch exists from main: `audit/v026-r1-first-attempt-failure-funnel-pr190-reaudit`.

Frozen re-audit identities:

- re-auditor blob `4bf1b3867a953b61e62225735883628869218ded`;
- hosted static re-audit workflow blob `5db1a2580c22ca2c65d9b0f0d87aa42940f402bd`;
- exact re-audit head `ece06ed801c65aa336a06ee8b421e9812b8e1e58`.

The audit branch differs from its `main` base only by those two re-audit files; it contains no runtime/science modifications. The re-auditor checks the exact frozen PR190 head/blobs, two-file target diff, compileability and adversarial fixtures for duplicate/rerun selection, nested ZIP extras, nested extracted-tree extras and basename-collision manifests. It does not execute the failure funnel or any science.

Hosted re-audit run is **`35036894735`**, job **`104607902297`**, run #1 / attempt #1. At the latest check it is `queued`, conclusion null. Repository-wide Actions also has multiple queued runs, so this is currently an infrastructure scheduling state, not an audit verdict.

Do not mutate PR190 head `5731b605...` while this exact re-audit is pending; doing so would invalidate the frozen target. Do not create a failure-funnel workflow while re-audit is pending.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> CORRECTED A/Q PROMOTED -> EXACT L-GATE AUTHORITY -> EXACT L TRIGGER -> RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> HISTORICAL INTERIM BLOCKED -> FORENSIC RUN #3 TERMINAL SUCCESS -> PR190 ORIGINAL CANDIDATE QUALIFIED WITH CORRECTIONS -> PR190 HARDENED EXACT HEAD 5731b605 -> INDEPENDENT STATIC RE-AUDIT RUN 35036894735 QUEUED -> FULL 107 ROW CLOSED`.

## Exact next admissible action

1. Observe exact re-audit run `35036894735`; do not rerun it merely because it is queued.
2. If it completes success, fetch/download its single artifact, independently hash ZIP and inner receipt, verify expected `QUALIFIED` classification and every fail-closed counterexample check.
3. Only after immutable hosted re-audit evidence passes, persist a **separate re-audit qualification authority** on main. That authority may at most authorize authoring/auditing a separately frozen hosted failure-funnel workflow; it must not itself authorize failure-funnel execution, terminal first-attempt result authority, successor science or full-107.
4. If the re-audit fails, inspect the exact failure and keep PR190/failure-funnel execution blocked. Do not silently mutate the frozen target and reuse the same audit evidence.
5. Never rerun sentinel run `35033268924`; never modify/remove/recreate final L; any future science sentinel requires separately prospectively frozen successor governance with a new trigger identity and independent pre-activation audit.

Effect remains `+0/+0`; readiness `68%`; scientific frontier `67%`.
