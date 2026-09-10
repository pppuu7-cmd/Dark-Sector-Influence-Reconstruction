# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority
- Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid max `0.9998247463807295`; retained 107; covariance restriction unauthorized.
- Exp073JI full-support feasibility remains support-only; Exp073JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`.
- Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, masks/domain/traversal and anti-rescue rules unchanged.
- Exp073JP separately retains validated support-only `PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0` authority at commit `de45b113ac34dcec30de29d6d583a1caad89fbb2`; it creates no scientific model PASS or Wm_S3 authority. Overall funnel readiness is 67%; Article III readiness remains 68%.

## Preserved JO v0.2 exact PASS receipts
- `history_slot10`: run `34506027292`, artifact `10164136352`, ZIP SHA256 `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`.
- `cache_roundtrip_slot10`: run `34506027292`, artifact `10164156389`, ZIP SHA256 `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`.

## JO v0.3 consumed infrastructure state
Run `34512184648`, frozen head `f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`.
- original `slot20_after_history` job `102988758987`: external runner shutdown during exact numerical phase, exit 137, no result/artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- original `slot20_fresh_tail` job `102988759155`: external runner shutdown during exact numerical phase, exit 143, no result/artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- targeted `slot20_fresh_tail` recovery job `103005530198`: all frozen guards/build passed, then hosted shutdown/cancellation during exact numerical phase, no artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- targeted `slot20_after_history` recovery job `103005532859`: all frozen guards/build passed, exact phase killed exit 137 under hosted shutdown, no artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
No exact-history negative and no scientific inference is authorized.

## Current authoritative process
A targeted rerun request for only failed fresh-tail job `103005530198` was issued only after live Actions showed 0 queued / 0 in-progress DSIR runs. GitHub matrix rerun semantics unexpectedly recreated both matrix siblings; this is not a competing DSIR control plane.
- workflow/run ID: `34512184648`;
- current required job ID: `103026063803` (`phase (slot20_fresh_tail)`);
- branch/frozen head: `main / f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`;
- current state: IN_PROGRESS in `Execute exact frozen slot20 phase`; setup, checkout, frozen v0.3 contract/identity guards, dependency stack, and exact pinned capacity-patched CLASS-IV build are SUCCESS;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- checkpoint namespace reserved for later JL successor: `checkpoints/exp073jo-jl-response-v0-1`;
- last durable scientific checkpoint: none required for this support-only phase receipt;
- unintended rerun sibling job `103026065923` (`slot20_after_history`) is terminal infrastructure failure: all frozen guards/build passed, exact numerical phase killed exit 137 with hosted-runner shutdown, no artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.

## Exact transition rules
- On valid fresh-tail PASS: inspect raw log and independently verify phase artifact ZIP/JSON/response/capacity hashes; preserve the receipt; then recover only still-missing unchanged `slot20_after_history` without duplicating an active process.
- On another hosted shutdown/kill before artifact: record `+0/+0`; do not blindly rerun the same 4097-node hosted architecture again. Prospectively redesign execution/resource architecture only, while preserving exact JO arithmetic/history semantics and adding a fail-closed equivalence/static guard.
- On exact assertion FAIL: classify strictly under frozen JO v0.3 contract; checkpoint replay remains forbidden.

## Recovery hardening retained
Prepared JL recovery must retain source-bundle guard commit `be1687db88b35951cf3e813c64dbdd017af2802e`, wrapper blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`, and exact recovered topology slot10=441 calls/83666 targets, slot20=569 calls/121682 targets, unsupported=0. Heavy JL recovery remains forbidden until an independently verified JO aggregate PASS authority exists.

## Frozen post-JL branch
Valid recovered JL CONVERGED -> only Exp073JN. Valid recovered JL NOT_CONVERGED -> only Exp073JM. Infrastructure/process invalid -> neither.
