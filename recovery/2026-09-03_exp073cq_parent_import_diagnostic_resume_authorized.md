# DSIR recovery — Exp073CQ audited parent-import diagnostic continuation authority

Date: 2026-09-03
Scope: DSIR only; RTK/RQIR excluded.
Classification impact: checkpoint/control/resource preparation only, `+0/+0`.

## Historical source state preserved
Exp073CP run `33726577654`, self-hosted job `100556826993`, remains `INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_COMPUTE_STAGE`, `+0/+0`. Frozen final comparator did not run and no authority artifact exists. The GitHub decoded job-log endpoint for `100556826993` was retried on this iteration and still returned `BlobNotFound`; the lower-level exception therefore remains unknown and is not guessed.

Parent durable authority is immutable checkpoint `checkpoints/exp073cp-wm-s3-full39-resource-v0-1` head `025629d9bb7b113bd0548ff6a32c6ee5812ae245`, parent fingerprint `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`. Exact tree audit confirms payload+receipt pairs exactly for bands `0..28`, with bands `29..38` absent. These verified expensive units MUST NOT be recomputed.

## Exp073CQ v0.1 prospective continuation
Preregistration commit: `60c975edb35c13bd22907440f4ed767a5fc55712`.
Driver commit: `b316354886e1b1857d6f205ffe5d0dd8f0151622`.
Home workflow commit: `76be666e2cc6b8f11710a44ff7772ef708ac1e80`.
Hosted audit workflow commit: `184dcd43526b87c26ed2fd0f22baa85a2451167f`.
Frozen implementation binding commit: `f8416855c7dd28b95d30cbf18835dd2b8bb37ddd`.
Checkpoint sync authority remains `ci/dsir_checkpoint_git_sync_v0_3.sh` commit `c20127b6762c6fc9b21875a321aecd7a4cd5f88e`.
Universal self-hosted policy remains commit `f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427`.

Successor namespace: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-1`.
Imported/read-only parent units: exactly bands `0..28`.
Numerical compute allowlist: exactly bands `29..38`.
Architecture: exactly 8 outer workers, maximum 8 in flight, nested numerical threading pinned to 1, exact complete-band durability, exact restore verification, no tolerance rescue, diagnostic first-exception capture, compiled-helper stage checkpoint, and exact final reassembly.

## Hosted audit authority
Hosted audit run `33742223874`, job `100606527087`, head `f8416855c7dd28b95d30cbf18835dd2b8bb37ddd`, completed SUCCESS. Authority is the immutable raw job log, which explicitly contains:
`PASS_EXP073CQ_STATIC_PARENT_IMPORT_DIAGNOSTIC_RESUME_AUDIT_V0_1`.

The audit verified exact implementation lineage, parent head/fingerprint, exact parent tree containing bands 0..28 only, import-only versus compute-only partition, 8/8/nested-1 scheduler architecture, CPU threshold `0.90`, launch-marker-only home trigger, checkpoint namespace and prospective diagnostic handling. Workflow green status alone is not used as the PASS authority; the raw token is required and was observed.

Activation authority commit: `5cfdf3fb2d41041eff0238718f7841edc8897640`, file `ci/exp073cq_wm_s3_missing29_38_resource_v0_1.activation.json`.

## Frozen resource outcome rule
Expected resource PASS token is `PASS_EXP073CQ_WM_S3_MISSING29_38_8WORKER_DIAGNOSTIC_RESUME_RESOURCE_V0_1`. Exact first-8 equivalence and frozen SHA, resumed compute CPU fraction >=0.90, zero positive swap increase, exact receipts and full 39-row canonical reassembly remain mandatory. Exact mismatch is numerical/resource FAIL; CPU or swap violation is resource/performance FAIL; restore/import/software/transport/control failure before final comparator is infrastructure/software/checkpoint incomplete. All outcomes remain Article-3 `+0/+0`.

No Wm_S3 angular scientific authority is created by this authorization. Full fresh-independent-PCL Wm_S3 A/B production remains forbidden until a resource gate actually PASSes.
