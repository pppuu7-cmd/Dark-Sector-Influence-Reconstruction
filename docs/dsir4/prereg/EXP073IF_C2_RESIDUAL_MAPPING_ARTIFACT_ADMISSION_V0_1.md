# Exp073IF — C2 residual mapping artifact admission v0.1

Status: PROSPECTIVELY FROZEN after Exp073IE source-audit PASS and after creation of the frozen mapping artifact, but before any mapping admission result is observed.

## Purpose and ceiling
Admission-only gate for `docs/dsir4/mappings/C2_IDE_LOCAL_TANGENT_CONE_MAPPING_V0_1.md`. It verifies exact artifact identity, six-component completeness, source/provenance bindings, gauge/sector convention and certified domain. It does not generate a prediction, evaluate an observational gate, or create scientific model authority.

## Frozen identities
- mapping artifact blob: `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`
- mapping creation commit: `543661eb745e075ffcaf6a00b8d7f4b13842740d`
- common residual convention blob: `9ab68fe254891a076e24757de724e32e2190bfb6`
- model mapping contract blob: `03fd11d8536b9743eb82f92f9a0d5386444079ed`
- baseline config blob: `cd2beb01ce6575f97f2e3203226ed6d4f048dcaa`
- baseline config SHA256: `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`
- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`
- pinned source SHA256: `background.c=7a6ad5d44c316c886fc15c3439e04217c6c480f0dc251e8080aa64643ce1c6fc`; `perturbations.c=61e73ed7d5b785ea5f49620e782c58ec552d2735640a1c1241d5ef354e7e0cbe`
- source-audit authority: Exp073IE `34250165394 / 102142253548`, exact PASS token `PASS_EXP073IE_C2_SIX_COMPONENT_RESIDUAL_MAPPING_SOURCE_AUDIT_V0_1`
- admitted tangent response: Exp073ID `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, base step `1e-4`.

## Exact admission requirements
The frozen mapping artifact must contain and bind, without synonym substitution that changes meaning:
1. `rho_X = rho_idm_iv + rho_iv`.
2. `p_X = -rho_iv`.
3. `delta_rho_X = rho_idm_iv * delta_idm_iv` in the pinned synchronous representation.
4. `q_X = 0` as a synchronous structural zero.
5. `delta_p_X = 0` as a structural zero.
6. `pi_X = 0` as a structural zero.

It must state that `T_known` excludes `idm_iv` and `iv`, that the authoritative residual is total `idm_iv+iv`, and that `Q = alpha_idm_iv*H*rho_idm_iv + beta_idm_iv*H*rho_iv` is internal transfer bookkeeping rather than an additional residual component.

It must bind the exact pinned solver commit/source hashes, baseline config identity, synchronous gauge, common residual convention and mapping contract.

Certified coordinate domain must be exactly `0.295<=z<=2.33` and `0<k<=0.06664762008318016 Mpc^-1`. It must explicitly forbid effective-coordinate/interpolation/extrapolation rescue and state the linear scalar/pinned-solver/local-tangent regime assumptions.

The artifact must preserve status separation: no prediction artifact and no scientific PASS are created by admission.

## Classification
PASS token: `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`.

On PASS only:
- `classification=MAPPING_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`
- `six_component_source_mapping_ready=true`
- `mapping_artifact_created=true`
- `mapping_ready=true`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=TESTABLE_NOT_EVALUATED`

Any mismatch is fail-closed as implementation/provenance failure `+0/+0`; scientific status is unchanged.