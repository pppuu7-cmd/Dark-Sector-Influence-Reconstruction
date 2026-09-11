# DSIR recovery V127 — Article III 32769 CLASS capacity prerequisite closed

Date: 2026-09-11. Scope: **DSIR only**. RTK/RQIR/KMQGB/KMDSB excluded.

## Scientific frontier
Unchanged. Canonical 8193->16385 remains independently classified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific response was executed or read in V127. Covariance restriction remains unauthorized and Wm_S3 remains closed.

## Newly closed in V127
The 32769 CLASS capacity-only build prerequisite is now frozen and independently validated.

Source workflow:
- workflow: `.github/workflows/layerb-32769-class-capacity-build-audit-v0-1.yml`;
- workflow Git blob: `688704a24c6219a76f7817ddfd17479f0adb4c98`;
- workflow head/creation commit: `a8347b14cea754448960e0bc51ae35b7851bd9cd`;
- run: `34632293214`;
- build job: `103371777163` — SUCCESS;
- independent consumer job: `103372066383` — SUCCESS.

Pinned CLASS source remains exactly `ac627d54e9ce196a08878d1ba33999819925d19c`.

The audit reconstructed both the previously validated capacity-18432 tree and the candidate capacity-32769 tree from the same pinned source, applied the same compatibility/public-exposure/setup patches to both, and required exact source-tree equivalence except for one capacity constant. The only old-vs-new changed file was `include/perturbations.h`, with the exact line change `_MAX_NUMBER_OF_K_FILES_ 18432` -> `32769`. Parser capacity remained `524288` and parser headers were byte-identical between the reconstructed trees after the same parser patch.

New build:
- capacity: `32769`;
- parser capacity: `524288`;
- clean build: PASS;
- CLASS executable size: `3072920` bytes;
- CLASS executable SHA256: `9958099b0a45f364affabe46d4fd32568db5d4867bc48b82a9b3170ae351203d`.

Source artifact:
- artifact id: `10276911032`;
- ZIP SHA256: `5e59eb4d1020bcb06adbe932bf9dca31867741d7ff989ff24b34c85052f440e1`;
- `build.json` SHA256: `9080212ad6523fd95772b170c689ab7d63b51d1656b0c9e286a3b3f30465b96e`;
- classification: `LAYERB_32769_CLASS_CAPACITY_BUILD_PASS_PLUS_0_PLUS_0`.

Independent consumer:
- artifact id: `10276239911`;
- ZIP SHA256: `a35f9db309a81f3a617e318ba74b471c0567799b576bb6f813db7e205927be34`;
- `result.json` SHA256: `326417b0f814e803e1aae03300defc04c9644f98087e3fca2762e9ddbf16c35c`;
- classification: `LAYERB_32769_CLASS_CAPACITY_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0`.

Durable authority:
`docs/dsir4/authority/LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_V0_1.json`, creation commit `e791ab69e014a225d24d532dcdc94899687ccbe6`, Git blob `ec773d9f5cbed652c52c52b5a4fae74efd5ecd0d`.

Therefore the following preflight conditions are now closed:
- `CLASS_32769_CAPACITY_BUILD_AUDIT_PASS = TRUE`;
- `PARSER_BUILD_PARITY_AUDIT_PASS = TRUE`;
- `SCIENTIFIC_EQUIVALENCE_STATIC_AUDIT_PASS = TRUE`.

They remain support-only `+0/+0`; `32769_EXECUTION_AUTHORIZED = FALSE`.

## Resource/lifecycle front
Ordinary GitHub-hosted `ubuntu-24.04` remains inadmissible as an inferred production topology. Existing canonical 16385 authority observed memory exhaustion in all four roles at approximately 15.4--15.7 GB Python RSS. A separate history-suppressed 16385 resource pilot reached roughly 8.98--9.23 GB with max one live instance, but that narrower resource-only success is not promoted or extrapolated to 32769.

A stale self-hosted 16385 resource run `34550495778 / 103112190909` remains queued/superseded. It must not be treated as current 32769 authority or receive production ownership. The next high-memory gate requires a new response-blind 32769-specific resource/lifecycle contract with exact host-memory telemetry and no scientific-response classification.

## Remaining authorization prerequisites
Still FALSE/open:
- `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS`;
- `ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS` (must be re-proven immediately before any production dispatch);
- `TERMINAL_SCHEMA_AND_INDEPENDENT_CONSUMER_FROZEN`.

Only after all remaining prerequisites close may a separate one-run 16385->32769 scientific authorization be created.

## Readiness
Frozen repository/publication rubric remains:
- `ARTICLE3_REPOSITORY_READINESS = 68%`;
- funnel-freeze readiness = `67%`.

For execution tracking against the user-approved remaining-task roadmap, the CLASS-capacity/parity/equivalence block has advanced from open to closed, so `WORKING_PLAN_COMPLETION = 73%`. This working-plan number is operational progress only and does not silently rewrite the frozen publication-readiness rubric.

## Exact next action
Prepare and freeze a **32769-specific response-blind high-memory resource/lifecycle pilot** and its terminal schema without dispatching scientific convergence. Because the stale 16385 self-hosted run is still queued/superseded, do not grant it authority or reuse it as the new gate. In parallel, freeze the future scientific terminal-result schema/independent consumer where this can be done without observing any 32769 scientific response.
