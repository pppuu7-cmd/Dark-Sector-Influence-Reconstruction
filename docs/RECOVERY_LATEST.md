# DSIR authoritative recovery — latest

Updated: 2026-09-15. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

GitHub repository state, immutable DSIR4 preregistrations/contracts/authorities, terminal GitHub Actions artifacts, independent audit qualifications/corrections, `docs/CURRENT_PROCESS.md`, and this file are the durable source of truth. Chat is not authority.

## Frozen scientific boundaries

Production `h=1e-4`; native `k_per_decade_for_pk=20`; production sampling `0.00035`; scientific numerical threshold strict `<1e-3`; technical reproducibility threshold strict `<1e-5`; requested/exact-node binding `<=1e-12`. Consolidated V0.26 R1 freezes alpha canonical-32769 route `tol_perturb_integration=3e-10` and beta exact-target route `tol_perturb_integration=1e-12`. Covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain unopened. Diagnostic/static progress alone does not raise scientific frontier/readiness.

## Terminal numerical/reproducibility chain through V0.25

V0.21 localized the hosted discrepancy to NumPy AVX-512 dispatch; V0.22 established a deterministic forced non-AVX512 baseline; V0.23 revalidated the frozen production-h replay cells; V0.24 attributed the remaining immutable violations to common-grid cubic interpolation under the validated baseline.

V0.25 authoritative run `34896282790` is terminal success, run #1 / attempt #1. Invariant + all 32 lanes + decision completed; all 32 lanes eligible; native classes 7 active / 25 inactive. Decision job `104165699139`; artifact `10370496892`; ZIP digest `sha256:7fcb329027fad04425802f4a90b7874baa2a25e949fbc1057db1a3ed70546562`.

Frozen numerical classification remains `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Exact-target-union matched direct exactly on all six frozen benchmark cells and satisfied node-set safety. One-step refinement remained rejected because GRID768/T3 = `0.001136253405249066 >= 0.001`.

Independent V0.25 funnel audit report `docs/dsir4/audits/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25_FUNNEL_AUDIT.md` gave historical verdict **`INVALID_PROVENANCE`** for the original producer artifact-to-repository binding only. It independently established actual terminal `decision.json` SHA256 `5bcc9d93c22d32ace5d97f78ff9ce89b399cc4c7e4377b174c5fe882869dd71f`, correcting the producer-recorded `f3d0f47c...`, and found the historical persisted raw decision omitted the 24-entry `primitive_response_metrics` field.

Terminal provenance correction `docs/dsir4/authority/LAYERB_BETA_V0_25_PROVENANCE_CORRECTION_V0_1.json` preserves the historical result and repairs only provenance. Exact terminal bytes are separately materialized at `results/dsir4/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25_DECISION_ARTIFACT_EXACT.json`.

The corrected V0.25 authority authorizes only `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`; it does not directly authorize a 107-row execution.

## Historical split V0.26 candidate qualification

The earlier `research/v026-full-layerb-prereg` split candidate remains historical. Its hosted response-blind static run `34952288638` exposed a concrete runtime-sensitive identity mismatch: split candidate expected M013 mixed `.17g` payload maximum `25062`, while pinned hosted NumPy `1.26.4` produced `25063`. Independent audit verdict was **`QUALIFIED`**, requiring a consolidated R1 specification. That historical result is not rewritten.

## Consolidated V0.26 R1 is now on main

R1 preregistration: `prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.md`, git blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`.

R1 machine contract: `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json`, git blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Independent R1/PR169 terminal audit authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json`, git blob `cdbcea2622564d40aa9d1edc045a5808f8cdd1c4`, verdict **`QUALIFIED`**. PR #170 carrying the audit authority merged before exact PR #169 promotion. Exact R1 promotion merge is commit `438ab2e6732512cf50c163719ade01575257b209`.

R1 freezes:

- full retained denominator exactly 107 rows, DES 53 / BOSS 54, retained-ID SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`, order SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- response-blind source plan artifact `10298655751`, ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`, `plan.json` 3,953,984 bytes SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`;
- exact hosted NumPy-1.26.4 GRID896 binary64 payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- mixed target-plan SHA256 `59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85`, payload-manifest SHA256 `6b0f08b196f6afa2086a4275ec364d527c50786921ef0ca1d77a30edbed91ce6`, M013 max `25063` bytes;
- direct target-plan SHA256 `1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864`, payload-manifest SHA256 `99a6e4c48d353b05bea5000fc27417731d1c347071254232ed807554ee569da6`;
- alpha canonical-32769 eight-chunk route at `3e-10`; beta exact-target-union route at `1e-12`;
- full solver accounting 738 CLASS constructions;
- complete downstream firewalls and numerical-only interpretation ceiling.

R1 preregisters a pre-full sentinel: 32 lanes; M076/M298/M300 with D50/D00/D58 comparators; 14 CLASS constructions/lane; minimum 6 eligible with >=3 native AVX512-active and >=3 native AVX512-inactive; strict primitive reproducibility/class-separation `<1e-5`; mixed-common vs pure-common and exact vs direct strict `<1e-3`; requested-node binding `<=1e-12`; no science retry solely to change class mix.

## PR #171 — qualified inert sentinel implementation

PR #171 `Construct DSIR V0.26 R1 pre-full sentinel candidate`, exact reviewed head `973eea003e6e246b7e1853b5469cb0a7d90c8177`, base `438ab2e6732512cf50c163719ade01575257b209`, is currently an open draft candidate and is **not** a sentinel science result.

Frozen implementation blobs:

- executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- decision finalizer `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- inert science-workflow blueprint `1ed36c850d80537646556a858204cac14eca852e`;
- sentinel implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`;
- static auditor V0.2 `ebb1db6b365560e9e4c8ab7e575d163bdab58cc4`.

PR171 adds no active sentinel science workflow, no launch authority and no launch descriptor. The executor requires a future terminal launch authority before lane/child execution. Native host classification occurs unmasked; forced preflight/substantive child are fresh subprocesses with the exact frozen non-AVX512 NumPy mask. The substantive child verifies the mask and forced dispatch profile before CLASS scientific work, verifies exact GRID896 identity and uses beta `tol_perturb_integration=1e-12`.

## PR #171 response-blind static evidence

Hosted static run `34958187529` is terminal success, run #1 / attempt #1, event push, job `104345200819`. Artifact `10392400462` ZIP SHA256 `2384436ee78a9a1ee4d55e5297e3b36f2dff9ffe53a243e20af0b2f7dfe729f0`; independent download matched exactly.

Artifact members:

- `sentinel_static_audit.json`: 1344 bytes, SHA256 `33972dc25eabb7a19097164234b5e336d4bc4bd3cfef37ff8a442443810b75a8`;
- `executor_static_preflight.json`: SHA256 `63429e12875545d0a3d0be01882c6bf9b71dd5e26a840fe739b969fa3f5be3bb`;
- `lane_without_authority.txt`: SHA256 `8ebb37d6a3d51d46e259f2eb66d5622162a5494cc94f085c52534d501208991d`.

The receipt records no CLASS solve, no scientific response read, no covariance read, no active science workflow, no launch authority, no launch descriptor, no sentinel science authorization and no full-107 authorization. The unauthorized-lane negative control fails before CLASS with `sentinel science launch authority is required and absent` and produces no lane artifact.

Separate external funnel run `34958540961` is terminal success, run #1 / attempt #1, job `104346337918`. Artifact `10392755109` ZIP SHA256 `8fade9139142e2ab3f6a99ef2696853d3f5dce026c6fa130a43d96bff6870edb`; independent download matched. Inner `funnel_audit.json` is 1848 bytes SHA256 `ac2c2cc9d2aa536207a8ee5121cb37d92665f521cb6e0ef41865540810ded333`, verdict `QUALIFIED`.

## Current independent PR #171 audit authority

Audit report: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_FUNNEL_AUDIT_V0_2.md`, commit `3200e887af26b686af882604ec8e3665785b2cd0`.

Terminal audit authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json`, commit `19a88e7e60f8c1bbb6711c5e7a2ea4fd486ab231`. Verdict: **`QUALIFIED`**.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_PR171_V0_2.md`, commit `b6611dc024e9f0306a00deff20d6546e66e01e77`.

The exact PR171 implementation may be promoted as an inert pre-full sentinel implementation. It does **not** authorize sentinel CLASS execution.

### Launch-provenance qualification

A concrete counterexample qualifies the separate external funnel receipt's proposed launch hardening. The current inert blueprint requires the future launch descriptor to contain the exact launch-authority git blob. The external funnel receipt also proposes that the launch authority contain the final launch-descriptor git blob. Mutual final git-blob hash binding forms a circular provenance equation and is not a generally realizable ordinary construction.

The corrected requirement is an **acyclic exact-hash provenance DAG**. Preferred sequence:

1. freeze the active sentinel workflow;
2. create launch authority binding exact R1 contract, R1 promotion authority, executor, decision finalizer and active-workflow git blob; authority may authorize exactly one sentinel run and must keep full107 false;
3. create the launch descriptor after that authority, binding launch-authority and active-workflow blobs;
4. independently response-blind static-audit the complete inactive launch package;
5. only a terminal launch-package audit authority may permit the one sentinel science run.

The launch authority must not simultaneously require the final launch-descriptor blob when the descriptor already binds the authority. An equivalent reverse DAG is acceptable only if it avoids mutual hash cycles.

This qualification does not invalidate current PR171 static evidence because neither launch object exists and no science response was executed.

## Exact current gate position

`V0.25 TERMINAL NUMERICAL AUTHORITY -> V0.26 R1 PREREGISTERED + INDEPENDENTLY QUALIFIED SPECIFICATION ON MAIN -> PR171 INERT SENTINEL IMPLEMENTATION QUALIFIED FOR EXACT PROMOTION -> LAUNCH PACKAGE NOT YET FROZEN/AUDITED -> SENTINEL SCIENCE NOT EXECUTED -> FULL 107 ROW CLOSED`.

No substantive sentinel value exists. Therefore do not infer interpolation success, solver-tolerance success, cross-host reproducibility, execution-order independence, statistical validity, nuisance removal or physical identifiability from static CI.

## Exact next order

1. Preserve V0.25 historical numerical classification and historical `INVALID_PROVENANCE` audit verdict together with its separate provenance correction.
2. Treat consolidated V0.26 R1 on main as the current prospective scientific/numerical specification; do not fall back to the historical split candidate.
3. Treat `LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json` as the current terminal audit authority for PR171 implementation scope.
4. Exact promotion of the qualified PR171 implementation blobs is authorized. Mutation of the scientific object, sentinel selections, thresholds, tolerances, dispatch semantics, denominator or response interpretation is forbidden without a new prospective successor.
5. After promotion, construct only an **inactive** active-workflow/launch-authority/launch-descriptor package with an acyclic exact-hash DAG.
6. Run a separate response-blind static launch-package audit. Do not execute CLASS sentinel science from PR171 authority alone.
7. Only after a terminal launch-package authority may exactly one frozen sentinel science run be launched.
8. Even a later `SENTINEL_PASS` does not automatically open full 107-row execution; it requires an independent sentinel-result funnel audit and a distinct explicit full-replay launch authority.
9. Full 107-row replay, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537 and downstream physical science remain unauthorized now.
10. Keep effect `+0/+0`, repository readiness `68%`, scientific frontier `67%`.

## Open PR #168 governance proposal

PR #168 remains a prospective Core-v1 governance/release-scope proposal only. Its prior independent verdict `QUALIFIED` is scoped to governance wording and does not authorize F2-F7 or alter the numerical gate chain above.
