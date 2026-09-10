# Exp073JK — Article 3 Layer-B common-grid second-refinement convergence v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 support only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JJ AND BEFORE ANY EXP073JK RESPONSE OUTPUT.

## Bound authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; covariance restriction and Wm_S3 remain unauthorized.

Validated Exp073JJ run/job `34492300395 / 102921844345`, artifact `10158706262`, independently verified ZIP SHA256 `079c08b7b8d62a775f5111b5696c41dd60babb2449b9f129d2518d1324908d14`, is support-only `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Its base N=512 versus N=1024 guarded-grid comparison retained all 107 rows with zero unsupported targets but had maximum atomic relative component difference `0.037280144773915974 > 1e-3`.

The validated JI geometry authority remains fixed: target range `[0.00033800000000000003, 0.06664596609379447] Mpc^-1`, geometry stream SHA256 `79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a`, and response-blind minimal centered-cubic support requires one upper same-ratio guard and no lower guard for the grids used here.

## Purpose
Measure the next independent shared-grid resolution step without changing the estimator or acceptance threshold. Exp073JK compares the previously tested fine architecture (base N=1024 + one upper guard = 1025 requested nodes) against a newly refined architecture (base N=2048 + one upper guard = 2049 requested nodes).

This gate is intentionally sequential rather than jumping directly to a presumed passing resolution: the observed convergence rate itself is evidence needed to choose any later production architecture without post-hoc tuning.

## Frozen lattices
Judged physical support remains unchanged.

Coarse architecture:
- base `C1024 = np.geomspace(1e-4,0.06664762008318016,1024,dtype=float64)`;
- same-ratio upper guard count exactly 1; lower guard count 0;
- requested-node count exactly 1025.

Fine architecture:
- base `F2048 = np.geomspace(1e-4,0.06664762008318016,2048,dtype=float64)`;
- same response-blind minimal centered-cubic guard derivation against the frozen JI target extrema;
- prospectively required lower guard count 0 and upper guard count 1;
- requested-node count exactly 2049.

Both lattices must independently prove complete centered-cubic stencil coverage before response evaluation. Base nodes must remain bitwise unchanged inside each guarded lattice.

## Frozen physical/numerical evaluation
Use the exact original Exp073IR parent lineage, 53 DES + 54 BOSS retained-coordinate support and unchanged atom traversal/accounting.

Use pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant `d_m`, exact baseline/precision inputs, and the same four finite-difference models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)` with frozen `h=1e-4`.

CLASS native `k_per_decade_for_pk` remains frozen to `20` for both suites. Inherited Exp073IR suite slot `10` maps deterministically to guarded N=1024 and slot `20` maps to guarded N=2048; these slot labels MUST NOT be interpreted as native-kpd values.

For each suite/model/redshift:
1. inject the full guarded common physical-k lattice with `k_output_values`;
2. recover every requested node from public transfer output with relative coordinate mismatch `<=1e-12`;
3. interpolate only between requested common nodes using the unchanged centered-cubic Lagrange rule in `x=ln(k)` and stencil `{j-2,j-1,j,j+1}`;
4. compute the inherited alpha-left one-sided and beta-symmetric finite-difference responses with frozen `h=1e-4`;
5. reuse the exact Exp073IR atomic comparison, finite/nonzero, row-label, BOSS dense-z and Layer-B accounting logic.

Infrastructure-only capacity patches may enlarge `_MAX_NUMBER_OF_K_FILES_` from 30 to `2304` and `_ARGUMENT_LENGTH_MAX_` from 1024 to `65536`. Exact one-replacement and pre/post SHA256 provenance are mandatory. No equations, transfer definitions, masks, physical domain, finite-difference arithmetic, interpolation rule or thresholds may change.

## Frozen decision
A valid complete Exp073JK run is `COMMON_GRID_SECOND_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` only if all are true:
- exact JJ/JI parent authority and geometry identity are enforced;
- requested counts are exactly 1025 and 2049 with guard counts `(0,1)` for each;
- zero unsupported target evaluations in both suite slots;
- no finite/nonzero-status change, row-label change or BOSS dense-z disagreement;
- maximum atomic coarse-vs-fine relative component difference is `< REL_TOL=1e-3`;
- inherited Layer-B invalid-row fraction under coarse accounting is `<=0.05` and retained dimension `>=15`;
- requested-node coordinate mismatch is `<=1e-12`.

Otherwise a valid numerical run is `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Lineage/hash/build/parser/capacity/grid/stencil/provenance failures are `INVALID_INFRA_PLUS_0_PLUS_0`.

## Interpretation boundary
Exp073JK is support-only `+0/+0` in every valid outcome. If converged, it may authorize only a separately prospectively frozen scientific Layer-B numerical rerun using a predeclared shared-grid architecture. If not converged, the next resolution step must itself be prospectively frozen; the acceptance tolerance may not be weakened.

For interpretation only after a valid result, the ratio of the JJ maximum (`512->1024`) to the JK maximum (`1024->2048`) may be reported as an empirical refinement reduction factor. It MUST NOT be used to retroactively alter either gate.

No post-hoc grid-density change, tolerance change, estimator switch, averaging, clipping, extrapolation, dropped atoms/rows or physical-domain modification is allowed.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; finite-difference `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
