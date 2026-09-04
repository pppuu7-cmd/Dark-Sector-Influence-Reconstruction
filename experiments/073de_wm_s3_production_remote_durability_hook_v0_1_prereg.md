# Exp073DE v0.1 — Wm_S3 production remote durability hook

Date: 2026-09-04. Scope DSIR only. Support/infrastructure `+0/+0`; no scientific scoring.

## Authority and purpose
Exp073DD v0.1 is authoritative `O1_STAGE_AWARE_CHECKPOINT_BUNDLE_PASS` from run/job `33884749118 / 101061680308`, artifact `9941347886`, independently verified ZIP SHA256 `ab8c4e322121e60feabad862224f5b818e6d73c9526005ba0745bb40a5c8d2ce`. Exp073BU production driver blob `5c8d5d3463e455389a1ca3df2639bf06a3b7b603` still creates only local stage manifests/payloads. This gate may add durability orchestration only; it must not change scientific arithmetic, data, fields, workspace construction, band edges, full-window route, TE selection or A/B comparator.

## Frozen design
Implement one production durability hook on the existing `checkpoints/*` authority plane. It must bind the local Exp073BU stage completion events to Exp073DD content-addressed stage bundles and exact remote-Git sync/restore.

Requirements:
1. Preserve the admitted production driver blob unchanged. Integrate by an execution/orchestration wrapper or hook layer around its existing `stage_manifest`/restore boundary; no edits to numerical functions are permitted in this gate.
2. Exact namespaces remain `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`; cross-replica numerical restore is forbidden.
3. Remote durability is cumulative and stage-aware across exactly the six frozen stages: `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`.
4. A stage is locally resumable as authoritative only after its remote complete head is known and exact restore of that head validates source head, contract fingerprint, replica, namespace, object/file SHA256 and whole-file bytes. Local-only completion may not advance scientific execution after interruption.
5. Each stage bundle enumerates all payload files needed to resume without recomputing any previously verified expensive stage. The workspace/MCM and later exact-window payloads must not be silently recomputed when a valid durable stage exists.
6. Use the admitted Exp073DD/Exp073DB Git transport; do not create a second checkpoint control plane. Object <=64 MiB, each remote transition <=1 GiB, exact existing-ref lease and verified-ABSENT creation semantics remain frozen.
7. GitHub authentication/remote binding must be explicit and testable without embedding credentials in manifests, logs or checkpoint payloads. Hosted regression may use a local bare remote; production workflow binding must prove that the self-hosted checkout can pass a credential-capable repository remote to the admitted transport without altering checkpoint identity.
8. Preserve exactly 8 outer workers where applicable and nested BLAS/OpenMP/MKL/OpenBLAS threads=1. This gate does not run DES-scale science.
9. Preserve source-head and contract-fingerprint identity fail-closed across local and remote manifests. A stale/foreign head, missing object, corrupt object, skipped stage, namespace mismatch or incomplete remote stage must block restore/advance.
10. No historical Wm_S3 numerical import, tolerance, rounding, smoothing, averaging, effective-scale or fiducial-P rescue.

## Hosted regression/static gate
Synthetic hosted tests must prove: six-stage hook order; local-complete/remote-incomplete cannot advance; interruption then exact remote resume; no recomputation of a completed expensive synthetic stage; exact A/B isolation; exact source/contract mismatch rejection; same Exp073DD transport/control plane; credential material absent from durable manifests; production driver blob unchanged; no science numerics executed.

## Frozen classifications
- `P1_PRODUCTION_REMOTE_DURABILITY_HOOK_PASS`: all frozen hook, remote-resume and fail-closed checks pass. Permits prospective integration into the manual Exp073BU activation shell and a final hosted activation audit; does not activate science.
- `P2_PRODUCTION_DURABILITY_HOOK_IMPLEMENTATION_FAIL`: causal software/interface defect; repair prospectively.
- `P3_PRODUCTION_DURABILITY_FAILCLOSED_FAIL`: remote bytes move but stage/identity/restore semantics are unsafe; no science.
- `P4_PRODUCTION_REMOTE_AUTH_BINDING_BLOCKED`: exact GitHub credential-capable remote binding cannot be established safely under the admitted transport; no home science.
- `P5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: hosted/source failure prevents evaluation.
