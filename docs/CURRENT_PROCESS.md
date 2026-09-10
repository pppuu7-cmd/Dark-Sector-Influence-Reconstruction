# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority
- Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid max `0.9998247463807295`; retained 107; covariance restriction unauthorized.
- Exp073JI full-support feasibility remains support-only; Exp073JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`.
- Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, masks/domain/traversal and anti-rescue rules unchanged.
- Exp073JP separately has validated support-only `PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0` authority at commit `de45b113ac34dcec30de29d6d583a1caad89fbb2`; it creates no scientific model PASS or Wm_S3 authority. Overall funnel readiness is 67%; Article III readiness remains 68%.

## Preserved JO v0.2 exact PASS receipts
- `history_slot10`: run `34506027292`, artifact `10164136352`, ZIP SHA256 `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`.
- `cache_roundtrip_slot10`: run `34506027292`, artifact `10164156389`, ZIP SHA256 `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`.

## JO v0.3 consumed infrastructure state
Run `34512184648`, frozen head `f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`.
- original `slot20_after_history` job `102988758987`: external runner shutdown during exact numerical phase, exit 137, no result/artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- original `slot20_fresh_tail` job `102988759155`: external runner shutdown during exact numerical phase, exit 143, no result/artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- aggregate `102991182740`: skipped because phase receipts were absent.
No exact-history negative and no scientific inference is authorized.

## Current authoritative process
Targeted GitHub job recovery of only one missing unchanged v0.3 phase, deliberately serialized to avoid duplicating the prior simultaneous hosted-load pattern.
- workflow/run ID: `34512184648`;
- current job ID: `103005530198` (`phase (slot20_fresh_tail)`);
- branch/frozen head: `main / f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`;
- state at dispatch: QUEUED;
- runner ownership: GitHub-hosted; home/self-hosted ownership none;
- checkpoint namespace reserved for later JL successor: `checkpoints/exp073jo-jl-response-v0-1`;
- last durable scientific checkpoint: none required for this support-only phase receipt;
- next action on valid phase PASS: inspect raw log and independently verify phase artifact ZIP/JSON/response/capacity hashes; preserve the receipt; then recover only still-missing unchanged `slot20_after_history`.
- next action on infrastructure failure: record `+0/+0`, diagnose first causal failure; do not activate JM/JN or weaken the frozen contract.
- next action on exact assertion FAIL: classify according to frozen JO v0.3 contract; checkpoint replay remains forbidden.

## Recovery hardening retained
Prepared JL recovery must retain source-bundle guard commit `be1687db88b35951cf3e813c64dbdd017af2802e`, wrapper blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`, and exact recovered topology slot10=441 calls/83666 targets, slot20=569 calls/121682 targets, unsupported=0. Heavy JL recovery remains forbidden until an independently verified JO aggregate PASS authority exists.

## Frozen post-JL branch
Valid recovered JL CONVERGED -> only Exp073JN. Valid recovered JL NOT_CONVERGED -> only Exp073JM. Infrastructure/process invalid -> neither.
