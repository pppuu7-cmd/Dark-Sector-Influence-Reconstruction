# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JO_SLOT20_PHASE_SPLIT_ACTIVE_V85.md`, creation commit `2fdb9d28de0643050dc7455f8191657108398165`. Earlier recovery notes remain immutable history.

## Preserved scientific authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with native-grid maximum `0.9998247463807295`. Exp073JI preserves all 107 retained rows with zero unsupported targets. Exp073JJ and Exp073JK remain support-only NOT_CONVERGED at `0.037280144773915974` and `0.016330535730270664`. Covariance restriction remains unauthorized; Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, support/masks/domain and anti-rescue rules remain unchanged.

## JO process state
JO v0.2 run `34506027292` has independently verified exact PASS receipts for `history_slot10` (artifact `10164136352`, ZIP SHA256 `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`) and `cache_roundtrip_slot10` (artifact `10164156389`, ZIP SHA256 `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`). Its `history_slot20` was externally shut down twice before any result/artifact, jobs `102968325017` and `102985819424`; both are `INVALID_INFRA_PLUS_0_PLUS_0`, not numerical/history-control failures.

Prospectively frozen JO v0.3 repairs only that process bottleneck by splitting the unchanged slot20 history control into two exact response receipts. Prereg commit `e1c2ef539657155a7475d1c182f39aa96fc2b62a`; helper commit `c01ed9a7d96ca6b12c2f5c9489142b69a28bfa53`, helper blob `24b1e5e87f6560cda145275072639eafaf097881`; workflow/head `f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`; active run `34512184648`.

The v0.3 hosted aggregate must re-hash the two preserved v0.2 PASS artifacts, reconstruct `slot20_after_history` and `slot20_fresh_tail` exact `<f8` `(4,2)` arrays, and require unchanged `np.array_equal` plus identical finite and positive masks. Wrapper Git blob remains frozen at `aa4c544c1e3e81137010fcdbd34f20567e1eb894`. Heavy checkpointed JL recovery remains forbidden until an independently verified v0.3 aggregate PASS authority exists.

Prepared JL recovery must retain the frozen science-source bundle guard and exact terminal topology: slot10=441 response calls / 83666 target evaluations; slot20=569 / 121682; unsupported=0. Valid recovered JL CONVERGED activates only JN; valid recovered JL NOT_CONVERGED activates only JM; infrastructure failure activates neither.

## Stable readiness telemetry
`docs/DSIR_READINESS_TELEMETRY_V0_1.md`, commit `0b06537a632dcf2421450a322d7b4b1c57a3d4c0`, fixes comparable project-management scoring with zero scientific weight.

Current scores:
- Article III repository readiness: **68%**.
- Overall funnel readiness for methodology freeze: **64%**.

Retries/process decomposition do not increase these scores. Scores move only when a frozen milestone in the telemetry rubric closes or is invalidated.

## Exact next action
Terminal-consume JO v0.3 run `34512184648`. Valid aggregate PASS -> independently verify phase and aggregate artifact ZIP/JSON/response hashes; commit durable JO v0.3 aggregate authority; adapt the prepared checkpointed JL recovery to require that exact authority; activate exactly one recovered JL run. External phase interruption -> preserve successful phase and recover only the missing unchanged phase. Exact equality failure -> checkpoint replay forbidden. No tolerance rescue.
