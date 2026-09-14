# DSIR V0.22 preregistration — forced NumPy baseline cross-host reproducibility audit

Status: **PROSPECTIVELY FROZEN BEFORE V0.22 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only.

## Parent authority

Parent: `docs/dsir4/authority/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json` (`NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`). Parent-authorized successor exactly: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT`.

## HYPOTHESIS

The hosted cross-job numerical branch observed in V0.13–V0.17 is caused by NumPy AVX-512 runtime dispatch. Therefore forcing the exact V0.20-validated NumPy non-AVX512 runtime-dispatch baseline before importing NumPy/classy should collapse the two frozen replay-failure responses to a single cross-host branch below the technical reproducibility tolerance, even when the native host pool contains both AVX-512-active and AVX-512-inactive NumPy dispatch classes.

## DESIGN

Launch exactly 32 independent `ubuntu-24.04` hosted jobs with `max-parallel:32`.

Each lane has two phases:

1. **Response-free native/forced fingerprint preflight.** No CLASS import and no DSIR response computation. Record NumPy 1.26.4 `__cpu_baseline__`, `__cpu_dispatch__`, `__cpu_features__`, active dispatch = dispatch-members whose feature value is true, CPU model/capability fingerprint, software controls, and the exact V0.20 mask. Then start a fresh child interpreter with the frozen `NPY_DISABLE_CPU_FEATURES` mask and verify the forced active dispatch profile.
2. **Forced-baseline numerical solve.** Only if the preflight is valid, start a fresh masked child before NumPy/classy import and compute exactly the two frozen replay-failure cells plus one anchor. No unmasked substantive response is computed in V0.22.

The glibc hwcaps intervention is not used in V0.22 because V0.21 prospectively showed `glibc_switch_supported=false`; the minimal causal repair under test is NumPy dispatch only.

## FROZEN NUMPY PROFILE AND MASK

NumPy version `1.26.4`.

Build baseline: `SSE,SSE2,SSE3`.
Build dispatch set: `SSSE3,SSE41,POPCNT,SSE42,AVX,F16C,FMA3,AVX2,AVX512F,AVX512CD,AVX512_KNL,AVX512_KNM,AVX512_SKX,AVX512_CLX,AVX512_CNL,AVX512_ICL`.
Validated AVX-512 dispatch targets: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.
Exact environment mask: `NPY_DISABLE_CPU_FEATURES=AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.
Required forced active AVX-512 dispatch: empty.
Required forced active non-AVX512 dispatch exactly: `AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.

No requirement is imposed on raw non-dispatch AVX-512 capability bits in `__cpu_features__`. They are explicitly forbidden as intervention-success criteria.

## FROZEN NUMERICAL OBJECT

- CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- Production `h=1e-4`; diagnostic cells exactly:
  - replay failure: `h=2e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`;
  - replay failure: `h=1e-4`, `z=3fe3d70a3d70a3d7`, `k=3f8fc70971921840`;
  - anchor: `h=1e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`.
- GRID1024 = base 1024 + one upper guard = 1025 requested nodes.
- `tol_perturb_integration=1e-12`.
- production perturbation sampling `0.00035`.
- technical reproducibility tolerance `<1e-5` relative.
- exact requested-node binding `<=1e-12`.
- frozen alternate-branch references from V0.17:
  - `h=2e-4 -> -0.32763449098638375`;
  - `h=1e-4 -> 0.13550307244258875`.

## ELIGIBILITY / POWER

A lane is eligible only if:
- NumPy version, baseline and dispatch set equal the frozen V0.20 profile;
- the forced child has zero active AVX-512 dispatch;
- the forced child preserves exactly the frozen active non-AVX512 dispatch set;
- binary/software controls are valid and frozen numerical inputs are unchanged.

Native response is never computed. Native dispatch class is response-free metadata only:
- `NATIVE_AVX512_ACTIVE` if native active AVX-512 dispatch is non-empty;
- `NATIVE_AVX512_INACTIVE` if native active AVX-512 dispatch is empty.

Minimum total eligible lanes: 6.
Minimum eligible lanes per native dispatch class: 3.
Both native classes must be represented. This cross-class representation is mandatory for the principal reproducibility claim.

## POSITIVE CONTROLS

- invariant source/blob/profile audit passes;
- all 32 lane identities present exactly once;
- no substantive response before forced-profile validation;
- exact mask present before child Python startup/import;
- forced active AVX-512 dispatch empty;
- forced active non-AVX512 dispatch exactly frozen profile;
- one common CLASS/classy binary key across eligible lanes;
- all forced responses finite;
- exact binding `<=1e-12`;
- no production h/sampling/tolerance mutation;
- no forbidden downstream reads.

## FROZEN DECISION

Priority order: `INVALID -> INCONCLUSIVE -> UNDERPOWERED -> SUPPORTED -> REPRODUCIBLE_REFERENCE_MISMATCH -> NOT_SUPPORTED`.

`FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_INVALID` if any eligible candidate fails mask/profile validation, substantive response is computed before valid forced preflight, or eligible binaries/software controls are not common. No promotion.

`FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_INCONCLUSIVE` if source/input identity fails, any forced response is non-finite, exact binding exceeds `1e-12`, anchor cross-host relative spread is `>=1e-5`, or any forbidden downstream object is touched. No promotion.

`FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_UNDERPOWERED` if total eligible n<6, either native dispatch class has n<3, or both native classes are not represented. Next stage only expanded forced-baseline replication.

For the two replay-failure cells define the maximum pairwise relative spread across every eligible forced-baseline lane. Also compute maximum pairwise relative spread between the two native-class means. For alternate-branch agreement require every eligible forced response on each replay-failure cell to be within `<1e-5` relative of the frozen V0.17 alternate branch.

`FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED` iff:
- both replay-failure cross-host spreads are `<1e-5`;
- both native-class mean separations are `<1e-5`;
- anchor cross-host spread is `<1e-5`;
- every replay-failure forced response agrees with the frozen alternate branch within `<1e-5`;
- all controls pass.
Authorized next stage exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT`.

`FORCED_NUMPY_BASELINE_REPRODUCIBLE_BUT_BRANCH_REFERENCE_MISMATCH` iff all three cells have cross-host spread `<1e-5` and native-class means agree `<1e-5`, but at least one replay-failure cell does not agree with the frozen alternate branch `<1e-5`. Authorized next stage only a prospectively frozen forced-baseline branch-reference diagnosis.

`FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_NOT_SUPPORTED` otherwise (with valid controls and adequate power). Authorized next stage only a prospectively frozen residual-runtime-state audit under the forced NumPy baseline.

## INTERPRETATION CEILING

A supported V0.22 establishes that the validated NumPy non-AVX512 runtime baseline repairs the specific hosted cross-job numerical reproducibility defect on the frozen witness cells across heterogeneous native dispatch classes. It does not by itself validate production Layer-B, the full 107-row traversal, covariance, whitening, nuisance handling, relation-null, `Wm_S3`, global 65537, a dark-sector model, or a physical signal. Scientific effect remains `+0/+0` until a separately frozen production-h replay revalidation and later science gates pass.
