# Exp073CZ v0.2 — corrected unified Wm_S3 production A/B driver integration audit

Date: 2026-09-04. Scope: DSIR only. Accounting: `+0/+0`. Hosted support/integration gate only; it cannot create Wm_S3 scientific authority or activate Exp073BU.

## Historical v0.1 disposition
Exp073CZ v0.1 remains immutable `Z2_IMPLEMENTATION_CONTRACT_FAIL`. Its receipt showed every frozen implementation check true except `resume_final_before_expensive=false`. Post-run inspection localized that single negative to the auditor itself: v0.1 used whole-file `src.index('fresh_or_restore_masks(root')`, which matched the earlier function definition rather than the call inside `run_replica`. The production driver already calls `validated_finished_receipt(...)`, returns immediately when a verified final receipt exists, and only afterward loads the workspace checkpoint and can call `fresh_or_restore_masks(...)`.

v0.2 is therefore a prospective repair of the audit method, not a reinterpretation or overwrite of v0.1 and not a change to frozen scientific arithmetic.

## Frozen production composition
The audited production driver remains `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py` with no arithmetic retuning. For each independent replica A/B it must:
1. bind only the tracked R1/S3 and DES lens authority exposed by `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py`;
2. on a fresh replica reconstruct lens and S3 masks exactly once and persist canonical `<f8` mask payloads at `fresh_masks_complete`; on restore verify canonical SHA256/provenance and reuse those payloads;
3. create exactly one `NmtField` pair from those masks, with the same field objects feeding both fresh mask PCL and `NmtWorkspace.compute_coupling_matrix`;
4. use PyMaster/NaMaster 2.7 and exact band edges `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`;
5. persist the fresh stock workspace using stock `write_to()`; production `get_coupling_matrix()` materialization is forbidden;
6. pass the persisted workspace through the admitted verified OS-mmap exact downstream route and select `wins[0,:,0,:] = TE<-TE`, canonical `<f8 [39,12288]`;
7. preserve durable boundaries `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`, isolated A/B namespaces, fail-closed restore, payload SHA256, contract fingerprint and source-head binding;
8. compare final A/B selected-TE by whole canonical SHA256 equality AND `numpy.array_equal`, with no tolerance/rounding/smoothing/averaging rescue.

Historical Wm_S3 numerical payload import and cross-replica restore remain forbidden. Scientific score remains absent in this gate.

## Corrected frozen resume audit
The v0.2 auditor MUST parse `run_replica` with Python AST and verify the actual call sites inside that function only. It must prove all of the following:
- a call to `validated_finished_receipt(...)` exists inside `run_replica`;
- the verified-final receipt call occurs before the `load_manifest(...,'fresh_workspace_mcm_complete',...)` call;
- that workspace-checkpoint load occurs before the `fresh_or_restore_masks(...)` call;
- after the verified-final receipt assignment and before the workspace-checkpoint load there is a fail-closed early return equivalent to `if done is not None: return done`.

Whole-file textual position of function definitions MUST NOT be used to score resume ordering.

## Other hosted checks
Hosted CI MUST NOT execute DES-scale Wm_S3 numerics. It must also preserve the v0.1 checks for source/blob bindings, Python compilation, exact frozen edges/TE semantics, single-field handoff, stock `write_to()` composition, absence of production `get_coupling_matrix()` materialization, exact comparator, checkpoint order/namespaces/fail-closed identity, 8-core outer-worker declaration with nested thread variables pinned to 1, and no historical numerical import.

Frozen classifications:
- `Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS`
- `Z2_IMPLEMENTATION_CONTRACT_FAIL`
- `Z3_EXACT_COMPARATOR_OR_CHECKPOINT_FAIL`
- `Z4_PROVENANCE_BINDING_FAIL`
- `Z5_INFRASTRUCTURE_FAIL`

Only v0.2 Z1 permits a subsequent fresh activation-readiness audit. Z1 itself does not authorize home science or create Wm_S3 authority.
