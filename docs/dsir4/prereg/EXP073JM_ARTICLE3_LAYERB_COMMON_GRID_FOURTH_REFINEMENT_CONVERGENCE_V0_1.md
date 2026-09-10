# Exp073JM — Article 3 Layer-B common-grid fourth-refinement convergence v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 numerical support only.

Status: CONDITIONALLY PROSPECTIVELY FROZEN WHILE EXP073JL IS STILL RUNNING AND BEFORE ANY EXP073JL NUMERICAL RESULT IS INSPECTED.

## Activation condition
Exp073JM is authorized to run only if Exp073JL terminates as a valid, independently verified `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` result under its already-frozen contract. If Exp073JL converges, Exp073JM MUST NOT run; the next allowed step is a separately prospectively frozen scientific Layer-B rerun using the admitted converged shared-grid architecture.

Infrastructure failure, malformed artifact, lineage failure, or any non-valid Exp073JL outcome does not activate Exp073JM.

## Purpose
Measure the immediately next sequential shared-grid resolution step without changing the estimator, interpolation rule, physical support, finite-difference step or acceptance threshold. The purpose is convergence certification, not scientific rescue.

## Frozen lattices
Judged physical support remains unchanged.

Coarse architecture:
- base `C4096 = np.geomspace(1e-4,0.06664762008318016,4096,dtype=float64)`;
- response-blind centered-cubic guard derivation inherited from Exp073JI/JJ/JK/JL;
- prospectively required lower guard count 0 and upper guard count 1;
- requested-node count exactly 4097.

Fine architecture:
- base `F8192 = np.geomspace(1e-4,0.06664762008318016,8192,dtype=float64)`;
- same response-blind guard derivation;
- prospectively required lower guard count 0 and upper guard count 1;
- requested-node count exactly 8193.

Base nodes must remain bitwise unchanged inside each guarded lattice. Both lattices must prove complete centered-cubic stencil coverage before response evaluation.

## Frozen physical/numerical evaluation
Preserve the exact Exp073IR parent lineage, all 53 DES + 54 BOSS retained-coordinate support, atom traversal/accounting, pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, public gauge-invariant `d_m`, exact baseline/precision inputs, and the four finite-difference models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)` with `h=1e-4`.

CLASS native `k_per_decade_for_pk` remains exactly 20 for both suites. Inherited Exp073IR suite slot `10` maps only to guarded N=4096 and slot `20` maps only to guarded N=8192; these slot labels are not native-kpd values.

For every suite/model/redshift:
1. inject the full guarded common physical-k lattice via `k_output_values`;
2. recover requested nodes from public transfer output with relative coordinate mismatch <=1e-12;
3. interpolate only between requested common nodes using the unchanged centered-cubic Lagrange rule in `x=ln(k)` with stencil `{j-2,j-1,j,j+1}`;
4. compute unchanged alpha-left and beta-symmetric finite-difference responses;
5. reuse exact Exp073IR atomic comparison, finite/nonzero, row-label, BOSS dense-z and Layer-B accounting logic.

## Infrastructure-only capacity
Because 8193 serialized requested nodes exceed the Exp073JL parser/capacity envelope, Exp073JM may enlarge only:
- `_MAX_NUMBER_OF_K_FILES_` from 30 to exactly 9216;
- `_ARGUMENT_LENGTH_MAX_` from 1024 to exactly 262144.

Exact one-replacement checks and pre/post SHA256 provenance are mandatory. These are infrastructure-only modifications. No equations, transfer definitions, masks, physical domain, arithmetic, interpolation or thresholds may change.

## Diagnostic metadata
The already-frozen `docs/dsir4/methods/LAYERB_CONVERGENCE_ARGMAX_DIAGNOSTIC_STANDARD_V0_1.md` may be implemented in Exp073JM. It may record the unchanged relative-error argmax location, response component, z/k, coarse/fine values, absolute difference and denominator, plus response-scale summaries. Diagnostic metadata MUST NOT change atom inclusion, the scalar maximum, classification, tolerance or any downstream authorization.

## Frozen decision
A valid complete Exp073JM run is `COMMON_GRID_FOURTH_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` only if all are true:
- exact independently verified Exp073JL NOT_CONVERGED authority activates the gate;
- exact Exp073JI geometry/parent lineage remains bound;
- requested counts are exactly 4097 and 8193 with guard counts `(0,1)` for each;
- zero unsupported target evaluations in both suite slots;
- no finite/nonzero-status change, row-label change or BOSS dense-z disagreement;
- maximum atomic coarse-vs-fine relative component difference is strictly `< REL_TOL=1e-3`;
- inherited Layer-B invalid-row fraction under coarse accounting is <=0.05 and retained dimension >=15;
- requested-node coordinate mismatch is <=1e-12.

Otherwise a valid numerical run is `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Lineage/hash/build/parser/capacity/grid/stencil/provenance failures are `INVALID_INFRA_PLUS_0_PLUS_0`.

## Interpretation boundary
Exp073JM is support-only `+0/+0` in every valid outcome. A converged result may authorize only a separately prospectively frozen scientific Layer-B numerical rerun. A non-converged result authorizes neither covariance restriction nor Wm_S3 and requires a separately prospectively frozen next step. No post-hoc density choice, tolerance change, estimator switch, denominator floor, averaging, clipping, extrapolation, atom/row dropping or physical-domain modification is allowed.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
