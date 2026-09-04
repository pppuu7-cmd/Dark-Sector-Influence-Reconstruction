# Exp073DD v0.1 — Wm_S3 stage-aware checkpoint bundle transport

Date: 2026-09-04. Scope DSIR only. Infrastructure/support `+0/+0`; no Wm_S3 authority or Exp073BU activation.

## Motivation and authority
Exp073DC v0.1 is authoritative `N2_PRODUCTION_DURABILITY_HOOK_GAP`. Exp073DA K1 proves exact 64 MiB payload sharding; Exp073DB v0.3 L1 proves fail-closed remote Git batch sequencing. The remaining transport-level integration problem is that Exp073BU has six cumulative stage snapshots on one exact A/B checkpoint branch, while the admitted DB single-stage manifest cannot replace an earlier stage without treating earlier chunks as extras or redundantly re-uploading multi-GiB payloads.

## Frozen design
Implement one stage-aware extension on the same existing `checkpoints/*` control plane. Each checkpoint branch has:
- a shared immutable content-addressed object store `checkpoint/objects/<sha256>.bin`, each object <=64 MiB;
- immutable stage directories keyed by frozen stage ordinal/name;
- each stage manifest lists logical files, byte counts, whole-file SHA256, ordered object SHA/offset/length references, source head, contract fingerprint, stage, replica and namespace;
- later stages reuse already-durable content-addressed objects exactly rather than re-uploading unchanged MCM/masks;
- each remote transition introduces <=1 GiB new object payload;
- a stage has no complete marker until every referenced object is remotely durable and exact post-push verification succeeds;
- restore pins exact remote head, verifies identity and every object/file SHA, reconstructs exact bytes, and never imports another replica.

The six science stages remain exactly `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`. No scientific operation, arithmetic, data domain, band edge, TE semantics or acceptance criterion changes.

Hosted deterministic regression must prove: multi-stage progression on one branch; cross-stage object reuse; interrupted partial stage cannot restore as complete; resume; exact file restore; existing-ref exact lease; verified-ABSENT safe creation; exact post-head; A/B namespace isolation; stage-order rejection; corrupt/missing object rejection where practical; all synthetic only.

## Frozen classifications
- `O1_STAGE_AWARE_CHECKPOINT_BUNDLE_PASS`: stage-aware object reuse/progression and exact restore pass. Permits prospective production-driver hook integration; no science activation.
- `O2_STAGE_BUNDLE_IMPLEMENTATION_FAIL`: causal software/infrastructure defect in the new stage-aware layer; repair prospectively.
- `O3_STAGE_BUNDLE_FAILCLOSED_SEMANTICS_FAIL`: bytes move but identity/order/completion/restore semantics are unsafe; no science.
- `O4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: hosted/source failure prevents evaluation.
