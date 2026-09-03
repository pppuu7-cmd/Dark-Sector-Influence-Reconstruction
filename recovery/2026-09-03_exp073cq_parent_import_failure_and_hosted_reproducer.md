# Exp073CQ parent-import failure forensics — 2026-09-03

DSIR only. Repository/checkpoint/action authority outranks chat.

## Terminal Exp073CQ v0.1

Workflow run `33742582807`, launch/head `ef4f02f0ff3e23d845b6dcd1f45317a0d3811b12` is terminal FAILURE.

- authorize job `100607659399`: SUCCESS.
- self-hosted job `100607697336`: FAILURE.
- runtime lineage/bootstrap/successor init: completed before failure.
- first noncompleted step: `Exact import of immutable Exp073CP band0-28 authority`.
- helper compile, numerical bands 29..38, telemetry, frozen final classification and authority artifact: NOT RUN.
- decoded job-log endpoint currently returns `BlobNotFound`; no exact stderr/exception is available and no lower-level cause is inferred.
- successor namespace `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-1` is absent remotely after terminal failure, therefore no CQ completed parent-import stage or numerical unit is durable authority.
- immutable Exp073CP parent checkpoint remains `025629d9bb7b113bd0548ff6a32c6ee5812ae245`, with exact complete bands 0..28 and parent fingerprint `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`.
- classification: `INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_PARENT_IMPORT`, Article-3 `+0/+0`; NOT scientific FAIL and NOT resource/performance FAIL.

No home rerun is authorized.

## Fail-closed next diagnostic

Hosted-only parent-import reproducer workflow was added at commit `76e15bf0af35965c99d7748f49bfdc6c8e699586` and launched by commit `de0c4e89432814875ac4dce687d6799c7e1e239e`.

Run `33752333426`, job `100638517360` reproduces, read-only, the exact parent restore at head `025629d9...`, CQ contract init using frozen v0.1 lineage, `import-parent`, and CQ validation. It performs no home computation and cannot create Wm_S3 scientific authority. Expected diagnostic token is `PASS_EXP073CQ_HOSTED_PARENT_IMPORT_REPRODUCER_V0_1`.

If this hosted reproducer fails, consume its first causal error and repair that exact defect prospectively. If it passes, CQ v0.1 import logic is reproducible on a clean hosted runner and the terminal home failure remains environment/transport-specific unless later logs prove a narrower cause; any future home continuation must be a new prospectively audited version with durable import-stage checkpointing before numerical work.
