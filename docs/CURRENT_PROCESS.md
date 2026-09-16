# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts and terminal authorities are authoritative. Chat is not authority.

## Scientific baseline and immutable boundary

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Frozen science boundary is unchanged: 107 retained rows = DES 53 + BOSS 54; alpha route tolerance `3e-10`; beta exact-target tolerance `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay accounting 738 CLASS constructions. There is no full-107 execution authority. Covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

## Consumed sentinel first attempt and immutable forensic chain

Science run `35033268924`, workflow `359060727`, run #1 / attempt #1, head `9a333294f3acb80201c5f6ed5b74918c1c767232`, is permanently consumed. It failed before science at frozen W event guard `assert added.count(launch)==1`; zero science artifacts exist. Never rerun it, never create a same-nonce second attempt, and never modify/remove/recreate final L.

Forensic producer run `35033678449` is terminal success. Artifact `10422924571` ZIP SHA256 is `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`; producer receipt SHA256 is `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`. Hardened PR190 exact head `5731b605afdc35bd85d3a2014a9e135719a07697`, auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`, contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`, and independent re-audit run `35036894735` remain terminal governance evidence only.

Historical v0.2 and v0.3 defects remain immutable and are not reopened. V0.3 terminal qualification established that visible-history uniqueness without monotonic `run_number==1` and without terminal post-run live-history closure was insufficient.

## Final prospective v0.4 source set

Exact final candidate is head `10e7f9bd8aaa5623e9f34adf17c2f53f50db5873` on `audit/v026-r1-failure-funnel-v04-dispatch-history-closure`.

Exact identities:
- hosted failure-funnel workflow blob `6bf2027a121348823914e9076338055a4820162e`;
- post-run terminal-history workflow blob `6c2617e756877fb3cbb8b27dcf16b2bfc164cab5`;
- static auditor blob `73ebfa8d680809f3d577c7eab4b6f6f689c9edab`;
- hosted static-audit workflow blob `884b9d13b1c76db6028fb81e892165f4377c1255`;
- machine-contract blob `23e2404d835b4615308fbbb345f8a00e45c449a1`.

V0.4 requires runtime `GITHUB_RUN_NUMBER==1`, API `run_number==1`, run attempt 1, exact current-run identity on `main`, zero/unique dispatch history as appropriate, an end-of-run fresh live-history recheck, and a separate `workflow_run: completed` terminal-history audit that requires the single exact run #1 / attempt #1 to be terminal success. A late duplicate fails closed.

## Terminal v0.4 static qualification

Authoritative hosted static run `35139440106`, workflow `359934434`, run #2 / attempt #1, exact head `10e7f9bd...`, job `104939962304`, is terminal `success`.

Artifact `10464695970`, `dsir-v026-r1-first-attempt-failure-funnel-v04-dispatch-history-static-audit`, was independently downloaded and verified. ZIP SHA256 is `bff94d6a0c0eb956efd19357a8099075ea035fcc78fe8a638b6e2c7b75333b60`; receipt SHA256 is `7072fa7f39f8c903f0b75fddc14f108981c9ec6beafc052f5593ba949b4e88ae`. Artifact contains exactly `v04_static_receipt.json`, `v04_static_receipt.sha256`, and `v04_live_runs.json`.

Receipt token: `QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_DISPATCH_HISTORY_STATIC_PLUS_0_PLUS_0`. Candidate dispatch count at review is zero. All required first-dispatch/end-of-run/post-run guards are true. All execution/science authorization side effects are false.

Independent Critic found no new deterministic v0.4 source defect; no v0.5 repair is justified. The stale intermediate authority candidate bound to head `8c772714...` / run `35139417993` is not authoritative for the final source set and remains historical without rewrite.

Durable final static qualification: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_FINAL_STATIC_QUALIFICATION_V0_1.json`.

Independent Critic: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_FINAL_STATIC_CRITIC_V0_1.md`.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> SENTINEL RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> FORENSIC EVIDENCE TERMINAL -> PR190 CONFIRMED_SCOPED -> V0.2/V0.3 DEFECTS TERMINAL -> V0.4 FINAL SOURCE SET FROZEN -> V0.4 STATIC QUALIFICATION QUALIFIED -> EXECUTION-AUTHORITY GATE NEXT -> FAILURE-FUNNEL DISPATCH CLOSED UNTIL THAT GATE -> SCIENCE CLOSED`.

Interpretation ceiling remains governance/provenance/static implementation only. Effect remains `+0/+0`.

## Exact next admissible action

1. Freeze a separate v0.4 execution-authority gate that binds the exact final source set and this terminal static qualification.
2. Require exact `workflow_dispatch`, `refs/heads/main`, a fresh nonce, `run_number==1`, `run_attempt==1`, zero prior target dispatches, no competing/in-progress sibling, no rerun/second attempt, exact authority/review/static-runtime identities, end-of-run recheck and terminal post-run history closure.
3. Independently audit that execution-authority source set. A PASS may authorize only one exact first v0.4 failure-funnel dispatch; it does not authorize successor science or full 107 rows.
4. Only after terminal execution-authority PASS and exact promotion may a single dispatch occur. No retry/rerun/manual outcome repair is allowed.
5. Never rerun science run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; keep successor sentinel science, full 107 rows and downstream science closed until a separate terminal runtime/promotion authority explicitly opens the minimal next object.
