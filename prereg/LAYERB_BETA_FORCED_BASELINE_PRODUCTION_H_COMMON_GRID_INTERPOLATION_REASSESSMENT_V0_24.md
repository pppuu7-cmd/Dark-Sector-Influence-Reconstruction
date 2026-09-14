# DSIR V0.24 preregistration — forced-baseline production-h common-grid interpolation reassessment

Status: **PROSPECTIVELY FROZEN BEFORE V0.24 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only.

## Parent authority

Parent authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.json`, classification `FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_REVALIDATED`.

Parent-authorized successor exactly:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT`.

V0.23 established that the complete frozen V0.12 production-h pure-common-grid replay object (five grids × three frozen targets = 15 cells at `h=1e-4`) is cross-host reproducible under the exact V0.20-validated forced NumPy non-AVX512 runtime baseline. V0.24 may therefore reassess the V0.12 **production-h interpolation mechanism**, but may not import historical unforced branch values as PASS/FAIL references.

## Hypothesis

After forcing the exact validated NumPy non-AVX512 runtime-dispatch baseline, the two immutable V0.12 parent violations that occur at production `h=1e-4` remain common-grid discrepancies relative to a freshly generated controlled direct-TOL300 reference, and their mechanism is cubic interpolation rather than k-output node-set solver dependence.

## Frozen scientific cells

Only the two V0.12 parent-violation cells at production `h=1e-4` are gating:

1. `GRID768`, target T2: `kind=F,d=D,z=3fdab851eb851eb8,k=3f890e66b051e28b` (`z=0.4175`, `k=0.01223449922166366`). Historical V0.12 unforced pure-vs-direct discrepancy was `0.004037659729341879`, descriptive only.
2. `GRID896`, target T3: `kind=F,d=D,z=3fe3d70a3d70a3d7,k=3f8fc70971921840` (`z=0.62`, `k=0.015516351488496949`). Historical V0.12 unforced pure-vs-direct discrepancy was `0.0011351878950117023`, descriptive only.

The V0.12 `GRID640,h=2e-4,T1` parent violation is explicitly outside V0.24 and is not promoted, retuned or silently treated as production-h evidence.

## Frozen numerical state

- CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- Frozen response engine `ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py`.
- Production `h=1e-4` only.
- Native `k_per_decade_for_pk=20`.
- Production perturb sampling `0.00035`.
- `tol_perturb_integration=1e-12` for every substantive CLASS construction.
- Scientific mechanism threshold exactly `<1e-3` / `>=1e-3` as in V0.12.
- Technical cross-host/runtime reproducibility threshold `<1e-5`.
- Exact requested-node binding tolerance `<=1e-12`.

Exact validated NumPy mask:
`NPY_DISABLE_CPU_FEATURES=AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.

Required forced active AVX-512 dispatch: empty.
Required forced active non-AVX512 dispatch exactly:
`AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.
Raw non-dispatch AVX-512 capability bits are forbidden as intervention-success criteria.

## Frozen common/mixed construction semantics

V0.24 preserves the V0.12 construction relevant to the two production-h parent violations.

For each gating grid independently:
- `GRID768`: frozen guarded common grid from base 768, 769 requested nodes total.
- `GRID896`: frozen guarded common grid from base 896, 897 requested nodes total.

The mixed node set is **not** allowed to be reduced to only the local cell target. It is exactly the union of that grid's frozen common nodes with all three V0.12 audit-target k values:
- T1 `3f900ea7bc915d36`,
- T2 `3f890e66b051e28b`,
- T3 `3f8fc70971921840`.

For each grid at `h=1e-4`, construct pure-common `+h/-h` and mixed-node `+h/-h` models. For the gating target of that grid derive:
- `pure_interp_response`: cubic-centered interpolation from the pure common nodes;
- `mixed_interp_response`: cubic-centered interpolation using the common-node values returned by the mixed invocation;
- `mixed_exact_response`: exact target value returned by the same mixed invocation.

## Frozen fresh direct-TOL300 semantics

Historical direct artifact numeric values are non-gating because their hosted runtime-dispatch branch was not controlled. However the **direct computational object** is frozen from the V0.7/V0.9 lineage and must be reproduced exactly under the forced baseline.

Source semantics:
- V0.9 `TOL300R` delegated to `ci/layerb_beta_solver_conditioning_v0_7.py::domain_mode` with `tol_perturb_integration=1e-12`.
- Probe manifest: `docs/dsir4/contracts/LAYERB_TARGETED_DIRECT_K_BETA_PROBES_V0_4.json`.
- Use the full frozen **D-domain** probe set, deduplicated exactly as V0.7 by `(kind,z,k)`.
- The direct CLASS `k_output_values` node array is the sorted unique set of **all** D-domain probe k values, not a single local target k.
- Construct one direct `+h` and one direct `-h` model at production `h=1e-4`, using the same baseline/precision and `tol_perturb_integration=1e-12`.
- Extract the exact T2 and T3 values from those direct models using the frozen requested-node extraction and binding check.
- `direct_response=(plus-minus)/(2h)`.

Only freshly generated forced-baseline direct responses are allowed in V0.24 PASS/FAIL comparisons. Historical V0.9/V0.12 direct numeric values may be reported descriptively but are forbidden as classifier inputs.

## Hosted design / power

Launch exactly 32 independent `ubuntu-24.04` hosted lanes with `max-parallel:32`.

Every substantive lane MUST have an explicit workflow DAG dependency `needs: invariant-audit`; this is a mandatory hardening control carried from V0.23.

Each lane:
1. records a response-free native CPU/NumPy fingerprint;
2. starts a fresh interpreter with the exact NumPy mask and response-free validates the forced dispatch profile;
3. computes no substantive unmasked response;
4. only after valid forced preflight computes the frozen V0.24 object in a fresh masked child.

Expected substantive solver constructions per eligible lane: exactly 10:
- GRID768 pure +/- and mixed +/- = 4;
- GRID896 pure +/- and mixed +/- = 4;
- fresh historical-semantics D-domain direct +/- = 2.

Minimum eligible n = 6.
Minimum eligible native `NATIVE_AVX512_ACTIVE` n = 3.
Minimum eligible native `NATIVE_AVX512_INACTIVE` n = 3.
Both native classes must be represented.

Eligible lanes must share one CLASS/classy binary identity and one software-control identity.

## Technical reproducibility gate before mechanism classification

For each of the two parent cells, the four primitive response series
`pure_interp_response`, `mixed_interp_response`, `mixed_exact_response`, `direct_response`
must each satisfy across eligible lanes:
- maximum pairwise relative spread `<1e-5`;
- native-class mean relative separation `<1e-5`.

Thus eight primitive response series are technical gating objects. If any fails, V0.24 must not classify the interpolation mechanism.

All response values must be finite. Exact requested-node mismatch must remain `<=1e-12`. The exact two parent-cell identities, common-grid definitions, all-three-target mixed union, D-domain direct-node semantics, production h, TOL300 setting and frozen source/input identities must pass.

## Frozen per-cell V0.12 mechanism logic

For each eligible lane and each immutable parent cell compute:
- `pure_vs_direct_response_rel`;
- `mixed_interp_vs_exact_response_rel`;
- `mixed_exact_vs_direct_response_rel`;
- `pure_vs_mixed_interp_response_rel`.

Parent violation reproduced iff:
`pure_vs_direct_response_rel >= 1e-3`.

Cubic interpolation mechanism supported iff all are true:
- `mixed_interp_vs_exact_response_rel >= 1e-3`;
- `mixed_exact_vs_direct_response_rel < 1e-3`;
- `pure_vs_mixed_interp_response_rel < 1e-3`.

k-output node-set solver dependence supported iff either is true:
- `mixed_exact_vs_direct_response_rel >= 1e-3`; or
- `pure_vs_mixed_interp_response_rel >= 1e-3`.

After primitive-series technical reproducibility passes, a scientific-mechanism predicate counts as supported for a parent cell only if it is true in **every eligible lane**. This unanimity rule prevents a cross-host mean from masking threshold straddling. Lane-mean metrics may be reported descriptively but are not a substitute for unanimity.

## Frozen decision hierarchy

Priority:
`INVALID -> INCONCLUSIVE -> UNDERPOWERED -> REPRODUCIBILITY_BLOCKED -> mechanism classification`.

`FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_INVALID` if any candidate fails forced preflight, a substantive response occurs before valid preflight, immutable object/solver identities are wrong, all-three-target mixed union or historical-semantics D-domain direct node construction is wrong, or eligible binary/software controls are not common.

`FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_INCONCLUSIVE` if any value is nonfinite, exact binding exceeds `1e-12`, immutable source/input identity fails, or any forbidden object is touched.

`FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_UNDERPOWERED` if total eligible n<6, either native class n<3, or both classes are not represented.

`FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_REPRODUCIBILITY_BLOCKED` if powered/valid/invariant but any of the eight primitive response series has cross-host spread `>=1e-5` or native-class mean separation `>=1e-5`. Authorized next stage only:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_INTERPOLATION_OBJECT_REPRODUCIBILITY_DIAGNOSTIC`.

If primitive responses are reproducible:

`FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_CUBIC_INTERPOLATION_SUPPORTED` iff both immutable parent violations reproduce in every eligible lane, both cells support the cubic interpolation mechanism in every eligible lane, and neither supports node-set dependence. Authorized next stage only:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK`.

`FORCED_BASELINE_PRODUCTION_H_K_OUTPUT_NODE_SET_SOLVER_DEPENDENCE_SUPPORTED` iff both parent violations reproduce in every eligible lane, both cells support node-set dependence in every eligible lane, and neither supports interpolation-only. Authorized next stage only:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_K_OUTPUT_NODE_SET_SENSITIVITY_AUDIT`.

`FORCED_BASELINE_PRODUCTION_H_MIXED_INTERPOLATION_AND_NODE_SET_DEPENDENCE_SUPPORTED` iff both parent violations reproduce in every eligible lane, each cell is unanimously accounted for by interpolation or node-set dependence, and at least one cell supports each mechanism. Authorized next stage only:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_MIXED_NUMERICAL_MECHANISM_AUDIT`.

`FORCED_BASELINE_PRODUCTION_H_PARENT_VIOLATIONS_NOT_REPRODUCED` iff one or both immutable parent violations fail the frozen `>=1e-3` pure-vs-fresh-direct criterion in at least one eligible lane. Authorized next stage only:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_DISCREPANCY_REBASELINE_AUDIT`.

Otherwise classify:
`FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_PATTERN_UNRESOLVED`, authorizing only
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_TARGET_STENCIL_GEOMETRY_AUDIT`.

Invalid/inconclusive authorize diagnosis only. Underpowered authorizes expanded replication only.

## Interpretation ceiling / firewall

V0.24 is a numerical-mechanism reassessment only. Even a supported cubic-interpolation classification does not validate full Layer-B, does not authorize the full 107-row traversal, does not authorize global 65537, and does not open covariance, whitening, nuisance, relation-null or `Wm_S3`. It is not dark-sector evidence. Effect remains `+0/+0`.

Forbidden after results: retune parent cells, target set, direct node semantics, mixed-node union, thresholds, power, production h, sampling, tolerance, mask, or decision branches.
