# Exp073IG — C2 local tangent prediction artifact admission v0.1

Status: PROSPECTIVELY FROZEN after Exp073IF mapping admission PASS and after creation of the versioned prediction artifact/payload, but before prediction admission result.

## Purpose / ceiling
Hosted static/provenance admission only. Verify that the C2 local tangent prediction artifact is a deterministic 28-coordinate basis built exactly from the admitted HW reference and ID/IC tangent authority. This gate does not evaluate data, likelihood, covariance, survey kernels, or a scientific model gate.

## Frozen identities
- mapping artifact blob `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`; SHA256 `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`.
- prediction artifact `docs/dsir4/predictions/C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_V0_1.md`; blob `7e244010ca65050d0c8edff8fe90a9583845a568`.
- prediction payload `docs/dsir4/predictions/C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_BASIS_V0_1.jsonl`; blob `b3c5dc5ec6aefb79f215c5e01d7baef566cc5251`; SHA256 `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`.
- Exp073IF admission `34250714613 / 102144147469`, exact PASS `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`.
- HW source artifact `10062705321`, ZIP SHA256 `7ea327f0d6e29e4b415c9f66201b266e9015d46a383e8867de94b05665517c00`, reference JSONL SHA256 `2b6eb07c99273292bcb2cf929295071e401e81ed51cfe3f4c3b19d5a395518fb`.
- ID admitted tangent artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`.
- ID-admitted IC candidate source `34249380208 / 10065344213`, response SHA256 `e97ef98a5b137081df5937454f02576d30e726266e9c50733bf399a9be2b1907`.
- admitted finite-difference base step exactly `1e-4`.

## Exact admission checks
1. Re-download exact HW and ID-admitted IC candidate artifacts and verify GitHub ZIP SHA256 provenance.
2. Verify HW reference JSONL SHA256 and IC response SHA256.
3. Reconstruct the 28 prediction-basis rows in z-major/k-minor order using only HW `Delta_m_hex` plus IC `dDelta_dalpha_h1e4_hex` and `dDelta_dbeta_h1e4_hex`; require byte equality to the frozen payload and exact SHA256.
4. Verify all 28 IDs and exact literal coordinates, all binary64 hex values finite, and payload schema exactly `request_id,z_literal,k_literal,Delta_ref_hex,dDelta_dalpha_hex,dDelta_dbeta_hex`.
5. Verify the prediction document binds the exact mapping SHA256, payload SHA256, baseline config/solver provenance and derivative definitions:
   - alpha `(Delta(-h)-Delta_ref)/(-h)`;
   - beta `(Delta(+h)-Delta(-h))/(2h)`;
   - `h=1e-4` only.
6. Verify the exact local rule `Delta_pred = Delta_ref + alpha*dDelta_dalpha + beta*dDelta_dbeta`, alpha left-sided at origin, beta two-sided, and explicit no finite-distance extrapolation/interpolation/QS/tolerance/smoothing rescue.
7. Preserve exact status separation.

## PASS classification
Exact token: `PASS_EXP073IG_C2_LOCAL_TANGENT_PREDICTION_ARTIFACT_ADMISSION_V0_1`.

On PASS only:
- `classification=PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`
- `mapping_ready=true`
- `prediction_artifact_created=true`
- `prediction_ready=true`
- `numerically_evaluated=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=TESTABLE_NOT_EVALUATED`

Any mismatch is fail-closed as implementation/provenance `+0/+0`, never a scientific FAIL. No scientific gate may be evaluated in Exp073IG.