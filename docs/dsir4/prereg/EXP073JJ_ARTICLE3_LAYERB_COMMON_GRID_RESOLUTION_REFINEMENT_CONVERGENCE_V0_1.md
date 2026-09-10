# Exp073JJ — Article 3 Layer-B common-grid resolution-refinement convergence v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 support only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JI AND BEFORE ANY EXP073JJ RESPONSE OUTPUT.

## Bound authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; covariance restriction and Wm_S3 remain unauthorized.

Validated Exp073JI run/job `34488466425 / 102908710275`, artifact `10156878354`, independently verified ZIP SHA256 `f8492ca04ff3b159ffe28003d28c3756e428e9851f4a3af56e6f343666d1b0de`, is support-only `GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0`.

JI response-blind geometry authority fixes the inherited full-support target range to `[0.00033800000000000003, 0.06664596609379447] Mpc^-1`, geometry stream SHA256 `79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a`. The N=512 JG/JH base lattice requires exactly one same-ratio upper guard and no lower guards, giving 513 requested common nodes. On this guarded lattice all inherited targets are supported, all 107 rows remain valid, and kpd10-vs20 response discrepancy is exactly zero.

## Why a new convergence axis is required
Once every model is evaluated on the same explicitly requested physical-k lattice, changing the otherwise-native `k_per_decade_for_pk` setting is no longer a strong measure of interpolation accuracy: Exp073JD/JI show requested-node responses can remain exactly invariant under that change. Therefore JI feasibility is not sufficient evidence of absolute full-support interpolation accuracy.

Exp073JJ prospectively changes the **shared requested-grid resolution itself** while preserving the physical observable, interpolation rule, judged support and all thresholds. This supplies an independent full-support numerical-convergence axis.

## Frozen coarse and fine evaluation lattices
Judged physical support remains exactly unchanged.

Coarse architecture:
- base `C512 = np.geomspace(1e-4,0.06664762008318016,512,dtype=float64)`;
- ratio `r512 = C512[1]/C512[0]` binary64;
- response-blind JI geometry implies `n_lo=0`, `n_hi=1`;
- append exactly `C512[-1]*r512`, producing 513 requested nodes.

Fine architecture:
- base `F1024 = np.geomspace(1e-4,0.06664762008318016,1024,dtype=float64)`;
- ratio `r1024 = F1024[1]/F1024[0]` binary64;
- use the exact same JI target extrema and the same minimal centered-cubic stencil rule;
- prospectively derived guard counts are `n_lo=0`, `n_hi=1`;
- append exactly `F1024[-1]*r1024`, producing 1025 requested nodes.

Both lattices must independently prove complete centered-cubic stencil coverage of the frozen JI target extrema before response evaluation. No response-dependent grid adjustment is allowed.

## Frozen physical/numerical evaluation
Use the exact original Exp073IR parent lineage, full 53 DES + 54 BOSS retained-coordinate support and unchanged atom traversal/accounting.

Use pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant `d_m`, exact baseline/precision inputs, and the same four finite-difference models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)` with frozen `h=1e-4`.

To isolate shared-grid interpolation resolution, CLASS native `k_per_decade_for_pk` is frozen to `20` for **both** coarse and fine suites. The inherited Exp073IR production/dense suite slots are used only as deterministic traversal/comparison slots: slot `10` selects the coarse 513-node lattice and slot `20` selects the fine 1025-node lattice. The wrapper result MUST explicitly record this remapping and MUST NOT interpret the inner labels as a native-kpd test.

For each suite and every model/redshift:
1. inject its full guarded common lattice through `k_output_values`;
2. recover every requested node from public transfer output with relative coordinate mismatch `<=1e-12`;
3. interpolate only between requested common nodes;
4. use the exact frozen JH/JI centered-cubic Lagrange rule in `x=ln(k)` and stencil `{j-2,j-1,j,j+1}`;
5. compute the exact inherited alpha-left one-sided and beta-symmetric finite-difference responses and absolute component magnitudes;
6. reuse the exact Exp073IR atomic comparison, finite/nonzero, row-label, BOSS dense-z and Layer-B accounting logic.

Infrastructure-only capacity patch may set `_MAX_NUMBER_OF_K_FILES_` from 30 to `1152`; parser capacity remains prospectively fixed at 32768. Exact one-replacement and pre/post SHA256 provenance is mandatory. The actual requested counts are 513 and 1025 and must be recorded. No equations, transfer definitions, masks, physical domain, finite-difference operator or threshold may change.

## Frozen convergence decision
A valid complete Exp073JJ run is `COMMON_GRID_RESOLUTION_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` only if all are true:
- exact JI parent identity and geometry authority are enforced;
- coarse and fine base/guard construction matches the frozen definitions and both support every inherited target;
- zero unsupported target evaluations in both suite slots;
- no finite/nonzero-status change, row-label change or BOSS dense-z disagreement between coarse and fine;
- maximum **atomic coarse-vs-fine relative component difference** is `< REL_TOL=1e-3`;
- inherited Layer-B invalid-row fraction under the coarse accounting remains `<=0.05` and retained dimension `>=15`;
- requested-node coordinate mismatch remains `<=1e-12`.

Otherwise a valid numerical run is `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Lineage/hash/build/parser/capacity/grid/stencil/provenance failures are `INVALID_INFRA_PLUS_0_PLUS_0`.

## Interpretation boundary
Exp073JJ is support-only `+0/+0` in every outcome. A convergence PASS, combined with JG exact-k anchors and JI full-support coverage, may authorize only the design of a separate prospectively frozen scientific Layer-B numerical rerun using a predeclared guarded shared-grid architecture. JJ itself does not retroactively PASS Exp073IR, authorize covariance restriction, open Wm_S3, or create model/manuscript authority.

No post-hoc grid density change, tolerance change, estimator switch, averaging, clipping, extrapolation, dropped atoms/rows or physical-domain modification is allowed.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; finite-difference `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
