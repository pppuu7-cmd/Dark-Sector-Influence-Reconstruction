# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, terminal artifacts and frozen authorities are authoritative; chat is not authority.

## Scientific boundary

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Frozen science boundary remains unchanged: 107 retained rows = DES 53 + BOSS 54; alpha route `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. Full-107 and downstream inference remain closed.

Science run `35033268924`, workflow `359060727`, run #1 / attempt #1, is permanently consumed. Never rerun it, never create a same-nonce second attempt, and never modify/remove/recreate final L.

## V0.4 static and execution authority

Final v0.4 source origin head: `10e7f9bd8aaa5623e9f34adf17c2f53f50db5873`.

Exact source identities:
- hosted failure-funnel workflow blob `6bf2027a121348823914e9076338055a4820162e`;
- post-run `workflow_run` history workflow blob `6c2617e756877fb3cbb8b27dcf16b2bfc164cab5`;
- final static qualification blob `eba53204d3a46b11c54c37adefe729722b00783f`;
- execution authority blob `d68aa9ffa3fb5a7768e6802146aed74a3b57cf1b`;
- review blob `01e5e9e0145e8c2ad1f0da639f3de073d9b26da2`;
- runtime static authority blob `6bbacdc70dbfbee1dc4753e4a05266f9dbe45399`;
- terminal execution-gate authority blob `35578c8eab01b11474c00b5306abe0c0fae7ac70`.

Terminal execution gate run `35145130524` was QUALIFIED with zero prior target dispatches and zero competing target siblings. It authorized exact promotion and at most one target dispatch after a fresh atomic preflight; it authorized no science.

## One-shot launch and consumed v0.4 runtime

One-shot launcher static audit run `35145717750` was terminal success. Artifact `10467406401` ZIP SHA256 is `d314cd72a1e5786e6a848a83f583374f9aa6d6ba8255f14af8329770b5180e2c`; launcher-static receipt SHA256 is `8a3e19094cd5713962b9574f076546d4eb9dd9f5e3e7ccbf249aff0d1f085a32`.

PR #196 merge `fcdcf5b90c2fe701b480bac8b5dc771bb3ccf871` activated the terminal one-shot launcher. Launcher run `35145835567`, workflow `359976724`, run #1 / attempt #1, completed success. Its atomic preflight observed zero target dispatches and zero active target siblings. Exactly one REST dispatch call returned HTTP 204. Launcher artifact `10467436639` ZIP SHA256 is `29957b38879e587862d775bd1faffeb61d6d560382df60ade301831cd101715a`.

The single target v0.4 failure-funnel run is `35145849799`, workflow `359974223`, `run_number=1`, `run_attempt=1`, event `workflow_dispatch`, branch `main`, head `fcdcf5b90c2fe701b480bac8b5dc771bb3ccf871`. The run completed `success`; every runtime provenance guard passed, the frozen independent failure-funnel auditor passed, and the end-of-run fresh live-history recheck passed.

Target artifact `10467257116` ZIP SHA256 is `fdb47099b592afb13959a94a0e82678db284d786b63e57501d73277ea522f58a`. Failure-funnel receipt SHA256 is `8495668b993620c99ffe77f08297077749813d218c2e68988130023b0d7037ab`. Pre-run and end-of-run history snapshots are identical, SHA256 `1fad673eaf80610f4a042b24ee62107d71cf83f30cdf346dbf70e2f8932e3eb5`, and contain exactly the one target run.

The failure-funnel receipt verdict remains `CONFIRMED_SCOPED`, classification `SENTINEL_FIRST_ATTEMPT_PRE_SCIENCE_ACTIONS_EVENT_GUARD_FAILURE_INDEPENDENTLY_CONFIRMED`; it explicitly authorizes no successor science and no full-107 execution.

## Terminal runtime blocker

The separately frozen post-run workflow required `workflow_run: completed`. After target completion, a fresh Actions query over the relevant time range returned zero `workflow_run` runs. Therefore the required terminal post-run receipt does not exist.

This is consistent with GitHub's documented `GITHUB_TOKEN` recursion rule: events caused by `GITHUB_TOKEN` do not create new workflow runs except `workflow_dispatch` and `repository_dispatch`. The launcher correctly created the target via the `workflow_dispatch` exception, but the downstream `workflow_run` chain did not materialize.

Durable authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_RUNTIME_POSTRUN_BLOCKER_V0_1.json`.

Classification: `V0_4_TARGET_RUNTIME_SUCCEEDED_BUT_REQUIRED_POST_RUN_WORKFLOW_RUN_TERMINAL_HISTORY_AUDIT_WAS_NOT_CREATED`.

V0.4 is now consumed and terminally BLOCKED before terminal runtime authority. Do not rerun/retry the target, do not create a second v0.4 dispatch, and do not substitute a post-hoc manual audit for the frozen requirement.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED PRE-SCIENCE FAILURE -> FORENSIC AUTHORITY TERMINAL -> V0.2/V0.3 DEFECTS TERMINAL -> V0.4 STATIC QUALIFIED -> V0.4 EXECUTION AUTHORITY QUALIFIED -> ONE-SHOT V0.4 RUN #1/ATTEMPT #1 SUCCESS -> END-OF-RUN HISTORY PASS -> REQUIRED WORKFLOW_RUN POST-RUN AUDIT NOT CREATED -> V0.4 TERMINAL RUNTIME BLOCKED -> SCIENCE CLOSED`.

Effect remains `+0/+0`. No new V0.26 R1 scientific response exists.

## Exact next admissible action

1. Never rerun target `35145849799`; never create another v0.4 dispatch or same-nonce attempt.
2. Prospectively freeze a **new successor repair identity** solely for the post-run trigger defect. The repair must not alter the historical v0.4 outcome.
3. Use an explicit GitHub event that is permitted from `GITHUB_TOKEN` (for example a separately frozen `workflow_dispatch` terminal-history auditor) and ensure that auditor evaluates the target only after it is terminal, then freshly proves exactly one run #1 / attempt #1.
4. Independently static-qualify that successor source set before any new live execution authority is considered.
5. No post-hoc recovery of v0.4 can authorize science. Successor sentinel science, full 107 rows and downstream science remain false until a completely separate terminal authority opens the minimal next scientific object.
