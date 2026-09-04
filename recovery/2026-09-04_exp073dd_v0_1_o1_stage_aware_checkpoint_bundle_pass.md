# DSIR recovery — Exp073DD v0.1 O1 stage-aware checkpoint bundle PASS

Date: 2026-09-04. Scope DSIR only; RTK/RQIR excluded.

## Authority
- Preregistration commit/blob: `3149db51e4091ef570be7c7bfd8f1e1781f2bd1a` / `0e7b9392df21f21172ca0d8fb12976c381803fe5`.
- Stage-aware transport implementation commit/blob: `92fa960bc640e4b41329e4660f8ef67a7fc5204a` / `b25232223511a7f65abdf3437a40a1c3aaec4702`.
- Hosted regression commit/blob: `34a1a9885495bbdca68a78ee150c034919325a01` / `c4172ed349b6f0e3cb8023c6dedb0ae32283ddf2`.
- Activation/workflow head: `dbeb4f66c681a94364fcffee92cb11464bf2bc57`.
- Actions run/job: `33884749118 / 101061680308`.
- Artifact: `9941347886`, name `exp073dd-stage-aware-checkpoint-bundle-dbeb4f66c681a94364fcffee92cb11464bf2bc57`.
- Actions artifact digest: `sha256:ab8c4e322121e60feabad862224f5b818e6d73c9526005ba0745bb40a5c8d2ce`.
- Independently downloaded artifact ZIP SHA256: `ab8c4e322121e60feabad862224f5b818e6d73c9526005ba0745bb40a5c8d2ce`, exact match to Actions digest.

## Raw artifact consumption
Raw `exp073dd_classification.json` was downloaded and inspected, not inferred from workflow success. It contains `token=O1_STAGE_AWARE_CHECKPOINT_BUNDLE_PASS`, `classification=+0/+0`, `regression_rc=0`, `run_id=33884749118`, `source_head=dbeb4f66c681a94364fcffee92cb11464bf2bc57`.

Raw `exp073dd_receipt.json` has all prospectively required positive fields exactly `true`: `multi_stage_progression`, `cross_stage_object_reuse`, `partial_stage_restore_rejected`, `resume`, `exact_file_restore`, `existing_ref_exact_lease`, `verified_absent_safe_creation`, `exact_post_head`, `ab_namespace_isolation`, `stage_order_rejection`, `corrupt_object_rejection`, `object_cap_64mib`, `transition_cap_1gib`, `same_control_plane`. It also has exactly `science_numerics_executed=false`, `wm_s3_authority_created=false`, `exp073bu_activated=false`.

## Frozen classification
`O1_STAGE_AWARE_CHECKPOINT_BUNDLE_PASS`, support/infrastructure `+0/+0`.

Validated O1 semantics are: same admitted Exp073DB remote-Git/checkpoints control plane; six ordered stage names; content-addressed immutable objects; <=64 MiB objects; <=1 GiB remote transitions; interrupted incomplete stage rejected by restore; resume to completion; exact file restore; cross-stage object reuse; existing-ref exact lease; verified-ABSENT safe creation; exact post-head; A/B namespace isolation; stage-order rejection; corrupt-object rejection. All regression payloads are synthetic.

## Authority boundary
This O1 result closes the transport-layer stage-bundle gap identified after Exp073DC N2. It does **not** by itself prove that the production Exp073BU driver invokes remote durable sync after each local scientific stage. Therefore O1 permits only prospective production durability-hook integration and hosted/static regression. It does not activate Exp073BU and creates no Wm_S3 scientific authority.

The current Exp073BU v0.2 manual science shell is not sufficient by itself for the user's durable-checkpoint requirement because its frozen driver still writes local stage manifests under the home checkpoint root without an admitted production binding to this O1 remote stage-bundle transport. Home science remains blocked until that hook is prospectively implemented and audited without changing scientific arithmetic.

Historical Exp073BU v0.1 workflow-validation failures and all prior scientific/resource results remain immutable.
