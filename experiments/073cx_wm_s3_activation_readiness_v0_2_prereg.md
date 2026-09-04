# Exp073CX v0.2 — Wm_S3 production-bound activation-readiness audit

Status: prospectively frozen hosted support/integration gate. Accounting: `+0/+0`. This gate cannot create Wm_S3 scientific authority and cannot itself activate Exp073BU.

## Historical context
Exp073CX v0.1 remains immutable `A2_IMPLEMENTATION_CONTRACT_FAIL` because the unified production A/B driver did not yet exist at that audit head. Exp073CZ v0.1 subsequently recorded an immutable verifier-scope Z2, and Exp073CZ v0.2 then returned `Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS` for the unchanged production-driver arithmetic. CX v0.2 is a new prospective readiness audit after that support closure; it does not reinterpret any earlier outcome.

## Authority bound before execution
The hosted auditor must bind all of the following exact Git blobs:
- this preregistration;
- Exp073BU science prereg `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`, blob `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`;
- Exp073CW single-mask helper `ci/exp073cw_single_mask_integrated_driver_v0_1.py`, blob `f61b4e42ace7e2ab7220c0df0b38d8663136896c`;
- Exp073CV exact production adapter `ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py`, blob `dafe86086a470c852106f0d4ecccbda1d389e397`;
- unified Exp073BU production A/B driver `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py`, blob `5c8d5d3463e455389a1ca3df2639bf06a3b7b603`;
- immutable Exp073CZ v0.2 Z1 recovery `recovery/2026-09-04_exp073cz_v0_2_z1_scoped_driver_integration_pass.md`, blob `140b65be4901af3893a75f770ab20a9eed9f2f14`.

The CZ recovery must contain run/job/head `33871304159 / 101017678531 / b7cc90467006718a115b4dba40962cc8275f1c69`, artifact `9935990587`, ZIP SHA256 `f9fdc68c951362c8f0b04cd0c48b3f88f9f9e77b7ddb37b3b4e74c8f095c93b6`, receipt SHA256 `03938c3b2f2759a60be1f4d5bfdd6eb23018e9507e0a6688ba20364e02eaa5b1`, and classification `Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS`.

## Frozen activation-readiness checks
Hosted CI must fail closed unless all are true:
1. Every bound blob above matches exactly at the audited source head.
2. Frozen angular authority is unchanged: 39 bands with edges `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, ell `0..12287`, selected `TE<-TE`, canonical `<f8 [39,12288]`.
3. Production A/B namespaces are exactly `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`; historical Wm_S3 numerical import and cross-replica numerical reads/restores remain false.
4. Durable boundaries remain exactly ordered `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete` with source-head, contract-fingerprint, payload-SHA and namespace fail-closed identity.
5. The exact production driver is the one admitted by CZ Z1. Its same reconstructed field pair feeds fresh PCL and stock workspace; stock `write_to()` persistence is used; production `get_coupling_matrix()` materialization is forbidden; verified exact mmap downstream and `TE<-TE` semantics remain composed.
6. Final A/B comparator requires selected-TE SHA256 equality AND `numpy.array_equal`; tolerance, rounding, smoothing, averaging, effective ell/z/k and fiducial-P rescue are forbidden.
7. Execution contract remains one owner running A then B, `OUTER_COMPUTE_WORKERS=8`, with `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`.
8. Hosted audit performs no DES-scale Wm_S3 numerical science; `science_gate_scored=false`, `wm_s3_authority_created=false`, `exp073bu_activated=false`.

## Frozen classification
- `A1_EXP073BU_ACTIVATION_READINESS_PASS`: all checks pass exactly. This authorizes only a subsequent fresh live Actions noncompetition/preflight check and explicit process-ledger activation step.
- `A2_IMPLEMENTATION_CONTRACT_FAIL`: production/composition contract absent or inconsistent.
- `A3_CHECKPOINT_FAILCLOSED_FAIL`: checkpoint, namespace, restore, or exact-comparator semantics insufficient.
- `A4_HISTORICAL_IMPORT_FAIL`: forbidden historical Wm_S3 numerical dependency detected.
- `A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: blob/source/audit infrastructure failure before valid classification.

No Wm_S3 science PASS/FAIL is scored here. No frozen criterion may be weakened after seeing output.
