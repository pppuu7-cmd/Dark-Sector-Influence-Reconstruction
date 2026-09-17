# DSIR Funnel Auditor — cross-host GRID896 diagnostic implementation successor V0.6 static audit

Date: 2026-09-17. Scope: DSIR only. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

Reviewed main: `ea517eaa3b5ab7329d694bb80a612ec33eaa35ad`.

Reviewed exact frozen V0.6 identities:

- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_6.py`, Git blob `eae9eee7ae6a1424bcac67279663a2c8ddd3ebf9`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-6.yml`, Git blob `832f0491421619579c2a1d77ba9ca339cb4898ac`;
- implementation manifest `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_MANIFEST_V0_6.json`, Git blob `e71d2c92a56555ffaea59a08c80d8f073c4b48da`.

Governing frozen design remains preregistration blob `903c80709439cb790bd41316029b218a77d5695b`, machine contract blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`, canonical source blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`, and terminal preexecution confirmation blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715` (`CONFIRMED_SCOPED`). Terminal parent V0.5 qualification remains blob `581759b3230bf6bd8491ca60d843857a5749e76a`, verdict `INVALID_IMPLEMENTATION`, classification `GRID896_DIAGNOSTIC_SUCCESSOR_V0_5_EXECUTING_WORKFLOW_IDENTITY_NOT_BOUND`.

## Authorization and chronology

V0.5 terminal authority authorized only prospective inert V0.6 authoring with exact executing-workflow identity binding followed by a fresh independent static audit. V0.6 was frozen before this audit in separate commits: executor `eedec65125fe3de2c1a9fcd9f519297b006853ad`, workflow `2797e82252d81f77ccd5b9723e7f55cf6068b75b`, manifest `59bb22344ca04e90035b089375c3d896ed81d1df`; recovery/process/handoff followed. No response-dependent threshold, lane, scientific object, tolerance, PASS/FAIL/BLOCKED/INVALID rule, or interpretation ceiling changed.

At review time the active V0.6 workflow path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-6.yml` is absent, the future V0.6 execution-authority path is absent, and the V0.6 launch marker is absent. Repository Actions has zero queued runs and zero in-progress runs. Therefore no V0.6 execution result or partial substantive value exists or was used.

## Independent code review

The exact V0.6 source closes the deterministic V0.5 alias-workflow counterexample. `current_actions_workflow_identity()` queries the live current run by `GITHUB_RUN_ID` and fail-closed cross-checks API/environment run id, run number, attempt, event, head SHA and main branch. It requires the run API `path` to equal the exact canonical promoted workflow path, requires exact `GITHUB_WORKFLOW_REF`, resolves the run `workflow_id` through the Actions workflow registry, and requires that registry object to have the same exact path and `active` state.

`verify_launch_authorization()` additionally requires the future terminal execution authority to bind a positive `promoted_workflow_id`, the exact canonical promoted path, exact executor/workflow blobs, and explicit workflow-identity/alias prohibitions. The current run's workflow path and workflow ID must equal those authority-bound values. Lane receipts persist the resulting workflow path/id/ref/registry state and aggregate recomputes the same live identity before accepting any receipt.

### Alias-workflow negative control

A byte-identical workflow copied to a different `.github/workflows/...` path cannot create admissible PASS/FAIL evidence. Its run API `path` differs from the canonical active path, so `current_actions_workflow_identity()` raises before canonical GRID896 byte operations. Lane code catches that authorization failure and writes an `INVALID_DIAGNOSTIC_PROVENANCE` receipt; the workflow uploads the receipt under `always()`. The decision job remains reachable on push/main, independently reruns aggregate identity binding, writes an INVALID decision, uploads it under `always()`, and reflects non-PASS as workflow failure. Thus the V0.5 two-workflow/run-#1 counterexample is prospectively closed.

A canonical-path run whose workflow ID differs from the authority-bound promoted ID is also rejected. `GITHUB_WORKFLOW_REF` mismatch, registry path mismatch, registry state other than `active`, API/environment run-number or attempt mismatch, event mismatch, head-SHA mismatch, or non-main head branch all fail closed before lane byte evaluation.

## Preserved independent controls

V0.5 duplicate/rerun reachability survives: lane jobs execute only for push/main + run #1 + attempt #1, while the decision job deliberately omits run-number/attempt gating and uses `always()` with the lane matrix as a dependency. Aggregate immediately classifies any non-1 run number or non-1 attempt as INVALID and still writes/uploads the decision.

V0.4/V0.5 first-parent chronology survives: checkout depth 2; checked-out `HEAD == GITHUB_SHA`; exactly one parent; terminal execution authority and exact promoted workflow must preexist unchanged in `HEAD^`; launch marker must be absent in `HEAD^`; first-parent launch diff must be exactly one added launch-marker path. Therefore authority/workflow creation or modification in the launch commit, preexisting marker, merge launch, or extra launch-commit changes are rejected.

The exact scientific-blind byte controls are unchanged: canonical source requires 897 lowercase u64hex words and frozen source SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`; producer uses unsigned-u64 parse plus fixed little-endian eight-byte packing only; payload length 7176 and SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; consumer performs `<d` binary64 decode followed immediately by `<d` reserialize without arithmetic; frozen one-bit corruption SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800` must be rejected.

Artifact/provenance logic remains fail-closed: exact lane artifact names only, unique ids/names, no extras, API artifact digest must equal independently computed downloaded ZIP SHA256, ZIP must contain exactly one expected lane receipt, inner receipt SHA256 is recorded, artifact run/head are bound, current-run jobs are rebound to exact `GRID896 R01..R32` names, and receipt run/job/event/ref/code/workflow/launch/workflow-identity fields must match aggregate-recomputed provenance.

Classifier precedence remains prospective and response-independent: present malformed/digest-invalid evidence raises INVALID before population BLOCKED; an established present frozen FAIL is preserved before missing-population BLOCKED; complete PASS requires exactly 32 present and provenance-valid all-PASS lane receipts. No CLASS import/solve, scientific response, covariance, whitening, nuisance, relation-null, `Wm_S3`, global65537 or downstream science object is accessed.

## Alternative explanations / counterexample search

The former explanation "a second byte-identical workflow identity can independently be run #1/attempt #1 and pass" is no longer viable for the exact V0.6 source because run path, workflow ID, workflow ref and workflow-registry path/state are all bound to the current Actions run and future authority.

The previously identified V0.1 consumer-roundtrip defect, V0.2 classifier precedence defect, V0.3 launch-chronology defect, V0.4 rerun-decision reachability defect and V0.5 executing-workflow identity defect remain historical and are not rewritten. Their corrective controls are all present in V0.6.

No new deterministic source-level counterexample was found within the **authorized future sequence** frozen by V0.6: exact-byte promotion first; capture the GitHub-assigned workflow ID; separately author/review a terminal execution authority binding the exact audited executor/workflow and promoted workflow ID; only then create a marker-only one-shot launch commit. This audit does not certify behavior outside that authorized sequence and does not authorize an execution authority or launch.

## Interpretation ceiling

This is a static implementation/provenance result only. It does not establish cross-host PASS, numerical response reproducibility, exact-target/scientific validity, statistical/model validity, nuisance removal, identifiability, or physical dark-sector evidence. Scientific effect remains `+0/+0`; full107 and every downstream science gate remain closed.

## Verdict

**CONFIRMED_SCOPED**.

Classification: `GRID896_DIAGNOSTIC_SUCCESSOR_V0_6_STATIC_IMPLEMENTATION_CONFIRMED_FOR_EXACT_BYTE_PROMOTION_ONLY`.

The exact frozen V0.6 executor/workflow/manifest survive independent static falsification in the reviewed scope. The only newly authorized next stage is exact-byte promotion of the audited inert workflow candidate to the canonical `.github/workflows/...v0-6.yml` path **without launch**. Promotion itself is not execution authority. After promotion, a fresh independent review must verify the active workflow blob, GitHub-assigned workflow ID/path/state, zero V0.6 run history, and exact linkage back to this static confirmation before any terminal execution authority may be authored. No launch marker or diagnostic execution is authorized by this review.
