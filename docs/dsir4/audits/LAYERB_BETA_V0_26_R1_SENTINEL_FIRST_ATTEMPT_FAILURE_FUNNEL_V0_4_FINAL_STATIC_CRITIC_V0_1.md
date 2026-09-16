# DSIR v0.26 R1 — v0.4 final static Critic v0.1

Date: 2026-09-16

## Scope

Independent consumption of the final prospective v0.4 failure-funnel source set and hosted static-audit evidence. This Critic is governance/provenance/static implementation evidence only and does not authorize execution or science.

## Exact candidate

- branch: `audit/v026-r1-failure-funnel-v04-dispatch-history-closure`
- head: `10e7f9bd8aaa5623e9f34adf17c2f53f50db5873`
- hosted workflow blob: `6bf2027a121348823914e9076338055a4820162e`
- post-run history workflow blob: `6c2617e756877fb3cbb8b27dcf16b2bfc164cab5`
- static auditor blob: `73ebfa8d680809f3d577c7eab4b6f6f689c9edab`
- static-audit workflow blob: `884b9d13b1c76db6028fb81e892165f4377c1255`
- machine-contract blob: `23e2404d835b4615308fbbb345f8a00e45c449a1`

## Authoritative hosted evidence

Run `35139440106`, workflow `359934434`, run #2 / attempt #1, exact head `10e7f9bd...`, job `104939962304`, completed `success`.

Artifact `10464695970` was downloaded and independently inspected. ZIP SHA-256 recomputed as `bff94d6a0c0eb956efd19357a8099075ea035fcc78fe8a638b6e2c7b75333b60`. It contains exactly three files: `v04_static_receipt.json`, `v04_static_receipt.sha256`, `v04_live_runs.json`.

Receipt SHA-256 recomputed as `7072fa7f39f8c903f0b75fddc14f108981c9ec6beafc052f5593ba949b4e88ae` and matches the recorded checksum. Receipt token is `QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_DISPATCH_HISTORY_STATIC_PLUS_0_PLUS_0`.

## Critic result

The exact final source set verifies the intended monotonic first-dispatch and post-run closure controls: runtime `GITHUB_RUN_NUMBER==1`, API `run_number==1`, attempt 1, unique visible current dispatch, end-of-run fresh live-history recheck, separate `workflow_run: completed` terminal history audit, and fail-closed behavior for a late duplicate. Candidate dispatch history at static review is zero.

No deterministic source defect was found that requires v0.5. The stale intermediate static-authority candidate bound to head `8c772714...` and run `35139417993` is not authoritative for the final source set and is not rewritten.

## Authorization boundary

This Critic and the hosted static receipt authorize no promotion, no failure-funnel dispatch, no rerun of science run `35033268924`, no same-nonce second attempt, no successor sentinel science, no full-107 execution and no downstream science.

The only admissible next step is a separate prospectively frozen execution-authority gate for exactly one first live `workflow_dispatch` of the exact final v0.4 workflow.
