# Exp073JN — Article 3 Layer-B shared-grid scientific closure rerun v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / Layer-B physical-support closure.

Status: CONDITIONALLY PROSPECTIVELY FROZEN WHILE EXP073JL IS STILL RUNNING AND BEFORE ANY EXP073JL NUMERICAL RESULT IS INSPECTED.

## Activation condition
Exp073JN is authorized to run only if Exp073JL terminates as a valid, independently verified `COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` result under its already-frozen contract. If Exp073JL is NOT_CONVERGED, Exp073JN MUST NOT run and the already-frozen Exp073JM branch governs the next sequential convergence step.

Infrastructure failure, malformed artifact, lineage failure, or any non-valid Exp073JL outcome does not activate Exp073JN.

## Purpose
Create a fresh science-authorizing Layer-B run after numerical convergence has been established independently by Exp073JL. Exp073JL itself is support-only `+0/+0` and cannot retroactively become scientific authority.

Exp073JN therefore prospectively repeats the exact converged 2048->4096 shared-grid comparison under a scientific decision contract rather than converting the support-only JL result into a scientific PASS post hoc.

## Frozen numerical architecture
Use exactly the Exp073JL lattices and no others:
- production/coarse: base N=2048 with the response-blind one-node upper guard, exactly 2049 requested nodes;
- dense/fine: base N=4096 with the response-blind one-node upper guard, exactly 4097 requested nodes;
- `KMIN=1e-4 Mpc^-1` and judged `KMAX=0.06664762008318016 Mpc^-1` unchanged;
- native CLASS `k_per_decade_for_pk=20` for both suites;
- centered-cubic Lagrange interpolation in `ln(k)` with stencil `{j-2,j-1,j,j+1}` unchanged;
- requested-node coordinate mismatch <=1e-12;
- finite-difference `h=1e-4` unchanged;
- numerical convergence threshold `REL_TOL=1e-3` unchanged.

Infrastructure-only capacity patches are exactly the JL envelope: `_MAX_NUMBER_OF_K_FILES_=4608`, `_ARGUMENT_LENGTH_MAX_=131072`, with exact one-replacement and pre/post SHA256 provenance. No scientific code path or threshold may change.

## Frozen physical support and lineage
Preserve the exact Exp073IR/Exp073IQ parent lineage and ordering:
- 107 retained coordinate rows total;
- 53 DES + 54 BOSS retained rows;
- DES reconstructed fine radial grid and exact inherited angular authorities;
- frozen BOSS z3 operators and exact existing physical-k geometry;
- pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c` and public gauge-invariant `d_m` exposure patch already audited;
- exact baseline/precision inputs and the four finite-difference models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

No covariance, whitening, nuisance, relation/null, likelihood or Wm_S3 scientific quantity may be read during Exp073JN.

## Frozen science decision
A valid complete Exp073JN is `PASS_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_V0_1` only if all are true:
1. exact independently verified Exp073JL CONVERGED authority activates the gate;
2. exact 107-row parent identity and full order are preserved;
3. requested counts are exactly 2049 and 4097 with guard counts `(0,1)` for each;
4. zero unsupported target evaluations in both suites;
5. requested-node coordinate mismatch <=1e-12;
6. no finite/nonzero-status change, row-label change or BOSS dense-z disagreement;
7. maximum atomic production-vs-dense relative component difference is strictly `< 1e-3`;
8. production-grid Layer-B invalid-row fraction is `<=0.05`;
9. retained dimension after Layer-B is `>=15`;
10. all forbidden downstream reads remain false.

If items 1-6 or lineage/build/parser/provenance conditions fail, classify `INVALID_INFRA_PLUS_0_PLUS_0` and do not infer science.

If the run is valid but item 7 fails, classify `NUMERICALLY_UNRESOLVED_EXP073JN` and do not authorize downstream covariance work.

If numerical convergence passes but physical-support row thresholds 8-9 fail, classify `FAIL_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_V0_1`.

## Downstream authorization boundary
Only `PASS_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_V0_1` may authorize the next separately frozen covariance-restriction/whitening stage to begin. Exp073JN does not itself perform or pass covariance restriction, whitening, nuisance-rank, quotient/relation/null, likelihood or Wm_S3 scientific arithmetic.

Wm_S3 remains governed by its separate resource/scientific authority chain and is not opened merely by Exp073JN.

## Anti-rescue rule
No post-hoc density change, tolerance change, denominator floor, rounding, smoothing, averaging, clipping, extrapolation, dropped atoms/rows, altered masks, effective-coordinate substitution or fiducial-P shortcut is allowed. A support-only JL result cannot be promoted directly; Exp073JN must execute prospectively under this frozen scientific contract.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`.
