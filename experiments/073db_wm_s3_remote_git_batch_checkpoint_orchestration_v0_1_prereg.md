# Exp073DB v0.1 — Wm_S3 remote Git batch checkpoint orchestration gate

Date: 2026-09-04. Scope: DSIR only. Support/infrastructure `+0/+0`; cannot create Wm_S3 authority or activate Exp073BU.

## Authority

Requires immutable Exp073CX v0.4 `A1_EXP073BU_ACTIVATION_READINESS_PASS` and immutable Exp073DA v0.1 `K1_LARGE_STAGE_SHARDED_CHECKPOINT_TRANSPORT_PASS`. Exp073DA proves the existing whole-tree checkpoint push is not admissible for the 4,831,838,208-byte stock MCM and freezes exact 64 MiB sharding plus a 1 GiB new-payload batch cap. This gate closes only the missing remote Git sequencing/binding layer.

## Frozen transport semantics

The adapter must preserve the repository's existing `checkpoints/*` control plane and the fail-closed principles of `ci/dsir_checkpoint_git_sync_v0_2.sh`; it must not create another authority plane.

1. A/B namespaces remain exactly `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`; cross-replica restore is forbidden.
2. Remote head is queried exactly before each mutation. UNKNOWN/ambiguous transport state fails closed.
3. New namespaces may start only from verified ABSENT. Existing namespaces require exact expected-head binding.
4. Shard chunks are immutable content-addressed files from Exp073DA's manifest. No numerical transformation is permitted.
5. At most 1 GiB of new chunk payload may be introduced by any single push transition. Each transition is a new commit parented to the exact previously observed checkpoint head and pushed with exact lease semantics.
6. After every push, the remote head is independently queried; computation may proceed only if it equals the exact candidate commit. Response-loss is resolved only by this post-query, never by trusting push exit status alone.
7. Partial transport commits are resumable infrastructure state and MUST NOT contain a stage-complete marker.
8. Stage completion is represented only by a final manifest commit after all expected chunks are present. The final manifest binds source head, contract fingerprint, stage, replica, checkpoint namespace, logical paths, chunk order/offset/length/chunk SHA and whole-file SHA.
9. Restore pins one exact remote head, verifies final stage completion and all identity fields, verifies every chunk and byte-exact whole-file reassembly, and fails closed on missing/extra/reordered/corrupt chunks or head mutation.
10. Hosted audit uses a local bare Git remote and deterministic synthetic payloads only. It must exercise: fresh namespace, multi-batch progression, interrupted partial state + resume, stale lease/race rejection, post-push exact verification, exact final restore, corruption/missing-chunk rejection, and A/B namespace isolation.
11. No DES-scale numerical science, historical Wm_S3 import, tolerance rescue, band/ell/data-domain change, or scientific classification is permitted.

## Frozen classifications

- `L1_REMOTE_GIT_BATCH_CHECKPOINT_ORCHESTRATION_PASS`: all frozen transport tests pass. Permits a separate Exp073BU six-stage activation-orchestration binding audit; does not activate science.
- `L2_REMOTE_GIT_BATCH_ORCHESTRATION_IMPLEMENTATION_FAIL`: deterministic implementation/static test failure; repair only the causal infrastructure defect prospectively.
- `L3_REMOTE_GIT_FAILCLOSED_SEMANTICS_FAIL`: implementation can move bytes but violates lease/post-check/stage-completion/restore identity semantics; no science launch.
- `L4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: CI/source/dependency failure prevents evaluation.
