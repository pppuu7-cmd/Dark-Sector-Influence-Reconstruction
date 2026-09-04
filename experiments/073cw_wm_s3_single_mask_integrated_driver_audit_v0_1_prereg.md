# Exp073CW — Wm_S3 single-mask integrated-driver assembly audit v0.1

**Frozen:** 2026-09-04, before Exp073CW numerical output. DSIR only.

## Purpose
Close the remaining executable-driver integration prerequisite after authoritative Exp073CV v0.3 `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS +0/+0`. This is hosted support/integration QA only. It cannot create Wm_S3 scientific authority or activate Exp073BU.

## Frozen authority
- Exp073BU prereg commit: `e1a0332c128c87049fb8699018a3a3e71c9c5321`.
- Exp073CV v0.3 immutable PASS commit: `df49dcb50d5ccffb7b29d030ed8f1f99cbf4cdd6`.
- Fresh-PCL helper source commit: `e6ffda3b5c558c964cf486d78a792d40bf9c76e5`.
- NaMaster/PyMaster lineage: 2.7 only.
- DES geometry remains NSIDE=4096, ell=0..12287.
- Frozen band edges exactly `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, exactly 39 bands.
- Full window semantics `[2,39,2,12288]`, selected `wins[0,:,0,:]` = `TE <- TE`, canonical `<f8 [39,12288]`.

## Single-mask handoff invariant
A production replica must reconstruct the S3 dense count map and lens mask exactly once per fresh replica, construct exactly one spin-0 lens `NmtField` and one spin-2 source `NmtField`, then use those same field objects for both:
1. fresh replica-local mask-PCL derivation from their mask ALMs; and
2. `NmtWorkspace.compute_coupling_matrix(field0, field2, binning)`.

No second call to either mask-reconstruction routine is permitted before `fresh_workspace_mcm_complete`. The fields may be released only after the workspace MCM has been persisted and verified at the frozen checkpoint boundary.

## Checkpoint sequence
Preserve Exp073CD order exactly:
`fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`.

`fresh_masks_complete` must bind canonical SHA256 identities of both freshly reconstructed dense masks plus the exact field construction semantics. Restore is fail-closed and replica-local. Cross-replica numerical restore is forbidden.

## Hosted audit
The hosted audit must:
- statically bind the exact 40 band-edge values above and verify 39 intervals ending at 12288;
- verify production driver source contains one reconstruction call per mask and passes the same field objects to both PCL and workspace stages;
- execute a low-resolution synthetic analogue under PyMaster 2.7 in which instrumented reconstruction counters are exactly one each, one pair of field objects is reused, and the full stock workspace/window path completes;
- verify selected component semantics are `TE <- TE`;
- verify no historical Wm_S3 numerical payload is read and no tolerance/rounding/smoothing/averaging rescue exists.

Synthetic dimensions are support QA only and do not alter DES scientific arithmetic or authority.

## Frozen classifications
- `H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS`: all static and executable invariants pass. Accounting `+0/+0`; permits the next activation-readiness audit only.
- `H2_MASK_RECONSTRUCTION_DUPLICATED`: executable/static evidence shows a mask is reconstructed more than once before workspace persistence. `+0/+0` blocking integration result.
- `H3_FIELD_HANDOFF_NOT_IDENTICAL`: PCL and workspace do not consume the exact same field object identities. `+0/+0` blocking integration result.
- `H4_CONTRACT_OR_BINDING_FAIL`: band-edge/provenance/source binding is invalid or ambiguous. `+0/+0`, fail closed.
- `H5_INFRASTRUCTURE_FAIL`: dependency/workflow/runtime failure prevents classification. `+0/+0`.

No classification from Exp073CW creates Wm_S3 authority. Exp073BU remains NOT ACTIVATED until a later explicit activation-readiness PASS and live exclusivity check.