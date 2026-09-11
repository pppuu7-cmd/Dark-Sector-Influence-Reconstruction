# Recovered Exp073JL — terminal authority schema v0.1

Date prospectively frozen: 2026-09-11, while recovered JL retry `34544293038` is still running and before its terminal scientific-support verdict is known. Scope: DSIR Article III process/provenance only.

## Purpose

Define one branch-neutral durable authority shape for the recovered Exp073JL v0.2 terminal artifact so downstream JM/JN activation code cannot influence how the JL result is packaged after the verdict is known.

This schema does not define or change the JL scientific classifier. That remains the prospectively frozen recovered-JL preregistration. It only prescribes lossless transcription of independently verified terminal facts.

## Required provenance fields

Every durable recovered-JL terminal authority, including infrastructure-invalid outcomes, must include:

- `schema` identifying the recovered terminal authority version;
- `experiment = "Exp073JL"`;
- `classification` copied exactly from the terminal `result.json`;
- `effect = "+0/+0"`;
- `artifact_verified_independently` boolean, which may be true only after ZIP/result/capacity provenance has actually been checked outside the producing workflow;
- `run_id`, `job_id`, `workflow_head_sha`, `artifact_id`;
- `artifact_zip_sha256`, `result_json_sha256`, and `capacity_patch_json_sha256` where the capacity receipt exists;
- frozen helper/prereg identities used by the run;
- `scientific_authority_created = false` for Exp073JL itself because JL remains support-only;
- `covariance_restriction_authorized = false` and `Wm_S3_opened = false` regardless of valid JL convergence outcome.

## Required observations block for valid scientific-support outcomes

For either valid terminal classification

- `COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0`, or
- `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`,

create an `observations` object by direct transcription only:

- `max_atomic_coarse_vs_fine_relative_component_difference` <- `result["convergence"]["max_relative_component_difference"]`;
- `finite_nonzero_status_changed` <- `result["convergence"]["finite_nonzero_status_changed"]`;
- `row_label_changed` <- `result["convergence"]["row_label_changed"]`;
- `boss_dense_z_disagreement` <- `result["convergence"]["boss_dense_z_disagreement"]`;
- `invalid_row_count` <- `result["layer_b"]["invalid_row_count"]`;
- `invalid_row_fraction` <- `result["layer_b"]["invalid_row_fraction"]`;
- `retained_after_layer_b` <- `result["layer_b"]["retained_after_layer_b"]`;
- `unsupported_target_evaluations` <- top-level recovered-JL result field of the same name;
- `max_requested_node_coordinate_rel_mismatch` <- top-level recovered-JL result field of the same name;
- `total_solver_constructions` <- `result["execution_lifecycle"]["total_solver_constructions"]`;
- `max_live_instances` <- `result["execution_lifecycle"]["max_live_instances"]`;
- `total_get_transfer_calls` <- `result["request_plan_authority"]["total_get_transfer_calls"]`;
- canonical coarse/fine decoded node SHA256 and response-blind coarse/fine plan SHA256 copied from the result receipts.

No rounding, threshold transformation, replacement of missing values, branch-dependent field omission, or derived rescue statistic is permitted.

The `observations` block exists for provenance and downstream cross-checks. **Only `classification` plus `artifact_verified_independently=true` activates JM or JN according to their frozen preregistrations.** Observation values must not be promoted into extra activation predicates unless that predicate was already frozen in the relevant branch preregistration. In particular, the known JM implementation bug adding `retained_after_layer_b==107` and `unsupported_target_evaluations==0` to activation remains forbidden.

## Infrastructure-invalid outcomes

For `INVALID_INFRA_PLUS_0_PLUS_0`, the authority must instead include the exact failure stage/error and all available provenance receipts. It must not fabricate a scientific `observations` block from absent/incomplete solver output. JM and JN activation are both false.

## Independent-verification requirements for valid outcomes

Before setting `artifact_verified_independently=true`, verify at minimum:

1. GitHub artifact digest equals independently downloaded ZIP SHA256;
2. terminal archive contains the expected `result.json` and capacity-patch receipt only/according to the frozen workflow;
3. result/capacity file SHA256 are recorded;
4. terminal classification is one of the two valid frozen scientific-support classifications;
5. canonical coarse/fine node identities equal Exp073JT authorities;
6. live response-blind plan identities equal independently verified request-plan authority V0.2;
7. exactly 8 solver constructions, max one live, final live count zero, no cross-process raw combination;
8. total transfer calls exactly 4040, unsupported target evaluations zero, lookup mismatch <=1e-12;
9. parent retained identity/order and inherited 107-row accounting are preserved;
10. no covariance/Wm_S3 authorization is created by JL.

Only after these checks may a valid JL authority select the already-frozen conditional downstream branch.

## Readiness boundary

Defining or populating this authority schema does not itself increase Article III repository readiness. Scientific readiness may be reassessed only after the terminal recovered-JL classification is independently verified.
