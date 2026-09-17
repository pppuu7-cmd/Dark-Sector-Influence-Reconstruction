# DSIR Funnel Auditor — GRID896 diagnostic implementation successor V0.3 static audit

Date: 2026-09-17. Scope: DSIR only. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

Reviewed main at audit start: `6b761a292ebaeb9712449a960fceafa3cfec3666`.

Reviewed exact frozen V0.3 identities:

- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_3.py`, Git blob `af1bc1e76338d6019bfa0fdde025d4ea17bd57ee`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-3.yml`, Git blob `63113da2c0091473482e833a5c766b904be3244a`;
- implementation manifest `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_MANIFEST_V0_3.json`, Git blob `e87f7ad25a4be9a499d1b8546504059cbeaaf087`.

The active workflow path and V0.3 launch marker were absent from `main` at review. No queued or in-progress Actions runs existed. No diagnostic execution or science object was used in this review.

## Authorization and preregistration chronology

V0.3 was prospectively authored only after terminal V0.2 static-audit qualification `effd843587442f1c7bb3e9d7ae1c7ae6a8afd618`. The frozen cross-host design remains preregistration `903c80709439cb790bd41316029b218a77d5695b`, contract `6ba6e5a6c946a1091680f8f44821d323c9a463f3`, canonical source `24fa61685ab45e42e3ab0d453f5cb223c247ced6`, and terminal preexecution confirmation `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`.

No scientific threshold, denominator, tolerance, sampling rule, PASS/FAIL criterion, or interpretation ceiling changed. V0.26 R1 science remains closed.

## V0.2 counterexamples — corrected

The exact V0.3 aggregate no longer short-circuits `total_count < 32` before reading present evidence. It enumerates current-run artifacts, rejects duplicate/extra/malformed/digest-mismatched present evidence before population BLOCKED, validates each present expected receipt, preserves an established frozen FAIL before incomplete-population BLOCKED, and permits PASS only for complete exact-32 all-PASS evidence.

Therefore the two terminal V0.2 counterexamples are prospectively corrected at source level:

1. one valid FAIL plus one missing infrastructure lane reaches FAIL rather than BLOCKED;
2. one present malformed/digest-invalid artifact plus missing lanes reaches INVALID rather than BLOCKED.

The binary64 decode/immediate little-endian reserialization, canonical 897-word/source/payload guards, frozen one-bit negative control, exact 32-lane topology, run #1 / attempt #1 checks, absence of `workflow_dispatch`, cryptographic Actions artifact ZIP/API digest check, inner receipt SHA256, run/head/job/code binding, and no-CLASS/no-science boundary are also preserved.

## New deterministic counterexample — launch-authority chronology is not fail-closed

The frozen preexecution authority requires the sequence: exact executor/workflow frozen without launch -> independent static prelaunch audit -> only a later terminal implementation authority may authorize one diagnostic run. The runtime implementation does not enforce that ordering.

`verify_launch_authorization()` checks only the **current checkout** for:

- existence of the future implementation-authority path;
- selected authority fields (`status`, `verdict`, `diagnostic_execution_authorized`, executor/workflow/preexecution blobs);
- existence of the active workflow exact-copy path;
- existence of a launch marker whose selected fields bind the current authority/executor/workflow blobs and run-number/attempt/lane-count values.

It does not check that the terminal implementation authority and promoted active workflow already existed in the first parent of the launch-marker commit. It does not require the launch-marker commit to add only the marker, does not inspect `HEAD^`, and the workflow checkout uses `fetch-depth: 1`, so the candidate has no runtime first-parent chronology control.

Concrete counterexample after a byte-exact active workflow has been promoted: a single push can add both (a) a newly authored JSON at the expected implementation-authority path containing the selected required fields and (b) the launch marker whose `implementation_authority_git_blob_sha1` is the blob of that same-commit JSON. The path-filtered workflow is triggered by the marker change. At runtime all current-tree checks in `verify_launch_authorization()` pass even though no implementation authority existed before the launch event. Thus the implementation cannot distinguish the required gate chain from a same-commit authority-plus-launch construction.

This is not a hypothetical scientific interpretation issue: it is a deterministic provenance/gate-chain implementation gap. The runtime currently proves *current-tree field consistency*, not `STATIC_AUDIT -> TERMINAL AUTHORITY -> PROMOTION -> LATER LAUNCH` chronology.

The same gap also means the launch marker is not bound to an exact first-parent diff. A marker can be created or modified in a commit that simultaneously changes other governance objects, while the frozen implementation still treats the run as authorized if the final tree satisfies the selected field checks.

## Why this invalidates execution readiness

The user-level funnel contract requires strict `OPEN -> PREREGISTERED -> EXECUTED -> VALIDATED -> TERMINAL AUTHORITY -> NEXT_STAGE` ordering and forbids gate skipping. The terminal preexecution confirmation likewise states that only a later terminal implementation authority may authorize one run. Because exact V0.3 permits a same-commit authority-plus-launch witness, the one-shot launch-authority control is not fail-closed to the frozen gate chain.

A green future diagnostic under this implementation could therefore have internally consistent blobs yet lack proof that execution was authorized by a terminal authority that predated the launch. That is an implementation/provenance defect, not a scientific result.

## Required prospective correction

Do not modify historical V0.3 blobs. A new inert successor must be prospectively frozen and independently audited before any promotion or launch. At minimum it must:

1. checkout enough history to inspect the first parent (`fetch-depth >= 2` or full history);
2. require the active workflow and exact terminal implementation authority to exist with their exact audited blobs in `HEAD^` before the launch-marker commit;
3. require the V0.3/V0.4 launch marker to be absent in `HEAD^` and added exactly in the triggering commit;
4. fail closed if the launch commit simultaneously creates/modifies the implementation authority or active workflow; preferably require the first-parent diff to contain exactly the launch marker and no other scientific/governance object;
5. bind the launch marker to the exact terminal implementation-authority blob and exact audited executor/workflow identities, while preserving run #1 / attempt #1 and no-rerun controls;
6. preserve all V0.3 classifier-precedence, binary64, hash, artifact-provenance, 32-lane, and no-science controls;
7. undergo a fresh independent static audit of the new exact blobs before promotion or launch.

## Validity layers and interpretation ceiling

Infrastructure/provenance/static implementation: V0.3 is not execution-ready because launch-authority chronology is not fail-closed.

Numerical/reproducibility validity: not evaluated.

Statistical/model validity: not evaluated.

Physical dark-sector inference: not evaluated.

Scientific effect remains `+0/+0`. No readiness/frontier increase is authorized. Full 107 rows, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, successor sentinel science and all downstream inference remain closed.

## VERDICT

`INVALID_IMPLEMENTATION`

Classification: `GRID896_DIAGNOSTIC_SUCCESSOR_V0_3_LAUNCH_AUTHORITY_CHRONOLOGY_NOT_FAIL_CLOSED`.

Authorized next stage: `AUTHOR_PROSPECTIVE_INERT_GRID896_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_V0_4_WITH_FIRST_PARENT_AUTHORITY_AND_LAUNCH_CHRONOLOGY_BINDING_ONLY`.
