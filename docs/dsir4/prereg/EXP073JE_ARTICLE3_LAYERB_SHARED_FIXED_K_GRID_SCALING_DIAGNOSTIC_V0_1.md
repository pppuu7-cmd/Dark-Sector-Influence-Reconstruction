# Exp073JE — Article 3 Layer-B shared fixed-k grid scaling diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JD AND BEFORE ANY EXP073JE NUMERICAL OUTPUT.

## Bound authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 107 retained coordinate rows, `f_B=0`, exact native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized.

Exp073JD is validated support-only `EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0`, run/job `34472918931 / 102856790715`, artifact ZIP SHA256 `1eb87185c6015277eeae72e3dd9017f48df03e8b166c05cde514330667189478`. At the two historically worst probes, exact internal-k injection gave identical kpd=10 and kpd=20 responses: alpha-left `11.514018402323245`, beta-symmetric `1.9210920856949087`, both relative discrepancies exactly `0.0`, with coordinate mismatch exactly `0.0`.

## Motivation and source-level constraint
The pinned CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c` defines `_MAX_NUMBER_OF_K_FILES_ 30`, so unmodified `k_output_values` cannot directly inject the many k atoms required by the full DES Limber support. A brute-force per-atom exact-k architecture is therefore not a suitable production design.

Exp073JE tests a scalable numerical architecture: a model-invariant, explicitly injected, fixed physical-k support grid. Responses are interpolated only between these common injected nodes, never between model-dependent native k nodes. The maximum-k-output constant may be enlarged from 30 to 512 by a one-line infrastructure patch. This patch changes only storage capacity for requested k nodes; it MUST NOT alter perturbation equations, transfer definitions, finite-difference operator, tolerances, cosmological inputs, or the public gauge-invariant `d_m` exposure.

## Purpose
Determine whether interpolation on a sufficiently dense **shared fixed physical-k grid** converges to the exact-k Exp073JD responses at the two historical worst probes, and whether the result is invariant to the otherwise irrelevant native `k_per_decade_for_pk` choice.

This is a support-only mechanism/scaling diagnostic. It does not rerun the 107-row Layer-B science gate.

## Frozen execution
Use exact pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant `d_m` exposure patch, exact baseline/precision inputs, finite-difference `h=1e-4`, and models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

Historical probes:
- alpha-left: `z=0.7000000000000001`, `k=0.002502504647141259 Mpc^-1`, exact-k reference response `11.514018402323245`;
- beta-symmetric: `z=0.9351`, `k=0.01860440444314368 Mpc^-1`, exact-k reference response `1.9210920856949087`.

Shared-grid domain: `[K_FIXED_MIN, K_FIXED_MAX] = [1e-4, 0.06664762008318016] Mpc^-1`.

Shared-grid node counts: `N in {64,128,256}`. For each N, nodes are `np.geomspace(K_FIXED_MIN,K_FIXED_MAX,N,dtype=float64)` and are identical literal physical k values for every model and every native-density run. Neither historical target k may be inserted explicitly into these grids; exact target coincidence within relative `1e-14` makes that N invalid infrastructure rather than a scientific pass.

Native-density cross-check: `k_per_decade_for_pk in {10,20}`.

For each `(N,kpd,model)`:
1. Enlarge only `_MAX_NUMBER_OF_K_FILES_` from 30 to 512 before building pinned CLASS-IV; verify exactly one source replacement and retain pre/post source SHA256.
2. Supply all N fixed physical nodes through `k_output_values`.
3. Compute the same `mTk` transfer/source stack.
4. At each probe redshift, retrieve the public class-format transfer table and the public patched `d_m` column.
5. Convert transfer k coordinate to physical `Mpc^-1` using the model's own `h` where required.
6. Locate every requested fixed node by nearest-coordinate identity. Every node used by a target bracket must have relative coordinate mismatch `<=1e-12`; otherwise INVALID_INFRA.
7. Construct target `d_m` only by linear interpolation in `ln(k)` between the two neighboring **requested fixed nodes** around the target. Native non-requested CLASS k nodes MUST NOT enter the interpolation.
8. Compute alpha-left one-sided and beta-symmetric responses with frozen `h=1e-4` exactly as in Exp073IR/JD.
9. For each response, compute exact relative error to the corresponding Exp073JD exact-k reference, `abs(approx-exact)/max(abs(approx),abs(exact))`.
10. For each N/probe, compute kpd10-vs-kpd20 discrepancy by the same relative formula.

## Frozen interpretation
Reference threshold remains historical `REL_TOL=1e-3`; it is not retuned.

A node count N is `scaling_candidate=true` only if, for both probes and both kpd values:
- response is finite and positive;
- exact-reference relative error `<1e-3`; and
- kpd10-vs-kpd20 response discrepancy `<1e-3`.

If at least one N is a scaling candidate, the smallest qualifying N may be nominated prospectively for a separate full-support feasibility/audit design. This nomination does NOT authorize Layer-B science, does NOT retroactively PASS Exp073IR, and does NOT authorize covariance restriction.

If no N qualifies, the shared fixed-grid interpolation architecture is not yet numerically adequate on the frozen ladder; mechanism/scaling isolation must continue without tolerance rescue.

## Frozen classifications
- `SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0`: complete valid observations produced.
- `INVALID_INFRA_PLUS_0_PLUS_0`: source/hash/build/interface/node-injection/execution/provenance prevents valid observation.

All valid outcomes are support-only `+0/+0`. No Wm_S3, covariance, model, or manuscript authority is created.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; finite-difference `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
