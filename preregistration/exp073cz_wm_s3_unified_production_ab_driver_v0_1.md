# Exp073CZ v0.1 — unified Wm_S3 production A/B driver integration audit

Date: 2026-09-04. Scope: DSIR only. Accounting: `+0/+0`. This is a hosted support/integration gate and cannot create Wm_S3 scientific authority or activate Exp073BU.

## Prospective purpose
Close the concrete Exp073CX A2 implementation gap after Exp073CY Y1 by introducing one production-capable driver `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py` that composes the already admitted fresh-input authority and exact stock-persistence/mmap downstream route without changing frozen scientific arithmetic.

## Frozen production composition
For each independent replica A/B:
1. bind only the exact tracked R1/S3 and DES lens authority exposed by `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py`;
2. on a fresh replica reconstruct lens and S3 masks exactly once and persist canonical `<f8` mask payloads at `fresh_masks_complete`; on restore verify canonical SHA256/provenance and load those payloads instead of reconstructing inputs;
3. create exactly one `NmtField` pair from those masks; the same field objects must feed both fresh mask PCL and `NmtWorkspace.compute_coupling_matrix`;
4. use PyMaster/NaMaster 2.7 and exact band edges `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`;
5. persist the fresh stock workspace using stock `write_to()`; `get_coupling_matrix()` materialization is forbidden in the production path;
6. pass the persisted workspace through the admitted verified OS-mmap exact downstream route and select `wins[0,:,0,:] = TE<-TE`, canonical `<f8 [39,12288]`;
7. preserve ordered durable boundaries `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete` with isolated namespaces `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`, fail-closed restore, payload SHA256, contract fingerprint and source-head binding;
8. final A/B comparison requires whole canonical selected-TE SHA256 equality AND `numpy.array_equal`; no tolerance/rounding/smoothing/averaging rescue.

Historical Wm_S3 numerical payload import and cross-replica restore are forbidden. Scientific score remains absent in this gate.

## Hosted audit
Hosted CI MUST NOT execute DES-scale Wm_S3 numerics. It must verify source/blob bindings, Python compilation, exact frozen edges/TE semantics, single-field handoff in production control flow, stock `write_to()` composition, absence of production `get_coupling_matrix()` materialization, exact comparator, checkpoint order/namespaces/fail-closed metadata, 8-core contract declaration with nested thread variables pinned to 1, and no historical numerical import.

Frozen classifications:
- `Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS`
- `Z2_IMPLEMENTATION_CONTRACT_FAIL`
- `Z3_EXACT_COMPARATOR_OR_CHECKPOINT_FAIL`
- `Z4_PROVENANCE_BINDING_FAIL`
- `Z5_INFRASTRUCTURE_FAIL`

Only Z1 permits a subsequent fresh activation-readiness audit. Z1 itself does not authorize home science.