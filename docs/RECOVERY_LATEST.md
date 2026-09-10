# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JO_SPLIT_PREFLIGHT_AND_SOURCE_GUARD_V83.md`, creation commit `25e412a0701b7fd0e937f2ba12351b4f063f0da7`. Earlier notes remain immutable history, including autonomous JO source-bundle V82.

## Preserved authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid maximum `0.9998247463807295`. Exp073JI preserves all 107 rows with zero unsupported targets. Exp073JJ and JK remain support-only NOT_CONVERGED at `0.037280144773915974` and `0.016330535730270664`. Covariance restriction remains unauthorized; Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, support/masks/domain and anti-rescue rules remain unchanged.

## JL/JO infrastructure history
Frozen JL run `34497160814` had two external hosted-runner shutdowns (jobs `102938434376`, `102944693569`) during numerical step 10 and produced no JL result artifact. Both are infrastructure/process +0/+0.

JO prereg commit `af034787b0493e80e12a0faa4127a08a451ab5df`; unchanged recovery wrapper commit `fb4cae4d4a407fe30faf1a9875d290887bcb822d`, blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`.

Combined JO preflight run/job `34504474368 / 102963111387`, head `374184d1b2e9f31628ab930bc271951569ce2bf9`, passed static/environment/exact CLASS-IV build but received an external hosted-runner shutdown at `2026-09-10T17:03:11Z` during the combined live-control step. No assertion/result JSON/artifact existed. Classification: `INVALID_INFRA_PLUS_0_PLUS_0`, not a negative history/cache result.

## Current process — split JO preflight v0.2
The exact same frozen controls are split into three shorter independent hosted jobs under prospective amendment commit `9f8bb9df1215fe114ffaaa6403d47c0c913564c2`. Helper implementation `9630487813533294dd7ec090916b289b78231b89`; workflow/head `f13c827bf265e1329e7d0502f1da12e2fa723d07`; active run `34506027292`.

Jobs:
- cache_roundtrip_slot10 `102968324698`;
- history_slot20 `102968325017`;
- history_slot10 `102968325131`.
`fail-fast=false`; aggregate PASS requires all three exact part artifacts. No JL Article-III numerical result is read by this preflight.

## Recovery hardening retained
Autonomous commit `be1687db88b35951cf3e813c64dbdd017af2802e` binds 16 frozen scientific/traversal/config files to `SCIENCE_REFERENCE_COMMIT=374184d1b2e9f31628ab930bc271951569ce2bf9`; retain this source-bundle guard. Wrapper identity amendment `41b5026f90ff0f4ac9252abc81255fe60a0e6d89` separately binds the JO wrapper blob `aa4c544c...`.

Independent reinspection of verified JK artifact `10160083225`, ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`, establishes full response-call topology: slot10 exactly 441 calls / 83666 target evaluations; slot20 exactly 569 calls / 121682 target evaluations; unsupported=0. Topology amendment commit `4fcb6035c880418a74bec8537bc11b2795f20607` requires these exact terminal counts for recovered JL.

Prepared heavy recovery workflow remains non-auto-triggered (`workflow_dispatch` only) and MUST NOT run before independently verified split-v0.2 aggregate PASS authority. When activated, preserve autonomous source-bundle guard and add v0.2 authority, wrapper-blob and 441/569 topology guards; launch exactly one checkpointed recovery.

## Frozen post-JL branches
Valid recovered JL CONVERGED -> only Exp073JN fresh science-authorizing Layer-B rerun. Valid recovered JL NOT_CONVERGED -> only Exp073JM 4097->8193 support-only refinement. Infrastructure/process failure -> neither. Known inactive JM activation overconstraint must be corrected before any JM science run without amending its frozen preregistration.

## Exact next action
Terminal-consume split run `34506027292`. If all three exact controls PASS, independently verify part and aggregate artifact hashes/identities and commit durable JO v0.2 preflight authority; then harden+activate one checkpointed JL recovery. If an individual part suffers external shutdown, preserve successful part artifacts and recover only the missing unchanged part where practical. No tolerance rescue.
