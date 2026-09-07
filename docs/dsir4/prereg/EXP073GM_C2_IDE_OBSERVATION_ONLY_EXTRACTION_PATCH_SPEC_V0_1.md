# Exp073GM — C2 IDE observation-only extraction patch specification v0.1

Status: prospectively frozen support gate. Scope: DSIR only.

Predecessor: validated Exp073GL hosted support PASS, run `34100709411`, job `101674267073`, token `PASS_EXP073GL_C2_IDE_PRETRANSFORM_SOURCE_ELIGIBILITY_STATIC_AUDIT_V0_1`.

## Authority ceiling

This experiment can create only `SUPPORT_PLUS_0_PLUS_0`. It cannot set `prediction_ready=true`, cannot create `G_DOMAIN_MAPPING` authority, cannot create scientific model PASS/FAIL, and cannot launch C2 numerical generation by itself.

## Frozen solver/source

Pinned solver lineage: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

The observation hook must be read-only with respect to CLASS evolution state and equations. It may copy values into a side-channel/output structure but must not mutate `y`, `dy`, `ppw->delta_m`, `ppw->theta_m`, background quantities, interaction parameters, or any perturbation/evolution equation.

## Frozen tap semantics

The eligible tap is inside `perturb_einstein` after the successful call to `perturb_total_stress_energy(...)` and before the native gauge-invariant correction of `ppw->delta_m`.

At that point the observation payload is exactly the current-gauge pair produced by `perturb_total_stress_energy`:

- `delta_m_current = ppw->delta_m = delta_rho_m/rho_m`;
- `theta_m_current = ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m`;
- `a = ppw->pvecback[pba->index_bg_a]`;
- `H = ppw->pvecback[pba->index_bg_H]`;
- `k2 = k*k` already belongs to the caller context.

The native downstream CLASS correction remains untouched. The observation payload must therefore be captured before that correction and must never apply a second correction to standard exported `index_tp_delta_m`.

## Frozen C2 bridge quantity

A later separately authorized generator may form a gauge-aware quantity from the pre-transform payload according to the already frozen C2 extraction/generation contract. Exp073GM itself only freezes and audits the source tap; it does not calculate or admit a prediction artifact.

## Fail-closed requirements

Static audit PASS requires all of the following against the pinned source commit:

1. exact IDE matter-density arithmetic contribution using `index_bg_rho_idm_iv` and `index_pt_delta_idm_iv` exists;
2. exact IDE matter-momentum arithmetic contribution using `index_bg_rho_idm_iv` and `index_pt_theta_idm_iv` exists with the synchronous-gauge special case preserved;
3. current-gauge assignments `ppw->delta_m = delta_rho_m/rho_m` and `ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m` exist;
4. `perturb_total_stress_energy(...)` is called before the native `ppw->delta_m` gauge correction in `perturb_einstein`;
5. native `index_bg_a`, `index_bg_H`, and caller `k2` are available at the boundary;
6. the proposed patch specification is observation-only and explicitly forbids solver-state/equation mutation and double transformation.

Any mismatch is `IMPLEMENTATION/STATIC_FAIL_PLUS_0_PLUS_0`, never a scientific model failure.

Expected token: `PASS_EXP073GM_C2_IDE_OBSERVATION_ONLY_EXTRACTION_PATCH_SPEC_STATIC_AUDIT_V0_1`.
