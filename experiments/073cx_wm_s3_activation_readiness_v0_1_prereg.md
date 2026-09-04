# Exp073CX v0.1 — Wm_S3 activation-readiness audit

Status: prospectively frozen support/integration gate. Accounting: +0/+0. This gate cannot create Wm_S3 scientific authority and cannot itself activate Exp073BU.

## Authority bound before execution
- Exp073BU prereg blob: `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`.
- Exp073CW single-mask executable helper blob: `f61b4e42ace7e2ab7220c0df0b38d8663136896c`; admitted raw result: `H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS` from run/job `33860891989 / 100984835847`, head `b7e42a5a9d215990f97943e3ee270ad09127d612`, artifact `9932088071`, ZIP SHA256 `a4a90847e9402b8a96852aef2abd027bea921a1a447b4077b9546f51e4ccb386`.
- Exp073CV production exact adapter blob: `dafe86086a470c852106f0d4ecccbda1d389e397`; admitted result `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS` remains support-only.
- Frozen DES angular authority remains exactly 39 bands, edges `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, ell `0..12287`, selection `TE<-TE`, canonical `<f8 [39,12288]`.

## Frozen activation-readiness checks
The hosted audit must fail closed unless all are true:
1. All three bound blobs above match exactly at the audited source head.
2. Exp073BU A/B namespaces are exactly `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`, with no cross-replica numerical restore/read before both final receipts.
3. Durable boundaries occur exactly in order: `fresh_masks_complete`, `fresh_workspace_mcm_complete`, `mcm_fits_verified`, `full_window_complete`, `selected_te_complete`, `replica_receipt_complete`.
4. Same freshly reconstructed field objects feed fresh PCL and stock workspace; each replica reconstructs lens/source masks only once before `fresh_workspace_mcm_complete`.
5. Production full-window route is stock `write_to()` persistence -> verified OS mmap -> exact full `ncls=2` stock-order downstream -> `TE<-TE`; production `get_coupling_matrix()` materialization is forbidden.
6. Canonical final comparator is exact SHA256 equality AND `numpy.array_equal`; tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P rescue are forbidden.
7. Historical CR/CQ/CM Wm_S3 numerical outputs are not imported as science input/reference.
8. Home execution architecture remains one A-then-B owner, exactly 8 outer workers where applicable, nested BLAS/OpenMP/MKL/OpenBLAS threads pinned to 1, durable payload SHA256 + provenance/contract/source-head/namespace verification and fail-closed restore.
9. Wm_S3 scientific authority remains false and Exp073BU remains not activated during this hosted audit.

## Frozen classification
- `A1_EXP073BU_ACTIVATION_READINESS_PASS`: every check above passes exactly. This only permits a subsequent explicit activation step after a fresh live Actions noncompetition check and process-ledger update.
- `A2_IMPLEMENTATION_CONTRACT_FAIL`: required production/composition contract absent or inconsistent.
- `A3_CHECKPOINT_FAILCLOSED_FAIL`: checkpoint/restore/isolation semantics insufficient.
- `A4_HISTORICAL_IMPORT_FAIL`: forbidden historical Wm_S3 numerical dependency detected.
- `A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: blob/source/runner/audit infrastructure failure before valid classification.

No scientific PASS/FAIL is scored here. No threshold may be weakened after seeing output.
