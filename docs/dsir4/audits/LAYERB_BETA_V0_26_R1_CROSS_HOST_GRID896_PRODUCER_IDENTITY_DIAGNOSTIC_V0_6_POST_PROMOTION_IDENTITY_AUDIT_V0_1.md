# DSIR Funnel Auditor — GRID896 V0.6 post-promotion workflow-identity audit

Date: 2026-09-17. Scope: DSIR only. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

Reviewed main at audit start: `24fd6b33bef60c16d3afcdd67af769568116d0c2`.

## Gate under review

Terminal static confirmation `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_STATIC_AUDIT_CONFIRMATION_V0_6.json`, blob `6cc317eb359a820bc1ecb3c657fc33b46a7d152b`, authorized one action only: exact-byte promotion of workflow candidate blob `832f0491421619579c2a1d77ba9ca339cb4898ac` to canonical active path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-6.yml`, followed by an independent post-promotion workflow-identity audit before any execution authority or launch marker.

The Researcher promotion commit is `3cd2ab71e490bc2ccbea0a8a8c3527d0e25c0a9d`. Its diff adds only the canonical active workflow file. Direct current-main reads show both candidate and active workflow have exact git blob `832f0491421619579c2a1d77ba9ca339cb4898ac`.

## Repository identity checks

The frozen V0.6 identities remain unchanged on current main:

- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_6.py`: blob `eae9eee7ae6a1424bcac67279663a2c8ddd3ebf9`;
- workflow candidate: blob `832f0491421619579c2a1d77ba9ca339cb4898ac`;
- canonical active workflow: blob `832f0491421619579c2a1d77ba9ca339cb4898ac`;
- implementation manifest: blob `e71d2c92a56555ffaea59a08c80d8f073c4b48da`;
- terminal static confirmation: blob `6cc317eb359a820bc1ecb3c657fc33b46a7d152b`.

The V0.6 manifest explicitly requires a future terminal execution authority to bind a positive promoted GitHub workflow ID, exact canonical path and registry state before marker creation. The executor independently re-queries the current Actions run and then the workflow registry by `workflow_id`, requiring the registry id to match, registry path to equal the canonical active path, and registry state to equal `active`.

## No-execution boundary

The future implementation execution-authority path remains absent on current main. The V0.6 launch-marker path remains absent on current main. Exact promotion-head Actions enumeration for `3cd2ab71e490bc2ccbea0a8a8c3527d0e25c0a9d` returns zero runs. Current repository queued count is zero and in-progress count is zero. The latest repository workflow run visible in Actions predates the V0.6 promotion. No V0.6 diagnostic artifact, lane receipt or decision exists, and no partial diagnostic/scientific value is used in this review.

## Independent identity finding

Repository-level promotion provenance is confirmed: the active file is the exact audited byte identity, the promotion was separately authorized, and no launch/execution object exists.

However the post-promotion workflow-identity gate is **not terminally confirmable from the durable evidence currently present**. The promotion record intentionally stores `github_assigned_workflow_id: null`, `registry_path: null`, `registry_state: null`, and `independent_post_promotion_review_complete: false`. Because the promoted workflow has never run, run history provides no current-run `workflow_id` from which to cross-check the registry. No durable raw Actions workflow-registry snapshot or equivalent signed/hashed receipt currently binds a positive GitHub-assigned workflow ID to the canonical path and `active` state.

This missing binding cannot be replaced by inference from the filename, by guessing a numeric workflow ID, by active-file blob equality, or by a later launch run. The purpose of V0.6 is specifically to prevent a byte-identical alias or unexpected registry identity from becoming admissible evidence. Authoring an execution authority without independently observed registry identity would bypass the newly frozen V0.6 control.

## Counterexamples that remain open until registry capture

1. The repository file can be byte-correct while the Actions registry entry is disabled/non-active.
2. The repository file can be byte-correct while the registry path/identity does not match the canonical path expected by the executor.
3. A guessed or inferred workflow ID can be wrong while every repository blob check remains green.
4. Zero run history proves non-execution, but cannot by itself prove the positive registry id/path/state tuple required by the frozen implementation.

These are provenance/infrastructure counterexamples only. They do not alter GRID896 scientific thresholds, population, binary64/hash semantics, or any historical scientific result.

## Required confirmation gate

Before any V0.6 execution authority is authored, obtain a read-only GitHub Actions workflow-registry record for the canonical active workflow and persist enough durable evidence to independently bind:

- positive GitHub-assigned workflow ID;
- exact path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-6.yml`;
- registry state exactly `active`;
- current active file blob `832f0491421619579c2a1d77ba9ca339cb4898ac`;
- exact linkage to static confirmation blob `6cc317eb359a820bc1ecb3c657fc33b46a7d152b`;
- zero V0.6 run history before authority creation;
- continued absence of launch marker and execution authority during the capture/review itself.

Prefer persisting the raw registry JSON or an exact canonicalized copy plus SHA256/provenance, followed by an independent review. Do not use a launch as the mechanism for discovering the workflow ID because that would invert the frozen gate chain.

## Interpretation ceiling

Infrastructure/provenance/static implementation only. Scientific effect remains `+0/+0`. Numerical response reproducibility, exact-target/scientific criteria, covariance, whitening, nuisance marginalization, relation-null, statistical/model validity, identifiability and physical dark-sector inference remain `NOT_EVALUATED` or closed. Full107 and all downstream science remain closed.

## Review result

Verdict: **REQUIRES_CONFIRMATION_GATE**.

Classification: `V0_6_POST_PROMOTION_REPOSITORY_IDENTITY_CONFIRMED_BUT_GITHUB_WORKFLOW_REGISTRY_ID_PATH_STATE_NOT_DURABLY_BOUND`.

The exact-byte promotion survives review in its authorized scope. The post-promotion identity gate does not yet authorize execution-authority creation because the mandatory positive GitHub workflow registry identity remains unbound in durable evidence.
