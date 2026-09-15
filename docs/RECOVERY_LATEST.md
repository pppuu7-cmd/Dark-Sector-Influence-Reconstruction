# DSIR authoritative recovery — latest

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts, terminal authorities, `docs/CURRENT_PROCESS.md`, and this file are the durable source of truth. Chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains the prospectively frozen numerical/reproducibility successor:

- preregistration `prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.md`, blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`;
- contract `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json`, blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`;
- denominator 107 retained rows = DES 53 + BOSS 54;
- alpha canonical-32769 `tol_perturb_integration=3e-10`;
- beta exact-target route `tol_perturb_integration=1e-12`;
- scientific relative criterion strict `<1e-3`;
- technical reproducibility criterion strict `<1e-5`;
- requested-node binding `<=1e-12`;
- full-replay accounting 738 CLASS constructions.

Full 107-row replay, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Frozen implementation and corrected launch package

Frozen sentinel identities remain:

- W `.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml`, blob `19907175f0f3417ddee2aba6916d961c6be02e26`;
- executor `ci/layerb_beta_v026_r1_sentinel_v0_1.py`, blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- decision `ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py`, blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- implementation contract blob `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`.

Historical A/Q runtime-schema blockers were corrected without changing science:

- corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`;
- corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`;
- corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #184 merge `41ef654d7552b670c20d3202249d7687bae5f870` promoted exact A/Q without L. Post-replacement hosted audit `35032839418` and independent funnel `35032991806` passed with zero sentinel-science runs at the replacement head.

PR #185 merge `2ca2d4c35f9dcfe2be00e573598e6189f987508d` promoted the separate exact-one-run L-gate authority:

`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_EXACT_L_GATE_AUTHORITY_V0_1.json`, blob `1c1819ee6aa7a48597770d9bc9116185d061a49c`.

That authority allowed exactly one new-file final-L trigger / one first attempt, explicitly forbade rerun, and kept full-107 false.

## Exact L trigger and consumed first attempt

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` created exact final L as the only runtime file change:

`docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json`, blob `fa7014435f0a5688def2124898ddd01d0c0183aa`.

It produced sentinel workflow run:

- run `35033268924`;
- workflow id `359060727`, `layerb-beta-v026-r1-sentinel-science-v0-1`;
- event `push`;
- run #1 / attempt #1;
- head `9a333294f3acb80201c5f6ed5b74918c1c767232`;
- terminal conclusion `failure`.

A fresh exact-head Actions enumeration on 2026-09-16 returned exactly one workflow run for that head: run `35033268924`, attempt 1. No rerun or duplicate exact-head selection contamination is currently present.

This attempt is consumed. **Never rerun it.**

## Failure localization: pre-science event guard

Hosted job outcomes:

- authorize job `104596462857`: failure;
- materialize-plan: skipped;
- lane: skipped;
- decision job `104596495504`: failure because current-run authorization was absent;
- science-run artifact count: 0.

No source-plan materialization, lane execution, CLASS scientific solve, scientific response, covariance read, or sentinel decision artifact exists from run `35033268924`.

Authorize log fails at embedded Python `<stdin>` line 48, exactly:

`assert added.count(launch)==1`

All preceding package/blob predicates were reached without failure. The repository tree is correct: staging commit `657e5d6b2fe3ad7f7c11bcd2af873cffe800cc96` and merge `9a333294f3acb80201c5f6ed5b74918c1c767232` both show exact L as the single added path relative to the authorized first parent.

Frozen W reconstructs event file changes from `github.event.commits[*].added`, `modified`, and `removed`, with missing fields falling back to `[]`. The Actions push payload platform contract used by the repository omits those commit-level file-list attributes, so effective `added.count(launch)=0` even for the correct L-only repository change.

This is a pre-science workflow/event-contract implementation failure. It is not an interpolation, resolution, solver-tolerance, reproducibility, covariance, nuisance, statistical, or physical-science result.

## Historical fail-closed interim authority

PR #187 merge `f85d679fd4e8a16b83e7b44fd74911149e868746` persisted:

- preliminary failure audit blob `387e13ac2f1c88d0405c7b3f7a41886cd1e276af`;
- interim authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAIL_CLOSED_INTERIM_V0_1.json`, blob `8f898f3579ac55db4bfd3b7cc6a12cad04a4a613`.

The historical interim verdict remains `BLOCKED`. It forbids rerun of `35033268924`, same-nonce second attempt, final-L modification/removal/recreation, full replay and downstream science. It does not claim a sentinel scientific PASS or refutation.

PR #189 later added immutable platform-contract review support blob `34acaa0f87af18cb85d765b9a2cb80003af65a71`; that file is review support only, not terminal first-attempt authority.

## Terminal forensic evidence now exists

The exact forensic producer is fixed at:

- branch `audit/v026-r1-sentinel-first-attempt-forensic`;
- head `c5502bc124f502cb4ef1c19300fcdf87f260089b`;
- auditor blob `63b6a0db41ff5e0e3c36be605596fb1c5aee0f1d`;
- workflow blob `4d09b78d3a586d3c4f7e42573a7bdac4454d3a48`;
- run `35033678449`, run #3 / attempt #1, event `push`;
- terminal status/conclusion `completed/success`;
- job `104597783801`: success.

It emitted exactly one immutable artifact:

- artifact id `10422924571`;
- name `dsir-v026-r1-sentinel-first-attempt-forensic-audit-v0-1`;
- Actions ZIP digest `sha256:226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`.

Independent download/hashing matched that ZIP digest exactly. The ZIP contains exactly seven files and no nested entries. Producer receipt `first_attempt_forensic_audit.json` is 2374 bytes with SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`. Both inner SHA256 manifests were independently verified.

The forensic receipt records `TERMINAL_BLOCKED` / `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`, no CLASS invocation, no scientific response, no covariance read, rerun false, same-nonce second attempt false, and full-107 false.

The forensic artifact is valid immutable evidence. It does **not** by itself replace the required independent failure-funnel audit/terminalization gate.

## Independent audit of PR #190 failure-funnel candidate

PR #190 is open/draft. Reviewed exact head: `d38e9825ba7fa87558c7f729c3abdf67002e038f`.

Reviewed candidate identities:

- independent auditor blob `5823daaa682a99460203ce3d4db5e59cd08c731d`;
- machine contract blob `7a57bfd512bcdb4042be0d7940e57c3059a9cc36`.

Independent audit:

`docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_AUDIT_V0_1.md`, commit `e23cb73df393d221c7e3a9742f1b915108644980`.

Terminal audit qualification authority:

`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_QUALIFICATION_V0_1.json`, commit `d7b329796f73d7b09bfb0d71d9ae422d51b3a583`.

Verdict: **QUALIFIED**.

The root-cause evidence and actual forensic artifact provenance survived review, and the live repository currently has exactly one exact-head science run. However, reviewed PR190 head is not executable/terminalizable as-is because:

1. contract fields for producer artifact id / ZIP SHA256 / receipt SHA256 are still null and say the producer is queued;
2. the candidate auditor does not live-enumerate exact science workflow/head runs, so a forbidden rerun created after the producer artifact could escape detection;
3. its claimed exact artifact-file-set check inspects only top-level files and would not reject nested extras;
4. manifest parsing should bind exact relative names/cardinality rather than basename-normalizing entries;
5. any future hosted funnel workflow must checkout full history or explicitly fetch all exact historical SHAs needed by the independent reconstruction.

These are fail-closed audit-implementation qualifications. They do not change the pre-science root cause and do not create a sentinel scientific result.

## Exact next admissible gate

Revise PR #190 prospectively as a new exact candidate head, changing only the failure-funnel audit/contract object:

- freeze artifact id `10422924571`;
- freeze ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`;
- freeze producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`;
- live-enumerate the exact science workflow/head and require exactly run `35033268924`, run #1 / attempt #1, with no duplicate/rerun;
- recursively require exactly the seven frozen forensic artifact relative paths and no extras;
- bind exact manifest names/cardinality without basename collisions;
- design the future hosted funnel workflow with full graph/exact-SHA availability.

Then conduct a **fresh independent response-blind static re-audit of the revised PR190 code+contract**. Do not execute a hosted failure-funnel workflow and do not write terminal first-attempt result authority before that re-audit passes.

## Recovery invariant

Do not rerun `35033268924`. Do not use rerun-failed-jobs or rerun-job actions. Do not modify/remove/recreate final L. Do not silently patch W and call it a continuation of attempt #1. Do not execute the reviewed PR190 failure funnel as-is.

Any future scientific sentinel requires a separately prospectively frozen successor launch-governance package/workflow with a **new trigger identity**, independently audited before activation. A successor event guard should validate aggregate `before...after` repository diff or equivalent first-parent tree diff rather than absent commit-level file lists.

Current funnel:

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> CORRECTED A/Q PROMOTED -> EXACT L-GATE AUTHORITY -> EXACT L TRIGGER -> RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> HISTORICAL INTERIM BLOCKED -> FORENSIC RUN #3 TERMINAL SUCCESS + IMMUTABLE ARTIFACT -> PR190 FAILURE-FUNNEL CANDIDATE QUALIFIED / NOT EXECUTION-READY -> PR190 HARDENING + REAUDIT REQUIRED -> FULL 107 ROW CLOSED`.

Effect remains `+0/+0`; readiness `68%`; scientific frontier `67%`.
