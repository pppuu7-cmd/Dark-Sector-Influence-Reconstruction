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

## Open PR #168 — prospective Core-v1 scope proposal

PR #168, `Freeze DSIR Core v1 completion scope`, is open on branch `dsir-core-v1-freeze-scope`, reviewed head `4983e0b1a8537e64b6a90eacd8857fe98ac0ebe0`. It adds a prospective Core-v1 completion-scope document and changes the branch copy of `docs/CURRENT_PROCESS.md`; it does not change V0.25 code, inputs, thresholds, artifacts, classification, or the current terminal authority.

Independent audit: `docs/dsir4/audits/DSIR_CORE_V1_COMPLETION_SCOPE_PR168_FUNNEL_AUDIT_V0_1.md`, commit `c6e5ec83dbdfffceb8417880b233493850be513a`.

Qualification authority: `docs/dsir4/authority/DSIR_CORE_V1_COMPLETION_SCOPE_PR168_QUALIFICATION_AUDIT_V0_1.json`, commit `37b4f7119f376a5b474f60e3b6607c611fad2b49`. Verdict: **`QUALIFIED`**.

The proposal is admissible only as prospective governance/release-scope planning. Its F1 description is compatible with the existing authorized successor, but the phrase `Authorized critical path` must not be read as current authorization for F2-F7. Covariance, whitening, nuisance, statistical/model gates, relation-null, `Wm_S3`, global 65537 and downstream science remain closed until separately reached through terminal authority.

The PR's green Actions run `34910842417` is not validation of the scope contract. It is the pre-existing G-T-tau additive-projection workflow; its artifact `10374282750` has digest `sha256:3648048f8ebae4c33cf2b99e702b338027d7a5725d9c3bfbfed3691edf160633` and is incidental regression evidence only.

PR #168 does not update this recovery file and does not add the F1 preregistration/immutable contract. If its scope is later accepted on main, recovery must be reconciled and the current 68% repository-readiness / 67% scientific-frontier accounting must remain authoritative until any replacement readiness dimensions have frozen denominators, calculation rules, migration rules and initial values. `DSIR Core v1 FROZEN` must never be equated with scientific closure or physical dark-sector inference.

## V0.26 prospective candidate branch — hosted response-blind static audit qualification

A new research branch `research/v026-full-layerb-prereg` proposes the authorized full Layer-B numerical replay. Reviewed branch head: `ed67dade1fb08873ec3807a9513a55a725527fe6`. The branch is **not main authority and not executable**.

Candidate chronology is prospective: preregistration commit `8fc1a9d8dc908309f956e2295e934639730d3796`; base contract `2cf8c2fa3ee24c29c77026e8dd022b67a00cfa14`; static auditor `da18cff9982d7ef91f13caa7a46a388295cd5207`; hardening amendment `54c7a6c32d04cf498df6cd9a79e1bc04b8ad2c90`; route-specific tolerance correction `e6b5e622e27ff8fde0820cbf0f731fd0c3751cd3`; hosted static-audit launch head `20eb0f8db1bc4d426fd957dbed6a1211a0459f10`.

Hosted response-blind static Actions run `34952288638` is terminal `success`, run number 1 / attempt 1, and is the unique push run for that exact head. Job `104325850674` succeeded. Artifact `10389832162` has ZIP digest `sha256:8fce87986b0e96356fdc6935df0f16470b224d10caa371db3fe644929d4616b3`; inner `v026_static_audit.json` is 2924 bytes, SHA256 `718a1ba3be7ce14527e8995bff174c9f53e540a0e5f74008cff0bc1e687acbcd`. The run invoked no CLASS solver and read no scientific response or covariance.

The static audit independently reproduces the exact source-plan bytes and principal response-blind batch identities: source artifact `10298655751` ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`, `plan.json` 3,953,984 bytes SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`; mixed plan 301 batches with canonical SHA256 `59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85`; direct plan 59 batches with canonical SHA256 `1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864`; GRID896 has 897 guarded common nodes and zero exact-target overlap. Source run `34695347893` itself failed, but its response-blind `materialize-plan` job `103557768867` succeeded and is the scoped provenance source for artifact `10298655751`; the failed parent run is not relabelled as a successful science run.

Independent funnel audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_RESPONSE_BLIND_STATIC_AUDIT_FUNNEL_REVIEW_V0_1.md`, commit `182676e8b53c9cf4fab673f5164fb43849ca0fc4`. Qualification authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_RESPONSE_BLIND_STATIC_AUDIT_QUALIFICATION_V0_1.json`, commit `d50419d3b8e4a9fc8ee10d9e28b98043d9cf7f2b`. Verdict: **`QUALIFIED`**.

Concrete qualification: the candidate preregistration/base contract freeze M013 maximum mixed `.17g` payload at `25062` bytes, but the hosted workflow correctly pins the candidate's NumPy `1.26.4` and its immutable receipt reports `25063`. Both are safely below the parser bound `32768`, so this is not a capacity failure; it is a frozen-static-identity mismatch. The static auditor does not assert equality to the frozen `25062`, so its PASS token cannot mean that every frozen static scalar reproduced exactly. An independent NumPy `2.3.5` response-blind control reproduces both `25062` and the hardening amendment's recorded non-authoritative local output SHA256 `d55cb61f2cd5338dba0b36df656409fdc248afe3cfa1972fe060b3a09b09c515`, while the hosted NumPy-1.26.4 receipt is `718a1ba3...`; this is an explicit environment-sensitive generated-grid/serialization witness.

The branch's final trigger note at commit `ed67dade1fb08873ec3807a9513a55a725527fe6` says zero run was created. That observation is stale: Actions shows run `34952288638` created at 09:23:21Z and completed at 09:23:39Z, while the note commit timestamp is 09:23:37Z. Actions overrides the race-prone branch note for workflow/provenance state.

No science execution is opened. Before promotion, create one consolidated V0.26 R1 preregistration plus one immutable machine-readable contract that directly incorporates the alpha-route hardening and route-specific tolerance correction, removes/corrects the superseded `25062` scalar, freezes the intended NumPy-1.26.4 GRID896 node identity (preferably exact binary64/u64hex hash), defines the payload-byte counting convention, and makes the static auditor assert the R1 expected identity. The R1 pair then requires an independent contract audit **before** any sentinel executor/workflow or 107-row execution is authorized.

## Exact next order

1. Treat the independent V0.25 audit verdict `INVALID_PROVENANCE` as historical qualification of the original producer binding; do not erase or relabel it.
2. Treat `LAYERB_BETA_V0_25_PROVENANCE_CORRECTION_V0_1.json` as the current terminal V0.25 provenance correction. Numerical V0.25 classification remains unchanged.
3. Treat the PR #168 scope audit verdict `QUALIFIED` as a qualification of that unmerged prospective governance proposal only. It does not modify scientific gate authorization.
4. Treat `LAYERB_BETA_V0_26_RESPONSE_BLIND_STATIC_AUDIT_QUALIFICATION_V0_1.json` as the current independent qualification of the research-branch V0.26 static candidate evidence. Do not promote the hosted PASS token into a numerical-response or science PASS.
5. The authorized successor remains exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`, but it is **not open for execution**. The next admissible gate is a consolidated prospective V0.26 R1 preregistration + immutable contract followed by independent R1 contract audit.
6. Do not author/launch the sentinel science workflow or full 107-row workflow until that R1 contract audit authorizes it. The current split candidate and its amendments are not execution authority.
7. The R1 must retain the full 107-row denominator/input identities and exact-target-union construction prospectively, incorporate route-specific alpha/beta tolerances, and bind exact generated GRID896 identity under the intended pinned runtime. V0.25's `1025 + 107 = 1132 < 1152` remains capacity feasibility only, not execution authorization.
8. No covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, or downstream physical-science gate is authorized.
9. Keep effect at `+0/+0`; response-blind static consistency and governance progress are not statistical/model evidence and not dark-sector evidence.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
