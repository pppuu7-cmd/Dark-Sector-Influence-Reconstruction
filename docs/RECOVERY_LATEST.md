# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JO_SPLIT_PARTIAL_PASS_SLOT20_RECOVERY_V84.md`, creation commit `965953f3ea5abcf8d5779d26a1718d508657af1c`. Earlier notes remain immutable history, including V83 and source-bundle V82.

## Preserved authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid maximum `0.9998247463807295`. Exp073JI preserves all 107 rows with zero unsupported targets. Exp073JJ and JK remain support-only NOT_CONVERGED at `0.037280144773915974` and `0.016330535730270664`. Covariance restriction remains unauthorized; Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, support/masks/domain and anti-rescue rules remain unchanged.

## JO split-v0.2 consumed state
Run `34506027292`, head `f13c827bf265e1329e7d0502f1da12e2fa723d07`:
- cache_roundtrip_slot10 job `102968324698`: validated exact PASS, artifact `10164156389`, ZIP digest `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`;
- history_slot10 job `102968325131`: validated exact PASS, artifact `10164136352`, ZIP digest `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`;
- history_slot20 job `102968325017`: external hosted-runner shutdown at `2026-09-10T17:11:13Z` during exact control before any result/artifact. Classification `INVALID_INFRA_PLUS_0_PLUS_0`; aggregate skipped.

The missing failed job only was requested for unchanged GitHub Actions recovery. Current slot20 job: `102985819424`, same run/head, state QUEUED at dispatch. Home/self-hosted ownership none. Successful part artifacts remain preserved and must not be invalidated merely because the missing part is retried.

## Recovery hardening retained
JO prereg `af034787b0493e80e12a0faa4127a08a451ab5df`; split amendment `9f8bb9df1215fe114ffaaa6403d47c0c913564c2`; wrapper commit `fb4cae4d4a407fe30faf1a9875d290887bcb822d`, blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`.

Prepared JL recovery must retain source-bundle guard `be1687db88b35951cf3e813c64dbdd017af2802e` and exact terminal traversal topology from verified JK: slot10=441 calls/83666 target evaluations; slot20=569 calls/121682 target evaluations; unsupported=0. Heavy recovery remains forbidden until independently verified JO v0.2 aggregate PASS authority.

## Frozen post-JL branches
Valid recovered JL CONVERGED -> only Exp073JN. Valid recovered JL NOT_CONVERGED -> only Exp073JM. Infrastructure/process failure -> neither. Known inactive JM activation overconstraint must be corrected before any JM science activation without changing its frozen preregistration.

## Exact next action
Terminal-consume job `102985819424`. If exact PASS, inspect raw log and artifact/digest/identity, combine only with preserved validated slot10/cache parts, write durable JO v0.2 aggregate authority, then harden+activate exactly one checkpointed JL recovery. If infrastructure failure, preserve successful parts and recover only missing unchanged slot20 where practical. Exact assertion failure blocks JL recovery. No tolerance rescue.
