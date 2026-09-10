# DSIR recovery V82 — Article III Exp073JO split preflight running

Date: 2026-09-10. Scope: DSIR only.

## Preserved scientific authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with native-grid maximum `0.9998247463807295`. Exp073JI preserves complete 107-row shared-grid support. Exp073JJ remains support-only NOT_CONVERGED at `0.037280144773915974`. Exp073JK remains support-only NOT_CONVERGED at `0.016330535730270664`. Covariance restriction remains unauthorized and Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, masks/domain/accounting are unchanged.

## Exp073JL process history
Original frozen JL run `34497160814` has two infrastructure-only attempts with no numerical result artifact:
- attempt 1 job `102938434376`: external hosted-runner shutdown during numerical step 10;
- attempt 2 job `102944693569`: external hosted-runner shutdown during numerical step 10 at 2026-09-10T16:10:29Z.
Neither is CONVERGED nor NOT_CONVERGED.

## Exp073JO v0.1 preflight terminal process result
JO recovery prereg commit `af034787b0493e80e12a0faa4127a08a451ab5df`; unchanged recovery wrapper commit `fb4cae4d4a407fe30faf1a9875d290887bcb822d`, Git blob SHA `aa4c544c1e3e81137010fcdbd34f20567e1eb894`.

Combined exact-build preflight run/job `34504474368 / 102963111387`, head `374184d1b2e9f31628ab930bc271951569ce2bf9`, passed static lineage, environment, capacity/parser patch and exact pinned CLASS-IV build. During the combined history-independence/cache-roundtrip step it received an external hosted-runner shutdown at `2026-09-10T17:03:11Z`. No assertion/CLASS traceback/result JSON/artifact existed. Classification: `INVALID_INFRA_PLUS_0_PLUS_0`; this is not a negative history-independence result.

## Minimal split recovery v0.2
Prospective split amendment: `docs/dsir4/prereg/EXP073JO_ARTICLE3_JL_CHECKPOINT_PREFLIGHT_SPLIT_RECOVERY_V0_2.md`, commit `9f8bb9df1215fe114ffaaa6403d47c0c913564c2`.

Unchanged controls are split into exactly three independent hosted jobs:
- `history_slot10` — same exact v0.1 history/fresh trailing-response comparison for inherited slot 10;
- `history_slot20` — same for slot 20;
- `cache_roundtrip_slot10` — same exact wrapper miss->hit byte/audit roundtrip.

Helper implementation `ci/exp073jo_preflight_parts_v0_2.py`, commit `9630487813533294dd7ec090916b289b78231b89`. The tested recovery wrapper itself is unchanged and must retain blob SHA `aa4c544c1e3e81137010fcdbd34f20567e1eb894`. Wrapper identity amendment commit `41b5026f90ff0f4ac9252abc81255fe60a0e6d89`.

Split workflow/head commit `f13c827bf265e1329e7d0502f1da12e2fa723d07`.
Run `34506027292` currently active with matrix jobs:
- cache_roundtrip_slot10 job `102968324698`;
- history_slot20 job `102968325017`;
- history_slot10 job `102968325131`.
Each part independently builds the exact pinned CLASS-IV environment and then executes only its frozen exact control. `fail-fast=false`; aggregation is permitted only if all three part jobs pass and upload artifacts.

## Full traversal topology guard
Independent reinspection of verified Exp073JK artifact `10160083225`, ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`, recovered the exact invariant Exp073IR response-call topology:
- slot10: 441 response calls, 83666 target evaluations, unsupported=0;
- slot20: 569 response calls, 121682 target evaluations, unsupported=0.
Prospective JO topology amendment commit `4fcb6035c880418a74bec8537bc11b2795f20607` requires a successful recovered JL process to finish exactly at 441/569 calls; target-evaluation totals are independent final audit expectations.

## Heavy recovery remains inactive
Prepared heavy workflow `.github/workflows/exp073jo-article3-jl-durable-response-checkpoint-recovery-v0-1.yml`, commit `a2ea07ff5a5bd4060cb3c7b7230b398dde202f08`, remains `workflow_dispatch`-only. It MUST NOT run until split-v0.2 aggregate PASS is independently artifact/hash verified and committed as durable JO preflight authority.

## Exact next action
Consume all three jobs of run `34506027292`. If all valid PASS: inspect aggregate artifact, independently verify ZIP and JSON hashes/part identities/wrapper blob/frozen constants, commit durable JO preflight authority, add topology and wrapper identity guards to the still-inactive heavy workflow while enabling exactly one push-trigger, then launch one checkpointed recovered JL. If any part has an actual exact mismatch, JO cache replay is rejected. If a part suffers external shutdown, rerun only that unchanged part architecture; do not reinterpret as science.

Post-JL branching remains frozen: valid JL CONVERGED -> only JN; valid JL NOT_CONVERGED -> only JM; infrastructure failure -> neither. Known JM implementation activation overconstraint remains to be corrected before any JM science run.
