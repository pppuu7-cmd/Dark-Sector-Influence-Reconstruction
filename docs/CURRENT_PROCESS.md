# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts and terminal authorities are authoritative. Chat is not authority.

## Scientific baseline

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains the prospectively frozen numerical/reproducibility successor:

- preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`;
- contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`;
- retained denominator 107 rows = DES 53 + BOSS 54;
- alpha route tolerance `3e-10`;
- beta exact-target route tolerance `1e-12`;
- scientific strict `<1e-3`;
- technical strict `<1e-5`;
- requested-node binding `<=1e-12`;
- full replay accounting 738 CLASS constructions.

No full-107 authority exists. Covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Frozen sentinel object

Frozen identities:

- W `19907175f0f3417ddee2aba6916d961c6be02e26`;
- executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`;
- corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`;
- corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`;
- corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #184 promoted exact A/Q without L. Separate hosted and independent post-replacement audits passed. PR #185 then promoted exact-one-run L-gate authority blob `1c1819ee6aa7a48597770d9bc9116185d061a49c`, authorizing one first attempt only, rerun forbidden, full-107 false.

## Consumed first attempt

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` added exact final L as the only runtime path and triggered run `35033268924`:

- workflow id `359060727`;
- run #1 / attempt #1;
- event `push`;
- exact head `9a333294f3acb80201c5f6ed5b74918c1c767232`;
- terminal conclusion `failure`.

A fresh exact-head Actions query now returns exactly one run for that head: `35033268924`. No rerun/duplicate exact-head run is currently present. The attempt is consumed and must never be rerun.

Hosted job state:

- authorize `104596462857`: failure;
- materialize-plan: skipped;
- lane: skipped;
- decision `104596495504`: failure from missing current-run authorization;
- science-run artifacts: zero.

No CLASS science solve, scientific response, covariance read or sentinel decision occurred. There is no sentinel scientific classification from attempt #1.

## Failure mechanism

Authorize traceback is embedded Python line 48:

`assert added.count(launch)==1`

All package/blob assertions before the event guard were reached without failure and independently reproduce as passing. Repository first-parent/staging diffs contain exactly one added L.

Frozen W uses `github.event.commits[*].added/modified/removed`, but the Actions push-event platform contract used by the repository omits those commit-level file-list attributes. With `c.get('added', [])`, effective added count becomes zero, so the event guard rejects the correct L-only change before science.

This is an infrastructure/implementation event-contract failure, not numerical/reproducibility science, statistical/model evidence, or physical inference.

## Historical interim state remains authoritative until independent terminalization

PR #187 persisted the preliminary audit and interim authority:

`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAIL_CLOSED_INTERIM_V0_1.json`, blob `8f898f3579ac55db4bfd3b7cc6a12cad04a4a613`.

Historical verdict remains `BLOCKED`. It forbids rerun, same-nonce second attempt, final-L mutation/removal/recreation, full replay and downstream science. It does not claim a sentinel scientific PASS or refutation.

PR #189 review support blob `34acaa0f87af18cb85d765b9a2cb80003af65a71` corroborates the platform-contract mechanism but is explicitly not terminal first-attempt authority.

## Exact forensic producer is now terminal

Frozen forensic producer:

- branch `audit/v026-r1-sentinel-first-attempt-forensic`;
- head `c5502bc124f502cb4ef1c19300fcdf87f260089b`;
- auditor blob `63b6a0db41ff5e0e3c36be605596fb1c5aee0f1d`;
- workflow blob `4d09b78d3a586d3c4f7e42573a7bdac4454d3a48`;
- run `35033678449`, run #3 / attempt #1;
- terminal `completed/success`;
- job `104597783801`: success.

Exactly one artifact exists:

- id `10422924571`;
- name `dsir-v026-r1-sentinel-first-attempt-forensic-audit-v0-1`;
- ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`.

Independent download/hashing matches the Actions digest. The ZIP has exactly seven entries and no nested extras. Receipt `first_attempt_forensic_audit.json` is 2374 bytes, SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`; both inner SHA manifests verify.

Producer receipt says `TERMINAL_BLOCKED` / `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`, with no CLASS invocation, no scientific response/covariance, rerun false and full-107 false.

This is immutable evidence, not yet the independent terminal first-attempt authority.

## Current reviewed gate: PR #190 failure-funnel candidate

PR #190 is open/draft. Reviewed exact head `d38e9825ba7fa87558c7f729c3abdf67002e038f` changes only the independent failure-funnel auditor and its machine contract:

- auditor blob `5823daaa682a99460203ce3d4db5e59cd08c731d`;
- contract blob `7a57bfd512bcdb4042be0d7940e57c3059a9cc36`.

Independent audit saved at:

`docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_AUDIT_V0_1.md`

commit `e23cb73df393d221c7e3a9742f1b915108644980`.

Terminal audit qualification authority:

`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_QUALIFICATION_V0_1.json`

commit `d7b329796f73d7b09bfb0d71d9ae422d51b3a583`.

Verdict: **QUALIFIED**.

The forensic evidence/root cause survive. The reviewed PR190 candidate is not execution-ready because:

1. contract producer artifact id / ZIP SHA256 / receipt SHA256 remain null and stale;
2. candidate auditor does not live-enumerate exact science workflow/head runs, so a later forbidden rerun could evade the immutable producer snapshot;
3. candidate exact-file-set check is only top-level and would not reject nested extras;
4. manifest parsing must bind exact relative names/cardinality with no basename collisions;
5. any future hosted failure-funnel workflow must fetch full graph or every exact historical SHA required by the independent reconstruction.

No hosted failure-funnel workflow exists at reviewed PR190 head, so no competing terminal verdict was created.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> CORRECTED A/Q PROMOTED -> EXACT L-GATE AUTHORITY -> EXACT L TRIGGER -> RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> HISTORICAL INTERIM BLOCKED -> FORENSIC RUN #3 TERMINAL SUCCESS -> PR190 FAILURE-FUNNEL CANDIDATE QUALIFIED / NOT EXECUTION-READY -> HARDEN + REAUDIT REQUIRED -> FULL 107 ROW CLOSED`.

## Exact next admissible action

Revise PR #190 prospectively, code/contract only:

- freeze artifact id `10422924571`;
- freeze ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`;
- freeze receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`;
- live-enumerate exact science workflow/head and require exactly run `35033268924`, run #1 / attempt #1;
- recursively require exactly seven frozen artifact relative paths and no extras;
- hard-bind manifest relative names/cardinality;
- ensure future hosted workflow has full graph/exact historical SHAs.

Then perform a fresh independent response-blind static re-audit of the revised PR190 head. **Do not execute the failure funnel yet and do not persist terminal first-attempt result authority yet.**

Do not rerun `35033268924`, do not modify/remove/recreate final L, and do not silently patch W and call it the same attempt. Any future science sentinel requires a separately prospectively frozen successor governance/workflow with a new trigger identity and independent pre-activation audit.

Effect remains `+0/+0`; readiness `68%`; scientific frontier `67%`.
