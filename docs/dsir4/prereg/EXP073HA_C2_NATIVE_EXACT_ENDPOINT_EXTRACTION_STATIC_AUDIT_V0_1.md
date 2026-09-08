# Exp073HA — C2 native exact-endpoint extraction static audit v0.1

Status: PROSPECTIVELY FROZEN after raw-validated Exp073GZ support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Exp073GZ closed the static runtime-admission receipt contract but did not solve how a future runtime producer can bind each frozen `(z,k)` request to an actually accepted native perturbation state without nearest-neighbour, tolerance matching or perturbation-state interpolation. Exp073HA freezes and statically audits the only currently admissible extraction architecture before any new C2 numerical payload is generated.

This gate MUST NOT build or execute CLASS and MUST NOT create recorder payload bytes.

## Frozen upstream identities

- hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`;
- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- pinned `source/perturbations.c` Git blob: `92a48331658c5941ed4eb43b0e98ee78e39b8385`;
- pinned `tools/evolver_ndf15.c` Git blob: `790ced55f2eaa08e805d467734ad1435954bc5b7`;
- GR sampling contract SHA256: `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`;
- recorder blob: `c6144598b9f75908ee27a517d31eda509f7947f6`;
- exact z requests: `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`;
- exact physical-k requests in Mpc^-1: `[0.00067,0.00201,0.0067,0.0201]`;
- request order: z-major / k-minor, exactly 28 requests.

## Frozen extraction architecture

A future producer may use only the following route.

1. **Native exact k insertion.** The requested physical k is converted only by the already frozen exact unit convention required by the solver input. The corresponding requested solver k must be supplied through native `k_output_values`, whose pinned implementation inserts that value into `ppt->k` and records its exact index. No nearest-neighbour lookup, tolerance match, bin centre, rounded `0.067`, effective k or interpolation is allowed.

2. **Native requested-z coordinate resolution.** The literal frozen request z is the authority. The only permitted z-to-conformal-time resolver is the pinned solver's own `background_tau_of_z(pba,z,&tau_target)` on that literal request. This is a coordinate-resolution call inside the pinned solver, not permission to interpolate a perturbation state, replace z by an effective value, or rescue a missed coordinate. No independently reconstructed background or second cosmology is allowed.

3. **Terminal endpoint, not source-table interpolation.** Diagnostic producer mode must make `tau_target` the terminal integration endpoint for the requested run. The accepted ODE state must therefore be the NDF15 `ynew` at `tnew=tfinal=tau_target`. A record obtained through the NDF15 `interp_from_dif(...)` branch, `perturb_sources_at_tau(...)`, a late-source spline, nearest output row, or any post-run time interpolation is invalid for science.

4. **Accepted-state capture only.** The pinned NDF15 path advances `t=tnew`, copies accepted `ynew` into the live state, and then performs its post-accepted-step derivative/print path. Future instrumentation must capture only the accepted terminal state on that path. Newton trial states at the same `tau_target`, rejected steps, intermediate accepted steps, and source-table interpolants must never be admitted as the one runtime record.

5. **Pre-transform matter variables only.** The existing Exp073GM observation-only source binding remains authoritative: capture the current-gauge `ppw->delta_m` and `ppw->theta_m` immediately after native total-matter construction and before the downstream standard gauge-invariant `delta_m` transformation. Do not reuse standard downstream `index_tp_delta_m` and do not apply a second gauge correction.

6. **Observation-only science semantics.** Any future endpoint patch may alter only diagnostic termination/output orchestration. It must not alter perturbation/background equations, species sums, approximation criteria, precision settings, tolerances, accepted physical branch, or downstream scientific gates. The uninstrumented code path must remain byte/logic equivalent when diagnostic mode is absent.

7. **No concurrent global side-channel ambiguity.** If an implementation uses process-global diagnostic state or environment flags to distinguish the accepted endpoint from Newton trial evaluations, the runtime must be frozen to one process/thread for that extraction (`OMP_NUM_THREADS=1`) and the flag must exist only around the already accepted terminal-state callback. A thread-racy capture is invalid for science.

## Static audit requirements

The hosted-only audit must fail closed unless the two pinned upstream blobs match exactly and source text proves all of the following:

- `k_output_values` are explicitly inserted into the solver k list and indexed;
- `perturb_solve` passes the native k mode to the ODE evolver;
- NDF15 explicitly forces `tnew = tfinal` for the terminal step;
- NDF15 calls output with `ynew` when `tnew==t_vec[next]` and uses `interp_from_dif` only in the alternate overshoot branch;
- after a successful step NDF15 assigns `t=tnew`, copies accepted `ynew`, then calls `derivs` before `print_variables` when the print callback is active;
- the final compulsory derivative/print path also receives `tnew,ynew`;
- `perturb_output_data` at nonzero z uses `perturb_sources_at_tau`, establishing why that standard downstream route is forbidden for the raw C2 record;
- the previously frozen no-rescue and pre-transform requirements remain unchanged.

The audit must emit exactly:

`PASS_EXP073HA_C2_NATIVE_EXACT_ENDPOINT_EXTRACTION_STATIC_AUDIT_V0_1`

## Classification

PASS is only `SUPPORT_PLUS_0_PLUS_0` with:

- `cosmological_run_started=false`;
- `record_payload_created=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Failure is `BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`, never a scientific model FAIL.

A PASS authorizes implementation and hosted build-audit of a diagnostic-only exact-endpoint producer patch. It does not authorize real C2 runtime while another home-heavy owner is active, and it does not by itself authorize scientific interpretation.