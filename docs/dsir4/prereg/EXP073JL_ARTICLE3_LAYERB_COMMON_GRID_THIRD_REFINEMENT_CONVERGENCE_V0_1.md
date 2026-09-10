# Exp073JL — Article 3 Layer-B common-grid third-refinement convergence v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 support only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JK AND BEFORE ANY EXP073JL RESPONSE OUTPUT.

## Bound authority

Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; covariance restriction and Wm_S3 remain unauthorized.

Validated Exp073JK run/job `34495159732 / 102931623100`, artifact `10160083225`, independently verified ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`, is support-only `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. It retained all 107 rows with zero unsupported targets but had maximum atomic relative component difference `0.016330535730270664 > 1e-3`. The measured JJ-to-JK reduction factor is `2.2828488538078164`; this value is interpretation only and does not alter the acceptance rule.

Validated JI geometry authority remains fixed: target range `[0.00033800000000000003, 0.06664596609379447] Mpc^-1`, geometry stream SHA256 `79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a`, and response-blind minimal centered-cubic support requires one upper same-ratio guard and no lower guard for the grids used here.

## Purpose

Measure the immediately next independent shared-grid resolution step without changing estimator, physical support or acceptance threshold. Exp073JL compares the previously tested fine architecture from JK (base N=2048 + one upper guard = 2049 requested nodes) against the next sequential refinement (base N=4096 + one upper guard = 4097 requested nodes).

This is a sequential convergence test, not a search for a passing grid. No result-dependent grid density, tolerance, masking or estimator change is permitted.

## Frozen lattices

Judged physical support remains unchanged.

Coarse architecture:
- base `C2048 = np.geomspace(1e-4,0.06664762008318016,2048,dtype=float64)`;
- response-blind guard counts exactly `(lower,upper)=(0,1)`;
- requested-node count exactly 2049.

Fine architecture:
- base `F4096 = np.geomspace(1e-4,0.06664762008318016,4096,dtype=float64)`;
- same frozen JI target extrema and same minimal centered-cubic support derivation;
- prospectively required guard counts exactly `(0,1)`;
- requested-node count exactly 4097.

Both lattices must independently prove complete centered-cubic stencil coverage before response evaluation. Base nodes must remain bitwise unchanged inside the guarded lattices.

## Frozen physical/numerical evaluation

Use the exact original Exp073IR parent lineage, 53 DES + 54 BOSS retained-coordinate support and unchanged atom traversal/accounting.

Use pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant `d_m`, exact baseline/precision inputs, and the same four finite-difference models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)` with frozen `h=1e-4`.

CLASS native `k_per_decade_for_pk` remains frozen to `20` for both suites. Inherited Exp073IR suite slot `10` maps deterministically to guarded N=2048 and slot `20` maps to guarded N=4096; these inherited labels MUST NOT be interpreted as native-kpd values.

For every suite/model/redshift:
1. inject the full guarded common physical-k lattice with `k_output_values`;
2. recover every requested node from public transfer output with relative coordinate mismatch `<=1e-12`;
3. interpolate only between requested common nodes using unchanged centered-cubic Lagrange interpolation in `x=ln(k)` with stencil `{j-2,j-1,j,j+1}`;
4. compute the inherited alpha-left one-sided and beta-symmetric finite-difference responses with frozen `h=1e-4`;
5. reuse exact Exp073IR atomic comparison, finite/nonzero, row-label, BOSS dense-z and Layer-B accounting logic.

## Frozen infrastructure-only capacities

A response-blind audit completed before the JK result showed that the analogous guarded N=4096 lattice serializes to approximately 89918 characters under the exact `.17g` `k_output_values` representation. Therefore Exp073JL prospectively enlarges only infrastructure capacities:

- `_MAX_NUMBER_OF_K_FILES_`: 30 -> `4608`;
- `_ARGUMENT_LENGTH_MAX_`: 1024 -> `131072`.

Exact one-replacement and pre/post SHA256 provenance are mandatory. These capacity changes do not alter equations, transfer definitions, masks, physical domain, finite-difference arithmetic, interpolation, support or thresholds.

## Frozen decision

A valid complete Exp073JL run is `COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` only if all are true:
- exact JK/JI authority identity and frozen geometry are enforced;
- requested counts are exactly 2049 and 4097 with guard counts `(0,1)` for each;
- zero unsupported target evaluations in both suite slots;
- no finite/nonzero-status change, row-label change or BOSS dense-z disagreement;
- maximum atomic coarse-vs-fine relative component difference is `< REL_TOL=1e-3`;
- inherited Layer-B invalid-row fraction under coarse accounting is `<=0.05` and retained dimension `>=15`;
- requested-node coordinate mismatch is `<=1e-12`.

Otherwise a valid numerical run is `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Lineage/hash/build/parser/capacity/grid/stencil/provenance failures are `INVALID_INFRA_PLUS_0_PLUS_0`.

## Interpretation boundary

Exp073JL is support-only `+0/+0` in every valid outcome. If converged, it may authorize only the design of a separate prospectively frozen scientific Layer-B numerical rerun using a predeclared converged shared-grid architecture. It does not itself retroactively pass Exp073IR, authorize covariance restriction, open Wm_S3, or create model/manuscript authority.

If not converged, any further resolution step must itself be prospectively frozen only after JL is terminal. The measured JK-to-JL reduction factor may be reported after the fact for interpretation but must not alter either gate.

No post-hoc grid-density change, tolerance change, estimator switch, averaging, clipping, extrapolation, dropped atoms/rows, effective-coordinate rescue, fiducial-P rescue or physical-domain modification is allowed.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; finite-difference `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`.
