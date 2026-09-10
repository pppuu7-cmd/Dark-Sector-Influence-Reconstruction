# Exp073JF — Article 3 Layer-B shared fixed-k grid extended-density diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JE AND BEFORE ANY EXP073JF NUMERICAL OUTPUT.

## Bound authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: retained 107, f_B=0, native production-vs-dense maximum 0.9998247463807295 > REL_TOL=1e-3. Covariance restriction and Wm_S3 remain unauthorized.

Exp073JE is validated support-only `SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0`, run/job `34474978911 / 102863474356`, artifact `10151168583`, independently verified ZIP SHA256 `cf2e70a8bb35dcdb782d49fe5a29b908f6897169d6fe2c055c9b92eb1bfa01af`. For N={64,128,256}, kpd10-vs-kpd20 discrepancy is exactly 0.0 at both historical worst probes, proving the common injected grid removes the diagnosed native-density dependence there. However no frozen N qualifies against exact-k reference at REL_TOL=1e-3.

## Purpose
Test whether the same already-defined shared fixed physical-k interpolation architecture becomes adequate at the largest node densities allowed by the prospectively repaired CLASS-IV k-output capacity, without changing the estimator, threshold, finite-difference step, target probes, interpolation rule, or physics.

## Frozen execution
Use exact pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, the audited public gauge-invariant d_m exposure, exact baseline/precision files, h=1e-4, and the same four models as Exp073JE.

Historical probes and exact-k references are unchanged:
- alpha-left: z=0.7000000000000001, k=0.002502504647141259 Mpc^-1, exact response 11.514018402323245;
- beta-symmetric: z=0.9351, k=0.01860440444314368 Mpc^-1, exact response 1.9210920856949087.

Shared-grid domain remains [1e-4, 0.06664762008318016] Mpc^-1. Nodes remain `np.geomspace(KMIN,KMAX,N,dtype=float64)` and target k values MUST NOT be inserted explicitly. Native-density cross-check remains k_per_decade_for_pk in {10,20}.

The only new prospective ladder is N in {384,512}. The already-preregistered infrastructure-only patches remain `_MAX_NUMBER_OF_K_FILES_ 30 -> 512` and `_ARGUMENT_LENGTH_MAX_ 1024 -> 32768`, each with exact one-replacement and SHA provenance. No other CLASS source changes are permitted beyond previously audited compatibility and public-d_m exposure patches.

For every N/kpd/model, use the exact Exp073JE requested-node identity checks and ln(k) interpolation between neighboring requested common fixed nodes. Relative error is the unchanged `abs(approx-exact)/max(abs(approx),abs(exact))`. kpd cross-check uses the same formula.

## Frozen interpretation
REL_TOL remains exactly 1e-3.

N is `scaling_candidate=true` only if for both probes and both kpd values: response finite and positive; exact-reference relative error <1e-3; and kpd10-vs-kpd20 discrepancy <1e-3.

If at least one N qualifies, the smallest qualifying N may be nominated prospectively for a separate full-support feasibility audit. This creates no Layer-B scientific authority.

If neither 384 nor 512 qualifies, simple global geomspace density up to the current exact capacity is declared numerically inadequate for the frozen worst probes. The next admissible work is mechanism isolation of interpolation phase/curvature or a prospectively specified grid-invariant architecture; no further density extrapolation or tolerance rescue may be inferred from this result alone.

Classification: valid complete observations -> `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`; source/hash/build/interface/capacity/injection failure -> `INVALID_INFRA_PLUS_0_PLUS_0`.

All outcomes are support-only +0/+0. Global frozen DSIR boundaries, REL_TOL=1e-3, h=1e-4, no effective-coordinate/fiducial-P/tolerance/rounding/smoothing/averaging rescue remain unchanged.
