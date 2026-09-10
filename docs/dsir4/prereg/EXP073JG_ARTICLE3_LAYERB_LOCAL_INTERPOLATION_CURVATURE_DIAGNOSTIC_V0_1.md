# Exp073JG — Article 3 Layer-B local interpolation curvature diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JF AND BEFORE ANY EXP073JG NUMERICAL OUTPUT.

## Bound authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: retained 107, f_B=0, native production-vs-dense maximum 0.9998247463807295 > REL_TOL=1e-3. Covariance restriction and Wm_S3 remain unauthorized.

Exp073JF is validated support-only `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`, run/job `34480349238 / 102881291672`, artifact `10153458465`, independently verified ZIP SHA256 `f71c1603f46e622a6c71ebab6733d30e9633cc92e9dc50a98cecdf364b28fffb`. At N=384 and N=512, kpd10-vs-kpd20 discrepancy is exactly 0.0 at both historical worst probes, but no N satisfies the unchanged exact-k reference criterion simultaneously for alpha and beta. N=512 errors are alpha=0.00010245604306152275 and beta=0.026575285704422986. Thus simple global geomspace density up to current exact capacity is numerically inadequate under the frozen criterion.

## Purpose
Isolate whether the remaining N=512 beta error is dominated by local interpolation curvature rather than solver/native-density dependence. This experiment is a support-only counterfactual diagnostic. It cannot create Layer-B authority and cannot authorize a replacement estimator.

## Frozen execution
Use exact pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant d_m exposure, exact baseline/precision files, h=1e-4, same four models and same historical probes as Exp073JE/JF.

Fixed shared physical-k grid is exactly N=512 `np.geomspace(1e-4,0.06664762008318016,512,dtype=float64)`. Target k values MUST NOT be inserted. Native-density cross-check remains `k_per_decade_for_pk` in {10,20}. Infrastructure-only capacity patches remain `_MAX_NUMBER_OF_K_FILES_ 30 -> 512` and `_ARGUMENT_LENGTH_MAX_ 1024 -> 32768`, with exact provenance checks.

For each probe/model/kpd, locate the unique bracketing fixed nodes `lo < target < hi` and require that requested-node coordinate recovery is exact within LOOKUP_REL_TOL=1e-12. Evaluate d_m(target) in x=ln(k) using four prospectively fixed local interpolation rules:

1. `linear_bracket`: degree-1 polynomial through {lo,hi}; this MUST reproduce the Exp073JF N=512 response exactly or the run is infrastructure-invalid.
2. `quadratic_left`: degree-2 polynomial through {lo-1,lo,hi}.
3. `quadratic_right`: degree-2 polynomial through {lo,hi,hi+1}.
4. `cubic_centered`: degree-3 polynomial through {lo-1,lo,hi,hi+1}.

Polynomial evaluation MUST be direct deterministic Lagrange interpolation in binary64 on x=ln(k); no smoothing, averaging, spline, adaptive fit, target insertion, effective coordinates, fiducial-P shortcut or tolerance change is permitted.

For each interpolation rule, form the same finite-difference responses: alpha-left `(d_m(alpha_left)-d_m(ref))/(-h)` and beta-symmetric `(d_m(beta_plus)-d_m(beta_minus))/(2h)`, take absolute response, and compare with unchanged exact-k references:
- alpha-left exact response = 11.514018402323245;
- beta-symmetric exact response = 1.9210920856949087.

Relative difference is unchanged: `abs(a-b)/max(abs(a),abs(b))`. REL_TOL remains exactly 1e-3.

## Frozen interpretation
This experiment is diagnostic only. A rule is `curvature_candidate=true` only if, for both probes and both kpd values, response is finite and positive, exact-reference relative error <1e-3, and kpd10-vs-kpd20 discrepancy <1e-3. Candidate status does not authorize use in Layer-B.

The diagnostic MUST also report the signed difference of each higher-order response from `linear_bracket`, the two one-sided quadratic predictions, and the cubic prediction. A strong reduction of beta exact-reference error with agreement between the two quadratic rules and cubic rule is evidence that local curvature dominates the residual N=512 interpolation error. Disagreement/oscillation is evidence against a simple local-curvature explanation and requires another prospectively frozen mechanism diagnostic.

If at least one higher-order rule qualifies, the next admissible work is a separate prospective full-support feasibility audit of a grid-invariant evaluation architecture; no scientific rerun is authorized by Exp073JG alone. If none qualifies, continue mechanism isolation without further simple density extrapolation and without tolerance rescue.

Classification: valid complete observations -> `LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0`; any lineage/hash/build/capacity/requested-node/linear-parent reproduction failure -> `INVALID_INFRA_PLUS_0_PLUS_0`.

All outcomes are support-only +0/+0. Global frozen DSIR boundaries, REL_TOL=1e-3, h=1e-4, no effective-coordinate/fiducial-P/tolerance/rounding/smoothing/averaging rescue remain unchanged.
