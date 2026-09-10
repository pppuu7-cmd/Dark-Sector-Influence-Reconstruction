# DSIR immutable recovery V87 — JO v0.3 repeated hosted shutdown recovery

Date: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority
- Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid maximum `0.9998247463807295`, retained 107; covariance restriction remains unauthorized.
- Exp073JI full-support feasibility remains support-only; Exp073JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`.
- Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, support/masks/domain/traversal and anti-rescue rules are unchanged.
- Exp073JP retains separately validated support-only `PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0` authority at commit `de45b113ac34dcec30de29d6d583a1caad89fbb2`; it creates no scientific model PASS or Wm_S3 authority.

## Preserved JO v0.2 receipts
- `history_slot10`: run `34506027292`, artifact `10164136352`, ZIP SHA256 `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`.
- `cache_roundtrip_slot10`: run `34506027292`, artifact `10164156389`, ZIP SHA256 `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`.

## JO v0.3 consumed infrastructure failures
Prospectively frozen run `34512184648`, head `f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`.

Previously consumed original phase jobs:
- `slot20_after_history` job `102988758987`: external shutdown during exact numerical phase, exit 137, no result/artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- `slot20_fresh_tail` job `102988759155`: external shutdown during exact numerical phase, exit 143, no result/artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.

Newly consumed targeted recovery attempts:
- `slot20_fresh_tail` job `103005530198`: frozen contract/static guards, dependency stack and exact pinned capacity-patched CLASS-IV build all passed; the exact numerical phase then received a hosted-runner shutdown/cancellation before artifact creation. No scientific assertion or JO equality result exists -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- `slot20_after_history` job `103005532859`: frozen guards/build passed; exact numerical phase was killed with exit 137 and hosted-runner shutdown before artifact creation -> `INVALID_INFRA_PLUS_0_PLUS_0`.

No exact-history negative result and no new scientific authority is authorized by any of these failures.

## Recovery action in this iteration
Before recovery, live Actions showed no queued or in-progress DSIR runs. A targeted rerun was requested for only failed fresh-tail job `103005530198` on the unchanged run/head. GitHub's matrix-job rerun behavior re-created both matrix siblings rather than only the requested phase. This was not a second DSIR control plane and no additional scientific branch was launched.

Current matrix attempt:
- authoritative needed phase: `slot20_fresh_tail`, job `103026063803`, run `34512184648`, frozen head `f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`, GitHub-hosted `ubuntu-24.04`;
- at last live inspection, static/identity guards, numerical dependencies and exact pinned capacity-patched CLASS-IV build were SUCCESS; exact frozen slot20 numerical phase was IN_PROGRESS;
- unintended sibling `slot20_after_history` job `103026065923` reached exact numerical execution after all frozen guards/build passed, then was killed with exit 137 and hosted-runner shutdown, no artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`.
- home/self-hosted ownership: none.

Because the active fresh-tail job remains in progress, it must not be duplicated. No partial numerical output may be inspected to alter frozen criteria.

## Frozen JO semantics retained
JO v0.3 still requires independent exact receipts for `slot20_after_history` and `slot20_fresh_tail` at the frozen guarded JL fine lattice of 4097 nodes, native CLASS `k_per_decade_for_pk=20`, centered-cubic ln(k), `h=1e-4`, and unchanged science/domain/provenance. Aggregate authority requires exact identity/hash checks and exact response equality under the preregistered contract. Infrastructure termination creates only `+0/+0`.

## Prepared JL recovery authority remains blocked
Prepared checkpointed JL recovery must retain source-bundle guard commit `be1687db88b35951cf3e813c64dbdd017af2802e`, wrapper blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`, and exact terminal topology slot10=441 calls/83666 target evaluations, slot20=569/121682, unsupported=0. JL recovery is forbidden until independently verified JO aggregate PASS authority exists.

## Exact next action
1. Terminal-consume job `103026063803` from raw logs and independently verified artifact if one is produced.
2. If it yields the exact frozen fresh-tail receipt, preserve its ZIP/JSON/response/capacity identities and then recover only the still-missing `slot20_after_history` receipt without duplicating an active process.
3. If it is another hosted shutdown/kill before artifact creation, do **not** blindly rerun the same 4097-node hosted architecture again. Prospectively redesign only the execution/resource architecture while preserving the exact JO scientific arithmetic and history semantics, and require an equivalence/static guard before resumption.
4. Only after both exact phase receipts exist may JO aggregate run. Only an independently verified aggregate PASS permits one checkpointed JL recovery. Valid recovered JL CONVERGED -> only JN; NOT_CONVERGED -> only JM; infrastructure/process invalid -> neither.
