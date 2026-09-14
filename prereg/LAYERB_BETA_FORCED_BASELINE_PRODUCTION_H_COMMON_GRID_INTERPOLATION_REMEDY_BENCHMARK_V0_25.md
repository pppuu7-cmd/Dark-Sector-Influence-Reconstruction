# DSIR V0.25 preregistration — forced-baseline production-h common-grid interpolation remedy benchmark

Status: **PROSPECTIVELY FROZEN BEFORE V0.25 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR numerical remedy benchmark only.

## Parent authority

Parent authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_V0_24.json` at commit `bcefebb72cfe9518a3b02dd746664aa9ec105b03`, blob `96aec62dc891e1be9851b45baecafee284ac2f8e`.

Required parent classification exactly:
`FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_CUBIC_INTERPOLATION_SUPPORTED`.

Required parent-authorized successor exactly:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK`.

V0.24 established, under the exact validated forced NumPy non-AVX512 dispatch baseline, that both immutable production-h parent violations are caused by common-grid cubic interpolation and not by k-output node-set solver dependence. V0.25 therefore benchmarks remedies; it does not reopen the mechanism classification.

## Frozen objective

Choose a numerically controlled production-h remedy for the two V0.24 parent violations while protecting nearby frozen V0.12 audit targets against remedy-induced regression.

The benchmark compares exactly two remedies against the original cubic-common-grid control and a freshly generated forced-baseline direct-TOL300 reference:

1. `EXACT_TARGET_UNION`: preserve each original guarded common grid, union it with **all three** frozen V0.12 audit-target k values, solve CLASS on that mixed set, and read the target itself exactly from the returned transfer table. No interpolation is used for the remedy value.
2. `ONE_STEP_GRID_REFINEMENT`: preserve cubic-centered interpolation but replace the gating grid by the next already-frozen V0.12 guarded grid: `GRID768 -> GRID896` and `GRID896 -> GRID1024`.

No third remedy may be added after results. Linear interpolation, PCHIP, spline retuning, target-local stencil changes, different h, different tolerance, different native k density, or a newly invented grid size are outside V0.25.

## Frozen benchmark panel

Production `h=1e-4` only.

Benchmark grids: original `GRID768` and original `GRID896`.

For **each** benchmark grid evaluate all three immutable V0.12 audit targets:

- T1: `kind=F,d=D,z=3fe43d70a3d70a3e,k=3f900ea7bc915d36` (`z=0.6325000000000001`, `k=0.015680905231730345`)
- T2: `kind=F,d=D,z=3fdab851eb851eb8,k=3f890e66b051e28b` (`z=0.4175`, `k=0.01223449922166366`)
- T3: `kind=F,d=D,z=3fe3d70a3d70a3d7,k=3f8fc70971921840` (`z=0.62`, `k=0.015516351488496949`)

Thus the immutable remedy-safety panel contains exactly six cells.

Two cells are scientific gating parent violations and MUST reproduce under the original control before remedy promotion:

- original `GRID768`, T2;
- original `GRID896`, T3.

The other four cells are frozen regression guards. They may not be discarded or relabeled after results.

## Frozen numerical state

- CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- Frozen response engine source `ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py`.
- Production `h=1e-4` only.
- Native `k_per_decade_for_pk=20`.
- Production perturb sampling `0.00035`.
- `tol_perturb_integration=1e-12` for every substantive CLASS construction.
- Scientific response threshold: `<1e-3` passes, `>=1e-3` fails.
- Technical cross-host/runtime reproducibility threshold: `<1e-5`.
- Exact requested-node binding tolerance: `<=1e-12`.

Exact validated forced NumPy mask:
`NPY_DISABLE_CPU_FEATURES=AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.

Required forced active AVX-512 dispatch: empty.
Required forced active non-AVX512 dispatch exactly:
`AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.

## Frozen node constructions

Original control grids use the inherited guarded-lattice construction:

- `GRID768`: base 768, lower guard 0, upper guard 1, total requested nodes 769.
- `GRID896`: base 896, lower guard 0, upper guard 1, total requested nodes 897.
- `GRID1024`: base 1024, lower guard 0, upper guard 1, total requested nodes 1025.

`EXACT_TARGET_UNION` for each original grid is the sorted exact union of that grid's common nodes with all three frozen target k values. The union is never target-local. Target extraction must bind to the explicitly requested target node within `1e-12` and must not call cubic interpolation for the remedy value.

`ONE_STEP_GRID_REFINEMENT` is exactly:

- for original `GRID768`, cubic-centered interpolation on inherited `GRID896` common nodes;
- for original `GRID896`, cubic-centered interpolation on inherited `GRID1024` common nodes.

The exact-target mixed invocation may additionally be cubic-interpolated over its **common-node subset** for a safety diagnostic. For every panel cell this mixed-common interpolation must remain within `<1e-3` of the original pure-common interpolation; otherwise the exact-target node union is treated as having a solver-node-set side effect and is not promotable.

## Frozen fresh direct reference

Use exactly the V0.24 forced-baseline direct-TOL300 semantics:

- manifest `docs/dsir4/contracts/LAYERB_TARGETED_DIRECT_K_BETA_PROBES_V0_4.json`;
- full frozen D-domain probe set;
- deduplicate by `(kind,z,k)` exactly as the V0.7/V0.9 lineage;
- direct `k_output_values` is the sorted unique set of all D-domain probe k values;
- one `+h` and one `-h` direct model at `h=1e-4`;
- `tol_perturb_integration=1e-12`;
- exact requested-node extraction for T1, T2 and T3.

Historical direct numeric values remain non-gating.

## Solver accounting

Each eligible substantive lane constructs exactly 12 CLASS models:

- original common `GRID768` +/-: 2;
- original common `GRID896` +/-: 2;
- refined common `GRID1024` +/-: 2;
- exact-target-union `GRID768` +/-: 2;
- exact-target-union `GRID896` +/-: 2;
- fresh direct D-domain +/-: 2.

The `GRID896` pure-common pair is shared: it is the original control for GRID896 and the one-step refinement model for GRID768. Recomputing an additional duplicate GRID896 pair is forbidden.

## Hosted design and power

Launch exactly 32 independent `ubuntu-24.04` hosted lanes with `max-parallel:32`.

Every substantive lane MUST depend explicitly on `invariant-audit`.

Each lane records a response-free native fingerprint, starts a fresh interpreter under the exact NumPy mask, validates the forced profile before any CLASS solve, and performs no substantive unmasked response.

Minimum eligible n = 6.
Minimum eligible `NATIVE_AVX512_ACTIVE` n = 3.
Minimum eligible `NATIVE_AVX512_INACTIVE` n = 3.
Both classes are required.

Eligible lanes must share one CLASS/classy binary identity and one software-control identity.

## Frozen per-cell outputs

For each of six panel cells compute:

- `control_response`: cubic interpolation on the original pure common grid;
- `mixed_common_interp_response`: cubic interpolation over the original-common-node subset returned by the exact-target-union invocation;
- `exact_target_union_response`: exact target value from the exact-target-union invocation;
- `one_step_refinement_response`: cubic interpolation on the next frozen grid;
- `direct_response`: fresh direct-TOL300 exact-node response.

And relative differences:

- `control_vs_direct_rel`;
- `mixed_common_vs_control_rel`;
- `exact_target_union_vs_direct_rel`;
- `one_step_refinement_vs_direct_rel`.

All values must be finite.

## Technical reproducibility gate

Before remedy classification, for each of the six panel cells the four scientific primitive response series
`control_response`, `exact_target_union_response`, `one_step_refinement_response`, `direct_response`
must each satisfy across eligible lanes:

- maximum pairwise relative spread `<1e-5`;
- native-class mean relative separation `<1e-5`.

Thus exactly 24 primitive series are technical gating objects. `mixed_common_interp_response` is an invariant/safety series and must also be finite; its per-lane relation to control is gated by the `<1e-3` node-set-side-effect criterion.

## Frozen remedy predicates

### Parent reproduction

Both gating cells must satisfy in **every eligible lane**:
`control_vs_direct_rel >= 1e-3`.

If either does not, V0.25 cannot choose a remedy because the frozen problem did not reproduce.

### EXACT_TARGET_UNION pass

The exact-target remedy passes only if, in every eligible lane:

1. both gating cells have `exact_target_union_vs_direct_rel < 1e-3`;
2. **all six panel cells** have `exact_target_union_vs_direct_rel < 1e-3`;
3. all six have `mixed_common_vs_control_rel < 1e-3`;
4. exact target binding is `<=1e-12`;
5. mixed node construction is exactly common union all three target k values.

### ONE_STEP_GRID_REFINEMENT pass

The refinement remedy passes only if, in every eligible lane:

1. both gating cells have `one_step_refinement_vs_direct_rel < 1e-3`;
2. **all six panel cells** have `one_step_refinement_vs_direct_rel < 1e-3`;
3. refinement mapping is exactly `768->896`, `896->1024`.

### Frozen preference if both pass

If both remedies pass, choose `EXACT_TARGET_UNION` as the preferred production candidate. This preference is frozen before results because it removes interpolation at the evaluation coordinate itself, preserves the original common lattice, and adds at most three nodes in this benchmark rather than globally increasing common-grid density.

No post-result cost weighting or alternate tie-break is allowed.

## Frozen decision hierarchy

Priority:
`INVALID -> INCONCLUSIVE -> UNDERPOWERED -> REPRODUCIBILITY_BLOCKED -> PARENT_NOT_REPRODUCED -> remedy classification`.

Classifications:

- `FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_INVALID`: failed forced preflight, wrong immutable identities, wrong solver count, wrong node construction, non-common binary/software controls, or substantive response before valid preflight. Next: diagnosis only.
- `FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_INCONCLUSIVE`: nonfinite, exact binding failure, invariant/source failure, forbidden object touched. Next: diagnosis only.
- `FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_UNDERPOWERED`: power/native-class requirements not met. Next: expanded replication only.
- `FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_REPRODUCIBILITY_BLOCKED`: any of the 24 primitive scientific series violates the `<1e-5` technical gate. Next: remedy-object reproducibility diagnostic only.
- `FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_PARENT_NOT_REPRODUCED`: either frozen V0.24 parent violation fails `control_vs_direct_rel >=1e-3` in any eligible lane. Next: parent-discrepancy rebaseline audit only.
- `FORCED_BASELINE_EXACT_TARGET_UNION_AND_ONE_STEP_REFINEMENT_REMEDIES_SUPPORTED_EXACT_TARGET_UNION_PREFERRED`: both remedies pass; exact-target union is selected by the frozen tie-break. Authorized next stage only: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`.
- `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`: exact-target union passes and one-step refinement does not. Authorized next stage only: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`.
- `FORCED_BASELINE_ONE_STEP_GRID_REFINEMENT_REMEDY_SUPPORTED`: refinement passes and exact-target union does not. Authorized next stage only: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_REFINED_COMMON_GRID_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`.
- `FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_NO_CANDIDATE_SUPPORTED`: neither passes. Authorized next stage only: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_INTERPOLATION_REMEDY_EXPANSION_AUDIT`.

## Static capacity feasibility note

V0.25 may verify capacity arithmetically but may not execute the full Layer-B traversal. The inherited patched k-output capacity is 1152 and the known full retained Layer-B row count is 107. Even the conservative bound `1025 + 107 = 1132 < 1152` shows that unioning at most one target k per retained row with the 1025-node guarded GRID1024 object is not excluded by the patched k-output count alone. This is only a static feasibility bound, not authorization to execute the 107-row object in V0.25.

## Interpretation firewall

Effect remains `+0/+0`.

V0.25 is a numerical remedy benchmark. It does **not** authorize:

- interpreting any result as dark-sector evidence;
- the full Layer-B 107-row traversal during V0.25;
- global 65537;
- covariance, whitening, nuisance, relation-null or `Wm_S3` access;
- opening a physical-science gate.

A successful remedy may authorize only the explicitly named prospectively frozen full-Layer-B **numerical replay** successor. That successor must be preregistered separately before execution.

Forbidden after results: retune panel cells, target set, candidates, grid mapping, direct semantics, thresholds, power, h, sampling, TOL300, NumPy mask, preference rule or decision branches.
