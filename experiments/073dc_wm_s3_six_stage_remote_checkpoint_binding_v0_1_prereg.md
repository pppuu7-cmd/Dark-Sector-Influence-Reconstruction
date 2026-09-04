# Exp073DC v0.1 — Exp073BU six-stage remote-checkpoint binding gate

Date: 2026-09-04. Scope: DSIR only. Support/readiness `+0/+0`; no Wm_S3 authority and no Exp073BU activation.

## Required authorities
- Exp073CX v0.4 `A1_EXP073BU_ACTIVATION_READINESS_PASS`.
- Exp073DA v0.1 `K1_LARGE_STAGE_SHARDED_CHECKPOINT_TRANSPORT_PASS`.
- Exp073DB v0.3 `L1_REMOTE_GIT_BATCH_CHECKPOINT_ORCHESTRATION_PASS`.
- Production driver blob `5c8d5d3463e455389a1ca3df2639bf06a3b7b603` remains the frozen arithmetic baseline.

## Purpose
Audit whether the production Exp073BU A/B driver is actually wired to the admitted durable remote transport at every frozen checkpoint boundary. Component-level checkpoint code or a separately validated transport is insufficient: expensive compute must stop until each completed stage is remotely durable, and verified restore must skip completed expensive stages.

## Frozen requirements
1. Exact stage order: `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`.
2. A/B namespaces remain exactly `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`; no cross-replica restore.
3. Immediately after each stage becomes locally complete, a production hook must pack the complete stage payload set using the admitted Exp073DA exact-byte sharding layer and synchronize it through the admitted Exp073DB v0.3 remote Git layer. Further expensive compute is forbidden until exact post-push durability succeeds.
4. At process start and before recomputing a completed stage, the driver/wrapper must query and restore the exact remote stage head, verify source-head/contract/stage/replica/namespace plus all chunk and whole-file SHA values, and skip recomputation when restore is valid.
5. Partial transport progress never counts as stage completion. Unknown remote state, corrupt/missing data, stale lease, credential failure or post-push ambiguity stops the process fail-closed.
6. One self-hosted process owns both replicas sequentially A then B; no competing home job. The A final output may not be used numerically by B before the final exact comparator.
7. The actual self-hosted workflow must expose a write-capable authenticated Git path for `checkpoints/*` while keeping main science sources read-only during execution. No secret value may be logged.
8. Exactly eight outer workers and nested BLAS/OpenMP/MKL/OpenBLAS threads pinned to 1 remain frozen; no arithmetic changes.
9. No tolerance rescue, historical Wm_S3 numerical import, data-domain/band/ell change, or scientific scoring in this hosted gate.
10. Hosted v0.1 is source/static only. It does not execute DES-scale numerics or create checkpoint branches.

## Frozen classifications
- `N1_SIX_STAGE_REMOTE_CHECKPOINT_BINDING_PASS`: every requirement is implemented and source-bound. Permits a final self-hosted workflow validation/preflight gate; does not activate science.
- `N2_PRODUCTION_DURABILITY_HOOK_GAP`: exact transport and science driver are individually valid, but one or more production stage sync/restore hooks are absent. Implement the smallest prospective wrapper/driver repair; no science launch.
- `N3_WORKFLOW_CREDENTIAL_OR_VALIDATION_GAP`: stage hooks exist but actual self-hosted workflow cannot prove a valid write-capable checkpoint credential/permission path or workflow parses invalidly. Repair infrastructure prospectively.
- `N4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: audit cannot evaluate the frozen contract due source/CI failure.
