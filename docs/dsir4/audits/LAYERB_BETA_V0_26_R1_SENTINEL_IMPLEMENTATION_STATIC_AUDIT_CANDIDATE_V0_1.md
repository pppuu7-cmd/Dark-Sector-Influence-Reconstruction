# DSIR V0.26 R1 sentinel implementation static-audit evidence V0.1

Status: **AUDIT EVIDENCE CANDIDATE — NOT LAUNCH AUTHORITY**  
Date: 2026-09-15  
Effect: `+0/+0`.

## Scope

This record preserves response-blind hosted evidence for the preregistered V0.26 R1 pre-full sentinel implementation. It does not authorize a CLASS sentinel solve, does not authorize a full 107-row replay, and does not open downstream science.

Construction is based on main `438ab2e6732512cf50c163719ade01575257b209`, where the independently qualified R1 specification and its promotion authority are already present.

## Frozen implementation objects

- R1 contract blob: `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.
- construction/promotion authority blob: `cdbcea2622564d40aa9d1edc045a5808f8cdd1c4`.
- sentinel executor: `ci/layerb_beta_v026_r1_sentinel_v0_1.py`, blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`.
- sentinel decision finalizer: `ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py`, blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`.
- inert workflow blueprint: `docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_SCIENCE_WORKFLOW_CANDIDATE_V0_1.yml`, blob `1ed36c850d80537646556a858204cac14eca852e`.
- sentinel implementation contract: `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json`, blob `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`.
- response-blind auditor actually executed: `ci/layerb_beta_v026_r1_sentinel_static_audit_v0_2.py`, blob `ebb1db6b365560e9e4c8ab7e575d163bdab58cc4`.

A pre-execution V0.1 static-auditor source contained an invalid quoted-string check. It was detected by source inspection before any hosted execution, was never used for a result, and has been removed from the final branch diff. V0.2 is the only hosted sentinel static auditor.

## Fail-closed implementation

The science executor has separate `static-preflight`, `fingerprint`, `lane`, and `child` modes. `lane` and `child` require a future file with schema `LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1`, status `TERMINAL_LAUNCH_AUTHORITY`, `sentinel_science_execution_authorized=true`, and `full_107_row_execution_authorized=false` before the numerical chain or CLASS solve may proceed.

No such launch authority exists on the candidate branch. No launch sentinel exists. The actual science workflow is not present under `.github/workflows`; only an inert blueprint under `docs/dsir4/workflow_candidates/` exists.

The implementation freezes the preregistered sentinel exactly:

- 32 `ubuntu-24.04` lanes;
- mixed batches `M076`, `M298`, `M300`;
- direct comparators `D50`, `D00`, `D58`;
- requested-node counts `PURE=897`, `M076=1152`, `M298=1141`, `M300=996`, `D50=1146`, `D00=1152`, `D58=99`;
- 14 CLASS constructions per eligible lane = 2 pure + 6 mixed + 6 direct;
- maximum possible 448 constructions if all 32 lanes are eligible;
- minimum power `6` eligible, `3` native AVX512-active and `3` native AVX512-inactive;
- technical primitive spread and native-class separation strict `<1e-5`;
- mixed-common vs pure-common strict `<1e-3`;
- exact-target vs direct strict `<1e-3`;
- requested-node binding `<=1e-12`.

The finalizer preserves the sentinel-only hierarchy `SENTINEL_INVALID -> SENTINEL_INCONCLUSIVE -> SENTINEL_UNDERPOWERED -> SENTINEL_REPRODUCIBILITY_BLOCKED -> SENTINEL_NODE_SET_SIDE_EFFECT_BLOCKED -> SENTINEL_DIRECT_REFERENCE_BLOCKED -> SENTINEL_PASS`. Even `SENTINEL_PASS` leaves `full_replay_launch_authorized=false` and requires a separate result audit/authority.

## Hosted static audit

Workflow: `.github/workflows/layerb-beta-v026-r1-sentinel-static-audit-v0-1.yml`.

Exact execution head: `510a7145bd5ea49e45db3ab53e56093567da746f`.

Actions run `34958187529`, run number `1`, attempt `1`, event `push`, terminal `success`.

Artifact:

- id `10392400462`;
- name `layerb-beta-v026-r1-sentinel-static-audit-v0-1`;
- GitHub digest and independently downloaded ZIP SHA256 both `2384436ee78a9a1ee4d55e5297e3b36f2dff9ffe53a243e20af0b2f7dfe729f0`.

Inner files independently rechecked:

- `sentinel_static_audit.json`: 1,344 bytes, SHA256 `33972dc25eabb7a19097164234b5e336d4bc4bd3cfef37ff8a442443810b75a8`;
- `sentinel_static_audit.sha256`: 98 bytes, SHA256 `b0da8eb1f0a634a2efa1876a1798bc80a16087389f920a5dccbb25e9494de0e5`;
- `executor_static_preflight.json`: 861 bytes, SHA256 `63429e12875545d0a3d0be01882c6bf9b71dd5e26a840fe739b969fa3f5be3bb`;
- `lane_without_authority.txt`: 1,020 bytes, SHA256 `8ebb37d6a3d51d46e259f2eb66d5622162a5494cc94f085c52534d501208991d`.

Receipt token: `PASS_LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_STATIC_AUDIT_PLUS_0_PLUS_0`.

Classification: `SENTINEL_IMPLEMENTATION_RESPONSE_BLIND_STATIC_AUDIT_PASS`.

The receipt binds the exact R1 contract, promotion authority, implementation contract, executor, decision finalizer, workflow blueprint, and source plan. It records:

- `active_science_workflow_present=false`;
- `launch_authority_present=false`;
- `launch_sentinel_present=false`;
- `lane_without_launch_authority_failed_closed=true`;
- `class_solver_invoked=false`;
- `scientific_response_read=false`;
- `covariance_read=false`;
- `sentinel_science_execution_authorized=false`;
- `full_107_row_execution_authorized=false`.

The static preflight independently reconstructs the exact source plan and GRID896 identity and returns `M076/M298/M300`, `D50/D00/D58`, and 14 constructions/lane with no scientific response access.

The negative authorization test invokes `lane` without a launch authority and terminates with the exact exception `RuntimeError: sentinel science launch authority is required and absent` before any CLASS import/solve. No unauthorized lane output is created.

## Interpretation

This evidence supports only the internal/static consistency and fail-closed authorization design of the sentinel implementation. It is not enough to launch the sentinel. The next admissible gate is an independent funnel review of the implementation contract/code/blueprint/static-run provenance. Only a separate terminal authority from that review may authorize creation of an active science workflow and explicit one-run launch authority.

Full 107-row execution and all downstream scientific layers remain closed.
