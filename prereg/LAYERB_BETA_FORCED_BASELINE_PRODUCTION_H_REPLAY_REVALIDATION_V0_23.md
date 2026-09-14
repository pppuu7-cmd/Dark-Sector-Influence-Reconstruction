# DSIR V0.23 preregistration — forced-baseline production-h replay revalidation

Status: **PROSPECTIVELY FROZEN BEFORE V0.23 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only.

## Parent authority

Parent: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, classification `FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED`. Parent-authorized successor exactly: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT`.

## HYPOTHESIS

The V0.12 production-h pure-common-grid replay invariant failed because hosted jobs could execute different NumPy AVX-512 runtime-dispatch branches. After forcing the exact V0.20-validated NumPy non-AVX512 runtime baseline before NumPy/classy import, the complete frozen V0.12 production-h replay set should become reproducible across hosted jobs and across both native dispatch classes at the frozen technical threshold `<1e-5`.

## FROZEN REPLAY OBJECT

This audit revalidates the complete V0.12 **production-h** pure-grid replay subset, not a selected witness subset and not the full Layer-B traversal.

Production `h=1e-4` only.

Frozen grids from V0.12:
- `GRID512`: base 512 + one upper guard = 513 requested nodes;
- `GRID640`: base 640 + one upper guard = 641 requested nodes;
- `GRID768`: base 768 + one upper guard = 769 requested nodes;
- `GRID896`: base 896 + one upper guard = 897 requested nodes;
- `GRID1024`: base 1024 + one upper guard = 1025 requested nodes.

Frozen V0.12 targets on every grid:
1. `kind=F,d=D,z=3fe43d70a3d70a3e,k=3f900ea7bc915d36`;
2. `kind=F,d=D,z=3fdab851eb851eb8,k=3f890e66b051e28b`;
3. `kind=F,d=D,z=3fe3d70a3d70a3d7,k=3f8fc70971921840`.

Therefore the principal replay object contains exactly `5 × 3 = 15` cells.

The two frozen V0.13 production-h cells that previously violated replay are:
- `GRID768`, target 3, historical max same-profile spread `2.4934371090895516e-5`;
- `GRID1024`, target 3, historical max same-profile spread `1.0478978062540487e-5`.

Frozen anchors include `GRID768` and `GRID1024` at target 2. No post-result cell selection is allowed.

## FROZEN NUMERICAL / RUNTIME STATE

- CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- Frozen response engine `ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py`.
- Production `h=1e-4`.
- Native `k_per_decade_for_pk=20`.
- Production perturbation sampling `0.00035`.
- `tol_perturb_integration=1e-12`.
- Technical replay tolerance `<1e-5` relative.
- Exact requested-node coordinate mismatch `<=1e-12`.
- Scientific response threshold remains `<1e-3` but is not a promotion criterion in V0.23.

Exact NumPy version `1.26.4` and V0.20-validated mask:
`NPY_DISABLE_CPU_FEATURES=AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.

Required forced active AVX-512 dispatch: empty.
Required forced active non-AVX512 dispatch exactly:
`AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.

Raw non-dispatch AVX-512 capability bits are explicitly forbidden as intervention-success criteria.

## DESIGN

Launch exactly 32 independent `ubuntu-24.04` hosted lanes with `max-parallel:32`.

Each lane:
1. records a response-free native NumPy/CPU fingerprint;
2. launches a fresh interpreter with the exact frozen NumPy mask and validates the forced active-dispatch profile response-free;
3. only if the forced profile is valid, launches a fresh masked numerical child and computes the exact 15-cell production-h replay object;
4. computes no unmasked substantive response.

The numerical child constructs only pure common-grid `+h/-h` CLASS solves. It does not add exact target nodes, does not run mixed-grid interpolation diagnostics, and does not read any downstream science object. For each grid only two CLASS solver constructions are allowed (`+1e-4`, `-1e-4`), for exactly 10 solver constructions per eligible lane.

## POWER / HOST-CLASS REPRESENTATION

Native dispatch class is response-free metadata only:
- `NATIVE_AVX512_ACTIVE` if native active AVX-512 NumPy dispatch is non-empty;
- `NATIVE_AVX512_INACTIVE` if native active AVX-512 NumPy dispatch is empty.

Minimum total eligible lanes: 6.
Minimum eligible lanes per native class: 3.
Both native classes must be represented.

## POSITIVE CONTROLS

- invariant source/blob/profile audit passes;
- all 32 lane identities present exactly once;
- no substantive response before valid forced preflight;
- exact mask is present before masked child Python startup/import;
- forced active AVX-512 dispatch is empty;
- forced active non-AVX512 dispatch equals the frozen profile;
- exactly one CLASS/classy binary identity and one software-control identity across eligible lanes;
- exactly 15 finite response cells per eligible lane, with exact frozen grid/target identities;
- exactly 10 solver constructions per eligible lane;
- exact requested-node binding `<=1e-12`;
- production h, sampling, tolerance and grid definitions unchanged;
- no covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 or science gate access.

Historical V0.10/V0.11/V0.12 response values were generated before the runtime mechanism was controlled and may belong to different runtime-dispatch branches. Their numeric branch identity may be reported descriptively but **must not be used as a V0.23 PASS/FAIL criterion**. V0.23 tests reproducibility of the forced baseline itself.

## FROZEN DECISION

Priority: `INVALID -> INCONCLUSIVE -> UNDERPOWERED -> SUPPORTED -> ORIGINAL_FAILURES_REPAIRED_BUT_GLOBAL_REPLAY_FAILS -> NOT_SUPPORTED`.

`FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_INVALID` if any candidate lane fails the forced dispatch preflight, a substantive response is computed before a valid preflight, cell/solver identities are wrong, or eligible binary/software controls are not common.

`FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_INCONCLUSIVE` if any response is non-finite, exact binding exceeds `1e-12`, an immutable source/input identity fails, or a forbidden downstream object is touched.

`FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_UNDERPOWERED` if total eligible n<6, either native class has n<3, or both classes are not represented.

For every one of the 15 cells compute:
- maximum pairwise relative spread across all eligible forced-baseline lanes;
- relative separation of the two native-class means.

`FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_REVALIDATED` iff all 15 cells have cross-host maximum pairwise relative spread `<1e-5` **and** all 15 native-class mean separations are `<1e-5`, with all controls passing. Authorized next stage exactly:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT`.

`FORCED_BASELINE_ORIGINAL_PRODUCTION_H_FAILURES_REPAIRED_BUT_GLOBAL_REPLAY_NOT_REVALIDATED` iff both originally failing production-h cells (`GRID768/target3`, `GRID1024/target3`) satisfy both `<1e-5` criteria but one or more of the other 13 cells fails. Authorized next stage only:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_RESIDUAL_REPLAY_STATE_AUDIT`.

`FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_NOT_REVALIDATED` otherwise, with valid controls and adequate power. Authorized next stage only:
`PROSPECTIVELY_FROZEN_RESIDUAL_RUNTIME_STATE_AUDIT_UNDER_FORCED_NUMPY_BASELINE`.

Underpowered authorizes only expanded forced-baseline production-h replay replication. Invalid/inconclusive authorizes only diagnosis of the corresponding frozen control/invariant failure.

## INTERPRETATION CEILING

A supported V0.23 closes the original **production-h hosted replay reproducibility blocker** for the exact V0.12 15-cell replay object under the validated forced NumPy baseline. It does not yet re-establish the V0.12 interpolation-mechanism conclusion, validate the full 30-cell two-h object, validate full Layer-B, open covariance/whitening/nuisance/relation-null or `Wm_S3`, authorize global 65537, or establish any dark-sector/physical result. Effect remains `+0/+0`.
