# DSIR V0.26 R1 sentinel launch-package static-audit evidence V0.1

Status: **AUDIT EVIDENCE CANDIDATE — INACTIVE / NOT SCIENCE AUTHORITY**  
Date: 2026-09-15  
Effect: `+0/+0`.

## Scope

This record preserves the response-blind static audit of the inactive, acyclic sentinel launch package. No active sentinel science workflow, final launch authority, final launch descriptor, or launch-package qualification authority is present at the audited candidate paths. No CLASS solver or scientific response was invoked.

## Frozen acyclic package

The package uses the realizable provenance DAG required by the V0.26 R1 sentinel implementation qualification:

`W -> A(W) -> L(A,W) -> static audit -> future Q(W,A,L)`.

Frozen objects:

- `W`: `docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml`, git blob `19907175f0f3417ddee2aba6916d961c6be02e26`;
- `A`: `docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json`, git blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`;
- `L`: `docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json`, git blob `9c217e41764d979bea12644fae372354241bc976`;
- package contract: `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_CONTRACT_V0_1.json`, git blob `26806597e651fb22956de59f102c0ad24d11c576`;
- static auditor: `ci/layerb_beta_v026_r1_sentinel_launch_package_static_audit_v0_1.py`, git blob `8efdccffcf0e740a799fd462c3988cdc20a29b1a`;
- static-audit workflow: `.github/workflows/layerb-beta-v026-r1-sentinel-launch-package-static-audit-v0-1.yml`, git blob `09e3a4b14bacd33e451b5f35aa4dc78004ac7945`.

`A` binds W but deliberately does not bind L. `L` is created after A and binds both A and W. A separate future package qualification `Q` must be created only after static/external package audit and must bind all W/A/L blobs.

## Upstream bindings

The package binds the already qualified main implementation:

- R1 contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`;
- R1 promotion authority blob `cdbcea2622564d40aa9d1edc045a5808f8cdd1c4`;
- sentinel implementation contract blob `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`;
- sentinel implementation qualification V0.2 blob `5d042377fa48d896865db0ada11508015c74e350`;
- sentinel executor blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- sentinel decision finalizer blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`.

## One-run safeguards frozen in W/A/L

The future active workflow W accepts only a `push` to `main` adding the exact final launch-descriptor path. At authorization time it requires:

- `github.run_attempt == 1`;
- the final launch path to occur exactly once in the push event's `added` collection and not in `modified` or `removed`;
- non-forced push;
- a unique push-triggered run for the exact head in the exact workflow;
- exact A/W/L live git-blob matches;
- a future terminal package qualification Q binding the exact W/A/L blobs;
- `authorized_launch_count=1`;
- `full_107_row_execution_authorized=false`.

Workflow dispatch is absent from W. Concurrency uses `cancel-in-progress: false`.

A authorizes exactly one pre-full sentinel execution in its intended final state, binds W and all frozen upstream implementation identities, requires Q, and explicitly does not bind the later L blob. L binds exact A and W and is immutable after the single new-file trigger.

## Static hosted audit

Workflow run `34959657394`, run number 1 / attempt 1 / event `push`, exact head `5d42cd84ce54c9781d7bbefd41b01d3cf775fbd7`, conclusion `success`.

Job `104349972403`, `static-launch-package-audit`, conclusion `success`; every step terminal success, including future-workflow YAML syntax check and exact W/A/L/provenance validation.

Artifact:

- id `10393170033`;
- name `layerb-beta-v026-r1-sentinel-launch-package-static-audit-v0-1`;
- GitHub artifact digest and independently downloaded ZIP SHA256 both `e95c4675db77a2ecd864d21e39dfdccffe289ed61a84ece95182f22c46e16184`.

Inner files independently rechecked:

- `launch_package_static_audit.json`: 1,348 bytes, SHA256 `133df1d2753c9228198a15be792fdcbbf99da243efeccdb785d610aad7dc5ee5`;
- `launch_package_static_audit.sha256`: 104 bytes, SHA256 `d02e8c9ad2950885bef4cb9d926d42e35cfbb8ac4ad0b7632874d700af82320f`;
- `future_W_exact_copy.yml`: byte SHA256 `1d8de6326efb9de2cf0d0ed9c6107221820e8158b3a6b9ee99606227173457c4`, git blob remains `19907175f0f3417ddee2aba6916d961c6be02e26`;
- `future_A_exact_copy.json`: byte SHA256 `b9b6b57f898b4abd089bb30a7def3542625a653e0737abd5d6c7a80bd0f6b549`, git blob remains `4ba40e59e6a9d48636d95d07efab575e56ae0966`;
- `future_L_exact_copy.json`: byte SHA256 `bcc4ec835d504fa5bc64fbedd3d7ad98a5fd9744e19f41ce081ec9fe7ded8223`, git blob remains `9c217e41764d979bea12644fae372354241bc976`.

Receipt classification:
`SENTINEL_LAUNCH_PACKAGE_ACYCLIC_RESPONSE_BLIND_STATIC_AUDIT_PASS`.

Receipt token:
`PASS_LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_STATIC_AUDIT_PLUS_0_PLUS_0`.

Receipt confirms:

- `A_binds_W=true`, `A_binds_L=false`;
- `L_binds_A=true`, `L_binds_W=true`;
- provenance topology `W_TO_A_TO_L_THEN_Q`;
- future active W absent;
- future authority A absent;
- future trigger L absent;
- future Q absent;
- one-run new-file trigger guard present;
- first-attempt guard present;
- unique exact-head workflow-run guard present;
- Q runtime gate present;
- `class_solver_invoked=false`;
- `scientific_response_read=false`;
- `sentinel_science_execution_authorized_by_this_receipt=false`;
- `full_107_row_execution_authorized=false`.

## Interpretation

This is static launch-package evidence only. It does not authorize promotion of W/A/L to active/final paths and does not authorize a sentinel CLASS solve.

Next admissible gate: independent external funnel audit of exact package code/contract/static-run provenance. If qualified, a separate Q authority may then be constructed from that audit, and exact W/A may be staged without L. The final exact L creation remains a later, explicit one-run trigger and must not occur before the package qualification authority exists on main.
