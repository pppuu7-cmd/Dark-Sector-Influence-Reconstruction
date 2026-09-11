# RECOVERY V135 — Article III 32769 runner-registration provenance gate

Date: 2026-09-11. Scope: **DSIR Article III only**. V134 and all earlier recovery notes remain immutable history.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

No 16385->32769 scientific execution is authorized or has occurred. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

Frozen scientific semantics remain unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, the same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup mismatch `<=1e-12`.

## V135 finding
The V134 isolation contract correctly required a future runner configured with `--no-default-labels` and only the dedicated `dsir-32769-highmem` routing label, but the measured-resource provenance chain did not itself prove that the executing runner had been configured that way. The candidate packager retrieved source job metadata but used the source job only for exact identity/status/conclusion; no registration receipt was bound into the independent resource evidence.

This was an evidence/provenance gap, not a scientific-core defect.

The old queued superseded run `34550495778`, job `103112190909`, still targets `[self-hosted, Linux, X64]`. The current 32769 source workflow routes only to `[dsir-32769-highmem]` and continues to fail closed if the stale job is observed `in_progress`.

## Frozen configurator
New script: `scripts/dsir4/configure_layerb_32769_highmem_runner_v0_1.sh`.

Creation commit: `47b556204054c3730d0272e442bebe7239e1b1d4`.

Git blob: `7489deb49b86245cf399d8020b9ac4fdfcac9278`.

SHA256: `2cd02d1a7ac58ea3945a435272f03ea1abe2d7e3410191b5a17a9c62e0a297ce`.

It refuses an already configured runner root and invokes `config.sh` with exactly:
- a caller-supplied fresh registration token and exact repository URL;
- a caller-supplied unique runner name;
- work directory `_work`;
- `--labels dsir-32769-highmem`;
- `--no-default-labels`;
- `--unattended`.

Only after successful runner configuration it writes `.dsir32769-registration-receipt.json`. The receipt contains the runner AgentId/AgentName, exact configured label set, `no_default_labels=true`, configurator SHA256 and frozen isolation-contract blob. It explicitly records that registration token/credentials are not recorded and contains no scientific authorization.

## Strengthened measured-resource source workflow
`.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-2.yml` remains the canonical path/name but is superseded in-place from old blob `8ec0027d6fb45f3f12aa5f410de62093a7144924` to current blob `3297a556299daf75e4c7ff15f8e56586e45ebdf0`, update commit `e44f343675736fa72c6f4ec6fccf1eb7a8cd3b32`.

The scientific/resource core blobs remain unchanged. Before resource computation the workflow now:
1. verifies the exact configurator SHA256 and frozen isolation contract;
2. loads the sanitized local registration receipt and current `.runner` AgentId/AgentName;
3. queries the current workflow run's jobs through the Actions API;
4. binds the exact `resource-lifecycle-pilot` job `runner_id` and `runner_name` to the registration receipt/current runner settings;
5. requires current job routing labels to be exactly `[dsir-32769-highmem]`;
6. writes a sanitized `source_job_runtime.json`;
7. hashes both registration/runtime receipts into `result.json` as `runner_registration_receipt_sha256` and `source_job_runtime_sha256` with `runner_registration_evidence_valid=true`.

The uploaded source artifact now contains both sanitized receipts in addition to the pre-existing response-blind resource evidence.

## Registration-aware independent consumer
New consumer: `ci/layerb_32769_resource_lifecycle_independent_consumer_v0_2.py`, creation commit `972ecd79b096135d9bdbbac64780c4a133b6f0f4`, Git blob `e08f15394ba3b16222b62d061a621e24f3a857ec`.

The event-chain workflow remains named/path-compatible with V132 packaging but now pins consumer V0.2 and source workflow blob `3297a556...`; current workflow blob `a68148e6826cda223368f8a624014a873cd1dc44`, update commit `86295a8bd6aed398e31868e459c5505053e5630d`.

Consumer V0.2 independently requires and checks:
- exact frozen configurator SHA256;
- exact isolation-contract blob;
- exact single configured custom label and `no_default_labels=true`;
- no registration token/credentials in the receipt;
- receipt AgentId/AgentName validity;
- current source job runner_id/runner_name equality with receipt identity;
- exact dedicated routing labels;
- source `result.json` SHA bindings to both receipt files;
- all previously frozen capacity, canonical, memory-ordering, lifecycle, response-blind, stale-job and telemetry checks.

Its PASS classification remains `LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0`, so the existing V132 packager/materializer interface remains compatible: it consumes classification/valid/errors plus the exact independent-validation SHA binding, not a frozen old schema name.

## Independent audit
Audit workflow `.github/workflows/layerb-32769-runner-registration-evidence-audit-v0-1.yml`, creation commit `2745e2b5b0773bc8164a4cb20b923bd756168bd0`, Git blob `c544881cf93c060bb8e2cbd722505a662214736a`.

Run `34645311690` passed:
- synthetic consumer job `103414563351`;
- static source-workflow job `103414563197`;
- independent verifier `103414777148`.

Synthetic artifact `10281202698`, ZIP SHA256 `8206c140aefba57a892ab4adb366bf315b8477c911fc78f4850c2b7b163b4fa0`; PASS receipt SHA256 `b4dd200a7437158800fc8074dcf0bcf80e1478d61b58822463f26482a2988225`; summary SHA256 `6564deb28e9ce66129f5e040ede9095cd2eeb9fc75f4dce2da30608956273349`.

Static artifact `10281867381`, ZIP SHA256 `7e7cf6b1ffc31c8ed23bde5aae891f1572c63ec17d20eab03e55446de2bc2d6b`; static receipt SHA256 `d58b9fcc2273ca66485de02b298a212d28930b5a337fc694bec0b3d24dcd9543`.

The exact valid registration-bound fixture passed. The audit independently rejected `no_default_labels=false`, wrong configurator SHA, an added generic `self-hosted` label, runner-id mismatch and routing-label substitution. Static audit confirmed the scientific/resource core blobs remained unchanged.

Durable V135 authority: `docs/dsir4/authority/LAYERB_32769_RUNNER_REGISTRATION_PROVENANCE_AUDIT_V0_1.json`, creation commit `6c6d9e82db30a5dadc5295b7e615822730df1a49`.

## Remaining true blockers
1. Configure/attach a real high-memory runner **using the V135 frozen configurator**, under a unique new runner name, with physical `MemTotal > 16372440 kB`.
2. Dispatch exactly one response-blind V0.2 measured 32769 lifecycle pilot; its source artifact must carry real V135 registration/runtime evidence.
3. Hosted independent consumer V0.2 must PASS and the existing candidate-packaging chain must produce a real candidate.
4. The real candidate must pass V133 exact-byte promotion review and the reviewed bytes must be deliberately copied to the durable resource-authority path.
5. Actual immediate one-live guard and current-run-only one-run authorization must PASS.
6. Only then exactly one canonical scientific 16385->32769 run may execute, followed by independent terminal classification.

## Automation state correction
`DSIR Continuous Research` is currently **disabled**. V134's statement that it remained enabled hourly is stale and is superseded by this recovery note. It was not re-enabled automatically in V135.

## Readiness
Frozen publication rubric remains **ARTICLE3_REPOSITORY_READINESS: 68%**.

Funnel-freeze/scientific frontier remains **67%**.

Operational roadmap tracking becomes **WORKING_PLAN_COMPLETION: 84%** because V135 closes a real runner-registration provenance gap. No scientific readiness increase is claimed.

## Exact next action
Use the frozen configurator to create the dedicated high-memory runner, start that runner, and then dispatch exactly one current V0.2 response-blind lifecycle pilot. Do not run canonical 16385->32769 science before measured resource evidence, durable resource authority, live guard and one-run authorization exist.
