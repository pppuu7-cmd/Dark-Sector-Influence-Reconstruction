# Exp073IE — C2 six-component residual mapping source audit v0.1

Status: PROSPECTIVELY FROZEN AFTER Exp073ID NUMERICAL TANGENT ADMISSION AND BEFORE C2 DOMAIN-MAPPING ADMISSION.

## Purpose and ceiling
Audit whether the exact pinned C2 implementation contains sufficient source-level evidence to construct the six DSIR-4 residual components under the already-frozen common residual convention. This is hosted-only source/readiness support. It does **not** create a prediction artifact, does not evaluate an observational gate, and cannot set `G_DOMAIN_MAPPING=PASS`.

## Frozen identities
- hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`
- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`
- C2 baseline repo blob: `cd2beb01ce6575f97f2e3203226ed6d4f048dcaa`
- C2 baseline SHA256: `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`
- DSIR-4 common residual convention repo blob: `9ab68fe254891a076e24757de724e32e2190bfb6`
- DSIR-4 model-mapping contract repo blob: `03fd11d8536b9743eb82f92f9a0d5386444079ed`
- admitted numerical tangent response: Exp073ID run `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, base step `1e-4`.

## Frozen common-source interpretation to audit
`T_known` is the DSIR-4 frozen ordinary sector: baryons, photons and frozen standard neutrinos. The C2 candidate dark matter `idm_iv` and interacting vacuum `iv` are excluded from `T_known`, so their **total** stress-energy is the C2 residual source. Internal transfer `Q` is provenance/bookkeeping and must not be added as a seventh residual component.

The source audit must require `gauge = synchronous` in the exact C2 baseline and prove the following solver-bound six-component formulas from the pinned implementation:

1. `rho_X = rho_idm_iv + rho_iv` — both background densities are explicitly present and both enter total density.
2. `p_X = -rho_iv` — idm contributes zero background pressure; iv contributes negative density to total pressure.
3. `delta_rho_X = rho_idm_iv * delta_idm_iv` in the pinned synchronous solver representation — the IDE block explicitly adds exactly this term to total perturbed stress-energy and exposes no independent vacuum-density perturbation state.
4. `q_X = 0` in the pinned synchronous representation — the idm_iv velocity state is absent/set to zero by the solver gauge choice, while vacuum has `rho+p=0`; the audit must require the source literal documenting synchronous idm_iv velocity zero/absent and must not infer a nonzero q from another gauge.
5. `delta_p_X = 0` in this pinned solver representation — the idm_iv total perturbed-stress block changes `delta_rho` (and non-synchronous momentum) but contains no `delta_p` contribution; no independent iv perturbation state is defined.
6. `pi_X = 0` in this pinned solver representation — the idm_iv total perturbed-stress block contains no shear/anisotropic-stress contribution.

These are source-bound mapping formulas for this solver/gauge implementation, not claims that arbitrary interacting-vacuum parameterizations share the same perturbation prescription.

## Interaction provenance
The audit must prove the pinned interaction convention contains
`Q = alpha_idm_iv * H * rho_idm_iv + beta_idm_iv * H * rho_iv`
(or source-equivalent exact terms) and record that Q enters component conservation/evolution while the DSIR common residual is the total idm_iv+iv stress-energy.

## Domain/readiness boundary
The audit must also verify the C2 baseline/request plan remains within the frozen DSIR domain `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`, but it must not upgrade this static/source proof to a domain-mapping PASS. A later versioned mapping artifact must bind these six formulas, exact source fingerprints, gauge, parameter domain/branch assumptions, and prediction lineage.

PASS token: `PASS_EXP073IE_C2_SIX_COMPONENT_RESIDUAL_MAPPING_SOURCE_AUDIT_V0_1`.

On PASS only:
- `classification=SUPPORT_PLUS_0_PLUS_0`
- `six_component_source_mapping_ready=true`
- `mapping_artifact_created=false`
- `mapping_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any missing source evidence must fail closed and identify the missing component; it may not be silently labeled zero.