# C2 diagnostic exact-endpoint implementation anchors v0.1

Status: implementation-support note only. Scope: DSIR4 / hypothesis `C2_IDE_LOCAL_TANGENT_CONE`. Scientific contribution: `SUPPORT_PLUS_0_PLUS_0`. This note does **not** supersede or alter any frozen preregistration, threshold, hypothesis ID, solver equation, approximation criterion, tolerance or scientific authority.

## Authority preserved

This note is subordinate to `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1.md` (blob `fc5f08889f84e628cb789070abd9179a74ef7e04`) and the upstream pin `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Pinned source blobs remain:

- `source/perturbations.c`: `92a48331658c5941ed4eb43b0e98ee78e39b8385`;
- `tools/evolver_ndf15.c`: `790ced55f2eaa08e805d467734ad1435954bc5b7`.

## Verified native endpoint anchors

Inspection of the pinned NDF15 source confirms the exact terminal-step route required by HB:

1. The accepted trial endpoint is held in `ynew`.
2. When the stretched final step is selected, the evolver sets `h = tfinal - t`, then `tnew = tfinal` and purifies `h = tnew - t`.
3. Newton iteration produces `ynew`; a step is accepted only after the error test. Failed steps return to step-size/Jacobian recovery and therefore are not admissible capture points.
4. Only after successful acceptance does the code update the backward-difference history and enter the output block.
5. If `tnew == t_vec[next]`, the output callback receives `ynew+1` directly. The alternate branch calls `interp_from_dif(...)`; that branch is forbidden for diagnostic recorder bytes.

Therefore the future diagnostic extraction must arrange the literal `tau_target` as the actual integration endpoint and exact output coordinate. It must fail closed unless `tnew == tfinal == tau_target == t_vec[next]`; it must never use the interpolation branch as a rescue.

## Verified total-matter anchors

Inspection of the pinned perturbation source confirms that native total-matter construction occurs inside `perturb_einstein(...)` before downstream source serialization:

- matter density contributions are accumulated into `delta_rho_m` and `rho_m`;
- matter momentum contributions are accumulated into `rho_plus_p_theta_m` and `rho_plus_p_m`;
- the native current-gauge values are then assigned as
  - `ppw->delta_m = delta_rho_m/rho_m`,
  - `ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m`;
- source code comments explicitly state that these are the current-gauge values and that the standard downstream path later forms the gauge-independent transfer quantity.

Hence an admissible diagnostic hook must copy `ppw->delta_m` / `ppw->theta_m` **at this exact construction boundary**, before any downstream gauge-invariant/source transformation. Reading ordinary transfer output later is not an equivalent substitute.

## Deterministic prospective patch shape

The least-invasive implementation consistent with HB is now constrained to the following shape:

1. Add an opt-in diagnostic state with default disabled. The disabled path must compile to ordinary upstream behavior and must not alter equations, tolerances, approximations, accepted branches or ordinary outputs.
2. Arm the diagnostic state only for one exact native `k_output_values` member and one literal redshift converted solely by `background_tau_of_z(...)`.
3. Set the diagnostic integration endpoint to that exact `tau_target`; no effective/nearest coordinate is permitted.
4. At the current-gauge matter-construction boundary inside `perturb_einstein(...)`, copy `ppw->delta_m` and `ppw->theta_m` only when the diagnostic state is armed for the exact requested mode. This copy is observation-only.
5. Commit the copied values to the external frozen recorder only from the already accepted terminal endpoint route. Trial Newton states, rejected steps, intermediate accepted steps and interpolated output states are invalid.
6. If process-global diagnostic state is used, extraction must be single-threaded (`OMP_NUM_THREADS=1`) and the hosted HB audit must fail closed if the state can be armed outside the terminal extraction scope.
7. No 28-record/1792-byte runtime set may be produced by the HB build/static audit itself.

## Static-audit obligations before HB PASS

A future HB implementation/workflow must still prove, rather than assume:

- exact prereg and upstream blob identities;
- clean deterministic patch application with no fuzz/rejects;
- default-off behavior and absence of unconditional scientific-path changes;
- native exact-k insertion/indexing and literal-z `background_tau_of_z` resolution;
- direct accepted-`ynew` terminal route and explicit exclusion of `interp_from_dif`/`perturb_sources_at_tau` for recorder bytes;
- capture exactly at the pre-transform `ppw->delta_m` / `ppw->theta_m` boundary;
- successful hosted compilation of the pinned patched solver;
- zero cosmological runs and zero runtime payload records during HB.

Until those checks pass with the frozen HB token, status remains `IMPLEMENTATION_NOT_YET_ADMITTED / SUPPORT_PLUS_0_PLUS_0`, never scientific FAIL.

## Scientific status

`prediction_ready=false`

`scientific_model_authority_created=false`

`G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

No scientific FAIL is created by this implementation-anchor analysis.
