# DSIR authoritative recovery — latest

Updated: 2026-09-15. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts, independent audit qualifications/corrections, and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention/reproducibility threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized. Diagnostic progress alone does not raise scientific frontier/readiness.

## Closed numerical runtime/replay chain through V0.24

V0.21 causally localized the hosted branch to NumPy AVX-512 runtime dispatch; V0.22 established a deterministic forced NumPy non-AVX512 baseline. V0.23 revalidated all 15 frozen V0.12 production-h replay cells across 32 lanes.

V0.24 terminal authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_V0_24.json`. Frozen classification `FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_CUBIC_INTERPOLATION_SUPPORTED`, effect `+0/+0`. The two immutable parent violations, GRID768/T2 and GRID896/T3, were attributed to common-grid cubic interpolation under the validated forced baseline; mixed exact agreed with direct and node-set solver dependence was rejected. V0.24 authorized exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK`.

## V0.25 — terminal interpolation-remedy benchmark

Preregistration: `prereg/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25.md`, commit `4a1247c56cfbe293a5203ca0b44968ae13aacade`.

Contract: `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25.json`, commit `876b56589d61b263a569583e7cb69e887d68d326`.

Executor: `ci/layerb_beta_forced_baseline_production_h_common_grid_interpolation_remedy_benchmark_v0_25.py`, commit `03cbd910774aa365859abaff18496b01b22bc24d`.

Workflow: `.github/workflows/layerb-beta-forced-baseline-production-h-common-grid-interpolation-remedy-benchmark-v0-25.yml`, commit `f63156fa1adaeb61e496cc5259cf77a584496612`.

Launch/head: `05c87c85093142cfca4d0a432269d5f2440a6e88`.

Authoritative run `34896282790` is terminal `success`, run number 1 / attempt 1: invariant + all 32 lanes + decision terminal; all 32 lanes eligible; native classes 7 active / 25 inactive; decision job `104165699139`. Decision artifact `10370496892`, ZIP digest `sha256:7fcb329027fad04425802f4a90b7874baa2a25e949fbc1057db1a3ed70546562`.

Frozen numerical classification remains `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Parent problem reproduced and all 24 primitive response series were technically reproducible. Exact-target-union matched direct exactly on all six frozen panel cells (`max relative difference = 0.0`) and satisfied node-set safety. One-step grid refinement was rejected because GRID768/T3 remained `0.001136253405249066`, exceeding the frozen `<1e-3` threshold.

## Independent V0.25 funnel audit and provenance correction

Independent audit report: `docs/dsir4/audits/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25_FUNNEL_AUDIT.md`, commit `44c322496cedd63152cdae9dc4a8c7015f7f0e4d`.

Audit qualification authority: `docs/dsir4/authority/LAYERB_BETA_V0_25_PROVENANCE_QUALIFICATION_AUDIT_V0_1.json`, commit `9dcc2be6f5cc2946d8ba6586db196c710034e846`. Audit verdict: **`INVALID_PROVENANCE`**, scoped to the producer authority's artifact-to-repository binding, not to the numerical classifier.

The audit independently downloaded artifact `10370496892` and verified its ZIP digest. The artifact contains exactly `decision.json`, 11082 bytes, actual SHA256 `5bcc9d93c22d32ace5d97f78ff9ce89b399cc4c7e4377b174c5fe882869dd71f`. The earlier producer authority/recovery/handoff had incorrectly recorded `f3d0f47c02c20f39da0fcd71e28665308d53ab8386c876776d3f64da6a7d4bb8`, and the earlier persisted raw decision omitted the executor-emitted 24-entry `primitive_response_metrics` field.

The historical producer result was not rewritten. Exact artifact content is now materialized separately at `results/dsir4/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25_DECISION_ARTIFACT_EXACT.json`, final exact-materialization commit `f26a0bd1dbf03f356509178061df40f104e93a46`.

Terminal provenance correction authority: `docs/dsir4/authority/LAYERB_BETA_V0_25_PROVENANCE_CORRECTION_V0_1.json`, commit `3d51ce928c0e6b76c69f5b42171abc3640c8b1e1`. It supersedes only the incorrect producer provenance fields, preserves the historical V0.25 classification, and restores a clean artifact anchor to the actual terminal bytes.

## Exact next order

1. Treat the independent audit verdict `INVALID_PROVENANCE` as historical qualification of the original producer binding; do not erase or relabel it.
2. Treat `LAYERB_BETA_V0_25_PROVENANCE_CORRECTION_V0_1.json` as the current terminal provenance correction. Numerical V0.25 classification remains unchanged.
3. The authorized successor is again exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`, but it is **not open for execution** until a new prospective preregistration and frozen contract are committed.
4. That successor must freeze the full 107-row denominator/input identities and exact-target-union construction prospectively; V0.25's `1025 + 107 = 1132 < 1152` is capacity feasibility only, not execution authorization.
5. No covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, or downstream physical-science gate is authorized.
6. Keep effect at `+0/+0`; numerical remedy support is not statistical/model evidence and not dark-sector evidence.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
