# DSIR immutable recovery — Exp073DC v0.1 N2 production durability-hook gap

Date: 2026-09-04. Scope DSIR only; RTK/RQIR excluded.

Authoritative hosted process: run/job/head `33883012763 / 101055972784 / f5920e9c3dbf1abce2b503d4798d462e0a21478e`; artifact `9940639955`. GitHub artifact digest and independently downloaded ZIP SHA256 exactly match `931fb890b41e3bd736f85b6e6f552115bf54ce00e89f0627d45123d4cba54869`. Raw receipt SHA256 `129cb341c31ca1bff517a7ed6f156d87ee3128e4eaabfd5ed37d7e429f03d57b`.

Frozen classification: `N2_PRODUCTION_DURABILITY_HOOK_GAP`, accounting `+0/+0`. No DES-scale numerical science was executed; `science_gate_scored=false`, `wm_s3_authority_created=false`, `exp073bu_activated=false`.

Passed exact bindings: Exp073BU frozen production-driver blob, Exp073DA sharding adapter blob, Exp073DB v0.3 L1 recovery/harness, six-stage order, exact A/B checkpoint namespaces, and 8-worker/nested-thread contract. The actual blocking checks are exactly: `remote_pack_hook=false`, `remote_sync_hook=false`, `remote_restore_hook=false`, `durability_before_further_compute=false`, and `workflow_checkpoint_transport_binding=false`. `workflow_write_permission=true`.

Interpretation: the scientific production driver and durable transport are separately admitted, but they are not yet wired together. Local `stage_manifest(... complete=True ...)` cannot count as remotely durable. Launching the home science now would violate the universal checkpoint policy because a runner loss after expensive MCM computation could lose the only large-stage payload.

Permitted successor: prospectively implement the smallest stage-aware durable transport integration while preserving the existing A/B branch namespaces and frozen science. It must support multiple sequential stage snapshots on one checkpoint branch, fail-closed remote restore at exact head, and exact file-byte verification; then wire hooks into a prospectively versioned production driver/wrapper and hosted-test synthetic stage progression before any self-hosted science dispatch.
